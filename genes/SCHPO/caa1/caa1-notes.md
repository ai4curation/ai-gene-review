# caa1 (SPAC10F6.13c, UniProt O42652) notes

Cytosolic aspartate aminotransferase (AspAT, EC 2.6.1.1).

- Reaction: [UniProt:O42652 "Reaction=L-aspartate + 2-oxoglutarate = oxaloacetate + L-glutamate;"] (by similarity to S. cerevisiae Aat2, P23542). PLP cofactor, homodimer (by similarity).
- Location: [UniProt:O42652 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16823372}."]; HDA cytosol from the ORFeome GFP screen [PMID:16823372 "we determined the localization of 4,431 proteins"].
- S. pombe genetics (Kitamura 2024, micropublication on maa1/glu1): [PMID:39502420 "The cytoplasmic Caa1 has a major role for this reaction in"] (i.e. aspartate synthesis in S. pombe). Multicopy caa1+ does NOT rescue the maa1/glu1 glutamate requirement on ammonium.
- PANTHER PTHR11879:SF55 (fungal cytosolic AspAT subfamily), same as S. cerevisiae AAT2.
- Budding-yeast ortholog AAT2: [PMID:9288922 "We demonstrate that the gene AAT2 codes for the cytosolic and peroxisomal AAT activities."]; [PMID:33397945 "suggesting that Aat2p is the major enzyme for aspartate synthesis under nitrogen starvation"]. Consistent with caa1 being the major aspartate-forming isozyme.

## GO-CAM
- gomodel:67c10cc400005826 has two caa1 activities (…/67c10cc400005832 and …/684b6c8100000690), both GO:0004069 in cytosol and **part_of GO:0043490 malate-aspartate shuttle**, not GO:0006532. The aspartate_asparagine_metabolism module describes …/684b6c8100000690 as "aspartate biosynthetic process (GO:0006532)" with inputs/outputs; in the model it is part_of the shuttle (has_input/has_output molecule associations present). The GOA IC row is malate-aspartate shuttle.

## Decisions
- Core: GO:0004069 / GO:0006532 / cytosol, same as S. cerevisiae AAT2 review.
- Malate-aspartate shuttle (IC, ARBA) kept as non-core: canonical by analogy, no S. pombe test.
- ISS donor P00508 is chicken *mitochondrial* AspAT; MF transfer fine, BP rows (2-oxoglutarate/glutamate/aspartate metabolic process) are generic -> non-core.


## 2026-10-26 comparative annotation audit

Reviewed all 17 existing rows and the core-function synthesis for SCHPO/caa1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 10, 'MODIFY': 5, 'KEEP_AS_NON_CORE': 2}.

Added and read full PMID:31641022, the direct native study underlying the later Maa1 paper's Caa1 comparison. “Deletion of the entire ORF of caa1” causes aspartate auxotrophy, slow growth and rapamycin sensitivity. The K255R catalytic-site variant is expressed but does not rescue these phenotypes. This independently supports existing Caa1 aspartate synthesis and the PLP-dependent catalytic mechanism. TORC1 responses depend on catalytic competence but the paper does not identify direct TOR binding or a dedicated sensor; no NEW TOR-regulatory annotation is proposed.

PMID:39502420 independently shows that Caa1 does not rescue the tested Maa1/glu1 ammonium-assimilation defect. These native observations replace reliance solely on budding-yeast analogy. The malate-aspartate-shuttle rows remain explicitly inferred and non-core, not newly established by the TORC1 phenotype. Cytoplasm and broad enzyme/process terms refine to supported cytosol and catalytic/BP children. Direct co-substrate metabolism and PLP binding are core chemistry.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP403 authentication failure; Perplexity returned HTTP401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-SCHPO-caa1-research.log` and `aspartate-SCHPO-caa1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-SCHPO-caa1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.
