# F1L5R2 notes

## 2026-11-23

- Started the `ASCSU/F1L5R2` review from current `origin/main` in a fresh
  registered worktree for the nematode anthelmintic target lane.
- Resolved the target from live UniProt before fetching: *Ascaris suum* uses
  the `ASCSU` mnemonic and taxon 6253; F1L5R2 is a 450 aa unreviewed
  beta-tubulin in PANTHER family PTHR11588 with EMBL mRNA records `JI171920`
  / `ADY45466.1` and `JI173475` / `ADY46271.1`.
- The F1L5R2 GOA row set has seven beta-tubulin rows and no GO_REF:0000108
  cytoskeleton-organization row, so this review accepts the directly asserted
  `GO:0000226` microtubule cytoskeleton organization row rather than modifying
  `GO:0007010` as in the related `ASCSU/F1L8A5` review.
- `just fetch-gene-pmids ASCSU F1L5R2` found no PMID rows in the GOA-derived
  review. `PMID:21685128` was already cached on `origin/main` and is cited
  because UniProt traces F1L5R2 to mRNA accessions from that Wang et al.
  transcriptome assembly.
- `just deep-research-falcon ASCSU F1L5R2 --fallback perplexity-lite` could not
  generate a provider report because only `claude_code` was available, so this
  review uses the seeded GOA rows, the live-matching UniProt flatfile, the
  cached Wang et al. paper PMID:21685128, C. elegans BEN-1 PMID:2592410, and
  the surrounding nematode beta-tubulin reviews.
- `just paint-losses ASCSU F1L5R2` reported no IRD or IKR loss on the gene's
  lineage, noting that F1L5R2 is not a leaf of the cached PTHR11588 tree.
- I added PMID:2592410 as the C. elegans genetic anchor that a beta-tubulin can
  convey nematode benzimidazole sensitivity. I did not find direct A. suum
  evidence assigning F1L5R2 or a reconciled F1L5R2-encoding locus to the
  equivalent Ascaris drug-sensitive isotype.
