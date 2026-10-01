## 2026-10-01 re-review

- Forced a current GOA/UniProt refresh for CHS7; current GOA has 16 rows, all
  represented in `CHS7-ai-review.yaml`.
- Preserved four historical assertions that no longer appear in live GOA as
  `retired: true`: the old PAINT `GO:0051082` row, the old UniProt keyword
  `GO:0015031` and `GO:0071555` rows, and the older SGD IMP `GO:0051082` row.
- Rechecked PTHR35329 PAINT. Current PAINT places `GO:0006031`,
  `GO:0005789`, `GO:0006457`, and the replacement `GO:0044183` on
  `PTN002175570`; the live GOA rows that already import IBA from that node are
  sound `NO_FAILURE_CORE` transfers.
- Added a conservative `NEW` recommendation for `GO:0044183 protein folding
  chaperone`, because current PAINT now asserts that function at
  `PTN002175570` but the GOA snapshot has not yet imported it.
- Replaced Falcon-derived snippets on the PAINT and key experimental rows with
  exact cached support from PMID:10366589, PMID:15623581, PMID:29405545, and
  PMID:40137259.
- Newer-literature search found the cached 2025 Chs3/Chs7 orphan-subunit
  trafficking paper, PMID:40137259, as the newest CHS7-focused budding-yeast
  primary paper. A 2025 Neurospora CSE-8/Chs7-family paper and a 2026
  Pleurotus ostreatus `chs7` chitin synthase paper did not require new
  S. cerevisiae CHS7 GO assertions.
