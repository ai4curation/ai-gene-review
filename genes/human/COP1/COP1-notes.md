# COP1 (RFWD2) review notes

UniProt: Q8NHY2 (COP1_HUMAN). HGNC:17440, gene symbol COP1 (synonyms RFWD2, RNF200, RING finger protein 200).
731 aa. EC 2.3.2.27. NCBITaxon:9606.

## Identity / domain architecture
- E3 ubiquitin-protein ligase COP1, the human homolog of the Arabidopsis "constitutive
  photomorphogenesis protein 1" (atCOP1) light-signaling regulator [PMID:12615916, PMID:12466024].
- Domain architecture (from UniProt Q8NHY2 feature table):
  - N-terminal RING-HC zinc finger (ZN_FING 136..174), C3HC4-type, mediating E3 ligase activity
    and zinc binding [file:human/COP1/COP1-uniprot.txt].
  - Coiled-coil (233..301) mediating homodimerization [file:human/COP1/COP1-uniprot.txt].
  - C-terminal 7-bladed WD40 beta-propeller (repeats ~419..729; domain 386-731) that is the
    substrate-recognition / adaptor module. The WD40 domain (386-731) is necessary and sufficient
    for TRIB1 binding [PMID:27041596 (UniProt-cited); file:human/COP1/COP1-uniprot.txt].
  - Crystal structures of the WD40 region alone and bound to a TRIB1 peptide: PDB 5HQG, 5IGQ.
- Belongs to the COP1 family (UniProt SIMILARITY).
- In the Proteostasis Network classification, COP1 is a Cul4A/Cul4B WD40 substrate adaptor /
  substrate-recognition subunit.

## Catalytic activity / mechanism
- RING-finger E3 ubiquitin-protein ligase: accepts ubiquitin from an E2 as a thioester and
  transfers it directly to substrate lysines (EC 2.3.2.27). Catalytic activity demonstrated in vitro
  in an autoubiquitination assay; RING mutations (C136A/C139A, C136S/C139S) abolish ligase function
  [PMID:12615916, PMID:19805145].
- COP1 homodimerizes via its coiled-coil [PMID:12466024; file:human/COP1/COP1-uniprot.txt].
- COP1 functions both as a stand-alone RING E3 and as the substrate-recognition subunit of a
  cullin-RING ligase (CRL4) module. In the DCX(DET1-COP1) complex (RBX1, DET1, DDB1, CUL4A, COP1),
  the catalytic RING is contributed by RBX1, not COP1; COP1 here acts as the substrate-recognition
  adaptor [PMID:14739464; file:human/COP1/COP1-uniprot.txt FUNCTION].
- Substrate selectivity is governed by the WD40 domain recognizing a degron motif
  (D/E)-(D/E)-x-x-x-V-P-(D/E) in substrates; phosphorylation can create or destroy degrons
  [PMID:25117710, PMID:27041596].
- Activity/substrate choice regulated by pseudokinase adaptors TRIB1/TRIB2, which bind the WD40
  domain and compete with substrates (TRIB1 competes with substrates for COP1 binding); TRIB1
  recruits non-canonical substrates such as C/EBPalpha (CEBPA) [PMID:27041596 (UniProt-cited),
  PMID:20410507 (UniProt-cited); file:human/COP1/COP1-uniprot.txt ACTIVITY REGULATION].

## Substrates (ubiquitination -> proteasomal degradation)
- c-Jun / JUN (and JUNB, JUND family) [PMID:12615916, PMID:14739464]. In PMID:12615916, COP1
  bound Jun factors and repressed AP-1 transcription; in the early study the repression was seen
  without a change in c-Jun levels, but PMID:14739464 established COP1 (with DET1/DDB1/CUL4A/RBX1)
  drives c-Jun ubiquitination and degradation.
- p53 / TP53: COP1 directly ubiquitinates p53 and targets it for proteasomal degradation
  independently of MDM2 or PIRH2/RCHY1, repressing p53-dependent transcription and apoptosis.
  COP1 is itself a p53-inducible gene (negative feedback) [PMID:15103385]. RING mutants C136A/C139A
  abolish p53 ubiquitination [file:human/COP1/COP1-uniprot.txt MUTAGEN].
- p53 stability is co-regulated by MTA1 [PMID:19837670 (UniProt-cited)].
- MTA1: COP1 ubiquitinates MTA1 for proteasomal degradation; MTA1 reciprocally destabilizes COP1 by
  promoting its autoubiquitination, forming a feedback loop. Ionizing radiation disrupts
  COP1-mediated MTA1 proteolysis, stabilizing MTA1 [PMID:19805145].
- ETS transcription factors ETV1, ETV4, ETV5 (and ETS2): COP1 ubiquitinates and degrades these
  proto-oncogenic ETS factors; this underlies its tumor-suppressor role in prostate cancer.
  TMPRSS2:ETV1 fusions delete the COP1 degron, escaping degradation [PMID:21572435].
- ETS1: COP1 recognizes a phospho-degron; Src/Yes-family-kinase phosphorylation of Tyr283 blocks
  COP1 binding and stabilizes ETS1 [PMID:25117710].
- 14-3-3 sigma / SFN: COP1 is an E3 ligase for 14-3-3sigma; degradation activates AKT and promotes
  survival. CSN6 (COPS6) stabilizes COP1 by reducing its autoubiquitination [PMID:21625211].
- ACC1 / ACACA (acetyl-CoA carboxylase 1): COP1 ubiquitinates ACC1; KIF12 enhances COP1-mediated
  ACC1 ubiquitination/turnover, suppressing lipogenesis (relevant to MASH). Loss of this turnover
  promotes steatohepatitis [PMID:39920308]. This is the basis for the IMP annotation to
  "negative regulation of fatty acid biosynthetic process" (GO:0045717).
- Additional reported substrates (literature/UniProt, not all in GOA): C/EBPalpha (CEBPA, via TRIB1),
  FOXO1, TORC2/CRTC2, acetyl-CoA carboxylase [PMID:25117710 intro review].

## Regulation / autoubiquitination
- COP1 autoubiquitinates and turns over by the proteasome (Reactome "Autodegradation of the E3
  ubiquitin ligase COP1", R-HSA-349425) [file:human/COP1/COP1-uniprot.txt PTM].
- COPS6/CSN6 (COP9 signalosome subunit 6) binds COP1, reduces self-ubiquitination, stabilizes it
  [PMID:21625211].
- DNA damage: ATM phosphorylates COP1 at Ser387; 14-3-3sigma binds phospho-Ser387 COP1 and drives
  its nuclear export and enhanced (auto)ubiquitination, relieving COP1 repression of p53
  [PMID:20843328; Reactome R-HSA-349444, R-HSA-264418].
- COP9 signalosome deneddylates the nuclear CRL4 complex (Reactome neddylation/deneddylation cycle).

## Subcellular localization
- Nucleus (nuclear speckles) and cytoplasm; shuttles between the two. NLS motifs (109-113, 195-206)
  and an NES (235-245). The RING also acts as a structural scaffold mimicking a bipartite NLS
  [file:human/COP1/COP1-uniprot.txt SUBCELLULAR LOCATION, DOMAIN, MOTIF].
- Reactome models place COP1/CRL4 activity in cytosol and nucleoplasm.
- The Golgi membrane IEA annotation (GO:0000139) is an Ensembl Compara ortholog transfer from a rat
  protein; not supported by the human literature, which describes nuclear-speckle and cytoplasmic
  localization. Likely an over-annotation.

## Isoforms
- 5 isoforms. Isoform 4 (COP1D) is a dominant-negative that heterodimerizes with isoform 1 and
  blocks association with DET1, stabilizing UV-stress-induced c-Jun [PMID:17968316 (UniProt-cited)].
- Isoform 2 (delta24) does not interact with CUL4A but still binds RBX1.

## Disease / physiology
- Tumor suppressor in prostate (ETV1/ETS axis), and Cop1 deletion in mice causes lymphoma; combined
  with Pten loss promotes invasive prostate cancer [PMID:21572435, PMID:25117710 intro].
- Lipogenic enzyme turnover / MASH via ACC1 [PMID:39920308].

## Annotation review reasoning summary
- Strong, well-supported core: RING-type ubiquitin-protein ligase activity (GO:0061630 /
  GO:0004842), protein ubiquitination (GO:0016567), proteasome-mediated ubiquitin-dependent
  protein catabolic process (GO:0043161), positive regulation of proteasomal degradation
  (GO:0032436), and membership of the Cul4A-RING E3 ligase complex (GO:0031464). All ACCEPT.
- Substrate-recognition adaptor function (WD40 propeller) is a candidate core MF not currently
  captured: GO:1990756 (ubiquitin-like ligase-substrate adaptor activity) — proposed new term.
- The 9 generic "protein binding" (GO:0005515, IPI) annotations are uninformative per curation
  guidelines; most are interactions with substrates (SFN, ETV1/ETV5, ETS1/ETS2) or regulators
  (COPS6). MARK_AS_OVER_ANNOTATED (binding itself is real but the term is uninformative).
- Localization: nuclear speck (GO:0016607), cytoplasm (GO:0005737), cytosol (GO:0005829),
  nucleoplasm (GO:0005654) are all supported. Golgi membrane (GO:0000139, IEA from rat ortholog)
  is unsupported -> MARK_AS_OVER_ANNOTATED.
- GO:0045717 (neg. reg. fatty acid biosynthesis) supported by PMID:39920308 (ACC1) — KEEP_AS_NON_CORE
  (downstream physiological consequence of catalytic activity, not the core MF).
- GO:0010212 (response to ionizing radiation) supported by PMID:19805145 — KEEP_AS_NON_CORE.

## Review completion (2026-06-07)
- Completed COP1-ai-review.yaml (status COMPLETE). All 40 existing_annotations reviewed.
- ACCEPT (core): GO:0061630 (EXP/IMP/IEA ubiquitin protein ligase activity), GO:0004842
  (ubiquitin-protein transferase activity), GO:0016567 (protein ubiquitination), GO:0043161
  (proteasome-mediated ubiquitin-dependent protein catabolic process, IBA+IMP), GO:0006511,
  GO:0032436 (positive regulation of proteasomal catabolism), GO:0031464 (Cul4A-RING E3
  ligase complex), GO:0016607 (nuclear speck), GO:0005737 is_active_in cytoplasm (IC).
- KEEP_AS_NON_CORE: GO:0005737 located_in cytoplasm (IEA), GO:0005829 cytosol (TAS x3),
  GO:0005654 nucleoplasm (TAS x8), GO:0045717 (neg reg fatty acid biosynthesis, ACC1),
  GO:0010212 (response to ionizing radiation).
- MARK_AS_OVER_ANNOTATED: all 9 bare GO:0005515 protein binding (IPI) annotations.
- REMOVE: GO:0000139 Golgi membrane (IEA Ensembl Compara from rat ortholog; unsupported in human).
- Proposed (core_functions, not added to existing as NEW): GO:1990756 ubiquitin-like
  ligase-substrate adaptor activity (WD40 substrate-recognition adaptor function).
- proposed_new_terms: [] (GO:1990756 already exists and is used in core_functions).
- Validation: ✓ Valid (3 advisory warnings: cytoplasm action consistency across qualifiers;
  novel adaptor MF and cytosol location not in existing block).
