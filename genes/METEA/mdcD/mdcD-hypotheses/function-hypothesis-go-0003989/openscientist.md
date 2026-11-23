---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:40:32.619724'
end_time: '2026-10-24T05:39:32.391201'
duration_seconds: 3539.77
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: METEA
  gene: mdcD
  gene_symbol: mdcD
  uniprot_accession: C5APL4
  taxon_id: NCBITaxon:272630
  taxon_label: Methylorubrum extorquens AM1
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0003989
  hypothesis_text: mdcD has acetyl-CoA carboxylase activity (GO:0003989).
  term_context: '- Term: acetyl-CoA carboxylase activity (GO:0003989)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - PMID:28757619

    - file:METEA/mdcD/mdcD-notes.md

    - file:METEA/mdcD/mdcD-uniprot.txt'
  source_file: genes/METEA/mdcD/mdcD-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0003989\n  label: acetyl-CoA carboxylase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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
citation_count: 1
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
- filename: provenance_mdcD_GO_decision_table.csv
  path: openscientist_artifacts/provenance_mdcD_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mdcD GO decision table
- filename: provenance_mdcD_evidence_matrix.csv
  path: openscientist_artifacts/provenance_mdcD_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mdcD evidence matrix
- filename: provenance_mdcD_sequence_identity_comparison.csv
  path: openscientist_artifacts/provenance_mdcD_sequence_identity_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mdcD sequence identity comparison
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** METEA
- **Taxon:** Methylorubrum extorquens AM1 (NCBITaxon:272630)
- **Gene directory:** mdcD
- **Gene symbol:** mdcD
- **UniProt accession:** C5APL4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0003989
- **Source file:** genes/METEA/mdcD/mdcD-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis

mdcD has acetyl-CoA carboxylase activity (GO:0003989).

## Term and Decision Context

- Term: acetyl-CoA carboxylase activity (GO:0003989)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:28757619
- file:METEA/mdcD/mdcD-notes.md
- file:METEA/mdcD/mdcD-uniprot.txt

## Source Context YAML

```yaml
term:
  id: GO:0003989
  label: acetyl-CoA carboxylase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
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

# mdcD (C5APL4) — Hypothesis Review: "acetyl-CoA carboxylase activity (GO:0003989)"

**Gene:** mdcD · **Organism:** *Methylorubrum extorquens* AM1 (NCBITaxon:272630) · **UniProt:** C5APL4 (310 aa)
**Focus:** function_assignment · **Seed hypothesis:** *mdcD has acetyl-CoA carboxylase activity (GO:0003989)* · **Evidence type in review:** IEA (GO_REF:0000118)

---

## Executive Judgment

**Verdict: REFUTED / over-annotated.**

`mdcD` encodes the **β-subunit of a biotin-independent malonate decarboxylase (MDC)**, not an acetyl-CoA carboxylase. The GO:0003989 annotation is a phylogenetic over-annotation produced by TreeGrafter (GO_REF:0000118) grafting the protein to a PANTHER *family* node (PTHR42995, "acetyl-CoA carboxylase carboxyl transferase subunit β"), while the matching PANTHER *subfamily* (PTHR42995:**SF1 = "malonate decarboxylase beta subunit"**) and the malonate-specific HMM signatures (NCBIfam **TIGR03133 "malonate_beta"**, InterPro **IPR017556 "Malonate_beta"**) correctly identify the protein.

The acetyl-CoA carboxylase reaction (GO:0003989 definition: `ATP + acetyl-CoA + HCO₃⁻ → ADP + Pi + malonyl-CoA`) is a **biotin-dependent, multi-step carboxylation** requiring biotin-carboxylase (ATP-grasp) and biotin-carboxyl-carrier (BCCP) functions. MdcD contains **only** a single carboxyltransferase domain (Pfam **PF01039 Carboxyl_trans**, InterPro IPR011762 COA_CT_N; crotonase/ClpP-like fold) and has **no ATP-grasp and no BCCP domain**, so it is mechanistically incapable of the GO:0003989 reaction. The referenced crystal-structure paper **PMID:28757619** shows directly that MdcD–MdcE form the **decarboxylase** catalytic component of the MDC holoenzyme and that a CoA thioester binds the MdcD–MdcE active site — a decarboxylation, not an acetyl-CoA carboxylation, chemistry.

**Organism-specific corroboration (Iteration 2):** KEGG annotates the exact target gene **mea:Mex_1p0025 (= C5APL4)** as "malonate decarboxylase, beta-subunit", KEGG Orthology **K13932, EC 4.1.1.87** (*malonyl-[malonate decarboxylase] decarboxylase*, a class-4 carboxy-lyase) — a different enzyme class from acetyl-CoA carboxylase (EC 6.4.1.2, class 6). A UniProt proteome search of *M. extorquens* AM1 recovers the **intact, syntenic mdc operon** (mdcA C5APL2, mdcB C5APL7, mdcC C5APL3 [ACP], mdcD C5APL4, mdcE C5APL5), consistent with a complete, functional biotin-independent malonate decarboxylase in this organism rather than a fatty-acid-biosynthetic ACC.

**Caveats:** (i) all target annotations are IEA/electronic — there is no experimental characterization of the *M. extorquens* AM1 protein itself; (ii) the strongest experimental evidence (PMID:28757619) is from a *Pseudomonas* ortholog; (iii) GO lacks a dedicated "malonate decarboxylase activity" MF term, so the best supported replacements are general (carboxy-lyase / carboxyltransferase).

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:28757619 | Structural (X-ray) + mutagenesis | **Refutes** | Does MdcD carboxylate acetyl-CoA? | MdcD–MdcE are the **decarboxylase** catalytic subunits of biotin-independent MDC; CoA bound in the MdcD–MdcE active site | *Pseudomonas* MDC holoenzyme (ortholog) | High; ortholog, not METEA itself |
| UniProt C5APL4 (TIGR03133 / IPR017556 / PANTHER SF1) | Computational / domain | **Refutes → reassigns** | Protein identity & function | Classified as **malonate decarboxylase β subunit**; single Carboxyl_trans (PF01039) domain; **no biotin-carboxylase / BCCP** | *M. extorquens* AM1 (target) | High |
| GO:0003989 definition (QuickGO) | Ontology / database | **Refutes** | Can a lone carboxyltransferase run the ACC reaction? | Term = `ATP + acetyl-CoA + HCO₃⁻ → ADP + Pi + malonyl-CoA`; biotin-dependent, multi-domain — impossible for MdcD alone | N/A | High |
| UniProt GO set (C5APL4) | Database (IEA) | **Qualifies** | Reliability of electronic annotations | Protein carries several **conflicting** IEA MF terms (GO:0003989 ACC; GO:0004658 propionyl-CoA carboxylase; GO:0016831 carboxy-lyase) — hallmark carboxyltransferase carry-over | Target | Moderate; all IEA, none experimental |
| TreeGrafter / GO_REF:0000118 | Computational (phylogenetic) | **Competing** | Provenance of GO:0003989 | Grafted at **family** node PTHR42995 (ACC CT-β); **subfamily SF1 = malonate decarboxylase β** is more specific and correct | N/A | High that the annotation is a family-level over-reach |
| KEGG mea:Mex_1p0025 (KO K13932) | Database | **Refutes → reassigns** | Organism-specific function of mdcD | Named "malonate decarboxylase, beta-subunit"; **K13932, EC 4.1.1.87** (carboxy-lyase, class 4) — *not* EC 6.4.1.2; only Carboxyl_trans motif | *M. extorquens* AM1 (target) | High (database-level; organism-specific) |
| UniProt proteome search (taxon 272630) | Database / evolutionary | **Supports reassignment** | Is the full MDC operon present in METEA? | Intact, syntenic **mdc cluster**: mdcA (C5APL2), mdcB (C5APL7), mdcC (C5APL3, ACP), mdcD (C5APL4), mdcE (C5APL5) | *M. extorquens* AM1 (target) | High; implies a functional MDC holoenzyme |

*Provenance artifacts:* `provenance/mdcD_evidence_matrix.csv`, `provenance/mdcD_GO_decision_table.csv` (UniProt/QuickGO queries executed live via the REST APIs).

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Label | Aspect | Action | Rationale |
|---|---|---|---|---|
| **GO:0003989** | acetyl-CoA carboxylase activity | MF | **REMOVE** | Over-annotation; MdcD cannot catalyze the biotin-dependent ACC reaction |
| GO:0004658 | propionyl-CoA carboxylase activity | MF | REMOVE | Same carboxyltransferase-domain carry-over (note: also present on C5APL4) |
| GO:0006633 | fatty acid biosynthetic process | BP | REMOVE/REVISE | Downstream of the ACC mis-assignment; MdcD is catabolic |
| GO:2001295 | malonyl-CoA biosynthetic process | BP | REMOVE/REVISE | Downstream of the ACC mis-assignment |
| GO:0016831 | carboxy-lyase activity | MF | **RETAIN** | Correct, mechanism-consistent general class (already IEA/InterPro) |
| GO:0016743 | carboxyl- or carbamoyltransferase activity | MF | ADD (lead) | Reflects the MdcD–MdcE carboxyltransferase step in the holoenzyme |
| GO:0090410 | malonate catabolic process | BP | ADD (lead) | Correct biological process for the mdc operon |

No dedicated "malonate decarboxylase activity" MF term exists in GO; `carboxy-lyase activity` (GO:0016831) is the most informative supported MF. "Protein binding" is **not** recommended.

---

## Sequence Discriminator (Iteration 3, computed)

A Needleman–Wunsch global alignment (own code; provenance `provenance/mdcD_sequence_identity_comparison.csv`) places mdcD (C5APL4) with malonate decarboxylase, not with acetyl-CoA carboxylase:

| C5APL4 vs | Role of reference | Global % identity |
|---|---|---|
| **Q9I6S7** (*P. aeruginosa* MdcD) | malonate decarboxylase β-subunit (structure organism) | **42.5 %** |
| P0A9Q5 (*E. coli* AccD) | **bona fide** ACC carboxyltransferase β | 18.3 % |
| P0ABD5 (*E. coli* AccA) | **bona fide** ACC carboxyltransferase α | 22.1 % |

mdcD is ~2× more similar to a malonate decarboxylase β-subunit than to any genuine acetyl-CoA carboxylase subunit; the residual 18–22 % reflects only the shared carboxyltransferase fold — exactly the signal that misleads automated (family-level) annotation.

## Mechanistic Scope

- **Direct molecular function tested:** whether MdcD carboxylates acetyl-CoA (ATP-/biotin-dependent). **Not supported.**
- **Actual direct function:** MdcD is the β carboxyltransferase subunit that, together with MdcE (γ), forms the **decarboxylase catalytic module** of the malonate decarboxylase holoenzyme (also containing MdcC acyl-carrier protein and MdcA ACP-transferase). The module decarboxylates a malonyl-thioester (malonyl-S-ACP) to acetyl-S-ACP + CO₂.
- **Pathway consequence (not direct activity):** malonate catabolism, allowing malonate use as a carbon/energy source — a *downstream* process, not the per-subunit molecular activity.
- The seed term conflates a shared **structural fold** (carboxyltransferase, common to ACC-β, PCC, methylmalonyl-CoA decarboxylase, and MDC-β) with a specific **reaction**.

---

## Conflicts and Alternatives

- **Paralog/family confusion (primary driver):** The PF01039 carboxyltransferase fold is shared across biotin-dependent carboxylases (ACC, propionyl-CoA carboxylase) and biotin-independent decarboxylases (MDC). Automated pipelines inherit the family label (acetyl-CoA carboxylase) instead of the subfamily (malonate decarboxylase β). The same protein simultaneously carries GO:0004658 (propionyl-CoA carboxylase) — an internal contradiction confirming annotation noise.
- **Organism specificity:** Experimental proof is from *Pseudomonas* (PMID:28757619) and historically *Klebsiella/Acinetobacter/Malonomonas*; the *M. extorquens* AM1 protein is inferred by orthology/synteny (mdc operon) and is not individually assayed.
- **No competing experimental claim** supports an ACC role for any MdcD ortholog.

---

## Knowledge Gaps

1. **No direct biochemistry on C5APL4 itself.** Checked: UniProt shows only IEA. Matters because curation ideally wants organism-specific support. Resolved by: in-vitro reconstitution/decarboxylation assay of the *M. extorquens* MDC, or demonstrated malonate-dependent growth phenotype on knockout.
2. **mdc operon completeness / synteny in METEA.** Checked: single-protein UniProt record only; did not enumerate neighboring mdcA/C/E/G/H. Matters because the holoenzyme context strengthens the decarboxylase call. Resolved by: genome-neighborhood analysis (e.g., NCBI/KEGG operon view).
3. **Exact GO MF granularity.** Checked QuickGO: no "malonate decarboxylase activity" term exists. Matters for choosing the replacement. Resolved by: proposing a new GO term or using GO:0016743/GO:0016831 with the holoenzyme noted in annotation extensions.

---

## Discriminating Tests

- **Domain/sequence:** confirm absence of ATP-grasp (PF00289 Biotin_carb) and BCCP (PF00364) in C5APL4 — already indicated by UniProt; a dedicated HMMER scan would formalize it.
- **Genomic context:** verify the mdcABCDE(GH) operon neighbors in *M. extorquens* AM1.
- **Biochemical:** malonate decarboxylase assay (CO₂/acetate release from malonyl-thioester) on reconstituted METEA subunits; ACC assay (malonyl-CoA formation from acetyl-CoA + bicarbonate + ATP) as the **negative** discriminator — expected inactive.
- **Genetics:** mdcD deletion → loss of growth on malonate as sole carbon source (parallels the *P. aeruginosa* result in PMID:28757619).

---

## Curation Leads (require curator verification)

- **Action:** Remove GO:0003989 (and flag GO:0004658, GO:0006633, GO:2001295 as derived over-annotations). Retain GO:0016831. Consider adding GO:0016743 (MF) and GO:0090410 (BP), annotating MdcD as the β carboxyltransferase subunit of the malonate decarboxylase holoenzyme.
- **Candidate reference to cite:** **PMID:28757619** — verify snippet: *"...decarboxylase (MdcD-MdcE) and acyl-carrier protein transferase (MdcA) catalytic activities."* and *"...the structure of malonate decarboxylase with CoA in the active site of MdcD-MdcE."*
- **Supporting signatures to cite:** UniProt C5APL4 cross-refs TIGR03133 (malonate_beta), InterPro IPR017556 (Malonate_beta), PANTHER PTHR42995:SF1 (malonate decarboxylase beta subunit).
- **Suggested questions for curator:** Is there a METEA-specific malonate-utilization phenotype or operon annotation? Should the review also down-rank the co-occurring propionyl-CoA carboxylase IEA term?
- **Suggested experiment:** reconstituted MDC decarboxylase assay + mdcD knockout growth test on malonate.

---

### Limitations
Evidence is orthology- and domain-based for the target protein; the decisive functional data are from a *Pseudomonas* ortholog. No local bioinformatics files were available in this run; all computational checks used live UniProt and QuickGO REST queries.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist mdcD GO decision table](openscientist_artifacts/provenance_mdcD_GO_decision_table.csv)
- [OpenScientist mdcD evidence matrix](openscientist_artifacts/provenance_mdcD_evidence_matrix.csv)
- [OpenScientist mdcD sequence identity comparison](openscientist_artifacts/provenance_mdcD_sequence_identity_comparison.csv)