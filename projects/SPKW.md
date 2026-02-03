# SwissProt Keywords (SPKW) Unique Terms Project

## Overview

This project reviews genes that have GO annotations derived **solely** from UniProt Keywords (SPKW) via GO_REF:0000043, with no corroborating evidence from experimental, computational, or curator sources. The goal is to identify systematic over-annotation patterns and distinguish legitimate SPKW contributions from problematic mappings.

## Key Findings

- **Over-annotation rates vary dramatically by organism and term**
- Eukaryotic BP terms (apoptosis, meiosis, autophagy, rhythm) show 80-100% over-annotation
- Bacterial annotations are mostly accurate (~5% issues for P. putida)
- Common patterns: process conflation, regulatory vs participatory confusion, caspase substrates

## Cumulative Results

| Subproject | Organism | Total Genes | Reviewed | Issue Rate | Main Pattern |
|------------|----------|-------------|----------|------------|--------------|
| [Apoptosis](SPKW-APOPTOSIS.md) | Human | 280 | 23 | 87% | Regulatory conflation |
| [Rhythmic Process](SPKW-RHYTHMIC.md) | Human | 146 | 5 | 100% | Expression ≠ function |
| [Autophagy](SPKW-AUTOPHAGY.md) | Human | 123 | 14 | 79% | Signaling over-extension |
| [ANOGA](SPKW-ANOGA.md) | A. gambiae | 5,812 | 22 | Mixed | D7 toxin=100%, immune=17% |
| [SCHPO](SPKW-SCHPO.md) | S. pombe | 1,963 | 7 | 100% | ATG-meiosis conflation |
| [DROME](SPKW-DROME.md) | D. melanogaster | 2,753 | 4 | 50% | Mixed patterns |
| [PSEPK](SPKW-PSEPK.md) | P. putida | 1,098 | 4 | 25% | RT defense keyword |
| [ARATH](SPKW-ARATH.md) | A. thaliana | 8,433 | 4 | 75% | Subclade divergence |
| [BPT4](SPKW-BPT4.md) | Phage T4 | ~300 | 3 | 100% | Eukaryote-centric terms |
| [ECO57](SPKW-ECO57.md) | E. coli O157 | ~74,000 | 2 | 50% | Toxin vs effector |

## Methods

See [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md) for detailed SQL queries and explanation of closure-based filtering (which reduces false positives by 70%+ in well-curated organisms).

## Over-Annotation Patterns Identified

| Pattern | Description | Examples | Action |
|---------|-------------|----------|--------|
| **Process conflation** | Gene active during process X gets annotated to X | ATG genes → meiosis (S. pombe) | REMOVE |
| **Regulatory conflation** | Gene regulates X, annotated to X | AIMP2 → apoptotic process | MODIFY to regulatory term |
| **Caspase substrate** | Cleaved by caspases, annotated to apoptosis | AIMP1, BCAP31 | REMOVE |
| **Signaling over-extension** | 4+ steps from direct function | Sin1 → apoptosis | REMOVE |
| **Eukaryote-centric terms** | Immune/defense terms for phage-bacteria | T4 DAM → innate immune | REMOVE |
| **Toxin vs effector** | Effectors incorrectly called toxins | NleB1 (E. coli) | REMOVE |
| **Subclade divergence** | Family keyword ignores subfunctionalization | LCR1 (Arabidopsis DEFL) | REMOVE |
| **Kratagonist ≠ toxin** | Sequestration ≠ toxin activity | D7 proteins (mosquito) | MODIFY |

## Legitimate SPKW Contributions

Not all SPKW-unique annotations are over-annotations:

- **Antimicrobial peptides/lysozymes** (D. melanogaster) - "killing of cells" is correct
- **Arsenic/antibiotic resistance genes** (P. putida) - direct functional annotations
- **Conserved functions** (Ced-12/ELMO in D. mel) - SPKW captures known biology missing from experimental annotations
- **Core circadian genes** (ELF4 in Arabidopsis) - accurate but redundant with specific terms

## Project Status

- **Started**: 2025-12-23
- **Last updated**: 2026-01-31
- **Total genes reviewed**: ~90 across all organisms

### Phase 1 (Original)
- [x] MAP3K5 - COMPLETE
- [x] PHF23 - COMPLETE
- [x] SIRT2 - COMPLETE

### Subprojects
- [x] [Apoptosis](SPKW-APOPTOSIS.md) - 23/280 reviewed
- [x] [Rhythmic Process](SPKW-RHYTHMIC.md) - 5/146 reviewed
- [x] [Autophagy](SPKW-AUTOPHAGY.md) - 14/123 reviewed
- [x] [ANOGA](SPKW-ANOGA.md) - D7 + immune genes
- [x] [SCHPO](SPKW-SCHPO.md) - ATG-meiosis pattern
- [x] [DROME](SPKW-DROME.md) - Case studies
- [x] [PSEPK](SPKW-PSEPK.md) - Bacterial control
- [x] [ARATH](SPKW-ARATH.md) - Plant patterns
- [x] [BPT4](SPKW-BPT4.md) - Phage semantics
- [x] [ECO57](SPKW-ECO57.md) - Toxin/effector

## Curation Recommendations

1. **Check regulatory vs participatory** - many genes regulate processes but don't participate IN them
2. **Consider organism biology** - same GO term can have different validity across taxa
3. **Distinguish toxins from effectors** - direct cytotoxicity vs signaling modulation
4. **Validate family-level keywords** - subfunctionalization can invalidate family annotations
5. **Expression ≠ function** - upregulation during a process doesn't mean functional involvement
