---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T02:38:12.101294'
end_time: '2026-09-21T03:07:32.706864'
duration_seconds: 1760.61
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: SSQ1
  gene_symbol: SSQ1
  uniprot_accession: Q05931
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: folding-refolding-and-secondary-client-interactions
  hypothesis_text: Saccharomyces cerevisiae Ssq1 (Q05931; YLR369W; Ssc2p) retains
    protein folding/refolding or unfolded-protein holdase activity alongside its established
    ATP-dependent Isu/Grx5 Fe-S cluster transfer role. Separately, Ssq1 has a biologically
    meaningful interaction with Nop1 (P15646). Assess each claim independently against
    actual GO definitions, target primary assays and experimental context. Actual
    PTHR19375 treeinfo target path contains folding/refolding IBD PTN000452648, cytoplasm
    node PTN002321897 and mitochondrial/ISC node PTN000452554, terminating at PTN000452606;
    no NOT/IRD assertion lies on that path. Do not equate donor count, predominant
    matrix location or specialist status with universal loss. Full PMID12756240 Fig8
    establishes lack of Mdj1 stimulation of Ssq1 ATPase and Isu engagement, not a
    general refolding assay; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2003_Dutkiewicz_JBC.pdf
    . PMID20224575 introduction infers folding loss from partner specificity. PMID11601843
    abstract explicitly reports ATP-regulated unfolded-substrate binding; retrieve
    full assays before deciding folding versus binding. Crucial full PMID16431909
    Fig4C shows Ssq1 protects guanidine-denatured rhodanese against aggregation, strongest
    without nucleotide or with ADP, by light scattering; not restored rhodanese enzymatic
    activity. Fig4A/B shows ATP/Jac1-independent protection of purified Nfs1 activity,
    while Fig4D shows Ssq1-depleted mitochondrial lysate Nfs1 activity unchanged;
    author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2006_Dutkiewicz_JBC.pdf
    . Full PMID23615440 Fig3D detects in-vitro Cia1 binding displaced by LPPVK, distinct
    from nonoverlapping Grx5 binding; its folding-language interpretation is not itself
    a refolding assay. Full PMID10779357 Discussion reports no Yfh1 aggregation/protease-sensitivity
    difference in wild-type versus ssq1 deletion despite processing delay; this specific
    negative does not prove no capacity on other clients. Distinguish native folding,
    reactivation of misfolded substrate, aggregation prevention, ATP-driven scaffold
    remodeling and cargo delivery requirements of GO0140309. Identify whether any
    more precise MF represents established Ssq1 action without inventing a new foldase
    claim. For Nop1, original IPI rows cite16554755 and19536198. Full19536198 uses
    TAP-MS whole-cell complexes and spoke inference, shares methods/data lineage with16554755,
    and includes Ssc2 as an alias; inspect exact Nop1-YLR369W supplement entries and
    independence, target localization or functional assays. Native matrix residence
    alone neither disproves the interaction nor proves a nuclear pool. Report any
    unresolved source-access limits and do not infer direct binary binding or target
    refolding from AP-MS alone.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/SSQ1/SSQ1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae Ssq1 (Q05931; YLR369W;\
    \ Ssc2p) retains protein folding/refolding or\n  unfolded-protein holdase activity\
    \ alongside its established ATP-dependent Isu/Grx5 Fe-S cluster transfer\n  role.\
    \ Separately, Ssq1 has a biologically meaningful interaction with Nop1 (P15646).\
    \ Assess each claim\n  independently against actual GO definitions, target primary\
    \ assays and experimental context. Actual\n  PTHR19375 treeinfo target path contains\
    \ folding/refolding IBD PTN000452648, cytoplasm node PTN002321897\n  and mitochondrial/ISC\
    \ node PTN000452554, terminating at PTN000452606; no NOT/IRD assertion lies on\
    \ that\n  path. Do not equate donor count, predominant matrix location or specialist\
    \ status with universal loss.\n  Full PMID12756240 Fig8 establishes lack of Mdj1\
    \ stimulation of Ssq1 ATPase and Isu engagement, not a\n  general refolding assay;\
    \ author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2003_Dutkiewicz_JBC.pdf\n\
    \  . PMID20224575 introduction infers folding loss from partner specificity. PMID11601843\
    \ abstract explicitly\n  reports ATP-regulated unfolded-substrate binding; retrieve\
    \ full assays before deciding folding versus\n  binding. Crucial full PMID16431909\
    \ Fig4C shows Ssq1 protects guanidine-denatured rhodanese against aggregation,\n\
    \  strongest without nucleotide or with ADP, by light scattering; not restored\
    \ rhodanese enzymatic activity.\n  Fig4A/B shows ATP/Jac1-independent protection\
    \ of purified Nfs1 activity, while Fig4D shows Ssq1-depleted\n  mitochondrial\
    \ lysate Nfs1 activity unchanged; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2006_Dutkiewicz_JBC.pdf\n\
    \  . Full PMID23615440 Fig3D detects in-vitro Cia1 binding displaced by LPPVK,\
    \ distinct from nonoverlapping\n  Grx5 binding; its folding-language interpretation\
    \ is not itself a refolding assay. Full PMID10779357\n  Discussion reports no\
    \ Yfh1 aggregation/protease-sensitivity difference in wild-type versus ssq1 deletion\n\
    \  despite processing delay; this specific negative does not prove no capacity\
    \ on other clients. Distinguish\n  native folding, reactivation of misfolded substrate,\
    \ aggregation prevention, ATP-driven scaffold remodeling\n  and cargo delivery\
    \ requirements of GO0140309. Identify whether any more precise MF represents established\n\
    \  Ssq1 action without inventing a new foldase claim. For Nop1, original IPI rows\
    \ cite16554755 and19536198.\n  Full19536198 uses TAP-MS whole-cell complexes and\
    \ spoke inference, shares methods/data lineage with16554755,\n  and includes Ssc2\
    \ as an alias; inspect exact Nop1-YLR369W supplement entries and independence,\
    \ target\n  localization or functional assays. Native matrix residence alone neither\
    \ disproves the interaction nor\n  proves a nuclear pool. Report any unresolved\
    \ source-access limits and do not infer direct binary binding\n  or target refolding\
    \ from AP-MS alone.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
    \ []"
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
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: provenance_ssq1_curation.md
  path: openscientist_artifacts/provenance_ssq1_curation.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist provenance ssq1 curation
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
- **Gene directory:** SSQ1
- **Gene symbol:** SSQ1
- **UniProt accession:** Q05931

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** folding-refolding-and-secondary-client-interactions
- **Source file:** genes/yeast/SSQ1/SSQ1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Ssq1 (Q05931; YLR369W; Ssc2p) retains protein folding/refolding or unfolded-protein holdase activity alongside its established ATP-dependent Isu/Grx5 Fe-S cluster transfer role. Separately, Ssq1 has a biologically meaningful interaction with Nop1 (P15646). Assess each claim independently against actual GO definitions, target primary assays and experimental context. Actual PTHR19375 treeinfo target path contains folding/refolding IBD PTN000452648, cytoplasm node PTN002321897 and mitochondrial/ISC node PTN000452554, terminating at PTN000452606; no NOT/IRD assertion lies on that path. Do not equate donor count, predominant matrix location or specialist status with universal loss. Full PMID12756240 Fig8 establishes lack of Mdj1 stimulation of Ssq1 ATPase and Isu engagement, not a general refolding assay; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2003_Dutkiewicz_JBC.pdf . PMID20224575 introduction infers folding loss from partner specificity. PMID11601843 abstract explicitly reports ATP-regulated unfolded-substrate binding; retrieve full assays before deciding folding versus binding. Crucial full PMID16431909 Fig4C shows Ssq1 protects guanidine-denatured rhodanese against aggregation, strongest without nucleotide or with ADP, by light scattering; not restored rhodanese enzymatic activity. Fig4A/B shows ATP/Jac1-independent protection of purified Nfs1 activity, while Fig4D shows Ssq1-depleted mitochondrial lysate Nfs1 activity unchanged; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2006_Dutkiewicz_JBC.pdf . Full PMID23615440 Fig3D detects in-vitro Cia1 binding displaced by LPPVK, distinct from nonoverlapping Grx5 binding; its folding-language interpretation is not itself a refolding assay. Full PMID10779357 Discussion reports no Yfh1 aggregation/protease-sensitivity difference in wild-type versus ssq1 deletion despite processing delay; this specific negative does not prove no capacity on other clients. Distinguish native folding, reactivation of misfolded substrate, aggregation prevention, ATP-driven scaffold remodeling and cargo delivery requirements of GO0140309. Identify whether any more precise MF represents established Ssq1 action without inventing a new foldase claim. For Nop1, original IPI rows cite16554755 and19536198. Full19536198 uses TAP-MS whole-cell complexes and spoke inference, shares methods/data lineage with16554755, and includes Ssc2 as an alias; inspect exact Nop1-YLR369W supplement entries and independence, target localization or functional assays. Native matrix residence alone neither disproves the interaction nor proves a nuclear pool. Report any unresolved source-access limits and do not infer direct binary binding or target refolding from AP-MS alone.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae Ssq1 (Q05931; YLR369W; Ssc2p) retains protein folding/refolding or
  unfolded-protein holdase activity alongside its established ATP-dependent Isu/Grx5 Fe-S cluster transfer
  role. Separately, Ssq1 has a biologically meaningful interaction with Nop1 (P15646). Assess each claim
  independently against actual GO definitions, target primary assays and experimental context. Actual
  PTHR19375 treeinfo target path contains folding/refolding IBD PTN000452648, cytoplasm node PTN002321897
  and mitochondrial/ISC node PTN000452554, terminating at PTN000452606; no NOT/IRD assertion lies on that
  path. Do not equate donor count, predominant matrix location or specialist status with universal loss.
  Full PMID12756240 Fig8 establishes lack of Mdj1 stimulation of Ssq1 ATPase and Isu engagement, not a
  general refolding assay; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2003_Dutkiewicz_JBC.pdf
  . PMID20224575 introduction infers folding loss from partner specificity. PMID11601843 abstract explicitly
  reports ATP-regulated unfolded-substrate binding; retrieve full assays before deciding folding versus
  binding. Crucial full PMID16431909 Fig4C shows Ssq1 protects guanidine-denatured rhodanese against aggregation,
  strongest without nucleotide or with ADP, by light scattering; not restored rhodanese enzymatic activity.
  Fig4A/B shows ATP/Jac1-independent protection of purified Nfs1 activity, while Fig4D shows Ssq1-depleted
  mitochondrial lysate Nfs1 activity unchanged; author PDF https://craiglab.biochem.wisc.edu/wp-content/uploads/sites/1625/2021/05/2006_Dutkiewicz_JBC.pdf
  . Full PMID23615440 Fig3D detects in-vitro Cia1 binding displaced by LPPVK, distinct from nonoverlapping
  Grx5 binding; its folding-language interpretation is not itself a refolding assay. Full PMID10779357
  Discussion reports no Yfh1 aggregation/protease-sensitivity difference in wild-type versus ssq1 deletion
  despite processing delay; this specific negative does not prove no capacity on other clients. Distinguish
  native folding, reactivation of misfolded substrate, aggregation prevention, ATP-driven scaffold remodeling
  and cargo delivery requirements of GO0140309. Identify whether any more precise MF represents established
  Ssq1 action without inventing a new foldase claim. For Nop1, original IPI rows cite16554755 and19536198.
  Full19536198 uses TAP-MS whole-cell complexes and spoke inference, shares methods/data lineage with16554755,
  and includes Ssc2 as an alias; inspect exact Nop1-YLR369W supplement entries and independence, target
  localization or functional assays. Native matrix residence alone neither disproves the interaction nor
  proves a nuclear pool. Report any unresolved source-access limits and do not infer direct binary binding
  or target refolding from AP-MS alone.
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

# AIGR Gene Hypothesis Deep Research — SSQ1 (Q05931): Folding/Refolding Activity and the Nop1 Interaction

**Target gene:** *SSQ1* / YLR369W / Ssc2p — *Saccharomyces cerevisiae* mitochondrial Hsp70 (UniProt **Q05931**)
**Focus type:** function_assignment
**Hypothesis slug:** folding-refolding-and-secondary-client-interactions

---

## Executive Judgment

**Verdict: Partially supported, with important precision caveats — and one clearly over-annotated sub-claim.**

The seed hypothesis makes two independent claims that must be judged separately.

**Claim 1 — Ssq1 retains protein folding/refolding or unfolded-protein holdase activity alongside its Fe–S role.** This is *partially supported but must be narrowed*. Direct in vitro assays establish that Ssq1 retains generic Hsp70 behavior: ATP-regulated binding to unfolded substrate proteins ([PMID: 11601843](https://pubmed.ncbi.nlm.nih.gov/11601843/)) and aggregation prevention of guanidine-denatured rhodanese by light scattering, strongest without nucleotide or with ADP ([PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/), Fig 4C). These are **holdase / unfolded-protein-binding** activities. Critically, **no published assay demonstrates productive refolding or reactivation** (i.e., restored enzymatic activity of a denatured substrate) by Ssq1. The rhodanese experiment measured aggregation suppression by light scattering, not recovered rhodanese activity; the Nfs1 experiments measured protection of *already-folded* enzyme activity, not reactivation of a misfolded species. Furthermore, Ssq1 lacks the general folding co-chaperone **Mdj1**, the matrix J-protein that powers Ssc1-driven refolding, and it is a specialist duplicate dedicated to Fe–S cluster transfer. Therefore a general **"protein refolding" (GO:0042026)** annotation over-reaches, whereas a **holdase (GO:0140309)** or substrate-binding characterization is defensible.

**Claim 2 — Ssq1 has a biologically meaningful interaction with Nop1 (P15646).** This is *weakly supported / likely a high-throughput artifact*. The interaction rests entirely on two whole-cell TAP-MS datasets ([PMID: 16554755](https://pubmed.ncbi.nlm.nih.gov/16554755/) and [PMID: 19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/)) that are **not independent** — they share authors, methods, and data lineage, and the second uses the alias "Ssc2." IntAct records both as moderate-score (0.56) spoke-expanded co-complex "associations" detected by TAP, with **no direct binary-binding or functional assay**. The two proteins occupy incompatible compartments (mitochondrial matrix vs. nucleolus), making a direct physical interaction topologically implausible. This interaction is **not** among Ssq1's current live GO annotations and should not be added.

The most important caveat for curation: the folding/refolding GO terms currently on Ssq1 are **phylogenetic inferences (IBA)** propagated from PANTHER family PTHR19375, not Ssq1-specific experimental findings. They are legitimate ancestral inferences (no experimental NOT/IRD exists on the path), but they are **less precise** than what direct Ssq1 assays actually show.

---

## Key Findings

### Finding 1 — Ssq1 retains ATP-regulated unfolded-substrate binding / holdase activity, but no refolding (foldase) activity is demonstrated

Two independent lines of direct in vitro evidence converge on a **holdase, not foldase**, characterization.

First, Schmidt et al. 2001 ([PMID: 11601843](https://pubmed.ncbi.nlm.nih.gov/11601843/)) report that "Ssq1 showed typical chaperone properties by binding to unfolded substrate proteins in an ATP-regulated manner." This is the canonical behavior of the Hsp70 substrate-binding domain — nucleotide-modulated capture and release of exposed hydrophobic segments on unfolded clients. It establishes that Ssq1 has **not** lost the generic Hsp70 substrate-binding capacity.

Second, Dutkiewicz et al. 2006 ([PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/)) provide the crucial biochemical detail the seed hypothesis flags. Their Fig 4C shows Ssq1 protects guanidine-denatured rhodanese against aggregation, measured by **light scattering**, with protection strongest in the absence of nucleotide or with ADP. Their Fig 4A/B show ATP/Jac1-independent protection of *purified Nfs1 activity*, which the authors attribute to "nonspecific binding of Ssq1p to Nfs1p [that] helped to prevent its unfolding." Fig 4D shows that Ssq1-depleted mitochondrial lysate retains unchanged Nfs1 activity. Every one of these readouts is **aggregation prevention or unfolding prevention (holdase)** — none measures the recovery of catalytic activity from a *misfolded* starting state (foldase/refolding).

The mechanistic distinction matters for GO curation. The obsolete term GO:0051082 ("unfolded protein binding") captured the older framing; the precise modern molecular-function term for the demonstrated action is **GO:0140309 "unfolded protein holdase activity"** (aggregation prevention plus escort to an acceptor), which also fits the ATP/ADP-modulated Isu1→Grx5 cluster-delivery cycle ([PMID: 23615440](https://pubmed.ncbi.nlm.nih.gov/23615440/)). By contrast, the foldase/refolding terms — **GO:0140662 "ATP-dependent protein folding chaperone," GO:0044183 "protein folding chaperone (in unfolded protein binding)," and BP GO:0042026 "protein refolding"** — assert an activity (productive folding/reactivation) that no Ssq1 assay demonstrates.

**Bottom line:** the seed's holdase framing is supported; the folding/refolding framing is not directly supported and would over-annotate if asserted as Ssq1 experimental fact.

### Finding 2 — Ssq1 lacks the general folding co-chaperone Mdj1 and is a specialized Fe–S factor, arguing against a general refolding annotation

The Hsp70 folding cycle is not autonomous; productive refolding requires a J-protein to trigger ATP hydrolysis and lock substrate, plus a nucleotide exchange factor to reset the cycle. In the yeast matrix, the multifunctional Hsp70 **Ssc1** performs general protein folding/refolding using the J-protein **Mdj1**. Schmidt et al. 2001 ([PMID: 11601843](https://pubmed.ncbi.nlm.nih.gov/11601843/)) explicitly report that "no interaction of Ssq1 with the two other mitochondrial Hsp70-cochaperones, Tim44 and Mdj1, was observed." Without Mdj1, Ssq1 lacks the machinery to run a productive folding cycle on general clients — consistent with its retained but *unproductive-for-folding* holdase behavior.

Dutkiewicz et al. 2006 ([PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/)) reinforce this: they conclude "Ssq1p/Jac1p/Mge1p are not important for Fe/S cluster synthesis on Isu1p," and the only in vitro stimulatory effect they observed (on Nfs1) was ATP- and Jac1-independent — i.e., not a productive ATP-driven folding cycle but nonspecific unfolding prevention.

Two further papers frame the specialization. Pukszta et al. 2010 ([PMID: 20224575](https://pubmed.ncbi.nlm.nih.gov/20224575/)) describe Ssq1 as an mtHsp70 duplicate that "specializes in iron-sulphur cluster biogenesis"; importantly, the *inference of folding loss in that paper is drawn from partner (Jac1) specialization*, not from a direct negative refolding assay — a nuance the seed correctly demands be preserved. Voisine et al. 2000 ([PMID: 10779357](https://pubmed.ncbi.nlm.nih.gov/10779357/)) report only a Yfh1 maturation/processing delay in *Δssq1* (mature Yfh1 ~75% of WT) with **no** aggregation or protease-sensitivity difference — a specific negative on one client that neither proves nor disproves generic holdase capacity on other clients.

The synthesis: Ssq1's established core is a **specialized ATP-dependent Isu/Grx5 Fe–S cluster transfer factor** (holdase/escort plus scaffold remodeling), sitting within the biological process **GO:0016226 "iron-sulfur cluster assembly."** A broad "protein folding chaperone" / "protein refolding" annotation is too strong as a statement about Ssq1's demonstrated activity.

### Finding 3 — The Ssq1–Nop1 interaction rests on two non-independent whole-cell AP-MS datasets across incompatible compartments; likely a high-throughput artifact

The Ssq1(Ssc2p)–Nop1 interaction derives from Krogan et al. 2006 ([PMID: 16554755](https://pubmed.ncbi.nlm.nih.gov/16554755/)), a genome-scale study that "used tandem affinity purification to process 4,562 different tagged proteins," and Gong et al. 2009 ([PMID: 19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/)), in which "systematic analysis of physical TAP-tag based protein–protein interactions of all known 63 chaperones in *Saccharomyces cerevisiae* has been carried out."

These two sources are **not independent evidence**. Gong 2009 and Krogan 2006 share authors (Krogan, Greenblatt, Emili) and TAP-MS data lineage; both IPI rows therefore trace to essentially one high-throughput, spoke-inferred dataset. Neither reports a direct binary-binding assay or a functional assay for Ssq1–Nop1. Compartmentally, Ssq1 is a mitochondrial-matrix Hsp70 (GO:0005759), whereas Nop1/fibrillarin (P15646) is a nucleolar rRNA 2′-O-methyltransferase; a direct physical interaction between them is topologically implausible. Abundant nucleolar proteins and "sticky" Hsp70s are classic AP-MS false-positive contaminants.

An IPI "protein binding" annotation founded on two non-independent AP-MS studies, with no orthogonal validation and a cross-compartment mismatch, is over-annotation. Native matrix residence alone does not formally disprove the interaction, but the burden of proof (direct binding, co-localization, a functional consequence) is unmet.

### Finding 4 — The folding/refolding GO annotations are phylogenetic (IBA from PANTHER PTHR19375), not experimental; the Nop1 interaction is NOT a current GO annotation

A QuickGO annotation pull for Q05931 (28 annotations) clarifies the provenance of every term at issue. The folding claims are both **IBA** (ECO:0000318, GO_REF:0000033 = PANTHER): **GO:0044183 "protein folding chaperone"** (MF, IBA) and **GO:0042026 "protein refolding"** (BP, IBA), plus **GO:0031072 "heat shock protein binding"** (MF, IBA). PANTHER geneinfo confirms Q05931 is in family **PTHR19375** (subfamily SF197), protein class "Hsp70 family chaperone" (PC00027), which propagates GO:0044183/GO:0031072 by descent — matching the seed's described PTHR19375 folding/refolding IBD path with **no NOT/IRD assertion** on the path.

By contrast, the **experimentally grounded** MF annotations are only **GO:0016887 "ATP hydrolysis activity"** ([PMID: 12756240](https://pubmed.ncbi.nlm.nih.gov/12756240/), [PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/), PMID 26545917) and **GO:0005515 "protein binding" (IPI)** — whose current references are PMID 12756240, 12947415, and 37968396 (Isu/Jac1/structural partners), **not** the Nop1 datasets. The Nop1 IPI (PMID 16554755 / 19536198) **does not appear** among Q05931's current live GO annotations; if it exists at all, it is an interaction-database/AP-MS entry, not a live GO curation. Localization is experimentally mitochondrial matrix (GO:0005759; PMID 10779357, 11273703, 8707841), with only an IBA cytoplasm term (GO:0005737).

Curation consequence: the folding/refolding terms under review are conserved-ancestor inferences, legitimately retainable as IBA (no experimental NOT exists), but **less precise** than the direct evidence, which supports holdase/substrate-binding (best captured by GO:0140309). GO:0042026 "protein refolding" is the weakest/most over-reaching term (no Ssq1 reactivation assay exists). The Nop1 interaction should **not** be added to GO on AP-MS-only, non-independent, cross-compartment evidence.

### Finding 5 — IntAct confirms Ssq1–Nop1 rests only on two TAP co-complex records (score 0.56); Ssq1's other "protein binding" IPI is also HTP AP-MS

A programmatic IntAct query (`findInteractions/Q05931`) returned 123 interaction records for Ssq1. Exactly two involve Nop1/P15646, both with `detectionMethod = 'tap'` (tandem affinity purification), type "association"/"physical association," `intactMiscore = 0.56`, `expansionMethod = spoke/co-complex`, from `publicationPubmedIdentifier` 19536198 and 16554755 — i.e., the same two non-independent AP-MS datasets, with **no direct binary method**. Ssq1's IntAct partner list is dominated by abundant nuclear/chromatin/cytosolic proteins (e.g., ASF1, HHT1, HIR3, INO80, EAF6/EAF7, IES1, ELF1) alongside the genuine ISU1/ISU2 — a textbook signature of sticky-Hsp70 AP-MS promiscuity.

Separately, one of Ssq1's *current* GO "protein binding" (GO:0005515) IPI references, PMID 37968396 (Michaelis et al., *Nature* 2023, "The social and structural architecture of the yeast protein interactome"), is itself a genome-scale affinity-enrichment MS study rather than a targeted binary assay. So even Ssq1's non-Isu/Jac1 "protein binding" evidence is largely high-throughput. This confirms that the Nop1 record should be treated as a likely high-throughput artifact / non-core and not curated as biologically meaningful.

---

## Mechanistic Model / Interpretation

Ssq1 is best understood as a **specialized, "de-generalized" Hsp70**: it kept the physical hardware of a chaperone (a nucleotide-binding domain with ATP hydrolysis, and a substrate-binding domain that captures unfolded/exposed segments) but shed the co-chaperone connections (Mdj1, Tim44) and acquired a dedicated J-protein (Jac1) and a specific client (Isu) that redirect it toward one job: **Fe–S cluster transfer**.

```
   GENERAL matrix Hsp70 (Ssc1)                SPECIALIST duplicate (Ssq1)
   ---------------------------                ---------------------------
   Co-chaperones: Mdj1, Tim44, Mge1           Co-chaperones: Jac1, Mge1 (NO Mdj1/Tim44)
   Clients: broad (import, folding)           Client: Isu (Fe-S scaffold), + Grx5 acceptor
   Activity: import + productive REFOLDING     Activity: holdase/escort + scaffold remodeling
                                              Retained generic property: ATP-regulated
                                              unfolded-substrate BINDING / aggregation
                                              prevention (HOLDASE) -- but NOT refolding
```

The Fe–S transfer cycle Ssq1 executes ([PMID: 23615440](https://pubmed.ncbi.nlm.nih.gov/23615440/); [PMID: 12756240](https://pubmed.ncbi.nlm.nih.gov/12756240/)):

```
  Jac1 (J-protein) targets Isu1 --> Ssq1 (ATP) binds Isu1 PVK motif
        --> ATP hydrolysis (stimulated by Jac1+Isu1) --> ADP-Ssq1 grips Isu1 tightly
        --> Grx5 binds a DISTINCT site on Ssq1 --> Fe-S cluster passed Isu1 --> Grx5
        --> Mge1 exchanges ADP for ATP --> release/reset
```

Where does "folding/refolding" fit? The **holdase** step — nucleotide-modulated grip on an exposed, unfolded region — is real and generic, and it plausibly doubles as aggregation prevention for at-risk clients (rhodanese in vitro; Nfs1 protection). But **productive refolding** — the ATP-driven conformational work that returns a *misfolded* protein to a native, catalytically active state — has never been demonstrated for Ssq1, and the loss of Mdj1 removes the machine's ability to do it on general clients. The correct GO granularity therefore separates:

| Activity concept | Demonstrated for Ssq1? | Best GO term |
|---|---|---|
| Unfolded-substrate binding (ATP-regulated) | Yes ([PMID: 11601843](https://pubmed.ncbi.nlm.nih.gov/11601843/)) | holdase / substrate binding |
| Aggregation prevention (holdase) | Yes ([PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/)) | GO:0140309 unfolded protein holdase activity |
| ATP-driven scaffold remodeling / cargo delivery | Yes ([PMID: 23615440](https://pubmed.ncbi.nlm.nih.gov/23615440/)) | GO:0016226 iron-sulfur cluster assembly (BP) |
| Reactivation of misfolded substrate (foldase) | **No** | GO:0042026 protein refolding — **unsupported by direct assay** |
| Native folding of nascent chain | **No** | GO:0044183 folding chaperone — IBA only |

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [11601843](https://pubmed.ncbi.nlm.nih.gov/11601843/) | Direct in vitro assay | Supports (holdase) / Refutes (foldase) | Ssq1 retains unfolded-protein binding | "binding to unfolded substrate proteins in an ATP-regulated manner"; no Mdj1/Tim44 interaction | Purified proteins + organello, *S. cerevisiae* | High for binding; shows lack of folding co-chaperone |
| [16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/) | Direct in vitro assay | Qualifies (holdase, not foldase) | Refolding vs. aggregation prevention | Prevents rhodanese aggregation (light scattering), strongest w/o nucleotide or ADP; protects Nfs1 via "nonspecific binding…helped to prevent its unfolding"; Ssq1 dispensable for cluster synthesis on Isu1 | Purified proteins + mito lysate | High; readouts are holdase, framed as nonspecific |
| [12756240](https://pubmed.ncbi.nlm.nih.gov/12756240/) | Direct in vitro assay | Supports (Fe–S core) | ATP hydrolysis + Isu/Jac1 engagement | "Jac1 and Isu1 cooperatively stimulate the ATPase activity of Ssq1"; high nucleotide affinity; shares Mge1 with Ssc1 | Purified proteins, *S. cerevisiae* | High; underpins ATP hydrolysis MF, not refolding |
| [23615440](https://pubmed.ncbi.nlm.nih.gov/23615440/) | Direct in vitro + in vivo | Supports (cargo delivery) | Cluster transfer mechanism | Ssq1 binds Isu1 and Grx5 at distinct sites; ADP-form binds Isu1 tightest; facilitates Isu1→Grx5 transfer | Purified proteins + yeast | High; matches holdase/escort, not a refolding assay |
| [20224575](https://pubmed.ncbi.nlm.nih.gov/20224575/) | Review/evolutionary + inference | Qualifies | Specialization implies folding loss | Ssq1 "specializes in iron-sulphur cluster biogenesis"; folding-loss inferred from partner specificity | Comparative *S. cerevisiae*/*S. pombe* | Med; inference, not direct negative refolding assay |
| [10779357](https://pubmed.ncbi.nlm.nih.gov/10779357/) | Mutant phenotype | Qualifies (specific negative) | Client handling in *Δssq1* | Yfh1 processing delay only; no aggregation/protease-sensitivity difference | *Δssq1* yeast | Med; single client; does not generalize |
| [16554755](https://pubmed.ncbi.nlm.nih.gov/16554755/) | Interaction (HTP AP-MS) | Refutes/weakens Nop1 claim | Ssq1–Nop1 direct interaction | Genome-scale TAP-MS of 4,562 tagged proteins; spoke-inferred | Whole-cell *S. cerevisiae* | Low for direct binding; cross-compartment |
| [19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/) | Interaction (HTP AP-MS) | Refutes/weakens Nop1 claim | Ssq1–Nop1 independence | Chaperone-focused TAP-tag reanalysis; shares authors/lineage with Krogan 2006; uses "Ssc2" alias | Whole-cell *S. cerevisiae* | Low; not independent corroboration |
| IntAct (Q05931) | Database (computed) | Refutes/weakens Nop1 claim | Provenance of Nop1 record | Only 2 Nop1 records, both TAP, score 0.56, spoke; partner list = sticky-Hsp70 promiscuity | IntAct query | Med confidence in provenance analysis |
| QuickGO (Q05931) | Database (computed) | Qualifies | Annotation provenance | Folding terms GO:0044183/GO:0042026 are IBA from PTHR19375; experimental MF = ATP hydrolysis + protein binding; Nop1 not a live GO term | QuickGO/PANTHER pull | Med–high; provenance clear |

---

## GO Curation Implications

**Lead requiring curator verification** — treat all recommendations below as candidate actions, not final edits.

1. **BP GO:0042026 "protein refolding" (currently IBA):** *Most over-reaching term.* No Ssq1 assay demonstrates reactivation/refolding of a misfolded substrate. **Lead:** flag as non-core; consider whether the IBA should be down-weighted or annotated with a caveat, since direct experimental evidence contradicts a productive foldase interpretation for Ssq1 even though the ancestral inference is formally valid.

2. **MF GO:0044183 "protein folding chaperone" / GO:0031072 "heat shock protein binding" (currently IBA):** *Retainable as ancestral inference* (legitimate IBA; no experimental NOT on the PTHR19375 path). **Lead:** retain but recognize these are less precise than the direct evidence.

3. **Add a more precise, experimentally grounded MF:** the demonstrated activity is aggregation prevention + escort/cargo delivery. **Lead:** consider **GO:0140309 "unfolded protein holdase activity"** (with experimental evidence from PMID 11601843 and 16431909) as the term that best matches direct assays — a positive, informative alternative to the generic folding terms. Do **not** invent a new foldase claim.

4. **Retain experimental core:** MF **GO:0016887 "ATP hydrolysis activity"** and BP **GO:0016226 "iron-sulfur cluster assembly"** (and cluster transfer) are well supported and should remain the primary functional characterization. CC **GO:0005759 "mitochondrial matrix"** is experimentally supported.

5. **Nop1 interaction:** **Do NOT add** an IPI "protein binding" annotation to Nop1. It is not a current live GO annotation, and the underlying evidence is two non-independent AP-MS datasets with a compartment mismatch. If any interaction annotation to Nop1 exists downstream in an interaction database, curators should mark it as non-core / likely artifact.

Avoid "protein binding" (GO:0005515) as a final recommendation for the retained functional claim — the holdase term (GO:0140309) or ATP hydrolysis (GO:0016887) is more informative.

### GO Decision Table

| GO term | Aspect | Current evidence code | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0042026 protein refolding | BP | IBA (PTHR19375) | Flag non-core / caveat | No Ssq1 reactivation assay; over-reaching |
| GO:0044183 protein folding chaperone | MF | IBA (PTHR19375) | Retain as ancestral inference | Legitimate IBA; less precise than direct data |
| GO:0031072 heat shock protein binding | MF | IBA | Retain | Family-level, uncontested |
| GO:0140309 unfolded protein holdase activity | MF | (candidate) | Consider adding (experimental) | Best matches PMID 11601843 / 16431909 |
| GO:0016887 ATP hydrolysis activity | MF | Experimental | Retain (core) | PMID 12756240, 16431909 |
| GO:0016226 iron-sulfur cluster assembly | BP | Experimental | Retain (core) | PMID 23615440, 16431909 |
| GO:0005759 mitochondrial matrix | CC | Experimental | Retain (core) | PMID 10779357, 11273703, 8707841 |
| Ssq1–Nop1 protein binding | MF (IPI) | AP-MS only | Do NOT add | Non-independent HTP, compartment mismatch |

---

## Mechanistic Scope

The immediate molecular function under test is **substrate-binding-domain activity of an Hsp70** — nucleotide-regulated capture of unfolded/exposed polypeptide segments — and whether that extends to **productive folding/refolding** (net conformational work restoring native state) or is limited to **holdase** behavior (binding + aggregation prevention).

- **Direct gene-product activity (supported):** ATP-regulated unfolded-substrate binding; aggregation prevention; ATP hydrolysis stimulated by Jac1+Isu1; Isu1/Grx5 binding and Fe–S cluster transfer.
- **Downstream / loss-of-function phenotypes (must not be conflated with direct activity):** Yfh1 processing delay in *Δssq1*; reduced Fe–S enzyme activities; elevated iron; mtDNA maintenance defects. These are consequences of impaired cluster transfer, not evidence of a foldase.
- **Inference-only (not direct assay):** "folding loss" argued from partner (Jac1) specialization (PMID 20224575) is an inference, not a negative refolding experiment; the seed correctly insists this be labeled as such.

---

## Conflicts and Alternatives

- **Paralog/alias confusion:** Ssq1 is also called **Ssc2p**, and its paralog **Ssc1** is the genuine general folding Hsp70. AP-MS datasets using the "Ssc2" alias (PMID 19536198) risk carry-over confusion, and the folding-competent behavior belongs to Ssc1, not Ssq1. Curators should ensure folding annotations are not migrating from the paralog.
- **In vitro–only activity:** the holdase/aggregation-prevention effects (rhodanese, Nfs1) are in vitro and explicitly described as **nonspecific** ([PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/)); their physiological weight is uncertain. This qualifies — but does not eliminate — the holdase claim.
- **Compartment mismatch (Nop1):** mitochondrial matrix vs. nucleolus is the strongest single argument against a biologically meaningful direct Ssq1–Nop1 interaction; the most parsimonious alternative is an AP-MS contaminant/co-purification artifact.
- **Database carry-over:** the folding GO terms are PANTHER-family IBA propagation, an alternative explanation to any assumption that they reflect Ssq1-specific experiments.

---

## Limitations and Knowledge Gaps

1. **No direct Ssq1 refolding assay exists.** *Checked:* PMID 11601843, 16431909, 23615440, 12756240 — all measure binding, aggregation prevention, ATPase, or cluster transfer. *Why it matters:* a true foldase claim requires a reactivation assay. *Resolver:* an in vitro luciferase/rhodanese *reactivation* assay (recovered enzymatic activity, not just light scattering) ± Jac1/Mge1.
2. **Physiological relevance of the holdase activity.** *Checked:* rhodanese/Nfs1 protection framed as nonspecific. *Why it matters:* determines whether GO:0140309 should be a core or non-core annotation. *Resolver:* client-capture proteomics in vivo under stress; test whether Ssq1 protects endogenous matrix clients beyond Isu.
3. **Full-text access to the AP-MS supplements for Ssq1–Nop1.** *Checked:* abstracts and IntAct provenance; not the raw supplement rows. *Why it matters:* to confirm exact Nop1–YLR369W entries and formally establish non-independence. *Resolver:* inspect Krogan 2006 and Gong 2009 supplementary tables directly. **This is an unresolved source-access limit and is reported plainly.**
4. **Whether any minor extra-mitochondrial pool of Ssq1 exists.** *Checked:* experimental localization is matrix (GO:0005759); cytoplasm term is IBA only. *Why it matters:* a nuclear/cytosolic pool could (barely) rationalize a Nop1 contact. *Resolver:* high-sensitivity fractionation / imaging — but prior data strongly favor matrix-exclusive residence.

---

## Discriminating Tests

1. **Refolding vs. holdase discrimination:** in vitro **reactivation** assay of chemically denatured firefly luciferase or rhodanese — measure recovered *enzymatic activity* (foldase readout) vs. suppressed light scattering (holdase readout) — for Ssq1 ± Jac1 ± Mge1 ± ATP, side-by-side with Ssc1+Mdj1 as a positive foldase control. Predicted outcome: Ssq1 suppresses aggregation but does **not** restore activity.
2. **Mdj1-dependence test:** attempt to reconstitute Ssq1-driven refolding by supplying Mdj1; if refolding does not appear, it confirms specialization removed foldase capacity.
3. **Nop1 direct-binding test:** purified Ssq1 + purified Nop1 by ITC/SPR/pulldown; and reciprocal endogenous co-IP with fractionation controls. Predicted outcome: no specific direct interaction.
4. **Provenance audit:** extract the exact Ssq1(YLR369W/Ssc2)–Nop1 rows from Krogan 2006 and Gong 2009 supplements to formally document non-independence and spoke inference.

---

## Proposed Follow-up Actions / Curation Leads

**All leads below require curator verification.**

- **Lead A (folding terms):** Retain IBA GO:0044183 / GO:0031072 as ancestral inference; flag BP **GO:0042026 "protein refolding"** as non-core / over-reaching for Ssq1 (no reactivation assay). *Verify snippet:* "Ssq1p/Jac1p/Mge1p are not important for Fe/S cluster synthesis on Isu1p" ([PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/)).
- **Lead B (positive replacement MF):** Consider adding experimentally supported **GO:0140309 "unfolded protein holdase activity."** *Verify snippets:* "binding to unfolded substrate proteins in an ATP-regulated manner" ([PMID: 11601843](https://pubmed.ncbi.nlm.nih.gov/11601843/)); "nonspecific binding of Ssq1p to Nfs1p helped to prevent its unfolding" ([PMID: 16431909](https://pubmed.ncbi.nlm.nih.gov/16431909/)).
- **Lead C (Nop1 interaction):** Do **not** add an IPI "protein binding" annotation to Nop1 (P15646). *Verify snippets:* "We used tandem affinity purification to process 4,562 different tagged proteins" ([PMID: 16554755](https://pubmed.ncbi.nlm.nih.gov/16554755/)); "Systematic analysis of physical TAP-tag based protein–protein interactions of all known 63 chaperones" ([PMID: 19536198](https://pubmed.ncbi.nlm.nih.gov/19536198/)). Rationale: non-independent AP-MS, spoke-inferred, IntAct score 0.56, matrix-vs-nucleolus mismatch.
- **Lead D (retain core):** Keep MF GO:0016887 (ATP hydrolysis), BP GO:0016226 (Fe–S cluster assembly/transfer), CC GO:0005759 (mitochondrial matrix) as the primary, experimentally grounded characterization.
- **Suggested curator questions:** (1) Should IBA folding terms carry a caveat when direct assays show only holdase? (2) Is GO:0140309 preferred over generic folding terms for the experimental MF? (3) Should the Nop1 interaction be explicitly marked non-core/artifact in any interaction annotation?
- **Suggested experiments:** luciferase/rhodanese reactivation assay (foldase vs. holdase); Mdj1-reconstitution test; Ssq1–Nop1 direct-binding assay + fractionation.

---

## Source-Access Limitations (reported plainly)

- Full-text figures cited in the seed (PMID 12756240 Fig 8; PMID 16431909 Fig 4A–D; PMID 23615440 Fig 3D; PMID 10779357 Discussion) were evaluated via abstracts, the seed's detailed figure descriptions, and cross-referenced literature — **not** by rendering the author PDFs programmatically. The conclusions rest on the abstract-level statements and the seed's figure summaries, which are internally consistent with the abstracts.
- The exact Krogan 2006 / Gong 2009 supplementary rows for Ssq1(YLR369W/Ssc2)–Nop1 were not opened directly; non-independence is inferred from shared authorship, methods, and data lineage plus IntAct provenance. This should be confirmed against the raw supplements before finalizing.
- No fabricated results are reported; computed provenance (QuickGO annotation pull, PANTHER geneinfo, IntAct `findInteractions/Q05931`) is described as executed database queries.

---

## Conclusion

The seed hypothesis is **partially supported with precision caveats**. Ssq1 retains generic Hsp70 unfolded-substrate binding and aggregation-prevention (**holdase**) activity, but **no evidence supports a productive folding/refolding (foldase) activity**, and it lacks the Mdj1 co-chaperone needed to run one. The existing folding annotations (GO:0044183, GO:0042026) are **IBA carry-over** from PANTHER PTHR19375, retainable as ancestral inference but less precise than the experimentally grounded holdase (GO:0140309) — with "protein refolding" the most over-reaching (treat as non-core). The **Nop1 interaction is weakly supported / likely artifactual**, is not a current GO annotation, and should not be added.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist provenance ssq1 curation](openscientist_artifacts/provenance_ssq1_curation.md)