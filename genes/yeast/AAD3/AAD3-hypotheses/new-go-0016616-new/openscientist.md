---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T16:23:39.197104'
end_time: '2026-08-22T16:41:50.452339'
duration_seconds: 1091.26
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: AAD3
  gene_symbol: AAD3
  uniprot_accession: P25612
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: proposed_go_term
  hypothesis_slug: new-go-0016616-new
  hypothesis_text: 'AAD3 should be considered for GO annotation to oxidoreductase
    activity, acting on the CH-OH group of donors, NAD or NADP as acceptor (GO:0016616).
    Current rationale: AAD3 is a full-length aldo/keto reductase (Pfam PF00248) with
    the AKR fold and NADP(H)-cofactor-associated regions, supporting a general NADP(H)-linked
    CH-OH oxidoreductase capability. Because no substrate or activity has been demonstrated
    for AAD3, this broad parent term is the appropriate, non-over-committing molecular
    function; it is offered as the replacement for the two over-specific aryl-alcohol-dehydrogenase
    annotations.'
  term_context: '- Term: oxidoreductase activity, acting on the CH-OH group of donors,
    NAD or NADP as acceptor (GO:0016616)

    - Evidence type: ISS

    - Original reference: PMID:10572264

    - Current review action: NEW

    - Review summary: Proposed generalized molecular function for AAD3: a superfamily-level
    NADP(H)-dependent oxidoreductase acting on CH-OH groups, replacing the over-specific
    "aryl-alcohol dehydrogenase (NADP+) activity". This is the most specific activity
    that can be responsibly assigned from AKR-fold membership without demonstrated
    substrate specificity.

    - Review reason: AAD3 is a full-length aldo/keto reductase (Pfam PF00248) with
    the AKR fold and NADP(H)-cofactor-associated regions, supporting a general NADP(H)-linked
    CH-OH oxidoreductase capability. Because no substrate or activity has been demonstrated
    for AAD3, this broad parent term is the appropriate, non-over-committing molecular
    function; it is offered as the replacement for the two over-specific aryl-alcohol-dehydrogenase
    annotations.'
  reference_context: '- PMID:10572264'
  source_file: genes/yeast/AAD3/AAD3-ai-review.yaml
  source_selector: existing_annotations[5]
  source_context_yaml: "term:\n  id: GO:0016616\n  label: oxidoreductase activity,\
    \ acting on the CH-OH group of donors, NAD or NADP as acceptor\nevidence_type:\
    \ ISS\noriginal_reference_id: PMID:10572264\nqualifier: enables\nreview:\n  summary:\
    \ 'Proposed generalized molecular function for AAD3: a superfamily-level NADP(H)-dependent\
    \ oxidoreductase\n    acting on CH-OH groups, replacing the over-specific \"aryl-alcohol\
    \ dehydrogenase (NADP+) activity\".\n    This is the most specific activity that\
    \ can be responsibly assigned from AKR-fold membership without\n    demonstrated\
    \ substrate specificity.'\n  action: NEW\n  reason: AAD3 is a full-length aldo/keto\
    \ reductase (Pfam PF00248) with the AKR fold and NADP(H)-cofactor-associated\n\
    \    regions, supporting a general NADP(H)-linked CH-OH oxidoreductase capability.\
    \ Because no substrate\n    or activity has been demonstrated for AAD3, this broad\
    \ parent term is the appropriate, non-over-committing\n    molecular function;\
    \ it is offered as the replacement for the two over-specific aryl-alcohol-dehydrogenase\n\
    \    annotations.\n  supported_by:\n  - reference_id: PMID:10572264\n    supporting_text:\
    \ By in silicio analysis, we have discovered that there are seven open reading\
    \ frames\n      (ORFs) in Saccharomyces cerevisiae whose protein products show\
    \ a high degree of amino acid sequence\n      similarity to the aryl alcohol dehydrogenase\
    \ (AAD) of the lignin-degrading fungus Phanerochaete\n      chrysosporium."
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
citation_count: 2
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** AAD3
- **Gene symbol:** AAD3
- **UniProt accession:** P25612

## Focus

- **Focus type:** proposed_go_term
- **Hypothesis slug:** new-go-0016616-new
- **Source file:** genes/yeast/AAD3/AAD3-ai-review.yaml
- **Source selector:** existing_annotations[5]

## Seed Hypothesis

AAD3 should be considered for GO annotation to oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor (GO:0016616). Current rationale: AAD3 is a full-length aldo/keto reductase (Pfam PF00248) with the AKR fold and NADP(H)-cofactor-associated regions, supporting a general NADP(H)-linked CH-OH oxidoreductase capability. Because no substrate or activity has been demonstrated for AAD3, this broad parent term is the appropriate, non-over-committing molecular function; it is offered as the replacement for the two over-specific aryl-alcohol-dehydrogenase annotations.

## Term and Decision Context

- Term: oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor (GO:0016616)
- Evidence type: ISS
- Original reference: PMID:10572264
- Current review action: NEW
- Review summary: Proposed generalized molecular function for AAD3: a superfamily-level NADP(H)-dependent oxidoreductase acting on CH-OH groups, replacing the over-specific "aryl-alcohol dehydrogenase (NADP+) activity". This is the most specific activity that can be responsibly assigned from AKR-fold membership without demonstrated substrate specificity.
- Review reason: AAD3 is a full-length aldo/keto reductase (Pfam PF00248) with the AKR fold and NADP(H)-cofactor-associated regions, supporting a general NADP(H)-linked CH-OH oxidoreductase capability. Because no substrate or activity has been demonstrated for AAD3, this broad parent term is the appropriate, non-over-committing molecular function; it is offered as the replacement for the two over-specific aryl-alcohol-dehydrogenase annotations.

## Reference Context

- PMID:10572264

## Source Context YAML

```yaml
term:
  id: GO:0016616
  label: oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor
evidence_type: ISS
original_reference_id: PMID:10572264
qualifier: enables
review:
  summary: 'Proposed generalized molecular function for AAD3: a superfamily-level NADP(H)-dependent oxidoreductase
    acting on CH-OH groups, replacing the over-specific "aryl-alcohol dehydrogenase (NADP+) activity".
    This is the most specific activity that can be responsibly assigned from AKR-fold membership without
    demonstrated substrate specificity.'
  action: NEW
  reason: AAD3 is a full-length aldo/keto reductase (Pfam PF00248) with the AKR fold and NADP(H)-cofactor-associated
    regions, supporting a general NADP(H)-linked CH-OH oxidoreductase capability. Because no substrate
    or activity has been demonstrated for AAD3, this broad parent term is the appropriate, non-over-committing
    molecular function; it is offered as the replacement for the two over-specific aryl-alcohol-dehydrogenase
    annotations.
  supported_by:
  - reference_id: PMID:10572264
    supporting_text: By in silicio analysis, we have discovered that there are seven open reading frames
      (ORFs) in Saccharomyces cerevisiae whose protein products show a high degree of amino acid sequence
      similarity to the aryl alcohol dehydrogenase (AAD) of the lignin-degrading fungus Phanerochaete
      chrysosporium.
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

# AAD3 (P25612) — Evaluation of proposed GO:0016616 annotation

**Gene:** AAD3 / YCR107W (*Saccharomyces cerevisiae*, NCBITaxon:559292) · **UniProt:** P25612
**Focus:** proposed_go_term `new-go-0016616-new` — assign **GO:0016616** *"oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor"* (ISS, ref PMID:10572264) as a generalized replacement for the over-specific "aryl-alcohol dehydrogenase (NADP+) activity".

---

## Executive Judgment

**Verdict: Weakly supported / partially supported — leaning over-annotated.**

The *structural* premise of the seed is correct: AAD3 is a genuine, full-length (363 aa) member of the aldo/keto reductase (AKR) superfamily (Pfam PF00248; CDD cd19147, the *Phanerochaete chrysosporium* AAD subfamily; SSF51430 NAD(P)-linked oxidoreductase), and GO:0016616 is the correct hierarchical **parent** of "aryl-alcohol dehydrogenase (NADP+) activity". So the *move* from an over-specific child term up to a broad parent is, in isolation, a defensible conservative curation action, and removing the over-specific term is clearly warranted.

**However, the underlying assertion — that AAD3 has any active NADP(H)-dependent CH-OH oxidoreductase activity — is contradicted by direct primary evidence.** Yang et al. 2018 (PMID:29079624) show that AAD3 carries a missense mutation at the **catalytically essential tyrosine (Tyr73)** and that *repairing that residue still did not yield a functional enzyme*, i.e. AAD3 is a pseudogenizing AKR with more than one inactivating lesion. Only paralogs Aad4 and Aad14 are functional.

I independently confirmed and refined the lesion. Global alignment shows AAD3 is 81.6% identical to functional Aad4 yet has **Cys** where Aad4 retains the catalytic **Tyr** (Tyr73→Cys). Motif-anchored mapping of the full **AKR catalytic tetrad** shows AAD3 retains **3 of 4** catalytic residues — **Asp68, Lys100, His148 (all present)** — but has lost only the **general-acid/base tyrosine (Tyr73→Cys)**, whereas both functional paralogs Aad4 and Aad14 carry the complete Asp/Tyr/Lys/His tetrad. Thus the AKR *scaffold and cofactor architecture are intact* (which is exactly why fold-based predictors flag AAD3), but the single catalytic residue that drives the hydride/proton chemistry is absent — and because its repair alone does not restore activity, further extra-tetrad lesions (substrate-binding loops, NADP contacts, or folding) must also contribute. Delneri et al. 1999 (PMID:10572264) found no aromatic-aldehyde phenotype even in a septuple aad-deletion strain.

Because a molecular-function term — even a broad one — asserts that the gene product *enables* the catalysis, GO:0016616 over-commits for AAD3. The most responsible action is to **remove the over-specific term and NOT assert an active catalytic MF**, or to keep at most a fold-based prediction that is explicitly flagged (ISS/ISM) against the experimental evidence of non-functionality.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt **P25612** | database / seq record | supports (fold only) | AAD3 is a full-length AKR | 363 aa, EC 1.1.1.-, "aldo/keto reductase family, AKR2 subfamily"; labelled **"Putative"** | *S. cerevisiae* record | High for fold; no activity demonstrated |
| InterPro/Pfam **PF00248**, CDD **cd19147**, SSF51430, PANTHER PTHR43364 | computational | supports (fold only) | AKR fold + NADP-linked oxidoreductase domain | IPR023210 NADP-dependent oxidoreductase domain; cd19147 = AAD subfamily | domain analysis | High; domain call ≠ activity |
| Own global alignment AAD3 vs **Aad4 (Q07747)** | computational | qualifies / refutes | AAD3 retains catalytic machinery? | 81.6% identity (261/320); **Aad4 has Tyr where AAD3 has Cys73**; His motif (…VHWWDYM…) conserved | in-silico Needleman–Wunsch | High; independent of literature |
| Own motif-anchored tetrad mapping (AAD3 vs Aad4/Aad14) | computational | qualifies / refutes | Which catalytic residues survive in AAD3? | AAD3 tetrad = **Asp68 ✓, Tyr73→Cys ✗, Lys100 ✓, His148 ✓** (3/4 intact); Aad4 & Aad14 = full Asp/Tyr/Lys/His | in-silico motif anchors (QNE, HWW, IDxA, IVIATK) | High; only catalytic Tyr is lost, so fold intact but chemistry dead |
| **Yang et al. 2018 — PMID:29079624** | mutant / repair phenotype (direct) | **refutes** | Does AAD3 encode a functional enzyme? | Catalytic Tyr73 mutated; **repair did not restore function**; only Aad4/Aad14 functional; other AAD genes "undergoing pseudogenization" | *S. cerevisiae* enzymology | High; direct experimental evidence |
| **Delneri et al. 1999 — PMID:10572264** (the ISS reference) | mutant phenotype (LoF) | refutes / qualifies | Do AAD genes drive aldehyde metabolism? | Septuple deletant: **no phenotype** by spectrophotometry & HPLC | *S. cerevisiae* genetics | Medium; redundancy could mask, but no AAD3 activity shown |

*Note:* PMID:10572264 (the cited ISS reference) is a gene-**disruption** paper that provides no positive biochemical support for AAD3 activity — it is a weak provenance choice for an activity-asserting MF.

---

## GO Curation Implications (leads — require curator verification)

| Term | Aspect | Recommended action | Rationale |
|---|---|---|---|
| "aryl-alcohol dehydrogenase (NADP+) activity" (over-specific) | MF | **Remove** (agree with review) | No substrate/activity demonstrated for AAD3; specific term unjustified |
| **GO:0016616** (proposed parent) | MF | **Do not add as an asserted (`enables`) function**, OR add only as an explicitly-flagged fold prediction (ISS/ISM) with a pseudogene caveat | Hierarchically valid generalization, but asserts catalysis that primary data (Tyr73Cys + non-rescue) contradict |
| GO:0016491 "oxidoreductase activity" | MF | Acceptable *more conservative* fallback if any MF must be retained | Commits only to fold-level redox potential, not direction/cofactor |

**Bottom line for the curator:** The review's instinct to *generalize away from over-specificity* is right, but GO:0016616 is still an activity assertion. Given experimental evidence that AAD3 is a non-functional, pseudogenizing AKR, the stronger and more defensible outcome is to leave AAD3 without an asserted catalytic MF (or with a clearly-labelled predicted term plus the Yang-2018 caveat), rather than to substitute one predicted activity term for another.

---

## Mechanistic Scope

- **Immediate molecular function under test:** NADP(H)-dependent oxidoreduction of a CH-OH / carbonyl substrate by the AAD3 gene product itself.
- **Direct gene-product activity:** *Not demonstrated for AAD3.* The catalytic general-acid tyrosine is absent (Tyr73→Cys), and engineered restoration of that residue does not produce a functional enzyme — direct evidence that AAD3 cannot perform the catalysis.
- **Downstream/inferred effects:** No aryl-aldehyde detoxification phenotype attributable to the AAD family (septuple deletant unaffected). The family's ancestral role in lignin-derived aldehyde detox is retained only by Aad4/Aad14.

Fold membership (a structural fact) is being conflated with catalytic capability (a functional claim). The seed correctly establishes the former but the latter is refuted for this paralog.

---

## Conflicts and Alternatives

- **Paralog over-annotation (primary concern):** The demonstrated NADPH-dependent aryl-aldehyde reductase activity belongs to **Aad4/Aad14**, not AAD3. Transferring a family-level function to AAD3 is exactly the kind of paralog carry-over that produces spurious annotations.
- **Direction of reaction:** Functional Aad enzymes physiologically *reduce* aldehydes (aldehyde + NADPH → alcohol). GO:0016616 describes the *oxidation* direction (CH-OH + NAD(P)+). The term is the correct EC/GO parent of "aryl-alcohol dehydrogenase (NADP+)", but it does not describe the enzymes' physiological reductase direction — another reason the term is an imperfect fit even for the functional members.
- **Pseudogenization gradient:** AAD3, AAD6, AAD10, AAD15, AAD16 are degenerate to varying degrees; AAD3 specifically is a full-length ORF whose lesions are point/missense rather than truncation — which can make automated fold-based pipelines mis-predict activity.

---

## Knowledge Gaps

1. **No direct in-vitro assay of purified AAD3 protein.** Checked: literature (Yang 2018 tested a *repaired* AAD3, not wild-type in a substrate panel). Matters because a definitive negative enzymatic result on WT AAD3 would fully settle the MF question. Resolve by: express/purify AAD3, assay aryl-/aliphatic-aldehyde reduction with NADPH (veratraldehyde, cinnamaldehyde, vanillin).
2. **Is AAD3 expressed/translated?** Checked: not established here. Matters for whether any GO MF annotation is even appropriate vs treating as a pseudogene. Resolve by: ribosome profiling / proteomics evidence.
3. **Complete catalog of inactivating substitutions.** Checked (partly resolved here): tetrad mapping shows only the catalytic **Tyr73** is lost in AAD3 (Asp68/Lys100/His148 retained), so the non-rescuable phenotype (Yang 2018) points to lesion(s) **outside** the tetrad. Matters for confidence in "non-functional" and for whether a fold-based MF could ever be defensible. Resolve by: map NADP-binding pocket + substrate loops in AAD3 vs Aad4/Aad14 and perform combinatorial site-directed rescue.
4. **NADP(H) binding retained?** The C-terminal cofactor loop appears intact, but binding was not measured. Resolve by: ITC/fluorescence cofactor-binding assay.

---

## Discriminating Tests

- **Recombinant enzyme assay** of wild-type AAD3 (± the Tyr73 repair, ± additional tetrad repairs) on a defined aryl/aliphatic aldehyde panel with NADPH — directly distinguishes "inactive pseudogene" from "cryptically active oxidoreductase."
- **Ancestral-state reconstruction / full tetrad repair** (as Yang did for Aad6-16 and Aad10) to pinpoint how many lesions separate AAD3 from function.
- **Expression evidence** (RNA-seq under DTT/oxidative stress; proteomics) to decide whether AAD3 warrants any protein-level GO annotation.
- **Comparative tetrad mapping** across all seven yeast AAD paralogs to build a per-paralog functionality call for consistent curation.

---

## Curation Leads (require curator verification)

- **Add reference PMID:29079624 (Yang et al. 2018)** — verbatim snippet to verify: *"Repair of an AAD3 missense mutation at the catalytically essential Tyr73 residue did not result in a functional enzyme."* and *"two of these genes, AAD4 and AAD14, encode functional enzymes that reduce aliphatic and aryl-aldehydes concomitant with the oxidation of cofactor NADPH."*
- **Re-examine the ISS reference PMID:10572264** — it is a disruption paper reporting *no* aldehyde phenotype; verify snippet *"None of the knock-out strains revealed any mutant phenotype when tested for the degradation of aromatic aldehydes."* It does not positively support an activity MF.
- **Candidate action change:** Remove the over-specific aryl-alcohol-dehydrogenase (NADP+) MF (agree). For the replacement, prefer **no asserted catalytic MF**, or GO:0016491/GO:0016616 only as an explicitly-flagged prediction (ISS/ISM) with a pseudogenization caveat citing PMID:29079624 — rather than substituting GO:0016616 as an `enables` annotation.
- **Suggested question for curator:** Should AAD3 be treated as a pseudogenizing ORF (annotate fold membership + note loss of catalytic Tyr73) rather than as an active oxidoreductase?
- **Suggested experiment:** WT-AAD3 recombinant aldehyde-reductase assay with NADPH (definitive).

---

### Provenance artifacts
- `/tmp/AAD3_evidence_matrix.csv` — evidence matrix (this analysis)
- `/tmp/AAD3_catalytic_tetrad.png` — AAD3 vs Aad4 alignment showing Tyr73→Cys catalytic-residue loss
- `/tmp/AAD3_tetrad_table.csv` / `/tmp/AAD3_tetrad_table.png` — motif-anchored AKR tetrad comparison (AAD3 vs Aad4/Aad14): 3/4 retained, only catalytic Tyr lost
- `/tmp/AAD3_GO_decision_table.csv` — GO decision table (attempted; regenerate if absent)

*Computational results (UniProt fetch, InterPro domain calls, AAD3-vs-Aad4 global alignment) were executed live; the Tyr73→Cys finding is reproduced independently of the cited literature and is concordant with it.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)