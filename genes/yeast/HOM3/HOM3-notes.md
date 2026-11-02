# HOM3 notes (YER052C, P10869)

- Aspartate kinase, EC 2.7.2.4, first committed step of aspartate pathway [PMID:10509015 "The HOM3 gene of Saccharomyces cerevisiae encodes aspartate kinase, which catalyses the first step in the branched pathway leading to the synthesis of threonine and methionine from aspartate."]
- Kinetics/active site: [PMID:14623312 "several of the targeted amino acids, particularly K18 and H292, have important roles in the enzymatic reaction"].
- Homohexamer, threonine-inhibited: [PMID:15358146 "The homogeneously purified enzyme was inhibited by threonine (K(i) 1.4 mM)"].
- Main flux control point: [PMID:18626862 "the data indicate that the main control is exerted by inhibition of the aspartate kinase"].
- FKBP12 (Fpr1) binds Hom3 and contributes to feedback inhibition: [PMID:9315655 "genetic analyses reveal that FKBP12 is important for this feedback inhibition"].

## Curation observations
- Five GO:0005515 protein binding rows (all Hom3-Fpr1) REMOVED per protein-binding policy; the interaction is real (regulatory, Hom3 is the client).


## 2026-10-26 systematic fungal threonine review

Reviewed all 42 rows and the core synthesis for yeast/HOM3. All original machine annotation fields are preserved; no rows were added or deleted. Current actions: {'MODIFY': 4, 'ACCEPT': 33, 'REMOVE': 5}.

Hom3 is the native yeast monofunctional aspartokinase. PMID:14623312 purified-mutant work directly tests catalytic residues; PMID:10509015 separates substrate-affinity changes from threonine-response mutations. PMID:15358146 explicitly reports a homohexamer and a reversible change of hydrodynamic size on threonine binding, not dissociation into a newly identified oligomer. PMID:9315655 establishes Fpr1 binding and a feedback phenotype, while fpr1 deletion retains wild-type aspartokinase activity: Fpr1 is not an obligatory catalytic subunit. Bare protein-binding rows retain the project REMOVE policy without denying the interactions. No regulator MF is invented on Hom3 merely because it is the target of regulation.

The trunk actually catalyzes reactions supplying homoserine and the threonine/methionine branches. Broad sulfur/amino-acid and threonine-metabolism annotations refine to those specific processes. The cytoplasmic screen refines to already supported cytosol. Full PMID:39349514 Fig2 shows the hom3 deletion rDNA-silencing phenotype is rescued by threonine; this is a metabolic connection, not direct evidence of nuclear localization or a new chromatin catalytic function.

### Access, workflow and validation

Actual per-gene Falcon research with Perplexity-lite fallback ran concurrently with normal publication caching. Both research providers failed authentication/quota checks; no provider report was fabricated. Publication caching succeeded. Logs are `.cache/module-audit-logs/threonine-yeast-HOM3-research.log` and `threonine-yeast-HOM3-publications.log`. Positive claims from abstract-only papers are limited to explicit results or independently publication-linked curated statements; inaccessible detailed evidence is not confidently rejected. Full new source caches and the publisher URL were obtained only through the normal fetcher.

The review and annotation-reviewer skills, independent reviewer consultation, current protein-binding policy and GO term-definition checks were applied. UniProt quotes were backfilled with record sections. Focused strict/term/source validation, rendering, helper-generated Codex histories and original-payload proof are recorded in the threonine-fungal manifests under `.cache/module-audit-logs/`. No module/tracker edits were made.


## PR #5569 source-specific corrective review (2026-10-26)

Replaced duplicated summary/reason prose with enzyme-specific chemistry, provenance and cofactor explanations. Existing nuclear phenotypes remain distinct from metabolic rescue and catalytic activity; organelle assertions and all original machine fields are preserved.

Sulfur amino-acid biosynthesis is true participation through the methionine carbon-skeleton pathway. Refinement to methionine biosynthesis reflects a supported specific descendant, not a requirement that this enzyme itself incorporate sulfur.

Annotation actions are unchanged; revisions clarify evidence or narrative.

All 42 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.
