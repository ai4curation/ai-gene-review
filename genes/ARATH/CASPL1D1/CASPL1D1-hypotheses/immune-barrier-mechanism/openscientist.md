---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T09:40:53.680650'
end_time: '2026-09-12T09:58:38.280259'
duration_seconds: 1064.6
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ARATH
  gene: CASPL1D1
  gene_symbol: CASPL1D1
  uniprot_accession: Q9FE29
  taxon_id: NCBITaxon:3702
  taxon_label: Arabidopsis thaliana
  focus_type: function_assignment
  hypothesis_slug: immune-barrier-mechanism
  hypothesis_text: CASPL1D1 contributes to pathogen-induced lignified barrier formation
    through a membrane-organizing molecular function.
  term_context: '- Determine whether available evidence supports a specific molecular
    organizing function or only participation in the biological process. Focus on
    CASPL1D1-specific immune-lignification evidence and the strongest testable alternative
    mechanism; distinguish single artificial-miRNA knockdown from combined CASPL4D1
    perturbation and CASPL4D1-specific localization/complementation. Separate this
    from canonical CASP1-5 scaffold mechanisms, CASPL1B1 aquaporin regulation and
    the CASPL1D1/1D2 root phenotype. One decisive question: can a specific molecular
    function now be assigned to CASPL1D1, and if not what experiment discriminates
    the leading mechanisms? Use primary evidence and independently reproducible analyses.
    Do not consult ai-gene-review repository reviews, generated reports or local bioinformatics
    results; these are held out. Verify the exact Arabidopsis protein and distinguish
    paralogs, mutants, tissue and assay context. Give evidence for and against the
    assignment, the narrowest defensible function, and what observation would change
    the verdict. Missing evidence is not refutation. Do not infer catalytic or regulatory
    function from interaction, docking or shared fold alone.'
  reference_context: '- PMID:31559647

    - PMID:24920445

    - PMID:36959183'
  source_file: genes/ARATH/CASPL1D1/CASPL1D1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: CASPL1D1 contributes to pathogen-induced lignified\
    \ barrier formation through a membrane-organizing\n  molecular function.\nfocus_type:\
    \ function_assignment\ncontext:\n- 'Determine whether available evidence supports\
    \ a specific molecular organizing function or only participation\n  in the biological\
    \ process. Focus on CASPL1D1-specific immune-lignification evidence and the strongest\n\
    \  testable alternative mechanism; distinguish single artificial-miRNA knockdown\
    \ from combined CASPL4D1\n  perturbation and CASPL4D1-specific localization/complementation.\
    \ Separate this from canonical CASP1-5\n  scaffold mechanisms, CASPL1B1 aquaporin\
    \ regulation and the CASPL1D1/1D2 root phenotype. One decisive\n  question: can\
    \ a specific molecular function now be assigned to CASPL1D1, and if not what experiment\n\
    \  discriminates the leading mechanisms? Use primary evidence and independently\
    \ reproducible analyses.\n  Do not consult ai-gene-review repository reviews,\
    \ generated reports or local bioinformatics results;\n  these are held out. Verify\
    \ the exact Arabidopsis protein and distinguish paralogs, mutants, tissue and\n\
    \  assay context. Give evidence for and against the assignment, the narrowest\
    \ defensible function, and\n  what observation would change the verdict. Missing\
    \ evidence is not refutation. Do not infer catalytic\n  or regulatory function\
    \ from interaction, docking or shared fold alone.'\nreference_id:\n- PMID:31559647\n\
    - PMID:24920445\n- PMID:36959183"
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
citation_count: 4
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
- **Gene directory:** CASPL1D1
- **Gene symbol:** CASPL1D1
- **UniProt accession:** Q9FE29

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** immune-barrier-mechanism
- **Source file:** genes/ARATH/CASPL1D1/CASPL1D1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

CASPL1D1 contributes to pathogen-induced lignified barrier formation through a membrane-organizing molecular function.

## Term and Decision Context

- Determine whether available evidence supports a specific molecular organizing function or only participation in the biological process. Focus on CASPL1D1-specific immune-lignification evidence and the strongest testable alternative mechanism; distinguish single artificial-miRNA knockdown from combined CASPL4D1 perturbation and CASPL4D1-specific localization/complementation. Separate this from canonical CASP1-5 scaffold mechanisms, CASPL1B1 aquaporin regulation and the CASPL1D1/1D2 root phenotype. One decisive question: can a specific molecular function now be assigned to CASPL1D1, and if not what experiment discriminates the leading mechanisms? Use primary evidence and independently reproducible analyses. Do not consult ai-gene-review repository reviews, generated reports or local bioinformatics results; these are held out. Verify the exact Arabidopsis protein and distinguish paralogs, mutants, tissue and assay context. Give evidence for and against the assignment, the narrowest defensible function, and what observation would change the verdict. Missing evidence is not refutation. Do not infer catalytic or regulatory function from interaction, docking or shared fold alone.

## Reference Context

- PMID:31559647
- PMID:24920445
- PMID:36959183

## Source Context YAML

```yaml
hypothesis: CASPL1D1 contributes to pathogen-induced lignified barrier formation through a membrane-organizing
  molecular function.
focus_type: function_assignment
context:
- 'Determine whether available evidence supports a specific molecular organizing function or only participation
  in the biological process. Focus on CASPL1D1-specific immune-lignification evidence and the strongest
  testable alternative mechanism; distinguish single artificial-miRNA knockdown from combined CASPL4D1
  perturbation and CASPL4D1-specific localization/complementation. Separate this from canonical CASP1-5
  scaffold mechanisms, CASPL1B1 aquaporin regulation and the CASPL1D1/1D2 root phenotype. One decisive
  question: can a specific molecular function now be assigned to CASPL1D1, and if not what experiment
  discriminates the leading mechanisms? Use primary evidence and independently reproducible analyses.
  Do not consult ai-gene-review repository reviews, generated reports or local bioinformatics results;
  these are held out. Verify the exact Arabidopsis protein and distinguish paralogs, mutants, tissue and
  assay context. Give evidence for and against the assignment, the narrowest defensible function, and
  what observation would change the verdict. Missing evidence is not refutation. Do not infer catalytic
  or regulatory function from interaction, docking or shared fold alone.'
reference_id:
- PMID:31559647
- PMID:24920445
- PMID:36959183
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

# CASPL1D1 (Q9FE29) — Immune Barrier Mechanism: Function-Assignment Evaluation

**Target gene:** CASPL1D1 / AT4G15610 (Arabidopsis thaliana, ARATH), UniProt **Q9FE29**
**Focus type:** function_assignment
**Seed hypothesis:** *CASPL1D1 contributes to pathogen-induced lignified barrier formation through a membrane-organizing molecular function.*

---

## Executive Judgment

**Verdict: Partially supported — the biological-process clause is supported; the molecular-function clause is unresolved / over-annotated if asserted.**

The seed hypothesis bundles two distinct claims that must be scored separately:

1. **Biological process ("contributes to pathogen-induced lignified barrier formation"):** **Supported.** Full-text evidence from the reference paper [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/) shows CASPL1D1 (AT4G15610) is one of only two of the 34 Arabidopsis CASPLs specifically induced by biotic stress, and that an artificial-microRNA knockdown line (amiCASPL1D1) reduces AvrRpm1-triggered leaf lignification and allows the hypersensitive-response (HR) cell-death lesion to spread beyond the infiltration zone. Control lines *casp1-1* and *caspl5b3-1* were unaffected. This is CASPL1D1-specific loss-of-function evidence for participation in the immune lignin barrier.

2. **Molecular function ("through a membrane-organizing molecular function"):** **Unresolved / not assignable to CASPL1D1.** No direct molecular assay of a membrane-organizing (scaffold) activity has been performed on CASPL1D1. The concrete "membrane-organizing" mechanism — exclusion of vesicle-tethering factors, displacement of secretory foci, and formation of a rigid membrane microdomain — is demonstrated only for the canonical **CASP1–CASP5** paralogs ([PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/)), and "scaffold" behavior is described as a **family-level hallmark** of the CASP/CASPL clade, not a CASPL1D1-specific measurement ([PMID:24920445](https://pubmed.ncbi.nlm.nih.gov/24920445/)). CASPL1D1 shares only the four-transmembrane MARVEL/CASP fold (Pfam PF04535) with these proteins and is only ~32–34 % identical to them, so the scaffold mechanism cannot be transferred by homology.

**Most important caveats:**
- The CASPL1D1 immune evidence rests on a **single artificial-miRNA knockdown** (no clean T-DNA null exists for AT4G15610), which carries knockdown-incompleteness and off-target risks. The gold-standard localization and complementation evidence in the same study was obtained for the paralog **CASPL4D1**, not CASPL1D1.
- The best-characterized loss-of-function phenotype for CASPL1D1 is actually in a **different tissue and process** — a subtle root endodermal suberization change and aquaporin (PIP2;1) association ([PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/)) — which competes with the leaf-immunity framing for "primary function."
- "Membrane-organizing molecular function" is inferred from **shared fold and analogy**, exactly the type of inference the task instructions caution against ("Do not infer catalytic or regulatory function from interaction, docking or shared fold alone").

**Bottom line for the curator:** Keep the GO **molecular function as ND** (no specific MF assignable). Support a defense/lignin **biological-process** annotation for CASPL1D1 as an IMP-level lead, flagged with the amiRNA-knockdown caveat. Retain plasma-membrane (and Golgi/endosome) cellular-component terms. Do **not** assign a specific membrane-scaffold MF term to CASPL1D1 on current evidence.

---

## Summary

CASPL1D1 (Q9FE29 / AT4G15610) is a divergent member of the CASP-like (MARVEL four-transmembrane) family. The seed hypothesis — that it contributes to pathogen-induced lignified-barrier formation **through a membrane-organizing molecular function** — separates into a well-supported biological-process claim and an unsupported molecular-function claim. Full-text evidence from [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/) shows CASPL1D1 is specifically pathogen-induced and that its knockdown reduces AvrRpm1-triggered leaf lignification and lets the hypersensitive lesion spread (with canonical *casp1-1* and *caspl5b3-1* unaffected), so **participation in the immune lignin barrier (BP) is supported** — with the caveat that the evidence is an artificial-miRNA knockdown and the cleaner localization/complementation was shown for the paralog CASPL4D1.

By contrast, **no specific molecular function can be assigned to CASPL1D1.** The "membrane-organizing" scaffold activity is a CASP-family propensity demonstrated directly only for the canonical CASP1–5 paralogs; CASPL1D1 shares only the PF04535 fold with them and is a mere ~32–34 % identical, placing homology-based function transfer in the twilight zone. UniProt carries no FUNCTION comment and QuickGO records MF as ND. Assigning a specific membrane-scaffold MF to CASPL1D1 would be fold/family over-reach and is explicitly cautioned against by the task framing.

The recommended curation stance is therefore: **keep MF as ND; add a defense/lignin BP annotation as an IMP lead flagged with the amiRNA-knockdown caveat; retain plasma-membrane (and trafficking) CC terms; keep paralog annotations distinct.** The verdict would change if a CASPL1D1-specific direct scaffold/microdomain assay, or CASPL1D1 (not CASPL4D1) localization at lignifying foci in a clean null-complementation background, were demonstrated — at which point a specific membrane-organizing MF term could be justified.

---

## Key Findings

### Finding 1 — No specific molecular function can be assigned to CASPL1D1; current GO MF (ND) is correct

UniProt **Q9FE29** (CASPL1D1 / At4g15610, 193 aa) is annotated with four transmembrane helices, plasma-membrane localization, homo- and heterodimerization capacity, and general CASP-family similarity — but it carries **no FUNCTION comment**. Domain resources (InterPro / Pfam) detect only the CASP/MARVEL four-span membrane domain (**PF04535**) with **no catalytic domain**. QuickGO reports the molecular-function annotation as **GO:0003674 (molecular_function) with ND evidence**, i.e., an explicit statement that no molecular function has been experimentally assigned.

The "membrane-organizing" mechanism at the heart of the seed hypothesis — vesicle-tether exclusion, secretory-focus displacement, and matrix adhesion — is demonstrated only for the **canonical CASP1–CASP5** proteins ([PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/)), and scaffold propensity is described as a **family-level property** ([PMID:24920445](https://pubmed.ncbi.nlm.nih.gov/24920445/)). Neither of these is a CASPL1D1-specific molecular assay. Assigning a specific membrane-scaffold MF to CASPL1D1 would therefore be a fold/family over-reach.

> Supporting quote — [PMID:24920445](https://pubmed.ncbi.nlm.nih.gov/24920445/): *"CASPs show high stability in their membrane domain, which presents all the hallmarks of a membrane scaffold"* — scaffold behavior is a CASP/CASPL family-level description, not a CASPL1D1-specific measurement.

> Supporting quote — [PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/): *"We propose that CASP microdomains displace initial secretory foci by excluding vesicle tethering factors"* — the concrete membrane-organizing molecular mechanism is established for canonical CASP1–5, not CASPL1D1.

### Finding 2 — CASPL1D1's best-characterized loss-of-function phenotype is root endodermal suberization + aquaporin association, not leaf immune lignification

Champeyroux et al. 2019 ([PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/)) showed that CASPL1B1/1B2/1D1/1D2 interact with the aquaporin **PIP2;1**, and that *caspl1d1 caspl1d2* double mutants show a **weak enlargement of the endodermal continuous suberization zone** under some control/NaCl conditions (not under ABA), **with no change in root hydraulic conductivity (Lp)**. This is a subtle root-tissue phenotype in a different biological context from leaf immunity, and it is the most directly documented CASPL1D1 loss-of-function result. It competes with the immune-barrier framing as a candidate "primary function" and cautions against treating leaf lignification as CASPL1D1's core role.

> Supporting quote — [PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/): *"caspl1d1*caspl1d2 double mutants showed, in some control or NaCl stress experiments and not upon abscisic acid (ABA) treatment, a weak enlargement of the continuous suberization zone."*

> Supporting quote — [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/): *"lignin accumulates in Arabidopsis leaves in response to incompatible interactions with bacterial pathogens in a manner dependent on Casparian strip membrane domain protein (CASP)-like proteins (CASPLs)"* — the immune-lignification dependency is stated at the level of CASPLs collectively.

### Finding 3 — CASPL1D1 is specifically implicated in pathogen-induced leaf lignification (amiRNA knockdown), strengthening the BP clause; but MF remains unassignable

The full text of Lee et al. 2019 (EMBO J; [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/)) identifies **CASPL1D1 (AT4G15610)** and **CASPL4D1 (AT2G39530)** as the two of 34 Arabidopsis CASPLs specifically induced by biotic stress. Because **no T-DNA knockout exists for CASPL1D1**, the authors used an **artificial-microRNA knockdown** line (amiCASPL1D1; amiR targeting nucleotides 223–242). CASPL4D1 was tested with two T-DNA knockouts (caspl4d1-1 SALK_201606; caspl4d1-2 SALK_078525).

**AvrRpm1-induced lignification was largely reduced in both amiCASPL1D1 and caspl4d1, but not in casp1-1 or caspl5b3-1 controls**, and HR cell death spread beyond the infiltration zone in both amiCASPL1D1 and caspl4d1. This constitutes CASPL1D1-specific loss-of-function evidence for participation in the immune lignin barrier (a BP-level claim). However, the evidence is via **amiRNA knockdown** (incompleteness / off-target caveat) rather than a clean null, and the **localization/complementation gold standard was demonstrated for CASPL4D1**, not CASPL1D1. No direct molecular assay of a membrane-organizing activity for CASPL1D1 was performed; the barrier model is an analogy to the canonical CASP Casparian-strip scaffold.

> Supporting quote — [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/): *"lignin accumulates in Arabidopsis leaves in response to incompatible interactions with bacterial pathogens in a manner dependent on Casparian strip membrane domain protein (CASP)-like proteins (CASPLs)"* — supports that CASPLs (including CASPL1D1 per full text) are required for the pathogen-induced leaf lignin barrier.

### Finding 4 — CASPL1D1 is highly divergent (~32–34 % identity) from CASP1 and CASPL4D1, so the CASP1–5 scaffold MF cannot be transferred by homology

Independently reproducible Needleman–Wunsch global alignments of the UniProt sequences give:

| Pair | % identity | Aligned residues |
|------|-----------|------------------|
| CASPL1D1 (Q9FE29, 193 aa) vs CASP1 (Q9SIH4, At2g36100, 206 aa) | **33.9 %** | 78/230 |
| CASPL1D1 vs CASPL4D1 (Q8GWD5, At2g39530, 178 aa) | **31.8 %** | 68/214 |
| CASP1 vs CASPL4D1 | 29.6 % | — |

All three proteins share only the CASP/MARVEL four-transmembrane fold (Pfam **PF04535**) with **no catalytic domain**. At ~one-third sequence identity — well within the "twilight zone" where fold is conserved but specific function frequently diverges — homology-based transfer of the canonical CASP1–5 scaffold mechanism to CASPL1D1 is not defensible. Notably, CASPL1D1 is no more similar to its immune co-actor CASPL4D1 (31.8 %) than to the distantly related CASP1 (33.9 %), underscoring that "CASPL1D1" and "CASPL4D1" are not functionally interchangeable and that phenotypes shown for one paralog do not license MF assignment to the other.

---

## Mechanistic Model / Interpretation

The evidence separates cleanly into a **supported biological-process layer** and an **unsupported molecular-function layer**:

```
                        SEED HYPOTHESIS
   "CASPL1D1 contributes to pathogen-induced lignified barrier
    formation THROUGH a membrane-organizing molecular function"
                              │
        ┌─────────────────────┴─────────────────────┐
        │                                             │
  BP CLAUSE (supported)                     MF CLAUSE (unresolved)
  "contributes to lignin barrier"           "membrane-organizing function"
        │                                             │
  amiCASPL1D1 knockdown →                     NO direct assay on CASPL1D1
   ↓ AvrRpm1 lignification,                   Scaffold mechanism shown for
   HR lesion spreads                          CASP1–5 only (PMID:36959183)
   (casp1-1, caspl5b3-1 = OK)                 Family-level "scaffold"
   [PMID:31559647]                            (PMID:24920445)
        │                                             │
   GO BP: defense/lignin (IMP,               GO MF: keep ND
   amiRNA caveat)                            (fold-only ⇒ over-reach)
                              │
                    COMPETING CONTEXT
        CASPL1D1's cleanest LOF phenotype is in ROOT:
        caspl1d1 caspl1d2 → weak ↑ suberization, no ΔLp,
        PIP2;1 aquaporin association  [PMID:30767240]
```

**Narrative.** CASPL1D1 is a small (193 aa), four-pass plasma-membrane protein of the CASP-like (MARVEL-domain) family. Functionally, the family's namesake members (CASP1–5) build the Casparian strip by self-assembling into an immobile plasma-membrane scaffold that recruits lignin-polymerizing machinery and excludes competing secretory/vesicle-tethering factors — a genuine, assayed "membrane-organizing" molecular activity. The seed hypothesis proposes, by analogy, that CASPL1D1 performs the same kind of membrane-organizing job to nucleate a lignified barrier at pathogen infection sites in leaves.

The **process-level analogy holds**: knocking down CASPL1D1 measurably impairs pathogen-induced leaf lignification and lets the HR lesion spread, and this is not a generic effect (canonical *casp1-1* and *caspl5b3-1* are unaffected). So CASPL1D1 genuinely participates in the immune lignin-barrier process.

The **molecular-function analogy does not hold at the evidence level**: no one has measured a scaffold/membrane-organizing activity *for CASPL1D1 itself*. The mechanism is imported wholesale from CASP1–5, from which CASPL1D1 differs at ~two-thirds of its residues. Under GO evidence standards and the task's explicit instruction not to infer function from shared fold, the MF must remain **ND**. Adding to the caution, CASPL1D1's most directly documented mutant phenotype is not in leaf immunity at all but in **root endodermal suberization** with aquaporin association — a reminder that this protein may be pleiotropic and that "immune barrier" may be a context-specific role rather than its primary molecular job.

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Context | Confidence & limitations |
|----------|---------------|--------------------------------------------|--------------|-------------|---------|--------------------------|
| [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/) | Mutant phenotype (amiRNA knockdown) | **Supports (BP); qualifies (MF)** | CASPL1D1 required for pathogen-induced leaf lignin barrier | amiCASPL1D1 reduces AvrRpm1-induced lignification; HR lesion spreads; casp1-1/caspl5b3-1 unaffected; CASPL1D1 & CASPL4D1 are the biotic-stress-induced CASPLs | A. thaliana leaves, AvrRpm1 incompatible interaction | Medium-high for BP. amiRNA knockdown (not null); off-target/incompleteness risk; gold-standard localization/complementation shown for CASPL4D1, not CASPL1D1 |
| [PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/) | Direct assay (mechanism) | **Competing / qualifies MF** | Membrane-organizing scaffold mechanism | CASP microdomains displace secretory foci by excluding vesicle-tethering factors | A. thaliana root endodermis, canonical CASP1–5 | High for CASP1–5; does NOT establish the mechanism for CASPL1D1 |
| [PMID:24920445](https://pubmed.ncbi.nlm.nih.gov/24920445/) | Structural / evolutionary (review + analysis) | **Qualifies MF** | Scaffold propensity of CASP family | CASPs present "all the hallmarks of a membrane scaffold"; family-wide analysis | CASP/CASPL family, evolutionary | Family-level property, not a CASPL1D1-specific assay |
| [PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/) | Mutant phenotype + interaction | **Competing (alternative primary function)** | CASPL1D1 function in root | caspl1d1 caspl1d2 → weak ↑ endodermal suberization, no ΔLp; CASPL1B1/1B2/1D1/1D2 associate with PIP2;1 | A. thaliana root endodermis; control/NaCl | Medium; subtle phenotype, redundancy with 1D2; different tissue/process from immunity |
| UniProt Q9FE29; InterPro/Pfam PF04535; QuickGO | Computational / database | **Supports MF=ND** | Any assignable MF for CASPL1D1 | 4 TM helices, PM localization, homo/heterodimer, CASP similarity; NO FUNCTION comment; MF = GO:0003674 ND | Sequence/domain annotation | High for "no MF assigned"; database-level |
| Needleman–Wunsch alignments (this work) | Computational (reproducible) | **Supports MF=ND** | Can CASP1–5 MF transfer by homology? | CASPL1D1 vs CASP1 = 33.9 %; vs CASPL4D1 = 31.8 % identity; fold-only (PF04535) | UniProt sequences | High; twilight-zone identity precludes function transfer |

---

## GO Curation Implications

**Lead recommendations (require curator verification):**

1. **Molecular Function — keep as ND (do NOT add a specific MF term).**
   No experimental molecular assay exists for CASPL1D1. The membrane-scaffold activity is demonstrated only for CASP1–5 and is a family-level propensity; at ~32–34 % identity it cannot be transferred by homology. Assigning terms such as "structural molecule activity," "protein-containing complex scaffold activity," or a bespoke "membrane microdomain organization" MF to CASPL1D1 would be **over-annotation from shared fold**. Also avoid falling back to "protein binding" (GO:0005515) as a final MF — the homo/heterodimer note is uninformative about the immune mechanism.

2. **Biological Process — support a defense/lignin BP annotation as an IMP lead with a caveat.**
   Candidate terms: **defense response to bacterium** (GO:0042742) and/or **lignin biosynthetic/metabolic process** (GO:0009809 / GO:0009808) in the context of the immune barrier, and **plant-type hypersensitive response** (GO:0009626) given the lesion-spread phenotype. Evidence code **IMP** based on amiCASPL1D1 ([PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/)), annotated with the explicit caveat that the perturbation is an artificial-miRNA knockdown (not a null) and that the cleaner localization/complementation evidence pertains to the paralog CASPL4D1. Curators may prefer to hold this at the "author statement / IMP-with-caveat" level pending a CASPL1D1 null or complementation line.

3. **Cellular Component — retain plasma membrane (GO:0005886) and, if supported, Golgi/endosome trafficking compartments.**
   Consistent with UniProt Q9FE29 (4 TM, PM localization) and CASP-family membrane biology. These are the most defensible annotations.

4. **Do not import the CASP1–5 Casparian-strip / root suberization mechanism onto CASPL1D1** as if it were CASPL1D1's own molecular function. Keep paralog annotations distinct.

---

## Mechanistic Scope

The **immediate molecular function being tested** is a *membrane-organizing / scaffolding* activity: the ability to self-assemble into a stable plasma-membrane microdomain that spatially organizes lignin-deposition machinery and excludes competing secretory factors. This is a genuine, assayable molecular activity — but it has been directly measured only for **CASP1–5** ([PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/)), not for CASPL1D1.

What is actually demonstrated for CASPL1D1 is **downstream and phenotypic**:
- **Loss-of-function phenotype** (leaf): reduced pathogen-induced lignification and failure to contain the HR lesion (amiRNA knockdown; [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/)).
- **Loss-of-function phenotype** (root): weak enlargement of the endodermal suberization zone, no change in hydraulic conductivity ([PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/)).
- **Interaction**: association with PIP2;1 and homo/heterodimerization (database).

None of these establishes the *direct molecular activity*. The barrier phenotype is a **pathway/tissue-level consequence** that could arise from CASPL1D1 acting as a scaffold, as an adaptor, as a trafficking chaperone, or merely as a required-but-accessory subunit. The evidence cannot yet discriminate among these, so the direct molecular function remains undefined.

---

## Conflicts and Alternatives

1. **Paralog confusion (CASPL1D1 vs CASPL4D1).** The strongest cell-biological evidence in [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/) — localization to sites of lignification and genetic complementation — was obtained for **CASPL4D1** (a clean T-DNA-knockout paralog), not CASPL1D1. CASPL1D1 evidence is knockdown-only. The two are only ~32 % identical, so CASPL4D1 results should **not** be read across to CASPL1D1's molecular function.

2. **Tissue/process conflict (leaf immunity vs root suberization).** CASPL1D1's most directly documented mutant phenotype is a **root endodermal suberization** change with aquaporin association ([PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/)), a different tissue and process. This raises the possibility that leaf immune lignification is a **context-specific / secondary** role rather than CASPL1D1's primary function.

3. **Fold-based over-annotation.** The membrane-scaffold mechanism is a **CASP-family hallmark** ([PMID:24920445](https://pubmed.ncbi.nlm.nih.gov/24920445/)) demonstrated for **CASP1–5** ([PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/)). Transferring it to CASPL1D1 relies on shared PF04535 fold alone — precisely the inference the task prohibits.

4. **Knockdown artifact risk.** amiRNA can act off-target and rarely gives a complete null; the observed lignification/HR phenotype could be partly attributable to related transcripts, and the magnitude of CASPL1D1's specific contribution is not cleanly quantified.

5. **Redundancy.** The root phenotype required the *caspl1d1 caspl1d2* double mutant, indicating functional redundancy with CASPL1D2; single-gene MF claims should account for this partial redundancy.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|-----|------------------|-----------------------------|-----------------------|
| No direct MF assay for CASPL1D1 | UniProt, InterPro/Pfam, QuickGO, primary papers | Determines whether any specific MF term is warranted (vs ND) | Biophysical/imaging assay of CASPL1D1 microdomain formation and factor exclusion, as done for CASP1–5 |
| Knockdown vs null | [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/) uses amiRNA for CASPL1D1 | amiRNA phenotype could be partial/off-target; affects IMP confidence | CRISPR null of AT4G15610 + complementation with tagged CASPL1D1 |
| CASPL1D1-specific localization at lignification sites | Only CASPL4D1 localization/complementation shown | Confirms CASPL1D1 acts at the barrier, not just transcriptionally induced | Live imaging of tagged CASPL1D1 at pathogen-induced lignifying foci |
| Primary vs context-specific role | Root ([PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/)) vs leaf ([PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/)) phenotypes | Determines which process (if any) is "core" for GO | Comparative phenotyping across tissues/conditions with the same null allele |
| Interaction partners in the immune context | PIP2;1 (root context) known; immune partners unknown | Distinguishes scaffold vs adaptor vs trafficking models | IP-MS of CASPL1D1 from pathogen-challenged leaves |

**Note:** Missing evidence is not refutation. The MF verdict is "unresolved/not-assignable," not "CASPL1D1 lacks a molecular function" — it may well have scaffold activity; it simply has not been shown for this protein.

---

## Discriminating Tests

The single most decisive question is: **can a specific membrane-organizing molecular function be assigned to CASPL1D1?** The following experiments would discriminate the leading models most efficiently:

1. **CRISPR null + complementation (definitive genetics).** Generate a true AT4G15610 loss-of-function allele; test whether it phenocopies amiCASPL1D1 for AvrRpm1-induced lignification and HR containment, and whether a tagged CASPL1D1 transgene rescues. This removes the amiRNA caveat and upgrades the BP annotation from IMP-with-caveat to a clean IMP.

2. **CASPL1D1-specific localization at lignifying foci.** Live/confocal imaging of a functional fluorescent CASPL1D1 fusion during incompatible infection to test whether the protein concentrates at sites of pathogen-induced lignin deposition (the CASPL4D1 result), directly linking CASPL1D1 to the barrier's spatial organization.

3. **Direct microdomain / scaffold assay.** Apply the same readouts used for CASP1–5 ([PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/)) — FRAP immobility, exclusion of vesicle-tethering markers, microdomain coalescence — to CASPL1D1. A positive result would justify a specific membrane-organizing MF term; a negative result would keep MF at ND and favor an accessory/adaptor model.

4. **IP-MS in the immune context.** Identify CASPL1D1 interactors from pathogen-challenged leaves to distinguish a scaffold (recruits lignification/oxidation machinery) from an adaptor/trafficking role.

5. **Paralog swap / cross-complementation.** Test whether CASPL4D1 can rescue amiCASPL1D1 and vice versa, quantifying functional divergence between the two ~32 %-identical immune CASPLs.

---

## Curation Leads (require curator verification)

**Candidate action changes:**
- **Molecular Function:** *Retain ND.* Reject any lead that assigns a specific membrane-scaffold or "membrane-organizing" MF to CASPL1D1 on current evidence. Do not use "protein binding" as the final MF.
- **Biological Process:** *Add* a defense/lignin-barrier BP annotation as an **IMP lead with an amiRNA-knockdown caveat** (e.g., defense response to bacterium GO:0042742; lignin biosynthetic process GO:0009809; and/or plant-type hypersensitive response GO:0009626). Curators should decide whether to annotate now with a caveat or hold pending a CASPL1D1 null.
- **Cellular Component:** *Retain* plasma membrane (GO:0005886); retain Golgi/endosome trafficking terms if independently supported.

**Candidate references with exact snippets to verify:**
- [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/) — *"lignin accumulates in Arabidopsis leaves in response to incompatible interactions with bacterial pathogens in a manner dependent on Casparian strip membrane domain protein (CASP)-like proteins (CASPLs)"* (BP support; verify CASPL1D1-specific amiRNA data in full text, figure panels for amiCASPL1D1).
- [PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/) — *"We propose that CASP microdomains displace initial secretory foci by excluding vesicle tethering factors"* (mechanism belongs to CASP1–5; use to justify NOT transferring MF).
- [PMID:24920445](https://pubmed.ncbi.nlm.nih.gov/24920445/) — *"CASPs show high stability in their membrane domain, which presents all the hallmarks of a membrane scaffold"* (family-level scaffold, not CASPL1D1-specific).
- [PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/) — *"caspl1d1*caspl1d2 double mutants showed... a weak enlargement of the continuous suberization zone"* (competing primary-function context).

**Suggested curator questions:**
1. Is a T-DNA/CRISPR null available for AT4G15610 yet? If not, annotate BP with the amiRNA caveat.
2. Does any published imaging place CASPL1D1 (not CASPL4D1) at lignifying foci?
3. Should the root suberization role ([PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/)) be captured as a separate BP annotation to reflect pleiotropy?

**Suggested experiments:** CRISPR null + complementation; CASPL1D1-specific localization; direct scaffold/microdomain assay; immune-context IP-MS (see Discriminating Tests).

---

## Evidence Base (Literature)

- *Lignin-based barrier restricts pathogens to the infection site and confers resistance in plants.* — Lee et al., EMBO J 2019. [PMID:31559647](https://pubmed.ncbi.nlm.nih.gov/31559647/). **Primary support for the BP clause**: identifies CASPL1D1 and CASPL4D1 as biotic-stress-induced CASPLs; amiCASPL1D1 knockdown impairs AvrRpm1-induced lignification and HR containment.
- *Directed growth and fusion of membrane-wall microdomains requires CASP-mediated inhibition and displacement of secretory foci.* — [PMID:36959183](https://pubmed.ncbi.nlm.nih.gov/36959183/). **Defines the membrane-organizing mechanism for CASP1–5**, which the seed hypothesis borrows by analogy; supports keeping CASPL1D1 MF as ND.
- *Functional and Evolutionary Analysis of the CASPARIAN STRIP MEMBRANE DOMAIN PROTEIN Family.* — [PMID:24920445](https://pubmed.ncbi.nlm.nih.gov/24920445/). **Establishes scaffold behavior as a family-level hallmark**, not a CASPL1D1-specific property.
- *Regulation of a plant aquaporin by a Casparian strip membrane domain protein-like.* — Champeyroux et al. 2019. [PMID:30767240](https://pubmed.ncbi.nlm.nih.gov/30767240/). **Competing context**: CASPL1D1's most direct mutant phenotype (root suberization) and PIP2;1 association.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)