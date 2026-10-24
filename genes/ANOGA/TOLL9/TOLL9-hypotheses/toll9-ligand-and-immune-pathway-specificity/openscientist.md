---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T01:52:14.716646'
end_time: '2026-09-21T02:12:30.270212'
duration_seconds: 1215.55
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: ANOGA
  gene: TOLL9
  gene_symbol: TOLL9
  uniprot_accession: Q5TWL7
  taxon_id: NCBITaxon:7165
  taxon_label: Anopheles gambiae
  focus_type: function_assignment
  hypothesis_slug: toll9-ligand-and-immune-pathway-specificity
  hypothesis_text: Anopheles gambiae TOLL9 (Q5TWL7/AGAP006974) has pattern-recognition
    receptor activity and participates in innate immunity through the Toll signaling
    pathway. Assess actual target phylogeny and transfer scope, ligand and accessory/downstream
    partners. Current target leaf PTN000688561 in PTHR24365 descends from PTN002808045
    supporting generic receptor/signaling/plasma membrane. PMID33963082 establishes
    Bombyx Toll9 LPS recognition with MD-2-like partners, including a chimera whose
    TM/TIR regions are mouse TLR4; distinguish those experiments. PMID21386906 reports
    Drosophila Toll9 knockout without basal or inducible antibacterial AMP defects
    under tested conditions, while acknowledging overexpression-induced signaling.
    PMID38191283 reports AGAP006974 induction after mosGILT disruption, not target
    perturbation. Determine whether conservation supports PRR/Toll immune roles or
    target divergence changes them; a small experimental donor set alone is not weak
    evidence. Do not assume every insect Toll uses Spaetzle, or confuse recognition
    of processed host cytokine with GO0038187 microbial PAMP recognition. The separate
    inflammatory-response row is already resolved by explicit GO0006954 vertebrate-only
    constraint and is not this question.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/ANOGA/TOLL9/TOLL9-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Anopheles gambiae TOLL9 (Q5TWL7/AGAP006974) has\
    \ pattern-recognition receptor activity and\n  participates in innate immunity\
    \ through the Toll signaling pathway. Assess actual target phylogeny and\n  transfer\
    \ scope, ligand and accessory/downstream partners. Current target leaf PTN000688561\
    \ in PTHR24365\n  descends from PTN002808045 supporting generic receptor/signaling/plasma\
    \ membrane. PMID33963082 establishes\n  Bombyx Toll9 LPS recognition with MD-2-like\
    \ partners, including a chimera whose TM/TIR regions are mouse\n  TLR4; distinguish\
    \ those experiments. PMID21386906 reports Drosophila Toll9 knockout without basal\
    \ or\n  inducible antibacterial AMP defects under tested conditions, while acknowledging\
    \ overexpression-induced\n  signaling. PMID38191283 reports AGAP006974 induction\
    \ after mosGILT disruption, not target perturbation.\n  Determine whether conservation\
    \ supports PRR/Toll immune roles or target divergence changes them; a small\n\
    \  experimental donor set alone is not weak evidence. Do not assume every insect\
    \ Toll uses Spaetzle, or\n  confuse recognition of processed host cytokine with\
    \ GO0038187 microbial PAMP recognition. The separate\n  inflammatory-response\
    \ row is already resolved by explicit GO0006954 vertebrate-only constraint and\
    \ is\n  not this question.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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
citation_count: 5
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: artifact_evidence_matrix.csv
  path: openscientist_artifacts/artifact_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist artifact evidence matrix
- filename: artifact_go_decision_table.csv
  path: openscientist_artifacts/artifact_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist artifact go decision table
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

- **Organism code:** ANOGA
- **Taxon:** Anopheles gambiae (NCBITaxon:7165)
- **Gene directory:** TOLL9
- **Gene symbol:** TOLL9
- **UniProt accession:** Q5TWL7

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** toll9-ligand-and-immune-pathway-specificity
- **Source file:** genes/ANOGA/TOLL9/TOLL9-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Anopheles gambiae TOLL9 (Q5TWL7/AGAP006974) has pattern-recognition receptor activity and participates in innate immunity through the Toll signaling pathway. Assess actual target phylogeny and transfer scope, ligand and accessory/downstream partners. Current target leaf PTN000688561 in PTHR24365 descends from PTN002808045 supporting generic receptor/signaling/plasma membrane. PMID33963082 establishes Bombyx Toll9 LPS recognition with MD-2-like partners, including a chimera whose TM/TIR regions are mouse TLR4; distinguish those experiments. PMID21386906 reports Drosophila Toll9 knockout without basal or inducible antibacterial AMP defects under tested conditions, while acknowledging overexpression-induced signaling. PMID38191283 reports AGAP006974 induction after mosGILT disruption, not target perturbation. Determine whether conservation supports PRR/Toll immune roles or target divergence changes them; a small experimental donor set alone is not weak evidence. Do not assume every insect Toll uses Spaetzle, or confuse recognition of processed host cytokine with GO0038187 microbial PAMP recognition. The separate inflammatory-response row is already resolved by explicit GO0006954 vertebrate-only constraint and is not this question.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Anopheles gambiae TOLL9 (Q5TWL7/AGAP006974) has pattern-recognition receptor activity and
  participates in innate immunity through the Toll signaling pathway. Assess actual target phylogeny and
  transfer scope, ligand and accessory/downstream partners. Current target leaf PTN000688561 in PTHR24365
  descends from PTN002808045 supporting generic receptor/signaling/plasma membrane. PMID33963082 establishes
  Bombyx Toll9 LPS recognition with MD-2-like partners, including a chimera whose TM/TIR regions are mouse
  TLR4; distinguish those experiments. PMID21386906 reports Drosophila Toll9 knockout without basal or
  inducible antibacterial AMP defects under tested conditions, while acknowledging overexpression-induced
  signaling. PMID38191283 reports AGAP006974 induction after mosGILT disruption, not target perturbation.
  Determine whether conservation supports PRR/Toll immune roles or target divergence changes them; a small
  experimental donor set alone is not weak evidence. Do not assume every insect Toll uses Spaetzle, or
  confuse recognition of processed host cytokine with GO0038187 microbial PAMP recognition. The separate
  inflammatory-response row is already resolved by explicit GO0006954 vertebrate-only constraint and is
  not this question.
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

# TOLL9 (Q5TWL7, AGAP006974) — Ligand and Immune-Pathway Specificity: Final Curation Report

**Target gene:** *Anopheles gambiae* TOLL9 (UniProt Q5TWL7 / AGAP006974)
**Focus:** function_assignment — `toll9-ligand-and-immune-pathway-specificity`
**Source:** `genes/ANOGA/TOLL9/TOLL9-ai-review.yaml`

---

## Executive Judgment

**Verdict: Partially supported / the strong claim is over-annotated as a direct function assignment.**

The seed hypothesis proposes that *A. gambiae* TOLL9 (1) **has pattern-recognition receptor (PRR) activity** and (2) **participates in innate immunity through the Toll signaling pathway**. After three iterations of orthology, domain-architecture, partner-availability, and literature analysis, the defensible position is nuanced:

- **What is supported (retain):** TOLL9 is a canonical Toll/TLR-family transmembrane receptor. Its generic, phylogeny-transferred annotations — **signaling receptor activity (GO:0038023, MF)**, **signal transduction (GO:0007165, BP)**, and **plasma membrane (GO:0005886, CC)** — are consistent with its domain architecture (LRR ectodomain + two TM helices + cytoplasmic TIR) and with the ancestral scope of PANTHER family PTHR24365. These should be retained.

- **What is NOT supported as a direct function assignment (flag as leads, do not assert):** The specific claims that TOLL9 **directly has PRR activity (GO:0038187)** and functions as an **innate-immune Toll-signaling receptor** are biologically plausible but **experimentally unproven in *Anopheles gambiae***. The only direct PRR/LPS evidence comes from the more distant lepidopteran *Bombyx mori*, and even there the downstream signaling was demonstrated using a **chimeric receptor whose transmembrane and TIR regions are mouse TLR4** — so the native insect signaling readout was never shown. The closest genetic test, a *Drosophila* Toll-9 loss-of-function mutant (~36% identical to the target), shows **no antibacterial defect**. The *Anopheles* mosGILT data are **correlative expression changes, not a perturbation of TOLL9 itself**.

**Most important caveat:** A "small experimental donor set" is not automatically weak evidence — but in this case the donor evidence is both **single-species** and **mechanistically partial** (chimeric TM/TIR), and the closest ortholog contradicts a required antibacterial role. That combination is exactly what should prevent a species-level MF PRR assignment while leaving the immune hypothesis open as a curator lead.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| UniProt Q5TWL7 (database) | Computational / database | Qualifies | What is currently annotated and by what evidence | Protein existence "Inferred from homology" (level 3). All four GO terms are **IBA** (phylogenetic, GO_Central): GO:0005886, GO:0038023, GO:0007165, GO:0006954. **No** GO:0038187 (PRR) or Toll-signaling/defense BP term is transferred. | *A. gambiae*, full proteome record | High for the annotation state; no experimental evidence for this protein |
| Domain analysis (this work) | Structural / computational | Supports (generic) | Is TOLL9 a canonical Toll/TLR receptor | LRR ectodomain (Pfam PF13855 LRR_8 ×2; SMART LRR_TYP ×7) + two TM helices (aa 29–49, 607–631) + cytoplasmic TIR (aa 667–807; PF01582; PROSITE PS50104). Family PTHR24365 ("TOLL-LIKE RECEPTOR 1"), subfamily SF530. | Sequence-derived | High for architecture; architecture alone does not specify ligand or PRR activity |
| [PMID: 33963082](https://pubmed.ncbi.nlm.nih.gov/33963082/) | Direct assay (heterologous/chimeric) | Qualifies / partial support | Does insect Toll9 recognize LPS via MD-2-like partners | BmToll9 recognizes **LPS** through two **MD-2-like** partners (BmMD-2A/B). Signaling competence shown with a **chimera = BmToll9 ectodomain + mouse TLR4 TM + TIR**, activating LPS-induced inflammatory-factor release in **murine cells** only with BmMD-2A/B present. | *Bombyx mori* ectodomain; murine cell readout | Medium; native insect TM/TIR and an insect signaling readout were NOT demonstrated; single donor species |
| [PMID: 21386906](https://pubmed.ncbi.nlm.nih.gov/21386906/) | Mutant phenotype (loss-of-function) | Refutes (required immune role) | Is Toll-9 required for antibacterial defense | Complete *Drosophila* Toll-9 LOF allele shows **no defect** in basal or infection-induced antibacterial (AMP) response; authors acknowledge overexpression-induced signaling. | *D. melanogaster*, whole animal | High for the tested conditions; does not exclude context-specific or non-AMP roles |
| [PMID: 38191283](https://pubmed.ncbi.nlm.nih.gov/38191283/) | Expression correlation (RNA-seq) | Qualifies (weak) | Is AGAP006974 immune-regulated in mosquito | AGAP006974 is **induced** in mosGILT^null *A. gambiae*; co-regulation of immune genes. | *A. gambiae*, transcriptome | Low for causation; TOLL9 itself was not perturbed; correlation only |
| [PMID: 35238667](https://pubmed.ncbi.nlm.nih.gov/35238667/) | Review-level | Qualifies | Is the Toll9/MD-2/LPS property established | States Toll9/MD-2-like complex in silkworm acts as PRR recognizing LPS. | Review | Medium; reiterates the single-species *Bombyx* finding |
| [PMID: 25573502](https://pubmed.ncbi.nlm.nih.gov/25573502/) | Expression/RNAi (paralog/related clade) | Competing / context | Do Toll9-clade receptors regulate AMPs elsewhere | Crayfish PcToll (clusters with *Drosophila*/*Anopheles* Toll9 and human Tolls) is bacteria-inducible; RNAi reduces crustins/ALF2/Lys1; S2 overexpression induces AMPs. | *Procambarus clarkii* | Low–medium for transfer; different species; overexpression/RNAi, not the mosquito ortholog |
| MD-2 partner search (this work) | Computational / database | Supports feasibility | Are MD-2-like partners available in *Anopheles* | ≥16 ML-domain proteins (Pfam PF02221 / IPR003172) in taxid 7165 (e.g., Q7QJ15, Q7PR71, Q7QCX7, cluster Q7QCX4/5/7/8/9). | *A. gambiae* proteome | High for presence; **no** demonstrated TOLL9 interaction |
| Ortholog alignment (this work) | Structural / evolutionary | Qualifies | How close is the target to the LOF-tested ortholog | Needleman–Wunsch global alignment Q5TWL7 (812 aa) vs *Dmel* Toll-9 Q9VPH1 (900 aa) = **35.6% identity** (343/963). Single-copy in both; same PTHR24365 subfamily. | Dipteran comparison | High for the number; 36% identity means LOF is relevant but transfer is imperfect |

---

## Key Findings (expanded)

### F001 — TOLL9 carries only generic receptor annotations, transferred phylogenetically

UniProt Q5TWL7 has protein existence "Inferred from homology" (level 3) — there is **no experimental characterization of this specific protein**. Its domain architecture is unambiguously that of a Toll/TLR receptor: an extracellular leucine-rich-repeat (LRR) ectodomain (Pfam PF13855 LRR_8 ×2; SMART LRR_TYP ×7), two transmembrane helices (aa 29–49 and 607–631), and a cytoplasmic TIR signaling domain (aa 667–807; Pfam PF01582; PROSITE PS50104). It belongs to PANTHER PTHR24365 ("TOLL-LIKE RECEPTOR 1"), subfamily SF530. All four of its GO annotations are **IBA** (phylogenetically inferred via GO_Central): plasma membrane (GO:0005886), signaling receptor activity (GO:0038023), signal transduction (GO:0007165), and inflammatory response (GO:0006954). Notably **absent** are GO:0038187 (pattern recognition receptor activity) and any Toll-signaling or defense-response BP term. The seed hypothesis's stronger claims are therefore **not** currently supported by the transferred annotation set — they would be new assertions. The current leaf PTN000688561 in PTHR24365 descends from PTN002808045, which supports only generic receptor/signaling/plasma-membrane properties — consistent with the observed transfer scope.

### F002 — Direct PRR/LPS evidence is Bombyx-only and mechanistically chimeric

The direct experimental basis for insect Toll9 as an LPS-recognizing PRR is [PMID: 33963082](https://pubmed.ncbi.nlm.nih.gov/33963082/): BmToll9 (*Bombyx mori*) recognizes LPS through two MD-2-like partners (BmMD-2A/BmMD-2B). However, the demonstration of downstream signaling used a **chimeric receptor** in which the BmToll9 ectodomain was fused to **mouse TLR4 transmembrane and TIR domains**, and the readout (LPS-induced inflammatory-factor release) occurred in **murine cells**. Thus the insect ectodomain's LPS/MD-2 binding is real, but native insect TM/TIR signaling and an insect functional readout were not established. Against a required immune role, the *Drosophila* Toll-9 complete loss-of-function mutant ([PMID: 21386906](https://pubmed.ncbi.nlm.nih.gov/21386906/)) shows no defect in basal or infection-induced AMP responses, while acknowledging overexpression-induced signaling. The *Anopheles* mosGILT^null data ([PMID: 38191283](https://pubmed.ncbi.nlm.nih.gov/38191283/)) are transcriptional co-regulation only — TOLL9 itself was never perturbed.

### F003 — MD-2-like partners exist in Anopheles, so partner-absence does not block the mechanism

A UniProt search (taxid 7165; Pfam PF02221 ML domain / IPR003172 MD-2-related lipid-recognition) returns ≥16 *A. gambiae* proteins (e.g., Q7QJ15, Q7PR71, Q7QCX7, A7USS7, A7UVK2, F5HMB6, and a cluster Q7QCX4/5/7/8/9 of ~148–170 aa). These are the mosquito counterparts of *Bombyx* BmMD-2A/B and mammalian MD-2. The presence of this accessory class means the *Bombyx*-style mechanism is **not excluded** in *Anopheles* on partner-availability grounds. However, **none** is annotated as interacting with TOLL9/AGAP006974, and no LPS-binding assay ties any of them to the target — so this is feasibility, not evidence of function.

### F004 — Anopheles TOLL9 vs Drosophila Toll-9 are ~36% identical

A Needleman–Wunsch global alignment (match +1 / mismatch −1 / gap −1) of full-length *A. gambiae* TOLL9 (Q5TWL7, 812 aa) against *D. melanogaster* Toll-9 (Q9VPH1, 900 aa) yields **35.6% identity** (343 identical positions across 963 aligned columns). Both are single-copy members of the same PANTHER family/subfamily and share the LRR+TM+TIR architecture. This level of divergence is high enough that the dipteran LOF-negative is the **most relevant genetic evidence** available, yet imperfect enough that it cannot fully exclude a divergent function. (The *Bombyx* BmToll9 could not be resolved to a single reviewed UniProt accession, so an *Anopheles*-vs-*Bombyx* identity was not computed — a stated limitation.)

---

## Mechanistic Model / Interpretation

The immediate molecular function under test is **direct microbial-PAMP recognition (PRR activity) coupled to Toll-pathway signal transduction**. The distinction that governs the curation call is:

```
 Direct gene-product activity          |  Downstream / inferred (NOT direct)
 -------------------------------------- | --------------------------------------
 - Transmembrane receptor topology  YES |  - AMP induction phenotypes (Drosophila LOF = none)
 - TIR-domain signaling capacity    ~   |  - Immune-gene co-regulation (mosGILT RNA-seq)
 - LPS/MD-2 recognition (Bombyx,        |  - "Innate immunity" as a pathway outcome
   chimeric TM/TIR)                 ~   |  - Inflammatory response (vertebrate-only, GO:0006954)
 - LPS recognition in Anopheles     NO  |
```

Three mechanistic separations drive the verdict:

1. **Recognition of a processed host cytokine vs. microbial PAMP.** Canonical *Drosophila* Toll binds the cleaved cytokine **Spätzle**, not microbes directly. The seed hypothesis correctly warns against assuming every insect Toll uses Spätzle *and* against equating host-cytokine recognition with GO:0038187 microbial-PAMP recognition. TOLL9's actual ligand in *Anopheles* is **unknown**.

2. **Ectodomain binding vs. native signaling.** In *Bombyx*, the ectodomain's LPS/MD-2 binding is demonstrated, but the productive signaling event used **mouse TLR4 TM+TIR**. This means the insect protein's own TM/TIR was not shown to transduce the signal — a critical gap when transferring an MF PRR term.

3. **Correlation vs. perturbation.** The *Anopheles* mosGILT^null induction of AGAP006974 is transcriptional co-regulation; TOLL9 was never knocked down or out. It cannot establish direct function.

Synthesizing: TOLL9 is architecturally a receptor, and the raw ingredients for an *Anopheles* Toll9/MD-2/LPS PRR complex exist (partner class present). But the chain of direct evidence for **this species** is broken at every functional link — no ligand assay, no partner interaction, no loss-of-function phenotype — and the closest genetic ortholog argues against a required antibacterial role. The proper model is a **plausible-but-unproven immune receptor** whose only defensible current annotations are generic.

---

## GO Curation Implications

**Lead recommendation (requires curator verification):**

| GO term | Aspect | Current status | Recommended action | Rationale |
|---|---|---|---|---|
| GO:0038023 signaling receptor activity | MF | IBA present | **Retain** | Matches domain architecture and ancestral PTHR24365 scope |
| GO:0007165 signal transduction | BP | IBA present | **Retain** | Consistent with TIR-domain receptor |
| GO:0005886 plasma membrane | CC | IBA present | **Retain** | Two TM helices; canonical Toll topology |
| GO:0038187 pattern recognition receptor activity | MF | **Absent** | **Do NOT add as an assertion; flag as lead** | Direct PRR/LPS evidence is *Bombyx*-only and chimeric; no *Anopheles* assay |
| Toll signaling pathway / defense response BP | BP | Absent | **Do NOT add; flag as lead** | Closest ortholog (Drosophila) LOF-negative; mosquito data correlative |
| GO:0006954 inflammatory response | BP | IBA present | **Out of scope here** (resolved separately by vertebrate-only GO:0006954 constraint) | Not part of this question |

The evidence does not justify promoting TOLL9 from a **generic signaling receptor** to a **specific microbial-PAMP pattern-recognition receptor** at the species level. "Protein binding" is explicitly avoided as a recommendation; the informative and defensible MF term remains **signaling receptor activity (GO:0038023)**.

---

## Evidence Base

- **[PMID: 33963082](https://pubmed.ncbi.nlm.nih.gov/33963082/)** — *Toll9 from Bombyx mori functions as a pattern recognition receptor sharing features with TLR4.* Establishes the LPS/MD-2-like PRR property for insect Toll9 and situates Toll9 with the mammalian TLR4 group. Verified snippet: *"Toll9 members differ from other insect Tolls by clustering with the mammalian TLR4 group, which recognizes lipopolysaccharide (LPS) through interaction with myeloid differentiation-2 (MD-2)-like proteins."* Crucially, the functional signaling assay used a chimeric receptor with mouse TLR4 TM+TIR, so it demonstrates ectodomain ligand recognition but not native insect signal transduction.

- **[PMID: 21386906](https://pubmed.ncbi.nlm.nih.gov/21386906/)** — *Lack of an antibacterial response defect in Drosophila Toll-9 mutant.* Loss-of-function genetics in the closest dipteran ortholog directly weakens a required antibacterial immune role. Verified snippet: *"Our results suggest that Toll-9 is neither required to maintain a basal anti-microbial response nor to mount an efficient immune response to bacterial infection."*

- **[PMID: 35238667](https://pubmed.ncbi.nlm.nih.gov/35238667/)** — Review-level statement confirming the Toll9/MD-2/LPS PRR property is a *Bombyx*-specific experimental finding: *"the Toll9/MD-2-like protein complex in the silkworm, Bombyx mori, acts as an innate pattern-recognition receptor that recognizes lipopolysaccharide (LPS)."* Reinforces that this is a single donor species.

- **[PMID: 38191283](https://pubmed.ncbi.nlm.nih.gov/38191283/)** — Reports AGAP006974 induction after mosGILT disruption in *A. gambiae* (RNA-seq). This is expression correlation, not a TOLL9 perturbation, and cannot establish direct function.

- **[PMID: 25573502](https://pubmed.ncbi.nlm.nih.gov/25573502/)** — Crayfish PcToll (clusters with *Drosophila*/*Anopheles* Toll9 and human Tolls) is bacteria-inducible; RNAi and S2 overexpression implicate it in AMP regulation. A competing/context line of evidence from a distant species that shows the Toll9 clade *can* be immune-associated, but does not establish direct PRR activity for the mosquito ortholog.

---

## Conflicts and Alternatives

- **Paralog/clade confusion:** Cross-species Toll9-clade immune associations (crayfish PcToll, [PMID: 25573502](https://pubmed.ncbi.nlm.nih.gov/25573502/)) are suggestive but come from distant taxa and overexpression/RNAi, not the mosquito ortholog. They should not be transferred as direct evidence.
- **Organism-specific divergence:** The strongest genetic test (Drosophila LOF) is negative for antibacterial defense, and the strongest biochemical test (Bombyx) is chimeric and single-species. These pull in opposite directions and together argue for a **species-level "unresolved/lead"** status rather than assertion.
- **Correlation ≠ causation:** mosGILT^null induction of AGAP006974 is a co-regulation signal, easily produced by generic stress/immune transcriptional programs without TOLL9 having direct PRR activity.
- **Database carry-over risk:** Adding GO:0038187 by phylogeny would propagate a *Bombyx*-specific, chimeric-signaling finding across the family — precisely the over-annotation the review should avoid.
- **Ligand-class ambiguity:** Whether TOLL9's ligand is a microbial PAMP (→ GO:0038187) or a processed host cytokine (Spätzle-like) is unknown; conflating the two would mis-annotate the MF.

---

## Limitations and Knowledge Gaps

1. **No *Anopheles*-specific functional data.** There is no LPS/PAMP binding assay, no ligand identification, no interaction assay with any MD-2-like partner, and no loss-of-function phenotype for AGAP006974. Everything about TOLL9's ligand and immune role in *Anopheles* is inferred. *What would resolve it:* direct LPS/microbial-binding assay and RNAi/CRISPR knockdown with infection challenge.

2. **Chimeric-signaling caveat unresolved for any insect.** Even the strongest donor (*Bombyx*) did not show native insect TM/TIR signaling. *What would resolve it:* reconstitute full-length insect Toll9 signaling in an insect cell system with an insect readout (e.g., Drosomycin-luciferase in S2 cells).

3. **Bombyx–Anopheles distance not quantified.** BmToll9 could not be mapped to a single reviewed accession, so the identity to the actual donor of the experimental property was not computed. *What would resolve it:* obtain the exact BmToll9 sequence from PMID33963082 and align.

4. **Partner interaction unproven.** ≥16 ML-domain proteins exist in *Anopheles*, but which (if any) partners TOLL9 is unknown. *What would resolve it:* co-IP / pull-down or AlphaFold-Multimer screening of the TOLL9 ectodomain against the ML-domain set.

5. **Ligand identity.** Microbial PAMP (GO:0038187) vs. processed host cytokine (Spätzle-like) is undetermined — these map to different GO terms. *What would resolve it:* ligand pull-down and Spätzle-processing assays.

---

## Discriminating Tests

1. **RNAi / CRISPR knockdown of AGAP006974 in *A. gambiae*** followed by bacterial (Gram-negative/LPS) and fungal challenge, measuring AMP induction and survival — directly tests the immune/Toll-pathway claim in the target species.
2. **Direct LPS/PAMP binding assay** with recombinant TOLL9 ectodomain ± *Anopheles* ML-domain partners — tests GO:0038187 PRR activity directly.
3. **Native insect signaling reconstitution** (full-length TOLL9, not a mouse-TLR4 chimera) in S2 cells with a Drosomycin/AMP reporter — resolves the chimeric-TM/TIR caveat.
4. **TOLL9–ML-domain interaction screen** (co-IP or AlphaFold-Multimer across the ≥16 candidates) — tests the accessory-partner requirement.
5. **Ligand-class discrimination**: microbial PAMP vs. processed Spätzle-like cytokine — determines the correct GO term (GO:0038187 vs. cytokine-receptor terms).

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

**Action changes:**
- **Retain** generic IBA annotations: GO:0038023 (signaling receptor activity, MF), GO:0007165 (signal transduction, BP), GO:0005886 (plasma membrane, CC).
- **Do NOT assert** GO:0038187 (PRR activity) or Toll-signaling/defense BP terms as species-level annotations. Record them as **hypothesis leads** with the *Bombyx* chimeric caveat and the *Drosophila* LOF-negative explicitly noted.
- GO:0006954 (inflammatory response) is out of scope here (already resolved by the vertebrate-only constraint).

**Candidate references with snippets to verify:**
- [PMID: 33963082](https://pubmed.ncbi.nlm.nih.gov/33963082/): *"Toll9 members differ from other insect Tolls by clustering with the mammalian TLR4 group, which recognizes lipopolysaccharide (LPS) through interaction with myeloid differentiation-2 (MD-2)-like proteins"* — supports PRR/LPS property, but note chimeric TM/TIR.
- [PMID: 21386906](https://pubmed.ncbi.nlm.nih.gov/21386906/): *"Toll-9 is neither required to maintain a basal anti-microbial response nor to mount an efficient immune response to bacterial infection"* — refutes required antibacterial role in the closest ortholog.
- [PMID: 35238667](https://pubmed.ncbi.nlm.nih.gov/35238667/): confirms the PRR property is *Bombyx*-specific (single donor).

**Suggested curator questions:**
- Is a chimeric-receptor demonstration (mouse TLR4 TM+TIR) sufficient to transfer an MF PRR term to a distant ortholog? (Recommended answer: no.)
- Should GO:0038187 be added only after an *Anopheles*-specific binding or LOF assay exists? (Recommended: yes.)

**Suggested experiments:** as listed under Discriminating Tests.

---

## Summary

*A. gambiae* TOLL9 is a bona fide Toll/TLR-family transmembrane receptor whose **generic** annotations — signaling receptor activity (GO:0038023), signal transduction (GO:0007165), and plasma membrane (GO:0005886) — are well justified by domain architecture and the ancestral PTHR24365 transfer scope and should be **retained**. The seed hypothesis's stronger claims — that TOLL9 **directly has pattern-recognition receptor activity (GO:0038187)** and functions as an **innate-immune Toll-signaling receptor** — are **biologically plausible but experimentally unproven in this species**. The direct PRR/LPS evidence is confined to the more distant *Bombyx mori* and was demonstrated through a receptor chimera bearing mouse TLR4 transmembrane and TIR domains; the closest genetic test (*Drosophila* Toll-9 LOF, ~36% identical) shows no antibacterial defect; and the *Anopheles* mosGILT signal is merely correlative. The MD-2-like accessory partner class does exist in *Anopheles* (≥16 ML-domain proteins), so the mechanism is not excluded — but no TOLL9 ligand, interaction, or loss-of-function phenotype has been demonstrated. The correct curation posture is therefore to **retain the generic receptor terms and treat PRR/immune terms as leads, not supported assignments.**


## Artifacts

- [OpenScientist artifact evidence matrix](openscientist_artifacts/artifact_evidence_matrix.csv)
- [OpenScientist artifact go decision table](openscientist_artifacts/artifact_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)