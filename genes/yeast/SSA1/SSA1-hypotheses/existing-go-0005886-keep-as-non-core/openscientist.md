---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T15:30:53.581805'
end_time: '2026-08-22T15:44:03.170092'
duration_seconds: 789.59
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: SSA1
  gene_symbol: SSA1
  uniprot_accession: P10591
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: existing_go_annotation_decision
  hypothesis_slug: existing-go-0005886-keep-as-non-core
  hypothesis_text: 'The existing SSA1 GO annotation to plasma membrane (GO:0005886)
    should receive review action KEEP_AS_NON_CORE. Current rationale: Retain conservatively
    because a stripped-plasma-membrane proteomics study detected Ssa1, but this high-throughput
    fractionation evidence does not establish the plasma membrane as a primary site
    of Ssa1 function.'
  term_context: '- Term: plasma membrane (GO:0005886)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033

    - Current review action: KEEP_AS_NON_CORE

    - Review summary: SSA1 has been detected at the plasma membrane by HDA (PMID:16622836).
    IBA is consistent.

    - Review reason: Retain conservatively because a stripped-plasma-membrane proteomics
    study detected Ssa1, but this high-throughput fractionation evidence does not
    establish the plasma membrane as a primary site of Ssa1 function.'
  reference_context: '- GO_REF:0000033'
  source_file: genes/yeast/SSA1/SSA1-ai-review.yaml
  source_selector: existing_annotations[3]
  source_context_yaml: "term:\n  id: GO:0005886\n  label: plasma membrane\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033\nreview:\n  summary: SSA1 has been\
    \ detected at the plasma membrane by HDA (PMID:16622836). IBA is consistent.\n\
    \  action: KEEP_AS_NON_CORE\n  reason: Retain conservatively because a stripped-plasma-membrane\
    \ proteomics study detected Ssa1, but\n    this high-throughput fractionation\
    \ evidence does not establish the plasma membrane as a primary site\n    of Ssa1\
    \ function."
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** SSA1
- **Gene symbol:** SSA1
- **UniProt accession:** P10591

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** existing-go-0005886-keep-as-non-core
- **Source file:** genes/yeast/SSA1/SSA1-ai-review.yaml
- **Source selector:** existing_annotations[3]

## Seed Hypothesis

The existing SSA1 GO annotation to plasma membrane (GO:0005886) should receive review action KEEP_AS_NON_CORE. Current rationale: Retain conservatively because a stripped-plasma-membrane proteomics study detected Ssa1, but this high-throughput fractionation evidence does not establish the plasma membrane as a primary site of Ssa1 function.

## Term and Decision Context

- Term: plasma membrane (GO:0005886)
- Evidence type: IBA
- Original reference: GO_REF:0000033
- Current review action: KEEP_AS_NON_CORE
- Review summary: SSA1 has been detected at the plasma membrane by HDA (PMID:16622836). IBA is consistent.
- Review reason: Retain conservatively because a stripped-plasma-membrane proteomics study detected Ssa1, but this high-throughput fractionation evidence does not establish the plasma membrane as a primary site of Ssa1 function.

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0005886
  label: plasma membrane
evidence_type: IBA
original_reference_id: GO_REF:0000033
review:
  summary: SSA1 has been detected at the plasma membrane by HDA (PMID:16622836). IBA is consistent.
  action: KEEP_AS_NON_CORE
  reason: Retain conservatively because a stripped-plasma-membrane proteomics study detected Ssa1, but
    this high-throughput fractionation evidence does not establish the plasma membrane as a primary site
    of Ssa1 function.
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

# SSA1 Plasma Membrane (GO:0005886) Annotation — Deep Research Report

**Gene:** SSA1 (P10591) · *Saccharomyces cerevisiae* (NCBITaxon:559292)
**Focus:** existing_go_annotation_decision · `existing_annotations[3]`
**Hypothesis slug:** `existing-go-0005886-keep-as-non-core`
**Term under review:** plasma membrane (GO:0005886), evidence IBA, original reference GO_REF:0000033
**Seed action:** KEEP_AS_NON_CORE

---

## Summary

**Executive verdict: partially supported — the recommended action (KEEP_AS_NON_CORE) is defensible on substance, but the rationale stated in the seed is factually wrong and must be corrected before the review is finalized.** The seed hypothesis asserts that (a) the plasma-membrane annotation is an IBA (phylogenetically inferred) term that is "consistent" with an underlying HDA detection, and (b) it should be retained conservatively as non-core. A live evidence check contradicts point (a): the PANTHER/PAINT phylogenetic (IBA) pipeline for P10591 propagated only nucleus (GO:0005634), cytoplasm (GO:0005737), and cytosol (GO:0005829) — **it never assigned plasma membrane**. The GO:0005886 annotation rests entirely on a single high-throughput proteomics dataset (HDA, ECO:0007005, [PMID: 16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/)), a crude "stripped plasma membrane" fraction in which Ssa1 was one of ~90 co-purifying proteins and was not functionally highlighted. The annotation is therefore even weaker than the seed's own summary implies.

Ssa1 is, by every line of primary evidence, an **abundant cytosolic Hsp70 chaperone**. Its sequence (UniProt P10591, 642 aa) has no transmembrane segment, no signal peptide, no GPI anchor, and no lipidation site, and its UniProt keyword set contains Cytoplasm, Cell wall, and Secreted but **not** Membrane/Cell membrane. Where Ssa1 genuinely contacts membranes, it does so as a peripheral, cytosol-facing chaperone — recruited to the vacuolar membrane during Cvt/aminopeptidase transport ([PMID: 10745074](https://pubmed.ncbi.nlm.nih.gov/10745074/)), acting at the cytosolic face of the ER during ERAD ([PMID: 18812321](https://pubmed.ncbi.nlm.nih.gov/18812321/)), and delivering precursors to the mitochondrial import receptors ([PMID: 27412066](https://pubmed.ncbi.nlm.nih.gov/27412066/)). None of these establish integral or stable plasma-membrane residence.

**Bottom line for the curator:** the plasma-membrane term should not be treated as core, so KEEP_AS_NON_CORE is an acceptable conservative outcome — but the review's supporting text should be rewritten to (1) remove the incorrect claim that an IBA supports plasma membrane, (2) state accurately that the term rests on one crude proteomic fraction (HDA, not IBA), and (3) note that REMOVE is a fully defensible alternative given the absence of any functional, genetic, or targeted-localization support. If a genuine surface pool of Ssa1 exists, the better-supported descriptor is the fungal-type cell wall (GO:0009277, IDA), not the plasma membrane.

---

## Key Findings

### Finding 1 — The plasma-membrane term rests only on high-throughput fraction proteomics; KEEP_AS_NON_CORE is justified on the substance

The plasma-membrane cellular-component assignment for Ssa1 traces to a single source: *The plasma membrane proteome of Saccharomyces cerevisiae and its response to the antifungal calcofluor* ([PMID: 16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/), Delom et al., 2006). This study prepared a **"stripped plasma membrane fraction"** — a crude enrichment that is solubilized with detergent and then subjected to mass spectrometry. The verified snippet from the abstract reads: *"Proteins from a stripped plasma membrane fraction were solubilized with the neutral and non-denaturing detergent."* Ssa1 was one of roughly 90 identified proteins and was not singled out for any membrane-specific function.

This kind of subcellular-fraction proteomics is precisely the situation in which an abundant, sticky cytosolic chaperone will appear as a contaminant or peripheral associate. The primary literature is unanimous that Ssa1's core identity is cytosolic. A study of ERAD of the thiazide-sensitive NaCl cotransporter notes the process *"required the activity of Ssa1, a cytoplasmic Hsp70 chaperone"* ([PMID: 22027832](https://pubmed.ncbi.nlm.nih.gov/22027832/)). Work on tombusvirus replication describes Hsp70 as *"an abundant cytosolic chaperone"* ([PMID: 19153242](https://pubmed.ncbi.nlm.nih.gov/19153242/)). High cellular abundance combined with intrinsic client-binding stickiness make co-fractionation with any membrane preparation a strong prior expectation. Because the annotation reflects bulk co-purification rather than a demonstrated functional site, treating plasma membrane as **non-core is the correct handling of the evidence weight** — the seed's action is substantively defensible.

### Finding 2 — There is NO IBA plasma-membrane annotation; the seed's "IBA is consistent" rationale is incorrect

A live QuickGO enumeration of all cellular-component annotations for P10591 returns 16 CC annotations. Critically, the phylogenetic IBA pipeline (GO_REF:0000033, contributed by GO_Central via PANTHER/PAINT) assigned only three locations: **GO:0005634 nucleus, GO:0005737 cytoplasm, and GO:0005829 cytosol**. It did **not** assign GO:0005886 plasma membrane. The only plasma-membrane annotation present is a single **HDA** (ECO:0007005), qualifier `located_in`, referencing PMID:16622836, assigned by SGD.

This directly contradicts the seed context, which lists the term as `evidence_type: IBA` with the summary "IBA is consistent." There is no IBA to be consistent with. The seed appears to have conflated the GO_REF:0000033 phylogenetic reference (which is attached to the *nucleus/cytoplasm/cytosol* propagations) with the plasma-membrane term. The plasma-membrane annotation is neither phylogenetically supported nor independently replicated — it is one crude proteomics hit.

By contrast, the core locations for Ssa1 carry **convergent, multi-method support**:

| Location | GO ID | Evidence chain |
|---|---|---|
| Cytosol | GO:0005829 | IBA + HDA (PMID:26928762) |
| Cytoplasm | GO:0005737 | IBA + HDA (PMID:11914276) + IDA (PMID:8755907) |
| Nucleus | GO:0005634 | IBA + IDA (PMID:10347213) + HDA (PMID:11914276) |
| Plasma membrane | GO:0005886 | **HDA only (PMID:16622836)** |

Sequence analysis reinforces the point. UniProt P10591 (642 aa) shows **no transmembrane helix, no intramembrane region, no signal peptide, no GPI-anchor site, and no lipidation modification**. Its keyword set lists Cytoplasm, Cell wall, and Secreted — but **not** Membrane or Cell membrane. A protein that stably resides in the plasma membrane would ordinarily carry at least one such feature or keyword; Ssa1 carries none. This is fully consistent with peripheral/contaminant detection rather than genuine membrane residence.

---

## Mechanistic Model / Interpretation

Ssa1 is a constitutively expressed member of the yeast cytosolic **Ssa (Hsp70) subfamily**. Its molecular function is ATP-dependent chaperone activity: binding exposed hydrophobic segments of client polypeptides to assist folding, prevent aggregation, drive translocation across organellar membranes, and target misfolded proteins for degradation. All of these activities occur in the **cytosol** or **at the cytosolic face of membranes**, not within the membrane bilayer.

```
                         SSA1 (cytosolic Hsp70) — where it really acts
   +---------------------------------------------------------------------+
   |  CYTOSOL  (core; IBA+HDA+IDA)                                        |
   |     - folding / anti-aggregation of nascent & stress-denatured       |
   |       clients                                                        |
   |     - NUCLEUS pool (core; IBA+IDA+HDA) - e.g. Pdr3 co-purification    |
   |       and transcriptional modulation (PMID:17636264)                 |
   |                                                                      |
   |   -- peripheral, cytosol-FACING membrane contacts (transient) --     |
   |     - ER surface  -> ERAD of CytoQC/membrane clients (PMID:18812321) |
   |     - Vacuole membrane -> Ape1/Cvt vesicle fusion (PMID:10745074)    |
   |     - Mito TOM receptors -> precursor delivery (PMID:27412066)       |
   +---------------------------------------------------------------------+
             ^
             |  co-fractionation / peripheral stickiness
             |
   +---------------------------------------------------------------------+
   |  PLASMA MEMBRANE  (GO:0005886) - HDA only, PMID:16622836             |
   |  crude "stripped PM" proteome; Ssa1 = 1 of ~90 proteins;            |
   |  no TM / signal / GPI / lipidation; NOT phylogenetically propagated  |
   |  -> reflects abundance-driven co-purification, not residence         |
   +---------------------------------------------------------------------+
```

The key mechanistic distinction: **a cellular-component annotation is meant to record where the gene product carries out its function.** For Ssa1, that answer is overwhelmingly the cytosol (with nuclear and peripheral membrane pools). The plasma-membrane detection is a *downstream observation of a fractionation experiment*, not evidence of a functional plasma-membrane pool. Even the organism-relevant surface literature points elsewhere: Ssa1 carries the UniProt keywords Cell wall and Secreted, and SGD records a fungal-type cell wall IDA (GO:0009277). Cytosolic Hsp70s are known to reach the yeast surface/cell wall under some conditions, so if any genuine surface pool exists, **fungal-type cell wall (GO:0009277)** is the more informative and better-evidenced descriptor than plasma membrane.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/) | Localization (HT proteomics) | Qualifies (sole basis for the term) | Is Ssa1 at the plasma membrane? | Ssa1 detected in a crude "stripped plasma membrane" fraction; 1 of ~90 proteins, not functionally highlighted | *S. cerevisiae*, PM fraction MS | Low specificity for a single protein; abundant cytosolic contaminants expected in fractions |
| QuickGO/UniProt P10591 (database) | Computational/database | Refutes seed rationale | Does an IBA support PM? | IBA (GO_REF:0000033) propagated only nucleus, cytoplasm, cytosol — never plasma membrane | GO_Central PANTHER/PAINT | Direct enumeration; database carry-over is the mechanism to watch |
| UniProt P10591 features (database) | Structural/sequence | Refutes membrane residence | Does sequence support PM residence? | No TM / signal / GPI / lipidation; keywords lack Membrane/Cell membrane (has Cytoplasm, Cell wall, Secreted) | 642-aa Hsp70 | Strong negative prior; absence of feature is not absolute proof |
| [PMID: 22027832](https://pubmed.ncbi.nlm.nih.gov/22027832/) | Mutant phenotype / functional | Refutes PM as primary site | Where does Ssa1 function? | ERAD of NCC "required the activity of Ssa1, a cytoplasmic Hsp70 chaperone" | *S. cerevisiae* ERAD | Defines core identity as cytoplasmic |
| [PMID: 19153242](https://pubmed.ncbi.nlm.nih.gov/19153242/) | Functional / localization | Refutes PM as primary site | Core compartment of Ssa1/Hsp70 | "an abundant cytosolic chaperone"; recruited to intracellular membranes for viral replication | Tombusvirus in yeast | Abundance explains co-fractionation |
| [PMID: 18812321](https://pubmed.ncbi.nlm.nih.gov/18812321/) | Mutant phenotype / functional | Qualifies (peripheral membrane role) | Membrane engagement mode | Ssa1p acts at the **cytosolic face of the ER** in ERAD of a cytosolic substrate | *S. cerevisiae* CytoQC | Peripheral, not integral; not PM |
| [PMID: 10745074](https://pubmed.ncbi.nlm.nih.gov/10745074/) | Localization / functional | Qualifies / competing (other membrane) | Where does Ssa1 bind membranes? | Ssa1/2p "prominently localized to the vacuolar membrane" for Ape1 vesicle fusion | *S. cerevisiae* Cvt pathway | Vacuolar, not plasma, membrane |
| [PMID: 27412066](https://pubmed.ncbi.nlm.nih.gov/27412066/) | Interaction / crosslinking | Qualifies (peripheral role) | Ssa1 at organellar surfaces | Ssa1 delivers precursors to mitochondrial import receptors Tom20/Tom70 | *S. cerevisiae* mito import | Cytosolic factor at mito surface; not PM |
| [PMID: 17636264](https://pubmed.ncbi.nlm.nih.gov/17636264/) | Interaction / functional | Qualifies (nuclear/cytosolic role) | Additional Ssa1 compartments | Cytosolic Hsp70 Ssa1p represses PDR5 via nuclear Pdr3 | *S. cerevisiae* Pdr pathway | Supports cytosolic/nuclear, not PM |

---

## GO Curation Implications

**Term:** plasma membrane (GO:0005886), a cellular-component (CC) term. This is a location claim, not an MF or BP claim.

**Lead action (requires curator verification): KEEP_AS_NON_CORE is acceptable, but the review text must be corrected; REMOVE is a defensible alternative.**

1. **Do not treat GO:0005886 as core.** No functional, genetic, or targeted-imaging evidence places Ssa1's activity at the plasma membrane. The only support is a single crude-fraction proteomics dataset. Non-core handling is correct in spirit.

2. **Correct the rationale.** The seed's summary ("detected... by HDA; IBA is consistent") is inaccurate. There is **no IBA** to plasma membrane; the PAINT pipeline propagated only nucleus/cytoplasm/cytosol. The evidence chain is HDA-only. The rewritten reason should say: *"Supported only by one high-throughput stripped-plasma-membrane proteomic fraction (PMID:16622836); no phylogenetic (IBA), genetic, or targeted-localization support; sequence has no membrane-targeting features. Retained conservatively as non-core; REMOVE is defensible."*

3. **Consider REMOVE as the stronger scientific action.** Given (i) HDA-only support, (ii) the high false-positive rate for abundant cytosolic chaperones in membrane fractions, and (iii) zero membrane-targeting sequence features, a curator could reasonably remove the annotation as a fractionation artifact / database carry-over rather than retain it. This should be flagged as an explicit option.

4. **Prefer a better-supported surface descriptor if any surface pool is to be captured.** Fungal-type cell wall (GO:0009277) carries IDA support and matches the UniProt Cell wall / Secreted keywords, making it a more informative CC term than plasma membrane for any genuine surface localization.

The well-supported core CC terms to retain as-is: cytosol (GO:0005829), cytoplasm (GO:0005737), and nucleus (GO:0005634).

---

## Mechanistic Scope

A CC annotation records *the site at which the gene product performs its activity*. Ssa1's activity is ATP-dependent Hsp70 chaperoning, which occurs in the cytosol and nucleus and, transiently, at the cytosolic faces of the ER, vacuolar, and mitochondrial membranes. The plasma-membrane term does not describe any Ssa1 activity; it is an inference drawn from a bulk fractionation experiment. Separating direct activity from observation:

- **Direct gene-product activity/location:** cytosolic (and nuclear) Hsp70 chaperoning — folding, translocation, degradation targeting.
- **Peripheral (cytosol-facing) membrane engagement:** ER surface (ERAD), vacuolar membrane (Cvt), mitochondrial import receptors — real but not integral, and not plasma membrane.
- **Downstream/observational only:** presence in a stripped-PM proteomic fraction — an artifact-prone readout, not a functional assignment.

---

## Conflicts and Alternatives

- **Seed vs. live database (the central conflict):** The seed labels the term IBA and calls the IBA "consistent" with the HDA; the live QuickGO record shows no IBA plasma-membrane annotation at all. This is a database carry-over / evidence-code mislabeling that the curator must reconcile.
- **Abundance/co-fractionation artifact:** Ssa1 is one of the most abundant cytosolic proteins in yeast. Fraction-based proteomics reliably co-enriches such proteins. This is the leading alternative explanation for the PM detection and is strongly favored over genuine residence.
- **Paralog considerations:** Ssa1 shares near-identity with Ssa2 (>95%) and functional overlap with Ssa3/Ssa4. Proteomic peptide assignments among Ssa paralogs can be ambiguous, further weakening a single-protein PM claim. The vacuolar-membrane study explicitly treats Ssa1/2p together ([PMID: 10745074](https://pubmed.ncbi.nlm.nih.gov/10745074/)).
- **Alternative surface term:** If any true cell-surface pool exists, fungal-type cell wall (GO:0009277, IDA) is better supported than plasma membrane and is consistent with the Secreted/Cell wall keywords.

---

## Limitations and Knowledge Gaps

- **No targeted imaging evidence was retrievable** for Ssa1 at the plasma membrane (e.g., GFP tagging with a PM marker, immuno-EM, or fractionation with quantitative controls). What was checked: SGD/UniProt/QuickGO annotation records and primary functional literature. Why it matters: a curator deciding KEEP vs REMOVE would benefit from any high-resolution localization; none supports PM. Resolution: a targeted GFP-Ssa1 co-localization with a PM marker (e.g., Pma1) under native abundance.
- **The Delom et al. dataset was not re-analyzed at the peptide level.** What was checked: the abstract and its role as the HDA source. Why it matters: knowing whether the Ssa1 identification is peptide-robust and paralog-unambiguous affects confidence. Resolution: inspect the paper's supplementary protein list and spectral counts.
- **Quantitative contamination controls unknown.** High-throughput PM fractions rarely report cytosolic-contaminant enrichment ratios for individual proteins. Resolution: compare Ssa1's PM-fraction abundance to its total-cell abundance; a chaperone present at cytosolic levels in a PM fraction indicates contamination.
- **GO_REF:0000033 provenance mismatch.** The seed attaches this phylogenetic reference to the PM term, but the live pipeline attaches it to nucleus/cytoplasm/cytosol. Resolution: curator to verify the current GAF/annotation source and correct the evidence code.

---

## Proposed Follow-up Experiments / Actions (Discriminating Tests)

1. **Quantitative co-fractionation control:** Measure Ssa1 abundance in the stripped-PM fraction relative to a bona fide integral PM protein (e.g., Pma1) and to total lysate. If Ssa1 tracks cytosolic markers, the PM annotation is an artifact → supports REMOVE.
2. **High-resolution live imaging:** GFP-Ssa1 expressed at native levels co-imaged with a PM marker (Pma1-mCherry). Absence of PM rim enrichment argues against residence.
3. **Carbonate/salt extraction:** Peripheral/contaminant proteins are stripped from membranes by Na₂CO₃ or high salt; integral proteins are not. Ssa1 should extract fully.
4. **Paralog-resolved MS:** Re-examine the Delom peptides for Ssa1-unique vs Ssa-shared peptides to test whether the identification is even Ssa1-specific.
5. **Cell-wall vs PM discrimination:** Spheroplasting and cell-wall digestion controls (or surface biotinylation of intact spheroplasts) to test whether the surface signal is cell-wall-associated (GO:0009277) rather than PM.

---

## Curation Leads (require curator verification)

- **Action:** Retain KEEP_AS_NON_CORE **or** change to REMOVE — both defensible. Prefer REMOVE if the curator weights artifact risk heavily; prefer KEEP_AS_NON_CORE if conservative retention is house policy. Either way, **rewrite the rationale**.
- **Rationale replacement (candidate text):** "GO:0005886 is supported only by one high-throughput 'stripped plasma membrane' proteomic fraction (PMID:16622836) in which Ssa1 was one of ~90 co-purifying proteins. No phylogenetic (IBA), genetic, or targeted-localization evidence supports plasma-membrane residence; the sequence lacks any transmembrane, signal, GPI, or lipidation feature. Ssa1 is an abundant cytosolic Hsp70; the detection most likely reflects co-fractionation. Retained as non-core (or removable as artifact)."
- **Correct the evidence code:** The term should be recorded as **HDA (ECO:0007005), not IBA**. Verify against the current QuickGO/GAF record for P10591.
- **Candidate references with exact snippets to verify:**
  - [PMID: 16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/): *"Proteins from a stripped plasma membrane fraction were solubilized with the neutral and non-denaturing detergent"* — confirms the crude-fraction basis.
  - [PMID: 22027832](https://pubmed.ncbi.nlm.nih.gov/22027832/): *"required the activity of Ssa1, a cytoplasmic Hsp70 chaperone"* — confirms cytosolic core identity.
  - [PMID: 19153242](https://pubmed.ncbi.nlm.nih.gov/19153242/): *"an abundant cytosolic chaperone"* — explains co-fractionation.
- **Candidate alternative CC term:** fungal-type cell wall (GO:0009277, IDA) if a surface pool is to be represented — better supported than plasma membrane.
- **Suggested curator questions:** Is there any single-gene, low-throughput imaging/genetic evidence for Ssa1 at the PM? Is the Delom identification paralog-specific and abundance-controlled? Does house policy retain single-HDA fraction hits as non-core, or remove them?
- **Suggested experiments:** quantitative PM-fraction contamination control; GFP-Ssa1 native imaging vs Pma1; carbonate extraction; paralog-resolved MS (as in Discriminating Tests).

---

## Evidence Base (key literature)

- [PMID: 16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/) — *The plasma membrane proteome of Saccharomyces cerevisiae and its response to the antifungal calcofluor.* The sole source of the GO:0005886 annotation; a crude stripped-PM proteomic fraction. Supports the annotation only weakly (bulk detection).
- [PMID: 22027832](https://pubmed.ncbi.nlm.nih.gov/22027832/) — Defines Ssa1 as "a cytoplasmic Hsp70 chaperone" in ERAD. Establishes cytosolic core identity.
- [PMID: 19153242](https://pubmed.ncbi.nlm.nih.gov/19153242/) — "an abundant cytosolic chaperone" recruited to intracellular (not plasma) membranes; abundance explains fraction contamination.
- [PMID: 18812321](https://pubmed.ncbi.nlm.nih.gov/18812321/) — Ssa1p functions at the cytosolic face of the ER in CytoQC/ERAD; peripheral, not integral, membrane engagement.
- [PMID: 10745074](https://pubmed.ncbi.nlm.nih.gov/10745074/) — Ssa1/2p localize to the vacuolar membrane for Ape1 vesicle fusion; genuine membrane contact, but vacuolar not plasma.
- [PMID: 27412066](https://pubmed.ncbi.nlm.nih.gov/27412066/) — Ssa1 delivers precursors to mitochondrial import receptors; cytosolic factor at organellar surface.
- [PMID: 17636264](https://pubmed.ncbi.nlm.nih.gov/17636264/) — Cytosolic Ssa1p modulates PDR5 transcription via nuclear Pdr3; supports cytosolic/nuclear pools.

---

## Conclusion

The seed hypothesis is **partially supported**: its recommended action (KEEP_AS_NON_CORE) is a reasonable, conservative outcome, but its supporting rationale is wrong in a way that materially affects curation. There is no IBA supporting plasma membrane for Ssa1; the term rests entirely on one crude high-throughput proteomic fraction (HDA, PMID:16622836), and Ssa1 is an abundant cytosolic Hsp70 with no membrane-targeting sequence features. The curator should retain the term as non-core *or* remove it as a likely fractionation artifact — and, either way, correct the evidence code (HDA, not IBA) and the rationale text. The genuinely well-supported locations are cytosol, cytoplasm, and nucleus; any true surface pool is better captured by fungal-type cell wall (GO:0009277).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)