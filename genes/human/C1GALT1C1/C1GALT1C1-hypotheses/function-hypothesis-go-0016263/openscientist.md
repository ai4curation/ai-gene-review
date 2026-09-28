---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-17T05:31:55.028136'
end_time: '2026-09-17T05:41:38.402808'
duration_seconds: 583.37
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: C1GALT1C1
  gene_symbol: C1GALT1C1
  uniprot_accession: Q96EU7
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0016263
  hypothesis_text: C1GALT1C1 does not have N-acetylgalactosaminide beta-1,3-galactosyltransferase
    activity (GO:0016263).
  term_context: '- Term: N-acetylgalactosaminide beta-1,3-galactosyltransferase activity
    (GO:0016263)

    - Evidence type: IMP

    - Original reference: PMID:37216524

    - Existing annotation is negated: true'
  reference_context: '- PMID:37216524'
  source_file: genes/human/C1GALT1C1/C1GALT1C1-ai-review.yaml
  source_selector: existing_annotations[8].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0016263\n  label: N-acetylgalactosaminide\
    \ beta-1,3-galactosyltransferase activity\nevidence_type: IMP\noriginal_reference_id:\
    \ PMID:37216524\nnegated: true"
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
- **Gene directory:** C1GALT1C1
- **Gene symbol:** C1GALT1C1
- **UniProt accession:** Q96EU7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016263
- **Source file:** genes/human/C1GALT1C1/C1GALT1C1-ai-review.yaml
- **Source selector:** existing_annotations[8].function_hypothesis

## Seed Hypothesis

C1GALT1C1 does not have N-acetylgalactosaminide beta-1,3-galactosyltransferase activity (GO:0016263).

## Term and Decision Context

- Term: N-acetylgalactosaminide beta-1,3-galactosyltransferase activity (GO:0016263)
- Evidence type: IMP
- Original reference: PMID:37216524
- Existing annotation is negated: true

## Reference Context

- PMID:37216524

## Source Context YAML

```yaml
term:
  id: GO:0016263
  label: N-acetylgalactosaminide beta-1,3-galactosyltransferase activity
evidence_type: IMP
original_reference_id: PMID:37216524
negated: true
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

# C1GALT1C1 (COSMC) — Function-Assignment Hypothesis Report

**Gene:** C1GALT1C1 (COSMC) · **UniProt:** Q96EU7 · **Organism:** Homo sapiens (NCBITaxon:9606)
**Term under review:** GO:0016263 — N-acetylgalactosaminide beta-1,3-galactosyltransferase activity (MF)
**Existing annotation:** IMP, PMID:37216524, **negated = true**
**Seed hypothesis:** *C1GALT1C1 does not have N-acetylgalactosaminide beta-1,3-galactosyltransferase activity (GO:0016263).*

---

## Executive Judgment

**Verdict: SUPPORTED (high confidence).** C1GALT1C1 encodes **Cosmc**, a **private ER molecular
chaperone** that is required for the folding/stability of the core 1 β3-galactosyltransferase
(**C1GALT1 / T-synthase**, UniProt Q9NS00). The catalytic activity GO:0016263 (synthesis of
Galβ1-3GalNAc-α-Ser/Thr, the T antigen) belongs to **C1GALT1, the client enzyme — not to
C1GALT1C1**. Multiple lines of primary evidence, and an explicit UniProt CAUTION, show that
C1GALT1C1 **has no transferase activity**. The negated annotation is therefore **justified and should
be retained**.

Key caveat on evidence code: the annotation uses **IMP** with negation. The mutant phenotype in the
reference (PMID:37216524) shows *loss of T-synthase (C1GALT1) activity* when Cosmc is defective. That
result demonstrates Cosmc's **chaperone requirement** for the reaction; it does not show Cosmc itself
catalyzes it. IMP is defensible for a NOT-annotation here, but the *positive* function of this gene is
chaperone activity, and that is what should carry the informative MF term.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| **UniProt Q96EU7** (CAUTION) | Database/curation | Supports | Does C1GALT1C1 have GT activity? | "Was originally assigned to be a glycosyltransferase. However, it was later shown that it has **no transferase activity and rather acts as a chaperone**." KW=Chaperone (no Transferase). | Human, reviewed entry | High; database-level, but cites primary work |
| **Ju & Cummings 2002, PMID:12464682** | Direct assay / mutant complementation | Supports | Is the transferase activity intrinsic to Cosmc? | Cosmc restores C1β3Gal-T activity in Cosmc-deficient Jurkat & insect cells; C1GALT1 gene/mRNA is normal in those cells; Cosmc "acts as a specific molecular chaperone in assisting the folding/stability of C1β3Gal-T." The transferase is a **separate gene product**. | Human Jurkat, Hi-5 insect cells | High; foundational functional study |
| **Aryal, Ju & Cummings 2010, PMID:19923218** | Direct in vitro assay | Supports | Does Cosmc perform folding vs catalysis? | Cosmc directly refolds denatured T-synthase in vitro (ATP-independent, substrate-specific); "**first ER chaperone required for folding of a glycosyltransferase**." Tn-syndrome Cosmc mutant has reduced chaperone function. | Recombinant proteins in vitro | High; isolates chaperone activity |
| **Aryal, Ju & Cummings 2014, PMID:24616093** | Interaction / mechanism | Supports | Mechanism of Cosmc–client recognition | Cosmc recognizes a specific stem-region motif (CBRT) in T-synthase; grafting CBRT onto β4GalT1 confers Cosmc binding — a chaperone recognition system, not catalysis. | Human proteins, in vitro | High |
| **Erger et al. 2023, PMID:37216524** (the IMP reference) | Mutant phenotype (germline) | Supports | What does a germline C1GALT1C1 variant cause? | Titled "**Germline C1GALT1C1 mutation causes a multisystem chaperonopathy**"; A20D-Cosmc reduces **C1GALT1 (T-synthase) activity** and impairs O-glycosylation → aHUS-like disease. Loss of chaperone function, not loss of intrinsic transferase activity. | Human patients (2 half-brothers) | High; defines role as chaperone |
| **Crew et al. 2008, PMID:18537974** | Mutant phenotype (human) | Supports/qualifies | Consequence of inactivating C1GALT1C1 variants | Inactivating variants (E152K, S193P, M1I) produce Tn phenotype via **T-synthase deficiency** — i.e., Cosmc loss disables the transferase, consistent with a chaperone role. | Human erythroblasts | High |
| **This report — pairwise alignment** | Computational (evolutionary) | Qualifies | Why was GT activity ever attributed? | COSMC (318 aa) vs C1GALT1 (363 aa) ≈ **33% identity**; both in GT31 (β3-Gal-T subfamily). Explains original name "C1Gal-T2" and the GT misannotation (PubMed:12361956). | Sequences Q96EU7 / Q9NS00 | Medium; coarse NW alignment, but consistent with UniProt family assignment |
| **QuickGO API** (this report) | Database provenance | Supports | Where does GO:0016263 actually sit? | **C1GALT1C1/Q96EU7:** single GO:0016263 = **NOT\|enables**, IMP, PMID:37216524 (the annotation under review). **C1GALT1/Q9NS00:** GO:0016263 = positive *enables* via **IDA (PMID:11677243)** + IBA + IEA. | EBI QuickGO, human | High; confirms term is experimentally grounded on the paralog, negated on the chaperone |
| **Ju et al. 2002, PMID:11677243** | Direct assay (IDA source) | Supports | Which gene product is the enzyme? | "Cloning and expression of human core 1 β1,3-galactosyltransferase" — establishes C1GALT1 as the GO:0016263 catalyst. | Human, recombinant enzyme | High |

---

## GO Curation Implications (leads — require curator verification)

- **Retain the negated GO:0016263 (MF) on C1GALT1C1.** The evidence robustly supports that this gene
  product lacks N-acetylgalactosaminide β-1,3-galactosyltransferase activity. The negation prevents
  paralog carry-over of the T-synthase activity onto its chaperone.
- **Positive MF that IS supported:** chaperone activity — candidate terms **GO:0051082 (unfolded
  protein binding)** and/or **GO:0044183 / GO:0140662-type** chaperone terms; most specifically the
  role assisting C1GALT1 folding. Direct evidence: PMID:19923218, PMID:12464682. Avoid "protein
  binding" as the final term — "unfolded protein binding / chaperone" is more informative.
- **Supported BP:** protein folding (GO:0006457) and **O-glycan / T-antigen biosynthesis via enabling
  C1GALT1** (e.g., GO:0016266 O-glycan processing) as an *involved-in / contributes-to* relationship,
  not as a direct catalytic step.
- **Supported CC:** endoplasmic reticulum membrane; single-pass type II membrane protein (GO:0005789).
- **Evidence-code note (lead):** consider whether the NOT-GO:0016263 is better supported as **IC/ND**
  or kept as **IMP**; the mutant data are about the *client's* activity, so IMP for a NOT-MF is
  acceptable but worth a curator note.

---

## GO Decision Table (lead — curator to verify)

| GO term | Aspect | Gene | Current / proposed | Recommended action | Evidence |
|---|---|---|---|---|---|
| GO:0016263 N-acetylgalactosaminide β-1,3-galactosyltransferase activity | MF | **C1GALT1C1** | NOT\|enables, IMP, PMID:37216524 | **RETAIN negation** | No intrinsic transferase activity; UniProt CAUTION; PMID:12464682/19923218 |
| GO:0016263 (same) | MF | C1GALT1 (paralog Q9NS00) | enables, IDA PMID:11677243 (+IBA/IEA) | Keep (belongs here) — reference point | Direct assay of the actual enzyme |
| GO:0051082 unfolded protein binding | MF | C1GALT1C1 | (candidate to add/confirm) | **ADD / confirm** as informative positive MF | PMID:19923218, PMID:12464682, PMID:24616093 |
| GO:0006457 protein folding | BP | C1GALT1C1 | (candidate) | ADD/confirm — direct chaperone role | PMID:19923218 |
| GO:0016266 O-glycan processing (or 'contributes to' C1GALT1 activity) | BP | C1GALT1C1 | (candidate) | ADD as *involved-in/contributes-to*, not direct catalysis | PMID:37216524, PMID:24643043 |
| GO:0005789 endoplasmic reticulum membrane | CC | C1GALT1C1 | (candidate) | Confirm; single-pass type II membrane | UniProt Q96EU7 |

**Bottom line:** retain the negated GO:0016263 on C1GALT1C1; the gene's informative *positive* molecular function is chaperone / unfolded-protein binding, not any transferase term.

---

## Mechanistic Scope

- **Immediate molecular function of C1GALT1C1:** ATP-independent, client-specific **molecular chaperone**
  in the ER that binds a stem-region motif (CBRT) of C1GALT1 and promotes its folding/stability,
  preventing proteasomal degradation.
- **Not the gene product's activity:** the galactosyl transfer reaction itself (Galβ1-3GalNAc-Ser/Thr
  synthesis) — that is enzymatically executed by **C1GALT1**.
- **Downstream / indirect (not to be conflated with MF):** T-antigen formation, extended O-glycan
  biosynthesis, Tn/STn antigen exposure on Cosmc loss, and disease phenotypes (Tn polyagglutination
  syndrome, aHUS-like chaperonopathy). These arise from *loss of chaperone function*, not from loss of
  an intrinsic transferase.

---

## Conflicts and Alternatives

- **Historical database carry-over (resolved):** the original 2002 report (PubMed:12361956) named the
  protein "Core 1 β1,3-galactosyltransferase 2 (C1GalT2)" based on GT31 paralogy (~33% identity to
  C1GALT1). This is the source of any residual GT annotation; it was explicitly refuted (UniProt CAUTION;
  PMID:12464682). No credible primary evidence supports intrinsic transferase activity.
- **Paralog confusion (the main risk):** C1GALT1 (Q9NS00) is the true GO:0016263 enzyme. Annotation
  pipelines keyed on GT31 family membership could re-propagate the term; the explicit negation guards
  against this.
- **No organism-specific or isoform-specific evidence** contradicts the chaperone-only interpretation;
  the chaperone role is conserved across vertebrates (client-specificity data, PMID:24616093).

---

## Knowledge Gaps

1. **Formal enzymatic exclusion assay.** Checked: no primary paper reports a direct in vitro assay of
   purified Cosmc acting as a galactosyltransferase; activity has only ever been observed via C1GALT1.
   Matters because the negation rests on *absence of evidence + mechanistic understanding*. Resolved by
   an in vitro UDP-Gal → GalNAcα-O-phenyl assay with purified Cosmc alone (expected: no activity).
2. **Structural confirmation of a degenerate catalytic site.** Checked: UniProt lists GT31 similarity
   but no experimental structure with catalytic-residue analysis surfaced in searches. A structure/model
   confirming loss of the catalytic/acceptor-binding residues would strengthen the mechanistic basis.
3. **Evidence-code appropriateness for the NOT annotation.** Whether IMP vs IC/ND best fits a negative
   MF; a curator judgment, not an experimental gap.

---

## Discriminating Tests

- **Direct transferase assay of purified Cosmc** (UDP-[3H]Gal donor, GalNAcα-O-phenyl acceptor) with
  C1GALT1 as positive control — cleanly separates "no intrinsic activity" from "chaperone only."
- **Reciprocal reconstitution:** active T-synthase produced only when Cosmc is co-expressed in
  Cosmc-null (insect) cells — already shown (PMID:12464682); a targeted re-run isolates the chaperone
  dependency.
- **Structure/AlphaFold catalytic-residue mapping:** compare Cosmc vs C1GALT1 active-site and
  donor-binding residues to show catalytic degeneration.

---

## Curation Leads (verify before applying)

- **Action:** *Keep* negated GO:0016263 (MF) on C1GALT1C1. **Do not** add any positive galactosyltransferase term.
- **Add positive MF:** unfolded protein binding / chaperone activity (e.g., GO:0051082) — refs PMID:19923218, PMID:12464682.
- **Add/confirm BP:** protein folding (GO:0006457); contributes-to O-glycan biosynthesis (via C1GALT1).
- **Add/confirm CC:** endoplasmic reticulum membrane (GO:0005789), integral/single-pass type II.
- **Candidate references w/ exact snippets to verify:**
  - PMID:12464682 — "Cosmc acts as a specific molecular chaperone in assisting the folding/stability of C1β3Gal-T."
  - PMID:19923218 — "Cosmc represents the first ER chaperone identified to be required for folding of a glycosyltransferase."
  - PMID:37216524 — title "Germline C1GALT1C1 mutation causes a multisystem chaperonopathy."
  - UniProt Q96EU7 CAUTION — "…it has no transferase activity and rather acts as a chaperone."
- **Suggested curator question:** Is IMP the preferred evidence code for this NOT-MF, or should IC/ND be used given the phenotype reflects the client enzyme's activity?
- **Suggested experiment:** direct in vitro transferase assay of purified Cosmc (expected negative).

---

## Provenance

- Literature via PubMed (PMIDs above); entry data via UniProt Q96EU7 (.txt) and Q9NS00 (.fasta).
- Computed pairwise global alignment COSMC vs C1GALT1: **~33% identity** (318 vs 363 aa), GT31 paralogs
  — executed in this run (Needleman–Wunsch over fetched UniProt sequences).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)