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

Post-processed ProtNLM2 XML export (`post-processed-2026_02_28k.xml`): 28,553 entries with predicted protein names, GO terms, subcellular locations, and function comments. All predictions use evidence code ECO:0008006 with source `Google:ProtNLM2`.

**Dataset version note:** The public ProtNLM2 pilot release (UniProt 2026_02) covers [26,856 accessions](https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv). Our XML is an earlier pre-release with 1,697 additional entries that were subsequently removed during quality filtering. Some predictions in our data may have been caught by the production Evidencer exclusion criteria.

**Note:** The XML uses a synthetic UniProt-like format with placeholder values for organism, dates, and dataset fields (`dataset="TrEMBL"`, `proteinExistence: uncertain`, `organism: PLACEHOLDER`). It is not a snapshot of actual UniProt entries — the proteins span the full range from long-established Swiss-Prot entries (e.g. Q6P6B1, Swiss-Prot since 2007) to unreviewed TrEMBL sequences.

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
