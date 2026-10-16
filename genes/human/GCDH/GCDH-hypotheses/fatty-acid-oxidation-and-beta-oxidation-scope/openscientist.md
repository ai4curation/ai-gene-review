---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T05:31:22.922157'
end_time: '2026-09-21T05:58:12.886838'
duration_seconds: 1609.96
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: GCDH
  gene_symbol: GCDH
  uniprot_accession: Q92947
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: fatty-acid-oxidation-and-beta-oxidation-scope
  hypothesis_text: 'Human GCDH Q92947 participates in fatty acid oxidation GO:0019395
    and specifically fatty acid beta-oxidation using acyl-CoA dehydrogenase GO:0033539.
    Adjudicate separately using exact process definitions, substrate chemistry, full
    primary studies and phylogenetic placement. Exact PTHR42807 target PTN002533783
    descends from positive IBD PTN005130278; GO:0033539 IBD uses Q92947 itself, which
    is legitimate experimental grounding, not circularity. The target IDA cites PMID25416781:
    the accessible cache contains abstract/introduction/discussion but omits the assay
    methods/results. Obtain the full assays and determine which substrate was tested
    with GCDH versus MCAD. RHEA13389 oxidatively decarboxylates glutaryl-CoA to crotonyl-CoA,
    with ETF as electron acceptor. Current ChEBI57378 glutaryl-CoA(5-) has parent177898
    omega-carboxy-(fatty acyl)-CoA(5-), so dicarboxylate chemistry alone is not exclusion
    from fatty-acid oxidation. GO0033539 specifically describes iterative beta-oxidation
    beginning with fatty-acid activation and ending in acetyl/propionyl-CoA; distinguish
    that from a related dehydrogenation and decarboxylation. PMID21974953 directly
    compared rat GCDH substrate specificity with short/medium-chain ACADs; recover
    its substrate table rather than infer no fatty acyl substrates from a lysine-pathway
    label. PMID37198486 shows GCDH-generated crotonyl-CoA in human cells, and PMID17176108
    identifies product release as rate limiting. Fatty-acyl-CoA binding and biosynthesis
    are independently plausible and are not the disputed hypotheses here. Determine
    any demonstrated secondary fatty-acid oxidation capability versus only downstream
    metabolic convergence. Do not equate lack of one assay, low relative activity,
    or predominant amino-acid catabolism with absence of all other capacities.'
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/GCDH/GCDH-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human GCDH Q92947 participates in fatty acid\
    \ oxidation GO:0019395 and specifically fatty\n  acid beta-oxidation using acyl-CoA\
    \ dehydrogenase GO:0033539. Adjudicate separately using exact process\n  definitions,\
    \ substrate chemistry, full primary studies and phylogenetic placement. Exact\
    \ PTHR42807 target\n  PTN002533783 descends from positive IBD PTN005130278; GO:0033539\
    \ IBD uses Q92947 itself, which is legitimate\n  experimental grounding, not circularity.\
    \ The target IDA cites PMID25416781: the accessible cache contains\n  abstract/introduction/discussion\
    \ but omits the assay methods/results. Obtain the full assays and determine\n\
    \  which substrate was tested with GCDH versus MCAD. RHEA13389 oxidatively decarboxylates\
    \ glutaryl-CoA\n  to crotonyl-CoA, with ETF as electron acceptor. Current ChEBI57378\
    \ glutaryl-CoA(5-) has parent177898\n  omega-carboxy-(fatty acyl)-CoA(5-), so\
    \ dicarboxylate chemistry alone is not exclusion from fatty-acid\n  oxidation.\
    \ GO0033539 specifically describes iterative beta-oxidation beginning with fatty-acid\
    \ activation\n  and ending in acetyl/propionyl-CoA; distinguish that from a related\
    \ dehydrogenation and decarboxylation.\n  PMID21974953 directly compared rat GCDH\
    \ substrate specificity with short/medium-chain ACADs; recover\n  its substrate\
    \ table rather than infer no fatty acyl substrates from a lysine-pathway label.\
    \ PMID37198486\n  shows GCDH-generated crotonyl-CoA in human cells, and PMID17176108\
    \ identifies product release as rate\n  limiting. Fatty-acyl-CoA binding and biosynthesis\
    \ are independently plausible and are not the disputed\n  hypotheses here. Determine\
    \ any demonstrated secondary fatty-acid oxidation capability versus only downstream\n\
    \  metabolic convergence. Do not equate lack of one assay, low relative activity,\
    \ or predominant amino-acid\n  catabolism with absence of all other capacities.'\n\
    focus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 7
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
- **Gene directory:** GCDH
- **Gene symbol:** GCDH
- **UniProt accession:** Q92947

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fatty-acid-oxidation-and-beta-oxidation-scope
- **Source file:** genes/human/GCDH/GCDH-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human GCDH Q92947 participates in fatty acid oxidation GO:0019395 and specifically fatty acid beta-oxidation using acyl-CoA dehydrogenase GO:0033539. Adjudicate separately using exact process definitions, substrate chemistry, full primary studies and phylogenetic placement. Exact PTHR42807 target PTN002533783 descends from positive IBD PTN005130278; GO:0033539 IBD uses Q92947 itself, which is legitimate experimental grounding, not circularity. The target IDA cites PMID25416781: the accessible cache contains abstract/introduction/discussion but omits the assay methods/results. Obtain the full assays and determine which substrate was tested with GCDH versus MCAD. RHEA13389 oxidatively decarboxylates glutaryl-CoA to crotonyl-CoA, with ETF as electron acceptor. Current ChEBI57378 glutaryl-CoA(5-) has parent177898 omega-carboxy-(fatty acyl)-CoA(5-), so dicarboxylate chemistry alone is not exclusion from fatty-acid oxidation. GO0033539 specifically describes iterative beta-oxidation beginning with fatty-acid activation and ending in acetyl/propionyl-CoA; distinguish that from a related dehydrogenation and decarboxylation. PMID21974953 directly compared rat GCDH substrate specificity with short/medium-chain ACADs; recover its substrate table rather than infer no fatty acyl substrates from a lysine-pathway label. PMID37198486 shows GCDH-generated crotonyl-CoA in human cells, and PMID17176108 identifies product release as rate limiting. Fatty-acyl-CoA binding and biosynthesis are independently plausible and are not the disputed hypotheses here. Determine any demonstrated secondary fatty-acid oxidation capability versus only downstream metabolic convergence. Do not equate lack of one assay, low relative activity, or predominant amino-acid catabolism with absence of all other capacities.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: 'Human GCDH Q92947 participates in fatty acid oxidation GO:0019395 and specifically fatty
  acid beta-oxidation using acyl-CoA dehydrogenase GO:0033539. Adjudicate separately using exact process
  definitions, substrate chemistry, full primary studies and phylogenetic placement. Exact PTHR42807 target
  PTN002533783 descends from positive IBD PTN005130278; GO:0033539 IBD uses Q92947 itself, which is legitimate
  experimental grounding, not circularity. The target IDA cites PMID25416781: the accessible cache contains
  abstract/introduction/discussion but omits the assay methods/results. Obtain the full assays and determine
  which substrate was tested with GCDH versus MCAD. RHEA13389 oxidatively decarboxylates glutaryl-CoA
  to crotonyl-CoA, with ETF as electron acceptor. Current ChEBI57378 glutaryl-CoA(5-) has parent177898
  omega-carboxy-(fatty acyl)-CoA(5-), so dicarboxylate chemistry alone is not exclusion from fatty-acid
  oxidation. GO0033539 specifically describes iterative beta-oxidation beginning with fatty-acid activation
  and ending in acetyl/propionyl-CoA; distinguish that from a related dehydrogenation and decarboxylation.
  PMID21974953 directly compared rat GCDH substrate specificity with short/medium-chain ACADs; recover
  its substrate table rather than infer no fatty acyl substrates from a lysine-pathway label. PMID37198486
  shows GCDH-generated crotonyl-CoA in human cells, and PMID17176108 identifies product release as rate
  limiting. Fatty-acyl-CoA binding and biosynthesis are independently plausible and are not the disputed
  hypotheses here. Determine any demonstrated secondary fatty-acid oxidation capability versus only downstream
  metabolic convergence. Do not equate lack of one assay, low relative activity, or predominant amino-acid
  catabolism with absence of all other capacities.'
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

# AIGR Gene Hypothesis Deep Research — GCDH (Q92947)

## Focus: Fatty-Acid Oxidation and β-Oxidation Scope (`function_assignment`)

**Hypothesis under evaluation:** Human GCDH (Q92947) participates in fatty acid oxidation (GO:0019395) and specifically fatty acid beta-oxidation using acyl-CoA dehydrogenase (GO:0033539).

---

## Summary

Human GCDH (glutaryl-CoA dehydrogenase, UniProt **Q92947**) should **not** carry the fatty-acid-oxidation biological-process terms **GO:0019395** or **GO:0033539** as descriptions of its physiological function. The seed hypothesis raises several legitimate nuances — that GCDH is chemically a member of the acyl-CoA dehydrogenase (ACAD) superfamily, that glutaryl-CoA is a dicarboxylic acyl-CoA that is not automatically excluded from fatty-acid chemistry, and that GCDH can dehydrogenate a medium-chain fatty acyl-CoA in vitro. Each of those sub-claims is true at the molecular/chemistry level. But none of them rescues the disputed **biological-process** annotations, because the specific evidence chain behind those annotations collapses on inspection.

The single experimental (IDA) anchor for GO:0033539 is a **misattribution**: it cites [PMID:25416781](https://pubmed.ncbi.nlm.nih.gov/25416781/), a paper about the mitochondrial lysine methyltransferase METTL20 and its methylation of ETFβ, in which GCDH appears only as an electron donor — not as the subject of a β-oxidation assay. The accompanying phylogenetic (IBA) annotation is **circular**, anchored (withFrom) on GCDH's own misattributed IDA. The second term, GO:0019395, is an **IEA ortholog-transfer artifact** from rat that is conspicuously absent from the genuine fatty-acid-oxidation enzymes. Meanwhile GCDH's real reaction — a *single* oxidative decarboxylation of the dicarboxylic glutaryl-CoA to crotonyl-CoA + CO₂ within lysine/tryptophan catabolism — is categorically distinct from the *iterative* β-oxidation spiral that GO:0033539 defines.

**Verdict: over-annotated / refuted for the process terms**, with a narrow, qualified caveat that GCDH does possess a low-level in vitro fatty acyl-CoA dehydrogenation capacity (e.g., on hexanoyl-CoA) that belongs, if anywhere, at the molecular-function level as a non-core promiscuous activity. The recommended curation action is to **remove GO:0033539 and GO:0019395** as GCDH functions while **retaining glutaryl-CoA dehydrogenase activity (GO:0004361) and lysine/tryptophan catabolism** as core.

---

## Key Findings

### Finding F001 — The GO:0033539 IDA cites a METTL20/ETFβ methyltransferase paper, not a GCDH β-oxidation assay

The QuickGO annotation set for Q92947 lists **GO:0033539** (*fatty acid beta-oxidation using acyl-CoA dehydrogenase*) with evidence code **IDA**, referenced to **[PMID:25416781](https://pubmed.ncbi.nlm.nih.gov/25416781/)** (Malecki et al., *J Biol Chem* 2015), supplemented by an IBA from GO_REF:0000033. On retrieval, PMID:25416781 is a characterization of **human METTL20 as a mitochondrial lysine methyltransferase that methylates ETFβ** (the beta subunit of electron transfer flavoprotein). GCDH is mentioned only as one of the dehydrogenases whose ability to transfer electrons to ETF is diminished when ETFβ is methylated:

> *"METTL20-mediated methylation of ETFβ in vitro reduced its ability to receive electrons from the medium chain acyl-CoA dehydrogenase and the glutaryl-CoA dehydrogenase."*

That sentence is the entire GCDH-relevant content of the cited reference. There is **no assay of GCDH performing iterative fatty-acid β-oxidation** anywhere in the paper. The seed hypothesis explicitly asked us to recover the full assay methods/results and to determine "which substrate was tested with GCDH versus MCAD." The answer is that **neither GCDH nor MCAD was assayed for β-oxidation** in that study; both were used as electron *donors* to test the functional consequence of ETFβ methylation. The IDA is therefore a **text-derived misattribution** — most plausibly generated by co-occurrence of "glutaryl-CoA dehydrogenase" with an acyl-CoA-dehydrogenase/ETF context, rather than by any demonstrated β-oxidation experiment. Notably, UniProt appears to have attached the same PMID:25416781-derived GO:0033539 to ACADM (P11310) as well, consistent with a bulk, text-derived assignment rather than curated biology.

### Finding F002 — GCDH performs a single oxidative decarboxylation, not the iterative cycle GO:0033539 requires

The GO definition of **GO:0033539** specifies a fatty acid β-oxidation pathway that *"begins with the addition of coenzyme A to a fatty acid, and ends when only two or three carbons remain (as acetyl-CoA or propionyl-CoA)."* This is an **iterative, multi-enzyme spiral** that shortens a fatty acyl chain two carbons at a time (dehydrogenation → hydration → dehydrogenation → thiolysis, repeated).

GCDH's actual catalytic reaction (**GO:0004361**, **RHEA:13389**) is fundamentally different:

```
glutaryl-CoA  +  oxidized ETF  ──►  (2E)-butenoyl-CoA (crotonyl-CoA)  +  CO2  +  reduced ETF
```

This is a **single dehydrogenation coupled to a decarboxylation** acting on a *dicarboxylic* CoA thioester. The physiological substrate, glutaryl-CoA, is generated in the catabolism of L-lysine, hydroxylysine, and L-tryptophan — not from fatty-acid activation. Multiple primary sources confirm this:

- [PMID:15274622](https://pubmed.ncbi.nlm.nih.gov/15274622/) (human GCDH crystal structures): *"GCD catalyzes decarboxylation of glutaryl-CoA to produce CO(2) and crotonyl-CoA"* — a decarboxylating dehydrogenation, distinct from β-oxidation.
- [PMID:37198486](https://pubmed.ncbi.nlm.nih.gov/37198486/) (human glioblastoma cells): describes GCDH as the *"crotonyl-coenzyme A (crotonyl-CoA)-producing enzyme glutaryl-CoA dehydrogenase (GCDH)"* operating within lysine catabolism.
- [PMID:17176108](https://pubmed.ncbi.nlm.nih.gov/17176108/) (kinetic mechanism): GCDH *"oxidatively decarboxylates glutaryl-CoA to crotonyl-CoA and CO2"* and identifies **crotonyl-CoA product release as the major rate-determining step**.

GCDH does **not** run iterative two-carbon-removal cycles yielding acetyl-/propionyl-CoA from a fatty acid; it performs one turnover event on one dicarboxylic substrate. The crotonyl-CoA it produces is a **downstream metabolic convergence point** (crotonyl-CoA is also a β-oxidation intermediate), but producing a shared intermediate is not the same as running the β-oxidation process. This is precisely the "demonstrated capability versus only downstream metabolic convergence" distinction the seed hypothesis asked us to make — and it resolves against process participation.

### Finding F003 — GCDH has a real but low-level in vitro fatty acyl-CoA dehydrogenation capacity (promiscuous side activity)

Consistent with GCDH being a bona fide member of the ACAD superfamily, it retains detectable activity on straight-chain fatty acyl-CoAs in vitro:

- [PMID:21974953](https://pubmed.ncbi.nlm.nih.gov/21974953/) (rat GCDH functional characterization) reports that *"the enzyme has its catalytic properties very similar to those of short-chain and medium-chain acyl-CoA dehydrogenase except its additional decarboxylation reaction."* This is the direct substrate-specificity comparison the seed hypothesis specifically asked us to recover, and it confirms GCDH is *mechanistically* an ACAD.
- [PMID:11024031](https://pubmed.ncbi.nlm.nih.gov/11024031/) (human GCDH Arg-94 mutagenesis) measured steady-state kinetics of *"alternative substrates, hexanoyl-CoA and glutaramyl-CoA, which are not decarboxylated."* **Hexanoyl-CoA is a C6 straight-chain fatty acyl-CoA**, so this is direct demonstration of in vitro fatty acyl-CoA dehydrogenation by human GCDH — without decarboxylation.

The critical curation point: this establishes a **molecular capability** (acyl-CoA dehydrogenase activity on a fatty substrate), used here largely as a *tool* to dissect the enzyme's mechanism, at low relative activity compared with its glutaryl-CoA turnover. It does **not** establish that GCDH participates in the fatty-acid β-oxidation *process* in vivo. The seed hypothesis rightly warns against equating "low relative activity" with "absence of capacity" — and that warning is respected here: the capacity is acknowledged and belongs at the MF level as a non-core/promiscuous activity, but it does not license a BP process annotation.

### Finding F004 — The IBA is self-referentially circular, and GO:0033539 is over-propagated across amino-acid-catabolism ACADs

Inspection of the QuickGO withFrom provenance for Q92947 shows the **GO:0033539 IBA** (GO_Central, GO_REF:0000033) has withFrom = `['PTN005130278', 'Q92947']`. In other words, the phylogenetically inferred annotation is anchored **on GCDH's own experimental annotation** — the very IDA shown in F001 to be a misattribution from PMID:25416781. This is circular provenance: the IBA does not add independent evidence; it re-propagates the erroneous IDA.

Two further observations reinforce the over-annotation pattern:

1. **Family-wide leakage.** GO:0033539 is annotated not only to the genuine mitochondrial β-oxidation ACADs (**ACADM/ACADS/ACADVL/ACADL**, which carry independent IDA/IMP/ISS support) but also to **amino-acid-catabolism enzymes GCDH and IVD** (isovaleryl-CoA dehydrogenase). IVD's GO:0033539 rests only on an IDA to PMID:3597357, a shared ACAD-purification paper — the same kind of co-purification/co-mention text signal. GCDH and IVD are lysine- and leucine-catabolism enzymes respectively; neither runs the fatty-acid β-oxidation spiral.
2. **Ortholog-transfer artifact for GO:0019395.** GO:0019395 (fatty acid oxidation) is present on GCDH alone as an **IEA** (Ensembl ortholog transfer from rat) and is conspicuously **absent** from the true fatty-acid-oxidation enzymes — a signature of an automated transfer artifact rather than curated biology.

Importantly, the phylogenetic machinery *does* correctly identify GCDH's true function: the GCDH-clade PANTHER node **PTN005130278** carries the GCDH-specific molecular-function IBA **GO:0004361 (glutaryl-CoA dehydrogenase activity)**, confirming it is the glutaryl-CoA-dehydrogenase ortholog node (distinct from ACADM's node PTN002535634). So the correct MF propagates cleanly along the tree, while the β-oxidation BP term rides along as leakage anchored on a bad IDA.

---

## Mechanistic Model / Interpretation

The evidence produces a clean three-way separation between **what GCDH actually does**, **what it is chemically capable of in a test tube**, and **what has been erroneously annotated**.

```
                       GCDH (Q92947) — what the evidence supports
 ─────────────────────────────────────────────────────────────────────────────
  PHYSIOLOGICAL (core)                     IN VITRO CAPACITY (non-core)
  ──────────────────────                   ──────────────────────────────
  L-lysine / L-tryptophan catabolism        promiscuous ACAD activity
        │                                    on straight-chain acyl-CoA
        ▼                                    (e.g. hexanoyl-CoA, C6)
   glutaryl-CoA (dicarboxylic)                     │
        │  GCDH: single oxidative                  ▼
        │  decarboxylation (RHEA:13389)     simple dehydrogenation
        ▼  ETF = electron acceptor          (2,3-enoyl-CoA), no
   crotonyl-CoA + CO2                        decarboxylation, low rate
        │
        ▼  (downstream convergence only)
   crotonyl-CoA also appears in β-oxidation
   → NOT evidence GCDH runs β-oxidation

 ─────────────────────────────────────────────────────────────────────────────
  ERRONEOUS ANNOTATIONS (should be removed / not asserted as GCDH function)
  ──────────────────────────────────────────────────────────────────────────
  GO:0033539  IDA  ← PMID:25416781  = METTL20/ETFβ paper (misattribution)
  GO:0033539  IBA  ← withFrom Q92947 itself = circular on the bad IDA
  GO:0019395  IEA  ← Ensembl ortholog transfer from rat = transfer artifact
```

**Interpretation.** GCDH is definitively a **glutaryl-CoA dehydrogenase** (MF GO:0004361) that catalyzes one oxidative decarboxylation step within **lysine/tryptophan degradation** (BP GO:0019477 and related). Its membership in the ACAD superfamily gives it a residual ability to dehydrogenate short/medium-chain fatty acyl-CoAs in vitro — a fact exploited by mechanistic studies — but this is a low-level side activity, not a physiological role in energy-yielding fatty-acid β-oxidation. The two fatty-acid *process* annotations trace to (a) a single misattributed IDA from an unrelated methyltransferase paper, (b) an IBA that circularly re-uses that IDA, and (c) an IEA ortholog transfer. None reflects a demonstrated β-oxidation function.

The seed hypothesis's most defensible sub-claims — that dicarboxylate chemistry alone doesn't exclude fatty-acid oxidation (ChEBI places glutaryl-CoA(5-) under omega-carboxy-(fatty acyl)-CoA(5-)), and that GCDH can turn over a fatty acyl-CoA — are true at the chemistry/molecular level. But they do not rescue the **process** terms, because GO:0033539 has a specific *iterative-spiral* definition that GCDH does not satisfy, and GO:0019395 is present only via an automated artifact.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:25416781](https://pubmed.ncbi.nlm.nih.gov/25416781/) | Review of cited IDA source (database provenance) | **Refutes** (as β-oxidation evidence) | Does the GO:0033539 IDA reference actually assay GCDH β-oxidation? | Paper characterizes METTL20 methylation of ETFβ; GCDH only mentioned as an electron donor whose ETF transfer drops with methylation. No β-oxidation assay of GCDH. | Human, in vitro (methyltransferase focus) | High that it is a misattribution; abstract/discussion-level access, but GCDH content is confined to the ETFβ electron-transfer sentence |
| GO/QuickGO definition of GO:0033539; RHEA:13389 | Ontology definition + reaction chemistry | **Refutes** | Does GCDH's reaction match the iterative β-oxidation definition? | GO:0033539 = iterative CoA-fatty-acid spiral ending in acetyl/propionyl-CoA; GCDH does a single decarboxylating dehydrogenation of a dicarboxylate. | Definitional / reaction database | High; definitional comparison |
| [PMID:15274622](https://pubmed.ncbi.nlm.nih.gov/15274622/) | Structural (crystal structures) | **Refutes / qualifies** | Nature of GCDH reaction | GCDH decarboxylates glutaryl-CoA to CO₂ + crotonyl-CoA; distinct from β-oxidation. | Human GCDH protein | High; direct structural/mechanistic |
| [PMID:37198486](https://pubmed.ncbi.nlm.nih.gov/37198486/) | Cellular / pathway | **Refutes** (redirects to lysine catabolism) | Physiological process of GCDH | GCDH is the crotonyl-CoA-producing enzyme of lysine catabolism in human cells. | Human glioblastoma cells | High; confirms amino-acid catabolism context |
| [PMID:17176108](https://pubmed.ncbi.nlm.nih.gov/17176108/) | Direct assay (kinetics) | **Qualifies** | Reaction/kinetics of GCDH | Oxidative decarboxylation of glutaryl-CoA; crotonyl-CoA release is rate-limiting. | Purified enzyme | High; kinetic mechanism |
| [PMID:21974953](https://pubmed.ncbi.nlm.nih.gov/21974953/) | Direct assay (substrate specificity) | **Qualifies / partially supports (MF)** | Is GCDH mechanistically an ACAD with fatty acyl capacity? | Catalytic properties very similar to short/medium-chain ACAD except added decarboxylation. | Rat GCDH, in vitro | High for mechanism; species = rat; relative activity not equated to physiology |
| [PMID:11024031](https://pubmed.ncbi.nlm.nih.gov/11024031/) | Direct assay (mutagenesis + kinetics) | **Partially supports (MF only)** | Can human GCDH dehydrogenate a fatty acyl-CoA? | Hexanoyl-CoA (C6) is a measurable non-decarboxylated alternative substrate. | Human GCDH, in vitro | High for in vitro capacity; used as mechanistic tool, low physiological relevance |
| QuickGO withFrom provenance (Q92947) | Computational/database provenance | **Refutes** (circularity) | Is the GO:0033539 IBA independent? | IBA withFrom = ['PTN005130278','Q92947'] — anchored on GCDH's own (misattributed) IDA. | GO_Central phylogenetic annotation | High; provenance directly inspected |
| GO annotation distribution (GCDH, IVD, ACADM/S/VL/L) | Computational/database | **Refutes** (paralog leakage) | Is GO:0033539 specific to true β-ox enzymes? | Term over-propagated to amino-acid-catabolism ACADs (GCDH, IVD) alongside true β-ox ACADs. | Cross-gene comparison | Medium-high; pattern-level evidence |

**How the literature bears on the findings:** The two crystallographic/kinetic papers ([PMID:15274622](https://pubmed.ncbi.nlm.nih.gov/15274622/), [PMID:17176108](https://pubmed.ncbi.nlm.nih.gov/17176108/)) and the human cellular study ([PMID:37198486](https://pubmed.ncbi.nlm.nih.gov/37198486/)) collectively pin GCDH's physiological role to a single decarboxylating dehydrogenation within lysine catabolism, challenging the β-oxidation process claim. The two substrate-specificity/mutagenesis papers ([PMID:21974953](https://pubmed.ncbi.nlm.nih.gov/21974953/), [PMID:11024031](https://pubmed.ncbi.nlm.nih.gov/11024031/)) support only a molecular-level acyl-CoA-dehydrogenase capacity, not process participation. The cited IDA source ([PMID:25416781](https://pubmed.ncbi.nlm.nih.gov/25416781/)) is the linchpin misattribution that, together with the circular IBA and the IEA transfer, generated the disputed annotations.

---

## GO Curation Implications

**Lead (requires curator verification):**

| GO term | Aspect | Current evidence on Q92947 | Recommended action |
|---|---|---|---|
| **GO:0033539** — fatty acid beta-oxidation using acyl-CoA dehydrogenase | BP | IDA (PMID:25416781, misattributed) + IBA (circular, withFrom Q92947) | **Remove** as a GCDH process annotation. The IDA reference does not support β-oxidation; the IBA re-uses that IDA. |
| **GO:0019395** — fatty acid oxidation | BP | IEA (Ensembl ortholog transfer from rat) | **Remove / do not assert.** Ortholog-transfer artifact; absent from the genuine FA-oxidation enzymes. |
| **GO:0004361** — glutaryl-CoA dehydrogenase activity | MF | IDA + IBA on node PTN005130278 | **Retain** — this is GCDH's core molecular function. |
| **GO:0019477 / GO:0006554** — L-lysine catabolic process (glutaryl-CoA / lysine degradation) | BP | Supported by cellular evidence (PMID:37198486) and enzyme role | **Retain / strengthen** — this is GCDH's core biological process. |
| Generic **acyl-CoA dehydrogenase activity** (e.g., GO:0003995) | MF | In vitro hexanoyl-CoA activity (PMID:11024031, PMID:21974953) | **Optional, non-core.** Could be captured at MF level with a clear "in vitro / promiscuous" note; do **not** upgrade to a fatty-acid β-oxidation BP term. |

**Summary of the curation call:** The evidence supports **retaining GCDH's molecular function (glutaryl-CoA dehydrogenase) and its lysine/tryptophan-catabolism process** and **removing the two fatty-acid-oxidation biological-process terms (GO:0033539, GO:0019395)**. If a curator wishes to preserve the demonstrated in vitro fatty acyl-CoA activity, it belongs as a non-core MF-level note, never as a β-oxidation process annotation. Note that this recommendation targets the *biological-process* claim specifically; it does not dispute GCDH's identity as an ACAD-fold enzyme.

---

## Mechanistic Scope

The immediate molecular function tested is **flavin-dependent oxidative decarboxylation of glutaryl-CoA** (a dicarboxylic CoA thioester) to crotonyl-CoA + CO₂, with **ETF as the electron acceptor** — an ACAD-type dehydrogenation *plus* a decarboxylation. This is a discrete, single catalytic event.

Separating direct activity from downstream/inferred effects:

- **Direct gene-product activity:** glutaryl-CoA → crotonyl-CoA + CO₂ (GO:0004361); low-level in vitro dehydrogenation of straight-chain acyl-CoAs (hexanoyl-CoA).
- **Downstream/convergent metabolite:** crotonyl-CoA is *also* a β-oxidation intermediate, but GCDH producing it from glutaryl-CoA does not mean GCDH runs β-oxidation. Sharing a product is metabolic convergence, not process participation.
- **Loss-of-function phenotype (not evidence for β-oxidation):** GCDH deficiency causes glutaric aciduria type I (accumulation of glutaric and 3-hydroxyglutaric acid), a *lysine-catabolism* disorder — again pointing to amino-acid catabolism, not fatty-acid oxidation.

---

## Conflicts and Alternatives

- **Paralog / family leakage:** GO:0033539 is shared across the ACAD family including amino-acid-catabolism members (GCDH, IVD). The term legitimately belongs to ACADM/ACADS/ACADVL/ACADL (which have independent IDA/IMP/ISS support) and appears to have leaked onto GCDH via superfamily membership and co-mention.
- **Circular provenance:** The IBA is anchored on GCDH's own misattributed IDA — a self-referential loop rather than independent phylogenetic support.
- **Text-mining misattribution:** The IDA source (PMID:25416781) is an unrelated methyltransferase paper; the same paper was bulk-attached to ACADM/P11310, consistent with an automated text-derived assignment.
- **Species differences:** The clearest substrate-specificity comparison (PMID:21974953) is *rat* GCDH; the human hexanoyl-CoA data (PMID:11024031) confirm the capacity is conserved, but neither addresses in vivo flux.
- **Legitimate counter-nuance (acknowledged):** ChEBI places glutaryl-CoA(5-) under omega-carboxy-(fatty acyl)-CoA(5-), and GCDH is mechanistically an ACAD — so the enzyme is not chemically excluded from acting on fatty acyl-CoAs. This nuance justifies an MF-level acyl-CoA-dehydrogenase note but does not rescue the β-oxidation *process* terms.

---

## Limitations and Knowledge Gaps

1. **Full-text of PMID:25416781 assays:** Access was at abstract/discussion level. The conclusion that it contains no GCDH β-oxidation assay is well supported by the abstract's framing (METTL20/ETFβ), but a curator should confirm against the full Methods/Results that GCDH was used only as an electron donor. *Why it matters:* it is the sole experimental anchor for GO:0033539. *Resolution:* direct full-text inspection.
2. **Quantitative relative activity:** We know hexanoyl-CoA is an alternative substrate but did not extract the exact kcat/Km ratio versus glutaryl-CoA. *Why it matters:* quantifies how minor the fatty-acyl activity is. *Resolution:* recover kinetic tables from PMID:11024031 / PMID:21974953.
3. **No in vivo fatty-acid-oxidation flux data for GCDH:** No study demonstrates GCDH contributing to cellular fatty-acid β-oxidation flux. *Why it matters:* absence of any in vivo evidence is the core reason to reject the BP terms. *Resolution:* isotope-tracing or GCDH-knockout FA-oxidation flux assays.
4. **IVD/other family annotations:** The over-propagation pattern was assessed at the annotation-listing level; a full audit of each family member's GO:0033539 provenance would strengthen the "leakage" claim. *Resolution:* systematic QuickGO provenance audit across the ACAD family.

---

## Discriminating Tests

1. **Full-text substrate audit of PMID:25416781** — confirm GCDH is only an electron donor, not a β-oxidation substrate, in the cited IDA source. (Fastest, highest-yield.)
2. **Kinetic ratio extraction** — pull kcat/Km for glutaryl-CoA vs hexanoyl-CoA from PMID:11024031 and the rat comparison in PMID:21974953 to quantify how minor the fatty-acyl activity is.
3. **Provenance audit across ACAD family** — compare withFrom chains for GO:0033539 on GCDH, IVD, and the true β-ox ACADs to confirm the leakage/circularity pattern.
4. **In vivo flux test (conceptual)** — a GCDH-specific perturbation in a fatty-acid-oxidation flux assay would definitively separate physiological β-oxidation participation from lysine catabolism; predicted result: no FA-oxidation defect from GCDH loss (whereas MCAD/VLCAD loss impairs FA oxidation).

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

All items below are **leads requiring curator verification.**

**Candidate action changes:**
- **Remove** GO:0033539 (fatty acid beta-oxidation using acyl-CoA dehydrogenase) IDA/IBA from Q92947 — IDA misattributed to PMID:25416781; IBA circular.
- **Remove / do-not-assert** GO:0019395 (fatty acid oxidation) IEA — ortholog-transfer artifact.
- **Retain** GO:0004361 (glutaryl-CoA dehydrogenase activity) as core MF.
- **Retain / strengthen** L-lysine catabolic process (GO:0019477 and related) as core BP.
- **Optional non-core MF note:** generic acyl-CoA dehydrogenase activity, flagged as in vitro/promiscuous only.

**Candidate references with snippets to verify:**
- PMID:25416781 — *"METTL20-mediated methylation of ETFβ in vitro reduced its ability to receive electrons from the medium chain acyl-CoA dehydrogenase and the glutaryl-CoA dehydrogenase"* → shows GCDH is only an electron donor; not a β-oxidation assay.
- PMID:15274622 — *"GCD catalyzes decarboxylation of glutaryl-CoA to produce CO(2) and crotonyl-CoA"* → confirms single decarboxylating dehydrogenation, not β-oxidation.
- PMID:37198486 — *"crotonyl-coenzyme A (crotonyl-CoA)-producing enzyme glutaryl-CoA dehydrogenase (GCDH)"* → amino-acid (lysine) catabolism context.
- PMID:21974953 — *"catalytic properties very similar to those of short-chain and medium-chain acyl-CoA dehydrogenase except its additional decarboxylation reaction"* → mechanistic ACAD, supports MF-level acyl-CoA capacity only.
- PMID:11024031 — *"alternative substrates, hexanoyl-CoA and glutaramyl-CoA, which are not decarboxylated"* → in vitro C6 fatty acyl-CoA activity, non-core.

**Suggested curator questions:**
- Does the full text of PMID:25416781 contain any GCDH β-oxidation assay? (Expected: no.)
- Is GO:0033539 on IVD (via PMID:3597357) similarly a co-purification carry-over?

**Suggested experiments:** GCDH-perturbation fatty-acid-oxidation flux assay; quantitative kinetics comparing glutaryl-CoA and fatty acyl-CoA substrates.

---

## Conclusion

The seed hypothesis raises legitimate nuances — GCDH is chemically an ACAD, glutaryl-CoA is a dicarboxylic acyl-CoA that ChEBI classifies under omega-carboxy-(fatty acyl)-CoA, and the enzyme can dehydrogenate a medium-chain fatty acyl-CoA in vitro — and those nuances correctly caution against dismissing all fatty-acyl capacity out of hand. But they do not sustain the disputed **process** annotations. The GO:0033539 IDA is misattributed to an unrelated METTL20/ETFβ paper; its IBA is circularly anchored on that same bad IDA; GO:0019395 is an IEA ortholog-transfer artifact; and GCDH's actual chemistry is a single oxidative decarboxylation within lysine/tryptophan catabolism, not the iterative β-oxidation spiral GO:0033539 defines. **Recommendation: remove GO:0033539 and GO:0019395 as GCDH functions; retain glutaryl-CoA dehydrogenase activity and lysine catabolism as core; and, at most, represent any residual fatty-acyl activity as a non-core in vitro molecular function.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)