# ALT1 notes (P52893, YLR089C)

- Mitochondrial matrix alanine aminotransferase [UniProt:P52893 "Reaction=L-alanine + 2-oxoglutarate = pyruvate + L-glutamate;"; "SUBCELLULAR LOCATION: Mitochondrion matrix"].
- Sole route of alanine synthesis and catabolism on respiratory carbon [PMID:19396236 "Alt1p constitutes the sole pathway for alanine biosynthesis and catabolism"]; catabolic under fermentation [PMID:19396236 "under fermentative conditions, it plays a catabolic role"].
- Ping-pong kinetics, PLP Schiff base, dimer [PMID:29867852 "ScAlt1 Displays a Kinetic Ping-Pong Mechanism Typical of Transaminases"]; paralog Alt2 cytosolic and inactive as ALT [PMID:29867852 "ScAlt1 is in the mitochondria, while ScAlt2 is cytosolic"].
- Mitochondrion IDA (PMID:11502169) abstract does not name Alt1; deferred to curator (UniProt cites it for matrix location).
- Module note: ALT1 is assigned to aspartate_asparagine_metabolism but its reaction is alanine/2-OG; it is an alanine-metabolism enzyme, not an Asp/Asn enzyme.


## 2026-10-26 comparative annotation audit

Reviewed all 18 existing rows and the core-function synthesis for yeast/ALT1; no rows were added or dropped. Original GO terms, evidence codes, source identifiers and all other machine fields are preserved. Actions: {'ACCEPT': 11, 'MODIFY': 7}.

PMID:19396236 explicitly distinguishes respiratory and fermentative growth: Alt1 supports both alanine synthesis and catabolism during respiratory growth, whereas fermentative alanine synthesis mainly uses another route. PMID:23049841 and PMID:29867852 full texts separate active Alt1 from Alt2 with no detected alanine-transaminase activity; “inactive” is not extended to every hypothetical Alt2 function. The latter supports PLP-dependent catalytic chemistry and mitochondrial Alt1 versus cytosolic Alt2.

Mitochondrial rows refine to the curated matrix location, without pretending each proteomics source resolves submitochondrial topology. The broad alanine-biosynthesis annotation refines to L-alanine biosynthesis. PLP binding is accepted as integral to core catalysis. No claim is made that ALT1 is the sole alanine-producing reaction under all carbon sources.

### Research access and provenance

An actual per-gene Falcon attempt with Perplexity-lite fallback ran in parallel with normal publication caching. Falcon returned HTTP 403 authentication failure; Perplexity returned HTTP 401 insufficient quota. No provider report was fabricated. Manual evidence review is recorded here; research and publication logs are `.cache/module-audit-logs/aspartate-yeast-ALT1-research.log` and `aspartate-yeast-ALT1-publications.log`. Normal publication fetching succeeded. Cached abstracts are used only for explicit reported findings; unverified target-specific experiments are not confidently rejected.

The annotation-reviewer workflow and current bare-protein-binding policy were applied. No GOA file is used as evidence. Existing sound source quotations were preserved, new quotations were checked against cached source text, and UniProt record sections were backfilled by the helper. Gene summaries are standalone biology. Histories use the helper with explicit Codex actor/tool; focused strict/term/source validation and HTML rendering are logged under `.cache/module-audit-logs/aspartate-yeast-ALT1-*`. Final results and machine-payload proof are in the panel validation/payload manifests.


## Root-organelle policy correction (2026-10-25)

Reassessed all 5 mitochondrion (GO:0005739) rows against their original source scope and independent localization evidence. Changed MODIFY to ACCEPT: CLAUDE.md and projects/ORGANELLES.md explicitly retain a supported root organelle rather than replacing it with a subcompartment. The row-specific reasons distinguish direct localization/proteomics from similarity or phylogenetic inference and preserve source-resolution limits. Existing matrix rows, core locations and other annotations are unchanged; no NEW row was added. This supersedes the earlier matrix-replacement decisions, not their historical records. No inferred granularity failure is retained for a biologically sound IBA.


## PR #5568 follow-up, 2026-10-26

Repaired authored citation spacing and fused numeric prose while preserving original annotation payloads, every action, raw UniProt/GOA records and all existing supporting quotations. Source-cited passages in notes were protected from rewriting.
