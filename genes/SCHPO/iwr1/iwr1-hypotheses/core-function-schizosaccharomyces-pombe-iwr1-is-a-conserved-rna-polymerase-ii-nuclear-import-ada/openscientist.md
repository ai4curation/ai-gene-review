---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T09:17:13.018481'
end_time: '2026-08-31T09:30:18.508199'
duration_seconds: 785.49
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: iwr1
  gene_symbol: iwr1
  uniprot_accession: O13951
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: core_function
  hypothesis_slug: core-function-schizosaccharomyces-pombe-iwr1-is-a-conserved-rna-polymerase-ii-nuclear-import-ada
  hypothesis_text: Schizosaccharomyces pombe Iwr1 is a conserved RNA polymerase II
    nuclear-import adaptor that binds assembled Pol II and presents its own NLS to
    karyopherin-alpha
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Iwr1 is a conserved\
    \ RNA polymerase II nuclear-import adaptor that\n  binds assembled Pol II and\
    \ presents its own NLS to karyopherin-alpha\nfocus_type: core_function\ncontext:\
    \ []\nreference_id: []"
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

- **Organism code:** SCHPO
- **Taxon:** Schizosaccharomyces pombe (strain 972 / ATCC 24843) (NCBITaxon:284812)
- **Gene directory:** iwr1
- **Gene symbol:** iwr1
- **UniProt accession:** O13951

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-schizosaccharomyces-pombe-iwr1-is-a-conserved-rna-polymerase-ii-nuclear-import-ada
- **Source file:**
- **Source selector:**

## Seed Hypothesis

Schizosaccharomyces pombe Iwr1 is a conserved RNA polymerase II nuclear-import adaptor that binds assembled Pol II and presents its own NLS to karyopherin-alpha

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Iwr1 is a conserved RNA polymerase II nuclear-import adaptor that
  binds assembled Pol II and presents its own NLS to karyopherin-alpha
focus_type: core_function
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

# AIGR Deep Research — *S. pombe* iwr1 (O13951) core-function hypothesis

**Hypothesis under review:** *Schizosaccharomyces pombe* Iwr1 is a conserved RNA polymerase II
nuclear-import adaptor that binds assembled Pol II and presents its own NLS to karyopherin-α.

**Focus type:** core_function · **Gene:** iwr1 / SPAC23H4.08 · **UniProt:** O13951 (277 aa)

---

## Executive Judgment

**Verdict: Partially supported (supported by orthology; not experimentally demonstrated in *S. pombe*).**

The described activity — an Iwr1 protein that binds assembled Pol II and presents its own
N-terminal bipartite NLS to karyopherin-α to drive Pol II nuclear import — is a *bona fide*,
directly demonstrated **core molecular function of the *Saccharomyces cerevisiae* ortholog**
(Czeko et al., 2011, PMID 21504834), and the authors explicitly report it is "apparently
conserved from yeast to human." For the *S. pombe* target specifically, the assignment is
**entirely inference-based**: every GO annotation on O13951 is electronic/phylogenetic
(IEA/ISO/IBA), the molecular-function slot is **ND (no data)**, and no primary *S. pombe*
experimental study of iwr1 exists in the literature. Sequence analysis I ran supports
transferability — O13951 carries the Iwr1 Pfam domain (PF08574) and conserves the N-terminal
basic (NLS-like) clusters and acidic C-terminal tail seen in budding-yeast Iwr1 — but the NLS /
karyopherin-α interaction and Pol II binding have **not been tested in fission yeast**.

**Most important caveats.** (1) The "presents its *own* NLS to karyopherin-α" clause is a
*S. cerevisiae* mechanistic detail, transferred by conservation, not verified in *S. pombe*.
(2) Iwr1 is **non-essential** and Pol II import can proceed by Iwr1-independent routes
(PMID 26455955), so it is a **facilitating adaptor, not the obligate importer**. (3) Budding-yeast
Iwr1 has additional documented roles (elongation, Pol II disassembly from chromatin, genome
stability, gene-specific transcription); the import-adaptor role is the best-supported **direct**
function, whereas transcription phenotypes are largely downstream. (4) Ortholog identity is
**low** (~23% to *S. cerevisiae*, ~20% to human SLC7A6OS); orthology rests on the shared Iwr1
Pfam domain (PF08574) and positionally conserved N-terminal basic clusters rather than high
sequence identity.

**Supporting feasibility checks I ran this iteration.** The AlphaFold model of O13951 is largely
low-confidence/disordered (mean pLDDT 64.6) but the **N-terminal NLS cluster (res 5–15) is
well-ordered (pLDDT ≈91)** — structurally consistent with an intrinsically disordered Pol II-cleft
adaptor carrying a defined, accessible NLS. *S. pombe* also **encodes the required importin-α
receptors** (imp1/O94374, cut15/O14063), so the proposed karyopherin-α–dependent mechanism is
feasible in this organism (though the Iwr1–importin-α interaction itself is untested here).

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| 21504834 (Czeko 2011) | Direct assay / structural / interaction | **Supports** | Iwr1 binds assembled Pol II and presents own NLS to karyopherin-α for import | Iwr1 binds Pol II in the active-center cleft between the two largest subunits; N-terminal **bipartite NLS recognized by karyopherin-α** directs import; displaced by initiation factors/nucleic acids; "Pol II specific, transcription independent, apparently conserved from yeast to human." | *S. cerevisiae* (+ conservation claim) | High for *S. cerevisiae*; conservation to *S. pombe* asserted but not directly shown |
| 19679657 (Peiró-Chova 2009) | Mutant phenotype / interaction | Qualifies | Iwr1 role in transcription vs import | Iwr1p physically interacts with most Pol II subunits; genetic interactions with basal machinery; nucleocytoplasmic shuttling; affects specific-gene transcription | *S. cerevisiae* | Transcription effects likely **downstream** of import/assembly role |
| 26455955 (Gómez-Navarro 2015) | Mutant phenotype / localization | **Qualifies** | Iwr1 is the sole Pol II importer | IWR1 is non-essential; Iwr1-independent import pathways exist (holoenzyme, partial assemblies, diffusion of small subunits) | *S. cerevisiae* | Iwr1 is a **facilitator/adaptor**, not obligate; supports "adaptor" but weakens "the importer" |
| 28258010 (Gómez-Navarro 2017) | Mutant phenotype / genetics | Competing/qualifies | Import is Iwr1's only role | Iwr1 also acts during **elongation** and in Pol II **disassembly from chromatin**; iwr1Δ causes genome instability, genotoxin sensitivity | *S. cerevisiae* | Argues for additional direct nuclear roles beyond import |
| 23267056 (Minaker 2013) | Mutant phenotype / localization | Supports (pathway) | Iwr1 in Pol II (and III) biogenesis | iwr1Δ Pol II import defect is suppressed by an NLS fused to Rpb3, consistent with Iwr1 supplying the NLS; GPN GTPases act upstream | *S. cerevisiae* | Reinforces the "Iwr1 provides the NLS" model; also implicates Pol III |
| 23438601 (Gómez-Navarro 2013) | Interaction / pathway | Qualifies | Import machinery composition | Rtp1/karyopherin-like factors and R2TP participate in Pol II assembly/import alongside Iwr1 | *S. cerevisiae* | Import is multi-factor; Iwr1 is one component |
| UniProt O13951 (by similarity) | Database | Supports (orientation) | Function of *S. pombe* protein | Annotated "Directs RNA polymerase II nuclear import," "Associates with RNA polymerase II," Cytoplasm+Nucleus, IWR1/SLC7A6OS family (PF08574) | *S. pombe* | Inferred by similarity, not experimental |
| QuickGO annotations for O13951 | Database | Qualifies | Current curation state | BP GO:0006606 (IEA/ISO/IBA); CC GO:0005634 + GO:0005737 (ISO/IBA/IEA); **MF = GO:0003674 ND** | *S. pombe* | No experimental (EXP/IDA/IPI) evidence; MF unassigned |
| This report (computed) | Computational / evolutionary | Supports | Architecture conserved in O13951 | Iwr1 domain present; N-terminal basic clusters (RVKRK res7–11, TKRRK res34–38) match budding-yeast bipartite-NLS position; acidic C-terminal tail conserved | *S. pombe* vs *S. cerevisiae* Q07532 | Sequence-level only; predicts, does not prove, NLS function |
| This report (computed, AlphaFold DB) | Structural / computational | Supports | Is the NLS in an ordered, accessible element? | O13951 is mostly low-confidence/disordered (mean pLDDT 64.6), but N-terminal NLS cluster1 (res 5–15) is well-ordered (pLDDT ~91); rest of protein and acidic C-tail are low-pLDDT | *S. pombe* AlphaFold model | Model-based; consistent with a disordered cleft-adaptor bearing a defined N-terminal NLS |
| This report (computed, NW alignment) | Evolutionary / computational | **Qualifies** | Strength of orthology | Global identity O13951 vs *S. cerevisiae* Iwr1 = **22.7%**; vs human SLC7A6OS = **20.4%** — low; orthology rests on shared Pfam PF08574 + positionally conserved basic clusters, not high identity | pairwise | Low identity weakens direct mechanistic transfer; family assignment is the stronger signal |
| This report (computed, UniProt) | Database / feasibility | Supports (feasibility) | Does the required receptor exist in *S. pombe*? | *S. pombe* encodes importin-α orthologs **imp1 (O94374)** and **cut15 (O14063)** | *S. pombe* | Presence of receptor makes the model feasible; Iwr1–importin-α binding itself untested in *S. pombe* |
| 16823372 (Matsuyama 2006) | Localization (high-throughput) | Supports (CC) | Subcellular localization in fission yeast | Genome-wide YFP localization of ~90% of *S. pombe* proteome (resource that provides direct *S. pombe* localization data) | *S. pombe* | High-throughput; iwr1-specific call should be verified in PomBase/the dataset |
| PomBase SPAC23H4.08 (record) | Database | **Qualifies** | Is there direct *S. pombe* evidence? | characterisation_status = **"biological role inferred"**; deletion **viable**; **single copy (1:1)**, no paralog; GO = CC cytoplasm+nucleus, BP protein import into nucleus, **no MF term**; descriptor "nucleocytoplasmic shuttling protein"; GO transfer via GO_REF:0000033 (IBA)/0000024 (ISO) | *S. pombe* | Confirms role is inferred, not experimentally shown; single-copy rules out paralog confusion |
| PomBase phenotypes (screens: PMID 20473289, 37787768) | Mutant phenotype (high-throughput) | Qualifies / competing | Are loss phenotypes the core function? | ~30 pleiotropic screen phenotypes: drug/stress **resistance** (MMS, HU, caffeine, cadmium, cycloheximide), decreased mating efficiency, multiseptate, loss of stationary-phase viability | *S. pombe* deletion screens | Pleiotropic/downstream, not core MF; iwr1Δ **MMS/HU resistance** contrasts with *S. cerevisiae* genotoxin **sensitivity** (PMID 28258010) — organism difference or screen artifact |

---

## GO Curation Implications (leads — require curator verification)

- **BP GO:0006606 "protein import into nucleus" — RETAIN.** Well-supported by orthology
  (ISO from SGD IWR1, IBA, IEA) and consistent with conserved architecture. It is appropriately
  general; there is no granular "RNA polymerase II complex nuclear import" GO term, so 0006606 is
  the correct level. Evidence code should remain non-experimental (ISO/IBA) for *S. pombe*.
- **MF is currently ND — a candidate ADD (lead).** The hypothesis implies a definable molecular
  function as an **import adaptor**. Best-supported candidate MF terms, by orthology only:
  - **GO:0030674 "protein-macromolecule adaptor activity"** — captures bridging Pol II cargo to
    karyopherin-α; the most informative MF consistent with the mechanism.
  - **GO:0000993 "RNA polymerase II complex binding"** — captures the direct Pol II association.
  - Avoid "protein binding" (GO:0005515) as a terminal recommendation; the above are more informative.
  - Because *S. pombe* evidence is inference-only, any MF addition should carry ISO/IBA evidence,
    not experimental codes.
- **CC GO:0005634 (nucleus) + GO:0005737 (cytoplasm) — RETAIN.** Consistent with a shuttling
  adaptor and with the *S. pombe* ORFeome localization resource (PMID 16823372, verify the
  iwr1-specific call).
- **Do not over-state.** Avoid annotating iwr1 as the obligate Pol II importer or asserting a
  verified karyopherin-α interaction in *S. pombe*; the import pathway is redundant (PMID 26455955).

---

### GO Decision Table (leads — require curator verification)

| Aspect | Term | Current state (O13951) | Recommended action | Suggested evidence code | Rationale |
|---|---|---|---|---|---|
| BP | GO:0006606 protein import into nucleus | Present (IEA/ISO/IBA) | **Retain** | ISO/IBA | Correct granularity (no Pol-II-specific import term exists); well-supported by orthology; PomBase concurs |
| MF | GO:0030674 protein-macromolecule adaptor activity | **Absent (MF = ND)** | **Consider ADD (lead)** | ISO/IBA | Captures the cargo↔karyopherin-α bridging that is the essence of the hypothesis |
| MF | GO:0000993 RNA polymerase II complex binding | Absent | **Consider ADD (lead)** | ISO/IBA | Captures direct Pol II association ("binds assembled Pol II") |
| MF | GO:0005515 protein binding | — | **Avoid as terminal** | — | Uninformative; use the two MF terms above instead |
| CC | GO:0005634 nucleus | Present | Retain | ISO/IBA/IEA | Shuttling adaptor; consistent with *S. pombe* record |
| CC | GO:0005737 cytoplasm | Present | Retain | ISO/IBA/IEA | Cytoplasmic Pol II binding / recycling |
| BP/CC | genotoxin sensitivity, mating, drug-resistance phenotypes | PomBase screen phenotypes | **Do NOT annotate as core function** | — | Pleiotropic, downstream, screen-derived; some conflict with *S. cerevisiae* |

All *S. pombe* MF/BP/CC calls should carry **non-experimental (ISO/IBA)** evidence — no
experimental (EXP/IDA/IPI) code is justified, as no direct fission-yeast assay exists.

## Mechanistic Scope

**Direct molecular function under test:** cytoplasmic binding of the assembled 12-subunit Pol II
in its cleft, and presentation of Iwr1's own N-terminal bipartite NLS to karyopherin-α
(importin-α; *S. pombe* Cut15/Imp1 family) to mediate Pol II nuclear import, followed by Iwr1
displacement, export and recycling. This is a **transcription-independent** transport/adaptor
activity.

**Downstream / non-core effects (should not be conflated with the core function):**
gene-specific transcription changes, NC2/TFIIA genetic bypass, elongation and Pol II
chromatin-disassembly roles, genome instability and genotoxin sensitivity in null mutants.
These are documented for budding yeast and are largely **consequences of** (or roles adjacent to)
the import/assembly function rather than the primary molecular activity.

---

## Conflicts and Alternatives

- **Organism gap (principal issue):** all direct evidence is *S. cerevisiae*/human-family; the
  *S. pombe* claim is orthology transfer. This is the central caveat, not a contradiction.
- **Redundancy:** Iwr1-independent import pathways exist (PMID 26455955); "adaptor" is accurate,
  "the importer" is too strong.
- **Multifunctionality:** Gómez-Navarro 2017 (PMID 28258010) supports additional direct roles
  (elongation, Pol II turnover), so "nuclear-import adaptor" may be **one of several** direct
  functions rather than the sole one — though it remains the best-characterized primary activity.
- **Pol specificity:** Minaker 2013 (PMID 23267056) reports iwr1 mutant Pol **III** localization
  defects too, mildly complicating the strict "Pol II-specific" clause.
- **Paralog/family note:** family is IWR1/SLC7A6OS (human SLC7A6OS); PomBase lists iwr1 as
  **"predominantly single copy (one to one)"** with no *S. pombe* paralog, so paralog
  over-annotation is unlikely here.
- **Phenotype direction conflict:** *S. pombe* iwr1Δ shows **resistance** to MMS/HU in genome-wide
  screens, whereas *S. cerevisiae* iwr1Δ is **sensitive** to genotoxins (PMID 28258010). Likely an
  organism difference or high-throughput screen artifact; either way these DNA-damage phenotypes
  are peripheral to the core import-adaptor function and should not drive the core-function call.
- **Taxonomic-scope nuance:** PomBase tags iwr1 both "conserved in eukaryotes" and "conserved in
  fungi only"; a clear 1:1 ortholog is fungal, while the broader Pfam family reaches metazoa
  (human SLC7A6OS) only at ~20% identity. The seed's "conserved… yeast to human" is defensible at
  the family level but weak at the sequence-identity level.

---

## Knowledge Gaps

1. **No direct *S. pombe* assay** of Iwr1–Pol II binding or Iwr1–karyopherin-α (Cut15/Imp1)
   interaction. *Checked:* PubMed (no iwr1 fission-yeast primary papers), UniProt (by-similarity),
   QuickGO (no EXP codes). *Matters:* the entire core-function call is inference. *Resolve:*
   co-IP/affinity capture of Pol II with tagged Iwr1 in *S. pombe*; NLS-deletion import assay.
2. **Functional NLS not verified in O13951.** *Checked:* sequence — basic clusters present in the
   conserved position. *Matters:* the "own NLS" clause is the crux of the hypothesis. *Resolve:*
   mutate res 7–11/34–38 and assay Rpb1 nuclear localization; test suppression by Rpb3-NLS fusion.
3. **iwr1-specific localization** in *S. pombe* — **partially resolved.** *Checked:* PomBase
   records CC cytoplasm + nucleus and the descriptor "nucleocytoplasmic shuttling protein," and
   flags characterisation_status = "biological role inferred." *Remaining:* these lack an
   experimental evidence code tied to a dedicated iwr1 study; confirm the ORFeome (PMID 16823372)
   call and whether shuttling was directly observed for iwr1 in *S. pombe*.
4. **Essentiality / redundancy in *S. pombe*** unquantified. *Resolve:* iwr1Δ phenotype and
   Rpb1-GFP localization in fission yeast.

---

## Discriminating Tests

1. **Iwr1–Pol II co-purification in *S. pombe*** (TAP/FLAG-Iwr1 → MS): confirms cargo binding.
2. **NLS-swap / NLS-deletion import assay:** delete O13951 N-terminal basic clusters, score
   Rpb1-GFP nuclear import; rescue by fusing a heterologous NLS to Rpb3 (mirrors PMID 23267056).
3. **Iwr1–karyopherin-α (Cut15) two-hybrid / pulldown** in *S. pombe*.
4. **Structure prediction of the O13951–Pol II cleft interface** (AlphaFold-Multimer of Iwr1 with
   Rpb1/Rpb2) to test cleft-binding conservation *in silico*.
5. **Cross-complementation:** does *S. pombe* iwr1 rescue *S. cerevisiae* iwr1Δ import defect?

---

## Curation Leads (require curator verification)

- **Action:** Keep BP GO:0006606; consider **adding an MF** (GO:0030674 protein-macromolecule
  adaptor activity and/or GO:0000993 RNA polymerase II complex binding) with **ISO/IBA** evidence,
  filling the current ND slot. Keep CC nucleus + cytoplasm.
- **Reference to cite for the mechanism (ortholog):** PMID **21504834** — snippet to verify:
  *"Iwr1 then uses an N-terminal bipartite nuclear localization signal that is recognized by
  karyopherin α to direct Pol II nuclear import"* and *"Iwr1 function is Pol II specific,
  transcription independent, and apparently conserved from yeast to human."*
- **Qualifier reference (redundancy):** PMID **26455955** — establish that import is not
  Iwr1-obligate; annotate as adaptor/facilitator, not sole importer.
- **Localization support (fission yeast):** PMID **16823372** (verify iwr1 call).
- **Suggested question for curator:** Should the *S. pombe* MF/BP additions be evidence-coded
  ISO/IBA (recommended) given the absence of any *S. pombe* experimental data?
- **Suggested experiments:** the discriminating tests above, especially the NLS-deletion import
  assay and Iwr1–Pol II co-IP in *S. pombe*.

---

*Provenance:* UniProt REST (O13951, Q07532), QuickGO annotation API, and an executed
sequence-conservation comparison (Iwr1 domain PF08574; N-terminal basic clusters; acidic C-tail)
were run during this review. All *S. pombe*-level functional statements are inference from
orthology; no *S. pombe* experimental primary literature was found.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
