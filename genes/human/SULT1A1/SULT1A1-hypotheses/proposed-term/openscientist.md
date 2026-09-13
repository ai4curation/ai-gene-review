---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T01:41:21.747048'
end_time: '2026-08-31T02:11:25.150602'
duration_seconds: 1803.4
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SULT1A1
  gene_symbol: SULT1A1
  uniprot_accession: P50225
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: proposed_go_term
  hypothesis_slug: proposed-term
  hypothesis_text: SULT1A1 should be considered for GO term .
  term_context: '- Proposed term:'
  reference_context: No specific reference context supplied.
  source_file: genes/human/SULT1A1/SULT1A1-ai-review.yaml
  source_selector: proposed_new_terms[1]
  source_context_yaml: "proposed_name: thyroid hormone sulfotransferase activity\n\
    proposed_definition: 'Catalysis of the reaction: 3''-phosphoadenosine 5''-phosphosulfate\
    \ + an iodothyronine\n  = adenosine 3'',5''-bisphosphate + an iodothyronine sulfate\
    \ + H+. The sulfonate group is transferred\n  to the phenolic 4''-hydroxyl of\
    \ the outer ring of thyroid hormones and their metabolites, including\n  L-thyroxine\
    \ (T4), 3,3'',5-triiodo-L-thyronine (T3), 3,3'',5''-triiodo-L-thyronine (reverse\
    \ T3) and 3,3''-diiodo-L-thyronine.'\njustification: GO has no molecular function\
    \ term for iodothyronine sulfation, although it is a principal\n  route of thyroid\
    \ hormone inactivation and is the highest-affinity chemistry documented for SULT1A1\
    \ (Km\n  0.14 uM for 3,3'-T2, roughly 240-fold tighter than SULT1A3). UniProt\
    \ curates four distinct iodothyronine\n  RHEA reactions for it on P50225 (RHEA:67876,\
    \ RHEA:67888, RHEA:67892, RHEA:83575) with ECO:0000269 evidence,\n  and Reactome\
    \ models three of them (R-HSA-176474, R-HSA-176585). At present curators must\
    \ fall back on\n  either GO:0008146 sulfotransferase activity, which loses the\
    \ substrate entirely, or GO:0004062 aryl\n  sulfotransferase activity, which is\
    \ correct chemically but does not distinguish thyroid hormone from\n  any other\
    \ phenol. The term would also apply to SULT1A3, SULT1B1 and SULT1E1, all of which\
    \ sulfate iodothyronines.\nproposed_parent:\n  id: GO:0004062\n  label: aryl sulfotransferase\
    \ activity\nsupported_by:\n- reference_id: PMID:10199779\n  supporting_text: In\
    \ all cases, the substrate preference was 3,3'-T2 >> rT3 > T3 > T4.\n  reference_section_type:\
    \ ABSTRACT\n- reference_id: file:human/SULT1A1/SULT1A1-uniprot.txt\n  supporting_text:\
    \ Catalyzes the sulfation of T4 (L-thyroxine/3,5,3',5'-tetraiodothyronine), T3\
    \ (3,5,3'-triiodothyronine),\n    rT3 (3,3',5'-triiodothyronine) and 3,3'-T2 (3,3'-diiodothyronine),\
    \ with a substrate preference of\n    3,3'-T2 > rT3 > T3 > T4."
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
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
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
- filename: provenance_go_gap_check.json
  path: openscientist_artifacts/provenance_go_gap_check.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go gap check
- filename: provenance_paralog_iodothyronine_check.json
  path: openscientist_artifacts/provenance_paralog_iodothyronine_check.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist paralog iodothyronine check
- filename: provenance_uniprot_rhea_verification.json
  path: openscientist_artifacts/provenance_uniprot_rhea_verification.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist uniprot rhea verification
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
- **Gene directory:** SULT1A1
- **Gene symbol:** SULT1A1
- **UniProt accession:** P50225

## Focus

- **Focus type:** proposed_go_term
- **Hypothesis slug:** proposed-term
- **Source file:** genes/human/SULT1A1/SULT1A1-ai-review.yaml
- **Source selector:** proposed_new_terms[1]

## Seed Hypothesis

SULT1A1 should be considered for GO term .

## Term and Decision Context

- Proposed term:

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
proposed_name: thyroid hormone sulfotransferase activity
proposed_definition: 'Catalysis of the reaction: 3''-phosphoadenosine 5''-phosphosulfate + an iodothyronine
  = adenosine 3'',5''-bisphosphate + an iodothyronine sulfate + H+. The sulfonate group is transferred
  to the phenolic 4''-hydroxyl of the outer ring of thyroid hormones and their metabolites, including
  L-thyroxine (T4), 3,3'',5-triiodo-L-thyronine (T3), 3,3'',5''-triiodo-L-thyronine (reverse T3) and 3,3''-diiodo-L-thyronine.'
justification: GO has no molecular function term for iodothyronine sulfation, although it is a principal
  route of thyroid hormone inactivation and is the highest-affinity chemistry documented for SULT1A1 (Km
  0.14 uM for 3,3'-T2, roughly 240-fold tighter than SULT1A3). UniProt curates four distinct iodothyronine
  RHEA reactions for it on P50225 (RHEA:67876, RHEA:67888, RHEA:67892, RHEA:83575) with ECO:0000269 evidence,
  and Reactome models three of them (R-HSA-176474, R-HSA-176585). At present curators must fall back on
  either GO:0008146 sulfotransferase activity, which loses the substrate entirely, or GO:0004062 aryl
  sulfotransferase activity, which is correct chemically but does not distinguish thyroid hormone from
  any other phenol. The term would also apply to SULT1A3, SULT1B1 and SULT1E1, all of which sulfate iodothyronines.
proposed_parent:
  id: GO:0004062
  label: aryl sulfotransferase activity
supported_by:
- reference_id: PMID:10199779
  supporting_text: In all cases, the substrate preference was 3,3'-T2 >> rT3 > T3 > T4.
  reference_section_type: ABSTRACT
- reference_id: file:human/SULT1A1/SULT1A1-uniprot.txt
  supporting_text: Catalyzes the sulfation of T4 (L-thyroxine/3,5,3',5'-tetraiodothyronine), T3 (3,5,3'-triiodothyronine),
    rT3 (3,3',5'-triiodothyronine) and 3,3'-T2 (3,3'-diiodothyronine), with a substrate preference of
    3,3'-T2 > rT3 > T3 > T4.
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

# SULT1A1 — Proposed GO Term: *Thyroid Hormone (Iodothyronine) Sulfotransferase Activity*

**Gene:** SULT1A1 (Homo sapiens, NCBITaxon:9606) · **UniProt:** P50225
**Focus:** proposed_go_term — `proposed_new_terms[1]`
**Proposed term name:** thyroid hormone sulfotransferase activity
**Proposed parent:** GO:0004062 (aryl sulfotransferase activity)

---

## Summary

**Verdict: SUPPORTED.** The proposal to create a new molecular-function (MF) GO term for iodothyronine/thyroid-hormone sulfation and annotate it to SULT1A1 is biologically well-justified, fills a genuine ontology gap, and is backed by direct enzymatic evidence on the human recombinant protein and on human thyroid-gland cytosol. The chemistry — transfer of a sulfonate group from PAPS to the phenolic 4′-hydroxyl of the outer ring of iodothyronines — is documented for SULT1A1 across all four physiologically relevant substrates (T4, T3, rT3, 3,3′-T2), with a strong and reproducible substrate preference of **3,3′-T2 >> rT3 > T3 > T4** and very high affinity for 3,3′-T2 (apparent Km ≈ 0.14 µM, roughly 240-fold tighter than the paralog SULT1A3).

Three independent lines of verification support the curation decision. First, direct enzyme assays (Kester et al. 1999; Li et al. 2001; Ebmeier & Anderson 2004) establish the reaction, the substrate order, and the kinetic parameters. Second, a **live UniProt REST query** on P50225 confirmed that all four RHEA reactions cited in the seed (RHEA:67876, 67888, 67892, 83575) are curated on the entry with experimental ECO:0000269 evidence, providing ready-made cross-references for a new term. Third, a **live EBI OLS (Ontology Lookup Service) query** confirmed that GO currently has **no** molecular-function term for iodothyronine or thyroid-hormone sulfation — only broader MF terms (GO:0008146 sulfotransferase activity; GO:0004062 aryl sulfotransferase activity) and unrelated thyroid-hormone BP/binding terms exist. This confirms the gap the proposal aims to fill.

Two caveats matter for the curator, both refinements rather than objections. (1) **Term label:** because the highest-affinity, preferred substrates (3,3′-T2, rT3) are inactive thyroid-hormone *metabolites* rather than the active hormones T3/T4, the more chemically neutral label **"iodothyronine sulfotransferase activity"** is preferable to "thyroid hormone sulfotransferase activity," though either is defensible given the shared reaction chemistry. (2) **Generic applicability / paralog scope:** the seed states the term should also apply to SULT1A3, SULT1B1, and SULT1E1. Live UniProt curation confirms curated iodothyronine reactions for SULT1A3 and SULT1B1 but **not** for SULT1E1, so SULT1E1's inclusion should be verified against primary literature before being carried into annotations.

---

## Key Findings

### Finding 1 — SULT1A1 directly sulfates iodothyronines with high affinity, and no existing GO MF term covers this activity

The foundational evidence comes from direct enzyme assays with recombinant human SULT1A1. Kester et al. (1999) [PMID: 10199779](https://pubmed.ncbi.nlm.nih.gov/10199779/) characterized human iodothyronine sulfotransferases and reported that "**In all cases, the substrate preference was 3,3′-T2 >> rT3 > T3 > T4**." This single ordering establishes that SULT1A1 acts on the full panel of physiologically relevant iodothyronines — the inactive metabolite 3,3′-diiodothyronine (3,3′-T2), reverse T3 (rT3), the active hormone T3, and the prohormone T4 — and that the enzyme strongly prefers the smaller, outer-ring diiodo/triiodo species.

The affinity difference relative to the paralog SULT1A3 is large and directly supports the seed's "highest-affinity chemistry" claim. Kester et al. reported apparent Km values of "**0.14 and 29.1 micromol/L for SULT1A1, and 33 and 112 micromol/L for SULT1A3**," i.e., Km(3,3′-T2) = 0.14 µM and Km(T3) = 29.1 µM for SULT1A1, versus 33 µM (3,3′-T2) for SULT1A3 — a roughly **240-fold tighter** binding of 3,3′-T2 by SULT1A1. This is exactly the quantitative claim used in the seed justification.

The substrate preference is not a single-study artifact. Li et al. (2001) [PMID: 11739018](https://pubmed.ncbi.nlm.nih.gov/11739018/) independently reproduced the ordering across SULT1A1 allozymes, reporting that "**the preferences of these SULT1A1 allozymes for iodothyronine substrates were the same (3,3′-diiodothyronine (3,3′-T2) > 3′,5′,3-triiodothyronine (rT3) > T3 > thyroxine (T4) >> 3,5-diiodothyronine (3,5-T2))**." The extended ordering adds that 3,5-T2 (an inner-ring diiodothyronine) is a very poor substrate, consistent with the reaction being specific to the **outer-ring (4′) phenolic hydroxyl** — the exact regiochemistry stated in the proposed definition. The finding is also independent of the common Arg213His polymorphism, i.e., the *identity* of the function is preserved across allozymes even though catalytic activity levels vary.

Human tissue evidence complements the recombinant data. Ebmeier & Anderson (2004) [PMID: 15531517](https://pubmed.ncbi.nlm.nih.gov/15531517/) identified SULT1A1 and SULT1A3 activities in normal and diseased human thyroid glands and found that "**Only 3,3′-diiodothyronine (3,3′-T2) and the phytoestrogen daidzein served as substrates for the normal thyroid SULT activities**," and that "**The preference of thyroid gland SULT activities for 3,3′-T2 suggests that sulfation may enhance degradation of intrathyroidal 3,3′-T2 for iodide reutilization**." This places the activity in a physiological human tissue context and ties it to a plausible biological process (intrathyroidal thyroid-hormone processing / iodide reutilization). The same study noted both SULT activities were significantly elevated in autoimmune thyroid disease glands.

Finally, the ontology gap is real. A live query of the EBI Ontology Lookup Service returned **0 hits** for "iodothyronine sulfotransferase" and "thyroid hormone sulfotransferase" as GO molecular functions. The relevant thyroid-hormone GO terms that do exist are biological-process or binding terms (GO:0042404 thyroid hormone catabolic process; GO:0042403 thyroid hormone metabolic process; GO:0070324 thyroid hormone binding), none of which capture the sulfotransferase chemistry. The nearest existing MF terms are the generic GO:0008146 (sulfotransferase activity) and the proposed parent GO:0004062 (aryl sulfotransferase activity). Both are correct but lose the substrate identity — precisely the curation limitation the proposal seeks to remedy.

### Finding 2 — All four cited iodothyronine RHEA reactions are curated on UniProt P50225 with experimental evidence

A live UniProt REST query (`rest.uniprot.org/uniprotkb/P50225.json`) returned 10 CATALYTIC ACTIVITY comments for SULT1A1. Four of them are iodothyronine sulfations, each carrying experimental **ECO:0000269** evidence, and each matching a seed-cited RHEA identifier exactly:

| RHEA ID | Substrate | Reaction (abbreviated) | Evidence |
|---|---|---|---|
| RHEA:67876 | T3 (3,3′,5-triiodo-L-thyronine) | T3 + PAPS = T3 sulfate + PAP + H⁺ | ECO:0000269 |
| RHEA:67888 | rT3 (3,3′,5′-triiodo-L-thyronine) | rT3 + PAPS = rT3 sulfate + PAP + H⁺ | ECO:0000269 |
| RHEA:67892 | 3,3′-T2 (3,3′-diiodo-L-thyronine) | 3,3′-T2 + PAPS = 3,3′-T2 sulfate + PAP + H⁺ | ECO:0000269 |
| RHEA:83575 | T4 (L-thyroxine) | T4 + PAPS = T4 sulfate + PAP + H⁺ | ECO:0000269 |

None of the four cited RHEA IDs was missing or mis-cited. The generic reaction RHEA:12164 ("a phenol + PAPS = an aryl sulfate + PAP + H⁺") is also present on the entry and corresponds to the proposed parent GO:0004062 (aryl sulfotransferase activity). This means a new child MF term can be defined against a single unified iodothyronine reaction (as written in the proposed definition, which uses the generic "an iodothyronine" substrate class) while the four specific RHEA reactions serve as the underlying experimentally verified xrefs. The alignment between the proposed definition, the RHEA reactions, and the ECO:0000269 evidence is exact — an unusually clean case for term creation. (Note: RHEA-DB's own API returned a Cloudflare 403 during the run, so the equations were confirmed via the UniProt entry rather than directly against RHEA.)

### Finding 3 — The proposed term is appropriately generic across paralogs, but SULT1E1's inclusion is unverified

The seed argues the new term would "also apply to SULT1A3, SULT1B1 and SULT1E1, all of which sulfate iodothyronines," making the term suitably generic rather than SULT1A1-specific. Live UniProt REST queries partially confirm this:

| Paralog | UniProt | Curated iodothyronine CATALYTIC ACTIVITY reactions | Supports generic term? |
|---|---|---|---|
| SULT1A1 | P50225 | 4 (T3, rT3, 3,3′-T2, T4) | Yes — primary target |
| SULT1A3 | P0DMM9 | 4 (T3, rT3, 3,3′-T2, T4) | Yes |
| SULT1B1 | O43704 | 3 (T3, rT3, 3,3′-T2) | Yes |
| SULT1E1 | P49888 | 0 curated iodothyronine reactions | **Not on UniProt** |

Thus the claim that the term is generic and reusable across the SULT1 family is supported for SULT1A1, SULT1A3, and SULT1B1. SULT1E1, however, carries **no curated iodothyronine catalytic-activity reaction** on its UniProt entry. Iodothyronine sulfation by SULT1E1 is reported in some literature, but it is not reflected in the curated catalytic-activity block, so any downstream annotation of SULT1E1 to the new term should be substantiated from primary experimental data rather than assumed. This does not weaken the SULT1A1 proposal; it is a scoping note for how broadly the term is propagated. Note also that SULT1A3, while sharing the function, acts at much lower affinity (Km(3,3′-T2) ≈ 33 µM vs 0.14 µM for SULT1A1) — a feature of a shared, generic activity term, not evidence of paralog over-annotation.

---

## Mechanistic Model / Interpretation

The molecular function under evaluation is a **sulfotransferase (sulfonation) reaction** in which SULT1A1 transfers the sulfonate group of the universal donor **3′-phosphoadenosine 5′-phosphosulfate (PAPS)** to the **phenolic 4′-hydroxyl on the outer (phenolic) ring** of an iodothyronine, producing an iodothyronine sulfate, PAP (adenosine 3′,5′-bisphosphate), and a proton.

```
                         SULT1A1
   Iodothyronine  +  PAPS  ───────►  Iodothyronine-4'-O-sulfate  +  PAP  +  H+
   (T4/T3/rT3/3,3'-T2)                (inactivated / D1-primed metabolite)

   Substrate preference (Km, affinity):
        3,3'-T2   >>   rT3   >   T3   >   T4   >>   3,5-T2
        (0.14 µM)                (29 µM)
        highest affinity                          poor / inner-ring
```

Biologically, outer-ring (4′-O) sulfation is a **principal route of thyroid-hormone inactivation**. Sulfation of T3 blocks its receptor binding and accelerates inner-ring deiodination by type I deiodinase (D1), routing hormone toward irreversible degradation and, in the thyroid gland, toward iodide reutilization (the interpretation offered by Ebmeier & Anderson 2004). The enzyme's strong preference for 3,3′-T2 and rT3 — both inactive metabolites — over the active hormone T3 and the prohormone T4 indicates that the physiological "hot spot" of this chemistry is the terminal clearance of already-partially-degraded iodothyronines, not the direct regulation of active T3 levels. This is why the neutral substrate-class label ("iodothyronine") is mechanistically more accurate than "thyroid hormone," even though the reaction chemistry is identical across the panel.

At the ontology level, the correct placement is a new **MF** term as a **child of GO:0004062 (aryl sulfotransferase activity)**, because iodothyronines are aryl (phenolic) substrates and the reaction is regiospecific for the phenolic hydroxyl. The generic parent (GO:0008146) is too coarse; GO:0004062 is chemically correct but cannot distinguish thyroid hormones from any other phenol, which is the resolution loss the proposal targets. The associated biological process is already captured by the existing GO:0042404 (thyroid hormone catabolic process) / GO:0042403 (thyroid hormone metabolic process), so the new term is specifically an MF gap, not a BP gap.

```
GO:0008146  sulfotransferase activity
     └── GO:0004062  aryl sulfotransferase activity   ← proposed parent
             └── [NEW]  iodothyronine sulfotransferase activity   ← proposed term
                        xref: RHEA:67876 / 67888 / 67892 / 83575
                        annotate to: SULT1A1 (P50225), SULT1A3, SULT1B1
```

---

## Evidence Base

### Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 10199779](https://pubmed.ncbi.nlm.nih.gov/10199779/) (Kester et al. 1999) | Direct enzyme assay | **Supports** | SULT1A1 sulfates iodothyronines; substrate order & affinity | Preference 3,3′-T2 >> rT3 > T3 > T4; Km(3,3′-T2)=0.14 µM vs 33 µM for SULT1A3 (~240×); Km(T3)=29.1 µM | Recombinant human SULT1A1/1A3; human liver/kidney cytosol | High; in-vitro recombinant kinetics; foundational paper |
| [PMID: 11739018](https://pubmed.ncbi.nlm.nih.gov/11739018/) (Li et al. 2001) | Direct enzyme assay | **Supports** | Reproducibility of substrate order across allozymes | 3,3′-T2 > rT3 > T3 > T4 >> 3,5-T2; identical across allozymes | Human SULT1A1 allozymes, T3 substrate | High; confirms outer-ring specificity (3,5-T2 poor), independent of Arg213His |
| [PMID: 15531517](https://pubmed.ncbi.nlm.nih.gov/15531517/) (Ebmeier & Anderson 2004) | Direct assay in human tissue | **Supports / qualifies** | Activity present in native human tissue; physiological role | Only 3,3′-T2 (and daidzein) served as substrates; sulfation tied to intrathyroidal iodide reutilization; ↑ in autoimmune thyroid disease | Human thyroid gland cytosol (normal/diseased, n=86) | High for tissue presence; qualifies term as physiologically real |
| [PMID: 9848125](https://pubmed.ncbi.nlm.nih.gov/9848125/) (Schuur et al. 1998) | Direct assay / inhibition kinetics | **Supports / qualifies** | hSULT1A1 catalyzes T2 sulfation; distinct from SULT1A3 | hSULT1A1 T2 sulfation inhibited by PCB-OHs (competitive), SULT1A3 not; T2 preferred iodothyronine substrate | Recombinant hSULT1A1 vs hSULT1A3, rat isozymes | Medium-high; confirms activity and isozyme specificity; flags endocrine-disruptor inhibition |
| UniProt P50225 (live REST query) | Database record | **Supports** | Four cited RHEA reactions curated with experimental evidence | RHEA:67876/67888/67892/83575 all present, ECO:0000269 | Curated entry | High; direct programmatic verification |
| UniProt P0DMM9 / O43704 / P49888 (live REST) | Database record | **Qualifies** | Generic term applicability across paralogs | SULT1A3 (4) and SULT1B1 (3) carry iodothyronine reactions; SULT1E1 (0) | Curated entries | High; SULT1E1 gap flagged |
| EBI OLS (live GO query) | Database/ontology | **Supports** | GO lacks any MF term for iodothyronine sulfation | 0 hits; only BP/binding thyroid terms + generic MF parents exist | GO ontology, Aug 2026 | High; confirms the gap; label search may miss synonyms |

### Narrative synthesis of the literature

- **[PMID: 10199779](https://pubmed.ncbi.nlm.nih.gov/10199779/)** is the anchor paper. It directly measured SULT1A1 and SULT1A3 iodothyronine sulfation, giving both the substrate-preference order and the Km values that appear verbatim in the seed justification. It is the strongest single piece of evidence and supports term creation.
- **[PMID: 11739018](https://pubmed.ncbi.nlm.nih.gov/11739018/)** independently reproduces the order across allozymes and extends it to 3,5-T2, confirming outer-ring regiospecificity and that the function's identity is preserved across the common Arg213His polymorphism. It reduces the risk that the preference is a one-lab artifact.
- **[PMID: 15531517](https://pubmed.ncbi.nlm.nih.gov/15531517/)** moves the activity from recombinant protein into native human thyroid cytosol and offers the physiological interpretation (iodide reutilization), strengthening the biological relevance of an MF term rather than an in-vitro curiosity.
- **[PMID: 9848125](https://pubmed.ncbi.nlm.nih.gov/9848125/)** confirms hSULT1A1 catalyzes iodothyronine (T2) sulfation and clearly distinguishes it from SULT1A3 (different inhibitor sensitivity), reinforcing paralog-specific behavior — relevant to how the generic term is later propagated.

---

## GO Curation Implications

**Likely curation action (lead requiring curator verification):** Create a new **molecular-function** term — recommended primary label **"iodothyronine sulfotransferase activity"** (with "thyroid hormone sulfotransferase activity" as an exact synonym) — as a **child of GO:0004062 (aryl sulfotransferase activity)**, defined by the reaction "PAPS + an iodothyronine = PAP + an iodothyronine sulfate + H⁺" with 4′-outer-ring regiospecificity, and cross-referenced to RHEA:67876, 67888, 67892, and 83575. Then annotate SULT1A1 (P50225) to this term with an experimental evidence code (IDA/EXP, ECO:0000269), citing PMID:10199779 (and PMID:11739018 / PMID:15531517 as supporting).

- **Term type:** MF (not BP or CC). The associated BP is already covered by GO:0042404 / GO:0042403.
- **Retain / replace:** This is an *addition*, not a replacement. It should not delete the existing GO:0004062 or GO:0008146 annotations, but it makes them more specific for SULT1A1. The new child term replaces the less-informative fallbacks in practice (GO:0008146 loses the substrate; GO:0004062 cannot distinguish thyroid hormones from other phenols).
- **Specificity level:** Appropriately specific — not too broad (GO:0004062 is the too-broad option) and not too narrow (it uses the generic "iodothyronine" class rather than a single hormone, so one term covers T4/T3/rT3/3,3′-T2).
- **Definition:** the supplied PAPS→PAP reaction definition is chemically correct; keep the enumerated substrate list (T4, T3, rT3, 3,3′-T2) as examples, not as an exhaustive/required set.
- **Label recommendation:** Prefer "iodothyronine" over "thyroid hormone" in the primary label because the highest-affinity substrates are inactive metabolites. Soft recommendation; both are chemically defensible.
- **Do not restrict to SULT1A1:** The term should be reusable for SULT1A3 and SULT1B1 (verified); verify SULT1E1 before propagating.
- **Avoid "protein binding":** Not applicable here — a specific catalytic MF term is fully supported by direct assay evidence.

---

## Mechanistic Scope

The hypothesis concerns an **immediate, direct molecular-function activity** of the SULT1A1 gene product: PAPS-dependent transfer of a sulfonate group to the outer-ring phenolic hydroxyl of iodothyronines. This is a bona fide catalytic activity measured directly on the recombinant enzyme and in native tissue cytosol — not a downstream phenotype, developmental outcome, or loss-of-function inference.

- **Direct gene-product activity (what the term captures):** the enzyme–substrate–product relationship (iodothyronine + PAPS → iodothyronine sulfate + PAP + H⁺), the substrate ordering, and the kinetic constants. This is a cytosolic, single-enzyme catalytic step.
- **Immediate consequence (rationale for importance, not the MF itself):** sulfated iodothyronines (T3S, T2S) are preferred substrates of type-I deiodinase, accelerating irreversible hormone degradation — i.e., thyroid-hormone inactivation/catabolism.
- **Downstream / out-of-scope for this MF term:** systemic thyroid status, developmental effects, disease associations, and drug/xenobiotic-metabolism phenotypes. These belong to BP/phenotype annotations, not the MF.

---

## Conflicts and Alternatives

1. **Paralog scope (SULT1E1).** The seed lists SULT1E1 among enzymes to which the term applies, but UniProt curation shows no iodothyronine catalytic-activity reactions for SULT1E1 (P49888). This is the single concrete discrepancy found. It does not affect the SULT1A1 annotation but should be resolved before propagating the term to SULT1E1.
2. **Label semantics ("thyroid hormone" vs "iodothyronine").** The enzyme's kinetic preference is inverted relative to hormonal potency: it most avidly sulfates the *inactive* metabolites (3,3′-T2, rT3) and least avidly the active/prohormone species (T3, T4). Calling the activity "thyroid hormone sulfotransferase" is not wrong, but "iodothyronine" better reflects the biochemistry.
3. **In-vitro provenance (partly mitigated).** Kester (1999) and Li (2001) are recombinant/in-vitro. However, Ebmeier & Anderson (2004) demonstrate the activity in native human thyroid cytosol, and UniProt curates the reactions with ECO:0000269 experimental evidence, so the activity is not an in-vitro artifact.
4. **Database carry-over risk.** UniProt/Reactome/RHEA already model these reactions; the new GO term should be cross-referenced (xref to RHEA) rather than created in isolation, to avoid divergence.
5. **No refuting evidence found.** No study in the reviewed literature contradicts SULT1A1's ability to sulfate iodothyronines or the substrate ordering. The evidence is internally consistent across three independent assay studies plus an inhibition study.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| SULT1E1 iodothyronine activity | UniProt P49888 catalytic-activity block — 0 iodothyronine reactions | Seed proposes term applies to SULT1E1; propagating without evidence risks over-annotation | Primary-literature kinetic assays for SULT1E1 on T2/rT3/T3/T4 |
| Preferred term label | Substrate-affinity ordering vs hormonal activity | Label choice affects downstream interpretation and synonymy | GO editorial decision; recommend "iodothyronine sulfotransferase activity" primary + synonym |
| Exact GO synonym coverage | OLS label search (0 MF hits) | A hidden synonym/obsolete term could duplicate the request | Curator search in GO editorial tools (Protégé/Noctua) for RHEA xrefs and "sulfo*" MF children |
| RHEA ID validity | **RESOLVED:** live UniProt query confirmed all four RHEA IDs with ECO:0000269 | New GO term should xref the correct RHEA reactions | Done — RHEA:67876/67888/67892/83575 are the ready-made xrefs |
| In-vivo physiological flux | Only in-vitro kinetics + tissue cytosol assays found | Confirms core vs minor physiological role (not required for MF term) | Human hepatocyte/thyroid flux or KO/variant studies of iodothyronine-sulfate output |
| Isoform/allozyme effects | PMID:11739018 shows *1 > *2 with T3 | Arg213His modulates activity level, not function identity | Sufficient for MF term; relevant only for phenotype annotation |

---

## Proposed Follow-up Experiments / Actions

Concrete, actionable next steps for a curator or bench scientist:

1. **Resolve SULT1E1 scope (highest priority for curation).** Query primary literature for SULT1E1 iodothyronine kinetics; if positive, propose a UniProt catalytic-activity update and only then annotate SULT1E1. If absent, restrict the initial annotation set to SULT1A1, SULT1A3, and SULT1B1.
2. **Draft the GO term with RHEA anchoring.** Submit a new-term request to GO/RHEA using the generic reaction (PAPS + iodothyronine → iodothyronine sulfate + PAP + H⁺), citing the four experimentally verified RHEA reactions and PMID:10199779 as the primary reference.
3. **Set the primary label and synonyms.** Recommend "iodothyronine sulfotransferase activity" (primary) with "thyroid hormone sulfotransferase activity" (exact synonym), parent GO:0004062.
4. **Annotate SULT1A1 with experimental evidence.** Attach the new MF term to P50225 with IDA/EXP (ECO:0000269) evidence from PMID:10199779 (order + Km), supported by PMID:11739018 (allozyme reproducibility) and PMID:15531517 (native tissue).
5. **Synonym/obsolete-term audit** in the GO editorial database to rule out an existing MF term before submission.
6. **Cross-check other SULT-family members and orthologs** (e.g., rodent Sult1c1, which sulfates iodothyronines per PMID:9848125) to define the correct taxonomic breadth for the term before broad propagation.
7. **Optional in-vivo confirmation (if core status is challenged):** measure iodothyronine-sulfate production in human hepatocytes ± SULT1A1 inhibition to confirm physiological contribution.

---

## Conclusion

The proposed molecular-function term for iodothyronine/thyroid-hormone sulfation is **biologically supported, appropriately specific, and fills a documented GO gap**. Direct recombinant and human-tissue assays establish that SULT1A1 sulfates the outer-ring 4′-hydroxyl of iodothyronines with the order 3,3′-T2 >> rT3 > T3 > T4 and very high affinity for 3,3′-T2 (Km ≈ 0.14 µM, ~240× tighter than SULT1A3). Live UniProt and OLS queries independently confirm the four cited RHEA reactions (with ECO:0000269 evidence) and the absence of any existing MF term. The two refinements for the curator are (i) prefer the "iodothyronine sulfotransferase activity" label and (ii) verify SULT1E1 before propagating the term to it. The proposal should proceed as a new MF child of GO:0004062 annotated to SULT1A1.

---

*Provenance:* This analysis rests on the supplied source-context YAML, four direct-assay primary-literature PMIDs (10199779, 11739018, 15531517, 9848125), a live EBI OLS GO query (confirming term absence), and live UniProt REST queries on P50225/P0DMM9/O43704/P49888 (confirming all four cited RHEA reactions with ECO:0000269 and characterizing paralog scope). RHEA-DB's own API returned a Cloudflare 403, so equations were confirmed via UniProt. Kinetic evidence is in-vitro/recombinant, consistent with an MF (activity) term. Artifacts: `provenance/go_gap_check.json`, `provenance/evidence_matrix.csv`, `provenance/uniprot_rhea_verification.json`.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.csv)
- [OpenScientist go gap check](openscientist_artifacts/provenance_go_gap_check.json)
- [OpenScientist paralog iodothyronine check](openscientist_artifacts/provenance_paralog_iodothyronine_check.json)
- [OpenScientist uniprot rhea verification](openscientist_artifacts/provenance_uniprot_rhea_verification.json)