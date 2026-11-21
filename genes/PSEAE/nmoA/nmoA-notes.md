# nmoA (PA4202, Q9HWH9) — curation notes

## Gene identity

UniProt Q9HWH9, `NMO_PSEAE`, 351 aa, reviewed; PseudoCAP PA4202; matches the
worklist accession. Named nmoA in PMID:25384477; UniProt RecName "Nitronate
monooxygenase", EC 1.13.12.- with `ECO:0000269|PubMed:25002579`. PDB 4Q4K
(1.44 A, with FMN); PANTHER PTHR42747:SF3.

## What is established

- Purified, kinetically characterised enzyme. PA4202 was cloned, expressed and
  purified, and is active on propionate 3-nitronate (P3N) and other alkyl
  nitronates but not on nitroalkanes [PMID:25002579 "The enzyme is active on
  P3N and other alkyl nitronates, but cannot oxidize nitroalkanes."]. P3N is
  the best substrate (kcat app 1300 s-1, Km app 110 uM); UniProt also records
  Km 5 mM for ethylnitronate and 6 mM for propyl-1-nitronate.
- Cofactor and fold. "Absorption spectroscopy, mass spectrometry, and x-ray
  crystallography demonstrate a tightly, non-covalently bound FMN in the active
  site of the enzyme" [PMID:25002579]; UniProt CC:COFACTOR "Binds 1 FMN per
  subunit", with binding sites at 21, 69, 176, 181, 218 and 237-240 from
  PDB 4Q4K. TIM-barrel fold. A flavosemiquinone forms within 7.5 ms on
  anaerobic reduction with P3N, consistent with a catalytic intermediate.
- Class definition. Four motifs shared with the fungal NMO of
  *Cyberlindnera saturnus* define class I NMO (bacterial, fungal, two animal);
  *Neurospora crassa* NMO lacks them and defines class II [PMID:25002579].
- In vivo role. A chromosomal deletion is less tolerant of 3-NPA
  [PMID:25384477 "Finally, deletion of the nmoA gene resulted in an increased
  sensitivity of the cells to 3-nitropropionic acid (3-NPA), confirming the role
  of the nitronate monooxygenase protein in the detoxification of nitronate."],
  and "The Δ nmoA mutant was clearly less able to grow in the presence of high
  concentrations of P3N."; the mutant also fails to show the dose-dependent
  nitrite release seen in wild type and in the ΔnmoR mutant.
- Regulation. "Here we show that PA4203 ( nmoR ) represses its own transcription
  and the expression of nmoA." [PMID:25384477]; nmoA is cotranscribed with ddlA
  but ddlA has an internal promoter.
- Pathway context. 3-NPA/P3N can serve pseudomonads as sole carbon, nitrogen and
  energy source, via P3N denitration to malonic semialdehyde and then acetyl-CoA
  [PMID:20382807 "Stoichiometry of the reaction indicates that the enzyme is a
  monooxygenase."]. That enzyme was purified from 3NPA-degrading isolates, not
  from PAO1, so for PAO1 the catabolic role is plausible but not shown.

## Relevance of other PAO1 NMO-family members

- PA0660 (Q9I5R1) is a leaf of the same PAINT node and was purified: "Despite
  its annotation, PA0660 did not exhibit nitronate monooxygenase activity."
  [PMID:31075192]; it is an NAD(P)H:quinone reductase and the proposed paradigm
  of a new class defined by six conserved motifs.
- PA1024 (Q9I4V0, already reviewed in this repository) is likewise an
  NADH:quinone reductase with no NMO activity, in a different PANTHER family
  (PTHR32332).
- PMID:29885842 reports a PA4202 ternary complex with neutral nitroethane and
  low-efficiency nitroalkane turnover via H183. This is a minor in vitro
  activity, not a reason to annotate nitroalkane oxidase activity (GO:0052664);
  UniProt's FUNCTION explicitly says PA4202 cannot oxidise nitroalkanes.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001284536 | GO:0018580 nitronate monooxygenase activity | 1 (sole seed) | 23 (19 taxa, PAINT leaf GAF) | GO:0018580, IDA, PMID:25002579 (PseudoCAP) | SOUND (seed); node over-broad | The seed is a direct enzyme assay on purified NmoA, not a mutant phenotype: steady-state kinetics on P3N and other alkyl nitronates, tightly bound FMN, a semiquinone intermediate and a 1.44 A structure. A sole seed is not weak support here. The node term is however carried to at least one leaf where it is experimentally false: P. aeruginosa PA0660 (Q9I5R1) has no NMO activity and is an NAD(P)H:quinone reductase (PMID:31075192). Recorded as a GO_CENTRAL `WRONG_TERM`/CHECK defect asking for a NOT at the PA0660 branch or for the IBD to move down to the class I (four-motif) group. The PseudoCAP row itself needs no defect. |

PseudoCAP has only this one annotation for PA4202, so no other seed needs
assessment.

## Decisions summary

- ACCEPT: GO:0018580 IDA (the seed), IEA (InterPro IPR004136), IBA.
- NEW: GO:0010181 FMN binding (IDA, PMID:25002579); GO:0070458 cellular
  detoxification of nitrogen compound (IMP, PMID:25384477) — NmoA is itself the
  enzyme that removes the nitronate, so this is participation, not necessity.
- No REMOVE. One GO_CENTRAL source defect at PTN001284536; no PseudoCAP defect.
