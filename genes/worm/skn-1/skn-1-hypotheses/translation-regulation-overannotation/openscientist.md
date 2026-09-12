---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-21T21:31:35.395824'
end_time: '2026-06-21T22:09:49.839066'
duration_seconds: 2294.44
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: worm
  gene: skn-1
  gene_symbol: skn-1
  taxon_id: NCBITaxon:6239
  taxon_label: Caenorhabditis elegans
  focus_type: free_text
  hypothesis_slug: translation-regulation-overannotation
  hypothesis_text: C. elegans SKN-1 (P34707) carries an IEA annotation for regulation
    of translation (GO:0006417), but its established activity is as a bZIP / Nrf-like
    transcription factor acting on RNA polymerase II target genes (e.g. Phase II detoxification
    genes). Using protein-domain and sequence analysis (presence or absence of RNA-binding
    or translation-factor domains), transcription-factor target / regulon and co-expression
    evidence, and the literature, determine whether SKN-1 DIRECTLY regulates translation
    (supporting GO:0006417) or whether this IEA annotation is an over-annotation of
    an indirect, transcription-mediated effect. Consider isoform-specific roles (SKN-1A/B/C)
    if relevant.
  term_context: '- Term: regulation of translation (GO:0006417)'
  reference_context: No specific reference context supplied.
  source_file: ''
  source_selector: ''
  source_context_yaml: "hypothesis: C. elegans SKN-1 (P34707) carries an IEA annotation\
    \ for regulation of translation (GO:0006417),\n  but its established activity\
    \ is as a bZIP / Nrf-like transcription factor acting on RNA polymerase II\n \
    \ target genes (e.g. Phase II detoxification genes). Using protein-domain and\
    \ sequence analysis (presence\n  or absence of RNA-binding or translation-factor\
    \ domains), transcription-factor target / regulon and\n  co-expression evidence,\
    \ and the literature, determine whether SKN-1 DIRECTLY regulates translation (supporting\n\
    \  GO:0006417) or whether this IEA annotation is an over-annotation of an indirect,\
    \ transcription-mediated\n  effect. Consider isoform-specific roles (SKN-1A/B/C)\
    \ if relevant.\nfocus_type: free_text\nterm_id: GO:0006417\nterm_label: regulation\
    \ of translation\ncontext: []\nreference_id: []"
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

- **Organism code:** worm
- **Taxon:** Caenorhabditis elegans (NCBITaxon:6239)
- **Gene directory:** skn-1
- **Gene symbol:** skn-1

## Focus

- **Focus type:** free_text
- **Hypothesis slug:** translation-regulation-overannotation
- **Source file:** 
- **Source selector:** 

## Seed Hypothesis

C. elegans SKN-1 (P34707) carries an IEA annotation for regulation of translation (GO:0006417), but its established activity is as a bZIP / Nrf-like transcription factor acting on RNA polymerase II target genes (e.g. Phase II detoxification genes). Using protein-domain and sequence analysis (presence or absence of RNA-binding or translation-factor domains), transcription-factor target / regulon and co-expression evidence, and the literature, determine whether SKN-1 DIRECTLY regulates translation (supporting GO:0006417) or whether this IEA annotation is an over-annotation of an indirect, transcription-mediated effect. Consider isoform-specific roles (SKN-1A/B/C) if relevant.

## Term and Decision Context

- Term: regulation of translation (GO:0006417)

## Reference Context

No specific reference context supplied.

## Source Context YAML

```yaml
hypothesis: C. elegans SKN-1 (P34707) carries an IEA annotation for regulation of translation (GO:0006417),
  but its established activity is as a bZIP / Nrf-like transcription factor acting on RNA polymerase II
  target genes (e.g. Phase II detoxification genes). Using protein-domain and sequence analysis (presence
  or absence of RNA-binding or translation-factor domains), transcription-factor target / regulon and
  co-expression evidence, and the literature, determine whether SKN-1 DIRECTLY regulates translation (supporting
  GO:0006417) or whether this IEA annotation is an over-annotation of an indirect, transcription-mediated
  effect. Consider isoform-specific roles (SKN-1A/B/C) if relevant.
focus_type: free_text
term_id: GO:0006417
term_label: regulation of translation
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
prompt so the report can be compared against them after the run. Use whatever
public sequence, domain, structure, orthology, localization, interaction, or
dataset checks are useful for the specific hypothesis, and report computational
results conservatively.

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

If the provider supports artifacts, produce artifact-friendly tables such as an
evidence matrix, GO decision table, or comparison table. These artifacts are
important provenance for hypothesis-level review.


## Output

# Final Report: SKN-1 GO:0006417 (Regulation of Translation) Over-Annotation Analysis

## Executive Judgment

**Verdict: Over-annotated.** The GO:0006417 (regulation of translation) annotation on *C. elegans* SKN-1 (P34707) should be removed. Nine independent lines of evidence — spanning domain architecture, physical interactions, ortholog comparison, comprehensive literature analysis (53 papers), and GO term definition — converge on the conclusion that SKN-1 does not directly regulate translation. The annotation derives entirely from an automated electronic inference (IEA) via UniProtKB keyword KW-0810 ("Translation regulation"), with no experimental evidence code (IDA, IMP, IGI, etc.) supporting it. The most likely source of the erroneous keyword assignment is the well-documented biological relationship in which SKN-1 is activated *by* translation inhibition as a downstream transcriptional effector — a relationship that was apparently conflated with SKN-1 directly regulating translation. The most important caveat is that we cannot entirely exclude the possibility of an undiscovered, non-canonical, isoform-specific translational role; however, no current evidence supports such a function, and the protein lacks all recognized RNA-binding and translation-factor domains.

---

## Summary

*C. elegans* SKN-1 is a well-characterized bZIP/CNC-family transcription factor orthologous to mammalian NRF1 (NFE2L1) and NRF2 (NFE2L2). It functions as a master regulator of the oxidative stress response, Phase II detoxification, proteasome homeostasis (via the SKN-1A isoform), and embryonic cell fate specification — all through transcriptional activation of target genes. The protein carries GO annotations for DNA-binding transcription factor activity (GO:0003700), positive regulation of transcription by RNA polymerase II (GO:0045944), and numerous biological process terms reflecting its transcriptional outputs, all supported by experimental evidence.

However, UniProt entry P34707 also carries an IEA annotation for GO:0006417 (regulation of translation), inferred from keyword KW-0810. This annotation has no experimental backing. Our investigation systematically evaluated whether SKN-1 could directly regulate translation through nine complementary analyses: (1) annotation provenance, (2) protein domain architecture, (3) physical interaction partners, (4) transcriptional target analysis, (5) ortholog comparison, (6) GO term definition analysis, (7) comprehensive literature review (53 papers), (8) isoform-specific function assessment, and (9) mechanistic pathway tracing. Every line of evidence supports the conclusion that this is an over-annotation arising from conflation of SKN-1's role as a transcriptional responder to translation perturbation with direct translation regulation.

The curation recommendation is to remove GO:0006417 from P34707 and to flag UniProtKB keyword KW-0810 for removal from this entry. No replacement GO term related to translation is warranted; the existing transcription-related annotations accurately capture SKN-1's molecular function.

---

## Key Findings

### Finding 1: GO:0006417 Annotation is IEA-Only with No Curator Support

The GO:0006417 (regulation of translation) annotation on SKN-1 (P34707) exists solely as an IEA (Inferred from Electronic Annotation) derived from UniProtKB keyword KW-0810 ("Translation regulation"). A comprehensive search of QuickGO annotations for P34707 reveals that none of the 78 manually curated or experimentally supported GO annotations include GO:0006417. No curation authority — not WormBase, UniProt manual curation, BHF-UCL, nor any other contributing group — has submitted this annotation based on experimental evidence. This IEA-only provenance is the weakest category of GO evidence and is explicitly understood to require verification before being treated as reliable. The absence of any corroborating evidence code (IDA, IMP, IGI, IPI, TAS, etc.) across the entire annotation history of this well-studied gene is itself strong evidence against the annotation's validity.

### Finding 2: SKN-1 Lacks All RNA-Binding and Translation-Regulatory Domains

Comprehensive domain analysis of SKN-1 (P34707, 623 amino acids) across six major protein domain databases (InterPro, Pfam, Gene3D, SUPERFAMILY, PROSITE, and CDD) reveals that the protein contains exclusively DNA-binding and transcription factor domains:

| Database | Domain | Accession | Function |
|----------|--------|-----------|----------|
| Pfam | bZIP_Maf | PF03131 | DNA-binding transcription factor |
| InterPro | Basic leucine zipper | IPR004827 | Dimerization and DNA binding |
| InterPro | NFE2-like family | IPR047167 | NRF/CNC transcription factor family |
| InterPro | Skn-1-like DNA-binding superfamily | IPR008917 | DNA-binding domain |
| SUPERFAMILY | SSF47454 | — | Eukaryotic TF DNA-binding domain |
| PROSITE | BZIP_BASIC | PS00036 | Basic region of bZIP domain |

Critically, **no RNA-binding domains** (RRM, KH, CCCH zinc finger, dsRBD, Pumilio, DEAD-box), **no translation factor domains** (eIF, eEF, or any ribosome-associated domain), and **no ribosome-interaction motifs** were detected by any database. Proteins that directly regulate translation invariably possess at least one RNA-binding or translation-machinery interaction domain. The complete absence of such domains in SKN-1 is strong negative evidence against direct translation regulation.

### Finding 3: SKN-1 Functions Exclusively as a Transcription Factor Across All Isoforms

SKN-1 exists in three isoforms (SKN-1A, SKN-1B, SKN-1C), all of which function as transcription factors:

- **SKN-1C** is the canonical stress-responsive isoform that activates Phase II detoxification genes (gcs-1, gst-4, gst-7) in intestinal cells, functioning as the *C. elegans* ortholog of mammalian NRF2.
- **SKN-1A** is the longer isoform orthologous to mammalian NRF1/NFE2L1, which transcriptionally regulates proteasome subunit genes (e.g., rpt-3) in the conserved "bounce-back response" to proteasome dysfunction ([PMID: 27528192](https://pubmed.ncbi.nlm.nih.gov/27528192/)). As stated in that paper: *"In Caenorhabditis elegans, this response requires SKN-1, a transcription factor related to mammalian Nrf1/2."*
- **SKN-1B** is expressed in ASI neurons and contributes to dietary restriction-mediated longevity, again through transcriptional regulation.

ChIP-seq data from the modENCODE project ([PMID: 21177963](https://pubmed.ncbi.nlm.nih.gov/21177963/)) mapped SKN-1's genome-wide binding sites, confirming it binds DNA near transcription start sites as part of a study of 22 transcription factors. No isoform has been reported to bind RNA, interact with ribosomes, or directly modulate translation.

### Finding 4: Translation Inhibition Activates SKN-1 Transcriptionally — The Likely Source of Keyword Confusion

The most probable explanation for the erroneous KW-0810 keyword assignment is the well-documented biological relationship in which perturbation of translation activates SKN-1 as a downstream transcriptional effector:

- **Wang et al. 2010** ([PMID: 20700440](https://pubmed.ncbi.nlm.nih.gov/20700440/)) demonstrated that *"translation initiation factor RNAi robustly induces SKN-1 target gene transcription and confers skn-1-dependent oxidative stress resistance."* This paper explicitly shows SKN-1 is activated **by** translation inhibition and responds via transcription — not that SKN-1 regulates translation.

- **Rieckher et al. 2018** ([PMID: 30282029](https://pubmed.ncbi.nlm.nih.gov/30282029/)) showed that *"The effects of mRNA decapping deficiency on stress resistance and longevity are orchestrated by a multimodal stress response involving the transcription factor SKN-1, which mediates lifespan extension upon reduced protein synthesis."* Again, SKN-1 is a transcriptional mediator of the cellular response to reduced protein synthesis.

The directionality is critical: translation perturbation → stress signaling → SKN-1 activation → transcriptional output. SKN-1 is downstream of translation regulation, not upstream. Automated keyword extraction likely captured the association between SKN-1 and "translation" without encoding the correct causal direction.

Additionally, during embryogenesis, SKN-1 protein itself is subject to translational regulation by MEX-3 and other CCCH zinc-finger proteins ([PMID: 11830574](https://pubmed.ncbi.nlm.nih.gov/11830574/)). This is SKN-1 *being regulated* at the translational level, not SKN-1 *regulating* translation — another potential source of keyword confusion.

### Finding 5: Mammalian Orthologs NRF1/NRF2 Lack GO:0006417 and KW-0810

Human NRF1/NFE2L1 (Q14494) and NRF2/NFE2L2 (Q16236) share the identical domain architecture with SKN-1 (bZIP, bZIP_Maf, NFE2-like, TF_DNA-bd_sf) and perform conserved transcriptional functions. Neither carries the KW-0810 keyword nor the GO:0006417 annotation. Given the strong functional conservation of the NRF/CNC transcription factor family, the absence of translation-regulatory annotation on the mammalian orthologs — which have been far more extensively studied — further supports the conclusion that the annotation on SKN-1 is erroneous rather than reflecting a *C. elegans*-specific function.

### Finding 6: SKN-1 Transcriptional Target RIOK-1 Provides Only an Indirect Link to Ribosome Biogenesis

The closest connection between SKN-1 and translation machinery is its transcriptional regulation of *riok-1*, a RIO protein kinase involved in rRNA processing and 40S ribosomal subunit maturation ([PMID: 25688864](https://pubmed.ncbi.nlm.nih.gov/25688864/)). As stated in that paper: *"the intestinal expression of riok-1 was dependent upon two putative binding sites for the oxidative and xenobiotic stress response transcription factor SKN-1."*

However, this represents a multi-step indirect pathway:

```
SKN-1 --[transcription]--> riok-1 mRNA --[translation]--> RIOK-1 protein
    --[rRNA processing]--> 40S ribosome maturation --[ribosome availability]--> translation capacity
```

By this logic, any transcription factor whose targets include ribosome biogenesis genes would qualify for GO:0006417, which would dramatically over-extend the term. The GO:0006417 definition requires **direct modulation** of translation frequency, rate, or extent — not transcriptional regulation of a gene whose protein product is two steps removed from translation.

### Finding 7: Nucleolar Disruption Activates SKN-1 Independently of Translation

Leung et al. 2012 ([PMID: 22240150](https://pubmed.ncbi.nlm.nih.gov/22240150/)) provided critical mechanistic evidence, demonstrating that disruption of nucleolar function (WDR-46, involved in 18S rRNA processing) activates SKN-1 and its target gene gst-4. Crucially, the paper states: *"disruptions to nucleolar function can activate SKN-1 by a mechanism that involves p53/cep-1 and is independent of protein translation."* This directly demonstrates that SKN-1 is a transcriptional responder activated by ribosome/translation perturbation through stress signaling pathways — not a protein that directly modulates translation.

### Finding 8: No Physical Interactions with Translation Machinery

IntAct PSICQUIC database queries returned 10 interaction records for SKN-1 (P34707). These include protein-protein interactions (yeast two-hybrid) with NMAD-1 (RNA demethylase), and DNA-binding interactions (one-hybrid) with regulatory regions of target genes. UniProt records interactions with ELT-3 (GATA transcription factor), PGMA-5 (phosphoglycerate mutase), and MXL-3 (transcription factor). **No interactions were detected with translation initiation factors (eIFs), elongation factors (eEFs), ribosomal proteins, or any mRNA-binding proteins involved in translational control.** Proteins that directly regulate translation typically show robust physical interactions with translation machinery components.

### Finding 9: GO:0006417 Definition Requires Direct Translation Modulation

GO:0006417 is defined as: *"Any process that modulates the frequency, rate or extent of the chemical reactions and pathways resulting in the formation of proteins by the translation of mRNA or circRNA."* This requires direct modulation of the translation process itself. SKN-1's only connections to translation are:

1. Being activated as a transcriptional effector when translation is inhibited (indirect; wrong direction)
2. Being itself subject to translational control during embryogenesis (SKN-1 is the target, not the regulator)
3. Transcriptionally regulating *riok-1*, a ribosome maturation factor (two-step indirect effect)

None of these constitute direct modulation of translation frequency, rate, or extent as required by the GO term definition.

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|--------------|-------------|---------|------------|
| 1 | UniProt P34707; QuickGO | Database/computational | Supports over-annotation | Is GO:0006417 experimentally supported? | IEA-only; no curator submission among 78 annotations | *C. elegans*, all tissues | High — comprehensive database search |
| 2 | InterPro, Pfam, PROSITE, SUPERFAMILY, Gene3D, CDD | Structural/evolutionary | Supports over-annotation | Does SKN-1 have RNA-binding or translation domains? | Only DNA-binding/bZIP domains; no RNA-binding or translation factor domains | Sequence analysis | High — 6 databases concordant |
| 3 | [PMID: 27528192](https://pubmed.ncbi.nlm.nih.gov/27528192/) | Direct assay (mutant + molecular) | Supports over-annotation | Is SKN-1A a translation regulator? | SKN-1A is a transcription factor regulating proteasome genes | *C. elegans*, intestine | High — mechanistic study |
| 4 | [PMID: 20700440](https://pubmed.ncbi.nlm.nih.gov/20700440/) | Direct assay (RNAi screen) | Supports over-annotation | Does SKN-1 regulate translation? | Translation inhibition activates SKN-1 *transcriptional* response | *C. elegans*, whole organism | High — directly tests relationship |
| 5 | [PMID: 30282029](https://pubmed.ncbi.nlm.nih.gov/30282029/) | Direct assay (genetic) | Supports over-annotation | Does SKN-1 regulate translation? | SKN-1 is transcriptional mediator of response to reduced protein synthesis | *C. elegans*, whole organism | High — mechanistic study |
| 6 | [PMID: 22240150](https://pubmed.ncbi.nlm.nih.gov/22240150/) | Direct assay (genetic) | Supports over-annotation | Is SKN-1 activation linked to translation? | SKN-1 activation by nucleolar disruption is *independent of translation* | *C. elegans*, intestine | High — directly discriminating |
| 7 | [PMID: 21177963](https://pubmed.ncbi.nlm.nih.gov/21177963/) | Direct assay (ChIP-seq) | Supports over-annotation | Where does SKN-1 bind? | SKN-1 binds DNA near TSS; profiled as 1 of 22 TFs | *C. elegans*, L1-L2 larvae | High — genome-wide |
| 8 | [PMID: 25688864](https://pubmed.ncbi.nlm.nih.gov/25688864/) | Direct assay (reporter/binding sites) | Qualifies | Does SKN-1 connect to ribosome biogenesis? | SKN-1 transcriptionally regulates *riok-1* (ribosome maturation factor) | *C. elegans*, intestine | Moderate — indirect link only |
| 9 | [PMID: 11830574](https://pubmed.ncbi.nlm.nih.gov/11830574/) | Direct assay (genetic) | Qualifies | Is SKN-1 involved in translational regulation? | SKN-1 protein is *translationally regulated* by MEX-3, not a translation regulator itself | *C. elegans*, early embryo | High — direction is clear |
| 10 | UniProt Q14494 (NRF1), Q16236 (NRF2) | Computational/orthology | Supports over-annotation | Do orthologs have GO:0006417? | Neither NRF1 nor NRF2 carry KW-0810 or GO:0006417 despite identical domains | Human | High — conserved family |
| 11 | IntAct PSICQUIC | Database/interaction | Supports over-annotation | Does SKN-1 interact with translation factors? | No interactions with eIFs, eEFs, or ribosomal proteins | *C. elegans* | Moderate — absence of evidence |
| 12 | [PMID: 32502151](https://pubmed.ncbi.nlm.nih.gov/32502151/) | Direct assay (genetic/electrophysiology) | Supports over-annotation | Does SKN-1A regulate translation? | SKN-1A/NRF1 transcriptionally controls proteasome levels affecting ERAD | *C. elegans*, neurons | High — mechanistic, confirms TF role |
| 13 | [PMID: 38466732](https://pubmed.ncbi.nlm.nih.gov/38466732/) | Direct assay (genetic/immune) | Supports over-annotation | What does SKN-1A regulate? | SKN-1A regulates proteasomal gene expression; loss affects innate immunity | *C. elegans*, epidermis/intestine | High — functional genomics |
| 14 | [PMID: 9015263](https://pubmed.ncbi.nlm.nih.gov/9015263/) | Mutant phenotype | Supports over-annotation | Do skn-1 mutants affect GLP-1 translation? | skn-1 mutants do not affect translational control of GLP-1 in embryo | *C. elegans*, early embryo | Moderate — negative evidence |
| 15 | [PMID: 25643626](https://pubmed.ncbi.nlm.nih.gov/25643626/) | Direct assay (genetic) | Qualifies | GCN-2 and SKN-1 in longevity | GCN-2 regulates translation; SKN-1 regulates transcription. Parallel pathways | *C. elegans*, lifespan | High — distinguishes parallel pathways |
| 16 | STRING network analysis | Computational (network) | Supports over-annotation | SKN-1 functional interaction partners | Top 20 partners are kinases, TFs, and target genes. No translation machinery | *C. elegans*, STRING | Moderate — functional associations |
| 17 | GO:0006417 definition (QuickGO) | Database/computational | Supports over-annotation | Does SKN-1 activity fit the GO term? | Term requires direct modulation of translation; SKN-1 does not do this | GO ontology | High — unambiguous definition |

---

## GO Curation Implications

### Primary Recommendation: Remove GO:0006417

**Action:** The IEA annotation GO:0006417 (regulation of translation) should be removed from P34707 (SKN-1). The supporting UniProtKB keyword KW-0810 (Translation regulation) should also be reviewed for removal from this entry.

**Rationale:**
1. The annotation has only IEA evidence from keyword mapping — no experimental evidence supports it.
2. SKN-1 lacks all expected molecular features of a translation regulator (no RNA-binding domains, no translation factor domains).
3. All established molecular functions are DNA-binding transcription factor activities.
4. No curation authority (WormBase, UniProt manual curators, etc.) has submitted this annotation.
5. The connection to translation is exclusively indirect — SKN-1 transcriptionally responds to translation inhibition.
6. Mammalian orthologs with identical domain architecture lack this annotation.

### GO Decision Table

| GO Term | Current Status | Evidence Codes | Recommendation | Rationale | Confidence |
|---------|---------------|----------------|----------------|-----------|------------|
| GO:0006417 (regulation of translation) | Annotated (IEA:UniProtKB-KW) | IEA only | **REMOVE** | No direct translation regulatory activity; IEA from erroneous KW-0810; no RNA-binding domains; no translation factor interactions; mammalian orthologs lack this annotation | Very High |
| GO:0003700 (DNA-binding TF activity) | Annotated (NAS) | NAS:UniProtKB | **RETAIN** | Well-established, foundational function | Very High |
| GO:0000981 (DNA-binding TF activity, RNAPII-specific) | Annotated (IBA) | IBA:GO_Central | **RETAIN** | Supported by phylogenetic inference and direct evidence | High |
| GO:0000978 (RNAPII cis-regulatory region DNA binding) | Annotated (IDA) | IDA:UniProtKB | **RETAIN** | Direct experimental evidence (ChIP-seq, EMSA) | Very High |
| GO:0045944 (positive regulation of transcription by RNAPII) | Annotated (IMP) | IMP:UniProtKB, IMP:WormBase | **RETAIN** | Multiple IMP evidence from independent groups | Very High |
| GO:0006351 (DNA-templated transcription) | Annotated (IEA:UniProtKB-KW) | IEA only | RETAIN (but upgrade evidence) | Correct annotation but IEA; ample experimental support exists | High |
| KW-0810 (Translation regulation) | Present in UniProt | Keyword | **REMOVE from UniProt** | No basis in function description or literature; likely curation error | Very High |

### Possible New Annotation

If curators wish to capture SKN-1's role in the cellular response to translation inhibition (an indirect relationship), the most appropriate annotation would be **GO:0006950** (response to stress) with an annotation extension indicating the stimulus is translation inhibition, referencing [PMID: 20700440](https://pubmed.ncbi.nlm.nih.gov/20700440/). The term GO:0032055 (regulation of translation in response to stress) should **not** be used because SKN-1's response to translation stress is itself transcriptional, not translational.

---

## Mechanistic Scope

### Direct Molecular Activity

SKN-1 is a **sequence-specific DNA-binding transcription factor** of the CNC-bZIP family. Its immediate molecular activity is:

1. **DNA binding** via the bZIP/CNC domain to antioxidant response elements (AREs) and related cis-regulatory sequences
2. **Transcriptional activation** of target genes including Phase II detoxification enzymes (gcs-1, gst-4, gst-7), proteasome subunits (rpt-3, via SKN-1A), metabolic genes, and embryonic patterning genes (med-1, med-2)

### Separation from Downstream Effects

The following are downstream consequences of SKN-1 transcriptional activity, NOT direct molecular functions:

| Level | Example | Relationship to SKN-1 |
|-------|---------|----------------------|
| Direct MF | Binds ARE DNA sequences | SKN-1 performs this |
| Direct BP | Activates transcription of gcs-1 | SKN-1 performs this |
| Downstream 1 | GCS-1 synthesizes glutathione | Product of SKN-1 target gene |
| Downstream 2 | Glutathione detoxifies ROS | Two steps removed |
| Downstream 1 | RIOK-1 processes rRNA | Product of SKN-1 target gene |
| Downstream 2 | Mature 40S subunits enable translation | Two steps removed |
| Phenotype | Lifespan extension, stress resistance | Multi-step consequence |

The GO:0006417 annotation conflates SKN-1's indirect, transcription-mediated effect on ribosome biogenesis (via *riok-1*) and its role as a stress-responsive transcription factor activated by translation perturbation with direct regulation of translation.

### Causal Pathway Diagram

```
ACTUAL BIOLOGY (SKN-1 is DOWNSTREAM of translation perturbation):

Translation inhibition (e.g., eIF RNAi)
        │
        ▼
   Stress signaling (p38/PMK-1, mTOR)
        │
        ▼
   SKN-1 nuclear translocation & activation
        │
        ▼
   TRANSCRIPTIONAL activation of target genes
        │
        ├──► gcs-1, gst-4 (detoxification)
        ├──► rpt-3 (proteasome subunits, via SKN-1A)
        └──► riok-1 (ribosome maturation factor)

MISINTERPRETATION (what GO:0006417 implies):

   SKN-1 ──[DIRECTLY]──► Regulates translation
   (This does NOT occur)
```

---

## Conflicts and Alternatives

### Potential Counterarguments Evaluated

**1. Could SKN-1 have an undiscovered RNA-binding function?**
Some transcription factors have been found to moonlight as RNA-binding proteins. However, SKN-1 lacks any of the recognized RNA-binding domain folds (RRM, KH, CCCH zinc finger, dsRBD, Pumilio). The bZIP domain binds double-stranded DNA and has not been reported to bind RNA in any CNC/NRF family member. While we cannot entirely exclude a cryptic RNA-binding activity, the complete absence of domain evidence and the lack of any experimental report across decades of study makes this highly unlikely.

**2. Could SKN-1A have an isoform-specific translation role?**
SKN-1A is the longest isoform and is orthologous to mammalian NRF1/NFE2L1. It has a unique N-terminal extension that mediates ER membrane association and DDI-1-dependent cleavage for proteasome gene regulation ([PMID: 27528192](https://pubmed.ncbi.nlm.nih.gov/27528192/), [PMID: 32502151](https://pubmed.ncbi.nlm.nih.gov/32502151/), [PMID: 38466732](https://pubmed.ncbi.nlm.nih.gov/38466732/)). This is a well-characterized transcriptional function. No evidence suggests any isoform has translational regulatory activity.

**3. Could the RIOK-1 connection justify GO:0006417?**
SKN-1 transcriptionally regulates *riok-1* ([PMID: 25688864](https://pubmed.ncbi.nlm.nih.gov/25688864/)), which is involved in ribosome maturation. However, this is a two-step indirect connection: SKN-1 → riok-1 transcription → RIOK-1 protein → ribosome maturation → translation capacity. GO annotation guidelines require direct participation in the process, not transcriptional regulation of an upstream factor. By the same logic, any transcription factor regulating ribosomal protein genes would carry GO:0006417, which would be clearly inappropriate.

**4. Could the keyword have been assigned correctly based on now-superseded evidence?**
A thorough literature search of 53 papers, including the earliest SKN-1 studies from the 1990s through 2024, found no paper reporting direct translation regulation by SKN-1. The keyword assignment appears to be an automated inference error, not a reflection of historical evidence that was later overturned.

**5. Paralog confusion or organism-specific differences?**
There are no close paralogs of SKN-1 in *C. elegans* that could cause confusion. The NRF/CNC family in worms consists of SKN-1 alone, unlike mammals which have NRF1, NRF2, NRF3, and other CNC members. No organism-specific translation-regulatory function has been reported.

**6. SKN-1A ER association as a translational nexus?**
SKN-1A is ER-membrane-associated before cleavage ([PMID: 27528192](https://pubmed.ncbi.nlm.nih.gov/27528192/)), and the ER is a site of co-translational protein insertion. However, SKN-1A's ER association is for regulated processing (glycosylation-dependent sensing of proteasome dysfunction), not for translation regulation. After cleavage by DDI-1, SKN-1A translocates to the nucleus where it functions as a transcription factor.

**7. SKN-1 in embryonic translational regulation circuits?**
SKN-1 protein distribution in early embryos is controlled by translational regulation of skn-1 mRNA via MEX-3 and other RNA-binding proteins ([PMID: 11830574](https://pubmed.ncbi.nlm.nih.gov/11830574/); [PMID: 9015263](https://pubmed.ncbi.nlm.nih.gov/9015263/)). However, SKN-1 is a **target** of translational regulation during embryogenesis, not a regulator of translation. Notably, Crittenden et al. 1997 ([PMID: 9015263](https://pubmed.ncbi.nlm.nih.gov/9015263/)) found that skn-1 mutants do **not** affect translational control of GLP-1 in the early embryo, providing direct negative evidence.

### Source of Keyword Confusion: Two Biological Contexts

Two biological contexts likely contributed to the erroneous KW-0810 assignment:

1. **Translation inhibition → SKN-1 activation pathway**: Wang et al. (2010, [PMID: 20700440](https://pubmed.ncbi.nlm.nih.gov/20700440/)) and Rieckher et al. (2018, [PMID: 30282029](https://pubmed.ncbi.nlm.nih.gov/30282029/)) demonstrated that inhibition of mRNA translation activates SKN-1-dependent transcription. This creates a functional link between SKN-1 and "regulation of translation" in the literature, but the directionality is reversed — SKN-1 is regulated BY translation status, it does not regulate translation.

2. **Embryonic translational regulation of SKN-1 itself**: SKN-1 protein distribution in early embryos is controlled by translational regulation of skn-1 mRNA (via MEX-3, PAR genes, etc.). SKN-1 is a TARGET of translational regulation during embryogenesis, not a regulator of translation.

---

## Evidence Base: Key Literature

### Papers Directly Testing the Relationship

- **Wang et al. 2010** ([PMID: 20700440](https://pubmed.ncbi.nlm.nih.gov/20700440/)) — *"RNAi screening implicates a SKN-1-dependent transcriptional response in stress resistance and longevity deriving from translation inhibition."* This is the single most relevant paper. It demonstrates that inhibiting translation initiation factors activates SKN-1-dependent **transcription**, not that SKN-1 regulates translation. The title itself encodes the correct causal direction. Key quote: *"translation initiation factor RNAi robustly induces SKN-1 target gene transcription and confers skn-1-dependent oxidative stress resistance."*

- **Rieckher et al. 2018** ([PMID: 30282029](https://pubmed.ncbi.nlm.nih.gov/30282029/)) — *"Maintenance of Proteostasis by P Body-Mediated Regulation of eIF4E Availability during Aging in Caenorhabditis elegans."* Shows SKN-1 mediates the transcriptional arm of the stress response to reduced protein synthesis. Key quote: *"The effects of mRNA decapping deficiency on stress resistance and longevity are orchestrated by a multimodal stress response involving the transcription factor SKN-1, which mediates lifespan extension upon reduced protein synthesis."*

- **Leung et al. 2012** ([PMID: 22240150](https://pubmed.ncbi.nlm.nih.gov/22240150/)) — *"Depletion of a nucleolar protein activates xenobiotic detoxification genes in Caenorhabditis elegans via Nrf/SKN-1 and p53/CEP-1."* Provides critical evidence that SKN-1 activation by nucleolar disruption is *independent of protein translation*. Key quote: *"disruptions to nucleolar function can activate SKN-1 by a mechanism that involves p53/cep-1 and is independent of protein translation."*

### Papers Establishing SKN-1 as a Transcription Factor

- **Lehrbach & Ruvkun 2016** ([PMID: 27528192](https://pubmed.ncbi.nlm.nih.gov/27528192/)) — Establishes SKN-1A as a transcription factor in the proteasome bounce-back response, activated by aspartic protease DDI-1 cleavage.

- **Niu et al. 2011** ([PMID: 21177963](https://pubmed.ncbi.nlm.nih.gov/21177963/)) — modENCODE ChIP-seq profiling of SKN-1 genome-wide binding sites confirms DNA-binding transcription factor function.

- **Doering et al. 2020** ([PMID: 32502151](https://pubmed.ncbi.nlm.nih.gov/32502151/)) — Shows SKN-1A/NRF1-mediated transcriptional mechanism controls proteasome levels, which indirectly affects BK channel density via ERAD.

- **Grover et al. 2024** ([PMID: 38466732](https://pubmed.ncbi.nlm.nih.gov/38466732/)) — SKN-1A regulates proteasomal gene expression; loss-of-function causes constitutive expression of innate immune programs.

- **Wu et al. 2021** ([PMID: 34407394](https://pubmed.ncbi.nlm.nih.gov/34407394/)) — SKN-1 is a protective transcription factor in intestinal immunity, regulated by p38 MAPK phosphorylation.

### Papers on SKN-1 Translational Regulation (SKN-1 as Target, Not Regulator)

- **Huang et al. 2002** ([PMID: 11830574](https://pubmed.ncbi.nlm.nih.gov/11830574/)) — MEX-3 interacting proteins (MEX-6, SPN-4) link cell polarity to asymmetric gene expression; SKN-1 protein is translationally regulated during embryogenesis, but SKN-1 does not itself regulate translation.

- **Crittenden et al. 1997** ([PMID: 9015263](https://pubmed.ncbi.nlm.nih.gov/9015263/)) — Mutants affecting anterior-posterior asymmetry disrupt GLP-1 translational control, but *skn-1 mutants do not affect the GLP-1 pattern* — negative evidence for SKN-1's role in translation regulation.

- **Mootz et al. 2004** ([PMID: 15201219](https://pubmed.ncbi.nlm.nih.gov/15201219/)) — GLD-1 mediates translational control of PAL-1; relevant context showing translational regulation of embryonic determinants, but not by SKN-1.

### Broader SKN-1/NRF Literature

Across all 53 papers reviewed — spanning topics from stress resistance and longevity, to detoxification, embryonic patterning, proteasome regulation, innate immunity, and metabolic regulation — **every paper describes SKN-1 exclusively as a transcription factor**. The papers from the nutraceutical/longevity field (constituting roughly half the literature) consistently describe SKN-1 as a transcriptional mediator of stress responses. Some papers use phrases like "up-regulating the translation of SKN-1 mRNA" ([PMID: 37316035](https://pubmed.ncbi.nlm.nih.gov/37316035/)), referring to SKN-1 protein production (i.e., translation of SKN-1's own mRNA), not SKN-1 regulating translation of other mRNAs.

---

## Limitations and Knowledge Gaps

### Limitations of This Analysis

1. **Absence of evidence vs. evidence of absence:** While no evidence supports direct translation regulation by SKN-1, we cannot prove a negative with certainty. An undiscovered, non-canonical function remains formally possible, though all available evidence argues against it.

2. **Interaction database coverage:** Physical interaction databases (IntAct, BioGRID) have incomplete coverage. Undiscovered interactions with translation machinery cannot be fully excluded without comprehensive proteomics studies (AP-MS, BioID/TurboID).

3. **Literature search scope:** While 53 papers were reviewed, the complete *C. elegans* SKN-1 literature likely exceeds 200 papers. However, the most relevant mechanistic studies were captured, and the consistency of findings across all reviewed papers is strong.

4. **KW-0810 assignment rationale:** We could not determine exactly why or when UniProt assigned the KW-0810 keyword to P34707. Understanding the rationale would help prevent similar errors.

### Knowledge Gaps Relevant to Curation

| Gap | What Was Checked | Why It Matters | Resolution |
|-----|-----------------|----------------|------------|
| Origin of KW-0810 assignment | UniProt entry, function description, all references | Understanding the historical basis could prevent recurrence | Contact UniProt curators |
| Whether SKN-1 transcriptional targets include core translation factor genes | Literature search; modENCODE targets; known regulon | If SKN-1 directly transcribes eIF/eEF genes, a qualified annotation might be warranted | Full cross-reference of ChIP-seq targets with translation machinery genes |
| No CLIP-seq/RIP-seq data for SKN-1 | PubMed searches; domain analysis | Would definitively rule out RNA binding | eCLIP or iCLIP of SKN-1 |
| Whether any SKN-1 isoform has non-transcriptional roles | Literature search for all isoforms | Isoform-specific functions could theoretically include translation regulation | Comprehensive molecular characterization of all isoforms |
| Polysome profiling in skn-1 mutants | Not performed | Would detect direct effects on translation | Ribo-seq comparing wild-type and skn-1(-) |

---

## Proposed Follow-up Experiments/Actions

### Immediate Curation Actions

1. **Submit annotation correction** to UniProt/GOA to remove GO:0006417 from P34707
2. **Submit keyword correction** to UniProt to remove KW-0810 from P34707
3. **Consider adding a NOT annotation** for GO:0006417 with evidence code IEA-reviewed or TAS, citing [PMID: 20700440](https://pubmed.ncbi.nlm.nih.gov/20700440/) and [PMID: 22240150](https://pubmed.ncbi.nlm.nih.gov/22240150/), to explicitly record that this function was evaluated and rejected

### Systematic Quality Control

4. **Audit other *C. elegans* transcription factors** for similar GO:0006417 over-annotations derived from KW-0810
5. **Review KW-0810 assignment criteria** — the keyword "Translation regulation" may be too broadly applied to proteins that participate in translation-related biological contexts without directly regulating translation

### Discriminating Experiments (If Desired)

6. **eCLIP-seq of tagged SKN-1 isoforms** — Would definitively determine whether SKN-1 binds any mRNAs in vivo. Prediction: negative (no RNA-binding domains). A negative result closes the question.

7. **Polysome profiling in skn-1 mutants vs. wild-type** — If SKN-1 directly regulates translation, global or specific changes in polysome occupancy should be detectable. This would distinguish direct translation regulation from transcriptional effects.

8. **Ribosome footprinting (Ribo-seq) comparing skn-1 mutant and wild-type** — Would detect changes in translational efficiency at specific mRNAs, distinguishing transcriptional from translational effects.

9. **In vitro translation assay with purified SKN-1** — Adding recombinant SKN-1 to an in vitro translation system would test whether SKN-1 can directly modulate translation. This is the gold-standard for demonstrating direct translation regulation.

10. **Tethered function assay** — Fusing SKN-1 to a bacteriophage coat protein (e.g., MS2) and measuring its effect on translation of a reporter mRNA bearing coat protein binding sites would test for any intrinsic translational regulatory activity.

---

## Curation Leads

### Lead 1: Remove GO:0006417 (HIGH CONFIDENCE)
- **Action:** Remove GO:0006417 (regulation of translation) from P34707
- **Rationale:** IEA-only evidence from KW-0810; no experimental support; domain analysis contradicts; all known activities are transcriptional; mammalian orthologs lack annotation
- **Curator verification needed:** Confirm KW-0810 keyword should also be removed from UniProt entry

### Lead 2: Remove KW-0810 from UniProt Entry (HIGH CONFIDENCE)
- **Action:** Contact UniProt to remove keyword KW-0810 (Translation regulation) from P34707
- **Rationale:** Function description mentions no translation-related activity; all references describe transcription factor function; keyword appears to be historical misassignment

### Lead 3: Retain Existing Transcription-Related GO Terms (RETAIN)
- **Action:** Keep GO:0003700, GO:0000981, GO:0000978, GO:0045944 with current evidence codes
- **Rationale:** Well-supported by multiple experimental evidence types (IDA, IMP, NAS, IBA)

### Lead 4: Candidate References for Verification

| PMID | Exact Snippet | Relevance |
|------|--------------|-----------|
| [20700440](https://pubmed.ncbi.nlm.nih.gov/20700440/) | *"translation initiation factor RNAi robustly induces SKN-1 target gene transcription and confers skn-1-dependent oxidative stress resistance"* | Demonstrates SKN-1 is activated BY translation inhibition as a transcriptional effector |
| [30282029](https://pubmed.ncbi.nlm.nih.gov/30282029/) | *"The effects of mRNA decapping deficiency on stress resistance and longevity are orchestrated by a multimodal stress response involving the transcription factor SKN-1, which mediates lifespan extension upon reduced protein synthesis"* | Confirms transcriptional mediator role in response to reduced protein synthesis |
| [22240150](https://pubmed.ncbi.nlm.nih.gov/22240150/) | *"disruptions to nucleolar function can activate SKN-1 by a mechanism that involves p53/cep-1 and is independent of protein translation"* | SKN-1 activation is independent of translation — it is a stress-responsive TF |
| [27528192](https://pubmed.ncbi.nlm.nih.gov/27528192/) | *"In Caenorhabditis elegans, this response requires SKN-1, a transcription factor related to mammalian Nrf1/2"* | SKN-1A is a transcription factor in the proteasome bounce-back response |
| [25688864](https://pubmed.ncbi.nlm.nih.gov/25688864/) | *"the intestinal expression of riok-1 was dependent upon two putative binding sites for the oxidative and xenobiotic stress response transcription factor SKN-1"* | Closest link to translation is indirect (transcriptional regulation of ribosome biogenesis factor) |
| [21177963](https://pubmed.ncbi.nlm.nih.gov/21177963/) | *"we have used chromatin immunoprecipitation coupled with high-throughput DNA sequencing (ChIP-seq) to determine the genome-wide binding sites of 22 transcription factors"* | Genome-wide confirmation of DNA-binding TF function |

### Lead 5: Suggested Questions for Curator Review
1. Should WormBase flag P34707's KW-0810 keyword to UniProt for review?
2. Are there other *C. elegans* transcription factors carrying GO:0006417 via IEA that may represent similar over-annotations?
3. Should a NOT annotation (GO:0006417 with NOT qualifier) be added to explicitly record that this function was evaluated and rejected?
4. Does the indirect connection via *riok-1* transcriptional regulation warrant any annotation, or is the two-step distance too great?

---

*Report generated from 3 iterations of systematic investigation, reviewing 53 papers and recording 9 confirmed findings. All evidence converges on the conclusion that GO:0006417 is an over-annotation on SKN-1 (P34707).*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)