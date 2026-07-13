---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T05:38:14.751190'
end_time: '2026-07-11T05:59:36.592830'
duration_seconds: 1281.84
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: rat
  gene: Akt1
  gene_symbol: Akt1
  uniprot_accession: P47196
  taxon_id: NCBITaxon:10116
  taxon_label: Rattus norvegicus
  focus_type: computational_prediction
  hypothesis_slug: prediction-kinase-inhibitor-activity
  hypothesis_text: GO-GPT (via BioReason-Pro) predicts protein serine/threonine kinase
    INHIBITOR activity (GO:0030291) for rat Akt1 (P47196). Independently assess whether
    Akt1 -- protein kinase B, an AGC-family serine/threonine protein kinase -- has
    protein-serine/threonine-kinase-INHIBITOR activity (i.e. it binds and inhibits
    another kinase, as a pseudosubstrate/inhibitor protein), or whether its molecular
    function is protein serine/threonine kinase activity itself (with any inhibition
    of downstream kinases such as GSK3 being a consequence of its own kinase activity
    rather than a distinct kinase-inhibitor molecular function), which would make
    the kinase-inhibitor prediction a misassignment. Determine whether the prediction
    is supported or refuted.
  term_context: '- Term: protein serine/threonine kinase inhibitor activity (GO:0030291)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: GO-GPT (via BioReason-Pro) predicts protein serine/threonine\
    \ kinase INHIBITOR activity (GO:0030291)\n  for rat Akt1 (P47196). Independently\
    \ assess whether Akt1 -- protein kinase B, an AGC-family serine/threonine\n  protein\
    \ kinase -- has protein-serine/threonine-kinase-INHIBITOR activity (i.e. it binds\
    \ and inhibits\n  another kinase, as a pseudosubstrate/inhibitor protein), or\
    \ whether its molecular function is protein\n  serine/threonine kinase activity\
    \ itself (with any inhibition of downstream kinases such as GSK3 being\n  a consequence\
    \ of its own kinase activity rather than a distinct kinase-inhibitor molecular\
    \ function),\n  which would make the kinase-inhibitor prediction a misassignment.\
    \ Determine whether the prediction is\n  supported or refuted.\nfocus_type: computational_prediction\n\
    term_id: GO:0030291\nterm_label: protein serine/threonine kinase inhibitor activity\n\
    context: []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: akt1_GO_annotation_trace.csv
  path: openscientist_artifacts/akt1_GO_annotation_trace.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist akt1 GO annotation trace
- filename: akt1_evidence_matrix.csv
  path: openscientist_artifacts/akt1_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist akt1 evidence matrix
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

- **Organism code:** rat
- **Taxon:** Rattus norvegicus (NCBITaxon:10116)
- **Gene directory:** Akt1
- **Gene symbol:** Akt1
- **UniProt accession:** P47196

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-kinase-inhibitor-activity
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

GO-GPT (via BioReason-Pro) predicts protein serine/threonine kinase INHIBITOR activity (GO:0030291) for rat Akt1 (P47196). Independently assess whether Akt1 -- protein kinase B, an AGC-family serine/threonine protein kinase -- has protein-serine/threonine-kinase-INHIBITOR activity (i.e. it binds and inhibits another kinase, as a pseudosubstrate/inhibitor protein), or whether its molecular function is protein serine/threonine kinase activity itself (with any inhibition of downstream kinases such as GSK3 being a consequence of its own kinase activity rather than a distinct kinase-inhibitor molecular function), which would make the kinase-inhibitor prediction a misassignment. Determine whether the prediction is supported or refuted.

## Term and Decision Context

- Term: protein serine/threonine kinase inhibitor activity (GO:0030291)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: GO-GPT (via BioReason-Pro) predicts protein serine/threonine kinase INHIBITOR activity (GO:0030291)
  for rat Akt1 (P47196). Independently assess whether Akt1 -- protein kinase B, an AGC-family serine/threonine
  protein kinase -- has protein-serine/threonine-kinase-INHIBITOR activity (i.e. it binds and inhibits
  another kinase, as a pseudosubstrate/inhibitor protein), or whether its molecular function is protein
  serine/threonine kinase activity itself (with any inhibition of downstream kinases such as GSK3 being
  a consequence of its own kinase activity rather than a distinct kinase-inhibitor molecular function),
  which would make the kinase-inhibitor prediction a misassignment. Determine whether the prediction is
  supported or refuted.
focus_type: computational_prediction
term_id: GO:0030291
term_label: protein serine/threonine kinase inhibitor activity
context: []
reference_id:
- doi:10.64898/2026.03.19.712954
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

# AIGR Gene Hypothesis Deep Research — Final Report

**Gene:** Akt1 (RAC-alpha serine/threonine-protein kinase / Protein kinase B alpha)
**Organism:** *Rattus norvegicus* (NCBITaxon:10116)
**UniProt:** P47196
**Hypothesis under evaluation:** GO-GPT (via BioReason-Pro) predicts **protein serine/threonine kinase inhibitor activity (GO:0030291)** for rat Akt1.
**Focus type:** computational_prediction
**Reference context:** doi:10.64898/2026.03.19.712954

---

## Summary

The computational prediction that rat Akt1 (P47196) possesses **protein serine/threonine kinase inhibitor activity (GO:0030291)** as a molecular function is **REFUTED / OVER-ANNOTATED** and should be rejected as a molecular-function (MF) assignment. Akt1's directly supported, primary molecular function is **catalytic protein serine/threonine kinase activity (GO:0004674; EC 2.7.11.1)** — it is a canonical AGC-family kinase that transfers the γ-phosphate of ATP onto serine/threonine residues of substrate proteins.

The prediction arises from a well-understood mechanism-typing error. Akt1 does indeed *inhibit* glycogen synthase kinase-3 (GSK3), and this is the exact biological observation that produced the original GO:0030291 annotation (QuickGO IPI evidence, PMID:8524413, with-from rat GSK3α/β UniProt P18265/P18266). However, Akt1 inhibits GSK3 by **phosphorylating it at Ser21 (GSK3α) / Ser9 (GSK3β)** — i.e., inhibition is a *downstream catalytic consequence of Akt1's own kinase activity*, not a distinct pseudosubstrate/inhibitor-protein function. The GO:0030291 term is explicitly defined as "**Binds to and stops, prevents or reduces the activity of a protein serine/threonine kinase**," a binding-based (stoichiometric, non-catalytic) inhibitor function exemplified by proteins such as p27^Kip1. Akt1 has no pseudosubstrate/inhibitor domain; its domain architecture is that of an active kinase (PH domain, protein kinase domain, AGC-kinase C-terminal domain).

The most important caveats are: (1) the biological *fact* that Akt1 negatively regulates GSK3 is correct and should be preserved — but as a **biological-process** term (negative regulation of GSK3 / of kinase activity), not as an MF kinase-inhibitor term; and (2) the human ortholog AKT1 (P31749) carries the same GO:0030291 term only by ISS carry-over propagated from the rat annotation, so this is a single, self-propagating mechanism-mistyping rather than independent evidence. The prediction essentially recapitulates a pre-existing questionable database annotation.

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED.**

Akt1's core molecular function is protein serine/threonine kinase *activity*, the opposite of a kinase *inhibitor* function. The GO:0030291 term denotes a stoichiometric binding inhibitor; Akt1 reduces GSK3 activity enzymatically, by phosphorylation. The prediction confuses a downstream biological outcome (GSK3 activity decreases) with a molecular-function mechanism (a bound pseudosubstrate) that Akt1 does not possess. The curator lead is to **remove/reject the GO:0030291 MF term**, retain **GO:0004674** as the core MF, and represent the GSK3 effect via a **biological-process negative-regulation** term.

---

## Key Findings

### Finding 1 — Akt1's core molecular function is catalytic protein serine/threonine kinase activity, not inhibitor activity

Rat Akt1 (P47196) is annotated in UniProt with the recommended name "RAC-alpha serine/threonine-protein kinase" and the enzyme classification **EC 2.7.11.1** (non-specific serine/threonine protein kinase). Its catalytic activity is documented as the canonical kinase reaction: *L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H⁺* (and the threonyl equivalent). This is the reaction of a phosphotransferase — the opposite of an inhibitor's stoichiometric binding.

The domain architecture reinforces this: Akt1 contains a **PH domain** (Pfam PF00169), a **protein kinase domain** (Pfam PF00069 Pkinase; PROSITE PS50011; PS00108 Ser/Thr active-site signature), and an **AGC-kinase C-terminal domain** (Pfam PF00433). This is the textbook architecture of an active AGC kinase. Critically, **there is no pseudosubstrate segment or kinase-inhibitor domain** anywhere in the protein — the structural hallmark that a genuine GO:0030291 kinase-inhibitor protein would require.

The GO record itself confirms catalytic function with strong experimental support: **GO:0004674 (protein serine/threonine kinase activity)** is annotated IDA (inferred from direct assay) by BHF-UCL, and **GO:0004672 (protein kinase activity)** is annotated IDA by RGD. UniProt keywords are "Kinase," "Serine/threonine-protein kinase," and "Transferase." In every primary and database source, Akt1 is a catalyst, not an inhibitor.

### Finding 2 — The GO:0030291 annotation traces to GSK3 inhibition-by-phosphorylation (Cross et al. 1995), i.e. over-annotation of a downstream consequence of kinase activity

Tracing the provenance of the annotation in QuickGO shows that rat Akt1 P47196's **GO:0030291** term carries evidence code **IPI (inferred from physical interaction; ECO:0000353)**, was assigned by **BHF-UCL**, cites **PMID:8524413**, and has a **with/from** field pointing to **UniProtKB:P18265 and P18266** — which are rat **GSK3α and GSK3β**, themselves serine/threonine kinases (EC 2.7.11.26).

PMID:8524413 (Cross, Alessi, Cohen, Andjelkovich & Hemmings, *Nature* 1995, *"Inhibition of glycogen synthase kinase-3 by insulin mediated by protein kinase B"*) states verbatim:

> "GSK3 is inhibited by serine phosphorylation in response to insulin or growth factors"

and

> "Another insulin-stimulated protein kinase inactivates GSK3 under these conditions, and we demonstrate that it is the product of the proto-oncogene protein kinase B"

Read carefully, this paper is the source of the annotation and it *explicitly describes the mechanism*: GSK3 is inhibited **by serine phosphorylation**, and the kinase that carries out that inhibitory phosphorylation is PKB/Akt. The inhibition is therefore an enzymatic, catalytic event — a post-translational modification installed by an active kinase — not the binding of a stoichiometric inhibitor protein. Curating this as an MF "kinase inhibitor activity" term conflates the *biological outcome* (GSK3 activity goes down) with a *molecular-function mechanism* (a bound pseudosubstrate) that does not exist here.

Notably, the human ortholog AKT1 (P31749) carries the identical GO:0030291 term only by **ISS (ECO:0000250, GO_REF:0000024)** propagated from the rat P47196 annotation. There is no independent experimental basis in human; this is database carry-over, exactly the failure mode the research objective flags (paralog/ortholog over-annotation and frequency bias).

### Finding 3 — The GO:0030291 definition denotes a binding-based inhibitor, which is mechanistically incompatible with Akt1's phosphorylation mechanism

The QuickGO ontology definition of **GO:0030291** is, verbatim: *"Binds to and stops, prevents or reduces the activity of a protein serine/threonine kinase."* Its aspect is **molecular_function**. The defining verb is **"binds to and ... reduces"** — the term is reserved for proteins that act as **stoichiometric, non-catalytic inhibitors** (e.g., pseudosubstrates or regulatory inhibitor proteins). Sampling the set of gene products annotated to GO:0030291 returns canonical non-catalytic inhibitors such as **p27^Kip1 (Cdkn1b)**, confirming the term's intended usage.

Akt1 does not fit this definition. It reduces GSK3 activity by **catalyzing an inhibitory phosphorylation** (Ser21 on GSK3α, Ser9 on GSK3β), which creates a primed pseudosubstrate segment that folds back and blocks the GSK3 active site. The inhibition is (a) enzymatic and (b) sub-stoichiometric/catalytic — one Akt molecule can inactivate many GSK3 molecules over time — the antithesis of a bound stoichiometric inhibitor. Thus the molecular-function mechanism required by GO:0030291 is absent. This is a clear case of **mechanism mis-typing**: an MF term describing "how the molecule works" has been applied on the basis of a downstream phenotype ("the target ends up less active").

---

## Mechanistic Model / Interpretation

The core of the analysis is distinguishing **what Akt1 does at the molecular level** from **what happens to its target downstream**. The two are frequently conflated in automated predictions, and that conflation is precisely what produced this prediction.

```
   CORRECT MODEL (catalytic)                 MIS-TYPED MODEL (implied by GO:0030291)
   ─────────────────────────                 ───────────────────────────────────────
   Growth factor / insulin                   Akt1 would have to be a
        │                                    stoichiometric inhibitor PROTEIN
        ▼                                    that BINDS GSK3 and blocks it
   PI3K → PIP3 → Akt1 (activated)                    │
        │                                            ▼
        │  Akt1 KINASE activity (EC 2.7.11.1)   [ NO SUCH DOMAIN / MECHANISM
        │  transfers ATP γ-phosphate             EXISTS IN Akt1 ]
        ▼
   GSK3β-Ser9-P  /  GSK3α-Ser21-P
        │
        │  phospho-Ser acts as intramolecular
        │  pseudosubstrate, blocks GSK3 active site
        ▼
   GSK3 activity ↓  (INHIBITED)   ◄── this downstream OUTCOME was
                                       mis-read as an MF "inhibitor activity"
```

**Molecular function (MF) — what Akt1 IS:** a protein serine/threonine kinase (GO:0004674). This is directly supported (IDA) and is the enzyme's intrinsic, primary activity.

**Biological process (BP) — what Akt1 DOES to GSK3:** negative regulation of GSK3 activity (and, generally, negative regulation of kinase activity). This is real and important, but it is the *consequence* of the MF, achieved through phosphorylation. The correct GO representation of the Cross et al. 1995 result is a **BP** term such as *negative regulation of glycogen synthase kinase-3 activity* / *negative regulation of protein kinase activity*, ideally with the causal MF being GO:0004674.

The single term **GO:0030291** tries to encode this BP outcome as an MF mechanism, and in doing so asserts a molecular capability (binding-based kinase inhibition) that Akt1 does not have.

| Aspect | Correct term | Evidence | Status |
|---|---|---|---|
| MF (what it is) | GO:0004674 protein serine/threonine kinase activity | IDA (BHF-UCL) | Retain — core function |
| MF (what it is) | GO:0004672 protein kinase activity | IDA (RGD) | Retain (parent) |
| BP (what it does to GSK3) | negative regulation of kinase / GSK3 activity | from PMID:8524413 | Add/retain as BP |
| MF (predicted) | **GO:0030291 kinase inhibitor activity** | IPI carry-over from GSK3 | **Remove / reject** |

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt P47196 (database) | Sequence/domain, database | **Refutes** prediction | Is Akt1's MF kinase or inhibitor? | "RAC-alpha serine/threonine-protein kinase," EC 2.7.11.1; PH + kinase + AGC-C-term domains; no pseudosubstrate/inhibitor domain; keywords Kinase/Transferase | Rat, curated record | High; database-level but reflects extensive primary evidence |
| GO record GO:0004674 IDA (BHF-UCL); GO:0004672 IDA (RGD) | Direct assay (annotated) | **Refutes** prediction (establishes catalytic MF) | Does Akt1 have direct kinase activity? | Kinase activity is experimentally supported (IDA) | Rat | High |
| [PMID: 8524413](https://pubmed.ncbi.nlm.nih.gov/8524413/) (Cross et al., *Nature* 1995) | Direct assay / mechanism | **Refutes** MF prediction; supports BP | Is GSK3 inhibition by Akt catalytic or binding-based? | "GSK3 is inhibited by serine phosphorylation…"; "protein kinase B … inactivates GSK3" — inhibition is via phosphorylation | Insulin/growth-factor signaling, cell/biochemical | High; this is the *source* reference for the annotation |
| QuickGO GO:0030291 annotation provenance | Database/interaction (IPI) | **Qualifies/Refutes** | What underlies the GO:0030291 term? | IPI, ref PMID:8524413, with-from rat GSK3α/β (P18265/P18266); human AKT1 term is ISS carry-over | Rat → human propagation | High; shows single-source, propagating annotation |
| QuickGO GO:0030291 ontology definition | Review/database (ontology) | **Refutes** | Does the term semantics fit Akt1? | Def: "Binds to and … reduces the activity of a protein Ser/Thr kinase"; exemplar annotees are stoichiometric inhibitors (p27^Kip1) | Ontology | High |
| [PMID: 28591657](https://pubmed.ncbi.nlm.nih.gov/28591657/) (AGC kinases review) | Review | **Refutes** (context) | Is PKB/Akt an active AGC kinase? | PKB/Akt is one of 63 AGC serine/threonine protein kinases, activated downstream of growth-factor signaling | Review | Medium; review-level orientation |
| [PMID: 12374740](https://pubmed.ncbi.nlm.nih.gov/12374740/) (Frödin et al.) | Structural/mechanistic | **Refutes** (context) | Is Akt/PKB a substrate-phosphorylating kinase? | PKBα activated by activation-loop + hydrophobic-motif phosphorylation; behaves as catalytic AGC kinase | Biochemistry/structure | Medium |
| [PMID: 19568789](https://pubmed.ncbi.nlm.nih.gov/19568789/) (PKB structure review) | Structural | **Refutes** (context) | Does PKB have kinase catalytic architecture? | X-ray structures of PKB PH and kinase domains; catalytic site rearrangement on activation | Structural biology | Medium |

---

## Evidence Base (Literature)

- *[PMID: 8524413](https://pubmed.ncbi.nlm.nih.gov/8524413/)* — **Inhibition of glycogen synthase kinase-3 by insulin mediated by protein kinase B** (Cross et al., *Nature* 1995). The origin reference for the GO:0030291 annotation. Its own wording establishes that PKB/Akt inactivates GSK3 **by serine phosphorylation** — i.e., catalytically. This paper simultaneously supports the *biological* fact (Akt negatively regulates GSK3) and *refutes* the MF typing (it is not a binding inhibitor).
- *[PMID: 28591657](https://pubmed.ncbi.nlm.nih.gov/28591657/)* — **AGC kinases, mechanisms of regulation and innovative drug development.** Establishes PKB/Akt as a bona fide member of the 63-strong AGC serine/threonine kinase group activated downstream of growth-factor signaling — i.e., an active kinase, not an inhibitor protein.
- *[PMID: 12374740](https://pubmed.ncbi.nlm.nih.gov/12374740/)* — **A phosphoserine/threonine-binding pocket in AGC kinases and PDK1…** Shows PKBα is activated by activation-loop and hydrophobic-motif phosphorylation and functions as a catalytic AGC kinase.
- *[PMID: 19568789](https://pubmed.ncbi.nlm.nih.gov/19568789/)* — **3-D structure and dynamics of protein kinase B…** X-ray structures of the PKB PH and kinase domains and the catalytic-site rearrangement on activation confirm canonical kinase architecture, with no inhibitor/pseudosubstrate module.
- *[PMID: 12169624](https://pubmed.ncbi.nlm.nih.gov/12169624/)* and *[PMID: 31964716](https://pubmed.ncbi.nlm.nih.gov/31964716/)* — supporting AGC-kinase regulation/structure context, consistent with Akt1 being a catalytic kinase.

---

## GO Curation Implications

**Leads (require curator verification):**

1. **Remove / do not add GO:0030291 (protein serine/threonine kinase inhibitor activity) as a molecular-function annotation on rat Akt1 (P47196).** The evidence indicates this is a mechanism-mistyped over-annotation. The term's definition requires binding-based inhibition; Akt1 inhibits GSK3 catalytically via phosphorylation. The existing IPI annotation (with-from GSK3α/β) documents an interaction whose functional consequence is phosphorylation, not stoichiometric inhibition.

2. **Retain GO:0004674 (protein serine/threonine kinase activity)** as the core MF — it is IDA-supported and represents Akt1's primary function.

3. **Capture the GSK3 effect as a biological process, not an MF.** Recommend a BP term such as **negative regulation of protein kinase activity** (or a more specific *negative regulation of glycogen synthase kinase-3 activity* if available/appropriate), sourced to PMID:8524413, ideally annotated so the causal MF is kinase activity. This preserves the true biology (Cross et al. 1995) without asserting a non-existent inhibitor mechanism.

4. **Flag the human AKT1 (P31749) GO:0030291 ISS annotation for the same treatment** — it is carry-over from the rat annotation and inherits the same mis-typing.

Because a more informative term (GO:0004674 as MF; negative-regulation BP) is available and supported, the recommendation does not fall back on "protein binding."

---

## Mechanistic Scope

**Immediate molecular function being tested:** whether Akt1 physically binds another serine/threonine kinase and reduces its activity *as an inhibitor protein* (GO:0030291), versus whether Akt1's molecular function is *catalytic kinase activity* whose downstream effect happens to be inhibition of a target kinase.

- **Direct gene-product activity:** phosphotransfer onto Ser/Thr of substrates (EC 2.7.11.1). This is what Akt1 *is* and *does* at the molecular level.
- **Downstream consequence (not MF):** GSK3 activity decreases because Akt1 phosphorylates GSK3 at Ser21/Ser9. This is a **pathway consequence**, mediated by the MF, and belongs in the BP aspect.
- **Not applicable here:** loss-of-function developmental phenotypes, disease manifestations. The prediction is refuted at the level of molecular mechanism, so no phenotype-level inference is needed to reject it.

The essential distinction: GO:0030291 is an MF that describes *how a molecule works* (binds and blocks a kinase). Akt1's inhibition of GSK3 describes *what happens to a target* (its activity drops) as a result of a *different* MF (kinase activity). The prediction mistakes the second for the first.

---

## Conflicts and Alternatives

- **Apparent conflict:** Akt1 unquestionably "inhibits" GSK3, and the phrase "inhibition of GSK3 by PKB" appears in the primary literature and drives the annotation. This is not a conflict at the level of biology — it is a conflict at the level of GO *aspect assignment*. The biology is real; the MF typing is wrong.
- **Paralog/ortholog carry-over:** The human AKT1 GO:0030291 annotation is ISS-propagated from rat, so the mis-typing is being copied across orthologs. There is no independent human experimental support. This matches the "paralog overannotation / frequency bias" failure mode named in the objective.
- **Alternative interpretation considered and rejected:** Could Akt1 act as a non-catalytic scaffold or pseudosubstrate for some kinase in a context where its catalytic activity is dispensable? No domain evidence supports a pseudosubstrate/inhibitor module, and no primary study was found describing Akt1 acting as a stoichiometric kinase inhibitor. The IPI with-from evidence points specifically to GSK3, whose inhibition is documented as phosphorylation-mediated.
- **In-vitro-only concern:** Not the issue here — the underlying biochemistry (Cross et al. 1995) is robust and in-cell; the problem is ontological typing, not assay artifact.

---

## Limitations and Knowledge Gaps

1. **Programmatic access to some resources was limited.** The findings synthesize UniProt/QuickGO records and the primary Cross et al. 1995 abstract as reported in the knowledge state; a curator should re-verify the QuickGO annotation provenance (evidence code IPI, with-from P18265/P18266, reference PMID:8524413) directly in the live QuickGO/GO_REF records before acting.
   - *Why it matters:* the recommendation to remove an MF term hinges on the provenance being exactly a GSK3-derived, phosphorylation-based interaction.
   - *Resolution:* pull the current GAF/annotation line for P47196 GO:0030291 from QuickGO.

2. **Whether a suitable specific BP term exists.** It was not exhaustively verified that a term like "negative regulation of glycogen synthase kinase-3 activity" exists in the current ontology.
   - *Why it matters:* the replacement recommendation needs a valid target term.
   - *Resolution:* check GO for the most specific available "negative regulation of … kinase activity" descendant.

3. **Scope of GO:0030291 usage.** The claim that GO:0030291 is reserved for stoichiometric/binding inhibitors rests on the definition text and a sample of annotees (e.g., p27^Kip1). A curator should confirm no GO convention permits catalytic-inhibitor annotation under this term.

4. **No structural/interaction database sweep (e.g., IntAct, PDB complexes) was performed here** to look for any bona fide Akt1–kinase inhibitory complex. Absence of evidence is not evidence of absence, though the mechanism and domain architecture make a genuine inhibitor role highly unlikely.

---

## Discriminating Tests

To definitively distinguish "catalytic kinase whose product is inhibited" from "kinase-inhibitor protein":

1. **Kinase-dead rescue test (mechanistic gold standard):** Express catalytically inactive Akt1 (e.g., K179M ATP-binding mutant or activation-loop/hydrophobic-motif phospho-site mutants) and ask whether GSK3 is still inhibited. Prediction under the catalytic model: **no inhibition** without kinase activity → refutes GO:0030291. If GSK3 were inhibited by mere binding, inhibition would persist. Existing literature already strongly implies the former.
2. **Phospho-site mutant target test:** Use GSK3β-S9A (non-phosphorylatable). If Akt1 can no longer inhibit S9A GSK3, inhibition is phosphorylation-dependent (catalytic), not binding-based.
3. **Stoichiometry / catalytic turnover assay:** Show that sub-stoichiometric Akt1 progressively inactivates excess GSK3 in an ATP-dependent manner — the signature of catalysis, incompatible with a 1:1 stoichiometric inhibitor.
4. **Interaction-database and structural check:** Query IntAct/BioGRID/PDB for any Akt1–kinase complex annotated as inhibitory and lacking a phosphotransfer readout. Absence supports removal.
5. **Ontology-consistency comparison:** Compare Akt1's annotation pattern to that of undisputed catalytic negative regulators (e.g., other kinases that inactivate targets by phosphorylation) to confirm the community convention uses BP negative-regulation terms rather than GO:0030291.

---

## Proposed Follow-up Actions / Curation Leads

**Candidate action change (lead — requires curator verification):**
- **Reject/remove** GO:0030291 (protein serine/threonine kinase inhibitor activity) as an MF annotation on rat Akt1 P47196, and do not accept the GO-GPT/BioReason-Pro prediction of this term. Classify as **over-annotation / mechanism mis-typing**.
- Apply the same scrutiny to the ISS-propagated GO:0030291 on human AKT1 (P31749).

**Candidate replacement / new terms (leads):**
- Retain MF: **GO:0004674** protein serine/threonine kinase activity (IDA-supported).
- Add/retain BP: **negative regulation of protein kinase activity** (or the most specific available *negative regulation of glycogen synthase kinase-3 activity*), evidenced by PMID:8524413.

**Candidate references with exact snippets to verify:**
- PMID:8524413 — verify verbatim: *"GSK3 is inhibited by serine phosphorylation in response to insulin or growth factors"* and *"Another insulin-stimulated protein kinase inactivates GSK3 under these conditions, and we demonstrate that it is the product of the proto-oncogene protein kinase B."* These establish that the inhibition is phosphorylation-mediated.
- QuickGO annotation line for P47196 GO:0030291 — verify evidence = IPI (ECO:0000353), reference = PMID:8524413, with/from = UniProtKB:P18265, P18266 (rat GSK3α/β).
- QuickGO ontology GO:0030291 — verify definition: *"Binds to and stops, prevents or reduces the activity of a protein serine/threonine kinase."*

**Suggested questions for the curator:**
1. Does GO convention ever permit GO:0030291 for a kinase that inhibits its target *by phosphorylation*? (Expected answer: no — that belongs in BP.)
2. Is there a specific "negative regulation of GSK3 activity" term to host the Cross et al. 1995 result?
3. Should the human AKT1 ISS annotation be withdrawn concurrently to prevent further propagation?

**Suggested experiments:** the kinase-dead rescue and GSK3β-S9A tests above (items 1–2 under Discriminating Tests) are the most efficient discriminators; both are standard and likely already answerable from existing literature.

---

## Conclusion

The GO:0030291 "protein serine/threonine kinase inhibitor activity" prediction for rat Akt1 (P47196) is **refuted as a molecular function**. Akt1 is a catalytic AGC serine/threonine kinase (GO:0004674, EC 2.7.11.1). Its inhibition of GSK3 — the sole documented basis for the annotation (PMID:8524413, IPI with-from GSK3α/β) — is achieved by phosphorylating GSK3 at Ser21/Ser9, a downstream consequence of its own kinase activity, not a distinct binding-based inhibitor function as GO:0030291 requires. The prediction recapitulates a mechanism-mistyped, ISS-propagated database annotation. Recommended curation: **remove/reject the GO:0030291 MF term**, retain **GO:0004674** as the core MF, and represent the GSK3 effect as a **biological-process negative-regulation** term.


## Artifacts

- [OpenScientist akt1 GO annotation trace](openscientist_artifacts/akt1_GO_annotation_trace.csv)
- [OpenScientist akt1 evidence matrix](openscientist_artifacts/akt1_evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)