# A0A0B2V7F6 notes

## 2026-11-23

- Started the `TOXCA/A0A0B2V7F6` review from current `origin/main` in a fresh
  registered worktree for the nematode beta-tubulin/benzimidazole lane.
- Resolved the target from live UniProt release 2026_04 before fetching:
  *Toxocara canis* uses the `TOXCA` mnemonic and taxon 6265; A0A0B2V7F6 is a
  442 aa unreviewed beta-tubulin in PANTHER family PTHR11588 with gene name
  `TBB`, ORF name `Tcan_18884`, and EMBL genomic record `JPKZ01001926` /
  protein `KHN79356.1`.
- The live UniProt PTHR11588 search for T. canis returned many alpha-, beta-
  and gamma-tubulin entries plus fragments. A0A0B2V7F6 is one of the
  near-full-length beta-tubulin candidates and is encoded on the same WGS
  scaffold as the A0A0B2VD78/tbb-4/Tcan_18889 beta-tubulin. I kept this review
  accession-scoped and did not infer a one-to-one BEN-1 relationship for the
  generic `TBB` gene name.
- `just deep-research-falcon TOXCA A0A0B2V7F6 --fallback perplexity-lite`
  could not generate a provider report because only `claude_code` was
  available, so this review uses the seeded GOA rows, live-matching UniProt
  flatfile, the cached Zhu et al. T. canis genome paper PMID:25649139, and the
  surrounding nematode beta-tubulin reviews.
- `just fetch-gene-pmids TOXCA A0A0B2V7F6` found no PMID rows in the
  GOA-derived review; `PMID:25649139` was already cached on `origin/main`
  because UniProt imports both A0A0B2V7F6 and the merged A0A0B2VD78 review
  accession from the T. canis WGS assembly reported by Zhu et al.
- `just paint-losses TOXCA A0A0B2V7F6` reported no IRD or IKR loss on the
  gene's lineage, noting that A0A0B2V7F6 is not a leaf of the cached PTHR11588
  tree.
- I added PMID:2592410 as the C. elegans genetic anchor that a beta-tubulin can
  convey nematode benzimidazole sensitivity. I did not find direct T. canis
  evidence assigning TBB/A0A0B2V7F6, A0A0B2VD78, or another current Toxocara
  beta-tubulin model to the equivalent drug-sensitive isotype.
