---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-06-22T04:47:20.501649'
end_time: '2026-06-22T04:47:23.748620'
duration_seconds: 3.25
template_file: templates/function_support_deep_research.md
template_variables:
  organism: human
  gene: LGALS3
  gene_symbol: LGALS3
  taxon_id: NCBITaxon:9606
  taxon_label: Homo sapiens
  focus_type: function_support
  hypothesis_slug: function-support-go-0090280
  hypothesis_text: LGALS3 has positive regulation of calcium ion import (GO:0090280).
  term_context: '- Term: positive regulation of calcium ion import (GO:0090280)

    - Existing evidence type: IBA

    - Original reference: GO_REF:0000033'
  reference_context: '- GO_REF:0000033'
  source_file: genes/human/LGALS3/LGALS3-ai-review.yaml
  source_selector: existing_annotations[14]
  source_context_yaml: "term:\n  id: GO:0090280\n  label: positive regulation of calcium\
    \ ion import\nevidence_type: IBA\noriginal_reference_id: GO_REF:0000033"
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

# Literature evidence for LGALS3 (Homo sapiens): LGALS3 has positive regulation of calcium ion import (GO:0090280).

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


## Output

# Asta Literature Retrieval: Literature evidence for LGALS3 (Homo sapiens): LGALS3 has positive regulation of calcium ion import (GO:0090280). Gen...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 12
- Snippets retrieved: 20

## Relevant Papers

### [1] Identification of an Internal Gene to the Human Galectin-3 Gene with Two Different Overlapping Reading Frames That Do Not Encode Galectin-3*
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
  - Snippet 1 (score: 0.733)
    > Human Rapid-Scan Gene Expression Panel was used to detect the alternative transcripts in various human tissues using RT-PCR. The primers used were designed to amplify a 923-or 629-bp fragment.
    > LGALS3 transcripts were detected as a 457-bp DNA and actin transcripts as a 640-bp DNA. PCR was performed using 0.25 ng or 2.5 ng (10ϫ) template cDNA.
    > average of other human proteins is 10 times lower. This rich content in tryptophans confers hydrophobic properties that may account for the membrane localization of the ORF2⅐EGFP protein (Fig. 6). Consistent with the mitochondrial localization of the ORF2⅐EGFP fusion protein, this sequence exhibits the common properties of mitochondrial-imported proteins such as the enrichment of arginine, leucine, and serine residues (36).
    > Tissue Specificity of galig Expression-Detection of galig transcripts in HOS cells and colon tumor cells revealed a low expression level. Based on this observation, the rationale that the appearance of galig transcripts may have resulted from a leaky transcription of a cryptic promoter rather than from an independently functioning promoter could not be excluded. Screening of several human tissues indicated clearly that galig is a tightly regulated gene whose expression is most efficient in leukocytes from peripheral blood. The low level of transcription in bone marrow indicates that galig is specifically expressed in mature forms of leukocytes. Whereas the precise quantification of galig mRNA has not been addressed in these experiments, it is clear that these transcripts are much less abundant than LGALS3 transcripts. This may not be surprising considering that LGALS3 is known to be highly expressed when activated (37,38). Indeed, the amount of LGALS3 transcripts appeared as abundant as those from actin genes. This shows a different type of regulation by the galig and LGALS3 promoters. In particular, muscle, stomach, and uterus, although expressing low levels of galig transcripts, revealed no LGALS3 transcripts, thus indicating an independent functioning of the two promoters.

### [2] LGALS3 is connected to CD74 in a previously unknown protein network that is associated with poor survival in patients with AML
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
  - Snippet 1 (score: 0.721)
    > LGALS3 is associated with active Fig. 7. Suppression of LGALS3 does not alter gene expression of LGALS3 network protein genes or CD74 in THP-1 cells. RNA from THP-1 transductant cells with either LKO vector control shRNA or LGALS3 shRNA was isolated, cDNA produced, and mRNA levels of ATG7, LGALS3, ITGAL, CCND3, PRKCA, PARP1, CD74, MYC, CD44, SSBP2, PPP2R2A, CLPP, and B2M were determined by qRT-PCR and levels normalized to ABL-1 as described in "Materials and methods".
    > AKT and MAPK signaling. The protein with the strongest positive correlation with LGALS3 is with ATG7, an autophagy protein that has recently been implicated in maintaining hematopoietic stem cells and serving as a survival factor in AML [46,47]. Recent studies implicate LGALS3 in regulation of autophagy via autophagasome formation, though whether the mechanism involves ATG7 is not clear [48]. Interestingly, phosphorylated PKC delta was positively correlated with LGALS3. PKC delta is viewed as a pro-stress kinase but recent studies suggest that the enzyme has pro-survival properties [49][50][51]. Kinehara and colleagues suggest that PKC delta may act in human pluripotent stem cells as part of a mechanism to regulate stem cell renewal [52]. The data also suggest a novel relationship between LGALS3 and PP2A. The negative correlation of LGALS3 expression with PPP2R2A/B/C/D could reflect LGALS3 suppression of PP2A. The PP2A isoform containing PPP2R2A dephosphorylates both AKT and PKC alpha [53]. Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated.
  - Snippet 2 (score: 0.640)
    > The role of other galectins such as LGALS1 in AML biology is not clear.
    > LGALS1 may substitute for some LGALS3 functions particularly those involved in survival pathways as knock down of either LGALS1 or LGALS3 sensitized AML cells to BH3 mimetic drugs [15]. The failure of LGALS3 suppression to affect many of the RPPA identified proteins with the exception of PPP2R2A/B/C/D (Fig. 5) may reflect LGALS1 activity in these cells that may not be present in the primary AML cells. It is possible that many of the LGALS3 network proteins act to regulate LGALS3 rather than being regulated by the galectin. It is also possible that LGALS3 and some of the LGALS3 network proteins are subject to regulation by a yet unidentified common regulator(s). Further examination of the mechanism regulating the LGALS3 network is ongoing.
    > Network analysis from the data identifies a new extremely poor prognosis group based on the interaction between the LGALS3 and CD74 associated protein networks revealing potential biological pathways that may be critical in supporting AML cell survival. AML patients with both networks active are 8.5% of patients in the study (Fig. 9A) and thus this group may represent a sizeable population of AML patients. It is possible the two proteins regulate independent survival pathways that may have a synergistic effect on survival when both are active. The top ten biological processes associated with LGALS3 network include processes associated with cell metabolism (GO:0031325; GO:0032268; and GO:0032270), cell migration (GO:0030355), and response to growth factor stimulus (GO:0071363) and response to chemical stimulus (GO:0070887) (Supplemental Table 1). While it is unclear how LGALS3 might mechanistically influence leukemic cell recovery and growth after therapy, perhaps regulation of these cellular processes are important in addition to the well documented role of LGALS3 in regulation of cell cycle and cell proliferation [1,2,13,14].
  - Snippet 3 (score: 0.626)
    > Thus, potential suppression of the PP2A subunit by LGALS3 could account for elevated AKT and PKC alpha phosphorylation in samples where LGALS3 expression is elevated. Induction of PPP2R2A protein (Fig. 5) but not gene expression (Fig. 7) in THP-1 cells expressing LGALS3 shRNA suggests that LGALS3 acts directly on the PP2A subunits via a post-transcriptional mechanism in these cells. The TCGA data (Table 3) however suggests that there is a positive correlation between gene expression of LGALS3 and PPP2R2A suggesting that a common pathway may regulate the two genes. Fig. 8. Progeny clustering identified an optimal number of 4 distinct protein clusters for this ProFnGrp. Protein networks were generated and showed interactions between "core-proteins" (large nodes) and other probed proteins (small nodes) from the data set. Clustering method has been described in our previous publication (ref. [37]) and further information on these protein networks can be found on our website "Leukemia Profile Atlases", available at https://www.leukemiaatlas.org/. Progeny clustering identified one protein cluster with expression similar to that of the normal CD34+ samples which was designated as "normal-state" while three "leukemia-specific" protein patterns characterized by high expression individually of CD74, LGAL3, and a fourth state with both on. PPP2RA/B/C/D was the only LGALS3 network protein demonstrated to be directly regulated by LGALS3 in the THP-1 cells (Fig. 5). In our previous study we saw potent suppression of AKT signaling by LGALS3 inhibition, so perhaps the mechanism involves LGALS3 suppression of the AKT phosphatase [15]. However, we did not see suppression of LGALS3 affect other network proteins in the THP-1 cells (data not shown). The role of other galectins such as LGALS1 in AML biology is not clear.
  - Snippet 4 (score: 0.623)
    > While it is unclear how LGALS3 might mechanistically influence leukemic cell recovery and growth after therapy, perhaps regulation of these cellular processes are important in addition to the well documented role of LGALS3 in regulation of cell cycle and cell proliferation [1,2,13,14]. Many of the CD74 network associated biological processes involved immune regulation (Supplemental Table 3) though it is unclear if CD74 network regulates potential immune response in AML. Many of the CD74 network associated biological processes did include those involved in regulation of cell death and apoptosis (Supplemental Table 3). Of the 31 proteins correlated with CD74 expression, 19 are associated with the biological pathway regulation of cell death (GO.0010941) and 16 are associated with the biological pathway negative regulation of apoptotic process (GO.0043066). The raises the question of what the cross-talk is between the LGALS3 and CD74 networks? Gene expression analysis of CD74, CD44, and CLPP in the THP-1 LKO cells versus THP-1 cells with LGALS3 shRNA showed no or only slight changes in these genes (Fig. 7). Protein expression of CD74, CD44, and CLPP were similar in THP-1 LKO and THP-1 LGALS3 shRNA cells (data not shown). While LGALS3 supports AKT activation via RAS, CD74 would be expected to support AKT via MIF mediated signaling involving CD44 and/or CXCR4 [19][20][21][22][23][24][25][26][27]. Though the functional roles of LGALS3 and CD74 in this process are very different, each network would contribute to activation and perhaps may explain why patients with both active networks do so poorly (Fig. 9A  and B). Unfortunately, CXCR4 is not represented in the RPPA panel due to lack of validated antibody. However, CD44 is present and interestingly is most elevated in patients with active LGALS3 network and CD74 network (Fig. 8).

### [3] Systematic identification of potential key microRNAs and circRNAs in the dorsal root ganglia of mice with sciatic nerve injury
- Authors: Youfen Yu, Xueru Xu, Chunshui Lin, Rongguo Liu
- Year: 2023
- Venue: Frontiers in Molecular Neuroscience
- URL: https://www.semanticscholar.org/paper/bb63dc0bb6c65149c674451492fc049ff2f4ce8f
- DOI: 10.3389/fnmol.2023.1119164
- PMID: 36998510
- PMCID: 10043392
- Citations: 4
- Summary: Gene Ontology and Kyoto Encyclopedia of Genes and Genomes analysis demonstrated that these differentially expressed mRNAs and targeting miRNAs were involved in signal transduction, positive regulation of receptor-mediated endocytosis and regulation of neuronal synaptic plasticity in NeP.
- Evidence snippets:
  - Snippet 1 (score: 0.719)
    > The metabolic processes included positive regulation of apoptotic process (GO:0043065), negative regulation of neuron death (GO:1901215), regulation of angiogenesis (GO:0045765), positive regulation of calcium ion import (GO:0090280), positive regulation of receptor-mediated endocytosis (GO:0048260), positive regulation of serotonin secretion (GO:0014064), positive regulation of chemokine production (GO:0032722), etc. For CC, almost all of the enriched terms were related to cellular metabolic processes, intracellular organelles and signal transmission, such as neuronal cell body (GO:0043025), glial cell projection (GO:0097386), neuron projection (GO:0043005), glutamatergic synapse (GO:0098978), Golgi apparatus (GO:0005794), axon cytoplasm (GO:1904115), and postsynaptic density (GO:0014069). Regarding MF, the enriched terms were almost all associated with protein binding, sequence-specific binding and ion channel activity, including chemokine receptor binding (GO:0048020), neuropeptide hormone activity (GO:0005184), calmodulin binding (GO:0005516), transcription factor activity (GO:0003700), sequence-specific DNA binding (GO:0043565), transmembrane transporter activity (GO:0022857), extracellular-glutamate-gated ion channel activity (GO:0005234), and ligand-gated ion channel activity (GO:0015276).
    > In summary, the involvement of intracellular and extracellular signaling pathways in immune, inflammatory and oxidative stress processes as well as endocrine metabolic processes may be closely related to the onset and development of NeP.
  - Snippet 2 (score: 0.675)
    > KEGG functional analysis of DEmRNAs showed the top 17 representative enrichment pathways, including the MAPK signaling pathway, calcium signaling pathway, p53 signaling pathway, HIF-1 signaling pathway, and cytokine-cytokine receptor interaction (Figure 2A; Supplementary Table S2).
    > Furthermore, we performed GO analysis of DEGs, and the enriched results were highly significant, including 131 entries enriched in biological process (BP), 36 entries in cellular component (CC) and 34 entries in molecular function (MF) (Figures 2B-D; Supplementary Table S2). For BP, DEmRNAs were mainly enriched in inflammatory and immune processes as well as endocrine metabolism processes. The inflammatory and immune processes included inflammatory response The construction of protein-protein interaction network and identification of hub genes. (GO:0006954), neutrophil chemotaxis (GO:0030593), cellular response to interleukin-1 (GO:0071347), macrophage chemotaxis (GO:0048246), cytokine-mediated signaling pathway (GO:0019221), positive regulation of tumor necrosis factor production (GO:0032760), immune system process (GO:0002376), etc. The metabolic processes included positive regulation of apoptotic process (GO:0043065), negative regulation of neuron death (GO:1901215), regulation of angiogenesis (GO:0045765), positive regulation of calcium ion import (GO:0090280), positive regulation of receptor-mediated endocytosis (GO:0048260), positive regulation of serotonin secretion (GO:0014064), positive regulation of chemokine production (GO:0032722), etc.

### [4] Comparative transcriptome analysis provides clues to molecular mechanisms underlying blue-green eggshell color in the Jinding duck (Anas platyrhynchos)
- Authors: Zhepeng Wang, Guohua Meng, Yun Bai, Ruifang Liu, Yu Du et al.
- Year: 2017
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/9d37ba3b57ef695a83d1039fe094ded0df9f4b38
- DOI: 10.1186/s12864-017-4135-2
- PMID: 28899357
- PMCID: 5596863
- Citations: 28
- Summary: Given the involvement of membrane cholesterol contents, ions and ATP levels in modulating the transport activity of bile pigment transporters, the data suggest a potential association between duck BGEC and the transportActivity of the related transporter.
- Evidence snippets:
  - Snippet 1 (score: 0.698)
    > During eggshell formation, a series of ions, including Ca 2+ , HCO 3 − , Na + , K + , H + , and Cl − participate in the mineralization process [40]. Here, a total of 13 Ca 2+ , 10 Na + , 8 K + , 5 H + , and 1 Cl − transporter and two HCO 3 − synthesis genes were identified among the candidate genes (Additional files 2, and 4). Among the 13 Ca 2+ transport genes, ATP2C2, HTP1B, PKD2, RASA3, CACNB2, TRPC1, TRPC4, and TRPV2 were further annotated as calcium ion import (GO:0070509) and positive regulation of calcium ion import (GO:0090280) (Additional file 5). These Ca 2+ import genes were almost all downregulated in the BSD groups, with the exception of HTR1B and ATP2C2 (Fig. 5). In contrast, three Ca 2+ pumps (ATP2A2, ATP2B2, and ATP2C2) were all upregulated (Fig. 5). Genes mediating Na + , K + , H + , and Cl − transport were almost all upregulated, with the exception of one Na + (PKD2) and two K + (PKD2 and KCNF1) transport genes (Fig. 5). In addition, two HCO 3 − synthesis genes (CA2 and CA8) were upregulated in the BSD groups (Fig. 5).
    > We identified a considerable number of candidate genes involved in ion transport coupled ATP hydrolysis (i.e. Ca 2+ pumps and Na + /K + exchangers) and synthesis (i.e. H + transporters).

### [5] Lgals3 Promotes Calcium Oxalate Crystal Formation and Kidney Injury Through Histone Lactylation‐Mediated FGFR4 Activation
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
  - Snippet 1 (score: 0.695)
    > The incidence of kidney stones is increasing worldwide. However, the underlying mechanism of the process of kidney stone formation and the kidney damage caused are not well understood. Here, it is observed that Lgals3, a β‐galactoside‐binding protein, is significantly increased in tissues with calcium oxalate (CaOx) stones, and in both in vivo and in vitro models. Lgals3 expression is positively correlated with the deposition of CaOx crystals. Knockout of Lgals3 markedly reduces the deposition of CaOx crystal and renal fibrosis in vivo. Furthermore, Lgals3 deficiency decrease the glycolytic rate and lactate production during the process of CaOx deposition and inhibited histone lactylation of H3K18la. Mechanistic studies shows that Lgals3 directly interacted with the key glycolysis protein pyruvate kinase M2 (PKM2) and promoted its expression by modulating E3 ligase Trim21, preventing the ubiquitination of PKM2. Furthermore, H3K18 lactylation promoted CaOx crystal deposition and kidney injury in vivo and in vitro. Lgals3 deficiency inhibites the transcription, activation, and expression of FGFR4 through inhibition of H3K18la. These findings suggest that Lgals3 may play a key role in CaOx stone formation and kidney injury by interacting with PKM2 and promoting both H3K18la‐mediated gene transcription and activation.
  - Snippet 2 (score: 0.661)
    > [23] The result of the present study revealed that Lgals3 exhibited several novel functions and mechanisms in the formation of kidney stones and the development of renal fibrosis (Figure 13). It was found that Lgals3 was highly expressed in CaOx crystal deposition and stimulated the activation of glycolysis during crystal deposition and renal fibrosis. Knockout or pharmacological inhibition of Lgals3 demonstrated a significant reduction of crystal deposition and renal fibrosis. In addition, IP-MS analysis identified PKM2, a key molecule in the regulation of glycolytic function, as the direct binding target of Lgals3. Furthermore, this study integrated analyses of CUT&Tag and RNA-seq and demonstrated that Lgals3mediated histone lactylation promoted FGFR4 expression during the formation of CaOx stones and renal fibrosis. [24] Lgals3 is considered a disease-associated biomarker and it is significantly increased in cases of acute myocardial infarction or AKI. [25,26] urthermore, recent investigations have shown that it has significant potential as a therapeutic target for various inflammatory and fibrotic illnesses, including lung or kidney fibrosis. [27] n this study, it was found that Lgals3 expression was increased in both mouse and human CaOx crystal kidney tissues. This study utilized Lgals3 −/-mice and demonstrated that Lgals3 deficiency alleviated CaOx crystal deposition and renal fibrosis. The deposition of CaOx crystals and the development of renal fibrosis are complex processes regulated by numerous genes and signaling pathways. RNA-seq and 4D-DIA proteomics were performed to detect alterations in mRNA and protein expression in Lgals3-deficient cells under COM stimulation. The KEGG analysis showed that Lgals3 deficiency primarily enriched metabolicrelated pathways, specifically glycolysis. When cells are exposed to various stimuli, the mitochondrial energy metabolism undergoes alterations, leading to significant activation of glycolysis, which in turn increases the overall energy supply. [28]
  - Snippet 3 (score: 0.653)
    > To explore the role of Lgals3 in kidney injury caused by CaOx crystal, Lgals3 knockout (Lgals3 −/− ) mice were generated (Figure S3A,B, Supporting Information). qPCR, Western blot and immunohistochemistry staining were used to verify knockout efficiency (Figure S3C-E, Supporting Information). Subsequently, a CaOx kidney stone model was established (Figure 2A). CaOx crystal deposition markedly elevated blood urea nitrogen (BUN) and creatinine levels, whereas Lgals3 knockout ameliorated kidney function (Figure 2B,C). Histological assessment of kidney pathology by hematoxylin and eosin (HE) and Von Kossa staining showed that tubular injury and CaOx crystal deposition were significantly increased in the model group, whereas knockout of Lgals3 alleviated kidney injury and CaOx crystal formation (Figure 2D). Meanwhile, renal fibrotic structural alterations were evaluated, and Lgals3 knockout reduced collagen fiber deposition (Figure 2E,F). In addition, Inflammatory responses play a crucial role in the formation of calcium oxalate kidney stones. We found that CaOx crystals leads to an increase in the expression of inflammatory cytokines such as IL-1,IL-6 and TNF- (Figure S3F, Supporting Information). Conversely, the knockout of Lgals3 results in a significant decrease in the expression of these inflammatory factors.
    > To identify the role of Lgals3 in vitro, a Lgals3-knockdown HK-2 cell line was established and western blot analysis confirmed that Lgals3 knockdown was successful (Figure S4A, Supporting Information). The HK-2 cells were treated with COM for 48h to established the cell model. Immunofluorescence staining found that Lgals3 knockdown alleviated -SMA expression in COM-treated HK-2 cells (Figure S4C, Supporting Information). Western blot analysis showed a significant decrease in fibrosis-related protein expression under the stimulation of COM in vitro (Figure S4D, Supporting Information).

### [6] Periplocin suppresses the growth of colorectal cancer cells by triggering LGALS3 (galectin 3)-mediated lysophagy
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
  - Snippet 1 (score: 0.658)
    > We next investigated the mechanism underlying periplocinmediated lysophagy. The expression of LGALS3, a key lysophagy marker [46], was found to be upregulated following periplocin treatment as evidenced by immunofluorescent staining (Figure 2M). To this end, we presumed that periplocin-induced lysophagy might be attributable to the upregulation of LGALS3. Indeed, periplocin treatment prominently elevated the protein level of LGALS3 as evidence by immunoblotting analysis (Figure 6A). The increased protein level of LGALS3 was further confirmed in tumor xenografts from periplocin-treated mice (Figure 6B,C). However, no obvious change was observed on the mRNA level of LGALS3 in periplocin-treated cells compared with controls (Figure S6A), suggesting that transcriptional regulation was not involved in increased LGALS3 expression following periplocin treatment. Therefore, we postulated that periplocin might elevate LGALS3 by regulating protein stability. Of note, cycloheximide (CHX, a translational inhibitor) treatment led to an obvious decrease in LGALS3 protein level in control cells, but had no obvious effect on the upregulated protein level of LGALS3 in periplocin-treated cells, suggesting periplocin maintains LGALS3 stability (Figure 6D,E). In support of this, treatment with MG132 (a proteasome inhibitor) failed to further enhance the protein level of LGALS3 in response to periplocin treatment (Figure 6F,G). These data suggest that periplocin may prevent proteasomal degradation of LGALS3.
    > We therefore measured the effect of periplocin on LGALS3 ubiquitination. As shown in Figure 6H, periplocin markedly decreased the ubiquitin-conjugated level of LGALS3.
  - Snippet 2 (score: 0.651)
    > In addition, periplocin was found to stabilize the protein level of LGALS3 against thermal changes using a cellular thermal shift assay (CETSA) (Figure 6J,K), implying the binding of periplocin with LGALS3. The interaction between periplocin and LGALS3 was further confirmed by drug affinity responsive target stability (DARTS) analysis, as evidenced by a more stable property of LGALS3 protein against pronase digestion in response to periplocin treatment (Figure 6L,M). Moreover, using semiflexible docking analysis, we found that LGALS3 showed a good binding activity for periplocin, with a binding energy of −6.689 kcal/mol. Glu165, Arg162, Gly152, Gln150, Arg144, and Asn143 of LGALS3 were identified as possible sites for periplocin binding (Figure 6N,O), which required further experimental investigation. Together, these data suggest that periplocin binds and prevents ubiquitin-mediated degradation of LGALS3 in CRC cells.

### [7] Lysosomal damage is a therapeutic target in Duchenne muscular dystrophy
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
  - Snippet 1 (score: 0.642)
    > To confirm the inflammatory origin of these regions, coimmunostaining for LGALS3 and CD11b was performed on serial TA muscle cross sections (Fig. 1F). An overlay of both staining (CD11b and LGALS3) was observed between the myofibers, confirming the presence of infiltrating macrophages, while LGALS3 staining was also evident within myofibers. This indicates that the up-regulation of Gal-3 in muscle lysates reflects contributions from both immune infiltrates and myogenic sources.
    > To specifically quantify LMP in myofibers, we measured the number of LAMP2 + LGALS3 + puncta within myofibers, excluding inflammatory areas using a segmentation method (fig. S2A). This analysis revealed a significant increase in LAMP2 + LGALS3 + puncta in dystrophic muscle compared to WT controls (mean puncta = 9 for Dmd mdx-4Cv versus 1 in WT) (Fig. 1G), confirming that LGALS3 upregulation in Dmd mdx-4Cv muscles is not solely due to macrophage infiltration but also reflects myogenic up-regulation and recruitment to the lysosome, suggesting substantial LMP in dystrophic myofibers.
    > To validate these findings in human and large animal models, we analyzed muscle biopsies from patients with DMD and golden retriever muscular dystrophy (GRMD) dogs. LGALS3 up-regulation within myofibers was consistently observed in biopsies of patients with DMD from children aged 2 and nearly 4 years (Fig. 1H and fig. S2B) and in 6-month-old GRMD dogs (Fig. 1H). In all cases, LGALS3 colocalized with LAMP2 in most myofibers, further supporting the presence of LMP and myofiber-intrinsic Gal-3 up-regulation across species.

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
  - Snippet 1 (score: 0.642)
    > Hepatocellular carcinoma (HCC) is widely recognized for its unfavorable prognosis. Increasing evidence has revealed that LGALS3 has an essential function in initiating and developing several malignancies in humans. Nevertheless, thorough analysis of the expression profile, clinical prognosis, pathway prediction, and immune infiltration of LGALS3 has not been fully explored in HCC. In this study, an initial pan-cancer analysis was conducted to investigate the expression and prognosis of LGALS3. Following a comprehensive analysis, which included expression analysis and correlation analysis, noncoding RNAs that contribute to the overexpression of LGALS3 were subsequently identified. This identification was further validated using HCC clinical tissue samples. TIMER2 and GEPIA2 were employed to examine the correlation between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration in HCC. The R program was applied to analyze the expression distribution of immune score in in HCC patients with high and low LGALS3 expression. The expression profiles of immune checkpoints were also analyzed. Use R to perform GSVA analysis in order to explore potential signaling pathways. First, we conducted pan-cancer analysis for LGALS3 expression level through an in-depth analysis of public databases and found that HCC has a high LGALS3 gene and protein expression level, which were then verified in clinical HCC specimens. Meanwhile, high LGALS3 gene expression is related to malignant progression and poor prognosis of HCC. Univariate and multivariate analyses confirmed that LGALS3 could serve as an independent prognostic marker for HCC. Next, by combining comprehensive analysis and validation on HCC clinical tissue samples, we hypothesize that the HCP5/hsa-miR-27b-3p axis could serve as the most promising LGALS3 regulation mechanism in HCC. KEGG and GO analyses highlighted that the LGALS3-related genes were involved in tumor immunity. Furthermore, we detected a significant positive association between LGALS3 and HCP5 with immunological checkpoints, cell chemotaxis, and immune infiltration. In addition, high LGALS3 expression groups had significantly
  - Snippet 2 (score: 0.616)
    > To delineate the driving mechanism of LGALS3 for the malignant progression of HCC, the KEGG and GO analysis was conducted.The volcano plot and heatmap showed significantly differentially expressed genes between LGALS3 high-and low-expression groups (Figure S3A-B).The KEGG pathway analysis revealed that these LGALS3-related genes were enriched in the IL-17 signaling pathway, ECM-receptor interaction pathway, central carbon metabolism in cancer pathway, leukocyte transendothelial migration pathway and PI3K-Akt signaling pathway.Meanwhile, the GO analysis revealed that these genes were strongly associated with cell chemotaxis, leukocyte chemotaxis, regulation of leukocyte migration, as well as regulation of chemotaxis (Fig. 5A).Accumulating evidence has proven the immune system has an essential role in malignancy pathogenesis [17], and LGALS3 is closely correlated with CD163 + tumor-associated macrophages (TAM) in glioma [10].Therefore, we studied the association between LGALS3 level and the immune infiltration level in HCC.There was no statistical difference in immune cell infiltration levels over a number of LGALS3 copy numbers (Fig. 5B).Meanwhile, immune infiltration analysis revealed that expression of LGALS3 showed a significant positive association with several immune cell populations, involving CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, dendritic cell, as well as cancer-associated fibroblasts (CAFs) within HCC (Fig. 5C-E).Based on these results, we further evaluated the immune score in HCC patients with high and low LGALS3 expression.The scores of immune cells, including CD4 + T cell, CD8 + T cell, B cell, neutrophil, macrophage, and dendritic cell, were significantly higher in the high LGALS3 expression groups, as shown in Fig. 5F.Chemokines are a group of molecules that are important for the chemotaxis of immune cells [18].

### [9] Microarray assay of circular RNAs reveals cicRNA.7079 as a new anti-apoptotic molecule in spinal cord injury in mice.
- Authors: Ying Yao, Jingyu Wang, T. He, Heyangzi Li, Jue Hu et al.
- Year: 2020
- Venue: Brain research bulletin
- URL: https://www.semanticscholar.org/paper/8e327ffbb4c66488f7c21b3dc5f8bcd5321ffdae
- DOI: 10.1016/j.brainresbull.2020.08.004
- PMID: 32882320
- Citations: 24
- Summary: The anticipation of anti-apoptosis circRNA 7079 may provide potential research targets for SCI in mice and contribute to new insights into the mechanism of apoptosis after SCI.
- Evidence snippets:
  - Snippet 1 (score: 0.627)
    > the expression of downstream target genes. Our current study Our current study verified that lgals3 is the downstream target of the cicRNA.7079-mmu-miR-6953-5p axis. To date, the mechanisms of the regulation of lgals3 expression in CNS were barely known. In this study, we identified a new regulatory mechanism of lgals3 expression in motor neurons. The previous study reported that lgals3 was increased on day 14 after SCI in rats' spinal cord (Chih-Yen et al., 2011). In line with that, lgals3 was increased at day 3 after SCI in mice spinal cord in our study. Lgals3, has been described as a mediator of apoptosis. The anti-apoptotic role of lgals3 has been was demonstrated in peritoneal macrophages (Hsu et al., 2000), myocardial cells (Al-Salam et al., 2020), and melanoma cells (Wang et al., 2019a). Our study provided evidence that the anti-apoptotic effect of cicRNA.7079 was mediated by mmu-miR-6953-5p -lgals3 axis in motor neurons. Lgals3 containing the anti-death Asp-Trp-Gly-Arg (NWGR) motif, plays an anti-apoptotic effect possibly through its interaction with Bcl-2 family members, Akt-1, NF kappa-B, beta-cateninn, and cathepsin D proteins (Yang et al., 1996;Al-Salam et al., 2020;Akahani et al., 1997). Therefore, the detailed mechanism by which lgals3 regulates apoptosis in motor neurons needs to be further investigated.
    > Recently, circRNA expression profile in rat spinal cord at 6 h after SCI was identified by RNA-seq finding out that 99 circRNAs were up- Fig. 6. The apoptosis-related ceRNA network analysis. The top 30 apoptosis-related circRNAs were plotted as triangles. LncRNAs were plotted as rectangles. miRNAs were plotted as V-shapes.

### [10] SREBP1 regulates Lgals3 activation in response to cholesterol loading
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
  - Snippet 1 (score: 0.623)
    > Thus far, our data have shown transcriptional control of LGALS3 by SREBP1, likely in combination with BRD2. Of note, LGALS3 was initially used as a macrophage marker reciprocally regulating SREBP1 levels (Figure 5). In fact, increasing evidence in the literature supports the notion that LGALS3 is not merely a marker, but it actively participates in various cellular events while distributed broadly in intra-or extra-cellular locations of different cell types. 30 e were thus prompted to examine its possible influence on cholesterol-induced SMC phenotype. The data in Figure 7A show that LGALS3 silencing and overexpression potently mitigated and pro-moted an SMC migratory behavior, respectively, and LGALS3 knockdown without cholesterol loading appeared to be pro-apoptotic (Figure S6). These results agree with previous reports. 30,36 Consistent with SREBP1 regulation of LGALS3 (Figure 1), silencing SREBP1 reduced SMC migration as well (Figure 7B). Because cholesterol loading resulted in remarkable lipid accumulation inside SMCs (Figure 7C), we were curious as to whether this treatment had turned SMCs into an adipocyte-like phenotype, a question not previously addressed. We found that although three lipid-storage factors, SREBP1 (Figure 1), FABP4, and ACC1, were elevated after cholesterol loading, other adipogenic factors including CEBPA, PPARg, adiponectin, and ACAT2, decreased (Figure 7D). This result was confirmed by experiments with rat primary SMCs (Figure S7). Indicative of a specific role for LGALS3, its silencing significantly inhibited cholesterolinduced upregulation of SREBP1 (Figure 5), FABP4, and ACC1, albeit without a significant effect on other markers (Figure 7E). Accordingly, the effects of SREBP1 silencing on these markers largely followed the pattern that resulted from LGALS3 silencing (Figure 7F).

### [11] Thyroid malignant neoplasm-associated biomarkers as targets for oncolytic virotherapy
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
  - Snippet 1 (score: 0.620)
    > The Galectin-3 (LGALS3) is a protein that is encoded by a single gene, LGALS3, located on chromosome 14, locus q21-q22. 63 The molecular weight of this protein is ∼30 kDa, and it contains a carbohydrate-recognition-binding domain of ∼130 amino acids that enable the specific binding of β-galactosides. This protein localizes to the extracellular matrix, the cytoplasm, and the nucleus. It plays a role in numerous cellular functions including cell adhesion, cell activation and chemoattraction, cell growth, differentiation, cell cycle, apoptosis, innate immunity, cell adhesion, and T-cell regulation. 63,64 It has been known that LGALS3 is distributed widely around the tissues but in a low level.
    > To date, LGALS3 has been extensively studied as an IHC marker of thyroid malignancy, and a high diagnostic accuracy has been reported even for difficult pathological diagnoses. 64 Feilchenfeldt et al reported that the mRNA levels of LGALS3 and thyroglobulin in 28 benign and 31 malignant thyroid samples were quantified by real-time PCR. The LGALS3 expression at the mRNA was 60% (12/20) and the protein level was 100% (8/8), respectively. 65 The positive rate was 84% (41/49) when combined with the LGALS3 and HBME-1 in PTC specimens. 66 Two groups of researchers have detected the LGALS3 by IHC in PTC specimens. Saleh et al have shown that the sensitivity and the specificity for LGALS3 were 92.3% and 77.3%, respectively. 67 Song et al reported that positive expression of LGALS3 was 97% (427/441) in PTC group and 51% (77/151) in the benign thyroid lesions group. 68 These results may further support the notion that the high level of LGALS3 antigen expression occurs in patients with PTC. There are a number of different types of oncolytic viruses that have been altered from natural viruses in the laboratory such as adenovirus, reovirus, measles virus, herpes simplex

### [12] Extracellular Vesicles from iPSC-Derived Glial Progenitor Cells Prevent Glutamate-Induced Excitotoxicity by Stabilising Calcium Oscillations and Mitochondrial Depolarisation
- Authors: M. Shedenkova, Anastasiia A. Gurianova, I. Krasilnikova, A. Sudina, E. Karpulevich et al.
- Year: 2025
- Venue: Cells
- URL: https://www.semanticscholar.org/paper/6a7fa01a0c5294235731390acdd5215a4a803f13
- DOI: 10.3390/cells14231915
- PMID: 41369405
- PMCID: 12691032
- Citations: 1
- Summary: The obtaining results demonstrated the improvement of neuronal survival by reducing intracellular calcium levels and stabilising mitochondrial membrane potential under glutamate-induced excitotoxicity via PI3K-Akt signalling pathway activation.
- Evidence snippets:
  - Snippet 1 (score: 0.619)
    > The final category of identified processes involved the maintenance of intracellular homeostasis, which encompassed the following pathways: regulation of metal ion transport, positive regulation of transmembrane transport, positive regulation of secretion by cell, peptide hormone secretion, neuropeptide signalling pathway, positive regulation of ion transmembrane transporter activity, receptor recycling, and regulation of membrane depolarisation (Figure 12A).
    > Analysis of down-regulated pathways revealed significant enrichment of processes associated with neuronal physiology, including axonogenesis, regulation of cellular response to stress, dendrite development, regulation of synapse organisation, calcium ion transport, regulation of synapse structure or activity, axon guidance, neuron projection guidance, regulation of calcium ion transport, calcium ion transmembrane import into cytosol, negative regulation of epigenetic gene expression, neuron projection organisation, actin-mediated cell contraction, regulation of calcium ion transmembrane transport via high voltage-gated calcium channel, and axo-dendritic protein transport (Figure 12B).
    > For deeper functional insights, we performed KEGG pathway enrichment analysis, consistent with our previous experimental approach. Additionally, Figure 13A displays a heatmap of selected differentially expressed genes, illustrating specific expression patterns across experimental conditions. Up-regulated DEGs showed significant enrichment in several signalling pathways, including focal adhesion, PI3K-Akt signalling pathway, ECM-receptor interaction, motor proteins, phagosome, regulation of actin cytoskeleton, and glutathione metabolism (Figure 13A). Down-regulated DEGs were significantly associated with pathways, including cAMP signalling pathway, MAPK signalling pathway, calcium signalling pathway, dopaminergic synapse, cGMP-PKG signalling pathway, Ras signalling pathway, cellular senescence, Wnt signalling pathway, axon guidance, long-term potentiation, cholinergic synapse, Apelin signalling pathway, glutamatergic synapse, and GABAergic synapse (Figure 13B). Gene set enrichment analysis (GSEA) identified coordinated gene expression patterns distinguishing the glutamate (GL) and extracellular vesicle-treated (GL_EV) groups.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.