# RPD3 IBA Re-review Notes

## PAINT / IBA rows

- `GO:0004407 histone deacetylase activity`: current PTHR10625 PAINT places this at `PANTHER:PTN008143312`, a broad class I HDAC node seeded by many experimentally annotated descendants, including budding-yeast RPD3 itself (`SGD:S000005274`) and HOS2 (`SGD:S000003162`). Retained as `ACCEPT` and `NO_FAILURE_CORE`.
- `GO:0031507 heterochromatin formation`: current PAINT places this at `PANTHER:PTN000743059` from fly Rpd3 and human HDAC1/HDAC2. The exact transfer needs yeast-specific wording: Rpd3 is not Sir2 and does not nucleate silent chromatin; Sun and Hampsey showed that "deletion of the SIN3 and RPD3 genes enhances silencing, implying that the Sin3-Rpd3 complex functions to counteract, rather than to establish or maintain, silencing" [PMID:10388812], and Zhou et al. showed Rpd3 directly deacetylates H4K5/H4K12 at boundary regions and characterized "the anti-silencing functions of Rpd3p during the formation of heterochromatin boundaries" [PMID:19372273]. Because the current GO:0031507 definition includes boundary formation, I left the term in place but downgraded it to `KEEP_AS_NON_CORE` with `NO_FAILURE_NON_CORE`.
- `GO:0070210 Rpd3L-Expanded complex`: current PTHR10625 PAINT places this at `PANTHER:PTN000835673`, a fungal node seeded by PomBase `SPBC36.05c`. This is consistent with Rpd3 as the conserved catalytic subunit of Rpd3L/Sin3-type HDAC complexes and remains `ACCEPT` / `NO_FAILURE_CORE`.

## 2025-2026 literature search

PubMed and web searches on 2026-09-28 for `Rpd3`, `Rpd3L`, `RPD3`, `Saccharomyces`, and `yeast` found nine 2025-2026 PubMed records. I cached the four direct budding-yeast primary papers and ignored the plant RPD3-type HDAC reviews, a Histoplasma Rpd3 paper, and the bioRxiv preprint that was superseded by the 2026 Cell Reports paper.

- Dai et al. 2025 found that sucrose-activated Tpk2 "phosphorylates Rpd3L catalytic subunit Rpd3 to inhibit its ability to deacetylate Ada3" and phosphorylates Ash1 to reduce the Rpd3L-SAGA interaction [PMID:40301306].
- Serrano-Quilez et al. 2025 identified "a functional and physical interaction between Mip6 and the histone deacetylase Rpd3" in heat-shock transcriptional memory [PMID:40537058].
- Chong et al. 2026 showed that "the Rpd3L histone deacetylase complex dynamically modulates chromatin state to control replication fork progression and buffer TRCs in Saccharomyces cerevisiae" [PMID:42268949].
- Bhattacharya et al. 2026 showed that Rpd3 "mediates nutrient-dependent chromatin reprogramming that coordinates transcriptional shutdown and global acetylation balance during metabolic transitions" [PMID:42418323].
