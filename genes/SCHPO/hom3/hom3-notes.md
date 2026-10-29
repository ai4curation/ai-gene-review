# hom3 (SPBC19F5.04, UniProt O60163) notes

Aspartate kinase (EC 2.7.2.4), monofunctional (no HSD fusion), single aspartokinase in S. pombe (PTHR21499:SF59).

- [UniProt:O60163 "Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;"]; [UniProt:O60163 "FUNCTION: Phosphorylates aspartate, the first step in the biosynthesis"] (by similarity to S. cerevisiae Hom3 P10869).
- Pathways: threonine step 1/5; de novo methionine (homoserine from aspartate step 1/3).
- HDA cytosol, PMID:16823372 (ORFeome).
- S. cerevisiae: [PMID:2892836 "Mutations in HOM3 result in a requirement for threonine and methionine"]; [PMID:6821505 "The gene HOM3 codes for aspartokinase (aspartate kinase; EC 2.7.2.4), the"] first enzyme, feedback-inhibited by threonine.
- No S. pombe enzymology or mutant data in GOA.

## Consistency
- Core = GO:0004072 / GO:0009090 / cytosol, identical to the HOM3 review and to GO-CAM gomodel:678073a900003175 (hom3 in cytosol, part_of GO:0009090).


## 2026-10-26 systematic fungal threonine review

Reviewed all 11 rows and the core synthesis for SCHPO/hom3. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'ACCEPT': 10, 'MODIFY': 1}.

Conserved aspartokinase chemistry is supported by curated P10869 donor inference, fungal family placement, and native budding-yeast biochemical studies PMID:2892836/6821505. PomBase experimental cytosolic localization is retained. Native fission-yeast kinetic regulation is not asserted from yeast threonine feedback alone. Broad amino-acid synthesis refines to the actual homoserine/threonine/methionine branches.

PMID:31784357 full main text was fetched/read as the primary source behind the chromatin-association lead cited in PMID:39349514. Main text does not name Hom3/Hom2/Hom6, and exact supplementary target hits have not been independently verified here. No new nuclear/heterochromatin row or direct silencing mechanism follows from that lead.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-SCHPO-hom3-research.log` and `threonine-SCHPO-hom3-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

Annotation actions are unchanged; revisions clarify evidence or narrative.

All 11 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
