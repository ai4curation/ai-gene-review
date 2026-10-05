# ESPL1 (separase, Q14674) - curation notes

## Identity and architecture

- Human ESPL1 encodes separase/separin, a 2,120-aa clan-CD (caspase-like) cysteine
  endopeptidase (EC 3.4.22.49). The catalytic domain is C-terminal (Peptidase_C50,
  IPR005314) with the active-site Cys2029 (UniProt FT ACT_SITE 2029); the large
  N-terminal region is a HEAT/TPR-like superhelical scaffold. [file:human/ESPL1/ESPL1-uniprot.txt
  "Caspase-like protease, which plays a central role in the chromosome segregation by cleaving the SCC1/RAD21 subunit of the cohesin complex at the onset of anaphase."]
- Catalytic cysteine is essential: the C2029A mutant is neither autoprocessed nor active
  [PMID:12672959 "The cysteine at the position 2029 of separase is essential for proteolytic activity and is conserved among all cysteine proteases"].

## Core biology

### 1. Cohesin kleisin cleavage triggers anaphase (core)

- Separase cleaves RAD21/SCC1 after Arg172 and Arg450 (ExxR consensus); efficient cleavage
  at the second site is promoted by PLK1 phosphorylation of S454
  [PMID:15737063 "separase cleaves Scc1 at the same sites that are cleaved at anaphase onset in vivo, Arg172 and Arg450"].
- Non-cleavable SCC1 blocks anaphase and cytokinesis completion in HeLa cells
  [PMID:11509732 "cohesin cleavage by separase is essential for sister chromatid separation and for the completion of cytokinesis"].
- Antisense depletion of separase produces lagging chromosomes
  [PMID:12672959 "Antisense oligonucleotide-mediated depletion of separase results in a >4-fold increase in the mitotic cells with lagging chromosomes"];
  RNAi depletion produces polyploid cells with unseparated sisters
  [PMID:12194817 "Inhibition of separase expression in human cells by RNA interference causes the formation of polyploid cells with large lobed nuclei."].
- Reactome models the reaction explicitly [Reactome:R-HSA-2467809 "ESPL1 (separin i.e. separase) cleaves RAD21 (SCC1) subunit of centromeric cohesin at two sites"].
- Substrate recognition needs an exosite: the RAD21 LPE docking motif and linkers, not only the
  cleavage-site consensus [PMID:34290405 "Deletion of these linkers, or replacement with a random sequence, abolished Scc1 cleavage in vitro"].

### 2. Regulation: separase-securin complex, CDK1-cyclin B1, PP2A, autocleavage

- Before anaphase separase is bound by securin (PTTG1), which is both a folding chaperone
  and a pseudosubstrate inhibitor occupying the catalytic and docking sites
  [PMID:34290405 "Consistent with previous studies, we find that securin acts as an extended pseudosubstrate that blocks substrate binding at the catalytic site and at nearby docking sites."];
  [PMID:12194817 "securin prevents the access of substrate analogs to the active site of separase"].
- CDK1-cyclin B1-CKS1 binding (phospho-Ser1126 dependent) is mutually exclusive with securin and
  inhibits separase by structuring separase's own autoinhibitory loops
  [PMID:34290405 "Unexpectedly, Cdk1-cyclin B1-Cks1 suppresses separase activity by activating autoinhibitory sequences in loops of separase itself"].
- PP2A (B'56) bound to separase stabilises separase-associated securin, preventing precocious
  activation during checkpoint arrests [PMID:24781523 "PP2A keeps separase-associated securin in a dephosphorylated state, thereby selectively stabilizing this protease-bound pool of the anaphase inhibitor."].
- On release, separase autocleaves at R1486/R1506/R1535; fragments stay associated; autocleavage
  is not required for cohesin cleavage but is abolished by C2029A
  [PMID:12672959 "no cleavage products were detected even on prolonged induction up to 72 h"];
  [PMID:12194817 "allowing rapid autocatalytic cleavage of separase at one of three sites"];
  [Reactome:R-HSA-2467775 "is rapidly autocatalytically cleaved after arginine residues at positions 1506 and 1535"].

### 3. Centrosome: centriole disengagement (secondary, direct)

- Separase localises to centrosomes (gamma-tubulin co-staining) in prometaphase/metaphase and the
  signal disappears at anaphase onset [PMID:12672959 "revealed colocalization of separase and γ-tubulin in centrosomes during the early stages of mitosis"];
  no staining along spindle microtubules [PMID:12672959 "We have not observed separase staining along spindle microtubules"].
- Separase cleaves centrosomal cohesin and pericentrin-B/kendrin to promote centriole
  disengagement, licensing the next centrosome duplication
  [PMID:24781523 "Separase also cleaves centrosomal cohesin and pericentrin-B (kendrin), which promotes centriole disengagement and licensing of subsequent centrosome duplication"];
  the same paper shows securin-4D-driven premature separase activation causes premature centriole disengagement in G2-arrested cells.
- There is no GO term for centriole disengagement; the closest BP is GO:0007098 centrosome cycle
  (checked via QuickGO search "disengagement": no hits). Used in core_functions only.

### 4. Meiosis (conserved, mammalian evidence from mouse)

- Separase cleaves REC8 in mammalian meiosis; direct evidence is from mouse oocytes, not human
  germ cells [file:human/ESPL1/ESPL1-deep-research-falcon.md "In mammalian meiosis, separase cleaves the meiosis-specific kleisin REC8."].
- The IBA for GO:0051307 (node PTN000300670; donors A. thaliana, S. pombe, C. elegans) is a sound
  node placement; human ESPL1 is inside the clade and there is no evidence of loss.

### 5. Localisation

- Interphase: predominantly cytoplasmic, nuclear export sequence; excluded from the nucleus
  [PMID:24781523 "Because separase is excluded from the nucleus"];
  [file:human/ESPL1/ESPL1-deep-research-falcon.md "predominantly cytoplasmic in HeLa cells, partly because of a nuclear-export sequence"].
- UniProt: [file:human/ESPL1/ESPL1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm. Nucleus."]. HPA IF: nucleoplasm (GO_REF:0000052).
- Nuclear accumulation after DNA damage has been reported (deep research, secondary role in
  cohesin removal at DSBs) - not annotated here.

## Annotation decisions (summary of reasoning)

- Protein-binding IPI rows: PTTG1 partner rows (PMID:12194817, 20360068, 24781523, 26496610,
  33961781, 34290405) -> REMOVE as uninformative; there is no informative MF for the enzyme side
  of an enzyme-inhibitor pair, and the biology is captured by GO:1990520 separase-securin complex
  (IPI, ACCEPT) and by PTTG1's own inhibitor annotation. Interaction is not disputed.
  RAD21 partner rows (PMID:12672959, 15737063, 34290405) -> MODIFY to GO:0004197: RAD21 is the
  substrate; PMID:15737063 and PMID:34290405 contain direct in vitro cleavage assays.
- GO:0045842 positive regulation of mitotic metaphase/anaphase transition and GO:0045875 negative
  regulation of sister chromatid cohesion (both NAS): separase *executes* the cohesion-dissolving
  step downstream of APC/C; regulation terms misdescribe an effector -> MODIFY to GO:0051306.
- GO:0034088 / GO:0034090 maintenance of (mitotic/meiotic) sister chromatid cohesion (NAS,
  PMID:34290405): separase is the inhibited enzyme; being inhibited is not doing the work of
  maintaining cohesion (that is cohesin, shugoshin-PP2A and the inhibitors securin / CDK1-cyclin
  B1). These are the mirror image of PTTG1's correct annotations -> REMOVE. No meiotic data in
  the paper either.
- GO:0040001 establishment of mitotic spindle localization (NAS, PMID:12672959): the paper only
  discusses worm and budding-yeast separase in this context; no human data -> REMOVE.
- GO:0006915 apoptotic process (TAS, PMID:11875078): the paper shows RAD21 is cleaved by
  caspases-3/-7 during apoptosis and names separase only as the anaphase protease -> REMOVE.
- GO:0000281 mitotic cytokinesis (NAS, PMID:11509732): cytokinesis failure is a downstream
  consequence of unseparated chromatids in the cleavage plane -> MARK_AS_OVER_ANNOTATED.
- GO:0072686 mitotic spindle (IBA): human separase is at spindle poles/centrosomes but not along
  spindle microtubules; poles are part of the spindle so not contradicted -> KEEP_AS_NON_CORE.
- GO:0003824 catalytic activity (NAS) -> MODIFY to GO:0004197; GO:0000280 nuclear division
  (ARBA) -> MODIFY to GO:0051306. Other broad peptidase / proteolysis / chromosome segregation
  IEA/TAS rows ACCEPT (correct, less specific; specific term already present).
- NEW: GO:0016540 protein autoprocessing (IDA, PMID:12672959). Participation is unambiguous (the
  enzyme cleaves itself; C2029A abolishes processing; three sites mapped). Comparator check via
  QuickGO: GO:0016540 carries IDA/IMP annotations for self-processing proteases CASP1, CASP4,
  CASP6, CTSL, PCSK9, TMPRSS2, so the convention is to annotate autoprocessing enzymes with it.
  Parent is protein processing / proteolysis, which names the cleaving entity - here separase.

## Comparator / GO-CAM checks

- gocams/index.tsv has no human ESPL1 activity; modules/metaphase_anaphase_transition_and_mitotic_exit.yaml
  models ESPL1 as GO:0004197 acting in GO:0051306 in the nucleus with RAD21 as target - consistent
  with the core function here.
- Mouse Espl1 (Q4GYR1) GOA (QuickGO 2026-09): same IBA set (GO:0004197, GO:0051307, nucleus,
  cytoplasm, mitotic spindle) plus IDA nucleoplasm/cytoplasm; no centrosome, no autoprocessing.
