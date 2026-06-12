# SRP9 (P49458) review notes

## Identity and overview
SRP9 is the 9 kDa subunit of the signal recognition particle (SRP). It is an 86-aa
protein (initiator Met removed; chain 2-86) belonging to the SRP9 family.

[file:human/SRP9/SRP9-uniprot.txt "Signal recognition particle 9 kDa protein"]

## Core function: Alu domain / elongation arrest
SRP9 together with SRP14 and the Alu portion of the SRP RNA constitutes the
elongation-arrest domain of SRP. SRP9 binds RNA as a heterodimer with SRP14.

[file:human/SRP9/SRP9-uniprot.txt "SRP9 together with SRP14 and the Alu portion of the\nCC       SRP RNA, constitutes the elongation arrest domain of SRP"]
[file:human/SRP9/SRP9-uniprot.txt "Heterodimer with SRP14; binds RNA as heterodimer"]
[file:human/SRP9/SRP9-uniprot.txt "The complex of SRP9 and SRP14 is required for SRP\nCC       RNA binding"]

Review (PMID:34208095, full text available) describes the elongation arrest mechanism:
[PMID:34208095 "SRP9 and SRP14 function in elongation arrest"]
[PMID:34208095 "SRP changes its conformation, positioning SRP9/14 proteins forming the Alu domain near the elongation factor binding site of the ribosome, physically preventing synthesis of polypeptides"]
[PMID:34208095 "the Alu domain, which consists of the binding region for the heterodimer SRP9 and SRP14"]
[PMID:34208095 "Neither SRP9 nor SRP14 in mammals can bind 7SL RNA by itself; they heterodimerize before binding the RNA"]

This supports:
- MF: SRP RNA / 7S RNA binding (GO:0008312) within SRP, as the SRP9/14 heterodimer
- BP: negative regulation of translational elongation (GO:0045900) — elongation arrest
- BP: SRP-dependent cotranslational protein targeting to membrane (GO:0006614)
- CC: signal recognition particle (GO:0005786 / GO:0048500)

## Complex membership
SRP is a ribonucleoprotein of one 7SL RNA (~300 nt) and six proteins: SRP72, SRP68,
SRP54, SRP19, SRP14, SRP9. SRP9 forms the Alu-domain heterodimer with SRP14.
[file:human/SRP9/SRP9-uniprot.txt "Component of a signal recognition particle complex that\nCC       consists of a 7SL RNA molecule of 300 nucleotides and six protein\nCC       subunits: SRP72, SRP68, SRP54, SRP19, SRP14 and SRP9"]

ComplexPortal: CPX-2652 Signal recognition particle.
[file:human/SRP9/SRP9-uniprot.txt "ComplexPortal; CPX-2652; Signal recognition particle."]

Structural evidence: X-ray of SRP9 (2-86) in complex with SRP14 (PMID:11089964,
"Structure and assembly of the Alu domain of the mammalian signal recognition particle";
abstract NOT cached). Cryo-EM of SRP in complex with ribosome-nascent chain and SRP
receptor (PMID:34020957; abstract NOT cached). Both establish the Alu/elongation-arrest
geometry and SRP9 as an Alu-domain RNA-binding subunit — SRP9 itself is NOT a GTPase
(the GTPases in the pathway are SRP54, SRα, SRβ).
[PMID:34208095 "There are three GTPases: SRP54 and SRα ... and SRβ"]

## Original characterization (PMID:7730321, abstract only)
Hsu, Chang & Maraia 1995 characterized human SRP9; SRP9/14 = the Alu RNA-binding
protein (RBP); binds the Alu region of 7SL plus scAlu/scB1 RNAs with high affinity.
[PMID:7730321 "together with hSRP14 (SRP9/14), forms the activity previously identified as Alu \nRNA-binding protein (RBP)"]
[PMID:7730321 "This region of 7SL RNA together \nwith 9- and 14-kDa polypeptides (SRP9/14) regulates translational elongation of \nribosomes engaged by SRP"]
This GOA reference (PMID:7730321) underlies the TAS annotations RNA binding (GO:0003723)
and signal recognition particle binding (GO:0005047). It also was used (PINC) for a
GO:0005785 "signal recognition particle receptor complex" CC annotation — but the paper
is about SRP9 in SRP (the Alu RBP), not the SR (SRα/SRβ) receptor complex. SRP9 is a
component of SRP, not of the SRP receptor complex. GO:0005785 is likely a curation
mislabel (SRP vs SRP receptor confusion) and is an over/mis-annotation.

## Subcellular location
UniProt: Cytoplasm. SRP9/14 colocalizes in the nucleolus during SRP biogenesis (review),
but the mature functional location is cytoplasm/cytosol.
[file:human/SRP9/SRP9-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm."]

## protein binding (GO:0005515, IPI) annotations
Many IPI "protein binding" annotations exist. Several name SRP14 (P37108) as the partner
(PMID:28514442, 30021884, 32296183, 33961781, 35271311, 40205054) — this is the genuine,
biologically central SRP9-SRP14 Alu heterodimer interaction. UniProt INTERACTION block:
[file:human/SRP9/SRP9-uniprot.txt "P49458; P37108: SRP14; NbExp=12; IntAct=EBI-350743, EBI-353399;"]
Others name unrelated high-throughput partners: ACTN2/P35609 (PMID:25910212);
CDHR3/Q6ZTQ4, DPP9/Q86TI2-2, RYBP/Q8N488 (PMID:32814053). PMID:24965446 reports SRP9
co-purifying with the pestivirus Npro RNP complex (P19712-PRO_0000038050), an
incidental ribosomal/RNP capture. Bare "protein binding" is uninformative per curation
guidelines; keep as non-core (do not REMOVE experimental IPI annotations).

## Conclusions for review actions
- Core MF: 7S/SRP RNA binding (GO:0008312) as the SRP9/14 Alu heterodimer; RNA binding
  (GO:0003723) is the correct but more general parent.
- Core BP: SRP-dependent cotranslational protein targeting to membrane (GO:0006614);
  negative regulation of translational elongation (GO:0045900, elongation arrest).
- Core CC: signal recognition particle (GO:0005786 / GO:0048500).
- GO:0005047 signal recognition particle binding (SRP9 binding to SRP) — acceptable but
  non-core (SRP9 IS part of SRP rather than an external SRP-binding factor; redundant with
  part_of SRP).
- GO:0005785 SRP receptor complex (part_of) — MODIFY/over-annotation: SRP9 is part of SRP,
  not the SRP receptor (SRα/SRβ) complex. Mark as over-annotated.
- GO:0006617 signal sequence recognition (NAS, ComplexPortal): signal-sequence recognition
  is SRP54's role, not SRP9's; SRP9 contributes elongation arrest. Keep as non-core
  (it is a complex-level NAS annotation; SRP9 is part of the complex that performs this).

## Falcon deep-research findings (incorporated 2026-06)

- Structural basis of the SRP9/14 Alu-domain RNA clamp: 2.0 A crystal structure of the human Alu RNP (SRP9/14 + Alu RNA) in the ribosome-stalling conformation; the heterodimer clamps the RNA and docks at the ribosomal elongation-factor binding site [PMID:26585389 "Retrotransposition and Crystal Structure of an Alu RNP in the Ribosome-Stalling Conformation"]. Added (HIGH) and used to strengthen the core 7S-RNA-binding and elongation-arrest core_functions.
- SRP9 contributes ~700 A^2 of the ~1,820 A^2 SRP9/14-RNA interface; mutations weakening the interface beyond DDG > 3.5 kcal/mol abolish Alu retrotransposition [PMID:26585389]. Links SRP9/14 binding energy to Alu retroelement activity.
- Noncanonical nuclear role: SRP9/14 localizes substantially in the nucleus and transcriptionally regulates the Pol III Alu-like transcripts 7SL (RN7SL1) and BC200 (BCYRN1) by modulating Pol III occupancy rather than RNA stability [PMID:37156570 "Nuclear SRP9/SRP14 heterodimer transcriptionally regulates 7SL and BC200 RNA expression"]. Added (MEDIUM); not core SRP function.
- Noncanonical splicing role: SRP9/14 binds closed/compact Alu RNA folds and regulates inclusion of Alu-derived exons (RNA structure predicts inclusion better than sequence motifs) [PMID:37309897 "Alu RNA fold links splicing with signal recognition particle proteins"]. Added (MEDIUM).
- Nucleolar assembly phase: GFP-SRP9 is mostly nuclear; SRP proteins associate with many nucleolar/ribosome-biogenesis factors and nucleolar integrity is required for proper SRP localization [PMID:38858088 "The nucleolar phase of signal recognition particle assembly"]. Added (MEDIUM); supports a nuclear/nucleolar biogenesis compartment for SRP9.
- Abundance/affinity context: primate SRP9/14 is present at ~20-fold molar excess over assembled SRP and binds 7SL with sub-nanomolar affinity, enabling extensive extra-canonical Alu-RNA regulation [PMID:39563162 "The role of SRP9/SRP14 in regulating Alu RNA"]. Added (MEDIUM, review).
- Reconstitution work indicates SRP54 and SRP68/72 dominate measurable SRP-ribosome affinity while the Alu (SRP9/14) domain contributes little to affinity, consistent with SRP9/14's role being steric/regulatory at the factor-binding site rather than high-affinity docking (Wild et al. 2019, DOI 10.1093/nar/gky1324). Consistent with existing review framing; notes-only (not added).
- Biomarker/association: higher SRP9 nuclear staining associates with improved recurrence-free survival in resected pancreatic cancer, modulated by nutrient/amino-acid status [PMID:38847231 "Significance of signal recognition particle 9 nuclear translocation: implications for pancreatic cancer prognosis"]. Added (LOW); association-level, not core function.
