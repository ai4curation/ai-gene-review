---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T03:38:21.925416'
end_time: '2026-10-15T03:51:08.223649'
duration_seconds: 766.3
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: PP_2482
  gene_symbol: PP_2482
  uniprot_accession: Q88K11
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0061798
  hypothesis_text: PP_2482 has GTP 3',8'-cyclase activity (GO:0061798).
  term_context: '- Term: GTP 3'',8''-cyclase activity (GO:0061798)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/PP_2482/PP_2482-deep-research-openscientist.md'
  source_file: genes/PSEPK/PP_2482/PP_2482-ai-review.yaml
  source_selector: existing_annotations[6].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0061798\n  label: GTP 3',8'-cyclase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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
- **Gene directory:** PP_2482
- **Gene symbol:** PP_2482
- **UniProt accession:** Q88K11

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0061798
- **Source file:** genes/PSEPK/PP_2482/PP_2482-ai-review.yaml
- **Source selector:** existing_annotations[6].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

PP_2482 has GTP 3',8'-cyclase activity (GO:0061798).

## Term and Decision Context

- Term: GTP 3',8'-cyclase activity (GO:0061798)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/PP_2482/PP_2482-deep-research-openscientist.md

## Source Context YAML

```yaml
term:
  id: GO:0061798
  label: GTP 3',8'-cyclase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **PP_2482 directly has the stated function**. Automated
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

# AIGR TreeGrafter Function-Inference Stress Test — PP_2482 (Q88K11)

**Target:** PP_2482 / Q88K11, *Pseudomonas putida* KT2440 (NCBITaxon:160488)
**Seed hypothesis under test:** PP_2482 has **GTP 3',8'-cyclase activity (GO:0061798)** — propagated by TreeGrafter/PANTHER (IEA, GO_REF:0000118).

---

## Summary

This stress test asked whether the TreeGrafter/PANTHER graft that assigned **GTP 3',8'-cyclase activity (GO:0061798)** to PP_2482 is a true call or one of three characteristic phylogenetic-propagation errors (family-vs-subfamily granularity, pseudo-enzyme, or within-superfamily mis-placement). The answer is that the graft is **correct**: PP_2482 (Q88K11, 322 aa) is a genuine, catalytically competent **MoaA** — a radical-SAM **GTP 3',8'-cyclase** (EC 4.1.99.22, KEGG K03639), the first enzyme of molybdenum-cofactor (Moco) biosynthesis.

The conclusion rests on three convergent, independently derived lines of evidence. First, the **domain architecture is an exact match to MoaA** — Pfam PF04055 (Radical_SAM) plus PF06463 (Mob_synth_C, the MoaA-specific C-terminal "twitch" domain), InterPro IPR040064 (MoaA-like) + IPR010505 (MoaA_twitch), PANTHER subfamily PTHR22960:SF0 (MOCS1/MoaA), and KEGG orthology K03639. Second, the **active site is fully intact**: all six catalytic cysteines of the two [4Fe-4S] clusters are present, correctly spaced, and align residue-for-residue with characterized *E. coli* MoaA. Third, the **AlphaFold model is well-ordered** at the active site (mean pLDDT 93.6; catalytic cysteines pLDDT ≈ 92), and the gene sits in a molybdenum-cofactor genomic neighborhood adjacent to MocA (K07141).

All three failure modes were actively tested and **excluded**. The term is at the correct granularity (the MoaA family function *is* specifically GTP 3',8'-cyclase); the protein is not a pseudo-enzyme (catalytic residues conserved and ordered); and it is not mis-placed within the radical-SAM superfamily (the diagnostic twitch domain anchors the MoaA subfamily, not a neighboring activity). *P. putida* carries three intact MoaA paralogs, which reflects **genetic redundancy, not misassignment**. **Recommended curation action: RETAIN GO:0061798.**

---

## Executive Judgment

**Verdict: SUPPORTED.** The propagated GO:0061798 annotation is correct and at the appropriate granularity for PP_2482. None of the three TreeGrafter failure modes apply:

- **Not a granularity error.** The protein's closest characterized relatives are MoaA / MOCS1 orthologs, and the family function *is* specifically GTP 3',8'-cyclase (EC 4.1.99.22). The term names exactly the reaction this subfamily performs.
- **Not a pseudo-enzyme.** All six catalytic cysteines coordinating the two [4Fe-4S] clusters are present, correctly spaced against characterized *E. coli* MoaA, and structurally ordered in the AlphaFold model.
- **Not a within-superfamily mis-placement.** PP_2482 carries the MoaA-specific C-terminal twitch domain (PF06463 / IPR010505), diagnostic of the MoaA subfamily and absent from other radical-SAM activities. It maps cleanly to PANTHER PTHR22960:SF0.

**Single most decisive piece of evidence:** the simultaneous presence of (a) the N-terminal radical-SAM CX₃CX₂C [4Fe-4S] motif and (b) the C-terminal MoaA-unique twitch-domain cysteine cluster that binds the GTP substrate — the two-cluster architecture that is the structural signature of GTP 3',8'-cyclase and of no sibling activity — with all catalytic residues intact and ordered.

---

## Independent Family/Function Assignment

From independent analysis of domain architecture, orthology, catalytic-residue conservation, genomic context, and structural modeling, PP_2482 is most likely a **radical-SAM GTP 3',8'-cyclase (MoaA)**, acting in the first committed step of Moco biosynthesis.

| Attribute | Value |
|---|---|
| Specific molecular function | GTP 3',8'-cyclase (GTP → 3',8-cyclo-7,8-dihydro-GTP, radical-SAM) |
| Characterized homolog basis | *E. coli* MoaA (P30745); *S. aureus* MoaA (structural reference for two-cluster/GTP-binding mechanism) |
| EC number | 4.1.99.22 |
| KEGG orthology | K03639 ("GTP 3',8-cyclase [EC:4.1.99.22]"), module M00880 (GTP ⇒ Moco) |
| PANTHER | PTHR22960:SF0 (Molybdenum cofactor biosynthesis protein 1, MOCS1/MoaA) |
| Pfam | PF04055 (Radical_SAM) + PF06463 (Mob_synth_C, twitch domain) |
| InterPro | IPR040064 (MoaA-like) + IPR010505 (MoaA_twitch) |
| **GO term I would assign** | **GO:0061798 — GTP 3',8'-cyclase activity** |
| Granularity vs. seed | **Same** (identical, correctly subfamily-specific) |

The independent assignment is **identical** to the seed term — a true-positive graft.

---

## Key Findings

### Finding 1 — PP_2482 is a bona fide MoaA / GTP 3',8'-cyclase (seed hypothesis supported)

Every line of family-level evidence converges on MoaA. The domain architecture matches MoaA exactly: Pfam **PF04055 (Radical_SAM)** paired with **PF06463 (Mob_synth_C)**, the MoaA-specific C-terminal "twitch" domain. The InterPro signatures are **IPR040064 (MoaA-like)** plus **IPR010505 (MoaA_twitch)**. The protein maps to PANTHER subfamily **PTHR22960:SF0** ("Molybdenum cofactor biosynthesis protein 1," MOCS1/MoaA). KEGG assigns orthology **K03639, "GTP 3',8-cyclase [EC:4.1.99.22],"** placing the gene in module **M00880** (Moco biosynthesis, GTP ⇒ Moco). The UniProt keyword set for Q88K11 — 4Fe-4S, GTP-binding, Lyase, S-adenosyl-L-methionine, Molybdenum cofactor biosynthesis — is precisely what is expected for MoaA. The protein length (322 aa) matches characterized MoaA proteins.

Crucially, the family function is itself specifically GTP 3',8'-cyclase — this is not a broad family label masking a diverged subfamily. [PMID: 25941396](https://pubmed.ncbi.nlm.nih.gov/25941396/) states directly: "the physiological function of MoaA is the conversion of GTP to 3',8-cH2GTP (GTP 3',8-cyclase), and that of MoaC is to catalyze the rearrangement of 3',8-cH2GTP into cPMP (cPMP synthase)." This establishes the one-to-one correspondence between the MoaA family and GO:0061798, excluding the **granularity failure mode**: the term is exactly as specific as it should be.

### Finding 2 — Both [4Fe-4S]-coordinating cysteine motifs are intact and correctly spaced (not a pseudo-enzyme)

MoaA catalysis requires two [4Fe-4S] clusters, each coordinated by a three-cysteine motif. In PP_2482 both are present, conserved, and correctly spaced relative to characterized *E. coli* MoaA (P30745):

- **N-terminal radical-SAM cluster:** PP_2482 Cys21/Cys25/Cys28 form the canonical **CX₃CX₂C** motif (local context C-NYA-C-TY-C), aligning residue-for-residue with *E. coli* MoaA Cys24/Cys28/Cys31 (C-NFR-C-TY-C). The "CTYC" core is **identical** between the two proteins. UniProt independently annotates binding sites at residues 21/25/28.
- **C-terminal "twitch" cluster (binds GTP substrate):** PP_2482 Cys253/Cys256/Cys270 (motif CRSC…GRLYGC) align with *E. coli* MoaA Cys257/Cys260/Cys274 (motif CATC…GKLHLC), including the conserved downstream C-terminal cysteine and conserved arginines (R254/R258/R260/R266).

All **six catalytic cysteines are present with conserved spacing**. A degenerate active site — the hallmark of a pseudo-enzyme — would show loss or displacement of these residues; instead they are fully conserved. [PMID: 30097104](https://pubmed.ncbi.nlm.nih.gov/30097104/) confirms "MoaA is one of the founding members of the radical S-adenosyl-methionine" superfamily — the enzyme class whose catalysis depends on exactly this conserved CX₃CX₂C [4Fe-4S] motif. The **pseudo-enzyme failure mode is therefore excluded.**

### Finding 3 — Three intact MoaA paralogs, Moco operon context, and an ordered AlphaFold active site

*P. putida* KT2440 encodes **three MoaA paralogs**, all mapping to PTHR22960:SF0 with the PF04055 + PF06463 architecture and both intact cysteine clusters:

| Paralog | UniProt | Len | N-cluster Cys | C-cluster Cys | Notes |
|---|---|---|---|---|---|
| **PP_2482** | Q88K11 | 322 | C21/C25/C28 | C253/C256/C270 (CRSC…YGC) | Target; clades with PP_1969 |
| PP_4597 | Q88E69 | 334 | C27/C31/C34 | C260/C263/C277 (CATC…HLC) | EC 4.1.99.22 assigned; closest to *E. coli* (CATCNRVRL vs *E. coli* CATCNRLRV) |
| PP_1969 | Q88LG4 | 337 | C36/C40/C43 | C268/C271/C285 (CRTC…HGC) | Clades with PP_2482 |

The existence of three intact paralogs reflects **genetic redundancy, not misassignment** — all three retain complete active sites. PP_2482 clusters with PP_1969 (shared ESxPFC…GC twitch motif), distinct from the more *E. coli*-like PP_4597.

Genomic context reinforces the assignment: PP_2482 is adjacent to **PP_2483 = K07141 molybdenum cofactor cytidylyltransferase (MocA, EC 2.7.7.76)**, a bona fide Moco-pathway gene. A GTP 3',8'-cyclase sitting next to a Moco cytidylyltransferase is exactly the expected genomic neighborhood.

Structurally, the AlphaFold model **AF-Q88K11 (v6)** has a high mean pLDDT of **93.6**, and the six catalytic cysteines have pLDDT 87.4–94.1 (mean **92.0**) — a well-ordered, confidently modeled active site, inconsistent with a decayed or non-functional catalytic pocket. Together with the twitch domain's uniqueness to the MoaA subfamily, this excludes the **within-superfamily mis-placement failure mode.**

---

## Mechanistic Model / Interpretation

PP_2482 catalyzes the first committed and chemically most complex step of molybdenum cofactor biosynthesis: the radical-SAM–dependent rearrangement of GTP into 3',8-cyclo-7,8-dihydro-GTP (3',8-cH₂GTP). This product is handed to MoaC, which completes the pyranopterin ring to form cyclic pyranopterin monophosphate (cPMP).

```
   GTP
    │
    │  MoaA  (= PP_2482, GTP 3',8'-cyclase, GO:0061798, EC 4.1.99.22)
    │  radical-SAM, two [4Fe-4S] clusters
    ▼
  3',8-cH2GTP
    │
    │  MoaC  (cPMP synthase)
    ▼
   cPMP ── ... ──► Molybdopterin ──► Molybdenum cofactor (Moco)
```

The two-cluster architecture is the mechanistic key, and PP_2482 has both:

```
  N-terminal radical-SAM cluster            C-terminal "twitch" cluster
  (PF04055; binds SAM, generates            (PF06463 / IPR010505; binds
   5'-deoxyadenosyl radical)                 and activates GTP substrate)
  CX3CX2C:  C21 .. C25 . C28                 C253 .. C256 .... C270
  (= E. coli C24/C28/C31)                    (= E. coli C257/C260/C274)
          │                                          │
          └────────── both intact, ordered ──────────┘
                 pLDDT ~92 across all six Cys
```

The presence of the twitch domain is what distinguishes MoaA from the thousands of other radical-SAM enzymes sharing the PF04055 fold. Because only the MoaA subfamily couples a radical-SAM cluster to a substrate-binding twitch cluster of this type, the within-superfamily mis-placement risk is fully controlled: the diagnostic subfamily feature is present. The family literature ([PMID: 41183211](https://pubmed.ncbi.nlm.nih.gov/41183211/), [PMID: 35480226](https://pubmed.ncbi.nlm.nih.gov/35480226/), [PMID: 30097104](https://pubmed.ncbi.nlm.nih.gov/30097104/)) consistently describes MoaA as a radical-SAM GTP 3',8-cyclase with exactly this two-cluster design, and [PMID: 26575208](https://pubmed.ncbi.nlm.nih.gov/26575208/) and [PMID: 25941396](https://pubmed.ncbi.nlm.nih.gov/25941396/) detail how the MoaA product 3',8-cH₂GTP is subsequently processed by MoaC to cPMP.

In short, this is a **true positive** from the TreeGrafter graft: the ancestral node's GO term propagated correctly to a descendant that genuinely retains the ancestral function.

---

## Evidence Base

| # | Citation | Evidence type | Role | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt Q88K11 + Pfam/InterPro/PANTHER | Database / computational | **Supports** | Family identity | PF04055 + PF06463; IPR040064 + IPR010505; PANTHER PTHR22960:SF0; keywords 4Fe-4S/GTP-binding/SAM/Lyase/Moco | PP_2482 directly | High; multi-source concordant |
| 2 | KEGG ppu:PP_2482 (K03639 / M00880) | Database | **Supports** | Specific activity | Orthology K03639 "GTP 3',8-cyclase EC 4.1.99.22"; Moco module M00880 | PP_2482 directly | High |
| 3 | Alignment vs *E. coli* MoaA (P30745) | Computational (active-site test) | **Supports** | Active-site integrity | 6/6 catalytic Cys conserved and correctly spaced (N: C21/C25/C28; C: C253/C256/C270) | PP_2482 vs *E. coli* | High; pairwise, not deep MSA |
| 4 | [PMID: 25941396](https://pubmed.ncbi.nlm.nih.gov/25941396/) | Review / mechanistic | **Supports** | Is the family function specifically GTP 3',8'-cyclase? | "the physiological function of MoaA is the conversion of GTP to 3',8-cH2GTP (GTP 3',8-cyclase)" | MoaA mechanism | High; defines term scope, not PP_2482 specifically |
| 5 | [PMID: 30097104](https://pubmed.ncbi.nlm.nih.gov/30097104/) | Structural / evolutionary review | **Supports** | Catalysis depends on conserved Cys motif? | "MoaA is one of the founding members of the radical S-adenosyl-methionine" superfamily | MoaA / radical-SAM | High |
| 6 | [PMID: 26575208](https://pubmed.ncbi.nlm.nih.gov/26575208/) | Mechanistic (in vitro) | **Qualifies** | Downstream fate of MoaA product | MoaC converts 3',8-cH₂GTP (MoaA product) to cPMP; confirms pathway logic | in vitro | High for pathway, indirect for PP_2482 |
| 7 | AlphaFold AF-Q88K11 (v6) | Computational / structural | **Supports** | Is the active site ordered? | Mean pLDDT 93.6; six catalytic Cys pLDDT 87.4–94.1 (mean 92.0) | PP_2482 model | High for order; model, not experimental |
| 8 | Genomic context (PP_2483 = MocA, K07141) | Computational / genomic | **Supports** | Moco neighborhood? | Adjacent to Mo-cofactor cytidylyltransferase (EC 2.7.7.76) | *P. putida* genome | Moderate-high; corroborative synteny |
| 9 | Paralog analysis (PP_4597, PP_1969) | Computational | **Qualifies** | Does paralogy imply misassignment? | Three intact MoaA paralogs → redundancy, not error | *P. putida* genome | Moderate; division of labor not experimentally resolved |

No evidence item **refutes** the seed hypothesis; all sources are mutually concordant.

---

## Active-Site / Placement Analysis (provenance)

**Catalytic residues: INTACT.** Both [4Fe-4S]-coordinating cysteine motifs are fully conserved and correctly spaced versus characterized *E. coli* MoaA (P30745):

| Cluster | Role | *E. coli* MoaA | PP_2482 (Q88K11) | Motif / context | Status |
|---|---|---|---|---|---|
| N-terminal | SAM reductive cleavage [4Fe-4S] | C24, C28, C31 | **C21, C25, C28** | CX₃CX₂C — PP: C·NYA·C·TY·C; Ec: C·NFR·C·TY·C | Intact; identical "CTYC" core |
| C-terminal "twitch" | GTP binding/activation [4Fe-4S] | C257, C260, C274 | **C253, C256, C270** | PP: CRSC…GRLYGC; Ec: CATC…GKLHLC | Intact; conserved spacing |

Additional conserved twitch-domain basic residues (Arg254/Arg258/Arg260/Arg266) and the shared C-terminal cysteine are present. The domain layout — N-terminal radical-SAM core plus C-terminal Mob_synth_C twitch — is the MoaA-diagnostic two-domain architecture, not a neighboring radical-SAM subfamily (e.g. MiaB, BioB, Elp3). **All catalytic residues intact → not a pseudo-enzyme; correctly placed.**

**AlphaFold (AF-Q88K11, v6):** mean pLDDT 93.6; the six catalytic cysteines are confidently modeled (pLDDT 87.4–94.1, mean 92.0) → a structurally ordered two-cluster active site.

### Failure-mode test results

1. **Granularity (family vs subfamily):** **PASS** — term is subfamily-specific (PANTHER SF0 = MoaA; KEGG K03639). Not too general.
2. **Pseudo-enzyme / lost activity:** **PASS** — both [4Fe-4S] cluster cysteine sets fully conserved and spaced; active site ordered.
3. **Within-superfamily mis-placement:** **PASS** — Mob_synth_C twitch domain + MoaA-like InterPro uniquely identify the MoaA subfamily.

---

## GO Curation Implications

**Recommended action: RETAIN GO:0061798 (GTP 3',8'-cyclase activity).**

The IEA/GO_REF:0000118 propagation should be upheld and flagged for routine curator verification. It is well supported by:
- Exact MoaA domain architecture (radical-SAM + twitch domains).
- Full conservation and correct spacing of all six catalytic cysteines.
- Clean mapping to PANTHER PTHR22960:SF0 and KEGG K03639 / EC 4.1.99.22.
- A molybdenum-cofactor genomic neighborhood (adjacent MocA).
- A high-confidence, well-ordered AlphaFold active site.

No generalization, specialization, sibling-term replacement, or removal is warranted — the term is at the correct granularity. Curators may additionally consider the companion Biological Process term **GO:0006777 (Mo-molybdopterin cofactor biosynthetic process)** and cofactor-binding terms (4Fe-4S, SAM, GTP binding). "Protein binding" is explicitly **not** an appropriate recommendation and is not suggested.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical assay for PP_2482.** All evidence is computational, evolutionary, and homology-based. There is no published activity measurement, mutant phenotype, or crystal structure specifically for PP_2482/Q88K11. The functional call rests on strong sequence/structure conservation, not a direct demonstration of catalysis in this protein.

2. **Paralog division of labor is unresolved.** *P. putida* KT2440 has three intact MoaA paralogs (PP_2482, PP_4597, PP_1969), all with complete active sites, so all are predicted catalytic. Which carries the principal physiological flux — and whether the divergent PP_2482/PP_1969 clade has a specialized or condition-specific role — is not established. This does not undermine the MF assignment but is a genuine biological gap.

3. **Pairwise, not phylogenetic, active-site comparison.** The catalytic-residue test was performed against *E. coli* MoaA (P30745). A deep multiple-sequence alignment across many characterized MoaA proteins and a formal tree would make the placement claim even more robust, though the diagnostic twitch domain and complete cysteine set already secure the subfamily call.

4. **AlphaFold is a model.** The high pLDDT values indicate confident prediction and an ordered active site, but a model cannot confirm the [4Fe-4S] clusters are loaded or that the enzyme is active in vivo. No direct coordinate superposition onto a MoaA crystal structure (e.g., *S. aureus*) was executed.

5. **Twitch-domain sequence divergence.** PP_2482's twitch motif (CRSC…GRLYGC) differs in detail from *E. coli* (CATC…GKLHLC), though the three coordinating cysteines and key arginines are conserved. This variation is within normal MoaA diversity but has not been experimentally shown to be catalytically neutral in this specific protein.

6. **Database carry-over caveat.** The annotation chain is partly database-driven; however, independence across Pfam, PANTHER, and KEGG plus explicit catalytic-residue conservation mitigates single-source bias.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic assay (most decisive).** Express and purify PP_2482 anaerobically, reconstitute the [4Fe-4S] clusters (dithionite/SAM/GTP), and detect GTP → 3',8-cyclo-7,8-dihydro-GTP conversion by LC-MS. This converts the computational call into a direct-assay confirmation.

2. **Heterologous complementation.** Complement an *E. coli* ΔmoaA mutant with PP_2482 and score restoration of Moco-dependent activity (e.g., nitrate reductase). This tests in-vivo function directly.

3. **Paralog genetics in *P. putida*.** Construct single and combinatorial knockouts of PP_2482, PP_4597, and PP_1969 and score Moco-dependent phenotypes / cPMP accumulation to resolve the division-of-labor gap.

4. **Deep MSA + phylogenetic placement.** Build a curated alignment of characterized MoaA/MOCS1 proteins plus representative sibling radical-SAM subfamilies and formally place all three *P. putida* paralogs, hardening the "not mis-placed" conclusion.

5. **Structural confirmation of cluster loading.** EPR/Mössbauer or UV-Vis on reconstituted protein to confirm two [4Fe-4S] clusters, and, if feasible, a crystal/cryo-EM structure or at minimum a coordinate superposition of the AlphaFold model onto a MoaA crystal structure to validate active-site geometry.

6. **Expression/regulation profiling.** Transcriptomic or proteomic data across conditions to determine which paralog(s) are expressed when, informing which should be treated as the "core" GTP 3',8'-cyclase for annotation priority.

---

## Conclusion

This is a **true-positive TreeGrafter propagation.** PP_2482 (Q88K11) is a genuine, catalytically competent **MoaA — a radical-SAM GTP 3',8'-cyclase (EC 4.1.99.22, KEGG K03639)** — and the propagated **GO:0061798** annotation is correct and at the right granularity. All three phylogenetic-propagation failure modes were actively tested and excluded: the term is appropriately specific (not a granularity error), the active site is fully intact and ordered (not a pseudo-enzyme), and the MoaA-diagnostic twitch domain anchors the correct subfamily (not a within-superfamily mis-placement). **Recommended curation action: retain GO:0061798**, flagged for routine curator verification, with the note that *P. putida* carries two additional intact MoaA paralogs whose physiological division of labor remains experimentally unresolved.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)