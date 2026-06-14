# CIPK24 / SOS2 (Q9LDI3, At5g35410) — research notes

## Identity
- UniProt Q9LDI3, RecName "CBL-interacting serine/threonine-protein kinase 24"; AltNames "Protein SALT OVERLY SENSITIVE 2" and "SNF1-related kinase 3.11"; gene names CIPK24, SnRK3.11, SOS2; locus At5g35410. Arabidopsis thaliana (NCBITaxon:3702). EC 2.7.11.1. [CIPK24-uniprot.txt lines 6-10]
- Belongs to "protein kinase superfamily. CAMK Ser/Thr protein kinase family. SNF1 subfamily." [CIPK24-uniprot.txt line 238-239]
- Domain architecture: N-terminal protein kinase domain (11..264), regulatory C-terminal region containing NAF/FISL domain (305..329) that binds CBL calcium sensors, and a PPI motif (336..365) that binds PP2C phosphatases (ABI1/ABI2). Activation loop 152..179; catalytic Lys at 40 (ATP binding); proton acceptor Asp at 134. [CIPK24-uniprot.txt lines 320-347]

## Core biology (synthesized)
CIPK24/SOS2 is a genuine, catalytically active Ser/Thr protein kinase that is the central kinase of the SOS (Salt Overly Sensitive) pathway. It is held inactive by an autoinhibitory C-terminal domain (the NAF/FISL motif). Binding of a Ca2+-loaded calcineurin-B-like (CBL) calcium sensor to the NAF motif relieves autoinhibition and activates the kinase in a Ca2+-dependent manner. The activated CBL–CIPK24 complex phosphorylates and activates downstream membrane transporters to restore Na+/K+ homeostasis under salt stress.

- At the plasma membrane, CBL4/SOS3 (myristoylated) recruits and activates SOS2, and the SOS2–SOS3 complex phosphorylates the autoinhibitory C-terminus of the plasma-membrane Na+/H+ antiporter SOS1/NHX7, relieving SOS1 autoinhibition and driving Na+ extrusion. [PMID:21262798 "SOS1 is relieved from auto-inhibition upon phosphorylation of the auto-inhibitory domain by SOS2-SOS3"]
- At the tonoplast, CBL10/SCABP8 recruits SOS2 to vacuolar membranes to regulate Na+ sequestration/compartmentalization, important mainly in shoots. [PMID:17825054 "the CBL10-CIPK24 (SOS2) complex is associated with the vacuolar compartments"; PMID:17449811 "SCABP8 ... recruit SOS2 to the plasma membrane, enhance SOS2 activity in a calcium-dependent manner, and activate SOS1 in yeast"]

## Evidence by reference

### PMID:10725382 (Liu et al. 2000, PNAS) — full text available
Positional cloning of SOS2; encodes a Ser/Thr kinase with N-terminal catalytic domain similar to yeast SNF1. "Autophosphorylation assays show that SOS2 is an active protein kinase." Kinase activity required for salt tolerance; sos2-5 G197E and K40N abolish autophosphorylation. [PMID:10725382 "Autophosphorylation assays show that SOS2 is an active protein kinase"] Supports protein kinase activity (IDA) and ATP binding (catalytic Lys-40). Transcript "up-regulated by salt stress in the root."

### PMID:10725350 (Halfter et al. 2000, PNAS) — full text available
SOS3 physically interacts with and activates SOS2 in a Ca2+-dependent manner; interaction via the C-terminal regulatory domain of SOS2; sos2 sos3 double mutant epistasis shows same pathway. [PMID:10725350 "SOS3 activates SOS2 protein kinase activity in a Ca 2+ -dependent manner"] Supports functional CBL4/SOS3 (O81223) binding and Ca2+-dependent kinase activation.

### PMID:11402167 (Guo et al. 2001, Plant Cell) — full text available
Identified the 21-aa SOS3-binding motif (NAF) in SOS2 that is also the autoinhibitory domain; removal of the regulatory domain gives constitutive (SOS3-independent) kinase activity; T168D in activation loop also constitutively activates. [PMID:11402167 "Removal of the regulatory domain of SOS2, including the SOS3 binding motif, resulted in constitutive activation of the protein kinase, indicating that the SOS3 binding motif can serve as a kinase autoinhibitory domain"] Supports CBL4/SOS3 (O81223) and CBL1 (O81445) binding via NAF motif and the autoinhibition/activation mechanism.

### PMID:14504388 (Ohta et al. 2003, PNAS) — full text available
Identified the 37-aa PPI motif of SOS2 necessary and sufficient for interaction with PP2C phosphatase ABI2 (O04719). [PMID:14504388 "a novel protein domain of 37 amino acid residues, designated as the protein phosphatase interaction (PPI) motif, of SOS2 that is necessary and sufficient for interaction with ABI2"] Supports specific ABI2 interaction (negative regulation by PP2C).

### PMID:14730064 (Kolukisaoglu et al. 2004, Plant Physiol) — full text available
Genomics of the CBL-CIPK network; 10 CBLs and 25 CIPKs in Arabidopsis. IntAct entries map CIPK24 interactions with CBL1 (O81445) and CBL9 (Q9LTB8). Establishes CIPK24 as a member of CBL-interacting kinase family. NOTE: this paper now carries an Expression of Concern and an Erratum per the cached record. [PMID:14730064 "These proteins form a complex network with their target kinases being the CBL-interacting protein kinases (CIPKs)"]

### PMID:17449811 (Quan et al. 2007, Plant Cell) — abstract only (full_text_available: false)
SCABP8/CBL10 binds Ca2+, interacts with SOS2 in vitro and in vivo, recruits SOS2 to the plasma membrane, enhances SOS2 activity in a Ca2+-dependent manner, activates SOS1 in yeast; CBL10 acts mainly in shoots, SOS3 mainly in roots. IntAct maps CBL4/SOS3 (O81223) and CBL10 (Q7FRS8). [PMID:17449811 "recruit SOS2 to the plasma membrane, enhance SOS2 activity in a calcium-dependent manner, and activate SOS1 in yeast"]

### PMID:17825054 (Kim et al. 2007, Plant J) — abstract only (full_text_available: false)
CBL10 interacts with CIPK24/SOS2; CBL10-CIPK24 complex associated with vacuolar compartments responsible for salt storage/detoxification. Basis for the IDA "plant-type vacuole membrane" localization annotation. [PMID:17825054 "the CBL10-CIPK24 (SOS2) complex is associated with the vacuolar compartments that are responsible for salt storage and detoxification in plant cells"]

### PMID:19448033 (Lin et al. 2009, Plant Cell) — full text available
SOS2 phosphorylates SCaBP8/CBL10 at C-terminal Ser-237 (does NOT phosphorylate SOS3); phosphorylation is salt-induced, occurs at the membrane, stabilizes the SCaBP8-SOS2 complex, and enhances plasma membrane Na+/H+ exchange. [PMID:19448033 "SOS2 phosphorylates SCaBP8 at its C terminus ... this phosphorylation was induced by salt stress, occurred at the membrane, stabilized the SCaBP8-SOS2 interaction, and enhanced plasma membrane Na+/H+ exchange activity"] Supports kinase activity acting on a CBL substrate (CBL10 isoform Q7FRS8-2).

### PMID:21262798 (Quintero et al. 2011, PNAS) — full text available
Mechanism of SOS1 activation: SOS1 held in resting state by C-terminal autoinhibitory domain; SOS2-SOS3 phosphorylates it to relieve autoinhibition; mutation of the SOS2 phosphorylation/recognition site impairs SOS1 activation in vivo and in vitro. IntAct maps SOS3/CBL4 (O81223) and SOS1/NHX7 (Q9LKW9). [PMID:21262798 "SOS1 is relieved from auto-inhibition upon phosphorylation of the auto-inhibitory domain by SOS2-SOS3"] Strongest direct support for SOS2 substrate = SOS1 and for regulation of sodium ion transport.

### PMID:17785451 (Verslues et al. 2007, MCB) — full text available
SOS2 interacts with NDPK2 (O64903) and catalases, linking salt stress and H2O2 signaling; sos2 ndpk2 double mutant more salt sensitive. SOS2 inhibits NDPK2 autophosphorylation. [PMID:17785451 "SOS2 was found to interact with the H2O2 signaling protein nucleoside diphosphate kinase 2 (NDPK2)"] Supports a specific protein interaction beyond CBL/transporters; a secondary (non-core) branch.

### PMID:9668136 (Zhu et al. 1998, Plant Cell) — abstract only (full_text_available: false)
Genetic screen defining the SOS2 locus; sos2 mutants specifically hypersensitive to Na+/Li+ (not general osmotic stress), and impaired in K+ nutrition; SOS1/SOS2/SOS3 act in the same pathway. Basis for IMP "response to salt stress." [PMID:9668136 "sos2 mutants are specifically hypersensitive to inhibition by Na+ or Li+ and not hypersensitive to general osmotic stresses"]

### PMID:40726285 (Wang et al. 2025, Plant J) — abstract only (full_text_available: false)
Nuclear branch: salt-induced SSN1 (AT2G36080) condensation; SSN1 co-condenses with PIF4 via assembling a SOS2-PIF4 complex in nuclear salt bodies to facilitate PIF4 degradation. Supports a nuclear role for SOS2 and the nucleus localization annotation. [PMID:40726285 "SSN1 also co-condenses with another negative regulator PHYTOCHROME-INTERACTING FACTOR 4 (PIF4) through assembling the SALT OVERLY SENSITIVE 2 (SOS2)-PIF4 complex in the same salt body"]

### PMID:17360592 (high-density protein microarray) — full text available; PMID:32612234 (interactome/signal integration) — abstract only; PMID:21798944 (Arabidopsis interactome map) — abstract only; PMID:11006339 (SOS3 myristoylation) — full text available
These are high-throughput / interactome papers contributing the IntAct GO:0005515 "protein binding" IPI entries (CAM4/CAM7/CML9, CBL1, CBL9). 11006339 is primarily about SOS3 N-myristoylation but its IntAct entry maps the SOS2–SOS3 (O81223) binding pair.

## GO term definitions verified (QuickGO API, June 2026)
- GO:0055078 sodium ion homeostasis: "Any process involved in the maintenance of an internal steady state of sodium ions within an organism or cell."
- GO:0006883 intracellular sodium ion homeostasis: "A homeostatic process involved in the maintenance of a steady state level of sodium ions within a cell."
- GO:0030007 intracellular potassium ion homeostasis: "A homeostatic process involved in the maintenance of a steady state level of potassium ions within a cell."
- GO:0002028 regulation of sodium ion transport: "any mechanism that adjusts how sodium ions move into, out of, or within cells..."
- GO:0009651 response to salt stress (IMP basis = PMID:9668136).

## Localization synthesis
- Cytoplasm and nucleus (UniProt SUBCELLULAR LOCATION, ECO PMID:17825054). [CIPK24-uniprot.txt lines 226-229]
- Targeted to plasma membrane when bound to CBL1/CBL5; to tonoplast (plant-type vacuole membrane) when bound to CBL2/CBL10 — localization is partner-dependent, not constitutive. [CIPK24-uniprot.txt lines 227-229]
- Plant-type vacuole membrane (GO:0009705) is a genuine IDA localization for the CBL10-CIPK24 complex. [PMID:17825054]

## Curation decisions summary
- Kinase MF terms (GO:0004672 protein kinase activity, GO:0004674 Ser/Thr kinase, GO:0106310 protein serine kinase) and GO:0005524 ATP binding: ACCEPT — core, strongly experimentally supported (IDA autophosphorylation + biochemical KM/Vmax in UniProt, EC 2.7.11.1).
- GO:0009651 response to salt stress (IMP): ACCEPT — core, defining phenotype.
- GO:0007165 signal transduction (IEA): MARK_AS_OVER_ANNOTATED — true but vague; CBL-CIPK calcium signaling is the specific role; keep as non-core high-level.
- GO:0005515 protein binding (many IPI): MARK_AS_OVER_ANNOTATED per project guidance (uninformative bare term); the specific functional interactions (CBL4/SOS3, CBL10, SOS1, ABI2, NDPK2) are captured in reasons/core_functions. Do NOT remove (valid experimental IPI evidence exists).
- Localization (nucleus, cytoplasm, plant-type vacuole membrane): ACCEPT/KEEP_AS_NON_CORE; vacuole membrane is IDA.
</content>
</invoke>
