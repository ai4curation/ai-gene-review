# ROR2 (human, Q01974) curation notes

Deep research providers were unavailable in this environment; evidence is from cached publications
and UniProt.

## Localization
- Single-pass type I plasma membrane receptor: UniProt `SUBCELLULAR LOCATION: Cell membrane
  {ECO:0000250}; Single-pass type I membrane protein`; extracellular Ig-like, Frizzled-like
  cysteine-rich and kringle domains are surface-exposed.
- [PMID:17717073 "Ror2 homodimerizes at the cell surface"] — cell-surface accessible, confirmed by
  bivalent-antibody-induced dimerization (relevant for antibody-based targeting).
- Clathrin-coated endocytic vesicle membrane (Reactome) kept as non-core trafficking compartment.

## Kinase activity
- [PMID:17717073 "Purified Ror2 phosphorylates 14-3-3beta in vitro, confirming 14-3-3beta as the
  first identified Ror2 substrate."]; UniProt EC 2.7.10.1. UniProt also notes "has also been shown
  to have very little tyrosine kinase activity in vitro", and TAK1-dependent phosphorylation of ROR2
  is "not mediated by the Ror2 tyrosine kinase domain" [PMID:18762249]. The kinase rows were
  therefore ACCEPTed (not removed as for a true pseudokinase such as PTK7) but the weak-activity
  caveat is recorded here and in the description.

## Wnt function
- UniProt: "May act as a receptor for wnt ligand WNT5A which may result in the inhibition of
  WNT3A-mediated signaling"; WNT5B identified in osteosarcoma [PMID:19486338].
- ROR2 knockdown reduces osteosarcoma proliferation and migration [PMID:19486338].

## Review decisions
- 29 generic `GO:0005515` rows removed per policy; Wnt-protein binding and MAP3K binding kept.
- `GO:0004672 protein kinase activity` modified to the tyrosine-specific terms; `GO:0007165 signal
  transduction` modified to the RTK signalling pathway term.
- `GO:0030424 axon` (IBA) kept as non-core.
