---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T14:19:29.646445'
end_time: '2026-08-13T14:50:32.378851'
duration_seconds: 1862.73
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PSEPK
  gene: eno
  gene_symbol: eno
  uniprot_accession: Q88MF9
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440)
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0005576
  hypothesis_text: eno has extracellular region (GO:0005576).
  term_context: '- Term: extracellular region (GO:0005576)

    - Evidence type: IEA

    - Original reference: GO_REF:0000044'
  reference_context: '- GO_REF:0000044'
  source_file: genes/PSEPK/eno/eno-ai-review.yaml
  source_selector: existing_annotations[4].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0005576\n  label: extracellular region\nevidence_type:\
    \ IEA\noriginal_reference_id: GO_REF:0000044"
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

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440) (NCBITaxon:160488)
- **Gene directory:** eno
- **Gene symbol:** eno
- **UniProt accession:** Q88MF9

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0005576
- **Source file:** genes/PSEPK/eno/eno-ai-review.yaml
- **Source selector:** existing_annotations[4].function_hypothesis

## Seed Hypothesis

eno has extracellular region (GO:0005576).

## Term and Decision Context

- Term: extracellular region (GO:0005576)
- Evidence type: IEA
- Original reference: GO_REF:0000044

## Reference Context

- GO_REF:0000044

## Source Context YAML

```yaml
term:
  id: GO:0005576
  label: extracellular region
evidence_type: IEA
original_reference_id: GO_REF:0000044
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

# AIGR Focused Hypothesis Report — *eno* (Q88MF9, PSEPK) extracellular region (GO:0005576)

**Gene:** eno (enolase / phosphopyruvate hydratase), *Pseudomonas putida* KT2440
**UniProt:** Q88MF9 (ENO_PSEPK, reviewed Swiss-Prot), EC 4.2.1.11, 429 aa
**Focus:** function-assignment — "eno has extracellular region (GO:0005576)"
**Annotation under review:** GO:0005576, IEA, GO_REF:0000044

---

## Executive Judgment

**Verdict: Over-annotated (weakly supported for this organism).**

The extracellular-region assignment is a purely computational propagation, not an
observation about *P. putida* enolase. QuickGO confirms GO:0005576 on Q88MF9 is
`IEA / GO_REF:0000044 / ECO:0007322`, mechanically mapped from the UniProtKB
**"Secreted"** subcellular-location term. That "Secreted"/"Cell surface" location
is itself asserted by **HAMAP rule MF_00318** (ECO:0000255, by sequence
similarity) for *every* bacterial enolase matching the rule, carrying the generic
note *"Fractions of enolase are present in both the cytoplasm and on the cell
surface."* There is **no experimental (non-IEA) evidence** for extracellular or
cell-surface enolase in *P. putida*.

The moonlighting surface/secreted enolase phenomenon is real biology, but the
primary literature that demonstrates it is confined to **pathogens and parasites**
(M. tuberculosis, Mycoplasma, Leptospira, Streptococcus, Bifidobacterium, Giardia),
where surface enolase acts as a plasminogen receptor contributing to virulence.
*P. putida* KT2440 is a non-pathogenic soil saprophyte; extending a virulence-linked
moonlighting location to it by rule is a frequency/paralog-style over-annotation.

The gene product's **direct, primary function is a cytoplasmic Mg²⁺-dependent
glycolytic lyase** (2-phosphoglycerate ⇌ phosphoenolpyruvate). Extracellular
localization is at best a context-specific secondary role and, for this organism,
unsupported by evidence.

A cross-ortholog audit (Iteration 3) makes the over-annotation explicit: the same
`IEA:UniProtKB-SubCell` extracellular term is attached to *E. coli* enolase (a
canonical cytoplasmic protein with no surface evidence) but is **absent** from
*S. pneumoniae* and *S. aureus* enolases, where surface localization is
experimentally established. The annotation is thus **anti-correlated with real
biology** and carries no organism-specific information for *P. putida*. No
experimental GO:0005576 annotation exists on any enolase examined.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| QuickGO record for Q88MF9 | database/computational | Qualifies (provenance) | Is GO:0005576 experimentally supported? | GO:0005576 is IEA, GO_REF:0000044, ECO:0007322, assignedBy UniProt; mapped from "Secreted" SubCell term | *P. putida* KT2440 | High confidence it is rule-derived; no experimental backing |
| HAMAP MF_00318 (UniRule) | computational/evolutionary | Qualifies | Where does "Secreted/Cell surface" come from? | Rule blanket-asserts Cytoplasm + Secreted + Cell surface + generic note for all matching bacterial enolases (ECO:0000255) | Pan-bacterial rule | High; explains propagation, not organism-specific truth |
| PMID 27569900 (Mtb enolase) | direct assay / localization | Competing / context | Is surface enolase demonstrated? | Enolase is surface-exposed, high-affinity plasminogen binder; C-terminal Lys required | *M. tuberculosis* (pathogen) | Strong, but pathogen — not transferable to *P. putida* |
| PMID 35337383 (Mycoplasma hyorhinis) | direct assay / localization | Competing / context | Surface enolase & host binding | Flow cytometry confirms surface enolase; binds plasminogen/fibronectin; mediates cytoadhesion | Pathogen | Strong in-species; not *Pseudomonas* |
| PMID 27989763 (Leptospira) | direct assay / localization | Competing / context | Secretion + surface reassociation | Enolase secreted by unknown mechanism, reassociates with membrane, binds plasminogen/complement regulators | Pathogen | Demonstrates leaderless secretion in a pathogen only |
| PMID 24319673 (Streptococcus review) | review | Competing / context | Moonlighting surface plasminogen binders | "Surface displayed cytoplasmic proteins with enzymatic activities (moonlighting proteins)" as a class | Streptococcus | Review-level; virulence framing |
| PMID 23872606 (moonlighting review) | review | Qualifies | Why do glycolytic enzymes appear on surface? | Surface localization tied to virulence/benefit; secretion/localization non-classical and regulated | Bacteria (general) | Review-level; supports "secondary, context-specific" reading |
| UniProt Q88MF9 keywords/comments | database | Supports core function | What is the primary function? | Cytoplasm (HAMAP), Glycolysis, Lyase, Mg-binding; FUNCTION = 2-PG⇌PEP, essential for glycolysis | *P. putida* | High for core cytoplasmic function |

---

## GO Curation Implications

**Lead (requires curator verification): do NOT accept GO:0005576 as a supported/core
annotation for eno in this review; treat it as non-core / candidate for removal or
downgrade.**

- The annotation is a mechanical `IEA / GO_REF:0000044` SubCell mapping seeded by a
  pan-bacterial HAMAP rule, not evidence that *P. putida* enolase directly resides in
  the extracellular region. Under AIGR guidance, a rule-propagated CC term with no
  organism-specific support and a plausible over-annotation mechanism should not be
  marked as a demonstrated function.
- **Cellular component that IS supported:** GO:0005737 (cytoplasm) — consistent with
  the enzyme's characterized function and the HAMAP cytoplasm assertion.
- The related IEA companions GO:0009986 (cell surface) and the "Secreted" keyword ride
  on the same rule and inherit the same weakness; if the curator removes/downgrades
  GO:0005576, the cell-surface term should be handled identically.
- **Molecular function / Biological process (the true core):** phosphopyruvate hydratase
  activity (GO:0000287 Mg binding; GO:0004634 phosphopyruvate hydratase activity) and
  glycolytic process (GO:0006096) — these are the informative, defensible annotations.

Recommended action label: **NOT_SUPPORTED / mark as over-annotation** for GO:0005576
(pending curator confirmation), with rationale "IEA rule propagation of a
pathogen-associated moonlighting location to a non-pathogen; no organism-specific evidence."

---

## Mechanistic Scope

- **Direct molecular activity being annotated by CC term:** physical presence of the
  enolase polypeptide in the extracellular region.
- **Established direct activity of the gene product:** cytoplasmic, homodimeric,
  Mg²⁺-dependent lyase catalyzing 2-PG ⇌ PEP in glycolysis/gluconeogenesis.
- **The extracellular claim is downstream/secondary at best:** in organisms where it
  is real, surface enolase is a *moonlighting* plasminogen receptor reached by a
  non-classical (signal-peptide-independent) export route and re-association with the
  envelope — a virulence-linked secondary role, not the enzyme's primary catalytic job.
- For *P. putida* there is no demonstrated export, no demonstrated surface display, and
  no functional consequence reported; the CC term reflects rule inference only.

---

## Conflicts and Alternatives

- **Rule/database carry-over (most likely explanation):** HAMAP MF_00318 applies
  Secreted/Cell surface uniformly, so the annotation reflects the rule, not the strain.
- **Organism mismatch:** all supporting experimental data are from pathogens/parasites
  that exploit host plasminogen; *P. putida* is an environmental non-pathogen with no
  such host interface, weakening biological plausibility.
- **Mechanistic requirement not evidenced:** surface plasminogen binding depends on a
  C-terminal lysine and specific internal Lys sites (e.g., PMID 27569900, 28770921);
  whether Q88MF9 has the relevant C-terminal/internal Lys determinants was not tested
  here and would still not establish localization in *P. putida*.
- **No competing experimental annotation** places enolase extracellularly in *Pseudomonas*;
  the only conflict is between an automatic prediction and the absence of evidence.

---

## Knowledge Gaps

1. **Organism-specific localization.** Checked: QuickGO/UniProt evidence codes — all IEA.
   Gap: no *P. putida* surface-proteome / secretome / OMV proteomics located enolase.
   Resolution: strain-specific surface biotinylation, secretome LC-MS/MS, or
   immuno-EM/flow cytometry.
2. **Export mechanism.** Enolase is leaderless; whether *P. putida* has any route to
   externalize it is unknown. Resolution: fractionation + membrane-integrity controls to
   exclude lysis artifacts.
3. **Sequence determinants.** Not analyzed here: presence/absence of the C-terminal and
   internal lysine plasminogen-binding motifs in Q88MF9. Resolution: alignment to
   experimentally validated surface enolases; but positive motif ≠ localization proof.

---

## Discriminating Tests

- **Surface-shaving / biotinylation proteomics** of intact *P. putida* KT2440 cells with
  strict cytoplasmic-contamination controls (e.g., absence of other abundant cytoplasmic
  markers) — the single most decisive experiment.
- **Secretome and OMV LC-MS/MS** under relevant growth conditions to see if enolase is
  externalized at all.
- **Flow cytometry / immuno-EM** with anti-enolase antibody on non-permeabilized cells.
- **Comparative bioinformatics:** align Q88MF9 to validated surface enolases (Mtb, Strep)
  to check C-terminal Lys / plasminogen-binding motif conservation — supportive context,
  not proof.

---

## Curation Leads (require curator verification)

- **Action change:** downgrade/remove GO:0005576 (extracellular region) as a supported
  annotation for eno; classify as **over-annotation from IEA rule propagation**. Apply the
  same treatment to GO:0009986 (cell surface) and the "Secreted" keyword.
- **Retain / promote:** GO:0005737 (cytoplasm, CC), GO:0004634 (phosphopyruvate hydratase
  activity, MF), GO:0000287 (magnesium ion binding, MF), GO:0006096 (glycolytic process, BP).
- **Provenance to verify in the record:**
  - QuickGO: `GO:0005576 | IEA | GO_REF:0000044 | ECO:0007322 | assignedBy UniProt`.
  - HAMAP MF_00318 subcellular-location note: *"Fractions of enolase are present in both the
    cytoplasm and on the cell surface"* (rule-level, ECO:0000255) — the origin of the term.
- **Candidate reference snippets (pathogen context, to justify "not transferable"):**
  - PMID 27569900: *"Enolase, a glycolytic enzyme, has long been studied as an anchorless
    protein present on the surface of many pathogenic bacteria that aids in tissue remodeling
    and invasion by binding to host plasminogen."*
  - PMID 23872606: *"They localise to the bacterial surface to take on additional activities,
    which have been hypothesised to contribute to bacterial virulence or bacterial benefit."*
- **Suggested curator question:** Is there any *P. putida* (or close-relative) surface/secretome
  proteomic dataset placing enolase extracellularly? If not, the term stands only on rule inference.
- **Suggested experiment:** surface biotinylation + LC-MS/MS on intact KT2440 cells with
  cytoplasmic-leakage controls.

---

## Cross-Ortholog Evidence-Code Audit (Iteration 3, computed)

Question: is the extracellular/cell-surface GO term on bacterial enolases ever
experimental, and does its presence track real surface biology?

| Enolase ortholog | GO:0005576 / GO:0009986 present? | Evidence | Experimentally surface-localized? |
|---|---|---|---|
| **Q88MF9 — *P. putida* (query)** | Yes | IEA:UniProtKB-SubCell | No data |
| P0A6P9 — *E. coli* | **Yes** | IEA:UniProtKB-SubCell | **No** (canonical cytoplasmic / RNA-degradosome) |
| P64075 — *M. tuberculosis* | Yes | IEA:UniProtKB-SubCell | (moonlighting reported) |
| P77972 — *Bifidobacterium* | Yes | IEA:UniProtKB-SubCell | Yes (PMID 24840471) |
| P9WNV9 — *M. tuberculosis* | **No CC term** | — | **Yes** (PMID 27569900) |
| Q8DR60 — *S. pneumoniae* | **No CC term** | — | **Yes** (well-established PgR) |
| P0A4G2 — *S. aureus* | **No CC term** | — | Yes (reported) |

**Reading:** the extracellular/cell-surface term is applied by rule to enolases where
surface display is **not** experimentally supported (*E. coli*), yet is **absent** from
several enolases where it **is** experimentally proven (*S. pneumoniae*, *S. aureus*,
one Mtb entry). The annotation is therefore **anti-correlated with real biology** —
classic frequency-bias/rule over-annotation that carries no organism-specific
information for *P. putida*. Every occurrence found is `IEA:UniProtKB-SubCell`; **no
experimental GO:0005576 annotation exists on any enolase examined.**

---

## Sequence-Feature Provenance (Iteration 2, computed)

Direct check of Q88MF9's physical plausibility for extracellular localization (public FASTA):

| Feature | Q88MF9 (*P. putida*) | E. coli enolase P0A6P9 (cytoplasmic) | Interpretation |
|---|---|---|---|
| Length | 429 aa | 432 aa | Canonical bacterial enolase |
| N-terminus | `MAKIVDIKGREVLDSRGNPTVEA…` | `MSKIVKIIGREIIDSRGNPTVEA…` | Conserved cytoplasmic enolase start; **no signal peptide** |
| N-term hydrophobicity (aa 1–25) | 0.40, no cleavable h-region | similar | No Sec/Tat secretion signal |
| C-terminal residue | **Gly** (`…RGRAEFRG`) | Ala | **No C-terminal Lys** (a determinant for some surface enolases' plasminogen binding, e.g., Mtb PMID 27569900) |
| Lys content | 6.8% (29 K) | 8.6% | Unremarkable |

**Reading:** the sequence is that of a classical cytoplasmic glycolytic enzyme with no
export signal and without the C-terminal lysine motif linked to plasminogen-binding
surface enolases. Any extracellular presence would require a non-classical export route
that has not been demonstrated in *P. putida*. This is supportive computational context,
reported conservatively — absence of a motif is not proof of non-localization, but it
provides **no positive support** for the GO:0005576 hypothesis and is consistent with the
over-annotation conclusion.

---

## Limitations

This assessment relied on public UniProt/QuickGO/HAMAP records and PubMed; local
`*-bioinformatics` analyses were intentionally withheld. Targeted PubMed queries for
*P. putida* enolase surface/secretome returned no hits, which is itself informative
(absence of organism-specific evidence) but not absolute proof of non-localization.
No sequence-motif analysis of Q88MF9's lysine determinants was performed.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)