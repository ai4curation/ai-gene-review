# STE11 (YLR362W, UniProt P23561) curation notes

## Identity
- Ste11 is the budding-yeast MEKK-family MAP kinase kinase kinase (MAP3K); 717 aa, N-terminal SAM domain
  (20-84), autoinhibitory region carrying the Ste20 phosphosites, C-terminal Ser/Thr kinase domain (415-712)
  [file:yeast/STE11/STE11-uniprot.txt "Belongs to the protein kinase superfamily. STE Ser/Thr"].
- Not to be confused with the S. pombe HMG-box transcription factor Ste11 (the S. pombe Ste11 ortholog is
  Byr2, SPBC1D7.05, which appears as an IBA donor).

## Molecular function: MAP3K
- In vitro reconstitution: purified GST-Ste11 phosphorylates and activates Ste7, which phosphorylates Fus3
  [PMID:8159759 "reconstituted a kinase cascade in which STE11 phosphorylates and activates STE7, which in turn phosphorylates the mitogen-activated protein kinase FUS3"].
- Genetic ordering: Ste11 acts before Ste7 [PMID:8455599 "This modification of STE7 requires the STE11 kinase, which is proposed to act before STE7 during signal transmission"].
- HOG branch substrate is Pbs2 [PMID:16778768 "Ste11 phosphorylates residues in the activation loop of Pbs2, leading to its activation (step 8)"].
- Ste50 is also phosphorylated by Ste11 in vitro, but Ste50 is an adaptor, not a canonical output
  [PMID:10397774 "Ste50p appears to modulate Ste11p autophosphorylation and is itself a substrate of the Ste11p kinase"].

## Activation / regulation
- Activated by the PAK Ste20 (and Cla4 in the HOG branch), which phosphorylates the N-terminal
  autoinhibitory domain [PMID:10837245 "phosphorylation of Ste11p by Ste20p removes an amino-terminal inhibitory domain, leading to activation of the Ste11 protein kinase"];
  Cla4 redundancy in HOG [PMID:16778768 "providing evidence that Ste20 and Cla4 are functionally redundant in the SHO1 branch"].
- Ste50 binds Ste11 constitutively through a heterotypic SAM-SAM interaction [PMID:16337230 "depends upon a direct interaction between the sterile alpha motif (SAM) domains of the Ste11 mitogen-activated protein kinase kinase kinase (MAPKKK) and its regulator Ste50"];
  relieves N-terminal inhibition [PMID:10397774 "This interaction relieves a negative activity of the Ste11p N terminus"].

## Pathways (Ste11 is shared by three MAPK modules)
1. Pheromone response: Ste20 -> Ste11 -> Ste7 -> Fus3/Kss1, organised on the Ste5 scaffold
   [PMID:8062390 "Ste5 forms a multikinase complex that joins these kinases for efficient Fus3 activation"; PMID:7851759].
2. Filamentous / invasive growth: Ste20 -> Ste11 -> Ste7 -> Kss1 -> Ste12/Tec1
   [PMID:8259520 "in diploids some of the same kinases and STE12 are required for filamentous growth"; PMID:8001818 "the same components of the MAP kinase cascade necessary for diploid pseudohyphal development (STE20, STE11, STE7, and STE12) are also required for both filament formation and agar penetration in haploids"].
3. Sho1 branch of HOG: Sho1/Cdc42/Ste50 -> Ste11 -> Pbs2 -> Hog1
   [PMID:9180081 "A second osmosensor, Sho1p, also activated Pbs2p and Hog1p, but did so through the Ste11p MAPKKK"].
   Sho1 acts as adaptor bringing Ste11-Ste50 and Pbs2 together [PMID:16778768 "the Ste11-Ste50 complex binds to the cytoplasmic domain of Sho1, to which Pbs2 also binds"].
   The ste11 single mutant is osmotolerant; ssk2/22 ste11 is not (branch redundancy).
- Specificity: Ste5 (mating) and Sho1 (HOG) act as adaptors that pair Ste11 with Ste7 or Pbs2 respectively
  [PMID:16778768 "By the adaptor proteins (Sho1 and Ste5) that interact with both Ste11 and one of its substrate MAPKKs (Pbs2 and Ste7), Ste11 can thus change its MAPKK partners depending on the incoming stimulus"].

## Cell integrity / crosstalk (secondary)
- Cullen 2000: glycosylation mutants activate a Sho1 -> Ste20/Ste50 -> Ste11 -> Ste7 -> Kss1 -> Ste12 pathway;
  this is the Kss1 (filamentous growth) module, not the Pkc1-Bck1-Mkk1/2-Slt2 cascade that GO:0000196 is defined by
  [PMID:10880465 "We specifically suggest that a Sho1 --> Ste20/Ste50 --> Ste11 --> Ste7 --> Kss1 --> Ste12 pathway is responsible for activation of FUS1 transcription in these mutants"].
- Leng & Song 2016: Ste11-Mkk1 interaction via Nst1, proposed crosstalk to CWI [PMID:26787465]. Treat as non-core.

## Localization
- Cytoplasmic in unstressed cells, does not enter nucleus on osmostress [PMID:9755161 "we found that HOG1, PBS2 and STE11 localize to the cytoplasm of unstressed cells"];
  punctate relocalisation after osmostress, transient cortical recruitment via Ste50/Cdc42/Sho1 [PMID:16778768].

## Annotation decisions (summary)
- Core: MAPKKK activity (GO:0004709); pheromone response MAPK cascade (GO:0071507); Sho1 osmosensory
  pathway (GO:0007232) / p38MAPK (Hog1) cascade (GO:0038066); filamentous-growth signalling (GO:0001402;
  the newer GO:0062031 filamentous growth MAPK cascade names Ste11 explicitly in its definition).
- Non-core: pseudohyphal growth, invasive growth, cellular hyperosmotic response (organism-level outcomes),
  self-association.
- GO:0000196 cell integrity MAPK cascade: marked over-annotated (Ste11 is not a tier of the Slt2 cascade).
- Protein binding rows: Ste50 -> SAM domain binding; Ste5 and Sho1 -> scaffold protein binding; Fus3/Kss1 ->
  MAP kinase binding; Mkk1 -> MAP kinase kinase binding.
- PMID:8670882 (Van Aelst 1996, mammalian POR1/Rac1 paper) is the IntAct source for a Ste11 self-interaction;
  the abstract does not mention Ste11 (it was probably used as a two-hybrid control) -> UNDECIDED.
