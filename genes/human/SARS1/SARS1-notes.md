# SARS1 (P49591) curation notes

## Sources consulted

- No deep-research provider file was present for SARS1 in this worktree, and none was
  generated for this pass. The review is built from the UniProt record
  (`SARS1-uniprot.txt`), the cached publications for every PMID in the GOA file, and the
  two cached Reactome reactions. Abstract-only papers (cached `full_text_available: false`):
  PMID:9431993, PMID:28236339, PMID:28655767, PMID:32814053, PMID:34570399, PMID:20458337.
- GO term status checked against QuickGO (2026-11-11): GO:0006434 seryl-tRNA
  aminoacylation is obsolete, `replaced_by` GO:0006418 tRNA aminoacylation for protein
  translation. GO:0098619 selenocysteine-tRNA ligase activity is defined as
  "tRNASec + L-Ser + ATP = Ser-tRNASec + AMP + diphosphate" and is a sibling of
  GO:0004828 (both is_a GO:0004812), not a child.
- `just paint-losses human SARS1`: no IRD/IKR loss on the lineage.

## Biology summary (with provenance)

- Canonical function: cytoplasmic class II seryl-tRNA synthetase, two-step reaction
  (Ser-AMP formation, transfer to tRNA(Ser)). [UniProt CC FUNCTION; PMID:9431993 "In
  functional studies, the enzyme aminoacylates calf liver tRNA and prokaryotic E. coli
  tRNA."] Kinetics with tRNASer and structure with Ser-SA [PMID:24095058 "on the overall
  aminoacylation activity of human SerRS as measured by the incorporation of serine onto
  tRNASer"]. Functional homodimer [PMID:22353712 "Three independent homodimers of SerRS
  were found in the asymmetric unit of the crystal"].
- tRNA(Sec) serylation, the first step of selenocysteine biosynthesis on its tRNA
  [PMID:26433229 "Here we present two cocrystal structures of human SerRS bound with
  tRNA(Sec)"; "dual substrate specificity of SerRS for both tRNASec and tRNASer"].
  Reactome R-HSA-2408526 places the SARS dimer at the start of Sec synthesis.
- Nuclear, vertebrate-specific moonlighting role: UNE-S C-terminal domain carries a
  bipartite NLS (482KKQKKQHEGSKKK494); ~10% of endogenous SerRS is nuclear in HUVEC and
  HEK293T [PMID:22353712]. Nuclear SerRS binds the VEGFA proximal promoter (DNase I
  footprint -62 to -38; Kd ~211 nM by EMSA), competes with c-Myc/MAX and recruits SIRT2 to
  deacetylate H4K16, repressing VEGFA transcription and restraining angiogenesis
  [PMID:24940000]. The zebrafish vascular phenotype is rescued by catalytically inactive
  but nuclear SerRS, and not by NLS-defective SerRS [PMID:22353712].
- Substrate-selection/activation factor for METTL6 (m3C32 on tRNASer): SerRS boosts METTL6
  activity ~1,000-fold independent of ATP/serine; cryo-EM of METTL6-SerRS-tRNASer
  [PMID:38918637; PMID:34268557; PMID:28655767].
- Disease: biallelic loss-of-function variants (D172N, R213L, others) cause NEDMAS;
  a de novo in-frame insertion causes dominant-negative complex spastic paraplegia with
  reduced serylation in patient fibroblasts [PMID:28236339; PMID:34570399; PMID:36041817].

## Judgement calls

- All six GO:0006434 rows: MODIFY to GO:0006418 (GO's own replaced_by; there is no
  serine-specific aminoacylation process term any more).
- GO:0004828 rows accepted consistently. The EXP row from PMID:26433229 rests on tRNA(Sec)
  serylation assays; that chemistry is GO:0098619, also accepted, but serine-tRNA ligase
  activity on tRNA(Ser) is independently established, so the row is kept rather than split.
- GO:0001887 selenium compound metabolic process (IEA, from mouse Sars IDA) MODIFY to
  GO:0016260 L-selenocysteine biosynthetic process; SARS1 performs the first step (tRNA(Sec)
  serylation). E. coli SerS carries GO:0016260 by IDA (EcoCyc), so this is the GO
  convention for the comparator in the same role. GO:0016260 is not an is_a descendant of
  GO:0001887 in the current ontology build, so this is a refinement in meaning rather than
  a strict descendant.
- GO:0001514 selenocysteine incorporation (IMP, PMID:34570399 abstract-only): kept as
  non-core. SARS1 catalyses the serylation step that the GO definition places within the
  Sec incorporation pathway ("Selenocysteine is synthesized from serine before its
  incorporation"), but decoding itself is done by EEFSEC/SECISBP2; consistent with the
  module, which uses SARS1 for the serylation annotation only.
- Cytoplasm rows MODIFY to cytosol (gene carries cytosol by IDA, HPA, IBA, Reactome).
- Bare protein-binding rows: REMOVE (Y2H screen PMID:32814053; METTL6 row, whose
  informative content is in GO:0060090 / GO:0043527 / GO:0106217). The self-interaction
  row from PMID:26433229 is MODIFY to GO:0042803 protein homodimerization activity.
- Exosome HDA rows: MARK_AS_OVER_ANNOTATED (abundant cytosolic enzyme in vesicle proteomics).
