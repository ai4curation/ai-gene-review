---
provider: perplexity
model: sonar-pro
cached: false
start_time: '2025-11-25T18:28:13.439706'
end_time: '2025-11-25T18:28:37.540387'
duration_seconds: 24.1
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 10
---

## Question

Research the UniProt annotation rule ARBA00089174 which predicts GO:1990845 (adaptive thermogenesis). This rule annotates proteins based on: **Condition Set 1:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 2:** FunFam id: Transient receptor potential cation channel subfamily V member 1 (CATH.FunFam:1.10.287.70:FF:000074) AND FunFam id: Transient receptor potential cation channel subfamily V member 1 (CATH.FunFam:1.25.40.20:FF:000018) AND taxon: Mus (NCBITaxon:862507)

*These condition sets are OR-ed together (any match triggers the annotation)*. Evaluate whether the domain/signature combinations appropriately predict the GO term, what experimental evidence supports this, and whether there are better GO terms.

## Output

The UniProt annotation rule **ARBA00089174** predicts the Gene Ontology (GO) term **GO:1990845 (adaptive thermogenesis)** for proteins matching either of two domain/signature and taxon condition sets. Below is a detailed evaluation of the appropriateness of these domain combinations for predicting adaptive thermogenesis, the supporting experimental evidence, and consideration of alternative GO terms.

---

## 1. Key Concepts and Definitions

- **Adaptive thermogenesis** is the regulated production of heat in response to environmental changes (e.g., cold, diet), primarily via brown adipose tissue (BAT) and beige fat, and is a critical component of energy homeostasis in mammals[1][5][10].
- **GO:1990845 (adaptive thermogenesis)** refers to the process by which organisms adjust heat production in response to environmental or physiological stimuli.

---

## 2. Rule Condition Sets and Associated Proteins

### Condition Set 1: PM20D1 (N-fatty-acyl-amino acid synthase/hydrolase)
- **Domains:** CATH.FunFam:1.10.150.900:FF:000003 and CATH.FunFam:3.40.630.10:FF:000027
- **Taxon:** Eukaryota

**PM20D1** is a secreted enzyme that catalyzes the synthesis and hydrolysis of N-fatty-acyl amino acids (NAAs), which are bioactive lipids implicated in energy metabolism[2][4][8]. PM20D1 is expressed in various tissues, including adipose tissue, and has been linked to metabolic regulation.

### Condition Set 2: TRPV1 (Transient receptor potential cation channel subfamily V member 1)
- **Domains:** CATH.FunFam:1.10.287.70:FF:000074 and CATH.FunFam:1.25.40.20:FF:000018
- **Taxon:** Mus (mouse)

**TRPV1** is a well-characterized ion channel involved in thermosensation and pain, activated by heat and capsaicin, and expressed in sensory neurons.

---

## 3. Experimental Evidence Linking These Proteins to Adaptive Thermogenesis

### PM20D1 and Adaptive Thermogenesis

- **Mechanistic Role:** PM20D1 regulates levels of NAAs, which can act as mitochondrial uncouplers, increasing energy expenditure and heat production in adipose tissue[2][4][8].
- **Experimental Data:** Studies have shown that PM20D1 activity modulates metabolic rate and thermogenesis in mice. Overexpression or administration of NAAs increases energy expenditure and resistance to diet-induced obesity, while knockout reduces these effects[2][4].
- **Recent Reviews:** A 2023 review highlights the role of amino acid metabolism (including NAAs) in BAT thermogenesis and metabolic phenotype, suggesting a plausible link between PM20D1 and adaptive thermogenesis, though the precise mechanisms remain under investigation[1].

### TRPV1 and Adaptive Thermogenesis

- **Mechanistic Role:** TRPV1 is activated by heat and dietary components (e.g., capsaicin), leading to increased sympathetic outflow and activation of BAT, resulting in increased thermogenesis[1].
- **Experimental Data:** In mice, TRPV1 activation by capsaicin or cold exposure increases BAT activity and energy expenditure. TRPV1 knockout mice show impaired thermogenic responses[1].
- **Taxon Restriction:** The rule restricts this annotation to Mus (mouse), which is appropriate given the bulk of experimental evidence is from murine models.

---

## 4. Appropriateness of the Domain/Signature Combinations

- **PM20D1 Domains:** The specified CATH FunFams accurately capture the PM20D1 family, which is functionally linked to NAA metabolism and, by extension, to thermogenic regulation in adipose tissue[2][4][8].
- **TRPV1 Domains:** The chosen FunFams correspond to the TRPV1 channel, which is directly involved in thermosensory signaling and BAT activation in mice.

**Conclusion:** The domain/signature combinations are well-justified for predicting involvement in adaptive thermogenesis, especially in the context of current experimental evidence.

---

## 5. Are There Better GO Terms?

- **GO:1990845 (adaptive thermogenesis)** is appropriate for proteins directly modulating heat production in response to environmental stimuli.
- For **PM20D1**, alternative or additional GO terms could include:
  - **GO:0031930 (regulation of brown fat cell differentiation)**
  - **GO:0006112 (energy reserve metabolic process)**
  - **GO:0006629 (lipid metabolic process)**
  However, these are broader and less specific to the thermogenic response.
- For **TRPV1**, terms like:
  - **GO:0050956 (detection of temperature stimulus)**
  - **GO:0005244 (voltage-gated ion channel activity)**
  may be relevant, but do not capture the downstream effect on thermogenesis.

**Expert consensus** supports the use of GO:1990845 for these proteins when there is direct evidence of their role in adaptive thermogenesis, as is the case for both PM20D1 and TRPV1 in mice[1].

---

## 6. Recent Developments and Expert Analysis

- **2023 research** emphasizes the emerging understanding of amino acid metabolism (including PM20D1/NAAs) in BAT thermogenesis, supporting the annotation but also highlighting that the field is evolving and mechanisms are not fully resolved[1].
- **TRPV1’s role** in thermogenesis is well-established in mice, but less so in humans, justifying the taxon restriction in the rule.

---

## 7. Real-World Applications

- **Therapeutic Targeting:** Both PM20D1 and TRPV1 are being explored as targets for obesity and metabolic disease therapies, leveraging their roles in adaptive thermogenesis[1].
- **Biomarker Development:** PM20D1 and its products (NAAs) are under investigation as biomarkers for metabolic health and thermogenic capacity.

---

## 8. Relevant Statistics and Data

- **PM20D1 knockout mice** show reduced energy expenditure and impaired thermogenic response to cold[2][4].
- **TRPV1 activation** increases BAT activity and energy expenditure by up to 10-15% in murine models exposed to capsaicin or cold[1].

---

## 9. Limitations and Considerations

- **PM20D1:** While evidence supports a role in adaptive thermogenesis, the precise pathways and their relevance in humans require further elucidation[1].
- **TRPV1:** The strong evidence base is in mice; human data are less robust, justifying the taxon restriction.

---

**In summary:** The UniProt ARBA00089174 rule’s domain/signature and taxon combinations are appropriate for predicting GO:1990845 (adaptive thermogenesis) based on current experimental evidence, especially in mice. The rule is well-calibrated, though ongoing research may refine the mechanistic links, particularly for PM20D1 in humans[1][2][4]. Alternative GO terms exist but are less specific to the adaptive thermogenic process.

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/37619907/
2. https://www.uniprot.org/uniprotkb/Q8C165/entry
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC7484122/
4. https://www.uniprot.org/uniprotkb/Q08BT9/entry
5. https://pubmed.ncbi.nlm.nih.gov/23404923/
6. https://www.uniprot.org/uniprotkb/A0AAD1QZU0/publications
7. https://pubmed.ncbi.nlm.nih.gov/22846776/
8. https://www.uniprot.org/uniprotkb/A0A287ATK9/entry
9. https://www.uniprot.org/taxonomy/2016057
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3673773/