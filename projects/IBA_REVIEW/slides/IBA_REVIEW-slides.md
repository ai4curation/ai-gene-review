---
title: "IBA Annotation Quality Project"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# IBA Annotation Quality Project

When phylogenetic propagation goes wrong — and when it falls short

**Chris Mungall** | AI-Assisted Gene Review

2026-06-22

---

## What is IBA?

**IBA = Inferred from Biological Aspect of Ancestor**

- Part of the GO Consortium **PAINT / PANTHER** phylogenetic annotation pipeline
- Curators annotate characterized proteins, then place those functions on the **ancestral node** of a phylogenetic tree (an **IBD** — Inferred from Biological aspect of Descendant)
- Those ancestral annotations **propagate down** to all descendant leaves as **IBA** annotations
- The `WITH/FROM` column records the exact source proteins a function was transferred from

IBA is a powerful, scalable way to annotate uncharacterized orthologs — but propagation can carry function where it no longer belongs.

---

## The problem: failure modes

A function correct for an ancestor may be wrong for a given leaf when:

1. **Functional divergence** — orthologs evolved different functions
2. **Pseudo-enzymes** — catalytic function lost despite retained domain fold
3. **Context-specific function** — function differs between organisms / tissues
4. **Over-generalization** — broad terms transferred when specific functions differ

Root-level annotations are especially risky: they propagate to **every** descendant, including subfamilies that have diverged.

---

## Two directions of IBA quality

This project examines **both** ways IBA fails:

**Over-annotation** (IBA is *wrong*) — patterns 1–15, the bulk of this work.

**Incompleteness** (IBA *under-calls* established biology) — phylogenetic propagation is conservative by construction, so much experimentally defined function never reaches the leaf.

> Quantified loss: **511 curated human core molecular functions across 423 genes** have **no IBA support at all** (401 grounded by experimental/traceable evidence).

The discovery method for both: the **AI gene review framework**.

---

## The approach

Findings emerged from **AI-assisted gene review**, then verified against primary evidence:

- Mined all `genes/*/*/*-ai-review.yaml` — **2,732** reviews; IBA actions distributed as
  `ACCEPT 4651 · KEEP_AS_NON_CORE 943 · MODIFY 321 · MARK_AS_OVER_ANNOTATED 189 · REMOVE 190 · UNDECIDED 39 · NEW 33`
- Each REMOVE candidate cross-checked against: **UniProt** FUNCTION/CAUTION, the **GO term definition** (QuickGO/OLS), GOA **WITH/FROM** provenance + PANTHER family composition, cached **publications**, and a reproducible **MSA** of catalytic residues
- Incompleteness quantified with a generic **evidence-subtraction** tool (`ai-gene-review subtraction-report`)

---

## Finding 1: Pseudo-enzyme propagation

Catalytic activity transferred to proteins that lost the active site but kept the fold — the **most defensible** REMOVE class (deficiency documented in UniProt).

- **Epe1** (pombe) — `GO:0032452` histone demethylase: HVD (not HXD) motif, no detectable activity
- **DPYSL2 / CRMP1 / DPYSL3 / DPYSL4** (human) — `GO:0016812` metallo-hydrolase: UniProt CAUTION "Lacks most of the conserved residues … for binding the metal cofactor"; **MSA confirms** loss of catalytic Lys159
- **AGO4** (human) — `GO:0004521` RNA endonuclease: "Lacks endonuclease activity"; MSA shows tetrad substitutions D669G, H807R (AGO3 *retains* the tetrad)
- **AKTIP** — `GO:0061631` E2: lacks catalytic Cys · **CASP12** — "Inactive caspase-12" · **HSP47/Serpinh1** (mouse) — non-inhibitory serpin

---

## Finding 2: Directional & sign errors

When a subfamily evolved the **opposite reaction** or a family mixes opposite-sign members.

- **Cds1** (M. tuberculosis, V. cholerae; PTHR10314 SF135) — `GO:0019344` cysteine **biosynthesis** propagated from the family root, but Cds1 catalyzes cysteine **catabolism** (EC 4.4.1.1: L-Cys → H2S + pyruvate). The most severe error type — *directionally opposite*. SF135 has the longest branch length (0.528) and only ~24% identity to synthases. (PMID:34439535, PMID:34283874)
- **BCL2** (human, mouse) — `GO:0043065` **positive** regulation of apoptosis, but BCL2 is the prototypical **anti-apoptotic** guardian. The IBA node (PTN000135648) mixes pro-apoptotic BAX/BAK1 with anti-apoptotic members. *(Caveat: a separate NAS annotation + context-dependent pro-apoptotic roles exist → "sign unreliable", not "impossible".)*

---

## Finding 3: WITH/FROM reveals mis-grouping

The single most useful diagnostic — reading the source proteins exposes the error directly.

**Tier A — wrong family / over-broad superfamily:**
- **NTN1 / NTN3** (human) — secreted Netrins given **POU-domain TF** activity (`GO:0000981` etc.); WITH/FROM = POU2F1, POU1F1, POU4F1, POU4F3
- **NOTCH1** — `GO:0007411` axon guidance from **SLIT1/2/3**
- **IL23R** — `GO:0004925` prolactin-receptor activity from **PRLR**

**Tier B — wrong paralog:**
- **ABRAXAS1** — spindle/MT terms trace to **ABRAXAS2**
- **opa1 / eat-3** — `GO:0016559` peroxisome fission on mitochondrial-fusion OPA1 (DRP1 branch does fission)

---

## Finding 4: Substrate & sub-activity over-propagation

Family nodes that lump enzymes of **different specificities** leak substrate terms.

- **AGK** (human) — `GO:0001729` ceramide kinase: three lines refute it ("only … monoacylglycerols and diacylglycerols … not ceramide and sphingosine", PMID:15939762; PMID:16269826). The dedicated ceramide kinase is **CERK**. PANTHER PTHR12358 mixes acylglycerol + sphingosine kinases.
- **SAMD8/SMSr** — `GO:0033188` sphingomyelin synthase: actually makes **ceramide phosphoethanolamine** ("larger PC prevents an efficient fit")
- **CPT1C** — RecName "Palmitoyl thioesterase"; lost carnitine transferase activity

**Sub-activity loss:** **CAPG** caps but does **not** sever actin (PMID:1322908); **CRYAA** is a holdase not a foldase — IBA contradicts a curated `NOT(refolding)`; worm **hsp-12.3/hsp-12.6** have *no* chaperone activity (PMID:9744800).

---

## Finding 5: Compartment & lineage errors

**Compartment over-transfer — but read the GO hierarchy first (two-sided):**
- **Valid REMOVE (mutually-exclusive):** nucleus on cytoplasmic PIWI/Argonaute (PIWIL1, prg-1, wago-1); nucleus on ER-kinase EIF2AK3 / BIRC6; PM on yeast SSB2/SSZ1
- **Anti-pattern (do NOT flag):** "cytoplasm" on a mitochondrial/ER/lysosomal protein — `GO:0005737` **subsumes** those organelles (e.g. Aga/GLA, DHCR24, ISCA1)

**Lineage-inappropriate (cross-kingdom) process transfer:**
- **TOLL9** (mosquito) — `GO:0006954` inflammatory response from human **TLR4** · **ndhA/D/K** (poplar) — aerobic respiration on **chloroplast** NDH · **che-3** (worm) — cilium motility on non-motile sensory cilia · **sta-2** (worm) — JAK-STAT (no JAK in worms)

---

## Summary: over-annotation patterns

| # | Pattern | Flagship example |
|---|---------|------------------|
| 1 | Pseudo-enzyme propagation | Epe1, DPYSL2/3/4, AGO4, CASP12 |
| 4 | Neo-functionalization (opposite reaction) | Cds1 (cysteine catabolism) |
| 6 | Organism/tissue context transfer | RIMBP2 (NMJ → CNS synapse) |
| 8 | Partial sub-activity loss | CAPG, CRYAA, hsp-12.3 |
| 9 | Regulatory-sign inversion | BCL2 |
| 10 | Complex/compartment over-transfer | EIF4E2, ALDH1L1, PEX2 |
| 11 | Substrate over-propagation | AGK, SAMD8, CPT1C |
| 12 | Mis-grouping via WITH/FROM | NTN1, NOTCH1, ABRAXAS1 |
| 13 | Generic compartment over-prop. | PIWIL1, EIF2AK3 |
| 14 | Cross-kingdom process transfer | TOLL9, ndhA/D/K, sta-2 |
| 15 | Regulator/effector conflation | SIR3, sigF/G/K, lys-7 |

---

## The other direction: IBA incompleteness

Phylogenetic propagation only transfers what a curated ancestor already carries, at the ancestor's granularity — so much established biology never reaches the leaf.

Using **evidence-subtraction** over **1015** reviewed human genes (with ontology closure, so an IBA call to a general parent still counts):

- **62%** of annotation-grounded `core_functions` terms (4516 / 7278) would be **lost** if IBA were the only evidence
- Restricting to molecular function (excluding low-info `binding`): **511 core MFs across 423 genes** have **no IBA support**, **401** experimentally grounded (IDA/IMP/IPI/EXP/TAS)

These sit in `core_functions` — the curator's distilled judgement of what the protein *does* — so they are central activities, not noise.

---

## Incompleteness: two mechanisms

**A. Activity absent from IBA entirely** (no IBA touches that branch):

| Gene | Core MF IBA misses | Evidence |
|------|--------------------|----------|
| USP21 | deubiquitinase (GO:0004843) | IDA, IMP |
| P4HB (PDI) | protein disulfide isomerase (GO:0003756) | EXP, IDA |
| FTH1 | ferroxidase (GO:0004322) | IMP |
| PARK7 | SOD copper chaperone (GO:0016532) | IDA |

**B. IBA stops at a general parent** (loss of resolution):

| Gene | IBA gives (general) | Experiment establishes |
|------|---------------------|------------------------|
| HDAC6 | protein deacetylase | tubulin deacetylase (GO:0042903) |
| SIRT2 | NAD-dependent deacetylase | H4K16 deacetylase (GO:0046970) |

**Caveat:** IBA isn't always the laggard — for PTEN, IBA carries the textbook PIP3 phosphatase; and IBA is the **sole** support for 66 human core MFs.

---

## Lessons learned (from the project log)

The recurring failure mode is **acting on one line of evidence**. Flagging a curated IBA is a strong claim — treat it like one.

1. **No single source is sufficient — synthesize.** Need ≥2 independent lines before REMOVE.
2. **Read the GO *definition*, not the label.** Worst miss: ATP7B "copper ion import" — definition covers movement into an *organelle*, so the Golgi-loading exporter is fine.
3. **"By similarity" is weak; direct experiment beats it.** AGK ceramide was a propagated tag refuted by two papers.
4. **Read the WITH/FROM column first** — wrong family / wrong paralog is near-mechanical evidence.
5. **Place both compartments in the GO hierarchy** before a localization REMOVE.
6. **Check taxon/lineage appropriateness** for process terms; **respect the curator** — uncertain ≠ wrong (UNDECIDED, e.g. UQCRC1).

---

## Recommendations for the GO / PAINT pipeline

1. **Flag pseudo-enzyme candidates** — enzyme domains missing catalytic residues
2. **Flag neo-functionalized subfamilies** — long branch lengths + different EC numbers
3. **Validate annotations at the family root** — root terms propagate everywhere; ensure truly universal
4. **Read the WITH/FROM** — wrong family or single paralog source is strong evidence of error
5. **Distinguish sub-activities** — capping≠severing, holdase≠foldase, slicer≠non-slicer
6. **Don't inherit a paralog's compartment/complex/pathway**
7. **Synthesize multiple lines of evidence — never a single keyword**
8. **Treat an IBA-only leaf as likely *under*-annotated** — prompt to seek the specific experimental activity

---

<!-- _class: lead -->

# Status: COMPLETE

IBA is powerful but **directional**: it can over-annotate diverged leaves *and* under-call established biology.

15 over-annotation patterns + a quantified incompleteness analysis (511 missed human core MFs).

Verify, don't trust — synthesize UniProt, GO definitions, WITH/FROM, MSA, and primary literature before flagging.

**Chris Mungall** | AI-Assisted Gene Review | 2026-06-22
