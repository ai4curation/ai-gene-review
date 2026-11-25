# hutF (PA5106, Q9HU77) notes

## Identity

- UniProt Q9HU77 (HUTF_PSEAE), 453 aa, Swiss-Prot reviewed. N-formimino-L-glutamate
  deiminase (formimidoylglutamate deiminase, FIGLU iminohydrolase, EC 3.5.3.13).
  Amidohydrolase superfamily, HutF family (InterPro IPR010252, NCBIfam TIGR02022,
  Pfam PF22429 HutF_N; PANTHER PTHR11271:SF48). Five PDB structures (3MDU, 3MDW,
  4RDV, 4RDW, 4RZB). Zinc ligands His56, His58, His232, Asp320; His269 general base.
- In the PAO1 hut cluster; first enzyme of the five-step (deiminase) FIGLU branch,
  followed by HutG (PA5091, N-formylglutamate amidohydrolase). The four-step branch
  uses HutE (PA3175, FIGLU iminohydrolase/formiminoglutamase), outside the operon.

## Biology (literature)

- Functional assignment by enzymology:
  [PMID:16475788 "The protein Pa5106 was shown to catalyze the deimination of N-formimino-L-glutamate to ammonia and N-formyl-L-glutamate, while Pa5091 catalyzed the hydrolysis of N-formyl-L-glutamate to formate and L-glutamate."].
  Two competing FIGLU routes coexist in P. aeruginosa
  [PMID:16475788 "The reason for the coexistence of two alternative pathways for the degradation of N-formimino-L-glutamate in P. aeruginosa is unknown."].
- Mechanism: Zn-dependent; mutation of Glu235, His269 or Asp320 drops activity
  2-6 orders of magnitude
  [PMID:17128965 "The mutation of Glu-235, His-269, or Asp-320 resulted in the diminution of catalytic activity by two to six orders of magnitude."].
- Structure with inhibitors; single zinc in the active site
  [PMID:25559274 "The active site of Pa5106 contains a single zinc atom that is coordinated by His-56, His-58, His-232, and Asp-320."].
- Lessie and Neidhardt 1967 (the PseudoCAP IMP reference; abstract only here,
  PMC276695 is a scanned article and could not be read, rechecked 2026-10-29)
  reports measurements of histidase,
  urocanase and "the capacity to degrade formiminoglutamate" (step IV) in
  P. aeruginosa extracts, with urocanase-deficient, auxotrophic and repression
  mutants [PMID:4290562 "Histidine ammonia lyase (histidase), urocanase, and the capacity to degrade formiminoglutamate, which are respectively involved in steps I, II, and IV in the catabolism of histidine"].
  Two enzymes degrade FIGLU in PAO1 (HutF and HutE), so the step IV activity of a
  1967 extract cannot be attributed to PA5106, and no hutF mutant appears in the
  abstract. Because that second point rests on the abstract's silence, the
  WRONG_REFERENCE defect is recorded as SUSPECTED rather than PROBABLE.

## Consistency with completed reviews

- genes/PSEAE/hutH: same 1967 paper judged SOUND for histidase (step I assayed
  directly and only one functional HAL in PAO1); IMP should be IDA.
- genes/PSEAE/hutI: same paper judged UNVERIFIABLE (step III not mentioned in the
  abstract); its reference defects are likewise SUSPECTED.
- hutF: step IV is mentioned, but only as a pooled extract activity that two
  different PAO1 enzymes provide, and without a hutF mutant. The IMP cannot tie the
  process to PA5106, so the verdict is UNVERIFIABLE, as for hutI. The claim itself is
  correct and supported independently by PMID:16475788.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000138516 | GO:0006548 L-histidine catabolic process | 1 (sole seed) | 8 (8 taxa) | GO:0006548 L-histidine catabolic process, IMP, PMID:4290562 (PseudoCAP) | UNVERIFIABLE | The 1967 abstract measures a pooled FIGLU-degrading capacity (step IV) that HutF and HutE both provide, and describes no hutF mutant; as a pre-cloning study it cannot assign anything to PA5106. The claim is correct (HutF catalyses the first step of the deiminase FIGLU branch, PMID:16475788), so the IBD conclusion is sound for HutF-family leaves; the anchor should be PMID:16475788. Node breadth: three nematode leaves (C. elegans cpin-1 Q20166, C. briggsae, Pristionchus) lack the HutF family signatures (IPR010252, TIGR02022, HutF_N) that the bacterial leaves carry; their IBAs may be over-propagation. |
| PTN000138516 | GO:0050416 formimidoylglutamate deiminase activity | 1 (sole seed) | 8 (8 taxa) | GO:0050416 formimidoylglutamate deiminase activity, IDA, PMID:16475788 (PseudoCAP); also UniProt EXP PMID:17128965 | SOUND | Purified PA5106 deiminates FIGLU to N-formylglutamate and ammonia, with kinetics, metal dependence and mutagenesis (PMID:17128965) and structures (PMID:25559274). The term suits the bacterial HutF leaves (all TIGR02022). Same nematode caveat. |

## Decisions summary

- ACCEPT: formimidoylglutamate deiminase activity (IBA, IEA, EXP, IDA), L-histidine
  catabolic process (IBA, IMP), cytosol (IBA).
- MODIFY to GO:0050416: hydrolase activity, hydrolase activity acting on C-N bonds
  (descendants); deaminase activity (lateral: GO:0050416 is not placed under
  GO:0019239 in GO).
- Source defects: PSEUDOCAP WRONG_REFERENCE CHECK (PROBABLE) on the IMP row, re-key
  to PMID:16475788; GO_CENTRAL CHECK (SUSPECTED) on PTN000138516 for re-anchoring the
  BP IBD and for the nematode leaves (raised to CONFIRMED after the tree check below).

## Full-text check of PMID:4290562 (2026-11-05)

The full text of Lessie and Neidhardt 1967 (J Bacteriol 93, 1800-1810) was supplied by the user and read. Its mutants are a urocanase-deficient strain, a histidine auxotroph and regulatory mutants with altered repression. Step IV is measured only as crude-extract formiminoglutamate degradation (shared by HutF and HutE in PAO1) and there is no hutF mutant. The WRONG_REFERENCE defect on the IMP row is now CONFIRMED and the reference is marked MISCITED.

## PANTHER tree check (2026-11-05)

Topology fetched with `projects/PSEUDOCAP/panther_tree.py node PTN000138516 --depth 5
--leaves` (PTHR11271). PTN000138516 is the family's LUCA SPECIATION root; every leaf is
subfamily PTHR11271:SF48.

| Child node | Event / taxon | Leaves | Subfamilies | Verdict |
|---|---|---|---|---|
| PTN000884852 | SPECIATION, Rhabditida-Chromadorea | 3 (Q20166 cpin-1, A8Y0T4 cpin-1, A0A2A6BT36) | SF48:3 | Over-propagated: no HutF signatures, no known histidine-degradation route |
| PTN000138520 | SPECIATION, Eubacteria | 5 (Q9HU77 hutF, Q9KZ77, Q89GV1, Q8PAA5 sdeB, Q9ZC76) | SF48:5 | Correct anchor for both IBDs |
| PTN000138522 | SPECIATION, Proteobacteria | 4 | SF48:4 | Narrower option |
| PTN001681702 | SPECIATION, Gammaproteobacteria | 3 (Q8PAA5, Q9HU77, Q9ZC76) | SF48:3 | Narrowest clade option; smallest clade holding Q9HU77 is its own leaf PTN002462020 |

The earlier concern is confirmed by the topology: the nematode leaves are not scattered
through the tree but form one clean child clade, so moving the GO:0006548 and GO:0050416
IBDs from PTN000138516 to PTN000138520 removes all three unsupported leaf IBAs without
touching any bacterial leaf. Note that within the bacterial clade only Q9HU77 is a
characterised formimidoylglutamate deiminase; the other four leaves are named
chlorohydrolase/hydrolase, which the tree cannot resolve further - that would need
enzymology on one of Q9KZ77, Q89GV1, Q8PAA5 or Q9ZC76. The P. aeruginosa leaf IBAs
reviewed here are unaffected (ACCEPT stands).
