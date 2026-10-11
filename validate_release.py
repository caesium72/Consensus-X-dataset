#!/usr/bin/env python3
"""Validate integrity and internal consistency of this release workspace."""

import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


DATA_ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = DATA_ROOT / "docs" / "reproducibility_manifest.json"


class ValidationError(Exception):
    pass


def fail(message):
    raise ValidationError(message)


def read_csv(relative_path):
    path = DATA_ROOT / relative_path
    try:
        with path.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            headers = reader.fieldnames
            if not headers or len(headers) != len(set(headers)):
                fail(f"Missing or duplicate CSV headers: {relative_path}")
            rows = list(reader)
    except OSError as error:
        fail(f"Cannot read {relative_path}: {error}")

    if any(None in row or None in row.values() for row in rows):
        fail(f"Malformed CSV row in {relative_path}")
    return headers, rows


def verify_manifest():
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Cannot read checksum manifest: {error}")

    if manifest.get("manifest_version") != 1:
        fail("Unsupported or missing manifest_version")
    if manifest.get("dataset_version") != "NSIO-Benchmark-v2.0-workspace-copy":
        fail("Manifest does not identify the inspected v2.0 workspace copy")

    expected = manifest.get("files")
    if not isinstance(expected, dict) or not expected:
        fail("Manifest contains no file checksums")

    actual_paths = {
        path.relative_to(DATA_ROOT).as_posix()
        for path in DATA_ROOT.rglob("*")
        if path.is_file() and path != MANIFEST_PATH
    }
    if actual_paths != set(expected):
        missing = sorted(set(expected) - actual_paths)
        extra = sorted(actual_paths - set(expected))
        fail(f"Manifest file inventory differs; missing={missing}, extra={extra}")

    for relative_path, details in sorted(expected.items()):
        path = DATA_ROOT / relative_path
        content = path.read_bytes()
        actual_hash = hashlib.sha256(content).hexdigest()
        if len(content) != details.get("size_bytes"):
            fail(f"Byte-size mismatch: {relative_path}")
        if actual_hash != details.get("sha256"):
            fail(f"SHA-256 mismatch: {relative_path}")
    return len(expected)


def verify_tables():
    master_headers, master = read_csv("processed/nsio_benchmark_5000.csv")
    if len(master) != 5000 or len(master_headers) != 69:
        fail("Master CSV must contain 5,000 rows and 69 columns")
    if "transaction_id" not in master_headers or "split" not in master_headers:
        fail("Master CSV is missing transaction_id or split")

    transaction_ids = [row["transaction_id"] for row in master]
    if any(not value for value in transaction_ids):
        fail("Master CSV contains an empty transaction_id")
    if len(transaction_ids) != len(set(transaction_ids)):
        fail("Master CSV contains duplicate transaction_id values")

    expected_splits = {"train": 3500, "validation": 748, "test": 752}
    split_counts = Counter(row["split"] for row in master)
    if split_counts != expected_splits:
        fail(f"Unexpected split counts: {dict(split_counts)}")

    scenario_headers = [header for header in master_headers if header != "split"]
    dictionary_headers, dictionary = read_csv("data_dictionary.csv")
    if len(dictionary) != 68 or "field_name" not in dictionary_headers:
        fail("Data dictionary must define 68 fields")
    if [row["field_name"] for row in dictionary] != scenario_headers:
        fail("Data dictionary fields do not match master CSV schema/order")

    seen_split_ids = set()
    for split_name, expected_count in expected_splits.items():
        relative_path = f"processed/{split_name}.csv"
        split_headers, split_rows = read_csv(relative_path)
        if split_headers != scenario_headers or len(split_rows) != expected_count:
            fail(f"Unexpected schema or row count in {relative_path}")

        expected_rows = [
            {header: row[header] for header in scenario_headers}
            for row in master
            if row["split"] == split_name
        ]
        if split_rows != expected_rows:
            fail(f"{relative_path} is not the exact master-table projection")

        split_ids = {row["transaction_id"] for row in split_rows}
        if len(split_ids) != expected_count or seen_split_ids & split_ids:
            fail(f"Duplicate or overlapping IDs in {relative_path}")
        seen_split_ids.update(split_ids)

    if seen_split_ids != set(transaction_ids):
        fail("Split files do not cover all master transaction IDs")

    selected_counts = Counter(row["selected_rail"] for row in master)
    if selected_counts != {"Fabric": 3743, "Besu": 1250, "REJECTED": 7}:
        fail(f"Unexpected selected-rail counts: {dict(selected_counts)}")

    feasible_counts = Counter(row["feasible"] for row in master)
    if feasible_counts != {"1": 4993, "0": 7}:
        fail(f"Unexpected feasibility counts: {dict(feasible_counts)}")

    observation_headers, observations = read_csv(
        "raw_external/source_observations.csv"
    )
    if len(observations) != 33 or len(observation_headers) != 7:
        fail("Observation ledger must contain 33 records and 7 columns")
    observation_ids = [row["observation_id"] for row in observations]
    if len(observation_ids) != len(set(observation_ids)):
        fail("Observation ledger contains duplicate observation IDs")

    market_headers, market_rows = read_csv("processed/market_snapshots.csv")
    if len(market_rows) != 4 or len(market_headers) != 10:
        fail("Market snapshots must contain 4 records and 10 columns")

    rail_headers, rail_rows = read_csv("processed/rail_capabilities.csv")
    if len(rail_rows) != 6 or len(rail_headers) != 8:
        fail("Rail capabilities must contain 6 records and 8 columns")


def main():
    try:
        file_count = verify_manifest()
        verify_tables()
    except ValidationError as error:
        print(f"Release validation failed: {error}", file=sys.stderr)
        return 1

    print(
        "Release validation passed: "
        f"{file_count} workspace files match the local SHA-256 manifest; "
        "table schemas, counts, and split projections are consistent."
    )
    print(
        "Scope: validates this workspace snapshot only; it does not regenerate "
        "scenarios or verify the Zenodo archive."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
