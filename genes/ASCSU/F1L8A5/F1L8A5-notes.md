# F1L8A5 notes

## 2026-11-23

- Started the `ASCSU/F1L8A5` review from current `origin/main` in a fresh
  registered worktree for the nematode anthelmintic target lane.
- Resolved the target from live UniProt release 2026_04 before fetching:
  *Ascaris suum* uses the `ASCSU` mnemonic and taxon 6253; F1L8A5 is a 444 aa
  unreviewed beta-tubulin in PANTHER family PTHR11588 with EMBL mRNA
  `JI173658` / protein `ADY46359.1`.
- The live UniProt search also returned multiple other PTHR11588 ASCSU
  beta-tubulin fragments or near-full-length candidates. I kept this review
  accession-scoped and did not invent an Ascaris gene symbol.
- `just deep-research-falcon ASCSU F1L8A5 --fallback perplexity-lite` could
  not generate a provider report because only `claude_code` was available, so
  this review uses the seeded GOA rows, live-matching UniProt flatfile, the
  cached Wang et al. paper PMID:21685128, and the surrounding nematode
  beta-tubulin reviews.
- `just fetch-gene-pmids ASCSU F1L8A5` found no PMID rows in the GOA-derived
  review; `PMID:21685128` was fetched explicitly because UniProt cites it as
  the nucleotide-sequence publication for the imported transcript.
- `just paint-losses ASCSU F1L8A5` reported no IRD or IKR loss on the gene's
  lineage, noting that F1L8A5 is not a leaf of the cached PTHR11588 tree.
