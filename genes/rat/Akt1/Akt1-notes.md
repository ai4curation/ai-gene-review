# Akt1 review notes

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: this review keeps conserved kinase and canonical PI3K/insulin signaling functions, while removing or downranking many donor-derived developmental, neuronal, immune, stress-response, and context-specific terms as ISO over-annotation.

## 2026-10-10 - OpenScientist kinase-inhibitor follow-up

The focused OpenScientist report for `prediction-kinase-inhibitor-activity`
supports keeping GO:0030291 `protein serine/threonine kinase inhibitor
activity` as REMOVE. PMID:8524413 shows Akt/PKB catalytically phosphorylating
GSK3 on inhibitory serines; the decreased GSK3 activity is the downstream
result of AKT1 kinase signaling, not a stoichiometric molecular function in
which AKT1 binds and inhibits a protein serine/threonine kinase.
