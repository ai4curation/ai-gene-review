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

## Updated Results (2026-03-21)

### Systematic GO-GPT Batch Comparison (250 genes)

Three-level comparison against AIGR curated reviews:

| Level | Overlap | Reference | Recall | Predicted | Precision |
|-------|---------|-----------|--------|-----------|-----------|
| vs GOA (raw annotations) | 1,046 | 2,967 | **35.3%** | 8,910 | 11.7% |
| vs Post-Review (accepted+new) | 971 | 2,913 | **33.3%** | 8,910 | 10.9% |
| vs Core Functions | 210 | 933 | **22.5%** | 8,910 | 2.4% |

**Key findings:**
1. GO-GPT recovers ~35% of existing GOA annotations from sequence alone
2. Post-review overlap (33.3%) is slightly LOWER than GOA (35.3%) — some GO-GPT predictions were removed during curation
3. Core function recall at 22.5% — GO-GPT gets ~1 in 5 core terms
4. Precision is low (11.7%) — massive over-prediction

**Per-aspect:**
- MF: 19.9% overlap (69/346)
- BP: 24.2% overlap (114/471)
- CC: 0% (reviews rarely capture CC in core_functions — this is a gap to fix)

### Where GO-GPT Excels

**Sigma factors** — correctly predicted GO:0016987 for B. subtilis sigE/sigF/sigG (but missed it for P. putida rpoS — organism-specific training gap)

**Classic enzymes with strong sequence→function mapping:**
- Dihydrofolate reductase (GO:0004146) — dfrP, frd
- Cellulase (GO:0008810) — P10477, celA, Q9RGE6
- Lysozyme (GO:0003796) — BPT4/E, LysB
- Alpha-amylase (GO:0004556) — amyE
- Serine endopeptidase (GO:0004252) — aprE
- Peptidyl-prolyl isomerase (GO:0003755) — SlyD, surA

**Top overlap genes:** Dscam1 (24/29 GOA), DnaJ (18/23), DnaK (18/27), SlyD (16/16 perfect recall)

### Where GO-GPT Fails

**Genes with zero overlap despite many predictions:**
- DROME/Hsp83: 43 predicted, 5 reviewed, 0 overlap
- DROME/git: 41 predicted, 10 reviewed, 0 overlap  
- ARATH/AT5G52640: 33 predicted, 18 reviewed, 0 overlap
- BACSU/spoIIE: 35 predicted, 6 reviewed, 0 overlap

Pattern: GO-GPT over-predicts generic terms (catalytic activity, protein binding) while missing the specific functional terms captured by literature-grounded curation.

### Full BioReason-Pro Reasoning Traces (Web App)

Successfully accessed BioReason-Pro web interface (app.bioreason.net) via Chrome AppleScript automation. The app provides:
- InterPro domain analysis
- GO-GPT predictions
- **Thinking trace** — structured chain-of-thought reasoning from domains to function
- Functional summary
- GO term predictions with hierarchy
- Downloadable markdown export

#### Case Study: E. coli SlyD — Sequence Length Sensitivity

Two runs were performed with different sequence lengths:

**Run 1: Full-length SlyD (196 aa, with His-rich C-terminal tail)**
- InterPro: IPR046357 (PPIase superfamily) + IPR001179 (FKBP domain) + **IPR048261 (SlpA/SlyD-like insertion domain)**
- MF predictions include: GO:0003755 (PPIase) ✅, **GO:0016151 (nickel binding) ✅**, GO:0008270 (zinc binding) ✅, GO:0051082 (unfolded protein binding) ✅
- BP: GO:0006457 (protein folding) ✅, GO:0042026 (protein refolding) ✅
- Reasoning trace correctly identified the SlyD-like insertion domain and metal-assisted folding

**Run 2: Truncated SlyD (110 aa, FKBP domain only)**
- InterPro: IPR046357 + IPR001179 only (no SlyD insertion domain)
- MF: GO:0003755 (PPIase) ✅ but **NO metal binding predictions** ❌
- Reasoning trace: correct for PPIase but completely missed the metallochaperone function

**Critical finding:** BioReason-Pro's predictions are **sequence-length-sensitive**. The C-terminal nickel/zinc-binding domain was essential for correct functional prediction. Truncation (which happens automatically for proteins >2000 aa in the ESM context window) can eliminate functionally critical domains.

#### Comparison with AIGR Curated Review

| Feature | BioReason-Pro (full) | AIGR Review |
|---------|---------------------|-------------|
| PPIase activity | ✅ GO:0003755 | ✅ GO:0003755 |
| Chaperone | ✅ GO:0051082 (unfolded protein binding) | ✅ GO:0051082 |
| Nickel binding | ✅ GO:0016151 | ✅ + specific role in hydrogenase/urease maturation |
| Zinc binding | ✅ GO:0008270 | ✅ |
| Metal homeostasis | ❌ Not mentioned | ✅ Nickel insertion into metalloenzymes |
| Interaction partners | Hypothesized: GroEL, Trigger Factor, DnaK | Literature-confirmed: HypB, UreE, specific PMIDs |
| Evidence provenance | None (reasoning from domains) | PMIDs with exact quotes |

**BioReason-Pro advantage:** Clean domain→function reasoning chain, no literature search needed
**AIGR advantage:** Literature-backed specificity, evidence provenance, dual function identification (PPIase + metallochaperone for specific metalloenzymes)

## Accessing BioReason-Pro Web Interface

### Method (for reproducibility)

The web app at app.bioreason.net requires Google OAuth (routed through institutional SSO). Browser automation via Playwright is blocked by Google's bot detection. The working approach:

1. Open Chrome tab via AppleScript: `osascript -e 'tell application "Google Chrome" to open location "https://app.bioreason.net/"'`
2. User logs in manually through Google OAuth / institutional SSO
3. Wait for login to complete (poll URL via AppleScript until `auth` is no longer in the URL)
4. Interact with the app via Chrome AppleScript JavaScript execution:
   - Fill sequence textarea: `document.querySelectorAll('textarea')[0]`
   - Fill organism textarea: `document.querySelectorAll('textarea')[1]`
   - Click send button (40x40 icon button)
5. Wait for results (~60-90 seconds for InterPro + GO-GPT + reasoning trace)
6. Click "Download Response" button to get markdown export
7. Downloaded files appear in ~/Downloads/ as `bioreason-chat-YYYY-MM-DD.md`

### Key technical notes
- Must use React-compatible input simulation (native value setter + dispatchEvent)
- Google OAuth blocks Playwright/Chromium automation — must use real Chrome with user session
- The app is a chat interface, not a form — "New Chat" button resets for each protein
- Results include: InterPro domains, GO-GPT predictions, thinking trace, functional summary, UniProt summary

## Updated TODO

- [ ] Fix GO-GPT batch script memory leak (torch.no_grad + gc.collect applied, needs testing at scale)
- [ ] Run full 1,207 gene comparison (parked due to 54GB memory issue)
- [ ] Run BioReason-Pro web app on 5-10 key proteins for detailed comparison
- [ ] Compute semantic similarity (Resnik/Lin) between predicted and curated terms
- [ ] Stratify by organism, protein length, annotation density
- [ ] Compare GO-GPT against IBA (phylogenetic) and InterPro2GO (IEA) baselines
- [ ] Generate PredictionReview YAMLs for BioReason-Pro web results
- [ ] Evaluate whether truncation at 2000 aa systematically removes C-terminal domains
- [x] ~~Run GO-GPT on case study genes (TP53, CAT2, rpoS)~~
- [x] ~~Set up three-level comparison (GOA, post-review, core functions)~~
- [x] ~~Access BioReason-Pro web interface~~
- [x] ~~Capture reasoning traces~~
