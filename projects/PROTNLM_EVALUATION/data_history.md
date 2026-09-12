# ProtNLM2 Data Source History

## REST API (current, recommended)

Predictions are fetched from the UniProt REST API endpoint `https://rest.uniprot.org/uniprotkb/protnlm/{accession}`. The canonical accession list (26,856 entries) is published at the [FTP site](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv).

```bash
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py          # fetch all + convert to TSVs
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py --resume  # resume interrupted fetch
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py --convert-only  # re-convert existing JSONL
```

The API returns JSON with evidence inline per prediction. The fetch script saves raw JSONL (`protnlm_api.jsonl`) for reproducibility and converts to 3 TSV files (entries, predictions, evidence).

## Pre-release XML (historical)

The original exploratory analysis used a pre-release XML export (`post-processed-2026_02_28k.xml`, 28,553 entries) parsed by `parse_protnlm_xml.py`. This included 1,697 entries subsequently removed during quality filtering (64.5% Swiss-Prot entries excluded from the TrEMBL-only public pilot, plus QC-filtered TrEMBL entries). The API serves the same predictions in a cleaner format.

## Dataset statistics

| Type | Count | Description |
|------|-------|-------------|
| Protein name | 28,553 | Every entry gets a predicted name (22,467 recommended, 6,086 submitted) |
| GO terms | 6,833 entries | GO annotations derived from model predictions |
| Subcellular location | 13,690 entries | Predicted localization |
| Function comment | 5,438 entries | Free-text functional description |
| Name only | 8,690 entries | Only protein name predicted, no GO/location/function |

## Evidencer corroboration provenance

Each prediction has a model score (0–1, threshold 0.05) and post-hoc corroboration from the Evidencer:

- **domain** (9,950): Domain architecture match
- **GO** (8,727): Direct GO term prediction
- **PANTHER** (4,190): PANTHER family/subfamily match
- **keyword** (4,111): UniProt keyword match
- **InterPro** (1,022): InterPro family match
- **recommended_protein_name** (543): Name transferred from characterized homolog
- Plus many smaller categories (Pfam, SUPFAM, Gene3D, CDD, etc.)

## TSV files

| File | Description |
|------|-------------|
| `entries.tsv` | One row per entry (accession, name, prediction counts) |
| `predictions.tsv` | One row per GO/function/location prediction |
| `evidence.tsv` | One row per evidence block (scores, provenance) |
| `taxonomy.tsv` | Accession -> species mapping from UniProt |
