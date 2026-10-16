---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:48:18.833642'
end_time: '2026-09-21T05:07:32.872772'
duration_seconds: 1154.04
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ATG14
  gene_symbol: ATG14
  uniprot_accession: Q6ZNE5
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: phagosomal-localization-and-posttranscriptional-regulation
  hypothesis_text: Human ATG14 localizes to phagocytic vesicles and regulates gene
    expression at a post-transcriptional level. Adjudicate these separately. For localization,
    trace the mouse Q8CDJ3 IDA source PMID:22493499 and distinguish exclusion from
    one SLAMF1/VPS34/UVRAG interaction from exclusion from every phagosome. For GO:0010608,
    read the actual definition and PMID:23878393 protein-versus-transcript and BECN1-complex-stability
    experiments; determine whether abundance/stability control meets the term or an
    RNA/translation step is required. Do not dispute the already directly demonstrated
    ATG14 mitophagy/complex-stability roles or manufacture negative experiments from
    missing panels.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/ATG14/ATG14-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human ATG14 localizes to phagocytic vesicles and\
    \ regulates gene expression at a post-transcriptional\n  level. Adjudicate these\
    \ separately. For localization, trace the mouse Q8CDJ3 IDA source PMID:22493499\n\
    \  and distinguish exclusion from one SLAMF1/VPS34/UVRAG interaction from exclusion\
    \ from every phagosome.\n  For GO:0010608, read the actual definition and PMID:23878393\
    \ protein-versus-transcript and BECN1-complex-stability\n  experiments; determine\
    \ whether abundance/stability control meets the term or an RNA/translation step\n\
    \  is required. Do not dispute the already directly demonstrated ATG14 mitophagy/complex-stability\
    \ roles\n  or manufacture negative experiments from missing panels.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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
- **Gene directory:** ATG14
- **Gene symbol:** ATG14
- **UniProt accession:** Q6ZNE5

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** phagosomal-localization-and-posttranscriptional-regulation
- **Source file:** genes/human/ATG14/ATG14-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ATG14 localizes to phagocytic vesicles and regulates gene expression at a post-transcriptional level. Adjudicate these separately. For localization, trace the mouse Q8CDJ3 IDA source PMID:22493499 and distinguish exclusion from one SLAMF1/VPS34/UVRAG interaction from exclusion from every phagosome. For GO:0010608, read the actual definition and PMID:23878393 protein-versus-transcript and BECN1-complex-stability experiments; determine whether abundance/stability control meets the term or an RNA/translation step is required. Do not dispute the already directly demonstrated ATG14 mitophagy/complex-stability roles or manufacture negative experiments from missing panels.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human ATG14 localizes to phagocytic vesicles and regulates gene expression at a post-transcriptional
  level. Adjudicate these separately. For localization, trace the mouse Q8CDJ3 IDA source PMID:22493499
  and distinguish exclusion from one SLAMF1/VPS34/UVRAG interaction from exclusion from every phagosome.
  For GO:0010608, read the actual definition and PMID:23878393 protein-versus-transcript and BECN1-complex-stability
  experiments; determine whether abundance/stability control meets the term or an RNA/translation step
  is required. Do not dispute the already directly demonstrated ATG14 mitophagy/complex-stability roles
  or manufacture negative experiments from missing panels.
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

# AIGR Deep Research Report: ATG14 Phagosomal Localization and Post-transcriptional Regulation

**Gene:** ATG14 (human, UniProt Q6ZNE5; mouse ortholog Q8CDJ3)
**Focus type:** function_assignment
**Hypothesis slug:** phagosomal-localization-and-posttranscriptional-regulation
**Source file:** genes/human/ATG14/ATG14-ai-review.yaml

---

## Summary

The seed hypothesis packages two independent GO assignments for human ATG14 that this focused review adjudicates separately, as instructed. On tracing each annotation back to its primary IDA/IMP source, **both are over-annotations** and neither is supported as a direct function of the ATG14 gene product. This is the inverted-pyramid answer: **remove both, retain the correct alternative already present.**

The **phagocytic-vesicle localization (GO:0045335)** originates as a mouse MGI IDA on Q8CDJ3, cited to [PMID:22493499](https://pubmed.ncbi.nlm.nih.gov/22493499/). That paper studies Slamf1 recruiting a Beclin-1/Vps34/UVRAG complex to *E. coli* phagosomes and explicitly reports that **Atg14L was excluded** from the complex — a negative co-immunoprecipitation, not a positive localization. The annotation therefore inverts the polarity of its own source. It then propagates to human Q6ZNE5 as an IEA by Ensembl orthology.

The **post-transcriptional-regulation term (GO:0010608)**, a human IMP by ParkinsonsUK-UCL cited to [PMID:23878393](https://pubmed.ncbi.nlm.nih.gov/23878393/), rests on ATG14 controlling beclin-1 Ser90/Ser93 **phosphorylation** and BECN1-complex stability — strictly **post-translational** events. GO:0010608 requires modulation of an RNA-level step (RNA processing, mRNA stability, or translation) after transcript production, and excludes protein-level proteostasis. The same paper already yielded the correct term, **GO:0061635 (regulation of protein complex stability)**. ATG14 has no RNA-binding domain, and the only paper linking it to post-transcriptional machinery ([PMID:36097301](https://pubmed.ncbi.nlm.nih.gov/36097301/)) shows ATG14 mRNA is a **target** of m6A/YTHDF1 translation control, not an effector. The directly demonstrated ATG14 roles in autophagosome–endolysosome fusion, PI3KC3 complex-I scaffolding, complex stability, and mitophagy are undisputed and should be retained.

---

## Executive Judgment

**Verdict: Over-annotated (refuted for both sub-claims as stated).**

1. **GO:0045335 (phagocytic vesicle) — refuted as a positive annotation.** The sole IDA source (PMID:22493499) provides **no positive localization data** placing ATG14 on a phagosome. It reports a negative interaction: Atg14L was excluded from the Slamf1/Beclin-1/Vps34/UVRAG phagosomal complex. The seed's framing — "distinguish exclusion from one interaction from exclusion from every phagosome" — does not rescue the term, because the source supplies no positive phagosomal evidence of any kind. The correct curatorial stance is that the term **lacks support**, not that localization is affirmatively disproven.

2. **GO:0010608 (post-transcriptional regulation of gene expression) — refuted as a term misassignment.** The IMP source (PMID:23878393) demonstrates post-translational control (beclin-1 phosphorylation, complex stability), which fails the term's RNA-step requirement. This is best read as a "post-translational → post-transcriptional" conflation. **GO:0061635**, already annotated from the same paper, correctly captures the biology and should be retained in its place.

**Most important caveats.** (a) The corroborating statement that the LAP/phagosomal PI3K complex "lacks ATG14" comes from [PMID:26098576](https://pubmed.ncbi.nlm.nih.gov/26098576/), **retracted in 2024** ([PMID:38438803](https://pubmed.ncbi.nlm.nih.gov/38438803/)); it is used only as orientation, and the refutation stands on the primary IDA/IMP sources without it. (b) Full-text figure panels of PMID:23878393 were not programmatically retrievable; the adjudication uses the abstract-level mechanism, which is unambiguously post-translational. (c) Nothing here disputes ATG14's established mitophagy and complex-stability roles.

---

## Key Findings

### Finding 1 — The phagocytic-vesicle (GO:0045335) annotation is contradicted by its own IDA source

Mouse Atg14 (Q8CDJ3) carries **GO:0045335 (phagocytic vesicle)** with evidence **IDA / `located_in`**, sourced to [PMID:22493499](https://pubmed.ncbi.nlm.nih.gov/22493499/) (Ma et al. 2012, *J. Biol. Chem.*), per QuickGO annotation retrieval (n=70 annotations for the accession). Human Q6ZNE5 does **not** independently carry GO:0045335 in QuickGO — it inherits the risk only by orthology.

The paper studies **Slamf1** recruiting a Beclin-1/Vps34/UVRAG complex to *E. coli*-containing phagosomes to regulate membrane fusion and NADPH oxidase 2 (NOX2) activity. The decisive sentence is a **negative result** for Atg14L:

> *"Because Slamf1 did not interact with Atg14L or Rubicon, which can also form a complex with Vps34 and Beclin-1, we conclude that Slamf1 recruits a subset of Vps34-associated proteins, which is involved in membrane fusion and NOX2 regulation."* — [PMID:22493499](https://pubmed.ncbi.nlm.nih.gov/22493499/)

This is the only reference behind the IDA. It contains no immunofluorescence, fractionation, or other assay placing Atg14 on a phagocytic vesicle; it reports the opposite — Atg14L was **excluded** from the phagosome-recruited Vps34 subcomplex. An IDA `located_in` phagocytic vesicle built on a negative co-IP is a probable curation error and should be removed.

Independent orientation: LC3-associated phagocytosis (LAP) uses a Class III PI3K complex "containing UVRAG but lacking ATG14" ([PMID:26098576](https://pubmed.ncbi.nlm.nih.gov/26098576/)). This paper was **retracted in 2024** ([PMID:38438803](https://pubmed.ncbi.nlm.nih.gov/38438803/)) and is cited here only as field-orientation, not primary evidence. The distinction between the ATG14-containing autophagy-initiation complex and the Rubicon/UVRAG-containing phagosomal complex is a broadly accepted feature of the field and does not depend on the retracted paper.

### Finding 2 — The GO:0010608 annotation conflates post-translational with post-transcriptional control

Human ATG14 (Q6ZNE5) carries **GO:0010608 (post-transcriptional regulation of gene expression)** with evidence **IMP / `involved_in`**, sourced to [PMID:23878393](https://pubmed.ncbi.nlm.nih.gov/23878393/) (Fogel et al. 2013).

The ontology definitions are decisive:
- **GO:0010608** = "Any process that modulates the frequency, rate or extent of gene expression **after the production of an RNA transcript**."
- **GO:0010467 (gene expression)** = "the process in which a gene's sequence is converted into a mature gene product (protein or RNA) … production of an RNA transcript and its processing, as well as translation and maturation."

GO:0010608 therefore requires a step acting on **RNA processing, mRNA stability, or translation**, and **excludes** post-translational proteostasis (protein modification, complex assembly/stability).

Fogel et al. describe exactly a **post-translational** mechanism:

> *"we demonstrated that human Atg14 is critical in controlling an autophagy-dependent phosphorylation of beclin-1. We map these novel phosphorylation sites to serines 90 and 93 and demonstrate that phosphorylation at these sites is necessary for maximal autophagy."* — [PMID:23878393](https://pubmed.ncbi.nlm.nih.gov/23878393/)

Phosphorylating an existing beclin-1 protein and stabilizing the BECN1/Vps34 complex are protein-level events. Critically, the **same paper already generated GO:0061635 (regulation of protein complex stability)** as an IMP for Q6ZNE5 — that term correctly captures the finding. GO:0010608 appears to be a term-selection error (a likely "post-translational → post-transcriptional" slip), since no RNA-level or translational assay is described.

### Finding 3 — ATG14 is a target, not an effector, of post-transcriptional regulation, and has no RNA-binding domain

A directed literature search for ATG14 acting on an RNA/translation step returned a single relevant primary paper — [PMID:36097301](https://pubmed.ncbi.nlm.nih.gov/36097301/) (Huang et al. 2022) — reporting the **opposite direction of causality**:

> *"YTHDF1 promoted the translation of autophagy-related genes ATG14, thus boosting autophagy."* — [PMID:36097301](https://pubmed.ncbi.nlm.nih.gov/36097301/)

Here **ATG14 mRNA is the substrate** of m6A/YTHDF1 post-transcriptional machinery; ATG14 protein is not the regulator of any RNA step. This is precisely the inverse of what GO:0010608 would assert for ATG14.

Structurally, InterPro for Q6ZNE5 returns only the **ATG14/VPS38 autophagy family** (IPR018791; Pfam **PF10186**, "Vacuolar sorting 38 and autophagy-related subunit 14"; PANTHER PTHR13664). There is **no RNA-binding, nucleic-acid-binding, or ribonucleoprotein domain**, so there is no structural basis for a direct post-transcriptional effector activity.

### Finding 4 — Both disputed annotations are root manual annotations amplified cross-species by orthology

QuickGO provenance tracing shows how each error propagates:

| Term | Root annotation | Evidence | Source (date) | Propagation |
|------|-----------------|----------|---------------|-------------|
| GO:0045335 (phagocytic vesicle) | mouse Q8CDJ3 | IDA (MGI) | PMID:22493499 (2014-01-30) | → human Q6ZNE5 as **IEA** (Ensembl, GO_REF:0000107, withFrom Q8CDJ3) |
| GO:0010608 (post-transcriptional reg.) | human Q6ZNE5 | IMP (ParkinsonsUK-UCL) | PMID:23878393 (2015-11-16) | → mouse Q8CDJ3 as **IEA** (Ensembl) and **ISO** (GO_Central), both withFrom Q6ZNE5 |

Each erroneous root is multiplied by electronic/phylogenetic transfer across species. **Curation must fix the root** (MGI for GO:0045335; ParkinsonsUK-UCL for GO:0010608); correcting only downstream IEA/ISO projections would leave the source error to re-propagate.

---

## Mechanistic Model / Interpretation

Both annotations fail for structurally analogous reasons — each attaches a GO term whose *scope or polarity* does not match the underlying experiment:

```
GO:0045335  (phagocytic vesicle, IDA)
   source = PMID:22493499
   experiment: Slamf1 pulls down Beclin-1 / Vps34 / UVRAG at phagosomes
   result for ATG14L: NO interaction  →  EXCLUDED from the complex
   annotation asserts: ATG14 located_in phagocytic vesicle
   ──►  POLARITY ERROR: absence recorded as presence

GO:0010608  (post-transcriptional regulation of gene expression, IMP)
   source = PMID:23878393
   experiment: ATG14 controls beclin-1 Ser90/93 phosphorylation
               + BECN1 complex stability
   level of action: PROTEIN (post-translational)
   term requires:   RNA / translation step (post-transcriptional)
   ──►  SCOPE ERROR: post-translational recorded as post-transcriptional
        (correct term GO:0061635 already exists from the same paper)
```

**Where ATG14 genuinely acts.** ATG14 (Barkor/ATG14L) is the autophagy-specific targeting subunit of the Class III PI3K (PI3KC3) complex I, partnering Beclin-1, Vps34 (PIK3C3), and Vps15. Its directly demonstrated functions include promoting membrane tethering and SNARE-mediated autophagosome–endolysosome fusion via STX17–SNAP29–VAMP8 ([PMID:25686604](https://pubmed.ncbi.nlm.nih.gov/25686604/)); scaffolding and stabilizing the BECN1/Vps34 complex and enabling beclin-1 phosphorylation ([PMID:23878393](https://pubmed.ncbi.nlm.nih.gov/23878393/)); and supporting NRBF2-modulated Atg14L-linked Vps34 activity ([PMID:24849286](https://pubmed.ncbi.nlm.nih.gov/24849286/)). These undisputed roles are captured by autophagy-initiation, PI3K-complex, and complex-stability terms — **not** by phagocytic-vesicle localization or post-transcriptional regulation.

The key curatorial distinction is between the **ATG14-containing PI3KC3 complex I** (canonical autophagy initiation) and the **Rubicon/UVRAG-containing complex** operating on phagosomes during LAP. ATG14 belongs to the former; PMID:22493499 is a direct experimental demonstration of that partition.

---

## Evidence Base

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| [PMID:22493499](https://pubmed.ncbi.nlm.nih.gov/22493499/) | Interaction (co-IP), localization | **Refutes support** for GO:0045335 | Is ATG14 in the Slamf1 phagosomal Vps34 complex? | Atg14L did **not** interact; excluded from the Slamf1/Beclin-1/Vps34/UVRAG complex | Mouse macrophages, *E. coli* phagosomes; HEK293 co-IP | High. Sole IDA source; a negative result for ATG14. |
| [PMID:23878393](https://pubmed.ncbi.nlm.nih.gov/23878393/) | Mutant phenotype / biochemistry (IMP) | **Refutes** GO:0010608; **supports** GO:0061635 | Does ATG14 regulate an RNA/translation step? | ATG14 controls beclin-1 Ser90/93 **phosphorylation** and BECN1 complex stability (post-translational) | Human cells | High for mechanism; full-text figure panels not retrievable programmatically. |
| [PMID:36097301](https://pubmed.ncbi.nlm.nih.gov/36097301/) | Direct assay (translation) | **Competing / refutes** ATG14 as post-transcriptional effector | Is ATG14 an RNA-level regulator? | ATG14 mRNA is a **target** of m6A/YTHDF1 translational promotion | Auditory hair cells, cisplatin model | Moderate-high; establishes opposite causality. |
| [PMID:26098576](https://pubmed.ncbi.nlm.nih.gov/26098576/) | Direct assay (complex composition) | Qualifies (corroborates non-phagosomal ATG14) | Does the LAP PI3K complex contain ATG14? | Complex "containing UVRAG but lacking ATG14 and Ambra1" | Macrophages, LAPosomes | **Low — RETRACTED ([PMID:38438803](https://pubmed.ncbi.nlm.nih.gov/38438803/)).** Orientation only. |
| [PMID:25686604](https://pubmed.ncbi.nlm.nih.gov/25686604/) | Direct assay (reconstitution) | Supports genuine ATG14 function | What is ATG14's core activity? | ATG14 tethers membranes; enhances STX17–SNAP29–VAMP8 fusion | In vitro + cells | High; context for true function, not disputed. |
| [PMID:24849286](https://pubmed.ncbi.nlm.nih.gov/24849286/) | Mutant phenotype | Supports genuine ATG14 function | ATG14-linked Vps34 regulation | NRBF2 binds Atg14L, enhances Atg14L-linked Vps34 kinase activity | Mouse cells/liver | High; context for true function. |
| QuickGO / InterPro (Q6ZNE5, Q8CDJ3) | Computational / database | Supports over-annotation verdict | Provenance and domain content | Root manual annotations propagate by IEA/ISO; no RNA-binding domain (only PF10186) | Database records | High for provenance; database-level evidence. |

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Term (aspect) | Annotation source | Recommended action | Rationale |
|-------|---------------|-------------------|--------------------|-----------|
| GO:0045335 | phagocytic vesicle (CC) | mouse Q8CDJ3 IDA, PMID:22493499 → human IEA | **REMOVE / do-not-propagate at root** | Source reports ATG14 *exclusion* from the Slamf1 complex; no positive localization data. |
| GO:0010608 | post-transcriptional regulation of gene expression (BP) | human Q6ZNE5 IMP, PMID:23878393 → mouse IEA/ISO | **REMOVE at root** | Evidence is post-translational (phosphorylation / complex stability); fails the term definition. |
| GO:0061635 | regulation of protein complex stability (BP) | human Q6ZNE5 IMP, PMID:23878393 | **RETAIN** | Correctly captures the BECN1-complex-stability role from the same paper. |
| GO:0031647 | regulation of protein stability (BP) | lead | **CONSIDER (lead)** | Captures ATG14→BECN1 protein-level stabilization if curator judges it distinct from GO:0061635. |

Both removals should occur **at the root annotation** so the derived cross-species copies stop being generated. Avoid "protein binding" as a substitute; GO:0061635 is the informative, evidence-matched term.

---

## Mechanistic Scope

- **Direct molecular functions tested:** (a) whether ATG14 physically resides on phagosomal membranes, and (b) whether ATG14 acts at an RNA/translational step of gene expression.
- **What the data show:** ATG14 is a subunit of the autophagy-specific Class III PI3K complex I. Its beclin-1 regulation is post-translational (phosphorylation, complex stabilization). The phagosomal PI3P/NOX2 activity in PMID:22493499 is driven by a **different, ATG14-lacking** (UVRAG-containing) complex.
- **Downstream vs direct:** Phagolysosomal maturation, NOX2 activity, and "gene-expression"-flavored autophagy phenotypes are downstream/indirect; they are not attributable to ATG14 localizing to phagosomes or to an ATG14 RNA-level activity.

---

## Conflicts and Alternatives

- **Curation carry-over / polarity error**, not a real organism difference: the phagosomal localization belongs to the UVRAG/Rubicon complex, and the IDA reads a negative co-IP as positive localization.
- **Scope/lexical conflation:** the IMP "post-transcriptional" label most plausibly conflates "post-translational" with "post-transcriptional."
- **Paralog/complex confusion:** LAP and Slamf1-phagosome PI3K activity use UVRAG/Rubicon complexes explicitly **without ATG14** — the opposite subunit branch.
- **Direction reversal:** the only literature linking ATG14 to an RNA/translation step (PMID:36097301) makes ATG14 mRNA a **target** of m6A/YTHDF1, not an effector — reinforcing removal of GO:0010608.
- **Retraction caveat:** PMID:26098576 (ATG14-independent phagosomal PI3K) is retracted and used only as corroborating context; the adjudication rests on the primary IDA/IMP sources and ontology definitions.

---

## Limitations and Knowledge Gaps

1. **Full-text of PMID:23878393 not programmatically retrievable.** Only front matter/abstract was accessible via NCBI efetch (PMC3753860). *Why it matters:* a hidden RNA-level assay could theoretically justify GO:0010608. *Resolution:* manual full-text read of figures. Risk is low because the described ATG14 activity (regulating an existing protein's phosphorylation/stability) is post-translational regardless of any transcript readout.
2. **Negative-space certainty for phagosome localization.** Absence of positive localization in one paper does not logically prove ATG14 is never on any phagocytic vesicle. *Why it matters:* a curator might consider a generalized term. *Resolution:* a targeted search found no positive ATG14 phagosome-localization report; the correct stance is that the term **lacks support**.
3. **Database-level provenance/domain evidence.** QuickGO/InterPro results are database evidence, appropriate for tracing propagation and domain content but not primary experiment.
4. **Retraction of PMID:26098576** removes one corroborating line; the core refutation is unaffected.

---

## Discriminating Tests

- **Read PMID:23878393 full text/figures** to confirm no assay measures ATG14 acting on ATG mRNA levels, transcript stability, or translation. If none, GO:0010608 removal is definitive.
- **Re-examine PMID:22493499 figures** for any imaging/fractionation placing Atg14L on phagosomes independent of the Slamf1 co-IP. If none, GO:0045335 removal is definitive.
- **Direct localization assay:** immunofluorescence / immuno-EM / phagosome fractionation for endogenous ATG14 in macrophages engulfing beads/bacteria, versus UVRAG/Rubicon controls (expected: ATG14 absent).
- **ATG14-KO vs Rubicon-KO** effect on phagosomal LC3/PI3P (LAP should be ATG14-independent).
- **RNA-interaction screen (CLIP/RIP/eCLIP)** for ATG14 protein to test for any RNA-binding (expected negative, consistent with absence of an RNA-binding domain).
- **qRT-PCR vs Western for BECN1** plus reporter/translation assays upon ATG14 perturbation to formally exclude any RNA/translation-level step.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Candidate reference snippets to verify:**
- PMID:22493499 — *"Because Slamf1 did not interact with Atg14L or Rubicon … we conclude that Slamf1 recruits a subset of Vps34-associated proteins."* → supports **removing** GO:0045335 for ATG14.
- PMID:23878393 — *"human Atg14 is critical in controlling an autophagy-dependent phosphorylation of beclin-1 … serines 90 and 93."* → supports **removing** GO:0010608 and **retaining** GO:0061635; consider GO:0031647.
- PMID:36097301 — *"YTHDF1 promoted the translation of autophagy-related genes ATG14."* → ATG14 is a target, not an effector, of post-transcriptional control.

**Suggested curator questions:**
1. Is the GO:0045335 IDA a mis-transfer of the complex's phagosomal localization to ATG14, given the source reports ATG14 exclusion?
2. Is GO:0010608 a lexical conflation of "post-translational" with "post-transcriptional"?
3. Should GO:0061635 be treated as the canonical replacement capturing the PMID:23878393 finding?

**Act at the root annotation:** GO:0045335 originates from the **MGI** IDA on mouse Q8CDJ3; GO:0010608 originates from the **ParkinsonsUK-UCL** IMP on human Q6ZNE5. Each propagates to the other species by Ensembl IEA / GO_Central ISO, so correcting the root removes the derived copies. Consider contacting MGI and the ParkinsonsUK-UCL group.

**Do not disturb:** the directly demonstrated ATG14 roles in autophagosome–endolysosome fusion (PMID:25686604), PI3KC3 complex-I scaffolding/Vps34 regulation (PMID:24849286), BECN1-complex stability (PMID:23878393 → GO:0061635), and mitophagy remain well supported and should be retained.

---

## Bottom-Line Answer

For human ATG14 (Q6ZNE5), the **phagocytic-vesicle localization (GO:0045335)** and **post-transcriptional-regulation (GO:0010608)** assignments are **not supported** as positive functions and are recommended for removal at their root annotations. The localization IDA (PMID:22493499) documents ATG14's *exclusion* from the Slamf1/Beclin-1/Vps34/UVRAG phagosomal complex; the GO:0010608 IMP (PMID:23878393) describes **post-translational** control of beclin-1 phosphorylation/complex stability that fails the term definition. Retain **GO:0061635 (regulation of protein complex stability)**, consider GO:0031647 as a lead, and leave the established mitophagy/complex-stability roles undisturbed.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)