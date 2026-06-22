---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:45:46.643162'
end_time: '2026-06-22T04:45:50.124782'
duration_seconds: 3.48
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0048030
  hypothesis_text: LGALS3 has disaccharide binding (GO:0048030).
  term_context: '- Term: disaccharide binding (GO:0048030)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[2]
  source_context_yaml: "term:\n  id: GO:0048030\n  label: disaccharide binding\nevidence_type:\
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
citation_count: 15
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has disaccharide binding (GO:0048030).

Gene/protein: LGALS3. Organism: Homo sapiens (NCBITaxon:9606).
Claim to support or refute with independent experimental literature: LGALS3 has disaccharide binding (GO:0048030).
Key context:
- Term: disaccharide binding (GO:0048030)
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
- **Hypothesis slug:** function-support-go-0048030
- **Source file:** genes/human/LGALS3/LGALS3-ai-review.yaml
- **Source selector:** existing_annotations[2]

## Reference Context

- GO_REF:0000033

## Source Context YAML

```yaml
term:
  id: GO:0048030
  label: disaccharide binding
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

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has disaccharide binding (GO:0048030). Gene/protein: LGALS3. Or...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 15
- Snippets retrieved: 20

## Relevant Papers

### [1] Clusterin Seals the Ocular Surface Barrier in Mouse Dry Eye
- Authors: Aditi Bauskar, W. Mack, J. Mauris, P. Argüeso, M. Heur et al.
- Year: 2015
- Venue: PLoS ONE
- URL: https://www.semanticscholar.org/paper/ddc53237e6b4b7c325cb047e4eaf34098273148e
- DOI: 10.1371/journal.pone.0138958
- PMID: 26402857
- PMCID: 4581869
- Citations: 35
- Influential citations: 2
- Summary: It is shown that CLU prevents and ameliorates ocular surface barrier disruption by a remarkable sealing mechanism dependent on attainment of a critical all-or-none concentration, and suggests CLU as a biotherapeutic for dry eye.
- Evidence snippets:
  - Snippet 1 (score: 0.933)
    > In other cases, CLU spots were clearly separate.
    > Next we considered what kinds of ocular surface molecules might bind CLU.
    > LGALS3, a key component of the ocular surface barrier, is a member of the galectin class of beta-galactosidebinding proteins. What is known about the glycosyl moiety of CLU is consistent with LGALS3 binding [25,27]. CLU applied to an LGALS3-sepharose affinity column bound to the beads and was not eluted 0.1 M sucrose, a disaccharide that does not compete with LGALS3 sugar binding, but was mostly eluted with a competitive inhibitor of LGALS3 sugar binding, 0.1 M beta-lactose (Fig 5C). This suggests that CLU binding to LGALS3 is specific for the beta-galactoside-binding function.

### [2] Beyond Colonoscopy: Exploring New Cell Surface Biomarkers for Detection of Early, Heterogenous Colorectal Lesions
- Authors: Saleh M. Ramezani, Arianna Parkhideh, P. Bhattacharya, M. Farach-Carson, D. Harrington
- Year: 2021
- Venue: Frontiers in Oncology
- URL: https://www.semanticscholar.org/paper/4b48091d0ad86a2121491218707db23e88605000
- DOI: 10.3389/fonc.2021.657701
- PMID: 34290978
- PMCID: 8287259
- Citations: 13
- Summary: This review contextualizes existing and emergent CRC surface biomarkers and assess each’s potential as a candidate marker for early marker-based detection of CRC lesions and presents an overview of recent advances in imaging techniques useful for visual detection of surface biomarker detection.
- Evidence snippets:
  - Snippet 1 (score: 0.812)
    > Galectin 3, or LGALS3, is a member of the galectin family, a group of carbohydrate-binding lectins characterized by their binding affinity for beta-galactosides (85).
    > LGALS3 is expressed at the cell surface, where it interacts with the extracellular matrix, especially with glycoproteins, and has the ability to affect intracellular signaling pathways (42). LGALS3-expressing cells also possess higher ALDH1 activity, which often correlates with a dedifferentiated cancer stem cell phenotype, than do their LGALS3-negative counterparts (86).
    > The correlation of LGALS3 expression in CRC with clinical pathological characteristics has been explored in several immunohistochemical and RT-PCR studies. In one study, the IHC staining of CRC tissue (n=61) and normal adjacent tissue (n=23) samples showed significantly higher LGALS3 expression in cancer tissue (62.5%) versus normal cancer-adjacent tissue (13.0%) (41). In another study, 75% of CRC tissue samples stain high for LGALS3, and ten CRC cell lines were shown to have increased LGALS3 protein levels compared to HeLa cells (42).
    > LGALS3 expression varies according to cancer staging and the degree of differentiation of the adenocarcinoma. LGALS3 mRNA levels were higher in early stage colorectal cancers (58% in stage I) compared to advanced cancers (50% in stage IV) (43). Protein analysis found higher LGALS3 levels in primary adenocarcinomas than in metastatic adenocarcinomas, and stronger LGALS3 staining in well-differentiated tumor areas compared to poorly differentiated tumor areas (43). Conversely, colorectal adenocarcinomas may display higher levels of LGALS3 than do colorectal adenomas; one study sets the rate of colorectal adenocarcinoma expression of LGALS3 at 95% while only 73% of adenomas were positive for LGALS3 (43).

### [3] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
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
  - Snippet 1 (score: 0.809)
    > In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3. The interaction between periplocin and LGALS3 was further confirmed by drug affinity responsive target stability (DARTS) analysis, as evidenced by a more stable property of LGALS3 protein against pronase digestion in response to periplocin treatment (Figure 6L,M). Moreover, using semiflexible docking analysis, we found that LGALS3 showed a good binding activity for periplocin, with a binding energy of −6.689 kcal/mol. Glu165, Arg162, Gly152, Gln150, Arg144, and Asn143 of LGALS3 were identified as possible sites for periplocin binding (Figure 6N,O), which required further experimental investigation. Together, these data suggest that periplocin binds and prevents ubiquitin-mediated degradation of LGALS3 in CRC cells.
  - Snippet 2 (score: 0.753)
    > Scale bar: 10 μm. (I) Immunofluorescent analysis of the colocalization of LGALS3 with ubiquitin in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm. (J) Representative fluorescent images of CRC cells transiently expressing Mrfp-GFP-tandem fluorescent-tagged LGALS3 (tfGal3) followed by 0.50 μM periplocin treatment for 24 h. Scale bar: 10 μm. (K) Quantitative analysis of the GFP + RFP + or GFP − RFP + LGALS3 puncta in (J). (L) the relative decreased ratio of Magic Red intensity, relative increased ratio of LysoSensor Blue intensity, relative increased ratio of the interaction between LGALS3 and TRIM16, and relative increased ratio of LC3B-II protein level in DLD-1 cells following 0.50 μM periplocin treatment at different time periods. Results are representative of three independent experiments. Data are presented as mean ± SD. *P < 0.05, **P < 0.01, ***P < 0.001. for LGALS3 degradation, we generated lysine to arginine mutants of LGALS3 at K196 or Lys210 (LGALS3 K196R or LGALS3 K210R ). As shown in Figure 6I, the ubiquitinconjugated level of LGALS3 K196R mutant was comparable to the wild type (WT), whereas K210 mutation significantly decreased LGALS3 ubiquitination. These results suggest that periplocin elevates LGALS3 level by preventing K210 ubiquitination and proteasomal degradation. In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3.

### [4] Impairment of lysosomal quality control in Huntington disease
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
  - Snippet 1 (score: 0.791)
    > In HD, high levels of LGALS3 have been found in plasma and brain of patients and mice. LGALS3 upregulation was observed in HD mice before the motor symptoms, in the microglia LGALS3 was found associated to damaged lysosomes and its suppression in microglia ameliorated the HD mice phenotype [36].
    > LGALS3 is emerging as a key factor for NDs for its intracellular role in lysosomal damage, but also for its functions linked to its secretion in the extracellular space. Many pieces of evidence suggest its detrimental role in neurodegeneration, even if a protective role of LGALS3 has been reported (reviewed in ref. [75]). LGALS3 mechanisms of action need further investigation but its pharmacological modulation might represent a valuable target for intervention for NDs. LGALS3 inhibitors have already been tested in metabolic and fibrotic diseases, and these approaches might be applied to NDs. 3′-bis-(4aryltriazol-1-yl) thiodigalactoside (GB039, formerly named TD139), a synthetic small molecule that antagonizes LGALS3 activity by binding to the carbohydrate recognition domain, was effective in idiopathic pulmonary fibrosis and retinal degeneration [76,77]. Pectins, plant cell wall polysaccharides, mostly obtained from citrus and apples, represent natural LGALS3 inhibitors [78,79].
    > In summary, our experiments suggest that LQC impairment might contribute to HD. Indeed, the LGALS3 accumulation observed in HD cellular models due to TFEB and TFE3 sequestration by muHTT inclusions causes LMP and lysophagy impairment, in turn, influences LQC.
    > Fig. 8 TFEB and TFE3 sequestration affects the LQC. A, B NSC-34 cells were transfected with wt or muHTT.

### [5] Mutation of the galectin‐3 glycan‐binding domain ( Lgals3‐R200S) enhances cortical bone expansion in male mice and trabecular bone mass in female mice
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
  - Snippet 1 (score: 0.791)
    > We previously observed that genomic loss of galectin-3 (Gal-3; encoded by Lgals3) in mice has a significant protective effect on age-related bone loss. Gal-3 has both intracellular and extracellular functionality, and we wanted to assess whether the affect we observed in the Lgals3 knockout (KO) mice could be attributed to the ability of Gal-3 to bind glycoproteins. Mutation of a highly conserved arginine to a serine in human Gal-3 (LGALS3-R186S) blocks glycan binding and secretion. We generated mice with the equivalent mutation (Lgals3-R200S) and observed a subsequent reduction in Gal-3 secretion from mouse embryonic fibroblasts and in circulating blood. When examining bone structure in aged mice, we noticed some similarities to the Lgals3-KO mice and some differences. First, we observed greater bone mass in Lgals3-R200S mutant mice, as was previously observed in Lgals3-KO mice. Like Lgals3-KO mice, significantly increased trabecular bone mass was only observed in female Lgals3-R200S mice. These results suggest that the greater bone mass observed is driven by the loss of extracellular Gal-3 functionality. However, the results from our cortical bone expansion data showed a sex-dependent difference, with only male Lgals3-KO mice having an increased response, contrasting with our earlier study. These notable sex differences suggest a potential role for sex hormones, most likely androgen signaling, being involved. In summary, our results suggest that targeting extracellular Gal-3 function may be a suitable treatment for age-related loss of bone mass.
    > Galectin-3 (Gal-3; encoded by Lgals3) is a protein that functions outside the cell to regulate glycoprotein secretion and turnover [1,2] and intracellularly in protein chaperoning and mRNA splicing [3,4]. We previously found that genomic deletion of Gal-3 in mice (Lgals3-KO) protects the mice against age-related [5] or sex-hormone deprivation bone loss [6]. A better understanding of the
  - Snippet 2 (score: 0.785)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.
  - Snippet 3 (score: 0.750)
    > In this study, we generated the Lgals3-R200S allele using CRISPR/Cas9 and a single-stranded DNA oligonucleotide as a template for homologous recombination. Mutation of the cognate arginine to serine in human Gal-3 (R186S) prevents Gal-3 secretion and glycan-binding [30,31,40]. Because mutation of the functionally equivalent arginine in galectin-7 also prevents glycan-binding [32,33], the R200S mutation in Gal-3 should be functionally equivalent. As confirmation, our surface biotinylation experiment demonstrated a dose-dependent reduction in surface Gal-3 in heterozygous and homozygous Lgals3-R200S mice. In our aged mouse bone studies, we observed a sexdependent increase in trabecular bone mass in female Lgals3-R200S mice. Yet only male Lgals3-R200S had significant increase in cortical bone expansion. The increased cortical bone expansion was coupled with reduced tissue quality (reduced max stress), and no change in tissue or whole bone stiffness values.
    > Similar to the findings presented here, we previously observed that female mice with genomic loss of Gal-3 (Lgals3-KO mice) had significant protection against age-related trabecular bone loss between 24 and 36 weeks of age [5]. But Lgals3-KO mice also had increased cortical bone expansion, whereas only male Lgals3-R200S did in this study. The effect size of the increases in cortical bone size was greater in Lgals3-KO females than males [5]. The similarities between Lgals3-R200S and Lgals3-KO mice (i.e., increased trabecular bone mass in female mice and increased cortical bone expansion in males) likely reflect the role of extracellular Gal-3 loss in increasing bone mass. Conversely, the differences between the two models (tissue stiffness and lack of female cortical bone expansion) could reflect the role of intracellular Gal-3.
    > The female dominance of the cortical bone expansion in

### [6] Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy
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
  - Snippet 1 (score: 0.780)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [7] SMURF1 controls the PPP3/calcineurin complex and TFEB at a regulatory node for lysosomal biogenesis
- Authors: Qin Xia, Hanfei Zheng, Yang Li, Wanting Xu, Chengwei Wu et al.
- Year: 2023
- Venue: Autophagy
- URL: https://www.semanticscholar.org/paper/7ab13fe72fa12a55aa9304ce52199d1494c8974a
- DOI: 10.1080/15548627.2023.2267413
- PMID: 37909662
- PMCID: 11062382
- Citations: 20
- Summary: This study showed that SMURF1 affected lysosomal biogenesis in response to lysosomal damage by preventing TFEB nuclear translocation, and determined that LLOMe-mediated TFEB nuclear import is dependent on SMURF1 under the condition of MTORC1 inhibition.
- Evidence snippets:
  - Snippet 1 (score: 0.758)
    > Immunofluorescence assay showed that PPP3R1 was also recruited to lysosomes upon LLOMe treatment in a LGALS3-dependent manner (Figure S4A).To identify the role of PPP3R1 in the formation of complex, as expected, we first found that PPP3CB directly binds with PPP3R1 in a LLOMe-enhanced manner (Figure 6A, B).Considering that PPP3CB was directly associated with LGALS3, we also checked the interaction between PPP3R1 and LGALS3.The results showed that PPP3R1 indirectly binds with LGALS3 (Figure 6C).Similarly, LLOMe treatment also promoted the binding affinity between PPP3R1 and LGALS3 (Figure 6D).We next mapped the key interaction domain of LGALS3 with PPP3R1, and showed the NT domain of LGALS3 was essential for the association with PPP3R1 (Figure 6E, F).Furthermore, overexpression of PPP3CB increased, suppression of PPP3CB abolished, the interactions of PPP3R1 and LGALS3 (Figure 6G, H), suggesting PPP3CB is also the bridge for the interaction between LGALS3 and PPP3R1.Interestingly, we also detected that SMURF1 indirectly interacted with PPP3R1, but not MCOLN1, in a LLOMe-enhanced manner (Figure S4B-E).Given that both SMURF1 and PPP3R1 were indirectly bound with the NT domain of LGALS3, we asked whether SMURF1 affected the interactions between PPP3R1 and LGALS3.Our data indicated that suppression of SMURF1 decreased, overexpression of SMURF1 increased, the interactions of PPP3R1 and LGALS3 (Figure 6I, J), suggesting SMURF1 promotes the recruitment of PPP3R1 by LGALS3.We next mapped the key HECT domain of SMURF1 which was essential for interaction with PPP3R1 (Figure 6K, L).
  - Snippet 2 (score: 0.748)
    > Consistently,
    > LGALS3 and PPP3R1 were required for binding of PPP3CB and TFEB evidenced by knocking down LGALS3 or PPP3R1 decreased, while overexpression of LGALS3 or PPP3R1 increased, the interaction of PPP3CB and TFEB (Figure 8K, L).Of note, we found that the enhanced PPP3CB and TFEB interaction mediated by SMURF1 overexpression was abolished by LGALS3 deletion (Figure 8M).Overall, these data strengthened our hypothesis that LGALS3 and SMURF1 contribute to PPP3CB from "close" to "open" form, which facilitates TFEB docking to the AID domain (Figure 8N).

### [8] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
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
  - Snippet 1 (score: 0.750)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.

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
  - Snippet 1 (score: 0.747)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.
  - Snippet 2 (score: 0.747)
    > However, CD44 is present and interestingly is most elevated in patients with active LGALS3 network and CD74 network (Fig. 8). LGALS3 has been shown to be critical for CD44 endocytosis so LGALS3 would be expected to promote CD44 surface expression [54]. In AML cells with LGALS3 supported CD44 surface expression, CD74 would be predicted to augment signaling mediated by CD44.
    > LGALS3 is well known as an immune regulatory molecule that suppresses host anti-tumor immune surveillance by diverse mechanisms [1,2,55].
    > LGALS3 blocks or at least dampens immune cell function by reducing surface expression of glycosylated T cell receptor in T cells and preventing NK cell receptor binding to antigen [1,2]. LGALS3 has emerged as a critical component in MSC in AML patients to impact response to therapy [56]. It is likely that LGALS3 secreted from MSC and other support cells in the AML microenvironment negatively impacts immune surveillance in AML patients. It is yet to be determined if LGALS3 derived from the leukemia cells plays a role as an immune response inhibitor in AML.
    > LGALS9 is emerging as an important immune checkpoint inhibitor molecule as a TIM-3 binding partner [2,57]. LGALS9 also regulates T cell function as a CD44 binding partner [58]. Whereas LGALS3 binding to CD44 promotes metastasis, LGALS9 binding to CD44 suppresses this process [59,60]. Future RPPA studies to determine the role of LGALS9 and galectins other than LGALS3 are warranted.
    > For the first time, an at risk AML population has been found that is associated with active LGALS3 and active CD74 networks (Fig. 9A and  B). At present, it is unclear which if any proteins within the LGALS3 or CD74 networks is driving this phenomenon. CD44, SPP1, and CLPP are highly induced in the patient cohort with both networks active compared to patients with normal-like state (Fig. 8).

### [10] In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression
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
  - Snippet 1 (score: 0.747)
    > Finally, since LGALS3 (Galectin-3) has been shown to interact with O-glycans in the mucosal epithelium [30], and considering its overexpression observed by proteomics and further confirmed by PCR and WB analyses upon depletion of C1GALT1, we focused on the role of LGALS3 in EC by IHC.
    > A total of 151 out of 178 cores from 79 EC patients were considered adequate for LGALS3 expression assessment by IHC. Morphologic assessment of LGALS3 IHC staining characteristics revealed different staining patterns (Fig. 5 A). Out of the 151 evaluable cores, 45 (29.8%) showed absent LGALS3 expression. LGALS3 positive samples showed variable and low intensity protein expression (mean positive tumor cells per sample = 35.4%). A small subset of cores (13/151, 8.6%) demonstrated diffuse (> 90% positive tumor cells per sample) staining. LGALS3 score varied across histologic types, with serous and undifferentiated tumors displaying the highest protein expression (median IHC LGALS3 score = 10, 20, 50 and 55 for endometrioid, clear cell, serous and undifferentiated tumor types, respectively) (Fig. 5B). Interestingly, the aggressive histologic variants (clear cell, serous and undifferentiated) showed higher LGALS3 IHC scores than endometrioid variants (p value < 0.001). In addition, LGALS3 expression positively correlated with tumor grade. High grade tumors (G3) displayed higher protein expression (median LGALS3 IHC score = 30) compared to low grade tumors (median LGALS3 IHC score for G1/G2 tumors = 10). This finding was independent of histologic type, as similar results were observed when analyzing endometrioid tumors.
    > Finally, we interrogated the correlation between the expression levels of LGALS3 and C1GALT1.

### [11] Phenotypic Switching of Vascular Smooth Muscle Cells in Atherosclerosis
- Authors: Runji Chen, D. McVey, D. Shen, Xiaoxin Huang, Shu Ye
- Year: 2023
- Venue: Journal of the American Heart Association: Cardiovascular and Cerebrovascular Disease
- URL: https://www.semanticscholar.org/paper/472c313e2214a97757712ab0a8b39b133bd6a6bc
- DOI: 10.1161/JAHA.123.031121
- PMID: 37815057
- PMCID: 10757534
- Citations: 133
- Influential citations: 2
- Summary: This review article discusses the 9 VSMC phenotypes that have been reported in atherosclerotic lesions and classifies them into differentiated VSMCs, intermediately dedifferentiated VSMCs, and dedifferentiated VSMCs.
- Evidence snippets:
  - Snippet 1 (score: 0.744)
    > Lgals3 (also referred to as galectin-3) is considered a marker of macrophage-like cells. 13,31 Rong et al detected a population of VSMCs that expressed Lgals3 following cholesterol loading in vitro. 31 Recently, Alencar et al found that Lgals3 activation is not a specific marker of the differentiation of VSMCs to a macrophage-like state but rather it is a marker of VSMCs entering a transitional state, with increased expression of genes associated with stem cells that are capable of extracellular matrix remodeling. 16 Of note, similar to SEM-like cells, Lgals3 + cells also have increased expression of lymphocyte antigen 6 family member A and vascular cell adhesion molecule 1. Further studies to investigate if SEM-like cells are derived from Lgals3 + cells are warranted.
    > Using mouse, rat, and human models of cholesterolloading in VSMCs, Li et al found that SREBP1 (sterol regulatory-element binding protein-1) and Krüppel-like factor-15 induced up-and downregulation of Lgals3, respectively, via binding to the Lgals3 gene promoter (albeit at different sites). 45 Likewise, Lgals3 promoted SREBP1 gene expression, producing a feedforward loop upregulated by cholesterol loading. 45 Moreover, Lgals3 and SREBP1 downregulated myocardin-related transcription factor A expression in VSMCs. 45 In another study, Owsiany et al used a dual lineage tracing model and found that Lgals3 + VSMCs produce monocyte chemoattractant protein 1, a proinflammatory chemokine. 15 Knockout of monocyte chemoattractant protein 1 specifically in Lgals3 + VSMCs resulted in the formation of atherosclerotic lesions with a greater ACTA2 content in the fibrous cap and decreased Lgals3 + cell content, a feature of stable plaque. 15

### [12] Morphological and transcriptional insights into the role of histone phosphorylation-related genes in early development of the chicken duodenum
- Authors: Xiaofeng Li, Bing Yang
- Year: 2025
- Venue: Animal Bioscience
- URL: https://www.semanticscholar.org/paper/b3da4d3a37ec0fae40140d0cf95db98d90b41079
- DOI: 10.5713/ab.25.0108
- PMID: 40506039
- PMCID: 12580959
- Citations: 1
- Summary: A novel paradigm wherein histone phosphorylation coordinates intestinal morphogenesis is established, providing mechanistic insights for optimizing poultry intestinal health and nutritional strategies.
- Evidence snippets:
  - Snippet 1 (score: 0.738)
    > LGALS3 Galectin 3
    > LGALS3 encodes a member of the galectin family of carbohydrate binding proteins which play an important role in numerous cellular functions including apoptosis, innate immunity, cell adhesion and T-cell regulation. The protein exhibits antimicrobial activity against bacteria and fungi.

### [13] Lysosomal damage is a therapeutic target in Duchenne muscular dystrophy
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
  - Snippet 1 (score: 0.738)
    > To investigate whether cholesterol accumulation in dystrophic muscle is associated with the impaired lysosomal function, we sought a method to quantify lysosomal damage. Several studies have recently focused on lysosomal dysfunction, in which LMP plays a central role (18). However, very few studies have investigated lysosome damage in muscle. One identified marker of LMP is Gal-3 (or LGALS3), which is part of the galectins, a family of lectins that bind specifically to carbohydrates (19). These lectins are present in the cytosol, nucleus, and extracellular matrix and are translocated to the membrane of damaged lysosomes before their removal by the autophagy machinery (20). To analyze LGALS3 expression in a myogenic environment and its capacity to detect LMP, we differentiated healthy human immortalized myoblasts into elongated myotubes for 7 days and then performed immunostaining for LGALS3 and lysosome-associated membrane protein 2 (LAMP2), which is commonly used as a lysosome marker (21). A diffuse expression of LGALS3 was observed in the cells (fig. S1A). Treatment with l-leucyl-l-leucine methyl ester (LLOMe), a lysomotropic agent that induces lysosome-specific membrane damage (22), for 30 min at 2.5 mM triggered the formation of LGALS3-positive puncta, which colocalized with LAMP2, indicating typical damaged lysosomes. An up-regulation of LGALS3 was also detected by Western blotting after 30 min to 1 hour of LLOMe treatment (fig. S1, B and C). LGALS3 puncta were markedly reduced 3 hours after treatment, and LGALS3 expression was restored to the control level, demonstrating efficient lysosomal repair by the cells. This pattern correlated inversely with the amount of LGALS3 released in the media, detected by an enzyme-linked immunosorbent assay (ELISA) assay (fig.

### [14] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
- Authors: Tammy R. Chaudoin, S. Bonasera
- Year: 2018
- Venue: BMC Neuroscience
- URL: https://www.semanticscholar.org/paper/613a09b176431cdca195e6b3c439b4edbe4f92af
- DOI: 10.1186/s12868-018-0428-x
- Summary: P perturbation of behavioral circadian rhythms in Lgals3−/− mice is noted, with mice at both ages demonstrating greater variability in day-to-day performance of feeding, drinking, and movement compared to wildtype.
- Evidence snippets:
  - Snippet 1 (score: 0.736)
    > Galectins are an evolutionarily ancient family of proteins sharing a high binding affinity for carbohydrates with β-galactoside linkages. In the extracellular space, galectins interact (through a conserved carbohydrate recognition domain, aka CRD) with glycosylated proteins to mediate both cell-to-cell interactions and cell-to-matrix adhesion. Galectins are thus pattern recognition molecules specialized to distinguish carbohydrate moieties.
    > Within the galectin family, galectin-3 (also known as Lgals3) has unique properties. Its preferred ligand is N-acetyllactosamine [1]. It is also the only galectin containing a conserved N-domain as well as a single CRD domain. This N-domain allows Lgals3 not bound to a carbohydrate target to form multimeric complexes [2].
    > In this manner, low extracellular Lgals3 concentrations tend to inhibit extracellular interactions and adhesion [3], while high Lgals3 extracellular concentrations facilitate cellular adhesion [4,5]. Lgals3 affinity for ECM substrates is also modulated by phosphorylation at its Ser6 residue [6].
    > Lgals3 is an NFκB target gene [7]; Lgals3 protein is widely distributed throughout most tissue sites (as demonstrated by the TiGER Tissue specific gene expression and regulation database; [8]). Furthermore, within specific tissues, Lgals3 protein expression is widespread, with extracellular [9], membrane bound, cytoplasmic, and nuclear localizations (for review, see [10]).

### [15] Mice lacking galectin-3 (Lgals3) function have decreased home cage movement
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
  - Snippet 1 (score: 0.733)
    > Galectins are an evolutionarily ancient family of proteins sharing a high binding affinity for carbohydrates with β-galactoside linkages. In the extracellular space, galectins interact (through a conserved carbohydrate recognition domain, aka CRD) with glycosylated proteins to mediate both cell-to-cell interactions and cell-to-matrix adhesion. Galectins are thus pattern recognition molecules specialized to distinguish carbohydrate moieties.
    > Within the galectin family, galectin-3 (also known as Lgals3) has unique properties. Its preferred ligand is N-acetyllactosamine [1]. It is also the only galectin containing a conserved N-domain as well as a single CRD domain. This N-domain allows Lgals3 not bound to a carbohydrate target to form multimeric complexes [2].
    > In this manner, low extracellular Lgals3 concentrations tend to inhibit extracellular interactions and adhesion [3], while high Lgals3 extracellular concentrations facilitate cellular adhesion [4,5]. Lgals3 affinity for ECM substrates is also modulated by phosphorylation at its Ser6 residue [6].
    > Lgals3 is an NFκB target gene [7]; Lgals3 protein is widely distributed throughout most tissue sites (as demonstrated by the TiGER Tissue specific gene expression and regulation database; [8]). Furthermore, within specific tissues, Lgals3 protein expression is widespread, with extracellular [9], membrane bound, cytoplasmic, and nuclear localizations (for review, see [10]).

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.