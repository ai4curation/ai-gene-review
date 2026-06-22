---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:46:05.981618'
end_time: '2026-06-22T04:46:09.421820'
duration_seconds: 3.44
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0005737
  hypothesis_text: LGALS3 has cytoplasm (GO:0005737).
  term_context: '- Term: cytoplasm (GO:0005737)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[4]
  source_context_yaml: "term:\n  id: GO:0005737\n  label: cytoplasm\nevidence_type:\
    \ IBA\noriginal_reference_id: GO_REF:0000033"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    query_char_limit: 500
    paper_limit: 50
    snippet_limit: 20
    snippet_paper_limit: 50
    restrict_snippets_to_papers: false
    paper_fields: title,abstract,authors,year,url,venue,journal,tldr,publicationDate,citationCount,influentialCitationCount,externalIds
    publication_date_range: ''
    venues: ''
    inserted_before: ''
citation_count: 14
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has cytoplasm (GO:0005737).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has cytoplasm (GO:0005737).
Key context:
- Term: cytoplasm (GO:0005737)
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
- **Hypothesis slug:** function-support-go-0005737
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[4]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0005737
  label: cytoplasm
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


## Output

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has cytoplasm (GO:0005737). Gene/protein: LGALS3. Organism: Hom...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 14
- Snippets retrieved: 20

## Relevant Papers

### [1] Physical Activity Attenuates the Obesity-Induced Dysregulated Expression of Brown Adipokines in Murine Interscapular Brown Adipose Tissue
- Authors: T. Sakurai, Toshiyuki Fukutomi, Sachiko Yamamoto, Eriko Nozaki, T. Kizaki
- Year: 2021
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/c62f909c1038a72ef7c427bfa9914983c22b5422
- DOI: 10.3390/ijms221910391
- PMID: 34638731
- PMCID: 8508858
- Citations: 2
- Summary: Results indicate that PA attenuates the obesity-induced dysregulated expression of brown adipokines and suggests that Lgals3 and Lgal3bp are involved in brown adipocyte differentiation.
- Evidence snippets:
  - Snippet 1 (score: 0.790)
    > In addition, although the Flag-tagged Lgals3 protein was secreted at each stage of brown adipocyte differentiation, most of this protein was uniformly present in the cytoplasm (Figure 1D). Furthermore, the expression of Flag-tagged Lgals3bp in the cytoplasm was heterogeneous compared with that of the Flag-tagged Lgals3 protein (Figure 1D).
  - Snippet 2 (score: 0.723)
    > Enhanced expression of Lgals3 gene is found in the WAT and the BAT of obese mice, and the insulin signal was reported to be altered in the WAT of Lgals3 knock out (KO) mice, but the influence of Lgals3 on brown adipocytes remains unknown [41,42]. Lgals3bp was identified as a protein that binds to Lgals3 and Lgals1, but its effect on brown adipocytes is also unknown [43]. As shown in Table 3, the expressions of genes for Lgals3 and Lgals3bp are thought to be greatly influenced by HFD intake and PA. Therefore, we attempted to establish an overexpression of Flag-tagged Lgals3 and Lgals3bp in HB2 cells. Real-time PCR analysis showed a significant increase in the expressions of Lgals3 and Lgals3bp mRNAs in Flag-tagged Lgals3 (HB2-L3 cells), Lgals3bp (HB2-L3bp cells), or both (HB2-L3-L3bp cells) when compared with that in control cells (HB2-C cells) (Figure 1A). Moreover, expression of exogenous Flag-tagged proteins in cell lysate and Flag-Lgals3 or Lgals3bp protein secretion into cell culture medium were confirmed in HB2-L3, -L3bp, and -L3-L3bp cells (Figure 1B). As shown in Figure 1B,C, in the differentiation process of HB2 cells into brown adipocytes, Flag-tagged Lgals3 protein was secreted the most during the early stages of differentiation, while the secretion from mature brown adipocytes was decreased by comparison. In contrast, the secretion of the Flag-tagged Lgals3bp protein from mature brown adipocytes was the most prominent. In addition, although the Flag-tagged Lgals3 protein was secreted at each stage of brown adipocyte differentiation, most of this protein was uniformly present in the cytoplasm (Figure 1D).

### [2] Selection signature analysis reveals genes underlying sheep milking performance
- Authors: Zehu Yuan, Wanhong Li, Fadi Li, X. Yue
- Year: 2019
- Venue: Archives Animal Breeding
- URL: https://www.semanticscholar.org/paper/fd4b15d018bfa94628954941797606d5d92cecb8
- DOI: 10.5194/aab-62-501-2019
- PMID: 31807661
- PMCID: 6859915
- Citations: 7
- Summary: SUCNR1 and PPARGC1A (PPARG coactivator 1 alpha) may be the most significant genes that affect sheep milking performance, which supply a significant indication for future studies to investigate candidate genes that play an important role in milk production and quality.
- Evidence snippets:
  - Snippet 1 (score: 0.783)
    > The most significant GO term of CC is cytoplasm (GO: 0005737, P =6.93E10-8, FDR = 2.98 × 10 −5 ). The most significant GO term of MF was the G-protein coupled nucleotide receptor activity (GO: 0001608, P = 6.37007×10 −5 , FDR = 6.37007×10 −5 ) and G-protein coupled purinergic nucleotide receptor activity (GO: 0045028, P = 6.37007 × 10 −5 , FDR = 6.37007 × 10 −5 ). The finding that the cytoplasm GO term (GO: 0005737) was enriched in our gene set is interesting. Previous studies have reported that candidate genes associated with milk protein composition traits in a Chinese Holstein population were significantly (FDR = 0.0247) enriched in cytoplasm (GO: 0005737) (Zhou et al., 2019). Apart from GO analysis, KEGG analysis showed that candidate genes could be annotated to 36 KEGG classes (Fig. S1) and could participate in 173 pathways. The highest number of genes of KEGG categories was signal transduction (29 genes). However, no significant pathways were found.

### [3] Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice
- Authors: Kevin A. Maupin, Daniel T. Dick, Vari Vivarium, Transgenics Core, B. Williams
- Year: 2020
- Venue: FEBS Open Bio
- URL: https://www.semanticscholar.org/paper/6ab62ea9acc6fef617d0b1f237c1a477f45b05c7
- DOI: 10.1002/2211-5463.13483
- PMID: 36062328
- PMCID: 9527582
- Citations: 2
- Summary: The results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3, while the cortical bone phenotypeof Lgal3- KO mice may have also been influenced by Loss of intracellular galECTin- 3.
- Evidence snippets:
  - Snippet 1 (score: 0.756)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.
  - Snippet 2 (score: 0.701)
    > s3 +/+ ), heterozygous (Lgals3-R200S KI/+ ), and homozygous (Lgals3-R200S KI/KI ) mutant mice (Fig. 1C). Consistent with a reduction in Gal-3 secretion, we observed significantly reduced Gal-3 protein levels in the plasma of adult heterozygous and homozygous mutant mice (Fig. 1D).
    > We generated mouse embryonic fibroblasts (MEFs) to look at cell-surface proteins, to confirm reduction of extracellular Gal-3 protein in Lgals3-R200S cells. Cell surface proteins were biotinylated and captured with NeutrAvidin Agarose. Western blot analysis showed cell surface Gal-3 levels were decreased in Lgals3-R200S KI/+ and Lgals3-R200S KI/KI cells compared to wild-type (Fig. 1E). The absence of the cytoplasmic protein, vinculin, from the pull-down lanes confirmed that the experiments worked to preferentially pull-down biotinylated cell surface proteins. Immunocytochemistry of MEFs from Lgals3-R200S KI/KI mice confirmed that Gal-3 is present in the cytosol and nucleus (Fig. 1F). Quantification of the mean and median amount of fluorescence per unit area indicated that Galectin-3 both on the cell surface and inside the cell was reduced, by approximately 30% and 26% respectively, in Lgals3-R200S KI/KI MEFs (P = 0.024). From these studies, we conclude that the R200S mutation in mice reduced cell surface Gal-3 and may have contributed to lower intracellular Gal-3 levels. Further studies will be necessary to determine if the 25-30% reduction in intracellular Gal-3 is biologically significant.

### [4] Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy
- Authors: Mi Guan, Yanping Ma, S. Shah, G. Romano
- Year: 2016
- Venue: Oncolytic Virotherapy
- URL: https://www.semanticscholar.org/paper/9f79d851e32ad25e83c0a2d64e12919bf81a89f8
- DOI: 10.2147/OV.S99856
- PMID: 27579295
- PMCID: 4996252
- Citations: 4
- Summary: This review focuses on the strategy of biomarkers for the production of novel TMN oncolytic therapeutics, which may improve the specificity of targeting of tumor cells and limit adverse effects in patients.
- Evidence snippets:
  - Snippet 1 (score: 0.738)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [5] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
- Authors: Kui Wang, Shuyue Fu, Lixia Dong, Dingyue Zhang, Mao Wang et al.
- Year: 2023
- Venue: Autophagy
- URL: https://www.semanticscholar.org/paper/3dadfc351823c4e325e65c171ab3765871189c80
- DOI: 10.1080/15548627.2023.2239042
- PMID: 37471054
- Citations: 35
- Influential citations: 2
- Summary: It is shown that periplocin exhibits promising anticancer activity against CRC both in vitro and in vivo, and is indicated as a potential therapeutic option for the treatment of CRC.
- Evidence snippets:
  - Snippet 1 (score: 0.734)
    > Scale bar: 10 μm. (I) Immunofluorescent analysis of the colocalization of LGALS3 with ubiquitin in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm. (J) Representative fluorescent images of CRC cells transiently expressing Mrfp-GFP-tandem fluorescent-tagged LGALS3 (tfGal3) followed by 0.50 μM periplocin treatment for 24 h. Scale bar: 10 μm. (K) Quantitative analysis of the GFP + RFP + or GFP − RFP + LGALS3 puncta in (J). (L) the relative decreased ratio of Magic Red intensity, relative increased ratio of LysoSensor Blue intensity, relative increased ratio of the interaction between LGALS3 and TRIM16, and relative increased ratio of LC3B-II protein level in DLD-1 cells following 0.50 μM periplocin treatment at different time periods. Results are representative of three independent experiments. Data are presented as mean ± SD. *P < 0.05, **P < 0.01, ***P < 0.001. for LGALS3 degradation, we generated lysine to arginine mutants of LGALS3 at K196 or Lys210 (LGALS3 K196R or LGALS3 K210R ). As shown in Figure 6I, the ubiquitinconjugated level of LGALS3 K196R mutant was comparable to the wild type (WT), whereas K210 mutation significantly decreased LGALS3 ubiquitination. These results suggest that periplocin elevates LGALS3 level by preventing K210 ubiquitination and proteasomal degradation. In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3.
  - Snippet 2 (score: 0.728)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.
  - Snippet 3 (score: 0.716)
    > In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3. The interaction between periplocin and LGALS3 was further confirmed by drug affinity responsive target stability (DARTS) analysis, as evidenced by a more stable property of LGALS3 protein against pronase digestion in response to periplocin treatment (Figure 6L,M). Moreover, using semiflexible docking analysis, we found that LGALS3 showed a good binding activity for periplocin, with a binding energy of −6.689 kcal/mol. Glu165, Arg162, Gly152, Gln150, Arg144, and Asn143 of LGALS3 were identified as possible sites for periplocin binding (Figure 6N,O), which required further experimental investigation. Together, these data suggest that periplocin binds and prevents ubiquitin-mediated degradation of LGALS3 in CRC cells.

### [6] Impairment of lysosomal quality control in Huntington disease
- Authors: P. Rusmini, F. Mina, M. Valenza, Martina Vitali, V. Ferrari et al.
- Year: 2025
- Venue: Cell Death & Disease
- URL: https://www.semanticscholar.org/paper/c874bbb3c9e6aa0a3f74519c022f3fa822daf4a8
- DOI: 10.1038/s41419-025-08103-z
- PMID: 41145409
- PMCID: 12559425
- Citations: 4
- Influential citations: 1
- Summary: TFEB and TFE3 are sequestered in muHTT aggregates, and muHTT proteins associates with LMP triggering the translocation of LGALS3 to the lumen of lysosomes, with a close relation between polyQ size and severity of these events.
- Evidence snippets:
  - Snippet 1 (score: 0.732)
    > In HD, high levels of LGALS3 have been found in plasma and brain of patients and mice. LGALS3 upregulation was observed in HD mice before the motor symptoms, in the microglia LGALS3 was found associated to damaged lysosomes and its suppression in microglia ameliorated the HD mice phenotype [36].
    > LGALS3 is emerging as a key factor for NDs for its intracellular role in lysosomal damage, but also for its functions linked to its secretion in the extracellular space. Many pieces of evidence suggest its detrimental role in neurodegeneration, even if a protective role of LGALS3 has been reported (reviewed in ref. [75]). LGALS3 mechanisms of action need further investigation but its pharmacological modulation might represent a valuable target for intervention for NDs. LGALS3 inhibitors have already been tested in metabolic and fibrotic diseases, and these approaches might be applied to NDs. 3′-bis-(4aryltriazol-1-yl) thiodigalactoside (GB039, formerly named TD139), a synthetic small molecule that antagonizes LGALS3 activity by binding to the carbohydrate recognition domain, was effective in idiopathic pulmonary fibrosis and retinal degeneration [76,77]. Pectins, plant cell wall polysaccharides, mostly obtained from citrus and apples, represent natural LGALS3 inhibitors [78,79].
    > In summary, our experiments suggest that LQC impairment might contribute to HD. Indeed, the LGALS3 accumulation observed in HD cellular models due to TFEB and TFE3 sequestration by muHTT inclusions causes LMP and lysophagy impairment, in turn, influences LQC.
    > Fig. 8 TFEB and TFE3 sequestration affects the LQC. A, B NSC-34 cells were transfected with wt or muHTT.
  - Snippet 2 (score: 0.689)
    > A, B NSC-34 cells were transfected with wt or muHTT. (A) Representative images by confocal microscopy of double immunostaining with anti-LAMP1 (green) and anti-HTT antibody (red), nuclei were stained with DAPI (blue) (63X magnification). Scale bar: 10 μm. B the scatter dot blot represents the quantification of lysosome volume. The fields were randomly selected and at least 100 cells for each sample were analyzed (***p < 0.001, one-way ANOVA with Tukey's test). C, D NSC-34 cells were cotransfected with wt or mutant HTT and EGFP-LGALS3. C Representative images by confocal microscopy of EGFP-LGALS3 (green) and IF staining with anti-HTT antibody (red), nuclei were stained with DAPI (blue) (63X magnification). Scale bar: 10 μm. D LGALS3 puncta assay. The bar graph represents the quantification of percentage of cells with >3 GFP-LGALS3 puncta. (** p < 0.005, **** p < 0.0001, one-way ANOVA with Tukey's test). NSC-34 cells were co-transfected with EGFP-LGALS3, FLAG-TFEB (E), FLAG-TFE3 (F), or EV, and wt or muHTT. LGALS3 puncta assay was performed. The graphs with individual values represent the quantification of percentage of cells with >3 GFP-LGALS3 puncta (**p < 0.005, ****p < 0.0001, two-way ANOVA with Bonferroni's test).

### [7] LGALS3 Is a Poor Prognostic Factor in Diffusely Infiltrating Gliomas and Is Closely Correlated With CD163+ Tumor-Associated Macrophages
- Authors: Wan-Ming Hu, Yuan-Zhong Yang, Tian Zhang, Changling Qin, Xuenong Li
- Year: 2020
- Venue: Frontiers in Medicine
- URL: https://www.semanticscholar.org/paper/53b083f91a08aefebb5f9edaaa95625e2dc98f2b
- DOI: 10.3389/fmed.2020.00182
- PMID: 32528967
- PMCID: 7254797
- Citations: 18
- Influential citations: 1
- Summary: LGALS3 was an independent poor prognostic marker in diffusely infiltrating gliomas and was positively correlated with immune cell infiltration, particularly CD163+ tumor-associated macrophages in the TCGA dataset, Rembrandt dataset, and the SYSUCC cohort.
- Evidence snippets:
  - Snippet 1 (score: 0.723)
    > In the LGALS family, LGALS3 has a special domain that recognizes and binds to β-galactosides on cellular glycoproteins and glycolipids (5).
    > LGALS3 may be observed in the cytoplasm and in the nucleus as well as the extracellular matrix (6). It serves different biological functions, such as cell growth, cell adhesion, angiogenesis, and apoptosis (7).
    > LGALS3 can be expressed in different types of tumors, and accumulating evidence has proved that LGALS3 plays a vital role in tumorigenesis and development (6,(8)(9)(10)(11)(12)(13)(14)(15)(16). Recently, a study indicated that LGALS3 can promote the therapeutic resistance of glioblastoma and is related to tumor risk and prognosis (17). However, its prognostic significance needs to be further confirmed in large glioma samples, and, hitherto, no studies have explored the role of LGALS3 in the glioma immune microenvironment and its correlation with key molecular markers, including isocitrate dehydrogenase 1 (IDH1), alpha-thalassemia/mental retardation X-linked (ATRX), O-6methylguanine-DNA methyltransferase (MGMT), telomerase reverse transcriptase (TERT), and 1p19q.
  - Snippet 2 (score: 0.702)
    > LGALS3 was Mainly Expressed in Pilocytic Astrocytoma, GBM, and IDH Wild-Type LGG
    > LGALS3 was mainly expressed in cytoplasm, and weak expression in endothelial cells was used as an internal control in glioma. The typical positive and negative results of IHC staining for LGALS3 in glioma are presented in Figures 1A-D. Distinctly high expression of LGALS3 was observed in pilocytic astrocytoma and GBM, both with a diffuse pattern (Figures 1E-H). In total, out of all 304 glioma cases, LGALS3 protein expression was positive in 125 glioma cases (41.1%, 125/304), with 69.2% (9/13) in WHO I (pilocytic astrocytoma), 9.8% (8/82) in WHO II (diffuse astrocytoma and oligodendroglioma), 34.2% (26/76) in WHO III (anaplastic astrocytoma and oligodendroglioma), and 61.7% (82/133) in WHO IV (glioblastoma) (Figure S2A). Further analysis showed that LGALS3 was mainly expressed in IDH wildtype LGG compared with IDH mutated LGG (Figure S2B). LGALS3-positive patients presented with significantly shorter OS than those of negative patients in all the gliomas, LGG, GBM, AA, and IDH glioma but no statistical difference in PA. PA, pilocytic astrocytoma; LGG, lower grade glioma; GBM, glioblastoma; AA, anaplastic astrocytoma.
    > = 0.002). Kaplan-Meier plots revealed that LGALS3 expression was a significantly unfavorable prognostic marker in diffusely infiltrating gliomas (WHO II-IV) but not in pilocytic glioma (WHO I).

### [8] Identification of an Internal Gene to the Human Galectin-3 Gene with Two Different Overlapping Reading Frames That Do Not Encode Galectin-3*
- Authors: M. Guittaut, Stéphane Charpentier, Thierry Normand, Martine Dubois, J. Raimond et al.
- Year: 2001
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/75ca62f4b6eb66b3bcdac062664da410941fdcaa
- DOI: 10.1074/JBC.M002523200
- PMID: 11160123
- Citations: 37
- Influential citations: 6
- Summary: It is demonstrated that these transcripts arise from an internal gene embedded within LGALS3 and named galig (Galectin-3 internal gene), which appears to be tightly regulated and principally activated in leukocytes from peripheral blood.
- Evidence snippets:
  - Snippet 1 (score: 0.719)
    > Human Rapid-Scan Gene Expression Panel was used to detect the alternative transcripts in various human tissues using RT-PCR. The primers used were designed to amplify a 923-or 629-bp fragment.
    > LGALS3 transcripts were detected as a 457-bp DNA and actin transcripts as a 640-bp DNA. PCR was performed using 0.25 ng or 2.5 ng (10ϫ) template cDNA.
    > average of other human proteins is 10 times lower. This rich content in tryptophans confers hydrophobic properties that may account for the membrane localization of the ORF2⅐EGFP protein (Fig. 6). Consistent with the mitochondrial localization of the ORF2⅐EGFP fusion protein, this sequence exhibits the common properties of mitochondrial-imported proteins such as the enrichment of arginine, leucine, and serine residues (36).
    > Tissue Specificity of galig Expression-Detection of galig transcripts in HOS cells and colon tumor cells revealed a low expression level. Based on this observation, the rationale that the appearance of galig transcripts may have resulted from a leaky transcription of a cryptic promoter rather than from an independently functioning promoter could not be excluded. Screening of several human tissues indicated clearly that galig is a tightly regulated gene whose expression is most efficient in leukocytes from peripheral blood. The low level of transcription in bone marrow indicates that galig is specifically expressed in mature forms of leukocytes. Whereas the precise quantification of galig mRNA has not been addressed in these experiments, it is clear that these transcripts are much less abundant than LGALS3 transcripts. This may not be surprising considering that LGALS3 is known to be highly expressed when activated (37,38). Indeed, the amount of LGALS3 transcripts appeared as abundant as those from actin genes. This shows a different type of regulation by the galig and LGALS3 promoters. In particular, muscle, stomach, and uterus, although expressing low levels of galig transcripts, revealed no LGALS3 transcripts, thus indicating an independent functioning of the two promoters.

### [9] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
- Authors: P. Ruvolo, Chenyue W. Hu, Y. Qiu, V. Ruvolo, Robin L. Go et al.
- Year: 2019
- Venue: EBioMedicine
- URL: https://www.semanticscholar.org/paper/46bbdbcb4660389e13acba24499cc415d75f18e0
- DOI: 10.1016/j.ebiom.2019.05.025
- PMID: 31105032
- PMCID: 6604360
- Citations: 25
- Influential citations: 2
- Summary: The data suggest that the LGALS3 network and the CD74 network each support AML cell survival and the two networks may cooperate in a novel high risk AML population.
- Evidence snippets:
  - Snippet 1 (score: 0.717)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.

### [10] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
- Authors: Yinghui Ren, Yongmei Qian, Qicheng Zhang, Xiaoping Li, Mingjiang Li et al.
- Year: 2024
- Venue: Cancer Cell International
- URL: https://www.semanticscholar.org/paper/552bd37c67dea75d0c33a9a0de2acdafcf0dcf6e
- DOI: 10.1186/s12935-024-03309-1
- PMID: 38643145
- PMCID: 11031979
- Citations: 13
- Summary: It is hypothesized that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC and the upregulation of LGALS3 via the HCP5/hsa-miR-27b-3p axis is associated with unfavorable prognosis and increased tumor immune infiltration in HCC.
- Evidence snippets:
  - Snippet 1 (score: 0.705)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.

### [11] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
- Authors: Tammy R. Chaudoin, S. Bonasera
- Year: 2018
- Venue: BMC Neuroscience
- URL: https://www.semanticscholar.org/paper/26255eafb963932be62ecb55d4943930217cb63f
- DOI: 10.1186/s12868-018-0428-x
- PMID: 29716523
- PMCID: 5930520
- Citations: 7
- Influential citations: 1
- Summary: P perturbation of behavioral circadian rhythms in Lgals3−/− mice is noted, with mice at both ages demonstrating greater variability in day-to-day performance of feeding, drinking, and movement compared to wildtype.
- Evidence snippets:
  - Snippet 1 (score: 0.697)
    > atlases suggest that Lgals3 expression (at low-to-moderate levels) occurs in both pre-and post-natal brain, and has been localized to regions involved in motor behavior generation, including the cortex, striatum, cerebellum, and spinal cord. We thus argue that Lgals3 loss alters mouse motor function, either through its impact on motor development or through altered neuronal signaling in CNS regions that regulate or produce motor behavior. Further studies examining the consequences of Lgals3 loss at synaptic, neuronal, ensemble, and tissue levels of organization will be required to determine the precise mechanisms underlying this functional loss. Grey bands depict periods where mouse cohorts were tested in the home cage monitoring system. Note that neither axis begins at 0. Sampling interval for x-axis is 7 days except where noted by breakpoints
    > As mentioned earlier, Lgals3 has been implicated in a large number of physiological tasks at both a cellular and organwide level of organization. It is thus notable that mice with complete loss of Lgals3 function demonstrate relatively few behavioral differences when compared to wildtype C57BL/6J mice. This finding suggests that, at least in the mouse, there is some genetic redundancy regarding Lgals3 function. Studies of galectin evolution focusing on intron/exon organization as well as sequence identity suggest that duplication of ancestral galectin genes in animal lineages preceding the first teleost fish [62] provided the precursors for what has become a large vertebrate protein family [63]. There is also data suggesting that galectins may be able to substitute for one another in specific circumstances. For example, Lgals1 may compensate for Lgals3 loss at the spliceosome [64]. Extracellular Lgals1 also regulates T cell apoptosis in a manner similar to that of extracellular Lgals3 [65]. The behavioral phenotype arising from Lgals3 functional loss thus identifies neuronal loci and processes where there is no compensation for gene loss.

### [12] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
- Authors: Tammy R. Chaudoin, S. Bonasera
- Year: 2018
- Venue: BMC Neuroscience
- URL: https://www.semanticscholar.org/paper/613a09b176431cdca195e6b3c439b4edbe4f92af
- DOI: 10.1186/s12868-018-0428-x
- Summary: P perturbation of behavioral circadian rhythms in Lgals3−/− mice is noted, with mice at both ages demonstrating greater variability in day-to-day performance of feeding, drinking, and movement compared to wildtype.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > atlases suggest that Lgals3 expression (at low-to-moderate levels) occurs in both pre-and post-natal brain, and has been localized to regions involved in motor behavior generation, including the cortex, striatum, cerebellum, and spinal cord. We thus argue that Lgals3 loss alters mouse motor function, either through its impact on motor development or through altered neuronal signaling in CNS regions that regulate or produce motor behavior. Further studies examining the consequences of Lgals3 loss at synaptic, neuronal, ensemble, and tissue levels of organization will be required to determine the precise mechanisms underlying this functional loss. Grey bands depict periods where mouse cohorts were tested in the home cage monitoring system. Note that neither axis begins at 0. Sampling interval for x-axis is 7 days except where noted by breakpoints
    > As mentioned earlier, Lgals3 has been implicated in a large number of physiological tasks at both a cellular and organwide level of organization. It is thus notable that mice with complete loss of Lgals3 function demonstrate relatively few behavioral differences when compared to wildtype C57BL/6J mice. This finding suggests that, at least in the mouse, there is some genetic redundancy regarding Lgals3 function. Studies of galectin evolution focusing on intron/exon organization as well as sequence identity suggest that duplication of ancestral galectin genes in animal lineages preceding the first teleost fish [62] provided the precursors for what has become a large vertebrate protein family [63]. There is also data suggesting that galectins may be able to substitute for one another in specific circumstances. For example, Lgals1 may compensate for Lgals3 loss at the spliceosome [64]. Extracellular Lgals1 also regulates T cell apoptosis in a manner similar to that of extracellular Lgals3 [65]. The behavioral phenotype arising from Lgals3 functional loss thus identifies neuronal loci and processes where there is no compensation for gene loss.

### [13] In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression
- Authors: A. Montero‐Calle, Á. López-Janeiro, Marta L. Mendes, Daniel Perez-Hernandez, Irene Echevarría et al.
- Year: 2023
- Venue: Cellular Oncology
- URL: https://www.semanticscholar.org/paper/92b64e01bcb30f7457ddb8cc4be26de8b0c7cf69
- DOI: 10.1007/s13402-023-00778-w
- PMID: 36745330
- PMCID: 10205863
- Citations: 19
- Summary: C1GALT1 stably depleted ECC-1 cells mimic an EC aggressive phenotype observed in patients and might be useful for the identification and validation of EC markers of progression.
- Evidence snippets:
  - Snippet 1 (score: 0.696)
    > Finally, since LGALS3 (Galectin-3) has been shown to interact with O-glycans in the mucosal epithelium [30], and considering its overexpression observed by proteomics and further confirmed by PCR and WB analyses upon depletion of C1GALT1, we focused on the role of LGALS3 in EC by IHC.
    > A total of 151 out of 178 cores from 79 EC patients were considered adequate for LGALS3 expression assessment by IHC. Morphologic assessment of LGALS3 IHC staining characteristics revealed different staining patterns (Fig. 5 A). Out of the 151 evaluable cores, 45 (29.8%) showed absent LGALS3 expression. LGALS3 positive samples showed variable and low intensity protein expression (mean positive tumor cells per sample = 35.4%). A small subset of cores (13/151, 8.6%) demonstrated diffuse (> 90% positive tumor cells per sample) staining. LGALS3 score varied across histologic types, with serous and undifferentiated tumors displaying the highest protein expression (median IHC LGALS3 score = 10, 20, 50 and 55 for endometrioid, clear cell, serous and undifferentiated tumor types, respectively) (Fig. 5B). Interestingly, the aggressive histologic variants (clear cell, serous and undifferentiated) showed higher LGALS3 IHC scores than endometrioid variants (p value < 0.001). In addition, LGALS3 expression positively correlated with tumor grade. High grade tumors (G3) displayed higher protein expression (median LGALS3 IHC score = 30) compared to low grade tumors (median LGALS3 IHC score for G1/G2 tumors = 10). This finding was independent of histologic type, as similar results were observed when analyzing endometrioid tumors.
    > Finally, we interrogated the correlation between the expression levels of LGALS3 and C1GALT1.

### [14] Lysosomal damage is a therapeutic target in Duchenne muscular dystrophy
- Authors: Abbass Jaber, Laura Palmieri, R. Bakour, N. Bourg, A. Hong et al.
- Year: 2025
- Venue: Science Advances
- URL: https://www.semanticscholar.org/paper/3265a29ad8c2d48b294017fd50b6df9188b55ecb
- DOI: 10.1126/sciadv.adv6805
- PMID: 41124255
- PMCID: 12542950
- Citations: 7
- Summary: Lysosomal perturbations in myofibers of patients with DMD and animal models are identified, highlighting lysosomal damage as an important pathomechanism in DMD and suggesting that combining trehalose with gene therapy could enhance therapeutic efficacy.
- Evidence snippets:
  - Snippet 1 (score: 0.690)
    > To investigate whether cholesterol accumulation in dystrophic muscle is associated with the impaired lysosomal function, we sought a method to quantify lysosomal damage. Several studies have recently focused on lysosomal dysfunction, in which LMP plays a central role (18). However, very few studies have investigated lysosome damage in muscle. One identified marker of LMP is Gal-3 (or LGALS3), which is part of the galectins, a family of lectins that bind specifically to carbohydrates (19). These lectins are present in the cytosol, nucleus, and extracellular matrix and are translocated to the membrane of damaged lysosomes before their removal by the autophagy machinery (20). To analyze LGALS3 expression in a myogenic environment and its capacity to detect LMP, we differentiated healthy human immortalized myoblasts into elongated myotubes for 7 days and then performed immunostaining for LGALS3 and lysosome-associated membrane protein 2 (LAMP2), which is commonly used as a lysosome marker (21). A diffuse expression of LGALS3 was observed in the cells (fig. S1A). Treatment with l-leucyl-l-leucine methyl ester (LLOMe), a lysomotropic agent that induces lysosome-specific membrane damage (22), for 30 min at 2.5 mM triggered the formation of LGALS3-positive puncta, which colocalized with LAMP2, indicating typical damaged lysosomes. An up-regulation of LGALS3 was also detected by Western blotting after 30 min to 1 hour of LLOMe treatment (fig. S1, B and C). LGALS3 puncta were markedly reduced 3 hours after treatment, and LGALS3 expression was restored to the control level, demonstrating efficient lysosomal repair by the cells. This pattern correlated inversely with the amount of LGALS3 released in the media, detected by an enzyme-linked immunosorbent assay (ELISA) assay (fig.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.