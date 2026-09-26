---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:21:48.391976'
end_time: '2026-09-21T04:52:42.714178'
duration_seconds: 1854.32
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: PARTE
  gene: A0BFB4
  gene_symbol: A0BFB4
  uniprot_accession: A0BFB4
  taxon_id: NCBITaxon:5888
  taxon_label: Paramecium tetraurelia
  focus_type: function_assignment
  hypothesis_slug: autophagy-ancestry-versus-hmm-family-placement
  hypothesis_text: Paramecium tetraurelia A0BFB4 (GSPATT00028266001, 381 aa) inherited
    autophagosome assembly/regulation and phagophore/autophagosome association from
    PTN000681272. The actual PANTHER treeinfo API for PTHR24348 places target leaf
    PTN002805316 below PTN000681272 through PTN007795585, PTN008401646, PTN001218730
    and PTN007795752; this is confirmed ancestry, not a donor-count inference. The
    same current PAINT resource propagates all four terms. However, live UniProt/InterPro
    HMM classification assigns PTHR44167:SF18 (match70-348, reported score7.6e-61),
    and the PTHR44167 tree lacks this target. Reconcile this discrepancy using sequence
    identity/versions, actual MSA/tree evidence and ciliate ATG1 biology. Does target-specific
    evolutionary or mechanistic evidence support loss/misplacement, or are the inherited
    autophagy functions still appropriate? Family labels, missing animal accessory
    domains, absent target experiments and short donor lists alone are not evidence
    of loss. Evaluate each activity/process/location distinctly and state what cannot
    be resolved. Root records actual tree path and classifications in projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/PARTE/A0BFB4/A0BFB4-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Paramecium tetraurelia A0BFB4 (GSPATT00028266001,\
    \ 381 aa) inherited autophagosome assembly/regulation\n  and phagophore/autophagosome\
    \ association from PTN000681272. The actual PANTHER treeinfo API for PTHR24348\n\
    \  places target leaf PTN002805316 below PTN000681272 through PTN007795585, PTN008401646,\
    \ PTN001218730\n  and PTN007795752; this is confirmed ancestry, not a donor-count\
    \ inference. The same current PAINT resource\n  propagates all four terms. However,\
    \ live UniProt/InterPro HMM classification assigns PTHR44167:SF18\n  (match70-348,\
    \ reported score7.6e-61), and the PTHR44167 tree lacks this target. Reconcile\
    \ this discrepancy\n  using sequence identity/versions, actual MSA/tree evidence\
    \ and ciliate ATG1 biology. Does target-specific\n  evolutionary or mechanistic\
    \ evidence support loss/misplacement, or are the inherited autophagy functions\n\
    \  still appropriate? Family labels, missing animal accessory domains, absent\
    \ target experiments and short\n  donor lists alone are not evidence of loss.\
    \ Evaluate each activity/process/location distinctly and state\n  what cannot\
    \ be resolved. Root records actual tree path and classifications in projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json.\n\
    focus_type: function_assignment\ncontext: []\nreference_id: []"
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
- filename: provenance_a0bfb4_alphafold_plddt.json
  path: openscientist_artifacts/provenance_a0bfb4_alphafold_plddt.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist a0bfb4 alphafold plddt
- filename: provenance_a0bfb4_family_and_alignment.json
  path: openscientist_artifacts/provenance_a0bfb4_family_and_alignment.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist a0bfb4 family and alignment
---

## Question

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** PARTE
- **Taxon:** Paramecium tetraurelia (NCBITaxon:5888)
- **Gene directory:** A0BFB4
- **Gene symbol:** A0BFB4
- **UniProt accession:** A0BFB4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** autophagy-ancestry-versus-hmm-family-placement
- **Source file:** genes/PARTE/A0BFB4/A0BFB4-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Paramecium tetraurelia A0BFB4 (GSPATT00028266001, 381 aa) inherited autophagosome assembly/regulation and phagophore/autophagosome association from PTN000681272. The actual PANTHER treeinfo API for PTHR24348 places target leaf PTN002805316 below PTN000681272 through PTN007795585, PTN008401646, PTN001218730 and PTN007795752; this is confirmed ancestry, not a donor-count inference. The same current PAINT resource propagates all four terms. However, live UniProt/InterPro HMM classification assigns PTHR44167:SF18 (match70-348, reported score7.6e-61), and the PTHR44167 tree lacks this target. Reconcile this discrepancy using sequence identity/versions, actual MSA/tree evidence and ciliate ATG1 biology. Does target-specific evolutionary or mechanistic evidence support loss/misplacement, or are the inherited autophagy functions still appropriate? Family labels, missing animal accessory domains, absent target experiments and short donor lists alone are not evidence of loss. Evaluate each activity/process/location distinctly and state what cannot be resolved. Root records actual tree path and classifications in projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Paramecium tetraurelia A0BFB4 (GSPATT00028266001, 381 aa) inherited autophagosome assembly/regulation
  and phagophore/autophagosome association from PTN000681272. The actual PANTHER treeinfo API for PTHR24348
  places target leaf PTN002805316 below PTN000681272 through PTN007795585, PTN008401646, PTN001218730
  and PTN007795752; this is confirmed ancestry, not a donor-count inference. The same current PAINT resource
  propagates all four terms. However, live UniProt/InterPro HMM classification assigns PTHR44167:SF18
  (match70-348, reported score7.6e-61), and the PTHR44167 tree lacks this target. Reconcile this discrepancy
  using sequence identity/versions, actual MSA/tree evidence and ciliate ATG1 biology. Does target-specific
  evolutionary or mechanistic evidence support loss/misplacement, or are the inherited autophagy functions
  still appropriate? Family labels, missing animal accessory domains, absent target experiments and short
  donor lists alone are not evidence of loss. Evaluate each activity/process/location distinctly and state
  what cannot be resolved. Root records actual tree path and classifications in projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json.
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

# AIGR Gene Hypothesis Deep Research — *Paramecium tetraurelia* A0BFB4

**Focus type:** function_assignment
**Hypothesis slug:** autophagy-ancestry-versus-hmm-family-placement
**Target:** A0BFB4 (GSPATT00028266001), 381 aa, *Paramecium tetraurelia* (NCBITaxon:5888)
**Source file:** `genes/PARTE/A0BFB4/A0BFB4-ai-review.yaml`

---

## Summary

The seed hypothesis asks whether the four autophagy IBA terms propagated into A0BFB4 through PANTHER family PTHR24348 reflect genuine ATG1/ULK ancestry or a misplacement created by the competing live UniProt/InterPro HMM assignment to the generic family PTHR44167:SF18. **The verdict is partially supported, with a clean split: the ancestry is real and the molecular-function terms should be retained, but the propagated autophagy process/location terms are over-annotations that should be removed or flagged uncertain.**

The apparent family-placement conflict dissolves on inspection. PTHR24348 is officially named "Serine/threonine-protein kinase UNC-51-RELATED" — the ATG1/ULK autophagy-initiating kinase family (UNC-51 is the *C. elegans* ATG1 ortholog). An independent Smith-Waterman local alignment of A0BFB4's kinase domain ranks human ULK2 (35.3% identity) and ULK1 (34.5%) as its closest characterized references, above the STE20-family kinases LOK/SLK and above CHEK2. The "competing" best-hit family PTHR44167:SF18 is a functionally uncharacterized "Serine/Threonine Protein Kinase" catch-all with no assigned GO. So the two families are not truly competing: one captures the evolutionary clade, the other is a scoring artifact carrying no function. A0BFB4 genuinely belongs to the ATG1/ULK clade by ancestry, and this ancestry is **not** a misplacement.

Ancestry, however, does not license the pathway-level terms. A0BFB4 is a bare 381-aa kinase catalytic domain. A comparative-genomics study that explicitly includes *Paramecium tetraurelia* ([PMID: 28123910](https://pubmed.ncbi.nlm.nih.gov/28123910/)) shows ciliates do not encode a typical Atg1: every candidate kinase lacks the Atg1-specific C-terminal domain required to build the Atg1 initiation complex, and the complex partners (Atg13, Atg17/FIP200, Atg101) are absent from ciliate genomes. An AlphaFold structural check (AF-A0BFB4-F1) confirms the missing module is genuinely absent — the only confidently folded non-kinase element is N-terminal, while the C-terminus is a short, partly disordered 33-residue tail. Because the machinery that nucleates a phagophore is absent in the ciliate lineage and in this protein specifically, GO:0000045, GO:0000407, GO:0005776, and GO:0010506 rest solely on phylogenetic IBA inference and cannot be executed by the canonical mechanism. The molecular-function terms (protein Ser/Thr kinase activity, ATP binding) are strongly supported and should be kept.

---

## Executive Judgment

**Verdict: Partially supported.** Family placement is correct (ATG1/ULK ancestry confirmed by two independent lines); MF terms supported; the four IBA-propagated autophagy BP/CC terms are over-annotations (weakly supported) for this ciliate protein.

Reasoning:

1. **No family misplacement.** The PAINT/TreeGrafter graft is into PTHR24348 = "Ser/Thr kinase UNC-51-RELATED" = the ATG1/ULK family. Top sequence identity is to ULK1/ULK2 (~35%), members of that same family. The graft reflects genuine ancestry.
2. **The "competing" HMM is not competing.** PTHR44167:SF18 is a generic, functionally uncharacterized kinase family with no specific GO. The PTHR24348-vs-PTHR44167 discrepancy is a best-hit-vs-graft methodology artifact, not evidence of an alternative function.
3. **Target-relevant biology weakens the specific autophagy function.** Ciliates (including *Paramecium tetraurelia*) lack a typical Atg1: kinase candidates lack the Atg1 C-terminal domain, and the Atg1-complex partners are absent. A0BFB4 fits this class exactly and, per AlphaFold, has no C-terminal partner-binding module. The process/location terms cannot be executed by the canonical mechanism.

**Most important caveats:** (a) the Atg1-absence evidence is in-silico and does not fully exclude a divergent/non-canonical role; (b) ~35% kinase-domain identity places the protein in the ATG1/ULK clade but is not proof of one-to-one orthology; (c) there are no experimental data on A0BFB4 itself (localization, substrates, knockdown phenotype).

---

## Key Findings

### Finding 1 — The autophagy IBA rests on genuine ATG1/UNC-51 ancestry, not a misplacement

The four autophagy IBA terms enter A0BFB4 via a PAINT/TreeGrafter graft into PANTHER family **PTHR24348**, officially "Serine/threonine-protein kinase UNC-51-RELATED." UNC-51 is the *C. elegans* ATG1 ortholog; this family is the ATG1/ULK clade of autophagy-initiating kinases. The seed hypothesis feared that the live UniProt/InterPro HMM best-hit — **PTHR44167:SF18** (match 70–348, reported score 7.6e-61) — represented a competing, contradictory placement. It does not: PTHR44167 carries the current InterPro name "Serine/Threonine Protein Kinase," a functionally uncharacterized catch-all family with **no specific GO or function assigned**. A best-single-HMM assignment to a generic family is a scoring artifact, not evidence of a distinct biological function.

An independent sequence-identity check corroborates the ATG1/ULK reading. A Smith-Waterman local alignment (BLOSUM62, gap -11/-1) of A0BFB4's kinase domain against a panel of characterized human kinases ranked:

| Human reference | Family | % identity | SW score |
|---|---|---|---|
| ULK2 | ATG1/ULK (PTHR24348) | 35.3% | 306 |
| ULK1 | ATG1/ULK (PTHR24348) | 34.5% | 299 |
| LOK/STK10 | STE20 | 32.3% | — |
| SLK | STE20 | 30.5% | — |
| CHEK2 | CAMK/CHK | 25.3% | — |
| yeast Atg1 | ATG1 | ~23% | — |

Two independent lines — the PANTHER tree graft and top-hit sequence identity — agree on ATG1/ULK ancestry. **The PTHR44167 assignment is a generic best-HMM artifact and does not refute the autophagy-family placement.** This reconciles the discrepancy in the seed hypothesis in favor of "confirmed ancestry, not misplacement."

### Finding 2 — A0BFB4 is an intact, catalytically active single-domain Ser/Thr kinase (MF terms strongly supported)

A0BFB4 (381 aa) carries only protein-kinase signatures: Pfam PF00069, InterPro IPR000719 (protein kinase domain), IPR017441 (ATP-binding site), IPR008271 (Ser/Thr active site); SMART S_TKc; PROSITE PS00107/PS00108/PS50011. All canonical catalytic residues are present and intact:

- Glycine-rich P-loop: **GEGTFG**
- VAIK β3 lysine: **CKV**
- HRD catalytic loop: **HRDIK**
- DFG Mg²⁺-binding motif: present
- APE motif: present

This architecture predicts a catalytically active (non-pseudo) kinase and directly supports **GO:0004674 (protein serine/threonine kinase activity)** and **GO:0005524 (ATP binding)**. Critically, the protein is a *bare catalytic domain*: it lacks the ULK/ATG1 C-terminal (CTD/MIT) module that binds ATG13/FIP200/ATG101 and targets the kinase to the phagophore. The molecular-function annotations are robust; the CC and BP autophagy terms depend on machinery the protein does not carry.

### Finding 3 — Comparative genomics: *Paramecium* and all ciliates lack a typical Atg1

Aslan, Küçükoğlu & Arslanyolu (2017, [PMID: 28123910](https://pubmed.ncbi.nlm.nih.gov/28123910/); open access PMC5244887) surveyed ATG proteins across five ciliate genomes, **explicitly including *Paramecium tetraurelia*** (plus *Tetrahymena thermophila*, *Ichthyophthirius multifiliis*, *Oxytricha trifallax*, *Stylonychia lemnae*). Two abstract statements directly govern this curation:

> "ciliate genomes do not encode typical Atg1 since all the candidate sequences lack an Atg1-specific C-terminal domain which is essential for Atg1 complex formation"

> "Consistent with the absence of Atg1, ciliates also lack other members of the Atg1 complex"

The full text adds that "these kinase domain containing proteins should not be considered as Atg1 candidates without further experimental analyses, since they all lack the important C-terminal domains," and that "Other components of this kinase complex (Atg1, Atg13, Atg17, Atg29 and Atg31) are also absent in ciliates." Canonical Atg1/ULK1 has three regions (N-terminal kinase domain, central Pro/Ser-rich region, C-terminal domain); the C-terminal domain binds Atg13/Atg17(FIP200)/Atg101 and is essential for the complex that induces autophagy. **A0BFB4 is exactly the kinase-domain-only class the authors say should NOT be counted as Atg1 without experiments.** The authors further propose that ciliate autophagosome formation may proceed via Atg6 (Beclin/Vps30) in an Atg1-*independent* manner — meaning even where autophagy occurs in ciliates, this kinase need not be the initiator.

### Finding 4 — AlphaFold confirms no C-terminal ATG1 partner-binding domain

The AlphaFold DB model **AF-A0BFB4-F1** (v6) provides a residue-level structural test. Segmenting by the HMM kinase match (residues 70–348):

| Region | Residues | Mean pLDDT | % > 70 | % < 50 | Interpretation |
|---|---|---|---|---|---|
| N-terminal flank | 1–69 | 93.2 | 99% | 0% | Confidently folded |
| Kinase domain | 70–348 | 91.6 | 95% | — | Confidently folded |
| C-terminal flank | 349–381 | 64.2 | 39% | 30% | Short, partly disordered |
| Whole protein | 1–381 | 89.5 | — | — | High-confidence model |

The only confidently structured non-kinase element is **N-terminal**, whereas the ATG1/ULK1 partner-binding module (recruiting ATG13/ATG17-FIP200/ATG101) is a **C-terminal** domain. A0BFB4 has no such C-terminal domain — its C-terminus is a 33-residue low-confidence tail — and the N-terminal folded region matches no InterPro signature, so its function is unresolved. This independently clinches the over-annotation call: the protein structurally lacks the module that would assemble the Atg1 initiation complex.

---

## Mechanistic Model / Interpretation

```
   ANCESTRY (real)                          EXECUTABLE FUNCTION (not supported)
   ───────────────                          ──────────────────────────────────
   A0BFB4 kinase domain                      Autophagy initiation requires:
     │  ~35% id to ULK1/ULK2                   • Atg1 C-terminal domain  ── ABSENT
     │  grafts into PTHR24348                  • Atg13 partner           ── ABSENT in ciliates
     ▼  (UNC-51/ATG1 family)                   • Atg17/FIP200            ── ABSENT in ciliates
   ATG1/ULK-family Ser/Thr kinase             • Atg101                  ── ABSENT in ciliates
     │                                                 │
     │  intact catalytic motifs                        ▼
     ▼  (P-loop, VAIK, HRD, DFG, APE)          No phagophore-nucleation complex
   ACTIVE kinase  ✔ MF terms                   ✘ BP/CC autophagy terms cannot execute
     │
     │  bare catalytic domain
     ▼
   No C-terminal partner-binding module (AlphaFold: C-term = 33-aa disordered tail)
```

**How the discrepancy is reconciled.** The seed hypothesis framed PTHR24348 (autophagy) vs PTHR44167:SF18 (generic kinase) as competing placements. They are not truly competing: PTHR24348 captures the *evolutionary clade* (ATG1/ULK), and PTHR44167 is a *scoring catch-all* with no function. So the family-placement conflict dissolves — A0BFB4 really is an ATG1/ULK-family kinase by ancestry and by top sequence identity.

**Why ancestry does not license the process/location terms.** Membership in the ATG1/ULK clade by kinase-domain homology is necessary but not sufficient to perform autophagosome initiation. That function is delivered by the C-terminal scaffolding domain and its binding partners, all of which are absent in ciliates generally and in A0BFB4 specifically (by architecture and by AlphaFold structure). IBA propagation transfers terms based on the phylogenetic node, but the transfer overreaches because it ignores the loss of the accessory module in the ciliate lineage. This is a textbook case where **evolutionary placement is correct but functional propagation is too strong.**

The seed guidance cautions that "family labels, missing animal accessory domains, absent target experiments and short donor lists alone are not evidence of loss." The over-annotation call here does not rest on any single such heuristic. It rests on convergent, target-relevant evidence: (1) a dedicated ciliate-wide comparative-genomics study that names *Paramecium tetraurelia* and states the C-terminal domain and entire Atg1 complex are absent; (2) an AlphaFold structure showing the missing module is genuinely absent, not merely HMM-undetected; and (3) the mechanistic requirement that the Atg1 complex — not a lone kinase domain — nucleates the phagophore. Together these exceed a "missing accessory domain" argument.

---

## Evidence Base / Evidence Matrix

| # | Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt A0BFB4; InterPro (live) | Computational / database | Qualifies | Live HMM family identity | Best-hit family PTHR44167:SF18 ("Serine/Threonine Protein Kinase", generic, no functional GO) | *P. tetraurelia* | High for the fact; family carries no function |
| 2 | PANTHER PTHR24348 (InterPro name) | Structural/evolutionary | Supports ancestry | Is the PAINT graft into an autophagy family? | PTHR24348 = "Ser/Thr kinase UNC-51-RELATED" = ATG1/ULK family | Cross-species tree | High; graft placement per PANTHER treeinfo |
| 3 | This work (Smith-Waterman, BLOSUM62) | Computational | Supports ancestry | Closest characterized kinase to A0BFB4 | ULK2 35.3%, ULK1 34.5% > LOK 32.3% > SLK 30.5% > CHEK2 25.3% | 381-aa kinase domain | Moderate; best-hit over kinase domain, not full phylogeny |
| 4 | This work (motif scan) | Computational (sequence) | Supports MF | Is it a catalytically active kinase? | Intact P-loop (GEGTFG), VAIK-K, HRD-D, DFG, APE | Sequence | High for "active kinase"; supports MF terms |
| 5 | [PMID: 28123910](https://pubmed.ncbi.nlm.nih.gov/28123910/) (Aslan 2017) | Comparative genomics (primary, in-silico) | **Refutes/qualifies BP/CC** | Do ciliates (incl. *Paramecium*) have a functional Atg1? | No typical Atg1; candidates lack Atg1 C-terminal domain; Atg1-complex members absent; *P. tetraurelia* is one of 5 genomes | 5 ciliate genomes | Moderate-high; in-silico; doesn't exclude non-canonical role |
| 6 | [PMID: 24280724](https://pubmed.ncbi.nlm.nih.gov/24280724/) (Akematsu 2014) | Mutant/pathway (Tetrahymena) | Qualifies (context) | Is ciliate autophagy functional/Atg1-dependent? | Programmed nuclear death is "a novel type of autophagy"; VPS34/ATG8-driven; "absence of some ATG genes" | *T. thermophila* | Autophagy exists but via non-ATG1 route |
| 7 | AlphaFold AF-A0BFB4-F1 (v6); this work | Structural/computational | **Refutes/qualifies CC/BP** | Does A0BFB4 have a C-terminal ATG1 partner-binding domain? | Confident N-term (1-69, pLDDT 93) + kinase (70-348, pLDDT 92); C-term (349-381) short, disordered (pLDDT 64); no C-terminal CTD/MIT | *P. tetraurelia* model | High for topology; N-term element function unresolved |
| 8 | [PMID: 21624459](https://pubmed.ncbi.nlm.nih.gov/21624459/) | Review | Qualifies (context) | Does autophagy occur in ciliates? | Programmed nuclear death by autophagy is a real ciliate process | *Tetrahymena* | Orientation only |

---

## GO Curation Implications (leads — require curator verification)

| GO term | Aspect | Current basis | Lead recommendation | Rationale |
|---|---|---|---|---|
| GO:0004674 protein serine/threonine kinase activity | MF | IBA | **RETAIN** | Intact catalytic motifs; strongly supported |
| GO:0005524 ATP binding | MF | IEA/architecture | **RETAIN** | Canonical P-loop/VAIK ATP site intact |
| GO:0000045 autophagosome assembly | BP | IBA (PTHR24348) | **REMOVE or mark uncertain** | Requires Atg1 complex absent in ciliates; no C-terminal domain |
| GO:0000407 phagophore assembly site | CC | IBA | **REMOVE or mark uncertain** | Depends on complex recruitment; localization unconfirmed |
| GO:0005776 autophagosome | CC | IBA | **REMOVE or mark uncertain** | No structural/experimental support in *Paramecium* |
| GO:0010506 regulation of autophagy | BP | IBA | **GENERALIZE / non-core / uncertain** | Non-canonical regulatory role conceivable but unproven |

Overall, the MF annotations should be retained — and are more informative than a bare "protein binding" placeholder — while the four IBA-propagated autophagy BP/CC terms should be treated as over-annotations pending experimental support, and are candidates for removal or an uncertainty qualifier. If the framework prefers not to delete IBA terms, the minimum defensible action is a caveat noting lineage-specific loss of the accessory module, citing PMID 28123910 and the AlphaFold structure. These are leads, not final GO actions.

---

## Mechanistic Scope

- **Directly testable / supported:** A0BFB4 is an intact, likely catalytically active protein serine/threonine kinase (ATP binding + phosphotransfer). This is the immediate molecular activity and is well supported by domain architecture.
- **Downstream / inferred only:** "autophagosome assembly," "phagophore assembly site," "autophagosome," and "regulation of autophagy" are pathway-level roles that, in yeast/mammals, depend on ATG1/ULK1 assembling with Atg13–Atg17(FIP200)–Atg101 via its C-terminal domain. A0BFB4 lacks that domain and ciliates lack those partners; hence these are inferred pathway consequences of the ancestral family, **not established activities of this gene product**.
- **Localization** (phagophore/autophagosome) is a consequence of targeting via the missing module — not supported.

No *Paramecium*-specific experiment (substrate, localization, mutant phenotype) exists for A0BFB4, so all process/location claims are inference only.

---

## Conflicts and Alternatives

- **Database carry-over / method artifact.** The autophagy terms are IBA propagations from the ATG1/ULK ancestral node; the live HMM lands on a generic family. Both are automated outputs; neither is experimental.
- **Paralog / expansion context.** *Paramecium tetraurelia* underwent successive whole-genome duplications, producing large kinase paralog sets; A0BFB4 may be one of several divergent ATG1-like kinase-domain paralogs, further weakening one-to-one ATG1 orthology.
- **Alternative pathway.** Aslan et al. propose ciliate autophagosome formation may proceed via Atg6/Beclin (Vps30) in an Atg1-independent manner — consistent with Tetrahymena programmed nuclear death being VPS34/ATG8-driven ([PMID: 24280724](https://pubmed.ncbi.nlm.nih.gov/24280724/)) rather than ATG1-driven.
- **Not a competing function.** The generic PTHR44167 framing is not supported by the current family name; there is no positive evidence for a distinct alternative function (e.g., DNA-damage checkpoint) to replace autophagy.
- **Genuine tension.** Ciliates DO have autophagy machinery (programmed nuclear death; PMID 24280724, 21624459) — the pathway is not absent wholesale. But the specific Atg1-complex-mediated initiation step that these GO terms describe is the part shown to be absent.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No experimental data on A0BFB4 | UniProt/literature — none found | All functional calls are inferential | Localization (GFP), in-vitro kinase assay, RNAi autophagy phenotyping in *Paramecium* |
| Is A0BFB4 the *Paramecium* Atg1 candidate in Aslan et al.? | Paper analyzes *Paramecium*; individual accessions not extractable here | Exact mapping to A0BFB4 | Cross-reference the paper's supplementary accession list |
| Non-kinase-domain partner-binding capacity | AlphaFold: folded N-term (1-69), short disordered C-term | Determines whether a cryptic module exists | *Partly resolved:* no C-terminal domain; N-term matches no InterPro — HHpred/Foldseek could assign it |
| Orthology vs homology | ~35% identity; PTHR24348 graft | Determines if function transfer is valid at all | Reciprocal best-hit + gene-tree/species-tree reconciliation |
| Substrate identity | Kinase active, substrate unknown | Function could be non-autophagy | Phosphoproteomics after knockdown |
| Full phylogeny vs best-hit | Only pairwise identities (all-pairs tree run timed out) | Firms up clade assignment | ML/NJ tree with ciliate homologs incl. C-terminal-domain character |

---

## Discriminating Tests

1. **RNAi/knockdown of A0BFB4 in *Paramecium* + autophagy readout** (ATG8 lipidation/puncta; starvation- or autogamy-induced macronuclear autophagy) — directly tests any autophagy role.
2. **In-vitro kinase assay** on recombinant A0BFB4 to confirm catalytic activity (validates MF) and, with candidate substrates, probe the pathway.
3. **Co-IP / proximity labeling** for Atg13/FIP200/Atg101 homologs — tests whether an Atg1 complex can form (predicted negative given their absence).
4. **GFP localization** under starvation/conjugation — tests "phagophore assembly site"/"autophagosome" CC terms.
5. **Phosphoproteomics** comparing wild-type vs knockdown to identify substrates and infer the real pathway.
6. **Phylogenetic placement / Foldseek-DALI** with a curated ATG1/ULK vs CAMK-group alignment across ciliates and model eukaryotes, scoring the C-terminal-domain presence/absence character; structural search of the unassigned N-terminal element.

---

## Curation Leads (require curator verification)

- **Candidate reference to add:** [PMID: 28123910](https://pubmed.ncbi.nlm.nih.gov/28123910/) (Aslan, Küçükoğlu & Arslanyolu, *PeerJ* 2017). Verify snippets: *"ciliate genomes do not encode typical Atg1 since all the candidate sequences lack an Atg1-specific C-terminal domain which is essential for Atg1 complex formation"* and *"Consistent with the absence of Atg1, ciliates also lack other members of the Atg1 complex."* Full text (PMC5244887) lists *Paramecium tetraurelia* among five genomes and states these kinase-domain proteins "should not be considered as Atg1 candidates without further experimental analyses."
- **Supporting reference:** [PMID: 24280724](https://pubmed.ncbi.nlm.nih.gov/24280724/) — verify: *"Programmed nuclear death (PND) in the ciliate protozoan Tetrahymena thermophila is a novel type of autophagy"* and *"the absence of some ATG genes in this organism."*
- **Structural provenance:** AlphaFold AF-A0BFB4-F1 (v6) — C-terminal region (349–381) mean pLDDT 64.2, no C-terminal partner-binding domain; document as evidence the Atg1 accessory module is genuinely absent.
- **Candidate action changes:** Retain MF (GO:0004674, GO:0005524). Flag/remove or add uncertainty to BP GO:0000045, GO:0010506 and CC GO:0000407, GO:0005776 as ATG1-complex-dependent functions unsupported in ciliates.
- **Suggested curator questions:** (i) Should IBA autophagy terms be down-weighted when the target lineage demonstrably lacks the required complex? (ii) Is a generic "protein phosphorylation" BP a safer core than "autophagosome assembly"? (iii) Should the MF terms be re-sourced to sequence/architecture evidence (ISS/ISM) rather than remain tied to the same IBA graft?
- **Suggested experiments:** the six Discriminating Tests above.

---

## Proposed Follow-up Experiments / Actions

1. **For the curator (immediate):** apply the GO decision table — retain the two MF terms, remove or flag the four autophagy BP/CC terms — and attach PMID 28123910 plus the AlphaFold provenance as justification.
2. **For wet-lab resolution:** RNAi knockdown + autophagy-flux assay under starvation/autogamy is the single most decisive experiment; a negative result would refute the BP terms outright.
3. **For bioinformatic firming-up:** run an ML phylogeny of ciliate ATG1-like kinases scoring C-terminal-domain presence, and a Foldseek/HHpred search of the unassigned N-terminal folded element to determine whether it confers any lineage-specific targeting or regulatory role.

---

## Provenance / Artifacts

- Catalytic-motif scan, family reconciliation table, and Smith-Waterman identity table (executed code + outputs).
- AlphaFold AF-A0BFB4-F1 (v6) per-residue pLDDT-by-region computation.
- UniProt/InterPro/PANTHER record retrieval; EuropePMC abstract + full-text extraction confirming *Paramecium* inclusion and Atg1-absence statements.

*Limitations: all computational results are conservative inferences; no experimental data on A0BFB4 exist; the Atg1-absence evidence is in-silico. Local repository `*-bioinformatics` analyses were withheld from this run.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist a0bfb4 alphafold plddt](openscientist_artifacts/provenance_a0bfb4_alphafold_plddt.json)
- [OpenScientist a0bfb4 family and alignment](openscientist_artifacts/provenance_a0bfb4_family_and_alignment.json)