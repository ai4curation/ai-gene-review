# wbpE (PA3155, Q9HZ76) notes

No deep-research provider was available; literature research done from the cached papers
(full text for PMID:18621892, PMID:19348502, PMID:20604544; abstract for PMID:19282284).

## Biology

- WbpE is the third enzyme of the UDP-ManNAc3NAcA pathway (WbpA-WbpB-WbpE-WbpD-WbpI)
  [PMID:19348502 "is thought to be produced by five enzymes (WbpA, WbpB, WbpE, WbpD, and WbpI) in a
  stepwise manner starting from UDP-GlcNAc"].
- Coupled activity with WbpB [PMID:19282284 "Activities of His(6)-WbpB and His(6)-WbpE were detected
  only when both proteins were combined in the same reaction."]; [PMID:19348502 "WbpB and WbpE are a
  dehydrogenase/aminotransferase pair that converts UDP-GlcNAcA to UDP-GlcNAc(3NH(2))A in a coupled
  reaction"].
- PLP structure, homodimer [PMID:20604544 "we present the crystal structure of the aminotransferase
  WbpE from P. aeruginosa PAO1 in complex with the cofactor pyridoxal 5'-phosphate (PLP)"].
- Knockout lacks B-band O antigen; complemented by B. pertussis wlbC [PMID:18621892 "The evidence
  presented here demonstrates that B-band O antigen is not produced when wbpB or wbpE is knocked out in
  P. aeruginosa"].
- No GO MF term for EC 2.6.1.98; GO:0008483 transaminase activity is the most specific.

### Annotation decisions

- GO:0008483 (EXP, IDA, IBA, IEA): ACCEPT, core MF.
- GO:0030170 (IDA, IBA, IEA): ACCEPT.
- GO:0009243 (EXP, IDA, IEA): ACCEPT.
- GO:0000271 (IBA, IDA) and GO:0009103 (IDA): TOO_GENERAL (GO:0009243 is an is_a descendant).
- GO:0006065 UDP-glucuronate biosynthetic process (EXP, PseudoCAP): MODIFY to GO:0009226; PSEUDOCAP
  WRONG_TERM, CONFIRMED (abstract names the product UDP-GlcNAc3NA). Same error as on wbpD.
- Action counts: ACCEPT 10, TOO_GENERAL 3, MODIFY 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001250039 | GO:0000271 polysaccharide biosynthetic process | 2 | 98 (45 taxa) | GO:0000271, IDA, PMID:19282284 (PseudoCAP) | SOUND | Purified WbpE makes a nucleotide-sugar precursor of the O antigen; the term is general but true. | E. coli WecE P27833 (ECA TDP-Fuc4NAc aminotransferase) | Yes; WecE makes a polysaccharide (ECA) precursor, so the general node term fits the clade |
| PTN001250039 | GO:0008483 transaminase activity | 6 | 95 (45 taxa) | GO:0008483, EXP, PMID:19282284 (PseudoCAP) | SOUND | Coupled WbpB/WbpE assay with purified protein; confirmed by IDA in PMID:19348502 and the PLP-product structure. | WecE P27833, ArnB P77690 and Q8ZNF3, NtdA O07566, Pat Q814Z4 | Yes; five other characterised sugar aminotransferases |

No GO_CENTRAL defect. The only PSEUDOCAP defect on wbpE is the non-seed GO:0006065 row.
