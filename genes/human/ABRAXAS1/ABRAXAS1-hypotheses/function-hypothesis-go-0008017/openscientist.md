---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T18:11:10.190996'
end_time: '2026-07-06T18:19:51.723880'
duration_seconds: 521.53
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ABRAXAS1
  gene_symbol: ABRAXAS1
  uniprot_accession: Q6UWZ7
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008017
  hypothesis_text: ABRAXAS1 has microtubule binding (GO:0008017).
  term_context: '- Term: microtubule binding (GO:0008017)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - file:human/ABRAXAS1/ABRAXAS1-uniprot.txt

    - file:human/ABRAXAS1/ABRAXAS1-notes.md'
  source_file: genes/human/ABRAXAS1/ABRAXAS1-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008017\n  label: microtubule binding\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033"
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
- **Gene directory:** ABRAXAS1
- **Gene symbol:** ABRAXAS1
- **UniProt accession:** Q6UWZ7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008017
- **Source file:** genes/human/ABRAXAS1/ABRAXAS1-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis

ABRAXAS1 has microtubule binding (GO:0008017).

## Term and Decision Context

- Term: microtubule binding (GO:0008017)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- file:human/ABRAXAS1/ABRAXAS1-uniprot.txt
- file:human/ABRAXAS1/ABRAXAS1-notes.md

## Source Context YAML

```yaml
term:
  id: GO:0008017
  label: microtubule binding
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
prompt so the report can be compared against them after the run.

Do not rely on literature alone. Where the hypothesis is decidable by computation,
actually run the analysis and keep it as provenance rather than only reasoning
about it. Match the analysis to the question, for example:

- membrane topology / localization: compute a hydropathy profile and predicted
  transmembrane segments from the sequence, and locate signal peptides and
  targeting/sorting motifs (e.g. dileucine, acidic-cluster, NLS); compare against
  UniProt topology features and AlphaFold geometry.
- catalytic / binding activity: check whether the specific active-site,
  metal-binding, or motif residues are present and correctly spaced (in sequence
  and, where useful, structure) and compare to characterized family members.
- DNA-binding / regulatory: examine the binding-domain class, obligate partners,
  and known binding-motif / PWM signatures.
- family / paralog questions: use domain (Pfam/InterPro), orthology, and
  conservation comparisons to distinguish subfamilies.

Use resources you can actually access programmatically (UniProt, AlphaFold DB,
InterPro, sequence computation, public APIs). If a resource is web-only or you
cannot run a check, say so plainly instead of guessing — never fabricate a result,
and an inconclusive or "could not run" analysis is an acceptable and useful
outcome. Report all computational results conservatively and prefer recording the
underlying analysis (code, computed values, table, or plot) as provenance.

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

# ABRAXAS1 (Q6UWZ7) — Evaluation of "microtubule binding" (GO:0008017, IBA)

**Focus:** function-assignment hypothesis — *ABRAXAS1 directly has microtubule binding (GO:0008017)*
**Source:** `genes/human/ABRAXAS1/ABRAXAS1-ai-review.yaml` → `existing_annotations[2].function_hypothesis`
**Evidence type under review:** IBA (GO_REF:0000033, PAINT phylogenetic inference)

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED (paralog carry-over).**

The IBA "microtubule binding" annotation on ABRAXAS1 is not supported by any primary
experimental evidence for ABRAXAS1 itself. Programmatic provenance tracing shows the
term was propagated by PAINT from a shared PANTHER ancestral node
(**PTN001272083**) whose experimental support comes from the **paralog ABRAXAS2
(ABRO1 / FAM175B, UniProt Q15018)** — the scaffold of the cytoplasmic BRISC complex,
which genuinely localizes to the spindle pole and has direct (IDA/IMP) microtubule and
spindle annotations. ABRAXAS1, by contrast, is an **exclusively nuclear** scaffold of the
BRCA1-A complex whose experimentally supported molecular function is
**polyubiquitin-modification-dependent protein binding (GO:0031593, IDA)**.

Two co-propagated terms from the *same* node/source — GO:0008608 (spindle-microtubule
attachment to kinetochore) and GO:0090307 (mitotic spindle assembly) — are part of the
same over-annotation cluster and share the fate of GO:0008017.

**Most important caveat:** This is a decision about *direct annotation carry-over*, not a
claim that ABRAXAS1 has zero mitotic role. ABRAXAS1 does participate in mitotic G2/M **DNA
damage checkpoint signalling** (properly annotated IMP/NAS), but that is checkpoint
regulation, not physical microtubule binding, and does not rescue GO:0008017.

---

## Evidence Matrix

| # | Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|------------------|--------------|-------------|---------|--------------------------|
| 1 | QuickGO provenance (GO_REF:0000033) | computational / database | **Refutes (as direct)** | Is GO:0008017 experimental for ABRAXAS1? | GO:0008017 on Q6UWZ7 is **IBA**, assignedBy GO_Central, `withFrom` = PANTHER **PTN001272083** + **UniProtKB:Q15018** | GO annotation record | High; definitively an inferred, not experimental, term |
| 2 | UniProt Q15018 (ABRAXAS2/ABRO1) | direct assay + localization | **Competing source** | Which protein actually binds microtubules? | ABRAXAS2 has GO:0008017 **IDA**, GO:0008608 **IMP**, GO:0090307 **IMP**; localizes to **spindle pole / cytoskeleton** | Human, BRISC complex | High; ABRAXAS2 is the true experimental source of the propagated cluster |
| 3 | Computed NW alignment (this run) | structural / evolutionary | **Qualifies** | Are ABRAXAS1 & ABRAXAS2 paralogs sharing a PANTHER family? | Global identity ~**40.8%** (shorter-seq) / ~45.4% (aligned core); both = MPN domain (7–160) + coiled-coil scaffold | Sequence computation | High; explains why IBA co-clusters them |
| 4 | UniProt Q6UWZ7 features/comments | database + localization | **Refutes** | What is ABRAXAS1's function/location? | Function = BRCA1-A scaffold recognizing K63-Ub histones; **Loc: Nucleus only**; MF IDA = GO:0031593 (polyUb-dependent binding) | Human | High |
| 5 | PMID **31253574** (Rabl et al., 2019, *Mol Cell*) | structural / review-level synthesis | **Refutes** | Are ABRAXAS & ABRO1 distinct scaffolds? | "…BRCC36 subunit that is functionalized by scaffold subunits **ABRAXAS and ABRO1, respectively**" — nuclear BRCA1-A vs cytoplasmic BRISC | Human, cryo-EM/biochem | High; clarifies paralog division of labour |
| 6 | PMID **28009280** (Kyrieleis et al., 2016) | structural | **Refutes** | Where does ABRAXAS1 act? | Recruited to **damaged chromatin**; cleaves K63-Ub on histones H2A/H2AX | Human, negative-stain EM | High; nuclear/chromatin, not spindle |
| 7 | PMIDs 17525340, 19261746, 19261748, 19261749 | direct assay (IDA) | **Refutes (context)** | ABRAXAS1's real MF/CC | Foundational BRCA1-A papers; basis for GO:0070531 (IDA nucleus) and GO:0031593 (IDA polyUb binding) | Human cells | High |
| 8 | PMID 34272385 / 37198153 / 31630195 | mutant phenotype / patient cells | **Qualifies** | ABRAXAS1 loss-of-function phenotypes | Genome-stability/HR pathway-choice, BRCA1 mislocalization, breast-cancer predisposition — all **nuclear DNA-repair** | Human patient cells | High; no spindle phenotype reported |

---

## GO Curation Implications

**Lead (requires curator verification):**

- **GO:0008017 microtubule binding (MF, IBA) → REMOVE / do not accept for ABRAXAS1.**
  It is an IBA carry-over whose only experimental support lies in the paralog ABRAXAS2
  (Q15018). No ABRAXAS1-specific experimental evidence exists.
- **Co-propagated from the same node/source — treat identically:**
  - GO:0008608 attachment of spindle microtubules to kinetochore (BP, IBA) → remove/flag.
  - GO:0090307 mitotic spindle assembly (BP, IBA) → remove/flag.
- **Retain the informative, experimentally grounded MF:** **GO:0031593
  polyubiquitin modification-dependent protein binding (IDA)** — this is the
  appropriate, more-specific molecular function and should be the annotation curators
  keep. (Do **not** fall back to bare "protein binding".)
- **Retain CC:** GO:0070531 BRCA1-A complex (IDA), GO:0005634 nucleus (IDA).

This is an MF-term removal driven by paralog-based IBA over-annotation, with a
better-supported MF already in place.

---

## Mechanistic Scope

- **Immediate molecular activity actually tested/supported for ABRAXAS1:** a
  **scaffold/adaptor** that reads **K63-linked polyubiquitin** (via associated RAP80/BRCC36)
  and physically tethers BRCA1–BARD1 to ubiquitinated H2A/H2AX at DNA double-strand
  breaks. Molecular function = polyubiquitin-dependent protein binding; cellular
  component = nuclear BRCA1-A complex.
- **Microtubule binding is a *molecular activity of a different gene product* (ABRAXAS2)**,
  not a downstream phenotype of ABRAXAS1. There is no direct-binding, localization, or
  mutant evidence placing ABRAXAS1 on microtubules or the spindle.
- ABRAXAS1's only mitosis-adjacent role is **G2/M DNA-damage checkpoint signalling** — a
  regulatory/pathway consequence, distinct from GO:0008017.

---

## Conflicts and Alternatives

- **Paralog confusion (primary explanation):** ABRAXAS1 (Q6UWZ7, nuclear BRCA1-A) vs
  ABRAXAS2 (Q15018, cytoplasmic BRISC, spindle pole). ~41% identical; same PANTHER
  family → PAINT propagated ABRAXAS2's experimental spindle/microtubule terms to
  ABRAXAS1. The `withFrom` field explicitly names Q15018 as the source.
- **Node separation is telling:** the *genuine* ubiquitin-binding term (GO:0031593)
  propagated from a **different** ancestral node (PTN001272081) and is independently IDA
  on ABRAXAS1; the microtubule cluster propagated from **PTN001272083** and is IDA/IMP
  only on ABRAXAS2. The annotations that are real are internally corroborated; the
  microtubule ones are not.
- **No isoform/organism rescue found:** UniProt lists ABRAXAS1 localization as Nucleus
  only; no spindle/cytoskeletal isoform is annotated.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| Any direct ABRAXAS1–tubulin/microtubule interaction | Literature search (multiple queries) + UniProt + QuickGO | If a real interaction existed, removal would be wrong | An in vitro microtubule co-sedimentation/pelleting assay with purified ABRAXAS1; IF co-localization with tubulin in mitosis |
| Whether ABRAXAS1 ever localizes to spindle/centrosome | UniProt subcellular location (Nucleus only); HPA nuclear body | Localization would be a prerequisite for the term | High-resolution mitotic IF / live imaging of endogenous ABRAXAS1 |
| PAINT node review status | Traced node PTN001272083 + Q15018 | Curators may already have flagged the node | Inspect the PANTHER family tree annotation and whether a NOT/qualifier was applied |

---

## Discriminating Tests

1. **Microtubule co-sedimentation assay** with purified recombinant ABRAXAS1 ± taxol-stabilized
   microtubules — direct test of GO:0008017; ABRAXAS2 as positive control.
2. **Mitotic immunofluorescence / live imaging** of endogenous ABRAXAS1 vs ABRAXAS2 to test
   spindle-pole localization (expected: ABRAXAS2 yes, ABRAXAS1 no).
3. **Depletion phenotype comparison:** siABRAXAS1 vs siABRAXAS2 spindle-assembly / chromosome
   mis-attachment scoring — the spindle phenotype should segregate to ABRAXAS2.
4. **PANTHER tree audit** of PTN001272083 to confirm the experimental basis is exclusively
   ABRAXAS2-lineage and apply an experimental-evidence-based override for ABRAXAS1.

---

## Curation Leads (require curator verification)

- **Action change:** Remove/reject IBA GO:0008017 (and co-clustered GO:0008608,
  GO:0090307) on ABRAXAS1 as paralog over-annotation; keep GO:0031593 (IDA) as the
  informative MF.
- **Candidate reference to cite for the over-annotation source (verify snippet):**
  PMID **31253574** — *"…the lysine-63 linkage-specific BRCC36 subunit that is functionalized
  by scaffold subunits ABRAXAS and ABRO1, respectively."*
- **Candidate reference for ABRAXAS1's true nuclear function (verify snippet):**
  PMID **28009280** — *"It is recruited to damaged chromatin as a component of the BRCA1-A
  deubiquitinase, which cleaves K63-linked ubiquitin chains attached to histone H2A and H2AX."*
- **Suggested curator question:** Does GO_Central want to add a `NOT` qualifier or
  experimental-override for ABRAXAS1 at node PTN001272083, given that Q15018 (ABRAXAS2) is
  the sole experimental source and ABRAXAS1 is nucleus-restricted?
- **Suggested experiment:** microtubule co-pelleting of purified ABRAXAS1 (definitive).

---

### Provenance (computed this run)
- UniProt Q6UWZ7: 409 aa; MPN domain 7–160; coiled-coil 206–260; Loc = Nucleus; MF IDA = GO:0031593.
- QuickGO: GO:0008017 = IBA / GO_REF:0000033 / assignedBy GO_Central / withFrom PANTHER:PTN001272083 + UniProtKB:Q15018.
- UniProt Q15018 (ABRAXAS2): microtubule binding IDA; spindle attachment IMP; spindle assembly IMP; Loc = spindle pole/cytoskeleton.
- Needleman–Wunsch ABRAXAS1 vs ABRAXAS2: ~40.8% identity (shorter seq) / ~45.4% (aligned core) → true paralogs in one PANTHER family.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)