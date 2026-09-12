# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** DROME
- **Taxon:** Drosophila melanogaster (NCBITaxon:7227)
- **Gene directory:** TyrRS
- **Gene symbol:** TyrRS
- **UniProt accession:** Q9VV60

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fly41-resveratrol-recognition
- **Source file:** genes/DROME/TyrRS/TyrRS-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The Drosophila melanogaster protein Q9VV60 binds resveratrol.

## Term and Decision Context

- Term: resveratrol binding (GO:1905594)
- # Focused fly function hypothesis

Hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.

Target: Drosophila melanogaster (NCBITaxon:7227), UniProt Q9VV60. Gene label: TyrRS. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

## Original prediction

F:resveratrol binding

## Decisive question

Evaluate biochemical resveratrol recognition by the supplied fly TyrRS sequence using verified ligand-bound structures, experimentally tested contact residues and conformational requirements in characterized TyrRS proteins. Establish the transferability of the binding pocket rather than relying on whole-protein similarity. Assess assay conditions, controls and compound isomer where reported. If docking is used, include meaningful controls and treat scores as hypotheses, not measured binding or evidence of physiological function. Separate binding from downstream stress signaling and from whether this interaction merits a GO molecular-function annotation; check the current status and scope of the emitted term independently.

## Identity and sequence

- Target record: https://www.uniprot.org/uniprotkb/Q9VV60/entry
- FlyBase identifier(s) from the cohort identity mapping: FBgn0027080.
- Frozen current UniProt sequence: 525 residues; SHA-256 `94682a9b94b943a5eca242d7bb960b2787dc2557781933a8d5849bd5e371a01f`.
- The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

```fasta
>Q9VV60 Drosophila melanogaster TyrRS
MVGITPAEKKALITRNLQETLGDDKLTKILAERDLKIYWGTATTGKPHVAYFVPMSKIAD
FLKAGCEVTILFADLHAYLDNMKAPWSLLELRTKYYEQVIKAMLSSIGVPLEKLKFVKGS
DYQLSKEYTLDVYKLSSVVTQHDAKKAGAEVVKQVEYPLLSGLLYPGLQALDEEYLKVDA
QFGGVDQRKIFTFSEKYLPQLGYEKRIHFMNPMVPGLAGGKMSSSEEDSKIDLLDSPANV
KKKLKKAFCEPGNIADNGLLSFVKHVLFSLFKEGEGFEVNREAEHGGDVTFLKYEDLEKY
YAEDKLHPGDLKATVEKYINRLLDPIRKAFENPELQKLSAAAYPPPAKVKAGAAPAAGAD
EDAPHRLDIRVGKVVEVARHPDADTLYVLKIDLAEAQPRTIISGLVKFVTEEELNQRLVA
VLCNLKPSKMRGILSEGMVLCTSNADHTVVEPIVLPATATAGSRLSFEGFSGTPDEQLNP
KKKVWEKLSADFKTNSDGLAVWKDNFLLTPEGEKLSSKLANCSIK
```

Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/25533949/

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. This is a focused mechanistic investigation, not a general gene overview. Seek supporting, contrary and competing explanations; an unresolved result is acceptable. Distinguish direct fly experiments, justified transfers and results on a different isoform. Do not equate missing target experiments with evidence of absence.

Do not consult the ai-gene-review repository's current reviews, generated research summaries or local bioinformatics analyses; these are held out for comparison. Agreement with ARBA or repeated prediction text does not validate the biology. Save executed methods/code, actual analysis outputs, sequence identifiers and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not just a verdict. Do not fabricate computations or use docking/structural resemblance alone as experimental validation.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.
focus_type: function_assignment
term_id: GO:1905594
term_label: resveratrol binding
context:
- |
  # Focused fly function hypothesis

  Hypothesis: The Drosophila melanogaster protein Q9VV60 binds resveratrol.

  Target: Drosophila melanogaster (NCBITaxon:7227), UniProt Q9VV60. Gene label: TyrRS. Verify identity and isoform independently; the gene label is not evidence for the hypothesis.

  ## Original prediction

  F:resveratrol binding

  ## Decisive question

  Evaluate biochemical resveratrol recognition by the supplied fly TyrRS sequence using verified ligand-bound structures, experimentally tested contact residues and conformational requirements in characterized TyrRS proteins. Establish the transferability of the binding pocket rather than relying on whole-protein similarity. Assess assay conditions, controls and compound isomer where reported. If docking is used, include meaningful controls and treat scores as hypotheses, not measured binding or evidence of physiological function. Separate binding from downstream stress signaling and from whether this interaction merits a GO molecular-function annotation; check the current status and scope of the emitted term independently.

  ## Identity and sequence

  - Target record: https://www.uniprot.org/uniprotkb/Q9VV60/entry
  - FlyBase identifier(s) from the cohort identity mapping: FBgn0027080.
  - Frozen current UniProt sequence: 525 residues; SHA-256 `94682a9b94b943a5eca242d7bb960b2787dc2557781933a8d5849bd5e371a01f`.
  - The sequence was frozen for the fly cohort on 2026-09-08. It is not established as the original prediction-time input. Analyze this sequence explicitly and document any alternate accession, version or isoform you analyze.

  ```fasta
  >Q9VV60 Drosophila melanogaster TyrRS
  MVGITPAEKKALITRNLQETLGDDKLTKILAERDLKIYWGTATTGKPHVAYFVPMSKIAD
  FLKAGCEVTILFADLHAYLDNMKAPWSLLELRTKYYEQVIKAMLSSIGVPLEKLKFVKGS
  DYQLSKEYTLDVYKLSSVVTQHDAKKAGAEVVKQVEYPLLSGLLYPGLQALDEEYLKVDA
  QFGGVDQRKIFTFSEKYLPQLGYEKRIHFMNPMVPGLAGGKMSSSEEDSKIDLLDSPANV
  KKKLKKAFCEPGNIADNGLLSFVKHVLFSLFKEGEGFEVNREAEHGGDVTFLKYEDLEKY
  YAEDKLHPGDLKATVEKYINRLLDPIRKAFENPELQKLSAAAYPPPAKVKAGAAPAAGAD
  EDAPHRLDIRVGKVVEVARHPDADTLYVLKIDLAEAQPRTIISGLVKFVTEEELNQRLVA
  VLCNLKPSKMRGILSEGMVLCTSNADHTVVEPIVLPATATAGSRLSFEGFSGTPDEQLNP
  KKKVWEKLSADFKTNSDGLAVWKDNFLLTPEGEKLSSKLANCSIK
  ```

  Primary literature lead to inspect (not a preassigned conclusion): https://pubmed.ncbi.nlm.nih.gov/25533949/

  ## Evidence and deliverable

  Use primary literature and public sequence, structural and genomic resources. This is a focused mechanistic investigation, not a general gene overview. Seek supporting, contrary and competing explanations; an unresolved result is acceptable. Distinguish direct fly experiments, justified transfers and results on a different isoform. Do not equate missing target experiments with evidence of absence.

  Do not consult the ai-gene-review repository's current reviews, generated research summaries or local bioinformatics analyses; these are held out for comparison. Agreement with ARBA or repeated prediction text does not validate the biology. Save executed methods/code, actual analysis outputs, sequence identifiers and primary-source URLs/DOIs/PMIDs. Report decisive evidence and limitations, not just a verdict. Do not fabricate computations or use docking/structural resemblance alone as experimental validation.
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

**Provider:** openscientist
**Generated:** 2026-09-08T22:09:28.885597

1. PMID:19561293
2. PMID:25533949
3. PMID:38903666
4. PMID:40644839
5. PMID:26761199
6. PMID:35688816