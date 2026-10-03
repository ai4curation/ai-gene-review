---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T17:59:21.616005'
end_time: '2026-09-20T19:28:31.101499'
duration_seconds: 5349.49
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: pdsA
  gene_symbol: pdsA
  uniprot_accession: P12019
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: extracellular-pde-and-camp-pathway-regulation
  hypothesis_text: Dictyostelium discoideum PdsA/DdPDE1 participates in negative regulation
    of adenylate cyclase-activating glucose-activated GPCR signaling (GO:0110034)
    and negative regulation of cAMP/PKA signal transduction (GO:0141162). Adjudicate
    the two claims independently against current GO definitions and experiments. Distinguish
    extracellular cAMP turnover and receptor signaling from the intracellular cAMP
    pool controlled by RegA. Determine whether PdsA itself performs a negative-regulatory
    step in either defined pathway, considering feedback and compartment coupling
    without inferring exclusion solely from secretion or missing target assays.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DICDI/pdsA/pdsA-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Dictyostelium discoideum PdsA/DdPDE1 participates\
    \ in negative regulation of adenylate cyclase-activating\n  glucose-activated\
    \ GPCR signaling (GO:0110034) and negative regulation of cAMP/PKA signal transduction\n\
    \  (GO:0141162). Adjudicate the two claims independently against current GO definitions\
    \ and experiments.\n  Distinguish extracellular cAMP turnover and receptor signaling\
    \ from the intracellular cAMP pool controlled\n  by RegA. Determine whether PdsA\
    \ itself performs a negative-regulatory step in either defined pathway,\n  considering\
    \ feedback and compartment coupling without inferring exclusion solely from secretion\
    \ or missing\n  target assays.\nfocus_type: function_assignment\ncontext: []\n\
    reference_id: []"
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

- **Organism code:** DICDI
- **Taxon:** Dictyostelium discoideum (NCBITaxon:44689)
- **Gene directory:** pdsA
- **Gene symbol:** pdsA
- **UniProt accession:** P12019

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** extracellular-pde-and-camp-pathway-regulation
- **Source file:** genes/DICDI/pdsA/pdsA-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Dictyostelium discoideum PdsA/DdPDE1 participates in negative regulation of adenylate cyclase-activating glucose-activated GPCR signaling (GO:0110034) and negative regulation of cAMP/PKA signal transduction (GO:0141162). Adjudicate the two claims independently against current GO definitions and experiments. Distinguish extracellular cAMP turnover and receptor signaling from the intracellular cAMP pool controlled by RegA. Determine whether PdsA itself performs a negative-regulatory step in either defined pathway, considering feedback and compartment coupling without inferring exclusion solely from secretion or missing target assays.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Dictyostelium discoideum PdsA/DdPDE1 participates in negative regulation of adenylate cyclase-activating
  glucose-activated GPCR signaling (GO:0110034) and negative regulation of cAMP/PKA signal transduction
  (GO:0141162). Adjudicate the two claims independently against current GO definitions and experiments.
  Distinguish extracellular cAMP turnover and receptor signaling from the intracellular cAMP pool controlled
  by RegA. Determine whether PdsA itself performs a negative-regulatory step in either defined pathway,
  considering feedback and compartment coupling without inferring exclusion solely from secretion or missing
  target assays.
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

# PdsA/DdPDE1 (DICDI, UniProt P12019) — Adjudication of two negative-regulation GO claims

**Focus:** function_assignment · **Hypothesis slug:** extracellular-pde-and-camp-pathway-regulation
**Terms adjudicated:** GO:0110034 (negative regulation of adenylate cyclase-activating **glucose-activated** G protein-coupled receptor signaling pathway) and GO:0141162 (negative regulation of cAMP/PKA signal transduction).

---

## Executive Judgment

**Verdict: REFUTED / over-annotated for both terms *as assigned to PdsA*.**

Both GO terms are already present on P12019 **only as IBA (phylogenetic, ECO:0000318) annotations** propagated from fungal cyclic-nucleotide phosphodiesterase orthologs via PANTHER family PTN002001416 (GO:0110034 ← *S. pombe* cgs2/Pde1, PomBase SPCC285.09c; GO:0141162 ← *C. albicans* PDE2, CGD CAL0000177603). Neither is backed by a Dictyostelium experiment.

- **Claim A (GO:0110034):** The GO term specifically denotes a **glucose-activated** GPCR→adenylate-cyclase pathway (the fungal Gpr1/Gpa2→Cyr1→cAMP→PKA glucose-sensing system). *Dictyostelium* has no such pathway; its adenylate-cyclase (ACA)-activating receptor cAR1 is **cAMP-activated, not glucose-activated**. PdsA's genuine negative-regulatory role — degrading the extracellular cAMP ligand of the cAR receptors — is real but is **the wrong biological pathway for this term**. The term is factually inapplicable, independent of PdsA being secreted.
- **Claim B (GO:0141162):** PdsA degrades the **extracellular** cAMP pool. PKA is activated by the **intracellular** cAMP pool, whose direct negative regulator is the cytosolic PDE **RegA** (Q23917). The direct catalytic step in cAMP/PKA signal transduction is RegA's, not PdsA's. PdsA can influence PKA only **indirectly** through cAR-receptor feedback/compartment coupling, which does not justify a direct BP annotation.

**Most important caveat:** This is a *compartment/term-specificity* judgement, not a claim that PdsA is irrelevant to cAMP signaling. PdsA is a bona-fide negative regulator of the *extracellular* cAMP relay/GPCR loop — that role is already captured by experimentally supported terms (GO:0007193 IMP, GO:1900115 IMP). The two seed terms should be removed as ortholog carry-over, not replaced with themselves.

**Decisive primary evidence (added Iteration 2):** Bader, Kortholt & Van Haastert 2007 (PMID:17040207) biochemically partition all seven Dictyostelium PDEs across three cyclic-nucleotide pools and state that **extracellular cAMP is degraded predominantly by DdPDE1 (= PdsA) and its homolog DdPDE7**, whereas **intracellular cAMP (which "mediates development") is degraded by DdPDE2 (= RegA) and DdPDE6**. This is a direct, quantitative pool assignment — not an inference from secretion — that separates PdsA (extracellular) from the RegA-controlled intracellular/PKA-relevant pool.

**Correct-term note:** GO does provide a non-glucose term, **GO:0106072 "negative regulation of adenylate cyclase-activating G protein-coupled receptor signaling pathway"**, and a cAMP-receptor pathway term **GO:0140582 "adenylate cyclase-activating G protein-coupled cAMP receptor signaling pathway"**. These, not the fungal glucose term GO:0110034, are the appropriate vocabulary if a receptor-pathway BP annotation is desired for PdsA's cAR/ACA context. (Note: GO:0043951 "negative regulation of cAMP-mediated signaling" is **obsolete** and unusable.)

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence/limits |
|---|---|---|---|---|---|---|
| PMID:9405107 | Mutant phenotype | Supports mechanism | PdsA controls extracellular cAMP | pdsA-null blocks coordinated chemotactic movement; PDE is **secreted**, controls extracellular cAMP | *D. discoideum* development | High; genetic |
| PMID:23473502 | Imaging/direct | Supports mechanism | PdsA degrades extracellular cAMP | Extracellular PDE degradation sets cAMP near the relay threshold; dual +/− feedback | *D. discoideum* aggregation | High |
| PMID:36688866 | Mutant phenotype | Qualifies | cAMP pool compartmentation | Adenylate cyclases make **secreted cAMP for gene expression** and **intracellular cAMP for PKA activation**; PdsA is the extracellular PDE | Polysphondylium/Dictyostelium | High |
| PMID:30790701 | Mutant phenotype | **Refutes Claim B for PdsA** | Neg. reg. of PKA = RegA | "the intracellular cAMP-specific phosphodiesterase RegA is a negative regulator of…PKA" | *D. discoideum* | High |
| PMID:11390363 | Genetic/direct | **Refutes Claim B for PdsA** | Intracellular cAMP/PKA set by RegA | Intracellular cAMP & PKA activity controlled by synthesis and **RegA** degradation | *D. discoideum* | High |
| PMID:17040207 | Direct assay (enzyme kinetics/pool partition) | **Refutes Claim B; supports correct term** | Which PDE clears which cAMP pool | **DdPDE1 (=PdsA)** clears **extracellular** cAMP; **DdPDE2 (=RegA)** clears **intracellular** cAMP that "mediates development"; basis of IMP GO:0007193 & GO:1900115 | *D. discoideum*, all 7 PDEs | High (quantitative, primary) |
| QuickGO/UniProt P12019 | Database/curation metadata | **Refutes seed terms** | Disputed terms are IBA | GO:0110034 & GO:0141162 are **IBA** (GO_REF:0000033) from fungal Pde1/Pde2 via PANTHER PTN002001416 | cross-species | High |
| QuickGO GO:0110034 annotation set | Computational | Qualifies | Term is fungal glucose-signaling | 34 annotations dominated by fungal cgs2/atf1/cgs1(PKA)/PDE1; Dictyostelium Pds enzymes added only by phylogeny | cross-species | Med-High |

*Provenance artifacts (computed this run): `/tmp/go_decision_table.csv`, `/tmp/evidence_matrix.csv`, `/tmp/GO0110034_composition.png`.*

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current evidence on P12019 | Lead action |
|---|---|---|---|
| GO:0110034 neg reg AC-activating **glucose-activated** GPCR signaling | BP | IBA only (from *S. pombe* cgs2/Pde1) | **Remove / do not assign.** Wrong pathway (glucose-sensing GPCR). Report as inappropriate IBA propagation. |
| GO:0141162 neg reg cAMP/PKA signal transduction | BP | IBA only (from *C. albicans* PDE2) | **Remove from pdsA.** Belongs to **regA** (Q23917), the intracellular cAMP/PKA regulator. |
| GO:1902660 neg reg glucose mediated signaling pathway | BP | IBA | Flag as **non-core**; same fungal-ortholog family; candidate removal. |
| GO:0007193 adenylate cyclase-inhibiting GPCR signaling pathway | BP | **IMP (PMID:17040207)** | **Retain** — experimentally supported *Dictyostelium* role. |
| GO:1900115 extracellular regulation of signal transduction | BP | **IMP (PMID:17040207)** | **Retain** — correctly captures action on the extracellular signal pool (core BP). |
| GO:0004115 3',5'-cyclic-AMP phosphodiesterase activity | MF | IDA (dictyBase); EC 3.1.4.35/3.1.4.53 | **Retain** — primary molecular function. |
| GO:0106072 neg reg adenylate cyclase-activating GPCR signaling (non-glucose) | BP | *not currently on P12019* | **Candidate replacement** for GO:0110034 if a receptor-loop BP is wanted; matches cAR/ACA (GO:0140582) context. Curator-verify against PMID:17040207/9405107. |

Do **not** default to "protein binding": the informative MF (cAMP phosphodiesterase, GO:0004115) and the correct BP terms are already available.

**Directionality nuance (curator-verify):** the currently retained BP term GO:0007193 is *adenylate cyclase-**inhibiting** GPCR signaling*, but the characterized Dictyostelium biology is that cAR1 **activates** adenylate cyclase (ACA) and PdsA negatively regulates that loop by degrading the extracellular cAMP ligand. On directional grounds **GO:0106072** (*negative regulation of adenylate cyclase-**activating** GPCR signaling*) is a more accurate BP than GO:0007193. A curator may wish to consider replacing GO:0007193 with GO:0106072 (context GO:0140582, cAMP-receptor pathway), rather than simply retaining GO:0007193.

---

## Mechanistic Scope

- **Direct molecular activity of PdsA:** hydrolysis of 3',5'-cyclic AMP (preferred) and cGMP to 5'-nucleotides (EC 3.1.4.35 / 3.1.4.53), acting on the **extracellular / cell-surface** cAMP pool (UniProt: "Secreted, extracellular space; Cell surface").
- **Direct cellular role:** clearing secreted cAMP so cAR-mediated relay can oscillate and cells stay responsive during aggregation (PMID:9405107, PMID:23473502). This is genuine **negative regulation of a cAMP-receptor (GPCR) / adenylate-cyclase loop** — the concept behind Claim A but for a *cAMP*-activated, not *glucose*-activated, receptor.
- **What is NOT PdsA's direct step:** setting the intracellular cAMP concentration that binds PKA regulatory subunits. That is done by RegA (intracellular) and adenylate cyclases (synthesis) (PMID:30790701, PMID:11390363, PMID:36688866). Any PdsA→PKA effect is a **downstream / feedback** consequence, not a direct transduction step.

---

## Conflicts and Alternatives

- **Paralog/ortholog carry-over (primary conflict):** both seed terms are IBA from a PANTHER family that pools fungal intracellular glucose-signaling PDEs (*S. pombe* Pde1/cgs2, *C. albicans* PDE2) with *Dictyostelium* secreted PdsA. In fungi those PDEs really do negatively regulate glucose-activated GPCR→cAMP→PKA signaling; the terms are correct **there**, then over-propagated to PdsA whose biology (extracellular, cAMP-chemoattractant) differs.
- **Compartment confusion:** the seed hypothesis explicitly asks to separate the extracellular pool (PdsA) from the RegA-controlled intracellular pool — the evidence confirms these are the correct compartment assignments, and the two seed terms conflate them.
- **Term-label subtlety:** GO:0110034's "glucose-activated" wording could be mistaken for generic "adenylate cyclase-activating GPCR" signaling. Curators should note the qualifier makes it fungal-glucose-specific, so it is not a substitute for the cAMP-receptor role already covered by GO:0007193.

---

## Knowledge Gaps

1. **Does PdsA measurably affect intracellular cAMP/PKA in vivo?** Checked: literature attributes PKA control to RegA; no assay shows PdsA setting intracellular cAMP. Matters because a genuine (if indirect) effect could justify a *regulates*-type annotation with an ISS/indirect qualifier — but current evidence favors indirect only. Resolve with: intracellular cAMP / PKA-reporter measurements in pdsA-null vs WT.
2. **Is there any Dictyostelium glucose-sensing GPCR→adenylate cyclase pathway?** Checked: not described; ACA-activating receptor is cAR1 (cAMP). Matters because GO:0110034 requires it. Resolve with: literature/annotation review confirming absence.
3. **RESOLVED (Iteration 2):** PMID:17040207 abstract read — it explicitly assigns extracellular-cAMP degradation to DdPDE1 (PdsA) and intracellular-cAMP degradation to DdPDE2 (RegA), confirming the compartment split. Remaining minor gap: the paper is enzyme-kinetics/pool-modeling, so the "IMP" evidence label on GO:0007193/GO:1900115 is curator interpretation; full-text confirmation of the receptor-signaling phenotype would further solidify the retained BP terms.

---

## Discriminating Tests

- **pdsA-null vs regA-null, intracellular cAMP + PKA activity time-course:** regA-null elevates intracellular cAMP/PKA (precocious development); pdsA-null should not directly elevate the intracellular pool — cleanly separates Claim B ownership.
- **8Br-cAMP / PKA-agonist rescue:** rescues intracellular-cAMP/PKA deficits (as in acaA-acrA- double mutants, PMID:36688866) but is not expected to be the axis of pdsA phenotypes (which are extracellular-relay/chemotaxis).
- **Ortholog-context check:** confirm PANTHER PTN002001416 groups secreted Dictyostelium PDEs with intracellular fungal PDEs — evidence that the IBA propagation crosses a compartment/function boundary and should be blocked for PdsA.

---

## Curation Leads (require curator verification)

- **Action:** Remove/withhold **GO:0110034** and **GO:0141162** from pdsA (P12019); both are IBA-only ortholog carry-overs crossing a compartment/pathway boundary. Consider flagging **GO:1902660** as non-core.
- **Optional replacement (curator-verify):** if a receptor-loop BP is desired, use the non-glucose **GO:0106072** (negative regulation of adenylate cyclase-activating GPCR signaling pathway), contextualized to the cAMP-receptor pathway **GO:0140582** — not the fungal glucose term GO:0110034. Note GO:0043951 is obsolete.
- **Reassign:** GO:0141162 is appropriate for **regA (Q23917)**, the intracellular cAMP/PKA negative regulator. Primary support: PMID:17040207 — "Intracellular cAMP is degraded by the DdPDE2 [RegA]…" vs "Extracellular cAMP is degraded predominantly by…DdPDE1 [PdsA]".
- **Retain:** GO:0004115 (MF, IDA), GO:0007193 and GO:1900115 (BP, IMP PMID:17040207) — these already capture PdsA's true negative-regulatory, extracellular role.
- **Candidate references / snippets to verify:**
  - PMID:30790701 — "the intracellular cAMP-specific phosphodiesterase RegA is a negative regulator of…PKA".
  - PMID:11390363 — "intracellular cAMP and PKA activity are controlled by…degradation by the cAMP-specific phosphodiesterase RegA".
  - PMID:36688866 — adenylate cyclases produce "secreted cAMP for…gene expression and intracellular cAMP for PKA activation".
  - PMID:9405107 / PMID:23473502 — PdsA is the secreted extracellular-cAMP PDE governing relay.
- **Suggested questions for curator:** Should IBA annotations from PANTHER PTN002001416 be suppressed for the secreted Dictyostelium Pds clade? Is a "regulation of adenylate cyclase-activating (cAMP) GPCR signaling" term (non-glucose) already covered by GO:0007193 for this gene?
- **Suggested experiments:** intracellular cAMP/PKA-reporter assay in pdsA-null vs regA-null to formally exclude any direct PdsA role in the PKA-activating pool.

---

### Limitations
Analysis used public UniProt/QuickGO metadata and PubMed/efetch abstracts; the fungal ortholog primary papers (S. pombe cgs2/Pde1; C. albicans PDE2) were not full-text read. Verdicts on IBA provenance are drawn from curation metadata (evidence code, GO_REF, with-from, PANTHER family PTN002001416) — high confidence — rather than re-derived phylogeny. PMID:17040207 was read at abstract level (Iteration 2) and directly documents the PdsA=extracellular / RegA=intracellular pool split.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)