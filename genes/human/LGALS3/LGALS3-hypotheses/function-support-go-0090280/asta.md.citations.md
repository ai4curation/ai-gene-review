# Citations for Research Query

**Query:** # Literature evidence for LGALS3 (Homo sapiens): LGALS3 has positive regulation of calcium ion import (GO:0090280).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has positive regulation of calcium ion import (GO:0090280).
Key context:
- Term: positive regulation of calcium ion import (GO:0090280)
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
- **Hypothesis slug:** function-support-go-0090280
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[14]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0090280
  label: positive regulation of calcium ion import
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
**Generated:** 2026-06-22T04:47:23.748620

1. M. Guittaut, Stéphane Charpentier, Thierry Normand, Martine Dubois, J. Raimond et al. (2001). Identification of an Internal Gene to the Human Galectin-3 Gene with Two Different Overlapping Reading Frames That Do Not Encode Galectin-3*. The Journal of Biological Chemistry. https://www.semanticscholar.org/paper/75ca62f4b6eb66b3bcdac062664da410941fdcaa
2. P. Ruvolo, Chenyue W. Hu, Y. Qiu, V. Ruvolo, Robin L. Go et al. (2019). LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML. EBioMedicine. https://www.semanticscholar.org/paper/46bbdbcb4660389e13acba24499cc415d75f18e0
3. Youfen Yu, Xueru Xu, Chunshui Lin, Rongguo Liu (2023). Systematic identification of potential key microRNAs and circRNAs in the dorsal root ganglia of mice with sciatic nerve injury. Frontiers in Molecular Neuroscience. https://www.semanticscholar.org/paper/bb63dc0bb6c65149c674451492fc049ff2f4ce8f
4. Zhepeng Wang, Guohua Meng, Yun Bai, Ruifang Liu, Yu Du et al. (2017). Comparative transcriptome analysis provides clues to molecular mechanisms underlying blue-green eggshell color in the Jinding duck (Anas platyrhynchos). BMC Genomics. https://www.semanticscholar.org/paper/9d37ba3b57ef695a83d1039fe094ded0df9f4b38
5. Zehua Ye, Yushi Sun, Songyuan Yang, Lei Li, Bojun Li et al. (2025). Lgals3 Promotes Calcium Oxalate Crystal Formation and Kidney Injury Through Histone Lactylation‐Mediated FGFR4 Activation. Advanced Science. https://www.semanticscholar.org/paper/adbfa30b5832407d200a5eade9196d41be08050e
6. Kui Wang, Shuyue Fu, Lixia Dong, Dingyue Zhang, Mao Wang et al. (2023). Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy. Autophagy. https://www.semanticscholar.org/paper/3dadfc351823c4e325e65c171ab3765871189c80
7. Abbass Jaber, Laura Palmieri, R. Bakour, N. Bourg, A. Hong et al. (2025). Lysosomal damage is a therapeutic target in Duchenne muscular dystrophy. Science Advances. https://www.semanticscholar.org/paper/3265a29ad8c2d48b294017fd50b6df9188b55ecb
8. Yinghui Ren, Yongmei Qian, Qicheng Zhang, Xiaoping Li, Mingjiang Li et al. (2024). High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma. Cancer Cell International. https://www.semanticscholar.org/paper/552bd37c67dea75d0c33a9a0de2acdafcf0dcf6e
9. Ying Yao, Jingyu Wang, T. He, Heyangzi Li, Jue Hu et al. (2020). Microarray assay of circular RNAs reveals cicRNA.7079 as a new anti-apoptotic molecule in spinal cord injury in mice.. Brain research bulletin. https://www.semanticscholar.org/paper/8e327ffbb4c66488f7c21b3dc5f8bcd5321ffdae
10. Jing Li, Hongtao Shen, G. Owens, Lian‐Wang Guo (2022). SREBP1 regulates Lgals3 activation in response to cholesterol loading. Molecular Therapy. Nucleic Acids. https://www.semanticscholar.org/paper/6c55d666855233ff0e7035d46075997924da854c
11. Mi Guan, Yanping Ma, S. Shah, G. Romano (2016). Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy. Oncolytic Virotherapy. https://www.semanticscholar.org/paper/9f79d851e32ad25e83c0a2d64e12919bf81a89f8
12. M. Shedenkova, Anastasiia A. Gurianova, I. Krasilnikova, A. Sudina, E. Karpulevich et al. (2025). Extracellular Vesicles from iPSC-Derived Glial Progenitor Cells Prevent Glutamate-Induced Excitotoxicity by Stabilising Calcium Oscillations and Mitochondrial Depolarisation. Cells. https://www.semanticscholar.org/paper/6a7fa01a0c5294235731390acdd5215a4a803f13