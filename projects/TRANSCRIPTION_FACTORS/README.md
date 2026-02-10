# Transcription Factor Annotation Review Project

## Objective

Use AI/ML tools as a **second-pass review** to validate, challenge, and enhance existing GO annotations for transcription factors and transcriptional regulators. This addresses the gap between traditional homology-based annotation and modern deep learning approaches.

## Background

### The Problem

Current GO annotations for TFs rely heavily on:
- Pfam/InterPro domain detection (HMMs)
- Sequence homology (BLAST)
- Manual curation from literature

These methods have limitations:
- Miss novel TF families with no homology to known TFs
- Cannot distinguish functional subtypes (activator vs repressor)
- Don't capture proteins that lack canonical DNA-binding domains but function as cofactors
- Propagate annotation errors through homology transfer

### Recent Advances (per Palsson et al. 2026)

| Tool | Type | What it predicts | Performance |
|------|------|------------------|-------------|
| **DeepTFactor** | CNN | TF vs non-TF | MCC 0.939 |
| **DeepECtransformer** | Transformer | EC numbers | Attention-based interpretability |
| **CLEAN** | Contrastive learning | EC numbers | Handles class imbalance |
| **Foldseek Cluster** | Structure similarity | Remote homology | Links unannotated domains |
| **iModulons** | Transcriptomics | Co-regulated genes | Identifies TF regulons |

## Workflow

### Phase 1: Sequence-based prediction

For each protein annotated with TF-related GO terms:

```
Input: UniProt sequence
    │
    ├─► DeepTFactor
    │   └─► Binary TF prediction + saliency maps (DBD regions)
    │
    ├─► InterPro/Pfam
    │   └─► Known DBD domains (zinc finger, HTH, etc.)
    │
    └─► ESM-2 embeddings
        └─► Cluster with known TF families
```

**Discrepancy flags:**
- GOA says TF but DeepTFactor says non-TF (or vice versa)
- DeepTFactor highlights non-canonical regions (no Pfam DBD match)
- Protein clusters with TFs in embedding space but lacks TF annotation

### Phase 2: Functional subtype analysis

Current GO doesn't cleanly distinguish:
- Sequence-specific DNA-binding TFs vs general TFs
- Transcriptional activators vs repressors
- Pioneer factors vs non-pioneer factors
- Direct DNA binders vs cofactors

**Approach:**
1. Extract proteins with GO:0003700 (DNA-binding TF activity) and children
2. Cross-reference with:
   - GO:0001228 (activator) vs GO:0001227 (repressor)
   - Presence/absence of transactivation domains
   - Literature evidence codes (IDA, IMP vs IEA, ISS)
3. Flag proteins with:
   - Only IEA evidence for TF function
   - Conflicting activator/repressor annotations
   - TF annotation but no detectable DBD

### Phase 3: Structure-based validation

For proteins where sequence methods are ambiguous:

```
Input: UniProt ID
    │
    ├─► AlphaFold structure
    │
    ├─► Foldseek search
    │   └─► Find structural neighbors (even with low sequence identity)
    │
    └─► Compare GO annotations of structural neighbors
```

**Use cases:**
- Validate DBD predictions via structural fold
- Identify potential DNA-binding surfaces
- Link "dark" proteins to annotated TF families via structure

### Phase 4: Transcriptomic validation (where available)

For bacterial TFs, leverage iModulon data:

```
Input: Gene symbol
    │
    ├─► iModulonDB lookup
    │   └─► Is this gene associated with a known iModulon?
    │
    └─► Compare predicted regulon with GO annotations
```

**Validation criteria:**
- TF annotation supported by iModulon membership
- Predicted target genes consistent with GO BP annotations

## Implementation

### Tools to integrate

| Tool | Source | Integration method |
|------|--------|-------------------|
| DeepTFactor | [GitHub](https://github.com/jylee1122/DeepTFactor) | Local installation or API |
| InterPro | EBI API | REST queries |
| ESM-2 | Meta AI | HuggingFace / local |
| AlphaFold DB | EBI | REST API for structures |
| Foldseek | [GitHub](https://github.com/steineggerlab/foldseek) | Local or web server |
| iModulonDB | [imodulondb.org](https://imodulondb.org) | Web API |

### Data sources

1. **GOA files**: QuickGO API for current annotations
2. **UniProt**: Sequence and reviewed annotation status
3. **Publications**: PMID cache in `publications/` folder

### Output format

For each reviewed protein, generate entries in the standard `ai-review.yaml` format:

```yaml
existing_annotations:
  - term:
      id: GO:0003700
      label: DNA-binding transcription factor activity
    evidence_type: IEA
    original_reference_id: InterPro:IPR000123
    review:
      action: MODIFY  # or ACCEPT, REMOVE, MARK_AS_OVER_ANNOTATED
      summary: |
        DeepTFactor predicts TF with high confidence (0.95).
        Saliency highlights residues 45-120 (zinc finger region).
        However, no experimental evidence for DNA binding.
      proposed_replacement_terms:
        - id: GO:0003712
          label: transcription coregulator activity
      ml_validation:
        deeptfactor_score: 0.95
        deeptfactor_regions: "45-120 (C2H2 zinc finger)"
        interpro_domains: ["IPR007087"]
        structural_neighbors: ["P12345 (0.85 TM-score)"]
```

## Prioritization

### High priority targets

1. **Human TFs with IEA-only evidence**: ~200 proteins
2. **Proteins with conflicting annotations**: activator AND repressor
3. **"TF" annotations lacking any DBD domain**: potential cofactors
4. **Bacterial y-ome candidates**: uncharacterized E. coli proteins predicted as TFs

### Species focus

| Organism | Rationale |
|----------|-----------|
| Human | Clinical relevance, most annotations |
| E. coli K-12 | Best characterized, iModulon data available |
| S. cerevisiae | Well-studied TF network |
| A. thaliana | Plant-specific TF families |

## Evaluation metrics

### Per-protein metrics

- Agreement rate: DeepTFactor vs existing GOA
- DBD detection rate: Pfam vs DeepTFactor saliency
- Evidence upgrade potential: IEA → computational support

### Cohort metrics

- False positive rate in IEA annotations (estimated by ML disagreement)
- Novel TF candidates identified (no current annotation)
- Annotation refinement suggestions (too general → more specific)

## References

### Key methodological papers

1. Kim GB et al. (2021) DeepTFactor. PNAS 118:e2021171118
2. Kim GB et al. (2023) DeepECtransformer. Nat Commun 14:7370
3. Yu T et al. (2023) CLEAN. Science 379:1358-1363
4. Barrio-Hernandez I et al. (2023) Foldseek Cluster. Nature 622:637-645
5. Palsson BO, Lee SY, Kim GB (2026) AI for gene function discovery. Nat Microbiol 11:350-358

### Deep research output

- `ai-methods-query.txt` - Query used for literature scan
- `ai-methods-tf-prediction-perplexity.md` - Literature scan results

### GO Consortium TF annotation guidelines

Two related documents exist:

| Document | Citation | Location |
|----------|----------|----------|
| **Journal paper** | Gaudet P et al. (2021) Gene Ontology representation for transcription factor functions. *BBA Gene Regul Mech* 1864:194752. PMID:34461313 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1874939921000705) |
| **Operational guidelines** | Gaudet P, Logie C, Lovering R (last updated 2023-10-24) | `TF-annotation-guidelines.pdf` |

The PDF states it is "replaced by" the journal paper, but this is misleading — **both documents are needed**:

**Journal paper (2021) provides:**
- Formal rationale for GTF/dbTF/coTF classification
- Peer-reviewed, citable reference
- Conceptual framework for ontology structure

**PDF guidelines (2023) provides content NOT in the paper:**
- **4-question checklist** for annotation decisions
- **Worked examples** with specific PMIDs:
  - GTF: GTF2H2 (PMID:10924514)
  - dbTF: NKX6.3 (PMID:26314965)
  - coTF: SIN3A (PMID:22783022) — includes removal of incorrect annotations
- **High-throughput data interpretation rules:**
  - HT-SELEX: supports DNA binding, NOT dbTF without functional evidence
  - ChIP-seq: inconclusive alone; needs DBD + functional data
  - Bacterial 1-hybrid (B1H) guidance
- **Pitfalls section** with common annotation errors
- **Annotation extensions syntax** (`has_input`, `is_active_in`, `occurs_in`)
- **Evidence tables** showing which experiments support which terms

**Synthesized guidelines:** `tf-synthesized-guidelines.md` — operational distillation of both sources.

### Human dbTF catalogue

From Lovering et al. (2021) "A GO catalogue of human DNA-binding transcription factors" (PMID:34673265):

| File | Description | Count |
|------|-------------|-------|
| `human-dbTF-list.tsv` | UniProt ID + gene symbol for each human dbTF | 1,448 |
| `human-dbTF-annotations-quickgo.tsv` | Full GO annotations with evidence codes | 5,020 rows |

**Source:** QuickGO API query for GO:0003700 descendants, taxon 9606, Swiss-Prot reviewed proteins.

**Related resources:**
- [QuickGO dbTF target set](https://www.ebi.ac.uk/QuickGO/targetset/dbTF)
- [TFCheckpoint 2.0](https://www.tfcheckpoint.org) — cross-references 13 TF collections

---

## Project History

### 2026-02-04: Initial setup

1. **Literature scan** on AI/ML methods for TF prediction from sequence
   - Created query in `ai-methods-query.txt`
   - Ran deep research via perplexity → `ai-methods-tf-prediction-perplexity.md`
   - Key finding: DeepTFactor (2021) is primary tool; transformers underexplored for TF classification

2. **Reviewed Palsson et al. 2026** (Nature Microbiology)
   - Comprehensive review of AI for gene function discovery
   - Covers DeepTFactor, DeepECtransformer, CLEAN, Foldseek, iModulons
   - 43 references vs 6 from deep research scan
   - Added to project references

3. **Gathered GO annotation guidelines**
   - Downloaded `TF-annotation-guidelines.pdf` (GO Consortium)
   - Compared with journal paper (PMID:34461313)
   - Created `tf-synthesized-guidelines.md` — concise operational version

4. **Defined ML-based review workflow** (this README)
   - 4-phase approach: sequence → subtype → structure → transcriptomics
   - Output format compatible with `ai-review.yaml` schema

---

## Status

- [ ] Set up DeepTFactor locally
- [ ] Build pipeline to fetch GOA + UniProt for TF-annotated proteins
- [ ] Implement comparison logic
- [ ] Run on pilot set (10 human TFs)
- [ ] Evaluate and refine workflow
- [ ] Scale to full human TF set
