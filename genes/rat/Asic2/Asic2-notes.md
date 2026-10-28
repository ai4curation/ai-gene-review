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

## 2026-10-28 review-fix pass

- The second core function (spine targeting of ASIC1a through PSD-95) now uses GO:0030165 PDZ domain binding as molecular_function in place of GO:0160125 pH-gated sodium channel activity, since the conductance does not do the targeting. Support is quoted from PMID:19571134 (mouse ASIC2a binds PSD-95 through its C-terminal PDZ-binding motif). Added a matching NEW IC row for GO:0030165. [Corrected 2026-10-28: the row is ISS from mouse UniProtKB:Q925H0, not IC; see the dated note below.] Rat ASIC2a (Q62962-1) ends in the same Ile-Ala-Cys motif.
- Removed supported_by self-citations of the gene's own -deep-research-manual.md where a primary citation in the same block already supports the row (the reviewer's own conclusion is not independent evidence). The validator now warns that no annotation cites the deep-research file; that warning is accepted deliberately, which sets the status to DRAFT.

## 2026-10-28: PDZ-binding row evidence code

The NEW GO:0030165 row rests on the mouse ASIC2a experiment (PMID:19571134) plus the conserved C-terminal
Ile-Ala-Cys motif in rat Q62962-1, so its evidence code is ISS with the mouse protein (UniProtKB:Q925H0)
as the source, not IC.
