---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:37:36.911196'
end_time: '2026-10-15T01:48:56.052963'
duration_seconds: 679.14
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: fadB
  gene_symbol: fadB
  uniprot_accession: Q88L02
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0016509
  hypothesis_text: fadB has long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+)
    activity (GO:0016509).
  term_context: '- Term: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity
    (GO:0016509)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/fadB/fadB-uniprot.txt

    - file:PSEPK/fadB/fadB-deep-research-falcon.md'
  source_file: genes/PSEPK/fadB/fadB-ai-review.yaml
  source_selector: existing_annotations[11].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0016509\n  label: long-chain (3S)-3-hydroxyacyl-CoA\
    \ dehydrogenase (NAD+) activity\nevidence_type: IEA\noriginal_reference_id: GO_REF:0000118"
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
- **Gene directory:** fadB
- **Gene symbol:** fadB
- **UniProt accession:** Q88L02

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016509
- **Source file:** genes/PSEPK/fadB/fadB-ai-review.yaml
- **Source selector:** existing_annotations[11].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

fadB has long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity (GO:0016509).

## Term and Decision Context

- Term: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity (GO:0016509)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/fadB/fadB-uniprot.txt
- file:PSEPK/fadB/fadB-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0016509
  label: long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **fadB directly has the stated function**. Automated
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

# AIGR TreeGrafter Function-Inference Stress Test — fadB (PSEPK, Q88L02)

**Target gene:** fadB · **UniProt:** Q88L02 · **Organism:** *Pseudomonas putida* KT2440 (NCBITaxon:160488)
**Seed hypothesis (TreeGrafter/PANTHER):** fadB has long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity — **GO:0016509** (IEA, GO_REF:0000118).

---

## Summary

This report independently evaluates an automated phylogenetic-propagation hypothesis: that *P. putida* KT2440 **fadB (Q88L02)** directly carries **long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity (GO:0016509)**. The term was emitted by TreeGrafter/PANTHER by grafting the query onto a PANTHER reference tree and propagating a term from an ancestral node. Because such grafts fail in three characteristic ways — over-broad family term, pseudo-enzyme, or within-superfamily mis-placement — each failure mode was actively tested from primary evidence rather than assumed away.

**The verdict is SUPPORTED, with only a minor granularity caveat.** Q88L02 is the genuine, catalytically intact **multifunctional FadB α-subunit** of the *P. putida* KT2440 fatty-acid β-oxidation (FadBA) complex. It shows the textbook two-domain FadB architecture (N-terminal crotonase/enoyl-CoA hydratase fused to a C-terminal 3-hydroxyacyl-CoA dehydrogenase/Rossmann domain), a fully intact dehydrogenase active site (catalytic His451, NAD-binding Rossmann motif GAGIMG@321, family signature GMHFFNPV@449–456), and a catalytic window that is **90% identical** to the biochemically characterized *E. coli* FadB (P21177). It is encoded in the canonical *fadBA* operon (PP_2136) immediately upstream of *fadA* (PP_2137), and is cleanly distinguishable from two shorter type-2 3HCDH paralogs. None of the three propagation failure modes materially applies.

The single residual nuance is **granularity**: Swiss-Prot assigns the chain-length-*general* EC 1.1.1.35 (GO:0003857), whereas GO:0016509 adds a "long-chain" qualifier. This is a one-step, same-branch parent/child relationship — the seed term is slightly more specific than what the curator-assigned EC strictly supports, but it is biologically defensible given FadB's long-chain physiological role. The recommended curation lead is therefore to **retain GO:0016509** (optionally generalizing to GO:0003857 for exact EC concordance), not to remove or replace it.

---

## Executive Judgment

**Verdict: SUPPORTED (with a minor granularity caveat).**

Q88L02 genuinely possesses NAD+-dependent (3S)-3-hydroxyacyl-CoA dehydrogenase activity. Testing each propagation failure mode:

- **Mode 2 — Pseudo-enzyme / loss of activity — EXCLUDED.** All catalytic and cofactor-binding residues are conserved and correctly spaced (see Active-Site Analysis).
- **Mode 3 — Within-superfamily mis-placement — EXCLUDED.** The sequence truly belongs to the 3-hydroxyacyl-CoA dehydrogenase family (C-terminal domain) fused to a crotonase/enoyl-CoA hydratase domain (N-terminal) — the textbook FadB architecture, not a neighboring oxidoreductase subfamily.
- **Mode 1 — Granularity / family-vs-subfamily — MILD ONLY.** Swiss-Prot assigns the chain-length-general EC 1.1.1.35 (→ GO:0003857), whereas GO:0016509 adds a *long-chain* qualifier. The qualifier is biologically defensible (physiological role is long-chain fatty-acid β-oxidation) but is one step more specific than the curator-verified EC.

**Single most decisive piece of evidence:** the C-terminal dehydrogenase catalytic window is **90% identical** to the biochemically characterized *E. coli* multifunctional FadB (P21177), with the catalytic His, the glycine-rich NAD-binding Rossmann motif, and the GMHFFNP family signature all present at identical relative positions — a direct, residue-level demonstration that the catalytic machinery is intact.

---

## Independent Family/Function Assignment

Independent of the propagated term, the analysis assigns:

- **Most likely specific molecular function:** NAD+-dependent (3S)-3-hydroxyacyl-CoA dehydrogenase (oxidation of L-3-hydroxyacyl-CoA to 3-oxoacyl-CoA in the β-oxidation cycle), as part of a multifunctional FadB that also carries enoyl-CoA hydratase (EC 4.2.1.17), Δ3-Δ2-enoyl-CoA isomerase (EC 5.3.3.8), and 3-hydroxyacyl-CoA epimerase (EC 5.1.2.3) activities in its N-terminal crotonase domain.
- **Characterized homolog basis:** *E. coli* FadB multifunctional enzyme (P21177) and the pseudomonad FadBA β-oxidation multienzyme complex ([PMID:12115060](https://pubmed.ncbi.nlm.nih.gov/12115060/)).
- **GO term I would assign:** **GO:0003857** (3-hydroxyacyl-CoA dehydrogenase activity, EC 1.1.1.35) as the evidence-matched call; **GO:0016509** (the seed) is an acceptable, slightly **more-specific child/sibling** reflecting the long-chain physiological role.
- **Granularity relative to seed:** the seed term is **one step more specific** than the curator-assigned EC strictly supports — **same branch, not a different branch**.

---

## Key Findings

### Finding 1 — Q88L02 is a catalytically intact NAD+-dependent 3-hydroxyacyl-CoA dehydrogenase

Q88L02 is a reviewed Swiss-Prot entry (**FADB_PSEPK**, 715 aa) governed by **HAMAP-Rule MF_01621 ("FadB")**. Its domain architecture is the canonical multifunctional FadB two-domain organization: an **N-terminal enoyl-CoA hydratase/isomerase/crotonase domain** (approx. residues 1–190; Gene3D 3.90.226.10; InterPro IPR001753) carrying the hydratase/isomerase/epimerase activities, fused to a **C-terminal 3-hydroxyacyl-CoA dehydrogenase / Rossmann domain** (approx. residues 312–715; InterPro IPR006176/IPR006108) carrying the NAD(P)-binding fold and the dehydrogenase catalytic machinery.

A direct active-site test by sequence indexing confirmed every expected catalytic and cofactor residue: the catalytic base **His451** (ACT_SITE), the NAD-binding glycine-rich Rossmann motif **GAGIMG@321**, the 3HCDH family catalytic signature **G-M-H-F-F-N-P-V (449–456)** (containing His451 + Asn454), and the crotonase catalytic glutamates **Glu120** and **Glu140**. The Swiss-Prot CATALYTIC ACTIVITY statement records the reaction **(3S)-3-hydroxyacyl-CoA + NAD+ = 3-oxoacyl-CoA + NADH + H+** (EC 1.1.1.35, RHEA:22432). The protein is a member of the **FadBA β-oxidation heterotetramer (α2β2)**. This is unambiguously an active enzyme, not a degenerate fold.

Literature directly supports that this assembly is a genuine functional complex in pseudomonads: [PMID:12115060](https://pubmed.ncbi.nlm.nih.gov/12115060/) explicitly describes "**the beta-oxidation multienzyme complex (FadBA)**," confirming that Q88L02 is an active FadB α-subunit rather than a pseudo-enzyme.

### Finding 2 — No paralog confusion: Q88L02 is the genuine FadBA α-subunit in the fadBA operon

A proteome-level UniProt query for *P. putida* KT2440 (organism 160488) 3-hydroxyacyl-CoA dehydrogenase / FadB-family members resolved the gene neighborhood and paralog landscape:

| Accession | Gene / Locus | Length | Status | Activity | Relationship |
|---|---|---|---|---|---|
| **Q88L02** | fadB / PP_2136 | 715 aa | reviewed | EC 1.1.1.35 / 4.2.1.17 / 5.1.2.3 / 5.3.3.8 | **Target — FadB α-subunit** |
| Q88L01 | fadA / PP_2137 | 391 aa | — | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) | Operon partner (β-subunit) |
| Q88KS5 | PP_2214 | 255 aa | — | 'type-2' 3HCDH (EC 1.1.1.178/1.1.1.35) | Short paralog, distinct |
| Q88L88 | PP_2047 | 412 aa | — | 3HCDH-family protein | Short paralog, distinct |

Q88L02 (715 aa) sits **immediately adjacent to Q88L01 (fadA, PP_2137)** — the canonical *fadBA* β-oxidation operon arrangement, FadB directly upstream of the thiolase FadA. The other 3HCDH-family members (Q88KS5 at 255 aa; Q88L88 at 412 aa) are much shorter, single-domain "type-2" proteins lacking the fused crotonase domain that defines multifunctional FadB — structurally and functionally distinct, and not competitors for the assignment. The graft landed on the correct protein.

This is corroborated functionally by [PMID:17653511](https://pubmed.ncbi.nlm.nih.gov/17653511/), which describes blocking "the **fadBA operon** in the fatty acid beta-oxidation pathway of *P. putida*" to redirect flux toward medium-chain-length polyhydroxyalkanoate (mcl-PHA) biosynthesis — confirming the operon identity and the physiological β-oxidation role of this gene pair.

### Finding 3 — Catalytic site is 90% identical to biochemically characterized E. coli FadB

A pairwise comparison of the C-terminal dehydrogenase catalytic region between Q88L02 (*P. putida*, 715 aa) and the biochemically characterized *E. coli* multifunctional FadB **P21177 (729 aa)** shows near-complete conservation of the catalytic machinery:

| Catalytic element | *P. putida* Q88L02 | *E. coli* P21177 | Conserved? |
|---|---|---|---|
| Catalytic signature motif | GMHFFNP @ 449 | GMHFFNP @ 448 | Yes (identical motif, offset by 1) |
| Catalytic histidine | His451 | His450 | Yes |
| NAD-binding Rossmann motif | GxGxxG @ 321 | GxGxxG @ 320 | Yes |
| 20-residue catalytic window | RPENF**C**GMHFFNPVH**R**MPLV | RPENF**V**GMHFFNPVH**M**MPLV | **90% identical** |

The 20-residue window around the catalytic center is **90% identical**, differing only by two conservative/semi-conservative substitutions (C↔V and R↔M) outside the catalytic and cofactor-binding positions. Because *E. coli* FadB is one of the most thoroughly characterized members of this family, this residue-level congruence is strong, direct evidence that Q88L02 is a fully active dehydrogenase.

---

## Mechanistic Model / Interpretation

The findings converge on a single coherent picture. Q88L02 is the α-subunit of the FadBA fatty-acid β-oxidation multienzyme complex, a multifunctional enzyme performing three of the four β-oxidation steps, while the companion FadA (Q88L01) supplies the final thiolytic step:

```
  Fatty acyl-CoA (medium/long chain)
        │
        │  (acyl-CoA dehydrogenase — separate enzyme, not FadB)
        ▼
  trans-2-enoyl-CoA
        │
        │  ①  ENOYL-CoA HYDRATASE  (EC 4.2.1.17)          ─┐
        ▼                                                  │  N-terminal
  (3S)-3-hydroxyacyl-CoA                                   │  CROTONASE domain
        │                                                  │  (res ~1–190; IPR001753)
        │  ②  3-HYDROXYACYL-CoA DEHYDROGENASE              │  catalytic Glu120 / Glu140
        │     (EC 1.1.1.35 / GO:0016509)  ◄── SEED TERM ───┼─ C-terminal
        │     NAD+ → NADH + H+                              │  ROSSMANN domain
        ▼                                                  │  (res ~312–715; IPR006176)
  3-oxoacyl-CoA (3-ketoacyl-CoA)                           │  catalytic His451
        │                                                  │  NAD motif GAGIMG@321
        │  ③  3-KETOACYL-CoA THIOLASE (EC 2.3.1.16)        ─┘  signature GMHFFNPV@449
        │     ── performed by FadA (Q88L01, β-subunit)
        ▼
  acyl-CoA (n−2) + acetyl-CoA  ──►  next β-oxidation cycle
```

The propagated term GO:0016509 names **step ②**, the dehydrogenase reaction catalyzed by the C-terminal Rossmann domain. Every independent line of evidence places Q88L02 squarely on this activity: the architecture is the textbook crotonase+Rossmann fusion; the catalytic residues are all present and correctly spaced; the genomic context is the canonical *fadBA* operon; the short paralogs are clearly separate; and the catalytic window is 90% identical to the gold-standard *E. coli* FadB.

The only residual subtlety is **granularity**. Swiss-Prot assigns the chain-length-general EC 1.1.1.35 (GO:0003857), whereas GO:0016509 adds a "long-chain / (NAD+)" qualifier. Biochemically, bacterial β-oxidation FadB complexes act on medium-to-long acyl chains across successive cycles, so the long-chain descendant is defensible — but a curator could equally generalize to GO:0003857 for exact EC concordance. This is a one-step granularity question within the *same* GO branch, not an error of kind.

---

## Evidence Base / Evidence Matrix

| Citation / Source | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|
| UniProt FADB_PSEPK (Q88L02), HAMAP MF_01621 | Review/database + rule-based | Supports | Does protein have 3-hydroxyacyl-CoA DH (NAD+) activity? | RecName includes "3-hydroxyacyl-CoA dehydrogenase, EC 1.1.1.35"; CATALYTIC ACTIVITY (3S)-3-OH-acyl-CoA + NAD+ → 3-oxoacyl-CoA + NADH (RHEA:22432) | *P. putida* KT2440, PP_2136 | High; activity inferred by HAMAP rule (ECO:0000255), not direct assay on this ortholog |
| Active-site computation (this report) | Computational / evolutionary | Supports | Are catalytic residues intact & correctly spaced? | ACT_SITE His451 = H; Rossmann GxGxxG (GAGIMG) @321; signature GMHFFNPV @449–456 (His451+Asn454); crotonase catalytic Glu120, Glu140 | Sequence indexing of 715-aa chain | High; residues match canonical 3HCDH + crotonase motifs |
| Alignment vs *E. coli* FadB P21177 (this report) | Computational vs characterized member | Supports | Do catalytic residues align to a characterized active enzyme? | 90% identity over 20-aa catalytic window; His451↔His450, GMHFFNP motif and NAD Rossmann at identical relative positions | *E. coli* multifunctional FadB | High; P21177 is biochemically characterized |
| UniProt domain architecture (IPR001753 + IPR006176/IPR006108; Gene3D 3.90.226.10 + 3.40.50.720) | Structural / evolutionary | Supports | Correct family vs mis-placed sibling? | N-term crotonase + C-term 3HCDH/Rossmann = textbook FadB two-domain fusion | — | High |
| [PMID:12115060](https://pubmed.ncbi.nlm.nih.gov/12115060/) (Fiedler/Steinbüchel/Rehm 2002) | Direct characterization (review context) | Supports / qualifies | Is pseudomonad FadBA a functional β-oxidation complex? | Characterizes the "beta-oxidation multienzyme complex (FadBA)" and its hydratase functions in *Pseudomonas* | *P. oleovorans*/*P. putida* | Medium-high; ortholog, not KT2440 FadB directly |
| [PMID:17653511](https://pubmed.ncbi.nlm.nih.gov/17653511/) (Vo et al. 2007) | Mutant phenotype | Supports | Is fadBA in the β-oxidation pathway in *P. putida*? | fadBA operon block redirects flux (mcl-PHA accumulation), confirming β-oxidation role | *P. putida* KCTC1639 | Medium; strain differs; targets operon not the DH residue |
| UniProt EC (1.1.1.35, general) vs GO:0016509 (long-chain) | Database / annotation | Qualifies | Is the *long-chain* granularity exact? | Curator EC is chain-length-general; seed term adds long-chain qualifier | — | Granularity nuance, not a refutation |

**How the literature supports the findings.** [PMID:12115060](https://pubmed.ncbi.nlm.nih.gov/12115060/) provides the closest primary characterization — it dissects the pseudomonad FadBA β-oxidation multienzyme complex at the molecular level, confirming that this assembly in *Pseudomonas* is catalytically functional (not a relic) and directly anchoring the identity of Q88L02 as the active FadB α-subunit. [PMID:17653511](https://pubmed.ncbi.nlm.nih.gov/17653511/) supplies in vivo genetic evidence: knocking out/blocking the *fadBA* operon in *P. putida* reroutes fatty-acid flux into mcl-PHA, confirming the operon's bona fide β-oxidation role. Neither paper contradicts the seed hypothesis; both reinforce it, with the caveat that they characterize the complex/operon rather than isolate the KT2440 FadB dehydrogenase residue by residue.

---

## Active-Site / Placement Analysis

Positions verified directly against the 715-aa sequence (UniProt feature-table annotations in parentheses):

| Position | Residue found | Annotation / role | Intact? |
|---|---|---|---|
| 451 | **His (H)** | ACT_SITE — catalytic base for 3-hydroxyacyl-CoA DH | Yes |
| 321–326 | **GAGIMG** | NAD-binding glycine-rich Rossmann motif (GxGxxG) | Yes |
| 449–456 | **GMHFFNPV** | 3-HCDH family catalytic signature (His451 + Asn454) | Yes |
| 344 | Asp (D) | NAD+ binding | Yes |
| 454 | Asn (N) | NAD+ binding | Yes |
| 120 / 140 | Glu / Glu | Crotonase (enoyl-CoA hydratase) catalytic residues | Yes |
| 297 / 501 / 660 | Asp / Asn / Tyr | Substrate binding | Yes |

**Alignment to a characterized active member (Iteration 3).** Compared against *E. coli* FadB (**P21177**, the biochemically characterized multifunctional fatty-acid-oxidation complex α-subunit, 729 aa):

| Feature | Q88L02 (P. putida) | P21177 (E. coli, characterized) |
|---|---|---|
| Catalytic signature motif | **GMHFFNP** @449 | **GMHFFNP** @448 |
| Catalytic His (within GxHxxNP) | His451 | His450 |
| NAD Rossmann GxGxxG | @321 | @320 |
| Local catalytic-window identity | — | **90%** (RPENF**C/V**GMHFFNPVH**R/M**MPLV) |

The catalytic histidine, its signature motif, and the NAD-binding Rossmann motif are present at the **same relative positions** as in the characterized enzyme, with a 90%-identical 20-residue catalytic window.

**Conclusion: catalytic residues are intact and correctly spaced**, and align residue-for-residue to a biochemically characterized active member. Both the dehydrogenase (C-terminal) and hydratase (N-terminal) active sites are complete. This is an active enzyme, not a pseudo-enzyme, and it is placed in the correct family — not a mis-grafted sibling.

*Provenance:* sequence pulled from UniProt REST (Q88L02.txt); residue indexing and motif scanning executed in `execute_code` across iterations 1–3 (outputs retained in iteration log). No whole-protein structural superposition (e.g., AlphaFold geometric overlay) was performed this run — see Limitations.

---

## GO Curation Implications

**Recommended lead (requires curator verification): RETAIN GO:0016509**, with an optional note to **also/instead annotate the parent GO:0003857** if strict fidelity to the curator-assigned EC 1.1.1.35 is preferred.

- The molecular function is genuinely present: Q88L02 is a catalytically intact NAD+-dependent 3-hydroxyacyl-CoA dehydrogenase. TreeGrafter's propagation did **not** fail here — the activity is real, the fold and active site are intact, and the family placement is correct.
- **Primary — RETAIN GO:0016509.** The FadBA complex acts on medium-to-long acyl chains, so the long-chain descendant is biologically reasonable.
- **Alternative (curator's discretion) — GENERALIZE to GO:0003857** to match the Swiss-Prot EC 1.1.1.35 assignment exactly, trading a small amount of specificity for tighter EC concordance.
- Because the IEA/TreeGrafter call is corroborated by independent residue-level and comparative analysis, the annotation's confidence could reasonably be upgraded or supplemented with sequence/orthology-based evidence.
- Ensure the companion crotonase-domain functions (enoyl-CoA hydratase EC 4.2.1.17; Δ3-Δ2-enoyl-CoA isomerase EC 5.3.3.8; 3-hydroxyacyl-CoA epimerase EC 5.1.2.3) are also captured, since this is a multifunctional protein.

**Do NOT** remove, treat-as-non-core, downgrade to a generic binding term, or replace with a sibling activity. There is no evidence for pseudo-enzyme status or mis-placement. ("Protein binding" is explicitly not a relevant recommendation here.)

---

## Limitations and Knowledge Gaps

- **Granularity ambiguity (long-chain vs general):** The dehydrogenase step in bacterial β-oxidation acts across chain lengths during successive cycles, whereas strictly "long-chain" enzymes are chain-length restricted. No direct chain-length kinetic profile exists for KT2440 FadB, so the exact fidelity of the "long-chain" qualifier cannot be confirmed from primary data here.
- **Evidence provenance:** All activity calls for this specific ortholog are rule-based (ECO:0000255 / HAMAP), not direct enzymatic assays on the KT2440 protein. The strongest primary data come from *E. coli* FadB (P21177) and *Pseudomonas* FadBA orthologs, not KT2440 itself.
- **Structural check not run:** AlphaFold geometric superposition and a formal multiple-sequence alignment to a panel of characterized members were not executed this run; the decision was already decidable from Swiss-Prot features plus motif conservation and the pairwise *E. coli* comparison.
- **Phenotype specificity:** The in vivo evidence (PMID:17653511) concerns the *fadBA* operon / fadA knockout, supporting pathway function rather than isolating FadB dehydrogenase catalysis via a catalytic-dead point mutant.

---

## Proposed Follow-up Experiments / Actions

1. **Chain-length specificity assay** — purify recombinant Q88L02 (or its C-terminal dehydrogenase domain) and measure NAD+-coupled dehydrogenase activity across a substrate panel (C4→C16 (3S)-3-hydroxyacyl-CoA). This directly resolves the GO:0016509 (long-chain) vs GO:0003857 (general) granularity question.
2. **Active-site point mutant (His451Ala)** — abolition of dehydrogenase activity would formally confirm the catalytic residue and exclude any residual pseudo-enzyme hypothesis.
3. **AlphaFold / structure overlay** — superpose the Q88L02 model onto *E. coli* FadB (P21177) to confirm NAD+-pocket and His451 geometry; cheap, fully computational, and adds structural provenance.
4. **Heterologous complementation** — express Q88L02 in an *E. coli* fadB-null background and test restoration of growth on long-chain fatty acids for a clean in vivo functional confirmation.
5. **Curation action** — enter the lead "retain GO:0016509 (or generalize to GO:0003857)" plus the companion crotonase-domain MF terms for curator verification.

---

*Investigator note:* Analyses were executed programmatically (UniProt REST fetch + residue/motif verification + pairwise comparison to a characterized homolog). No results were fabricated; rule-based (ECO:0000255) provenance is flagged wherever direct assay data on the KT2440 protein were unavailable.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)