---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T22:59:12.368602'
end_time: '2026-10-14T23:22:37.354918'
duration_seconds: 1404.99
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: SACEN
  gene: eryCIV
  gene_symbol: eryCIV
  uniprot_accession: A4F7N3
  taxon_id: NCBITaxon:405948
  taxon_label: Saccharopolyspora erythraea NRRL 2338
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0008483
  hypothesis_text: eryCIV has transaminase activity (GO:0008483).
  term_context: '- Term: transaminase activity (GO:0008483)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118'
  source_file: genes/SACEN/eryCIV/eryCIV-ai-review.yaml
  source_selector: existing_annotations[2].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0008483\n  label: transaminase activity\n\
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

- **Organism code:** SACEN
- **Taxon:** Saccharopolyspora erythraea NRRL 2338 (NCBITaxon:405948)
- **Gene directory:** eryCIV
- **Gene symbol:** eryCIV
- **UniProt accession:** A4F7N3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0008483
- **Source file:** genes/SACEN/eryCIV/eryCIV-ai-review.yaml
- **Source selector:** existing_annotations[2].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

eryCIV has transaminase activity (GO:0008483).

## Term and Decision Context

- Term: transaminase activity (GO:0008483)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0008483
  label: transaminase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **eryCIV directly has the stated function**. Automated
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

**Target gene:** eryCIV (UniProt **A4F7N3**) · *Saccharopolyspora erythraea* NRRL 2338 (NCBITaxon:405948)
**Seed hypothesis under test:** eryCIV has **transaminase activity (GO:0008483)** — propagated by TreeGrafter/PANTHER, evidence type IEA, reference GO_REF:0000118
**Source selector:** `existing_annotations[2].function_hypothesis` in `genes/SACEN/eryCIV/eryCIV-ai-review.yaml`

---

## Summary

The TreeGrafter/PANTHER graft assigned **transaminase activity (GO:0008483)** to eryCIV. My independent analysis finds this assignment **partially supported but too general**: eryCIV is a genuine pyridoxal-5′-phosphate (PLP)-dependent aminotransferase, but the propagated term stops at the broad *family* level when the protein in fact belongs to a well-defined *subfamily* carrying out a specific sugar C4-transamination reaction. Of the three characteristic phylogenetic-propagation failure modes the objective asks me to test, only **Failure Mode #1 (granularity / family-vs-subfamily)** applies. Failure Mode #2 (pseudo-enzyme / loss of catalysis) and Failure Mode #3 (within-superfamily mis-placement onto a functionally distinct neighbor) are both **affirmatively ruled out**.

The decisive evidence is active-site conservation. The DegT/DnrJ/EryC1 fold (Pfam PF01041) supports two divergent chemistries — C4 transamination versus C3,4-dehydration — within a single structural scaffold, making a wrong-subfamily graft a live risk that a tree graft cannot self-diagnose. I therefore directly tested the catalytic apparatus. EryCIV retains the catalytic PLP Schiff-base **lysine (Lys200)** in register with the catalytic lysines of the structurally characterized transaminases ArnB (Lys188) and WecE (Lys181), whereas the family members that *lost* transamination and became dehydratases (ColD, AscC) carry a **histidine** at that exact position. EryCIV has lysine, not histidine. It is **60.5% identical** to **DesI**, an X-ray-characterized dTDP-sugar C4 aminotransferase, far above any other characterized member. The AlphaFold model (mean pLDDT 96.5) independently places Lys200 and the PLP-anchoring Asp171 in a compact, well-ordered pocket with geometry consistent with a bridging PLP cofactor.

The practical outcome for curation is **retain-and-refine**: keep the transaminase assignment but make it more specific to a **dTDP-4-amino-4,6-dideoxy-D-glucose (C4) sugar aminotransferase** in desosamine biosynthesis — the direct ortholog of DesI. The legacy "3,4-dehydratase" database name that still clings to eryCIV is a pre-structural mis-label, contradicted by the active-site analysis, and should not be propagated.

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED / TOO GENERAL.**

- **Failure mode that applies:** **#1 (granularity / family-vs-subfamily).** The propagated term is correct in kind but under-granular.
- **Failure modes ruled out:** **#2 (pseudo-enzyme)** — all catalytic and cofactor-anchoring residues are intact and well-ordered; **#3 (within-superfamily mis-placement)** — EryCIV is on the transaminase side of the DegT/DnrJ/EryC1 split, not a ColD-type PLP dehydratase.
- **Single most decisive piece of evidence:** EryCIV retains the catalytic PLP Schiff-base **Lys200** (motif `SFHA-T-K-AVTS`), aligned residue-for-residue to the catalytic lysine of ArnB (Lys188) and WecE (Lys181). The non-transaminase member ColD carries **His** at this exact position — its hallmark loss-of-transamination substitution — and EryCIV does not. Combined with 60.5% identity to the structurally characterized C4 transaminase DesI, this fixes EryCIV as a genuine transaminase.

---

## Independent Family / Function Assignment

Independent of the propagated PANTHER term, my own sequence and structural analysis assigns:

> **dTDP-4-keto-6-deoxy-D-glucose → dTDP-4-amino-4,6-dideoxy-D-glucose, a C4 sugar aminotransferase** in dTDP-D-desosamine biosynthesis.

- **Characterized homolog this is based on:** **DesI** (*Streptomyces venezuelae*, UniProt **Q9ZGH0**), the X-ray-characterized PLP-dependent C4 aminotransferase of the methymycin/pikromycin desosamine pathway, solved in complex with its product dTDP-4-amino-4,6-dideoxyglucose ([PMID: 17630700](https://pubmed.ncbi.nlm.nih.gov/17630700/)). EryCIV is **60.5% identical** to DesI over ~400 aligned columns — by far its nearest characterized neighbor. Erythromycin and methymycin/pikromycin share identical D-desosamine machinery, so eryCIV is the erythromycin-pathway ortholog of desI.
- **Domain architecture:** Pfam **PF01041 (DegT_DnrJ_EryC1)**, InterPro **IPR030967 (PLP_DesI)**; single-domain fold-type I PLP enzyme, 401 aa (SACE_0716).
- **GO term I would assign:** a **more specific** child of GO:0008483 on the **same branch** — functionally a "dTDP-4-amino-4,6-dideoxy-D-glucose transaminase" / sugar aminotransferase (EC 2.6.1.–). Granularity relative to the seed term: **more specific (same branch)** — not a sibling and not a different branch. Also well-supported: **GO:0030170 (pyridoxal phosphate binding)**, already present, and a desosamine/dTDP-sugar biosynthetic process term.

---

## Key Findings

### Finding 1 — The DegT/DnrJ/EryC1 transaminase active site is fully conserved; EryCIV is not a ColD-type dehydratase

The DegT/DnrJ/EryC1 family (PF01041) is a textbook case where one PLP-binding fold supports two divergent chemistries: **C4 transamination** (DesI, ArnB, WecE, EryCI/DesV type) and **C3,4-dehydration** (ColD, AscC). Because these diverged within a single fold, a graft could land eryCIV on the wrong side — the exact shape of Failure Mode #3 — and the tree alone cannot tell. I tested this directly with a Needleman–Wunsch global alignment (BLOSUM62) of EryCIV against characterized members, anchored on literature catalytic residues.

The two diagnostic PLP-handling residues are present and in register. The catalytic Schiff-base lysine, **EryCIV Lys200** (motif `SFHA-T-K-AVTS`), aligns exactly to **ArnB Lys188** (`SFHA-I-K-NITC`) and **WecE Lys181** (`SFHE-T-K-NYTA`) — the lysine that forms the internal aldimine with PLP and is absolutely required for transamination. Crucially, in the dehydratase members that lost transaminase activity this position is occupied instead by **histidine**: cross-alignment confirms the ColD residue aligned to ArnB Lys188 is His. **EryCIV has Lys, not His**, placing it unambiguously on the transaminase side of the split. The PLP pyridine-N1 anchor is likewise conserved: **EryCIV Asp170/171** in motif `FFDAAHA` aligns to **ArnB `EDAAHAV`**, the aspartate that hydrogen-bonds the protonated pyridine nitrogen of PLP.

Pairwise identities reinforce the placement by a roughly two-fold margin:

| Characterized member | Function | % identity to EryCIV |
|---|---|---|
| **DesI** (Q9ZGH0) | C4 sugar aminotransferase | **60.5%** |
| ArnB (P77690) | sugar aminotransferase | 37.5% |
| EryCI (P14290) | C3 sugar aminotransferase | 36.1% |
| DesV (Q9ZGH4) | C3 sugar aminotransferase | 32.5% |
| WecE (P27833) | sugar aminotransferase | 32.4% |
| AscC (Q57174) | PLP 3,4-dehydratase | 23.0% |
| **ColD** (G4WJD4) | PLP 3-dehydratase | **19.8%** |

The ~2-fold identity gap between the nearest transaminase (DesI, 60.5%) and the dehydratases (≤23%), together with the Lys-vs-His discriminator, refutes Failure Mode #3.

### Finding 2 — EryCIV's nearest characterized homolog is DesI, a C4 sugar aminotransferase: the seed term is correct but too general

EryCIV's closest characterized neighbor by a wide margin is **DesI** (60.5% identity over 400 columns). DesI is an X-ray-characterized PLP-dependent aminotransferase that converts **dTDP-4-keto-6-deoxyglucose → dTDP-4-amino-4,6-dideoxyglucose** ([PMID: 17630700](https://pubmed.ncbi.nlm.nih.gov/17630700/)). Because erythromycin (in *S. erythraea*) and methymycin/pikromycin (in *S. venezuelae*) both deploy identical D-desosamine machinery, **eryCIV is the desosamine-pathway ortholog of desI**. This is precisely the granularity failure (Failure Mode #1): the propagated term names the broad *family* activity (any transaminase), while the protein carries out a specific C4 sugar-transamination step. UniProt annotation is concordant — EryCIV carries GO:0008483 (transaminase activity, IEA/TreeGrafter) and GO:0030170 (PLP binding), and the PLP-binding keyword is present.

This finding also surfaces the main **competing / historical** signal: EryCIV was originally deposited under a **"3,4-dehydratase"** name (it was said to "resemble the AscC 3,4-dehydratase"; [PMID: 9353926](https://pubmed.ncbi.nlm.nih.gov/9353926/)). That label predates the structural era and is a **pre-structural homology carry-over** — the same vintage of error that for years left DesI itself mislabeled a "4-dehydrase" despite being a proven aminotransferase. It is directly contradicted by the active-site analysis in Finding 1 (EryCIV has the transaminase Lys, not the dehydratase His) and must not be propagated by a curator.

### Finding 3 — AlphaFold confirms an intact, well-ordered PLP aminotransferase pocket (not a degenerate active site)

To test Failure Mode #2 (fold retained but catalysis lost), I examined AlphaFold DB model **AF-A4F7N3-F1 (v6)**, overall mean **pLDDT 96.5**. The catalytic Schiff-base **Lys200** and the pyridine-N1-anchoring **Asp171** (motif `DAAHA`) co-localize in a single compact pocket, each modeled with very high local confidence (pLDDT 96–99). Measured geometry:

| Residue pair | Distance | Interpretation |
|---|---|---|
| Lys200-NZ ↔ Asp171 carboxyl (OD1) | **6.98 Å** | Consistent with a PLP ring bridging the two anchors; Asp anchors pyridine N1 |
| Lys200-NZ ↔ His174-NE2 | 3.15 Å | Pocket-lining His, H-bonding distance |
| Lys200-NZ ↔ Ser195-OG | 4.52 Å | Pocket-lining Ser |

Active-site pocket residues average **pLDDT 98.1**, indicating a **well-ordered, non-degenerate** catalytic site. There is no evidence of active-site erosion, loop disorder, or catalytic-residue substitution that would mark a pseudo-enzyme. The geometry is consistent with a PLP cofactor bridging Lys200 (internal aldimine) and Asp171 — i.e., an intact, catalytically competent aminotransferase active site. Failure Mode #2 is refuted.

---

## Mechanistic Model / Interpretation

EryCIV operates in the **dTDP-D-desosamine** branch of the erythromycin deoxysugar machinery. Desosamine is one of two sugars (with L-mycarose/L-cladinose) appended to the erythronolide macrolactone; *eryC*-class mutants accumulate 3-α-mycarosyl erythronolide B, the signature of a block in desosamine attachment ([PMID: 9563840](https://pubmed.ncbi.nlm.nih.gov/9563840/)). Within that pathway, EryCIV performs the **C4 transamination** step, installing the amino group that is later elaborated into the dimethylamino function of desosamine:

```
 dTDP-4-keto-6-deoxy-D-glucose
            |
            |   EryCIV (= DesI ortholog)
            |   PLP-dependent C4 transaminase
            |   Lys200 forms internal aldimine with PLP;
            |   Asp171 anchors PLP pyridine N1;
            |   amino donor (L-Glu) -> PMP -> transfer to sugar C4
            v
 dTDP-4-amino-4,6-dideoxy-D-glucose
            |
            |   (downstream N,N-dimethylation, etc.)
            v
        dTDP-D-desosamine  ---->  glycosyl transfer onto erythronolide
```

The family-level ambiguity that makes the graft under-specified — and its resolution:

```
              DegT/DnrJ/EryC1 fold (PF01041, fold-type I PLP)
                               |
        +----------------------+------------------------+
   TRANSAMINASES                                    DEHYDRATASES
 (catalytic Lys at PLP site)                   (His at that position)
 DesI, ArnB, WecE, EryCI, DesV                     ColD, AscC
        |                                               |
   EryCIV sits here  <-- Lys200 present            EryCIV is NOT here
   (60.5% id to DesI)                              (<=23% id; His discriminator absent)
```

The three findings converge on one coherent conclusion: EryCIV has the **right fold, the right subfamily, the right nearest characterized neighbor, and an intact catalytic apparatus**. The only defect in the propagated annotation is **resolution** — it stops at family-level "transaminase activity" rather than naming the specific sugar C4-aminotransferase reaction. This is a true-positive IEA requiring a **granularity refinement**, not a false positive.

---

## Evidence Base

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|----------|---------------|--------|--------------|-------------|---------|--------------------------|
| 1 | [PMID: 17630700](https://pubmed.ncbi.nlm.nih.gov/17630700/) (Burgie & Holden 2007, *Molecular architecture of DesI*) | Structural (X-ray), direct | **Supports** | Is the nearest neighbor a transaminase? | DesI is a PLP-dependent aminotransferase; solved with product dTDP-4-amino-4,6-dideoxyglucose | *S. venezuelae* desosamine pathway | High; DesI is the characterized homolog (not EryCIV itself) |
| 2 | This work (NW alignment, BLOSUM62) | Computational / evolutionary | **Supports** | Nearest characterized neighbor of EryCIV | 60.5% identity to DesI; far above ColD (19.8%), AscC (23.0%) | UniProt sequences | High; linear-gap NW, not a curated MSA |
| 3 | This work (active-site mapping) | Computational / evolutionary | **Supports** (refutes Modes #2 & #3) | Catalytic Lys present (not dehydratase/pseudo-enzyme) | EryCIV Lys200 + Asp170 conserved; ColD has His where transaminases have Lys | Aligned to ArnB K188, WecE K181, ColD | High for Lys call; exact catalysis not wet-assayed |
| 4 | UniProt A4F7N3 (database) | Database | **Qualifies** | Domain/subfamily placement | Pfam PF01041 DegT_DnrJ_EryC1; InterPro IPR030967 **PLP_DesI**; PLP-binding keyword | *S. erythraea* SACE_0716 | High; InterPro signatures can be broad |
| 5 | [PMID: 9353926](https://pubmed.ncbi.nlm.nih.gov/9353926/) (Summers et al. 1997) | Review/database, mutant phenotype | **Competing / qualifies** | Historical "dehydratase" label | EryCIV "resembles AscC 3,4-dehydratase"; eryCIV mutant blocks desosamine | *S. erythraea* genetics | Pre-structural homology carry-over; contradicted by active-site Lys |
| 6 | [PMID: 9563840](https://pubmed.ncbi.nlm.nih.gov/9563840/) (Salah-Bey et al. 1998) | Mutant phenotype | **Supports (pathway role)** | EryCIV required for desosamine | eryC-class mutants accumulate 3-α-mycarosyl-erythronolide B (desosamine-deficient) | *S. erythraea* in vivo | Confirms pathway role, not the exact chemical step |
| 7 | AlphaFold DB AF-A4F7N3-F1 (v6) | Computational / structural | **Supports** (refutes Mode #2) | Active site intact, not degenerate | Lys200 + Asp171 form one well-ordered PLP pocket (pLDDT 96–99); Lys200-NZ↔Asp171 6.98 Å | Predicted structure | High local confidence; predicted (no bound PLP/substrate) |

**How the literature frames the conclusion.** [PMID: 17630700](https://pubmed.ncbi.nlm.nih.gov/17630700/) provides the structural keystone: it establishes DesI — EryCIV's 60.5%-identical nearest neighbor — as a PLP-dependent aminotransferase and defines its exact reaction product, pinning EryCIV's specific function by orthology. [PMID: 9563840](https://pubmed.ncbi.nlm.nih.gov/9563840/) anchors the pathway role genetically, showing eryC-class disruptions produce the desosamine-deficient 3-α-mycarosyl erythronolide B phenotype. [PMID: 9353926](https://pubmed.ncbi.nlm.nih.gov/9353926/) documents the competing historical "3,4-dehydratase" label — the carry-over that motivated the active-site test and that this report recommends against propagating.

---

## Active-Site / Placement Analysis (computed provenance)

**Method:** Needleman–Wunsch global alignment (BLOSUM62, gap −7) of EryCIV against characterized DegT/DnrJ/EryC1 members; catalytic positions anchored on literature residues (ArnB Lys188, WecE Lys181). AlphaFold geometry read from AF-A4F7N3-F1 v6.

**Catalytic PLP Schiff-base lysine — INTACT:**
```
                  catalytic residue v
EryCIV   ...S F H A T K A V T S...   (Lys200)
ArnB     ...S F H A I K N I T C...   (Lys188, catalytic)
WecE     ...S F H E T K N Y T A...   (Lys181, catalytic)
ColD     ...aligned position = His (NOT Lys)  -> dehydratase hallmark
```

**Second PLP anchor (pyridine-N1 Asp) — INTACT:**
`EryCIV FFDAAHA (Asp170)` aligns to `ArnB EDAAHAV`.

**Pairwise % identity to EryCIV (nearest-neighbor placement):**
```
DesI  Q9ZGH0  60.5%   (characterized C4 transaminase)  <- nearest
ArnB  P77690  37.5%   (characterized transaminase)
EryCI P14290  36.1%   (characterized C3 transaminase)
DesV  Q9ZGH4  32.5%   (characterized C3 transaminase)
WecE  P27833  32.4%   (characterized transaminase)
AscC  Q57174  23.0%   (PLP dehydratase)
ColD  G4WJD4  19.8%   (PLP 3-dehydratase)             <- far
```

**AlphaFold structural confirmation (AF-A4F7N3-F1, v6; mean pLDDT 96.5):**
```
Lys200-NZ  <->  Asp171 carboxyl   6.98 Å   (spans a PLP ring; Asp anchors pyridine N1)
Lys200-NZ  <->  His174-NE2        3.15 Å
Lys200-NZ  <->  Ser195-OG         4.52 Å
pocket residues mean pLDDT = 98.1
```

**Conclusion:** Catalytic residues are **intact** and correctly spaced; EryCIV is unambiguously placed in the transaminase subfamily (DesI clade), not the dehydratase clade. The pocket is well-ordered, not degenerate — consistent with a catalytically competent aminotransferase.

---

## GO Curation Implications

Recommended lead action (requires curator verification):

- **GO:0008483 transaminase activity (IEA): RETAIN, but MAKE MORE SPECIFIC.** Replace/augment with a child term reflecting a **dTDP-sugar C4 aminotransferase** (sugar aminotransferase; EC 2.6.1.–). The broad term is not wrong, merely under-granular for a protein with a 60.5%-identical, structurally characterized neighbor of known specific activity.
- **GO:0030170 pyridoxal phosphate binding: RETAIN.** The cofactor keyword and conserved PLP-binding residues confirm it.
- **Biological process:** flag any generic polysaccharide-biosynthesis propagation for the curator — the accurate BP is **dTDP-sugar / desosamine (deoxysugar) biosynthetic process**, not generic polysaccharide biosynthesis.
- **Do NOT** propagate the legacy "3,4-dehydratase" name — a pre-structural carry-over contradicted by the active-site analysis.
- This is a true-positive IEA with a **granularity refinement**. "Protein binding" is explicitly not an appropriate fallback.

---

## Limitations and Knowledge Gaps

1. **No direct enzymatic assay for EryCIV itself.** The specific-function call rests on 60.5% orthology to DesI plus active-site conservation and genetics, not on a purified-enzyme kinetic assay of A4F7N3. Strong but inferential.
2. **AlphaFold is a prediction.** The 6.98 Å Lys200–Asp171 geometry and pocket ordering come from a predicted model (very high pLDDT, but not experimental coordinates); no PLP ligand is present in the model.
3. **Regiochemistry inference.** The exact C4-vs-C3 regiochemistry is inferred from DesI orthology; EryCI/DesV already account for C3 amination in related pathways, making C4 the parsimonious assignment for EryCIV, but this is not experimentally confirmed for A4F7N3.
4. **Reference-set and method scope.** Analysis is sequence/structure-homology based (programmatic UniProt + custom Needleman–Wunsch, linear gap, no curated MSA). The characterized-member panel is representative but not exhaustive; reference catalytic-residue numbering is from the literature while EryCIV numbering is from alignment.
5. **Substrate promiscuity.** [PMID: 9563840](https://pubmed.ncbi.nlm.nih.gov/9563840/) notes some ery deoxysugar enzymes "can accommodate alternative substrates," so the precise in vivo substrate channel is not fully pinned by sequence alone.

---

## Proposed Follow-up Experiments / Actions

1. **Curator action (immediate):** Refine the EryCIV annotation from family-level GO:0008483 to the specific sugar C4-aminotransferase child term, citing orthology-to-DesI ([PMID: 17630700](https://pubmed.ncbi.nlm.nih.gov/17630700/)) as ISS/ISO support; flag the "3,4-dehydratase" name as deprecated carry-over.
2. **Direct biochemical confirmation:** Express and purify EryCIV, reconstitute with PLP, and assay transamination of **dTDP-4-keto-6-deoxy-D-glucose + L-glutamate**, detecting dTDP-4-amino-4,6-dideoxyglucose by LC-MS; include the **K200A** mutant as a loss-of-function control. This directly closes the one inferential gap.
3. **Cross-complementation genetics:** Test whether eryCIV complements a *desI* mutant of *S. venezuelae* (and vice versa), confirming functional orthology in vivo.
4. **Structural validation:** Solve EryCIV with PLP (or PMP + sugar-nucleotide), or 3-D superpose the AlphaFold model onto the DesI structure, to confirm the predicted Lys200/Asp171 geometry and substrate pose.
5. **Genome paralog check:** Confirm no second DegT/DnrJ/EryC1 paralog in *S. erythraea* has been confused with eryCIV in the annotation pipeline, ruling out orthology-assignment error at the genome level.

---

### Bottom line

EryCIV (A4F7N3) is a **genuine PLP-dependent sugar aminotransferase** — the desosamine-pathway ortholog of DesI. The TreeGrafter/PANTHER graft identified the correct *kind* of activity (transaminase) but stopped at the family level. The decidable, evidence-backed action is to **retain the transaminase assignment and make it more specific** (dTDP-4-amino-4,6-dideoxy-D-glucose C4 aminotransferase). The pseudo-enzyme and wrong-subfamily failure modes are affirmatively ruled out by the intact catalytic lysine, the Lys-vs-His discriminator, and the well-ordered AlphaFold active site.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)