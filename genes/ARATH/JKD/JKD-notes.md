# JKD (JACKDAW / IDD10, At5g03150, UniProtKB:Q700D2) — curation notes

## Session 2026-10-05 (root radial patterning module: SHR–SCR–BIRD–CYCD6;1)

Deep research (`just deep-research-falcon ARATH JKD`) failed (HTTP 402 from provider); notes are from cached publications.

- BIRD/IDD C2H2 zinc-finger TF. Feed-forward loop with SHR: [PMID:17785527 "JACKDAW and MAGPIE genes, which encode members of a plant-specific family of zinc finger proteins, act in a SHR-dependent feed-forward loop to regulate the range of action of SHORT-ROOT and SCARECROW"]. JKD expression is SHR-independent: [PMID:17785527 "JACKDAW expression is initiated independent of SHORT-ROOT and regulates the SCARECROW expression domain outside the stele"].
- Structural mechanism: [PMID:28211915 "SHR-SCR function as transcription cofactors by binding to the third and fourth ZFs, (ZF3-ZF4) of JKD"]; [PMID:28211915 "the ZF1-ZF2-ZF3 of JKD in the JKD-SHR-SCR complex is involved in DNA binding"]; JKD and MGP compete: [PMID:28211915 "suggesting that the binding of JKD and MGP is exclusive"].
- Transcriptional activation of SCR/MGP: [PMID:21935722 "Transient expression of LUC reporter genes with the proximal sequences upstream from the ATG codon of SCR and MGP in protoplasts were activated by JKD"]; IDD sites in SCR promoter essential [PMID:28324206 "mutation of the -340 bp sequence eliminated most of the promoter activity, indicating that this sequence was indispensable for SCR expression"].
- SHR nuclear retention and formative divisions: [PMID:26494755 "JKD and BALD-IBIS regulate SHR movement by promoting its nuclear retention, and cooperatively with MAGPIE (MGP) and NUTCRACKER (NUC) are required for the formative divisions that pattern the ground tissue into cortex and endodermis"]; [PMID:25829440 "constraining SHORT-ROOT spread through nuclear retention and transcriptional regulation of key downstream SHORT-ROOT targets, including SCARECROW and CYCLIND6"].
- In vivo higher-order complexes (SHR, SCR, JKD): [PMID:28746306 "three fully functional fluorescently tagged cell fate regulators establish cell-type-specific interactions at endogenous expression levels and can form higher order complexes"].
- Epidermal patterning (secondary, non-cell-autonomous from cortex): [PMID:20356954 "Tissue-specific induction experiments indicate non-cell-autonomous action of JKD from the underlying cortex cell layer to specify epidermal cell fate"].
- GA/DELLA: [PMID:24821766 "These results suggest that the coregulators DELLA and SCL3, using IDDs as transcriptional scaffolds for DNA binding, antagonistically regulate the expression of their downstream targets to control the GA signaling pathway"]; [PMID:24821766 "lack of AtIDD10 causes a defect in DELLA-mediated feedback, thus resulting in increased cell division"].

### Curation decisions
- All protein-binding IPIs with SHR/SCR/DELLA/SCL3 -> MODIFY to GO:0001221 transcription coregulator binding (these partners are GRAS coregulators that use IDDs as DNA-binding scaffolds); JKD–MGP -> GO:0140297.
- DNA binding (IDA) -> MODIFY to GO:0000976 transcription cis-regulatory region binding.
- NEW GO:0090057 root radial pattern formation (JKD does molecular work in the SHR-SCR-JKD complex).
- Broad root development / meristem growth / regulation of cell division kept as non-core.
- PANTHER: UniProt places IDDs in PTHR10593 whose family name is "SERINE/THREONINE-PROTEIN KINASE RIO" (dominated name); not used in the module.
