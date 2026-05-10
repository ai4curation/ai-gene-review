# atpF notes

- Reviewed UniProt and GOA on 2026-05-10.
- UniProt identifies atpF as chloroplast ATP synthase subunit b / F0 sector subunit b [file:POPTR/atpF/atpF-uniprot.txt "RecName: Full=ATP synthase subunit b, chloroplastic"].
- Function text supports ATP synthase process and complex-level proton transport: F1F0 ATP synthase produces ATP using a proton/sodium gradient and subunit b links F1 to F0 as part of the F0 channel [file:POPTR/atpF/atpF-uniprot.txt "F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient."; file:POPTR/atpF/atpF-uniprot.txt "Component of the F(0) channel, it forms part of the peripheral stalk, linking F(1) to F(0)."].
- Used contributes_to for complex-level MF terms because subunit b is structural/stator-linked rather than an independent ATP synthase enzyme.
- Addressed PR #470 re-review on 2026-05-10: changed the contributes_to MF annotations from ACCEPT to MODIFY because the action changes the source GOA enables qualifier.
