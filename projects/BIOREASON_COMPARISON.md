# AI-Curated vs. AI-Predicted GO Annotations: A Systematic Comparison of AIGR and BioReason-Pro

## Abstract

We systematically compare GO term predictions from BioReason-Pro/GO-GPT (Fallahpour et al. 2026), a multimodal reasoning LLM for protein function prediction, against expert-curated AI-assisted reviews from the AI Gene Review (AIGR) knowledge base. AIGR combines deep literature research, evidence evaluation, and ontology-aware curation across 500+ genes and 75+ organisms. Our comparison reveals that GO-GPT captures the correct functional neighborhood but consistently lacks the specificity required for production-quality annotation, predicting ancestor terms rather than the precise leaf annotations identified through literature-grounded curation. This highlights a fundamental gap between sequence-based function prediction and evidence-based annotation that current protein language models do not bridge.

## Introduction

### The annotation gap

Protein function annotation remains a critical bottleneck. The Gene Ontology Consortium provides the gold standard for functional annotation, but experimental evidence (EXP, IDA, IPI, etc.) covers <0.1% of known proteins (UniProt). Computational methods fill this gap through homology transfer (InterPro2GO, BLAST), but these propagate errors and lack specificity.

### Two AI approaches

Two recent paradigms attempt to improve annotation quality:

1. **AI-assisted curation (AIGR approach):** LLM-powered coding agents perform deep literature research (via PaperQA/Edison, Perplexity, OpenAI), evaluate existing annotations against primary evidence, and produce structured reviews with provenance chains. This mirrors expert curation but at scale.

2. **AI-predicted function (BioReason-Pro approach):** Multimodal reasoning LLMs integrate protein embeddings (ESM2/ESM3), domain architecture (InterPro), protein-protein interactions (STRING), and organism context to predict GO terms directly from sequence. GO-GPT treats GO prediction as autoregressive sequence generation; BioReason-Pro adds chain-of-thought reasoning traces.

### The question

How do these approaches compare? BioReason-Pro claims annotations "preferred over UniProt ground truth in 79% of cases" by human experts. But UniProt entries for many proteins are sparse. How do BioReason-Pro predictions compare against *careful* AI-assisted curation with full literature review?

## Methods

### AIGR knowledge base

- 500+ genes reviewed across 75+ organisms
- Each review includes: existing annotation audit, deep literature research, core function identification, new annotation proposals, validation against LinkML schema
- Deep research providers: Edison/PaperQA (Falcon), Perplexity, OpenAI, Cyberian
- All reviews validated with `just validate` (schema + PMID reference checking)

### GO-GPT setup

- Model: `wanglab/gogpt` from HuggingFace
- Backbone: ESM2-3B (`facebook/esm2_t36_3B_UR50D`) for protein embeddings
- 3.1B total parameters, inference on Apple M-series GPU (MPS)
- Organism-aware prediction with 201 organism embeddings
- Sequence input only (no domain annotations, no PPI context)
- Output: predicted GO terms per aspect (MF, BP, CC), propagated through ontology hierarchy

### Comparison methodology

For each gene with both a curated AIGR review and a UniProt sequence:
1. Extract protein sequence from UniProt flat file
2. Run GO-GPT prediction with correct organism
3. Compare predicted terms against:
   - `existing_annotations` from the review (accepted terms)
   - `new_annotations` proposed by the review
   - `core_functions` identified in the review
4. Classify overlap as: exact match, ancestor match (GO-GPT predicts parent), descendant match, or no match

### Tools

- `just gogpt-predict <organism> <gene>` — run GO-GPT prediction
- `just gogpt-compare <organism> <gene>` — predict + compare with review
- `just gogpt-compare-all` — systematic comparison across all reviewed genes

## Preliminary Results

### Case studies

| Gene | Organism | GO-GPT MF | AIGR MF | Relationship |
|------|----------|-----------|---------|-------------|
| rpoS | P. putida KT2440 | GO:0003677 (DNA binding) | GO:0016987 (sigma factor activity) | Wrong branch |
| TP53 | Human | GO:0005515 (protein binding) | GO:0000976 (TF cis-reg region binding) | Wrong branch, too generic |
| CAT2 | S. cerevisiae | GO:0016413 (O-acetyltransferase) | GO:0004092 (carnitine O-acetyltransferase) | **Ancestor match** — parent term |
| EGFR | Human | GO:0005515, GO:0019899 | TBD | Pending comparison |

### Emerging patterns

1. **Ancestor granularity gap:** GO-GPT frequently predicts the correct *parent* term but not the specific *leaf* term. This is expected given Fmax training rewards ancestor-propagated predictions.

2. **BP > MF for GO-GPT:** GO-GPT performs better on BP (where ancestor terms are more informative) than MF (where specificity matters most for annotation utility).

3. **Organism sensitivity:** GO-GPT has KT2440-specific embeddings but still defaults to generic bacterial predictions. Model organism genes (human, yeast) may perform better.

4. **Missing core functions:** For specialized proteins (sigma factors, specific enzymes), GO-GPT misses the defining molecular function entirely, falling back to generic co-functions like DNA binding or protein binding.

## Discussion

### What GO-GPT does well

- Captures broad functional category (transferase → correct for CAT2)
- Predicts correct subcellular localization (nucleus for TP53)
- Organism-aware embeddings recover phylogenetic relationships

### What GO-GPT cannot do

- Distinguish core molecular function from co-functions (DNA binding vs sigma factor activity)
- Identify gene-specific pathway terms (p53 signaling pathway)
- Provide evidence provenance (no literature, no experimental basis)
- Generate new annotation proposals not in training data

### Implications for GO annotation

1. **GO-GPT as hypothesis generator:** Could serve as a first-pass filter, identifying the functional neighborhood for genes lacking any annotation. Not suitable as a standalone annotator.

2. **Complementary approaches:** AIGR's literature-grounded curation catches what sequence-based prediction misses. BioReason-Pro's attention analysis could potentially flag residues for curation focus.

3. **The "79% preferred" claim in context:** BioReason-Pro's advantage over UniProt entries likely reflects completeness (adding missing annotations) rather than specificity. Against careful curation, the advantage diminishes.

## TODO

- [ ] Run `just gogpt-compare-all` for systematic comparison across all 500+ reviewed genes
- [ ] Add BioReason-Pro full model (with reasoning traces) comparison, not just GO-GPT
- [ ] Compute semantic similarity (Resnik/Lin) between predicted and curated terms
- [ ] Stratify by organism, protein length, annotation density
- [ ] Compare against existing IEA annotations (InterPro2GO, UniProtKB-KW) as additional baseline
- [ ] Evaluate whether GO-GPT predictions add signal when combined with AIGR workflow
- [ ] Check BioReason-Pro web interface for TP53/BRCA1 reasoning traces (requires account)

## References

- Fallahpour A, Seyed-Ahmadi A, Idehpour P, et al. BioReason-Pro: Advancing Protein Function Prediction with Multimodal Biological Reasoning. bioRxiv 2026.03.19.712954 (2026).
- The Gene Ontology Consortium. The Gene Ontology resource: enriching a GOld mine. NAR (2021).
- Evans R, Shen J. InterLabelGO+. CAFA5 (2024).
- Chervov A. ProtBoost. CAFA5 (2024).

## Data Availability

- AIGR reviews: `genes/` directory in this repository
- GO-GPT predictions: `genes/<organism>/<gene>/<gene>-gogpt-predictions.json`
- Comparison script: `scripts/gogpt_predict.py`
- Just targets: `just gogpt-predict`, `just gogpt-compare`, `just gogpt-compare-all`
