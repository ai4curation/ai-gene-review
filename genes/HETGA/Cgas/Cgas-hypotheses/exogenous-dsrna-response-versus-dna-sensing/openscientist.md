---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:08:07.884813'
end_time: '2026-09-21T02:23:21.055354'
duration_seconds: 913.17
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: HETGA
  gene: Cgas
  gene_symbol: Cgas
  uniprot_accession: A0AAX6RS70
  taxon_id: NCBITaxon:10181
  taxon_label: Heterocephalus glaber
  focus_type: function_assignment
  hypothesis_slug: exogenous-dsrna-response-versus-dna-sensing
  hypothesis_text: Heterocephalus glaber Cgas participates in cellular response to
    exogenous double-stranded RNA (GO:0071360). Assess the mouse Q8C6L5 source experiments
    (PMID:23258413, PMID:24077100, PMID:28214358, PMID:28363908) and the phylogenetic
    assertion at PTN002579681. Determine whether they demonstrate a direct or indirect
    mechanistic response to exogenous dsRNA, or instead specifically test dsDNA. Lack
    of direct RNA binding or poly(I:C)-stimulated catalysis does not by itself exclude
    participation in a cellular response. Separate target-specific evolutionary divergence
    from ambiguity in donor evidence.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/HETGA/Cgas/Cgas-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Heterocephalus glaber Cgas participates in cellular\
    \ response to exogenous double-stranded\n  RNA (GO:0071360). Assess the mouse\
    \ Q8C6L5 source experiments (PMID:23258413, PMID:24077100, PMID:28214358,\n  PMID:28363908)\
    \ and the phylogenetic assertion at PTN002579681. Determine whether they demonstrate\
    \ a\n  direct or indirect mechanistic response to exogenous dsRNA, or instead\
    \ specifically test dsDNA. Lack\n  of direct RNA binding or poly(I:C)-stimulated\
    \ catalysis does not by itself exclude participation in\n  a cellular response.\
    \ Separate target-specific evolutionary divergence from ambiguity in donor evidence.\n\
    focus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 5
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: artifacts_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: artifacts_go0071360_annotation_provenance.csv
  path: openscientist_artifacts/artifacts_go0071360_annotation_provenance.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go0071360 annotation provenance
- filename: artifacts_go_decision_table.csv
  path: openscientist_artifacts/artifacts_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
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

- **Organism code:** HETGA
- **Taxon:** Heterocephalus glaber (NCBITaxon:10181)
- **Gene directory:** Cgas
- **Gene symbol:** Cgas
- **UniProt accession:** A0AAX6RS70

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** exogenous-dsrna-response-versus-dna-sensing
- **Source file:** genes/HETGA/Cgas/Cgas-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Heterocephalus glaber Cgas participates in cellular response to exogenous double-stranded RNA (GO:0071360). Assess the mouse Q8C6L5 source experiments (PMID:23258413, PMID:24077100, PMID:28214358, PMID:28363908) and the phylogenetic assertion at PTN002579681. Determine whether they demonstrate a direct or indirect mechanistic response to exogenous dsRNA, or instead specifically test dsDNA. Lack of direct RNA binding or poly(I:C)-stimulated catalysis does not by itself exclude participation in a cellular response. Separate target-specific evolutionary divergence from ambiguity in donor evidence.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Heterocephalus glaber Cgas participates in cellular response to exogenous double-stranded
  RNA (GO:0071360). Assess the mouse Q8C6L5 source experiments (PMID:23258413, PMID:24077100, PMID:28214358,
  PMID:28363908) and the phylogenetic assertion at PTN002579681. Determine whether they demonstrate a
  direct or indirect mechanistic response to exogenous dsRNA, or instead specifically test dsDNA. Lack
  of direct RNA binding or poly(I:C)-stimulated catalysis does not by itself exclude participation in
  a cellular response. Separate target-specific evolutionary divergence from ambiguity in donor evidence.
focus_type: function_assignment
context: []
reference_id: []
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

# AIGR Hypothesis Review — HETGA *Cgas* (A0AAX6RS70)

**Hypothesis (slug: exogenous-dsrna-response-versus-dna-sensing):** *Heterocephalus glaber* Cgas participates in **cellular response to exogenous double‑stranded RNA (GO:0071360)**.
**Focus type:** function_assignment.

---

## Executive Judgment

**Verdict: Refuted / over‑annotated (as a dsRNA response).**

The seed hypothesis rests on a GO annotation that is a **term‑selection error at the donor**, not a genuine dsRNA‑response function. Mouse cGAS (Q8C6L5) carries GO:0071360 "cellular response to exogenous **dsRNA**" supported by four experimental references — **PMID:23258413, PMID:24077100, PMID:28214358, PMID:28363908** — and **every one of these papers assays double‑stranded *DNA* (transfected DNA, DNA virus, λ/dsDNA binding), with no exogenous dsRNA / poly(I:C) experiment at all.** cGAS is the canonical cytosolic **dsDNA** sensor; it binds RNA structurally but is not catalytically activated by dsRNA, and even DNA:RNA hybrids are largely inert.

The HETGA annotation is **pure phylogenetic inheritance** (IEA:TreeGrafter via PANTHER node **PTN002579681**; the source IBA is GO_REF:0000033). There is **no naked mole‑rat experimental evidence** of any kind. Therefore this is **ambiguity/error in the donor evidence, not target‑specific evolutionary divergence.**

Important caveat honoured from the seed: lack of direct RNA binding or poly(I:C)‑stimulated catalysis does not, by itself, exclude an *indirect* cellular response to exogenous dsRNA (e.g., dsRNA‑induced mitochondrial damage → mtDNA release → cGAS). **However, GO IDA/IMP evidence requires the cited experiment to demonstrate the process, and none of the four donor papers tests dsRNA.** So even granting the indirect possibility, the cited evidence does not establish it.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID:23258413 (Sun 2013, Science) | Direct assay + mutant/knockdown (IMP for GO:0071360) | **Refutes** dsRNA; supports dsDNA | Is cGAS a nucleic‑acid sensor and of which? | "cGAS is a cytosolic **DNA** sensor that induces interferons by producing…cGAMP"; assays = DNA transfection & DNA virus | Mouse/human cells | High. No RNA/poly(I:C) assay; term=dsRNA appears mis‑selected |
| PMID:24077100 (Ablasser 2013, Nature) | Direct assay (IDA for GO:0071360) | **Refutes** dsRNA; supports DNA/cGAMP | How does cGAS‑derived immunity spread? | "**Cytosolic DNA is sensed** by…cGAS"; cGAMP transferred via gap junctions | Murine & human cells | High. Concerns cGAMP transfer, not dsRNA sensing |
| PMID:28214358 (Lee 2017, FEBS Lett) | Biochemical/structural (IDA) | **Refutes** dsRNA; supports dsDNA | N‑terminus effect on cGAS catalysis | "catalytic activity of core‑cGAS decreased as the length of **double‑stranded DNA (dsDNA)** increased" | In vitro / cells | High. Explicitly dsDNA |
| PMID:28363908 (Tao 2017, J Immunol) | Single‑molecule + biochem (IDA) | **Refutes** dsRNA; supports dsDNA | N‑terminus role in DNA binding/activation | "binding of nonspecific **dsDNA** by the N‑terminal domain of cGAS promotes its activation" (λDNA) | Human cGAS, in vitro/cells | High. Explicitly dsDNA (λDNA) |
| PANTHER PTN002579681 / GO_REF:0000033 (IBA) | Phylogenetic (ECO:0000318) | **Qualifies/competing** | Ortholog‑based propagation of donor terms | Propagates the (erroneous) dsRNA term across the cGAS clade, incl. HETGA | Computational | Medium. Inherits donor error; no species data |
| A0AAX6RS70 IEA:TreeGrafter (UniProt/QuickGO) | Computational (IEA) | **Qualifies** | Is HETGA term experimentally grounded? | GO:0071360 on HETGA is IEA only; no experimental support | *H. glaber* | High that it is IEA‑only |
| PMID:42629426 (Lebrec 2026) | Review‑adjacent primary tool paper | Supports dsDNA identity | cGAS ligand landscape | "cGAS is the primary innate immune **DNA** sensor"; "simple **DNA:RNA hybrids are inert**" | Human cells | Medium. Orientation‑level for RNA inertness |

---

## GO Curation Implications

**Lead (requires curator verification):**

- **Do not assign GO:0071360 (cellular response to exogenous dsRNA) to HETGA *Cgas*.** The IEA:TreeGrafter propagation inherits an unsupported donor term.
- **Flag the donor annotation (mouse Q8C6L5 → GO:0071360) for correction.** All four cited experiments demonstrate response to exogenous/cytosolic **dsDNA**, not dsRNA. The biologically correct BP analog already exists: **GO:1990786 "cellular response to dsDNA"** (aspect BP). This is best treated as a **dsRNA↔dsDNA term‑selection error**.
- Retained/positive terms that *are* well supported for cGAS and appropriately propagated to HETGA: **GO:0061501 (2′,3′‑cGAMP synthase activity, MF)**, **GO:0003690 (dsDNA binding, MF)**, **GO:0140896 (cGAS/STING signaling, BP)**, **GO:0032481 (positive regulation of type I IFN production, BP)**, **GO:0002230 (positive regulation of defense response to virus by host, BP)**. These, not a dsRNA term, capture the gene product's function.
- Avoid "protein binding" as a recommendation — more informative MF/BP terms above are supported.

---

## Mechanistic Scope

**Immediate molecular function tested by the donor references:** binding of cytosolic **double‑stranded DNA** by cGAS and DNA‑stimulated catalysis of **2′,3′‑cGAMP** (a nucleotidyltransferase reaction, EC 2.7.7.86), which activates STING → TBK1/IRF3 → type I IFN. The N‑terminal papers (28214358, 28363908) dissect how the low‑complexity N‑terminus modulates **dsDNA** binding and catalytic output.

- **Direct gene‑product activity:** dsDNA sensing + cGAMP synthesis.
- **Downstream (not the tested MF):** type I IFN induction, antiviral state, paracrine cGAMP spread, senescence.
- **Not demonstrated by any cited paper:** a response to exogenous **dsRNA** — neither direct (RNA binding/poly(I:C) catalysis) nor indirect (dsRNA‑triggered mtDNA release feeding cGAS).

---

## Conflicts and Alternatives

- **Term mislabel (most likely):** "dsRNA" was selected where "dsDNA" was meant; the four references and the entire cGAS field describe DNA sensing. Analog term GO:1990786 exists.
- **Database carry‑over:** the error is amplified by IBA (PANTHER PTN002579681) → IEA:TreeGrafter to orthologs including HETGA, so multiple species now carry it.
- **Indirect‑response steelman:** exogenous dsRNA can cause mitochondrial/nuclear damage that releases DNA activating cGAS; this *could* justify a broad "response to dsRNA" chain, but it is (a) not what the cited papers test and (b) would still be indirect and better annotated to the DNA‑sensing MF/BP with the actual trigger, not a direct dsRNA term.
- **No paralog confusion:** the donor is bona fide cGAS/MB21D1; the issue is term choice, not gene identity. HETGA A0AAX6RS70 is a clear cGAS ortholog (XP_021099394.1, Mb21d1).

---

## Knowledge Gaps

1. **Was the donor "dsRNA" term deliberate or a typo for "dsDNA"?** Checked: all 4 cited abstracts test DNA; a DNA analog term exists. Matters because it determines whether to correct vs remove. Resolve by inspecting the original UniProt/MGI curation record and the exact figure cited.
2. **Any *H. glaber*‑specific cGAS immune data?** Checked: no experimental UniProt evidence; HETGA term is IEA‑only. Matters for whether species divergence could rescue the term. Resolve with naked mole‑rat cGAS ligand/activation assays (poly(I:C) vs dsDNA).
3. **Does naked mole‑rat cGAS have altered nucleic‑acid selectivity?** Not established here. Resolve with recombinant HETGA cGAS in vitro cGAMP assays across dsDNA, dsRNA, and RNA:DNA hybrids.

---

## Discriminating Tests

- **In vitro cGAMP synthesis assay** with purified HETGA (and mouse) cGAS challenged with dsDNA vs poly(I:C)/dsRNA vs RNA:DNA hybrids — directly separates "dsDNA sensor" from "dsRNA responder." Expectation: activation by dsDNA only.
- **Cellular IFN‑β reporter** in HETGA cells: transfected dsDNA vs poly(I:C), ± cGAS knockdown/knockout, to test whether any dsRNA‑driven IFN is cGAS‑dependent (would test the indirect route).
- **Curation provenance check:** retrieve the exact experiment/figure the donor annotation cites for GO:0071360 to confirm dsRNA vs dsDNA wording.

---

## Curation Leads (require curator verification)

- **Action:** Remove/replace GO:0071360 on HETGA *Cgas* (A0AAX6RS70); it is IEA:TreeGrafter inheritance of an unsupported donor term.
- **Candidate replacement term:** **GO:1990786 "cellular response to dsDNA"** (BP) if a stimulus‑response BP is desired; otherwise rely on the well‑supported **GO:0140896 cGAS/STING signaling** and **GO:0032481 positive regulation of type I IFN production**.
- **Upstream fix:** File a note to correct mouse Q8C6L5 GO:0071360 (dsRNA→dsDNA) and re‑propagate; PANTHER node **PTN002579681** should be updated so all clade orthologs stop inheriting the dsRNA term.
- **Candidate references + verify‑snippets:**
  - PMID:23258413 — "cGAS is a cytosolic DNA sensor that induces interferons by producing the second messenger cGAMP."
  - PMID:28214358 — "the catalytic activity of core-cGAS decreased as the length of double-stranded DNA (dsDNA) increased."
  - PMID:28363908 — "binding of nonspecific dsDNA by the N-terminal domain of cGAS promotes its activation."
  - PMID:24077100 — "Cytosolic DNA is sensed by the receptor cyclic GMP-AMP (cGAMP) synthase (cGAS)."
- **Suggested question for curators:** Is the donor GO:0071360 traceable to a specific dsRNA experiment, or is it a dsDNA/dsRNA wording error? If the latter, correct at source before any ortholog carries it.

---

## Provenance / Artifacts

Computed provenance from QuickGO/UniProt REST queries (run 2026-09-21):

- `artifacts/go0071360_annotation_provenance.csv` — every GO:0071360 annotation on mouse Q8C6L5 and HETGA A0AAX6RS70 with qualifier/evidence/reference. **All are positive `involved_in` (not `NOT`) annotations**; mouse = 1 IBA + 1 IMP + 3 IDA; HETGA = single IEA:TreeGrafter (GO_REF:0000118).
- `artifacts/evidence_matrix.csv` — the evidence matrix above in tabular form.
- `artifacts/go_decision_table.csv` — GO decision table (remove/replace/retain per term).

Key confirmation this iteration: the mouse and HETGA annotations use qualifier **`involved_in`** — i.e., the database positively asserts participation in exogenous-dsRNA response, so this is a genuine over-annotation to correct, not a mis-read `NOT` (does-not-respond) annotation.

## Limitations

- Analysis is annotation/literature‑based; abstract‑level reading of the four references (full texts not machine‑parsed here) — but the abstracts are explicit about DNA. No new wet‑lab data. QuickGO/UniProt snapshots as of the run date (2026‑09‑21).


## Artifacts

- [OpenScientist evidence matrix](openscientist_artifacts/artifacts_evidence_matrix.csv)
- [OpenScientist go0071360 annotation provenance](openscientist_artifacts/artifacts_go0071360_annotation_provenance.csv)
- [OpenScientist go decision table](openscientist_artifacts/artifacts_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)