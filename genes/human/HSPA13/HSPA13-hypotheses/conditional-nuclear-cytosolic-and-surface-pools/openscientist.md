---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T00:36:49.617893'
end_time: '2026-09-21T01:03:39.557193'
duration_seconds: 1609.94
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: HSPA13
  gene_symbol: HSPA13
  uniprot_accession: P48723
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: conditional-nuclear-cytosolic-and-surface-pools
  hypothesis_text: Human HSPA13 localizes to the nucleus, plasma membrane or cytosol.
    Assess each independently using primary evidence, isoforms/constructs and physiological
    conditions. Reconcile ER-luminal proximity-labeling evidence with reported NKCC2
    cytoplasmic-tail interaction and examine whether any secondary pool was actually
    demonstrated. A main ER residence or secretory-pathway role does not establish
    exclusivity. The existing protein-folding report is related but does not adjudicate
    these localization claims.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/HSPA13/HSPA13-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human HSPA13 localizes to the nucleus, plasma\
    \ membrane or cytosol. Assess each independently\n  using primary evidence, isoforms/constructs\
    \ and physiological conditions. Reconcile ER-luminal proximity-labeling\n  evidence\
    \ with reported NKCC2 cytoplasmic-tail interaction and examine whether any secondary\
    \ pool was\n  actually demonstrated. A main ER residence or secretory-pathway\
    \ role does not establish exclusivity.\n  The existing protein-folding report\
    \ is related but does not adjudicate these localization claims.\nfocus_type: function_assignment\n\
    context: []\nreference_id: []"
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

# AIGR Gene Hypothesis Deep Research

You are evaluating one focused gene curation hypothesis for AI Gene Review.
This is not a general gene overview. Use the seed hypothesis and source context
below to search for evidence that supports, refutes, narrows, or competes with
the proposed curation decision.

## Target Gene

- **Organism code:** human
- **Taxon:** Homo sapiens (NCBITaxon:9606)
- **Gene directory:** HSPA13
- **Gene symbol:** HSPA13
- **UniProt accession:** P48723

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** conditional-nuclear-cytosolic-and-surface-pools
- **Source file:** genes/human/HSPA13/HSPA13-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human HSPA13 localizes to the nucleus, plasma membrane or cytosol. Assess each independently using primary evidence, isoforms/constructs and physiological conditions. Reconcile ER-luminal proximity-labeling evidence with reported NKCC2 cytoplasmic-tail interaction and examine whether any secondary pool was actually demonstrated. A main ER residence or secretory-pathway role does not establish exclusivity. The existing protein-folding report is related but does not adjudicate these localization claims.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human HSPA13 localizes to the nucleus, plasma membrane or cytosol. Assess each independently
  using primary evidence, isoforms/constructs and physiological conditions. Reconcile ER-luminal proximity-labeling
  evidence with reported NKCC2 cytoplasmic-tail interaction and examine whether any secondary pool was
  actually demonstrated. A main ER residence or secretory-pathway role does not establish exclusivity.
  The existing protein-folding report is related but does not adjudicate these localization claims.
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

# HSPA13 (STCH) Localization Hypothesis — Final Curation Report

**Gene:** HSPA13 / STCH (human) · **UniProt:** P48723 · **Taxon:** *Homo sapiens* (NCBITaxon:9606)
**Focus type:** function_assignment · **Hypothesis slug:** conditional-nuclear-cytosolic-and-surface-pools
**Source file:** `genes/human/HSPA13/HSPA13-ai-review.yaml`

---

## Summary

**Verdict: Over-annotated / refuted for the nuclear and plasma-membrane pools; unresolved (indirect inference only) for the cytosolic pool.**

The seed hypothesis proposes that human HSPA13 localizes — as independently demonstrable pools — to the **nucleus**, **plasma membrane**, or **cytosol**, and asks whether ER-luminal proximity-labeling evidence can be reconciled with a reported NKCC2 cytoplasmic-tail interaction. After auditing the actual GO annotation provenance, the primary experimental literature, and the protein's sequence architecture, the conclusion is that the nuclear, plasma-membrane, and cytosolic Cellular Component (CC) annotations on P48723 are **IBA (Inferred from Biological Ancestor) phylogenetic inferences** propagated from the broader HSP70 family, **not** HSPA13-specific experimental findings. None of these three secondary pools is supported by an IDA/IMP/HDA/TAS experimental annotation for HSPA13 itself, and the Human Protein Atlas reports no confident immunofluorescence subcellular localization.

The **directly supported** localization for HSPA13/STCH is the **endoplasmic reticulum / microsome / secretory pathway**. This is established by (1) a cleaved N-terminal signal peptide (residues 1–22) and the absence of any transmembrane segment; (2) immunofluorescence plus subcellular fractionation showing microsomal enrichment ([PMID: 8131751](https://pubmed.ncbi.nlm.nih.gov/8131751/)); (3) an independent description of STCH as "a microsomal protein" ([PMID: 18793616](https://pubmed.ncbi.nlm.nih.gov/18793616/)); and (4) an HDA extracellular-exosome annotation ([PMID: 19199708](https://pubmed.ncbi.nlm.nih.gov/19199708/)) consistent with secretory/endosomal egress rather than a nuclear or cytosolic functional pool.

The reported NKCC2 interaction ([PMID: 33672238](https://pubmed.ncbi.nlm.nih.gov/33672238/)) is with the **ER-resident (immature) form** of NKCC2 in an **ERAD** context — it locates STCH in the ER biogenesis/quality-control machinery and does **not** demonstrate a cytosolic or cytoplasmic-tail-facing pool. The one genuine, unresolved topological question is raised by [PMID: 10675567](https://pubmed.ncbi.nlm.nih.gov/10675567/), which shows cytosolic ubiquitin-like proteins (UBQLN/BAG6-family homologs) binding a peptide within the STCH ATPase domain — a binding assay, not an in-situ localization. **Overall: retain/strengthen ER; flag nucleus, plasma membrane, and cytosol as paralog carry-over lacking direct support.**

---

## Executive Judgment

**Partially supported / over-annotated → the secondary pools were not demonstrated.** Evaluated as a function-assignment (CC) hypothesis, HSPA13 does **not** directly and demonstrably carry the nucleus, plasma-membrane, or cytosol GO terms. Those terms exist on the record only as IBA inferences transferred from cytosolic/nuclear HSP70 paralogs. The gene product's directly supported location is the ER/microsome/secretory pathway. The cytosolic pool is the only one with a mechanistic hint (UbL/BAG6 binding to the ATPase core), but that hint is unresolved and does not rise to a demonstrated pool. The most important caveat is that IBA annotations are legitimate GO evidence; the issue is that for a **divergent** family member with its own experimentally supported compartment, blanket transfer of generic HSP70 localizations is a systematic over-annotation risk.

---

## Key Findings

### Finding 1 — The nucleus, plasma-membrane, and cytosol CC terms are IBA paralog carry-over, not HSPA13 evidence

An annotation-provenance audit of P48723 (via QuickGO/UniProt, executed with `requests`) shows the following Cellular Component landscape:

| GO CC term | GO ID | Evidence code | Source | Interpretation |
|---|---|---|---|---|
| Nucleus | GO:0005634 | **IBA** | GO_REF:0000033 | Phylogenetic inference from HSP70 ancestors |
| Cytoplasm | GO:0005737 | **IBA** | GO_REF:0000033 | Phylogenetic inference |
| Cytosol | GO:0005829 | **IBA** | GO_REF:0000033 | Phylogenetic inference |
| Plasma membrane | GO:0005886 | **IBA** | UniProt dump | Phylogenetic inference |
| Endoplasmic reticulum | GO:0005783 | **IEA** | UniProtKB-SubCell SL-0095 | Sequence/keyword-based, ER |
| Extracellular exosome | GO:0070062 | **HDA** | PMID:19199708 | High-throughput direct assay |

Critically, the "with/from" support panels for the nucleus, cytosol, cytoplasm, and plasma-membrane IBA annotations are dominated by **other HSP70 family members** — P11142 (HSPA8/HSC70), P11021 (HSPA5/BiP), P17066, P34931, and yeast/worm/plant orthologs. These are cytosolic and nuclear-cytoplasmic Hsp70 paralogs whose localizations were transferred onto HSPA13 by the Reference Genome phylogenetic annotation pipeline. **No IDA, IMP, HDA, or TAS experimental annotation supports nucleus, plasma membrane, or cytosol for HSPA13 specifically.** Consistent with this, the Human Protein Atlas reports no confident subcellular immunofluorescence localization for HSPA13 (Subcellular location => None), so there is no independent imaging support for the secondary pools.

**Curation consequence:** IBA annotations are legitimate GO evidence, but for a divergent family member with its own experimentally supported compartment, transferring generic HSP70 cytosolic/nuclear localizations risks a systematic over-annotation. These three CC terms should be flagged as non-core / paralog-derived.

### Finding 2 — The primary experimental localization is ER / microsome, via a cleaved signal peptide

UniProt P48723 feature annotation shows a **signal peptide at residues 1–22 (cleaved)**, a mature chain at 23–471, and **no transmembrane domain**. This is the canonical architecture of a soluble secretory-pathway (ER-luminal) protein, not a cytosolic Hsp70.

The foundational primary paper, Otterson et al. 1994 ([PMID: 8131751](https://pubmed.ncbi.nlm.nih.gov/8131751/), *"Stch encodes the 'ATPase core' of a microsomal stress 70 protein"*), reports that STCH migrates predominantly as a ~60 kDa species enriched in a membrane-bound microsome fraction (immunofluorescence + subcellular fractionation); has a unique hydrophobic leader sequence; is calcium (A23187)-inducible but NOT heat-inducible; and has a truncated C-terminal peptide-binding domain with peptide-independent ATPase activity.

> *"Immunofluorescent and subcellular analyses show that STCH migrates predominantly as a 60 kDa species and is enriched in a membrane-bound microsome fraction."* — PMID:8131751 (verified snippet)

Yamagata et al. 2008 ([PMID: 18793616](https://pubmed.ncbi.nlm.nih.gov/18793616/)) independently describe STCH as "**a microsomal protein** that contains a N-terminal ATPase domain but lacks a C-terminal protein binding domain," reinforcing the ER/secretory assignment.

> *"a member of the heat shock protein 70 (HSP70) superfamily, is a microsomal protein that contains a N-terminal ATPase domain but lacks a C-terminal protein binding domain"* — PMID:18793616 (verified snippet)

The **HDA extracellular-exosome** annotation (PMID:19199708) fits the same secretory/endosomal narrative: an ER-luminal chaperone can egress via multivesicular bodies into exosomes (cf. the urinary-exosome proteomics context of [PMID: 19056867](https://pubmed.ncbi.nlm.nih.gov/19056867/)). This is not evidence of a nuclear or cytosolic functional pool.

### Finding 3 — The NKCC2 interaction is an ER/ERAD context, not a demonstrated cytosolic pool

Bakhos-Douaihy et al. 2021 ([PMID: 33672238](https://pubmed.ncbi.nlm.nih.gov/33672238/)) identify STCH as a binding partner of the **ER-resident (immature, ER-retained) form** of NKCC2/SLC12A1, promoting its **ER-associated degradation** (proteasomal plus ER-to-lysosome routing) and impairing NKCC2 maturation and cell-surface expression.

> *"we report the identification of chaperone stress 70 protein (STCH) and the stress-inducible heat shock protein 70 (Hsp70), as two novel binding partners of the ER-resident form of NKCC2"* — PMID:33672238 (verified snippet)

This is an **ER-lumen / ER-membrane biogenesis** context. The co-immunoprecipitation does **not** map the STCH contact to the NKCC2 cytoplasmic tail specifically, and it does not establish that STCH is present in the cytosol. The seed hypothesis's framing — that a "NKCC2 cytoplasmic-tail interaction" competes with ER-luminal evidence — is not supported by the primary data: the interaction is with the ER-resident client during quality control, fully consistent with an ER-luminal STCH pool acting on nascent/misfolded NKCC2.

Separately, Kaye et al. 2000 ([PMID: 10675567](https://pubmed.ncbi.nlm.nih.gov/10675567/)) isolated two human ubiquitin-like (UbL) proteins (Chap1/Chap2 — UBQLN/Dsk2 and Scythe/BAG6-family homologs) that bind a short peptide within the **ATPase domain** of STCH.

> *"We have isolated two human ubiquitin-like (UbL) proteins that bind to a short peptide within the ATPase domain of the Hsp70-like Stch protein."* — PMID:10675567 (verified snippet)

Because UBQLN/BAG6-family proteins are cytosolic, this interaction would require cytosolic exposure of the STCH ATPase core. However, it was demonstrated by in-vitro binding/isolation assays, **not** by in-situ localization. It is a legitimate unresolved topology question — not a demonstrated cytosolic pool.

### Finding 4 — Sequence architecture is secretory (BiP-like), lacking the cytosolic-Hsp70 EEVD/TPR signature

A computed sequence audit (UniProt FASTA; Needleman–Wunsch alignment in numpy) shows HSPA13's architecture aligns with ER/secretory Hsp70s, not cytosolic ones:

| Feature | HSPA13 (P48723) | HSC70/HSPA8 (cytosolic) | HSPA1A (cytosolic) | BiP/HSPA5 (ER) |
|---|---|---|---|---|
| N-terminus | `MAREMTILGSAVLTLLLAGYLAQQY` (hydrophobic ER signal, sig. pep. 1–22) | `M…GIDLGTTYSCV` (Hsp70 NBD motif, no signal peptide) | `M…GIDLGTTYSCV` (no signal peptide) | `MKLSLVAAMLLLLSAAR\|A` (ER signal peptide) |
| C-terminal motif | ends `HLQKTNFN` — **no EEVD, no KDEL/HDEL** | ends **EEVD** (TPR/Hop/CHIP docking) | ends **EEVD** | ends **KDEL** (ER retention) |
| Global NW identity to HSPA13 | — | 29.5% | 30.3% | 30.8% |

Key implications:

- HSPA13 begins with a **hydrophobic ER signal**, like BiP — not with the cytosolic Hsp70 nucleotide-binding-domain motif `GIDLGTTYSCV` that opens HSC70 and HSPA1A.
- HSPA13 **lacks the C-terminal EEVD** motif that is the docking signature for cytosolic TPR co-chaperones (Hop, CHIP). This directly undercuts the assumption that HSPA13 behaves like a cytosolic Hsp70 in the cytoplasm/nucleus.
- HSPA13 also **lacks KDEL/HDEL**, so it is not a classically ER-retained luminal chaperone in the BiP sense — consistent with its being a divergent, secretory-competent, exosome-detectable protein with a **truncated substrate-binding domain** and a **~50-aa ATPase insertion**.
- Global identity to each reference (~29–31%) shows HSPA13 is a **divergent, roughly equidistant** family member — precisely the situation in which uncritical IBA transfer of paralog localizations is most error-prone.

---

## Mechanistic Model / Interpretation

The evidence converges on a single coherent model:

```
                       HSPA13 / STCH  (P48723)
                  divergent HSP70-superfamily member
        signal peptide 1–22 · truncated SBD · Ca2+-inducible · not heat-inducible

   ┌───────────────────────────── ER / MICROSOME (PRIMARY) ─────────────────────────────┐
   │  • Cleaved N-terminal signal peptide targets it to the secretory pathway            │
   │  • Microsomal enrichment by IF + fractionation (PMID 8131751)                        │
   │  • "microsomal protein" (PMID 18793616)                                              │
   │  • Binds ER-resident (immature) NKCC2 → ERAD / quality control (PMID 33672238)       │
   │  • ATPase-driven, peptide-independent activity (truncated SBD)                       │
   └──────────────────────────────────────────┬──────────────────────────────────────────┘
                                               │ secretory / MVB egress
                                               ▼
                                  EXTRACELLULAR EXOSOME (HDA, PMID 19199708)

   ┌──────────────── SECONDARY POOLS AS ANNOTATED (nucleus / PM / cytosol) ──────────────┐
   │  • All three = IBA (GO_REF:0000033), "with/from" = HSPA8, HSPA5, HSPA6, orthologs     │
   │  • No IDA/IMP/HDA/TAS for HSPA13 · HPA subcellular = None                             │
   │  → PARALOG CARRY-OVER, not demonstrated                                               │
   └──────────────────────────────────────────────────────────────────────────────────────┘

   ┌──────────────── UNRESOLVED TOPOLOGY QUESTION (cytosol only) ─────────────────────────┐
   │  • Cytosolic UbL/BAG6 (UBQLN, Scythe/BAG6) bind STCH ATPase peptide (PMID 10675567)   │
   │  • Would require cytosolic exposure of ATPase core — shown by binding assay, not      │
   │    by in-situ localization → hypothesis, not established pool                          │
   └──────────────────────────────────────────────────────────────────────────────────────┘
```

In plain terms: HSPA13 is an ER/microsomal, secretory-pathway member of the HSP70 superfamily that participates in ER protein quality control (illustrated by its role in NKCC2 ERAD) and can be exported into exosomes. Its nuclear, plasma-membrane, and cytosolic GO annotations are artifacts of phylogenetic (IBA) transfer from its cytosolic paralogs and are not backed by any HSPA13-specific experiment. The only mechanistic hint toward a cytosol-facing role is the UbL/BAG6 binding to the ATPase core, which raises — but does not resolve — a question about whether some of the ATPase domain is ever cytosolically exposed (e.g., during retrotranslocation or in an alternate topology). That question deserves a targeted experiment before any cytosolic annotation is asserted as HSPA13-specific.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [8131751](https://pubmed.ncbi.nlm.nih.gov/8131751/) | Localization (IF + fractionation) | **Supports ER**, refutes secondary pools as primary | Where does STCH localize? | ~60 kDa, enriched in microsome fraction; hydrophobic leader; Ca2+-inducible; truncated SBD; not heat-inducible | Human, cell lines | High for microsomal residence; 1994-era resolution, no super-res imaging |
| [18793616](https://pubmed.ncbi.nlm.nih.gov/18793616/) | Primary description | **Supports ER** | Is STCH microsomal? | Explicitly "a microsomal protein"; N-terminal ATPase, no C-terminal SBD | Human, stomach cancer | Moderate–high; localization stated, not the paper's main assay |
| [33672238](https://pubmed.ncbi.nlm.nih.gov/33672238/) | Interaction (co-IP) + phenotype | **Qualifies** (ER/ERAD context), does not support cytosol | Does STCH bind cytoplasmic tail / cytosolic pool? | STCH binds **ER-resident** immature NKCC2, promotes ERAD, impairs maturation/surface expression | Human/heterologous cells, SLC12A1 | High for ER-client interaction; does not map contact to cytoplasmic tail nor localize STCH to cytosol |
| [10675567](https://pubmed.ncbi.nlm.nih.gov/10675567/) | Interaction (binding/isolation) | **Competing / unresolved** for cytosol | Is ATPase core cytosolically exposed? | Cytosolic UbL proteins (UBQLN/BAG6 homologs) bind a peptide in the STCH ATPase domain | Human, in-vitro binding | Moderate; binding assay, not in-situ localization; topology inferred |
| [19199708](https://pubmed.ncbi.nlm.nih.gov/19199708/) | HDA (proteomics) | **Supports secretory egress** | Is STCH exosomal? | GO:0070062 extracellular exosome (HDA) | Human exosomes | Moderate; consistent with secretory route, not nucleus/cytosol |
| QuickGO/UniProt audit (GO_REF:0000033) | Review/database | **Refutes** secondary pools as HSPA13-specific | Are nucleus/PM/cytosol experimentally supported? | All three = IBA; with/from = HSPA8, HSPA5, HSPA6, orthologs; no IDA/IMP/HDA/TAS | Annotation provenance | High; IBA is inference, not experiment |
| UniProt P48723 sequence audit | Structural/evolutionary (computed) | **Supports ER**, refutes cytosolic-Hsp70 behavior | Does HSPA13 have cytosolic-Hsp70 features? | Signal peptide 1–22, no TM; no EEVD; no KDEL; ~29–31% id to HSC70/BiP/HSPA1A | Computed alignment | High for motif presence/absence; identity from pairwise NW |

---

## Evidence Base

**Primary localization anchors.** *Stch encodes the 'ATPase core' of a microsomal stress 70 protein* ([PMID: 8131751](https://pubmed.ncbi.nlm.nih.gov/8131751/)) is the single most important paper: it provides direct IF and fractionation evidence for microsomal enrichment and describes the defining architecture (hydrophobic leader, truncated substrate-binding domain, Ca2+-inducibility, peptide-independent ATPase). *Stomach cancer-derived del223V-226L mutation of the STCH gene* ([PMID: 18793616](https://pubmed.ncbi.nlm.nih.gov/18793616/)) independently labels STCH "a microsomal protein," corroborating the ER/secretory assignment while linking STCH to TRAIL-mediated apoptosis sensitization.

**Interaction context.** *Differential Effects of STCH and Stress-Inducible Hsp70 on the Stability and Maturation of NKCC2* ([PMID: 33672238](https://pubmed.ncbi.nlm.nih.gov/33672238/)) places STCH firmly in ER quality control by identifying it as a partner of the ER-resident form of NKCC2 that promotes ERAD. This is the paper the seed hypothesis invokes as a "cytoplasmic-tail interaction," but the primary text describes an **ER-resident-client** interaction, not a cytosolic tail contact. *A family of ubiquitin-like proteins binds the ATPase domain of Hsp70-like Stch* ([PMID: 10675567](https://pubmed.ncbi.nlm.nih.gov/10675567/)) is the sole line of evidence hinting at cytosolic exposure of STCH's ATPase core; it is a binding study, so it raises rather than resolves the cytosol question.

**Secretory egress.** The extracellular-exosome HDA annotation (PMID:19199708; and the related urinary-exosome proteomics context of [PMID: 19056867](https://pubmed.ncbi.nlm.nih.gov/19056867/)) is consistent with an ER/secretory protein being exported via multivesicular bodies.

**Peripheral transcriptomic mentions.** HSPA13 appears as a differentially expressed gene in estrogen-receptor and breast-cancer studies ([PMID: 32387340](https://pubmed.ncbi.nlm.nih.gov/32387340/); [PMID: 25541910](https://pubmed.ncbi.nlm.nih.gov/25541910/)). These are expression/regulation observations and carry **no localization information**; they do not bear on the CC hypothesis.

---

## GO Curation Implications

**Leads requiring curator verification** (not automated changes):

1. **Retain / strengthen `GO:0005783` endoplasmic reticulum (CC).** Currently IEA (UniProtKB-SubCell). It is backed by direct experimental localization (PMID:8131751) and an independent microsomal description (PMID:18793616). Consider upgrading the evidence basis by citing PMID:8131751 as experimental (IDA-type) support and/or annotating **microsome/ER lumen** more specifically. The signal peptide + truncated SBD architecture supports an ER/secretory chaperone role.

2. **Flag `GO:0005634` nucleus, `GO:0005886` plasma membrane, and `GO:0005829` cytosol (all IBA) as paralog carry-over.** They lack any HSPA13-specific experimental support, and their "with/from" panels are dominated by cytosolic/nuclear HSP70 paralogs. These are candidates to be **removed, or retained only as non-core IBA** with an explicit curator note that they are phylogenetic inferences not demonstrated for HSPA13. This directly answers the seed hypothesis: the secondary pools were **not actually demonstrated**.

3. **`GO:0070062` extracellular exosome (HDA)** may be retained as-is; it reflects secretory/exosomal egress, not a nuclear/cytosolic functional pool.

4. **Do not add a cytosol annotation** on the strength of PMID:10675567 alone; the topology is inferred from a binding assay. If a BP/MF term is desired to capture the ER-quality-control role, an **ERAD / ER protein quality-control BP** term supported by PMID:33672238 is a better-informed lead than a generic "protein binding" MF term.

---

## Mechanistic Scope

The immediate molecular activity under test is **subcellular localization** (a CC assignment), coupled to HSPA13's role as an **ATP-dependent HSP70-superfamily chaperone** with a truncated, peptide-independent substrate-binding capacity operating in the ER/secretory pathway. The directly demonstrated gene-product-level facts are: (a) signal-peptide-directed ER/microsomal residence; (b) participation in ER quality control of a membrane client (NKCC2) via ERAD. Everything else attributed by the seed hypothesis — nuclear, plasma-membrane, cytosolic pools — is either downstream inference (IBA transfer) or an unproven topology question (UbL/BAG6 binding). The breast-cancer/estrogen expression signals are transcriptional responses, not localization, and are outside the mechanistic scope of this CC hypothesis.

---

## Conflicts and Alternatives

- **Paralog confusion (primary alternative).** The nucleus/PM/cytosol annotations are the expected localizations of cytosolic HSP70s (HSPA8/HSC70, HSPA1A) and were transferred to HSPA13 by IBA. This is the most parsimonious explanation for the secondary pools and is the leading alternative to a genuine multi-compartment HSPA13.
- **Isoform/construct caveats.** The seed hypothesis rightly asks about isoforms/constructs. Overexpressed or signal-peptide-deleted constructs could mislocalize; none of the primary localization papers here relied on tagged over-expression to claim ER (PMID:8131751 used endogenous-scale IF + fractionation). No isoform-specific nuclear/cytosolic localization was found in the reviewed literature.
- **Topology question (genuine).** PMID:10675567's cytosolic UbL binding to the ATPase core is a real conflict with a strictly ER-luminal model and cannot be dismissed; it is simply unproven by localization.
- **Database carry-over.** The UniProt "plasma membrane" line and the QuickGO IBA set are the database-level source of the hypothesis; they should be treated as orientation, not evidence.

---

## Limitations and Knowledge Gaps

1. **No high-resolution HSPA13-specific imaging.** HPA reports no confident IF localization; PMID:8131751 imaging is 1994-era. *What to resolve:* endogenous-tag or validated-antibody confocal/immuno-EM across ER, nucleus, PM, cytosol.
2. **Cytosolic exposure of the ATPase core is unresolved.** PMID:10675567 shows binding but not localization. *Why it matters:* it is the only mechanistic basis for any cytosol annotation. *Resolve with:* proximity labeling (BioID/APEX at ER lumen vs cytosol), protease-protection topology assays.
3. **NKCC2 contact site not mapped.** PMID:33672238 does not localize the STCH–NKCC2 interface to the cytoplasmic tail. *Resolve with:* domain-mapping co-IP / crosslinking to determine whether the contact is luminal or cytosolic.
4. **No proximity-labeling dataset for HSPA13 was directly accessible in this run.** The seed hypothesis references "ER-luminal proximity-labeling evidence"; that specific dataset was not retrievable here and should be located and cited directly by the curator.
5. **Exosome route vs plasma-membrane residence not disentangled.** Exosomal detection (PMID:19199708) does not equal a stable plasma-membrane pool.

---

## Discriminating Tests

1. **Split proximity labeling:** APEX2/TurboID fused to HSPA13 (respecting the signal peptide) plus orthogonal ER-lumen, cytosol, and nuclear baits — directly quantifies which compartments HSPA13 samples.
2. **Protease-protection / topology assay** on microsomes ± detergent to test whether any HSPA13 ATPase epitope is cytosolically exposed (tests the PMID:10675567 implication).
3. **Endogenous CRISPR knock-in tag** (e.g., HaloTag) + confocal and immuno-EM to score nucleus/PM/cytosol pools without over-expression artifacts.
4. **Signal-peptide-deletion construct** to determine whether removing ER targeting redirects HSPA13 to cytosol/nucleus — clarifying whether any secondary pool is physiological or construct-dependent.
5. **NKCC2 interface mapping** (truncation/crosslinking co-IP) to test the "cytoplasmic-tail interaction" claim explicitly.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**Candidate references + exact snippets to verify:**

- PMID:8131751 — *"...STCH migrates predominantly as a 60 kDa species and is enriched in a membrane-bound microsome fraction."* → supports ER/microsome CC.
- PMID:18793616 — *"...is a microsomal protein that contains a N-terminal ATPase domain but lacks a C-terminal protein binding domain"* → supports ER; supports truncated-SBD MF nuance.
- PMID:33672238 — *"...STCH...as two novel binding partners of the ER-resident form of NKCC2"* → ER/ERAD context; **does not** support cytosol.
- PMID:10675567 — *"...ubiquitin-like (UbL) proteins that bind to a short peptide within the ATPase domain of the Hsp70-like Stch protein."* → unresolved cytosolic-topology question only.

**Candidate GO actions:**

- **Retain/strengthen** GO:0005783 (ER, CC) with experimental citation PMID:8131751; consider a more specific ER-lumen/microsome term.
- **Flag as non-core / candidate removal** GO:0005634 (nucleus), GO:0005886 (plasma membrane), GO:0005829 (cytosol) — all IBA paralog carry-over, no HSPA13 experimental support.
- **Retain** GO:0070062 (exosome, HDA).
- Consider an **ERAD / ER protein quality-control BP** term supported by PMID:33672238 instead of leaving only generic protein binding.

**Suggested curator questions:** Which specific proximity-labeling dataset underlies the "ER-luminal" claim in the seed? Is any HSPA13 isoform annotated without the signal peptide? Does any experimental (non-IBA) source place HSPA13 in the nucleus/PM/cytosol?

**Suggested experiments:** the five discriminating tests above, prioritizing split proximity labeling and topology/protease-protection.

---

### Bottom line

HSPA13/STCH is an **ER/microsomal, secretory-pathway HSP70-superfamily chaperone** (signal peptide, no TM, no EEVD, no KDEL, truncated SBD) whose **nucleus, plasma-membrane, and cytosol GO CC annotations are IBA phylogenetic carry-over from cytosolic paralogs with no HSPA13-specific experimental support**. The NKCC2 interaction is an ER-resident/ERAD context and does not demonstrate a cytosolic pool; only cytosolic UbL/BAG6 binding to the ATPase core (a binding assay) leaves a genuine but unproven cytosolic-topology question. **Recommendation: retain/strengthen ER; flag the three secondary pools as paralog carry-over lacking direct support.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)