# CYP79B3 (At2g22330, Q501D8) curation notes

## 2026-10-03 — initial review (claude-code)

Sources: UniProt Q501D8, GOA (25 rows), Falcon deep research
(`CYP79B3-deep-research-falcon.md`), cached publications, and the completed
paralog review `genes/ARATH/CYP79B2/CYP79B2-ai-review.yaml` (kept strictly
consistent). Module: `modules/camalexin_biosynthesis.yaml`, annoton
`cyp79b_activity` (GO:0090489, ER membrane) — this review agrees.

### Activity
- Hull et al. 2000 cloned CYP79B2 and CYP79B3 and showed both convert Trp to IAOx
  in E. coli membrane extracts [PMID:10681464 "We have identified two Arabidopsis
  cytochrome P450s (CYP79B2 and CYP79B3) that can convert Trp to
  indole-3-acetaldoxime (IAOx), a precursor to IAA and indole glucosinolates."].
  Only the abstract is cached; deep research (Fig. 2C) confirms CYP79B3 was assayed
  directly, not by inference from CYP79B2.
- UniProt: EC 1.14.14.156, RHEA:33279, reaction uses reduced
  [NADPH--hemoprotein reductase] (flavoprotein donor) -> GO:0090489 sits under
  GO:0016712, not GO:0016709 (same correction as CYP79B2).
- No CYP79B3-specific kinetics or substrate panel; Phe/Tyr negative tests were done
  on CYP79B2 only (deep research).
- GOA has only an IEA for GO:0090489 on CYP79B3; there is no experimental MF row,
  although Hull 2000 is a direct assay. Proposed NEW GO:0090489 (IDA, PMID:10681464).

### Pathways (shared IAOx branch point)
- Camalexin and indole glucosinolates: double mutant devoid of both; labelled IAOx
  is incorporated into camalexin [PMID:15148388 "These results demonstrate that only
  CYP79B2 and CYP79B3 contribute significantly to the IAOx pool from which camalexin
  and indole glucosinolates are synthesized."].
- Paralog difference: [PMID:15148388 "the transcript level of CYP79B2, but not
  CYP79B3, is increased upon induction of camalexin by silver nitrate"]. So CYP79B2
  is the main pathogen-induced contributor; CYP79B3 still catalyses the same step.
- IAA: [PMID:12464638 "cyp79B2 cyp79B3 double mutants have reduced levels of IAA and
  show growth defects consistent with partial auxin deficiency."]; root IAA synthesis
  reduced [PMID:15772288 "Root-localized IAA synthesis was diminished in a cyp79B2
  cyp79B3 double knockout"]. Minor route; non-core.
- CYP79B3-GUS in roots around lateral root primordia [PMID:15772288 "CYP79B3 -GUS was
  expressed in cells of the primary root that surround LRP"].

### Localization
- UniProt: single-pass membrane protein (TM 22-42), signal anchor typical of ER P450s.
- No direct CYP79B3 localization in the cache. Deep research notes an old N-terminal
  GUS fusion that went to plastids, contradicted by predictions and P450 biology, and
  unresolved. CYP79B2 colocalizes with ER CYP71A13 (Mucha 2019). Treated ER membrane
  as the location by family inference (IBA accepted) and chloroplast ISM as
  over-annotation (not REMOVE, since a plastid fusion report exists).
- CYP79B3 is NOT part of the ComplexPortal camalexin metabolon rows (no NAS rows for
  B3 in GOA), unlike CYP79B2.

### Defence phenotypes (all double mutant, all upstream necessity)
- P. brassicae susceptibility [PMID:20230487], mlo2 antifungal defence
  [PMID:20023151], flg22 callose [PMID:19095898], Pf.SS101 ISR [PMID:23073694].
  Kept as non-core, matching CYP79B2. Did not add `defense response to fungus`:
  CYP79B3 makes a precursor; the antifungal work is done by camalexin and indole
  glucosinolate hydrolysis products (PAD3, PEN2, CYP81F2 sides).
- SAR (GO:0010112, IEP, Truman 2010, abstract only): indole compounds implicated in
  SAR [PMID:20081042 "our data provide compelling evidence for a role of
  indole-derived compounds, but not auxin itself, in the establishment and
  maintenance of systemic immunity"]. An expression change does not show that a
  biosynthetic enzyme regulates SAR -> MARK_AS_OVER_ANNOTATED.
- Wounding (IEP, PMID:17675405): microarray list of JA-dependent wound-inducible
  genes; CYP79B3 not named in main text (presumably in supplementary list). Kept
  non-core; JA/wound inducibility of CYP79B3 is consistent with deep research
  (MeJA 3.5-fold induction, Mikkelsen 2003).
- Aphid (IEP, PMID:23144921): [PMID:23144921 "B. brassicae induced expression of
  CYP79B2 and CYP79B3 under drought and water-logged conditions"]. Non-core.
