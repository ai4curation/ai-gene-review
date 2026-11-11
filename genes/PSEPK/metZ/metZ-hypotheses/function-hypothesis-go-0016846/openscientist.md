---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T03:38:21.925746'
end_time: '2026-10-15T04:33:49.554588'
duration_seconds: 3327.63
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: PSEPK
  gene: metZ
  gene_symbol: metZ
  uniprot_accession: Q88LD4
  taxon_id: NCBITaxon:160488
  taxon_label: Pseudomonas putida KT2440
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0016846
  hypothesis_text: metZ has carbon-sulfur lyase activity (GO:0016846).
  term_context: '- Term: carbon-sulfur lyase activity (GO:0016846)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - file:PSEPK/metZ/metZ-uniprot.txt

    - file:PSEPK/metZ/metZ-goa.tsv

    - file:PSEPK/metZ/metZ-deep-research-openscientist.md'
  source_file: genes/PSEPK/metZ/metZ-ai-review.yaml
  source_selector: existing_annotations[4].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0016846\n  label: carbon-sulfur lyase activity\n\
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
citation_count: 2
artifact_count: 3
artifact_sources:
  openscientist_artifacts_zip: 3
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
- filename: provenance_metZ_subfamily_placement.md
  path: openscientist_artifacts/provenance_metZ_subfamily_placement.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist metZ subfamily placement
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
- **Gene directory:** metZ
- **Gene symbol:** metZ
- **UniProt accession:** Q88LD4

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0016846
- **Source file:** genes/PSEPK/metZ/metZ-ai-review.yaml
- **Source selector:** existing_annotations[4].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

metZ has carbon-sulfur lyase activity (GO:0016846).

## Term and Decision Context

- Term: carbon-sulfur lyase activity (GO:0016846)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- file:PSEPK/metZ/metZ-uniprot.txt
- file:PSEPK/metZ/metZ-goa.tsv
- file:PSEPK/metZ/metZ-deep-research-openscientist.md

## Source Context YAML

```yaml
term:
  id: GO:0016846
  label: carbon-sulfur lyase activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **metZ directly has the stated function**. Automated
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

**Target:** metZ (UniProt **Q88LD4**), *Pseudomonas putida* KT2440 (NCBITaxon:160488)
**Seed hypothesis under test:** metZ has **carbon-sulfur lyase activity (GO:0016846)** — propagated by TreeGrafter/PANTHER (IEA, GO_REF:0000118)
**Hypothesis slug:** function-hypothesis-go-0016846

---

## Executive Judgment

**Verdict: REFUTED — Within-superfamily mis-placement (Failure Mode 3).**

The TreeGrafter/PANTHER graft that assigned **carbon-sulfur lyase activity (GO:0016846)** to metZ is **wrong**. metZ is not a lyase at all; it is a **PLP-dependent O-succinylhomoserine sulfhydrylase**, a **transferase** (EC 2.5.1.-) that catalyzes direct sulfhydrylation in methionine biosynthesis. The graft placed the query onto a structurally related but functionally *distinct* neighboring subfamily of the shared **Cys/Met-metabolism PLP-dependent (transsulfuration) fold superfamily** — specifically the cystathionine γ-lyase branch (PANTHER PTHR11808:SF80) — whose enzymes cleave carbon–sulfur bonds in the *reverse* chemical direction.

The single most decisive piece of evidence: metZ is **82.1% identical** to the experimentally characterized *P. aeruginosa* MetZ O-succinylhomoserine sulfhydrylase (P55218, EC 2.5.1.-, a transferase), but only **~36.5% identical** to human cystathionine γ-lyase (P32929, EC 4.4.1.1, the C–S lyase whose label drove the graft). The nearest *characterized* neighbor is unambiguously a transferase, and its reaction chemistry — net **addition** of sulfide to O-succinylhomoserine — is the opposite of the "elimination of hydrogen sulfide" that defines GO:0016846.

This is **not** a pseudo-enzyme (Failure Mode 2): the catalytic PLP Schiff-base lysine (K219, within the canonical **SATKF** motif) is intact and correctly spaced, confirming the protein is a fully active enzyme. And it is **not** a mere granularity problem (Failure Mode 1): the issue is not that GO:0016846 is "too broad" but that it names the **wrong reaction class** (lyase vs. transferase) in a sibling subfamily. The correct molecular-function branch is **transferase**, not lyase.

---

## Independent Family/Function Assignment

From primary evidence, metZ (Q88LD4) is an **O-succinylhomoserine sulfhydrylase**:

> O-succinyl-L-homoserine + H₂S → L-homocysteine + succinate

This is the first (and in *P. putida*, the committed) step of L-homocysteine synthesis from O-succinylhomoserine, feeding directly into **L-methionine biosynthesis** via **direct sulfhydrylation**. The enzyme is PLP-dependent (cofactor pyridoxal 5′-phosphate, covalently bound as N6-(pyridoxal phosphate)-lysine at **K219**).

| Attribute | Independent assignment |
|---|---|
| **Specific MF** | O-succinylhomoserine sulfhydrylase |
| **EC class** | EC 2.5.1.- (**transferase**, transferring alkyl/aryl groups other than methyl) |
| **Recommended GO term** | **GO:0016765** — transferase activity, transferring alkyl or aryl (other than methyl) groups |
| **Characterized homolog basis** | *P. aeruginosa* MetZ (P55218), 82.1% identical, experimentally characterized sulfhydrylase |
| **Granularity vs. seed (GO:0016846)** | **Different branch** — the seed term is in the lyase (EC 4) ontology branch; the correct term is in the transferase (EC 2) branch. Not "same," not "more specific," not a close sibling within one activity — a different reaction class. |

Notably, QuickGO already shows Q88LD4 carrying **GO:0016765** (UniRule UR000282477) — the branch-correct transferase term — *alongside* the disputed GO:0016846. The curation task is therefore to correct a conflicting, mis-grafted lyase annotation that coexists with the correct transferase annotation.

---

## Key Findings

### Finding 1 — metZ is a PLP-dependent sulfhydrylase (transferase), not a carbon-sulfur lyase

The reviewed UniProt entry for Q88LD4, annotated via HAMAP rule **MF_02056** ("MetZ subfamily"), gives the recommended name **O-succinylhomoserine sulfhydrylase** with EC class **2.5.1.-** — unambiguously the **transferase** class. The catalytic reaction it annotates is *O-succinyl-L-homoserine + H₂S → L-homocysteine + succinate*, with PLP cofactor bound at **K219** and a pathway assignment of *L-methionine biosynthesis; L-homocysteine from O-succinyl-L-homoserine, step 1 of 1*.

Crucially, the Gene Ontology definition of the seed term **GO:0016846 (carbon-sulfur lyase activity)** describes the **elimination of hydrogen sulfide** — a β- or γ-**elimination** that *breaks* a C–S bond and *releases* sulfide. metZ does the chemical opposite: it nets the **addition** of sulfide (H₂S) across O-succinylhomoserine to build homocysteine. A reaction that consumes H₂S to form a C–S bond cannot be described by a term defined as sulfide elimination. This directional mismatch is dispositive at the level of reaction chemistry, independent of any sequence analysis.

This finding is directly supported by the primary literature that first identified and sequenced metZ:

> *"The second step is achieved by direct sulfhydrylation, involving the enzyme encoded by a metZ gene that we have identified and sequenced"* — [PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/)

Direct sulfhydrylation is a γ-replacement/transferase reaction, not a lyase cleavage. This establishes the enzyme's mechanism from experimental work, not from database inference.

### Finding 2 — The nearest *characterized* homolog is a transferase (82% identity); C–S lyases are distant (≤37%)

To localize the graft error, pairwise global (Needleman–Wunsch) alignments were computed between the query Q88LD4 and a panel of characterized members of the transsulfuration/Cys-Met PLP superfamily spanning both the transferase and lyase branches:

| Characterized protein | Accession | Activity | EC | Class | % identity to Q88LD4 |
|---|---|---|---|---|---|
| *P. aeruginosa* MetZ | P55218 | O-succinylhomoserine sulfhydrylase | 2.5.1.- | **Transferase** | **82.1%** |
| *E. coli* MetB | P00935 | cystathionine γ-synthase | 2.5.1.48 | **Transferase** | 38.0% |
| Human CTH | P32929 | cystathionine γ-lyase | 4.4.1.1 | **C–S lyase** | 36.5% |
| *E. coli* MetC | P06721 | cystathionine β-lyase | 4.4.1.8 | **C–S lyase** | 25.0% |

The query is overwhelmingly closest (82%) to a **characterized transferase** and far more distant (≤37%) from any **carbon-sulfur lyase**. Critically, human CTH (P32929, EC 4.4.1.1) corresponds to the label of **PANTHER subfamily PTHR11808:SF80 ("cystathionine gamma-lyase")** — the node that drove the GO:0016846 graft. The query sits ~46 percentage points of identity closer to the transferase than to the lyase that supplied the term. The graft reached across the superfamily to a sibling subfamily with the wrong chemistry.

The organismal biology reinforces this placement. The classic survey of *P. putida* sulfur metabolism reports:

> *"Both these organisms used direct sulfhydrylation of O-succinylhomoserine for the synthesis of methionine"* — [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/)

and, decisively against the lyase assignment:

> *"no cystathionine gamma-lyase, the key enzyme of the reverse transsulfuration pathway, was found in this species"* — [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/)

So the very activity named by the PANTHER SF80 label — cystathionine γ-lyase — **does not exist in *P. putida***. There is no enzyme in this organism to which GO:0016846 (via the γ-lyase label) could correctly apply, let alone metZ, which performs the biosynthetic transferase step.

### Finding 3 — The catalytic PLP Schiff-base lysine (K219, SATKF) is intact: this rules out the pseudo-enzyme failure mode

A motif scan for the canonical PLP Schiff-base lysine signature **[S/A]-A-T-K-[F/Y]** across the superfamily shows the catalytic lysine is present and correctly positioned in the query:

| Protein | Motif | Catalytic Lys position |
|---|---|---|
| **Q88LD4 (metZ, query)** | **SATKF** | **K219** (matches UniProt N6-(PLP)-lysine feature) |
| *P. aeruginosa* MetZ (P55218) | SATKY | K219 (identical position) |
| *E. coli* MetB (P00935) | CTKY | ~K198 |
| Human CTH (P32929) | SATKY | ~K212 |
| *E. coli* MetC (P06721) | ATKY | ~K210 |

The query's catalytic lysine is intact, matches the UniProt feature annotation exactly, and is spaced consistently with active family members. The fold's active-site machinery is therefore **complete** — metZ is a catalytically competent enzyme, not a degenerate pseudo-enzyme. This finding closes off Failure Mode 2. It is, however, family-wide: the PLP lysine alone is shared by both transferases and lyases of this superfamily, so it confirms catalytic competence but does **not** by itself discriminate transferase from lyase. The discrimination comes from Finding 1 (reaction direction / UniProt-HAMAP subfamily rule MF_02056) and Finding 2 (nearest characterized neighbor + organism gene content).

---

## Mechanistic Model / Interpretation

### The reaction metZ actually catalyzes

```
   O-succinyl-L-homoserine  +  H2S
                 |
                 |   metZ (Q88LD4), PLP-dependent, K219
                 |   DIRECT SULFHYDRYLATION  (net ADDITION of sulfide)
                 v
   L-homocysteine  +  succinate   --->  (methylation) --->  L-methionine
```

This is **transferase** chemistry (EC 2.5.1.-, GO:0016765): a sulfur nucleophile (H₂S) is added across the substrate to forge a new **C–S bond**.

### The reaction GO:0016846 actually describes

```
   substrate-C-S  --->  C=C / C  +  H2S        (carbon-sulfur LYASE; elimination of H2S)
```

This is **lyase** chemistry (EC 4.4.1.-): a C–S bond is **broken** and sulfide **released** — the opposite net transformation. Assigning this term to metZ inverts the enzyme's chemistry.

### How the graft went wrong (within-superfamily mis-placement)

```
  Cys/Met-metabolism PLP-dependent (transsulfuration) fold SUPERFAMILY
  (one shared fold, shared PLP-K catalytic lysine, several activities)
  ─────────────────────────────────────────────────────────────────────
   TRANSFERASE branch (EC 2.5.1)            LYASE branch (EC 4.4.1)
     • MetZ  O-succinylhomoserine             • cystathionine γ-lyase (CTH)
       sulfhydrylase   <-- QUERY (82% id)       EC 4.4.1.1  <-- PANTHER SF80 label
     • MetB  cystathionine γ-synthase          • cystathionine β-lyase (MetC)
       EC 2.5.1.48                               EC 4.4.1.8
                     \                         /
                      \   graft crossed here  /
                       --->  GO:0016846  <----  (WRONG branch for the query)
```

Because all members share one fold and the same catalytic PLP lysine, a graft that keys on fold-level features can land on the wrong subfamily. TreeGrafter propagated the lyase-branch term from an ancestral/subfamily node (SF80, γ-lyase) even though the query's actual nearest *characterized* neighbor — and the HAMAP MF_02056 "MetZ subfamily" rule that reviewers applied — place it firmly in the **transferase** branch. The failure is invisible to the graft itself (both branches have the PLP lysine and the same fold); it is only exposed by (a) comparing against the nearest *characterized* homolog, (b) reading the reaction direction, and (c) checking the host organism's gene content — exactly the three tests this stress test requires.

---

## Evidence Base / Evidence Matrix

| # | Citation | Evidence type | Role | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|---|
| 1 | UniProt Q88LD4 (HAMAP MF_02056); QuickGO | Review/database | **Refutes** seed | Is metZ a lyase or transferase? | Recommended name O-succinylhomoserine sulfhydrylase; EC 2.5.1.- (transferase); reaction nets H₂S *addition*; carries GO:0016765 (transferase) via UR000282477 | Reviewed entry; curated rule | High for class assignment; database-derived, not a fresh assay |
| 2 | GO:0016846 definition | Review/database | **Refutes** seed | Does term chemistry match metZ? | Term = "elimination of hydrogen sulfide" (C–S bond cleavage) — opposite direction to metZ | Ontology definition | High; definitional, direction-dispositive |
| 3 | [PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/) | Direct (gene ID + mechanism) | **Refutes** seed / supports transferase | Mechanism of metZ step | metZ catalyzes **direct sulfhydrylation** (γ-replacement/transferase), gene identified & sequenced | *P. aeruginosa* (MetZ ortholog, 82% id) | High; primary characterization of the orthologous system |
| 4 | Pairwise NW identities (computed, this study) | Computational / evolutionary | **Refutes** seed | Nearest characterized neighbor | 82.1% to *P. aeruginosa* MetZ (transferase) vs 36.5% to human CTH γ-lyase (the SF80 label source); 25.0% to MetC | Superfamily panel | High; global alignment, well-separated branches |
| 5 | [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/) | Review / biochemical survey | **Refutes** seed | Does *P. putida* use sulfhydrylation? Does it have γ-lyase? | Uses direct sulfhydrylation of O-succinylhomoserine; **no cystathionine γ-lyase** present in the species | *P. putida* | High; organism-level pathway evidence |
| 6 | Motif scan SATKF/K219 (computed, this study) | Structural / evolutionary | **Qualifies** (rules out pseudo-enzyme) | Is the active site intact? | Catalytic PLP Schiff-base Lys K219 present, correctly spaced; matches UniProt feature | Superfamily panel | High that enzyme is active; motif is family-wide, does not discriminate subtype |

**Literature detail:**

- **[PMID: 7704274](https://pubmed.ncbi.nlm.nih.gov/7704274/)** — *A direct sulfhydrylation pathway is used for methionine biosynthesis in Pseudomonas aeruginosa.* Identified and sequenced the *metZ* gene and established that methionine's second biosynthetic step proceeds by **direct sulfhydrylation**, i.e. transferase chemistry. This is the foundational primary evidence that metZ-type enzymes are sulfhydrylases, not lyases. **Supports** the transferase assignment; **refutes** the carbon-sulfur lyase graft.
- **[PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/)** — *Pathways of assimilative sulfur metabolism in Pseudomonas putida.* Shows *P. putida* uses direct sulfhydrylation of O-succinylhomoserine and, critically, that **no cystathionine γ-lyase** is present in the species. Because the GO:0016846 graft rode on a "cystathionine γ-lyase" subfamily label, this paper removes any organismal basis for the term. **Refutes** the graft at the organism level.

---

## Active-Site / Placement Analysis

**Subfamily placement (percent identity to characterized members):**

```
Query Q88LD4 (P. putida metZ) vs:
  P. aeruginosa MetZ (P55218)  O-succ-HSer sulfhydrylase  EC 2.5.1.-   82.1%  [transferase]  <-- nearest characterized
  E. coli MetB   (P00935)      cystathionine gamma-synth  EC 2.5.1.48  38.0%  [transferase]
  Human  CTH     (P32929)      cystathionine gamma-lyase  EC 4.4.1.1   36.5%  [C-S LYASE = SF80 graft label]
  E. coli MetC   (P06721)      cystathionine beta-lyase   EC 4.4.1.8   25.0%  [C-S lyase]
```

**Conclusion:** The query is ~44–46 percentage points closer to the transferase than to either carbon-sulfur lyase. Placement is in the **transferase (sulfhydrylase/synthase) branch**, not the lyase branch from which GO:0016846 was propagated.

**Active-site conservation (PLP Schiff-base lysine):**

```
Motif [S/A]-A-T-K-[F/Y]:
  Q88LD4 (query)      SATKF   K219   (matches UniProt N6-(PLP)-Lys feature)  -> INTACT
  P. aeruginosa MetZ  SATKY   K219                                           -> INTACT
  E. coli MetB        C-TKY   ~K198                                          -> present
  Human CTH           SATKY   ~K212                                          -> present
  E. coli MetC        -ATKY   ~K210                                          -> present
```

**Catalytic residues: INTACT.** The protein is an active enzyme. The active-site test rules out the pseudo-enzyme failure mode but, because the PLP lysine is conserved across both transferase and lyase branches, it does not by itself distinguish the two; subfamily placement and reaction-direction evidence make that call.

*Provenance note:* The percent-identity values are from Needleman–Wunsch global pairwise alignments of the UniProt sequences listed, and the motif positions are from a signature scan of the same panel; both were executed during the investigation (iterations 1–2) and are reproduced here as the quantitative basis for the placement call.

---

## GO Curation Implications

**Recommended action (lead requiring curator verification):**

1. **REMOVE / REPLACE GO:0016846 (carbon-sulfur lyase activity).** The IEA term from GO_REF:0000118 (TreeGrafter/PANTHER) is a within-superfamily mis-graft onto the cystathionine γ-lyase subfamily and describes the wrong reaction class (lyase) and wrong chemical direction for this protein.

2. **RETAIN / promote the transferase-branch annotation GO:0016765** (transferase activity, transferring alkyl or aryl (other than methyl) groups), already present via UniRule UR000282477. If a more specific child term for O-succinylhomoserine sulfhydrylase exists or is created, prefer it; otherwise GO:0016765 is the correct branch-level term.

3. **Retain the mechanistic/pathway context**: PLP binding at K219 and the L-methionine biosynthesis (L-homocysteine from O-succinylhomoserine) pathway are well supported and should stay.

This is a **replace-with-correct-branch / remove-mis-grafted-term** case — explicitly *not* a "generalize" case (the problem is wrong branch, not wrong granularity) and *not* "treat-as-non-core." Per instructions, "protein binding" is not recommended; the enzyme has a well-defined catalytic transferase function.

---

## Limitations and Knowledge Gaps

- The percent-identity and motif analyses are sequence/alignment-based (computational). They agree strongly with the reviewed UniProt-HAMAP (MF_02056) assignment, but they are **not a fresh enzyme assay** on Q88LD4 itself.
- Direct kinetic characterization in the literature is for the *P. aeruginosa* ortholog (82% identity), not the *P. putida* protein specifically. Cross-organism inference at 82% identity with conserved active site is well supported but formally indirect for Q88LD4.
- **Residual/promiscuous lyase side-activity** is not quantified for metZ. Many PLP transsulfuration enzymes show low-level side reactions; even if present at trace levels for metZ, this would not justify a primary GO:0016846 MF annotation, but it remains an untested detail.
- The analysis relied on a focused panel of four characterized reference enzymes spanning both branches; a full phylogenetic re-grafting with a broader sampling was not performed, though the identity gap (82% vs ≤37%) is large enough that the conclusion is robust.

---

## Conflicts, Alternatives, and Discriminating Tests

**Conflicts / alternatives considered:**

- **Paralog confusion (the central issue):** The graft confused the transferase subfamily (MetZ sulfhydrylases) with the lyase subfamily (cystathionine γ-lyase, PTHR11808:SF80). Resolved — the query is 82% identical to a characterized MetZ and the host organism lacks γ-lyase entirely ([PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/)).
- **Database carry-over:** Q88LD4 simultaneously carries GO:0016765 (correct) and GO:0016846 (mis-grafted). A curator should ensure the correction does not inadvertently remove the correct transferase term.
- **Residual lyase activity:** No evidence quantifies any C–S lyase side activity for metZ; a knowledge gap rather than a conflict.

**Most efficient discriminating tests:**

1. **In vitro assay of recombinant Q88LD4**: measure O-succinylhomoserine + H₂S → homocysteine + succinate (sulfhydrylase/transferase) and, as a negative control, assay for cystathionine γ-lyase activity. Expected: robust sulfhydrylase activity, no/negligible γ-lyase.
2. **K219A active-site mutant**: loss of PLP binding and activity would confirm K219 as the catalytic Schiff-base lysine.
3. **Genetic complementation**: a *P. putida metZ* knockout should be methionine-auxotrophic and rescued by the wild-type gene (and by *P. aeruginosa* metZ), confirming the biosynthetic transferase role — not a catabolic lyase role.

---

## Summary

The TreeGrafter/PANTHER hypothesis that *P. putida* KT2440 **metZ (Q88LD4)** has **carbon-sulfur lyase activity (GO:0016846)** is **refuted**. The graft is a textbook **within-superfamily mis-placement (Failure Mode 3)**: the query was propagated a term from the cystathionine γ-lyase subfamily (PANTHER PTHR11808:SF80) of the shared Cys/Met PLP-dependent transsulfuration fold, even though metZ belongs to the **transferase** branch of that superfamily. metZ is an **O-succinylhomoserine sulfhydrylase** (EC 2.5.1.-) that catalyzes **direct sulfhydrylation** — the net *addition* of H₂S to O-succinylhomoserine to make L-homocysteine for methionine biosynthesis — which is the chemical *opposite* of the "elimination of hydrogen sulfide" that defines GO:0016846.

Three independent lines of evidence converge. First, reaction chemistry and the reviewed UniProt-HAMAP rule (MF_02056) place metZ in the transferase class (GO:0016765 is already annotated). Second, the nearest *characterized* homolog is *P. aeruginosa* MetZ sulfhydrylase at **82.1% identity**, whereas the carbon-sulfur lyases are ≤37% identical — and *P. putida* has **no cystathionine γ-lyase at all**, so the grafted label names an activity absent from the organism. Third, the active site is intact (catalytic PLP Schiff-base lysine **K219** in the **SATKF** motif), which rules out the pseudo-enzyme failure mode and confirms metZ is a fully active enzyme — just of the wrong (transferase, not lyase) type.

**Curation lead:** Remove/replace the mis-grafted **GO:0016846** and retain the branch-correct transferase annotation **GO:0016765** (ideally refined to O-succinylhomoserine sulfhydrylase), preserving the PLP-K219 and methionine-biosynthesis context. The decisive single datum: metZ is 82% identical to a characterized O-succinylhomoserine sulfhydrylase transferase and only ~36% identical to the γ-lyase whose label produced the graft.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist metZ subfamily placement](openscientist_artifacts/provenance_metZ_subfamily_placement.md)