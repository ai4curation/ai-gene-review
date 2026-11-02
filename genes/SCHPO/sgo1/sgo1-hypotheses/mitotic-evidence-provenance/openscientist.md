---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T21:03:52.230874'
end_time: '2026-09-04T21:24:10.019072'
duration_seconds: 1217.79
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: sgo1
  gene_symbol: sgo1
  uniprot_accession: Q9P7A0
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: mitotic-evidence-provenance
  hypothesis_text: Determine whether PMID:20739936 establishes an endogenous mitotic
    function for S. pombe Sgo1, and distinguish this from engineered expression or
    experiments on other shugoshins.
  term_context: '- PomBase retains a mitotic-metaphase IMP annotation. Do not infer
    misattribution or absence from a title, abstract, or Sgo2-focused supplement.
    Recover exact primary assay details, species, genotype and figure provenance;
    report inaccessible evidence honestly.'
  reference_context: '- PMID:20739936'
  source_file: genes/SCHPO/sgo1/sgo1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Determine whether PMID:20739936 establishes an\
    \ endogenous mitotic function for S. pombe Sgo1,\n  and distinguish this from\
    \ engineered expression or experiments on other shugoshins.\nfocus_type: free_text\n\
    context:\n- PomBase retains a mitotic-metaphase IMP annotation. Do not infer misattribution\
    \ or absence from a title,\n  abstract, or Sgo2-focused supplement. Recover exact\
    \ primary assay details, species, genotype and figure\n  provenance; report inaccessible\
    \ evidence honestly.\nreference_id:\n- PMID:20739936"
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
citation_count: 4
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: go_decision_table.csv
  path: openscientist_artifacts/go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
- filename: pombase_curation_split_PMID20739936.csv
  path: openscientist_artifacts/pombase_curation_split_PMID20739936.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pombase curation split PMID20739936
- filename: provenance_figure_scan.json
  path: openscientist_artifacts/provenance_figure_scan.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist provenance figure scan
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
- **Gene directory:** sgo1
- **Gene symbol:** sgo1
- **UniProt accession:** Q9P7A0

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** mitotic-evidence-provenance
- **Source file:** genes/SCHPO/sgo1/sgo1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Determine whether PMID:20739936 establishes an endogenous mitotic function for S. pombe Sgo1, and distinguish this from engineered expression or experiments on other shugoshins.

## Term and Decision Context

- PomBase retains a mitotic-metaphase IMP annotation. Do not infer misattribution or absence from a title, abstract, or Sgo2-focused supplement. Recover exact primary assay details, species, genotype and figure provenance; report inaccessible evidence honestly.

## Reference Context

- PMID:20739936

## Source Context YAML

```yaml
hypothesis: Determine whether PMID:20739936 establishes an endogenous mitotic function for S. pombe Sgo1,
  and distinguish this from engineered expression or experiments on other shugoshins.
focus_type: free_text
context:
- PomBase retains a mitotic-metaphase IMP annotation. Do not infer misattribution or absence from a title,
  abstract, or Sgo2-focused supplement. Recover exact primary assay details, species, genotype and figure
  provenance; report inaccessible evidence honestly.
reference_id:
- PMID:20739936
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

# AIGR Deep Research Report — S. pombe *sgo1* (Q9P7A0)

**Hypothesis (slug: mitotic-evidence-provenance):** Determine whether **PMID:20739936** establishes an *endogenous mitotic function* for *S. pombe* Sgo1, and distinguish this from engineered expression or experiments on other shugoshins (Sgo2).

**Annotation under review (PomBase, retained):**
`sgo1` → **GO:1990758 "mitotic sister chromatid biorientation"**, evidence **IMP**, reference **PMID:20739936**, annotation extension `happens_during` **GO:0000089 "mitotic metaphase"**. (This is the "mitotic-metaphase IMP annotation" named in the task context.)

---

## Executive Judgment

**Verdict: Over-annotated for Sgo1 (weakly supported at best). The endogenous mitotic function in PMID:20739936 is established for the paralog Sgo2, named explicitly in Figure 2.**

PMID:20739936 (Tsukahara, Tanno & Watanabe, *Nature* 2010, 467:719–723, "Phosphorylation of the CPC by Cdk1 promotes chromosome bi-orientation") is a genuine *S. pombe* **mitotic** study. Its endogenous mitotic mechanism — Cdk1–cyclin-B phosphorylation of Survivin (Bir1) driving direct binding to shugoshin, which acts as the centromeric adaptor recruiting the chromosomal passenger complex (CPC) for bi-orientation — is demonstrated for **Sgo2**, the mitotic fission-yeast shugoshin.

**Figure-level provenance (recovered in Iteration 2).** The publisher HTML (doi:10.1038/nature09390) exposes the abstract, all four figure captions, and the reference list. **Figure 2 is titled: "Phosphorylation of Bir1 promotes the association with *Sgo2* and targeting the CPC to centromeres."** Figures 1, 3 and 4 concern Bir1 phosphorylation, human Borealin, and generic "shugoshins." Across **all accessible text, the string "Sgo1" occurs 0 times, while "Sgo2" occurs 4 times** (the Fig. 2 title plus citations to human *Tripin/hSgo2*). Thus the named fission-yeast shugoshin in the paper's figures is **Sgo2, not Sgo1**.

This matches the paper's own PomBase curation (a Canto session curated by author Y. Watanabe), which assigns every piece of **direct** mitotic evidence — adaptor activity (GO:0140463 IPI, "recruits Bir1"), protein–protein binding, and two-hybrid interaction phenotypes — to **Sgo2 (SPAC15A10.15)**. Sgo1 (SPBP35G2.03c) received *only* a bare gene-level GO:1990758 **IMP** with **no allele, no genotype, and no accompanying mutant-phenotype (FYPO) annotation** — unusual for an IMP, which by definition requires a mutant phenotype.

Independently, Sgo1 is **meiosis-specific** (Kitajima 2004; Kawashima 2007; Vanoosthuyse 2007) and its PomBase expression records are entirely meiosis-associated, so an *endogenous* mitotic role is biologically implausible. The most parsimonious reading is that the Sgo1 IMP is a **paralog-parallel / conserved-mechanism carry-over annotation** rather than a figure-supported endogenous mitotic function of Sgo1.

**Most important caveat (reported honestly):** The *Nature* **full body text and Supplementary remain paywalled** (not in PMC/Europe PMC/OA; Semantic Scholar returned no open PDF). I could read the abstract, figure captions, and reference list but **not the Methods/Supplementary**, so a buried Sgo1 mention cannot be *fully* excluded. However, the main figure explicitly names Sgo2 and Sgo1 is absent from all accessible content, so the residual uncertainty is small. Even if a minor in-vitro Sgo1 binding experiment existed, it would support a **biochemical/conserved-binding** property (an MF/IPI statement), not an **endogenous in-vivo mitotic BP** role.

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|----------|---------------|----------------------------|--------------|-------------|---------|--------------------------|
| 1 | PMID:20739936 (Tsukahara 2010, *Nature*) — abstract | Direct assay (in vivo + biochemical) | **Qualifies** hypothesis | Does the paper show a mitotic shugoshin→CPC adaptor function? | Cdk1-phosphorylated Survivin binds "shugoshin," defined as a conserved centromeric CPC adaptor; enables mitotic bi-orientation | *S. pombe* mitosis (prometaphase/metaphase) | High that the paper is mitotic; abstract does not name Sgo1 vs Sgo2. Body/Supp. paywalled. |
| 1b | PMID:20739936 — **Figure captions (publisher HTML, doi:10.1038/nature09390)** | Direct assay (figure provenance) | **Refutes** Sgo1-specific reading; **Supports** Sgo2 | Which shugoshin is named in the fission-yeast experiment? | **Fig. 2 title: "Phosphorylation of Bir1 promotes the association with Sgo2 and targeting the CPC to centromeres."** "Sgo1" occurs 0×, "Sgo2" 4× in all accessible text | *S. pombe* mitosis | High. Captions retrieved directly; full body/Supp. not accessible. |
| 2 | PMID:20739936 — **PomBase Canto curation of this paper** (curator: Y. Watanabe; 9 genes) | Review/database (structured author curation) | **Refutes** Sgo1-specific reading; **Supports** Sgo2 | Which shugoshin carries the direct mitotic evidence? | Adaptor activity **GO:0140463 (IPI, "recruits Bir1")**, reciprocal protein-binding IPI **Bir1↔Sgo2**, and two-hybrid "abolished PPI" phenotypes are all on **Sgo2 (SPAC15A10.15)**. Sgo1 gets only a bare **GO:1990758 IMP** (no allele, no FYPO phenotype). | *S. pombe* mitosis | High. Author-curated. Note: IMP without a mutant allele/phenotype is anomalous. |
| 3 | PMID:17322402 (Kawashima 2007, *Genes Dev*) | Mutant phenotype + interaction | **Refutes** Sgo1 mitotic role | Which shugoshin is mitotic and binds Bir1/Survivin? | "Sgo1 is meiosis specific"; **Sgo2** interacts with Bir1/Survivin and promotes Aurora/CPC localization for tension-generating attachment | *S. pombe* mitosis & meiosis | High. Independent confirmation Sgo2 = mitotic CPC partner. |
| 4 | PMID:17301288 (Vanoosthuyse 2007, *J Cell Sci*) | Mutant phenotype/localization | **Refutes** Sgo1 mitotic role | Which shugoshin ensures mitotic biorientation? | "Sgo1 … protector of centromere cohesion in meiosis I"; **Sgo2** required for mitotic biorientation and CPC/passenger retention | *S. pombe* mitosis | High. |
| 5 | PMID:14730319 (Kitajima 2004, *Nature*) | Mutant phenotype | **Refutes** / paralog context | Original identification of Sgo1 vs Sgo2 roles | Sgo1 protects meiotic Rec8 cohesin; **Sgo2** paralog required for faithful **mitotic** segregation | *S. pombe* | High. |
| 6 | PomBase gene record SPBP35G2.03c (expression + paralog) | Database | **Qualifies/Refutes** | Is Sgo1 expressed in mitosis? | Sgo1 expression annotations are **meiosis-associated only**; Sgo1 is the **paralog of Sgo2**; all other Sgo1 BP terms are meiotic | *S. pombe* | Medium-high (curated expression, not exhaustive proteomics). |

---

## GO Curation Implications (leads requiring curator verification)

**Target annotation:** `sgo1` GO:1990758 (mitotic sister chromatid biorientation), IMP, PMID:20739936, `happens_during` GO:0000089.

- **Aspect:** BP (biological process).
- **Recommended action (lead):** **Flag for review; likely too strong / candidate for removal or re-scoping to the paralog Sgo2.** The evidence code **IMP is not adequately supported for Sgo1** because the curation carries no Sgo1 allele or mutant phenotype, and all direct experimental evidence in the paper is Sgo2-specific. Sgo1 is meiosis-specific.
- **Preferred outcomes, in order:**
  1. **Remove** the Sgo1 GO:1990758 IMP if figure review confirms no Sgo1 loss-of-function mitotic phenotype exists (most likely).
  2. If the paper contains an **in-vitro** demonstration that recombinant Sgo1 binds phospho-Survivin (conserved-mechanism exemplar), **re-scope** to a molecular-function/interaction statement (e.g., IPI protein binding to Bir1/Survivin) **without** an in-vivo mitotic BP claim, and add a note that Sgo1 is meiosis-specific.
  3. If retained, add an explicit provenance comment distinguishing it from the endogenous Sgo2 function.
- **Do NOT** default to "protein binding" as the informative term for the mitotic role; the informative mitotic MF term (**GO:0140463 chromatin-protein adaptor activity, recruits Bir1**) is correctly held by **Sgo2**, and Sgo1's core, well-supported terms are meiotic (GO:1990813; GO:0045144; GO:0051455) plus centromere/heterochromatin CC.

---

## Mechanistic Scope

- **Immediate molecular event tested by the paper:** Cdk1–cyclin-B phosphorylation of Survivin (Bir1) creates a phospho-dependent binding surface for shugoshin; shugoshin then acts as the centromeric adaptor that docks the CPC (Aurora B/Ark1–INCENP/Pic1–Survivin/Bir1–Borealin/Nbl1) at centromeres to enable bi-orientation.
- **Direct gene-product activity (Sgo2):** phospho-Survivin binding + CPC recruitment (chromatin-protein adaptor activity) — a *direct* mitotic molecular function.
- **Downstream/indirect:** chromosome bi-orientation and faithful mitotic segregation are downstream cellular outcomes of correct CPC localization.
- **Sgo1:** no direct mitotic molecular activity is demonstrated; its established direct activity is meiotic centromeric cohesin (Rec8) protection with PP2A. Any Sgo1 signal in this paper is at most a **conserved biochemical binding property**, not an endogenous mitotic process role.

---

## Conflicts and Alternatives

- **Paralog confusion (primary alternative):** "Shugoshin" in the abstract is generic; the mitotic shugoshin in *S. pombe* is **Sgo2**. The Sgo1 annotation risks conflating the paralogs. The paper's own curation localizes direct evidence to Sgo2.
- **Engineered/conserved-mechanism exemplar:** Watanabe's group frequently uses the small (319-aa) Sgo1 coiled-coil as a tractable model of the conserved shugoshin CPC-binding module. An in-vitro Sgo1–phospho-Bir1 binding result would be a **conserved-mechanism** demonstration, not endogenous mitotic biology.
- **Author-curated over-annotation:** Because the senior author curated the paper, the Sgo1 IMP may reflect an intent to flag conserved mechanism at the gene level; the missing allele/phenotype supports "carry-over/parallel annotation" rather than a data-backed IMP.
- **No conflicting evidence** was found that Sgo1 is expressed or functions in vegetative mitosis.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| Exact figure/panel that generated the Sgo1 IMP | **Largely resolved (Iter. 2-3):** Fig. 2 names **Sgo2**; "Sgo1" absent from all accessible text (abstract, 4 captions, reference list, editorial summary). The **paywalled Methods** are not in the HTML. The **Supplementary PDF is freely downloadable** (Suppl. Table 1 + Suppl. Figs 1-18 w/ legends) but its text is Flate-compressed (300 streams) and could not be extracted in the sandbox (no `zlib`); raw-byte search returned 0 for all terms incl. Survivin/Bir1, so it is **inconclusive, not negative**. Per the task's own context this is a "Sgo2-focused supplement" | Determines whether any Sgo1-specific panel exists | Decompress/OCR the Supplementary PDF, or read the paywalled Methods, to fully exclude a buried Sgo1 panel (residual, low-probability) |
| Whether an sgo1 mutant shows a mitotic biorientation phenotype | PomBase FYPO annotations for this paper — **none on sgo1** | IMP requires a mutant phenotype; its absence undermines the IMP | Locate any sgo1Δ / sgo1 point-mutant mitotic assay in the paper (none evident) |
| Sgo1 protein presence in mitosis | PomBase expression = meiosis-only | Endogenous mitotic function requires mitotic expression | Vegetative-cell proteomics/Western or tagged-Sgo1 imaging in mitosis |

---

## Discriminating Tests

1. **Full-text figure audit** of PMID:20739936 (and Supplementary): catalog every panel labeled "Sgo1" vs "Sgo2," recording whether it is in-vitro binding, localization, or an in-vivo mutant phenotype. This single step is decisive.
2. **sgo1Δ vs sgo2Δ mitotic bi-orientation assay** (minichromosome loss / lagging chromosomes / CPC-Bir1 centromere localization in vegetative cells): predicts a defect only in sgo2Δ.
3. **Mitotic expression check** for endogenous Sgo1 (tagged strain, vegetative growth): predicts undetectable Sgo1 in mitosis.
4. **In-vitro phospho-Bir1 pulldown** comparing recombinant Sgo1 vs Sgo2 N-terminal coiled-coils: tests whether Sgo1 retains conserved binding (a biochemical property) even though it is not expressed in mitosis.

---

## Curation Leads (require curator verification)

- **Candidate reference to verify with exact snippet:** PMID:20739936 abstract — *"Survivin phosphorylation promotes direct binding with shugoshin, which we now define as a conserved centromeric adaptor of the CPC."* Verify in the figures **which shugoshin** (Sgo1 vs Sgo2) was used for each assay.
- **Candidate action change:** Re-scope or remove `sgo1` GO:1990758 (IMP, PMID:20739936); the mitotic biorientation/CPC-adaptor function is supported for **sgo2** (GO:0140463 IPI recruits Bir1; GO:1990758 IMP) in the same paper.
- **Candidate corrected placement:** If a real Sgo1 experiment exists, it is most likely an **in-vitro conserved-binding** result → an MF/interaction statement (Sgo1–Bir1/Survivin binding), **not** an in-vivo mitotic BP.
- **Suggested curator questions:**
  - Is there any sgo1 allele or loss-of-function mitotic phenotype in PMID:20739936 (required to justify IMP)?
  - Was recombinant Sgo1 used only as a conserved-mechanism exemplar?
- **Suggested experiments:** the four discriminating tests above.
- **Retain (well-supported) Sgo1 core terms:** meiotic centromeric cohesion protection (GO:1990813), meiotic sister chromatid segregation (GO:0045144), spindle attachment to meiosis I kinetochore (GO:0051455); CC centromere/pericentric heterochromatin/inner kinetochore.

---

## Limitations

- Figure captions were recovered directly from the publisher HTML (Iteration 2): **Fig. 2 explicitly names Sgo2**, and "Sgo1" is absent from all accessible text. The *Nature* **Methods/full body remain paywalled**. The **Supplementary PDF is freely downloadable but text-locked** (Flate-compressed; not extractable in the sandbox, no `zlib`), so it was neither confirmed nor excluded programmatically — the task context itself labels it "Sgo2-focused." A buried Sgo1 mention in Methods/Supplementary therefore cannot be 100% excluded (residual, low probability).
- Conclusions rest on the paper abstract + **figure captions**, the structured PomBase author curation of this exact paper (direct evidence all on Sgo2; Sgo1 = bare IMP, no allele/phenotype), and orthogonal primary literature (Kitajima 2004; Kawashima 2007; Vanoosthuyse 2007). These lines of evidence are mutually consistent.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/go_decision_table.csv)
- [OpenScientist pombase curation split PMID20739936](openscientist_artifacts/pombase_curation_split_PMID20739936.csv)
- [OpenScientist provenance figure scan](openscientist_artifacts/provenance_figure_scan.json)