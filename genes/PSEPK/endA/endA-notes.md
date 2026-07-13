# endA notes

2026-07-10: First-pass nuclease/DNase/toxin side-node split curation.
endA encodes an EndA/NucM-family endonuclease I candidate with signal-peptide context. The fetched GOA block contains only broad nuclease activity, so a UniProt-backed endonuclease row is added.

Primary provenance:
- [file:PSEPK/endA/endA-uniprot.txt "DE   SubName: Full=Endonuclease I {ECO:0000313|EMBL:AAN68979.1};"]
- [file:PSEPK/endA/endA-uniprot.txt "DR   GO; GO:0004519; F:endonuclease activity; IEA:UniProtKB-KW."]
- [file:PSEPK/endA/endA-uniprot.txt "DR   PANTHER; PTHR33607; ENDONUCLEASE-1; 1."]
- [file:PSEPK/endA/endA-uniprot.txt "DR   Pfam; PF04231; Endonuclease_1; 1."]
- [file:PSEPK/endA/endA-uniprot.txt "KW   Endonuclease {ECO:0000313|EMBL:AAN68979.1};"]
- [file:PSEPK/endA/endA-uniprot.txt "DR   InterPro; IPR035451; Ada-like_dom_sf."]
- [file:PSEPK/endA/endA-uniprot.txt "DR   InterPro; IPR007346; Endonuclease-I."]
- [file:PSEPK/endA/endA-uniprot.txt "DR   InterPro; IPR044925; His-Me_finger_sf."]
- [file:PSEPK/endA/endA-deep-research-asta.md "  uniprot_accession: Q88HI2"]
- [file:PSEPK/endA/endA-deep-research-asta.md "  protein_description: 'SubName: Full=Endonuclease I {ECO:0000313|EMBL:AAN68979.1};'"]

Decision: route as nuclease/toxin/RNA side-node context rather than as a single DNA repair pathway.
