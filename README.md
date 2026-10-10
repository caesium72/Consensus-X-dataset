# NSIO-Benchmark — Provenance-Aware Hybrid Benchmark

**Current Zenodo record:** Version 1.0, DOI `10.5281/zenodo.23239670`  
**Corrected archive:** prepared locally for the next Zenodo upload; not yet part of the existing Version 1.0 record  
**Prepared archive build:** 5,000 controlled synthetic scenarios; 68 schema fields across nine categories (69 columns in the consolidated CSV including `split`).

## What this dataset is

NSIO-Benchmark is a provenance-aware hybrid benchmark for studying context-aware selection among blockchain and payment rails. Its 5,000 scenario rows are controlled synthetic configurations, not historical payment transactions. External source data are shared environmental/market observations or documented parameters; they were not collected separately for each scenario row.

The six rails represented are Ethereum, Polygon, Solana, Hyperledger Fabric, Hyperledger Besu, and Stripe. The four scenario domains are Healthcare, Retail, Payroll, and Supply Chain, with 1,250 configurations per domain in the prepared archive.

## Provenance categories

- **External observations:** dated values captured from public market/network pages.
- **Source-derived parameters:** information drawn from official technical documentation or published pricing.
- **Public-dataset metadata:** RPW catalog coverage and corridor-count metadata only.
- **Controlled synthetic scenarios:** scenario attributes such as amount, country pair, domain, urgency, privacy, modality, and intent.
- **Decision-derived outputs:** feasibility checks, utilities, selected rails, and modeled settlement estimates.
- **Evaluation-derived fields:** baselines and evaluation scaffold fields. SHAP-named fields in the prepared archive are proxies/placeholders, not empirical SHAP values produced by a trained model.

## World Bank RPW limitation

The two RPW ledger records describe catalog temporal coverage through 2025 Q1 and a catalog-reported count of 377 corridors, as captured during the documented retrieval. They do **not** contain individual provider remittance-price quotes, transaction-level remittance prices, or actual remittance transactions. They must not be described as observed transaction costs or as labels for benchmark scenarios.

## What is modeled or derived?

- Ethereum and Solana fee examples are calculated from captured values and documented fee rules.
- Utility and routing labels are produced by deterministic study rules; they are not independent gold-standard annotations.
- Fabric and Besu fee, latency, and throughput values are modeled parameters, not deployment-level measurements.
- The USD 10,000 KYC threshold is a study-defined synthetic rule, not a universal legal or FATF threshold.
- The current release does not report supervised model training.

## Files in the prepared corrected archive

The Zenodo-ready ZIP is organized as follows:

```text
NSIO-Benchmark-v2.0-Zenodo-FINAL/
  README.md
  CITATION.cff
  RELEASE_MANIFEST.json
  LICENSE_SELECTION_NOTE.txt
  annotations/README.md
  data/raw/source_observations.csv
  data/processed/nsio_benchmark_5000.csv
  data/processed/train.csv
  data/processed/validation.csv
  data/processed/test.csv
  data/processed/market_snapshots.csv
  data/processed/rail_capabilities.csv
  data/processed/NSIO-Benchmark-v2.0.xlsx
  data/metadata/source_registry.csv
  data/metadata/provenance.csv
  data/metadata/data_dictionary.csv
  data/metadata/collection_manifest.json
  data/metadata/quality_summary.json
  docs/DATA_COLLECTION.md
  docs/dataset_card.md
  references/references.bib
  scripts/README.md
```

The consolidated CSV has 69 columns: 68 schema fields plus the `split` partition indicator. The split CSVs omit `split` and contain 68 fields. In the consolidated CSV, the quality report counts 5,063 missing cells in total: 4,993 expected nulls for `rejection_reason` in non-rejected rows and 70 nulls across ten derived fields for the seven rejected rows.

## Reproducibility and generator

The original generator used to produce the existing benchmark rows was not recovered. Any newly supplied `generate_dataset.py` is an independently authored reconstruction from documented assumptions. It must not be described as the original script or as code that reproduces the existing rows exactly. Its outputs are a separate reconstruction unless documented row-level equivalence tests establish otherwise.

## Release/version note

The corrected ZIP named above has been prepared but had **not yet been uploaded** to Zenodo at the time this README was updated. Do not cite the current Version 1.0 DOI as if it already contained this ZIP. After upload, verify the new version-specific DOI, metadata, license, file list, row/column counts, and hashes.

## Citation

Cite the version-specific Zenodo record that actually contains the files used in your work. Repository: https://github.com/caesium72/Consensus-X-dataset
