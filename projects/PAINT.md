---
title: "PAINT Human No-IBA Gene Review Project"
maturity: SCOPING
tags: [PIPELINE, FLAGSHIP]
species: [human]
---

# PAINT Human No-IBA Gene Review Project

## Overview

Review human genes that lack IBA (Inferred from Biological Ancestor) annotations. These genes are candidates for PAINT (Phylogenetic Annotation INference Tool) but currently have no phylogenetically-inferred annotations, meaning they may be:
- Poorly characterized
- Have unique/divergent functions
- Lack clear orthologs with experimental evidence

For each gene, the workflow generates at least 2 deep research reports (from different providers) and completes AI-assisted annotation review.

**Source**: [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review)

## Data Source

- **Spreadsheet**: https://docs.google.com/spreadsheets/d/12bR3FZ7XrUXL86IKJc__K6QbFBEsSlQeSdiVXwFsjEI/
- **Local**: `projects/PAINT/human-no-IBA-simple.csv` (format: species,uniprot_id,gene_symbol)
- **Total genes**: 7,594

## Model Species

**Primary: Homo sapiens (human)**
- UniProt species code: human
- Genes without IBA annotations are priority targets

## Completed Reviews

**165 genes with COMPLETE status** (as of 2026-01-25)

### Highlighted Reviews (Notable Findings)

| Gene | Function | Finding |
|------|----------|---------|
| PLD3/PLD4/PLD5 | 5'-3' exonuclease | Misnamed - NOT phospholipase D enzymes |
| DAB2IP | GAP, tumor suppressor | Comprehensive multi-function review |
| RASA3 | Bifunctional RasGAP | Acts on both RAS and RAP1 |
| ICA1/ICA1L | BAR domain proteins | Membrane curvature sensing |
| IFIT2/IFIT3 | Antiviral effectors | Interferon-stimulated response |
| GADD45A/B/G | Stress response | MAPK pathway regulation |

## Notable Findings

### PLD3/PLD4/PLD5 Misannotation
These proteins are named "phospholipase D" but are actually:
- **PLD3/PLD4**: 5'-3' exonucleases with immune regulatory functions
- **PLD5**: Catalytically inactive pseudoenzyme

This is a prime example of misleading gene nomenclature that AI review can flag.

## Batch Processing Infrastructure

The project has scaled to industrial batch processing:
- 50 batches prepared (2,500 gene capacity)
- Parallel architecture for continuous pipeline
- Can process 100+ genes per hour with deep research automation

## Reproducibility

Per-gene workflow:

```bash
just fetch-gene human GENE
just deep-research human GENE --provider falcon
just deep-research human GENE --provider cyberian
# Review and complete ai-review.yaml
just validate human GENE
```

List all completed PAINT genes:

```bash
comm -12 <(cut -d',' -f3 projects/PAINT/human-no-IBA-simple.csv | sort) \
         <(grep -l "status: COMPLETE" genes/human/*/*.yaml | xargs dirname | xargs -I{} basename {} | sort)
```

Supplementary files in `projects/PAINT/`:
- `human-no-IBA-simple.csv` - Gene list (species, uniprot_id, gene_symbol)
- `human-no-IBA.tsv` - Full annotation data

---

# STATUS

**Project Statistics (2026-09-04):**
- Total genes in project: 7,594
- **PAINT genes completed: 635** (8.4%)
- Ready for review (have deep research but not complete): 6
  (ERVMER34-1, PEX11A, SUMF2, TAX1BP1, TMEM67, TMF1)
- Structured PANTHER FamilyReviews written for reviewed genes' families: 19 of 19
  (`interpro/panther/<PTHR>/<PTHR>-review.yaml`)

## Progress
- [x] Infrastructure setup (batch processing, parallel deep research)
- [x] 635 PAINT gene reviews completed
- [x] Family-level review dimension added: paired FamilyReview per reviewed gene
- [ ] Complete reviews for remaining 6 genes with deep research
- [x] FamilyReviews for all 19 families of the 2026-09-04 batch (the three
      InterPro-outage stragglers — PTHR11494, PTHR15414, PTHR48482 — recovered
      and completed the same day)
- [ ] Re-fetch IL10 GOA: the cached snapshot still carries now-obsolete
      GO:0005615 rows that PAINT has already migrated to GO:0005576
- [ ] Re-derive the no-IBA source list against current GOA (see 2026-09-04 note)
- [ ] Scale deep research to all genes
- [ ] Full project completion (7,594 genes)

Last updated: 2026-09-04

# NOTES

## 2026-09-04

**20-gene batch with paired PANTHER family reviews**

Completed finishing reviews (all validate with zero warnings, status COMPLETE)
for 20 genes: BCKDHA, BCKDHB, CD28, CTLA4, NDUFS2, NDUFV1, PEX2, PEX10,
PEX11B, PEX13, PEX16, ORMDL3, MBL2, MTCH2, IL10, ERLEC1, CFAP61, LOXHD1,
GPATCH11, NAALADL2 — and, new for this project, wrote structured FamilyReviews
(node-level PAINT/IBD adjudication) for all 19 of their PANTHER families
(CD28/CTLA4 share PTHR11494; the three families stalled by a multi-hour
InterPro API outage were recovered and completed the same day). Across the
19: residue validator 506 checks pass / 0 fail, family-gene crosscheck 0
conflicts.

Key findings:
- **The no-IBA source list is stale.** Most of the 20 "no-IBA" genes now
  receive IBAs (PAINT IBDs dated 2022–2026): PEX11B, ORMDL3, CFAP61, LOXHD1,
  BCKDHA/B, PEX13, PEX16, MTCH2, MBL2 among them. The recurring *real* gap is
  narrower and invisible to a has-IBA test: **families lacking any
  molecular-function IBD** (BCKDH E1, PEX13, PEX16, NDUFV1's eukaryotic node),
  leaving human genes with only uninformative protein-binding IPI rows as MFs.
- **PTHR48178 (PEX2)**: the Cdc73/Paf1-complex IBD is a homonym confusion
  (PEX2 synonym PAF1 vs the PAF1 elongation factor), seeded by the target's
  own miscited IDA — WRONG_NODE, retraction recommended.
- **IL10**: four GO_REF:0000024 ISS rows trace to mouse TNF (P06804), not
  mouse IL-10 — a wrong-accession entry set argued from fold non-homology.
- **PTHR10404 (NAALADL2)**: human NAALADL2 descends from the carboxypeptidase
  IBD node yet receives no IBA (silent pruning); recommended an explicit IRD,
  with a machine-checked residue site proving loss of the catalytic Glu pair.
- **GPATCH11**: PAINT's 2026-02-25 snapshot already withdrew the kinetochore
  IBD (go-annotation#6450); the 2017 GOA kinetochore IBA is stale propagation.
- **BCKDHA**: draft carried a systematic 45-residue precursor-vs-mature
  numbering error, now corrected against the UniProt SQ block.

Provenance: history records under `history/genes/human/<GENE>/` and
`history/other/<PTHR>/` (one per gene and per family review).

## 2026-02-04

**Major batch annotation review session**
- Reviewed 81 genes using annotation-reviewer agent
- PAINT-specific completions: 165 → 207 (+42)
- Total completions: 246 → 328 (+82)
- Remaining with deep research: 104 → 22 (-82)

Notable genes reviewed include:
- Fe-S cluster assembly pathway: HSCB, HSPA9, IBA57, ISCA1, ISCA2, ISCU, NFS1, NFU1, MMS19, CIAO1, BOLA3
- Apoptosis/autophagy: BCL2, BCL2L1, BECN1, CASP9, ATG4D, ATG5, ATG7, DRAM1, DRAM2
- Transcription factors: GATA3, FOXO1, IRF8, OLIG2, ASCL1
- Signaling: NOTCH1, LRRK2, AXIN1, FAS
- Disease-relevant: HTT (Huntington), FXN (Friedreich ataxia), CBS (homocystinuria)

Note: Subagent status updates weren't persisting; fixed manually.

## 2026-01-25

**Project reorganization and stats update**
- Created top-level PAINT.md project file
- Renamed folder from `paint/` to `PAINT/` for consistency
- Updated stats: 165 COMPLETE reviews (was showing 14 - massively out of date)
- Started cyberian server for deep research
- Identified 285 genes needing cyberian deep research
- Created batch processing script
- First gene (ABCB7) completed in 17 minutes

## 2025-12-18(Massive Scaling Session)

**Major Achievement**: Transformed from manual workflow to industrialized batch processing
- Expanded from 297 to 1,806 gene folders (+508% growth)
- Submitted 1,500+ cyberian deep research jobs
- Created 50 batches (2,500 gene capacity)
- Established fully parallel, async pipeline

## 2025-12-18 (Review Session)

Completed reviews for:
- ICA1, ICA1L - BAR domain proteins
- SOCS4 - E3 ligase adaptor
- PLD3, PLD4, PLD5 - Discovered misannotation (NOT phospholipases)
- RASA3 - Bifunctional RasGAP

Key finding: PLD3/PLD4/PLD5 nomenclature is misleading - they are exonucleases, not phospholipases.
