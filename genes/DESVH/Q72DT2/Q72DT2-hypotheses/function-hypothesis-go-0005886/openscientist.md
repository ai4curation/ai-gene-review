---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T17:55:09.260505'
end_time: '2026-09-20T18:10:24.021369'
duration_seconds: 914.76
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DESVH
  gene: Q72DT2
  gene_symbol: aprA
  uniprot_accession: Q72DT2
  taxon_id: NCBITaxon:882
  taxon_label: Nitratidesulfovibrio vulgaris (Desulfovibrio vulgaris) Hildenborough
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0005886
  hypothesis_text: Desulfovibrio vulgaris Hildenborough AprA (Q72DT2), the alpha subunit
    of adenylylsulfate reductase, localizes to the plasma membrane (GO:0005886). Distinguish
    soluble cytoplasmic enzyme from a peripheral membrane-associated pool through
    QmoABC binding. Evaluate direct fractionation, localization, complex and interaction
    evidence; membrane interaction alone may or may not establish residency. The absence
    of a transmembrane helix does not exclude peripheral membrane localization. Separate
    AprA from succinate dehydrogenase.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DESVH/Q72DT2/Q72DT2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Desulfovibrio vulgaris Hildenborough AprA (Q72DT2),\
    \ the alpha subunit of adenylylsulfate reductase,\n  localizes to the plasma membrane\
    \ (GO:0005886). Distinguish soluble cytoplasmic enzyme from a peripheral\n  membrane-associated\
    \ pool through QmoABC binding. Evaluate direct fractionation, localization, complex\n\
    \  and interaction evidence; membrane interaction alone may or may not establish\
    \ residency. The absence\n  of a transmembrane helix does not exclude peripheral\
    \ membrane localization. Separate AprA from succinate\n  dehydrogenase.\nfocus_type:\
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

- **Organism code:** DESVH
- **Taxon:** Nitratidesulfovibrio vulgaris (Desulfovibrio vulgaris) Hildenborough (NCBITaxon:882)
- **Gene directory:** Q72DT2
- **Gene symbol:** aprA
- **UniProt accession:** Q72DT2

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0005886
- **Source file:** genes/DESVH/Q72DT2/Q72DT2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Desulfovibrio vulgaris Hildenborough AprA (Q72DT2), the alpha subunit of adenylylsulfate reductase, localizes to the plasma membrane (GO:0005886). Distinguish soluble cytoplasmic enzyme from a peripheral membrane-associated pool through QmoABC binding. Evaluate direct fractionation, localization, complex and interaction evidence; membrane interaction alone may or may not establish residency. The absence of a transmembrane helix does not exclude peripheral membrane localization. Separate AprA from succinate dehydrogenase.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Desulfovibrio vulgaris Hildenborough AprA (Q72DT2), the alpha subunit of adenylylsulfate reductase,
  localizes to the plasma membrane (GO:0005886). Distinguish soluble cytoplasmic enzyme from a peripheral
  membrane-associated pool through QmoABC binding. Evaluate direct fractionation, localization, complex
  and interaction evidence; membrane interaction alone may or may not establish residency. The absence
  of a transmembrane helix does not exclude peripheral membrane localization. Separate AprA from succinate
  dehydrogenase.
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

# AIGR Deep Research — AprA (Q72DT2) plasma membrane localization (GO:0005886)

**Gene:** aprA — adenylyl-sulfate reductase, alpha subunit
**Organism:** *Nitratidesulfovibrio (Desulfovibrio) vulgaris* Hildenborough (NCBITaxon:882)
**UniProt:** Q72DT2 (664 aa; flavoprotein; SdhA/FrdA/AprA superfamily)
**Focus:** function_assignment — does AprA directly localize to the plasma membrane (GO:0005886)?

---

## Executive Judgment

**Verdict: Partially supported / weakly supported as a bare CC term — refine, do not accept as-is.**

AprA is fundamentally a **soluble cytoplasmic flavoenzyme**: the exact-strain enzyme was purified to homogeneity as a soluble αβ (α2β2) protein (PMID 8174563), and Q72DT2 has **no transmembrane helix**. The plasma-membrane annotation currently carried by UniProt (GO:0005886) rests only on **IEA:TreeGrafter**, a phylogenetic graft from the SdhA/FrdA membrane-anchored flavoprotein family, and is therefore weak and imprecise.

However, the hypothesis is not simply wrong. There is genuine **experimental** evidence for a **peripheral, partially stable membrane-associated pool** of AprAB, recruited to the cytoplasmic face of the **integral membrane QmoABC complex** (co-purification + blue-native PAGE in the exact strain, PMID 23842468; direct electron transfer, PMID 26768116). Crucially, this is a **peripheral/extrinsic association driven by protein–protein interaction, not intrinsic membrane residency**. Membrane interaction via Qmo alone does not establish residency.

**Bottom line for the curator:** The primary location is **cytoplasm (GO:0005737)**. A membrane pool is real but peripheral; if captured, it is best modeled as **extrinsic component of the cytoplasmic side of the plasma membrane (GO:0031234)** supported by IPI evidence, not as bare "plasma membrane." Separately, the co-annotated **GO:0000104 succinate dehydrogenase activity** is a paralog overannotation and should be removed.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID 8174563 (Verhagen 1994) | Direct biochemistry / purification | Refutes intrinsic membrane residency; supports soluble | Is AprAB a soluble enzyme? | Purified to homogeneity as soluble αβ (67.8/25.6 kDa), α2β2, one Fe-S cluster + FAD; no membrane anchor | *D. vulgaris* Hildenborough (exact strain) | High for solubility; predates Qmo-complex concept, did not test membrane fraction |
| PMID 23842468 (Krumholz 2013) | Interaction / co-purification / BN-PAGE | Qualifies (supports peripheral membrane pool) | Does AprAB associate with the membrane? | Membrane band contains 3 Qmo subunits + AprA + AprB; AprA/QmoA/QmoB tagging reciprocally co-purifies AprA/B; "Qmo-Apr complex at least partially stable in protein extracts" | *D. vulgaris* Hildenborough + *D. alaskensis* G20 | High for interaction; shows association via Qmo, i.e., peripheral, not integral; does not quantify soluble vs membrane partition |
| PMID 26768116 (Duarte 2016) | Direct assay (electrochemistry) | Qualifies (interaction, not residency) | Is the AprAB–Qmo link functional? | Direct QmoABC→AprAB electron transfer; Qmo essential for efficient electron delivery to sustain catalysis | *D. desulfuricans* ATCC 27774 | High for electron transfer; orthologous strain; demonstrates functional interaction, not localization |
| PMID 20581180 (Zane 2010) | Mutant phenotype | Supports Qmo being the membrane partner | Is Qmo the transmembrane electron conduit to Apr? | ΔqmoABC cannot grow on sulfate; Qmo is a transmembrane complex delivering electrons to Apr | *D. vulgaris* Hildenborough | High; establishes Qmo as membrane-integral partner of soluble Apr |
| UniProt Q72DT2 (database) | Computational / database | Competing (weak basis for GO:0005886; flags overannotation) | What is the current annotation basis? | GO:0005886 = IEA:TreeGrafter; GO:0000104 SDH activity = IEA:TreeGrafter; family = SdhA/FrdA/AprA (PF00890); 0 TM | Sequence/family | Orientation only; IEA graft from membrane-anchored SDH/FRD relatives |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current basis | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0005886 plasma membrane | CC | IEA:TreeGrafter | **Do not retain as bare term / generalize-then-specify.** Replace with **GO:0031234 extrinsic component of cytoplasmic side of plasma membrane** (or GO:0019898 extrinsic component of membrane) with IPI evidence from PMID 23842468 / 26768116. | AprAB is peripherally recruited via Qmo; no TM helix; bare "plasma membrane" overstates residency. |
| GO:0005737 cytoplasm | CC | (absent) | **Add** as primary location (IDA/IEA) | Soluble αβ enzyme purified from non-membrane fraction (PMID 8174563); no membrane anchor. |
| GO:0000104 succinate dehydrogenase activity | MF | IEA:TreeGrafter | **Remove** | Paralog overannotation from SdhA/FrdA/AprA family; AprA catalyzes APS reduction, not succinate oxidation. |
| GO:0009973 adenylyl-sulfate reductase activity | MF | IEA:UniProtKB-EC | **Retain** (core function) | Correct primary molecular function. |
| GO:0009055 electron transfer activity | MF | IEA:TreeGrafter | Retain (defensible) | Consistent with FAD/Fe-S redox chemistry and Qmo electron transfer. |

Avoids "protein binding" as the recommendation; the interaction is captured more informatively via the extrinsic-membrane CC term plus retention of the APS reductase MF term.

---

## Computed Provenance (Iteration 2 sequence analysis)

Kyte–Doolittle hydropathy analysis of the Q72DT2 sequence (664 aa) fetched live from UniProt:

| Metric | Value | Interpretation |
|---|---|---|
| Max KD hydropathy, 19-res window | **1.232** (res 25–43) | Below the ~1.6 transmembrane threshold → **no TM-length hydrophobic segment** |
| N-terminal max window (res 1–30) | 1.232 | No signal-peptide-like hydrophobic n-region |
| GRAVY (grand avg hydropathy) | **−0.371** | Hydrophilic → soluble character |
| UniProt annotated TM features | 0 | Consistent with the above |

*Provenance CSV saved to `/tmp/aprA_artifacts/seq_membrane_analysis.csv`.* This independent sequence check corroborates that AprA has **no intrinsic membrane anchor or secretion signal**; any plasma-membrane association is necessarily peripheral/extrinsic (Qmo-mediated), not integral.

**QuickGO annotation provenance (live query, EBI):** All 7 GO annotations for Q72DT2 are **electronic (IEA); none are experimental**. Critically, GO:0005886 plasma membrane carries the strong `located_in` (residency) qualifier but is assigned solely by **TreeGrafter/PANTHER (GO_REF:0000118)** — the same source as the erroneous GO:0000104 succinate dehydrogenase, GO:0050660 FAD binding, GO:0009055 electron transfer, and GO:0009061 anaerobic respiration. Only GO:0009973 (adenylyl-sulfate reductase, UniProt EC, GO_REF:0000003) and GO:0016491 (oxidoreductase, InterPro) come from non-PANTHER sources.

| GO id | Aspect | Qualifier | Evidence | AssignedBy / Ref |
|---|---|---|---|---|
| GO:0005886 plasma membrane | CC | located_in | IEA | TreeGrafter / GO_REF:0000118 |
| GO:0000104 succinate dehydrogenase activity | MF | enables | IEA | TreeGrafter / GO_REF:0000118 |
| GO:0009055 electron transfer activity | MF | enables | IEA | TreeGrafter / GO_REF:0000118 |
| GO:0050660 FAD binding | MF | enables | IEA | TreeGrafter / GO_REF:0000118 |
| GO:0009061 anaerobic respiration | BP | involved_in | IEA | TreeGrafter / GO_REF:0000118 |
| GO:0009973 adenylyl-sulfate reductase activity | MF | enables | IEA | UniProt / GO_REF:0000003 |
| GO:0016491 oxidoreductase activity | MF | enables | IEA | InterPro / GO_REF:0000002 |

The key curation point: despite direct experimental interaction/complex data existing (PMID 23842468, 26768116), the CC annotation is a pure phylogenetic graft asserting residency (`located_in`). It is both **under-evidenced and over-specified** — the experimental record supports a peripheral, Qmo-recruited pool (an IPI-supportable *extrinsic component* CC), not intrinsic plasma-membrane residency.

---

## Mechanistic Scope

- **Immediate molecular function (direct):** two-electron reduction of adenosine-5′-phosphosulfate (APS) → sulfite + AMP, using FAD and a [4Fe-4S] cluster (AprA = flavoprotein subunit; AprB = Fe-S subunit).
- **Immediate cellular context (direct):** soluble αβ enzyme in the cytoplasm that **transiently/peripherally docks onto the cytoplasmic face of the membrane-integral QmoABC complex** to receive electrons from the menaquinone pool.
- **Downstream/inferred (not localization evidence):** dissimilatory sulfate reduction growth phenotype; ΔqmoABC lethality on sulfate. These reflect the pathway, not AprA membrane residency.

---

## Conflicts and Alternatives

1. **Peripheral pool vs. residency:** Membrane co-fractionation (Krumholz) genuinely conflicts with a purely cytoplasmic model, but is fully explained by peripheral recruitment to Qmo — not intrinsic membrane insertion. Both can be true (dual pool).
2. **Paralog confusion (SdhA/FrdA):** The FAD_binding_2 family drives TreeGrafter to graft membrane-anchoring and succinate-dehydrogenase terms from SDH/FRD, where the flavoprotein subunit is tethered to membrane cytochromes. This is the likely origin of GO:0005886 and the certain origin of the erroneous GO:0000104.
3. **Partition unknown:** No study quantifies the soluble:membrane ratio of AprAB in vivo, so "resident membrane protein" cannot be asserted.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | Resolving experiment |
|---|---|---|---|
| Quantitative soluble vs. membrane partition of AprAB | Literature (PMID 8174563 soluble; 23842468 membrane pool) — no partition data | Determines whether "membrane" is a minor or major pool; affects whether a CC membrane term is warranted at all | Quantitative cell fractionation / Western of AprA in soluble vs. membrane fractions ± Qmo |
| Dependence of membrane pool on Qmo | Co-purification only | Confirms peripheral (Qmo-dependent) vs. independent membrane binding | AprA localization in ΔqmoABC background |
| Structural interface / topology of Apr–Qmo | Electrochemistry (26768116), no cryo-EM cited here | Confirms extrinsic cytoplasmic-face geometry | Cryo-EM of the Qmo–Apr supercomplex |

---

## Discriminating Tests

1. **Fractionation ± high salt / carbonate wash:** peripheral proteins strip off at high pH/salt — would confirm extrinsic (not integral) membrane association.
2. **AprA localization in ΔqmoABC:** loss of the membrane pool would prove Qmo-dependent peripheral recruitment.
3. **Cryo-EM / crosslinking of the Apr–Qmo supercomplex:** defines the cytoplasmic-face docking geometry.
4. **Family-aware GO re-annotation:** verify that GO:0005886/GO:0000104 trace to SDH/FRD ancestral grafts and are not experimentally supported for AprA.

---

## Curation Leads (require curator verification)

- **Candidate references to attach:** PMID 8174563 (soluble αβ enzyme, exact strain), PMID 23842468 (Qmo-Apr membrane co-complex, exact strain), PMID 26768116 (direct Qmo→Apr electron transfer), PMID 20581180 (Qmo membrane partner, phenotype).
  - Verify snippet — 23842468: *"This provides clear evidence for the presence of a Qmo-Apr complex that is at least partially stable in protein extracts of D. vulgaris and D. alaskensis."*
  - Verify snippet — 8174563: *"Adenosine phosphosulfate reductase from Desulfovibrio vulgaris Hildenborough has been purified to homogeneity and was found to consist of two subunits."*
  - Verify snippet — 26768116: *"the QmoABC complex is essential for efficient electron delivery to AprAB, in order to sustain catalysis."*
- **Candidate GO changes:** add GO:0005737 (cytoplasm, primary); replace bare GO:0005886 with GO:0031234 (extrinsic component of cytoplasmic side of plasma membrane, IPI); remove GO:0000104 (succinate dehydrogenase activity, paralog overannotation); retain GO:0009973.
- **Suggested curator question:** Is there any quantitative fractionation establishing AprA as a majority membrane pool? If not, treat plasma-membrane residency as non-core / peripheral only.
- **Suggested experiments:** carbonate-wash fractionation; AprA localization in ΔqmoABC.

---

## Limitations

Literature search was constrained to PubMed abstracts; UniProt was queried live (GO evidence codes, family, TM count). No local bioinformatics files were used. Snippets are quoted verbatim from retrieved abstracts and should be re-verified against source.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)