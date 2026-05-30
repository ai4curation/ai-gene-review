# SwissProt Keywords (SPKW) Unique Terms Project

## Overview

This project reviews genes that have GO annotations derived **solely** from UniProt Keywords (SPKW) via GO_REF:0000043, with no corroborating evidence from experimental, computational, or curator sources. The goal is to identify systematic over-annotation patterns and distinguish legitimate SPKW contributions from problematic mappings.

## Key Findings

- **Over-annotation rates vary dramatically by organism and term**
- Eukaryotic BP terms (apoptosis, meiosis, autophagy, rhythm) show 80-100% over-annotation
- Bacterial annotations are mostly accurate (~5% issues for P. putida)
- Viral annotations are clade-sensitive: phage immune/defense terms are often semantic mismatches, while eukaryotic viral immune-evasion terms may be legitimate but too broad
- Common patterns: process conflation, regulatory vs participatory confusion, caspase substrates
- **GOA has retired the SPKW pipeline (≈April 2026)**: `GO_REF:0000043` keyword-to-GO
  annotations have been removed from live GOA for all cellular organisms (verified zero for
  human, mouse, fly, worm, *S. pombe*, plants; only viruses retain them). The problem this
  project documented is now resolved at the source. Retrospective review of 34 non-Arabidopsis
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
| [Virus clades](SPKW-VIRUS.md) | Viral taxa | 54,131 | 11 | 55% | Host-context mismatch, specificity |
| [PLANTS](SPKW-PLANTS.md) | Non-ARATH plants | 4,117 | 34 | 15% Tier-A | Term-tiering; GOA retired SPKW |
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
| **Enzyme-class keyword → bare process** | An activity keyword maps to a generic, substrate-less process term; substrate specificity lives on the MF branch | Methyltransferase → methylation (plant MTases: MET1A, EZ1, CCOAOMT, COQ5) | MARK_OVER / MODIFY |

## Legitimate SPKW Contributions

Not all SPKW-unique annotations are over-annotations:

- **Antimicrobial peptides/lysozymes** (D. melanogaster) - "killing of cells" is correct
- **Arsenic/antibiotic resistance genes** (P. putida) - direct functional annotations
- **Conserved functions** (Ced-12/ELMO in D. mel) - SPKW captures known biology missing from experimental annotations
- **Core circadian genes** (ELF4 in Arabidopsis) - accurate but redundant with specific terms
- **DELLA growth repressors** (RHT1/"Reduced height" in wheat) - "GA signaling pathway" is the core function of a DELLA; retirement was collateral damage (left only "nucleus")
- **Storage proteins** (patatin PATB1 in potato) - "nutrient reservoir activity" is patatin's defining role; current GOA has no storage term after retirement
- **Viral life-cycle terms** (phage DGR reverse transcriptase, phage quorum-sensing peptide, influenza M2) - often accurate but may need more specific viral or molecular-function terms

## Project Status

- **Started**: 2025-12-23
- **Last updated**: 2026-05-30
- **Total genes reviewed**: 129 across 11 subprojects
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
- [x] [PLANTS](SPKW-PLANTS.md) - Non-Arabidopsis crops (34 genes, 14 species); term-tier classification + retrospective validation + full Tier-A keyword-watch-list sweep (methylation, developmental, defense, nodulation, hormone-signaling x6)
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

### 2026-05-30

- Added a **keyword-level** view to [SPKW-METHODOLOGY.md](SPKW-METHODOLOGY.md): reverse-map
  SPKW-unique GO terms to their source UniProt keywords via the public `keyword2go`
  (external2go) mapping (the GAF stores only the GO term). Produced a tier-annotated
  watch-list of the ~30 process/role keywords that drive plant over-annotation; it is
  organism-independent (same keywords drove the human/pombe/Arabidopsis subprojects).
- Reviewed the largest unreviewed Tier A keyword, **`Methyltransferase` → *methylation*
  (GO:0032259)** (92 plant genes), across 4 substrate classes: MET1A (rice, DNA),
  EZ1 (maize, histone H3K27), CCOAOMT (potato, lignin caffeoyl-CoA), COQ5 (rice, ubiquinone).
- **Finding: `Methyltransferase → methylation` is a reliable, mechanistically-explained
  over-annotation** (4/4 flagged; 3 MARK_OVER, 1 MODIFY). GO keeps methylation
  substrate-specificity on the molecular-function branch and has **obsoleted** the specific
  *process* terms (DNA methylation GO:0006306, histone methylation GO:0016571, H3K27
  methylation GO:0070734), so the bare *methylation* (GO:0032259) is structurally doomed to be
  redundant with the specific *…-methyltransferase activity* MF the gene already carries.
- Bonus: the review pass also caught two unrelated over-predictions — CCOAOMT *circadian
  rhythm* (ARBA) and EZ1 *single-stranded RNA binding* (ortholog transfer), both REMOVEd.
- **Keyword-watch-list sweep** (12 more genes across the next three Tier A keyword classes):
  - *Developmental* (`Differentiation`/`Flowering`): GI, HD3A (REMOVE cell differentiation;
    MODIFY flower development on flowering-TIME genes — the ELF4 pattern), MADS3
    (MODIFY→specification of stamen identity), FEA2 (MODIFY→meristem maintenance). "cell
    differentiation" is a catch-all that's wrong or too coarse.
  - *Defense/killing* (`Plant defense`/toxin): XA21 R-gene (MODIFY→defense response to
    bacterium), CPS4 phytoalexin synthase (MARK_OVER, STS3 enzyme-vs-product), O6/b-32 RIP
    (toxin activity **legitimate**, kept→rRNA N-glycosylase), CHIB chitinase (mixed).
  - *Nodulation*: NSP1 (ACCEPT — legitimate core Nod-signaling TF, removal=collateral damage),
    CCAMK (MODIFY→arbuscular mycorrhizal association — rice doesn't nodulate; PPC16-style
    organism-context error), LBA leghemoglobin (O2-carrier ACCEPT, nodulation MARK_OVER),
    ENOD2A (MARK_OVER, expression marker).
- **Meta-rule confirmed:** a process/role keyword is only as good as the gene's position
  relative to that process → (1) core component → keep; (2) wrong organism/pathway → MODIFY;
  (3) right area wrong altitude → MODIFY-to-specific; (4) expression/component ≠ function →
  MARK_OVER/REMOVE. PLANTS now **30 genes / 14 species** (added common bean).
- **Hormone-signaling-subtype batch** (4 genes; completes all six major plant hormones):
  VP1 (maize, ABA B3 TF) MODIFY→regulation of/response to ABA (responsive effector); CKX2
  (rice cytokinin **dehydrogenase**) MARK_OVER — a catabolic enzyme that *degrades* the hormone,
  not a signaling component (cleanest case); TUD1 (rice BR U-box E3 ligase) ACCEPT (legitimate
  component); EIL2 (rice ethylene EIN3-like TF) ACCEPT (legitimate; collateral damage). With
  auxin (ABP1) and GA (RHT1/DELLA), one keyword ("X signaling pathway") yields keep / MODIFY /
  remove purely by the gene's pathway position (transduction component vs responsive effector vs
  hormone-metabolism enzyme). PLANTS now **34 genes / 14 species**; the full high/medium-value
  Tier A watch-list is covered.

### 2026-05-29

- Extended [PLANTS](SPKW-PLANTS.md) with five more genes across four new species
  (maize, wheat, the moss *Physcomitrium patens*, potato), bringing PLANTS to 14 genes /
  13 species. Selected from the `plant.ddb` closure-filtered TRUE SPKW-unique set
  (`spkw_plants_unique` table) to stress-test the highest-risk Tier A keyword classes.
- Reviewed (falcon deep research + full ai-review.yaml, all `just validate`-clean):
  - **RHT1** (wheat DELLA, GA signaling) → MODIFY→neg. regulation of GA signaling; removal
    **NOT justified** (core repressor function lost — strongest collateral-damage case yet).
  - **ABP1** (maize, auxin signaling) → MARK_AS_OVER_ANNOTATED→response to auxin; removal
    justified (contested receptor), but auxin *binding* kept as core.
  - **MPK4a** (moss, innate immunity/defense) → MARK_AS_OVER_ANNOTATED ×2; removal justified
    (correct but redundant with experimental PRR-signaling-pathway).
  - **AM1** (maize AMEIOTIC1, chromosome segregation/cell division) → REMOVE / MARK_OVER;
    removal justified (over-broad/mis-placed; specific meiotic terms carry the biology).
  - **PATB1** (potato patatin, nutrient reservoir/lipid catabolic/defense) → ACCEPT/ACCEPT/
    MARK_OVER; **mixed** — storage role is collateral damage, defense over-annotated.
- **New finding — hormone-signaling keywords cut both ways.** Tier alone does not decide a
  hormone-signaling term; the gene's pathway position does. RHT1 (DELLA, a transduction
  *component*) refines the earlier ARF19/PARA rule (those were merely hormone-*responsive*).
  Running collateral-damage tally now five: CASP1, EME1, PR1B1, RHT1, PATB1.

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

### 2026-05-21

- Added [SPKW-VIRUS.md](SPKW-VIRUS.md) as the virus-wide and clade-specific counterpart to the organism SPKW subprojects
- Quantified `virus.ddb`: 180,680 SPKW annotations, 135,117 naive SPKW-unique annotations, and 80,218 closure-filtered SPKW-unique annotations
- Summarized 11 existing viral gene reviews across phage, anti-CRISPR, influenza, phage quorum-sensing, and DGR cases
