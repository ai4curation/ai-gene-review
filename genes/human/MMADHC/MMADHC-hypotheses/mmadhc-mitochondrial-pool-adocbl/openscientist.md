---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-18T17:08:49.831860'
end_time: '2026-10-18T17:24:11.023902'
duration_seconds: 921.19
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: MMADHC
  gene_symbol: MMADHC
  uniprot_accession: Q9H3L0
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: mmadhc-mitochondrial-pool-adocbl
  hypothesis_text: 'Human MMADHC (UniProt Q9H3L0) performs part of its cobalamin-trafficking
    function inside the mitochondrial matrix: its mitochondrially imported pool is
    required for adenosylcobalamin (AdoCbl) supply to methylmalonyl-CoA mutase (MMUT),
    rather than mitochondrial import serving mainly as a turnover route while the
    decisive branch-point activity is cytosolic.'
  term_context: '- Term: mitochondrial matrix (GO:0005759)

    - Decisive question: does loss or mistargeting of the mitochondrial MMADHC pool
    selectively impair AdoCbl synthesis/MMUT function (genotype-phenotype data, targeting-sequence
    and alternative-start-site variants, rescue experiments), and is there evidence
    for a matrix-side interaction partner (e.g. MMAB, MMUT, MMAA)?'
  reference_context: '- PMID:22156578

    - PMID:23415655

    - PMID:23270877

    - PMID:42709793'
  source_file: genes/human/MMADHC/MMADHC-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human MMADHC (UniProt Q9H3L0) performs part of\
    \ its cobalamin-trafficking function inside\n  the mitochondrial matrix: its mitochondrially\
    \ imported pool is required for adenosylcobalamin (AdoCbl)\n  supply to methylmalonyl-CoA\
    \ mutase (MMUT), rather than mitochondrial import serving mainly as a turnover\n\
    \  route while the decisive branch-point activity is cytosolic.'\nfocus_type:\
    \ function_assignment\nterm_id: GO:0005759\nterm_label: mitochondrial matrix\n\
    context:\n- 'Decisive question: does loss or mistargeting of the mitochondrial\
    \ MMADHC pool selectively impair AdoCbl\n  synthesis/MMUT function (genotype-phenotype\
    \ data, targeting-sequence and alternative-start-site variants,\n  rescue experiments),\
    \ and is there evidence for a matrix-side interaction partner (e.g. MMAB, MMUT,\
    \ MMAA)?'\nreference_id:\n- PMID:22156578\n- PMID:23415655\n- PMID:23270877\n\
    - PMID:42709793"
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
citation_count: 9
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
- **Gene directory:** MMADHC
- **Gene symbol:** MMADHC
- **UniProt accession:** Q9H3L0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** mmadhc-mitochondrial-pool-adocbl
- **Source file:** genes/human/MMADHC/MMADHC-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human MMADHC (UniProt Q9H3L0) performs part of its cobalamin-trafficking function inside the mitochondrial matrix: its mitochondrially imported pool is required for adenosylcobalamin (AdoCbl) supply to methylmalonyl-CoA mutase (MMUT), rather than mitochondrial import serving mainly as a turnover route while the decisive branch-point activity is cytosolic.

## Term and Decision Context

- Term: mitochondrial matrix (GO:0005759)
- Decisive question: does loss or mistargeting of the mitochondrial MMADHC pool selectively impair AdoCbl synthesis/MMUT function (genotype-phenotype data, targeting-sequence and alternative-start-site variants, rescue experiments), and is there evidence for a matrix-side interaction partner (e.g. MMAB, MMUT, MMAA)?

## Reference Context

- PMID:22156578
- PMID:23415655
- PMID:23270877
- PMID:42709793

## Source Context YAML

```yaml
hypothesis: 'Human MMADHC (UniProt Q9H3L0) performs part of its cobalamin-trafficking function inside
  the mitochondrial matrix: its mitochondrially imported pool is required for adenosylcobalamin (AdoCbl)
  supply to methylmalonyl-CoA mutase (MMUT), rather than mitochondrial import serving mainly as a turnover
  route while the decisive branch-point activity is cytosolic.'
focus_type: function_assignment
term_id: GO:0005759
term_label: mitochondrial matrix
context:
- 'Decisive question: does loss or mistargeting of the mitochondrial MMADHC pool selectively impair AdoCbl
  synthesis/MMUT function (genotype-phenotype data, targeting-sequence and alternative-start-site variants,
  rescue experiments), and is there evidence for a matrix-side interaction partner (e.g. MMAB, MMUT, MMAA)?'
reference_id:
- PMID:22156578
- PMID:23415655
- PMID:23270877
- PMID:42709793
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

# AIGR Gene Hypothesis Deep Research: MMADHC Mitochondrial Matrix Pool and AdoCbl Supply

**Target gene:** MMADHC (human; UniProt Q9H3L0)
**Focus type:** function_assignment
**Hypothesis slug:** mmadhc-mitochondrial-pool-adocbl
**GO term under evaluation:** mitochondrial matrix (GO:0005759)

---

## Summary

The seed hypothesis asserts that human MMADHC performs part of its cobalamin-trafficking function **inside the mitochondrial matrix** — specifically that its mitochondrially imported pool is *required* for adenosylcobalamin (AdoCbl) supply to methylmalonyl-CoA mutase (MMUT), rather than mitochondrial import serving mainly as a turnover route while the decisive branch-point activity is cytosolic. After three investigative iterations synthesizing primary literature, STRING interaction data, QuickGO annotation records, and a presequence sequence analysis, the overall verdict is **partially supported, and best treated as a cellular-component (CC) refinement rather than a new functional claim.**

The hypothesis bundles two separable assertions. The **first** — that MMADHC has a genuinely mitochondrially-imported pool that reaches the matrix — is well supported: UniProt annotates a cleavable N-terminal matrix-targeting presequence (residues 1–38) with canonical features; immunofluorescence plus subcellular fractionation establish dual cytosolic/mitochondrial localization ([PMID:23270877](https://pubmed.ncbi.nlm.nih.gov/23270877/)); and MMADHC accumulates **inside** mitochondria when the soluble matrix protease LONP1 is inhibited ([PMID:42709793](https://pubmed.ncbi.nlm.nih.gov/42709793/)), physically placing an imported pool in the matrix. Targeting-sequence engineering and genotype-phenotype data causally tie the mitochondrial form to the AdoCbl branch ([PMID:22156578](https://pubmed.ncbi.nlm.nih.gov/22156578/), [PMID:24722857](https://pubmed.ncbi.nlm.nih.gov/24722857/)).

The **second** assertion — that the matrix pool is the *decisive* AdoCbl-supply activity rather than a turnover route — remains **unproven and is actively contested** by the newest primary literature. The only biochemically and structurally characterized MMADHC interaction is cytosolic (with CblC/MMACHC via the C-terminal domain; [PMID:23415655](https://pubmed.ncbi.nlm.nih.gov/23415655/), [PMID:26364851](https://pubmed.ncbi.nlm.nih.gov/26364851/)); STRING shows zero experimental interaction evidence for the mitochondrial enzymes MMAA/MMAB/MMUT; and the 2026 study frames mitochondrial import partly as LONP1-dependent turnover while cytosol-stabilized MMADHC drives methionine synthase (MTR). The practical curation implication is that refining the existing GO:0005739 (mitochondrion, IDA) toward GO:0005759 (mitochondrial matrix) is defensible but should carry an **inferential evidence code, not IDA**, and no matrix-side molecular-function annotation should be added on the strength of this hypothesis.

---

## Executive Judgment

**Verdict: Partially supported — CC refinement, not a new MF/BP claim.**

- The **location** claim (MMADHC has an imported matrix pool) is strongly supported by converging localization, genetic, and perturbation evidence.
- The **function-in-location** claim (the matrix pool is the decisive AdoCbl supplier to MMUT) is **unresolved**, and an equally-consistent competing model places the decisive branch-point chemistry in the cytosol with the matrix pool acting partly as a turnover sink.
- No published experiment demonstrates a matrix-side molecular partner (MMAB/MMUT/MMAA) or a matrix-localized catalytic/carrier step. Therefore the hypothesis as literally stated cannot be affirmed.

---

## Key Findings

### F001 — MMADHC is dual-localized to cytosol and mitochondrion, with a matrix-degraded pool

Human MMADHC carries a predicted N-terminal mitochondrial transit peptide (UniProt Q9H3L0, residues 1–38) and is annotated with dual subcellular location (Cytoplasm; Mitochondrion). This is not purely a prediction: immunofluorescence combined with subcellular fractionation directly demonstrated that MMADHC is present in both compartments ([PMID:23270877](https://pubmed.ncbi.nlm.nih.gov/23270877/)), which concluded that "*MMADHC is both mitochondrial and cytoplasmic, consistent with the proposal that MMADHC acts as a branch point for vitamin B12 delivery to the cytoplasm and mitochondria.*"

The most compartment-specific line of evidence comes from the 2026 study ([PMID:42709793](https://pubmed.ncbi.nlm.nih.gov/42709793/)): MMADHC **accumulates in mitochondria when the matrix protease LONP1 is inhibited**, and relocates to the cytosol upon proton-motive-force (PMF) collapse (which blocks import). Because LONP1 is a soluble matrix protease, accumulation of its substrate upon LONP1 inhibition places an imported MMADHC pool physically inside the matrix. This is the single best argument for GO:0005759 over the more general GO:0005739. The important nuance is that this same observation frames the matrix pool partly as a **degradation substrate**, which is in direct tension with the "decisive functional pool" framing of the seed hypothesis.

### F002 — Enhancing MMADHC mitochondrial targeting selectively increases AdoCbl synthesis

The strongest causal link between the mitochondrial form of MMADHC and the AdoCbl/MMUT branch is an engineering experiment in patient cells. In cblD-MMA/HC fibroblasts, attaching an enhanced mitochondrial leader sequence to MMADHC "*clearly increased the formation of adenosylcobalamin (AdoCbl) with a concomitant decrease in MeCbl formation*" ([PMID:22156578](https://pubmed.ncbi.nlm.nih.gov/22156578/)). The reciprocal shift (more AdoCbl, less MeCbl) is mechanistically informative: directing more MMADHC to mitochondria pulls cobalamin flux toward the mitochondrial (AdoCbl) arm at the expense of the cytosolic (MeCbl) arm, consistent with MMADHC acting at the branch point and with a functional role for the mitochondrial form.

This is reinforced by genotype-phenotype correlation. Null mutations N-terminal to Met116 — i.e., affecting or removing the N-terminal targeting region while leaving an internal alternative start (Met116) to produce a cytosol-only protein — cause **isolated** methylmalonic aciduria (cblD-MMA) from AdoCbl deficiency ([PMID:24722857](https://pubmed.ncbi.nlm.nih.gov/24722857/)). Losing the N-terminal/targeted form selectively knocks out the AdoCbl branch while sparing the MeCbl branch, exactly the dissociation predicted if the mitochondrially-targeted form serves AdoCbl synthesis.

These two results are the empirical backbone of the hypothesis. They establish that the **targeted (N-terminal) form** is required for AdoCbl. What they do **not** establish is *where* the required activity physically occurs — targeting-sequence experiments change the amount of protein delivered to mitochondria but do not prove the decisive chemistry happens in the matrix rather than at the import interface or in a cytosolic pool whose size is coupled to targeting efficiency.

### F003 — The only characterized molecular interaction of MMADHC is cytosolic (with CblC/MMACHC); no matrix partner demonstrated

Mechanistically, the best-defined MMADHC interaction is with the cytosolic processing enzyme CblC/MMACHC, mediated by MMADHC's C-terminal domain (~residues 116–296). The crystal structure of human CblD showed "*the globular C-terminal domain of human CblD, which is sufficient for its interaction with MMADHC... or CblC, and for supporting the cytoplasmic cobalamin trafficking pathway*" ([PMID:26364851](https://pubmed.ncbi.nlm.nih.gov/26364851/)); the interaction was also characterized biochemically by Gherasim et al. ([PMID:23415655](https://pubmed.ncbi.nlm.nih.gov/23415655/)). This interaction is explicitly cytoplasmic.

Critically, the newest study demonstrates a **functionally important cytosolic role** that competes with the matrix-centric interpretation: "*Cytosol-stabilized MMADHC increases MTR levels and activity*" ([PMID:42709793](https://pubmed.ncbi.nlm.nih.gov/42709793/)). Stabilizing MMADHC in the cytosol enhances methionine synthase (MTR) — a cytosolic, MeCbl-dependent enzyme — while the authors frame mitochondrial import partly as a LONP1-dependent turnover route. No direct physical interaction between MMADHC and any mitochondrial cobalamin enzyme (MMAB, MMUT, MMAA) has been demonstrated in any assay.

### F004 — STRING: MMADHC's only experimentally-scored interactor is cytosolic MMACHC; matrix enzymes link only by text-mining

A programmatic STRING-db query (human, taxon 9606) for MMADHC interaction partners quantifies the asymmetry of the evidence:

| Partner | Compartment | STRING combined score | Experimental subscore (escore) | Dominant evidence channel |
|---|---|---|---|---|
| **MMACHC** | Cytosol | 0.998 | **0.90** | Experimental + text-mining |
| MMAA | Mitochondrion | 0.986 | **0.00** | Text-mining (~0.95–0.99) + pathway |
| MMAB | Mitochondrion | 0.978 | **0.00** | Text-mining + pathway |
| MMUT | Mitochondrion | 0.958 | **0.00** | Text-mining + pathway |

The mitochondrial cobalamin enzymes have high *combined* scores but **zero experimental evidence** — their association is inferred from co-mention in literature and shared pathway membership, not from any interaction assay. This is exactly the pattern expected when proteins operate in the same pathway but do not physically partner, and it is the kind of frequency/co-mention bias a curator must discount.

Separately, analysis of the N-terminal presequence (residues 1–38) confirmed canonical cleavable matrix-targeting features: **net charge +5, zero acidic (D/E) residues across all 38 positions** (and none in the first 15), amphipathic and hydrophobic-rich, with arginines at positions 8, 10, and 24. This supports classical TOM/TIM23-mediated import to the matrix and is consistent with (though not proof of) matrix delivery.

### F005 — MMADHC is already annotated to mitochondrion (GO:0005739, IDA) but NOT to mitochondrial matrix (GO:0005759)

A programmatic EBI QuickGO query for Q9H3L0 (24 unique annotation lines) establishes the current curation baseline:

| Aspect | GO term | Current status | Evidence / source |
|---|---|---|---|
| CC | GO:0005737 cytoplasm | Annotated | IDA ([PMID:23270877](https://pubmed.ncbi.nlm.nih.gov/23270877/)) |
| CC | GO:0005739 mitochondrion | Annotated | IDA ([PMID:23270877](https://pubmed.ncbi.nlm.nih.gov/23270877/)); IEA/IBA/HTP |
| CC | GO:0005829 cytosol | Annotated | IDA/TAS |
| CC | **GO:0005759 mitochondrial matrix** | **NOT annotated** | — (this hypothesis) |
| MF | GO:0005515 protein binding | Annotated | IPI ([PMID:23415655](https://pubmed.ncbi.nlm.nih.gov/23415655/)) |
| MF | GO:0140104 molecular carrier activity | Annotated | IDA/EXP ([PMID:22156578](https://pubmed.ncbi.nlm.nih.gov/22156578/)) |
| BP | GO:0009235 cobalamin metabolic process | Annotated | IDA ([PMID:22156578](https://pubmed.ncbi.nlm.nih.gov/22156578/), [PMID:24722857](https://pubmed.ncbi.nlm.nih.gov/24722857/)) |

The decisive curation question is therefore narrow: should the existing GO:0005739 (mitochondrion, IDA) be **refined to** the child term GO:0005759 (mitochondrial matrix)? The evidence (F001–F004) makes the matrix sub-compartment *plausible and defensible* but not *directly demonstrated* at IDA strength.

---

## Mechanistic Model / Interpretation

MMADHC sits at the cobalamin "branch point" where intracellular B12 is partitioned between the mitochondrial AdoCbl arm (feeding MMUT / methylmalonyl-CoA metabolism) and the cytosolic MeCbl arm (feeding MTR / methionine synthesis).

```
                 cytosolic Cbl (from MMACHC/CblC processing)
                              |
                       [ MMADHC ]  <-- C-terminal domain binds MMACHC (cytosol; PMID:23415655, 26364851)
                        /        \
         N-terminal presequence   C-terminal / Met116 cytosolic form
         (residues 1-38) directs          |
         import via TOM/TIM23              v
                 |                   MeCbl arm --> MTR (methionine synthase)
                 v                   (cytosol-stabilized MMADHC boosts MTR; PMID:42709793)
        MITOCHONDRIAL MATRIX
        - imported pool present (LONP1 substrate; PMID:42709793)
        - targeting enhancement raises AdoCbl, lowers MeCbl (PMID:22156578)
        - N-terminal null => isolated MMA / AdoCbl deficiency (PMID:24722857)
                 |
                 ?  <-- NO demonstrated matrix partner (MMAB/MMUT/MMAA escore=0)
                 v
        AdoCbl arm --> MMUT (methylmalonyl-CoA mutase)
```

Two interpretations remain compatible with all current data:

1. **Seed hypothesis (matrix-decisive):** the imported matrix pool is where MMADHC hands cobalamin into the AdoCbl pathway for MMUT. Supported by targeting-sequence rescue and N-terminal genotype-phenotype dissociation.

2. **Competing model (cytosol-decisive + matrix turnover):** the decisive trafficking/branch-point chemistry happens in the cytosol (where the only characterized interaction, with MMACHC, occurs), and mitochondrial import is partly a LONP1-dependent turnover route. Supported by the structural/interaction data and by the 2026 finding that cytosol-stabilized MMADHC drives MTR.

The targeting-enhancement experiment (F002) is the pivot: it is consistent with model 1 but does not exclude model 2, because increasing import efficiency also changes the cytosol/mitochondrion partition and could act by removing MMADHC from a cytosolic competing reaction. No experiment yet shows a matrix-localized catalytic or carrier step, nor a matrix partner. The honest status is that the **location** claim is strong, while the **function-in-location** claim is unresolved.

---

## Evidence Matrix

| Citation | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:23270877](https://pubmed.ncbi.nlm.nih.gov/23270877/) | Localization (IF + fractionation) | **Supports** (import pool) | MMADHC is mitochondrial | Dual cytosolic + mitochondrial localization; "branch point" for B12 delivery | Human fibroblasts/cell lines | High for mitochondrion; does not resolve matrix sub-compartment |
| [PMID:42709793](https://pubmed.ncbi.nlm.nih.gov/42709793/) | Localization + perturbation | **Qualifies** (matrix pool but as turnover) | Imported pool reaches matrix | MMADHC accumulates in mito under LONP1 (matrix protease) inhibition; cytosol-stabilized MMADHC raises MTR | Human cells | High that a matrix pool exists; frames import partly as turnover, competing with "decisive" framing |
| [PMID:22156578](https://pubmed.ncbi.nlm.nih.gov/22156578/) | Mutant/engineering phenotype | **Supports** | Mitochondrial targeting drives AdoCbl | Enhanced mito leader → ↑AdoCbl, ↓MeCbl | cblD-MMA/HC patient fibroblasts | High causal link to AdoCbl branch; does not localize the decisive step to matrix per se |
| [PMID:24722857](https://pubmed.ncbi.nlm.nih.gov/24722857/) | Mutant phenotype / genotype-phenotype | **Supports** | N-terminal form needed for AdoCbl | Null mutations N-terminal to Met116 → isolated MMA (AdoCbl deficiency) | Patient alleles / functional domain mapping | High; dissociates AdoCbl vs MeCbl arms by targeting region |
| [PMID:23415655](https://pubmed.ncbi.nlm.nih.gov/23415655/) | Interaction (IPI) | **Competing** (cytosolic) | Characterized partner is cytosolic | MMADHC–MMACHC interaction, C-terminal domain | In vitro / human proteins | High; the only biochemically defined interaction is cytosolic |
| [PMID:26364851](https://pubmed.ncbi.nlm.nih.gov/26364851/) | Structural | **Competing** (cytosolic) | Domain sufficient for cytosolic pathway | C-terminal domain sufficient for MMACHC/CblC interaction & cytoplasmic trafficking | Crystal structure, human CblD | High; locates characterized function to cytosol |
| STRING-db (9606) | Computational/interaction | **Qualifies / competing** | Matrix enzyme partners | MMACHC escore 0.90; MMAA/MMAB/MMUT escore 0.00 (text-mining only) | Database | Medium; argues against demonstrated matrix partner |
| UniProt Q9H3L0 + presequence analysis | Computational/sequence | **Supports** (import feasibility) | Matrix-targeting presequence | Residues 1–38: +5 net charge, 0 acidic, amphipathic Arg-rich | Sequence | Medium; predicts cleavable matrix targeting, not proof of matrix residence |
| EBI QuickGO (Q9H3L0) | Database | **Context** | Current GO baseline | GO:0005739 annotated (IDA); GO:0005759 NOT annotated | Database | High for baseline; defines the decision |

---

## GO Curation Implications

**Lead requiring curator verification:** Consider refining the existing CC annotation **GO:0005739 (mitochondrion, IDA)** toward its child **GO:0005759 (mitochondrial matrix)**, but **with an inferential evidence code** (e.g., ISM — inferred from sequence model, IC — inferred by curator, or an author-statement code), **not IDA**.

Rationale:
- The matrix sub-compartment is supported by (a) a canonical cleavable matrix-targeting presequence and (b) LONP1 (matrix protease)-dependent accumulation of MMADHC inside mitochondria ([PMID:42709793](https://pubmed.ncbi.nlm.nih.gov/42709793/)). This exceeds a pure prediction but falls short of a direct sub-compartment assay (mitoplast fractionation, protease-protection, submitochondrial immuno-EM).
- IDA should be reserved for a direct experiment that physically places MMADHC in the matrix lumen. None is published; using IDA would overstate the evidence.

**Do NOT, on the basis of this hypothesis:**
- Add any matrix-side **MF** term implying a matrix-localized catalytic/carrier step beyond the existing GO:0140104 (molecular carrier activity), which is already annotated without a sub-compartment qualifier.
- Add an interaction (IPI) annotation to MMAB/MMUT/MMAA — there is no experimental interaction evidence (STRING escore 0).
- Strengthen BP GO:0009235 (cobalamin metabolic process) into a matrix-specific functional claim.

**Net recommendation:** The hypothesis should influence the review as a **CC-term refinement lead** (mitochondrion → mitochondrial matrix, inferential code), explicitly flagged as not-yet-IDA, and should **not** be used to assert a matrix-decisive molecular function. The competing cytosolic-branch-point interpretation must be retained in the review notes.

---

## Mechanistic Scope

The immediate molecular entity being tested is a **cellular-component assignment** (matrix residence) coupled to an implied **molecular carrier/trafficking function** (handing cobalamin into the AdoCbl pathway). The directly supported items are:

- **Direct gene-product activity:** cobalamin carrier/branch-point activity (GO:0140104), characterized mechanistically only via the cytosolic MMADHC–MMACHC interaction.
- **Localization fact:** an imported mitochondrial pool that reaches the LONP1-accessible matrix compartment.

The following are **downstream or inferred**, and must be separated from the direct claim:
- *AdoCbl deficiency / methylmalonic aciduria* is a **loss-of-function phenotype** (patient metabolite data), not a direct demonstration of matrix-side catalysis.
- *MMUT dysfunction* is a **pathway consequence** downstream of AdoCbl supply, not a demonstrated direct MMADHC–MMUT handoff.
- *The AdoCbl↑/MeCbl↓ shift under enhanced targeting* is a **flux-partition readout**, consistent with but not proof of matrix-localized activity.

---

## Conflicts and Alternatives

1. **Cytosolic branch-point model (strongest competitor).** The only structurally/biochemically defined MMADHC interaction is cytosolic (with MMACHC, via the C-terminal domain; [PMID:23415655](https://pubmed.ncbi.nlm.nih.gov/23415655/), [PMID:26364851](https://pubmed.ncbi.nlm.nih.gov/26364851/)). The 2026 study shows cytosol-stabilized MMADHC boosts MTR and treats mitochondrial import partly as turnover ([PMID:42709793](https://pubmed.ncbi.nlm.nih.gov/42709793/)). Under this model, the decisive trafficking chemistry is cytosolic and the matrix pool is at least partly a degradation sink.

2. **Turnover-sink interpretation of the LONP1 result.** The very observation that best localizes MMADHC to the matrix (LONP1-inhibition accumulation) simultaneously implies the matrix pool is a protease substrate — which weakens the "decisive functional pool" framing.

3. **Frequency / co-mention bias in databases.** High STRING combined scores for MMAA/MMAB/MMUT could mislead a curator into inferring matrix partners; these are driven by text-mining and pathway co-membership (escore 0), not interaction assays.

4. **Targeting-experiment confound.** Enhanced mitochondrial targeting (F002) changes the cytosol/mitochondrion partition; the AdoCbl increase could in principle reflect relief of a cytosolic competing reaction rather than new matrix activity.

5. **No organism-specific or paralog confusion identified.** MMADHC has no close functional paralog that would create overannotation here; the main risk is sub-compartment overstatement, not paralog mix-up.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| No direct matrix sub-compartment assay | UniProt topology, QuickGO (no GO:0005759), PMID:42709793 (LONP1 proxy) | Determines whether GO:0005759 can be IDA vs inferential | Mitoplast fractionation / protease-protection / submitochondrial immuno-EM on endogenous MMADHC |
| No demonstrated matrix partner | STRING escore for MMAA/MMAB/MMUT = 0; interaction literature | The decisive-function claim hinges on a matrix handoff partner | Co-IP / proximity labeling (BioID/APEX) of the imported MMADHC form in matrix |
| Cannot separate matrix vs cytosol as the decisive step | PMID:22156578 (targeting), PMID:24722857 (genotype) | Distinguishes seed hypothesis from cytosolic-branch model | Matrix-restricted vs cytosol-restricted MMADHC rescue in null cells, scoring AdoCbl and MMUT activity |
| Presequence cleavage unconfirmed experimentally | Sequence features computed (net +5, 0 acidic) | A cleaved mature matrix form vs uncleaved membrane-associated form changes interpretation | N-terminal Edman/MS of the mature imported form |
| PMID:42709793 details read from snippet only | One snippet verified, abstract unchecked | The turnover-vs-function framing is pivotal | Full-text read of PMID:42709793 methods/results |

---

## Discriminating Tests

1. **Compartment-restricted rescue.** In MMADHC-null (cblD) fibroblasts, express (a) a matrix-restricted MMADHC (strong cleavable presequence, no cytosolic retention) vs (b) a cytosol-restricted form (Met116 start / import-dead). Score AdoCbl synthesis and MMUT activity. The seed hypothesis predicts only the matrix-restricted form rescues the AdoCbl/MMUT arm.

2. **Proximity labeling of the imported pool.** BioID/APEX2 fused to the N-terminally targeted MMADHC, with streptavidin pulldown and MS, to test for matrix partners (MMAB, MMUT, MMAA) directly — addressing the escore-0 gap.

3. **Mitoplast + protease-protection fractionation** of endogenous MMADHC to physically assign GO:0005759 at IDA strength, controlling with known matrix (MMUT), IMS, and inner-membrane markers.

4. **LONP1-independent matrix stabilization.** Separate "functional residence" from "turnover substrate" by stabilizing matrix MMADHC without LONP1 inhibition and asking whether AdoCbl/MMUT output rises.

5. **MS of the mature N-terminus** to confirm presequence cleavage and define the mature matrix form.

---

## Proposed Follow-up Experiments / Actions

- **Curation action (lead):** stage a refinement of GO:0005739 → GO:0005759 with an **inferential evidence code**, annotated with the rationale (matrix-targeting presequence + LONP1-substrate behavior), and explicitly note that IDA is not yet justified. Retain the existing GO:0005739 unless curators accept the child term.
- **Do not** add matrix-side MF/BP functional terms or MMAB/MMUT/MMAA interaction annotations from this hypothesis.
- **Record the competing cytosolic-branch interpretation** (PMID:23415655, PMID:26364851, PMID:42709793) in the review so the matrix claim is not overstated.
- **Flag for curator** the two verifiable snippets: PMID:22156578 ("improving mitochondrial targeting... increased the formation of adenosylcobalamin... concomitant decrease in MeCbl") and PMID:42709793 ("MMADHC accumulates in mitochondria with LONP1 inhibition but in the cytosol upon PMF collapse").
- **Recommend the compartment-restricted rescue experiment** as the single most decisive future test.

---

## Evidence Base (Key Literature)

- *Gene identification for the cblD defect of vitamin B12 metabolism.* [PMID:18385497](https://pubmed.ncbi.nlm.nih.gov/18385497/) — identifies MMADHC; notes putative mitochondrial targeting sequence and cobalamin-binding motif; WT transfection rescues both AdoCbl and MeCbl synthesis.
- *Molecular mechanisms leading to three different phenotypes in the cblD defect.* [PMID:22156578](https://pubmed.ncbi.nlm.nih.gov/22156578/) — enhanced mitochondrial targeting increases AdoCbl, decreases MeCbl (core support for the mitochondrial-form → AdoCbl link).
- *Characterization of functional domains of the cblD (MMADHC) gene product.* [PMID:24722857](https://pubmed.ncbi.nlm.nih.gov/24722857/) — N-terminal null mutations (N-terminal to Met116) → isolated MMA / AdoCbl deficiency.
- *Subcellular location of MMACHC and MMADHC.* [PMID:23270877](https://pubmed.ncbi.nlm.nih.gov/23270877/) — dual mitochondrial + cytoplasmic localization; branch-point model.
- *The 2026 LONP1/PMF study.* [PMID:42709793](https://pubmed.ncbi.nlm.nih.gov/42709793/) — matrix accumulation under LONP1 inhibition (matrix pool) but turnover framing; cytosol-stabilized MMADHC increases MTR.
- *Characterization/structure of CblD and its interactions.* [PMID:23415655](https://pubmed.ncbi.nlm.nih.gov/23415655/), [PMID:26364851](https://pubmed.ncbi.nlm.nih.gov/26364851/) — C-terminal domain mediates the cytosolic MMADHC–MMACHC/CblC interaction (competing cytosolic model).
- *Clinical/molecular heterogeneity of cblD.* [PMID:19058814](https://pubmed.ncbi.nlm.nih.gov/19058814/) — N-terminal mutations → MMA, C-terminal → homocystinuria, supporting the branch-point domain logic.
- *The complex machinery of human cobalamin metabolism.* [PMID:36680553](https://pubmed.ncbi.nlm.nih.gov/36680553/) — review-level orientation on the pathway.

---

### Bottom line for the curator

The matrix **location** claim is defensible and warrants a GO:0005739 → GO:0005759 refinement under an **inferential** evidence code. The matrix **function-decisive** claim is **unresolved** and currently balanced against a well-supported cytosolic branch-point model; it should not drive a matrix-side functional annotation. A single compartment-restricted rescue experiment would most efficiently settle the question.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)