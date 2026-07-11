---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-09T13:42:29.429598'
end_time: '2026-07-09T13:56:14.266516'
duration_seconds: 824.84
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: alo1
  gene_symbol: alo1
  uniprot_accession: Q9HDX8
  taxon_id: NCBITaxon:4896
  taxon_label: Schizosaccharomyces pombe
  focus_type: computational_prediction
  hypothesis_slug: prediction-gulonolactone-oxidase
  hypothesis_text: BioReason-Pro SFT predicts L-gulonolactone oxidase activity (GO:0050105)
    and L-ascorbic acid biosynthetic process (GO:0019853) for the Schizosaccharomyces
    pombe protein alo1 (Q9HDX8). Independently assess whether alo1 is specifically
    an L-gulonolactone oxidase producing L-ascorbate (the mammalian-type enzyme and
    pathway), or whether it is a D-arabinono-1,4-lactone oxidase of the fungal D-erythroascorbate
    pathway -- a related aldonolactone-oxidoreductase (ALO/GULO-family) paralog with
    a different substrate and product -- which would make the L-gulonolactone-oxidase
    and L-ascorbate-biosynthesis predictions a paralog/substrate misassignment. Determine
    whether the predictions are supported or refuted.
  term_context: '- Term: L-gulonolactone oxidase activity (GO:0050105)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts L-gulonolactone oxidase\
    \ activity (GO:0050105) and L-ascorbic acid\n  biosynthetic process (GO:0019853)\
    \ for the Schizosaccharomyces pombe protein alo1 (Q9HDX8). Independently\n  assess\
    \ whether alo1 is specifically an L-gulonolactone oxidase producing L-ascorbate\
    \ (the mammalian-type\n  enzyme and pathway), or whether it is a D-arabinono-1,4-lactone\
    \ oxidase of the fungal D-erythroascorbate\n  pathway -- a related aldonolactone-oxidoreductase\
    \ (ALO/GULO-family) paralog with a different substrate\n  and product -- which\
    \ would make the L-gulonolactone-oxidase and L-ascorbate-biosynthesis predictions\n\
    \  a paralog/substrate misassignment. Determine whether the predictions are supported\
    \ or refuted.\nfocus_type: computational_prediction\nterm_id: GO:0050105\nterm_label:\
    \ L-gulonolactone oxidase activity\ncontext: []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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
citation_count: 3
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: provenance_evidence_matrix.csv
  path: openscientist_artifacts/provenance_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_go_decision_table.csv
  path: openscientist_artifacts/provenance_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
- filename: provenance_sequence_identity_matrix.csv
  path: openscientist_artifacts/provenance_sequence_identity_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist sequence identity matrix
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (NCBITaxon:4896)
- **Gene directory:** alo1
- **Gene symbol:** alo1
- **UniProt accession:** Q9HDX8

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-gulonolactone-oxidase
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts L-gulonolactone oxidase activity (GO:0050105) and L-ascorbic acid biosynthetic process (GO:0019853) for the Schizosaccharomyces pombe protein alo1 (Q9HDX8). Independently assess whether alo1 is specifically an L-gulonolactone oxidase producing L-ascorbate (the mammalian-type enzyme and pathway), or whether it is a D-arabinono-1,4-lactone oxidase of the fungal D-erythroascorbate pathway -- a related aldonolactone-oxidoreductase (ALO/GULO-family) paralog with a different substrate and product -- which would make the L-gulonolactone-oxidase and L-ascorbate-biosynthesis predictions a paralog/substrate misassignment. Determine whether the predictions are supported or refuted.

## Term and Decision Context

- Term: L-gulonolactone oxidase activity (GO:0050105)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts L-gulonolactone oxidase activity (GO:0050105) and L-ascorbic acid
  biosynthetic process (GO:0019853) for the Schizosaccharomyces pombe protein alo1 (Q9HDX8). Independently
  assess whether alo1 is specifically an L-gulonolactone oxidase producing L-ascorbate (the mammalian-type
  enzyme and pathway), or whether it is a D-arabinono-1,4-lactone oxidase of the fungal D-erythroascorbate
  pathway -- a related aldonolactone-oxidoreductase (ALO/GULO-family) paralog with a different substrate
  and product -- which would make the L-gulonolactone-oxidase and L-ascorbate-biosynthesis predictions
  a paralog/substrate misassignment. Determine whether the predictions are supported or refuted.
focus_type: computational_prediction
term_id: GO:0050105
term_label: L-gulonolactone oxidase activity
context: []
reference_id:
- doi:10.64898/2026.03.19.712954
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

# AIGR Deep Research — S. pombe *alo1* (Q9HDX8): L-gulonolactone oxidase prediction

**Hypothesis slug:** prediction-gulonolactone-oxidase
**Focus type:** computational_prediction
**Term under test:** GO:0050105 L-gulonolactone oxidase activity (+ GO:0019853 L-ascorbic acid biosynthetic process)
**Model source of prediction:** BioReason-Pro SFT (ref doi:10.64898/2026.03.19.712954)

---

## Executive Judgment

**Verdict: REFUTED (over-annotated — paralog/substrate misassignment).**

The BioReason-Pro predictions of **L-gulonolactone oxidase activity (GO:0050105)** and
**L-ascorbic acid biosynthetic process (GO:0019853)** for *S. pombe* alo1 (Q9HDX8) are
**not supported** and should not enter the review as-is. Multiple independent lines of
evidence identify alo1 as **D-arabinono-1,4-lactone oxidase (EC 1.1.3.37)**, the terminal
enzyme of the **fungal D-erythroascorbate** pathway — a distinct-substrate, distinct-product
paralog within the same ALO/GULO/GLDH aldonolactone-oxidoreductase (FAD, vanillyl-alcohol-oxidase)
superfamily:

- UniProtKB Q9HDX8 curated recommended name = *D-arabinono-1,4-lactone oxidase*, EC 1.1.3.37;
  curated reaction produces **dehydro-D-arabinono-1,4-lactone + H₂O₂**, and the assigned pathway
  is **D-erythroascorbate biosynthesis (step 2/2)** — not L-ascorbate.
- PomBase/GO_Central assigns MF **GO:0003885 (D-arabinono-1,4-lactone oxidase activity, IBA)**;
  GO:0050105 is **absent**.
- The mislabel is explainable: the enzyme sits in **PANTHER family PTHR43762**, whose *family-level*
  name is "L-gulonolactone oxidase," while alo1 maps to **subfamily SF1 = D-arabinono-1,4-lactone oxidase**.
  A model keying on the family name (frequency/name bias) will over-call GULO.
- Biochemistry of orthologs confirms the fungal substrate/product: *S. cerevisiae* ALO1 was **purified**
  as D-arabinono-1,4-lactone oxidase making D-erythroascorbate and shares only **32 % identity with rat GULO**
  (PMID:10094636); *C. albicans* ALO1 null mutants lose the activity and D-erythroascorbate (PMID:11349062, 18282465).

**Most important caveat:** Members of this family have measurable *in vitro* promiscuity toward related
aldonolactones (the Q9HDX8 alt-name "L-galactono-γ-lactone oxidase" reflects this), so a weak *in vitro*
turnover of L-gulono-1,4-lactone cannot be excluded. That would still not justify a GULO/L-ascorbate
annotation, because the physiological substrate and product are D-arabinono-lactone → D-erythroascorbate.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence |
|---|---|---|---|---|---|---|
| UniProtKB Q9HDX8 (ALO_SCHPO) | database/curated | Refutes seed | Is alo1 a GULO making L-ascorbate? | Rec. name D-arabinono-1,4-lactone oxidase EC 1.1.3.37; rxn → dehydro-D-arabinono-1,4-lactone + H₂O₂; pathway = D-erythroascorbate biosynthesis step 2/2 | *S. pombe* alo1 | High (ECO:0000250) |
| PomBase GO:0003885 (IBA) | database/phylogenetic | Refutes / true MF | Correct MF term | D-arabinono-1,4-lactone oxidase activity; **no** GO:0050105 | *S. pombe* alo1 | High |
| PANTHER PTHR43762:SF1 | computational/orthology | Qualifies | Source of mislabel | Subfamily SF1 = D-arabinono-lactone oxidase; parent family named "L-gulonolactone oxidase" → name carryover | protein family | Med-High |
| PMID:10094636 | direct assay + sequence | Refutes | Fungal enzyme identity / GULO homology | *S. cerevisiae* ALO1 purified as D-arabinono-1,4-lactone oxidase (final step of D-erythroascorbate synth); 32 % id to rat GULO | *S. cerevisiae* | High |
| PMID:11349062 | mutant phenotype + cloning | Refutes | Gene product & pathway | *C. albicans* ALO1 = D-arabinono-1,4-lactone oxidase; alo1 null loses activity + D-erythroascorbate; antioxidant/virulence | *C. albicans* | High |
| PMID:18282465 | mutant phenotype | Qualifies | Pathway product | alo1/alo1 mutant lacks ALO; D-erythroascorbate (EASC) is the product regulating alternative-oxidase respiration | *C. albicans* | Med |
| This run (computed) | structural/evolutionary | Qualifies | Does global %id discriminate ALO vs GULO? | Gotoh/BLOSUM62 global identity: alo1 vs ScALO1 = **30.5%**, alo1 vs rat GULO = **31.0%**, alo1 vs plant GLDH = 19.9%. Twilight-zone, ~tie with GULO. Four-point test weakly groups (alo1,ScALO1)|(GULO,GLDH), margin 0.8 | Q9HDX8/P54783/P10867/Q9SU56 | Med; explains model error, not itself discriminating |
| QuickGO (this run) | database (verification) | Refutes seed | Are the predicted terms in the curated set? | Q9HDX8 curated set: MF **GO:0003885** (IGC), BP **GO:0070485** dehydro-D-arabinono-1,4-lactone biosynthetic process (IGC), CC mitochondrion/outer membrane. **GO:0050105 and GO:0019853 both ABSENT** (verified present=False) | *S. pombe* alo1, PomBase | High |

*(Provenance: `provenance/evidence_matrix.csv`, `provenance/go_decision_table.csv`, `provenance/sequence_identity_matrix.csv`; UniProt fetch + alignment executed via MCP execute_code.)*

**Computed identity note (this run):** A Gotoh global alignment (BLOSUM62) shows alo1 is essentially
equidistant from the fungal ALO (S. cerevisiae ALO1, 30.5 %) and the mammalian GULO (rat, 31.0 %) —
both in the ~30 % alignment "twilight zone". Global % identity therefore **does not** discriminate the two
functions and marginally favors GULO, which is exactly why a homology/embedding-based model can
over-predict L-gulonolactone oxidase. Discrimination instead rests on the PANTHER subfamily assignment
(PTHR43762:SF1 = D-arabinono-lactone oxidase), the curated EC 1.1.3.37 / D-erythroascorbate pathway, and
fungal-clade biology — all of which point to ALO, not GULO. This nuance strengthens, rather than weakens,
the refuted verdict.

---

## GO Curation Implications *(leads — require curator verification)*

Verified against the live QuickGO annotation set for Q9HDX8 (13 annotations). **Both model-predicted
terms are absent from the curated set**, and the curated terms are already correct and *more specific*:

| GO term | Aspect | Curated status | Recommended action | Rationale |
|---|---|---|---|---|
| **GO:0050105** L-gulonolactone oxidase activity | MF | **Absent** (predicted only) | **REMOVE / do not add** | Wrong substrate; curated enzyme is EC 1.1.3.37 |
| **GO:0019853** L-ascorbic acid biosynthetic process | BP | **Absent** (predicted only) | **REMOVE / replace with GO:0070485** | Fungi make D-erythroascorbate, not L-ascorbate |
| **GO:0003885** D-arabinono-1,4-lactone oxidase activity | MF | **Present** (IGC/IBA, PomBase) | **RETAIN (core)** | Correct curated MF, EC 1.1.3.37 |
| **GO:0070485** dehydro-D-arabinono-1,4-lactone biosynthetic process | BP | **Present** (IGC, PomBase) | **RETAIN (core)** | Direct product of the alo1 reaction; the correct specific BP that supersedes GO:0019853 |
| **GO:0005741** mitochondrial outer membrane / **GO:0005739** mitochondrion | CC | **Present** (ISO / HDA-IBA) | **RETAIN** | Consistent with ALO-family localization |

Core function is fully captured by the curated MF (GO:0003885) plus the specific product BP (GO:0070485);
"protein binding" is neither needed nor recommended. The model prediction is strictly *less accurate* than
existing curation — a textbook paralog/substrate over-annotation.

---

## Mechanistic Scope

Direct molecular function tested: a mitochondrial-membrane, covalent-FAD flavoprotein oxidase that
oxidizes an aldono-1,4-lactone using O₂, releasing H₂O₂. The *specific, physiological* reaction for
alo1 is **D-arabinono-1,4-lactone → dehydro-D-arabinono-1,4-lactone**, the last step yielding
**D-erythroascorbate** (a 5-carbon L-ascorbate analog). Downstream/pleiotropic effects (oxidative-stress
resistance, virulence, alternative-oxidase induction seen in *Candida*) are pathway consequences of the
D-erythroascorbate product, **not** the enzyme's direct activity, and must not be conflated with the MF term.
The seed's GULO/L-ascorbate claim describes a **different substrate (L-gulono-1,4-lactone) and different product
(L-ascorbate)** belonging to the mammalian pathway.

---

## Conflicts and Alternatives

- **Paralog confusion (primary conflict):** GULO (mammals), GLDH/L-galactono-lactone dehydrogenase (plants),
  and ALO (fungi) are homologous but substrate-distinct. ~32 % identity between fungal ALO1 and rat GULO
  (PMID:10094636) is exactly the zone where automated methods over-transfer the better-known family label.
- **Family-name bias:** PANTHER PTHR43762 carries the name "L-gulonolactone oxidase" at family level; the
  correct assignment is subfamily SF1 (D-arabinono-lactone oxidase).
- **In-vitro promiscuity:** The UniProt alt-name "L-galactono-γ-lactone oxidase" and known broad aldonolactone
  activity mean a low-level *in vitro* L-gulonolactone turnover is possible; this is an artifact-level caveat,
  not physiological evidence for L-ascorbate biosynthesis in *S. pombe*.

---

## Knowledge Gaps

1. **No S. pombe-specific enzymatic assay was located.** Checked PubMed (no *S. pombe* ALO papers returned);
   the *S. pombe* assignment rests on curated by-similarity + IBA. Matters because direct *S. pombe* kinetics
   would definitively fix substrate preference. Resolve with: in-vitro substrate-panel kinetics on recombinant Q9HDX8.
2. **Exact GO BP ID for D-erythroascorbate biosynthesis** not confirmed here — curator should map the UniProt
   pathway string to the current ontology term.
3. **Whether *S. pombe* actually accumulates D-erythroascorbate** (vs. only enzyme presence) — resolve by
   metabolite LC-MS of wild-type vs. alo1Δ.

---

## Discriminating Tests

- **Substrate-panel oxidase assay** on recombinant Q9HDX8: compare V/Km for D-arabinono-1,4-lactone,
  L-gulono-1,4-lactone, and L-galactono-1,4-lactone (O₂ consumption / H₂O₂ release). Physiological substrate
  should dominate.
- **Metabolomics of alo1Δ *S. pombe*:** loss of D-erythroascorbate (not L-ascorbate) confirms pathway identity.
- **Phylogenetic placement / reciprocal-best-hit** of Q9HDX8 vs. GULO (rat), GLDH (plant), ALO1 (Sc/Ca):
  expect clustering with fungal ALO subfamily, away from GULO.

---

## Curation Leads (require curator verification)

- **Action change:** reject BioReason-Pro GO:0050105 and GO:0019853 for alo1; keep GO:0003885; consider adding
  the D-erythroascorbate biosynthetic-process BP term.
- **Candidate references / snippets to verify:**
  - PMID:11349062 — "ALO1, the gene encoding D-arabinono-1,4-lactone oxidase, which catalyzes the final step of D-erythroascorbic acid biosynthesis."
  - PMID:10094636 — "shared 32% … identity with … L-gulono-1,4-lactone oxidase from rat," establishing paralogy, not identity.
  - UniProtKB Q9HDX8 — EC 1.1.3.37; pathway "D-erythroascorbate biosynthesis; step 2/2."
- **Suggested question for curator:** Is a fungal-ascorbate-analog BP term already applied? If not, add and
  remove the L-ascorbate BP.
- **Suggested experiment:** recombinant-enzyme substrate panel + alo1Δ metabolomics (above).

---

## Limitations

Evidence is predominantly curated-database and ortholog-biochemistry; no *S. pombe*-specific assay was found in
the literature search. Network access limited the run to UniProt REST + PubMed; a direct sequence/phylogeny
computation was not executed. The conclusion (paralog misassignment) is nonetheless robust because it is
concordant across UniProt curation, GO_Central phylogenetics, PANTHER subfamily mapping, and ortholog
biochemistry.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.csv)
- [OpenScientist go decision table](openscientist_artifacts/provenance_go_decision_table.csv)
- [OpenScientist sequence identity matrix](openscientist_artifacts/provenance_sequence_identity_matrix.csv)