# HSP104 review notes

## 2026-10-05 fungal PAINT-family review

- `CANAL/HSP104` was selected for the first fungal PAINT-family batch because
  `PTHR11638` has a fungal Hsp104 node, `PANTHER:PTN007521008`, carrying
  `GO:0005829`, `GO:0042026`, `GO:0043335`, `GO:0051087`, and `GO:0070370`.
  The heat-acclimation row is seeded by `CGD:CAL0000200274` itself, which is
  correct PAINT grounding because the Candida mutant phenotype helps place the
  inherited fungal Hsp104 assertion.

- Deep-research providers were unavailable in this shell (`falcon` lacked
  `agentapi`, and the API-key-backed fallback was not configured), so this
  review used manual literature triage from cached GOA publications and live
  searches. No newer Candida HSP104 primary paper displaced the 2006
  functional-ortholog study, the 2011 sumoylation study, the 2012 Candida
  deletion/reconstitution biofilm and heat-stress study, or the 2017 Candida
  Hsp104 N-terminal crystal structure.

- Zenthon et al. established that CaHsp104 is an Hsp104 ortholog and could
  provide all tested ScHsp104 functions in an S. cerevisiae hsp104 null mutant:
  high-temperature tolerance, heat-denatured protein reactivation, and PSI+
  propagation [PMID:16467463, "CaHsp104 is able to provide all known functions
  of ScHsp104 in an S. cerevisiae hsp104 null mutant, i.e., tolerance to
  high-temperature stress, reactivation of heat-denatured proteins, and
  propagation of the [PSI+] prion."]. The cache is abstract-only, so this paper
  supports the Hsp104-family molecular-function synthesis but not more granular
  claims about in vitro reconstitution.

- Fiori et al. directly support the C. albicans heat-acclimation and biofilm
  process annotations: HSP104-null cells were hypersensitive to lethal heat,
  reintegration restored wild-type heat resistance, induced ectopic HSP104 was
  sufficient to increase thermotolerance, and the deletion mutant formed
  defective mature biofilms on polystyrene and polyurethane
  [PMID:22635920, "biofilm formation by cells lacking HSP104 proved to be
  defective in two established in vitro models that use polystyrene and
  polyurethane as the substrates."]. The biofilm term is credible but was kept
  non-core because Hsp104 is a stress disaggregase, not a dedicated matrix or
  adhesin component.

- Leach et al. identified Hsp104 as a sumoylation target and found that changing
  the Hsp104 consensus SUMO site affected C. albicans thermal-stress resistance
  [PMID:21209325, "Mutation of consensus sumoylation sites in Hsp60 and Hsp104
  affected the resistance of C. albicans to thermal stress."]. This supports the
  heat-response row but is less direct than the deletion/reconstitution assay.

- The CGD `cell surface` IDA was left `UNDECIDED`. The cell-wall proteomics
  paper is abstract-only in `publications/`, and the abstract states only that
  mass spectrometry found several cell-surface proteins classically associated
  with both the wall and other compartments. That is enough to trust that CGD
  had a full-text basis, but not enough to tell whether HSP104 had unique
  peptides or whether the surface association is physiologically meaningful.
