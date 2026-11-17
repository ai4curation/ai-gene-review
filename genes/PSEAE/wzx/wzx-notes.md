# wzx (PA3153, G3XD19) notes

## Literature

No deep-research provider was available. Full texts cached for PMID:20824106, PMID:22554073 and
PMID:24023388; abstracts only for PMID:9922263 and PMID:8606190.

- Integral IM protein [PMID:20824106 "requiring the integral inner membrane proteins Wzx (O-antigen [O-Ag]
  flippase), Wzy (O-Ag polymerase), and WaaL (O-Ag ligase)"]; topology resolved into cytoplasmic, TM and
  periplasmic regions [PMID:20824106 "allowed for the assignment of specific regions of the proteins to
  cytoplasmic, transmembrane (TM), or periplasmic loci"].
- Proton-coupled antiport [PMID:24023388 "allow for the first H(+)-dependent antiport mechanism to be
  proposed for lipid-linked oligosaccharide translocation across the bacterial IM"].
- Mutants lose B-band LPS [PMID:9922263 "led in both cases to the loss of B-band lipopolysaccharide (LPS)
  O-antigen production"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001250140 | GO:0005886 plasma membrane | 5 | 101 (33 taxa) | GO:0005886, IDA, PMID:24023388 (PseudoCAP) | SOUND | Full text: membrane-fraction recovery of the overexpressed fusion; IM topology shown in PMID:20824106. | E. coli P0AAA7, P37746, P77377, Q46841 | Yes. |
| PTN001250140 | GO:0005886 plasma membrane | 5 | 101 (33 taxa) | GO:0098567 periplasmic side of plasma membrane, IDA, PMID:20824106 (PseudoCAP) | WRONG | Full text: Wzx is a 12-TM integral protein with loops on both sides, not a periplasmic-face protein. PSEUDOCAP WRONG_TERM defect, CONFIRMED. | as above | Yes, on the sound GO:0005886 seed and four E. coli seeds; no GO_CENTRAL defect. |

Consistent with the pmpM review (tier 2), where a periplasmic-side row on a polytopic transporter was
also judged WRONG.

## Other decisions

- GO:0009276 Gram-negative cell wall (PseudoCAP IDA, PMID:9922263): REMOVE, PSEUDOCAP WRONG_TERM,
  PROBABLE (abstract only; independent topology data place Wzx in the IM).
- GO:0016020 membrane: MODIFY to GO:0005886.
- GO:0015774 polysaccharide transport (ISS) and GO:0055085 (IEA): MODIFY to GO:0034203 glycolipid
  translocation (Wzx flips single lipid-linked repeat units).
- GO:0043165 outer membrane assembly: KEEP_AS_NON_CORE.
- GO:0015297 antiporter activity: ACCEPT; no proton-coupled flippase term exists (floppase terms are
  ATP-driven). Raised as a suggested question.
- Consistent with Q9HTB8 (wzm): plasma membrane accepted, generic membrane modified to plasma membrane,
  O antigen biosynthesis accepted.
