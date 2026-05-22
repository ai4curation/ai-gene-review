# SwissProt Keywords (SPKW) Unique Terms Project

## Overview

This project reviews genes that have GO annotations derived **solely** from UniProt Keywords (SPKW) via GO_REF:0000043, with no corroborating evidence from experimental, computational, or curator sources. The goal is to identify systematic over-annotation patterns and distinguish legitimate SPKW contributions from problematic mappings.

## Key Findings

- **Over-annotation rates vary dramatically by organism and term**
- Eukaryotic BP terms (apoptosis, meiosis, autophagy, rhythm) show 80-100% over-annotation
- Bacterial annotations are mostly accurate (~5% issues for P. putida)
- Viral annotations are clade-sensitive: phage immune/defense terms are often semantic mismatches, while eukaryotic viral immune-evasion terms may be legitimate but too broad
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
| [Virus clades](SPKW-VIRUS.md) | Viral taxa | 54,131 | 11 | 55% | Host-context mismatch, specificity |
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
| **Viral host-context mismatch** | Same host-pathogen term valid in one viral clade but wrong in another | Phage AcrF8 → innate immune | MODIFY |
| **Toxin vs effector** | Effectors incorrectly called toxins | NleB1 (E. coli) | REMOVE |
| **Subclade divergence** | Family keyword ignores subfunctionalization | LCR1 (Arabidopsis DEFL) | REMOVE |
| **Kratagonist ≠ toxin** | Sequestration ≠ toxin activity | D7 proteins (mosquito) | MODIFY |

## Legitimate SPKW Contributions

Not all SPKW-unique annotations are over-annotations:

- **Antimicrobial peptides/lysozymes** (D. melanogaster) - "killing of cells" is correct
- **Arsenic/antibiotic resistance genes** (P. putida) - direct functional annotations
- **Conserved functions** (Ced-12/ELMO in D. mel) - SPKW captures known biology missing from experimental annotations
- **Core circadian genes** (ELF4 in Arabidopsis) - accurate but redundant with specific terms
- **Viral life-cycle terms** (phage DGR reverse transcriptase, phage quorum-sensing peptide, influenza M2) - often accurate but may need more specific viral or molecular-function terms

## Project Status

- **Started**: 2025-12-23
- **Last updated**: 2026-05-21
- **Total genes reviewed**: 95 recorded in compiled data, plus viral clade reviews summarized in [SPKW-VIRUS.md](SPKW-VIRUS.md)
- **Compiled data**: [spkw_reviewed_genes.csv](spkw_reviewed_genes.csv)

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
- [x] [Virus clades](SPKW-VIRUS.md) - Virus-wide and clade-specific patterns
- [x] [BPT4](SPKW-BPT4.md) - Phage semantics
- [x] [ECO57](SPKW-ECO57.md) - Toxin/effector

## Curation Recommendations

1. **Check regulatory vs participatory** - many genes regulate processes but don't participate IN them
2. **Consider organism biology** - same GO term can have different validity across taxa
3. **Distinguish toxins from effectors** - direct cytotoxicity vs signaling modulation
4. **Validate family-level keywords** - subfunctionalization can invalidate family annotations
5. **Expression ≠ function** - upregulation during a process doesn't mean functional involvement
6. **Check viral host context** - phage-bacterium interactions need different terms from eukaryotic viral immune evasion

## Swiss-Prot vs TrEMBL Analysis

**Key finding**: Keywords on Swiss-Prot entries are **manually assigned by curators**, not by ARBA/UniRule automatic systems. This means:

| Organism | Swiss-Prot % | Implication |
|----------|-------------|-------------|
| Human | 99.6% | Over-annotations reflect manual curator keyword choices |
| T4 Phage | 99.6% | Same - curators chose these keywords |
| E. coli O157 | 88.6% | Mostly manual |
| P. putida | 32.2% | Mixed manual/automatic |
| Virus (all) | 13.1% | Mostly TrEMBL; errors may reflect mapping or automatic keyword assignment |
| A. gambiae | 3.8% | Mostly automatic keyword assignment |

**Of 71 genes with over-annotation issues: 70 are Swiss-Prot (99%)**

For reviewed high-confidence organism batches, this confirms the problem is usually in the **KW→GO mapping layer**, not keyword assignment. Virus-wide analysis is different because most candidates are TrEMBL. See [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md) and [SPKW-VIRUS.md](SPKW-VIRUS.md) for stratification queries.

---

## Session Notes

### 2026-02-04

- Researched UniProt keyword assignment process (confirmed: Swiss-Prot = manual)
- Created [spkw_reviewed_genes.csv](spkw_reviewed_genes.csv) compiling 95 reviewed genes
- Added Swiss-Prot vs TrEMBL stratification to methodology
- Cross-species analysis: issue rates 10-40%, all Swiss-Prot dominated

### 2026-05-21

- Added [SPKW-VIRUS.md](SPKW-VIRUS.md) as the virus-wide and clade-specific counterpart to the organism SPKW subprojects
- Quantified `virus.ddb`: 180,680 SPKW annotations, 135,117 naive SPKW-unique annotations, and 80,218 closure-filtered SPKW-unique annotations
- Summarized 11 existing viral gene reviews across phage, anti-CRISPR, influenza, phage quorum-sensing, and DGR cases
