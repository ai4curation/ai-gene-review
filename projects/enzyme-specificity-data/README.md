# Enzyme substrate-specificity data sources

Lightweight, runnable clients for the **experimental / curated** databases that are the
authoritative evidence for enzyme substrate specificity — the recommended alternative to
binding-affinity prediction (see [`../BOLTZ2_SUBSTRATE_SPECIFICITY.md`](../BOLTZ2_SUBSTRATE_SPECIFICITY.md)).

| Script | Source | Auth | What it gives |
|---|---|---|---|
| `query_sabiork.py` | [SABIO-RK](https://sabiork.h-its.org) | **none** | Km / kcat / kcat·Km per substrate (specificity) |
| `query_mcsa.py` | [M-CSA](https://www.ebi.ac.uk/thornton-srv/m-csa) | **none** | catalytic residues + curated reaction/mechanism |
| `query_brenda.py` | [BRENDA](https://www.brenda-enzymes.org) | **account + zeep** | Km / turnover number across organisms |

Only dependency for the two open clients is `requests`. BRENDA additionally needs a free
account and `pip install zeep` (it makes real SOAP calls — it does **not** scrape the site).

## Usage

```bash
# Substrate specificity from kinetics (open) — Km/kcat grouped by substrate
python query_sabiork.py --ec 2.7.1.1 --organism "Homo sapiens" --summary
python query_sabiork.py --uniprot P19367 --tsv hk1.tsv      # raw TSV w/ PubMed IDs

# Catalytic mechanism / active-site residues (open)
python query_mcsa.py --uniprot P56868
python query_mcsa.py --ec 5.1.1.3 --json glurac.json

# BRENDA (needs free account + zeep)
export BRENDA_EMAIL=you@example.org BRENDA_PASSWORD=...   # password sent only as SHA-256 hash
python query_brenda.py --ec 2.7.1.1 --organism "Homo sapiens" --param km
```

## Why this beats Boltz-2 for specificity

SABIO-RK directly returns the **measured** discrimination an enzyme makes between substrates.
Example (human hexokinase, EC 2.7.1.1): D-Glucose Km ≈ 4.6×10⁻⁵ M vs D-Fructose ≈ 1×10⁻² M —
a ~200× preference, measured, with PubMed provenance. That is the ground truth that affinity
predictors only approximate (and, per published benchmarks, approximate poorly).

## Using results in a gene review

- Cite specific records by **PubMed ID** (SABIO-RK returns these) in `GENE-notes.md` and in the
  relevant annotation `review.reason` — e.g. to justify MODIFY (too narrow/broad) per the
  [`ENZYME_SPECIFICITY`](../ENZYME_SPECIFICITY.md) categories.
- Use M-CSA catalytic residues + reaction to sanity-check the *reaction class* (e.g. the PHYKPL
  transaminase-vs-phospho-lyase case) before changing an MF term.
- Treat database values as evidence to *read and verify*, not to copy blindly: kinetic values vary
  with assay conditions; never hardcode or over-interpret a single record.
