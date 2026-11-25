# A0A0B2VSH4 notes

## 2026-11-23

- Started the `TOXCA/A0A0B2VSH4` review from current `origin/main` in a
  fresh registered worktree for the nematode beta-tubulin/benzimidazole lane.
- Resolved the target from live UniProt before fetching: *Toxocara canis* uses
  the `TOXCA` mnemonic and taxon 6265; A0A0B2VSH4 is a 450 aa unreviewed
  beta-tubulin in PANTHER family PTHR11588 with ORF name `Tcan_03365` and EMBL
  genomic record `JPKZ01001101` / protein `KHN83955.1`.
- QuickGO timed out or returned HTTP 500 twice for this accession, then
  recovered and returned the seven GOA rows seeded in
  `A0A0B2VSH4-ai-review.yaml`.
- The live UniProt check also resolved another current T. canis full-length
  beta-tubulin candidate, A0A0B2VUK1/Tcan_06249. I kept this review
  accession-scoped and did not infer a one-to-one BEN-1 relationship for
  Tcan_03365.
- `just deep-research-falcon TOXCA A0A0B2VSH4 --fallback perplexity-lite`
  could not generate a provider report because only the `claude_code`
  provider was available. This review uses the seeded GOA rows, live-matching
  UniProt flatfile, the cached Zhu et al. T. canis genome paper PMID:25649139,
  the C. elegans BEN-1 genetic anchor PMID:2592410, and the surrounding
  nematode beta-tubulin reviews.
- `just fetch-gene-pmids TOXCA A0A0B2VSH4` found no PMID rows in the
  GOA-derived review; `PMID:25649139` was already cached on `origin/main`
  because UniProt imports A0A0B2VSH4 from the T. canis WGS assembly reported
  by Zhu et al.
- `just paint-losses TOXCA A0A0B2VSH4` reported no IRD or IKR loss on the
  gene's lineage, noting that A0A0B2VSH4 is not a leaf of the cached PTHR11588
  tree.
- I added PMID:2592410 as the C. elegans genetic anchor that a beta-tubulin can
  convey nematode benzimidazole sensitivity. I did not find direct T. canis
  evidence assigning A0A0B2VSH4, Tcan_03365, or another current Toxocara
  beta-tubulin model to the equivalent drug-sensitive isotype.
