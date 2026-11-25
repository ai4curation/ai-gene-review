# SLC6A14 (ATB0+) review notes

- SLC6A14 is the molecular basis of system B0+: concentrative, Na+- and Cl--coupled symport
  (2 Na+ + 1 Cl- per amino acid) of a broad range of neutral and cationic L-amino acids
  (exception: proline) at the apical/brush-border membrane
  [PMID:10446133 "hATB(0+) was found to transport both neutral and cationic amino acids, with the highest affinity for hydrophobic amino acids and the lowest affinity for proline"].
- Also transports carnitine/acylcarnitines (low-affinity, high-capacity) coupled to the same
  gradients [PMID:17855766 "L-carnitine is absorbed in the intestinal tract via the carnitine transporter OCTN2 and the amino acid transporter ATB(0,+)"], a genuine secondary activity.
- It is the beta-alanine carrier [PMID:18599538 "can transport non-alpha-amino acids such as beta-alanine with low affinity, and has a higher affinity for dipolar and cationic amino acids such as leucine and lysine"].

## Neurotransmitter-exclusion argument
- SLC6A14 is grouped by Reactome under "SLC-mediated transport of neurotransmitters" by SLC6
  family membership, but it is a broad epithelial nutrient amino-acid transporter (lung, salivary
  gland, mammary gland, gut) with no established neurotransmission role. GO:0006836 neurotransmitter
  transport kept MARK_AS_OVER_ANNOTATED. NOTE: unlike B0AT2/SLC6A15, SLC6A14 DOES carry glycine
  (a high-affinity substrate, KM ~0.32 mM), so the over-annotation (not REMOVE) call is the right
  one here — the term is over-reaching, not strictly false.

## Decisions
- Item-1 action framework (2026-11-14 ruling): generic substrate-named amino-acid parent terms
  (GO:0003333, GO:0006865, GO:0015171) treated as ACCEPT; only bare parents TOO_GENERAL. Here the
  bare GO:0015370 solute:sodium symporter activity (ARBA) set to TOO_GENERAL (bare, unspecified
  solute), entailed by the curated GO:0015374 amino acid:Na:Cl symporter activity. GO:0016020
  membrane: both rows are TOO_GENERAL here because their own (electronic) evidence stops at
  "membrane", while the specific apical/plasma-membrane location is asserted on other rows. The
  action for a membrane row follows whether that row's own evidence resolves the compartment —
  MODIFY -> plasma membrane only where it does (see SLC6A15's IDA/NAS membrane rows), TOO_GENERAL
  where it stops at membrane.
