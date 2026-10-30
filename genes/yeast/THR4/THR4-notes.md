# THR4 (YCR053W, P16120) review notes

## Evidence journal
- Activity depends on THR4 [PMID:8082795 "this activity depends on the presence in the cell of an active form of the THR4 gene"].
- Crystal structure, PLP enzyme, monomer [PMID:11756443 "the pyridoxal 5'-phosphate (PLP)-dependent conversion of O-phosphohomoserine into threonine and inorganic phosphate"; "a PLP-binding domain that covalently anchors the cofactor"].
- Localization: cytoplasm and nucleus from GFP screens [PMID:14562095]; cytoplasm during sporulation [PMID:24390141].
- thr4 homoserine toxicity [PMID:20305002]; serum and in vivo sensitivity [PMID:20305003].

## Pathway observations
- THRESYN-PWY gives "L-homoserine biosynthetic process": removed.
- IBA for threonine synthase has THR4 itself as the only experimental source (a fungal clade node).


## 2026-10-26 systematic fungal threonine review

Reviewed all 24 rows and the core synthesis for yeast/THR4. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'ACCEPT': 18, 'KEEP_AS_NON_CORE': 1, 'MODIFY': 5}.

PMID:8082795 ties threonine formation from O-phosphohomoserine to THR4, while PMID:11756443 directly reports a monomeric PLP-dependent synthase structure; the oligomeric architecture should not be transferred from other PLP families. PLP binding remains core. The broad threonine/amino-acid process and cytoplasm annotations refine to the supported biosynthetic process and cytosol. The homoserine-biosynthesis import is corrected to threonine biosynthesis on actual downstream chemistry, not merely a chosen module boundary.

Full PMID:20305002/20305003 support homoserine-related conditional toxicity and upstream suppression. Their discussions of phosphohomoserine feedback/dephosphorylation and misincorporation are hypotheses, so the summary uses genetic inference rather than asserting a direct quantitative intermediate measurement. Full PMID:39349514 shows threonine-rescuable thr4 silencing defects. Nuclear location is retained without dismissive diffusion speculation; neither rescue nor nuclear signal establishes a specific chromatin catalytic role.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-yeast-THR4-research.log` and `threonine-yeast-THR4-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

The homoserine-biosynthesis row is now REMOVE: established downstream conversion of homoserine to threonine does not form homoserine. PMID:20305003 names the sequential Thr1/Thr4 reactions; PMID:20305002 establishes homoserine toxicity in the blocked route. This does not reject broad biosynthetic participation merely for being upstream: Hom3/Hom2/Hom6 actually catalyze the homoserine-forming route. Thr1 homoserine metabolism remains accepted.

Action changes: Row 22 GO:0009090: MODIFY → REMOVE.

All 24 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
