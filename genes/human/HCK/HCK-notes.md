# HCK notes

Deep research providers unavailable in this environment; research from UniProt (P08631),
cached publications, and Reactome.

## Identity
- HCK (hematopoietic cell kinase): non-receptor Src-family protein tyrosine kinase, expressed
  predominantly in myeloid/phagocytic and B-lymphoid hematopoietic cells [PMID:3496523
  "HCK (hemopoietic cell kinase) because its expression is prominent in the lymphoid and myeloid
  lineages of hemopoiesis"].
- Two isoforms from alternative translation initiation: p59Hck and p61Hck, with distinct
  localizations [PMID:15998323 "two isoforms, p59Hck and p61Hck, present at the plasma membrane
  and lysosomes, respectively"]. Myristoylated and differentially palmitoylated (Cys-3).
- SH3-SH2-kinase architecture with autoinhibition; Tyr-411 autophosphorylation activates,
  C-terminal Tyr-522 phosphorylation (by CSK) inhibits (UniProt).

## Localization (cell-surface benchmark)
- INTRACELLULAR / membrane inner leaflet. HCK is lipid-anchored (myristoyl/palmitoyl) to the
  cytoplasmic face of membranes, not an ecto-domain cell-surface protein.
- [PMID:11904303 IMP] p59Hck at the cytoplasmic side of the plasma membrane and focal adhesions;
  p61Hck on lysosomes/azurophil granules. [PMID:7791757 "p59hck is entirely associated with
  cellular membranes, including the organelles known as caveolae"].
- Conclusion: plasma-membrane inner leaflet (cytoplasmic side) plus caveolae, lysosomes, cytosol,
  Golgi, vesicles. No extracellular domain.

## Function
- Core: non-membrane-spanning (Src-family) protein tyrosine kinase [PMID:10092522 "Hematopoietic
  cell kinase (Hck) is a member of the Src-family of protein tyrosine kinases"].
- Transmits signals downstream of Fc receptors, integrins and cytokine receptors; phosphorylates
  CBL, VAV1, WAS etc. (UniProt). Drives phagocytosis, secretory-lysosome mobilization,
  degranulation and NADPH-oxidase respiratory burst (UniProt).
- Reorganizes the actin cytoskeleton and drives podosome/protrusion formation [PMID:11904303
  "triggered reorganization of the actin cytoskeleton"; PMID:15998323 podosome rosettes].
- SH2 domain binds phosphotyrosine [PMID:20624904]; SH3 domain binds TP73, inhibiting
  TP73-mediated apoptosis [PMID:17535448] (UniProt "Inhibits TP73-mediated ... apoptosis").

## Notable curation calls
- GO:0007498 mesoderm development (TAS PMID:3453117): the cited paper is the hck gene
  characterization (hematopoietic expression); mesoderm development is an indirect
  over-annotation -> MARK_AS_OVER_ANNOTATED.
- GO:0005515 bare protein binding (many IPI): REMOVE per protein-binding policy; informative
  binding captured by phosphotyrosine residue binding and signaling receptor binding.
