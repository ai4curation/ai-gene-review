# PP_1106 notes

2026-07-10: First-pass repair-helicase/recombination split curation.
PP_1106 is a DNA-ligase-associated metallo-beta-lactamase/Xnuc_lig-associated nuclease candidate near the Lhr-Core locus. Its only fetched GOA row is RNA endonuclease activity from TreeGrafter, but the local metadata support only a broad predicted nuclease context, so no precise core GO function is asserted in this first pass.

Primary provenance:
- [file:PSEPK/PP_1106/PP_1106-uniprot.txt "DE   RecName: Full=DNA ligase-associated DEXH box helicase {ECO:0008006|Google:ProtNLM};"]
- [file:PSEPK/PP_1106/PP_1106-uniprot.txt "DR   PANTHER; PTHR11203:SF49; BLL1145 PROTEIN; 1."]
- [file:PSEPK/PP_1106/PP_1106-uniprot.txt "DR   InterPro; IPR050698; MBL."]
- [file:PSEPK/PP_1106/PP_1106-uniprot.txt "DR   InterPro; IPR036866; RibonucZ/Hydroxyglut_hydro."]
- [file:PSEPK/PP_1106/PP_1106-uniprot.txt "DR   InterPro; IPR026360; Xnuc_lig_assoc."]
- [file:PSEPK/PP_1106/PP_1106-deep-research-asta.md "  uniprot_accession: Q88NU8"]
- [file:PSEPK/PP_1106/PP_1106-deep-research-asta.md "  protein_description: 'RecName: Full=DNA ligase-associated DEXH box helicase {ECO:0008006|Google:ProtNLM};'"]
- [file:PSEPK/PP_1106/PP_1106-deep-research-asta.md "  protein_domains: MBL. (IPR050698); RibonucZ/Hydroxyglut_hydro. (IPR036866); Xnuc_lig_assoc."]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
