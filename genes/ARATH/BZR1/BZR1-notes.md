# BZR1 (BRASSINAZOLE-RESISTANT 1; Q8S307; AT1G75080) — curation notes

## Identity / family
- Master transcription factor of the brassinosteroid (BR) signaling pathway; member of the plant-specific BZR/BES1 (BZR/LAT61) family, an atypical bHLH-like family that binds DNA via a non-canonical N-terminal domain.
- UniProt: "Belongs to the BZR/LAT61 family." Pfam PF05687 BES1_N; InterPro IPR008540 (BES1_N), IPR033264 (BZR). 336 aa, nuclear.

## Core molecular function — sequence-specific DNA-binding TF / repressor
- BZR1 is a transcriptional repressor that binds the BR-response element (BRRE) 5'-CGTG(T/C)G-3' in promoters of feedback-regulated BR biosynthetic genes [PMID:15681342 "BZR1 is a transcriptional repressor that has a previously unknown DNA binding domain and binds directly to the promoters of feedback-regulated BR biosynthetic genes"].
- UniProt FUNCTION: "Transcriptional repressor that binds to the brassinosteroid (BR) response element (BRRE) 5'-CGTG(T/C)G-3' in gene promoter."
- DNA-binding region maps to residues 21–104 (UniProt REGION "Required for DNA-binding"); crystal structure (PDB 5ZD4, residues 21–104) in complex with DNA, homodimerizing [PMID:30287951 X-ray structure of BIL1/BZR1 21-104 in complex with DNA, and homodimerization — from UniProt RN[15]].
- Genome-wide ChIP-chip: 953 BR-regulated BZR1 target (BRBT) genes; BZR1 acts as BOTH activator (~450 genes) and repressor (~462 genes) depending on promoter; binds BRRE (repressed targets) and E-box/G-box (CACGTG) [PMID:21074725 "There are 450 BRBT genes activated, 462 repressed, and 41 affected in complex ways by BR, indicating BZR1 can be activator and repressor for different genes"; "BZR1 binds to the BR-response element (BRRE, CGTGT/CG) of BR-repressed genes"].
- DNA-binding transcription factor activity demonstrated directly (IDA) [PMID:21074725].
- cis-regulatory region sequence-specific DNA binding: BZR1 directly activates the NSN1 promoter during ovule germline specification [PMID:36748257 "BZR1 coordinates female germline specification by directly activating the expression of a nucleolar GTP-binding protein, NUCLEOSTEMIN-LIKE 1 (NSN1)"].

## Process — BR signaling pathway (core)
- BZR1 is the key nuclear effector of BR signaling; bzr1-1D dominant mutation suppresses bri1 and bin2 phenotypes; positive regulator of BR-induced growth and feedback suppression of BR biosynthesis [PMID:11970900 "BZR1 is a positive regulator of the BR signaling pathway that mediates both downstream BR responses and feedback regulation of BR biosynthesis"].
- Dual roles: coordinates BR homeostasis (feedback repression of biosynthetic genes CPD, DWF4, BRI1) and downstream growth responses [PMID:15681342 "BZR1 coordinates BR homeostasis and signaling by playing dual roles in regulating BR biosynthesis and downstream growth responses"].

## Regulation / localization (PTM-driven)
- BIN2 (GSK3-like kinase) phosphorylates BZR1 → nuclear export, cytoplasmic retention, degradation; BR-activated phosphatase (PP2A; BSU1) dephosphorylates → nuclear accumulation/activation [PMID:17873094 "GSK3-like kinases induce the nuclear export of BZR1 by modulating BZR1 interaction with the 14-3-3 proteins. BR-activated phosphatase mediates rapid nuclear localization of BZR1"].
- Nucleocytoplasmic shuttling: BZR1 found in BOTH nucleus and cytosol; cytosol localization is real (IDA) but reflects the inactive/exported phosphorylated pool [PMID:17873094 "BZR1 functions as a nucleocytoplasmic shuttling protein"]. Nucleus is the functional compartment.
- PP2A B' regulatory subunits (B'alpha/beta/eta/theta) dephosphorylate BZR1 to activate it [PMID:21258370].
- 14-3-3 proteins (GRF6 etc.) bind phospho-BZR1 and mediate cytoplasmic retention [PMID:17681130 14-3-3 in BR signal transduction].

## Protein interactions (the GO:0005515 IPI annotations)
All of these are generic "protein binding" (GO:0005515) IPI annotations from IntAct/TAIR. They are real interactions but uninformative as MF terms; the informative functions are captured by DNA binding / repressor activity / TF binding / dimerization:
- PMID:17681130 — 14-3-3 (GRF6/P48349) and ASK7/Q39011. Regulatory (14-3-3 sequestration).
- PMID:22307275 — BIN2/ASK7 (Q39011); BR regulates stomatal development via GSK3-mediated MAPK inhibition. Kinase-substrate.
- PMID:22820377 — DELLAs RGL1 (Q9C8Y3), GAI (Q9LQT8), RGA (Q9SLH3); BR/GA/phytochrome common transcription module. BZR1 interacts with DELLA proteins (GA signaling).
- PMID:22820378 — PIF1 (Q8GZM7), PIF4 (Q8W2F3); BZR1-PIF4 integrate BR and environmental signals, bind ~2000 common targets, synergistic [PMID:22820378 "BZR1 and PIF4 interact ... bind to nearly 2,000 common target genes, and synergistically regulate many of these target genes"]. → DNA-binding TF binding.
- PMID:28650476 — CrY2H-seq interactome: RGL1, TCP15 (Q9C9L2), TCP21 (Q9FTA2), GAI, TCP13 (Q9S7W5). High-throughput.
- PMID:32612234 — phytohormone protein network (large-scale Y2H): BEL1, At3g51180, TCP15, At5g47790, ANAC094, HHO3, TCP21, MYB21, GAI, MGH6.1, TCP16, TCP3, TCP13, RGA. Many TFs.
- PMID:37335918 — BLISTER (BLI, AT3G23980) interacts with BIN2 and BZR1; BLI cooperates with BZR1 to activate BR-responsive genes in skotomorphogenesis.
- PMID:21258370 — PP2A B' subunits (O04375, O04376, Q9LU89, Q8LF36). Phosphatase-substrate.
- PMID:25663622 — BSS1/BOP1 (AT3G57130) complex; BSS1 sequesters BZR1.

Note: Many partners are DNA-binding TFs (PIF1/PIF4, TCP3/13/15/16/21, MYB21, DELLAs are not classic DNA binders but PIFs/TCPs/MYB are) → supports GO:0140297 DNA-binding transcription factor binding as a NEW informative MF.

## Biological processes (downstream / developmental — generally non-core developmental outputs of the BR pathway)
- Ovule/seed development: BZR1 regulates HLL, ANT, AP2; dephospho-BZR1 level correlates with ovule/seed number [PMID:22914576 "BR regulates the expression level of genes related to ovule development, including HLL, ANT, and AP2 ... by ... BZR1"].
- Female germline (MMC) specification via NSN1 [PMID:36748257].
- Response to light / photomorphogenesis & response to water deprivation: BR/BZR1 decision-making in seedlings; note PMID:36508461 is primarily about BIN2 alleles, BZR1 acts within the BR pathway downstream [PMID:36508461 abstract — BIN2 alleles as "decision mutants"; light + water withdrawal screen].

## Deep research synthesis (Falcon / Edison Scientific, 2026-06-06)

The Falcon deep research report (`file:ARATH/BZR1/BZR1-deep-research-falcon.md`) corroborates and extends the existing review. Key points used as `supported_by` evidence:
- Core MF/activator-repressor role: "It binds BRRE/E-box-associated promoters and can activate or repress BR-responsive genes controlling growth and BR homeostasis" — supports GO:0003700 and the regulation-of-transcription terms.
- BR signaling pathway role: BZR1 "acts as a principal nuclear effector of the BR receptor-initiated signaling cascade" — supports GO:0009742.
- Localization switch: "phosphorylated forms are biased toward cytoplasmic sequestration, while dephosphorylated forms accumulate in the nucleus and drive transcriptional outputs"; and "BIN2-phosphorylated BZR1 is retained more in the cytoplasm through 14-3-3 association, whereas dephosphorylated BZR1 accumulates in the nucleus to regulate transcription" — supports nucleus (core) and cytosol (non-core, inactive exported pool).
- Signal integration: reviews "emphasize BZR1 as an integration node for light, auxin, GA, ethylene, and stress signaling" — supports GO:0140297 (DNA-binding TF binding) NEW term.

New mechanistic detail not previously captured (recorded here, not added as GO annotations because no new verifiable GO ID is warranted):
- 14-3-3 recognition is structurally defined: minimal phosphomotif at BZR1 residues 169–175 (RISNpSAP) centered on pSer173, binding 14-3-3κ with KD ~0.5 µM, 2:2 stoichiometry, complex lifetime ~1 s (Obergfell et al. 2024, Plant & Cell Physiology; doi:10.1093/pcp/pcae112-era / bioRxiv 2023.10.13.562204).
- Auxin promotes BZR1 nuclear accumulation via MPK3/MPK6-dependent phosphorylation/destabilization of GRF4 (a 14-3-3) at S248 (Yu et al. 2023, Science Advances, doi:10.1126/sciadv.ade2493).
- BIN2 proximity network (TurboID + phosphoproteomics): 482 BIN2-proximal proteins, BZR1 recovered as a canonical BIN2 substrate (Kim et al. 2023, Plant Cell, doi:10.1093/plcell/koad013).
- BZR1 family is redundant and indispensable for BR signaling (Chen et al. 2019, Mol Plant).

No UNDECIDED annotations existed; none required resolution. No new GO annotation was added from the deep research because the new mechanistic findings (14-3-3 KD, auxin/MPK crosstalk, BIN2 network) concern upstream regulation rather than a new verifiable BZR1 GO molecular function/process/component not already represented.

## Curation reasoning summary
- MF: keep DNA-binding TF activity (GO:0003700, IDA + IEA); refine DNA binding (GO:0003677) → sequence-specific repressor / cis-regulatory binding; the existing GO:0000987 (cis-regulatory region SS DNA binding) is well-supported. Add repressor activity (GO:0001227) as NEW, and homodimerization (GO:0042803) from the crystal structure, and DNA-binding TF binding (GO:0140297) for the PIF/TCP partners.
- Remove all generic GO:0005515 "protein binding".
- CC: nucleus = core (IDA); cytosol = real but reflects exported inactive pool (keep non-core).
- BP: BR signaling = core; negative regulation of transcription = core; developmental outputs (ovule, seed, germline, light, water deprivation) = keep as non-core.
