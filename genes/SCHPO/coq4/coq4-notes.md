# coq4 (O94453, SPAC1687.12c) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record (HAMAP MF_03111) and the cached
literature; PMID:24911838 was read in full, PMID:38295803 is abstract-only.

## Literature

- Deletion abolishes CoQ10 [PMID:24911838 "Overall, these data indicate that, like the
  S. pombe Δdps1, Δdlp1, Δppt1/coq2, Δcoq3, Δcoq7, and Δcoq8 strains described
  previously, the Δcoq4, Δcoq5, Δcoq6, and Δcoq9 strains are also unable to synthesize
  CoQ."]
- Human COQ4 complements [PMID:24911838 "Similar results were obtained when HsCOQ4 and
  HsCOQ6 were expressed in the Δcoq4 and Δcoq6 strains, respectively (Figures 6A and
  6B)."]
- COQ4 is the C1 oxidative decarboxylase (human/yeast proteins in bacterial hosts)
  [PMID:38295803 "Here, we provide evidence that these two reactions occur in a single
  oxidative decarboxylation step catalyzed by COQ4."]
- No S. pombe enzymology.

## Audit decisions (2026-11)

- GO:0016831 carboxy-lyase activity changed from TOO_GENERAL to MODIFY -> GO:0120539,
  matching the S. cerevisiae COQ4 review (human COQ4 uses KEEP_AS_NON_CORE with the same
  replacement listed; flagged as a sibling inconsistency for the coordinator).
- Truncated UniProt FUNCTION and CATALYTIC ACTIVITY quotes completed.
- Core function GO:0120539 agrees with the module annoton. The PomBase GO-CAM assigns the
  C1 hydroxylation to coq6; PMID:38295803 assigns both C1 reactions to COQ4.
