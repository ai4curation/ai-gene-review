# PP_2403 Notes

## 2026-07-09 PDT / 2026-07-10 UTC

First-pass PSEPK motility-bucket curation. PP_2403 entered the bucket with the
UniProt product name `Chemotaxis protein CheY`
[file:PSEPK/PP_2403/PP_2403-uniprot.txt "DE   SubName: Full=Chemotaxis protein CheY {ECO:0000313|EMBL:AAN68015.1};"].
However, both UniProt and Asta show an OmpR/PhoB-type DNA-binding response
regulator architecture, not a compact canonical CheY output protein
[file:PSEPK/PP_2403/PP_2403-uniprot.txt "DR   InterPro; IPR001867; OmpR/PhoB-type_DNA-bd."]
[file:PSEPK/PP_2403/PP_2403-uniprot.txt "DR   Pfam; PF00486; Trans_reg_C; 1."]
[file:PSEPK/PP_2403/PP_2403-deep-research-asta.md "Key Domains:** CheY-like_superfamily. (IPR011006); OmpR/PhoB-type_DNA-bd. (IPR001867); Sig_transdc_resp-reg_C-effctor. (IPR016032); Sig_transdc_resp-reg_receiver. (IPR001789); WalR-like. (IPR039420)"].

Decision: curate PP_2403 as an orphan DNA-binding two-component response
regulator in `modules/orphan_two_component_regulators_boundary.yaml`, not as a
core chemotaxis CheY protein.
