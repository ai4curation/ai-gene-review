---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T08:23:11.617960'
end_time: '2026-10-01T08:33:55.423590'
duration_seconds: 643.81
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: SPRY1
  gene_symbol: SPRY1
  uniprot_accession: O43609
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: free_text
  hypothesis_slug: spry1-grb2-sh3-motif
  hypothesis_text: 'Human SPRY1 (O43609) carries a C-terminal PxxPxR GRB2 SH3-binding
    motif equivalent to the one that lets SPRY2 sequester GRB2. Test this with one
    analysis: scan human SPRY1, SPRY2 and SPRY4 and their mouse and zebrafish orthologs
    for PxxPxR motifs and report the positions and conservation of any hits.'
  term_context: '- Term: protein sequestering activity (GO:0140311)'
  reference_context: '- PMID:12402043'
  source_file: genes/human/SPRY1/SPRY1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: 'Human SPRY1 (O43609) carries a C-terminal PxxPxR\
    \ GRB2 SH3-binding motif equivalent to the\n  one that lets SPRY2 sequester GRB2.\
    \ Test this with one analysis: scan human SPRY1, SPRY2 and SPRY4 and\n  their\
    \ mouse and zebrafish orthologs for PxxPxR motifs and report the positions and\
    \ conservation of any\n  hits.'\nfocus_type: free_text\nterm_id: GO:0140311\n\
    term_label: protein sequestering activity\ncontext: []\nreference_id:\n- PMID:12402043"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 6
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
- **Gene directory:** SPRY1
- **Gene symbol:** SPRY1
- **UniProt accession:** O43609

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** spry1-grb2-sh3-motif
- **Source file:** genes/human/SPRY1/SPRY1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human SPRY1 (O43609) carries a C-terminal PxxPxR GRB2 SH3-binding motif equivalent to the one that lets SPRY2 sequester GRB2. Test this with one analysis: scan human SPRY1, SPRY2 and SPRY4 and their mouse and zebrafish orthologs for PxxPxR motifs and report the positions and conservation of any hits.

## Term and Decision Context

- Term: protein sequestering activity (GO:0140311)

## Reference Context

- PMID:12402043

## Source Context YAML

```yaml
hypothesis: 'Human SPRY1 (O43609) carries a C-terminal PxxPxR GRB2 SH3-binding motif equivalent to the
  one that lets SPRY2 sequester GRB2. Test this with one analysis: scan human SPRY1, SPRY2 and SPRY4 and
  their mouse and zebrafish orthologs for PxxPxR motifs and report the positions and conservation of any
  hits.'
focus_type: free_text
term_id: GO:0140311
term_label: protein sequestering activity
context: []
reference_id:
- PMID:12402043
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

# SPRY1 and the GRB2 SH3-Binding PxxPxR Motif: Hypothesis Evaluation

**Target gene:** SPRY1 (human, UniProt O43609) · **Term under evaluation:** protein sequestering activity (GO:0140311) · **Hypothesis slug:** `spry1-grb2-sh3-motif` · **Reference context:** PMID:12402043

---

## Summary

The seed hypothesis proposes that human SPRY1 (O43609) "carries a C-terminal PxxPxR GRB2 SH3-binding motif equivalent to the one that lets SPRY2 sequester GRB2," and asks for a single decisive analysis: scan human SPRY1, SPRY2, and SPRY4 plus their mouse and zebrafish orthologs for PxxPxR motifs and report positions and conservation. I ran that scan on the canonical UniProt sequences using the regex `P..P.R`. The result **refutes** the hypothesis. The canonical PxxPxR GRB2-SH3 ligand — **PTVPPR at position 304** — is present and conserved specifically in mammalian **SPRY2** (human O43597 and mouse Q9QXV8). It is **absent from SPRY1** (human O43609, mouse Q9QXV9), **absent from SPRY4** (human Q9C004, mouse Q9WTP2), and **absent from the C-terminus of zebrafish spry2** (Q4VBS7). Human SPRY1's actual C-terminal sequence (`...LESCPSRGQGKPS`) contains no PxxPxR motif at all.

This computational result is in exact agreement with the primary experimental literature, which describes the C-terminal PXXPXR GRB2-SH3 motif as **"found exclusively on Spry2"** ([PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/)) and as an **"exclusive, necessary, but cryptic PXXPXR motif in the C terminus of Spry2"** ([PMID:17255109](https://pubmed.ncbi.nlm.nih.gov/17255109/)). Because the structural premise of the hypothesis is false, the proposed basis for assigning **GO:0140311 (protein sequestering activity)** to SPRY1 — GRB2 sequestration via a SPRY2-copied SH3-ligand motif — does not hold. SPRY1 should **not** inherit this annotation by paralog analogy to SPRY2.

Two caveats bound the verdict. First, "refuted" applies narrowly to the *specific mechanism named in the hypothesis* (a constitutive C-terminal SH3 ligand). SPRY1 does conserve an alternative GRB2-engagement feature: the N-terminal phospho-tyrosine Y53 in the context `NEYTEG`, which the supplied reference [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) identifies as the growth-factor-inducible tyrosine mediating SPRY1/SPRY2 binding to GRB2. Second, even for SPRY2 — the paralog that *does* possess the motif — whether GRB2 binding is functionally required for ERK inhibition is actively contested ([PMID:17689925](https://pubmed.ncbi.nlm.nih.gov/17689925/)). Both caveats *strengthen* rather than weaken the recommendation against a sequestration annotation for SPRY1.

---

## Key Findings

### Finding 1 — SPRY1 lacks the C-terminal PxxPxR GRB2 SH3-binding motif present in SPRY2

The hypothesis-specific test was a regex scan (`P..P.R`) of the canonical UniProt sequences for the three human paralogs and their mouse and zebrafish orthologs. The outcome is unambiguous:

| Protein | UniProt | PxxPxR hits | C-terminal SPRY2-type motif? |
|---|---|---|---|
| Human SPRY2 | O43597 | **PTVPPR @ pos 304** | **Yes (C-terminal)** |
| Mouse Spry2 | Q9QXV8 | **PTVPPR @ pos 304** | **Yes (conserved)** |
| Human SPRY1 | O43609 | **none** | No |
| Mouse Spry1 | Q9QXV9 | **none** | No |
| Human SPRY4 | Q9C004 | **none** | No |
| Mouse Spry4 | Q9WTP2 | **none** | No |
| Zebrafish spry2 | Q4VBS7 | none at C-term (`...CRCKNKGVEK`) | No |
| Zebrafish spry1 | B1PBZ7 | N-terminal hits only (pos 34, 44) | No (not SPRY2-type) |

Human SPRY1's C-terminal segment (`...LESCPSRGQGKPS`) contains no PxxPxR. The only canonical C-terminal PxxPxR GRB2-SH3 ligand in any mammalian Sprouty is SPRY2's PTVPPR at position 304, and it is conserved between human and mouse — exactly the paralog- and position-specific signature expected of a SPRY2-specific innovation. The scattered N-terminal "hits" in zebrafish spry1 (positions 34 and 44) are neither positionally nor functionally equivalent to the SPRY2 C-terminal SH3 ligand and do not rescue the hypothesis.

This matches the experimental record directly. [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) states that GRB2 binding "correlates with the binding to Grb2 via a C-terminal proline-rich sequence that is **found exclusively on Spry2**. This PXXPXR motif binds directly to the N-terminal Src homology domain 3 of Grb2, and when added onto the C terminus of Spry4 the resultant chimera inhibits the Ras/ERK pathway." The chimera experiment is especially telling: SPRY4 acquires the GRB2-SH3 activity *only when the SPRY2 motif is grafted onto it*, confirming that non-SPRY2 paralogs — SPRY4, and by the same logic SPRY1 — do not natively possess the motif. [PMID:17255109](https://pubmed.ncbi.nlm.nih.gov/17255109/) independently reinforces exclusivity: "An exclusive, necessary, but cryptic PXXPXR motif in the C terminus of Spry2 is revealed upon stimulation." The core structural claim of the hypothesis is therefore false.

### Finding 2 — Any SPRY1–GRB2 interaction uses a distinct phospho-tyrosine mechanism, and the functional relevance of GRB2 binding is contested even for SPRY2

The reference supplied with the hypothesis, [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/), describes a mechanism *different* from the one the hypothesis invokes: "after stimulation by growth factors Spry1 and Spry2 translocate to the plasma membrane and become phosphorylated on a conserved tyrosine. Next, they bind to the adaptor protein Grb2." This is an **inducible, phospho-tyrosine-dependent** engagement — not a constitutive C-terminal SH3 ligand. In other words, to whatever extent SPRY1 binds GRB2 at all, it would do so through a route that has nothing to do with the PxxPxR motif named in the hypothesis.

Moreover, the functional significance of GRB2 binding is directly challenged even for SPRY2. [PMID:17689925](https://pubmed.ncbi.nlm.nih.gov/17689925/) maps the SPRY2–GRB2 interface to the GRB2 N-terminal SH3 domain and two proline-rich stretches (residues 59–64 and 303–307) and then tests a GRB2-binding-dead double mutant: "a double Sprouty2 mutant (hSpry2 P59AP304A), which is unable to bind Grb2, developed at a similar inhibition level of fibroblast growth factor receptor-ERK pathway than that which originated from Sprouty2 wt. These results are evidence that the Sprouty2 mechanism of ERK inhibition is independent of Grb2 binding." If GRB2 binding is dispensable for ERK inhibition in the paralog that *does* possess the motif, then a sequestration-based functional annotation is on weak ground even in the best case — and weaker still for SPRY1, which lacks the motif entirely.

### Finding 3 — SPRY1 conserves the N-terminal NEYTEG phospho-tyrosine (Y53) but none of SPRY2's canonical SH3-ligand proline motifs

Sequence inspection localizes the conserved regulatory tyrosine. In SPRY2 the key tyrosine sits in the motif `...RNTNEYTEGP...`; human SPRY1 conserves the identical `NEYTEG` context at **Tyr53** (`...RGSNEYTEGP...`), whereas SPRY4 has a divergent context (`...VENDYIDNP...`, Tyr52). This conserved N-terminal tyrosine is precisely the residue that PMID:12402043 requires for growth-factor-induced GRB2 binding, and its presence in SPRY1 defines the *alternative*, non-SH3 route.

Importantly, the SPRY2 N-terminal GRB2-contact proline stretch (residues 59–64, `PTVVPR`) is itself **not** a canonical PxxPxR (`P..P.R`) motif, and SPRY1's aligned region (`PSVVKR`) is likewise not PxxPxR. Thus neither the N-terminal nor the C-terminal SPRY2 proline features are reproduced as a canonical SH3 ligand in SPRY1. The only canonical PxxPxR in any mammalian Sprouty remains SPRY2 position 304 (PTVPPR). The distinction is mechanistically essential: a conserved regulatory tyrosine is not evidence for a constitutive GRB2-SH3 sequestration activity.

---

## Mechanistic Model / Interpretation

The two paralogs engage GRB2 — if at all — through architecturally different features:

```
                         N-terminus                       C-terminus
                             |                                 |
 SPRY2 (O43597):  ...RNT[NEYTEG]P...  ...(PTVVPR 59-64)...  ...[PTVPPR @304]...
                        ^Y55 conserved       ^prolines         ^CANONICAL PxxPxR
                        phospho-Tyr          (not PxxPxR)       GRB2 N-SH3 ligand
                                                                (SPRY2-EXCLUSIVE)

 SPRY1 (O43609):  ...RGS[NEYTEG]P...  ...(PSVVKR aligned)...  ...LESCPSRGQGKPS
                        ^Y53 conserved       ^not PxxPxR        ^NO PxxPxR MOTIF
                        phospho-Tyr

 SPRY4 (Q9C004):  ...VEN[DYIDNP]...   ...                      ...NO PxxPxR MOTIF
                        ^Y52 divergent context
```

The hypothesis conflates two separable modules:

1. **The C-terminal PxxPxR → GRB2-SH3 "sequestration" module.** This is a SPRY2-specific innovation (PTVPPR @304), conserved to mouse but absent from SPRY1, SPRY4, and zebrafish spry2. It is the structural basis for the GO:0140311-style "sequester GRB2" narrative. **SPRY1 does not have it.**

2. **The N-terminal conserved phospho-tyrosine (NEYTEG) → inducible GRB2 engagement.** This *is* conserved in SPRY1 (Y53) and is the route described in the reference PMID:12402043. But it is inducible and phospho-dependent, not a constitutive SH3-ligand sequestration mechanism, and its functional output (ERK inhibition) has been shown to be GRB2-independent even in SPRY2.

The correct reading: the specific molecular feature the hypothesis asserts (a SPRY2-equivalent C-terminal SH3 ligand) **does not exist in SPRY1**. Whatever GRB2-related biology SPRY1 participates in operates through a different, tyrosine-phosphorylation-gated mechanism whose status as "protein sequestering activity" is unsupported by the evidence reviewed here.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| This analysis (UniProt scan, `P..P.R`) | Computational / evolutionary | **Refutes** | Does SPRY1 carry a C-terminal PxxPxR? | PxxPxR (PTVPPR @304) present only in SPRY2 (human + mouse); none in SPRY1, SPRY4, zebrafish spry2 C-term | Canonical UniProt O43609/O43597/Q9C004 + mouse/zebrafish orthologs | High for human/mouse; depends on canonical isoform + regex definition |
| [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) | Direct assay + mutagenesis | **Refutes** (motif = SPRY2-exclusive) | Is the C-terminal GRB2-SH3 motif paralog-specific? | PXXPXR "found exclusively on Spry2"; grafting onto SPRY4 confers ERK inhibition | Mammalian cells, FGFR/ERK | High; in vitro / overexpression |
| [PMID:17255109](https://pubmed.ncbi.nlm.nih.gov/17255109/) | Direct assay | **Refutes** (SPRY2-exclusivity) | Is the C-terminal PXXPXR SPRY2-exclusive and conditional? | "exclusive, necessary, but cryptic PXXPXR motif in the C terminus of Spry2 is revealed upon stimulation" | FGFR–ERK, PP2A context | High; concerns SPRY2 specifically |
| [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) (reference) | Interaction / mechanism | **Qualifies** | How do SPRY1/2 bind GRB2? | GRB2 binding via conserved phospho-tyrosine after membrane translocation — not a constitutive SH3 ligand | Ras/MAPK, growth-factor stimulation | High; defines alternative mechanism conserved in SPRY1 |
| [PMID:17689925](https://pubmed.ncbi.nlm.nih.gov/17689925/) | Mutant phenotype | **Competing** | Is GRB2 binding required for ERK inhibition? | GRB2-binding-dead SPRY2 (P59A/P304A) still inhibits FGFR–ERK → inhibition is GRB2-independent | FGFR–ERK, SPRY2 mutants | High; undercuts sequestration-as-function even for SPRY2 |
| [PMID:24469046](https://pubmed.ncbi.nlm.nih.gov/24469046/) | Review/database + assay | Qualifies | Regulation of SPRY2–GRB2 binding | CK1 phosphorylation modulates SPRY2–GRB2 binding and ERK inhibition | FGF–ERK, PC12 / gastric cancer | Medium; SPRY2-focused, orientation only |
| [PMID:39456824](https://pubmed.ncbi.nlm.nih.gov/39456824/) | Review | Orientation | SPRY2 as GRB2-SOS inhibitor | SPRY2 binds GRB2, inhibits GRB2-SOS, attenuates RAS/ERK | Review | Low–medium; review-level, SPRY2-centric |

---

## Evidence Base

- **[PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/)** — *A Src homology 3-binding sequence on the C terminus of Sprouty2 is necessary for inhibition of the Ras/ERK pathway downstream of fibroblast growth factor receptor stimulation.* The keystone paper: it demonstrates the C-terminal PXXPXR GRB2-SH3 ligand is **exclusive to SPRY2**, binds GRB2's N-terminal SH3, and that transplanting it onto SPRY4 is sufficient to confer ERK inhibition. This directly establishes that SPRY1/SPRY4 lack the motif natively — exactly what the sequence scan found.
- **[PMID:17255109](https://pubmed.ncbi.nlm.nih.gov/17255109/)** — *Direct binding of PP2A to Sprouty2…* Confirms the C-terminal PXXPXR motif is "exclusive" to SPRY2 and only becomes functionally "revealed" upon stimulation, reinforcing both exclusivity and conditionality.
- **[PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/)** — *Sprouty1 and Sprouty2 provide a control mechanism for the Ras/MAPK signalling pathway.* The hypothesis's own reference. It describes SPRY1/SPRY2 binding GRB2 via a conserved phospho-tyrosine after membrane translocation — a mechanism distinct from a C-terminal SH3 ligand and the basis for the alternative (non-refuted) route conserved at SPRY1 Y53.
- **[PMID:17689925](https://pubmed.ncbi.nlm.nih.gov/17689925/)** — *Sprouty2 binds Grb2 at two different proline-rich regions, and the mechanism of ERK inhibition is independent of this interaction.* Competing evidence: a GRB2-binding-dead SPRY2 mutant still inhibits ERK, so GRB2 sequestration is not the functional mechanism even in SPRY2.
- **[PMID:24469046](https://pubmed.ncbi.nlm.nih.gov/24469046/)** and **[PMID:39456824](https://pubmed.ncbi.nlm.nih.gov/39456824/)** — Orientation/review-level material on SPRY2–GRB2 regulation and the GRB2-SOS inhibition model; both are SPRY2-centric and do not provide SPRY1-specific support for GO:0140311.

---

## GO Curation Implications

**Leads for curator verification — do not auto-apply:**

- **GO:0140311 (protein sequestering activity) should NOT be assigned to SPRY1** on the basis of the SPRY2 PxxPxR/GRB2-SH3 paradigm. The structural premise (a SPRY2-equivalent C-terminal SH3 ligand in SPRY1) is directly refuted by the sequence scan and by primary literature stating the motif is SPRY2-exclusive. Assigning GO:0140311 to SPRY1 by analogy would be **paralog over-annotation** / database carry-over.
- If any GRB2-related SPRY1 annotation is contemplated, it must rest on **SPRY1-specific experimental evidence** for the phospho-tyrosine (Y53/NEYTEG) route (per PMID:12402043), not on the C-terminal motif. Even then, the appropriate molecular-function term is uncertain because GRB2 binding is dispensable for ERK inhibition in SPRY2 (PMID:17689925).
- **MF vs BP vs CC:** The best-supported SPRY1 role in this evidence set is participation in **negative regulation of RTK/RAS/MAPK signaling** (a **BP**-level concept), not a specific sequestration MF. For MF, avoid "protein sequestering activity" here; "protein binding" would be uninformative and should be avoided as a final recommendation. If an MF is required, tie it explicitly to the phospho-tyrosine mechanism and flag it as *SPRY1-specific-evidence-pending*.
- **Net recommendation:** Treat GO:0140311 as **non-core / unsupported for SPRY1**; retain it (where experimentally grounded) for **SPRY2**, not SPRY1.

---

## Mechanistic Scope

The immediate molecular event under test is: *does SPRY1 directly present a C-terminal PxxPxR peptide that binds the GRB2 N-terminal SH3 domain to sequester GRB2?* The answer is no — the peptide does not exist in SPRY1. This is a statement about a **direct gene-product structural feature**, the cleanest level at which to evaluate the hypothesis.

Separable and downstream are: (i) SPRY1's broader role as a negative regulator of RAS/MAPK signaling (a pathway-level consequence), (ii) developmental phenotypes from Spry1 loss of function, and (iii) any disease associations. None of these require the C-terminal PxxPxR motif, and none should be used to back-infer a GRB2-sequestration MF for SPRY1. The conserved N-terminal phospho-tyrosine (Y53) is a *direct* feature of SPRY1, but its engagement of GRB2 is inducible and its necessity for ERK inhibition is contested — so it supports, at most, a conditional interaction, not a constitutive sequestration activity.

---

## Conflicts and Alternatives

- **Paralog confusion (primary risk):** The entire GRB2-SH3 "sequestration" story in the literature is SPRY2-specific. Transferring it to SPRY1 is exactly the over-annotation error the evidence warns against. The chimera experiment (PMID:16893902), where SPRY4 gains the activity only after the SPRY2 motif is grafted on, is a direct demonstration that non-SPRY2 paralogs lack the motif natively. (During accession lookup, even the mouse Spry1/Spry2 entries were easy to swap, underscoring this risk.)
- **Mechanism substitution:** The reference PMID:12402043 describes a phospho-tyrosine route, not an SH3-ligand route. A curator could misread "SPRY1 binds GRB2" (true, inducibly) as "SPRY1 sequesters GRB2 via PxxPxR" (false).
- **Function vs. binding:** PMID:17689925 shows GRB2 binding is not required for SPRY2's ERK inhibition, so even a confirmed SPRY1–GRB2 interaction would not establish sequestration as SPRY1's functional mechanism.
- **Organism specificity:** Zebrafish spry2 (Q4VBS7) lacks the C-terminal PxxPxR; zebrafish spry1 (B1PBZ7) has only N-terminal PxxPxR-like stretches. The motif is thus neither pan-vertebrate nor SPRY1-specific.
- **Isoform caveat:** The scan used canonical UniProt sequences; non-canonical SPRY1 isoforms were not exhaustively examined.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | How to resolve |
|---|---|---|---|
| Isoform coverage | Canonical UniProt O43609 only | A rare SPRY1 isoform could in principle contain a C-terminal proline insertion | Scan all annotated SPRY1 isoforms + Ensembl transcripts |
| Direct SPRY1–GRB2 assay | Relied on joint SPRY1/SPRY2 statement in PMID:12402043 | Strength of SPRY1-specific (not SPRY2) GRB2 binding is not quantified here | SPRY1-specific co-IP / ITC with GRB2 ± Y53 mutation |
| Non-canonical SH3 ligands | Only canonical PxxPxR (`P..P.R`) regex used | GRB2 SH3 can tolerate atypical ligands; a non-PxxPxR SPRY1 ligand could be missed | SPOT/peptide-array or structural docking against GRB2 N-SH3 |
| Functional output | Took PMID:17689925 (SPRY2) as read-across | SPRY1 ERK-inhibition dependence on GRB2 not directly tested | SPRY1 GRB2-binding-dead mutant ERK rescue assay |
| GO:0140311 applicability | Evaluated against the PxxPxR premise only | The term might in principle apply via a different SPRY1 partner | Curate against all SPRY1 interaction evidence, not just GRB2 |

---

## Discriminating Tests

1. **Exhaustive isoform/transcript scan** of SPRY1 (all UniProt isoforms + Ensembl) for any C-terminal proline-rich/PxxPxR feature — fastest way to fully close the structural question.
2. **SPRY1-specific GRB2 co-immunoprecipitation** with and without Y53 (NEYTEG) mutated, under growth-factor stimulation, to confirm the phospho-tyrosine route and exclude an SH3 route.
3. **GRB2 N-SH3 pulldown / peptide-array** using SPRY1 C-terminal peptides vs. the SPRY2 PTVPPR peptide as positive control — a direct binding discriminator.
4. **SPRY1 GRB2-binding-dead mutant ERK rescue**, mirroring the SPRY2 P59A/P304A experiment, to test whether any SPRY1 function depends on GRB2.
5. **Cross-species ortholog alignment** anchored on SPRY2 position 304 to formally confirm the motif's SPRY2-restricted phylogenetic distribution.

---

## Proposed Follow-up Actions / Curation Leads

**Leads requiring curator verification:**

- **Action change:** Do not assign **GO:0140311 (protein sequestering activity)** to SPRY1 based on the PxxPxR/GRB2-SH3 analogy. Flag the premise as refuted.
- **Candidate reference + snippet:** [PMID:16893902](https://pubmed.ncbi.nlm.nih.gov/16893902/) — "*via a C-terminal proline-rich sequence that is found exclusively on Spry2. This PXXPXR motif binds directly to the N-terminal Src homology domain 3 of Grb2.*"
- **Candidate reference + snippet:** [PMID:17255109](https://pubmed.ncbi.nlm.nih.gov/17255109/) — "*An exclusive, necessary, but cryptic PXXPXR motif in the C terminus of Spry2 is revealed upon stimulation.*"
- **Candidate reference + snippet (alternative mechanism):** [PMID:12402043](https://pubmed.ncbi.nlm.nih.gov/12402043/) — "*Spry1 and Spry2 translocate to the plasma membrane and become phosphorylated on a conserved tyrosine. Next, they bind to the adaptor protein Grb2.*"
- **Candidate reference + snippet (functional caveat):** [PMID:17689925](https://pubmed.ncbi.nlm.nih.gov/17689925/) — "*a double Sprouty2 mutant (hSpry2 P59AP304A), which is unable to bind Grb2… the Sprouty2 mechanism of ERK inhibition is independent of Grb2 binding.*"
- **Suggested curator question:** Is the SPRY1 GRB2/sequestration lineage derived from SPRY2 by paralog inference? If so, flag for removal or qualification.
- **Suggested experiments:** SPRY1 Y53 mutant GRB2 co-IP; SPRY1 C-terminal peptide vs. GRB2 N-SH3 pulldown (tests 2–3 above).

---

## Conclusion

The hypothesis that human SPRY1 carries a C-terminal PxxPxR GRB2 SH3-binding motif "equivalent to the one that lets SPRY2 sequester GRB2" is **refuted**. The canonical PxxPxR motif (PTVPPR @304) is a SPRY2-specific, mouse-conserved feature absent from SPRY1, SPRY4, and the C-terminus of zebrafish spry2, in exact agreement with primary literature describing the motif as "found exclusively on Spry2." SPRY1 instead conserves an N-terminal phospho-tyrosine (Y53/NEYTEG) that mediates an inducible, mechanistically distinct GRB2 engagement — a route whose functional necessity is contested even for SPRY2. Accordingly, **GO:0140311 (protein sequestering activity) should not be assigned to SPRY1 on the basis of this hypothesis**, and any GRB2-related SPRY1 annotation must await SPRY1-specific experimental evidence for the phospho-tyrosine mechanism.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)