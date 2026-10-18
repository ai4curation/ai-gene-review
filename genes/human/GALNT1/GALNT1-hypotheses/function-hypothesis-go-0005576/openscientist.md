---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-17T14:55:18.343684'
end_time: '2026-09-17T15:07:36.673619'
duration_seconds: 738.33
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: GALNT1
  gene_symbol: GALNT1
  uniprot_accession: Q10472
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0005576
  hypothesis_text: GALNT1 has extracellular region (GO:0005576).
  term_context: '- Term: extracellular region (GO:0005576)

    - Evidence type: IEA

    - Original reference: GO_REF:0000044'
  reference_context: '- GO_REF:0000044

    - PMID:12506059'
  source_file: genes/human/GALNT1/GALNT1-ai-review.yaml
  source_selector: existing_annotations[14].function_hypothesis
  source_context_yaml: "term:\n  id: GO:0005576\n  label: extracellular region\nevidence_type:\
    \ IEA\noriginal_reference_id: GO_REF:0000044"
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
citation_count: 5
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: galnt1_go0005576_evidence_matrix.csv
  path: openscientist_artifacts/galnt1_go0005576_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist galnt1 go0005576 evidence matrix
- filename: galnt1_go_decision_table.csv
  path: openscientist_artifacts/galnt1_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist galnt1 go decision table
- filename: galnt1_paralog_GO0005576_comparison.csv
  path: openscientist_artifacts/galnt1_paralog_GO0005576_comparison.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist galnt1 paralog GO0005576 comparison
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
- **Gene directory:** GALNT1
- **Gene symbol:** GALNT1
- **UniProt accession:** Q10472

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0005576
- **Source file:** genes/human/GALNT1/GALNT1-ai-review.yaml
- **Source selector:** existing_annotations[14].function_hypothesis

## Seed Hypothesis

GALNT1 has extracellular region (GO:0005576).

## Term and Decision Context

- Term: extracellular region (GO:0005576)
- Evidence type: IEA
- Original reference: GO_REF:0000044

## Reference Context

- GO_REF:0000044
- PMID:12506059

## Source Context YAML

```yaml
term:
  id: GO:0005576
  label: extracellular region
evidence_type: IEA
original_reference_id: GO_REF:0000044
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

# AIGR Gene Hypothesis Deep Research — GALNT1 / Extracellular Region (GO:0005576)

**Gene:** GALNT1 (Polypeptide N-acetylgalactosaminyltransferase 1) · Human · UniProt **Q10472**
**Focus:** function-assignment — *GALNT1 has extracellular region (GO:0005576)*
**Evidence type of the annotation under review:** IEA · **Original reference:** GO_REF:0000044
**Source:** `genes/human/GALNT1/GALNT1-ai-review.yaml` → `existing_annotations[14].function_hypothesis`

---

## Executive Judgment

**Verdict: Weakly supported / partially supported — treat as a non-core cellular-component annotation.**

The seed hypothesis that GALNT1 "has extracellular region (GO:0005576)" is technically defensible as an inferred, low-confidence localization, but it does **not** represent the gene product's primary or core cellular location and should **not** be treated as a leading localization in the gene review. GALNT1 is, at its core, a **Golgi-resident, single-pass type II transmembrane glycosyltransferase** that initiates mucin-type O-GalNAc glycosylation in the Golgi lumen. The GO:0005576 term is an **IEA-only** annotation, auto-derived through **GO_REF:0000044** (the UniProtKB keyword→GO subcellular-location mapping) solely from UniProt's evidence-free **"Secreted"** keyword. It is not backed by a targeted secretion or localization experiment for GALNT1, and the reference supplied in the review context (**PMID:12506059**) is a tissue-distribution immunohistochemistry study of GalNAc-transferases in ocular-surface epithelium — it does not demonstrate extracellular/secreted localization.

A genuine biological mechanism does exist by which Golgi glycosyltransferases can appear in the extracellular space: **SPPL3-mediated intramembrane proteolysis** cleaves the membrane anchor of Golgi enzymes and releases soluble ectodomains that are detectable in human blood (**PMID:35279766**). UniProt itself records a curated "soluble form" chain for GALNT1 (residues 41–559, lacking the cytoplasmic tail and transmembrane helix). This lends **biological plausibility** to a shed, soluble GALNT1 species, but plausibility is not the same as direct evidence, and a shed ectodomain is a *derived product* rather than the enzyme's primary functional location.

The most important caveat is that the annotation is **carried forward automatically** and is **easy to over-interpret**. The correct curatorial framing is: **retain Golgi membrane (GO:0000139) as the core cellular component**, and **either downgrade GO:0005576 to an explicitly non-core/low-confidence annotation or remove it**, because no GALNT1-specific experimental evidence for extracellular localization was located, and the community resource Human Protein Atlas classifies GALNT1 as "Intracellular and membrane," not secreted-to-blood.

---

## Key Findings

### Finding 1 — GO:0005576 is a broad, IEA-only annotation auto-derived from UniProt's "Secreted" keyword, not from direct GALNT1 evidence

GALNT1/Q10472 is curated by UniProt as a **Golgi apparatus (Golgi stack membrane) single-pass type II membrane protein**, with the topology cytoplasmic residues 1–8, transmembrane helix residues 9–28, and a large lumenal catalytic domain spanning residues 29–559. This architecture is the canonical form of the GALNT family: a short N-terminal cytoplasmic tail, a single signal-anchor transmembrane segment, a stem region, and a C-terminal catalytic + lectin domain that faces the Golgi lumen where O-glycosylation is initiated.

The extracellular-region annotation (GO:0005576) is attached with evidence code **IEA (ECO:0007322)**, qualifier **located_in**, and reference **GO_REF:0000044**. GO_REF:0000044 is the standardized pipeline that maps **UniProtKB subcellular-location keywords to GO cellular-component terms**. In this case the annotation is auto-derived **solely** from UniProt's **"Secreted"** subcellular-location keyword. Critically, UniProt attaches that "Secreted" keyword **without any PubMed evidence** of its own; it is instead supported internally by a curated **"soluble form" chain** (residues 41–559) that lacks the cytoplasmic tail and transmembrane anchor — i.e., a predicted/curated cleaved ectodomain rather than an experimentally localized secreted protein.

The reference bundled in the review context, **PMID:12506059**, is a **tissue immunolocalization study** describing how the "cell-layer- and cell-type-specific distribution of GalNAc-transferases in the ocular surface epithelia is altered during keratinization." This is a study of *which epithelial cell layers express GalNAc-transferases*, not evidence that GALNT1 protein resides in the *extracellular region*. It therefore does **not** directly support GO:0005576, and its inclusion in the context should not be read as experimental confirmation of secretion.

Independent orientation from the **Human Protein Atlas** classifies GALNT1's secretome location as **"Intracellular and membrane"** — explicitly *not* secreted-to-blood/extracellular. This is consistent with the enzyme's core Golgi biology and inconsistent with a strong, primary extracellular assignment.

Finally, a real shedding mechanism provides plausibility without confirming the specific claim. **PMID:35279766** established that "*Secretion of soluble Golgi enzymes that are released from their membrane anchor by endoprotease activity is a wide-spread yet largely unexplored phenomenon,*" identifying **SPPL3 intramembrane proteolysis** as the route by which Golgi glycosyltransferases become soluble and enter human blood. This shows that a soluble/extracellular GALNT1 form is mechanistically possible, but it also frames such a form as a **shed, derived product** — not the enzyme's primary Golgi location or function.

### Finding 2 — Paralog comparison: GO:0005576 is not blanket-propagated across the GALNT family, but GALNT1's remains IEA-only, whereas all paralogs share a Golgi component

To test whether the extracellular annotation is a generic family-wide carry-over (which would weaken any gene-specific meaning), QuickGO cellular_component annotations were compared across **10 human GALNT paralogs** (GALNT1, 2, 3, 4, 5, 6, 7, 10, 12, 14).

| Observation | Result |
|---|---|
| Paralogs carrying **GO:0005576** (extracellular region) | **2 of 10** — only GALNT1 and GALNT2 |
| GALNT1 GO:0005576 evidence | **IEA**, GO_REF:0000044 (keyword-derived) |
| GALNT2 GO:0005576 evidence | **EXP**, PMID:37453717 (chondroitin-sulfate glycoproteome mapping) |
| Paralogs carrying a **Golgi** cellular-component term | **10 of 10** |

Two conclusions follow. First, the extracellular term is **not** blanket-propagated to the whole family, so it is not simply a family-level artifact — but for **GALNT1 specifically it remains IEA-only** with no experimental support. Second, the **only** paralog with an "experimental" extracellular annotation (GALNT2) obtained it from a **high-throughput chondroitin-sulfate glycoproteome mapping study (PMID:37453717, Mol Cell Proteomics 2023)** — i.e., proteomic *detection in a fraction*, not a targeted secretion/localization assay. This means even the family's single "experimental" extracellular annotation is a weak, indirect line of evidence. In sharp contrast, **the Golgi cellular component is universal (10/10)**, which is the signal a curator should anchor on.

---

## Mechanistic Model / Interpretation

GALNT1's molecular function is the **initiation of mucin-type O-GalNAc glycosylation**: it transfers N-acetylgalactosamine (GalNAc) from UDP-GalNAc onto serine/threonine residues of acceptor proteins. This reaction occurs in the **Golgi lumen**, and the enzyme is anchored to the **Golgi stack membrane** by its type II single-pass topology. This is the enzyme's *primary function and primary location*.

The extracellular annotation arises downstream of, and is subordinate to, that core biology:

```
   PRIMARY (core, well supported)                 DERIVED (plausible, weakly supported)
   ------------------------------                 ------------------------------------
   Golgi stack membrane                           Regulated intramembrane proteolysis
   type II single-pass TM protein                 (e.g., SPPL3; PMID:35279766)
   TM 9-28, lumenal catalytic 29-559                       |
            |                                                v
            v                                       Soluble "ectodomain" (res 41-559)
   O-GalNAc glycosylation of Ser/Thr                        |
   (mucin-type O-glycan initiation)                         v
            |                                       UniProt "Secreted" keyword
            v                                                |
   GO:0000139 Golgi membrane  <-- CORE CC           GO_REF:0000044 keyword->GO mapping
                                                             |
                                                             v
                                                    GO:0005576 extracellular region (IEA)
                                                    <-- NON-CORE, low confidence
```

The chain from "Golgi membrane protein" to "extracellular region" passes through a **cleavage/shedding step** that is mechanistically real for the class of Golgi glycosyltransferases (PMID:35279766) but has **not** been demonstrated specifically for GALNT1 in the evidence located. The GO:0005576 term is therefore best understood as an **automatic annotation of a plausible but unconfirmed derived state**, several inferential steps removed from the direct, experimentally grounded Golgi function.

For curation, the practical implication is a clear hierarchy of confidence:

| Cellular component | GO term | Confidence | Curatorial status |
|---|---|---|---|
| Golgi (stack) membrane | GO:0000139 | High (family-universal, UniProt-curated topology) | **Core — retain/prioritize** |
| Extracellular region | GO:0005576 | Low (IEA, keyword-derived, no GALNT1 experiment) | **Non-core — downgrade or remove** |

---

## Evidence Matrix

| Citation | Evidence type | Supports / Refutes / Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt Q10472 (database) | Review/database | **Qualifies / competes** | Is extracellular region GALNT1's core location? | GALNT1 curated as Golgi stack membrane, type II single-pass TM (cyto 1–8, TM 9–28, lumenal 29–559); "Secreted" keyword supported by curated soluble chain 41–559, no PubMed evidence | Human, curated record | High for topology; the "Secreted" keyword itself is not experimentally referenced |
| GO_REF:0000044 (database) | Computational | **Qualifies** | Origin of GO:0005576 annotation | GO:0005576 is IEA, auto-mapped from UniProt "Secreted" keyword | Automated pipeline | High — confirms the annotation is keyword-derived, not experimental |
| [PMID:12506059](https://pubmed.ncbi.nlm.nih.gov/12506059/) | Localization (IHC) | **Does not support** | Does the cited reference show extracellular GALNT1? | Tissue distribution of GalNAc-transferases across ocular-surface epithelial layers changes with keratinization; not an extracellular-localization result | Human ocular surface epithelium | Moderate; relevant to expression pattern, not to secretion/extracellular residence |
| [PMID:35279766](https://pubmed.ncbi.nlm.nih.gov/35279766/) | Direct assay / mechanism | **Qualifies (plausibility)** | Can Golgi glycosyltransferases become extracellular? | SPPL3 intramembrane proteolysis releases soluble Golgi enzymes into blood — "wide-spread yet largely unexplored" | Human, N-terminome/secretome | High for the class; not GALNT1-specific in the evidence reviewed |
| Human Protein Atlas (database) | Localization/database | **Refutes strong claim** | Is GALNT1 secreted-to-blood/extracellular? | Secretome location classified "Intracellular and membrane" | Human, multi-tissue | Moderate; classifier-based, but argues against primary secretion |
| QuickGO paralog scan (database) | Computational/comparative | **Qualifies** | Is GO:0005576 a family-wide artifact? | 2/10 GALNTs have GO:0005576 (GALNT1 IEA; GALNT2 EXP); 10/10 have a Golgi term | Human GALNT1/2/3/4/5/6/7/10/12/14 | High for annotation census; interpretation depends on annotation completeness |
| [PMID:37453717](https://pubmed.ncbi.nlm.nih.gov/37453717/) (via GALNT2) | Direct assay (HT proteomics) | **Qualifies (weak analog)** | Basis of the only EXP extracellular GALNT annotation | GALNT2 extracellular annotation derives from chondroitin-sulfate glycoproteome mapping | Human, proteomic fraction | Low-moderate; detection in a fraction, not targeted localization; concerns a paralog, not GALNT1 |

---

## GO Curation Implications

**Lead (requires curator verification):** Do **not** promote GO:0005576 to a core cellular-component annotation for GALNT1. The evidence supports a **CC** decision in which:

- **Golgi membrane (GO:0000139)** — and more broadly the Golgi apparatus — is **retained as the core cellular component**. This is family-universal (10/10 paralogs) and consistent with UniProt's curated type II single-pass Golgi topology.
- **Extracellular region (GO:0005576)** should be **treated as non-core**: either
  1. **Retained but explicitly flagged as low-confidence / IEA-only / non-core** (acceptable if the curation model tolerates keyword-derived localizations), or
  2. **Removed**, on the grounds that it is a generic, keyword-derived term with no GALNT1-specific experimental support and is potentially misleading about the enzyme's biology.

The term is a **cellular-component (CC)** term. It should **not** be *generalized* further (it is already broad) and it should **not** be *made more specific* without new evidence (e.g., there is no basis to assert "extracellular space" or a specific secreted-form annotation). If retained, an **NOT**-qualifier is not warranted (a soluble form is plausible), but a confidence/evidence downgrade is. The core molecular-function and biological-process annotations of GALNT1 (UDP-GalNAc:polypeptide N-acetylgalactosaminyltransferase activity; O-glycan/mucin-type O-glycosylation) are unaffected by this decision and remain the enzyme's defining functions.

---

## Mechanistic Scope

The immediate molecular event being tested here is purely a **localization claim** (a cellular-component assertion), not a molecular-function or biological-process claim. The question is narrowly: *does the GALNT1 gene product reside in the extracellular region?*

- **Direct gene-product activity/location (well supported):** Golgi-luminal O-GalNAc glycosyltransferase anchored in the Golgi stack membrane. This is the enzyme's primary, experimentally and structurally grounded location.
- **Derived state (weakly supported, inference only):** A soluble ectodomain (res 41–559) that could be released by regulated intramembrane proteolysis and reach the extracellular space/blood. This is a *downstream product* of a shedding mechanism, not the enzyme's operative location.
- **Not localization evidence at all:** The tissue-distribution IHC study (PMID:12506059) reports *which epithelial cell types/layers express* GalNAc-transferases — an expression-pattern phenotype, not evidence of extracellular residence.

The extracellular annotation thus sits at the far end of an inference chain and should be separated cleanly from GALNT1's directly assayed Golgi function.

---

## Conflicts and Alternatives

1. **Database carry-over / keyword inflation.** The strongest alternative explanation for GO:0005576 is that it is an **artifact of automated keyword→GO mapping** (GO_REF:0000044) applied to a UniProt "Secreted" keyword that itself lacks direct experimental backing. This is the most parsimonious account and is consistent with the IEA evidence code.
2. **Paralog confusion / family propagation — partially ruled out.** The paralog census shows GO:0005576 is *not* uniformly propagated (only 2/10), so it is not a blanket family artifact. However, this same scan confirms GALNT1's term is IEA-only, and the sole "experimental" family analog (GALNT2, PMID:37453717) rests on high-throughput proteomic detection rather than targeted localization — so the alternative "extracellular is a real, general GALNT property" is **not** supported.
3. **Organism/tissue context.** No organism-specific extracellular evidence for GALNT1 was located; the Human Protein Atlas classification ("Intracellular and membrane") actively conflicts with a primary secreted assignment.
4. **Isoform/soluble-form specificity.** If GALNT1 does appear extracellularly, the relevant species is a **cleaved soluble form**, not full-length membrane GALNT1. A curator should not conflate the two: the extracellular claim, if entertained, applies to a shed ectodomain and should be annotated with that nuance rather than as generic localization of the canonical protein.

---

## Limitations and Knowledge Gaps

- **No GALNT1-specific extracellular assay was found.** The investigation relied on database records, a mechanistic class-level paper (PMID:35279766), a paralog annotation census, and orientation from Human Protein Atlas. A direct secretion/shedding experiment for GALNT1 (mass spectrometry of conditioned media or plasma with GALNT1 peptides mapped to the soluble form) was **not** identified. *Why it matters:* this is the single piece of evidence that would move the term from "weakly supported" to "supported."
- **PMID:12506059 abstract only partially reviewed.** The reference was assessed from its stated scope (ocular-surface GalNAc-transferase distribution) and judged not to be extracellular-localization evidence; the full text was not exhaustively mined. *Why it matters:* small chance of a secretion observation buried in the paper, though unlikely given its stated aim.
- **GALNT2 EXP annotation (PMID:37453717) not deeply verified.** It was classified from annotation metadata as a chondroitin-sulfate glycoproteome mapping study; the primary paper was not fully read. *Why it matters:* it is the family's only experimental extracellular datapoint and sets a precedent for how curators treat HT-proteomic "extracellular" detections.
- **Human Protein Atlas classification is classifier-based.** Its "Intracellular and membrane" call is orientation-level, not a targeted experiment. *Why it matters:* it argues against secretion but should not be over-weighted as definitive.
- **SPPL3–GALNT1 link is inferred by class membership.** PMID:35279766 establishes the mechanism for Golgi glycosyltransferases broadly; direct demonstration that SPPL3 sheds GALNT1 specifically was not confirmed.

---

## Proposed Follow-up Experiments / Actions (Discriminating Tests)

To move this annotation from "weakly supported" to a firm decision, the following would be most efficient:

1. **Targeted secretome/plasma proteomics for GALNT1.** Query existing human plasma/secretome MS datasets (including those associated with PMID:35279766) for GALNT1 peptides, and check whether detected peptides map **exclusively to the soluble form (res 41–559)** and **exclude the cytoplasmic tail/TM (res 1–28)**. Peptide topology is the decisive discriminator between a genuine shed ectodomain and contamination.
2. **SPPL3 perturbation.** Test whether SPPL3 knockout/knockdown reduces, and SPPL3 overexpression increases, soluble GALNT1 release in a relevant human cell line — directly linking GALNT1 to the established shedding mechanism.
3. **Subcellular fractionation + confocal colocalization.** Confirm the dominant pool colocalizes with Golgi markers (GM130/TGN46) and quantify any surface/secreted fraction, establishing the core-vs-derived ratio.
4. **Paralog-controlled annotation audit.** Systematically compare how curators handle HT-proteomic "extracellular" detections across GALNT2 and other glycosyltransferases to set a consistent evidence bar for GO:0005576.

---

## Curation Leads

*All items below are leads requiring curator verification.*

- **Candidate action change:** Downgrade **GO:0005576 (extracellular region)** from an unqualified localization to an explicitly **non-core / low-confidence (IEA-only)** annotation, or remove it; **retain GO:0000139 (Golgi membrane)** as the core cellular component. *Rationale:* IEA, keyword-derived (GO_REF:0000044), no GALNT1-specific experimental support; Golgi is family-universal (10/10 paralogs).

- **Candidate references to verify:**
  - [PMID:35279766](https://pubmed.ncbi.nlm.nih.gov/35279766/) — verify snippet: *"Secretion of soluble Golgi enzymes that are released from their membrane anchor by endoprotease activity is a wide-spread yet largely unexplored phenomenon."* Use as *mechanistic plausibility* for a soluble form, **not** as direct GALNT1 extracellular evidence.
  - [PMID:12506059](https://pubmed.ncbi.nlm.nih.gov/12506059/) — verify snippet: *"The cell-layer- and cell-type-specific distribution of GalNAc-transferases in the ocular surface epithelia is altered during keratinization."* Confirm this is expression-distribution, **not** extracellular localization; it should not be cited as support for GO:0005576.
  - [PMID:37453717](https://pubmed.ncbi.nlm.nih.gov/37453717/) — verify it is the basis of GALNT2's EXP extracellular annotation and assess whether HT glycoproteome detection meets the curation bar for CC assignment.

- **Candidate GO decision (CC):** No new/replacement CC term is recommended. If the curation model requires a positive core CC, use **GO:0000139 (Golgi membrane)**. Do not adopt more specific extracellular terms (e.g., extracellular space) without new evidence.

- **Suggested curator questions:**
  1. Does the review model permit retaining an IEA keyword-derived CC term flagged as non-core, or should it be removed?
  2. Is there a consistency policy for HT-proteomic "extracellular" detections (as in GALNT2/PMID:37453717) that should apply to GALNT1?

- **Suggested experiments:** SPPL3-dependent shedding assay for GALNT1; secretome/plasma MS with soluble-form peptide mapping; Golgi-marker colocalization to quantify core vs. shed pools (see *Proposed Follow-up Experiments*).

---

## Evidence Base (Literature Summary)

- **[PMID:35279766](https://pubmed.ncbi.nlm.nih.gov/35279766/)** — *N-terminome analyses of SPPL3-mediated intramembrane proteolysis among Golgi-resident enzymes.* Establishes the mechanism (SPPL3) that releases soluble Golgi glycosyltransferases into blood. **Supports plausibility** of a soluble GALNT1 form while framing it as a shed, derived product — not the primary location.
- **[PMID:12506059](https://pubmed.ncbi.nlm.nih.gov/12506059/)** — *Cell-layer/cell-type distribution of GalNAc-transferases in ocular-surface epithelia during keratinization.* The reference bundled with the annotation; an **expression-distribution IHC study**, **not** extracellular-localization evidence. Does not directly support GO:0005576.
- **[PMID:37453717](https://pubmed.ncbi.nlm.nih.gov/37453717/)** (via GALNT2) — chondroitin-sulfate glycoproteome mapping; the sole EXP-coded extracellular annotation in the GALNT family, and only a **high-throughput proteomic detection**, illustrating how weak the family's extracellular evidence is.
- **UniProt Q10472** and **GO_REF:0000044** (database orientation) — confirm the Golgi type II single-pass topology and the keyword-derived, IEA origin of the extracellular annotation.
- **Human Protein Atlas** (database orientation) — classifies GALNT1 as "Intracellular and membrane," arguing against a primary secreted/extracellular assignment.
- Family context reviews (*The Critical Role of GALNTs-Regulated O-GalNAc Glycosylation in Cancer Malignancy*, [PMID:42012463](https://pubmed.ncbi.nlm.nih.gov/42012463/); *GalNAc-Transferases in Cancer*, [PMID:41595542](https://pubmed.ncbi.nlm.nih.gov/41595542/)) reinforce that the GALNT family's characterized biology is **Golgi-based O-glycan initiation**, consistent with Golgi as the core location.

---

## Bottom Line

GALNT1 is fundamentally a **Golgi-resident type II single-pass membrane glycosyltransferase** that initiates mucin-type O-GalNAc glycosylation. The **extracellular region (GO:0005576)** annotation is **IEA-only**, auto-derived from UniProt's evidence-free "Secreted" keyword via GO_REF:0000044, and is unsupported by any GALNT1-specific experiment; the reference PMID:12506059 is a tissue-distribution study, and Human Protein Atlas calls the protein intracellular/membrane. A shed soluble form is biologically plausible (SPPL3 mechanism; PMID:35279766) but unconfirmed for GALNT1. **Recommendation: retain Golgi membrane (GO:0000139) as the core cellular component and treat GO:0005576 as non-core/low-confidence — flag or remove — pending direct secretion evidence.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist galnt1 go0005576 evidence matrix](openscientist_artifacts/galnt1_go0005576_evidence_matrix.csv)
- [OpenScientist galnt1 go decision table](openscientist_artifacts/galnt1_go_decision_table.csv)
- [OpenScientist galnt1 paralog GO0005576 comparison](openscientist_artifacts/galnt1_paralog_GO0005576_comparison.csv)