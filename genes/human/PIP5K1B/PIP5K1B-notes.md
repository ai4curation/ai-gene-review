# PIP5K1B review notes

## Core function

PIP5K1B encodes phosphatidylinositol 4-phosphate 5-kinase type 1 beta. Its core
function is phosphorylation of PI4P to PI(4,5)P2/PIP2 at membranes. The original
human PIP5KI study identified PIP5KIbeta as a type I phosphatidylinositol-4-phosphate
5-kinase isoform and notes that PIP5Ks synthesize PI(4,5)P2, a key phosphoinositide
signaling precursor [PMID:8955136 "Type I phosphatidylinositol-4-phosphate 5-kinases are distinct members of this novel lipid kinase family."].
UniProt summarizes the same core activity as PI4P phosphorylation to form PI(4,5)P2
[file:human/PIP5K1B/PIP5K1B-uniprot.txt].

Reactome contains multiple PIP5K1B phosphoinositide reactions. The PI4P to PI(4,5)P2
reaction is the core physiological function. PI, PI3P, and PI(3,4)P2 phosphorylation
entries are useful biochemical/pathway context, but they should not replace the core
PI4P 5-kinase identity.

## Proteostasis network context

The Proteostasis Network places PIP5K1B under
`Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Regulation of autolysosome membrane composition`.
The PN mapping marks this group as `no_mapping` because the node is a broad taxonomy
container; that means PN membership alone should not be used as evidence. In this
case, however, the primary ALR paper provides a direct starting point: Rong et al.
report that clathrin and PI(4,5)P2 regulate ALR
[PMID:22885770 "Clathrin and phosphatidylinositol-4,5-bisphosphate regulate autophagic lysosome reformation."],
and the article page identifies Figure 3 as "PIP5K1B is required for the initiation
of ALR" [url:https://www.nature.com/articles/ncb2557].

Because GO appears not to contain a specific "autophagic lysosome reformation" process
term in the local term cache, the most defensible current term is broad
`GO:0007040 lysosome organization`, with a proposed new ALR-specific child term.
This is not inferred from the PN row alone; it is based on the Rong et al. ALR paper.

## Annotation decisions

- Accept `GO:0016308 1-phosphatidylinositol-4-phosphate 5-kinase activity` as the
  core molecular function.
- Accept phosphatidylinositol phosphate biosynthesis as the core process, and modify
  broader phosphatidylinositol metabolic/biosynthetic process annotations to this
  more specific process.
- Keep plasma membrane and endomembrane system as supported membrane contexts; keep
  cytosol as non-core because UniProt describes a cytosolic/membrane-associated enzyme.
- Keep PI, PI3P, and PI(3,4)P2 side-reaction annotations as non-core pathway context
  where Reactome explicitly assigns them, but treat the PI4P-to-PI(4,5)P2 reaction as
  the core catalytic function.
- Mark `protein binding` as over-annotated. The uropod paper supports EBP50/ERM
  interactions and localization, but generic GO:0005515 does not describe the
  informative function.
- Add a new broad `GO:0007040 lysosome organization` annotation for the ALR context,
  while also proposing a more specific `autophagic lysosome reformation` term.

## Deep research provenance

Falcon deep research was attempted with `just deep-research-falcon human PIP5K1B`, but
the provider timed out after 600 seconds and no `PIP5K1B-deep-research-falcon.md` file
was generated in the gene folder. This review therefore relies on cached GOA/UniProt,
cached publications, Reactome entries, PN mappings, the article page for PMID:22885770,
and these notes.
