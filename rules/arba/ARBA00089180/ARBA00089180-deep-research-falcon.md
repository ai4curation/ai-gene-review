---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-01T21:46:37.456477'
end_time: '2025-12-01T21:53:21.108274'
duration_seconds: 403.65
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00089180
  rule_type: arba
  go_terms: GO:1990858 (cellular response to lectin)
  conditions_summary: '**Condition Set 1:** FunFam id: Non-specific serine/threonine
    protein kinase (CATH.FunFam:1.10.510.10:FF:000011) AND FunFam id: Non-specific
    serine/threonine protein kinase (CATH.FunFam:3.30.200.20:FF:000069) AND taxon:
    Primates (NCBITaxon:9443)


    **Condition Set 2:** FunFam id: E1A binding protein p300 (CATH.FunFam:1.10.246.20:FF:000001)
    AND FunFam id: E1A binding protein p300 (CATH.FunFam:1.20.1020.10:FF:000001) AND
    taxon: Catarrhini (NCBITaxon:9526)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00089180
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990858 (cellular response to lectin)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: Non-specific serine/threonine protein kinase (CATH.FunFam:1.10.510.10:FF:000011) AND FunFam id: Non-specific serine/threonine protein kinase (CATH.FunFam:3.30.200.20:FF:000069) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 2:** FunFam id: E1A binding protein p300 (CATH.FunFam:1.10.246.20:FF:000001) AND FunFam id: E1A binding protein p300 (CATH.FunFam:1.20.1020.10:FF:000001) AND taxon: Catarrhini (NCBITaxon:9526)

*These condition sets are OR-ed together (any match triggers the annotation)*

---

## Research Objective

This is a UniProt annotation rule that predicts GO terms based on protein domain/family signatures. Your task is to evaluate whether this rule makes valid biological predictions based on what is known about the relevant domains and families, their structure, and conservation.

In an ideal case, you will be able to find literature that speaks specifically to the relationship between domains/families and
the function. Failing that, include what is known specifically about other functions that domains/families have, as well what domains/
families are known for the function.

## Research Questions

### 1. Domain/Signature Context

For each domain signature in this rule:
- What is the biological function of proteins containing this domain?
- Is this domain diagnostic for the predicted function?
- Are there known subfamilies with different functions?
- Is the domain or family known to be multifunctional, are there known cases of neofunctionalization?

### 2. GO Term Appropriateness

For the predicted GO term(s) **GO:1990858 (cellular response to lectin)**:
- Is this GO term appropriate for proteins matching these conditions?
- Is the term too broad? (e.g., "catalytic activity" when a more specific term exists)
- Is the term too narrow? (e.g., a specific substrate when the domain covers broader specificity)
- Are there better alternative GO terms?

### 3. Literature Support

- What experimental evidence supports this functional annotation?
- Are there key papers describing this protein family/enzyme?
- Are there any contradictory findings in the literature?
- Is this a well-established function or more speculative?

### 4. Taxonomic Considerations

If this rule has taxonomic restrictions:
- Is the function conserved across the taxa included?
- Are there taxa that should be excluded (different function)?
- Are there taxa that could be included but are currently excluded?

### 5. Rule Logic Assessment

- Do the domain combinations make biological sense?
- Are there redundant conditions that could be removed?
- Could false positives arise from these conditions?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief assessment of rule validity
2. **Domain Analysis** - What each domain/signature represents
3. **GO Term Evaluation** - Assessment of the predicted annotation
4. **Evidence Review** - Key literature supporting or contradicting the rule
5. **Recommendations** - Suggested improvements or concerns

Be sure to include citations for all statements.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00089180
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990858 (cellular response to lectin)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: Non-specific serine/threonine protein kinase (CATH.FunFam:1.10.510.10:FF:000011) AND FunFam id: Non-specific serine/threonine protein kinase (CATH.FunFam:3.30.200.20:FF:000069) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 2:** FunFam id: E1A binding protein p300 (CATH.FunFam:1.10.246.20:FF:000001) AND FunFam id: E1A binding protein p300 (CATH.FunFam:1.20.1020.10:FF:000001) AND taxon: Catarrhini (NCBITaxon:9526)

*These condition sets are OR-ed together (any match triggers the annotation)*

---

## Research Objective

This is a UniProt annotation rule that predicts GO terms based on protein domain/family signatures. Your task is to evaluate whether this rule makes valid biological predictions based on what is known about the relevant domains and families, their structure, and conservation.

In an ideal case, you will be able to find literature that speaks specifically to the relationship between domains/families and
the function. Failing that, include what is known specifically about other functions that domains/families have, as well what domains/
families are known for the function.

## Research Questions

### 1. Domain/Signature Context

For each domain signature in this rule:
- What is the biological function of proteins containing this domain?
- Is this domain diagnostic for the predicted function?
- Are there known subfamilies with different functions?
- Is the domain or family known to be multifunctional, are there known cases of neofunctionalization?

### 2. GO Term Appropriateness

For the predicted GO term(s) **GO:1990858 (cellular response to lectin)**:
- Is this GO term appropriate for proteins matching these conditions?
- Is the term too broad? (e.g., "catalytic activity" when a more specific term exists)
- Is the term too narrow? (e.g., a specific substrate when the domain covers broader specificity)
- Are there better alternative GO terms?

### 3. Literature Support

- What experimental evidence supports this functional annotation?
- Are there key papers describing this protein family/enzyme?
- Are there any contradictory findings in the literature?
- Is this a well-established function or more speculative?

### 4. Taxonomic Considerations

If this rule has taxonomic restrictions:
- Is the function conserved across the taxa included?
- Are there taxa that should be excluded (different function)?
- Are there taxa that could be included but are currently excluded?

### 5. Rule Logic Assessment

- Do the domain combinations make biological sense?
- Are there redundant conditions that could be removed?
- Could false positives arise from these conditions?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief assessment of rule validity
2. **Domain Analysis** - What each domain/signature represents
3. **GO Term Evaluation** - Assessment of the predicted annotation
4. **Evidence Review** - Key literature supporting or contradicting the rule
5. **Recommendations** - Suggested improvements or concerns

Be sure to include citations for all statements.

1. Executive Summary
The UniProt ARBA rule ARBA00089180 predicts GO:1990858 (cellular response to lectin) for proteins matching either (a) CATH FunFams corresponding to generic serine/threonine protein kinase lobes in Primates, or (b) CATH FunFams corresponding to E1A binding protein p300 (EP300/CBP) domains in Catarrhini. Based on current evidence, this rule is not well supported biologically. The kinase FunFams capture broad, multifunctional catalytic domains and are not diagnostic for lectin-triggered processes; EP300/CBP domains are general transcriptional coactivator modules with no demonstrated specificity for lectin responses. While the GO term appears in recent enrichment analyses of immune and cardiovascular datasets, its assignment to individual kinases or EP300 by domain architecture alone is likely to generate false positives and is not taxonomically restricted to primates. We recommend not applying this rule, or at minimum tightening the logic to require explicit lectin pathway markers or experimentally supported pathway membership rather than generic domain signatures (adeyelu2023kinfamsdenovoclassification pages 4-5, kovacs2023predictivebiomarkersof pages 6-8, zhang2023integrationofmachine pages 10-14, kumar2024patternrecognitionreceptorsand pages 9-10, yang2024tlrsandother pages 12-15).

2. Domain Analysis
- Non-specific serine/threonine protein kinase FunFams (CATH 1.10.510.10:FF:000011 and 3.30.200.20:FF:000069): These map to the canonical C-lobe and N-lobe of protein kinases, respectively. CATH explicitly represents the kinase functional unit as two globular domains (3.30.200.20 N-lobe; 1.10.510.10 C-lobe), and more recently introduced a concatenated ‘functional unit’ level because both lobes are required for catalysis and most inhibitors bind the inter-lobe hinge. These domains are ubiquitous across eukaryotic kinases and are multifunctional; they are not diagnostic for a specific upstream stimulus such as lectin recognition, and numerous subfamilies perform diverse signaling roles across many pathways (Biomolecules 2023; DOI:10.3390/biom13020277) (adeyelu2023kinfamsdenovoclassification pages 4-5).
- EP300/CBP FunFams (CATH 1.10.246.20:FF:000001 and 1.20.1020.10:FF:000001): EP300/CBP are global coactivators with histone acetyltransferase (KAT) activity, bromodomains, and multiple interaction modules (e.g., CH/TAZ, KIX). However, the evidence assembled here does not identify these specific CATH FunFams nor tie them uniquely to cellular responses to lectins. Contemporary immunology reviews emphasize broad roles of coactivators and kinases downstream of many PRRs, but do not establish EP300/CBP domains as markers of lectin-triggered signaling per se (yang2024tlrsandother pages 12-15, kumar2024patternrecognitionreceptorsand pages 9-10).

3. GO Term Evaluation (GO:1990858: cellular response to lectin)
- Appropriateness: GO:1990858 refers to any cellular process modulated in response to a lectin stimulus at the cellular level. Recent studies use this term in gene set enrichment contexts (e.g., immune-checkpoint therapy transcriptomes; acute myocardial infarction leukocyte transcriptomes), indicating it marks pathway-level responses rather than specific molecular functions (Acta Pharmacol Sin 2023; DOI:10.1038/s41401-023-01079-6; J Transl Med 2023; DOI:10.1186/s12967-023-04573-x) (kovacs2023predictivebiomarkersof pages 6-8, zhang2023integrationofmachine pages 10-14).
- Too broad or too narrow: Assigning GO:1990858 to proteins by generic kinase or EP300/CBP domains is too broad, because these domains participate in many pathways not specific to lectin signaling. Conversely, the term is a biological process and should be supported by evidence of participation in lectin receptor pathways (e.g., C-type lectin receptors (CLRs) or galectin-mediated signaling) rather than the presence of widely used signaling domains (yang2024tlrsandother pages 12-15, kumar2024patternrecognitionreceptorsand pages 9-10).
- Better alternatives: If domain-level annotation is desired, generic signal transduction or kinase activity terms are appropriate for kinase domains, and histone acetyltransferase/transcription coactivator process terms are appropriate for EP300/CBP. GO:1990858 should be reserved for proteins with curated involvement in CLR or galectin signaling modules, or for datasets with pathway-level enrichment (adeyelu2023kinfamsdenovoclassification pages 4-5, kovacs2023predictivebiomarkersof pages 6-8, zhang2023integrationofmachine pages 10-14).

4. Evidence Review
- Lectin pathways and downstream signaling: CLRs are established PRRs activating intracellular signaling via canonical kinases (e.g., AKT/mTORC1, GSK3β) and inflammasome components. Recent reviews outline PRR networks including CLRs and note serine/threonine kinases (e.g., AKT; NEK7) in innate immune signaling and immunometabolic reprogramming, but do not tie the presence of generic kinase domains to a lectin-specific response (J Innate Immun 2024; DOI:10.1159/000539278; IntechOpen 2024; DOI:10.5772/intechopen.1003018) (kumar2024patternrecognitionreceptorsand pages 9-10, yang2024tlrsandother pages 12-15).
- EP300/CBP in immune signaling: Contemporary immunology overviews describe broad coactivator roles (EP300/CBP) in regulating transcriptional programs in response to various stimuli. However, within the assembled evidence there is no direct 2023–2024 demonstration that EP300/CBP domain presence alone predicts “cellular response to lectin.” Thus, linking EP300/CBP FunFams to GO:1990858 would be speculative without pathway-specific evidence (yang2024tlrsandother pages 12-15, kumar2024patternrecognitionreceptorsand pages 9-10).
- Use of GO:1990858 in recent literature: Two recent studies highlight practical usage. In a multi-cohort immunotherapy biomarker analysis, GO enrichment found “C-type lectin receptor signaling pathway” and “cellular response to lectin” among overrepresented processes associated with anti–PD-L1 response signatures, demonstrating the term’s utility at the gene-set level (Acta Pharmacol Sin 2023; DOI:10.1038/s41401-023-01079-6) (kovacs2023predictivebiomarkersof pages 6-8). In an AMI leukocyte transcriptomics study integrating machine learning, enrichment included “response to lectin” and “cellular response to lectin,” again in a pathway-level context (J Transl Med 2023; DOI:10.1186/s12967-023-04573-x) (zhang2023integrationofmachine pages 10-14).
- Kinase domain context from structure classification: CATH explicitly designates the N-lobe (3.30.200.20) and C-lobe (1.10.510.10) of kinase domains and emphasizes their ubiquity and multifunctionality across kinases; they are not tied to a unique upstream stimulus such as lectin exposure (Biomolecules 2023; DOI:10.3390/biom13020277) (adeyelu2023kinfamsdenovoclassification pages 4-5).
- Taxonomic considerations: Reviews of PRR-induced immunometabolism underline species differences (e.g., human vs mouse microglia) in downstream metabolic wiring after PRR activation, but do not confine lectin responses to primates or Catarrhini. CLR signaling is conserved across mammals and not primate-specific; therefore, restricting GO:1990858 to primate taxa lacks support (J Innate Immun 2024; DOI:10.1159/000539278; IntechOpen 2024; DOI:10.5772/intechopen.1003018) (kumar2024patternrecognitionreceptorsand pages 9-10, yang2024tlrsandother pages 12-15).
- Related mechanistic context: Immune epigenetics in sepsis shows histone modification enzymes and coactivators modulate innate responses, and macrophage biology reviews emphasize PRR networks including CLRs in shaping polarization. These underscore that many generic signaling and epigenetic regulators participate downstream of multiple PRRs, further arguing against domain-only inference for lectin-specific responses (Cell Death Dis 2023; DOI:10.1038/s41419-023-05656-9; Signal Transduct Target Ther 2023; DOI:10.1038/s41392-023-01452-1) (wu2023epigeneticmechanismsof pages 8-9, chen2023macrophagesinimmunoregulation pages 19-20).

5. Recommendations
- Do not annotate GO:1990858 from generic kinase lobes (CATH 1.10.510.10 and 3.30.200.20) alone: These FunFams capture essentially all eukaryotic serine/threonine kinases; they are multifunctional and not diagnostic for lectin response. Rule-driven annotation here will produce many false positives (adeyelu2023kinfamsdenovoclassification pages 4-5).
- Do not annotate GO:1990858 from EP300/CBP domain FunFams alone: EP300/CBP are broad coactivators across myriad pathways; no curated evidence in 2023–2024 sources ties their domain architecture specifically to lectin responses. Without pathway-specific evidence, such inference is speculative (yang2024tlrsandother pages 12-15, kumar2024patternrecognitionreceptorsand pages 9-10).
- Require pathway-level or experimental evidence: If the aim is to capture lectin-responsive proteins, integrate domain signatures for recognized CLR adaptors/signaling modules (e.g., SYK-dependent CLR adapters in species where applicable) or transcriptomic/proteomic evidence linking the protein to lectin stimulation. Alternatively, restrict the rule to proteins annotated to CLR pathways or to datasets where GO:1990858 is enriched and the protein is a demonstrated component (kovacs2023predictivebiomarkersof pages 6-8, zhang2023integrationofmachine pages 10-14).
- Remove primate/Catarrhini taxon restrictions: There is no evidence that cellular responses to lectins are primate-specific; PRR/CLR signaling is a conserved mammalian innate immune mechanism. Restricting to Primates/Catarrhini risks unnecessary false negatives and lacks support (kumar2024patternrecognitionreceptorsand pages 9-10, yang2024tlrsandother pages 12-15).
- Alternative GO assignments: For kinase FunFams, use molecular function terms such as “protein serine/threonine kinase activity” or “signal transduction” process terms based on broader evidence. For EP300/CBP FunFams, use “histone acetyltransferase activity” and “positive regulation of transcription” process terms where applicable, rather than lectin-specific cellular response (adeyelu2023kinfamsdenovoclassification pages 4-5).

URLs and publication dates (selected):
- Adeyelu et al., Biomolecules, Feb 2023. KinFams and CATH kinase lobes: https://doi.org/10.3390/biom13020277 (adeyelu2023kinfamsdenovoclassification pages 4-5).
- Kovács et al., Acta Pharmacologica Sinica, Apr 2023. GO:1990858 enrichment in immunotherapy datasets: https://doi.org/10.1038/s41401-023-01079-6 (kovacs2023predictivebiomarkersof pages 6-8).
- Zhang et al., Journal of Translational Medicine, Oct 2023. GO: response/cellular response to lectin enrichment in AMI leukocytes: https://doi.org/10.1186/s12967-023-04573-x (zhang2023integrationofmachine pages 10-14).
- Kumar & Stewart, Journal of Innate Immunity, May 2024. PRRs incl. CLRs and ser/thr kinase roles in immunometabolism: https://doi.org/10.1159/000539278 (kumar2024patternrecognitionreceptorsand pages 9-10).
- Yang & Yuan, IntechOpen chapter, 2024. TLR crosstalk and listing of CLRs; AKT ser/thr kinase mentioned in crosstalk context: https://doi.org/10.5772/intechopen.1003018 (yang2024tlrsandother pages 12-15).
- Wu et al., Cell Death & Disease, Feb 2023. Epigenetic regulation in sepsis innate immunity: https://doi.org/10.1038/s41419-023-05656-9 (wu2023epigeneticmechanismsof pages 8-9).
- Chen et al., Signal Transduction and Targeted Therapy, May 2023. Macrophage immunoregulation and PRRs including CLRs: https://doi.org/10.1038/s41392-023-01452-1 (chen2023macrophagesinimmunoregulation pages 19-20).

References

1. (adeyelu2023kinfamsdenovoclassification pages 4-5): Tolulope Adeyelu, Nicola Bordin, Vaishali P. Waman, Marta Sadlej, Ian Sillitoe, Aurelio A. Moya-Garcia, and Christine A. Orengo. Kinfams: de-novo classification of protein kinases using cath functional units. Biomolecules, 13:277, Feb 2023. URL: https://doi.org/10.3390/biom13020277, doi:10.3390/biom13020277. This article has 8 citations and is from a poor quality or predatory journal.

2. (kovacs2023predictivebiomarkersof pages 6-8): Szonja Anna Kovács, János Tibor Fekete, and Balázs Győrffy. Predictive biomarkers of immunotherapy response with pharmacological applications in solid tumors. Acta Pharmacologica Sinica, 44:1879-1889, Apr 2023. URL: https://doi.org/10.1038/s41401-023-01079-6, doi:10.1038/s41401-023-01079-6. This article has 156 citations and is from a peer-reviewed journal.

3. (zhang2023integrationofmachine pages 10-14): Lin Zhang, Yue Liu, Kaiyue Wang, Xiangqin Ou, Jiashun Zhou, Houliang Zhang, Min Huang, Zhenfang Du, and Sheng Qiang. Integration of machine learning to identify diagnostic genes in leukocytes for acute myocardial infarction patients. Journal of Translational Medicine, Oct 2023. URL: https://doi.org/10.1186/s12967-023-04573-x, doi:10.1186/s12967-023-04573-x. This article has 11 citations and is from a peer-reviewed journal.

4. (kumar2024patternrecognitionreceptorsand pages 9-10): Vijay Kumar and John H. Stewart IV. Pattern-recognition receptors and immunometabolic reprogramming: what we know and what to explore. Journal of Innate Immunity, 16:295-323, May 2024. URL: https://doi.org/10.1159/000539278, doi:10.1159/000539278. This article has 18 citations and is from a peer-reviewed journal.

5. (yang2024tlrsandother pages 12-15): Chao Yang and Ruoxi Yuan. Tlrs and other molecules signaling crosstalk in diseases. Thirty Years since the Discovery of Toll-Like Receptors, Jan 2024. URL: https://doi.org/10.5772/intechopen.1003018, doi:10.5772/intechopen.1003018. This article has 0 citations.

6. (wu2023epigeneticmechanismsof pages 8-9): Dan Wu, Yuxin Shi, Hao Zhang, and Changhong Miao. Epigenetic mechanisms of immune remodeling in sepsis: targeting histone modification. Cell Death &amp; Disease, Feb 2023. URL: https://doi.org/10.1038/s41419-023-05656-9, doi:10.1038/s41419-023-05656-9. This article has 94 citations and is from a peer-reviewed journal.

7. (chen2023macrophagesinimmunoregulation pages 19-20): Shanze Chen, Abdullah F U H Saeed, QUAN LIU, Qiong Jiang, Haizhao Xu, G. Xiao, L. Rao, and Yanhong Duo. Macrophages in immunoregulation and therapeutics. Signal Transduction and Targeted Therapy, May 2023. URL: https://doi.org/10.1038/s41392-023-01452-1, doi:10.1038/s41392-023-01452-1. This article has 1632 citations and is from a peer-reviewed journal.

## Citations

1. adeyelu2023kinfamsdenovoclassification pages 4-5
2. kovacs2023predictivebiomarkersof pages 6-8
3. zhang2023integrationofmachine pages 10-14
4. kumar2024patternrecognitionreceptorsand pages 9-10
5. yang2024tlrsandother pages 12-15
6. wu2023epigeneticmechanismsof pages 8-9
7. chen2023macrophagesinimmunoregulation pages 19-20
8. https://doi.org/10.3390/biom13020277
9. https://doi.org/10.1038/s41401-023-01079-6
10. https://doi.org/10.1186/s12967-023-04573-x
11. https://doi.org/10.1159/000539278
12. https://doi.org/10.5772/intechopen.1003018
13. https://doi.org/10.1038/s41419-023-05656-9
14. https://doi.org/10.1038/s41392-023-01452-1
15. https://doi.org/10.3390/biom13020277,
16. https://doi.org/10.1038/s41401-023-01079-6,
17. https://doi.org/10.1186/s12967-023-04573-x,
18. https://doi.org/10.1159/000539278,
19. https://doi.org/10.5772/intechopen.1003018,
20. https://doi.org/10.1038/s41419-023-05656-9,
21. https://doi.org/10.1038/s41392-023-01452-1,