# GAI (GIBBERELLIC ACID INSENSITIVE) — research notes

UniProt: Q9LQT8 (GAI_ARATH), gene AT1G14920, 533 aa. GRAS family, DELLA subfamily.
Synonyms: GRAS family protein 3 / AtGRAS-3; RGA2; "Restoration of growth on ammonia protein 2".

## Core biology

GAI is one of five Arabidopsis DELLA proteins (GAI, RGA, RGL1, RGL2, RGL3) that act as
nuclear negative regulators (repressors) of the gibberellin (GA) signaling pathway.

- DELLA proteins are nuclear and **lack a DNA-binding domain**; they regulate transcription
  via protein–protein interactions rather than by binding DNA directly.
  [PMID:24989044 "DELLAs are nuclear proteins lacking a DNA binding domain and negatively regulate GA responses through interaction with other transcription factors"]
  [PMID:25035403 "a chromatin immunoprecipitation ( ChIP ) assay showed an in vivo association of DELLAs with promoters of several genes, although DELLAs lack known DNA binding motifs"]
- DELLA structural similarity is to mammalian STAT proteins, not classic TFs.
  [PMID:25035403 "DELLAs localize in the nucleus and show structural similarities to mammalian STAT (for signal transducers and activators of transcription) proteins"]

## Domain architecture (UniProt)
- N-terminal DELLA domain (DELLA motif 28-32, LEXLE 50-54, VHYNP 73-77): GA/GID1 receiver domain.
  [PMID:17416730 "the DELLA domain functions as a receiver domain for activated GA receptors"]
- C-terminal GRAS domain (160-529; LRI, VHIID, LRII, PFYRE, SAW subdomains): protein interaction / repressor activity.

## Function / mechanism

- GAI represses GA responses; gai loss-of-function alone is near-WT but synergizes with rga.
  [PMID:11606552 "RGA and GAI have partially redundant functions in maintaining the repressive state of the GA-signaling pathway, but RGA plays a more dominant role than GAI"]
  [PMID:11606552 "the rga-24 and gai-t6 null mutations have a synergistic effect on plant growth"]
- Notably, in the rga gai double null, "seed germination and flower development defects were not restored" — GAI is not the principal DELLA for germination/floral development (RGL2/RGL1 dominate).
  [PMID:11606552 "However, seed germination and flower development defects were not restored"]
- Green revolution orthologues: GAI orthologues (wheat Rht, maize d8) are GA response modulators resembling nuclear TFs.
  [PMID:10421366 "These genes encode proteins that resemble nuclear transcription factors and contain an SH2-like domain"]
  Note: the "nuclear transcription factor" description here is a resemblance inference (1999), predating the finding that DELLAs lack a DNA-binding domain. The TAS/ISS GO:0003700 DNA-binding TF activity annotations derive from this older inference and are not supported by later mechanistic work.

### Dual transcriptional mechanism (key paper PMID:25035403)
- GAF1/IDD2 (and ENY/IDD1) are DNA-binding IDD-family TFs; GAI binds the GAF1 PAM/SAW region and acts as a **coactivator** of GAF1 at GA feedback genes (e.g. GA20OX2).
  [PMID:25035403 "DELLAs and TOPLESS-RELATED (TPR) act as coactivators and a corepressor of GAF1, respectively"]
  [PMID:25035403 "DELLAs promote the transcription of genes encoding GA biosynthetic enzymes and GA receptors as coactivators of a DNA binding transcription factor, GAF1"]
- GA degrades DELLAs → converts GAF1-DELLA activator to GAF1-TPR repressor; this is the mechanism for GA homeostasis / feedback.
  [PMID:25035403 "GA converts the GAF1 complex from transcriptional activator to repressor via the degradation of DELLAs"]
- DELLAs thus have dual roles: titration of activators (PIFs/BZR1) AND coactivation of GAF1.
  [PMID:25035403 "DELLAs turn on or off two sets of GA-regulated genes via dual functions, namely titration and coactivation"]
- Activity regulation: transcription activation repressed by GA(3) in presence of TPR4 (UniProt ACTIVITY REGULATION).

### Epidermal germination module (PMID:24989044)
- GAI (DELLA) interacts directly with HD-ZIP TFs ATML1 and PDF2; GA-driven DELLA loss releases ATML1/PDF2 to activate L1-box genes (LIP1) in epidermis, enhancing germination.
  [PMID:24989044 "DELLA proteins interact directly with ATML1 and its paralogue PDF2"]
  [PMID:24989044 "increased GA levels reduce DELLA protein abundance and release ATML1/PDF2 to activate L1 box gene expression, thus enhancing germination potential"]

### GID1 receptor interaction
- GA-GID1 binds the GAI DELLA domain (N-terminus); structural basis solved (2ZSH/2ZSI).
  [PMID:17416730 "the GAI DELLA domain alone can mediate GA-dependent GID1A interactions"]
  [PMID:16709201 "in vivo interaction in the presence of GA(4) between each AtGID1 and the Arabidopsis DELLA proteins"]
  [PMID:19037309 "the amino-terminal DELLA domain of GAI ... interacts with the DELLA domain containing DELLA, VHYNP and LExLE motifs"]
- GAI is unusual among DELLAs: not robustly destabilized by GA in some assays.
  [PMID:12492836 "GAI, like RGL1, is stable in response to GA treatment"]

### Other interactions / processes
- Prefoldin (PFD3/PFD5): GAI/DELLA sequesters prefoldin in nucleus in absence of GA, affecting tubulin folding / cortical microtubule organization.
  [PMID:23583555 "physical interaction between the nuclear-localized DELLA proteins and the prefoldin complex"]
- CONSTANS (CO): DELLA-CO interaction links GA and photoperiod flowering.
  [PMID:26801684 "DELLA proteins physically interact with CONSTANS (CO)"]
- ANAC106: DELLA-ANAC106 reciprocal negative feedback for GA homeostasis / male fertility.
  [PMID:40755058 "DELLA proteins physically interact with ANAC106 ... inhibiting its transcriptional activation capacity"]
- Meiotic cytokinesis / 2n pollen: rga gai double mutant shows defective male meiotic cytokinesis (RMA organization); GA/DELLA acts largely in somatic anther tissue.
  [PMID:27621423 "Similar defects in meiotic cell division and reproductive ploidy stability occur in Arabidopsis plants depleted of RGA and GAI"]
- Far-red / red light & germination: PIL5 (PIF1) directly binds GAI and RGA promoters and upregulates them in dark; phytochrome light signaling represses GAI/RGA transcription.
  [PMID:17449805 "PIL5 increases the expression of two GA repressor (DELLA) genes, GA-INSENSITIVE (GAI) and REPRESSOR OF GA1-3 (RGA/RGA1), in darkness"]
  Note: GO:0010218 (response to far red light) IEP for GAI reflects GAI being a transcriptional *target* of light/PIL5, i.e. its expression responds; this is a "response to" annotation supported by the data.
- Phloem RNA trafficking: GAI mRNA moves long-distance via phloem and affects leaf development (engineered dominant ΔDELLA-gai construct).
  [PMID:15773853 "Both engineered mutant gai transcripts were able to exit the scion phloem and traffic cell to cell into the shoot apex"]
- Nitrogen: GAI (RGA2) was originally cloned by complementation of a yeast gln3 gdh1 nitrogen-regulation mutant.
  [PMID:9237632 "isolated two Arabidopsis thaliana cDNAs by complementation of a yeast gln3 gdh1 strain that is affected in the regulation of nitrogen metabolism"]
  Note: this is a heterologous yeast complementation phenotype; GO:0006808 regulation of nitrogen utilization is weakly supported as a native Arabidopsis function — treat as non-core / over-annotation candidate.
- Secondary cell wall network (PMID:25533953): large Y1H gene regulatory network; GRAS family over-represented among TFs binding cell wall promoters. The GO:0000976 "transcription cis-regulatory region binding" IPI to GAI derives from a Y1H protein-DNA screen. DELLAs lack a DNA-binding domain, so a direct, sequence-specific cis-region binding by GAI is mechanistically questionable; Y1H positives for non-DNA-binding cofactors can occur via bridging. Treat as over-annotation / MODIFY away from direct DNA binding.

## GO annotation assessment summary
- Core MF: GAI has no catalytic/DNA-binding activity of its own; its molecular function is **transcription coactivator activity** (GO:0003713, IDA, PMID:25035403) exerted via protein-protein interactions, and adapter/co-regulator binding (GID1, IDD TFs, PIFs, prefoldin).
- Core BP: negative regulation of GA signaling (GO:0009938), GA homeostasis (GO:0010336), regulation of transcription/gene expression.
- Core CC: nucleus (GO:0005634), strongly supported (IDA multiple).
- GO:0003700 DNA-binding transcription factor activity (TAS/ISS x4): over-annotation; DELLAs lack a DNA-binding domain (see above). Recommend MARK_AS_OVER_ANNOTATED / MODIFY.
- Many GO:0005515 "protein binding" IPI: real interactions but uninformative as a core MF; KEEP_AS_NON_CORE.
