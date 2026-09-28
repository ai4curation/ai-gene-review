---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T17:45:40.218013'
end_time: '2026-09-20T18:00:55.103431'
duration_seconds: 914.89
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: RIMBP2
  gene_symbol: RIMBP2
  uniprot_accession: O15034
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0007274
  hypothesis_text: Human RIMBP2 participates in neuromuscular synaptic transmission
    (GO:0007274). Evaluate direct evidence and phylogenetically justified inference,
    including ortholog and paralog specificity. A role at additional synapse types
    neither establishes nor excludes this function. Read the current GO definition
    and distinguish evidence against this hypothesis from experiments not yet performed.
  term_context: '- Term: neuromuscular synaptic transmission (GO:0007274)'
  reference_context: No specific reference context supplied.
  source_file: genes/human/RIMBP2/RIMBP2-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human RIMBP2 participates in neuromuscular synaptic\
    \ transmission (GO:0007274). Evaluate direct\n  evidence and phylogenetically\
    \ justified inference, including ortholog and paralog specificity. A role\n  at\
    \ additional synapse types neither establishes nor excludes this function. Read\
    \ the current GO definition\n  and distinguish evidence against this hypothesis\
    \ from experiments not yet performed.\nfocus_type: function_assignment\nterm_id:\
    \ GO:0007274\nterm_label: neuromuscular synaptic transmission\ncontext: []\nreference_id:\
    \ []"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: rimbp2_go0007274_evidence_matrix.csv
  path: openscientist_artifacts/rimbp2_go0007274_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist rimbp2 go0007274 evidence matrix
- filename: rimbp2_go_decision_table.csv
  path: openscientist_artifacts/rimbp2_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist rimbp2 go decision table
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
- **Gene directory:** RIMBP2
- **Gene symbol:** RIMBP2
- **UniProt accession:** O15034

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0007274
- **Source file:** genes/human/RIMBP2/RIMBP2-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human RIMBP2 participates in neuromuscular synaptic transmission (GO:0007274). Evaluate direct evidence and phylogenetically justified inference, including ortholog and paralog specificity. A role at additional synapse types neither establishes nor excludes this function. Read the current GO definition and distinguish evidence against this hypothesis from experiments not yet performed.

## Term and Decision Context

- Term: neuromuscular synaptic transmission (GO:0007274)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human RIMBP2 participates in neuromuscular synaptic transmission (GO:0007274). Evaluate direct
  evidence and phylogenetically justified inference, including ortholog and paralog specificity. A role
  at additional synapse types neither establishes nor excludes this function. Read the current GO definition
  and distinguish evidence against this hypothesis from experiments not yet performed.
focus_type: function_assignment
term_id: GO:0007274
term_label: neuromuscular synaptic transmission
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

# AIGR Gene Hypothesis Deep Research — RIMBP2 and Neuromuscular Synaptic Transmission (GO:0007274)

**Gene:** RIMBP2 (RIM-binding protein 2) · **Organism:** *Homo sapiens* (NCBITaxon:9606) · **UniProt:** O15034
**Focus:** function_assignment · **Term under evaluation:** GO:0007274 — *neuromuscular synaptic transmission*
**Hypothesis slug:** function-hypothesis-go-0007274

---

## Executive Judgment

**Verdict: Weakly / indirectly supported for human — unresolved and over-specific as a direct annotation (over-annotation risk).**

A direct GO:0007274 (*neuromuscular synaptic transmission*) annotation for human RIMBP2 is **not supported by any human or mammalian primary evidence** and, if applied to the human gene, would constitute over-annotation. Every primary mammalian study of RIMBP2 localizes and functionally tests the protein at **central synapses** (calyx of Held, hippocampus) and **sensory ribbon synapses** (cochlear inner hair cells) — not at the cholinergic vertebrate neuromuscular junction (NMJ). The single source of direct GO:0007274 evidence in the entire RIM-BP family is the **Drosophila ortholog Rbp**, annotated by FlyBase from a mutant phenotype (IMP) at the glutamatergic fly NMJ ([PMID: 22174254](https://pubmed.ncbi.nlm.nih.gov/22174254/)).

The seed hypothesis correctly instructs us to distinguish *evidence against* the hypothesis from *experiments not yet performed*. Applying that distinction: there is **no experiment refuting** a mammalian NMJ role for RIMBP2 — such an experiment simply has **not been done**. RIMBP2's molecular architecture (a generic presynaptic active-zone adaptor linking RIMs and voltage-gated Ca²⁺ channels) is compatible in principle with a role at any fast chemical synapse, including the NMJ. Thus the hypothesis is **weakly supported by phylogenetic inference** (orthology to fly Rbp) but is **unresolved for the human protein** and, critically, is **too specific** to be applied directly. The demonstrated mammalian function is better captured by general active-zone / Ca²⁺-channel-coupling terms, which is exactly what the current GO record does (it assigns GO:0150037, *regulation of calcium-dependent activation of synaptic vesicle fusion*, not GO:0007274).

**Most important caveat for curators:** absence of an NMJ annotation on human RIMBP2 reflects (a) a genuine gap in vertebrate NMJ experiments and (b) the fact that the fly IMP evidence is organism-specific and should not be transferred by orthology into a term whose definition ("synaptic transmission from a neuron to a muscle") has never been experimentally satisfied in a mammal. The correct curation posture is to **retain the general/central-synapse framing** and **not add GO:0007274** to O15034 unless a vertebrate NMJ experiment appears.

---

## Summary

RIMBP2 (RIM-binding protein 2, UniProt O15034) is a multidomain scaffolding protein of the presynaptic **active zone (AZ)**. Its canonical architecture — three SH3 domains and three fibronectin type-III (FN3) domains (InterPro family IPR040325, shared with RIMBP1/TSPOAP1 and RIMBP3) — enables it to act as a **bifunctional molecular linker** that simultaneously binds Rab3-interacting molecules (RIMS1/RIMS2) and voltage-gated Ca²⁺ channels (CACNA1D, CACNA1B), thereby positioning Ca²⁺ channels near the synaptic vesicle release machinery. This coupling function is the protein's demonstrated core activity.

The hypothesis under review asks whether human RIMBP2 participates specifically in **neuromuscular synaptic transmission** (GO:0007274), a Biological Process term whose GO definition is narrow: "The process of synaptic transmission from a neuron to a muscle, across a synapse." Our investigation traced the provenance of any GO:0007274 signal in the RIM-BP family and found it originates **entirely** from *Drosophila melanogaster* Rbp, annotated with a direct mutant-phenotype evidence code (IMP) at the fly glutamatergic NMJ. No human, mouse, or other mammalian RIM-BP family member carries GO:0007274 in QuickGO; among 31 human and 65 mouse gene products annotated to GO:0007274, **none** is a RIM-BP-family protein. Human RIMBP2's own GO annotation set (6 terms) contains **no** GO:0007274, and its only IBA (phylogenetically inferred) biological-process term is the more general GO:0150037.

Consistent with a central-nervous-system rather than neuromuscular role, the primary mammalian literature places RIMBP2 at the calyx of Held, cultured hippocampal neurons, and cochlear inner-hair-cell ribbon synapses, where loss-of-function selectively degrades the fidelity of Ca²⁺-influx-to-exocytosis coupling rather than abolishing release outright. Expression data reinforce this: Human Protein Atlas shows RIMBP2 RNA is "tissue enhanced" in brain and neuroendocrine tissues (pituitary, parathyroid), with skeletal muscle **not** among enhanced tissues. Taken together, the evidence supports curating RIMBP2 with **general active-zone / Ca²⁺-channel-coupling terms** and treating a direct human GO:0007274 assignment as **over-specific and unsupported**, while acknowledging that a vertebrate NMJ role remains formally untested rather than disproven.

---

## Key Findings

### Finding 1 — The only direct GO:0007274 evidence in the RIM-BP family belongs to *Drosophila* Rbp, not human RIMBP2

A QuickGO annotation search establishes the provenance of the neuromuscular-transmission term precisely. *Drosophila melanogaster* Rbp is annotated to **GO:0007274** with evidence code **IMP** (inferred from mutant phenotype — a direct, experiment-backed code), citing reference [PMID: 22174254](https://pubmed.ncbi.nlm.nih.gov/22174254/) and assigned by FlyBase. This is a bona fide, high-quality annotation reflecting the well-documented role of Rbp at the *Drosophila* glutamatergic NMJ, a favored genetic model of synaptic release.

By contrast, human RIMBP2 (O15034) carries **6 GO annotations, none of which is GO:0007274**. Its only IBA (Inferred from Biological ancestor / phylogenetic) biological-process term is **GO:0150037** — *regulation of calcium-dependent activation of synaptic vesicle fusion* — a term that is both mechanistically accurate and appropriately general (synapse-type-agnostic). The GO definition of the disputed term (QuickGO) is explicitly muscle-directed: *"The process of synaptic transmission from a neuron to a muscle, across a synapse."*

The curation significance is that GO:0007274 is a **process term tied to a specific synapse type** (neuron→muscle). Transferring it to the human protein by orthology would import an organism-specific phenotype into a definitional context (the vertebrate NMJ) that has never been experimentally examined for RIMBP2. This is the central over-annotation risk flagged by the hypothesis.

### Finding 2 — Mammalian RIMBP2 is characterized at central and ribbon synapses, never at the NMJ

A systematic reading of the primary mammalian loss-of-function and localization literature shows a consistent picture: RIMBP2 has been studied at **central synapses** and **sensory ribbon synapses**, and at no point at the cholinergic vertebrate neuromuscular junction.

- **Calyx of Held and cultured hippocampal neurons:** Acuna et al. 2015 studied a RIM-BP1/2 double conditional knockout ([PMID: 26402606](https://pubmed.ncbi.nlm.nih.gov/26402606/)). Two verbatim findings anchor this: first, the paper notes that *"In Drosophila, deletion of RIM-BPs dramatically reduces neurotransmitter release, but little is known about RIM-BP function in mammalian synapses"* — directly flagging the ortholog-context gap. Second, it establishes the mammalian phenotype: *"we find that in murine synapses, RIM-BPs are not essential for neurotransmitter release as such, but are selectively required for high-fidelity coupling of action potential-induced Ca(2+) influx to Ca(2+)-stimulated synaptic vesicle exocytosis."* This is a **qualitatively different** phenotype from the fly NMJ (where release collapses), and it is measured at central synapses.
- **Hippocampal synapses:** Grauel et al. 2016 ([PMID: 27671655](https://pubmed.ncbi.nlm.nih.gov/27671655/)) show RIMBP2 fine-tunes release probability by positioning Ca²⁺ channels.
- **Calyx of Held AZ organization:** Butola et al. 2021 ([PMID: 34353898](https://pubmed.ncbi.nlm.nih.gov/34353898/)) and Miyano et al. 2024 ([PMID: 38329474](https://pubmed.ncbi.nlm.nih.gov/38329474/)) address AZ nano-organization and Ca²⁺-channel recruitment.
- **Cochlear inner-hair-cell ribbon synapses:** Krinner et al. 2017 ([PMID: 29163046](https://pubmed.ncbi.nlm.nih.gov/29163046/)) and 2021 ([PMID: 33867935](https://pubmed.ncbi.nlm.nih.gov/33867935/)) show RIM-BP2 promotes a large number of Ca²⁺ channels and is required for normal sound encoding.

Across this body of work, **no primary study localizes or functionally tests RIMBP2 at the mammalian NMJ.** This is the empirical basis for classifying the NMJ hypothesis as *untested* rather than *refuted*.

### Finding 3 — Domain architecture and UniProt annotation support a generic active-zone adaptor role, not an NMJ-specific one

UniProt O15034 describes the function generically: *"Plays a role in the synaptic transmission as bifunctional linker that interacts simultaneously with RIMS1, RIMS2, CACNA1D and CACNA1B."* Its subcellular location is **Cell membrane / Synapse**, with **no tissue-specificity or disease comment** tying it to muscle or the NMJ.

The domain architecture is the canonical RIM-BP layout: **3× SH3** (residues 167–234, 848–916, 952–1019) plus **3× FN3** (residues 297–590), belonging to InterPro family **IPR040325 (RIMBP1/2/3)** — the same architecture shared with *Drosophila* Rbp. This shared architecture is precisely why orthology-based inference is tempting, but it is also synapse-type-agnostic: the SH3-Ca²⁺-channel and RIM-binding modules operate at any fast chemical synapse.

Critically, a paralog/ortholog specificity check via QuickGO shows that **neither human paralog** — RIMBP1/TSPOAP1 (O95153) or RIMBP3 (Q9UFD9) — **nor the mouse ortholog Rimbp2 is annotated to GO:0007274.** Among all human (31) and mouse (65) GO:0007274 annotations, **zero** are RIM-BP-family proteins. The neuromuscular term is thus **exclusively** a *Drosophila* annotation within this family, strengthening the conclusion that it is organism-specific rather than a conserved family function that merely lacks a vertebrate label.

### Finding 4 — RIMBP2 expression is brain/neuroendocrine-enhanced, not muscle — consistent with a CNS-synapse role

Human Protein Atlas (queried via API) reports RIMBP2 RNA tissue specificity as **"Tissue enhanced"**, with the highest nTPM values in **brain (18.7), parathyroid gland (21.3), and pituitary gland (27.5)**. RNA single-cell specificity is "Cell type enhanced." **Skeletal muscle is not among the enhanced tissues.** While transcript abundance does not define function, the expression pattern is congruent with the localization literature (central + sensory ribbon synapses) and neuroendocrine secretory contexts, and is not congruent with a primary neuromuscular-junction function. This is corroborating, not decisive, evidence.

---

## Mechanistic Model / Interpretation

RIMBP2's demonstrated molecular function is **spatial coupling of voltage-gated Ca²⁺ channels to the synaptic vesicle release apparatus** at the presynaptic active zone. The mechanistic chain is:

```
   Action potential
        │
        ▼
  Ca²⁺ channels (CACNA1B/CACNA1D)
        │  ← positioned by RIMBP2 (SH3 domains)
        │        │
        │        └── RIMBP2 (3×SH3 + 3×FN3) ── binds ──► RIMS1/RIMS2
        │                                                   │
        ▼                                                   ▼
   Local Ca²⁺ nanodomain  ───────────────►  Vesicle Ca²⁺ sensor → fast fusion
        (tight AP–Ca²⁺–exocytosis coupling; GO:0150037)
```

The key interpretive point is that this coupling function is **synapse-type-agnostic at the molecular level** but has been **experimentally demonstrated only at specific synapse types** in mammals:

| Attribute | *Drosophila* Rbp | Mammalian RIMBP2 (human/mouse) |
|---|---|---|
| Synapse studied | Glutamatergic **NMJ** | Calyx of Held, hippocampus, IHC ribbon synapse |
| Loss-of-function phenotype | Neurotransmitter release **dramatically reduced** | Release **not abolished**; loss of **high-fidelity Ca²⁺–exocytosis coupling** |
| GO:0007274 annotation | **Yes** (IMP, PMID:22174254, FlyBase) | **No** — none in the family |
| General coupling term | — | **GO:0150037** (IBA) |
| Tissue expression | NMJ context | Brain / neuroendocrine enhanced; not muscle |

The divergence between the fly and mammalian phenotypes (release collapse vs. selective loss of coupling fidelity) is itself a reason to be cautious about transferring the fly-specific NMJ annotation: the **quantitative role of RIM-BPs differs between the invertebrate NMJ and vertebrate central synapses**, so even the process semantics are not guaranteed to transfer. The most defensible interpretation is that RIMBP2's **core function is Ca²⁺-channel-to-release-site coupling at the active zone**, and that its participation in any *particular* transmission process (neuromuscular, central, sensory) is a **context-specific instantiation** of that core function — one that is documented for central/ribbon synapses and merely inferred (not demonstrated) for the vertebrate NMJ.

---

## Evidence Matrix

| Citation | Evidence type | Supports / refutes / qualifies / competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 22174254](https://pubmed.ncbi.nlm.nih.gov/22174254/) (via QuickGO/FlyBase) | Mutant phenotype (IMP) / database | **Supports** (orthology only) | Does an RIM-BP-family member function in neuromuscular transmission? | *Drosophila* Rbp is annotated GO:0007274 from mutant phenotype at the fly NMJ | *Drosophila melanogaster*, glutamatergic NMJ | High for fly; **not transferable** to human — organism-specific, invertebrate NMJ |
| [PMID: 26402606](https://pubmed.ncbi.nlm.nih.gov/26402606/) (Acuna 2015) | Mutant phenotype (dcKO) | **Qualifies / competing** | Do mammalian RIM-BPs act like fly Rbp? | Mammalian RIM-BPs are **not essential for release** but required for **high-fidelity Ca²⁺–exocytosis coupling** | Mouse, calyx of Held + hippocampal culture | High; central synapses, **not NMJ**; explicitly notes fly-vs-mammal knowledge gap |
| [PMID: 27671655](https://pubmed.ncbi.nlm.nih.gov/27671655/) (Grauel 2016) | Mutant phenotype / localization | **Qualifies** | Where and how does RIMBP2 act in mammals? | RIMBP2 tunes release probability via Ca²⁺-channel localization | Mouse hippocampal synapses | High; central synapse, not NMJ |
| [PMID: 34353898](https://pubmed.ncbi.nlm.nih.gov/34353898/) (Butola 2021) | Localization / structure-function | **Qualifies** | RIMBP2 role in AZ organization | Organizes Ca²⁺-channel topography at the AZ | Mouse calyx of Held | High; central synapse |
| [PMID: 38329474](https://pubmed.ncbi.nlm.nih.gov/38329474/) (Miyano 2024) | Mutant phenotype / imaging | **Qualifies** | RIMBP2 Ca²⁺-channel recruitment | Regulates Ca²⁺-channel number/coupling | Mouse calyx of Held | High; central synapse |
| [PMID: 29163046](https://pubmed.ncbi.nlm.nih.gov/29163046/) (Krinner 2017) | Mutant phenotype | **Qualifies** | RIMBP2 at sensory synapses | Promotes a large number of Ca²⁺ channels at IHC ribbon synapse | Mouse cochlear inner hair cells | High; ribbon (sensory) synapse, not NMJ |
| [PMID: 33867935](https://pubmed.ncbi.nlm.nih.gov/33867935/) (Krinner 2021) | Mutant phenotype | **Qualifies** | RIM-BP requirement for sound encoding | RIM-BPs required for normal afferent IHC sound encoding | Mouse cochlea | High; sensory synapse |
| [PMID: 31535974](https://pubmed.ncbi.nlm.nih.gov/31535974/) (RIM-BP2 priming) | Mutant phenotype | **Qualifies** | RIMBP2 vesicle priming | RIM-BP2 primes synaptic vesicles / coordinates Ca²⁺ | Central synapse | High; central synapse |
| UniProt O15034 | Review/database | **Qualifies** | Core molecular function | Bifunctional linker: RIMS1/2 + CACNA1D/B; location Synapse; no muscle/NMJ comment | Human, curated | Orientation-level; supports generic AZ role |
| Human Protein Atlas (API) | Computational / expression | **Qualifies** | Tissue distribution | Tissue-enhanced in brain/pituitary/parathyroid; **not** skeletal muscle | Human RNA/scRNA | Corroborating; expression ≠ function |
| QuickGO paralog/ortholog scan | Computational / database | **Refutes (as direct human annotation)** | Is GO:0007274 a conserved family term in vertebrates? | 0/31 human & 0/65 mouse GO:0007274 gene products are RIM-BP family; no mammalian RIM-BP carries the term | Human + mouse | High; establishes term is *Drosophila*-exclusive in family |

---

## GO Curation Implications

**Lead requiring curator verification:** Do **not** add GO:0007274 (*neuromuscular synaptic transmission*) as a direct annotation to human RIMBP2 (O15034). The term is **too specific** for the human protein and is not supported by any human/mammalian experiment.

- **Term type:** GO:0007274 is a **Biological Process (BP)** term. The evidence does **not** support it for human RIMBP2 as a direct or experimentally-backed annotation.
- **Recommended action:** **Do not assign / do not retain** GO:0007274 for O15034. If it exists as an IEA/ISS/IBA carry-over, it should be **removed or generalized**.
- **Preferred alternatives (already present or more informative):**
  - **BP:** Retain **GO:0150037** (*regulation of calcium-dependent activation of synaptic vesicle fusion*, currently IBA) — accurate and synapse-type-agnostic. Consider adding a general AZ / Ca²⁺-channel-clustering process term supported by the mammalian phenotype literature (e.g., regulation of neurotransmitter secretion / synaptic-vesicle-Ca²⁺-channel coupling).
  - **MF:** The bifunctional-linker activity (simultaneous RIMS and Ca²⁺-channel binding) supports specific molecular-function/interaction annotations to **RIMS1/RIMS2** and **CACNA1B/CACNA1D** rather than a bare "protein binding." A structural/adaptor MF term is more informative than protein binding.
  - **CC:** **Presynaptic active zone** / synapse localization is strongly supported (UniProt: Synapse; multiple AZ-organization studies).
- **Bottom line:** Treat GO:0007274 as **non-core and organism-specific** for this gene. The demonstrated core is **active-zone Ca²⁺-channel–release-site coupling**, best captured by general terms.

---

## Mechanistic Scope

The **immediate molecular function** being tested is whether RIMBP2 directly participates in *transmission from a neuron to a muscle*. What is directly demonstrated for the gene product is:

- **Direct activity:** RIMBP2 physically links RIMS1/RIMS2 to CACNA1B/CACNA1D (bifunctional SH3/FN3 adaptor), spatially clustering Ca²⁺ channels at release sites.
- **Direct cellular consequence:** high-fidelity coupling of AP-triggered Ca²⁺ influx to vesicle fusion (demonstrated at central and ribbon synapses).

What is **downstream, inferred, or context-specific** and therefore should not be conflated with the core function:

- **Downstream/phenotypic:** loss of release fidelity, altered short-term plasticity, impaired sound encoding (IHC) — these are *loss-of-function readouts*, not the molecular activity itself.
- **Inferred-only (NMJ):** neuromuscular transmission per se — supported for mammals **only by orthology to fly Rbp**, with no vertebrate NMJ experiment.
- **Not a disease/developmental claim:** UniProt lists no muscle disease or tissue-specificity, so there is no disease-driven basis for an NMJ annotation.

The NMJ hypothesis therefore tests a **context-specific instantiation** of a general coupling function, and the evidence establishes the general function while leaving the specific NMJ instantiation untested.

---

## Conflicts and Alternatives

1. **Paralog/ortholog confusion (primary risk).** The GO:0007274 signal is entirely from *Drosophila* Rbp. Because the fly gene and human RIMBP2 share the IPR040325 architecture, an automated or orthology-based pipeline could propagate the fly NMJ term to the human protein. This is the classic over-annotation-by-orthology pattern. The paralogs (RIMBP1/TSPOAP1, RIMBP3) and the mouse ortholog do **not** carry the term, reinforcing that it is fly-specific.

2. **Organism-specific phenotype divergence.** The fly NMJ phenotype (release collapse) differs qualitatively from the mammalian central-synapse phenotype (selective loss of coupling fidelity; [PMID: 26402606](https://pubmed.ncbi.nlm.nih.gov/26402606/)). Even if a vertebrate NMJ were tested, the process semantics might not match the fly annotation.

3. **Synapse-type breadth as a confound.** RIMBP2 acts at multiple synapse types (central, ribbon). As the seed hypothesis notes, a role at additional synapse types *neither establishes nor excludes* an NMJ role — but it does mean that generic active-zone terms, not a single synapse-type term, best represent the function.

4. **Expression vs. function.** Brain/neuroendocrine-enhanced expression with no muscle enhancement (HPA) argues against a *primary* NMJ role, but expression alone cannot exclude a minor/uncharacterized NMJ contribution.

No evidence was found that *refutes* an NMJ role outright; the conflict is between **orthology-based inference** and the **absence of vertebrate NMJ data**, resolved conservatively in favor of general terms.

---

## Limitations and Knowledge Gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No vertebrate NMJ experiment for RIMBP2 | Full primary mammalian literature (7 papers) — all central/ribbon synapses | Determines whether GO:0007274 is *untested* vs *false* for human | RIMBP2 cKO or knockdown at a mouse NMJ with electrophysiology (EPP/mEPP, quantal content) |
| PMID:22174254 abstract not independently re-verified here | Provenance confirmed via QuickGO/FlyBase annotation record | Anchors the fly IMP evidence | Direct read of the FlyBase reference to confirm NMJ assay details |
| Human-specific functional data | UniProt + HPA (human); functional studies are mouse | Human ortholog function is inferred from mouse | Human iPSC-derived neuromuscular co-culture or motor-neuron synapse assays |
| MF/interaction granularity | UniProt lists RIMS1/2, CACNA1D/B interactions | Determines the most informative non-"protein binding" MF terms | Curator review of interaction-supported MF terms |
| Isoform-specific behavior | Not resolved | Different isoforms could differ in synapse targeting | Isoform-resolved localization/interaction studies |

---

## Discriminating Tests

To distinguish "human RIMBP2 participates in NMJ transmission" from "RIMBP2 is a general AZ coupler not demonstrated at the vertebrate NMJ":

1. **Motor-endplate electrophysiology in RIMBP2 (± RIMBP1) conditional knockouts** — record endplate potentials (EPPs), miniature EPPs, quantal content, and short-term plasticity at the mouse diaphragm/soleus NMJ. A selective coupling-fidelity deficit (paralleling central synapses) would *demonstrate* an NMJ role; no deficit would argue against it.
2. **Immunolocalization at the mammalian NMJ** — high-resolution (STED/expansion) imaging for RIMBP2 at motor endplate active zones. Presence at motor AZs would upgrade plausibility.
3. **Ortholog-swap / rescue** — test whether human RIMBP2 rescues the *Drosophila* Rbp NMJ phenotype, probing functional conservation of the NMJ-relevant activity.
4. **Single-cell / spatial transcriptomics of motor neurons** — confirm whether RIMBP2 is expressed in α-motor neurons at levels consistent with an NMJ role.
5. **Comparative GO-provenance audit** — programmatically confirm that no vertebrate RIM-BP annotation to GO:0007274 exists across UniProt-GOA releases, to rule out silent carry-over.

---

## Proposed Follow-up Experiments / Actions (Curation Leads)

**All items below are leads requiring curator verification.**

1. **Do NOT add or retain GO:0007274 for human RIMBP2 (O15034).** Rationale: no human/mammalian evidence; term is *Drosophila*-specific in this family; over-specific by orthology.
2. **Retain GO:0150037** (*regulation of calcium-dependent activation of synaptic vesicle fusion*, IBA) as the accurate, synapse-type-agnostic BP term.
3. **Add/strengthen general active-zone terms** supported by mammalian phenotypes (Ca²⁺-channel clustering / coupling of Ca²⁺ influx to exocytosis; presynaptic active zone CC).
4. **Prefer specific MF/interaction terms** (RIMS1/RIMS2, CACNA1B/CACNA1D binding as bifunctional linker) over bare "protein binding."
5. **Flag the fly annotation as organism-specific** in any orthology-based inference note; document that transfer to human is not warranted.

**Candidate references with snippets to verify:**
- [PMID: 26402606](https://pubmed.ncbi.nlm.nih.gov/26402606/): *"in murine synapses, RIM-BPs are not essential for neurotransmitter release as such, but are selectively required for high-fidelity coupling of action potential-induced Ca(2+) influx to Ca(2+)-stimulated synaptic vesicle exocytosis"* → defines the demonstrated mammalian function (general coupling, central synapse).
- [PMID: 26402606](https://pubmed.ncbi.nlm.nih.gov/26402606/): *"In Drosophila, deletion of RIM-BPs dramatically reduces neurotransmitter release, but little is known about RIM-BP function in mammalian synapses"* → documents the fly-vs-mammal gap underpinning the over-annotation caution.
- [PMID: 22174254](https://pubmed.ncbi.nlm.nih.gov/22174254/) (FlyBase/QuickGO): source of the *Drosophila* Rbp GO:0007274 IMP annotation → verify it is NMJ-specific and fly-only.

**Suggested curator questions:**
- Is any GO:0007274 assignment on O15034 an IEA/ISS carry-over from the fly ortholog? If so, remove/generalize.
- Does the review intend synapse-type-agnostic terms (preferred) or synapse-type-specific terms (not supported for NMJ)?

**Suggested experiments (for the field):** RIMBP2 conditional-KO NMJ electrophysiology; motor-endplate super-resolution localization; fly-rescue with human RIMBP2 (see Discriminating Tests).

---

## Evidence Base (Literature)

- *RIM-BPs Mediate Tight Coupling of Action Potentials to Ca²⁺-Triggered Neurotransmitter Release* — [PMID: 26402606](https://pubmed.ncbi.nlm.nih.gov/26402606/) (Acuna et al. 2015). Defines the mammalian phenotype (coupling fidelity, not release essentiality) and explicitly contrasts it with the fly NMJ. **Central to the over-annotation argument.**
- *RIM-binding protein 2 regulates release probability by fine-tuning calcium channel localization at murine hippocampal synapses* — [PMID: 27671655](https://pubmed.ncbi.nlm.nih.gov/27671655/) (Grauel et al. 2016). Central-synapse localization/function.
- *RIM-Binding Protein 2 Organizes Ca²⁺ Channel Topography...* — [PMID: 34353898](https://pubmed.ncbi.nlm.nih.gov/34353898/) (Butola et al. 2021). AZ organization at calyx of Held.
- *RIM-BP2 regulates Ca²⁺-channel recruitment...* — [PMID: 38329474](https://pubmed.ncbi.nlm.nih.gov/38329474/) (Miyano et al. 2024). Calyx of Held.
- *RIM-BP2 primes synaptic vesicles...* — [PMID: 31535974](https://pubmed.ncbi.nlm.nih.gov/31535974/). Central-synapse priming/Ca²⁺ coordination.
- *RIM-Binding Protein 2 Promotes a Large Number of Ca²⁺ Channels...* — [PMID: 29163046](https://pubmed.ncbi.nlm.nih.gov/29163046/) (Krinner et al. 2017). IHC ribbon synapse.
- *RIM-Binding Proteins Are Required for Normal Sound-Encoding at Afferent Inner Hair Cell Synapses* — [PMID: 33867935](https://pubmed.ncbi.nlm.nih.gov/33867935/) (Krinner et al. 2021). Sensory synapse.
- *Drosophila Rbp GO:0007274 (IMP)* — [PMID: 22174254](https://pubmed.ncbi.nlm.nih.gov/22174254/) (FlyBase/QuickGO). The sole family source of the neuromuscular term.

Database/orientation sources: **UniProt O15034** (function, domains, location), **QuickGO** (annotation provenance, paralog/ortholog scan), **InterPro IPR040325**, **Human Protein Atlas** (expression).

---

## Conclusion

The seed hypothesis — that human RIMBP2 participates in neuromuscular synaptic transmission (GO:0007274) — is **weakly supported by phylogenetic inference** (orthology to *Drosophila* Rbp) but **unresolved and over-specific for the human protein**. Direct GO:0007274 evidence exists only for the fly ortholog; no vertebrate RIM-BP family member carries the term, and every mammalian study places RIMBP2 at central and sensory ribbon synapses, where its role is general Ca²⁺-channel–release-site coupling. A mammalian NMJ role is **untested, not disproven**. For curation, GO:0007274 should **not** be assigned directly to human RIMBP2; the function is best represented by general active-zone / Ca²⁺-coupling terms (e.g., GO:0150037) and specific RIMS/Ca²⁺-channel interaction terms.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist rimbp2 go0007274 evidence matrix](openscientist_artifacts/rimbp2_go0007274_evidence_matrix.csv)
- [OpenScientist rimbp2 go decision table](openscientist_artifacts/rimbp2_go_decision_table.csv)