---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T06:49:59.341715'
end_time: '2026-11-14T07:04:15.230389'
duration_seconds: 855.89
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: TRPC4
  gene_symbol: TRPC4
  uniprot_accession: Q9UBN4
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: kisspeptin-trpc-subunit-identity
  hypothesis_text: Among the TRPC subunits co-expressed in GnRH neurons (TRPC1, TRPC3,
    TRPC4, TRPC5, TRPC6, TRPC7), TRPC4 is the subunit that carries the kisspeptin-evoked
    cation current, because it alone combines the cSrc-phosphorylated tyrosine and
    the PIP2-interaction determinants that the published gating mechanism requires.
  term_context: '- Single decisive analysis requested: a residue-level comparison
    of the cSrc target tyrosine and the PIP2-interaction determinants across those
    six human TRPC subunits. Do not broaden to fold assignment, disorder or targeting.

    - The kisspeptin-evoked current in GnRH neurons is defined only by TRPC-blocker
    pharmacology; TRPC4-alpha was identified by mRNA, not by subunit-specific functional
    evidence.'
  reference_context: '- PMID:23744639

    - PMID:18434521'
  source_file: genes/human/TRPC4/TRPC4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Among the TRPC subunits co-expressed in GnRH neurons\
    \ (TRPC1, TRPC3, TRPC4, TRPC5, TRPC6, TRPC7),\n  TRPC4 is the subunit that carries\
    \ the kisspeptin-evoked cation current, because it alone combines the\n  cSrc-phosphorylated\
    \ tyrosine and the PIP2-interaction determinants that the published gating mechanism\n\
    \  requires.\nfocus_type: free_text\ncontext:\n- 'Single decisive analysis requested:\
    \ a residue-level comparison of the cSrc target tyrosine and the\n  PIP2-interaction\
    \ determinants across those six human TRPC subunits. Do not broaden to fold assignment,\n\
    \  disorder or targeting.'\n- The kisspeptin-evoked current in GnRH neurons is\
    \ defined only by TRPC-blocker pharmacology; TRPC4-alpha\n  was identified by\
    \ mRNA, not by subunit-specific functional evidence.\nreference_id:\n- PMID:23744639\n\
    - PMID:18434521"
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
citation_count: 8
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: provenance_go_decision_table.md
  path: openscientist_artifacts/provenance_go_decision_table.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
- filename: provenance_trpc_residue_comparison.md
  path: openscientist_artifacts/provenance_trpc_residue_comparison.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist trpc residue comparison
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
- **Gene directory:** TRPC4
- **Gene symbol:** TRPC4
- **UniProt accession:** Q9UBN4

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** kisspeptin-trpc-subunit-identity
- **Source file:** genes/human/TRPC4/TRPC4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Among the TRPC subunits co-expressed in GnRH neurons (TRPC1, TRPC3, TRPC4, TRPC5, TRPC6, TRPC7), TRPC4 is the subunit that carries the kisspeptin-evoked cation current, because it alone combines the cSrc-phosphorylated tyrosine and the PIP2-interaction determinants that the published gating mechanism requires.

## Term and Decision Context

- Single decisive analysis requested: a residue-level comparison of the cSrc target tyrosine and the PIP2-interaction determinants across those six human TRPC subunits. Do not broaden to fold assignment, disorder or targeting.
- The kisspeptin-evoked current in GnRH neurons is defined only by TRPC-blocker pharmacology; TRPC4-alpha was identified by mRNA, not by subunit-specific functional evidence.

## Reference Context

- PMID:23744639
- PMID:18434521

## Source Context YAML

```yaml
hypothesis: Among the TRPC subunits co-expressed in GnRH neurons (TRPC1, TRPC3, TRPC4, TRPC5, TRPC6, TRPC7),
  TRPC4 is the subunit that carries the kisspeptin-evoked cation current, because it alone combines the
  cSrc-phosphorylated tyrosine and the PIP2-interaction determinants that the published gating mechanism
  requires.
focus_type: free_text
context:
- 'Single decisive analysis requested: a residue-level comparison of the cSrc target tyrosine and the
  PIP2-interaction determinants across those six human TRPC subunits. Do not broaden to fold assignment,
  disorder or targeting.'
- The kisspeptin-evoked current in GnRH neurons is defined only by TRPC-blocker pharmacology; TRPC4-alpha
  was identified by mRNA, not by subunit-specific functional evidence.
reference_id:
- PMID:23744639
- PMID:18434521
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

# TRPC4 subunit identity in the kisspeptin-evoked GnRH-neuron current — Hypothesis Review

**Gene:** TRPC4 (human, Q9UBN4) · **Hypothesis slug:** kisspeptin-trpc-subunit-identity
**Focus:** free_text / core-function & function-assignment reasoning
**Seed hypothesis:** Among TRPC1/3/4/5/6/7 co-expressed in GnRH neurons, TRPC4 carries the
kisspeptin-evoked cation current *because it alone combines the cSrc-phosphorylated tyrosine
and the PIP2-interaction determinants* that the published gating mechanism requires.

---

## Executive Judgment

**Verdict: Weakly / partially supported — the specific molecular-determinant rationale is REFUTED.**

The residue-level comparison that the hypothesis requests does not do the work the hypothesis
claims it does:

1. **cSrc tyrosines (TRPC4 Y959/Y972; Odell 2005, PMID:16144838) are TRPC4-specific — but for the
   wrong reason.** They sit in the hypervariable *distal C-tail* (not conserved in TRPC5/1/3/6/7),
   and they were characterised as **trafficking / membrane-insertion** determinants in EGF-stimulated
   COS-7/HEK cells, *not* as gating residues of a kisspeptin current. They are also present in **both
   TRPC4α and TRPC4β**, so they cannot explain the α-specific identification in GnRH neurons.

2. **The PIP2 determinant does not discriminate TRPC4 from TRPC5.** Phosphoinositide regulation is
   the *only common regulatory feature of all TRP channels* (Rohacs 2024, PMID:37871124). The
   PIP2-*depletion-activated* behaviour that the kisspeptin mechanism requires (Zhang 2013,
   PMID:23744639) is shared by **TRPC5** (Trebak 2009, PMID:18665391) and is a property of the
   whole **TRPC1/4/5 subfamily**; the TRPC4-specific part of PIP2 regulation is **isoform-level**
   (α vs β; Otsuguro 2008, PMID:18230622), not paralog-level.

3. **The two determinants are not a single coherent "TRPC4-only gating module."** They live in
   different C-terminal regions and serve different roles (distal-tail trafficking vs α-insert /
   subfamily PIP2 gating).

4. **Pharmacology points to a heteromer, not a TRPC4 homomer.** The native kisspeptin current is
   **not blocked by 100 µM La³⁺** (Zhang 2008, PMID:18434521), whereas homomeric TRPC4/TRPC5 are
   *potentiated* by micromolar La³⁺; native TRPC1/4/5 subunits form PIP2-regulated heteromers
   (Shi 2012, PMID:21968068). This favours a heteromeric TRPC1/4(/5) channel.

**Net:** TRPC4α remains a *plausible contributor* (its mRNA is in GnRH neurons and its PIP2-depletion
pharmacology fits), but it is **not uniquely singled out** by the cSrc+PIP2 determinants. The strong
"alone combines the determinants" claim should not be used as curation-grade evidence. Most important
caveat: subunit identity of the native current was never established functionally (only by blocker
pharmacology + TRPC4α mRNA), so any subunit-exclusive statement is under-determined.

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | PMID:16144838 (Odell 2005) | Direct assay + mutant | Qualifies | Identity of cSrc tyrosine | TRPC4 **Y959/Y972** phosphorylated by Src-family (Fyn); Y959F/Y972F blocks EGF-induced **membrane insertion** and Ca²⁺ influx | hTRPC4 in COS-7/HEK293, EGF stimulation | High for site ID; **trafficking role, not gating**; heterologous, not GnRH |
| 2 | Computed (this run) | Structural/evolutionary | Refutes "alone" basis | Are Y959/Y972 TRPC4-unique and meaningful? | Tyrosines TRPC4-specific but in hypervariable distal tail; absent at aligned position in all 5 paralogs; present in both α and β | UniProt seqs, SW/NW BLOSUM62 | Medium (distal-tail alignment uncertain); specificity ≠ gating relevance |
| 3 | PMID:23744639 (Zhang 2013) | Direct assay (native) | Supports (partial) | Kisspeptin gating needs PIP2 depletion + cSrc | Kisspeptin→TRPC via PLCβ/**PIP2 hydrolysis** + cSrc; **TRPC4α mRNA** detected (scRT-PCR) | Female mouse GnRH neurons | High for mechanism class; **TRPC4α by mRNA only**, not subunit-resolved function |
| 4 | PMID:18434521 (Zhang 2008) | Direct assay (native) | Competing | Subunit identity of current | Kisspeptin NSCC blocked by 2-APB/FFA/SKF96365/Cd²⁺ but **NOT La³⁺ (100 µM)** | Mouse GnRH neurons | High; La³⁺-insensitivity argues **heteromer**, not homomeric TRPC4/5 |
| 5 | PMID:18230622 (Otsuguro 2008) | Direct assay (recomb.) | Qualifies | PIP2 determinant location | **TRPC4α (not β)** inhibited by PIP2; PIP2 binds α C-terminus; PIP2 breakdown required for activation | Recombinant TRPC4α/β | High; determinant is **α-vs-β**, not paralog-exclusive |
| 6 | PMID:18665391 (Trebak 2009) | Direct assay (recomb.) | Refutes "alone" | Is PIP2-depletion-gating TRPC4-unique? | **TRPC5** also activated by PIP2 depletion & inhibited by PIP2 (not TRPC3/7) | Recombinant TRPC5 | High; **TRPC5 behaves like TRPC4α** → no discrimination |
| 7 | PMID:21968068 (Shi 2012) | Direct assay (native) + interaction | Competing | Heteromer alternative | Native **TRPC1/C5** heteromers; PIP2/PIP3/PKC-activated; TRPC1 confers PI activation | Mouse mesenteric VSMC | High for heteromer concept; different tissue |
| 8 | PMID:27994151 (Storch 2017) | Interaction + mutant | Refutes "alone" | NHERF/PDZ determinant specificity | **NHERF–TRPC4/5** interaction (C-terminal …VTTRL) required for DAG gating | Recombinant TRPC4/5 | High; the PDZ/NHERF determinant is **shared TRPC4+TRPC5** |
| 9 | PMID:37871124 (Rohacs 2024) | Review | Refutes "alone" | Is PIP2 interaction discriminating? | Phosphoinositide regulation is the **only common regulatory feature** of TRP channels | Review | Review-level; pan-TRP → PIP2 can't single out TRPC4 |

---

## GO Curation Implications (leads — require curator verification)

- **Do not use the cSrc-tyrosine + PIP2 "combined determinant" argument as evidence for a
  subunit-exclusive GO Molecular Function assignment to TRPC4.** The determinants are either
  trafficking-related (Y959/Y972) or shared across the TRPC1/4/5 subfamily / isoform-specific
  (PIP2), so they do not support a TRPC4-unique gating claim.
- **MF:** Supportable at the level of **GO:0005262 calcium channel activity** /
  **GO:0005216 monoatomic ion channel activity** / **GO:0005272? (sodium)** — i.e.,
  *non-selective cation channel activity* — for TRPC4 generally; this is retained but is **not
  diagnostic of the kisspeptin current specifically**. Avoid "protein binding" as a terminal call.
- **BP:** Any term tying TRPC4 to **regulation of GnRH neuron excitability / response to kisspeptin**
  should carry a **context-specific, non-core qualifier** and acknowledge that the native channel
  is likely **heteromeric** and defined only pharmacologically. Treat as *contributes_to*, not a
  core exclusive function.
- **CC:** Plasma membrane localization is supported; the α-specific PIP2/NHERF C-terminus links
  TRPC4α to the **cortical actin / NHERF** complex (PMID:18230622, PMID:27994151) — a legitimate,
  better-than-"protein binding" interaction lead if a CC/complex term is desired.
- **Action:** Keep TRPC4's generic cation-channel MF; **do not elevate** "carries the kisspeptin
  current" to a core, subunit-exclusive function on determinant grounds. Flag TRPC5 and TRPC1/4/5
  heteromers as competing annotations.

---

## Mechanistic Scope

- **Immediate molecular activity being tested:** gating of a receptor-operated, PIP2-depletion-sensitive,
  non-selective cation (Na⁺/Ca²⁺) current downstream of Gαq/PLCβ.
- **Direct gene-product activity:** TRPC4α can form a PIP2-inhibited, PIP2-depletion-activated cation
  channel (recombinant evidence).
- **Downstream / inferred (not direct determinant evidence):** depolarization and sustained firing of
  GnRH neurons, GnRH secretion, reproductive-axis activation. These are pathway/physiology outcomes,
  not proof that TRPC4 homomers carry the current.
- **Trafficking vs gating confound:** the cSrc-Y959/Y972 evidence is about surface delivery of TRPC4,
  which the hypothesis mis-casts as a gating determinant.

---

## Conflicts and Alternatives

1. **TRPC5 (closest co-expressed paralog):** identical PIP2-depletion gating (PMID:18665391), shares
   the …VTTRL NHERF/PDZ motif (PMID:27994151) → equally qualified on the stated determinants.
2. **Heteromeric TRPC1/4/5 or TRPC1/4:** native heteromers exist and are PIP2-regulated (PMID:21968068);
   the La³⁺-insensitive native current (PMID:18434521) is more consistent with a heteromer than a
   homomer.
3. **Isoform confound:** the PIP2 determinant is α-vs-β (PMID:18230622), while the cSrc tyrosines are
   α=β — the hypothesis conflates two different "specificities."
4. **mRNA ≠ protein/function:** TRPC4α was identified by single-cell RT-PCR (PMID:23744639); other
   subunits are co-expressed, and pharmacology cannot resolve subunit stoichiometry.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | Resolving evidence |
|-----|------------------|----------------|--------------------|
| Does cSrc phosphorylate Y959/Y972 *in GnRH neurons* and is it needed for the *current* (not trafficking)? | Odell 2005 (heterologous, trafficking) | Hypothesis assumes a gating role | Y959F/Y972F knock-in or dominant-negative in GnRH neurons + kisspeptin recording |
| Subunit stoichiometry of the native current (homomer vs TRPC1/4/5 heteromer) | Pharmacology + mRNA only | "TRPC4 carries the current" vs heteromer | Subunit-specific KO/conditional KO in GnRH neurons; concatemers; subunit-specific toxins |
| Does TRPC5 reproduce the kisspeptin current if TRPC4 removed? | Trebak 2009 shows equivalent PIP2 behavior | Determines whether TRPC4 is necessary | TRPC4 cKO GnRH recording ± TRPC5 compensation |
| Is the α-specific PIP2 C-terminal insert the actual determinant used in GnRH neurons? | Otsuguro 2008 (recombinant) | Links α isoform to mechanism | Isoform-specific rescue in GnRH neurons |

---

## Discriminating Tests (most efficient first)

1. **GnRH-neuron-specific conditional KO of TRPC4 vs TRPC5 vs TRPC1** with kisspeptin whole-cell
   recording — directly tests necessity and heteromer composition.
2. **Y959F/Y972F TRPC4 knock-in** in GnRH neurons — separates trafficking from gating.
3. **Subunit-selective pharmacology** (e.g., Pico145/HC-070 for TRPC1/4/5; (−)-englerin A sensitivity)
   on the native kisspeptin current.
4. **Co-IP / proximity ligation** in GnRH neurons for TRPC1/4/5 heteromer detection.
5. **Isoform-resolved expression** (α vs β) at protein level in GnRH neurons.

---

## Curation Leads (require curator verification)

- **Reference to add / verify:** PMID:16144838 — snippet *"two tyrosine residues in the C terminus of
  human TRPC4 (hTRPC4), Tyr-959 and Tyr-972, are phosphorylated"* and *"this translocation and
  association was defective upon mutation of Tyr-959 and Tyr-972"* → supports a **trafficking** role,
  not gating.
- **Reference to add / verify:** PMID:18230622 — *"TRPC4alpha but not TRPC4beta was strongly inhibited
  by intracellularly applied phosphatidylinositol 4,5-bisphosphate (PIP(2))"* → PIP2 determinant is
  isoform-level.
- **Reference to add / verify:** PMID:18665391 — *"Depletion of … PIP2 … activates calcium entry and
  membrane currents in TRPC5-expressing but not in TRPC3- or TRPC7-expressing cells"* → PIP2 gating
  is shared with TRPC5.
- **Reference to add / verify:** PMID:18434521 — kisspeptin current *"not by lanthanum (100 microM)"* →
  heteromer lead.
- **Reference (review orientation):** PMID:37871124 — PIP2 is the only common TRP regulatory feature.
- **Candidate action change:** downgrade any "TRPC4 uniquely carries the kisspeptin current" statement
  from core/exclusive to **context-specific contributor**; add competing-subunit note (TRPC5,
  TRPC1/4/5 heteromer).
- **Candidate GO terms:** retain generic non-selective cation channel MF; add BP
  *regulation of neuronal action potential / GnRH neuron excitability* as **non-core, context-specific**;
  do not add determinant-based exclusivity.
- **Suggested curator questions:** Is there any *functional* subunit-resolved evidence (KO, selective
  blocker) beyond mRNA + blocker pharmacology? Is the α isoform confirmed at protein level?

---

## Limitations of this analysis

- Distal-C-tail alignments are inherently uncertain (low-complexity, variable length across paralogs;
  TRPC1 is 793 aa so its "last-200" window is not positionally homologous to TRPC4's).
- No GnRH-neuron functional data were (re)generated; all functional claims are from published recordings.
- Precise atomistic PIP2-binding residues were not uniquely defined in the literature, so the PIP2
  "determinant" is treated at the region/isoform level rather than as a residue motif.
- Computed provenance: `provenance/trpc_residue_comparison.md` (sequences, methods, residue table).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table](openscientist_artifacts/provenance_go_decision_table.md)
- [OpenScientist trpc residue comparison](openscientist_artifacts/provenance_trpc_residue_comparison.md)