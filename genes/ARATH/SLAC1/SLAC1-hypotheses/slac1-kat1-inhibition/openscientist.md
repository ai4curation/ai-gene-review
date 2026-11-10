---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T04:52:25.908697'
end_time: '2026-10-24T05:17:20.272876'
duration_seconds: 1494.36
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ARATH
  gene: SLAC1
  gene_symbol: SLAC1
  uniprot_accession: Q9LD83
  taxon_id: NCBITaxon:3702
  taxon_label: Arabidopsis thaliana
  focus_type: free_text
  hypothesis_slug: slac1-kat1-inhibition
  hypothesis_text: Arabidopsis SLAC1 (Q9LD83) physically interacts with and directly
    inhibits the guard-cell inward K+ channels KAT1 and AKT2 (but not KAT2), as reported
    by Zhang et al. 2016 (PMID:27002025), and this inhibition contributes to suppression
    of stomatal opening in planta; the finding has been independently replicated or
    corroborated and is not contradicted by later work.
  term_context: '- Term: potassium channel inhibitor activity (GO:0019870)

    - Test by literature: find studies after 2016 that measured guard-cell inward
    K+ currents, KAT1/AKT2 activity or stomatal opening in slac1 mutants or with SLAC1
    coexpression, and state whether each supports, fails to replicate, or contradicts
    direct SLAC1-mediated K+ channel inhibition. Distinguish physical interaction
    from functional inhibition, and Xenopus oocyte data from guard-cell patch clamp.'
  reference_context: '- PMID:27002025'
  source_file: genes/ARATH/SLAC1/SLAC1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Arabidopsis SLAC1 (Q9LD83) physically interacts\
    \ with and directly inhibits the guard-cell\n  inward K+ channels KAT1 and AKT2\
    \ (but not KAT2), as reported by Zhang et al. 2016 (PMID:27002025), and\n  this\
    \ inhibition contributes to suppression of stomatal opening in planta; the finding\
    \ has been independently\n  replicated or corroborated and is not contradicted\
    \ by later work.\nfocus_type: free_text\nterm_id: GO:0019870\nterm_label: potassium\
    \ channel inhibitor activity\ncontext:\n- 'Test by literature: find studies after\
    \ 2016 that measured guard-cell inward K+ currents, KAT1/AKT2\n  activity or stomatal\
    \ opening in slac1 mutants or with SLAC1 coexpression, and state whether each\
    \ supports,\n  fails to replicate, or contradicts direct SLAC1-mediated K+ channel\
    \ inhibition. Distinguish physical\n  interaction from functional inhibition,\
    \ and Xenopus oocyte data from guard-cell patch clamp.'\nreference_id:\n- PMID:27002025"
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
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: evidence_matrix.csv
  path: openscientist_artifacts/evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
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
- filename: go_decision_table.csv
  path: openscientist_artifacts/go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
- filename: hypothesis_clause_verdicts.csv
  path: openscientist_artifacts/hypothesis_clause_verdicts.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist hypothesis clause verdicts
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** ARATH
- **Taxon:** Arabidopsis thaliana (NCBITaxon:3702)
- **Gene directory:** SLAC1
- **Gene symbol:** SLAC1
- **UniProt accession:** Q9LD83

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** slac1-kat1-inhibition
- **Source file:** genes/ARATH/SLAC1/SLAC1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Arabidopsis SLAC1 (Q9LD83) physically interacts with and directly inhibits the guard-cell inward K+ channels KAT1 and AKT2 (but not KAT2), as reported by Zhang et al. 2016 (PMID:27002025), and this inhibition contributes to suppression of stomatal opening in planta; the finding has been independently replicated or corroborated and is not contradicted by later work.

## Term and Decision Context

- Term: potassium channel inhibitor activity (GO:0019870)
- Test by literature: find studies after 2016 that measured guard-cell inward K+ currents, KAT1/AKT2 activity or stomatal opening in slac1 mutants or with SLAC1 coexpression, and state whether each supports, fails to replicate, or contradicts direct SLAC1-mediated K+ channel inhibition. Distinguish physical interaction from functional inhibition, and Xenopus oocyte data from guard-cell patch clamp.

## Reference Context

- PMID:27002025

## Source Context YAML

```yaml
hypothesis: Arabidopsis SLAC1 (Q9LD83) physically interacts with and directly inhibits the guard-cell
  inward K+ channels KAT1 and AKT2 (but not KAT2), as reported by Zhang et al. 2016 (PMID:27002025), and
  this inhibition contributes to suppression of stomatal opening in planta; the finding has been independently
  replicated or corroborated and is not contradicted by later work.
focus_type: free_text
term_id: GO:0019870
term_label: potassium channel inhibitor activity
context:
- 'Test by literature: find studies after 2016 that measured guard-cell inward K+ currents, KAT1/AKT2
  activity or stomatal opening in slac1 mutants or with SLAC1 coexpression, and state whether each supports,
  fails to replicate, or contradicts direct SLAC1-mediated K+ channel inhibition. Distinguish physical
  interaction from functional inhibition, and Xenopus oocyte data from guard-cell patch clamp.'
reference_id:
- PMID:27002025
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

# SLAC1 (Q9LD83) as a Potassium Channel Inhibitor (KAT1/AKT2) — Hypothesis Evaluation

**Gene:** SLAC1 (Arabidopsis thaliana, UniProt Q9LD83, AT1G12480)
**Term under test:** GO:0019870 potassium channel inhibitor activity (MF)
**Seed reference:** Zhang et al. 2016, Plant Cell 28(4):949-955 (PMID:27002025)
**Hypothesis slug:** slac1-kat1-inhibition

---

## Executive Judgment

**Verdict: Partially supported (weak–moderate), not independently replicated.**

The seed hypothesis faithfully represents what Zhang et al. 2016 report, and that
single paper provides genuinely direct evidence for the molecular activity:
SLAC1 physically interacts with KAT1, KAT2 and AKT2 (Y2H, co-IP) and, in Xenopus
oocyte voltage-clamp, **functionally inhibits the inward-K⁺ (K⁺in) channels KAT1
and AKT2 but not KAT2**, with guard-cell gain-of-function (overexpression)
reducing K⁺in currents and light-induced stomatal opening. This is sufficient to
qualify SLAC1 as a candidate potassium-channel inhibitor (GO:0019870).

However, the stronger clauses of the hypothesis — "independently replicated or
corroborated and not contradicted by later work" — are **not met**:

1. **No independent functional replication.** Searching the 45 PubMed "cited-by"
   records (2017–2026) found no independent lab reproducing SLAC1→KAT1/AKT2
   patch-clamp inhibition. Citations are predominantly reviews or tangential.
2. **Database silence on the K⁺-channel interaction.** IntAct curates 19 SLAC1
   interactions, but **all are signaling kinases/phosphatases** (CPK6/21/23,
   PP2CA, SnRK2s/OST1) — **none with KAT1, AKT2 or KAT2**. The Zhang 2016 channel
   interaction has not been captured by interaction databases.
3. **The term is not currently annotated — this is an ADDITION.** UniProt/TAIR/
   QuickGO carry no potassium-channel inhibitor (GO:0019870) or regulator
   (GO:0015459) MF term for SLAC1; current MF terms are anion-channel activity and
   kinase/phosphatase binding. So the curation question is whether to *add* a new
   MF annotation on single-study evidence, not whether to retain one.
4. **Competing/contradicting in-planta directionality.** Laanemets et al. 2013
   (PMID:23126621) show that *slac1* loss-of-function **reduces** guard-cell K⁺in
   and slows opening — the *opposite* of the "relief of inhibition" predicted by a
   direct-inhibition model — and attribute it to elevated cytosolic [Ca²⁺] and
   increased Ca²⁺ sensitivity of K⁺in channels. The physiological role therefore
   rests mainly on gain-of-function overexpression.
5. **Conceptually corroborated.** The broader principle of S-type anion channels
   regulating K⁺ channels by protein–protein interaction is independently
   supported by analogous pairs (SLAH3–GORK/SKOR; ALMT12–SLAC1), lending indirect
   plausibility but not specific replication.

**Curation bottom line:** GO:0019870 is defensible as a non-core MF annotation
with explicit evidence/qualifier caveats (single study, heterologous oocyte
assay + overexpression), but it must not be presented as SLAC1's core function,
which remains S-type anion (Cl⁻/malate/NO₃⁻) channel activity driving stomatal
closure.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:27002025 (Zhang 2016) | Interaction (Y2H, split-ubiquitin, co-IP) | Supports | SLAC1 physically binds inward K⁺ channels | SLAC1 interacts with KAT1, KAT2, AKT2 but **not** AKT1 | Yeast system + oocyte co-IP | Moderate; single lab; no database curation (IntAct empty) |
| PMID:27002025 (Zhang 2016) | Direct assay (Xenopus oocyte voltage-clamp) | Supports | Functional inhibition of K⁺in | SLAC1 strongly inhibits KAT1 and AKT2 K⁺in; **does not inhibit KAT2**; K⁺out unaffected | Heterologous oocytes, overexpression | Moderate; heterologous, non-native stoichiometry; homotetramers only |
| PMID:27002025 (Zhang 2016) | Mutant / gain-of-function + guard-cell patch clamp | Supports (qualified) | In-planta relevance | SLAC1 (WT + truncated) overexpression impairs guard-cell K⁺in and light-induced opening; drought up-regulates SLAC1/SLAH3 | Arabidopsis guard cells | Low–moderate; gain-of-function, not loss-of-function; overexpression artifact plausible |
| PMID:23126621 (Laanemets 2013) | Mutant phenotype + guard-cell patch clamp | **Competing / qualifies** | Does *slac1* loss enhance K⁺in? | *slac1* **reduces** K⁺in and slows opening; rescued by lowering [Ca²⁺]cyt — a Ca²⁺-sensitivity mechanism, not relief of direct inhibition | Intact Arabidopsis, guard cells | High for the phenotype; directly complicates direct-inhibition interpretation in planta |
| PMID:36653170 (Liu 2023) | Direct assay (oocyte) + mutant | Corroborates concept | Do S-type anion channels regulate K⁺ channels generally? | SLAH3 interacts with and partially inhibits **outward** K⁺ channels GORK/SKOR (different channels) | Arabidopsis / oocytes | Independent lab (He/Luan); supports general mechanism, not SLAC1–KAT1 specifically |
| PMID:41022577 (Lin 2025) | Direct assay (oocyte + guard cell) | Corroborates concept | Channel–channel regulation of guard-cell anion channels | ALMT12 interacts with and inhibits SLAC1 | Arabidopsis guard cells | Independent; shows channel–channel coupling is real but is a different pairing/direction |
| PMID:38985761 (Qin 2024) | Structural / electrophysiology | Neutral/qualifies | SLAC1 activation mechanism | SLAC1 N/C cytosolic regulatory domain autoinhibits the TMD; phosphoactivation releases it | Structure/AlphaFold + oocyte | Independent; the same N/C termini implicated in KAT1 binding also mediate SLAC1 autoinhibition — raises an alternative role for those termini |
| PMID:24033256 (Acharya 2013) | Interaction + phenotype | Context | OST1 ties anion and K⁺in channels | OST1 physically interacts with both SLAC1 and KAT1 and inhibits K⁺in | Arabidopsis guard cells | Supports an alternative/parallel route (kinase-mediated) to K⁺in inhibition |
| IntAct (Q9LD83), this run | Database | Qualifies (absence) | Independent interaction curation | 19 curated SLAC1 interactions, all kinases/phosphatases (CPK6/21/23, PP2CA, SnRK2s/OST1); **none with KAT1/AKT2/KAT2** | Database query (this run) | The K⁺-channel interaction is not independently curated; absence ≠ disproof |
| UniProt/QuickGO (Q9LD83), this run | Database | Qualifies (current state) | Is GO:0019870 currently annotated? | **No** K⁺ channel inhibitor/regulator MF term present; current MF = anion channel + kinase/phosphatase binding; BP already has regulation of stomatal opening (GO:1902456) | TAIR/UniProt/InterPro | Reframes action as ADD, not retain |

---

## GO Curation Implications

- **Current state (verified this run):** GO:0019870 is **not** currently annotated to
  SLAC1 in UniProt/TAIR/QuickGO. The decision is therefore whether to **ADD** a new
  MF term on single-study evidence — a higher bar than retaining an existing one.
- **Term GO:0019870 (potassium channel inhibitor activity, MF):** *Supportable only
  as a cautious, explicitly-caveated non-core lead.* There is direct functional
  evidence (oocyte voltage-clamp inhibition of KAT1 and AKT2) plus physical
  interaction. Appropriate evidence code would be IDA (functional, from heterologous
  assay) optionally paired with IPI (physical interaction). **Mandatory caveats**:
  single study, single lab, heterologous oocyte system, gain-of-function
  overexpression, no independent replication, no database curation of the
  interaction, and a directionally opposite in-planta loss-of-function phenotype.
  Note it does **not** inhibit KAT2 despite binding it. A conservative curator could
  reasonably **decline the addition** pending independent replication.
- **Do not treat as core function.** SLAC1's primary MF is S-type anion channel
  activity (voltage-gated anion/chloride channel; the gene drives stomatal
  *closure*). The K⁺-channel-inhibitor activity is a secondary/regulatory
  "moonlighting" activity. If the review is deciding whether GO:0019870 should be
  a prominent/core term, the answer is **no — keep it, but mark non-core**.
- **Alternative/parent term consideration:** GO:0015459 (potassium channel
  regulator activity) is the more conservative parent if a curator judges
  "inhibitor" too strong given the single-study, heterologous basis. Given the
  data *do* show inhibition (not activation), GO:0019870 is biologically correct;
  the conservatism concern is about evidential strength, not direction.
- **Associated BP:** negative regulation of stomatal opening / regulation of
  stomatal movement is reasonable but is largely a downstream/physiological
  outcome and is confounded by the Laanemets loss-of-function result.

---

## Mechanistic Scope

- **Immediate molecular activity being tested:** SLAC1 protein binding to Shaker
  inward-K⁺ channel subunits (KAT1, AKT2) and reduction of their K⁺in conductance
  — i.e., a channel–channel inhibitory protein–protein interaction.
- **Directly supported (in the one study):** physical interaction (Y2H/co-IP) and
  current inhibition in oocytes.
- **Downstream / inferred, not the molecular activity itself:** suppression of
  light-induced stomatal opening; drought/ABA physiology. These are pathway-level
  consequences shown mainly by overexpression and are confounded in loss-of-function
  by Ca²⁺-sensitivity feedback.
- **Selectivity note:** binding ≠ inhibition. SLAC1 binds KAT2 in Y2H yet does not
  inhibit it; this dissociation argues for a specific functional, not merely
  steric/co-localization, effect on KAT1/AKT2 — a point in the hypothesis's favor.

---

## Conflicts and Alternatives

1. **Directional contradiction (Laanemets 2013, PMID:23126621).** Loss of SLAC1
   lowers, not raises, K⁺in. Explained by elevated cytosolic [Ca²⁺] increasing
   Ca²⁺-sensitivity-mediated K⁺in inhibition — an **alternative mechanism** that
   does not require direct SLAC1–KAT1 contact.
2. **Kinase-route alternative (Acharya 2013, PMID:24033256).** OST1 interacts with
   both SLAC1 and KAT1 and inhibits K⁺in; K⁺in suppression during closure may be
   dominated by kinase signaling rather than direct anion-channel binding.
3. **Autoinhibition reinterpretation (Qin 2024, PMID:38985761).** The SLAC1 N/C
   termini that Zhang 2016 implicate in KAT1 binding are the same cytosolic
   regulatory domains that mediate SLAC1 *autoinhibition*; constructs/overexpression
   effects attributed to KAT1 binding deserve scrutiny.
4. **Heterologous-system artifact.** Oocyte overexpression of a membrane protein can
   non-specifically depress co-expressed channel currents (membrane crowding,
   trafficking competition); KAT2 serving as a negative control mitigates but does
   not eliminate this.
5. **Paralog/term carry-over risk:** SLAH3 (SLAC1 homolog) inhibits different K⁺
   channels (GORK/SKOR). Curators should avoid propagating GO:0019870 across the
   SLAC/SLAH family by homology — the specific K⁺ targets differ per paralog.

---

## Knowledge Gaps

- **Independent functional replication (highest priority).** Checked: 45 citing
  papers; none reproduce SLAC1→KAT1/AKT2 patch-clamp inhibition independently.
  Resolution: an independent guard-cell patch-clamp or oocyte study.
- **Clean loss-of-function test.** Does *slac1* enhance K⁺in once the Ca²⁺ feedback
  is clamped out (Laanemets' <10 nM [Ca²⁺] condition)? This is the decisive in-planta
  test of direct inhibition and has not been reported.
- **Native interaction evidence.** IntAct has no SLAC1 records; no reported
  endogenous co-IP from guard-cell tissue (as opposed to oocyte overexpression).
- **AKT2 specificity.** Full-text confirms AKT2 K⁺in inhibition (Suppl. Fig. 2), but
  this rests on one supplemental figure; independent confirmation absent.
- **Structural basis.** No structure of a SLAC1–KAT1 complex; unknown whether
  binding occludes the pore/voltage sensor or alters gating/trafficking.

---

## Discriminating Tests

1. **Ca²⁺-clamped *slac1* patch clamp:** measure guard-cell K⁺in in *slac1* vs WT
   with cytosolic [Ca²⁺] buffered <10 nM. Direct-inhibition model predicts *higher*
   K⁺in in *slac1*; Ca²⁺-feedback model predicts rescue to WT levels.
2. **Non-conducting SLAC1 point mutants:** test whether a pore-dead SLAC1 (anion
   transport abolished) still inhibits KAT1 — separates the inhibitor activity from
   anion-channel function.
3. **Interface-mutant SLAC1:** map the KAT1-binding surface and test a binding-dead,
   transport-competent SLAC1 for loss of K⁺in inhibition while retaining closure.
4. **Endogenous proximity assay:** split-luciferase/BiFC or co-IP from native guard
   cells (not overexpression) ± drought to show the interaction occurs at
   physiological levels.
5. **Quantitative stoichiometry:** compare SLAC1:KAT1 abundance in guard cells to
   judge whether direct binding can plausibly titrate KAT1 in planta.

---

## Curation Leads (require curator verification)

- **Lead 1 — Retain GO:0019870 as a non-core MF annotation** with an explicit
  caveat that evidence is from a single study using heterologous oocyte voltage
  clamp plus guard-cell overexpression (IDA), supported by IPI (Y2H/co-IP), and is
  not independently replicated. Verify snippet: *"Voltage-clamp results demonstrated
  that SLAC1 inhibited KAT1 dramatically, but did not inhibit KAT2."* (PMID:27002025).
- **Lead 2 — Add a NOT/contrast note on specificity:** SLAC1 binds KAT2 (Y2H) but
  does **not** inhibit it; do not annotate KAT2 inhibition. Verify snippet: full-text
  "SLAC1 Strongly Inhibits KAT1, but Not KAT2, in Xenopus laevis Oocytes."
- **Lead 3 — Flag competing mechanism:** cite PMID:23126621 as a qualifier that
  in-planta *slac1* K⁺in reduction is Ca²⁺-mediated, not a relief-of-direct-inhibition
  effect. Verify snippet: *"severely reduced activity of inward K+ (K+in) channels in
  slac1 guard cells."*
- **Lead 4 — Do not homology-propagate** GO:0019870 to SLAH3/other SLAC paralogs;
  SLAH3's K⁺ targets (GORK/SKOR, outward) differ (PMID:36653170).
- **Candidate alternative term if curator deems "inhibitor" too strong:** GO:0015459
  potassium channel regulator activity (direction still supports "inhibitor").
- **Suggested curator question:** Is a single-lab, heterologous + overexpression
  result sufficient for an experimental MF annotation given the opposite-direction
  loss-of-function phenotype? If policy requires independent corroboration for core
  terms, keep GO:0019870 as non-core only.

---

## Supported vs Refuted Clauses of the Seed Hypothesis

| Clause | Status |
|---|---|
| SLAC1 physically interacts with KAT1 and AKT2 (not AKT1) | **Supported** (Zhang 2016; single study; not in IntAct) |
| SLAC1 directly inhibits KAT1 and AKT2 K⁺in | **Supported in vitro** (oocyte; single study) |
| SLAC1 does not inhibit KAT2 | **Supported** (binds but does not inhibit) |
| Inhibition contributes to suppression of stomatal opening in planta | **Partially supported** (gain-of-function only; loss-of-function is opposite, Ca²⁺-confounded) |
| Independently replicated or corroborated | **Not met** (concept corroborated via analogues; SLAC1–KAT1 not independently replicated) |
| Not contradicted by later work | **Partially contradicted / qualified** (Laanemets 2013 directional conflict; Qin 2024 autoinhibition reinterpretation) |

*Analyses run across iterations: NCBI E-utilities (efetch/elink/esummary) for the
reference paper, full-text AKT2/patch-clamp verification from PMC4863386, cited-by
screen of all 45 papers citing Zhang 2016, IntAct web-service interactor query for
Q9LD83 (19 interactors, all kinases/phosphatases), and UniProt/QuickGO MF-annotation
checks confirming GO:0019870 is not currently annotated.*

**Provenance artifacts (computed this run):** `evidence_matrix.csv`,
`go_decision_table.csv`, `hypothesis_clause_verdicts.csv` in the job directory.


## Artifacts

- [OpenScientist evidence matrix](openscientist_artifacts/evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/go_decision_table.csv)
- [OpenScientist hypothesis clause verdicts](openscientist_artifacts/hypothesis_clause_verdicts.csv)