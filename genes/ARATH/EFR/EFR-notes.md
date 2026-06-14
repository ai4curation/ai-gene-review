# EFR (EF-TU RECEPTOR) — Arabidopsis thaliana, UniProt C0LGT6, At5g20480

Research journal for the GO annotation review. Provenance is inline as
[PMID:xxxx "verbatim quote"] or from the UniProt record (C0LGT6).

## Summary of biology

EFR is a plasma-membrane-localized leucine-rich repeat receptor-like
serine/threonine kinase (LRR-RLK) that is the pattern-recognition receptor (PRR)
for the bacterial pathogen-associated molecular pattern (PAMP) elongation factor
Tu (EF-Tu), specifically perceiving its N-terminal epitope elf18. Ligand
perception triggers PAMP-triggered immunity (PTI). EFR is a single-pass type I
membrane protein: extracellular LRR ectodomain (residues 25–653, 21 LRRs),
transmembrane helix (654–674), cytoplasmic kinase domain (712–1001)
(UniProt C0LGT6 FT lines).

### Identity / discovery
- [PMID:16713565 "we used this finding in a targeted reverse-genetic approach to identify a receptor kinase essential for EF-Tu perception, which we called EFR"]
- [PMID:16713565 "Nicotiana benthamiana, a plant unable to perceive EF-Tu, acquires EF-Tu binding sites and responsiveness upon transient expression of EFR"] — gain-of-function shows EFR is sufficient for elf18 perception/responsiveness.
- [PMID:16713565 "These results demonstrate that EFR is the EF-Tu receptor and that plant defense responses induced by PAMPs such as EF-Tu reduce transformation by Agrobacterium"]
- Disruption phenotype: efr mutants → enhanced susceptibility to Agrobacterium (R. radiobacter) [PMID:16713565 "Arabidopsis efr mutants show enhanced susceptibility to the bacterium Agrobacterium tumefaciens, as revealed by a higher efficiency of T-DNA transformation"].

### Catalytic / kinase activity
- UniProt: EC 2.7.11.1; serine/threonine protein kinase. CATALYTIC ACTIVITY records cite PubMed:18158241 and PubMed:29649442.
- Autophosphorylation upon elicitation [UniProt PTM: "Autophosphorylated after elicitation with elfl18"].
- EFR directly phosphorylates the RLCK BIK1 [PMID:29649442 "EFR regulates the phytohormone jasmonic acid (JA) through direct phosphorylation of a receptor-like cytoplasmic kinase, BIK1"].
- Active-site/catalytic D849; D849N abolishes kinase activity [UniProt MUTAGEN 849 "D->N: Loss of kinase activity"].
- Tyrosine phosphorylation: EFR is activated by phosphorylation on tyrosines; Y836 is required [PMID:24625928 "is activated upon ligand binding by phosphorylation on its tyrosine residues. Phosphorylation of a single tyrosine residue, Y836, is required for activation of EFR and downstream immunity"]. Y836F: "Loss of elf18-triggered immunity, but no effect on the kinase activity" [UniProt MUTAGEN 836].

### Receptor / transmembrane signaling
- Type I single-pass membrane protein; combines elf18 ligand binding (ectodomain) with intracellular kinase signaling — fits GO:0019199 transmembrane receptor protein kinase activity (def: "Combining with a signal and transmitting the signal from one side of the membrane to the other to initiate a change in cell activity by catalysis of the reaction: a protein + ATP = a phosphoprotein + ADP").
- Last two LRRs (561–597) necessary for elf18 binding [UniProt DOMAIN "The last two LRR (561-597) are necessary for elf18 binding and functionality"].
- Co-receptor: ligand-induced complex with SERK3/BAK1 (and SERK4/BKK1, SERK1, SERK2) [UniProt SUBUNIT "Interacts with SERK3/BAK1, SERK4/BKK1, SERK1 and SERK2 in a specific ligand-induced manner"]. BAK1 required for early elf18 signaling [PMID:20113440 "electrical signaling in response to either flg22 or elf 18 critically depends on the activity of the FLS2-associated receptor-like kinase BAK1"].

### Downstream signaling / PTI outputs
- elf18 (via EFR) and flg22 (via FLS2) "activate a common set of signaling events and defense responses" [PMID:16713565].
- Early signaling: Ca2+-associated plasma-membrane anion channel opening / depolarization [PMID:20113440 "activation of FLS2 and EFR lead to BAK1-dependent, calcium-associated plasma membrane anion channel opening as an initial step in the pathogen defense pathway"]. This is the IMP support for GO:0140426 (PAMP receptor signaling pathway).
- ROS burst, phosphorylation, gene expression, callose [PMID:23395902 "Perception of flg22, elf18 or chitin induces a series of early immune responses, including a rapid burst of reactive oxygen species (ROS), phosphorylation events, gene expression, as well as late responses such as callose deposition"].
- Hormone branch: EFR–BIK1 axis regulates JA/SA; PRR–BIK1–WRKY [PMID:29649442 "the mechanistic basis of signal transduction from PRR to phytohormones, mediated through a PRR-BIK1-WRKY axis"].

### Subcellular location & ER quality control
- Cell membrane (plasma membrane); endomembrane system (single-pass type I) [UniProt SUBCELLULAR LOCATION]. ISM:TAIR plasma membrane (GO_REF:0000122 AtSubP), IEA UniProtKB-SubCell.
- ER quality control needed for biogenesis/maturation: STT3a-OST, CRT3 (calreticulin-3), UGGT, ERdj3B/ERD2B; N-glycosylation [PMID:19763087 "EFR accumulation and signalling ... are impaired in psl1, psl2, and stt3a plants. PSL1 and PSL2, respectively, encode calreticulin3 (CRT3) and UDP-glucose:glycoprotein glycosyltransferase that act in concert with STT3A-containing oligosaccharyltransferase complex in an N-glycosylation pathway in the endoplasmic reticulum"]. UniProt: "Specific endoplasmic reticulum quality control components (ERD2B, CRT3, UGGT and STT3A) are required for the biogenesis of EFR."
- PMID:19763087 also annotated by TAIR for immune response-regulating signaling pathway (IMP) and plant-type hypersensitive response (IMP); it is fundamentally an EFR-function + subcellular-location paper (UniProt FUNCTION, SUBCELLULAR LOCATION). It does NOT report an EFR-driven hypersensitive response per se — see below.

### Protein interactions (GO:0005515 IPI entries)
- PMID:18158241 → AvrPto1 (Q87Y16): bacterial effector that binds and inhibits EFR (and FLS2) kinase [PMID:18158241 "AvrPto binds receptor kinases, including Arabidopsis FLS2 and EFR ... to block plant immune responses"]. Also the source for catalytic activity (autophosphorylation).
- PMID:24625928 → BAK1 (Q94F62) and HopAO1/hopD2 (Q79LY0): EFR–co-receptor and EFR–effector phosphatase interactions.
- PMID:23395902 → GRP7/RBG7 (Q03250): GRP7 associates with EFR (and FLS2) at the PM and binds EFR mRNA; HopU1 blocks GRP7–mRNA interaction. [PMID:23395902 "GRP7 directly interacts in vivo with the PRRs FLS2 and EFR in a specific manner"]. This is a regulatory RNA-binding-protein co-association, not core receptor function.
- PMID:27317676 → IOS1 (Q9C8I6): malectin-like LRR-RLK that complexes with EFR/FLS2/CERK1 and primes PTI [PMID:27317676 "analyses supported the existence of complexes between the membrane-localized IOS1 and ... PRRs FLS2 and EFR"].
- PMID:29320478 → high-throughput extracellular LRR-RK interaction network (Nature 2018); reports many ectodomain interactions (SERK5/Q8LPS5, At4g30520/Q8VYT3, BAK1/Q94F62, NIK1/Q9LFS4, LRR-RLK/Q9ZVD4). Large-scale binary IPI screen.
- PMID:29649442 → BIK1 (O48814): EFR binds BIK1 in absence of ligand, dissociates upon PAMP, and phosphorylates it.

## GO annotation review decisions (rationale)

Molecular function:
- GO:0019199 transmembrane receptor protein kinase activity (TAS, PMID:19763087): ACCEPT, CORE. Most informative MF term — captures both receptor (ligand→transmembrane signal) and Ser/Thr kinase nature. Definition matches EFR exactly.
- GO:0106310 protein serine kinase activity (EXP PMID:18158241, EXP PMID:29649442): ACCEPT, CORE. Backed by experimental autophosphorylation + BIK1 phosphorylation; EC 2.7.11.1.
- GO:0004674 protein serine/threonine kinase activity (IEA EC): ACCEPT (core kinase activity; consistent with EC mapping).
- GO:0004672 protein kinase activity (IEA): KEEP_AS_NON_CORE — correct but a generic parent of the more specific Ser/Thr term; redundant.
- GO:0005524 ATP binding (IEA InterPro): ACCEPT — kinase requires ATP (BINDING 718-726, 741); supportive MF.
- GO:0005515 protein binding (IPI, ×8 across 6 papers): all real interactions, but uninformative bare term. MARK_AS_OVER_ANNOTATED per curation guidance (avoid endorsing bare protein binding as core); the biologically meaningful relationship (co-receptor binding, substrate, effector targeting) belongs in more specific MF/process terms.

Cellular component:
- GO:0005886 plasma membrane (IEA UniProtKB-SubCell; and ISM:TAIR): ACCEPT, CORE — EFR is a PM PRR.
- GO:0012505 endomembrane system (IEA UniProtKB-SubCell): KEEP_AS_NON_CORE — reflects ER transit/biogenesis and broad CC; true but less informative than plasma membrane.

Biological process:
- GO:0140426 PAMP receptor signaling pathway (IMP PMID:20113440): ACCEPT, CORE — the defining process.
- GO:0002237 response to molecule of bacterial origin (IMP PMID:29649442): ACCEPT (core; elf18/EF-Tu response).
- GO:0016045 detection of bacterium (IDA PMID:16713565): ACCEPT, CORE — EFR detects bacterial EF-Tu; gain-of-function and loss-of-function support.
- GO:0009617 response to bacterium (IEA ARBA): KEEP_AS_NON_CORE — correct but a broad parent of the IMP/IDA terms.
- GO:0031349 positive regulation of defense response (IEA ARBA): ACCEPT — EFR positively regulates defense (PTI activation; positive regulator).
- GO:0002764 immune response-regulating signaling pathway (IMP PMID:19763087): ACCEPT — EFR signaling regulates immune responses; supported by EFR functional studies.
- GO:0009626 plant-type hypersensitive response (IMP PMID:19763087): UNDECIDED → leaning MARK_AS_OVER_ANNOTATED. PMID:19763087 is about ER quality control of EFR and elf18-triggered (PTI) responses/anthocyanin de-repression, not a classic EFR-dependent HR (programmed cell death). PTI by surface PRRs like EFR generally does NOT trigger HR/cell death (that is the hallmark of ETI/intracellular NLRs). The abstract does not mention hypersensitive response. Cached full text is available but the abstract foregrounds N-glycosylation QC, anthocyanin, and SA-dependent (EFR-independent) defense. Mark as over-annotated: HR is not a core EFR output; the IMP TAIR annotation likely over-propagates "defense" to HR. Not REMOVE because it is an experimental TAIR annotation whose full reasoning I cannot fully verify (use MARK_AS_OVER_ANNOTATED rather than REMOVE).

IBA terms present in UniProt DR block but NOT in GOA stub (not part of existing_annotations to review): GO:0038023 signaling receptor activity (IBA), GO:0009755 hormone-mediated signaling pathway (IBA). Noted for completeness; GO:0009755 (hormone-mediated signaling) is a questionable IBA propagation for a PRR — EFR regulates hormone levels downstream (via BIK1) but is not itself a hormone-signaling receptor.

## Core functions (for synthesis)
1. elf18/EF-Tu pattern recognition receptor — transmembrane receptor Ser/Thr kinase (GO:0019199) at the plasma membrane (GO:0005886) that detects bacterial EF-Tu (GO:0016045).
2. Ligand-activated protein serine/threonine kinase (GO:0106310) that autophosphorylates and phosphorylates BIK1.
3. Initiation of PAMP-triggered immune signaling (GO:0140426) leading to PTI defense outputs.
