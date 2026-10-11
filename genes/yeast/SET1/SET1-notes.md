# SET1 Review Notes

## 2026-09-29 IBA and recent-literature re-review

- Re-read the PAINT IBA rows against the cached PTHR45814 data. Both propagated rows,
  `GO:0042800 histone H3K4 methyltransferase activity` and `GO:0048188 Set1C/COMPASS
  complex`, descend from `PANTHER:PTN002505229`, the eukaryotic SETD1 ancestral node in
  `interpro/panther/PTHR45814/PTHR45814-paint.tsv`. The node placement is appropriate:
  P38827 is in the SETD1 subfamily, the IBD seeds include S. cerevisiae SET1 itself plus
  fission yeast, Candida, fly, worm, Dictyostelium, mouse, and human SETD1 evidence, and
  the cached foundational papers establish that budding-yeast Set1 is the catalytic
  Set1C/COMPASS subunit and methylates H3K4.

- Re-read the cached foundational Set1C papers. Miller et al. 2001, Roguev et al. 2001,
  Krogan et al. 2002, Nagy et al. 2002, and Lee et al. 2007 collectively support
  Set1/COMPASS complex membership, H3K4 methyltransferase activity, and
  H2Bub/Swd2-dependent COMPASS regulation [PMID:11687631; PMID:11742990;
  PMID:11805083; PMID:11752412; PMID:18083099].

- Converted all nine collapsed `GO:0005515 protein binding` IPI rows to `REMOVE`.
  The interactions themselves are not being rejected. The direct Set1C rows already
  capture the functional complex-membership assertion, and the generic molecular-function
  term adds no information for the remaining high-throughput or Mec3 interaction rows.

- Searched PubMed for 2023-2026 `Set1`/`COMPASS` yeast papers and cached five newer
  direct papers. Woo et al. 2024 and Oh et al. 2024 refine regulation of H3K4
  methylation through N-terminal acetylation of Set1C subunits and Swd2/Rad6 control.
  Mishra et al. 2025 and Luciano et al. 2026 expand Set1C's non-histone-substrate space
  to Dam1 and Snf2, and Park et al. 2025/2026 demonstrates a Set1-dependent requirement
  for sustained transcription at Leo1-sensitive newly activated loci [PMID:38996018;
  PMID:38702628; PMID:40523001; PMID:42747427; PMID:41344592]. These do not alter the
  existing PAINT call or warrant a new GO assertion in this pass.

## 2026-10-01 current GOA refresh

- Force-refreshed GOA and UniProt after rebasing to current `origin/main`. The active
  SET1 GOA set now has 94 rows and the deterministic seed added 31 exact source rows:
  nine additional IntAct `GO:0005515 protein binding` rows, the direct UniProt nucleus,
  chromosome, and H3K4 trimethyltransferase rows, two ARBA parent rows, and 17 Set1C
  subunit-specific IPI rows for the Miller, Roguev, and Nagy foundational COMPASS
  papers.

- Re-read the cached foundational publications for the refreshed rows. The new
  Set1C/COMPASS complex rows are all direct co-complex evidence and were accepted;
  the additional generic protein-binding rows were removed under the current
  `GO:0005515` policy because they add no functional information beyond complex
  membership; the new broad ARBA `methyltransferase activity` row was kept as
  non-core because SET1 already carries H3K4-specific terms.

- Marked five exact source assertions that disappeared from current GOA as retired:
  the old UniProt-keyword `chromatin organization`, `transferase activity`, and
  `methylation` rows, the old keyword/ARBA-combined `methyltransferase activity`
  parent row, and the stale Krogan et al. generic protein-binding row.
