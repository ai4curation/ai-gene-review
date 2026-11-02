---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:40:32.655106'
end_time: '2026-10-24T05:04:59.833164'
duration_seconds: 1467.18
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ECOLI
  gene: yciO
  gene_symbol: yciO
  uniprot_accession: P0AFR4
  taxon_id: NCBITaxon:83333
  taxon_label: Escherichia coli K-12
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0061710
  hypothesis_text: yciO has L-threonylcarbamoyladenylate synthase activity (GO:0061710).
  term_context: '- Term: L-threonylcarbamoyladenylate synthase activity (GO:0061710)

    - Evidence type: IDA

    - Original reference: PMID:37963869'
  reference_context: '- PMID:37963869

    - PMID:40703034

    - file:ECOLI/yciO/yciO-deep-research-falcon.md'
  source_file: genes/ECOLI/yciO/yciO-ai-review.yaml
  source_selector: existing_annotations[4].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0061710\n  label: L-threonylcarbamoyladenylate\
    \ synthase activity\nevidence_type: IDA\noriginal_reference_id: PMID:37963869"
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
citation_count: 5
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
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
- filename: provenance_yciO_GO_decision_table.csv
  path: openscientist_artifacts/provenance_yciO_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist yciO GO decision table
- filename: provenance_yciO_evidence_matrix.csv
  path: openscientist_artifacts/provenance_yciO_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist yciO evidence matrix
- filename: provenance_yciO_vs_tsaC_STRING_partners.csv
  path: openscientist_artifacts/provenance_yciO_vs_tsaC_STRING_partners.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist yciO vs tsaC STRING partners
- filename: provenance_yciO_vs_tsaC_activity.csv
  path: openscientist_artifacts/provenance_yciO_vs_tsaC_activity.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist yciO vs tsaC activity
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ECOLI
- **Taxon:** Escherichia coli K-12 (NCBITaxon:83333)
- **Gene directory:** yciO
- **Gene symbol:** yciO
- **UniProt accession:** P0AFR4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0061710
- **Source file:** genes/ECOLI/yciO/yciO-ai-review.yaml
- **Source selector:** existing_annotations[4].function_hypothesis

## Seed Hypothesis

yciO has L-threonylcarbamoyladenylate synthase activity (GO:0061710).

## Term and Decision Context

- Term: L-threonylcarbamoyladenylate synthase activity (GO:0061710)
- Evidence type: IDA
- Original reference: PMID:37963869

## Reference Context

- PMID:37963869
- PMID:40703034
- file:ECOLI/yciO/yciO-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0061710
  label: L-threonylcarbamoyladenylate synthase activity
evidence_type: IDA
original_reference_id: PMID:37963869
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

# AIGR Gene Hypothesis Deep Research — Final Report

## Target: *E. coli* K-12 **yciO** (UniProt **P0AFR4**)
### Seed hypothesis: *yciO* has **L-threonylcarbamoyladenylate synthase activity (GO:0061710)** — IDA, original reference PMID:37963869

Focus type: `function_assignment` · Term: GO:0061710 (EC 2.7.7.87) · Evidence: IDA · Original reference: [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/)

---

## Summary

**The seed hypothesis is OVER-ANNOTATED.** YciO *can* catalyze L-threonylcarbamoyladenylate (TC-AMP) formation in a test tube — and that in-vitro observation is what grounds the GO:0061710 IDA imported from the DeepECtransformer machine-learning paper ([PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/)). So the molecular *capability* is not fabricated. But a convergent weight of independent evidence shows that this activity is **residual, promiscuous paralog activity rather than YciO's physiological function**, and that curating GO:0061710 as YciO's core function would materially mislead downstream users.

Four independent lines of evidence support this judgment. (1) **Kinetics:** a dedicated expert re-evaluation of precisely this ML assignment ([PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/), de Crécy-Lagard, Swairjo et al. 2025) measured YciO at ~0.14 nM/min versus the genuine enzyme TsaC/YrdC at ~2.8 µM/min — roughly **20,000-fold (4.3 orders of magnitude) weaker** under comparable conditions. (2) **Genetics:** *tsaC/yrdC* is **essential** in *E. coli* ([PMID:19287007](https://pubmed.ncbi.nlm.nih.gov/19287007/)) even though *yciO* is present in the same genome, and YciO does **not** complement TsaC loss; YciO is itself non-essential and has no reported t6A/tRNA phenotype. (3) **Sequence/family:** the two proteins share only the ancestral YrdC/Sua5 fold (Pfam PF01300, ~35–40% identity by computed global alignment) but fall into **different InterPro subfamilies** (YciO: IPR052532; TsaC subfamily: IPR023535) and sit in distant genome loci/operons (*yciO* = b1267; *tsaC/yrdC* = b3282). (4) **Functional network:** an independent STRING-db v12 check cleanly separates YciO from the t6A module.

The best mechanistic explanation is that the YrdC/Sua5 fold is intrinsically capable of tRNA-independent TC-AMP synthesis ([PMID:37427786](https://pubmed.ncbi.nlm.nih.gov/37427786/)), so a diverged Sua5-fold paralog like YciO retains a trace of that ancestral chemistry without being under selection for it. The recommended curation action is therefore **not** to deny the in-vitro activity but to prevent GO:0061710 from being treated as YciO's **core function**, to **block** propagation of the downstream t6A biosynthesis (BP) term, and to record YciO's physiological function as currently **unknown**.

---

## Executive Judgment

**Verdict: Over-annotated — partially supported in vitro, refuted as a core/physiological function.**

The IDA is literally defensible (a direct assay detected the activity), so the annotation is not a hallucination. The problem is scope: retaining GO:0061710 as YciO's representative function — and the UniProt name "Threonylcarbamoyl-AMP synthase YciO" — implies a t6A biosynthetic role that YciO does not perform in vivo. The single primary source supporting the seed hypothesis is an ML-prediction validation study whose conclusions were explicitly challenged by domain experts who re-examined this exact assignment and found that current ML EC-prediction methods "make basic logic errors … that human annotators avoid." Weighed against trace kinetics, genetic non-redundancy, subfamily divergence, and network separation, the hypothesis fails at every layer that matters for a core-function annotation.

**Most important caveat:** because the activity is real and the IDA carries a PMID and an "experimental" tag, it looks stronger than it is and is at risk of cascade propagation to paralogs/orthologs. Curators should flag it rather than silently inherit it.

---

## Key Findings

### Finding 1 — The GO:0061710 IDA originates from an ML prediction, and a dedicated expert re-evaluation classifies it as an over-annotation

The seed IDA traces to [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) (*Functional annotation of enzyme-encoding genes using deep learning with transformer layers*, "DeepECtransformer"). In that work a transformer model predicted EC 2.7.7.87 (TC-AMP synthase) for YciO, and the authors report: *"We experimentally validated the enzymatic activities predicted for three proteins (YgfF, YciO, and YjdM)."* This single in-vitro validation of an ML call is the entire experimental basis for the annotation. Notably, the assay readout partly rests on ATP→AMP hydrolysis, which is weaker evidence than direct identification of the TC-AMP product.

A **dedicated expert re-evaluation of exactly these ML assignments** was subsequently published: [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) (*Limitations of current machine learning models in predicting enzymatic functions for uncharacterized proteins*; de Crécy-Lagard, Swairjo and colleagues — the group that originally discovered the YrdC/Sua5→t6A pathway). Its central conclusion is blunt: *"We found that current ML methods not only mostly fail to make novel predictions but also make basic logic errors in their predictions that human annotators avoid by leveraging the available knowledge base."* This paper specifically re-examines the YciO case and quantifies the kinetic deficit: YciO makes TC-AMP at roughly **0.14 nM/min** versus TsaC/YrdC at roughly **2.8 µM/min** under comparable enzyme/assay conditions — a **~20,000-fold (≈4.3 orders of magnitude)** rate gap. An activity this far below the true physiological enzyme is the signature of residual, non-selected paralog activity, not a biological function.

### Finding 2 — TsaC/YrdC is essential and is not rescued by YciO, proving genetic non-redundancy

[PMID:19287007](https://pubmed.ncbi.nlm.nih.gov/19287007/) (*The universal YrdC/Sua5 family is required for the formation of threonylcarbamoyladenosine in tRNA*) states plainly that the authors *"prove that yrdC is essential in E. coli."* The logical force for curation is decisive: *E. coli* K-12 carries **both** *yrdC/tsaC* and *yciO* in the same genome, yet deletion of *tsaC* is lethal. If YciO produced physiologically meaningful quantities of TC-AMP, it would at least partially rescue *tsaC* loss — it does not, even when overexpressed (as noted in the re-evaluation). YciO is itself non-essential, has no reported t6A or tRNA-modification phenotype, and therefore is not the cell's TC-AMP source. This converts the seed hypothesis from "YciO is the TC-AMP synthase" into, at most, "YciO retains a vestigial ability to make TC-AMP that the cell does not use."

### Finding 3 — Sequence family and subfamily analysis place YciO as a distant paralog, not a TsaC ortholog

Both YciO and TsaC belong to the universal YrdC/Sua5 superfamily (Pfam **PF01300**), which is why YciO retains the ancestral fold capable of binding ATP, threonine, and bicarbonate and performing the chemistry weakly. However, InterPro resolves them into **different subfamilies**: YciO in **IPR052532**, versus the functionally validated TsaC enzymes in **IPR023535**. A global Needleman–Wunsch alignment computed during this investigation returned only ~**35–40% identity** between YciO and TsaC — consistent with an ancient duplication followed by functional divergence, not with recent orthology. The shared fold explains the in-vitro activity; the subfamily split and modest identity explain why that activity is not under selection in YciO. The fold-level promiscuity is corroborated by [PMID:37427786](https://pubmed.ncbi.nlm.nih.gov/37427786/), which shows a Pandoravirus Sua5 domain makes TC-AMP tRNA-independently — i.e., the Sua5 fold is intrinsically capable of the reaction.

### Finding 4 — STRING functional-association networks independently separate YciO from the t6A machinery

Using STRING-db v12 for *E. coli* K-12 (taxon 511145), the interaction neighborhoods of the two proteins are strikingly different:

- **TsaC/YrdC** co-clusters tightly with the **complete t6A biosynthesis machinery**: TsaB (0.969), TsaD (0.968), TsaE (0.958), plus the *yrdD/yrdB* genomic neighbors.
- **YciO** associates with **unrelated** partners: YciV (0.952), YciQ (0.887), RluB (0.807, a 23S rRNA pseudouridine synthase), YbjL, and YgfF. It shows **no association with TsaD or TsaE at all**, only a weak link to TsaB (0.566), and a weak link to TsaC (0.467) readily attributable to paralog sequence similarity rather than shared pathway membership.

Genomically, the two genes sit far apart in different operons (*yciO* = b1267; *tsaC/yrdC* = b3282). The network thus operationalizes the exact "available knowledge base" that [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) argues human annotators use and ML models ignore — and it independently corroborates that YciO is not part of the t6A module.

---

## Mechanistic Model / Interpretation

This is a textbook **paralog over-annotation driven by residual in-vitro activity plus ML homology/frequency bias**. The YrdC/Sua5 fold is ancient and catalytically promiscuous at the level of weak chemistry. A gene duplication in the bacterial lineage produced two *E. coli* descendants that have since diverged in subfamily, genome context, partners, and selection pressure:

```
                 Ancestral YrdC/Sua5 fold (Pfam PF01300)
                 (binds ATP + L-Thr + HCO3-, can make TC-AMP)
                              │
             ┌────────────────┴─────────────────┐
             │                                   │
      TsaC / YrdC (b3282)                   YciO (b1267)
      InterPro IPR023535                    InterPro IPR052532
      ESSENTIAL                             NON-ESSENTIAL
      ~2.8 µM/min TC-AMP                    ~0.14 nM/min TC-AMP  (~20,000x weaker)
      Partners: TsaB/TsaD/TsaE (0.96+)      Partners: YciV/YciQ/RluB (unrelated)
      Supplies t6A pathway in vivo          No t6A phenotype; function UNKNOWN
             │
     TC-AMP ──► TsaB/TsaD/TsaE ──► t6A37 in tRNA (accurate ANN-codon decoding)
```

The pathway on the left is complete, essential, and network-coherent. YciO on the right has **retained the ancestral fold** — hence a detectable trace of the ancestral chemistry in a sensitive assay — but has diverged in every dimension that signals a dedicated function. The cell cannot be using YciO to make TC-AMP, because if it were, *tsaC* could not be essential.

For GO curation this maps cleanly onto the layers the ontology is meant to distinguish:

| Layer | TsaC/YrdC | YciO |
|---|---|---|
| **MF capability (in vitro)** | TC-AMP synthase (GO:0061710) — strong | TC-AMP synthase (GO:0061710) — **trace only** |
| **MF as core function** | Yes | **No** |
| **BP (t6A biosynthesis, GO:0002949)** | Yes | **No** — no phenotype, not in module |
| **Essentiality** | Essential | Non-essential |
| **Physiological function** | Known (t6A) | **Unknown** |

The seed hypothesis is true only at the "MF capability in vitro" layer and false at every layer that matters for a core-function annotation.

---

## Evidence Base

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|
| [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) | Computational + in-vitro assay | Qualifies (source of IDA) | YciO has EC 2.7.7.87 | DeepECtransformer predicted EC 2.7.7.87; in-vitro assay detected activity (incl. ATP→AMP hydrolysis) | *E. coli* K-12, purified protein | Low–moderate; ML-driven; weak activity; physiology not addressed |
| [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) | Expert re-evaluation + comparative biochemistry | **Refutes (as core function)** | Is the activity YciO's true function? | YciO ~0.14 nM/min vs TsaC ~2.8 µM/min (~20,000× weaker); no TsaC complementation; distinct genome context; ML "logic errors" | *E. coli* K-12 | High; authors discovered the t6A/TsaC pathway and re-examined this exact call |
| [PMID:19287007](https://pubmed.ncbi.nlm.nih.gov/19287007/) | Genetic (null allele) + biochemistry | **Refutes (as core function)** | Is YciO the physiological TC-AMP synthase? | *yrdC/tsaC* essential in *E. coli* despite *yciO* presence → no complementation | *E. coli* K-12 | High; essentiality is a strong in-vivo readout |
| UniProt P0AFR4 / InterPro / Pfam + global alignment (this analysis) | Structural / evolutionary | Qualifies | Are YciO and TsaC the same enzyme? | Shared PF01300 fold; different subfamilies (IPR052532 vs IPR023535); ~35–40% identity (computed NW) | Sequence/domain databases | Moderate–high; shared fold, divergent subfamily explains both activity and split |
| [PMID:37427786](https://pubmed.ncbi.nlm.nih.gov/37427786/) | Structural/biochemical (homolog) | Qualifies | Can a Sua5 fold make TC-AMP tRNA-independently? | Pandoravirus TsaN Sua5 domain makes TC-AMP tRNA-independently → fold intrinsically capable | Pandoravirus, in vitro, cryo-EM | Moderate; explains fold-level promiscuity behind weak YciO activity |
| STRING-db v12 (this analysis) | Computational (functional-association network) | **Refutes (as core function)** | Is YciO in the t6A module? | TsaC clusters with TsaB/TsaD/TsaE (0.96+); YciO does NOT (no TsaD/TsaE; TsaB 0.566, TsaC 0.467); YciO top partners YciV/YciQ/RluB | *E. coli* K-12 (taxon 511145) | Moderate; association ≠ direct interaction, but pattern is clear |
| [PMID:21775474](https://pubmed.ncbi.nlm.nih.gov/21775474/) | Biochemical/structural | Supports (context) | What is the true t6A transfer machinery? | YrdC behaves as a subunit/component of the t6A transferase system; binds unmodified ASL-Lys | *E. coli* | Orientation; establishes TsaC/YrdC as the physiological actor |

---

## GO Curation Implications (leads — require curator verification)

- **GO:0061710 (MF, IDA, [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/)):** Do **not** retain as YciO's core/primary function. In order of preference:
  1. **Qualify** the annotation as *in-vitro / residual activity only* (curator note that activity is ~10⁴× weaker than TsaC and non-physiological), or
  2. **Remove / do not propagate** as a paralog over-annotation driven by an ML prediction (the EC call itself was reported as low/zero model confidence per [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)).
- **Do NOT add BP GO:0002949 (tRNA threonylcarbamoyladenosine modification)** to YciO — that process belongs to TsaC; YciO has no t6A phenotype and cannot complement TsaC.
- **Do NOT assign a CC/complex term** tying YciO to the t6A/KEOPS/Tsa machinery; the network places YciO outside that module.
- **Most accurate current state:** YciO's molecular/biological function is **unknown** (candidate role in RNA metabolism, distinct from t6A). This is more honest than the current EC/MF assignment.
- **Avoid "protein binding"** as a fallback — it is not more informative here. The defensible position is an explicitly qualified MF, or an "unknown function" flag with the TsaC-paralog relationship noted.

---

## Mechanistic Scope

- **Immediate molecular activity tested:** adenylate formation — L-threonine + HCO₃⁻/CO₂ + ATP → L-threonylcarbamoyl-AMP (TC-AMP) + PPi (EC 2.7.7.87). YciO performs this in vitro at a trivial rate; the assay readout in [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) partly rests on ATP→AMP hydrolysis.
- **Downstream / pathway consequence (NOT YciO's):** TC-AMP is the substrate for TsaD/TsaB/TsaE to install t6A₃₇ on ANN-decoding tRNAs. This pathway is executed by **TsaC/YrdC**, not YciO.
- **Loss-of-function inference (refuted as a route to the annotation):** No t6A/translation phenotype is attributable to Δ*yciO*; the essentiality expected of a TC-AMP supplier belongs to *tsaC*. The seed hypothesis conflates a **shared ancestral catalytic capability** with a **dedicated cellular function**.

---

## Conflicts and Alternatives

- **Paralog confusion (primary issue):** YciO is a diverged paralog of TsaC; function-by-similarity (ML and sequence) incorrectly transferred TsaC's EC number. This is the exact failure mode [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) documents.
- **Assay artifact / promiscuity:** The in-vitro activity is consistent with intrinsic Sua5-fold promiscuity ([PMID:37427786](https://pubmed.ncbi.nlm.nih.gov/37427786/)) rather than a bona fide YciO function; it is not an artifact (reproducible) but is in-vivo-irrelevant.
- **Database carry-over risk:** A PMID-backed "experimental" IDA can look stronger than it is and propagate to orthologs/paralogs; flag it to prevent cascade annotation.
- **Alternative function:** [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) suggests YciO may act on a different substrate or require a missing partner — a genuinely open question; STRING links to YciV/YciQ/RluB are suggestive leads, not proof.

---

## Limitations and Knowledge Gaps

1. **What is YciO's real substrate/partner?** Checked: literature + genome-neighborhood + STRING. Matters because it defines the correct GO term. Resolve by: interaction screens/pulldowns, conditional phenotyping, structure-guided substrate docking; experimentally test the YciV/YciQ/RluB associations.
2. **Does any in-vivo condition reveal a t6A contribution?** Checked: no reported t6A phenotype for Δ*yciO*; TsaC essential/non-complementable. Resolve by: t6A LC-MS quantification in Δ*yciO* and under TsaC depletion/stress.
3. **Exactly what did [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) measure?** The annotation partly rests on ATP→AMP hydrolysis; direct TC-AMP product identification and kinetics matter because product detection is stronger evidence. Resolve by: inspecting the original assay (full text/SI not programmatically retrievable in this environment — stated plainly, not inferred).
4. **Exact kinetic parameters depend on one re-evaluation.** The ~0.14 nM/min vs ~2.8 µM/min comparison comes from [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) and was not independently re-run here. Resolve by: side-by-side kcat/Km under identical conditions.
5. **No structural superposition of active-site residues** was performed. A YciO vs TsaC overlay would quantify catalytic-residue conservation vs degradation. Resolve by: AlphaFold/experimental structure comparison focused on the TC-AMP active site.

---

## Discriminating Tests

- **Quantitative t6A LC-MS/MS** on WT, Δ*yciO*, TsaC-depleted, and Δ*yciO* + TsaC-depleted — directly tests any in-vivo t6A role. Predicted: no change in t6A for Δ*yciO*.
- **Complementation assay:** can plasmid-borne *yciO* (native and overexpressed) rescue a *tsaC*-depletion lethality? Predicted: no rescue (supports over-annotation). Single most decisive experiment.
- **Side-by-side steady-state kinetics** of YciO vs TsaC for TC-AMP (confirms the ~10⁴× gap).
- **Active-site residue audit:** structural/sequence comparison of the TC-AMP catalytic residues; degraded/substituted residues in YciO would mechanistically explain the weak activity.
- **Phylogenomic co-occurrence profiling** of the IPR052532 subfamily vs the t6A machinery to nominate YciO's true pathway (approach advocated in [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/)).
- **Interactomics / substrate screening** (alternative RNA or metabolite substrates) to identify YciO's real function.

---

## Proposed Follow-up Experiments / Actions (Curation Leads — require curator verification)

- **Action change:** Reclassify GO:0061710 on YciO from a core function to **in-vitro-only / non-core**, or remove as paralog over-annotation. Add an explicit caveat linking to [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/).
- **Candidate reference to add:** [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/) (de Crécy-Lagard et al., 2025; also bioRxiv doi:10.1101/2024.07.01.601547). Snippet to verify: *"current ML methods not only mostly fail to make novel predictions but also make basic logic errors in their predictions that human annotators avoid by leveraging the available knowledge base."* Full text reports the quantitative YciO vs TsaC rate gap (~0.14 nM/min vs ~2.8 µM/min) and non-complementation.
- **Supporting reference:** [PMID:19287007](https://pubmed.ncbi.nlm.nih.gov/19287007/). Snippet to verify: *"prove that yrdC is essential in E. coli"* (establishes TsaC essentiality / non-redundancy with YciO).
- **Provenance of source IDA:** [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/). Snippet to verify: *"We experimentally validated the enzymatic activities predicted for three proteins (YgfF, YciO, and YjdM)."*
- **Name/annotation lead:** Flag the UniProt recommended name "Threonylcarbamoyl-AMP synthase YciO" as over-reaching; prefer "YciO, TsaC/Sua5-family protein of unknown function (paralog of TsaC)."
- **Suggested curator questions:** (1) Did [PMID:37963869](https://pubmed.ncbi.nlm.nih.gov/37963869/) detect the TC-AMP product or only ATP→AMP hydrolysis? (2) Should a qualifier or NOT-annotation be used given ~10⁴× weaker activity and no in-vivo phenotype? (3) Should the IDA be flagged to block paralog/ortholog propagation?
- **Suggested experiments:** t6A LC-MS in Δ*yciO*; *yciO*→*tsaC* complementation; neighborhood-guided pathway hypothesis for YciO's real function.

---

## Bottom Line

The seed hypothesis is **over-annotated**. YciO's TC-AMP synthase activity (GO:0061710) is a genuine but **vestigial, in-vitro-only paralog activity** — ~20,000-fold weaker than the true enzyme TsaC/YrdC, unable to complement essential *tsaC*, phenotypically silent for t6A, residing in a distinct InterPro subfamily (IPR052532) and a separate genomic/functional-network context from the t6A module (TsaB/TsaD/TsaE). It should **not** be curated as YciO's core function, the t6A biosynthesis BP term should **not** be assigned, and YciO's physiological role should be recorded as **unknown**.

---

*Computational note:* UniProt records and sequences were retrieved programmatically; the YciO–TsaC identity (~35–40%) was computed by Needleman–Wunsch alignment, and the ~20,000×/4.3-orders activity gap was computed locally from rates reported in [PMID:40703034](https://pubmed.ncbi.nlm.nih.gov/40703034/). STRING-db v12 partner scores were retrieved for *E. coli* K-12 (taxon 511145). Full-text PDFs could not be parsed programmatically in this environment; this is stated plainly rather than inferred.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist yciO GO decision table](openscientist_artifacts/provenance_yciO_GO_decision_table.csv)
- [OpenScientist yciO evidence matrix](openscientist_artifacts/provenance_yciO_evidence_matrix.csv)
- [OpenScientist yciO vs tsaC STRING partners](openscientist_artifacts/provenance_yciO_vs_tsaC_STRING_partners.csv)
- [OpenScientist yciO vs tsaC activity](openscientist_artifacts/provenance_yciO_vs_tsaC_activity.csv)