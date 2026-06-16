---
species: []
sidecars: {}
---
# ProtNLM2 Evaluation

Systematic evaluation of Google's ProtNLM2 protein name and function predictions against expert-curated AIGR gene reviews and existing UniProt/GO annotations.

## Data source

Post-processed ProtNLM2 XML export (`post-processed-2026_02_28k.xml`): 28,553 entries with predicted protein names, GO terms, subcellular locations, and function comments. All predictions use evidence code ECO:0008006 (match to sequence model evidence used in automatic assertion) with source `Google:ProtNLM2`.

**Note:** The XML uses a synthetic UniProt-like format with placeholder values for organism, dates, and dataset fields (`dataset="TrEMBL"`, `proteinExistence: uncertain`, `organism: PLACEHOLDER`). It is not a snapshot of actual UniProt entries — the proteins span the full range from long-established Swiss-Prot entries (e.g. Q6P6B1, Swiss-Prot since 2007) to unreviewed TrEMBL sequences.

## Prediction types

| Type | Count | Description |
|------|-------|-------------|
| Protein name | 28,553 | Every entry gets a predicted name (22,467 recommended, 6,086 submitted) |
| GO terms | 6,833 entries | GO annotations derived from model predictions |
| Subcellular location | 13,690 entries | Predicted localization |
| Function comment | 5,438 entries | Free-text functional description |
| Name only | 8,690 entries | Only protein name predicted, no GO/location/function |

## Evidence provenance

Each prediction has a model score (0-1) and provenance showing what the model matched against:

- **domain** (9,950): Domain architecture match
- **GO** (8,727): Direct GO term prediction
- **PANTHER** (4,190): PANTHER family/subfamily match
- **keyword** (4,111): UniProt keyword match
- **InterPro** (1,022): InterPro family match
- **recommended_protein_name** (543): Name transferred from characterized homolog
- Plus many smaller categories (Pfam, SUPFAM, Gene3D, CDD, etc.)

## Files

| File | Description |
|------|-------------|
| `PROTNLM_EVALUATION/parse_protnlm_xml.py` | Parser: XML -> TSV files |
| `PROTNLM_EVALUATION/fetch_taxonomy.py` | Fetches species from UniProt REST API |
| `PROTNLM_EVALUATION/entries.tsv` | One row per entry (accession, name, prediction counts) |
| `PROTNLM_EVALUATION/predictions.tsv` | One row per GO/function/location prediction |
| `PROTNLM_EVALUATION/evidence.tsv` | One row per evidence block (scores, provenance) |
| `PROTNLM_EVALUATION/taxonomy.tsv` | Accession -> species mapping from UniProt |
| `PROTNLM_EVALUATION/protnlm_summary.ipynb` | Summary statistics notebook |

## Overlap with AIGR reviews

Only 8 of 1,334 reviewed genes appear in this 28K dataset (all TrEMBL/unreviewed proteins): C5AXM3, O94267, Q09490, Q21303, Q86WA8, Q9BZE2, Q9UNW9, Q9XUS3.
