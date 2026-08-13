# SSQ1 review notes

## 2026-08-12 re-review

- Identity verified as *Saccharomyces cerevisiae* SSQ1/YLR369W, UniProt Q05931,
  the mitochondrial Ssq-type Hsp70 dedicated to iron-sulfur cluster biogenesis.
- The existing Falcon report is correctly scoped to Q05931. An OpenScientist
  run was launched through `just deep-research-openscientist yeast SSQ1`; after
  extended silent polling without a returned artifact it was interrupted. No
  unreturned result was treated as evidence.
- Core mechanism: Jac1 recruits the Isu scaffold and stimulates the Ssq1 ATPase
  cycle; Mge1 promotes nucleotide exchange; Ssq1 recognizes the Isu LPPVK motif
  and drives release/handoff of the newly assembled cluster to Grx5.
- UniProt resolves the GOA IntAct partners directly: Q03020 is the physiological
  Isu1 scaffold client, whereas P15646 is the nucleolar protein Nop1. The Isu1
  rows are biologically relevant but poorly expressed by bare protein binding;
  the Nop1 rows are likely high-throughput background for a matrix protein.
- Generic family terms were narrowed where a more informative child exists:
  GO:0044183 and GO:0051082 are modified to GO:0140662, generic nucleotide and
  hydrolase parents are over-annotated, and mitochondrial matrix is the core
  location rather than its broad organelle/lumen parents.
- GO:0042026 protein refolding is an unsafe general-Hsp70 IBA transfer. Ssq1 is
  specialized for the Isu client and ISC transfer rather than broad stress
  refolding; the propagation audit records this functional divergence.
- The cytoplasm IBA is ontologically true because mitochondria are part of the
  GO cytoplasm, but it is marked over-annotated because matrix is the precise
  functional compartment. Intracellular iron homeostasis is retained as a
  genuine downstream phenotype, not a core direct function.
