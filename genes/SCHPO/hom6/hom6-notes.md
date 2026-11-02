# hom6 (SPBC776.03, UniProt O94671) notes

Homoserine dehydrogenase (EC 1.1.1.3), monofunctional, PTHR43070:SF5.

- [UniProt:O94671 "Reaction=L-homoserine + NADP(+) = L-aspartate 4-semialdehyde + NADPH +"]; also NAD(+) reaction (RHEA:15757); both by similarity to S. cerevisiae Hom6 (P31116).
- [UniProt:O94671 "FUNCTION: Catalyzes the conversion of L-aspartate-beta-semialdehyde (L-"]; homoserine is the threonine/methionine branch point [UniProt:O94671 "point in the pathway as it can either be O-phosphorylated for"].
- S. cerevisiae Hom6: [PMID:11341914 "HSD efficiently reduces aspartate semialdehyde to homoserine (Hse) using either NADH or NADPH"].
- No S. pombe experimental annotation; cytosol only by PomBase IC from GO-CAM 678073a900003175.

## Decisions
- GO:0004022 alcohol dehydrogenase (NAD+) from Rhea2GO of RHEA:15757: MODIFY -> GO:0004412 (checked: GO:0004412 is not is_a GO:0004022; ancestors are oxidoreductase CH-OH/NAD(P) classes). Same as S. cerevisiae HOM6 review.
- Core = GO:0004412 / GO:0009090 / cytosol (same as HOM6 review).


## 2026-10-26 systematic fungal threonine review

Reviewed all 14 rows and the core synthesis for SCHPO/hom6. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'MODIFY': 4, 'ACCEPT': 10}.

The conserved P31116 donor supports dual NADH/NADPH homoserine dehydrogenase chemistry (PMID:11341914/11341915). This is explicit ortholog inference, not native fission-yeast kinetic measurement. The broad alcohol-dehydrogenase and oxidoreductase terms refine to the substrate-specific function; NADP and NAD+ binding are integral and core. Broad amino-acid/aspartate-family biosynthesis refines to the homoserine/threonine/methionine branches; the PAINT node is not alleged to be erroneous. The cytosol assignment remains PomBase curator inference, not a native localization assay manufactured from neighboring enzymes.

The S. cerevisiae Hom6 repair/silencing findings in PMID:39349514 are not automatically transferred as native S. pombe functions. Full PMID:31784357 underlies a reported chromatin-proteomics lead, but its main text does not identify the Hom targets and their exact supplementary hits remain unverified. No NEW chromatin/repair annotation is added.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-SCHPO-hom6-research.log` and `threonine-SCHPO-hom6-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

Live QuickGO definitions checked on 2026-10-26: GO:0004022 explicitly uses NAD+; GO:0004412 explicitly uses NADP+. Homoserine is a primary alcohol, so its NAD-dependent oxidation fits GO:0004022 without implying ethanol metabolism or substrate promiscuity. Both can refine their common broad oxidoreductase ancestor. Retain the NAD-dependent catalytic capacity as core across all four enzymes, while distinguishing directly measured yeast kinetics from conserved inference in other targets. Missing native cofactor comparisons limit claims about physiological preference, not the biological centrality of the supported homoserine reaction. Earlier fungal MODIFY to GO:0004412 erased the cofactor distinction and is superseded. Sources: https://www.ebi.ac.uk/QuickGO/term/GO:0004022 and https://www.ebi.ac.uk/QuickGO/term/GO:0004412 .

Action changes: Row 1 GO:0004022: MODIFY → ACCEPT.

All 14 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
