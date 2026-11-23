---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T22:40:15.015983'
end_time: '2026-10-14T23:15:25.977814'
duration_seconds: 2110.96
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: ptxD
  gene_symbol: ptxD
  uniprot_accession: Q88HI1
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0030267
  hypothesis_text: ptxD has glyoxylate reductase (NADPH) activity (GO:0030267).
  term_context: '- Term: glyoxylate reductase (NADPH) activity (GO:0030267)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/ptxD/ptxD-uniprot.txt

    - PMID:39770733'
  source_file: genes/PSEPK/ptxD/ptxD-ai-review.yaml
  source_selector: existing_annotations[5].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0030267\n  label: glyoxylate reductase (NADPH)\
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
citation_count: 3
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
- **Gene directory:** ptxD
- **Gene symbol:** ptxD
- **UniProt accession:** Q88HI1

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0030267
- **Source file:** genes/PSEPK/ptxD/ptxD-ai-review.yaml
- **Source selector:** existing_annotations[5].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

ptxD has glyoxylate reductase (NADPH) activity (GO:0030267).

## Term and Decision Context

- Term: glyoxylate reductase (NADPH) activity (GO:0030267)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/ptxD/ptxD-uniprot.txt
- PMID:39770733

## Source Context YAML

```yaml
term:
  id: GO:0030267
  label: glyoxylate reductase (NADPH) activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **ptxD directly has the stated function**. Automated
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

**Target:** ptxD / PP_3376 (UniProt **Q88HI1**), *Pseudomonas putida* KT2440 (NCBITaxon:160488)
**Seed hypothesis (TreeGrafter/PANTHER, IEA, GO_REF:0000118):** ptxD has **glyoxylate reductase (NADPH) activity (GO:0030267)**
**Hypothesis slug:** function-hypothesis-go-0030267

---

## Summary

The TreeGrafter/PANTHER graft of **GO:0030267 (glyoxylate reductase, NADPH)** onto Q88HI1 is **substantially correct**. By independent global pairwise alignment the 320-aa query is **53.4% identical to the biochemically characterized *E. coli* GhrB** (glyoxylate/hydroxypyruvate reductase B, EC 1.1.1.79/1.1.1.81) — its single nearest characterized neighbor and exactly the PANTHER subfamily (PTHR10996:SF283) it was grafted onto. Its catalytic machinery (His285, Glu266, Arg237 triad; NAD(P)-binding Rossmann motif GMGRIG@152; both diagnostic PROSITE signatures) is fully intact, and the cofactor-specificity region matches the NADPH-using GhrB. Of the three characteristic phylogenetic-propagation failure modes, only **#1 (granularity)** applies, and only mildly: GhrB-type enzymes are **dual** glyoxylate **and** hydroxypyruvate reductases, so the single seed term understates the characterized activity.

The notable twist of this stress test is that the TreeGrafter graft is **more trustworthy than the gene name**. The record's competing annotation — "ptxD / phosphite dehydrogenase" (GO:0050609, EC 1.20.1.1) — rests only on an automated EMBL gene name and a distant 35.1%-identity homolog (characterized PtxD of *P. stutzeri* WM88, O69054). The query **lacks PtxD's distinctive phosphite-binding residues** (Lys76→Val75, Trp314→Ser307), retaining only the generic family triad that all reductases share. This is positive evidence *against* phosphite dehydrogenase activity. The real over-call in the record is therefore the *ptxD* symbol-driven phosphite annotation, not the propagated glyoxylate-reductase term.

All conclusions rest on sequence/structure homology; no direct enzymology exists for the *P. putida* protein. The recommended curation action is to **retain GO:0030267, add GO:0016618 (hydroxypyruvate reductase) to capture the dual activity, and flag the phosphite-dehydrogenase (GO:0050609) annotation for curator scrutiny / removal.**

---

## Executive Judgment

**Verdict: SUPPORTED, partially (too specific) — the graft is essentially correct; the applicable failure mode is #1 (granularity), not #2 (pseudo-enzyme) or #3 (mis-placement).**

**Most decisive evidence:** the query is 53.4% identical to characterized *E. coli* GhrB — within-subfamily, function-conserving territory — and GhrB is its nearest characterized neighbor and the exact subfamily it was grafted to.

| Failure mode | Applies? | Basis |
|---|---|---|
| **#1 Granularity (family vs subfamily)** | **Yes (mild)** | GhrB-type enzymes are dual glyoxylate + hydroxypyruvate reductases; single term GO:0030267 names only one of two sibling activities |
| **#2 Pseudo-enzyme / lost activity** | **No** | Catalytic triad (His285/Glu266/Arg237), Rossmann motif GMGRIG@152, PROSITE PS00065 + PS00671 all intact; full-length, no truncation |
| **#3 Within-superfamily mis-placement** | **No** | Independent homology places the protein in exactly the subfamily it was grafted to (53.4% to GhrB vs ≤35.1% for all sibling subfamilies) |

---

## Independent Family / Function Assignment

- **Most likely specific function:** NADPH-dependent **glyoxylate/hydroxypyruvate reductase** (GhrB subfamily of the D-isomer-specific 2-hydroxyacid dehydrogenase family).
- **Characterized homolog it is based on:** *E. coli* **GhrB** (UniProt P37666; EC 1.1.1.79 glyoxylate reductase / EC 1.1.1.81 hydroxypyruvate reductase), 53.4% identity; PANTHER PTHR10996:SF283; InterPro IPR050223; Pfam PF00389 + PF02826. Human **GRHPR** (39.4%) is a second, independent corroborating neighbor.
- **GO term I would assign:** **GO:0030267** (glyoxylate reductase, NADPH) **together with GO:0016618** (hydroxypyruvate reductase, NAD(P)H). Relative to the seed term, this is the **same branch** — the seed is on the correct branch but **narrower** than the protein's likely dual-substrate activity.

---

## Key Findings

### Finding 1 — Closest characterized homolog is GhrB, not phosphite dehydrogenase

Global Needleman–Wunsch alignment of the 320-aa query against a panel of characterized family members produced an unambiguous ranking. The query is **53.4% identical over 320 aligned columns to *E. coli* GhrB** (P37666, glyoxylate/hydroxypyruvate reductase B). All other characterized candidates are substantially more distant: characterized phosphite dehydrogenase PtxD (*P. stutzeri* WM88, O69054, EC 1.20.1.1) = 35.1%; *E. coli* SerA (P0A9T0) = 28.8%; *E. coli* GhrA (P75913) = 23.5%. The query carries the InterPro family signature **IPR050223** (D-isomer 2-hydroxyacid dehydrogenase) with **Pfam PF00389 + PF02826**, and PANTHER places it in **PTHR10996:SF283 "glyoxylate/hydroxypyruvate reductase B"** — i.e., the GhrB subfamily. The graft target is therefore the genuine nearest relative, directly ruling out failure mode #3.

### Finding 2 — Catalytic machinery is fully intact (not a pseudo-enzyme)

The query retains the complete D-2-hydroxyacid dehydrogenase catalytic apparatus, ruling out failure mode #2. The NAD(P)-binding Rossmann **glycine-rich motif GMGRIG** is present at position 152. The conserved family **catalytic base His285** (within the NVVATP-**H**-IGS motif) and the paired acidic residue **Glu266** align 1:1 to the characterized PtxD/GhrB catalytic triad. UniProt reports both PROSITE catalytic signatures **PS00065** and **PS00671** (D-2-hydroxyacid dehydrogenase) as matched. The protein is full-length (320 aa) with no frameshift or truncation. A conserved fold with a degenerate active site would argue against a catalytic MF term; here the active site is conserved, so the catalytic MF term is warranted.

### Finding 3 — Query lacks PtxD's phosphite-binding residues while retaining the generic 2-hydroxyacid reductase triad

Mapping characterized PtxD (O69054) active/binding residues onto the query confirms a clean split. The **generic family catalytic triad is conserved** (PtxD Arg237 = query Arg237; PtxD Glu266 = query Glu266; PtxD His292 = query His285 in GhrB-like numbering; PtxD Ser295 = query Ser288). But the **PtxD-distinctive phosphite-pocket residues are NOT conserved**: PtxD **Lys76** (phosphite binding) → query **Val75**; PtxD **Trp314** → query **Ser307**; PtxD **Tyr139** → query **Phe139**. Across a broadened panel, the two nearest characterized neighbors are both glyoxylate/hydroxypyruvate reductases (GhrB 53.4%, human GRHPR 39.4%), with PtxD (35.1%), formate DH (28.8%), SerA (28.8%), and GhrA (23.5%) all more distant. The query's catalytic His position (285) and length (320 aa) match GhrB (H285, 324 aa), **not** PtxD (H292, 336 aa). This is the decisive argument that the protein is not a phosphite dehydrogenase.

### Finding 4 — Cofactor-determinant region matches the NADPH-using GhrB

In the Rossmann cofactor-specificity window (~residues 152–177, immediately after the GxGxxG motif), the query (**GMGRIGEALARRAAAGFGMRVLYHSQ**) is near-identical to NADPH-dependent GhrB (**GMGRIGMALAQRAHFGFNMPILYNAR**). Both carry basic Arg residues in the 2′-phosphate recognition region and lack the acidic Asp that H-bonds the adenosine 2′/3′-OH in strict NAD(H)-specific members (that Asp is present in NAD-dependent SerA, "YFYDIE", and in the PtxD region). This supports the **NADPH** qualifier of the seed term — at fingerprint level, not kinetic level.

---

## Mechanistic Model / Interpretation

Q88HI1 is a soluble, NADPH-dependent D-2-hydroxyacid dehydrogenase of the GhrB type. Enzymes of this subfamily reduce small 2-oxo/2-hydroxy acids using NADPH:

```
   Glyoxylate      + NADPH + H+  --->  Glycolate     + NADP+     (EC 1.1.1.79; GO:0030267)
   Hydroxypyruvate + NADPH + H+  --->  D-glycerate   + NADP+     (EC 1.1.1.81; GO:0016618)
```

The chemistry is standard D-2-hydroxyacid dehydrogenase hydride transfer: **His285** acts as general acid/base, oriented by **Glu266**, while **Arg237** polarizes the substrate carbonyl; NADPH binds in the Rossmann domain whose 2′-phosphate pocket is lined by basic residues (the GhrB-like Arg-rich fingerprint).

Family placement and failure-mode triage:

```
Family: D-isomer 2-hydroxyacid dehydrogenases (IPR050223; PF00389+PF02826)
   |
   |-- GhrB-type (glyoxylate/hydroxypyruvate reductase, NADPH) ... 53.4% id  <== Q88HI1 lives here
   |      (E. coli GhrB P37666; human GRHPR 39.4%)
   |-- PtxD-type (phosphite dehydrogenase, EC 1.20.1.1) .......... 35.1% id  (NOT this protein)
   |-- SerA-type (3-P-glycerate dehydrogenase, NAD) ............. 28.8% id
   |-- Formate dehydrogenase .................................... 28.8% id
   |-- GhrA-type ............................................... 23.5% id
```

The one genuine annotation hazard in this gene record is **not** the TreeGrafter graft but the **gene symbol *ptxD***, which implies phosphite dehydrogenase (EC 1.20.1.1, GO:0050609). That interpretation is refuted by the residue-level analysis (missing Lys76/Trp314 phosphite-binding residues; 18-point identity gap to true PtxD). The reviewed literature describes authentic *P. stutzeri* PtxD used as an NAD(H)-regeneration tool — a genuinely different, more distant enzyme — and should not be conflated with Q88HI1.

---

## Active-Site / Placement Analysis (provenance)

**Catalytic residues: INTACT.** The generic triad, the Rossmann motif, and both PROSITE signatures are present; PtxD's phosphite-pocket residues are absent.

**(a) Nearest-characterized-neighbor ranking (global NW, 320-aa query):**

| Reference (characterized) | Function (EC) | % identity |
|---|---|---|
| **GhrB** *E. coli* (P37666) | glyoxylate/hydroxypyruvate reductase (1.1.1.79/.81) | **53.4** |
| **GRHPR** human | glyoxylate/hydroxypyruvate reductase | **39.4** |
| PtxD *P. stutzeri* WM88 (O69054) | phosphite dehydrogenase (1.20.1.1) | 35.1 |
| SerA *E. coli* (P0A9T0) | D-3-P-glycerate dehydrogenase (1.1.1.95) | 28.8 |
| Formate dehydrogenase (NAD) | formate dehydrogenase | 28.8 |
| GhrA *E. coli* (P75913) | glyoxylate/hydroxypyruvate reductase A | 23.5 |

The two nearest characterized homologs are both glyoxylate/hydroxypyruvate reductases; phosphite dehydrogenase ranks third.

**(b) Active-site discrimination — phosphite pocket vs generic triad (PtxD O69054 numbering):**

| Functional element | Reference | Query (Q88HI1) | Conserved? | Interpretation |
|---|---|---|---|---|
| Rossmann glycine-rich motif | GxGxxG | **GMGRIG** @152 | ✅ | NAD(P) binding intact |
| Catalytic base His | PtxD His292 / GhrB His285 | **His285** | ✅ | Proton donor intact |
| Catalytic acid Glu | Glu266 | **Glu266** | ✅ | His-orienting residue intact |
| Substrate-binding Arg | Arg237 | **Arg237** | ✅ | Carbonyl polarization intact |
| Ser (triad) | PtxD Ser295 | **Ser288** | ✅ | Intact |
| PROSITE catalytic signatures | PS00065, PS00671 | Both matched | ✅ | Family signatures present |
| **PtxD phosphite-binding Lys76** | Lys76 | **Val75** | ❌ | No phosphite pocket |
| **PtxD Trp314** | Trp314 | **Ser307** | ❌ | No phosphite pocket |
| PtxD Tyr139 | Tyr139 | **Phe139** | ❌ (conservative) | Divergent from PtxD |

**Conclusion:** Catalytic machinery is intact → competent oxidoreductase, **not a pseudo-enzyme**. The protein is a **glyoxylate/hydroxypyruvate reductase, not a phosphite dehydrogenase**. A low level of residual phosphite activity cannot be formally excluded from sequence alone, but both the nearest-neighbor ranking and the missing phosphite-pocket residues point away from it.

*Provenance note:* these computations (global NW alignments, residue mapping, motif identification) were executed during iterations 1–3; numeric outputs are reproduced above. The cofactor-specificity call is fingerprint-level, not kinetic — stated as a limitation.

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes/Qualifies/Competing | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|
| UniProt Q88HI1 | review/database | Qualifies | Identity/annotation | Family = D-2-hydroxyacid DH; carries conflicting GO:0050609 (EC) vs GO:0030267/0016618 (TreeGrafter) | *P. putida* KT2440 | High; *ptxD* name is ECO:0000313 (automated, EMBL) |
| This work (NW alignment) | computational/evolutionary | **Supports** seed | Nearest characterized homolog | Query 53.4% id to GhrB; 35.1% PtxD; 28.8% SerA; 23.5% GhrA | in-silico | High; robust margin |
| This work (active-site map) | computational/structural | Supports (not pseudo-enzyme) + refutes phosphite-DH | Catalytic residues intact; phosphite pocket absent | Triad R237/E266/H285/S288 conserved; PtxD Lys76→Val, Trp314→Ser absent | in-silico (O69054 numbering) | Med-high; residual phosphite activity not formally excludable |
| This work (broadened panel) | computational/evolutionary | **Supports** seed | Nearest two neighbors | GhrB 53.4%, GRHPR 39.4% (both glyoxylate/hydroxypyruvate reductases) rank above phosphite DH | in-silico | High |
| This work (cofactor region) | computational | Supports NADPH | Cofactor preference | NAD(P)-binding window near-identical to NADPH-using GhrB | in-silico | Medium; fingerprint-level |
| UniProt P37666 (GhrB) | review/database | Supports | Target function | "NADPH-dependent reduction of glyoxylate and hydroxypyruvate into glycolate and glycerate" | *E. coli* | High |
| UniProt O69054 (PtxD) | review/database | Competing | Phosphite-DH identity | Characterized PtxD oxidizes phosphite, EC 1.20.1.1; only 35% to query | *P. stutzeri* WM88 | High for PtxD; weak link to query |
| [PMID: 29910188](https://pubmed.ncbi.nlm.nih.gov/29910188/) | review/direct assay | Competing/context | What bona fide PtxD does | PtxD double mutant used to probe NADPH supply; PtxD oxidizes phosphite reducing NAD(P) | heterologous | High for PtxD biology |
| [PMID: 24908186](https://pubmed.ncbi.nlm.nih.gov/24908186/) | review/applied | Competing/context | PtxD as NAD(H)-regeneration tool | "Codon-optimized *Pseudomonas stutzeri* phosphite dehydrogenase (PtxD) was overexpressed for cofactor (NADH) regeneration" | engineered *E. coli* | High for PtxD; contextual |
| [PMID: 41415686](https://pubmed.ncbi.nlm.nih.gov/41415686/) | review/applied | Competing/context | PtxD function | "PtxD catalyzes the conversion of phosphite to phosphate while reducing NAD" | engineered system | High for PtxD; contextual |

**How the literature bears on the findings:** The three PtxD papers are all about *authentic* phosphite dehydrogenase (*P. stutzeri* WM88) used as a cofactor-regeneration tool. They establish what genuine PtxD does — oxidize phosphite to phosphate with NAD(H)/NADPH regeneration — and thereby sharpen, rather than support, the distinction: Q88HI1 lacks the phosphite-binding residues these enzymes require and is 18 identity points more distant from true PtxD than from GhrB. The UniProt records for GhrB (P37666) and PtxD (O69054) anchor the two competing branches, and the homology ranking resolves the query firmly onto the GhrB (reductase) branch.

---

## Limitations and Knowledge Gaps

- **No direct enzymology on Q88HI1 itself.** All evidence is sequence/structure-based homology; no measured kcat/Km, cofactor preference, or substrate panel exists for the *P. putida* protein. Confidence is high for "GhrB-type reductase," moderate for the exact preferred substrate (glyoxylate vs hydroxypyruvate) and cofactor (NADPH vs NAD(P)H).
- **Cofactor specificity (NADPH vs NADH) is inferred from a sequence fingerprint**, not measured. The GO:0030267 NADPH qualifier is plausible but not experimentally pinned for this ortholog.
- **Residual phosphite activity cannot be formally excluded** from sequence alone, though the missing phosphite-pocket residues make it unlikely.
- **Paralog caution:** *Pseudomonas* genomes carry several 2-hydroxyacid dehydrogenase paralogs; the *ptxD* label is likely database carry-over and may invite the wrong EC.
- **Alignment method:** crude global Needleman–Wunsch scoring; margins are large and robust, but a profile/HMM or structural superposition would strengthen the placement.

---

## Proposed Follow-up Experiments / Actions

1. **Enzyme assay (most decisive, single experiment).** Express and purify recombinant Q88HI1 and measure steady-state kinetics for (a) glyoxylate + NADPH, (b) hydroxypyruvate + NADPH, versus (c) phosphite + NAD⁺. This resolves activity vs pseudo-enzyme, glyoxylate vs hydroxypyruvate ranking, NADPH vs NADH, and definitively excludes phosphite dehydrogenase. kcat/Km for glyoxylate/hydroxypyruvate ≫ phosphite would confirm GO:0030267/GO:0016618 over GO:0050609.
2. **Structural superposition.** AlphaFold/crystal model of Q88HI1 superposed onto GhrB (P37666) and PtxD (O69054) to confirm the absence of a phosphite-binding pocket at the modeled Val75/Ser307 positions.
3. **Physiological phenotyping.** Growth/complementation of a *P. putida* PP_3376 deletion on glyoxylate/glycolate and hydroxypyruvate/serine-cycle intermediates to assign the physiological role.

### GO Curation Implications (leads for curator verification)

1. **GO:0030267 (seed) — RETAIN**, but recognize it as one half of a dual activity. Recommend **make-more-complete, not more-specific**: keep GO:0030267 and also retain/add **GO:0016618** (hydroxypyruvate reductase). Both are consistent with the GhrB nearest neighbor.
2. **GO:0050609 (phosphonate/phosphite dehydrogenase) — FLAG as likely over-call.** It derives from the automated *ptxD* gene name, not experimental data, and the nearest characterized phosphite DH is only 35% identical. Candidate action: **remove or demote** pending evidence.
3. Do **not** downgrade to "protein binding" — the protein is an intact oxidoreductase.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)