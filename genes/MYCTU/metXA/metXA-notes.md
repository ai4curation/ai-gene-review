# metXA notes (Rv3341, P9WJY9; also called metA / HTA in the literature)

No deep-research file; literature found by Europe PMC search ("Rv3341 OR homoserine transacetylase/acetyltransferase AND tuberculosis", 2026-11-13).

- Acetyl-CoA specific: [PMID:32976971 "LC-MS confirmed that MetA possessed HAT activity, but no homoserine-succinyltransferase (HST) and serine-acetyltransferase (SAT) activities."]
- Ping-pong with acetyl-enzyme intermediate: [PMID:36753622 "Crystallographic and mass spectral observation of the acetylated HTA intermediate and initial velocity studies were consistent with a ping-pong kinetic mechanism."]; proposed substrate inhibition by acetyl-CoA and product inhibition by CoA and O-acetylhomoserine.
- Structures 6PUX (PMID:31889085, full text), 7RYT, 8F2L.
- Deletion abolishes Met/SAM synthesis; rapid killing, cleared in mice [PMID:26221021 "Here we show that deletion of the gene encoding homoserine transacetylase (metA) inactivates methionine and S-adenosylmethionine (SAM) biosynthesis in Mtb"].
- Engineering: L322R switches to succinylation; A59G/G62P gives SAT-like activity [PMID:34090964]. Wild-type is acetyl-specific.
- Hydrolase activity on p-nitrophenyl acetate (PMID:32976971) is artificial-substrate chemistry, not annotated.
- Family: PTHR32268:SF11; NCBIfam NF047917 MetX_acetyl_MTB; HAMAP MF_00296. IBA node PTN000791315 (acetyl) applies correctly.
- UniProt entry is rule-based only (ECO:0000255) and does not cite PMID:32976971 / PMID:36753622.

## Curation decisions (2026-11-13)
- 6 GOA rows: 5 ACCEPT, GO:0016747 MODIFY -> GO:0004414. Core: GO:0004414, L-methionine biosynthetic process, cytoplasm.
