---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T20:44:34.928228'
end_time: '2026-09-20T20:58:46.948257'
duration_seconds: 852.02
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: AKTIP
  gene_symbol: AKTIP
  uniprot_accession: Q9H8T0
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: noncatalytic-k63-ubiquitination-and-lesion-bypass
  hypothesis_text: Human AKTIP/FTS participates noncatalytically in K63-linked ubiquitination
    (GO:0070534) and DNA damage tolerance (GO:0006301). Adjudicate independently,
    distinguishing AKTIP from UBE2V1/UBE2V2 and other UEV-family members. Does its
    characterized TRF1/PCNA telomere-replication scaffold role perform a lesion-bypass
    step as defined by GO:0006301, or does it only suppress replication stress through
    another mechanism? Does any defined complex establish a contribution to K63-chain
    synthesis despite loss of intrinsic E2 catalytic activity? Loss of catalysis does
    not itself exclude complex participation, and replication-stress phenotypes do
    not by themselves establish lesion bypass.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/AKTIP/AKTIP-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human AKTIP/FTS participates noncatalytically\
    \ in K63-linked ubiquitination (GO:0070534) and\n  DNA damage tolerance (GO:0006301).\
    \ Adjudicate independently, distinguishing AKTIP from UBE2V1/UBE2V2\n  and other\
    \ UEV-family members. Does its characterized TRF1/PCNA telomere-replication scaffold\
    \ role perform\n  a lesion-bypass step as defined by GO:0006301, or does it only\
    \ suppress replication stress through another\n  mechanism? Does any defined complex\
    \ establish a contribution to K63-chain synthesis despite loss of\n  intrinsic\
    \ E2 catalytic activity? Loss of catalysis does not itself exclude complex participation,\
    \ and\n  replication-stress phenotypes do not by themselves establish lesion bypass.\n\
    focus_type: function_assignment\ncontext: []\nreference_id: []"
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
citation_count: 6
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

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** AKTIP
- **Gene symbol:** AKTIP
- **UniProt accession:** Q9H8T0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** noncatalytic-k63-ubiquitination-and-lesion-bypass
- **Source file:** genes/human/AKTIP/AKTIP-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human AKTIP/FTS participates noncatalytically in K63-linked ubiquitination (GO:0070534) and DNA damage tolerance (GO:0006301). Adjudicate independently, distinguishing AKTIP from UBE2V1/UBE2V2 and other UEV-family members. Does its characterized TRF1/PCNA telomere-replication scaffold role perform a lesion-bypass step as defined by GO:0006301, or does it only suppress replication stress through another mechanism? Does any defined complex establish a contribution to K63-chain synthesis despite loss of intrinsic E2 catalytic activity? Loss of catalysis does not itself exclude complex participation, and replication-stress phenotypes do not by themselves establish lesion bypass.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human AKTIP/FTS participates noncatalytically in K63-linked ubiquitination (GO:0070534) and
  DNA damage tolerance (GO:0006301). Adjudicate independently, distinguishing AKTIP from UBE2V1/UBE2V2
  and other UEV-family members. Does its characterized TRF1/PCNA telomere-replication scaffold role perform
  a lesion-bypass step as defined by GO:0006301, or does it only suppress replication stress through another
  mechanism? Does any defined complex establish a contribution to K63-chain synthesis despite loss of
  intrinsic E2 catalytic activity? Loss of catalysis does not itself exclude complex participation, and
  replication-stress phenotypes do not by themselves establish lesion bypass.
focus_type: function_assignment
context: []
reference_id: []
```

## Research Objective

Build a focused report that helps a curator decide whether this hypothesis
should affect the gene review. Address the focus type directly:

1. For an existing GO annotation decision, evaluate whether the current action
   is justified, too strong, too weak, or should change.
2. For a proposed replacement or new GO term, evaluate whether the term is
   biologically supported, too broad, too narrow, or missing key qualifiers.
3. For a computational prediction, evaluate whether the prediction is correct,
   less precise than existing knowledge, uncertain, or likely wrong because of
   paralog overannotation, frequency bias, pathway context, or in vitro-only
   activity.
4. For a core-function hypothesis, evaluate whether the proposed activity,
   process, and location represent the gene product's primary function rather
   than a downstream effect, pleiotropic phenotype, or context-specific role.
5. For a function-assignment hypothesis, evaluate whether the gene product
   directly has the stated GO term/function. Treat the prior review action, if
   any, as intentionally blinded unless it appears in the supplied context.

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews and database records as
orientation unless they contain directly relevant synthesized evidence that is
clearly labeled as review-level or database-level support.

Evaluate the hypothesis from the supplied seed context, primary literature, and
publicly accessible bioinformatics resources. Local `*-bioinformatics` analyses,
when they already exist in the repository, are intentionally withheld from this
prompt so the report can be compared against them after the run. Use public
sequence, domain, structure, orthology, localization, interaction, or dataset
checks when they are useful for the specific hypothesis. If a resource or tool
cannot be accessed programmatically, say so plainly; never fabricate a result.
Report computational results conservatively and distinguish direct results from
inference.

## Required Output

### Executive Judgment

Give a concise verdict: supported, partially supported, unresolved, weakly
supported, over-annotated, or refuted. Explain the reasoning and the most
important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (direct assay, mutant phenotype, localization, interaction,
  structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies / competing
- Claim tested
- Key finding
- Organism, tissue, cell type, or assay context
- Confidence and limitations

### GO Curation Implications

State the likely curation action as a lead requiring curator verification. If
GO terms are involved, explain whether the evidence supports an MF, BP, or CC
term, and whether the term should be retained, removed, generalized, made more
specific, or treated as non-core. Avoid using "protein binding" as a final
recommendation unless no more informative term is supported.

### Mechanistic Scope

Describe the immediate molecular or cellular function being tested. Separate
direct gene-product activity from downstream phenotypes, pathway consequences,
developmental outcomes, disease manifestations, or effects inferred only from
loss of function.

### Conflicts and Alternatives

Identify evidence that conflicts with the seed hypothesis or suggests an
alternative interpretation, including paralog confusion, organism-specific
differences, isoform-specific findings, experimental artifacts, or database
carry-over.

### Knowledge Gaps

List explicit uncertainties that matter for curation. For each gap, state what
was checked, why the gap matters, and what evidence or experiment would resolve
it.

### Discriminating Tests

Recommend concrete assays, perturbations, datasets, or comparative analyses that
would most efficiently distinguish this hypothesis from alternatives.

### Curation Leads

Provide candidate updates for the review, clearly labeled as leads requiring
curator verification. Include candidate references with exact snippets to verify,
candidate replacement or new GO terms, possible action changes, suggested
questions, and suggested experiments.

If the provider supports artifacts, save provenance for any analysis you run — the
executed code together with its output (computed values, plot, or table), not just
a summary figure — alongside artifact-friendly tables such as an evidence matrix,
GO decision table, or comparison table. Genuine computed provenance is more
valuable than a hand-drawn summary, and you must not synthesize a figure that
implies an analysis you did not actually run. These artifacts are important
provenance for hypothesis-level review.


## Output

# AIGR Gene Hypothesis Deep Research — AKTIP (Q9H8T0)

**Hypothesis slug:** `noncatalytic-k63-ubiquitination-and-lesion-bypass`
**Focus type:** function_assignment
**Target:** Human AKTIP/FTS (UniProt Q9H8T0), *Homo sapiens* (NCBITaxon:9606)
**GO terms adjudicated:** GO:0070534 (protein K63-linked ubiquitination), GO:0006301 (DNA damage tolerance / postreplication repair / "lesion bypass")

---

## Summary

The seed hypothesis proposes that human AKTIP/FTS participates *noncatalytically* in K63-linked ubiquitination (GO:0070534) and in DNA damage tolerance / lesion bypass (GO:0006301), and asks whether any defined complex establishes an AKTIP contribution to K63-chain synthesis despite loss of intrinsic E2 catalytic activity. After three iterations combining sequence and structural-family analysis, GO annotation-provenance checks, interaction-network mining, and primary-literature review, the answer is that **neither GO term is supported as a direct, core function of AKTIP**. Both are best explained as **paralog-driven, phylogenetically inferred (IBA) over-annotation** projected onto AKTIP from the genuinely K63/DDT-active UEV clade (UBE2V1/UEV1A and UBE2V2/MMS2), from which AKTIP is a divergent outgroup.

Four convergent lines of evidence drive this verdict. First, AKTIP is a **catalytically dead UEV (ubiquitin E2 variant)** — it adopts a UBC-like fold but lacks the E2 active-site cysteine required for any thioester/transfer chemistry (only two cysteines total in 292 aa, neither at the active-site position). Second, the current GO annotations for both hypothesis terms are **IBA-only (ECO:0000318)** — inferred from a family-wide phylogeny, not from any experiment on AKTIP — and there is an explicit **manual NOT annotation denying ubiquitin-like protein transferase activity (GO:0019787, NOT|enables)**. Third, no primary study and no curated interaction (IntAct, 200 interactions) places AKTIP in a complex with UBE2N/UBC13, UBE2V1, UBE2V2, RAD18, or PCNA-ubiquitination machinery; its actual partners are the FHF cargo-adaptor complex and replication-fork proteins (RPA1, POLA2, PCNA). Fourth, at subfamily resolution AKTIP falls **outside** the tight UBE2V1/UBE2V2 K63-DDT clade (those two are ~90% identical to each other; AKTIP is only ~41–45% identical to either), and CDD assigns it a dedicated domain model (cd23814).

The better-supported interpretation is that AKTIP is a **catalytically dead UEV acting as a telomere-replication scaffold** (binding TRF1/TRF2/telomeric DNA/PCNA/RPA70, suppressing replication stress) and, in the cytoplasm, a **cargo-adaptor scaffold in the FTS–Hook–FHIP (FHF) complex** — not a K63-chain builder or a lesion-bypass factor. The hypothesis is **refuted / over-annotated** for both proposed terms; the curator's most defensible action is to remove or down-qualify GO:0070534 and GO:0006301 as non-core, retain the NOT-transferase call, and anchor the review on the scaffold functions.

---

## Key Findings

### Finding 1 — AKTIP is a catalytically dead UEV; no direct evidence it synthesizes K63 chains

AKTIP/Ft1 is homologous to the **E2-variant ubiquitin-conjugating (UEV) enzymes**, as established by Burla et al. 2015 ([PMID: 26110528](https://pubmed.ncbi.nlm.nih.gov/26110528/)): *"AKTIP/Ft1 shares homology with the E2 variant ubiquitin-conjugating (UEV) enzymes."* By definition, UEV proteins adopt the UBC fold but lack the catalytic cysteine of true E2 enzymes and therefore cannot form the ubiquitin–thioester intermediate needed for conjugation or chain elongation.

An in-run pairwise alignment of AKTIP (292 aa) against UBE2N, UBE2V1, UBE2V2, and UBE2D1 gave ~41–45% aligned identity, confirming UEV-family membership, and critically showed that **the residue aligning to the UBE2N catalytic Cys87 is not a cysteine** in AKTIP. AKTIP contains only two cysteines in the entire sequence, neither at the E2 active site. This is a mechanistic-impossibility argument for *direct* catalysis: without the active-site Cys, AKTIP cannot itself catalyze ubiquitin transfer or K63-chain building.

The proteins that actually synthesize K63 chains for DNA damage tolerance are the UEVs **UBE2V1 (UEV1A) and UBE2V2 (MMS2)**, partnering with the catalytic E2 **UBE2N/UBC13**. These canonical UEVs are moreover functionally redundant for PCNA polyubiquitination: Zhang et al. 2008 ([PMID: 18284681](https://pubmed.ncbi.nlm.nih.gov/18284681/)) report that *"the additional knockdown of a UEV1A (MMS2 homolog) does not deplete PCNA polyubiquitination."* A dedicated literature search returned **no** study connecting AKTIP to UBE2N or to K63 polyubiquitin chain assembly.

### Finding 2 — AKTIP's DNA-related role is telomere/replication scaffolding and replication-stress suppression, not lesion bypass (GO:0006301)

Burla et al. 2015 ([PMID: 26110528](https://pubmed.ncbi.nlm.nih.gov/26110528/)) characterized AKTIP as a **shelterin-interacting telomeric factor**. It binds telomeric DNA, TRF1 and TRF2, and physically interacts with the replication factors **PCNA and RPA70**. RNAi depletion in human primary fibroblasts produces telomere dysfunction-induced foci (TIFs), defective PCNA recruitment, and intra-S checkpoint activation: *"AKTIP-depleted human primary fibroblasts showed that they are defective in PCNA recruiting and arrest in the S phase due to the activation of the intra S checkpoint."*

These are **replication-stress and telomere-replication phenotypes**, not evidence of a defined lesion-bypass event. GO:0006301 is mechanistically defined by translesion synthesis (TLS) or template-switch bypass of a specific replication-blocking lesion. Xu et al. 2014 ([PMID: 24674630](https://pubmed.ncbi.nlm.nih.gov/24674630/)) state that *"error-free PRR utilizes noncanonical K63-linked polyubiquitinated PCNA to signal lesion bypass through template switch, a process thought to be dependent on Mms2-Ubc13."* The classical DDT/lesion-bypass apparatus — RAD6–RAD18 (PCNA mono-ubiquitination) plus UBC13–MMS2–RAD5 (K63 poly-ubiquitination) — **does not include AKTIP** ([PMID: 18284681](https://pubmed.ncbi.nlm.nih.gov/18284681/); [PMID: 18757916](https://pubmed.ncbi.nlm.nih.gov/18757916/)). No reviewed paper demonstrates AKTIP mediating TLS or template-switch bypass of a defined lesion. Suppressing replication stress by stabilizing fork progression at telomeres is a distinct, upstream role.

### Finding 3 — Both hypothesis GO annotations are phylogenetic (IBA); a manual NOT annotation denies transferase activity

QuickGO records for Q9H8T0 (retrieved in-run) show that **GO:0070534 (protein K63-linked ubiquitination)** and **GO:0006301 (DNA repair / postreplication repair)** are both annotated `involved_in` with evidence code **ECO:0000318 (IBA — inferred from biological ancestor / phylogeny)**, not from any experiment on AKTIP. The molecular-function term **GO:0061631 (ubiquitin-conjugating enzyme activity)** is likewise IBA-only.

Decisively, **GO:0019787 (ubiquitin-like protein transferase activity) carries a `NOT|enables` qualifier** (ECO:0000303) — an explicit curator assertion that AKTIP *lacks* transferase activity. InterPro/CDD classifies the domain specifically as **cd23814, "ubiquitin E2 variant (UEV) domain of AKT-interacting protein and related proteins"** (UBC-like fold, IPR000608) — a dedicated subfamily rather than the canonical K63-active UEV group.

IntAct (200 interactions, in-run) reinforces this: among 53 distinct partners are the **FHF complex** (HOOK1/2/3, FHIP1A/1B/2A/2B, DCTN1) and replication factors **RPA1 and POLA2** — but **no UBE2N/UBC13, UBE2V1, UBE2V2, RAD18, or PCNA-ubiquitination machinery**. This is consistent with AKTIP being a replication-fork/telomere scaffold (its RPA70 partner appears as RPA1) and removes the empirical basis for the K63/UBE2N complex-participation route posited by the hypothesis.

### Finding 4 — AKTIP is a distinct UEV subfamily (outgroup), not part of the UBE2V1/UBE2V2 K63-DDT clade

A pairwise identity matrix computed in-run (global alignment; crude aligner, so absolute values are approximate) shows that the two K63/DDT UEVs **UBE2V1 (UEV1A) and UBE2V2 (MMS2) are ~90.3% identical to each other**, forming a tight functional clade, whereas AKTIP is only **~41.5% identical to UBE2V1 and ~44.8% to UBE2V2** — comparable to its ~41% identity to the catalytic E2 UBE2N and ~45% to the generic E2 UBE2D1. AKTIP is therefore roughly equidistant from the K63-active UEVs and from generic E2s, positioning it as an **outgroup** rather than a member of the DDT clade.

This is precisely why the IBA projection is over-broad: the GO:0070534 / GO:0006301 annotations derive from a **family-wide UBC phylogeny**, but at **subfamily resolution** AKTIP is not within the UBE2V1/UBE2V2 clade that actually performs K63-linked DNA-damage tolerance. CDD's dedicated cd23814 model formalizes this distinction.

---

## Mechanistic Model / Interpretation

The seed hypothesis conflates two things the data keep separate: (a) *being a UEV-fold protein at replication forks*, and (b) *building K63 chains for lesion bypass*. The canonical K63-DDT pathway and AKTIP's actual role can be laid out as follows.

```
 CANONICAL K63 / DNA-DAMAGE-TOLERANCE PATHWAY (does NOT include AKTIP)
 --------------------------------------------------------------------
   Replication-blocking lesion
            │
   RAD6–RAD18  ── monoUb ─────────►  PCNA-Ub (K164)  ──► TLS (Polη/Polζ)
            │
   UBC13(UBE2N) + MMS2(UBE2V2)/UEV1A(UBE2V1) + RAD5/HLTF/SHPRH
            │  builds K63-linked poly-Ub on PCNA
            ▼
   PCNA-K63-polyUb ──► error-free lesion bypass via TEMPLATE SWITCH   ← GO:0006301 / GO:0070534
                                                                          defined mechanistic step

 AKTIP / FTS ACTUAL ROLE (scaffold; replication-stress suppression)
 --------------------------------------------------------------------
   Telomere / replication fork
            │  binds TRF1, TRF2, telomeric DNA
   AKTIP ── binds ──► PCNA, RPA70/RPA1, POLA2   (recruitment / fork support)
            │
   Loss of AKTIP ──► TIFs, defective PCNA recruitment, intra-S checkpoint,
                     S-phase arrest  (REPLICATION STRESS — upstream of, and
                     distinct from, a defined lesion-bypass step)

   Separate, experimentally supported role:
   AKTIP = FTS core of FTS–Hook–FHIP (FHF) complex ─► dynein cargo/AP-4/ATG9A transport (GO:0070695)
```

Key interpretive points:

- **Catalysis is impossible; scaffolding is unsupported.** The absence of the active-site cysteine rules out direct catalysis. The hypothesis's fallback — noncatalytic scaffold participation in a K63-building complex — is legitimate in principle, but the specific empirical hook it requires (a physical/functional link to UBE2N–UBE2V machinery or PCNA-polyubiquitination) is absent from both literature and curated interactomes. So this route is *unsupported*, not merely untested.
- **Replication stress ≠ lesion bypass.** AKTIP depletion causes intra-S checkpoint activation and defective PCNA recruitment — consistent with a fork-support/recruitment scaffold, but GO:0006301 requires evidence of a bypass event (TLS or template switch) across a defined lesion, which no study provides for AKTIP.
- **The annotation is a phylogeny artifact.** IBA propagation from the UBC/UEV family projected the K63-DDT function onto an outgroup with a dedicated CDD model and a manual NOT-transferase call.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports/Refutes/Qualifies/Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [26110528](https://pubmed.ncbi.nlm.nih.gov/26110528/) (Burla 2015) | Interaction + localization + mutant phenotype | **Qualifies** (scaffold, not bypass) | AKTIP telomere/replication role | Binds telomeric DNA, TRF1, TRF2, PCNA, RPA70; depletion → TIFs, defective PCNA recruiting, intra-S arrest | Human primary fibroblasts | High for scaffold role; no lesion-specific bypass assay |
| [26110528](https://pubmed.ncbi.nlm.nih.gov/26110528/) | Structural/evolutionary | **Qualifies/Competing** | AKTIP is a UEV | "shares homology with the E2 variant ubiquitin-conjugating (UEV) enzymes" | Sequence homology | High; UEVs are catalytically inactive by definition |
| This run (Q9H8T0 alignment) | Computational | **Refutes** direct catalysis | AKTIP lacks E2 catalytic Cys | Residue aligning UBE2N Cys87 is non-Cys; only 2 Cys/292 aa, none at active site; ~41–45% id to UBE2N/UBE2V1/UBE2V2 | Pairwise alignment | Medium (crude aligner); consistent with UEV literature |
| [18284681](https://pubmed.ncbi.nlm.nih.gov/18284681/) (Zhang 2008) | Mutant/knockdown | **Competing** | Which UEVs drive K63/PCNA polyUb | UEV1A/MMS2 redundant for human PCNA polyubiquitination; AKTIP not implicated | Human cells | High; defines the real K63-DDT UEVs |
| [24674630](https://pubmed.ncbi.nlm.nih.gov/24674630/) (Xu 2014) | Genetic/mechanistic | **Competing** | Definition of error-free lesion bypass | K63-polyUb PCNA lesion bypass = Mms2-Ubc13 template switch | *S. cerevisiae* | High; mechanistic definition of GO:0006301 |
| [18757916](https://pubmed.ncbi.nlm.nih.gov/18757916/) (Pagès 2008) | Genetic/mutant | **Competing** | Lesion-bypass machinery | Rad6-Rad18 + Mms2-Ubc13-Rad5 mediate TLS/PRR | Yeast | High; AKTIP absent from pathway |
| [27234244](https://pubmed.ncbi.nlm.nih.gov/27234244/) (rice UBC13) | Direct assay | **Competing** | Conserved K63-DDT UEV partners | OsUbc13 binds Mms2/Uev1A, catalyzes K63 polyUb in vitro | Rice/yeast | High; reinforces UBE2V, not AKTIP |
| [32073997](https://pubmed.ncbi.nlm.nih.gov/32073997/) (Mattera 2020) | Interaction/complex | **Competing** (alt. core function) | AKTIP/FTS non-telomeric role | FTS is core of FTS-Hook-FHIP (FHF) complex; AP-4/ATG9A/dynein cargo adaptor | Human cells | High; distinct experimentally supported function |
| [24065519](https://pubmed.ncbi.nlm.nih.gov/24065519/) (Muthusami 2013) | Expression | Context | FTS/AKT-survival axis | FTS regulated by p53; supports AKT phosphorylation/survival | HeLa | Low relevance to Ub/DDT |
| QuickGO (this run) | Review/database | **Refutes/qualifies** | Evidence basis of GO:0070534 & GO:0006301 | Both IBA (ECO:0000318) only; GO:0019787 transferase = **NOT\|enables**; no experimental Ub/DDT annotation | Q9H8T0 GO record | High; DB-level, reflects lack of primary evidence |
| InterPro/CDD (this run) | Structural/evolutionary | **Qualifies** | AKTIP domain identity | CDD **cd23814** "UEV domain of AKTIP…"; UBC-like fold IPR000608 | Sequence | High; confirms non-catalytic UEV fold |
| IntAct (this run) | Interaction | **Refutes** K63 complex | Does AKTIP bind UBE2N/K63 machinery? | 53 partners incl. FHF, RPA1, POLA2; **no UBE2N/UBE2V1/UBE2V2/RAD18/PCNA-Ub machinery** | Curated + HT | Medium-high; absence-of-evidence, consistent across DBs |

---

## GO Curation Implications (leads — require curator verification)

- **GO:0070534 (protein K63-linked ubiquitination, BP):** **Remove or down-qualify (non-core).** IBA-only (ECO:0000318), no experimental backing, conflicts with the manual **NOT|enables GO:0019787** call. Homology to UBE2V1/UBE2V2 is insufficient; treat as paralog-driven.
- **GO:0061631 (ubiquitin-conjugating enzyme activity, MF):** **Remove/NOT.** IBA-only and inconsistent with the catalytically-dead UEV fold and the NOT-transferase annotation.
- **GO:0006301 (DNA damage tolerance / postreplication repair, BP):** **Remove as lesion-bypass — IBA-only.** Evidence supports a more general telomeric-replication role. Better-supported alternatives (curator to map exact IDs/evidence codes from PMID 26110528): **telomere maintenance / regulation of telomere maintenance / DNA replication** (IMP/IPI).
- **GO:0019787 (ubiquitin-like protein transferase activity, MF) — NOT|enables:** **Retain the NOT.** Consistent with all evidence.
- **Experimentally supported core functions to elevate:** **GO:0070695 (FHF complex)** and associated dynein/transport BP terms ([PMID: 32073997](https://pubmed.ncbi.nlm.nih.gov/32073997/)); **shelterin/chromosome telomeric region (CC)** and **TRF1 binding / PCNA binding / telomeric DNA binding (MF, IPI)** ([PMID: 26110528](https://pubmed.ncbi.nlm.nih.gov/26110528/)). Prefer these specific terms over a bare "protein binding".

### GO Decision Table

| GO term | Aspect | Current evidence (QuickGO) | This-run verdict | Recommended action |
|---|---|---|---|---|
| GO:0070534 protein K63-linked ubiquitination | BP | IBA (ECO:0000318) only | Paralog projection; not AKTIP-specific | **Remove / down-qualify (non-core)** |
| GO:0006301 DNA repair / postreplication repair | BP | IBA (ECO:0000318) only | Replication-stress phenotype, not lesion bypass | **Remove as lesion-bypass** |
| GO:0061631 ubiquitin-conjugating enzyme activity | MF | IBA (ECO:0000318) only | Contradicted by dead UEV fold + NOT-transferase | **Remove / NOT** |
| GO:0019787 ubiquitin-like transferase activity | MF | **NOT\|enables** (ECO:0000303) | Consistent with data | **Retain NOT** |
| GO:0070695 FHF complex | CC | IDA (ECO:0000314) | Experimentally supported core | **Retain** |
| Telomere maintenance / shelterin / telomeric region | BP/CC | PMID 26110528 (IPI/IMP) | Experimentally supported core | **Add/retain** (map exact IDs) |
| TRF1 binding / PCNA binding / telomeric DNA binding | MF | PMID 26110528 (IPI) | More informative than "protein binding" | **Add** as candidate MF |

**Paralog-distance provenance (this run):** Pairwise % identity (crude global aligner — absolute values approximate, contrast robust): **UBE2V1 vs UBE2V2 = 90.3%** (tight K63-DDT clade) vs **AKTIP = 41.5% / 44.8%** to those two — no closer than AKTIP's ~41% to catalytic UBE2N. AKTIP is an **outgroup UEV subfamily** (CDD cd23814), so the family-wide UBC IBA tree over-projects UBE2V1/UBE2V2-specific K63/DDT functions onto it.

---

## Mechanistic Scope

The immediate molecular function tested is whether AKTIP **directly enables or noncatalytically contributes to K63-linked ubiquitin chain assembly and to lesion bypass**. Direct, supported activities: (1) **protein/DNA scaffolding at telomeres** — binds telomeric dsDNA, shelterin (TRF1/TRF2), and replication factors PCNA/RPA70, facilitating PCNA loading/telomere replication; (2) **cargo-adaptor scaffolding** in the cytoplasmic FHF complex (dynein/AP-4/ATG9A trafficking). Downstream phenotypes (not the direct activity): S-phase/intra-S checkpoint arrest, telomere fragility/TIFs, senescence, altered AKT survival signaling. K63-chain synthesis and lesion bypass are **inferred from domain identity/phenotype**, never from a direct AKTIP activity.

---

## Conflicts and Alternatives

- **Paralog confusion (primary risk):** The K63/DDT UEV functions belong to **UBE2V1/UBE2V2 + UBE2N**, not AKTIP. AKTIP is a divergent UEV branch (~41–45% aligned identity) that has never been shown to bind UBE2N.
- **Alternative core function:** AKTIP/FTS is the scaffolding core of the **FHF complex** (dynein cargo adaptor) — a well-supported, mechanistically distinct role arguing against a primary Ub-enzyme identity.
- **Replication-stress ≠ lesion bypass:** The intra-S arrest/PCNA phenotype reflects impaired (telomere) replication and checkpoint signaling, which can arise without any postreplication-repair/lesion-bypass activity.
- **No contradicting positive evidence found:** No primary paper reported AKTIP–UBE2N interaction, AKTIP-dependent K63 chain formation, or AKTIP-dependent TLS/template switch. The absence is consistent across literature and IntAct.

---

## Limitations and Knowledge Gaps

1. **Approximate sequence identities.** The pairwise identity matrix used a crude in-run global aligner; absolute percentages are approximate. The qualitative outgroup conclusion is corroborated by the independent CDD subfamily assignment, but a formal phylogeny (MAFFT/MUSCLE + IQ-TREE) would harden it.
2. **Does AKTIP physically associate with UBE2N/UBC13 or K63 machinery?** Checked: PubMed and IntAct — none found. This is the crux of GO:0070534. Absence of interactome coverage cannot fully exclude a transient/condition-specific scaffold role. Resolve with co-IP / proximity-labeling and in-vitro K63 chain-assembly assays (AKTIP ± UBE2N vs UBE2V2 control).
3. **Is AKTIP required for PCNA K63-polyubiquitination or lesion-induced DDT?** Checked: no assays exist. Matters for GO:0006301. Resolve with PCNA-Ub Westerns after UV/MMS in AKTIP-KO cells and TLS/template-switch reporter assays.
4. **Isoform / PTM considerations.** Whether any AKTIP isoform gains a distinct ubiquitin-pathway role was not exhaustively assessed; current evidence gives no such indication.

---

## Discriminating Tests

- **UBE2N interaction + in-vitro K63 assay:** purified AKTIP + UBE2N + E1/Ub — does it build K63 chains? (UBE2V2+UBE2N as positive control). Distinguishes true UEV-partner function from fold-only homology.
- **AKTIP-KO PCNA-ubiquitination assay** after UV/MMS ± aphidicolin: tests GO:0006301 lesion bypass directly vs. replication-stress-only.
- **Domain-swap / active-site rescue:** does the AKTIP UEV domain complement *mms2Δ* in yeast DDT? A negative result cements paralog non-equivalence.
- **Proximity interactome (BioID/TurboID) of AKTIP** to score telomere/shelterin + FHF partners vs. DDT/UBE2N machinery, ideally under replication stress.
- **Rigorous UEV-family phylogeny** (MAFFT + IQ-TREE with bootstrap) to formally place AKTIP as an outgroup to UBE2V1/UBE2V2.

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

- **Candidate reference to cite:** [PMID: 26110528](https://pubmed.ncbi.nlm.nih.gov/26110528/) — verify snippets: *"AKTIP/Ft1 shares homology with the E2 variant ubiquitin-conjugating (UEV) enzymes"* and *"defective in PCNA recruiting and arrest in the S phase due to the activation of the intra S checkpoint."*
- **Candidate action changes:** (a) **Remove/reject or mark non-core** any GO:0070534 K63-ubiquitination annotation for AKTIP; (b) **Do not add** GO:0006301 as lesion bypass; (c) **Add/retain** telomere-maintenance (BP), telomeric-region/shelterin (CC), and TRF1/PCNA/DNA-binding (MF, IPI) terms from PMID 26110528; (d) retain FHF/dynein cargo-adaptor terms from [PMID: 32073997](https://pubmed.ncbi.nlm.nih.gov/32073997/); (e) retain the GO:0019787 NOT|enables call.
- **Suggested curator questions:** Are the K63/DDT annotations for AKTIP all IEA/IBA (paralog-derived)? If so they likely stem from UEV-domain projection from UBE2V1/UBE2V2 and should be down-weighted.
- **Suggested experiments:** the discriminating tests above (UBE2N binding + in-vitro K63 assay; AKTIP-KO PCNA-Ub after genotoxin).

---

## Evidence Base (Key Literature)

- *AKTIP/Ft1, a New Shelterin-Interacting Factor Required for Telomere Maintenance.* [PMID: 26110528](https://pubmed.ncbi.nlm.nih.gov/26110528/) — AKTIP as a UEV-homolog telomere/replication scaffold (TRF1/TRF2/PCNA/RPA70); source of the replication-stress phenotypes. **Primary support for the scaffold interpretation; refutes lesion-bypass.**
- *hMMS2 serves a redundant role in human PCNA polyubiquitination.* [PMID: 18284681](https://pubmed.ncbi.nlm.nih.gov/18284681/) — Identifies UEV1A/MMS2 as the redundant K63-PCNA UEVs. **Names the true actors; excludes AKTIP.**
- *The Rad5 helicase activity is dispensable for error-free DNA post-replication repair.* [PMID: 24674630](https://pubmed.ncbi.nlm.nih.gov/24674630/) — Defines K63-polyUb-PCNA template-switch bypass via Mms2-Ubc13. **Mechanistic definition of GO:0006301.**
- *Requirement of Rad5 for DNA polymerase zeta-dependent translesion synthesis.* [PMID: 18757916](https://pubmed.ncbi.nlm.nih.gov/18757916/) — Rad5 + Mms2-Ubc13 K63-PCNA polyubiquitination in DDT. **Confirms machinery without AKTIP.**
- *Rice UBC13 … required for K63-linked polyubiquitination and tolerance to DNA damage.* [PMID: 27234244](https://pubmed.ncbi.nlm.nih.gov/27234244/) — OsUbc13 partners Mms2/Uev1A, K63 catalysis in vitro. **UBE2V, not AKTIP, is the conserved K63 actor.**
- *The FTS-Hook-FHIP (FHF) complex interacts with AP-4 …* [PMID: 32073997](https://pubmed.ncbi.nlm.nih.gov/32073997/) — FTS/AKTIP as core FHF scaffold in trafficking. **Alternative experimentally grounded core function.**
- Database provenance (in-run): QuickGO Q9H8T0 (IBA annotations + NOT|enables GO:0019787), InterPro/CDD cd23814, IntAct (200 interactions).

---

## Conclusion

The hypothesis that human AKTIP/FTS directly participates in K63-linked ubiquitination (GO:0070534) and DNA damage tolerance / lesion bypass (GO:0006301) is **refuted as a direct function assignment and best classified as paralog-driven over-annotation**. AKTIP is a catalytically dead UEV outgroup with a manual NOT-transferase call, IBA-only support for both disputed terms, and no interaction or primary-literature link to K63-chain machinery. Its genuine, experimentally supported roles are as a **telomere/replication-fork scaffold** and a core subunit of the **FHF trafficking complex**. Both GO:0070534 and GO:0006301 should be removed or down-qualified as non-core, the NOT-transferase annotation retained, and the review anchored on AKTIP's scaffold functions.

---

*Provenance: Sequence retrieval + pairwise alignment executed this run (UniProt Q9H8T0/P61088/Q13404/Q15819): AKTIP has 2 Cys, none aligned to the UBE2N catalytic Cys87 column; ~41–45% aligned identity to UBE2N/UBE2V1/UBE2V2 — consistent with a catalytically inactive UEV. GO/InterPro/IntAct records retrieved via public APIs; literature via PubMed. Where a resource could not be queried it is stated; no results were fabricated.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)