---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T05:16:31.455090'
end_time: '2026-09-21T05:31:13.204938'
duration_seconds: 881.75
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: WIPI2
  gene_symbol: WIPI2
  uniprot_accession: Q9Y4P8
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: selective-pexophagy-nucleophagy-and-glycophagy
  hypothesis_text: 'Human WIPI2 (Q9Y4P8) participates in pexophagy, nucleophagy and
    glycophagy. Assess each separately, examining the actual PTN000132136 ancestral
    assignments, WIPI paralog divergence and primary mechanism. WIPI2 may contribute
    common phagophore/ATG16L1 adaptor machinery without being the selective cargo
    receptor; absence of cargo-recognition function does not exclude participation.
    Read GO definitions and parents: nucleophagy is not necessarily restricted to
    yeast piecemeal microautophagy of the nucleus. Distinguish general requirement
    or perturbation from a direct shared-machinery step in each selective pathway,
    and lack of a target-specific experiment from evidence of evolutionary loss.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/WIPI2/WIPI2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human WIPI2 (Q9Y4P8) participates in pexophagy,\
    \ nucleophagy and glycophagy. Assess each separately,\n  examining the actual\
    \ PTN000132136 ancestral assignments, WIPI paralog divergence and primary mechanism.\n\
    \  WIPI2 may contribute common phagophore/ATG16L1 adaptor machinery without being\
    \ the selective cargo receptor;\n  absence of cargo-recognition function does\
    \ not exclude participation. Read GO definitions and parents:\n  nucleophagy is\
    \ not necessarily restricted to yeast piecemeal microautophagy of the nucleus.\
    \ Distinguish\n  general requirement or perturbation from a direct shared-machinery\
    \ step in each selective pathway, and\n  lack of a target-specific experiment\
    \ from evidence of evolutionary loss.'\nfocus_type: function_assignment\ncontext:\
    \ []\nreference_id: []"
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
citation_count: 6
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifacts_WIPI2_GO_decision_table.csv
  path: openscientist_artifacts/artifacts_WIPI2_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist WIPI2 GO decision table
- filename: artifacts_WIPI2_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_WIPI2_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist WIPI2 evidence matrix
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
- **Gene directory:** WIPI2
- **Gene symbol:** WIPI2
- **UniProt accession:** Q9Y4P8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** selective-pexophagy-nucleophagy-and-glycophagy
- **Source file:** genes/human/WIPI2/WIPI2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human WIPI2 (Q9Y4P8) participates in pexophagy, nucleophagy and glycophagy. Assess each separately, examining the actual PTN000132136 ancestral assignments, WIPI paralog divergence and primary mechanism. WIPI2 may contribute common phagophore/ATG16L1 adaptor machinery without being the selective cargo receptor; absence of cargo-recognition function does not exclude participation. Read GO definitions and parents: nucleophagy is not necessarily restricted to yeast piecemeal microautophagy of the nucleus. Distinguish general requirement or perturbation from a direct shared-machinery step in each selective pathway, and lack of a target-specific experiment from evidence of evolutionary loss.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human WIPI2 (Q9Y4P8) participates in pexophagy, nucleophagy and glycophagy. Assess each separately,
  examining the actual PTN000132136 ancestral assignments, WIPI paralog divergence and primary mechanism.
  WIPI2 may contribute common phagophore/ATG16L1 adaptor machinery without being the selective cargo receptor;
  absence of cargo-recognition function does not exclude participation. Read GO definitions and parents:
  nucleophagy is not necessarily restricted to yeast piecemeal microautophagy of the nucleus. Distinguish
  general requirement or perturbation from a direct shared-machinery step in each selective pathway, and
  lack of a target-specific experiment from evidence of evolutionary loss.'
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

# WIPI2 (Q9Y4P8) in Pexophagy, Nucleophagy and Glycophagy — Focused Curation Report

**Gene:** WIPI2 (human, NCBITaxon:9606) · **UniProt:** Q9Y4P8 · **PANTHER family:** PTHR11227 (WIPI/Atg18 PROPPIN family), subfamily SF27
**Focus:** function_assignment · **Hypothesis slug:** selective-pexophagy-nucleophagy-and-glycophagy
**Terms under review:** GO:0000425 pexophagy · GO:0044804 nucleophagy · GO:0061723 glycophagy (all currently **IBA**)

---

## Executive Judgment

**Verdict: Partially supported — retain as non-core, shared-machinery participation; do not treat as WIPI2-specific selective functions.**

The seed hypothesis is essentially correct on mechanism. Human WIPI2's only experimentally supported activity is a **generic core step of autophagosome biogenesis**: it senses PI3P and recruits the ATG12–ATG5–ATG16L1 (E3) complex, allosterically activating LC3/GABARAP lipidation (PMID:24954904, PMID:32437499, PMID:20505359). Pexophagy, glycophagy (both defined by GO as "by macroautophagy") and mammalian macro-nucleophagy all build canonical LC3/GABARAP double-membrane autophagosomes and therefore **mechanistically require this WIPI2 step**. In that sense WIPI2 "participates" — exactly as it demonstrably does in Salmonella xenophagy, where WIPI2b coats the bacterial membrane and recruits ATG12-5-16L1 (PMID:24954904).

However, three important caveats keep this at **partially supported / non-core** rather than "supported":

1. **No target-specific experiment exists for human WIPI2** in any of the three pathways. All three annotations are phylogenetic inferences (**IBA, ECO:0000318, GO_Central, GO_REF:0000033**), not IDA/IMP on WIPI2.
2. **WIPI2 is not the cargo/selectivity receptor** for any of the three: pexophagy uses NBR1/p62 + ubiquitinated PEX5 (+PEX2 E3); mammalian nucleophagy uses a direct LC3–LMNB1 interaction; glycophagy uses STBD1 (CBM20+LIR→GABARAPL1/RB1CC1). The seed's own framing — "may contribute common phagophore/ATG16L1 adaptor machinery without being the selective cargo receptor" — is confirmed.
3. **The IBA seeds are loss-of-function "general requirement" experiments** on the yeast/fly ortholog acting as core machinery, and the same blanket annotation was propagated identically to all four human paralogs (WIPI1/2/3/4), which have functionally diverged (ATG16L1 arm vs ATG2 arm). IBA cannot resolve this.

**Bottom line for the curator:** The activity is real but generic. These BP terms are defensible as "required-for/part-of" shared machinery, but they are **not** evidence that WIPI2 has a peroxisome-, nucleus-, or glycogen-specific function. If the review's convention is to record only pathway-specific or core functions, these three should be flagged **non-core / generalizable to macroautophagy (GO:0016236) / autophagosome assembly (GO:0000045)**, which WIPI2 *does* hold by direct experiment.

---

## Evidence Matrix

| # | Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | QuickGO/GO_Central (GO_REF:0000033) | review/database | Qualifies | Are WIPI2's pexophagy/nucleophagy/glycophagy annotations experimental? | All three (+mitophagy) are **IBA only**; no IDA/IMP/EXP on Q9Y4P8 | Human WIPI2 annotation set (50 annotations) | High for the fact; IBA ≠ direct evidence |
| 2 | 24954904 (Dooley 2014) | direct assay + interaction | Supports (shared machinery) | WIPI2 molecular function | ATG16L1 directly binds WIPI2b; WIPI2b is PI3P effector required for LC3 conjugation; also required for autophagic clearance of *Salmonella* | Human cells, MEFs, GUV | High; xenophagy shows shared-machinery role in a *selective* pathway |
| 3 | 32437499 (Fracchiolla 2020) | direct assay (reconstitution) | Supports (shared machinery) | WIPI2 activates LC3 lipidation | On GUVs, LC3 lipidation strictly requires PI3P-dependent WIPI2, which allosterically activates the E3 complex | In vitro reconstitution | High; defines generic mechanism, not cargo-specific |
| 4 | 20505359 (Polson 2010) | localization + mutant | Supports (core function) | WIPI2 localizes/regulates lipidation | WIPI2 at omegasome-anchored phagophores; positively regulates LC3 lipidation (IDA/IMP source for CC/BP) | Human cells | High |
| 5 | 11739783 (yeast ATG18) | mutant phenotype (IMP) | Qualifies (IBA seed, pexophagy) | Is the Atg18 ortholog required for pexophagy? | S. cerevisiae Atg18 required for pexophagy | Yeast | Seed of pexophagy IBA; general requirement, core machinery |
| 6 | 18701704; 22768199 (yeast ATG18/ATG21) | mutant phenotype (IMP) | Qualifies (IBA seed, nucleophagy) | Atg18/Atg21 required for nucleophagy (PMN) | Core Atg cohort incl. Atg18 required for piecemeal microautophagy of the nucleus | Yeast | Seed of nucleophagy IBA; yeast PMN |
| 7 | 24265594 (Zirin/Perrimon, Drosophila) | mutant phenotype (IMP) | Qualifies (IBA seed, glycophagy) | Is Atg18a required for glycogen breakdown? | Whole core Atg set (incl. **Atg18a**) required for autophagic glycogen degradation | Drosophila | **Within-family experimental seed** legitimizing glycophagy IBA; core machinery, not receptor |
| 8 | 26524528; 26654219 (Dou 2015/2016) | direct assay + mutant | Competing (nucleophagy mechanism) | What confers nuclear selectivity? | Direct **LC3–LMNB1** interaction targets lamin-associated domains; drives oncogene-induced senescence | Human primary cells | High; selectivity is LC3–cargo, WIPI2 not implicated as receptor |
| 9 | 39236246 (Zhang 2024) | structural + direct assay | Competing (glycophagy receptor) | What confers glycogen selectivity? | **STBD1** CBM20 binds glycogen; LIR binds GABARAPL1 and recruits RB1CC1/FIP200 | Human, structures | High; WIPI2 is not the glycophagy receptor |
| 10 | 36541703; 37493040; 39765694 | mutant/localization | Competing (pexophagy receptor) | What confers peroxisome selectivity? | NBR1/p62 + ubiquitinated PEX5, PEX2 E3 drive mammalian pexophagy | Human/zebrafish/rat | High; WIPI2 not the pexophagy receptor |
| 11 | QuickGO paralog scan | computational/database | Qualifies (paralog over-propagation) | Is the IBA paralog-specific? | Identical IBA (pexo/nucleo/glyco/mito) on WIPI1, WIPI2, WIPI3/WDR45B, WIPI4/WDR45 | Human paralogs | High; IBA cannot resolve ATG16L1-arm vs ATG2-arm divergence |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current | Evidence for WIPI2 | Lead recommendation |
|---|---|---|---|---|
| GO:0000425 pexophagy | BP | IBA | Ortholog general-requirement (yeast Atg18); no human WIPI2 experiment; not the receptor | **Retain as non-core OR generalize.** Legitimate IBA, but flag as shared-machinery/"required-for" rather than a WIPI2-specific function. If the review disallows unverified selective-autophagy terms, generalize to GO:0016236/GO:0000045. |
| GO:0044804 nucleophagy | BP | IBA | Ortholog requirement in yeast PMN; mammalian selectivity is LC3–LMNB1, not WIPI2 | **Retain as non-core.** Definition is broad (not restricted to yeast PMN), so IBA is not term-inappropriate, but treat as shared machinery. |
| GO:0061723 glycophagy | BP | IBA | **Within-family experimental seed = Drosophila Atg18a (PMID:24265594)**; mammalian receptor is STBD1 | **Retain as non-core.** IBA is phylogenetically valid; not WIPI2-cargo-specific. |
| GO:0016236 macroautophagy / GO:0000045 autophagosome assembly | BP | IMP/IDA (direct) | Direct experiments (PMID:20505359, 24954904, 28561066) | **Retain as core** — this is WIPI2's primary, directly supported BP. |
| GO:0032266 PI3P binding; GO:0030674 adaptor activity | MF | IDA/IBA | Direct (PMID:20505359, 28561066) | **Retain as core MF** — more informative than "protein binding". |

**Recommended framing:** WIPI2's *core* annotations are the PI3P-binding/ATG16L1-adaptor MF and macroautophagy/autophagosome-assembly BP. The three selective-autophagy BP terms are **downstream, pathway-context consequences of that same single molecular step**, delivered via IBA; they should be labeled **non-core / shared-machinery**, not removed as wrong (each has a valid within-family experimental seed), and certainly not read as cargo-recognition functions.

---

## Mechanistic Scope

- **Immediate molecular function (direct):** PI3P-dependent β-propeller effector that recruits/allosterically activates the ATG12–ATG5–ATG16L1 E3 to lipidate LC3/GABARAP onto the phagophore (PMID:24954904, 32437499). Location: phagophore assembly site / omegasome / autophagosome membrane (IDA).
- **Downstream / pathway-context (inferred):** Because pexophagy and glycophagy are *macroautophagy* (GO definitions explicitly state "by macroautophagy") and mammalian nucleophagy of lamin B1 is autophagosome-mediated, loss of WIPI2 would impair all of them — but this is a **general requirement**, identical to losing any core Atg factor, not a peroxisome/nucleus/glycogen-specific activity.
- **Not attributable to WIPI2:** cargo selection (NBR1/p62/ubiquitin-PEX5; LC3–LMNB1; STBD1–glycogen). These provide the selectivity; WIPI2 provides the shared build step.

---

## Conflicts and Alternatives

- **Paralog over-annotation:** All four human WIPI paralogs carry identical IBA for the four selective terms. WIPI1/WIPI2 operate in the ATG16L1-recruiting arm; WIPI3(WDR45B)/WIPI4(WDR45) operate with ATG2 in lipid transfer. Blanket IBA cannot distinguish these — a database carry-over artifact, though not necessarily biologically false (all are required for autophagosome formation).
- **Organism-specific seeds:** The pexophagy/nucleophagy seeds are yeast (piecemeal microautophagy for PMN); glycophagy seed is Drosophila. Extrapolation to human WIPI2 is inference, not observation.
- **Competing selectivity mechanisms:** For each pathway, the literature attributes selectivity to dedicated receptors, not WIPI2 — so any curation implying WIPI2 confers selective recognition would be an over-statement.
- **"General requirement vs direct shared step":** The seed asks to distinguish these. The available evidence is loss-of-function *requirement* (IMP) plus a mechanistic *direct step* (PI3P→ATG16L1→LC3) that is generic; there is no experiment isolating a WIPI2 step *within* pexophagy/nucleophagy/glycophagy specifically.

---

## Knowledge Gaps

1. **No human WIPI2 loss-of-function in any of the three pathways.** Checked QuickGO (0 experimental annotations). Matters because IBA alone is being asked to justify three BP terms. Resolve with WIPI2 KO/KD + peroxisome (PMP70/PEX14), lamin B1, or glycogen turnover readouts.
2. **Paralog specificity.** Checked annotation blanketing across WIPI1/2/3/4. Matters because curators may want paralog-resolved terms. Resolve with paralog-specific KO rescue in each selective assay.
3. **Whether nucleophagy of lamin B1 requires WIPI2 at all** vs. proceeding through a non-canonical/WIPI-independent route. Checked: Dou papers implicate LC3 directly but did not test WIPI2. Resolve with WIPI2 dependence test in RAS-induced senescence lamin B1 degradation.
4. **Glycophagy dependence on WIPI2 specifically in mammals** (Drosophila seed only). Resolve with STBD1-based glycophagy flux assay under WIPI2 depletion.

---

## Discriminating Tests

1. **WIPI2 depletion + selective-flux readouts:** pexophagy (peroxisome number/PMP70, HaloTag-PTS1 processing), nucleophagy (lamin B1 degradation in oncogene-induced senescence, PMID:26524528 model), glycophagy (glycogen/PAS or 2-NBDG flux, STBD1 reporter). Expectation if "shared machinery only": all three blocked to the same degree as bulk autophagy, with no additional selectivity phenotype.
2. **Separation-of-function ATG16L1-binding mutant of WIPI2** (WIPI2b residues that bind ATG16L1 vs PI3P): should block all three pathways coordinately, confirming the single shared step.
3. **Paralog swap/rescue:** test whether WIPI3/WIPI4 (ATG2 arm) rescue each selective pathway in WIPI2-null cells, to resolve paralog-specific claims.
4. **Proximity/interaction proteomics of WIPI2 vs receptors** (STBD1, NBR1, LMNB1): absence of direct cargo-receptor complexes would corroborate "no selectivity role."

---

## Curation Leads (require curator verification)

- **Candidate action:** Keep GO:0000425 / GO:0044804 / GO:0061723 as **IBA/non-core, shared-machinery** annotations; add an annotation note that WIPI2 acts as generic autophagosome-biogenesis machinery, not a cargo receptor. Do **not** upgrade to experimental; do **not** remove outright (each IBA has a valid within-family experimental seed).
- **Candidate core terms to foreground instead:** MF GO:0032266 (PI3P binding), MF GO:0030674 (protein-macromolecule adaptor activity), BP GO:0000045 (autophagosome assembly), BP GO:0016236 (macroautophagy), CC GO:0000407 (phagophore assembly site) — all direct-evidence supported. Prefer these over "protein binding".
- **Candidate references with exact snippets to verify:**
  - PMID:24954904 — "Atg16L1 directly binds WIPI2b … WIPI2b is a PtdIns(3)P effector upstream of Atg16L1 and is required for LC3 conjugation … WIPI2b is also required for autophagic clearance of pathogenic bacteria."
  - PMID:32437499 — "LC3 lipidation is strictly dependent on the recruitment of WIPI2 that in turn depends on PI(3)P … WIPI2 allosterically activate[s] the E3 complex."
  - PMID:24265594 — Drosophila core Atg genes (incl. Atg18a) required for autophagic glycogen breakdown (glycophagy IBA seed).
  - PMID:26524528 — "The autophagy protein LC3/Atg8 … directly interacts with the nuclear lamina protein lamin B1" (nucleophagy selectivity is LC3–cargo, not WIPI2).
  - PMID:39236246 — STBD1 CBM20/LIR mechanism of glycophagy selectivity.
- **Suggested question for curator:** Does this review's policy annotate core autophagy machinery to each selective-autophagy sub-process (IBA), or restrict such terms to factors with pathway-specific experimental evidence? The answer determines retain-as-non-core vs generalize.
- **Suggested experiments:** the four discriminating tests above.

---

### Provenance
Machine-readable artifacts: `artifacts/WIPI2_evidence_matrix.csv`, `artifacts/WIPI2_GO_decision_table.csv`.

Computed with QuickGO REST (annotation + ontology endpoints) and PANTHER geneinfo, executed in-session (iterations 1–3):
- WIPI2 annotation pull (50 rows) → three target terms are IBA only.
- GO term definition pull → pexophagy/glycophagy "by macroautophagy"; nucleophagy broadly defined (not yeast-PMN-restricted).
- Paralog scan (WIPI1/2/3/4 + yeast Atg18/Atg21/Hsv2) → identical blanket IBA; yeast Atg18 IMP seeds pexophagy/nucleophagy.
- Cross-family experimental-source scan → glycophagy seeded by Drosophila Atg18a (PMID:24265594); human experimental annotations for all three terms are on dedicated receptors/regulators, never WIPI2.


## Artifacts

- [OpenScientist WIPI2 GO decision table](openscientist_artifacts/artifacts_WIPI2_GO_decision_table.csv)
- [OpenScientist WIPI2 evidence matrix](openscientist_artifacts/artifacts_WIPI2_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)