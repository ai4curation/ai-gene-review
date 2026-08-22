---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T15:54:06.304744'
end_time: '2026-08-22T16:16:52.873079'
duration_seconds: 1366.57
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: SSA2
  gene_symbol: SSA2
  uniprot_accession: P10592
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: existing_go_annotation_decision
  hypothesis_slug: existing-go-0005886-keep-as-non-core
  hypothesis_text: 'The existing SSA2 GO annotation to plasma membrane (GO:0005886)
    should receive review action KEEP_AS_NON_CORE. Current rationale: Retain conservatively
    because a stripped-plasma-membrane proteomics study detected Ssa2, but this high-throughput
    fractionation evidence does not establish the plasma membrane as a primary site
    of Ssa2 function.'
  term_context: '- Term: plasma membrane (GO:0005886)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033

    - Current review action: KEEP_AS_NON_CORE

    - Review summary: SSA2 has been detected at the plasma membrane by HDA (PMID:16622836).
    IBA is consistent.

    - Review reason: Retain conservatively because a stripped-plasma-membrane proteomics
    study detected Ssa2, but this high-throughput fractionation evidence does not
    establish the plasma membrane as a primary site of Ssa2 function.'
  reference_context: '- GO_REF:0000033'
  source_file: genes/yeast/SSA2/SSA2-ai-review.yaml
  source_selector: existing_annotations[3]
  source_context_yaml: "term:\n  id: GO:0005886\n  label: plasma membrane\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033\nreview:\n  summary: SSA2 has been\
    \ detected at the plasma membrane by HDA (PMID:16622836). IBA is consistent.\n\
    \  action: KEEP_AS_NON_CORE\n  reason: Retain conservatively because a stripped-plasma-membrane\
    \ proteomics study detected Ssa2, but\n    this high-throughput fractionation\
    \ evidence does not establish the plasma membrane as a primary site\n    of Ssa2\
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** SSA2
- **Gene symbol:** SSA2
- **UniProt accession:** P10592

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** existing-go-0005886-keep-as-non-core
- **Source file:** genes/yeast/SSA2/SSA2-ai-review.yaml
- **Source selector:** existing_annotations[3]

## Seed Hypothesis

The existing SSA2 GO annotation to plasma membrane (GO:0005886) should receive review action KEEP_AS_NON_CORE. Current rationale: Retain conservatively because a stripped-plasma-membrane proteomics study detected Ssa2, but this high-throughput fractionation evidence does not establish the plasma membrane as a primary site of Ssa2 function.

## Term and Decision Context

- Term: plasma membrane (GO:0005886)
- Evidence type: IBA
- Original reference: GO_REF:0000033
- Current review action: KEEP_AS_NON_CORE
- Review summary: SSA2 has been detected at the plasma membrane by HDA (PMID:16622836). IBA is consistent.
- Review reason: Retain conservatively because a stripped-plasma-membrane proteomics study detected Ssa2, but this high-throughput fractionation evidence does not establish the plasma membrane as a primary site of Ssa2 function.

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
  summary: SSA2 has been detected at the plasma membrane by HDA (PMID:16622836). IBA is consistent.
  action: KEEP_AS_NON_CORE
  reason: Retain conservatively because a stripped-plasma-membrane proteomics study detected Ssa2, but
    this high-throughput fractionation evidence does not establish the plasma membrane as a primary site
    of Ssa2 function.
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

# SSA2 (P10592) — Review of GO:0005886 "plasma membrane" annotation

**Focus:** existing_go_annotation_decision · `existing-go-0005886-keep-as-non-core`
**Term:** plasma membrane (GO:0005886) · Evidence: IBA · Ref: GO_REF:0000033
**Current action under test:** KEEP_AS_NON_CORE
**Iteration:** finalized in Iteration 3 of 3

> **Data-integrity note (Iteration 2, QuickGO/EBI live check):** In the current GO database the
> **only** plasma-membrane (GO:0005886) annotation for SSA2 is **HDA from PMID:16622836** (SGD).
> There is **no IBA annotation to plasma membrane** — the IBA (GO_REF:0000033, GO_Central) pipeline
> propagated only cytosol/cytoplasm/nucleus to SSA2. The seed row's `evidence_type: IBA` for GO:0005886
> therefore appears to be a **mismatch**; the reviewed term is HDA-only. The paralog **SSA1 (P10591)
> carries the identical single HDA PM annotation from the same paper**, consistent with shared-peptide
> paralog co-detection (SSA1/SSA2 ≈97% identical). This does not change the verdict but should be
> corrected in the review.

---

## Executive Judgment

**Verdict: Partially supported — the KEEP_AS_NON_CORE action is justified (conservative and appropriate).**

The plasma-membrane annotation is real in the databases but weakly grounded. It rests on
(1) a single high-throughput proteomics detection in a *stripped* plasma-membrane fraction
(PMID:16622836, Delom et al. 2006) recorded as HDA, and (2) an IBA phylogenetic propagation
from the HSP70 family (GO_REF:0000033). Neither establishes plasma membrane as a **primary
site of Ssa2 function**. SSA2 is one of the most abundant cytosolic Hsp70 chaperones and has
**no transmembrane domain, no signal peptide, and no lipid anchor** (UniProt P10592), so its
appearance in a membrane pellet is best explained by abundant-cytosolic-protein carryover —
the same fractions routinely capture elongation factors and enolase (PMID:16544286). There is
genuine cell-periphery biology (histatin-5 receptor at the cell envelope, PMID:12761219;
secreted/cell-wall and extracellular-vesicle IDA annotations), but that is **cell wall/secreted**,
not integral plasma membrane.

**Most important caveats:** (a) The evidence would also support a defensible *remove/do-not-propagate*
argument for the IBA specifically; KEEP_AS_NON_CORE is the more conservative of two reasonable
choices. (b) Curators should ensure the term is never treated as core and that the richer, better-
evidenced peripheral terms (cell wall GO:0009277, extracellular region/vesicle) carry the
cell-surface story instead.

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:16622836 | Localization, HT proteomics (HDA) | Qualifies | Ssa2 is at the PM | ~90 proteins from a *stripped* PM fraction (dodecyl-maltoside, IEC/LDS-PAGE + LC-MS/MS); Ssa2 detected | S. cerevisiae stripped PM | Weak — single HT study, no functional follow-up; abundant-protein carryover likely |
| QuickGO/EBI live check | Database provenance | Refutes (seed evidence_type) | GO:0005886 is supported by IBA (per seed) | **No IBA to PM exists**; live PM annotation is HDA-only (PMID:16622836). IBA (GO_REF:0000033) covers only cytosol/cytoplasm/nucleus. Paralog SSA1 has identical single HDA PM annotation. | GO/SGD/GO_Central, 2026 snapshot | Strong; corrects the seed row's evidence code |
| UniProt P10592 | Database / sequence-feature | Refutes (core) | Ssa2 is an integral/core PM protein | No TM, no signal peptide, no lipidation; curated location = Cytoplasm; Secreted, cell wall; PM only as HDA; no "Membrane" keyword | UniProtKB curated | Strong against integral PM residence; soluble protein |
| PMID:16544286 | Methodological control | Qualifies | PM fractions are clean | Yeast surface/membrane proteomics fractions also recover elongation factors & other cytoplasmic proteins | S. cerevisiae surface proteomics | Supports contamination interpretation |
| PMID:12761219 | Direct assay + mutant phenotype | Competing | Ssa1/2p works at the cell periphery | Ssa1/2p is the cell-envelope receptor for histatin-5; co-localized on cell-wall extracts AND cytosolic fractions; Δssa1Δssa2 lowers binding/killing | C. albicans & S. cerevisiae | Real cell-surface role, but **cell wall/envelope**, not PM per se |
| PMID:25853343 | Direct assay | Competing | Primary site of Ssa2 function | Ssa2p = major cytoplasmic Hsp70; nuclear tRNA import, binds Nup116 | S. cerevisiae | Core = cytosolic/nuclear chaperone-carrier |
| PMID:29651044; PMID:10745074 | Direct assay | Competing | Ssa1/2 core molecular function | Cytosolic Hsp70 chaperone activity in protein import/folding (aconitase mito import; Ape1 vacuolar transport) | S. cerevisiae | Membrane association is transient / client-directed |

*Provenance: `/tmp/SSA2_GO0005886_evidence_matrix.csv`, `/tmp/SSA2_CC_landscape.csv` (computed this run).*

## GO Curation Implications

- **Lead (requires curator verification): KEEP the GO:0005886 annotation but treat it as NON-CORE** — consistent with the seed action.
  - It is a **CC** term. Evidence supports *presence at* but not *function at* the plasma membrane.
  - Do **not** generalize it to a core location term (cytoplasm/cytosol IDA already carry the core CC).
  - **Alternative lead worth flagging:** because the sole experimental support is one stripped-membrane HT proteomics hit for a hyper-abundant soluble chaperone, a curator could reasonably down-weight or not-propagate the **IBA** (mark with NOT/annotation-extension review) while retaining the HDA as non-core. This is a stronger-scrutiny option, not a recommendation to delete outright.
  - Ensure the **better-evidenced peripheral terms** are the ones telling the cell-surface story: fungal-type cell wall (GO:0009277, IDA), extracellular vesicle (GO:1903561, IDA), secreted/extracellular region.

SSA2 cellular-component landscape (from UniProt/SGD): cytoplasm (IDA, core), cytosol (IDA, core),
fungal-type cell wall (IDA), extracellular vesicle (IDA), fungal-type vacuole membrane (IDA),
mitochondrion (IDA), nucleus (IBA), **plasma membrane (HDA + IBA → non-core, weak).**

## Mechanistic Scope

The immediate molecular function of Ssa2 is **ATP-dependent Hsp70 chaperone activity** (nucleotide-
binding domain + substrate-binding domain) acting in the **cytosol/nucleus**: de novo folding,
post-translational translocation across organelle membranes, tRNA nuclear import, and assembly of
client complexes. Any plasma-membrane signal is **downstream/associative**, not a direct PM
activity: (i) fraction co-purification of an abundant soluble protein, and (ii) transient,
client-directed membrane engagement (e.g., inserting viral replication proteins into membranes,
PMID:19153242). None of these convert PM into a site of intrinsic Ssa2 molecular function.

## Conflicts and Alternatives

- **Contamination / frequency bias:** Ssa2's extreme cytosolic abundance makes membrane-pellet
  detection the expected null result; the control literature (PMID:16544286) confirms cytoplasmic
  carryover in these fractions.
- **Paralog confusion:** Ssa1/Ssa2 are ~97% identical and functionally redundant; several
  "cell-surface Ssa" studies (e.g., histatin) cannot resolve Ssa1 vs Ssa2 vs Ssa3/4. Cell-surface
  claims may be family-level, not SSA2-specific. **Confirmed:** SSA1 (P10591) carries the *identical*
  single HDA PM annotation from the same paper (PMID:16622836), i.e. the proteomics signal was
  propagated to both paralogs and cannot distinguish them.
- **Evidence-code carry-over (data integrity):** the seed labels the reviewed annotation `IBA`
  (GO_REF:0000033), but the live GO record has **no IBA to plasma membrane**; the term is HDA-only.
  The "IBA is consistent" rationale in the review summary does not apply and should be revised.
- **Location mis-typing:** the strongest peripheral evidence points to **cell wall/cell envelope
  and secreted**, which are distinct from the plasma membrane; GO:0005886 may be a coarse stand-in
  for these better-supported terms.
- **IBA source strength:** the phylogenetic call inherits mammalian Hsc70 PM annotations, whose own
  "PM" status is itself partly surface/associative.

## Knowledge Gaps

1. **Is Ssa2 genuinely at the PM vs cell wall?** Checked: UniProt features (no TM/anchor), Delom
   proteomics (stripped PM), histatin papers (cell wall). Matters because it decides cell-wall vs PM
   term. Resolve with GFP/split-GFP PM-marker co-localization or protease-shaving surface proteomics
   with strict PM-marker controls.
2. **Paralog specificity.** Checked: sequence identity/redundancy literature. Matters for SSA2-
   specific annotation. Resolve with Ssa2-only tagged strains in an ssa1Δ ssa3Δ ssa4Δ background.
3. **Functional consequence at the PM.** Checked: no functional PM assay exists. Matters because
   "non-core" hinges on absence of a PM function. Resolve with PM-targeted degron/anchor-away tests
   for a PM-localized phenotype.
4. **Quantitative abundance rank.** The contamination argument leans on Ssa2 being among the most
   abundant cytosolic proteins. Checked: attempted a programmatic PaxDb lookup (YLL024C) — the PaxDb
   API was **not accessible (HTTP 404)**, so no numeric rank is reported here to avoid fabrication.
   The abundance is nonetheless well documented in the literature (Hsp70 Ssa1/Ssa2 are among the
   highest-copy chaperones; UniProt lists "Direct protein sequencing"). A curator can confirm the
   exact rank via PaxDb/SGD abundance datasets; this would further quantify carryover risk.

## Discriminating Tests

- **Quantitative co-localization** of Ssa2-GFP with a bona-fide PM marker (e.g., Pma1-mCherry) vs a
  cell-wall marker, in live cells — distinguishes PM from wall/cytosol.
- **Fractionation with sucrose-gradient PM enrichment + abundance normalization**: does Ssa2 enrich
  with PM markers beyond its bulk cytosolic level, or track with soluble contaminants?
- **Surface biotinylation / trypsin-shaving** of intact spheroplasts to test true surface exposure.
- **Cross-reference** SGD/GO annotation provenance to confirm the HDA derives solely from Delom 2006
  and whether the IBA has independent experimental support in the HSP70 tree.

## Curation Leads (require curator verification)

- **Action:** Retain seed action **KEEP_AS_NON_CORE** for GO:0005886. Rationale is sound.
- **Correct the review metadata:** change `evidence_type` for GO:0005886 from **IBA → HDA** (live GO
  shows HDA/PMID:16622836 only; no IBA to PM). Revise the review summary sentence "IBA is consistent"
  because no PM IBA exists. Verify against QuickGO (`geneProductId=P10592&goId=GO:0005886`).
- **Candidate reference to cite in the review:** PMID:16622836 — verify snippet: *"Proteins from a
  stripped plasma membrane fraction were solubilized with the neutral and non-denaturing detergent,
  the n-dodecyl beta-D-maltoside."* (documents the HT/fractionation nature of the evidence).
- **Contamination-control reference:** PMID:16544286 — verify snippet: *"Elongation factors,
  mitochondrial membrane proteins and a mannosyltransferase... were also identified in this
  fraction."* (supports carryover interpretation).
- **Competing/peripheral biology reference:** PMID:12761219 — verify snippet: *"co-localized on
  immunoblots of yeast beta-mercaptoethanol cell wall extracts and cytosolic fractions."*
- **Candidate refinement:** ensure cell-surface signal is represented by GO:0009277 (fungal-type
  cell wall, IDA) and GO:1903561 (extracellular vesicle, IDA), so PM is not over-interpreted.
- **Optional stronger-scrutiny lead:** flag the **IBA** GO:0005886 for reduced propagation confidence
  given the single abundant-protein HT source; do not delete without curator review.
- **Suggested question for curator:** Should GO:0005886 be down-graded/annotated with an evidence
  note distinguishing "detected in PM fraction" from "functions at PM"?

---

*Analyses run: NCBI eutils fetch of PMID:16622836; UniProt P10592 feature/localization/GO-CC parse;
QuickGO/EBI live annotation query for P10592 and P10591 (Iteration 2); evidence-matrix and
CC-landscape tables (saved to /tmp).*

*Iteration-2 QuickGO result (verbatim): SSA2 GO:0005886 = 1 annotation, evidence=HDA,
ref=PMID:16622836, by=SGD; SSA1 GO:0005886 = 1 annotation, evidence=HDA, ref=PMID:16622836, by=SGD.
Full SSA2 CC set (16 annotations) shows IBA/GO_REF:0000033 only on GO:0005634, GO:0005737, GO:0005829.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)