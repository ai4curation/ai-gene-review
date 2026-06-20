---
title: ProtNLM2 Evaluation
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

## ARGO-ProtNLM-50 Evaluation Results

All 50 benchmark proteins received full AIGR annotation reviews (`*-ai-review.yaml`), falcon deep research, and the 39 proteins with GO predictions received biologically informed prediction assessments (`*-protnlm-predictions-review.yaml`). Assessment categories follow [de Crécy-Lagard et al. 2025 (PMID:40703034)](https://pubmed.ncbi.nlm.nih.gov/40703034/).

### Aggregate results (75 predictions across 39 proteins)

| Category | Code | CS | Count | % | Description |
|----------|------|----|-------|---|-------------|
| Correct novel | COR | 2 | 17 | 23% | Biologically accurate, adds new information beyond GOA |
| Correct not novel | CNN | 2 | 11 | 15% | Correct but already captured in existing annotations |
| Less precise | LSP | 2 | 18 | 24% | Correct at higher level but more specific term exists in GOA |
| Uncertain | UNC | 1 | 13 | 17% | Cannot validate or refute from available evidence |
| Nonparalog incorrect | NPI | 0 | 14 | 19% | Refuted by biological evidence |
| Paralog incorrect | PLI | 0 | 2 | 3% | Wrong paralog subfamily assignment |
| **Total** | | | **75** | | **Mean CS: 1.40/2.0; Aggregate: 105/150 (70%)** |

**Concordant** (CS=2): 46/75 (61%) — predictions supported by evidence
**Uncertain** (CS=1): 13/75 (17%) — insufficient evidence to judge
**Discordant** (CS=0): 16/75 (21%) — predictions refuted by evidence

### Results by GOA overlap category

| Match category | n | Dominant assessments |
|----------------|---|---------------------|
| EXACT | 19 | LSP:13, CNN:6 — predictions match existing GOA but are typically parent terms |
| MORE_SPECIFIC | 6 | CNN:3, NPI:2, UNC:1 — some correctly refine GOA, others overreach |
| LESS_SPECIFIC | 1 | LSP:1 |
| NO_OVERLAP | 26 | NPI:9, UNC:6, COR:5, PLI:2 — mixed; novel predictions often wrong |
| NOT_IN_GOA | 23 | COR:12, UNC:6, NPI:3 — best category for genuinely novel discoveries |

### Error analysis (16 incorrect predictions)

| Error type | Count | Description |
|------------|-------|-------------|
| FREQUENCY_BIAS | 13 | Model defaults to high-frequency training labels (e.g., generic "membrane", "transferase activity") |
| PARALOG_OVERANNOTATION | 4 | Wrong subfamily — e.g., predicting phosphatase activity for catalytically dead MTMR9, kinase activity for kinase-domain-lacking RIC7 |
| PATHWAY_CONTEXT_IGNORED | 3 | Cross-kingdom errors — e.g., neuronal/immune terms for plant proteins |
| TRAINING_DATA_CONTAMINATION | 2 | Predictions that simply reproduce existing IEA annotations |

### Key findings

1. **ProtNLM2 is strongest for uncharacterized proteins (NOT_IN_GOA)**: 12/23 (52%) of these predictions were correct and novel, identifying genuine functions like DNA binding for a KilA-N domain protein (A2FPI7), ECM organization for OLFML2A (A0A8C9H4D2), and nuclear localization for MCM-4 (A0A061AL94).

2. **EXACT matches are predominantly less precise, not novel**: 13/19 (68%) of "exact" matches are actually parent terms of more specific existing annotations (e.g., predicting "cytoplasm" when "clathrin-coated vesicle" is already annotated). This suggests ProtNLM2 captures broad functional categories but lacks resolution.

3. **Frequency bias is the dominant error mode** (13/22 error annotations): The model over-predicts common GO terms (membrane, transferase activity, phosphorylation) without biological specificity. This is especially problematic for proteins with unusual functions (e.g., HERC3 truncation lacking HECT domain, auxilin's repurposed PTEN-like domain).

4. **Cross-kingdom errors persist despite taxon constraint filtering**: 3 predictions applied animal-specific terms (neuronal cell body, protein antigen binding) to plant proteins, indicating the Evidencer's taxon constraint checking has gaps.

5. **Paralog discrimination is a weakness**: The model conflates catalytically active and inactive family members (MTMR9 pseudophosphatase, RIC7 lacking kinase domain), a Type 6 error pattern that sequence similarity methods inherently struggle with.

6. **Assessment quality depends on biological synthesis**: The mechanical category mapping (EXACT→CNN, NO_OVERLAP→UNC) used in preliminary analysis was substantially revised by expert review. For example, many "EXACT" matches were reclassified from CNN to LSP, and several "MORE_SPECIFIC" predictions from CNN to NPI, after considering protein biology.
