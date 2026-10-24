# GATA4 (human, P43694) review notes

Automated deep research was unavailable for this run (falcon 402, OpenAI 401), so no
`-deep-research-<provider>.md` file exists. These notes were compiled manually from cached
publications in `publications/`, the UniProt record, and PubMed searches (E-utilities).

## Identity and domains
- GATA zinc-finger transcription factor, 442 aa; two GATA-type zinc fingers (UniProt ZN_FING 217-241
  N-terminal, 271-295 C-terminal), N-terminal transactivation domains, C-terminal NLS region.
- UniProt: "Transcriptional activator that binds to the consensus sequence 5'-AGATAG-3' and plays a key
  role in cardiac development and function". Nuclear.
- C-terminal finger = DNA recognition; N-terminal finger stabilises binding and binds FOG cofactors
  [PMID:21220346 "The C-terminal zinc finger region is required for the recognition and binding of DNA, and the N-terminal zinc finger region contributes to the stability of this binding"].

## Molecular function
- Sequence-specific Pol II cis-regulatory binding and activation: binds GATA element of AMH promoter
  (EMSA) and transactivates [PMID:21220346 "we performed EMSA, which showed WT GATA4 binding to the GATA4-responsive element on the AMH promoter"].
- Patient mutations reduce DNA binding and transcriptional activity [PMID:24000169 "the GATA4 mutants were consistently associated with diminished DNA-binding affinity and decreased transcriptional activity"];
  [PMID:12845333 "This mutation resulted in diminished DNA-binding affinity and transcriptional activity of Gata4"].
- Pioneer-like activity: GATA-4 binds sites in linker-histone-compacted nucleosome arrays and opens local
  chromatin without ATP-dependent remodelers [PMID:11864602 "HNF3 and GATA-4, but not NF-1, C/EBP, and GAL4-AH, bound their sites in compacted chromatin and opened the local nucleosomal domain in the absence of ATP-dependent enzymes"].
- Genome-wide: co-occupies cardiac enhancers with TBX5 in human iPSC-cardiomyocytes; G296S disrupts TBX5
  recruitment to super-enhancers; also required for repression of non-cardiac genes [PMID:27984724].

## Partner TFs and cofactors (combinatorial complexes)
- NKX2-5: mutual cofactors, physical interaction via GATA4 C-terminal finger + extension and NKX2-5
  homeodomain; synergistic activation of NPPA/ANF [PMID:9312027 "The synergy involves physical Nkx2-5-GATA-4 interaction, seen in vitro and in vivo, which maps to the C-terminal zinc finger of GATA-4 and a C-terminus extension"];
  [PMID:9584153 "Coimmunoprecipitation experiments demonstrate that Csx and GATA4 associate intracellularly"]. Consistent with the
  NKX2-5 (human) and Nkx2-5 (mouse) reviews, which use GO:0061629 for this binding.
- TBX5: [PMID:12845333 "the Gata4 mutation abrogated a physical interaction between Gata4 and TBX5"].
- SMAD4: co-SMAD binding; cooperative activation of Id2 in endocardial cushion [PMID:21330551].
- ZFPM2/FOG2 (N-terminal finger): required for heart and gonad development; Gata4 V217G knock-in
  (FOG-binding defective) gives DORV and valve defects [PMID:11297508] and gonad failure with low Sry [PMID:12223418].
- NR5A1/SF-1: synergistic activation of AMH [PMID:21220346].
- KLF13 [PMID:17053787]; HEY/HRT bHLH repressors bind GATA4 and inhibit it [PMID:15485867, PMID:16199874].
- BRD4, GLYR1, SMARCC1 from AP-MS interactome in cardiac progenitors [PMID:35182466].

## Biological roles
- Heart: Gata4-/- mouse embryos lack a ventral heart tube because of failed ventral folding, but
  cardiomyocytes do differentiate; GATA4 "is not essential for the specification of the cardiac cell lineages"
  [PMID:9136932]; [PMID:9136933 "generated two independent heart tubes that contained differentiated cardiomyocytes"].
  So "cardiac cell fate specification/commitment" should not be asserted strongly for mammalian GATA4
  (redundancy with GATA5/6). Myocardial Gata4 controls cardiomyocyte proliferation, RV and AV canal
  morphogenesis [PMID:15902305]. Dosage-sensitive: 70% reduction gives CAVC, DORV, hypoplastic myocardium
  [PMID:15464586]. Human heterozygous mutations: ASD, VSD, AVSD, TOF, BAV [PMID:12845333, PMID:24000169, PMID:29325903, PMID:21330551].
- Endoderm: foregut morphogenesis defect in null [PMID:9136932]; liver bud expansion and ventral pancreas require GATA4
  (liver effect likely non-cell-autonomous via septum transversum) [PMID:17451603]. Intestinal
  terminal differentiation (Xenopus/chick/human cell data) [PMID:9566909].
- Gonad: GATA4-FOG2 required for Sry expression and testis differentiation in mouse [PMID:12223418];
  human G221R (N-finger) mutation causes 46,XY DSD [PMID:21220346].

## Curation decisions summary
- Core: GO:0000981 / GO:0000978 / GO:0045944 in heart development (matches module annoton GO:0000981 in
  GO:0007507); partner-TF binding GO:0061629; testis development as second core role.
- Generic `protein binding` IPI rows -> MODIFY to GO:0061629 (TF partners) or GO:0001221 (FOG2; BRD4/GLYR1/SMARCC1).
- Response-to-X and stress/tissue-repair IEA rows from rodent orthologs -> mostly MARK_AS_OVER_ANNOTATED.
- PMID:20585342 (SNP association with acamprosate relapse) does not support "response to xenobiotic stimulus" -> REMOVE.
- PMID:28473536 methyl-SELEX: GATA4 not mentioned in cached text (supplementary data); accepted deferring to curator.
