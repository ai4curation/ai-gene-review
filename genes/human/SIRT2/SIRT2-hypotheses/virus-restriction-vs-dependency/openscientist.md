---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-23T23:50:03.592692'
end_time: '2026-09-24T00:02:21.580866'
duration_seconds: 737.99
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SIRT2
  gene_symbol: SIRT2
  uniprot_accession: Q8IXJ6
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: virus-restriction-vs-dependency
  hypothesis_text: SIRT2 has defense response to virus (GO:0051607).
  term_context: '- Term: defense response to virus (GO:0051607)

    - Decisive question: determine the SIGN of human SIRT2''s effect on virus replication.
    Does depletion or inhibition of SIRT2 INCREASE infectious viral progeny (SIRT2
    acting as a host restriction factor, consistent with GO:0051607), or DECREASE
    it (SIRT2 acting as a host dependency factor that viruses require)? Settle the
    sign before judging the GO assignment.

    - Published perturbation experiments exist pointing in BOTH directions, in some
    cases from overlapping author groups. Do not settle this by citation count, journal
    or recency. Weigh perturbation type (siRNA knockdown, genetic knockout, small-molecule
    inhibition, sirtuin activation), virus identity and family, cell system, and whether
    the readout is infectious progeny titre or a surrogate such as viral transcript
    or protein level.

    - Consider explicitly whether the direction is virus-specific rather than uniform:
    whether SIRT2 restricts some viruses while being required by others. State whether
    a single unqualified defense-response-to-virus assignment to human SIRT2 (UniProt
    Q8IXJ6) is warranted, or whether the evidence supports only virus-specific statements.
    Deliverable: a direction verdict (restriction factor / dependency factor / virus-specific
    / unresolved) with the decisive experiments, their PMIDs or DOIs, and contrary
    evidence.'
  reference_context: No specific reference context supplied.
  source_file: genes/human/SIRT2/SIRT2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: SIRT2 has defense response to virus (GO:0051607).\n\
    focus_type: function_assignment\nterm_id: GO:0051607\nterm_label: defense response\
    \ to virus\ncontext:\n- 'Decisive question: determine the SIGN of human SIRT2''s\
    \ effect on virus replication. Does depletion\n  or inhibition of SIRT2 INCREASE\
    \ infectious viral progeny (SIRT2 acting as a host restriction factor,\n  consistent\
    \ with GO:0051607), or DECREASE it (SIRT2 acting as a host dependency factor that\
    \ viruses require)?\n  Settle the sign before judging the GO assignment.'\n- Published\
    \ perturbation experiments exist pointing in BOTH directions, in some cases from\
    \ overlapping\n  author groups. Do not settle this by citation count, journal\
    \ or recency. Weigh perturbation type (siRNA\n  knockdown, genetic knockout, small-molecule\
    \ inhibition, sirtuin activation), virus identity and family,\n  cell system,\
    \ and whether the readout is infectious progeny titre or a surrogate such as viral\
    \ transcript\n  or protein level.\n- 'Consider explicitly whether the direction\
    \ is virus-specific rather than uniform: whether SIRT2 restricts\n  some viruses\
    \ while being required by others. State whether a single unqualified defense-response-to-virus\n\
    \  assignment to human SIRT2 (UniProt Q8IXJ6) is warranted, or whether the evidence\
    \ supports only virus-specific\n  statements. Deliverable: a direction verdict\
    \ (restriction factor / dependency factor / virus-specific\n  / unresolved) with\
    \ the decisive experiments, their PMIDs or DOIs, and contrary evidence.'\nreference_id:\
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
citation_count: 14
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
- **Gene directory:** SIRT2
- **Gene symbol:** SIRT2
- **UniProt accession:** Q8IXJ6

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** virus-restriction-vs-dependency
- **Source file:** genes/human/SIRT2/SIRT2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

SIRT2 has defense response to virus (GO:0051607).

## Term and Decision Context

- Term: defense response to virus (GO:0051607)
- Decisive question: determine the SIGN of human SIRT2's effect on virus replication. Does depletion or inhibition of SIRT2 INCREASE infectious viral progeny (SIRT2 acting as a host restriction factor, consistent with GO:0051607), or DECREASE it (SIRT2 acting as a host dependency factor that viruses require)? Settle the sign before judging the GO assignment.
- Published perturbation experiments exist pointing in BOTH directions, in some cases from overlapping author groups. Do not settle this by citation count, journal or recency. Weigh perturbation type (siRNA knockdown, genetic knockout, small-molecule inhibition, sirtuin activation), virus identity and family, cell system, and whether the readout is infectious progeny titre or a surrogate such as viral transcript or protein level.
- Consider explicitly whether the direction is virus-specific rather than uniform: whether SIRT2 restricts some viruses while being required by others. State whether a single unqualified defense-response-to-virus assignment to human SIRT2 (UniProt Q8IXJ6) is warranted, or whether the evidence supports only virus-specific statements. Deliverable: a direction verdict (restriction factor / dependency factor / virus-specific / unresolved) with the decisive experiments, their PMIDs or DOIs, and contrary evidence.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: SIRT2 has defense response to virus (GO:0051607).
focus_type: function_assignment
term_id: GO:0051607
term_label: defense response to virus
context:
- 'Decisive question: determine the SIGN of human SIRT2''s effect on virus replication. Does depletion
  or inhibition of SIRT2 INCREASE infectious viral progeny (SIRT2 acting as a host restriction factor,
  consistent with GO:0051607), or DECREASE it (SIRT2 acting as a host dependency factor that viruses require)?
  Settle the sign before judging the GO assignment.'
- Published perturbation experiments exist pointing in BOTH directions, in some cases from overlapping
  author groups. Do not settle this by citation count, journal or recency. Weigh perturbation type (siRNA
  knockdown, genetic knockout, small-molecule inhibition, sirtuin activation), virus identity and family,
  cell system, and whether the readout is infectious progeny titre or a surrogate such as viral transcript
  or protein level.
- 'Consider explicitly whether the direction is virus-specific rather than uniform: whether SIRT2 restricts
  some viruses while being required by others. State whether a single unqualified defense-response-to-virus
  assignment to human SIRT2 (UniProt Q8IXJ6) is warranted, or whether the evidence supports only virus-specific
  statements. Deliverable: a direction verdict (restriction factor / dependency factor / virus-specific
  / unresolved) with the decisive experiments, their PMIDs or DOIs, and contrary evidence.'
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

# SIRT2 and "defense response to virus" (GO:0051607): Restriction vs. Dependency

**Gene:** SIRT2 (human) · **UniProt:** Q8IXJ6 · **Taxon:** NCBITaxon:9606
**Focus:** function_assignment · **Seed hypothesis:** *SIRT2 has defense response to virus (GO:0051607)*
**Deliverable:** direction verdict + decisive experiments + contrary evidence

---

## Executive Judgment

**Verdict: REFUTED as an unqualified assignment / OVER-ANNOTATION. Direction is VIRUS-SPECIFIC, and the preponderance of decisive perturbation evidence points to SIRT2 acting as a host DEPENDENCY (pro-viral) factor — the opposite sign to GO:0051607.**

A single, unqualified "defense response to virus" annotation on human SIRT2 is **not warranted**. The sign of SIRT2's effect on virus replication is not uniform, and where the readout is *infectious progeny titre* (the decisive metric), SIRT2 behaves as a factor that viruses **require**, not one that restricts them:

- **Both decisive infectious-progeny studies point pro-viral.** In dengue, a SIRT2-directed inhibitor reduces release of infectious progeny and the effect is abolished by SIRT2 knockdown (on-target; PMID 34147476). In HIV-1, a SIRT2 inhibitor reduces viral growth by >1 log₁₀ in macrophages and humanized mice (PMID 41883165).
- **HBV (6 studies, multiple perturbation types)** consistently shows SIRT2 *promotes* replication: overexpression increases HBV nucleic acids (PMID 35663860), and three independent chemical inhibitors/modulators (AGK2 — PMID 30275764, 40270769; FLS-359 — PMID 38641024) suppress HBV.
- **HSV-1:** SIRT2 *suppresses* the antiviral cGAS-STING/type-I-IFN axis, so SIRT2 loss or inhibition *increases* interferon and clears virus (PMID 37870259) — again pro-viral.

**Contrary evidence exists but is weaker for GO:0051607.** The antiviral (restriction-like) direction rests on (i) influenza, where SIRT2 *activation* lowers replication via redox restoration (PMID 35071051) — an activation gain-of-function with a surrogate readout, not loss-of-function; (ii) SIRT2 support of IFN-stimulated-gene transcription via CDK9/STAT1 (PMID 30487288) — a signaling surrogate, no viral titre; and (iii) a minor alternatively spliced isoform 5 that inhibits HBV (PMID 32493816) — isoform-specific and opposite to the dominant isoform 1.

**Key caveat / important curation fact:** A QuickGO query of all 206 GO annotations on Q8IXJ6 found **no existing viral-defense annotation** (GO:0051607 and all related/descendant viral terms return 0 hits). The seed is therefore a **proposed addition**, and the evidence does not support adding it in unqualified form.

---

## Evidence Matrix

| Citation | Evidence type | Stance vs seed | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID:35663860 | Direct assay / overexpression | **Refutes** | Does SIRT2 promote HBV? | Ectopic SIRT2 ↑ HBV RNAs, 3.5-kb RNA, core DNA (via p53) | HBV-infected HepG2-NTCP | Med–High; surrogate (RNA/DNA), gain-of-function |
| PMID:29366781 | Overexpression / pathway | **Refutes** | HBx→SIRT2→replication | SIRT2 facilitates HBV transcription/replication; HBx upregulates SIRT2 | Hepatoma cells | Med; surrogate readout |
| PMID:30111572 | Direct assay (isoform 1) | **Refutes** | SIRT2 isoform 1 vs HBV | Isoform 1 enhances HBV via AKT/GSK-3β/β-catenin | Hepatoma cells | Med; surrogate readout |
| PMID:30275764 | Small-molecule inhibition | **Refutes** | Does SIRT2 inhibition ↓HBV? | AGK2 inhibits HBV replication | HBV cell model | Med; inhibitor specificity |
| PMID:40270769 | Small-molecule inhibition | **Refutes** | AGK2 epigenetic anti-HBV | AGK2 ↓SIRT2, ↓HBV RNA/DNA, ↓cccDNA (repressive histone marks) | HBV-transfected/infected cells | Med–High; surrogate but mechanistic |
| PMID:38641024 | Allosteric inhibition | **Refutes** | SIRT2 needed for cccDNA? | FLS-359 (SIRT2 modulator) blocks cccDNA establishment & transcription | HBV infection model | Med–High; surrogate (cccDNA) |
| **PMID:34147476** | Inhibitor + siRNA (rescue) | **Refutes** | SIRT2 required for DENV? | Tenovin-1 ↓ **infectious progeny release**; effect abolished by SIRT2 knockdown (on-target) | DENV1–4, BHK-21/Vero | **High; decisive infectious-titre readout + genetic on-target control** |
| **PMID:41883165** | Small-molecule inhibition | **Refutes** | SIRT2 required for HIV-1? | Sirtinol ↓ HIV-1 growth **>1 log₁₀** | Human macrophages; humanized mice | High; titre-like readout, in vivo |
| PMID:36719240 | Association / biomarker | **Refutes** | SIRT2 vs HIV load | Plasma SIRT2 ↑ with viral loads & provirus levels | People living with HIV | Low–Med; correlational |
| PMID:37870259 | KO + inhibitor + interaction | **Refutes** | SIRT2 vs antiviral IFN | SIRT2 deacetylates G3BP1, suppresses cGAS-STING; deficiency ↑IFN; AGK2 protects mice from HSV-1 | HSV-1; mouse; cell | High; loss-of-function ↑ antiviral response |
| PMID:40220296 | Mutant phenotype | **Qualifies** | SIRT2 in COVID severity | SIRT2 suppresses aging cGAS; SIRT2-KO aged mice get *severe* COVID | Aged mice, SARS-CoV-2 | Med; **disease severity/immunopathology, not viral restriction** |
| PMID:35071051 | Sirtuin **activation** | **Supports** | Does SIRT2 restrict IAV? | SIRT2 activator restores G6PD/NRF2/GSH redox, ↓IAV replication; virus downregulates SIRT2 | Influenza A, cell culture | Med; **activation GoF + surrogate readout, not LoF titre** |
| PMID:30487288 | Signaling assay | **Supports** | SIRT2 in IFN response | SIRT2 required for ISG transcription via CDK9 deacetylation / STAT1-Ser727 | MEFs / cells | Med; signaling surrogate, no viral titre |
| PMID:32493816 | Isoform assay | **Supports (isoform)** | Isoform 5 vs HBV | Alt-spliced SIRT2 isoform 5 *inhibits* HBV from cccDNA (repressive epigenetics) | HBV cell model | Med; **minor isoform, opposite to isoform 1** |

*Tally: 10 refute (pro-viral/dependency), 3 support (all activation-based, signaling-surrogate, or minor-isoform), 1 qualifies (anti-inflammatory protection, not restriction). Provenance: evidence-matrix code + output executed in Iteration 2; CSV saved to the code sandbox at `/tmp/sirt2_virus_evidence_matrix.csv`.*

---

## GO Curation Implications (leads requiring curator verification)

- **GO:0051607 (defense response to virus, BP):** **Do NOT add as an unqualified annotation.** It is not currently in the GO record for Q8IXJ6 (QuickGO: 0 hits), and the primary literature does not support a uniform host-restriction role. If any viral statement is captured at all, it should be **virus-qualified** and directionally correct.
- The **dominant, mechanistically coherent** signal (HBV, dengue, HIV-1, HSV-1) is that SIRT2 is **pro-viral / permissive**. If a curator wishes to record this, the accurate directional term is closer to **positive regulation of viral genome replication (GO:0045070)** or **negative regulation of type I interferon-mediated / innate immune response** (e.g., via GO:0032480 negative regulation of type I IFN production), each **paper- and virus-specific with the appropriate NOT/qualifier discipline** — **not** GO:0051607.
- **Preferred core annotations remain the well-supported ones:** NAD⁺-dependent protein/α-tubulin deacetylase activity (MF), protein deacetylation (GO:0006476, BP, IDA), and cytoplasm/microtubule/centrosome localization (CC). The antiviral phenotypes are **downstream, context-dependent consequences** of this deacetylase activity, not a distinct "defense response to virus" function.
- **Isoform caution:** Any HBV-restriction statement (PMID 32493816) is **isoform-5-specific** and should not be propagated to the canonical Q8IXJ6 entry.

---

## Mechanistic Scope

The **immediate molecular function** being modulated in every study is SIRT2's **NAD⁺-dependent lysine deacetylase activity** (substrates include α-tubulin, G3BP1, CDK9, G6PD, p53, β-catenin pathway components). Virus outcomes are **downstream** of this enzyme activity:

- Pro-viral routes: SIRT2 deacetylates **G3BP1** to disassemble the cGAS-G3BP1 condensate and dampen STING/IFN (HSV-1, COVID); supports **AKT/GSK-3β/β-catenin** and **p53**-dependent enhancer activity for HBV; is co-opted by dengue and HIV-1.
- Antiviral routes: SIRT2 deacetylates **CDK9** to promote STAT1-Ser727/ISG transcription; deacetylates **G6PD** to sustain NADPH/GSH redox that limits influenza.

Thus "defense response to virus" is at best a **pleiotropic, context-specific downstream phenotype**, not a primary gene-product function.

---

## Conflicts and Alternatives

- **Genuine biological heterogeneity**, not artifact: same enzyme, opposite outcomes depending on which acetyl-substrate/pathway dominates in a given virus/cell system.
- **Perturbation-type asymmetry:** antiviral effects rely on **SIRT2 activation** or **signaling surrogates**; pro-viral effects are shown by **inhibition + genetic knockdown with on-target rescue** (dengue) and **in vivo** inhibition (HIV-1) — methodologically stronger for settling the sign.
- **Isoform confounding:** isoform 1 (pro-HBV) vs isoform 5 (anti-HBV) from the same locus.
- **Paralog caution:** many "sirtuin" antiviral claims involve **SIRT1** or pan-sirtuin tools (e.g., tenovin-1 is SIRT1/2; resveratrol/SRT compounds activate SIRT1). Curators must avoid SIRT1→SIRT2 carry-over.
- **Phenotype vs restriction:** SARS-CoV-2 protection (PMID 40220296) is **reduced immunopathology/disease severity**, not reduced viral replication — a different GO concept from GO:0051607.

---

## Knowledge Gaps

1. **Clean genetic loss-of-function on infectious titre.** Most decisive HBV/HIV data use inhibitors; only dengue pairs inhibitor with siRNA. *Checked:* no CRISPR-KO study reporting infectious titre increase upon SIRT2 loss. *Resolve:* isogenic SIRT2-KO vs WT, plaque/TCID50 across virus panel.
2. **Catalytic dependence.** *Checked:* inhibitor data imply catalytic requirement but few catalytic-dead (H187Y) rescues. *Resolve:* WT vs catalytic-dead re-expression in KO.
3. **Isoform-resolved effects.** *Resolve:* isoform-specific knockdown/expression with titre readout.
4. **Inhibitor off-target / SIRT1 contribution.** *Resolve:* SIRT2-selective genetic tools alongside chemistry.
5. **Whether any virus is truly restricted by endogenous SIRT2 (LoF ↑ titre).** *Checked:* not found for influenza (only activation GoF). *Resolve:* SIRT2 depletion + IAV plaque assay.

---

## Discriminating Tests

- **Isogenic SIRT2-KO (CRISPR) vs WT**, infectious-progeny titre (plaque/TCID50), across DENV, HIV-1, HBV, HSV-1, IAV — the single most decisive experiment for the sign.
- **Catalytic-dead rescue (H187Y)** to tie any effect to deacetylase activity.
- **SIRT2-selective inhibitor vs pan-sirtuin tool** side-by-side to exclude SIRT1.
- **Isoform-specific reconstitution** (isoform 1 vs 5) in KO cells.
- **G3BP1/cGAS-STING reporter** ± SIRT2 to confirm the immunosuppressive (pro-viral) axis quantitatively.

---

## Curation Leads (require curator verification)

- **Action:** Reject/withhold unqualified GO:0051607 on Q8IXJ6 (**over-annotation**). If a viral role is captured, make it **virus-specific and directionally correct** (predominantly pro-viral / negative regulation of innate antiviral response).
- **Candidate references + snippets to verify:**
  - PMID:34147476 — *"the release of progeny viruses was inhibited by tenovin-1 treatment"* and *"The antiviral effect of tenovin-1 was abrogated with SIRT agonist or SIRT2 knockdown treatment, which indicated the effect of tenovin-1 was on-target"* (decisive, pro-viral).
  - PMID:41883165 — *"Sirtinol, a Sirt2 inhibitor, significantly reduced HIV-1 growth in M0, M1, and M2-MΦs by >1log10 over 7 days"* (pro-viral, in vivo).
  - PMID:35663860 — *"ectopic SIRT2 overexpression markedly increased total HBV RNAs, 3.5-kb RNA and HBV core DNA"* (pro-viral).
  - PMID:37870259 — SIRT2 suppresses cGAS-STING; *"SIRT2 deficiency markedly elevated the expression levels of type I interferon"* (pro-viral/immunosuppressive).
  - Contrary (to weigh, not to base GO:0051607 on): PMID:35071051 (IAV, activation), PMID:30487288 (ISG signaling), PMID:32493816 (isoform 5).
- **Candidate replacement/qualified terms:** positive regulation of viral genome replication (GO:0045070); negative regulation of type I interferon production (GO:0032480) / negative regulation of innate immune response — each paper- and virus-scoped. Retain core MF (protein/tubulin deacetylase) and CC (cytoplasm/microtubule).
- **Suggested curator questions:** Is the proposed GO:0051607 from text-mining/paralog inference? Does any cited paper show LoF *increasing* infectious titre? Are isoform and SIRT1 confounds controlled?

---

## Limitations

- Assessment is literature- and database-driven (PubMed + QuickGO); no wet-lab replication.
- Several HBV/HIV readouts are surrogates (nucleic acid, growth) rather than plaque titre.
- Literature coverage, while broad (HBV, HIV-1, dengue, HSV-1, IAV, SARS-CoV-2), is not exhaustive; additional virus-specific reports may exist.

**Direction verdict:** **Virus-specific, dependency-dominant.** Decisive infectious-progeny evidence (dengue PMID 34147476; HIV-1 PMID 41883165) and the HBV/HSV-1 bodies of work place SIRT2 as a **host dependency / pro-viral factor**, contradicting an unqualified "defense response to virus" assignment. Restriction-like observations are real but confined to specific contexts (influenza via activation; IFN/ISG signaling; a minor HBV isoform) and do not justify GO:0051607 for canonical human SIRT2.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)