# A0A0B2VD78 notes

## 2026-11-23

- Started the `TOXCA/A0A0B2VD78` review from current `origin/main` in a fresh
  registered worktree for the nematode beta-tubulin/benzimidazole lane.
- Resolved the target from live UniProt release 2026_04 before fetching:
  *Toxocara canis* uses the `TOXCA` mnemonic and taxon 6265; A0A0B2VD78 is a
  444 aa unreviewed beta-tubulin in PANTHER family PTHR11588 with gene name
  `tbb-4`, ORF name `Tcan_18889`, and EMBL genomic record
  `JPKZ01001926` / protein `KHN79367.1`.
- The live UniProt PTHR11588 search for T. canis returned many alpha-, beta-
  and gamma-tubulin entries plus fragments. A0A0B2VD78 is one of the
  near-full-length beta-tubulin candidates; another candidate,
  A0A0B2V7F6/Tcan_18884, is a 442 aa beta-tubulin on the same WGS scaffold.
  I kept this review accession-scoped and did not infer a one-to-one BEN-1
  relationship for the `tbb-4` name.
- `just deep-research-falcon TOXCA A0A0B2VD78 --fallback perplexity-lite`
  could not generate a provider report because only `claude_code` was
  available, so this review uses the seeded GOA rows, live-matching UniProt
  flatfile, the cached Zhu et al. T. canis genome paper PMID:25649139, and the
  surrounding nematode beta-tubulin reviews.
- `just fetch-gene-pmids TOXCA A0A0B2VD78` found no PMID rows in the
  GOA-derived review; `PMID:25649139` was fetched explicitly because UniProt
  imports A0A0B2VD78 from the T. canis WGS assembly reported by Zhu et al.
- `just paint-losses TOXCA A0A0B2VD78` reported no IRD or IKR loss on the
  gene's lineage, noting that A0A0B2VD78 is not a leaf of the cached PTHR11588
  tree.
- I added PMID:2592410 as the C. elegans genetic anchor that a beta-tubulin can
  convey nematode benzimidazole sensitivity. I did not find direct T. canis
  evidence assigning tbb-4/A0A0B2VD78 or the adjacent Tcan_18884 beta-tubulin
  to the equivalent Toxocara drug-sensitive isotype.
