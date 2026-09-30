---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:12:35.756735'
end_time: '2026-08-31T08:30:41.707078'
duration_seconds: 1085.95
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: dca7
  gene_symbol: dca7
  uniprot_accession: O74763
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: core_function
  hypothesis_slug: core-function-schizosaccharomyces-pombe-dca7-forms-an-evolutionarily-conserved-scaffold-complex
  hypothesis_text: Schizosaccharomyces pombe Dca7 forms an evolutionarily conserved
    scaffold complex with a DYRK/Yak-family kinase
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Dca7 forms an evolutionarily\
    \ conserved scaffold complex with a DYRK/Yak-family\n  kinase\nfocus_type: core_function\n\
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
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: artifacts_conservation_provenance.md
  path: openscientist_artifacts/artifacts_conservation_provenance.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist conservation provenance
- filename: artifacts_evidence_matrix.csv
  path: openscientist_artifacts/artifacts_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: artifacts_go_decision_table.csv
  path: openscientist_artifacts/artifacts_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist go decision table
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
- **Gene directory:** dca7
- **Gene symbol:** dca7
- **UniProt accession:** O74763

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-schizosaccharomyces-pombe-dca7-forms-an-evolutionarily-conserved-scaffold-complex
- **Source file:**
- **Source selector:**

## Seed Hypothesis

Schizosaccharomyces pombe Dca7 forms an evolutionarily conserved scaffold complex with a DYRK/Yak-family kinase

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Dca7 forms an evolutionarily conserved scaffold complex with a DYRK/Yak-family
  kinase
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

# Dca7 (S. pombe, O74763) — Core-Function Hypothesis Review

**Hypothesis:** *Schizosaccharomyces pombe* Dca7 forms an evolutionarily conserved scaffold complex with a DYRK/Yak-family kinase.
**Focus type:** core_function • **Gene:** dca7 / SPBC17D11.08 / UniProt O74763 (YBE8_SCHPO) • **Iteration:** 1 of 3

---

## Executive Judgment

**Verdict: Supported (strong for orthology/conservation; moderate for direct in‑organism demonstration).**

The hypothesis is well supported by two independent lines of evidence that converge:

1. **Orthology/evolutionary evidence (strong).** Dca7 is the fission‑yeast ortholog of human **DCAF7/WDR68** (InterPro IPR045159 "DCAF7‑like"; PomBase 1:1 orthologs = human DCAF7 HGNC:30915 and *S. cerevisiae* YPL247C). WDR68/DCAF7 is a textbook, deeply conserved seven‑bladed WD40 β‑propeller **scaffold for DYRK‑family kinases** (DYRK1A/DYRK1B), documented in humans, zebrafish, insects and plants (PMID 21777625, 23349862, 25342745).
2. **Direct in‑organism interaction (moderate).** In *S. pombe*, Dca7 physically binds **ppk15** (SPAC823.03), whose catalytic domain is specifically the **Yak1‑type kinase domain** (CDD cd14212 PKc_YAK1) and whose orthologs are **human DYRK1A/DYRK1B and budding‑yeast Yak1 (YJL141C)**. The Dca7–ppk15 interaction is a verified binary yeast‑two‑hybrid hit from the fission‑yeast interactome (Vo et al., *Cell* 2016; PMID 26771498).

Thus the two fission‑yeast orthologs of the conserved human DCAF7–DYRK1A/1B pair physically associate in *S. pombe* — precisely the relationship the seed hypothesis predicts.

**Three‑species concordance (added Iteration 2).** STRING confirms the DCAF7–Yak/DYRK partnership independently in two yeasts: **S. cerevisiae Yak1–YPL247C** combined score **0.996 (experimental subscore 0.979)** and **S. pombe dca7–ppk15** combined **0.933 (experimental subscore 0.873)**. Together with the direct mammalian DCAF7/WDR68–DYRK1A/1B binding (PMID 21777625), the kinase–scaffold pairing is experimentally supported across human, budding‑yeast and fission‑yeast lineages.

**Sequence-conservation provenance (added Iteration 3).** Global Needleman–Wunsch/BLOSUM62 alignments computed this run: **Dca7 vs human DCAF7 = 44.2% identity** (328 aligned cols), **Dca7 vs Sc YPL247C = 37.5%**, and **human DCAF7 vs YPL247C = 42.7%**. This ~38–44% identity across the shared ~330‑residue WD40 β‑propeller core, preserved over ~1 billion years, confirms Dca7 is a bona‑fide DCAF7/WDR68 ortholog (not a name‑only match). See `artifacts/conservation_provenance.md`, `artifacts/evidence_matrix.csv`, `artifacts/go_decision_table.csv`.

**GO annotation state (added Iteration 2).** QuickGO for O74763 shows the molecular‑function and biological‑process roots are annotated **ND ("no data," GO_REF:0000015)** — Dca7 has **no experimental MF or BP annotation at all**. The only complex CC term, **GO:0080008 "Cul4‑RING E3 ubiquitin ligase complex," is evidence code ISS**, projected by similarity from human DCAF7 (UniProtKB:P61962). Nucleus (GO:0005634) is **IBA** (phylogenetic); cytoplasm/Golgi are IEA (UniProt‑SubCell). So the DYRK/Yak‑scaffold role is a genuine, unfilled annotation gap.

**Most important caveats.** (i) The pombe interaction rests on a **single high‑throughput Y2H method**, without in‑organism co‑IP or a demonstrated scaffolding *function* (PomBase characterisation status = "conserved unknown"). (ii) "Scaffold" is an **inference from orthology**, not a measured pombe activity. (iii) The **Cul4‑RING E3 complex CC annotation is an ISS carry‑over from human DCAF7**, not pombe evidence, and is a plausible over‑annotation relative to the better‑supported DYRK‑scaffold role.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| InterPro/UniProt O74763 (DB) | Computational (domain/family) | Supports | Dca7 is a DCAF7/WDR68‑family WD40 protein | IPR045159 "DCAF7‑like"; 7× WD40 (PF00400); β‑propeller fold | S. pombe protein | High for classification; family ≠ proof of pombe function |
| PomBase SPBC17D11.08 (DB) | Review/database + orthology | Supports | Orthology to DCAF7/WDR68 | 1:1 orthologs human DCAF7 (HGNC:30915), Sc YPL247C; "conserved in eukaryotes, single copy" | S. pombe | High orthology confidence; product note says "implicated in gene expression," status "conserved unknown" |
| PMID 26771498 (Vo et al., Cell 2016) | Interaction (binary Y2H) | **Supports (direct, in‑organism)** | Dca7 binds a DYRK/Yak kinase in pombe | Verified binary Y2H: dca7 ↔ **ppk15** | S. pombe interactome | Moderate: single method, HT screen; no co‑IP/functional follow‑up |
| PomBase SPAC823.03 / CDD (DB) | Computational (domain/orthology) | Supports | ppk15 is a Yak/DYRK kinase | Catalytic domain cd14212 **PKc_YAK1**; orthologs DYRK1A (HGNC:3091), DYRK1B (HGNC:3092), Yak1 (YJL141C) | S. pombe | High for family assignment |
| PMID 21777625 (Miyata & Nishida 2011) | Direct assay (co‑IP, mapping) | Supports | DCAF7/WDR68 is a conserved DYRK scaffold | WDR68 binds DYRK1A **and DYRK1B** (not DYRK2/3/4) via DYRK N‑terminus; conserved WD40 protein | Human/mammalian cells | High; different organism (conservation argument) |
| PMID 23349862 (Wang et al. 2013) | Mutant/localization (in vivo) | Supports | WDR68 acts as a scaffold with Dyrk1 | "highly conserved scaffolding protein… Ras‑Map3k‑Wdr68‑Dyrk1 signaling relay" | Zebrafish/C2C12 | High for scaffold concept; vertebrate context |
| PMID 25342745 (Miyata et al. 2014) | Direct assay (proteomics/structure model) | Supports + qualifies | WDR68 binding repertoire & fold | Binds DYRK1A, MEKK1, **and CUL4‑DDB1**; forms 7‑bladed β‑propeller | Human cells | High; shows CUL4‑DDB1 association also real in metazoa |
| STRING v12 (DB, aggregates experiments) | Interaction (multi-dataset) | **Supports (independent)** | DCAF7 ortholog binds Yak/DYRK in yeast | **Sc Yak1–YPL247C** combined 0.996 (exp 0.979); **Sp dca7–ppk15** combined 0.933 (exp 0.873) | S. cerevisiae & S. pombe | High experimental subscores; aggregated (specific primary paper not individually confirmed here) |
| This run (NW/BLOSUM62; O74763,P61962,Q12523) | Structural/evolutionary (computational) | Supports | Dca7 is a true DCAF7-family ortholog | Dca7–DCAF7 **44.2%** id (328 cols); Dca7–YPL247C 37.5%; DCAF7–YPL247C 42.7% | 3-species WD40 core | Genuine computation; global-alignment approximation |
| QuickGO O74763 (DB) | Review/database (annotation state) | Qualifies (over-annotation flag) | Current GO annotations & evidence | MF & BP = **ND**; GO:0080008 Cul4-RING = **ISS** from human DCAF7 (P61962); nucleus = IBA; cyto/Golgi = IEA | S. pombe | Authoritative annotation snapshot; shows scaffold role is unannotated |
| PomBase phenotypes (DB) | Mutant phenotype (HT) | Qualifies | Cellular role of dca7 | Δdca7: loss of viability in G0/stationary phase, decreased growth in glucose starvation; multiple stress‑resistance phenotypes | S. pombe | Downstream/pleiotropic; not a direct MF readout |

---

## GO Curation Implications (leads — require curator verification)

- **Molecular Function (add — currently ND).** dca7's MF root is annotated **ND ("no data")**, so there is no existing MF to retain or conflict with. Evidence supports adding a **kinase‑binding MF**. Recommended lead: **GO:0019901 "protein kinase binding"** (or the more specific **protein serine/threonine kinase binding**), evidence **IPI from PMID 26771498** (dca7↔ppk15) supported by orthology (**ISO** to DCAF7–DYRK1A/1B). More informative than "protein binding" and should be preferred. No "DYRK binding" child term exists; "protein kinase binding" is the best‑supported informative term.
- **Cellular Component (review; over‑annotation confirmed as ISS carry‑over).** QuickGO shows **GO:0080008 "Cul4‑RING E3 ubiquitin ligase complex" is evidence code ISS**, projected by similarity from human DCAF7 (UniProtKB:P61962) — **not** pombe experimental data. In metazoa WDR68 does associate with CUL4‑DDB1 (PMID 25342745), so it is not wrong in principle, but for *S. pombe* it should be treated as **not experimentally established / non‑core** and flagged for review. The **nucleus (GO:0005634) term is IBA** (phylogenetic), and UniProt independently annotates **cytoplasm + Golgi (IEA)**, so the subcellular picture is inference‑only and partner‑dependent; reconcile rather than assert nuclear localization. A **Dca7–ppk15 complex** CC could be a future lead but currently lacks a defined complex term.
- **Biological Process (candidate).** Consider a **"regulation of DYRK/Yak kinase signaling"**‑type BP by orthology, but keep as **non‑core/tentative** until pombe function is shown. Δdca7 phenotypes (G0/stationary‑phase viability, glucose‑starvation growth) are **downstream/pleiotropic** and should not be used to assign a direct MF/BP.
- **Net recommendation:** The seed hypothesis **should inform the review** by adding a kinase‑binding MF lead and by scrutinizing the CUL4 CC annotation. Do **not** upgrade "scaffold" to an asserted pombe function without functional data.

---

## Mechanistic Scope

- **Immediate molecular function being tested:** direct physical binding of the Dca7 WD40 β‑propeller to a DYRK/Yak‑family kinase (ppk15), i.e., a **kinase‑scaffold/adaptor** activity.
- **Direct (supported):** Dca7 = DCAF7/WDR68 ortholog; Dca7 binds ppk15 (Yak/DYRK ortholog) in pombe; the human orthologous pair binds directly and the interaction is conserved.
- **Downstream / not the tested activity:** Δdca7 growth and stress phenotypes; "implicated in gene expression"; anthocyanin/craniofacial/developmental outcomes of orthologs; possible CUL4‑DDB1 ubiquitin‑ligase adaptor role. These are pathway consequences or context‑specific roles, not the core scaffold activity.

---

## Conflicts and Alternatives

- **Competing molecular role (CUL4 adaptor).** The "DCAF7 = DDB1‑CUL4 associated factor" identity and the pombe CC annotation to a Cul4‑RING E3 complex offer an alternative/additional function. Literature (PMID 25342745) confirms WDR68–CUL4‑DDB1 association in metazoa, so this is a genuine dual role, not simply an error — but which role is "core" in pombe is unresolved. The **DYRK‑scaffold role is the more consistently documented, defining function** across the family.
- **Paralog/kinase‑identity nuance.** *S. pombe* has more than one CMGC/DYRK‑type kinase (e.g., **pom1**, MNB/DYRK subfamily; lkh1, LAMMER; prp4). The kinase captured interacting with Dca7 is specifically **ppk15 (Yak1/DYRK1A/1B ortholog)**, the expected DCAF7 partner — this argues *against* paralog confusion, but a curator should confirm ppk15 (not pom1) is the relevant partner.
- **Localization conflict.** UniProt (cytoplasm + Golgi) vs PomBase GO CC (nucleus) — WDR68 orthologs are pan‑cellular and shuttle with their partners (PMID 21777625, 23349862), so both may be partially correct in a partner‑dependent manner.
- **Method limitation.** A single Y2H hit could in principle be a false positive; however, dca7 has only two recorded physical partners (not a sticky hub), which raises confidence.

---

## Knowledge Gaps

1. **In‑organism validation of Dca7–ppk15.** Checked: only one HT Y2H (PMID 26771498). Matters because "scaffold" claims need biochemical confirmation. Resolve with **co‑IP / affinity‑MS of tagged Dca7 in pombe** and reciprocal ppk15 pulldown.
2. **Functional scaffolding readout.** Checked: PomBase status "conserved unknown"; no pombe assay. Matters for MF/BP assignment. Resolve by testing whether **Δdca7 alters ppk15 localization, stability, or substrate phosphorylation** (analogous to WDR68 controlling DYRK1A nuclear accumulation).
3. **Budding‑yeast anchor.** *Largely resolved (Iteration 2):* STRING shows **Yak1–YPL247C** with combined 0.996 / experimental 0.979, strongly supporting the conserved pairing in *S. cerevisiae*. Remaining gap: the **specific primary reference(s)** behind that experimental subscore were not individually confirmed (likely large AP‑MS/PCA datasets). Resolve via BioGRID/SGD YPL247C interaction records.
4. **CUL4 CC evidence code.** *Resolved (Iteration 2):* GO:0080008 is **ISS from human DCAF7 (P61962)** — a similarity carry‑over, confirming the over‑annotation concern. Curator action: decide whether to retain as non‑core ISS or remove pending pombe evidence.

---

## Discriminating Tests

- **Co‑IP / proximity‑labeling (BioID/TurboID) of Dca7 in *S. pombe*** to confirm ppk15 (and to distinguish ppk15 vs pom1 as the partner).
- **AlphaFold‑Multimer / AF3 modeling of Dca7–ppk15** vs Dca7–DDB1 to compare interface plausibility (a fast in‑silico discriminator between the DYRK‑scaffold and CUL4‑adaptor hypotheses).
- **Structure‑guided mutagenesis** of the Dca7 β‑propeller "top face" (the DYRK‑binding surface in DCAF7) to test whether it is required for ppk15 binding and for Δdca7 phenotypes.
- **Phospho‑proteomics of Δdca7 vs WT** to test whether Dca7 modulates ppk15/Yak‑dependent phosphorylation (functional scaffolding).
- **Cross‑complementation:** can human DCAF7 or the Dca7–ppk15 pair reconstitute known DYRK‑scaffold outputs?

---

## Curation Leads (require curator verification)

- **Candidate references to verify:**
  - PMID **26771498** (Vo et al., *Cell* 2016) — verify the exact Dca7↔ppk15 binary Y2H record in the supplementary interactome / BioGRID.
  - PMID **21777625** (Miyata & Nishida 2011) — snippet: *"DYRK1A and DYRK1B, but not DYRK2, DYRK3, or DYRK4, bound to endogenous and expressed WDR68."*
  - PMID **23349862** (Wang et al. 2013) — snippet: *"Wdr68 is a highly conserved scaffolding protein… A Ras‑Map3k‑Wdr68‑Dyrk1 signaling relay…"*
  - PMID **25342745** (Miyata et al. 2014) — snippet: *"WDR68 is an evolutionarily conserved WD40 repeat protein that binds to several proteins, including … (DYRK1A), … (MEKK1), and Cullin4‑damage‑specific DNA‑binding protein 1 (CUL4‑DDB1)."*
- **Candidate GO term changes:**
  - **Add MF:** GO:0019901 *protein kinase binding* (or protein serine/threonine kinase binding) — evidence IPI (PMID 26771498) + ISO (DCAF7). Preferred over "protein binding."
  - **Review CC:** GO:0080008 *Cul4‑RING E3 ubiquitin ligase complex* — flag as name/orthology‑based; confirm evidence code; consider demoting to non‑core for pombe. Reconcile nucleus (GO) vs cytoplasm/Golgi (UniProt).
  - **Optional BP (tentative, non‑core):** regulation of DYRK/Yak kinase signaling — by orthology only.
- **Suggested questions for curator:** Is ppk15 (not pom1) the intended DYRK/Yak partner? Is the Cul4 complex annotation experimentally grounded in pombe or an IEA carry‑over? Should Dca7's core function be recorded as "DYRK‑kinase scaffold/adaptor" pending functional data?
- **Suggested experiments:** pombe co‑IP/BioID of Dca7; AF‑Multimer Dca7–ppk15; Δdca7 phospho‑proteomics; propeller‑surface mutants.

---

### Provenance
All database results were retrieved programmatically this run: UniProt REST (O74763), PomBase API (SPBC17D11.08, SPAC823.03, SPAC25A8.01c), InterPro/CDD annotations, and NCBI eSummary for PMIDs. Interaction counts and orthology mappings are quoted directly from those queries. Human functional claims are from the cited primary papers (PMIDs above). No results were fabricated; where a resource was not queried (e.g., SGD YPL247C–Yak1), it is listed as a knowledge gap.


## Artifacts

- [OpenScientist conservation provenance](openscientist_artifacts/artifacts_conservation_provenance.md)
- [OpenScientist evidence matrix](openscientist_artifacts/artifacts_evidence_matrix.csv)
- [OpenScientist go decision table](openscientist_artifacts/artifacts_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
