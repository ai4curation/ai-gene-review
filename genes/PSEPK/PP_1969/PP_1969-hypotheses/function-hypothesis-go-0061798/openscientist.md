---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T22:40:15.011877'
end_time: '2026-10-14T22:59:08.722675'
duration_seconds: 1133.71
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: PP_1969
  gene_symbol: PP_1969
  uniprot_accession: Q88LG4
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0061798
  hypothesis_text: PP_1969 has GTP 3',8'-cyclase activity (GO:0061798).
  term_context: '- Term: GTP 3'',8''-cyclase activity (GO:0061798)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/PP_1969/PP_1969-deep-research-openscientist.md'
  source_file: genes/PSEPK/PP_1969/PP_1969-ai-review.yaml
  source_selector: existing_annotations[6].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0061798\n  label: GTP 3',8'-cyclase activity\n\
    evidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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
- **Gene directory:** PP_1969
- **Gene symbol:** PP_1969
- **UniProt accession:** Q88LG4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0061798
- **Source file:** genes/PSEPK/PP_1969/PP_1969-ai-review.yaml
- **Source selector:** existing_annotations[6].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

PP_1969 has GTP 3',8'-cyclase activity (GO:0061798).

## Term and Decision Context

- Term: GTP 3',8'-cyclase activity (GO:0061798)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/PP_1969/PP_1969-deep-research-openscientist.md

## Source Context YAML

```yaml
term:
  id: GO:0061798
  label: GTP 3',8'-cyclase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **PP_1969 directly has the stated function**. Automated
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

# AIGR TreeGrafter Stress Test — PP_1969 (Q88LG4), GO:0061798 GTP 3',8'-cyclase

## Executive Judgment

**Verdict: SUPPORTED.** PP_1969 (UniProt Q88LG4, *Pseudomonas putida* KT2440) is a
bona fide **MoaA** ortholog, and GO:0061798 (**GTP 3',8'-cyclase activity**) is the
correct, appropriately *specific* molecular function. None of the three
characteristic TreeGrafter failure modes apply:

1. **Granularity — PASS.** GO:0061798 is the subfamily-specific MoaA term (not a
   broad family label). The protein maps to PANTHER **PTHR22960:SF0**
   ("molybdenum cofactor biosynthesis protein 1" = MoaA/MOCS1A).
2. **Pseudo-enzyme — PASS.** All six catalytic cysteines of **both** [4Fe-4S]
   clusters are conserved and correctly spaced. The active site is intact.
3. **Within-superfamily mis-placement — PASS.** The diagnostic MoaA C-terminal
   **"twitch" domain** (Pfam PF06463 / InterPro IPR010505) is present, placing it
   in the true MoaA subfamily rather than a neighboring radical-SAM activity.

**Single most decisive evidence:** 1:1 conservation of the C-terminal
GTP-binding [4Fe-4S] cluster II ligand cysteines (PP_1969 Cys268/Cys271/Cys285 ↔
E. coli MoaA Cys257/Cys260/Cys274) within the conserved twitch motif — this
cluster directly anchors the GTP substrate and defines GTP 3',8'-cyclase catalysis.

**Paralogy caveat (resolved, Iteration 2):** *P. putida* KT2440 carries **three**
MoaA-type radical-SAM paralogs — Q88E69 (the gene formally named *moaA*), Q88K11,
and Q88LG4/PP_1969. This is a textbook failure-mode-1 trap, but it does **not**
overturn the call: PP_1969 is actually the paralog **most** similar to the
characterized *E. coli* MoaA (40.9% vs 37.5% for the named *moaA*), and all three
paralogs retain the full six-cysteine active site. PP_1969's assignment is
therefore well justified; the multiplicity reflects lineage-specific MoaA
expansion, not functional reassignment.

## Independent Family/Function Assignment

- **Most likely specific function:** GTP 3',8'-cyclase (MoaA), first step of
  molybdopterin (Moco) biosynthesis: 5'-GTP → 3',8-cyclo-7,8-dihydro-GTP
  (3',8-cH₂GTP), a radical-SAM reaction using two [4Fe-4S] clusters.
- **Characterized homolog basis:** *E. coli* MoaA (P30745), 40.0% identity over
  315 aligned residues; mechanism/structure from *S. aureus*/E. coli MoaA
  (Hänzelmann & Schindelin).
- **GO term I would assign:** GO:0061798 (GTP 3',8'-cyclase activity).
  **Granularity vs seed: SAME** (correct and specific).
- Supporting terms consistent with assignment: GO:0051539 (4Fe-4S binding),
  GO:0006777 (Mo-molybdopterin cofactor biosynthetic process).

## Evidence Matrix

| Citation | Evidence type | Call | Claim tested | Key finding | Context | Confidence/limits |
|---|---|---|---|---|---|---|
| PMID 16632608 (Hänzelmann & Schindelin 2006) | Structural/biochemical (direct) | Supports | MoaA = GTP→precursor-Z enzyme using two [4Fe-4S] clusters | MoaA binds 5'-GTP at C-terminal [4Fe-4S] cluster; N-terminal cluster cleaves SAM | *E. coli*/*S. aureus* MoaA, crystal + biochem | High; reference enzyme, not PSEPK directly |
| PMID 41183211 (Pang et al. 2025) | Mechanistic (direct) | Supports | MoaA is a radical SAM GTP 3',8-cyclase | Confirms current term/mechanism nomenclature | Radical SAM GTP 3',8-cyclase | High |
| UniProt Q88LG4 xrefs | Review/database + computational | Supports | Domain architecture = MoaA | PF04055 + PF06463; IPR040064 MoaA-like; IPR010505 twitch; PANTHER SF0 | PSEPK PP_1969 | High |
| This report: NW alignment vs P30745 | Computational (evolutionary) | Supports | Ortholog with intact active site | 40.9% id; 6/6 cluster cysteines conserved & spaced | PP_1969 vs E. coli MoaA | High; heuristic aligner, but motifs unambiguous |
| This report: paralog scan (UniProt, Iter 2) | Computational (evolutionary) | Qualifies/supports | Is PP_1969 the MoaA or a diverged paralog? | 3 MoaA paralogs in KT2440; PP_1969 is CLOSEST to E. coli MoaA; all 3 keep 6/6 cys | PSEPK | High |
| This report: AlphaFold AF-Q88LG4 v6 (Iter 2) | Computational (structural) | Supports | Are both [4Fe-4S] sites geometrically intact? | SG–SG 5.8–6.9 Å per triad; pLDDT 86–95; 21.4 Å inter-cluster cleft | PP_1969 model | High for geometry; predicted (no metals in model) |
| UniProt Q88LG4 GO:0061799 (IEA:TreeGrafter) | Database propagation | Competing/qualifies | Does PP_1969 also do the MoaC step? | No MoaC (PF01967) domain present → sibling-term error | PSEPK PP_1969 | High |

## Active-Site / Placement Analysis

Pairwise alignment PP_1969 (Q88LG4) vs characterized E. coli MoaA (P30745):
40.0% identity (126/315 aligned positions).

| Cluster | Role | E. coli MoaA | PP_1969 | Status |
|---|---|---|---|---|
| N-term radical-SAM, Cx₃Cx₂C | SAM reductive cleavage → 5'-dAdo• | Cys24 / Cys28 / Cys31 | **Cys36 / Cys40 / Cys43** | Conserved, correct spacing |
| C-term cluster II (GTP-binding) | Anchors 5'-GTP substrate | Cys257 / Cys260 / Cys274 | **Cys268 / Cys271 / Cys285** | Conserved, correct spacing |

C-terminal motif alignment (twitch domain):
```
E.coli P30745:  D F C A T C N R L R V S S I G K L H L C L   (257,260,...,274)
PP_1969 Q88LG4: P F C R T C S R L R L S S T G W L H G C L   (268,271,...,285)
```
Conserved GGEP motif present (…ITGGEPLV…, ~res 86). **All catalytic/metal-binding
residues are intact** — no evidence of pseudo-enzyme degeneracy.

**3D geometry (AlphaFold AF-Q88LG4-F1 v6, mean pLDDT 90):**

| Cluster | Cys triad | SG–SG distances (Å) | pLDDT |
|---|---|---|---|
| N-term radical-SAM | 36 / 40 / 43 | 5.9, 6.9, 6.0 | 86–95 |
| C-term GTP-binding | 268 / 271 / 285 | 6.4, 5.8, 6.3 | 88–92 |

Both triads show SG–SG spacing consistent with 3-Cys coordination of a [4Fe-4S]
cluster (one unique Fe left open for SAM cleavage / GTP binding respectively). The
two cluster centroids sit 21.4 Å apart, flanking the central substrate cleft —
the canonical MoaA arrangement. (Metals are not present in the AF model; geometry
is inferred from the apo cysteine positions.)

**Paralog placement (UniProt PANTHER PTHR22960, taxon 160488):**

| Accession | Gene | Length | % id to E. coli MoaA | 6-Cys active site |
|---|---|---|---|---|
| **Q88LG4 (PP_1969, target)** | — | 337 | **40.9%** | 6/6 intact |
| Q88E69 | *moaA* | 334 | 37.5% | 6/6 intact |
| Q88K11 | — | 322 | 36.3% | 6/6 intact |

PP_1969 and Q88K11 are a recent duplication (67.0% mutual identity). PP_1969 is
the **closest** paralog to the characterized cyclase → not a diverged outlier.

**Twitch / GTP-binding region conservation (Iteration 3).** Aligning the C-terminal
substrate-binding region (E. coli cols ~248–282) shows the cluster-II motif intact
in all three paralogs:
```
E.coli : ...DFCATCNRLRVSSIGKLHLCL...
Q88E69 : ...NFCATCNRVRLTVEGRLLLCL...
Q88K11 : ...PFCRSCSRLRLSSTGRLYGCL...
PP_1969: ...PFCRTCSRLRLSSTGWLHGCL...
```
PP_1969 vs E. coli identity is balanced across domains — N-terminal radical-SAM
41%, C-terminal twitch 39% — i.e. the GTP-recognition domain is **not** selectively
eroded. This rules out the subtler form of failure-mode 1 (clusters kept but
substrate specificity re-tuned).

## GO Curation Implications

- **GO:0061798 (GTP 3',8'-cyclase activity): RETAIN.** The IEA TreeGrafter call is
  correct and at the right granularity; it can be upgraded in confidence given
  strong orthology + full active-site conservation (lead for curator verification).
- **GO:0061799 (cyclic pyranopterin monophosphate synthase activity): REMOVE /
  replace.** This is the MoaC activity; PP_1969 has no MoaC domain. It is a
  sibling-activity carry-over from the mixed PANTHER family and should not sit on
  a MoaA protein (curator verification recommended).
- Keep GO:0051539 (4Fe-4S binding) and GO:0006777 (Moco biosynthetic process).

## Conflicts, Knowledge Gaps, Discriminating Tests

- **Paralog check (done):** *P. putida* KT2440 has **three** MoaA paralogs
  (Q88E69=*moaA*, Q88K11, Q88LG4=PP_1969). All retain the full 6-Cys active site,
  and PP_1969 is the closest to E. coli MoaA. This redundancy means the *in vivo*
  roles may be partitioned (e.g., condition-specific expression, aerobic vs
  anaerobic Moco demand, or distinct molybdoenzyme clients). The MF term is
  justified for PP_1969, but which paralog(s) carry flux in a given condition is
  an open experimental question and a candidate for transcriptomic/knockout study.
- **No direct PSEPK assay:** The function is inferred from orthology + residue
  conservation, not from a *P. putida*-specific enzymatic assay. Confidence is
  high but remains computational/evolutionary for this exact organism.
- **Most efficient discriminating experiment:** heterologous expression + in vitro
  radical-SAM assay measuring 5'-GTP → 3',8-cH₂GTP conversion (anaerobic, with
  dithionite/SAM), or complementation of an *E. coli ΔmoaA* mutant for Moco-/nitrate
  reductase–dependent growth. Either would directly confirm GTP 3',8'-cyclase activity.
- **Database carry-over caveat:** the GO:0061799 co-annotation illustrates that a
  single PANTHER family spanning MoaA and MoaC can emit both terms; curators should
  separate them by domain architecture.

## Conclusion

PP_1969 directly has the stated function. GO:0061798 is **supported** and
specific; the only curation fix is removing the co-propagated MoaC sibling term
GO:0061799.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)