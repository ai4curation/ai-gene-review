# CASP3 (Caspase-3) review notes

UniProt: P42574 (CASP3_HUMAN), 277 aa precursor. EC 3.4.22.56. Peptidase C14A family.
Synonyms: CPP32, Yama, apopain, SCA-1. Heterotetramer of two p17 (large) + p12 (small) subunits.

## Core identity / molecular function
- CASP3 is a cysteine-dependent aspartate-directed endopeptidase: cleaves substrates after Asp
  with strict requirement for Asp at P1 and P4 (preferred motif DxxD-|-). [UniProt CATALYTIC ACTIVITY,
  "Strict requirement for an Asp residue at positions P1 and P4. It has a preferred cleavage sequence of Asp-Xaa-Xaa-Asp-|-"]
- It is the principal effector/executioner caspase of apoptosis. Purified as "apopain" responsible
  for PARP cleavage, derived from proenzyme CPP32; related to ICE and C. elegans CED-3. [PMID:7596430,
  "This enzyme, named apopain, is composed of two subunits ... derived from a common proenzyme identified as CPP32 ...
  apopain/CPP32 is important for the initiation of apoptotic cell death"]
- Activated by upstream initiator caspases (CASP8, CASP9, CASP10) and granzyme B; PTM section confirms
  cleavage by granzyme B, caspase-6, -8, -10 generates the two active subunits. [UniProt PTM]
- Caspase-3 is the major executioner caspase, more promiscuous than caspase-7, and "appears to be the major
  executioner caspase during the demolition phase of apoptosis." [PMID:18723680]

## Substrate cleavage / downstream demolition (all DEPEND on the same MF, mostly downstream processes)
- PARP1 cleavage at 216-Asp|Gly-217 (hallmark execution substrate). [UniProt FUNCTION; PMID:16374543 nuclear
  caspase-3 activation and PARP cleavage early in camptothecin apoptosis]
- ICAD/DFF45 cleavage -> releases CAD/DFF40 endonuclease for oligonucleosomal DNA fragmentation. Apoptotic
  DNA laddering relies on cytosolic DFF40/CAD activated by caspase processing of ICAD. [PMID:22253444]
- GATA-1 cleavage in erythroid precursors; Hsp70 protects GATA-1 during terminal erythroid differentiation
  (link to erythropoiesis). [PMID:17167422]
- Phospholipid scramblase / PtdSer exposure: cleaves XKR8 and ATP11C flippase to drive apoptotic PtdSer "eat me"
  signal; also XRCC4 cleavage releases fragment activating Xkr4 scrambling. [PMID:24904167 ATP11C flippase;
  PMID:33725486 XRCC4/Xkr4]
- IL-18 processing in monocytes (CASP3 contributes along with CASP1). [PMID:9334240]; note newer UniProt text
  says CASP3 "cleaves and inactivates IL18" (context-dependent).
- Pyroptosis crosstalk: cleaves/activates gasdermin-E (GSDME/DFNA5) to switch apoptosis to secondary
  necrosis/pyroptosis and permit IL-1b release. [PMID:28459430 caspase-3 cleavage of a gasdermin (GSDME);
  PMID:33852854 GSDME permits IL-1b release; Reactome R-HSA-9647632 CASP3 cleaves GSDME]
  CASP3 also cleaves/inactivates GSDMD (Reactome R-HSA-9686088), generally inhibiting GSDMD pyroptosis.
- Antiviral / innate immunity restraint: cleaves cGAS, MAVS, IRF3 to suppress type I IFN during apoptosis;
  cleaves NF-kB members p65/RelA, RelB, c-Rel to dampen cytokine production. [PMID:30878284; PMID:36002459]
- Tau cleavage (Alzheimer link), BACE/GGA3 -> amyloid-beta (APP processing). [PMID:12888622; PMID:9736630;
  PMID:17553422]
- Many additional substrates curated by Reactome (desmosomal cadherins, fodrin/spectrin, ROCK1, gelsolin,
  beta-catenin, MST kinases, etc.) — these are CASP3 substrate-cleavage reactions, located in cytosol/nucleus.

## Localization
- Cytoplasm (UniProt SUBCELLULAR LOCATION, PMID:15003516). Procaspase cytosolic; active CASP3 also translocates
  to nucleus during apoptosis (PARP, DFF45 cleavage there). Nuclear localization is functional/active-site
  context (PMID:16374543 nuclear caspase-3 activation; Reactome R-HSA-211219 translocation to nucleus).

## Regulation
- S-nitrosylation of catalytic Cys163 keeps procaspase inactive; denitrosylated on Fas activation. [UniProt PTM;
  PMID:10213689]
- Inhibited by XIAP (BIR2) and ubiquitinated/inhibited by BIRC6/BRUCE (relieved by SMAC/DIABLO). [UniProt;
  PMID:11257232 XIAP structure]
- ADP-riboxanation at Arg207 by bacterial CopC blocks activation (microbial infection).

## Curation strategy
- CORE molecular function: GO:0004197 cysteine-type endopeptidase activity (many IDA + IBA) -> ACCEPT.
  Broader MF parents (GO:0008234 cysteine-type peptidase, GO:0008233 peptidase, GO:0004175 endopeptidase) ->
  ACCEPT as correct-but-general. GO:0004190 aspartic-type endopeptidase activity is WRONG (CASP3 is a cysteine
  protease that cleaves after Asp; it is not an aspartic protease) -> REMOVE.
- CORE biological process: apoptotic process (GO:0006915), execution phase of apoptosis (GO:0097194),
  proteolysis (GO:0006508), protein processing/maturation -> ACCEPT.
- Pyroptosis terms (GO:0070269, GO:0140639) -> ACCEPT (well supported IDA, gasdermin cleavage).
- Many tissue/process annotations (neuron/erythrocyte/keratinocyte differentiation, hippocampus development,
  synapse pruning, platelet formation, learning/memory, muscle differentiation) are downstream non-apoptotic or
  tissue-specific roles -> KEEP_AS_NON_CORE.
- Long list of IEA GO_REF:0000107 "response to X" stimulus terms (hypoxia, glucose, nicotine, ethanol, X-ray,
  metal ion, etc.) are ortholog-transferred stimulus/response terms, not core; mostly KEEP_AS_NON_CORE; a few
  questionable MF transfers (aspartic-type endopeptidase, CDK inhibitor, phospholipase A2 activator) -> REMOVE/
  MARK_AS_OVER_ANNOTATED.
- bare protein binding (GO:0005515, IPI, many) -> MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE (uninformative;
  many from interactome screens). Do not endorse as core.
- Reactome cytosol/nucleoplasm CC TAS (dozens) -> ACCEPT location, but these are substrate-cleavage reaction
  contexts; cytosol/nucleus are valid.
