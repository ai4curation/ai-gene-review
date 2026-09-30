---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-22T14:23:54.428749'
end_time: '2026-08-22T14:35:32.166595'
duration_seconds: 697.74
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: yeast
  gene: SSA3
  gene_symbol: SSA3
  uniprot_accession: P09435
  taxon_id: NCBITaxon:559292
  taxon_label: Saccharomyces cerevisiae
  focus_type: existing_go_annotation_decision
  hypothesis_slug: existing-go-0005886-keep-as-non-core
  hypothesis_text: 'The existing SSA3 GO annotation to plasma membrane (GO:0005886)
    should receive review action KEEP_AS_NON_CORE. Current rationale: The falcon report
    describes Ssa3 as a cytosolic Hsp70 and does not support

    plasma membrane as a site of function. The IBA annotation is retained as a

    low-confidence, non-core localization rather than removed.'
  term_context: '- Term: plasma membrane (GO:0005886)

    - Evidence type: IBA

    - Original reference: GO_REF:0000033

    - Current review action: KEEP_AS_NON_CORE

    - Review summary: Plasma membrane is not a primary site of Ssa3 action. The deep
    research

    consistently localizes Ssa3 to the cytosol; any plasma-membrane

    association would be transient/peripheral (e.g. via translocation or

    client interactions). Kept as non-core.

    - Review reason: The falcon report describes Ssa3 as a cytosolic Hsp70 and does
    not support

    plasma membrane as a site of function. The IBA annotation is retained as a

    low-confidence, non-core localization rather than removed.'
  reference_context: '- GO_REF:0000033

    - file:yeast/SSA3/SSA3-deep-research-falcon.md'
  source_file: genes/yeast/SSA3/SSA3-ai-review.yaml
  source_selector: existing_annotations[3]
  source_context_yaml: "term:\n  id: GO:0005886\n  label: plasma membrane\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033\nreview:\n  summary: |-\n    Plasma\
    \ membrane is not a primary site of Ssa3 action. The deep research\n    consistently\
    \ localizes Ssa3 to the cytosol; any plasma-membrane\n    association would be\
    \ transient/peripheral (e.g. via translocation or\n    client interactions). Kept\
    \ as non-core.\n  action: KEEP_AS_NON_CORE\n  reason: |-\n    The falcon report\
    \ describes Ssa3 as a cytosolic Hsp70 and does not support\n    plasma membrane\
    \ as a site of function. The IBA annotation is retained as a\n    low-confidence,\
    \ non-core localization rather than removed.\n  supported_by:\n  - reference_id:\
    \ file:yeast/SSA3/SSA3-deep-research-falcon.md\n    supporting_text: SSA3 is consistently\
    \ treated as a **cytosolic** Hsp70 of the Ssa family\n    reference_section_type:\
    \ OTHER"
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

- **Organism code:** yeast
- **Taxon:** Saccharomyces cerevisiae (NCBITaxon:559292)
- **Gene directory:** SSA3
- **Gene symbol:** SSA3
- **UniProt accession:** P09435

## Focus

- **Focus type:** existing_go_annotation_decision
- **Hypothesis slug:** existing-go-0005886-keep-as-non-core
- **Source file:** genes/yeast/SSA3/SSA3-ai-review.yaml
- **Source selector:** existing_annotations[3]

## Seed Hypothesis

The existing SSA3 GO annotation to plasma membrane (GO:0005886) should receive review action KEEP_AS_NON_CORE. Current rationale: The falcon report describes Ssa3 as a cytosolic Hsp70 and does not support
plasma membrane as a site of function. The IBA annotation is retained as a
low-confidence, non-core localization rather than removed.

## Term and Decision Context

- Term: plasma membrane (GO:0005886)
- Evidence type: IBA
- Original reference: GO_REF:0000033
- Current review action: KEEP_AS_NON_CORE
- Review summary: Plasma membrane is not a primary site of Ssa3 action. The deep research
consistently localizes Ssa3 to the cytosol; any plasma-membrane
association would be transient/peripheral (e.g. via translocation or
client interactions). Kept as non-core.
- Review reason: The falcon report describes Ssa3 as a cytosolic Hsp70 and does not support
plasma membrane as a site of function. The IBA annotation is retained as a
low-confidence, non-core localization rather than removed.

## Reference Context

- GO_REF:0000033
- file:yeast/SSA3/SSA3-deep-research-falcon.md

## Source Context YAML

```yaml
term:
  id: GO:0005886
  label: plasma membrane
evidence_type: IBA
original_reference_id: GO_REF:0000033
review:
  summary: |-
    Plasma membrane is not a primary site of Ssa3 action. The deep research
    consistently localizes Ssa3 to the cytosol; any plasma-membrane
    association would be transient/peripheral (e.g. via translocation or
    client interactions). Kept as non-core.
  action: KEEP_AS_NON_CORE
  reason: |-
    The falcon report describes Ssa3 as a cytosolic Hsp70 and does not support
    plasma membrane as a site of function. The IBA annotation is retained as a
    low-confidence, non-core localization rather than removed.
  supported_by:
  - reference_id: file:yeast/SSA3/SSA3-deep-research-falcon.md
    supporting_text: SSA3 is consistently treated as a **cytosolic** Hsp70 of the Ssa family
    reference_section_type: OTHER
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

# SSA3 (P09435) — Plasma Membrane GO:0005886 Annotation Review

**Hypothesis under review:** The existing SSA3 IBA annotation to *plasma membrane* (GO:0005886) should receive review action **KEEP_AS_NON_CORE**.

**Focus type:** existing_go_annotation_decision · **Source:** `genes/yeast/SSA3/SSA3-ai-review.yaml` → `existing_annotations[3]` · **Organism:** *Saccharomyces cerevisiae* (NCBITaxon:559292)

---

## Summary

The seed action **KEEP_AS_NON_CORE** is well justified in spirit: the plasma membrane is **not** a primary or core site of Ssa3 function. Every line of curated and experimental evidence localizes Ssa3 — a stress-inducible cytosolic Hsp70 of the Ssa family — to the **cytosol/cytoplasm**. The plasma-membrane assignment is a **phylogenetic (IBA) inference only**, carried on GO_REF:0000033, with no yeast-specific experimental support for Ssa3. Ssa3 also has **no transmembrane domain, signal peptide, or lipidation site**, so it possesses no intrinsic mechanism to reside in or anchor to a membrane.

One material fact tilts the practical decision toward **REMOVE** rather than merely keeping the term as non-core: a live check of GO_Central via QuickGO shows that the plasma-membrane annotation for P09435 **no longer exists** (`GO:0005886` on P09435 → 0 hits), even though the UniProt cross-reference dump still lists it as a synchronization-lag artifact. Because the authoritative source has already retired this IBA, "keep as non-core" retains an annotation that upstream curation has already dropped. Both KEEP_AS_NON_CORE and REMOVE are curatorially reasonable and agree on the essential biology; REMOVE is now better aligned with the source of truth and with the paralog-over-annotation mechanism that produced the term.

A paralog audit explains where the family-level plasma-membrane signal actually comes from. The constitutive paralogs **Ssa1 and Ssa2** were detected in a whole-cell *S. cerevisiae* plasma-membrane proteome (HDA, Delom et al. 2006, [PMID:16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/)) — a low-specificity context in which highly abundant cytosolic Hsp70 readily co-purifies with a membrane fraction. Ssa3 was **not** detected and now carries no PM annotation. Combined with mammalian Hsp70 orthologs that have genuine experimental cell-surface localization, this is the ancestral-node source from which the (now-retired) IBA leaked onto the low-abundance, stress-inducible Ssa3/Ssa4. The verdict is therefore **partially supported**: the biological conclusion is correct, but the chosen action is weaker than the evidence warrants.

---

## Executive Judgment

**Verdict: Partially supported (KEEP_AS_NON_CORE is a defensible conservative action; REMOVE is the stronger, evidence-aligned alternative).**

The core claim of the seed hypothesis — that plasma membrane is not a primary site of Ssa3 action — is **correct and well supported**. The weakness lies in the chosen mechanism: retaining an IBA that (1) has no Ssa3-specific experimental support, (2) is a paralog/cross-organism over-propagation artifact, and (3) has already been retired at GO_Central. The most important caveat is that this is a **localization nuance, not a functional error**, and that transient/peripheral membrane association by a cytosolic Hsp70 during client handling cannot be formally excluded — it is simply undocumented for Ssa3.

### Paralog audit (QuickGO live, GO:0005886)

| Protein | Accession | Expression | GO:0005886 status | Evidence / source |
|---|---|---|---|---|
| Ssa1 | P10591 | constitutive | present | **HDA** (ECO:0007005), PMID:16622836 (Delom 2006, PM proteome), SGD |
| Ssa2 | P10592 | constitutive | present | **HDA** (ECO:0007005), PMID:16622836, SGD |
| **Ssa3** | **P09435** | **stress-inducible** | **absent (0 hits)** | IBA retired at GO_Central |
| Ssa4 | P22202 | stress-inducible | absent (0 hits) | — |
| HSC70/HSPA8 (human) | P11142 | — | present | IEA + TAS (Reactome) |

Interpretation: the ancestral Hsp70 node inherits PM from Ssa1/Ssa2 (HDA) and mammalian Hsp70s, which is how the now-retired **IBA** leaked onto the low-abundance, stress-inducible Ssa3/Ssa4 — neither of which was detected in the PM proteome.

---

## Key Findings

### F001 — The plasma-membrane annotation is IBA-only, unsupported by yeast experimental evidence, and already retired at GO_Central

A direct audit of UniProt and QuickGO records for P09435 shows the plasma-membrane assignment never had experimental backing for Ssa3. UniProt's curated `SUBCELLULAR LOCATION` comment lists **Cytoplasm only**, and the keyword set includes **Cytoplasm** with **no membrane keyword**. The cellular-component GO annotations in UniProt were: GO:0005737 cytoplasm (IBA), GO:0005829 cytosol (**IDA:SGD, PMID:10745074** — the only experimental CC record), GO:0005634 nucleus (IBA), and GO:0005886 plasma membrane (**IBA:GO_Central**).

When queried against the live QuickGO annotation service, P09435 returns five current CC-aspect records: cytoplasm (IBA), cytosol (IBA), nucleus (IBA), cytoplasm (IEA, GO_REF:0000120), and cytosol (IDA, ECO:0000314, PMID:10745074). A targeted query for **GO:0005886 on P09435 returns `numberOfHits = 0`** — the plasma-membrane IBA is **no longer present** in GO_Central. The term originated purely as a phylogenetic inference whose ancestral `withFrom` set includes mammalian Hsp70s carrying experimental cell-surface / PM localization — HSC70/HSPA8 (P11142), HSPA1A/B (P0DMV8 / P0DMV9), HSPA6 (P17066), and HSPA1L (P34931). None of these are direct evidence for the yeast Ssa3 protein. This is the single most decision-relevant fact for the curator: the annotation being "kept" may no longer exist upstream.

### F002 — The Ssa-family plasma-membrane signal traces to one PM proteomics study on the constitutive paralogs Ssa1/Ssa2, not Ssa3

To identify the true origin of the family-level signal, each Ssa paralog was audited in QuickGO for GO:0005886 (see paralog table above). Only Ssa1 (P10591) and Ssa2 (P10592) carry the term, each with a single **HDA** (ECO:0007005) record from **PMID:16622836** (Delom, Szponarski, Sommerer, Boyer, *Proteomics* 2006, *"The plasma membrane proteome of Saccharomyces cerevisiae and its response to the antifungal calcofluor"*). Ssa3 and Ssa4 return **0 hits**. The two annotated paralogs are among the most abundant cytosolic proteins in yeast, and their detection in a plasma-membrane-enriched fraction is readily explained as low-specificity co-purification rather than bona fide PM residence. Human HSC70/HSPA8 additionally carries GO:0005886 via IEA and TAS (Reactome). The Ssa3 phylogenetic ancestral node would inherit plasma membrane from the Ssa1/Ssa2 HDA evidence **and** from the mammalian Hsp70s, producing the (now-retired) IBA on Ssa3/Ssa4 despite no direct observation. This is a textbook **paralog over-annotation** pattern.

### F003 — Ssa3 has no membrane-targeting sequence features; its sole experimental localization is cytosolic

An independent sequence-level check confirms no biophysical basis for a plasma-membrane residence. A UniProt feature audit of P09435 returns feature types limited to `{Chain:1, Region:1, Compositional bias:1, Sequence conflict:1}` — with **no transmembrane segment, no signal peptide, and no lipidation site**. Consistent with this, the only experimental CC annotation for Ssa3 (GO:0005829 cytosol, IDA, ECO:0000314) derives from **PMID:10745074** (Satyanarayana, Schröder-Köhne, Craig, Schu, *FEBS Letters* 2000, *"Cytosolic Hsp70s are involved in the transport of aminopeptidase 1 from the cytoplasm into the vacuole"*), a study that explicitly treats the Ssa Hsp70s as cytosolic chaperones. Absence of membrane-targeting features plus positive cytosolic evidence closes the loop: any plasma-membrane association, if it occurs, would be transient/peripheral, not a stable localization or a dedicated site of function.

---

## Mechanistic Model / Interpretation

```
  EXPERIMENTAL REALITY (yeast)                 ANNOTATION PROPAGATION PATH
  ---------------------------                  ---------------------------
  Ssa1/Ssa2 (constitutive, abundant)  ──HDA──▶ GO:0005886 PM  (PMID:16622836)
        │                                            │
        │ high cytosolic abundance                   │ phylogenetic tree
        │ co-fractionates w/ PM prep                 ▼ (IBA, GO_REF:0000033)
        │                              Ancestral Hsp70 node inherits PM
  Mammalian HSC70/HSPA1 etc. ──exp──▶  (also from mammalian cell-surface Hsp70s)
                                                     │
                                                     ▼  over-propagation
                                        Ssa3 (P09435) IBA GO:0005886  ← REVIEW TARGET
                                                     │
                                                     ▼  GO_Central re-curation
                                        RETIRED (QuickGO: 0 hits today)

  Ssa3 DIRECT EVIDENCE:
     • Cytosol IDA (PMID:10745074)          ← only experimental CC
     • Cytoplasm (UniProt curated comment)
     • No TM / signal peptide / lipidation  ← no membrane-targeting features
```

Ssa3 is a stress-inducible cytosolic Hsp70 whose documented molecular activities — chaperoning Hsp90 clients (PMID:32299842), regulating ribonucleotide reductase via its C-terminal domain (PMID:35417483), promoting autophagic degradation of toxic aggregates (PMID:30376576), and prion propagation / thermotolerance (PMID:24628813) — are all **cytosolic/nuclear**. None require or imply a plasma-membrane site of action. The plasma-membrane term is therefore best understood as an annotation-provenance artifact rather than a reflection of Ssa3 cell biology.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt P09435 (curated CC comment) | Review/database | Refutes PM as core | Where is Ssa3 localized? | Curated SUBCELLULAR LOCATION = **Cytoplasm** only; keyword "Cytoplasm"; no membrane keyword | *S. cerevisiae* | High for cytosol; DB-level |
| [PMID:10745074](https://pubmed.ncbi.nlm.nih.gov/10745074/) (Satyanarayana 2000; SGD IDA, GO:0005829) | Localization (direct assay) | Supports cytosol; refutes PM as primary | Experimental localization | Only **experimental** CC annotation = **cytosol** (ECO:0000314, IDA); "Cytosolic Hsp70s… transport of aminopeptidase 1 from the cytoplasm into the vacuole" | *S. cerevisiae* | Moderate-high; single experimental CC record |
| UniProt P09435 sequence features | Structural/sequence | Refutes PM residence mechanism | Any membrane-anchoring signal? | **No** transmembrane, signal-peptide, or lipidation features — soluble protein with no PM-targeting mechanism | *S. cerevisiae* | High; absence-of-feature argument |
| GO_Central IBA GO:0005886 (GO_REF:0000033) | Computational (phylogenetic) | The annotation being reviewed | Is PM directly evidenced? | PM assigned by **IBA only**; ancestral withFrom includes mammalian Hsp70s (P11142; P0DMV8/9; P17066; P34931) with experimental cell-surface localization | Phylogenetic node | Low; inference, not yeast data |
| QuickGO live query (2026-08) | Database status | Qualifies/strengthens removal | Does PM IBA still exist? | Direct query `P09435 + GO:0005886` → **0 hits**; annotation retired at GO_Central | GO_Central | High; live check |
| [PMID:16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/) (Delom 2006; HDA on Ssa1 & Ssa2) | Localization (HT proteomics) | Qualifies (family-level, not Ssa3) | Any yeast PM evidence for the Ssa family? | Constitutive Ssa1/Ssa2 detected in PM proteome; **Ssa3 not detected** | *S. cerevisiae* PM fraction | Low specificity; abundant chaperone in membrane prep is contamination-prone |
| [PMID:24628813](https://pubmed.ncbi.nlm.nih.gov/24628813/) (Hasin 2014) | Mutant phenotype / expression | Supports cytosolic function | Ssa3 functional role | Ssa1–4 are "cytosolic Hsp70-Ssa family"; Ssa3 stress-inducible, most proficient for [PSI+] prion | *S. cerevisiae* | High; cytosolic context |
| [PMID:35417483](https://pubmed.ncbi.nlm.nih.gov/35417483/) (Knighton 2022) | Mutant phenotype / interaction | Supports cytosolic function | Ssa3 role & identity | "four highly similar **cytosolic** Hsp70s Ssa1,2,3,4… Ssa3 and 4 induced upon heat shock"; regulate RNR | *S. cerevisiae* | High |
| [PMID:32299842](https://pubmed.ncbi.nlm.nih.gov/32299842/) (Gaur 2020) | Interaction / phenotype | Supports cytosolic function | Ssa3 in Hsp90 pathway | Ssa3 acts as cytosolic Hsp70 modulating Hsp90 client (v-Src) maturation | *S. cerevisiae* | High |
| [PMID:30376576](https://pubmed.ncbi.nlm.nih.gov/30376576/) (Gupta 2018) | Mutant phenotype | Supports cytosolic function | Ssa3 protective role | Stress-inducible Ssa3/4 reduce α-synuclein toxicity via autophagy; treated as cytosolic Hsp70 | *S. cerevisiae* | High |

---

## Evidence Base (literature synthesis)

The functional literature is unanimous that Ssa3 is a **cytosolic** Hsp70 and never invokes a plasma-membrane role. [PMID:35417483](https://pubmed.ncbi.nlm.nih.gov/35417483/) states directly that budding yeast "express four highly similar cytosolic Hsp70s Ssa1, 2, 3 and 4," with Ssa3/4 induced on heat shock, and assigns Ssa3 a role in regulating ribonucleotide reductase (a cytosolic/nuclear process) via its C-terminal domain. [PMID:24628813](https://pubmed.ncbi.nlm.nih.gov/24628813/) characterizes the Ssa isoforms as "the cytosolic Hsp70-Ssa family" and finds Ssa3 most proficient for [PSI+] prion propagation — again a cytosolic function. [PMID:32299842](https://pubmed.ncbi.nlm.nih.gov/32299842/) places Ssa3 in the cytosolic Hsp90 client-maturation pathway (v-Src), and [PMID:30376576](https://pubmed.ncbi.nlm.nih.gov/30376576/) shows stress-inducible Ssa3/4 reduce α-synuclein toxicity via autophagy. The only two localization-relevant primary sources are [PMID:10745074](https://pubmed.ncbi.nlm.nih.gov/10745074/) (Ssa3 cytosol, IDA — supports the core CC) and [PMID:16622836](https://pubmed.ncbi.nlm.nih.gov/16622836/) (PM proteome detecting only Ssa1/Ssa2 — the qualifying, family-level source of the propagated PM term). No primary study documents Ssa3 at the plasma membrane.

---

## GO Curation Implications

- **Aspect:** Cellular Component (CC). Term = plasma membrane (GO:0005886), evidence IBA, ref GO_REF:0000033.
- **Primary lead — REMOVE** the plasma-membrane IBA for SSA3. Rationale: (1) no yeast experimental support; (2) contradicted in emphasis by the only experimental CC annotation (cytosol, IDA, PMID:10745074) and the UniProt curated location (Cytoplasm); (3) it is an ancestral-node over-propagation from mammalian Hsp70 paralogs plus the constitutive Ssa1/Ssa2 HDA; (4) **GO_Central has already retired it** (QuickGO returns 0 hits), so removal restores consistency with the authoritative source.
- **Acceptable fallback — KEEP_AS_NON_CORE** (the seed action) if the curator prefers to preserve a low-confidence peripheral-association possibility. This is defensible but effectively re-instates an annotation the source has dropped.
- **Retain as core:** GO:0005829 cytosol (IDA) and GO:0005737 cytoplasm — these are the supported CC terms. Do **not** upgrade or make PM more specific; there is no evidence for a specific membrane subdomain.

### GO decision table (leads — require curator verification)

| GO term | Aspect | Current evidence for Ssa3 | Recommended action | Confidence |
|---|---|---|---|---|
| GO:0005886 plasma membrane | CC | IBA only (retired at GO_Central; 0 hits); no Ssa3 experimental data; no TM/signal/lipid | **REMOVE** (or KEEP_AS_NON_CORE as conservative fallback) | High that PM is non-core |
| GO:0005829 cytosol | CC | IDA (PMID:10745074, ECO:0000314) + IBA | **RETAIN as core** | High |
| GO:0005737 cytoplasm | CC | IBA + IEA; curated UniProt location | Retain (parent of cytosol) | High |
| GO:0005634 nucleus | CC | IBA | Retain as non-core (plausible for Hsp70 clients/DDR) | Moderate |

---

## Mechanistic Scope

Ssa3 has **no transmembrane domain, signal peptide, or lipidation site** in UniProt (P09435) — i.e., no intrinsic mechanism to reside in or anchor to the plasma membrane, reinforcing that any PM detection is peripheral/adventitious. The immediate molecular function of Ssa3 is ATP-dependent Hsp70 chaperone activity in the **cytosol** (holdase/foldase for misfolded and nascent clients; partner to Hsp90 and J-domain co-chaperones Ydj1/Sis1; nucleotide-exchange-regulated client binding/release). Its documented cellular processes — prion propagation, protein-aggregate/α-synuclein clearance, RNR regulation, Hsp90 client maturation, thermotolerance — all occur in the cytosol/nucleus. No direct membrane-anchoring, transmembrane, or lipid-binding activity is annotated. Any plasma-membrane presence would be a **transient, peripheral** consequence of client handling or translocation, i.e., downstream of the core cytosolic chaperone role — not an intrinsic localization.

---

## Conflicts and Alternatives

- **Paralog over-annotation (most likely explanation):** The Hsp70 ancestral node inherits plasma membrane from two sources — the yeast constitutive paralogs Ssa1/Ssa2 (HDA, PMID:16622836) and mammalian Hsp70s with experimental cell-surface localization. Phylogenetic propagation carried "plasma membrane" onto the stress-inducible Ssa3/Ssa4 as IBA, even though neither was detected in the yeast PM proteome. GO_Central has since retired the Ssa3/Ssa4 IBA while retaining the HDA calls on Ssa1/Ssa2.
- **High-throughput artifact (why even the Ssa1/Ssa2 HDA is weak):** Ssa1/Ssa2 are among the most abundant cytosolic proteins; their appearance in a plasma-membrane preparation is a classic low-specificity co-purification and does not establish bona fide PM residence, further undermining any inference that Ssa3 functions at the PM.
- **Database carry-over:** UniProt still lists the GO:0005886 IBA cross-reference while GO_Central has dropped it — a synchronization lag, not new evidence. Curators should treat the QuickGO live status as authoritative.
- **Not excluded:** Genuine transient membrane association during co-translational translocation or client delivery is biologically plausible for cytosolic Hsp70s but is unproven for Ssa3 specifically.

---

## Limitations and Knowledge Gaps

1. **Is there any yeast experimental PM/cell-surface evidence for Ssa3?** Checked UniProt, QuickGO, and PubMed — none found. Matters because it is the sole basis that could justify keeping the term. Resolve with a targeted GFP/immuno-EM or surface-biotinylation study of tagged Ssa3.
2. **Identity/robustness of the cytosol IDA (PMID:10745074).** Verified it exists as the single experimental CC record; did not read the full paper. Matters for weighting cytosol as core. Resolve by confirming the assay (likely fractionation/localization).
3. **Exact GO_Central removal history.** QuickGO shows 0 hits now; the removal date/reason was not retrieved. Matters for justifying REMOVE vs KEEP. Resolve via GO annotation change logs.
4. **Delom 2006 peptide-level specificity.** Because Ssa paralogs share extensive sequence identity, I did not confirm from the raw peptide tables whether Ssa1/Ssa2 assignments rest on paralog-discriminating peptides. This bears on how confidently Ssa3 can be called "absent" from the PM proteome.

---

## Discriminating Tests / Proposed Follow-up Actions

- **Localization:** High-resolution live-cell imaging (endogenously tagged GFP-Ssa3) ± heat shock, with a PM marker (e.g., Pma1-mCherry), plus cell-surface biotinylation/flow cytometry to test for any surface pool. Expected: diffuse cytosolic signal, no PM enrichment.
- **Fractionation:** Sucrose-gradient / membrane-vs-cytosol fractionation of induced Ssa3 (heat shock), with protease-protection to distinguish peripheral from integral association. Expected: fully soluble/peripheral.
- **Comparative annotation audit:** Confirm whether Ssa1 (P10591), Ssa2 (P10592), and Ssa4 (P22202) still carry GO:0005886; consistent removal across the stress-inducible paralogs confirms the over-propagation interpretation.
- **Provenance check:** Compare the GO release used to build the AIGR review against current GO_Central to determine whether the action is "remove" or "confirm already-removed."

---

## Curation Leads (require curator verification)

- **Candidate action change:** `KEEP_AS_NON_CORE` → **`REMOVE`** for GO:0005886 (IBA, GO_REF:0000033), justified by absence of yeast evidence and confirmed retirement at GO_Central. If the curator prefers maximum conservatism, retain the seed `KEEP_AS_NON_CORE` with an explicit note that the term is IBA-only and source-retired.
- **Candidate references / snippets to verify:**
  - UniProt P09435: curated `SUBCELLULAR LOCATION: Cytoplasm`; CC GO includes `GO:0005829 cytosol | IDA:SGD` and `GO:0005886 plasma membrane | IBA:GO_Central`.
  - QuickGO live: `GET annotation/search?geneProductId=P09435&goId=GO:0005886` → `numberOfHits = 0`.
  - PMID:16622836 — *"The plasma membrane proteome of Saccharomyces cerevisiae and its response to the antifungal calcofluor"* (supports only Ssa1/Ssa2 at the PM).
  - PMID:10745074 — *"Cytosolic Hsp70s are involved in the transport of aminopeptidase 1 from the cytoplasm into the vacuole"* (supports cytosol as core CC).
  - PMID:35417483 — "cells express four highly similar cytosolic Hsp70s Ssa1, 2, 3 and 4… Ssa3 and 4 are induced upon heat shock."
- **Suggested curator questions:** (1) Should source-retired IBA terms be removed rather than downgraded? (2) Is there any organism-specific PM evidence justifying retention?
- **Suggested experiment:** Surface-biotinylation + fractionation of induced GFP-Ssa3 to settle the peripheral-association question.

---

*Analyses executed live against UniProt REST and EBI QuickGO on 2026-08-22; PubMed evidence as cited. Computational results reported conservatively; direct database queries distinguished from phylogenetic inference.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)