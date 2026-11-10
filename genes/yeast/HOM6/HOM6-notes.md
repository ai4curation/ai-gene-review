# HOM6 notes (YJR139C, P31116)

- Homoserine dehydrogenase, EC 1.1.1.3; uses NADPH or NADH [PMID:11341914 "HSD efficiently reduces aspartate semialdehyde to homoserine (Hse) using either NADH or NADPH"]; required for Thr/Ile/Met [PMID:11341914 "Fungal homoserine dehydrogenase (HSD) is required for the biosynthesis of threonine, isoleucine and methionine from aspartic acid"].
- Mechanism: [PMID:11341915 "yeast HSD follows an ordered Bi Bi kinetic mechanism, where NAD(P)H must bind the enzyme prior to aspartate semialdehyde (ASA)"].
- Structure (dimer; apo/holo/ternary): [PMID:10700284 "each monomer composed of three regions, the nucleotide-binding region, the dimerization region and the catalytic region"].

## Curation observations
- GO:0004022 alcohol dehydrogenase (NAD+) activity (Rhea RHEA:15757 mapping) -> MODIFY to GO:0004412. Note GO:0004412 is defined with NADP+ only although Hom6 uses both NAD(H) and NADP(H).


## 2026-10-26 systematic fungal threonine review

Reviewed all 37 rows and the core synthesis for yeast/HOM6. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'MODIFY': 7, 'ACCEPT': 29, 'KEEP_AS_NON_CORE': 1}.

Native Hom6 biochemistry is well established: PMID:11341914 explicitly reports dimeric enzyme, efficient reduction with either NADH or NADPH and much weaker reverse activity at physiological assay pH; PMID:11341915 gives ordered binding/release and pro-S hydride transfer. PMID:10700284 independently establishes the folded nucleotide-binding/dimerization/catalytic architecture. Abstract-access limits are stated; explicit positive experimental results and publication-linked UniProt chemistry support the claims. Broad alcohol-dehydrogenase and oxidoreductase terms are refined to homoserine dehydrogenase, rather than declared chemically false. NADP and NAD+ binding are integral, core properties.

Full PMID:39349514 adds genuine chromatin/repair biology absent from the old summary. In W303 reporter assays, exogenous threonine rescues hom3/hom2/thr4 silencing but not hom6. Hom6 E208L and D219L are both threonine auxotrophs yet differ in silencing and damage-response phenotypes. BY-background plasmid-end-joining and MRX double-mutant experiments are distinct assay contexts. Figure7 explicitly says there is no evidence for a direct physical MRX interaction. Neither catalytic mutant rescues the hom6 mrx double-mutant HU phenotype, even though single-mutant responses can separate some metabolic and repair functions. Therefore 'catalysis-independent DNA repair' is not generalized to every phenotype. The nuclear location is retained with current context. No NEW repair catalytic MF/BP is manufactured from necessity or interaction alone; the unresolved biochemical role is posed as a question. PMID:26936955 is earlier target-specific screening evidence, not a license to transfer Gdh1's detailed mechanism.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-yeast-HOM6-research.log` and `threonine-yeast-HOM6-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

Sulfur amino-acid biosynthesis is true participation through the methionine carbon-skeleton pathway. Refinement to methionine biosynthesis reflects a supported specific descendant, not a requirement that this enzyme itself incorporate sulfur.

Live QuickGO definitions checked on 2026-10-26: GO:0004022 explicitly uses NAD+; GO:0004412 explicitly uses NADP+. Homoserine is a primary alcohol, so its NAD-dependent oxidation fits GO:0004022 without implying ethanol metabolism or substrate promiscuity. Both can refine their common broad oxidoreductase ancestor. Retain the NAD-dependent catalytic capacity as core across all four enzymes, while distinguishing directly measured yeast kinetics from conserved inference in other targets. Missing native cofactor comparisons limit claims about physiological preference, not the biological centrality of the supported homoserine reaction. Earlier fungal MODIFY to GO:0004412 erased the cofactor distinction and is superseded. Sources: https://www.ebi.ac.uk/QuickGO/term/GO:0004022 and https://www.ebi.ac.uk/QuickGO/term/GO:0004412 .

Action changes: Row 2 GO:0004022: MODIFY → ACCEPT.

All 37 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
