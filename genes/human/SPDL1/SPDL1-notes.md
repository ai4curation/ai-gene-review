# SPDL1 (Spindly) Gene Review Notes

## Gene Overview

SPDL1 (also known as CCDC99, Spindly, hSpindly) encodes Protein Spindly, a coiled-coil domain-containing protein that functions as a dynein adaptor at kinetochores during mitosis. UniProt: Q96EA4. 605 amino acids. Chromosome 5.

## Key Publications and Findings

### PMID:17576797 - Griffis et al. 2007, J Cell Biol
- **Title:** "Spindly, a novel protein essential for silencing the spindle assembly checkpoint, recruits dynein to the kinetochore."
- **VERIFIED: REAL** - Published in J Cell Biol 177:1005-1015 (2007). Authors: Griffis ER, Stuurman N, Vale RD. HHMI/UCSF.
- This is the discovery paper for Spindly. Identified via RNAi screen in Drosophila S2 cells.
- Key findings: Spindly accumulates on unattached kinetochores; required for SAC silencing in Drosophila; dynein cannot target to kinetochores after Spindly depletion; human homologue identified with similar function.
- [PMID:17576797 "After the depletion of Spindly, dynein cannot target to kinetochores, and, as a result, cells arrest in metaphase with high levels of kinetochore-bound Mad2 and RZZ."]

### PMID:19468067 - Chan et al. 2009, J Cell Biol
- **Title:** "Mitotic control of kinetochore-associated dynein and spindle orientation by human Spindly."
- **VERIFIED: REAL** - Published in J Cell Biol 185:859-874 (2009). Authors: Chan YW, Fava LL, Uldschmid A, Schmitz MH, Gerlich DW, Nigg EA, Santamaria A.
- The primary characterization paper for human Spindly. This is the main reference for most experimental GO annotations.
- Key findings:
  - hSpindly KT localization controlled by RZZ complex and Aurora B
  - Depletion causes reduced inter-KT tension, unstable KT fibers, prometaphase delay, severe chromosome misalignment
  - Depletion induces striking spindle rotation (rescued by co-depletion of dynein)
  - In contrast to Drosophila, hSpindly depletion does NOT abolish removal of MAD2 and ZW10 from KTs
  - Interacts with KNTC1 (Rod) and ZW10 (interactions appear weak/transient)
  - Localizes to outer kinetochore (IDA), spindle pole (IDA), nucleus in interphase (IDA)
- [PMID:19468067 "hSpindly depletion results in reduced inter-KT tension, unstable KT fibers, an extensive prometaphase delay, and severe chromosome misalignment. Moreover, depletion of hSpindly induces a striking spindle rotation"]

### PMID:25035494 - McKenney et al. 2014, Science
- **Title:** "Activation of cytoplasmic dynein motility by dynactin-cargo adapter complexes."
- **VERIFIED: REAL** - Published in Science 345:337-341 (2014). Authors: McKenney RJ, Huynh W, Tanenbaum ME, Bhabha G, Vale RD.
- Key finding: Spindly acts as an adapter protein linking the dynein motor complex to cargo; converts dynein from non-processive to highly processive motor in the presence of dynactin.
- This paper established the paradigm for dynein-dynactin activation by cargo adaptors (including BICD2, Spindly, etc.)

### PMID:30258100 - Conte et al. 2018, Sci Rep
- **Title:** "USP45 and Spindly are part of the same complex implicated in cell migration."
- **VERIFIED: REAL** - Published in Sci Rep 8:14375 (2018). Authors: Conte C, Griffis ER, Hickson I, Perez-Oliva AB.
- Key findings:
  - Spindly identified as a new interactor of USP45 by mass spectrometry
  - Interaction depends on catalytic activity of USP45
  - Spindly is monoubiquitinated; USP45 removes this monoubiquitin
  - USP45 has preferential activity on K48 ubiquitin chains
  - USP45 plays a role in cell migration similar to Spindly
- [PMID:30258100 "Spindly is mono-ubiquitylated and this can be specifically removed by USP45 in its active form but not by the catalytic inactive form"]

### PMID:23382074 - Armour et al. 2013, Mol Cell Biol
- **Title:** "A high-confidence interaction map identifies SIRT1 as a mediator of acetylation of USP22 and the SAGA coactivator complex."
- **VERIFIED: REAL** - Published in Mol Cell Biol 33:1487-1502 (2013).
- This paper is about SIRT1/USP22/SAGA complex. SPDL1 interaction with SIRT1 is likely a high-throughput finding from the interaction screen. The enzyme binding annotation (GO:0019899) from this paper is based on SPDL1 appearing in the SIRT1 interactome. The GOA annotation says the IPI is with Q96EB6 (SIRT1). This is from a large-scale interaction study.

### PMID:25416956 - Rolland et al. 2014, Cell
- **Title:** "A proteome-scale map of the human interactome network."
- **VERIFIED: REAL** - Large-scale yeast two-hybrid study. SPDL1 interactions detected: CA8, RTP5, PPP1R18, DNAAF4, TRAF4, USP15.

### PMID:25910212 - Sahni et al. 2015, Cell
- **Title:** "Widespread macromolecular interaction perturbations in human genetic disorders."
- **VERIFIED: REAL** - Follow-up to the interactome network study.

### PMID:26871637 - Yang et al. 2016, Cell
- **Title:** "Widespread Expansion of Protein Interaction Capabilities by Alternative Splicing."
- **VERIFIED: REAL** - Studies alternative splicing effects on protein interactions.

### PMID:33961781 - Huttlin et al. 2021, Cell
- **Title:** "Dual proteome-scale networks reveal cell-specific remodeling of the human interactome."
- **VERIFIED: REAL** - BioPlex 3.0 interactome study.

### Additional key papers (not in current annotations):

### PMID:20439434 - Gassmann et al. 2010, Genes Dev
- "Removal of Spindly from microtubule-attached kinetochores controls spindle checkpoint silencing in human cells."
- Identified conserved Spindly motif essential for dynein targeting to KT. Dynein-mediated removal of Spindly from KTs is the critical reaction in checkpoint silencing.

### PMID:20427577 - Barisic et al. 2010, Mol Biol Cell
- "Spindly/CCDC99 is required for efficient chromosome congression and mitotic checkpoint regulation."
- Showed Spindly is a mitotic phosphoprotein, interacts with RZZ, and levels at KT are regulated by MT attachment and tension.

### PMID:29915359 - Sacristan et al. 2018, Nat Cell Biol
- "Dynamic kinetochore size regulation promotes microtubule capture and chromosome biorientation in mitosis."
- Showed Spindly and RZZ drive kinetochore expansion (corona formation) in a dynein-independent manner. C-terminal farnesylation and MPS1 activity cause Spindly conformational changes promoting RZZ-Spindly oligomerization.

### PMID:25825516 - Moudgil et al. 2015, J Cell Biol
- Showed hSpindly undergoes farnesylation at C-terminal cysteine, essential for KT localization and RZZ interaction.

## BioReason Analysis Assessment

### Verified claims in BioReason's deep research:
- Correct: IPR028593 (Protein Spindly, chordates) and IPR051149 (Spindly/BICDR Dynein Motor Adapter)
- Correct: Dynein adapter function at kinetochores
- Correct: Coiled-coil architecture (residues 2-442)
- Correct: Roles in chromosome alignment, spindle orientation, protein localization to KT

### Questionable/unverified claims in BioReason:
- Claims about "BUB1B/BUB3" and "NDC80 complex" as direct Spindly receptors at the outer kinetochore: Not supported. Spindly binds via the RZZ complex (Rod/ZW10/Zwilch), not directly to BUB1B or NDC80. This is a significant error.
- Claims about "SKA1/2/3" and "CENP-F" as Spindly interactors: Not supported by literature. SKA complex and CENP-F are outer KT components but not established Spindly interactors.
- Claims about "HOX-D13" as a partner: No evidence for this. Likely hallucinated.
- Claims about "MKLN1 (BICDR)" association: BICDR1/BICDL1 (not MKLN1) is the related dynein adaptor. MKLN1 is muskelin, not the same protein. This is an error.
- The mention of GO:0098806 "Spindly-BICDR complex" needs verification - this GO term may not exist.
- Claims about "Golgi-directed transport" via Spindly: The cell migration role is documented but the Golgi mechanism is speculative.

### Summary of BioReason accuracy:
The BioReason analysis gets the broad strokes correct (dynein adaptor, kinetochore localization, chromosome alignment, spindle orientation) but contains several specific errors about binding partners (BUB1B, NDC80, SKA, CENP-F, HOX-D13, MKLN1) that are not supported by the literature. The actual RZZ complex interaction is underemphasized.
