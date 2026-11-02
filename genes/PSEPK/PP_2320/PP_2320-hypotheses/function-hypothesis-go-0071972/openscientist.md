---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:37:37.043845'
end_time: '2026-10-15T02:50:58.205212'
duration_seconds: 4401.16
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: PP_2320
  gene_symbol: PP_2320
  uniprot_accession: Q88KH0
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0071972
  hypothesis_text: PP_2320 has peptidoglycan L,D-transpeptidase activity (GO:0071972).
  term_context: '- Term: peptidoglycan L,D-transpeptidase activity (GO:0071972)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118'
  source_file: genes/PSEPK/PP_2320/PP_2320-ai-review.yaml
  source_selector: existing_annotations[8].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0071972\n  label: peptidoglycan L,D-transpeptidase\
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
citation_count: 4
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
- **Gene directory:** PP_2320
- **Gene symbol:** PP_2320
- **UniProt accession:** Q88KH0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0071972
- **Source file:** genes/PSEPK/PP_2320/PP_2320-ai-review.yaml
- **Source selector:** existing_annotations[8].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

PP_2320 has peptidoglycan L,D-transpeptidase activity (GO:0071972).

## Term and Decision Context

- Term: peptidoglycan L,D-transpeptidase activity (GO:0071972)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0071972
  label: peptidoglycan L,D-transpeptidase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **PP_2320 directly has the stated function**. Automated
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

# AIGR TreeGrafter Function-Inference Stress Test — PP_2320 (Q88KH0)

**Target:** PP_2320 / Q88KH0, *Pseudomonas putida* KT2440 (NCBITaxon:160488)
**Seed hypothesis (TreeGrafter / PANTHER, IEA, GO_REF:0000118):** PP_2320 has **peptidoglycan L,D-transpeptidase activity (GO:0071972)**
**Focus:** function_assignment · function-hypothesis-go-0071972

---

## Executive Judgment

**Verdict: SUPPORTED — retain GO:0071972.**

The automated phylogenetic propagation is correct in this case. None of the three
characteristic failure modes applies:

- **(1) Granularity / family-vs-subfamily:** The protein maps to the single-domain
  ErfK/YbiS/YnhG group of the L,D-transpeptidase family (PANTHER PTHR30582:SF24).
  The family-level molecular function term GO:0071972 is the correct level of
  granularity — see caveat below on the exact sub-reaction.
- **(2) Pseudo-enzyme / loss of activity:** The active site is **intact**. The
  catalytic His193 and the catalytic nucleophile Cys209 are both conserved and
  correctly spaced; Cys209 is in fact the *only* cysteine in the entire protein,
  so the catalytic thiol is unambiguously present.
- **(3) Within-superfamily mis-placement:** The sequence belongs squarely to the
  YkuD / L,D-transpeptidase fold and subfamily, not a structurally related but
  functionally distinct neighbor. Pfam PF03734, PROSITE PS52029, CDD cd16913
  (YkuD_like), and Gene3D 2.40.440.10 all agree.

**Single most decisive piece of evidence:** By Smith-Waterman alignment (live
UniProt sequences), PP_2320's catalytic dyad residues map **one-to-one** onto the
experimentally annotated active sites of characterized *E. coli* L,D-transpeptidases
— His193→YbiS His194 / ErfK His191, and Cys209→YbiS Cys210 / ErfK Cys207 — at
37–44% sequence identity. A degenerate pseudo-enzyme would show loss or mis-spacing
of exactly these residues; it does not.

The sole residual uncertainty is **not** about whether the molecular function term
is right, but about *which sub-reaction* the enzyme performs (lipoprotein anchoring
vs. 3→3 peptidoglycan cross-linking). That distinction is sequence-ambiguous here
and should **not** be over-specified. The evidence remains computational (IEA): no
direct enzymatic assay of PP_2320 itself exists.

---

## Independent Family/Function Assignment

From first-principles analysis of the sequence, domain architecture, and active-site
conservation — independent of the propagated annotation — PP_2320 is a **secreted
(periplasmic) L,D-transpeptidase of the ErfK/YbiS/YnhG class**.

- **Most likely specific molecular function:** peptidoglycan L,D-transpeptidase
  activity — cysteine-nucleophile catalysis forming L,D (3→3) linkages in/attached to
  peptidoglycan.
- **Characterized homolog the assignment is based on:** *E. coli* **YbiS/LdtB**
  (UniProt P0AAX8; 43.5% identity, nearest characterized neighbor), closely followed
  by **YnhG/LdtE** (P76193; 41.6%) and **ErfK/LdtA** (P39176; 36.9%).
- **GO term I would assign:** **GO:0071972** (peptidoglycan L,D-transpeptidase
  activity) — **same granularity** as the seed term. I would *not* descend to a more
  specific child term (e.g., a dedicated Braun's-lipoprotein-anchoring term vs. a
  3→3 cross-linking term), because the two nearest characterized homologs carry
  *different* sub-roles and are near-equidistant (43.5% vs. 41.6%), making the exact
  sub-reaction undeterminable from sequence alone.

**Conclusion on granularity:** seed term = assigned term = GO:0071972. Retain.

---

## Key Findings

### Finding 1 — PP_2320 is a catalytically intact L,D-transpeptidase-family protein

Independent primary-evidence analysis of UniProt Q88KH0 (325 aa) establishes a
complete, canonical L,D-transpeptidase architecture and an intact active site.

**Domain architecture.** The protein comprises (i) an N-terminal Sec signal peptide
(residues ~1–25) directing periplasmic/secreted localization; (ii) a **LysM
peptidoglycan-binding domain** (CDD cd00118 / InterPro IPR018392), which tethers the
enzyme to its peptidoglycan substrate; and (iii) a C-terminal **L,D-transpeptidase
(YkuD) catalytic domain** spanning approximately residues 98–233 (Pfam **PF03734**,
PROSITE **PS52029**, CDD **cd16913** "YkuD_like", Gene3D **2.40.440.10**, InterPro
**IPR005490**). This is the textbook domain layout of a periplasmic L,D-transpeptidase.

**Catalytic residues intact and correctly spaced.** The catalytic machinery is fully
present: **His193** (proton donor/acceptor, in the local context "PGYLIHGSNKK") and
the canonical **S-H-G-C** motif at positions 206–209 with **Cys209** as the catalytic
nucleophile (local context "RTSHGCFRMFN"). Critically, **Cys209 is the only cysteine
in the entire protein** — so the catalytic thiol nucleophile is unambiguously conserved
and cannot be confused with any other cysteine.

**Structural confidence.** AlphaFold model AF-Q88KH0 has a global pLDDT of **84.4**,
with 63.7% of residues in the very-high-confidence band; the catalytic domain is
well-folded in the model, consistent with a competent enzyme rather than a disordered
pseudo-enzyme.

**Family placement.** PANTHER assigns the protein to **PTHR30582** (L,D-transpeptidase
family), subfamily **SF24** (ErfK/SrfK-related). The L,D-transpeptidase family uses a
catalytic cysteine nucleophile to form L,D (3→3) peptidoglycan cross-links, the exact
activity described by GO:0071972
([PMID: 30514506](https://pubmed.ncbi.nlm.nih.gov/30514506/)).

### Finding 2 — Nearest characterized homologs are *E. coli* ErfK/YbiS with 1:1 catalytic-residue correspondence

Smith-Waterman alignment (BLOSUM62, gap penalty −8; sequences fetched live from
UniProt) against characterized L,D-transpeptidases gives:

| Query vs. target | UniProt | % identity | Aligned positions | SW score |
|---|---|---|---|---|
| PP_2320 vs. *E. coli* **YbiS/LdtB** | P0AAX8 | **43.5%** | 107/246 | 503 |
| PP_2320 vs. *E. coli* **ErfK/LdtA** | P39176 | **36.9%** | 110/298 | 491 |

In **both** alignments, the query's catalytic residues map one-to-one onto the
targets' experimentally annotated active-site residues:

- query **His193** → ErfK **His191** / YbiS **His194** (target residue = H, confirmed)
- query **Cys209** → ErfK **Cys207** / YbiS **Cys210** (target residue = C, confirmed)

Both targets belong to the same PANTHER subfamily as PP_2320 (PTHR30582:SF24,
ErfK/SrfK-related). This is the strongest single discriminator against the
"pseudo-enzyme" and "mis-placement" failure modes: the catalytic dyad is not merely
present but is positionally homologous to residues with direct experimental support.
*Provenance: `provenance/PP_2320_alignment.py`.*

### Finding 3 — Single-domain ErfK/YbiS/YnhG group; MF robust, exact sub-reaction sequence-ambiguous

Extending the alignment panel across both functional sub-clades of the family:

| Characterized LDT | UniProt | Sub-role | % identity to PP_2320 |
|---|---|---|---|
| **YbiS/LdtB** | P0AAX8 | lipoprotein (Lpp) anchoring | **43.5%** |
| **YnhG/LdtE** | P76193 | 3,3-crosslink | **41.6%** |
| **ErfK/LdtA** | P39176 | lipoprotein (Lpp) anchoring | **36.9%** |
| **YcbB/LdtD** | P22525 | 3,3-crosslink | 27.5% |
| **LdtMt2** | I6Y9J2 | 3,3-crosslink (*M. tuberculosis*) | 23.9% |

PP_2320 clearly belongs to the **single-domain ErfK/YbiS/YnhG group** (top three
hits), and in all three the catalytic His193 and Cys209 align one-to-one to the
targets' annotated active sites (His194/Cys210, His193/Cys209, His191/Cys207
respectively). However, the two closest hits carry **different** sub-roles —
YbiS/LdtB anchors Braun's lipoprotein to peptidoglycan, while YnhG/LdtE forms 3→3
cross-links — and they are **near-equidistant** (43.5% vs. 41.6%). Consequently, the
family-level molecular function (GO:0071972) is robustly supported, but the precise
chemical sub-reaction cannot be resolved from sequence alone and should not be
over-specified. *Provenance: `provenance/PP_2320_subclade.py`.*

---

## Mechanistic Model / Interpretation

The convergent lines of evidence assemble into a coherent, internally consistent model
of a functional periplasmic L,D-transpeptidase:

```
   N ──[ Sec signal ]──[ LysM PG-binding ]──────[ YkuD / L,D-TPase catalytic ]────── C
        (~1–25)          (CDD cd00118)            (~98–233; PF03734, PS52029)
        secretion        substrate tether         His193 ···· Cys209 (sole Cys)
                                                   proton shuttle   nucleophile
                                                        │
                                                        ▼
                         Cys-thioester acyl-enzyme intermediate on a
                         peptidoglycan stem peptide (meso-DAP, position 3)
                                                        │
                                                        ▼
                    ┌───────────────────────────────────────────────────┐
                    │  L,D (3→3) transpeptidation — one of two sub-roles: │
                    │   • 3→3 peptidoglycan cross-link (YnhG/LdtE-like)   │
                    │   • Braun's Lpp anchoring to PG (YbiS/ErfK-like)    │
                    │  ← sequence cannot discriminate (43.5% vs 41.6%)    │
                    └───────────────────────────────────────────────────┘
```

**Why the propagation succeeded here.** TreeGrafter grafted PP_2320 onto a node whose
diagnostic feature — the YkuD catalytic domain with its Cys-His dyad — is precisely the
feature PP_2320 retains. Unlike the three classic propagation failures, there is no
granularity mismatch (the term is at the correct family level), no active-site decay
(the dyad is intact and uniquely identifiable), and no superfamily mis-placement (every
independent domain database agrees on YkuD/PF03734). The LysM substrate-binding module
and Sec signal peptide further corroborate that this is a *bona fide* periplasmic
peptidoglycan-remodeling enzyme operating in the compartment where L,D-transpeptidation
occurs.

**The one honest caveat.** The L,D-transpeptidase family has functionally diverged into
at least two sub-activities that share an identical catalytic mechanism and fold:
3→3 cross-link formation and lipoprotein anchoring. PP_2320's two nearest characterized
neighbors sit on *opposite sides* of this divide at nearly identical sequence identity.
The shared molecular-function umbrella term GO:0071972 correctly captures what we can
assert; descending to a sub-reaction-specific term would overreach the evidence.

---

## Evidence Base / Matrix

| # | Citation | Evidence type | Supports / refutes / qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt Q88KH0 (database) | Review/database + computational | **Supports** | Domain architecture consistent with LDT | Sec signal + LysM + YkuD catalytic domain (PF03734 / PS52029 / cd16913) | *P. putida* KT2440 | High; annotation partly IEA itself |
| 2 | Active-site inspection (computational, this work) | Computational / structural-evolutionary | **Supports** | Catalytic residues present & spaced | His193 + Cys209 (S-H-G-C motif); Cys209 is sole Cys | Sequence of Q88KH0 | High; in-silico, no assay |
| 3 | AlphaFold AF-Q88KH0 (structural model) | Computational / structural | **Supports** | Catalytic domain is folded | pLDDT 84.4; 63.7% very-high confidence | Predicted model | Medium-high; prediction not experiment |
| 4 | SW alignment to P0AAX8 (YbiS) — `provenance/PP_2320_alignment.py` | Computational / evolutionary | **Supports** | Nearest characterized homolog & 1:1 active-site mapping | 43.5% id; His193→His194, Cys209→Cys210 | *E. coli* vs query | High for homology; no direct assay |
| 5 | SW alignment to P39176 (ErfK) — `provenance/PP_2320_alignment.py` | Computational / evolutionary | **Supports** | Active-site correspondence across subfamily | 36.9% id; His193→His191, Cys209→Cys207 | *E. coli* vs query | High |
| 6 | SW subclade panel (P76193, P22525, I6Y9J2) — `provenance/PP_2320_subclade.py` | Computational / evolutionary | **Qualifies** | Which sub-reaction? | Two nearest hits (43.5% anchor vs 41.6% crosslink) are near-equidistant | *E. coli* / *M. tb* vs query | High that it's ambiguous |
| 7 | [PMID: 30514506](https://pubmed.ncbi.nlm.nih.gov/30514506/) | Review / mechanistic (QM/MM) | **Supports** | Family mechanism = Cys-nucleophile 3→3 crosslink | "Formation of 3 → 3 crosslinks … catalyzed by l,d-transpeptidases" | *M. tuberculosis* Ldt2 | High for family mechanism |
| 8 | [PMID: 33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/) | Mutant phenotype / biochemical | **Qualifies** | LDT paralogs can have non-crosslink roles (Lpp cleavage/anchoring) | LdtF is an LDT paralog acting on Braun's Lpp | gram-negative envelope | Supports sub-role ambiguity |
| 9 | [PMID: 39294212](https://pubmed.ncbi.nlm.nih.gov/39294212/) | Direct assay / crystallography | **Supports** | LDT catalytic dyad & substrate chemistry | Biochemical/crystal characterization of Mtb Ldt2 | *M. tuberculosis* | Family-level support |
| 10 | [PMID: 31024745](https://pubmed.ncbi.nlm.nih.gov/31024745/) | Direct assay (purification/characterization) | **Supports** | LDT2 is an active enzyme | Isolation & characterization of Mtb LDT2 | *M. tuberculosis* | Family-level support |

*Note: no paper reports a direct enzymatic assay of PP_2320/Q88KH0 itself; all direct-assay
evidence is on homologous family members.*

**How the key papers bear on the findings.**
[PMID: 30514506](https://pubmed.ncbi.nlm.nih.gov/30514506/) establishes the shared family
mechanism — "Formation of 3 → 3 crosslinks in the peptidoglycan layer of *M. tuberculosis*
is catalyzed by l,d-transpeptidases" — anchoring the inference that PP_2320's conserved
Cys-His dyad performs the GO:0071972 activity.
[PMID: 39294212](https://pubmed.ncbi.nlm.nih.gov/39294212/) and
[PMID: 31024745](https://pubmed.ncbi.nlm.nih.gov/31024745/) provide direct biochemical and
crystallographic characterization of a representative family member (Mtb Ldt2), confirming
the enzyme class is genuinely catalytic.
[PMID: 33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/) qualifies the picture by showing
that LDT paralogs (LdtF) can act on Braun's lipoprotein rather than form cross-links,
which is exactly why the sub-reaction of PP_2320 must be treated as ambiguous.

---

## Active-Site / Placement Analysis

**Catalytic residues: INTACT.**

| Feature | PP_2320 (Q88KH0) | *E. coli* YbiS (P0AAX8) | *E. coli* ErfK (P39176) | Status |
|---|---|---|---|---|
| Catalytic His (proton shuttle) | **His193** | His194 | His191 | Conserved, 1:1 aligned |
| Catalytic Cys (nucleophile) | **Cys209** | Cys210 | Cys207 | Conserved, 1:1 aligned |
| S-H-G-C motif | present (206–209) | present | present | Conserved |
| Number of Cys in protein | **1** (Cys209) | — | — | Nucleophile unambiguous |
| Catalytic domain | PF03734 / PS52029 / cd16913 | same family | same family | Correct fold |
| Sequence identity to query | — | **43.5%** | 36.9% | Nearest characterized |

**Subfamily placement:** PANTHER PTHR30582:SF24 (ErfK/SrfK-related), single-domain
ErfK/YbiS/YnhG group. Independent confirmation from Pfam (PF03734), PROSITE (PS52029),
CDD (cd16913 YkuD_like), Gene3D (2.40.440.10), InterPro (IPR005490) — all consistent.

**Conclusion:** The catalytic dyad is present, correctly spaced, and positionally
homologous to experimentally annotated active sites of characterized family members.
This decisively rules out the pseudo-enzyme and superfamily-misplacement failure modes.
Provenance scripts: `provenance/PP_2320_alignment.py`, `provenance/PP_2320_subclade.py`.

---

## GO Curation Implications

**Recommended curation action: RETAIN GO:0071972 (peptidoglycan L,D-transpeptidase
activity) at the family level — lead requiring curator verification.**

- **Do NOT remove.** The active site is intact; there is no evidence of pseudo-enzyme
  status.
- **Do NOT generalize.** The term is already at the appropriate family granularity; a
  broader parent would lose information.
- **Do NOT make more specific.** Although the enzyme clearly performs L,D-transpeptidation,
  the exact sub-reaction (3→3 cross-linking vs. Braun's-lipoprotein anchoring) is
  sequence-ambiguous — the two nearest characterized homologs carry different sub-roles
  at near-identical identity (43.5% vs. 41.6%). Descending to a sub-reaction-specific
  child term would exceed the evidence.
- **Do NOT replace with a sibling term.** No evidence points to a neighboring,
  functionally distinct activity.
- **Evidence tier:** keep as **IEA / computational**. There is no direct assay or mutant
  phenotype for PP_2320 itself; all catalytic evidence is by homology and in-silico
  active-site conservation. This supports retaining the term but not upgrading the
  evidence code to an experimental tier.
- **Not "protein binding."** Avoided as a recommendation, per instructions; the
  catalytic MF term is well justified here.

The accompanying cellular-component interpretation (periplasmic/secreted, via the Sec
signal peptide and LysM module) and biological-process context (peptidoglycan remodeling
/ cell wall organization) are consistent and could be curated alongside the MF term if
not already present.

---

## Limitations and Knowledge Gaps

- **No direct experimental data for PP_2320 itself.** There is no enzymatic assay,
  experimental structure, or mutant phenotype for Q88KH0; all catalytic evidence is
  homology-based (IEA). This is sufficient to retain the term but not to upgrade the
  evidence tier.
- **Sub-reaction ambiguity.** The two nearest characterized homologs (YbiS/LdtB, 43.5%;
  YnhG/LdtE, 41.6%) carry *different* sub-roles, so sequence cannot discriminate whether
  PP_2320 primarily forms 3→3 cross-links or anchors a lipoprotein.
- **Organism-specific envelope differences.** *P. putida* does not share the identical
  Braun's-lipoprotein configuration of *E. coli*, complicating direct transfer of the
  "Lpp-anchoring" sub-role; this is unresolved by sequence alone.
- **Structural evidence is predicted, not experimental.** AlphaFold confidence is good
  globally (pLDDT 84.4) but is a model.
- **Family can harbor hydrolase paralogs.** LdtF-type paralogs cleave rather than form
  bonds ([PMID: 33941679](https://pubmed.ncbi.nlm.nih.gov/33941679/)); PP_2320's intact
  transpeptidase dyad argues against this, but it is a formal caveat.

---

## Proposed Follow-up Experiments / Actions

In priority order, the most efficient discriminating analyses are:

1. **In-vitro activity assay** of recombinant PP_2320 with (a) a peptidoglycan-mimetic
   donor/acceptor to test 3→3 cross-linking and (b) a Braun's-lipoprotein peptide to test
   anchoring — directly resolves the sub-reaction and upgrades the evidence tier.
2. **Cys209→Ala active-site mutant** + activity assay to confirm the nucleophile is
   catalytically required (distinguishes true enzyme from pseudo-enzyme).
3. **ΔPP_2320 phenotyping** in *P. putida* KT2440: muropeptide HPLC/MS to quantify 3→3
   cross-link abundance, plus β-lactam/carbapenem susceptibility shifts, to place the
   enzyme in its native cell-wall-remodeling role.
4. **Experimental structure** (X-ray / cryo-EM) to confirm the dyad geometry and
   substrate channel predicted by AlphaFold.

**Immediate curation action:** mark GO:0071972 as **retained (verified by independent
active-site analysis)**, keep IEA evidence, annotate the sub-reaction as undetermined,
and flag follow-up assay #1 as the decisive experiment.

---

## Summary (for busy readers)

PP_2320 (Q88KH0) from *Pseudomonas putida* KT2440 is a *bona fide*, catalytically intact
**L,D-transpeptidase**, and the TreeGrafter/PANTHER-propagated term **GO:0071972
(peptidoglycan L,D-transpeptidase activity) is SUPPORTED and should be RETAINED.** The
protein has the canonical architecture — Sec signal peptide, LysM peptidoglycan-binding
domain, and a YkuD catalytic domain (Pfam PF03734 / PROSITE PS52029) — and its catalytic
dyad (His193 and the sole-cysteine nucleophile Cys209) is fully conserved and correctly
spaced. Smith-Waterman alignment to characterized *E. coli* enzymes (YbiS/LdtB 43.5%,
YnhG/LdtE 41.6%, ErfK/LdtA 36.9% identity) maps these catalytic residues one-to-one onto
experimentally annotated active sites.

Systematic testing for the three characteristic propagation-failure modes returns
negative on all three: the term is at the correct **granularity** (family level), the
**active site is intact** (no pseudo-enzyme signal), and the sequence sits firmly in the
**YkuD/L,D-transpeptidase subfamily** (no superfamily mis-placement). The only residual
uncertainty is the precise sub-reaction — 3→3 peptidoglycan cross-linking versus Braun's
lipoprotein anchoring — which is sequence-ambiguous because PP_2320's two nearest
characterized homologs carry different sub-roles at nearly equal identity. The family-level
molecular function term correctly captures what the evidence supports; it should not be
made more specific.

All evidence is computational / by-homology (IEA): no direct assay of PP_2320 exists. The
recommended curation action is therefore to **retain GO:0071972 at the family level, keep
the IEA evidence tier, and not over-specify the sub-reaction** pending an in-vitro activity
assay or a ΔPP_2320 muropeptide-profiling experiment.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)