# CHAF1B (Q13112) curation notes

## Identity and overview
- CHAF1B = Chromatin assembly factor 1 subunit B (CAF-1 subunit B), also "CAF-I p60 subunit",
  "M-phase phosphoprotein 7" (MPHOSPH7/MPP7). UniProt Q13112; HGNC:1911; 559 aa.
  Synonyms in record: CAF1A, CAF1P60, MPHOSPH7, MPP7 [file:human/CHAF1B/CHAF1B-uniprot.txt].
- Maps to chromosome 21q22 (Down syndrome region) [file:human/CHAF1B/CHAF1B-uniprot.txt
  "Proteomes; UP000005640; Chromosome 21"; PMID:16780588 "human chromosome 21 proteins"].
- Domain architecture: N-terminal WD40 beta-propeller (7 WD repeats, ~res 1-385) plus a
  C-terminal disordered/low-complexity region (386-559) that is heavily phosphorylated
  [file:human/CHAF1B/CHAF1B-uniprot.txt; "Belongs to the WD repeat HIR1 family"].

## Core function: medium subunit of CAF-1 histone H3-H4 chaperone
- CAF-1 (CHAF1A/p150, CHAF1B/p60, RBBP4/p48) is a three-subunit histone chaperone that
  assembles histone octamers onto replicating DNA in a cell-free system
  [PMID:7600578 "Chromatin assembly factor I (CAF-I) from human cell nuclei is a
  three-subunit protein complex that assembles histone octamers onto replicating DNA"].
- p60 contains WD repeats; p150 and p60 directly interact and are both required for
  DNA replication-dependent assembly of nucleosomes; deletion of the p60-binding domain
  from p150 prevents chromatin assembly [PMID:7600578 "p150 and p60 directly interact and
  are both required for DNA replication-dependent assembly of nucleosomes. Deletion of the
  p60-binding domain from the p150 protein prevents chromatin assembly"].
- p150 and p60 form complexes with newly synthesized histones H3 and acetylated H4
  [PMID:7600578 "p150 and p60 form complexes with newly synthesized histones H3 and
  acetylated H4 in human cell extracts, suggesting that such complexes are intermediates
  between histone synthesis and assembly onto replicating DNA"].
- The chromatin assembly complex (CAC) contains the three CAF-1 subunits (p150, p60, p48)
  plus H3 and H4 and promotes DNA replication-dependent chromatin assembly
  [PMID:8858152 "a chromatin assembly complex (CAC), which contains the three subunits of
  CAF-1 (p150, p60, p48) and H3 and H4, and promotes DNA replication-dependent chromatin
  assembly"].
- CAF-1 is the histone chaperone for the replication-coupled (DNA-synthesis-dependent)
  H3.1 deposition pathway; the H3.1 complex contains CAF-1 and is necessary for
  DNA-synthesis-dependent nucleosome assembly [PMID:14718166 "The H3.1 and H3.3 complexes
  contain distinct histone chaperones, CAF-1 and HIRA, that we show are necessary to mediate
  DNA-synthesis-dependent and -independent nucleosome assembly, respectively"].
- p60 binds histones H3.1/H3.2/H3.1t [file:human/CHAF1B/CHAF1B-uniprot.txt "Interacts with
  histones H3.1, H3.2 and H3.1t (PubMed:33857403)"].

## Subcellular localization and cell cycle regulation
- All three CAF-1 subunits present throughout the cell cycle. In interphase p150 and p60 are
  nuclear; during S phase concentrated at sites of intranuclear DNA replication; they
  dissociate from chromatin during mitosis [PMID:9614144 "In interphase, p150 and p60 are
  bound to the nucleus, but they predominantly dissociate from chromatin during mitosis.
  During S phase, p150 and p60 are concentrated at sites of intranuclear DNA replication"].
- During mitosis the p60 subunit of inactive CAF-1 is hyperphosphorylated and displaced to
  the cytosol; progressively dephosphorylated from G1 to S/G2 [PMID:9614144 "In mitosis, the
  p60 subunit of inactive CAF-1 is hyperphosphorylated"; file:human/CHAF1B/CHAF1B-uniprot.txt
  PTM]. UniProt: Nucleus and Cytoplasm (M-phase cytoplasmic), DNA replication foci.
- Chromosome-21 protein localization screen independently observed CHAF1B nuclear at
  interphase, translocating to cytoplasm of daughter cells after cytokinesis
  [PMID:16780588 "most of the CHAF1B protein localizing in the nucleus at interphase, where
  it is involved in chromatin assembly and DNA replication. After cytokinesis ... we detected
  the presence of the CHAF1B protein in the cytoplasm of two daughter cells"].
- HDA/HPA mass-spec/immunofluorescence localizations (cytosol, nucleoplasm) are high-throughput
  and consistent with the cell-cycle-dependent nucleo-cytoplasmic distribution; the cytosolic
  pool corresponds to the M-phase inactive form (colocalizes_with qualifier in GOA).

## DNA repair link
- Phosphorylated CAF-1 (p60) is recruited to chromatin undergoing DNA repair after UV
  irradiation in G1, S or G2 [file:human/CHAF1B/CHAF1B-uniprot.txt PTM; FUNCTION
  ECO:0000269|PubMed:9813080 "assembles histone octamers onto DNA during replication and
  repair"]. Supports the DNA-repair-coupled chromatin assembly role (UniProtKB-KW DNA repair).

## Protein-binding (IPI) annotations — assessment
The bare GO:0005515 protein binding IPI annotations capture interaction partners but are
uninformative as molecular function:
- PMID:16980972 — ASF1A (Q9Y294) and ASF1B (Q9NVP2): CAF-1 p60 uses B-domain-like motifs to
  bind ASF1a, mutually exclusive with HIRA binding [PMID:16980972 "CAF-1 p60 also employs
  B-domain-like motifs for binding to ASF1a, thereby competing with HIRA"]. Functionally
  meaningful (histone-chaperone hand-off) but term is generic protein binding.
- PMID:24981860 (ASF1A/Q9Y294), PMID:27705803, PMID:28514442, PMID:33961781, PMID:40205054 —
  high-throughput AP-MS / interactome maps (BioPlex 2.0/3.0, Polycomb complexome, chromatin
  interactome, multimodal cell maps). Generic, not specific MF. ASF1B (Q9NVP2) is the
  recurrent interactor consistent with the ASF1-CAF-1 histone hand-off.

## Recommended curation summary
- Core: histone chaperone (CAF-1 medium/p60 subunit), part of CAF-1 complex, DNA
  replication-dependent (and repair-coupled) chromatin/nucleosome assembly, nuclear.
- ACCEPT: CAF-1 complex (GO:0033186), DNA replication-dependent chromatin assembly
  (GO:0006335), chromatin (GO:0000785), nucleus (GO:0005634), histone binding (GO:0042393).
- MARK_AS_OVER_ANNOTATED: all bare protein binding (GO:0005515) IPI rows; broad
  protein-containing complex (GO:0032991).
- KEEP_AS_NON_CORE: cytoplasm/cytosol localizations (M-phase inactive pool), nucleoplasm.
- chromatin binding (GO:0003682, TAS) is acceptable but generic; histone binding is more
  informative MF.
