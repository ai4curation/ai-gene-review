---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-07T00:24:22.528349'
end_time: '2026-06-07T00:52:35.054354'
duration_seconds: 1692.53
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 22
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
- **Gene directory:** STAT3
- **Gene symbol:** STAT3

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** readout-go-0030335
- **Source file:** genes/human/STAT3/STAT3-ai-review.yaml
- **Source selector:** existing_annotations[247]

## Seed Hypothesis

The existing STAT3 GO annotation to positive regulation of cell migration (GO:0030335) is currently action ACCEPT and was flagged by the ASSAY_TO_FUNCTION readout class CELL_MIGRATION_INVASION. Decide whether this BP term is a CORE function of STAT3 (a primary process the gene product evolved to drive) versus a DOWNSTREAM, secondary, or context-dependent consequence of its core molecular activity that is better captured as non-core. Distinguish a 'real, documented effect' (which may not be in question) from a 'core function'. Flag rationale: ACCEPT BP call aligned to CELL_MIGRATION_INVASION; rubric default is non-core unless gene is in the machinery

## Term and Decision Context

- Term: positive regulation of cell migration (GO:0030335)
- Evidence type: IMP
- Original reference: PMID:31638206
- Current review action: UNDECIDED
- Review summary: Experimental evidence (IMP) supports positive regulation of cell migration for STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]
- Review reason: Real but borderline core vs non-core. STAT3's core molecular function is signal-dependent DNA-binding transcription factor activity (JAK-STAT); cell migration is a downstream transcriptional consequence rather than an activity STAT3 itself performs, and STAT3 is not part of the cytoskeletal/ adhesion motility machinery. The IMP evidence (knockdown/overexpression migration phenotype) is the classic indirect "perturb gene -> phenotype" inference. Flagged by the ASSAY_TO_FUNCTION CELL_MIGRATION_INVASION readout class; given STAT3 is high-profile and the call is genuinely contested (oncogenic migration driver vs downstream consequence), deferred to expert review rather than unilaterally demoted (issue #1422; staged OpenScientist hypothesis job under STAT3-hypotheses/).

## Reference Context

- PMID:31638206

## Source Context YAML

```yaml
term:
  id: GO:0030335
  label: positive regulation of cell migration
evidence_type: IMP
original_reference_id: PMID:31638206
review:
  summary: Experimental evidence (IMP) supports positive regulation of cell migration for STAT3 [file:human/STAT3/STAT3-deep-research-falcon.md]
  action: UNDECIDED
  reason: 'Real but borderline core vs non-core. STAT3''s core molecular function is signal-dependent
    DNA-binding transcription factor activity (JAK-STAT); cell migration is a downstream transcriptional
    consequence rather than an activity STAT3 itself performs, and STAT3 is not part of the cytoskeletal/
    adhesion motility machinery. The IMP evidence (knockdown/overexpression migration phenotype) is the
    classic indirect "perturb gene -> phenotype" inference. Flagged by the ASSAY_TO_FUNCTION CELL_MIGRATION_INVASION
    readout class; given STAT3 is high-profile and the call is genuinely contested (oncogenic migration
    driver vs downstream consequence), deferred to expert review rather than unilaterally demoted (issue
    #1422; staged OpenScientist hypothesis job under STAT3-hypotheses/).'
  supported_by:
  - reference_id: PMID:31638206
    supporting_text: Oct 11. MicroRNA‑4500 suppresses tumor progression in non‑small cell lung cancer
      by regulating STAT3.
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

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

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

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.

## Output

# STAT3 Annotation to Positive Regulation of Cell Migration (GO:0030335): Core vs. Non-Core Classification

## Executive Judgment

**Verdict: NON-CORE (over-annotated as core function).** The GO annotation of STAT3 to positive regulation of cell migration (GO:0030335) should be **retained as biologically accurate but reclassified as non-core** — a real, well-documented downstream consequence of STAT3's core transcription factor activity rather than a primary function the gene product evolved to perform.

Three convergent lines of evidence support this classification: (1) The dominant mechanism by which STAT3 promotes cell migration is **transcriptional** — STAT3 drives expression of Twist1, MMPs, and EMT markers as downstream targets of its core DNA-binding transcription factor activity in the JAK-STAT pathway; (2) STAT3 exerts **bidirectional effects on migration** — promoting it in cancer and wound healing contexts while inhibiting it in cortical neuron migration — a hallmark of context-dependent downstream function that is incompatible with classification as core migration machinery; (3) Although a secondary non-transcriptional mechanism exists (STAT3-stathmin interaction stabilizing microtubules), this mechanism is context-limited, partially redundant, and was not tested in the reference paper's NSCLC context ([PMID: 31638206](https://pubmed.ncbi.nlm.nih.gov/31638206/)). The reference paper itself employs classic indirect IMP evidence (miR-4500 targeting STAT3 → reduced migration), which is the canonical "perturb gene → observe phenotype" design that cannot distinguish core from downstream function.

The current UNDECIDED action should be resolved to **ACCEPT as non-core**. The annotation is scientifically valid and should not be removed, but it should be clearly flagged as a downstream consequence of STAT3's primary molecular function (signal-dependent DNA-binding transcription factor activity) rather than evidence that STAT3 is part of the cell migration machinery.

**Key caveats:**
1. The STAT3-stathmin interaction means STAT3 IS capable of directly modulating cytoskeletal dynamics — this is not purely a transcriptional relay
2. The non-core classification is strong but not absolute; the stathmin mechanism prevents a categorical "no direct involvement"
3. The annotation is biologically accurate regardless of core/non-core classification
4. STAT3 has BIDIRECTIONAL migration effects — it promotes migration in cancer/wound healing (GO:0030335) but INHIBITS neuronal migration in developing cortex (GO:2001223, [PMID: 22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/)). Core migration machinery components do not show bidirectional effects; this is a hallmark of a context-dependent transcription factor whose migration effects depend on which target genes it activates in a given cellular context

---

## Summary

STAT3 (Signal Transducer and Activator of Transcription 3) is a well-characterized intracellular transcription factor (~92 kDa, 750–795 amino acids) whose core molecular function is signal-dependent DNA-binding transcription factor activity within the JAK-STAT signaling pathway. Constitutive STAT3 knockout in mice is embryonic lethal at E6.5–E7.5 ([PMID: 30254684](https://pubmed.ncbi.nlm.nih.gov/30254684/)), underscoring its essential role in transcriptional regulation during development. The question under review is whether STAT3's documented role in promoting cell migration constitutes a **core function** (i.e., STAT3 is part of the migration machinery) or a **downstream, context-dependent consequence** of its transcription factor activity.

Our investigation, spanning 73 papers and 5 analytical iterations, establishes that STAT3 promotes cell migration primarily through transcriptional activation of pro-migratory target genes — including Twist1, MMPs (MMP-1, -2, -3, -9, -10, -13), EMT transcription factors, and chemokines — rather than through direct participation in the cytoskeletal or adhesion machinery that executes cell movement. A secondary, non-transcriptional mechanism involving direct STAT3-stathmin interaction and microtubule stabilization has been documented since 2006 ([PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/)), but this mechanism is context-restricted (demonstrated primarily in T-cells, motoneurons, and fibroblasts) and was not evaluated in the NSCLC context of the reference paper. Critically, STAT3 has **bidirectional** effects on migration: it promotes migration in cancer cells, wound-healing keratinocytes, and T-cells, but **inhibits** radial neuronal migration in the developing cerebral cortex ([PMID: 22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/)). This bidirectionality is a defining feature of a context-dependent downstream effector, not a core component of the migration machinery.

The GO database itself reflects this picture: STAT3 carries 17+ annotations to transcription/signaling terms, exactly one annotation to positive regulation of cell migration (GO:0030335), one to negative regulation of neuron migration (GO:2001223), and zero annotations to microtubule, stathmin, cytoskeletal, or actin-related terms — despite published biochemical evidence for the STAT3-stathmin interaction. This annotation profile is consistent with a transcription factor whose pleiotropic target genes include migration regulators, rather than a gene product whose primary function is in the migration pathway.

---

## Key Findings

### Finding 1: STAT3 Promotes Cell Migration via Transcriptional Activation of Pro-Migratory Genes

The predominant mechanism by which STAT3 influences cell migration is through its canonical role as a transcription factor. Multiple independent studies demonstrate that STAT3 directly binds the promoters of pro-migratory genes and drives their expression:

- **Twist1 transcription:** STAT3 directly binds the Twist1 promoter to induce EMT transcription factor expression. In hepatocellular carcinoma cells, a dual-luciferase reporter assay confirmed that "STAT3 may bind the Twist promoter, mediate its transcriptional activity, and then promote the EMT process in HCC cells" ([PMID: 25653024](https://pubmed.ncbi.nlm.nih.gov/25653024/)). Similarly, in prostate cancer, "STAT3 and HIF-1α up-regulated TWIST1 expression by direct binding to a TWIST1 promoter" ([PMID: 23623921](https://pubmed.ncbi.nlm.nih.gov/23623921/)). Additional ChIP evidence from colorectal cancer confirms IL-6 treatment promotes "recruitment of STAT3, κB and C/EBPβ toward the Twist promoter region" ([PMID: 37047623](https://pubmed.ncbi.nlm.nih.gov/37047623/)).

- **Matrix metalloproteinase expression:** STAT3 activation drives expression of multiple MMPs critical for extracellular matrix remodeling during migration. Knockdown of the lncRNA PRECSIT "inhibited expression of activated STAT3 and resulted in down-regulation of the expression of matrix metalloproteinase (MMP)-1, MMP-3, MMP-10, and MMP-13" in cutaneous squamous cell carcinoma ([PMID: 31837949](https://pubmed.ncbi.nlm.nih.gov/31837949/)). PLOD3 interacts with STAT3 to express MMP-2 and MMP-9 for tumor metastasis ([PMID: 30442941](https://pubmed.ncbi.nlm.nih.gov/30442941/)). The IL-6/STAT3/MMP signaling axis drives gastric cancer cell migration via paracrine activation ([PMID: 30361813](https://pubmed.ncbi.nlm.nih.gov/30361813/)). EZH2 promotes renal cell carcinoma invasion through STAT3-mediated MMP-2 upregulation ([PMID: 29286132](https://pubmed.ncbi.nlm.nih.gov/29286132/)).

- **Non-canonical STAT3 roles are mitochondrial, not cytoskeletal:** The well-documented non-transcriptional functions of STAT3 involve modulation of mitochondrial electron transport chain activity via S727 phosphorylation — not cytoskeletal regulation. As stated in the literature: "STAT3 is increasingly becoming known for its non-transcriptional regulation of mitochondrial bioenergetic function upon activation of its S727 residue" ([PMID: 27978828](https://pubmed.ncbi.nlm.nih.gov/27978828/)) and "STAT3 is a transcription factor involved in several cellular activities including inflammation, proliferation, and survival, but it also plays a non-transcriptional role in modulating mitochondrial metabolism" ([PMID: 33305182](https://pubmed.ncbi.nlm.nih.gov/33305182/)). The mitochondrial role is the dominant non-transcriptional STAT3 activity discussed in the literature, far outweighing the stathmin interaction.

This evidence establishes that migration effects observed upon STAT3 perturbation are predominantly downstream transcriptional consequences, not evidence of STAT3 participation in the migration machinery itself.

### Finding 2: STAT3 Core Function is Signal-Dependent Transcription Factor Activity

STAT3's evolutionarily conserved primary function is as a transcription factor in the JAK-STAT signaling pathway:

- Constitutive STAT3 knockout mice are embryonic lethal at E6.5–E7.5, "prior to potential functional role in early development can be assessed" ([PMID: 30254684](https://pubmed.ncbi.nlm.nih.gov/30254684/)). This early lethality reflects transcriptional essentiality, not a migration defect.
- STAT3 is activated by JAK-mediated Y705 phosphorylation for nuclear translocation and DNA binding. Conditional knockout studies confirm STAT3 "is a transcription factor that has many essential roles during inflammation, development and cancer" ([PMID: 28170160](https://pubmed.ncbi.nlm.nih.gov/28170160/)).
- A comprehensive review describes STAT3 as an "intracellular transcription factor, spanning 750-795 amino acids and weighing approximately 92 kDa, [that] is crucial in key cellular activities such as growth, migration, invasion, inflammation, and angiogenesis" — notably listing migration as one of many downstream activities ([PMID: 39473261](https://pubmed.ncbi.nlm.nih.gov/39473261/)).
- The GO annotation profile for STAT3 (UniProt P40763) includes 17+ annotations to DNA-binding transcription factor activity (GO:0003700), RNA pol II-specific TF activity (GO:0000981), JAK-STAT signaling (GO:0007259), and cytokine-mediated signaling (GO:0019221), compared to a single migration annotation.

### Finding 3: The Reference Paper (PMID:31638206) Provides Classic Indirect IMP Evidence

The original reference supporting the GO:0030335 annotation uses a standard perturb-gene-observe-phenotype experimental design:

- miR-4500 directly targets the STAT3 3'UTR (confirmed by luciferase reporter assay): "A luciferase reporter assay suggested that miR‑4500 directly targeted the 3' untranslated region of STAT3" ([PMID: 31638206](https://pubmed.ncbi.nlm.nih.gov/31638206/)).
- miR-4500 overexpression suppresses STAT3 protein levels and "suppressed the cell proliferation, migration, invasion and promoted apoptosis of the human NSCLC cell lines A549 and H1975" ([PMID: 31638206](https://pubmed.ncbi.nlm.nih.gov/31638206/)).
- siRNA against STAT3 phenocopies the migration suppression, and "The tumor inhibition effect of small interfering RNA STAT3 in A549 and H1975 lines may be partially impaired by a miR‑4500 inhibitor" ([PMID: 31638206](https://pubmed.ncbi.nlm.nih.gov/31638206/)).

This is classic IMP evidence. Critically, migration was measured as **one of several phenotypic readouts** alongside proliferation and apoptosis. The paper does not distinguish whether STAT3's effect on migration is direct (via migration machinery) or indirect (via transcriptional targets). The experimental design cannot make this distinction.

### Finding 4: A Non-Transcriptional STAT3-Stathmin Mechanism Exists but Is Context-Limited

A significant complication arises from the documented non-transcriptional role of STAT3 in microtubule regulation via direct interaction with stathmin (STMN1):

- The seminal paper by Ng et al. (2006) demonstrated that STAT3 physically interacts with stathmin: "Previously, the function of Stat3 had been attributed exclusively to its transcriptional activity in the nucleus. In this study, we reveal an interaction between Stat3 and the microtubule (MT)-destabilizing protein stathmin." Furthermore, "Recombinant Stat3 was also capable of reversing stathmin inhibition of tubulin polymerization in vitro" ([PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/)). This is a genuine biochemical interaction where STAT3 protein directly modulates cytoskeletal dynamics independent of transcription.

- This mechanism was confirmed in migrating T-cells: "STAT3 physically interacts with stathmin to regulate microtubule dynamics in migrating T-cells" ([PMID: 19251695](https://pubmed.ncbi.nlm.nih.gov/19251695/)).

- It was observed in motoneuron axons: "activated STAT3 interacted with stathmin and inhibited its microtubule-destabilizing activity" ([PMID: 23109669](https://pubmed.ncbi.nlm.nih.gov/23109669/)).

- In gastric cancer: "STAT3 depletion inhibited the activity of RhoA and the interaction with stathmin, downregulated the expression of pFAK (phosphorylated focal adhesion kinase), acetylated-tubulin" ([PMID: 23333463](https://pubmed.ncbi.nlm.nih.gov/23333463/)).

- A commentary described the mechanism: "new evidence suggests a novel role for non-tyrosine-phosphorylated and cytoplasmically localized STAT3 in mediating cell migration by disrupting an interaction between microtubules and one of its partners, stathmin" ([PMID: 16835434](https://pubmed.ncbi.nlm.nih.gov/16835434/)).

However, several factors limit the relevance of this mechanism for the annotation under review:

1. **Partial redundancy:** In the original paper, "down-regulation of stathmin protein levels in Stat3-deficient cells partially reversed the MT and migration deficiencies" — only partial rescue, indicating multiple contributing pathways ([PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/)).
2. **Context restriction:** The STAT3-stathmin interaction has been demonstrated primarily in fibroblasts, T-cells, motoneurons, and gastric cancer cells. It has **not** been tested in the NSCLC context of the reference paper.
3. **No GO annotation exists:** Despite publication in 2006 (20 years ago), STAT3 has zero GO annotations to microtubule, stathmin, tubulin, or cytoskeletal terms, suggesting the community does not regard this as a core function.
4. **Stoichiometric considerations:** Unphosphorylated cytoplasmic STAT3 mediates this interaction, which is distinct from the Y705-phosphorylated pool responsible for transcription. This may represent a moonlighting function of the abundant cytoplasmic pool rather than a primary evolved activity.
5. **Evidence asymmetry:** Approximately 14+ papers document the transcriptional migration mechanism vs. ~6 papers documenting the stathmin mechanism, reflecting both publication trends and biological dominance of the transcriptional pathway.

{{figure:evidence_comparison.png|caption=Quantitative comparison of evidence supporting transcriptional vs. stathmin-mediated STAT3 migration mechanisms. The transcriptional pathway has substantially more independent supporting studies across diverse cancer types and tissues, while the stathmin mechanism is documented in a limited number of cell type contexts.}}

### Finding 5: Bidirectional Migration Effects Confirm Non-Core Classification

The strongest evidence against core classification is STAT3's **bidirectional** effect on migration:

- **Pro-migratory:** In cancer cells (NSCLC, breast, gastric, colorectal, glioma), wound-healing keratinocytes, and migrating T-cells, STAT3 activation promotes migration.
- **Anti-migratory:** In developing cerebral cortex, STAT3 activation via KLF4-induced Y705 phosphorylation **inhibits** radial neuronal migration. "Blocking STAT3 activation with a dominant negative form can rescue the migration defect induced by constitutive KLF4 expression" ([PMID: 22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/)).

This bidirectionality is reflected in GO annotations: STAT3 carries both positive regulation of cell migration (GO:0030335) **and** negative regulation of neuron migration (GO:2001223). A gene product that is genuinely part of the migration machinery (e.g., a cytoskeletal motor, an adhesion receptor, or a Rho GTPase) would not exhibit opposing effects depending on cell context. The bidirectional phenotype is the hallmark of a **transcription factor** whose different target gene repertoires in different cell types lead to opposing downstream effects on the same biological process.

### Finding 6: Keratinocyte-Specific STAT3 KO Shows In Vivo Migration Defect, but Is Cell-Type Dependent

Conditional knockout studies provide important in vivo context:

- Keratinocyte-specific Stat3 knockout mice show that "Stat3 activation contributed to skin wound healing, keratinocyte migration, hair follicle growth, and resistance to UV irradiation-induced apoptosis" ([PMID: 17601706](https://pubmed.ncbi.nlm.nih.gov/17601706/)). This confirms a real migration phenotype in vivo.
- However, myeloid-specific STAT3 knockout showed that the "impact on wound closure dynamics and quality of healing after acute excision skin injury was minor" ([PMID: 29898959](https://pubmed.ncbi.nlm.nih.gov/29898959/)), demonstrating cell-type dependency.
- In wound healing, the mechanism is transcriptional: STAT3-activated SPRR1B+ keratinocytes mediate rapid mucosal repair, and "SPRR1B knockdown significantly inhibits mucosal keratinocyte migration" ([PMID: 39300285](https://pubmed.ncbi.nlm.nih.gov/39300285/)). STAT3 acts by transcriptionally activating SPRR1B — the migration effect is downstream of transcription.

This cell-type specificity further supports classification as a context-dependent downstream effect rather than a core function.

---

## Mechanistic Model / Interpretation

The following model synthesizes the evidence into a coherent framework for understanding STAT3's relationship to cell migration:

```
                    CORE FUNCTION                           DOWNSTREAM EFFECTS
                    ─────────────                           ──────────────────
                                                           
  Cytokine/Growth Factor                                   
         │                                                 
         ▼                                                 
   JAK phosphorylation                                     
         │                                                 
         ▼                                                 
  ┌──────────────────┐                                     
  │  STAT3 (Y705-P)  │──── Core MF: DNA-binding            
  │  Transcription   │     transcription factor             
  │  Factor Activity │     activity (GO:0003700)            
  └──────┬───────────┘                                     
         │                                                 
         ├──► Twist1, Snail, Slug ──► EMT ──► Migration ↑  (cancer)
         ├──► MMP-1/2/3/9/10/13 ──► ECM remodeling ──► Invasion ↑
         ├──► VEGFA, iNOS ──► Angiogenesis                 
         ├──► Bcl-2, survivin ──► Survival                 
         ├──► SPRR1B ──► Keratinocyte migration ↑          (wound)
         ├──► Neuronal gene targets ──► Migration ↓        (cortex)
         └──► Chemokines, cytokines ──► Immune cell migration
                                                           
  ┌──────────────────┐                                     
  │ STAT3 (unP, cyto)│──── Secondary/Accessory:            
  │ Stathmin binding │     stathmin sequestration           
  └──────┬───────────┘     (context-limited)               
         │                                                 
         └──► MT stabilization ──► Migration ↑             (T-cells,
                                                            fibroblasts,
                                                            some cancers)
```

**Key insight:** The same transcription factor (STAT3) drives **different transcriptional programs** in different cellular contexts, leading to **opposing effects** on migration. This is the defining signature of a downstream, context-dependent function — not a core migration function. A core migration gene (e.g., RAC1, CDC42, ACTN1, the Arp2/3 complex) does not switch between pro- and anti-migratory roles based on cell type. The fact that STAT3 promotes migration in cancer cells but inhibits it in cortical neurons ([PMID: 22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/)) definitively establishes that STAT3 is not part of the universal migration machinery.

The secondary stathmin mechanism represents a genuine direct participation in cytoskeletal dynamics, but it is (a) context-limited, (b) partially redundant with other stathmin regulators, (c) uses a distinct STAT3 pool (unphosphorylated, cytoplasmic), and (d) was not tested in the reference paper's context. It constitutes a moonlighting function rather than the primary evolved activity of STAT3.

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence & Limitations |
|----------|--------------|-----------|-------------|-------------|---------|-------------------------|
| [PMID: 31638206](https://pubmed.ncbi.nlm.nih.gov/31638206/) | Mutant phenotype (IMP) | Supports annotation | STAT3 knockdown reduces migration | miR-4500 targets STAT3 3'UTR; knockdown reduces migration in NSCLC | Human, NSCLC (A549, H1975) | Moderate; classic IMP, cannot distinguish mechanism |
| [PMID: 23623921](https://pubmed.ncbi.nlm.nih.gov/23623921/) | Direct assay (ChIP) | Qualifies as transcriptional | STAT3 directly activates Twist1 | STAT3+HIF-1α bind TWIST1 promoter directly | Human, prostate cancer | High; direct promoter binding |
| [PMID: 25653024](https://pubmed.ncbi.nlm.nih.gov/25653024/) | Direct assay (reporter) | Qualifies as transcriptional | STAT3 drives Twist transcription | Luciferase confirms STAT3-Twist promoter activity → EMT | Human, HCC | High; reporter assay |
| [PMID: 31837949](https://pubmed.ncbi.nlm.nih.gov/31837949/) | Mutant phenotype | Qualifies as transcriptional | STAT3 drives MMP expression | STAT3 activation → MMP-1, -3, -10, -13 in cSCC | Human, cutaneous SCC | High |
| [PMID: 30442941](https://pubmed.ncbi.nlm.nih.gov/30442941/) | Mutant phenotype + interaction | Qualifies as transcriptional | PLOD3-STAT3 drives metastasis | PLOD3 interacts with STAT3 → MMP-2, MMP-9 → metastasis | Human, lung cancer + xenograft | High |
| [PMID: 30361813](https://pubmed.ncbi.nlm.nih.gov/30361813/) | Mutant phenotype | Qualifies as transcriptional | IL-6/STAT3/MMP pathway | IL-6 from fibroblasts activates STAT3→MMP→migration | Human, gastric cancer | High |
| [PMID: 29286132](https://pubmed.ncbi.nlm.nih.gov/29286132/) | Mutant phenotype | Qualifies as transcriptional | EZH2-STAT3-MMP axis | EZH2 increases p-STAT3 → MMP-2 → invasion | Human, RCC | High |
| [PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/) | **Direct assay (co-IP, in vitro polymerization)** | **Competing (supports core)** | STAT3 directly antagonizes stathmin | Recombinant STAT3 reverses stathmin inhibition of tubulin polymerization; stathmin KD partially rescues migration in STAT3-null cells | Mouse fibroblasts (MEFs) | **High; strongest evidence for non-transcriptional mechanism; partial rescue only** |
| [PMID: 19251695](https://pubmed.ncbi.nlm.nih.gov/19251695/) | Direct assay (co-IP) | **Competing (supports core)** | STAT3-stathmin in T-cell migration | STAT3 physically interacts with stathmin to regulate MT dynamics in migrating T-cells | Human, Hut78 T-lymphoma | High; direct non-transcriptional mechanism |
| [PMID: 16835434](https://pubmed.ncbi.nlm.nih.gov/16835434/) | Commentary | **Competing (supports core)** | Non-transcriptional STAT3 migration | Non-tyrosine-phosphorylated, cytoplasmic STAT3 mediates migration via stathmin-MT disruption | Commentary | Moderate |
| [PMID: 23109669](https://pubmed.ncbi.nlm.nih.gov/23109669/) | Direct assay | **Competing (supports core)** | STAT3-stathmin in axons | Activated STAT3 interacts with stathmin, inhibits MT-destabilizing activity in motoneurons | Mouse, motoneurons | High; but axon context, not classical cell migration |
| [PMID: 23333463](https://pubmed.ncbi.nlm.nih.gov/23333463/) | Knockdown phenotype | **Supports both mechanisms** | STAT3 in gastric cancer motility | STAT3 depletion impairs RhoA, stathmin interaction, pFAK, microtubules AND MMP activity | Human, gastric cancer | High; shows dual mechanisms |
| [PMID: 22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/) | Mutant phenotype | **Supports non-core (bidirectional)** | STAT3 inhibits neuron migration | STAT3 activation INHIBITS radial neuronal migration in cortex; DN-STAT3 rescues | Mouse, developing cerebral cortex | **High; bidirectionality clinches non-core** |
| [PMID: 17601706](https://pubmed.ncbi.nlm.nih.gov/17601706/) | Review (conditional KO) | Supports annotation | STAT3 in keratinocyte migration in vivo | Keratinocyte-specific Stat3 KO: impaired wound healing and migration | Mouse, keratinocyte KO | High; in vivo |
| [PMID: 29898959](https://pubmed.ncbi.nlm.nih.gov/29898959/) | Conditional KO | Qualifies | Myeloid STAT3 KO in wound healing | Myeloid STAT3 KO: minor impact on wound closure | Mouse, myeloid KO | High; cell-type specificity |
| [PMID: 30254684](https://pubmed.ncbi.nlm.nih.gov/30254684/) | Knockout | Supports core TF function | STAT3 knockout phenotype | Constitutive KO lethal at E6.5–E7.5 | Mouse embryo | High |
| [PMID: 33305182](https://pubmed.ncbi.nlm.nih.gov/33305182/) | Direct assay | Qualifies (mitochondrial) | STAT3 non-transcriptional function | Non-transcriptional role is mitochondrial, not cytoskeletal | Human, tumor cells | High |
| [PMID: 27978828](https://pubmed.ncbi.nlm.nih.gov/27978828/) | Direct assay | Qualifies | Integrin-FAK-STAT3 pathway | S727 non-transcriptional function is mitochondrial | Mouse, brain endothelial | High |
| [PMID: 39300285](https://pubmed.ncbi.nlm.nih.gov/39300285/) | scRNA-seq + functional | Qualifies as transcriptional | STAT3 in wound healing | STAT3-activated SPRR1B+ keratinocytes; SPRR1B KD inhibits migration | Human/Mouse, oral mucosa | High; transcriptional mechanism |
| [PMID: 39473261](https://pubmed.ncbi.nlm.nih.gov/39473261/) | Review | Supports core TF function | STAT3 overview | Describes STAT3 as transcription factor with migration among many activities | Review | Moderate |
| UniProt SPARQL (June 2026) | Database record | Supports non-core | STAT3 GO annotation landscape | 17+ TF annotations, 1 pos migration, 1 neg migration, 0 cytoskeletal | Human P40763 | Moderate |

{{figure:go_decision_table.png|caption=GO curation decision table summarizing the evidence for and against core vs. non-core classification of the STAT3 migration annotation. The weight of evidence from multiple independent analyses favors non-core classification.}}

---

## GO Curation Implications

### Recommended Action: Reclassify as NON-CORE (Lead Requiring Curator Verification)

**Current state:** The annotation GO:0030335 (positive regulation of cell migration) with IMP evidence from PMID:31638206 is marked UNDECIDED.

**Recommended curation lead:**

| Aspect | Recommendation | Rationale |
|--------|---------------|-----------|
| **Term** | GO:0030335 — retain | Migration effect is real and reproducible |
| **Evidence code** | IMP — retain | Appropriate for perturb-gene-observe-phenotype |
| **Core/Non-core** | **Non-core** | Transcriptional downstream effect; bidirectional |
| **Reference** | PMID:31638206 — retain | Valid experimental evidence |
| **Action** | ACCEPT as non-core | Resolve current UNDECIDED status |

### Rationale for Non-Core

1. **STAT3 is not part of the migration machinery.** It has no structural or functional homology to cytoskeletal components, adhesion molecules, Rho GTPases, or other bona fide migration effectors. Its GO annotation landscape (17+ TF/signaling annotations, 0 cytoskeletal annotations) reflects this.
2. **The migration effect is transcriptionally mediated.** STAT3 drives expression of Twist1, MMPs, and EMT markers — the migration phenotype is a downstream consequence of these transcriptional targets.
3. **Bidirectional effects.** STAT3 promotes migration in some contexts (cancer, wound healing) and inhibits it in others (cortical neurons), which is inconsistent with core migration function but perfectly consistent with a context-dependent transcription factor.
4. **The IMP evidence is indirect.** The reference paper uses knockdown/overexpression → migration readout, which cannot distinguish core from downstream function.
5. **STAT3 knockout lethality.** Embryonic lethality at E6.5–E7.5 reflects transcriptional essentiality, not a migration defect.
6. **Stathmin interaction is secondary.** Despite genuine biochemical evidence, the stathmin mechanism is context-limited, partially redundant, and not tested in the reference paper's system.

### Additional GO Considerations

- The existing annotation to **negative regulation of neuron migration (GO:2001223)** should also be classified as non-core, for the same reasons.
- The **STAT3-stathmin interaction** ([PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/)) could potentially support a separate annotation to **positive regulation of microtubule polymerization (GO:0031116)** or **regulation of microtubule stability**, but this requires independent curator evaluation.
- STAT3's core MF annotation as **DNA-binding transcription factor activity (GO:0003700)** and core BP annotations to **JAK-STAT signaling (GO:0007259)** should remain unchanged.

### Alternative Interpretation: If Curator Judges Stathmin Interaction as Sufficient for Core

If a curator determines that the STAT3-stathmin interaction constitutes direct participation in the migration machinery sufficient for core classification, this would be an unusual but defensible interpretation. In that case:
- The annotation could be classified as CORE with a note documenting both transcriptional and non-transcriptional mechanisms
- This would require policy guidance on how dual-mechanism genes are handled
- The β-catenin precedent (dual adhesion + Wnt transcription function) may be informative

---

## Conflicts and Alternatives

### The STAT3-Stathmin Argument for Core Function

The most significant competing evidence comes from the STAT3-stathmin interaction literature. If STAT3 directly stabilizes microtubules by sequestering stathmin — a mechanism demonstrated with purified recombinant proteins in vitro ([PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/)) — this would constitute a direct, non-transcriptional role in the migration machinery. Several considerations limit this argument:

1. **Partial rescue only.** Stathmin knockdown in STAT3-deficient cells only "partially reversed the MT and migration deficiencies," indicating the stathmin mechanism is one of multiple pathways, not the sole mechanism.
2. **Context restriction.** Demonstrated in fibroblasts (MEFs), T-cells, motoneurons, and gastric cancer cells, but not in NSCLC cells or most other cancer types.
3. **20 years without GO annotation.** Despite publication in 2006, no curator has annotated STAT3 to microtubule-related GO terms, suggesting a community assessment that this is not a primary function.
4. **Stoichiometric moonlighting.** Unphosphorylated, cytoplasmically localized STAT3 mediates this interaction — a distinct functional pool from the transcriptionally active, Y705-phosphorylated STAT3.

### Bidirectionality as Definitive Evidence

The bidirectional migration phenotype is the single strongest piece of evidence for non-core classification. Core migration machinery proteins (e.g., Rac1, Cdc42, WASP, Arp2/3 complex, cofilin) consistently function in the same direction because they ARE the molecular machinery executing movement. STAT3 promotes migration in cancer and wound healing but inhibits migration in cortical neurons — because in neurons, STAT3 activates different transcriptional targets that produce the opposite migratory effect. This is the textbook behavior of an upstream regulator, not a core machinery component.

### Cell-Type Dependency

The myeloid-specific STAT3 knockout showing "minor" impact on wound closure ([PMID: 29898959](https://pubmed.ncbi.nlm.nih.gov/29898959/)) versus the keratinocyte-specific knockout showing clear migration defects ([PMID: 17601706](https://pubmed.ncbi.nlm.nih.gov/17601706/)) illustrates that even the magnitude of STAT3's migration effect varies dramatically by cell type. This is another hallmark of a downstream effect mediated through different transcriptional programs.

### No Paralog or Organism-Specific Confounds

STAT3 is the primary STAT family member implicated in migration. STAT1, STAT5A/B have distinct functions and are not prominently associated with cell migration. No organism-specific discrepancies were identified across human, mouse, and rat studies.

---

## Knowledge Gaps

| Gap | What Was Checked | Why It Matters | Resolution Needed |
|-----|-----------------|----------------|-------------------|
| **STAT3-stathmin in NSCLC** | Literature search for STAT3-stathmin in lung cancer; only transcriptional evidence found | Reference paper (PMID:31638206) is from NSCLC; stathmin mechanism not tested there | Test STAT3-stathmin co-IP in A549/H1975 NSCLC cells |
| **Transcription-independent migration** | No studies using transcriptionally dead STAT3 mutants in NSCLC migration | Would definitively distinguish core vs. downstream in the annotation's context | Express STAT3 DNA-binding mutants in STAT3-null NSCLC cells, measure migration |
| **Quantitative contribution** | Partial rescue data from PMID:16401721 only | Need to know what fraction of STAT3's migration effect is transcriptional vs. stathmin-mediated | Simultaneous measurement with WT, Y705F, DBD mutants, and stathmin-KD |
| **Stathmin mechanism breadth** | Demonstrated in T-cells, neurons, fibroblasts, gastric cancer; not tested in most other contexts | If context-limited, strengthens non-core; if universal, strengthens core | Systematic survey across cell types |
| **Isoform-specific effects** | STAT3α vs. STAT3β not distinguished in migration studies | STAT3β lacks transactivation domain but may retain stathmin binding | Test isoform-specific knockdown/overexpression in migration assays |
| **Wound healing mechanism** | STAT3-SPRR1B transcriptional mechanism documented; stathmin role not tested | Wound healing is a physiological migration context | Test STAT3-stathmin interaction in migrating keratinocytes |
| **Evolutionary conservation** | Not systematically assessed | If STAT3-migration link is conserved in invertebrates, may reflect ancient core function | Compare in Drosophila STAT92E models |

---

## Discriminating Tests

The following experiments would most efficiently resolve remaining uncertainty:

1. **Separation-of-function STAT3 mutants + migration assay (HIGHEST PRIORITY):** Express in STAT3-null NSCLC cells: (a) WT STAT3, (b) STAT3-Y705F (transcriptionally impaired but retains stathmin binding), (c) STAT3-DBD mutant (cannot bind DNA), (d) STAT3 with stathmin-binding domain disrupted. Compare migration rescue. This would definitively separate the two mechanisms in the reference paper's context.

2. **STAT3-stathmin co-IP in NSCLC cells:** Test whether the stathmin mechanism is active in A549/H1975 cells. If absent, the annotation from PMID:31638206 is purely transcriptional.

3. **Acute STAT3 degradation kinetics:** Use dTAG/auxin-inducible degron STAT3 and measure migration at 2h (before transcriptional effects) vs. 24h. If acute degradation immediately impairs migration, the stathmin mechanism is active in that context.

4. **STAT3β isoform migration test:** Express STAT3β (lacks transactivation domain) in STAT3-null cells. If migration is partially rescued, confirms non-transcriptional contribution is sufficient.

5. **Comparative annotation analysis:** Examine how GO annotates other dual-function proteins (e.g., β-catenin in both adhesion and Wnt transcription) for analogous core/non-core precedents.

---

## Curation Leads

### Lead 1: Change Action from UNDECIDED to ACCEPT (Non-Core) — RECOMMENDED

- **Current action:** UNDECIDED
- **Proposed action:** ACCEPT as non-core
- **Rationale:** The annotation is biologically correct. The dominant mechanism is transcriptional (STAT3→Twist1/MMPs→migration). The bidirectionality (pro-migratory in cancer, anti-migratory in neurons) clinches the non-core classification.
- **Confidence:** Moderate-to-high. The stathmin complication prevents absolute certainty but does not change the overall assessment.
- **Key references for curator verification:**
  - [PMID: 23623921](https://pubmed.ncbi.nlm.nih.gov/23623921/): *"STAT3 and HIF-1α up-regulated TWIST1 expression by direct binding to a TWIST1 promoter"* — confirms transcriptional mechanism
  - [PMID: 22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/): *"Blocking STAT3 activation with a dominant negative form can rescue the migration defect induced by constitutive KLF4 expression"* — confirms bidirectionality (STAT3 inhibits migration in neurons)
  - [PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/): *"Recombinant Stat3 was also capable of reversing stathmin inhibition of tubulin polymerization in vitro"* — documents the stathmin complication (for curator awareness)

### Lead 2: No Term Change Needed

- **GO:0030335 (positive regulation of cell migration)** is the correct term regardless of core/non-core classification
- Do NOT replace with a more general term; do NOT remove the annotation
- The IMP evidence code is appropriate

### Lead 3: Consider Separate Stathmin Interaction Annotation

- If curators determine the STAT3-stathmin interaction warrants its own annotation, consider:
  - **BP:** positive regulation of microtubule polymerization (GO:0031116) with evidence from [PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/)
  - **Evidence code:** IDA (direct assay — in vitro tubulin polymerization)
  - This would be a separate curation action, independent of the migration annotation

### Lead 4: Core Function Annotations to Verify

Ensure the following core-function annotations exist for STAT3:
- **MF:** DNA-binding transcription factor activity, RNA polymerase II-specific (GO:0000981)
- **BP:** JAK-STAT signaling pathway (GO:0007259)
- **BP:** Cytokine-mediated signaling pathway (GO:0019221)

### Suggested Curator Questions

1. Does the curation framework have established policy for dual-mechanism genes (both transcriptional and non-transcriptional contributions to the same biological process)?
2. Is the bidirectionality argument (pro-migratory in cancer, anti-migratory in neurons) sufficient grounds for non-core classification even in the absence of separation-of-function experiments?
3. Should the ASSAY_TO_FUNCTION CELL_MIGRATION_INVASION readout class flag be resolved differently for transcription factors with documented non-transcriptional cytoskeletal interactions?
4. Is there precedent from β-catenin curation (dual adhesion + transcription function) that could inform this decision?

---

## Evidence Base: Key Literature

### Primary Evidence (Directly Supporting Classification)

| PMID | Title (abbreviated) | Role in Assessment |
|------|---------------------|-------------------|
| [31638206](https://pubmed.ncbi.nlm.nih.gov/31638206/) | *miR-4500 suppresses NSCLC by regulating STAT3* | **Reference paper** — IMP evidence for migration annotation; classic indirect design |
| [23623921](https://pubmed.ncbi.nlm.nih.gov/23623921/) | *STAT3 mediates TGF-β1-induced TWIST1 and invasion* | Establishes transcriptional mechanism for migration via ChIP |
| [25653024](https://pubmed.ncbi.nlm.nih.gov/25653024/) | *STAT3 cooperates with Twist for EMT in HCC* | Confirms transcriptional pathway to migration via reporter assay |
| [22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/) | *KLF4 role in neurogenesis and radial migration* | **Critical** — shows STAT3 INHIBITS migration in neurons; clinches bidirectionality |
| [16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/) | *Stat3 regulates MTs by antagonizing stathmin* | Seminal stathmin interaction paper; strongest competing evidence |
| [19251695](https://pubmed.ncbi.nlm.nih.gov/19251695/) | *STAT3-stathmin in migrating T-cells* | Confirms stathmin mechanism in T-cell migration |

### Supporting Evidence (Contextual and Mechanistic)

| PMID | Title (abbreviated) | Role in Assessment |
|------|---------------------|-------------------|
| [30254684](https://pubmed.ncbi.nlm.nih.gov/30254684/) | *STAT3-inducible mouse ESCs* | STAT3 KO lethality at E6.5–E7.5 confirms transcriptional essentiality |
| [28170160](https://pubmed.ncbi.nlm.nih.gov/28170160/) | *Inducible model to silence Stat3* | Core TF function characterization |
| [17601706](https://pubmed.ncbi.nlm.nih.gov/17601706/) | *Stat3 in skin biology* | Keratinocyte-specific KO shows in vivo migration defect |
| [29898959](https://pubmed.ncbi.nlm.nih.gov/29898959/) | *Myeloid STAT3 antifibrotic repair* | Cell-type specificity of wound healing role (minor effect) |
| [33305182](https://pubmed.ncbi.nlm.nih.gov/33305182/) | *STAT3 inhibitor OPB-51602* | Non-transcriptional STAT3 role is mitochondrial, not cytoskeletal |
| [27978828](https://pubmed.ncbi.nlm.nih.gov/27978828/) | *Integrin-FAK and mitochondrial STAT3* | S727 non-transcriptional function is mitochondrial |
| [31837949](https://pubmed.ncbi.nlm.nih.gov/31837949/) | *PRECSIT promotes cSCC via STAT3/MMPs* | STAT3 → MMP transcriptional axis for invasion |
| [30442941](https://pubmed.ncbi.nlm.nih.gov/30442941/) | *PLOD3 promotes lung metastasis via STAT3* | STAT3 → MMP-2/9 in lung cancer metastasis |
| [30361813](https://pubmed.ncbi.nlm.nih.gov/30361813/) | *Paeoniflorin inhibits gastric CAF migration* | IL-6/STAT3/MMP paracrine migration cascade |
| [23109669](https://pubmed.ncbi.nlm.nih.gov/23109669/) | *STAT3 in pmn motoneuron disease* | STAT3-stathmin interaction in axon maintenance |
| [23333463](https://pubmed.ncbi.nlm.nih.gov/23333463/) | *STAT3/Skp2/p27/p21 in gastric cancer motility* | Dual mechanisms: cytoskeletal + transcriptional |
| [39300285](https://pubmed.ncbi.nlm.nih.gov/39300285/) | *SPRR1B+ keratinocytes in wound healing* | STAT3 → SPRR1B transcriptional mechanism for keratinocyte migration |
| [39473261](https://pubmed.ncbi.nlm.nih.gov/39473261/) | *STAT3 in CRC pathogenesis* | Review listing migration among many STAT3 downstream activities |
| [16835434](https://pubmed.ncbi.nlm.nih.gov/16835434/) | *Touched and moved by STAT3* | Commentary on stathmin mechanism |

---

## Limitations

1. **Literature bias toward cancer.** The vast majority of STAT3-migration studies are in cancer cell lines, which have numerous dysregulated pathways that may amplify or distort STAT3's contribution to migration. Normal physiological contexts (wound healing, immune cell trafficking) are less well-studied.

2. **Incomplete mechanism dissection.** Most studies use total STAT3 knockdown/knockout, which eliminates both transcriptional and non-transcriptional functions simultaneously. No study directly compares the quantitative contribution of each mechanism in the same cell system.

3. **Reference paper limitations.** PMID:31638206 is a cancer cell line study focused on miR-4500 as an anti-cancer mechanism, with migration as one of several measured phenotypes. It was not designed to address the core vs. non-core question.

4. **Stathmin mechanism under-explored.** The STAT3-stathmin interaction, first published in 2006, has relatively few follow-up studies (~6) compared to the transcriptional migration literature (~14+). This asymmetry may partly reflect publication bias rather than biological importance.

5. **No separation-of-function experiments in NSCLC.** The definitive experiment (transcriptionally dead STAT3 mutant in NSCLC migration assay) has not been performed. Our classification relies on the convergence of indirect evidence.

6. **Species considerations.** Most evidence is from mouse conditional knockouts and human cancer cell lines. Evolutionary conservation of the stathmin mechanism has not been systematically assessed.

---

## Proposed Follow-up Experiments and Actions

### For Curators (Immediate Actions)

1. **Resolve UNDECIDED → ACCEPT as non-core** based on the convergent evidence for transcriptional mechanism and bidirectionality
2. **Add curator note** citing the bidirectional migration evidence ([PMID: 22907754](https://pubmed.ncbi.nlm.nih.gov/22907754/)) as key discriminating evidence for non-core classification, and noting the stathmin complication ([PMID: 16401721](https://pubmed.ncbi.nlm.nih.gov/16401721/)) for transparency
3. **Evaluate STAT3-stathmin annotation** as a separate curation question (microtubule regulation, not migration per se)

### For Experimentalists (Future Work)

1. **Priority 1:** Test transcriptionally dead STAT3 mutant (Y705F or DNA-binding domain mutant) in NSCLC migration assays to definitively resolve the transcription dependence of migration in this specific context
2. **Priority 2:** Perform STAT3-stathmin co-IP in A549/H1975 cells to determine if the stathmin mechanism is active in the reference paper's cell system
3. **Priority 3:** Acute STAT3 degradation (dTAG system) with time-course migration measurement to separate immediate (cytoskeletal) from delayed (transcriptional) effects

### For Bioinformaticians

1. Compare STAT3 migration annotations across model organism databases (SGD, FlyBase, WormBase) to assess evolutionary conservation
2. Network analysis of STAT3 transcriptional targets in migration-relevant GO terms to quantify the "transcriptional distance" between STAT3 and migration execution
3. Systematic review of GO annotation policies for dual-function proteins (e.g., β-catenin) to establish precedent for this classification decision

---

*Report generated from 5 iterations of systematic investigation, reviewing 73 papers across PubMed, UniProt, and GO databases. Investigation covered transcriptional mechanisms, non-transcriptional stathmin interaction, bidirectional migration effects, conditional knockout phenotypes, and GO annotation landscape analysis. Last updated: 2026-06-07.*
