---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T03:44:15.198879'
end_time: '2026-09-21T04:10:04.426007'
duration_seconds: 1549.23
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: ATG2A
  gene_symbol: ATG2A
  uniprot_accession: Q2TAZ0
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0034727
  hypothesis_text: Human ATG2A participates in piecemeal microautophagy of the nucleus
    (GO:0034727), inherited via PANTHER node PTN000324023 from yeast ATG2. Determine
    whether the lipid-transfer and membrane-tethering machinery participates in this
    specific microautophagic route in mammals, versus macroautophagic nucleophagy
    or other selective autophagy routes. Inspect the source process and target conservation;
    lipid-supply participation does not require ATG2A to recognize nuclear cargo directly.
    Distinguish a demonstrated lineage restriction or loss from absence of target
    experiments.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/ATG2A/ATG2A-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human ATG2A participates in piecemeal microautophagy\
    \ of the nucleus (GO:0034727), inherited\n  via PANTHER node PTN000324023 from\
    \ yeast ATG2. Determine whether the lipid-transfer and membrane-tethering\n  machinery\
    \ participates in this specific microautophagic route in mammals, versus macroautophagic\
    \ nucleophagy\n  or other selective autophagy routes. Inspect the source process\
    \ and target conservation; lipid-supply\n  participation does not require ATG2A\
    \ to recognize nuclear cargo directly. Distinguish a demonstrated\n  lineage restriction\
    \ or loss from absence of target experiments.\nfocus_type: function_assignment\n\
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
citation_count: 12
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
artifacts:
- filename: artifacts_ATG2A_GO_decision_table.csv
  path: openscientist_artifacts/artifacts_ATG2A_GO_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ATG2A GO decision table
- filename: artifacts_ATG2A_PMN_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_ATG2A_PMN_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ATG2A PMN evidence matrix
- filename: artifacts_PMN_taxonomy_provenance.md
  path: openscientist_artifacts/artifacts_PMN_taxonomy_provenance.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist PMN taxonomy provenance
- filename: artifacts_orthology_provenance.md
  path: openscientist_artifacts/artifacts_orthology_provenance.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist orthology provenance
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
- **Gene directory:** ATG2A
- **Gene symbol:** ATG2A
- **UniProt accession:** Q2TAZ0

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0034727
- **Source file:** genes/human/ATG2A/ATG2A-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human ATG2A participates in piecemeal microautophagy of the nucleus (GO:0034727), inherited via PANTHER node PTN000324023 from yeast ATG2. Determine whether the lipid-transfer and membrane-tethering machinery participates in this specific microautophagic route in mammals, versus macroautophagic nucleophagy or other selective autophagy routes. Inspect the source process and target conservation; lipid-supply participation does not require ATG2A to recognize nuclear cargo directly. Distinguish a demonstrated lineage restriction or loss from absence of target experiments.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human ATG2A participates in piecemeal microautophagy of the nucleus (GO:0034727), inherited
  via PANTHER node PTN000324023 from yeast ATG2. Determine whether the lipid-transfer and membrane-tethering
  machinery participates in this specific microautophagic route in mammals, versus macroautophagic nucleophagy
  or other selective autophagy routes. Inspect the source process and target conservation; lipid-supply
  participation does not require ATG2A to recognize nuclear cargo directly. Distinguish a demonstrated
  lineage restriction or loss from absence of target experiments.
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

# AIGR Gene Hypothesis Deep Research — Final Report

## Target: Human ATG2A (UniProt Q2TAZ0) — GO:0034727 "piecemeal microautophagy of the nucleus"

**Focus type:** function_assignment · **Hypothesis slug:** function-hypothesis-go-0034727
**Source:** genes/human/ATG2A/ATG2A-ai-review.yaml (free-text)
**Seed:** Human ATG2A participates in piecemeal microautophagy of the nucleus (GO:0034727), inherited via PANTHER node PTN000324023 from yeast ATG2.

---

## Summary

**Verdict: Over-annotated / refuted as a direct, applicable function assignment.** The annotation of human ATG2A with **GO:0034727 "piecemeal microautophagy of the nucleus" (PMN)** is an **IBA-only phylogenetic carry-over from budding yeast** and should be treated as **non-core and a candidate for removal** in the ATG2A curated review. The human ATG2A GO:0034727 record carries evidence code **IBA**, `assignedBy=GO_Central`, `reference=GO_REF:0000033` (PAINT phylogenetic annotation), and `withFrom=PANTHER:PTN000324023` plus the yeast ATG2 gene (SGD:S000005186). That is precisely the phylogenetic propagation the seed hypothesis flagged. There is **no experimental (IDA/IMP/IGI/EXP) support** for PMN in human ATG2A, or in any metazoan.

The seed asked a sharp question: does ATG2A's lipid-transfer/membrane-tethering machinery participate in this *specific* microautophagic route in mammals, and is any absence a *demonstrated lineage restriction* or merely a gap in target experiments? The evidence points firmly to a **demonstrated lineage restriction**. PMN is a fungal-specific process defined at the **nucleus–vacuole (NV) junction**, which is built by the direct **Nvj1–Vac8** interaction and requires a **vacuole**. QuickGO shows that **all 44 experimental-evidence PMN annotations are in *Saccharomyces cerevisiae* (100%)**. PANTHER v19 (positive-control validated by yeast ATG2 → human ATG2A/ATG2B) shows that **NVJ1 and VAC8 have no human ortholog**, while ATG2 is conserved. Because the scaffolds that make PMN a distinct microautophagic route are absent from the human lineage, the term cannot biologically apply to human ATG2A — regardless of the fact that ATG2's own lipid-supply subunit is conserved.

Human ATG2A's genuine, experimentally supported function is **macroautophagic lipid transfer and membrane tethering** at ER–phagophore contact sites. Every direct-evidence GO annotation on Q2TAZ0 describes macroautophagy. The only mammalian nuclear-degradation events that are actually documented (lamin B1/LMNB1, SIRT1 turnover) are **LC3-dependent macroautophagic nucleophagy** — a *different* process and GO term from microautophagic PMN, and one whose dependence on ATG2A is itself untested. The recommended curation lead is therefore: **mark GO:0034727 non-core / remove**, retain the macroautophagy lipid-transfer core, and do **not** substitute a nucleophagy term without independent experimental support.

---

## Key Findings

### Finding F001 — ATG2A's direct/experimental function is macroautophagic lipid transfer; PMN is IBA-only

UniProt Q2TAZ0 (ATG2A, *Homo sapiens*) carries 17 GO cross-references. Every **experimental / direct-evidence** annotation describes **macroautophagy**, not microautophagy of the nucleus:

- GO:0120013 **lipid transfer activity** (IDA)
- GO:0000045 **autophagosome assembly** (IMP)
- GO:0034045 **phagophore assembly site membrane** (EXP)
- GO:0005789 **endoplasmic reticulum membrane** (EXP)
- GO:0044232 **organelle membrane contact site** (IDA)
- GO:2000786 **positive regulation of autophagosome assembly** (IDA)

By contrast, **GO:0034727 (PMN)** is annotated **only** as IBA:GO_Central — phylogenetic inference. It sits in a cluster of selective-autophagy *process* terms (pexophagy, reticulophagy, glycophagy, mitophagy) that are all inherited by ancestry with no human experimental support. These are generic consequences of ATG2A being core autophagy machinery, not evidence of a demonstrated PMN role.

The core molecular activity is established directly. In [PMID: 31271352](https://pubmed.ncbi.nlm.nih.gov/31271352/), *The autophagic membrane tether ATG2A transfers lipids between membranes*, the authors "demonstrate that human ATG2A is a lipid transfer protein. ATG2A can extract lipids from membrane vesicles and unload them to other vesicles," acting most efficiently when it tethers two membranes; recruitment is via the PI3P effectors WIPI4/WIPI1. [PMID: 33850023](https://pubmed.ncbi.nlm.nih.gov/33850023/) frames ATG2 as the protein "proposed to transfer bulk lipid from the endoplasmic reticulum (ER) during autophagosome biogenesis" — i.e., ER-to-phagophore bulk lipid transfer during macroautophagy, with no requirement that ATG2 recognize nuclear cargo. This is reinforced by [PMID: 38622126](https://pubmed.ncbi.nlm.nih.gov/38622126/), which shows ANKFY1 recruits ATG2A to PI3P-enriched endosomes to donate lipid to phagophores, again a macroautophagy function.

**Interpretation.** ATG2A's core, experimentally supported function is a lipid-transfer/membrane-tether activity feeding phagophore expansion in macroautophagy. PMN is not part of this experimentally supported core in humans.

### Finding F002 — GO:0034727 has experimental support exclusively in *S. cerevisiae* via fungal-specific NV-junction machinery absent in mammals

QuickGO reports **59,856 total annotations** for GO:0034727, but restricting to experimental evidence (ECO:0000269 EXP and descendants) leaves **44 annotations, all in *S. cerevisiae* (taxon 559292; 100%)**. The experimentally annotated PMN gene set is a fungal cast: yeast ATG2 plus **NVJ1, VAC8, OSH1–7**, the core ATG1–18 machinery, and vacuolar fusion genes (VAM3/6/7, VPS41, YPT7). All non-yeast PMN annotations — including human ATG2A — are **IEA/IBA only**.

Mechanistically, PMN is degradation of the nucleus by **micro**autophagy at **NV junctions** formed by the direct Nvj1 (perinuclear ER)–Vac8 (vacuole) interaction. [PMID: 18701704](https://pubmed.ncbi.nlm.nih.gov/18701704/) states that "Piecemeal microautophagy of the nucleus (PMN) occurs in *Saccharomyces cerevisiae* at nucleus-vacuole (NV) junctions and results in the pinching-off and release into the vacuole of nonessential portions of the nucleus." [PMID: 28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/) shows that "Disruption of the Nvj1p-Vac8p interaction results in the loss of tight NVJs, which impairs piecemeal microautophagy of the nucleus" — the route is strictly junction-dependent. [PMID: 20943953](https://pubmed.ncbi.nlm.nih.gov/20943953/) further shows PMN requires the vacuolar V-ATPase electrochemical gradient and Osh1p, and forms a vacuolar diffusion barrier — all fungal features.

Mammals have **no vacuole** and **no Nvj1/Vac8 orthologs** (Finding F003), so the specific microautophagic route named by GO:0034727 cannot occur in human cells. The mammalian nuclear-degradation events that *are* documented are **macroautophagic (LC3-dependent)**: [PMID: 33292048](https://pubmed.ncbi.nlm.nih.gov/33292048/) identifies "the nuclear lamina protein LMNB1 (lamin B1) as a nuclear autophagy substrate in primary human cells," and describes SIRT1 as a nuclear autophagy substrate — a process mechanistically distinct from yeast microautophagic PMN.

**Interpretation.** GO:0034727 is a **yeast-specific term** at the experimental level. Its cross-species propagation onto human ATG2A conflates a fungal microautophagic route with the (mechanistically unrelated) mammalian macroautophagic nucleophagy.

### Finding F003 — PMN junction-defining proteins Nvj1 and Vac8 have no human ortholog, while ATG2 is conserved (PANTHER v19)

The single human ATG2A (UniProtKB:Q2TAZ0) GO:0034727 annotation is **evidence=IBA**, `assignedBy=GO_Central`, `reference=GO_REF:0000033` (PAINT), `withFrom=PANTHER:PTN000324023` and SGD:S000005186 (yeast ATG2) — pure phylogenetic propagation from yeast ATG2, exactly as the seed hypothesis anticipated.

An orthology test was run against the PANTHER v19 ortholog API (yeast taxon 559292 → human 9606), validated with a positive control:

| Query protein (yeast) | UniProt | Human ortholog returned? | Result |
|---|---|---|---|
| ATG2 (positive control) | P53855 | **Yes** — ATG2A (Q2TAZ0, least-diverged), ATG2B (Q96BY7) | Conserved |
| NVJ1 (NV-junction ER protein) | P38881 | **None** | No human ortholog |
| VAC8 (NV-junction vacuolar protein) | P39968 | **None** | No human ortholog |

(An initial NVJ1 lookup mistakenly used P32602, which is actually SEC17/α-SNAP; this was corrected to the verified NVJ1 accession P38881. All accessions were checked in UniProt.)

The two proteins that **define** the PMN NV junction have **no human ortholog**, while ATG2 itself is well conserved. Combined with F002, this resolves the seed's central question — "demonstrated lineage restriction or loss vs. absence of target experiments" — decisively toward **demonstrated lineage restriction**: the scaffold that makes PMN a distinct microautophagic route is absent from the human lineage.

**Interpretation.** ATG2 conservation is real, but it does not carry the PMN process with it, because PMN is defined by junction machinery (Nvj1/Vac8) and an organelle (the vacuole) that mammals lack. Propagating GO:0034727 to ATG2A on the strength of ATG2 orthology alone is a category error.

---

## Mechanistic Model / Interpretation

The core issue is that **ATG2 conservation ≠ PMN conservation.** ATG2 is a shuttle/tether that supplies lipid to a growing membrane; the *identity of the degradative route* is set by other, non-conserved components.

```
  YEAST (S. cerevisiae)                        HUMAN (H. sapiens)
  ---------------------                        ------------------
  Perinuclear ER ── Nvj1 ─┐                    ER ──────────────┐
                          │ NV junction              (no Nvj1)  │
  Vacuole ────────  Vac8 ─┘  (Velcro)          (NO VACUOLE)     │
        │                                                       │
        │  PMN = MICROautophagy                                 │
        ▼  nucleus pinched into vacuole                         ▼
  GO:0034727 (experimental, 44/44 = yeast)     Macroautophagy: phagophore
  Requires: vacuole + Nvj1–Vac8 + ATG core     expansion via ATG2A lipid transfer
                                               from ER (WIPI4/WIPI1, PI3P)
        ATG2  ── conserved ──────────────────► ATG2A / ATG2B
        Nvj1  ── NO human ortholog ──────────► (absent)
        Vac8  ── NO human ortholog ──────────► (absent)

  Mammalian nuclear degradation that IS documented:
  LMNB1 (lamin B1), SIRT1 turnover → LC3-dependent MACROautophagic nucleophagy
  (a DIFFERENT GO term than microautophagic PMN)
```

**Where ATG2A actually acts (human, experimentally supported):**

| Layer | Term | Evidence | Process |
|---|---|---|---|
| Molecular function | GO:0120013 lipid transfer activity | IDA | Macroautophagy |
| Cellular component | GO:0005789 ER membrane; GO:0034045 phagophore assembly site membrane; GO:0044232 organelle MCS | EXP/IDA | Macroautophagy |
| Biological process | GO:0000045 autophagosome assembly; GO:2000786 positive regulation of autophagosome assembly | IMP/IDA | Macroautophagy |
| Biological process | **GO:0034727 PMN** | **IBA only** | **fungal microautophagy — not applicable** |

Even granting the seed's fair point that "lipid-supply participation does not require ATG2A to recognize nuclear cargo directly," the route still requires an NV junction and a vacuole to *be* PMN. Absent those, any ATG2A lipid-transfer contribution to a mammalian nuclear-degradation event would be captured by macroautophagy/nucleophagy terms, not by GO:0034727.

---

## Evidence Base

| Citation | Evidence type | Supports/Refutes/Qualifies/Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 31271352](https://pubmed.ncbi.nlm.nih.gov/31271352/) | Direct in vitro assay | Refutes (redirects to macroautophagy) | ATG2A's core molecular function | Human ATG2A extracts/transfers lipids between vesicles; tether-enhanced; WIPI4/WIPI1-recruited | Recombinant human ATG2A + liposomes | High; in vitro only |
| [PMID: 33850023](https://pubmed.ncbi.nlm.nih.gov/33850023/) | Model/review | Qualifies | ATG2 role is bulk ER→phagophore lipid transfer | Positions ATG2 in macroautophagy lipid supply with scramblases (TMEM41B/VMP1/ATG9) | Conceptual/biochemical | Review-level orientation |
| [PMID: 38622126](https://pubmed.ncbi.nlm.nih.gov/38622126/) | Direct/interaction/mutant | Supports (macroautophagy) | ATG2A lipid-source flexibility | ANKFY1 recruits ATG2A to PI3P endosomes; ATG2A/B depletion impairs autophagosome growth | Human cells | High; unrelated to PMN |
| [PMID: 18701704](https://pubmed.ncbi.nlm.nih.gov/18701704/) | Mutant/morphological | Refutes (defines PMN as yeast-specific) | Where PMN occurs | PMN occurs in *S. cerevisiae* at NV junctions; requires core ATG genes | *S. cerevisiae* | High; organism-specific by design |
| [PMID: 28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/) | Structural + mutant | Refutes | PMN depends on Nvj1–Vac8 junction | Disrupting Nvj1p–Vac8p abolishes tight NVJs and impairs PMN | *S. cerevisiae* | High; machinery absent in mammals |
| [PMID: 20943953](https://pubmed.ncbi.nlm.nih.gov/20943953/) | Mechanistic/imaging | Refutes | PMN vesicle formation requirements | NV junctions need Nvj1p/Vac8p, V-ATPase gradient, Osh1p; form vacuolar diffusion barrier | *S. cerevisiae* | High; strongly fungal |
| [PMID: 19182523](https://pubmed.ncbi.nlm.nih.gov/19182523/) | Morphological (EM) | Refutes | PMN genetics/morphology | PMN ("micronucleophagy") requires core ATG genes at NV junctions | *S. cerevisiae* | High |
| [PMID: 15367582](https://pubmed.ncbi.nlm.nih.gov/15367582/) | Interaction/localization | Refutes | PMN cofactors | Osh1p targeted to NV junctions via Nvj1p; Osh1–7 needed for PMN vesicles | *S. cerevisiae* | High |
| [PMID: 15958487](https://pubmed.ncbi.nlm.nih.gov/15958487/) | Mutant | Refutes | PMN lipid requirements | VLCFA/Tsc13p at NV junctions shape PMN vesicle biogenesis | *S. cerevisiae* | High |
| [PMID: 31512555](https://pubmed.ncbi.nlm.nih.gov/31512555/) | Structural/biophysical | Refutes | Vac8 governs PMN vs Cvt | Vac8 quaternary states differentially regulate PMN and Cvt | *S. cerevisiae* | High; Vac8 absent in humans |
| [PMID: 33292048](https://pubmed.ncbi.nlm.nih.gov/33292048/) | Localization/substrate | Competing (alternative route) | Mammalian nuclear autophagy mechanism | LMNB1 and SIRT1 are substrates of LC3-dependent (macro)nuclear autophagy | Primary human cells | High; supports macroautophagic, not micro-PMN |
| [PMID: 38308641](https://pubmed.ncbi.nlm.nih.gov/38308641/) | Mechanistic | Competing (alternative route) | Mammalian nucleophagy mechanism | SUMOylated Lamin B1 binds LC3 → lysosomal delivery (macroautophagic nucleophagy) | Rodent/human neurons | Moderate; not ATG2A-specific |
| UniProt Q2TAZ0 / QuickGO annotation | Database | Refutes | Evidence basis of human PMN annotation | Human ATG2A GO:0034727 = IBA, GO_REF:0000033, withFrom PANTHER:PTN000324023 + yeast ATG2 | Database | High; direct record |
| QuickGO experimental filter | Database/computational | Refutes | Species distribution of PMN experiments | 44/44 experimental GO:0034727 annotations are *S. cerevisiae* | Database | High |
| PANTHER v19 ortholog API | Computational/evolutionary | Refutes | Conservation of PMN machinery | NVJ1, VAC8 → no human ortholog; ATG2 → ATG2A/B (positive control) | Computational | High; single-method — see limitations |

---

## GO Curation Implications (leads — require curator verification)

| GO ID | Term | Aspect | On ATG2A now | Lead action |
|---|---|---|---|---|
| **GO:0034727** | piecemeal microautophagy of the nucleus | BP | IBA:GO_Central | **REMOVE / treat as non-core** — over-propagated, lineage-restricted (fungal) term |
| GO:0044804 | autophagy of nucleus (nucleophagy) | BP | absent | **Do not add** without evidence (mammalian nucleophagy is macroautophagic; ATG2A role untested) |
| GO:0120013 | lipid transfer activity | MF | IDA | **RETAIN** — core MF |
| GO:0000045 | autophagosome assembly | BP | IMP | **RETAIN** — core BP |
| GO:2000786 | positive regulation of autophagosome assembly | BP | IDA | **RETAIN** |
| GO:0034045 | phagophore assembly site membrane | CC | EXP | **RETAIN** — core CC |
| GO:0005789 | endoplasmic reticulum membrane | CC | EXP | **RETAIN** |
| GO:0044232 | organelle membrane contact site | CC | IDA | **RETAIN** |

**Rationale.** The experimentally supported core of ATG2A is a **lipid-transfer / membrane-tether MF** acting at **ER–phagophore contact sites** in **macroautophagy**. GO:0034727 is one of several IBA selective-autophagy process terms inherited by ancestry; for a fungal-specific *microautophagic* route absent from the human cell, the term is best treated as **not supported / non-core**. We deliberately avoid recommending "protein binding" (GO:0005515) as a substitute; the informative core is the lipid-transfer MF and the macroautophagy CC/BP set, which are already present.

---

## Mechanistic Scope

- **Direct gene-product activity (human, experimentally supported):** intermembrane bulk **lipid transfer** and **membrane tethering**; ATG2A bridges ER (and PI3P endosomes, via ANKFY1) to the PI3P-marked phagophore, recruited by WIPI4/WIPI1, cooperating with scramblases (TMEM41B/VMP1/ATG9) to expand the phagophore. No nuclear-envelope targeting or nuclear-cargo recognition is documented (PMID 31271352, 33850023, 38622126).
- **PMN (yeast — the term's definitional scope):** microautophagic pinching of nuclear blebs directly into the vacuole at Nvj1–Vac8 junctions; core ATG genes (including yeast Atg2) are required for the terminal enclosure/release step — a lipid/membrane-machinery contribution, consistent with the seed's framing (PMID 18701704, 28533415, 20943953).
- **Downstream / different route (mammals):** macroautophagic nucleophagy of LMNB1 and SIRT1 (LC3-dependent). If ATG2A contributes here it does so as generic phagophore-lipid supply — its macroautophagy function — not as a dedicated nuclear program, and that contribution is currently untested (PMID 33292048, 38308641).

Separating the layers: the *immediate molecular function* (lipid transfer) is well supported and macroautophagic; PMN is a *cellular-route* claim that fails on machinery-conservation grounds; mammalian nucleophagy is a *distinct competing route* that would map to a different term.

---

## Conflicts and Alternatives

1. **Cross-lineage database carry-over (primary confounder).** GO:0034727 experimental support is 100% *S. cerevisiae* (44/44); the human annotation is IBA (GO_REF:0000033/PAINT), `withFrom` PANTHER:PTN000324023 + SGD:S000005186 (yeast ATG2) — confirmed by QuickGO, exactly matching the seed. This is legitimate automated inference being tested for biological applicability.
2. **ATG2 orthology is real but insufficient.** ATG2 conservation (positive control: yeast ATG2 → human ATG2A/ATG2B) might *seem* to justify inheriting all yeast ATG2 processes. It does not, because PMN's identity depends on Nvj1/Vac8/vacuole, which are not conserved.
3. **Process-type mismatch.** The mammalian counterpart of nuclear autophagy is **macro**autophagic, not **micro**autophagic (PMID 33292048, 38308641); even a bona fide mammalian ATG2A nuclear role would map to a different GO term.
4. **Not paralog confusion.** ATG2A vs ATG2B redundancy concerns macroautophagy; both would inherit the same IBA PMN term. The issue is term specificity/lineage applicability, not paralog mis-assignment.
5. **Method single-sourcing.** The ortholog conclusion rests on PANTHER v19 (positive-control validated). Orthology inference is method-dependent (see Limitations).

---

## Limitations and Knowledge Gaps

1. **Orthology inference is single-method.** NVJ1/VAC8 "no human ortholog" comes from PANTHER v19 with a validated positive control, but was not cross-checked here against OrthoDB, eggNOG, or InParanoid, nor by structure-based search. *Why it matters:* the central argument rests on machinery non-conservation. *Resolution:* confirm absence in ≥2 additional orthology resources and by Foldseek/structural search against the human proteome, since Nvj1/Vac8 are fast-evolving and sequence searches can miss remote homologs (Vac8 is an armadillo-repeat protein; humans have many ARM-repeat proteins, but functional NV-junction orthology is what matters).
2. **Does human ATG2A participate in macroautophagic nucleophagy?** Checked: no primary evidence found. A positive result would justify a *nucleophagy* (GO:0044804) lead — but not PMN. *Resolution:* ATG2A/B-KO + LMNB1/SIRT1 turnover assays.
3. **Is any microautophagy-of-nucleus route present in mammals at all?** Checked: literature shows only macroautophagic nuclear degradation. This bounds whether GO:0034727 could ever apply. *Resolution:* EM/live imaging of direct lysosomal engulfment of nuclear material.
4. **Absence of experiments ≠ proof of absence of function.** No study has tested whether ATG2A contributes lipid to any mammalian nuclear-membrane remodeling; the claim is specifically that the *PMN route* is inapplicable, not that ATG2A can never touch nuclear membranes.
5. **Database counts are time-stamped.** The 44/44 experimental-in-yeast figure reflects QuickGO at query time and could shift with future curation.

---

## Discriminating Tests

- **ATG2A/ATG2B double-KO human cells + starvation/senescence:** quantify LMNB1/SIRT1 nucleophagic flux (autophagosome/lysosome) to test any *macro*nucleophagy role (would support GO:0044804, not GO:0034727).
- **Multi-resource orthology + structural search:** confirm absence of Nvj1/Vac8 orthologs and vacuole-equivalent NVJ machinery in *Homo sapiens* via OrthoDB/eggNOG/InParanoid and Foldseek to formalize the lineage restriction.
- **Localization:** high-resolution imaging of endogenous ATG2A relative to the nuclear envelope during stress — absence of NE enrichment further argues against a dedicated nuclear route.
- **Literature sweep for metazoan PMN:** systematic keyword search for "piecemeal microautophagy of the nucleus" in any non-fungal organism (expected: none).
- **GO_Central PAINT review:** evaluate whether GO:0034727 IBA propagation should be taxon-constrained to Fungi at PANTHER node PTN000324023.

---

## Proposed Follow-up Actions / Curation Leads (verify before applying)

- **Candidate action:** mark GO:0034727 on ATG2A as **NOT accepted / non-core (remove)**; label its basis as IBA over-propagation of a fungal-specific process, with an explicit note that NV-junction machinery (Nvj1/Vac8) and the vacuole are absent from the human lineage.
- **Do not substitute** a broader nucleophagy/autophagy term for ATG2A on the basis of this annotation; any nucleophagy annotation would require independent experimental support.
- **Retain** the macroautophagy lipid-transfer core (GO:0120013 IDA; GO:0000045 IMP; GO:2000786 IDA; GO:0034045/GO:0005789/GO:0044232 CC).
- **Candidate references with exact snippets to cite/verify:**
  - [PMID: 31271352](https://pubmed.ncbi.nlm.nih.gov/31271352/) — "human ATG2A is a lipid transfer protein. ATG2A can extract lipids from membrane vesicles and unload them to other vesicles" (core MF; retain).
  - [PMID: 28533415](https://pubmed.ncbi.nlm.nih.gov/28533415/) — "Disruption of the Nvj1p-Vac8p interaction results in the loss of tight NVJs, which impairs piecemeal microautophagy of the nucleus" (PMN machinery is fungal).
  - [PMID: 18701704](https://pubmed.ncbi.nlm.nih.gov/18701704/) — PMN "occurs in *Saccharomyces cerevisiae* at nucleus-vacuole (NV) junctions" (lineage restriction).
  - [PMID: 33292048](https://pubmed.ncbi.nlm.nih.gov/33292048/) — "the nuclear lamina protein LMNB1 (lamin B1) as a nuclear autophagy substrate in primary human cells" (competing, macroautophagic route; different term).
  - Provenance: QuickGO — experimental PMN annotations = 44/44 *S. cerevisiae*; PANTHER v19 — NVJ1/VAC8 have no human ortholog.
- **Suggested curator questions:** (a) Should PMN IBA propagation be taxon-restricted to Fungi at PANTHER node PTN000324023? (b) Is a generic *nucleophagy* (GO:0044804) lead warranted for ATG2A, or should nuclear-autophagy terms be withheld pending mammalian evidence?
- **Suggested experiment:** ATG2A/B-KO nucleophagy flux assay (above).

---

## Bottom Line

Human ATG2A's demonstrated function is **macroautophagic lipid transfer/membrane tethering** at ER–phagophore contact sites. **GO:0034727 (piecemeal microautophagy of the nucleus) is a yeast-specific microautophagic process propagated to ATG2A by phylogeny only (IBA/PAINT, PANTHER:PTN000324023 + yeast ATG2); the defining machinery — a vacuole and the Nvj1–Vac8 junction — is absent in mammals (NVJ1/VAC8 have no human ortholog), a demonstrated lineage restriction rather than an untested cargo.** Recommend treating GO:0034727 as **over-annotated / non-core for human ATG2A (candidate for removal)**, while noting that a generic macroautophagic-nucleophagy role remains untested and must not be annotated without direct evidence.


## Artifacts

- [OpenScientist ATG2A GO decision table](openscientist_artifacts/artifacts_ATG2A_GO_decision_table.csv)
- [OpenScientist ATG2A PMN evidence matrix](openscientist_artifacts/artifacts_ATG2A_PMN_evidence_matrix.csv)
- [OpenScientist PMN taxonomy provenance](openscientist_artifacts/artifacts_PMN_taxonomy_provenance.md)
- [OpenScientist orthology provenance](openscientist_artifacts/artifacts_orthology_provenance.md)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)