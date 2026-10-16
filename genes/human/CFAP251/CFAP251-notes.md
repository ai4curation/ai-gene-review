# CFAP251 (WDR66) review notes

## Deep research status

- `just deep-research human CFAP251 --provider falcon` failed: Edison API authentication
  error ("Failed to authenticate", HTTP 403 Forbidden).
- `just deep-research human CFAP251 --provider perplexity` failed: provider not available
  in this environment ("Provider 'perplexity' not available. Available: falcon, asta,
  openscientist").
- No deep-research file was written. The literature synthesis below was done manually
  from PubMed searches (CFAP251 / WDR66 / FAP251) and the cached publications in
  `publications/`.

## Identity

- UniProt Q8TBY9, Cilia- and flagella-associated protein 251; alias WDR66. WD40 repeat
  protein (14 WD repeats annotated in UniProt) with CFAP251_N and CFAP251_C Pfam domains;
  PANTHER PTHR13720:SF13. Chain d2 in the human respiratory axoneme cryo-EM model PDB 8J07.
- Disease: spermatogenic failure 33 (SPGF33, MIM:618152), autosomal recessive MMAF.

## Literature findings (with provenance)

### Position in the axoneme: calmodulin- and spoke-associated complex (CSC), radial spoke 3 base

- The CSC was found in Chlamydomonas by CaM immunoprecipitation; it "mediates regulatory
  signals between the radial spokes and dynein arms" [PMID:17967944].
- In Chlamydomonas the CSC "connects three major axonemal complexes involved in dynein
  regulation: RS2, the nexin-dynein regulatory complex (N-DRC), and RS3S" [PMID:22740634].
- Knockdown of CSC subunits in Chlamydomonas: "the CSC is required for spoke assembly and
  wild-type motility" [PMID:21613541].
- Tetrahymena: "loss of either FAP61 or FAP251 reduces cell swimming and affects the ciliary
  waveform and that RS3 is either missing or incomplete, whereas RS1 and RS2 are unaffected.
  Specifically, FAP251-null cilia lack an arch-like density at the RS3 base"
  [PMID:25694453] (abstract only in cache).
- Human respiratory-cilia cryo-EM: RS3 is "built on a base of CFAP61, CFAP91 and CFAP251",
  and CFAP91 "links the RS3 subunits CFAP251 and CFAP61" [PMID:37258679].
- Tetrahymena CFAP91 knockout: "the level of RS3-specific proteins, Cfap61 and Cfap251 ...
  are significantly diminished in Tetrahymena CFAP91-KO cells" [PMID:36552811].
- Mouse: "CFAP91 immunoprecipitates with RS3 proteins CFAP251 and LRRC23, whose localization
  is disrupted in Cfap91 KO sperm flagella" [PMID:40931011].

GO now has `GO:0120342 radial spoke base 3` (part_of radial spoke 3, axoneme). This is a
better fit than `radial spoke stalk` for the evidence above.

### Human genetics (sperm)

- Kherraf et al. 2018: homozygous SVA-mediated deletion removing the two penultimate exons
  of WDR66 in 7 of 78 MMAF subjects; Trypanosoma ortholog axonemal; reproducing the deletion
  "impaired flagellar movement" [PMID:30122540] (abstract only in cache).
- Auguste et al. 2018: bi-allelic loss-of-function WDR66 variants in three men with MMAF;
  "CFAP251 is normally located along the flagellum but is absent in men carrying WDR66
  mutations"; loss "affects the formation of the mitochondrial sheath"; authors "propose
  that CFAP251 plays a structural role during biogenesis of the spermatozoon flagellum in
  vertebrates" [PMID:30122541] (abstract only in cache).
- Li et al. 2019: biallelic CFAP251 loss-of-function in 3 of 65 Han Chinese MMAF men
  [PMID:30310178] (abstract only).
- Wang et al. 2022: CFAP251 splice variant (maternal UPD), reduced CFAP251 protein in
  sperm [PMID:35087568].

### Mouse knockout and respiratory cilia (2026)

- Liu et al. 2026: "The Cfap251 knockout mouse model replicated the MMAF and male
  infertility phenotypes observed in humans for the first time" [PMID:41943837].
- Respiratory cilia in KO mice: "TEM revealed a frequent absence of inner dynein arms
  within the axoneme" though no overt defect in ciliary length/density [PMID:41943837].
- "In the respiratory epithelium, CFAP251 was detected in the ciliary axoneme and
  cytoplasm" [PMID:41943837].
- The human "PCD-like" phenotype is symptomatic only; authors state the human data were
  "inferred solely from symptoms and chest CT findings rather than direct morphological
  evidence" [PMID:41943837]. Treat respiratory involvement in humans as unproven.
- Interactions with TUBB4B and SLC25A4 reported in the same paper; these are single-study
  findings and not used for GO annotation here.

## Curation judgements

- Core MF: no GO MF in GOA. Following the CFAP61 review in this repository (same
  complex), a non-enzymatic structural role in the axoneme is captured as
  `GO:0005200 structural constituent of cytoskeleton` (NEW). Note that comparator
  axonemal scaffolds (CFAP61, CCDC39, LRRC23) carry no MF in GOA beyond protein binding,
  so this is a judgement, flagged as a question.
- Core BP: `GO:0062177 radial spoke assembly` (NEW). Comparator check: LRRC23, an RS3
  component in the same structural role, carries this term (IMP, IBA) in human and mouse
  (QuickGO, 2026-10-16), as do RSPH4A/RSPH9. CFAP251 contributes structure (the arch-like
  density at the RS3 base) that RS3 assembly depends on [PMID:25694453].
- `GO:0120316 sperm flagellum assembly` was considered as NEW but not added: it has
  `GO:0030317 flagellated sperm motility` and `GO:0003341 cilium movement` among its GO
  ancestors, both of which CFAP251 already carries, so CLAUDE.md's rule against proposing
  descendants of carried terms applies. Raised as a suggested question.
- `radial spoke stalk` (colocalizes_with, ISS) -> MODIFY to `radial spoke base 3`.
- HPA sperm midpiece / end piece IDA: true sub-locations of a protein distributed along the
  whole flagellum; kept as non-core.
