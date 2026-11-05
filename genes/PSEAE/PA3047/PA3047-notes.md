# PA3047 (Q9HZG1) notes

Penicillin-binding protein 4 (PBP4, dacB), peptidase S13 family, predicted signal peptide
(SignalP 1-22). No deep-research provider was available; literature search by hand (full text
of PMID:25495032 in the cache, PMC4304477; QuickGO for the E. coli DacB and Dictyostelium pscA
seeds).

## Literature

- Lee et al. 2015 (PMID:25495032; full text): purified PBP4 (residues 23-476) is a bifunctional
  DD-carboxypeptidase/4,3-endopeptidase ["PBP4 is a bifunctional enzyme having both
  dd-carboxypeptidase and endopeptidase activities."; "The endopeptidase activity is specific to
  hydrolysis of 4,3-cross-linked peptidoglycan."; "PBP4 catalyzes both reactions equally well."].
  The DD-carboxypeptidase assay used synthetic pentapeptides ending D-Ala-D-Ala. Cefoxitin
  induction raises pentapeptide and 4,3-cross-linked material that enters muropeptide recycling.
  No biosynthetic step is measured.
- E. coli DacB (P24228): IMP GO:0000270 (PMID:2046551), IMP GO:0009002 (PMID:331322), ISM
  GO:0004185. Dictyostelium pscA (Q86I79): dictyBase IDA GO:0004185 (PMID:12843630).

## Review decisions

- GO:0000270 IBA: ACCEPT. GO:0004175 IDA: ACCEPT.
- GO:0004185 (IBA, IEA, IDA): MODIFY to GO:0009002 serine-type D-Ala-D-Ala carboxypeptidase.
- GO:0006508 proteolysis IEA: MARK_AS_OVER_ANNOTATED (substrate is peptidoglycan, not protein).
- GO:0009252 IDA: MODIFY to GO:0000270; PSEUDOCAP WRONG_TERM defect, PROBABLE.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000768632 | GO:0000270 peptidoglycan metabolic process | 2 | 20 (18 taxa) | GO:0009252 peptidoglycan biosynthetic process, IDA, PMID:25495032 (PseudoCAP) | OVER-SPECIFIC | Full text: only hydrolytic activities (DD-CPase, 4,3-endopeptidase) are shown, tied to muropeptide recycling; biosynthesis is not shown. PAINT already placed the parent GO:0000270, which the paper supports. PSEUDOCAP WRONG_TERM defect, PROBABLE. | E. coli DacB P24228 (IMP GO:0000270, PMID:2046551) | Yes, on DacB |
| PTN000768632 | GO:0004185 serine-type carboxypeptidase activity | 3 | 20 (18 taxa) | GO:0004185, IDA, PMID:25495032 (PseudoCAP) | SOUND | Full text: purified PBP4 trims the terminal D-Ala of stem pentapeptides; the specific term would be GO:0009002, but the node term is right for the clade. | E. coli DacB P24228 (ISM; IMP GO:0009002); Dictyostelium pscA Q86I79 (IDA GO:0004185, PMID:12843630) | Yes, on pscA IDA (and DacB) |

No GO_CENTRAL defect. Open point: GO:0000270 propagates to Dictyostelium pscA, which has no cell
wall peptidoglycan; recorded as a suggested question rather than a defect, because pscA may act
on ingested bacterial peptidoglycan.
