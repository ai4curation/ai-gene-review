---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-04T16:34:41.475053'
end_time: '2026-07-04T16:55:38.393344'
duration_seconds: 1256.92
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: KCTD14
  gene_symbol: KCTD14
  uniprot_accession: Q9BQ13
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: core_function
  hypothesis_slug: core-function-1-go-0042802
  hypothesis_text: 'identical protein binding (GO:0042802) is a core function of KCTD14.
    Current rationale: KCTD14 forms homooligomeric assemblies via its BTB domain,
    likely as pentamers based on family-wide structural analysis. The primary molecular
    function beyond oligomerization remains to be determined experimentally.'
  term_context: '- Molecular function: identical protein binding (GO:0042802)

    - Description: KCTD14 forms homooligomeric assemblies via its BTB domain, likely
    as pentamers based on family-wide structural analysis. The primary molecular function
    beyond oligomerization remains to be determined experimentally.

    - Directly involved in: protein homooligomerization (GO:0051260)'
  reference_context: '- file:human/KCTD14/KCTD14-deep-research-falcon.md'
  source_file: genes/human/KCTD14/KCTD14-ai-review.yaml
  source_selector: core_functions[1]
  source_context_yaml: "description: KCTD14 forms homooligomeric assemblies via its\
    \ BTB domain, likely as pentamers based on family-wide\n  structural analysis.\
    \ The primary molecular function beyond oligomerization remains to be determined\n\
    \  experimentally.\nmolecular_function:\n  id: GO:0042802\n  label: identical\
    \ protein binding\ndirectly_involved_in:\n- id: GO:0051260\n  label: protein homooligomerization\n\
    supported_by:\n- reference_id: file:human/KCTD14/KCTD14-deep-research-falcon.md\n\
    \  supporting_text: KCTD14 is expected to oligomerize via its BTB domain, most\
    \ commonly as a homopentamer,\n    in keeping with the family trend"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 17
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** KCTD14
- **Gene symbol:** KCTD14
- **UniProt accession:** Q9BQ13

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0042802
- **Source file:** genes/human/KCTD14/KCTD14-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

identical protein binding (GO:0042802) is a core function of KCTD14. Current rationale: KCTD14 forms homooligomeric assemblies via its BTB domain, likely as pentamers based on family-wide structural analysis. The primary molecular function beyond oligomerization remains to be determined experimentally.

## Term and Decision Context

- Molecular function: identical protein binding (GO:0042802)
- Description: KCTD14 forms homooligomeric assemblies via its BTB domain, likely as pentamers based on family-wide structural analysis. The primary molecular function beyond oligomerization remains to be determined experimentally.
- Directly involved in: protein homooligomerization (GO:0051260)

## Reference Context

- file:human/KCTD14/KCTD14-deep-research-falcon.md

## Source Context YAML

```yaml
description: KCTD14 forms homooligomeric assemblies via its BTB domain, likely as pentamers based on family-wide
  structural analysis. The primary molecular function beyond oligomerization remains to be determined
  experimentally.
molecular_function:
  id: GO:0042802
  label: identical protein binding
directly_involved_in:
- id: GO:0051260
  label: protein homooligomerization
supported_by:
- reference_id: file:human/KCTD14/KCTD14-deep-research-falcon.md
  supporting_text: KCTD14 is expected to oligomerize via its BTB domain, most commonly as a homopentamer,
    in keeping with the family trend
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

# KCTD14 Core Function Hypothesis: Identical Protein Binding (GO:0042802)

## Executive Judgment

**Verdict: Partially supported — valid annotation lead but should not be designated as core function**

The hypothesis that identical protein binding (GO:0042802) is a core function of KCTD14 is **partially supported** as a factual description of what KCTD14 likely does, but **weakly supported** as a core function designation. Two lines of evidence confirm KCTD14 self-association: (1) yeast two-hybrid self-interaction data from the proteome-scale HI-II-14 interactome ([PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/)), and (2) AlphaFold multimer predictions yielding reliable pentameric models with a distinctive circle-like CTD organization ([PMID: 36362127](https://pubmed.ncbi.nlm.nih.gov/36362127/)). Family-wide structural studies using electron microscopy and X-ray crystallography corroborate that BTB-mediated pentamerization is the norm across the KCTD family ([PMID: 27152988](https://pubmed.ncbi.nlm.nih.gov/27152988/); [PMID: 26334369](https://pubmed.ncbi.nlm.nih.gov/26334369/)).

However, the critical curation issue is whether self-binding constitutes a "core function" or merely a structural prerequisite that enables core function. For every experimentally characterized KCTD family member, oligomerization is the assembly step that enables the protein's primary molecular activity — serving as a Cullin3 E3 ubiquitin ligase adaptor, modulating Gβγ signaling, or scaffolding receptor complexes. Treating the scaffold assembly as the core function is analogous to designating "protein folding" as the core function of a kinase. GO:0042802 is a valid annotation lead with IPI evidence, but it should be treated as **non-core**; KCTD14's primary molecular function beyond oligomerization remains experimentally undetermined.

Two additional caveats sharpen this assessment. First, GO:0042802 is **not currently annotated** for KCTD14 in QuickGO — only GO:0051260 (protein homooligomerization, IEA) and GO:0005515 (protein binding, IPI) exist — so the hypothesis proposes both a new annotation and its elevation to core status simultaneously. Second, the Y2H evidence comes from a single high-throughput study with moderate confidence (MI-score 0.37, 3/4 replicas), without independent biochemical validation of the interaction or its stoichiometry.

---

## Summary

KCTD14 (UniProt: Q9BQ13) is a member of the 25-member potassium channel tetramerization domain (KCTD) protein family in humans. Like most family members, it contains an N-terminal BTB (bric-à-brac, tramtrack, broad complex) domain that mediates oligomerization, and a C-terminal domain (CTD) of less-well-characterized function. The seed hypothesis proposes that identical protein binding (GO:0042802) — the capacity to bind copies of itself — represents a core molecular function of KCTD14, based on its predicted pentameric assembly via the BTB domain.

Our investigation confirmed the self-interaction through direct evidence (Y2H) and computational prediction (AlphaFold pentameric modeling), supplemented by extensive family-wide structural data showing pentamerization as the default state for KCTD BTB domains. However, for every characterized KCTD family member, BTB-mediated oligomerization enables downstream molecular activities: Cullin3 E3 ubiquitin ligase adaptor function (KCTD5, KCTD6, KCTD9, KCTD11, KCTD17), Gβγ modulation (KCTD2, KCTD5, KCTD12, KCTD16), GABAB receptor regulation (KCTD8, KCTD12, KCTD16), or developmental pathway control (KCTD1, KCTD11). For KCTD14 specifically, none of these downstream functions have been experimentally confirmed, and the protein remains one of the least-characterized members of the family.

The most informative action for curators is to consider adding GO:0042802 as a non-core MF annotation with IPI evidence from PMID:25416956, while explicitly noting that the core molecular function remains undetermined. Candidate core functions to monitor include Cullin3 adaptor activity (by closest-paralog KCTD7 analogy), Gβγ subunit modulation (by family-wide screen data), and a potential immunomodulatory role via the TNF-TNFR1 axis (recently proposed computationally for pancreatic cancer).

---

## Key Findings

### Finding 1: KCTD14 Self-Interaction Detected by Yeast Two-Hybrid

The most direct experimental evidence for KCTD14 identical protein binding comes from the HI-II-14 proteome-scale human binary interactome map ([PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/)). Rolland et al. (2014) systematically mapped approximately 14,000 high-quality human binary protein-protein interactions using a yeast two-hybrid (Y2H) array approach. Their study, described as providing "reference maps of interactome networks [that] will be critical to fully understand genotype-phenotype relationships," detected KCTD14 (Q9BQ13) self-interaction in 3 out of 4 replicas (IntAct accession: EBI-10487331, MI-score: 0.37, MI method: MI:0397 — two-hybrid array).

This Y2H self-interaction constitutes the experimental basis for any potential GO:0042802 annotation. The evidence is genuine but has important limitations: Y2H operates in yeast, not in human cells; it detects binary interactions between fusion proteins that may not reflect full-length protein behavior or native oligomeric context; and the MI-score of 0.37 is moderate, consistent with high-throughput detection rather than focused biochemical validation. Notably, the self-interaction data exists in IntAct but has been annotated to the broader GO:0005515 (protein binding) rather than the more specific GO:0042802 (identical protein binding), suggesting GO curators have not yet propagated this evidence to the more specific term.

### Finding 2: AlphaFold Predicts KCTD14 Pentameric Assembly with Distinctive CTD Organization

Esposito et al. (2022) applied AlphaFold multimer predictions to model oligomeric states of all KCTD family members ([PMID: 36362127](https://pubmed.ncbi.nlm.nih.gov/36362127/)). Their approach "led to the identification of reliable three-dimensional models for the pentameric states of KCNRG, KCTD6, KCTD4, KCTD7, KCTD9, and KCTD14 and possibly for KCTD11 and KCTD21 that are involved in key biological processes and that were previously uncharacterized from a structural point of view." Critically, the study revealed a distinctive structural signature for the KCTD7/14 subclade: "the structure of the related proteins KCTD7 and KCTD14, although pentameric, appears to be characterized by a different organization of the CTD region, with the five chains forming a circle-like structure with a large cavity." This contrasts with the propeller-like CTD arrangement seen in other KCTD family members.

The AlphaFold monomer model for KCTD14 (AF-Q9BQ13-F1) has a mean pLDDT of 85.88, indicating high overall confidence. The pentameric prediction provides specific structural context for the self-interaction — predicting not just that KCTD14 self-associates but that it does so as a specific pentameric ring with an unusual CTD architecture. However, these remain computational predictions; no crystal structure, cryo-EM structure, or solution biophysics data exist for KCTD14 itself.

### Finding 3: KCTD Family BTB Domains Prevalently Form Pentamers — Structural Evidence from Related Members

The structural basis for KCTD self-interaction is robustly established at the family level through converging experimental approaches:

- **Electron microscopy:** Smaldone et al. (2016) examined BTB domains from 7 KCTD members spanning 5 major phylogenetic clades and found that their "present electron microscopy data highlight the occurrence of well-defined pentameric states for all domains" ([PMID: 27152988](https://pubmed.ncbi.nlm.nih.gov/27152988/)).

- **X-ray crystallography:** Ji et al. (2016) reported pentameric crystal structures of the KCTD1 and KCTD9 BTB domains and demonstrated that Cul3 binding affinity varies — "KCTD proteins 5, 6, 9 and 17 bind to Cul3 with high affinity, while the KCTD proteins 1 and 16 do not have detectable binding" ([PMID: 26334369](https://pubmed.ncbi.nlm.nih.gov/26334369/)). Pinkas et al. (2017) added crystal structures for additional members, noting that "Members of the potassium channel tetramerization domain (KCTD) family are soluble non-channel proteins that commonly function as Cullin3 (Cul3)-dependent E3 ligases" ([PMID: 28963344](https://pubmed.ncbi.nlm.nih.gov/28963344/)).

- **Molecular dynamics simulations:** Balasco et al. (2019) demonstrated that "KCTD-BTB domains are stable in the simulation timescales, even in their monomeric forms" and that open pentameric states relate to functional roles ([PMID: 31370201](https://pubmed.ncbi.nlm.nih.gov/31370201/)).

One important exception is KCTD11, which forms tetramers rather than pentamers ([PMID: 21237243](https://pubmed.ncbi.nlm.nih.gov/21237243/)), demonstrating that the oligomeric state is not invariant across the family and cannot be automatically assumed for unstudied members.

### Finding 4: GO:0042802 Is Not Currently Annotated for KCTD14 in QuickGO

Examination of the current GO annotation status for Q9BQ13 revealed that GO:0042802 (identical protein binding) is **not currently assigned**. The existing annotations are:

| GO Term | GO ID | Evidence Code | Source |
|---------|-------|---------------|--------|
| protein homooligomerization | GO:0051260 | IEA | InterPro IPR003131 |
| protein binding | GO:0005515 | IPI | IntAct (PMIDs: 25416956, 28514442, 29892012, 33961781) |

The IPI-supported GO:0005515 annotation encompasses interactions with STK16, TCF4, and ACSF3 in addition to the self-interaction. The Y2H self-interaction data from PMID:25416956 exists in IntAct but has not been propagated to GO:0042802. This means the seed hypothesis proposes both a new annotation and its elevation to core status — a step requiring stronger justification than is currently available.

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence & Limitations |
|---|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| 1 | [PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) (Rolland et al. 2014) | Direct assay (Y2H) | **Supports** | KCTD14 binds itself | Self-interaction detected in 3/4 replicas; MI-score 0.37 | Human proteins in yeast Y2H; HI-II-14 systematic screen | Moderate. Single method, HT screen, no biochemical validation |
| 2 | [PMID: 36362127](https://pubmed.ncbi.nlm.nih.gov/36362127/) (Esposito et al. 2022) | Computational (AlphaFold) | **Supports** | KCTD14 forms pentamers | Reliable pentameric model with distinctive circle-like CTD | In silico (AlphaFold2-multimer) | Moderate. Prediction, not experimental; validated for other KCTDs |
| 3 | [PMID: 27152988](https://pubmed.ncbi.nlm.nih.gov/27152988/) (Smaldone et al. 2016) | Structural/evolutionary (EM) | **Supports** (by analogy) | KCTD BTB domains pentamerize | Pentameric states for all 7 tested BTB domains across 5 clades | In vitro EM, recombinant BTB domains | High for family; KCTD14 not directly tested |
| 4 | [PMID: 26334369](https://pubmed.ncbi.nlm.nih.gov/26334369/) (Ji et al. 2016) | Structural (X-ray, cryo-EM) | **Supports** (by analogy) | KCTD proteins form pentameric rings | Crystal structures of KCTD1 and KCTD9 BTB pentamers; Cul3 binding varies | In vitro | High for family; demonstrates Cul3-binding variability |
| 5 | [PMID: 28963344](https://pubmed.ncbi.nlm.nih.gov/28963344/) (Pinkas et al. 2017) | Structural (X-ray) | **Supports** (by analogy) | KCTDs are pentameric Cul3 adaptors | Crystal structures confirm pentameric assemblies; KCTDs commonly function as Cul3 E3 ligases | In vitro | High for family; inferential for KCTD14 |
| 6 | [PMID: 31370201](https://pubmed.ncbi.nlm.nih.gov/31370201/) (Balasco et al. 2019) | Computational (MD) | **Supports** (by analogy) | BTB domain stability in oligomeric states | MD simulations show stability in various oligomeric states including pentamers | In silico | Moderate. KCTD14 not specifically modeled |
| 7 | [PMID: 36736897](https://pubmed.ncbi.nlm.nih.gov/36736897/) (Barthet/Sloan et al. 2023) | Direct assay (co-IP, BRET) | **Qualifies** | KCTDs interact with Gβγ | Nearly all 25 KCTDs interact with Gβγ; functional consequence on cAMP signaling | HEK293 cells; family-wide screen | Moderate. Suggests alternative core function beyond self-binding |
| 8 | [PMID: 37762619](https://pubmed.ncbi.nlm.nih.gov/37762619/) (Bhatt/Liao et al. 2023) | Direct assay (co-IP, BRET) | **Qualifies** | KCTDs form hetero-oligomers | KCTD5 forms hetero-oligomeric complexes with various family members | HEK293 cells | Moderate. Complicates "identical protein binding" as sole interaction mode |
| 9 | [PMID: 22748208](https://pubmed.ncbi.nlm.nih.gov/22748208/) (Staropoli et al. 2012) | Direct assay (paralog KCTD7) | **Qualifies** | KCTD7-Cullin3 interaction | KCTD7 R184C mutation abrogated Cullin3 interaction | Human KCTD7 in cell-based assays | High for KCTD7. Suggests Cul3 adaptor is the core function for the clade |
| 10 | [PMID: 30295347](https://pubmed.ncbi.nlm.nih.gov/30295347/) (Metz et al. 2018) | Direct assay (paralog KCTD7) | **Qualifies** | KCTD7 disease mechanism | KCTD7 mutations impair Cul3 binding and autophagy | Patient fibroblasts, yeast | High for KCTD7. Core function is Cul3-dependent, not just self-binding |
| 11 | [PMID: 41080575](https://pubmed.ncbi.nlm.nih.gov/41080575/) (Liang et al. 2025) | Computational/functional | **Competing** | KCTD14 immunomodulatory function | KCTD14 implicated as immunomodulatory oncogene via TNF-TNFR1 axis in PC | Computational + scRNA-seq | Low. Indirect, computational, requires experimental validation |
| 12 | [PMID: 21237243](https://pubmed.ncbi.nlm.nih.gov/21237243/) (Dementieva et al. 2011) | Structural (biophysical) | **Qualifies** | All KCTDs pentamerize | KCTD11 forms tetramers, not pentamers | In vitro (gel filtration, light scattering) | High. Demonstrates that pentamerization is not universal in the family |
| 13 | QuickGO/UniProt (database) | Database/computational | **Qualifies** | Current annotation status | GO:0042802 not annotated despite Y2H evidence in IntAct | Database records 2026-07 | High. Confirms this is a proposed new annotation, not an existing one |

---

## GO Curation Implications

### Current Annotation Status

KCTD14 (Q9BQ13) has a minimal GO annotation profile:

- **GO:0051260** (protein homooligomerization, BP) — IEA from InterPro IPR003131. Appropriately assigned based on the BTB domain, which is the canonical oligomerization motif for this family.
- **GO:0005515** (protein binding, MF) — IPI from IntAct, supported by multiple PMIDs. This covers both the self-interaction and heteromeric interactions with STK16, TCF4, and ACSF3.
- **GO:0042802** (identical protein binding, MF) — **Not currently annotated**, despite the Y2H self-interaction evidence existing in IntAct.

### Assessment of GO:0042802 as Core Function

**The proposed annotation GO:0042802 is technically justifiable as an MF annotation but should NOT be treated as a core function.** The reasoning is threefold:

1. **As a GO MF annotation:** GO:0042802 could be validly assigned based on the Y2H self-interaction from [PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/), using IPI evidence code. This would represent a more specific annotation than the currently assigned GO:0005515 and would accurately capture the observed self-interaction. This is a legitimate annotation lead.

2. **As a core function:** Identical protein binding is a *prerequisite activity* shared across virtually all KCTD family members. It enables the protein's actual downstream function but is not itself the endpoint activity. For characterized family members, the core molecular function is typically Cullin3 E3 ubiquitin ligase adaptor activity, Gβγ binding and GPCR signal modulation, or receptor scaffolding. Designating self-binding as the core function for KCTD14 is premature and mechanistically superficial.

3. **Comparison with paralogs:** For KCTD7 (the closest paralog), disease-causing mutations disrupt Cullin3 binding and autophagy-lysosome function — not oligomerization per se ([PMID: 30295347](https://pubmed.ncbi.nlm.nih.gov/30295347/); [PMID: 22748208](https://pubmed.ncbi.nlm.nih.gov/22748208/)). This strongly suggests that the core function of the KCTD7/14 subclade lies downstream of self-assembly.

### Recommended Curation Actions (Leads for Curator Verification)

- **Retain** GO:0051260 (protein homooligomerization, BP) — well-supported by domain architecture and family-wide evidence
- **Consider adding** GO:0042802 (identical protein binding, MF) with IPI evidence from [PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) — but flag as non-core
- **Do not designate** GO:0042802 as core MF — the true core molecular function is undetermined
- **Monitor** Cullin3 adaptor activity, Gβγ modulation, and TNF-TNFR1 axis involvement as candidate core functions pending experimental data

---

## Mechanistic Scope

### Direct Gene-Product Activity

The immediate molecular activity under evaluation is **self-binding** — the ability of KCTD14 monomers to associate into homo-oligomeric (likely pentameric) complexes via the BTB domain. This is a well-supported structural property, but it is mechanistically **upstream** of the protein's biological role. The assembly hierarchy can be represented as:

```
KCTD14 monomer
    ↓ BTB domain-mediated self-association
Pentameric BTB ring (predicted)
    ↓ CTD region forms circle-like structure with large cavity
Full-length pentameric assembly
    ↓ [UNKNOWN — no experimental data for KCTD14]
    ├── Cullin3 binding? → E3 ubiquitin ligase complex → substrate ubiquitination
    ├── Gβγ binding? → GPCR signal modulation → cAMP pathway effects
    ├── TNF-TNFR1 axis? → immunomodulation (computational evidence only)
    └── Novel function? → unknown biological process
```

### What Self-Binding Enables — Family Analogies

For characterized KCTD family members, the pentameric BTB ring serves as a platform for three main classes of molecular activity:

| KCTD Member(s) | Downstream Function | Core MF | Evidence Level |
|----------------|--------------------|---------|----|
| KCTD5, KCTD6, KCTD9, KCTD11, KCTD17 | Cullin3 E3 ubiquitin ligase adaptor | Ubiquitin ligase complex component | Crystal structures, biochemistry |
| KCTD2, KCTD5, KCTD12, KCTD16 | Gβγ binding → GPCR modulation | G protein modulator | Co-IP, BRET, functional assays |
| KCTD8, KCTD12, KCTD12b, KCTD16 | GABAB receptor regulation | Receptor auxiliary subunit | Co-IP, electrophysiology |
| KCTD7 (closest paralog) | Cul3-dependent autophagy-lysosome regulation | Cul3 adaptor | Genetics, cell biology |
| **KCTD14** | **Unknown** | **Unknown** | — |

### Separation of Direct Activity from Downstream Phenotypes

KCTD14 has been identified in several transcriptomic and computational disease studies, but these represent expression-level associations that do not inform molecular function:

- **Dengue infection:** KCTD14 upregulated in dengue patients regardless of severity ([PMID: 39397194](https://pubmed.ncbi.nlm.nih.gov/39397194/); [PMID: 35220956](https://pubmed.ncbi.nlm.nih.gov/35220956/)) — transcriptomic correlation, not MF evidence
- **Pancreatic cancer:** KCTD14 identified as potential immunomodulatory oncogene via TNF-TNFR1 axis ([PMID: 41080575](https://pubmed.ncbi.nlm.nih.gov/41080575/)) — computational/scRNA-seq inference, not validated
- **Ovarian cancer:** KCTD14 included in DNA methylation-related prognostic signature ([PMID: 36978087](https://pubmed.ncbi.nlm.nih.gov/36978087/)) — statistical association only
- **Diabetes:** KCTD14 transcript altered in diabetic rat colon ([PMID: 34806320](https://pubmed.ncbi.nlm.nih.gov/34806320/)) — rat model, low fold-change

None of these disease-context findings should influence GO MF annotation for KCTD14.

---

## Conflicts and Alternatives

### 1. Hetero-Oligomerization Complicates "Identical Protein Binding"

Bhatt et al. (2023) demonstrated that KCTD5 forms hetero-oligomeric complexes with various KCTD family members, with "different regions on KCTD5 responsible for uniquely contributing to interactions with other KCTD proteins" ([PMID: 37762619](https://pubmed.ncbi.nlm.nih.gov/37762619/)). The authors concluded that "KCTD hetero-oligomeric interactions may occur throughout the KCTD family." If KCTD14 preferentially forms hetero-oligomers in vivo (e.g., with KCTD7 or other family members), then GO:0042802 (identical protein binding) would be an incomplete or misleading annotation. The Y2H self-interaction assay cannot distinguish between a protein that exclusively forms homo-oligomers and one that can also form hetero-oligomers.

### 2. Cullin3 Adaptor Activity as the True Core Function

The closest paralog, KCTD7, has well-established Cullin3 interaction: Staropoli et al. (2012) showed that the R184C mutation "abrogated interaction with cullin-3, a ubiquitin-ligase component and known KCTD7 interactor" ([PMID: 22748208](https://pubmed.ncbi.nlm.nih.gov/22748208/)), and Metz et al. (2018) demonstrated that KCTD7 mutations impair autophagy through Cul3-dependent pathways ([PMID: 30295347](https://pubmed.ncbi.nlm.nih.gov/30295347/)). If KCTD14 similarly functions as a Cul3 adaptor, then its core MF would be related to ubiquitin ligase activity, not self-binding.

However, not all KCTDs bind Cul3. Ji et al. (2016) found that "KCTD proteins 1 and 16 do not have detectable binding" to Cul3 despite having functional BTB domains ([PMID: 26334369](https://pubmed.ncbi.nlm.nih.gov/26334369/)). Whether KCTD14 falls in the Cul3-binding or non-binding subgroup has not been tested.

### 3. Gβγ Modulation as an Alternative Core Function

The family-wide screen by Sloan/Barthet et al. (2023) demonstrated that "nearly all the 25 KCTD proteins interact with Gβγ" with functional consequences for adenylyl cyclase-cAMP signaling ([PMID: 36736897](https://pubmed.ncbi.nlm.nih.gov/36736897/)). KCTD14 was included in this screen. If Gβγ binding proves to be KCTD14's primary signaling role, the core MF would shift toward G-protein modulation rather than self-binding.

### 4. Paralog Confusion Risk with KCTD7

KCTD14 and KCTD7 form a distinct subclade with shared structural features (circle-like CTD, large cavity) ([PMID: 36362127](https://pubmed.ncbi.nlm.nih.gov/36362127/)). KCTD7 is well-characterized as a disease gene (progressive myoclonic epilepsy EPM3/CLN14) with Cul3 interaction and autophagy-lysosome involvement. There is a risk of inappropriately transferring KCTD7 annotations to KCTD14 without direct experimental evidence. KCTD14 may have distinct substrates, tissue expression, and biological roles despite sharing structural organization with KCTD7.

### 5. Oligomeric State Exceptions

KCTD11 forms tetramers rather than pentamers ([PMID: 21237243](https://pubmed.ncbi.nlm.nih.gov/21237243/)), showing that the oligomeric state cannot be automatically assumed for untested members. While the AlphaFold prediction for KCTD14 specifically indicates a pentameric state, this has not been experimentally validated.

---

## Knowledge Gaps

| Gap | What Was Checked | Why It Matters | Resolving Evidence |
|-----|-----------------|----------------|-------------------|
| **No direct biochemical characterization of KCTD14** | PubMed literature, UniProt, IntAct | Cannot confirm oligomeric state, binding affinity, or stoichiometry | Recombinant expression + SEC-MALS, analytical ultracentrifugation, or native MS |
| **No experimental structure** | PDB search (no entries); AlphaFold DB (monomer model, pLDDT 85.88) | Pentameric prediction is computational only; circle-like CTD cavity is unverified | X-ray crystallography or cryo-EM of KCTD14 BTB domain and/or full-length protein |
| **Cullin3 binding status unknown** | Literature on KCTD-Cul3 interactions; KCTD14 not tested in any study | Determines whether E3 ligase adaptor is a candidate core function | Co-IP or ITC of KCTD14 with Cul3 N-terminal domain |
| **Gβγ binding specifics unknown** | Family-wide screen ([PMID: 36736897](https://pubmed.ncbi.nlm.nih.gov/36736897/)) included KCTD14 but individual data not reported in detail | If confirmed, would suggest GPCR modulation as core function | Focused BRET/co-IP with domain deletions |
| **Substrate identity unknown** | No data available | If KCTD14 is a Cul3 adaptor, the substrate defines its specific biological role | Proximity labeling (BioID/TurboID) or ubiquitin remnant profiling |
| **In vivo oligomeric state unknown** | Y2H detects binary interactions only | Actual stoichiometry in human cells may differ from predictions | BRET titration, cross-linking MS, or fluorescence fluctuation spectroscopy |
| **Hetero-oligomerization partners unknown** | KCTD5 hetero-oligomers studied ([PMID: 37762619](https://pubmed.ncbi.nlm.nih.gov/37762619/)); KCTD14 not specifically tested | If KCTD14 preferentially hetero-oligomerizes, GO:0042802 may be secondary | Co-IP screen with all KCTD family members |
| **Tissue/cell expression context** | Disease transcriptomics mention KCTD14 in dengue, cancer, diabetes | Expression pattern constrains which functions are physiologically relevant | GTEx/HPA queries, single-cell atlas data |

---

## Discriminating Tests

### Priority 1: Confirm Self-Interaction and Determine Stoichiometry
- **Recombinant KCTD14 BTB domain expression** followed by size-exclusion chromatography coupled with multi-angle light scattering (SEC-MALS) to determine native oligomeric state
- **Analytical ultracentrifugation** (AUC) to confirm or refute the pentameric stoichiometry predicted by AlphaFold
- **Co-immunoprecipitation with differentially epitope-tagged constructs** in human cells (e.g., FLAG-KCTD14 + HA-KCTD14) to validate Y2H self-interaction in a mammalian context

### Priority 2: Test Cullin3 Adaptor Activity
- **Co-immunoprecipitation or pull-down** of KCTD14 with the Cul3 N-terminal domain, following the approach used for KCTD5, KCTD9, and KCTD7
- **Isothermal titration calorimetry** (ITC) to measure binding affinity, as performed for KCTD5-Cul3 (Kd = 59 nM; [PMID: 24747150](https://pubmed.ncbi.nlm.nih.gov/24747150/))
- If Cul3 binding confirmed: **in vitro ubiquitination assay** with candidate substrates

### Priority 3: Characterize Gβγ Interaction
- **Focused BRET assay** with KCTD14 and Gβγ subunits, including agonist-dependence testing
- **Domain deletion mapping** to identify whether the BTB, CTD, or both regions mediate Gβγ binding
- **Functional readout:** adenylyl cyclase 5 sensitization assay to test whether KCTD14 blunts Gβγ-mediated cAMP signaling, as shown for other KCTDs ([PMID: 36736897](https://pubmed.ncbi.nlm.nih.gov/36736897/))

### Priority 4: Structural Determination
- **Cryo-EM** of full-length KCTD14 pentamer to verify the distinctive circle-like CTD cavity predicted by AlphaFold
- **X-ray crystallography** of the BTB domain to compare with other family members
- These would definitively resolve the oligomeric state and provide a structural basis for understanding specificity

### Priority 5: Identify Biological Context and Substrates
- **BioID/TurboID proximity labeling** with KCTD14 as bait in relevant cell types to identify the in vivo interactome
- **CRISPR knockout** followed by transcriptomic and proteomic profiling to identify downstream effects
- **Tissue expression profiling** using GTEx, Human Protein Atlas, and single-cell atlas data to identify primary sites of function

---

## Curation Leads

*All items below are leads requiring curator verification.*

### Lead 1: Add GO:0042802 as Non-Core MF Annotation
- **Action:** Consider annotating GO:0042802 (identical protein binding) for Q9BQ13 with IPI evidence code
- **Reference:** [PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) (Rolland et al. 2014)
- **Snippet to verify:** "Just as reference genome sequences revolutionized human genetics, reference maps of interactome networks will be critical to fully understand genotype-phenotype relationships. Here, we describe a systematic map of ~14,000 high-quality human binary protein-protein interactions."
- **IntAct accession:** EBI-10487331 (KCTD14 self-interaction, Q9BQ13-Q9BQ13)
- **Caveat:** Y2H detects binary interactions; does not confirm oligomeric stoichiometry. Should be flagged as non-core function.

### Lead 2: Retain GO:0051260 but Consider Evidence Upgrade
- **Action:** Retain GO:0051260 (protein homooligomerization) and consider whether AlphaFold pentamer predictions warrant ISS or IC evidence upgrade from IEA
- **Reference:** [PMID: 36362127](https://pubmed.ncbi.nlm.nih.gov/36362127/) (Esposito et al. 2022)
- **Snippet to verify:** "our approach led to the identification of reliable three-dimensional models for the pentameric states of KCNRG, KCTD6, KCTD4, KCTD7, KCTD9, and KCTD14 and possibly for KCTD11 and KCTD21 that are involved in key biological processes and that were previously uncharacterized from a structural point of view"
- **Question for curator:** Does the combination of Y2H self-interaction + AlphaFold pentamer prediction + family-wide EM data warrant upgrading from IEA to a manually assigned evidence code?

### Lead 3: Do Not Designate Self-Binding as Core Function
- **Rationale:** For every experimentally characterized KCTD family member, BTB-mediated oligomerization enables the protein's downstream molecular activity — it is the assembly step, not the functional output. The KCTD7/14 subclade data specifically suggest Cullin3 adaptor activity as the likely core function. Until KCTD14's primary molecular activity is determined, the core MF slot should remain open.
- **Suggested action:** Annotate GO:0042802 but note it as a structural/assembly property rather than core function. Add a curator note that the primary molecular function beyond oligomerization is experimentally undetermined.

### Lead 4: Monitor Emerging Functional Evidence
- **Gβγ binding:** [PMID: 36736897](https://pubmed.ncbi.nlm.nih.gov/36736897/) — "we report that nearly all the 25 KCTD proteins interact with Gβγ" — family-wide screen suggesting alternative core function
- **TNF-TNFR1 axis:** [PMID: 41080575](https://pubmed.ncbi.nlm.nih.gov/41080575/) — "highlights KCTD14 as a novel immunomodulatory oncogene acting through the TNF-TNFR1 axis" — computational evidence in pancreatic cancer
- **Autophagy/lysosome connection:** If KCTD14 shares functional parallels with KCTD7 ([PMID: 30295347](https://pubmed.ncbi.nlm.nih.gov/30295347/)), autophagy-related GO terms may become relevant

### Lead 5: Candidate GO Terms for Future Consideration
If downstream function is experimentally established, consider:

| Candidate GO Term | GO ID | Ontology | Condition |
|-------------------|-------|----------|-----------|
| Cul3-RING ubiquitin ligase complex | GO:0031463 | CC | If Cul3 binding confirmed |
| ubiquitin protein ligase binding | GO:0031625 | MF | If Cul3 binding confirmed |
| Gβγ-subunit complex binding | GO:0002058 (or related) | MF | If Gβγ interaction confirmed as primary activity |
| ubiquitin-dependent protein catabolic process | GO:0006511 | BP | If E3 ligase substrate adaptor role confirmed |

### Lead 6: Relationship Between GO:0042802 and GO:0051260
- **GO:0042802** (identical protein binding) is an MF term describing the binding activity itself
- **GO:0051260** (protein homooligomerization) is a BP term describing the process outcome
- These are complementary, not redundant — if GO:0042802 is added as MF, it should complement rather than replace GO:0051260
- For a gene with minimal experimental characterization, the BP term GO:0051260 may be more informative because it specifies the *outcome* (homo-oligomeric assembly) rather than just the binding activity

---

## Evidence Base: Key Literature

### Primary Evidence for KCTD14

**Rolland et al. (2014)** — *A proteome-scale map of the human interactome network.* [PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/)
The HI-II-14 interactome provides the only direct experimental evidence for KCTD14 self-interaction. This systematic Y2H study detected KCTD14 self-binding in 3 of 4 replicas (MI-score 0.37). This is the foundation for any potential GO:0042802 annotation and represents the most important primary evidence for this hypothesis.

**Esposito et al. (2022)** — *AlphaFold Predictions Provide Insights into the Structural Features of the Functional Oligomers of All Members of the KCTD Family.* [PMID: 36362127](https://pubmed.ncbi.nlm.nih.gov/36362127/)
Used AlphaFold multimer to predict oligomeric states for all KCTD members. Identified reliable pentameric models for KCTD14 and revealed its distinctive circle-like CTD architecture shared with KCTD7. This is the most detailed structural information available for KCTD14, albeit computational.

### Family-Wide Structural Evidence

**Smaldone et al. (2016)** — *The BTB domains of the potassium channel tetramerization domain proteins prevalently assume pentameric states.* [PMID: 27152988](https://pubmed.ncbi.nlm.nih.gov/27152988/)
EM data establishing pentamerization as the norm for KCTD BTB domains across multiple phylogenetic clades.

**Ji et al. (2016)** — *Structural Insights into KCTD Protein Assembly and Cullin3 Recognition.* [PMID: 26334369](https://pubmed.ncbi.nlm.nih.gov/26334369/)
Crystal structures of KCTD1 and KCTD9 BTB pentamers. Crucially demonstrated that Cul3 binding affinity varies across the family — KCTD1 and KCTD16 do not detectably bind Cul3, challenging the assumption that all KCTDs are Cul3 adaptors.

**Pinkas et al. (2017)** — *Structural complexity in the KCTD family of Cullin3-dependent E3 ubiquitin ligases.* [PMID: 28963344](https://pubmed.ncbi.nlm.nih.gov/28963344/)
Additional crystal structures establishing that KCTDs "commonly function as Cullin3 (Cul3)-dependent E3 ligases." Provides the structural framework for understanding KCTD oligomerization as a means to Cul3 binding.

**Balasco et al. (2019)** — *The Structural Versatility of the BTB Domains of KCTD Proteins.* [PMID: 31370201](https://pubmed.ncbi.nlm.nih.gov/31370201/)
MD simulations showing BTB domain stability across oligomeric states and demonstrating that open pentameric conformations relate to functional roles, not structural instability.

### Closest Paralog KCTD7

**Staropoli et al. (2012)** — *A homozygous mutation in KCTD7 links neuronal ceroid lipofuscinosis to the ubiquitin-proteasome system.* [PMID: 22748208](https://pubmed.ncbi.nlm.nih.gov/22748208/)
Demonstrated that KCTD7 mutations can abrogate Cullin3 interaction, linking the KCTD7/14 subclade to the ubiquitin-proteasome system. The R184C mutation "abrogated interaction with cullin-3."

**Metz et al. (2018)** — *KCTD7 deficiency defines a distinct neurodegenerative disorder with a conserved autophagy-lysosome defect.* [PMID: 30295347](https://pubmed.ncbi.nlm.nih.gov/30295347/))
Showed that KCTD7 mutations cause impaired autophagy through Cul3-dependent mechanisms, establishing that the core function of KCTD7 is Cul3-dependent — not merely self-binding.

### Family-Wide Functional Studies

**Sloan/Barthet et al. (2023)** — *Multiple potassium channel tetramerization domain (KCTD) family members interact with Gβγ, with effects on cAMP signaling.* [PMID: 36736897](https://pubmed.ncbi.nlm.nih.gov/36736897/)
Family-wide screen showing nearly all KCTDs interact with Gβγ, with functional consequences for cAMP signaling. Raises the possibility that Gβγ modulation, not self-binding, is a more informative core function annotation for KCTD14.

**Bhatt/Liao et al. (2023)** — *KCTD5 Forms Hetero-Oligomeric Complexes with Various Members of the KCTD Protein Family.* [PMID: 37762619](https://pubmed.ncbi.nlm.nih.gov/37762619/)
Demonstrated that KCTD hetero-oligomerization is widespread, suggesting KCTD14 may form mixed complexes in vivo — complicating the exclusive "identical protein binding" annotation.

### Disease Context (Not MF Evidence)

**Liang et al. (2025)** — *Dendritic cell-related gene signature in pancreatic cancer stratifies patient subtypes and implicates a KCTD14-TNF signaling axis.* [PMID: 41080575](https://pubmed.ncbi.nlm.nih.gov/41080575/)
Computational/scRNA-seq study proposing KCTD14 as an immunomodulatory oncogene acting through TNF-TNFR1 in pancreatic cancer. While not direct MF evidence, this is the most specific functional claim about KCTD14 in the current literature and warrants monitoring.

---

## Limitations

1. **No direct biochemical characterization of KCTD14 exists.** All functional inferences are based on family analogy, one Y2H result, and computational predictions. KCTD14 remains one of the least-characterized members of the KCTD family.

2. **The Y2H evidence is from a single high-throughput study.** While the HI-II-14 interactome is well-validated at the dataset level, the individual KCTD14 self-interaction has not been independently confirmed by co-immunoprecipitation, BRET, or other orthogonal methods.

3. **AlphaFold predictions are not experimental evidence.** The pentameric model and circle-like CTD cavity, while plausible and consistent with family trends, require experimental validation.

4. **Family-wide functional data cannot be directly transferred to KCTD14.** The KCTD family shows considerable functional diversity: some are Cul3 adaptors, some are GABAB receptor modulators, some bind Gβγ, some do not bind Cul3 at all, and substrate specificity varies widely. Shared BTB domain architecture does not guarantee shared molecular function.

5. **Disease-context transcriptomic associations are not MF evidence.** The recurring identification of KCTD14 in dengue, cancer, and diabetes transcriptomic studies reflects expression changes, not molecular function.

6. **The closely related KCTD7 has strong disease genetics, but even KCTD7's molecular function is incompletely characterized.** While KCTD7 binds Cullin3 and regulates autophagy, the specific substrates and detailed mechanism remain under investigation, limiting knowledge transfer to KCTD14.

7. **This analysis could not programmatically access certain bioinformatics resources** (e.g., live QuickGO API queries, tissue expression data from GTEx/HPA, PDB structure search). Annotation status and expression data were derived from literature and database records available in the knowledge base.

---

## Conclusion

The seed hypothesis that identical protein binding (GO:0042802) is a core function of KCTD14 is **partially supported as a factual claim** about what KCTD14 likely does — it almost certainly self-associates via its BTB domain to form homo-oligomeric assemblies — but is **not justified as a core function designation**. Self-binding is a structural prerequisite shared across the entire KCTD family that enables downstream molecular activities (Cullin3 adaptor function, Gβγ modulation, receptor scaffolding), which are the true core functions for characterized family members. For KCTD14, the downstream molecular function remains experimentally undetermined.

The recommended curation approach is to consider adding GO:0042802 as a non-core MF annotation with IPI evidence from the Y2H self-interaction data ([PMID: 25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/)), while clearly noting that the core molecular function of KCTD14 awaits experimental characterization. The most promising leads for future core function identification are Cullin3 adaptor activity (by KCTD7 analogy), Gβγ modulation (by family-wide screen data), and the computationally proposed TNF-TNFR1 axis involvement.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)