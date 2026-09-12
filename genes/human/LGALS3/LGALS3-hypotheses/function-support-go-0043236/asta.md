---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:46:50.712680'
end_time: '2026-06-22T04:46:53.636967'
duration_seconds: 2.92
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0043236
  hypothesis_text: LGALS3 has laminin binding (GO:0043236).
  term_context: '- Term: laminin binding (GO:0043236)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[10]
  source_context_yaml: "term:\n  id: GO:0043236\n  label: laminin binding\nevidence_type:\
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
citation_count: 13
---

## Question

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has laminin binding (GO:0043236).

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


## Output

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has laminin binding (GO:0043236). Gene/protein: LGALS3. Organis...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 13
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
  - Snippet 1 (score: 0.841)
    > Scale bar: 10 μm. (I) Immunofluorescent analysis of the colocalization of LGALS3 with ubiquitin in CRC cells treated with or without 0.50 μM periplocin for 24 h. Scale bar: 10 μm. (J) Representative fluorescent images of CRC cells transiently expressing Mrfp-GFP-tandem fluorescent-tagged LGALS3 (tfGal3) followed by 0.50 μM periplocin treatment for 24 h. Scale bar: 10 μm. (K) Quantitative analysis of the GFP + RFP + or GFP − RFP + LGALS3 puncta in (J). (L) the relative decreased ratio of Magic Red intensity, relative increased ratio of LysoSensor Blue intensity, relative increased ratio of the interaction between LGALS3 and TRIM16, and relative increased ratio of LC3B-II protein level in DLD-1 cells following 0.50 μM periplocin treatment at different time periods. Results are representative of three independent experiments. Data are presented as mean ± SD. *P < 0.05, **P < 0.01, ***P < 0.001. for LGALS3 degradation, we generated lysine to arginine mutants of LGALS3 at K196 or Lys210 (LGALS3 K196R or LGALS3 K210R ). As shown in Figure 6I, the ubiquitinconjugated level of LGALS3 K196R mutant was comparable to the wild type (WT), whereas K210 mutation significantly decreased LGALS3 ubiquitination. These results suggest that periplocin elevates LGALS3 level by preventing K210 ubiquitination and proteasomal degradation. In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3.
  - Snippet 2 (score: 0.834)
    > In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3. The interaction between periplocin and LGALS3 was further confirmed by drug affinity responsive target stability (DARTS) analysis, as evidenced by a more stable property of LGALS3 protein against pronase digestion in response to periplocin treatment (Figure 6L,M). Moreover, using semiflexible docking analysis, we found that LGALS3 showed a good binding activity for periplocin, with a binding energy of −6.689 kcal/mol. Glu165, Arg162, Gly152, Gln150, Arg144, and Asn143 of LGALS3 were identified as possible sites for periplocin binding (Figure 6N,O), which required further experimental investigation. Together, these data suggest that periplocin binds and prevents ubiquitin-mediated degradation of LGALS3 in CRC cells.

### [2] Identification of an Internal Gene to the Human Galectin-3 Gene with Two Different Overlapping Reading Frames That Do Not Encode Galectin-3*
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
  - Snippet 1 (score: 0.798)
    > Human Rapid-Scan Gene Expression Panel was used to detect the alternative transcripts in various human tissues using RT-PCR. The primers used were designed to amplify a 923-or 629-bp fragment.
    > LGALS3 transcripts were detected as a 457-bp DNA and actin transcripts as a 640-bp DNA. PCR was performed using 0.25 ng or 2.5 ng (10ϫ) template cDNA.
    > average of other human proteins is 10 times lower. This rich content in tryptophans confers hydrophobic properties that may account for the membrane localization of the ORF2⅐EGFP protein (Fig. 6). Consistent with the mitochondrial localization of the ORF2⅐EGFP fusion protein, this sequence exhibits the common properties of mitochondrial-imported proteins such as the enrichment of arginine, leucine, and serine residues (36).
    > Tissue Specificity of galig Expression-Detection of galig transcripts in HOS cells and colon tumor cells revealed a low expression level. Based on this observation, the rationale that the appearance of galig transcripts may have resulted from a leaky transcription of a cryptic promoter rather than from an independently functioning promoter could not be excluded. Screening of several human tissues indicated clearly that galig is a tightly regulated gene whose expression is most efficient in leukocytes from peripheral blood. The low level of transcription in bone marrow indicates that galig is specifically expressed in mature forms of leukocytes. Whereas the precise quantification of galig mRNA has not been addressed in these experiments, it is clear that these transcripts are much less abundant than LGALS3 transcripts. This may not be surprising considering that LGALS3 is known to be highly expressed when activated (37,38). Indeed, the amount of LGALS3 transcripts appeared as abundant as those from actin genes. This shows a different type of regulation by the galig and LGALS3 promoters. In particular, muscle, stomach, and uterus, although expressing low levels of galig transcripts, revealed no LGALS3 transcripts, thus indicating an independent functioning of the two promoters.

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
  - Snippet 1 (score: 0.792)
    > The study of galectin-3 is complicated by its ability to function both intracellularly and extracellularly. While the mechanism of galectin-3 secretion is unclear, studies have shown that the mutation of a highly conserved arginine to a serine in human galectin-3 (LGALS3-R186S) blocks glycan binding and secretion. To gain insight into the roles of extracellular and intracellular functions of galectin-3, we generated mice with the equivalent mutation (Lgals3-R200S) using CRISPR/Cas9-directed homologous recombination. Consistent with a reduction in galectin-3 secretion, we observed significantly reduced galectin-3 protein levels in the plasma of heterozygous and homozygous mutant mice. We observed a similar increased bone mass phenotype in Lgals3-R200S mutant mice at 36 weeks as we previously observed in Lgals3-KO mice with slight variation. Like Lgals3-KO mice, Lgals3-R200S females, but not males, had significantly increased trabecular bone mass. However, only male Lgals3-R200S mice showed increased cortical bone expansion, which we had previously observed in both male and female Lgals3-KO mice and only in female mice using a separate Lgals3 null allele (Lgals3). These results suggest that the trabecular bone phenotype of Lgals3-KO mice was driven primarily by loss of extracellular galectin-3. However, the cortical bone phenotype of Lgals3-KO mice may have also been influenced by loss of intracellular galectin-3. Future analyses of these mice will aid in identifying the cellular and molecular mechanisms that contribute to the Lgals3-deficient bone phenotype as well as aid in distinguishing the extracellular vs. intracellular roles of galectin-3 in various signaling pathways.
  - Snippet 2 (score: 0.770)
    > We previously observed that genomic loss of galectin-3 (Gal-3; encoded by Lgals3) in mice has a significant protective effect on age-related bone loss. Gal-3 has both intracellular and extracellular functionality, and we wanted to assess whether the affect we observed in the Lgals3 knockout (KO) mice could be attributed to the ability of Gal-3 to bind glycoproteins. Mutation of a highly conserved arginine to a serine in human Gal-3 (LGALS3-R186S) blocks glycan binding and secretion. We generated mice with the equivalent mutation (Lgals3-R200S) and observed a subsequent reduction in Gal-3 secretion from mouse embryonic fibroblasts and in circulating blood. When examining bone structure in aged mice, we noticed some similarities to the Lgals3-KO mice and some differences. First, we observed greater bone mass in Lgals3-R200S mutant mice, as was previously observed in Lgals3-KO mice. Like Lgals3-KO mice, significantly increased trabecular bone mass was only observed in female Lgals3-R200S mice. These results suggest that the greater bone mass observed is driven by the loss of extracellular Gal-3 functionality. However, the results from our cortical bone expansion data showed a sex-dependent difference, with only male Lgals3-KO mice having an increased response, contrasting with our earlier study. These notable sex differences suggest a potential role for sex hormones, most likely androgen signaling, being involved. In summary, our results suggest that targeting extracellular Gal-3 function may be a suitable treatment for age-related loss of bone mass.
    > Galectin-3 (Gal-3; encoded by Lgals3) is a protein that functions outside the cell to regulate glycoprotein secretion and turnover [1,2] and intracellularly in protein chaperoning and mRNA splicing [3,4]. We previously found that genomic deletion of Gal-3 in mice (Lgals3-KO) protects the mice against age-related [5] or sex-hormone deprivation bone loss [6]. A better understanding of the
  - Snippet 3 (score: 0.755)
    > s3 +/+ ), heterozygous (Lgals3-R200S KI/+ ), and homozygous (Lgals3-R200S KI/KI ) mutant mice (Fig. 1C). Consistent with a reduction in Gal-3 secretion, we observed significantly reduced Gal-3 protein levels in the plasma of adult heterozygous and homozygous mutant mice (Fig. 1D).
    > We generated mouse embryonic fibroblasts (MEFs) to look at cell-surface proteins, to confirm reduction of extracellular Gal-3 protein in Lgals3-R200S cells. Cell surface proteins were biotinylated and captured with NeutrAvidin Agarose. Western blot analysis showed cell surface Gal-3 levels were decreased in Lgals3-R200S KI/+ and Lgals3-R200S KI/KI cells compared to wild-type (Fig. 1E). The absence of the cytoplasmic protein, vinculin, from the pull-down lanes confirmed that the experiments worked to preferentially pull-down biotinylated cell surface proteins. Immunocytochemistry of MEFs from Lgals3-R200S KI/KI mice confirmed that Gal-3 is present in the cytosol and nucleus (Fig. 1F). Quantification of the mean and median amount of fluorescence per unit area indicated that Galectin-3 both on the cell surface and inside the cell was reduced, by approximately 30% and 26% respectively, in Lgals3-R200S KI/KI MEFs (P = 0.024). From these studies, we conclude that the R200S mutation in mice reduced cell surface Gal-3 and may have contributed to lower intracellular Gal-3 levels. Further studies will be necessary to determine if the 25-30% reduction in intracellular Gal-3 is biologically significant.

### [4] Regulation and use of the extracellular matrix by Trypanosoma cruzi during early infection
- Authors: P. Nde, M. Lima, Candice A. Johnson, S. Pratap, F. Villalta
- Year: 2012
- Venue: Frontiers in Immunology
- URL: https://www.semanticscholar.org/paper/0f8537bce448a98bc55bef38dcc8d4b462ab72b5
- DOI: 10.3389/fimmu.2012.00337
- PMID: 23133440
- PMCID: 3490126
- Citations: 43
- Influential citations: 2
- Summary: The first elucidation of the human ECM interactome network regulated by T. cruzi is presented, a ligand that mediates the attachment of trypanosomes to cells to initiate infection, up-regulates LAMC1 expression to enhance cellular infection.
- Evidence snippets:
  - Snippet 1 (score: 0.790)
    > The fact that LAMC1 is connected to LGALS3 through MYOC in the ECM interactome suggests the importance of LGALS3 in the manipulation of host ECM by T. cruzi.
    > Increased LGALS3 expression in the ECM promotes the adhesion of T. cruzi to host cells and subsequent infection (Kleshchenko et al., 2004). In addition, LGALS3 has numerous ECM interacting partners (Dumic et al., 2006), including collagen IV, hensin, laminins, fibronectin, vitronectin, tenascin, and elastin. LGALS3 regulates adhesion of these ECM proteins to a variety of host cells. Matrix metalloproteases, which are more active in T. cruzi infected mice, regulate LGAL3 function (Gutierrez et al., 2008). When metalloproteases are activated in the ECM, they can cleave LGALS3 and negatively regulate its function. Consequently, increased activation of MMP1 and MMP9 is associated with ECM destruction and myocarditis in T. cruzi infection.
    > Multiple types of collagen interact with the three central seed nodes, THBS1, LGALS3, and LAMC1. A glimpse of the importance of collagen in early T. cruzi infection was reported (Velge et al., 1988).

### [5] Beyond Colonoscopy: Exploring New Cell Surface Biomarkers for Detection of Early, Heterogenous Colorectal Lesions
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
  - Snippet 1 (score: 0.787)
    > Galectin 3, or LGALS3, is a member of the galectin family, a group of carbohydrate-binding lectins characterized by their binding affinity for beta-galactosides (85).
    > LGALS3 is expressed at the cell surface, where it interacts with the extracellular matrix, especially with glycoproteins, and has the ability to affect intracellular signaling pathways (42). LGALS3-expressing cells also possess higher ALDH1 activity, which often correlates with a dedifferentiated cancer stem cell phenotype, than do their LGALS3-negative counterparts (86).
    > The correlation of LGALS3 expression in CRC with clinical pathological characteristics has been explored in several immunohistochemical and RT-PCR studies. In one study, the IHC staining of CRC tissue (n=61) and normal adjacent tissue (n=23) samples showed significantly higher LGALS3 expression in cancer tissue (62.5%) versus normal cancer-adjacent tissue (13.0%) (41). In another study, 75% of CRC tissue samples stain high for LGALS3, and ten CRC cell lines were shown to have increased LGALS3 protein levels compared to HeLa cells (42).
    > LGALS3 expression varies according to cancer staging and the degree of differentiation of the adenocarcinoma. LGALS3 mRNA levels were higher in early stage colorectal cancers (58% in stage I) compared to advanced cancers (50% in stage IV) (43). Protein analysis found higher LGALS3 levels in primary adenocarcinomas than in metastatic adenocarcinomas, and stronger LGALS3 staining in well-differentiated tumor areas compared to poorly differentiated tumor areas (43). Conversely, colorectal adenocarcinomas may display higher levels of LGALS3 than do colorectal adenomas; one study sets the rate of colorectal adenocarcinoma expression of LGALS3 at 95% while only 73% of adenomas were positive for LGALS3 (43).

### [6] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
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
  - Snippet 1 (score: 0.780)
    > Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated. Induction of PPP2R2A protein (Fig. 5) but not gene expression (Fig. 7) in THP-1 cells expressing LGALS3 shRNA suggests that LGALS3 acts directly on the PP2A subunits via a post-transcriptional mechanism in these cells. The TCGA data (Table 3) however suggests that there is a positive correlation between gene expression of LGALS3 and PPP2R2A suggesting that a common pathway may regulate the two genes. Fig. 8. Progeny clustering identified an optimal number of 4 distinct protein clusters for this ProFnGrp. Protein networks were generated and showed interactions between "core-proteins" (large nodes) and other probed proteins (small nodes) from the data set. Clustering method has been described in our previous publication (ref. [37]) and further information on these protein networks can be found on our website "Leukemia Profile Atlases", available at https://www.leukemiaatlas.org/. Progeny clustering identified one protein cluster with expression similar to that of the normal CD34+ samples which was designated as "normal-state" while three "leukemia-specific" protein patterns characterized by high expression individually of CD74, LGAL3, and a fourth state with both on. PPP2RA/B/C/D was the only LGALS3 network protein demonstrated to be directly regulated by LGALS3 in the THP-1 cells (Fig. 5). In our previous study we saw potent suppression of AKT signaling by LGALS3 inhibition, so perhaps the mechanism involves LGALS3 suppression of the AKT phosphatase [15]. However, we did not see suppression of LGALS3 affect other network proteins in the THP-1 cells (data not shown). The role of other galectins such as LGALS1 in AML biology is not clear.
  - Snippet 2 (score: 0.777)
    > However, CD44 is present and interestingly is most elevated in patients with active LGALS3 network and CD74 network (Fig. 8). LGALS3 has been shown to be critical for CD44 endocytosis so LGALS3 would be expected to promote CD44 surface expression [54]. In AML cells with LGALS3 supported CD44 surface expression, CD74 would be predicted to augment signaling mediated by CD44.
    > LGALS3 is well known as an immune regulatory molecule that suppresses host anti-tumor immune surveillance by diverse mechanisms [1,2,55].
    > LGALS3 blocks or at least dampens immune cell function by reducing surface expression of glycosylated T cell receptor in T cells and preventing NK cell receptor binding to antigen [1,2]. LGALS3 has emerged as a critical component in MSC in AML patients to impact response to therapy [56]. It is likely that LGALS3 secreted from MSC and other support cells in the AML microenvironment negatively impacts immune surveillance in AML patients. It is yet to be determined if LGALS3 derived from the leukemia cells plays a role as an immune response inhibitor in AML.
    > LGALS9 is emerging as an important immune checkpoint inhibitor molecule as a TIM-3 binding partner [2,57]. LGALS9 also regulates T cell function as a CD44 binding partner [58]. Whereas LGALS3 binding to CD44 promotes metastasis, LGALS9 binding to CD44 suppresses this process [59,60]. Future RPPA studies to determine the role of LGALS9 and galectins other than LGALS3 are warranted.
    > For the first time, an at risk AML population has been found that is associated with active LGALS3 and active CD74 networks (Fig. 9A and  B). At present, it is unclear which if any proteins within the LGALS3 or CD74 networks is driving this phenomenon. CD44, SPP1, and CLPP are highly induced in the patient cohort with both networks active compared to patients with normal-like state (Fig. 8).
  - Snippet 3 (score: 0.772)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.
  - Snippet 4 (score: 0.751)
    > LGALS3 levels correlate with a variety of signaling molecules in blast cells from AML patients RPPA was used to examine correlations of LGALS3 with 230 other proteins. As shown in Fig. 3A, 68 of 231 proteins showed statistically significant (p b 0.0001, R N 0.25) correlation with LGALS3, with positive correlation for 27 total and 10 phospho-proteins and negative correlation for 24 total and 7 phospho-proteins. The strongest positive correlation was with the autophagy protein ATG7. The phospho-proteins positively correlated with LGALS3 included survival kinases such as p-ERK (pY202/pY204), p-AKT (pT308), three phospho-protein variants of PKC delta (i.e. pT507, pS645, and pS664), and p-PKC alpha (pS657) (Fig. 3). LGALS3 expression also positively correlated with phosphorylation of the tyrosine kinase SRC (i.e. pY416 and pY527). The most negatively correlated protein was Single Stranded DNA Binding Protein 2 (SSBP2) (Fig. 3). Among the other proteins negatively correlated with LGALS3 was the members of the PP2A B55 family (PPP2R2A, PPP2R2B, PPP2R2C, and PPP2R2D).
    > Protein network analysis was performed on the set of proteins associated with LGALS3 using String software (String 10.1; website: http:// string-db.org; ref. 38). The network of LGALS3 proteins identified by RPPA are highly associated with a protein:protein enrichment p value b1.0e−16 (Fig. 4) by String. Numerous biological pathways (N = 588) and KEGG pathways (N = 86) associated with LGALS3 network were identified using the String software. Data are presented in Supplemental Table 1 and Supplemental Table 2, respectively.

### [7] Clusterin Seals the Ocular Surface Barrier in Mouse Dry Eye
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
  - Snippet 1 (score: 0.779)
    > In other cases, CLU spots were clearly separate.
    > Next we considered what kinds of ocular surface molecules might bind CLU.
    > LGALS3, a key component of the ocular surface barrier, is a member of the galectin class of beta-galactosidebinding proteins. What is known about the glycosyl moiety of CLU is consistent with LGALS3 binding [25,27]. CLU applied to an LGALS3-sepharose affinity column bound to the beads and was not eluted 0.1 M sucrose, a disaccharide that does not compete with LGALS3 sugar binding, but was mostly eluted with a competitive inhibitor of LGALS3 sugar binding, 0.1 M beta-lactose (Fig 5C). This suggests that CLU binding to LGALS3 is specific for the beta-galactoside-binding function.

### [8] Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy
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
  - Snippet 1 (score: 0.771)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [9] High LGALS3 expression induced by HCP5/hsa-miR-27b-3p correlates with poor prognosis and tumor immune infiltration in hepatocellular carcinoma
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
  - Snippet 1 (score: 0.770)
    > LGALS3 has a crucial function in mediating cell adhesion as well as cell-cell interaction by recognizing complex carbohydrates on the surface of cells [22,23], as well as regulates cell apoptosis, autophagy, and inflammation [24,25].Interestingly, recent studies suggested that LGALS3 involves in essential cancer-related mechanisms, including cellular metabolism, carcinogenesis, metastasis, neoplasia, angiogenesis, as well as immune escape [26][27][28].In addition, LGALS3 is highly expressed and implicated in different cancer types progression such as HCC, gastric, colorectal, pancreatic carcinomas, melanomas or glioblastomas and breast cancer [29,30].Indeed, LGALS3 has been considered a potential marker for these malignancies.Interestingly, LGALS3, which is differentially expressed in different cancers, has been shown to exhibit tumor suppressor activity in certain cancer types.The different roles of LGALS3 may be attributed to different potential mechanisms that appear cancer-type dependent.The different locations and mutations of LGALS3 also contribute to its various functions.However, LGALS3 remains inadequately understood in HCC and requires further investigation.First, we conducted an extensive investigation of the expression profile, clinical prognosis, and pathologic stage of LGALS3 in HCC through an in-depth analysis of the public database.On the basis of TCGA and CPTAC datasets, we found that LGALS3 gene and protein expression was elevated in HCC tissues.Moreover, the OS and DSS were lesser in patients with HCC having higher expression levels of LGALS3 contrasted to those with low expression levels of LGALS3 based on GEPIA2 and Kaplan-Meier plotter datasets.Meanwhile, the expression of LGALS3 within HCC was significantly associated with the advanced tumor stage and grade, indicating that elevated LGALS3 expression could increase tumor progression.Song et al. [31] indicated that galectin-3 promoted HCC tumorigenesis and metastasis via β-catenin signalling in vitro and in vivo.

### [10] SMURF1 controls the PPP3/calcineurin complex and TFEB at a regulatory node for lysosomal biogenesis
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
  - Snippet 1 (score: 0.760)
    > Consistently,
    > LGALS3 and PPP3R1 were required for binding of PPP3CB and TFEB evidenced by knocking down LGALS3 or PPP3R1 decreased, while overexpression of LGALS3 or PPP3R1 increased, the interaction of PPP3CB and TFEB (Figure 8K, L).Of note, we found that the enhanced PPP3CB and TFEB interaction mediated by SMURF1 overexpression was abolished by LGALS3 deletion (Figure 8M).Overall, these data strengthened our hypothesis that LGALS3 and SMURF1 contribute to PPP3CB from "close" to "open" form, which facilitates TFEB docking to the AID domain (Figure 8N).
  - Snippet 2 (score: 0.758)
    > Immunofluorescence assay showed that PPP3R1 was also recruited to lysosomes upon LLOMe treatment in a LGALS3-dependent manner (Figure S4A).To identify the role of PPP3R1 in the formation of complex, as expected, we first found that PPP3CB directly binds with PPP3R1 in a LLOMe-enhanced manner (Figure 6A, B).Considering that PPP3CB was directly associated with LGALS3, we also checked the interaction between PPP3R1 and LGALS3.The results showed that PPP3R1 indirectly binds with LGALS3 (Figure 6C).Similarly, LLOMe treatment also promoted the binding affinity between PPP3R1 and LGALS3 (Figure 6D).We next mapped the key interaction domain of LGALS3 with PPP3R1, and showed the NT domain of LGALS3 was essential for the association with PPP3R1 (Figure 6E, F).Furthermore, overexpression of PPP3CB increased, suppression of PPP3CB abolished, the interactions of PPP3R1 and LGALS3 (Figure 6G, H), suggesting PPP3CB is also the bridge for the interaction between LGALS3 and PPP3R1.Interestingly, we also detected that SMURF1 indirectly interacted with PPP3R1, but not MCOLN1, in a LLOMe-enhanced manner (Figure S4B-E).Given that both SMURF1 and PPP3R1 were indirectly bound with the NT domain of LGALS3, we asked whether SMURF1 affected the interactions between PPP3R1 and LGALS3.Our data indicated that suppression of SMURF1 decreased, overexpression of SMURF1 increased, the interactions of PPP3R1 and LGALS3 (Figure 6I, J), suggesting SMURF1 promotes the recruitment of PPP3R1 by LGALS3.We next mapped the key HECT domain of SMURF1 which was essential for interaction with PPP3R1 (Figure 6K, L).

### [11] Krüppel-like Factor 3 (KLF3/BKLF) Is Required for Widespread Repression of the Inflammatory Modulator Galectin-3 (Lgals3)*
- Authors: Alexander J. Knights, Jinfen. J. Yik, Hanapi Mat Jusoh, Laura J. Norton, Alister P. W. Funnell et al.
- Year: 2016
- Venue: The Journal of Biological Chemistry
- URL: https://www.semanticscholar.org/paper/dce84b7faec66ad9234b04f596d036ed32078971
- DOI: 10.1074/jbc.M116.715748
- PMID: 27226561
- Citations: 27
- Influential citations: 1
- Summary: It is shown that the zinc finger transcription factor Krüppel-like factor 3 (KLF3) directly represses galectin-3 transcription, and mechanistic insights into the regulation of Lgals3 are provided, demonstrating that C-terminal binding protein (CtBP) is required to drive optimal KLF3-mediated silencing.
- Evidence snippets:
  - Snippet 1 (score: 0.757)
    > Despite the importance of galectin-3 in a host of biological settings, little is known about how its gene is activated (32)(33)(34), and to our knowledge, there is no published work on the repression of Lgals3. Here we have shown that galectin-3 expression is up-regulated in the absence of KLF3, and we have demonstrated that KLF3 directly binds and represses the Lgals3 promoter in vivo. Furthermore, we have provided mechanistic insights into KLF3 repression of Lgals3. In reporter assays, a KLF3 mutant that is unable to bind the co-repressor CtBP showed a reduced ability to repress Lgals3. Analysis of the expression levels of Lgals3 in Klf3 Ϫ/Ϫ MEFs rescued with KLF3 or a KLF3 mutant unable to bind to CtBP also showed that KLF3 recruitment of CtBP is necessary for optimal Lgals3 repression. These two lines of evidence suggest that recruitment of the co-repressor CtBP is important for KLF3 repression of Lgals3 but that CtBP-independent mechanisms also exist. We also assessed the contribution of the KLF3 functional domain to repression in Klf3 Ϫ/Ϫ MEF rescue experiments. KLF3 DNA-binding domain only showed only a modest ability to rescue Lgals3 repression when introduced into Klf3 Ϫ/Ϫ MEFs, suggesting that the functional domain (where CtBP binds) is important and also that direct competition for DNA binding to the Lgals3 promoter between KLF3 and the activating KLF1 is not likely to be a major feature of the mechanism of repression.
    > Galectin-3 has been identified as an important regulator of inflammation in metabolic tissues (27). Its deficiency in mice is associated with increased adiposity, systemic inflammation, and an accumulation of inflammatory cells in metabolic tissues (26,28). This phenotype poses a striking contrast to that seen in mice lacking KLF3, which display reduced fat mass and are protected from diet-induced obesity and glucose intolerance (23).

### [12] In-depth quantitative proteomics analysis revealed C1GALT1 depletion in ECC-1 cells mimics an aggressive endometrial cancer phenotype observed in cancer patients with low C1GALT1 expression
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
  - Snippet 1 (score: 0.755)
    > Finally, since LGALS3 (Galectin-3) has been shown to interact with O-glycans in the mucosal epithelium [30], and considering its overexpression observed by proteomics and further confirmed by PCR and WB analyses upon depletion of C1GALT1, we focused on the role of LGALS3 in EC by IHC.
    > A total of 151 out of 178 cores from 79 EC patients were considered adequate for LGALS3 expression assessment by IHC. Morphologic assessment of LGALS3 IHC staining characteristics revealed different staining patterns (Fig. 5 A). Out of the 151 evaluable cores, 45 (29.8%) showed absent LGALS3 expression. LGALS3 positive samples showed variable and low intensity protein expression (mean positive tumor cells per sample = 35.4%). A small subset of cores (13/151, 8.6%) demonstrated diffuse (> 90% positive tumor cells per sample) staining. LGALS3 score varied across histologic types, with serous and undifferentiated tumors displaying the highest protein expression (median IHC LGALS3 score = 10, 20, 50 and 55 for endometrioid, clear cell, serous and undifferentiated tumor types, respectively) (Fig. 5B). Interestingly, the aggressive histologic variants (clear cell, serous and undifferentiated) showed higher LGALS3 IHC scores than endometrioid variants (p value < 0.001). In addition, LGALS3 expression positively correlated with tumor grade. High grade tumors (G3) displayed higher protein expression (median LGALS3 IHC score = 30) compared to low grade tumors (median LGALS3 IHC score for G1/G2 tumors = 10). This finding was independent of histologic type, as similar results were observed when analyzing endometrioid tumors.
    > Finally, we interrogated the correlation between the expression levels of LGALS3 and C1GALT1.

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
  - Snippet 1 (score: 0.753)
    > To investigate whether cholesterol accumulation in dystrophic muscle is associated with the impaired lysosomal function, we sought a method to quantify lysosomal damage. Several studies have recently focused on lysosomal dysfunction, in which LMP plays a central role (18). However, very few studies have investigated lysosome damage in muscle. One identified marker of LMP is Gal-3 (or LGALS3), which is part of the galectins, a family of lectins that bind specifically to carbohydrates (19). These lectins are present in the cytosol, nucleus, and extracellular matrix and are translocated to the membrane of damaged lysosomes before their removal by the autophagy machinery (20). To analyze LGALS3 expression in a myogenic environment and its capacity to detect LMP, we differentiated healthy human immortalized myoblasts into elongated myotubes for 7 days and then performed immunostaining for LGALS3 and lysosome-associated membrane protein 2 (LAMP2), which is commonly used as a lysosome marker (21). A diffuse expression of LGALS3 was observed in the cells (fig. S1A). Treatment with l-leucyl-l-leucine methyl ester (LLOMe), a lysomotropic agent that induces lysosome-specific membrane damage (22), for 30 min at 2.5 mM triggered the formation of LGALS3-positive puncta, which colocalized with LAMP2, indicating typical damaged lysosomes. An up-regulation of LGALS3 was also detected by Western blotting after 30 min to 1 hour of LLOMe treatment (fig. S1, B and C). LGALS3 puncta were markedly reduced 3 hours after treatment, and LGALS3 expression was restored to the control level, demonstrating efficient lysosomal repair by the cells. This pattern correlated inversely with the amount of LGALS3 released in the media, detected by an enzyme-linked immunosorbent assay (ELISA) assay (fig.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.