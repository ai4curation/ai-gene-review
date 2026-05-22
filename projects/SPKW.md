# SwissProt Keywords (SPKW) Unique Terms Project

## Overview

This project reviews genes that have GO annotations derived **solely** from UniProt Keywords (SPKW) via GO_REF:0000043, with no corroborating evidence from experimental, computational, or curator sources. The goal is to identify systematic over-annotation patterns and distinguish legitimate SPKW contributions from problematic mappings.

## Key Findings

- **Over-annotation rates vary dramatically by organism and term**
- Eukaryotic BP terms (apoptosis, meiosis, autophagy, rhythm) show 80-100% over-annotation
- Bacterial annotations are mostly accurate (~5% issues for P. putida)
- Common patterns: process conflation, regulatory vs participatory confusion, caspase substrates
- **GOA has retired the SPKW pipeline (≈April 2026)**: `GO_REF:0000043` keyword-to-GO
  annotations have been removed from live GOA for all cellular organisms (verified zero for
  human, mouse, fly, worm, *S. pombe*, plants; only viruses retain them). The problem this
  project documented is now resolved at the source. Retrospective review of 9 non-Arabidopsis
  plant genes (see [PLANTS](SPKW-PLANTS.md)) shows only ~15% of plant SPKW-unique terms carry
  real over-annotation risk; removal was justified for those, but blanket retirement also
  dropped *correct* annotations when the keyword was the only carrier of a fact.

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
| [PLANTS](SPKW-PLANTS.md) | Non-ARATH plants | 4,117 | 9 | 15% Tier-A | Term-tiering; GOA retired SPKW |
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
- **Last updated**: 2026-05-21
- **Total genes reviewed**: 104 across 11 subprojects
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
- [x] [PLANTS](SPKW-PLANTS.md) - Non-Arabidopsis crops (9 genes, 9 species); term-tier classification + retrospective validation of GOA's SPKW retirement
- [x] [BPT4](SPKW-BPT4.md) - Phage semantics
- [x] [ECO57](SPKW-ECO57.md) - Toxin/effector

## Curation Recommendations

1. **Check regulatory vs participatory** - many genes regulate processes but don't participate IN them
2. **Consider organism biology** - same GO term can have different validity across taxa
3. **Distinguish toxins from effectors** - direct cytotoxicity vs signaling modulation
4. **Validate family-level keywords** - subfunctionalization can invalidate family annotations
5. **Expression ≠ function** - upregulation during a process doesn't mean functional involvement

## Swiss-Prot vs TrEMBL Analysis

**Key finding**: Keywords on Swiss-Prot entries are **manually assigned by curators**, not by ARBA/UniRule automatic systems. This means:

| Organism | Swiss-Prot % | Implication |
|----------|-------------|-------------|
| Human | 99.6% | Over-annotations reflect manual curator keyword choices |
| T4 Phage | 99.6% | Same - curators chose these keywords |
| E. coli O157 | 88.6% | Mostly manual |
| P. putida | 32.2% | Mixed manual/automatic |
| A. gambiae | 3.8% | Mostly automatic keyword assignment |

**Of 71 genes with over-annotation issues: 70 are Swiss-Prot (99%)**

This confirms the problem is in the **KW→GO mapping layer**, not keyword assignment. See [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md) for stratification queries.

---

## Session Notes

### 2026-05-21

- Added [PLANTS](SPKW-PLANTS.md) subproject: SPKW over-annotation in non-Arabidopsis
  Viridiplantae.
- Built `plant.ddb` (go-db, `make plant`) from the Sept 2025 `goa_uniprot_gcrp` snapshot;
  40.4M annotations, 26,493 SwissProt accessions.
- Closure-filtered TRUE SPKW-unique query (non-ARATH, SwissProt-only): 6,678 annotations,
  4,117 genes, 214 terms — 74% closure reduction; aspect F 54% / P 37% / C 8%. Rice
  dominates (1,927 genes); 200+ species represented.
- **Discovered GOA retired `GO_REF:0000043` for all cellular organisms** since the snapshot.
  Reframed PLANTS as a retrospective validation study.
- Reviewed 4 genes (rice EME1, soybean PPC16, tobacco PARA, tomato PR1B1) — all 4 SPKW-unique
  annotations were over-annotations; GOA's removal justified for every headline term, but
  EME1 (endonuclease activity) and PR1B1 (defense response to fungus) lost correct biology.
- Classified all 214 SPKW-unique terms into 4 tiers: A over-annotation-risk (15%, 29 terms),
  B broad cofactor/enzyme-class MF (48%), C specific informative (31%), D context-dependent
  (6%). Only ~15% carry real over-annotation risk; ~79% (B+C) are correct — "SPKW-unique"
  is not a synonym for "over-annotation".
- Reviewed 5 more genes across broader taxa (grape STS3, Medicago NFP, poplar METK1,
  Chlamydomonas psaC, sorghum CASP1) — 9 genes / 9 species total, sampling all 4 tiers.
  The tier predicts the verdict: every Tier A removal was justified; the Tier C removal
  (CASP1, cell wall organization) discarded correct plant-specific biology.

### 2026-02-04

- Researched UniProt keyword assignment process (confirmed: Swiss-Prot = manual)
- Created [spkw_reviewed_genes.csv](spkw_reviewed_genes.csv) compiling 95 reviewed genes
- Added Swiss-Prot vs TrEMBL stratification to methodology
- Cross-species analysis: issue rates 10-40%, all Swiss-Prot dominated
