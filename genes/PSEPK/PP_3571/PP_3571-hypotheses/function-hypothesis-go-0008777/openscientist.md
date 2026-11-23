---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T22:40:15.017642'
end_time: '2026-10-14T23:05:17.775327'
duration_seconds: 1502.76
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: PP_3571
  gene_symbol: PP_3571
  uniprot_accession: Q88GZ4
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008777
  hypothesis_text: PP_3571 has acetylornithine deacetylase activity (GO:0008777).
  term_context: '- Term: acetylornithine deacetylase activity (GO:0008777)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/PP_3571/PP_3571-deep-research-openscientist.md'
  source_file: genes/PSEPK/PP_3571/PP_3571-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008777\n  label: acetylornithine deacetylase\
    \ activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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
citation_count: 2
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
- **Gene directory:** PP_3571
- **Gene symbol:** PP_3571
- **UniProt accession:** Q88GZ4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008777
- **Source file:** genes/PSEPK/PP_3571/PP_3571-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

PP_3571 has acetylornithine deacetylase activity (GO:0008777).

## Term and Decision Context

- Term: acetylornithine deacetylase activity (GO:0008777)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/PP_3571/PP_3571-deep-research-openscientist.md

## Source Context YAML

```yaml
term:
  id: GO:0008777
  label: acetylornithine deacetylase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **PP_3571 directly has the stated function**. Automated
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

# AIGR TreeGrafter Function-Inference Stress Test — PP_3571 (Q88GZ4)

**Target:** PP_3571 (UniProt **Q88GZ4**), *Pseudomonas putida* KT2440 (NCBITaxon:160488)
**Seed hypothesis (TreeGrafter/PANTHER, IEA, GO_REF:0000118):** PP_3571 has **acetylornithine deacetylase activity (GO:0008777)**
**Focus:** function_assignment · Hypothesis slug: function-hypothesis-go-0008777

---

## Summary

The seed hypothesis is **partially supported / too general, with paralog confusion** — it is not outright wrong, but it over-claims a specific substrate that the evidence assigns to a different gene. PP_3571 is unquestionably a member of the M20A (ArgE/DapE) metal-dependent acyl-amino-acid deacetylase family: its domain architecture (Pfam PF01546 Peptidase_M20 + PF07687 M20_dimer; InterPro IPR010169/IPR001261; PROSITE PS00759) is textbook, and a global alignment to *E. coli* ArgE shows **all seven catalytic/Zn²⁺-binding residues conserved with correct spacing**. The protein is therefore a genuine, catalytically competent enzyme — the pseudo-enzyme failure mode is firmly ruled out.

The problem is **which substrate** and **which paralog**. The single most decisive observation is that PANTHER's *own* fine-grained subfamily classifier — the very resource underneath the TreeGrafter graft — assigns PP_3571 to subfamily **PTHR43808:SF31 "N-acetyl-L-citrulline deacetylase"**, while its paralog **PP_5186 (Q88CJ5)** is assigned to **PTHR43808:SF1 "acetylornithine deacetylase."** The propagated GO:0008777 is the broad family-level term; the pipeline's own classifier places PP_3571 under a *sibling* activity, not the canonical ArgE one. This is corroborated by sequence identity: **PP_5186 is 49.6% identical to *E. coli* ArgE** (the signature of a true ortholog), whereas **PP_3571 is only 34.8%** and clusters at ~28–35% with *every* characterized M20A deacetylase, below the ~50–60% threshold needed to transfer substrate specificity by homology.

The failure mode is therefore **#1 (family-vs-subfamily granularity), compounded by paralog confusion**: TreeGrafter propagated a broad family term onto a divergent paralog whose specific substrate is unresolved, while the genome's true ArgE ortholog (PP_5186) went unlabeled with the specific term. This is reinforced by pathway context — *P. putida* runs the **cyclic ArgJ** arginine pathway, in which ArgJ/NAOGAT (not a standalone ArgE) performs acetyl-group recycling — so there is no pathway-level necessity forcing PP_3571 to be *the* acetylornithine deacetylase. The recommended curation action is to **generalize** GO:0008777 to a catalytic parent or **flag it low-confidence** on PP_3571 (with the sibling GO:0043909 as an equal alternative), and to re-anchor the specific ArgE annotation on PP_5186.

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED / TOO GENERAL (sibling-term risk) — with paralog confusion.**

- **Failure mode:** #1 (granularity, family-vs-subfamily), compounded by **paralog confusion**. Borderline #3 (within-superfamily misplacement) in that PP_3571 belongs to a sibling subfamily of the same fold. **NOT** #2 (pseudo-enzyme).
- **Single most decisive evidence:** PANTHER's own classifier splits the two paralogs — **PP_3571 → SF31 "N-acetyl-L-citrulline deacetylase"; PP_5186 → SF1 "acetylornithine deacetylase."** The emitted GO:0008777 is the ancestral family-level term, not PP_3571's subfamily-level assignment.

---

## Independent Family/Function Assignment

Independent of the propagated term, our own analysis places PP_3571 as follows:

- **Fold/family (high confidence):** Peptidase **M20A family, ArgE/DapE clan** — Pfam PF01546 + PF07687; InterPro IPR010169 (AcOrn-deacetyl) / IPR001261 (ArgE/DapE_CS); PROSITE PS00759 positive; a Zn-dependent di-metal exopeptidase/deacetylase.
- **Closest characterized homolog:** *E. coli* ArgE (acetylornithine deacetylase, EC 3.5.1.16, P23908) at **34.8% identity** — a *paralog-level*, not ortholog-level, match.
- **Most likely specific molecular function:** a metal-dependent **acyl-L-amino-acid deacetylase of unresolved exact substrate**. PANTHER assigns PP_3571 to **SF31 "N-acetyl-L-citrulline deacetylase"** (GO:0043909), a documented **sibling** activity, making that the best-supported *specific* lead. The canonical acetylornithine-deacetylase role for *P. putida* is better carried by paralog **PP_5186** (49.6% to ArgE).
- **GO term I would assign:** cautiously the catalytic parent **GO:0016811** (hydrolase acting on C–N bonds in linear amides) pending assay. GO:0008777 is defensible only as a *low-confidence, family-level* label; **GO:0043909 (sibling)** is an equally plausible specific alternative.
- **Granularity relative to seed term:** **sibling / parent** — not a confirmed exact match.

---

## Key Findings

### Finding 1 — PP_3571 is a catalytically intact M20A deacetylase, not a pseudo-enzyme

A global pairwise alignment (Needleman–Wunsch, BLOSUM62) of PP_3571 (391 aa) against *E. coli* ArgE (P23908) demonstrates that the complete di-zinc catalytic apparatus is present and correctly spaced. Every one of the seven ArgE catalytic and metal-binding residues has a conserved counterpart in PP_3571, and the domain architecture (PF01546 Peptidase_M20 catalytic domain plus PF07687 M20_dimer dimerization domain) is fully intact, with a positive PROSITE PS00759 (ARGE_DAPE_CPG2_2) signature. The practical consequence is important: the curation question is **not** about loss of catalysis. Whatever substrate PP_3571 prefers, it almost certainly hydrolyzes an N-acyl-amino-acid amide bond using an intact dinuclear metal center. Catalytic-residue conservation is **7/7 (100%)**.

### Finding 2 — PP_3571 is NOT the canonical acetylornithine deacetylase ortholog; PP_5186 is

A pairwise percent-identity matrix separates the two *P. putida* M20A paralogs decisively. **PP_5186 is 49.6% identical to *E. coli* ArgE** — the hallmark of a genuine functional ortholog — whereas **PP_3571 is only 34.8%** identical to the same reference, and is roughly *equidistant* (~30–35%) from canonical ArgE, from PP_5186 itself (32.8%), and from the sibling N-acetyl-L-citrulline deacetylase of *Xanthomonas* (29.8%). The fact that KEGG assigns the *same* orthology identifier **K01438 (EC 3.5.1.16) to both PP_3571 and PP_5186** is itself a diagnostic of family-level carry-over: an automated pipeline cannot tell the two apart, so the specific ArgE term was propagated onto the wrong (or at least an ambiguous) paralog. The identity gradient says the specific-substrate call belongs on PP_5186.

### Finding 3 — PANTHER's own subfamily classifier splits the paralogs into sibling activities

This is the pivotal finding. UniProt cross-references record two *different* PANTHER subfamily assignments inside the same family tree (PTHR43808). PP_3571 (Q88GZ4) maps to **PTHR43808:SF31 "N-ACETYL-L-CITRULLINE DEACETYLASE"**, while PP_5186 (Q88CJ5) maps to **PTHR43808:SF1 "ACETYLORNITHINE DEACETYLASE."** The seed term GO:0008777 was propagated from an ancestral node shared by both siblings, but the fine classifier that PANTHER itself provides disagrees with the propagated term for PP_3571 and names a *different specific substrate*. A broadened nearest-characterized-neighbor scan confirms the picture — ArgE *E. coli* 34.8%, ArgE *Enterobacter* 34.8%, PP_5186 32.8%, ACDase *Xanthomonas* 29.8%, ArgE *Arabidopsis* 28.2%, DapE *E. coli* 28.0%, CPG2 22.8% — all characterized M20A deacetylases cluster at 28–35% identity to PP_3571, below the ortholog-confidence threshold, whereas PP_5186 vs *E. coli* ArgE is 49.6%.

### Finding 4 — Pseudomonas uses the cyclic ArgJ pathway, weakening the need for a dedicated ArgE step

*P. putida* KT2440 encodes **ArgJ ornithine acetyltransferase (PP_1346, KEGG K00620)**. In the *cyclic* ornithine biosynthetic pathway used by pseudomonads, the acetyl group is recycled by ArgJ/NAOGAT — "the key deacetylating enzyme of the cyclic ornithine pathway" ([PMID: 42765862](https://pubmed.ncbi.nlm.nih.gov/42765862/)) — rather than removed by a standalone ArgE deacetylase. Complementation and hybridization work establishes that the *Pseudomonas*-type pathway is ArgJ-based and "reflects the divergent nature of the arginine biosynthetic pathway in these organisms" ([PMID: 1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/)). A dedicated ArgE acetylornithine-deacetylase step is therefore **not the principal arginine-biosynthetic route** in *Pseudomonas*. This removes the pathway-necessity argument that would otherwise make "an ArgE-family paralog here is probably the acetylornithine deacetylase" a safe default — and leaves the M20A paralogs free to have diverged toward other acyl-amino-acid substrates.

---

## Mechanistic Model / Interpretation

The findings assemble into a clean account of *why the graft erred and where the truth lies*:

```
                 PANTHER family PTHR43808  (ArgE/DapE M20A deacetylases)
                 GO:0008777 propagated from this ancestral node ──► emitted onto PP_3571 (IEA)
                                     │
             ┌───────────────────────┴───────────────────────┐
             │                                               │
      SF1  ACETYLORNITHINE DEACETYLASE            SF31  N-ACETYL-L-CITRULLINE DEACETYLASE
      = PP_5186 (Q88CJ5)                           = PP_3571 (Q88GZ4)  ◄── the actual query
      49.6% id to E. coli ArgE                      34.8% id to E. coli ArgE
      → true ArgE ortholog                          → divergent sibling paralog
```

- **Active site (F1):** intact → a real enzyme; closes off "pseudo-enzyme." The dispute is strictly about *which acyl-amino acid* it prefers.
- **Identity gradient (F2):** PP_5186 is the high-confidence ArgE; PP_3571 is a low-confidence, roughly-equidistant paralog. A family-level term propagated by homology will, by construction, land on both — but only one deserves the *specific* substrate call.
- **Subfamily split (F3):** the pipeline's own classifier resolves the ambiguity and places PP_3571 under the sibling N-acetyl-L-citrulline deacetylase subfamily — the datum that most directly contradicts the graft.
- **Pathway context (F4):** Pseudomonas doesn't rely on an ArgE deacetylase step at all, so there is no selective pressure forcing PP_3571 to be the acetylornithine deacetylase.

**Net interpretation:** GO:0008777 on PP_3571 is a *right-superfamily, wrong-substrate, wrong-paralog* annotation. It is not nonsense — the protein is a metal-dependent acyl-amino-acid deacetylase — but it over-claims a specific substrate that, on current evidence, belongs to PP_5186, while PP_3571's best specific lead is the citrulline-deacetylase sibling activity.

---

## Evidence Base

| # | Citation | Evidence type | Role | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|--------------|------|--------------|-------------|---------|--------------------------|
| 1 | UniProt Q88GZ4; InterPro IPR010169/IPR001261; Pfam PF01546/PF07687; PROSITE PS00759 | database/computational | Supports (fold) | Is it an M20A ArgE/DapE deacetylase? | Yes — M20 peptidase + dimerization domain; ArgE/DapE site profile positive | *P. putida* KT2440 | High for fold; silent on substrate |
| 2 | This report: NW/BLOSUM62 alignment to *E. coli* ArgE P23908 | computational / structural-evolutionary | Qualifies (rules out pseudo-enzyme) | Are catalytic/metal residues intact? | 7/7 conserved (H77, D79, D109, E141, E142, E169, H363), correct spacing | vs reviewed ArgE | High; residue mapping, no 3D refinement |
| 3 | This report: pairwise identity matrix (PP_3571, PP_5186, ArgE, ACDase) | computational | **Refutes/competing** | Is PP_3571 the canonical ArgE? | **No** — PP_5186 = 49.6% to ArgE (true ortholog); PP_3571 = 34.8% | KT2440 paralogs | High; identity is a proxy, not an assay |
| 4 | KEGG ppu:PP_3571 and ppu:PP_5186 (both K01438, EC 3.5.1.16) | database | Qualifies | KEGG substrate assignment | K01438 given to **both** paralogs → automated, non-discriminating | KEGG KO | Low independence (same family pipeline) |
| 5 | UniProt Q88GZ4 vs Q88CJ5 PANTHER cross-refs (SF31 vs SF1) | database/computational | **Refutes/competing** | Does the pipeline's own classifier agree with the propagated term? | **No** — PP_3571 = SF31 (citrulline deacetylase); PP_5186 = SF1 (acetylornithine deacetylase) | TreeGrafter/PANTHER | High internal consistency; still a prediction, not assay |
| 6 | [PMID: 42765862](https://pubmed.ncbi.nlm.nih.gov/42765862/) | review / primary (structure) | Supports pathway argument | Who deacetylates in the cyclic pathway? | ArgJ/NAOGAT is "the key deacetylating enzyme of the cyclic ornithine pathway" | Plant NAOGAT structure | Medium; general mechanism, not Pseudomonas-specific |
| 7 | [PMID: 1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/) | primary (complementation) | Supports pathway argument | Is the Pseudomonas pathway ArgJ-based/divergent? | Pathway "reflects the divergent nature of the arginine biosynthetic pathway in these organisms" | Neisseria/Pseudomonas argJ | Medium; argues divergence, not PP_3571 substrate directly |
| 8 | UniProt Q8P8J5 (ACDAS_XANCP) | review/database | Competing | Does a characterized sibling enzyme/term exist? | N-acetyl-L-citrulline deacetylase exists (GO:0043909); PP_3571 is 29.8% to it | *Xanthomonas campestris* | Medium; distant homolog |

**Literature notes.** [PMID: 42765862](https://pubmed.ncbi.nlm.nih.gov/42765862/) (*Plant NAOGAT (ArgJ) Structure Reveals Mechanism of Ornithine Biosynthesis…*) and [PMID: 1339419](https://pubmed.ncbi.nlm.nih.gov/1339419/) (*Sequence analysis and complementation studies of the argJ gene…*) jointly support the pathway-divergence argument (Finding 4): in the cyclic ornithine pathway that *Pseudomonas* uses, the deacetylation is done by ArgJ, not by a standalone ArgE, so there is no functional pressure forcing an ArgE-family paralog like PP_3571 to carry out canonical acetylornithine deacetylation. No retrievable paper directly assays PP_3571 or PP_5186; all specific-substrate calls here are computational/database-derived.

---

## Active-Site / Placement Analysis

Alignment-mapped catalytic residues (*E. coli* ArgE P23908 → PP_3571), all conserved:

| ArgE pos | ArgE res | PP_3571 pos | PP_3571 res | Role | Conserved |
|---------:|:--------:|------------:|:-----------:|------|:---------:|
| 80 | His | 77 | His | Zn²⁺ ligand | ✔ |
| 82 | Asp | 79 | Asp | active site | ✔ |
| 112 | Asp | 109 | Asp | Zn²⁺ ligand (bridging) | ✔ |
| 144 | Glu | 141 | Glu | active site / proton shuttle | ✔ |
| 145 | Glu | 142 | Glu | Zn²⁺ ligand | ✔ |
| 169 | Glu | 169 | Glu | Zn²⁺ ligand | ✔ |
| 355 | His | 363 | His | Zn²⁺ ligand | ✔ |

**Subfamily placement:**

| Metric | PP_3571 (Q88GZ4) | PP_5186 (Q88CJ5) |
|---|---|---|
| PANTHER subfamily | **PTHR43808:SF31** | **PTHR43808:SF1** |
| Subfamily label | N-acetyl-L-citrulline deacetylase | Acetylornithine deacetylase |
| % id to *E. coli* ArgE (P23908) | 34.8% | 49.6% |
| Role call | divergent sibling paralog | canonical ArgE ortholog |

**Conclusion:** Catalytic residues are **intact (7/7)** — catalytically competent, NOT a pseudo-enzyme. **Placement:** divergent paralog in the sibling subfamily; PP_5186 is the ArgE ortholog. *Provenance:* percent-identity values and residue mapping are computed outputs of Needleman–Wunsch/BLOSUM62 alignments; subfamily assignments are taken verbatim from UniProt/PANTHER cross-references for Q88GZ4 and Q88CJ5.

---

## GO Curation Implications

**Lead for curator verification: GENERALIZE or flag as low-confidence — make-more-specific is not warranted.**

- Do **not** assert the *specific* substrate acetyl-L-ornithine for PP_3571: it is a divergent paralog, the genuine ArgE ortholog is PP_5186, and *P. putida* runs the ArgJ cyclic pathway.
- Options: (a) **generalize** GO:0008777 to a catalytic parent (metal-dependent acyl-amino-acid deacetylase / GO:0016811) pending assay; or (b) **retain as low-confidence IEA** with an explicit note that the specific substrate is unverified and may be the **sibling** N-acetyl-L-citrulline deacetylase (**GO:0043909**, per PANTHER SF31). Avoid "protein binding" as a fallback — the protein is demonstrably catalytic.
- Re-anchor the exact-specificity acetylornithine-deacetylase annotation on **PP_5186 (Q88CJ5)**.
- For PP_3571, treat the acetylornithine-deacetylase function as **non-core / unverified**; the core evidence supports only "metal-dependent M20A acyl-amino-acid deacetylase."

---

## Limitations and Knowledge Gaps

- **No direct enzymology** exists for either PP_3571 or PP_5186; both specific-substrate calls are computational/database-derived.
- **Identity cannot fix substrate:** residue-level conservation confirms the fold and active site but cannot discriminate acetylornithine vs acetylcitrulline vs other N-acyl substrates — M20A enzymes are broadly promiscuous across N-acetyl/N-succinyl amino acids and dipeptides.
- **Single-sequence pairwise identities** were used (not a full MSA/phylogenetic tree); AlphaFold substrate-pocket geometry was not re-refined here.
- **Subfamily labels are predictions**, not experimental assignments, for these exact proteins; the ~30% identity to the characterized *Xanthomonas* ACDase is modest.
- **Database carry-over** (identical KEGG K01438/EC on both paralogs) is a warning sign, not independent evidence.
- **GO:0008777 vs GO:0043909 cannot be decided from sequence alone.**

---

## Proposed Follow-up Experiments / Actions

1. **Direct in-vitro deacetylase assay (decisive).** Express and purify recombinant PP_3571 (and PP_5186) and assay against a substrate panel — N-α-acetyl-L-ornithine, N-acetyl-L-citrulline, N-succinyl-diaminopimelate, and other N-acetyl amino acids — with Zn²⁺/Co²⁺ cofactor, to measure substrate preference directly.
2. **Structural pocket comparison (runnable computationally).** Superpose AlphaFold models of PP_3571, *E. coli* ArgE, and *Xanthomonas* ACDase, focusing on the specificity-determining residues lining the substrate side-chain pocket (ornithine vs citrulline differ by the δ-ureido group).
3. **In-vivo genetics.** ΔPP_3571 and ΔPP_5186 single/double knockouts in *P. putida*, scored for arginine auxotrophy and cross-complementation of an *E. coli* ΔargE strain, to assign the in-vivo acetylornithine-deacetylase role between the paralogs.
4. **Curation action now.** Flag GO:0008777 on PP_3571 as low-confidence/too-general, record GO:0043909 as a competing sibling, and route the specific ArgE annotation to PP_5186.

---

*Report produced by autonomous discovery agent over 3 iterations; 4 findings confirmed; 2 primary papers reviewed. All percent-identity and active-site values are computed provenance from Needleman–Wunsch/BLOSUM62 alignments; subfamily assignments are taken verbatim from UniProt/PANTHER cross-references.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)