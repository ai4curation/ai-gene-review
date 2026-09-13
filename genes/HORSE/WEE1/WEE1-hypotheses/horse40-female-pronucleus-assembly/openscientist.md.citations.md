# Citations for Research Query

**Query:** # AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** HORSE
- **Taxon:** Equus caballus (NCBITaxon:9796)
- **Gene directory:** WEE1
- **Gene symbol:** WEE1
- **UniProt accession:** F6TY09

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** horse40-female-pronucleus-assembly
- **Source file:** genes/HORSE/WEE1/WEE1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

The horse protein F6TY09 participates in female pronucleus assembly.

## Term and Decision Context

- Term: female pronucleus assembly (GO:0035038)
- # Focused function hypothesis

Hypothesis: The horse protein F6TY09 participates in female pronucleus assembly.

Target: Equus caballus (NCBITaxon:9796), UniProt F6TY09. Gene label: WEE1; verify identity independently rather than treating the label as proof.

Target GO claim: GO:0035038 — female pronucleus assembly. Verify its definition and scope.

## Decisive question

Resolve the relevant mammalian paralogs and original oocyte perturbation experiments, then assess transfer to horse. Distinguish participation from necessity or sufficiency and evaluate plausible compensation. Identify any direct horse expression or functional evidence.

## Identity and sequence inputs

- Target record: https://www.uniprot.org/uniprotkb/F6TY09/entry
- Human comparison lead: https://www.uniprot.org/uniprotkb/P30291/entry (WEE1). Establish the relevant orthology/isoform relationship rather than assuming it.
- Frozen current UniProt sequence: 646 residues; SHA-256 `f46f1c6be9cdfa7025987fbd2b3d5f5a49a4e7cbb69d75d9101e8b34234429d4`.
- These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

```fasta
>F6TY09 Equus caballus WEE1
MSFLSRQQPPPPRRAAASCSLRQKLIFSPCSDCEEEEEEEEEEGSGHSTGEDSAFQEPDS
PLPPARSPTEPGPERRRSPGPAPGSPGELEEDMLLRGACTGADAAGGGAEGDSWEEEGFG
SSSPVKSPAAAYFLASCFSPVRCGGPGDASPRGYGARGAAEGPCSPLPDQPGTPPHKTFR
KLRLFDTPHTPKSLLSKARGIDSSSVKLRSGSLFMDTEKSGKRELDMRQTPQVNINPFTP
DSVLFHSSGQCRRRKRTYWNDSCGEDMEASDYEFEDETRPAKRITITESNMKSRYTTEFH
ELEKIGSGEFGSVFKCVKRLDGCIYAIKRSKKPLAGSVDEQNALREVYAHAVLGQHSHVV
RYFSAWAEDDHMLIQNEYCNGGSLADAISENYRRMSYFTEVDLKDLLLQVGRGLRYIHSM
SLVHMDIKPSNIFISRTSIPNAASEEGDEDDWASNKVMFKIGDLGHVTRISSPQVEEGDS
RFLANEVLQENYTHLPKADIFALALTVVCAAGAEPLPRNGDEWHEIRQGRLPRIPQVLSQ
EFTELLKVMIHPDPERRPSAMALVKHSVLLSASRKSAEQLRIELNAEKFKNSLLQKELKK
AQMAKAAAEERALFTDRMATRSTTQSNRTARLIGKKMNRSVSLTIY
```

## Evidence and deliverable

Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: The horse protein F6TY09 participates in female pronucleus assembly.
focus_type: function_assignment
term_id: GO:0035038
term_label: female pronucleus assembly
context:
- |
  # Focused function hypothesis

  Hypothesis: The horse protein F6TY09 participates in female pronucleus assembly.

  Target: Equus caballus (NCBITaxon:9796), UniProt F6TY09. Gene label: WEE1; verify identity independently rather than treating the label as proof.

  Target GO claim: GO:0035038 — female pronucleus assembly. Verify its definition and scope.

  ## Decisive question

  Resolve the relevant mammalian paralogs and original oocyte perturbation experiments, then assess transfer to horse. Distinguish participation from necessity or sufficiency and evaluate plausible compensation. Identify any direct horse expression or functional evidence.

  ## Identity and sequence inputs

  - Target record: https://www.uniprot.org/uniprotkb/F6TY09/entry
  - Human comparison lead: https://www.uniprot.org/uniprotkb/P30291/entry (WEE1). Establish the relevant orthology/isoform relationship rather than assuming it.
  - Frozen current UniProt sequence: 646 residues; SHA-256 `f46f1c6be9cdfa7025987fbd2b3d5f5a49a4e7cbb69d75d9101e8b34234429d4`.
  - These are current sequences downloaded for the cohort on 2026-09-08. Identity with the original prediction-time input has not been established. Evaluate the supplied sequence explicitly; document any different sequence used.

  ```fasta
  >F6TY09 Equus caballus WEE1
  MSFLSRQQPPPPRRAAASCSLRQKLIFSPCSDCEEEEEEEEEEGSGHSTGEDSAFQEPDS
  PLPPARSPTEPGPERRRSPGPAPGSPGELEEDMLLRGACTGADAAGGGAEGDSWEEEGFG
  SSSPVKSPAAAYFLASCFSPVRCGGPGDASPRGYGARGAAEGPCSPLPDQPGTPPHKTFR
  KLRLFDTPHTPKSLLSKARGIDSSSVKLRSGSLFMDTEKSGKRELDMRQTPQVNINPFTP
  DSVLFHSSGQCRRRKRTYWNDSCGEDMEASDYEFEDETRPAKRITITESNMKSRYTTEFH
  ELEKIGSGEFGSVFKCVKRLDGCIYAIKRSKKPLAGSVDEQNALREVYAHAVLGQHSHVV
  RYFSAWAEDDHMLIQNEYCNGGSLADAISENYRRMSYFTEVDLKDLLLQVGRGLRYIHSM
  SLVHMDIKPSNIFISRTSIPNAASEEGDEDDWASNKVMFKIGDLGHVTRISSPQVEEGDS
  RFLANEVLQENYTHLPKADIFALALTVVCAAGAEPLPRNGDEWHEIRQGRLPRIPQVLSQ
  EFTELLKVMIHPDPERRPSAMALVKHSVLLSASRKSAEQLRIELNAEKFKNSLLQKELKK
  AQMAKAAAEERALFTDRMATRSTTQSNRTARLIGKKMNRSVSLTIY
  ```

  ## Evidence and deliverable

  Use primary literature and public sequence, structural and genomic resources. Select analyses that answer the decisive question; this is not a general gene review. Assess support and contrary evidence, and allow an unresolved outcome. Distinguish directly observed horse evidence, justified mammalian transfer, and results for a different protein model.

  Do not consult the ai-gene-review repository's existing judgments, research syntheses or local bioinformatics analyses. Those are held out for comparison. Do not use agreement with ARBA or another prediction as biological validation. Preserve reproducible methods, accessions/versions, actual computation outputs and primary-source URLs/DOIs/PMIDs. Report the decisive findings and limitations, not just a verdict.
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
**Generated:** 2026-09-08T16:12:21.588630

1. PMID:21454751
2. PMID:16169490
3. PMID:23616086
4. PMID:20083600
5. PMID:10790391
6. PMID:40830301