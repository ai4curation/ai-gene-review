---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T09:58:40.570491'
end_time: '2026-09-12T10:23:28.914369'
duration_seconds: 1488.34
template_file: /Users/cjm/orca/workspaces/ai-gene-review/arath-test/tmp/openscientist-arath-20260912/5-DRB1-template.md
template_variables:
  organism: ARATH
  gene: DRB1
  gene_symbol: DRB1
  uniprot_accession: O04492
  taxon_id: NCBITaxon:3702
  taxon_label: Arabidopsis thaliana
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004525
  hypothesis_text: DRB1 has ribonuclease III activity (GO:0004525).
  term_context: '- Term: ribonuclease III activity (GO:0004525)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - PMID:18632569'
  source_file: genes/ARATH/DRB1/DRB1-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004525\n  label: ribonuclease III activity\n\
    evidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
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
citation_count: 6
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

- **Organism code:** ARATH
- **Taxon:** Arabidopsis thaliana (NCBITaxon:3702)
- **Gene directory:** DRB1
- **Gene symbol:** DRB1
- **UniProt accession:** O04492

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004525
- **Source file:** genes/ARATH/DRB1/DRB1-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

DRB1 has ribonuclease III activity (GO:0004525).

## Term and Decision Context

- Term: ribonuclease III activity (GO:0004525)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- PMID:18632569

## Source Context YAML

```yaml
term:
  id: GO:0004525
  label: ribonuclease III activity
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

## Specific adjudication question

Adjudicate whether DRB1/HYL1 itself catalyzes RNase III cleavage or instead binds substrate and promotes cleavage by DCL1. Compare target sequence/domain/structure to experimentally characterized catalytic RNase III proteins and dsRNA-binding cofactors. Trace the relevant PAINT/IBA ancestral assertion if public data permit; donor count is not evidence strength. Distinguish intrinsic catalysis, complex contribution and activation, and identify the decisive published biochemical assay. Use primary evidence and independently reproducible analyses. Do not consult ai-gene-review repository reviews, generated reports or local bioinformatics results; these are held out. Verify the exact Arabidopsis protein and distinguish paralogs, mutants, tissue and assay context. Give evidence for and against the assignment, the narrowest defensible function, and what observation would change the verdict. Missing evidence is not refutation. Do not infer catalytic or regulatory function from interaction, docking or shared fold alone.


## Output

# Adjudication Report: DRB1/HYL1 (O04492) — ribonuclease III activity (GO:0004525)

**Gene:** DRB1 / HYL1 (HYPONASTIC LEAVES 1), *Arabidopsis thaliana* (UniProt O04492)
**Hypothesis under review:** "DRB1 has ribonuclease III activity (GO:0004525)."
**Existing annotation:** GO:0004525, evidence IBA, GO_REF:0000033 (PANTHER/PAINT). Reference context PMID:18632569.
**Focus type:** function_assignment — does the gene product directly have the stated function?

---

## Summary

**Verdict: REFUTED / OVER-ANNOTATED.** DRB1/HYL1 does **not** intrinsically catalyze RNase III cleavage. It is a double-stranded RNA-binding cofactor of the plant microprocessor that binds pri-/pre-miRNA substrate and **promotes cleavage by DCL1**, the true RNase III enzyme. The GO:0004525 IBA annotation is a phylogenetic over-propagation (PAINT) inherited through a shared dsRNA-binding module, not through any catalytic domain, and it should be removed or down-graded on HYL1.

Two independent, mutually reinforcing lines of evidence drive this conclusion. First, **domain architecture is decisive and reproducible**: HYL1 (419 aa) contains only two double-stranded RNA-binding domains (DRBM/DSRM; Pfam PF00035) and completely lacks the RNase III catalytic domain (Pfam PF00636/PF14622), a PAZ domain, a helicase domain, and the conserved acidic active-site residues that coordinate the catalytic metal ions. RNase III chemistry mechanistically requires that catalytic domain; HYL1 does not have it, so intrinsic cleavage is architecturally impossible. Second, the **decisive biochemistry** — from the very reference cited by the annotation context (PMID:18632569) — shows that with purified recombinant proteins, DCL1 alone releases 21-nt products from dsRNA and miR167b precursors, whereas HYL1 (with SERRATE) only accelerates the rate and improves the accuracy of DCL1 cleavage. HYL1 is never observed to cleave on its own.

The mechanism of the erroneous annotation is a classic **PAINT/IBA over-propagation**. PANTHER family PTHR11207 ("RIBONUCLEASE III") contains both a catalytic subfamily (SF0, "Ribonuclease 3", bearing the RNase III catalytic domain — e.g., *E. coli* RNase III and human DROSHA) and a non-catalytic dsRNA-binding subfamily (SF1, "Double-stranded RNA-binding protein 1"), to which HYL1 belongs. The catalytic MF term was correctly asserted for the catalytic members and then propagated by ancestral inference across the whole family, incorrectly reaching the DRBM-only SF1 subfamily. Donor count is not evidence strength here: all the catalytic "with" donors resemble HYL1 only through the shared, non-catalytic dsRNA-binding fold. The narrowest defensible molecular function for HYL1 is **double-stranded RNA binding (GO:0003725)**, which is IDA-supported, with a contributory (non-catalytic) role in the biological process of miRNA processing. Per the guidance that "missing evidence is not refutation," the refutation here is positive rather than merely absent: the catalytic domain is demonstrably absent, and the in vitro reconstitution positively localizes catalysis to DCL1.

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED.**

Reasoning, in order of decisiveness:

1. **Domain architecture (direct, reproducible):** HYL1 (419 aa) contains only two dsRNA-binding domains (DRBM; Pfam PF00035) and no RNase III catalytic domain (Pfam PF00636 / PF14622), no PAZ, no helicase, no catalytic acidic-residue cluster. RNase III catalysis mechanistically requires the RIBOc catalytic domain; HYL1 lacks it entirely.
2. **Decisive biochemistry (PMID:18632569 — the reference cited by the annotation itself):** With purified recombinant proteins, DCL1 alone releases 21-nt products from dsRNA and miR167b precursors; recombinant HYL1 (with SE) only accelerates the rate and improves accuracy of DCL1 cleavage. HYL1 is never shown to cleave.
3. **IBA source (PAINT):** The "with" donors for the GO:0004525 IBA are genuine catalytic RNase III enzymes (*E. coli* RNase III P0A7Y0, human DROSHA Q9NRR4, Dicers). Each carries the RNase III catalytic domain; HYL1 shares with them only the non-catalytic DRBM.

**Most important caveat:** the narrowest defensible molecular function for HYL1 is double-stranded RNA binding (GO:0003725), which is IDA-supported. The only observation that would overturn the verdict is a reproducible demonstration that purified HYL1 alone cleaves dsRNA in a metal-dependent manner — biochemically implausible given the demonstrable absence of the catalytic domain.

---

## Key Findings

### Finding 1 — HYL1 lacks the RNase III catalytic domain and possesses only dsRNA-binding domains

UniProt O04492 describes a 419-residue protein with the domain architecture DRBM 1 (residues 15–84) and DRBM 2 (residues 101–170), corresponding to Pfam PF00035 (dsrm, double-stranded RNA-binding motif). There is **no RNase III catalytic domain** (Pfam PF00636 "Ribonuclease_3" or PF14622), **no PAZ domain**, **no helicase domain**, and none of the conserved acidic active-site residues that coordinate the two catalytic metal ions required for phosphodiester-bond hydrolysis by RNase III enzymes.

This is decisive because catalysis is a property of the RNase III catalytic domain, not of the dsRNA-binding module. The catalytic RNase III proteins that serve as the IBA "with" donors all carry that catalytic domain: *E. coli* RNase III (P0A7Y0, PF14622); human DROSHA (Q9NRR4, PF00636 + PF14622); and *Arabidopsis* DCL1 (Q9SP32), which contains two RNase III domains (residues 1342–1518 and 1559–1707) plus a PAZ domain and a helicase domain. HYL1 shares with all of these enzymes **only** the PF00035 dsRNA-binding module — i.e., the non-catalytic accessory part. The catalytic assignment is therefore architecturally impossible for HYL1.

### Finding 2 — The decisive biochemical assay shows DCL1 catalyzes cleavage; HYL1 only accelerates and improves accuracy

The most direct and decisive evidence comes from in vitro reconstitution with purified recombinant proteins. Dong, Han & Fedoroff (2008) (PMID:18632569) developed an in vitro miRNA-processing assay and reported that "DCL1 alone releases 21-nt short RNAs from dsRNA as well as synthetic miR167b precursor RNAs," and that "recombinant HYL1 and SE proteins accelerate the rate of DCL1-mediated cleavage of pre- and pri-miR167b substrates and promote accurate processing." In other words, cleavage occurs with DCL1 alone; HYL1's contribution is kinetic and fidelity-enhancing, not catalytic. This is the annotation's own cited reference, and it supports HYL1 as a cofactor, not as the catalyst.

This is corroborated by Kurihara & Watanabe (2004) (PMID:15314213), who provided direct evidence using *dcl1* mutants that "Dicer-like 1 (DCL1) catalyzes at least the first and second cleavage steps and that double-stranded RNA-binding domains of DCL1 are involved in positioning of the cleavage sites." Across the literature, HYL1 is consistently described as a double-stranded RNA-binding protein "crucial for efficient and accurate processing" (PMID:32636270) — never as the catalytic nuclease. The catalytic activity is unambiguously attributed to DCL1.

### Finding 3 — IBA over-propagation traced: HYL1 is PANTHER PTHR11207 subfamily SF1 (dsRNA-binding), not catalytic SF0

PANTHER cross-references (via UniProt) place HYL1/DRB1 (O04492) in family **PTHR11207** ("RIBONUCLEASE III") but specifically in subfamily **PTHR11207:SF1 = "Double-stranded RNA-binding protein 1"** — a subfamily defined by two DRBM domains only, with no catalytic domain. The IBA "with" donor catalytic enzymes — *E. coli* RNase III (P0A7Y0) and human DROSHA (Q9NRR4) — belong to subfamily **PTHR11207:SF0 = "Ribonuclease 3"**, which carries the RNase III catalytic domain.

The GO:0004525 term was legitimately asserted for the catalytic SF0 members and then PAINT-propagated across the entire PTHR11207 family down to the non-catalytic SF1 subfamily, which is where the erroneous HYL1 annotation arises. This illustrates why donor count is not evidence strength: the ancestral assertion is valid at the family root only because of the catalytic subfamily, and its propagation to a dsRNA-binding-only subfamily is a false positive. Notably, HYL1's actual catalytic partner DCL1 is **not** even in PTHR11207 — it is in the Dicer-related family **PTHR14950** — underscoring that shared family membership between HYL1 and true RNase III enzymes reflects only the dsRNA-binding module, not catalytic identity.

### Finding 4 — Family-wide pattern: Arabidopsis DRB paralogs are all DRBM-only, none catalytic

A domain check of the *Arabidopsis* DRB (double-stranded RNA-binding) protein family shows a consistent architecture: DRB1/HYL1 (O04492, 419 aa), DRB2 (Q9SKN2, 434 aa), and DRB5 (Q8GY79, 393 aa) each contain **only two DRBM domains** (Pfam PF00035) and lack any RNase III catalytic domain (PF00636/PF14622). None are enzymes; all function as dsRNA-binding cofactors that partner with Dicer-like nucleases. This family-wide pattern reinforces that RNase III catalytic activity is architecturally impossible for the DRB family and that the GO:0004525 assignment to any DRB member reflects annotation carry-over rather than biology.

---

## Mechanistic Model / Interpretation

The plant microprocessor that produces miRNAs comprises DCL1 (the catalytic RNase III/Dicer-like enzyme), HYL1 (a dsRNA-binding cofactor), and SERRATE (a zinc-finger cofactor). The division of labor is clear:

```
   pri-miRNA (dsRNA stem-loop substrate)
            │
            │  HYL1 binds dsRNA substrate (via 2× DRBM / PF00035)
            │  SE (zinc-finger) assists complex assembly
            ▼
   ┌─────────────────────────────────────────────┐
   │  DCL1  =  CATALYST (RNase III activity)      │
   │  • 2× RNase III catalytic domains (PF00636)  │
   │  • PAZ domain, helicase domain               │
   │  • active-site acidic residues + Mg2+        │
   │  → hydrolyzes phosphodiester bonds           │
   └─────────────────────────────────────────────┘
            │
            │  HYL1 + SE accelerate rate & improve accuracy
            ▼
   miRNA/miRNA* duplex (~21 nt)
```

- **Intrinsic catalysis:** DCL1 only. Demonstrated by DCL1-alone cleavage in vitro (PMID:18632569) and by *dcl1* mutant analysis (PMID:15314213).
- **Complex contribution / activation:** HYL1 (and SE) accelerate the DCL1 reaction rate and enforce accurate cleavage-site selection, but neither is a nuclease.
- **HYL1's direct molecular function:** double-stranded RNA binding (GO:0003725), mediated by its two DRBM domains.

The correct GO representation separates these roles. The molecular function RNase III activity (GO:0004525) belongs to DCL1. HYL1's molecular function is dsRNA binding (GO:0003725). Both proteins participate in the biological process of miRNA/pri-miRNA processing, but process participation does not confer the catalytic molecular function. The GO true-path and MF/BP distinction is precisely what the IBA over-propagation violated.

| Protein | UniProt | Length | RNase III catalytic domain (PF00636/PF14622) | dsRNA-binding domain (PF00035) | PAZ/Helicase | Catalyzes cleavage? |
|---|---|---|---|---|---|---|
| DRB1/HYL1 | O04492 | 419 aa | **Absent** | 2× DRBM | Absent | **No** (cofactor) |
| DRB2 | Q9SKN2 | 434 aa | Absent | 2× DRBM | Absent | No (cofactor) |
| DRB5 | Q8GY79 | 393 aa | Absent | 2× DRBM | Absent | No (cofactor) |
| DCL1 | Q9SP32 | ~1910 aa | **Present (2×)** | present | Present | **Yes** |
| DROSHA (human) | Q9NRR4 | — | **Present** | present | — | Yes |
| RNase III (*E. coli*) | P0A7Y0 | — | **Present** | present | — | Yes |

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt O04492 (this run) | Structural/evolutionary (domain) | **Refutes** | HYL1 has an RNase III catalytic domain | Only DRBM×2 (PF00035); **no** RNase III (PF00636/PF14622), PAZ or helicase | *A. thaliana* protein, 419 aa | High; sequence-annotation based |
| UniProt Q9SP32 / [PMID:15314213](https://pubmed.ncbi.nlm.nih.gov/15314213/) | Structural + mutant/assay | Qualifies (localizes catalysis) | Which protein is the nuclease | **DCL1** carries two RNase III domains and "catalyzes at least the first and second cleavage steps"; its DRBMs position cleavage sites | *A. thaliana*, miR163 in *dcl1* mutants | High |
| **[PMID:18632569](https://pubmed.ncbi.nlm.nih.gov/18632569/)** (Dong, Han, Fedoroff 2008) | Direct assay (in vitro reconstitution) | **Refutes intrinsic catalysis** | Does HYL1 cleave, or only assist DCL1? | "DCL1 **alone** releases 21-nt short RNAs…"; "HYL1 and SE proteins **accelerate the rate** of DCL1-mediated cleavage and **promote accurate processing**" | Purified recombinant proteins, miR167b substrates | High; this is the annotation's own reference and it supports cofactor, not catalyst |
| [PMID:32636270](https://pubmed.ncbi.nlm.nih.gov/32636270/) (Gao et al. 2020) | Mutant/mechanistic | Competing (alternative role) | Additional HYL1 function | HYL1 protects pri-miRNAs from nuclear exosome — a **binding/protective**, non-catalytic role | *A. thaliana* D-bodies | Medium; reinforces non-catalytic function |
| [PMID:34196710](https://pubmed.ncbi.nlm.nih.gov/34196710/) | Structural/evolutionary (ancestral reconstruction) | Qualifies | HYL1 function and DCL1 partnership | HYL1 evolved high affinity for dsRNA and for DCL1; DSRM2 mediates DCL1 interaction | Land-plant evolution, in vitro + Arabidopsis | Medium; reinforces cofactor/binding role, not catalysis |
| QuickGO donors P0A7Y0, Q9NRR4, Dicers (this run) | Computational (IBA provenance) | Explains over-annotation | Origin of GO:0004525 IBA | All donors have the RNase III catalytic domain; HYL1 shares only DRBM → propagation error | Cross-species PANTHER family PTHR11207 | High |
| PANTHER PTHR11207 family trace (this run) | Computational (phylogeny) | Explains over-annotation | Why HYL1 inherited RNase III activity | HYL1 = **PTHR11207:SF1 "dsRNA-binding protein 1"** (DRBM-only); catalytic donors *E. coli* RNC & DROSHA = **PTHR11207:SF0 "Ribonuclease 3"**. DCL1 is not even in this family (PTHR14950) | Cross-species PANTHER | High; reproducible via UniProt PANTHER xrefs |
| [PMID:40957739](https://pubmed.ncbi.nlm.nih.gov/40957739/) (2025 review) | Review/structural | Orientation | Complex architecture | DCL1–HYL1–SE complex; HYL1 is an accessory dsRNA-binding factor | Plant microprocessor | Review-level orientation only |

---

## GO Curation Implications

**Lead (requires curator verification):**

- **Remove / do not propagate GO:0004525 (ribonuclease III activity, MF) on O04492.** The IBA is a PAINT over-propagation via the shared DRBM. HYL1 lacks the RNase III catalytic domain and no assay shows intrinsic cleavage. **Confirmed provenance:** HYL1 sits in PANTHER family **PTHR11207 ("Ribonuclease III") but in subfamily SF1 ("Double-stranded RNA-binding protein 1")**, whereas the catalytic IBA donors (*E. coli* RNase III P0A7Y0, human DROSHA Q9NRR4) are in the catalytic subfamily **SF0 ("Ribonuclease 3")**. The ancestral RNase III MF assertion should be restricted to catalytic-domain-bearing subfamilies and **not** propagated to the DRBM-only SF1 members — a candidate node/annotation-rule correction upstream.
- **Retain the correct, more informative MF: GO:0003725 (double-stranded RNA binding)** — IDA-supported and consistent with the DRBM×2 architecture. This is preferable to a vague "protein binding" recommendation.
- **BP:** miRNA processing/biogenesis (e.g., GO:0035196 production of miRNAs; or "pri-miRNA processing") is appropriate as a **non-catalytic contributory** role; annotate with "contributes_to" semantics rather than implying enzymatic activity.
- **CC:** nucleus / nuclear dicing (D-)body is supported.
- HYL1's role in the microprocessor is best captured as a molecular function of **dsRNA binding** plus BP involvement in miRNA processing — not as ribonuclease activity.

---

## Mechanistic Scope

- **Immediate molecular function tested:** metal-dependent endonucleolytic cleavage of double-stranded RNA (RNase III catalysis). HYL1 has no catalytic domain and does not perform this.
- **HYL1's actual direct activity:** sequence-independent binding of double-stranded/structured pri-/pre-miRNA via two DRBMs; recruitment/positioning within the DCL1–HYL1–SE complex; enhancement of cleavage rate and site accuracy (activation), and protection of pri-miRNA from exosomal degradation.
- **Downstream / not to be conflated with catalysis:** the pleiotropic *hyl1* phenotypes (hyponastic leaves, altered hormone response, development, skotomorphogenesis; PMID:31922639) are loss-of-function consequences of impaired miRNA production, not evidence of intrinsic nuclease activity.

---

## Conflicts and Alternatives

- **Paralog/partner confusion is the root cause.** The catalytic activity belongs to **DCL1** (Q9SP32), a bona fide Dicer/RNase III with two RNase III domains. The IBA lumps HYL1 into a family with catalytic RNase III enzymes (*E. coli* RNC, DROSHA, Dicers) through the shared DRBM. DCL1 is in a different PANTHER family (PTHR14950) from HYL1 (PTHR11207), confirming they are distinct protein classes.
- **Family-wide non-catalytic architecture (this run):** the Arabidopsis DRB paralogs are all DRBM-only and lack any RNase III catalytic domain — DRB1/HYL1 (O04492, 419 aa), DRB2 (Q9SKN2, 434 aa), DRB5 (Q8GY79, 393 aa) each have exactly two DRBMs (PF00035) and no PF00636/PF14622. RNase III catalysis is architecturally impossible across this dsRNA-binding cofactor family, so any RNase III activity propagated to DRB members is over-annotation.
- **No isoform rescue:** HYL1 alternative splicing affects the DRBM region/regulation, not acquisition of a catalytic domain.
- **No experimental artifact supports catalysis:** the one in vitro reconstitution designed to test this (PMID:18632569) explicitly shows DCL1, not HYL1, is the nuclease.
- **Alternative non-catalytic functions** (exosome protection, PMID:32636270; microprocessor-independent skotomorphogenesis role, PMID:31922639) further argue HYL1 is a multifunctional RNA/protein-binding factor, not an enzyme.
- **Shared fold ≠ shared function:** HYL1 shares the dsRNA-binding module (PF00035) with true RNase III enzymes, but this module is non-catalytic. Per the adjudication guidance, catalytic function must not be inferred from shared fold, interaction, or docking alone.

---

## Limitations and Knowledge Gaps

1. **Is there any report of HYL1 acting as a nuclease alone?** Checked: primary reconstitution (PMID:18632569) and mechanistic studies attribute cleavage to DCL1. Gap matters because a positive HYL1-alone cleavage assay would be the only thing that could support GO:0004525. Resolution: a purified-HYL1 dsRNA cleavage assay with Mg²⁺ (expected negative).
2. **Exact PAINT node annotation rationale.** Checked and largely resolved: HYL1 = PANTHER **PTHR11207:SF1** (dsRNA-binding protein subfamily); catalytic donors = **PTHR11207:SF0** (Ribonuclease 3). Propagation occurred through the family-level RNase III assertion despite SF1 lacking the catalytic domain. Remaining gap: the exact ancestral node ID and whether GO already carries a subfamily-level restriction. Resolution: inspect the PANTHER PTHR11207 tree/annotation rules.
3. **Programmatic domain verification:** The domain-architecture calls rest on UniProt/Pfam/PANTHER records rather than a de novo HMMER/InterProScan run in this session. The entire refutation hinges on the absence of a catalytic domain, so an independent PF00636/PF14622 scan of O04492 (expected: no hit) would fully close this.
4. **Explicit negative control quote:** PMID:18632569 shows DCL1-alone cleavage but I did not locate a dedicated "HYL1-alone, no cleavage" negative control statement. The framing strongly implies it; an explicit catalytically-dead HYL1 assay would be the cleanest negative. Missing evidence here does not weaken the conclusion — it is a strengthening opportunity.

---

## Proposed Follow-up Experiments / Actions (Discriminating Tests)

- **In vitro cleavage assay with purified recombinant HYL1 alone** on a labeled dsRNA/pri-miRNA ± Mg²⁺ — the decisive experiment; catalysis-positive would overturn the verdict (expected: no cleavage).
- **DCL1 RNase III active-site mutant + wild-type HYL1** reconstitution: predict loss of cleavage despite intact HYL1, localizing catalysis to DCL1.
- **HMMER/InterProScan of O04492** against Pfam RNase III models (PF00636, PF14622): expect no hit (consistent with the UniProt domain table used here).
- **Catalytic-residue mutagenesis is not applicable** (no RNase III catalytic residues exist to mutate) — itself confirmatory.
- **PAINT provenance pull:** Retrieve the PTHR11207 GO_REF:0000033 PAINT record to document the exact ancestral node and confirm HYL1's SF1 placement receives GO:0004525 by propagation.

---

## Curation Leads (require curator verification)

1. **Action change:** Change the review action for the existing RNase III activity annotation to **REMOVE / DO-NOT-PROPAGATE (over-annotation)** for GO:0004525 on O04492.
2. **Replacement MF term:** Retain/assert **GO:0003725 double-stranded RNA binding** (IDA) as the narrowest defensible molecular function.
3. **BP framing:** Keep involvement in miRNA processing/biogenesis as a **contributory, non-catalytic** role (contributes_to), not RNase activity.
4. **Candidate reference + exact snippet to verify (decisive):** PMID:18632569 — *"We find that DCL1 alone releases 21-nt short RNAs from dsRNA as well as synthetic miR167b precursor RNAs… recombinant HYL1 and SE proteins accelerate the rate of DCL1-mediated cleavage of pre- and pri-miR167b substrates and promote accurate processing."*
5. **Supporting reference + snippet:** PMID:15314213 — *"Dicer-like 1 (DCL1) catalyzes at least the first and second cleavage steps and… double-stranded RNA-binding domains of DCL1 are involved in positioning of the cleavage sites."*
6. **Suggested curator question:** Should the PANTHER PTHR11207 RNase III MF propagation be restricted to members bearing PF00636/PF14622, excluding DRBM-only proteins (HYL1 and other DRB family members)?
7. **Suggested experiment:** purified-HYL1-alone dsRNA cleavage assay (expected negative) to formally close the gap.

---

## Evidence Base (Key Literature)

- **[PMID:18632569](https://pubmed.ncbi.nlm.nih.gov/18632569/)** — *The RNA-binding proteins HYL1 and SE promote accurate in vitro processing of pri-miRNA by DCL1.* **Decisive.** DCL1 alone cleaves; HYL1/SE accelerate rate and confer accuracy. Separates catalysis (DCL1) from cofactor function (HYL1).
- **[PMID:15314213](https://pubmed.ncbi.nlm.nih.gov/15314213/)** — *Arabidopsis micro-RNA biogenesis through Dicer-like 1 protein functions.* Direct evidence via *dcl1* mutants that DCL1 catalyzes the cleavage steps and its dsRBDs position cleavage sites.
- **[PMID:32636270](https://pubmed.ncbi.nlm.nih.gov/32636270/)** — *Hyponastic Leaves 1 protects pri-miRNAs from nuclear exosome attack.* Describes HYL1 as a double-stranded RNA-binding protein crucial for efficient/accurate processing and reveals a non-canonical protective role — reinforcing binding, not catalysis.
- **[PMID:34196710](https://pubmed.ncbi.nlm.nih.gov/34196710/)** — *Direct Molecular Evidence for an Ancient, Conserved Developmental Toolkit…* Ancestral reconstruction shows HYL1 evolved high affinity for dsRNA and DCL1; DSRM2 mediates the HYL1–DCL1 interaction.
- **[PMID:40957739](https://pubmed.ncbi.nlm.nih.gov/40957739/)** — *Form follows function — structural interplay between DCL1 and pri-miRNAs.* Review framing the microprocessor as DCL1 (catalyst) + HYL1 + SE (cofactors), consistent with the division of labor.
- **[PMID:31922639](https://pubmed.ncbi.nlm.nih.gov/31922639/)** — *Dual function of HYPONASTIC LEAVES 1…* Shows HYL1 has microprocessor-independent roles via protein-protein interaction domains — again a binding/regulatory protein, not a nuclease.
- Database records: **UniProt O04492** (HYL1 architecture), **Q9SP32** (DCL1), **Q9NRR4** (DROSHA), **P0A7Y0** (*E. coli* RNase III), and **PANTHER PTHR11207** (family/subfamily provenance).

---

## Bottom Line

The seed hypothesis is **refuted** as stated. HYL1 binds substrate and activates cleavage by DCL1; it does not catalyze RNase III cleavage. The RNase III activity (GO:0004525) belongs to DCL1, and the IBA on HYL1 is an architecturally impossible, PAINT-over-propagated assignment from catalytic RNase III donors via a shared non-catalytic dsRNA-binding fold. The narrowest defensible molecular function is double-stranded RNA binding (GO:0003725), with a contributory, non-catalytic role in miRNA processing. The only observation that would change the verdict is a reproducible demonstration that purified HYL1 alone cleaves dsRNA in a metal-dependent manner — biochemically implausible given the absence of the catalytic domain.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)