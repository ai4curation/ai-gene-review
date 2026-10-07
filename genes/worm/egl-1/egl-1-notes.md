# egl-1 notes

## 2026-09-30 APOPTOSIS manual review

EGL-1 is the C. elegans BH3-only trigger for the canonical CED-9/CED-4/CED-3
apoptosis pathway. The core molecular function is not generic protein binding:
EGL-1 donates its BH3-like helix to the CED-9 binding groove, inhibits the
anti-apoptotic CED-9/CED-4 complex, and releases CED-4 so it can activate CED-3
[PMID:9604928, "EGL-1 activates programmed cell death by binding to and
directly inhibiting the activity of CED-9"; PMID:11027303, "direct physical
interaction between EGL-1 and CED-9 is essential"; PMID:15383288, "The
C-terminal half of EGL-1 is necessary and sufficient for binding to CED-9"].

- Generic `GO:0005515 protein binding` rows to CED-9 were modified to a
  proposed EGL-1/BH3-ligand-side term, `pro-survival BCL2 family protein
  inhibitor activity`. The existing `GO:0051434 BH3 domain binding` term is
  correct for CED-9, the groove-containing partner, but is directionally wrong
  for the BH3-only ligand.
- The top-level `GO:0006915 apoptotic process` row from the Salmonella
  germline-death paper was narrowed to `GO:0043065 positive regulation of
  apoptotic process`. The same paper's `defense response to Gram-negative
  bacterium` row is over-annotated: EGL-1 is part of the apoptosis pathway that
  affects Salmonella survival, not a bacterium-specific defense effector
  [PMID:11226309, "egl-1(n1084n3082) loss-of-function mutant also exhibited a
  reduction in Salmonella -induced germ-line apoptosis"].
- The structural CED-4/CED-9 paper supports apoptotic signaling rather than the
  generic `positive regulation of protein-containing complex assembly`: EGL-1
  binding causes CED-4 dimer release and subsequent oligomerization
  [PMID:16208361, "The released CED-4 dimer further dimerizes to form a
  tetramer"].
- The RME/DD neuron rows from Meng et al. were kept as non-core synapse-pruning
  annotations or modified to `GO:1905808 positive regulation of synapse
  pruning`. EGL-1 is enriched near synaptic mitochondria and genetically
  required with CED-4/CED-9/CED-3 to remove transient presynaptic components,
  but GSNL-1 is the actin-severing effector downstream of CED-3
  [PMID:26074078, "loss-of-function in pro-apoptotic genes, egl-1 and ced-4,
  and gain-of-function in the anti-apoptotic gene ced-9 induced elimination
  defects"].
- The Jagasia mitochondrial-fragmentation row was kept as non-core. EGL-1 can
  induce DRP-1-dependent mitochondrial fragmentation in apoptotic cells
  [PMID:15716954, "Mitochondrial fragmentation is induced by the BH3-only
  protein EGL-1"], but the central EGL-1 output remains CED-9 inhibition and
  CED-4 release.
- The PIG-1/PAR-4 cell-extrusion paper is over-annotation for EGL-1. `egl-1`
  loss, `ced-4` loss, and `ced-9(gf)` all block canonical apoptosis and reveal a
  distinct caspase-independent shedding pathway rather than demonstrating that
  EGL-1 performs the PIG-1-dependent adhesion/extrusion step
  [PMID:22801495, "the BH3 domain-encoding gene egl-1 ... also produced shed
  cells"].
- Three rows were left conservative. The cached 1998 JBC abstract describes
  EGL-1-dependent CED-4 redistribution but not enough full-text detail to
  adjudicate the exact `cytosol` and `intracellular membrane-bounded organelle`
  EGL-1 localization rows [PMID:9837929]. The cached miRNA enhancer abstract
  establishes a non-apoptotic CED-3 heterochronic pathway but does not show
  whether EGL-1 participates directly upstream [PMID:25432023].
