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

## 2026-10-10 refresh

- Re-fetched `yeast/SAS2`, bringing the review to the current 25 GOA rows and
  adding five current rows for ComplexPortal SAS-I membership, UniProt's
  experimentally supported protein-lysine-acetyltransferase activity, and three
  extra IntAct `GO:0005515 protein binding` rows.
- Kept the standing IBA calls for `PANTHER:PTN007449682`: `GO:0046972 histone
  H4K16 acetyltransferase activity` is a supported inherited KAT8/Sas2 activity,
  while `GO:0035267 NuA4 histone acetyltransferase complex` is a KAT5/TIP60
  complex-membership assertion leaking across MYST paralogs.
- Accepted the new ComplexPortal and UniProt rows, removed the newly added
  generic interaction rows, and added explicit `PTHR10615` PAINT support so the
  accepted and rejected IBA rows both trace to the PAINT node.
- Repeated the newer-paper search. PubMed still finds no direct 2022-2026
  `SAS2`/`Sas2`/`SAS-I` primary paper in *Saccharomyces*; the latest direct
  SAS-I H4K16 paper from a broader H4K16/Sas2 query remains the 2021
  replication-coupled acetylation study, PMID:34014972.
