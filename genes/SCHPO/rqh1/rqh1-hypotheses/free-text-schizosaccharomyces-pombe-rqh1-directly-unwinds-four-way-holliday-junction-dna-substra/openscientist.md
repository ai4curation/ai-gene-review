---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T12:22:47.983123'
end_time: '2026-09-01T12:37:53.964245'
duration_seconds: 905.98
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: rqh1
  gene_symbol: rqh1
  uniprot_accession: Q09811
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: free_text
  hypothesis_slug: free-text-schizosaccharomyces-pombe-rqh1-directly-unwinds-four-way-holliday-junction-dna-substra
  hypothesis_text: Schizosaccharomyces pombe Rqh1 directly unwinds four-way Holliday-junction
    DNA substrates, supporting GO:0009378 four-way junction helicase activity
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: genes/SCHPO/rqh1/rqh1-ai-review.yaml
  source_selector: free-text
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Rqh1 directly unwinds\
    \ four-way Holliday-junction DNA substrates,\n  supporting GO:0009378 four-way\
    \ junction helicase activity\nfocus_type: free_text\ncontext: []\nreference_id:\
    \ []"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 14
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
- **Gene directory:** rqh1
- **Gene symbol:** rqh1
- **UniProt accession:** Q09811

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** free-text-schizosaccharomyces-pombe-rqh1-directly-unwinds-four-way-holliday-junction-dna-substra
- **Source file:** genes/SCHPO/rqh1/rqh1-ai-review.yaml
- **Source selector:** free-text

## Seed Hypothesis

Schizosaccharomyces pombe Rqh1 directly unwinds four-way Holliday-junction DNA substrates, supporting GO:0009378 four-way junction helicase activity

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Rqh1 directly unwinds four-way Holliday-junction DNA substrates,
  supporting GO:0009378 four-way junction helicase activity
focus_type: free_text
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

# AIGR Gene Hypothesis Deep Research — *S. pombe* Rqh1 Four-Way Junction Helicase Activity (GO:0009378)

**Target gene:** rqh1 (UniProt Q09811), *Schizosaccharomyces pombe* (strain 972 / ATCC 24843), NCBITaxon:284812
**Seed hypothesis:** *S. pombe* Rqh1 directly unwinds four-way Holliday-junction DNA substrates, supporting GO:0009378 four-way junction helicase activity.
**Focus type:** free_text / function-assignment

---

## Summary

**Executive verdict: Partially / weakly supported — supported by orthology inference, not by direct experimental evidence.** The claim that Rqh1 possesses *four-way junction (Holliday-junction) helicase activity* (GO:0009378) rests entirely on phylogenetic propagation from experimentally characterized RecQ orthologues (human BLM, human WRN, and budding-yeast Sgs1), not on any direct biochemical assay of purified Rqh1 protein. The GO annotation of Q09811 for GO:0009378 carries evidence code **IBA (ECO:0000318, GO_REF:0000033, PAINT/GO_Central)**, with the "with/from" field naming human BLM (P54132), human WRN (Q14191), and Arabidopsis RecQ loci — i.e., the assignment is inferred from ancestral reconstruction, not measured in fission yeast.

By contrast, the **only** experimentally supported molecular-function annotation for Rqh1 is **GO:0043138 "3'–5' DNA helicase activity" (IDA:PomBase)**, which is backed by two independent direct biochemical characterizations of purified Rqh1p: Laursen et al. 2003 ([PMID: 12724426](https://pubmed.ncbi.nlm.nih.gov/12724426/)) and Ahmad et al. 2002 ([PMID: 12478586](https://pubmed.ncbi.nlm.nih.gov/12478586/)). Both studies demonstrated generic 3'→5' single-strand-displacement helicase activity on standard duplex/tailed substrates and **neither tested a four-way-junction or Holliday-junction substrate**. Targeted literature searches did not identify any primary paper demonstrating in-vitro four-way-junction unwinding or branch migration by purified Rqh1. Direct demonstration of Holliday-junction branch migration and double-Holliday-junction (dHJ) dissolution exists only for the orthologues BLM, Sgs1, and WRN.

Supporting the plausibility of the inference, *S. pombe* in-vivo genetics place Rqh1 firmly in pathways that process branched recombination intermediates — most notably a helicase-activity–dependent suppression of mitotic crossovers (Hope et al. 2007, [PMID: 17353272](https://pubmed.ncbi.nlm.nih.gov/17353272/)) — and a computed InterPro domain-architecture comparison confirms that Rqh1 conserves the full RecQ core, including the **RQC winged-helix domain (IPR018982)** and **HRDC domain (IPR002121)** that mediate structure-specific junction recognition in BLM/WRN/Sgs1. These are, however, biological-process (BP) phenotype inferences and structural/evolutionary inferences respectively — they raise prior confidence in the orthology call but do not constitute a direct molecular-function measurement. **Curation lead: retain GO:0009378 as an inferred annotation (IBA/ISS); do not upgrade it to an experimental evidence code; keep GO:0043138 as the directly evidenced molecular function.**

---

## Key Findings

### Finding 1 — GO:0009378 for Rqh1 is an orthology inference (IBA), not a direct assay

The UniProt/PomBase annotation of Q09811 assigns GO:0009378 "four-way junction helicase activity" with evidence code **IBA:GO_Central** (phylogenetic inference by ancestral-state reconstruction). The only experimentally supported molecular-function annotation for the same protein is GO:0043138 "3'–5' DNA helicase activity" with evidence code IDA:PomBase, derived from Laursen et al. 2003 ([PMID: 12724426](https://pubmed.ncbi.nlm.nih.gov/12724426/)), which characterized purified Rqh1 as a 3'→5' helicase and did not test four-way-junction substrates. Targeted PubMed searches combining "Rqh1" with "Holliday junction," "branch migration," and "branched substrate" biochemistry returned no primary paper describing such an assay. The direct four-way-junction / HJ branch-migration and dHJ dissolution activities are demonstrated only for the orthologues human BLM and *S. cerevisiae* Sgs1.

> Laursen et al. 2003 ([PMID: 12724426](https://pubmed.ncbi.nlm.nih.gov/12724426/)): *"We show that Rqh1, the single Schizosaccharomyces pombe homologue, is a 3'-to-5' helicase and exists with Top3 in a high-molecular-weight complex."*

> On the orthologue BLM ([PMID: 16670433](https://pubmed.ncbi.nlm.nih.gov/16670433/)): *"BLM also promotes branch migration of Holliday junctions."* — This is the directly demonstrated orthologue activity that is the basis of the orthology inference to Rqh1.

**Interpretation:** the four-way-junction MF term is a well-motivated *inference*, but it is not an experimental fact for the fission-yeast protein.

### Finding 2 — In-vivo *S. pombe* genetics support a helicase-dependent role for Rqh1 in processing recombination / four-way-junction intermediates

`rqh1Δ` cells show a ~4-fold increase in crossover frequency during mitotic double-strand-break repair, and this crossover suppression is dependent on Rqh1 helicase activity (Hope et al. 2007, [PMID: 17353272](https://pubmed.ncbi.nlm.nih.gov/17353272/)). Multiple additional studies describe Rqh1 as resolving/disassembling recombination joint molecules — e.g. [PMID: 39580958](https://pubmed.ncbi.nlm.nih.gov/39580958/) ("RecQ helicase Rqh1 resolves recombination intermediates") and [PMID: 31584934](https://pubmed.ncbi.nlm.nih.gov/31584934/) ("Rqh1-mediated disassembly of joint-molecules"). These are mutant-phenotype (IMP/IGI) inferences consistent with in-vivo action on branched/Holliday-junction-containing intermediates, but they do not directly demonstrate four-way-junction unwinding by the purified enzyme.

> Hope et al. 2007 ([PMID: 17353272](https://pubmed.ncbi.nlm.nih.gov/17353272/)): *"This suppression of crossover formation by Rqh1 is dependent on its helicase activity."*

**Interpretation:** the genetics tie Rqh1's helicase function to crossover control — a downstream consequence consistent with junction processing — but map onto a **biological-process** conclusion rather than a molecular-function assay.

### Finding 3 — Two independent direct assays show only generic 3'→5' helicase; the GO:0009378 IBA is propagated from experimental BLM/WRN annotations

QuickGO annotation provenance for Q09811 shows GO:0009378 = IBA (ECO:0000318), GO_REF:0000033 (PAINT), with/from human BLM (UniProtKB P54132), human WRN (UniProtKB Q14191), Arabidopsis RecQ loci (AT1G31360, AT4G35740), PANTHER family PTN000344873 — i.e., propagated from experimentally characterized RecQ orthologues, **not** from any Rqh1 experiment. The 3'–5' DNA helicase MF (GO:0043138) carries **two** independent IDA (ECO:0000314) references from PomBase: [PMID: 12724426](https://pubmed.ncbi.nlm.nih.gov/12724426/) (Laursen 2003) and [PMID: 12478586](https://pubmed.ncbi.nlm.nih.gov/12478586/) (Ahmad, Kaplan & Stewart 2002). Both demonstrate generic 3'→5' DNA helicase activity for purified Rqh1p; neither tested four-way-junction / Holliday-junction substrates. Ahmad 2002 additionally reports that helicase activity of Rqh1p is only partially required for its function.

> Ahmad et al. 2002 ([PMID: 12478586](https://pubmed.ncbi.nlm.nih.gov/12478586/)): *"Here we show that, like other RecQ family members, the Rqh1p protein displays 3' to 5' DNA helicase activity."*

> Ahmad et al. 2002 ([PMID: 12478586](https://pubmed.ncbi.nlm.nih.gov/12478586/)): *"unlike other RecQ family members, the helicase activity of Rqh1p is only partially required for its function."*

**Interpretation:** the experimental record for Rqh1 stops at generic 3'→5' helicase. The four-way-junction annotation is entirely a carry-over from experimentally validated orthologues, and the "partially required" caveat warns against treating any single helicase sub-activity as the sole core function.

### Finding 4 — Rqh1 conserves the RecQ RQC winged-helix module shared with BLM/WRN/Sgs1, structurally supporting the four-way-junction IBA inference

A computed InterPro domain-architecture comparison (via UniProt REST) across Rqh1 (Q09811), human BLM (P54132), human WRN (Q14191), human RECQ1 (P46063), and *S. cerevisiae* Sgs1 (P35187) shows that Rqh1 shares the full RecQ core: RecQ helicase family (IPR004589), P-loop NTPase (IPR027417), Helicase C-like (IPR001650), RecQ Zn-binding (IPR032284), the **RQC winged-helix domain (IPR018982)**, and **HRDC (IPR002121)** — with BLM, WRN, and Sgs1. The RQC winged-helix is the structural module implicated in structure-specific DNA / Holliday-junction recognition and branch migration in RecQ helicases; allosteric-inhibitor structures of BLM provide "a model for branch migration of Holliday junctions by BLM" ([PMID: 33647232](https://pubmed.ncbi.nlm.nih.gov/33647232/)).

**Interpretation:** Rqh1 possesses the machinery known to confer HJ recognition/branch-migration in its orthologues. This raises the prior probability that Rqh1 can act on four-way junctions but is structural/evolutionary evidence — it does not substitute for a direct assay.

---

## Mechanistic Model / Interpretation

The distinction that matters for curation is between **direct molecular-function evidence** and **inference** (phylogenetic, phenotypic, or structural). The evidence for Rqh1 stratifies cleanly:

```
                 EVIDENCE FOR Rqh1 four-way-junction helicase (GO:0009378)
  ┌───────────────────────────────────────────────────────────────────────────┐
  │ DIRECT MF ASSAY on purified Rqh1                                            │
  │   • 3'->5' DNA helicase (GO:0043138)  ── IDA  ── PMID 12724426, 12478586    │
  │   • four-way junction unwinding      ── NONE (never assayed)     ✗          │
  ├───────────────────────────────────────────────────────────────────────────┤
  │ IN-VIVO GENETICS (BP-level, phenotype)                                     │
  │   • helicase-dependent crossover suppression ── IMP ── PMID 17353272        │
  │   • resolves/disassembles joint molecules   ── IGI/IMP ─ PMID 39580958,     │
  │                                                          31584934           │
  ├───────────────────────────────────────────────────────────────────────────┤
  │ STRUCTURAL / EVOLUTIONARY (conserved machinery)                            │
  │   • RQC winged-helix (IPR018982) + HRDC (IPR002121) shared w/ BLM/WRN/Sgs1  │
  ├───────────────────────────────────────────────────────────────────────────┤
  │ ORTHOLOGUE DIRECT ASSAYS (the basis of the IBA)                            │
  │   • BLM: HJ branch migration                 ── PMID 16670433               │
  │   • BLM-TopoIIIα-BLAP75: dHJ dissolution     ── PMID 18390547, 24392087     │
  │   • Sgs1/BLM RecQ HJ branch-migration enzyme ── PMID 24984776               │
  └───────────────────────────────────────────────────────────────────────────┘
           │
           ▼
  IBA propagation (GO_Central / PAINT, GO_REF:0000033, ECO:0000318)
  with/from: BLM P54132, WRN Q14191, Arabidopsis RecQ loci
           │
           ▼
  Rqh1 (Q09811) GO:0009378  ── INFERRED, not measured
```

The coherent narrative is that Rqh1 is the **single** RecQ helicase of *S. pombe*, orthologous to Sgs1/BLM/WRN, and functions in a complex with Top3 (topoisomerase III) to process aberrant recombination and replication intermediates during S phase and G2. Its orthologues, when purified, catalyze HJ branch migration and, together with Top3α + BLAP75/RMI, dissolve double Holliday junctions to yield non-crossover products. Rqh1's in-vivo phenotypes (crossover suppression that requires its helicase activity; disassembly of joint molecules; maintenance of circular chromosomes by inhibiting crossovers) are exactly what one would predict if Rqh1 acted on four-way junctions in cells. Conservation of the RQC winged-helix and HRDC modules provides the structural substrate for this activity. **What is missing is the one experiment that would convert inference into fact: an in-vitro assay showing purified Rqh1 unwinding or migrating a defined four-way-junction substrate.**

### GO decision table

| GO term | Aspect | Current evidence for Rqh1 | Recommended curation action |
|---|---|---|---|
| GO:0043138 — 3'–5' DNA helicase activity | MF | IDA ×2 (PMID 12724426, 12478586) | **Retain** — directly evidenced core MF |
| GO:0009378 — four-way junction helicase activity | MF | IBA only (from BLM/WRN/Sgs1) | **Retain as inference (IBA/ISS); do NOT upgrade to IDA/EXP** |
| Recombinational repair / crossover control | BP | IMP/IGI (PMID 17353272 and others) | Retain as BP — well supported in vivo |
| Rqh1–Top3 complex | CC/complex | IDA/IPI (PMID 12724426) | Retain |

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [12724426](https://pubmed.ncbi.nlm.nih.gov/12724426/) (Laursen 2003) | Direct assay | Qualifies | Does purified Rqh1 have four-way-junction helicase activity? | Rqh1 is a 3'→5' helicase in a complex with Top3; four-way-junction substrate not tested | Purified *S. pombe* Rqh1p, in vitro | High for 3'→5'; establishes absence of direct HJ evidence |
| [12478586](https://pubmed.ncbi.nlm.nih.gov/12478586/) (Ahmad 2002) | Direct assay | Qualifies | Same, independent replicate | Rqh1p displays 3'→5' helicase; helicase activity only partially required for function | Purified Rqh1p, in vitro | High; second independent IDA; no HJ substrate |
| [17353272](https://pubmed.ncbi.nlm.nih.gov/17353272/) (Hope 2007) | Mutant phenotype (IMP) | Supports (BP-level) | Does Rqh1 helicase activity control crossovers in vivo? | ~4-fold crossover increase in `rqh1Δ`; suppression is helicase-dependent | *S. pombe* mitotic DSB repair | High for genetics; indirect for MF |
| [39580958](https://pubmed.ncbi.nlm.nih.gov/39580958/) | Mutant phenotype | Supports (BP-level) | Does Rqh1 resolve recombination intermediates? | "Rqh1 resolves recombination intermediates" | *S. pombe* | Medium; phenotype-level |
| [31584934](https://pubmed.ncbi.nlm.nih.gov/31584934/) | Mutant phenotype | Supports (BP-level) | Does Rqh1 disassemble joint molecules? | Histone deposition antagonizes "Rqh1-mediated disassembly of joint-molecules" | *S. pombe* arrested forks | Medium; phenotype-level |
| [16670433](https://pubmed.ncbi.nlm.nih.gov/16670433/) (BLM) | Direct assay (orthologue) | Supports inference | Do RecQ orthologues migrate HJs? | "BLM also promotes branch migration of Holliday junctions" | Purified human BLM | High for BLM; basis of IBA |
| [24392087](https://pubmed.ncbi.nlm.nih.gov/24392087/) | Direct assay (orthologue) | Supports inference | dHJ dissolution mechanism | Top3α required for convergent migration step of dHJ dissolution with BLM | Human BLM/Top3α in vitro | High for orthologue |
| [18390547](https://pubmed.ncbi.nlm.nih.gov/18390547/) | Direct assay (orthologue) | Supports inference | BTB complex HJ processing | BLAP75/BLM/TopoIIIα branch-migrate HJ and dissolve dHJ | Human proteins in vitro | High for orthologue |
| [24984776](https://pubmed.ncbi.nlm.nih.gov/24984776/) | Review/database | Supports inference | dHJ dissolution as conserved Sgs1/BLM+Top3 function | Defines HJ branch-migration/dissolution for Sgs1/BLM+Top3 | Review | Orientation only |
| [33647232](https://pubmed.ncbi.nlm.nih.gov/33647232/) | Structural (orthologue) | Supports inference | Structural basis of HJ branch migration | BLM–DNA structures give "a model for branch migration of Holliday junctions" | Human BLM crystallography | High for BLM |
| InterPro/UniProt REST (computed) | Structural/evolutionary | Supports inference | Does Rqh1 conserve HJ-recognition modules? | Rqh1 shares RQC winged-helix (IPR018982) + HRDC (IPR002121) with BLM/WRN/Sgs1 | Computed domain architecture | High for conservation; not an activity measurement |
| QuickGO (Q09811, computed) | Database | Qualifies | What is the evidence code for GO:0009378? | IBA, ECO:0000318, GO_REF:0000033; with/from BLM/WRN/Arabidopsis RecQ | GO annotation provenance | Definitive for evidence code |

---

## Conflicts and Alternatives

- **Orthologue carry-over.** The strongest alternative interpretation is that GO:0009378 is a database carry-over from BLM/WRN/Sgs1 rather than a fission-yeast fact. QuickGO provenance confirms this directly (IBA, with/from human BLM P54132 and WRN Q14191). Rqh1 is the *sole* RecQ in *S. pombe*, so this is not intra-organism paralog confusion, but it is cross-species propagation.
- **Helicase-independent functions.** Ahmad 2002 ([PMID: 12478586](https://pubmed.ncbi.nlm.nih.gov/12478586/)) explicitly reports that Rqh1p's helicase activity is "only partially required for its function," and Top3-related genetics (e.g., [PMID: 10572171](https://pubmed.ncbi.nlm.nih.gov/10572171/), [PMID: 15340008](https://pubmed.ncbi.nlm.nih.gov/15340008/)) show that Rqh1/Top3 lethality relationships involve helicase-dependent and independent components. This cautions against over-weighting any single helicase sub-activity as *the* core function.
- **BP vs MF conflation.** The in-vivo phenotypes (crossover suppression, joint-molecule disassembly) are readily explained by junction dissolution together with Top3 (a topoisomerase-dependent dissolution) rather than by autonomous four-way-junction unwinding. In the orthologue system, robust dHJ processing requires the BLM–TopoIIIα–BLAP75 complex, not BLM alone — so even the orthologue "activity" is partly complex-dependent. The four-way-junction MF term for Rqh1 alone may therefore be biologically narrower than what the enzyme actually does in its physiological Top3 complex.

---

## Limitations and Knowledge Gaps

1. **No direct four-way-junction assay for Rqh1.** *Checked:* PubMed for Rqh1 + Holliday junction / branch migration / branched-substrate biochemistry; PomBase/QuickGO evidence codes. *Why it matters:* this is the single experiment separating inference from fact. *Resolution:* purify recombinant Rqh1 (± Top3) and assay on a defined synthetic four-way (X-junction) substrate for unwinding and branch migration.
2. **Rqh1-alone vs Rqh1–Top3 complex activity.** *Checked:* complex composition (PMID 12724426) and orthologue dHJ requirements (PMID 24392087, 18390547). *Why it matters:* the physiological unit is the Rqh1–Top3 dissolvasome; the MF term describes Rqh1 alone. *Resolution:* compare junction processing by Rqh1 alone vs Rqh1–Top3 (± Rmi1/BLAP75 orthologue) in vitro.
3. **Whether the IBA should be annotated as ISS with a specific "with" gene.** *Checked:* QuickGO provenance. *Why it matters:* curators may prefer an explicit ISS to BLM/Sgs1 over a PAINT IBA. *Resolution:* curator judgment plus a documented sequence/domain alignment (already supported by Finding 4).
4. **Direct correspondence between in-vivo crossover suppression and four-way-junction unwinding.** *Checked:* Hope 2007 genetics. *Why it matters:* crossover suppression could operate via D-loop dissolution/SDSA rather than HJ migration. *Resolution:* separation-of-function alleles and substrate-specific in-vitro assays.

---

## Discriminating Tests

1. **In-vitro four-way-junction unwinding/branch-migration assay** on purified recombinant Rqh1 using a defined synthetic X-junction (fluorescently or radiolabeled), ± ATP, ± Mg²⁺. A positive result would directly justify GO:0009378 at IDA; a negative would confirm the term is inference-only for Rqh1.
2. **Rqh1 vs Rqh1–Top3(±Rmi1) comparison** on double-Holliday-junction and mobile-D-loop substrates, mirroring the BLM–TopoIIIα–BLAP75 experiments (PMID 24392087, 18390547), to determine whether junction processing is an autonomous Rqh1 activity or a complex property.
3. **Separation-of-function helicase-dead and junction-binding mutants** (e.g., Walker-A K→I, analogous to `rad12-K547I`, PMID 10572171) assayed both in vitro (substrate specificity) and in vivo (crossover frequency), to map the crossover-suppression phenotype onto a specific molecular activity.
4. **Structure-guided comparison** of the Rqh1 RQC winged-helix against the BLM branch-migration model (PMID 33647232) via AlphaFold/homology modeling to predict junction-binding residues, then test them experimentally.

---

## Proposed Follow-up Actions (Curation Leads — require curator verification)

- **Retain GO:0009378 "four-way junction helicase activity" as an inferred annotation (IBA, ECO:0000318, or ISS to BLM/Sgs1).** Do **not** upgrade to an experimental evidence code (IDA/EXP) — no direct Rqh1 assay exists.
- **Retain GO:0043138 "3'–5' DNA helicase activity" (IDA)** as the primary, directly evidenced molecular function, backed by two independent references (PMID 12724426, 12478586).
- **Candidate references to verify:**
  - PMID 12478586 — snippet: *"Here we show that, like other RecQ family members, the Rqh1p protein displays 3' to 5' DNA helicase activity."* (confirms MF is 3'→5', not four-way-junction)
  - PMID 12478586 — snippet: *"unlike other RecQ family members, the helicase activity of Rqh1p is only partially required for its function."* (caveat on core-function weighting)
  - PMID 17353272 — snippet: *"This suppression of crossover formation by Rqh1 is dependent on its helicase activity."* (BP-level support)
  - PMID 16670433 — snippet: *"BLM also promotes branch migration of Holliday junctions."* (orthologue basis of IBA)
- **Suggested question for curators:** should the four-way-junction MF be re-expressed as an ISS to a named orthologue (BLM P54132 / Sgs1 P35187) rather than a PAINT IBA, given the strong domain-architecture conservation documented here?
- **Suggested experiment:** direct in-vitro four-way-junction assay on purified Rqh1 (± Top3), which would resolve the inference-vs-fact gap in a single experiment.

---

## Evidence Base (selected literature)

- **[PMID: 12724426](https://pubmed.ncbi.nlm.nih.gov/12724426/)** — Laursen et al. 2003. Direct assay: Rqh1 is a 3'→5' helicase in a Top3 complex (basis of GO:0043138 IDA). *No HJ substrate tested.*
- **[PMID: 12478586](https://pubmed.ncbi.nlm.nih.gov/12478586/)** — Ahmad, Kaplan & Stewart 2002. Second independent 3'→5' helicase IDA; notes helicase activity only partially required.
- **[PMID: 17353272](https://pubmed.ncbi.nlm.nih.gov/17353272/)** — Hope et al. 2007. Helicase-dependent crossover suppression in vivo (BP support).
- **[PMID: 39580958](https://pubmed.ncbi.nlm.nih.gov/39580958/)** / **[PMID: 31584934](https://pubmed.ncbi.nlm.nih.gov/31584934/)** — Rqh1 resolves/disassembles recombination joint molecules (BP support).
- **[PMID: 16670433](https://pubmed.ncbi.nlm.nih.gov/16670433/)** — BLM promotes HJ branch migration (orthologue direct evidence).
- **[PMID: 24392087](https://pubmed.ncbi.nlm.nih.gov/24392087/)**, **[PMID: 18390547](https://pubmed.ncbi.nlm.nih.gov/18390547/)**, **[PMID: 24984776](https://pubmed.ncbi.nlm.nih.gov/24984776/)** — BLM/Sgs1 + Top3(+BLAP75/Rmi1) dHJ dissolution and HJ processing (orthologue basis of the conserved-function inference).
- **[PMID: 33647232](https://pubmed.ncbi.nlm.nih.gov/33647232/)** — BLM structures providing a model for HJ branch migration (structural basis).
- **[PMID: 32085395](https://pubmed.ncbi.nlm.nih.gov/32085395/)**, **[PMID: 23161011](https://pubmed.ncbi.nlm.nih.gov/23161011/)** — Reviews of yeast/human RecQ helicase function (orientation only).

---

*Report prepared for AI Gene Review hypothesis-level curation. All molecular-function claims are separated into direct Rqh1 assays vs orthologue-derived inference. Computed provenance: QuickGO evidence-code lookup for Q09811 and InterPro/UniProt-REST domain-architecture comparison across Rqh1/BLM/WRN/RECQ1/Sgs1.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)