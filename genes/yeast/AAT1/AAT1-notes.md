# AAT1 notes (YKL106W, Q01802)

- Mitochondrial aspartate aminotransferase, EC 2.6.1.1, PLP-dependent class-I aminotransferase; matrix-localised [UniProt:Q01802 "SUBCELLULAR LOCATION: Mitochondrion matrix"].
- Cloning: [PMID:1482685 "AAT1 encodes a 451 amino acid protein with a predicted molecular weight of 51,687, which is likely to be the yeast mitochondrial AspAT."]
- Minor contributor to aspartate synthesis: [PMID:33397945 "Loss of Aat1p reduced [U-13C]-aspartate modestly, whereas synthesis of [U-13C]-aspartate was almost completely abolished in aat2Δ cells"]
- Shuttle / respiration: [PMID:22010850 "complete inactivation of the mitochondrial aspartate aminotransferase (Aat1)"]; [PMID:22010850 "deletion of the AAT1 gene in a wild-type strain caused respiratory deficiency and disruption of iron homoeostasis"]; acetylated [PMID:22010850 "Aat1 is acetylated in wild-type mitochondria"].

## Curation observations
- YeastPathways RCA places the AspAT reaction in the cytosol for both isozymes; the 7 cytosol RCA rows on AAT1 were REMOVED (Aat1 is mitochondrial).
- RCA BP rows for asparagine biosynthesis/degradation, homoserine biosynthesis and threonine metabolism are precursor-supply inheritance (MARK_AS_OVER_ANNOTATED).


## 2026-10-26 comparative annotation audit

Reviewed all 41 existing rows and the core-function synthesis for yeast/AAT1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'MODIFY': 12, 'ACCEPT': 17, 'REMOVE': 7, 'KEEP_AS_NON_CORE': 5}.

Aat1 catalysis and mitochondrial localization are supported by PMID:1482685 and PMID:22010850. The latter reports that “deletion of the AAT1 gene in a wild-type strain caused respiratory deficiency”; it also describes secondary enzyme inactivation in frataxin-deficient cells, not a universal direct iron-regulatory activity. PMID:33397945 full text shows a modest loss of newly synthesized aspartate in aat1 cells under the tested nitrogen-starvation conditions. “Minor isozyme” is therefore scoped to this experiment, not all physiology.

The seven cytosol RCA rows describe the imported reaction compartment rather than this mitochondrial isozyme; they remain REMOVE with supported mature matrix localization. General mitochondrion terms refine to matrix; the inherited location remains sound and the PAINT-node metadata records specificity refinement, not failed phylogeny. PLP binding and direct glutamate/2-oxoglutarate metabolism are integral catalytic properties. Existing asparagine and homoserine pathway participation is retained as secondary where the specified reaction route includes AspAT. PMID:36040324 describes the downstream asparagine-catabolic conversion: “Intracellular aspartate is converted to glutamate and oxaloacetate”. Hom3 being the first enzyme *from aspartate* (PMID:10509015) does not exclude AspAT when the reviewed route starts at oxaloacetate. The threonine metabolism row refines to biosynthesis. These are existing pathway assignments, not new claims of dedicated regulation or equal compartment-specific flux.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP403 authentication failure; Perplexity returned HTTP401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-AAT1-research.log` and `aspartate-yeast-AAT1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-AAT1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.


## Root-organelle policy correction (2026-10-25)

Reassessed all 6 mitochondrion (GO:0005739) rows against their original source scope and independent localization evidence. Changed MODIFY to ACCEPT: CLAUDE.md and projects/ORGANELLES.md explicitly retain a supported root organelle rather than replacing it with a subcompartment. The row-specific reasons distinguish direct localization/proteomics from similarity or phylogenetic inference and preserve source-resolution limits. Existing matrix rows, core locations and other annotations are unchanged; no NEW row was added. This supersedes the earlier matrix-replacement decisions, not their historical records. No inferred granularity failure is retained for a biologically sound IBA.
