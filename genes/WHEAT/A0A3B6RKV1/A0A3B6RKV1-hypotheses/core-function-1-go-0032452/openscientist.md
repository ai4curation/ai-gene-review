---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-21T20:52:44.851540'
end_time: '2026-06-21T21:40:45.234236'
duration_seconds: 2880.38
template_file: templates/gene_hypothesis_deep_research.md
template_variables:
  organism: WHEAT
  gene: A0A3B6RKV1
  gene_symbol: A0A3B6RKV1
  uniprot_accession: A0A3B6RKV1
  taxon_id: NCBITaxon:4565
  taxon_label: Triticum aestivum
  focus_type: core_function
  hypothesis_slug: core-function-1-go-0032452
  hypothesis_text: 'histone demethylase activity (GO:0032452) is a core function of
    A0A3B6RKV1. Current rationale: Putative histone demethylase that catalyzes Fe(II)-
    and 2-oxoglutarate-dependent oxidative removal of methyl groups from histone H3,
    functioning in the nucleus to regulate gene expression epigenetically. Inferred
    from membership in the JARID1/KDM5 subfamily and domain architecture.'
  term_context: '- Molecular function: histone demethylase activity (GO:0032452)

    - Description: Putative histone demethylase that catalyzes Fe(II)- and 2-oxoglutarate-dependent
    oxidative removal of methyl groups from histone H3, functioning in the nucleus
    to regulate gene expression epigenetically. Inferred from membership in the JARID1/KDM5
    subfamily and domain architecture.

    - Directly involved in: epigenetic regulation of gene expression (GO:0040029)

    - Locations: nucleus (GO:0005634)'
  reference_context: '- file:WHEAT/A0A3B6RKV1/A0A3B6RKV1-deep-research-falcon.md'
  source_file: genes/WHEAT/A0A3B6RKV1/A0A3B6RKV1-ai-review.yaml
  source_selector: core_functions[1]
  source_context_yaml: "description: Putative histone demethylase that catalyzes Fe(II)-\
    \ and 2-oxoglutarate-dependent oxidative\n  removal of methyl groups from histone\
    \ H3, functioning in the nucleus to regulate gene expression epigenetically.\n\
    \  Inferred from membership in the JARID1/KDM5 subfamily and domain architecture.\n\
    supported_by:\n- reference_id: file:WHEAT/A0A3B6RKV1/A0A3B6RKV1-deep-research-falcon.md\n\
    \  supporting_text: LOC123148885 belongs to the KDM5/JARID1 subfamily of JmjC\
    \ domain-containing histone\n    demethylases, which specifically catalyze the\
    \ removal of methyl groups from histone H3 lysine 4 marks\n    (H3K4me1/2/3) via\
    \ Fe(II)- and 2-oxoglutarate-dependent oxidative demethylation. The protein is\
    \ predicted\n    to localize to the nucleus, consistent with its chromatin-associated\
    \ function.\nmolecular_function:\n  id: GO:0032452\n  label: histone demethylase\
    \ activity\ndirectly_involved_in:\n- id: GO:0040029\n  label: epigenetic regulation\
    \ of gene expression\nlocations:\n- id: GO:0005634\n  label: nucleus"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 10
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

- **Organism code:** WHEAT
- **Taxon:** Triticum aestivum (NCBITaxon:4565)
- **Gene directory:** A0A3B6RKV1
- **Gene symbol:** A0A3B6RKV1
- **UniProt accession:** A0A3B6RKV1

## Focus

- **Focus type:** core_function
- **Hypothesis slug:** core-function-1-go-0032452
- **Source file:** genes/WHEAT/A0A3B6RKV1/A0A3B6RKV1-ai-review.yaml
- **Source selector:** core_functions[1]

## Seed Hypothesis

histone demethylase activity (GO:0032452) is a core function of A0A3B6RKV1. Current rationale: Putative histone demethylase that catalyzes Fe(II)- and 2-oxoglutarate-dependent oxidative removal of methyl groups from histone H3, functioning in the nucleus to regulate gene expression epigenetically. Inferred from membership in the JARID1/KDM5 subfamily and domain architecture.

## Term and Decision Context

- Molecular function: histone demethylase activity (GO:0032452)
- Description: Putative histone demethylase that catalyzes Fe(II)- and 2-oxoglutarate-dependent oxidative removal of methyl groups from histone H3, functioning in the nucleus to regulate gene expression epigenetically. Inferred from membership in the JARID1/KDM5 subfamily and domain architecture.
- Directly involved in: epigenetic regulation of gene expression (GO:0040029)
- Locations: nucleus (GO:0005634)

## Reference Context

- file:WHEAT/A0A3B6RKV1/A0A3B6RKV1-deep-research-falcon.md

## Source Context YAML

```yaml
description: Putative histone demethylase that catalyzes Fe(II)- and 2-oxoglutarate-dependent oxidative
  removal of methyl groups from histone H3, functioning in the nucleus to regulate gene expression epigenetically.
  Inferred from membership in the JARID1/KDM5 subfamily and domain architecture.
supported_by:
- reference_id: file:WHEAT/A0A3B6RKV1/A0A3B6RKV1-deep-research-falcon.md
  supporting_text: LOC123148885 belongs to the KDM5/JARID1 subfamily of JmjC domain-containing histone
    demethylases, which specifically catalyze the removal of methyl groups from histone H3 lysine 4 marks
    (H3K4me1/2/3) via Fe(II)- and 2-oxoglutarate-dependent oxidative demethylation. The protein is predicted
    to localize to the nucleus, consistent with its chromatin-associated function.
molecular_function:
  id: GO:0032452
  label: histone demethylase activity
directly_involved_in:
- id: GO:0040029
  label: epigenetic regulation of gene expression
locations:
- id: GO:0005634
  label: nucleus
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

# Final Report: Core Function Hypothesis for Wheat A0A3B6RKV1 — Histone Demethylase Activity (GO:0032452)

## Executive Judgment

**Verdict: Over-annotated.** The seed hypothesis that A0A3B6RKV1 is a KDM5/JARID1-subfamily H3K4 lysine demethylase is incorrect in its subfamily assignment and substrate specificity. However, the broad GO term GO:0032452 (histone demethylase activity) is defensible by orthology to the experimentally characterized Arabidopsis JMJ22 (At5g06550), an H4R3me2 arginine demethylase. The correct specific annotation should be GO:0033749 (histone H4R3 demethylase activity), and all references to KDM5/JARID1 subfamily membership and H3K4 substrate specificity must be corrected to JMJD6 subfamily and H4R3me2 substrate.

**Key caveats:**
1. No direct experimental evidence exists for A0A3B6RKV1 itself; all functional inference is from orthology to AtJMJ22.
2. The JMJD6 family has debated dual activities (arginine demethylation vs. lysyl hydroxylation) in animals, though plant JMJ22 was experimentally shown to have arginine demethylase activity.
3. The UniProt "Similarity" field says "Belongs to the JARID1 histone demethylase family" — this likely propagated the misclassification, but it contradicts the more rigorous PANTHER and InterPro family-level classifications.

---

## Summary

The wheat protein A0A3B6RKV1 (UniProt accession A0A3B6RKV1, *Triticum aestivum*, chromosome 7A) was proposed to possess histone demethylase activity (GO:0032452) as a core function, with the rationale that it belongs to the KDM5/JARID1 subfamily and catalyzes Fe(II)- and 2-oxoglutarate-dependent removal of methyl groups from histone H3K4. This investigation found that the KDM5/JARID1 classification is erroneous. Multiple independent lines of evidence — domain architecture, phylogenetic classification (PANTHER, InterPro), NCBI orthology assignment, and sequence alignment — consistently place A0A3B6RKV1 in the **JMJD6 subfamily** of JmjC domain-containing proteins, orthologous to Arabidopsis JMJ22 (At5g06550).

JMJ22 has been experimentally demonstrated to function as a histone H4R3me2 arginine demethylase that promotes seed germination by removing repressive arginine methylation marks at GA biosynthesis loci ([PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/)). The protein's domain architecture — an F-box domain (residues 89–135) and a JmjC domain (residues 285–445) within a compact 511-amino-acid protein — is fundamentally incompatible with KDM5/JARID1 proteins, which require JmjN, ARID, PHD finger, and FYR domains and are typically 800–1200+ amino acids in plants.

AlphaFold structural prediction confirms high-confidence folding of the JmjC domain (pLDDT 95.8) with a perfectly conserved Fe(II)-binding facial triad (His330-Asp332-His362). The protein exists as a complete homeologous triad on wheat chromosomes 7A, 7B (A0A3B6SQ95), and 7D (A0A3B6TWS8), all 511 amino acids with 96–98% sequence identity, indicating strong purifying selection on this enzymatic function. The UniProt "Similarity" annotation stating "Belongs to the JARID1 histone demethylase family" appears to be an automated annotation error that propagated the incorrect subfamily assignment.

---

## Key Findings

### Finding 1: A0A3B6RKV1 Is Orthologous to AtJMJ22, an H4R3me2 Arginine Demethylase — Not a KDM5/JARID1 H3K4 Lysine Demethylase

The most critical finding of this investigation is that the seed hypothesis misidentifies the protein's subfamily. A0A3B6RKV1 (511 amino acids) possesses only an F-box domain (residues 89–135) and a JmjC domain (residues 285–445). True KDM5/JARID1 family proteins in plants are substantially larger (800–1200+ amino acids) and contain a characteristic multi-domain architecture: JmjN, ARID (AT-rich interaction domain), one or more PHD (plant homeodomain) fingers, JmjC, and FYR (FY-rich) domains. A0A3B6RKV1 lacks all of these signature domains except JmjC, which is shared across all JmjC-containing demethylase subfamilies.

NCBI Gene identifies the Arabidopsis ortholog of wheat LOC123148885 (encoding A0A3B6RKV1) as At5g06550, which corresponds to JMJ22. PANTHER classifies both proteins in family PTHR12480 (JMJD6 arginine demethylases/lysyl-hydroxylases), subfamily SF21. InterPro independently classifies both under IPR050910 (JMJD6 family arginine demethylases/lysyl-hydroxylases). JmjC domain identity between A0A3B6RKV1 and AtJMJ22 is approximately 77% at the full-length alignment level and ~88.5% in conserved blocks — far exceeding typical cross-subfamily identity.

Crucially, AtJMJ22 has been experimentally characterized as an H4R3me2 arginine demethylase, not an H3K4 lysine demethylase. Cho et al. (2012) demonstrated that JMJ20 and JMJ22 "act redundantly as positive regulators of seed germination" by removing "repressive histone arginine methylations at GA3ox1/GA3ox2," thereby increasing gibberellic acid levels and promoting germination under phytochrome B activation ([PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/)).

### Finding 2: Current GO Annotation Status — GO:0032452 Absent from A0A3B6RKV1, Present on AtJMJ22 but Without Specific H4R3 Term

QuickGO shows that A0A3B6RKV1 currently carries zero annotations for GO:0032452 (histone demethylase activity). The seed hypothesis therefore proposes a new annotation rather than evaluating an existing one. The Arabidopsis ortholog AtJMJ22 (Q67XX3) does carry GO:0032452 with IGI (Inferred from Genetic Interaction) evidence, based on [PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/) and assigned by TAIR, citing genetic interaction with AT5G63080.

Notably, even AtJMJ22 does not carry the more specific GO:0033749 (histone H4R3 demethylase activity), despite experimental evidence supporting H4R3me2 as its substrate. This represents an annotation gap in the reference organism. AtJMJ22 also does not carry GO:0032453 (histone H3K4 demethylase activity), which is consistent with the experimental evidence showing it is not an H3K4 demethylase.

### Finding 3: UniProt JARID1 Family Annotation Is an Automated Error Contradicted by PANTHER/InterPro

The UniProt "Similarity" field for A0A3B6RKV1 and its orthologs (including A0A453STL0 from *Oryza sativa*, A0A8R7R6R6 from *Zea mays*, and Q67XX3/AtJMJ22 from *Arabidopsis thaliana*) states: "Belongs to the JARID1 histone demethylase family." This annotation contradicts the PANTHER (PTHR12480, JMJD6 family) and InterPro (IPR050910, JMJD6 family) classifications. NCBI Gene describes the wheat locus LOC123148885 simply as "F-box protein At5g06550," avoiding the JARID1 subfamily claim. This discrepancy likely arose from automated annotation pipelines that classified any JmjC-containing protein with histone demethylase activity into the JARID1 family without checking domain architecture. True wheat KDM5/JARID1 proteins do exist as separate, much larger proteins (940+ amino acids) in distinct PANTHER subfamilies.

### Finding 4: AlphaFold Structure and Sequence Alignment Confirm Catalytic Competence and JMJD6 Orthology

AlphaFold predictions for A0A3B6RKV1 show an overall mean pLDDT of 84.5, with the JmjC domain achieving 95.8 and the F-box domain achieving 93.8 — both indicating high-confidence structural predictions. The Arabidopsis ortholog AtJMJ22 achieves a comparable JmjC pLDDT of 95.6.

Needleman-Wunsch alignment of the full proteins yields 62.3% identity (311/499 aligned positions), while the JmjC domain alone shows 77.0% identity (124/161 aligned positions). The Fe(II)-binding catalytic facial triad is perfectly conserved: A0A3B6RKV1 has His330-Val-Asp332...His362 with the flanking context SSFH**V**DPNS, while AtJMJ22 has His324-Ile-Asp326...His356 with context SSFH**I**DPNS. The conservative Val/Ile substitution at the non-catalytic position within this motif does not affect metal coordination. This conservation strongly supports maintained enzymatic activity in the wheat protein.

### Finding 5: Complete Homeologous Triad on Wheat Chromosomes 7A/7B/7D

A0A3B6RKV1 exists as part of a complete homeologous triad in hexaploid wheat (*Triticum aestivum*, AABBDD genome): the A-genome copy on chromosome 7A (A0A3B6RKV1), B-genome copy on 7B (A0A3B6SQ95), and D-genome copy on 7D (A0A3B6TWS8). All three homeologs are exactly 511 amino acids and share the identical domain architecture (F-box [89–135] + JmjC [285–445]) and PANTHER SF21 classification.

Pairwise sequence identity is extremely high: 7A–7B = 97.3%, 7A–7D = 96.9%, 7B–7D = 98.2%. Only 19 positions out of 511 are variable (96.3% overall conservation), with variations concentrated in the N-terminal disordered region (11.4% variable). Functional domains are highly conserved: F-box 2.1% variable, linker 2.9%, JmjC 1.8%, C-terminus 1.5%. The catalytic facial triad (His330, Asp332, His362) is perfectly conserved across all three homeologs. This extreme conservation across all three subgenomes indicates strong purifying selection, consistent with an essential, non-redundant enzymatic function.

| Accession | Chromosome | Length | PANTHER SF | Identity to 7A |
|-----------|-----------|--------|-----------|----------------|
| A0A3B6RKV1 | 7A | 511 aa | SF21 | — |
| A0A3B6SQ95 | 7B | 511 aa | SF21 | 97.3% |
| A0A3B6TWS8 | 7D | 511 aa | SF21 | 96.9% |

Wheat also possesses 6 longer JMJ21-like paralogs (808–946 amino acids) on chromosomes 2A/2B/2D and 5A/5B/5D in different PANTHER subfamilies (SF34, SF35), confirming that A0A3B6RKV1 is distinct from other JmjC family members in wheat and is specifically the JMJ22 ortholog.

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence & Limitations |
|---|----------|---------------|-----------|--------------|-------------|---------|--------------------------|
| 1 | [PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/) | Direct assay / mutant phenotype | **Qualifies** — supports H4R3me2 demethylase, refutes H3K4 demethylase | AtJMJ22 enzymatic activity | JMJ20/JMJ22 remove repressive histone arginine methylations at GA3ox1/GA3ox2 to promote seed germination | *A. thaliana*, seed germination, phyB signaling | **High** for JMJ22; moderate for orthology transfer to wheat |
| 2 | PANTHER PTHR12480:SF21 | Computational (phylogenetic) | **Refutes** KDM5; **supports** JMJD6 | Subfamily identity | A0A3B6RKV1 classified as JMJD6 family, SF21 | Cross-species classification | **High** — curated phylogenomic resource |
| 3 | InterPro IPR050910 | Computational (domain) | **Refutes** KDM5; **supports** JMJD6 | Family identity | JMJD6 family assignment | Automated domain analysis | **High** — independent of PANTHER |
| 4 | UniProt A0A3B6RKV1 | Database annotation | **Conflicts** (erroneous) | JARID1 family membership | UniProt Similarity field says "JARID1" | Automated annotation | **Low** — contradicted by PANTHER, InterPro, domain architecture |
| 5 | NCBI Gene LOC123148885 | Database (orthology) | **Supports** JMJ22 orthology | Gene identity | Ortholog identified as At5g06550 = JMJ22 | Cross-species orthology | **High** — NCBI curated orthology |
| 6 | QuickGO (A0A3B6RKV1) | Database | **Qualifies** | Current annotation status | A0A3B6RKV1 has 0 annotations for GO:0032452 | Current GO database state (June 2026) | **High** — verified |
| 7 | QuickGO (AtJMJ22) | Database | **Supports** GO:0032452 broadly | Histone demethylase annotation transferability | AtJMJ22 has GO:0032452 with IGI evidence; lacks specific GO:0033749 | *A. thaliana* experimental annotation | **High** for JMJ22; IBA transfer justified |
| 8 | AlphaFold AF-A0A3B6RKV1-F1 | Structural prediction | **Supports** catalytic competence | Protein is structurally competent | JmjC pLDDT 95.8; catalytic triad intact | AlphaFold prediction | **Medium** — prediction, not experimental |
| 9 | Sequence alignment | Computational (sequence) | **Supports** orthology | JmjC domain conservation | 77% identity to AtJMJ22 JmjC domain; catalytic triad context SSFH[VI]DPNS conserved | Global alignment | **High** — quantitative |
| 10 | Domain architecture | Computational (domain) | **Refutes** KDM5/JARID1 | Domain composition | F-box + JmjC only (511 aa); lacks JmjN, ARID, PHD, FYR | All KDM5/JARID1 require multi-domain architecture | **High** — definitive |
| 11 | Homeolog triad analysis | Computational (genomic) | **Supports** functional importance | Selective constraint | 7A/7B/7D copies 96–98% identical; catalytic triad invariant | *T. aestivum* hexaploid genome | **High** — genomic evidence |
| 12 | [PMID: 26059336](https://pubmed.ncbi.nlm.nih.gov/26059336/) | Computational (evolutionary) | **Supports** subfamily distinction | JMJD6 as distinct from KDM5 | 14 JmjC subfamilies defined; JMJD6 shared by plants, animals, fungi; KDM5 separate | Eukaryote-wide phylogenomics | **High** — comprehensive |
| 13 | [PMID: 26152513](https://pubmed.ncbi.nlm.nih.gov/26152513/) | Computational (evolutionary) | **Supports** JMJD6 classification | Group-V JMJD6 substrate associations | JMJD6 found in all plant species; associated with H3R2, H4R3 demethylation and H4 hydroxylation | Green lineage evolution | **High** — systematic |
| 14 | [PMID: 36092409](https://pubmed.ncbi.nlm.nih.gov/36092409/) | Computational / expression | **Supports** broadly | Wheat JmjC family context | Genome-wide identification of JmjC genes in wheat; subfamily classification including JMJD6 | *T. aestivum*, drought stress | **Medium** — genome-wide survey |
| 15 | [PMID: 20684070](https://pubmed.ncbi.nlm.nih.gov/20684070/) | Structural (crystallography) | **Qualifies** | JMJD6 enzymatic mechanism | Crystal structure shows JMJD6 catalyzes C-5 lysyl hydroxylation rather than Nε-demethylation | Animal JMJD6 | **Medium** — different organism context |
| 16 | [PMID: 22189873](https://pubmed.ncbi.nlm.nih.gov/22189873/) | Direct assay | **Qualifies** | JMJD6 substrate specificity | Animal Jmjd6 showed lysyl-hydroxylase but not arginine demethylase activity in vitro | Mouse/human JMJD6 | **Medium** — animal; may not apply to plants |
| 17 | [PMID: 24349476](https://pubmed.ncbi.nlm.nih.gov/24349476/) | Direct assay / mutant | **Supports** H4R3 biology | H4R3sme2 function in plants | SKB1/PRMT5-catalyzed H4R3sme2 regulates SAM maintenance via CRN repression | *A. thaliana*, shoot apical meristem | **High** — establishes H4R3me2 as active mark in plants |
| 18 | [PMID: 23943859](https://pubmed.ncbi.nlm.nih.gov/23943859/) | Direct assay / mutant | **Supports** H4R3 biology | H4R3sme2 function in plants | CAU1/PRMT5/SKB1 mediates H4R3sme2 to regulate CAS expression and stomatal closure | *A. thaliana*, stomata, drought | **High** — establishes H4R3me2 regulatory roles |

---

## GO Curation Implications

### Current Annotation State

- A0A3B6RKV1 does **not** currently carry GO:0032452 in QuickGO (as of June 2026).
- Existing annotations include: GO:0000987 (cis-regulatory region sequence-specific DNA binding, IBA), GO:0046872 (metal ion binding, IEA), GO:0005634 (nucleus, IBA/IEA).

### Recommended Curation Actions (Leads Requiring Curator Verification)

1. **GO:0033749 (histone H4R3 demethylase activity)**: **Recommended as the most specific and accurate MF term**, based on orthology to AtJMJ22 which demethylates H4R3me2 (PMID:22483719). Evidence code: ISS (Inferred from Sequence or Structural Similarity) with AtJMJ22 (Q67XX3) as the reference. This term is a child of GO:0032452.

2. **GO:0032452 (histone demethylase activity)**: **Supportable as IBA** from AtJMJ22 (Q67XX3), which carries this term with IGI evidence. May be retained as a broader parent-level annotation alongside GO:0033749.

3. **GO:0032453 (histone H3K4 demethylase activity)**: **Should NOT be annotated.** No evidence supports H3K4 lysine demethylation for this protein or its ortholog. The seed hypothesis's implied H3K4 specificity is refuted.

4. **GO:0040029 (epigenetic regulation of gene expression)**: **Supportable as IBA** from AtJMJ22 which has IDA evidence.

5. **GO:0005634 (nucleus)**: **Already annotated (IBA)**. Retain — consistent with chromatin-associated function.

6. **Subfamily designation**: Must be corrected from "KDM5/JARID1" to "JMJD6" throughout the review.

### GO Decision Table

| GO Term | Current Status | Proposed Action | Evidence Basis | Confidence |
|---------|---------------|-----------------|----------------|------------|
| GO:0032452 (histone demethylase activity) | Not annotated | Supportable (IBA) but prefer more specific term | AtJMJ22 orthology, IGI evidence | Medium |
| GO:0033749 (histone H4R3 demethylase activity) | Not annotated | **Recommended** as specific MF (ISS) | AtJMJ22 demethylates H4R3me2 (PMID:22483719) | Medium–High |
| GO:0032453 (histone H3K4 demethylase activity) | Not annotated | **Do NOT annotate** | KDM5 misclassification refuted | High confidence to exclude |
| GO:0040029 (epigenetic regulation of gene expression) | Not annotated | Supportable (IBA) | AtJMJ22 has IDA | Medium |
| GO:0005634 (nucleus) | Annotated (IBA) | **Retain** | Consistent evidence | High |
| GO:0009845 (seed germination) | Not annotated | Consider adding (IBA) with caution | AtJMJ22 demonstrated; conservation in wheat unknown | Low–Medium |

**Note:** Even the reference organism AtJMJ22 lacks GO:0033749, despite experimental evidence. This is an upstream annotation gap that should be flagged to TAIR curators.

---

## Mechanistic Model / Interpretation

### Direct Gene-Product Activity (Inferred from Orthology)

The immediate molecular function of A0A3B6RKV1, inferred from orthology to AtJMJ22, is the **Fe(II)- and 2-oxoglutarate-dependent oxidative removal of methyl groups from histone H4 arginine 3 (H4R3me2)**. This is an arginine demethylation reaction, mechanistically distinct from the lysine demethylation performed by KDM5/JARID1 enzymes, although both reaction types use the same JmjC catalytic mechanism (2-oxoglutarate-dependent dioxygenase chemistry).

The protein's F-box domain (residues 89–135) suggests possible integration with SCF ubiquitin ligase complexes, which could provide an additional regulatory layer or facilitate substrate targeting. This F-box + JmjC combination is distinctive and not found in KDM5/JARID1 proteins.

```
Mechanistic Model (inferred from AtJMJ22 orthology):

  Environmental Signal (e.g., light/phyB activation)
           │
           ▼
  ┌─────────────────────────────┐
  │  Derepression of JMJ22      │  (SOMNUS represses JMJ22 when phyB inactive)
  │  (= A0A3B6RKV1 in wheat)    │
  └─────────────────────────────┘
           │
           ▼
  ┌─────────────────────────────┐
  │  H4R3me2 demethylation at   │  ← Direct enzymatic activity
  │  target gene loci            │     (Fe²⁺ + 2-OG dependent)
  │  (e.g., GA3ox1/GA3ox2)      │
  └─────────────────────────────┘
           │
           ▼
  ┌─────────────────────────────┐
  │  Transcriptional activation  │  ← Downstream consequence
  │  of target genes             │
  └─────────────────────────────┘
           │
           ▼
  ┌─────────────────────────────┐
  │  Increased GA levels →       │  ← Phenotypic outcome
  │  Seed germination            │
  └─────────────────────────────┘
```

### Downstream vs. Direct Effects

The seed hypothesis mentions "regulate gene expression epigenetically" (GO:0040029). This is a downstream consequence of the direct enzymatic activity (histone demethylation), not the primary molecular function itself. While appropriate as a BP annotation, it should not be conflated with the MF annotation. Similarly, seed germination is a developmental outcome, not a molecular function.

### H4R3sme2 as an Active Epigenetic Mark in Plants

The H4R3sme2 mark that JMJ22-type proteins remove is deposited by PRMT5/SKB1 ([PMID: 24349476](https://pubmed.ncbi.nlm.nih.gov/24349476/); [PMID: 23943859](https://pubmed.ncbi.nlm.nih.gov/23943859/)). In Arabidopsis, PRMT5-mediated H4R3sme2 is a repressive mark involved in:
- Shoot apical meristem maintenance via CRN repression ([PMID: 24349476](https://pubmed.ncbi.nlm.nih.gov/24349476/))
- Stomatal closure via CAS regulation ([PMID: 23943859](https://pubmed.ncbi.nlm.nih.gov/23943859/))
- Seed germination control via GA3ox1/GA3ox2 ([PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/))

This establishes H4R3sme2 as a biologically significant regulatory mark in plants, supporting the relevance of JMJ22-type demethylases as functional epigenetic regulators.

### Caveat: JMJD6 Bifunctionality

In animals, JMJD6 has been shown to possess dual activity — both arginine demethylase and lysyl-hydroxylase functions ([PMID: 20684070](https://pubmed.ncbi.nlm.nih.gov/20684070/); [PMID: 28587176](https://pubmed.ncbi.nlm.nih.gov/28587176/)). One study found that animal Jmjd6 showed lysyl-hydroxylase but not arginine demethylase activity in vitro ([PMID: 22189873](https://pubmed.ncbi.nlm.nih.gov/22189873/)). However, the plant ortholog AtJMJ22 has been experimentally demonstrated to function as an arginine demethylase in vivo, and plant JMJD6 subfamily members classified in Group-V are associated with H3R2, H4R3 demethylation and H4 hydroxylation ([PMID: 26152513](https://pubmed.ncbi.nlm.nih.gov/26152513/)). Whether A0A3B6RKV1 also possesses lysyl-hydroxylase activity remains an open question.

---

## Evidence Base

### Primary Experimental Evidence (Ortholog)

**Cho et al. (2012)** — *"Control of seed germination by light-induced histone arginine demethylation activity"* ([PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/))

This is the single most important paper for this hypothesis. The authors demonstrated that Arabidopsis JMJ20 and JMJ22 "act redundantly as positive regulators of seed germination. When PHYB is inactive, JMJ20/JMJ22 are directly repressed by the zinc-finger protein SOMNUS. However, upon PHYB activation, JMJ20/JMJ22 are derepressed, resulting in increased gibberellic acid levels through the removal of repressive histone arginine methylations at GA3ox1/GA3ox2, which in turn promotes seed germination." This establishes JMJ22 as an H4R3me2 arginine demethylase with a defined biological role, and since A0A3B6RKV1 is the wheat ortholog of JMJ22 (NCBI Gene orthology, 77% JmjC identity), this evidence directly informs the expected function of A0A3B6RKV1.

### Evolutionary and Phylogenomic Context

**Lei and Liu (2015)** — *"Expansion and Functional Divergence of Jumonji C-Containing Histone Demethylases"* ([PMID: 26059336](https://pubmed.ncbi.nlm.nih.gov/26059336/))

Defined 14 JmjC subfamilies across eukaryotes, including JMJD6 as a subfamily shared by plants, animals, and fungi — phylogenetically distinct from KDM5. This confirms the independent evolutionary origin and functional divergence of these two groups.

**Chen et al. (2015)** — *"Evolution and conservation of JmjC domain proteins in the green lineage"* ([PMID: 26152513](https://pubmed.ncbi.nlm.nih.gov/26152513/))

Classified plant JmjC proteins into seven groups. Group-V (JMJD6) was "found in all the plant species" and associated with "H3R2, H4R3, and hydroxylation of H4." This directly supports the classification of A0A3B6RKV1 as a JMJD6 family member with predicted H4R3 demethylase activity.

### H4R3 Methylation Biology in Plants

**Wang et al. (2014)** — *"Histone H4R3 methylation catalyzed by SKB1/PRMT5 is required for maintaining shoot apical meristem"* ([PMID: 24349476](https://pubmed.ncbi.nlm.nih.gov/24349476/))

Established that SKB1/PRMT5-catalyzed H4R3sme2 is a functional epigenetic mark in Arabidopsis, repressing CRN expression to maintain SAM geometry. This confirms that H4R3me2 is a biologically active mark in plants, providing substrate context for JMJ22-type demethylases.

**Liang et al. (2013)** — *"Arabidopsis histone methylase CAU1/PRMT5/SKB1 acts as an epigenetic suppressor of the calcium signaling gene CAS"* ([PMID: 23943859](https://pubmed.ncbi.nlm.nih.gov/23943859/))

Further demonstrated H4R3sme2 function in plant stomatal closure and drought tolerance, reinforcing the biological significance of H4R3 methylation as a regulatory mechanism in plants and the importance of demethylases that counteract this mark.

### Wheat JmjC Family Context

**Min et al. (2022)** — *"Genome-wide identification of the jumonji C domain-containing histone demethylase gene family in wheat"* ([PMID: 36092409](https://pubmed.ncbi.nlm.nih.gov/36092409/))

Identified the complete JmjC gene family in wheat, including JMJD6 subfamily members, and analyzed their expression under drought stress. Provides the genomic context for A0A3B6RKV1 within the wheat JmjC family.

### Animal JMJD6 — Caution for Cross-Kingdom Extrapolation

**Mantri et al. (2010)** — *"Crystal structure of the 2-oxoglutarate- and Fe(II)-dependent lysyl hydroxylase JMJD6"* ([PMID: 20684070](https://pubmed.ncbi.nlm.nih.gov/20684070/))

Showed that animal JMJD6 "catalyses the iron- and 2-oxoglutarate-dependent hydroxylation of lysyl residues in arginine-serine-rich domains of RNA splicing-related proteins" and explained structurally "how JMJD6 binds its lysyl residues such that it can catalyse C-5 hydroxylation rather than Nepsilon-demethylation." This raises the possibility that plant JMJD6 orthologs might also have hydroxylase activity, though the in vivo data for AtJMJ22 clearly demonstrates arginine demethylase activity.

**Han et al. (2012)** — *"The hydroxylation activity of Jmjd6 is required for its homo-oligomerization"* ([PMID: 22189873](https://pubmed.ncbi.nlm.nih.gov/22189873/))

Reported that animal Jmjd6 "is unable to remove the methyl group from histone arginine residues but can hydroxylate the histone H4 tail at lysine residues in a 2-oxoglutarate (2-OG)- and Fe(II)-dependent manner." This creates uncertainty about the JMJD6 family's primary activity, but the plant-specific experimental evidence ([PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/)) demonstrates arginine demethylation for AtJMJ22.

---

## Conflicts and Alternatives

### 1. UniProt vs. PANTHER/InterPro Classification Conflict

The most significant conflict is between the UniProt "Similarity" annotation (JARID1 family) and the PANTHER/InterPro classification (JMJD6 family). The evidence overwhelmingly supports the PANTHER/InterPro assignment:
- Domain architecture is incompatible with KDM5/JARID1
- NCBI orthology points to JMJ22, a known JMJD6 subfamily member
- Sequence identity to AtJMJ22 is high (77% JmjC domain)
- True KDM5/JARID1 proteins exist separately in wheat at much larger sizes

**Resolution:** The UniProt annotation is likely an automated error. Notably, UniProt names AtJMJ22 as "Arginine-specific demethylase JMJ22" while simultaneously stating it "Belongs to the JARID1 histone demethylase family" — these are internally inconsistent within UniProt itself.

### 2. Arginine Demethylase vs. Lysyl Hydroxylase Activity

Animal JMJD6 has been shown to have lysyl-hydroxylase activity rather than (or in addition to) arginine demethylase activity in some assays ([PMID: 22189873](https://pubmed.ncbi.nlm.nih.gov/22189873/)). This raises the question of whether plant orthologs like A0A3B6RKV1 might primarily function as hydroxylases rather than demethylases. However, the in vivo evidence from Cho et al. ([PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/)) clearly demonstrates arginine demethylation activity for AtJMJ22. The animal results may reflect kingdom-specific functional divergence within the JMJD6 subfamily, or methodological differences between in vitro and in vivo assays.

### 3. Paralog Confusion Risk

A0A3B6RKV1 should not be confused with other JmjC proteins in wheat. The wheat genome contains at least 6 JMJ21-like paralogs (808–946 amino acids, chromosomes 2/5) that belong to different PANTHER subfamilies (SF34, SF35). These are larger proteins with distinct domain architectures and likely different substrate specificities. The JMJ22 orthologs are uniquely compact (511 aa) with the F-box + JmjC architecture on chromosome group 7.

### 4. Domain Architecture and Substrate Specificity

Wang et al. (2020) demonstrated that in Arabidopsis JMJ16 (a true KDM5 protein), the FYR domain restricts JmjC substrate specificity to H3K4 in somatic cells ([PMID: 32572214](https://pubmed.ncbi.nlm.nih.gov/32572214/)). A0A3B6RKV1 completely lacks FYR, JmjN, ARID, and PHD domains. This is NOT consistent with being a KDM5 protein with "deregulated" specificity — it is a fundamentally different protein architecture (JMJD6 subfamily) with inherently different substrate recognition. The F-box domain present in A0A3B6RKV1 is never found in KDM5/JARID1 proteins but is characteristic of the plant JMJD6 subfamily.

### 5. F-box Domain: Potential Additional Function

The presence of an F-box domain is notable and could indicate involvement in ubiquitin-mediated protein degradation pathways. This is not a feature of canonical animal JMJD6 proteins and may represent a plant-specific functional adaptation. Whether the F-box domain contributes to the protein's core function (e.g., by targeting substrates for ubiquitination after demethylation) or serves as a structural scaffold is unknown.

---

## Knowledge Gaps

| Gap | What Was Checked | Why It Matters | What Would Resolve It |
|-----|-----------------|----------------|----------------------|
| No direct biochemical assay on A0A3B6RKV1 | Literature search for wheat JMJ22 enzymology | Function inferred by orthology only; substrate specificity could differ from AtJMJ22 | In vitro demethylase/hydroxylase assay with recombinant A0A3B6RKV1 |
| Substrate specificity not experimentally verified | AtJMJ22 shows H4R3me2; animal JMJD6 shows lysyl hydroxylation | Could have different or additional substrates in wheat | Histone peptide array or mass spectrometry-based substrate profiling |
| No expression data for A0A3B6RKV1 specifically | Genome-wide wheat JmjC studies exist but gene-level expression for this locus not extracted | Expression pattern would confirm whether this gene is active and in which tissues/conditions | RNA-seq or qRT-PCR across wheat developmental stages for LOC123148885 |
| Functional redundancy with JMJ21-like paralogs unknown | Identified 6 JMJ21 paralogs on chr 2/5 in different subfamilies | If JMJ21 and JMJ22 act redundantly (as JMJ20/JMJ22 do in Arabidopsis), single-gene annotation may overstate essentiality | Genetic interaction studies; double/triple mutant analysis in wheat |
| F-box domain function uncharacterized | Domain architecture noted; no functional studies found | Could indicate SCF complex involvement or substrate targeting | Mutagenesis of F-box domain; co-IP/pull-down for SCF complex partners |
| AtJMJ22 lacks specific GO:0033749 annotation | QuickGO checked for Q67XX3 | Upstream annotation gap prevents straightforward ISS transfer of the specific term | TAIR curation update for AtJMJ22 |
| Possible lysyl-hydroxylase activity not tested | Animal JMJD6 literature reviewed | Bifunctionality could change the annotation | Hydroxylation assays on histone H4 peptides |

---

## Discriminating Tests

### High-Priority Experiments

1. **In vitro demethylase assay with recombinant A0A3B6RKV1:** Express and purify the wheat protein; test activity against methylated histone peptides (H4R3me2s, H4R3me2a, H3K4me1/2/3) using MALDI-TOF mass spectrometry or antibody-based detection. This would definitively establish substrate specificity.

2. **In vitro lysyl-hydroxylase assay:** Test A0A3B6RKV1 against lysine-containing peptide substrates (histone H4 tail, RS-domain peptides) to determine whether the protein has hydroxylase activity in addition to or instead of demethylase activity.

3. **ChIP-qPCR in wheat:** Perform chromatin immunoprecipitation with anti-H4R3me2 antibodies in wild-type vs. A0A3B6RKV1 knockdown/knockout wheat lines at target loci (wheat GA3ox orthologs, if the germination pathway is conserved).

### Medium-Priority Computational Analyses

4. **Molecular docking of H4R3me2 vs. H3K4me3 into AlphaFold structure:** Use the high-confidence JmjC domain structure to model substrate binding. Compare with crystallized JMJD6 (PDB: 3K2O, [PMID: 20684070](https://pubmed.ncbi.nlm.nih.gov/20684070/)) and KDM5A structures to predict substrate preference.

5. **Co-expression network analysis in wheat:** Use publicly available wheat RNA-seq data (e.g., WheatExp, expVIP) to identify genes co-expressed with LOC123148885. If co-expressed genes are enriched for GA biosynthesis or seed germination pathways, this would support functional conservation from Arabidopsis.

6. **Comprehensive phylogenetic analysis:** Build a phylogenetic tree including all plant JMJD6 subfamily members to confirm A0A3B6RKV1's placement and identify the closest paralogs/orthologs with more statistical rigor.

### Validation Experiments

7. **Complementation test:** Express A0A3B6RKV1 in Arabidopsis *jmj20 jmj22* double mutant to test whether the wheat protein can rescue the seed germination phenotype — would directly demonstrate functional conservation.

8. **Homeolog-specific wheat knockouts:** Generate CRISPR knockouts of individual or combined 7A/7B/7D homeologs to assess functional redundancy and phenotypic consequences.

---

## Curation Leads

### Lead 1: Correct Subfamily Assignment (Critical Priority)

**Action:** Change subfamily classification from KDM5/JARID1 to JMJD6 in all relevant records.
- **Evidence:** PANTHER PTHR12480:SF21, InterPro IPR050910, domain architecture (F-box + JmjC, 511 aa, no JmjN/ARID/PHD/FYR), NCBI orthology to JMJ22
- **Affected annotations:** UniProt "Similarity" field for A0A3B6RKV1, A0A3B6SQ95, A0A3B6TWS8, and cross-species orthologs
- **Status:** Lead requiring curator verification with UniProt

### Lead 2: Add Specific MF Annotation GO:0033749 (High Priority)

**Action:** Annotate A0A3B6RKV1 with GO:0033749 (histone H4R3 demethylase activity) using evidence code ISS, with AtJMJ22 (Q67XX3) as the reference protein and [PMID: 22483719](https://pubmed.ncbi.nlm.nih.gov/22483719/) as the supporting publication.
- **Snippet to verify (from PMID:22483719 abstract):** "the histone arginine demethylases, JMJ20 and JMJ22, act redundantly as positive regulators of seed germination... resulting in increased gibberellic acid levels through the removal of repressive histone arginine methylations at GA3ox1/GA3ox2"
- **Note:** This is more specific and accurate than GO:0032452 alone.

### Lead 3: Remove/Correct H3K4 Substrate References (Critical Priority)

**Action:** Remove all references to H3K4 demethylase activity and KDM5/JARID1 membership from the gene review.
- **Rationale:** Domain architecture definitively excludes KDM5/JARID1 membership; the ortholog AtJMJ22 does not have H3K4 demethylase activity.

### Lead 4: Retain GO:0032452 as Broader MF Term (Medium Priority)

**Action:** GO:0032452 (histone demethylase activity) may be retained as a parent term annotation, consistent with AtJMJ22's existing annotation in TAIR. However, it should not be the sole or most specific annotation if GO:0033749 is applied.

### Lead 5: Flag Upstream AtJMJ22 Annotation Gap (Low Priority)

**Action:** Note that AtJMJ22 (Q67XX3) in TAIR/QuickGO lacks GO:0033749 despite experimental evidence for H4R3me2 demethylation. Suggest TAIR curators consider adding this specific term to the reference organism annotation.

### Lead 6: Annotate All Three Homeologs Consistently (Medium Priority)

**Action:** Apply the same corrected annotations to all three homeologs: A0A3B6RKV1 (7A), A0A3B6SQ95 (7B), A0A3B6TWS8 (7D). Their 96–98% identity and perfectly conserved catalytic residues justify identical functional annotation.

### Lead 7: Correct Seed Hypothesis Description (High Priority)

**Current description:** "Putative histone demethylase that catalyzes Fe(II)- and 2-oxoglutarate-dependent oxidative removal of methyl groups from histone H3, functioning in the nucleus to regulate gene expression epigenetically. Inferred from membership in the JARID1/KDM5 subfamily and domain architecture."

**Recommended correction:** "Putative histone arginine demethylase that catalyzes Fe(II)- and 2-oxoglutarate-dependent oxidative removal of methyl groups from histone H4 arginine 3 (H4R3me2), functioning in the nucleus to regulate gene expression epigenetically. Inferred from orthology to Arabidopsis JMJ22 (At5g06550) in the JMJD6 subfamily and conserved JmjC domain architecture."


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)