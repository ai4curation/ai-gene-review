---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T21:43:52.188544'
end_time: '2026-09-20T22:06:09.095688'
duration_seconds: 1336.91
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ABCD4
  gene_symbol: ABCD4
  uniprot_accession: O14678
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: fatty-acid-functions-and-peroxisome-organization
  hypothesis_text: Human ABCD4 retains fatty acid transmembrane transporter activity,
    fatty acid beta-oxidation participation, very-long-chain fatty acid biosynthesis
    participation, or peroxisome organization. Adjudicate these four claims separately
    using their actual GO definitions, direct substrate experiments, pathway mechanism
    and relevant phylogenetic branches. Its demonstrated lysosomal cobalamin transport
    function does not alone establish loss of alternative substrates or indirect peroxisome
    organization. Distinguish direct negative localization assays from evidence about
    these activities/processes.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/ABCD4/ABCD4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human ABCD4 retains fatty acid transmembrane transporter\
    \ activity, fatty acid beta-oxidation\n  participation, very-long-chain fatty\
    \ acid biosynthesis participation, or peroxisome organization. Adjudicate\n  these\
    \ four claims separately using their actual GO definitions, direct substrate experiments,\
    \ pathway\n  mechanism and relevant phylogenetic branches. Its demonstrated lysosomal\
    \ cobalamin transport function\n  does not alone establish loss of alternative\
    \ substrates or indirect peroxisome organization. Distinguish\n  direct negative\
    \ localization assays from evidence about these activities/processes.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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
- **Gene directory:** ABCD4
- **Gene symbol:** ABCD4
- **UniProt accession:** O14678

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** fatty-acid-functions-and-peroxisome-organization
- **Source file:** genes/human/ABCD4/ABCD4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ABCD4 retains fatty acid transmembrane transporter activity, fatty acid beta-oxidation participation, very-long-chain fatty acid biosynthesis participation, or peroxisome organization. Adjudicate these four claims separately using their actual GO definitions, direct substrate experiments, pathway mechanism and relevant phylogenetic branches. Its demonstrated lysosomal cobalamin transport function does not alone establish loss of alternative substrates or indirect peroxisome organization. Distinguish direct negative localization assays from evidence about these activities/processes.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human ABCD4 retains fatty acid transmembrane transporter activity, fatty acid beta-oxidation
  participation, very-long-chain fatty acid biosynthesis participation, or peroxisome organization. Adjudicate
  these four claims separately using their actual GO definitions, direct substrate experiments, pathway
  mechanism and relevant phylogenetic branches. Its demonstrated lysosomal cobalamin transport function
  does not alone establish loss of alternative substrates or indirect peroxisome organization. Distinguish
  direct negative localization assays from evidence about these activities/processes.
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

# ABCD4 (O14678) — Adjudication of Fatty-Acid & Peroxisome Function Claims

**Focus:** function_assignment · hypothesis `fatty-acid-functions-and-peroxisome-organization`
**Source:** `genes/human/ABCD4/ABCD4-ai-review.yaml` (free-text)
**Date:** 2026-09-21 · Iteration 1

---

## Executive Judgment

**Verdict: Over-annotated / Refuted for all four claims (as direct ABCD4 functions).**

The seed hypothesis proposes that human ABCD4 *retains* (i) fatty acid transmembrane
transporter activity, (ii) fatty acid β-oxidation participation, (iii) very-long-chain
fatty acid (VLCFA) biosynthesis participation, or (iv) peroxisome organization.
Adjudicating each claim separately against its actual GO definition, the evidence
codes on ABCD4, direct substrate/localization experiments, and the ABCD-subfamily
phylogeny:

- **None of the four claims has any experimental support on ABCD4.** In EBI QuickGO
  (O14678, 55 annotations), every one of these terms is annotated **only by IBA**
  (Inferred from Biological Ancestor, ECO:0000318, GO_Central, GO_REF:0000033) — i.e.
  phylogenetically propagated from the ABCD1–3 ancestor, not from an ABCD4 experiment.
- **Claim 3 is factually mis-stated:** the *biosynthetic* term GO:0042761 is **not
  annotated to ABCD4 at all**; only the *catabolic* term GO:0042760 (also IBA-only) is
  present. ABC-D transporters import substrate for β-oxidation (catabolism), so a
  biosynthesis assignment is mechanistically backwards regardless.
- **Claim 4 (peroxisome organization) is contradicted by direct localization data:**
  ABCD4 localizes to the **ER and lysosome, not peroxisomes**, because it lacks the
  N-terminal peroxisomal-targeting region conserved in ABCD1–3 (PMID:19010322,
  27456980, 27766264).
- **The experimentally grounded core function is lysosomal cobalamin (vitamin B12)
  export** (PMID:22922874, 33845046, 31467407, 42303638), with MF term
  GO:0015420 supported by EXP/IDA/IMP.

The demonstrated cobalamin role does not, by itself, prove ABCD4 *cannot* carry a
fatty-acyl substrate — but the burden of a positive claim is unmet: there is no direct
ABCD4 fatty-acid transport/β-oxidation assay, no peroxisomal residence, and the
biosynthesis term is absent. **Recommended action: treat all four claims as non-core;
do not assert them as ABCD4 functions.**

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| QuickGO O14678 (retrieved 2026-09-21) | Database (evidence codes) | Refutes (as direct claims) | 1–4 | All four seed terms are **IBA-only**; GO:0042761 (VLCFA biosynthesis) not annotated at all | Human, curated GO | High for provenance; IBA ≠ experiment |
| 19010322 (Kashiwayama 2009) | Localization (IF, deletion constructs) | Refutes | 4 (peroxisome) | P70R/ABCD4 localizes to **ER, not peroxisomes**; lacks N-terminal hydrophilic peroxisomal-targeting region present in ABCD1–3 | CHO cells, transfected | High; overexpression system |
| 27456980 (Kawaguchi 2016) | Localization + interaction | Refutes / qualifies | 4 | Endogenous ABCD4 is ER+lysosome; lysosomal delivery requires escort LMBD1 (lost on LMBRD1 KO) | Human cells | High; direct endogenous assay |
| 27766264 (Kawaguchi & Morita 2016) | Review synthesis | Supports (reframing) | 1–4 | ABCD1–3 = peroxisomal VLCFA/branched acyl-CoA transporters; **ABCD4 = lysosomal, vitamin B12** — explicit functional separation | Review | Review-level; well-supported |
| 22922874 (Coelho 2012) | Mutant phenotype + localization | Refutes (legacy) / supports core | 4 + core | cblJ mutations block **lysosomal cobalamin release**; ABCD4 colocalizes LAMP1/LMBD1; gene "previously thought to have peroxisomal localization and function" | Human patients/fibroblasts | High; landmark primary study |
| 33845046 (Reactome/UniProt EXP) | Direct assay (EXP/IDA/IMP) | Supports core | core MF | ABC-type **vitamin B12 transporter activity** (GO:0015420) experimentally supported | Human | High |
| 31467407 (Xu 2019) | Structure (cryo-EM) | Supports core | core | Cryo-EM of human **lysosomal cobalamin exporter ABCD4** | Recombinant human protein | High |
| 42303638 (Liu 2026) | Structure (cryo-EM) | Supports core | core / 4 | ABCD4–LMBD1 complex; cobalamin recognition & transport cycle; LMBD1-dependent lysosomal trafficking | Recombinant human | High |
| 23141461 (Kim 2012) | Mutant phenotype | Supports core | core | cblJ ABCD4 mutation blocks cobalamin transport lysosome→cytoplasm | Human patient | High |
| 28572511 (Fettelschoss 2017) | Interaction/mechanism | Supports core | core | ABCD4 ATPase/clinical mutations disrupt cobalamin-pathway interaction | Human | Moderate–high |
| 9302272 / 14533738 (old) | Localization (IDA) | Competing/legacy | 4 | Older IDA "peroxisome" CC annotations | Human | Low; superseded by targeted studies |
| This report (computed, UniProt seqs) | Structural/evolutionary | Qualifies/supports | 1–4 | ABCD4 shares only ~34% identity with ABCD1–3 (mean 33.8%) vs 49.2% among ABCD1/2/3; ABCD4 is shortest (606 aa), lacking the N-terminal peroxisomal-targeting extension | Human paralogs, NW global alignment | Medium; identity alone ≠ substrate, but aligns with demonstrated functional divergence |
| 33729671 / 23141461 / 22922874 (cblJ patients) | Mutant phenotype | Refutes (indirectly) | 1–4 | cblJ disease signature is combined **methylmalonic acidemia + homocystinuria** (a cobalamin phenotype); **no VLCFA accumulation / peroxisomal-disease phenotype** reported | Human patients | Medium; absence-of-report, not a systematic VLCFA assay |

Provenance artifacts: `/tmp/abcd4_claim_evidence_matrix.csv` (QuickGO evidence codes) and the
computed pairwise Needleman-Wunsch %identity table below (ABCD1–4).

**Computed ABCD subfamily divergence (NW global alignment, match+1/mismatch−1/gap−1):**

| Pair | % identity |
|---|---|
| ABCD1–ABCD2 | 64.9 |
| ABCD1–ABCD3 | 40.7 |
| ABCD2–ABCD3 | 42.1 |
| **ABCD1–ABCD4** | **32.2** |
| **ABCD2–ABCD4** | **33.1** |
| **ABCD3–ABCD4** | **36.0** |
| ABCD4 vs ABCD1-3 (mean) | 33.8 |
| ABCD1/2/3 among themselves (mean) | 49.2 |

ABCD4 is the divergent out-group of the subfamily and the shortest member (606 aa vs
659–745 aa), consistent with the missing N-terminal peroxisomal-targeting region — the
branch across which the IBA fatty-acid/peroxisome terms were propagated is exactly the
weak, long branch where phylogenetic inference is least reliable.

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current evidence on ABCD4 | Recommended action |
|---|---|---|---|
| GO:0005324 long-chain fatty acid transmembrane transporter activity (≈ seed GO:0015245) | MF | IBA only | **Do not assert as core; candidate for removal/NOT.** No direct substrate assay; propagated from ABCD1–3. |
| GO:0006635 fatty acid β-oxidation | BP | IBA only | **Non-core / candidate removal.** No pathway participation shown for ABCD4. |
| GO:0042761 VLCFA biosynthetic process | BP | **Not annotated** | Claim unsupported; if a curator was tempted to add it, **do not** — mechanistically backwards and absent. |
| GO:0042760 VLCFA catabolic process | BP | IBA only | **Non-core / candidate removal.** |
| GO:0007031 peroxisome organization | BP | IBA only | **Candidate removal; contradicted** by ER/lysosomal localization. |
| GO:0005777 peroxisome / GO:0005778 peroxisomal membrane | CC | old IDA / IBA | **Deprecate in favor of** lysosome/ER; flag as superseded. |
| GO:0015420 ABC-type vitamin B12 transporter activity | MF | EXP/IDA/IMP | **Retain as core MF.** |
| GO:0015889 cobalamin transport; GO:0009235 cobalamin metabolic process | BP | IMP/IDA/TAS | **Retain as core BP.** |
| GO:0005765 lysosomal membrane | CC | EXP/IDA | **Retain as core CC.** |

Not recommending "protein binding" (GO:0005515) as a substantive call — a specific,
better-supported set of cobalamin terms is available.

---

## Mechanistic Scope

- **Immediate molecular function tested:** ATP-driven transmembrane transport of a
  small-molecule substrate. ABCD4's demonstrated substrate is **cobalamin**, exported
  from the lysosomal lumen to the cytosol (handoff toward MMACHC), not a fatty
  acyl-CoA.
- **Direct activity vs. downstream:** The fatty-acid β-oxidation and VLCFA claims are
  *pathway-level* processes that in ABCD1–3 follow acyl-CoA import into peroxisomes.
  For ABCD4 there is neither the transport step (no assay) nor the compartment
  (not peroxisomal), so any such role would be inference, not direct activity.
- **Peroxisome organization** is an organelle-biogenesis process; ABCD4 is not a
  peroxisomal resident, removing the mechanistic basis for a direct role.

---

## Conflicts and Alternatives

- **Paralog over-annotation (primary explanation):** ABCD4 shares the ABC-D
  half-transporter architecture with ABCD1 (X-ALD, VLCFA-CoA), ABCD2, and ABCD3
  (branched acyl-CoA). GO's IBA pipeline propagates the ancestral fatty-acid/peroxisome
  functions to ABCD4. This is exactly the "frequency bias / paralog carry-over" the
  seed warns about.
- **Historical naming:** ABCD4 = "P70R / PMP69," named as a peroxisomal-membrane-protein
  relative, seeding legacy peroxisome CC annotations (PMID:9302272, 14533738) later
  overturned (PMID:19010322, 22922874).
- **Seed's own term error:** the VLCFA claim names the *biosynthetic* process
  (GO:0042761), which is not annotated; only catabolic (GO:0042760) exists — reinforcing
  that the claim is loose paralog carry-over rather than a curated ABCD4 assignment.
- **Human loss-of-function phenotype is cobalamin-specific:** cblJ patients (ABCD4
  biallelic mutations) present with combined **methylmalonic acidemia + homocystinuria**
  (PMID:22922874, 23141461, 33729671) — the cobalamin signature — with **no reported
  VLCFA accumulation or peroxisomal-disease phenotype** (contrast X-linked ALD from
  ABCD1). This is indirect negative evidence against a physiologically important
  fatty-acid role, though not a systematic VLCFA measurement.
- **Sequence divergence (computed):** ABCD4 shares only ~34% identity with ABCD1–3
  (vs 49% among the peroxisomal trio) and lacks their N-terminal targeting extension,
  so IBA transfer of ABCD1–3 attributes across this long branch is unreliable.
- **Not fully excluded:** no experiment has directly tested whether ABCD4 can bind/move
  a fatty-acyl species in vitro. Absence of evidence is not proof of substrate
  exclusivity — but it is insufficient to *assert* the function.

---

## Knowledge Gaps

1. **Direct substrate specificity of ABCD4.** Checked: no reconstitution/transport assay
   with fatty-acyl-CoA substrates found. Matters because it would positively confirm or
   exclude a residual lipid-transport activity. Resolve with proteoliposome transport
   assays comparing cobalamin vs. (V)LCFA-CoA.
2. **Whether IBA annotations should be experimentally overridden.** Checked: GO_Central
   IBA present for all four. Matters for curation policy: IBA can be retained but should
   not outrank direct experimental CC/MF. A NOT-qualifier or removal request is the lead.
3. **Fate of legacy peroxisome CC annotations.** Checked: old IDA still present in
   QuickGO. Matters because CC drives downstream inference. Resolve by curator review
   citing PMID:19010322/22922874/27456980.

---

## Discriminating Tests

- **In vitro transport / ATPase stimulation** of purified ABCD4 (±LMBD1) with cobalamin
  vs. C22:0/C24:0-CoA and branched acyl-CoA — the decisive substrate-specificity test.
- **Comparative localization** (endogenous, tagged CRISPR knock-in) vs. peroxisomal
  (PMP70/ABCD3) and lysosomal (LAMP1) markers — confirms non-peroxisomal residence.
- **VLCFA / plasma C26:0 profiling** in cblJ (ABCD4-deficient) patient fibroblasts vs.
  X-ALD (ABCD1) cells — if ABCD4 contributed to VLCFA handling, C26:0 should rise; the
  prediction under this report is **no VLCFA accumulation** in cblJ.
- **Phylogenetic branch-length / ancestral-state check** confirming the fatty-acid GO
  terms trace to the ABCD1–3 clade rather than a demonstrated ABCD4 attribute.

---

## Curation Leads (require curator verification)

- **Action changes:** Mark GO:0005324, GO:0006635, GO:0042760, GO:0007031 (and any
  GO:0015245 if present) as **non-core / candidate removal or NOT** on ABCD4, noting they
  are IBA-only paralog propagation. Do **not** add GO:0042761 (VLCFA biosynthesis).
- **Retain as core:** GO:0015420 (MF), GO:0015889 + GO:0009235 (BP), GO:0005765 (CC).
- **Reconcile CC:** deprecate/annotate-superseded the legacy peroxisome CC terms in
  favor of lysosome/ER.
- **Candidate references + snippets to verify:**
  - PMID:19010322 — "P70R-HA was localized to the endoplasmic reticulum (ER), not to peroxisomes."
  - PMID:27456980 — "ABCD4 does not localize to peroxisomes but rather, the endoplasmic reticulum (ER), because it lacks the NH2-terminal hydrophilic region required for peroxisomal targeting."
  - PMID:27766264 — "ABCD1-3 and ABCD4 are localized to peroxisomes and lysosomes, respectively."
  - PMID:22922874 — "ABCD4, a gene that codes for an ABC transporter, which was previously thought to have peroxisomal localization and function."
- **Suggested questions for curator:** Are the four IBA fatty-acid/peroxisome terms
  worth retaining given definitive lysosomal/cobalamin evidence, or should they be
  removed/NOT-qualified to prevent downstream propagation?
- **Suggested experiments:** proteoliposome substrate panel; cblJ-fibroblast VLCFA
  profiling (see Discriminating Tests).

---

### Limitations
IBA/evidence-code snapshot reflects QuickGO on 2026-09-21 and may differ from the
review's frozen release. No wet-lab exclusion of fatty-acyl transport by ABCD4 exists;
this report distinguishes *absence of positive evidence* from *proven exclusivity*.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)