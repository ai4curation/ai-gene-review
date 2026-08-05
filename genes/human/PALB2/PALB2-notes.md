# PALB2 (Q86YC2) review notes

PALB2 = Partner And Localizer of BRCA2 / FANCN. Human, 1186 aa, chr16. Tumor suppressor;
biallelic loss = Fanconi anemia group N (FANCN); monoallelic = breast/pancreatic/ovarian
cancer predisposition.

## Domain architecture (from UniProt Q86YC2)
- N-terminal coiled-coil (res ~9-41): binds BRCA1; also mediates self-oligomerization.
- N-terminal region 1-579: DNA-binding domain (preference D-loop > dsDNA > ssDNA).
- RAD51 interaction region ~101-184 (mapped in PMID:20871616).
- ChAM (chromatin-association motif, ~395-446): intrinsic chromatin/nucleosome binding.
- C-terminal 7-bladed WD40 β-propeller (~853-1186): binds BRCA2 (pocket at WD4/WD5
  crossover), and also RAD51C, RAD51, XRCC3; also required for POLH interaction.

## Core biology (verified from cached publications)
- Scaffold/adaptor: PALB2 physically links BRCA1 (coiled-coil) to BRCA2 (WD40), forming the
  BRCA1-PALB2-BRCA2 complex required for HR. [PMID:19369211 "PALB2, the partner and localizer of BRCA2, binds directly to BRCA1, and serves as the molecular scaffold in the formation of the BRCA1-PALB2-BRCA2 complex"] and [PMID:19369211 "Our findings uncover PALB2 as the molecular adaptor between the BRCA proteins"].
- Localizes/stabilizes BRCA2. [PMID:16793542 "PALB2 colocalizes with BRCA2 in nuclear foci, promotes its localization and stability in key nuclear structures (e.g., chromatin and nuclear matrix), and enables its recombinational repair and checkpoint functions"].
- WD40 domain binds BRCA2 (structure). [PMID:19609323 "Localization of BRCA2 to nuclear foci requires its association with the partner and localizer of BRCA2 (PALB2)"] and structure of "PALB2 carboxy-terminal β-propeller domain in complex with a BRCA2 peptide".
- WD40 also directly binds RAD51C, RAD51, BRCA2, XRCC3; scaffolds an HR complex. [PMID:24141787 "the PALB2 WD40 domain can directly and independently bind RAD51C and BRCA2"] and [PMID:24141787 "the PALB2 WD40 domain may scaffold the RAD51C, RAD51, and BRCA2 HR proteins into a complex"].
- Chromatin association + oligomerization anchor BRCA2·RAD51 at breaks. [PMID:19423707 "PALB2 exists as homo-oligomers and that PALB2 oligomerization is essential for its focal accumulation at DNA breaks in vivo"] and [PMID:19423707 "PALB2 localizes to chromatin and assembled as oligomers at the site of DNA damage, which then serves as an anchor for the loading of BRCA2 and RAD51"].
- DNA binding: N-terminal half binds DNA, D-loop > dsDNA > ssDNA. [PMID:20871616 "Full length PALB2 bound all three species of DNA with the following preference: D-loop > dsDNA > ssDNA"].
- Stimulates RAD51 recombinase / D-loop formation, cooperates with RAD51AP1. [PMID:20871616 "although PALB2 alone stimulates D-loop formation, it has a cooperative effect with RAD51AP1"] and [PMID:20871616 "PALB2 binds DNA and physically interacts with RAD51"].
- N-DBD has intrinsic strand-exchange activity; DNA binding needed for RAD51 foci/HDR. [PMID:31017574 "We identified a major DNA-binding site of PALB2, mutations in which reduce RAD51 foci formation and the overall HDR efficiency in cells by 50%"] and [PMID:31017574 "it possesses the strand exchange activity without RAD51"].
- Strand-exchange/DBD is intrinsically disordered; coiled-coil dimerization + ssDNA-driven tetramerization; scaffold linking BRCA1-BRCA2-RAD51. [PMID:39584160 "The partner and localizer of BRCA2 (PALB2) is a scaffold protein linking BRCA1 with BRCA2 and RAD51 during homologous recombination (HR)"] and [PMID:39584160 "Single-stranded (ss)DNA binding promotes additional structural compaction and protein tetramerization"].
- With BRCA2 stimulates POLH DNA synthesis at blocked forks. [PMID:24485656 "PALB2 and BRCA2 interact with Polη and are required to sustain the recruitment of Polη at blocked replication forks"].
- Part of an ERCC5/XPG-BRCA2-PALB2-DSS1-RAD51 HR complex. [PMID:26833090 "XPG directly interacts with BRCA2, RAD51, and PALB2, and XPG depletion reduces their chromatin binding and subsequent RAD51 foci formation"].
- BRCA1-PALB2 interaction directs HR vs SSA choice. [PMID:28398198 "the BRCA1-PALB2 interaction dictates the choice between HR and SSA"] and [PMID:28319063 "The two BRCA proteins are linked by a third tumor suppressor, PALB2, in the HR pathway"].
- MRG15/MORF4L1 binds PALB2 (chromatin targeting). [PMID:20332121 "PALB2 binds directly to a conserved chromodomain protein, MRG15"].

## Review decisions summary
- Core molecular function best captured as molecular adaptor activity (GO:0060090):
  PALB2 bridges BRCA1 and BRCA2 (and scaffolds RAD51C/RAD51/XRCC3) for HR. Uninformative
  "protein binding" (GO:0005515) IPI rows to BRCA1/BRCA2 MODIFIED -> GO:0060090; the many
  other IPI rows (RAD51, RAD51C, XRCC3, RAD51AP1, MORF4L1, POLH, KEAP1, XPG, high-throughput
  interactome papers) MARKED_AS_OVER_ANNOTATED (real interactions but uninformative term;
  informative role captured in core_functions).
- Genuine DNA binding (GO:0003677), ssDNA binding (GO:0003697), homodimerization
  (GO:0042803), homotetramerization (GO:0051289) accepted (experimental).
- HR (GO:0000724) accepted across IBA/IEA/IDA/IMP. Nucleoplasm/nucleus accepted; nuclear
  speck (HPA IDA) kept as non-core.
- KEAP1 interaction (KEAP1-NRF2 oxidative-stress) is a secondary role, not the HR-scaffold
  core function; over-annotated as protein binding.
</content>
