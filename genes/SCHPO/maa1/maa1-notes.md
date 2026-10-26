# maa1 (SPBC725.01, UniProt O94320) notes

Mitochondrial aspartate aminotransferase; = classical glu1 (glutamate-requiring) locus.

- Reaction (by similarity to S. cerevisiae Aat1 Q01802): [UniProt:O94320 "Reaction=L-aspartate + 2-oxoglutarate = oxaloacetate + L-glutamate;"]
- Location: [UniProt:O94320 "SUBCELLULAR LOCATION: Mitochondrion matrix"] (ECO:0000269, PMID:16823372); predicted N-terminal transit peptide.
- Kitamura 2024 (full text cached): [PMID:39502420 "maa1 , encoding a mitochondrial aspartate aminotransferase, is the causative"] gene of glu1; glu1-NS176 is an R176 opal nonsense allele, rescued by integrated maa1+ and by sup3-5 suppressor; multicopy yhm2 (mitochondrial 2-oxoglutarate carrier) weakly suppresses; caa1+ does not.
  - Direction: [PMID:39502420 "However, mitochondrial Maa1 has a pivotal role in glutamate synthesis by promoting the reaction in an opposite direction"]; [PMID:39502420 "Since this reaction can proceed in both directions, the same enzyme also supplies glutamate by catalyzing the reverse reaction."]
  - [PMID:39502420 "growth defects in this mutant may be related to glutamate, but not aspartate, shortage."]

## S. pombe-specific difference from S. cerevisiae AAT1 review
- AAT1 review core BP = L-aspartate biosynthetic process (matrix). For maa1 the S. pombe genetics point to the glutamate-forming direction, so core BP chosen = GO:0097054 L-glutamate biosynthetic process (MODIFY of the ISS "glutamate metabolic process" row). IBA L-aspartate catabolic process (same direction) ACCEPTED.
- PomBase GO-CAM 67c10cc400005826 has maa1 part_of GO:0006532 (aspartate biosynthesis) and GO:0043490 (shuttle); the IC GO:0006532 row is kept as non-core.

## Other
- Shuttle (IC/ARBA) non-core: plausible by analogy (S. cerevisiae aat1 respiratory deficiency, PMID:22010850) but untested in S. pombe.


## 2026-10-26 comparative annotation audit

Reviewed all 21 existing rows and the core-function synthesis for SCHPO/maa1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'MODIFY': 8, 'ACCEPT': 10, 'KEEP_AS_NON_CORE': 3}.

Read full PMID:39502420, including the nonsense allele, integrated maa1 rescue, failure of multicopy caa1 rescue and weaker yhm2 suppression. Glutamate/glutamine dependence supports reverse AspAT chemistry supplying glutamate during the tested ammonium-assimilation conditions. These are causal genetic observations; they do not directly measure universal net flux. PMID:31641022 supplies the cytosolic/mitochondrial contrast and direct Caa1 biosynthetic evidence.

The core retains reversible matrix AspAT and glutamate synthesis. Existing aspartate-biosynthetic inference remains secondary rather than being rejected simply because the reverse direction is more prominent in this experiment. Broad glutamate metabolism refines to the supported glutamate-biosynthetic child. Shuttle assignments remain non-core comparative inference. PLP binding and 2-oxoglutarate participation are integral chemistry. Matrix location is supported by curated/localization evidence; broad mitochondrial rows refine to matrix without redefining the original assay.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP403 authentication failure; Perplexity returned HTTP401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-SCHPO-maa1-research.log` and `aspartate-SCHPO-maa1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-SCHPO-maa1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.
