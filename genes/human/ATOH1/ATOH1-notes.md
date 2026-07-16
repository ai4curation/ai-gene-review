# ATOH1 review notes

## 2026-07-14: evidence review and curation journal

### Inputs and review boundary

- Reviewed the 24 seeded human GOA annotations in `ATOH1-goa.tsv` against the
  reviewed UniProtKB record Q92858, the two GOA-cited publications, additional
  cached primary literature, and current GO definitions.
- The task context reports that both configured deep-research routes are
  globally quota-blocked (Falcon HTTP 402; Perplexity HTTP 401). These providers
  were not retried, and no provider-named deep-research file was created.
- This review distinguishes direct human evidence from conserved mammalian
  evidence. Much of the developmental causality comes from mouse, while the
  human protein's DNA-binding activity, human embryonic stem-cell-derived
  cerebellar lineage, and human cell-line intestinal phenotypes provide direct
  human support.

### Protein and molecular mechanism

- Human ATOH1 is a 354-aa basic helix-loop-helix transcription factor. UniProt
  places the bHLH domain at residues 159-211 and records no alternative protein
  isoforms. `[file:genes/human/ATOH1/ATOH1-uniprot.txt, "DOMAIN          159..211"; "bHLH"]`
- ATOH1 activates E-box-dependent transcription with TCF3/E47, and HES1
  antagonizes this activity. `[file:genes/human/ATOH1/ATOH1-uniprot.txt,
  "Activates E box-dependent transcription in collaboration with TCF3/E47, but the activity is completely antagonized by the negative regulator of neurogenesis HES1."]`
- Efficient DNA binding depends on bHLH dimerization, and the protein functions
  in the nucleus. `[file:genes/human/ATOH1/ATOH1-uniprot.txt,
  "Efficient DNA binding requires dimerization with another bHLH protein."]`
- A human methylation-sensitive SELEX study assayed 542 human transcription
  factors and is the source of the direct sequence-specific double-stranded DNA
  binding annotation. The cached paper text describes the systematic assay but
  does not expose the ATOH1-specific supplementary row; the annotation is
  nevertheless biologically concordant with the bHLH domain, E-box-binding IBA,
  and cis-regulatory DNA-binding orthology annotations. `[PMID:28473536,
  "By analysis of 542 human TFs with methylation-sensitive SELEX (systematic evolution of ligands by exponential enrichment)"]`

### Developmental roles

- The original cloning paper recovered the human ortholog and showed that the
  chicken and mouse orthologs are expressed in hindbrain progenitors predicted
  to form the external granule layer. Its conclusion about vertebrate CNS
  development is expression-based, not direct human loss-of-function evidence.
  `[PMID:8872459, "Here we report the cloning of atonal homologs from red flour beetle, puffer fish, chicken, mouse, and human."]`
  `[PMID:8872459, "Both the chicken and the mouse homologs are expressed early in embryogenesis in the hind brain, and specifically in cells predicted to give rise to the external granular layer of the cerebellum."]`
- In mouse cerebellum, reciprocal knock-in and electroporation experiments show
  that Atoh1 is sufficient to impose glutamatergic fates, including granule and
  deep cerebellar nuclear neurons, on ventricular-zone cells. This is the
  strongest causal support for the slide/module's rhombic-lip glutamatergic
  lineage node, but it remains mouse evidence. `[PMID:24695699,
  "ectopically Atoh1-expressing VZ cells produced glutamatergic neurons, including granule cells and deep cerebellar nuclei neurons"]`
- A postnatal mouse cerebellar targetome identified more than 600 direct Atoh1
  targets and a 10-nt Atoh1 E-box-associated motif, connecting DNA binding to
  migration, adhesion, and metabolic programs. `[PMID:21300888,
  "We used a multipronged approach to create a comprehensive, unbiased list of over 600 direct Atoh1 target genes in the postnatal cerebellum."]`
- A direct human developmental model derived the ATOH1 lineage from human
  pluripotent stem cells; derived cerebellar granule cells migrated along glial
  fibers and integrated after transplantation. `[PMID:34842137,
  "We report a rapid protocol for the derivation of the human ATOH1 lineage, the precursor of excitatory cerebellar neurons, from human pluripotent stem cells (hPSCs)."]`
- Inner-ear evidence is conserved mammalian evidence: an Atoh1-null comparison
  explicitly identifies the gene as essential for hair-cell differentiation.
  `[PMID:15846349, "a gene essential for hair cell differentiation"]`
- ATOH1 is also a major epithelial lineage determinant. Genetic disruption in
  mouse intestine and knockdown in colorectal cancer cells demonstrate a
  requirement for intestinal secretory-cell gene expression and differentiation.
  `[PMID:20621629, "The atonal homolog 1 (Atoh1) transcription factor is required for intestinal secretory (goblet, Paneth, enteroendocrine) cell differentiation."]`
  `[PMID:20621629, "ATOH1 was required for secretory cell gene expression in cell lines and in mice."]`

### Ontology checks and curation choices

- Current QuickGO definitions and labels were checked on 2026-07-14 for the
  authored core/replacement terms. In particular:
  - GO:0001228 — DNA-binding transcription activator activity, RNA polymerase
    II-specific.
  - GO:0045944 — positive regulation of transcription by RNA polymerase II.
  - GO:0021707 — cerebellar granule cell differentiation; its definition
    explicitly includes commitment to granule-cell fate.
  - GO:0060575 — intestinal epithelial cell differentiation.
- GO:0003700 is correct in essence but less informative than the activator term
  GO:0001228, so the legacy TAS annotation is `MODIFY` rather than removed.
- GO:0006366 describes transcription by RNA polymerase II itself. ATOH1
  regulates that process rather than performing polymerase transcription, so it
  is `MODIFY` to GO:0045944.
- GO:0048731 (system development) is true only at an unhelpfully broad level and
  is marked over-annotated because the record already contains specific neural
  and sensory developmental processes.
- Context-specific outcomes (sensory organ development, axon development,
  negative regulation of gliogenesis, and broad CNS development) are retained
  as non-core rather than rejected.
- No existing experimental annotation was removed. The ATOH1-specific row of
  the high-throughput SELEX dataset was not visible in the cached extraction,
  but the annotated activity is independently supported by the protein class
  and multiple convergent annotations; it was therefore accepted with an
  explicit evidence limitation rather than second-guessed.

### Remaining knowledge gaps

- Direct in-vivo causal evidence for many lineage effects in humans remains
  limited; mouse orthology should remain explicit whenever developmental
  mechanisms are discussed.
- The exact human target repertoire and partner usage can vary by lineage, even
  though E-box-directed transcription activation is conserved.
- The available GO vocabulary lacks a single term for the full ATOH1-dependent
  intestinal secretory-lineage program; GO:0060575 is a conservative parent
  process rather than an assertion that ATOH1 specifies every intestinal
  epithelial subtype.
