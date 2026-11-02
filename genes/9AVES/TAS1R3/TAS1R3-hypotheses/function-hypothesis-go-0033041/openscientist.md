---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:37:36.607946'
end_time: '2026-10-15T01:50:28.524661'
duration_seconds: 771.92
template_file: templates/treegrafter_function_hypothesis.md
template_variables:
  organism: 9AVES
  gene: TAS1R3
  gene_symbol: TAS1R3
  uniprot_accession: A0A7L3N407
  taxon_id: NCBITaxon:689266
  taxon_label: Oreotrochilus melanogaster
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0033041
  hypothesis_text: TAS1R3 has sweet taste receptor activity (GO:0033041).
  term_context: '- Term: sweet taste receptor activity (GO:0033041)

    - Evidence type: IEA

    - Original reference: GO_REF:0000118'
  reference_context: '- GO_REF:0000118

    - PMID:25146290'
  source_file: genes/9AVES/TAS1R3/TAS1R3-ai-review.yaml
  source_selector: existing_annotations[6].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0033041\n  label: sweet taste receptor activity\n\
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

- **Organism code:** 9AVES
- **Taxon:** Oreotrochilus melanogaster (NCBITaxon:689266)
- **Gene directory:** TAS1R3
- **Gene symbol:** TAS1R3
- **UniProt accession:** A0A7L3N407

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0033041
- **Source file:** genes/9AVES/TAS1R3/TAS1R3-ai-review.yaml
- **Source selector:** existing_annotations[6].function_hypothesis

## Seed Hypothesis (propagated by TreeGrafter/PANTHER)

TAS1R3 has sweet taste receptor activity (GO:0033041).

## Term and Decision Context

- Term: sweet taste receptor activity (GO:0033041)
- Evidence type: IEA
- Original reference: GO_REF:0000118

## Reference Context

- GO_REF:0000118
- PMID:25146290

## Source Context YAML

```yaml
term:
  id: GO:0033041
  label: sweet taste receptor activity
evidence_type: IEA
original_reference_id: GO_REF:0000118
```

## Research Objective

Decide whether **TAS1R3 directly has the stated function**. Automated
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

**Target:** TAS1R3 (UniProt **A0A7L3N407**), *Oreotrochilus melanogaster* (Andean hillstar, a hummingbird; NCBITaxon:689266, organism code 9AVES)
**Seed hypothesis under test:** TAS1R3 has **sweet taste receptor activity (GO:0033041)** — propagated by TreeGrafter/PANTHER, evidence type IEA, original reference GO_REF:0000118.

---

## Summary

The TreeGrafter/PANTHER graft that placed A0A7L3N407 into subfamily **PTHR24061:SF435 (Taste receptor type 1 member 3, TAS1R3)** is **correct at the subfamily level**. The protein is a genuine, intact class C (family 3) G-protein-coupled receptor with the canonical taste-receptor architecture: an extracellular Venus flytrap domain, a 9-cysteine linker, and a seven-transmembrane bundle. It is **95.1% identical** to the functionally characterized *Calypte anna* T1R3. Thus the sequence was **not** mis-placed within its superfamily (failure mode #3 excluded), and it is **not** a pseudo-enzyme — indeed it is not an enzyme at all, so there is no catalytic active site to degrade (failure mode #2 is categorically inapplicable).

The error the pipeline makes is one of **granularity and biological context — failure mode #1**. "Sweet taste receptor activity" is an **emergent property of the T1R2+T1R3 heterodimer**, not an intrinsic, autonomous molecular function of the TAS1R3 subunit. TAS1R3 is the **obligate shared co-receptor** of the T1R family: it partners with T1R2 to make a sweet receptor, or with T1R1 to make an umami/amino-acid receptor, and its ligand specificity is set by the *partner* subunit. The principal sweetener-binding pocket lies in T1R2, not T1R3. The pipeline's own output betrays this: the *same* run annotated this single protein with **both** GO:0033041 (sweet) and GO:0050917 (umami perception) — the classic signature of annotating a shared co-receptor with the function of every complex it joins.

In this organism the over-generalization is compounded into a near-impossibility. A UniProt proteome query shows the hummingbird possesses **TAS1R1 and TAS1R3 but no TAS1R2** (zero TAS1R2 across all of Trochilidae), so the canonical sweet receptor **cannot physically assemble**. Hummingbirds nevertheless strongly prefer sugar because the ancestral **T1R1–T1R3 umami receptor was evolutionarily repurposed into a carbohydrate sensor** (Baldwin et al. 2014, the paper underlying the GO_REF context). The physiological percept ("sweet") is preserved, but the molecular machine responsible is different from the one GO:0033041 defines. The recommended curation lead is therefore **generalize / retain-with-qualification** — generalize to taste receptor activity (GO:0008527), keep the parallel umami term, and flag the mammalian→bird organism-specific carryover for curator verification.

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED / TOO GENERAL (qualified).**

**Failure mode: #1 — Granularity / family-vs-subfamily, specifically a *shared co-receptor subunit* mislabeled with the emergent function of the complex it participates in — compounded by an organism-specific caveat.**

- **Not failure mode #2 (pseudo-enzyme):** TAS1R3 is a GPCR, not an enzyme; there are no catalytic/metal-binding residues to lose. The fold is intact.
- **Not failure mode #3 (within-superfamily mis-placement):** the graft onto PANTHER SF435 (TAS1R3) is correct; 95% identity to the characterized *Calypte anna* T1R3 confirms it.

**Single most decisive piece of evidence:** a UniProt proteome query for *Oreotrochilus melanogaster* (taxon 689266) returns **TAS1R1 (A0A7L3NBT4) and TAS1R3 (A0A7L3N407) but NO TAS1R2**, and a family-wide query across Trochilidae (taxon 9242) returns **zero TAS1R2 entries**. The sweet-specific partner subunit required to build the canonical GO:0033041 sweet receptor (T1R2+T1R3) is physically absent from this animal, so the only assemblable T1R complex is **T1R1+T1R3**, the repurposed umami→carbohydrate receptor ([PMID: 25146290](https://pubmed.ncbi.nlm.nih.gov/25146290/)). Reinforcing this, the same TreeGrafter run annotated the single TAS1R3 protein with **both** GO:0033041 (sweet) and GO:0050917 (umami) — direct internal evidence that TAS1R3 is a promiscuous co-receptor, not a sweet-specific receptor.

---

## Independent Family / Function Assignment

From our own analysis (domain architecture + orthology + pairwise alignment), independent of the propagated term:

- **Identity:** Class C (family 3) GPCR, **Taste receptor type 1 member 3 (TAS1R3 / T1R3)** — the obligate **shared co-receptor** subunit of the T1R family. Architecture confirmed: extracellular **Venus flytrap domain** (ANF_receptor, PF01094, ~471 aa), **9-cysteine linker** (NCD3G, PF07562; 10 Cys in the 481–560 linker), and **7-transmembrane** bundle (7tm_3, PF00003).
- **Nearest characterized homolog:** *Calypte anna* (Anna's hummingbird) **T1R3** (UniProt A0A088DCH0), **95.1% identical** — the exact species in which Baldwin et al. experimentally showed T1R1/T1R3 functions as a sugar receptor. The specific function it carries: co-receptor subunit of the hummingbird **T1R1–T1R3 carbohydrate (umami-derived) receptor**.
- **Function I would assign:** TAS1R3 is a **taste receptor co-receptor subunit** that, within a heterodimer, participates in sweet and/or umami transduction. The most defensible intrinsic molecular-function term is **GO:0008527 (taste receptor activity)** (with GO:0004930 G-protein-coupled receptor activity already applicable). GO:0033041 is acceptable **only** as a complex-subunit annotation, and in this species is additionally unrealizable.

| Granularity axis | Seed term GO:0033041 | Independent assignment |
|---|---|---|
| vs. intrinsic subunit MF | Too specific / partner-dependent complex term | **More general → GO:0008527** |
| vs. actually-assemblable complex | Names only sweet, omits the realizable umami role | Keep **GO:0050917** in parallel |
| Organism realizability | Unrealizable (no T1R2 in hummingbirds) | Realizable (T1R1+T1R3 present) |

**Granularity relative to seed:** the seed is a **sibling/partner-dependent complex term**; the honest independent assignment is the **more general** taste receptor activity (GO:0008527), retaining the parallel umami term.

---

## Key Findings

### Finding 1 — TAS1R3 is a genuine class C GPCR co-receptor subunit, not a sweet-specific receptor

A0A7L3N407 is an 832-amino-acid protein correctly grafted to PANTHER subfamily **PTHR24061:SF435 "Taste receptor type 1 member 3."** Its domain architecture is the canonical T1R class C GPCR architecture: the extracellular **ANF_receptor / Venus flytrap domain (PF01094)** that binds ligand and mediates dimerization; the **9-cysteine NCD3G linker (PF07562)**, with 10 cysteines observed in the 481–560 region; and the **7tm_3 (PF00003)** seven-transmembrane class C bundle. This is a textbook, intact T1R receptor — there is **no enzymatic active site to degenerate**, which categorically rules out the pseudo-enzyme failure mode.

Critically, the literature defines sweet taste receptor activity as a property of the **T1R2+T1R3 heterodimer** ([PMID: 31553164](https://pubmed.ncbi.nlm.nih.gov/31553164/): "Sweet taste receptor, a heterodimer belonging to the class C G-protein coupled receptor (GPCR) family and composed of the T1R2 and T1R3 subunits"), and molecular-dynamics work localizes the principal sweetener-binding Venus flytrap pocket to **T1R2**, "rather than T1R3 region" ([PMID: 31308429](https://pubmed.ncbi.nlm.nih.gov/31308429/)). TAS1R3 therefore contributes dimerization and G-protein coupling, not sweet-ligand specificity — it is the **shared obligate co-receptor** whose downstream specificity is set by its partner. The fact that the same TreeGrafter run propagated **both** the sweet (GO:0033041) and umami (GO:0050917) terms to this one protein is itself diagnostic: a single molecule cannot be both "the sweet receptor" and "the umami receptor"; both are complex-level functions of two different heterodimers that share T1R3.

### Finding 2 — In hummingbirds the canonical sweet receptor is absent; sugar is sensed by a repurposed T1R1–T1R3 receptor

Baldwin et al. 2014 (*Science*) — **the very paper (PMID:25146290) cited in the GO_REF:0000118 decision context** — report "the widespread absence in birds of an essential subunit (T1R2) of the only known vertebrate sweet receptor," and demonstrate by receptor-expression and behavioral assays that "the ancestral umami receptor (the T1R1-T1R3 heterodimer) was repurposed in hummingbirds to function as a carbohydrate receptor." *Oreotrochilus melanogaster* is a hummingbird (family Trochilidae). The mechanistic basis for sweet/sugar perception in this lineage is therefore **structurally distinct** from the mammalian T1R2+T1R3 sweet receptor around which GO:0033041 is defined. Annotating this bird's T1R3 with "sweet taste receptor activity" imports a mammalian complex that cannot assemble here.

### Finding 3 — Proteome query empirically confirms TAS1R2 is absent while TAS1R1 + TAS1R3 are present

A UniProt proteome query for taxon **689266** (*Oreotrochilus melanogaster*) returns **TAS1R3 (A0A7L3N407, 832 aa)** and **TAS1R1 (A0A7L3NBT4, 572 aa)** — but **no TAS1R2**. Broadening to the whole hummingbird family (Trochilidae, taxon 9242) returns **zero TAS1R2 entries**, while TAS1R1 (e.g., *Calypte anna* A0A088DBT6) and TAS1R3 (*Calypte anna* A0A088DCH0) are present. This is a direct, organism-specific empirical reproduction of the bird-wide T1R2 loss reported by Baldwin et al. The only assemblable T1R heterodimer in this hummingbird is **T1R1/T1R3** — the umami-derived carbohydrate receptor — so the canonical sweet receptor simply cannot form.

### Finding 4 — The query T1R3 is 95% identical to the functionally characterized *Calypte anna* T1R3

A global Needleman–Wunsch alignment (executed in this work, numpy implementation) established orthology and correct placement:

| Comparison | Identities | % identity | Interpretation |
|---|---|---|---|
| Oreotrochilus T1R3 (A0A7L3N407, 832 aa) vs **Calypte anna T1R3** (A0A088DCH0, 836 aa) | 795 / 836 | **95.1%** | Essentially the same hummingbird-clade co-receptor |
| Oreotrochilus T1R3 vs **human TAS1R3** (Q7RTX0, 852 aa) | 359 | **41.9%** | Expected mammal–bird orthologous divergence |

The ~95% identity to *Calypte anna* T1R3 — the species where T1R1/T1R3 was shown to drive sugar-taste behavior "in captive and wild hummingbirds" ([PMID: 25146290](https://pubmed.ncbi.nlm.nih.gov/25146290/)) — establishes that the query is the *same* functionally validated co-receptor, not a diverged paralog, and excludes a degenerate/pseudogene fold. The ~42% identity to human T1R3 is consistent with a genuine, well-conserved ortholog across the bird–mammal split, confirming the PANTHER graft onto SF435 is correct.

---

## Mechanistic Model / Interpretation

The T1R taste-receptor system is a **combinatorial heterodimer system built on one shared subunit**:

```
          MAMMALS (e.g., human)                    HUMMINGBIRDS (Oreotrochilus)
          ---------------------                    ----------------------------

   T1R2 ──┐                                         T1R2  ✗ (GENE LOST across all birds)
          ├──► SWEET receptor  (GO:0033041)
   T1R3 ──┘  (sweetener pocket in T1R2 VFD)

   T1R1 ──┐                                         T1R1 ──┐
          ├──► UMAMI receptor  (GO:0050917)                ├──► repurposed CARBOHYDRATE /
   T1R3 ──┘                                         T1R3 ──┘    "sweet-sensing" receptor
                                                              (Baldwin et al. 2014)

   T1R3 = shared obligate CO-RECEPTOR — specificity is set by its PARTNER, not by T1R3 itself
```

The pipeline correctly identified the subunit (TAS1R3 → PANTHER SF435) but then propagated the **complex-level function** down to the subunit. Because T1R3 is shared between two complexes, the pipeline emitted **both** sweet and umami terms for the same protein — a logical signature of co-receptor annotation inflation.

Layered on top is an **organism-specific** problem that makes the sweet term not just over-general but **physically unrealizable**: this hummingbird (and all surveyed birds) **lacks the T1R2 gene entirely**. Without T1R2, no T1R2+T1R3 dimer can form, so there is no molecular machine in this animal with "sweet taste receptor activity" as GO defines it. Yet hummingbirds obviously detect and prefer sugar — because evolution **re-tuned the ligand-binding pocket of the T1R1–T1R3 umami dimer** to respond to carbohydrates. The physiological outcome ("sweet perception") is preserved; the **molecular identity of the responsible receptor is different** from the GO:0033041 definition.

The correct reading of A0A7L3N407's molecular function is therefore: (1) it **is** a bona fide T1R3 co-receptor subunit (graft correct → not mode #3); (2) it is an intact GPCR, not a degraded enzyme (→ not mode #2); (3) the propagated term is the **emergent function of a heterodimer**, too specific/mis-contextualized for the isolated subunit, and in this species additionally **unassemblable** (→ failure mode #1).

---

## Active-Site / Placement Analysis

**There is no catalytic active site to test** — TAS1R3 is a class C GPCR, not an enzyme — so the catalytic-residue arm of the stress test is **not applicable**, and the pseudo-enzyme failure mode (#2) is categorically ruled out. The analytically meaningful equivalents are **(a) structural integrity of the receptor machinery**, **(b) subfamily placement**, and **(c) functional-partner availability**, all computed below.

**(a) Receptor architecture integrity (UniProt/Pfam features):**

| Module | Expected (class C GPCR / T1R3) | Observed in A0A7L3N407 | Intact? |
|---|---|---|---|
| Venus flytrap (ANF_receptor, PF01094) | ~450–480 aa bilobed ligand/dimer domain | ~471 aa present | Yes |
| 9-cysteine / cysteine-rich linker (NCD3G, PF07562) | ≥9 conserved Cys linking VFT→7TM | 10 Cys in 481–560 | Yes |
| 7TM bundle (7tm_3, PF00003) | 7 TM helices + G-protein coupling | 5 TM helices annotated (prediction) | Largely; prediction incomplete, not degenerate |
| Subfamily placement | PANTHER PTHR24061:SF435 | Exact match (TAS1R3) | Yes — graft correct |

**(b) Subfamily / orthology placement (provenance: global Needleman–Wunsch alignment, numpy, executed this work):**

| Pair | Identities | % identity | Interpretation |
|---|---|---|---|
| Oreotrochilus T1R3 (A0A7L3N407) vs **Calypte anna T1R3 (A0A088DCH0)** | 795/836 | **95.1%** | Same hummingbird-clade co-receptor Baldwin 2014 characterized → functional context transfers with high confidence |
| Oreotrochilus T1R3 vs **human TAS1R3 (Q7RTX0)** | 359 | **41.9%** | Expected mammal–bird divergence of a genuine T1R3 ortholog |

**(c) Functional-partner availability (provenance: UniProt proteome query, taxa 689266 and 9242):**

| Subunit | Present in *O. melanogaster*? | Present in Trochilidae? | Consequence |
|---|---|---|---|
| TAS1R1 | **Yes** (A0A7L3NBT4, 572 aa) | Yes (*Calypte anna* A0A088DBT6) | T1R1–T1R3 (umami/carbohydrate) dimer **can** form |
| TAS1R3 | **Yes** (A0A7L3N407, 832 aa) | Yes (*Calypte anna* A0A088DCH0) | Shared co-receptor present |
| TAS1R2 | **No** | **No (0 entries)** | T1R2–T1R3 (sweet) dimer **CANNOT** form |

**Explicit statement:** Catalytic residues — **not applicable (no enzyme).** Receptor fold and co-receptor subunit — **intact and correctly placed.** The decisive deficiency is **absence of the T1R2 partner**, which makes the GO:0033041 complex unassemblable in this organism.

---

## Evidence Base (Evidence Matrix)

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limits |
|---|---|---|---|---|---|---|---|
| 1 | UniProt A0A7L3N407 + InterPro/PANTHER | Database / computational | Qualifies | Is the graft a true TAS1R3? | PANTHER SF435 = TAS1R3; VFT+9Cys+7TM class C GPCR | *O. melanogaster*, predicted protein | High for identity; sequence flagged as fragment-like with 1 ambiguous residue |
| 2 | TreeGrafter annotations (same run) | Database | Refutes "sweet-specific" | Is TAS1R3 sweet-specific? | Same protein carries GO:0033041 **and** GO:0050917 (umami) | — | High; internal evidence it is a shared co-receptor |
| 3 | [PMID: 31553164](https://pubmed.ncbi.nlm.nih.gov/31553164/) | Structural / review | Qualifies | What has sweet activity? | Sweet receptor = **T1R2+T1R3 heterodimer** (class C GPCR) | Human, modeling/MD | High; activity is complex-level |
| 4 | [PMID: 31308429](https://pubmed.ncbi.nlm.nih.gov/31308429/) | Structural / computational (MD) | Qualifies | Does T1R3 bind sweeteners? | Preferential sweetener site is **T1R2 VFD, not T1R3** | Human T1R2–T1R3, MD | High; T1R3 = co-receptor; model-based |
| 5 | [PMID: 25146290](https://pubmed.ncbi.nlm.nih.gov/25146290/) | Direct assay + behavior + evolutionary | Refutes/Competing | Does the canonical sweet receptor exist in hummingbirds? | **T1R2 lost in birds**; **T1R1–T1R3 repurposed** to sense carbohydrates; guides feeding behavior | Hummingbirds incl. *Calypte anna* | High; decisive for organism-specific mechanism |
| 6 | UniProt proteome query (this work) | Computational / database | Refutes assemblability | Is TAS1R2 present in *O. melanogaster*? | **TAS1R2 absent**; TAS1R1 + TAS1R3 present; **0 TAS1R2** across Trochilidae | Taxon 689266 / 9242 | High; absence-in-DB caveat (see Limitations) |
| 7 | Pairwise alignment (this work) | Computational / evolutionary | Supports/Qualifies | Is the query a functional hummingbird T1R3? | **95.1% identical to characterized *Calypte anna* T1R3**; 41.9% to human | NW global alignment | High; orthology transfer from a Baldwin-characterized receptor |

**How the literature supports or challenges the findings:** [PMID: 31553164](https://pubmed.ncbi.nlm.nih.gov/31553164/) and [PMID: 31308429](https://pubmed.ncbi.nlm.nih.gov/31308429/) jointly establish that sweet activity is a heterodimer property with the ligand pocket in T1R2 — challenging the notion that the isolated TAS1R3 subunit "has" sweet activity. [PMID: 25146290](https://pubmed.ncbi.nlm.nih.gov/25146290/) (the GO_REF-context paper) supplies the decisive organism-specific mechanism: T1R2 is lost in birds and sugar is sensed via a repurposed T1R1–T1R3 receptor. Our own computational work (proteome query + alignment) reproduces the T1R2 loss in this exact species and confirms the query is the same co-receptor those studies characterized.

---

## Limitations and Knowledge Gaps

- **Proteome completeness / absence-of-evidence.** The TAS1R2-absence conclusion rests on current UniProt proteome content. It is strongly corroborated by Baldwin et al.'s bird-wide survey, but a database absence is formally weaker than a verified syntenic pseudogene at the TAS1R2 locus in the *O. melanogaster* assembly.
- **Sequence quality.** The UniProt entry shows fragment-like/ambiguous features (one ambiguous residue), so the predicted TM-helix count (5 of the expected 7) reflects incomplete prediction, not evidence of structural degeneration.
- **No direct functional assay on this exact species.** Functional inference for A0A7L3N407 is by 95% homology to *Calypte anna*, not by assay of the *Oreotrochilus* protein itself. Baldwin et al. characterized other hummingbird species.
- **Tuning residues not individually mapped.** We did not localize the specific VFD substitutions in the hummingbird T1R1–T1R3 pocket that confer carbohydrate responsiveness; doing so would upgrade the umami/carbohydrate assignment from homology to mechanism.
- **GO modeling nuance.** Whether curation policy permits "contributes_to"/complex-subunit framing for co-receptors affects whether GO:0033041 can be retained-with-qualification versus replaced.

---

## Proposed Follow-up Experiments / Actions

1. **Syntenic genome check for the TAS1R2 locus** in the *O. melanogaster* assembly — confirm gene loss / pseudogenization directly. Decisive for the "canonical sweet receptor is impossible here" claim and upgrades the absence-in-DB caveat.
2. **Heterologous co-expression functional assay.** Express this TAS1R3 with conspecific T1R1 (and attempt T1R2+T1R3) in a calcium-reporter cell line; test sugars vs. amino acids to reproduce the Baldwin et al. assay in this species.
3. **Map the known hummingbird sweet-tuning residues** onto this T1R1/T1R3 sequence to confirm the carbohydrate-response machinery is present and identify the responsible substitutions.
4. **Curation action (lead requiring verification):** generalize GO:0033041 → **GO:0008527 (taste receptor activity)** as the intrinsic MF; retain the co-propagated **GO:0050917 (umami)** in parallel; if retaining GO:0033041 at all, mark it as a **complex-subunit / "contributes_to"** annotation and flag the mammalian→bird organism-specific carryover. Avoid "protein binding" as the fallback; the correct nuance is **co-receptor subunit of a heterodimeric taste receptor**.

---

## GO Curation Implications

**Lead action (requires curator verification): GENERALIZE / RETAIN-WITH-QUALIFICATION — do not treat as an autonomous sweet-receptor claim.**

1. **GO:0033041 (sweet taste receptor activity):** do **not** keep as an unqualified intrinsic MF of the isolated subunit — it is a heterodimer-emergent function and, in this hummingbird, is **unrealizable** because TAS1R2 is absent. At most, keep as a *complex-subunit* annotation with explicit qualification.
2. **Preferred robust annotation:** generalize to **GO:0008527 (taste receptor activity)** (with GO:0004930 G-protein-coupled receptor activity as applicable) — the correct granularity for a shared co-receptor whose specificity is partner-conferred.
3. **Companion term:** retain the co-propagated **GO:0050917 (umami perception)** in parallel; its presence is the key signal that TAS1R3 is a shared co-receptor, and in hummingbirds this is the ancestral route now tuned to carbohydrates.
4. **Avoid** "protein binding" as the final recommendation.

---

### Bottom line

The graft correctly identifies the protein as TAS1R3, but **GO:0033041 overstates the case**: TAS1R3 is a shared, partner-dependent **co-receptor**, and in this hummingbird the canonical sweet (T1R2/T1R3) receptor does not even exist — sweet/sugar is sensed through a repurposed T1R1/T1R3 umami receptor. Curate as **generalize / retain-with-qualification**, keeping the parallel umami annotation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)