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
- Corrected the newly seeded `GO:0005515` Q12495 interactor from Sas5 to
  Cac1/Rlf2, the CAF-I largest subunit. The row remains `REMOVE` because generic
  protein binding is uninformative, but its evidence records the SAS-I link to
  CAF-I/Asf1 rather than another SAS acetyltransferase complex subunit.
- Replaced residual title-only `supporting_text` snippets after PR review:
  `PMID:11731479` and `PMID:15788653` now quote informative abstract text,
  the SGD `PMID:27655944` silent-mating-type row is retained by curator
  deference with an `UNVERIFIED` reference review because the local abstract
  does not mention Sas2, and the zinc-binding RCA row now cites the
  bioinformatic zinc-proteome method plus the UniProt C2HC MYST zinc-finger
  feature.

## 2026-10-11 GOA source refresh

- Ran `just fetch-gene yeast SAS2`, then forced a current GOA/UniProt refresh with
  `just fetch-gene yeast SAS2 --force`. The 2026 live GOA feed split several
  IntAct protein-binding rows by supporting entity and added current source rows
  for the SAS4/Cac1 interactions from PMID:11731480, the SAS4 chromatin
  interactome association from PMID:21179020, the ComplexPortal SAS
  acetyltransferase complex annotation from PMID:11731480, and the UniProt
  protein-lysine-acetyltransferase activity annotation from PMID:22020126.
- Marked nine rows that vanished from the current GOA snapshot as `retired:
  true`: six old UniProt keyword rows, the Krogan 2006 IntAct SAS4
  protein-binding row, and two stale Q99314-supported protein-binding rows that
  had been seeded from the pre-force local GOA snapshot. The retirements record
  upstream disappearance only; they do not change the biological interpretation
  of Sas2 as the catalytic SAS-I/SAS acetyltransferase subunit.
- Re-read cached PMID:11731480, PMID:21179020, and PMID:22020126 while resolving
  the new rows. PMID:11731480 is abstract-only in the cache but directly states
  that Sas2 interacts with Cac1 and Asf1 and is present in a nuclear protein
  complex with Sas4 and Sas5. PMID:21179020 has full text cached and supports the
  high-throughput chromatin-associated interactome source. PMID:22020126 is
  abstract-only in the cache but directly reports ySas2 active-site lysine
  autoacetylation and its requirement for acetylation and protein substrate
  binding in vitro.
- `just deep-research-falcon yeast SAS2 --fallback perplexity-lite` could not run
  in this environment because the deep-research provider credentials were absent.
  I searched the current web/PubMed-facing index for 2024-2026 direct
  Sas2/SAS-I primary papers and did not find evidence that changes the September
  IBA review.
- Fetched PMID:38229233 while checking recent Saccharomyces subtelomeric
  heterochromatin papers. The paper uses IMD2 to follow GTP-dependent
  heterochromatin fluctuations and cites Sas2-mediated H4K16 acetylation as
  established boundary context, but it does not provide new direct Sas2
  biochemical, localization, or SAS-complex evidence.
