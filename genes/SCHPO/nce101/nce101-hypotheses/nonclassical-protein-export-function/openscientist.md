---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T21:57:17.210562'
end_time: '2026-08-31T22:17:32.056105'
duration_seconds: 1214.85
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: nce101
  gene_symbol: nce101
  uniprot_accession: C6Y4B6
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: nonclassical-protein-export-function
  hypothesis_text: Schizosaccharomyces pombe nce101 directly participates in signal-sequence-independent
    non-classical protein export, rather than merely inheriting an ambiguous family-level
    annotation from the Saccharomyces cerevisiae NCE101 screen.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/nce101/nce101-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe nce101 directly participates\
    \ in signal-sequence-independent non-classical\n  protein export, rather than\
    \ merely inheriting an ambiguous family-level annotation from the Saccharomyces\n\
    \  cerevisiae NCE101 screen.\nfocus_type: free_text\ncontext: []\nreference_id:\
    \ []"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifacts_nce101_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_nce101_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist nce101 evidence matrix
- filename: artifacts_nce101_go_decision_table.csv
  path: openscientist_artifacts/artifacts_nce101_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist nce101 go decision table
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
- **Gene directory:** nce101
- **Gene symbol:** nce101
- **UniProt accession:** C6Y4B6

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** nonclassical-protein-export-function
- **Source file:** genes/SCHPO/nce101/nce101-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe nce101 directly participates in signal-sequence-independent non-classical protein export, rather than merely inheriting an ambiguous family-level annotation from the Saccharomyces cerevisiae NCE101 screen.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe nce101 directly participates in signal-sequence-independent non-classical
  protein export, rather than merely inheriting an ambiguous family-level annotation from the Saccharomyces
  cerevisiae NCE101 screen.
focus_type: free_text
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

# AIGR Deep Research Report — *S. pombe* nce101 (C6Y4B6): "non-classical protein export" function

**Gene:** nce101 / SPAC12G12.17 (SCHPO) · **UniProt:** C6Y4B6 (NCE1_SCHPO) · **Family:** NCE101 (Pfam PF11654 / InterPro IPR024242 / PANTHER PTHR28011)
**Seed hypothesis:** *S. pombe* nce101 **directly** participates in signal-sequence-independent non-classical protein export, **rather than merely inheriting** an ambiguous family-level annotation from the *S. cerevisiae* NCE101 screen.

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED (with respect to "direct participation").**

The evidence points to the *opposite* of the seed hypothesis. Far from having direct, gene-product-specific evidence, *S. pombe* nce101 carries **no experimental functional data of any kind**, and every "non-classical export / exocytosis / protein secretion" annotation is electronically or phylogenetically transferred. This is precisely the "inherited ambiguous family-level annotation" scenario the hypothesis was framed to exclude.

Key pillars:
1. **No direct evidence in fission yeast.** UniProt C6Y4B6 is a 58-aa single-TM peptide at Protein Existence level 2 (transcript only). Its FUNCTION comment is 100% "By similarity" (ECO:0000250); GO terms are ISO (exocytosis), IBA (protein secretion), and IEA (membrane).
2. **PomBase itself calls it uncharacterized — and formally annotates it "unknown."** Characterisation status = **"conserved unknown"**; product name is the family label *"non-classical export protein family Nce101."* QuickGO confirms PomBase curates all three GO roots as **No Data (ND, GO_REF:0000015): molecular_function (GO:0003674) = ND, biological_process (GO:0008150) = ND, cellular_component (GO:0005575) = ND.** The only non-root functional terms are **GO:0009306 "protein secretion" via IEA (InterPro IPR024242) + IBA (GO_Central, from the *S. cerevisiae* NCE101 node S000003742)** and **GO:0016020 membrane via IEA.** No experimental (EXP/IDA/IMP/IGI) annotation exists. The only phenotypes are generic chemical-genomic drug/stress sensitivities.
3. **The founder annotation is weak and ambiguous.** *S. cerevisiae* NCE101 (Q02820, PE = 3 "inferred from homology") rests on a single 1996 galectin-1 **over-expression** screen (PMID 8655575) and is explicitly hedged: *"may be part of the export machinery **or** may also be a substrate."*
4. **The "NCE" family is a phenotype label, not a molecular-function family.** Sibling screen hits were reassigned to unrelated functions: **NCE103 = β-carbonic anhydrase** (an enzyme; PMID 25109265) and **NCE102 = plasma-membrane sphingolipid sensor / eisosome-MCC microdomain protein** (PMID 35758748) — neither a dedicated export-machinery component.

5. **Both reference databases call it "unknown function."** SGD's curated description of the founder (Verified ORF YJL205C) is *"Protein of unknown function; … SWAT-GFP and mCherry fusion proteins localize to the **cytosol**"* — and PomBase calls the *S. pombe* gene "conserved unknown." The experimental cytosolic localization further **conflicts** with the transferred "single-pass membrane protein" CC (a TMHMM prediction), so even the location term is uncertain.

**Most important caveat:** "Refuted" here means the *direct-participation* claim is unsupported and the annotation is over-strong; it does **not** prove nce101 is uninvolved in secretion. It is a genuine, fungi-conserved small peptide of currently unknown molecular function (Verified ORF, not dubious). Absence of evidence ≠ evidence of a different function. Note the location is itself ambiguous: predicted single-TM vs experimentally cytosolic tag fusions.

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | UniProt C6Y4B6 (NCE1_SCHPO) | Database record | Qualifies → refutes | Does *S. pombe* nce101 have direct export evidence? | 58-aa single-pass TM peptide; PE = 2 (transcript only); FUNCTION entirely "By similarity" (ECO:0000250); GO exocytosis = ISO, protein secretion = IBA, membrane = IEA | *S. pombe* | High for annotation provenance; no experimental function exists |
| 2 | PomBase SPAC12G12.17 | Database record | Refutes | Is nce101 experimentally characterized? | **characterisation_status = "conserved unknown"**; product = "non-classical export protein family Nce101"; no experimental GO MF/BP/CC; deletion_viability = unknown; taxonomic distribution = fungi only | *S. pombe* | High; authoritative organism database |
| 3 | PomBase phenotype set (FYPO) | Mutant phenotype (HTP) | Qualifies (not export-specific) | Do deletion phenotypes indicate export role? | Only generic chemical-genomic hits: resistance/sensitivity to amorolfine, EGTA, Li⁺, SDS combinations, MMS, cadmium, diamide, valproate, vanadate | *S. pombe* genome-wide screens | Medium; none implicate protein export; typical pleiotropic stress hits |
| 4 | UniProt Q02820 (NCE1_YEAST) | Database record | Qualifies | Strength of founder annotation | 53-aa peptide; PE = 3 "inferred from homology"; GO protein secretion = IGI | *S. cerevisiae* | High; even the founder lacks protein-level/MF evidence |
| 5 | Cleves, Cooper, Barondes, Kelly 1996 — PMID **8655575** (DOI 10.1083/jcb.133.5.1017) | Direct assay (screen) | Competing / qualifies | Origin of "non-classical export" label | Screen using heterologous mammalian galectin-1 over-expression identified NCE genes; UniProt function is hedged "machinery **or** substrate" | *S. cerevisiae*, galectin-1 reporter | Medium; over-expression heterologous reporter; does not establish endogenous direct role for the 53-aa peptide |
| 6 | Zahumenský et al. 2022 — PMID **35758748** | Localization / mechanism | Competing (family reassignment) | Is the "NCE" family a molecular-function family? | NCE102 is a plasma-membrane **sphingolipid sensor** redistributing in eisosome/MCC microdomains | *S. cerevisiae* | High; shows NCE members have unrelated real functions |
| 7 | Lehneck & Pöggeler 2014 — PMID **25109265** | Structural/enzymatic review | Competing (family reassignment) | Same as #6 | NCE103 is a structurally characterized **β-carbonic anhydrase** (enzyme), unrelated to export | Fungal CAs incl. *S. cerevisiae* Nce103 | High; canonical example of NCE mis-labeling by phenotype |
| 8 | UniProt PF11654 family listing (50+ entries) | Computational/evolutionary | Qualifies | Is there any experimental anchor in the family? | All NCE101-family members are PE 3 (inferred) or PE 4 (predicted); fungi-only; no experimental characterization anywhere | Pan-fungal | High; entire family is annotation-by-homology |
| 9 | SGD locus YJL205C/NCE101 | Localization / database | Refutes / qualifies | Is the founder characterized, and where does it localize? | Verified ORF but **"Protein of unknown function"**; SWAT-GFP and mCherry fusions localize to the **cytosol** (conflicts with predicted single-pass-membrane CC) | *S. cerevisiae* | High for curation status; GFP tag on a 53-aa peptide could perturb targeting |
| 10 | UniProt Q12207 (NCE2_YEAST) vs Q02820/C6Y4B6 | Structural/evolutionary | Qualifies | Paralog confusion between NCE101 and NCE102? | NCE101 = Pfam **PF11654** (53–58 aa, 1 predicted TM); NCE102 = **PF01284** MARVEL/tetraspanin (173 aa, multi-TM) — unrelated families | Cross-species | High; rules out nce101/NCE102 conflation |
| 11 | QuickGO annotation set for C6Y4B6 | Database (provenance) | Refutes | What does PomBase actually assert for nce101? | PomBase curates **MF, BP, and CC all = ND** (No Data, GO_REF:0000015); "protein secretion" exists **only** as IEA (InterPro) + IBA (from *Sc* NCE101 node S000003742); membrane = IEA; **no experimental annotation** | *S. pombe* | High; definitive database-level provenance |

---

## GO Curation Implications *(leads — require curator verification)*

The three functional GO annotations on C6Y4B6 all trace, ultimately, to transferred/ambiguous evidence:

| GO term | Aspect | Current evidence | Lead |
|---------|--------|------------------|------|
| GO:0009306 protein secretion | BP | IBA (GO_Central) + IEA (InterPro) | **Weaken / flag as non-core.** Supported only electronically + phylogenetically from the ambiguous *Sc* founder node; PomBase itself curates BP root as ND (unknown). Retain at most as low-confidence IBA, or defer to the ND ("unknown biological process") position. |
| GO:0003674 / GO:0008150 / GO:0005575 (roots) | MF/BP/CC | ND (PomBase, GO_REF:0000015) | **Respect the ND curation.** PomBase explicitly records molecular function, biological process, and cellular component as *unknown*. Do **not** add any MF export/transporter term. |
| GO:0006887 exocytosis | BP | ISO (from *S. cerevisiae*) | **Candidate for removal or generalization.** ISO transfer from a founder whose own annotation is "machinery or substrate"; "exocytosis" is more specific than the founder evidence supports. |
| GO:0016020 membrane | CC | IEA + a real TMHMM helix (aa 10–27) | **Retain only cautiously / flag.** A predicted single-TM helix supports it, but the *S. cerevisiae* ortholog's SWAT-GFP/mCherry fusions localize to the **cytosol** (SGD), a direct conflict. Do not upgrade to a specific membrane system; consider "cytoplasm" as a competing CC pending organism-specific data. |

- **No MF term is justified** by current evidence beyond, at most, generic membrane localization. Do **not** assert an export-machinery molecular activity.
- Recommend the curated position mirror PomBase's **"conserved unknown"**: a fungi-conserved small single-pass membrane protein of **unknown molecular function**, with any secretion/export terms explicitly marked as homology-transferred and non-core.
- Avoid defaulting to "protein binding" — no interaction evidence exists for the *S. pombe* product.

---

## Mechanistic Scope

**Immediate molecular function being tested:** whether the 58-aa nce101 peptide is itself a component (or dedicated substrate) of a signal-sequence-independent export apparatus.

- **Direct gene-product activity:** unknown. The only hard biochemical/structural fact is a single predicted transmembrane helix (aa 10–27) → integral membrane peptide.
- **Downstream / inferred:** the "export" descriptor derives from an *over-expression* phenotype on a heterologous reporter (galectin-1) in a different species (*S. cerevisiae*), then propagated by orthology. This is a pathway-level phenotype, not a demonstrated molecular activity of the endogenous peptide.
- The *S. pombe* deletion phenotypes (drug/stress sensitivities) are pleiotropic and do not localize the protein to an export step.

---

## Conflicts and Alternatives

- **Family carry-over / mis-labeling (strongest alternative):** NCE103 (carbonic anhydrase) and NCE102 (sphingolipid sensor) demonstrate that "NCE" screen membership routinely does **not** correspond to a direct export function. nce101 is the least-characterized member.
- **"Substrate vs machinery" ambiguity:** even the founder UniProt statement cannot decide whether the peptide is machinery or cargo — a fundamental unresolved distinction that undercuts any "directly participates in the export machinery" claim.
- **Species differences:** all *S. pombe* evidence is transferred; there is no fission-yeast export assay for nce101.
- **Over-expression artifact:** the founding phenotype is an over-expression/heterologous-reporter effect, a known source of gain-of-function artifacts that need not reflect endogenous function.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| No endogenous localization for *S. pombe* nce101 | UniProt CC = ECO:0000305; PomBase = conserved unknown | CC term (PM vs internal membrane) constrains plausible function | Endogenous tagged live-cell imaging in *S. pombe* |
| Machinery vs substrate unresolved | Founder function comment is hedged | Determines whether any MF/BP export term is even appropriate | Interactome + secretome comparison of Δnce101 |
| No secretion assay in fission yeast | PomBase phenotypes are drug/stress only | Direct test of export role is absent | Leaderless-cargo (e.g., Acb1/GAPDH-type) secretion assay in Δnce101 |
| Family function anywhere | Whole PF11654 = PE 3/4 | If any ortholog were characterized it would anchor the family | Targeted biochemistry on any tractable ortholog |

---

## Discriminating Tests

1. **Endogenous localization:** C-terminal tag of *S. pombe* nce101 at native locus; ask PM/eisosome vs ER/Golgi vs cytosolic membranes.
2. **Leaderless-secretion functional test:** measure unconventional secretion of an established cargo (e.g., Acb1, or heterologous galectin-1/GAPDH) in wild-type vs Δnce101 and vs over-expression — replicating the founder assay in the *actual* organism.
3. **Interactome:** AP-MS / proximity labeling to test physical association with any secretion apparatus vs membrane-microdomain proteins (parallels the NCE102 outcome).
4. **AlphaFold/structural check:** compare the modeled fold/topology against NCE102 (tetraspanin-like) to assess whether nce101 shares a microdomain-protein architecture rather than a transporter fold.
5. **Cross-species annotation audit:** confirm no experimental anchor exists anywhere in PF11654 before propagating export terms.

---

## Curation Leads *(all require curator verification)*

- **Action change:** Treat the "non-classical protein export / exocytosis" function as **non-core, homology-transferred, and over-strong** for C6Y4B6. Align the review with PomBase's **"conserved unknown"** characterisation.
- **GO leads:**
  - Retain **GO:0016020 membrane (CC, IEA)** — supported by a predicted TM helix (aa 10–27).
  - Flag/weaken **GO:0006887 exocytosis (ISO)** and **GO:0009306 protein secretion (IBA)** as non-experimental transfers; consider removing the more specific "exocytosis" term. Do **not** add an MF export/transporter term.
- **Candidate references to cite for the review:**
  - PMID **8655575** (founder screen; snippet: *"A screen for components of the export machinery has identified genes that are involved in nonclassical export."*) — note it is a heterologous over-expression screen and the UniProt function is hedged "machinery or substrate."
  - PMID **35758748** (NCE102 = sphingolipid sensor) and PMID **25109265** (NCE103 = carbonic anhydrase) — precedents that "NCE" ≠ molecular export function.
- **Suggested curator questions:**
  1. Is there *any* experimental (non-IBA/ISO/IEA) evidence for *S. pombe* nce101 function? (Current answer: no.)
  2. Should family-name-derived BP terms be demoted to "unknown molecular function" pending an organism-specific assay?
- **Suggested experiment (highest value):** Δnce101 leaderless-cargo secretion assay in *S. pombe* (Discriminating Test #2).

---

### Provenance
All programmatic results above were retrieved live during this run via the UniProt REST API (C6Y4B6, Q02820, Q12207 NCE102, PF11654 family search), the PomBase gene API (SPAC12G12.17), and the SGD backend locus API (YJL205C), plus PubMed abstracts (PMIDs 8655575, 35758748, 25109265). No local repository bioinformatics files were used. No result was fabricated; where evidence is absent it is stated as absent.

**Iteration 2 additions:** SGD confirms YJL205C is a *Verified* (not dubious) ORF but "protein of unknown function" with **cytosolic** GFP/mCherry localization; NCE101 (PF11654) and NCE102 (PF01284, MARVEL) are confirmed unrelated families, ruling out paralog confusion.

**Iteration 3 additions:** QuickGO API confirms PomBase curates C6Y4B6's MF/BP/CC roots as **ND** (unknown; GO_REF:0000015) and that "protein secretion" is present only as IEA + IBA transfers (IBA source = *S. cerevisiae* NCE101 node S000003742) — the definitive database-level demonstration that the export annotation is inherited, not direct. Computed provenance saved as `artifacts/nce101_evidence_matrix.csv` and `artifacts/nce101_go_decision_table.csv`.


## Artifacts

- [OpenScientist nce101 evidence matrix](openscientist_artifacts/artifacts_nce101_evidence_matrix.csv)
- [OpenScientist nce101 go decision table](openscientist_artifacts/artifacts_nce101_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)