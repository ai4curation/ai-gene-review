# THR1 (YHR025W, P17423) review notes

## Evidence journal
- Purified homoserine kinase, homodimer, gene cloned [PMID:2165904 "the enzyme was purified by four consecutive column chromatographies, monitoring homoserine kinase activity"; "the native enzyme appears to be a homodimer"].
- Pathway step [PMID:20305003 "Homoserine is converted to threonine by the sequential actions of homoserine kinase (Thr1p) and threonine synthase (Thr4p)."].
- Homoserine toxicity in thr1/thr4 [PMID:20305002 "they are dependent on the toxic biosynthetic intermediate homoserine"].
- GHMP kinase family [UniProt:P17423].

## Pathway observations
- THRESYN-PWY superpathway gives "L-homoserine biosynthetic process": removed (THR1 consumes homoserine).
- "L-threonine metabolic process" (InterPro, P4-PWY-1) modified to L-threonine biosynthetic process.
- No direct localization data; cytosol from YeastPathways is accepted as plausible.


## 2026-10-26 systematic fungal threonine review

Reviewed all 20 rows and the core synthesis for yeast/THR1. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'ACCEPT': 17, 'MODIFY': 3}.

Thr1 directly consumes homoserine and ATP to produce O-phosphohomoserine; PMID:2165904 reports cloning and purified native homodimer, and publication-linked UniProt states the reaction. ATP binding is core. Existing GO:0009092 homoserine metabolism is ACCEPT because actual substrate conversion satisfies the definition, irrespective of the module boundary. The imported homoserine-biosynthesis claim is corrected to threonine biosynthesis: consuming homoserine downstream is not producing it. No row is dropped.

Full PMID:20305002 and PMID:20305003 distinguish auxotrophy from conditional intermediate toxicity. Blocking HOM3/HOM6 suppresses thr1 phenotypes; exogenous homoserine is toxic. Proposed protein misincorporation, proteasome effects and particular DNA-damage mechanisms remain hypotheses, not new direct functions. Mouse survival and fungal species contexts are kept separate from core chemistry.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-yeast-THR1-research.log` and `threonine-yeast-THR1-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

The homoserine-biosynthesis row is now REMOVE: established downstream conversion of homoserine to threonine does not form homoserine. PMID:20305003 names the sequential Thr1/Thr4 reactions; PMID:20305002 establishes homoserine toxicity in the blocked route. This does not reject broad biosynthetic participation merely for being upstream: Hom3/Hom2/Hom6 actually catalyze the homoserine-forming route. Thr1 homoserine metabolism remains accepted.

Action changes: Row 19 GO:0009090: MODIFY → REMOVE.

All 20 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
