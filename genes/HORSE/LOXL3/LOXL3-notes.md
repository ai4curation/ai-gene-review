# LOXL3 (horse, A0A9L0TKN1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: horse partner of the DONKEY40 LOXL3 target (donkey A0A9L0K7N3); folder created
with `just fetch-gene HORSE A0A9L0TKN1 --alias LOXL3` (stub id confirmed A0A9L0TKN1).
ProtNLM2 output was not consulted.

Deep research: `just deep-research-falcon HORSE LOXL3 --fallback perplexity-lite` failed
(Edison API "Failed to authenticate"; perplexity-lite fallback also failed). No deep
research file exists; the review uses cached publications on the human and mouse orthologs.

### Identity

- A0A9L0TKN1 (unreviewed, PE 3) is a full-length LOXL3 gene model: 753 aa, the same
  length as human canonical P58215-1, gapless alignment at 95.6% identity
  (`LOXL3-bioinformatics/RESULTS.md`). Signal peptide 1..25, four SRCR domains, lysyl
  oxidase domain. Cu-binding His607/609/611 and LTQ Lys634/Tyr670 all conserved.
  Not a fragment or isoform.
- PANTHER PTHR45817:SF2 (LYSYL OXIDASE HOMOLOG 3), same subfamily as human P58215, mouse
  Q9Z175 and zebrafish loxl3a/loxl3b (`interpro/panther/PTHR45817/PTHR45817-entries.csv`).

### Evolutionary grounding

PAINT (`interpro/panther/PTHR45817/PTHR45817-paint.tsv`):
- PTN002550804 (family root, Bilateria): protein-lysine 6-oxidase activity, extracellular
  region; P58215 among seeds. Inherited by horse.
- PTN008698711 (Chordata): collagen fibril organization, extracellular matrix. Inherited.
- PTN002910812 (angiogenesis, seeded by LOXL2 + zebrafish) and PTN002910759
  (GO:0035791, seeded by LOX) were NOT propagated to horse LOXL3; treated as deliberate
  (those clades are LOXL2- and LOX-specific). No such terms added.

### Literature (orthologs)

- Human LOXL3 is secreted [PMID:11284725 "Recombinant LOXL3, expressed in HT-1080 cells, was secreted into the culture medium"].
- Amine oxidase activity on collagen/elastin for LOXL3 variants [PMID:17018530; PMID:28112368].
- Mouse Loxl3 KO: reduced collagen cross-links, cleft palate, spinal deformity [PMID:26307084 "In LOXL3-deficient mice, an obvious decrease in collagen cross-links was detected."].
- Mouse LoxL3 oxidizes fibronectin at the MTJ [PMID:26954549].
- Single study: nuclear SRCR-dependent STAT3 deacetylation, Th17/Treg phenotype [PMID:28065600]; treated as non-core.

### Decisions

- ACCEPT: GO:0004720 (IBA, IEA), GO:0005507, GO:0005576 (IBA, IEA), GO:0030199, GO:0031012.
- MODIFY: GO:0016641 -> GO:0004720.
- REMOVE: GO:0016020 membrane (SRCR InterPro2GO mapping; protein is secreted, no TM).
- KEEP_AS_NON_CORE: nucleus, cytoplasm, tissue development, animal organ development,
  negative regulation of Th17 lineage commitment.
- MARK_AS_OVER_ANNOTATED: elastic fiber.
- NEW: GO:0018057 peptidyl-lysine oxidation (ISS; the enzyme performs the step; human ortholog carries it).

### Relative

Closest characterised relative by phylogeny: human LOXL3 P58215 (same PANTHER subfamily
SF2, member of the PAINT seed set). Complete review exists at
`genes/human/LOXL3/LOXL3-ai-review.yaml`. No mouse Loxl3 review in repo. No PANTHER family
review (only entries/metadata/paint) under `interpro/panther/PTHR45817/`; no modules mention
LOXL3 or lysyl oxidase.
