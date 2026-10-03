---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T05:07:39.944885'
end_time: '2026-09-21T05:28:56.440066'
duration_seconds: 1276.5
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: LPIN3
  gene_symbol: LPIN3
  uniprot_accession: Q9BQK8
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: transcriptional-and-metabolic-regulation
  hypothesis_text: Human LPIN3 (Q9BQK8) has transcription coactivator activity, promotes
    RNA polymerase II transcription, participates in fatty acid catabolism, or responds
    to insulin. Evaluate these independently from its established phosphatidate phosphatase
    activity. Compare lipin paralogs, relevant conserved binding interfaces, experimental
    gene identity and context, and the actual ancestral assignments. Distinguish a
    lack of LPIN3-specific testing from target-specific divergence or direct negative
    experiments.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/LPIN3/LPIN3-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human LPIN3 (Q9BQK8) has transcription coactivator\
    \ activity, promotes RNA polymerase II transcription,\n  participates in fatty\
    \ acid catabolism, or responds to insulin. Evaluate these independently from its\n\
    \  established phosphatidate phosphatase activity. Compare lipin paralogs, relevant\
    \ conserved binding interfaces,\n  experimental gene identity and context, and\
    \ the actual ancestral assignments. Distinguish a lack of\n  LPIN3-specific testing\
    \ from target-specific divergence or direct negative experiments.\nfocus_type:\
    \ function_assignment\ncontext: []\nreference_id: []"
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

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** LPIN3
- **Gene symbol:** LPIN3
- **UniProt accession:** Q9BQK8

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** transcriptional-and-metabolic-regulation
- **Source file:** genes/human/LPIN3/LPIN3-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human LPIN3 (Q9BQK8) has transcription coactivator activity, promotes RNA polymerase II transcription, participates in fatty acid catabolism, or responds to insulin. Evaluate these independently from its established phosphatidate phosphatase activity. Compare lipin paralogs, relevant conserved binding interfaces, experimental gene identity and context, and the actual ancestral assignments. Distinguish a lack of LPIN3-specific testing from target-specific divergence or direct negative experiments.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human LPIN3 (Q9BQK8) has transcription coactivator activity, promotes RNA polymerase II transcription,
  participates in fatty acid catabolism, or responds to insulin. Evaluate these independently from its
  established phosphatidate phosphatase activity. Compare lipin paralogs, relevant conserved binding interfaces,
  experimental gene identity and context, and the actual ancestral assignments. Distinguish a lack of
  LPIN3-specific testing from target-specific divergence or direct negative experiments.
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

# LPIN3 (Q9BQK8) — Transcriptional & Metabolic Regulation Hypothesis

**Focus:** function_assignment · **Hypothesis slug:** transcriptional-and-metabolic-regulation
**Gene:** human LPIN3 / lipin-3 · **UniProt:** Q9BQK8 · **Taxon:** Homo sapiens (NCBITaxon:9606)

---

## Summary

The seed hypothesis proposes that human LPIN3 (Q9BQK8) directly possesses **transcription coactivator activity** (GO:0003713), **positively regulates RNA polymerase II transcription** (GO:0045944), **participates in fatty acid catabolism** (GO:0009062), and **responds to insulin** (GO:0032869), independent of its established phosphatidate phosphatase (PAP) activity. After three iterations of annotation-provenance analysis, comparative paralog sequence analysis, and targeted literature review, the verdict is **over-annotated / partially refuted**: every one of these four functions rests **solely on phylogenetic-ancestor inference (IBA, ECO:0000318, GO_Central, GO_REF:0000033)** with **no LPIN3-specific experimental support**. They are uniform PANTHER family-node (PAINT) propagations whose experimental anchor is the **mouse Lpin1 ortholog** — not any human lipin, and certainly not LPIN3.

The coactivator branch is not merely untested; it is contradicted by target-specific data. Lipin-1's nuclear coactivator function is mechanistically gated by **sumoylation-dependent nuclear import**, and Liu & Gerace (2009, PMID 19753306) explicitly report they were *"unable to detect sumoylation of the related proteins lipin-2 and lipin-3."* Our own computational scan corroborates this at the motif level: LPIN3 encodes **zero canonical SUMO consensus motifs** versus 3 in LPIN1 and 4 in LPIN2. LPIN3 retains the polybasic nuclear-localization signal and the catalytic DxDxT PAP motif, so the *catalytic core* is conserved while the *nuclear-coactivator apparatus* has diverged. Consistently, the only direct-assay localization for LPIN3 places it in the **cytosol (IDA, Human Protein Atlas)** and **ER membrane (TAS, Reactome)** — not the nucleus.

For a curator, the recommended reading is: LPIN3's experimentally grounded, core molecular function is **Mg²⁺-dependent phosphatidate phosphatase activity (GO:0008195)** feeding **triacylglycerol/glycerolipid biosynthesis (GO:0019432)** at the cytosol/ER. The transcriptional-coactivator, RNA-Pol-II, fatty-acid-catabolism, and insulin-response terms should be treated as **non-core, ancestral carry-over**, flagged with the IBA/homology caveat, and — for the coactivator and nucleus terms specifically — considered candidates for removal or NOT/uncertain qualification given the direct sumoylation-negative and cytosolic localization evidence.

---

## Executive Judgment

**Verdict: Over-annotated (weakly supported by homology only; partially refuted by direct data).**

Two tiers of confidence must be distinguished, because the seed hypothesis explicitly asks us to separate a *lack of LPIN3-specific testing* from *target-specific divergence or direct negative experiments*:

1. **Coactivator / nuclear branch (GO:0003713, GO:0045944, nuclear component) — evidence of divergence.** Here we have a **direct negative result** (no lipin-3 sumoylation, PMID 19753306) plus an independent computational corroboration (zero SUMO acceptor motifs). This is stronger than "untested" — the mechanism required for the ancestral function appears actively lost in lipin-3. Recommendation strength: **high** for treating as non-core / candidate removal.

2. **Metabolic-input branch (GO:0009062 fatty acid catabolism, GO:0032869 insulin response) — absence of LPIN3 evidence.** These are downstream/regulatory processes characterized for lipin-1 (insulin→14-3-3 mechanism; PPARα/PGC-1α amplifier loop) with no direct LPIN3 test. Recommendation strength: **moderate** — flag as non-core and LPIN3-untested rather than asserting a definitive negative.

The most important caveats: (a) the SUMO-motif scan is consensus-pattern based, not empirical PTM mapping — and note LPIN2 *has* SUMO motifs yet is also unsumoylated, so motif presence/absence is suggestive, not decisive; (b) "absence of a nuclear coactivation assay on LPIN3 itself" remains a genuine gap; the PMID 19753306 negative is on the modification, not on a lipin-3 coactivation assay directly.

---

## Key Findings

### Finding 1 — All four seed-hypothesis functions are IBA-only for LPIN3, not experimental

A direct QuickGO annotation pull for Q9BQK8 returned 12 annotations. Every one of the four seed-hypothesis functions is supported **solely by phylogenetic-ancestor inference (IBA; ECO:0000318; GO_Central; GO_REF:0000033)**, while LPIN3's only direct experimental annotations point to cytosol/ER localization and (via ISS) to phosphatidate phosphatase activity:

| GO term | Aspect | Description | LPIN3 evidence |
|---|---|---|---|
| GO:0003713 | MF | transcription coactivator activity | **IBA only** |
| GO:0045944 | BP | positive regulation of transcription by RNA Pol II | **IBA only** |
| GO:0009062 | BP | fatty acid catabolic process | **IBA only** |
| GO:0032869 | BP | cellular response to insulin stimulus | **IBA only** |
| GO:0005634 | CC | nucleus | IBA + IEA (ECO:0007322) |
| GO:0008195 | MF | phosphatidate phosphatase activity | **ISS + IBA + IEA** |
| GO:0019432 | BP | triglyceride biosynthetic process | IBA |
| GO:0005829 | CC | cytosol | **IDA (HPA)** |
| GO:0005789 | CC | endoplasmic reticulum membrane | **TAS (Reactome)** |

The contrast is the crux: LPIN3's direct (IDA/TAS) and ISS evidence supports the *enzymatic/metabolic* picture, whereas the four seed functions carry only the ancestral IBA code — the signature of family-level propagation rather than gene-specific characterization.

### Finding 2 — Lipin-1's nuclear coactivator mechanism (sumoylation) is directly absent in lipin-3

Lipin-1's coactivator function is mechanistically dependent on sumoylation. Liu & Gerace (2009, [PMID: 19753306](https://pubmed.ncbi.nlm.nih.gov/19753306/)) showed lipin-1 is sumoylated at two consensus sites, that this facilitates nuclear localization, and that a **sumoylation-site mutant loses the capacity to coactivate PGC-1α and MEF2** ("consistent with its nuclear exclusion"). In the same study the authors state: *"We are unable to detect sumoylation of the related proteins lipin-2 and lipin-3."* This is a **direct negative result** on the exact modification that enables the coactivator function being propagated to lipin-3.

Independently, insulin regulation of lipin-1's localization is mediated by 14-3-3 binding to a serine-rich domain (Péterfy et al. 2010, [PMID: 19955570](https://pubmed.ncbi.nlm.nih.gov/19955570/)) — again a lipin-1-characterized mechanism. A sequence scan confirmed the catalytic **DxDxT PAP motif is conserved in all three human lipins** (LPIN1 @677, LPIN2 @688, LPIN3 @643), consistent with shared phosphatase activity but not with a shared nuclear-coactivator apparatus. The paralogs share the *enzyme*, not the *transcriptional machinery*.

### Finding 3 — LPIN3 lacks any canonical SUMO consensus motif, corroborating loss of the coactivator-enabling PTM code

Computed pairwise Needleman-Wunsch global alignments showed moderate identity across the family (LPIN1–LPIN3 = 50.0%, LPIN2–LPIN3 = 51.5%, LPIN1–LPIN2 = 52.0%; roughly half the protein diverged). A scan for the canonical SUMO consensus motif [VILMFP]KxE found:

| Paralog | SUMO consensus sites | Polybasic NLS | N-terminal Ser density |
|---|---|---|---|
| LPIN1 | 3 (I564, V594, P823) | retained | 13.2% |
| LPIN2 | 4 | retained | 11.2% |
| **LPIN3** | **0** | **retained (RRKR@138, RRRRKPK@145)** | 10.3% |

LPIN3 retains the polybasic NLS — so nuclear entry is not structurally precluded — but has **lost every canonical SUMO acceptor motif**, providing an independent computational line consistent with the direct wet-lab negative in Finding 2. Caveat: this is a consensus-motif scan (LPIN2 has motifs but is empirically unsumoylated), so it is supportive inference rather than proof.

### Finding 4 — Ancestral (IBA) terms are propagated identically to all human lipins; the experimental anchor is mouse Lpin1

A QuickGO comparison of the four seed terms between human LPIN3 (Q9BQK8) and human LPIN1 (Q14693) showed that **human LPIN1 carries the same evidence tiers as LPIN3**: coactivator (GO:0003713) = IBA-only, RNA Pol II (GO:0045944) = IBA-only, FA catabolism (GO:0009062) = ISS+IBA, insulin response (GO:0032869) = IBA+IEA(Ensembl), nucleus (GO:0005634) = IBA+ISS. **Neither human paralog has an IDA/EXP annotation for the coactivator or RNA Pol II terms.** The primary experimental coactivator evidence — Finck et al. 2006 ([PMID: 16950137](https://pubmed.ncbi.nlm.nih.gov/16950137/)) and Liu & Gerace 2009 ([PMID: 19753306](https://pubmed.ncbi.nlm.nih.gov/19753306/)) — was generated on the **mouse Lpin1 ortholog**. The IBA propagation (GO_REF:0000033, PAINT) applies the term uniformly across the PANTHER lipin family node, which is exactly why the same terms decorate LPIN3 with the same non-experimental evidence code. This is the mechanism of over-annotation: a mouse Lpin1 phenotype seeds a family-node ancestral annotation that propagates to every descendant, including LPIN3.

---

## Mechanistic Model / Interpretation

```
                        LIPIN FAMILY (PANTHER node)
                                  |
        experimental anchor: MOUSE Lpin1 (Finck 2006; Liu 2009)
                                  |
              IBA propagation (GO_REF:0000033, PAINT)
                                  |
        +-------------------------+-------------------------+
        v                         v                         v
   human LPIN1               human LPIN2               human LPIN3 (Q9BQK8) <-- TARGET
   (Q14693)                                                 |
        |                                                   |
   coactivator = IBA         coactivator = IBA         coactivator = IBA
   RNAPolII    = IBA                                   RNAPolII    = IBA
   FA catab.   = ISS+IBA                               FA catab.   = IBA
   insulin     = IBA+IEA                               insulin     = IBA
        |                                                   |
   3 SUMO motifs                                       0 SUMO motifs
   (mouse ortholog sumoylated)                         NOT sumoylated (direct, PMID 19753306)
        |                                                   |
   NUCLEAR coactivation                                NLS retained BUT no SUMO code
   of PGC-1a / MEF2                                          |
                                                            v
                                          DIRECT evidence for LPIN3:
                                          - PAP activity (DxDxT @643; ISS)
                                          - cytosol (IDA, HPA)
                                          - ER membrane (TAS, Reactome)
                                          - triglyceride biosynthesis (IBA)
```

The lipin family shares a conserved bifunctional architecture but has diverged in its regulatory couplings. The demonstrable, core function of LPIN3 is **Mg²⁺-dependent phosphatidate phosphatase activity** acting in **glycerolipid/triacylglycerol synthesis** at the **cytosol/ER**. The transcriptional and insulin-signaling roles are **lipin-1-specialized elaborations** built on post-translational machinery (sumoylation, 14-3-3 phospho-binding) that lipin-3 does not share. Annotating LPIN3 with the coactivator/RNA-Pol-II/insulin/FA-catabolism terms conflates the shared catalytic core with paralog-specific regulatory functions.

---

## Evidence Base

| # | Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| 1 | QuickGO pull Q9BQK8 (this run) | database/computational | qualifies/refutes | Are the four functions LPIN3-experimental? | Coactivator, +reg RNA Pol II, FA catabolism, insulin response, and nucleus are **IBA-only** (+IEA for nucleus); PAP is ISS+IBA+IEA; cytosol **IDA (HPA)**; ER membrane TAS | Human, UniProt/GO_Central | High for provenance; IBA = inference not assay |
| 2 | Liu & Gerace 2009, [PMID 19753306](https://pubmed.ncbi.nlm.nih.gov/19753306/) | direct assay (biochemical) | refutes/qualifies | Does lipin-3 share lipin-1's nuclear-coactivator mechanism? | Sumoylation drives lipin-1α nuclear localization + coactivation of PGC-1α/MEF2; **"unable to detect sumoylation of ... lipin-2 and lipin-3."** | Neuronal cells, in vitro | Direct negative for lipin-3; absence-of-modification, not a coactivation assay on lipin-3 |
| 3 | Finck et al. 2006, [PMID 16950137](https://pubmed.ncbi.nlm.nih.gov/16950137/) | direct assay + interaction | competing (paralog source) | Origin of the coactivator annotation | **Lipin-1** interacts with PPARα/PGC-1α and amplifies the FA-oxidation gene program | Mouse liver | Establishes function for LPIN1, not LPIN3 — source of ancestral term |
| 4 | Péterfy et al. 2010, [PMID 19955570](https://pubmed.ncbi.nlm.nih.gov/19955570/) | direct assay | competing (paralog source) | Origin of the insulin-response annotation | Insulin → lipin-1 phosphorylation → 14-3-3 binding → cytoplasmic retention | 3T3-L1 adipocytes | Lipin-1-specific mechanism; no lipin-3 data |
| 5 | Temprano et al. 2016, [PMID 27344312](https://pubmed.ncbi.nlm.nih.gov/27344312/) | mutant phenotype (siRNA) | supports (core PAP function) | Is LPIN3 a functional PAP in humans? | All three lipins contribute to PAP1/adipogenic gene regulation; lipin-1 ~95% of adipocyte PAP1; redundant TAG synthesis | Human SGBS adipocytes | Supports PAP/TAG role; LPIN3 contribution modest/redundant |
| 6 | Boroda et al. 2017, [PMID 28982975](https://pubmed.ncbi.nlm.nih.gov/28982975/) | structural/biochemical | qualifies | Are lipin-1/lipin-3 regulatory interfaces identical? | Phosphatidic-acid-binding polybasic domain underlies **differences** in phosphoregulation between lipins 1 and 3 | In vitro | Shows paralog divergence in regulatory interfaces |
| 7 | Sequence scan (this run) | computational | qualifies | Is the catalytic core conserved? | DxDxT PAP motif conserved in all three lipins (LPIN1@677, LPIN2@688, LPIN3@643) | Human UniProt seqs | Supports shared *catalytic* function only |
| 8 | Paralog alignment (this run) | computational/evolutionary | qualifies/refutes | Does LPIN3 retain coactivator-enabling motifs? | LPIN3 = **0** SUMO consensus motifs vs 3 (LPIN1) / 4 (LPIN2); NLS retained; LPIN1–LPIN3 identity 50.0% | Human UniProt seqs | Corroborates PMID 19753306; motif≠modification (LPIN2 has motifs yet unsumoylated) |
| 9 | QuickGO LPIN1 vs LPIN3 (this run) | database | qualifies | Is the coactivator term human-experimental for any lipin? | Human **LPIN1 also IBA-only** for coactivator/RNA Pol II; no human lipin has IDA/EXP; anchor is mouse Lpin1 | Human vs mouse | Uniform PAINT family propagation across species |
| 10 | [PMID 40042548](https://pubmed.ncbi.nlm.nih.gov/40042548/) | expression/phenotype | competing (disease context) | Does LPIN3 have a transcriptional role in cancer? | LPIN3 promotes CRC growth via β-catenin signaling, dampens CD8⁺ immunity | Human CRC, TCGA | Disease-context downstream phenotype, not coactivator MF evidence |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current LPIN3 evidence | Lead recommendation |
|---------|--------|------------------------|---------------------|
| GO:0003713 transcription coactivator activity | MF | IBA only; sumoylation absent (PMID 19753306) | **Do not treat as core.** Remove or mark NOT/uncertain for LPIN3; retain only as ancestral-homology note. |
| GO:0045944 positive regulation of transcription by RNA Pol II | BP | IBA only | **Non-core / remove.** No direct or ISS evidence. |
| GO:0009062 fatty acid catabolic process | BP | IBA only | **Non-core, LPIN3-untested.** Downstream consequence of lipin-1 coactivation, not a lipin-3 activity. |
| GO:0032869 cellular response to insulin stimulus | BP | IBA only | **Non-core, LPIN3-untested.** Lipin-1-specific 14-3-3 mechanism. |
| GO:0005634 nucleus | CC | IBA + IEA; contradicted by IDA cytosol | **Weaken/flag.** Direct evidence favors cytosol/ER; retain nucleus only with caveat. |
| GO:0008195 phosphatidate phosphatase activity | MF | ISS + IBA + IEA; motif conserved; functional data (PMID 27344312) | **Retain — core molecular function.** |
| GO:0019432 triglyceride biosynthetic process | BP | IBA; supported by adipocyte data | **Retain as core BP.** |
| GO:0005789 ER membrane / GO:0005829 cytosol | CC | TAS / IDA | **Retain — direct/traceable; primary location.** |

Avoiding "protein binding" as a recommendation: the informative supported MF is **phosphatidate phosphatase activity (GO:0008195)**.

---

## Mechanistic Scope

- **Direct gene-product activity (supported):** Mg²⁺-dependent phosphatidate phosphatase converting phosphatidate → diacylglycerol at the ER membrane, feeding glycerolipid/TAG synthesis; catalyzed by the conserved HAD-like DxDxT motif (LPIN3 @643).
- **Direct gene-product activity (contested for LPIN3):** transcription coactivator activity — a nuclear protein-bridging function requiring sumoylation-gated import in lipin-1. LPIN3 lacks the SUMO code.
- **Downstream/pathway (lipin-1-derived, not LPIN3 activity):** "fatty acid catabolism," "positive regulation of RNA Pol II transcription," and "cellular response to insulin" are physiological/regulatory outcomes of lipin-1 acting as a PGC-1α/PPARα coactivator and as a 14-3-3-regulated protein. For LPIN3 these are inferred network-level consequences, not demonstrated molecular functions.

---

## Conflicts and Alternatives

- **Paralog carry-over (primary alternative):** The four hypothesis functions originate from lipin-1 experiments (PMID 16950137, 19955570, 19753306) and are propagated across the clade by IBA. Even human LPIN1 carries these terms as IBA/ISS-only (no human IDA/EXP); the experimental grounding is the *mouse* Lpin1 ortholog, and PAINT propagates uniformly to LPIN1/LPIN2/LPIN3. LPIN3's coactivator annotation is therefore exactly as weak as human LPIN1's — a cross-species family inference, not a human-lipin experimental result.
- **Direct divergence, not just untested:** PMID 19753306 provides an explicit negative (no lipin-3 sumoylation), and PMID 28982975 shows the lipin-1 vs lipin-3 regulatory interface differs — target-specific divergence, stronger than "merely not tested."
- **Localization conflict:** IBA/IEA "nucleus" vs IDA "cytosol" (HPA) for LPIN3.
- **Cancer context (not core):** PMID 40042548 links LPIN3 to β-catenin signaling in colorectal cancer — a disease-context phenotype, not evidence for general transcriptional coactivator activity.
- **Redundancy caveat:** Human lipins are functionally redundant in adipocyte TAG synthesis (PMID 27344312), arguing the transcriptional/FA-oxidation program is not cleanly attributable to any single lipin, least of all LPIN3.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No direct LPIN3 coactivation assay | QuickGO (no IDA); literature | Only way to confirm/exclude the coactivator MF | Mammalian two-hybrid/luciferase coactivation assay (LPIN3 + PGC-1α/PPARα) + co-IP |
| SUMO-motif scan is consensus-based | [VILMFP]KxE regex scan | Non-consensus SUMO sites exist; LPIN2 has motifs yet is unsumoylated | LPIN3 SUMO-site mass spectrometry / mutant IP |
| No LPIN3 insulin-response experiment | Literature (all lipin-1) | GO:0032869 unsupported for LPIN3, not directly refuted | Insulin stimulation + LPIN3 phospho/localization time course |
| FA-catabolism attribution | IBA only; no LPIN3 KO flux | Cannot distinguish absent from untested | LPIN3 KO/KD β-oxidation flux + PPARα-target expression |
| 14-3-3 phosphosite conservation | Ser density only (similar) | Determines whether the insulin mechanism could transfer | Map exact lipin-1 14-3-3 phosphosites across paralogs |
| Human LPIN3 nuclear presence/function | IEA nucleus + retained NLS | Nuclear entry plausible; function unknown | Endogenous LPIN3 fractionation/imaging in relevant tissue |

### Paralog Comparison (computed provenance)

| Feature | LPIN1 (Q14693) | LPIN2 (Q92539) | LPIN3 (Q9BQK8) | Interpretation |
|---------|----------------|----------------|----------------|----------------|
| Global % identity to LPIN3 (NW) | 50.0% | 51.5% | — | Moderate divergence; ~half the protein differs |
| DxDxT catalytic PAP motif | @677 | @688 | @643 (present) | Shared catalytic core → shared PAP activity |
| Polybasic NLS (≥4 K/R in 7 aa) | present | present | @138/@145 (present) | Nuclear-import signal retained in all three |
| SUMO consensus [VILMFP]KxE | 3 sites | 4 sites | **0 sites** | LPIN3 lacks SUMO acceptor motifs; corroborates PMID 19753306 |
| N-terminal Ser density | 13.2% | 11.2% | 10.3% | Broadly similar; not a discriminator alone |

---

## Proposed Follow-up Experiments / Actions

**Discriminating tests (most efficient first):**

1. **Coactivation reporter assay:** LPIN3 vs LPIN1 (and a sumoylation-dead LPIN1 control) on a PPARα/PGC-1α-driven luciferase reporter — directly separates homology inference from real activity. Prediction: LPIN3 ≈ sumo-dead LPIN1 (no coactivation) if over-annotated.
2. **Empirical SUMO-site mapping:** SUMO-IP + MS on LPIN3 vs LPIN1 in the same cell line, converting the motif inference into a measurement (and confirming PMID 19753306 in a second system).
3. **Insulin-stimulated 14-3-3 co-IP** and cyto/nuclear partitioning with LPIN3 vs LPIN1; LPIN3's divergent polybasic domain (PMID 28982975) predicts a different response.
4. **LPIN3-specific metabolic flux:** CRISPR LPIN3 KO in an LPIN3-expressing tissue; measure β-oxidation flux and PPARα-target transcript panel to test the FA-catabolism term.
5. **Phylogenetic re-analysis:** Re-examine the PANTHER family-node PAINT annotations to determine whether the ancestral coactivator assignment should be restricted to the Lpin1 subclade rather than propagated to the Lpin3 branch.

**Curation actions (leads):**

- Reclassify GO:0003713, GO:0045944, GO:0009062, GO:0032869 (and weaken GO:0005634) for LPIN3 as **non-core / ancestral-inference-only**; consider NOT/uncertain qualifiers on the coactivator and nucleus terms given the sumoylation negative and cytosolic IDA.
- Retain as core: GO:0008195 (PAP, MF), GO:0019432 (TAG biosynthesis, BP), GO:0005789 (ER membrane, CC), GO:0005829 (cytosol, CC).
- Candidate references + snippets to verify:
  - PMID **19753306** — *"We are unable to detect sumoylation of the related proteins lipin-2 and lipin-3."*
  - PMID **19753306** — *"The sumoylation site mutant of lipin-1alpha loses the capacity to coactivate the transcriptional (co-) activators PGC-1alpha and MEF2, consistent with its nuclear exclusion."*
  - PMID **16950137** — lipin-1 (not lipin-3) is the amplifier of PGC-1α/PPARα (source of the ancestral coactivator term).
  - PMID **27344312** — supports LPIN3's PAP/TAG role in human adipocytes (core function).
- Questions for curator: Was the IBA propagation intended to assert an equivalent function in LPIN3, or only clade membership? Should the nucleus CC be demoted given the HPA cytosol IDA?

---

### Provenance

- **GO annotation pull:** QuickGO REST (`/annotation/search?geneProductId=Q9BQK8`), 12 annotations, evidence codes tabulated above.
- **Sequence scan:** UniProt FASTA for Q14693/Q92539/Q9BQK8; DxDxT catalytic motif conserved in all three (positions 677/688/643).
- **Paralog alignment (Needleman-Wunsch, this run):** global identity LPIN1–LPIN3 50.0%, LPIN2–LPIN3 51.5%, LPIN1–LPIN2 52.0%; SUMO consensus [VILMFP]KxE counts 3/4/0 for LPIN1/LPIN2/LPIN3; polybasic NLS retained in all three; N-terminal Ser density 13.2/11.2/10.3%.
- **LPIN1 vs LPIN3 GO evidence compare (this run):** for all four seed terms human LPIN1 and LPIN3 share IBA(±ISS/IEA) tiers only; no human lipin has IDA/EXP for coactivator (GO:0003713) or RNA Pol II (GO:0045944); experimental basis is mouse Lpin1.

*Motif scans are consensus-pattern based and should be treated as supportive computational inference rather than empirical PTM mapping. Where a resource could not be queried programmatically it is stated plainly rather than fabricated.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)