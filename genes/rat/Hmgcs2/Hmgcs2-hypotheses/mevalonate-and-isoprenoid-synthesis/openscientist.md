---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T18:09:25.180950'
end_time: '2026-09-20T19:03:08.059625'
duration_seconds: 3222.88
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: rat
  gene: Hmgcs2
  gene_symbol: Hmgcs2
  uniprot_accession: P22791
  taxon_id: NCBITaxon:10116
  taxon_label: Rattus norvegicus
  focus_type: function_assignment
  hypothesis_slug: mevalonate-and-isoprenoid-synthesis
  hypothesis_text: Rat HMGCS2 participates in farnesyl diphosphate biosynthesis via
    mevalonate (GO:0010142) and isoprenoid biosynthesis (GO:0008299). Determine whether
    mitochondrial HMGCS2 executes an endogenous mevalonate/isoprenoid synthetic step,
    including possible context-dependent compartment coupling, or whether complementation
    and cancer overexpression demonstrate ectopic capacity only. Distinguish HMGCS1
    from HMGCS2, identify the site of HMG-CoA production and its access to downstream
    enzymes, and compare genuine physiological participation with indirect metabolic
    effects. Assess each GO claim separately; mitochondrial localization alone does
    not settle the pathway.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/rat/Hmgcs2/Hmgcs2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Rat HMGCS2 participates in farnesyl diphosphate\
    \ biosynthesis via mevalonate (GO:0010142) and\n  isoprenoid biosynthesis (GO:0008299).\
    \ Determine whether mitochondrial HMGCS2 executes an endogenous\n  mevalonate/isoprenoid\
    \ synthetic step, including possible context-dependent compartment coupling, or\n\
    \  whether complementation and cancer overexpression demonstrate ectopic capacity\
    \ only. Distinguish HMGCS1\n  from HMGCS2, identify the site of HMG-CoA production\
    \ and its access to downstream enzymes, and compare\n  genuine physiological participation\
    \ with indirect metabolic effects. Assess each GO claim separately;\n  mitochondrial\
    \ localization alone does not settle the pathway.\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
citation_count: 9
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: hmgcs2_go_decision_table.csv
  path: openscientist_artifacts/hmgcs2_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist hmgcs2 go decision table
- filename: hmgcs_paralog_comparison.csv
  path: openscientist_artifacts/hmgcs_paralog_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist hmgcs paralog comparison
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** rat
- **Taxon:** Rattus norvegicus (NCBITaxon:10116)
- **Gene directory:** Hmgcs2
- **Gene symbol:** Hmgcs2
- **UniProt accession:** P22791

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** mevalonate-and-isoprenoid-synthesis
- **Source file:** genes/rat/Hmgcs2/Hmgcs2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Rat HMGCS2 participates in farnesyl diphosphate biosynthesis via mevalonate (GO:0010142) and isoprenoid biosynthesis (GO:0008299). Determine whether mitochondrial HMGCS2 executes an endogenous mevalonate/isoprenoid synthetic step, including possible context-dependent compartment coupling, or whether complementation and cancer overexpression demonstrate ectopic capacity only. Distinguish HMGCS1 from HMGCS2, identify the site of HMG-CoA production and its access to downstream enzymes, and compare genuine physiological participation with indirect metabolic effects. Assess each GO claim separately; mitochondrial localization alone does not settle the pathway.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Rat HMGCS2 participates in farnesyl diphosphate biosynthesis via mevalonate (GO:0010142) and
  isoprenoid biosynthesis (GO:0008299). Determine whether mitochondrial HMGCS2 executes an endogenous
  mevalonate/isoprenoid synthetic step, including possible context-dependent compartment coupling, or
  whether complementation and cancer overexpression demonstrate ectopic capacity only. Distinguish HMGCS1
  from HMGCS2, identify the site of HMG-CoA production and its access to downstream enzymes, and compare
  genuine physiological participation with indirect metabolic effects. Assess each GO claim separately;
  mitochondrial localization alone does not settle the pathway.
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

# AIGR Deep Research Report: Rat HMGCS2 (P22791) — Mevalonate/Isoprenoid Function Assignment

**Gene:** Hmgcs2 (rat, *Rattus norvegicus*, NCBITaxon:10116)
**UniProt:** P22791
**Focus type:** function_assignment
**Hypothesis slug:** mevalonate-and-isoprenoid-synthesis
**GO claims under evaluation:** GO:0010142 (farnesyl diphosphate biosynthetic process, mevalonate pathway) and GO:0008299 (isoprenoid biosynthetic process)

---

## Summary

The seed hypothesis asks whether rat HMGCS2 participates in **farnesyl diphosphate biosynthesis via mevalonate (GO:0010142)** and **isoprenoid biosynthesis (GO:0008299)** as an endogenous function, or whether any such capacity is merely ectopic (observed only in complementation or cancer-overexpression contexts). After three iterations of investigation against primary literature and curated database records, the answer is clear: **the mevalonate/isoprenoid biological-process assignment is refuted / over-annotated for HMGCS2.** Rat HMGCS2 (P22791) is the **mitochondrial-matrix, ketogenic** isoform of HMG-CoA synthase (EC 2.3.3.10). Its endogenous role is to catalyze the first committed, rate-limiting step of **ketone-body synthesis** — condensing acetyl-CoA and acetoacetyl-CoA into HMG-CoA — after which mitochondrial HMG-CoA lyase cleaves that HMG-CoA to acetoacetate and β-hydroxybutyrate. It does not feed the mevalonate/isoprenoid pathway.

The two GO claims must be assessed separately, as the hypothesis instructs. **GO:0010142** is present on HMGCS2 only as an **IBA (Inferred from Biological Ancestor) annotation from GO_Central** — a phylogenetic carry-over from the shared HMG-CoA synthase ancestral node — and is not supported by any HMGCS2-specific experimental evidence. **GO:0008299 is not currently annotated on HMGCS2 at all and should not be added.** The mevalonate/isoprenoid program legitimately belongs to the cytosolic paralog **HMGCS1**, whose downstream partner enzyme HMGCR (HMG-CoA reductase) is an integral endoplasmic-reticulum (ER) membrane protein physically inaccessible to the mitochondrial matrix.

The one genuine, retained function shared by both paralogs is the **molecular function** hydroxymethylglutaryl-CoA synthase activity (GO:0004421, IDA). The biological process that reflects HMGCS2's true endogenous role is **ketone body biosynthetic process (GO:0046951)**, and its cellular component is the **mitochondrial matrix (GO:0005759, IDA:RGD)**. The critical conceptual caveat is that HMGCS2 genuinely produces HMG-CoA — the same metabolite that seeds the mevalonate pathway — which is precisely why automated phylogenetic pipelines mis-assign the mevalonate BP term. But producing the shared metabolite in the wrong subcellular compartment is not the same as participating in the pathway. Mitochondrial localization does not settle the pathway in favor of mevalonate; it settles it against.

---

## Key Findings

### Finding 1 — HMGCS2 is the mitochondrial, ketogenic isoform; the mevalonate/isoprenoid role belongs to cytosolic HMGCS1

Rat HMGCS2 (UniProt P22791) is annotated with EC 2.3.3.10, a subcellular location of mitochondrion / mitochondrial matrix (GO:0005759, IDA:RGD), and a UniProt function statement describing it as the enzyme that catalyzes "the first irreversible step in ketogenesis." Across the recent primary literature — spanning kidney, liver, and placenta — HMGCS2 is uniformly and explicitly described as **the rate-limiting enzyme of ketogenesis**, and never as a mevalonate or isoprenoid enzyme. A representative renal study states that "the rate-limiting enzyme for ketogenesis, mitochondrial hydroxymethylglutaryl-CoA synthase 2 (HMGCS2), is induced in the proximal tubule of the kidney during fasting" ([PMID: 41568909](https://pubmed.ncbi.nlm.nih.gov/41568909/)). The same characterization recurs independently in hepatic MASLD-MASH flux studies ([PMID: 40272888](https://pubmed.ncbi.nlm.nih.gov/40272888/), [PMID: 39464122](https://pubmed.ncbi.nlm.nih.gov/39464122/)), in diabetic kidney disease ([PMID: 41580118](https://pubmed.ncbi.nlm.nih.gov/41580118/)), in exercise/cognition work ([PMID: 39808588](https://pubmed.ncbi.nlm.nih.gov/39808588/)), and in placental ketone delivery ([PMID: 40288162](https://pubmed.ncbi.nlm.nih.gov/40288162/)).

In direct contrast, the **mevalonate committed step is assigned to the paralog HMGCS1.** A *C. elegans* aging-metabolism study identifies the worm HMG-CoA synthase HMGS-1 as "the ortholog of human HMGCS1 enzyme, which mediates the first committed step of the mevalonate pathway" ([PMID: 25187565](https://pubmed.ncbi.nlm.nih.gov/25187565/)). This establishes the functional division of labor between the two paralogs: **cytosolic HMGCS1 for mevalonate/sterol/isoprenoid synthesis, mitochondrial HMGCS2 for ketogenesis.** This paralog split is the single most decisive discriminating fact for this review, because it explains both why the two enzymes share a molecular function and why only one of them carries the mevalonate biological process.

### Finding 2 — Compartmentalization blocks mitochondrial HMG-CoA from feeding the cytosolic/ER mevalonate–isoprenoid pathway

Even though HMGCS2 chemically produces HMG-CoA, it cannot physiologically participate in mevalonate/isoprenoid synthesis, because **the obligatory next enzyme in that pathway, HMG-CoA reductase (HMGCR), is an integral ER membrane protein**, physically separated from the mitochondrial matrix where HMGCS2 resides. A review of sterol and nonsterol isoprenoid synthesis describes "Endoplasmic reticulum (ER)-localized 3-hydroxy-3-methylglutaryl coenzyme A (HMG CoA) reductase (HMGCR), the rate limiting enzyme in the mevalonate pathway" ([PMID: 36275615](https://pubmed.ncbi.nlm.nih.gov/36275615/)), and a primary localization study confirms that HMGCR "is an integral membrane protein of the endoplasmic reticulum (ER)" ([PMID: 38397481](https://pubmed.ncbi.nlm.nih.gov/38397481/)).

HMG-CoA is a bulky, charged coenzyme-A thioester; it does not freely cross the mitochondrial inner membrane, and no carrier has been described that exports mitochondrial matrix HMG-CoA to the cytosol/ER for mevalonate synthesis. Within the matrix, HMG-CoA is instead cleaved by HMG-CoA lyase to acetoacetate, committing it to ketone-body production. The compartment-confined nature of this flux is reinforced by the observation that renal HMGCS2-derived product acts locally and does not even contribute to the systemic circulating ketone pool ([PMID: 41568909](https://pubmed.ncbi.nlm.nih.gov/41568909/)). This compartmentalization argument is decisive and answers the seed hypothesis's question about "context-dependent compartment coupling" in the negative: there is no described physiological route by which matrix HMG-CoA reaches the ER mevalonate machinery.

```
   CYTOSOL / ER                              MITOCHONDRIAL MATRIX
   ------------                              --------------------
   acetyl-CoA + acetoacetyl-CoA             acetyl-CoA + acetoacetyl-CoA
          |                                          |
        HMGCS1  (GO:0004421)                       HMGCS2  (GO:0004421)  <-- P22791
          |                                          |
        HMG-CoA                                    HMG-CoA
          |                                          |
        HMGCR  (ER integral membrane)             HMG-CoA lyase
          |                                          |
        MEVALONATE                                 ACETOACETATE
          |                                          |
     FPP / isoprenoids / sterols               KETONE BODIES (beta-HB, AcAc)
     GO:0010142, GO:0008299                    GO:0046951  <-- HMGCS2's true BP
```

The two branches begin with the same metabolite in different compartments and never converge.

### Finding 3 — Direct paralog comparison: mevalonate/isoprenoid BP terms are experimentally/orthology-supported on HMGCS1 but only IBA on HMGCS2

A side-by-side comparison of the rat paralogs' GO annotations is the clearest single piece of curation evidence and pinpoints the annotation-provenance problem:

| Feature | HMGCS1 (rat, P17425) | HMGCS2 (rat, P22791) |
|---|---|---|
| Subcellular location | Cytoplasm / cytosol | Mitochondrion, mitochondrial matrix (GO:0005759, IDA:RGD) |
| Molecular function | GO:0004421 HMG-CoA synthase | GO:0004421 HMG-CoA synthase (IDA) |
| GO:0010142 (FPP biosynthesis, mevalonate) | Present, **ISO:RGD** (orthology, exp-backed) | Present, **IBA:GO_Central only** |
| GO:0019287 (isopentenyl-PP biosynthesis, mevalonate) | Present, ISO:RGD | **Absent** |
| GO:0033489 / 0033490 / 0036197 (cholesterol/sterol biosynthesis) | Present, ISO:RGD | **Absent** |
| Cellular response to cholesterol (GO:0071397) | Present, IEP:RGD | **Absent** |
| GO:0008299 (isoprenoid biosynthesis) | Consistent with pathway role | **Not annotated** |
| GO:0046951 (ketone body biosynthesis) | Absent | Present, IEP:RGD (core BP) |

The pattern is unambiguous. On **HMGCS1**, the mevalonate/isoprenoid/sterol terms form a **coherent, mutually corroborating set** — orthology-supported ISO annotations for the biosynthetic steps plus a regulatory IEP term (cellular response to cholesterol) — exactly what one expects of a genuine pathway participant embedded in sterol-feedback regulation. On **HMGCS2**, only the single term GO:0010142 appears, and it appears with the **weakest evidence code in the set, IBA**, a phylogenetic propagation from the shared HMG-CoA synthase family node in GO_Central. HMGCS2 carries **none** of the accompanying sterol/isoprenoid biosynthesis terms and **none** of the cholesterol-response regulatory terms that would corroborate real pathway membership. This asymmetry — a full, experimentally anchored program on HMGCS1 versus a lone, phylogenetically inferred term on HMGCS2 — is the diagnostic signature of paralog/ancestral carry-over rather than a genuine second function.

---

## Mechanistic Model / Interpretation

The HMG-CoA synthase family has two vertebrate paralogs that arose by gene duplication and specialized to different subcellular compartments and metabolic fates:

1. **HMGCS1 (cytosolic)** condenses acetyl-CoA + acetoacetyl-CoA to HMG-CoA in the cytosol, where it feeds ER-membrane HMGCR and thence the mevalonate → farnesyl-PP → sterol/nonsterol isoprenoid pathway. Its regulation is sterol-responsive (SREBP-linked), consistent with a cholesterol/isoprenoid role.

2. **HMGCS2 (mitochondrial matrix)** performs the identical chemistry inside the mitochondrion, where the product HMG-CoA is committed to **ketogenesis** via HMG-CoA lyase. Its regulation is nutritional — fasting/PPARα-driven and post-translationally tuned (e.g., SIRT5 desuccinylation at Lys367 shifts output toward acetoacetate; [PMID: 41580118](https://pubmed.ncbi.nlm.nih.gov/41580118/)).

Because both enzymes catalyze the same reaction (GO:0004421) and produce the same metabolite, **automated phylogenetic annotation (GO_Central IBA) propagates the mevalonate-pathway BP term from the family's ancestral node onto both descendants.** This is a well-recognized source of paralog over-annotation. The molecular function is genuinely shared; the **downstream biological process is not**, because the physical fate of the shared metabolite is dictated by compartment and by the availability of the next enzyme in the pathway.

The seed hypothesis explicitly raises "possible context-dependent compartment coupling." The evidence does not support any such coupling under physiological conditions. Where HMGCS2 is reported to support mevalonate-type outputs — for example experimental complementation of HMGCS1-deficient systems, cytosolic-mistargeting constructs, or tumor overexpression — these represent **ectopic enzymatic capacity**: the enzyme *can* make HMG-CoA that, if placed in the correct compartment or expressed at supraphysiological levels, could seed mevalonate flux. That capacity is a property of the shared active site, not evidence of an endogenous HMGCS2 mevalonate function. GO biological-process annotations should reflect the *normal* physiological role, not the maximal in-vitro or overexpression potential.

The correct annotation profile for HMGCS2 is therefore:

- **MF:** GO:0004421 hydroxymethylglutaryl-CoA synthase activity — **retain** (IDA, shared, genuine).
- **BP (core):** GO:0046951 ketone body biosynthetic process — **retain/emphasize**.
- **CC:** GO:0005759 mitochondrial matrix (IDA:RGD) — **retain**.
- **BP (mevalonate):** GO:0010142 — **remove or NOT-qualify** (IBA carry-over, compartment-incompatible).
- **BP (isoprenoid):** GO:0008299 — **do not add**.

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 41568909](https://pubmed.ncbi.nlm.nih.gov/41568909/) | Mutant phenotype / metabolomics | **Refutes** mevalonate; supports ketogenic | Is HMGCS2 the mitochondrial rate-limiting ketogenic enzyme? | "the rate-limiting enzyme for ketogenesis, mitochondrial HMGCS2, is induced in the proximal tubule … during fasting"; product acts locally | Mouse/rat kidney proximal tubule | High for ketogenic role |
| [PMID: 25187565](https://pubmed.ncbi.nlm.nih.gov/25187565/) | Structural/evolutionary (ortholog) | **Competing** (assigns mevalonate to paralog) | Which paralog performs the mevalonate committed step? | HMGS-1 is "the ortholog of human HMGCS1 enzyme, which mediates the first committed step of the mevalonate pathway" | *C. elegans* / human | High; cross-species but explicit |
| [PMID: 36275615](https://pubmed.ncbi.nlm.nih.gov/36275615/) | Review | **Qualifies** (compartment barrier) | Where is the next mevalonate enzyme HMGCR? | HMGCR is "the rate limiting enzyme in the mevalonate pathway," "ER-localized" | Mammalian review | Medium (review), mechanistically decisive |
| [PMID: 38397481](https://pubmed.ncbi.nlm.nih.gov/38397481/) | Localization (primary) | **Qualifies/Refutes** (compartment barrier) | Is HMGCR accessible to matrix HMG-CoA? | HMGCR "is an integral membrane protein of the endoplasmic reticulum (ER)" | Human cells | High; establishes physical separation |
| UniProt P22791 (RGD) | Localization / database | **Refutes** endogenous mevalonate role | HMGCS2 compartment & annotation basis | Mitochondrion/matrix (GO:0005759 IDA); MF GO:0004421 IDA; GO:0010142 IBA only; GO:0008299 absent | Rat | High; curated record |
| P17425 vs P22791 (paralog GO comparison) | Computational / database | **Refutes** (IBA carry-over pattern) | Evidence strength of GO:0010142 per paralog | HMGCS1 carries mevalonate/sterol terms with ISO+IEP support; HMGCS2 carries only GO:0010142 via IBA and none of the corroborating terms | Rat | High; direct provenance contrast |
| [PMID: 40272888](https://pubmed.ncbi.nlm.nih.gov/40272888/) / [PMID: 39464122](https://pubmed.ncbi.nlm.nih.gov/39464122/) | Loss-of-function flux modeling | **Supports** ketogenic core role | HMGCS2 LOF phenotype | Disrupting HMGCS2, "the rate-limiting step of ketogenesis," impairs hepatic fat oxidation → MASLD-MASH phenotype; no sterol phenotype | Human + mouse liver | High |
| [PMID: 41580118](https://pubmed.ncbi.nlm.nih.gov/41580118/) | Direct assay / PTM | **Supports** ketogenic core role | HMGCS2 product identity | HMGCS2 "the rate-limiting enzyme of ketogenesis"; SIRT5 desuccinylation (K367) shifts output to acetoacetate | Mouse kidney tubule | High; product is ketone |
| [PMID: 39808588](https://pubmed.ncbi.nlm.nih.gov/39808588/) | Mutant phenotype (knockdown) | **Supports** ketogenic core role | HMGCS2 endogenous output | Hepatic HMGCS2 knockdown reduces plasma ketones; "first reaction in ketogenesis" | Rat liver/brain | High; ketone readout only |
| [PMID: 40288162](https://pubmed.ncbi.nlm.nih.gov/40288162/) | Expression / localization | **Supports** ketogenic core role | HMGCS2 tissue function | HMGCS2 "the rate-limiting enzyme of ketogenesis" highly expressed in chorionic plate; produces 3-HB | Human placenta | High for ketogenesis |

**How the evidence coheres:** Every retrievable primary study of HMGCS2 loss-of-function or expression reports a *ketogenic* readout (plasma ketones, hepatic fat oxidation, acetoacetate/β-HB), never a sterol/isoprenoid deficit. The mevalonate role is consistently assigned to HMGCS1. The two mechanistic papers on HMGCR fix the downstream enzyme in the ER, closing the compartment loop. No primary study asserting endogenous HMGCS2-driven mevalonate/isoprenoid flux was retrievable.

---

## GO Curation Implications (leads requiring curator verification)

| GO term | Aspect | Current status on P22791 | Recommended lead |
|---|---|---|---|
| GO:0004421 hydroxymethylglutaryl-CoA synthase activity | MF | IDA:RGD | **Retain.** Genuine, experimentally supported core molecular function shared with HMGCS1. |
| GO:0046951 ketone body biosynthetic process | BP | IEP:RGD | **Retain / elevate as primary BP.** Core physiological process. |
| GO:0010142 farnesyl diphosphate biosynthetic process, mevalonate pathway | BP | **IBA:GO_Central** | **Remove or NOT-qualify.** Compartment-incompatible paralog carry-over; belongs to HMGCS1. |
| GO:0008299 isoprenoid biosynthetic process | BP | **Not annotated** | **Do not add.** Over-broad and unsupported for the mitochondrial isoform. |
| GO:0005759 mitochondrial matrix | CC | IDA:RGD | **Retain.** |

Curators should not "upgrade" the mevalonate/isoprenoid claim to an experimental or ISS annotation for HMGCS2. A NOT-qualifier on GO:0010142 (rather than silent deletion) is defensible given the recurrent nature of the IBA propagation, to prevent automated re-annotation. Note that "protein binding" is explicitly *not* recommended — a more informative and supported MF term (GO:0004421) exists.

---

## Mechanistic Scope

The immediate molecular function under test is **HMG-CoA synthase activity** — condensation of acetyl-CoA + acetoacetyl-CoA to HMG-CoA + CoA. This chemistry is real and shared by both paralogs; it is not in dispute. The question is exclusively about the **biological process** to which HMGCS2's HMG-CoA is committed.

- **Direct gene-product activity (core):** production of HMG-CoA in the mitochondrial matrix, cleaved by HMG-CoA lyase to acetoacetate and thence to β-hydroxybutyrate — i.e., ketone-body synthesis.
- **Downstream / indirect effects (not core function):** systemic ketone signaling, hepatic fat-oxidation balance, MASLD-MASH protection, renal ischemia protection, tubule–macrophage inflammatory crosstalk, fetal ketone supply, and cognitive/mitochondrial effects. These are physiological consequences of ketogenesis, not evidence of mevalonate participation.
- **Ectopic capacity (not core function):** the ability of HMGCS2, when mistargeted or overexpressed, to generate HMG-CoA that could seed mevalonate flux. This is an intrinsic property of the shared active site, consistent with the seed's own "ectopic capacity only" framing.

The mevalonate/isoprenoid claim conflates a shared *molecular function* with a *compartment-specific biological process* — precisely the distinction the seed hypothesis was designed to probe.

---

## Conflicts and Alternatives

- **Paralog confusion (primary alternative, favored):** GO:0010142 is propagated by IBA from the HMGCS ancestor shared with HMGCS1. The MF is common; the mevalonate BP is HMGCS1-specific. This is the most parsimonious explanation for the annotation.
- **UniProt free-text ambiguity:** The P22791 FUNCTION line notes that HMG-CoA can be "converted by HMG-CoA reductase (HMGCR) into mevalonate." Read literally this implies mevalonate participation, but it conflates the general chemistry of HMG-CoA with compartment-restricted physiology; in the mitochondrion, HMG-CoA is a ketogenic, not a mevalonate, intermediate. This text is a plausible source of the over-annotation and should not be used as primary support.
- **Ectopic capacity (compatible with the seed's own framing):** complementation or cancer/overexpression settings that place HMGCS2 activity where cytosolic HMG-CoA is usable demonstrate enzymatic *capacity*, not endogenous pathway participation.
- **Organism/tissue differences:** ketogenic HMGCS2 expression is inducible and tissue-specific (liver, kidney, placenta); none of these contexts show a mevalonate output. No organism-specific exception was found.

---

## Limitations and Knowledge Gaps

1. **Annotation provenance verified from curated records, not re-run programmatically.** The IBA-vs-ISO evidence-code contrast was drawn from RGD/UniProt/GO_Central records. A curator should confirm the live evidence codes on P22791 and P17425 in QuickGO/RGD. This matters because the entire recommendation hinges on GO:0010142 being IBA-only on HMGCS2.
2. **No direct isotopic flux tracing of mitochondrial HMG-CoA fate.** The compartment-barrier argument rests on the established ER localization of HMGCR and the absence of a matrix→cytosol HMG-CoA carrier, not on a dedicated tracing experiment. A positive tracer result is the only thing that could rescue the BP claim; its absence in the literature is consistent with refutation but is not a formal disproof.
3. **Cancer-overexpression literature not exhaustively adjudicated.** Targeted PubMed searches for the seed's "complementation" and "cancer overexpression" scenarios returned no primary study asserting physiological mevalonate/isoprenoid flux by HMGCS2; where HMGCS2 appears in cancer, the retrievable primary literature ties it to ketogenesis/ketone-body signaling. The "ectopic capacity" scenario therefore remains a theoretical enzymatic-capacity argument and cannot be cited as physiological.
4. **No local bioinformatics files were provided.** Analyses used public UniProt/RGD records and PubMed literature; no rat-specific structural or flux dataset was available in-run.

---

## Proposed Follow-up Experiments / Actions

1. **GO annotation provenance audit:** Programmatically pull QuickGO/RGD annotations for P22791 and P17425; confirm GO:0010142 is IBA-only on HMGCS2 and ISO/experimental on HMGCS1, and that HMGCS2 lacks the sterol/isoprenoid corroborating terms. Apply a PAINT/GO_Central curator override restricting GO:0010142 to the HMGCS1 clade.
2. **Compartment-resolved isotope tracing:** In cells lacking HMGCS1 but expressing native (matrix-targeted) HMGCS2, trace ¹³C-acetate/acetyl-CoA into cholesterol/FPP. Endogenous mevalonate participation predicts label incorporation; the ketogenic-only model predicts label appears instead in acetoacetate/β-HB.
3. **Mistargeting rescue test:** Compare cytosol-retargeted HMGCS2 (mitochondrial-targeting-sequence deleted) versus native HMGCS2 for the ability to rescue mevalonate output in HMGCS1-null cells. Rescue only by the retargeted form confirms the function is compartment-gated capacity, not endogenous role.
4. **Loss-of-function readout specificity:** Re-examine existing HMGCS2-KO models for any sterol/isoprenoid deficit. Absence of such a phenotype (only ketogenic/fat-oxidation defects reported to date) further argues against a mevalonate role.
5. **Curation action:** Remove or NOT-qualify GO:0010142 on P22791; do not add GO:0008299; retain GO:0004421 (MF), GO:0046951 (core BP), and GO:0005759 (CC). Consider clarifying the UniProt FUNCTION free-text to avoid implying mitochondrial mevalonate synthesis.

**Candidate references with exact snippets to verify:**
- [PMID: 41568909](https://pubmed.ncbi.nlm.nih.gov/41568909/): *"the rate-limiting enzyme for ketogenesis, mitochondrial hydroxymethylglutaryl-CoA synthase 2 (HMGCS2), is induced in the proximal tubule of the kidney during fasting."*
- [PMID: 25187565](https://pubmed.ncbi.nlm.nih.gov/25187565/): *"the ortholog of human HMGCS1 enzyme, which mediates the first committed step of the mevalonate pathway."*
- [PMID: 36275615](https://pubmed.ncbi.nlm.nih.gov/36275615/): *"Endoplasmic reticulum (ER)-localized 3-hydroxy-3-methylglutaryl coenzyme A (HMG CoA) reductase (HMGCR), the rate limiting enzyme in the mevalonate pathway."*
- [PMID: 38397481](https://pubmed.ncbi.nlm.nih.gov/38397481/): *"It is an integral membrane protein of the endoplasmic reticulum (ER)."*

---

## Bottom Line

Rat HMGCS2 (P22791) is the mitochondrial-matrix ketogenic HMG-CoA synthase. Its endogenous biological process is ketone-body biosynthesis, not mevalonate/isoprenoid synthesis. The mevalonate function belongs to the cytosolic paralog HMGCS1, whose downstream partner HMGCR is ER-bound and physically inaccessible to matrix HMG-CoA. **GO:0010142 on HMGCS2 is an IBA paralog carry-over and should be removed or NOT-qualified; GO:0008299 should not be added. The shared molecular function (GO:0004421) and the ketogenesis BP / mitochondrial-matrix CC annotations should be retained.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist hmgcs2 go decision table](openscientist_artifacts/hmgcs2_go_decision_table.csv)
- [OpenScientist hmgcs paralog comparison](openscientist_artifacts/hmgcs_paralog_comparison.csv)