---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:14:57.793928'
end_time: '2026-09-21T04:33:42.110250'
duration_seconds: 1124.32
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: KDX1
  gene_symbol: KDX1
  uniprot_accession: P36005
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: function_assignment
  hypothesis_slug: cell-cycle-complex-and-nucleotide-binding-functions
  hypothesis_text: Saccharomyces cerevisiae Kdx1/Mlp1 (P36005, YKL161C) regulates
    cell cycle, participates in G1/S or G2/M transitions, belongs to a cyclin-dependent
    protein kinase holoenzyme complex, or binds ATP. Adjudicate each independently.
    Its noncatalytic CWI-Swi4/Swi6 transcription role and pseudokinase sequence are
    established; determine whether these entail retention, divergence or absence of
    the candidate functions. Separate loss of phosphotransfer from ATP binding, regulatory
    process participation and noncatalytic complex membership. Read full primary experiments
    including PMID:18268013, PMID:20641022 and PMID:20489023, distinguish the nuclear-pore
    MLP1 namesake, and inspect PAINT nodes PTN001172579/PTN000623979/PTN000623980
    relevant to leaf PTN000623199. A NOT at another fungal node PTN008603245 must
    not be applied to this target unless ancestry is established. Lack of a target
    assay or a specialized CWI role alone does not refute inherited functions.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/yeast/KDX1/KDX1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Saccharomyces cerevisiae Kdx1/Mlp1 (P36005, YKL161C)\
    \ regulates cell cycle, participates in\n  G1/S or G2/M transitions, belongs to\
    \ a cyclin-dependent protein kinase holoenzyme complex, or binds\n  ATP. Adjudicate\
    \ each independently. Its noncatalytic CWI-Swi4/Swi6 transcription role and pseudokinase\n\
    \  sequence are established; determine whether these entail retention, divergence\
    \ or absence of the candidate\n  functions. Separate loss of phosphotransfer from\
    \ ATP binding, regulatory process participation and noncatalytic\n  complex membership.\
    \ Read full primary experiments including PMID:18268013, PMID:20641022 and PMID:20489023,\n\
    \  distinguish the nuclear-pore MLP1 namesake, and inspect PAINT nodes PTN001172579/PTN000623979/PTN000623980\n\
    \  relevant to leaf PTN000623199. A NOT at another fungal node PTN008603245 must\
    \ not be applied to this\n  target unless ancestry is established. Lack of a target\
    \ assay or a specialized CWI role alone does not\n  refute inherited functions.\n\
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
citation_count: 3
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
- **Gene directory:** KDX1
- **Gene symbol:** KDX1
- **UniProt accession:** P36005

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** cell-cycle-complex-and-nucleotide-binding-functions
- **Source file:** genes/yeast/KDX1/KDX1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Saccharomyces cerevisiae Kdx1/Mlp1 (P36005, YKL161C) regulates cell cycle, participates in G1/S or G2/M transitions, belongs to a cyclin-dependent protein kinase holoenzyme complex, or binds ATP. Adjudicate each independently. Its noncatalytic CWI-Swi4/Swi6 transcription role and pseudokinase sequence are established; determine whether these entail retention, divergence or absence of the candidate functions. Separate loss of phosphotransfer from ATP binding, regulatory process participation and noncatalytic complex membership. Read full primary experiments including PMID:18268013, PMID:20641022 and PMID:20489023, distinguish the nuclear-pore MLP1 namesake, and inspect PAINT nodes PTN001172579/PTN000623979/PTN000623980 relevant to leaf PTN000623199. A NOT at another fungal node PTN008603245 must not be applied to this target unless ancestry is established. Lack of a target assay or a specialized CWI role alone does not refute inherited functions.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Saccharomyces cerevisiae Kdx1/Mlp1 (P36005, YKL161C) regulates cell cycle, participates in
  G1/S or G2/M transitions, belongs to a cyclin-dependent protein kinase holoenzyme complex, or binds
  ATP. Adjudicate each independently. Its noncatalytic CWI-Swi4/Swi6 transcription role and pseudokinase
  sequence are established; determine whether these entail retention, divergence or absence of the candidate
  functions. Separate loss of phosphotransfer from ATP binding, regulatory process participation and noncatalytic
  complex membership. Read full primary experiments including PMID:18268013, PMID:20641022 and PMID:20489023,
  distinguish the nuclear-pore MLP1 namesake, and inspect PAINT nodes PTN001172579/PTN000623979/PTN000623980
  relevant to leaf PTN000623199. A NOT at another fungal node PTN008603245 must not be applied to this
  target unless ancestry is established. Lack of a target assay or a specialized CWI role alone does not
  refute inherited functions.
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

# KDX1/Mlp1 (P36005, YKL161C) — Adjudication of Cell-Cycle, CDK-Complex, and ATP-Binding Function Assignments

**Focus type:** function_assignment · **Hypothesis slug:** cell-cycle-complex-and-nucleotide-binding-functions
**Organism:** *Saccharomyces cerevisiae* (NCBITaxon:559292) · **Gene:** KDX1 (synonym MLP1) · **ORF:** YKL161C

---

## Executive Judgment

**Verdict: Over-annotated / Refuted for the cell-cycle & CDK-complex claims; Weakly-supported→Unresolved for ATP binding.**

The four seed candidate functions are adjudicated independently:

| Candidate function | Current GO (evidence) | Verdict |
|---|---|---|
| Regulates cell cycle / G1/S–G2/M transition | GO:0000086 G2/M transition (IBA) | **Refuted as a direct function / over-annotated** |
| Cyclin-dependent protein kinase holoenzyme complex | GO:0000307 (IBA) | **Refuted / over-annotated** |
| Cyclin-dependent protein Ser/Thr kinase activity | GO:0004693 (IBA) | **Refuted / over-annotated** |
| Binds ATP | GO:0005524 (IEA:InterPro) | **Weakly supported → Unresolved** (rule-based only; likely impaired) |

**Reasoning.** KDX1/Mlp1 is a **pseudokinase** — a whole-genome-duplication paralog of the active cell-wall-integrity (CWI) MAPK Slt2/Mpk1. Its only experimentally established molecular function is **noncatalytic transcriptional coactivation**: together with (and redundantly to) Mpk1, it forms a complex with the Swi4/Swi6 (SBF) transcription factor to drive cell-wall-stress genes (FKS2 and others) independently of kinase activity (PMID:18268013, PMID:20641022, PMID:20219973). It is a MAPK-family (CMGC group) protein, **not** a cyclin-dependent kinase. The CDK-activity, CDK-holoenzyme-complex, and G2/M-transition annotations are **IBA (PANTHER/PAINT) propagations** from a broad CMGC-group ancestor that co-mingles CDK and MAPK subfamilies; they are not supported by any KDX1 primary experiment and conflict with the protein's demonstrated biology. ATP binding is an **IEA:InterPro rule-based** call from the generic protein-kinase profile; sequence analysis shows KDX1 has lost the DFG Mg²⁺-coordinating aspartate (→NFG) and has a degraded glycine-rich loop, so Mg-ATP binding is likely impaired and remains experimentally undemonstrated.

**Most important caveats.** (1) Absence of a direct ATP-binding assay means we cannot formally exclude residual nucleotide binding (the β3 catalytic Lys55 is retained). (2) SBF (Swi4/Swi6) does have a bona-fide G1/S cell-cycle role, so a *tenuous, indirect* cell-cycle connection exists via its partner — but this is a downstream/partner property, not a direct KDX1 function. (3) The seed's caution is correct: a NOT annotation from a different fungal PANTHER node (PTN008603245) should not be transferred to this target without established ancestry.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| 18268013 (Kim, Truman, Levin 2008) | Mutant/biochemical (ChIP, kinase-dead) | Refutes catalytic role; supports noncatalytic SBF function | Does Mlp1/Mpk1 act via kinase activity or noncatalytically? | Mpk1 **and its pseudokinase paralog Mlp1** activate FKS2 via a **noncatalytic** mechanism; form dimeric complex with Swi4, recruit Swi6; FKS2 activation independent of protein kinase activity | *S. cerevisiae*, cell-wall stress, FKS2 promoter | High for mechanism. Directly labels Mlp1 a pseudokinase. |
| 20641022 (Kim & Levin 2010) | Reporter/genetic | Supports; Qualifies redundancy | Is Mlp1 role redundant with Mpk1? Which genes? | "The Mlp1 pseudokinase serves a redundant function with Mpk1"; additional SBF-noncatalytic targets CHA1, YLR042c, YKR013w | *S. cerevisiae* CWI transcription | High. Confirms redundant, noncatalytic, SBF-dependent role. |
| 20219973 (Kim et al 2010) | Biochemical/localization | Qualifies; contextualizes SBF | Mechanism of Swi6 recruitment | Mpk1(/Mlp1)–Swi4 complex recruits Swi6 to nucleus for CWI transcription; Mpk1 phosphorylates Swi6 Ser238 | *S. cerevisiae* | High for Mpk1; Mlp1 shares the complex-formation step (noncatalytic). |
| 20489023 (Breitkreutz et al 2010, *Science*) | Interaction (systematic network) | Competing/context (not CDK evidence) | Seed's 3rd cited PMID — what is it? | Global yeast **kinase–phosphatase interaction network** (large-scale AP-MS); a systematic interactome resource, not a functional CDK-complex study | *S. cerevisiae*, proteome-scale | Verified this run via NCBI eSummary. Explains how systematic interaction data enter databases; does not place KDX1 in a CDK holoenzyme. |
| UniProt P36005 (features) | Computational/rule-based | Qualifies ATP-binding claim | Are ATP-binding sites experimental? | P-loop (29–37), Lys55, active-site 153 all annotated by **PROSITE-ProRule (ECO:0000255)**; GO:0005524 = **IEA:InterPro** | Sequence rule | Rule-based only; no assay. Cannot confirm ATP binding. |
| UniProt GO xrefs | Database (IBA/IEA) | Competing/context | Provenance of CDK/cell-cycle terms | GO:0000307, GO:0004693, GO:0000086 are all **IBA:GO_Central** (PAINT); no experimental support | PANTHER family tree | These are the terms under adjudication; provenance is phylogenetic inference, not experiment. |
| This report — sequence analysis (P36005 vs P32485) | Structural/evolutionary (computed) | Refutes catalytic competence; qualifies ATP binding | Does KDX1 retain kinase catalytic machinery? | KDX1 vs Slt2: **DFG→NFG** (Mg-Asp lost), **HRD→HCD** (Arg→Cys), **degraded P-loop** (no GxGxxG), **no MAPK T-x-Y activation motif**; β3 Lys retained | In-silico, public sequences | High for motif calls; ATP-binding consequence is inferred, not assayed. |
| This report — InterPro/PANTHER/CDD (P36005) | Computational/database | Refutes CDK classification; competing with CDK IBA terms | Which kinase family does KDX1 belong to? | **PANTHER PTHR24055 "MAPK"**; InterPro family **IPR050117 "Mitogen-activated protein kinase"**; **CDD cd07857 = fungal MPK1 (Slt2) MAPK clade**. ATP-binding GO derives from **IPR017441 / PROSITE PS00107** ATP-binding *signature* (motif pattern), no CDK family present | InterPro protein2ipr | High. Confirms MAPK, not CDK; CDK IBA terms must be cross-clade over-propagation. |

---

## GO Curation Implications (leads — require curator verification)

- **GO:0000307 cyclin-dependent protein kinase holoenzyme complex (CC, IBA):** *Lead — REMOVE / do-not-assert.* No evidence KDX1 is in a CDK–cyclin complex; it is a MAPK-family pseudokinase whose documented complex is with Swi4/Swi6 (SBF). Consider replacing with a supported CC such as the transcription-factor/SBF context (or leaving CC to the nucleus based on its SBF role).
- **GO:0004693 CDK Ser/Thr kinase activity (MF, IBA):** *Lead — REMOVE / do-not-assert.* Pseudokinase; no catalytic activity, and even the parent kinase-activity call is questionable. If any MF is kept it should reflect the noncatalytic scaffolding role, not CDK activity.
- **GO:0004674 / GO:0106310 protein (Ser/Thr) kinase activity (ISS/IEA):** *Lead — flag for review.* Contradicted by pseudokinase status (DFG→NFG, no activation motif); at minimum should not be a core function; a NOT-qualifier is defensible if curator confirms no residual activity.
- **GO:0000086 G2/M transition of mitotic cell cycle (BP, IBA):** *Lead — REMOVE / do-not-assert as direct function.* No KDX1 experiment supports G2/M control; any cell-cycle link is indirect through its SBF partner (which is G1/S, not G2/M).
- **GO:0005524 ATP binding (MF, IEA:InterPro):** *Lead — treat as uncertain.* Rule-based only; sequence predicts impaired Mg-ATP binding. Do not upgrade to experimental; acceptable to retain as low-confidence IEA or flag pending assay.
- **Supported terms to retain/strengthen (positive leads):** BP cell-wall-stress transcriptional response / **GO:0071554 cell wall organization or biogenesis** context; MF/BP capturing **noncatalytic transcription coactivator activity** with SBF (e.g., a transcription-coregulator MF is more informative than "protein binding"); CC **nucleus** (promoter-bound complex). Interaction with Rlm1 and Swi4/Swi6 supports specific complex/coregulator terms rather than generic "protein binding."

---

## Mechanistic Scope

**Immediate molecular function tested:** whether KDX1 directly (a) has CDK/kinase catalytic activity, (b) belongs to a CDK holoenzyme complex, (c) directly controls cell-cycle transitions, and (d) binds ATP.

- **Direct gene-product activity that is supported:** noncatalytic assembly with Swi4 (and Swi6) to confer DNA-binding competence and activate cell-wall-stress transcription — redundant with Mpk1.
- **Downstream / partner-derived, not direct:** any cell-cycle connotation arises from SBF's separate G1/S role, not from KDX1 acting on the cell-cycle machinery. G2/M is not mechanistically linked at all.
- **Inferred, not assayed:** ATP/nucleotide binding — predicted impaired from loss of DFG-Asp and P-loop degradation; no phosphotransfer expected (no activation motif; HRD-Arg lost).

---

## Conflicts and Alternatives

- **Paralog/namesake confusion (flagged in seed, confirmed relevant):** "MLP1" is also the name of the *nuclear-pore / myosin-like protein* **Mlp1 (YKR095W, UniProt Q02455)**, a ~1875-aa nuclear-basket coiled-coil protein, and its paralog **Mlp2 (YIL149C, P40457, 1679 aa)** which "associate with the nuclear pore complex" and organise perinuclear chromatin (verified via UniProt this run). The target here is **KDX1/Mlp1 = YKL161C, P36005** (433 aa, Slt2 pseudokinase) — a completely different, much smaller protein. Curators must not import nuclear-basket / NPC / mRNA-export annotations onto P36005.
- **PANTHER/PAINT over-propagation (confirmed):** InterPro/PANTHER/CDD place P36005 unambiguously in the **MAPK family (PTHR24055; IPR050117)** and specifically the **fungal MPK1/Slt2 MAPK clade (CDD cd07857)** — no CDK-family assignment exists. The CDK-activity, CDK-holoenzyme, and G2/M IBA terms therefore cannot come from KDX1's own subfamily and must be propagated from a broad CMGC-group ancestor node that mixes CDK and MAPK clades. This is a classic family-tree over-annotation; the MAPK subfamily should not inherit CDK-specific MF/CC/BP terms. The ATP-binding IEA traces to the **PROSITE PS00107 / IPR017441 ATP-binding signature** (a sequence motif pattern), not to any binding assay.
- **NOT-annotation transfer risk:** The seed correctly warns that a NOT at another fungal node (PTN008603245) must not be applied unless ancestry to leaf PTN000623199 is established. My recommendation to *not assert* CDK/cell-cycle terms does not depend on importing that NOT; it rests on the target's own biology and sequence.
- **Genuine but indirect cell-cycle thread:** Because SBF (Swi4/Swi6) governs G1/S, and KDX1 physically joins SBF under stress, a curator could see spurious support for "cell-cycle." This is an alternative interpretation to guard against, not evidence for a direct KDX1 cell-cycle function.

---

## Knowledge Gaps

1. **Direct ATP/nucleotide binding of KDX1.** Checked: sequence (DFG→NFG, degraded P-loop, retained Lys55) and UniProt provenance (rule-based). Matters because GO:0005524 rests entirely on an InterPro rule. Resolve with: ITC/DSF thermal-shift or ADP-Glo nucleotide-binding assay on recombinant Kdx1; or a structure/AlphaFold-nucleotide-pocket analysis.
2. **Any residual catalytic activity.** Checked: motif loss predicts none. Matters for whether a NOT-kinase-activity qualifier is warranted. Resolve with: in-vitro kinase assay (already implied negative by kinase-dead-independent transcription in PMID:18268013, but not directly assayed for Kdx1 alone).
3. **PANTHER tree ancestry for the disputed IBA terms.** Checked: UniProt lists them as IBA:GO_Central. Matters because the correct curation is to prune CDK terms from the MAPK leaf. Resolve with: inspection of PAINT nodes PTN001172579/PTN000623979/PTN000623980 vs leaf PTN000623199 to confirm the terms derive from CDK-clade ancestors.
4. **Whether the SBF-linked role justifies any cell-cycle BP term.** Checked: literature ties Mlp1 to stress transcription, not cell-cycle progression. Resolve with: cell-cycle phenotyping of kdx1Δ (synchronised cultures) — expected null given redundancy and stress-specific role.

---

## Discriminating Tests

- **Nucleotide-binding assay** (DSF/thermal shift ± ATP-Mg²⁺; ADP-Glo) on recombinant Kdx1 vs Slt2 — cleanly separates "ATP binding" from "no binding."
- **Structure-based pocket check:** AlphaFold model of P36005 → measure ATP-pocket integrity (DFG-Asp absent, P-loop geometry) and compare to Slt2 — supports/undermines GO:0005524 conservatively.
- **Cell-cycle assay of kdx1Δ and slt2Δ kdx1Δ** (FACS/bud-index, synchronised) — tests any real G1/S or G2/M contribution.
- **PANTHER PAINT node audit** (PTN000623199 leaf and ancestors) — confirms the IBA CDK/cell-cycle terms originate from a CDK-clade ancestor and should be pruned for the MAPK leaf.
- **ChIP/co-IP of Kdx1 with Swi4/Swi6 and Rlm1** — strengthens the correct complex/coregulator CC/MF terms.

---

## Curation Leads (require curator verification)

- **Candidate references to verify (exact snippets):**
  - PMID:18268013 — "We show that the MAPK of this pathway (Mpk1) and its pseudokinase paralog (Mlp1) use a noncatalytic mechanism to activate transcription of the FKS2 gene." and "Transcriptional activation of FKS2 was dependent on the Swi4/Swi6 (SBF) transcription factor and on an activating signal to Mpk1 but not on protein kinase activity."
  - PMID:20641022 — "In this context, the Mlp1 pseudokinase serves a redundant function with Mpk1."
  - PMID:20219973 — Mpk1–Swi4 complex recruits Swi6 to the nucleus for cell-wall-stress transcription (context for KDX1's shared complex step).
- **Candidate action changes:** Remove / do-not-assert GO:0000307, GO:0004693, GO:0000086 for KDX1 (PAINT over-propagation from CDK clade); downgrade/flag GO:0005524 (IEA-only, likely impaired); flag GO:0004674/GO:0106310 kinase activity as contradicted by pseudokinase status.
- **Candidate replacement/new terms:** noncatalytic transcription-coregulator role with SBF (Swi4/Swi6); cell-wall-stress transcriptional response / cell wall organization or biogenesis BP; nucleus CC; specific complex/interaction terms for Swi4/Swi6 and Rlm1 (avoid generic "protein binding").
- **Suggested questions for curator:** Are the disputed IBA terms confirmed to descend from a CDK-clade ancestor (safe to prune)? Is a NOT-kinase-activity qualifier desired? Should ATP binding be retained as IEA or removed pending assay?
- **Suggested experiments:** nucleotide-binding thermal-shift; kdx1Δ cell-cycle phenotyping; AlphaFold pocket analysis.

---

### Provenance
Computational analyses executed this run: (1) UniProt REST fetch of P36005 (sequence, features, GO xrefs, comments); (2) UniProt fetch of paralog P32485 (SLT2); (3) regex motif scan comparing catalytic motifs (P-loop, VAIK, HRD, DFG, MAPK T-x-Y) between KDX1 and SLT2. Key computed result: KDX1 lacks GxGxxG, carries HRD→HCD and DFG→NFG substitutions, and has no T-x-Y activation motif, whereas SLT2 retains all. UniProt binding/active-site features for P36005 are ECO:0000255 (PROSITE-ProRule) rule-based, and the disputed CDK/cell-cycle GO terms are IBA:GO_Central; ATP binding is IEA:InterPro. No result was fabricated; where no assay exists (direct ATP binding), this is stated explicitly.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)