---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T00:50:53.055489'
end_time: '2026-10-20T01:04:42.486872'
duration_seconds: 829.43
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ARATH
  gene: CLV2
  gene_symbol: CLV2
  uniprot_accession: O80809
  taxon_id: NCBITaxon:3702
  taxon_label: Arabidopsis thaliana
  focus_type: function_assignment
  hypothesis_slug: clv2-direct-clv3-binding
  hypothesis_text: Arabidopsis CLAVATA2 (CLV2, a receptor-like protein lacking a kinase
    domain) directly binds the CLV3 CLE peptide ligand through its extracellular LRR
    domain, rather than acting only as a non-binding co-receptor of ligand-binding
    receptors such as CLV1/BAM1.
  term_context: '- Term: peptide hormone binding (GO:0017046)

    - Test a single question: is there direct, specific CLV3/CLE-peptide binding by
    the CLV2 ectodomain? Weigh assay design (radioligand vs photoaffinity labelling,
    expression system, ligand modification e.g. arabinosylated vs non-glycosylated
    CLV3) and any structural or sequence evidence (LRR ectodomain features compared
    with CLE-binding receptors CLV1, BAM1, PXY/TDR).'
  reference_context: '- PMID:20626648

    - PMID:25754504'
  source_file: genes/ARATH/CLV2/CLV2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Arabidopsis CLAVATA2 (CLV2, a receptor-like protein\
    \ lacking a kinase domain) directly binds\n  the CLV3 CLE peptide ligand through\
    \ its extracellular LRR domain, rather than acting only as a non-binding\n  co-receptor\
    \ of ligand-binding receptors such as CLV1/BAM1.\nfocus_type: function_assignment\n\
    term_id: GO:0017046\nterm_label: peptide hormone binding\ncontext:\n- 'Test a\
    \ single question: is there direct, specific CLV3/CLE-peptide binding by the CLV2\
    \ ectodomain?\n  Weigh assay design (radioligand vs photoaffinity labelling, expression\
    \ system, ligand modification e.g.\n  arabinosylated vs non-glycosylated CLV3)\
    \ and any structural or sequence evidence (LRR ectodomain features\n  compared\
    \ with CLE-binding receptors CLV1, BAM1, PXY/TDR).'\nreference_id:\n- PMID:20626648\n\
    - PMID:25754504"
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
citation_count: 11
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
artifacts:
- filename: artifacts_clv2_clv3_binding_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_clv2_clv3_binding_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist clv2 clv3 binding evidence matrix
- filename: artifacts_clv2_domain_comparison.csv
  path: openscientist_artifacts/artifacts_clv2_domain_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist clv2 domain comparison
- filename: artifacts_ectodomain_identity_matrix.csv
  path: openscientist_artifacts/artifacts_ectodomain_identity_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ectodomain identity matrix
- filename: artifacts_pairwise_identity_matrix.csv
  path: openscientist_artifacts/artifacts_pairwise_identity_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pairwise identity matrix
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
- **Gene directory:** CLV2
- **Gene symbol:** CLV2
- **UniProt accession:** O80809

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** clv2-direct-clv3-binding
- **Source file:** genes/ARATH/CLV2/CLV2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Arabidopsis CLAVATA2 (CLV2, a receptor-like protein lacking a kinase domain) directly binds the CLV3 CLE peptide ligand through its extracellular LRR domain, rather than acting only as a non-binding co-receptor of ligand-binding receptors such as CLV1/BAM1.

## Term and Decision Context

- Term: peptide hormone binding (GO:0017046)
- Test a single question: is there direct, specific CLV3/CLE-peptide binding by the CLV2 ectodomain? Weigh assay design (radioligand vs photoaffinity labelling, expression system, ligand modification e.g. arabinosylated vs non-glycosylated CLV3) and any structural or sequence evidence (LRR ectodomain features compared with CLE-binding receptors CLV1, BAM1, PXY/TDR).

## Reference Context

- PMID:20626648
- PMID:25754504

## Source Context YAML

```yaml
hypothesis: Arabidopsis CLAVATA2 (CLV2, a receptor-like protein lacking a kinase domain) directly binds
  the CLV3 CLE peptide ligand through its extracellular LRR domain, rather than acting only as a non-binding
  co-receptor of ligand-binding receptors such as CLV1/BAM1.
focus_type: function_assignment
term_id: GO:0017046
term_label: peptide hormone binding
context:
- 'Test a single question: is there direct, specific CLV3/CLE-peptide binding by the CLV2 ectodomain?
  Weigh assay design (radioligand vs photoaffinity labelling, expression system, ligand modification e.g.
  arabinosylated vs non-glycosylated CLV3) and any structural or sequence evidence (LRR ectodomain features
  compared with CLE-binding receptors CLV1, BAM1, PXY/TDR).'
reference_id:
- PMID:20626648
- PMID:25754504
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

# CLV2 Direct CLV3/CLE-Peptide Binding — Hypothesis Deep Research Report

**Gene:** CLAVATA2 (CLV2) — *Arabidopsis thaliana* (ARATH, NCBITaxon:3702)
**UniProt:** O80809
**Focus type:** function_assignment
**Hypothesis slug:** clv2-direct-clv3-binding
**Term under evaluation:** GO:0017046 — *peptide hormone binding* (Molecular Function)

---

## Executive Judgment

**Verdict: REFUTED (direct CLV3/CLE-peptide binding by the CLV2 ectodomain is not supported).**

The seed hypothesis proposes that CLV2 — a kinase-less leucine-rich-repeat (LRR) receptor-like protein (RLP) — directly binds the CLV3 CLE peptide through its extracellular LRR domain, rather than acting only as a non-binding co-receptor. The strongest, most physiologically relevant evidence refutes this. When the perception question was tested with the **native, triarabinosylated CLV3 glycopeptide** using **photoaffinity labeling**, CLV2 (and RPK2) showed **no direct binding**, whereas the LRR-receptor kinases **CLV1 and BAM1 did bind directly** ([PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/)). The lone primary report supporting CLV2 binding ([PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/)) used a bulk membrane-binding assay with a CLV3 peptide that was almost certainly **not arabinosylated**, and arabinosylation is now established as critical for high-affinity, specific CLE receptor binding ([PMID:20580598](https://pubmed.ncbi.nlm.nih.gov/20580598/)). The discrepancy is therefore best explained by ligand modification state, and the weight of evidence falls against a direct-binding function for CLV2.

Independent lines of evidence converge on the same conclusion. CLV2 is an obligate partner of the **CRN pseudokinase** and directly heterodimerizes with CRN independent of CLV3 ([PMID:27229734](https://pubmed.ncbi.nlm.nih.gov/27229734/), [PMID:19843317](https://pubmed.ncbi.nlm.nih.gov/19843317/)), consistent with a scaffolding/co-receptor role rather than a direct ligand-binding receptor. Comparative sequence analysis (performed in this investigation, both full-length and ectodomain-only) places CLV2 as the clear **outlier** relative to the coherent clade of validated direct CLE binders (CLV1, BAM1, PXY/TDR), which are mutually far more similar to each other than any is to CLV2.

**Curation implication:** GO:0017046 (*peptide hormone binding*) should **not** be asserted as a direct molecular function of CLV2 based on current evidence. A co-receptor/scaffold framing is better supported — e.g., *protein heterodimerization activity* (GO:0046982, with CRN) and *receptor complex* (GO:0043235, CC). The most important caveat is that one primary paper does report a CLV2-associated CLE-binding activity; a curator should document this conflict and the arabinosylation-based reconciliation rather than silently discarding it.

---

## Key Findings

### Finding 1 — Rigorous photoaffinity assay with native arabinosylated CLV3 shows CLV2 does NOT directly bind CLV3

The decisive experiment comes from Shinohara & Matsubayashi (2015), who re-examined the CLV3-receptor interaction specifically from a **direct ligand-binding** standpoint ([PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/)). Critically, they used a **photoactivatable, physiologically triarabinosylated** CLV3 glycopeptide — the native post-translationally modified form of the ligand — in photoaffinity labeling assays. Under these conditions, **CLV2 and RPK2 exhibited no direct binding**, whereas the LRR receptor kinases **CLV1 and BAM1 bound the peptide directly**. The verified quote is explicit:

> "We showed that CLV2 and RPK2 exhibited no direct binding to the CLV3 peptide. Further analysis showed that the receptor kinase BAM1 directly binds the CLV3 peptide." ([PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/))

This biochemical result is reinforced by genetics in the same body of work: a *clv1 bam1* double mutant was insensitive to exogenous arabinosylated CLV3 and accumulated stem cells with an enlarged WUS domain, genetically assigning **direct perception** of CLV3 to CLV1 and BAM1. The assay design is the gold standard for this question — covalent photoaffinity capture with the native glycopeptide in an appropriate expression system — and it directly tests the molecular event named in GO:0017046. Because it uses the physiological ligand and a direct (covalent) readout, this is the single most informative piece of evidence, and it is negative for CLV2.

### Finding 2 — The conflicting earlier report used a non-physiological ligand; the discrepancy is explained by arabinosylation

Guo et al. (2010) reported that CLV2 alone generates a membrane-localized CLE-binding activity independent of CLV1, and that CLV2, CLV1, BAM1, and BAM2 bind CLV3 with similar kinetics ([PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/)). The verified quote is:

> "We also find that CLV2 alone generates a membrane-localized CLE binding activity independent of CLV1." ([PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/))

This is the **only** primary claim of a direct CLV2-associated CLE-binding activity, and it must be weighed carefully. Three factors reduce its weight relative to the photoaffinity data. First, it used a **bulk membrane-binding assay** on transiently expressed receptors rather than a covalent, receptor-resolved capture — such assays cannot distinguish binding by CLV2 itself from binding by an endogenous or co-expressed partner in the membrane preparation. Second, the CLV3 peptide used was almost certainly **non-arabinosylated** synthetic peptide. Third, and decisively, arabinosylation is now established as critical for genuine high-affinity, specific CLE binding:

> "Arabinosylation of CLV3 is important for its biological activity and for high-affinity binding to its receptor, CLV1." ([PMID:20580598](https://pubmed.ncbi.nlm.nih.gov/20580598/))

For context, direct CLV1 binding of arabinosylated CLV3 has a measured dissociation constant of **Kd = 17.5 nM** ([PMID:18202283](https://pubmed.ncbi.nlm.nih.gov/18202283/)). The simplest reconciliation of the two primary reports is that the 2010 membrane assay detected a lower-specificity binding signal with a non-native ligand, while the 2015 photoaffinity assay, using the native glycopeptide and a direct covalent readout, found no CLV2 binding. The discrepancy is thus attributable to **ligand modification state and assay resolution**, not to a genuine CLV2 receptor function.

### Finding 3 — CLV2 is the sequence outlier among CLAVATA-type receptors; validated direct binders form a coherent clade that excludes CLV2

To test whether CLV2 even resembles the proteins that are known to bind CLE peptides, this investigation computed Needleman–Wunsch global pairwise identities from UniProt full-length sequences across CLV2 and the three validated direct binders (CLV1, BAM1, and TDR/PXY). CLV2 shares only ~29.7–31.7% identity with each direct binder (CLV1 31.7%, BAM1 31.0%, TDR/PXY 29.7%), whereas the direct binders are mutually far more similar (CLV1–BAM1 55.5%, CLV1–TDR 42.8%, BAM1–TDR 44.6%). In other words, the validated binders form a tight clade, and CLV2 sits well outside it.

This is consistent with CLV2's architecture: it is a **720-aa LRR receptor-like protein (RLP)** with ~21 LRRs and **no kinase domain**, obligately partnered with the catalytically questionable CRN pseudokinase:

> "CLV2, a leucine-rich repeat (LRR) receptor-like protein, and CRN, a protein kinase, have to interact to form a receptor-kinase complex. The kinase domain of CRN has been reported to be catalytically inactive" ([PMID:27229734](https://pubmed.ncbi.nlm.nih.gov/27229734/))

Moreover, CLV2's best-supported molecular interaction is not with a peptide ligand but with CRN:

> "CLV2 can directly interact with CRN in the absence of CLV3" ([PMID:19843317](https://pubmed.ncbi.nlm.nih.gov/19843317/))

This frames CLV2 as a **co-receptor scaffold** rather than a direct-binding receptor.

### Finding 4 — Ectodomain-only alignment confirms the outlier status (kinase-inflation caveat resolved)

A fair objection to Finding 3 is that full-length identity could be depressed simply because CLV2 lacks the kinase domain present in CLV1/BAM1/TDR. To control for this, each protein was trimmed to its **ectodomain only** (from the UniProt signal-peptide end to the residue before the transmembrane start; TM_start CLV2=687, CLV1=639, BAM1=641, TDR=653) and identities were recomputed. CLV2's ectodomain mean identity to the three direct binders was **35.3%** (CLV1 34.4%, BAM1 36.3%, TDR/PXY 35.3%), versus a binder-clade ectodomain mean of **45.3%** (CLV1–BAM1 51.0%, CLV1–TDR 41.4%, BAM1–TDR 43.6%). Even restricting the comparison to the ligand-binding LRR ectodomain — exactly the region the hypothesis invokes — CLV2 remains the outlier. The sequence features of CLV2's LRR ectodomain are therefore not those of the CLE-binding receptor clade, consistent with the negative direct-binding result.

---

## Mechanistic Model / Interpretation

The convergent evidence supports a model in which **direct CLV3 perception is carried out by LRR receptor kinases (CLV1, BAM1, and RPK2-associated pathways), while CLV2 acts as a non-binding co-receptor/scaffold in an obligate complex with the CRN pseudokinase.**

```
        Native arabinosylated CLV3 glycopeptide (Ara3)
                           │
          ┌────────────────┼─────────────────┐
          │ DIRECT BINDING │                  │  NO DIRECT BINDING
          ▼                ▼                  ▼
       CLV1            BAM1 / BAM2         CLV2 ─(heterodimer, CLV3-independent)─ CRN
   (LRR-RK, Kd≈17.5nM) (LRR-RK)           (LRR-RLP,            (pseudokinase,
   PMID:18202283       PMID:25754504       no kinase)          inactive kinase)
                                           = "no direct binding"  PMID:27229734
                                           PMID:25754504          PMID:19843317
                           │
                           ▼
                 WUS repression / SAM stem-cell homeostasis (downstream BP)
```

Key distinctions for curation:

| Layer | What it is | CLV2's role | GO category |
|---|---|---|---|
| **Direct molecular activity (tested)** | Binding the CLV3 glycopeptide | **Not supported** (no direct binding) | MF — GO:0017046 *rejected* |
| **Supported molecular activity** | Heterodimerization with CRN | Supported (CLV3-independent) | MF — GO:0046982 |
| **Complex / location** | CLV2–CRN receptor complex at plasma membrane | Supported | CC — GO:0043235 |
| **Downstream process** | SAM/RAM stem-cell maintenance, nematode CLE perception | Required genetically (loss-of-function) | BP — context-specific |

The genetic requirement of CLV2 in CLE signaling (SAM homeostasis; cyst-nematode CLE perception, e.g. [PMID:21265896](https://pubmed.ncbi.nlm.nih.gov/21265896/), [PMID:22835273](https://pubmed.ncbi.nlm.nih.gov/22835273/)) is real but is a **downstream, loss-of-function phenotype** — it demonstrates that CLV2 is *needed for* signaling, not that CLV2 *directly binds* the ligand. Conflating pathway requirement with direct binding is the central inferential error the seed hypothesis risks.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/) | Direct assay (photoaffinity labeling) + mutant phenotype | **Refutes** | Does CLV2 directly bind native CLV3? | CLV2 (and RPK2) show **no direct binding**; CLV1 and BAM1 bind directly; *clv1 bam1* insensitive to Ara-CLV3 | Arabidopsis; native triarabinosylated CLV3; receptor-resolved covalent capture | High confidence; the most physiologically relevant assay for this exact question |
| [PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/) | Direct assay (membrane binding) | **Competing/supports** | Does CLV2 generate CLE-binding activity? | CLV2 alone generates membrane CLE-binding activity; CLV2/CLV1/BAM1/BAM2 bind with similar kinetics | Transient expression; bulk membrane assay; likely **non-arabinosylated** CLV3 | Moderate; non-native ligand and non-receptor-resolved assay weaken it |
| [PMID:20580598](https://pubmed.ncbi.nlm.nih.gov/20580598/) | Review/database (synthesized) | **Qualifies** | Does arabinosylation matter for binding? | Arabinosylation needed for CLV3 activity and high-affinity CLV1 binding | Arabidopsis CLV3 structure | High for the reconciling principle; explains the 2010 vs 2015 discrepancy |
| [PMID:18202283](https://pubmed.ncbi.nlm.nih.gov/18202283/) | Direct assay (ligand binding + photoaffinity) | **Qualifies** | Benchmark for genuine direct CLE binding | CLV3 directly binds CLV1 ectodomain, Kd = 17.5 nM | Arabidopsis; CLV1 ectodomain | High; defines the standard CLV2 fails to meet |
| [PMID:27229734](https://pubmed.ncbi.nlm.nih.gov/27229734/) | Structural/functional + review | **Supports (alt.)** | Is CLV2 a kinase-less RLP needing a partner? | CLV2 is an LRR-RLP; must interact with CRN (inactive kinase) to form a complex | Arabidopsis SAM/RAM | High; establishes co-receptor architecture |
| [PMID:19843317](https://pubmed.ncbi.nlm.nih.gov/19843317/) | Interaction | **Supports (alt.)** | What does CLV2 directly bind? | CLV2 directly interacts with CRN in absence of CLV3 | Arabidopsis | High; the best-supported direct CLV2 interaction |
| [PMID:27498761](https://pubmed.ncbi.nlm.nih.gov/27498761/) | Structural | **Qualifies** | What does a bona fide CLE-binding ectodomain look like? | TDR ectodomain (22 LRRs) binds TDIF on inner concave surface; conserved CLE recognition | Crystal structure, plant LRR-RK | High; structural template; CLV2 ectodomain diverges from this clade |
| This investigation (computed) | Computational (sequence) | **Supports (alt.)** | Does CLV2 resemble direct binders? | CLV2 is the outlier (full-length ~30–32%; ectodomain-only ~35% vs binder clade ~45%) | NW global identity, UniProt sequences | Moderate; sequence divergence is suggestive, not proof of non-binding |

---

## Evidence Base (narrative)

- ***Reevaluation of the CLV3-receptor interaction in the shoot apical meristem*** [PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/) — The pivotal paper. Its use of the native arabinosylated glycopeptide and covalent photoaffinity capture makes it the definitive test. CLV2 negative; CLV1/BAM1 positive. Directly refutes the hypothesis.
- ***CLAVATA2 forms a distinct CLE-binding receptor complex...*** [PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/) — The sole primary support. Its binding signal is reinterpretable as an assay/ligand artifact given the arabinosylation requirement; must be cited by curators as the conflicting datapoint.
- ***Arabinosylated glycopeptide hormones: new insights into CLAVATA3 structure*** [PMID:20580598](https://pubmed.ncbi.nlm.nih.gov/20580598/) — Provides the mechanistic key that reconciles the two primary reports: non-arabinosylated CLV3 does not reflect physiological high-affinity binding.
- ***Arabidopsis CLV3 peptide directly binds CLV1 ectodomain*** [PMID:18202283](https://pubmed.ncbi.nlm.nih.gov/18202283/) — Establishes what a genuine, quantified direct CLE-receptor interaction looks like (Kd 17.5 nM), a benchmark CLV2 never meets.
- ***Shared and distinct functions of the pseudokinase CORYNE (CRN)...*** [PMID:27229734](https://pubmed.ncbi.nlm.nih.gov/27229734/) and ***Analysis of interactions among the CLAVATA3 receptors... CLAVATA2 and CORYNE*** [PMID:19843317](https://pubmed.ncbi.nlm.nih.gov/19843317/) — Together define CLV2's actual, well-supported molecular role: a kinase-less scaffold that heterodimerizes with CRN independent of ligand.
- ***Crystal structure of the plant receptor-like kinase TDR in complex with the TDIF peptide*** [PMID:27498761](https://pubmed.ncbi.nlm.nih.gov/27498761/) — A structural reference for the CLE-binding LRR ectodomain architecture; CLV2's divergence from this clade is consistent with non-binding.
- Nematode CLE papers ([PMID:21265896](https://pubmed.ncbi.nlm.nih.gov/21265896/), [PMID:22835273](https://pubmed.ncbi.nlm.nih.gov/22835273/), [PMID:25581705](https://pubmed.ncbi.nlm.nih.gov/25581705/)) — Demonstrate CLV2/CRN is *genetically required* for CLE perception in multiple contexts, but these are loss-of-function/pathway requirements, not direct-binding evidence.

---

## Conflicts and Alternatives

1. **The 2010 vs 2015 discrepancy (central conflict).** [PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/) reports CLV2-associated CLE binding; [PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/) reports none. Best explanation: ligand arabinosylation state and assay resolution (bulk membrane binding vs receptor-resolved covalent photoaffinity). This is a genuine conflict a curator must acknowledge, not erase.

2. **Co-receptor vs receptor framing.** CLV2's genetic requirement in CLE signaling could be misread as direct perception. The alternative — and better-supported — interpretation is a non-binding scaffold acting through CRN and in concert with ligand-binding kinases.

3. **Docking/prediction literature.** Computational docking papers (e.g., [PMID:20697738](https://pubmed.ncbi.nlm.nih.gov/20697738/)) propose CLE peptides fitting CLV2–CRN complexes, but these are *in silico* models, not binding measurements, and should not be treated as direct evidence of CLV2 binding.

4. **Paralog/ortholog carry-over.** Soybean "CLE receptor" orthologue studies ([PMID:25581705](https://pubmed.ncbi.nlm.nih.gov/25581705/)) test crop receptors; any binding attributed there should not be transferred to Arabidopsis CLV2 by orthology.

---

## Limitations and Knowledge Gaps

- **Single decisive negative assay.** The strongest refuting evidence rests substantially on one laboratory's photoaffinity study ([PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/)). Independent replication with native arabinosylated CLV3 (e.g., SPR/MST on purified CLV2 ectodomain) would strengthen the conclusion. *Gap matters because* curation is rejecting a GO term largely on one method.
- **No published high-resolution CLV2 ectodomain structure bound (or not bound) to CLV3.** The TDR–TDIF structure ([PMID:27498761](https://pubmed.ncbi.nlm.nih.gov/27498761/)) is a surrogate. *What would resolve it:* a CLV2 ectodomain crystal/cryo-EM structure with/without ligand, or AlphaFold-Multimer modeling of CLV2 ectodomain + CLV3 (noting AF cannot model the arabinose chain).
- **Sequence divergence ≠ proof of non-binding.** Findings 3/4 are suggestive, not dispositive; low identity does not strictly preclude binding. *Checked:* full-length and ectodomain-only NW identity. *Would resolve:* direct biochemistry on purified CLV2 ectodomain.
- **Was the 2010 ligand truly non-arabinosylated?** This is inferred, not confirmed from the abstract. *Would resolve:* re-running the 2010 membrane assay side-by-side with arabinosylated vs non-arabinosylated CLV3.

---

## Discriminating Tests

1. **Quantitative direct binding on purified CLV2 ectodomain** (SPR, MST, or ITC) with **native triarabinosylated CLV3** vs non-arabinosylated CLV3, benchmarked against CLV1 (expected Kd ≈ 17.5 nM). A flat/no-binding curve for CLV2 with native ligand would confirm the refutation.
2. **Side-by-side re-test of the 2010 assay** with controlled ligand glycosylation, to formally attribute the 2010 signal to ligand modification state.
3. **AlphaFold-Multimer / structural modeling** of CLV2 ectodomain + CLV3 core peptide vs CLV1/BAM1/TDR positive controls, inspecting the inner-concave LRR surface residues shown to contact CLE in TDR ([PMID:27498761](https://pubmed.ncbi.nlm.nih.gov/27498761/)).
4. **Reconstituted ternary assay:** test whether CLV2–CRN confers or enhances CLV3 binding only in the presence of a kinase partner (CLV1/BAM1), distinguishing scaffold from receptor.

---

## GO Curation Implications

**Lead (requires curator verification):** Do **not** assert GO:0017046 (*peptide hormone binding*) as a direct molecular function of CLV2. The direct-binding claim is refuted by the physiologically appropriate assay and supported only by a single non-native-ligand membrane study.

| GO term | Category | Recommended action | Rationale |
|---|---|---|---|
| GO:0017046 *peptide hormone binding* | MF | **Do not assert / remove or restrict to NOT** | Native-ligand photoaffinity shows no direct CLV2 binding ([PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/)) |
| GO:0046982 *protein heterodimerization activity* | MF | **Candidate add** | CLV2 directly heterodimerizes with CRN, CLV3-independent ([PMID:19843317](https://pubmed.ncbi.nlm.nih.gov/19843317/)) |
| GO:0043235 *receptor complex* | CC | **Candidate add/retain** | CLV2–CRN plasma-membrane receptor complex ([PMID:27229734](https://pubmed.ncbi.nlm.nih.gov/27229734/)) |
| BP terms (SAM/RAM stem-cell maintenance; CLE perception) | BP | **Retain as genetic/loss-of-function** | Genetically required but downstream, not direct binding |

A curator could consider a `NOT GO:0017046` annotation with evidence from [PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/), while explicitly logging the conflicting [PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/) and the arabinosylation reconciliation ([PMID:20580598](https://pubmed.ncbi.nlm.nih.gov/20580598/)). Per GO best practice, "protein binding" is avoided here in favor of the more informative *protein heterodimerization activity* and *receptor complex* framings.

---

## Mechanistic Scope

The immediate molecular function under test is **binding of the CLV3 glycopeptide hormone by the CLV2 ectodomain** (GO:0017046). The evidence indicates this direct activity does not occur. What CLV2 *does* do at the molecular level is **heterodimerize with CRN** (GO:0046982) to form a plasma-membrane **receptor complex** (GO:0043235). Everything else attributed to CLV2 — SAM/RAM stem-cell maintenance, WUS repression, cyst-nematode CLE perception — is a **downstream biological process** inferred largely from loss-of-function genetics, not a direct biochemical property of the CLV2 protein. The curation decision should keep these layers separate: reject the direct-binding MF, retain the complex-formation MF/CC, and tag the developmental BP annotations as genetic/loss-of-function in origin.

---

## Curation Leads (require curator verification)

- **Candidate reference (refuting):** [PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/) — snippet to verify: *"We showed that CLV2 and RPK2 exhibited no direct binding to the CLV3 peptide. Further analysis showed that the receptor kinase BAM1 directly binds the CLV3 peptide."*
- **Candidate reference (conflicting, must be addressed):** [PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/) — snippet: *"We also find that CLV2 alone generates a membrane-localized CLE binding activity independent of CLV1."*
- **Candidate reference (reconciling principle):** [PMID:20580598](https://pubmed.ncbi.nlm.nih.gov/20580598/) — snippet: *"Arabinosylation of CLV3 is important for its biological activity and for high-affinity binding to its receptor, CLV1."*
- **Candidate reference (alternative supported MF):** [PMID:19843317](https://pubmed.ncbi.nlm.nih.gov/19843317/) — snippet: *"CLV2 can directly interact with CRN in the absence of CLV3."*
- **Candidate reference (architecture):** [PMID:27229734](https://pubmed.ncbi.nlm.nih.gov/27229734/) — snippet: *"CLV2, a leucine-rich repeat (LRR) receptor-like protein, and CRN, a protein kinase, have to interact to form a receptor-kinase complex. The kinase domain of CRN has been reported to be catalytically inactive."*
- **Suggested action change:** Replace/avoid any *peptide hormone binding* assertion with co-receptor framing (GO:0046982; GO:0043235); keep SAM/RAM BP annotations tagged as loss-of-function/genetic.
- **Suggested curator question:** Is the historical CLV2 binding annotation traceable to [PMID:20626648](https://pubmed.ncbi.nlm.nih.gov/20626648/) with a non-arabinosylated ligand? If so, flag as superseded by [PMID:25754504](https://pubmed.ncbi.nlm.nih.gov/25754504/).
- **Suggested experiment:** Quantitative direct binding (SPR/MST) on purified CLV2 ectodomain with native arabinosylated CLV3, CLV1 as positive control.

---

## Summary Statement

The hypothesis that the CLV2 ectodomain directly binds CLV3/CLE peptide is **refuted** by the best available evidence. CLV2 is a kinase-less LRR receptor-like protein that functions as a non-binding co-receptor/scaffold via obligate heterodimerization with the CRN pseudokinase; direct CLV3 perception is carried out by the LRR receptor kinases CLV1 and BAM1 using the native arabinosylated ligand. GO:0017046 should not be asserted for CLV2.


## Artifacts

- [OpenScientist clv2 clv3 binding evidence matrix](openscientist_artifacts/artifacts_clv2_clv3_binding_evidence_matrix.csv)
- [OpenScientist clv2 domain comparison](openscientist_artifacts/artifacts_clv2_domain_comparison.csv)
- [OpenScientist ectodomain identity matrix](openscientist_artifacts/artifacts_ectodomain_identity_matrix.csv)
- [OpenScientist pairwise identity matrix](openscientist_artifacts/artifacts_pairwise_identity_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)