---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-26T20:07:25.496018'
end_time: '2026-10-26T20:25:49.852241'
duration_seconds: 1104.36
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SPIC
  gene_symbol: SPIC
  uniprot_accession: Q8N5J4
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: spic-bach1-cooccurrence
  hypothesis_text: 'The heme-induced red pulp macrophage programme (heme inactivates
    the repressor BACH1, de-repressing the ETS factor SPI-C) is restricted to vertebrate
    lineages in which SPIC orthologs exist and BACH1 retains its C-terminal heme-binding
    cysteine-proline (CP) motifs. Test with one analysis: identify SPIC orthologs
    across vertebrates and check conservation of the BACH1 C-terminal CP motifs in
    the same species.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/SPIC/SPIC-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'The heme-induced red pulp macrophage programme\
    \ (heme inactivates the repressor BACH1, de-repressing\n  the ETS factor SPI-C)\
    \ is restricted to vertebrate lineages in which SPIC orthologs exist and BACH1\
    \ retains\n  its C-terminal heme-binding cysteine-proline (CP) motifs. Test with\
    \ one analysis: identify SPIC orthologs\n  across vertebrates and check conservation\
    \ of the BACH1 C-terminal CP motifs in the same species.'\nfocus_type: free_text\n\
    context: []\nreference_id: []"
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
- **Gene directory:** SPIC
- **Gene symbol:** SPIC
- **UniProt accession:** Q8N5J4

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** spic-bach1-cooccurrence
- **Source file:** genes/human/SPIC/SPIC-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The heme-induced red pulp macrophage programme (heme inactivates the repressor BACH1, de-repressing the ETS factor SPI-C) is restricted to vertebrate lineages in which SPIC orthologs exist and BACH1 retains its C-terminal heme-binding cysteine-proline (CP) motifs. Test with one analysis: identify SPIC orthologs across vertebrates and check conservation of the BACH1 C-terminal CP motifs in the same species.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'The heme-induced red pulp macrophage programme (heme inactivates the repressor BACH1, de-repressing
  the ETS factor SPI-C) is restricted to vertebrate lineages in which SPIC orthologs exist and BACH1 retains
  its C-terminal heme-binding cysteine-proline (CP) motifs. Test with one analysis: identify SPIC orthologs
  across vertebrates and check conservation of the BACH1 C-terminal CP motifs in the same species.'
focus_type: free_text
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

# AIGR Gene Hypothesis Deep Research — SPIC / BACH1 Co-occurrence

**Target gene:** SPIC (human; UniProt Q8N5J4; NCBITaxon:9606)
**Hypothesis slug:** `spic-bach1-cooccurrence`
**Source file:** `genes/human/SPIC/SPIC-ai-review.yaml`
**Focus type:** free_text

---

## Executive Judgment

**Verdict: Partially supported.**

The seed hypothesis states that the heme-induced red pulp macrophage (RPM) programme — in which heme inactivates the repressor **BACH1**, de-repressing the ETS-family transcription factor **SPI-C (SPIC)** — should be restricted to vertebrate lineages in which SPIC orthologs exist *and* in which BACH1 retains its C-terminal heme-binding cysteine-proline (CP) motifs. The requested single analysis was to identify SPIC orthologs across vertebrates and check conservation of the BACH1 C-terminal CP motifs in the same species.

Public orthology and sequence analysis **confirms the co-occurrence prerequisites** of the hypothesis. SPIC is a **jawed-vertebrate (gnathostome) innovation**, present from the elephant shark (*Callorhinchus milii*) through all bony vertebrates (mammals, birds, reptiles, amphibians including caecilians, teleosts, and the coelacanth *Latimeria*), but **absent in cyclostomes** (lamprey, hagfish) and invertebrates. In the matched panel of curated bony-vertebrate BACH1 transcription factors (human, mouse, chicken, *Xenopus*, zebrafish), the **C-terminal heme-regulatory Cys-Pro motif is positionally conserved** at a near-constant fractional position (~0.87–0.89 of protein length) within a near-identical sequence context (`QILAKYS[A/S][A/S][D/T/E]CPL`). Critically, **no discordant species** was found: there is no lineage carrying SPIC without a BACH1 ortholog, and no bony-vertebrate BACH1 TF lacking the C-terminal CP motif.

However, three caveats keep this from a full endorsement. **First**, co-presence and sequence conservation are not the same as conserved *regulatory wiring* — the heme→BACH1→SPIC axis is experimentally demonstrated only in mouse, so the hypothesis's functional claim is an inference, not a direct result, outside *Mus*. **Second**, the C-terminal CP status **at the chondrichthyan boundary is unresolved**: deep-lineage BACH1 gene models (elephant shark, gar) are unreliable auto-translations with anomalous lengths (>1000 aa vs the expected ~630–780 aa for the BTB-bZIP TF), so the test could not be completed cleanly at the SPIC-origin boundary. **Third, and most important for curation**: heme sensing is a **BACH1** function, not a SPIC function. SPIC (Q8N5J4) is a 248-aa ETS-family DNA-binding transcription factor with no heme-binding CP architecture. The hypothesis is therefore sound as an evolutionary co-occurrence statement but must not be read as licensing a "heme binding" annotation on SPIC.

---

## Key Findings

### Finding 1 — SPIC and a C-terminal-CP BACH1 co-occur across bony vertebrates (F001)

A UniProt ortholog survey established that the **SPIC gene is present in >150 vertebrate species**, spanning mammals, birds, reptiles, amphibians (including caecilians), teleosts, and the coelacanth *Latimeria*. In a matched five-species panel — human (BACH1 O14867), mouse (P97302), chicken (A0A8V0YE10), *Xenopus* (F7BYY6), and zebrafish (A0AB13A814) — the **BACH1 transcription factor** (a BTB-bZIP protein of 632–765 aa) retains a C-terminal **Cys-Pro dipeptide** at a conserved fractional position (0.87–0.89 of length) within a near-identical motif, `QILAKYS[A/S][A/S][D/T/E]CPL`.

Two disambiguations are essential here. (1) The relevant BACH1 is the **BTB-and-CNC-homology 1 transcription factor** (O14867, ~736 aa), *not* the 1174–1249 aa **BRIP1/FANCJ helicase** that shares the legacy alias "BACH1" — a classic source of database carry-over error. (2) The heme-regulatory CP motifs reside in **BACH1**, not SPIC.

No discordant species was found: there was no lineage with SPIC present but the C-terminal CP absent, nor the converse. Invertebrate outgroups (*Ciona*, *Branchiostoma*, *Drosophila*, *S. purpuratus*) have **neither SPIC nor a BACH1-TF**. This co-occurrence pattern is exactly what the seed hypothesis predicts for the co-evolved arms of the pathway.

The functional relevance of the CP motif is anchored by [PMID: 24630724](https://pubmed.ncbi.nlm.nih.gov/24630724/): *"cysteine-proline dipeptide motifs in BACH1 that mediate heme-dependent degradation were necessary for Spic induction by heme."* This establishes the CP motifs as the functional element coupling heme to SPIC de-repression, which is precisely what motivates testing their conservation in SPIC-bearing lineages.

### Finding 2 — Heme sensing is a BACH1 function; SPIC is the downstream DNA-binding transcription factor (F002)

This is the most consequential finding for curation. The heme sensor in this pathway is **BACH1**, and SPIC is the **downstream effector transcription factor**, not a heme sensor. Haldar et al. 2014 ([PMID: 24630724](https://pubmed.ncbi.nlm.nih.gov/24630724/)) state: *"Spic expression in monocytes was constitutively inhibited by the transcriptional repressor BACH1. Heme induced proteasome-dependent BACH1 degradation and rapid Spic derepression."*

SPIC (Q8N5J4) is a **248-aa ETS-family transcription factor** with no heme-binding CP architecture. The CP motifs that confer heme responsiveness are located in BACH1 (O14867, 736 aa, BTB + bZIP). Consequently, any curation action derived from this hypothesis should annotate SPIC as a **sequence-specific DNA-binding transcription factor** driving RPM differentiation and iron homeostasis — and should **not** attribute heme binding or heme sensing to SPIC itself.

### Finding 3 — SPIC is a gnathostome innovation that arose after BACH1; no lineage has SPIC without BACH1 (F003)

Ensembl Compara orthology data (human SPIC: 183 ortholog species; human BACH1: 191 species) show that the **SPIC ortholog is present from the elephant shark *Callorhinchus milii* (a chondrichthyan) through all bony vertebrates**, but **absent in cyclostomes** (lamprey *Petromyzon marinus*, hagfish *Eptatretus burgeri*) and invertebrates (*Ciona*, *C. elegans*). By contrast, **BACH1 orthology extends deeper** — it is present in hagfish and, via Compara, has invertebrate CNC/BTB-bZIP relatives.

A discordance analysis returned **0 species with SPIC but lacking a BACH1 ortholog**. The 8-species gap (191 BACH1 minus 183 SPIC) corresponds entirely to **pre-gnathostome/invertebrate lineages that diverged before SPIC arose**. This ordering — BACH1 ancestral, SPIC a later gnathostome addition — is consistent with a model in which SPIC was recruited into a pre-existing heme/BACH1-responsive regulatory landscape.

The ancestral, direct heme-binding nature of BACH1 is corroborated by [PMID: 39323025](https://pubmed.ncbi.nlm.nih.gov/39323025/), which describes *"the transcription factors BACH1 and BACH2, which are expressed in B cells and regulated by direct heme binding."*

One important limitation surfaced here: deep-lineage BACH1 auto-translations were **unreliable** (anomalous lengths of 1826/1083 aa for *Callorhinchus*/*Lepisosteus*), so the C-terminal CP status **at the chondrichthyan boundary is unresolved from auto-annotation**. C-terminal CP conservation is robust only across the UniProt-curated Osteichthyes panel.

### Finding 4 — The chondrichthyan-boundary CP test is unresolvable from public auto-annotation (F004)

An iteration-3 re-check of Ensembl Compara BACH1 orthologs confirmed that deep-lineage gene models are not trustworthy for this specific motif test. The elephant shark gene ENSCMIG00000016693 returns four translations of 1826/1192/1160/1096 aa; gar (*Lepisosteus*) 1083 aa; coelacanth (*Latimeria*) 716 aa; hagfish 612 aa. **None of the anomalously long models contains the positionally homologous C-terminal `(Q/V)ILAKYS…CPL` signature** present in all five UniProt-curated bony-vertebrate BACH1 TFs.

Crucially, the anomalous lengths (>1000 aa versus the ~630–780 aa expected for the BTB-bZIP TF) indicate **mis-assigned or merged gene models rather than a true C-terminal CP loss**. The coelacanth (716 aa) and hagfish (612 aa) models are length-plausible, but hagfish is a cyclostome lacking SPIC, so it is not an informative test point for the hypothesis's co-occurrence prediction. The upshot: the hypothesis's co-occurrence claim is **confirmed for curated Osteichthyes** and **inferred-but-unverified at the SPIC-origin (chondrichthyan) boundary** because the data quality there is insufficient — not because the motif is absent.

---

## Mechanistic Model / Interpretation

The pathway tested by this hypothesis is a **two-component, heme-gated transcriptional switch** operating in monocyte-to-macrophage differentiation:

```
          Low heme                         High heme (hemolysis / RBC recycling)
   ┌───────────────────────┐        ┌──────────────────────────────────────────┐
   │  BACH1 (BTB-bZIP)      │        │  heme binds BACH1 C-terminal CP motifs    │
   │  bound at Spic locus   │  ───►  │  → proteasomal BACH1 degradation          │
   │  → REPRESSES Spic      │        │  → Spic DE-REPRESSION                      │
   └───────────────────────┘        └──────────────────────────────────────────┘
                                                      │
                                                      ▼
                                      SPIC (ETS-family DNA-binding TF, 248 aa)
                                                      │
                                                      ▼
                            Red pulp macrophage differentiation program
                            (iron recycling / erythrophagocytosis identity)
```

The sensing/decision node is **BACH1**; the executing node is **SPIC**. Heme is read by BACH1's C-terminal CP dipeptide motifs, whose engagement triggers BACH1 ubiquitination and degradation, lifting repression at the *Spic* locus. SPIC then acts as a conventional sequence-specific transcription factor to install the RPM identity.

Evolutionarily, the components are **layered in time**: BACH1 (and its heme-sensing CP architecture) predates SPIC. SPIC appears at the base of gnathostomes and is thereafter universally accompanied by a BACH1 ortholog.

| Lineage | SPIC present? | BACH1-TF present? | C-terminal CP motif | Informative for hypothesis? |
|---|---|---|---|---|
| Invertebrates (Ciona, Drosophila, amphioxus, sea urchin) | No | No (CNC/BTB-bZIP relatives only) | n/a | Outgroup — consistent |
| Cyclostomes (lamprey, hagfish) | No | Yes (e.g. hagfish, length-plausible model) | Not scored (pre-SPIC) | Not informative (no SPIC) |
| Chondrichthyans (elephant shark) | **Yes** | Yes, but gene model unreliable (1826 aa) | **Unresolved** | Key boundary — data-limited |
| Bony vertebrates (human→zebrafish, curated) | **Yes** | **Yes** (632–765 aa) | **Conserved** (frac ~0.88, `QILAKYS..CPL`) | Confirms co-occurrence |

The core evolutionary signature the hypothesis predicts — **strict co-occurrence of SPIC with a CP-motif-bearing BACH1** — holds everywhere the data are reliable. The one gap is a data-quality gap (chondrichthyan gene models), not contradictory evidence.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 24630724](https://pubmed.ncbi.nlm.nih.gov/24630724/) | Direct assay / mutant | **Supports** (mechanism) | BACH1 CP motifs couple heme to Spic induction | *"cysteine-proline dipeptide motifs in BACH1 ... were necessary for Spic induction by heme"*; BACH1 represses Spic, heme degrades BACH1 → Spic de-repression | Mouse monocytes/RPM | High for mouse; single-species functional demonstration |
| [PMID: 24630724](https://pubmed.ncbi.nlm.nih.gov/24630724/) | Direct assay | **Qualifies** (locates heme sensing in BACH1, not SPIC) | Which protein is the heme sensor | SPIC is downstream DNA-binding TF; heme acts on BACH1 | Mouse | High; argues against heme-binding annotation on SPIC |
| [PMID: 39323025](https://pubmed.ncbi.nlm.nih.gov/39323025/) | Review/database + direct | **Supports** (BACH1 = heme sensor) | BACH1 directly binds heme | *"BACH1 and BACH2 ... regulated by direct heme binding"* | Human/mouse B & plasma cells | Moderate; confirms sensor identity, not SPIC-specific |
| UniProt ortholog survey (this analysis) | Structural/evolutionary (computational) | **Supports** | SPIC + CP-BACH1 co-occur in bony vertebrates | SPIC in >150 species; BACH1 CP motif conserved frac ~0.88 in matched panel; 0 discordant species | Human→zebrafish curated | High within Osteichthyes; curated entries only |
| Ensembl Compara orthology (this analysis) | Structural/evolutionary (computational) | **Supports (with gap)** | SPIC is gnathostome-restricted, arose after BACH1 | SPIC absent in cyclostomes/invertebrates, present shark→mammals; 0 SPIC-without-BACH1 | 183 SPIC / 191 BACH1 species | High for presence/absence; CP status unresolved at shark boundary |
| Ensembl Compara BACH1 deep-lineage models (this analysis) | Computational | **Qualifies** (data limitation) | C-terminal CP conservation at SPIC origin | Shark/gar models anomalously long (1826/1083 aa) → mis-assembled, CP not scorable | Chondrichthyan/basal bony fish | Low-quality models; absence of motif ≠ true loss |
| [PMID: 39315605](https://pubmed.ncbi.nlm.nih.gov/39315605/) | Review | **Supports** (background) | BACH1 is a heme-binding transcriptional repressor | *"BACH1, a heme-binding transcription repressor, promotes pro-ferroptotic signalling"* | Mouse iMEF ferroptosis model | Review-level; corroborates BACH1 heme-repressor identity |
| [PMID: 42296716](https://pubmed.ncbi.nlm.nih.gov/42296716/) | Review | **Supports** (background) | BACH1 is redox/heme-sensitive repressor degraded by heme stress | *"UV-induced oxidative or heme stress promotes Bach1 nuclear export and degradation"* | Skin/keratinocytes | Review-level; confirms heme→BACH1 degradation generality |

---

## GO Curation Implications

**Lead requiring curator verification.** The evidence base supports annotating **SPIC** with its intrinsic molecular and cellular role, while attributing heme sensing to BACH1, not SPIC.

- **Molecular Function (MF):** SPIC evidence supports a **DNA-binding transcription factor** term — e.g., *DNA-binding transcription factor activity, RNA polymerase II-specific* (GO:0000981) or the more general *sequence-specific DNA binding* (GO:0043565). SPIC is an ETS-family factor; a *DNA-binding transcription factor activity* MF is informative and defensible. **Do not** annotate SPIC with *heme binding* (GO:0020037) or any heme-sensor MF — the CP motifs and heme responsiveness belong to BACH1 (F002).

- **Biological Process (BP):** Supported terms include **monocyte/macrophage differentiation** and **red pulp macrophage differentiation** (the RPM identity program) and **iron ion homeostasis** / **heme recycling** context (as a downstream developmental output). These are supported by the mouse functional study (PMID 24630724). Frame these as **downstream developmental/physiological outputs of SPIC transcriptional activity**, with heme acting upstream on BACH1, not SPIC.

- **Cellular Component (CC):** **Nucleus** (GO:0005634) is appropriate for a DNA-binding transcription factor.

- **Non-core / avoid:** Any annotation implying SPIC directly senses heme is **not core** and should be treated as a pathway-context statement about BACH1, not SPIC. "Protein binding" (GO:0005515) is not recommended as a final term — the more informative *DNA-binding transcription factor activity* is supported.

- **Evolutionary note for the review:** The co-occurrence finding is appropriate as **free-text/orthology context** supporting the lineage restriction of the RPM program, but it is **not itself a GO annotation**. It bolsters the plausibility that the mouse-demonstrated wiring is conserved across bony vertebrates without supplying direct experimental evidence of that conservation.

---

## Mechanistic Scope

The immediate molecular function under test is **transcriptional regulation**. Two distinct activities must be kept separate:

1. **BACH1 activity (heme sensing + repression):** BACH1 binds heme via C-terminal CP dipeptide motifs; heme engagement drives BACH1 degradation and relieves repression. This is the **sensing/decision** step. It is a **BACH1** function.

2. **SPIC activity (DNA binding + gene activation):** Once de-repressed, SPIC acts as a sequence-specific ETS-family transcription factor to execute the RPM differentiation program. This is SPIC's **direct gene-product activity**.

Everything else in the seed hypothesis is **downstream or inferred**:
- *Red pulp macrophage differentiation* and *iron recycling* are **downstream developmental/physiological outputs**, not direct molecular activities of SPIC.
- *Lineage restriction to gnathostomes* is an **evolutionary inference** from orthology data, not a molecular function.
- *Conserved regulatory wiring across vertebrates* is **inferred from sequence conservation**, with direct experimental demonstration only in mouse.

The hypothesis correctly places heme sensing on BACH1, but a curator must ensure that the SPIC review does not absorb BACH1's heme-sensing function by proximity.

---

## Conflicts and Alternatives

- **Paralog / alias confusion (addressed):** "BACH1" is a shared legacy alias for two unrelated proteins — the BTB-bZIP transcription factor (O14867, ~736 aa) and the BRIP1/FANCJ DNA helicase (1174–1249 aa). The analysis explicitly tracked the **BTB-bZIP TF** by length, domain architecture, and the C-terminal CP signature, avoiding carry-over error. Curators should verify any BACH1 cross-reference points to the transcription factor, not the helicase.

- **Co-occurrence ≠ conserved wiring:** The strongest alternative interpretation is that SPIC and CP-BACH1 co-occur by shared vertebrate ancestry **without** the heme→BACH1→SPIC regulatory link being conserved outside mouse. The orthology data cannot distinguish "co-present components" from "co-functioning circuit." Only mouse has direct functional data.

- **Chondrichthyan boundary ambiguity:** At the SPIC-origin boundary, unreliable BACH1 gene models mean a *true* C-terminal CP loss cannot be formally excluded. The anomalous lengths favor assembly/annotation artifact over biological loss, but this is inference, not a verified result.

- **Species scope of SPIC function:** SPIC's RPM role is best characterized in mouse spleen; human SPIC function is inferred by orthology. Organism-specific differences in the RPM program are possible and not tested here.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| CP status at chondrichthyan (SPIC-origin) boundary | Ensembl Compara BACH1 models for elephant shark, gar | This is the exact boundary where the hypothesis's prediction is most testable | Curated/manually corrected BACH1 gene model for *Callorhinchus milii*; targeted RNA-seq-based ORF reconstruction |
| Conserved regulatory wiring beyond mouse | Literature search; only PMID 24630724 gives direct functional data | Determines whether co-occurrence implies conserved function | Reporter/knockdown assays showing heme→BACH1-degradation→SPIC induction in a non-mouse vertebrate (e.g., zebrafish) |
| Human SPIC RPM function | Inferred by orthology from mouse | Annotation is for human SPIC (Q8N5J4) | Human macrophage differentiation / ChIP-seq / perturbation data |
| Direct heme non-binding by SPIC | Sequence inspection (no CP architecture in 248-aa SPIC) | Prevents erroneous heme-binding annotation on SPIC | Biophysical heme-binding assay on recombinant SPIC (expected negative) |
| Quantitative motif conservation across the full >150-species SPIC set | Matched 5-species curated panel only | Panel is small; broader sampling strengthens the inference | Automated CP-motif scoring across all curated BACH1 orthologs with alignment-anchored positions |

---

## Discriminating Tests

1. **Curated chondrichthyan BACH1 reconstruction.** Manually reconstruct the *Callorhinchus milii* BACH1 ORF from transcriptomic data and score the C-terminal CP motif. This directly tests the hypothesis at the SPIC-origin boundary where auto-annotation failed.

2. **Cross-species functional test of the circuit.** In a bony-vertebrate model (e.g., zebrafish), test whether heme exposure degrades Bach1 and de-represses spic, replicating the mouse result. This distinguishes "co-present components" from "conserved circuit."

3. **Alignment-anchored CP scoring across all curated BACH1 orthologs.** Build a multiple sequence alignment of the BACH1 bZIP + C-terminal region across the full SPIC-bearing species set and score CP conservation at the aligned position (rather than by fractional length), quantifying conservation and detecting any true losses.

4. **SPIC heme-binding negative control.** A biophysical assay (UV-vis/heme titration) on recombinant human SPIC to formally confirm SPIC does not bind heme — closing the door on any heme-binding annotation.

5. **Human SPIC perturbation + ChIP-seq.** Confirm SPIC's direct DNA-binding transcription-factor activity and RPM target genes in human cells, grounding the MF/BP annotations in human data.

---

## Curation Leads

*All items below are leads requiring curator verification.*

- **Candidate MF term:** *DNA-binding transcription factor activity, RNA polymerase II-specific* (GO:0000981) or *sequence-specific DNA binding* (GO:0043565) for SPIC. **Explicitly reject** *heme binding* (GO:0020037) for SPIC.
  - *Verify snippet:* PMID 24630724 — *"Spic expression in monocytes was constitutively inhibited by the transcriptional repressor BACH1. Heme induced proteasome-dependent BACH1 degradation and rapid Spic derepression."*

- **Candidate BP terms:** red pulp macrophage / monocyte differentiation and iron ion homeostasis as **downstream outputs** of SPIC activity. Frame heme upstream of BACH1, not SPIC.

- **Candidate CC term:** *nucleus* (GO:0005634).

- **Evolutionary free-text context (not a GO annotation):** "SPIC is a gnathostome innovation co-occurring universally with a C-terminal-CP BACH1 ortholog across bony vertebrates (0 discordant species); CP-motif conservation is robust in curated Osteichthyes but unresolved at the chondrichthyan boundary due to unreliable gene models."

- **Alias-disambiguation note:** Ensure any BACH1 reference in the SPIC review points to the **BTB-bZIP transcription factor (O14867, ~736 aa)**, not the BRIP1/FANCJ helicase sharing the "BACH1" alias.

- **Suggested curator questions:**
  1. Does the review distinguish BACH1 (heme sensor) from SPIC (downstream TF)? If not, correct any implication that SPIC senses heme.
  2. Is any heme-related GO term currently on SPIC that should be removed or reassigned to BACH1-context?

- **Suggested experiments:** chondrichthyan BACH1 ORF reconstruction; zebrafish heme→Bach1→spic reporter test; recombinant SPIC heme-binding negative control (see Discriminating Tests).

---

## Evidence Base (Literature)

- **[PMID: 24630724](https://pubmed.ncbi.nlm.nih.gov/24630724/)** — *Heme-mediated SPI-C induction promotes monocyte differentiation into iron-recycling macrophages.* The foundational functional study. Establishes that BACH1 represses Spic, that heme degrades BACH1 (proteasome-dependent) to de-repress Spic, and that **BACH1 CP motifs are necessary for heme-induced Spic induction**. This is the sole direct functional demonstration of the circuit and the anchor for both the mechanism and the "heme-sensing is BACH1" conclusion. Mouse.

- **[PMID: 39323025](https://pubmed.ncbi.nlm.nih.gov/39323025/)** — *Absolute quantification of BACH1 and BACH2 transcription factors in B and plasma cells.* Confirms BACH1/BACH2 are **regulated by direct heme binding**, corroborating that BACH1 is the heme sensor upstream of SPIC. Human/mouse B & plasma cells.

- **[PMID: 39315605](https://pubmed.ncbi.nlm.nih.gov/39315605/)** — *BACH to the ferroptosis.* Review describing BACH1 as a **"heme-binding transcription repressor"** that promotes pro-ferroptotic signaling. Background support for BACH1's identity as a heme-regulated repressor.

- **[PMID: 42296716](https://pubmed.ncbi.nlm.nih.gov/42296716/)** — *Bach transcription factors: Emerging molecular regulators for oxidative stress-mediated skin responses.* Review confirming that **heme stress promotes Bach1 nuclear export and degradation**, generalizing the heme→BACH1-degradation mechanism beyond the RPM context.

- **[PMID: 41652971](https://pubmed.ncbi.nlm.nih.gov/41652971/)** — *The neuronal ALAS2/5-ala axis mitigates chemotherapy-induced neurotoxicity via the BACH1/NRF2 pathway.* Shows heme-dependent BACH1 stability/degradation controlling downstream transcription (BACH1/NRF2), reinforcing the heme→BACH1 regulatory logic in another tissue context.

- **[PMID: 38876253](https://pubmed.ncbi.nlm.nih.gov/38876253/)** — *Endogenous small molecule effectors in GATA transcription factor mechanisms.* Places heme as a regulator acting through **BACH1** in erythroid transcriptional networks, consistent with heme sensing residing in BACH1.

- **[PMID: 39657677](https://pubmed.ncbi.nlm.nih.gov/39657677/)** — *Dual BACH1 regulation by complementary SCF-type E3 ligases.* Documents post-translational (ubiquitin-ligase) control of BACH1 stability, consistent with the proteasome-dependent BACH1 degradation step in the heme→SPIC axis.

---

## Conclusion

The seed hypothesis is **partially supported**. The requested analysis confirms the evolutionary co-occurrence prerequisites: **SPIC is a gnathostome innovation present from elephant shark through all bony vertebrates, never occurring without a BACH1 ortholog**, and the **BACH1 C-terminal heme-regulatory CP motif is positionally conserved** across curated bony-vertebrate BACH1 transcription factors (frac ~0.88, `QILAKYS..CPL` from zebrafish to human), with **no discordant species**. The hypothesis fails to reach full support on two counts: (1) the heme→BACH1→SPIC **regulatory wiring is experimentally demonstrated only in mouse**, so cross-vertebrate conservation of function is inferred rather than shown, and (2) the **CP status at the chondrichthyan boundary is unresolved** because deep-lineage gene models are unreliable. For curation, the decisive point is that **heme sensing is a BACH1 function** — SPIC should be annotated as a **nuclear DNA-binding ETS transcription factor** driving red-pulp-macrophage differentiation and iron homeostasis, and must **not** be annotated as a heme sensor or heme-binding protein.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)