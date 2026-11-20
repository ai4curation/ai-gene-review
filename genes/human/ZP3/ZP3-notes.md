# ZP3 notes

Deep research providers unavailable in this environment (falcon/perplexity-lite failed); research from
cached publications and the UniProt record.

## Function
- Egg-coat structural glycoprotein: polymers of ZP2 and ZP3 cross-linked by ZP1
  [file:human/ZP3/ZP3-uniprot.txt "Polymers of ZP2 and ZP3 organized into long filaments cross-"]; ZP-domain
  self-assembly [PMID:26879157].
- Sperm receptor and inducer of the acrosome reaction: recombinant ZP3 beads bind capacitated human sperm
  [PMID:19700799]; native ZP3 induces the acrosome reaction, glycosylation-dependent [PMID:18667750]; fragments
  bind the anterior sperm head and trigger acrosomal exocytosis [PMID:19246320]. Human ZP3 restores fertility in
  Zp3-null mice but does not confer human-sperm binding [PMID:9609824] — species specificity is not ZP3 alone.
- Binds proacrosin/acrosin [PMID:15950651]. Missense ZP3 mutation causes empty follicle syndrome / zona-less
  oocytes [PMID:28886344].

## Annotation issues
- A block of ISS immune-process terms (type IV hypersensitivity, humoral immune response, leukocyte migration,
  IFN-gamma, IL-4, T cell proliferation, inflammatory response, follicle development) derives from ZP3 peptide
  immunization (contraceptive vaccine / autoimmune oophoritis) models: ZP3 is the antigen, not an actor.
  Marked over-annotated.
- Two ISS transcription-regulation terms removed: ZP3 is a secreted glycoprotein, and the well-studied item is
  the oocyte-specific ZP3 *promoter*, a property of the gene, not the protein.

## Localization conclusion (surface benchmark)
Extracellular: mature ZP3 is the cleaved ectodomain incorporated into the **zona pellucida (egg coat)**, outside
the oocyte plasma membrane. The precursor is a single-pass type I membrane protein cleaved before the TM
[UniProt "Proteolytically cleaved before the transmembrane segment to yield"], so plasma-membrane rows are kept
as a precursor/trafficking location only, not as the functional site.
