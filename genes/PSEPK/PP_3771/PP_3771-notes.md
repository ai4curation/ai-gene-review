# PP_3771 Notes

## 2026-07-09 PDT / 2026-07-10 UTC

First-pass PSEPK motility-bucket curation. PP_3771 has a machine-named
chemotaxis product description
[file:PSEPK/PP_3771/PP_3771-uniprot.txt "DE   RecName: Full=Chemotaxis protein {ECO:0008006|Google:ProtNLM};"],
but Asta reports no UniProt family or domain assignment
[file:PSEPK/PP_3771/PP_3771-deep-research-asta.md "Protein Family:** Not specified in UniProt"]
[file:PSEPK/PP_3771/PP_3771-deep-research-asta.md "Key Domains:** Not specified in UniProt"].
The one concrete feature is a predicted transmembrane segment
[file:PSEPK/PP_3771/PP_3771-uniprot.txt "FT   TRANSMEM        34..52"].

Decision: add only a conservative membrane annotation and place PP_3771 as a
low-confidence membrane accessory candidate in
`modules/chemotaxis_adaptation_accessory_boundary.yaml`. Do not assert a
chemotaxis process annotation from the product name alone.
