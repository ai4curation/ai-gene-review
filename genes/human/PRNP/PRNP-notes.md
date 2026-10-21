# PRNP (human, P04156) curation notes

Deep research providers were unavailable in this environment (`just deep-research-falcon human PRNP
--fallback perplexity-lite` failed: "Provider 'perplexity' not available"). Research below is from
the cached publications, the UniProt record and the cached Reactome entry.

## Localization
- GPI-anchored to the outer leaflet of the plasma membrane: UniProt `SUBCELLULAR LOCATION: Cell
  membrane; Lipid-anchor, GPI-anchor {ECO:0000269|PubMed:19936054}`; Golgi by similarity to mouse.
- [PMID:18419754 "The cellular prion protein (PrP(c)) is a glycosyl-phosphatidylinositol
  (GPI)-anchored protein trafficking in the secretory and endocytic pathway and localized mainly at
  the plasma membrane."] — ER/Golgi are biosynthetic transit compartments.
- Raft residence and copper-driven exit: [PMID:16254249 "Copper caused PrP(C) to move laterally out
  of detergent-insoluble lipid rafts into detergent-soluble regions of the plasma membrane."]
- Cytosol annotations trace to mislocalized PrP quality control: [Reactome:R-HSA-9617595
  "inappropriately localized proteins such as cytosolic PRNP (PrP) (Leznicki and High 2012), which is
  normally located in the plasma membrane"]. Reviewed as over-annotation, as are lamin binding and
  generic cytoplasm.
- Conclusion for the benchmark: cell-surface accessible, entire mature chain extracellular.

## Core biochemistry
- Octarepeat Cu(2+) binding, atomic structure: [PMID:11900542 "The crystal structure of HGGGW in a
  complex with Cu2+ reveals equatorial coordination by the histidine imidazole, two deprotonated
  glycine amides, and a glycine carbonyl"].
- Amyloid-beta oligomer receptor: [PMID:19242475 "Here we identify the cellular prion protein
  (PrP(C)) as an amyloid-beta-oligomer receptor by expression cloning."]; Fyn coupling
  [PMID:22820466 "Aβ-PrP(C) interaction leads to Fyn kinase activation"]; co-receptors mGluR5
  [PMID:24012003 "PrP(C) and mGluR5 interact physically"] and LRP1 [PMID:23386614 "The cell surface
  binding, internalization, and downstream toxicity of Aβ oligomers was dependent on the
  transmembrane low density lipoprotein receptor-related protein-1 (LRP1)."].
- Phase separation / condensate scaffold: [PMID:30401430 "Here, we show that PrPC separates as a
  liquid phase"].
- BACE1 inhibition: [PMID:23386614 "PrPC lowered Aβ production through the inhibition of BACE1"].

## Review decisions
- Generic `GO:0005515 protein binding` rows removed per the project protein-binding policy.
- Large block of Ensembl-Compara IEA / ISS rows describing rodent knockout phenotypes (cytokine
  production, vascular smooth muscle, placenta, mitochondrion organization, ferroptosis, TRAIL) were
  marked over-annotated: these are indirect organismal phenotypes, not steps PrP(C) executes.
- `GO:0038023 signaling receptor activity` marked over-annotated: a GPI-anchored protein requires
  transmembrane co-receptors to signal; the informative activity is amyloid-beta binding.
- `GO:0016020 membrane` and `GO:0019898 extrinsic component of membrane` modified to
  `GO:0009897 external side of plasma membrane`; `GO:0046872 metal ion binding` modified to
  `GO:0005507 copper ion binding`.
- `GO:1903136 cuprous ion binding` left UNDECIDED: the cited study used Cu(2+).
