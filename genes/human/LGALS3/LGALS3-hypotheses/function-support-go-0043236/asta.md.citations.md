# Citations for Research Query

**Query:** # Literature evidence for LGALS3 (Homo sapiens): LGALS3 has laminin binding (GO:0043236).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has laminin binding (GO:0043236).
Key context:
- Term: laminin binding (GO:0043236)
- Existing evidence type: IBA
- Original reference: GO_REF:0000033

Retrieve primary experimental papers that directly test this claim for
LGALS3 (or a well-supported ortholog): assays, mutant phenotypes,
localisation, interactions, or structures.

<!--
The lines above are deliberately first so length-limited retrieval providers
(e.g. asta, which truncates the query to ~500 characters) search on the gene
and its biology rather than on the curation boilerplate below.
-->

## How to use this prompt

You are searching for **independent literature support for the single
gene-function hypothesis stated above**. The hypothesis is a plain claim that a
gene product has a particular molecular function, biological role, or cellular
location. Find primary (or well-justified orthologous) evidence that **confirms
or refutes** that claim for this specific gene.

This is a recall-oriented search: surface every plausible piece of supporting
evidence, but make each candidate **independently checkable** so a downstream
curator or agent can filter false positives. This is not a general gene
overview, and any prior curation decision shown in the context is intentionally
neutralised — judge the hypothesis on the external evidence, not on the existing
annotation.

A common use of this template is confirming annotations that currently rest only
on phylogenetic inference (evidence code IBA, propagated from PANTHER
`GO_REF:0000033`), but it applies to any gene-function hypothesis.

## Focus

- **Focus type:** function_support
- **Hypothesis slug:** function-support-go-0043236
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[10]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0043236
  label: laminin binding
evidence_type: IBA
original_reference_id: GO_REF:0000033
```

## Research Objective

Find the strongest available **independent** evidence bearing on whether the
hypothesis is true for LGALS3. Prioritise, in order:

1. Direct experimental evidence in LGALS3 itself (the named gene in the
   named organism): assays, mutant phenotypes, localisation, interactions,
   structures.
2. Direct experimental evidence in a clearly orthologous gene, where the
   orthology is well established and the function is expected to be conserved.
3. Strong indirect or computational evidence (domain architecture, conserved
   motifs, structural homology, operon/pathway context), reported
   conservatively.

Prefer **PMID** citations; include **DOI** citations when no PMID is available.
Treat reviews and database records as orientation only — cite the underlying
primary papers wherever possible.

**Expect false positives.** This pipeline is tuned for recall, so a downstream
curator/agent will sift your results. For every candidate you must therefore
provide an **exact verbatim snippet** from the source that can be checked, plus
enough context (organism, assay, gene actually studied) to detect paralog
confusion, wrong-organism carry-over, or claims that are really about a
different gene.

## Required Output

### Executive Judgment

State whether independent support exists: **supported** (with strong primary
evidence), **partially / indirectly supported**, **unresolved** (no independent
evidence found), or **refuted**. One short paragraph; lead with the verdict.

### Evidence Matrix

A table with one row per candidate evidence item:

- Citation (PMID preferred; DOI otherwise)
- Gene/protein actually studied (and organism) — flag if it is an ortholog or a paralog
- Evidence type (direct assay, mutant phenotype, localization, interaction, structural/evolutionary, computational, review/database)
- Supports / refutes / qualifies
- Exact verbatim snippet to verify (quote the source)
- Key finding in your own words
- Confidence and the most important caveat (false-positive risk)

### Best Supporting References

List the 1–3 references most suitable to add to the review's `supported_by`
for this hypothesis, each with the exact snippet a curator should confirm. If
none qualify, say so explicitly.

### Conflicts and Alternatives

Note any evidence that contradicts the hypothesis or that points to paralog
confusion, organism-specific differences, isoform-specific findings, or
database carry-over.

### Knowledge Gaps

If no adequate independent evidence exists, state what was searched, why the gap
matters, and what evidence or experiment would resolve it.

**Provider:** asta
**Generated:** 2026-06-22T04:46:53.636967

1. Kui Wang, Shuyue Fu, Lixia Dong, Dingyue Zhang, Mao Wang et al. (2023). Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy. Autophagy. https://www.semanticscholar.org/paper/3dadfc351823c4e325e65c171ab3765871189c80
2. M. Guittaut, Stéphane Charpentier, Thierry Normand, Martine Dubois, J. Raimond et al. (2001). Identification of an Internal Gene to the Human Galectin-3 Gene with Two Different Overlapping Reading Frames That Do Not Encode Galectin-3*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/75ca62f4b6eb66b3bcdac062664da410941fdcaa
3. Kevin A. Maupin, Daniel T. Dick, Vari Vivarium, Transgenics Core, B. Williams (2020). Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice. FEBS Open Bio. https://www.semanticscholar.org/paper/6ab62ea9acc6fef617d0b1f237c1a477f45b05c7
4. P. Nde, M. Lima, Candice A. Johnson, S. Pratap, F. Villalta (2012). Regulation and use of the extracellular matrix by Trypanosoma cruzi during early infection. Frontiers in Immunology. https://www.semanticscholar.org/paper/0f8537bce448a98bc55bef38dcc8d4b462ab72b5
5. Saleh M. Ramezani, Arianna Parkhideh, P. Bhattacharya, M. Farach-Carson, D. Harrington (2021). Beyond Colonoscopy: Exploring New Cell Surface Biomarkers for Detection of Early, Heterogenous Colorectal Lesions. Frontiers in Oncology. https://www.semanticscholar.org/paper/4b48091d0ad86a2121491218707db23e88605000
6. P. Ruvolo, Chenyue W. Hu, Y. Qiu, V. Ruvolo, Robin L. Go et al. (2019). LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML. EBioMedicine. https://www.semanticscholar.org/paper/46bbdbcb4660389e13acba24499cc415d75f18e0
7. Aditi Bauskar, W. Mack, J. Mauris, P. Argüeso, M. Heur et al. (2015). Clusterin Seals the Ocular Surface Barrier in Mouse Dry Eye. PLoS ONE. https://www.semanticscholar.org/paper/ddc53237e6b4b7c325cb047e4eaf34098273148e
8. Mi Guan, Yanping Ma, S. Shah, G. Romano (2016). Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy. Oncolytic Virotherapy. https://www.semanticscholar.org/paper/9f79d851e32ad25e83c0a2d64e12919bf81a89f8
9. Yinghui Ren, Yongmei Qian, Qicheng Zhang, Xiaoping Li, Mingjiang Li et al. (2024). High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma. Cancer Cell International. https://www.semanticscholar.org/paper/552bd37c67dea75d0c33a9a0de2acdafcf0dcf6e
10. Qin Xia, Hanfei Zheng, Yang Li, Wanting Xu, Chengwei Wu et al. (2023). SMURF1 controls the PPP3/calcineurin complex and TFEB at a regulatory node for lysosomal biogenesis. Autophagy. https://www.semanticscholar.org/paper/7ab13fe72fa12a55aa9304ce52199d1494c8974a
11. Alexander J. Knights, Jinfen. J. Yik, Hanapi Mat Jusoh, Laura J. Norton, Alister P. W. Funnell et al. (2016). Krüppel-like Factor 3 (KLF3/BKLF) Is Required for Widespread Repression of the Inflammatory Modulator Galectin-3 (Lgals3)*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/dce84b7faec66ad9234b04f596d036ed32078971
12. A. Montero‐Calle, Á. López-Janeiro, Marta L. Mendes, Daniel Perez-Hernandez, Irene Echevarría et al. (2023). In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression. Cellular Oncology. https://www.semanticscholar.org/paper/92b64e01bcb30f7457ddb8cc4be26de8b0c7cf69
13. Abbass Jaber, Laura Palmieri, R. Bakour, N. Bourg, A. Hong et al. (2025). Lysosomal damage is a therapeutic target in Duchenne muscular dystrophy. Science Advances. https://www.semanticscholar.org/paper/3265a29ad8c2d48b294017fd50b6df9188b55ecb