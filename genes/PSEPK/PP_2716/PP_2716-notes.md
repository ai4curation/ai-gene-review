# PP_2716 notes

2026-07-10: First-pass arsenic/copper metal-resistance stress-bucket curation.
PP_2716 encodes a predicted low-molecular-weight arsenate reductase in Pseudomonas putida KT2440. UniProt names the product as arsenate reductase and marks arsenical-resistance context, but the fetched GOA table has no rows. The first-pass GO-level assignment is therefore conservative oxidoreductase activity plus response to arsenic-containing substance, without asserting a more specific arsenate reductase GO term.

Primary provenance:
- [file:PSEPK/PP_2716/PP_2716-uniprot.txt "DE   SubName: Full=Arsenate reductase {ECO:0000313|EMBL:AAN68324.1};"]
- [file:PSEPK/PP_2716/PP_2716-uniprot.txt "DR   InterPro; IPR023485; Ptyr_pPase."]
- [file:PSEPK/PP_2716/PP_2716-uniprot.txt "DR   Pfam; PF01451; LMWPc; 1."]
- [file:PSEPK/PP_2716/PP_2716-deep-research-asta.md "  protein_description: 'SubName: Full=Arsenate reductase {ECO:0000313|EMBL:AAN68324.1};'"]
- [file:PSEPK/PP_2716/PP_2716-deep-research-asta.md "  protein_family: Not specified in UniProt"]
- [file:PSEPK/PP_2716/PP_2716-deep-research-asta.md "  protein_domains: Ptyr_pPase. (IPR023485); Ptyr_pPase_sf. (IPR036196); LMWPc (PF01451)"]

Decision: keep the assignment conservative. ArsH proteins are curated to FMN reductase activity; arsenate reductase candidates get broad oxidoreductase plus arsenic-response context because the fetched GOA has no exact MF rows; CopAB proteins are represented as copper-binding/homeostasis or broad oxidoreductase cell-envelope copper-resistance proteins.
