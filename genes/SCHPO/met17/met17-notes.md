# SCHPO met17 notes

## 2026-10-24

Fetched `SCHPO/met17` with `just fetch-gene SCHPO met17`; the current GOA file
contains 22 rows. Falcon deep research was attempted with
`just deep-research-falcon SCHPO met17`, but no provider API keys were
configured, so this review used the fetched PomBase/GOA/UniProt records, the
cached publications, manual PubMed/web search, and the local PTHR43797 PAINT
table.

The direct cached evidence is:

- PMID:6526818, "O-Acetylhomoserine sulfhydrylase of the fission yeast
  Schizosaccharomyces pombe: partial purification, characterization, and its
  probable role in homocysteine biosynthesis" - abstract-only in the cache;
  extracts "catalyzed sulfhydrylation of both O-acetyl-L-serine and
  O-acetyl-L-homoserine with H2S", the enzyme was purified about 300-fold, and
  the enzyme was reactivated by pyridoxal 5'-phosphate.
- PMID:7926667, "Sulfur amino acid metabolism in Schizosaccharomyces pombe:
  occurrence of two O-acetylhomoserine sulfhydrylases and the lack of the
  reverse transsulfuration pathway" - abstract-only; reports "two distinct
  O-acetylhomoserine sulfhydrylases" and states that S. pombe lacks the
  reverse transsulfuration enzymes cystathionine beta-synthase and
  cystathionine gamma-lyase.
- PMID:11754480, "Sulphur amino acid synthesis in Schizosaccharomyces pombe
  represents a specific variant of sulphur metabolism in fungi" -
  abstract-only; reiterates that S. pombe lacks cystathionine beta-synthase and
  cystathionine gamma-lyase and reports that sulfur metabolite repression
  operates at the transcriptional level for the homocysteine synthase gene.
- PMID:16823372, "ORFeome cloning and global analysis of protein localization
  in the fission yeast Schizosaccharomyces pombe" - abstract-only; provides the
  large-scale YFP localization source for the cytosolic/cytoplasmic and nuclear
  annotations.
- PMID:17482430, "Multiple fungal enzymes possess cysteine synthase activity in
  vitro" - abstract-only; reports that S. pombe mutant strains gave similar
  results to A. nidulans, where multiple enzymes had in-vitro cysteine synthase
  activity but only the canonical cysteine synthase was physiologically
  important.

The current PTHR43797 PAINT export has three `PTN002887184` rows: cytoplasm,
O-acetylhomoserine sulfhydrylase activity, and L-homocysteine biosynthetic
process. The stale 2023 IBA to `GO:0004124` cysteine synthase activity should
therefore be treated as inherited from older PAINT output rather than as a
current node assertion. Because S. pombe Met17 has curated experimental
support for O-acetylserine sulfhydrylation, the activity is still
biologically defensible as non-core in-vitro chemistry.

Manual web searches for newer `met17`/`cys2`/O-acetylhomoserine sulfhydrylase
papers in S. pombe did not find a newer primary paper changing the direct Met17
functional picture; newer hits were sulfur-metabolism reviews, database pages,
or budding-yeast MET17/Met15 work.
