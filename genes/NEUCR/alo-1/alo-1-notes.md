# NEUCR alo-1 notes

## 2026-10-10

- `just fetch-gene NEUCR alo-1` seeded 15 GOA rows for the PTHR43762
  sugar-lactone oxidase family. GO-Central places `GO:0003885
  D-arabinono-1,4-lactone oxidase activity` at `PANTHER:PTN000356435`
  from the SGD and CGD fungal ALO1 anchors, and places generic
  `GO:0005739 mitochondrion` at the Dikarya node
  `PANTHER:PTN001015900`.
- `just deep-research-falcon NEUCR alo-1` failed because `agentapi` is not
  installed and no supported deep-research provider key is present
  (`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, or
  `PERPLEXITY_API_KEY`).
- Web/PubMed searches for `"alo-1" "Neurospora crassa"
  D-arabinono-1,4-lactone oxidase`, `Q7SGY1 Neurospora ALO1`, and related
  terms did not find a newer paper assaying N. crassa alo-1 directly. The
  most recent relevant primary paper found was the 2022 M. oryzae MoAlo1
  paper, which includes the N. crassa protein in the conserved fungal ALO
  comparison and experimentally localizes the M. oryzae ortholog to
  mitochondria [PMID:35050012, "Sequence analysis using SMART showed that
  the ALO domain and FAD_binding_4 domains are also present in
  S. cerevisiae [15], C. albicans [16], Schizosaccharomyces pombe,
  Neurospora crassa, Fusarium oxysporum, Colletotrichum gloeosporioides,
  Ustilaginoidea virens, Brassica oleracea [25], Rattus norvegicus [26],
  and Mus musculus (Figure 1A)."].
- The direct N. crassa literature is at the metabolite level rather than at
  alo-1. Dumbrava and Pall identified erythroascorbic acid in N. crassa
  extracts [PMID:2825802, "UDPglucuronic acid and erythroascorbic acid
  were identified in extracts of the fungus Neurospora crassa."], supporting
  the plausibility of the fungal D-arabinono-1,4-lactone oxidase pathway in
  this organism but not a direct assay of Q7SGY1.
- The exact catalytic IBA is well grounded by direct S. cerevisiae and
  Candida ALO1 work: the S. cerevisiae paper purified the enzyme from the
  mitochondrial fraction, matched it to YML086C/ALO1, and showed that alo1
  mutants lose the enzyme activity and D-erythroascorbic acid
  [PMID:10094636, "In the alo1 mutants, D-erythroascorbic acid and the
  activity of D-arabinono-1,4-lactone oxidase could not be detected."];
  the C. albicans paper cloned ALO1 and reached the same null-mutant
  conclusion [PMID:11349062, "In the alo1/alo1 null mutants, the activity
  of D-arabinono-1,4-lactone oxidase was completely lost and
  D-erythroascorbic acid could not be detected."].
- UniProt's membrane placement for Q7SGY1 is only "mitochondrion
  membrane" by homology. The Ensembl Compara transfer of the cytoplasmic
  face of the mitochondrial outer membrane is an over-specific S. cerevisiae
  projection for this review unless a direct N. crassa localization paper
  appears.
- The Ensembl Compara `GO:0031489 myosin V binding` row should not be
  propagated to N. crassa alo-1. It is a protein-binding claim transferred
  from budding yeast and is not implied by the conserved sugar-lactone
  oxidase activity or by the PAINT mitochondrial placement.
- Added structured propagation reviews to the Ensembl Compara transfers:
  broad mitochondrion, oxidative-stress response, and
  D-erythroascorbate biosynthesis are safe transfers from S. cerevisiae, while
  the Myo2-binding row is a bad transfer and the two outer-membrane rows are
  over-specific for the available N. crassa ALO-1 evidence.
