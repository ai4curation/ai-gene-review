---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T01:56:23.864117'
end_time: '2026-11-09T02:08:39.020007'
duration_seconds: 735.16
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: mouse
  gene: G6pc2
  gene_symbol: G6pc2
  uniprot_accession: Q9Z186
  taxon_id: NCBITaxon:10090
  taxon_label: Mus musculus
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0006094
  hypothesis_text: G6pc2 has gluconeogenesis (GO:0006094).
  term_context: '- Term: gluconeogenesis (GO:0006094)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033

    - file:mouse/G6pc2/G6pc2-deep-research-claude-code.md

    - PMID:32213654

    - PMID:23274894

    - PMID:10078553

    - PMID:25552595'
  source_file: genes/mouse/G6pc2/G6pc2-ai-review.yaml
  source_selector: existing_annotations[11].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0006094\n  label: gluconeogenesis\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033"
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

- **Organism code:** mouse
- **Taxon:** Mus musculus (NCBITaxon:10090)
- **Gene directory:** G6pc2
- **Gene symbol:** G6pc2
- **UniProt accession:** Q9Z186

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0006094
- **Source file:** genes/mouse/G6pc2/G6pc2-ai-review.yaml
- **Source selector:** existing_annotations[11].function_hypothesis

## Seed Hypothesis

G6pc2 has gluconeogenesis (GO:0006094).

## Term and Decision Context

- Term: gluconeogenesis (GO:0006094)
- Evidence type: IBA
- Original reference: GO_REF:0000033

## Reference Context

- GO_REF:0000033
- file:mouse/G6pc2/G6pc2-deep-research-claude-code.md
- PMID:32213654
- PMID:23274894
- PMID:10078553
- PMID:25552595

## Source Context YAML

```yaml
term:
  id: GO:0006094
  label: gluconeogenesis
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


## Output

# G6pc2 Gluconeogenesis (GO:0006094) — Function-Assignment Hypothesis Review

**Target gene:** *G6pc2* (IGRP, islet-specific glucose-6-phosphatase catalytic subunit-related protein), *Mus musculus* (NCBITaxon:10090), UniProt **Q9Z186**
**Focus:** function_assignment — "G6pc2 has gluconeogenesis (GO:0006094)"
**Annotation under review:** GO:0006094 (gluconeogenesis), evidence type **IBA**, original reference **GO_REF:0000033**
**Source:** `genes/mouse/G6pc2/G6pc2-ai-review.yaml` → `existing_annotations[11].function_hypothesis`

---

## Summary

The IBA (Inferred from Biological Ancestor) annotation of **gluconeogenesis (GO:0006094)** to mouse *G6pc2* is a **phylogenetic carry-over from the liver/kidney enzyme G6PC1**, and it mis-assigns the biological context of this gene product. G6pc2 is a close paralog of the gluconeogenic enzyme G6pc1 and retains a genuine glucose-6-phosphatase catalytic signature, which is why an ancestral-inference pipeline (GO_REF:0000033 = IBA/PAINT) transferred the liver-enzyme biological process onto it. However, three independent lines of evidence show that the gluconeogenesis BP does not describe G6pc2's physiology.

First, there is a **tissue mismatch**: G6pc2 is expressed essentially only in pancreatic islet β-cells and is absent from the gluconeogenic tissues — liver, kidney, and intestine — where net glucose synthesis and export occur. Gluconeogenesis in those peripheral tissues is served by the other isoforms G6pc1 and G6pc3. Second, the **demonstrated physiological function is different**: knockout and metabolic-flux studies show G6pc2's role is intracellular glucose cycling in the β-cell, hydrolyzing glucose-6-phosphate to oppose glucokinase and thereby tuning the glucose sensitivity of insulin secretion and setting fasting blood glucose — not the production of free glucose for release into the bloodstream. Third, G6pc2 catalyzes only a **single hydrolysis step within a futile cycle** in a cell that neither performs nor exports gluconeogenesis; it carries out no step of the defined PEPCK→FBPase→G6Pase gluconeogenic sequence.

The important nuance is that the **molecular function** term — glucose-6-phosphatase activity (GO:0004346, MF) — is strongly supported: the catalytic active site is fully conserved (56.5% identity to G6pc1; catalytic His and phosphate-binding Arg intact). The correct curation outcome is therefore not "G6pc2 has no enzymatic activity," but rather "G6pc2 has G6Pase MF, but its BP is β-cell glucose cycling / regulation of insulin secretion / glucose homeostasis, not gluconeogenesis." **Verdict: refuted / over-annotated as a Biological Process.** The gluconeogenesis BP should be removed or flagged as a non-core, paralog-driven IBA carry-over.

---

## Key Findings

### Finding 1 — G6pc2 is β-cell-specific and absent from gluconeogenic tissues

The single most decisive argument against the gluconeogenesis annotation is anatomical. Gluconeogenesis — the *de novo* synthesis of glucose from lactate, glycerol, and amino acids with subsequent release into the blood — is a property of hepatocytes, renal proximal-tubule cells, and enterocytes. G6pc2 is not expressed in any of these.

The original cloning paper [PMID: 10078553](https://pubmed.ncbi.nlm.nih.gov/10078553/) established that *"the mRNA was highly expressed in pancreatic islets and expressed more in beta-cell lines than in an alpha-cell line. It was notably absent in tissues and cell lines of non-islet neuroendocrine origin."* This directly excludes the liver and kidney tissues where gluconeogenesis takes place. The UniProt record for Q9Z186 reinforces the same conclusion, describing the protein as *"Specifically expressed in pancreatic islet cells... Not detected in testis, kidney, muscle, liver, lung, spleen, brain."*

A direct isoform comparison by Bosma et al. 2020 [PMID: 32213654](https://pubmed.ncbi.nlm.nih.gov/32213654/) quantified this distribution: *"expression of G6pc1 and/or G6pc3 are much greater than G6pc2 in peripheral tissues, whereas G6pc2 expression is much higher than G6pc3 in both pancreas and islets."* In other words, the tissues that actually perform gluconeogenesis rely on **G6pc1 and G6pc3**, while **G6pc2** is the islet-restricted member of the family. Beta-cell-specific deletion of *G6pc2* alone is sufficient to lower fasting blood glucose, confirming that the islet is the physiologically relevant site of G6pc2 action.

**Interpretation:** A gene product that is not present in gluconeogenic organs cannot participate in the organismal gluconeogenesis pathway. This is the core reason the IBA transfer is biologically inappropriate.

### Finding 2 — G6pc2's demonstrated function is β-cell glucose cycling that regulates insulin secretion

The validated physiology of G6pc2 is mechanistically distinct from gluconeogenesis. Pound et al. 2013 [PMID: 23274894](https://pubmed.ncbi.nlm.nih.gov/23274894/) characterized *G6pc2* knockout mice and concluded that *"G6pc2 represents a novel, negative regulator of basal GSIS that acts by hydrolyzing glucose-6-phosphate, thereby reducing glycolytic flux."* Here, G6P hydrolysis is not the terminal step of glucose export — it is one arm of a **substrate (futile) cycle** inside the β-cell that opposes glucokinase-driven glycolysis.

Bosma et al. 2020 [PMID: 32213654](https://pubmed.ncbi.nlm.nih.gov/32213654/) made the mechanism explicit, proposing *"a model in which G6PC2 regulates the sensitivity of GSIS to glucose by opposing the action of glucokinase."* In knockout islets, glucose-6-phosphatase activity and glucose cycling are abolished and glucose-stimulated insulin secretion is enhanced. Rahim et al. 2022 [PMID: 35176280](https://pubmed.ncbi.nlm.nih.gov/35176280/) extended this with metabolic flux analysis in βTC3 cells, showing that *G6pc2* deletion increased glycolytic and citric-acid-cycle fluxes by ~60% and roughly doubled glucose-stimulated insulin secretion and intracellular insulin content.

**Interpretation:** The enzyme's measurable output in its native cell is to blunt glycolytic flux and thereby raise the glucose threshold for insulin secretion. This is a **regulatory / glucose-homeostasis** function — captured by BP terms such as regulation of insulin secretion and glucose homeostasis — categorically different from the anabolic "make-and-release glucose" meaning of gluconeogenesis.

### Finding 3 — The G6Pase catalytic signature is conserved, which explains (but does not justify) the IBA transfer

To confirm why an ancestral-inference pipeline would transfer the liver-enzyme BP, a pairwise global alignment of the canonical mouse paralogs was computed. G6pc1 (P35576, 357 aa) vs G6pc2 (Q9Z186, 355 aa) share **56.5% identity**; G6pc2 vs G6pc3 (Q6NSQ9) share **49.4%**. All three conserve the PAP2/acid-phosphatase catalytic blocks:

- **C1** phosphate-binding motif `KWILFG(Q/H/D)RP` (catalytic Arg)
- **C2** `GSPSGHAM` (catalytic His — His119 / His115 / His114 across the three paralogs)
- **C-terminal** nucleophilic-His motif `HFPHQ` (G6pc1 `LSRIYLAAH-FPHQ`; G6pc2 `RVFIATH-FPHQ`; His176 / His174)

These values and motifs match the Arden et al. 1999 report [PMID: 10078553](https://pubmed.ncbi.nlm.nih.gov/10078553/) of ~50% identity with conserved catalytic residues. A sister study on the IGRP gene, Martin et al. [PMID: 10078554](https://pubmed.ncbi.nlm.nih.gov/10078554/), further emphasizes the reciprocal, tissue-exclusive promoter behavior: *"The IGRP and G-6-Pase catalytic subunit gene promoters show a reciprocal pattern of activity, with the IGRP promoter being approximately 150-fold more active than the G-6-Pase promoter in HIT cells"* — i.e., the two paralogs are built to operate in different tissues.

**Interpretation:** The conserved active site is exactly why GO_REF:0000033 (IBA/PAINT) propagated the ancestral "gluconeogenesis" BP. But sequence-level conservation of **molecular function** does not license transfer of the **biological process** when the gene has been recruited into a different tissue and pathway. The MF term (GO:0004346) should be retained; the BP term (GO:0006094) should not be inferred from it.

---

## Mechanistic Model / Interpretation

The distinction that matters for curation is **molecular function vs. biological process**, and **tissue context**.

```
          LIVER / KIDNEY / INTESTINE                 PANCREATIC ISLET β-CELL
          (gluconeogenic tissues)                    (G6pc2 / IGRP territory)
        ┌──────────────────────────┐               ┌───────────────────────────┐
        │  Gluconeogenesis pathway │               │  Glucose sensing / GSIS   │
        │  PEPCK → FBPase → G6Pase │               │                           │
        │                          │               │   glucose                 │
        │  G6P --G6PC1/G6PC3-->     │               │     │ GLUT2               │
        │        glucose --> BLOOD │               │     ▼                     │
        │  (NET glucose SYNTHESIS  │               │   glucose --GCK--> G6P    │
        │   and EXPORT)            │               │     ▲                │     │
        └──────────────────────────┘               │     └--G6PC2 (IGRP)--┘     │
                                                    │     (FUTILE glucose cycle)│
        GO:0006094 gluconeogenesis  YES             │     ▼ glycolysis           │
                                                    │   ATP/ADP ↑ -> insulin    │
                                                    │   secretion               │
                                                    └───────────────────────────┘
                                                    GO:0006094 gluconeogenesis  NO
                                                    Correct BP: regulation of
                                                    insulin secretion / glucose
                                                    homeostasis
```

Both G6pc1 and G6pc2 hydrolyze glucose-6-phosphate (shared **MF** = GO:0004346). In the liver, that hydrolysis is the terminal, committed step of gluconeogenesis, releasing free glucose to the blood. In the β-cell, the identical chemistry is wired into a **futile cycle against glucokinase**: glucose → G6P (glucokinase) → glucose (G6pc2), which dissipates a fraction of glucose-derived carbon, lowers glycolytic flux, and raises the glucose concentration needed to trigger insulin release. Deleting G6pc2 abolishes the counter-cycle, increases glycolytic/CAC flux, enhances GSIS, and lowers fasting blood glucose — the opposite physiological axis from gluconeogenesis.

| Attribute | G6pc1 (liver/kidney) | G6pc2 / IGRP (islet β-cell) |
|---|---|---|
| Molecular function | Glucose-6-phosphatase (GO:0004346) | Glucose-6-phosphatase (GO:0004346) |
| Catalytic site conserved | Yes | Yes (56.5% id; His/Arg intact) |
| Expression site | Liver, kidney, intestine | Pancreatic islet β-cells only |
| Biological process | Gluconeogenesis (export glucose) | β-cell glucose cycling → regulation of insulin secretion / glucose homeostasis |
| Net glucose synthesis/export | Yes | No |
| GO:0006094 appropriate? | Yes | **No — over-annotation** |

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 10078553](https://pubmed.ncbi.nlm.nih.gov/10078553/) | Localization / expression (original cloning) | **Refutes** BP | Is G6pc2 expressed in gluconeogenic tissues? | mRNA highly expressed in islets, more in β-cell than α-cell lines, "notably absent" from non-islet tissues | Mouse islets, β-/α-cell lines | High; mRNA-level, early study |
| [PMID: 32213654](https://pubmed.ncbi.nlm.nih.gov/32213654/) | Mutant phenotype + expression | **Refutes** BP / supports insulin-secretion BP | Isoform tissue distribution; β-cell KO effect | Peripheral tissues use G6pc1/G6pc3; G6pc2 islet-restricted; β-cell-specific KO lowers FBG; KO abolishes glucose cycling and enhances GSIS; "opposing the action of glucokinase" | Mouse, tissue qPCR + β-cell KO | High |
| [PMID: 23274894](https://pubmed.ncbi.nlm.nih.gov/23274894/) | Mutant phenotype (KO) | **Refutes** BP / defines true BP | What is G6pc2's physiological role? | "Negative regulator of basal GSIS that acts by hydrolyzing glucose-6-phosphate, thereby reducing glycolytic flux" | Mouse global KO islets | High |
| [PMID: 35176280](https://pubmed.ncbi.nlm.nih.gov/35176280/) | Direct assay (flux analysis) | **Qualifies** / supports true BP | Effect of G6pc2 loss on β-cell metabolism | KO raises glycolytic & CAC flux ~60%, doubles GSIS and insulin content | βTC3 murine β-cell line, CRISPR | High; cell line |
| [PMID: 10078554](https://pubmed.ncbi.nlm.nih.gov/10078554/) | Structural/promoter | **Qualifies** | Tissue exclusivity of paralog promoters | IGRP promoter ~150× more active than G6Pase promoter in islet HIT cells; reciprocal pattern | Mouse gene / islet vs liver cell lines | Medium-high |
| [PMID: 24142592](https://pubmed.ncbi.nlm.nih.gov/24142592/) | Review/database synthesis | **Supports** true BP | Functional role of G6PC2 | G6pc2 = negative regulator of basal GSIS opposing glucokinase; evolutionary benefit "unlikely to be related to its ability to modulate FBG" | Review | Medium (review-level) |
| [PMID: 26822088](https://pubmed.ncbi.nlm.nih.gov/26822088/) | Mechanistic (sorcin axis) | **Qualifies** | G6PC2 as GSIS regulator | G6PC2 is "a negative regulator of glucose-stimulated insulin secretion (GSIS)" | Mouse/human islets | Medium |
| Computed alignment (this report) | Structural/evolutionary | **Qualifies** (explains IBA) | Is the G6Pase active site conserved? | 56.5% id to G6pc1; catalytic His115/His174 + phosphate-binding Arg conserved | In silico, UniProt sequences | High for MF; does not license BP |

---

## GO Curation Implications

**Lead for curator verification (not an automated action):**

1. **GO:0006094 gluconeogenesis (BP, IBA, GO_REF:0000033) — REMOVE or FLAG as a non-core paralog carry-over.** The term is a phylogenetic inference from the gluconeogenic paralog G6PC1 and does not reflect G6pc2's demonstrated β-cell physiology. Experimental evidence (KO phenotype, flux analysis) and expression data place G6pc2 outside gluconeogenic tissues and outside the gluconeogenesis pathway.

2. **RETAIN glucose-6-phosphatase activity (GO:0004346, MF).** Well supported by conserved catalytic residues and the direct demonstration that loss of G6pc2 abolishes islet G6Pase activity ([PMID: 23274894](https://pubmed.ncbi.nlm.nih.gov/23274894/), [PMID: 32213654](https://pubmed.ncbi.nlm.nih.gov/32213654/)). This MF is the informative, defensible core function.

3. **ADD / RETAIN an accurate BP** reflecting the real physiology — candidates for curator selection:
   - **regulation of insulin secretion** (GO:0050796), or **negative regulation of insulin secretion involved in cellular response to glucose stimulus** (GO:0061179)
   - **glucose homeostasis** (GO:0042593)
   - These are directly supported by experimental (IMP/EXP) evidence from KO studies, which is stronger than the IBA inference being removed.

4. **CC:** endoplasmic reticulum membrane (GO:0005789) is appropriate for this integral-membrane G6Pase catalytic subunit and should be retained if present.

Because experimental (EXP/IMP) evidence directly contradicts the IBA-inferred BP, the general curation principle that experimental annotations supersede phylogenetic inference applies: the gluconeogenesis IBA should not stand.

---

## Mechanistic Scope

- **Immediate molecular activity tested:** hydrolysis of D-glucose-6-phosphate to D-glucose + inorganic phosphate — glucose-6-phosphatase activity. This is **confirmed** for G6pc2 at the sequence/active-site level and functionally (islet G6Pase activity is lost in KO).
- **Direct cellular function:** participation in an intracellular **glucose/G6P substrate cycle** in the β-cell that opposes glucokinase and modulates glycolytic flux.
- **Downstream phenotype (not direct activity):** altered glucose-stimulated insulin secretion and fasting blood glucose — physiological consequences of glucose-cycling activity, appropriately captured as "regulation of insulin secretion" / "glucose homeostasis."
- **Not supported as a direct function:** gluconeogenesis (net synthesis of glucose from non-carbohydrate precursors and its release into the circulation). G6pc2 performs no step of the PEPCK→FBPase→G6Pase gluconeogenic sequence in a gluconeogenic tissue.

The seed hypothesis conflates **shared molecular chemistry** (G6P hydrolysis) with **shared biological process** (gluconeogenesis). These are separable: the same reaction serves glucose export in the liver and flux regulation in the β-cell.

---

## Conflicts and Alternatives

- **Paralog confusion (the central issue):** G6pc2 is one of three mouse G6Pase catalytic-subunit genes (G6pc1, G6pc2, G6pc3). Only G6pc1 (and partly G6pc3) operate in gluconeogenic tissues. The IBA pipeline grouped all three under the ancestral gluconeogenic function. This is the textbook scenario of **paralog over-annotation via phylogenetic transfer**.
- **Database carry-over:** GO_REF:0000033 is the PAINT/IBA reference; the annotation originates from ancestral inference, not from any G6pc2-specific experiment. No primary paper assigns gluconeogenesis to G6pc2.
- **Alternative interpretation considered and rejected:** Could G6pc2's G6P hydrolysis count as "gluconeogenesis" loosely because it produces free glucose? No — within the β-cell the glucose produced re-enters the futile cycle and is not exported as net new glucose; the physiological readout is insulin-secretion tuning, not glucose output. The "glucose cycling" terminology used in the primary literature is explicitly distinct from gluconeogenesis.
- **Organism/isoform note:** Human G6PC2 (a GWAS fasting-glucose locus) mirrors the mouse biology — islet-restricted, insulin-secretion regulator — so the conclusion is not a mouse-specific artifact.

---

## Limitations and Knowledge Gaps

1. **Exact current review action is blinded.** We evaluated the hypothesis independently; if the existing review already removed/down-weighted the IBA, this report corroborates that. *Resolution:* curator inspection of the review YAML's decision field.
2. **Precise subcellular/topology annotation.** ER-membrane localization is inferred from paralogy and family membership; a G6pc2-specific localization experiment would strengthen the CC term. *Resolution:* immunolocalization or a validated proteomics dataset.
3. **Residual glucose output under extreme conditions.** No evidence suggests G6pc2 contributes measurable glucose output, but this has not been exhaustively excluded. *Resolution:* isotopic glucose-production flux in islets vs liver.
4. **Choice between competing BP terms.** Whether "regulation of insulin secretion," "negative regulation of insulin secretion involved in cellular response to glucose stimulus," or "glucose homeostasis" best fits is a curator judgment; all three are supportable. *Resolution:* GO term-granularity review against the KO phenotype papers.
5. The gluconeogenesis IBA is an inference, not a G6pc2-specific experimental claim; this review argues from absence of positive evidence plus strong contradicting phenotype data.
6. The computed sequence identity/active-site analysis establishes **MF conservation**, not BP; it is offered to explain the IBA, not to support gluconeogenesis.

---

## Proposed Follow-up Experiments / Actions (Discriminating Tests)

The hypothesis is already well discriminated by existing data, but the most efficient confirmatory analyses are:

1. **Tissue-expression cross-check (public):** Confirm in Tabula Muris / GTEx-equivalent mouse islet atlases and the Human Protein Atlas that G6PC2 expression is islet/β-cell-restricted and that G6PC1/G6PC3 carry liver/kidney/intestine — a one-figure confirmation that gluconeogenic tissues lack the gene.
2. **Isotope flux in KO islets vs hepatocytes:** Measure net glucose production ([U-¹³C] tracer) — gluconeogenic tissues release labeled glucose, islets do not; G6pc2 KO changes glycolytic/GSIS flux, not glucose output.
3. **Orthology/phylogeny with per-species function tags:** A PAINT-style tree annotated with experimental evidence would show the gluconeogenesis function is restricted to the G6PC1 clade, justifying pruning the BP from the G6PC2 branch.
4. **GO rule check:** Apply the taxon/evidence-conflict rule that experimental EXP/IMP annotations (insulin-secretion regulation) override an IBA (gluconeogenesis) when they describe mutually exclusive processes in the same gene product.

---

## Curation Leads (require curator verification)

**Candidate action change**
- Remove or demote GO:0006094 (gluconeogenesis, IBA, GO_REF:0000033) on G6pc2 (Q9Z186); treat as a paralog-driven phylogenetic over-annotation.

**Candidate GO terms to retain/add**
- **Retain:** GO:0004346 glucose-6-phosphatase activity (MF) — informative, well supported.
- **Retain (if present):** GO:0005789 endoplasmic reticulum membrane (CC).
- **Add (EXP/IMP-supported BP):** GO:0050796 regulation of insulin secretion and/or GO:0061179 negative regulation of insulin secretion involved in cellular response to glucose stimulus; GO:0042593 glucose homeostasis.

**Candidate references with snippets to verify**
- [PMID: 10078553](https://pubmed.ncbi.nlm.nih.gov/10078553/): *"the mRNA was highly expressed in pancreatic islets... It was notably absent in tissues and cell lines of non-islet neuroendocrine origin"* → excludes gluconeogenic tissues.
- [PMID: 32213654](https://pubmed.ncbi.nlm.nih.gov/32213654/): *"expression of G6pc1 and/or G6pc3 are much greater than G6pc2 in peripheral tissues, whereas G6pc2 expression is much higher... in both pancreas and islets"* and *"a model in which G6PC2 regulates the sensitivity of GSIS to glucose by opposing the action of glucokinase."*
- [PMID: 23274894](https://pubmed.ncbi.nlm.nih.gov/23274894/): *"G6pc2 represents a novel, negative regulator of basal GSIS that acts by hydrolyzing glucose-6-phosphate, thereby reducing glycolytic flux."*
- [PMID: 35176280](https://pubmed.ncbi.nlm.nih.gov/35176280/): KO raises glycolytic/CAC flux ~60% and doubles GSIS.

**Suggested curator questions**
- Does the review record already remove/flag the IBA? If so, confirm alignment.
- Is the ER-membrane CC term independently supported for G6pc2 or only by paralogy?
- Which single BP term best matches the KO phenotype at the desired granularity?

**Suggested experiments**
- Mouse islet vs liver [U-¹³C]glucose production flux ± G6pc2.
- Validated G6pc2 subcellular localization in primary β-cells.

---

## Bottom Line

Keep the molecular function (glucose-6-phosphatase activity) and add/retain the β-cell insulin-secretion / glucose-homeostasis biological process; **remove or flag the gluconeogenesis (GO:0006094) IBA annotation** as a paralog-driven carry-over from G6PC1 that does not reflect G6pc2's islet-restricted, insulin-regulating physiology.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)