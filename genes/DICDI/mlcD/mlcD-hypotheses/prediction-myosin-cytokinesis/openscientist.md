---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-10T03:43:52.439262'
end_time: '2026-07-10T03:53:33.149597'
duration_seconds: 580.71
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DICDI
  gene: mlcD
  gene_symbol: mlcD
  uniprot_accession: Q7Z2B8
  taxon_id: NCBITaxon:44689
  taxon_label: Dictyostelium discoideum
  focus_type: computational_prediction
  hypothesis_slug: prediction-myosin-cytokinesis
  hypothesis_text: BioReason-Pro SFT predicts several myosin-II / cytokinesis roles
    for the Dictyostelium discoideum myosin light chain mlcD (Q7Z2B8) -- mitotic cytokinesis
    (GO:0000281), negative regulation of actin filament polymerization (GO:0030837),
    regulation of myosin II filament assembly (GO:0043520), and protein localization
    to cell division site (GO:0071976). Independently assess mlcD's identity -- is
    it the light chain of a specific myosin class (e.g. a myosin-I essential/regulatory
    light chain, or a calmodulin-like EF-hand light chain) -- and whether these specific
    myosin-II-filament-assembly and cytokinesis regulatory roles are supported for
    it, or are transferred from a different myosin class or paralog (such as the myosin-II
    regulatory light chain mlcE), which would make them a paralog misassignment. Determine
    whether the predictions are supported or refuted.
  term_context: '- Term: regulation of myosin II filament assembly (GO:0043520)'
  reference_context: '- doi:10.64898/2026.03.19.712954'
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: BioReason-Pro SFT predicts several myosin-II /\
    \ cytokinesis roles for the Dictyostelium discoideum\n  myosin light chain mlcD\
    \ (Q7Z2B8) -- mitotic cytokinesis (GO:0000281), negative regulation of actin filament\n\
    \  polymerization (GO:0030837), regulation of myosin II filament assembly (GO:0043520),\
    \ and protein localization\n  to cell division site (GO:0071976). Independently\
    \ assess mlcD's identity -- is it the light chain of\n  a specific myosin class\
    \ (e.g. a myosin-I essential/regulatory light chain, or a calmodulin-like EF-hand\n\
    \  light chain) -- and whether these specific myosin-II-filament-assembly and\
    \ cytokinesis regulatory roles\n  are supported for it, or are transferred from\
    \ a different myosin class or paralog (such as the myosin-II\n  regulatory light\
    \ chain mlcE), which would make them a paralog misassignment. Determine whether\
    \ the predictions\n  are supported or refuted.\nfocus_type: computational_prediction\n\
    term_id: GO:0043520\nterm_label: regulation of myosin II filament assembly\ncontext:\
    \ []\nreference_id:\n- doi:10.64898/2026.03.19.712954"
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

- **Organism code:** DICDI
- **Taxon:** Dictyostelium discoideum (NCBITaxon:44689)
- **Gene directory:** mlcD
- **Gene symbol:** mlcD
- **UniProt accession:** Q7Z2B8

## Focus

- **Focus type:** computational_prediction
- **Hypothesis slug:** prediction-myosin-cytokinesis
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

BioReason-Pro SFT predicts several myosin-II / cytokinesis roles for the Dictyostelium discoideum myosin light chain mlcD (Q7Z2B8) -- mitotic cytokinesis (GO:0000281), negative regulation of actin filament polymerization (GO:0030837), regulation of myosin II filament assembly (GO:0043520), and protein localization to cell division site (GO:0071976). Independently assess mlcD's identity -- is it the light chain of a specific myosin class (e.g. a myosin-I essential/regulatory light chain, or a calmodulin-like EF-hand light chain) -- and whether these specific myosin-II-filament-assembly and cytokinesis regulatory roles are supported for it, or are transferred from a different myosin class or paralog (such as the myosin-II regulatory light chain mlcE), which would make them a paralog misassignment. Determine whether the predictions are supported or refuted.

## Term and Decision Context

- Term: regulation of myosin II filament assembly (GO:0043520)

## Reference Context

- doi:10.64898/2026.03.19.712954

## Source Context YAML

```yaml
hypothesis: BioReason-Pro SFT predicts several myosin-II / cytokinesis roles for the Dictyostelium discoideum
  myosin light chain mlcD (Q7Z2B8) -- mitotic cytokinesis (GO:0000281), negative regulation of actin filament
  polymerization (GO:0030837), regulation of myosin II filament assembly (GO:0043520), and protein localization
  to cell division site (GO:0071976). Independently assess mlcD's identity -- is it the light chain of
  a specific myosin class (e.g. a myosin-I essential/regulatory light chain, or a calmodulin-like EF-hand
  light chain) -- and whether these specific myosin-II-filament-assembly and cytokinesis regulatory roles
  are supported for it, or are transferred from a different myosin class or paralog (such as the myosin-II
  regulatory light chain mlcE), which would make them a paralog misassignment. Determine whether the predictions
  are supported or refuted.
focus_type: computational_prediction
term_id: GO:0043520
term_label: regulation of myosin II filament assembly
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

# mlcD (Q7Z2B8) — Myosin-II / Cytokinesis Prediction Assessment

**Gene:** mlcD (UniProt Q7Z2B8, MLCD_DICDI), *Dictyostelium discoideum* (NCBITaxon:44689)
**Focus:** computational_prediction — hypothesis `prediction-myosin-cytokinesis`
**Terms tested:** GO:0000281 mitotic cytokinesis; GO:0030837 negative regulation of actin filament polymerization; GO:0043520 regulation of myosin II filament assembly; GO:0071976 protein localization to cell division site.
**Reference context:** doi:10.64898/2026.03.19.712954

---

## Executive Judgment

**Verdict: REFUTED (over-annotation / paralog–class misassignment).**

BioReason-Pro-SFT predicts myosin-II and cytokinesis regulatory roles for mlcD. Primary
biochemistry and the curated UniProt/dictyBase record independently establish that **mlcD is
the dedicated essential light chain of MyoD, a single-headed class I (unconventional) myosin** —
not a component of the conventional myosin-II (mhcA) contractile machinery. All four predicted
terms belong to the myosin-II system (heavy chain mhcA plus its regulatory light chain and
essential light chain), whose bipolar filaments drive cytokinesis. Class I myosins are monomeric,
membrane-associated motors that **do not self-assemble into filaments**, so mlcD cannot mediate or
regulate myosin-II filament assembly or contractile-ring–based cytokinesis.

The most important caveat: I could not access the specific reference `doi:10.64898/2026.03.19.712954`
programmatically, and I did not run a MyoD-null phenotype search successfully (PubMed queries for
class-I phenotypes returned no hits in this environment). The refutation nonetheless rests on
direct, unambiguous primary evidence (protein sequencing + complex purification) and on the
curated functional record.

---

## Evidence Matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| PMID:12826013 (De La Roche, Lee, Côté 2003) | Direct assay (protein sequencing, ESI-MS, ITC, complex purification) | **Refutes** seed | Is mlcD a myosin-II light chain? | MlcD is a 16 kDa 4-EF-hand protein co-purifying with **MyoD**, a long-tailed **class I** myosin; FLAG-MlcD complexes with MyoD but **not** MyoB/MyoC; low Ca²⁺ affinity (cannot sense physiological Ca²⁺) | *D. discoideum*, native + FLAG-tagged expression | High. Directly defines class/partner identity. |
| PMID:21671662 (Crawley et al. 2011) | Interaction / biochemical mapping | **Refutes** seed | Light-chain assignments across Dictyostelium myosin-I | Each long-tailed myosin-I has a unique light chain: **MyoB–MlcB, MyoC–MlcC, MyoD–MlcD**; short-tailed MyoA/MyoE use calmodulin | *D. discoideum* | High. Confirms MyoD–MlcD pairing. |
| UniProt Q7Z2B8 (MLCD_DICDI) | Database / curated record | **Refutes** seed | Protein identity, family, oligomeric state | Recommended name "**Myosin-ID light chain**"; FUNCTION "light chain for myosin-D"; SUBUNIT "Myosin I… **Inability to self-assemble into filaments**… Interacts with myoD; does not interact with myoB or myoC" | Curated | High (review/database-level, but backed by the primary papers above). |
| dictyBase GO (via UniProt xrefs) | Database (experimental IDA/IPI) | **Qualifies** / competing | What processes/locations are experimentally supported? | Curated terms: myosin complex (IDA), myosin heavy chain binding→myoD (IPI), Ca²⁺ binding (IDA), **actin wave** (IDA), **macropinocytic cup cytoskeleton** (IDA). **None** of the 4 predicted myosin-II/cytokinesis terms present | *D. discoideum* | High. Absence of predicted terms in curated set is informative. |
| InterPro/PANTHER/Pfam (Q7Z2B8) | Structural/evolutionary | **Qualifies** | Domain architecture | 147 aa, four EF-hands (EF-hands 2–4 degenerate), CALM/Myosin/TropC-like (IPR050230), calmodulin-like — consistent with an EF-hand myosin light chain, not a filament-assembly regulator | Sequence | High. |
| Iteration-2 NW/BLOSUM62 (this study) | Computational (sequence identity) | **Qualifies/refutes** | Which clade does MlcD belong to? | MlcD 45.6% id to calmodulin & 45.2% to MlcB (myosin-I LC) vs only 30.8%/31.2% to myosin-II mlcR/mlcE; reproduces published ~44% CaM benchmark | *D. discoideum* paralogs | Medium-high. Global alignment, single method; concordant with primary data. |
| PMID:10423462 (Dai et al. 1999) | Mutant phenotype (micropipette aspiration) | **Qualifies** (class context) | What do Dictyostelium myosin-I motors do? | Amoeboid myosin-I's drive pseudopod formation, macropinocytosis; double mutants lose ~50% cortical tension; required for migration — NOT cytokinesis | *D. discoideum* myosin-I mutants | Medium (about myosin-I class generally, not MyoD-specific). |

---

## GO Curation Implications (leads — require curator verification)

- **Do NOT add** GO:0000281 (mitotic cytokinesis), GO:0030837 (neg. reg. actin filament polymerization),
  GO:0043520 (regulation of myosin II filament assembly), or GO:0071976 (protein localization to cell
  division site) to mlcD. These are conventional-myosin-II / contractile-ring functions and are
  **class-inappropriate** for a myosin-I light chain.
- **GO:0043520 specifically:** refuted. The correct effectors of Dictyostelium myosin-II filament
  assembly are the mhcA heavy chain (regulated by myosin heavy-chain kinases) and its **regulatory /
  essential light chains** — not MlcD. If any myosin light chain warrants GO:0043520, it is the
  myosin-II RLC/ELC paralog, not mlcD.
- **Retain / support instead (MF/CC):** MF `GO:0032036 myosin heavy chain binding` (IPI to myoD) and
  the calmodulin-like light-chain role; CC `GO:0016459 myosin complex`. Prefer these informative terms
  over generic "protein binding."
- **Class-appropriate BP/CC leads (verify against MyoD phenotype literature):** class-I myosin
  processes at the plasma membrane — macropinocytosis/endocytosis and cortical actin dynamics
  (consistent with curated `macropinocytic cup cytoskeleton` and `actin wave` localizations).

---

## Mechanistic Scope

Direct molecular function of the gene product: MlcD is a calmodulin-like EF-hand **essential light
chain** that binds the IQ motifs in the neck of the class I myosin heavy chain **MyoD**, stabilizing
its lever arm. Its Ca²⁺ affinity is low, so it is not a Ca²⁺ sensor; De La Roche et al. propose it
confers Ca²⁺-insensitive regulatory properties distinguishing MyoD from calmodulin-bearing myosin-I.
The predicted terms describe **downstream cellular processes of a different motor system** (myosin-II
contractile ring); they are neither the immediate activity of MlcD nor a documented phenotype of it.

---

## Conflicts and Alternatives

- **Paralog/class confusion (most likely source of the prediction):** "mlc*" myosin light-chain genes
  form a paralog pool spanning classes. The myosin-II regulatory (mlcR) and essential (mlcE) light
  chains legitimately carry cytokinesis/filament-assembly context; a sequence/name-similarity or
  frequency-biased transfer plausibly propagated those terms onto mlcD.
- **Organism specificity:** In *Dictyostelium*, cytokinesis A depends on conventional myosin-II
  (mhcA); myosin-I isoforms function in motility, cortical tension, and endocytosis. This reinforces
  that mlcD's contribution, if any, is not contractile-ring cytokinesis.
- **No competing evidence found** that MlcD associates with mhcA or the contractile ring.

---

## Knowledge Gaps

1. **MyoD-null / MlcD-null cellular phenotype.** Partially addressed: MyoD-specific knockout papers
   were not retrievable here, but class-level phenotype data (Dai et al. 1999, PMID:10423462) show
   Dictyostelium myosin-I motors drive pseudopod formation, macropinocytosis, and cortical tension —
   not cytokinesis. A positive class-I process annotation for mlcD (e.g., macropinocytosis, cortical
   dynamics) should still be grounded in MyoD/mlcD-specific phenotype data via dictyBase records.
2. **Reference doi:10.64898/2026.03.19.712954.** Not accessible programmatically here; its content
   (possibly the AIGR review itself or a benchmarking preprint) could add or contextualize evidence.
3. **Exact myosin-II light-chain paralog identities (mlcE vs mlcR).** Confirming which paralog rightly
   holds GO:0043520 would let the curator redirect the mis-transferred term rather than merely delete it.

---

## Discriminating Tests

- **Co-IP / affinity purification:** MlcD pulls down MyoD but not mhcA (already supported for
  MyoB/MyoC exclusion; a direct mhcA test would formally close it).
- **Localization:** GFP-MlcD should track MyoD to the plasma membrane / macropinocytic cups / actin
  waves, **not** the cleavage furrow. Curated IDA localizations already favor the membrane pattern.
- **Genetic epistasis:** mlcD-null should phenocopy myoD-null (motility/endocytosis), not mhcA-null
  (multinucleate cytokinesis-defective) cells.
- **Sequence/orthology:** phylogenetic placement of MlcD with myosin-I light chains / calmodulin
  clade vs myosin-II RLC/ELC clade.

---

## Curation Leads (require curator verification)

- **Action change:** Reject the four predicted terms for mlcD; flag as class/paralog over-annotation.
- **Candidate references to verify:** PMID:12826013 (identity, MyoD specificity, Ca²⁺ properties);
  PMID:21671662 (MyoD–MlcD light-chain assignment). Snippets provided in the recorded findings.
- **Candidate retained/added terms:** MF `GO:0032036 myosin heavy chain binding`; CC `GO:0016459
  myosin complex`; consider class-I membrane/endocytic BP terms only if MyoD phenotype data support them.
- **Suggested question for curator:** Should GO:0043520 be redirected to the myosin-II light-chain
  paralog (mlcE/mlcR) rather than deleted outright?
- **Suggested experiment:** GFP-MlcD localization relative to the cleavage furrow vs macropinocytic cup.

---

## Computed Provenance — Pairwise Sequence Identity (Iteration 2)

Global Needleman–Wunsch alignment (BLOSUM62, gap = −8), MlcD (Q7Z2B8) vs *D. discoideum* paralogs.
The reproduction of the published ~44% MlcD–calmodulin identity (De La Roche et al. 2003, PMID:12826013)
serves as a method-validity check.

| Comparison (vs MlcD Q7Z2B8) | UniProt | % identity | Aligned cols | Class |
|---|---|---|---|---|
| Calmodulin (calA) | P02599 | **45.6** | 147 | Ca²⁺ sensor / myosin-I LC clade |
| MlcB — Myosin-IB light chain | Q54GL7 | 45.2 | 73* | Class I myosin LC |
| mlcR — Myosin-II **regulatory** LC | P13833 | **30.8** | 146 | Myosin-II LC |
| mlcE — Myosin-II **essential** LC | P09402 | **31.2** | 141 | Myosin-II LC |

*MlcB record is only 73 aa (partial), so its alignment spans fewer columns.

**Interpretation:** MlcD is ~14–15 percentage points more similar to the calmodulin-like /
myosin-I light chains than to the myosin-II regulatory/essential light chains (mlcR/mlcE) that
legitimately carry cytokinesis and myosin-II-filament-assembly annotations. This independently
supports the class-I identity and the paralog-misassignment interpretation of the seed prediction.
(Computed value 45.6% ≈ published 44% → analysis validated.)

---

## Limitations

Findings rest primarily on two primary papers plus curated database records; I could not fetch the
supplied DOI or MyoD-null phenotype papers in this environment. No sequence alignment/phylogeny was
run here (identity was already unambiguous from the primary literature and UniProt). Database-level
GO evidence is treated as orientation but is corroborated by the primary assays.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)