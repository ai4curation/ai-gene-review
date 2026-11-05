# migA (PA0705, Q9I5M1) notes

## Literature (own research, 2026-11-05)

- [PMID:18178733 "These results provide evidence that WapR is the alpha-1,3-rhamnosyltransferase, while MigA is the alpha-1,6-rhamnosyltransferase."]; [PMID:18178733 "In contrast, uncapped core OS from the migA mutant lacked alpha-1,6-L-Rha."] (NMR, MS); loss of the 5C101 outer-core epitope; MigA overexpression raises the uncapped proportion.
- [PMID:22685285 "wapR is negatively regulated, while migA is positively regulated by RhlR/RhlI quorum sensing."]
- Downstream phenotypes of core truncation: motility and attachment (PMID:19589832), biofilm mechanics (PMID:19717596).
- All cached papers are abstract-only; full text (PMC2258888 etc.) could not be retrieved this session. The abstract of PMID:18178733 describes no in vitro transferase assay (title says "putative"), so the IDA code on the glycosyltransferase row looks generous; noted, no defect filed.
- GO:0016757 refined to GO:0016758 hexosyltransferase activity (rhamnosyltransferases sit under it in GO; no LPS-core rhamnosyltransferase term).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000531320 | GO:0016757 glycosyltransferase activity | 7 | 44 (17 taxa) | GO:0016757, IDA, PMID:18178733 | SOUND | Specific loss of alpha-1,6-L-Rha in the mutant supports MigA as the transferase (evidence is mutant structure rather than an enzyme assay). | Salmonella RfbV P26401 (GO:0047600 IDA), E. coli WcaA P77414 (GO:0015020 IDA), Mtb Rv2957 P9WMX7 (GO:0016758 IDA), B. subtilis SunS O31986 (GO:0008194 IDA), P. aeruginosa PA1014 Q9I4V9 (GO:0008919 IDA), WapR | Yes |
| PTN000531351 | GO:0009244 lipopolysaccharide core region biosynthetic process | 2 | 18 (10 taxa) | GO:0009244, IMP, PMID:18178733 | SOUND | Mutant LPS structure (NMR/MS) lacks the sugar MigA adds. | WapR Q9HUG5 only (PseudoCAP IMP/IDA) | Yes, on WapR alone; but the node term does not suit the clade (see below) |

Node-level GO_CENTRAL defect for PTN000531351 is recorded once, on genes/PSEAE/wapR (WapR IBA row): the clade's leaves include Salmonella RfbV (O-antigen abequosyltransferase) and E. coli WcaA (colanic acid), whose experimental annotations contradict an LPS-core term. Not repeated here.

PseudoCAP defect: GO:0015920 lipopolysaccharide transport (IDA, PMID:19589832) WRONG_TERM, PROBABLE.

## Action counts

ACCEPT 2, MODIFY 2, MARK_AS_OVER_ANNOTATED 1, REMOVE 1.
