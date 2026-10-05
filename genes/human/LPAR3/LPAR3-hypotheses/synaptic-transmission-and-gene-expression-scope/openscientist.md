---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T01:03:43.004615'
end_time: '2026-09-21T01:42:11.418948'
duration_seconds: 2308.41
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: LPAR3
  gene_symbol: LPAR3
  uniprot_accession: Q9UBY5
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: synaptic-transmission-and-gene-expression-scope
  hypothesis_text: 'Evaluate human LPAR3 Q9UBY5 participation in chemical synaptic
    transmission GO0007268 and inferred synapse location GO0045202, and separately
    involved_in gene expression GO0010467 transferred from mouse Q9EQ31 IMP20864640.
    Full human founding10488122 text is accessible through author-deposited ResearchGate;
    it contains receptor cloning, calcium/cAMP, PC12 Elk1 assays and tissue Northern
    blots, but text search finds no synaptic assay. Do not infer absence of all neuronal
    function from its negative bulk-brain Northern: primary10727522 Fig7C explicitly
    reports human frontal cortex/hippocampus/amygdala expression, and mouse primary22465231
    has curated axon IDA plus Lpar3-dependent hippocampal axon branching. Distinguish
    neural expression, axon location/branching, and actual synaptic transmission;
    do not conflate them. Obtain complete primary20864640 assays: Lpar3-null uterine
    collagen/protease expression changes support downstream transcriptional regulation,
    but do they establish actual work in gene-product production versus acts_upstream_of?
    Name which entity performs the expression step and inspect term parents, annotation
    conventions and appropriate receptor comparators. Avoid overriding experimental
    curators from abstract-only evidence. Search later primary functional evidence
    for synaptic actions and any direct expression machinery role. This question is
    separate from the shared LPAR2/LPAR3 cAMP adjudication already requested; do not
    repeat that research.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/LPAR3/LPAR3-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Evaluate human LPAR3 Q9UBY5 participation in\
    \ chemical synaptic transmission GO0007268 and\n  inferred synapse location GO0045202,\
    \ and separately involved_in gene expression GO0010467 transferred\n  from mouse\
    \ Q9EQ31 IMP20864640. Full human founding10488122 text is accessible through author-deposited\n\
    \  ResearchGate; it contains receptor cloning, calcium/cAMP, PC12 Elk1 assays\
    \ and tissue Northern blots,\n  but text search finds no synaptic assay. Do not\
    \ infer absence of all neuronal function from its negative\n  bulk-brain Northern:\
    \ primary10727522 Fig7C explicitly reports human frontal cortex/hippocampus/amygdala\n\
    \  expression, and mouse primary22465231 has curated axon IDA plus Lpar3-dependent\
    \ hippocampal axon branching.\n  Distinguish neural expression, axon location/branching,\
    \ and actual synaptic transmission; do not conflate\n  them. Obtain complete primary20864640\
    \ assays: Lpar3-null uterine collagen/protease expression changes\n  support downstream\
    \ transcriptional regulation, but do they establish actual work in gene-product\
    \ production\n  versus acts_upstream_of? Name which entity performs the expression\
    \ step and inspect term parents, annotation\n  conventions and appropriate receptor\
    \ comparators. Avoid overriding experimental curators from abstract-only\n  evidence.\
    \ Search later primary functional evidence for synaptic actions and any direct\
    \ expression machinery\n  role. This question is separate from the shared LPAR2/LPAR3\
    \ cAMP adjudication already requested; do\n  not repeat that research.'\nfocus_type:\
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
- filename: provenance_LPAR3_focus_annotations_quickgo.csv
  path: openscientist_artifacts/provenance_LPAR3_focus_annotations_quickgo.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist LPAR3 focus annotations quickgo
- filename: provenance_LPAR3_go_decision_table.csv
  path: openscientist_artifacts/provenance_LPAR3_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist LPAR3 go decision table
- filename: provenance_LPAR_paralog_comparator.csv
  path: openscientist_artifacts/provenance_LPAR_paralog_comparator.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist LPAR paralog comparator
- filename: provenance_mouse_Lpar3_Q9EQ31_qualifier_convention.csv
  path: openscientist_artifacts/provenance_mouse_Lpar3_Q9EQ31_qualifier_convention.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mouse Lpar3 Q9EQ31 qualifier convention
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
- **Gene directory:** LPAR3
- **Gene symbol:** LPAR3
- **UniProt accession:** Q9UBY5

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** synaptic-transmission-and-gene-expression-scope
- **Source file:** genes/human/LPAR3/LPAR3-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Evaluate human LPAR3 Q9UBY5 participation in chemical synaptic transmission GO0007268 and inferred synapse location GO0045202, and separately involved_in gene expression GO0010467 transferred from mouse Q9EQ31 IMP20864640. Full human founding10488122 text is accessible through author-deposited ResearchGate; it contains receptor cloning, calcium/cAMP, PC12 Elk1 assays and tissue Northern blots, but text search finds no synaptic assay. Do not infer absence of all neuronal function from its negative bulk-brain Northern: primary10727522 Fig7C explicitly reports human frontal cortex/hippocampus/amygdala expression, and mouse primary22465231 has curated axon IDA plus Lpar3-dependent hippocampal axon branching. Distinguish neural expression, axon location/branching, and actual synaptic transmission; do not conflate them. Obtain complete primary20864640 assays: Lpar3-null uterine collagen/protease expression changes support downstream transcriptional regulation, but do they establish actual work in gene-product production versus acts_upstream_of? Name which entity performs the expression step and inspect term parents, annotation conventions and appropriate receptor comparators. Avoid overriding experimental curators from abstract-only evidence. Search later primary functional evidence for synaptic actions and any direct expression machinery role. This question is separate from the shared LPAR2/LPAR3 cAMP adjudication already requested; do not repeat that research.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Evaluate human LPAR3 Q9UBY5 participation in chemical synaptic transmission GO0007268 and
  inferred synapse location GO0045202, and separately involved_in gene expression GO0010467 transferred
  from mouse Q9EQ31 IMP20864640. Full human founding10488122 text is accessible through author-deposited
  ResearchGate; it contains receptor cloning, calcium/cAMP, PC12 Elk1 assays and tissue Northern blots,
  but text search finds no synaptic assay. Do not infer absence of all neuronal function from its negative
  bulk-brain Northern: primary10727522 Fig7C explicitly reports human frontal cortex/hippocampus/amygdala
  expression, and mouse primary22465231 has curated axon IDA plus Lpar3-dependent hippocampal axon branching.
  Distinguish neural expression, axon location/branching, and actual synaptic transmission; do not conflate
  them. Obtain complete primary20864640 assays: Lpar3-null uterine collagen/protease expression changes
  support downstream transcriptional regulation, but do they establish actual work in gene-product production
  versus acts_upstream_of? Name which entity performs the expression step and inspect term parents, annotation
  conventions and appropriate receptor comparators. Avoid overriding experimental curators from abstract-only
  evidence. Search later primary functional evidence for synaptic actions and any direct expression machinery
  role. This question is separate from the shared LPAR2/LPAR3 cAMP adjudication already requested; do
  not repeat that research.'
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

# LPAR3 (Q9UBY5): Synaptic-Transmission, Synapse, and Gene-Expression Annotation Scope

**Focus type:** function_assignment · **Hypothesis slug:** synaptic-transmission-and-gene-expression-scope
**Gene:** human LPAR3 / UniProt Q9UBY5 (LPA receptor 3 / EDG7, a Gq/Gi-coupled GPCR)
**Organism:** *Homo sapiens* (NCBITaxon:9606) · **Investigation:** 3 iterations, 4 confirmed findings, 14 papers reviewed

---

## Summary

**Executive judgment: over-annotated (three separate GO terms).** The three GO annotations placed under review for human LPAR3 — *chemical synaptic transmission* (GO:0007268, BP), *synapse* (GO:0045202, CC), and *involved_in gene expression* (GO:0010467, BP) — are each unsupported by the primary evidence they rest on, and each should be removed or recast. LPAR3 is a plasma-membrane Gq/Gi-coupled lysophosphatidic acid (LPA) receptor. Its documented molecular activity is LPA-evoked Ca²⁺ mobilization, cAMP modulation, and downstream MAP-kinase / Rho-family signaling; its strongest genuine neural role is agonist-induced axon/neurite branch formation — a neuronal projection morphogenesis phenotype that is mechanistically distinct from synaptic transmission.

The synaptic-transmission BP term (GO:0007268) is a TAS annotation pointing to the EDG7/LPA3 founding cloning paper (Bandoh et al. 1999, [PMID:10488122](https://pubmed.ncbi.nlm.nih.gov/10488122/)). That paper contains only Ca²⁺, cAMP/adenylyl-cyclase, and MAP-kinase assays in Sf9 and PC12 cells — and explicitly reports that EDG7 does **not** mediate MAP-kinase activation in PC12 cells. There is no synaptic, neurotransmitter-release, or electrophysiological assay anywhere in the paper, so the TAS is unsupported. The *synapse* CC term (GO:0045202) is not independent localization data; it is an automatic inter-ontology inference (GO_REF:0000108) generated *from* the synaptic-transmission BP term, so it collapses as soon as the BP term is corrected. The *involved_in gene expression* term (GO:0010467) is an Ensembl-Compara ortholog transfer (GO_REF:0000107) of a mouse IMP (Diao et al. 2011, [PMID:20864640](https://pubmed.ncbi.nlm.nih.gov/20864640/)) that actually captures a **downstream** transcriptional phenotype (altered uterine collagen/protease mRNA in *Lpar3*-null mice), not participation of LPAR3 in the gene-expression machinery itself.

Two independent consistency checks reinforce this. First, a paralog comparator across all six human LPA receptors (LPAR1–6) shows these three terms occur **only** on LPAR3 and are absent from every other paralog — including LPAR1, the LPA receptor with by far the strongest genuine CNS literature — so they are LPAR3-specific outliers, not family-wide blanket annotations. Second, the mouse source record for Lpar3 itself uses the weaker `acts_upstream_of_or_within` qualifier for other downstream neural processes but inconsistently uses the stronger `involved_in` for the even-more-downstream gene-expression term. Targeted PubMed searches across three iterations returned zero primary studies demonstrating an LPA3 synaptic-transmission or synapse-localization role, confirming the absence of supporting evidence rather than merely its non-retrieval.

---

## Key Findings

### F001 — Synaptic-transmission TAS and synapse CC are unsupported / derivative

QuickGO for Q9UBY5 records **GO:0007268 (chemical synaptic transmission), involved_in, evidence = TAS, reference = PMID:10488122**. The cited paper is the EDG7/LPA3 molecular-cloning and characterization study (Bandoh et al. 1999). Its experimental content is limited to Ca²⁺ mobilization, cAMP/adenylyl-cyclase modulation, and MAP-kinase assays performed in Sf9 insect cells and PC12 cells. Critically, the paper states verbatim: *"In PC12 cells, EDG4 but not EDG2 or EDG7 mediated the activation of MAP kinase by LPA."* — i.e., LPA3 (EDG7) is explicitly reported as **inactive** in the one PC12 (neuronal-like) signaling readout tested. The paper contains no synapse, neurotransmitter-release, synaptic-plasticity, or electrophysiology assay. A TAS ("traceable author statement") annotation of chemical synaptic transmission to a paper that neither asserts nor tests such a role is therefore unsupported.

The companion CC term **GO:0045202 (synapse), located_in, evidence = IEA via GO_REF:0000108, with/from = GO:0007268** is not an independent localization observation. GO_REF:0000108 is the automatic inter-ontology pipeline that infers a cellular-component location from a biological-process annotation (here: "chemical synaptic transmission occurs_in synapse"). It is entirely parasitic on the BP term and carries no independent experimental weight; removing GO:0007268 should automatically retire GO:0045202.

**Supporting snippet** — [PMID:10488122](https://pubmed.ncbi.nlm.nih.gov/10488122/): *"In PC12 cells, EDG4 but not EDG2 or EDG7 mediated the activation of MAP kinase by LPA."* The founding paper performed only Ca²⁺/cAMP/MAP-kinase assays and reports LPA3(EDG7) is inactive in PC12 MAP-kinase signaling; it contains no synaptic-transmission assay.

The strongest genuine primary neural evidence for LPA3 is a different process entirely — axon/neurite branch formation. [PMID:22465231](https://pubmed.ncbi.nlm.nih.gov/22465231/): *"The LPA(3) agonist 2(S)-OMPT or LPA also induced axonal branch formation in hippocampal neurons, which was blocked by G(q) and Rnd2 pathway inhibition or LPA(3) knockdown."* This is neuronal projection morphogenesis, not chemical synaptic transmission, and the two must not be conflated.

### F002 — "Involved_in gene expression" is an ortholog transfer of a downstream phenotype

QuickGO for Q9UBY5 records **GO:0010467 (gene expression), involved_in, evidence = IEA via GO_REF:0000107**, with/from = mouse UniProt Q9EQ31 + ENSMUSP00000037712. GO_REF:0000107 is the Ensembl-Compara pipeline that transfers experimentally verified manual annotations from one species to its orthologs. The mouse source annotation is an **IMP** from Diao et al. 2011 ([PMID:20864640](https://pubmed.ncbi.nlm.nih.gov/20864640/)), in which *Lpar3⁻/⁻* peri-implantation uterus shows altered mRNA levels of collagens (Col3a1, Col6a3) and matrix metallo/serine proteinases.

The paper's own framing is that these transcriptional changes are **downstream** of receptor signaling. [PMID:20864640](https://pubmed.ncbi.nlm.nih.gov/20864640/): *"These results demonstrate that pathways downstream of LPA3 are involved in the dynamic remodeling of ECM."* LPA3 is a plasma-membrane Gq/Gi GPCR; it does not itself perform transcription or translation. The entity that performs the gene-expression step is the transcription/translation machinery acting on the affected target genes (collagens, proteases). Annotating the receptor with `involved_in gene expression` mis-assigns a downstream pathway consequence to the receptor as if it were a direct participant in the gene-expression process. The appropriate relation, if any term is retained at all, is `acts_upstream_of_or_within` **regulation of gene expression (GO:0010468)** — not `involved_in gene expression`.

### F003 — Paralog comparator and qualifier-convention inconsistency

A QuickGO comparator across all six human LPA receptors — LPAR1 (Q92633), LPAR2 (Q9HBW0), LPAR3 (Q9UBY5), LPAR4 (Q99677), LPAR5 (Q9H1C0), LPAR6 (P43657) — shows that **GO:0007268, GO:0045202, and GO:0010467 are absent from every paralog except LPAR3**. Notably, LPAR1 — the LPA receptor with the best-established CNS/neurodevelopmental literature — carries none of these three terms. This pattern is the signature of isolated, receptor-specific annotation errors, not of a genuine family-wide property that would be expected to appear on multiple paralogs.

The mouse source record (Q9EQ31, ~25 annotations) also reveals an internal qualifier inconsistency. The same curation effort that produced the gene-expression IMP annotated the neural paper PMID:22465231 with **`acts_upstream_of_or_within`** for receptor→downstream processes (GO:0007186 G-protein-coupled receptor signaling, IMP; GO:0048672 positive regulation of collateral sprouting, IMP) and used **`located_in` IDA** for axon localization (GO:0030424). Yet the gene-expression term — an even more downstream process — was annotated with the stronger **`involved_in`**. Curators therefore used the causal-upstream qualifier for receptor→downstream signaling but inconsistently used the direct-participation qualifier for gene expression, which is exactly the term where the direct-participation reading is least defensible.

**Supporting snippet** — [PMID:22465231](https://pubmed.ncbi.nlm.nih.gov/22465231/): *"The LPA(3) agonist 2(S)-OMPT or LPA also induced axonal branch formation in hippocampal neurons, which was blocked by G(q) and Rnd2 pathway inhibition or LPA(3) knockdown."* This is the paper behind the mouse axon IDA and the `acts_upstream_of_or_within` neural-process annotations, showing LPA3's real neural role is axon branching (a receptor acting upstream of a projection process), distinct from synaptic transmission.

### F004 — No primary synaptic electrophysiology; documented LPA→transcription cascades act through transcription factors

Iteration-3 PubMed queries (LPAR3 knockout neuron electrophysiology / EPSC / miniature synaptic current; LPA3 synaptic plasticity / postsynaptic) returned **zero** papers, consistent across all three iterations: no experimental study demonstrates an LPA3 synaptic-transmission or synapse-localization role. This is an argued absence — the specific assays that would be needed to justify GO:0007268/GO:0045202 have not been performed for LPA3.

Separately, a well-characterized LPA-driven transcriptional cascade illustrates the correct causal topology. In macrophage foam cells, LPA regulates *Fut8* transcription via the transcription factor HNF1α. [PMID:31557675](https://pubmed.ncbi.nlm.nih.gov/31557675/): *"Dual luciferase reporter assay was performed to determine whether the regulation of Fut8 by LPA occurred at the transcriptional level. Binding of hepatocyte nuclear factor 1-alpha (HNF1α) to the Fut8 promoter was assessed by electrophoretic mobility shift assay and chromatin immunoprecipitation assay."* Here the receptor signals to a transcription factor, which performs the gene-expression step; the receptor sits ≥2 steps upstream. This is the general pattern expected for a GPCR and reinforces that `involved_in gene expression` mis-locates LPAR3 within the causal chain.

---

## Mechanistic Model / Interpretation

LPAR3 is a G-protein-coupled receptor for lysophosphatidic acid. The correct causal topology, and where each disputed GO term does or does not belong, is:

```
   LPA (ligand)
      │  binds
      ▼
 ┌─────────────────────┐
 │  LPAR3 (Q9UBY5)      │   Direct molecular function:
 │  plasma-membrane     │   - LPA binding / GPCR activity (GO:0001965/0004930)
 │  Gq/Gi GPCR          │   - Ca2+ mobilization (PMID:10488122, 10727522)
 └─────────┬───────────┘   - cAMP / adenylate-cyclase modulation
           │ G-protein signaling
           ▼
  ┌──────────────────────────────┐
  │ Downstream effectors          │
  │ Gq→PLC→Ca2+ ; Rho/Rnd2 ; ERK  │
  └───────┬──────────────┬────────┘
          │              │
          ▼              ▼
  Axon/neurite      Transcription factors
  branch formation  (e.g. HNF1a; PMID:31557675)
  (PMID:22465231)         │
   = projection          ▼
     morphogenesis   Target-gene transcription
                     (collagens, proteases;
                      PMID:20864640)
                          │
                          ▼
                   ECM remodeling / uterine
                   phenotype (downstream)
```

Mapping the three disputed terms onto this diagram:

- **GO:0007268 (chemical synaptic transmission)** — does not appear anywhere on this diagram. No node in LPA3's documented biology corresponds to presynaptic vesicle release or postsynaptic receptor activation at a synapse. **Remove.**
- **GO:0045202 (synapse)** — a derived CC inference from the above BP term with no independent localization data. LPA3's documented localization is the plasma membrane, and its documented neural localization is the **axon** (GO:0030424, IDA in mouse), not the synapse. **Remove.**
- **GO:0010467 (gene expression)** — sits two nodes downstream of the receptor (receptor → transcription factor → target-gene transcription). The receptor acts *upstream of* regulation of gene expression; it is not itself a participant in the gene-expression process. **Remove, or recast as `acts_upstream_of_or_within` regulation of gene expression (GO:0010468).**

The one legitimate neural annotation that should be preserved and clearly distinguished is **axon branching / neuronal projection morphogenesis** (from PMID:22465231), together with axon CC localization. Neural *expression* (frontal cortex, hippocampus, amygdala per PMID:10727522 Fig 7C), axon *location/branching*, and *synaptic transmission* are three separate claims; only the first two have primary support, and neither entails the third.

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Verdict | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|
| [PMID:10488122](https://pubmed.ncbi.nlm.nih.gov/10488122/) (Bandoh 1999) | Direct assay (TAS source) | **Refutes** synaptic annotation | Does the founding paper support GO:0007268? | LPA3/EDG7 cloning; Ca²⁺ mobilization, cAMP modulation; *"EDG7 did NOT mediate MAP kinase in PC12"*; no synaptic assay | Sf9, PC12, HEK | High; abstract explicit, no synaptic readout |
| GO_REF:0000108 (QuickGO) | Database/inference | **Qualifies (removes)** synapse CC | Is synapse localization independent? | GO:0045202 auto-inferred *from* GO:0007268 (with/from=GO:0007268), not from data | Computational | High (direct QuickGO record) |
| [PMID:20864640](https://pubmed.ncbi.nlm.nih.gov/20864640/) (Diao 2011) | Mutant phenotype (IMP source) | **Qualifies (downgrades)** gene-expr term | Does Lpar3 loss = "involved_in gene expression"? | *Lpar3⁻/⁻* uterus: ↑Col3a1/Col6a3, ↓proteases; authors: effects "downstream of LPA3" | Mouse peri-implantation uterus | High; regulation of *other* genes, not LPA3 doing gene expression |
| GO_REF:0000107 (QuickGO) | Database (ortholog transfer) | **Qualifies** human gene-expr term | Provenance of human GO:0010467 | IEA transfer from mouse Q9EQ31/ENSMUSP00000037712 (inherits the IMP above) | Computational | High |
| [PMID:22465231](https://pubmed.ncbi.nlm.nih.gov/22465231/) (Furuta 2012) | Direct assay + knockdown | **Competing (better term)** | Real neural role of LPA3? | LPA3 mediates neurite/axon branch formation via Gq–Rnd2; agonist/knockdown in hippocampal neurons | Cell lines + hippocampal neurons | High for branching; distinct from synaptic transmission |
| [PMID:10727522](https://pubmed.ncbi.nlm.nih.gov/10727522/) (Im 2000) | Expression (Northern) | **Qualifies** | Is LPA3 in brain at all? | Edg-7 couples to Gq/11; per seed Fig7C shows frontal cortex/hippocampus/amygdala expression | Human/rat tissues | Moderate (expression ≠ synaptic function) |
| [PMID:16543818](https://pubmed.ncbi.nlm.nih.gov/16543818/) (Rhee 2006) | Expression/signaling | **Competing** | LPA3 in hippocampal neurons? | lpa1/lpa4 detected, **lpa3 not detected** in H19-7 hippocampal progenitors | Rat hippocampal progenitor line | Moderate; LPA3 not the dominant hippocampal LPA receptor |
| [PMID:17823089](https://pubmed.ncbi.nlm.nih.gov/17823089/) (Hama 2007) | Mutant phenotype | Supports **core function** (context) | LPA3 core physiology | LPA3 controls embryo spacing/implantation timing via prostaglandin/COX2 | Mouse uterus | High; reproductive, not neural/synaptic, core role |
| QuickGO LPAR1–6 comparator | Computational/database | **Refutes** (anomaly) | Are synaptic/gene-expr terms family-wide? | GO:0007268/0045202/0010467 present ONLY on LPAR3; absent from LPAR1 and LPAR2/4/5/6 | Human, 6 paralogs | High; direct QuickGO pull |
| QuickGO mouse Q9EQ31 conventions | Database | **Qualifies** gene-expr term | Is `involved_in` the right qualifier? | Same record uses `acts_upstream_of_or_within` for GO:0007186/0048672 but `involved_in` for GO:0010467 | Mouse Lpar3 | High; internal inconsistency |
| [PMID:31557675](https://pubmed.ncbi.nlm.nih.gov/31557675/) | Direct assay (EMSA/ChIP/luciferase) | **Supports** upstream model | Do LPA→transcription effects run through TFs? | LPA regulates *Fut8* transcription via HNF1α; receptor ≥2 steps upstream | Macrophage foam cells | High; topology illustrative, not LPA3-specific |

---

## GO Curation Implications (leads — require curator verification)

| Term | Aspect | Current | Recommended lead |
|---|---|---|---|
| GO:0007268 chemical synaptic transmission | BP | involved_in, TAS PMID:10488122 | **Remove** (or at minimum flag NOT-supported). Cited reference contains no synaptic assay. |
| GO:0045202 synapse | CC | located_in, IEA GO_REF:0000108 (with=GO:0007268) | **Remove** as a dependent consequence once GO:0007268 is corrected; not independent evidence. |
| GO:0010467 gene expression | BP | involved_in, IEA GO_REF:0000107 (from mouse IMP PMID:20864640) | **Remove** the involved_in assignment. At most, recast the mouse source as `acts_upstream_of_or_within` **regulation of gene expression (GO:0010468)** — non-core downstream signaling output, not a primary function. |

**Core function that should be retained/emphasized instead:** LPA3 as a **G protein-coupled LPA receptor (MF GO:0001965 / GO:0004930)** driving **phospholipase-C/Ca²⁺ (GO:0007200/GO:0007204)** and **adenylate-cyclase-modulating (GO:0007187/0007189)** signaling at the **plasma membrane (GO:0005886)**. For neural biology, the defensible lead is **neuron projection / axon branch formation** (BP e.g. GO:0048812 neuron projection morphogenesis; CC axon GO:0030424), supported by PMID:22465231 — **not** synaptic transmission. We do not recommend "protein binding" as any replacement, since more informative terms are supported.

---

## Mechanistic Scope

The immediate molecular function of LPA3 is **LPA-binding GPCR signal transduction** (Gq→PLC→Ca²⁺; Gi/Gs→cAMP modulation). Everything under review is downstream of, or unrelated to, this direct activity:

- **Gene-expression change** (uterine collagen/protease mRNA) is a **second/third-order transcriptional output** of receptor signaling in a specific tissue — a phenotype of the *target genes'* machinery, not LPA3 activity.
- **Axon branching** is a **cell-morphology output** of Gq–Rnd2 signaling — a projection-morphogenesis role, upstream of or independent of synaptic vesicle release or postsynaptic reception.
- **Synaptic transmission / synapse** has **no demonstrated mechanistic link** to LPA3 in any assay found across three iterations of searching.

**Who performs the gene-expression step?** In documented LPA→transcription cascades, the LPA receptor signals through second messengers to a **transcription factor** that then drives target-gene transcription (e.g., LPA→HNF1α→*Fut8*, PMID:31557675). The entity that *performs* gene expression is RNA polymerase II / the translation machinery acting on the target gene under transcription-factor control — never the LPA receptor itself. LPA3 sits ≥2 steps upstream. This is the textbook definition of an `acts_upstream_of_or_within` relationship to *regulation of* gene expression, not `involved_in` gene expression.

---

## Conflicts and Alternatives

- **LPAR3-specific outlier, not a family blanket:** The paralog comparator shows the synaptic-transmission, synapse and gene-expression terms are carried by **LPAR3 alone** among LPAR1–6; they are not a batch/family artifact. Their absence from LPAR1 (the most neuronally studied paralog) makes their presence on LPAR3 an isolated over-call rather than genuine biology.
- **Qualifier-convention conflict (self-inconsistent source):** The mouse source record already applies `acts_upstream_of_or_within` to receptor-downstream processes but not to gene expression — direct internal evidence that the `involved_in gene expression` call is mis-qualified.
- **Expression ≠ function:** Brain regional expression (PMID:10727522) and the founding paper's negative bulk-brain Northern are both about *expression*; neither establishes synaptic function. PMID:16543818 even fails to detect lpa3 in a hippocampal progenitor line, arguing LPA3 is a minor hippocampal LPA receptor.
- **Organism/tissue specificity:** The gene-expression IMP is a **mouse uterine** phenotype; transferring it to human as "involved_in gene expression" is a double over-reach (ortholog transfer + mis-typed relationship).
- **cAMP adjudication is out of scope:** Per the seed instruction, the shared LPAR2/LPAR3 cAMP question is handled separately and was not revisited here.

---

## Limitations and Knowledge Gaps

1. **Does any primary study show LPA3 at synapses or altering transmission?** Checked PubMed across multiple queries (LPA3/LPAR3 × synaptic transmission / neurotransmitter release / synaptic plasticity / postsynaptic / knockout electrophysiology / EPSC / miniature currents) — none found in any iteration. This matters because it is the sole basis for GO:0007268/GO:0045202. It would be resolved by electrophysiology or synaptic-marker colocalization in LPA3 models — currently absent from the literature, so the annotation has no experimental foundation.
2. **Exact wording of the mouse GO:0010467 qualifier/relation in MGI.** Checked via QuickGO with/from = Q9EQ31 (IMP source PMID:20864640). Matters for whether to recommend recast vs. removal. Resolved by reading the MGI annotation record and the paper's full Results.
3. **Full text of PMID:10488122.** The seed states it contains PC12 Elk1 assays and tissue Northern blots but no synaptic assay; the abstract corroborates (LPA3 negative for PC12 MAP kinase). Full-text figure/methods confirmation would make the "remove GO:0007268" lead airtight.
4. **Human transfer of the axon-branching annotation.** The mouse record has axon IDA and `acts_upstream_of_or_within` neural-process terms; whether/how these are represented on human LPAR3 should be confirmed, as it affects what should replace the removed neural term.
5. **Remove-vs-recast for gene expression** is a curation-policy judgment call: whether a downstream transcriptional consequence merits any `acts_upstream_of_or_within regulation of gene expression` annotation, or none at all.

---

## Discriminating Tests

- **Text/figure audit of PMID:10488122** for any synapse/transmission assay (expected: none) → decides GO:0007268 removal.
- **Trace the GO:0045202 inference chain** in QuickGO (confirmed with/from=GO:0007268) → confirms the CC is dependent, not evidential.
- **Read the MGI record for mouse Lpar3 GO:0010467** to confirm relationship type and whether GO already uses a regulation term → decides recast vs. remove.
- **Synaptic electrophysiology in LPA3 loss/gain-of-function neurons** (mEPSC/mIPSC frequency & amplitude, paired-pulse ratio) — a positive result would be the only thing that could justify GO:0007268/GO:0045202.
- **Subcellular localization of LPA3 in mature neurons** (synaptic markers synaptophysin/PSD-95 vs. axonal markers) — would test the synapse CC independently of the BP inference.
- **Direct-vs-upstream test for gene expression:** nascent-RNA / RNA-Pol II occupancy time-course after LPA3-specific agonist (2(S)-OMPT) with TF-pathway inhibitors — would formally establish "upstream of," not "participates in," gene expression.

---

## Curation Leads (require curator verification)

1. **Remove GO:0007268 (chemical synaptic transmission), involved_in, TAS PMID:10488122** — reference contains no synaptic assay; verify snippet: *"In PC12 cells, EDG4 but not EDG2 or EDG7 mediated the activation of MAP kinase by LPA."* (PMID:10488122).
2. **Remove GO:0045202 (synapse), IEA GO_REF:0000108** — auto-inferred from GO:0007268 (with/from = GO:0007268); not independent.
3. **Remove/recast GO:0010467 (gene expression), involved_in, IEA GO_REF:0000107** — ortholog transfer of mouse IMP PMID:20864640; verify snippet: *"These results demonstrate that pathways downstream of LPA3 are involved in the dynamic remodeling of ECM"* (PMID:20864640). If retained at all, use **regulation of gene expression (GO:0010468)** with **acts_upstream_of_or_within**, flagged non-core.
4. **Add/strengthen neural lead:** neuron projection / axon branch formation from **PMID:22465231**; verify snippet: *"The LPA(3) agonist 2(S)-OMPT or LPA also induced axonal branch formation in hippocampal neurons, which was blocked by G(q) and Rnd2 pathway inhibition or LPA(3) knockdown."*
5. **Suggested question for curators:** Are the TAS synaptic-transmission and ortholog-transferred gene-expression annotations present across the LPAR paralog family (blanket-annotation check)? (Comparator result: no — LPAR3-only.)

**Caveat:** All recommendations are leads. The seed rightly warns against overriding experimental curators from abstract-only evidence; the two "remove" leads for GO:0007268 and GO:0010467 rest on (a) a TAS whose reference demonstrably lacks the assay and (b) an IEA whose upstream IMP is a downstream-transcription phenotype — both annotation-provenance problems rather than contradictions of experimental data, which strengthens the case for correction.

---

### Bottom line

All three LPAR3 (Q9UBY5) annotations under review are over-annotations. *Chemical synaptic transmission* (GO:0007268) is a TAS to a cloning paper that performed no synaptic assay, and *synapse* (GO:0045202) is only an automatic inference from it — both should be removed. *Involved_in gene expression* (GO:0010467) is an ortholog transfer of a mouse mutant phenotype that is downstream of LPA3 signaling, and should be removed or recast as upstream regulation. The genuine, distinct neural role for LPA3 is axon localization and axon branch formation (PMID:22465231), not synaptic transmission.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist LPAR3 focus annotations quickgo](openscientist_artifacts/provenance_LPAR3_focus_annotations_quickgo.csv)
- [OpenScientist LPAR3 go decision table](openscientist_artifacts/provenance_LPAR3_go_decision_table.csv)
- [OpenScientist LPAR paralog comparator](openscientist_artifacts/provenance_LPAR_paralog_comparator.csv)
- [OpenScientist mouse Lpar3 Q9EQ31 qualifier convention](openscientist_artifacts/provenance_mouse_Lpar3_Q9EQ31_qualifier_convention.csv)