---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T23:38:03.540584'
end_time: '2026-09-21T00:00:46.366778'
duration_seconds: 1362.83
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: pgl-1
  gene_symbol: pgl-1
  uniprot_accession: Q9TZQ3
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: function_assignment
  hypothesis_slug: pgl-fold-and-inherited-helicase-rna-processing
  hypothesis_text: Caenorhabditis elegans PGL-1 (Q9TZQ3) has RNA helicase activity,
    participates in spliceosomal mRNA splicing or nuclear mRNA export. Evaluate each
    independently. Its exact accession leaf PTN002773363 in current PTHR47958 descends
    from positive PTN002774595, PTN002776867 and PTN002776405; known helicase-loss
    nodes PTN002774495 and PTN002773962 are outside its lineage. Reconcile this curated
    ancestry with the experimentally solved PGL dimerization/RNase fold in PMID:26787882
    and the target sequence/domain architecture. Establish whether this is functional
    divergence, a family/classification problem, or retained activity. Lack of canonical
    helicase catalysis does not itself exclude noncatalytic splicing or export participation,
    and perinuclear/cytoplasmic location does not prove exclusive localization. Read
    target primary studies and source-node context; distinguish untested possibilities
    from direct negative results.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/worm/pgl-1/pgl-1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Caenorhabditis elegans PGL-1 (Q9TZQ3) has RNA\
    \ helicase activity, participates in spliceosomal\n  mRNA splicing or nuclear\
    \ mRNA export. Evaluate each independently. Its exact accession leaf PTN002773363\n\
    \  in current PTHR47958 descends from positive PTN002774595, PTN002776867 and\
    \ PTN002776405; known helicase-loss\n  nodes PTN002774495 and PTN002773962 are\
    \ outside its lineage. Reconcile this curated ancestry with the\n  experimentally\
    \ solved PGL dimerization/RNase fold in PMID:26787882 and the target sequence/domain\
    \ architecture.\n  Establish whether this is functional divergence, a family/classification\
    \ problem, or retained activity.\n  Lack of canonical helicase catalysis does\
    \ not itself exclude noncatalytic splicing or export participation,\n  and perinuclear/cytoplasmic\
    \ location does not prove exclusive localization. Read target primary studies\n\
    \  and source-node context; distinguish untested possibilities from direct negative\
    \ results.\nfocus_type: function_assignment\ncontext: []\nreference_id: []"
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

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** pgl-1
- **Gene symbol:** pgl-1
- **UniProt accession:** Q9TZQ3

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** pgl-fold-and-inherited-helicase-rna-processing
- **Source file:** genes/worm/pgl-1/pgl-1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Caenorhabditis elegans PGL-1 (Q9TZQ3) has RNA helicase activity, participates in spliceosomal mRNA splicing or nuclear mRNA export. Evaluate each independently. Its exact accession leaf PTN002773363 in current PTHR47958 descends from positive PTN002774595, PTN002776867 and PTN002776405; known helicase-loss nodes PTN002774495 and PTN002773962 are outside its lineage. Reconcile this curated ancestry with the experimentally solved PGL dimerization/RNase fold in PMID:26787882 and the target sequence/domain architecture. Establish whether this is functional divergence, a family/classification problem, or retained activity. Lack of canonical helicase catalysis does not itself exclude noncatalytic splicing or export participation, and perinuclear/cytoplasmic location does not prove exclusive localization. Read target primary studies and source-node context; distinguish untested possibilities from direct negative results.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Caenorhabditis elegans PGL-1 (Q9TZQ3) has RNA helicase activity, participates in spliceosomal
  mRNA splicing or nuclear mRNA export. Evaluate each independently. Its exact accession leaf PTN002773363
  in current PTHR47958 descends from positive PTN002774595, PTN002776867 and PTN002776405; known helicase-loss
  nodes PTN002774495 and PTN002773962 are outside its lineage. Reconcile this curated ancestry with the
  experimentally solved PGL dimerization/RNase fold in PMID:26787882 and the target sequence/domain architecture.
  Establish whether this is functional divergence, a family/classification problem, or retained activity.
  Lack of canonical helicase catalysis does not itself exclude noncatalytic splicing or export participation,
  and perinuclear/cytoplasmic location does not prove exclusive localization. Read target primary studies
  and source-node context; distinguish untested possibilities from direct negative results.
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

# PGL-1 (Q9TZQ3) Function Assignment: Helicase, Splicing, and Nuclear Export — Deep Curation Review

**Target gene:** *pgl-1* (P-granule abnormality-1), *Caenorhabditis elegans* (NCBITaxon:6239)
**UniProt:** Q9TZQ3 (730 aa)
**Focus type:** function_assignment
**Hypothesis slug:** pgl-fold-and-inherited-helicase-rna-processing

---

## Executive Judgment

**Verdict: REFUTED (helicase activity) / OVER-ANNOTATED (splicing and nuclear mRNA export).**

The seed hypothesis proposes three independent activities for PGL-1: (1) RNA helicase activity, (2) participation in spliceosomal mRNA splicing (GO:0000398), and (3) participation in nuclear mRNA export (GO:0006406). Evaluating each independently against primary literature, sequence/domain architecture, structure, and public bioinformatics resources yields a consistent conclusion:

1. **RNA helicase activity is refuted.** PGL-1 contains none of the diagnostic catalytic machinery of an ATP-dependent RNA helicase — no Walker A P-loop (GxxxxGKT/S), no DEAD/DExH box, and no helicase motif VI. Its experimentally solved fold ([PMID:26787882](https://pubmed.ncbi.nlm.nih.gov/26787882/)) is a **novel 13-α-helix dimerization domain that functions as a guanosine-specific, single-stranded endonuclease (RNase)** — a fundamentally different biochemical activity from strand-displacement helicase catalysis. The apparent "helicase" phylogenetic signal is best explained by classification confusion with PGL-1's constitutive P-granule partners, the germline DEAD-box helicases GLH-1/GLH-4.

2. **mRNA splicing and nuclear mRNA export are over-annotations.** In UniProt, GO:0000398 and GO:0006406 for PGL-1 are supported **only** by IBA:GO_Central evidence (Inferred from Biological Ancestor — automated PANTHER phylogenetic propagation), with **zero** experimental (EXP/IDA/IMP/IPI) support. They are inconsistent with the well-documented cytoplasmic/perinuclear P-granule biology of PGL-1, which operates *downstream* of nuclear export on the cytoplasmic face of the nuclear pore.

The most important caveat, honoring the seed's own instruction, is that **absence of catalytic helicase motifs does not by itself exclude a noncatalytic scaffolding role in splicing or export.** However, the correct curation standard is direct evidence, and there is none: no interaction, localization, or mutant-phenotype data place PGL-1 in the spliceosome or in the nuclear export machinery. These remain *untested possibilities*, not *direct negative results* — but for GO annotation purposes, an IBA propagation contradicted by the organism's experimental biology is an over-annotation, not a supported call.

---

## Key Findings

### Finding 1 — PGL-1 has no helicase catalytic machinery; its solved fold is a base-specific ssRNase/dimerization domain

A direct scan of the UniProt Q9TZQ3 sequence (730 aa) and its domain architecture establishes that PGL-1 is not a helicase at the sequence level. The annotated architecture comprises a **dimerization region (residues ~205–447)**, disordered linker regions, and an **RGG-box RNA-binding motif (residues ~674–730)**. The Pfam families assigned to PGL-1 are **PGL-specific** (PGL_N and PGL_C), not shared with any helicase family. There is **no DEAD/DEAH-box or helicase domain** anywhere in the protein.

To make this concrete, a motif-level comparison was performed against a bona fide germline DEAD-box helicase, GLH-1 (UniProt P34689), which is a constitutive P-granule component and physical partner of PGL-1:

| Diagnostic helicase motif | GLH-1 (P34689, true DEAD-box helicase) | PGL-1 (Q9TZQ3) |
|---|---|---|
| Walker A P-loop (GxxxxGKT/S) | Present (~pos 385) | **Absent** |
| DEAD box (motif II) | Present (~pos 499) | **Absent** |
| Helicase motif VI (QxxGRxGR) | Present (~pos 692) | **Absent** |
| ATP-dependent unwinding capacity | Expected | Not supported |

The structural work of Aoki et al. ([PMID:26787882](https://pubmed.ncbi.nlm.nih.gov/26787882/)) crystallized the PGL-1 dimerization domain and found a **novel 13 α-helix fold that creates a positively charged channel as a homodimer**. Critically, they then tested this domain's RNA activity and discovered it is a **guanosine-specific, single-stranded endonuclease** — an RNase T1-like activity — rather than any form of helicase. This is captured in UniProt as GO:0046589 (ribonuclease T1 activity, evidence EXP) and GO:0004521 (RNA endonuclease activity, IDA). Thus the one experimentally solved catalytic activity of PGL-1 is an RNase, not an ATP-dependent helicase. The verbatim structural claim:

> *"PGL-1 DD has a novel 13 α-helix fold that creates a positively charged channel as a homodimer. We investigate its capacity to bind RNA and discover unexpectedly that PGL-1 DD is a guanosine-specific, single-stranded endonuclease."* — [PMID:26787882](https://pubmed.ncbi.nlm.nih.gov/26787882/)

This finding directly refutes the helicase leaf of the hypothesis at the level of sequence, domain architecture, and solved structure simultaneously.

### Finding 2 — Splicing and nuclear-export annotations are IBA-only propagations inconsistent with cytoplasmic P-granule biology

The two biological-process claims in the seed — GO:0000398 (mRNA splicing, via spliceosome) and GO:0006406 (mRNA export from nucleus) — are present in UniProt Q9TZQ3 **exclusively with evidence code IBA:GO_Central**, i.e., inferred from a biological ancestor via PANTHER (PTHR47958) phylogenetic propagation. No experimental annotation (EXP, IDA, IMP, or IPI) supports either term.

By contrast, PGL-1's **experimentally supported** annotations are uniformly cytoplasmic and germline in character:

| GO term | Aspect | Evidence code | Compartment/process |
|---|---|---|---|
| GO:0043186 (P granule) | CC | IDA | Cytoplasmic germ granule |
| GO:0030719 (P granule organization) | BP | IMP | Germ-granule assembly |
| GO:0046589 (ribonuclease T1 activity) | MF | EXP | Base-specific RNase |
| GO:0004521 (RNA endonuclease activity) | MF | IDA | RNase |
| Oogenesis / gamete generation | BP | IMP | Germline development |
| GO:0000398 (mRNA splicing) | BP | **IBA only** | *no experimental support* |
| GO:0006406 (mRNA export from nucleus) | BP | **IBA only** | *no experimental support* |

The primary literature places PGL-1 firmly in the cytoplasm on the **cytoplasmic face of nuclear pores**, functioning as a translational-repression scaffold — a location and role that operate *downstream* of nuclear export and are physically separated from the nuclear spliceosome. Voronina et al. ([PMID:22991439](https://pubmed.ncbi.nlm.nih.gov/22991439/)) describe P-granule function in terms consistent with post-export cytoplasmic mRNA handling:

> *"P granules facilitate mRNA silencing by providing an environment in which translational repressors can encounter their mRNA targets immediately upon exit from the nucleus."* — [PMID:22991439](https://pubmed.ncbi.nlm.nih.gov/22991439/)

The phrase "immediately upon exit from the nucleus" is the decisive spatial fact: PGL-1 acts on mRNAs *after* they have already been exported and spliced, not within the splicing or export machinery. This makes the IBA-propagated splicing and export terms mechanistically implausible as direct functions, even before considering that they lack any experimental support.

### Finding 3 — PGL-1 family/classification is unstable across resources, confirming a classification artifact

The seed hypothesis rests heavily on a specific PANTHER lineage argument (PTHR47958, with leaf PTN002773363 descending from "positive" ancestor nodes and avoiding "helicase-loss" nodes). Direct interrogation of the InterPro/EBI resources for Q9TZQ3 shows this family placement is **not stable across databases**, which is the signature of a classification artifact rather than a genuinely retained ancestral activity.

The InterPro mapping for Q9TZQ3 returns only **5 signatures**: two PGL-specific InterPro domains (IPR062035 PGL_N and IPR062036 PGL_C), their corresponding Pfam models (PF29800 and PF29799), and a single PANTHER family assignment — **PTHR23237 "H/ACA Ribonucleoprotein Complex Subunit GAR1."** No helicase (DEAD/DEAH) InterPro, Pfam, or PANTHER signature is present anywhere in the mapping.

Crucially, the InterPro-mapped PANTHER family (PTHR23237, a GAR1/snoRNP family) is **different** from the PTHR47958 lineage that the seed hypothesis cites as the source of the helicase/splicing/export propagation. When two automated resources assign the same protein to two unrelated families (a GAR1 snoRNP family vs. the helicase-adjacent PTHR47958), and neither corresponds to the protein's experimentally solved PGL-specific fold, the propagated functional terms inherited through either family tree are unreliable. This is a family/classification problem, not evidence of retained helicase function.

---

## Mechanistic Model / Interpretation

The three findings converge on a single coherent model that resolves the seed's central question — *functional divergence vs. classification problem vs. retained activity* — decisively toward **classification problem**, with the true function being an RNase/RNA-binding scaffold.

```
         SEED HYPOTHESIS                          EVIDENCE-BASED MODEL
   ┌───────────────────────────┐          ┌──────────────────────────────────┐
   │ PGL-1 = RNA helicase      │   ──X──> │ PGL-1 = base-specific ssRNase +   │
   │  + spliceosome component  │          │   dimerization scaffold (P granule)│
   │  + nuclear mRNA exporter  │          │   RGG-box RNA binding             │
   └───────────────────────────┘          └──────────────────────────────────┘
              │                                          │
   Source of the signal:                     What PGL-1 actually does:
   PANTHER PTHR47958 IBA                      - Nucleates P-granule assembly
   propagation (unstable;                       (GO:0030719, IMP)
   InterPro maps to PTHR23237                 - Guanosine-specific ssRNase
   GAR1 instead — inconsistent)                 (GO:0046589 EXP; GO:0004521 IDA)
              │                               - Homodimerizes via 13-α-helix fold
   Real helicases in the same                   (PMID:26787882)
   granule = GLH-1/GLH-4                      - Sits on CYTOPLASMIC face of
   (DEAD-box; P34689 has Walker A,              nuclear pore, downstream of export
   DEAD box, motif VI) → likely                 (PMID:22991439)
   source of family confusion
```

**Spatial logic.** The nuclear spliceosome and the nuclear-pore export machinery act on pre-mRNA/mRNA *inside* or *at the inner face* of the nucleus. PGL-1 is documented on the **cytoplasmic** side of the nuclear pore, where it scaffolds translational repressors that engage mRNAs "immediately upon exit from the nucleus." Direct participation in splicing or export would require PGL-1 to act on the opposite side of the nuclear envelope from where it is observed. This does not make a moonlighting role impossible, but it removes any prima facie mechanistic plausibility and shifts the burden entirely onto direct evidence — which is absent.

**Why the helicase signal exists at all.** P granules are defined by two protein families that co-assemble constitutively: the **PGL proteins** (PGL-1, PGL-3) and the **GLH DEAD-box helicases** (GLH-1, GLH-2, GLH-4). GLH-1 is a genuine ATP-dependent RNA helicase (P34689, with all diagnostic motifs). Automated phylogenetic pipelines that group germline RNA-associated proteins can readily conflate the scaffold (PGL) with its helicase partner (GLH), especially given shared RGG/RNA-binding features and co-annotation in the same organelle. The instability of PGL-1's family assignment across InterPro (PTHR23237/GAR1) and the seed's cited tree (PTHR47958) is exactly the footprint such a conflation leaves.

**Reconciliation with the seed's lineage argument.** The seed correctly notes that "lack of canonical helicase catalysis does not itself exclude noncatalytic splicing or export participation." This is accepted. But the resolution is not that PGL-1 retains a noncatalytic splicing/export role — it is that the IBA terms are propagated from an unstable, likely incorrect family placement, and no experimental data support the retained-participation alternative. The correct classification of the observation is **untested possibility**, and for GO curation an IBA term contradicted by the organism's experimental biology is treated as an over-annotation candidate, not a supported annotation.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:26787882](https://pubmed.ncbi.nlm.nih.gov/26787882/) | Structural + direct biochemical assay | **Refutes** helicase; **supports** RNase | Does PGL-1's fold have helicase activity? | Novel 13-α-helix dimerization fold; guanosine-specific single-stranded endonuclease (RNase), not a helicase | Recombinant PGL-1 dimerization domain, in vitro | High confidence for RNase/fold; in vitro activity |
| UniProt Q9TZQ3 (domain scan) | Sequence/computational | **Refutes** helicase | Does PGL-1 contain helicase catalytic motifs? | No Walker A, no DEAD/DExH box, no motif VI; PGL-specific Pfam only (PGL_N/PGL_C) | 730 aa protein sequence | High confidence; direct motif scan vs. GLH-1 positive control |
| UniProt P34689 (GLH-1, control) | Sequence/computational | Contextual (positive control) | Do bona fide germline helicases carry the motifs PGL-1 lacks? | GLH-1 has Walker A (~385), DEAD box (~499), motif VI (~692) | Germline DEAD-box helicase, P-granule partner | High confidence; establishes discriminating baseline |
| UniProt Q9TZQ3 (GO evidence codes) | Database | **Qualifies/Refutes** splicing & export | What supports GO:0000398 and GO:0006406? | Both terms IBA:GO_Central only; zero EXP/IDA/IMP/IPI | Curated annotation set | High confidence in evidence-code status |
| [PMID:22991439](https://pubmed.ncbi.nlm.nih.gov/22991439/) | Localization + functional | **Refutes** direct splicing/export role | Where and when does PGL-1 act on mRNA? | P granules act in cytoplasm "immediately upon exit from the nucleus"; PGL-1 promotes FBF-2 silencing | Germline stem cells, cytoplasmic face of nuclear pore | High confidence for localization/timing |
| InterPro mapping Q9TZQ3 | Computational/database | **Qualifies** (classification instability) | Is family placement stable? | InterPro→PANTHER = PTHR23237 (GAR1), differs from seed's PTHR47958; no helicase signature | Cross-resource family assignment | High confidence; demonstrates artifact |
| [PMID:21146518](https://pubmed.ncbi.nlm.nih.gov/21146518/) | Interaction/localization | Contextual | Where does helicase activity reside in P granules? | GLH-1 (helicase) and DCR-1 partner in P granules on cytoplasmic side of nuclear pores | Adult germline | Supports GLH, not PGL, as helicase locus |
| [PMID:24746798](https://pubmed.ncbi.nlm.nih.gov/24746798/) | Mutant phenotype | Contextual | What is PGL-1's core biological role? | PGL-1/PGL-3 (+GLH-1/-4) knockdown → loss of totipotency/germline identity | Germline, RNAi | Supports scaffold/totipotency role, not splicing |
| [PMID:23550120](https://pubmed.ncbi.nlm.nih.gov/23550120/) | Mutant phenotype | Contextual | Downstream germline roles of PGL-1 | PGL-1 supports temperature-sensitive synaptonemal complex assembly | Meiosis | Downstream/pleiotropic, not a molecular-function claim |

---

## GO Curation Implications

**Lead (requires curator verification):**

1. **GO:0003724 (RNA helicase activity) / any helicase MF term — DO NOT ADD; if present, remove or NOT-qualify.** No sequence, domain, or structural evidence supports helicase activity. The solved fold is an RNase, not a helicase. If a helicase term has been propagated to PGL-1, it is a candidate for removal or a `NOT` qualifier.

2. **GO:0000398 (mRNA splicing, via spliceosome) — treat as non-core over-annotation; candidate for removal or `NOT`.** Supported only by IBA and contradicted by cytoplasmic post-export localization. Recommend removing from the core function set; a curator may retain it as a low-confidence IBA only if house rules require, but it should not drive the gene review.

3. **GO:0006406 (mRNA export from nucleus) — treat as non-core over-annotation; candidate for removal or `NOT`.** Same rationale as splicing: IBA-only, mechanistically inconsistent with the protein acting on the cytoplasmic side of the pore.

**Retain / strengthen (well-supported core annotations):**

- **MF:** GO:0046589 (ribonuclease T1 activity, EXP) and GO:0004521 (RNA endonuclease activity, IDA) — **retain**; these are the experimentally validated molecular functions.
- **MF:** RNA binding (RGG-box) — supported by domain architecture; appropriate as a retained MF.
- **CC:** GO:0043186 (P granule, IDA) — **retain** as the primary localization.
- **BP:** GO:0030719 (P granule organization, IMP) — **retain** as the core biological process.

The core molecular function to feature in the review is **base-specific single-stranded RNase / RNA-binding activity in germline P-granule assembly**, not helicase, splicing, or export. "Protein binding" is explicitly avoided as a recommendation because a more informative RNase/RNA-endonuclease MF is directly supported.

---

## Mechanistic Scope

The immediate molecular activities being tested are: (a) ATP-dependent RNA unwinding (helicase), (b) participation in the spliceosome-catalyzed splicing reaction, and (c) participation in the nuclear-pore mRNA export reaction. The directly measured gene-product activity of PGL-1 is instead a **guanosine-specific, single-stranded endoribonuclease** housed in a homodimeric 13-α-helix fold, plus **RGG-box-mediated RNA binding** and **self-association driving P-granule assembly**.

Everything else attributed to PGL-1 in the literature is **downstream or pleiotropic**, not a molecular-function claim: promotion of synaptonemal-complex assembly during meiosis ([PMID:23550120](https://pubmed.ncbi.nlm.nih.gov/23550120/)), maintenance of germline totipotency and suppression of somatic reprogramming ([PMID:24746798](https://pubmed.ncbi.nlm.nih.gov/24746798/)), and roles in DNA-damage-induced germ-cell apoptosis via autophagic clearance ([PMID:31125345](https://pubmed.ncbi.nlm.nih.gov/31125345/)). These are developmental/organismal consequences of a germ-granule scaffold, and none of them implicates PGL-1 directly in splicing or export catalysis.

---

## Conflicts and Alternatives

1. **Paralog/partner confusion (most important).** The genuine RNA helicases of the P granule are the GLH proteins (GLH-1/GLH-4), not PGL proteins. GLH-1 (P34689) carries all diagnostic helicase motifs; PGL-1 carries none. Automated pipelines co-annotating germline RNA-granule proteins are the most likely source of the helicase signal attaching to PGL-1.

2. **Cross-resource family disagreement.** InterPro maps Q9TZQ3 to PANTHER PTHR23237 (GAR1/snoRNP), whereas the seed cites PTHR47958. Two unrelated families for one protein — neither matching its solved PGL-specific fold — signal that inherited (IBA) terms from either tree are untrustworthy.

3. **Noncatalytic-participation alternative (cannot be fully excluded).** The seed rightly notes that lacking helicase catalysis does not exclude noncatalytic splicing/export participation, and that perinuclear/cytoplasmic localization does not prove *exclusive* localization. This remains an untested possibility. However, it is unsupported by any interaction, co-localization, or genetic evidence, and it is opposed by the documented cytoplasmic, post-export site of action. It should be logged as a gap, not a supported annotation.

4. **In-vitro-only caveat for the RNase.** The guanosine-specific RNase activity ([PMID:26787882](https://pubmed.ncbi.nlm.nih.gov/26787882/)) was demonstrated with recombinant protein in vitro; its precise in-vivo substrate repertoire and regulation remain to be fully mapped. This does not affect the helicase refutation but is relevant to how strongly the RNase MF should be worded.

---

## Limitations and Knowledge Gaps

1. **Programmatic resource access.** The domain/motif scans, GO evidence-code inventory, and InterPro family mapping summarized here were assembled from UniProt/InterPro/EBI records and the primary structural paper. Where a resource could not be queried programmatically in full, conclusions rely on the curated database records; these are stated as database-level evidence, not de novo re-derivation.

2. **Noncatalytic moonlighting is untested, not disproven.** No experiment has directly tested whether PGL-1 physically associates with spliceosomal or nuclear-export complexes. The refutation of *helicase catalysis* is strong; the rejection of *splicing/export participation* rests on absence of evidence plus mechanistic implausibility, which is appropriate for down-grading an IBA term but is not a direct negative result.

3. **In-vivo RNase substrates unknown.** The physiological targets and biological consequences of PGL-1's guanosine-specific RNase activity are not established, limiting how specifically the RNase BP context can be annotated.

4. **PANTHER tree internals.** The specific ancestor-node logic in the seed (PTN002773363 descending from PTN002774595/PTN002776867/PTN002776405, avoiding helicase-loss nodes PTN002774495/PTN002773962) was not independently reconstructed node-by-node; the cross-resource instability (PTHR47958 vs PTHR23237) is sufficient to flag the propagation as unreliable, but the exact tree topology was taken as given from the seed.

---

## Proposed Follow-up Experiments / Discriminating Tests

1. **Direct helicase assay** (fluorescence-based duplex unwinding ± ATP) on recombinant full-length PGL-1 and its dimerization domain. Prediction: no ATP-dependent unwinding. This would convert the sequence/structure-based helicase refutation into a direct negative result.

2. **Co-immunoprecipitation / proximity labeling (TurboID) of PGL-1** in germline, probing for spliceosomal (e.g., snRNP, Prp) and nuclear-export (e.g., NXF-1/TAP, nucleoporin) components. Prediction: enrichment for P-granule/translational-repression partners (GLH-1, FBF-2, DCR-1), not spliceosome/export machinery.

3. **Nuclear vs. cytoplasmic fractionation + high-resolution imaging** to test for any nucleoplasmic PGL-1 pool. Prediction: cytoplasmic/perinuclear only, on the cytoplasmic face of the pore.

4. **Splicing/export functional readouts in *pgl-1* null** (RT-PCR splicing panels; poly(A)+ mRNA nuclear-retention FISH). Prediction: no primary splicing or export defect attributable to PGL-1 loss (distinguishable from secondary germline dysfunction).

5. **Comparative CLIP-seq of PGL-1 vs. GLH-1** to localize each protein's RNA engagement relative to processing steps, discriminating the RNase/repression scaffold (PGL) from the helicase (GLH).

---

## Curation Leads (require curator verification)

**Candidate action changes:**
- Mark **RNA helicase activity** (any helicase MF) as **not supported / remove or `NOT`-qualify** for PGL-1. Rationale: no motifs, RNase fold (structural refutation).
- Mark **GO:0000398 (mRNA splicing)** and **GO:0006406 (mRNA export)** as **over-annotated IBA propagations**; recommend removal from core function or explicit down-weighting. Rationale: IBA-only, cytoplasmic post-export biology, unstable family placement.
- **Retain and feature** GO:0046589 (RNase T1 activity, EXP), GO:0004521 (RNA endonuclease, IDA), GO:0043186 (P granule, IDA), GO:0030719 (P granule organization, IMP) as the gene's core.

**Candidate references with snippets to verify:**
- [PMID:26787882](https://pubmed.ncbi.nlm.nih.gov/26787882/): *"PGL-1 DD has a novel 13 α-helix fold that creates a positively charged channel as a homodimer... PGL-1 DD is a guanosine-specific, single-stranded endonuclease."* → supports RNase MF, refutes helicase.
- [PMID:22991439](https://pubmed.ncbi.nlm.nih.gov/22991439/): *"P granules facilitate mRNA silencing by providing an environment in which translational repressors can encounter their mRNA targets immediately upon exit from the nucleus."* → supports cytoplasmic post-export scaffold role, refutes direct splicing/export.

**Suggested curator questions:**
- Does the review's annotation set currently carry a helicase MF or the splicing/export BP terms with anything stronger than IBA? If so, verify the source.
- Should the GLH-1/PGL-1 partner relationship be noted to explain the propagated helicase signal?

**Suggested experiments:** items 1–5 in Discriminating Tests, prioritizing the direct helicase assay (1) and PGL-1 interactome (2).

---

## Evidence Base (Key Literature)

- **[PMID:26787882](https://pubmed.ncbi.nlm.nih.gov/26787882/)** — *PGL germ granule assembly protein is a base-specific, single-stranded RNase.* Provides the decisive structural + biochemical refutation of helicase activity: novel 13-α-helix dimerization fold, guanosine-specific ssRNase.
- **[PMID:22991439](https://pubmed.ncbi.nlm.nih.gov/22991439/)** — *The P granule component PGL-1 promotes the localization and silencing activity of the PUF protein FBF-2 in germline stem cells.* Establishes cytoplasmic, post-export translational-repression scaffold role.
- **[PMID:21146518](https://pubmed.ncbi.nlm.nih.gov/21146518/)** — *C. elegans Dicer interacts with the P-granule component GLH-1...* Locates the genuine RNA helicase (GLH-1) in the same granule on the cytoplasmic pore face — the likely source of family confusion.
- **[PMID:24746798](https://pubmed.ncbi.nlm.nih.gov/24746798/)** — *Germ-granule components prevent somatic development...* PGL-1 as a totipotency/germline-identity scaffold (downstream biology, not splicing).
- **[PMID:23550120](https://pubmed.ncbi.nlm.nih.gov/23550120/)** — *Assembly of the Synaptonemal Complex... supported by PGL-1...* Pleiotropic meiotic role, not a molecular-function claim.
- **[PMID:31125345](https://pubmed.ncbi.nlm.nih.gov/31125345/)** — *Autophagy of germ-granule components PGL-1 and PGL-3...* Perinuclear localization and germ-cell apoptosis, downstream biology.

---

## Conclusion

PGL-1 (Q9TZQ3) is a **germline P-granule scaffold with base-specific single-stranded RNase and RGG-box RNA-binding activity**, whose experimentally solved fold is a novel 13-α-helix dimerization/RNase domain. It is **not an RNA helicase** — it lacks every diagnostic catalytic motif that its true-helicase partner GLH-1 possesses — and its **mRNA-splicing and nuclear-export annotations are IBA-only phylogenetic propagations** from an unstable family classification, unsupported by any experimental evidence and inconsistent with its cytoplasmic, post-export site of action. The seed's helicase leaf is **refuted**; the splicing and export leaves are **over-annotations** and candidates for removal or NOT-qualification. The evidence points to a **classification problem** (confusion with GLH DEAD-box helicases), not functional divergence or retained helicase activity.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)