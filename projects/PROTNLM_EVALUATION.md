---
species: []
sidecars: {}
---
# ProtNLM2 Evaluation

Systematic evaluation of Google's ProtNLM2 protein name and function predictions against expert-curated AIGR gene reviews and existing UniProt/GO annotations.

**References:**
- [UniProt ProtNLM help page](https://www.uniprot.org/help/ProtNLM)
- [ProtNLM2 accession list (FTP)](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv)

## What is ProtNLM2?

ProtNLM2 is a transformer-based sequence-to-sequence model (T5 architecture) developed by Google DeepMind in collaboration with UniProt. It is trained on 240 million proteins from UniProt release 2023_04 (Swiss-Prot + TrEMBL) and takes amino acid sequence, organism TaxID, and AlphaFold secondary structure as inputs. The original ProtNLM predicted only protein names; ProtNLM2 expands to GO terms, subcellular locations, keywords, and function comments.

Predictions are post-processed by the **Evidencer** — a corroboration pipeline that checks each prediction against string matches, phmmer sequence similarity (bit score > 25), and TM-align structural similarity. Predictions failing GO taxon constraints or lacking corroboration are excluded. See the [UniProt help page](https://www.uniprot.org/help/ProtNLM) for full details.

## Data source

### REST API (recommended, reproducible)

Predictions are fetched from the UniProt REST API endpoint `https://rest.uniprot.org/uniprotkb/protnlm/{accession}`. The canonical accession list (26,856 entries) is published at the [FTP site](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv).

```bash
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py          # fetch all + convert to TSVs
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py --resume  # resume interrupted fetch
python projects/PROTNLM_EVALUATION/fetch_protnlm_api.py --convert-only  # re-convert existing JSONL
```

The API returns JSON with evidence inline per prediction. The fetch script saves raw JSONL (`protnlm_api.jsonl`) for reproducibility and converts to the same 3 TSV files used by the analysis notebooks.

### Pre-release XML (historical)

The original analysis used a pre-release XML export (`post-processed-2026_02_28k.xml`, 28,553 entries) parsed by `parse_protnlm_xml.py`. This included 1,697 entries subsequently removed during quality filtering (64.5% Swiss-Prot entries excluded from the TrEMBL-only public pilot, plus QC-filtered TrEMBL entries). The API serves the same predictions in a cleaner format.

## Prediction types

| Type | Count | Description |
|------|-------|-------------|
| Protein name | 28,553 | Every entry gets a predicted name (22,467 recommended, 6,086 submitted) |
| GO terms | 6,833 entries | GO annotations derived from model predictions |
| Subcellular location | 13,690 entries | Predicted localization |
| Function comment | 5,438 entries | Free-text functional description |
| Name only | 8,690 entries | Only protein name predicted, no GO/location/function |

## Evidencer corroboration provenance

Each prediction has a model score (0–1, threshold 0.05) and post-hoc corroboration from the Evidencer showing what supported each prediction:

- **domain** (9,950): Domain architecture match
- **GO** (8,727): Direct GO term prediction
- **PANTHER** (4,190): PANTHER family/subfamily match
- **keyword** (4,111): UniProt keyword match
- **InterPro** (1,022): InterPro family match
- **recommended_protein_name** (543): Name transferred from characterized homolog
- Plus many smaller categories (Pfam, SUPFAM, Gene3D, CDD, etc.)

## ARGO-ProtNLM-50 Benchmark

A curated set of 50 proteins for systematic evaluation, stratified across:
- 14 taxonomic groups (mammals, plants, bacteria, fish, insects, fungi, etc.)
- 4 prediction categories (rich, partial, go_only, name_only)
- Multiple evidence methods (string match, phmmer, tmalign)
- 5 case studies from the exploratory analysis (trivially correct, phmmer transfer, false positive, cross-kingdom error, ontology gap)

All 50 are in the public pilot release. See `argo_protnlm_50.csv`.

## Files

| File | Description |
|------|-------------|
| `PROTNLM_EVALUATION/fetch_protnlm_api.py` | Fetches from REST API -> JSONL + TSV files |
| `PROTNLM_EVALUATION/parse_protnlm_xml.py` | Legacy parser: XML -> TSV files |
| `PROTNLM_EVALUATION/fetch_taxonomy.py` | Fetches species from UniProt REST API |
| `PROTNLM_EVALUATION/argo_protnlm_50.csv` | Benchmark set of 50 proteins for evaluation |
| `PROTNLM_EVALUATION/entries.tsv` | One row per entry (accession, name, prediction counts) |
| `PROTNLM_EVALUATION/predictions.tsv` | One row per GO/function/location prediction |
| `PROTNLM_EVALUATION/evidence.tsv` | One row per evidence block (scores, provenance) |
| `PROTNLM_EVALUATION/taxonomy.tsv` | Accession -> species mapping from UniProt |
| `PROTNLM_EVALUATION/protnlm_summary.ipynb` | Exploratory analysis notebook |
| `PROTNLM_EVALUATION/protnlm_bench50_eval.ipynb` | ARGO-ProtNLM-50 benchmark evaluation notebook |

## Overlap with AIGR reviews

Only 8 of 1,334 reviewed genes appear in this 28K dataset (all TrEMBL/unreviewed proteins): C5AXM3, O94267, Q09490, Q21303, Q86WA8, Q9BZE2, Q9UNW9, Q9XUS3.
