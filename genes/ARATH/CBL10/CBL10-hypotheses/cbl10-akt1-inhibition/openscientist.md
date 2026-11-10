---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:52:25.908700'
end_time: '2026-10-24T05:18:20.848439'
duration_seconds: 1554.94
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ARATH
  gene: CBL10
  gene_symbol: CBL10
  uniprot_accession: Q7FRS8
  taxon_id: NCBITaxon:3702
  taxon_label: Arabidopsis thaliana
  focus_type: free_text
  hypothesis_slug: cbl10-akt1-inhibition
  hypothesis_text: Arabidopsis CBL10 (Q7FRS8) directly inhibits the inward-rectifying
    K+ channel AKT1 by physical binding, independently of CIPK kinase activity, as
    reported by Ren et al. 2013 (PMID:23331977); this inhibition has been independently
    replicated or corroborated in planta (e.g. cbl10 mutant root K+ currents or K+
    content) and is not contradicted by later work.
  term_context: '- Term: potassium channel inhibitor activity (GO:0019870)

    - Test by literature: find every study after 2013 that measured CBL10 effects
    on AKT1 currents, root K+ uptake or K+/Na+ content in cbl10 loss-of-function or
    overexpression lines, and state whether each supports, fails to replicate, or
    contradicts direct, kinase-independent AKT1 inhibition. Distinguish physical interaction
    (Y2H/BiFC) from functional inhibition, and oocyte data from in-planta data.'
  reference_context: '- PMID:23331977'
  source_file: genes/ARATH/CBL10/CBL10-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Arabidopsis CBL10 (Q7FRS8) directly inhibits the\
    \ inward-rectifying K+ channel AKT1 by physical\n  binding, independently of CIPK\
    \ kinase activity, as reported by Ren et al. 2013 (PMID:23331977); this\n  inhibition\
    \ has been independently replicated or corroborated in planta (e.g. cbl10 mutant\
    \ root K+ currents\n  or K+ content) and is not contradicted by later work.\n\
    focus_type: free_text\nterm_id: GO:0019870\nterm_label: potassium channel inhibitor\
    \ activity\ncontext:\n- 'Test by literature: find every study after 2013 that\
    \ measured CBL10 effects on AKT1 currents, root\n  K+ uptake or K+/Na+ content\
    \ in cbl10 loss-of-function or overexpression lines, and state whether each\n\
    \  supports, fails to replicate, or contradicts direct, kinase-independent AKT1\
    \ inhibition. Distinguish\n  physical interaction (Y2H/BiFC) from functional inhibition,\
    \ and oocyte data from in-planta data.'\nreference_id:\n- PMID:23331977"
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
citation_count: 10
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

- **Organism code:** ARATH
- **Taxon:** Arabidopsis thaliana (NCBITaxon:3702)
- **Gene directory:** CBL10
- **Gene symbol:** CBL10
- **UniProt accession:** Q7FRS8

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** cbl10-akt1-inhibition
- **Source file:** genes/ARATH/CBL10/CBL10-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Arabidopsis CBL10 (Q7FRS8) directly inhibits the inward-rectifying K+ channel AKT1 by physical binding, independently of CIPK kinase activity, as reported by Ren et al. 2013 (PMID:23331977); this inhibition has been independently replicated or corroborated in planta (e.g. cbl10 mutant root K+ currents or K+ content) and is not contradicted by later work.

## Term and Decision Context

- Term: potassium channel inhibitor activity (GO:0019870)
- Test by literature: find every study after 2013 that measured CBL10 effects on AKT1 currents, root K+ uptake or K+/Na+ content in cbl10 loss-of-function or overexpression lines, and state whether each supports, fails to replicate, or contradicts direct, kinase-independent AKT1 inhibition. Distinguish physical interaction (Y2H/BiFC) from functional inhibition, and oocyte data from in-planta data.

## Reference Context

- PMID:23331977

## Source Context YAML

```yaml
hypothesis: Arabidopsis CBL10 (Q7FRS8) directly inhibits the inward-rectifying K+ channel AKT1 by physical
  binding, independently of CIPK kinase activity, as reported by Ren et al. 2013 (PMID:23331977); this
  inhibition has been independently replicated or corroborated in planta (e.g. cbl10 mutant root K+ currents
  or K+ content) and is not contradicted by later work.
focus_type: free_text
term_id: GO:0019870
term_label: potassium channel inhibitor activity
context:
- 'Test by literature: find every study after 2013 that measured CBL10 effects on AKT1 currents, root
  K+ uptake or K+/Na+ content in cbl10 loss-of-function or overexpression lines, and state whether each
  supports, fails to replicate, or contradicts direct, kinase-independent AKT1 inhibition. Distinguish
  physical interaction (Y2H/BiFC) from functional inhibition, and oocyte data from in-planta data.'
reference_id:
- PMID:23331977
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

# CBL10–AKT1 Kinase-Independent Inhibition: A Hypothesis-Level Curation Review

**Target gene:** CBL10 (Calcineurin B-Like protein 10), *Arabidopsis thaliana* (ARATH, NCBITaxon:3702)
**UniProt:** Q7FRS8
**Hypothesis slug:** cbl10-akt1-inhibition
**GO term under test:** GO:0019870 — *potassium channel inhibitor activity* (MF)
**Seed reference:** [PMID: 23331977](https://pubmed.ncbi.nlm.nih.gov/23331977/) (Ren et al. 2013)

---

## Executive Judgment

**Verdict: Partially supported, single-source, non-core — adding GO:0019870 would be over-annotation.**

The seed hypothesis has two parts, and they diverge sharply in strength. The first part — that CBL10 directly inhibits the inward-rectifying K⁺ channel AKT1 by physical binding, independently of CIPK kinase activity — is **accurately reported** by Ren et al. 2013 and is internally well-supported within that single paper. The authors assembled a genuinely multi-method evidence package: physical interaction by yeast two-hybrid (Y2H), bimolecular fluorescence complementation (BiFC), and co-immunoprecipitation (co-IP); functional impairment of AKT1-mediated inward K⁺ currents in **two** independent electrophysiological systems (*Xenopus* oocytes and Arabidopsis root-cell protoplasts); CBL10-overexpression lines phenocopying *akt1* loss-of-function (low-K⁺ sensitivity, reduced K⁺ content); and a Y2H competition assay suggesting CBL10 competes with CIPK23 for AKT1 binding.

The **second part** of the hypothesis — that this inhibition "has been independently replicated or corroborated in planta … and is not contradicted by later work" — **fails**. A systematic replication audit (NCBI ELink `citedin` on all 76 PubMed articles citing PMID:23331977 through 2026, plus a 105-record Europe PMC full-text co-mention search for "CBL10" AND "AKT1") found **zero** independent primary studies that re-measured CBL10 effects on AKT1 currents or on root K⁺ in *cbl10* loss-of-function lines. The in-planta support that does exist is overexpression-based, not derived from *cbl10*-null plants, so it cannot distinguish a physiological inhibitory role from an overexpression artifact. Later works citing the CBL10–AKT1 link are reviews, not replications.

Critically for curation: **GO:0019870 is not currently annotated to CBL10.** QuickGO retrieval for Q7FRS8 shows that the two annotations derived from Ren 2013 are the conservative BP term **GO:0043266 (regulation of potassium ion transport, IMP)** and **GO:0005515 (protein binding, IPI)** — not the specific inhibitor MF term. The evidence does not justify promoting the regulatory claim to a dedicated molecular-function inhibitor term, for three reasons: (1) it rests on a single laboratory with no independent replication; (2) the in-planta data are overexpression-only; and (3) CBL10's behavior toward K⁺ transport systems is not uniformly inhibitory — it *activates* the high-affinity K⁺ transporter HAK5 in a kinase-*dependent* manner (Ragel et al. 2015), the opposite sign and opposite mechanism from the AKT1 story. The recommended action is to **retain the conservative GO:0043266 annotation as non-core and reject the proposed GO:0019870 term.**

---

## Key Findings

### Finding 1 — Ren 2013 is the sole primary source; no independent in-planta replication exists post-2013

Ren et al. 2013 ([PMID: 23331977](https://pubmed.ncbi.nlm.nih.gov/23331977/)) remains the **only** primary report of CBL10's direct, kinase-independent inhibition of AKT1. The paper itself is methodologically thorough. It reports, in the authors' own words, that *"CBL10 directly interacted with AKT1, as verified in yeast two-hybrid, BiFC and co-immunoprecipitation experiments,"* and that *"the results of electrophysiological analysis in both Xenopus oocytes and Arabidopsis root cell protoplasts demonstrated that CBL10 impairs AKT1-mediated inward K⁺ currents."* The mechanistic claim is explicit: *"the present study revealed a CBL-interacting protein kinase-independent regulatory mechanism of calcineurin B-like proteins in which CBL10 directly regulates AKT1 activity and affects ion homeostasis in plant cells."*

The replication audit was deliberately exhaustive. Using NCBI ELink `citedin`, all 76 PubMed articles citing PMID:23331977 through 2026 were enumerated and screened; a complementary Europe PMC full-text search for co-mentions of "CBL10" and "AKT1" returned 105 records. **None** of these constitutes an independent primary re-measurement of CBL10 effects on AKT1 inward currents or on root K⁺ content in *cbl10* loss-of-function lines. The AKT1-focused follow-up literature instead converges on different regulators: AtKC1 and CIPK23 (PMID:26829980) and the structural basis of CIPK23 recognition of AKT1 (PMID:32015077) — neither of which involves CBL10. Works that do cite the CBL10–AKT1 link (e.g., PMID:33519853, PMID:27618104, PMID:32117382) are review articles that propagate the original claim rather than test it.

This matters for curation because single-source, unreplicated functional claims — even internally strong ones — warrant conservative annotation. The claim is credible but not corroborated.

### Finding 2 — CBL10's effect on K⁺ transport is context-dependent, not uniformly inhibitory

The hypothesis treats CBL10 as a K⁺ *channel inhibitor*, but CBL10's documented relationship with K⁺ transport systems is bidirectional. Ragel et al. 2015 ([PMID: 26474642](https://pubmed.ncbi.nlm.nih.gov/26474642/)) showed that *"the Ca²⁺ sensors calcineurin B-like (CBL1), CBL8, CBL9, and CBL10, together with CBL-interacting protein kinase23 (CIPK23), activated HAK5 in vivo,"* increasing both the K⁺ affinity and Vmax of the high-affinity K⁺ transporter HAK5 via CIPK23-mediated phosphorylation of the HAK5 N-terminus.

This is the opposite sign and opposite mechanism from the AKT1 story:

| Property | CBL10 → AKT1 (Ren 2013) | CBL10 → HAK5 (Ragel 2015) |
|---|---|---|
| Direction | Inhibition (negative) | Activation (positive) |
| CIPK dependence | Kinase-**independent** | Kinase-**dependent** (CIPK23) |
| Target | Inward-rectifying channel | High-affinity transporter |
| System | Oocytes + root protoplasts | Heterologous HAK5 reconstitution |

A single gene product that both activates one K⁺ uptake system (kinase-dependently) and inhibits another (kinase-independently) cannot cleanly carry a uniform molecular-function term of "potassium channel inhibitor activity." The 2020/2021 CBL10 review (PMID:33519853) itself frames CBL10 as versatile — able to "activate (in a CIPK-dependent manner) or repress (by direct interaction) downstream targets" at different subcellular locations. This context-dependence argues against a specific inhibitor MF term and in favor of the more neutral regulatory BP term.

### Finding 3 — GO:0019870 is NOT currently annotated; the existing Ren-2013 annotations are conservative

A QuickGO annotation retrieval for Q7FRS8 returned 23 annotations. The two that trace to PMID:23331977 are:

- **GO:0043266** — *regulation of potassium ion transport* (BP; IMP / ECO:0000315; TAIR)
- **GO:0005515** — *protein binding* (MF; IPI / ECO:0000353; TAIR)

The molecular-function term under test, **GO:0019870 (potassium channel inhibitor activity), is absent** from the current annotation set. The protein-binding annotation is supported directly by the Ren 2013 interaction data: *"CBL10 directly interacted with AKT1, as verified in yeast two-hybrid, BiFC and co-immunoprecipitation experiments."*

CBL10's remaining annotations center on its core, independently replicated biology: calcium ion binding (GO:0005509, IDA PMID:17449811), kinase binding (GO:0019900), hyperosmotic salinity response (GO:0042538, IMP PMID:17825054), monoatomic ion homeostasis (GO:0050801), detection of calcium ion (GO:0005513), calcium-mediated signaling (GO:0019722); and localization to the plant-type vacuole membrane (GO:0009705, IDA PMID:17825054), plasma membrane (GO:0005886, IDA PMID:17449811), vacuolar membrane, cytoplasm, and endosome. This is the profile of a **Ca²⁺ sensor** whose primary characterized role is Na⁺ compartmentation and salt tolerance — not a dedicated channel inhibitor.

### Finding 4 — Final verdict: partially supported, over-annotation if promoted to GO:0019870

Consolidating the three-part audit:

1. **Internal strength (positive):** Ren 2013 provides multi-method evidence — Y2H + BiFC + co-IP interaction; AKT1 inward-current impairment in oocytes *and* root protoplasts; CBL10-OE phenocopying *akt1*; and a CIPK23 competition assay. The mechanism proposed is competitive displacement: *"the results from the yeast two-hybrid competition assay indicated that CBL10 may compete with CIPK23 for binding to AKT1 and negatively modulate AKT1 activity."* Note the hedged "may" from the single source.
2. **Replication (negative):** 76/76 citing papers and 105 Europe PMC records screened → 0 independent primary replications of AKT1-current inhibition; in-planta support is overexpression-only, not *cbl10*-null.
3. **Conflicts (negative/qualifying):** CBL10 activates HAK5 kinase-dependently (PMID:26474642); the mainstream AKT1 negative regulator is AtKC1 (PMID:26829980); CBL10 is absent from the CIPK23 structural activation model (PMID:32015077); and CBL10's core replicated function is Ca²⁺-sensor-mediated Na⁺/salt tolerance (PMID:31100786, PMID:17825054).

The mechanism described — competitive displacement of an activating kinase (CIPK23) from the channel — is more naturally captured by a *regulation* term than by an intrinsic *inhibitor activity* term, because the "inhibition" is competitive and context-dependent rather than a stoichiometric channel-blocking activity.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 23331977](https://pubmed.ncbi.nlm.nih.gov/23331977/) Ren 2013 | Direct assay + interaction + mutant/OE phenotype | **Supports** | CBL10 directly, kinase-independently inhibits AKT1 | Y2H/BiFC/co-IP interaction; AKT1 inward K⁺ current impaired in oocytes AND root protoplasts; CBL10-OE phenocopies *akt1*; CBL10 competes with CIPK23 | Arabidopsis roots; *Xenopus* oocytes; root protoplasts | High internal quality, but single-lab; in-planta evidence is OE-only; competition claim hedged ("may") |
| [PMID: 26474642](https://pubmed.ncbi.nlm.nih.gov/26474642/) Ragel 2015 | Direct assay (heterologous) | **Qualifies / competes** | Uniform K⁺-channel-inhibitor role | CBL10 (with CBL1/8/9 + CIPK23) *activates* HAK5, increasing K⁺ affinity & Vmax — opposite sign, kinase-dependent | Heterologous HAK5 reconstitution | Shows CBL10 is bidirectional on K⁺ transport; undermines a uniform inhibitor MF term |
| QuickGO (Q7FRS8) | Database | **Qualifies** | Is GO:0019870 currently annotated? | GO:0019870 absent; Ren-2013 terms are GO:0043266 (BP, IMP) + GO:0005515 (MF, IPI) | GO annotation set, 23 terms | Database-level; reflects current curation, confirms the term is a *new* proposal |
| PMID:26829980 (AtKC1/CIPK23) | Direct assay | **Competing** | Who negatively regulates AKT1? | AtKC1 is the characterized negative regulator of AKT1; no CBL10 involvement | Arabidopsis roots | Orientation; points to an alternative, replicated inhibitor |
| PMID:32015077 (CIPK23–AKT1 structure) | Structural | **Competing** | Mechanism of AKT1 regulation | Structural basis of CIPK23 activation of AKT1; CBL10 absent from the model | Structural biology | Orientation; CBL10 not part of mainstream AKT1 activation model |
| [PMID: 31100786](https://pubmed.ncbi.nlm.nih.gov/31100786/) | Mutant phenotype | **Qualifies** | CBL10's core function | CBL10 mediates salt-tolerance pathways (Na⁺ focus), with CBL4 | Arabidopsis | Reinforces Ca²⁺-sensor/Na⁺ core role over K⁺-channel inhibition |
| PMID:33519853 (CBL10 review) | Review | **Qualifies** | Is CBL10 a uniform inhibitor? | CBL10 described as versatile: can "activate (CIPK-dependent) or repress (direct interaction)" targets | Review | Review-level synthesis; not a replication |
| [PMID: 32117382](https://pubmed.ncbi.nlm.nih.gov/32117382/) | Review | Orientation | CBL-CIPK nutrient regulation | Frames CBL-CIPK systems in nutrient uptake/balance | Review | Review-level orientation only |

---

## Mechanistic Model / Interpretation

The immediate molecular function under test is whether CBL10 **intrinsically inhibits the AKT1 channel** by direct physical binding, independent of CIPK kinase activity. The Ren 2013 model is best represented as competitive regulation rather than channel blockade:

```
   ACTIVATING PATHWAY (canonical)          PROPOSED CBL10 PATHWAY (Ren 2013)
   ------------------------------          --------------------------------
   CBL1/9  →  CIPK23  →  (phospho)         CBL10  —|  AKT1   (direct binding,
      |                      |                        |       no kinase step)
      └──→ binds AKT1 ───────┘                        └─ competes with CIPK23
           ↑ AKT1 inward K+ current ↑           ↓ AKT1 inward K+ current ↓
```

**Direct gene-product activity** (what the MF term would assert): physical binding to AKT1 and reduction of AKT1 inward K⁺ current. This is supported *in vitro/oocyte* and in root protoplasts within one study.

**Downstream / inferred effects** (NOT the MF term): altered root K⁺ uptake, K⁺/Na⁺ content, and low-K⁺ sensitivity. In Ren 2013 these in-planta readouts come from **overexpression** lines, so they report the consequence of excess CBL10, not the physiological requirement for CBL10 — a *cbl10*-null phenotype on AKT1 currents or root K⁺ was not demonstrated. CBL10's primary, independently replicated function is as a Ca²⁺ sensor controlling Na⁺ compartmentation and salt tolerance via CIPK24/SOS2 at the tonoplast and plasma membrane. The AKT1-inhibition activity, even if real, is a secondary/context-specific branch of CBL10 biology.

The competing interpretation is important: because the mechanism is competitive displacement of an *activating* kinase (CIPK23) rather than a stoichiometric pore block, the correct ontology representation is a *regulation* relationship (GO:0043266), not an intrinsic inhibitor molecular activity (GO:0019870). Molecular-function "inhibitor activity" terms imply a direct, defined inhibitory biochemical action; a competitive binder that merely excludes a positive regulator does not satisfy that definition cleanly.

---

## Evidence Base

- ***Calcineurin B-like protein CBL10 directly interacts with AKT1 and modulates K⁺ homeostasis in Arabidopsis*** — [PMID: 23331977](https://pubmed.ncbi.nlm.nih.gov/23331977/). The seed and sole primary source. Provides the complete evidence package (interaction, two-system electrophysiology, OE phenotype, CIPK23 competition). **Supports** the molecular claim but is single-lab and uses OE for in-planta readouts.
- ***The CBL-Interacting Protein Kinase CIPK23 Regulates HAK5-Mediated High-Affinity K⁺ Uptake in Arabidopsis Roots*** — [PMID: 26474642](https://pubmed.ncbi.nlm.nih.gov/26474642/). Shows CBL10 *activates* HAK5 kinase-dependently. **Qualifies/competes** with a uniform inhibitor assignment by demonstrating opposite-sign, opposite-mechanism behavior on a different K⁺ system.
- ***Calcineurin B-Like Proteins CBL4 and CBL10 Mediate Two Independent Salt Tolerance Pathways*** — [PMID: 31100786](https://pubmed.ncbi.nlm.nih.gov/31100786/). Reinforces CBL10's core Ca²⁺-sensor/Na⁺-salt-tolerance role, contextualizing AKT1 inhibition as non-core.
- ***Calcium-Regulated Phosphorylation Systems Controlling Uptake and Balance of Plant Nutrients*** — [PMID: 32117382](https://pubmed.ncbi.nlm.nih.gov/32117382/). Review-level orientation on CBL-CIPK nutrient control; propagates (does not replicate) the CBL10–AKT1 link.
- AtKC1/CIPK23 (PMID:26829980) and CIPK23–AKT1 structure (PMID:32015077): the mainstream AKT1 regulatory literature, in which AtKC1 is the characterized negative regulator and CBL10 does not appear — **competing** context the curator should weigh.
- CBL10 review (PMID:33519853): review-level synthesis describing CBL10 as a versatile activator-or-repressor.

---

## GO Curation Implications

**Lead (requires curator verification):** Do **not** add GO:0019870 (potassium channel inhibitor activity) to CBL10/Q7FRS8. Retain the existing conservative annotations derived from Ren 2013 and treat them as **non-core**.

- **Molecular Function:** The specific MF term GO:0019870 is not justified. The underlying activity is a *competitive, context-dependent* modulation (displacement of CIPK23) rather than an intrinsic channel-blocking activity, and CBL10 shows the opposite (activating) effect on HAK5. The existing MF annotation GO:0005515 (protein binding, IPI) is defensible from the interaction data, though it should be viewed as minimally informative; a more specific MF is not supported by replicated evidence. If any MF were considered, "calcium ion binding" (GO:0005509, IDA) and "kinase binding" (GO:0019900) better reflect CBL10's core, replicated molecular activities.
- **Biological Process:** **Retain GO:0043266 (regulation of potassium ion transport, IMP)** as the appropriate, conservative representation of the Ren 2013 result. It captures the regulatory relationship without overcommitting to a mechanism (inhibition) that is single-source and context-dependent.
- **Cellular Component:** No change prompted by this hypothesis; CBL10's CC annotations (plasma membrane, vacuolar/tonoplast membrane) are independently supported (IDA, PMID:17449811, PMID:17825054).

**Net action:** Reject the proposed GO:0019870; keep GO:0043266 + GO:0005515 as non-core, single-source annotations pending independent replication.

---

## Conflicts and Alternatives

1. **Opposite-sign activity on HAK5 (PMID:26474642):** CBL10 positively and kinase-dependently activates HAK5, directly conflicting with a blanket "K⁺ channel inhibitor" characterization and implying that CBL10's effect depends on the target and the CIPK partner.
2. **Alternative AKT1 negative regulator (AtKC1):** The replicated, mainstream negative regulator of AKT1 is AtKC1 (PMID:26829980), and the canonical AKT1-activation model is built on CIPK23 (PMID:32015077) — CBL10 is absent from both. The curation risk is attributing a specific inhibitor MF to CBL10 when the field's consensus AKT1 inhibitor is a different protein.
3. **Overexpression artifact risk:** The in-planta readouts in Ren 2013 are overexpression-based. Overexpressed CBL10 may titrate shared CIPK partners or mislocalize, producing phenotypes that do not reflect endogenous function — a classic source of over-interpretation.
4. **Mechanism mismatch:** The proposed mechanism is competitive displacement of CIPK23 ("may compete"), which is a *regulatory* interaction, not a stoichiometric pore block. GO:0019870 implies an intrinsic inhibitory molecular activity that the competition model does not cleanly satisfy.
5. **No paralog confusion detected, but adjacent:** CBL10 is one of ten Arabidopsis CBLs; the HAK5 study shows CBL1/8/9/10 act partly redundantly. Curators should ensure AKT1-inhibition annotations are not generalized across the CBL family from a CBL10-specific (and unreplicated) observation.

---

## Limitations and Knowledge Gaps

- **No independent replication (checked: 76 citing papers + 105 Europe PMC records; found: 0).** Why it matters: single-source functional claims are fragile; GO best practice favors conservative terms until corroborated. Resolution: an independent lab re-measuring AKT1 currents with/without CBL10.
- **No *cbl10* loss-of-function electrophysiology (checked: Ren 2013 used OE for in-planta readouts).** Why it matters: OE phenotypes cannot establish a physiological requirement for CBL10 in restraining AKT1. Resolution: AKT1 inward-current and root K⁺-uptake measurements in a *cbl10*-null background.
- **Mechanistic ambiguity of "inhibition" (checked: competition assay hedged as "may").** Why it matters: distinguishes an intrinsic MF (GO:0019870) from a competitive regulatory interaction (better served by GO:0043266). Resolution: reconstitution with defined CBL10:CIPK23:AKT1 stoichiometry and direct biophysical binding/competition constants.
- **Localization/compartment match (checked: CBL10 annotated at tonoplast + PM; AKT1 is PM).** Why it matters: an inhibitory interaction requires co-localization at the plasma membrane; CBL10's dominant characterized role is tonoplast/Na⁺. Resolution: quantitative co-localization and in vivo interaction at the PM under physiological conditions.
- **No structural data for a CBL10–AKT1 complex (checked: structural literature covers CIPK23–AKT1 only).** Why it matters: structure would clarify whether CBL10 occludes the CIPK23 site or acts allosterically. Resolution: cryo-EM/crystallography or AlphaFold-Multimer modeling of CBL10–AKT1.

---

## Discriminating Tests

1. **Independent *cbl10*-null electrophysiology:** Measure AKT1-mediated inward K⁺ currents in root protoplasts from *cbl10* loss-of-function vs. wild type (and vs. *akt1*). A physiological inhibitory role predicts *increased* AKT1 current in *cbl10*-null plants. This is the single most decisive missing experiment.
2. **Root K⁺ uptake/content in *cbl10*-null under low K⁺:** Directly test whether endogenous CBL10 restrains K⁺ uptake, complementing OE data.
3. **Kinase-independence confirmation:** Reconstitute AKT1 in oocytes with a non-catalytic CIPK (or no CIPK) ± CBL10, and with a CBL10 variant unable to bind CIPKs, to confirm inhibition is CIPK-independent in a second lab.
4. **Competition quantification:** Measure binding/competition constants for CBL10 vs. CIPK23 on AKT1 (SPR/ITC/BLI) to decide whether "inhibition" is competitive displacement (→ GO:0043266) or an intrinsic block (→ GO:0019870).
5. **AlphaFold-Multimer CBL10–AKT1 vs. CIPK23–AKT1 modeling:** A public, programmatic comparison to test whether CBL10 plausibly occupies the CIPK23-binding surface of AKT1.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**All items below are leads requiring curator verification.**

- **Action:** Reject the proposed addition of **GO:0019870 (potassium channel inhibitor activity)** to CBL10/Q7FRS8. Retain **GO:0043266 (regulation of potassium ion transport, IMP, from PMID:23331977)** and **GO:0005515 (protein binding, IPI)** as **non-core, single-source** annotations.
- **Candidate reference + snippet to verify (supports regulatory, not inhibitor-MF, interpretation):** PMID:23331977 — *"the results from the yeast two-hybrid competition assay indicated that CBL10 may compete with CIPK23 for binding to AKT1 and negatively modulate AKT1 activity."* Verify that "may compete" and "modulate" are preserved to avoid over-strong wording.
- **Candidate conflicting reference + snippet:** PMID:26474642 — *"the Ca²⁺ sensors calcineurin B-like (CBL1), CBL8, CBL9, and CBL10, together with CBL-interacting protein kinase23 (CIPK23), activated HAK5 in vivo."* Verify and flag as evidence against a uniform inhibitor MF term.
- **Candidate GO term (if any MF change is desired):** Prefer no new specific MF; if a BP qualifier is wanted, GO:0043266 already covers the relationship. Do **not** promote to GO:0019870.
- **Suggested curator questions:** (1) Has any post-2013 study measured AKT1 currents or root K⁺ in a *cbl10*-null? (2) Is the "inhibition" competitive (CIPK23 displacement) or intrinsic? (3) Should CBL10's bidirectional K⁺-transport behavior preclude a specific inhibitor MF?
- **Suggested experiments (for the review's "needs evidence" field):** *cbl10*-null AKT1 electrophysiology; *cbl10*-null root K⁺ uptake; independent-lab oocyte reconstitution; CBL10–AKT1 binding/competition thermodynamics.

---

## Summary Table — Hypothesis Scorecard

| Hypothesis component | Verdict | Basis |
|---|---|---|
| CBL10 physically binds AKT1 | **Supported** | Y2H + BiFC + co-IP (PMID:23331977) |
| Binding inhibits AKT1 inward K⁺ current | **Supported (single-source)** | Oocytes + root protoplasts (PMID:23331977) |
| Inhibition is CIPK-kinase-independent | **Supported (single-source)** | CIPK23 competition model (PMID:23331977) |
| Independently replicated / corroborated in planta | **Refuted** | 0/76 citing papers; 0/105 Europe PMC records; OE-only, no *cbl10*-null |
| "Not contradicted by later work" | **Refuted / qualified** | CBL10 activates HAK5 (PMID:26474642); AtKC1 is mainstream AKT1 inhibitor |
| Justifies adding GO:0019870 | **No — over-annotation** | Single-source, OE-only, context-dependent; term not currently annotated |

---

*Report generated from a 3-iteration autonomous curation review. Primary evidence from Ren et al. 2013 (PMID:23331977); replication audit via NCBI ELink citedin (76 papers) and Europe PMC full-text search (105 records); GO state via QuickGO (Q7FRS8); conflicting evidence from Ragel et al. 2015 (PMID:26474642).*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)