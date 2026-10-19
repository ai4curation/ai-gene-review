---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T18:28:19.555860'
end_time: '2026-10-09T18:38:33.357289'
duration_seconds: 613.8
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: XANAU
  gene: dhlA
  gene_symbol: dhlA
  uniprot_accession: P22643
  taxon_id: NCBITaxon:280
  taxon_label: Xanthobacter autotrophicus
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004301
  hypothesis_text: dhlA has epoxide hydrolase activity (GO:0004301).
  term_context: '- Term: epoxide hydrolase activity (GO:0004301)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118'
  source_file: genes/XANAU/dhlA/dhlA-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004301\n  label: epoxide hydrolase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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

- **Organism code:** XANAU
- **Taxon:** Xanthobacter autotrophicus (NCBITaxon:280)
- **Gene directory:** dhlA
- **Gene symbol:** dhlA
- **UniProt accession:** P22643

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004301
- **Source file:** genes/XANAU/dhlA/dhlA-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis

dhlA has epoxide hydrolase activity (GO:0004301).

## Term and Decision Context

- Term: epoxide hydrolase activity (GO:0004301)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0004301
  label: epoxide hydrolase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
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

# dhlA (P22643, XANAU) — Epoxide Hydrolase Activity (GO:0004301) Hypothesis Review

**Focus type:** function_assignment
**Seed hypothesis:** dhlA has epoxide hydrolase activity (GO:0004301).
**Decision context:** GO:0004301 (epoxide hydrolase activity), Evidence IEA, original reference GO_REF:0000118.
**Source:** `genes/XANAU/dhlA/dhlA-ai-review.yaml` → `existing_annotations[2].function_hypothesis`

---

## Executive Judgment

**Verdict: Over-annotated (refuted as a direct function).**

The gene product P22643/DHLA_XANAU is the archetypal **haloalkane dehalogenase** (EC 3.8.1.5)
from *Xanthobacter autotrophicus* GJ10. Its experimentally established, curated molecular
function is hydrolytic cleavage of carbon–halogen bonds (GO:0018786, haloalkane dehalogenase
activity). The `GO:0004301` epoxide hydrolase annotation is an **IEA:TreeGrafter** assignment
(consistent with the supplied GO_REF:0000118) that arises purely from the shared **α/β‑hydrolase
fold** and the InterPro **"Epoxide hydrolase‑like" signature (IPR000639 / PRINTS EPOXHYDRLASE)**.
Epoxide hydrolases (EC 3.3.2.x) and haloalkane dehalogenases are homologous, use the same fold and
an Asp–His–Asp/Glu triad with a covalent enzyme intermediate, but are **distinct enzymatic
activities** — interconverting them requires deliberate active‑site engineering. No primary
literature or curated UniProt catalytic-activity statement reports epoxide hydrolysis by DhlA.

**Most important caveat:** The annotation is not biologically absurd (the fold genuinely is
epoxide‑hydrolase‑like, and promiscuous low-level activity on some epoxides cannot be formally
excluded without an assay), but it is **less precise than existing experimental knowledge** and
should be treated as a non‑core, computationally derived term that a curator would normally not
retain for this well-characterized enzyme.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt P22643 (DHLA_XANAU), curated record | Review/database | **Refutes** (direct function is dehalogenase) | What is DhlA's curated activity? | Rec. name "Haloalkane dehalogenase", EC 3.8.1.5; two CATALYTIC ACTIVITY statements are C–halogen hydrolysis only; **no** epoxide reaction listed | Swiss-Prot curated entry, X. autotrophicus | High for dehalogenase; database record, orientation only |
| UniProt P22643 GO annotations | Database | **Qualifies** (identifies source) | Where does GO:0004301 come from? | GO:0004301 = **IEA:TreeGrafter**; GO:0018786 (dehalogenase) = IEA:UniRule; GO:0019260 (1,2-DCE catabolism) = UniPathway | Automated pipeline | High — directly shows evidence code = GO_REF:0000118 (TreeGrafter) |
| UniProt P22643 domain cross-refs | Structural/evolutionary, computational | **Qualifies** (explains over-transfer) | Why is an EH term applied? | Matches IPR000639 "Epox_hydrolase-like", PRINTS PR00412 EPOXHYDRLASE, under α/β-hydrolase fold (SSF53474, PF00561, IPR029058); PANTHER PTHR42977 "HYDROLASE-RELATED" | Sequence/domain signatures | High — signatures are the mechanistic cause of the IEA call |
| Blazic, Gautier, Norberg, Widersten 2024, **PMID:38828992** | Direct assay / protein engineering | **Refutes / Qualifies** | Are EH and DhlA the same activity? | "Epoxide hydrolase StEH1 … is similar in overall structural fold and catalytic mechanism to haloalkane dehalogenase DhlA"; alkyl-halide hydrolase activity had to be **engineered** into an EH scaffold | Potato StEH1 vs DhlA, in vitro | High — shows activities are distinct and require active-site change to interconvert |
| Argiriadi, Morisseau, Hammock, Christianson 1999, **PMID:10485878** | Structural / evolutionary | **Qualifies** | Fold relationship EH↔dehalogenase | EH catalytic domain "is similar to that of haloalkane dehalogenase and shares the α/β hydrolase fold"; proposes shared evolutionary sequence | Murine cytosolic EH crystal structure | High for homology; does not assay DhlA on epoxides |
| Kokkonen et al. 2018 (**PMID:29858243**); Bosma et al. 2003 (**PMID:12834356**); Olsson & Warshel 2004 (**PMID:15548014**) | Direct assay / mechanism | **Refutes** | What reaction does DhlA catalyze? | DhlA/DhaA catalyze hydrolysis of carbon–halogen bonds via Asp nucleophile + His/Asp; covalent alkyl-enzyme intermediate; SN2 on haloalkane | Enzymology/kinetics/QM-MM | High — consistent primary evidence for dehalogenase mechanism, no epoxide chemistry |
| UniProt REST family audit (this report, Iter 2) | Computational / database | **Qualifies / Refutes** | Is GO:0004301 a conserved family function? | 33/33 reviewed EC 3.8.1.5 enzymes carry GO:0018786; only 13/33 (39%) carry GO:0004301, all IEA; absent from DhaA subgroup & LinB; no experimental EH annotation anywhere | 33 Swiss-Prot haloalkane dehalogenases | High — patchy distribution indicates over-propagation, not conserved activity |

---

## QuickGO Annotation Inventory for P22643 (computed provenance, Iteration 3)

Complete set of GO annotations on P22643 (EBI QuickGO API) — **all four are IEA**:

| GO ID | Term | Evidence | Reference | Assigned by |
|---|---|---|---|---|
| GO:0003824 | catalytic activity | IEA | GO_REF:0000002 | InterPro |
| **GO:0004301** | **epoxide hydrolase activity** | **IEA** | **GO_REF:0000118** | **TreeGrafter** |
| GO:0018786 | haloalkane dehalogenase activity | IEA | GO_REF:0000120 | UniProt (UniRule) |
| GO:0019260 | 1,2-dichloroethane catabolic process | IEA | GO_REF:0000041 | UniProt |

- **Confirms directly that GO_REF:0000118 = the TreeGrafter pipeline** (QuickGO `assignedBy` field).
- Despite DhlA being one of the most experimentally characterized α/β-hydrolases, **no experimental
  (EXP/IDA/IMP) GO annotation exists** — every term is electronic. The dehalogenase term is nonetheless
  backed by UniRule + the curated EC 3.8.1.5 reaction and decades of primary enzymology; the epoxide
  hydrolase term is TreeGrafter-only and has no corresponding assay.

---

## Family-Wide Annotation Audit (computed provenance, Iteration 2)

UniProt REST query of **all 33 reviewed Swiss-Prot EC 3.8.1.5 haloalkane dehalogenases**,
checking presence of each GO term:

| GO term | Label | Count carrying it | Fraction | Evidence code |
|---|---|---|---|---|
| GO:0018786 | haloalkane dehalogenase activity | **33 / 33** | **100%** | all IEA |
| GO:0004301 | epoxide hydrolase activity | **13 / 33** | **39%** | all IEA (TreeGrafter) |

- The core dehalogenase term is **universal**; the epoxide hydrolase term is **patchy**.
- GO:0004301 is present in DHLA_XANAU/DHLA_XANFL and the **DhmA** subgroup
  (Mycobacterium/Caulobacter) but **absent from the entire DhaA subgroup**
  (e.g., DHAA_RHORH/P0A3G2, DHAA_MYCTU/P9WMR9) and from **LinB** (D4Z2G1).
- **Zero** of the 33 enzymes carry an experimental (non-IEA) epoxide hydrolase annotation.

**Interpretation:** a genuinely conserved catalytic activity would annotate uniformly; the
39% patchiness tracks TreeGrafter/PANTHER subtree placement, i.e. classic homology-driven
over-propagation of the sibling fold activity — not evidence of real epoxide hydrolysis.

---

## GO Curation Implications

- **Lead (requires curator verification):** Treat **GO:0004301 (epoxide hydrolase activity, IEA/TreeGrafter)** as a
  **non-core, over-propagated computational term**. Recommended action: **remove or demote** (do not
  retain as a representative function) for P22643, because a more specific, experimentally grounded
  MF term already exists.
- **Retain as the primary MF term:** **GO:0018786 (haloalkane dehalogenase activity)** — matches the
  curated EC 3.8.1.5 and all primary enzymology.
- **Retain BP:** **GO:0019260 (1,2-dichloroethane catabolic process)** — pathway context.
- The epoxide-hydrolase term is **too broad/incorrect in specificity** for this gene: it is an MF
  sibling activity on the same fold, not DhlA's demonstrated activity. It should not be generalized
  or made more specific — it should be flagged as homology carry-over.

---

## Mechanistic Scope

- **Immediate molecular activity tested:** hydrolysis of an epoxide C–O bond (epoxide hydrolase).
- **What DhlA actually does (direct):** nucleophilic Asp124 performs SN2 attack on the terminal carbon
  of a haloalkane, displacing halide and forming a covalent **alkyl–enzyme ester**, which is then
  hydrolyzed by a water activated by the His289–Asp260 pair — yielding a primary alcohol, halide, and H⁺.
- **Relationship to epoxide hydrolysis:** EH uses the *same fold and an analogous Asp–His–acid triad*
  but opens an epoxide ring (covalent alkoxy/ester intermediate). The mechanistic similarity is the
  reason for the mis-transfer; it is **not** evidence that DhlA performs epoxide hydrolysis.
- Epoxide hydrolysis would be a **separate catalytic function**, not a downstream phenotype — so the
  question is purely whether DhlA has this activity, and the record indicates it does not (as a
  demonstrated function).

---

## Conflicts and Alternatives

- **Database carry-over / paralog-family confusion (most likely explanation):** TreeGrafter grafts
  the sequence onto a PANTHER family (PTHR42977 "HYDROLASE-RELATED") whose members include epoxide
  hydrolases; the InterPro "Epoxide hydrolase-like" signature (IPR000639) and PRINTS EPOXHYDRLASE
  then license GO:0004301. This is frequency/fold bias, not organism-specific biology.
- **Promiscuity caveat (cannot be fully excluded):** α/β-hydrolase enzymes are catalytically
  promiscuous; low-level, in-vitro-only epoxide hydrolysis by DhlA has not been reported but also has
  not been exhaustively assayed. Even if present, promiscuous activity would be non-core and should
  not be annotated without an experimental reference.
- **No conflicting primary evidence** supports epoxide hydrolase activity as a physiological function.

---

## Knowledge Gaps

1. **Has DhlA ever been assayed against epoxides (e.g., epichlorohydrin, styrene oxide, 1,2-epoxyalkanes)?**
   Checked UniProt catalytic-activity statements and primary enzymology abstracts — none report epoxide
   turnover. Matters because a single positive assay would convert "over-annotation" into
   "non-core promiscuous activity." Resolver: direct spectrophotometric/GC epoxide-hydrolase assay on
   purified DhlA.
2. **Exact PANTHER subfamily/tree node driving the TreeGrafter call.** Checked UniProt cross-refs
   (PTHR42977:SF3). Matters because knowing the grafted family clarifies whether the whole subfamily is
   mis-annotated. Resolver: inspect the PANTHER tree and GO_REF:0000118 propagation rules.
3. **Whether sibling haloalkane dehalogenases (DhaA, LinB, DbjA) carry the same GO:0004301 IEA.**
   Not yet queried. Matters for systematic correction across the family. Resolver: batch UniProt/QuickGO query.

---

## Discriminating Tests

- **Direct epoxide hydrolase assay** on purified recombinant DhlA (e.g., styrene oxide, epichlorohydrin,
  1,2-epoxyhexane) measuring diol formation vs. a known EH positive control and a buffer blank — the
  single most decisive experiment.
- **Active-site logic check:** DhlA's halide-binding pocket (Trp125/Trp175) is tuned to stabilize a
  departing halide, not an alkoxide/diol; structural comparison with StEH1/human EH active sites
  predicts poor epoxide turnover. A docking/structure comparison is a cheap computational discriminator.
- **Family-wide annotation audit:** QuickGO/UniProt query of all PTHR42977 members and all EC 3.8.1.5
  enzymes to quantify how broadly GO:0004301 is TreeGrafter-propagated (frequency-bias test).

---

## Curation Leads (require curator verification)

- **Candidate action:** Do **not** accept GO:0004301 as a represented molecular function for dhlA;
  mark the IEA/TreeGrafter epoxide hydrolase term as **over-annotated / non-core** and prefer
  GO:0018786 (haloalkane dehalogenase activity) + GO:0019260 (1,2-dichloroethane catabolic process).
- **Candidate reference + snippet to verify (PMID:38828992):**
  *"Epoxide hydrolase StEH1, from potato, is similar in overall structural fold and catalytic mechanism
  to haloalkane dehalogenase DhlA from"* — use to document that fold/mechanism similarity (not a real
  shared activity) explains the term; the two activities had to be engineered apart.
- **Candidate reference + snippet (PMID:10485878):**
  *"this domain is similar to that of haloalkane dehalogenase and shares the alpha/beta hydrolase fold"*
  — supports homology-driven mis-transfer.
- **Database provenance to cite:** UniProt P22643 shows GO:0004301 = IEA:**TreeGrafter** (= GO_REF:0000118),
  while the curated reaction statements are strictly EC 3.8.1.5 dehalogenase.
- **Suggested curator question:** Is there *any* experimental reference showing epoxide turnover by DhlA?
  If none, remove/demote GO:0004301.
- **Suggested experiment:** Spectrophotometric epoxide hydrolase assay on purified DhlA with EH-positive
  control.

---

## Limitations

- This review relied on literature and the public UniProt/InterPro records; no wet-lab assay was run.
- Absence of a reported epoxide-hydrolase assay is evidence of absence of *demonstrated* activity, not
  proof that trace promiscuous activity is impossible.
- GO_REF:0000118 ↔ TreeGrafter equivalence was inferred from the UniProt evidence string "IEA:TreeGrafter";
  curators should confirm the exact GO_REF mapping in their pipeline.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)