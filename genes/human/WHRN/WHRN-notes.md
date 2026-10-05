# WHRN (whirlin, Q9P202) — research notes

Reviewer journal for the annotation review (2026-09-04, annotation-reviewer agent).

## Gene identity

- HGNC symbol WHRN (formerly DFNB31; KIAA1526), 9q32; UniProt Q9P202, 907 aa canonical.
- Multi-PDZ scaffold: HHD1/HNL1–PDZ1–PDZ2–HHD2/HNL2–proline-rich–PDZ3–C-terminal PDZ-binding
  motif (UniProt features; deep research: Mathur & Yang 2019, Hearing Research).
- Alternative promoters/splicing produce long (full-length), N-terminal, and short (C-terminal)
  isoforms. Long isoform carries PDZ1+PDZ2 (needed for USH2/ankle-link and retinal roles);
  short isoform retains HHD2–PDZ3–PBM (tip complex role).

## Two spatially/temporally distinct hair-cell roles

1. **Ankle-link / USH2 complex (long isoform, developing bundles, stereocilia base).**
   Quaternary complex WHRN–PDZD7–USH2A–ADGRV1(GPR98/VLGR1b):
   [PMID:25406310 "Importantly, both WHRN and PDZD7 are required for the complex formation
   with USH2A and GPR98."] and [PMID:25406310 "In this USH2 quaternary complex, WHRN prefers
   to bind to USH2A, whereas PDZD7 prefers to bind to GPR98. Interaction between WHRN and
   PDZD7 is the bridge between USH2A and GPR98."]. Localization:
   [PMID:25406310 "In hair cells, proteins encoded by the four genes are colocalized at the
   ankle link region of the mechanosensitive structure, the hair bundle, during development"].
   Founding interaction paper: [PMID:16434480 "we provide evidence that whirlin directly
   associates with USH2A isoform b and VLGR1b, two proteins that we previously reported to be
   part of the Usher protein interactome"]. Note the ankle link fiber itself (GO:0002141) is
   extracellular (USH2A/ADGRV1 ectodomains); whirlin belongs to the cytoplasmic ankle-link
   complex (GO:0002142) — basis for the MODIFY calls on GO:0002141.
   Recent mechanism (deep research, not in GOA refs): Wang et al. 2023 Nat Commun
   (10.1038/s41467-023-37267-5) — the four-protein assembly is a phase-separated condensate;
   WHRN A64D/R223H impair self-association and LLPS; high ADGRV1 dissolves the condensate,
   a plausible mechanism for ankle-link disappearance ~P12 in mouse.

2. **Stereocilia tip complex (short isoform, elongation).** WHRN–MYO15A–EPS8 tip complex
   controls stereocilia elongation; MYO15A delivers whirlin to tips (UniProt SUBUNIT).
   [PMID:16434480 "Whirlin is known to be essential for the elongation process of the
   stereocilia of sensory hair cells in the inner ear"]. CIB2 interacts with whirlin at tips:
   [PMID:23023331 "We show that CIB2 can multimerize and interacts with whirlin, which is
   localized at the tips of stereocilia"], though whirlin is not required for CIB2 tip
   localization [PMID:23023331 "in vivo, myosin VIIa and whirlin are not required for
   localization of CIB2 in mouse inner ear hair cell stereocilia"]. Lin et al. 2021 Cell Rep
   (10.1016/j.celrep.2021.108770; deep research) showed the tip complex phase-separates and
   condensation enhances EPS8-mediated F-actin bundling.

## Retina

- Periciliary membrane complex (PMC) at the inner segment apex, around the connecting cilium:
  [PMID:25406310 "In photoreceptors, USH2A, GPR98, and WHRN proteins are colocalized at the
  periciliary membrane complex of the inner segment apex and immediately below the outer
  segment"]; whirlin recruits its partners there:
  [PMID:25406310 "WHRN is able to recruit USH2A and GPR98 to the periciliary membrane complex"].
- Connecting cilium / OLM: [PMID:16434480 "we demonstrate that whirlin, USH2A and Vlgr1b
  co-localize at the connecting cilium and the outer limiting membrane of photoreceptor cells
  and in spiral ganglion neurons of the inner ear"].
- MPP1/p55 link to the Crumbs complex: [PMID:17584769 "We demonstrate that both proteins
  interact strongly by both a classical PDZ domain-to-PDZ binding motif (PBM) mechanism, and a
  mechanism involving internal epitopes."]; co-localization at
  [PMID:17584769 "the OLM, at the outer synaptic layer and at the basal bodies and the ciliary
  axoneme"] — supports basal body and synapse CC annotations (non-core).

## Human genetics (wild-type function inferred from patients)

- **USH2D** (long-isoform mutations → deafness + RP): [PMID:17171570 "We describe a novel
  genetic subtype for Usher syndrome, which we named USH2D and which is caused by mutations in
  whirlin."]; [PMID:17171570 "While mutations in the C-terminal half of whirlin have previously
  been reported in non-syndromic deafness (DFNB31), both alterations identified in our USH2
  family affect the long protein isoform."]; [PMID:17171570 "We propose that mutations causing
  Usher syndrome are probably restricted to exons 1-6 that are specific for the long isoform
  and probably crucial for retinal function."]
- **DFNB31** nonsyndromic deafness: C-terminal/3' variants disrupting tip-complex function
  (deep research: Mathur & Yang 2019; mouse whirler = short stereocilia, profound deafness,
  no retinal degeneration).
- Genotype–phenotype: isoform-position model is probabilistic, not absolute (deep research).

## Other reported sites/roles (non-core)

- Synapses of photoreceptors and OHCs: [PMID:16434480 "These proteins co-localize with whirlin
  at the synaptic regions of both photoreceptor cells and outer hair cells in the cochlea."]
- Developing brain expression: [PMID:16434480 "in embryonic development, the gene is not only
  expressed in the inner ear, but also in the developing brain and the retina"] — background
  for the Ensembl-transferred cerebellar Purkinje cell layer formation annotation (kept non-core).
- Paranodal junction maintenance (mouse; James Green 2013 thesis per deep research): paranodal
  decompaction/axonal swellings in Whrn-deficient mice, conduction largely normal — non-core.
- CASK: whirlin peptide (pSer685) binds CASK SH3-GK phospho-dependently
  [PMID:22117215 "we predicted a possible CASK SH3-GK-binding peptide sequence of whirlin,
  which is a reported binding target of CASK"].

## Curation decisions of note

- All bare GO:0005515 "protein binding" IPIs: none endorsed as-is. MODIFY → GO:0030674
  protein-macromolecule adaptor activity for the mechanistically central direct interactions
  (PMID:16434480 USH2A/ADGRV1; PMID:17584769 MPP1); MARK_AS_OVER_ANNOTATED for high-throughput
  or ligand-side evidence (PMID:12421765 KIAA Y2H; PMID:32296183 HuRI; PMID:36115835
  fragmentomics — source of >400 GOA lines; PMID:22117215 CASK; PMID:23023331 CIB2).
- GO:0042802 identical protein binding ACCEPTed: self-association is mechanistically core
  (homooligomers per UniProt; LLPS multivalency per Wang 2023/Lin 2021).
- GO:0002141 stereocilia ankle link (located_in/part_of; ISS+IEA) → MODIFY to GO:0002142:
  whirlin is in the cytoplasmic complex, not the extracellular link fiber.
- GO:0050910 detection of mechanical stimulus... → MARK_AS_OVER_ANNOTATED (whirlin acts
  upstream via stereocilium organization, not in the transduction event).
- GO:0060113 inner ear receptor cell differentiation (NAS) → MODIFY to GO:0060122 (the
  developmental role is specifically stereocilium organization).
- GO:0045184 establishment of protein localization (ISS) → MODIFY to GO:0072659 (whirlin
  recruits USH2A/ADGRV1 to specific plasma-membrane domains).
- GO:0005884 actin filament (IEA) → MARK_AS_OVER_ANNOTATED (localizes to actin-rich
  stereocilia, not an actin-filament component).
- Human IMPs from PMID:17171570 (retina homeostasis, sound, light) ACCEPTed — patient-based
  IMP is acceptable for wild-type function.
