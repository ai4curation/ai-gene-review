---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T03:38:21.909519'
end_time: '2026-10-15T04:22:38.250277'
duration_seconds: 2656.34
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: PP_4594
  gene_symbol: PP_4594
  uniprot_accession: Q88E72
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004123
  hypothesis_text: PP_4594 has cystathionine gamma-lyase activity (GO:0004123).
  term_context: '- Term: cystathionine gamma-lyase activity (GO:0004123)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/PP_4594/PP_4594-goa.tsv

    - file:PSEPK/PP_4594/PP_4594-uniprot.txt

    - file:projects/P_PUTIDA/deep-research/PSEPK__methionine_biosynthesis__ppu00270-deep-research-openscientist.md

    - file:PSEPK/PP_4594/PP_4594-deep-research-openscientist.md'
  source_file: genes/PSEPK/PP_4594/PP_4594-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004123\n  label: cystathionine gamma-lyase\
    \ activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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

# AIGR TreeGrafter Function-Inference Stress Test

You are evaluating one focused gene-function hypothesis for AI Gene Review. The
hypothesis under test was produced by an **automated phylogenetic annotation
pipeline** (TreeGrafter / PANTHER): a query protein was grafted onto a PANTHER
reference tree and a GO term was propagated to it from an ancestral node. Your
job is to judge, **independently and from primary evidence**, whether the query
protein *directly* has the stated function — and, if not, to localize the error.

This is not a general gene overview. Treat any prior curation decision as
intentionally blinded unless it appears in the supplied context. Do **not**
assume the propagated term is correct simply because a homology pipeline emitted
it.

## Target Gene

- **Organism code:** PSEPK
- **Taxon:** Pseudomonas putida KT2440 (NCBITaxon:160488)
- **Gene directory:** PP_4594
- **Gene symbol:** PP_4594
- **UniProt accession:** Q88E72

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004123
- **Source file:** genes/PSEPK/PP_4594/PP_4594-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

PP_4594 has cystathionine gamma-lyase activity (GO:0004123).

## Term and Decision Context

- Term: cystathionine gamma-lyase activity (GO:0004123)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/PP_4594/PP_4594-goa.tsv
- file:PSEPK/PP_4594/PP_4594-uniprot.txt
- file:projects/P_PUTIDA/deep-research/PSEPK__methionine_biosynthesis__ppu00270-deep-research-openscientist.md
- file:PSEPK/PP_4594/PP_4594-deep-research-openscientist.md

## Source Context YAML

```yaml
term:
  id: GO:0004123
  label: cystathionine gamma-lyase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **PP_4594 directly has the stated function**. Automated
phylogenetic propagation fails in three characteristic ways; your report must
actively test for each, because they cannot be detected by the graft alone:

1. **Granularity / family-vs-subfamily.** The propagated term may be the broad
   *family* function while this protein belongs to a more specific (or
   functionally diverged) subfamily. Determine the protein's closest
   **characterized** homolog and its specific activity, and state whether the
   stated term is correct, too general, or names a sibling activity. (Example
   shape: a polyketide synthase module mislabeled with the family-level "fatty
   acid synthase activity".)
2. **Pseudo-enzyme / loss of activity.** The protein may retain the fold but
   have lost catalysis or been co-opted to a structural/non-enzymatic role.
   Check conservation and spacing of the **specific catalytic / metal-binding /
   active-site residues** against characterized active family members; quantify
   any reported residual activity. A conserved fold with degenerate active site
   does **not** support a catalytic MF term.
3. **Within-superfamily mis-placement.** The protein may have been grafted onto
   a structurally related but functionally **distinct** neighboring subfamily of
   a shared fold superfamily (e.g. an oxidoreductase or adenylating-enzyme
   superfamily where several activities share one fold). Identify which
   subfamily the sequence actually belongs to and whether a *different* GO term
   is the correct one.

Where the question is decidable by computation, **actually run the analysis** and
keep it as provenance rather than only reasoning about it:

- **Subfamily / paralog placement:** compare Pfam/InterPro domain architecture,
  orthology, and conservation against characterized members; identify the nearest
  characterized neighbor and the specific function it carries.
- **Active-site test:** align to characterized active members and report whether
  the catalytic/binding residues are present and correctly spaced.
- **Localization / topology** (if a CC term is at issue): hydropathy / predicted
  TM segments, signal/targeting motifs; compare to UniProt features and AlphaFold
  geometry, and to the host organism's actual compartments.

Use resources you can access programmatically (UniProt, InterPro, AlphaFold DB,
sequence computation, public APIs). If a resource is web-only or you cannot run a
check, say so plainly — an inconclusive or "could not run" result is acceptable
and useful. **Never fabricate a result.** Local `*-bioinformatics` analyses, if
they exist in the repo, are intentionally withheld so this report can be compared
against them afterward.

## Required Output

### Executive Judgment

Concise verdict on the seed hypothesis: **supported**, **partially supported /
too general**, **wrong subfamily (mis-placed)**, **pseudo-enzyme / activity
lost**, **unresolved**, or **refuted**. Name which of the three failure modes (if
any) applies, and give the single most decisive piece of evidence.

### Independent Family/Function Assignment

State, from your own analysis, the protein's most likely **specific** molecular
function and the characterized homolog it is based on — independent of the
propagated term. Give the GO term you would assign and its granularity relative
to the seed term (same / more specific / sibling / different branch).

### Evidence Matrix

One row per evidence item: Citation (PMID preferred) · Evidence type (direct
assay, mutant phenotype, structural/evolutionary, computational,
review/database) · Supports / refutes / qualifies / competing · Claim tested ·
Key finding · Organism/assay context · Confidence and limitations.

### Active-Site / Placement Analysis

Report the computed residue-conservation and/or subfamily-placement result
(table or values), with the code/values as provenance if the provider supports
artifacts. State explicitly whether catalytic residues are intact.

### GO Curation Implications

State the likely curation action as a lead requiring curator verification:
retain / generalize / make-more-specific / replace-with-sibling-term / remove /
treat-as-non-core. Avoid "protein binding" as a final recommendation.

### Conflicts, Knowledge Gaps, Discriminating Tests

Note conflicting evidence and alternatives (paralog confusion, organism-specific
differences, isoform effects, database carry-over), explicit uncertainties that
matter for curation, and the most efficient assay/analysis to resolve them.

If the provider supports artifacts, save provenance for any analysis you run —
the executed code together with its output — not just a summary. Do not
synthesize a figure implying an analysis you did not run.


## Output

# AIGR Function-Inference Stress Test — PP_4594 (Q88E72) vs GO:0004123

**Target:** PP_4594 / UniProt Q88E72, *Pseudomonas putida* KT2440 (NCBITaxon:160488)
**Seed hypothesis (TreeGrafter/PANTHER, IEA, GO_REF:0000118):** PP_4594 has cystathionine gamma-lyase activity (GO:0004123, EC 4.4.1.1).

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED / sibling-activity ambiguity (failure mode 1 — granularity / family-vs-subfamily).**

PP_4594 is unambiguously a catalytically competent, fold-type I PLP-dependent enzyme of the **trans-sulfuration (Cys/Met metabolism) family, gamma subfamily**. The *catalytic machinery is intact* and the protein sits in the correct broad family, so the term is correct at the superfamily/catalytic-competence level. However, the **specific** assignment "cystathionine gamma-lyase" cannot be distinguished by sequence from its near-identical siblings **methionine gamma-lyase (EC 4.4.1.11)** and **cystathionine gamma-synthase (EC 2.5.1.48)**. There is no experimental assay of PP_4594.

- **Failure mode 2 (pseudo-enzyme): RULED OUT.** Catalytic PLP-Schiff-base Lys205 is conserved and correctly positioned; PLP cofactor annotated; fold intact.
- **Failure mode 3 (mis-placement into a distinct neighbor): RULED OUT.** It is clearly a *gamma*-subfamily enzyme, not a cystathionine beta-lyase (only 29% identity to MetC vs 39–44% to gamma members).
- **Failure mode 1 (granularity / sibling activity): APPLIES.** The propagated CGL term is one of several indistinguishable sibling activities.

**Single most decisive piece of evidence:** In a BLOSUM62 global alignment, PP_4594 is **equidistant (~40%) to all gamma-family activities**, with the single top characterized homolog being *methionine gamma-lyase* (44.3%), essentially tied with human CGL (43.9%) and above cystathionine gamma-synthase (38.8%) — i.e., sequence provides **no discrimination** of the exact EC, while the family literature states CGS and CGL "have highly similar amino acid sequences" (PMID 41562399).

---

## Independent Family / Function Assignment

- **Most likely specific function (from first principles):** a **pyridoxal-5′-phosphate-dependent, gamma-family carbon–sulfur lyase/synthase of the trans-sulfuration family** (PF01053 / IPR000277). The physiological substrate is not resolvable computationally.
- **Nearest characterized homolog:** *Pseudomonas putida* L-methionine gamma-lyase (P13254, 44.3% id), essentially tied with human cystathionine gamma-lyase (P32929, 43.9%).
- **GO term I would assign with confidence:** parent term **carbon–sulfur lyase activity (GO:0016846)** or the well-supported **pyridoxal phosphate binding (GO:0030170)** + **transsulfuration (GO:0019346)**. The seed term **GO:0004123** is of *correct granularity depth but names one specific sibling among several equally plausible ones* (same branch, specific; relationship to seed = **plausible but unverifiable sibling**).

---

## Evidence Matrix

| # | Citation / Source | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt Q88E72 (features/xrefs) | Database / computational | Qualifies | Is this a PLP trans-sulfuration enzyme? | PF01053 Cys_Met_Meta_PP; SSF53383 PLP transferase; PLP cofactor; catalytic Lys205 | Reviewed annotation (IEA/ARBA) | High for family; all IEA |
| 2 | This study — NW alignment, catalytic Lys | Computational / structural-evolutionary | Supports (not pseudo-enzyme) | Is catalysis retained? | Lys205 conserved & aligned to catalytic Lys of CGL/MGL/CGS/CBL; conserved S-x-S-K motif | BLOSUM62 global align | High |
| 3 | This study — %identity table | Computational / evolutionary | Qualifies / competing | Which sibling activity? | ~40% equidistant to MGL(44.3)/CGL(43.9)/OSHS(41.5)/CGS(38.8); CBL only 29.4% | Characterized refs | Decisive for "gamma not beta"; cannot pick EC |
| 4 | PANTHER PTHR11808:SF15 | Database (phylo) | Supports seed | Subfamily call | SF15 = cystathionine gamma-lyase | TreeGrafter source | Automated, same pipeline class |
| 5 | KEGG K01758 (PP_4594) | Database (ortholog) | Supports seed | KO call | K01758 = cystathionine gamma-lyase EC 4.4.1.1 | Independent of PANTHER | Automated, convergent |
| 6 | GenBank/EMBL AAN70167.1 name | Database | Competing | Product name | "cystathionine gamma-synthase" | Original author annotation | Conflicts with seed; unverified |
| 7 | KEGG ppu gene set | Database (genomic context) | Qualifies (supports catabolic CGL role) | Is PP_4594 the biosynthetic MetB? | No — dedicated metB=PP_0659 (K01739), metC=PP_4348 (K01760), metY=PP_2528 | *P. putida* KT2440 | Context argues PP_4594 is a "spare"/catabolic gamma enzyme |
| 8 | PMID 41562399 (2026) | Review / structural | Qualifies | CGS vs CGL separability | "CGS and CGL have highly similar amino acid sequences"; specificity set by few pocket residues (E55, V232) | *L. plantarum* | Supports sibling ambiguity |
| 9 | PMID 28106980 (2017) | Structural / mutational | Qualifies | CGL↔MGL interconversion | Human CGL scaffold engineered into an L-Met-degrading enzyme (MGL activity) | Human CGL | Shows CGL/MGL differ by few residues |

---

## Active-Site / Placement Analysis (provenance)

**Catalytic PLP-Schiff-base lysine (PP_4594 Lys205) — conserved across all references:**

| Reference (characterized) | PP_4594 K205 aligns to | Activity |
|---|---|---|
| human CGL (P32929) | **K** (K212) | cystathionine gamma-lyase |
| yeast CYS3 (P31373) | **K** | cystathionine gamma-lyase |
| *P. putida* MGL (P13254) | **K** | methionine gamma-lyase |
| *E. coli* MetB (P00935) | **K** | cystathionine gamma-synthase |
| *E. coli* MetC (P06721) | **K** | cystathionine beta-lyase |
| OSHS metZ (P55218) | **K** | O-succinylhomoserine sulfhydrylase |

Conserved PLP motif window (PP_4594 `DLVMHSASKYIGGHSDL` vs human CGL `DISMYSATKYMNGHSDV`) — the catalytic lysine and flanking PLP-binding scaffold are intact. **Catalytic residues are present and correctly spaced → the enzyme is catalytically competent (not a pseudo-enzyme).**

**Subfamily placement (global %identity, BLOSUM62 NW):**

```
MGL  P. putida   P13254  44.3%   (gamma: methionine gamma-lyase)  <-- top hit
CGL  human       P32929  43.9%   (gamma: cystathionine gamma-lyase = seed)
OSHS metZ        P55218  41.5%   (gamma: O-succinylhomoserine sulfhydrylase)
CGL  yeast CYS3  P31373  41.2%   (gamma: cystathionine gamma-lyase)
CGS  metB E.coli P00935  38.8%   (gamma: cystathionine gamma-synthase)
CBL  metC E.coli P06721  29.4%   (beta:  cystathionine beta-lyase)   <-- clearly excluded
```

Interpretation: gamma subfamily confirmed; exact sibling activity **unresolved** (all gamma activities within a 39–44% band, no outlier winner).

**Iteration 2 — UPGMA phylogenetic placement (10 taxa, BLOSUM62 NW distances):**

```
%identity of PP_4594 to reviewed references (sorted):
 CGS M. tuberculosis (P9WGB7)  45.7%   <-- single best hit = a gamma-SYNTHASE
 CGL rat           (P18757)    44.5%
 MGL P. putida     (P13254)    44.3%
 CGL human         (P32929)    43.9%
 CGL yeast CYS3    (P31373)    41.2%
 CGS E. coli metB  (P00935)    38.8%
 MGL Brevibacterium(A0A2H1K3G9)38.7%
 OAHS S. pombe     (O13326)    37.1%
 CBL E. coli metC  (P06721)    29.4%   <-- clear outgroup (beta-lyase)

UPGMA: PP_4594 first merges with MGL_Pputida (d=55.7), then with the
       CGL(mammal/yeast)+CGS(Mtb) clade (d=56.1); CBL is the outgroup.
```

The query sits **at the junction of the gamma clades with no clean assignment**: its single best sequence match is a cystathionine gamma-*synthase* (Mtb) and its nearest tree neighbour is a methionine gamma-*lyase* — neither is the seed's cystathionine gamma-*lyase*. This independently corroborates the sibling-activity ambiguity and again excludes the beta-lyase branch. (Caveat: UPGMA is an unrooted distance phenogram, not a bootstrapped ML tree.)

---

## GO Curation Implications

**Lead for curator verification:** **Treat GO:0004123 as a plausible-but-low-confidence computational sibling call; do NOT assert it as directly demonstrated.** Recommended actions, in order of preference:

1. **Generalize / safe retain:** keep the better-supported parent/companion terms — **pyridoxal phosphate binding (GO:0030170)**, **transsulfuration (GO:0019346)**, and, for MF, consider the parent **carbon–sulfur lyase activity (GO:0016846)** — all of which are robustly supported by fold and catalytic-residue evidence.
2. **If a specific MF term is required:** retain GO:0004123 **flagged IEA/low-confidence**, with an explicit note that methionine gamma-lyase (GO:0018826 / EC 4.4.1.11) and cystathionine gamma-synthase (GO:0003962 / EC 2.5.1.48) are indistinguishable siblings and that a separate *bona fide* metB (PP_0659) exists.
3. **Do not** upgrade the IEA to a more specific or experimental-equivalent evidence code without assay.

(Per instructions, "protein binding" is explicitly avoided as a recommendation.)

---

## Conflicts, Knowledge Gaps, Discriminating Tests

- **Database conflict:** PANTHER SF15 + KEGG K01758 say *cystathionine gamma-lyase*; GenBank product name says *cystathionine gamma-synthase*; the single closest characterized sequence is *methionine gamma-lyase*. These three sibling activities cannot be separated from sequence.
- **Paralog/context:** *P. putida* KT2440 encodes dedicated metB (PP_0659) and metC (PP_4348) for forward (biosynthetic) transsulfuration, so PP_4594 is most plausibly a **catabolic/spare gamma-elimination enzyme** — consistent with (but not proof of) a CGL/MGL role rather than biosynthetic CGS.
- **Key uncertainty for curation:** no experimental characterization of PP_4594 exists; all evidence is IEA/computational, and two of the supporting calls (PANTHER, KEGG) are themselves automated, so they are not independent confirmation of the TreeGrafter graft.
- **Most efficient discriminating test:** a simple in-vitro PLP enzyme assay on recombinant PP_4594 measuring (a) cystathionine → cysteine + α-ketobutyrate + NH3 (CGL), (b) L-methionine → methanethiol + α-ketobutyrate + NH3 (MGL), and (c) O-acyl-homoserine + cysteine → cystathionine (CGS). Alternatively, an AlphaFold-model active-site pocket comparison of the substrate-specificity residues (e.g., the positions equivalent to *L. plantarum* CGS E55/V232 per PMID 41562399) would computationally narrow the call.

---

## Supported / Refuted Hypotheses

- **Supported:** PP_4594 is a catalytically intact PLP trans-sulfuration enzyme of the gamma subfamily (not a pseudo-enzyme; not a beta-lyase).
- **Partially supported:** the seed GO:0004123 (CGL) — correct family and plausible, but one of several indistinguishable siblings; not directly demonstrated.
- **Refuted:** that the specific CGL EC can be confirmed from sequence alone (it cannot); that PP_4594 is the organism's biosynthetic cystathionine gamma-synthase (that is PP_0659).

## Limitations

Global NW identity with BLOSUM62 and a UPGMA distance phenogram (not a profile/HMM, bootstrapped ML tree, or structural pocket analysis); no biochemical assay accessible; AlphaFold pocket-residue comparison and a formal MSA of specificity residues were not run and would further refine the sibling call. The ~40–46% identities to all gamma siblings lie in the twilight zone for exact substrate/EC transfer, which is the fundamental reason the specific activity cannot be pinned computationally.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)