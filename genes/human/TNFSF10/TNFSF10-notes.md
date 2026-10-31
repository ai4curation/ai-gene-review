# TNFSF10 manual curation notes

## 2026-09-30

- TNFSF10/TRAIL is a type II TNF-family ligand whose extracellular TNF-homology
  domain can act both at the cell surface and as a soluble shed ligand. The two
  original discovery papers showed that full-length or soluble TRAIL is a
  pro-apoptotic TNF-family cytokine [PMID:8777713 Identification and
  characterization of a new member of the TNF family that induces apoptosis,
  "Both full-length cell surface expressed TRAIL"; PMID:8663110 Induction of
  apoptosis by Apo-2 ligand, a new member of the tumor necrosis factor cytokine
  family, "Soluble Apo-2L induces extensive apoptosis"].
- The core molecular event is TNFSF10 homotrimer binding to TNFRSF10A/DR4 or
  TNFRSF10B/DR5, with the decoy receptors TNFRSF10C and TNFRSF10D competing in
  the same extracellular receptor-binding space. Structural work directly
  supports both death receptors: the DR5-Apo2L/TRAIL structure places three DR5
  ectodomains against the homotrimeric ligand [PMID:10549288 Triggering cell
  death: the crystal structure of Apo2L/TRAIL in a complex with death receptor
  5, "three elongated receptors snuggled into long crevices"], and the later
  DR4 structure plus ITC compares DR4 and DR5 binding thermodynamics
  [PMID:26457518 The structure of the death receptor 4-TNF-related
  apoptosis-inducing ligand (DR4-TRAIL) complex, "DR4 or DR5 titrated into
  TRAIL"].
- The appropriate process term for the death-receptor arm is
  `GO:0036462 TRAIL-activated apoptotic signaling pathway`: production GO-CAMs
  for both the TRAIL/TRAILR1 and TRAIL/TRAILR2 arms enable the TNFSF10 activity
  as `GO:0005125 cytokine activity`, place it in the extracellular region, and
  make it part of `GO:0036462`. This is the useful tightening for the early
  broad `apoptotic process`, `signal transduction`, and `cell-cell signaling`
  rows.
- TNFSF10 is genuinely present as membrane-bound and soluble protein in human
  immune cells [PMID:14609566 Regulation of soluble and surface-bound TRAIL in
  human T cells, B cells, and monocytes, "membrane-bound and soluble protein"].
  A 2011 plasma cytokine panel measured soluble TRAIL in human plasma and is
  adequate extracellular-region support, but it is not a direct assay of
  receptor binding or cytokine activity.
- Zinc coordination and self-association are structural support for the TNF
  homotrimer rather than separate core activities. Ramamurthy et al. observed
  the expected trimer and a Zn2+ site in recombinant TRAIL
  [PMID:26457518, "TRAIL suggested that the protein forms the expected trimeric
  structure"; "a Zn 2+ site was found"].
- The `PMID:19427028` CUL3 import is downstream DISC biology. CUL3-based
  polyubiquitination acts on caspase-8 after death receptor ligation
  [PMID:19427028 Cullin3-based polyubiquitination and p62-dependent aggregation
  of caspase-8 mediate extrinsic apoptosis signaling, "death receptor ligation
  induces polyubiquitination of caspase-8"], so it should not stand as a direct
  TNFSF10 molecular function.
- Several later IntAct rows use TRAIL as an exogenous stimulus in bortezomib,
  resveratrol, HDAC-inhibitor, NF-kappaB, or V-ATPase sensitization studies.
  The receptor edges are consistent with the known TNFRSF10A/B/C/D binding
  activity and can be narrowed from `protein binding`; the cytochrome-c release
  row is over-annotated because release of mitochondrial cytochrome c is
  executed downstream through BID, BAX, and BAK rather than by the ligand.
- NF-kappaB activation and exosomal detection were kept as non-core context:
  a cDNA overexpression screen recovered TNFSF10 as one of many NF-kappaB
  activators [PMID:12761501 Large-scale identification and characterization of
  human genes that activate NF-kappaB and MAPK signaling pathways, "identified
  299 cDNAs that activate the NF-kappaB pathway"], and a parotid-saliva MudPIT
  study placed TNFSF10 in a mass-spectrometry exosome fraction
  [PMID:19199708 Proteomic analysis of human parotid gland exosomes by
  multidimensional protein identification technology (MudPIT), "491 proteins in
  the exosome fraction"].
