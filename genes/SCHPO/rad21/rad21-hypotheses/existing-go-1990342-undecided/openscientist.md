---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T06:25:56.262368'
end_time: '2026-09-01T06:47:33.285453'
duration_seconds: 1297.02
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: rad21
  gene_symbol: rad21
  uniprot_accession: P30776
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: existing_go_annotation_decision
  hypothesis_slug: existing-go-1990342-undecided
  hypothesis_text: 'The existing rad21 GO annotation to heterochromatin island (GO:1990342)
    should receive review action UNDECIDED. Current rationale: This is an experimental
    IDA annotation from a reliable curator, but the relevant full text is unavailable
    and the abstract establishes the heterochromatin islands without identifying Rad21.
    Retain the annotation while deferring judgment rather than accepting or rejecting
    it from incomplete evidence.'
  term_context: '- Term: heterochromatin island (GO:1990342)

    - Evidence type: IDA

    - Original reference: PMID:22144463

    - Current review action: UNDECIDED

    - Review summary: Rad21/cohesin localizes to facultative heterochromatin islands
    that form over meiotic genes according to the curator annotation. The cached paper
    is abstract-only and does not mention Rad21, so the specific localization cannot
    be independently checked here.

    - Review reason: This is an experimental IDA annotation from a reliable curator,
    but the relevant full text is unavailable and the abstract establishes the heterochromatin
    islands without identifying Rad21. Retain the annotation while deferring judgment
    rather than accepting or rejecting it from incomplete evidence.'
  reference_context: '- PMID:22144463'
  source_file: genes/SCHPO/rad21/rad21-ai-review.yaml
  source_selector: existing_annotations[19]
  source_context_yaml: "term:\n  id: GO:1990342\n  label: heterochromatin island\n\
    evidence_type: IDA\noriginal_reference_id: PMID:22144463\nqualifier: is_active_in\n\
    review:\n  summary: Rad21/cohesin localizes to facultative heterochromatin islands\
    \ that form over meiotic genes\n    according to the curator annotation. The cached\
    \ paper is abstract-only and does not mention Rad21,\n    so the specific localization\
    \ cannot be independently checked here.\n  action: UNDECIDED\n  reason: This is\
    \ an experimental IDA annotation from a reliable curator, but the relevant full\
    \ text is\n    unavailable and the abstract establishes the heterochromatin islands\
    \ without identifying Rad21. Retain\n    the annotation while deferring judgment\
    \ rather than accepting or rejecting it from incomplete evidence.\n  supported_by:\n\
    \  - reference_id: PMID:22144463\n    supporting_text: facultative heterochromatin\n\
    \    reference_section_type: ABSTRACT"
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
citation_count: 7
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: evidence_matrix_rad21_GO1990342.csv
  path: openscientist_artifacts/evidence_matrix_rad21_GO1990342.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix rad21 GO1990342
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
- filename: go_decision_table_rad21.csv
  path: openscientist_artifacts/go_decision_table_rad21.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table rad21
- filename: island_genes_from_PMID22144463.csv
  path: openscientist_artifacts/island_genes_from_PMID22144463.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist island genes from PMID22144463
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** rad21
- **Gene symbol:** rad21
- **UniProt accession:** P30776

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** existing-go-1990342-undecided
- **Source file:** genes/SCHPO/rad21/rad21-ai-review.yaml
- **Source selector:** existing_annotations[19]

## Seed Hypothesis

The existing rad21 GO annotation to heterochromatin island (GO:1990342) should receive review action UNDECIDED. Current rationale: This is an experimental IDA annotation from a reliable curator, but the relevant full text is unavailable and the abstract establishes the heterochromatin islands without identifying Rad21. Retain the annotation while deferring judgment rather than accepting or rejecting it from incomplete evidence.

## Term and Decision Context

- Term: heterochromatin island (GO:1990342)
- Evidence type: IDA
- Original reference: PMID:22144463
- Current review action: UNDECIDED
- Review summary: Rad21/cohesin localizes to facultative heterochromatin islands that form over meiotic genes according to the curator annotation. The cached paper is abstract-only and does not mention Rad21, so the specific localization cannot be independently checked here.
- Review reason: This is an experimental IDA annotation from a reliable curator, but the relevant full text is unavailable and the abstract establishes the heterochromatin islands without identifying Rad21. Retain the annotation while deferring judgment rather than accepting or rejecting it from incomplete evidence.

## Reference Context

- PMID:22144463

## Source Context YAML

```yaml
term:
  id: GO:1990342
  label: heterochromatin island
evidence_type: IDA
original_reference_id: PMID:22144463
qualifier: is_active_in
review:
  summary: Rad21/cohesin localizes to facultative heterochromatin islands that form over meiotic genes
    according to the curator annotation. The cached paper is abstract-only and does not mention Rad21,
    so the specific localization cannot be independently checked here.
  action: UNDECIDED
  reason: This is an experimental IDA annotation from a reliable curator, but the relevant full text is
    unavailable and the abstract establishes the heterochromatin islands without identifying Rad21. Retain
    the annotation while deferring judgment rather than accepting or rejecting it from incomplete evidence.
  supported_by:
  - reference_id: PMID:22144463
    supporting_text: facultative heterochromatin
    reference_section_type: ABSTRACT
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

# rad21 (SCHPO, P30776) — Review of GO:1990342 "heterochromatin island" IDA annotation

**Focus:** existing_go_annotation_decision · hypothesis slug `existing-go-1990342-undecided`
**Annotation under review (PomBase detail 472247):** rad21 (SPCC338.17c/P30776) *is_active_in* **heterochromatin island (GO:1990342)**, evidence **IDA (ECO:0000314)**, reference **PMID:22144463**, extension *exists_during* meiotic cell cycle (GO:0098762), assigned_by PomBase 2020-11-26, low throughput.
**Seed hypothesis:** the annotation should receive review action **UNDECIDED**.

---

## Executive Judgment

**Verdict: SUPPORTED. The annotation is directly confirmed by the primary paper's own ChIP data. UNDECIDED is no longer warranted — the recommended action is ACCEPT (with one minor caveat on the temporal extension).**

The central knowledge gap — whether PMID:22144463 actually contains a Rad21 localization assay, which was inaccessible from the abstract — was **resolved by reading the full text** (obtained via PMC6338074). The paper states verbatim:

> "Factors that bind H3K9me and their associated effectors localize to heterochromatin islands: Chromatin immunoprecipitation (ChIP) detected the Clr4 complex (ClrC) subunit Raf2, Swi6/HP1, as well as … RITS (Chp1 and Ago1) and SHREC (Clr3 and Mit1) … at heterochromatin islands (fig. S2). … **We also found the cohesin-loading factor Mis4, which interacts with Swi6/HP1 (10), and the cohesin sub unit Rad21 enriched at meiotic heterochromatin islands (fig. S2).**"

This is an explicit ChIP-based (IDA-appropriate) demonstration that Rad21 — and its loader Mis4 — are enriched at heterochromatin islands. It fully validates the PomBase IDA annotation and explains the internal curation pattern found in Iteration 2 (both the cohesin kleisin **and** its loader annotated to islands from this single reference). The abstract's silence on Rad21 (the entire basis for the seed's caution) is simply because the cohesin result is a supplementary-figure finding, not an abstract-level headline.

**Caveats / remaining minor issue:**
- The ChIP was performed in **log-growing (vegetative) cells**; the islands *cover meiotic-gene loci* ("meiotic heterochromatin islands") but the localization is a vegetative-growth phenomenon. The rad21-specific **`exists_during` meiotic cell cycle (GO:0098762) extension** is therefore likely a minor mis-extension (Rad21 is also largely replaced by Rec8 during actual meiosis; Kitajima 2003, Yokobayashi 2003). The **base CC term is fully supported**; the temporal qualifier should be reviewed/removed independently.
- Confidence in the base term is now **high/direct**; confidence that the extension is correct is **low**.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| **PMID:22144463 (Zofall 2012, Science), full text Fig. S2** | **Direct assay (ChIP)** | **SUPPORTS (decisive)** | rad21 localizes to heterochromatin islands | *"the cohesin sub unit Rad21 enriched at meiotic heterochromatin islands (fig. S2)"*; Mis4 loader also enriched | S. pombe, **vegetative (log-growing) cells** | Direct in-paper evidence; islands cover meiotic genes but assay is vegetative → temporal extension questionable |
| PomBase term GO:1990342 (API) | Database/curation pattern | Supports | rad21 IDA basis is genuine | 11 island genes curated from PMID:22144463 incl. **both Rad21 (kleisin) and Mis4 (loader)** + Swi6/Chp1 | S. pombe (PomBase 2020) | Corroborates the direct finding |
| GEO GSE33404 (NCBI eutils) | Dataset audit | Qualifies | Genomic data underlying the paper | Only 5 **H3K9me2** array samples; Rad21/Mis4 shown by **targeted ChIP (fig. S2)**, not arrays | S. pombe | Explains why cohesin data are figure-level |
| PMID:11780129 (Nonaka 2002, Nat Cell Biol) | Interaction + localization | Supports (mechanism) | Heterochromatin recruits cohesin | Swi6/HP1 recruits cohesin; Psc3–Swi6 interaction | S. pombe centromere/mat | Mechanistic basis for cohesin at Swi6-bound islands (cited as ref 10 in the paper) |
| PMID:21189291 (Dheur 2011, MCB) | Mutant phenotype + localization | Supports (general) | Rad21 acts in facultative-type heterochromatin | rad21 mutation depletes Swi6/H3K9me across a subtelomeric domain | S. pombe subtelomere | Different locus class from islands |
| PMID:31278118 (Folco 2019, Genetics) | Localization (ChIP) + genetics | Supports (general)/Competing | Rad21 within heterochromatin | Genome-wide Rad21/Psc3 within heterochromatin; can *impede* assembly in pds5Δ | S. pombe | Constitutive heterochromatin; role context-dependent |
| PMID:25307058 (Mizuguchi 2014, Nature) | Hi-C + ChIP | Supports (general) | Cohesin at heterochromatin | Cohesin loaded at pericentromeric/subtelomeric heterochromatin | S. pombe | Not island-specific |
| PMID:12750522 (Kitajima 2003, Nature) | Localization/genetics | Refutes/conflicts (extension only) | rad21 active *during meiotic cell cycle* | Rec8 largely replaces Rad21/Scc1 in meiosis | S. pombe meiosis | Conflicts with the `exists_during` extension, not the CC term |
| PMID:12748297 (Yokobayashi 2003, Dev Cell) | Localization/genetics | Qualifies (extension) | rad21 in meiosis | Rad21 substitutes only at centromeres when Rec8 absent | S. pombe meiosis | Meiotic Rad21 role is substitutive/limited |

*(Provenance: PMC6338074 full-text retrieval with verbatim quote; PomBase REST API annotation + term records; NCBI eutils GDS esummary for GSE33404. CSVs: `evidence_matrix_rad21_GO1990342.csv`, `go_decision_table_rad21.csv`, `island_genes_from_PMID22144463.csv`.)*

---

## GO Curation Implications

This is a **cellular component (CC)** annotation. Lead (requires curator verification):

- **ACCEPT / RETAIN GO:1990342** for rad21. The IDA is directly supported by ChIP data in Fig. S2 of PMID:22144463. Change the review action from **UNDECIDED → ACCEPT**.
- **Review the `exists_during` meiotic cell cycle (GO:0098762) extension** (present only on the rad21 annotation). The assay is in vegetative cells and islands merely *cover* meiotic genes; consider **removing or replacing** this temporal qualifier (e.g., no temporal extension, or a `coincident_with` meiotic-gene locus extension as used for other island genes in the same term).
- This is not a "protein binding" case — the informative content is the CC localization term, which is now well-supported.

---

## Mechanistic Scope

- **Direct molecular event (confirmed):** the cohesin kleisin Rad21 (with loader Mis4) is physically enriched by ChIP at facultative heterochromatin islands — small H3K9me/Swi6 domains over meiotic genes silenced during vegetative growth.
- **Upstream vs. downstream:** island *formation* is driven by RNA elimination (Mmi1/Red1) + Clr4/H3K9me; Swi6/HP1 then binds H3K9me and recruits downstream effectors, **including cohesin (Rad21/Mis4)**. Rad21 is thus a *recruited effector at* islands, not an island-forming factor — but the CC term "is_active_in heterochromatin island" is exactly a localization statement and is correct.
- The mechanistic chain (H3K9me → Swi6 → Psc3/Mis4–Swi6 interaction → cohesin) is consistent with Nonaka 2002 (cited as ref 10 in the paper).

---

## Conflicts and Alternatives

- **Temporal-extension conflict (only remaining concern):** `exists_during` meiotic cell cycle conflicts with (i) the vegetative-cell context of the actual ChIP and (ii) Rad21→Rec8 replacement in meiosis. The base localization is unaffected.
- **No paralog confusion for the base term:** the paper explicitly assays Rad21 (mitotic kleisin), not Rec8; the vegetative context is where Rad21, not Rec8, is the active kleisin.
- **Context-dependent cohesin role:** Folco 2019 shows cohesin can antagonize heterochromatin elsewhere, but that does not affect the *localization* claim at islands.

---

## Knowledge Gaps

1. **Quantitative magnitude / genome-wide extent of Rad21 island enrichment.** Checked: the paper shows targeted ChIP (fig. S2); GSE33404 has no cohesin arrays. Matters only for strength, not existence, of the annotation. *Resolve by:* intersecting published Rad21/Psc3 ChIP-seq (Mizuguchi 2014; Folco 2019) with island coordinates.
2. **Intended meaning/validity of the `exists_during` meiotic cell cycle extension.** Checked: assay is vegetative; conflicts with Rec8 replacement. *Resolve by:* curator review of the extension against the figure legend and Materials.
3. **Functional role of cohesin at islands (vs. mere presence).** Checked: not addressed in this paper. Not required for a CC localization annotation. *Resolve by:* rad21-ts/mis4-ts effects on island H3K9me and meiotic-gene silencing.

---

## Discriminating Tests

- **(Already done here) Full-text/Fig. S2 inspection** — decisive; confirms Rad21 at islands.
- **Coordinate-overlap analysis:** intersect published Rad21/Psc3 ChIP-seq peaks with the ~21 island coordinates; permutation test for enrichment (quantifies the effect genome-wide).
- **Perturbation:** test island Rad21 enrichment in swi6Δ/clr4Δ (predicted loss, per Nonaka 2002 logic) to confirm the recruitment mechanism.
- **Rec8 vs. Rad21 discrimination** only needed if the meiotic-timing extension is to be retained.

---

## Curation Leads (require curator verification)

- **Action change:** **UNDECIDED → ACCEPT** for rad21 *is_active_in* heterochromatin island (GO:1990342).
- **Confirming reference + exact snippet to verify:** PMID:22144463, Fig. S2 / Results — *"the cohesin sub unit Rad21 enriched at meiotic heterochromatin islands (fig. S2)"* and *"We also found the cohesin-loading factor Mis4, which interacts with Swi6/HP1 (10) … enriched at meiotic heterochromatin islands."* (Text obtained from PMC6338074; curator should confirm against the published Fig. S2.)
- **Supporting mechanistic reference:** PMID:11780129 — Swi6/HP1 recruits cohesin to heterochromatin (paper's ref 10).
- **Separate flag:** review/remove the `exists_during` meiotic cell cycle (GO:0098762) extension on this annotation (assay is vegetative; Rad21→Rec8 in meiosis).
- **Suggested question to annotator (ORCID 0000-0003-4148-4606):** confirm Fig. S2 as the IDA basis and clarify the intent of the meiotic-cell-cycle extension.
- **Suggested experiment (optional, for functional depth):** rad21/mis4 loss-of-function effect on island H3K9me and meiotic-gene silencing.

---

*Resolution note: Iterations 1–2 flagged this as unresolved/partially supported because the full text was believed inaccessible (Science 403; Europe PMC OA XML 404). Iteration 3 successfully retrieved the author-manuscript full text from PMC6338074, which contains the direct ChIP statement, converting the verdict to SUPPORTED. The only residual issue is the temporal extension.*


## Artifacts

- [OpenScientist evidence matrix rad21 GO1990342](openscientist_artifacts/evidence_matrix_rad21_GO1990342.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table rad21](openscientist_artifacts/go_decision_table_rad21.csv)
- [OpenScientist island genes from PMID22144463](openscientist_artifacts/island_genes_from_PMID22144463.csv)