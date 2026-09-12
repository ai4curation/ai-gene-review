# PRPS1 review notes

UniProtKB:P60891, human PRPS1 (ribose-phosphate pyrophosphokinase 1 / PRPP synthetase 1 / PRS-I). X-linked (Xq22.3), 318 aa, EC 2.7.6.1.

## Core function (well established)
- Catalyzes transfer of the beta,gamma-diphosphoryl group of ATP to ribose-5-phosphate:
  D-ribose 5-phosphate + ATP = 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) + AMP + H+
  (RHEA:15609) [file:human/PRPS1/PRPS1-uniprot.txt "Catalyzes the synthesis of phosphoribosylpyrophosphate (PRPP)"].
- PRPP is the activated precursor used by de novo and salvage purine, pyrimidine, and pyridine
  (NAD) nucleotide biosynthesis; PRPS1 is the metabolic bridge from the pentose phosphate pathway
  (ribose-5-P) into nucleotide metabolism [PMID:16939420 "PRPP (phosphoribosylpyrophosphate) is an important metabolite essential for"].
- Mg2+-dependent; activated by inorganic phosphate; feedback-inhibited by ADP/GDP
  [file:human/PRPS1/PRPS1-uniprot.txt "Activated by magnesium and inorganic phosphate."]; KM 23 uM ATP, 54 uM R5P (PMID:7593598).
- Cytosolic. Assembles as homodimer; active form probably a hexamer of 3 homodimers (crystal structure PMID:16939420).

## Disease (dosage-sensitive, bidirectional)
- Loss-of-function -> Arts syndrome (PMID:17701896), CMTX5/Rosenberg-Chutorian (PMID:17701900), DFNX1/DFN2 nonsyndromic deafness (PMID:20021999).
- Gain-of-function (feedback-resistant) -> PRPP synthetase superactivity: purine overproduction, hyperuricemia/gout (PMID:7593598, PMID:8253776, PMID:12847698).
- Intermediate p.V142L bridges both (PMID:22246954).

## Annotation decisions
- All GO:0004749 (MF), GO:0006015 (PRPP biosynth), GO:0005524 (ATP binding), GO:0000287 (Mg binding),
  GO:0002189 (complex), GO:0034214 (hexamerization), GO:0042802/GO:0042803 (self-association): ACCEPT — core.
- GO:0006164 (purine nucleotide biosynth), GO:0009156, GO:0009165: ACCEPT — PRPP feeds these.
- GO:0006221 (pyrimidine nucleotide biosynth, NAS): ACCEPT — PRPP is substrate for de novo pyrimidine (UMP synthase/OPRT).
- GO:0006144 (purine nucleobase metabolic process): ACCEPT (broad but correct).
- GO:0034418 urate biosynth, GO:0046101 hypoxanthine biosynth: KEEP_AS_NON_CORE — downstream metabolic consequences seen in superactivity, not the direct MF.
- GO:0007399 nervous system development: KEEP_AS_NON_CORE — pleiotropic disease phenotype (CMTX5/Arts), housekeeping enzyme not neuron-specific.
- GO:0005515 bare protein binding (IntAct/Y2H high-throughput, incl. PMID:32814053 neurodegeneration screen): MARK_AS_OVER_ANNOTATED — uninformative.
- GO:0008584 male gonad development (Ensembl IEA from rat ortholog): MARK_AS_OVER_ANNOTATED — single-organism electronic transfer, not a demonstrated human function.
