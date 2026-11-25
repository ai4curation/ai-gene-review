# coq6 (Q9Y7Z9, SPBC146.12) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record (HAMAP MF_03193) and the cached
literature; PMID:24911838 and PMID:38425362 were read in full, PMID:38295803 from the
abstract.

## Literature

- Deletion abolishes CoQ10; human COQ6 complements [PMID:24911838 "Similar results were
  obtained when HsCOQ4 and HsCOQ6 were expressed in the Δcoq4 and Δcoq6 strains,
  respectively (Figures 6A and 6B)."]
- Electron supply: by homology via ferredoxin reductase and ferredoxin [PMID:24911838
  "cerevisiae, the two essential genes, ARH1 and YAH1, are involved in CoQ synthesis
  through the regulation of Coq6 [26]."] In S. pombe this is still a proposal
  [PMID:37156397 "Coq6 may require ferredoxin Yah1 (Etp1) and ferredoxin reductase Arh1
  as in S."]
- C1 hydroxylation conflict: human COQ6 hydroxylates C1 in vitro [PMID:38425362 "Indeed,
  COQ6, in the presence of FDXR and FDX2, produced the 4b adduct corroborating its dual
  functionality as both a C5 and C1 hydroxylase"], whereas COQ4 performs both C1 reactions
  in vivo [PMID:38295803 "Here, we provide evidence that these two reactions occur in a
  single oxidative decarboxylation step catalyzed by COQ4."]

## Audit decisions (2026-11)

- GO:0120538 (C1 hydroxylase, IEA from HAMAP) changed from ACCEPT to
  MARK_AS_OVER_ANNOTATED: real in vitro activity of the human ortholog, disputed in vivo.
  Siblings disagree (yeast COQ6 REMOVE, human COQ6 ACCEPT with IDA); flagged for the
  coordinator. Suggested question added.
- GO:0016712 changed from MARK_AS_OVER_ANNOTATED to MODIFY -> GO:0106364 (wrong donor
  class, monooxygenase essence sound), matching the S. cerevisiae COQ6 review.
- Core function GO:0106364 (C5 hydroxylation) agrees with the module.
