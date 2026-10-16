# CFAP91 (MAATS1, AAT-1, C3orf15) review notes

## Deep research status

- `just deep-research human CFAP91 --provider falcon` failed: Edison API authentication
  error ("Failed to authenticate", HTTP 403 Forbidden).
- `just deep-research human CFAP91 --provider perplexity` failed: provider not available
  in this environment ("Provider 'perplexity' not available. Available: falcon, asta,
  openscientist").
- No deep-research file was written. Literature research was done manually (PubMed search
  for CFAP91 / MAATS1 / FAP91 / AAT-1) using the cached publications in `publications/`.

## Identity

- UniProt Q7Z4T9, Cilia- and flagella-associated protein 91; aliases MAATS1, AAT-1,
  C3orf15. CFAP91 family (PANTHER PTHR22455). Many isoforms from alternative promoters and
  splicing (AAT-1alpha/beta/gamma, AAT-1L/M/S).
- Disease: spermatogenic failure 51 (SPGF51, MIM:619177), autosomal recessive MMAF /
  astheno-teratozoospermia.

## Literature findings (with provenance)

### CSC and radial spoke base

- Chlamydomonas FAP91 was identified in the CaM-containing CSC; "FAP91 directly interacts
  with radial spoke protein 3 (an AKAP), which is located at the base of the spoke", and
  antibodies to FAP91 restored dynein activity in a sliding assay; "the CaM- and
  spoke-associated complex mediates regulatory signals between the radial spokes and
  dynein arms" [PMID:17967944].
- CSC knockdown: "the CSC is required for spoke assembly and wild-type motility"; RS2
  assembly defective [PMID:21613541].
- CSC cryo-ET: connects RS2, N-DRC and RS3S [PMID:22740634].
- Tetrahymena CFAP91 knockout: "lack of Tetrahymena Cfap91 protein affects stable
  docking/positioning of the radial spoke RS3 and the base of RS2, and adjacent inner
  dynein arms"; Cfap61/Cfap251 diminished; "CFAP91-KO cells swam about a hundred times
  slower than wild-type cells"; "Tetrahymena Cfap91 localizes at the base of radial spokes
  RS2 and RS3" [PMID:36552811] (abstract only).
- Human respiratory axoneme cryo-EM: CFAP91 "begins at the base of RS2, interacts with the
  N-DRC and then links the RS3 subunits CFAP251 and CFAP61" [PMID:37258679].

### Mouse and human sperm

- Martinez et al. 2020: six unrelated MMAF men with homozygous deleterious MAATS1
  variants; "severe central pair complex (CPC) and radial spokes defects"; WDR66 is "a
  physical and functional partner of CFAP91"; Trypanosoma TbCFAP91 is axonemal and its
  knockdown "impaired flagellar movement led to CPC defects" [PMID:32161152] (abstract
  only).
- Wang et al. 2025 (mouse): "Cfap91 knockout (KO) mice exhibit impaired sperm flagellum
  formation and male infertility"; CFAP91 co-immunoprecipitates with CFAP251 and LRRC23,
  which fail to localize in KO sperm flagella; authors "establish CFAP91 as an essential
  scaffolder of RS3 assembly" [PMID:40931011] (full text). Ependymal and tracheal cilia
  elongated normally in KO mice ("ciliary elongation was endurable in Cfap91-/- mice in
  contrast to disrupted sperm flagellum formation"); hydrocephalus was investigated in a
  susceptible background.
- CCDC113 interacts with CFAP91 and is needed for its distribution on doublet
  microtubules [PMID:39671309].

### Older AAT-1 work (somatic cells, overexpression)

- AAT-1 was cloned as an AMY-1 (MYCBP)-binding protein; "AAT-1alpha was found to bind to
  and be colocalized in mitochondria with AMY-1 in human HeLa and mouse GC-1 cells"; forms
  a complex with AKAP1 (S-AKAP84/AKAP149) and PKA RII; phosphorylated by PKA
  [PMID:12223483] (abstract only).
- Further isoforms: "AAT-1L and AAT-1M were found to be localized diffusely in the
  cytoplasm, AAT-1S, like AAT-1alpha, was found to be localized in the mitochondria-like
  structure" [PMID:15863901] (abstract only).
- These are the source of the cytoplasm and mitochondrion EXP rows. They concern specific
  isoforms in transfected somatic cell lines; the endogenous full-length protein in
  sperm and airway cilia is axonemal. AKAP1 is itself a mitochondrial AKAP, so a fraction
  of some isoforms could be mitochondrial, but this has not been shown for endogenous
  CFAP91 in germ cells.

## Curation judgements

- Cytoplasm (EXP x2, IEA): kept as non-core (isoform behaviour in transfected cells).
- Mitochondrion (EXP x2, IEA): marked as over-annotated; the claim (a mitochondrial
  protein) exceeds the evidence (overexpressed isoforms in HeLa/GC-1 cells).
- Protein binding (IPI, HuRI, DPY30): removed per protein-binding policy (no functional
  context; DPY30 interaction not otherwise supported).
- Spermatogenesis (IMP): MODIFY to `GO:0120316 sperm flagellum assembly`, the specific
  process the MMAF phenotype reports.
- Axonemal central apparatus assembly (IMP): CPC loss in patient sperm and Trypanosoma
  knockdown is a recurrent secondary feature of MMAF; CFAP91 is located on the doublets
  at the RS2/RS3 base, not in the central apparatus. Marked as over-annotated.
- Radial spoke stalk (colocalizes_with, ISS): MODIFY to `GO:0120341 radial spoke base 2` and
  `GO:0120342 radial spoke base 3`.
- NEW: `GO:0062177 radial spoke assembly` (comparator LRRC23, an RS3 subunit that CFAP91
  co-immunoprecipitates with, carries it by IMP/IBA); `GO:0005200 structural constituent of
  cytoskeleton` (consistent with the CFAP61 review).
