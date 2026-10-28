# Asic2 (rat) review notes

- UniProt Q62962 (Swiss-Prot), RGD:2017, GeneID 25364; fetch-gene resolved the expected accession.
- Deep-research API unavailable; manual synthesis in Asic2-deep-research-manual.md.
- PMID:19074149 (Li, Yang, Canessa 2009) mainly mutates rat ASIC1; for ASIC2a it reports only
  that mutating the conserved Tyr/Trp pair abolishes function [PMID:19074149 "Substitution of either one the aromatic residues by Ala or Gly in rat ASIC2a and ASIC3 also produced non-functional channels."].
  Residue numbers 72/288 refer to ASIC1 numbering, not Q62962.
- Core function: proton (pH)-gated, Na+-selective channel subunit (GO:0160125), plasma membrane,
  Na+ transmembrane transport; ASIC2b is a modulatory subunit only.
- Secondary: PSD-95-dependent targeting of ASIC1a to dendritic spines (mouse, PMID:19571134).
- Most process rows are RGD ISO from mouse knockouts (acts_upstream_of_or_within): baroreflex,
  touch, myogenic tone, retina, cochlea, synapse number. Kept as non-core; apoptosis and hearing
  rows judged over-annotations (retinal degeneration is indirect; null mice have normal hearing
  per PMID:15537887).
- Cellular response to xenobiotic stimulus (IDA, PMID:12736332) reflects amiloride block of the
  channel - drug pharmacology, not a cellular response process; marked over-annotated.
- No NEW terms proposed.
