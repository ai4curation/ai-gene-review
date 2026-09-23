---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T19:14:43.882849'
end_time: '2026-09-20T19:42:36.987345'
duration_seconds: 1673.1
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: statC
  gene_symbol: statC
  uniprot_accession: Q54BD4
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: proliferation-and-defense-response
  hypothesis_text: Dictyostelium discoideum statC participates in regulation of cell
    population proliferation (GO:0042127) and defense response (GO:0006952). Adjudicate
    each separately using actual GO definitions, primary Dictyostelium experiments,
    and phylogenetic conservation. Distinguish developmental differentiation, growth/proliferation,
    stress adaptation, and defense. Establish which steps this transcription factor
    itself contributes to each candidate process.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DICDI/statC/statC-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Dictyostelium discoideum statC participates in\
    \ regulation of cell population proliferation\n  (GO:0042127) and defense response\
    \ (GO:0006952). Adjudicate each separately using actual GO definitions,\n  primary\
    \ Dictyostelium experiments, and phylogenetic conservation. Distinguish developmental\
    \ differentiation,\n  growth/proliferation, stress adaptation, and defense. Establish\
    \ which steps this transcription factor\n  itself contributes to each candidate\
    \ process.\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: statC_GO_decision_table.csv
  path: openscientist_artifacts/statC_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist statC GO decision table
- filename: statC_evidence_matrix.csv
  path: openscientist_artifacts/statC_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist statC evidence matrix
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** DICDI
- **Taxon:** Dictyostelium discoideum (NCBITaxon:44689)
- **Gene directory:** statC
- **Gene symbol:** statC
- **UniProt accession:** Q54BD4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** proliferation-and-defense-response
- **Source file:** genes/DICDI/statC/statC-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Dictyostelium discoideum statC participates in regulation of cell population proliferation (GO:0042127) and defense response (GO:0006952). Adjudicate each separately using actual GO definitions, primary Dictyostelium experiments, and phylogenetic conservation. Distinguish developmental differentiation, growth/proliferation, stress adaptation, and defense. Establish which steps this transcription factor itself contributes to each candidate process.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Dictyostelium discoideum statC participates in regulation of cell population proliferation
  (GO:0042127) and defense response (GO:0006952). Adjudicate each separately using actual GO definitions,
  primary Dictyostelium experiments, and phylogenetic conservation. Distinguish developmental differentiation,
  growth/proliferation, stress adaptation, and defense. Establish which steps this transcription factor
  itself contributes to each candidate process.
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

# AIGR Gene Hypothesis Deep Research — *Dictyostelium discoideum* statC (Q54BD4)

**Focus:** function_assignment · **Hypothesis slug:** proliferation-and-defense-response
**Target:** statC / Dd‑STATc / dstC (UniProt Q54BD4; dictyBase DDB_G0293532; 931 aa)
**Candidate GO terms under adjudication:** GO:0042127 (regulation of cell population proliferation), GO:0006952 (defense response)

---

## Summary

**Executive verdict: over-annotated / refuted for both candidate terms.** Neither GO:0042127 (regulation of cell population proliferation) nor GO:0006952 (defense response) is supported by *Dictyostelium* experimental evidence for statC. Both terms are attached to statC exclusively by phylogenetically-inferred annotation (IBA, ECO:0000318, GO_REF:0000033) propagated from the metazoan STAT clade through PANTHER node PTN000927860. The "with/from" evidence sets for these IBA calls point to animal STATs (human STAT1 P42224, STAT2 P52630, STAT5A P42229) and — critically for the proliferation term — to the *Dictyostelium* paralog statB/dstB, **not** to any experimental result on statC itself.

When the two terms are adjudicated separately, as the seed hypothesis demands, they fail for different reasons. **GO:0042127 is a paralog carry-over:** the only experimentally supported proliferation phenotype among the three *Dictyostelium* STATs belongs to statB/dstB (Q70GP4), whose null cells are gradually outcompeted in co-culture with wild-type ([PMID:14701681](https://pubmed.ncbi.nlm.nih.gov/14701681/), IMP). statC and statA carry the same term only by IBA. **GO:0006952 has no experimental basis in any *Dictyostelium* STAT:** genuine amoebal anti-bacterial defense is executed by sentinel (S) cells via the TIR-domain protein TirA and ROS-generating NADPH oxidases ([PMID:26927887](https://pubmed.ncbi.nlm.nih.gov/26927887/); [PMID:17673666](https://pubmed.ncbi.nlm.nih.gov/17673666/)), a machinery in which statC is not implicated. STATc's only documented relationship to oxidative conditions is as a stress-activated transcription factor (GO:0006979, IDA), not as an effector of pathogen defense.

By contrast, statC's experimentally supported core function is clear and well-documented: it is a **stress-activated, DNA-binding transcription factor** governing the transcriptional response to hyperosmotic, heat, oxidative, and DIF‑1 (prestalk-inducer) signals, and it directs prestalk cell differentiation and sorocarp morphogenesis during development. Activation is non-canonical — driven by inhibition of the tyrosine phosphatase PTP3 rather than by the metazoan JAK/cytokine-receptor cascade. Because the interferon/cytokine-driven proliferation and immune-defense functions of animal STATs depend on exactly that receptor system, which *Dictyostelium* lacks, the phylogenetic transfer of these two functions to statC is mechanistically unjustifiable. The recommended curation action is to remove or de-prioritize (mark non-core / NOT) GO:0042127 and GO:0006952 on statC, retaining the well-supported stress-response and developmental transcription-factor annotations.

---

## Key Findings

### F001 — Both candidate terms are IBA-only carry-overs from animal STATs with zero *Dictyostelium* experimental support

QuickGO retrieval for Q54BD4 (39 annotations) shows that **GO:0042127 (regulation of cell population proliferation) is annotated solely by IBA** (ECO:0000318, GO_REF:0000033, PANTHER PTN000927860), with a with/from set consisting of animal STATs including human STAT1 (P42224) and STAT5A (P42229). Likewise, **GO:0006952 (defense response) is annotated solely by IBA** (same PANTHER node), with a with/from set of human STAT1 (P42224) and STAT2 (P52630). Neither term carries any IDA, IMP, IEP, or HDA experimental annotation in *D. discoideum*.

This matters because the same QuickGO record shows that **every experimental annotation statC actually possesses concerns stress response or development**, not proliferation or defense:

| GO term | Description | Evidence | Reference |
|---|---|---|---|
| GO:0006972 | response to osmotic stress | IEP / IDA | [PMID:17517120](https://pubmed.ncbi.nlm.nih.gov/17517120/), [PMID:12771188](https://pubmed.ncbi.nlm.nih.gov/12771188/) |
| GO:0006979 | response to oxidative stress | IDA | [PMID:12771188](https://pubmed.ncbi.nlm.nih.gov/12771188/) |
| GO:0009408 | response to heat | IDA | [PMID:12771188](https://pubmed.ncbi.nlm.nih.gov/12771188/) |
| GO:0006970 | response to osmotic stress | IMP | [PMID:22944283](https://pubmed.ncbi.nlm.nih.gov/22944283/) |
| GO:1903013 | response to DIF-1 | HDA | [PMID:25518940](https://pubmed.ncbi.nlm.nih.gov/25518940/) |
| GO:0031288 | sorocarp morphogenesis | IMP | [PMID:11336701](https://pubmed.ncbi.nlm.nih.gov/11336701/) |
| GO:0045892 | negative regulation of transcription | IMP | — |
| GO:0010628 | positive regulation of gene expression | IMP | [PMID:24587195](https://pubmed.ncbi.nlm.nih.gov/24587195/) |

The absence of any experimental evidence for the two candidate terms, contrasted against a rich set of experimental stress/development annotations, is the single most decisive observation for curation: the candidate terms are computational inferences layered onto a gene whose genuine, assayed function lies elsewhere.

### F002 — *Dictyostelium* defense response is executed by TirA + NADPH oxidases in sentinel cells, not by STATc

The defense-response term can be independently refuted by identifying what actually performs anti-bacterial defense in *Dictyostelium*. Zhang et al. ([PMID:26927887](https://pubmed.ncbi.nlm.nih.gov/26927887/)) demonstrated that Sentinel (S) cells of the multicellular slug produce extracellular DNA traps that trap and kill bacteria in a reactive-oxygen-species–dependent manner, and that this requires the **Toll/Interleukin-1 receptor domain-containing protein TirA** and **ROS-generating NADPH oxidases**; disruption of these genes decreased clearance of bacterial infection. Chen et al. ([PMID:17673666](https://pubmed.ncbi.nlm.nih.gov/17673666/)) originally identified sentinel cells and TirA as the immune-like detoxification/defense machinery. **STATc appears in neither study.** Its only mechanistic link to oxidative conditions is as a stress-activated transcription factor (GO:0006979, IDA, [PMID:12771188](https://pubmed.ncbi.nlm.nih.gov/12771188/)) — i.e., it responds to oxidative *stress* as a general environmental cue, which is categorically distinct from executing a *defense response* against a pathogen. Conflating "responds to oxidative stress" with "defense response" would be a category error; the GO defense-response branch (GO:0006952) concerns responses to attack by another organism or injury, a process for which no statC evidence exists.

### F003 — Canonical STAT domain architecture, but within a Dictyostelid-specific expansion; the proliferation IBA also draws on paralog dstB

UniProt Q54BD4 (gene *dstC*, dictyBase DDB_G0293532, 931 aa) has a bona fide STAT domain architecture: an N-terminal intrinsically disordered region carrying a DIF-inducible nuclear-import signal (aa ~6–46), a *Dictyostelium* STAT coiled-coil (Pfam PF09267), a STAT DNA-binding domain of the p53-like/RHD fold (InterPro IPR008967/IPR037059), an EF-hand (PF17901), a STATa_Ig domain (PF18214), and a C-terminal SH2 domain (aa ~802–931; PF00017). It is assigned to PANTHER family PTHR11801 (STAT1 family). So statC *is* a genuine STAT by sequence.

However, the three *Dictyostelium* STATs (dstA = O00910, dstB = Q70GP4, dstC = Q54BD4) form a **lineage-specific expansion**, and only the shared transcription-factor module is truly homologous to the metazoan proteins. The domains that in animals couple STATs to cytokine/interferon receptors and the JAK kinases — the functional substrate for proliferation and immune-defense signaling — have no counterpart pathway in *Dictyostelium*. statC is instead activated by a **non-canonical PTP3 phosphatase-inhibition switch** ([PMID:12771188](https://pubmed.ncbi.nlm.nih.gov/12771188/), [PMID:20159963](https://pubmed.ncbi.nlm.nih.gov/20159963/)): stress-induced serine phosphorylation of the tyrosine phosphatase PTP3 inhibits its activity toward STATc, allowing a semi-constitutive tyrosine kinase to phosphorylate and activate STATc. Notably, the IBA with/from set for GO:0042127 includes *Dictyostelium* DDB_G0268638 = dstB (STATb) alongside the animal STATs — direct evidence that the proliferation annotation on statC is being propagated in part from its own paralog.

### F004 — The proliferation term is paralog over-annotation from statB; defense response has no experimental support in ANY *Dictyostelium* STAT

This is the decisive discriminating finding. QuickGO shows that the paralog **dstB (STATb, Q70GP4) carries an experimental IMP annotation to GO:0042127** derived from Zhukovskaya et al. ([PMID:14701681](https://pubmed.ncbi.nlm.nih.gov/14701681/)), which reports that "Dd-STATb ... has a subtle role in growth, so that Dd-STATb-null cells are gradually lost from the population when they are co-cultured with parental cells." statC (dstC) and statA carry GO:0042127 **only by IBA** (GO_REF:0000033). In other words, the one real proliferation phenotype in the *Dictyostelium* STAT family belongs to a *different* gene, and the annotation has been phylogenetically spread to its paralogs — the textbook signature of paralog over-annotation.

For GO:0006952 (defense response), all three *Dictyostelium* STATs (dstA, dstB, dstC) are annotated **only by IBA**, propagated from animal STAT1/STAT2. No experimental *Dictyostelium* defense-response annotation exists for any of them. The defense-response term therefore fails not just for statC specifically but for the entire *Dictyostelium* STAT clade.

---

## Mechanistic Model / Interpretation

The core of the adjudication is separating **what statC directly does** from **what has been computationally attributed to it by homology**. The following model summarizes the evidence.

```
   METAZOAN STATs (STAT1/2/5A)                 DICTYOSTELIUM statC (Dd-STATc/dstC)
   ─────────────────────────────              ─────────────────────────────────────
   Cytokine / IFN receptor + JAK               NO cytokine receptor / NO JAK pathway
              │                                            │
              ▼                                            ▼
   Receptor-driven Tyr-P of STAT                Stress (osmotic/heat/oxidative) or DIF-1
              │                                            │
              │                                  PTP3 phosphatase INHIBITED (S448/S747-P)
              │                                            │
              ▼                                            ▼
   Dimerize → nucleus → transcription           Semi-constitutive kinase Tyr-P STATc
              │                                  → dimerize → nucleus → transcription
              ▼                                            ▼
   ┌──────────────────────────┐                 ┌────────────────────────────────────┐
   │ Cell proliferation        │                │ Stress-response gene program        │
   │ Immune / defense response │   ══╗          │ (gapA, rtoA ...)                    │
   │ (GO:0042127, GO:0006952)  │     ║ IBA       │ Prestalk (pstO) differentiation      │
   └──────────────────────────┘     ║ transfer  │ Sorocarp / culmination morphogenesis │
                                     ╚═════════▶ │ (GO:0006979/0006970/0009408/0031288) │
                                   (NOT valid —  └────────────────────────────────────┘
                                    no shared      ▲
                                    upstream       │ real proliferation phenotype lives in
                                    pathway)       │ PARALOG statB/dstB (PMID:14701681)
```

The immediate molecular function under test is **sequence-specific DNA-binding transcription-factor activity acting downstream of a stress/DIF‑1 signal**. Everything statC does experimentally is a transcriptional response to environmental or developmental cues. The candidate proliferation and defense functions are neither immediate activities nor even downstream phenotypes documented in statC mutants — they are inferences transferred across a homology boundary that does not carry the required upstream signaling context (cytokine receptors, JAKs, interferon response). Because the transfer crosses a mechanistic discontinuity, the resulting annotations are not merely "context-specific" or "downstream" — they are unsupported.

**Adjudication of each candidate term separately, as the seed required:**

| Candidate term | Mechanism required in metazoa | Present in *Dictyostelium*? | Experimental statC evidence? | Verdict |
|---|---|---|---|---|
| GO:0042127 regulation of cell population proliferation | Cytokine/JAK-driven growth signaling | No JAK/cytokine system | None (IBA only; real phenotype in paralog statB) | **Refuted for statC — paralog carry-over** |
| GO:0006952 defense response | IFN/immune receptor signaling | Defense done by TirA + NADPH oxidase sentinel cells | None (IBA only in all 3 STATs) | **Refuted — no evidence in any Dicty STAT** |
| (statC's real role) stress-activated TF / prestalk differentiation | — | Yes, via PTP3 switch | Multiple IDA/IMP/IEP/HDA | **Supported — core function** |

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| QuickGO record for Q54BD4 (database) | Review/database | Refutes (both terms) | Are GO:0042127 & GO:0006952 experimentally supported on statC? | Both terms IBA-only (ECO:0000318, GO_REF:0000033, PTN000927860); with/from = animal STATs + paralog dstB | Annotation metadata, *D. discoideum* | High for annotation provenance; depends on current QuickGO state |
| [14701681](https://pubmed.ncbi.nlm.nih.gov/14701681/) | Mutant phenotype (IMP) | Competing / refutes statC proliferation | Which *Dictyostelium* STAT has a proliferation phenotype? | Dd-STATb-null cells gradually lost in co-culture with parental — subtle growth role | statB/dstB, vegetative growth | High; phenotype is subtle and belongs to paralog, not statC |
| [26927887](https://pubmed.ncbi.nlm.nih.gov/26927887/) | Mutant phenotype / direct assay | Refutes statC defense role | What executes anti-bacterial defense in *Dictyostelium*? | Sentinel-cell DNA extracellular traps require TirA + NADPH oxidases; disruption ↓ bacterial clearance | Slug sentinel cells | High; statC not implicated |
| [17673666](https://pubmed.ncbi.nlm.nih.gov/17673666/) | Mutant phenotype | Refutes statC defense role | Identity of immune-like defense machinery | Sentinel cells + TirA provide detoxification/immune-like function | Slug, vegetative amoebae | High; statC absent |
| [12771188](https://pubmed.ncbi.nlm.nih.gov/12771188/) | Direct assay (IDA) | Supports core stress-TF role | Does STATc mediate stress transcriptional response? | STATc activated by osmotic/heat/oxidative stress and DIF; drives gapA, rtoA induction | *D. discoideum* cells | High; establishes stress-response, not defense |
| [17517120](https://pubmed.ncbi.nlm.nih.gov/17517120/) | Expression profiling (IEP) | Supports core stress-TF role | STATc's role in hyperosmotic response | ~20% of osmotic-stress-regulated genes are STATc-dependent | Microarray, sorbitol stress | High |
| [20159963](https://pubmed.ncbi.nlm.nih.gov/20159963/) | Direct assay | Qualifies (mechanism) | How is STATc activated? | Non-canonical activation: PTP3 inhibition via S448/S747 phosphorylation; cGMP + Ca²⁺ second messengers | *D. discoideum* | High; confirms no JAK/cytokine route |
| [24587195](https://pubmed.ncbi.nlm.nih.gov/24587195/) | Direct assay (IMP) | Supports core stress-TF role | Upstream kinases of STATc | Pyk3/Phg2 regulate STATc phosphorylation via PTP3; STATc positively regulates its own gene set | *D. discoideum* | High |
| [11336701](https://pubmed.ncbi.nlm.nih.gov/11336701/) | Mutant phenotype (IMP) | Supports core developmental role | STATc's developmental function | Regulates early development speed, terminal differentiation timing, ecmA prestalk expression | Developing slug | High; developmental TF, not proliferation |
| UniProt/InterPro/PANTHER (Q54BD4) | Structural/evolutionary | Qualifies | Is statC a genuine STAT? | Canonical STAT architecture (coiled-coil, DBD, SH2) but in Dictyostelid-specific expansion; PTHR11801 | Sequence/domain | High for domains; homology ≠ functional transfer |

---

## GO Curation Implications

**Lead requiring curator verification.** The evidence supports the following curation actions on statC (Q54BD4):

- **GO:0042127 (regulation of cell population proliferation) — BP.** Recommend **removal or reclassification to non-core / NOT**. It is an IBA-only annotation whose with/from set includes the paralog statB/dstB, which holds the only experimental proliferation phenotype in the family. This is paralog over-annotation. If policy retains IBA calls, at minimum flag it as non-core and add a curator note that the experimental evidence is paralog-specific (statB, PMID:14701681).
- **GO:0006952 (defense response) — BP.** Recommend **removal or NOT**. IBA-only in all three *Dictyostelium* STATs, propagated from animal STAT1/STAT2. No experimental support in any *Dictyostelium* STAT; genuine defense is a TirA/NADPH-oxidase sentinel-cell function (PMID:26927887, 17673666). Do not conflate with statC's oxidative-*stress* response (GO:0006979).
- **Retain (well-supported, core):** response to osmotic stress (GO:0006972/0006970), response to oxidative stress (GO:0006979), response to heat (GO:0009408), response to DIF-1 (GO:1903013), sorocarp morphogenesis (GO:0031288), and transcription-regulator activities (GO:0045892 negative regulation of transcription; GO:0010628 positive regulation of gene expression). These reflect the gene product's primary MF (DNA-binding transcription factor activity) and BP (stress-response transcription; prestalk differentiation).
- **MF anchor:** The most informative molecular-function term is **sequence-specific DNA-binding transcription factor activity** acting in stress/DIF‑1 response — not "protein binding."

---

## Mechanistic Scope

The immediate molecular activity being tested is that of a **latent, cytoplasmic-to-nuclear DNA-binding transcription factor**. On receipt of a stress or DIF‑1 signal, statC is tyrosine-phosphorylated, dimerizes, translocates to the nucleus (via an N-terminal import signal, with DIF-regulated nuclear export control; [PMID:12506009](https://pubmed.ncbi.nlm.nih.gov/12506009/)), and activates or represses target genes. That is the direct gene-product activity. Everything else attributed to statC is downstream of this transcriptional switch. The two candidate GO terms fall outside even this downstream scope:

- **Proliferation (GO:0042127)** would require statC transcription to regulate cell-cycle or growth-fitness genes in a demonstrated manner. No such statC regulon or statC-null growth phenotype is documented; the closest evidence is the paralog statB's subtle competitive-growth defect.
- **Defense response (GO:0006952)** would require statC to be an effector or transcriptional driver of an anti-pathogen program. Instead, defense is a distinct cellular module (sentinel cells, TirA, NADPH oxidases). statC's oxidative-stress responsiveness is a generic environmental-stress adaptation, not a pathogen-directed defense process.

Thus both candidate terms are separated from statC's genuine activity by at least one, and in the defense case an entire, mechanistic discontinuity.

---

## Conflicts and Alternatives

1. **Paralog confusion (primary alternative explanation).** The strongest alternative interpretation of the proliferation annotation is that it is genuine — *for statB, not statC*. The IBA with/from set explicitly lists dstB (Q70GP4), and the experimental IMP annotation (PMID:14701681) is on statB. Any curator retaining GO:0042127 on statC should recognize this as carry-over from a paralog.
2. **Stress vs. defense category boundary.** statC is IDA-annotated to oxidative-stress response (GO:0006979). A curator could be tempted to treat this as evidence for defense response. This is an alternative that the evidence refutes: responding to oxidative stress as an environmental cue is distinct from mounting a defense response against a pathogen. The two GO branches are separate for good reason.
3. **Organism-specific signaling discontinuity.** Metazoan STAT proliferation/immune roles depend on cytokine/interferon receptors and JAK kinases, absent in *Dictyostelium*. statC is activated by a phosphatase-inhibition switch (PTP3), a mechanism unrelated to the receptor systems that drive the metazoan functions. Homology of the DNA-binding/SH2 module does not license transfer of the receptor-context-dependent functions.
4. **Database carry-over.** Both candidate terms trace to a single PANTHER node (PTN000927860). This is a systematic propagation, not independent lines of evidence, so it should be weighted as one inference, not several.

---

## Limitations and Knowledge Gaps

- **Annotation snapshot dependency.** The provenance analysis relies on the QuickGO/UniProt annotation state at the time of retrieval. Curators should re-verify current evidence codes and with/from sets, as PANTHER-based IBA propagation is periodically re-computed.
- **No statC proliferation assay has been reported.** The gap is not that statC was tested and found negative for proliferation — it is that it appears never to have been directly assayed for a growth/proliferation phenotype in a controlled competition experiment analogous to the statB study. A statC-null co-culture competition assay would resolve whether statC has any statB-like subtle growth role.
- **No statC bacterial-clearance assay.** statC has not been tested in sentinel-cell/ET or bacterial-killing assays. Its role (if any) in defense is untested rather than experimentally excluded, though the mechanistic evidence points strongly to TirA/NADPH oxidases as the effectors.
- **Structure/PANTHER details inferred from database records**, not from a locally executed structural alignment. Domain boundaries and family assignment are as reported by UniProt/InterPro/PANTHER; independent HMM/structure verification was not run programmatically here.
- **Possible indirect roles.** Because statC broadly reprograms transcription under stress, an indirect contribution to population fitness under specific stresses cannot be formally excluded — but "indirect fitness effect under stress" is not equivalent to the specific GO terms GO:0042127 or GO:0006952.

---

## Discriminating Tests

To most efficiently separate the seed hypothesis from the paralog-carry-over / stress-TF alternative:

1. **statC-null vs. parental co-culture competition assay** (mirroring PMID:14701681 for statB). If statC-null cells are *not* progressively outcompeted, GO:0042127 on statC is refuted experimentally, not just by provenance.
2. **statC involvement in sentinel-cell extracellular traps / bacterial clearance** (mirroring PMID:26927887). Assay bacterial clearance and ET formation in statC-null slugs. Expected result: no defect (defense is TirA/NADPH-oxidase driven), directly testing GO:0006952.
3. **Comparative annotation audit across the STAT1 PANTHER family** (PTN000927860) to quantify how many non-metazoan members receive proliferation/defense IBA terms — establishes whether this is systematic over-propagation warranting a family-level curation fix.
4. **ChIP-seq / RNA-seq of statC targets** under stress vs. growth to confirm that statC's regulon is dominated by stress/differentiation genes (gapA, rtoA, ecmA) rather than cell-cycle or immune-effector genes.
5. **Cross-check statB and statA** annotations: verify that statB retains its experimental GO:0042127 and that statA's GO:0042127 is likewise IBA-only, consolidating the paralog-source interpretation.

---

## Proposed Follow-up Actions / Curation Leads

*All items below are leads requiring curator verification.*

- **Action change (GO:0042127 on statC):** Change from active annotation to **removed / non-core / NOT**. Rationale snippet to verify against PMID:14701681: *"Dd-STATb ... has a subtle role in growth, so that Dd-STATb-null cells are gradually lost from the population when they are co-cultured with parental cells."* — establishes the phenotype belongs to the paralog statB, not statC.
- **Action change (GO:0006952 on statC):** Change to **removed / NOT**. Rationale snippets to verify: PMID:26927887 *"The production of ETs by S cells requires a Toll/Interleukin-1 receptor domain-containing protein TirA and reactive oxygen species-generating NADPH oxidases. Disruption of these genes results in decreased clearance of bacterial infections."*; PMID:17673666 *"A Toll/interleukin-1 receptor (TIR) domain protein, TirA, was also required for some S cell functions."* — defense executed by TirA/NADPH oxidase, not STATc.
- **Retain as core:** stress-response (GO:0006979 IDA, PMID:12771188 — *"hyperosmotic stress, heat shock and oxidative stress also activate Dd-STATc"*) and developmental/prestalk transcription-factor roles (GO:0031288 IMP, PMID:11336701 — *"a Dictyostelium STAT, Dd-STATc, which regulates the speed of early development and the timing of terminal differentiation"*).
- **Candidate curator note:** "GO:0042127 and GO:0006952 on statC derive from a single metazoan-STAT PANTHER IBA propagation (PTN000927860); with/from includes paralog dstB and animal STAT1/2/5A. No *Dictyostelium* experimental support for either term on any of dstA/dstB/dstC except the statB-specific IMP growth phenotype."
- **Suggested questions for curator:** (1) Does project policy retain IBA-only calls when the with/from includes an in-organism paralog with the experimental phenotype? (2) Should the defense-response term be corrected family-wide across dstA/dstB/dstC?
- **Suggested experiments:** statC-null competitive growth assay; statC-null bacterial-clearance/ET assay (see Discriminating Tests 1–2).

---

## Bottom Line

statC is a genuine STAT-family, stress- and DIF‑1-activated DNA-binding transcription factor that drives *Dictyostelium* stress-response gene expression and prestalk differentiation via a non-canonical PTP3 phosphatase switch. Its two candidate annotations — regulation of cell population proliferation and defense response — are **over-annotations**: both are IBA-only, propagated from metazoan STATs (and, for proliferation, from the paralog statB) across a signaling-context boundary (no JAK/cytokine/interferon system) that invalidates the functional transfer. The recommended lead is removal or non-core reclassification of GO:0042127 and GO:0006952 on statC, pending curator verification.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist statC GO decision table](openscientist_artifacts/statC_GO_decision_table.csv)
- [OpenScientist statC evidence matrix](openscientist_artifacts/statC_evidence_matrix.csv)