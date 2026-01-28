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

## Workflow

```bash
just fetch-gene human GENE
just deep-research human GENE --provider falcon
just deep-research human GENE --provider cyberian
# Review and complete ai-review.yaml
just validate human GENE
```

## Completed Reviews

**165 genes with COMPLETE status** (as of 2026-01-25)

To list all completed PAINT genes:
```bash
comm -12 <(cut -d',' -f3 projects/PAINT/human-no-IBA-simple.csv | sort) \
         <(grep -l "status: COMPLETE" genes/human/*/*.yaml | xargs dirname | xargs -I{} basename {} | sort)
```

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

## Supplementary Files

See `projects/PAINT/` folder:
- `human-no-IBA-simple.csv` - Gene list (species, uniprot_id, gene_symbol)
- `human-no-IBA.tsv` - Full annotation data

---

# STATUS

**Project Statistics (2026-01-25):**
- Total genes in project: 7,594
- **Comprehensive reviews completed: 165** (2.2%)
- Genes with gene folders: 325+
- Genes with deep research: 200+

## Progress
- [x] Infrastructure setup (batch processing, parallel deep research)
- [x] 165 comprehensive reviews completed
- [ ] Complete reviews for remaining genes with deep research
- [ ] Scale deep research to all genes
- [ ] Full project completion (7,594 genes)

Last updated: 2026-01-25

# NOTES

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
