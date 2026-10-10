# Data Collection and Provenance

## 1. Release and version status

This documentation describes the corrected NSIO-Benchmark v2.0 archive prepared for a future Zenodo deposit. At the time of preparation, the only published Zenodo version was Version 1.0 at <https://doi.org/10.5281/zenodo.23239670>. The corrected archive had not yet been uploaded. The Version 1.0 DOI must not be presented as identifying the prepared archive. The prepared release's version-specific DOI and licence remain pending.

## 2. Construction approach

The resource is a provenance-aware hybrid benchmark. Its construction pipeline comprises:

1. Capture a bounded set of public network and market snapshots, published pricing and documented protocol parameters.
2. Register source identifiers, URLs, retrieval context, values, units and provenance classes.
3. Configure controlled synthetic transaction scenarios.
4. Map scenario attributes, external inputs and transformations into the 68-field benchmark schema.
5. Apply the study-defined feasibility gate and deterministic utility/routing rules.
6. Store decision outputs, baselines, evaluation scaffolding and source-to-field traceability.

The 5,000 transaction-oriented rows are controlled synthetic configurations, not executed payment transactions. External evidence is shared context and was not collected separately for each scenario row.

## 3. Evidence ledger and source registry

`data/raw/source_observations.csv` contains 33 evidence-ledger records: 23 external network/market observations, eight source-derived parameters and two public-dataset metadata entries. The source registry is broader and also lists contextual documentation references that are not separate evidence-ledger observations. In particular, references to XRP Ledger/Stellar consensus and API documentation are not observations in the 33-row ledger and are not additional settlement rails in this benchmark.

SRC-009 (Stripe's published pricing schedule) is a source-derived parameter. SRC-015 and SRC-016 are public-dataset metadata sources rather than transaction-price observations.

## 4. World Bank Remittance Prices Worldwide (RPW)

OBS-032 records catalog temporal coverage through 2025 Q1. OBS-033 records a catalog-reported count of 377 corridors at the captured retrieval. These records describe RPW catalog coverage only. They do not contain provider-level quotes, transaction-level remittance-price values or actual remittance transactions. Do not treat them as transaction-cost labels.

## 5. Synthetic and derived fields

Synthetic scenario values include amount, country pair, domain, urgency, privacy level, asset type, intent, modality and perception-like fields. The USD 10,000 KYC condition is a study-defined scenario rule rather than a universal regulatory threshold. Feasibility, utility and selected-rail outputs are deterministic rule-derived labels, not independent ground truth. Fabric and Besu fee, latency and throughput are modeled estimates, not measured properties of deployed production networks. SHAP-named columns are proxy/reserved fields, not empirical SHAP explanations from a trained model.

## 6. Partitions and quality checks

The consolidated CSV has 5,000 rows and 69 columns (68 schema fields plus `split`). The train, validation and test files contain 3,500, 748 and 752 rows, respectively. The source archive does not document the original split seed, stratification process or dependency controls. The quality summary reports no duplicate rows and 5,063 missing cells: 4,993 expected nulls in `rejection_reason` for non-rejected rows and 70 derived-field nulls across the seven rejected rows.

## 7. Code reproducibility limit

The original executable used to create the existing CSV rows was not recovered. The repository's `generate_dataset.py` is a new reconstruction from documented assumptions and should be treated as such. It is not proof that the existing rows can be regenerated exactly. The immutable script is available at [GitHub commit 5ecb791](https://github.com/caesium72/Consensus-X-dataset/blob/5ecb791dea05558741f96a4e46c2043fb8729aba/generate_dataset.py). Any exact-reproduction claim requires separate, documented row-level comparison and file-hash validation.

## 8. Licence

No reuse licence has been selected. The archive is a prepared package, not yet a final public deposit. Select and confirm an appropriate licence before publication, and check each third-party source's redistribution terms.
