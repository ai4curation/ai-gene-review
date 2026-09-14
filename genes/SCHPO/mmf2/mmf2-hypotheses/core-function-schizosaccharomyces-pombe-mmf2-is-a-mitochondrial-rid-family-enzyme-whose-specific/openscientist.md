---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T11:17:36.317696'
end_time: '2026-08-31T11:34:12.272925'
duration_seconds: 995.96
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: mmf2
  gene_symbol: mmf2
  uniprot_accession: Q9UR06
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: core_function
  hypothesis_slug: core-function-schizosaccharomyces-pombe-mmf2-is-a-mitochondrial-rid-family-enzyme-whose-specific
  hypothesis_text: Schizosaccharomyces pombe mmf2 is a mitochondrial Rid-family enzyme
    whose specific molecular function is 2-iminobutanoate/2-iminopropanoate (including
    2-aminoacrylate) deaminase activity, GO:0120241, rather than only generic deaminase
    activity
  term_context: '- Distinguish direct evidence on Q9UR06/SPAC1039.10 from evidence
    on Saccharomyces cerevisiae Mmf1p, Hmf1p, bacterial RidA, RutC, or other Rid subfamilies.

    - Evaluate the significance of PANTHER PTHR11803:SF58 PROTEIN HMF1-RELATED and
    UniProt RutC-family wording, and explicitly assess paralog/subfamily substrate
    specificity.'
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/mmf2/mmf2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe mmf2 is a mitochondrial\
    \ Rid-family enzyme whose specific molecular\n  function is 2-iminobutanoate/2-iminopropanoate\
    \ (including 2-aminoacrylate) deaminase activity, GO:0120241,\n  rather than only\
    \ generic deaminase activity\nfocus_type: core_function\ncontext:\n- Distinguish\
    \ direct evidence on Q9UR06/SPAC1039.10 from evidence on Saccharomyces cerevisiae\
    \ Mmf1p, Hmf1p,\n  bacterial RidA, RutC, or other Rid subfamilies.\n- Evaluate\
    \ the significance of PANTHER PTHR11803:SF58 PROTEIN HMF1-RELATED and UniProt\
    \ RutC-family wording,\n  and explicitly assess paralog/subfamily substrate specificity.\n\
    reference_id: []"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 9
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: artifacts_mmf2_catalytic_arg_conservation.csv
  path: openscientist_artifacts/artifacts_mmf2_catalytic_arg_conservation.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mmf2 catalytic arg conservation
- filename: artifacts_mmf2_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_mmf2_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mmf2 evidence matrix
- filename: artifacts_mmf2_go_decision_table.csv
  path: openscientist_artifacts/artifacts_mmf2_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mmf2 go decision table
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** mmf2
- **Gene symbol:** mmf2
- **UniProt accession:** Q9UR06

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-schizosaccharomyces-pombe-mmf2-is-a-mitochondrial-rid-family-enzyme-whose-specific
- **Source file:** genes/SCHPO/mmf2/mmf2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe mmf2 is a mitochondrial Rid-family enzyme whose specific molecular function is 2-iminobutanoate/2-iminopropanoate (including 2-aminoacrylate) deaminase activity, GO:0120241, rather than only generic deaminase activity

## Term and Decision Context

- Distinguish direct evidence on Q9UR06/SPAC1039.10 from evidence on Saccharomyces cerevisiae Mmf1p, Hmf1p, bacterial RidA, RutC, or other Rid subfamilies.
- Evaluate the significance of PANTHER PTHR11803:SF58 PROTEIN HMF1-RELATED and UniProt RutC-family wording, and explicitly assess paralog/subfamily substrate specificity.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe mmf2 is a mitochondrial Rid-family enzyme whose specific molecular
  function is 2-iminobutanoate/2-iminopropanoate (including 2-aminoacrylate) deaminase activity, GO:0120241,
  rather than only generic deaminase activity
focus_type: core_function
context:
- Distinguish direct evidence on Q9UR06/SPAC1039.10 from evidence on Saccharomyces cerevisiae Mmf1p, Hmf1p,
  bacterial RidA, RutC, or other Rid subfamilies.
- Evaluate the significance of PANTHER PTHR11803:SF58 PROTEIN HMF1-RELATED and UniProt RutC-family wording,
  and explicitly assess paralog/subfamily substrate specificity.
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

# AIGR Gene Hypothesis Deep Research — Final Report

## Target: *Schizosaccharomyces pombe* mmf2 (Q9UR06 / SPAC1039.10)

**Seed hypothesis:** *S. pombe* mmf2 is a mitochondrial Rid-family enzyme whose specific molecular function is 2-iminobutanoate/2-iminopropanoate (including 2-aminoacrylate) deaminase activity (**GO:0120241**), rather than only generic deaminase activity (**GO:0019239**).

**Focus type:** core_function

---

## Summary

The seed hypothesis is **supported** on homology and active-site grounds. *S. pombe* mmf2 (Q9UR06, 126 aa) carries every diagnostic feature of a catalytically active RidA-subfamily imine deaminase: it is assigned InterPro IPR006056 (RidA) and IPR006175 (YjgF/YER057c/UK114), Pfam PF01042 (Ribonuc_L-PSP), and PANTHER PTHR11803 — a family whose canonical name is literally "2-iminobutanoate/2-iminopropanoate deaminase RidA." UniProt's "RutC family" wording is legacy nomenclature for this same YjgF/RidA fold, not evidence of a distinct RutC subfamily activity. A global BLOSUM62 alignment computed in this investigation places mmf2 Arg101 exactly on the *E. coli* RidA catalytic Arg105 — the invariant residue essential for imine hydrolysis that is present only in the active RidA/Rid1–Rid3 subfamilies (absent in the inactive Rid4–Rid7 subfamilies). mmf2 is therefore in the active branch.

The closest characterized ortholog, *S. cerevisiae* Mmf1p (same PANTHER subfamily PTHR11803:SF58 "HMF1-RELATED"), is a directly demonstrated mitochondrial 2-aminoacrylate/enamine–imine deaminase. Independently, the human ortholog HRSP12/UK114 (P52758) is already annotated with the two children of GO:0120241 (GO:0120242 via TAS:Reactome; GO:0120243 via IEA:RHEA), establishing that the GO consortium already treats the specific deaminase terms — not the generic GO:0019239 — as the appropriate molecular function for this family. Taken together, GO:0120241 is a better-justified core molecular function for mmf2 than the current generic GO:0019239.

The single most important caveat is that **no direct enzymatic assay exists for Q9UR06/SPAC1039.10 itself** — the assignment rests on family membership plus active-site conservation plus ortholog data. The correct evidence code for adding GO:0120241 is therefore **ISS/ISO** (with/from Mmf1p P40185 and/or human HRSP12 P52758), not an experimental code. Additionally, "mitochondrial DNA maintenance" and related growth/heme phenotypes observed in yeast orthologs are **downstream biological-process consequences** of the deaminase activity, not the core molecular function, and should be flagged as non-core.

---

## Key Findings

### Finding 1 — mmf2 is a RidA-subfamily enzyme retaining the catalytic arginine; its specific MF is GO:0120241

Q9UR06 is a 126-amino-acid protein annotated by UniProt with InterPro IPR006056 (RidA) and IPR006175 (YjgF/YER057c/UK114), Pfam PF01042 (Ribonuc_L-PSP), and PANTHER PTHR11803, named "2-iminobutanoate/2-iminopropanoate deaminase RidA" (subfamily PTHR11803:SF58, "PROTEIN HMF1-RELATED"). This domain architecture is the defining molecular signature of the Rid superfamily.

Membership in the *catalytically active* branch of the family is established not by domain assignment alone but by the presence of a conserved active-site arginine. Niehaus et al. ([PMID: 25975565](https://pubmed.ncbi.nlm.nih.gov/25975565/)) established the diagnostic criterion: "**The Rid1 to Rid3 subfamilies, but not the Rid4 to Rid7 subfamilies, have a conserved arginine residue that, in RidA proteins, is essential for imine-hydrolyzing activity.**" A BLOSUM62 global alignment computed in this investigation places mmf2 Arg101 aligning exactly to *E. coli* RidA catalytic Arg105, placing mmf2 firmly in the active RidA branch rather than a degenerate subfamily.

The mechanistic activity underlying GO:0120241 is well defined. Lambrecht et al. ([PMID: 22094463](https://pubmed.ncbi.nlm.nih.gov/22094463/)) demonstrated that "**YjgF proteins have enamine/imine deaminase activity and accelerate the release of ammonia from reactive enamine/imine intermediates of the pyridoxal 5'-phosphate-dependent threonine dehydratase (IlvA).**" This is exactly the reaction described by GO:0120241.

The closest characterized ortholog, *S. cerevisiae* Mmf1p, is a mitochondrial member of this family: "**The mitochondrial RidA homolog, Mmf1p, prevents enamine/imine stress and is important for normal growth and maintenance of mitochondrial DNA**" ([PMID: 34559917](https://pubmed.ncbi.nlm.nih.gov/34559917/)). This confirms both the mitochondrial localization and the enamine/imine deaminase activity of the closest ortholog, and frames mtDNA maintenance as a *downstream* consequence of the deaminase activity rather than the core function.

Pairwise identity of mmf2 to characterized RidA-family members is in the expected homolog range (~30–43%): Hmf1p ≈43%, Mmf1p ≈34–42%, *E. coli* RidA ≈30–37%, human UK114/HRSP12 ≈34–49%. The current UniProt/PomBase GO MF for mmf2 is only the generic **GO:0019239 (deaminase activity, IBA)**, which is less informative than the family-defining specific term.

### Finding 2 — GO:0120241 is the family-defining MF for the RidA/PTHR11803 group; the human ortholog is already annotated with its children, and *S. pombe* has two RidA paralogs (mmf1, mmf2)

QuickGO defines **GO:0120241** as "Catalyzes the hydrolytic deamination of imine intermediates formed by several types of pyridoxal-5'-phosphate-dependent dehydratases, such as EC 4.3.1.19 and EC 4.3.1.17" — i.e., exactly the RidA activity. It has two children: **GO:0120242** (2-iminobutanoate → 2-oxobutanoate) and **GO:0120243** (2-iminopropanoate → pyruvate).

The human ortholog **HRSP12/UK114 (P52758)** is already annotated with these specific child terms: GO:0120242 (TAS:Reactome) and GO:0120243 (IEA:RHEA). This is a strong term precedent — the GO consortium already treats the specific deaminase terms, not the generic GO:0019239, as the appropriate molecular function for this family.

A UniProt taxonomy search (taxid 284812, InterPro IPR006175) returns exactly two RidA-type paralogs in *S. pombe*: **mmf1 (O43003, 162 aa)** and **mmf2 (Q9UR06, 126 aa)**. Both are PANTHER PTHR11803:SF58 "HMF1-RELATED," both are annotated "RutC family," both localize to mitochondrion + cytosol, and both currently carry only generic GO:0019239. (Note: mug71/Q9USQ7 shares the fold reference but is a diphthine-ammonia ligase — an unrelated activity — and should not be conflated with the RidA paralogs.)

### Finding 3 — The catalytic arginine (E. coli RidA Arg105 equivalent) is conserved in mmf2 and every RidA homolog tested

A global Needleman–Wunsch alignment (BLOSUM62, gap = −6) of each candidate protein against *E. coli* RidA (P0AF93), mapping to reference position 105, gave the following results:

| Protein | Accession | Length | Residue at RidA-105 position | % identity to E. coli RidA |
|---|---|---|---|---|
| **mmf2 (S. pombe)** | **Q9UR06** | **126 aa** | **Arg (R)** | **36.9%** |
| mmf1 (S. pombe) | O43003 | 162 aa | Arg (R) | 41.9% |
| Mmf1p (S. cerevisiae) | P40185 | — | Arg (R) | 41.6% |
| Hmf1p (S. cerevisiae) | P40037 | — | Arg (R) | 42.4% |
| HRSP12/UK114 (human) | P52758 | — | Arg (R) | 48.8% |
| YabJ (Bacillus) | P37552 | — | Arg (R) | 52.4% |

The essential catalytic arginine — "**a conserved arginine residue that, in RidA proteins, is essential for imine-hydrolyzing activity**" ([PMID: 25975565](https://pubmed.ncbi.nlm.nih.gov/25975565/)) — is present in mmf2 and in every homolog tested, including both *S. pombe* paralogs. This confirms catalytic competence at the sequence level: both fission-yeast paralogs are in the catalytically active RidA branch, not a degenerate Rid4–7 subfamily. Computed provenance is preserved in `artifacts/mmf2_catalytic_arg_conservation.csv`.

---

## Mechanistic Model / Interpretation

The Rid/RidA reaction and mmf2's place in it:

```
   PLP-dependent dehydratases
   ├─ Threonine dehydratase (IlvA, EC 4.3.1.19)  ── Thr/Ile pathway
   └─ Serine/cysteine dehydratase (EC 4.3.1.17)  ── Ser/Cys pathway
              │  (α,β-elimination)
              ▼
   2-iminobutanoate  /  2-iminopropanoate (= 2-aminoacrylate, 2AA)
              │        ← reactive enamine/imine; METABOLIC STRESSOR
              │           (covalently inactivates PLP enzymes)
              │
              │   RidA-family deaminase  ◄── mmf2 acts HERE (GO:0120241)
              │   (catalytic Arg101 + active-site water)
              ▼
   2-oxobutanoate  /  pyruvate   +   NH3   ← stable, harmless products
```

**Direct molecular function (core, what to annotate):** mmf2 is proposed to catalyze the hydrolytic deamination of reactive 2-imino/enamine intermediates — 2-iminobutanoate (from Thr/Ile metabolism via threonine dehydratase, EC 4.3.1.19) and 2-iminopropanoate/2-aminoacrylate (from Ser/Cys metabolism, EC 4.3.1.17) — yielding 2-oxobutanoate/pyruvate plus ammonia. This is **GO:0120241** and its children GO:0120242/GO:0120243.

**Downstream biological process (not core MF):** By deaminating these reactive intermediates before they covalently inactivate PLP-dependent enzymes, RidA-family proteins protect central metabolism. In mitochondria, the consequence of losing this activity (documented for yeast Mmf1p) is enamine/imine stress, impaired growth, disrupted heme biosynthesis (via Hem1p), and loss of mitochondrial DNA. These are **pleiotropic downstream phenotypes**, not the immediate catalytic function.

**Cellular location:** Both *S. pombe* RidA paralogs are annotated mitochondrion + cytosol; the closest characterized ortholog Mmf1p is mitochondrial. The seed hypothesis's "mitochondrial" framing is consistent with this, though the more complete current annotation is dual localization (mitochondrion + cytosol).

The curation logic chain:

```
Domain (RidA/PTHR11803)  +  conserved catalytic Arg101  +  characterized ortholog Mmf1p
        └──────────────────────────┬──────────────────────────┘
                                    ▼
   GO:0120241 (2-iminobutanoate/2-iminopropanoate deaminase activity)
   assigned by ISS/ISO  (with/from: Mmf1p P40185 or human HRSP12 P52758)
                                    │
                                    ▼
   Downstream (non-core):  enamine/imine detoxification, metabolic-stress
                           protection, mtDNA maintenance = phenotypes
```

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 22094463](https://pubmed.ncbi.nlm.nih.gov/22094463/) | Direct assay | **Supports** | Family deaminase activity underlying GO:0120241 | YjgF/Rid proteins deaminate enamine/imine intermediates of PLP dehydratases | *S. enterica* in vitro | High for activity definition; not on Q9UR06 |
| [PMID: 23386433](https://pubmed.ncbi.nlm.nih.gov/23386433/) | Direct assay / reconstitution | **Supports** | Role = pre-empt 2AA damage across all domains | RidA loss lowers IlvE via 2AA; conserved across all domains of life | *S. enterica* + cross-domain | High for family conservation |
| [PMID: 25975565](https://pubmed.ncbi.nlm.nih.gov/25975565/) | Structural/evolutionary | **Supports** | Catalytic Arg is diagnostic of active RidA subfamilies | Rid1–Rid3 (active) retain the essential Arg; Rid4–Rid7 do not | Salmonella + phylogenomics | High for family logic; not specific to Q9UR06 |
| [PMID: 34559917](https://pubmed.ncbi.nlm.nih.gov/34559917/) | Mutant phenotype / localization | **Supports** | Closest ortholog is mitochondrial enamine/imine deaminase | Mmf1p prevents enamine/imine stress, maintains mtDNA; loss damages Hem1p | *S. cerevisiae* mitochondria | High for ortholog; mtDNA/heme roles are downstream |
| [PMID: 29487232](https://pubmed.ncbi.nlm.nih.gov/29487232/) | Mutant phenotype | **Qualifies** | mtDNA maintenance is downstream | Mmf1p couples 2AA deamination to mtDNA maintenance | *S. cerevisiae* | High; frames mtDNA as consequence |
| [PMID: 40596262](https://pubmed.ncbi.nlm.nih.gov/40596262/) | Direct assay / structural | **Supports** | Active-site Arg + water drive 2AA deamination | SsRidA deaminates 2AA → pyruvate; homotrimer with active-site Arg | *S. sanguinis* | High for mechanism |
| [PMID: 38801230](https://pubmed.ncbi.nlm.nih.gov/38801230/) | Direct assay / mutagenesis | **Supports** | RidA hydrolyzes 2-imino acids → 2-keto acids + NH₃ | Confirms core reaction and role in 2AA degradation | *Capra hircus* | High for mechanism |
| [PMID: 32669283](https://pubmed.ncbi.nlm.nih.gov/32669283/) | Review/database | **Supports (orientation)** | RidA is the archetypal active subfamily | RidA found in all domains; biochemical function is enamine deaminase | Review | Review-level; orientation |
| [PMID: 32576850](https://pubmed.ncbi.nlm.nih.gov/32576850/) | Direct assay | **Qualifies** | Paralog-specific substrate properties within Rid | Two fish RidA paralogs differ biochemically | *Salmo salar* | Shows paralogs can diverge — relevant caveat |
| Sequence analysis (this work) | Computational | **Supports** | mmf2 retains catalytic Arg | mmf2 Arg101 ≡ E. coli RidA Arg105; conserved in all homologs | Q9UR06 vs P0AF93 + 5 homologs | Direct on Q9UR06 sequence; inference only for activity |
| UniProt/PANTHER/InterPro (this work) | Computational/database | **Supports** | mmf2 belongs to active RidA family | IPR006056/IPR006175, PF01042, PTHR11803:SF58 | Q9UR06 record | Database-level; strong family signal |
| UniProt P52758 (HRSP12) | Database | **Supports** | Specific MF terms used for orthologs | Human ortholog annotated GO:0120242 (TAS) + GO:0120243 (RHEA) | *H. sapiens* | High term precedent |

**How the papers connect:** [PMID: 25975565](https://pubmed.ncbi.nlm.nih.gov/25975565/) supplies the sequence criterion (catalytic Arg) that lets us place mmf2 in the active branch; [PMID: 22094463](https://pubmed.ncbi.nlm.nih.gov/22094463/), [PMID: 23386433](https://pubmed.ncbi.nlm.nih.gov/23386433/), [PMID: 40596262](https://pubmed.ncbi.nlm.nih.gov/40596262/), and [PMID: 38801230](https://pubmed.ncbi.nlm.nih.gov/38801230/) supply the direct biochemistry of the family reaction (GO:0120241); and [PMID: 34559917](https://pubmed.ncbi.nlm.nih.gov/34559917/) plus [PMID: 29487232](https://pubmed.ncbi.nlm.nih.gov/29487232/) characterize the closest ortholog Mmf1p and demonstrate that mtDNA maintenance is downstream. [PMID: 32576850](https://pubmed.ncbi.nlm.nih.gov/32576850/) provides a cautionary note that paralogs can diverge biochemically — relevant to mmf1 vs mmf2.

*(Computed provenance: `artifacts/mmf2_catalytic_arg_conservation.csv`.)*

---

## GO Curation Implications (leads — require curator verification)

- **ADD MF `GO:0120241` (2-iminobutanoate/2-iminopropanoate deaminase activity)** with evidence code **ISS/ISO** (with/from *S. cerevisiae* Mmf1p P40185 and/or human HRSP12 P52758), or retain IBA if the GO_Central IBA set is refreshed. GO:0120241 is defined as the "hydrolytic deamination of imine intermediates formed by … PLP-dependent dehydratases such as EC 4.3.1.19 and EC 4.3.1.17" — i.e., exactly the RidA activity. This directly answers the seed hypothesis: the specific term is warranted.
- **Do NOT use an experimental code (IDA/IMP/EXP)** — there is no direct assay on Q9UR06.
- **Generic `GO:0019239` (deaminase activity)** is too broad; it should be superseded by GO:0120241 (or retained only as the redundant parent).
- **Optionally add the two children `GO:0120242` / `GO:0120243`**, mirroring the human ortholog HRSP12; but the parent GO:0120241 is the safest single-term choice absent mmf2-specific substrate data.
- **CC:** retain mitochondrion (e.g., GO:0005759 mitochondrial matrix, ISO) and cytosol (GO:0005829) — dual localization matches both paralogs and the predicted N-terminal transit peptide.
- **Reclassify "mitochondrial DNA maintenance"** free-text/annotation as **non-core / downstream BP phenotype**, not the molecular function ([PMID: 29487232](https://pubmed.ncbi.nlm.nih.gov/29487232/) shows it is a consequence of unmanaged 2AA).
- **Avoid** "protein binding" — a specific, well-supported catalytic MF is available and far more informative.

---

## Mechanistic Scope

**Immediate molecular function (core):** hydrolytic deamination of reactive 2-imino acids — 2-iminobutanoate (from Thr/Ile metabolism, EC 4.3.1.19) and 2-iminopropanoate/2-aminoacrylate (from Ser/Cys metabolism, EC 4.3.1.17) — yielding 2-oxobutanoate/pyruvate + NH₄⁺. This is the direct gene-product activity captured by GO:0120241.

**Downstream effects (not core):**
- *Prevention of 2-aminoacrylate damage to PLP enzymes* — the protective consequence of the deaminase activity.
- *Mitochondrial DNA maintenance* (yeast Mmf1p) — a downstream consequence of preventing enamine/imine stress.
- *Heme biosynthesis* (via Hem1p, [PMID: 34559917](https://pubmed.ncbi.nlm.nih.gov/34559917/)) — pathway-level downstream effect in yeast.
- *Growth defects / respiratory competence / isoleucine biosynthesis* — loss-of-function phenotypes.

None of these should be annotated as the core molecular function; they are properly BP/phenotype-level observations.

---

## Conflicts and Alternatives

1. **Paralog/ortholog confusion (principal caveat).** All direct enzymatic evidence is from Mmf1p, Hmf1p, bacterial RidA, RutC, human HRSP12, and fish/goat/streptococcal RidA — **not** from Q9UR06. The assignment for mmf2 is inference by homology, appropriately coded ISS/ISO.

2. **Paralog substrate divergence.** [PMID: 32576850](https://pubmed.ncbi.nlm.nih.gov/32576850/) shows that gene-duplication paralogs within the Rid family can diverge biochemically. *S. pombe* has two RidA paralogs (mmf1, mmf2), both retaining the catalytic Arg. This does not undermine the family assignment but means the *precise* child term (GO:0120242 vs GO:0120243) for mmf2 specifically is not established, and there is no direct evidence of narrowed/divergent specificity between the two paralogs. GO:0120241 (the generalist parent) therefore applies to both.

3. **PANTHER subfamily / "RutC family" wording.** PTHR11803:SF58 is named "PROTEIN HMF1-RELATED," and UniProt uses "RutC family" language. This is legacy nomenclature for the YjgF/RidA fold, not evidence of a distinct RutC pyrimidine-utilization activity. Because mmf2 retains the conserved catalytic Arg and its closest characterized ortholog (Mmf1p) is a bona fide 2AA deaminase, the "HMF1-related/RutC-family" wording does not argue against GO:0120241 — it reflects naming history.

4. **Legacy RNase / translation-inhibitor annotations.** The UK114/p14.5 family historically carried "endoribonuclease" and "translation inhibitor" annotations. These are widely regarded as secondary or artifactual since the RidA deaminase activity was established and should **not** be propagated to mmf2.

5. **Rid4–Rid7 inactive subfamilies.** These lack the catalytic Arg and would NOT justify GO:0120241. mmf2 is explicitly not in this group — it retains Arg101 — so this alternative is ruled out by the sequence analysis.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct assay of Q9UR06 | PubMed + UniProt; only orthologs/paralogs assayed | Determines experimental vs ISS/ISO evidence code | In vitro 2AA/2-iminobutanoate deaminase assay on recombinant mmf2 |
| Substrate specificity (2-iminobutanoate vs 2-iminopropanoate) | Family definition; ortholog data | Determines which child term (GO:0120242 vs GO:0120243) is most accurate | Enzyme kinetics with defined substrates |
| Precise subcellular localization of mmf2 | UniProt: mitochondrion + cytosol (by similarity) | "Mitochondrial" claim in seed may be incomplete | GFP fusion / fractionation in *S. pombe* |
| Functional redundancy of mmf1 vs mmf2 | Two paralogs identified | Single-deletion phenotypes may be masked | Single and double deletion phenotyping under 2AA/Ser stress |
| Whether mmf2 complements a ridA/mmf1 mutant | Not available for Q9UR06 | Direct functional proof | Heterologous complementation of *S. enterica* ridA or yeast mmf1Δ |

Additional limitation: the inference is homology/active-site based; PubMed access via the provided tool was intermittent for some queries; and localization for mmf2 is by similarity (ISO/ECO:0000250), not measured directly in fission yeast.

---

## Discriminating Tests

1. **Heterologous complementation:** Express mmf2 in an *S. enterica* ridA⁻ strain (or *S. cerevisiae* mmf1Δ) and test rescue of 2AA-mediated stress / growth on minimal medium — the classic decisive functional test (used for SsRidA in [PMID: 40596262](https://pubmed.ncbi.nlm.nih.gov/40596262/)).

2. **In vitro deaminase kinetics:** Purify recombinant mmf2 and measure deamination of 2-aminoacrylate (→ pyruvate) and 2-iminobutanoate (→ 2-oxobutanoate) via the coupled L-amino-acid-oxidase or IlvA/IlvE assay. Distinguishes GO:0120242 from GO:0120243 preference.

3. **Active-site Arg mutagenesis:** Generate mmf2 R101A and confirm loss of activity — directly tying the conserved arginine identified computationally to catalysis (mirrors goat RidA, [PMID: 38801230](https://pubmed.ncbi.nlm.nih.gov/38801230/)).

4. **Localization:** GFP-tagged mmf2 in *S. pombe* to confirm mitochondrial and/or cytosolic localization.

5. **Genetic interaction / paralog dissection:** mmf1Δ, mmf2Δ, and mmf1Δmmf2Δ under serine/cysteine/isoleucine-pathway stress plus metabolomics for 2AA-adduct accumulation and mtDNA/respiration phenotypes.

---

## Proposed Follow-up Actions / Curation Leads (verify before applying)

- **Candidate new MF term:** `GO:0120241` (ISS/ISO, with-from P40185 and/or P52758). Optional children GO:0120242, GO:0120243.
- **Action change:** downgrade/replace generic `GO:0019239`; reclassify "mtDNA maintenance" free text as a downstream phenotype rather than core function.
- **Candidate references + snippets to verify:**
  - [PMID: 34559917](https://pubmed.ncbi.nlm.nih.gov/34559917/) — *"The mitochondrial RidA homolog, Mmf1p, prevents enamine/imine stress and is important for normal growth and maintenance of mitochondrial DNA."*
  - [PMID: 22094463](https://pubmed.ncbi.nlm.nih.gov/22094463/) — *"YjgF proteins have enamine/imine deaminase activity and accelerate the release of ammonia from reactive enamine/imine intermediates of the pyridoxal 5'-phosphate-dependent threonine dehydratase (IlvA)."*
  - [PMID: 25975565](https://pubmed.ncbi.nlm.nih.gov/25975565/) — *"The Rid1 to Rid3 subfamilies, but not the Rid4 to Rid7 subfamilies, have a conserved arginine residue that, in RidA proteins, is essential for imine-hydrolyzing activity."*
- **Suggested curator questions:** Is an ISS MF acceptable given no pombe-specific assay? Should both paralogs (mmf1, mmf2) receive the same MF? Retain generic GO:0019239 as redundant parent or remove?
- **Suggested experiments:** the discriminating tests above, prioritizing heterologous complementation and R101A mutagenesis.

---

## Conclusion

The seed hypothesis is **supported**: mmf2 has every hallmark of an active RidA-subfamily enzyme — the RidA/PTHR11803 domain assignment plus the conserved catalytic Arg101 (aligning to *E. coli* RidA Arg105) — and its closest characterized ortholog (yeast Mmf1p) is a demonstrated mitochondrial 2-aminoacrylate/enamine–imine deaminase. **GO:0120241** is a better-justified core molecular function than the current generic **GO:0019239** and should be added by **ISS/ISO** (with/from Mmf1p P40185 or human HRSP12 P52758), not an experimental code. Mitochondrial DNA maintenance and related phenotypes should be treated as downstream biological-process consequences, not the core function. The one substantive limitation is the absence of any direct enzymatic assay on Q9UR06 itself, which a heterologous complementation or in vitro deaminase assay would readily resolve.


## Artifacts

- [OpenScientist mmf2 catalytic arg conservation](openscientist_artifacts/artifacts_mmf2_catalytic_arg_conservation.csv)
- [OpenScientist mmf2 evidence matrix](openscientist_artifacts/artifacts_mmf2_evidence_matrix.csv)
- [OpenScientist mmf2 go decision table](openscientist_artifacts/artifacts_mmf2_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)