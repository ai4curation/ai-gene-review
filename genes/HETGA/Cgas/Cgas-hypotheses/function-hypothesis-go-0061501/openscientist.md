---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T23:15:29.929353'
end_time: '2026-10-14T23:33:19.253125'
duration_seconds: 1069.32
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: HETGA
  gene: Cgas
  gene_symbol: Cgas
  uniprot_accession: A0AAX6RS70
  taxon_id: NCBITaxon:10181
  taxon_label: Heterocephalus glaber
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0061501
  hypothesis_text: Cgas has 2',3'-cyclic GMP-AMP synthase activity (GO:0061501).
  term_context: '- Term: 2'',3''-cyclic GMP-AMP synthase activity (GO:0061501)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118'
  source_file: genes/HETGA/Cgas/Cgas-ai-review.yaml
  source_selector: existing_annotations[11].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0061501\n  label: 2',3'-cyclic GMP-AMP synthase\
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

- **Organism code:** HETGA
- **Taxon:** Heterocephalus glaber (NCBITaxon:10181)
- **Gene directory:** Cgas
- **Gene symbol:** Cgas
- **UniProt accession:** A0AAX6RS70

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0061501
- **Source file:** genes/HETGA/Cgas/Cgas-ai-review.yaml
- **Source selector:** existing_annotations[11].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

Cgas has 2',3'-cyclic GMP-AMP synthase activity (GO:0061501).

## Term and Decision Context

- Term: 2',3'-cyclic GMP-AMP synthase activity (GO:0061501)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118

## Source Context YAML

```yaml
term:
  id: GO:0061501
  label: 2',3'-cyclic GMP-AMP synthase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **Cgas directly has the stated function**. Automated
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

**Target:** *Heterocephalus glaber* (naked mole-rat) Cgas — UniProt **A0AAX6RS70** (554 aa)
**Seed hypothesis (TreeGrafter/PANTHER, IEA, GO_REF:0000118):** Cgas has **2',3'-cyclic GMP-AMP synthase activity (GO:0061501)**
**Verdict:** **SUPPORTED** — the propagated term is correct and already at maximal specificity. **RETAIN.**

---

## Summary

The naked mole-rat protein A0AAX6RS70 ("Cgas") was electronically annotated with **2',3'-cyclic GMP-AMP synthase activity (GO:0061501)** by the TreeGrafter/PANTHER phylogenetic pipeline. The task was to independently judge whether this protein *directly* performs that function, and — because automated propagation can silently fail — to actively test three characteristic failure modes: (1) granularity (the term being a broad family function rather than this protein's specific subfamily activity), (2) pseudo-enzyme status (a conserved fold with a degenerate active site), and (3) within-superfamily mis-placement (grafting onto a structurally related but functionally distinct neighbor of the shared Mab-21 nucleotidyltransferase fold).

Across three iterations of analysis — domain-architecture inspection, global pairwise alignment to characterized human and mouse cGAS, residue-level active-site mapping, and a paralog-discrimination panel across the Mab-21 superfamily — **all three failure modes were explicitly tested and excluded.** The protein was grafted to the cGAS-specific subfamily node (PANTHER **PTHR10656:SF35, "CYCLIC GMP-AMP SYNTHASE"**), not the broad family node, so there is no granularity problem. Its complete catalytic apparatus — the three-acidic-residue Mg²⁺-coordinating triad and the zinc thumb — is conserved with **zero substitutions, insertions, or deletions**, so it is not a pseudo-enzyme. And its nearest characterized neighbor, by a wide margin, is cGAS itself (≈57% global identity to both human and mouse cGAS), ruling out paralog mis-placement.

The conclusion is that the seed hypothesis is **SUPPORTED**: A0AAX6RS70 is a bona fide mammalian cGAS ortholog that directly performs the 2',3'-cGAMP synthase reaction (ATP + GTP → 2',3'-cGAMP). GO:0061501 should be **retained** at its current granularity; no generalization, sibling-replacement, or removal is warranted. The only residual limitation is the absence of a direct biochemical assay in *H. glaber* — all evidence is sequence/structure-based orthology inference, which is strong but formally inferential.

---

## Key Findings

### Finding 1 — A0AAX6RS70 is a genuine cGAS ortholog with fully intact catalytic machinery

The UniProt record for A0AAX6RS70 (554 aa, *Heterocephalus glaber*) carries the submission name "Cyclic GMP-AMP synthase isoform X1" and the canonical cGAS domain signature: Pfam **PF03281 (Mab-21)** plus **PF20266 (Mab-21_C)**, and InterPro **IPR046903** (Mab-21-like nucleotidyltransferase, residues 246–420) plus **IPR046906** (HhH / H2TH-like, residues 437–541). This is the two-lobed architecture of mammalian cGAS: an N-terminal nucleotidyltransferase (NTase) catalytic lobe fused to a C-terminal Mab-21 helix-hairpin-helix / zinc-thumb DNA-binding lobe.

Crucially, PANTHER placed the protein at **PTHR10656:SF35 = "CYCLIC GMP-AMP SYNTHASE"** — a *subfamily-level* node specific to cGAS, not the broad pan-Mab-21 family node. The GO propagation therefore originated from the cGAS-specific clade, which immediately removes the most common granularity failure: the term inherited is the subfamily function, not a generic family function.

A Needleman–Wunsch global alignment (BLOSUM62) of A0AAX6RS70 against human CGAS (Q8N884) gives **57.2% whole-chain identity (297/519 aligned positions)** and **76.9% identity across the catalytic core** (human positions ~212–421). The whole-chain divergence is concentrated in the intrinsically disordered, low-complexity N-terminus (roughly residues 28–197), which is not part of the catalytic machinery and is expected to vary across species. Within the catalytic core, every functional residue is conserved:

| Functional role | Human cGAS (Q8N884) | NMR Cgas (A0AAX6RS70) | Status |
|---|---|---|---|
| Mg²⁺-coordinating catalytic acid | Glu225 | **Glu257** | Conserved |
| Mg²⁺-coordinating catalytic acid | Asp227 | **Asp259** | Conserved |
| Mg²⁺-coordinating catalytic acid | Asp319 | **Asp351** | Conserved |
| Zinc thumb | His390 | **His422** | Conserved |
| Zinc thumb | Cys396 | **Cys428** | Conserved |
| Zinc thumb | Cys397 | **Cys429** | Conserved |
| Zinc thumb | Cys404 | **Cys436** | Conserved |

There are **no substitutions, insertions, or deletions at any active-site, catalytic, or metal-binding position**, and the spacing between residues is preserved. The E–D–D triad coordinates the two divalent metal ions (Mg²⁺, or Mn²⁺) required for the two-metal-ion nucleotidyl-transfer chemistry, and the C₃H₁ zinc thumb stabilizes the activation loop and mediates DNA binding. A protein that conserves this entire apparatus in a mammal performs the mammal-specific 2',3'-cGAMP reaction. This excludes the pseudo-enzyme failure mode.

The canonical reaction is firmly established in the primary literature: cGAS is activated by cytosolic double-stranded DNA and uses ATP and GTP to synthesize the cyclic dinucleotide second messenger 2',3'-cGAMP ([PMID: 42810574](https://pubmed.ncbi.nlm.nih.gov/42810574/); [PMID: 41806557](https://pubmed.ncbi.nlm.nih.gov/41806557/)). This reaction corresponds precisely to GO:0061501.

### Finding 2 — The sequence is cGAS, not a Mab-21 family paralog (rules out within-superfamily mis-placement)

The Mab-21 superfamily contains several paralogs (MAB21L1, MAB21L2, MAB21L3, MB21D2) that share the NTase/Mab-21 fold but lack cGAS catalytic activity. To exclude the third failure mode — grafting onto a structurally related but functionally distinct neighbor — we computed the global Needleman–Wunsch percent identity of A0AAX6RS70 against each characterized superfamily member:

| Query vs | % identity (aligned) | Note |
|---|---|---|
| **cGAS (human, Q8N884)** | **57.2% (297/519)** | nearest neighbor |
| **cGAS (mouse, Q8C6L5)** | **57.1% (287/503)** | ortholog, co-top hit |
| MAB21L3 (Q8N816) | 45.7% (118/258) | short alignment; paralog |
| MAB21L2 (Q9Y586) | 34.3% (123/359) | paralog, no cGAS activity |
| MAB21L1 (Q13394) | 33.4% (120/359) | paralog, no cGAS activity |
| MB21D2 (Q8IYB1) | 19.1% (94/491) | distant |

The nearest neighbors are the two cGAS orthologs, and the margin over the next-closest paralog (MAB21L3) is large — ~12 percentage points, and the MAB21L3 match spans only 258 positions versus full-length coverage for cGAS. Over the next tier (MAB21L1/2) the margin is ~23 percentage points. Decisively, the **cGAS-diagnostic zinc thumb (His422/Cys428/Cys429/Cys436)** is present in A0AAX6RS70 — this motif is a hallmark of cGAS and is **absent** from the MAB21L1/2 paralogs that lack cGAS activity. The combination of (i) best global match to cGAS, (ii) full-length coverage of the catalytic core, and (iii) the cGAS-specific zinc thumb jointly excludes any within-superfamily mis-placement.

---

## Mechanistic Model / Interpretation

The logical structure of the stress test — and how each failure mode was tested and excluded — is summarized below.

```
               TreeGrafter grafts A0AAX6RS70 → PANTHER PTHR10656:SF35
                          propagates GO:0061501 (IEA)
                                     |
          -------------------------------------------------------
          |                          |                          |
  (1) GRANULARITY?           (2) PSEUDO-ENZYME?         (3) MIS-PLACEMENT?
  Broad family node, so      Fold intact but active     Grafted onto a
  term is too general?       site degenerate?           different Mab-21
                                                        paralog, not cGAS?
          |                          |                          |
  Node = SF35, cGAS-         E257/D259/D351 triad       Best global match =
  SPECIFIC subfamily.        intact; zinc thumb         cGAS (57.2%), >12 pts
  No child term exists;      H422/C428/C429/C436        above nearest paralog;
  term already maximally     intact; 0 indels at        cGAS-specific zinc
  specific.                  active site.               thumb present.
          |                          |                          |
     NOT A PROBLEM              NOT A PROBLEM              NOT A PROBLEM
          -------------------------------------------------------
                                     |
                       VERDICT: SUPPORTED — RETAIN GO:0061501
```

The domain architecture of cGAS (and of A0AAX6RS70):

```
 N-term (disordered, divergent)   NTase catalytic lobe        Mab-21 / zinc-thumb DNA-binding lobe
 |----------~245 aa-------------|--IPR046903 (246–420)-----|--IPR046906 HhH/H2TH (437–541)--|
                                   Mg2+ triad:                 Zinc thumb:
                                   E257, D259, D351            H422, C428, C429, C436
```

Biologically this is fully coherent. cGAS is the principal cytosolic dsDNA sensor of the cGAS–STING innate-immune axis. On binding dsDNA it undergoes allosteric activation and, using ATP and GTP with two catalytic metal ions, synthesizes 2',3'-cGAMP — the cyclic dinucleotide that binds STING and triggers type-I interferon signaling. The defining feature of the *mammalian* enzyme is the mixed 2'-5'/3'-5' phosphodiester linkage of its product (hence "2',3'-cGAMP"), which is exactly what GO:0061501 encodes. The naked mole-rat ortholog preserves every residue that executes this chemistry, and its sequence divergence is confined to the disordered, non-catalytic N-terminus, which is typical of cross-species cGAS comparison. Nothing in the sequence suggests a functional pivot to a different activity.

---

## Evidence Base

| # | Citation (PMID) | Evidence type | Role | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | Our analysis (UniProt A0AAX6RS70; InterPro/Pfam; PANTHER SF35) | Computational / database | Supports | Correct subfamily graft? | Name "Cyclic GMP-AMP synthase isoform X1"; PF03281+PF20266; IPR046903+IPR046906; grafted to cGAS-specific node PTHR10656:SF35 | *H. glaber*, 554 aa | High; annotations are automated but mutually consistent and corroborated by independent alignment |
| 2 | Our analysis (NW alignment to Q8N884) | Structural / evolutionary (computational) | Supports | Catalytic residues conserved and spaced? | 57.2% whole-chain / 76.9% catalytic-core identity; Mg²⁺ triad E257/D259/D351 and zinc thumb H422/C428/C429/C436 all identical, 0 indels at active site | vs human cGAS | High; sequence-based, no experimental HETGA assay |
| 3 | Our analysis (paralog panel) | Evolutionary (computational) | Supports / competing-excluded | Is this really a different paralog? | Nearest neighbor is cGAS (57.2%/57.1%) vs MAB21L3 45.7% (short span), MAB21L1/2 ~33–34%, MB21D2 19.1%; cGAS-specific zinc thumb present | Mab-21 superfamily | High; clear separation margin |
| 4 | [PMID: 42810574](https://pubmed.ncbi.nlm.nih.gov/42810574/) | Review / direct-assay basis | Supports | Exact cGAS reaction | "cyclic GMP-AMP synthase (cGAS) catalyzes ATP and GTP to synthesize the cyclic dinucleotide 2',3'-cGAMP" | mammalian cGAS | High for defining the reaction matching GO:0061501 |
| 5 | [PMID: 41806557](https://pubmed.ncbi.nlm.nih.gov/41806557/) | Review / structural | Supports | Canonical activity | "structural basis of cGAS activation by dsDNA and its catalytic synthesis of 2'3'-cGAMP" | mammalian cGAS–STING | High for canonical activity |
| 6 | [PMID: 28940468](https://pubmed.ncbi.nlm.nih.gov/28940468/) | Direct assay / kinetic | Qualifies | Product distribution | First kinetic constants for 2',3'-cGAMP formation; notes 2',3'-cGAMP may be a *minor* product vs linear nucleotides in vitro | human cGAS | Qualifier on efficiency/product ratio, not on identity of the activity |
| 7 | [PMID: 32814054](https://pubmed.ncbi.nlm.nih.gov/32814054/) | Mechanistic | Qualifies | Metal dependence | DNA binding allosterically activates cGAS to synthesize 2'3'-cGAMP using Mg²⁺ (and Mn²⁺) | cGAS mechanism | Supports metal-dependent catalysis consistent with conserved triad |

**How the literature supports the call.** [PMID: 42810574](https://pubmed.ncbi.nlm.nih.gov/42810574/) and [PMID: 41806557](https://pubmed.ncbi.nlm.nih.gov/41806557/) jointly establish that the canonical, defining activity of mammalian cGAS is dsDNA-activated synthesis of 2',3'-cGAMP from ATP and GTP — i.e., exactly GO:0061501. [PMID: 32814054](https://pubmed.ncbi.nlm.nih.gov/32814054/) confirms the two-metal-ion mechanism that the conserved E257/D259/D351 triad serves. [PMID: 28940468](https://pubmed.ncbi.nlm.nih.gov/28940468/) provides a careful qualifier: in vitro, the 2',3'-cGAMP product can be minor relative to linear di-nucleotides — but this concerns catalytic efficiency and product ratio, not the identity of the enzyme or the validity of assigning GO:0061501. None of the reviewed literature challenges the assignment.

---

## Active-Site / Placement Analysis (Provenance)

**Method:** Global pairwise Needleman–Wunsch alignment (BLOSUM62) of A0AAX6RS70 against human cGAS (Q8N884) and against a panel of characterized Mab-21 superfamily paralogs (Q8C6L5, Q13394, Q9Y586, Q8N816, Q8IYB1). Active-site positions were mapped from human cGAS numbering to the naked mole-rat sequence via the alignment. Sequences retrieved from UniProt REST; alignment executed in-session.

**Catalytic / metal-binding residue conservation — verdict: FULLY INTACT**

| Site | Human position | NMR position | Conserved? |
|---|---|---|---|
| Mg²⁺ triad | Glu225 | Glu257 | ✔ |
| Mg²⁺ triad | Asp227 | Asp259 | ✔ |
| Mg²⁺ triad | Asp319 | Asp351 | ✔ |
| Zinc thumb | His390 | His422 | ✔ |
| Zinc thumb | Cys396 | Cys428 | ✔ |
| Zinc thumb | Cys397 | Cys429 | ✔ |
| Zinc thumb | Cys404 | Cys436 | ✔ |

**Subfamily placement — verdict: cGAS is the nearest characterized neighbor** (see Finding 2 table). Catalytic-core identity to human cGAS is 76.9%; whole-chain 57.2% (297/519), with divergence confined to the disordered N-terminus.

**Explicit statement:** The catalytic and metal-binding residues are **intact and correctly spaced**, and the protein's nearest characterized neighbor is **cGAS**. Both independent tests converge on an active cGAS enzyme. No pseudo-enzyme signature; no paralog mis-placement.

---

## GO Curation Implications

**Recommended curator action (lead requiring verification): RETAIN GO:0061501 (2',3'-cyclic GMP-AMP synthase activity).**

- The term is correct and at the right granularity — **same** granularity as the seed; it is a leaf-level molecular-function term encoding the diagnostic mixed 2'-5'/3'-5' linkage, so no more-specific child exists ("make-more-specific" not applicable).
- Do **not** generalize to a parent nucleotidyltransferase term — that would discard well-supported specificity.
- Do **not** replace with a sibling term — there is no evidence of a diverged or sibling activity; the paralog panel excludes MAB21L-type functions.
- Do **not** remove — the active site is intact and the ortholog assignment is unambiguous.
- Treat as a **core** molecular-function annotation for cGAS.

Because the current evidence code is **IEA** (electronic, GO_REF:0000118), the annotation remains inference-based. The convergent active-site conservation and paralog-distance evidence substantially raise confidence and could justify a curator-reviewed phylogenetic evidence note; a direct assay would be required to upgrade to an experimental code (IDA). "Protein binding" is explicitly *not* an appropriate fallback.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical assay in *H. glaber*.** All conclusions rest on orthology plus active-site conservation. Conserved residues strongly predict, but do not prove, catalytic competence and the exact 2',3' product regiochemistry.
2. **Alignment-based residue mapping.** Active-site positions were transferred from human cGAS numbering via global alignment rather than from an experimental naked mole-rat structure. An AlphaFold model superposition would add geometric confirmation but was not run.
3. **Product-ratio nuance.** Human-cGAS kinetics ([PMID: 28940468](https://pubmed.ncbi.nlm.nih.gov/28940468/)) note that 2',3'-cGAMP can be a minor product relative to linear nucleotides in vitro. This concerns output proportions, not enzyme identity or the validity of GO:0061501.
4. **Database carry-over.** UniProt submission name and PANTHER/InterPro calls are themselves automated; however they are mutually consistent and corroborated by the independent active-site alignment, so paralog confusion (Mab21L1/2 or cGLR) is ruled out by the cGAS-diagnostic residue set.
5. **Species-specific innate-immune biology.** Naked mole-rats have notable immune and longevity peculiarities; whether NMR cGAS has altered regulation (DNA affinity, STING coupling) is unknown — relevant to downstream biological-process annotation but outside the scope of this molecular-function term.
6. **Isoform scope.** The record is "isoform X1"; alternative isoforms were not individually assessed.

---

## Proposed Follow-up Experiments / Actions

1. **Direct activity assay (definitive).** Express recombinant NMR Cgas, activate with dsDNA, incubate with ATP/GTP + Mg²⁺, and detect 2',3'-cGAMP by LC-MS/MS (with linkage analysis to confirm the 2'-5'/3'-5' bond) or via a STING-reporter activation readout. This is the single most efficient experiment to convert IEA → IDA and settle any residual doubt.
2. **AlphaFold structural superposition.** Superpose the AlphaFold model of A0AAX6RS70 on a human cGAS–DNA–nucleotide complex to confirm the 3D spacing of E257/D259/D351 and the zinc thumb, complementing the sequence-level conservation.
3. **Phylogenetic tree reconstruction.** Build a maximum-likelihood tree across the Mab-21 superfamily including the query, to visually confirm it falls inside the cGAS clade rather than at an internal paralog-splitting node — independent corroboration of the PANTHER SF35 graft.
4. **Curator note.** Record the active-site conservation table and paralog-distance panel as provenance supporting retention of GO:0061501, documenting that all three TreeGrafter failure modes were explicitly tested and excluded.

---

## Conclusion

The TreeGrafter/PANTHER propagation of **GO:0061501** to naked mole-rat **Cgas (A0AAX6RS70)** is **correct**. The protein is a genuine mammalian cGAS ortholog grafted to the cGAS-specific subfamily node (PTHR10656:SF35), with the complete catalytic Mg²⁺-coordinating triad (E257/D259/D351 = human E225/D227/D319) and zinc thumb (H422/C428/C429/C436 = human H390/C396/C397/C404) perfectly conserved, and with cGAS as its unambiguous nearest characterized neighbor (~57% global identity, ~12–23 points above the next paralog). None of the three characteristic failure modes — granularity, pseudo-enzyme, or within-superfamily mis-placement — applies. **Curation action: RETAIN at current granularity.**

---
*Provenance: UniProt REST (A0AAX6RS70, Q8N884, Q8C6L5, Q13394, Q9Y586, Q8N816, Q8IYB1); custom Needleman–Wunsch alignment (BLOSUM62) executed in-session; PubMed PMIDs 41806557, 42810574, 28940468, 32814054, 41738955.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)