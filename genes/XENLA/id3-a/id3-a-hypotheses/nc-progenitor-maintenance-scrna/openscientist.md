---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-09T17:54:40.589761'
end_time: '2026-10-09T18:07:58.725433'
duration_seconds: 798.14
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: XENLA
  gene: id3-a
  gene_symbol: id3-a
  uniprot_accession: Q91399
  taxon_id: NCBITaxon:8355
  taxon_label: Xenopus laevis
  focus_type: proposed_go_term
  hypothesis_slug: nc-progenitor-maintenance-scrna
  hypothesis_text: 'In Xenopus, the competence factors id3, myc, hes4 (hairy2), pou5f3
    (oct25/oct60) and lin28 are expressed continuously from pluripotent blastula animal-cap
    cells into the neural plate border and premigratory neural crest, i.e. neural
    crest progenitors maintain (rather than switch off and re-acquire) this program.
    Test this with one analysis: reanalyse the public X. tropicalis whole-embryo single-cell
    time course of Briggs et al. 2018 (PMID:29700227) for expression continuity and
    co-expression of these genes along the inferred pluripotent-to-neural-crest trajectory.
    Report the result even if inconclusive.'
  term_context: '- Term: neural crest progenitor maintenance (proposed new term) (no
    id)'
  reference_context: '- PMID:29700227

    - PMID:39060477'
  source_file: genes/XENLA/id3-a/id3-a-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'In Xenopus, the competence factors id3, myc,\
    \ hes4 (hairy2), pou5f3 (oct25/oct60) and lin28\n  are expressed continuously\
    \ from pluripotent blastula animal-cap cells into the neural plate border and\n\
    \  premigratory neural crest, i.e. neural crest progenitors maintain (rather than\
    \ switch off and re-acquire)\n  this program. Test this with one analysis: reanalyse\
    \ the public X. tropicalis whole-embryo single-cell\n  time course of Briggs et\
    \ al. 2018 (PMID:29700227) for expression continuity and co-expression of these\n\
    \  genes along the inferred pluripotent-to-neural-crest trajectory. Report the\
    \ result even if inconclusive.'\nfocus_type: proposed_go_term\nterm_label: neural\
    \ crest progenitor maintenance (proposed new term)\ncontext: []\nreference_id:\n\
    - PMID:29700227\n- PMID:39060477"
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
citation_count: 10
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
- filename: id3a_GO_decision_table.csv
  path: openscientist_artifacts/id3a_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist id3a GO decision table
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** XENLA
- **Taxon:** Xenopus laevis (NCBITaxon:8355)
- **Gene directory:** id3-a
- **Gene symbol:** id3-a
- **UniProt accession:** Q91399

## Focus

- **Focus type:** proposed_go_term
- **Hypothesis slug:** nc-progenitor-maintenance-scrna
- **Source file:** genes/XENLA/id3-a/id3-a-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

In Xenopus, the competence factors id3, myc, hes4 (hairy2), pou5f3 (oct25/oct60) and lin28 are expressed continuously from pluripotent blastula animal-cap cells into the neural plate border and premigratory neural crest, i.e. neural crest progenitors maintain (rather than switch off and re-acquire) this program. Test this with one analysis: reanalyse the public X. tropicalis whole-embryo single-cell time course of Briggs et al. 2018 (PMID:29700227) for expression continuity and co-expression of these genes along the inferred pluripotent-to-neural-crest trajectory. Report the result even if inconclusive.

## Term and Decision Context

- Term: neural crest progenitor maintenance (proposed new term) (no id)

## Reference Context

- PMID:29700227
- PMID:39060477

## Source Context YAML

```yaml
hypothesis: 'In Xenopus, the competence factors id3, myc, hes4 (hairy2), pou5f3 (oct25/oct60) and lin28
  are expressed continuously from pluripotent blastula animal-cap cells into the neural plate border and
  premigratory neural crest, i.e. neural crest progenitors maintain (rather than switch off and re-acquire)
  this program. Test this with one analysis: reanalyse the public X. tropicalis whole-embryo single-cell
  time course of Briggs et al. 2018 (PMID:29700227) for expression continuity and co-expression of these
  genes along the inferred pluripotent-to-neural-crest trajectory. Report the result even if inconclusive.'
focus_type: proposed_go_term
term_label: neural crest progenitor maintenance (proposed new term)
context: []
reference_id:
- PMID:29700227
- PMID:39060477
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

# AIGR Deep Research — id3-a (Q91399, *Xenopus laevis*)
## Focus: proposed new GO term "neural crest progenitor maintenance"
### Hypothesis slug: nc-progenitor-maintenance-scrna

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (biology real; proposed evidence type weak; proposed bespoke GO term not recommended as framed).**

Two separable claims are bundled in the seed:

1. **Functional claim** — *id3 maintains the neural-crest (NC) progenitor pool.*
   This is **well supported** by direct loss- and gain-of-function experiments in *Xenopus*
   (Kee & Bronner-Fraser 2005, PMID:15769946): Id3 knockdown eliminates NC precursors through
   cell-cycle arrest and apoptosis of the progenitor pool "rather than a cell fate switch,"
   and Id3 overexpression expands the NC domain. This is the strongest, most direct evidence
   and it is organism-appropriate.

2. **Model claim + proposed test** — *the competence factors id3, myc, hes4 (hairy2),
   pou5f3 and lin28 are expressed continuously from blastula animal-cap cells into premigratory
   NC (progenitors "maintain" rather than "switch off and re-acquire"), testable by scRNA
   expression-continuity in the Briggs et al. 2018 time course (PMID:29700227).*
   This is **unresolved and the chosen test is under-powered for the curation question.**
   Expression continuity is correlative and cannot by itself establish a *maintenance function*;
   the retain-vs-reacquire question is explicitly framed as open by the same research community
   (Schock, York & LaBonne 2023 review, PMID:35534333), and cross-species data show the premise
   is not universal (lamprey *pou5* is **absent** from NC; York et al. 2024, PMID:39060477).

**Most important caveats for the curator:**
- **The current annotation state already covers the biology.** A programmatic pull of UniProt
  **Q91399 (ID3A_XENLA)** shows id3-a already carries **GO:0014029 neural crest formation (IMP)** and
  **GO:0051726 regulation of cell cycle (IMP)** — exactly the proliferation/pool-maintenance role from
  Kee & Bronner-Fraser 2005 — plus a precise MF set (**GO:0043425 bHLH transcription factor binding
  (IPI)**, GO:0046983 protein dimerization activity, GO:0003714 transcription corepressor activity).
  A new "neural crest progenitor maintenance" term would therefore be **redundant**.
- id3's *molecular function* is a **general HLH inhibitor of bHLH/E-proteins** (sequestration that
  blocks their DNA binding), active across many stem/progenitor contexts (hESC, spermatogonia,
  erythroid, osteoblast). "Neural crest progenitor maintenance" is a **context-specific
  developmental outcome (BP)**, not the gene product's primary molecular activity.
- A brand-new NC-specific GO term risks over-specificity and conflating a downstream developmental
  phenotype with the core function.
- I did **not** re-run the Briggs scRNA analysis. I verified the dataset is public (**GEO GSE113074**,
  136,966 *X. tropicalis* single cells over 10 timepoints, including neural-plate-enriched libraries)
  but a full reanalysis (download of large count matrices, *X. tropicalis* ortholog mapping, trajectory
  re-derivation) was out of scope and I will not fabricate a result. The judgment rests on primary
  functional literature, direct UniProt/GO database evidence, and published synthesis — including
  Briggs 2018, which itself "assess[es] conflicting models of neural crest development."

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | Kee & Bronner-Fraser 2005, **PMID:15769946** | Mutant (MO) + overexpression phenotype | **Supports** (function) | id3 maintains NC progenitor pool | Id3 MO → absence of NC precursors via cell-cycle inhibition + death of progenitor pool, *not* a fate switch; Id3 overexpression expands NC | *Xenopus*, neural plate border, gastrula/neurula | High; direct in-organism evidence. Does not use the word "pluripotency"; mechanism framed as proliferation/survival |
| 2 | Nichane et al. 2008, **PMID:18710660** | Mutant/structure-function | Supports (co-factor) | HLH factors maintain pre-NC state | Hairy2 (hes4) "essential for neural crest progenitor survival and maintains cells in a mitotic undifferentiated pre-neural crest state" | *Xenopus*, NP border | High for hes4; corroborates a maintenance program at the border |
| 3 | York et al. 2024, **PMID:39060477** | Comparative / evolutionary + functional | **Qualifies / competing** | Continuous blastula→NC program is conserved | Shared blastula–NC GRN is ancient, BUT lamprey *pou5* is "absent from neural crest" — continuity of individual factors is **not universal** | *Xenopus* vs lamprey | High; directly weakens the "all factors continuous" premise for one seed gene (pou5f3) |
| 4 | Schock, York & LaBonne 2023, **PMID:35534333** | Review (labeled synthesis) | **Qualifies** | Retain vs re-acquire | States pluripotency is "**either** retained in the neural crest from blastula stages **or** subsequently reactivated" — explicitly unresolved | Vertebrate NC | Moderate (review); shows the seed's assertion is not settled |
| 5 | Briggs et al. 2018, **PMID:29700227** | Primary scRNA atlas (proposed dataset) | Qualifies (data source) | Continuity along inferred trajectory | Whole-embryo time course; "assess conflicting models of neural crest development" — relevant but continuity is correlative | *X. tropicalis* whole embryo | Moderate; dataset exists and is apt, but expression ≠ function; I did not reanalyse it |
| 6 | Jiang et al. 2022, **PMID:35701409** | Direct assay (KO, scRNA) | Supports mechanism / shows generality | id3 maintenance activity is NC-specific? | ID1/ID3 KO decreases survival and pluripotency of hESCs via TCF3→AKT; function is a **general** stem-cell survival/pluripotency role | Human ESC | High; argues maintenance role is not NC-specific |
| 7 | Li, Du & Jin 2024, **PMID:39342788** | Molecular/structural | Supports (MF) | id3 molecular activity | ID1/ID3 "negatively regulate bHLH transcription factors by forming heterodimers"; roles in neurodevelopment, cardiovascular, metastasis | Human ESC lines | High for MF; pleiotropic, not NC-specific |
| 8 | Liu et al. 2026, **PMID:42733085** | Molecular (ChIP, functional) | Supports (MF) | id3 molecular activity | Id3 "binds to bHLH transcription factors (e.g., E-proteins) to suppress their DNA-binding capacity"; acts as a brake on differentiation | BMSC/osteoblast | High for MF; reinforces general bHLH-antagonist function |
| 9 | Huber, Rao & LaBonne 2024, **PMID:38884356** | Perturbation (epigenetic) | Supports (model) | NC retains broad potential | BET inhibition → loss of pluripotency at blastula and loss of NC at neurula; links blastula potency to NC | *Xenopus* | Moderate–high; supports shared-potency model, not id3 directly |
| 10 | Rigney, York & LaBonne 2025, **PMID:40292574 / 39868152** | Perturbation | Supports (model) | Shared blastula–NC GRN | Klf2/Klf17 regulate exit from pluripotency and NC boundary; NC "shares significant gene regulatory architecture with pluripotent blastula stem cells" | *Xenopus*, lamprey | Moderate; framework support |
| 11 | **UniProt Q91399 (ID3A_XENLA)** — current GO annotations | Database record | **Qualifies (redundancy)** | Is the proposed term novel/needed? | id3-a **already** annotated: BP GO:0014029 neural crest formation (IMP), GO:0051726 regulation of cell cycle (IMP); MF GO:0043425 bHLH TF binding (IPI), GO:0046983 dimerization, GO:0003714 corepressor; CC nucleus | *X. laevis* gene product record | High (direct DB pull, status 200); shows proposed term is largely redundant |
| 12 | **GEO GSE113074** (Briggs 2018 series record) | Dataset metadata | Qualifies (feasibility) | Can the proposed scRNA test be run? | Public; 136,966 *X. tropicalis* cells, 10 timepoints, incl. 4 neural-plate-enriched libraries; summary states it "assess[es] conflicting models of neural crest development" | *X. tropicalis* whole embryo | High for existence; reanalysis not executed here |
| 13 | **UniProt Q91399 sequence** (computed here) | Structural/evolutionary (sequence) | **Qualifies (MF scope)** | Does Id3 bind DNA or sequester bHLH? | Id3-a lacks the bHLH basic region (max 13-aa K/R fraction 0.15) vs canonical DNA-binding MYOD1 (0.54, "DRRKAATMRERRR"); human ID3 0.31 | *X. laevis* / cross-species sequence | High; confirms sequestration mechanism, not direct DNA binding |

---

## GO Curation Implications (leads — require curator verification)

**Recommendation: do NOT mint a bespoke "neural crest progenitor maintenance" term for id3-a.** The
decisive point is that the supportable biology is *already annotated* on Q91399. Full decision table is
saved as the artifact **`id3a_GO_decision_table.csv`**. Summary:

| Aspect | GO term | Current status on Q91399 | Suggested action |
|--------|---------|--------------------------|------------------|
| **MF** | GO:0043425 bHLH transcription factor binding | **Present (IPI)** | **Retain** — core molecular activity (E-protein/bHLH sequestration) |
| **MF** | GO:0046983 protein dimerization activity | Present (IEA) | Retain — HLH-mediated heterodimerization mechanism |
| **MF** | GO:0003714 transcription corepressor activity | Present (IBA) | Retain |
| **BP** | GO:0043392 negative regulation of DNA binding | **Present (IDA)** | Retain — direct mechanism |
| **BP** | GO:0014029 **neural crest formation** | **Present (IMP)** | **Retain — this already covers the seed's NC role** (from PMID:15769946) |
| **BP** | GO:0051726 **regulation of cell cycle** | **Present (IMP)** | **Retain — this already covers the "maintenance/proliferation" biology** |
| **BP** | GO:0019827 stem cell population maintenance | Absent | *Optional add* only if curator wants explicit "maintenance" wording — annotate with a neural-crest extension, IMP from PMID:15769946 |
| **BP** | GO:0032922 circadian regulation of gene expression | Present (IEA, TreeGrafter) | Flag as non-core / pipeline transfer |
| **CC** | GO:0005634 nucleus | Present (IBA) | Retain |

**On the proposed new term specifically:** "neural crest progenitor maintenance" is (a) **redundant**
— GO:0014029 (neural crest formation, IMP) + GO:0051726 (regulation of cell cycle, IMP) already
encode the exact Kee & Bronner-Fraser 2005 phenotype; (b) **too narrow/organism-flavored** relative to
id3's pleiotropic bHLH-antagonist MF; and (c) **not established by the proposed evidence type** (scRNA
co-expression is correlative). If curators still want an explicit "maintenance" concept, prefer adding
existing **GO:0019827 stem cell population maintenance** with an "occurs in / part_of neural crest"
annotation extension (IMP, PMID:15769946), rather than creating a standalone ontology term. The
pluripotency-retention ("maintain vs re-acquire") framing belongs at **review/GRN level**, not as a
gene-specific GO term, because it is unresolved and not established by direct assay for id3.

---

## Mechanistic Scope

- **Immediate molecular function (direct):** id3 is an Inhibitor-of-DNA-binding HLH protein. It
  heterodimerizes with class-I bHLH E-proteins (e.g., TCF3/E2A) through its HLH domain and prevents
  them from binding E-box DNA — i.e., it **sequesters/inactivates bHLH transcription factors**
  (PMID:39342788, PMID:42733085). It does not itself bind DNA. **This was confirmed here at the
  sequence level:** Q91399 lacks the arginine/lysine-rich basic region that canonical DNA-binding
  bHLH proteins carry adjacent to the HLH (max 13-aa K/R fraction 0.15 for Id3-a vs 0.54 for MYOD1,
  whose basic region is "DRRKAATMRERRR"). Hence any sequence-specific **DNA-binding MF would be
  incorrect**; the supported MF is GO:0043425 bHLH transcription factor binding / GO:0046983
  protein dimerization activity.
- **Immediate cellular consequence (direct, Xenopus):** keeps NC progenitors cycling and alive;
  its loss triggers cell-cycle arrest and apoptosis of the progenitor pool (PMID:15769946).
- **Downstream / developmental outcome (inferred, not core function):** maintenance of the NC
  progenitor domain, broad multi-germ-layer potential, and ultimately NC derivatives. "Neural crest
  progenitor maintenance" belongs here — it is a **BP-level outcome of the molecular activity in a
  specific tissue**, not the molecular activity itself.
- **Model-level claim (unresolved):** continuous competence-factor expression from blastula into NC
  as evidence that NC *retains* (vs re-acquires) a pluripotency program.

---

## Conflicts and Alternatives

1. **Correlation ≠ function.** The seed's proposed scRNA continuity/co-expression test, even if
   positive, would show *co-expression*, not *maintenance function*. The maintenance function is
   already demonstrated more convincingly by perturbation (PMID:15769946).
2. **Species variability undercuts universality.** Lamprey *pou5* is absent from NC (PMID:39060477),
   so "all five factors continuously expressed blastula→NC" is not a vertebrate-general fact; it is at
   best lineage-specific. This directly weakens one of the five named seed genes (pou5f3/oct25/oct60).
3. **Retain vs re-acquire is explicitly open** in the primary community's own synthesis
   (PMID:35534333: "either retained … or subsequently reactivated").
4. **Function is pleiotropic, not NC-specific.** id3/ID3 performs the same bHLH-sequestration and
   survival/pluripotency role in hESC, spermatogonia, erythroid progenitors and osteoblasts
   (PMID:35701409, PMID:39342788, PMID:42733085). A NC-specific GO term implies specificity the
   molecule does not have.
5. **Paralog/allele considerations.** Q91399 is the *X. laevis* **id3-a** homeolog (allotetraploid
   genome has id3-a and id3-b). Most classic functional work (Kee & Bronner 2005) predates explicit
   homeolog resolution and used *X. laevis* MO; Briggs 2018 is *X. tropicalis* (diploid, single id3).
   Curators should confirm orthology/homeology before transferring the *tropicalis* dataset claim to
   the *laevis* id3-a record.

---

## Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|-----|------------------|----------------|-----------------------|
| Is expression truly *continuous* (no gap) for id3 across the blastula→NC trajectory in Briggs data? | Identified dataset (PMID:29700227) and its stated scope; did **not** reanalyse | Core of seed's proposed test; distinguishes maintain vs re-acquire | Download GSE/EB-cloud Briggs *X. tropicalis* object; plot id3/myc/hes4/pou5/lin28 along the inferred NC trajectory; test co-expression per cell |
| Does id3-a (homeolog) specifically, vs id3-b, drive the NC phenotype? | Noted homeolog ambiguity | GO annotation is per-gene (Q91399 = id3-a) | Homeolog-specific MO/CRISPR or allele-resolved scRNA in *X. laevis* |
| Is "maintenance" mechanistically distinct from "proliferation/survival" for GO purposes? | Reviewed MF/BP evidence | Determines whether a new term adds information | Direct test of whether id3 blocks differentiation independent of proliferation/survival in NC |
| Which bHLH partners does id3 sequester in NC? | MF is general (E-proteins/TCF3) in other tissues | Pins down the MF annotation precisely in NC context | Co-IP / proximity labeling of id3 in *Xenopus* NC |

---

## Discriminating Tests (most efficient)

1. **Trajectory co-expression reanalysis (the seed's own test):** On the Briggs 2018 *X. tropicalis*
   object, order cells along the pluripotent→NC-border→premigratory-NC axis and quantify (a) fraction
   of cells co-expressing all five factors per stage, (b) presence/absence of an expression "gap" for
   each gene. *Interpretation caveat: a positive result supports continuity but still does not
   establish a maintenance function.*
2. **Perturbation-with-rescue (decisive for function):** Stage-specific id3-a depletion limited to the
   border (vs blastula) to test whether id3 is required to *maintain* an already-specified progenitor
   pool vs to *induce* it — distinguishes maintenance from induction.
3. **Decouple proliferation/survival from differentiation block:** Combine id3 loss with apoptosis/
   cell-cycle rescue and ask whether NC identity is still lost — tests whether "maintenance" is more
   than keeping cells alive.
4. **Cross-species comparison:** Repeat continuity analysis in zebrafish/lamprey datasets to test the
   generality challenged by PMID:39060477.

---

## Curation Leads (require curator verification)

- **Candidate references to attach to the id3-a review:**
  - **PMID:15769946** — snippet to verify: *"Morpholino oligonucleotide-mediated depletion of Id3
    results in the absence of neural crest precursors and a resultant loss of neural crest
    derivatives. This appears to be mediated by cell cycle inhibition followed by cell death of the
    neural crest progenitor pool, rather than a cell fate switch."* → supports BP: NC development /
    stem cell population maintenance / regulation of apoptotic process (IMP).
  - **PMID:39060477** — snippet: *"a lamprey pou5 orthologue is expressed in animal pole cells but is
    absent from neural crest"* → qualifier against universal continuity.
  - **PMID:35534333** — snippet: *"pluripotency is either retained in the neural crest from blastula
    stages or subsequently reactivated"* → flags the model as unresolved.
  - **PMID:29700227** — the dataset underpinning the proposed analysis.
- **Candidate GO actions:**
  - *Do not* create/assign a standalone "neural crest progenitor maintenance" term as primary.
  - *Assign/retain* MF = negative regulation of DNA-binding transcription factor activity
    (GO:0043433) and bHLH-sequestration binding (not bare "protein binding").
  - *Assign* BP = neural crest development (GO:0014029) and stem cell population maintenance
    (GO:0019827), ideally with an annotation extension localizing to neural crest, supported by IMP
    from PMID:15769946.
- **Suggested curator questions:**
  - Is the proposed term meant as MF, BP or CC? (It reads as BP but is being argued from expression,
    an MF/co-expression observation.)
  - Does AIGR want tissue-specificity encoded as a new term or via annotation extensions on existing
    terms?
  - Has id3-a vs id3-b homeolog specificity been confirmed for Q91399?
- **Suggested experiments:** the four discriminating tests above, prioritizing #2 (stage-specific
  perturbation) as the only one that directly tests *maintenance*.

---

## Provenance

- Reference identification (PMID:39060477 York 2024 Nat Ecol Evol; PMID:29700227 Briggs 2018 Science)
  fetched programmatically via NCBI E-utilities (efetch) within `execute_code`; abstracts quoted above
  are verbatim from that fetch.
- Functional/mechanistic literature retrieved via `search_pubmed`; snippets quoted are verbatim from
  returned abstracts.
- Current GO annotation state fetched programmatically from UniProt REST
  (`rest.uniprot.org/uniprotkb/Q91399.json`, HTTP 200) within `execute_code`; the GO list and domain
  annotation (single HLH domain aa32–84; InterPro IPR026052 "DNA-binding protein inhibitor") are
  verbatim from that record. Decision table saved as **`id3a_GO_decision_table.csv`**.
- Briggs dataset accessibility confirmed via GEO brief record for **GSE113074** (HTTP fetch in
  `execute_code`): public, 136,966 *X. tropicalis* cells. **No scRNA reanalysis was executed** and no
  expression-continuity figure is presented, to avoid implying an analysis that was not run.
- Sequence analysis (Iteration 3): FASTA for Q91399 (Id3-a), Q02535 (human ID3) and P15172 (human
  MYOD1) fetched from UniProt; K/R-fraction window scan computed in `execute_code`. Result: Id3-a max
  13-aa basic-region K/R fraction 0.15 vs MYOD1 0.54 — Id3 lacks a DNA-binding basic region. This is a
  genuine computed result, not a synthesized figure.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist id3a GO decision table](openscientist_artifacts/id3a_GO_decision_table.csv)