# ACP4 notes

## Manual literature review

- Deep research could not be generated for this family because the configured `falcon` and `perplexity` providers were unavailable in the local runner (`agentapi not found`; fallback providers unavailable). I reviewed the fetched UniProt, GOA, PANTHER/PAINT, and cached PMID records manually.
- ACP4/ACPT is a single-pass membrane protein tyrosine phosphatase. PMID:15219672 shows that ACPT dephosphorylates ERBB4, reduces neuregulin-induced ERBB4 phosphorylation and proteolytic cleavage, and modulates ErbB4-dependent neuronal differentiation.
- PMID:27843125 links recessive ACPT variants to hypoplastic amelogenesis imperfecta. The molecular tooth substrate was not resolved in this review, so odontogenesis was kept as a non-core phenotype/process row.

## PAINT

The ACP4 clade has its own PAINT node, `PANTHER:PTN002611605`, for protein tyrosine phosphatase activity, receptor tyrosine kinase binding, ERBB4 signaling, and synaptic-plasticity regulation. ACP2-like lysosomal acid phosphatase activity and lysosomal localization should be pruned before this clade.
