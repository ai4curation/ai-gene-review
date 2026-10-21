# CEACAM5 (CEA) notes

Deep research providers unavailable in this environment; research from the 18 cached publications and
UniProt P06731.

## Topology / localization
- IgV domain + 3 IgC2 repeats, GPI-anchored: [PMID:3387431 "The COOH-terminal amino acid of
  carcinoembryonic antigen (CEA) is shown to covalently link with ethanolamine, evidence consistent with
  the anchorage of CEA to the plasma membrane through a phosphatidylinositol-glycan tail"].
  UniProt: "Cell membrane; Lipid-anchor, GPI-anchor; Extracellular side" and "Localized to the apical
  glycocalyx surface".
- Conclusion: plasma membrane, outer leaflet, whole mature protein extracellular; apical/glycocalyx in
  normal colonic epithelium [PMID:10436421], depolarized and overexpressed in carcinoma. Shed soluble
  form circulates (serum tumour marker); detected in exosomes.

## Functions
- Homophilic and heterophilic (e.g. CEACAM6) adhesion [PMID:2803308]; IgV-domain dimer in crystal
  [PMID:18086185]; subdomains mapped [PMID:10864933].
- Blocks myogenic differentiation when ectopically overexpressed; requires its own GPI anchor
  [PMID:10931872].
- Inhibits anoikis [PMID:10910050] and apoptosis [PMID:11448920].
- Pathogen receptor: E. coli Dr adhesins [PMID:18086185]; MERS-CoV attachment factor [PMID:27489282].

## Curation decisions
- GO:0034235 GPI anchor binding (IMP, PMID:10931872) REMOVEd with a source defect: the paper shows CEA's
  *own* GPI anchor carries the differentiation-blocking information, not that CEA binds GPI anchors.
- Protein-binding rows modified: CEACAM1 interactions -> cell adhesion molecule binding; MERS spike ->
  receptor-mediated virion attachment to host cell.
- Basolateral plasma membrane (IDA, PMID:15052268, ARC syndrome/VPS33B) marked UNDECIDED: abstract-only
  cache, CEA not mentioned; may reflect disease mislocalization of an apical protein.
