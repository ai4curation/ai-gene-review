---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:31:16.852358'
end_time: '2026-08-31T08:49:55.004010'
duration_seconds: 1118.15
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: SCHPO
  gene: dca7
  gene_symbol: dca7
  uniprot_accession: O74763
  taxon_id: NCBITaxon:284812
  taxon_label: Schizosaccharomyces pombe (strain 972 / ATCC 24843)
  focus_type: core_function
  hypothesis_slug: core-function-schizosaccharomyces-pombe-dca7-is-a-bona-fide-substrate-receptor-component-of-a-cu
  hypothesis_text: Schizosaccharomyces pombe Dca7 is a bona fide substrate receptor
    component of a Cul4-Ddb1 RING ubiquitin ligase complex
  term_context: No specific term context supplied.
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: Schizosaccharomyces pombe Dca7 is a bona fide\
    \ substrate receptor component of a Cul4-Ddb1\n  RING ubiquitin ligase complex\n\
    focus_type: core_function\ncontext: []\nreference_id: []"
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
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
artifacts:
- filename: dca7_evidence_matrix.csv
  path: openscientist_artifacts/dca7_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist dca7 evidence matrix
- filename: dca7_go_decision_table.csv
  path: openscientist_artifacts/dca7_go_decision_table.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist dca7 go decision table
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
- **Hypothesis slug:** core-function-schizosaccharomyces-pombe-dca7-is-a-bona-fide-substrate-receptor-component-of-a-cu
- **Source file:**
- **Source selector:**

## Seed Hypothesis

Schizosaccharomyces pombe Dca7 is a bona fide substrate receptor component of a Cul4-Ddb1 RING ubiquitin ligase complex

## Term and Decision Context

No specific term context supplied.

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: Schizosaccharomyces pombe Dca7 is a bona fide substrate receptor component of a Cul4-Ddb1
  RING ubiquitin ligase complex
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

# AIGR Gene Hypothesis Deep Research — *S. pombe* Dca7 (O74763)

**Gene:** dca7 (SPBC17D11.08) · **UniProt:** O74763 · **Organism:** *Schizosaccharomyces pombe* (972 / ATCC 24843)
**Focus type:** core_function
**Seed hypothesis:** *S. pombe* Dca7 is a bona fide substrate receptor component of a Cul4-Ddb1 RING ubiquitin ligase complex.

---

## Summary

**Verdict: Weakly supported / over-annotated.** The claim that *S. pombe* Dca7 (UniProt O74763; systematic name SPBC17D11.08) is a bona fide substrate-receptor subunit of a Cul4-Ddb1 (CRL4) RING ubiquitin ligase rests entirely on orthology transfer and a historically loaded protein name ("DCAF7" = **D**DB1- and **C**UL4-**A**ssociated **F**actor **7**). It is **not** supported by any direct experimental evidence in fission yeast. The single cellular-component GO annotation placing Dca7 in a Cul4-RING E3 ubiquitin ligase complex (GO:0080008) carries an ISS (Inferred from Sequence/Structural Similarity) evidence code with GO_REF:0000024 — i.e., a manual transfer of annotation to an ortholog, not an experimental observation in *S. pombe*.

Three independent lines of analysis argue that the CRL4 substrate-receptor role is **not** the primary (core) function of Dca7. First, Dca7 lacks the conserved **WDxR** DDB1-binding motif that genuine WD40-type DCAFs use to dock onto the DDB1 β-propeller; a motif scan of the 435-residue sequence returned zero WDxR matches. Second, PomBase records no physical or genetic interaction between Dca7 and any *S. pombe* CRL4 core subunit (Pcu4/Cul4, Ddb1, Rik1, Cdt2); its only two curated physical interactors are the chromatin remodeller Fft3 and, tellingly, the dual-specificity protein kinase Ppk15. Third, the deeply conserved and experimentally validated function of this entire WD40 β-propeller family — human DCAF7/WDR68/HAN11, petunia AN11, *C. elegans* Swan-1/2 — is that of a **catalytically inactive scaffold** that binds and coordinates DYRK-family, HIPK, and MEKK kinases, regulating their stability, localization, and downstream gene-expression programs.

The competing "kinase scaffold" model is not merely a plausible alternative; it is the better-evidenced core function across the family, and it is echoed in fission yeast by Dca7's interaction with Ppk15, a kinase annotated with both Ser/Thr and Tyr kinase activities — the dual-specificity signature of the DYRK family. In balance, one report does document that human WDR68 can physically associate with CUL4-DDB1, so the DCAF designation is not baseless; however, **no study in any organism demonstrates DCAF7/WDR68/Dca7 delivering a substrate for CRL4-mediated ubiquitination.** For curation, the Cul4-RING complex annotation on Dca7 should be treated as low-confidence/orthology-only, and the gene's core function is better captured by a kinase-scaffold / gene-expression regulatory role.

---

## Executive Judgment

**Weakly supported / over-annotated.** *S. pombe* Dca7 (O74763) is the ortholog of human DCAF7/WDR68, and the sole support for it being a Cul4-Ddb1 substrate receptor is an orthology-transferred GO term (GO:0080008, ISS/GO_REF:0000024) inherited from the historically loaded "DCAF7" name. There is no direct *S. pombe* evidence, no WDxR DDB1-binding motif (0 matches), and no recorded interaction with any pombe CRL4 subunit (Pcu4/Ddb1/Rik1/Cdt2). The deeply conserved, experimentally validated core function of this WD40 β-propeller family is a **catalytically inactive scaffold for DYRK/HIPK/MEKK kinases** — echoed in fission yeast by Dca7's interaction with the dual-specificity kinase Ppk15. A single mammalian report shows WDR68 can associate with CUL4-DDB1, so the DCAF label is not baseless, but substrate delivery has never been demonstrated. Curators should treat the Cul4-RING annotation as low-confidence/orthology-only, not a demonstrated substrate-receptor core function.

**Most important caveats:** (1) "No recorded interaction" reflects curated PomBase datasets, which are not exhaustive; (2) some DCAFs dock onto DDB1 through non-WDxR surfaces, so motif absence is strong but not absolute proof; (3) the Ppk15 link rests on a single two-hybrid plus GO-level dual-specificity annotation.

---

## Key Findings

### Finding 1 — The Cul4-RING annotation on Dca7 is an orthology transfer (ISS), not experimental evidence

Dca7 (O74763 / SPBC17D11.08) is the *S. pombe* ortholog of human **DCAF7/WDR68**. UniProt places it in InterPro family **IPR045159 "DCAF7-like"**, and PomBase lists the human ortholog as HGNC:30915 (DCAF7/WDR68), the *S. cerevisiae* ortholog as YPL247C, and the *S. japonicus* ortholog as SJAG_04087.

Critically, the only cellular-component GO annotations on Dca7 are:

- **GO:0080008** "Cul4-RING E3 ubiquitin ligase complex" — evidence code **ISS**, reference **GO_REF:0000024** (manual transfer of experimentally-supported annotations to orthologs), and
- **GO:0005634** "nucleus" — evidence code **IBA** (Inferred from Biological ancestor), reference GO_REF:0000033.

There is **no molecular-function and no biological-process GO term** on the gene, and no direct assay placing Dca7 in a CRL4 complex. The 28 references associated with the gene in PomBase are high-throughput proteomics/interactome/genetic-screen datasets — none is a dedicated CRL4 biochemistry paper focused on Dca7. The biochemical criterion that a WD40 protein must meet to be a genuine Cul4-Ddb1 substrate receptor was established by [PMID: 16949367](https://pubmed.ncbi.nlm.nih.gov/16949367/): *"DCAFs interact with multiple surfaces on Ddb1, and the interaction of WD40-containing DCAFs with Ddb1 requires a conserved 'WDXR' motif."* This provides the objective standard against which Dca7 can be judged — and Dca7 fails it (Finding 2).

### Finding 2 — Dca7 lacks a WDxR DDB1-binding motif and shows no interaction with the *S. pombe* CRL4 core

A motif scan of the 435-amino-acid O74763 sequence found **zero WD-x-R (WDxR) matches** (only two bare "WD" dipeptides, at positions 194 and 343). The conserved DDB1-binding box required of WD40-type DCAFs is therefore absent from Dca7. This is a direct, sequence-level discriminator: the very feature [PMID: 16949367](https://pubmed.ncbi.nlm.nih.gov/16949367/) defines as necessary for a WD40 DCAF to bind Ddb1 is missing.

Consistent with the absence of a docking motif, PomBase records only **two physical interactors** for Dca7, neither of them a CRL4 subunit:

- **Fft3** (SPAC25A8.01c), a SMARCAD1-family chromatin remodeller (Affinity Capture-MS, [PMID: 28218250](https://pubmed.ncbi.nlm.nih.gov/28218250/)), and
- **Ppk15** (SPAC823.03), a Ser/Thr protein kinase (two-hybrid, [PMID: 26771498](https://pubmed.ncbi.nlm.nih.gov/26771498/)).

No physical or genetic interaction is recorded with *S. pombe* Cul4/Pcu4, Ddb1, Rik1, Cdt2, or any other CRL4 component. PomBase's curated product description reads: *"WD repeat protein, DDB1 and CUL4-associated factor Dca7, implicated in gene expression"*; the deletion is viable. Both the interactor profile (a kinase and a chromatin remodeller) and the "implicated in gene expression" descriptor fit the DCAF7 kinase-scaffold / gene-regulation paradigm far better than a CRL4 substrate-receptor role. The competing paradigm is captured by [PMID: 23349862](https://pubmed.ncbi.nlm.nih.gov/23349862/): the vertebrate ortholog *"Wdr68 is a highly conserved scaffolding protein... A Ras-Map3k-Wdr68-Dyrk1 signaling relay may mediate these and other diverse signaling events."*

### Finding 3 — The conserved core function of the DCAF7/WDR68/Han11 family is a catalytically inactive kinase scaffold

Across eukaryotes, the Dca7 ortholog is characterized as a scaffold/adaptor with **no catalytic activity** that binds and coordinates protein kinases:

- Han11 directly binds HIPK2, DYRK1A, DYRK1B and MEKK1 and is required to couple MEKK1 to DYRK1/HIPK2 ([PMID: 20940704](https://pubmed.ncbi.nlm.nih.gov/20940704/)): *"these experiments identify Han11 as a novel scaffold protein regulating kinase signalling by HIPK2 and MEKK1."*
- DCAF7 *"is an evolutionarily conserved protein with a single WD40 repeat domain and has no catalytic activity"* and acts as a substrate-recruiting subunit of DYRK1A and HIPK2 ([PMID: 27307198](https://pubmed.ncbi.nlm.nih.gov/27307198/)).
- WDR68 binds the N-terminal domain of DYRK1A and controls its nuclear localization ([PMID: 21777625](https://pubmed.ncbi.nlm.nih.gov/21777625/)), and is required for normal DYRK1A/1B protein levels ([PMID: 30496304](https://pubmed.ncbi.nlm.nih.gov/30496304/)).

Consistent with this conserved role, the only characterized *S. pombe* protein-kinase interactor of Dca7, **Ppk15** (SPAC823.03; two-hybrid [PMID: 26771498](https://pubmed.ncbi.nlm.nih.gov/26771498/)), carries **both** GO:0004674 (protein Ser/Thr kinase) and GO:0004713 (protein Tyr kinase) activities — the **dual-specificity signature of the DYRK family** (the canonical pombe DYRK, Pom1, is likewise annotated). This is strong circumstantial evidence that fission-yeast Dca7 preserves the ancestral DYRK-scaffold function.

**Balance note:** human WDR68 has also been reported to bind CUL4-DDB1 ([PMID: 25342745](https://pubmed.ncbi.nlm.nih.gov/25342745/): *"binds to several proteins, including... Cullin4-damage-specific DNA-binding protein 1 (CUL4-DDB1)"*), so the "DCAF" designation is not entirely baseless. But no study demonstrates the protein delivering substrates for CRL4-mediated ubiquitination — the defining activity of a genuine substrate receptor.

### Finding 4 — The AlphaFold model of Dca7 is a confident WD40 β-propeller consistent with the DCAF7/WDR68 fold

Parsing the deposited AlphaFold model **AF-O74763-F1-model_v6** (435 residues) gave a mean pLDDT of **78.6** (median 92.3), with **73.3%** of residues confident (pLDDT ≥ 70) and **59.3%** very high (≥ 90). The InterPro-defined WD40 propeller core (residues **80–345**) has a mean pLDDT of **89.5** (high confidence), while the N- and C-terminal extensions are low-confidence/flexible.

This matches the experimentally described seven-bladed β-propeller of WDR68 ([PMID: 25342745](https://pubmed.ncbi.nlm.nih.gov/25342745/): *"Computer-aided structural analysis suggested that WDR68 forms a seven-bladed β-propeller ring."*) and the observation that regions outside the central WD40 repeats mediate DYRK1A binding ([PMID: 21777625](https://pubmed.ncbi.nlm.nih.gov/21777625/)). The structural prediction is fully compatible with the kinase-scaffold model: a stable WD40 propeller core presenting flexible terminal arms that, in the orthologs, engage kinase partners. The fold alone does not distinguish DCAF from scaffold — WD40 propellers serve both roles — so structure neither confirms nor refutes the CRL4 claim; it simply confirms family membership.

---

## Mechanistic Model / Interpretation

The central question is whether the CRL4 substrate-receptor activity, or the kinase-scaffold activity, represents the **core (primary)** molecular function of Dca7. The evidence favors the kinase scaffold.

```
   COMPETING MODELS FOR Dca7 CORE FUNCTION
   ========================================

   (A) SEED HYPOTHESIS — CRL4 substrate receptor
   ---------------------------------------------
        Pcu4/Cul4 —— Ddb1 —— [Dca7?] —— (substrate) —> ubiquitination
                                 ^
                                 |  requires WDxR DDB1-binding motif  X ABSENT
                                 |  requires interaction with Ddb1/Cul4 core  X NONE
                                 |  requires a demonstrated substrate  X NONE (any organism)
        SUPPORT: orthology/name only (ISS, GO_REF:0000024)


   (B) COMPETING / BETTER-EVIDENCED — kinase scaffold
   --------------------------------------------------
        DYRK/HIPK/MEKK kinase  ==bind==>  Dca7 (WD40 propeller, catalytically inactive)
              |                                   |
              |                                   +--> controls kinase stability & levels
              |                                   +--> controls kinase nuclear localization
              +--> regulates gene expression / signaling relay
        SUPPORT: direct assays across human/mouse/plant/worm orthologs;
                 pombe interactor Ppk15 is a DYRK-type dual-specificity kinase
```

The seed hypothesis conflates a **name** ("DCAF7") with a **demonstrated activity**. The DCAF7 name was coined when the human protein was catalogued among Cul4-Ddb1-associated factors, but subsequent functional work redefined the protein's principal biology as kinase scaffolding. The name has since propagated to orthologs — including *S. pombe* Dca7 — via automated and manual orthology transfer, carrying the CRL4 complex annotation with it. In fission yeast, none of the three hallmarks of a genuine substrate receptor is met: (i) no WDxR docking motif, (ii) no interaction with the CRL4 core, and (iii) no demonstrated substrate. By contrast, the scaffold model is supported by a conserved fold, a conserved family function, and a locally relevant kinase interactor (Ppk15).

Importantly, *S. pombe* **does** possess well-characterized, genuinely CRL4-associated DCAFs — Raf1 ([PMID: 22319459](https://pubmed.ncbi.nlm.nih.gov/22319459/)), Cdt2 ([PMID: 17039252](https://pubmed.ncbi.nlm.nih.gov/17039252/)), Wdr70 ([PMID: 27098497](https://pubmed.ncbi.nlm.nih.gov/27098497/)) — each with direct biochemical/phenotypic evidence and (for Raf1) a validated WDxR motif. Dca7 is conspicuously absent from this list, reinforcing that its CRL4 annotation is a carry-over rather than a curated experimental result.

| Discriminating criterion | Genuine pombe DCAFs (Raf1, Cdt2, Wdr70) | Dca7 |
|---|---|---|
| WDxR / DDB1-binding motif | Present (Raf1, verified by mutation) | **Absent** (0 matches) |
| Recorded interaction with Ddb1/Cul4 core | Yes (biochemical) | **None** |
| Demonstrated substrate | Yes (e.g. Cdt1 for Cdt2; Epe1 for Cdt2 complex) | **None** |
| Dedicated CRL4 biochemistry paper | Yes | **None** |
| Alternative conserved function | — | Kinase scaffold (DYRK/HIPK/MEKK) |

---

## Evidence Base / Evidence Matrix

| Citation (PMID) | Evidence type | Supports / Refutes / Qualifies / Competing | Claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PomBase / UniProt O74763 | Review/database | Qualifies | Is the CRL4 annotation experimental? | Only CC term GO:0080008 (Cul4-RING) is ISS/GO_REF:0000024 (ortholog transfer); no MF/BP terms | *S. pombe* Dca7 | High that annotation is ISS; database-level |
| [16949367](https://pubmed.ncbi.nlm.nih.gov/16949367/) | Direct assay (biochemistry) | Refutes (sets criterion) | What defines a WD40 DCAF | WD40 DCAFs require a conserved WDxR motif to bind Ddb1 | Human | High; establishes the standard Dca7 fails |
| Motif scan (computational, this study) | Computational | Refutes | Does Dca7 have a WDxR motif? | Zero WDxR matches in 435-aa sequence | *S. pombe* Dca7 | High for absence; scans can miss non-canonical variants |
| PomBase interactions | Interaction/database | Refutes / Competing | Does Dca7 bind CRL4 core? | Only interactors are Fft3 (remodeller) and Ppk15 (kinase); no Cul4/Ddb1/Rik1/Cdt2 | *S. pombe* | Medium-high; absence of evidence, not exhaustive |
| [26771498](https://pubmed.ncbi.nlm.nih.gov/26771498/) | Interaction (two-hybrid) | Competing | Dca7 kinase partner? | Dca7 interacts with Ppk15, a dual-specificity (Ser/Thr + Tyr) DYRK-type kinase | *S. pombe* | Medium; Y2H, single method |
| [20940704](https://pubmed.ncbi.nlm.nih.gov/20940704/) | Direct assay | Competing | Family core function | Han11 is a scaffold for HIPK2/MEKK1/DYRK kinase signalling | Human | High |
| [27307198](https://pubmed.ncbi.nlm.nih.gov/27307198/) | Direct assay | Competing | Catalytic activity & role | DCAF7 has no catalytic activity; adaptor for DYRK1A/HIPK2 | Human | High |
| [21777625](https://pubmed.ncbi.nlm.nih.gov/21777625/) | Direct assay / localization | Competing | Kinase binding & localization | WDR68 binds DYRK1A N-terminus; controls nuclear translocation | Mammalian cells | High |
| [30496304](https://pubmed.ncbi.nlm.nih.gov/30496304/) | Mutant / knockout | Competing | Functional consequence | WDR68 required for normal DYRK1A/1B protein levels | Mouse/human cell lines | High |
| [25342745](https://pubmed.ncbi.nlm.nih.gov/25342745/) | Direct assay / structural | Qualifies (balance) | Does WDR68 bind CUL4-DDB1? | WDR68 forms 7-bladed β-propeller; binds DYRK1A and CUL4-DDB1 | Human | Medium; association shown, no substrate delivery |
| AlphaFold AF-O74763 (computational, this study) | Structural/computational | Qualifies | Fold of Dca7 | Confident WD40 β-propeller (core pLDDT 89.5); flexible termini | *S. pombe* Dca7 | High for fold; fold shared by both models |
| [23349862](https://pubmed.ncbi.nlm.nih.gov/23349862/) | Mutant phenotype | Competing | Ortholog in vivo role | Wdr68 is a conserved scaffold in a Ras-Map3k-Wdr68-Dyrk1 relay | Zebrafish/vertebrate | High for scaffold role |
| [22319459](https://pubmed.ncbi.nlm.nih.gov/22319459/) | Direct assay / mutant | Qualifies (contrast) | What a real pombe DCAF looks like | Raf1 is a bona fide pombe DCAF with WDxR motif for Rik1/Cul4 | *S. pombe* | High; shows Dca7 is not analogous |
| [17039252](https://pubmed.ncbi.nlm.nih.gov/17039252/) | Mutant / biochemistry | Qualifies (contrast) | Genuine CRL4 substrate degradation | Cdt2/Ddb1/Cul4 degrade Cdt1 — real substrate-receptor biology in pombe | *S. pombe* | High; contrasts with Dca7's lack of substrate |
| [27098497](https://pubmed.ncbi.nlm.nih.gov/27098497/) | Direct assay / mutant | Qualifies (contrast) | Another genuine pombe DCAF | Wdr70 is recruited as part of CRL4(Wdr70), stimulates uH2B, aids resection | *S. pombe* | High; a real WD40 DCAF, unlike Dca7 |

---

## GO Curation Implications

**Lead requiring curator verification.** The single cellular-component annotation **GO:0080008 "Cul4-RING E3 ubiquitin ligase complex"** on Dca7 is an **ISS orthology transfer** (GO_REF:0000024) with no supporting *S. pombe* experimental evidence, no WDxR motif, and no recorded interaction with the pombe CRL4 core. It should **not** be treated as a demonstrated core function.

Suggested curation actions (for curator verification):

1. **Retain but flag / down-weight** GO:0080008 as orthology-only (ISS), or reassess whether it meets the local evidence bar at all. Do not promote it to represent the gene's core function, and do not assert a substrate-receptor molecular activity on the basis of this term.
2. **Do not add** a molecular-function term implying substrate-recognition/ubiquitin-ligase substrate-adaptor activity — no evidence supports it in any organism.
3. **Consider the better-supported core function.** The conserved family activity is a **kinase scaffold / adaptor**. If a curator wishes to reflect demonstrated biology, candidate directions include a molecular-function reflecting **protein kinase binding / kinase-scaffold activity** and a biological-process reflecting **regulation of gene expression / signal transduction** — but note these rest on ortholog data plus the local Ppk15 interaction, so ISS-level support at best in *S. pombe*. (Avoid the uninformative "protein binding" as a final recommendation.)
4. **CC "nucleus" (GO:0005634, IBA)** is consistent with both models and with WDR68 nuclear localization; it can be retained.

Net: the evidence supports treating the Cul4-RING CC annotation as **non-core / low-confidence orthology carry-over**, and identifies a competing, better-evidenced kinase-scaffold function that a curator may choose to represent conservatively.

| GO term | Current evidence | Recommended action (lead) | Rationale |
|---|---|---|---|
| GO:0080008 Cul4-RING E3 ubiquitin ligase complex (CC) | ISS, GO_REF:0000024 | Flag as orthology-only/non-core; do not treat as demonstrated | No WDxR motif, no CRL4-core interaction, no substrate in pombe |
| GO:0005634 nucleus (CC) | IBA, GO_REF:0000033 | Retain | Consistent with WDR68 nuclear localization |
| (candidate) protein kinase binding / kinase-scaffold (MF) | Not currently annotated | Consider adding at ISS level | Conserved family function; local Ppk15 interaction |
| (candidate) regulation of gene expression (BP) | Not currently annotated | Consider at ISS level | PomBase descriptor "implicated in gene expression" |

---

## Mechanistic Scope

**Immediate molecular function being tested:** whether Dca7 acts as a substrate-recognition subunit that docks onto Ddb1 within a Cul4 RING E3 ligase and thereby delivers substrates for ubiquitination.

- **Direct gene-product activity (what is actually supported):** Dca7 is a WD40 β-propeller protein (confident AlphaFold model). By strong family conservation it is a catalytically inactive scaffold that binds protein kinases; locally it interacts with the DYRK-type kinase Ppk15 and the chromatin remodeller Fft3.
- **Not supported as direct activity:** substrate-receptor function within CRL4 — this is inferred solely from the name/orthology and fails the WDxR and core-interaction tests.
- **Downstream / inferred effects (in orthologs, not to be conflated with core activity):** regulation of DYRK1A/1B protein levels and localization, control of proliferation/differentiation balance, craniofacial and developmental patterning, and (in disease contexts) modulation of RAS/IFN signaling. These are consequences of the scaffold activity, not evidence for a ubiquitin-ligase substrate-receptor role.

---

## Conflicts and Alternatives

- **Name-driven database carry-over (principal confound).** "DCAF7" encodes a CRL4 association in its very name, which has propagated to orthologs via ISS. This is the most parsimonious explanation for the pombe annotation and is the classic pattern of ortholog over-annotation.
- **Genuine WDR68–CUL4-DDB1 association exists but is not substrate delivery.** [PMID: 25342745](https://pubmed.ncbi.nlm.nih.gov/25342745/) shows human WDR68 can bind CUL4-DDB1. This qualifies (does not refute) the possibility that the family retains some CRL4 contact, but no substrate ubiquitination has ever been attributed to it. The seed hypothesis over-reaches from "can associate" to "is a bona fide substrate receptor."
- **Organism-specific divergence.** Even if human WDR68 touches CUL4-DDB1, *S. pombe* Dca7 shows no such interaction in curated datasets and lacks the WDxR motif; fission-yeast biology may not recapitulate the mammalian association.
- **Bona fide pombe DCAFs provide the contrast case.** Raf1, Cdt2, and Wdr70 are genuine pombe CRL4 substrate receptors with direct evidence; Dca7's absence from this well-studied group is itself informative.

---

## Limitations and Knowledge Gaps

1. **No dedicated Dca7 biochemistry in *S. pombe*.** *Checked:* PomBase interactions and references — all high-throughput. *Why it matters:* the entire CRL4 claim hinges on whether Dca7 physically contacts Ddb1/Pcu4. *Resolution:* co-IP / affinity-MS of tagged Dca7 probing for Ddb1, Pcu4, Rik1, Cdt2.
2. **Is Ppk15 a functional DYRK partner of Dca7?** *Checked:* GO annotations (dual-specificity) and a single Y2H. *Why it matters:* would confirm the conserved scaffold role locally. *Resolution:* co-IP, kinase-level/localization changes in *dca7Δ*, epistasis.
3. **Does Dca7 deletion cause any CRL4-pathway phenotype** (heterochromatin, Cdt1/Spd1 degradation, DSB resection)? *Checked:* deletion is viable; no CRL4 phenotype recorded. *Why it matters:* a genuine substrate-receptor deletion should perturb a defined CRL4 output. *Resolution:* targeted phenotyping of *dca7Δ* against known CRL4 readouts.
4. **Non-canonical DDB1 docking.** *Checked:* WDxR scan (absent). *Why it matters:* some DCAFs use non-WDxR helix-loop-helix docking; absence of WDxR is not absolute proof. *Resolution:* structural docking / cross-linking against Ddb1.

**Additional analysis limitations:** "No recorded interaction" reflects curated PomBase datasets, which are not exhaustive; a negative in databases is not a definitive experimental negative. The Ppk15 link rests on a single two-hybrid observation plus GO-level dual-specificity annotation. No wet-lab experiments were performed here; the analysis integrates public sequence, structure (AlphaFold), orthology, interaction, and literature evidence.

---

## Discriminating Tests

1. **Affinity purification–MS of endogenously tagged Dca7** in *S. pombe*: presence/absence of Ddb1, Pcu4/Cul4, Rik1, Cdt2 would directly settle the CRL4-membership question; enrichment of Ppk15/other kinases and Fft3 would support the scaffold model.
2. **Reciprocal tagging of Ddb1/Pcu4** to test whether Dca7 co-purifies with the CRL4 core under conditions where Raf1/Cdt2 do.
3. **Phenotypic epistasis:** compare *dca7Δ* to *cdt2Δ*/*ddb1Δ*/*raf1Δ* for Cdt1 stability, Spd1 degradation/dNTP levels, H3K9me/heterochromatin silencing, and DSB resection. A substrate-receptor role predicts a specific, shared CRL4 defect.
4. **Structure-guided docking / mutagenesis:** test any predicted Ddb1-contact surface; conversely map the Dca7–Ppk15 interface to the propeller-flanking regions used by WDR68 to bind DYRK1A.
5. **Cross-species complementation:** can Dca7 rescue *wdr68*/DCAF7 kinase-scaffold phenotypes but not CRL4-substrate phenotypes?

---

## Proposed Follow-up Actions / Curation Leads (require curator verification)

- **Candidate action change:** Reclassify GO:0080008 (Cul4-RING E3 ubiquitin ligase complex) on Dca7 as **non-core / low-confidence orthology transfer (ISS, GO_REF:0000024)**; do not treat it as evidence of a substrate-receptor molecular function. Do not assert an MF implying CRL4 substrate-adaptor activity.
- **Candidate reference + snippet to verify (criterion for real DCAFs):** [PMID: 16949367](https://pubmed.ncbi.nlm.nih.gov/16949367/) — *"the interaction of WD40-containing DCAFs with Ddb1 requires a conserved 'WDXR' motif."* Use to justify demoting Dca7 (WDxR absent).
- **Candidate reference + snippet (competing core function):** [PMID: 27307198](https://pubmed.ncbi.nlm.nih.gov/27307198/) — *"DCAF7 is an evolutionarily conserved protein with a single WD40 repeat domain and has no catalytic activity."*; [PMID: 20940704](https://pubmed.ncbi.nlm.nih.gov/20940704/) — *"identify Han11 as a novel scaffold protein regulating kinase signalling by HIPK2 and MEKK1."*
- **Candidate reference + snippet (balance):** [PMID: 25342745](https://pubmed.ncbi.nlm.nih.gov/25342745/) — WDR68 *"binds to several proteins, including... Cullin4-damage-specific DNA-binding protein 1 (CUL4-DDB1)."* Documents association but not substrate delivery.
- **Candidate new/alternative GO directions (ISS-level, for curator judgment):** a molecular-function reflecting **protein-kinase binding / kinase-scaffold activity**, and a biological-process reflecting **regulation of gene expression** — consistent with PomBase's "implicated in gene expression" descriptor and the Ppk15 interaction. Retain **GO:0005634 nucleus (IBA)**.
- **Suggested questions for curators:** Is GO:0080008 desired at all under local evidence standards? Should the gene's primary function annotation reflect the kinase-scaffold role instead? Is there any unpublished pombe co-IP linking Dca7 to Ddb1?
- **Suggested experiments:** Dca7 affinity-MS for CRL4 subunits vs. kinases; *dca7Δ* phenotyping against canonical CRL4 outputs; Dca7–Ppk15 interaction validation.

---

*Report generated from a 3-iteration autonomous investigation. Computational analyses (WDxR motif scan of O74763; AlphaFold AF-O74763-F1-model_v6 pLDDT parsing) were executed during the investigation; all literature attributions derive from verified PubMed abstract snippets recorded in the knowledge state.*


## Artifacts

- [OpenScientist dca7 evidence matrix](openscientist_artifacts/dca7_evidence_matrix.csv)
- [OpenScientist dca7 go decision table](openscientist_artifacts/dca7_go_decision_table.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
