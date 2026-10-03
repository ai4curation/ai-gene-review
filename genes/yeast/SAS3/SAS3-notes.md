# SAS3 re-review notes

## 2026-09-29 IBA re-review

- Re-read the SAS3 review together with the relevant cached NuA3 literature,
  including PMID:10817755, PMID:12077334, PMID:17157260, PMID:25104842,
  PMID:25473596, and PMID:37968396.
- Checked the PTHR10615 PAINT cache. The broad SAS3 IBA rows for chromatin,
  nucleus, chromatin binding, histone acetyltransferase activity, transcription
  coregulator activity, and regulation of transcription by RNA polymerase II all
  come from `PANTHER:PTN004172926`, a eukaryotic MYST-family node. The NuA3a
  IBA comes from `PANTHER:PTN008308138`, which is seeded by `SGD:S000000148`
  (SAS3) itself; this is expected PAINT behavior, not circular support.
- Searched PubMed and the web for 2023-2026 yeast SAS3/NuA3 papers. Two direct
  S. cerevisiae primary papers were newly cached and added to the review:
  PMID:38914563 for Taf14/Yng1/Sas3 assembly contacts in NuA3 and PMID:41318527
  for cryo-EM structures explaining NuA3 H3K14 substrate recognition.
- Other 2023-2026 PubMed hits were not direct SAS3 evidence: PMID:39299382 is a
  review of H3K36 methylation, PMID:39082211 studies a NuA3 ortholog subunit in
  Beauveria bassiana, and PMID:36864781 focuses on Gcn5 and NuA4 HAT activities.

## 2026-10-01 current GOA refresh

- Refreshed SAS3 from current UniProt/GOA. GOA now carries 36 live rows; six
  newly materialized rows were reviewed: three additional IntAct `GO:0005515`
  rows, two direct UniProt `GO:0061733` rows, and the ComplexPortal
  `GO:1990467` NuA3a row.
- Re-read the newly needed cached abstracts for PMID:10600516 and the relevant
  cached NuA3 publications for PMID:10817755, PMID:12077334, PMID:17157260,
  PMID:25104842, and PMID:25473596. The three new generic protein-binding rows
  report real NuA3 interaction/co-complex evidence but remain uninformative GO
  molecular-function assertions and were removed consistently with the existing
  SAS3 protein-binding rows.
- Retained eight source assertions that are no longer in current GOA with
  `retired: true`: the six old UniProt keyword rows from GO_REF:0000043 and the
  two old generic IntAct rows from PMID:16554755 and PMID:21179020.
- Rechecked the PTHR10615 PAINT export refreshed on 2026-10-01. The current
  IBA rows still resolve to the eukaryotic MYST node
  `PANTHER:PTN004172926` and the fungal NuA3a node
  `PANTHER:PTN008308138`, so the existing PTN-only propagation reviews remain
  aligned with the IBA project.

## PR #3790 H3K14 follow-up

- Replaced the false proposed-new-term entry for "histone H3K14 acetyltransferase
  activity" with a `NEW` annotation to the existing GO term
  `GO:0036408 histone H3K14 acetyltransferase activity`.
- Tightened the core molecular function from generic
  `GO:0004402 histone acetyltransferase activity` to `GO:0036408`, supported by
  direct NuA3 H3K14 enzymology in PMID:41318527 and earlier Yng1-dependent
  NuA3 K14 acetylation evidence in PMID:17157260.
- Corrected the SAS3 current-GOA audit counts from 30 pre-refresh rows to the
  actual 38 rows.
