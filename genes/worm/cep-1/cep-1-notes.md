# cep-1 notes

## 2026-09-30

- Completed the worm cep-1 review as the final C. elegans CED-pathway comparator
  in the APOPTOSIS slice. CEP-1 was curated as the nuclear p53-family
  sequence-specific transcription activator that induces `egl-1` and `ced-13`
  BH3-only transcription after genotoxic stress, engaging the
  CED-9/CED-4/CED-3 intrinsic apoptosis module. The core DNA-damage branch is
  supported by the original cep-1 germline-apoptosis paper [PMID:11696333],
  the HUS-1/egl-1 checkpoint paper [PMID:12445383], the ced-13 induction paper
  [PMID:15605074], UV-C and genome-wide transcriptional profiling studies
  [PMID:17347667; PMID:18627611], and PRMT-5/CBP-1 modulation of
  CEP-1-dependent `egl-1` induction [PMID:19521535].
- Tightened generic transcription rows. `GO:0003677 DNA binding`,
  `GO:0003700 DNA-binding transcription factor activity`, and broad
  `GO:0006355 regulation of DNA-templated transcription` rows were moved toward
  `GO:0001228 DNA-binding transcription activator activity, RNA polymerase
  II-specific` or `GO:0045944 positive regulation of transcription by RNA
  polymerase II`, using the CEP-1 p53 response-element evidence from the DNA
  binding-domain and `fasn-1` target-gene studies [PMID:15242600;
  PMID:16582625].
- Kept the PRMT-5/CBP-1 transcription repressor complex as a real but non-core
  regulatory assembly, kept ER-stress/IRE-1-triggered p53-mediated germline
  apoptosis as a non-DNA-damage branch, and retained hypoxia, starvation,
  lifespan, and meiotic chromosome-segregation rows as non-core stress or
  genome-quality phenotypes rather than direct apoptotic outputs.
- Marked the SMG-1 paraquat row to `GO:0006979 response to oxidative stress`
  as over-annotated for CEP-1: smg-1 inactivation produces cep-1-dependent
  oxidative-stress resistance, but the experiment is an endpoint epistasis
  assay and does not show that CEP-1 itself directly executes an oxidative
  stress response [PMID:18836529].
- Left four rows unresolved pending full-text or structural evidence: the old
  RAD-51 IGI apoptosis row from an abstract-only rad-51 paper
  [PMID:12684824], the two zinc-binding rows whose direct seeded paper concerns
  the C-terminal oligomerization/SAM domain [PMID:17581633], and the old
  nucleolus localization row from the abstract-only founding CEP-1 paper
  [PMID:11557844].
