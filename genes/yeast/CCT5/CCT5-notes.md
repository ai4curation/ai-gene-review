# CCT5 curation notes

## 2026-10-01 current GOA refresh

- Re-fetched CCT5 and kept every historical source assertion while adding the current 2026 InterPro ATP-binding row and the ComplexPortal structural CCT-complex row from PMID:21701561.
- Re-read cached PMID:16762366, PMID:15704212, PMID:21701561, PMID:19536198, and PMID:37968396. The strongest direct activity evidence remains yeast CCT purified through internally tagged CCT3 folding yeast ACT1p and human beta-actin in an ATP-dependent assay. PMID:15704212 supports the eight-subunit CCT1-CCT8 complex composition. PMID:21701561 adds the yeast CCT-actin crystal structure and is appropriate for the current ComplexPortal `part_of GO:0005832` row.
- Checked local PTHR11353 PAINT. The current extract retains PTN004253040 for conserved CCT/TRiC protein folding and PTN000144283 for epsilon-subunit chaperonin-containing T-complex membership, and no longer carries the old `GO:0051082 unfolded protein binding` molecular-function row.
- The 2026 GOA refresh removed the obsolete IBA/IEA/IDA `GO:0051082` rows, the broad `GO:0000166 nucleotide binding` keyword row, the older GO_REF:0000120 ATP-binding row, and two generic EFT2 protein-binding rows from PMID:19536198 and PMID:37968396. I marked these as `retired: true` in the preserved review rather than deleting them.
- Web/PubMed searches for exact yeast CCT5/Cct5/YJR064W mentions in 2025-2026 did not find a newer direct *S. cerevisiae* CCT5 primary paper that would change the GO review.

## 2026-10-01 IBA alignment refresh

- Rebased from `origin/main` and reran `just fetch-gene yeast CCT5 --force`;
  the current 13-row GOA import matched the review.
- Fetched current PTHR11353 PAINT; CCT5 still receives `GO:0006457` protein
  folding from `PTN004253040` and `GO:0005832` chaperonin-containing T-complex
  from the CCT5/epsilon-subunit node `PTN000144283`. Added structured
  `propagation_review` blocks that treat those PAINT nodes, not raw donor
  counts, as the reviewed sources.
- Rechecked 2024-2026 web search results. The 2025 CCT monomer interactome
  paper is human-cell work and the 2025 public yeast TRiC/CCT nuclear dataset
  does not change this CCT5 GO review, so no additional annotations were
  proposed.
