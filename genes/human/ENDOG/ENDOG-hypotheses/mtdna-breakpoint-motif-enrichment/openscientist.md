---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-26T20:53:21.972766'
end_time: '2026-10-26T21:15:48.028332'
duration_seconds: 1346.06
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ENDOG
  gene_symbol: ENDOG
  uniprot_accession: Q14249
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: mtdna-breakpoint-motif-enrichment
  hypothesis_text: 'Human ENDOG''s cleavage-site preferences explain where mitochondrial
    DNA breakpoints fall: breakpoints of nuclear mitochondrial insertions (NUMTs)
    and of mtDNA deletions are enriched at G-quadruplex-forming and C-rich motifs
    in the mitochondrial genome, relative to position- and composition-matched control
    sites.'
  term_context: '- This must be a computational analysis on sequence and coordinate
    data, not a literature review. Compute, do not cite: scan the human mitochondrial
    reference sequence (rCRS, NC_012920.1) for G-quadruplex propensity (e.g. G4Hunter)
    and for the C-rich motifs ENDOG is reported to cleave, then test whether published
    mtDNA breakpoint coordinates fall at those motifs more often than position- and
    base-composition-matched control sites. Report the test used, effect size and
    p-value.

    - Breakpoint coordinate sources to use if obtainable: the NUMT catalogue of 1637
    NUMTs across 66083 genomes (PMID:36198798, supplementary tables give mtDNA coordinates);
    MITOMAP''s mtDNA deletion breakpoint table; and the common 9 bp deletion hotspot
    at mtDNA 8271-8281. Per-individual NUMT genotypes are UK Biobank controlled-access
    and are NOT needed: this tests where breakpoints sit in the mtDNA sequence, not
    who carries them.

    - Biological background for the motifs, already established, do not re-derive:
    human ENDOG prefers oxidatively damaged, nicked and gapped DNA (PMID:41854021);
    it binds G-quadruplex structures at the 9 bp deletion hotspot and induces breaks
    there (PMID:36394256); in mouse it cleaves C-rich motifs in a mitochondrial transcript
    (PMID:39752519); and yeast EndoG limits transfer of long mtDNA to the nucleus
    (PMID:39227600).

    - State clearly if the breakpoint coordinate data cannot be obtained programmatically,
    and in that case report the motif scan alone rather than substituting a literature
    summary. A negative result, no enrichment over matched controls, is a valid and
    useful outcome.'
  reference_context: '- PMID:36198798

    - PMID:36394256

    - PMID:39752519

    - PMID:41854021

    - PMID:39227600'
  source_file: genes/human/ENDOG/ENDOG-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human ENDOG''s cleavage-site preferences explain\
    \ where mitochondrial DNA breakpoints fall:\n  breakpoints of nuclear mitochondrial\
    \ insertions (NUMTs) and of mtDNA deletions are enriched at G-quadruplex-forming\n\
    \  and C-rich motifs in the mitochondrial genome, relative to position- and composition-matched\
    \ control\n  sites.'\nfocus_type: free_text\ncontext:\n- 'This must be a computational\
    \ analysis on sequence and coordinate data, not a literature review. Compute,\n\
    \  do not cite: scan the human mitochondrial reference sequence (rCRS, NC_012920.1)\
    \ for G-quadruplex propensity\n  (e.g. G4Hunter) and for the C-rich motifs ENDOG\
    \ is reported to cleave, then test whether published mtDNA\n  breakpoint coordinates\
    \ fall at those motifs more often than position- and base-composition-matched\
    \ control\n  sites. Report the test used, effect size and p-value.'\n- 'Breakpoint\
    \ coordinate sources to use if obtainable: the NUMT catalogue of 1637 NUMTs across\
    \ 66083 genomes\n  (PMID:36198798, supplementary tables give mtDNA coordinates);\
    \ MITOMAP''s mtDNA deletion breakpoint table;\n  and the common 9 bp deletion\
    \ hotspot at mtDNA 8271-8281. Per-individual NUMT genotypes are UK Biobank\n \
    \ controlled-access and are NOT needed: this tests where breakpoints sit in the\
    \ mtDNA sequence, not who\n  carries them.'\n- 'Biological background for the\
    \ motifs, already established, do not re-derive: human ENDOG prefers oxidatively\n\
    \  damaged, nicked and gapped DNA (PMID:41854021); it binds G-quadruplex structures\
    \ at the 9 bp deletion\n  hotspot and induces breaks there (PMID:36394256); in\
    \ mouse it cleaves C-rich motifs in a mitochondrial\n  transcript (PMID:39752519);\
    \ and yeast EndoG limits transfer of long mtDNA to the nucleus (PMID:39227600).'\n\
    - State clearly if the breakpoint coordinate data cannot be obtained programmatically,\
    \ and in that case\n  report the motif scan alone rather than substituting a literature\
    \ summary. A negative result, no enrichment\n  over matched controls, is a valid\
    \ and useful outcome.\nreference_id:\n- PMID:36198798\n- PMID:36394256\n- PMID:39752519\n\
    - PMID:41854021\n- PMID:39227600"
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
citation_count: 5
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** ENDOG
- **Gene symbol:** ENDOG
- **UniProt accession:** Q14249

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** mtdna-breakpoint-motif-enrichment
- **Source file:** genes/human/ENDOG/ENDOG-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ENDOG's cleavage-site preferences explain where mitochondrial DNA breakpoints fall: breakpoints of nuclear mitochondrial insertions (NUMTs) and of mtDNA deletions are enriched at G-quadruplex-forming and C-rich motifs in the mitochondrial genome, relative to position- and composition-matched control sites.

## Term and Decision Context

- This must be a computational analysis on sequence and coordinate data, not a literature review. Compute, do not cite: scan the human mitochondrial reference sequence (rCRS, NC_012920.1) for G-quadruplex propensity (e.g. G4Hunter) and for the C-rich motifs ENDOG is reported to cleave, then test whether published mtDNA breakpoint coordinates fall at those motifs more often than position- and base-composition-matched control sites. Report the test used, effect size and p-value.
- Breakpoint coordinate sources to use if obtainable: the NUMT catalogue of 1637 NUMTs across 66083 genomes (PMID:36198798, supplementary tables give mtDNA coordinates); MITOMAP's mtDNA deletion breakpoint table; and the common 9 bp deletion hotspot at mtDNA 8271-8281. Per-individual NUMT genotypes are UK Biobank controlled-access and are NOT needed: this tests where breakpoints sit in the mtDNA sequence, not who carries them.
- Biological background for the motifs, already established, do not re-derive: human ENDOG prefers oxidatively damaged, nicked and gapped DNA (PMID:41854021); it binds G-quadruplex structures at the 9 bp deletion hotspot and induces breaks there (PMID:36394256); in mouse it cleaves C-rich motifs in a mitochondrial transcript (PMID:39752519); and yeast EndoG limits transfer of long mtDNA to the nucleus (PMID:39227600).
- State clearly if the breakpoint coordinate data cannot be obtained programmatically, and in that case report the motif scan alone rather than substituting a literature summary. A negative result, no enrichment over matched controls, is a valid and useful outcome.

## Reference Context

- PMID:36198798
- PMID:36394256
- PMID:39752519
- PMID:41854021
- PMID:39227600

## Source Context YAML

```yaml
hypothesis: 'Human ENDOG''s cleavage-site preferences explain where mitochondrial DNA breakpoints fall:
  breakpoints of nuclear mitochondrial insertions (NUMTs) and of mtDNA deletions are enriched at G-quadruplex-forming
  and C-rich motifs in the mitochondrial genome, relative to position- and composition-matched control
  sites.'
focus_type: free_text
context:
- 'This must be a computational analysis on sequence and coordinate data, not a literature review. Compute,
  do not cite: scan the human mitochondrial reference sequence (rCRS, NC_012920.1) for G-quadruplex propensity
  (e.g. G4Hunter) and for the C-rich motifs ENDOG is reported to cleave, then test whether published mtDNA
  breakpoint coordinates fall at those motifs more often than position- and base-composition-matched control
  sites. Report the test used, effect size and p-value.'
- 'Breakpoint coordinate sources to use if obtainable: the NUMT catalogue of 1637 NUMTs across 66083 genomes
  (PMID:36198798, supplementary tables give mtDNA coordinates); MITOMAP''s mtDNA deletion breakpoint table;
  and the common 9 bp deletion hotspot at mtDNA 8271-8281. Per-individual NUMT genotypes are UK Biobank
  controlled-access and are NOT needed: this tests where breakpoints sit in the mtDNA sequence, not who
  carries them.'
- 'Biological background for the motifs, already established, do not re-derive: human ENDOG prefers oxidatively
  damaged, nicked and gapped DNA (PMID:41854021); it binds G-quadruplex structures at the 9 bp deletion
  hotspot and induces breaks there (PMID:36394256); in mouse it cleaves C-rich motifs in a mitochondrial
  transcript (PMID:39752519); and yeast EndoG limits transfer of long mtDNA to the nucleus (PMID:39227600).'
- State clearly if the breakpoint coordinate data cannot be obtained programmatically, and in that case
  report the motif scan alone rather than substituting a literature summary. A negative result, no enrichment
  over matched controls, is a valid and useful outcome.
reference_id:
- PMID:36198798
- PMID:36394256
- PMID:39752519
- PMID:41854021
- PMID:39227600
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

# ENDOG mtDNA-breakpoint motif-enrichment hypothesis — Deep Research Report

**Gene:** ENDOG (Q14249), *Homo sapiens* (NCBITaxon:9606)
**Hypothesis slug:** `mtdna-breakpoint-motif-enrichment`
**Focus type:** free_text (computational analysis on sequence + coordinate data)
**Date:** 2026-10-26

> **Seed hypothesis.** Human ENDOG's cleavage-site preferences explain where mitochondrial
> DNA breakpoints fall: breakpoints of nuclear mitochondrial insertions (NUMTs) **and** of
> mtDNA deletions are enriched at G-quadruplex-forming and C-rich motifs in the mitochondrial
> genome, relative to position- and composition-matched control sites.

This was executed as a **computation on sequence and coordinate data**, not a literature review.
All breakpoint coordinate sources named in the seed context were obtained programmatically.

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED, and over-interpreted as stated — the NUMT arm is REFUTED and the
deletion arm is a direct-repeat confound rather than evidence of ENDOG causation.**

- **mtDNA deletions:** breakpoints *are* statistically enriched at G4-forming / C-rich motifs,
  even after matching local GC composition (local max|G4Hunter| fold ≈ 1.17, z = +13, p < 1e-4;
  robust across G4Hunter windows and a stringent ±1 kb local null). **However**, a direct-repeat
  stratification shows the entire signal comes from **repeat-mediated deletions** (DR ≥ 5 bp:
  fold 1.24, z = +16) and **disappears in non-repeat deletions** (DR < 5 bp: fold 0.97, p = 0.91).
  mtDNA direct repeats are themselves G/C-rich, so the "motif" enrichment is **collinear with the
  classical slipped-replication / direct-repeat mechanism** and does not isolate ENDOG cleavage.
- **NUMTs:** No enrichment at G4/C-rich motifs over GC-matched controls, in **three independent
  datasets** — the exact 66,083-genome catalogue named in the seed (PMID:36198798 germline, z = +0.3,
  p = 0.39; somatic, p = 0.10) and the UCSC NumtS set (p = 0.59). The seed's NUMT claim is **refuted**.

**Curation bottom line:** This computational result should **not** be used to assign ENDOG a
mtDNA-breakpoint-determining function. It demonstrates *co-localization* of deletion breakpoints with
G/C-rich, repeat-prone sequence — a long-known property of mtDNA deletions — not a specific,
ENDOG-attributable cleavage signature. The enrichment is real but non-discriminating; the NUMT
prediction is wrong.

---

## Computed Results (primary provenance)

GC-composition-matched permutation null (10 GC deciles, 10,000 permutations); statistic = local
max|G4Hunter| (window 25, ±5 bp slack) and local C-fraction (window 25). Reference: rCRS NC_012920.1
(16,569 bp; reference/light strand is C-rich: C = 31.3 %, G = 13.1 %, so **negative G4Hunter =
C-rich on the reference = G4-forming potential on the complementary heavy strand**).

| Breakpoint set | n positions | max\|G4\| obs | null | fold | z | p | C-frac fold | C-frac z | C-frac p |
|---|---|---|---|---|---|---|---|---|---|
| mtDNA deletions (MitoBreak, all) | 1963 | 0.794 | 0.680 | **1.168** | +13.0 | 1e-4 | 1.080 | +12.3 | 1e-4 |
| — deletions: direct-repeat DR≥5 bp | 1483 | 0.847 | 0.685 | **1.237** | +16.2 | 1e-4 | 1.115 | +15.5 | 1e-4 |
| — deletions: non-repeat DR<5 bp | 609 | 0.647 | 0.667 | **0.969** | −1.4 | 0.91 | 0.973 | −2.3 | 0.99 |
| NUMT germline (PMID:36198798 T1) | 2758 | 0.670 | 0.669 | 1.003 | +0.2 | 0.40 | 1.009 | +1.6 | 0.051 |
| NUMT somatic (PMID:36198798 T4) | 628 | 0.681 | 0.662 | 1.029 | +1.3 | 0.10 | 1.018 | +1.5 | 0.068 |
| NUMT UCSC NumtS | 1195 | 0.638 | 0.640 | 0.997 | −0.2 | 0.59 | 0.994 | −0.7 | 0.75 |

Supporting robustness (deletions, all):
- **Parameter sweep:** fold 1.14–1.28 across G4Hunter windows 15/25/35 × ±0/5/10 bp slack, all p ≈ 2e-4.
- **Stringent local null (±1 kb):** breakpoints sit at the 57th percentile (median 60th) of G4
  propensity *within their own neighborhood* (Wilcoxon p = 2.8e-23) → not purely a regional-composition artifact.
- **Mann–Whitney vs whole genome:** deletions p = 4.4e-43; NUMTs (germline) p = 0.015 (unmatched,
  dissolves under GC-matching).
- **Known hotspots sit at extreme motifs:** 9 bp deletion hotspot 8271–8281 max|G4| = 2.0 (99.8th
  genome percentile); CSB2 (99.9th); common 4977-del 5′ 8470–8482 (96.9th), 3′ 13447–13459 (90.3th).
  These are all direct-repeat-flanked deletions, i.e., the hotspot G/C-richness *is* the repeat.
- **Direct-repeat prevalence:** 69.9 % of the 1,369 deletion pairs have a ≥5 bp perfect repeat at the
  junction (median 5 bp), consistent with the known microhomology/direct-repeat mechanism.

Data provenance (all fetched programmatically this run):
- rCRS: NCBI efetch `NC_012920.1`.
- mtDNA deletions: MitoBreak human `Del` table (1,369 pairs → 1,963 unique breakpoints).
- NUMTs: Springer static-content supplementary of PMID:36198798 (`MOESM4_ESM.xlsx`, Suppl. Tables 1 & 4);
  UCSC hg19 `numtSMitochondrion` track (766 features → 1,195 boundaries).

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| This analysis (MitoBreak + rCRS) | Computational | Qualifies | Deletion breakpoints enriched at G4/C-rich motifs vs matched controls | Fold 1.17, z +13, p<1e-4, GC-matched; robust to params and local null | Human mtDNA deletions, 1,963 positions | High for association; cannot attribute to ENDOG |
| This analysis (DR stratification) | Computational | Competing/Refutes causal reading | Is the enrichment independent of direct repeats? | Signal only in DR≥5 bp deletions (fold 1.24); absent in DR<5 bp (fold 0.97, p=0.91) | Human mtDNA deletions | High; LCS proxy for repeats (±15 bp) |
| This analysis (PMID:36198798 T1/T4) | Computational | Refutes | NUMT breakpoints enriched at G4/C-rich motifs | No enrichment after GC-matching (germline p=0.39; somatic p=0.10) | 1,637 germline + 379 somatic NUMTs, 66,083 genomes | High; authoritative intended dataset |
| This analysis (UCSC NumtS) | Computational | Refutes | NUMT breakpoints enriched (replication) | No enrichment (p=0.59) | 766 NUMTs | High; independent dataset |
| PMID:36198798 (Suppl. Table 6) | Database/computational (their own) | Qualifies | Breakpoint trinucleotide motif enrichment | Mixed: C-rich (CCC p=2e-5, ACC p=4e-7) *and* AT-rich (TTT p=7e-5, ATT p=4e-5) | NUMT mtDNA/nuclear breakpoints | Microhomology signal, not clean G4/C-rich |
| PMID:36394256 | Direct assay (cited background) | Supports (motif biology) | ENDOG binds G4 at 9 bp hotspot, induces breaks | Provides the mechanistic rationale for motif relevance | Human, in vitro/cell | Not re-derived here; motif biology taken as given |
| PMID:39752519 | Direct assay (cited background) | Supports (motif biology) | ENDOG cleaves C-rich motifs | Mouse mitochondrial transcript, C-rich | Mouse | Organism/substrate-specific (RNA context) |
| PMID:41854021 | Direct assay (cited background) | Qualifies | ENDOG prefers oxidatively-damaged/nicked/gapped DNA | Primary determinant may be lesion/structure, not plain sequence motif | Human, in vitro | Suggests damage, not motif, drives site selection |
| PMID:39227600 | Mutant phenotype (cited background) | Competing | Yeast EndoG limits long-mtDNA→nucleus transfer | If conserved, predicts ENDOG shapes NUMT ends — not supported by human NUMT coords | *S. cerevisiae* | Organism-specific; human NUMT test is null |

---

## GO Curation Implications (leads — require curator verification)

- **Do NOT create/assign a BP term implying ENDOG determines mtDNA breakpoint/NUMT positions**
  (e.g., nothing like "regulation of mitochondrial genome rearrangement / NUMT formation via
  sequence-specific cleavage"). The computational enrichment does not support an ENDOG-specific,
  motif-driven breakpoint-placement function; the deletion signal is a direct-repeat confound and
  the NUMT prediction is refuted.
- **Molecular function:** Evidence (cited, not re-derived) supports ENDOG's core MF as a
  **nuclease acting on structured/damaged DNA** — candidates such as `endonuclease activity`
  (GO:0004519) / `deoxyribonuclease activity` (GO:0004536), and possibly `G-quadruplex DNA binding`
  (GO:0051880) on the strength of PMID:36394256. These are MF claims about the *enzyme*, independent
  of the breakpoint-enrichment hypothesis, and should be curated from the primary assays, not from
  this coordinate analysis.
- **This analysis is best logged as negative/qualifying computational context**, not as an IEA/ISS
  basis for any term. Prefer: retain existing experimentally-supported nuclease MF terms; **do not**
  add a breakpoint-placement BP term on the basis of motif co-localization.
- Avoid "protein binding" as a recommendation; a more informative supported MF is the nuclease /
  G4-binding activity above (from primary literature, pending curator check of those PMIDs).

---

## Mechanistic Scope

- **Immediate molecular activity under test:** sequence/structure-specific DNA cleavage by ENDOG
  (G4-forming / C-rich motif preference). The analysis probes whether *where breakpoints sit in the
  mtDNA sequence* matches ENDOG's reported preference.
- **What the data actually show:** a statistical **association** between mtDNA *deletion* breakpoints
  and G/C-rich, G4-prone, **direct-repeat** sequence. This is a property of the breakpoints' genomic
  neighborhood, not a demonstration that ENDOG cut there.
- **Downstream / not tested here:** actual deletion/NUMT formation, replication-slippage vs
  nuclease-cut causation, ENDOG loss-of-function effects on breakpoint spectra, disease phenotypes.
  The enrichment is agnostic to which nuclease (if any) acts; direct-repeat replication slippage
  explains the same localization without invoking ENDOG.

---

## Conflicts and Alternatives

1. **Direct-repeat mechanism (strongest competing explanation).** 70 % of deletions are flanked by
   ≥5 bp repeats; the motif enrichment is entirely within this class. mtDNA deletion hotspots have
   long been attributed to direct/imperfect repeats and replication slippage — a mechanism that does
   not require ENDOG and fully accounts for the observed G/C-rich localization.
2. **NUMT arm contradicted by its own source.** The 66,083-genome catalogue shows no G4/C-rich
   enrichment after composition matching; its trinucleotide table is dominated by low-complexity
   microhomology (AT- and C-rich), consistent with non-homologous end joining at the nuclear insertion
   site rather than ENDOG motif cleavage in mtDNA.
3. **Substrate determinant may be damage, not sequence (PMID:41854021).** If ENDOG's site selection is
   driven by oxidative lesions / nicks / gaps, a static reference-sequence motif scan cannot capture it —
   the negative/confounded motif result is expected even if ENDOG is biologically involved.
4. **Organism / substrate specificity.** The C-rich cleavage evidence is mouse (PMID:39752519) and in an
   RNA/transcript context; the yeast transfer-limiting role (PMID:39227600) is species-specific. Neither
   licenses a human DNA-breakpoint-placement claim.
5. **Composition collinearity.** G4 propensity, C-richness, and GC content are mutually correlated in the
   GC-skewed major arc where deletions cluster; GC-decile matching mitigates but cannot fully disentangle
   these from repeat content.

---

## Knowledge Gaps

- **Causal attribution to ENDOG.** Checked: motif co-localization (association only). Why it matters:
  association ≠ cleavage. Resolve with ENDOG-knockout vs WT mtDNA breakpoint spectra (ChIP/cleavage-seq,
  END-seq, or deletion mapping).
- **Damage-conditioned motif preference.** Checked: static rCRS scan only. Why it matters: ENDOG prefers
  oxidized/nicked DNA (PMID:41854021), invisible to reference-sequence scans. Resolve with in-vitro
  cleavage mapping on damaged mtDNA templates, then test breakpoint overlap.
- **Repeat-independent deletions.** Checked: DR<5 bp subset is null. Why it matters: this is the cleanest
  window to detect an ENDOG-specific motif effect, and it shows none. Resolve with a larger,
  uniformly-ascertained repeat-free deletion set.
- **G4 strand/structure validation.** Checked: G4Hunter propensity (sequence predictor). Why it matters:
  predicted ≠ folded G4. Resolve with experimental G4 maps (BG4 CUT&Tag, G4-seq) on mtDNA and overlap
  with breakpoints.

---

## Discriminating Tests

1. **ENDOG-null vs WT breakpoint spectra** (cells/mouse): if ENDOG drives breakpoint placement, its loss
   should shift/deplete breakpoints at G4/C-rich sites — most informative single experiment.
2. **In-vitro ENDOG cleavage-site mapping** on mtDNA (undamaged vs oxidatively-damaged) → define the true
   human cleavage motif, then test breakpoint overlap (replaces the assumed motif with a measured one).
3. **Repeat-controlled re-analysis** at scale: restrict to repeat-free deletions and NUMTs and ask whether
   *any* residual ENDOG-specific motif survives (this run: none).
4. **Experimental G4 maps (G4-seq / BG4)** on mtDNA to replace G4Hunter predictions and re-test overlap.
5. **Cross-nuclease comparison:** test whether other mitochondrial nucleases' known motifs fit the
   breakpoints equally well — if so, the signal is non-specific.

---

## Curation Leads (require curator verification)

- **Action lead:** Treat the breakpoint-motif hypothesis as **non-core / not curation-actionable for a
  breakpoint-placement function**. Flag the deletion enrichment as **confounded by direct repeats** and
  the NUMT enrichment as **refuted** in the review free-text.
- **Candidate references to verify (exact snippets to pull from primary sources):**
  - PMID:36394256 — verify the specific claim that ENDOG **binds G-quadruplex** at the 9 bp hotspot and
    induces breaks (supports a `G-quadruplex DNA binding` MF, GO:0051880, if the assay is direct).
  - PMID:41854021 — verify ENDOG's preference for **oxidatively-damaged / nicked / gapped DNA**
    (argues site selection is lesion-driven, tempering any pure-motif claim).
  - PMID:36198798 — the authoritative NUMT coordinates used here; Suppl. Table 6 trinucleotide result is
    mixed, not G4/C-rich-specific (supports the refutation).
- **Candidate GO terms (MF, from primary assays — not from this analysis):** `endonuclease activity`
  (GO:0004519) / `deoxyribonuclease activity` (GO:0004536); conditionally `G-quadruplex DNA binding`
  (GO:0051880). **Do not** add a breakpoint-/NUMT-placement BP term.
- **Suggested curator questions:** (i) Is there any *ENDOG-dependent* (knockout-controlled) evidence that
  it determines human mtDNA breakpoint positions? (ii) Does the review already cite the direct-repeat
  mechanism as the explanation for deletion hotspots? (iii) Is the G4-binding claim (PMID:36394256) a
  direct binding/cleavage assay suitable for an MF annotation?
- **Suggested experiment:** ENDOG-null vs WT mtDNA breakpoint mapping (above) as the decisive test.

---

## Limitations

- Reference-sequence motif scan cannot capture damage-conditioned or structure-conditioned cleavage.
- Direct-repeat detection used a longest-common-substring proxy (±15 bp); imperfect repeats and
  microhomology thresholds could shift the exact DR≥5 split, though the qualitative confound is robust.
- G4Hunter predicts, but does not prove, G4 folding.
- MitoBreak aggregates deletions of heterogeneous ascertainment; recurrent hotspots were collapsed to
  unique positions to avoid double-counting (results unchanged).
- No ENDOG perturbation data were available; causation cannot be tested from coordinates alone.

## Conclusion

The seed hypothesis is **partially supported for the descriptive claim** (deletion breakpoints
co-localize with G4/C-rich motifs) but **over-interpreted as an ENDOG function**: the deletion signal is
a **direct-repeat confound** (absent in non-repeat deletions), and the **NUMT arm is refuted** in the
exact 66,083-genome catalogue and a second independent dataset. The analysis should inform the review as
a **negative/qualifying computational result**, not as support for a new ENDOG breakpoint-placement
annotation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)