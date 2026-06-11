# RNF5 (RMA1) review notes

UniProt: Q99942 (RNF5_HUMAN), 180 aa, gene RNF5 / synonyms RMA1, NG2, G16. HGNC:10068. Chromosome 6 MHC class III region.

## Core identity
RNF5 is a membrane-anchored RING-type E3 ubiquitin ligase (EC 2.3.2.27). It has a C3HC4 RING domain (ZN_FING 27-68; catalytic Cys-42, mutation C42S abolishes ligase activity) and two C-terminal transmembrane helices (118-138, 160-180) that anchor it to the ER membrane (tail-anchored / multi-pass).

[file:human/RNF5/RNF5-uniprot.txt "Membrane-bound E3 ubiquitin-protein ligase that mediates ubiquitination of target proteins"]
[file:human/RNF5/RNF5-uniprot.txt "MUTAGEN 42 ... C->S: Loss of E3 ubiquitin-protein ligase activity"]

## Primary role: ERAD of misfolded membrane proteins (incl. CFTR/CFTRdeltaF508)
RNF5/RMA1 is one of the founding mammalian ER-associated E3 ligases for ERAD. It primes misfolded CFTR/CFTRdeltaF508 for degradation co-translationally, acting in an ER-membrane complex with the E2 Ubc6e and Derlin-1, upstream of/parallel to the cytosolic Hsc70/CHIP branch.

[PMID:16901789 "We identified an ER membrane-associated ubiquitin ligase complex containing the E3 RMA1, the E2 Ubc6e, and Derlin-1 that cooperates with the cytosolic Hsc70/CHIP E3 complex to triage CFTR and CFTR Delta F508"]
[PMID:24019521 "Cystic fibrosis transmembrane conductance regulator (CFTR) is one ERAD substrate targeted to co-translational degradation by the E3 ligase RNF5/RMA1"]

## Functional redundancy with RNF185
RNF5 and its paralog RNF185 form a partly redundant ERAD E3 module for CFTR; simultaneous depletion profoundly blocks CFTRdeltaF508 degradation. RNF5 interacts physically with RNF185 (IntAct).

[PMID:24019521 "Our data thus identify RNF185 and RNF5 as a novel E3 ligase module that is central to the control of CFTR degradation"]
[PMID:24019521 "simultaneous depletion of RNF5 and RNF185 profoundly blocks CFTRΔF508 degradation not only during translation but also after synthesis is complete"]

## E2 partners / ubiquitin chain topologies
RNF5 works with UBE2D (UbcH5) family E2s and can use Ubc13 (UBE2N) for K63 chains. It builds K48 chains on CFTR (degradative) and K63 chains on JAMP/JKAMP (non-degradative, regulatory).

[PMID:19269966 "RNF5 mediates Lys-63-based polyubiquitination of JAMP"]
[PMID:19269966 "CFTR ubiquitination occurred at the canonical Lys-48 topology"]
[file:human/RNF5/RNF5-uniprot.txt "Mediates the 'Lys-63'-linked polyubiquitination of JKAMP thereby regulating JKAMP function by decreasing its association with components of the proteasome and ERAD; the ubiquitination appears to involve E2 ubiquitin-conjugating enzyme UBE2N"]

## Secondary / non-core roles (pleiotropic)
- Antiviral immunity: K48-linked ubiquitination and degradation of STING1/MITA at Lys-150 at mitochondria, negatively regulating type I IFN responses. Note this is at mitochondria, not ER, and is a regulatory immune role.
  [PMID:19285439 "RNF5 targeted MITA at Lys150 for ubiquitination and degradation after viral infection"]
  [PMID:19285439 "virus-induced ubiquitination and degradation of MITA by RNF5 occurred at the mitochondria"]
- Autophagy: regulates basal autophagy by controlling stability of membrane-associated ATG4B, limiting LC3 processing.
  [PMID:23093945 "the membrane-associated E3 ligase RNF5 regulates basal levels of autophagy by controlling the stability of a select pool of the cysteine protease ATG4B"]
- Cell motility: non-canonical (Ubc13/K63) ubiquitination of paxillin (PXN), altering its localization.
  [PMID:12861019 "the human homologue of RNF5 associates with the amino-terminal domain of paxillin, resulting in its ubiquitination"]
- Breast cancer / glutamine carrier (SLC1A5, SLC38A2) regulation under ER stress (PMID:25759021).

## Localization
UniProt records Cell membrane (plasma membrane, PMID:9533025 early study), Mitochondrion membrane (PMID:19285439), and ER membrane (PMID:19285439). The functionally dominant ERAD location is the ER membrane. Plasma membrane and mitochondrial membrane localizations are real but reflect the original cloning paper and the antiviral/MITA study respectively. ER membrane is the core compartment for the ligase's ERAD function.

[file:human/RNF5/RNF5-uniprot.txt "Endoplasmic reticulum membrane {ECO:0000269|PubMed:19285439}; Multi-pass membrane protein"]

## Annotation review decisions (summary)
- ubiquitin protein ligase activity (GO:0061630): CORE, ACCEPT (IBA/IEA/TAS/EXP all supported; EC 2.3.2.27).
- ERAD pathway (GO:0036503): CORE, ACCEPT (IBA, IMP PMID:24019521 & PMID:19269966).
- ER membrane (GO:0005789): CORE location, ACCEPT.
- zinc ion binding (GO:0008270): KEEP_AS_NON_CORE (structural RING feature).
- protein binding (GO:0005515, many IPI): KEEP_AS_NON_CORE (uninformative; includes meaningful E2 and CFTR/Derlin partners but bare term not core).
- ubiquitin-like protein conjugating enzyme binding (GO:0044390): ACCEPT non-core / KEEP_AS_NON_CORE — reflects E2 (UBE2D/UBE2N) binding, informative-ish but ancillary to ligase activity.
- K48-linked (GO:0070936) and K63-linked (GO:0070534) ubiquitination: ACCEPT (IDA, both topologies demonstrated).
- protein-containing complex binding (GO:0044877): KEEP_AS_NON_CORE.
- plasma membrane (GO:0005886), mitochondrial membrane (GO:0031966), membrane (GO:0016020): KEEP_AS_NON_CORE (real but secondary; ER membrane is core).
- transmembrane transport (GO:0055085, Reactome TAS): MARK_AS_OVER_ANNOTATED — RNF5 is not a transporter; this is pathway-context (ABC transport / CFTR) bleed-through, not a direct RNF5 function.
- endoplasmic reticulum mannose trimming (GO:1904380, IEA ARBA / Reactome TAS): MARK_AS_OVER_ANNOTATED — RNF5 does not trim mannose; this is pathway-adjacency over-annotation.
- ER quality control compartment (GO:0044322, IEA inter-ontology link): KEEP_AS_NON_CORE / ACCEPT — plausible localization from ERAD inference.
- identical protein binding (GO:0042802): KEEP_AS_NON_CORE (RNF5 self-interaction in interactome screens).
