---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:45:54.802431'
end_time: '2026-06-22T04:46:01.863834'
duration_seconds: 7.06
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0005634
  hypothesis_text: LGALS3 has nucleus (GO:0005634).
  term_context: '- Term: nucleus (GO:0005634)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[3]
  source_context_yaml: "term:\n  id: GO:0005634\n  label: nucleus\nevidence_type:\
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
citation_count: 12
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has nucleus (GO:0005634).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has nucleus (GO:0005634).
Key context:
- Term: nucleus (GO:0005634)
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
- **Hypothesis slug:** function-support-go-0005634
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[3]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0005634
  label: nucleus
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has nucleus (GO:0005634). Gene/protein: LGALS3. Organism: Homo...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 12
- Snippets retrieved: 20

## Relevant Papers

### [1] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
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
  - Snippet 1 (score: 0.779)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.
  - Snippet 2 (score: 0.764)
    > Scale bar: 10 μm. (I) Immunofluorescent analysis of the colocalization of LGALS3 with ubiquitin in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm. (J) Representative fluorescent images of CRC cells transiently expressing Mrfp-GFP-tandem fluorescent-tagged LGALS3 (tfGal3) followed by 0.50 μM periplocin treatment for 24 h. Scale bar: 10 μm. (K) Quantitative analysis of the GFP + RFP + or GFP − RFP + LGALS3 puncta in (J). (L) the relative decreased ratio of Magic Red intensity, relative increased ratio of LysoSensor Blue intensity, relative increased ratio of the interaction between LGALS3 and TRIM16, and relative increased ratio of LC3B-II protein level in DLD-1 cells following 0.50 μM periplocin treatment at different time periods. Results are representative of three independent experiments. Data are presented as mean ± SD. *P < 0.05, **P < 0.01, ***P < 0.001. for LGALS3 degradation, we generated lysine to arginine mutants of LGALS3 at K196 or Lys210 (LGALS3 K196R or LGALS3 K210R ). As shown in Figure 6I, the ubiquitinconjugated level of LGALS3 K196R mutant was comparable to the wild type (WT), whereas K210 mutation significantly decreased LGALS3 ubiquitination. These results suggest that periplocin elevates LGALS3 level by preventing K210 ubiquitination and proteasomal degradation. In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3.
  - Snippet 3 (score: 0.738)
    > Therefore, periplocininduced lysophagy-mediated clearance of damaged lysosomes can nonspecifically engulf vicinal functional lysosomes when lysosome fusion occurs, leading to excessive lysophagy and subsequent cell death. Our findings thus demonstrate a cytotoxic mechanism of lysophagy, and suggest a contextdependent manner for lysophagy-mediated cell fate decision. In addition, we found that periplocin treatment promoted the translocation of TFEB (transcription factor EB) into the nucleus (Figure S7A,B). Interestingly, periplocin treatment led to increased TFEB nuclear translocation and LGALS3 expression both in a time-dependent manner. While the protein level of LGALS3 increased at 1 h of periplocin treatment, the level of nuclear TFEB increased at 3-6 h after periplocin treatment (Figure S7C,D). These data imply that TFEB nuclear translocation and activation in periplocin-treated CRC cells may represent a compensate mechanism for lysosomal damage through promoting the lysosomal biogenesis.
    > Target identification is the initial and critical step for understanding the mechanism of action and development of novel natural products [50,56]. In this study, we found periplocin physically engaged LGALS3 in living CRC cells, suggesting LGALS3 is a binding target of periplocin. Further studies are needed to confirm the direct binding using recombinant LGALS3 protein. The binding of periplocin inhibited ubiquitin-mediated degradation of LGALS3, leading to elevated protein level of LGALS3. Periplocin binding might affect the conformational change of LGALS3 and decrease its binding with related E3 ligase, thereby preventing ubiquitin-mediated degradation of LGALS3, which also requires further investigation. Upregulated LGALS3 was then recruited to the lysosomes following periplocin treatment to initiate excessive lysophagy machinery.
  - Snippet 4 (score: 0.725)
    > In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3. The interaction between periplocin and LGALS3 was further confirmed by drug affinity responsive target stability (DARTS) analysis, as evidenced by a more stable property of LGALS3 protein against pronase digestion in response to periplocin treatment (Figure 6L,M). Moreover, using semiflexible docking analysis, we found that LGALS3 showed a good binding activity for periplocin, with a binding energy of −6.689 kcal/mol. Glu165, Arg162, Gly152, Gln150, Arg144, and Asn143 of LGALS3 were identified as possible sites for periplocin binding (Figure 6N,O), which required further experimental investigation. Together, these data suggest that periplocin binds and prevents ubiquitin-mediated degradation of LGALS3 in CRC cells.
  - Snippet 5 (score: 0.705)
    > As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3. In addition, periplocin did not affect the ubiquitination of other proteins, such as PHGDH (phosphoglycerate dehydrogenase) and PRMT1 (protein arginine methyltransferase 1) (Figure S6B,C), and had no obvious effect on the expression of several essential proteasome components (Figure S6D,E). These data suggest that periplocin specifically prevents LGALS3 from ubiquitin-mediated degradation, regardless of the general ubiquitylation status of the proteasome. A previous study of systematic ubiquitination profiling identified Lys196 (K196) and Lys210 (K210) as the potential ubiquitination sites of LGALS3 [47]. To determine the ubiquitination site required without 0.50 μM periplocin for 24 h. (D) Immunoblotting analysis of PRKAA, p-PRKAA (Thr172), ACACA, p-ACACA (Ser79), MTOR, and p-MTOR (Ser2448) in cells treated with periplocin for 24 h at the indicated concentrations. (E and F) Reciprocal co-immunoprecipitation analysis of the interaction between endogenous LGALS3 and TRIM16 in cells treated with or without 0.50 μM periplocin for 24 h. (G) Co-immunoprecipitation analysis of the interaction between endogenous LGALS3 with PDCD6IP/Alix, CHMP4B, and TRIM16 in DLD-1 cells treated with 0.50 μM periplocin at different time periods. (H) Immunofluorescent analysis of the colocalization of LC3B with LGALS3 in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm.

### [2] Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy
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
  - Snippet 1 (score: 0.767)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [3] Impairment of lysosomal quality control in Huntington disease
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
  - Snippet 1 (score: 0.748)
    > In HD, high levels of LGALS3 have been found in plasma and brain of patients and mice. LGALS3 upregulation was observed in HD mice before the motor symptoms, in the microglia LGALS3 was found associated to damaged lysosomes and its suppression in microglia ameliorated the HD mice phenotype [36].
    > LGALS3 is emerging as a key factor for NDs for its intracellular role in lysosomal damage, but also for its functions linked to its secretion in the extracellular space. Many pieces of evidence suggest its detrimental role in neurodegeneration, even if a protective role of LGALS3 has been reported (reviewed in ref. [75]). LGALS3 mechanisms of action need further investigation but its pharmacological modulation might represent a valuable target for intervention for NDs. LGALS3 inhibitors have already been tested in metabolic and fibrotic diseases, and these approaches might be applied to NDs. 3′-bis-(4aryltriazol-1-yl) thiodigalactoside (GB039, formerly named TD139), a synthetic small molecule that antagonizes LGALS3 activity by binding to the carbohydrate recognition domain, was effective in idiopathic pulmonary fibrosis and retinal degeneration [76,77]. Pectins, plant cell wall polysaccharides, mostly obtained from citrus and apples, represent natural LGALS3 inhibitors [78,79].
    > In summary, our experiments suggest that LQC impairment might contribute to HD. Indeed, the LGALS3 accumulation observed in HD cellular models due to TFEB and TFE3 sequestration by muHTT inclusions causes LMP and lysophagy impairment, in turn, influences LQC.
    > Fig. 8 TFEB and TFE3 sequestration affects the LQC. A, B NSC-34 cells were transfected with wt or muHTT.

### [4] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
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
  - Snippet 1 (score: 0.747)
    > Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated. Induction of PPP2R2A protein (Fig. 5) but not gene expression (Fig. 7) in THP-1 cells expressing LGALS3 shRNA suggests that LGALS3 acts directly on the PP2A subunits via a post-transcriptional mechanism in these cells. The TCGA data (Table 3) however suggests that there is a positive correlation between gene expression of LGALS3 and PPP2R2A suggesting that a common pathway may regulate the two genes. Fig. 8. Progeny clustering identified an optimal number of 4 distinct protein clusters for this ProFnGrp. Protein networks were generated and showed interactions between "core-proteins" (large nodes) and other probed proteins (small nodes) from the data set. Clustering method has been described in our previous publication (ref. [37]) and further information on these protein networks can be found on our website "Leukemia Profile Atlases", available at https://www.leukemiaatlas.org/. Progeny clustering identified one protein cluster with expression similar to that of the normal CD34+ samples which was designated as "normal-state" while three "leukemia-specific" protein patterns characterized by high expression individually of CD74, LGAL3, and a fourth state with both on. PPP2RA/B/C/D was the only LGALS3 network protein demonstrated to be directly regulated by LGALS3 in the THP-1 cells (Fig. 5). In our previous study we saw potent suppression of AKT signaling by LGALS3 inhibition, so perhaps the mechanism involves LGALS3 suppression of the AKT phosphatase [15]. However, we did not see suppression of LGALS3 affect other network proteins in the THP-1 cells (data not shown). The role of other galectins such as LGALS1 in AML biology is not clear.
  - Snippet 2 (score: 0.742)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.

### [5] LGALS3 Is a Poor Prognostic Factor in Diffusely Infiltrating Gliomas and Is Closely Correlated With CD163+ Tumor-Associated Macrophages
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
  - Snippet 1 (score: 0.732)
    > In the LGALS family, LGALS3 has a special domain that recognizes and binds to β-galactosides on cellular glycoproteins and glycolipids (5).
    > LGALS3 may be observed in the cytoplasm and in the nucleus as well as the extracellular matrix (6). It serves different biological functions, such as cell growth, cell adhesion, angiogenesis, and apoptosis (7).
    > LGALS3 can be expressed in different types of tumors, and accumulating evidence has proved that LGALS3 plays a vital role in tumorigenesis and development (6,(8)(9)(10)(11)(12)(13)(14)(15)(16). Recently, a study indicated that LGALS3 can promote the therapeutic resistance of glioblastoma and is related to tumor risk and prognosis (17). However, its prognostic significance needs to be further confirmed in large glioma samples, and, hitherto, no studies have explored the role of LGALS3 in the glioma immune microenvironment and its correlation with key molecular markers, including isocitrate dehydrogenase 1 (IDH1), alpha-thalassemia/mental retardation X-linked (ATRX), O-6methylguanine-DNA methyltransferase (MGMT), telomerase reverse transcriptase (TERT), and 1p19q.

### [6] Lgals3 Promotes Calcium Oxalate Crystal Formation and Kidney Injury Through Histone Lactylation‐Mediated FGFR4 Activation
- Authors: Zehua Ye, Yushi Sun, Songyuan Yang, Lei Li, Bojun Li et al.
- Year: 2025
- Venue: Advanced Science
- URL: https://www.semanticscholar.org/paper/adbfa30b5832407d200a5eade9196d41be08050e
- DOI: 10.1002/advs.202413937
- PMID: 39903812
- PMCID: 11947994
- Citations: 18
- Summary: Findings suggest that Lgals3 may play a key role in CaOx stone formation and kidney injury by interacting with PKM2 and promoting both H3K18la‐mediated gene transcription and activation.
- Evidence snippets:
  - Snippet 1 (score: 0.729)
    > Furthermore, this study investigated whether Lgals3 deficiency reduced H3K18la during CaOx deposition. Western blot and immunofluorescence staining showed that Lgals3 knockdown in vitro decreased the levels of global lactylation and H3K18la levels (Figure 9E-G). Similarly, Lgals3 −/− mice exhibited significant decreases in global lactylation and H3K18la levels compared with the WT mice through Western blot and immunofluorescence staining (Figure 9H-J). Meanwhile, we also tested the level of acetylation of histone H3 and histone H4 and the results showed that Lgals3 deficiency have no impact on the expression of acetylation of histone H3 and histone H4 (Figure S9, Supporting Information)

### [7] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
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
  - Snippet 1 (score: 0.726)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly
  - Snippet 2 (score: 0.724)
    > Next, the prognostic value of LGALS3 expression in the 23 kinds of cancer patients was then determined.Correlations between LGALS3 expression with OS (overall survival) were evaluated using the GEPIA2 database.In the OS study, only elevated LGALS3 expression indicated poorer survival for HCC patients (Fig. 2A).LGALS3 was not statistically significant for OS of 22 other cancer types patients.Furthermore, DSS (disease-specific survival) LGALS3 in predicting 1-, 3-, and 5-year OS. (H) ROC curve for LGALS3 in predicting 1-, 3-, and 5-year DSS.The higher values of AUC corresponding to higher predictive power.*p value < 0.05; ***p value < 0.001 was lesser in patients suffering from HCC having higher levels of LGALS3 expression (Fig. 2B).Next, we validated the expression levels of LGALS3 protein in HCC tissues using IF staining.As expected, HCC tumor demonstrated strong LGALS3 expression (Fig. 2C).These findings were further validated by qRT-PCR assay of tumor and adjacent normal tissues from 5 HCC patients.Here, LGALS3 expression was also significantly increased in the HCC tissues (Fig. 2D).In addition, LGALS3 expression was shown to be linked with the pathological stage of HCC, as illustrated in Fig. 2E.High expression of LGALS3 gene is associated with high tumor grade in HCC (Fig. 2F).Moreover, LGALS3 expression was significantly associated with OS and DSS in both univariate and multivariate analyses (Figure S2A-H).Time-dependent ROC analysis showed that the area under the ROC curve was 0.672 at 5 years of OS, and 0.691 at 5 years of DSS (Fig. 2G-H).Taken together, LGALS3 might function as a prospective biomarker for the prognosis of patients suffering from HCC.
  - Snippet 3 (score: 0.710)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.

### [8] Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice
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
  - Snippet 1 (score: 0.723)
    > s3 +/+ ), heterozygous (Lgals3-R200S KI/+ ), and homozygous (Lgals3-R200S KI/KI ) mutant mice (Fig. 1C). Consistent with a reduction in Gal-3 secretion, we observed significantly reduced Gal-3 protein levels in the plasma of adult heterozygous and homozygous mutant mice (Fig. 1D).
    > We generated mouse embryonic fibroblasts (MEFs) to look at cell-surface proteins, to confirm reduction of extracellular Gal-3 protein in Lgals3-R200S cells. Cell surface proteins were biotinylated and captured with NeutrAvidin Agarose. Western blot analysis showed cell surface Gal-3 levels were decreased in Lgals3-R200S KI/+ and Lgals3-R200S KI/KI cells compared to wild-type (Fig. 1E). The absence of the cytoplasmic protein, vinculin, from the pull-down lanes confirmed that the experiments worked to preferentially pull-down biotinylated cell surface proteins. Immunocytochemistry of MEFs from Lgals3-R200S KI/KI mice confirmed that Gal-3 is present in the cytosol and nucleus (Fig. 1F). Quantification of the mean and median amount of fluorescence per unit area indicated that Galectin-3 both on the cell surface and inside the cell was reduced, by approximately 30% and 26% respectively, in Lgals3-R200S KI/KI MEFs (P = 0.024). From these studies, we conclude that the R200S mutation in mice reduced cell surface Gal-3 and may have contributed to lower intracellular Gal-3 levels. Further studies will be necessary to determine if the 25-30% reduction in intracellular Gal-3 is biologically significant.
  - Snippet 2 (score: 0.720)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.

### [9] In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression
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
  - Snippet 1 (score: 0.711)
    > Finally, since LGALS3 (Galectin-3) has been shown to interact with O-glycans in the mucosal epithelium [30], and considering its overexpression observed by proteomics and further confirmed by PCR and WB analyses upon depletion of C1GALT1, we focused on the role of LGALS3 in EC by IHC.
    > A total of 151 out of 178 cores from 79 EC patients were considered adequate for LGALS3 expression assessment by IHC. Morphologic assessment of LGALS3 IHC staining characteristics revealed different staining patterns (Fig. 5 A). Out of the 151 evaluable cores, 45 (29.8%) showed absent LGALS3 expression. LGALS3 positive samples showed variable and low intensity protein expression (mean positive tumor cells per sample = 35.4%). A small subset of cores (13/151, 8.6%) demonstrated diffuse (> 90% positive tumor cells per sample) staining. LGALS3 score varied across histologic types, with serous and undifferentiated tumors displaying the highest protein expression (median IHC LGALS3 score = 10, 20, 50 and 55 for endometrioid, clear cell, serous and undifferentiated tumor types, respectively) (Fig. 5B). Interestingly, the aggressive histologic variants (clear cell, serous and undifferentiated) showed higher LGALS3 IHC scores than endometrioid variants (p value < 0.001). In addition, LGALS3 expression positively correlated with tumor grade. High grade tumors (G3) displayed higher protein expression (median LGALS3 IHC score = 30) compared to low grade tumors (median LGALS3 IHC score for G1/G2 tumors = 10). This finding was independent of histologic type, as similar results were observed when analyzing endometrioid tumors.
    > Finally, we interrogated the correlation between the expression levels of LGALS3 and C1GALT1.

### [10] Galectin-3 aggravates microglial activation and tau transmission in tauopathy
- Authors: Jian-Jing Siew, Hui-Mei Chen, Feng‐Lan Chiu, Chia-Wei Lee, Yao-Ming Chang et al.
- Year: 2023
- Venue: The Journal of Clinical Investigation
- URL: https://www.semanticscholar.org/paper/8c77eea796475aa4e26a4051432bc4d4c021d847
- DOI: 10.1172/JCI165523
- PMID: 37988169
- PMCID: 10786694
- Citations: 24
- Influential citations: 1
- Summary: It is shown that Gal3 was upregulated in the microglia of humans and mice with tauopathy, and is a potential therapeutic target for tauopathy.
- Evidence snippets:
  - Snippet 1 (score: 0.710)
    > In particular, the knockout of Gal3 normalized 348 DEG genes between Tau22/Lgals3 +/+ and WT mice (Figure 6, A and B and Supplemental Table 7). Further GO enrichment analysis revealed that the upregulated DEGs of Tau22/Lgals3 +/+ versus WT mice were enriched in multiple processes, including metabolic processes, oxidative reduction processes, and immune system processes (Figure 6, C and D). Importantly, the downregulated DEGs by Lgals3 deletion within the context of Tau22 were primarily enriched in immune responses and the production of cytokines and chemokines (Figure 6E). Conversely, the downregulated DEGs in Tau22/Lgals3 -/-versus Tau22/Lgals3 +/+ mice were enriched in processes including nervous system development, protein phosphorylation, synapse assembly, and learning (Supplemental Figure 21, E and F). No specific enriched processes were identified for the upregulated DEGs in Tau22/Lgals3 -/- versus Tau22/Lgals3 +/+ mice. These findings are consistent with what were observed in human iMGLs, confirming that Gal3 plays a principal role in governing the microglia-mediated immune response in tauopathy.
    > We next categorized these DEGs by their enriched cell type based on the Tabula Muris Consortium database (39) (Supplemental Figure 21D), and, as predicted, we found that the largest population of DEGs identified between Tau22/Lgals3 -/-and Tau22/Lgals3 +/+ mice was enriched in microglia (21.3%; Supple-cells (Figure 8). When encountering pathological tau, microglia become active and release Gal3 into the extracellular space either directly or via EVs (Figure 3O). Under the tested conditions, we found that Gal3 directly facilitated the aggregation of pTau into β-pleated-sheet structures (Figure 3L). This interaction between pTau and Gal3 may occur in EVs and/or the extracellular space between microglia and neurons.

### [11] Enhanced cortical bone expansion in Lgals3-deficient mice during aging
- Authors: Kevin A. Maupin, Kevin Weaver, Alexis Bergsma, Cheryl Christie, Z. Zhong et al.
- Year: 2018
- Venue: Bone Research
- URL: https://www.semanticscholar.org/paper/186b9fa98d1dd1342931f3b02765fa78aecd0100
- DOI: 10.1038/s41413-017-0003-6
- PMID: 30886760
- PMCID: 6416267
- Citations: 15
- Summary: Investigation of bone cells showed the increase was probably due to increased bone formation, rather than decreased bone resorption, and the researchers conclude that disrupting galectin-3 may help to prevent aging-related bone loss.
- Evidence snippets:
  - Snippet 1 (score: 0.706)
    > Mice from this cross were then crossed to mice homozygous for the Crerecombinase transgene under control of the CMV enhancer [BALB/ c-Tg(CMV-cre)1Cgn/J] to remove exon 4 which was flanked with loxP sites. These mice were then crossed to a wild-type C57BL/6J mouse to remove the Cre transgene to obtain Lgals3 Δ/+ heterozygous mice. These heterozygotes were set up into breeding pairs to generate litters containing wild type (Lgals3 +/ + ), heterozygous (Lgals3 Δ/+ ) and homozygous mutant (Lgals3 Δ/Δ ) offspring.
    > We verified loss of galectin-3 protein in these mice by western blot of lung lysates using a Mac-2/galectin-3 rat monoclonal antibody 59 (gift from John Wang, MSU, E. Lansing, MI) which recognizes an that is N-terminal of the region encoded by exon 4. 60 No protein product corresponding to full-length or truncated galectin-3 was detected from lung lysates of Lgals3 Δ/Δ mice. The additional benefits of using Lgals3 Δ/Δ mice is that they avoid potential transcriptional effects on neighboring genes by a neomycin resistance cassette 61 ; also, the genomic deletion is downstream from the galectin-3 internal gene, Galig, which utilizes a promoter in intron 2 and encodes a small protein via an alternative open reading frame of exon 3 of Lgals3. 62,63 Figure 2 shows the null alleles utilized in this study. Genomic DNA was isolated from tail clips at weaning and necropsy by proteinase K digestion and ethanol precipitation. Genotypes were assigned by allele specific PCR.

### [12] SREBP1 regulates Lgals3 activation in response to cholesterol loading
- Authors: Jing Li, Hongtao Shen, G. Owens, Lian‐Wang Guo
- Year: 2022
- Venue: Molecular Therapy. Nucleic Acids
- URL: https://www.semanticscholar.org/paper/6c55d666855233ff0e7035d46075997924da854c
- DOI: 10.1016/j.omtn.2022.05.028
- PMID: 35694209
- PMCID: 9168384
- Citations: 13
- Summary: Results identify a previously uncharacterized cholesterol-responsive dyad—SREBP1 and LGALS3, constituting a feedforward circuit that can be blocked by BETs inhibition in SMC phenotypic transition and potential interventional targets.
- Evidence snippets:
  - Snippet 1 (score: 0.706)
    > Beyond this knowledge, our data contributed new information showing that LGALS3 decreased expression of MRTF-A protein, a well-established transcription co-activator of SMC contractile genes. Collectively, our results and existing reports suggest that rather than merely a cell-type marker, LGALS3 is a key effector that promotes cholesterol-induced SMC phenotypic states, including migration, inflammation, dedifferentiation, lipid storage, and resistance to apoptosis (Figure S3). Moreover, we identified it as an atypical target gene of both SREBP1 and KLF15. In addition, we observed that LGALS3 promotes SREBP1 expression but represses KLF15 production. Our coIP experiments did not show an obvious LGALS3/ SREBP1 physical association, although it has been reported that
    > LGALS3 participates in nuclear function, such as forming an early splicing machinery. 29 However, it will be important that future studies determine how LGALS3 regulates SREBP1 and KLF15 expression.
    > In view of the SREBP1/LGALS3/SREBP1 feedforward circuit identified herein, and previous evidence that SMCs with activated Lgals3 preferentially give rise to atherosclerotic lesion cells, 4 it is interesting to consider LGALS3 as a potential interventional target for breaking this vicious cycle. However, the effectiveness of using an
    > 6][47] In contrast, BETs inhibition with JQ1 abrogated cholesterol-induced increases of
    > LGALS3 and SREBP1 protein levels, in rodent SMCs and also in human primary SMCs. This potent effect implicates an alternative strategy to inhibit this SREBP1/LGALS3 pathway. BETs inhibitors have shown anti-atherogenic efficacy in preclinical models. 35,40 In a phase II clinical trial, the pan-BETs inhibitor RVX208, which is known to increase apolipoprotein A-I, 48 has exhibited a favorable profile of safety and efficacy in amelioration of major adverse cardiovascular events. 49

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.