---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T21:12:26.751023'
end_time: '2026-09-20T21:26:38.325817'
duration_seconds: 851.57
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DAPPU
  gene: DpuGr29
  gene_symbol: DpuGr29
  uniprot_accession: E9FXF3
  taxon_id: NCBITaxon:6669
  taxon_label: Daphnia pulex
  focus_type: function_assignment
  hypothesis_slug: daphnia-courtship-and-ligand-gated-channel-function
  hypothesis_text: Daphnia pulex DpuGr29 (E9FXF3) participates in male courtship behavior
    and has ligand-gated cation channel activity. Assess the inherited behavioral
    annotation and an existing reviewer-added channel proposal separately. PMID:19383158
    places this receptor in an expanded Daphnia gustatory-receptor clade; known insect
    cuticular-hydrocarbon receptors can belong to different lineages. Inspect PTN001080220
    placement and compare experimental ligand/channel/behavior evidence without imposing
    an insect-only taxon restriction on courtship. Broad chemosensory family membership
    alone does not establish a particular ligand, behavioral role, or demonstrated
    channel chemistry.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DAPPU/DpuGr29/DpuGr29-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Daphnia pulex DpuGr29 (E9FXF3) participates in\
    \ male courtship behavior and has ligand-gated\n  cation channel activity. Assess\
    \ the inherited behavioral annotation and an existing reviewer-added channel\n\
    \  proposal separately. PMID:19383158 places this receptor in an expanded Daphnia\
    \ gustatory-receptor clade;\n  known insect cuticular-hydrocarbon receptors can\
    \ belong to different lineages. Inspect PTN001080220\n  placement and compare\
    \ experimental ligand/channel/behavior evidence without imposing an insect-only\n\
    \  taxon restriction on courtship. Broad chemosensory family membership alone\
    \ does not establish a particular\n  ligand, behavioral role, or demonstrated\
    \ channel chemistry.\nfocus_type: function_assignment\ncontext: []\nreference_id:\
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
- filename: provenance_DpuGr29_GO_decision_table.csv
  path: openscientist_artifacts/provenance_DpuGr29_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist DpuGr29 GO decision table
- filename: provenance_DpuGr29_evidence_matrix.csv
  path: openscientist_artifacts/provenance_DpuGr29_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist DpuGr29 evidence matrix
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** DAPPU
- **Taxon:** Daphnia pulex (NCBITaxon:6669)
- **Gene directory:** DpuGr29
- **Gene symbol:** DpuGr29
- **UniProt accession:** E9FXF3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** daphnia-courtship-and-ligand-gated-channel-function
- **Source file:** genes/DAPPU/DpuGr29/DpuGr29-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Daphnia pulex DpuGr29 (E9FXF3) participates in male courtship behavior and has ligand-gated cation channel activity. Assess the inherited behavioral annotation and an existing reviewer-added channel proposal separately. PMID:19383158 places this receptor in an expanded Daphnia gustatory-receptor clade; known insect cuticular-hydrocarbon receptors can belong to different lineages. Inspect PTN001080220 placement and compare experimental ligand/channel/behavior evidence without imposing an insect-only taxon restriction on courtship. Broad chemosensory family membership alone does not establish a particular ligand, behavioral role, or demonstrated channel chemistry.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Daphnia pulex DpuGr29 (E9FXF3) participates in male courtship behavior and has ligand-gated
  cation channel activity. Assess the inherited behavioral annotation and an existing reviewer-added channel
  proposal separately. PMID:19383158 places this receptor in an expanded Daphnia gustatory-receptor clade;
  known insect cuticular-hydrocarbon receptors can belong to different lineages. Inspect PTN001080220
  placement and compare experimental ligand/channel/behavior evidence without imposing an insect-only
  taxon restriction on courtship. Broad chemosensory family membership alone does not establish a particular
  ligand, behavioral role, or demonstrated channel chemistry.
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

# AIGR Gene Hypothesis Deep Research: DpuGr29 (E9FXF3) — Courtship Behavior and Ligand-Gated Cation Channel Function

**Target gene:** DpuGr29 / E9FXF3 — *Daphnia pulex* (NCBITaxon:6669)
**Focus type:** function_assignment
**Hypothesis slug:** daphnia-courtship-and-ligand-gated-channel-function

---

## Executive Judgment

**Verdict — the hypothesis is composed of two claims that must be judged separately:**

1. **"Male courtship behavior" (GO:0008049) — OVER-ANNOTATED (down-weight/remove as a direct function).** This Biological Process annotation on DpuGr29 exists *only* as a phylogenetically-inferred (IBA) over-transfer propagated from *Drosophila* courtship gustatory receptors (Gr32a, Gr33a, and relatives) through PANTHER ancestral node PTN001080220. It represents a *Drosophila*-specific downstream behavioral phenotype, not a demonstrated molecular activity or process of the *Daphnia* protein. There is no *Daphnia* ligand, behavior, or expression evidence supporting it. The correct curatorial stance is to **not assert male courtship behavior for DpuGr29** — and to base that decision on the *absence of supporting evidence*, not on an insect-only taxon restriction (the seed hypothesis is correct that courtship is not intrinsically insect-restricted; the problem is evidentiary, not taxonomic).

2. **"Ligand-gated cation channel activity" (Molecular Function) — PARTIALLY SUPPORTED as a homology/structure-based inference, but NOT experimentally demonstrated.** Insect gustatory receptors (GRs) are now established by cryo-EM to be 7-transmembrane tetrameric ligand-gated cation channels, and DpuGr29 is a bona fide member of that superfamily that retains the conserved C-terminal TM7 pore/gating signature motif. This makes channel activity a *reasonable homology-based inference*. However, no channel electrophysiology, ligand deorphanization, or any functional data exist for DpuGr29 — or for any *Daphnia* GR. The term should therefore be entered, if at all, as an explicitly **inferred / not-demonstrated** MF, and the specific ligand must remain unspecified.

**Most important caveat:** E9FXF3 is UniProt protein-existence level **4 (Predicted)** with zero experimental characterization. Both claims rest entirely on computational/homology inference. The seed hypothesis's core caution — "broad chemosensory family membership alone does not establish a particular ligand, behavioral role, or demonstrated channel chemistry" — is fully vindicated by this investigation.

---

## Key Findings

### Finding 1 — "Male courtship behavior" is an IBA over-transfer from *Drosophila*, not a direct DpuGr29 function

The GO annotation GO:0008049 (male courtship behavior) on E9FXF3, as recorded in QuickGO, carries evidence code **IBA (ECO:0000318, "biological aspect of ancestor")**, reference **GO_REF:0000033**, and is **assignedBy GO_Central**. It was propagated computationally from the PANTHER ancestral node **PTN001080220**. The experimental source annotations feeding that node come from *Drosophila melanogaster* genes: **Gr32a (FBgn0032416)** and the related receptors FBgn0041231, FBgn0041246, and FBgn0264556.

The underlying experimental basis is entirely *Drosophila*-specific. Moon et al. 2009 ([PMID: 19765987](https://pubmed.ncbi.nlm.nih.gov/19765987/)) demonstrated that **Gr32a is necessary for inhibiting male-to-male courtship**, and that Gr33a mutant males show increased male-to-male courtship. These are behavioral phenotypes of specific *Drosophila* receptors that detect specific *Drosophila* cuticular-hydrocarbon pheromones.

Critically, DpuGr29 sits within a **lineage-specific expansion of 58 gustatory receptors** in the *Daphnia pulex* genome (Peñalva-Arana et al. 2009, [PMID: 19383158](https://pubmed.ncbi.nlm.nih.gov/19383158/)). Membership in a large, independently expanded receptor clade means that subfamily membership *cannot* be used to infer a specific behavioral role. IBA propagation across such an expansion transfers a *Drosophila* phenotype label onto a crustacean protein that has never been shown to detect a pheromone, participate in mating, or even be expressed in a relevant tissue.

**Statistical/evidentiary summary:**
- Evidence code: IBA (ECO:0000318), GO_REF:0000033, GO_Central, from PANTHER node PTN001080220.
- Experimental source: *Drosophila* Gr32a/Gr33a courtship phenotypes (PMID:19765987).
- DpuGr29 status: UniProt protein-existence level 4 (Predicted); member of PTHR21143 / IPR013604; one of 58 lineage-specific *Daphnia* Grs (PMID:19383158).

> Supporting quote (PMID:19765987): *"GR32a, which is necessary for inhibiting male-to-male courtship"* — establishes the courtship role as a *Drosophila*-specific behavioral phenotype, the experimental origin of the propagated IBA annotation.

> Supporting quote (PMID:19383158): *"We describe 58 Grs (gustatory receptors), belonging to the insect chemoreceptor superfamily, which were identified bioinformatically in the draft genome of the crustacean waterflea Daphnia pulex."* — places DpuGr29 in a large lineage-specific expansion, so subfamily membership alone cannot establish a specific behavior.

### Finding 2 — Ligand-gated cation channel activity is a structurally-supported *family* property, but only homology-inferred for DpuGr29

Recent cryo-EM work has resolved the long-standing question of insect GR mechanism. Insect GRs are **7-transmembrane tetrameric ligand-gated cation channels**. The structure of *Bombyx mori* Gr9 (BmGr9) shows it is a **fructose-gated cation channel** that opens its gate through movement of the C-terminal S7b helix ([PMID: 38573859](https://pubmed.ncbi.nlm.nih.gov/38573859/); [PMID: 38187590](https://pubmed.ncbi.nlm.nih.gov/38187590/)). A 2025 review synthesizes the field's consensus that GRs "operate as ligand-gated cation channels" ([PMID: 41208322](https://pubmed.ncbi.nlm.nih.gov/41208322/)). The odorant receptor (OR) family, which evolved from the GR family, likewise assembles into heteromeric ligand-gated cation channels ([PMID: 33502604](https://pubmed.ncbi.nlm.nih.gov/33502604/)).

DpuGr29 is a genuine member of this superfamily: it is classified in **PANTHER PTHR21143** (invertebrate gustatory receptor), **InterPro IPR013604** (7TM chemoreceptor), and **Pfam PF08395 (7tm_7)**, with 7–8 predicted transmembrane helices. Because the channel chemistry is a conserved, structurally-demonstrated property of the family, it is a reasonable inference that DpuGr29 possesses the same fold and, plausibly, the same channel activity.

However, the inference stops at plausibility. **No channel electrophysiology, no ligand deorphanization, and no functional data exist for DpuGr29 or for any *Daphnia* GR.** Furthermore, *Daphnia* has **no Orco/OR co-receptor** (PMID:19383158), so the co-receptor requirements for assembling a functional *Daphnia* GR channel are entirely unknown. The activity is therefore *homology-inferred, not demonstrated*.

**Statistical/evidentiary summary:**
- Structural demonstration: BmGr9 is a fructose-gated cation channel; gate opens via S7b helix (PMID:38573859, PMID:38187590).
- Family consensus: GRs operate as ligand-gated cation channels (PMID:41208322); ORs form ligand-gated cation channels (PMID:33502604).
- DpuGr29 membership: PTHR21143 / IPR013604 / PF08395, 7–8 predicted TM helices.
- Limitation: E9FXF3 is protein-existence level 4 (Predicted); zero functional data; no *Daphnia* co-receptor known.

> Supporting quote (PMID:38573859): *"We present structures of Bombyx mori Gr9 (BmGr9), a fructose-gated cation channel, in agonist-free and fructose-bound states."*

> Supporting quote (PMID:41208322): *"Functionally, GRs operate as ligand-gated cation channels."*

> Supporting quote (PMID:33502604): *"the odorant receptors (ORs), which evolved from the gustatory receptor family. Both receptor types assemble to heteromeric ligand-gated cation channels."*

### Finding 3 — DpuGr29 retains the conserved TM7 pore/gating signature motif

A direct regex scan of the E9FXF3 sequence (379 aa) located the canonical 7tm-chemoreceptor C-terminal signature **T-Y-x(5)-Q-F** as the sequence **`TYLVILYQF` at residues 364–372**, positioned inside the UniProt-predicted final transmembrane helix (TM8, residues 354–372). This motif corresponds to the structurally conserved pore-lining / gating segment — the **S7b helix** in the BmGr9 cryo-EM structure — that forms the ion-conducting channel gate in insect GRs and ORs (PMID:38573859).

Retention of this signature is meaningful structural corroboration: DpuGr29 has not diverged so far from the insect GR fold that it has lost the gating machinery. This strengthens the homology argument for channel activity beyond mere superfamily membership. It does **not**, however, demonstrate function — sequence retention of a gating motif is consistent with, but does not prove, an active channel, a particular ligand, or a functional oligomeric assembly.

**Computational provenance note:** The motif scan was performed directly on the E9FXF3 sequence. PANTHER web endpoints returned HTTP 403 and were not programmatically accessible during this run, so PTN001080220 placement was confirmed via QuickGO annotation provenance rather than a live PANTHER tree query. No *Daphnia* Orco/Or exists (PMID:19383158); co-receptor requirements for *Daphnia* GR channel assembly remain unknown.

> Supporting quote (PMID:38573859): *"Upon fructose binding, BmGr9's channel gate opens through helix S7b movements."* — identifies the C-terminal TM7 (S7b) helix as the gating element, the region where DpuGr29 retains the conserved TY..QF signature.

---

## Mechanistic Model / Interpretation

The two claims map onto two different levels of the gene-product's biology, and conflating them is the central curatorial risk.

```
                        DpuGr29 (E9FXF3) — Daphnia pulex GR
                        UniProt PE level 4 (Predicted)
                                    |
        ┌───────────────────────────┴───────────────────────────┐
        |                                                        |
  MOLECULAR FUNCTION (MF)                              BIOLOGICAL PROCESS (BP)
  "ligand-gated cation channel activity"              "male courtship behavior"
        |                                                        |
  Basis: STRUCTURAL HOMOLOGY                           Basis: IBA PHENOTYPE TRANSFER
  - PTHR21143 / IPR013604 / PF08395                    - PANTHER node PTN001080220
  - 7-8 TM helices                                     - Source: Dmel Gr32a/Gr33a
  - TM7 gate motif TYLVILYQF (res 364-372)            - Moon 2009 (PMID:19765987)
  - Family cryo-EM proof: BmGr9 (PMID:38573859)        - Drosophila-specific behavior
        |                                                        |
   PLAUSIBLE, CONSERVED FOLD                          DOWNSTREAM PHENOTYPE of a
   -> homology-inferred channel MF                     SPECIFIC INSECT RECEPTOR
        |                                                        |
   x No electrophysiology                              x No Daphnia pheromone
   x No ligand known                                   x No Daphnia mating assay
   x No Daphnia co-receptor known                      x No Daphnia expression data
        |                                                        |
   VERDICT: PARTIALLY SUPPORTED                        VERDICT: OVER-ANNOTATED
   (enter as inferred / not demonstrated)              (do not assert as direct function)
```

**Interpretation.** The molecular function (channel activity) is a *conserved, deep, structural* property of the receptor fold. When a protein clearly belongs to a family whose defining biochemical activity is structurally demonstrated across multiple members, homology transfer of that activity is defensible — this is exactly how the GO IEA/ISS framework is intended to work, provided the annotation is flagged as inferred and the specific ligand is left open.

The biological process (courtship) is a *shallow, lineage-specific, downstream* phenotype. It emerges only when a *particular* receptor detects a *particular* pheromone in a *particular* neuron in a *particular* species' mating circuit. None of those particulars are established for *Daphnia*. Transferring "male courtship behavior" across a 58-member lineage-specific expansion is precisely the kind of over-propagation that IBA pipelines are prone to, and it should be corrected on evidentiary grounds.

The seed hypothesis's framing is analytically correct: the courtship annotation should be down-weighted **because the evidence does not exist**, not because courtship is taxonomically forbidden outside insects. Cuticular-hydrocarbon receptors can belong to different lineages, and behavior is not lineage-restricted a priori — but neither of those considerations supplies the missing *Daphnia* evidence.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Direction | Claim tested | Key finding | Context | Confidence / limitations |
|------|-----------------|---------------|-----------|--------------|-------------|---------|--------------------------|
| [19383158](https://pubmed.ncbi.nlm.nih.gov/19383158/) | *Chemoreceptor genes of the waterflea Daphnia pulex: many Grs but no Ors* | Structural/evolutionary | Qualifies | Family placement of DpuGr29 | 58 lineage-specific Grs; no Ors/Orco in *Daphnia* | *Daphnia pulex* genome | High for placement; membership != specific function |
| [19765987](https://pubmed.ncbi.nlm.nih.gov/19765987/) | *A Drosophila GR essential for aversive taste and inhibiting male-to-male courtship* | Mutant phenotype | Competing (source of IBA) | Origin of courtship BP annotation | Gr32a required to inhibit male-to-male courtship | *Drosophila melanogaster* | High for *Drosophila*; not transferable to *Daphnia* without evidence |
| [38573859](https://pubmed.ncbi.nlm.nih.gov/38573859/) | *Structural basis of ligand specificity and channel activation in an insect GR* | Direct assay / structural | Supports (MF, by homology) | Channel activity of insect GRs | BmGr9 is a fructose-gated cation channel; S7b gate | *Bombyx mori*, cryo-EM | High for family; homology inference for DpuGr29 |
| [38187590](https://pubmed.ncbi.nlm.nih.gov/38187590/) | *Structure of an insect gustatory receptor* | Structural | Supports (MF, by homology) | GR 7TM tetrameric channel architecture | First experimental GR structures | Insect GR, cryo-EM | High for family; not DpuGr29-specific |
| [41208322](https://pubmed.ncbi.nlm.nih.gov/41208322/) | *A structural perspective on insect gustatory receptors* | Review/database | Supports (MF, by homology) | GR molecular function consensus | "GRs operate as ligand-gated cation channels" | Review | Review-level; orientation for MF |
| [33502604](https://pubmed.ncbi.nlm.nih.gov/33502604/) | *Functional properties of insect olfactory receptors: IRs and ORs* | Review/database | Supports (MF, by homology) | Superfamily channel chemistry | ORs (from GR family) form ligand-gated cation channels | Review | Review-level; superfamily context |
| [18952610](https://pubmed.ncbi.nlm.nih.gov/18952610/) | *A Drosophila protein family implicated in pheromone perception (CheB / GM2-AP)* | Localization / interaction | Qualifies | CH-pheromone perception mechanism | CheB proteins interact with lipid-like pheromones in taste hairs | *Drosophila* | Context on pheromone machinery; not a GR channel study |
| [35700364](https://pubmed.ncbi.nlm.nih.gov/35700364/) | *Taste avoidance of metal ions* | Behavioral | Qualifies | GR-mediated taste behavior scope | GR-mediated aversive taste in fly | *Drosophila* | Illustrates diversity of GR ligands/behaviors |
| [29081083](https://pubmed.ncbi.nlm.nih.gov/29081083/) | *IR76b required for gustatory aversion to excessive Na+* | Mutant phenotype | Qualifies | Ionotropic gustation | IR-mediated salt aversion | *Drosophila* | Parallel chemosensory channel context |

**How the evidence coheres:** Four independent structural/review papers (PMID:38573859, 38187590, 41208322, 33502604) converge on the ligand-gated cation channel identity of the insect GR/OR superfamily, and DpuGr29's domain classification plus its retained TM7 gate motif place it inside that superfamily — this is the strongest, most defensible part of the hypothesis. In contrast, the courtship BP claim traces to a single *Drosophila* mutant-phenotype study (PMID:19765987) whose relevance to *Daphnia* is entirely assumed by IBA propagation across a lineage-specific expansion documented in PMID:19383158.

---

## GO Curation Implications

**Lead requiring curator verification — two distinct actions:**

**(A) Molecular Function — ligand-gated cation channel activity (e.g., GO:0099094 "ligand-gated monoatomic cation channel activity").**
- Evidence supports an **MF** term at the family level by structural homology.
- Recommended action: **Retain only as an inferred (ISS/ISO or IBA) annotation, explicitly flagged as not experimentally demonstrated.** Do not upgrade to an experimental evidence code. Leave the ligand unspecified (do not assert fructose, sugar, or any pheromone). If the curation model allows, prefer a slightly more general channel term or annotate at the level justified by homology while noting the co-receptor and functional-assembly uncertainties.
- Avoid "protein binding" as a fallback — the channel MF is more informative and is family-supported.

**(B) Biological Process — male courtship behavior (GO:0008049).**
- Evidence does **not** support asserting this as a direct BP of DpuGr29.
- Recommended action: **Do not assert / remove or down-weight the IBA annotation for this gene.** The annotation is a *Drosophila*-specific downstream phenotype over-transferred across a lineage-specific expansion. If any BP is to be retained, use a **generic chemosensory / taste / sensory-perception BP** (e.g., detection of chemical stimulus / gustatory-type sensory behavior) rather than the specific courtship term — and even that should be homology-inferred, not asserted.
- The rationale for down-weighting is **evidentiary (no *Daphnia* ligand/behavior/expression data)**, explicitly *not* a taxon restriction on courtship.

**(C) Cellular Component.** By homology, an **integral component of membrane / plasma membrane** CC is defensible (7TM receptor), but no *Daphnia*-specific localization data exist; treat as inferred.

---

## Mechanistic Scope

The **immediate molecular function** under test is: does the DpuGr29 protein form (or contribute to) a ligand-gated cation channel that conducts current in response to binding a chemical ligand? This is a direct biochemical/biophysical property of the receptor protein and is the appropriate MF-level claim. The evidence for it is *homology-based*: the fold, the domain signatures, and the retained TM7 gate motif are all present, and the family's channel activity is structurally proven — but the specific channel activity of DpuGr29 has never been directly measured.

The **male courtship behavior** claim is not a molecular function at all; it is a **downstream, organism-level, lineage-specific phenotype**. In *Drosophila*, courtship inhibition emerges from a specific circuit: Gr32a/Gr33a-expressing taste neurons on the male foreleg detect specific cuticular-hydrocarbon pheromones, which modulate the mating decision (context supported by PMID:19765987 and the CheB pheromone-perception work, PMID:18952610). Every element of this circuit — the ligand, the neuron, the expression pattern, the behavioral readout — is *Drosophila*-specific and undemonstrated in *Daphnia*. Assigning the behavioral term to DpuGr29 confuses "this protein family member, in one insect, participates in a mating circuit" with "this *Daphnia* protein directly performs male courtship behavior." That is a category error at the MF/BP boundary and a paralog/ortholog over-transfer at the phylogenetic level.

---

## Conflicts and Alternatives

1. **Paralog/expansion over-annotation (primary conflict).** DpuGr29 is one of 58 lineage-specifically expanded *Daphnia* Grs (PMID:19383158). IBA propagation from a handful of *Drosophila* courtship receptors across this entire clade is a classic frequency/expansion bias: the annotation attaches to many crustacean paralogs that likely detect entirely different (and unknown) ligands.

2. **Organism-specific circuitry.** *Daphnia* lacks Orco/ORs (PMID:19383158) and its GR channel assembly requirements are unknown. The *Drosophila* courtship pathway cannot be assumed to have a *Daphnia* counterpart; *Daphnia* reproduction (cyclical parthenogenesis with environmentally-induced males) differs fundamentally from *Drosophila* mating.

3. **In-silico-only characterization.** E9FXF3 is protein-existence level 4 (Predicted). Both claims are computational. There is no in vitro or in vivo assay for this protein.

4. **Ligand ambiguity.** Even within demonstrated GR structures, ligands vary widely (fructose for BmGr9; bitter/aversive compounds and CH-pheromones for various *Drosophila* Grs; metal-ion avoidance, PMID:35700364). Family membership predicts *a* channel but not *which* ligand — so any specific ligand assertion for DpuGr29 would be unsupported.

5. **Alternative interpretation for the MF.** It remains formally possible (though there is no positive evidence) that DpuGr29 has diverged functionally or requires an unidentified *Daphnia*-specific co-receptor to form a channel, in which case an isolated monomer might not be a functional channel. The retained TM7 motif argues against complete loss of gating capacity but cannot rule out assembly-dependence.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters for curation | What would resolve it |
|-----|------------------|-----------------------------|------------------------|
| No functional data for DpuGr29 | UniProt PE level 4; literature search | MF and BP both rest entirely on inference | Heterologous electrophysiology / calcium-imaging deorphanization |
| Unknown ligand | Family ligands vary (fructose, bitters, CH-pheromones, metals) | Cannot assert any specific ligand or behavior | Ligand screen in a heterologous expression system |
| No *Daphnia* expression data | Literature; no tissue/cell data found | Cannot place DpuGr29 in any sensory circuit | In situ hybridization / scRNA-seq of *Daphnia* sensory tissue |
| Co-receptor requirement unknown | PMID:19383158 (no Orco/OR) | Channel may need an unidentified partner to assemble | Co-expression / interaction studies in *Daphnia* |
| PANTHER tree not queried live | QuickGO provenance used; PANTHER endpoints returned HTTP 403 | PTN001080220 placement confirmed indirectly | Direct PANTHER tree inspection when accessible |
| No AlphaFold channel-pore analysis run | Sequence motif scan only | Would strengthen/weaken structural homology inference | AlphaFold-Multimer tetramer model + pore analysis |

---

## Discriminating Tests

The following would most efficiently separate the supported, inferred, and refuted components of the hypothesis:

1. **Heterologous deorphanization + electrophysiology (decisive for MF).** Express DpuGr29 (with candidate *Daphnia* co-receptors) in *Xenopus* oocytes, HEK293, or a *Drosophila* empty-neuron system and test for ligand-evoked cation currents against a panel (sugars including fructose, amino acids, bitter compounds, metal ions, candidate *Daphnia* semiochemicals). A positive current would upgrade the MF from inferred to demonstrated and identify the ligand.

2. **AlphaFold-Multimer tetramer model + pore geometry analysis (cheap, in-silico).** Model the DpuGr29 homotetramer and check whether the TM7/S7b helices line a plausible ion-conduction pathway, comparing pore radius to BmGr9. This strengthens or weakens the channel inference without wet-lab work.

3. **Expression profiling in *Daphnia* (decisive for any BP).** scRNA-seq or in situ hybridization localizing DpuGr29 to specific sensory neurons/tissues; presence in male-specific reproductive sensory structures would be a prerequisite (not proof) for any courtship-related role.

4. **Behavioral genetics in *Daphnia* (decisive for the courtship BP).** RNAi/CRISPR knockdown of DpuGr29 followed by mating/male-behavior assays. Absence of a mating phenotype would confirm the courtship annotation is spurious for this gene.

5. **Comparative clade analysis.** Map which *Daphnia* Grs are orthologous vs. lineage-specific relative to *Drosophila* courtship Grs; a large phylogenetic distance would further undermine the IBA transfer.

---

## Curation Leads

*All items below are leads requiring curator verification.*

**Candidate action changes:**
- **Remove or down-weight** GO:0008049 (male courtship behavior) IBA annotation on E9FXF3 — over-transferred *Drosophila* phenotype, no *Daphnia* evidence. Rationale = evidentiary, not taxonomic.
- **Retain** ligand-gated cation channel MF **only as an explicitly inferred (homology/structure-based) annotation**, ligand unspecified; do not use an experimental evidence code.

**Candidate references with exact snippets to verify:**
- PMID:19765987 — *"GR32a, which is necessary for inhibiting male-to-male courtship"* (source of the courtship IBA; *Drosophila*-specific).
- PMID:19383158 — *"We describe 58 Grs ... in the draft genome of the crustacean waterflea Daphnia pulex"* (lineage-specific expansion; no Ors/Orco).
- PMID:38573859 — *"structures of Bombyx mori Gr9 (BmGr9), a fructose-gated cation channel"* and *"BmGr9's channel gate opens through helix S7b movements"* (family channel MF; TM7 gate).
- PMID:41208322 — *"GRs operate as ligand-gated cation channels"* (review-level MF orientation).
- PMID:33502604 — *"Both receptor types assemble to heteromeric ligand-gated cation channels"* (superfamily channel chemistry).

**Candidate GO terms:**
- MF (inferred): GO:0099094 *ligand-gated monoatomic cation channel activity* (or a suitable channel-activity term), ligand left open.
- CC (inferred): integral component of membrane / plasma membrane.
- BP: prefer a generic chemosensory/gustatory sensory term over GO:0008049; or assert no BP pending evidence.

**Suggested curator questions:**
- Does any *Daphnia* expression, ligand, or behavioral dataset support DpuGr29 involvement in mating? (Current answer: none found.)
- Should IBA courtship annotations propagated across lineage-specific crustacean Gr expansions be systematically reviewed for over-transfer?

**Suggested experiments:** heterologous electrophysiology/deorphanization; AlphaFold-Multimer pore analysis; *Daphnia* expression profiling; RNAi/CRISPR behavioral assays (detailed in Discriminating Tests).

---

## Conclusion

Judge the two claims separately. **"Male courtship behavior" (GO:0008049) is over-annotated** for DpuGr29 — a *Drosophila*-specific downstream phenotype propagated by IBA across a 58-member lineage-specific *Daphnia* Gr expansion, with no *Daphnia* ligand, expression, or behavioral support; it should not be asserted as a direct function (on evidentiary, not taxonomic, grounds). **"Ligand-gated cation channel activity" is partially supported** as a homology/structure-based inference — insect GRs are structurally proven ligand-gated cation channels (BmGr9 cryo-EM) and DpuGr29 is a bona fide superfamily member retaining the conserved TM7 gating signature (TYLVILYQF, residues 364–372) — but it is not experimentally demonstrated for any *Daphnia* GR, the ligand is unknown, and E9FXF3 is protein-existence level 4 (Predicted) with zero experimental characterization. The MF should be entered as inferred/not-demonstrated; the courtship BP should be removed or replaced with a generic chemosensory term.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist DpuGr29 GO decision table](openscientist_artifacts/provenance_DpuGr29_GO_decision_table.csv)
- [OpenScientist DpuGr29 evidence matrix](openscientist_artifacts/provenance_DpuGr29_evidence_matrix.csv)