# csc-1 (O45952) manual literature research

No deep-research API was available for this session. This file records a manual
literature survey performed with the cached publications and PubMed searches.

## Search log

- PubMed `csc-1[Title/Abstract] AND elegans`: 2 hits; PMID:12707312 (the CSC-1 discovery
  paper) and PMID:40741693 (unrelated: a bacterial strain also named CSC-1).
- PubMed combinations of CSC-1 / borealin / chromosomal passenger / BIR-1 / ICP-1 / elegans:
  no further hits indexed under the gene name.
- Cached publications cited by GOA: PMID:12707312 (full text), PMID:21110867 (full text).

The primary experimental literature specific to CSC-1 is therefore essentially one paper
(Romano et al. 2003). Later CPC work in C. elegans largely studies AIR-2, ICP-1 and BIR-1.

## Identity and family

- 249-aa protein, gene Y48E1B.12 on chromosome II. N-terminal predicted coiled coil
  (residues 12-48) and a long disordered C-terminal region [file:worm/csc-1/csc-1-uniprot.txt
  "COILED          12..48"].
- At discovery, no homologues outside C. briggsae were detected [PMID:12707312 "Surprisingly,
  with the exception of a sequence from the C. briggsae genome, no other sequences in the
  available databases have significant homology to CSC-1."].
- UniProt now places it in the borealin family, flagged as highly divergent
  [file:worm/csc-1/csc-1-uniprot.txt "Belongs to the borealin family. Highly divergent."].
  A later PDZ interactome paper also refers to it as a Borealin orthologue
  [PMID:21110867 "CSC-1 and ICP-1 are orthologs of Borealin and Incenp two components of the
  vertebrate chromosomal passenger complex (CPC)."].

## Key findings (PMID:12707312, Romano et al. 2003, J Cell Biol, full text)

- Loss of function (t1171, Q128 stop; and RNAi) phenocopies AIR-2/ICP-1/BIR-1 loss: defective
  meiotic chromosome segregation and polar body extrusion; failed mitotic congression and
  segregation; furrow forms but fails to complete [PMID:12707312 "In particular, meiotic
  chromosome segregation and polar body extrusion are defective."].
- Localization by immunofluorescence (RNAi-validated antibody): central region of meiotic
  bivalents, meiotic spindle midzone in anaphase I, mitotic chromosomes in metaphase,
  spindle midzone in anaphase/telophase [PMID:12707312 "During anaphase of meiosis I, CSC-1
  localizes to the midzone of the meiotic spindle"].
- CSC-1, BIR-1 and ICP-1 are interdependent for localization; AIR-2 requires all three
  [PMID:12707312 "AIR-2 requires CSC-1, BIR-1, and ICP-1 to localize to chromosomes."].
- CSC-1 co-immunoprecipitates BIR-1 and ICP-1 from embryo extracts; binds BIR-1 directly in
  vitro, dependent on the Zn-bound BIR domain [PMID:12707312 "CSC-1 and BIR-1 associate in the
  absence of any other nematode proteins"].
- ICP-1 binds robustly only to the CSC-1/BIR-1 subcomplex; AIR-2 binding to BIR-1 requires
  CSC-1 and ICP-1 [PMID:12707312 "The binding of AIR-2 to BIR-1 required CSC-1 (and ICP-1) and
  vice versa."].
- CSC-1/BIR-1 do not stimulate AIR-2 kinase activity; they are proposed targeting subunits
  [PMID:12707312 "suggest that CSC-1 and BIR-1 do not function primarily by regulating AIR-2
  kinase activity, at least toward the model substrate MBP."].
- Model: CSC-1/BIR-1/ICP-1 localize and activate AIR-2, activation by ICP-1 [PMID:12707312
  "Thus, we suggest that a complex containing CSC-1/BIR-1/ICP-1 functions to localize and
  activate AIR-2, the activation function being provided principally by ICP-1."].
- Not tested: spindle assembly checkpoint, sister chromatid separation per se.

## PDZ interactome (PMID:21110867, Lenfant et al. 2010)

- Yeast two-hybrid PDZ screen detected CSC-1 binding to PDZ domains of LIN-7/LIN-10 and other
  PDZ proteins (MAGI-1, AFD-1, P90976). Functional relevance unknown; authors raise only the
  possibility of a link [PMID:21110867 "This raises the possibility of an unsuspected functional
  link between these two protein complexes"].
