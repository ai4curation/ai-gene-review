---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T09:40:53.680648'
end_time: '2026-09-12T10:10:16.393433'
duration_seconds: 1762.71
template_file: /Users/cjm/orca/workspaces/ai-gene-review/arath-test/tmp/openscientist-arath-20260912/3-EIN3-template.md
template_variables:
  organism: ARATH
  gene: EIN3
  gene_symbol: EIN3
  uniprot_accession: O24606
  taxon_id: NCBITaxon:3702
  taxon_label: Arabidopsis thaliana
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0001666
  hypothesis_text: EIN3 has response to hypoxia (GO:0001666).
  term_context: '- Term: response to hypoxia (GO:0001666)

    - Evidence type: IMP

    - Original reference: PMID:25284079'
  reference_context: '- PMID:25284079'
  source_file: genes/ARATH/EIN3/EIN3-ai-review.yaml
  source_selector: existing_annotations[16].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0001666\n  label: response to hypoxia\nevidence_type:\
    \ IMP\noriginal_reference_id: PMID:25284079"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: EIN3_hypoxia_GO_decision_table.csv
  path: openscientist_artifacts/EIN3_hypoxia_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist EIN3 hypoxia GO decision table
- filename: EIN3_hypoxia_evidence_matrix.csv
  path: openscientist_artifacts/EIN3_hypoxia_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist EIN3 hypoxia evidence matrix
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

- **Organism code:** ARATH
- **Taxon:** Arabidopsis thaliana (NCBITaxon:3702)
- **Gene directory:** EIN3
- **Gene symbol:** EIN3
- **UniProt accession:** O24606

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0001666
- **Source file:** genes/ARATH/EIN3/EIN3-ai-review.yaml
- **Source selector:** existing_annotations[16].function_hypothesis

## Seed Hypothesis

EIN3 has response to hypoxia (GO:0001666).

## Term and Decision Context

- Term: response to hypoxia (GO:0001666)
- Evidence type: IMP
- Original reference: PMID:25284079

## Reference Context

- PMID:25284079

## Source Context YAML

```yaml
term:
  id: GO:0001666
  label: response to hypoxia
evidence_type: IMP
original_reference_id: PMID:25284079
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

## Specific adjudication question

Adjudicate the original PMID25284079 response-to-hypoxia assignment. Read Results, Figure 6, legends and Discussion independently; identify the actual ein3-1 genotype effect, sample size and statistical comparison. Assess whether EIL1 redundancy or a different condition is experimentally supported, rather than invoked to rescue a null result. If raw data are public, perform a reproducible reanalysis; do not invent data from a plot. Explain whether other cited experiments test hypoxia tolerance or merely EIN3 stabilization. Give a source-specific GO verdict and a separate overall biological verdict. Use primary evidence and independently reproducible analyses. Do not consult ai-gene-review repository reviews, generated reports or local bioinformatics results; these are held out. Verify the exact Arabidopsis protein and distinguish paralogs, mutants, tissue and assay context. Give evidence for and against the assignment, the narrowest defensible function, and what observation would change the verdict. Missing evidence is not refutation. Do not infer catalytic or regulatory function from interaction, docking or shared fold alone.


## Output

# EIN3 → Response to Hypoxia (GO:0001666): Hypothesis Adjudication Report

**Gene:** EIN3 (ETHYLENE INSENSITIVE 3), *Arabidopsis thaliana*
**UniProt:** O24606 (EIN3_ARATH) · Locus: At3g20770
**Focus:** function_assignment — `existing_annotations[16].function_hypothesis`
**Seed hypothesis:** EIN3 has response to hypoxia (GO:0001666)
**Annotation under review:** GO:0001666, evidence IMP, reference [PMID:25284079](https://pubmed.ncbi.nlm.nih.gov/25284079/), qualifier `acts_upstream_of_or_within`, assigned by TAIR

---

## Summary

**Executive verdict — source-specific: REFUTED / over-annotated. Overall biological: weakly / partially supported (indirect, redundant, upstream).**

The EIN3 → *response to hypoxia* (GO:0001666) IMP annotation does not survive independent reading of its cited source. [PMID:25284079](https://pubmed.ncbi.nlm.nih.gov/25284079/) (Xie et al., 2015, *The Plant Journal*) is a study of the acyl-CoA-binding protein **ACBP3**, not of EIN3. In that paper `ein3-1` appears only as one genotype in an epistasis panel built around an ACBP3 overexpressor (OE-1). The decisive experiment (Figure 6b) shows that the `ein3-1` single mutant was **not significantly different from wild type** under either dark submergence (DS) or light submergence (LS), and that the `OE-1 ein3-1` double combination **still resembled the hypoxia-sensitive OE-1 parent**. In other words, removing EIN3 neither produced a hypoxia phenotype on its own nor modified the ACBP3 phenotype. The authors' own conclusion attributes the attenuated hypoxic tolerance of ACBP3 overexpressors to **NPR1- and CTR1-mediated signaling**, explicitly not to EIN3. An IMP (Inferred from Mutant Phenotype) annotation requires a mutant phenotype; here the mutant phenotype was null. The paper's proposed EIL1 redundancy was **invoked to explain the null result but never tested** — no `ein3 eil1` double mutant was assayed for hypoxia in this work. This is a textbook case of a database carry-over annotation where the qualifying phenotype does not exist.

Separately from the source, the *broader biology* offers modest, indirect support for an EIN3/EIL1 role in low-oxygen adaptation, but only as an **upstream ethylene-signaling** step and only in **redundancy with EIL1**. Hartman et al., 2019 ([PMID:31488841](https://pubmed.ncbi.nlm.nih.gov/31488841/)) show that ethylene perception on submergence pre-adapts plants to hypoxia by depleting nitric oxide (via PHYTOGLOBIN1) and thereby stabilizing group VII ERF transcription factors; this pathway runs through EIN2 and the redundant EIN3/EIL1 pair, and EIN3-GFP nuclear accumulation is used only as a *readout* of ethylene perception. Crucially, direct oxygen sensing and the transcriptional activation of hypoxia-responsive genes are executed by the **N-degron pathway and group VII ERFs** (RAP2.2/2.12/2.3, HRE1/2; [PMID:26668304](https://pubmed.ncbi.nlm.nih.gov/26668304/)), not by EIN3.

**Bottom line for the curator:** The specific IMP annotation to PMID:25284079 should be **removed or re-sourced**, because its cited experiment reports a null EIN3 phenotype. If any hypoxia link is to be retained for EIN3, it should be a **non-core, indirect BP** annotation citing Hartman et al. 2019, with a qualifier that does not imply direct oxygen sensing, and it should acknowledge EIN3/EIL1 redundancy. No molecular-function (MF) term implying oxygen sensing is warranted. Identity was verified: O24606 is EIN3 (At3g20770), distinct from its paralog EIL1 (At2g27050), so there is no paralog misassignment — the annotation is on the correct protein but rests on inadequate evidence.

---

## Key Findings

### F001 — The cited source (PMID:25284079) reports a *null* ein3-1 hypoxia phenotype; it does not support the IMP annotation

[PMID:25284079](https://pubmed.ncbi.nlm.nih.gov/25284079/) (Xie et al., 2015, *Plant J*, full text PMC4309432) is an **ACBP3** paper — "*Arabidopsis acyl-CoA-binding protein ACBP3 participates in plant response to hypoxia by modulating very-long-chain fatty acid metabolism.*" EIN3 is not the subject of the study. The `ein3-1` mutant enters only as one of several genotypes in an epistasis screen designed to place the ACBP3 overexpressor (OE-1) hypoxia-sensitivity phenotype within a signaling network.

The relevant result is in the Results subsection "Hypoxia hypersensitivity in OE-1 is dependent on NPR1 and CTR1" and Figure 6b. Two verbatim observations define the evidence:

> "the ein3-1 mutant was not significantly different to wild type under either DS or LS (Figure 6b), possibly due to the functional redundancy of the EIL1 gene in Arabidopsis."

> "the OE-1 coi1-2 and OE-1 ein3-1 double combinations were hypoxia sensitive, resembling the OE-1 phenotype."

Both statements point the same way. First, the `ein3-1` single mutant had **no hypoxia phenotype** (no significant difference from wild type under either dark or light submergence). Second, adding `ein3-1` to the ACBP3 overexpressor **did not rescue or modify** the OE-1 hypoxia-sensitivity phenotype — the double still behaved like OE-1. Both are the signatures of a gene that is *not required* for the phenotype under assay. The abstract's own conclusion makes the exclusion explicit:

> "we observed that the attenuated hypoxic tolerance in ACBP3-OEs was dependent on NPR1- and CTR1-mediated signaling pathways"

EIN3 is not named as a required node; NPR1 and CTR1 are.

Methodologically, the annotation is further weakened by the *quality* of the negative result reported. No survival counts, no sample size (n), and no explicit statistical test are reported for the `ein3-1` comparison — the claim is a qualitative "not significantly different." An IMP (Inferred from Mutant Phenotype, ECO:0000315) annotation is meant to record a phenotype *conferred* by loss of the gene. Here the loss-of-function mutant conferred no detectable phenotype. Using a null result to justify a positive functional annotation inverts the logic of IMP evidence.

### F002 — The proposed EIL1 redundancy was invoked, not tested; independent biology supports only an indirect, redundant, upstream role

The paper itself hedges the null `ein3-1` result by "possibly due to the functional redundancy of the EIL1 gene." That is a hypothesis to explain absence of phenotype, **not evidence of function**. No `ein3 eil1` double mutant was assayed for hypoxia tolerance anywhere in PMID:25284079. Redundancy invoked to rescue a null result cannot be used to support the very annotation the null result fails to justify.

However, redundancy of EIN3/EIL1 in hypoxia adaptation *is* independently supported by a different, stronger study. Hartman et al., 2019 ([PMID:31488841](https://pubmed.ncbi.nlm.nih.gov/31488841/), *Nat Commun*) demonstrate that ethylene perception pre-adapts *Arabidopsis* to subsequent hypoxia:

> "This ethylene-mediated NO depletion and consequent ERFVII accumulation pre-adapts plants to survive subsequent hypoxia"

Mechanistically, entrapment of ethylene during submergence is perceived through the canonical pathway (EIN2 → EIN3/EIL1), leading to PHYTOGLOBIN1-mediated depletion of nitric oxide, which stabilizes group VII ERF transcription factors (ERF-VIIs) and thereby pre-adapts the plant. In that study the `ein3eil1-1` **double** mutant is among the ethylene-signaling mutants in which the pre-adaptation response is abolished, and EIN3-GFP nuclear accumulation is used as a readout of ethylene perception on submergence. This places EIN3/EIL1 **upstream** of the oxygen-sensing machinery as part of ethylene signal transduction — it is not itself an oxygen sensor or a direct activator of the core hypoxia-responsive gene battery. The requirement is genetically satisfied only by the *double* mutant, consistent with EIN3 and EIL1 being redundant.

Thus the *overall biological* picture allows a defensible but weak, indirect claim: EIN3, redundantly with EIL1, participates in ethylene-mediated pre-adaptation to hypoxia. That claim is *not* the one tested by PMID:25284079, and it is BP-level, indirect, and non-core.

### F003 — Identity verified: O24606 = EIN3 (At3g20770); no paralog misassignment, but no oxygen-sensing molecular function

UniProt REST (O24606.json) returns `uniProtKBId = EIN3_ARATH`, protein name "ETHYLENE INSENSITIVE 3", gene `EIN3`, ordered locus At3g20770. The functional keywords are **Activator, Chromatin regulator, DNA-binding, Ethylene signaling pathway, Nucleus, Transcription regulation** — the profile of a nuclear DNA-binding transcriptional activator in the ethylene pathway. There is **no** oxygen-sensing, dioxygenase, or hypoxia molecular-function keyword. Among UniProt's GO cross-references, exactly one hypoxia/oxygen-related term appears: GO:0001666 *response to hypoxia*, with evidence code **IMP:TAIR** — i.e., the very annotation under review, and the only hypoxia link on the record.

The paralog **EIL1 is a distinct gene at a distinct locus (At2g27050)**. Therefore the annotation sits on the correct protein — there is no confusion of EIN3 with EIL1 at the identity level. The problem is not misassigned identity; it is inadequate evidence for the assigned process.

### F004 — QuickGO confirms a single, TAIR-only annotation with a loose qualifier and no orthology support

The EBI QuickGO annotation API (`geneProductId=O24606, goId=GO:0001666`) returns `numberOfHits = 1`. That single annotation has: evidence **IMP (ECO:0000315)**, reference **PMID:25284079**, `assignedBy = TAIR`, qualifier **`acts_upstream_of_or_within`**, `withFrom = null`, taxon 3702. There is **no second, independent annotation** of GO:0001666 for EIN3, and no with/from ortholog transfer supporting it. The annotation is therefore a **single-source record** whose entire evidentiary weight depends on the one paper analyzed above — and that paper reports a null.

The `acts_upstream_of_or_within` qualifier is itself telling: it is the loosest causal relationship in the GO relations vocabulary, signaling that even the curator did not assert a direct role. That loose qualifier is consistent with — but does not remedy — the underlying null phenotype.

---

## Mechanistic Model / Interpretation

The core question is whether EIN3 *directly has* the function "response to hypoxia," or whether it is a bystander/upstream node that was captured by an epistasis screen and then over-annotated. The evidence supports the latter. The two pathways involved should be kept sharply distinct:

```
  DIRECT OXYGEN SENSING & HYPOXIA-GENE ACTIVATION  (EIN3 NOT a member)
  ─────────────────────────────────────────────────────────────────
   O2 / NO ──► N-degron pathway (PCO oxidation of Cys) ──► ERF-VII
                                                          stability
   ERF-VIIs (RAP2.2, RAP2.12, RAP2.3, HRE1, HRE2)  ──►  ~50 hypoxia-
     bind Hypoxia-Responsive Promoter Element (HRPE)     responsive
                                                         genes (HRGs)
                                        [PMID:26668304, 41732087]

  UPSTREAM ETHYLENE SIGNALING  (where EIN3/EIL1 acts — indirectly)
  ─────────────────────────────────────────────────────────────────
   Submergence ──► ethylene entrapment ──► ETR1/CTR1 ──► EIN2
        │                                                  │
        │                                                  ▼
        │                              EIN3 / EIL1 (redundant TFs, nucleus)
        │                                                  │
        └──► PHYTOGLOBIN1 ──► NO depletion ──► ERF-VII stabilization
                                    "pre-adaptation to hypoxia"
                                        [PMID:31488841 (Hartman 2019)]
```

EIN3's authenticated molecular function (F003) is that of a **nuclear DNA-binding transcriptional activator in the ethylene pathway**. Its documented connection to hypoxia is *upstream and indirect*: as part of ethylene signal transduction that can pre-adapt the plant by feeding into ERF-VII stability. It is **not** a component of the oxygen-sensing N-degron machinery and **not** one of the ERF-VII activators that directly bind hypoxia-responsive promoters.

Mapping this onto GO evidence logic:

| Layer | Molecular event | EIN3 role | Correct GO framing |
|---|---|---|---|
| Oxygen sensing | Cys oxidation by PCOs, N-degron proteolysis | none | not applicable to EIN3 |
| Direct HRG activation | ERF-VII binding HRPE motif | none | belongs to RAP2.x / HRE1/2 |
| Upstream ethylene relay | EIN2 → EIN3/EIL1 transcription | member, redundant with EIL1 | non-core, indirect BP (if any) |
| Source (PMID:25284079) test | ein3-1 submergence survival | null phenotype | fails IMP requirement |

The single IMP annotation conflates the "upstream relay" layer (weakly, indirectly true) with a direct "response to hypoxia" claim, and sources it to a paper whose only EIN3 experiment produced a null. That is the definition of an over-annotation.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:25284079](https://pubmed.ncbi.nlm.nih.gov/25284079/) (Xie 2015, *Plant J*) | Mutant phenotype (epistasis) | **Refutes** (source-specific) | Does loss of EIN3 (ein3-1) alter hypoxia/submergence tolerance? | `ein3-1` **not significantly different from WT** under DS or LS; `OE-1 ein3-1` still hypoxia-sensitive like OE-1; phenotype attributed to NPR1/CTR1 | *Arabidopsis*, whole-plant dark/light submergence survival; EIN3 is a secondary genotype in an ACBP3 study | High that result is null; **no n, no explicit test reported** for the ein3-1 comparison; EIL1 redundancy invoked but not tested |
| [PMID:31488841](https://pubmed.ncbi.nlm.nih.gov/31488841/) (Hartman 2019, *Nat Commun*) | Mutant phenotype + mechanism | **Qualifies / weak support** (overall biology) | Does ethylene signaling (EIN2–EIN3/EIL1) pre-adapt plants to hypoxia? | Ethylene → NO depletion (PGB1) → ERF-VII stabilization pre-adapts to hypoxia; `ein3eil1-1` **double** abolishes response; EIN3-GFP a perception readout | *Arabidopsis*, submergence/hypoxia; genetic requirement satisfied only by double mutant | Establishes an **indirect, redundant, upstream** role — not direct oxygen sensing; not the assay in the cited reference |
| [PMID:26668304](https://pubmed.ncbi.nlm.nih.gov/26668304/) (Gasch/Bailey-Serres, *Plant Cell*) | Direct assay (Y1H, ChIP, mutant) | **Competing** | Which TFs directly activate hypoxia-responsive genes? | RAP2.2/RAP2.12 (with RAP2.3) are the principal redundant ERF-VII activators binding the HRPE motif; HRE1/2 minor | *Arabidopsis*, hypoxia-responsive gene battery | Strong; identifies the *actual* direct hypoxia TFs — EIN3 not among them |
| [PMID:41732087](https://pubmed.ncbi.nlm.nih.gov/41732087/) (review) | Review/database | Orientation | What executes plant oxygen sensing? | N-degron/PCO/ERF-VII axis is the core oxygen-sensing/response module | *Arabidopsis* synthesis | Review-level; supports mechanistic framing, not EIN3 specifically |
| UniProt O24606 (EIN3_ARATH) | Database record | Supports identity | Is O24606 EIN3 At3g20770 and does it carry an oxygen-sensing MF? | Nuclear DNA-binding ethylene-pathway activator; **only** hypoxia link is GO:0001666 IMP:TAIR; no oxygen-sensing MF keyword | *Arabidopsis*, sequence/annotation | High; database-level; confirms correct protein, distinct from EIL1 (At2g27050) |
| QuickGO (O24606 × GO:0001666) | Database record | Supports (provenance) | How many/what annotations back this term? | **1 hit**: IMP/ECO:0000315, PMID:25284079, TAIR, qualifier `acts_upstream_of_or_within`, withFrom null | *Arabidopsis* | High; confirms single-source, no ortholog support |

---

## GO Curation Implications

**Lead (requires curator verification): remove or re-source the GO:0001666 IMP annotation on EIN3 (O24606).**

- **Term type:** GO:0001666 *response to hypoxia* is a **Biological Process** term. There is no molecular-function claim in play, and none is warranted — EIN3 has no oxygen-sensing or dioxygenase activity (F003). Do **not** add any MF term implying direct oxygen sensing.
- **Action on the existing annotation:** The IMP evidence code requires a mutant phenotype attributable to the gene. The cited paper's `ein3-1` mutant showed **no phenotype** and did **not** modify the ACBP3 phenotype (F001). The evidence therefore does not meet the IMP standard. Recommended action: **remove** the annotation, or at minimum **re-source** it.
- **If a hypoxia link is retained for EIN3:** cite Hartman et al. 2019 ([PMID:31488841](https://pubmed.ncbi.nlm.nih.gov/31488841/)) instead, framed as a **non-core, indirect BP** role in ethylene-mediated pre-adaptation, with an `acts_upstream_of` relationship and explicit recognition of **EIN3/EIL1 redundancy** (ideally supported by the `ein3eil1` double-mutant evidence, not `ein3-1` alone). This is an IGI/IMP-on-double-mutant style claim, not an IMP on the single mutant.
- **Qualifier:** The existing loose `acts_upstream_of_or_within` qualifier already signals a non-direct role; it is consistent with removal or with a re-sourced, indirect BP annotation, but it does not repair the missing phenotype in the current source.
- **Avoid "protein binding":** Not applicable; the informative framing is transcriptional activator in the ethylene signaling pathway (already captured by other EIN3 annotations).

**GO decision table**

| Element | Current | Recommended lead |
|---|---|---|
| Term | GO:0001666 (BP) | Remove; or re-source as indirect BP |
| Evidence | IMP (ECO:0000315) | Not met by source; if retained via Hartman 2019, use double-mutant genetic evidence |
| Reference | PMID:25284079 | Replace with PMID:31488841 if retained |
| Qualifier | acts_upstream_of_or_within | acts_upstream_of (if retained) |
| With/From | null | consider EIL1 (redundancy) if retained |
| Core? | (implied) | **Non-core**, indirect, redundant |

---

## Mechanistic Scope

- **Immediate molecular function of EIN3 (direct):** sequence-specific nuclear DNA-binding transcriptional activator in the ethylene signaling pathway (UniProt keywords: Activator, DNA-binding, Nucleus, Ethylene signaling). This is the gene product's authenticated core activity.
- **What GO:0001666 asserts:** participation in the *response to hypoxia* biological process. For EIN3 this is at best an **upstream, indirect** contribution via ethylene signal transduction (EIN2 → EIN3/EIL1), feeding into ERF-VII stabilization (Hartman 2019).
- **Downstream / not-direct effects that must not be conflated with EIN3 activity:** the actual oxygen-sensing step (N-degron/PCO), the direct transcriptional activation of the hypoxia-responsive gene battery (ERF-VIIs binding the HRPE motif), and the whole-plant submergence-survival phenotypes assayed in PMID:25284079 (which are driven by ACBP3/very-long-chain fatty acid metabolism and NPR1/CTR1 signaling, not EIN3).
- **Effects inferred only from loss of function:** none usable here — the `ein3-1` loss-of-function produced *no* hypoxia phenotype, so no function can be inferred from it.

---

## Conflicts and Alternatives

1. **The source is not an EIN3 study.** PMID:25284079 is an ACBP3 paper; EIN3 enters only as an epistasis control. Database carry-over of a term from a secondary genotype is the most likely origin of this annotation.
2. **Null result mislabeled as IMP.** The mutant phenotype that IMP requires is absent (`ein3-1` = WT under submergence). This is the central conflict with the seed hypothesis.
3. **Redundancy invoked, not demonstrated.** EIL1 redundancy is a rescue narrative for the null in PMID:25284079; the double mutant was not tested there. Genuine redundancy evidence exists elsewhere (Hartman 2019) but for a different, upstream process.
4. **Competing direct actors.** The direct transcriptional response to hypoxia is executed by group VII ERFs (RAP2.2/2.12/2.3, HRE1/2; [PMID:26668304](https://pubmed.ncbi.nlm.nih.gov/26668304/)), not EIN3. Attributing "response to hypoxia" to EIN3 risks implying it is one of these direct activators, which it is not.
5. **No paralog/identity artifact.** Identity is clean: O24606 = EIN3 (At3g20770) ≠ EIL1 (At2g27050). The problem is evidentiary, not identity-based.

---

## Limitations and Knowledge Gaps

- **No raw data / no reanalysis possible.** PMID:25284079 reports the `ein3-1` comparison qualitatively ("not significantly different"). No survival counts, sample size, or test statistic are given, and no deposited raw dataset was located, so an independent reproducible reanalysis of the ein3-1 phenotype could not be performed. The verdict rests on the authors' own reported null and stated conclusions, read independently. **Gap:** the quantitative strength of the null (was the study powered to detect a small EIN3 effect?) is unknown; a properly powered `ein3-1` and `ein3 eil1` submergence assay would resolve it. *Missing evidence is not refutation of the broader biology — only of the specific IMP claim.*
- **Direction of the Hartman 2019 requirement.** The `ein3eil1-1` double abolishes ethylene-mediated pre-adaptation, but the study's primary aim was the ethylene→NO→ERF-VII axis; the quantitative EIN3/EIL1 contribution versus other ethylene-pathway components is not fully partitioned. **Gap:** an `ein3 eil1` hypoxia-tolerance survival curve with ERF-VII target readouts would quantify the contribution.
- **Curation provenance vs. curator intent.** QuickGO confirms a single TAIR IMP with a loose qualifier, but the internal TAIR curation note that led to term assignment was not retrievable. **Gap:** the original TAIR curation rationale, if it cited a figure other than 6b, should be checked before deletion.
- **Single-species scope.** All primary evidence is *Arabidopsis*; ortholog behavior (e.g., rice EIL1/2 under submergence) may differ and is not with/from-linked here.

---

## Discriminating Tests

The following would most efficiently separate "EIN3 directly has response to hypoxia" from "EIN3 is an upstream, redundant, indirect node":

1. **Powered `ein3-1`, `eil1`, and `ein3 eil1` submergence survival assays** (dark and light), with explicit n and statistics, plus reoxygenation recovery. Prediction: single mutants ≈ WT; only the double shows reduced tolerance if the pre-adaptation role is real.
2. **ERF-VII stability / hypoxia-marker readout in `ein3 eil1`** (e.g., ADH1, PDC1, SUS4 induction; RAP2.12 protein) under submergence to test whether EIN3/EIL1 loss impairs the ethylene→ERF-VII pre-adaptation relay (as Hartman 2019 predicts) without EIN3 binding the HRGs directly.
3. **ChIP-seq / DAP-seq of EIN3** across hypoxia-responsive promoters to test directly whether EIN3 binds the core HRG battery (expected: it does not, in contrast to ERF-VIIs and their HRPE motif).
4. **Epistasis re-test of ACBP3 with `ein3 eil1` double**, since PMID:25284079 only used `ein3-1`; this would test whether redundancy actually masks a contribution to the ACBP3 phenotype (expected: still NPR1/CTR1-dependent).

---

## Curation Leads (require curator verification)

**Candidate action:** Remove GO:0001666 IMP (PMID:25284079) from EIN3, **or** re-source it as a non-core indirect BP.

**Candidate reference snippets to verify in the source (PMID:25284079):**
- Results, Fig. 6b: *"the ein3-1 mutant was not significantly different to wild type under either DS or LS (Figure 6b), possibly due to the functional redundancy of the EIL1 gene in Arabidopsis."*
- Results: *"the OE-1 coi1-2 and OE-1 ein3-1 double combinations were hypoxia sensitive, resembling the OE-1 phenotype."*
- Abstract: *"we observed that the attenuated hypoxic tolerance in ACBP3-OEs was dependent on NPR1- and CTR1-mediated signaling pathways"* (EIN3 not named as required).

**Candidate replacement reference (if a hypoxia link is retained):** [PMID:31488841](https://pubmed.ncbi.nlm.nih.gov/31488841/) — snippet to verify: *"This ethylene-mediated NO depletion and consequent ERFVII accumulation pre-adapts plants to survive subsequent hypoxia."* Frame as indirect, redundant (EIN3/EIL1), `acts_upstream_of`, non-core BP.

**Candidate competing-context reference (for scope, not for EIN3 annotation):** [PMID:26668304](https://pubmed.ncbi.nlm.nih.gov/26668304/) — identifies the actual direct hypoxia transcriptional activators (ERF-VIIs), which EIN3 is not.

**Suggested curator questions:**
- Does the TAIR curation note point to any figure other than 6b? If not, the IMP basis is the null.
- Should the annotation be transferred to EIN3/EIL1 as a redundant pair with double-mutant evidence rather than to EIN3 alone?

**Suggested experiments:** the four discriminating tests above, prioritizing the powered `ein3 eil1` submergence survival + ERF-VII readout.

---

## Final Verdicts

- **Source-specific GO verdict (PMID:25284079):** **REFUTED / over-annotated.** The cited experiment reports a null `ein3-1` phenotype and attributes the hypoxia phenotype to NPR1/CTR1, not EIN3; EIL1 redundancy was invoked but untested. The IMP evidence standard is not met.
- **Overall biological verdict:** **Weakly / partially supported.** An indirect, redundant, upstream EIN3/EIL1 role in ethylene-mediated pre-adaptation to hypoxia is defensible (Hartman 2019), but EIN3 is not an oxygen sensor and not a direct activator of hypoxia-responsive genes.
- **Narrowest defensible function:** EIN3 acts, redundantly with EIL1, as an upstream ethylene-signaling transcription factor that can *contribute to* pre-adaptation to hypoxia — i.e., `acts_upstream_of` the low-oxygen response, non-core.
- **What would change the verdict:** a properly powered, statistically reported `ein3-1` (or `ein3 eil1`) submergence-survival experiment showing a reproducible loss-of-function hypoxia phenotype attributable to EIN3 — ideally with direct evidence that EIN3 binds/activates hypoxia-responsive genes. Absent that, the specific IMP annotation remains unsupported by its source.


## Artifacts

- [OpenScientist EIN3 hypoxia GO decision table](openscientist_artifacts/EIN3_hypoxia_GO_decision_table.csv)
- [OpenScientist EIN3 hypoxia evidence matrix](openscientist_artifacts/EIN3_hypoxia_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)