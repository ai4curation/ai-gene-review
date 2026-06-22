# Citations for Research Query

**Query:** # Literature evidence for LGALS3 (Homo sapiens): LGALS3 has monocyte chemotaxis (GO:0002548).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has monocyte chemotaxis (GO:0002548).
Key context:
- Term: monocyte chemotaxis (GO:0002548)
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
- **Hypothesis slug:** function-support-go-0002548
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[7]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0002548
  label: monocyte chemotaxis
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
**Generated:** 2026-06-22T04:46:30.860784

1. Yinghui Ren, Yongmei Qian, Qicheng Zhang, Xiaoping Li, Mingjiang Li et al. (2024). High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma. Cancer Cell International. https://www.semanticscholar.org/paper/552bd37c67dea75d0c33a9a0de2acdafcf0dcf6e
2. C. Contini, B. Manconi, A. Olianas, Giulia Guadalupi, Alessandra Schirru et al. (2024). Combined High—Throughput Proteomics and Random Forest Machine-Learning Approach Differentiates and Classifies Metabolic, Immune, Signaling and ECM Intra-Tumor Heterogeneity of Colorectal Cancer. Cells. https://www.semanticscholar.org/paper/b7d8516d42c8108cbdf59e6865a8fb424c450946
3. Runji Chen, D. McVey, D. Shen, Xiaoxin Huang, Shu Ye (2023). Phenotypic Switching of Vascular Smooth Muscle Cells in Atherosclerosis. Journal of the American Heart Association: Cardiovascular and Cerebrovascular Disease. https://www.semanticscholar.org/paper/472c313e2214a97757712ab0a8b39b133bd6a6bc
4. Yaoru Song, S.-W. Pan, Jiahe Tian, Yingying Yu, Siyu Wang et al. (2024). Activation of CD14+ Monocytes via the IFN-γ Signaling Pathway Is Associated with Immune-Related Adverse Events in Hepatocellular Carcinoma Patients Receiving PD-1 Inhibition Combination Therapy. Biomedicines. https://www.semanticscholar.org/paper/b05a3ac750e4ab33f0d31bc2708c804f3502f743
5. Philip K Farahat, Chino Kumagai-Cresse, Raquel L. Aragón, Feiyang Ma, Justin K. Amakor et al. (2025). Macrophage-derived Spp1 promotes intramuscular fat in dystrophic muscle. JCI Insight. https://www.semanticscholar.org/paper/25c265aed44730ce4b23491cd7ac24d8c3fcf94b
6. E. Ragni, C. Perucca Orfei, L. de Girolamo (2022). Secreted Factors and Extracellular Vesicles Account for the Immunomodulatory and Tissue Regenerative Properties of Bone-Marrow-Derived Mesenchymal Stromal Cells for Osteoarthritis. Cells. https://www.semanticscholar.org/paper/b4611c0ee0053b5bd745e5c412143451f2f14a97
7. S. Blois, G. Dveksler, G. Vasta, N. Freitag, V. Blanchard et al. (2019). Pregnancy Galectinology: Insights Into a Complex Network of Glycan Binding Proteins. Frontiers in Immunology. https://www.semanticscholar.org/paper/68fad2b87411701fa708a1f49f8b918370486857
8. Kui Wang, Shuyue Fu, Lixia Dong, Dingyue Zhang, Mao Wang et al. (2023). Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy. Autophagy. https://www.semanticscholar.org/paper/3dadfc351823c4e325e65c171ab3765871189c80
9. Wan-Ming Hu, Yuan-Zhong Yang, Tian Zhang, Changling Qin, Xuenong Li (2020). LGALS3 Is a Poor Prognostic Factor in Diffusely Infiltrating Gliomas and Is Closely Correlated With CD163+ Tumor-Associated Macrophages. Frontiers in Medicine. https://www.semanticscholar.org/paper/53b083f91a08aefebb5f9edaaa95625e2dc98f2b
10. P. Rusmini, F. Mina, M. Valenza, Martina Vitali, V. Ferrari et al. (2025). Impairment of lysosomal quality control in Huntington disease. Cell Death & Disease. https://www.semanticscholar.org/paper/c874bbb3c9e6aa0a3f74519c022f3fa822daf4a8
11. G. Ávila, M. Bonnet, D. Viala, S. Déjean, G. Grilli et al. (2024). Citrus pectin modulates chicken peripheral blood mononuclear cell proteome in vitro. Poultry Science. https://www.semanticscholar.org/paper/6755550163f80e4863389b3402bd6ac0b5ac8aa0
12. Kevin A. Maupin, Daniel T. Dick, Vari Vivarium, Transgenics Core, B. Williams (2020). Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice. FEBS Open Bio. https://www.semanticscholar.org/paper/6ab62ea9acc6fef617d0b1f237c1a477f45b05c7