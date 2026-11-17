# Choline-O-sulfate module notes

## 2026-11-06 — PR #6105 ontology maintenance

Moved the ontology-only COS-transporter gap into module notes. Bacillus OpuC COS transport is established; the outstanding issue is terminology. Generic transport plus explicit CHEBI:16822 cargo preserves the claim without inventing a process annotation or describing established activity as biologically unknown.


## PR6105 candidate-function provenance follow-up (2026-11-06)

The optional Ruegeria BetT annoton now carries a free-text transmembrane-transporter candidate descriptor. Its BCCT/COG1292 family assignment and multipass architecture support the candidate activity class, while the insertion/depletion phenotype remains confounded by downstream betA. No GO molecular-function identifier, transported cargo or coupling mechanism is asserted, no required import role is added, and the production checker continues to reject this candidate as sufficient for COS import. The member evidence cleanup removes a circular quotation of the BetC localization verdict and derives the missing UniProt record sections; no annotation action or native pathway-capacity claim changes.
