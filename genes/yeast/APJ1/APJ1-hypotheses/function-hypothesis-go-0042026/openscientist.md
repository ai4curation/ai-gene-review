---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T18:16:52.717314'
end_time: '2026-08-22T18:28:00.430787'
duration_seconds: 667.71
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: APJ1
  gene_symbol: APJ1
  uniprot_accession: P53940
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0042026
  hypothesis_text: APJ1 has protein refolding (GO:0042026).
  term_context: '- Term: protein refolding (GO:0042026)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - file:yeast/APJ1/APJ1-deep-research-falcon.md'
  source_file: genes/yeast/APJ1/APJ1-ai-review.yaml
  source_selector: existing_annotations[3].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0042026\n  label: protein refolding\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033"
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
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
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
- filename: provenance_APJ1_GO_decision_table.csv
  path: openscientist_artifacts/provenance_APJ1_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist APJ1 GO decision table
- filename: provenance_APJ1_refolding_evidence_matrix.csv
  path: openscientist_artifacts/provenance_APJ1_refolding_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist APJ1 refolding evidence matrix
- filename: provenance_APJ1_uniprot_GO_annotations.csv
  path: openscientist_artifacts/provenance_APJ1_uniprot_GO_annotations.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist APJ1 uniprot GO annotations
- filename: provenance_APJ1_vs_YDJ1_domain_comparison.csv
  path: openscientist_artifacts/provenance_APJ1_vs_YDJ1_domain_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist APJ1 vs YDJ1 domain comparison
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** APJ1
- **Gene symbol:** APJ1
- **UniProt accession:** P53940

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0042026
- **Source file:** genes/yeast/APJ1/APJ1-ai-review.yaml
- **Source selector:** existing_annotations[3].function_hypothesis

## Seed Hypothesis

APJ1 has protein refolding (GO:0042026).

## Term and Decision Context

- Term: protein refolding (GO:0042026)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- file:yeast/APJ1/APJ1-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0042026
  label: protein refolding
evidence_type: IBA
original_reference_id: GO_REF:0000033
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

# APJ1 (P53940) — "protein refolding" (GO:0042026) Hypothesis Evaluation

**Gene:** APJ1 / *Saccharomyces cerevisiae* (UniProt P53940, APJ1_YEAST, 528 aa)
**Focus:** function_assignment — does APJ1 directly have protein refolding (GO:0042026)?
**Current annotation under review:** GO:0042026 protein refolding, evidence IBA, GO_REF:0000033

---

## Executive Judgment

**Verdict: Weakly supported / partially over-annotated (as a *direct* function).**

APJ1 is unambiguously a bona fide **Hsp40 / J-domain co-chaperone** of the Hsp70 (Ssa) system: it carries a canonical J domain (residues 4–73) with an intact HPD catalytic tripeptide (position 34), a zinc-binding region typical of type-I DnaJ proteins, and has **direct experimental** molecular-function annotations for **ATPase activator activity** (GO:0001671, IDA) and **unfolded protein binding** (GO:0051082, IMP). As a J-protein it is a component of the Hsp70 machinery that *can* mediate refolding, so a family-level association with the refolding pathway is not unreasonable.

However, the specific term **GO:0042026 "protein refolding" is supported only by IBA** (phylogenetic propagation from the DnaJ/Hsp40 tree, GO_REF:0000033) with **no APJ1-specific experimental evidence**, and the single strongest functional characterization of APJ1 argues **against** refolding as its output: den Brave et al. 2020 (PMID 32492414, *Molecular Cell*) demonstrate that "**Disaggregation mediated by Apj1/Hsp70 promotes turnover rather than refolding**," coupling APJ1-dependent nuclear disaggregation to **26S-proteasomal degradation**, not restoration of native structure. Therefore "protein refolding" is best treated as an **indirect co-chaperone contribution / non-core** term for APJ1, not its demonstrated primary function.

**Most important caveat:** J-proteins are co-chaperones; refolding (if it occurs) is performed by the Hsp70 machine, and for APJ1 the characterized in-vivo route directs clients to degradation. The IBA term is not "wrong" at the level of pathway participation, but it overstates a direct refolding activity that has not been shown and is contradicted by the primary functional study.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt P53940 (SGD/InterPro) | Structural/domain + curated | Supports co-chaperone identity | APJ1 is a J-domain Hsp40 co-chaperone | J domain aa 4–73, HPD at 34, zinc-binding; **ATPase activator activity (IDA)**, **unfolded protein binding (IMP)** | *S. cerevisiae*, curated | High for identity; MF terms are direct |
| **PMID 32492414** (den Brave 2020, *Mol Cell*) | Direct assay + mutant phenotype | **Refutes/qualifies refolding** | Does APJ1 refold proteins? | "Disaggregation mediated by Apj1/Hsp70 **promotes turnover rather than refolding**"; apj1 loss uncouples disaggregation from proteasomal turnover → toxic soluble species | *S. cerevisiae*, nuclear inclusions in vivo | High; strongest functional study |
| PMID 21379326 (Hines 2011) | Genetic/mechanistic | Supports co-chaperone (not refolding per se) | APJ1 J-domain stimulates Hsp70 | Apj1 J-domain stimulates Hsp70 ATPase; can substitute for Ydj1 in [SWI+] propagation | *S. cerevisiae*, prion genetics | Medium-High |
| PMID 19828623 (Weeks 2010) | Mutant phenotype | Qualifies (pleiotropic/indirect) | APJ1 loss affects client processes | apj1Δ reduces flock house virus RNA accumulation by ~60% | *S. cerevisiae* | Medium; downstream, not a folding assay |
| GO:0042026 IBA:GO_Central (GO_REF:0000033) | Computational (phylogenetic) | Competing / weak support | Is refolding APJ1's function? | Family-level propagation from DnaJ tree; no APJ1-specific data | Inference | Low direct confidence |
| This report (UniProt features + NW alignment) | Structural/evolutionary (computed) | Qualifies | Is APJ1 a competent Hsp70 co-chaperone? Is it YDJ1-like? | APJ1 is a **type-I DnaJ** protein (J domain aa4–73 + **CR-type Zn finger aa193–274**, 4 CxxCxGxG repeats); only **34.2% full-length / 48.1% J-domain identity** to paralog YDJ1 | *S. cerevisiae* sequences, in-silico | Medium; architecture is neutral on refolding-vs-degradation |

Provenance CSVs: `provenance/APJ1_uniprot_GO_annotations.csv`, `provenance/APJ1_refolding_evidence_matrix.csv`, `provenance/APJ1_GO_decision_table.csv`, `provenance/APJ1_vs_YDJ1_domain_comparison.csv`.

---

## GO Curation Implications (leads — require curator verification)

- **GO:0042026 protein refolding (IBA):** Do **not** treat as a demonstrated direct function. Options, in order of preference:
  1. **Retain as non-core** IBA (defensible family-level pathway participation) **but add a curator note** citing PMID 32492414 that APJ1's characterized disaggregation output is degradation, not refolding.
  2. **Generalize / de-emphasize** in favor of the experimentally supported process (below).
- **Consider ADDing an experimentally-supported BP** capturing APJ1's characterized role: nuclear protein-aggregate **disaggregation coupled to proteasomal degradation** / protein quality control (supported by PMID 32492414, an EXP/IMP-grade source). GO:0043335 (protein unfolding, IMP) already partially captures the unfolding/disaggregation step and should be **retained**.
- **Retain core MF terms** with direct evidence: **GO:0001671 ATPase activator activity (IDA)** and **GO:0051082 unfolded protein binding (IMP)** — these are the informative, well-supported molecular functions and are preferable to generic "protein binding."

---

## Mechanistic Scope

- **Direct molecular activity (supported):** J-domain stimulation of Hsp70 (Ssa) ATPase (ATPase activator activity) and binding of unfolded/aggregated clients — i.e., APJ1 acts as a substrate-targeting co-chaperone that licenses Hsp70.
- **Cellular process (supported):** Hsp70-dependent, Hsp104-independent solubilization/disaggregation of nuclear protein inclusions, which is then **channeled to the 26S proteasome** for clearance.
- **Refolding (the tested claim):** Not demonstrated for APJ1; the primary study explicitly contrasts APJ1's output with refolding. Any refolding is a generic property of the Hsp70 machine, not a shown APJ1 activity.
- **Downstream/pleiotropic effects (do not equate with core function):** prion [PSI+]/[SWI+] propagation modulation, viral RNA replication support — these are client-specific consequences, not folding assays.

---

## Conflicts and Alternatives

- **Direct conflict:** PMID 32492414 states the disaggregation is coupled to **turnover rather than refolding** — the single most direct piece of evidence opposes the seed term.
- **Paralog context (quantified):** APJ1 shares the type-I DnaJ architecture (J domain + CR-type zinc finger + C-terminal SBD) with **YDJ1**, but computed pairwise identity is only **34.2% full-length / 48.1% over the J domain** (NW global alignment; `provenance/APJ1_vs_YDJ1_domain_comparison.csv`). Functional overlap exists in some assays (Hines 2011), but this level of divergence means YDJ1's canonical refolding-co-chaperone phenotypes should **not** be automatically transferred to APJ1 by homology/IBA. Notably, the identical domain toolkit serves **both** refolding (YDJ1) and disaggregation-coupled degradation (APJ1), so domain architecture is **neutral** on the refolding question — the gene-specific experimental data (PMID 32492414) remain decisive.
- **Evidence-code caveat:** GO:0042026 is IBA (no wet-lab support for APJ1); its persistence is a database/phylogenetic carry-over rather than gene-specific finding.

---

## Knowledge Gaps

1. **No in-vitro APJ1 refolding assay** (e.g., luciferase/G6PDH reactivation with Ssa1 ± Apj1). Checked PubMed; none found. Matters because it would directly test whether APJ1+Hsp70 can restore activity vs only solubilize. *Resolve:* biochemical reactivation assay.
2. **Fate of solubilized substrate quantified?** den Brave shows turnover dominates in vivo, but the partition between refolding and degradation for physiological substrates is not quantified. *Resolve:* pulse-chase of a model aggregation substrate in apj1Δ ± proteasome inhibition.
3. **Basis of GO:0016925 sumoylation (IGI) and the degradation link** (STUbL pathway) not fully resolved from abstracts retrieved. Matters for defining APJ1's primary BP. *Resolve:* review SGD primary references for the IGI annotation.

---

## Discriminating Tests

- **In-vitro chaperone reactivation:** aggregated firefly luciferase + Ssa1/Sse1/Hsp104 ± Apj1, measure regained enzymatic activity (refolding) vs solubilization only. Distinguishes refolding from disaggregation-to-degradation.
- **In-vivo fate assay:** photoactivatable/aggregation-prone reporter in WT vs apj1Δ, ± proteasome inhibitor (MG132/pdr5Δ), scoring recovery of soluble native reporter vs its degradation.
- **Domain dissection:** HPD→QPD J-domain mutant to confirm Hsp70-dependence of any observed activity.
- **Comparative:** side-by-side YDJ1 vs APJ1 in the same refolding assay to separate paralog-specific outputs.

---

## Curation Leads (require curator verification)

- **Candidate reference / snippet to verify (degradation-not-refolding):** PMID **32492414** — verbatim: *"Disaggregation mediated by Apj1/Hsp70 promotes turnover rather than refolding."* and *"The nuclear J-domain protein Apj1 supports protein disaggregation together with Hsp70 but independent of the canonical disaggregase Hsp104."*
- **Candidate reference / snippet (co-chaperone MF):** PMID **21379326** — *"the highly conserved 70 amino acid J-domain, which serves to stimulate the ATPase activity of Hsp70."*
- **Candidate action change:** downgrade GO:0042026 from an implied core function to **non-core IBA with an explicit conflicting-evidence note**, or replace emphasis with an experimentally-grounded disaggregation/quality-control BP.
- **Candidate terms to prioritize:** keep GO:0001671 (MF, IDA), GO:0051082 (MF, IMP), GO:0043335 (BP, IMP); evaluate adding a disaggregation-coupled-degradation / protein-quality-control BP.
- **Suggested curator questions:** (1) Is any direct APJ1 refolding assay in the SGD primary literature? (2) Should IBA refolding be retained when a gene-specific EXP study contradicts a refolding output? (3) What is the primary reference underpinning the IGI sumoylation annotation, and does it define APJ1's degradation role?
- **Suggested experiments:** in-vitro luciferase reactivation ± Apj1; in-vivo soluble-reporter recovery vs degradation in apj1Δ.

---

## Limitations

- Assessment relies on PubMed abstracts + UniProt/SGD/InterPro records accessed programmatically; full texts (esp. den Brave 2020 methods and any biochemical refolding data) were not parsed. No local bioinformatics files were provided. Findings on domain architecture are from UniProt feature annotations (direct fetch), plus an in-house Needleman-Wunsch alignment for paralog identity (not re-derived from 3D structure).
- The literature index available in this run returned no records for the APJ1 sumoylation/STUbL-degradation basis (the SGD IGI GO:0016925 reference) or for human DNAJA ortholog refolding studies; these could not be verified here and are flagged as open gaps rather than asserted. A curator with full PubMed/SGD access should confirm the IGI reference and the cross-species IBA basis directly.

---

## Provenance Artifacts (computed this run)

| File | Contents |
|---|---|
| `provenance/APJ1_uniprot_GO_annotations.csv` | All current UniProt/SGD GO annotations for P53940 with evidence codes |
| `provenance/APJ1_refolding_evidence_matrix.csv` | Evidence matrix (this report) |
| `provenance/APJ1_GO_decision_table.csv` | Per-term GO curation recommendation table |
| `provenance/APJ1_vs_YDJ1_domain_comparison.csv` | Type-I DnaJ architecture + NW % identity APJ1 vs YDJ1 |


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist APJ1 GO decision table](openscientist_artifacts/provenance_APJ1_GO_decision_table.csv)
- [OpenScientist APJ1 refolding evidence matrix](openscientist_artifacts/provenance_APJ1_refolding_evidence_matrix.csv)
- [OpenScientist APJ1 uniprot GO annotations](openscientist_artifacts/provenance_APJ1_uniprot_GO_annotations.csv)
- [OpenScientist APJ1 vs YDJ1 domain comparison](openscientist_artifacts/provenance_APJ1_vs_YDJ1_domain_comparison.csv)