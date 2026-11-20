# metXS notes (PP_5097, Q88CT3)

- MetX-fold (PTHR32268:SF11; HAMAP MF_00296) but succinyl-CoA specific. UniProt FUNCTION "Transfers a succinyl group from succinyl-CoA to L-homoserine" (ECO:0000269|PubMed:28581482) and NCBIfam NF047916 MetX_succinyl.
- Requires MetW for activity (UniProt ACTIVITY REGULATION, ECO:0000269|PubMed:28581482).
- Family-level caution [PMID:28581482 "Members of these families are prone to incorrect annotation because MetX and MetA enzymes are assumed to always use acetyl-CoA and succinyl-CoA, respectively."]. Full text of PMID:28581482 not open access; gene-level data taken from UniProt.

## Curation decisions (2026-11-13)
- GO:0004414 IEA (ARBA00088393 + PANTHER PTN002426741) REMOVE as over-propagation of the MetX acetyl default; source defect recorded (PROBABLE) on the ARBA rule.
- Added NEW GO:0071266 'de novo' L-methionine biosynthetic process (IC, from the EXP activity + pathway step); fixes the core-function BP gap.
- Removed DE (protein name/EC) quotes and the self-GOA reference entry.
- PAINT: metXS gets no IBA from PTN000791315 (acetyl node); only TreeGrafter via PTN002426741.
