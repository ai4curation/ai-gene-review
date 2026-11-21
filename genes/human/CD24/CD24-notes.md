# CD24 notes

Deep research (`just deep-research-falcon human CD24 --fallback perplexity-lite`) failed in this
environment (no provider available); research done directly from cached publications and UniProt.

## Identity and localization
- 80-aa precursor: signal peptide 1-26, mature peptide 27-59, C-terminal propeptide 60-80 removed;
  GPI anchor on amidated Gly59 (UniProt P25063, by similarity). Two N-glycosylation sites; extensively O-glycosylated.
- UniProt: "SUBCELLULAR LOCATION: Cell membrane; Lipid-anchor, GPI-anchor."
- [PMID:16390867 "CD24 is a small, heavily glycosylated cell-surface protein which is linked to the membrane via a glycosyl-phosphatidylinositol (GPI-) anchor and therefore localizes in lipid rafts"]
- Conclusion: outer leaflet of plasma membrane, entire mature protein extracellular; raft-enriched.
  No cytoplasmic domain [PMID:11313396 "CD24 has no cytoplasmic portion to transduce signals intracellularly"].

## Ligand functions
- Siglec-10: [PMID:31367043 "CD24 is the primary protein ligand for Siglec-10"]; anti-phagocytic
  "don't eat me" signal on tumours. [PMID:19264983 "Siglec-10, but not Siglecs -5, -7 or -11, bound to CD24"];
  CD24-Siglec-G/10 represses DAMP (HMGB1, HSP70, HSP90) responses (mostly mouse data).
- P-selectin: [PMID:9129046 "CD24 ... can promote binding to P-selectin"]; platelet adhesion to DU145 [PMID:15633604].

## Signaling
- Associates with FGR (SW2) and LYN (K562) [PMID:8753773]; raft LYN activation and apoptosis after cross-linking in Burkitt lymphoma [PMID:11313396].
- Calcium flux / oxidative burst after antibody cross-linking [PMID:2153173, PMID:8223854].
- Reduces CXCR4 signaling/raft association [PMID:16390867].

## Curation issues
- PMID:8753773 protein binding row WITH UniProtKB:P11362 (FGFR1) — paper studies c-fgr (FGR, P09769); recorded as source defect.
- Wnt signaling NAS (PMID:16532032): CD24 is a Wnt target-gene readout, removed.
- Added NEW: signaling receptor binding (Siglec-10 ligand) and negative regulation of immune response (PMID:31367043).
