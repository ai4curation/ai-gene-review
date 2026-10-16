---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T19:58:29.385392'
end_time: '2026-09-20T20:15:12.548908'
duration_seconds: 1003.16
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: rasC
  gene_symbol: rasC
  uniprot_accession: P32253
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0044351
  hypothesis_text: Dictyostelium discoideum RasC participates in macropinocytosis
    (GO:0044351). Distinguish positive and negative regulatory contributions, direct
    machinery roles, compensatory Ras paralogs, and secondary growth effects. An increase
    in fluid uptake after deletion does not by itself establish lack of a role.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DICDI/rasC/rasC-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Dictyostelium discoideum RasC participates in\
    \ macropinocytosis (GO:0044351). Distinguish positive\n  and negative regulatory\
    \ contributions, direct machinery roles, compensatory Ras paralogs, and secondary\n\
    \  growth effects. An increase in fluid uptake after deletion does not by itself\
    \ establish lack of a role.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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
- **Gene directory:** rasC
- **Gene symbol:** rasC
- **UniProt accession:** P32253

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0044351
- **Source file:** genes/DICDI/rasC/rasC-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Dictyostelium discoideum RasC participates in macropinocytosis (GO:0044351). Distinguish positive and negative regulatory contributions, direct machinery roles, compensatory Ras paralogs, and secondary growth effects. An increase in fluid uptake after deletion does not by itself establish lack of a role.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Dictyostelium discoideum RasC participates in macropinocytosis (GO:0044351). Distinguish positive
  and negative regulatory contributions, direct machinery roles, compensatory Ras paralogs, and secondary
  growth effects. An increase in fluid uptake after deletion does not by itself establish lack of a role.
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

# RasC and Macropinocytosis (GO:0044351) in *Dictyostelium discoideum* — Focused Curation Report

**Gene:** rasC (DICDI) · **UniProt:** P32253 · **Hypothesis slug:** function-hypothesis-go-0044351
**Focus type:** function_assignment
**Seed hypothesis:** *Dictyostelium discoideum RasC participates in macropinocytosis (GO:0044351). Distinguish positive/negative regulatory contributions, direct machinery roles, compensatory Ras paralogs, and secondary growth effects. An increase in fluid uptake after deletion does not by itself establish lack of a role.*

---

## Executive Judgment

**Verdict: Weakly supported / over-annotated for a direct role.** There is **no primary experimental evidence that RasC directly participates in macropinocytosis.** Across the entire primary macropinocytosis literature in *Dictyostelium*, the Ras proteins repeatedly and specifically implicated are **RasG, RasS, and RasB** — never RasC. RasC's experimentally validated function is a distinct axis: RasGEFA(Aimless)→RasC→TORC2→PKB, driving cAMP relay (adenylyl cyclase activation) and chemotaxis. Direct paralog-substitution data show RasC **cannot** replace RasG in growth in suspension, a macropinocytosis-dependent process.

The current GO:0044351 annotation on P32253 carries the evidence code **IBA** (Inferred from Biological Ancestor, GO_Central) — a phylogenetic projection, not experimental support. Given that RasC is ~66% identical to RasG (the validated macropinocytosis regulator) and sits in the same catalytic Ras clade, the annotation is best explained as **clade-level paralog carry-over**.

**Most important caveat (honoring the seed):** Absence of a published rasC⁻ macropinocytosis assay means a *subtle or negative-regulatory* contribution cannot be formally excluded. The seed's warning — that increased fluid uptake after deletion would not by itself disprove a role — is methodologically valid, but here there is no such deletion-uptake dataset in evidence either way; the case against a *direct machinery* role rests on positive identification of other paralogs plus a direct negative substitution result. This warrants **not** asserting a direct RasC macropinocytosis function while flagging the IBA term as a candidate for removal/generalization pending curator review.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| 30967009 (Williams, Paschke, Kay 2019) | Review of genetics + gain/loss-of-function | Competing / refutes direct RasC role | Which Ras drive macropinocytosis | "RasG and RasS are the key Ras proteins involved"; GefF implicated GEF | *D. discoideum*, growing cells | High; review-level synthesis of primary data, RasC not mentioned |
| 23843627 (Hoeller et al. 2013) | Direct assay: Ras–PI3K binding + single mutants | Competing / refutes | Which Ras act via PI3K in macropinocytosis | RasG and RasS bind PI3K1/2 & PI3K4; single rasG or rasS mutants have severe macropinocytosis defects | *D. discoideum*, vegetative | High; direct biochemistry + phenotype; does not test rasC |
| 27821733 (Junemann et al. 2016) | Direct assay: effector regulation | Competing / refutes | Upstream Ras of macropinocytosis formin ForG | ForG directly regulated by RasB and RasG | *D. discoideum*, macroendocytosis | High; direct; RasC not implicated |
| 38263885 (Putar et al. 2024) | Mutant + localization | Competing / refutes | Major macropinocytosis Ras | "RasG is a major regulator of macropinocytosis"; IqgC loading depends on RasG | *D. discoideum* | High |
| 20833893 (Bolourani et al. 2010) | Mutant paralog-substitution | Refutes (negative) | Can RasC substitute for RasG in growth in suspension (macropinocytic feeding)? | RasD fully substitutes; **RasC is without effect** | *D. discoideum* vegetative | High; direct negative evidence relevant to macropinocytosis-dependent growth |
| 17380187 (Kae et al. 2007) | Direct GEF specificity (in vitro + in vivo) | Qualifies (assigns RasC elsewhere) | RasC pathway specificity | RasGEFA activates RasC for adenylyl cyclase activation; RasG for chemotaxis | *D. discoideum* development | High; defines RasC's true niche |
| 20493808 / 20660630 / 27172998 (Charest, Cai, Khanna) | Direct assay / interaction | Qualifies | RasC effector | RasC is the upstream activator of TORC2→PKB for chemotaxis/cAMP relay | *D. discoideum* | High; RasC = TORC2 axis, not macropinocytosis |
| 25815683 (Bloomfield et al. 2015) | Forward genetics / mutant | Context | What limits fluid uptake | NF1 RasGAP loss increases fluid uptake via greater Ras/PI3K activity | *D. discoideum* axenic strains | High; shows Ras-tone control of uptake but does not implicate RasC specifically |
| UniProt P32253 (dictyBase/GO_Central) | Database annotation | Qualifies | Current annotation basis | GO:0044351 = **IBA**; all experimental codes (IDA/IMP/IGI) are TORC2/cAMP/chemotaxis | Annotation record | High; documents phylogenetic, non-experimental basis |
| 24742374 (Chattwood et al. 2014) | Mutant / growth context | Qualifies (supports no essential RasC role) | Does feeding require RasC? | rasG⁻C⁻ double-null cells are routinely grown in axenic medium (which depends on macropinocytic feeding), i.e. bulk fluid uptake persists without RasC | *D. discoideum* | Medium; incidental to the study's chemotaxis focus, not a quantitative uptake assay |
| This report (computed) | Computational (sequence) | Structural/evolutionary | Paralog relatedness | RasC↔RasG 65.6%, ↔RasD 64.6%, ↔RasB 58.4%, ↔RasS 53.1% identity (global NW) | In-silico | Medium; simple global alignment, supports paralog-projection interpretation |

---

## GO Curation Implications

**Lead (requires curator verification):**

- **Term:** GO:0044351 macropinocytosis (BP), currently on P32253 via **IBA**.
- **Recommended action:** **Do not retain as an experimentally-styled assertion of RasC function.** Treat as **non-core / candidate for removal or generalization**. The experimental record supports RasG/RasS/RasB for this process, not RasC.
  - Option A (preferred): **Remove** the IBA macropinocytosis annotation from RasC, or down-rank it, noting paralog carry-over from RasG.
  - Option B (conservative): **Retain but flag** as phylogenetic-only (IBA) with an explicit note that no RasC-specific experimental evidence exists; do not promote to an experimental code.
- **Terms that ARE experimentally supported and should be emphasized as core:** GO:1904841 TORC2 complex binding (IDA), GO:1904515 positive regulation of TORC2 signaling (IDA), GO:0010856 adenylate cyclase activator activity (IGI), GO:0030250 guanylate cyclase activator activity (IMP), GO:0043327 chemotaxis to cAMP (IMP), GO:0007188 adenylate cyclase-modulating GPCR signaling (IMP). These represent RasC's primary function.

"Protein binding" is not used as a recommendation; the informative core MF/BP terms above are supported.

### GO Decision Table (lead — requires curator verification)

| GO ID | Term (aspect) | Current code on P32253 | Evidence for RasC specifically | Recommended curation action |
|---|---|---|---|---|
| GO:0044351 | macropinocytosis (BP) | IBA (phylogenetic) | None experimental; paralog carry-over from RasG | **Remove or flag as phylogenetic-only / non-core**; do not promote to experimental code |
| GO:1904841 | TORC2 complex binding (MF) | IDA | Direct (RasC–TOR/TORC2 binding) | Retain — core |
| GO:1904515 | positive regulation of TORC2 signaling (BP) | IDA | Direct | Retain — core |
| GO:0010856 | adenylate cyclase activator activity (MF) | IGI | Genetic, RasC-specific | Retain — core |
| GO:0030250 | guanylate cyclase activator activity (MF) | IMP | Mutant phenotype | Retain |
| GO:0043327 | chemotaxis to cAMP (BP) | IMP | Mutant phenotype | Retain — core |
| GO:0007188 | adenylate cyclase-modulating GPCR signaling (BP) | IMP | Mutant phenotype | Retain — core |
| GO:0031152 | aggregation involved in sorocarp development (BP) | IMP | Mutant phenotype | Retain |

---

## Mechanistic Scope

- **Immediate molecular function of RasC:** a GTP-binding/GTPase small G-protein that, when activated by its cognate GEF **RasGEFA (Aimless)**, binds and activates **TORC2**, driving PKB/PKBR1 phosphorylation and adenylyl cyclase A activation (cAMP relay) and chemotaxis to cAMP.
- **Macropinocytosis machinery (separate module):** organized around a plasma-membrane patch of PIP3 + active **RasG/RasS/RasB** and Rac, recruiting SCAR/WAVE→Arp2/3 and the formin ForG; regulated by GEFs (GefF, RasGEFX) and GAPs (NF1, RGBARG, IqgC, Leep2). RasC is not a documented member of this module.
- **Downstream/secondary effects to keep separate from a direct role:** any effect of rasC deletion on growth or fluid uptake would be a *secondary* consequence (e.g., altered global Ras tone, compensatory RasD/RasG expression), not evidence of RasC acting in the macropinocytic cup.

---

## Conflicts and Alternatives

1. **Paralog confusion / clade projection (most likely):** RasC ~66% identical to RasG. IBA rules project ancestral function across the clade, sweeping RasC into "macropinocytosis" without species/paralog-specific data.
2. **Shared reporter ambiguity:** Excitable-network and cup-imaging studies often use RBD (Ras-binding-domain) biosensors that detect active Ras collectively and cannot distinguish RasC from RasG/RasD; such images should not be read as RasC-specific localization to macropinocytic cups.
3. **Compensation masking:** Because RasG (and RasD when de-repressed) can cover growth/cytokinesis, a rasC single deletion could appear neutral or even show increased uptake through compensatory paralog activity — the seed's caveat. This is an argument for caution, not for asserting a direct role.
4. **Negative substitution result:** Bolourani 2010 is the cleanest conflict with the hypothesis — RasC explicitly fails to substitute for RasG in growth in suspension (macropinocytic feeding), whereas RasD succeeds.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | Resolving evidence |
|---|---|---|---|
| No published rasC⁻ (or rasC-GTP-locked) macropinocytosis / fluid-phase uptake assay | Multiple PubMed query variants (RasC + macropinocytosis/pinocytosis/endocytosis/fluid-phase/growth/axenic) returned no direct RasC uptake assay; no study reports RasC-GTP binding the macropinocytosis effectors PI3K1/2/4 or ForG | Cannot formally exclude a subtle positive or negative-regulatory RasC contribution; also means the seed's "increased fluid uptake after deletion" scenario has no supporting dataset in evidence | TRITC-dextran fluid-uptake time course in rasC⁻, rasC⁻rasG⁻, and RasC(Q62L) vs WT |
| Whether RasC localizes to macropinocytic cups | UniProt CC terms list plasma membrane/leading edge/vesicle but not cup-specific; imaging uses pan-Ras RBD probes | Localization to cups would be needed for a direct machinery role | RasC-specific (not RBD) live reporter co-imaged with PIP3/PHcrac and SCAR/WAVE |
| Whether RasC-GTP binds the macropinocytosis PI3Ks (PI3K1/2, PI3K4) | Hoeller 2013 tested RasG/RasS binding, not RasC | Direct effector binding would upgrade from IBA | In vitro Ras–PI3K RBD pulldowns including RasC |
| Basis of the IBA call | Confirmed evidence code = IBA on P32253 | Determines whether curator should trust the annotation | Inspect the GO_Central PAINT tree / ancestral node for the projection |

---

## Discriminating Tests

1. **Quantitative fluid-phase uptake (TRITC-dextran/FITC-dextran) and macropinosome sizing** in WT vs rasC⁻ vs rasG⁻ vs rasC⁻rasG⁻, plus constitutively active RasC(Q62L). A direct positive role predicts reduced uptake in rasC⁻ and/or increased uptake with RasC(Q62L); a purely compensatory/secondary effect predicts little change (or increase) in rasC⁻ that is explained by paralog upregulation.
2. **RasC-specific live-cell localization** (not RBD) relative to PIP3 and SCAR/WAVE cup markers.
3. **Direct effector-binding assays** of RasC-GTP with PI3K1/2, PI3K4, and ForG, benchmarked against RasG/RasS/RasB.
4. **Compensation controls:** measure RasG/RasD/RasS activation and protein levels in rasC⁻ to interpret any uptake phenotype.
5. **Inspect the GO_Central PAINT annotation tree** to see whether the macropinocytosis node was experimentally anchored on RasG and projected to RasC.

---

## Curation Leads (require curator verification)

- **Candidate action change:** Flag/remove or mark-as-phylogenetic the RasC → GO:0044351 (macropinocytosis) IBA annotation; do not treat RasC macropinocytosis as core function.
- **Candidate references to cite in the review:**
  - PMID **30967009** — snippet to verify: *"genetic analysis suggests that RasG and RasS are the key Ras proteins involved."*
  - PMID **23843627** — *"RasG and RasS interact most strongly with PI3K1/2 and PI3K4, and single mutants of either Ras have severe macropinocytosis defects."*
  - PMID **27821733** — *"ForG is directly regulated in large-scale endocytosis by RasB and RasG."*
  - PMID **38263885** — *"RasG is a major regulator of macropinocytosis."*
  - PMID **20833893** — *"RasD is capable of totally substituting for RasG for cytokinesis and growth in suspension, whereas RasC is without effect."*
  - PMID **17380187** — *"RasG regulates chemotaxis and RasC is responsible for adenylyl cyclase activation."*
- **Suggested curator questions:** (a) Is the GO:0044351 IBA on RasC anchored on an experimentally-annotated RasG node? (b) Is there any unpublished dictyBase phenotype linking rasC⁻ to fluid uptake? (c) Should RasC's TORC2/cAMP annotations be emphasized as the core function set?
- **Suggested experiments:** the discriminating tests above (fluid-uptake panel, RasC-specific imaging, RasC–PI3K binding).

---

## Provenance / Artifacts

- Computed Ras paralog global %identity matrix (Needleman-Wunsch): RasC↔RasG 65.6, ↔RasD 64.6, ↔RasB 58.4, ↔RasS 53.1; RasG↔RasD 82.5 (executed in this run).
- UniProt P32253 GO cross-reference dump confirming GO:0044351 = **IBA** and experimental codes limited to TORC2/cAMP/chemotaxis (executed in this run).
- Recorded knowledge-state findings #1–#3.

*Computational results reported conservatively; simple global alignment used, no structural modeling performed. No fabricated assay results.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)