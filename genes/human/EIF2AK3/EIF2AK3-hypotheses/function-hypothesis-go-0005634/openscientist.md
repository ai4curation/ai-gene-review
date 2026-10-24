---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-20T17:49:06.537184'
end_time: '2026-09-20T17:59:17.952843'
duration_seconds: 611.42
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: human
  gene: EIF2AK3
  gene_symbol: EIF2AK3
  uniprot_accession: Q9NZJ5
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_assignment
  hypothesis_slug: function-hypothesis-go-0005634
  hypothesis_text: Human EIF2AK3/PERK localizes to the nucleus (GO:0005634). Assess
    localization evidence, possible nuclear-envelope versus nucleoplasmic localization,
    relevant isoforms/fragments and stress context, and family inference. Its primary
    ER localization does not by itself exclude another location.
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/human/EIF2AK3/EIF2AK3-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Human EIF2AK3/PERK localizes to the nucleus (GO:0005634).\
    \ Assess localization evidence, possible\n  nuclear-envelope versus nucleoplasmic\
    \ localization, relevant isoforms/fragments and stress context,\n  and family\
    \ inference. Its primary ER localization does not by itself exclude another location.\n\
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
- **Gene directory:** EIF2AK3
- **Gene symbol:** EIF2AK3
- **UniProt accession:** Q9NZJ5

## Focus

- **Focus type:** function_assignment
- **Hypothesis slug:** function-hypothesis-go-0005634
- **Source file:** genes/human/EIF2AK3/EIF2AK3-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Human EIF2AK3/PERK localizes to the nucleus (GO:0005634). Assess localization evidence, possible nuclear-envelope versus nucleoplasmic localization, relevant isoforms/fragments and stress context, and family inference. Its primary ER localization does not by itself exclude another location.

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Human EIF2AK3/PERK localizes to the nucleus (GO:0005634). Assess localization evidence, possible
  nuclear-envelope versus nucleoplasmic localization, relevant isoforms/fragments and stress context,
  and family inference. Its primary ER localization does not by itself exclude another location.
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

# EIF2AK3/PERK Nuclear Localization (GO:0005634) — Focused Curation Report

**Gene:** EIF2AK3 (PERK) · Human · UniProt Q9NZJ5
**Hypothesis (seed):** Human EIF2AK3/PERK localizes to the nucleus (GO:0005634).
**Focus type:** function_assignment (does the gene product directly have GO:0005634?)
**Date:** 2026-09-21 · Iteration 1

---

## Executive Judgment

**Verdict: Over-annotated / weakly supported (non-core at best).**

The "nucleus" (GO:0005634) assignment for PERK is **not supported by any direct primary
experimental localization evidence**. In UniProt/QuickGO (Q9NZJ5) the single GO:0005634 term
carries the evidence code **IBA / GO_REF:0000033 (GO_Central/PANTHER PTN000113601)** — a
*phylogenetically inferred* prediction, not an experimental result. Its `withFrom` set is seeded by
soluble family paralogs that genuinely enter the nucleus — notably **PKR/EIF2AK2 (P19525)**, which
carries **EXP** nucleus annotations (PMID:21029237, 21072047) and IDA (PMID:26705305), and
**HRI/EIF2AK1 (Q9BQI3)** with IDA. PERK itself (and GCN2/Q9P2K8) have **IBA-only** nucleus calls.
Every experimentally- or manually-supported cellular-component annotation for PERK is ER-centric,
and UniProt's manually curated *Subcellular location* comment is exclusively
**"Endoplasmic reticulum membrane; Single-pass type I membrane protein."**

The one quasi-experimental nuclear signal for PERK itself is **Human Protein Atlas** immunofluorescence
(Nucleoplasm/Cytosol main; Mitochondria additional). However this is single-source, only **"Approved"**
reliability, and — tellingly — **HPA fails to detect the ER**, PERK's biochemically established
compartment, which points to antibody-specificity limitations rather than a robust nuclear pool.

Two independent lines of reasoning argue the term is a **paralog/family over-annotation**:

1. **Topology.** PERK is an integral single-pass type-I ER-membrane protein (luminal sensor 30–514,
   TM 515–535, cytoplasmic kinase domain 536–1116). A membrane-anchored protein cannot reside free
   in the nucleoplasm. Any nuclear-adjacent pool would be the **nuclear envelope** (outer nuclear
   membrane, continuous with ER → GO:0005635), with the kinase domain facing the cytoplasm — **not**
   the nucleoplasmic interior that GO:0005634 denotes.
2. **Family inference.** The soluble eIF2α-kinase paralogs do have genuine nuclear pools
   (PKR/EIF2AK2 in nucleus/nucleoli; GCN2). The GO_Central family tree therefore propagates a
   "nucleus" ancestral state that fits the soluble kinases but is inappropriate for the uniquely
   membrane-bound PERK.

**Caveat / what would change the call:** ER is continuous with the nuclear envelope, and PERK
functionally interacts with nuclear-envelope-associated factors (e.g., PARP16). If a curator wishes
to capture that, the correct term is **nuclear envelope (GO:0005635)** or ER, *not* nucleus
(GO:0005634). I found no primary paper demonstrating nucleoplasmic PERK.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| UniProt Q9NZJ5 / QuickGO (database record; retrieved 2026-09-21) | Database/annotation | **Refutes** (as direct evidence) | Is GO:0005634 experimentally supported for PERK? | GO:0005634 = **IBA / GO_REF:0000033 (GO_Central)** only; `withFrom` = PKR(P19525), HRI(Q9BQI3), GCN2 orthologs; curated CC comment = ER membrane, single-pass type I | Human, Swiss-Prot | High that basis is inferential; IBA ≠ experiment |
| QuickGO family check (P19525, Q9BQI3, Q9P2K8, Q9NZJ5) | Structural/evolutionary | **Competing / explains IBA** | Which family members drive the nucleus IBA? | PKR has **EXP** nucleus (PMID:21029237, 21072047) + IDA (PMID:26705305); HRI IDA; PERK & GCN2 **IBA-only** | Human paralogs | High; shows paralog-seeded propagation |
| Human Protein Atlas (ENSG00000172071; IF) | Localization | **Qualifies / weak-support** | Does PERK show a nuclear pool? | Nucleoplasm+Cytosol (main); reliability **"Approved"**; **no ER detected** | Human cell lines, antibody IF | Low–medium; single-source, misses ER (specificity concern) |
| UniProt Q9NZJ5 topology features | Structural/topology | **Qualifies/Refutes** | Can full-length PERK be nucleoplasmic? | Signal 1–29; lumenal 30–514; TM 515–535; cytoplasmic kinase 536–1116 → membrane-anchored | Human | High; topology well established |
| PMID 41406153 (2025) | Localization (paralog) | **Competing / explains IBA** | Do family paralogs localize to nucleus? | "a fraction of PKR maps to the nucleoli" | Human PKR/EIF2AK2 | Medium; about paralog, not PERK |
| PMID 29352251 (2018) | Localization (paralog) | **Competing / explains IBA** | PKR nuclear/cytoplasmic partition | "repartition of PKR in the cytoplasm and the nucleus" | PKR/EIF2AK2 | Medium; paralog |
| PMID 34094832 (2021) | Interaction/localization | **Qualifies** | PERK near nuclear envelope? | PARP16 "correlated with the nuclear envelope and the ER"; interacts with PERK/IRE1 | Vascular cells | Medium; supports NE/ER, not nucleoplasm |
| PMID 16352659 (2006) | Mutant phenotype | **Qualifies (ER role)** | PERK's cellular compartment of action | PERK−/− causes "distention and fragmentation of the ER"; ER Ca²⁺ signalling defects | Mouse secretory/muscle cells | High for ER function |
| PMID 26268696 (2015) | Interaction/localization | **Qualifies (ER role)** | PERK compartment | PERK is an "ER transmembrane protein"; binds ER-membrane TMEM33 | Breast cancer cells | High for ER membrane |
| PMID 16432136 (2006, review) | Review | **Qualifies** | ER–NE continuity | ER "is contiguous with the nuclear envelope" | Review | Orientation only |

---

## GO Decision Table

| GO term | Aspect | Current evidence for PERK | Recommendation (lead) |
|---|---|---|---|
| GO:0005634 nucleus | CC | IBA-only (GO_REF:0000033), paralog-seeded; HPA IF nucleoplasm at "Approved", misses ER | **Remove / down-weight — non-core, not directly supported** |
| GO:0005635 nuclear envelope | CC | Not currently annotated; ER is continuous with NE; PARP16 interaction (PMID:34094832) | Optional add **only** if a specificity-validated primary source appears |
| GO:0005789 ER membrane | CC | ISS + NAS (PMID:11907036) + TAS(Reactome) | **Retain (core)** |
| GO:0005783 endoplasmic reticulum | CC | IDA (PMID:9930704), IC (PMID:11907036), TAS | **Retain (core)** |
| GO:0044233 MAM contact site | CC | IDA (PMID:39116259) | **Retain** |
| GO:0005829 cytosol | CC | TAS(Reactome) — cytosolic kinase-domain face | **Retain (supportive)** |

## Isoform / fragment check (Iteration 3)

UniProt Q9NZJ5 annotates **a single isoform**, **one mature chain (30–1116)**, **no released
cytosolic fragment**, and a crude scan found **no classical monopartite NLS** (≥4 consecutive K/R).
The seed hypothesis's "relevant isoforms/fragments" route to the nucleus is therefore **not
supported by curated sequence features**.

## GO Curation Implications (leads — require curator verification)

- **GO:0005634 (nucleus, CC):** Recommend **remove or down-weight** as a stand-alone localization
  claim. It is IBA-only and conflicts with PERK's curated ER-membrane topology; it most likely
  reflects phylogenetic carry-over from the soluble paralogs (PKR/GCN2). Do **not** promote it to an
  experimental CC term.
- **If a nuclear-adjacent location must be captured:** the biologically defensible term is
  **GO:0005635 (nuclear envelope)** or retention of the existing ER terms — but only if a curator
  finds a primary localization paper; I did not.
- **Retain (well-supported):** GO:0005789 (ER membrane), GO:0005783 (ER, IDA),
  GO:0044233 (MAM contact site, IDA), GO:0005829/0005737 (cytosol/cytoplasm — the kinase domain's
  cytosolic face). These represent the gene product's primary location.

---

## Mechanistic Scope

The immediate molecular function of PERK is an **ER-membrane–resident eIF2α protein kinase**: its
luminal domain senses ER unfolded-protein load (via BiP release / direct binding), it
oligomerizes/autophosphorylates, and its cytosolic kinase domain phosphorylates eIF2α (Ser51) to
attenuate translation and induce ATF4. **Nuclear consequences of the pathway (ATF4/CHOP
transcription, NRF2 activation) are executed by downstream effectors that translocate to the
nucleus — not by PERK itself.** Attributing "nucleus" to PERK conflates the sensor with its
downstream transcriptional output.

---

## Conflicts and Alternatives

- **Paralog confusion (most likely explanation):** PKR/EIF2AK2 has documented nuclear/nucleolar
  pools; GO_Central's family-level inference plausibly propagated a "nucleus" state to PERK.
- **ER–NE continuity artifact:** Immunofluorescence perinuclear ER signal can be misread as
  "nuclear." GO:0048471 (perinuclear region) is already annotated (IEA) and captures this better.
- **Topology constraint:** For membrane-anchored PERK, nucleoplasmic residence is topologically
  incoherent; only the nuclear envelope (ER-continuous) is physically available.

---

## Knowledge Gaps

1. **Is there any *specific* primary paper showing nucleoplasmic PERK?** Checked UniProt CC, QuickGO,
   and PubMed; none found. HPA IF does report Nucleoplasm but at "Approved" reliability and without
   detecting the ER, so its antibody specificity is uncertain. Matters because HPA is currently the
   only experimental-type signal that could upgrade GO:0005634.
   *Resolve:* validate with a knockout-verified antibody (IF + subcellular fractionation), or
   confirm HPA antibody specificity against PERK-null cells.
2. **Does a proteolytically released PERK cytosolic fragment ever enter the nucleus?** Not
   established here. *Resolve:* look for cleavage/processing reports and fragment localization.
3. **Exact GO_Central IBA ancestor supporting the nucleus call.** Confirming it derives from PKR/GCN2
   would formally document the over-annotation. *Resolve:* inspect the PAINT/GO_Central family tree.

---

## Discriminating Tests

- **Subcellular fractionation + Western** (nuclear vs. ER/microsomal vs. cytosol) for endogenous PERK.
- **Confocal co-localization** of PERK with ER (calnexin), nuclear envelope (lamin B/emerin), and
  nucleoplasm markers, ± ER stress (thapsigargin/tunicamycin).
- **Human Protein Atlas** subcellular immunofluorescence review for EIF2AK3.
- **GO_Central/PAINT tree inspection** to confirm the IBA ancestor is a soluble nuclear paralog.

---

## Curation Leads (verify before acting)

- **Action change:** Mark GO:0005634 (nucleus) as **not supported by direct evidence (IBA-only)**;
  do not treat as core localization. Prefer removal or replacement with GO:0005635 (nuclear
  envelope) *only if* a primary source is found.
- **Candidate references to cite for the ER core location:** PMID 26268696 (PERK an ER transmembrane
  protein), PMID 16352659 (PERK ER function/phenotype).
- **Candidate references explaining the over-annotation:** PMID 41406153, PMID 29352251 (nuclear
  paralog PKR).
- **Suggested question for curator:** "Is the GO:0005634 term meant to capture nuclear-envelope/ER
  continuity? If so, GO:0005635 is more accurate; if nucleoplasm, no primary evidence exists."
- **Suggested experiment:** endogenous PERK fractionation + confocal, ± ER stress.

---

## Provenance (computed, live queries 2026-09-21)

- **UniProt REST (Q9NZJ5):** curated CC = "Endoplasmic reticulum membrane; Single-pass type I
  membrane protein"; topology signal 1–29, lumenal 30–514, TM 515–535, cytoplasmic 536–1116;
  single isoform; single chain 30–1116; no NLS by crude K/R scan.
- **QuickGO annotation API (Q9NZJ5):** GO:0005634 = **IBA / GO_REF:0000033 (GO_Central)** only;
  `withFrom` includes PKR (P19525), HRI (Q9BQI3), GCN2 orthologs (PANTHER PTN000113601).
  Family check: PKR has **EXP** nucleus (PMID:21029237, 21072047) + IDA (PMID:26705305);
  HRI IDA; PERK & GCN2 IBA-only.
- **Human Protein Atlas API (ENSG00000172071):** Subcellular = Nucleoplasm/Mitochondria/Cytosol;
  main = Nucleoplasm/Cytosol; Reliability(IF) = "Approved"; **ER not reported** (specificity concern).
- **PubMed:** no primary evidence for nucleoplasmic PERK; nuclear pools confirmed for paralog PKR.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)