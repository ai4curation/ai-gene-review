# ANKRD34A notes

- Uncharacterized ANKRD34-family protein; brain-enhanced (HPA). Cytosol IDA (HPA) is ACCEPT, and the current PAINT node PTN001192733 (seeded by ANKRD34A and ANKRD34B, 2026-07-30) asserts cytosol too.
- **Stale pi-body IBA:** GOA's GO:0071546 IBA comes from node PTN001192751, whose only donor is MGI:1921318 = mouse **Asz1/GASZ** (checked in UniProt Q8VD46). Asz1 is a germline piRNA-pathway protein, now in PANTHER family PTHR24157, while ANKRD34A is in PTHR24156. The node is absent from the current PTHR24156 PAINT slice. REMOVE, with root cause SOURCE_STALE_OR_MISSING. Mouse Ankrd34c also still carries a pi-body IBA (QuickGO), probably from the same stale node; ANKRD34C should be checked when it is reviewed.
- Literature: only a HEMK2/N6AMT1 substrate screen [PMID:26797129], the source of UniProt's Gln-15 methylation PTM. PubMed otherwise has one unrelated tilapia transcriptomics hit.
- knowledge_gaps: MF_DARK (location known; activity and process unknown).
