---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:28:36.546991'
end_time: '2026-09-20T20:44:19.925475'
duration_seconds: 943.38
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: csr-1
  gene_symbol: csr-1
  uniprot_accession: H2KZD5
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: corrected-argonaute-mirna-binding-specificity
  hypothesis_text: 'Caenorhabditis elegans Argonaute CSR-1a (H2KZD5, F20D12.1a; CSR-1b
    Q27GU1) binds miRNAs. The exact H2KZD5 leaf PTN000527417 in PTHR22891 descends
    from miRNA-binding IBD PTN001113179. Assess whether guide-loading selectivity,
    domain/phylogenetic divergence or biochemical experiments establish retention
    or loss. Primary PMID19804758 immunopurifies CSR-1-associated 22G RNAs; PMID18007599
    attributes secondary-siRNA-induced slicing to CSR-1. Do these experiments test
    miRNA binding itself, or only recovered guide classes and relative slicing efficiencies?
    A strong 22G preference does not automatically exclude miRNA binding. Distinguish
    physical loading/binding from miRNA-directed slicing and from physiological gene
    regulation. Correct identity is essential: Q17370 is nhr-47 with old csr-1 synonym,
    and deleted Q21992 belonged to LARP-1; neither is this Argonaute.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/worm/csr-1/csr-1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Caenorhabditis elegans Argonaute CSR-1a (H2KZD5,\
    \ F20D12.1a; CSR-1b Q27GU1) binds miRNAs.\n  The exact H2KZD5 leaf PTN000527417\
    \ in PTHR22891 descends from miRNA-binding IBD PTN001113179. Assess\n  whether\
    \ guide-loading selectivity, domain/phylogenetic divergence or biochemical experiments\
    \ establish\n  retention or loss. Primary PMID19804758 immunopurifies CSR-1-associated\
    \ 22G RNAs; PMID18007599 attributes\n  secondary-siRNA-induced slicing to CSR-1.\
    \ Do these experiments test miRNA binding itself, or only recovered\n  guide classes\
    \ and relative slicing efficiencies? A strong 22G preference does not automatically\
    \ exclude\n  miRNA binding. Distinguish physical loading/binding from miRNA-directed\
    \ slicing and from physiological\n  gene regulation. Correct identity is essential:\
    \ Q17370 is nhr-47 with old csr-1 synonym, and deleted\n  Q21992 belonged to LARP-1;\
    \ neither is this Argonaute.'\nfocus_type: function_assignment\ncontext: []\n\
    reference_id: []"
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
citation_count: 8
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: csr1_evidence_matrix.csv
  path: openscientist_artifacts/csr1_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist csr1 evidence matrix
- filename: csr1_go_decision_table.csv
  path: openscientist_artifacts/csr1_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist csr1 go decision table
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

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** csr-1
- **Gene symbol:** csr-1
- **UniProt accession:** H2KZD5

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** corrected-argonaute-mirna-binding-specificity
- **Source file:** genes/worm/csr-1/csr-1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Caenorhabditis elegans Argonaute CSR-1a (H2KZD5, F20D12.1a; CSR-1b Q27GU1) binds miRNAs. The exact H2KZD5 leaf PTN000527417 in PTHR22891 descends from miRNA-binding IBD PTN001113179. Assess whether guide-loading selectivity, domain/phylogenetic divergence or biochemical experiments establish retention or loss. Primary PMID19804758 immunopurifies CSR-1-associated 22G RNAs; PMID18007599 attributes secondary-siRNA-induced slicing to CSR-1. Do these experiments test miRNA binding itself, or only recovered guide classes and relative slicing efficiencies? A strong 22G preference does not automatically exclude miRNA binding. Distinguish physical loading/binding from miRNA-directed slicing and from physiological gene regulation. Correct identity is essential: Q17370 is nhr-47 with old csr-1 synonym, and deleted Q21992 belonged to LARP-1; neither is this Argonaute.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Caenorhabditis elegans Argonaute CSR-1a (H2KZD5, F20D12.1a; CSR-1b Q27GU1) binds miRNAs.
  The exact H2KZD5 leaf PTN000527417 in PTHR22891 descends from miRNA-binding IBD PTN001113179. Assess
  whether guide-loading selectivity, domain/phylogenetic divergence or biochemical experiments establish
  retention or loss. Primary PMID19804758 immunopurifies CSR-1-associated 22G RNAs; PMID18007599 attributes
  secondary-siRNA-induced slicing to CSR-1. Do these experiments test miRNA binding itself, or only recovered
  guide classes and relative slicing efficiencies? A strong 22G preference does not automatically exclude
  miRNA binding. Distinguish physical loading/binding from miRNA-directed slicing and from physiological
  gene regulation. Correct identity is essential: Q17370 is nhr-47 with old csr-1 synonym, and deleted
  Q21992 belonged to LARP-1; neither is this Argonaute.'
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

# AIGR Gene Hypothesis Deep Research — CSR-1 (H2KZD5) "miRNA Binding" Function Assignment

**Target gene:** *csr-1* (CSR-1a / F20D12.1a), *Caenorhabditis elegans* (NCBITaxon:6239)
**UniProt:** H2KZD5 (isoform A, 1030 aa); Q27GU1 (isoform B / CSR-1b, 867 aa)
**Focus type:** function_assignment
**Hypothesis slug:** corrected-argonaute-mirna-binding-specificity
**GO term under evaluation:** GO:0035198 "miRNA binding" (MF)

---

## Summary

The molecular-function annotation "CSR-1 binds miRNAs" (GO:0035198) on H2KZD5 is **not experimentally supported** for *C. elegans* CSR-1. It is a purely **phylogenetic (IBA) carry-over** annotation, propagated by GO_Central from a broad Argonaute-family ancestral node whose experimental anchors are the canonical bilaterian miRNA Argonautes — not CSR-1. Every primary experiment on CSR-1 tests **22G-RNA (endo-siRNA) binding and siRNA-directed slicing**, never miRNA loading. CSR-1's guide class (22G-RNAs) is produced by an RNA-dependent RNA polymerase (RdRP)/DRH-3 route that is **Dicer-independent**, mechanistically distinct from the Dicer→miRNA duplex pathway serviced by the worm miRNA Argonautes ALG-1/ALG-2.

The investigation confirmed the exact provenance of the annotation. QuickGO shows GO:0035198 on H2KZD5 carries evidence ECO:0000318 (IBA), reference GO_REF:0000033, and a `withFrom` field pointing to PANTHER internal-branch node **PTN001113179** — the precise node named in the seed hypothesis — anchored by Drosophila AGO1, mammalian AGO1–4, worm *alg-1/alg-2*, and zebrafish Argonaute. None of those anchors is *csr-1*. PANTHER v19 (family PTHR22891, subfamily SF181) is the propagation source that placed the miRNA-binding term onto CSR-1 as a family-level attribute.

The most important caveat, which the seed hypothesis correctly raises, is epistemic: no published assay has **directly tested and excluded physical miRNA binding** by CSR-1. The refutation is therefore of the *annotation's evidentiary basis* — there is no worm evidence for it, and the evidence that exists is all about a different guide class — rather than a positive biochemical demonstration that CSR-1 cannot bind a miRNA duplex in vitro. For curation, the accurate statement is "no positive evidence for miRNA binding," which for a molecular-function term justifies **removal / non-core / NOT-qualification**. Separately, the accession/identity claims in the seed hypothesis are **correct**: H2KZD5 and Q27GU1 are the two genuine CSR-1 isoforms; Q17370 is *nhr-47* (carrying an obsolete "csr-1" synonym), and Q21992 is a deleted entry formerly belonging to LARP-1.

---

## Executive Judgment

**Verdict: Over-annotated / refuted as a direct CSR-1 function (with one honest residual caveat).**

Where CSR-1 has real worm-based biochemical evidence, that evidence points to **siRNA (22G-RNA) activity**, not miRNA binding. The miRNA-binding term is the only one of CSR-1's molecular-function annotations that lacks an experimental (IDA/IMP/IPI) code — a strong signal that it is inference, not observation. The demonstrated, experimentally grounded molecular function is **GO:0070551 "endoribonuclease activity, cleaving siRNA-paired mRNA"** (IDA:WormBase), with biological process **GO:0090625 "siRNA-mediated gene silencing by mRNA destabilization"** (IDA). The recommendation is to treat GO:0035198 as **non-core/removable or NOT-qualified**, promote an informative **siRNA/22G-RNA binding** term, and retain the IDA-supported slicer activity.

---

## Key Findings

### Finding 1 — GO:0035198 on H2KZD5 is an IBA (phylogenetic) annotation, not an experimental one

UniProt H2KZD5 (*csr-1*, F20D12.1a, 1030 aa) carries the standard Argonaute architecture — a PAZ domain plus the nematode Piwi (PIWI) domain — and is placed by PANTHER in family **PTHR22891** (eIF2C/Argonaute family). Its GO:0035198 "miRNA binding" term is annotated with evidence code **IBA:GO_Central** — *inferred from biological ancestor*, i.e. propagated from the phylogenetic reconstruction of the Argonaute family, which includes bilaterian miRNA-binding AGOs.

By direct contrast, the **experimentally supported** molecular function for CSR-1 is **GO:0070551 "endoribonuclease activity, cleaving siRNA-paired mRNA"** (evidence IDA:WormBase), and the experimentally supported biological process is **GO:0090625 "siRNA-mediated gene silencing by mRNA destabilization."** Where CSR-1 has real worm biochemical evidence, that evidence points to **siRNA (22G-RNA) activity**, not miRNA binding. The miRNA-binding term is the only one of these MF annotations that lacks an experimental code — a strong signal that it is inference, not observation.

### Finding 2 — Every primary CSR-1 experiment recovers 22G-RNAs / siRNA-directed slicing, never miRNA binding

The two primary references named in the seed hypothesis, plus the most relevant modern isoform paper, all interrogate the siRNA branch:

- **[PMID: 19804758](https://pubmed.ncbi.nlm.nih.gov/19804758/)** (Claycomb et al., 2009): CSR-1 immunopurification recovers small RNAs that are "**antisense to thousands of germline-expressed protein-coding genes**" — i.e. 22G-RNAs. This is a guide-class recovery experiment; it identifies what CSR-1 co-purifies with, and that is the 22G-RNA class, not miRNAs.
- **[PMID: 18007599](https://pubmed.ncbi.nlm.nih.gov/18007599/)** (Aoki et al., 2007): in a *C. elegans* cell-free assay, "**An Argonaute protein, CSR-1, is responsible for the Slicer activity induced by secondary-type siRNAs.**" This tests slicing directed by **secondary siRNA guides**, not miRNA loading.
- **[PMID: 34244496](https://pubmed.ncbi.nlm.nih.gov/34244496/)** (Nguyen & Phillips, 2021): both isoforms bind 22G-RNAs; CSR-1A associates preferentially with **spermatogenesis-specific 22G-RNAs** and CSR-1B with **oogenesis-specific 22G-RNAs**, with the CSR-1A-unique exon's arginine dimethylation controlling this **siRNA-binding specificity**.

Critically for the seed hypothesis's own framing: these are experiments about **recovered guide classes and relative slicing efficiencies**, not direct tests of miRNA binding. A strong 22G-RNA preference does not, by itself, logically exclude the physical possibility of miRNA binding. But it does mean there is **no positive worm evidence** for miRNA binding, and the entire experimental record for CSR-1 loads it with 22G-RNAs.

### Finding 3 — CSR-1 identity is confirmed; nhr-47 / LARP-1 accessions are not this Argonaute

UniProt lookups confirm the identity claims in the seed hypothesis exactly:

| Accession | Gene / entry | Identity | Family | Is this the Argonaute? |
|-----------|--------------|----------|--------|------------------------|
| **H2KZD5** | *csr-1* / F20D12.1a | CSR-1A, 1030 aa | PTHR22891 (Argonaute) | **Yes** (isoform A) |
| **Q27GU1** | *csr-1* / F20D12.1b | CSR-1B, 867 aa | PTHR22891 (Argonaute) | **Yes** (isoform B) |
| Q17370 | NHR47_CAEEL (C24G6.4) | Nuclear hormone receptor *nhr-47*, carries obsolete "csr-1" synonym | PTHR24083 | No (not an Argonaute) |
| Q21992 | Inactive / deleted entry | Formerly LARP-1 | — | No (deleted) |

This matters for curation hygiene: any GO annotation that reached the *csr-1* review via Q17370 or Q21992 would be a **misattribution/database carry-over** and should be discarded. The two genuine CSR-1 Argonaute isoforms are H2KZD5 and Q27GU1.

### Finding 4 — PANTHER (PTHR22891:SF181) directly propagates GO:0035198 to CSR-1 as a family-level term

The PANTHER v19 geneinfo record for H2KZD5 (family **PTHR22891**, subfamily **SF181**) lists in its molecular-function annotation set: GO:0003676 (nucleic acid binding), GO:0003723 (RNA binding), GO:0003727 (single-stranded RNA binding), **GO:0035198 (miRNA binding)**, and GO:0070551 (endoribonuclease activity cleaving siRNA-paired mRNA). PANTHER's protein-class assignment is PC00224 "translation initiation factor" (the historical eIF2C/Argonaute label), and Reactome carryover for the family includes "MicroRNA (miRNA) biogenesis." This is the mechanistic **source** of the IBA:GO_Central "miRNA binding" annotation seen in UniProt — the term rides on the family, not on CSR-1-specific data.

For comparison, the bona fide worm miRNA Argonautes **ALG-1 and ALG-2** are experimentally defined: **[PMID: 11461699](https://pubmed.ncbi.nlm.nih.gov/11461699/)** (Grishok et al., 2001) shows *alg-1* and *alg-2* (together with Dicer *dcr-1*) are required for the maturation and activity of the *lin-4* and *let-7* small temporal RNAs (miRNAs). CSR-1 has no comparable miRNA-function evidence.

### Finding 5 — QuickGO pins the exact IBD node; its experimental anchors are miRNA-Argonautes, not csr-1

The QuickGO annotation API for H2KZD5 / GO:0035198 "miRNA binding" returns: evidence **ECO:0000318 (IBA)**, reference **GO_REF:0000033**, assignedBy **GO_Central**, with the **withFrom** field pointing to PANTHER node **PTN001113179** and its experimentally annotated members. Those members are the canonical miRNA Argonautes:

- FB:FBgn0262739 — *Drosophila* AGO1
- MGI:2446630 / MGI:2446632 — mouse Argonautes
- UniProtKB Q9UL18 / Q9UKV8 / Q9H9G7 / Q9HCK5 — human AGO1–AGO4
- WB:WBGene00000105 / WBGene00000106 — *C. elegans* **alg-1** and **alg-2**
- ZFIN — zebrafish Argonaute

This is **exactly the IBD node named in the seed hypothesis (PTN001113179)**. The worm experimental anchors driving the "miRNA binding" term across the family are **alg-1/alg-2**, the true miRNA Argonautes — **not csr-1**. CSR-1 receives the term only by virtue of sharing the ancestral node, not because any of its own members were experimentally shown to bind miRNAs. (The leaf node PTN000527417 named in the hypothesis was not separately dereferenced but is consistent with H2KZD5's PTHR22891:SF181 placement descending from PTN001113179.)

---

## Mechanistic Model / Interpretation

The core of the evaluation is a distinction between two Argonaute sub-systems that both live in the *C. elegans* germline but use different guide classes generated by different biogenesis machinery:

```
   miRNA branch (ALG-1/ALG-2)              22G-RNA branch (CSR-1)
   ---------------------------             ------------------------------
   pri-miRNA (lin-4, let-7 ...)            target mRNA template
        | Drosha                                 | RdRP (EGO-1) — Dicer-INDEPENDENT
   pre-miRNA                                unprimed 5'-ppp 22G-RNA synthesis
        | Dicer (DCR-1)  <-- REQUIRED           | DRH-3 helicase complex
   ~22 nt miRNA duplex (5'-monoP)          22 nt 5'-G antisense 22G-RNAs (5'-triP)
        |                                       |
   loaded into ALG-1/ALG-2                 loaded into CSR-1 (GO:0070551 slicer)
        |                                       |
   translational repression /              chromosome segregation, holocentric
   mRNA destabilization                    kinetochore organization, germline
   (developmental timing:                  transcript "tuning" (NOT silencing)
    lin-4, let-7)                          [PMID 19804758, 27020753]
```

Key mechanistic separators:

1. **Biogenesis.** miRNAs are **Dicer-dependent** (DCR-1). 22G-RNAs are made by RdRP (EGO-1) with the DRH-3 helicase and are **Dicer-independent** ([PMID: 19800275](https://pubmed.ncbi.nlm.nih.gov/19800275/)). A CSR-1 that loads RdRP-made 22G-RNAs is operating in a fundamentally different guide-supply pipeline than a miRNA Argonaute.
2. **Guide 5′ chemistry and length.** 22G-RNAs are 22 nt with a 5′ triphosphorylated guanosine; miRNAs are ~22 nt with a 5′ monophosphate produced by Dicer. These are physically distinct substrates for the MID/PIWI loading pocket.
3. **Function.** CSR-1's demonstrated roles are chromosome segregation / holocentric kinetochore organization ([PMID: 19804758](https://pubmed.ncbi.nlm.nih.gov/19804758/)), germline transcript **tuning** rather than silencing ([PMID: 27020753](https://pubmed.ncbi.nlm.nih.gov/27020753/)), and meiotic homolog pairing ([PMID: 37078421](https://pubmed.ncbi.nlm.nih.gov/37078421/)). None of these is a miRNA-type post-transcriptional repression of developmental-timing genes.

The "miRNA binding" GO term therefore represents a **phylogenetic leak**: a family-ancestral capacity, real in ALG-1/ALG-2 and in bilaterian AGOs, painted onto CSR-1 because it descends from node PTN001113179. The evidence that would be needed to keep it — direct physical loading of a miRNA duplex into CSR-1 — has never been generated in worm, and everything that *has* been generated points to the 22G-RNA branch.

### GO decision table

| GO term | Aspect | Current evidence on CSR-1 | Recommended curator action |
|---------|--------|---------------------------|----------------------------|
| GO:0035198 miRNA binding | MF | IBA only (PTN001113179 carry-over); no worm experiment | **Remove / mark non-core, or NOT-qualify.** Not a demonstrated CSR-1 function |
| GO:0070551 endoribonuclease activity, cleaving siRNA-paired mRNA | MF | IDA:WormBase; slicer assay [PMID 18007599] | **Retain** — core molecular function |
| GO:0090625 siRNA-mediated gene silencing by mRNA destabilization | BP | IDA-supported; siRNA branch | **Retain** (note "tuning" nuance from [PMID 27020753]) |
| siRNA binding (GO:0035197 / 22G-RNA binding) | MF | Strongly supported [PMID 19804758, 34244496] | **Add / prefer** as the informative binding term over "miRNA binding" |

---

## Evidence Matrix

| Citation | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|-------------------------------|--------------|-------------|---------|--------------------------|
| [PMID: 19804758](https://pubmed.ncbi.nlm.nih.gov/19804758/) | Direct assay (IP-small RNA seq) + mutant phenotype | **Refutes** miRNA-binding as CSR-1's guide class | What small RNAs does CSR-1 bind? | CSR-1-associated 22G-RNAs are antisense to thousands of germline protein-coding genes; CSR-1 needed for chromosome segregation | *C. elegans* germline | High for 22G-RNA identity; does not directly test miRNA binding |
| [PMID: 18007599](https://pubmed.ncbi.nlm.nih.gov/18007599/) | Direct assay (cell-free slicer) | **Refutes / qualifies** — activity is siRNA-directed | Which Argonaute slices under secondary siRNAs? | CSR-1 is responsible for Slicer activity induced by secondary-type siRNAs | *C. elegans* cell-free extract | High for siRNA slicing; miRNA guides not tested |
| [PMID: 34244496](https://pubmed.ncbi.nlm.nih.gov/34244496/) | Direct assay (isoform IP) | **Refutes / qualifies** | Guide specificity of CSR-1 isoforms | CSR-1A ↔ spermatogenic 22G-RNAs, CSR-1B ↔ oogenic 22G-RNAs; arginine dimethylation sets siRNA specificity | *C. elegans* germline | High; entire assay is 22G-RNA binding, not miRNA |
| [PMID: 11461699](https://pubmed.ncbi.nlm.nih.gov/11461699/) | Mutant phenotype / genetic | **Competing** (identifies the real miRNA Argonautes) | Which worm AGOs handle miRNAs? | *alg-1/alg-2* + *dcr-1* required for lin-4/let-7 stRNA maturation & activity | *C. elegans* | High; establishes ALG-1/2, not CSR-1, as miRNA AGOs |
| [PMID: 19800275](https://pubmed.ncbi.nlm.nih.gov/19800275/) | Genetic / biogenesis | **Qualifies** (mechanistic separator) | How are 22G-RNAs made? | 22G-RNAs are RdRP/DRH-3-dependent, Dicer-independent | *C. elegans* germline | High; supports guide-class distinction from miRNAs |
| QuickGO annotation API (H2KZD5, GO:0035198) | Database (evidence-code audit) | **Refutes** experimental basis | Is miRNA binding experimental? | Evidence = IBA (ECO:0000318), GO_REF:0000033, withFrom PANTHER PTN001113179, anchored by alg-1/alg-2 + bilaterian AGOs | Curation record | High; confirms carry-over, not experiment |
| PANTHER v19 (PTHR22891:SF181) | Computational / evolutionary | **Qualifies** (source of term) | Where does the term come from? | miRNA-binding is a family-level MF term propagated to CSR-1 | Phylogenetic | High; explains propagation mechanism |
| UniProt (H2KZD5, Q27GU1, Q17370, Q21992) | Database (identity) | **Supports** identity claims | Are the accessions correct? | H2KZD5/Q27GU1 = CSR-1; Q17370 = nhr-47; Q21992 = deleted LARP-1 | Sequence records | High |
| [PMID: 27020753](https://pubmed.ncbi.nlm.nih.gov/27020753/) | Mutant phenotype | **Qualifies** (function is tuning) | What does CSR-1 slicing do? | CSR-1 tunes (not silences) germline transcripts to ensure embryonic divisions | *C. elegans* germline/embryo | High; distinct from miRNA repression logic |
| [PMID: 37078421](https://pubmed.ncbi.nlm.nih.gov/37078421/) | Mutant phenotype | **Qualifies** (function is chromosomal) | CSR-1 role in meiosis | CSR-1/CSR-2 + 22G-RNAs required for accurate homolog pairing & unpaired silencing | *C. elegans* meiosis | High; 22G-RNA-based, not miRNA |
| [PMID: 25510497](https://pubmed.ncbi.nlm.nih.gov/25510497/) | Comparative / evolutionary | **Qualifies** | Conservation of CSR-1 pathway | CSR-1 22G-RNA pathway and nuclear role conserved across *Caenorhabditis* | *C. briggsae/elegans* | Medium; supports 22G, not miRNA, identity |

**Computed provenance artifacts (from executed UniProt / PANTHER v19 / QuickGO queries):** `csr1_evidence_matrix.csv`, `csr1_go_decision_table.csv`.

---

## Evidence Base — narrative

The **primary references the seed hypothesis itself names** are the strongest evidence against the miRNA-binding assignment, precisely because of what they *do not* test. Claycomb et al. ([PMID: 19804758](https://pubmed.ncbi.nlm.nih.gov/19804758/)) is a guide-class recovery experiment: it defines the CSR-1-associated small-RNA population as 22G-RNAs antisense to germline genes. Aoki et al. ([PMID: 18007599](https://pubmed.ncbi.nlm.nih.gov/18007599/)) is a slicer assay driven by secondary siRNAs. Neither presents a miRNA to CSR-1. The modern isoform study ([PMID: 34244496](https://pubmed.ncbi.nlm.nih.gov/34244496/)) reinforces this by showing the *entire* binding-specificity machinery of CSR-1 (down to arginine dimethylation of the CSR-1A exon) is tuned for **22G-RNA** discrimination between spermatogenic and oogenic guides.

The **comparative reference** ([PMID: 11461699](https://pubmed.ncbi.nlm.nih.gov/11461699/)) matters because it names the actual worm miRNA Argonautes: ALG-1 and ALG-2 mature and act on lin-4/let-7. This is the experimental footprint that the family term "miRNA binding" legitimately reflects — and it belongs to a different gene. The QuickGO evidence-code audit closes the loop by showing that the *withFrom* provenance of the CSR-1 term is exactly PTN001113179, anchored by alg-1/alg-2 and bilaterian AGOs, not by any csr-1 experiment.

The **supporting/qualifying references** ([PMID: 19800275](https://pubmed.ncbi.nlm.nih.gov/19800275/), [PMID: 27020753](https://pubmed.ncbi.nlm.nih.gov/27020753/), [PMID: 37078421](https://pubmed.ncbi.nlm.nih.gov/37078421/), [PMID: 25510497](https://pubmed.ncbi.nlm.nih.gov/25510497/)) establish that CSR-1's guide class is biogenetically distinct from miRNAs (RdRP/Dicer-independent) and that its downstream functions (transcript tuning, chromosome segregation, meiotic pairing, cross-species conservation) are not miRNA-type repression. Together they place CSR-1 firmly in the 22G-RNA endo-siRNA world.

---

## Mechanistic Scope

The **immediate molecular function** at issue is *physical loading/binding of a small-RNA guide* — specifically whether CSR-1's MID/PIWI guide-binding pocket accepts a miRNA. This must be separated from three adjacent layers that the literature *does* document and that should not be conflated with miRNA binding:

- **Guide-class recovery** — IP–seq yields 22G-RNAs; a *composition* readout, not a binding-exclusion assay ([PMID: 19804758](https://pubmed.ncbi.nlm.nih.gov/19804758/)).
- **miRNA-directed slicing** — CSR-1 slices, but assays show it does so under **siRNA/22G-RNA** guides, a *catalytic* readout ([PMID: 18007599](https://pubmed.ncbi.nlm.nih.gov/18007599/), [PMID: 27020753](https://pubmed.ncbi.nlm.nih.gov/27020753/)).
- **Physiological gene regulation** — germline transcript "tuning," chromosome segregation, meiotic pairing and fertility are pathway/organismal consequences, not the binding event.

No published assay isolates the miRNA-loading step for CSR-1. The seed hypothesis is right to insist on this separation: a strong 22G-RNA preference does not *logically* exclude miRNA binding, but the burden of proof lies with a positive binding assay that has never been done. The GO term "miRNA binding" is a molecular-function (binding) claim, and it currently has zero direct-assay support in worm.

---

## Conflicts and Alternatives

1. **Paralog/family over-annotation (the primary alternative, and it wins).** The most parsimonious explanation for GO:0035198 on CSR-1 is family-level propagation from PTN001113179. The withFrom anchors are ALG-1/ALG-2 and bilaterian AGOs. This is textbook IBA carry-over, and it is the reason to down-weight the term. The nematode-specific Piwi signature and lineage-specific acquisition of RdRP-dependent 22G loading flag the divergence that makes the ancestral miRNA term inappropriate for CSR-1.
2. **The real worm miRNA Argonautes are ALG-1/ALG-2** ([PMID: 11461699](https://pubmed.ncbi.nlm.nih.gov/11461699/)): they, not CSR-1, are genetically required for lin-4/let-7 miRNA maturation and function. 22G-RNAs are RdRP/DRH-3-dependent and Dicer-independent ([PMID: 19800275](https://pubmed.ncbi.nlm.nih.gov/19800275/)), a biogenesis route incompatible with the canonical Dicer→miRNA duplex-loading pathway.
3. **Database carry-over via wrong accessions (ruled out but worth flagging).** Q17370 (*nhr-47*, carrying an obsolete "csr-1" synonym) and Q21992 (deleted, formerly LARP-1) are decoys — confirmed *not* the source of the H2KZD5 annotation, but curators should ensure no legacy annotation entered *csr-1* through them.
4. **Isoform nuance.** CSR-1A (H2KZD5) and CSR-1B (Q27GU1) differ in the N-terminal exon and in guide-specificity control ([PMID: 34244496](https://pubmed.ncbi.nlm.nih.gov/34244496/)), but both bind 22G-RNAs. There is no isoform for which miRNA binding is demonstrated; the term cannot be salvaged by assigning it to one isoform.
5. **The honest residual (pro-hypothesis caveat).** No study has run a direct in vitro CSR-1 miRNA-binding assay and reported a negative result. So the term is *unsupported*, not *disproven at the bench*. This is why the recommendation is removal/non-core/NOT-qualification rather than a claim of proven incapacity.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|-----|------------------|-----------------------------|-----------------------|
| No direct in vitro miRNA-binding assay for CSR-1 | Primary CSR-1 papers all use 22G-RNA/siRNA guides | Distinguishes "unsupported" from "disproven"; sets the correct qualifier (remove vs NOT) | EMSA / filter-binding / RNA-loading assay presenting a defined miRNA duplex to recombinant CSR-1 |
| Structural basis of guide 5′-ppp vs 5′-p selectivity in CSR-1 | Family architecture (PAZ+PIWI) known; MID-pocket specificity not experimentally mapped for CSR-1 | Would explain *why* CSR-1 favors 22G-RNAs and whether it could sterically accommodate a miRNA | Cryo-EM/crystal structure or MID-domain mutagenesis + loading assay |
| Whether any CSR-1 IP has ever recovered miRNAs above background | Published IPs report 22G-RNAs; miRNA fraction not explicitly quantified/excluded | A clean negative (no miRNA enrichment) would strengthen removal | Re-analysis of existing CSR-1 IP small-RNA-seq for miRNA reads vs input |
| Provenance completeness of the IBA term — RESOLVED | QuickGO withFrom = PTN001113179 confirmed; anchors alg-1/alg-2 + bilaterian AGOs | Confirms carry-over; ensures no hidden experimental support | Already resolved by QuickGO audit; leaf PTN000527417 not separately dereferenced |

Method transparency: findings rest on public UniProt, PANTHER v19, and QuickGO records plus the cited PubMed abstracts. Where a value came from a database record (evidence codes, withFrom anchors) versus a primary experiment (guide-class identity, slicer activity), that distinction is preserved throughout. No in-house sequence/structure computation was fabricated; PANTHER internal-node annotation was retrieved via public API.

---

## Discriminating Tests

The single most decisive experiment would be a **direct guide-loading / binding assay** with recombinant CSR-1A (and CSR-1B) presented with (a) a defined 22G-RNA (5′-ppp), (b) a canonical worm miRNA (e.g. let-7, 5′-p, Dicer-processed), and (c) a scrambled control, read out by EMSA/filter binding and by small-RNA-seq of what stays bound. Predicted outcome under the refutation: robust 22G-RNA binding, little-to-no specific miRNA binding.

Complementary discriminators:

1. **Re-mine existing CSR-1 IP small-RNA-seq** (Claycomb 2009; Nguyen & Phillips 2021 datasets) for canonical miRNA reads (5′-monophosphate, mature miRBase sequences) relative to input — a quantitative negative would convert "unsupported" toward "excluded."
2. **5′-end chemistry dependence:** test whether a 5′-triphosphate is required for stable CSR-1 loading (predicts miRNA exclusion).
3. **MID-pocket swap / point mutants** between CSR-1 and ALG-1 to test whether guide 5′-phosphate discrimination is the barrier to miRNA loading.
4. **Comparative annotation audit:** map which nodes in PTHR22891 carry IDA miRNA-binding evidence versus IBA-only leaves to quantify propagation.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Lead 1 — Down-weight GO:0035198 "miRNA binding."**
Action: change from a supported/asserted MF to **non-core**, or apply a **NOT** qualifier, or remove. Rationale: IBA-only, propagated from PTN001113179 whose anchors are alg-1/alg-2 and bilaterian AGOs; no worm experiment for CSR-1.
Candidate reference to cite for removal rationale: QuickGO annotation record for H2KZD5/GO:0035198 (evidence ECO:0000318, GO_REF:0000033, withFrom PANTHER:PTN001113179).

**Lead 2 — Prefer an informative siRNA-binding term.**
Add/prefer **GO:0035197 "siRNA binding" (22G-RNA binding)** over "miRNA binding" as the informative MF binding term; avoid falling back to generic "protein binding."
Snippet to verify — [PMID: 19804758](https://pubmed.ncbi.nlm.nih.gov/19804758/): *"the CSR-1-interacting small RNAs (22G-RNAs) are antisense to thousands of germline-expressed protein-coding genes."*
Snippet to verify — [PMID: 34244496](https://pubmed.ncbi.nlm.nih.gov/34244496/): *"CSR-1 is an essential Argonaute protein that binds to a subclass of 22G-RNAs targeting most germline-expressed genes."*

**Lead 3 — Retain the experimentally grounded slicer function.**
Keep **GO:0070551** (endoribonuclease activity, cleaving siRNA-paired mRNA; IDA).
Snippet to verify — [PMID: 18007599](https://pubmed.ncbi.nlm.nih.gov/18007599/): *"An Argonaute protein, CSR-1, is responsible for the Slicer activity induced by secondary-type siRNAs."*

**Lead 4 — Note function is transcript "tuning," not silencing.**
Snippet to verify — [PMID: 27020753](https://pubmed.ncbi.nlm.nih.gov/27020753/): *"employing catalytic slicing activity to broadly tune, instead of silence, germline gene expression."*

**Lead 5 — Identity hygiene.**
Confirm the review is anchored on H2KZD5/Q27GU1 only; explicitly exclude Q17370 (*nhr-47*) and Q21992 (deleted, LARP-1) as sources of any *csr-1* annotation.

**Suggested curator questions:**
- Is there *any* primary assay demonstrating CSR-1–miRNA binding, or is GO:0035198 solely IBA? (Our search: solely IBA.)
- Is there value in an explicit NOT-qualifier to prevent re-propagation, versus silent removal?

**Suggested experiment:** direct CSR-1 miRNA-vs-22G-RNA loading assay on recombinant CSR-1A/CSR-1B (see Discriminating Tests).

---

## Bottom Line for the Curator

The hypothesis "CSR-1 binds miRNAs" should **not** be adopted as a curated CSR-1 function. The GO:0035198 annotation is an evolutionary carry-over from the Argonaute family node PTN001113179, whose experimental support lies with ALG-1/ALG-2 and bilaterian AGOs — not CSR-1. All CSR-1 primary data describe 22G-RNA binding and siRNA-directed slicing. Recommend treating GO:0035198 as non-core/removable (optionally NOT-qualified), promoting an informative **siRNA/22G-RNA binding** term, and retaining the IDA-supported slicer activity (GO:0070551). The one honest caveat — no direct assay has physically excluded miRNA binding — argues for cautious wording ("unsupported"), not for retaining an unsupported positive annotation. Identity claims (Q17370 = *nhr-47*; Q21992 = deleted LARP-1) are confirmed and should guard against accession carry-over.

---
*Provenance: UniProt REST queries for H2KZD5, Q27GU1, Q17370, Q21992; PANTHER v19 geneinfo (PTHR22891:SF181); QuickGO annotation API for H2KZD5/GO:0035198; and PubMed abstracts for the PMIDs cited above. Computational results reported conservatively; no result fabricated.*


## Artifacts

- [OpenScientist csr1 evidence matrix](openscientist_artifacts/csr1_evidence_matrix.csv)
- [OpenScientist csr1 go decision table](openscientist_artifacts/csr1_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)