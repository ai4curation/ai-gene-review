# ENTR1 (human, Q96C92) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised reference for HORSE/ENTR1
(A0A5F5Q1J2). No ProtNLM2 output was consulted.

### Deep research
- `just deep-research-falcon human ENTR1 --fallback perplexity-lite` failed: Edison API
  returned 403 "Failed to authenticate", and the perplexity fallback returned 401
  (insufficient quota). No deep-research file exists; review is based on the cached
  literature below, found by a PubMed search for "SDCCAG3 OR ENTR1" (32 hits, 2026-10-21).

### Evolutionary grounding
- UniProt: PANTHER PTHR31259 (ENTR1 family), subfamily PTHR31259:SF6; Pfam PF29363; C-terminal
  coiled coil 261-371. Mouse Entr1 (A2AIW0) and horse ENTR1 are in SF3 (see
  genes/HORSE/ENTR1/ENTR1-bioinformatics/RESULTS.md); all are one-to-one mammalian orthologs.
- All five IBA nodes in human GOA (PTN002039065: early endosome, recycling endosome,
  centrosome, midbody, regulation of cytokinesis; PTN004793274: ciliary basal body, positive
  regulation of cilium assembly, positive regulation of protein localization to cilium) list
  human ENTR1 itself in WITH/FROM: human is the experimental donor. This is expected, not
  circular.
- PAINT did not propagate endosome (general), retromer colocalization, or endocytic recycling.
  Treated as deliberate; no change proposed.

### Literature (human unless stated)
- PMID:23108400 (abstract only): early/recycling endosomes; midbody in cytokinesis; PTPN13 and
  GIT1 complex; multinucleation on over/under-expression ["Overexpression as well as
  downregulation correlates with the generation of multinucleate cells."].
- PMID:25278552 (full text): VPS35 interactome; colocalizes with VPS35; knockdown reduces GLUT1
  surface/total levels, minor effects on CD97 and TRAILR1.
- PMID:27767179 (full text): basal body and centrosome localization via aa 1-100; IFT88
  binding; knockdown reduces ciliated cells and cilium length (rescued by human ENTR1 in
  IMCD3); polycystin-2 ciliary localization reduced, Rab8 unaffected.
- PMID:31308371 (full text, not in GOA): ENTR1/PTPN13/dysbindin promote sorting of Fas into
  intraluminal vesicles and lysosomes; ENTR1 depletion increases Fas recycling and surface
  levels; ENTR1 cleaved by caspases at aa 236 ["ENTR1 regulates, via binding to the coiled
  coil domain protein Dysbindin, the delivery of Fas from endosomes to lysosomes thereby
  controlling termination of Fas signal transduction."]. Basis for NEW GO:0008333.
- PMID:38849673 (full text; mouse cells/tissue): DLG1 upstream of SDCCAG3 and IFT20 in ciliary
  PC2 targeting; SDCCAG3-IFT20 complex.
- PMID:27373827 (abstract; mouse protein, HeLa assay): Arf6 binding via C-terminal 101 aa,
  needed for midbody recruitment.
- PMID:16332174 (abstract; mouse): dominant-negative coiled-coil fragment reduces surface TNFR1.
  Only mouse characterisation paper; not used to add a human annotation.
- PMID:27812135: NOD2 interactor screen, no ENTR1 function.
- PMID:41494271 (abstract): antiviral role via MAVS stabilization; species/cell model unclear,
  not used.

### Decisions
- 5x protein binding: REMOVE (policy; interactions not disputed).
- cytoplasm IEA/ISS: TOO_GENERAL (entailed by accepted endosome/centrosome/midbody terms).
- All other rows ACCEPT. NEW: GO:0008333 endosome to lysosome transport (IMP, PMID:31308371).
- No MF asserted: no demonstrated activity beyond binding.
