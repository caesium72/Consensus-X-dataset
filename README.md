# NSIO-Benchmark v2.0 — Provenance-Backed Hybrid Benchmark

**Build date:** 2026-09-30  
**Rows:** 5,000  
**Schema:** 68 fields, matching the nine category counts in the NSIO manuscript.

## 1. What was taken from where?

### Real/external observations

| Dataset field / observation | Source | What was captured |
|---|---|---|
| `eth_gas_gwei` | Etherscan Gas Tracker | 0.114 Gwei in the captured page result |
| ETH price | CoinGecko Ethereum | $2,657.51 |
| SOL price | CoinGecko Solana | $120.25 |
| Ethereum/Solana TVL | DeFiLlama | $49.265B / $5.777B |
| Ethereum/Solana chain fees | DeFiLlama | $344,737 / $978,477 per 24h in captured snapshot |
| Ethereum/Solana DEX volume | DeFiLlama | $1.357B / $3.0B per 24h |
| Ethereum/Solana active addresses | DeFiLlama | 601,507 / 2.47M |
| Polygon gas | PolygonScan | 281.048 Gwei standard |
| Polygon confirmation | PolygonScan | ~16 s standard estimate |
| Polygon ERC-20 example fee | PolygonScan | $0.001 |
| Stripe domestic card pricing | Stripe | 2.9% + $0.30 |
| Solana base fee | Solana docs | 5,000 lamports/signature |
| Ethereum slot time | Ethereum docs | 12 s |
| Ethereum validator deposit | Ethereum docs | 32 ETH |
| Besu QBFT | Besu docs | >=2/3 signatures; 4 validators for BFT |

## 2. What is synthetic?

The 5,000 transaction rows are **controlled synthetic scenarios**, not real payment records.

Synthetic fields include transaction amount, country pair, domain, urgency, privacy class, intent, modality, perception outputs and scenario labels.

The real external observations are injected as market/environment anchors.

## 3. What is derived?

Examples:
- ETH transfer fee = observed gas price × 21,000 gas × observed ETH/USD.
- Solana base fee USD = 5,000 lamports × observed SOL/USD.
- Utility scores = NSIO paper utility equation.
- CAS = NSIO paper cosine-similarity definition.
- RFS = NSIO paper definition.
- Consensus/capability labels = derived from official documentation.

## 4. Critical legal/compliance note

The manuscript contains an amount > $10,000 KYC condition. This benchmark preserves that condition as a **study-defined synthetic rule** only. It is not represented as a universal legal/FATF requirement.

## 5. Important limitation

This release is a **provenance-backed hybrid benchmark**, not a complete historical scrape of every provider. The web environment allowed direct inspection of public pages and current source observations, but some API/download endpoints require API credentials or an interactive download form. Those limitations are recorded in `docs/collection_manifest.json`.

## 6. Files

- `processed/nsio_benchmark_5000.csv` — full 68-field benchmark.
- `processed/train.csv` — training split.
- `processed/validation.csv` — validation split.
- `processed/test.csv` — test split.
- `raw_external/source_observations.csv` — external observations captured during this build.
- `processed/market_snapshots.csv` — normalized market layer.
- `processed/rail_capabilities.csv` — documented capability layer.
- `data_dictionary.csv` — field definitions and provenance.
- `provenance.csv` — field-level provenance mapping.
- `source_registry.csv` — source/citation registry.
- `references/references.bib` — BibTeX.
- `docs/collection_manifest.json` — source-to-field mapping.
- `docs/quality_summary.json` — QA summary.
