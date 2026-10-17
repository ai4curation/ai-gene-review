---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:37:37.320068'
end_time: '2026-10-15T02:35:14.800923'
duration_seconds: 3457.48
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: gabD-II
  gene_symbol: gabD-II
  uniprot_accession: Q88EN2
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0004777
  hypothesis_text: gabD-II has succinate-semialdehyde dehydrogenase (NAD+) activity
    (GO:0004777).
  term_context: '- Term: succinate-semialdehyde dehydrogenase (NAD+) activity (GO:0004777)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/gabD-II/gabD-II-deep-research-openscientist.md'
  source_file: genes/PSEPK/gabD-II/gabD-II-ai-review.yaml
  source_selector: existing_annotations[1].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0004777\n  label: succinate-semialdehyde dehydrogenase\
    \ (NAD+) activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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
- **Gene directory:** gabD-II
- **Gene symbol:** gabD-II
- **UniProt accession:** Q88EN2

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0004777
- **Source file:** genes/PSEPK/gabD-II/gabD-II-ai-review.yaml
- **Source selector:** existing_annotations[1].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

gabD-II has succinate-semialdehyde dehydrogenase (NAD+) activity (GO:0004777).

## Term and Decision Context

- Term: succinate-semialdehyde dehydrogenase (NAD+) activity (GO:0004777)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/gabD-II/gabD-II-deep-research-openscientist.md

## Source Context YAML

```yaml
term:
  id: GO:0004777
  label: succinate-semialdehyde dehydrogenase (NAD+) activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **gabD-II directly has the stated function**. Automated
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

# AIGR TreeGrafter Function-Inference Stress Test — Final Report

**Target gene:** gabD-II (`gabD-II`, locus `PP_4422`) · *Pseudomonas putida* KT2440 (PSEPK, NCBITaxon:160488)
**UniProt accession:** Q88EN2
**Seed hypothesis (TreeGrafter/PANTHER, IEA, GO_REF:0000118):** gabD-II has succinate-semialdehyde dehydrogenase (NAD+) activity — **GO:0004777**
**Focus:** function_assignment · `function-hypothesis-go-0004777`

---

## Summary

The seed hypothesis is **partially supported but too specific**. The reaction identity is right; the cofactor qualifier is wrong. Q88EN2 is unambiguously a *bona fide*, catalytically intact **succinate-semialdehyde dehydrogenase (SSADH)** of the ALDH superfamily. It carries the diagnostic Pfam aldehyde-dehydrogenase domain (PF00171, Aldedh), maps to InterPro families IPR015590/IPR016163, and is assigned by PANTHER to the SSADH subfamily PTHR43353:SF5. Its two catalytic residues — the nucleophilic **Cys296** and the general-base **Glu262** — are present and correctly spaced relative to characterized active members (they align to human ALDH5A1 Cys340/Glu306 and to the Cys/Glu pair shown by mutagenesis to be essential in a cyanobacterial SSADH). This decisively **rejects the pseudo-enzyme failure mode (mode 2)**: the active site is intact, not degenerate.

The protein also sits firmly inside the **GabD clade** of bacterial SSADHs rather than the neighboring YneI/Sad clade. Pairwise identities place it at 51.7% to *E. coli* GabD and 48.2% to human ALDH5A1, but only 35.4% to *E. coli* Sad/YneI. Because the reaction (succinate semialdehyde + NAD(P)+ → succinate + NAD(P)H) is correct and the subfamily placement is coherent, the **within-superfamily mis-placement failure mode (mode 3) is also rejected**. The graft landed on the right functional subfamily.

What does **not** hold up is the **NAD+** specification embedded in GO:0004777. This is a **granularity/cofactor error (failure mode 1)**. Cofactor preference in SSADHs is set by a small number of residues in the coenzyme 2′-pocket, not by the catalytic machinery, and most characterized SSADHs are *promiscuous*, using both NAD+ and NADP+ with different affinities. Q88EN2's coenzyme-binding module tracks the **NADP+-specific** *E. coli* GabD very closely (76% local identity over the 2′-pocket region, with conserved basic residues Arg172/Lys173 that help accommodate the NADP+ 2′-phosphate), whereas it is only 35.4% identical overall to the NAD+/dual-cofactor YneI clade. Thus strict NAD+ dependence — the exact thing GO:0004777 asserts — is the *least* likely of the possibilities for this protein. The recommended curation lead is to **retain the SSADH function but generalize or replace the cofactor**: move to **GO:0009013** [succinate-semialdehyde dehydrogenase (NAD(P)+) activity] or to the NADP+ sibling **GO:0036243**, pending a definitive in vitro NAD+/NADP+ kinetics assay. We did not find primary biochemical data for Q88EN2 itself, so the cofactor call remains a sequence-based lean rather than a measured fact, and we flag it as such.

---

## Executive Judgment

**Verdict: Partially supported / too specific — cofactor granularity error (failure mode 1).**

- **Reaction (SSADH) — supported.** Catalytic Cys296 and Glu262 conserved and correctly spaced; PF00171 + PTHR43353:SF5; ~48–52% identity to characterized SSADHs.
- **Pseudo-enzyme (mode 2) — rejected.** Active-site residues intact; no evidence of degeneration.
- **Wrong subfamily (mode 3) — rejected.** Clean GabD-clade placement (51.7% to *E. coli* GabD vs 35.4% to YneI).
- **Cofactor "NAD+" qualifier (mode 1) — not supported.** Coenzyme pocket is GabD/NADP+-type; strict NAD+ is the least likely cofactor.

**Single most decisive piece of evidence:** The coenzyme-binding 2′-pocket of Q88EN2 is 76% identical to the NADP+-specific *E. coli* GabD and retains the basic Arg172/Lys173 pair that accommodates the NADP+ 2′-phosphate, while the protein is only 35.4% identical overall to the NAD+/dual YneI clade. The fold and catalytic residues confirm SSADH activity, but the pocket argues against the specific NAD+ claim in GO:0004777.

---

## Independent Family / Function Assignment

**Most likely specific molecular function (from our own analysis):** succinate-semialdehyde dehydrogenase, catalyzing

```
succinate semialdehyde + NAD(P)+ + H2O  →  succinate + NAD(P)H + H+
```

**Nearest characterized homolog:** *Escherichia coli* **GabD** (UniProt P25526), an **NADP+-specific** succinate-semialdehyde dehydrogenase — 51.7% identical to Q88EN2 and the closest characterized neighbor. Human ALDH5A1 (P51649, NAD+-preferring) is a more distant characterized relative at 48.2%. The NAD+/dual-cofactor *E. coli* Sad/YneI (P76149) is clearly more distant at 35.4%.

**GO term we would assign and granularity vs. the seed term:**

| GO term | Label | Relationship to seed GO:0004777 |
|---|---|---|
| **GO:0009013** | succinate-semialdehyde dehydrogenase (NAD(P)+) activity | **More general** (parent/sibling that drops the strict cofactor qualifier) — our primary recommendation |
| **GO:0036243** | succinate-semialdehyde dehydrogenase (NADP+) activity | **Sibling** — alternative if curator wants a specific cofactor and accepts the GabD-clade lean |
| GO:0004777 | succinate-semialdehyde dehydrogenase (NAD+) activity | The seed term — reaction correct, cofactor qualifier unsupported |

Granularity summary: the seed term is **correct in reaction but over-specified in cofactor**. The defensible call from sequence alone is the **cofactor-agnostic** term GO:0009013; the best-guess specific call is the **NADP+** sibling GO:0036243. Strict NAD+ is not supportable without an assay.

---

## Evidence Matrix

| # | Citation | Evidence type | Role | Claim tested | Key finding | Organism / context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | [PMID: 32966327](https://pubmed.ncbi.nlm.nih.gov/32966327/) | Structural / mutagenesis | **Supports** SSADH reaction; rejects pseudo-enzyme | Are the catalytic Cys/Glu essential, and are they intact in Q88EN2? | "the conserved Cys262 and Glu228 residues were crucial for the catalytic activity" — the Cys/Glu pair is essential; Q88EN2 retains equivalent Cys296/Glu262, correctly spaced | *Cyanothece* sp. ATCC51142 SSADH | High for residue essentiality; conservation inference is computational (alignment-based) |
| 2 | [PMID: 23229889](https://pubmed.ncbi.nlm.nih.gov/23229889/) | Structural / comparative | **Qualifies** (cofactor) | Do bacteria have two SSADH clades with different cofactor preference, and which is Q88EN2? | "many organisms…encode two succinate semialdehyde dehydrogenases…different cofactor preference (YneI and GabD)"; "the conserved Lys160 contributes to the enzyme preference to NAD(+)" | *Salmonella typhimurium* YneI | High; establishes that cofactor preference is residue-determined. Q88EN2 is GabD-clade, not YneI |
| 3 | [PMID: 23500184](https://pubmed.ncbi.nlm.nih.gov/23500184/) | Structural | **Qualifies** (cofactor) | Is cofactor preference set by single pocket residues? | "Ser157…and corresponding Pro159…play critical structural roles in determining NADP(+) and NAD(+) preference" | Cyanobacterial SSADH | High; confirms single-residue cofactor determinants — the NAD+ qualifier is a specific claim requiring verification |
| 4 | [PMID: 2647149](https://pubmed.ncbi.nlm.nih.gov/2647149/) | Direct assay | **Qualifies / competing** | Are SSADH cofactor assignments clean in vivo? | Two SSADH forms; the large form is NADP-specific, the "NAD-linked" form "was able to use NADP as cofactor" | *Klebsiella pneumoniae* | Moderate; different organism, but shows NAD/NADP labels are leaky |
| 5 | [PMID: 25092794](https://pubmed.ncbi.nlm.nih.gov/25092794/) | Direct assay | **Qualifies / competing** | Can a single SSADH use both cofactors? | Recombinant enzyme "could use both NAD(+) and NADP(+) as co-factors," Km 579 µM (NAD+) vs 1.0 mM (NADP+) | *Saccharomyces cerevisiae* | Moderate; eukaryotic enzyme, but directly demonstrates dual-cofactor behavior |
| 6 | [PMID: 25888791](https://pubmed.ncbi.nlm.nih.gov/25888791/) | Structural | Supports (reaction) | Reaction/catalytic context of a bacterial SSADH | SSADHs "catalyze the oxidation of succinic semialdehyde (SSA) to succinic acid in the presence of NAD(P)(+)" | *Streptococcus pyogenes* (NADP+-dependent) | High for reaction; reinforces NAD(P)+ description |
| 7 | [PMID: 29242124](https://pubmed.ncbi.nlm.nih.gov/29242124/) | Direct assay / modeling | Qualifies (cofactor) | Example of an NADP+-preferring bacterial-type SSADH | Cyanobacterial enzyme was NADP+-preferring | *Anabaena* sp. PCC7120 | Moderate; supports that GabD-type SSADHs commonly favor NADP+ |
| 8 | [PMID: 30690134](https://pubmed.ncbi.nlm.nih.gov/30690134/) | Direct assay | Context | Kinetic characterization of a bacterial SSADH | SSADH kinetically characterized in a chemolithotroph | *Nitrosomonas europaea* | Low-moderate; general support for bacterial SSADH biochemistry |
| 9 | UniProt/InterPro/Pfam/PANTHER | Computational / database | **Supports** family | Domain architecture and subfamily | PF00171 (Aldedh), IPR015590/IPR016163, PANTHER PTHR43353:SF5 (SSADH); PROSITE PS00070 present | Q88EN2 | High for family assignment; database-derived, not experimental for this protein |

---

## Active-Site / Placement Analysis

### Catalytic residues (reaction identity) — INTACT

A Needleman–Wunsch global alignment (BLOSUM62) of Q88EN2 against characterized SSADHs shows both catalytic residues present and correctly spaced:

| Catalytic role | Q88EN2 residue | Aligns to | Status |
|---|---|---|---|
| Nucleophile (thiol) | **Cys296** | Human ALDH5A1 Cys340; UniProt-annotated active site; essential Cys of *Cyanothece* SSADH (PMID 32966327) | **Conserved, correctly spaced** |
| General base | **Glu262** | Human ALDH5A1 Glu306; essential Glu of *Cyanothece* SSADH (PMID 32966327) | **Conserved, correctly spaced** |
| ALDH Cys signature | — | PROSITE **PS00070** ALDEHYDE_DEHYDR_CYS pattern | **Present** |

**Conclusion:** the catalytic apparatus is intact → the SSADH reaction MF term is justified; **pseudo-enzyme ruled out.**

### Subfamily placement (reaction subtype) — GabD clade

| Comparison protein | UniProt | Cofactor class | % identity to Q88EN2 |
|---|---|---|---|
| *E. coli* **GabD** | P25526 | NADP+-specific | **51.7%** (closest characterized) |
| Human ALDH5A1 | P51649 | NAD+-preferring | 48.2% |
| *E. coli* **Sad/YneI** | P76149 | NAD+/dual | **35.4%** (clearly more distant) |

**Conclusion:** Q88EN2 is a **GabD-clade** SSADH. The large identity gap to YneI rules out within-superfamily mis-placement into the NAD+/dual clade.

### Coenzyme 2′-pocket (cofactor determinant) — NADP+/GabD-type

| Feature | Observation | Implication |
|---|---|---|
| 2′-pocket local identity to *E. coli* GabD (NADP+) | **76% (28/37)** across GabD 148–184 → Q88EN2 155–191 | Pocket resembles NADP+-specific enzyme |
| ALDH coenzyme glycine motif | …TPWNFP… at Q88EN2 162–166 | Canonical ALDH cofactor motif present |
| Basic pocket residues | **Arg172 / Lys173** (GabD Arg165/Lys166) conserved | Accommodate NADP+ 2′-phosphate → NADP+ lean |
| Literature NAD+ determinant "YneI Lys160" | Maps to Q88EN2 **Lys187**, but conserved in ALL panel members irrespective of cofactor | Pyrophosphate-binding Lys, **not** a discriminator — does not support NAD+ |
| Genome-wide diagnostic-column vote | 38:24 toward NADP, **but confounded** by overall GabD identity and mislabeled refs | Treated as unreliable; excluded from the call |

**Conclusion:** cofactor is **not cleanly decidable from sequence**, but every reliable pocket signal leans **NADP+/dual**, and **strict NAD+ is the least likely** option. Two intended external references (Gluconobacter Gox0499, Synechococcus Sp2771) resolved to wrong-length UniProt entries and were discarded.

> **Provenance note:** the alignments, residue mappings, identity percentages, and the diagnostic-column vote above were computed during iterations 1–4 (Needleman–Wunsch/BLOSUM62 pairwise alignments and panel comparisons) and are recorded as findings F001–F004. The genome-wide vote was explicitly judged unreliable and excluded from the final cofactor determination.

---

## Mechanistic Model / Interpretation

Q88EN2 is the "second" succinate-semialdehyde dehydrogenase of *P. putida* KT2440 (hence **gabD-II**). It operates at the convergence of GABA catabolism and succinate-semialdehyde detoxification, oxidizing succinate semialdehyde to succinate and feeding carbon into the TCA cycle:

```
   GABA  ──(GABA aminotransferase, gabT)──►  succinate semialdehyde (SSA)
                                                     │
                            Q88EN2 (gabD-II, SSADH)  │  + NAD(P)+
                                                     ▼
                                                 succinate  ──►  TCA cycle
```

The three-part stress test resolves as follows:

```
Failure mode 1 (granularity / cofactor):  TRIGGERED
    Reaction correct, but NAD+ qualifier over-specified → generalize/replace

Failure mode 2 (pseudo-enzyme):           NOT triggered
    Cys296 + Glu262 intact, correctly spaced → active enzyme

Failure mode 3 (wrong subfamily):         NOT triggered
    Clean GabD-clade placement (51.7% vs 35.4%) → right subfamily
```

The crux is that PANTHER propagated a term (**GO:0004777**) whose *reaction* is exactly right but whose *cofactor annotation* is an artifact of the reference node the graft inherited. Cofactor identity in this enzyme family is encoded by a handful of 2′-pocket residues and is frequently promiscuous — multiple characterized SSADHs use **both** NAD+ and NADP+ (PMID 25092794, PMID 2647149). Q88EN2's pocket matches the NADP+-specific GabD, so the pipeline's confident "NAD+" label is the weakest-supported part of the annotation. This is a textbook granularity error: the fold and catalytic residues are shared across the family, so homology correctly transfers "SSADH," but the cofactor sub-specification should not have transferred without pocket-level evidence.

---

## Evidence Base

- **[PMID: 32966327](https://pubmed.ncbi.nlm.nih.gov/32966327/)** — *Kinetic and structural insights into enzymatic mechanism of SSADH from Cyanothece sp. ATCC51142.* Mutagenesis establishes the conserved Cys/Glu pair as essential for catalysis. **Supports** the reaction assignment and anchors the active-site conservation test for Q88EN2 (Cys296/Glu262).
- **[PMID: 23229889](https://pubmed.ncbi.nlm.nih.gov/23229889/)** — *Structure and activity of the NAD(P)+-dependent SSADH YneI from Salmonella typhimurium.* Documents the two-clade (YneI vs GabD) organization with different cofactor preference and the residue basis of NAD+ preference (Lys160). **Qualifies** the cofactor claim and localizes Q88EN2 to the GabD (not YneI) clade.
- **[PMID: 23500184](https://pubmed.ncbi.nlm.nih.gov/23500184/)** — *Structural basis for cofactor and substrate selection by cyanobacterium SSADH.* Shows single-residue determinants (Ser157/Pro159) switch NADP+/NAD+ preference. **Qualifies** — the NAD+ qualifier is a specific, residue-level claim that must be verified.
- **[PMID: 25092794](https://pubmed.ncbi.nlm.nih.gov/25092794/)** — *Characterization of recombinant SSADH from S. cerevisiae.* Enzyme uses **both** NAD+ and NADP+ (Km 579 µM vs 1.0 mM). **Competing/qualifies** — demonstrates dual-cofactor behavior typical of SSADHs, undercutting a strict NAD+-only annotation.
- **[PMID: 2647149](https://pubmed.ncbi.nlm.nih.gov/2647149/)** — *Two SSADHs from Klebsiella pneumoniae.* The "NAD-linked" form can also use NADP. **Competing/qualifies** — cofactor labels are leaky in vivo.
- **[PMID: 25888791](https://pubmed.ncbi.nlm.nih.gov/25888791/)**, **[PMID: 29242124](https://pubmed.ncbi.nlm.nih.gov/29242124/)**, **[PMID: 30690134](https://pubmed.ncbi.nlm.nih.gov/30690134/)** — Additional bacterial/cyanobacterial SSADH characterizations consistently describe the reaction as NAD(P)+-dependent and show NADP+ preference in several GabD-type enzymes. **Support** the reaction and the NADP+/dual lean.
- **UniProt/InterPro/Pfam/PANTHER** — PF00171 (Aldedh), IPR015590/IPR016163, PANTHER PTHR43353:SF5 (SSADH), PROSITE PS00070. **Supports** the family and subfamily assignment for Q88EN2.

---

## GO Curation Implications

**Recommended curation action (lead requiring curator verification):**

1. **Retain** the succinate-semialdehyde dehydrogenase *reaction* — well supported by fold, subfamily, and intact catalytic residues. Do **not** remove the MF annotation; this is a genuine enzyme, not a non-core / "protein binding" case.
2. **Generalize the cofactor:** replace **GO:0004777** [SSADH (NAD+) activity] with **GO:0009013** [SSADH (NAD(P)+) activity]. This is the defensible, sequence-supported call.
3. **Alternative (more specific):** if the curator prefers a specific cofactor, **replace with the sibling GO:0036243** [SSADH (NADP+) activity], justified by the GabD-clade placement and the NADP+-type 2′-pocket (76% identity to NADP+-specific *E. coli* GabD; basic Arg172/Lys173). Flag as a lean, not a measured fact.
4. **Do NOT retain strict NAD+ (GO:0004777)** as the sole term — the least-supported option.
5. Keep the evidence code at **IEA** until an experimental assay exists; the generalization is a sequence/structure-based curator inference.

**Why not "protein binding" or removal:** the active site is intact and the subfamily is coherent; the only error is cofactor over-specification. Removal would discard correct information.

---

## Conflicts, Knowledge Gaps, Discriminating Tests

### Conflicts and alternatives
- **Paralog confusion:** the "-II" suffix implies a gabD-I paralog. The GabD vs YneI two-clade pattern (PMID 23229889) means cofactor annotations can be swapped between paralogs; we verified Q88EN2 is the GabD-clade member, but curators should confirm the paralog's identity if one exists.
- **Cofactor promiscuity vs. specificity:** several characterized SSADHs use both NAD+ and NADP+ (PMID 25092794, PMID 2647149), so a strict single-cofactor term may misrepresent reality regardless of "preference." This is the strongest argument for the cofactor-agnostic GO:0009013.
- **Database carry-over:** the NAD+ qualifier most plausibly entered via an ancestral PANTHER node annotated NAD+, not via evidence specific to this protein. Two intended external reference sequences resolved to wrong-length UniProt entries and were discarded, weakening part of the comparative panel.

### Knowledge gaps
- **No primary biochemistry for Q88EN2 itself.** All cofactor inferences are by homology/structure, not measurement.
- **No experimental structure.** The 2′-pocket analysis rests on alignment to *E. coli* GabD; an AlphaFold model + cofactor docking was not completed and would strengthen (or overturn) the NADP+ lean.
- The genome-wide diagnostic-column vote (38:24 NADP) is confounded and was not used for the call.

### Most efficient discriminating tests
1. **In vitro NAD+/NADP+ kinetics** on recombinant Q88EN2 — measure kcat/Km with each cofactor. This single assay definitively resolves GO:0004777 vs GO:0036243 vs GO:0009013. **Highest value.**
2. **Structural / docking check:** build the AlphaFold model, inspect the 2′-pocket (Arg172/Lys173 geometry), dock NADP+ vs NAD+. Fast, computational, corroborates the sequence lean.
3. **Comparative genomics of P. putida SSADH paralogs:** confirm gabD-I vs gabD-II cofactor division of labor, mirroring the GabD/YneI pattern, to ensure the right term is on the right paralog.

---

## Limitations

- This report is a **sequence- and literature-based** assessment. No wet-lab assay was performed on Q88EN2, and no experimental 3D structure exists for it. The catalytic-residue conservation is robust and well anchored to mutagenesis data; the **cofactor assignment is a lean, not a fact**, and is reported as such.
- Two intended reference sequences were unusable (wrong-length UniProt entries), and a genome-wide diagnostic vote was judged unreliable and excluded — so the NADP+ lean rests primarily on the strong local identity to *E. coli* GabD plus the conserved basic pocket residues.
- Any local `*-bioinformatics` analyses in the repository were intentionally withheld and were not consulted; this report is independent and may be compared against them.

---

### Bottom line

Q88EN2 is a real, catalytically competent succinate-semialdehyde dehydrogenase of the GabD clade. The seed annotation got the reaction right but over-specified the cofactor: the defensible GO term is **GO:0009013 [SSADH (NAD(P)+) activity]** (or the NADP+ sibling **GO:0036243**), not the strict NAD+ term **GO:0004777**. The decisive follow-up is a simple NAD+/NADP+ kinetic assay.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)