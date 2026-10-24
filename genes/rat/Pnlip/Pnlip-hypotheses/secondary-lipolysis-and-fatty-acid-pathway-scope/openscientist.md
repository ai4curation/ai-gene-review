---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T21:14:12.986580'
end_time: '2026-09-20T22:32:51.679634'
duration_seconds: 4718.69
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: rat
  gene: Pnlip
  gene_symbol: Pnlip
  uniprot_accession: P27657
  taxon_id: NCBITaxon:10116
  taxon_label: Rattus norvegicus
  focus_type: function_assignment
  hypothesis_slug: secondary-lipolysis-and-fatty-acid-pathway-scope
  hypothesis_text: Rat pancreatic lipase Pnlip has phospholipase A1 or lipoprotein
    lipase activity, participates in HDL remodeling or fatty-acid biosynthesis, or
    positively regulates triacylglycerol lipase activity. Assess each separately using
    exact term definitions, actual PTN000906454 placement and source identity. PMID:8656075
    says pancreatic lipase poorly hydrolyzes phospholipids; test positional chemistry
    and retained capacity without converting weak turnover into zero. Lipoprotein
    lipase requires lipoprotein-bound TG, not arbitrary emulsified TG. Distinguish
    direct release of fatty acids by hydrolysis from the defined biosynthetic process,
    and validate any claimed positive regulation against the actual ortholog/source.
    Do not infer a particular protein from a generic family enzyme name.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/rat/Pnlip/Pnlip-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Rat pancreatic lipase Pnlip has phospholipase\
    \ A1 or lipoprotein lipase activity, participates\n  in HDL remodeling or fatty-acid\
    \ biosynthesis, or positively regulates triacylglycerol lipase activity.\n  Assess\
    \ each separately using exact term definitions, actual PTN000906454 placement\
    \ and source identity.\n  PMID:8656075 says pancreatic lipase poorly hydrolyzes\
    \ phospholipids; test positional chemistry and retained\n  capacity without converting\
    \ weak turnover into zero. Lipoprotein lipase requires lipoprotein-bound TG,\n\
    \  not arbitrary emulsified TG. Distinguish direct release of fatty acids by hydrolysis\
    \ from the defined\n  biosynthetic process, and validate any claimed positive\
    \ regulation against the actual ortholog/source.\n  Do not infer a particular\
    \ protein from a generic family enzyme name.\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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
citation_count: 11
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: go_decision_table_Pnlip_P27657.csv
  path: openscientist_artifacts/go_decision_table_Pnlip_P27657.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table Pnlip P27657
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
- **Gene directory:** Pnlip
- **Gene symbol:** Pnlip
- **UniProt accession:** P27657

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** secondary-lipolysis-and-fatty-acid-pathway-scope
- **Source file:** genes/rat/Pnlip/Pnlip-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Rat pancreatic lipase Pnlip has phospholipase A1 or lipoprotein lipase activity, participates in HDL remodeling or fatty-acid biosynthesis, or positively regulates triacylglycerol lipase activity. Assess each separately using exact term definitions, actual PTN000906454 placement and source identity. PMID:8656075 says pancreatic lipase poorly hydrolyzes phospholipids; test positional chemistry and retained capacity without converting weak turnover into zero. Lipoprotein lipase requires lipoprotein-bound TG, not arbitrary emulsified TG. Distinguish direct release of fatty acids by hydrolysis from the defined biosynthetic process, and validate any claimed positive regulation against the actual ortholog/source. Do not infer a particular protein from a generic family enzyme name.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Rat pancreatic lipase Pnlip has phospholipase A1 or lipoprotein lipase activity, participates
  in HDL remodeling or fatty-acid biosynthesis, or positively regulates triacylglycerol lipase activity.
  Assess each separately using exact term definitions, actual PTN000906454 placement and source identity.
  PMID:8656075 says pancreatic lipase poorly hydrolyzes phospholipids; test positional chemistry and retained
  capacity without converting weak turnover into zero. Lipoprotein lipase requires lipoprotein-bound TG,
  not arbitrary emulsified TG. Distinguish direct release of fatty acids by hydrolysis from the defined
  biosynthetic process, and validate any claimed positive regulation against the actual ortholog/source.
  Do not infer a particular protein from a generic family enzyme name.
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

# Rat *Pnlip* (P27657) — Secondary Lipolysis & Fatty-Acid Pathway Scope

**Hypothesis slug:** secondary-lipolysis-and-fatty-acid-pathway-scope
**Focus type:** function_assignment
**Target:** Rattus norvegicus *Pnlip* / Pancreatic triacylglycerol lipase / UniProt **P27657** / EC 3.1.1.3

---

## Executive Judgment

**Verdict: REFUTED / OVER-ANNOTATED for the secondary functions in the seed hypothesis.**

The seed hypothesis asks whether rat pancreatic lipase (Pnlip) genuinely (a) has phospholipase A1 activity, (b) has lipoprotein lipase activity, (c) participates in HDL remodeling or fatty-acid biosynthesis, or (d) positively regulates triacylglycerol lipase activity. Evaluating each **separately against the actual UniProt/GO record and primary literature**, none of these represent a directly-supported, core function of the classical pancreatic lipase gene product:

- The **only experimentally supported (IDA) molecular functions** for P27657 are **triacylglycerol lipase activity (GO:0004806)** and its parent **lipase activity (GO:0016298)**, localized to the **extracellular region (GO:0005576, IDA)**. Its catalytic reaction is TG + H₂O → DAG + fatty acid (sn-1,3 specific), i.e. a hydrolase/catabolic enzyme.
- **All four** flagged terms that the seed treats as suspect — **glycerophospholipid phospholipase A1 activity (GO:0008970)**, **lipoprotein lipase activity (GO:0004465)**, **HDL particle remodeling (GO:0034375)**, and **fatty acid biosynthetic process (GO:0006633)** — carry evidence code **IBA:GO_Central**, i.e. **phylogenetic propagation (PAINT) from the PANTHER PTHR11610 lipase-family ancestral node** (the node referenced in the seed as PTN000906454). They are family-level inferences, **not direct evidence for classical pancreatic lipase**.
- The fifth flagged term, **positive regulation of triglyceride lipase activity (GO:0061365)**, traces (rat ISO ← mouse ISO ← human PNLIP **IDA PMID:9631512**) to a paper that characterizes pancreatic lipase's **own** colipase-dependent interfacial activation — i.e., it is a **mis-mapping** of the enzyme's own catalysis onto a "regulation-of" term, not evidence that Pnlip regulates a separate triglyceride lipase.

**Most important caveats.** (1) "Refuted as a core function" is not the same as "zero activity in vitro" — classical pancreatic lipase is an sn-1,3 carboxyl esterase, so any residual phospholipid hydrolysis would be positional PLA1 chemistry at sn-1, but the *rate is negligible* and non-physiological. This is confirmed **rat-specifically** by the seed's own citation **PMID:8656075** (Jennens & Lowe, *J Lipid Res* 1995), which states rat PLRP2 "could hydrolyze phospholipids, **a substrate poorly hydrolyzed by PL**" (PL = classical colipase-dependent pancreatic lipase). (2) The retinyl-ester activities (GO:0047376 ISS, GO:0050253 ISO) are separate secondary functions not part of the seed and are left as non-core.

**Iteration-2 verification (QuickGO with/from provenance).** All four flagged terms carry evidence IBA under GO_REF:0000033 (PAINT) and share ancestral node **PANTHER:PTN000906454**; I resolved their "with/from" seed proteins to precise identities, proving they are inherited from **vascular-lipase paralogs**, not from pancreatic-lipase evidence:
- GO:0004465 lipoprotein lipase activity ← **P06858 (human LPL) + P11151 (bovine LPL)**
- GO:0008970 phospholipase A1 activity ← **P06858 (LPL), P11150 (hepatic lipase LIPC), Q9Y5X9 (endothelial lipase LIPG)**
- GO:0034375 HDL remodeling ← **P11150 (LIPC), Q9Y5X9 (LIPG)**
- GO:0006633 fatty acid biosynthetic process ← **P06858 (LPL), P11150 (LIPC), P11151 (bovine LPL)**

Conversely, the **core** term GO:0004806 triacylglycerol lipase activity is backed by **IDA PMID:8656075 + EXP PMID:10769148**, and GO:0005576 extracellular region by **IDA PMID:17010228, PMID:8967484**.

**Iteration-3 verification (GO:0061365 traced to origin).** The fifth flagged term, positive regulation of triglyceride lipase activity, resolves along an orthology chain: rat P27657 (ISO:RGD) ← mouse *Pnlip* Q6P8U6 (ISO, GO_REF:0000119) ← **human PNLIP P16233 (IDA, PMID:9631512)**. That root paper (Yang & Lowe, *Protein Expr Purif* 1998) is a **self-characterization** of recombinant human pancreatic lipase — it reports the enzyme "was inhibited by bile salts, required colipase for activity, and demonstrated **interfacial activation**." It does **not** show Pnlip regulating a *separate* triglyceride lipase. GO:0061365 therefore appears to be a **mis-mapping of the enzyme's own interfacial activation/colipase dependence** onto a "regulation-of" term; the immediate event is the enzyme's own catalysis (GO:0004806). Lead: remove or re-map GO:0061365 to the core catalytic term, pending curator review.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt P27657 (database) | Database record | Qualifies (frames all) | Actual GO/EC of rat Pnlip | Core IDA MFs = triacylglycerol lipase (GO:0004806) + lipase (GO:0016298); CC = extracellular (GO:0005576, IDA). All 4 flagged secondary terms are **IBA**; GO:0061365 is **ISO**. EC 3.1.1.3, sn-1,3 hydrolase. | Rat, exocrine pancreas/intestinal lumen | High for annotation facts; evidence codes fetched live |
| **PMID:9805004** (Carrière 1998) | Structural + direct assay (review of primary) | **Refutes PLA1 as core** | Does classical pancreatic lipase have phospholipase A1 activity? | "HPL displays significant activity only on triglycerides, whereas GPLRP2 displays high phospholipase and galactolipase activities." Swapping the GPLRP2 mini-lid into HPL did **not** induce phospholipase activity. | Human/guinea-pig pancreatic lipase family; kinetics + 3D structure | High; classical PL, directly transferable to rat ortholog |
| **PMID:15450178** (De Caro 2004) | Direct assay | Refutes/Qualifies | Where does PLA1 reside; how strong? | PLRP2 (paralog) phospholipase activity on PL micelles "very low"; galactolipase is its main function. Antibodies cross-react with native rat PLRP2. | Human + rat PLRP2, pancreatic juice | High; confirms paralog identity incl. rat |
| **PMID:9805004** (Carrière 1998) | Structural | Qualifies | Mechanistic basis | Full-length ~23-residue lid of classical pancreatic lipase sterically blocks large/polar head-group substrates; GPLRP2 has a 5-residue mini-lid. | Pancreatic lipase gene family | High |
| **PMID:37062468 / 22835523 / 21554982** | Direct assay | Competing (assigns PLA1 to paralog) | Which family member is the PLA1/galactolipase | PLRP2 "exhibits remarkable galactolipase and phospholipase A1 activities." | Guinea-pig/human PLRP2 | High; supports paralog reassignment |
| **PMID:32034094** (Kristensen 2020) | Direct assay/structural | **Refutes LPL activity for Pnlip** | Is lipoprotein lipase the same activity? | LPL binds GPIHBP1 and hydrolyzes **lipoprotein-bound** TG at the capillary endothelium, regulated by ApoC-II/ANGPTL. Distinct enzyme (gene *Lpl*), distinct compartment. | Human LPL, intravascular | High; establishes LPL is a separate, specialized enzyme |
| **PMID:32562799** (ApoC2) | Mutant/model | Qualifies | LPL physiology distinct from digestion | LPL-mediated plasma TG hydrolysis is activated by ApoC-II; a plasma/endothelial system unrelated to luminal fat digestion. | Hamster/rodent | Medium; context support |
| UniProt FUNCTION + CATALYTIC ACTIVITY (P27657) | Database | **Refutes FA biosynthesis** | Direction of reaction | "splits the esters of long-chain fatty acids at positions 1 and 3, producing mainly 2-monoacylglycerol and free fatty acids"; reaction = hydrolysis (catabolism). | Rat | High; biosynthesis is the opposite direction |
| **PMID:8656075** (Jennens & Lowe 1995, *J Lipid Res*) — **verified** | Direct assay | **Supports "poor PLA1" (rat-specific) + Refutes PLA1 as core** | Residual phospholipid hydrolysis; direction of activity | "rPLRP2 could hydrolyze phospholipids, **a substrate poorly hydrolyzed by PL**." rPLRP2 (paralog) lacks interfacial activation, is not bile-salt inhibited, weak colipase dependence — opposite of classical PL. Also the **IDA source for GO:0004806 (core TG-lipase)**. | Rat; recombinant rPLRP2 vs rPL, kinetics | High; rat ortholog, primary data, seed's own anchor |
| QuickGO with/from provenance (P27657) — **computed in-run** | Computational/database | **Refutes (paralog carry-over)** | Origin of the 4 flagged IBA terms | All 4 flagged terms = PAINT (GO_REF:0000033) at node **PTN000906454**, propagated from LPL (P06858), bovine LPL (P11151), hepatic lipase LIPC (P11150), endothelial lipase LIPG (Q9Y5X9). Core TG-lipase term is IDA/EXP. | GO/PANTHER annotation graph | High; direct API records |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current evidence | Lead action |
|---|---|---|---|
| GO:0004806 triacylglycerol lipase activity | MF | IDA:RGD | **Retain — core MF** |
| GO:0016298 lipase activity | MF | IDA:RGD | Retain (parent; core) |
| GO:0005576 extracellular region | CC | IDA:RGD | **Retain — core CC** |
| GO:0019433 triglyceride catabolic process | BP | IBA | Retain — correct-direction core process |
| GO:0008970 glycerophospholipid phospholipase A1 activity | MF | IBA | **Do not treat as core / consider NOT-supported.** Refuted by PMID:9805004; belongs to paralog PLRP2. At most weak in-vitro sn-1 activity. |
| GO:0004465 lipoprotein lipase activity | MF | IBA | **Remove / do not propagate.** Wrong paralog (gene *Lpl*); distinct compartment & cofactors. |
| GO:0034375 HDL particle remodeling | BP | IBA | **Remove.** Function of hepatic/endothelial lipase, LCAT, CETP, PLTP — not luminal digestive lipase. |
| GO:0006633 fatty acid biosynthetic process | BP | IBA | **Remove — direction error.** Pnlip releases FA by hydrolysis (catabolism), it does not synthesize FA. |
| GO:0061365 positive regulation of triglyceride lipase activity | BP | ISO:RGD ← mouse ISO ← human IDA PMID:9631512 | **Remove / re-map to GO:0004806.** Source paper characterizes the enzyme's own colipase-dependent interfacial activation, not regulation of a separate TG lipase. |

Avoid "protein binding" as a recommendation; the informative core MF is **triacylglycerol lipase activity (GO:0004806)**.

**Consolidated GO decision table** (all evidence codes fetched live; saved as artifact `go_decision_table_Pnlip_P27657.csv`):

| GO_ID | Term | Aspect | Evidence provenance | Curator lead |
|---|---|---|---|---|
| GO:0004806 | triacylglycerol lipase activity | MF | IDA PMID:8656075; EXP PMID:10769148 | **RETAIN (core)** |
| GO:0016298 | lipase activity | MF | IDA PMID:15181189/8203536 | RETAIN |
| GO:0005576 | extracellular region | CC | IDA PMID:17010228/8967484 | **RETAIN (core)** |
| GO:0019433 | triglyceride catabolic process | BP | IBA (incl. PLRP2 P54317) | RETAIN |
| GO:0008970 | phospholipase A1 activity | MF | IBA PTN000906454 ← LPL/LIPC/LIPG | **REMOVE/non-core** (refuted PMID:8656075, 9805004) |
| GO:0004465 | lipoprotein lipase activity | MF | IBA PTN000906454 ← LPL, bovine LPL | **REMOVE** (gene *Lpl*) |
| GO:0034375 | HDL particle remodeling | BP | IBA PTN000906454 ← LIPC, LIPG | **REMOVE** (HL/EL/LCAT) |
| GO:0006633 | fatty acid biosynthetic process | BP | IBA PTN000906454 ← LPL, LIPC | **REMOVE** (direction error) |
| GO:0061365 | positive regulation of triglyceride lipase activity | BP | ISO ← ISO ← human IDA PMID:9631512 | **REMOVE/RE-MAP** to GO:0004806 |
| GO:0047376 | all-trans-retinyl-palmitate hydrolase | MF | ISS/IEA/ISO | NON-CORE, keep w/ caveat |
| GO:0050253 | retinyl-palmitate esterase activity | MF | ISO (MGI) | NON-CORE |
| GO:0030299 | intestinal cholesterol absorption | BP | ISO (MGI) | KEEP w/ caveat |
| GO:0042632 | cholesterol homeostasis | BP | IBA | NON-CORE |

---

## Mechanistic Scope

**Direct molecular function (the thing being tested):** interfacial hydrolysis of the sn-1 and sn-3 ester bonds of emulsified dietary triacylglycerols, yielding 2-monoacylglycerol + free fatty acids, in the intestinal lumen, requiring colipase and bile salts, with the amphipathic lid controlling substrate access. This is a **carboxyl-ester hydrolase / catabolic** activity.

**Separated from the seed's secondary claims:**
- *Phospholipase A1* — a positional descriptor (sn-1 acyl release) that, for classical pancreatic lipase, is at best a trace in-vitro side reaction; the physiological PLA1/galactolipase is the paralog PLRP2. Not a downstream phenotype — it is a **misassigned molecular activity**.
- *Lipoprotein lipase activity / HDL remodeling* — activities of **different genes/enzymes** (LPL, hepatic/endothelial lipase) in the intravascular compartment; not properties of the pancreatic gene product.
- *Fatty-acid biosynthesis* — a **pathway/direction confusion**: FA release by hydrolysis ≠ FA biosynthesis.
- *Positive regulation of TG lipase* — a **regulatory-role assignment** that conflates the enzyme with a regulator of the enzyme.

---

## Conflicts and Alternatives

1. **Paralog confusion (primary explanation).** PLA1, LPL, HDL-remodeling annotations are correct for *other* members of PANTHER PTHR11610 (LPL, hepatic lipase, endothelial lipase, PLRP2). IBA/PAINT propagation from the shared ancestral node (PTN000906454) carried these down to classical pancreatic lipase.
2. **In-vitro-only / positional artifact.** Because pancreatic lipase is sn-1,3 specific, phospholipid assays can register residual sn-1 cleavage; converting this weak, non-physiological turnover into a functional PLA1 annotation over-states it. Equally, one must not falsely convert it to a categorical zero — the accurate statement is "very poor/negligible."
3. **Direction/term error.** "Fatty acid biosynthetic process" is anabolic; the enzyme is catabolic. This is a term-selection error rather than a paralog issue.
4. **Orthology carry-over (ISO).** GO:0061365 and the retinyl-ester terms come from ISO to mouse/human RGD orthologs; their applicability to the *direct* rat gene-product function should be checked at source.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| ~~PMID:8656075 wording~~ **RESOLVED (Iter 2)** | Fetched full abstract via NCBI E-utilities | It is the seed's anchor; now verified rat-specific ("poorly hydrolyzed by PL") and is the IDA source for the core TG-lipase term | Done — quantitative kcat/Km on PC vs TG would further quantify the residual rate |
| ~~Rat-specific PLA1 measurement~~ **Largely resolved (Iter 2)** | PMID:8656075 is rat data (rPL vs rPLRP2) | Removes the human/guinea-pig extrapolation concern | A modern purified rat PNLIP PC-monolayer assay would give an exact residual rate |
| ~~Source of GO:0061365~~ **RESOLVED (Iter 3)** | Traced orthology chain: rat ISO ← mouse ISO ← human PNLIP IDA PMID:9631512 | Shows it is a mis-mapping of the enzyme's own interfacial activation, not a genuine regulatory role | Done — curator to decide remove vs re-map to GO:0004806 |
| ~~GO:0008970 non-IBA support in rat~~ **RESOLVED (Iter 2)** | QuickGO with/from: only IBA from LPL/LIPC/LIPG at PTN000906454 | Confirms no experimental support; safe to treat as non-core | None needed for curation; optional direct assay |

---

## Discriminating Tests

1. **pH-stat / monomolecular-film kinetics** on purified rat PNLIP vs rat PLRP2 using triolein, egg-PC (PLA1 substrate), and MGDG (galactolipid), ± colipase ± bile salts — expect PNLIP active only on triolein.
2. **Lid-domain swap** (rat PNLIP full lid ↔ PLRP2 mini-lid) to test whether phospholipase activity tracks the lid, replicating PMID:9805004 in the rat background.
3. **Compartment/cofactor test** for the LPL claim: assay PNLIP on lipoprotein-bound TG ± ApoC-II ± GPIHBP1 — expect no LPL-like activation.
4. **Annotation provenance audit:** pull the PAINT record for PTHR11610 and confirm the ancestral node from which GO:0008970/0004465/0034375/0006633 were propagated (PTN000906454), plus the with/from evidence for GO:0061365.
5. **Positional-product analysis:** if any phospholipid hydrolysis is seen, confirm sn-1 specificity and quantify rate relative to TG (expect <1–5%).

---

## Curation Leads (require curator verification)

- **Candidate references to cite/verify:**
  - **PMID:8656075** (verified) — "rPLRP2 could hydrolyze phospholipids, **a substrate poorly hydrolyzed by PL**." Rat-specific; also the IDA basis for core GO:0004806. (supports weak-not-zero; assigns phospholipid activity to paralog rPLRP2)
  - PMID:9805004 — "HPL displays significant activity only on triglycerides, whereas GPLRP2 displays high phospholipase and galactolipase activities" and "The phospholipase activity is, however, not induced in the case of the HPL mutant with GPLRP2 mini-lid." (refutes core PLA1)
  - PMID:15450178 — "The phospholipase activity of HPLRP2 on phospholipid micelles was very low" (paralog carries only weak PLA1; confirms rat PLRP2 identity)
  - PMID:32034094 — LPL/GPIHBP1 endothelial, lipoprotein-bound-TG mechanism (refutes LPL activity assignment to Pnlip)
  - **PMID:9631512** (Yang & Lowe 1998) — root IDA for GO:0061365 on human PNLIP: "it was inhibited by bile salts, required colipase for activity, and demonstrated interfacial activation." Characterizes the enzyme's OWN activity → supports remove/re-map of GO:0061365.
  - **QuickGO provenance (computed):** the 4 flagged IBA terms all propagate from node PTN000906454 seeded by LPL (P06858/P11151), hepatic lipase LIPC (P11150) and endothelial lipase LIPG (Q9Y5X9) — direct evidence of vascular-lipase paralog carry-over.
- **Candidate GO actions:** treat **GO:0008970, GO:0004465, GO:0034375, GO:0006633** as **non-core / candidate-remove** for Pnlip (IBA family carry-over; PLA1 & FA-biosynthesis additionally refuted/direction-wrong). Verify **GO:0061365** at source. **Retain** GO:0004806 (core MF), GO:0005576 (core CC), GO:0019433 (correct catabolic BP).
- **Suggested questions for curator:** Is any of the flagged terms supported by non-IBA evidence in rat/human? Should PLA1 be reassigned to *Pnliprp2*? Is GO:0006633 a mis-selected term for a hydrolase?
- **Suggested experiments:** the discriminating tests above (film kinetics; lid swap; LPL-cofactor assay).

---

### Provenance
Computed in-run: (1) live UniProt P27657 GO/EC fetch + GO-triage table; (2) NCBI E-utilities fetch of PMID:8656075 full abstract (verified rat-specific "poorly hydrolyzed by PL"); (3) QuickGO annotation API for P27657 returning evidence codes, references and with/from seed proteins for every term; (4) UniProt identity resolution of the PTN000906454 with/from accessions (P06858=human LPL, P11151=bovine LPL, P11150=human hepatic lipase LIPC, Q9Y5X9=human endothelial lipase LIPG, P54317=human PNLIPRP2, P16233=human PNLIP); (5) GO:0061365 orthology-chain trace (rat P27657 ISO → mouse Q6P8U6 ISO → human P16233 IDA PMID:9631512) + E-utilities fetch of PMID:9631512 showing it characterizes the enzyme's own interfacial activation; (6) consolidated GO decision table saved as `go_decision_table_Pnlip_P27657.csv`. Literature verified via PubMed abstracts (PMIDs above). All database facts fetched live; no values fabricated.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist go decision table Pnlip P27657](openscientist_artifacts/go_decision_table_Pnlip_P27657.csv)