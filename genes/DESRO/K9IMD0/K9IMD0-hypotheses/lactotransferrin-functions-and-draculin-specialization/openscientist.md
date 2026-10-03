---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T01:08:52.668658'
end_time: '2026-09-21T01:28:37.605918'
duration_seconds: 1184.94
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: DESRO
  gene: K9IMD0
  gene_symbol: K9IMD0
  uniprot_accession: K9IMD0
  taxon_id: NCBITaxon:9430
  taxon_label: Desmodus rotundus
  focus_type: function_assignment
  hypothesis_slug: lactotransferrin-functions-and-draculin-specialization
  hypothesis_text: Desmodus rotundus lactotransferrin/draculin K9IMD0 retains transferrin-family
    metal binding GO:0046872, iron/monoatomic ion transport GO:0006826/GO:0006811,
    serine-type peptidase/peptidase/hydrolase activity GO:0008236/GO:0008233/GO:0016787
    and proteolysis GO:0006508, antibacterial humoral response GO:0019731, defense
    response to bacterium GO:0042742 and immune system process GO:0002376. Evaluate
    these independently of its anticoagulant role. Separately assess early/recycling
    endosome and plasma-membrane association GO:0005769/GO:0055037/GO:0005886, considering
    uptake and receptor-associated pools of a secreted protein. Trace the exact relationship
    of K9IMD0 to the purified draculin in PMID:7740503 and the salivary proteomics
    identification PMID:23748026. Distinguish measurements on this protein from human
    lactoferrin and other transferrins; test any claimed loss of iron-binding sites
    or protease activity against sequence/structure. Anticoagulant specialization
    does not itself exclude another inherited function; missing transmembrane topology
    does not exclude peripheral association.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/DESRO/K9IMD0/K9IMD0-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Desmodus rotundus lactotransferrin/draculin K9IMD0\
    \ retains transferrin-family metal binding\n  GO:0046872, iron/monoatomic ion\
    \ transport GO:0006826/GO:0006811, serine-type peptidase/peptidase/hydrolase\n\
    \  activity GO:0008236/GO:0008233/GO:0016787 and proteolysis GO:0006508, antibacterial\
    \ humoral response\n  GO:0019731, defense response to bacterium GO:0042742 and\
    \ immune system process GO:0002376. Evaluate\n  these independently of its anticoagulant\
    \ role. Separately assess early/recycling endosome and plasma-membrane\n  association\
    \ GO:0005769/GO:0055037/GO:0005886, considering uptake and receptor-associated\
    \ pools of a\n  secreted protein. Trace the exact relationship of K9IMD0 to the\
    \ purified draculin in PMID:7740503 and\n  the salivary proteomics identification\
    \ PMID:23748026. Distinguish measurements on this protein from\n  human lactoferrin\
    \ and other transferrins; test any claimed loss of iron-binding sites or protease\
    \ activity\n  against sequence/structure. Anticoagulant specialization does not\
    \ itself exclude another inherited function;\n  missing transmembrane topology\
    \ does not exclude peripheral association.\nfocus_type: function_assignment\n\
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

- **Organism code:** DESRO
- **Taxon:** Desmodus rotundus (NCBITaxon:9430)
- **Gene directory:** K9IMD0
- **Gene symbol:** K9IMD0
- **UniProt accession:** K9IMD0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** lactotransferrin-functions-and-draculin-specialization
- **Source file:** genes/DESRO/K9IMD0/K9IMD0-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Desmodus rotundus lactotransferrin/draculin K9IMD0 retains transferrin-family metal binding GO:0046872, iron/monoatomic ion transport GO:0006826/GO:0006811, serine-type peptidase/peptidase/hydrolase activity GO:0008236/GO:0008233/GO:0016787 and proteolysis GO:0006508, antibacterial humoral response GO:0019731, defense response to bacterium GO:0042742 and immune system process GO:0002376. Evaluate these independently of its anticoagulant role. Separately assess early/recycling endosome and plasma-membrane association GO:0005769/GO:0055037/GO:0005886, considering uptake and receptor-associated pools of a secreted protein. Trace the exact relationship of K9IMD0 to the purified draculin in PMID:7740503 and the salivary proteomics identification PMID:23748026. Distinguish measurements on this protein from human lactoferrin and other transferrins; test any claimed loss of iron-binding sites or protease activity against sequence/structure. Anticoagulant specialization does not itself exclude another inherited function; missing transmembrane topology does not exclude peripheral association.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Desmodus rotundus lactotransferrin/draculin K9IMD0 retains transferrin-family metal binding
  GO:0046872, iron/monoatomic ion transport GO:0006826/GO:0006811, serine-type peptidase/peptidase/hydrolase
  activity GO:0008236/GO:0008233/GO:0016787 and proteolysis GO:0006508, antibacterial humoral response
  GO:0019731, defense response to bacterium GO:0042742 and immune system process GO:0002376. Evaluate
  these independently of its anticoagulant role. Separately assess early/recycling endosome and plasma-membrane
  association GO:0005769/GO:0055037/GO:0005886, considering uptake and receptor-associated pools of a
  secreted protein. Trace the exact relationship of K9IMD0 to the purified draculin in PMID:7740503 and
  the salivary proteomics identification PMID:23748026. Distinguish measurements on this protein from
  human lactoferrin and other transferrins; test any claimed loss of iron-binding sites or protease activity
  against sequence/structure. Anticoagulant specialization does not itself exclude another inherited function;
  missing transmembrane topology does not exclude peripheral association.
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

# AI Gene Review — Focused Hypothesis Report
## K9IMD0 (TRLF_DESRO), *Desmodus rotundus* lactotransferrin / **draculin**
### Focus: function_assignment — "lactotransferrin functions and draculin specialization"

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED / largely OVER-ANNOTATED (family carry-over).**

K9IMD0 is unambiguously **draculin**, and draculin has been explicitly established
as *"a mutated version of the lactotransferrin scaffold"* (PMID:23748026). The seed
hypothesis asks whether this protein still *directly* holds a battery of inherited
transferrin/lactoferrin GO terms independent of its anticoagulant specialization.
The evidence splits sharply:

- **Experimentally supported for THIS protein (retain, core):** secretion /
  extracellular region (GO:0005576, IDA) and **negative regulation of blood
  coagulation** (GO:0030195, IDA) — FXa/FIXa inhibition (PMID:9795244, PMID:10556567).
  Anticoagulation is the *primary, demonstrated* function.
- **Structurally defensible but not assayed in bat (retain only as ISS/IEA with a
  species caveat):** metal-ion binding (GO:0046872) — the **N-lobe iron site is fully
  conserved**; and serine-type peptidase (GO:0008236) — the **nucleophile Ser is
  conserved** but one essential catalytic residue is altered (Lys→Arg).
- **Weak / electronic carry-over (generalize, flag non-core, or remove pending
  evidence):** iron ion transport (GO:0006826/0006811) — the **C-lobe iron site is
  broken (Y454→D452)** so bilobal transport is degraded; antibacterial humoral
  response / defense-to-bacterium / immune-system-process (GO:0019731/0042742/0002376);
  and the endosome / recycling-endosome / plasma-membrane locations
  (GO:0005769/0055037/0005886), which derive from mammalian lactoferrin **receptor
  recycling** and have no support for a secreted salivary bat protein.

**Most important caveat:** every non-anticoagulant term is IEA:TreeGrafter or a
family keyword — none rests on a direct assay of draculin. The seed's framing is
correct that "anticoagulant specialization does not exclude inherited functions,"
but the molecular evidence shows *active degradation* of two ancestral active sites
(C-lobe iron Tyr; catalytic Lys of the protease dyad), so inheritance cannot be
assumed and should be curated conservatively.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID:23748026 | Structural/evolutionary (proteome+transcriptome) | Qualifies (identity) | K9IMD0 = purified draculin | Draculin "established… a mutated version of the lactotransferrin scaffold"; large sequence stretch recovered | *D. rotundus* submaxillary gland | High for identity; implies functional divergence |
| PMID:7740503 | Direct assay (purification) | Supports (secreted anticoagulant) | Draculin is a secreted salivary anticoagulant glycoprotein | Purified ~88 kDa glycoprotein, the saliva anticoagulant factor | *D. rotundus* saliva | High; partial characterization only |
| PMID:9795244 | Direct assay (biochemistry) | Supports (core function) | Anticoagulation | Inhibits FIXa and FXa; glycosylation-dependent activity | Native draculin | High |
| PMID:10556567 | Direct assay (kinetics) | Supports (core function) | FXa inhibition mechanism | Tight-binding, noncompetitive FXa inhibitor, Ki≈14.8 nM | Purified draculin | High |
| PMID:23411029 | Localization/expression (RNA-seq + LC-MS/MS) | Qualifies | Where/what class | "Lactotransferrin" among accessory-gland **antimicrobials**; secreted | *D. rotundus* glands | Medium; grouping ≠ functional assay |
| This report (align vs P02788) | Computational (structural/evolutionary) | Qualifies/partly refutes | Iron-binding retained? | N-lobe Fe ligands (D79,Y111,Y211,H272)+carbonate conserved; **C-lobe Y454→D452 lost**; 72% id | Sequence analysis | Medium-high; prediction, not binding assay |
| PMID:12535064 | Direct assay + mutagenesis | Qualifies | LF serine-protease mechanism | Catalytic dyad **Ser259+Lys73**; mutating either "dramatic decrease in proteolysis" | Human milk LF | High for human LF; not draculin |
| PMID:9770539 | Direct assay | Qualifies | LF antibacterial protease | N-lobe serine-protease activity cleaves *H. influenzae* IgA1 protease/Hap; blocked by serine-protease inhibitors | Human milk LF | High for human LF |
| PMID:11163480 | Direct assay | Qualifies | LF proteolysis site | LF cleaves Iga within the β-anchor region | Human LF | High for human LF |
| This report (dyad mapping) | Computational | Qualifies/partly refutes | Protease dyad conserved in draculin? | Ser278 conserved; **Lys92→Arg** (essential Lys altered); cationic N-term net +9 | Sequence analysis | Medium; predicts uncertain/reduced activity |

---

## GO Curation Implications (leads — require curator verification)

See `K9IMD0_GO_decision_table.csv` (computed provenance). Summary:

- **RETAIN (core, experimental):** GO:0005576 extracellular region (CC, IDA);
  GO:0030195 negative regulation of blood coagulation (BP, IDA). These are the
  protein's demonstrated identity and primary function.
- **RETAIN as ISS/IEA with explicit "not verified in *D. rotundus*" caveat, treat
  as non-core:** GO:0046872 metal ion binding (N-lobe site intact — a *bona fide*
  structural feature); GO:0008236 serine-type peptidase (nucleophile Ser conserved).
- **GENERALIZE / flag non-core / candidate for removal pending evidence:**
  GO:0006826 & GO:0006811 iron/ion transport (C-lobe site broken; no bat transport
  assay; a secreted protein without the receptor-recycling context); GO:0008233
  peptidase, GO:0016787 hydrolase, GO:0006508 proteolysis (downstream/too-broad
  parents of an unverified activity); GO:0019731/0042742/0002376
  antibacterial/defense/immune (family carry-over + transcriptomic grouping only).
- **REMOVE or down-weight to peripheral-IEA:** GO:0005769 early endosome,
  GO:0055037 recycling endosome, GO:0005886 plasma membrane — these describe the
  mammalian lactoferrin-receptor recycling itinerary and are not supported for a
  secreted salivary bat protein. (The seed's point that "missing TM topology does
  not exclude peripheral association" is fair, but there is *no positive evidence*
  of a membrane/endosomal pool of draculin.)

We avoid recommending "protein binding" as a terminal term; the informative core
terms are the anticoagulation BP and extracellular CC.

---

## Mechanistic Scope

- **Immediate molecular function (demonstrated):** noncompetitive tight-binding
  inhibition of activated coagulation factors Xa and IXa (Ki ≈ 15 nM), requiring
  correct glycosylation. This is the direct gene-product activity.
- **Inherited scaffold features (molecular, partly degraded):** a bilobal
  transferrin fold with an intact N-lobe metal-binding pocket and a broken C-lobe
  pocket; a conserved protease nucleophile Ser but altered catalytic Lys.
- **Downstream / inferred-only (not direct activity):** iron *transport* (a
  systemic/cellular process needing receptor recycling), antibacterial *response*,
  and endosomal/plasma-membrane *localization* — all inferred from human lactoferrin
  biology, not observed for draculin.

---

## Conflicts and Alternatives

- **Database carry-over (main risk):** TreeGrafter/PANTHER propagation and
  keyword→GO mapping assign the full lactoferrin repertoire to a protein the same
  authors call "mutated." Direct measurements exist only for anticoagulation.
- **Organism/paralog specificity:** all protease/antibacterial/iron-transport
  measurements are on **human** lactoferrin (PMID:12535064/9770539/11163480), not
  draculin. Two catalytic-site substitutions (C-lobe iron Tyr; protease Lys) argue
  against naive transfer.
- **Interpretation of the cationic N-terminus:** draculin retains a lactoferricin-like
  basic N-terminal stretch (net +9), so a peptide-based antimicrobial activity is
  *plausible* — a genuine alternative route to GO:0019731 that does not depend on
  the protease dyad. This remains untested.

---

## Knowledge Gaps

1. **Does draculin bind iron?** Checked: sequence/structure only (N-lobe intact,
   C-lobe Tyr lost). Matters because it gates GO:0046872/0006826. Resolve with a
   spectrophotometric Fe³⁺-saturation / urea-gel iron-binding assay on recombinant
   or salivary draculin.
2. **Does draculin have protease activity?** Checked: dyad mapping (Ser conserved,
   Lys→Arg). Matters for GO:0008236/0008233/0016787/0006508 and mechanistically for
   antibacterial. Resolve with an *H. influenzae* IgA1-protease/Hap cleavage assay
   ± serine-protease inhibitors, as in PMID:9770539.
3. **Is draculin antibacterial?** Checked: only transcriptomic grouping
   (PMID:23411029). Resolve with MIC/killing assays vs Gram+/– bacteria.
4. **Any endosomal/plasma-membrane pool?** Checked: none found; IEA only. Resolve
   with cell-surface receptor-binding / uptake assays in a relevant cell type.

---

## Discriminating Tests

- **Iron binding:** UV-vis (465 nm holo-transferrin band) and urea-PAGE mobility
  shift on apo vs Fe-loaded recombinant draculin; compare N-lobe-only vs full-length.
- **Protease:** recombinant draculin (and a draculin-R92K back-mutant) against
  IgA1-protease/Hap substrates; serine-protease-inhibitor panel.
- **Antibacterial:** killing/MIC assays and a draculin N-terminal peptide
  (lactoferricin-analog) test to separate peptide- vs protease-based activity.
- **Localization:** anti-draculin surface staining / receptor pulldown to test any
  membrane/endosomal association.
- **Comparative genomics:** map the C-lobe Y→D and protease K→R substitutions across
  bat lactoferrins to test whether they are draculin-lineage specialization vs
  species polymorphism.

---

## Curation Leads (require curator verification)

**Candidate references to attach (with exact snippets to verify):**
- PMID:23748026 — verify: *"…a very large sequence stretch of draculin and thus
  established that it is a mutated version of the lactotransferrin scaffold"*
  (identity of K9IMD0 = draculin; supports functional divergence).
- PMID:12535064 — verify: *"mutation of either Ser259 or Lys73 results in a dramatic
  decrease in proteolysis"* (basis of the serine-protease term; note Lys→Arg in bat).
- PMID:9770539 — verify: *"…localized to the N-lobe of the bilobed lactoferrin
  molecule and were inhibited by serine protease inhibitors…"* (protease↔antibacterial link).
- PMID:9795244 / PMID:10556567 — anticoagulant core function (FIXa/FXa inhibition).
- PMID:23411029 — lactotransferrin among accessory-gland antimicrobials (localization/expression, review-of-glands level).

**Candidate action changes:**
- Keep GO:0030195 and GO:0005576 as **core/experimental**.
- Downgrade GO:0006826/0006811, GO:0008233/0016787/0006508, GO:0019731/0042742/0002376
  to **non-core, IEA/ISS with caveats**; consider removing the CC endosome/PM terms
  (GO:0005769/0055037/0005886) unless localization evidence is produced.
- Where retained (GO:0046872 metal binding; GO:0008236 serine peptidase), annotate
  with an explicit note that the site is **structurally present but one essential
  residue diverges** and the activity is **unverified in *D. rotundus***.

**Suggested curator questions:** Is species-blinded IEA propagation appropriate for a
protein the source literature calls "mutated"? Should the C-lobe iron-site loss and
protease Lys→Arg be captured as sequence-feature caveats on the MF terms?

---

## Limitations

All non-anticoagulant conclusions rest on sequence/structure inference and
human-lactoferrin literature; no functional assay of draculin's iron binding,
protease, or antibacterial activity exists. Alignment-based ligand mapping (72%
identity to P02788) is robust for conserved columns but a single-substitution
functional prediction (e.g., Lys→Arg) is a hypothesis, not a measurement.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)