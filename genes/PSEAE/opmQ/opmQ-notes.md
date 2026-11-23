# opmQ (PA2391, Q9I189) review notes

Literature as in genes/PSEAE/pvdR/pvdR-notes.md (same four PvdRT-OpmQ papers;
PMID:19906986 full text read, the others abstract only). OpmQ is the OMF lipoprotein
[PMID:19906986 "Therefore, the entire PvdRT-OpmQ system (i.e., the IM ABC transporter PvdT, the periplasmic fusion protein PvdR, and the OM porin OpmQ) appears to be involved in the transport of PVD from the periplasm to the extracellular milieu."].

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008411811 | GO:0016020 membrane | 3 | 85 (20 taxa) | GO:1990281 efflux pump complex, IDA PMID:19906986/21035449/22187978; IMP PMID:19906986/22187978/23766114 | SOUND | OpmQ is the outer-membrane component of the pump; a membrane protein complex term is valid evidence for membrane. PMID:19906986 IDA code wrong (mutants only) -> PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE. | OprM Q51487 (cell outer membrane EXP PMID:10889211; efflux pump complex IDA), OprJ Q51397 (outer membrane IDA PMID:8878035) | Yes |
| PTN008411811 | GO:0022857 transmembrane transporter activity | 4 | 85 (20 taxa) | GO:0015562 efflux transmembrane transporter activity, same six rows | SOUND | Pump exports PVD; GO:0015562 is_a GO:0022857. Same IDA-code defect. | OprM (GO:0015562 IDA/IMP), OprJ (GO:0022857 IMP/IGI), E. coli CusC P77211 (GO:0005375 IGI) | Yes |

Node terms are generic and suit an OMF clade. No GO_CENTRAL defect. The leaf IBAs on
OpmQ are TOO_GENERAL (membrane, transporter activity) or MODIFY (transmembrane
transport -> GO:0015891 siderophore transport, with propagation_review
NO_FAILURE_CORE).

PvdR (PA2389) shares the operon and the same PseudoCAP rows; it seeds PTN001253051.
The GO:0002049 IMP (PMID:12686626) gets the same MODIFY and PSEUDOCAP WRONG_TERM
defect as on pvdR.
