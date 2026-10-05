# SAS2 re-review notes

## 2026-09-29 IBA re-review

- Re-read the cached primary literature that anchors the current review:
  PMID:11731479, PMID:11731480, PMID:12626510, PMID:15788653, PMID:16554755,
  PMID:21179020, PMID:27655944, PMID:30358795, and PMID:37968396. The core
  picture remains SAS-I/SAS, composed of Sas2/Sas4/Sas5, as the H4K16/H3K14
  acetyltransferase for free histones rather than a NuA4 subunit.
- Checked `PTHR10615-paint.tsv`. Both SAS2 IBA rows come from
  `PANTHER:PTN007449682`: the node is appropriate for
  `GO:0046972 histone H4K16 acetyltransferase activity`, but
  `GO:0035267 NuA4 histone acetyltransferase complex` is a MYST-family
  paralog/complex mismatch. The NuA4 donor set is KAT5/TIP60-like, whereas
  budding yeast Sas2 is in the distinct SAS acetyltransferase complex.
- Searched PubMed for 2023-2026 papers with `Sas2`, `SAS2`, or `SAS-I` in the
  title/abstract together with yeast or Saccharomyces and found no direct new
  papers. A broader web search likewise found no direct 2023-2026 Sas2/SAS-I
  primary paper beyond PMID:37968396, the broad 2023 Nature yeast interactome
  study already represented in the review.

## 2026-10-01 current-GOA refresh

- Re-ran `just fetch-gene yeast SAS2 --force` and `just fetch-gene-pmids yeast
  SAS2`. Live GOA now contains 25 rows. The refresh added three IntAct
  `GO:0005515 protein binding` rows, a ComplexPortal `GO:0033255 SAS
  acetyltransferase complex` row from PMID:11731480, and a UniProt
  `GO:0061733 protein-lysine-acetyltransferase activity` row from PMID:22020126.
- Preserved seven source rows that are no longer live in current GOA as
  `retired: true`: six broad UniProt keyword IEAs from `GO_REF:0000043`
  (`GO:0006325`, `GO:0006351`, `GO:0008270`, `GO:0016740`, `GO:0016746`,
  `GO:0046872`) and the old BioGRID PMID:16554755 protein-binding row.
- Read the cached PMID:11731480 and PMID:22020126 records while reviewing the
  new rows. The additional Sas4 and Cac1/Rlf2 interactions from PMID:11731480
  are valid physical evidence but remain uninformative as generic protein
  binding; the ComplexPortal SAS acetyltransferase complex row is accepted.
  PMID:22020126 independently supports the broad protein-lysine-acetyltransferase
  activity through the conserved Sas2 active-site autoacetylation requirement.
- Searched again for newer direct SAS2/Sas2/SAS-I/YMR127C/P40963 papers in
  yeast/Saccharomyces through 2026. I did not find a newer direct biochemical,
  localization, or complex-membership paper that changes the 2026-09-29 IBA
  assessment. I fetched PMID:38229233 because it is a 2024 single-cell study of
  IMD2 subtelomeric heterochromatin fluctuations that mentions Sas2-mediated
  H4K16 acetylation as boundary context, but it does not provide new direct
  Sas2 evidence or force a GO annotation change here.

## 2026-10-05 reviewer follow-up

- Re-read `interpro/panther/PTHR10615/PTHR10615-entries.csv` after PR review
  and refined the NuA4 diagnosis: PANTHER places P40963/Sas2 in
  `PTHR10615:SF219` with KAT5/TIP60 proteins and the three `GO:0035267` IBD
  seeds, while Q08649/Esa1 is in `PTHR10615:SF218` and gets its own IBAs from
  `PTN004172926`.
- Kept the `GO:0035267 NuA4 histone acetyltransferase complex` IBA as
  `REMOVE`, but reworded the propagation record to say the remedy is re-placing
  Sas2 toward the KAT8/MOF subfamily or adding an IRD/NOT on the yeast Sas2
  branch for NuA4 complex membership, not merely constraining the existing
  `PTN007449682` KAT5/TIP60 node.
