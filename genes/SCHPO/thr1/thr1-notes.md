# thr1 (SPBC4C3.03, UniProt O43056) notes

Homoserine kinase (EC 2.7.1.39), GHMP kinase, PTHR20861:SF1.

- [UniProt:O43056 "Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+);"]; [UniProt:O43056 "FUNCTION: Commits homoserine to the threonine biosynthesis pathway by"] (by similarity to S. cerevisiae Thr1, P17423).
- HDA cytoplasm, PMID:16823372; IC cytosol from GO-CAM 678073a900003175.
- S. cerevisiae: [PMID:2176637 "Disruption of the THR1 gene results in threonine auxotrophy in yeast."]

## Decisions
- PomBase ISS (from P17423) "L-methionine metabolic process": SGD has no such THR1 annotation (checked genes/yeast/THR1/THR1-goa.tsv). Homoserine kinase competes with the methionine branch rather than participating -> MARK_AS_OVER_ANNOTATED.
- Core = GO:0004413 / GO:0009088 / cytosol, same as THR1 review and GO-CAM.


## 2026-10-26 systematic fungal threonine review

Reviewed all 9 rows and the core synthesis for SCHPO/thr1. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'ACCEPT': 6, 'MODIFY': 2, 'MARK_AS_OVER_ANNOTATED': 1}.

Curated orthology to budding-yeast Thr1 (P17423), the GHMP kinase family and PMID:2176637 support ATP-dependent homoserine phosphorylation. ATP binding is core; broad cytoplasm refines to the already inferred cytosol and threonine metabolism to threonine biosynthesis. Native fission-yeast kinetics are not claimed.

The methionine-process ISS names P17423 as donor. The fungal enzyme partitions homoserine toward threonine, whereas methionine uses homoserine O-acetylation. Shared-substrate competition is insufficient evidence for a methionine-process step, so the existing MARK_AS_OVER_ANNOTATED is retained with source-specific ROLE_CONFLATION metadata. This differs from plant HSK, whose phosphohomoserine product actually supplies both Thr and Met branches. Absence of a donor annotation is not used as evidence against the transfer.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-SCHPO-thr1-research.log` and `threonine-SCHPO-thr1-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

Annotation actions are unchanged; revisions clarify evidence or narrative.

All 9 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
