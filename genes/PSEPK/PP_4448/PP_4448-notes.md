# PP_4448 notes

2026-07-10: First-pass repair-helicase/recombination split curation.
PP_4448 is a HerA-like central-domain protein with P-loop NTPase domain evidence but no GOA rows. The first pass records it as a boundary candidate without asserting helicase or DNA-repair GO terms from the domain name alone.

Primary provenance:
- [file:PSEPK/PP_4448/PP_4448-uniprot.txt "DE   RecName: Full=Helicase HerA central domain-containing protein {ECO:0000259|Pfam:PF01935};"]
- [file:PSEPK/PP_4448/PP_4448-uniprot.txt "DR   PANTHER; PTHR42957; HELICASE MJ1565-RELATED; 1."]
- [file:PSEPK/PP_4448/PP_4448-uniprot.txt "DR   Pfam; PF01935; DUF87; 1."]
- [file:PSEPK/PP_4448/PP_4448-uniprot.txt "FT   DOMAIN          121..414"]
- [file:PSEPK/PP_4448/PP_4448-uniprot.txt "DR   InterPro; IPR008571; HerA-like."]
- [file:PSEPK/PP_4448/PP_4448-uniprot.txt "DR   InterPro; IPR002789; HerA_central."]
- [file:PSEPK/PP_4448/PP_4448-uniprot.txt "DR   InterPro; IPR027417; P-loop_NTPase."]
- [file:PSEPK/PP_4448/PP_4448-deep-research-asta.md "  uniprot_accession: Q88EL4"]
- [file:PSEPK/PP_4448/PP_4448-deep-research-asta.md "  protein_description: 'RecName: Full=Helicase HerA central domain-containing protein"]
- [file:PSEPK/PP_4448/PP_4448-deep-research-asta.md "  protein_domains: HerA-like. (IPR008571); HerA_central. (IPR002789); P-loop_NTPase."]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
