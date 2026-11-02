# Atp2a2 (rat) review notes

## Session 1 (2026-10-28)

- fetch-gene resolved P11507 (AT2A2_RAT, RGD:2174, GeneID 29693); 111 GOA rows.
- No deep-research API keys; literature synthesis written by hand in
  `Atp2a2-deep-research-manual.md`.
- Full text read: PMID:20177054, PMID:21300842, PMID:24610369. Others abstract-only.

### Key judgements

- Core: P-type Ca2+ pump (GO:0005388) moving Ca2+ from cytosol into ER/SR lumen
  (GO:1903515, GO:1990036) in ER/SR membrane [PMID:21300842 "its ability to
  hydrolyze ATP and transport Ca(2+) was significantly reduced"]. SERCA2a drives
  cardiac relaxation [PMID:9851937].
- GO:0031234 extrinsic component of cytoplasmic side of plasma membrane (RGD IDA,
  PMID:20177054) is a wrong term: the paper places SERCA2b in subplasmalemmal SR
  ("SERCA2b serves an SR compartment proximal to the plasma membrane"); SERCA2 is a
  multi-pass ER/SR membrane protein. MODIFY to GO:0033017 + source_defect (RGD).
- GO:0016240 autophagosome membrane docking (ISO/ISS from human UniProt IDA,
  PMID:28890335): the paper is about ER-isolation membrane contacts in autophagosome
  formation, not autophagosome docking in maturation. Over-annotated; source_defect.
- GO:0045822 negative regulation of heart contraction (ISO from MGI IGI,
  PMID:10555147 with Pln): the negative regulator is PLN; SERCA2a overexpression
  increases contractility [PMID:9851937]. Direction looks wrong for SERCA2;
  source_defect CHECK to MGI.
- Mouse acts_upstream_of_or_within phenotype rows (T-tubule organization, fiber-type
  transition, hypertrophy, apoptosis, ER-nucleus signalling, oxidative stress,
  neurotransmitter exocytosis): consequences of Ca2+ mishandling; marked
  over-annotated.
- GO:0034605 cellular response to heat (RGD IEP, PMID:10748035): abstract names ER
  stress agents (tunicamycin, DTT, AZC), not heat. Abstract-only -> UNDECIDED.
- GO:0086036 / GO:0098909 (BHF-UCL IDA PMID:9851937): abstract gives no membrane
  potential/action potential data; full text not available -> UNDECIDED.
- Precomposed GO:0086039 -> MODIFY to GO:0005388 (context dropped: SERCA2's effect
  on sarcolemmal potential is indirect, via cytosolic Ca2+ and NCX).
- No NEW rows: phenotype/expression data do not justify new process terms.
