# PP_4331 Notes

## 2026-07-09 PDT / 2026-07-10 UTC

First-pass PSEPK motility-bucket curation. PP_4331 has a machine-named
chemotaxis product description
[file:PSEPK/PP_4331/PP_4331-uniprot.txt "DE   RecName: Full=Chemotaxis protein {ECO:0008006|Google:ProtNLM};"].
Its stronger concrete evidence is DUF2802 plus a predicted transmembrane segment
[file:PSEPK/PP_4331/PP_4331-uniprot.txt "DR   InterPro; IPR021244; DUF2802."]
[file:PSEPK/PP_4331/PP_4331-uniprot.txt "DR   Pfam; PF10975; DUF2802; 1."]
[file:PSEPK/PP_4331/PP_4331-uniprot.txt "FT   TRANSMEM        6..24"].
Asta recovered the same DUF2802 signal
[file:PSEPK/PP_4331/PP_4331-deep-research-asta.md "Key Domains:** DUF2802. (IPR021244); DUF2802 (PF10975)"].

Decision: add only a conservative membrane annotation and place PP_4331 as a
DUF2802 membrane accessory candidate in
`modules/chemotaxis_adaptation_accessory_boundary.yaml`. Do not assert a
chemotaxis process annotation without direct pathway evidence.
