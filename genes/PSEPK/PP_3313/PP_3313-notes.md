# PP_3313 notes

2026-07-10: First-pass cold/heat-shock stress-bucket curation.
PP_3313 encodes a predicted HSP20-family small heat shock protein in Pseudomonas putida KT2440. It contains an alpha-crystallin/HSP20 domain and an HSP21-like family assignment, supporting a putative heat-responsive holdase chaperone that binds non-native or unfolded proteins.

Primary provenance:
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "DE   SubName: Full=Heat shock protein {ECO:0000313|EMBL:AAN68920.1};"]
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "CC   -!- SIMILARITY: Belongs to the small heat shock protein (HSP20) family."]
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "DR   PANTHER; PTHR46733; 26.5 KDA HEAT SHOCK PROTEIN, MITOCHONDRIAL; 1."]
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "DR   Pfam; PF00011; HSP20; 1."]
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "FT   DOMAIN          12..123"]
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "DR   InterPro; IPR002068; A-crystallin/Hsp20_dom."]
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "DR   InterPro; IPR008978; HSP20-like_chaperone."]
- [file:PSEPK/PP_3313/PP_3313-uniprot.txt "DR   InterPro; IPR044587; HSP21-like."]

Decision: keep the call at the family/domain-supported level. Cold-shock proteins are retained as nucleic-acid-binding CSD proteins without a specific RNA/DNA target; HSP20-family proteins are treated as putative unfolded-protein-binding holdases without assigning specific clients.
