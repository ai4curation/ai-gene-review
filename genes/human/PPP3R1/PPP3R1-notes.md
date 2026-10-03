# PPP3R1 notes (calcineurin B type 1, P63098)

Reviewed for the ADAPTIVE_IMMUNITY project (TCR signaling; calcineurin-NFAT branch).

## Biology summary

- CnB is the obligate regulatory subunit of calcineurin [PMID:26794871 "a heterodimer composed of a catalytic subunit A and an essential regulatory subunit B"]; CnA and CnB are unstable alone [PMID:20639889 "CnB is the exclusive and obligate binding partner of the CnA catalytic subunit, and neither protein is appreciably stable without expression of the other"].
- Four EF-hand Ca2+ sites [PMID:23468591 "CN is always composed of a catalytic A subunit (CNA), bound to a regulatory B subunit (CNB) that binds four Ca2+ ions"]. Low-affinity site occupancy drives CnA activation [PMID:11123943 "Ca(2+) binding to the low-affinity sites of calcineurin B affects the conformation of calcineurin B and induces a conformational change of the regulatory domain of calcineurin A"].
- Immunophilin-drug complexes bind the CnA/CnB composite surface [PMID:12218175 "The CyPA-CsA complex binds to a composite surface formed by the catalytic and regulatory subunits of CN"]; LxVP pocket includes CnB residues [PMID:27974827].
- Membrane tethering via myristoylation [PMID:22343722 "tethering of CNB to the cell membrane through its myristoyl modification"].
- No catalytic domain; phosphatase activity belongs to CnA (PPP3CA/PPP3CB/PPP3CC).

## Curation decisions

- Phosphatase activity rows (IEA GO:0004721, NAS GO:0004723): MODIFY to GO:0008597 regulator activity. Core function uses GO:0008597 with contributes_to GO:0033192 (the MF used for PPP3CB's core function).
- Calmodulin binding (NAS): REMOVE; the calmodulin-binding domain is on CnA.
- 25 protein binding rows: CnA partners in structural/biochemical papers (6) MODIFY to GO:0008597; HTP screens, RCAN1, ASK1 (substrate), SPATA33 REMOVE; PMID:19896943 is withdrawn, REMOVE.
- Positive regulation of calcineurin-NFAT cascade (NAS): MODIFY to the cascade itself (calcineurin is the effector, not a regulator).
- Positive regulation of Ca2+ import (NAS, PMID:17640527): REMOVE, the abstract attributes the enhancement to PKA and the suppression to anchored CaN; the negative-regulation row kept as non-core.
- Calcineurin complex rows ACCEPT, consistent with PPP3CA and PPP3CB reviews (both ACCEPT GO:0005955).
- No NEW terms. Comparator: PPP3CA and PPP3CB carry only TAS T cell activation, not GO:0050852 TCR signaling pathway; calcineurin's TCR role is captured by GO:0033173.
- Consistency with PPP3CB (finished): catalytic MF GO:0033192 in GO:0005955; PPP3R1 core function carries contributes_to GO:0033192 and in_complex GO:0005955; Ca2+ binding is PPP3R1's own MF. GO:0030346 (PP2B binding) not used, as self-referential for a calcineurin subunit.
