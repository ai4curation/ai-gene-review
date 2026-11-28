# ACP2 notes

## Manual literature review

- Deep research could not be generated for this family because the configured `falcon` and `perplexity` providers were unavailable in the local runner (`agentapi not found`; fallback providers unavailable). I reviewed the fetched UniProt, GOA, PANTHER/PAINT, Reactome, and cached PMID records manually.
- ACP2 is the lysosomal acid phosphatase branch of PTHR11567. UniProt records EC 3.1.3.2 acid phosphatase activity, a type I lysosomal membrane precursor, and proteolytic release into the lysosomal lumen.
- The key localization and processing papers are PMID:3056714 and PMID:2684640, which show that human lysosomal acid phosphatase reaches lysosomes as a transmembrane protein and is released from the membrane after lysosomal proteolysis.
- PMID:28272419 supports the influenza A/B entry phenotype as a non-core host factor role in the membrane-fusion step.

## PAINT

`PANTHER:PTN000902303` supports ACP2 acid phosphatase activity and lysosomal localization but also propagates both rows to human ACP4. ACP4 has diverged to a membrane protein tyrosine phosphatase, so the node should be pruned at the ACP4 clade.
