# ibpA notes

2026-07-10: First-pass cold/heat-shock stress-bucket curation.
ibpA encodes a predicted HSP20-family small heat shock protein in Pseudomonas putida KT2440. It contains an alpha-crystallin/HSP20 domain and is best treated as a putative stress-responsive holdase chaperone that binds non-native or unfolded proteins, while its specific KT2440 clients remain unknown.

Primary provenance:
- [file:PSEPK/ibpA/ibpA-uniprot.txt "DE   SubName: Full=Small heat shock protein IbpA {ECO:0000313|EMBL:AAN67597.1};"]
- [file:PSEPK/ibpA/ibpA-uniprot.txt "CC   -!- SIMILARITY: Belongs to the small heat shock protein (HSP20) family."]
- [file:PSEPK/ibpA/ibpA-uniprot.txt "DR   PANTHER; PTHR47062; -; 1."]
- [file:PSEPK/ibpA/ibpA-uniprot.txt "DR   Pfam; PF00011; HSP20; 1."]
- [file:PSEPK/ibpA/ibpA-uniprot.txt "FT   DOMAIN          32..144"]
- [file:PSEPK/ibpA/ibpA-uniprot.txt "DR   InterPro; IPR002068; A-crystallin/Hsp20_dom."]
- [file:PSEPK/ibpA/ibpA-uniprot.txt "DR   InterPro; IPR037913; ACD_IbpA/B."]
- [file:PSEPK/ibpA/ibpA-uniprot.txt "DR   InterPro; IPR008978; HSP20-like_chaperone."]

Decision: keep the call at the family/domain-supported level. Cold-shock proteins are retained as nucleic-acid-binding CSD proteins without a specific RNA/DNA target; HSP20-family proteins are treated as putative unfolded-protein-binding holdases without assigning specific clients.
