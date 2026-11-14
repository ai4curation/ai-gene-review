# wbpA (PA3159, G3XD94) notes

Sources read on 2026-11-05: UniProt G3XD94 (UGND_PSEAE), the GOA file, cached abstracts
of PMID:15226302, PMID:10930727, PMID:8939432 and the cached full text of PMID:18621892.
No deep-research provider file (no keys). Related reviews: genes/PSEAE/wbpI (shares
PMID:10930727), wbpD, wbpE.

## Biology

- WbpA is the first enzyme of the five-step WbpA-WbpB-WbpE-WbpD-WbpI pathway to
  UDP-D-ManNAc3NAcA, a precursor of the serotype O5 B-band O antigen
  [PMID:18621892 "A five-enzyme biosynthetic pathway that requires WbpA, WbpB, WbpE, WbpD, and WbpI has been proposed for the production of this sugar in P. aeruginosa"].
- Purified His-WbpA is a UDP-GlcNAc 6-dehydrogenase (EC 1.1.1.136) using NAD+; product
  UDP-GlcNAcA confirmed by NMR; requires NH4+ or K+; trimer in solution
  [PMID:15226302 "the data revealed that WbpA is a UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136), which uses NAD(+) as a coenzyme"].
- wbpA knockout loses B-band LPS
  [PMID:10930727 "Specific knockout mutations in the putative UDP-D-N-acetylglucosamine (UDP-D-GlcNAc) epimerase gene, wbpI, or the putative UDP-D-N-acetylmannosamine dehydrogenase gene, wbpA, resulted in strains that no longer produced B-band lipopolysaccharide"];
  restored by His-WbpA in trans (PMID:18621892 full text,
  "The wbpA knockout of P. aeruginosa PAO1 is devoid of B-band O antigen but still produces A-band O antigen in a variety of lengths.").
- In PMID:18621892 the enzymes assayed by capillary electrophoresis were the B. pertussis
  WbpO homologs, not WbpA; NADH was detected as a product of those reactions. WbpA itself
  appears only in knockout and complementation experiments in that paper.
- Sequence check: the UniProt TRANSMEM 13-32 (ECO:0000255, a prediction) covers
  SRQALIGIVGLGYVGLPLML, which contains the GxGxxG dinucleotide-binding motif of the
  Rossmann fold (G22-L-G-Y-V-G27) at the N-terminus of the UDP-glucose/GDP-mannose
  dehydrogenase family. This is the NAD-binding beta-alpha-beta unit, not a membrane
  anchor; the enzyme was purified and characterised as a soluble oligomer
  (PMID:15226302).

## Annotation judgements

- GO:0047004 (EXP, IEA): ACCEPT, core MF.
- GO:0003954 NADH dehydrogenase activity (PseudoCAP EXP, PMID:18621892): REMOVE. NADH
  dehydrogenase activity is NADH oxidation (NADH + acceptor -> NAD+); WbpA reduces NAD+
  to NADH. In the cited paper the activity assay was on B. pertussis WbpO, not WbpA.
  The correct term (GO:0047004) is already annotated from PMID:15226302. CONFIRMED
  (full text read).
- GO:0016628 (CH-CH donors) InterPro2GO from IPR028359: wrong sub-class; the enzyme
  oxidises the C6 alcohol (EC 1.1.1.x, CH-OH donors). REMOVE, INTERPRO defect.
- GO:0016616 (CH-OH donors) and GO:0016491: TOO_GENERAL (entailed by GO:0047004).
- GO:0000271: TOO_GENERAL (entailed by GO:0009243 O antigen biosynthetic process).
- GO:0009243 (EXP, IEA): ACCEPT, core BP.
- GO:0016020 membrane (IEA, UniProt SubCell from a predicted TM helix): REMOVE; the
  predicted helix is the Rossmann GxGxxG motif.
- GO:0051287 NAD binding: ACCEPT (NAD+ coenzyme, Rossmann motif).

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000890018 | GO:0016491 oxidoreductase activity | 2 | 30 (25 taxa) | GO:0003954 NADH dehydrogenase activity, EXP, PMID:18621892 (PseudoCAP) | WRONG | Full text: WbpA was only knocked out and complemented in this paper; the assayed dehydrogenases were B. pertussis WbpO, and NADH is the product, not the substrate. PSEUDOCAP WRONG_TERM, CONFIRMED. | E. coli WecC P27829 (EcoCyc IDA GO:0089714 UDP-N-acetyl-D-mannosamine dehydrogenase activity, PMID:381306) | Yes; WecC alone supports it, and WbpA's own GO:0047004 seed is sound |
| PTN000890018 | GO:0016491 oxidoreductase activity | 2 | 30 (25 taxa) | GO:0047004, EXP, PMID:15226302 (PseudoCAP) | SOUND | Abstract: purified WbpA converts UDP-GlcNAc to UDP-GlcNAcA with NAD+, product confirmed by NMR, kinetics measured. (IDA would be the usual code; EXP is acceptable.) | as above | Yes |
| PTN000146785 | GO:0000271 polysaccharide biosynthetic process | 2 | 17 (15 taxa) | GO:0000271, IDA, PMID:15226302 (PseudoCAP) | SOUND | WbpA makes the first nucleotide-sugar precursor of B-band O antigen; it does a step of the pathway. | E. coli WecC P27829 (EcoCyc IMP GO:0009246 enterobacterial common antigen biosynthetic process, PMID:2166030; is_a GO:0000271) | Yes |
| PTN000146785 | GO:0000271 polysaccharide biosynthetic process | 2 | 17 (15 taxa) | GO:0009243 O antigen biosynthetic process, EXP, PMID:18621892 (PseudoCAP) | SOUND | Full text: wbpA knockout lacks B-band O antigen and His-WbpA in trans restores it (mutant evidence; IMP would be the usual code). | as above | Yes |

Both node terms are broad and suit clades of nucleotide-sugar dehydrogenases feeding
ECA, capsule and O antigen. No GO_CENTRAL defect. Consistent with wbpI, where the
PTN001056041 polysaccharide-biosynthesis seed from PMID:10930727 was also judged SOUND.

Defects recorded: PSEUDOCAP WRONG_TERM on GO:0003954 (CONFIRMED); INTERPRO WRONG_TERM on
the IPR028359 -> GO:0016628 mapping (CONFIRMED); UNIPROT on the predicted TM segment
behind GO:0016020 (PROBABLE).
