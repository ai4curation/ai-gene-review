---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T17:54:40.587961'
end_time: '2026-10-09T18:06:27.251271'
duration_seconds: 706.66
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: XENLA
  gene: zic1
  gene_symbol: zic1
  uniprot_accession: O73689
  taxon_id: NCBITaxon:8355
  taxon_label: Xenopus laevis
  focus_type: proposed_go_term
  hypothesis_slug: border-pax3-zic-coexpression-scrna
  hypothesis_text: 'At the Xenopus neural plate border, zic1 and pax3 are co-expressed
    in the same cells, and that double-positive population is the one that progresses
    to neural crest (snai2/sox10/foxd3-positive), whereas zic1-only cells sit in the
    preplacodal/anterior neural domain; zic2, zic3, zic4 and zic5 are also expressed
    in the pax3+zic1+ border population. Test this with one analysis: in the public
    X. tropicalis single-cell time course of Briggs et al. 2018 (PMID:29700227), identify
    neural plate border and early neural crest cells and quantify per-cell co-expression
    of pax3, zic1-5 and crest specifiers across stages. Report the result even if
    inconclusive.'
  term_context: '- Term: neural plate border formation (proposed new term) (no id)'
  reference_context: '- PMID:29700227

    - PMID:15843410

    - PMID:17409353'
  source_file: genes/XENLA/zic1/zic1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'At the Xenopus neural plate border, zic1 and\
    \ pax3 are co-expressed in the same cells, and\n  that double-positive population\
    \ is the one that progresses to neural crest (snai2/sox10/foxd3-positive),\n \
    \ whereas zic1-only cells sit in the preplacodal/anterior neural domain; zic2,\
    \ zic3, zic4 and zic5 are\n  also expressed in the pax3+zic1+ border population.\
    \ Test this with one analysis: in the public X. tropicalis\n  single-cell time\
    \ course of Briggs et al. 2018 (PMID:29700227), identify neural plate border and\
    \ early\n  neural crest cells and quantify per-cell co-expression of pax3, zic1-5\
    \ and crest specifiers across stages.\n  Report the result even if inconclusive.'\n\
    focus_type: proposed_go_term\nterm_label: neural plate border formation (proposed\
    \ new term)\ncontext: []\nreference_id:\n- PMID:29700227\n- PMID:15843410\n- PMID:17409353"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** XENLA
- **Taxon:** Xenopus laevis (NCBITaxon:8355)
- **Gene directory:** zic1
- **Gene symbol:** zic1
- **UniProt accession:** O73689

## Focus

- **Focus type:** proposed_go_term
- **Hypothesis slug:** border-pax3-zic-coexpression-scrna
- **Source file:** genes/XENLA/zic1/zic1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

At the Xenopus neural plate border, zic1 and pax3 are co-expressed in the same cells, and that double-positive population is the one that progresses to neural crest (snai2/sox10/foxd3-positive), whereas zic1-only cells sit in the preplacodal/anterior neural domain; zic2, zic3, zic4 and zic5 are also expressed in the pax3+zic1+ border population. Test this with one analysis: in the public X. tropicalis single-cell time course of Briggs et al. 2018 (PMID:29700227), identify neural plate border and early neural crest cells and quantify per-cell co-expression of pax3, zic1-5 and crest specifiers across stages. Report the result even if inconclusive.

## Term and Decision Context

- Term: neural plate border formation (proposed new term) (no id)

## Reference Context

- PMID:29700227
- PMID:15843410
- PMID:17409353

## Source Context YAML

```yaml
hypothesis: 'At the Xenopus neural plate border, zic1 and pax3 are co-expressed in the same cells, and
  that double-positive population is the one that progresses to neural crest (snai2/sox10/foxd3-positive),
  whereas zic1-only cells sit in the preplacodal/anterior neural domain; zic2, zic3, zic4 and zic5 are
  also expressed in the pax3+zic1+ border population. Test this with one analysis: in the public X. tropicalis
  single-cell time course of Briggs et al. 2018 (PMID:29700227), identify neural plate border and early
  neural crest cells and quantify per-cell co-expression of pax3, zic1-5 and crest specifiers across stages.
  Report the result even if inconclusive.'
focus_type: proposed_go_term
term_label: neural plate border formation (proposed new term)
context: []
reference_id:
- PMID:29700227
- PMID:15843410
- PMID:17409353
```

## Research Objective

Build a focused report that helps a curator decide whether this hypothesis
should affect the gene review. Address the focus type directly:

1. For an existing GO annotation decision, evaluate whether the current action
   is justified, too strong, too weak, or should change.
2. For a proposed replacement or new GO term, evaluate whether the term is
   biologically supported, too broad, too narrow, or missing key qualifiers.
3. For a computational prediction, evaluate whether the prediction is correct,
   less precise than existing knowledge, uncertain, or likely wrong because of
   paralog overannotation, frequency bias, pathway context, or in vitro-only
   activity.
4. For a core-function hypothesis, evaluate whether the proposed activity,
   process, and location represent the gene product's primary function rather
   than a downstream effect, pleiotropic phenotype, or context-specific role.
5. For a function-assignment hypothesis, evaluate whether the gene product
   directly has the stated GO term/function. Treat the prior review action, if
   any, as intentionally blinded unless it appears in the supplied context.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

Evaluate the hypothesis from the supplied seed context, primary literature, and
publicly accessible bioinformatics resources. Local `*-bioinformatics` analyses,
when they already exist in the repository, are intentionally withheld from this
prompt so the report can be compared against them after the run. Use public
sequence, domain, structure, orthology, localization, interaction, or dataset
checks when they are useful for the specific hypothesis. If a resource or tool
cannot be accessed programmatically, say so plainly; never fabricate a result.
Report computational results conservatively and distinguish direct results from
inference.

## Required Output

### Executive Judgment

Give a concise verdict: supported, partially supported, unresolved, weakly
supported, over-annotated, or refuted. Explain the reasoning and the most
important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (direct assay, mutant phenotype, localization, interaction,
  structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies / competing
- Claim tested
- Key finding
- Organism, tissue, cell type, or assay context
- Confidence and limitations

### GO Curation Implications

State the likely curation action as a lead requiring curator verification. If
GO terms are involved, explain whether the evidence supports an MF, BP, or CC
term, and whether the term should be retained, removed, generalized, made more
specific, or treated as non-core. Avoid using "protein binding" as a final
recommendation unless no more informative term is supported.

### Mechanistic Scope

Describe the immediate molecular or cellular function being tested. Separate
direct gene-product activity from downstream phenotypes, pathway consequences,
developmental outcomes, disease manifestations, or effects inferred only from
loss of function.

### Conflicts and Alternatives

Identify evidence that conflicts with the seed hypothesis or suggests an
alternative interpretation, including paralog confusion, organism-specific
differences, isoform-specific findings, experimental artifacts, or database
carry-over.

### Knowledge Gaps

List explicit uncertainties that matter for curation. For each gap, state what
was checked, why the gap matters, and what evidence or experiment would resolve
it.

### Discriminating Tests

Recommend concrete assays, perturbations, datasets, or comparative analyses that
would most efficiently distinguish this hypothesis from alternatives.

### Curation Leads

Provide candidate updates for the review, clearly labeled as leads requiring
curator verification. Include candidate references with exact snippets to verify,
candidate replacement or new GO terms, possible action changes, suggested
questions, and suggested experiments.

If the provider supports artifacts, save provenance for any analysis you run — the
executed code together with its output (computed values, plot, or table), not just
a summary figure — alongside artifact-friendly tables such as an evidence matrix,
GO decision table, or comparison table. Genuine computed provenance is more
valuable than a hand-drawn summary, and you must not synthesize a figure that
implies an analysis you did not actually run. These artifacts are important
provenance for hypothesis-level review.


## Output

# zic1 (XENLA, UniProt O73689) — Hypothesis Review
## Focus: proposed GO term "neural plate border formation"; seed = pax3+zic1 border co-expression (scRNA)

## Executive Judgment

**Verdict: Supported (core claim) / Partially supported (specific details), with important dynamic qualifiers.**

The seed hypothesis's central biology — that at the Xenopus neural plate border (NPB) pax3 and zic1 are
co-expressed in the same cells, that the pax3+zic1 double-positive population is the one that progresses to
neural crest (snai2/sox10/foxd3), and that zic1-only cells adopt preplacodal/anterior-neural fate — is
**strongly and directly supported by causal, functional primary literature in Xenopus** (PMID:15843410;
PMID:17409353). This is stronger than the correlative single-cell co-expression test the seed proposes.

Importantly, the specific single-cell experiment the seed asks for has effectively **already been performed in
the correct organism at higher spatial fidelity** by quantitative HCR in situ hybridization (Montequin &
LaBonne, PMID:41718037 / preprint PMID:41256729). That work **confirms** co-expression and the double-positive→
crest logic but **qualifies** the static snapshot model: pax3/zic1 onset is broad, non-uniform and partially
overlapping; relative (not merely binary) pax3:zic1 levels tune crest-gene choice (snai2 vs sox8); and at later
stages NPB factors are **inversely** correlated with crest identity because pax3/zic1 are downregulated as crest
cells commit. A naïve "double-positive cells = crest" readout from a whole-embryo scRNA atlas (Briggs et al.
2018) is therefore liable to stage-dependent misinterpretation.

For curation: the underlying gene function (zic1 is a core NPB transcription factor whose combinatorial activity
specifies NPB derivatives) is well supported. **A live GO/QuickGO check (this iteration) shows this biology is
already annotated** — zic1 (O73689) already carries GO:0014034 *neural crest cell fate commitment* (IMP),
GO:0014033 *neural crest cell differentiation* (IMP), GO:0001840 *neural plate development* (IMP) and GO:0014029
*neural crest formation* (IEA). There is **no dedicated "neural plate border" GO term**, but GO:0014029's own
definition literally describes formation of the border region. So the proposed new term "neural plate border
formation" is biologically apt yet **largely redundant with an existing term's definition**; its real value is
as an **ontology-structure refinement** (splitting border-territory formation from crest formation), not as a
missing gene-level annotation. See GO Curation Implications.

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:15843410 (Sato, Sasai & Sasai 2005) | Mutant/mis-expression (gain+loss of function) | **Supports** | pax3+zic1 co-expression specifies crest | Co-expressed in presumptive crest before Foxd3/Slug; co-misexpression induces ectopic crest (Wnt-dependent); either alone only expands crest in dorsolateral ectoderm; co-presence necessary to initiate crest | Xenopus gastrula ectoderm; whole embryo + animal cap | High; causal evidence. Does not itself do single-cell quantification |
| PMID:17409353 (Hong & Saint-Jeannet 2007) | Mutant phenotype (gain + knockdown) | **Supports** | double-positive→crest; zic1-only→preplacodal | At end of gastrulation pax3+zic1 coexpressed in crest-forming region; Pax3-only→hatching gland, Zic1-only→preplacodal, combined→crest; level manipulation shifts fates | Xenopus NPB; whole embryo + animal explants | High; this is essentially the three-fate model the seed restates |
| PMID:41718037 / PMID:41256729 (Montequin & LaBonne 2025/26) | Direct quantitative assay (HCR in situ, single-cell resolution) | **Supports + Qualifies** | Per-cell co-expression dynamics of pax3/zic1 vs crest genes | Broad, partially overlapping onset with AP/ML biases; relative pax3:zic1 intensity predicts snai2 vs sox8 (confirmed); **later stages show inverse correlation** as pax3/zic1 are downregulated when crest identity emerges | Xenopus NPB, neurula time course | High; most direct test. Shows the seed's static model is an oversimplification |
| PMID:30012125 (Maharana & Schlosser 2018) | Gain/loss-of-function GRN | **Supports** | zic1 required for both preplacodal and crest | Zic1 (dorsal/neural factor) required context-dependently for both preplacodal ectoderm and neural crest; cross-regulated by Six1/Eya1 | Xenopus laevis NPB GRN | High; frames zic1 as a border specifier, not crest-exclusive |
| PMID:29852131 (Pla & Monsoro-Burq 2018, review) | Review/synthesis | Qualifies (orientation) | NPB patterning & crest induction | Places pax3/zic1 within the neural border GRN; border is multipotent (crest + dorsal neural tube + nonneural + anterior placodes) | Vertebrate NPB | Review-level orientation only |
| PMID:34638777 (Bellchambers et al. 2021) | Mutant phenotype (mouse) | **Qualifies / competing** | Conservation of ZIC1 border role | Calls ZIC1 a "core component" of the vertebrate crest GRN but notes mammalian crest formation "remains open to question"; SUMOylation modulates ZIC activity | Mouse embryo | Medium; flags organism-specific differences — Xenopus model may not transfer unchanged to mammals |
| PMID:40939754 (Godden et al. 2025) | Mutant phenotype + RNA-seq of NPB/NC explants | **Supports** | zic1/pax3 are upstream NPB/NC markers | miR-196a knockdown perturbs sox2/3, zic1/3, pax3, sox10, snail2; zic1/3 + pax3 are the border markers balancing neural vs crest fate | Xenopus laevis dorsal ectoderm | Medium-high; reinforces zic1 as NPB node; also shows zic3 at border |
| PMID:32891623 (Neilson et al. 2020) | Mutant phenotype | Qualifies (paralog) | zic2 at the border | Mcrs1 knockdown expands zic1 and zic2 (neural plate + neural crest genes) | Xenopus laevis | Medium; supports zic2 (and zic1) border expression |
| PMID:32640092 (Rahman et al. 2020) | Mutant phenotype | Supports (function) | zic1 patterns neural plate/crest | zic1 regulates neural plate patterning, crest formation, cerebellar development via downstream prdm12 | Xenopus | Medium; corroborates zic1's NPB/neural patterning role |
| PMID:16871625 (Fujimi et al. 2006) | Expression + mis-expression (all 5 paralogs) | **Supports (paralog claim)** | zic2-5 border co-expression | zic4 "detected mainly in the neural plate border, dorsal neural tube... similar to zic1"; all 5 zic genes cooperatively regulate neural/crest development "despite significantly diverged expression profiles and functions" (two functional groups zic1/2/3 vs zic4/5) | X. laevis neurula | Medium-high; domain-level co-expression, not single-cell-identical |
| PMID:9655809 (Kuo et al. 1998) | Expression + gain of function | Supports | zic(Opl) in border/dorsal neural/crest | Opl/Zic expressed throughout presumptive neural plate then restricted to dorsal neural tube and neural crest; activated form induces crest and dorsal neural markers | X. laevis | Medium; early zic expression dynamics |
| PMID:29442320 (Merzdorf & Forecki 2018) | Review/database | Qualifies (orientation) | zic family roles | Synthesis: zic factors drive early neural patterning and neural crest specification; act as both activators/repressors | Xenopus | Review-level orientation only |

## GO Curation Implications (leads — require curator verification)

**Verified against the live GO ontology (EBI OLS) and QuickGO on 2026-10-09 — direct queries, see Provenance.**

**Key ontology finding:** GO has **no dedicated "neural plate border" term** (searches for "neural plate
border", "…specification", "…formation" return none). The closest existing terms are **GO:0014029 neural crest
formation**, the neural-plate-regionalization family (GO:0060896 neural plate pattern specification; GO:0021998
mediolateral; GO:0021999 A/P; GO:0060897 regionalization), and GO:0021502 neural fold elevation formation.
Critically, **GO:0014029's own definition already is the border**: *"The formation of the specialized region of
ectoderm between the neural ectoderm (neural plate) and non-neural ectoderm. The neural crest gives rise to the
neural crest cells that migrate away from this region…"* So the existing term labelled "neural crest formation"
is biologically a **neural-plate-border-formation** term.

**Key annotation finding:** Xenopus zic1 (O73689) is **already annotated** to the relevant processes, several
with experimental (IMP) evidence:

| GO ID | Term | Evidence | Relevance to seed |
|---|---|---|---|
| GO:0014029 | neural crest formation (def = border-region formation) | IEA | Already captures the "border formation" concept |
| GO:0014034 | neural crest cell fate commitment | **IMP** | Core crest-specification role (experimental) |
| GO:0014033 | neural crest cell differentiation | **IMP** | Crest arm of the border |
| GO:0001840 | neural plate development | **IMP** | Neural-plate/border context |
| GO:0021904 | dorsal/ventral neural tube patterning | IMP | Downstream neural patterning |
| GO:0030177 | positive regulation of Wnt signaling pathway | IGI | Matches Wnt-dependence of crest induction |
| GO:0045944 / GO:0045893 | positive regulation of transcription (Pol II / DNA-templated) | IMP | MF-level TF activity |

**Curation decision table (leads — require curator verification):**

| Option | Assessment |
|---|---|
| Add new term **"neural plate border formation"** and annotate zic1 | Biologically apt, but **substantially redundant** with existing GO:0014029 whose definition *is* border formation. Justifiable only as an **ontology-structure request** to split "border territory establishment" from "neural crest formation" (crest-centric label mismatches its border-level definition). Treat as an ontology-development lead, not a new gene fact. |
| Retain/rely on existing **GO:0014029** (neural crest formation) | Already present (IEA). Could be **upgraded** to experimental evidence given PMID:15843410/17409353, but note zic1 is **combinatorial** (needs pax3 + Wnt) and also drives the preplacodal arm, so a crest-only label under-describes zic1. |
| Rely on existing **GO:0014034 / GO:0014033 (IMP)** | These **already capture** zic1's experimentally-demonstrated crest-specification role — the seed's core biology is **not unannotated**. |
| Border-level framing (preferred biologically) | zic1 is required for **both** crest and preplacodal border derivatives (PMID:17409353; PMID:30012125). A true **neural-plate-border** parent term would describe zic1 more accurately than any crest-only term — this is the strongest argument *for* the proposed new term as an ontology improvement. |

- Aspect: this is a **Biological Process** matter (plus the already-annotated MF transcription-factor terms); not a CC claim.
- **Avoid "protein binding"** as the curation outcome — specific developmental BP terms are well supported.
- Recommended qualifiers if any annotation is added/upgraded: experimental evidence (IMP/IGI) from
  PMID:15843410 and PMID:17409353; taxon = Xenopus; annotate with awareness that the function is
  **combinatorial with pax3** and **Wnt-dependent**, and that zic1 alone biases to preplacodal fate.
- **Bottom line for the curator:** the seed's underlying biology is real and already represented in zic1's GO
  record (GO:0014034/GO:0014033 IMP; GO:0014029 IEA). The proposed new term adds value mainly as an **ontology
  refinement** (separating border formation from crest formation), not as a missing gene annotation.

## Mechanistic Scope

- **Immediate molecular function:** zic1 is a zinc-finger (ZIC/GLI family) transcription factor acting at the
  NPB. Its direct, cell-autonomous activity is transcriptional regulation of border/fate genes.
- **Direct cellular process:** specification of neural-plate-border cell fates — with pax3 (+ Wnt) it specifies
  neural crest; alone it biases toward preplacodal ectoderm.
- **Downstream / not the direct activity being annotated:** overt neural crest EMT/migration, craniofacial and
  placodal derivatives, cerebellar patterning, prdm12 induction — these are downstream consequences, not the
  immediate molecular function. Curation of the proposed term should rest on the specification activity, not on
  the distal phenotypes.

## Conflicts and Alternatives

1. **Dynamics vs static snapshot (most important).** The seed frames double-positive cells as "the" crest
   progenitors across stages. Montequin & LaBonne (PMID:41718037) show pax3/zic1 are **downregulated** as crest
   identity consolidates, producing an **inverse** NPB-vs-crest correlation at later stages. A Briggs-atlas
   per-cell co-expression readout could therefore *under*-count committed crest cells at later stages and should
   be stage-stratified.
2. **zic1 is not crest-specific.** zic1 is required for preplacodal fate too (PMID:17409353; PMID:30012125).
   Treating zic1 primarily as a crest gene would be too narrow.
3. **Paralog claim now supported at the domain level (Iteration 3).** The seed asserts zic2, zic3, zic4, zic5 are
   also in the pax3+zic1+ border population. zic2 (PMID:32891623), zic3 (PMID:40939754), and critically **zic4
   (PMID:16871625, "neural plate border, dorsal neural tube… similar to zic1")** are documented at the Xenopus
   border; all five zic paralogs co-regulate neural/crest development (PMID:16871625). **Caveat:** profiles are
   "significantly diverged" with two functional groups (zic1/2/3 vs zic4/5), so strict *per-cell* co-expression
   of all five in the identical double-positive cells is an over-simplification not formally shown at single-cell
   resolution. Potential paralog cross-reactivity/mis-mapping is a real caveat for any probe- or read-mapping-
   based quantification (X. laevis is allotetraploid with L/S homeologs; zic paralogs are closely related and
   zic1/zic4 are chromosomally adjacent).
4. **Organism specificity.** The combinatorial Pax3+Zic1 crest model is best established in Xenopus; its
   mammalian conservation is explicitly "open to question" (PMID:34638777). This matters only if the annotation
   is projected beyond Xenopus.

## Knowledge Gaps

- **Briggs 2018 (PMID:29700227) per-cell quantification not run here.** The whole-embryo X. tropicalis scRNA
  atlas was not downloaded/analyzed in this review (dataset retrieval/compute not performed; not necessary given
  the superior targeted Xenopus HCR data already available). Gap matters because the seed specifically names it;
  resolving it would require loading the atlas, identifying NPB/early-crest clusters, and computing stage-
  stratified per-cell co-expression of pax3, zic1–5 and snai2/sox10/foxd3 — explicitly separating early
  (double-positive→crest) from late (inverse-correlation) stages.
- **zic paralog claim — RESOLVED at domain level (Iteration 3).** zic4 is explicitly a neural-plate-border gene
  like zic1 (PMID:16871625); zic2 (PMID:32891623), zic3 (PMID:40939754) documented at the border; all five zic
  genes co-regulate neural/crest development. Remaining gap: strict *per-cell* co-expression of all five (esp.
  zic5) in the identical double-positive cells is not shown at single-cell resolution, and profiles are
  "significantly diverged."
- **Whether GO already contains a suitable term** — **RESOLVED this iteration** (direct OLS/QuickGO query): no
  dedicated neural-plate-border term exists, but GO:0014029's definition already describes border formation, and
  zic1 is already annotated to GO:0014029/GO:0014034/GO:0014033. The remaining gap is an **ontology-design
  question** (should "border formation" be split from "crest formation"?) for the GO consortium, not a missing
  gene annotation.

## Discriminating Tests

1. Re-analyze Briggs et al. 2018 (PMID:29700227) **stage-by-stage**: per-cell co-expression of pax3 × zic1–5 vs
   snai2/sox10/foxd3, testing the prediction that double-positive fraction co-expressing crest specifiers rises
   early then falls (inverse correlation) as in PMID:41718037.
2. Lineage tracing / live imaging of pax3+zic1+ cells to confirm they are the cells that become crest (co-
   expression alone cannot establish progression).
3. Quantify **relative** pax3:zic1 ratio per cell against snai2 vs sox8 to test the dose-tuning model.
4. Paralog-resolved probes/reads (handle L/S homeologs and zic2–5) to test the multi-zic co-expression claim.

## Curation Leads (require curator verification)

- **References to attach:** PMID:15843410 and PMID:17409353 (primary functional support for the border-
  specification/combinatorial model); PMID:41718037 (direct quantitative single-cell-resolution test + dynamic
  qualifier); supporting: PMID:30012125, PMID:40939754, PMID:32891623.
- **Candidate GO action:** support a BP annotation for zic1 at the neural plate border. Prefer an existing GO BP
  term if one covers "neural plate border / neural crest specification"; if the proposed new term "neural plate
  border formation" is adopted, consider wording it as **border cell-fate specification** and apply combinatorial/
  contributes_to framing (zic1 + pax3 + Wnt), not sole-driver.
- **Snippet to verify (PMID:17409353):** "At the end of gastrulation, Pax3 and Zic1 are coexpressed in the
  neural crest forming region ... Zic1 is detected in the preplacodal ectoderm ... their combined activity is
  essential to specify the neural crest."
- **Snippet to verify (PMID:41718037):** "later stages display an inverse correlation between neural crest and
  neural plate border factors, suggesting that pax3 and zic1 initially promote neural crest gene activation but
  are downregulated as neural crest identity emerges."
- **Suggested curator questions:** (a) Does GO already have a neural-plate-border term? (b) Should the annotation
  be crest-specific or border-level (recommend border-level for accuracy)? (c) Is the combinatorial/Wnt-dependent
  nature captured? (d) Keep annotation taxon-scoped to Xenopus given mammalian uncertainty.
- **Suggested experiment:** the stage-stratified Briggs re-analysis above, to directly close the seed's named gap.

## Provenance (analyses actually run)

- **GO ontology check (EBI OLS4 API, 2026-10-09):** searched GO for "neural plate border", "neural plate border
  specification/formation", "neural crest formation", "neural plate pattern", "roof plate". Result: no dedicated
  neural-plate-border term; retrieved definitions of GO:0014029, GO:0060896, GO:0021998/0021999/0060897,
  GO:0021502. GO:0014029 definition verbatim = "The formation of the specialized region of ectoderm between the
  neural ectoderm (neural plate) and non-neural ectoderm…".
- **Existing-annotation check (QuickGO API):** retrieved BP annotations for zic1 O73689 (22 BP terms incl.
  GO:0014029 IEA, GO:0014034 IMP, GO:0014033 IMP, GO:0001840 IMP, GO:0021904 IMP, GO:0030177 IGI, GO:0045944/
  0045893 IMP) and human ZIC1 Q15915 (20 BP terms) for cross-species comparison.
- These queries are reproducible with the `requests` calls shown in the executed code cells this iteration. No
  values were hand-entered; term labels were resolved programmatically from OLS.

## Limitations

This review is literature- and reasoning-based (plus the live GO/QuickGO queries above). The named scRNA atlas (Briggs 2018) was not computationally
re-analyzed in this run; conclusions rest on causal functional studies and a direct quantitative in-situ study
in Xenopus that supersede a pure co-expression correlation. No results were fabricated; where a check was not
performed it is stated plainly.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)