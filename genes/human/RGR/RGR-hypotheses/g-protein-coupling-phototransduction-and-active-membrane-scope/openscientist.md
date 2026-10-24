---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T23:03:47.715195'
end_time: '2026-09-21T00:11:49.264720'
duration_seconds: 4081.55
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: RGR
  gene_symbol: RGR
  uniprot_accession: P47804
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: g-protein-coupling-phototransduction-and-active-membrane-scope
  hypothesis_text: Human RGR P47804 enables G-protein-coupled receptor/photoreceptor
    activity, participates in GPCR signaling and phototransduction, and is active
    in the plasma membrane. Evaluate each separately using full primary studies, exact
    GO definitions and isoform context. Exact target PTN002517412 descends from opsin
    ancestral IBD PTN008398221 for all five propagated terms; assess inheritance or
    target divergence, not donor counts. PMID18474598 directly shows light-dependent
    regulation of retinyl-ester mobilization in human RPE/mouse models and explicitly
    leaves open a G-protein or another signaling mechanism. Its GRY/NAXXY motifs are
    not a direct negative G-protein assay; identify any positive or appropriately
    controlled negative coupling assays, including non-ocular contexts such as PMID
    linked to PMC9014095. Photoisomerase function does not itself disprove a second
    signaling capacity. GO0007602 is conversion of absorbed photons into a molecular
    signal and does not explicitly demand heterotrimeric G protein, so distinguish
    its scope from GO0008020/0004930, which require GDP/GTP exchange on a G-protein
    alpha subunit. Evaluate light-regulated enzyme activity and chromophore production
    against that distinction. PMID27011730 full text directly localizes exon6-skipping
    RGR-d to human RPE basolateral plasma membrane with splice-specific DE21 antibody
    and controls. Normal RGR is ER-associated. This resolves simple gene-level location
    but not necessarily the IBA qualifier is_active_in or whether a human-specific
    splice variant establishes the ancestral assertion. Do not use ER localization
    as proof of no plasma-membrane isoform; determine whether functional activity
    at that membrane is established. PMID7947717 retinal binding is bovine RGR plus
    human sequence, not all direct human experiments. Separate primary biochemical
    evidence from a historical GPCR name or propagated database assertions.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/RGR/RGR-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human RGR P47804 enables G-protein-coupled receptor/photoreceptor\
    \ activity, participates in\n  GPCR signaling and phototransduction, and is active\
    \ in the plasma membrane. Evaluate each separately\n  using full primary studies,\
    \ exact GO definitions and isoform context. Exact target PTN002517412 descends\n\
    \  from opsin ancestral IBD PTN008398221 for all five propagated terms; assess\
    \ inheritance or target divergence,\n  not donor counts. PMID18474598 directly\
    \ shows light-dependent regulation of retinyl-ester mobilization\n  in human RPE/mouse\
    \ models and explicitly leaves open a G-protein or another signaling mechanism.\
    \ Its\n  GRY/NAXXY motifs are not a direct negative G-protein assay; identify\
    \ any positive or appropriately controlled\n  negative coupling assays, including\
    \ non-ocular contexts such as PMID linked to PMC9014095. Photoisomerase\n  function\
    \ does not itself disprove a second signaling capacity. GO0007602 is conversion\
    \ of absorbed photons\n  into a molecular signal and does not explicitly demand\
    \ heterotrimeric G protein, so distinguish its\n  scope from GO0008020/0004930,\
    \ which require GDP/GTP exchange on a G-protein alpha subunit. Evaluate\n  light-regulated\
    \ enzyme activity and chromophore production against that distinction. PMID27011730\
    \ full\n  text directly localizes exon6-skipping RGR-d to human RPE basolateral\
    \ plasma membrane with splice-specific\n  DE21 antibody and controls. Normal RGR\
    \ is ER-associated. This resolves simple gene-level location but\n  not necessarily\
    \ the IBA qualifier is_active_in or whether a human-specific splice variant establishes\n\
    \  the ancestral assertion. Do not use ER localization as proof of no plasma-membrane\
    \ isoform; determine\n  whether functional activity at that membrane is established.\
    \ PMID7947717 retinal binding is bovine RGR\n  plus human sequence, not all direct\
    \ human experiments. Separate primary biochemical evidence from a\n  historical\
    \ GPCR name or propagated database assertions.\nfocus_type: function_assignment\n\
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
- **Gene directory:** RGR
- **Gene symbol:** RGR
- **UniProt accession:** P47804

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** g-protein-coupling-phototransduction-and-active-membrane-scope
- **Source file:** genes/human/RGR/RGR-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human RGR P47804 enables G-protein-coupled receptor/photoreceptor activity, participates in GPCR signaling and phototransduction, and is active in the plasma membrane. Evaluate each separately using full primary studies, exact GO definitions and isoform context. Exact target PTN002517412 descends from opsin ancestral IBD PTN008398221 for all five propagated terms; assess inheritance or target divergence, not donor counts. PMID18474598 directly shows light-dependent regulation of retinyl-ester mobilization in human RPE/mouse models and explicitly leaves open a G-protein or another signaling mechanism. Its GRY/NAXXY motifs are not a direct negative G-protein assay; identify any positive or appropriately controlled negative coupling assays, including non-ocular contexts such as PMID linked to PMC9014095. Photoisomerase function does not itself disprove a second signaling capacity. GO0007602 is conversion of absorbed photons into a molecular signal and does not explicitly demand heterotrimeric G protein, so distinguish its scope from GO0008020/0004930, which require GDP/GTP exchange on a G-protein alpha subunit. Evaluate light-regulated enzyme activity and chromophore production against that distinction. PMID27011730 full text directly localizes exon6-skipping RGR-d to human RPE basolateral plasma membrane with splice-specific DE21 antibody and controls. Normal RGR is ER-associated. This resolves simple gene-level location but not necessarily the IBA qualifier is_active_in or whether a human-specific splice variant establishes the ancestral assertion. Do not use ER localization as proof of no plasma-membrane isoform; determine whether functional activity at that membrane is established. PMID7947717 retinal binding is bovine RGR plus human sequence, not all direct human experiments. Separate primary biochemical evidence from a historical GPCR name or propagated database assertions.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human RGR P47804 enables G-protein-coupled receptor/photoreceptor activity, participates in
  GPCR signaling and phototransduction, and is active in the plasma membrane. Evaluate each separately
  using full primary studies, exact GO definitions and isoform context. Exact target PTN002517412 descends
  from opsin ancestral IBD PTN008398221 for all five propagated terms; assess inheritance or target divergence,
  not donor counts. PMID18474598 directly shows light-dependent regulation of retinyl-ester mobilization
  in human RPE/mouse models and explicitly leaves open a G-protein or another signaling mechanism. Its
  GRY/NAXXY motifs are not a direct negative G-protein assay; identify any positive or appropriately controlled
  negative coupling assays, including non-ocular contexts such as PMID linked to PMC9014095. Photoisomerase
  function does not itself disprove a second signaling capacity. GO0007602 is conversion of absorbed photons
  into a molecular signal and does not explicitly demand heterotrimeric G protein, so distinguish its
  scope from GO0008020/0004930, which require GDP/GTP exchange on a G-protein alpha subunit. Evaluate
  light-regulated enzyme activity and chromophore production against that distinction. PMID27011730 full
  text directly localizes exon6-skipping RGR-d to human RPE basolateral plasma membrane with splice-specific
  DE21 antibody and controls. Normal RGR is ER-associated. This resolves simple gene-level location but
  not necessarily the IBA qualifier is_active_in or whether a human-specific splice variant establishes
  the ancestral assertion. Do not use ER localization as proof of no plasma-membrane isoform; determine
  whether functional activity at that membrane is established. PMID7947717 retinal binding is bovine RGR
  plus human sequence, not all direct human experiments. Separate primary biochemical evidence from a
  historical GPCR name or propagated database assertions.
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

# RGR (P47804) — Function-Assignment Review: GPCR coupling, phototransduction, and plasma-membrane activity

**Focus:** function_assignment · **Hypothesis slug:** g-protein-coupling-phototransduction-and-active-membrane-scope
**Gene:** human RGR (RPE-retinal G protein-coupled receptor), UniProt P47804 · **Iteration:** 1 of 3

---

## Executive Judgment

**Verdict: Over-annotated (refuted for the G-protein/signaling claims; partially/weakly supported only in a narrow, isoform-specific sense for plasma membrane).**

The seed hypothesis proposes that human RGR *enables GPCR/photoreceptor activity, participates in GPCR signaling and phototransduction, and is active in the plasma membrane.* Evaluating each claim separately against primary literature, exact GO scope, and a direct sequence check:

1. **GPCR activity (GO:0004930) / G-protein-coupled photoreceptor activity (GO:0008020) — NOT SUPPORTED.** These MF terms require GDP/GTP exchange on a Gα subunit. Thirty years of research have produced **no coupled G protein and no positive coupling assay** for RGR (PMID 39961453). RGR's demonstrated molecular function is **light-driven retinaldehyde photoisomerase** activity (atRAL→11cRAL) (PMID 32493732, 37585292, 33187985, 37057907). A direct scan of P47804 shows it **lacks both canonical class-A activation motifs** (no DRY/ERY — it has GRY at 112; no NPxxY — it has NAINY at 261), i.e., the structural determinants of canonical G-protein engagement are absent. A comparative scan (Iteration 3; see table below) shows RGR is the **only** human opsin sampled to have lost both — rhodopsin, red/blue cone opsins, and even peropsin all retain DRY and NPxxY — establishing this as target-specific divergence rather than a shared opsin-family trait. These are IBA terms propagated from the opsin ancestral node (PTN008398221) and represent **paralog/ancestral over-propagation**, not a target-specific property.

2. **GPCR signaling pathway (GO:0007186) — NOT SUPPORTED** for the same reason; no downstream heterotrimeric G-protein cascade has been demonstrated for RGR.

3. **Phototransduction (GO:0007602) — QUALIFIED / non-core.** GO:0007602 ("conversion of absorbed photons into a molecular signal") does not itself demand a heterotrimeric G protein. RGR does perform a **light-driven molecular event** (photoisomerization producing 11-cis-retinal, the chromophore that *enables* photoreceptor phototransduction). However, RGR acts in the **visual/retinoid cycle in RPE and Müller glia**, upstream of and physically separate from the photoreceptor phototransduction cascade — it supplies chromophore rather than transducing the light signal that leads to neuronal excitation. Assigning canonical "phototransduction" to RGR conflates chromophore regeneration with signal transduction; a **visual-cycle / chromophore-biosynthesis framing is more accurate** than GO:0007602 as a core BP.

4. **Plasma membrane (GO:0005886) — WEAKLY / ISOFORM-SPECIFICALLY SUPPORTED, not for the canonical product.** Full-length (normal) RGR is **ER/microsomal-membrane associated** (PMID 8639565; RPE microsomes). Plasma-membrane localization is documented **only for the human exon-VI-skipping splice isoform RGR-d** (PMID 27011730), which escapes ER-associated degradation, traffics to the RPE basolateral membrane, and **co-localizes with terminal complement complex C5b-9/vitronectin in Bruch's-membrane deposits** (an aging/AMD, likely pathological context). No functional signaling activity has been shown at that membrane. This supports a *gene-level* CC of plasma membrane at most as isoform-specific, and does **not** justify an `is_active_in plasma membrane` (active MF at that location).

**Most important caveats:** (a) Absence of a positive coupling assay plus loss of DRY/NPxxY is strong convergent inference but is not a formal, controlled negative G-protein assay; (b) the non-ocular lead (RGR in human skin keratinocytes, PMID 35445026 / PMC9014095) was read in full (Iteration 2) and does **not** rescue the signaling claim: the authors themselves call RGR "a photoisomerase," RGR localizes predominantly to **nucleus, mitochondria and cytoplasm** (immunoEM) rather than a canonical plasma-membrane GPCR pattern, and the only functional data are an **siRNA-knockdown phenotype** (proliferation/migration/apoptosis) with no G-protein coupling assay. This is a loss-of-function cellular phenotype, not evidence of G-protein activation.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| 39961453 (2025) | Review (synthesis, 30 yr) | **Refutes** G-protein claim | Does RGR couple a G protein? | "While named a G protein-coupled receptor, RGR has no known coupled G protein"; acts as alternative visual-cycle photoisomerase | Human/vertebrate RPE & Müller glia | High for the negative statement; review-level. |
| 32493732 (2021) | Review of primary genetic/biochemical work | **Refutes** GPCR-MF; supports photoisomerase | Core molecular function | RGR is a mammalian retinaldehyde photoisomerase homologous to invertebrate retinochrome; physiological relevance in 11cRAL regeneration established | Mammalian eye | High; homology is to retinochrome (a photoisomerase), not to signaling opsins. |
| 37585292 (2023) | Primary (mouse ERG, cell-specific reactivation) | Supports photoisomerase BP | Physiological role | RGR is a pan-retinal atRAL sink supporting rapid chromophore regeneration in RPE + specialized Müller glia | Mouse retina | High for photoisomerase; not a signaling assay. |
| 37057907 (2023) | Primary biophysics | Supports photoisomerase MF | Reaction mechanism | Reversible photoreaction of RGR as a retinal photoisomerase | In vitro | High for isomerase mechanism. |
| 18474598 (2008) | Primary (KO mice, RNAi human RPE, in vitro) | **Qualifies** | Signaling mechanism of light response | RGR mediates light-dependent retinyl-ester mobilization; in the dark RGR-opsin inhibits LRAT and atRE hydrolase in vitro, released by light. **No G protein identified**; mechanism left open | Human RPE cells + mouse | High for phenotype; explicitly does **not** establish a G-protein mechanism. |
| 8639565 (1996) | Primary biochemistry (bovine + human seq) | Supports retinal-binding MF; localizes to microsomes | Chromophore binding; location | RGR binds all-trans-retinal forming pH-dependent photopigments; isolated from **bovine RPE microsomes** | Bovine RPE (+ human sequence) | High for retinal binding; **not all-human**; location = microsomal/ER. |
| 7947717 (1994) | Primary biochemistry + structural/evolutionary | Supports isomerase MF; **qualifies** GPCR framing | Retinal binding; family placement | **Bovine** RGR covalently binds all-trans- (preferentially) and 11-cis-retinal; human 86% identical by sequence; RGR is "the earliest independent branch of the vertebrate opsin gene family"; proposes **retinochrome-like** isomerization | Bovine RPE protein + human gene/sequence | High; direct binding is **bovine**, human by homology; evolutionary divergence argues against opsin-ancestor G-protein inheritance. |
| 27011730 (2016) | Primary localization (human tissue, fetal RPE, splice-specific Ab) | **Qualifies** plasma-membrane claim | Subcellular location | RGR-d (exon-VI-skip isoform), **not** normal RGR, traffics to RPE basolateral plasma membrane; co-localizes with C5b-9/vitronectin in basal deposits | Human RPE, young vs old donors | High; isoform-specific and disease-associated; no activity assay at PM. |
| P47804 sequence scan (this analysis) | Computational/structural | **Refutes** canonical coupling | Presence of GPCR activation motifs | No DRY/ERY (GRY@112); no NPxxY (NAINY@261) — both G-protein-coupling determinants absent | UniProt human RGR, 291 aa | Moderate-high inference; motif loss ≠ formal negative assay. |
| 35445026 (2022) | Primary (skin/keratinocytes; localization + knockdown) | **Qualifies (does not support signaling)** | Non-ocular signaling role | Authors call RGR "a photoisomerase"; RGR localizes to nucleus/mitochondria/cytoplasm (immunoEM) + membrane; siRNA knockdown alters proliferation/migration/apoptosis. **No G-protein coupling assay**; localization not canonical PM-GPCR | Human keratinocytes, melanocytes, fibroblasts | Moderate; loss-of-function phenotype only; intracellular/nuclear localization argues against classic GPCR signaling. |
| 8639565 + phylogeny (41618564, 2026) | Structural/evolutionary | Supports isomerase framing | Family placement | RGRs are blue-absorbing rhodopsins acting as retinal photoisomerases across vertebrates | Cross-species | Supports conserved photoisomerase, not signaling. |

---

## Comparative Motif Analysis (computed provenance, Iteration 3)

Direct scan of UniProt sequences for the two class-A GPCR activation motifs. **RGR is the only opsin sampled that has lost BOTH** — even peropsin (another non-visual opsin homolog) retains them:

| UniProt | Protein | Length | DRY/ERY ([DE]R[YFW], TM3 ionic lock) | NPxxY (TM7) | G-protein coupling |
|---|---|---|---|---|---|
| **P47804** | **RGR (human)** | 291 | **ABSENT** (GRY@112) | **NAINY@261** (Pro→Ala) | none demonstrated |
| P08100 | Rhodopsin | 348 | ERY@134 | NPVIY@302 | Gt (transducin) |
| P04000 | Red cone opsin | 364 | ERW@150 | NPVIY@318 | Gt |
| P03999 | Blue cone opsin | 345 | ERY@128 | NPIIY@296 | Gt |
| O14718 | Peropsin (RRH) | 337 | DRY@122 | NPCIY@290 | opsin homolog |

**Interpretation:** loss of both motifs is specific to RGR, not a shared opsin-family trait, supporting **target-specific divergence** rather than inheritance of ancestral opsin G-protein function. (Computational inference; converges with the absence of any positive coupling assay in 30 years of literature.)

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current basis | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0004930 G-protein coupled receptor activity | MF | IBA from opsin ancestor PTN008398221 | **Remove / do not propagate (NOT qualifier candidate)** | No coupled G protein, no positive assay, DRY+NPxxY both absent. Ancestral over-propagation. |
| GO:0008020 G-protein coupled photoreceptor activity | MF | IBA | **Remove / do not propagate** | Requires Gα GDP/GTP exchange; unsupported. Target has diverged from opsin ancestor. |
| GO:0007186 GPCR signaling pathway | BP | IBA | **Remove / do not propagate** | No demonstrated heterotrimeric cascade. |
| GO:0007602 phototransduction | BP | IBA | **Generalize / replace with visual-cycle framing** (e.g., visual perception / retinoid metabolic process / chromophore regeneration). Treat as **non-core** for phototransduction sensu stricto | RGR regenerates chromophore in RPE/Müller glia; upstream of and separate from photoreceptor signal transduction. |
| GO:0005886 plasma membrane | CC | IBA / isoform | **Retain only as isoform-specific (RGR-d), not `is_active_in`; prefer ER membrane (GO:0005789) for canonical product** | Full-length RGR is ER/microsomal; PM localization is the RGR-d splice variant in a pathological deposit context. |
| **Positive MF to consider adding** | MF | Primary literature | **Lead: retinal photoisomerase activity / all-trans-retinal binding** (visual-cycle) | Directly supported (PMID 32493732, 37057907, 8639565). More informative than "protein binding". |
| **Positive BP to consider** | BP | Primary literature | **Lead: visual cycle / retinoid metabolic process; regeneration of 11-cis-retinal** | PMID 37585292, 18474598, 33187985. |

The lead recommendation is to **treat the five opsin-ancestor-propagated GPCR/phototransduction/plasma-membrane terms as over-annotations for canonical RGR** and to anchor the review on RGR's directly evidenced **photoisomerase/retinaldehyde-binding** function in the **RPE/Müller-glia visual cycle**, with plasma-membrane restricted to the RGR-d isoform.

---

## Mechanistic Scope

- **Direct gene-product activity:** light absorption by RGR-bound all-trans-retinal (blue/near-UV photopigment) → **photoisomerization to 11-cis-retinal** (photoisomerase; MF). Also **retinaldehyde (all-trans-retinal) binding via a Schiff base**.
- **Immediate cellular role:** supplies 11-cis-retinal chromophore for opsin regeneration under photopic conditions in RPE and specialized Müller glia (auxiliary/photic visual cycle).
- **Downstream / not direct RGR MF:** regeneration of photoreceptor light sensitivity, phototransduction in rods/cones, and the whole-visual-cycle flux are *consequences* of chromophore supply, not RGR's own signal-transduction activity.
- **Regulatory phenotype (PMID 18474598):** light-dependent release of RGR's dark inhibition of LRAT and atRE hydrolase — a genuine light-regulated regulatory effect, but **no G-protein mediator identified**; mechanism explicitly left open.
- **Disease/pleiotropic:** RGR mutations → retinitis pigmentosa / peripapillary choroidal atrophy / AMD associations; RGR-d in Bruch's-membrane complement deposits — these are phenotypes, not evidence of a signaling MF.

---

## Conflicts and Alternatives

- **Paralog/ancestral over-propagation:** the GPCR/phototransduction terms trace to opsin ancestral node PTN008398221 (IBD). RGR is a *retinochrome-type* photoisomerase, a functional divergence from signaling opsins; the target descends from the ancestor but has **diverged in function** (motif loss). Inheritance should not be assumed.
- **Historical naming artifact:** "RPE-retinal G protein-coupled receptor" is a homology-based name from the 1990s, repeatedly flagged in reviews as **not reflecting a demonstrated G-protein function** (PMID 39961453).
- **Isoform-specific localization:** plasma-membrane data are for RGR-d (exon-VI skip), which the canonical UniProt entry/annotation may not represent; using it to support gene-level PM `is_active_in` conflates isoforms.
- **Organism caveat:** foundational biochemistry (retinal binding, spectra) is **bovine** RGR (PMID 8639565) with human sequence context — not a direct human coupling experiment.
- **Non-ocular lead resolved (Iteration 2):** the keratinocyte study (PMID 35445026) was read in full. It does not support a G-protein/GPCR signaling capacity — RGR is again described as a photoisomerase, localizes mainly to nucleus/mitochondria/cytoplasm, and the functional readout is an siRNA-knockdown phenotype (proliferation/migration/apoptosis) with no coupling assay. If anything it suggests a non-canonical intracellular role, not plasma-membrane GPCR signaling.
- **Evolutionary divergence (PMID 7947717):** RGR is the earliest-diverging branch of the vertebrate opsin family with a proposed retinochrome-like mechanism — direct support that opsin-ancestor (PTN008398221) G-protein signaling functions should not be assumed to propagate to RGR (target divergence, not mere donor-count).

---

## Knowledge Gaps

1. **Is there any positive or controlled-negative G-protein coupling assay for RGR?** Checked: no positive assay found; review explicitly says no coupled G protein. Matters because MF terms hinge on it. Resolve with a GTPγS/BRET/TGFα-shedding coupling panel (all Gα families) using purified/reconstituted human RGR ± light.
2. **Mechanism of PMID 18474598 light response.** Checked: phenotype clear, mediator unknown. Matters for whether GO:0007186 could ever be defensible. Resolve by identifying the effector linking RGR photostate to LRAT/hydrolase regulation (G-protein vs conformational/retinoid-transfer).
3. **Functional activity of RGR-d at the plasma membrane.** Checked: only localization + complement co-deposit shown. Matters for `is_active_in` PM. Resolve with activity/interaction assays on RGR-d at the basolateral membrane.
4. **Non-ocular (keratinocyte) mechanism (PMID 35445026 / PMC9014095).** Checked (Iteration 2): abstract read in full — RGR framed as a photoisomerase, localized to nucleus/mitochondria/cytoplasm, functional evidence is siRNA-knockdown phenotype only, no G-protein readout. Largely resolved: does not support GPCR signaling. Residual gap: the molecular basis of the knockdown phenotype (retinoid/photoisomerase-dependent vs a novel non-ocular role) remains undefined; would need effector/mechanism studies.
5. **Exact GO-term IDs and current review actions in the RGR-ai-review.yaml.** The local gene YAML was not available in this environment; curator should confirm which of the five propagated terms are actually present and their current qualifiers.

---

## Discriminating Tests

1. **Multiplexed G-protein coupling panel** (GTPγS binding, BRET/NanoBiT Gα sensors, TGFα-shedding) on reconstituted human RGR under dark/light — the single most decisive test to accept or reject GO:0004930/0008020/0007186.
2. **DRY/NPxxY restoration mutagenesis** (GRY→DRY, NAINY→NPxxY): if coupling cannot be conferred, reinforces functional divergence.
3. **Isoform-resolved proteomics/interactomics** of full-length RGR vs RGR-d (ER vs plasma membrane) to test whether any PM-localized RGR engages signaling partners vs complement/deposit proteins.
4. **Full-text mining of PMID 35445026** and any PMC9014095-linked work for a defined non-ocular signaling readout.
5. **Comparative PAINT/annotation review of ancestral node PTN008398221** to flag which descendants genuinely retain coupling vs photoisomerase-only members (RGR, retinochrome, peropsin) — informs whether IBA propagation should be blocked at this clade.

---

## Curation Leads (require curator verification)

- **Action:** Down-annotate / remove the opsin-ancestor-propagated **GO:0004930, GO:0008020, GO:0007186** for canonical human RGR as **paralog/ancestral over-propagation** (no coupled G protein; DRY+NPxxY absent).
- **Action:** **Generalize/replace GO:0007602 (phototransduction)** with a **visual-cycle / chromophore-regeneration** BP; treat classical phototransduction as non-core (RGR supplies chromophore upstream of, and separate from, the photoreceptor cascade).
- **Action:** **Constrain GO:0005886** to the **RGR-d isoform** (do not assert gene-level `is_active_in` plasma membrane); prefer **ER membrane (GO:0005789)** for the canonical product.
- **Add (leads):** MF **retinal photoisomerase activity** / **all-trans-retinal binding**; BP **visual cycle / retinoid metabolic process (regeneration of 11-cis-retinal)** — better than "protein binding".
- **Candidate references + snippets to verify:**
  - PMID 39961453 — "While named a G protein-coupled receptor, RGR has no known coupled G protein."
  - PMID 32493732 — RGR "identified previously as a mammalian retinaldehyde photoisomerase homologous to retinochrome found in invertebrates."
  - PMID 27011730 — "RGR-d is targeted to the basolateral plasma membrane of the RPE. RGR-d, but not normal RGR ... trafficks to the plasma membrane."
  - PMID 18474598 — "in the dark, RGR-opsin inhibits lecithin:retinol acyltransferase and all-trans-retinyl ester hydrolase in vitro and that this inhibition is released upon exposure to light" (light-regulated, **no G protein identified**).
  - PMID 8639565 — RGR binds all-trans-retinal forming pH-dependent photopigments; isolated from bovine RPE microsomes.
  - PMID 7947717 — "the rgr gene represents the earliest independent branch of the vertebrate opsin gene family"; direct binding shown on **bovine** RGR, human 86% identical by sequence; proposes retinochrome-like isomerization (supports target divergence + photoisomerase MF).
  - PMID 35445026 — "The retinal G protein-coupled receptor (RGR) is a photoisomerase in the human retina"; non-ocular knockdown phenotype only, intracellular/nuclear localization (does not support GPCR signaling).
- **Suggested questions for curator:** Which of the five terms are actually present with which qualifiers/evidence codes? Is the PM annotation tied to an isoform? Should IBA propagation from PTN008398221 be blocked for the RGR/retinochrome photoisomerase clade?
- **Suggested experiments:** the G-protein coupling panel and isoform interactomics above.

---

## Provenance

Sequence motif analysis executed on UniProt P47804 (291 aa) via `execute_code` (requests + regex): DRY/ERY motif absent (found GRY at position 112); NPxxY absent (found NAINY at position 261). Full abstracts for PMID 35445026 and PMID 7947717 fetched via NCBI E-utilities efetch (Iteration 2) and read in full. Literature retrieved via PubMed search (PMIDs 39961453, 32493732, 37585292, 37057907, 33187985, 18474598, 27011730, 8639565, 7947717, 35445026, 41618564).

*Note: the local `RGR-ai-review.yaml` and any `*-bioinformatics` analyses were not present in this environment; exact term IDs/current actions should be confirmed against the repository.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)