# AIGR IBA-Support Deep Research

You are searching for **independent literature support** for a single GO
annotation that is currently assigned to a gene **only by phylogenetic
inference** (evidence code IBA, propagated from PANTHER `GO_REF:0000033`). IBA
annotations are not, by themselves, experimental evidence — your job is to find
primary (or well-justified orthologous) evidence that confirms or refutes the
annotation for this specific gene.

This is not a general gene overview, and it is not a re-litigation of the GO
curation decision. Stay tightly focused on the one annotation below.

## Target Gene

- **Organism code:** {organism}
- **Taxon:** {taxon_label} ({taxon_id})
- **Gene directory:** {gene}
- **Gene symbol:** {gene_symbol}

## Focus

- **Focus type:** {focus_type}
- **Hypothesis slug:** {hypothesis_slug}
- **Source file:** {source_file}
- **Source selector:** {source_selector}

## Seed Hypothesis

{hypothesis_text}

## Annotation Context

{term_context}

## Reference Context

{reference_context}

## Source Context YAML

```yaml
{source_context_yaml}
```

## Research Objective

Find the strongest available **independent** evidence bearing on whether this
GO term genuinely applies to {gene_symbol}. Prioritise, in order:

1. Direct experimental evidence in {gene_symbol} itself (the annotated gene in
   the annotated organism): assays, mutant phenotypes, localisation,
   interactions, structures.
2. Direct experimental evidence in a clearly orthologous gene, where the
   orthology is well established and the function is expected to be conserved.
3. Strong indirect or computational evidence (domain architecture, conserved
   motifs, structural homology, operon/pathway context), reported
   conservatively.

Prefer **PMID** citations; include **DOI** citations when no PMID is available.
Treat reviews and database records as orientation only — cite the underlying
primary papers wherever possible.

**Expect false positives.** This pipeline is tuned for recall, so a downstream
curator/agent will sift your results. For every candidate you must therefore
provide an **exact verbatim snippet** from the source that a curator can check,
plus enough context (organism, assay, gene actually studied) to detect paralog
confusion, wrong-organism carry-over, or claims that are really about a
different gene.

## Required Output

### Executive Judgment

State whether independent support exists: **supported** (with strong primary
evidence), **partially / indirectly supported**, **unresolved** (no independent
evidence found), or **refuted**. One short paragraph; lead with the verdict.

### Evidence Matrix

A table with one row per candidate evidence item:

- Citation (PMID preferred; DOI otherwise)
- Gene/protein actually studied (and organism) — flag if it is an ortholog or a paralog
- Evidence type (direct assay, mutant phenotype, localization, interaction, structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies
- Exact verbatim snippet to verify (quote the source)
- Key finding in your own words
- Confidence and the most important caveat (false-positive risk)

### Best Supporting References

List the 1–3 references most suitable to add to the review's `supported_by`
for this annotation, each with the exact snippet a curator should confirm. If
none qualify, say so explicitly.

### Conflicts and Alternatives

Note any evidence that contradicts the annotation or that points to paralog
confusion, organism-specific differences, isoform-specific findings, or
database carry-over.

### Knowledge Gaps

If no adequate independent evidence exists, state what was searched, why the gap
matters, and what evidence or experiment would resolve it.
