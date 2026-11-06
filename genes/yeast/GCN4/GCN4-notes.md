# GCN4 (YEL009C, P03069) review notes

## Literature search (2026-11-04)

No deep-research provider was available. Sources checked:

- SGD curated description (`GCN4-deep-research-sgd.md`).
- UniProt P03069 curated FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, INDUCTION, DOMAIN, PTM text.
- All 37 GOA-cited publications cached by `just fetch-gene-pmids yeast GCN4` (full text in cache for PMID:12455686, 16402857, 16472744, 22195967, 29628310, 31211995; others abstract-only).
- SGD ids in WITH/FROM resolved through UniProt REST (S000005411 GAL11/MED15; S000005160 RAP1; S000002552 TAF12; S000005786 GCD1; S000003315 GCD2; S000000189 ROX3/MED19; S000000285 SPT7; S000005508 SPT20; S000006175 HFI1/ADA1; S000005335 POP2).
- Context only: integrated stress response module, gcn4 effector realizer (module proposed in ai4curation/ai-gene-review#5904).

## Findings

- bZIP activator binding ATGA(C/G)TCAT as a homodimer [PMID:3678204 "demonstrating that GCN4 binds DNA as a dimer"; PMID:1473154 crystal structure; PMID:3532321; PMID:2204805].
- Activates amino acid and purine biosynthetic genes under starvation [PMID:3907851; PMID:1939099 ADE4; PMID:8336737].
- Activation domains recruit Mediator via Gal11/Med15 (fuzzy complex) and also SAGA, TFIID (Taf12), SWI/SNF [PMID:22195967; PMID:19940160; PMID:20308326; PMID:15121833].
- Represses ribosomal protein genes via direct Rap1 binding [PMID:21183953 "Gcn4p bound directly to Rap1p, which in turn inhibited Esa1p-Rap1p binding"]; negative effects on AQR1 and PHM8 [PMID:15590823; PMID:26979516].
- Nuclear; NLS2 imported by Srp1/Kap95; degraded in nucleus after Pho85 phosphorylation [PMID:12455686; PMID:14648200].
- Gcn4 binds within coding sequences and activates internal promoters [PMID:29628310].
- Positioning domain tethers target loci to the NPC [PMID:31211995].
- Many identical-protein-binding IPI rows come from papers using the GCN4 leucine zipper as a dimerization tool or control (Drosophila ORs, mycobacterial PFC, T2SS pseudopilins, Brucella membrane proteins, C2H, Hsp104/ClpB). Self-association is real, so kept as homodimerization.
