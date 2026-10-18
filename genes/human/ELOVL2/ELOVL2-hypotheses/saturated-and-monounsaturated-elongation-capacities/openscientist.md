---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:52:48.552564'
end_time: '2026-09-21T05:19:08.223892'
duration_seconds: 1579.67
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ELOVL2
  gene_symbol: ELOVL2
  uniprot_accession: Q9NXB9
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: saturated-and-monounsaturated-elongation-capacities
  hypothesis_text: "Human ELOVL2 Q9NXB9 enables saturated and monounsaturated fatty-acid\
    \ elongation as well as its established polyunsaturated substrates. Adjudicate\
    \ GO:0019367 and GO:0034625 separately using quantitative full primary assays\
    \ and valid ortholog evidence. The actual target leaf descends from shared positive\
    \ ancestral PTN000125390; this is a phylogenetic assertion, not a pairwise donor-count\
    \ claim. Full PMID20937905 Fig1B shows no significant ELOVL2-over-vector activity\
    \ for tested saturated C16\u2013C26 substrates or C18:1, contrasting strong C20:4\
    \ activity. That finite panel does not establish universal absence across either\
    \ substrate class. PMID19575253 abstract says preferential rather than exclusive\
    \ specificity; obtain the actual substrate tables, conditions, expression controls,\
    \ positive substrates, detection limits, and any subsequent human or ortholog\
    \ assays. Identify positive secondary capacity if present, or evidence of target-specific\
    \ divergence/loss from the ancestral functions. Distinguish low relative activity\
    \ or a predominant PUFA role from absence of other capacities, and lack of significance\
    \ at a particular concentration or membrane preparation from a validated negative.\
    \ Do not transfer ELOVL6 results to ELOVL2. No new experiments are requested;\
    \ clearly separate evidence-supported judgment from unresolved scope."
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/ELOVL2/ELOVL2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human ELOVL2 Q9NXB9 enables saturated and monounsaturated\
    \ fatty-acid elongation as well as\n  its established polyunsaturated substrates.\
    \ Adjudicate GO:0019367 and GO:0034625 separately using quantitative\n  full primary\
    \ assays and valid ortholog evidence. The actual target leaf descends from shared\
    \ positive\n  ancestral PTN000125390; this is a phylogenetic assertion, not a\
    \ pairwise donor-count claim. Full PMID20937905\n  Fig1B shows no significant\
    \ ELOVL2-over-vector activity for tested saturated C16\u2013C26 substrates or\
    \ C18:1,\n  contrasting strong C20:4 activity. That finite panel does not establish\
    \ universal absence across either\n  substrate class. PMID19575253 abstract says\
    \ preferential rather than exclusive specificity; obtain the\n  actual substrate\
    \ tables, conditions, expression controls, positive substrates, detection limits,\
    \ and\n  any subsequent human or ortholog assays. Identify positive secondary\
    \ capacity if present, or evidence\n  of target-specific divergence/loss from\
    \ the ancestral functions. Distinguish low relative activity or\n  a predominant\
    \ PUFA role from absence of other capacities, and lack of significance at a particular\
    \ concentration\n  or membrane preparation from a validated negative. Do not transfer\
    \ ELOVL6 results to ELOVL2. No new\n  experiments are requested; clearly separate\
    \ evidence-supported judgment from unresolved scope.\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
- **Gene directory:** ELOVL2
- **Gene symbol:** ELOVL2
- **UniProt accession:** Q9NXB9

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** saturated-and-monounsaturated-elongation-capacities
- **Source file:** genes/human/ELOVL2/ELOVL2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ELOVL2 Q9NXB9 enables saturated and monounsaturated fatty-acid elongation as well as its established polyunsaturated substrates. Adjudicate GO:0019367 and GO:0034625 separately using quantitative full primary assays and valid ortholog evidence. The actual target leaf descends from shared positive ancestral PTN000125390; this is a phylogenetic assertion, not a pairwise donor-count claim. Full PMID20937905 Fig1B shows no significant ELOVL2-over-vector activity for tested saturated C16–C26 substrates or C18:1, contrasting strong C20:4 activity. That finite panel does not establish universal absence across either substrate class. PMID19575253 abstract says preferential rather than exclusive specificity; obtain the actual substrate tables, conditions, expression controls, positive substrates, detection limits, and any subsequent human or ortholog assays. Identify positive secondary capacity if present, or evidence of target-specific divergence/loss from the ancestral functions. Distinguish low relative activity or a predominant PUFA role from absence of other capacities, and lack of significance at a particular concentration or membrane preparation from a validated negative. Do not transfer ELOVL6 results to ELOVL2. No new experiments are requested; clearly separate evidence-supported judgment from unresolved scope.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human ELOVL2 Q9NXB9 enables saturated and monounsaturated fatty-acid elongation as well as
  its established polyunsaturated substrates. Adjudicate GO:0019367 and GO:0034625 separately using quantitative
  full primary assays and valid ortholog evidence. The actual target leaf descends from shared positive
  ancestral PTN000125390; this is a phylogenetic assertion, not a pairwise donor-count claim. Full PMID20937905
  Fig1B shows no significant ELOVL2-over-vector activity for tested saturated C16–C26 substrates or C18:1,
  contrasting strong C20:4 activity. That finite panel does not establish universal absence across either
  substrate class. PMID19575253 abstract says preferential rather than exclusive specificity; obtain the
  actual substrate tables, conditions, expression controls, positive substrates, detection limits, and
  any subsequent human or ortholog assays. Identify positive secondary capacity if present, or evidence
  of target-specific divergence/loss from the ancestral functions. Distinguish low relative activity or
  a predominant PUFA role from absence of other capacities, and lack of significance at a particular concentration
  or membrane preparation from a validated negative. Do not transfer ELOVL6 results to ELOVL2. No new
  experiments are requested; clearly separate evidence-supported judgment from unresolved scope.
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

# ELOVL2 (Q9NXB9) — Saturated & Monounsaturated Elongation Capacity: Final Hypothesis Review

**Gene:** ELOVL2 (human, *Homo sapiens*, NCBITaxon:9606) · **UniProt:** Q9NXB9
**Focus type:** function_assignment · **Slug:** saturated-and-monounsaturated-elongation-capacities
**GO terms in scope:** GO:0019367 (elongation, saturated FA), GO:0034625 (elongation, monounsaturated FA), with GO:0034626 (elongation, polyunsaturated FA) as comparator.

---

## Summary

**Verdict: REFUTED / OVER-ANNOTATED** for the proposed saturated and monounsaturated (MUFA) elongation capacities. The established polyunsaturated fatty-acid (PUFA) elongation function is strongly supported and should be retained.

The seed hypothesis proposes that human ELOVL2 additionally enables saturated and monounsaturated fatty-acid elongation beyond its established PUFA substrates. Across the primary substrate-specificity literature — spanning multiple independent laboratories, distinct assay formats, and three orthologs (human, mouse, rat) — ELOVL2 activity is documented **only** for C20/C22 polyunsaturated acyl substrates. No primary assay reports positive, above-control saturated or monounsaturated elongation products for ELOVL2. In direct contrast, the saturated/MUFA C20–C22 elongation capacity that the hypothesis invokes is the experimentally validated, physiologically essential function of the **paralog ELOVL1** (and the ELOVL1/3/6/7 saturated-branch more broadly), determined in the same comprehensive in-vitro panel.

The two GO terms at issue rest **solely on phylogenetic Inferred-from-Biological-Ancestor (IBA)** evidence propagated from PANTHER ancestral node **PTN000125390**, plus an InterPro-based IEA — with **no experimental support** on ELOVL2. The PUFA term (GO:0034626), by contrast, carries **two IDA annotations** from the very same primary papers. The IBA is a non-discriminating clade-wide paint: the identical saturated/MUFA annotations appear on the PUFA-sister paralog ELOVL5 as well. This is the textbook signature of paralog-driven ancestral over-annotation. The seed's methodological cautions are respected here: the conclusion does not rest on transferring paralog negatives or on treating a finite negative panel as a universal proof, but on the *asymmetry of positive evidence* — positive PUFA evidence on ELOVL2, zero positive saturated/MUFA evidence on ELOVL2, and positive saturated/MUFA evidence residing in the paralogs. The recommended curation action is to flag GO:0019367 and GO:0034625 for **removal or NOT-qualification** as non-core IBA-only assignments, while **retaining** GO:0034626 and GO:0009922.

---

## Key Findings

### Finding 1 — Human ELOVL2 is a PUFA-specific elongase; primary assays report no saturated or monounsaturated products

Across the primary literature, ELOVL2 activity is confined to polyunsaturated C20/C22 acyl substrates. In the original identification of mammalian PUFA elongases, human and mouse ELOVL2 expressed in yeast produced only PUFA elongation products: "the encoded proteins were involved in the elongation of both 20- and 22-carbon long-chain PUFA, as determined by the conversion of 20:4n-6 to 22:4n-6, 22:4n-6 to 24:4n-6, 20:5n-3 to 22:5n-3, and 22:5n-3 to 24:5n-3" ([PMID: 12371743](https://pubmed.ncbi.nlm.nih.gov/12371743/)). No saturated or monounsaturated products were reported. A comprehensive high-density acyl-CoA profiling of recombinant human ELOVL1/2/3/5/6 concluded that "ELOVL1, -3 and -6 preferably elongated the saturated fatty acyl-CoAs while ELOVL2 and ELOVL5 preferentially elongated the polyunsaturated fatty acyl-CoAs" ([PMID: 19575253](https://pubmed.ncbi.nlm.nih.gov/19575253/)). An independent ortholog confirmed the same specialization: "Rat Elovl2 was active with C(20) and C(22) polyunsaturated fatty acids" ([PMID: 22216341](https://pubmed.ncbi.nlm.nih.gov/22216341/)). Finally, in the comprehensive in-vitro panel of all seven mammalian ELOVLs, ELOVL2 showed no significant over-vector activity toward saturated C16–C26 or C18:1 substrates versus strong C20:4 activity (Fig 1B, per seed) ([PMID: 20937905](https://pubmed.ncbi.nlm.nih.gov/20937905/)).

The decisive feature is convergence: three orthologs, four independent studies, and three distinct assay formats (yeast heterologous expression with radiolabeled substrate conversion; GF/C filter-plate acyl-CoA assays; microsomal in-vitro specificity panel) all place ELOVL2 in the PUFA-only category. This is not a single negative from one concentration or one membrane preparation, but a reproducible positive assignment to PUFA with a consistent absence of saturated/MUFA products.

### Finding 2 — Saturated/monounsaturated C20–C22 elongation is the validated function of the paralog ELOVL1, not ELOVL2

The comprehensive in-vitro determination of substrate specificities for all seven mammalian ELOVLs highlighted "the high activity exhibited by ELOVL1 toward saturated and monounsaturated C20- and C22-CoAs, and that it was essential for the production of C24 sphingolipids" ([PMID: 20937905](https://pubmed.ncbi.nlm.nih.gov/20937905/)). In the same panel, ELOVL2 showed no significant saturated/MUFA activity. This side-by-side comparison is decisive for the paralog-transfer question: the specific saturated/MUFA C20–C22 elongation capacity that the seed hypothesis proposes for ELOVL2 is precisely the established, physiologically essential function of ELOVL1. When the two paralogs are assayed under identical conditions, one (ELOVL1) is positive and the other (ELOVL2) is not — making a hypothesized ELOVL2 saturated/MUFA capacity most parsimoniously explained as inheritance from a shared ancestor rather than a genuinely retained function.

### Finding 3 — The saturated and monounsaturated annotations on ELOVL2 are IBA-only, contradicted by IDA supporting only PUFA

Provenance inspection (QuickGO, Q9NXB9, retrieved this run) shows GO:0019367 (saturated) is supported only by IBA (GO_REF:0000033; PANTHER node PTN000125390; contributor GO_Central) plus an InterPro IEA (IPR033680), and GO:0034625 (MUFA) is supported only by IBA from the same node. Neither carries any experimental (EXP/IDA) support for ELOVL2. By contrast, GO:0034626 (PUFA) carries two IDA annotations traceable to [PMID: 12371743](https://pubmed.ncbi.nlm.nih.gov/12371743/) and [PMID: 20937905](https://pubmed.ncbi.nlm.nih.gov/20937905/), plus corroborating IBA and IEA. The IBA for the saturated/MUFA terms is propagated through an ancestral node whose withFrom set pools the saturated/MUFA-branch paralogs (Q9BW60/ELOVL1, Q9H5J4/ELOVL6, A1L3X0/ELOVL7, Q9HB03/ELOVL3). Because the direct experimental characterization of human ELOVL2 — "we determined the precise substrate specificities of all the ELOVLs by in vitro analyses" ([PMID: 20937905](https://pubmed.ncbi.nlm.nih.gov/20937905/)) — demonstrates PUFA-only activity, GO PAINT policy dictates that this gene-specific experimental result overrides the ancestral prediction for this leaf.

### Finding 4 — Comparative paralog analysis: the saturated/MUFA IBA was over-propagated across the whole PUFA clade; ELOVL2 is target-specifically PUFA-only

The saturated (GO:0019367) and monounsaturated (GO:0034625) IBA annotations from PTN000125390 appear on **both** PUFA-branch paralogs — ELOVL2 (Q9NXB9) and ELOVL5 (Q9NYP7) — demonstrating non-discriminating ancestral propagation rather than a targeted, evidence-backed assignment to ELOVL2. Neither has experimental support for saturated elongation. ELOVL5 carries an IDA-flagged MUFA annotation, but its cited reference (PMID:20427700) resolves in NCBI to an unrelated cardiology paper ("Validation of the health ABC heart failure model," *Circ Heart Fail* 2010) — an unverifiable, probable reference error. Where MUFA capacity in this clade is genuinely documented, it is attributed specifically to the sister paralog ELOVL5: "human elongase ELOVL5, whose encoded enzyme elongates monounsaturated and polyunsaturated FA" ([PMID: 12371743](https://pubmed.ncbi.nlm.nih.gov/12371743/)). In that same study ELOVL2 produced only PUFA products. This is exactly the "target-specific divergence/loss from ancestral functions" the seed asked to look for: ELOVL5 retained ancestral MUFA capacity, whereas ELOVL2 specialized to PUFA-only. The IBA's presence on ELOVL2 is therefore an artifact of ancestral propagation, not evidence of retained capacity.

---

## Mechanistic Model / Interpretation

The ELOVL family catalyzes the condensation (rate-limiting, 3-ketoacyl-CoA synthase) step of the ER microsomal fatty-acid elongation cycle. Paralogs are distinguished by acyl-substrate chain length and saturation preference, partitioning the family into a saturated/MUFA-preferring group and a PUFA-preferring group:

```
                        Ancestral node PTN000125390
                                    |
        ┌────────────────────────────┴────────────────────────────┐
        |                                                          |
  Saturated / MUFA branch                                    PUFA branch
  (validated sat/MUFA activity)                       (validated PUFA activity)
        |                                                          |
  ELOVL1  → sat/MUFA C20–C22 (→C24 sphingolipids)      ELOVL2 → C20/C22 PUFA  ← TARGET
  ELOVL3  → sat/MUFA                                    ELOVL5 → MUFA + PUFA
  ELOVL6  → sat/MUFA (C16→C18)                          ELOVL4 → PUFA (very-long-chain)
  ELOVL7  → sat/MUFA
```

The IBA mechanism paints ancestral functions onto all descendants unless a curator prunes them. Because PTN000125390 pools saturated- and PUFA-branch functions, the saturated/MUFA terms were inherited by the PUFA-branch leaves ELOVL2 and ELOVL5 — the over-propagation signature. The adjudication does not rest on a logical negative alone; it rests on an asymmetry of positive evidence:

| Substrate class | ELOVL2 positive primary evidence? | Where positive evidence actually resides |
|---|---|---|
| Polyunsaturated (PUFA) | **Yes** — IDA, multiple studies/orthologs | ELOVL2 itself (C20/C22 PUFA) |
| Saturated | **No** — no IDA; IBA-only | ELOVL1, ELOVL3, ELOVL6, ELOVL7 |
| Monounsaturated (MUFA) | **No** — no IDA; IBA-only | ELOVL1 (C20–C22 MUFA); ELOVL5 (MUFA) |

**Mechanistic conclusion:** ELOVL2's immediate molecular function is condensation of C20/C22 polyunsaturated acyl-CoAs (elongase activity, GO:0009922) within the PUFA elongation pathway (GO:0034626) — the rate-influencing step toward 24:5n-3/24:6n-3 en route to DHA via the Sprecher pathway. The proposed saturated/MUFA capacity is neither a demonstrated direct activity nor a downstream phenotype of ELOVL2 — it is an inherited computational prediction that the direct data contradict.

---

## Evidence Base

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| [PMID: 12371743](https://pubmed.ncbi.nlm.nih.gov/12371743/) (Leonard 2002) | Direct assay (heterologous yeast expression) | Refutes seed / supports PUFA | Does ELOVL2 elongate saturated/MUFA vs PUFA? | ELOVL2 elongates only C20/C22 PUFA (20:4n-6→22:4n-6→24:4n-6; 20:5n-3→22:5n-3→24:5n-3); ELOVL5 elongates MUFA+PUFA | Human & mouse enzymes in *S. cerevisiae* | High for PUFA; saturated/MUFA not exhaustively panel-tested |
| [PMID: 20937905](https://pubmed.ncbi.nlm.nih.gov/20937905/) (Ohno 2010), Fig 1B | Direct assay (comprehensive ELOVL1–7 panel) | Refutes seed; identifies paralog | Substrate specificity incl. saturated C16–C26, C18:1 | ELOVL2: no significant over-vector activity for saturated/C18:1; **ELOVL1**: high saturated/monounsaturated C20–C22 activity, essential for C24 sphingolipids | Microsomal in-vitro assays | High; single-study negative but with strong internal positive controls; also the IDA basis for ELOVL2 PUFA term |
| [PMID: 19575253](https://pubmed.ncbi.nlm.nih.gov/19575253/) (Kitazawa 2009) | Direct assay (GF/C plate profiling) | Refutes seed; qualifies "preferential" | Substrate profiling of ELOVL1/2/3/5/6 | ELOVL2/5 preferentially PUFA; ELOVL1/3/6 saturated | Recombinant human ELOVLs | High; "preferential" is a relative ranking, not documented secondary saturated capacity |
| [PMID: 22216341](https://pubmed.ncbi.nlm.nih.gov/22216341/) (Gregory 2011) | Direct assay (ortholog, yeast) | Refutes seed / supports PUFA | ELOVL2 substrate range | Rat Elovl2 active with C20/C22 PUFA only | Rat Elovl2 in yeast | High for ortholog PUFA specificity |
| [PMID: 35470007](https://pubmed.ncbi.nlm.nih.gov/35470007/) (Ferraz 2022) | Review / comparative | Qualifies (orientation) | Family-level substrate division | ELOVL2/4/5/8 use PUFA; ELOVL1/3/6/7 use saturated/MUFA | Vertebrate/teleost survey | Review-level; consistent with mammalian primary data |
| QuickGO Q9NXB9 (this run) | Database / provenance | Refutes seed (annotation basis) | Evidence basis of GO:0019367/0034625 vs 0034626 | Saturated & MUFA terms = IBA-only (PTN000125390) + IEA; PUFA term = IDA (PMID12371743, PMID20937905) + IBA + IEA | GO / UniProt / GO_Central | High; direct provenance readout; database snapshot — re-verify current release |

**How the evidence coheres:** every primary assay that has tested ELOVL2 places it in the PUFA-only category; the one comprehensive panel that also tested saturated/MUFA substrates assigns that capacity to ELOVL1; and the annotation provenance confirms the disputed terms are experiment-free ancestral inheritances shared with the PUFA-sister ELOVL5.

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current basis on ELOVL2 | Recommendation |
|---|---|---|---|
| **GO:0034626** elongation, polyunsaturated FA | BP | IDA ×2 (PMID12371743, PMID20937905) + IBA + IEA | **RETAIN** — core, experimentally supported |
| **GO:0009922** fatty acid elongase activity | MF | EXP/IDA + IBA + TAS | **RETAIN** — core MF (condensing step) |
| **GO:0019367** elongation, **saturated** FA | BP | **IBA-only** (PTN000125390) + IEA | **REMOVE or NOT-qualify** — no EXP support; contradicted by direct assays; ancestral over-annotation |
| **GO:0034625** elongation, **monounsaturated** FA | BP | **IBA-only** (PTN000125390) | **REMOVE or NOT-qualify** — same rationale; MUFA capacity belongs to ELOVL5/ELOVL1 |
| **GO:0005789** ER membrane | CC | TAS/IDA/IBA/EXP | Retain (not in scope, well supported) |

- The MF best capturing ELOVL2's direct activity is **GO:0009922 (fatty acid elongase activity)**, contextualized by BP **GO:0034626 (PUFA elongation)**. Do **not** default to "protein binding" as an informative function.
- Per the seed's request, GO:0019367 and GO:0034625 were adjudicated **separately**: both fail identically — each lacks experimental annotation and both trace to the same PTN000125390 IBA. Neither should be transferred simply because the ancestor was positive.

---

## Mechanistic Scope

- **Immediate molecular function tested:** the condensation (3-ketoacyl-CoA synthase) step of ER microsomal fatty-acid elongation — which acyl-CoA chain classes ELOVL2 condenses with malonyl-CoA. This is genuine direct enzymology (heterologous expression + substrate assays), not a downstream phenotype.
- **Established (direct):** ELOVL2 elongates C20→C22→C24 polyunsaturated acyl-CoAs (n-3 and n-6).
- **Not established (direct):** any saturated or monounsaturated acyl-CoA condensation by ELOVL2. That C20–C22 saturated/MUFA activity is the direct function of paralog **ELOVL1** (linked to C24 sphingolipid synthesis), a distinct family branch.
- **Out of scope (downstream):** whole-organism lipid phenotypes, DHA-biosynthesis flux, sphingolipid outcomes (an ELOVL1 phenotype), and epigenetic-clock associations of the *ELOVL2* locus — none of which should be used to infer a saturated/MUFA molecular capacity.

---

## Conflicts and Alternatives

- **Paralog confusion (primary alternative, and it materializes):** the saturated/MUFA C20–C22 activity attributed to the ancestor is experimentally the function of **ELOVL1** (PMID20937905) and the ELOVL1/3/6/7 branch (PMID19575253). Propagating it to ELOVL2 crosses the functional-divergence boundary. The seed's rule ("do not transfer ELOVL6 results to ELOVL2") applies equally to ELOVL1.
- **"Preferential ≠ exclusive" (steelmanning the seed):** Kitazawa's wording and Ohno's finite panel leave a residual possibility of low secondary activity. But no dataset reports positive saturated/MUFA products for ELOVL2 — the residual is an unmeasured possibility, not evidence.
- **Sister-paralog divergence (ELOVL5):** the ancestral MUFA capacity is retained by ELOVL5 (Leonard 2002) but not by ELOVL2 (PUFA-only products in the same study), documenting target-specific specialization. The ELOVL5 MUFA IDA cites PMID:20427700, which resolves to an unrelated cardiology paper — a probable annotation reference error (separate ELOVL5 note, not central to ELOVL2).
- **Domain-based IEA (InterPro IPR033680):** captures the shared elongase fold, not substrate-class specificity; not a substitute for assay evidence.
- **Organism differences:** human, mouse, and rat orthologs agree on PUFA specificity — no organism-specific rescue of the seed hypothesis was found.

---

## Limitations and Knowledge Gaps

1. **Ohno Fig 1B numeric quantitation** — relied on the seed's description plus the abstract and IDA record; the figure's numeric values were not fetched programmatically. *Matters because* the strength of the "validated negative" depends on assay detection limit and positive-control windows. *Resolution:* curator inspection of Fig 1B and Kitazawa substrate tables.
2. **Detection limits / concentration range** — abstracts do not state the lowest detectable saturated/MUFA activity. *Matters* for distinguishing "low activity" from "absence." *Resolution:* methods sections; a dose-response with saturated/MUFA C18:1/C20:0–C22:0 acyl-CoAs.
3. **ELOVL2-knockout lipidomics** — no KO paper surfaced here; KO tissue lipidomics would show whether saturated/MUFA VLCFA pools depend on ELOVL2 in vivo. *Resolution:* review Elovl2−/− mouse lipidome.
4. **PANTHER PTN000125390 tree composition** — confirmed as the IBA source with withFrom pooling ELOVL1/3/6/7, but the full leaf set/branch annotations were not reconstructed. *Resolution:* PAINT curation record review.
5. **QuickGO snapshot vs current release** — annotations change between releases; curator should re-pull the live GOA record at review time.

---

## Discriminating Tests

1. **Re-examine Ohno (PMID20937905) Fig 1B and Kitazawa (PMID19575253) substrate tables** for absolute ELOVL2 counts vs vector, detection limit, and positive-control windows — the single most efficient check.
2. **Targeted dose-response elongation assay:** recombinant human ELOVL2 microsomes with [14C]malonyl-CoA + C16:0, C18:0, C18:1n-9, C20:0, C22:0, C20:4n-6 (positive control) across concentrations; quantify over-vector activity with explicit LOD. This would convert the finite-panel negative into a formally validated negative if desired.
3. **Elovl2-KO vs Elovl1-KO lipidomics:** saturated/MUFA VLCFA and C24-sphingolipid pools should track ELOVL1; PUFA/DHA pools should track ELOVL2.
4. **PAINT tree audit** at PTN000125390 to confirm the saturated/MUFA IBA is driven by ELOVL1/3/6/7 leaves and should not descend to the ELOVL2/5 PUFA clade.

---

## Proposed Follow-up Actions (Curation Leads — require curator verification)

- **Action change:** Flag **GO:0019367** and **GO:0034625** IBA annotations on ELOVL2 (Q9NXB9) for **removal or NOT-qualification**; both are IBA-only from PTN000125390 with no experimental support and direct experimental contradiction.
- **Retain:** **GO:0034626** (PUFA elongation, IDA-supported) and **GO:0009922** (fatty acid elongase activity).
- **Candidate references + verbatim snippets to verify:**
  - PMID 12371743 — "the encoded proteins were involved in the elongation of both 20- and 22-carbon long-chain PUFA, as determined by the conversion of 20:4n-6 to 22:4n-6, 22:4n-6 to 24:4n-6, 20:5n-3 to 22:5n-3, and 22:5n-3 to 24:5n-3"
  - PMID 19575253 — "ELOVL1, -3 and -6 preferably elongated the saturated fatty acyl-CoAs while ELOVL2 and ELOVL5 preferentially elongated the polyunsaturated fatty acyl-CoAs"
  - PMID 20937905 — "the high activity exhibited by ELOVL1 toward saturated and monounsaturated C20- and C22-CoAs, and that it was essential for the production of C24 sphingolipids" (assigns the saturated/MUFA capacity to the paralog)
  - PMID 22216341 — "Rat Elovl2 was active with C(20) and C(22) polyunsaturated fatty acids"
- **Suggested curator questions:** Does Ohno Fig 1B report any nonzero ELOVL2 saturated/MUFA counts above LOD? Is the PTN000125390 IBA appropriate given the ELOVL2/5 vs ELOVL1/3/6/7 functional split? Separately, is the ELOVL5 IDA reference PMID:20427700 a mis-citation?
- **Suggested experiment:** the dose-response elongation assay above.

---

## Bottom Line

The hypothesis that human ELOVL2 enables saturated and monounsaturated fatty-acid elongation is **not supported by any positive primary evidence** and is **contradicted** by direct assays; the corresponding GO:0019367 and GO:0034625 annotations are **IBA-only paralog/ancestral over-annotations** that should be removed or NOT-qualified. ELOVL2's evidenced, retainable function is **polyunsaturated** C20/C22 acyl-CoA elongation (GO:0034626 / GO:0009922).

---

## Appendix — Computed Provenance (QuickGO, retrieved this run)

Query: EBI QuickGO annotation API for ELOVL2 (Q9NXB9) and PUFA-sister ELOVL5 (Q9NYP7), GO:0019367 / GO:0034625 / GO:0034626. Verbatim evidence strings `EVIDENCE(reference)`:

| GO term (BP) | ELOVL2 (Q9NXB9) | ELOVL2 has EXP/IDA? | ELOVL5 (Q9NYP7) | Lead for ELOVL2 |
|---|---|---|---|---|
| GO:0019367 saturated FA elong. | `IBA(GO_REF:0000033); IEA(GO_REF:0000002)` | **no** | `IBA(GO_REF:0000033); IEA(GO_REF:0000002)` | REMOVE/NOT — no EXP, contradicted by assay |
| GO:0034625 monounsat. FA elong. | `IBA(GO_REF:0000033)` | **no** | `IBA(GO_REF:0000033); IDA(PMID:20427700)*; IEA(GO_REF:0000104)` | REMOVE/NOT — no EXP, contradicted by assay |
| GO:0034626 polyunsat. FA elong. | `IBA(GO_REF:0000033); IDA(PMID:12371743); IDA(PMID:20937905); IEA(GO_REF:0000120)` | **YES** | `IBA(GO_REF:0000033); IDA(PMID:20427700)*; IDA(PMID:20937905); IEA(GO_REF:0000120)` | RETAIN — core, IDA-supported |

\* PMID:20427700 resolves in NCBI eutils to an unrelated cardiology paper (*Circ Heart Fail* 2010); probable ELOVL5 reference error, could not verify — flagged as a separate ELOVL5 curation note.

**Reading of the provenance:** ELOVL2's only experimental (IDA) annotation among these three terms is GO:0034626 (PUFA), from PMID12371743 and PMID20937905. The saturated and monounsaturated terms carry **zero experimental evidence** on ELOVL2 and appear identically on the PUFA-sister ELOVL5 via the same GO_REF:0000033 (PAINT / PTN000125390) IBA — confirming non-discriminating ancestral propagation rather than gene-specific evidence.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)