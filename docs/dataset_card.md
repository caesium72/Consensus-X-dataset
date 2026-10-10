# NSIO-Benchmark — Dataset Card (Prepared Release)

## Summary

- **Release state:** corrected ZIP prepared locally; not yet deposited on Zenodo.
- **Current Zenodo record:** Version 1.0, DOI [10.5281/zenodo.23239670](https://doi.org/10.5281/zenodo.23239670). This DOI does not identify the corrected prepared archive.
- **Prepared benchmark:** 5,000 controlled synthetic transaction scenarios.
- **Schema:** 68 fields in nine categories; the consolidated CSV has 69 columns including the `split` indicator.
- **Domains:** Healthcare, Retail, Payroll and Supply Chain, 1,250 scenarios each.
- **Settlement rails:** Ethereum, Polygon, Solana, Hyperledger Fabric, Hyperledger Besu and Stripe.
- **Evidence ledger:** 33 shared evidence records—23 external observations, eight source-derived parameters and two public-dataset metadata records.

## Intended use

Suitable for schema validation, provenance-aware data integration, controlled feasibility/routing experiments, utility-sensitivity analysis, deterministic pipeline regression tests and research on data lineage.

## Not intended for

The benchmark is not a source of historical payment events, observed user preferences, population-level transaction distributions, legal-compliance determinations or validated production-routing performance. Selected-rail labels are deterministic outputs of the documented rules, not independent gold-standard annotations. The current release does not report supervised model training.

## Data provenance

### External observations

The ledger contains public network and market snapshots from Etherscan, CoinGecko, DeFiLlama and PolygonScan. They are shared observations, not transaction-level measurements collected separately for each scenario.

### Source-derived parameters

Technical capabilities come from official Ethereum, Solana, Hyperledger Fabric and Hyperledger Besu documentation. Stripe's published domestic-card pricing is a source-derived pricing parameter, not a fee observed on a benchmark transaction. Fabric and Besu fee, latency and throughput estimates are modeled parameters rather than deployment measurements.

### World Bank RPW

The two Remittance Prices Worldwide (RPW) entries document catalog temporal coverage through 2025 Q1 and a catalog-reported count of 377 corridors at the recorded retrieval. They do not contain provider-level quotes, transaction-level remittance prices or actual remittance transactions. They must be treated as catalog metadata only.

### Controlled scenarios and derived outputs

All 5,000 rows are controlled synthetic configurations. Amounts, country pairs, domain, urgency, privacy, asset, intent, modality and perception-like attributes do not identify real users or represent executed payments. Feasibility flags, utility values, selected-rail labels, modeled settlement estimates and baseline deltas are rule-derived. The USD 10,000 KYC condition is a study-defined synthetic rule, not a universal legal or FATF threshold. SHAP-named fields are proxy/reserved values, not empirical SHAP attributions produced by a trained model.

## Splits and quality

- Train: 3,500 rows.
- Validation: 748 rows.
- Test: 752 rows.
- The original split seed, stratification method and grouping/dependency controls are undocumented; statistically independent or leakage-free partitions are not claimed.
- Consolidated CSV: 5,000 rows and 69 columns (68 schema fields plus `split`); no duplicate rows in the audited prepared build.
- 5,063 missing cells: 4,993 expected empty `rejection_reason` cells in non-rejected rows and 70 derived-field nulls across the seven rejected rows.

## Code and reproducibility

The original executable used to create the existing CSV rows was not recovered. The GitHub `generate_dataset.py` is an independently authored reconstruction based on documented assumptions; it does not claim to regenerate the current CSV byte-for-byte or row-for-row. The immutable source is [commit 5ecb791](https://github.com/caesium72/Consensus-X-dataset/blob/5ecb791dea05558741f96a4e46c2043fb8729aba/generate_dataset.py).

## Licence and citation

No reuse licence has yet been selected. Do not treat this prepared archive as a finalized public release until a licence decision and third-party terms review are complete. Once this archive is deposited on Zenodo, cite its specific version DOI; do not cite the current Version 1.0 DOI as though it refers to the prepared archive.
