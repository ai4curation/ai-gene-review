# RPD3 IBA Re-review Notes

## PAINT / IBA rows

- `GO:0004407 histone deacetylase activity`: current PTHR10625 PAINT places this at `PANTHER:PTN008143312`, a broad class I HDAC node seeded by many experimentally annotated descendants, including budding-yeast RPD3 itself (`SGD:S000005274`) and HOS2 (`SGD:S000003162`). Retained as `ACCEPT` and `NO_FAILURE_CORE`.
- `GO:0031507 heterochromatin formation`: current PAINT places this at `PANTHER:PTN000743059` from fly Rpd3 and human HDAC1/HDAC2. The transfer crosses a regulatory-sign boundary in budding yeast: Rpd3 is not Sir2 and does not nucleate silent chromatin; Sun and Hampsey showed that "deletion of the SIN3 and RPD3 genes enhances silencing, implying that the Sin3-Rpd3 complex functions to counteract, rather than to establish or maintain, silencing" [PMID:10388812], and Zhou et al. showed Rpd3 directly deacetylates H4K5/H4K12 at boundary regions and characterized "the anti-silencing functions of Rpd3p during the formation of heterochromatin boundaries" [PMID:19372273]. I changed the row to `MODIFY` with `GO:0033696 heterochromatin boundary formation` and `PROPAGATION_BAD` / `REGULATORY_SIGN_INVERSION`.
- `GO:0070210 Rpd3L-Expanded complex`: current PTHR10625 PAINT places this at `PANTHER:PTN000835673`, a fungal node seeded by PomBase `SPBC36.05c`. This is consistent with Rpd3 as the conserved catalytic subunit of Rpd3L/Sin3-type HDAC complexes and remains `ACCEPT` / `NO_FAILURE_CORE`.

## 2025-2026 literature search

PubMed and web searches on 2026-09-28 for `Rpd3`, `Rpd3L`, `RPD3`, `Saccharomyces`, and `yeast` found nine 2025-2026 PubMed records. I cached the four direct budding-yeast primary papers and ignored the plant RPD3-type HDAC reviews, a Histoplasma Rpd3 paper, and the bioRxiv preprint that was superseded by the 2026 Cell Reports paper.

- Dai et al. 2025 found that sucrose-activated Tpk2 "phosphorylates Rpd3L catalytic subunit Rpd3 to inhibit its ability to deacetylate Ada3" and phosphorylates Ash1 to reduce the Rpd3L-SAGA interaction [PMID:40301306].
- Serrano-Quilez et al. 2025 identified "a functional and physical interaction between Mip6 and the histone deacetylase Rpd3" in heat-shock transcriptional memory [PMID:40537058].
- Chong et al. 2026 showed that "the Rpd3L histone deacetylase complex dynamically modulates chromatin state to control replication fork progression and buffer TRCs in Saccharomyces cerevisiae" [PMID:42268949].
- Bhattacharya et al. 2026 showed that Rpd3 "mediates nutrient-dependent chromatin reprogramming that coordinates transcriptional shutdown and global acetylation balance during metabolic transitions" [PMID:42418323].
- A 2026-10-01 PubMed/web update found Zhao et al. 2026, which solved Rpd3L structures on mono- and di-nucleosome substrates and showed that "dual nucleosome engagement selectively enhances Rpd3L activity and broadens substrate specificity" [PMID:42152683].

## Current GOA refresh on 2026-10-01

- Forced the RPD3 UniProt/GOA refresh and accepted all seven newly seeded rows: an SGD IMP row for `GO:0000727` break-induced replication from a 2025 genome-wide BIR screen; InterPro `GO:0004407`; `GO:0032221 Rpd3S complex` from the Rpd3/Sin3 small-complex proteomics reanalysis; `GO:0033698 Rpd3L complex` from the 2023 Rpd3L cryo-EM structure; the broad ARBA `GO:0051052 regulation of DNA metabolic process` row; `GO:0070211 Snt2C complex`; and the direct `GO:0141221 histone deacetylase activity, hydrolytic mechanism` row from the Rpd3 ER-motif mutagenesis paper.
- Marked 56 old rows as `retired: true` because their exact source assertions are absent from current GOA. These are five stale automatic parent rows, nine old unqualified duplicate transcription-regulation rows from `PMID:20398213`/`PMID:24358376`, and 42 stale generic protein-binding rows from older proteomics snapshots.
- Left the three current IBA rows unchanged biologically: `GO:0004407` and `GO:0070210` remain sound `NO_FAILURE_CORE` transfers from `PTN008143312` and `PTN000835673`, while the `PTN000743059` `GO:0031507 heterochromatin formation` row remains a `MODIFY` to heterochromatin boundary formation because the PAINT node crosses a regulatory-sign boundary in budding yeast.

## PR #3787 follow-up

- Rewrote the `GO:0000727` break-induced replication IMP row to cite the
  cached RPD3/Rpd3L-specific BIR prose from PMID:41398407 and changed its
  action to `KEEP_AS_NON_CORE`.
- Changed the broad ARBA `GO:0051052 regulation of DNA metabolic process` row
  to `KEEP_AS_NON_CORE` and trimmed its evidence back to the TRC/replication-fork
  Rpd3L paper.
- Normalized the RPD3 gene and IBA_REVIEW history actors from `claude-code` to
  `codex` to match the agent and commit provenance.
- Corrected `rpd3-current-goa.yaml` after those two action flips: final action
  totals are now ACCEPT 95 and KEEP_AS_NON_CORE 7, and both changed rows record
  `after: KEEP_AS_NON_CORE`.
