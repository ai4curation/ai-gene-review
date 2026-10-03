---
title: "Human Protein Atlas: Re-evaluating HPA Subcellular Location Evidence"
maturity: SCOPING
tags: [PIPELINE]
species: [human]
autolink_gene_symbols: true
---

# Human Protein Atlas: Re-evaluating HPA Subcellular Location Evidence

**Bottom line:** The Human Protein Atlas (HPA) Subcellular Section already maps
its immunofluorescence (IF) location calls to GO cellular-component terms and
exports them to GOA as `IDA` with reference `GO_REF:0000052`. HPA and this
project grade evidence differently. HPA grades each location by antibody
reliability. We judge each GO annotation against the whole literature and ask
whether it describes where the protein acts. This project downloads the HPA
data, joins it to our reviews, and works through the cases where the two
frameworks disagree.

## Background

### What HPA asserts

The HPA Subcellular Section ([Thul et al. 2017, PMID:28495876](https://doi.org/10.1126/science.aal3321))
images antibody-stained cell lines by confocal microscopy and calls a
**main** location and any **additional** locations for each protein, using
about 35 organelle and substructure classes (30 in the 2017 paper). Each location gets one of four
reliability grades:

| Grade | Meaning (HPA) |
|---|---|
| Enhanced | Validated by an orthogonal method: independent antibodies against separate epitopes, siRNA knockdown, or tagged-protein co-localization |
| Supported | Consistent with external experimental data, such as UniProt location annotation |
| Approved | Detected by one antibody with no supporting external data |
| Uncertain | Antibody staining contradicts other data, or the RNA level is very low |

HPA maps each location class to one GO term, for example `Nucleoli fibrillar center`
→ `GO:0001650 fibrillar center`. GOA receives the GO term as an IDA annotation.

### How this differs from our evidence model

1. **Supported means "agrees with the literature".** It is not an independent
   experiment. A Supported call copies existing knowledge, including any errors
   in it, so it is circular evidence for a GO annotation the literature already
   supports. Only **Enhanced** includes an orthogonal validation of the antibody.
2. **One antibody stains one cell line.** IF in fixed U2OS, A-431 or HEK293
   cells shows where the epitope is at steady state. It does not show where the
   protein carries out its function. Cytosol and nucleoplasm calls are often
   diffuse background, unprocessed precursors, or cross-reacting signal.
3. **The class vocabulary is coarse.** HPA calls `Mitochondria`, which becomes
   `GO:0005739 mitochondrion`, even for an inner-membrane translocase. Our
   reviews usually prefer the specific compartment, such as
   `mitochondrial inner membrane`. Many of our "disagreements" are about
   specificity, not about whether the location is real.
4. **HPA calls change between releases.** HPA re-grades locations in each
   version, and GOA lags behind. An annotation exported while a location was
   Supported can stay in GOA after HPA downgrades it to Approved or Uncertain,
   or drops it.
5. **The GO_REF description is out of date.** `GO_REF:0000052` still says
   annotations are exported only when supported by literature. The current
   data show that Enhanced calls are exported too (223 of the HPA annotations
   in our reviews are Enhanced).

## Data

- Source: `https://www.proteinatlas.org/download/tsv/subcellular_location.tsv.zip`
  (HPA **v25**, file dated 2025-11-06; 13,597 genes)
- Snapshot: [HUMAN_PROTEIN_ATLAS/data/subcellular_location.tsv](HUMAN_PROTEIN_ATLAS/data/subcellular_location.tsv)
- Join script: [HUMAN_PROTEIN_ATLAS/scripts/hpa_join.py](HUMAN_PROTEIN_ATLAS/scripts/hpa_join.py)

```bash
uv run python projects/HUMAN_PROTEIN_ATLAS/scripts/hpa_join.py            # use snapshot
uv run python projects/HUMAN_PROTEIN_ATLAS/scripts/hpa_join.py --refresh  # re-download
```

Outputs, all in `HUMAN_PROTEIN_ATLAS/data/`:

- `hpa_review_join.tsv`: every HPA-sourced annotation (`GO_REF:0000052` or
  `PMID:18029348`) in `genes/human/*/*-ai-review.yaml`, with our action and
  HPA's per-location grade
- `hpa_summary.md`: cross-tabulations
- `hpa_worklist.tsv`: annotations where the two frameworks disagree

Per-gene antibody details (antibody IDs, RRIDs, validation) are available
from `https://www.proteinatlas.org/<ENSG>.json`, under the `Antibody` and
`Subcellular location` keys.

## Baseline (2026-10-03)

There are **1,206** HPA-sourced annotations across **890** reviewed human genes.

| HPA per-location grade | ACCEPT | KEEP_AS_NON_CORE | MODIFY | OVER_ANNOTATED | REMOVE | UNDECIDED | total |
|---|---|---|---|---|---|---|---|
| Supported | 660 | 239 | 4 | 34 | 8 | 11 | 956 |
| Enhanced | 162 | 38 | 3 | 18 | 1 | 1 | 223 |
| Approved | 3 | 6 | 0 | 0 | 2 | 0 | 12 |
| Uncertain | 0 | 3 | 0 | 0 | 0 | 1 | 4 |
| absent in v25 / gene not found | 5 | 2 | 0 | 1 | 0 | 0 | 11 |

Early observations:

- We agree with most HPA calls: 69% ACCEPT and 24% KEEP_AS_NON_CORE.
- Enhanced calls are marked over-annotated more often than Supported calls
  (8.1% vs 3.6%). Most of these are mitochondrial import machinery (TOMM40,
  TOMM70, TOMM22, TIMM44, TIMM17A, PMPCB) where we prefer a sub-mitochondrial
  term. In these cases antibody validation is strong but the term is too general.
- **Additional** locations get KEEP_AS_NON_CORE far more often than **main**
  locations (38% vs 20%). This suggests an annotation extension or a
  main/additional flag would make the HPA data more useful.
- 16 annotations sit in GOA although v25 now grades the location Approved or
  Uncertain, and 7 more use a term v25 no longer reports for that gene. Examples are the EGFR and PTEN sperm-tail
  calls and the GAPDH nuclear-membrane call. These are stale exports.
- Some reviews cite `GO_REF:0000052` on reviewer-proposed `NEW` rows, including
  a biological-process term (PEX19 `peroxisome membrane biogenesis`). HPA only
  provides CC evidence, so these citations need fixing.
- Joining on gene symbol misses renamed genes, such as AIRIM and ATP5MD. The
  join should move to Ensembl or UniProt identifiers.

## Cilium atlas and sperm locations

HPA v24 and v25 added two cilia-related datasets to the Subcellular Section:

- **Primary cilium atlas** ([Hansen et al. 2025, *Cell*, PMID:41005307](https://doi.org/10.1016/j.cell.2025.08.039)).
  Antibody IF of primary cilia in three cell lines located 715 proteins to
  four sub-ciliary classes. The paper reports that 69% of the ciliary
  proteome is cell-type specific and that 78% of proteins vary between
  individual cilia.
- **Sperm flagellum and acrosome** locations from IF of human sperm.
  Related motile-cilia mapping in fallopian tube is in
  [Hikmet et al. 2026, PMID:42010243](https://doi.org/10.1038/s41467-026-71692-6).

HPA maps these classes to GO as follows:

| HPA class | GO term | Note |
|---|---|---|
| Primary cilium | GO:0005929 cilium | `primary cilium` (GO:0072372) is obsolete and replaced by `cilium`. `non-motile cilium` (GO:0097730) is the specific alternative |
| Primary cilium tip | GO:0097542 ciliary tip | |
| Primary cilium transition zone | GO:0035869 ciliary transition zone | |
| Basal body | GO:0036064 ciliary basal body | |
| Mid / Principal / End piece | GO:0097225 / GO:0097228 / GO:0097229 sperm midpiece / principal piece / end piece | |
| Connecting piece | GO:0120212 sperm head-tail coupling apparatus | |
| Flagellar centriole | GO:0005814 centriole | Generic. The sperm centrioles sit inside GO:0120212 |
| Acrosome | GO:0001669 acrosomal vesicle | |

Script: [HUMAN_PROTEIN_ATLAS/scripts/hpa_cilia.py](HUMAN_PROTEIN_ATLAS/scripts/hpa_cilia.py).
Outputs: `data/hpa_cilia_calls.tsv` (one row per gene and location) and
`data/hpa_cilia_summary.md`.

### Findings (2026-10-03)

| | Primary cilium | Sperm |
|---|---|---|
| Calls / genes | 1,144 / 757 | 1,238 / 596 |
| Enhanced | 0 | 6 |
| Supported | 178 (16%) | 119 (10%) |
| Approved | 524 (46%) | 1,087 (88%) |
| Uncertain | 442 (39%) | 26 (2%) |
| Calls on reviewed genes / already in GOA from HPA | 171 / 27 | 186 / 13 |

- **The cilium atlas is mostly invisible to GO.** None of its calls are
  Enhanced, and about 85% are Approved or Uncertain, so they are not
  exported. Only 27 of the 171 calls on genes we have reviewed are in GOA.
  This is a different situation from the main project. We are not
  re-evaluating annotations that already exist. We are deciding whether
  evidence that was never exported should become annotations.
- **Rough calibration by grade.** We counted reviewed genes whose review
  already has non-HPA ciliary or sperm support (a text match on cilia
  vocabulary in accepted annotations, core functions or description):

  | Best HPA grade | Primary cilium | Sperm |
  |---|---|---|
  | Supported | 18/19 (95%) | 5/6 (83%) |
  | Approved | 13/37 (35%) | 31/87 (36%) |
  | Uncertain | 12/53 (23%) | 0/4 (0%) |

  Supported calls agree with existing knowledge by definition. For Approved
  and Uncertain calls, two thirds of the genes have no other ciliary
  evidence in our reviews. These are either new ciliary proteins, which is
  the atlas's claim, or false positives.
- **Approved calls include both kinds.** Genuine ciliary genes include
  AHI1, CFAP300, CFAP418, ANKS6, DNAJB13, DYNLT2B, INTU and ADGRV1.
  Implausible ones include PHGDH, MAPK1, IDO1, TDO2, DDC, MTHFR and LRAT,
  metabolic enzymes and kinases with no ciliary literature in our reviews.
  A cilium IDA from one antibody in one cell line should not be accepted on
  its own.
- **Uncertain calls can still be right.** LZTFL1 (a BBSome regulator), NEK1
  and LRRK2 have Uncertain cilium calls but well-established ciliary
  biology. HPA's "Uncertain" grade reflects disagreement with UniProt or low
  RNA, not a failed antibody.
- **Sperm midpiece calls are often trivial.** The midpiece is packed with
  mitochondria, so Approved midpiece and principal-piece calls on
  respiratory-chain and TCA enzymes (NDUFB11, NDUFS2, ATP5F1D, DLAT, AIFM1,
  CPS1) are probably real. They add nothing beyond `mitochondrion`, and as
  annotations they would be over-annotations.
- **Some mappings are too generic.** `Flagellar centriole` → `centriole` loses
  the sperm context. `Primary cilium` → `cilium` loses the non-motile context
  that `non-motile cilium` would keep.

### Proposed handling

1. Do not treat Approved or Uncertain cilium-atlas calls as annotation
   evidence by themselves. Use them as **leads**: when a review has
   independent support (literature, IFT/BBSome interactions, ciliopathy
   genetics, CiliaCarta/SYSCILIA membership), cite PMID:41005307 as
   corroborating IDA.
2. For reviewed genes with ciliary biology but no cilium annotation, add
   `NEW` cilium terms citing the atlas plus the independent evidence, per the
   `NEW` rules in CLAUDE.md.
3. Treat the atlas's cell-type and single-cilium heterogeneity as context, not
   as a reason to reject. A protein seen in the cilia of one of three cell
   lines can still be a genuine ciliary component.
4. For sperm midpiece calls on mitochondrial proteins, do not propose
   annotations. `mitochondrion` already covers them.

## Approach

For each worklist annotation:

1. Check the HPA per-location grade, main vs additional, and the number of
   antibodies and cell lines that agree (from the gene JSON).
2. Classify the disagreement:
   - **SPECIFICITY**: the location is real but the HPA class is too coarse.
     Use MODIFY to the specific term, not MARK_AS_OVER_ANNOTATED.
   - **NON_FUNCTIONAL_SITE**: the staining is probably real but is not where
     the protein acts. Use KEEP_AS_NON_CORE.
   - **ARTIFACT**: diffuse or cross-reacting signal, an Uncertain or Approved
     grade, or a contradiction with tagged-protein or fractionation data. Use
     REMOVE or MARK_AS_OVER_ANNOTATED, citing the contradicting evidence.
   - **STALE**: HPA itself no longer supports the call. Flag it for HPA/GOA.
3. Make the review action consistent with the class, record the reasoning in
   the gene notes, and note HPA-side feedback below.
4. Follow the project rule: do not overrule an Enhanced call from the abstract
   alone. Enhanced calls carry orthogonal validation.

---
# STATUS

Last updated: 2026-10-03

## Setup
- [x] Download HPA v25 subcellular location data
- [x] Join HPA calls to existing human reviews (`hpa_join.py`)
- [x] Generate disagreement worklist (107 annotations, 86 genes)
- [ ] Switch the join key from symbol to Ensembl or UniProt (fixes renamed genes)
- [ ] Pull per-gene antibody count and validation method from the HPA JSON API into the join
- [ ] Decide whether to add an `hpa_class` (SPECIFICITY / NON_FUNCTIONAL_SITE / ARTIFACT / STALE) field to the review schema or keep it in notes

## Tier 2: stale exports (HPA v25 no longer supports the call)
- [ ] human/EGFR: cytosol (absent), cilium and ciliary basal body (Uncertain), sperm midpiece, principal and end piece (Approved)
- [ ] human/PTEN: sperm midpiece and principal piece (Approved)
- [ ] human/GAPDH: nuclear membrane (Uncertain)
- [ ] human/BRCA2: cytosol (Approved)
- [ ] human/CKAP2: nucleolus (absent), centrosome (Approved)
- [ ] human/INTU: cytosol and ciliary basal body (Approved)
- [ ] human/OLA1: centrosome (absent)
- [ ] human/SAMD8: cytosol (Uncertain; also Tier 1)
- [ ] human/SCN1A: nucleoplasm and nuclear body (Approved; also Tier 1, REMOVE)
- [ ] human/STAT1: nucleolus (absent; also Tier 1)
- [ ] human/PEX19, human/ADIRF: `GO_REF:0000052` cited on reviewer `NEW` rows. Fix the reference (PEX19 includes a BP term)
- [ ] human/AIRIM, human/ATP5MD: symbol mismatch, re-check after the join-key fix

## Tier 1: our review rejects or doubts an HPA call
Mitochondrial import machinery, probably SPECIFICITY:
- [ ] human/TOMM40, human/TOMM70, human/TOMM22, human/TOMM5, human/TOMM6
- [ ] human/TIMM44, human/TIMM17A, human/TIMM23, human/TIMM50, human/TIMMDC1
- [ ] human/PAM16, human/PMPCA, human/PMPCB, human/SAMM50, human/MTX2, human/CHCHD4, human/GFER

Possible artifacts or non-functional sites:
- [ ] human/ATP23 (plasma membrane, Enhanced; cell junction): REMOVE
- [ ] human/SYVN1 (nucleoplasm, plasma membrane): REMOVE
- [ ] human/GNAS (plasma membrane): REMOVE
- [ ] human/PEX5 (Golgi), human/SIRT2 (nucleolus), human/GCNT1 (nuclear speck), human/GTF2F2 (microtubule cytoskeleton): REMOVE
- [ ] human/FASN (plasma membrane, Enhanced), human/RPN1 (cytosol, Enhanced), human/PIGN (cytosol and plasma membrane, Enhanced)
- [ ] Nucleoplasm calls on cytoplasmic or organellar enzymes: human/NANS, human/PDXK, human/PGAM2, human/UPP1, human/NMRK2, human/NAALADL2, human/UROD, human/HMGCS1, human/MMACHC, human/SGPP1, human/CERS3, human/LRMDA, human/HRAS
- [ ] Remaining OVER_ANNOTATED: human/AHCTF1, human/BNIP3L, human/BRIP1, human/CKAP2, human/DOLK, human/ELOVL1, human/ILF3, human/MPDU1, human/NEU1, human/PDSS2, human/RFK, human/RPS3, human/SMOX, human/SPG11, human/STING1, human/TANK, human/TMEM63A
- [ ] UNDECIDED (needs a decision): human/APC, human/ARL13B, human/CDK7, human/COPS2, human/CRY2, human/DNAJB2, human/PTPN11, human/SERINC5, human/SIRT1, human/SYNE2, human/WEE1
- [ ] MODIFY (confirm replacement): human/AP1B1, human/CRY1, human/FLG, human/MORC3, human/TRAPPC12

## Cilium atlas (PMID:41005307) and sperm locations
- [x] Characterize cilia/sperm calls by grade, GOA export and independent support (`hpa_cilia.py`)
- [ ] Fetch PMID:41005307 into `publications/` (`just fetch-gene` will not pull it; use the publication fetcher) so reviews can quote it
- [ ] Get the per-protein supplementary table (cell line, sub-ciliary class, heterogeneity) and add it to the join
- [ ] Build a positive and negative control set (CiliaCarta / SYSCILIA gold standard vs non-ciliary housekeeping proteins) to calibrate Approved and Uncertain precision properly, replacing the text match
- [ ] Ciliary genes in our reviews with Approved/Uncertain atlas calls and no cilium annotation: decide on `NEW` with corroborating evidence (start with human/AHI1, human/ANKS6, human/LZTFL1, human/NEK1, human/DYNLT2B, human/DNAJB13, human/CFAP418)
- [ ] Implausible Approved calls: record as atlas false-positive candidates (human/PHGDH, human/MAPK1, human/IDO1, human/TDO2, human/DDC, human/MTHFR, human/LRAT)
- [ ] Raise with GO/HPA: `Flagellar centriole` → `centriole` and `Primary cilium` → `cilium` lose context

## Tier 3: not yet reviewed
- [ ] Scope new reviews of genes with Enhanced main-location calls that have no review yet

# NOTES

## 2026-10-03

- Created the project. Downloaded HPA v25 `subcellular_location.tsv` and wrote
  `hpa_join.py` to join it with HPA-sourced GOA rows in our reviews.
- GOA receives HPA rows only as IDA / `GO_REF:0000052`. Almost all of them are
  Supported (956) or Enhanced (223) in v25. The 16 Approved, Uncertain or absent
  rows are probably exports from earlier releases that HPA has since downgraded.
- Most disagreements are about specificity (mitochondrial classes), not
  artifacts. Before marking an HPA call over-annotated, consider whether
  MODIFY to the specific term is more accurate.

- Added the cilium atlas analysis (`hpa_cilia.py`). The atlas is
  PMID:41005307. Almost none of it reaches GOA because about 85% of calls are
  Approved or Uncertain. Calibrated against our reviews, about a third of
  Approved calls have independent ciliary support. Use the atlas as leads and
  corroboration, not as standalone IDA evidence.

## HPA / GOA feedback (to collect)

- `GO_REF:0000052` describes literature-gated export, but Enhanced
  (orthogonally validated) calls are exported as well. The description should
  be updated.
- Stale exports that HPA itself has downgraded (see Tier 2).
- The cilium atlas mappings `Flagellar centriole` → `centriole` and
  `Primary cilium` → `cilium` could use `sperm head-tail coupling apparatus`
  and `non-motile cilium`.
