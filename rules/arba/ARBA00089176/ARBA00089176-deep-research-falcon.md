---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-01T19:49:16.349594'
end_time: '2025-12-01T19:55:55.439983'
duration_seconds: 399.09
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00089176
  rule_type: arba
  go_terms: GO:1990840 (response to lectin)
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
citation_count: 27
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00089176
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990840 (response to lectin)
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

For the predicted GO term(s) **GO:1990840 (response to lectin)**:
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

- **Rule ID:** ARBA00089176
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990840 (response to lectin)
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

For the predicted GO term(s) **GO:1990840 (response to lectin)**:
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
UniProt Rule ARBA00089176 assigns GO:1990840 (response to lectin) based on two alternative domain-logic condition sets: (1) non-specific serine/threonine protein kinase FunFams in Primates, or (2) p300/CBP FunFams in Catarrhini. Current evidence shows that lectin responses in mammals are primarily mediated by pattern-recognition receptors (PRRs), notably C-type lectin receptors (CLRs) and the complement lectin pathway, which signal via tyrosine-kinase modules (Syk) and adaptor scaffolds (CARD9–BCL10–MALT1), while also engaging downstream serine/threonine kinase cascades (e.g., PKCδ, MAPKs). However, generic serine/threonine kinase domains and p300/CBP histone acetyltransferase domains are not diagnostic for lectin responsiveness and occur across many signaling pathways. The rule therefore risks false positives and appears biologically under-justified, particularly with primate-restricted taxon filters. Recent literature (2023–2024) confirms lectin signaling pathways and the usage of GO “response to lectin”/“cellular response to lectin” in human datasets, but provides no direct linkage between p300 domain composition per se and a lectin response phenotype. Overall, the rule should not be activated as written without additional, more specific lectin-receptor or pathway markers. (malamud2024thedectin1and pages 1-2, colaco2024mannoseandlactobionic pages 20-22, ganguly2024neemleafglycoprotein pages 14-16, kumarUnknownyearaspectsofgene pages 68-71)

2. Domain Analysis
- Non-specific serine/threonine protein kinase FunFams (CATH FunFams: 1.10.510.10:FF:000011; 3.30.200.20:FF:000069). These FunFams correspond to generic protein kinase catalytic cores found in many signaling proteins (e.g., MAPKs, PKCs, AKT). In mammalian lectin pathways, CLR engagement activates Syk and CARD9 and can propagate to serine/threonine kinase modules (e.g., PKCδ and MAPKs), but those kinases are ubiquitous in diverse pathways; domain presence is not diagnostic of lectin signaling. Evidence from human THP-1 monocytic cells challenged with glycans shows MAPK/AP-1 pathway activation, supporting that serine/threonine cascades can be downstream of lectin/PRR stimulation; nevertheless, many non-lectin stimuli use the same cascades. Thus these FunFams are not specific for “response to lectin.” (kotrba2023mastcellsecretory pages 26-30, ganguly2024neemleafglycoprotein pages 14-16, kumarUnknownyearaspectsofgene pages 68-71)
- p300/CBP FunFams (CATH FunFams: 1.10.246.20:FF:000001; 1.20.1020.10:FF:000001). p300/CBP are broad coactivator histone acetyltransferases (HATs) integrating many immune and stress signals to remodel chromatin and regulate transcription. Reviews and recent studies emphasize p300/CBP roles in cytokine signaling, STAT3/AKT cross-talk, and disease contexts, but do not establish that p300 domain presence predicts a protein’s involvement in lectin responses. No direct evidence was found that p300 is uniquely or preferentially recruited by lectin receptor signaling relative to other PRRs; rather, it is a general transcriptional coactivator. Hence p300/CBP FunFam membership is not diagnostic for “response to lectin.” (, )
- Multifunctionality and neofunctionalization: Both kinase cores and p300/CBP are highly multifunctional with many subfamilies and context-dependent roles. Their widespread use across signaling reduces specificity for lectin pathways. (, )

3. GO Term Evaluation (GO:1990840 “response to lectin”)
- Appropriateness: The term describes changes in state or activity of a cell or organism as a result of lectin stimulus; it is used in recent human clinical and omics datasets (e.g., cardiovascular/immune transcriptomes) alongside “cellular response to lectin” (GO:1990858). This supports the conceptual validity of annotating lectin-responsive biology. However, applying it based solely on generic kinase or p300 domains is too broad and risks misannotation. (Examples of usage: Frontiers in Immunology 2024 NAFLD–HF meta-analysis; Journal of Translational Medicine 2023 AMI leukocyte study; pediatric sepsis transcriptomics 2024). (colaco2024mannoseandlactobionic pages 20-22)
- Specificity: The term is neither too broad nor too narrow if applied when a protein participates in lectin recognition or its immediate, canonical signaling adapters (e.g., CLRs, Syk, CARD9/BCL10/MALT1, MASPs in complement). It is inappropriate for generic downstream effectors (ubiquitous kinases, chromatin coactivators) absent evidence of preferential coupling to lectin signaling. (colaco2024mannoseandlactobionic pages 20-22, malamud2024thedectin1and pages 1-2)
- Alternatives: Consider pathway-proximal terms such as “C-type lectin receptor signaling pathway” (GO:0002223) or “lectin complement pathway” child terms, if supported by domain or experimental features. “Response to lectin” should be reserved for proteins with clear functional involvement in lectin detection or immediate transduction. (colaco2024mannoseandlactobionic pages 20-22)

4. Evidence Review
- CLR signaling and serine/threonine kinase involvement. Authoritative reviews and 2024 primary data demonstrate that CLR engagement (e.g., Dectin-1) signals via tyrosine kinases (Syk) and adaptor complexes (CARD9–BCL10–MALT1) to activate NF-κB, with documented use of serine/threonine PKCδ and MAPKs downstream. For example, murine dendritic cells stimulated with a β-glucan–containing neem leaf glycoprotein required Dectin-1→PKCδ→CARD9 signaling to remodel IL-12/IL-10 outputs, directly linking lectin receptor ligation to a serine/threonine kinase cascade. Reviews also note Raf-1–dependent CLR signaling and MAPK activation. Human monocyte-derived THP-1 cells challenged with glycans showed AP-1/MAPK pathway engagement. Together, these confirm that lectin receptor signaling can recruit ubiquitous Ser/Thr kinase modules, but these modules are not unique to lectin signaling. URLs: https://doi.org/10.1186/s12964-024-01576-z (Apr 2024); https://doi.org/10.25673/110894 (Jan 2023). (ganguly2024neemleafglycoprotein pages 14-16, kotrba2023mastcellsecretory pages 26-30, kumarUnknownyearaspectsofgene pages 68-71)
- Complement lectin pathway breadth. The lectin pathway (MBL, ficolins, collectins; MASP-1/2/3) is broadly conserved across vertebrates and is implicated in numerous diseases. This underlines that “response to lectin” biology is taxonomically broad, not confined to primates or Catarrhini. URL: https://doi.org/10.3390/ijms25031566 (Jan 2024). (colaco2024mannoseandlactobionic pages 20-22)
- Mammalian CLR biology and taxonomic considerations. 2024 reviews emphasize the conserved genomic organization and function of Dectin clusters in humans and mice, documenting CLR-triggered phagocytosis, cytokine production, ROS/NETs, and antigen presentation. This again argues against primate-limited rules unless tied to primate-specific sequences/ligands. URL: https://doi.org/10.1038/s44319-024-00296-2 (Oct 2024). (malamud2024thedectin1and pages 1-2)
- Use of “response to lectin” in recent human datasets. Multiple 2023–2024 omics analyses report enrichment of “response to lectin”/“cellular response to lectin” terms, indicating active usage in human systems biology: (i) NAFLD–heart failure meta-analysis (Frontiers in Immunology 2024) lists “response to lectin” among enriched processes; (ii) AMI leukocyte machine-learning study (Journal of Translational Medicine 2023) similarly enriches CLR signaling and “response to lectin;” (iii) pediatric sepsis transcriptomics notes “response to lectin” enrichment in outcome groups. URLs: https://doi.org/10.3389/fimmu.2024.1424308 (Sep 2024); https://doi.org/10.1186/s12967-023-04573-x (Oct 2023); https://doi.org/10.5005/jp-journals-10071-24789 (Aug 2024). (colaco2024mannoseandlactobionic pages 20-22)
- p300/CBP in immune signaling. Reviews highlight p300/CBP roles as generalist HAT coactivators integrating immune pathways (e.g., STAT3, AKT) and shaping transcriptional programs across inflammation and disease; however, these studies do not tie p300/CBP specifically to lectin receptor signaling. Any coupling is indirect and context-dependent. URLs: https://doi.org/10.1038/s12276-023-01014-z (Jul 2023); https://doi.org/10.3390/ijms241914551 (Sep 2023). (, )
- Additional lectin receptor in mammals. LOX-1 (OLR1), a lectin-like receptor, participates in inflammatory signaling and host–pathogen interactions, further demonstrating the diversity of mammalian lectin responses, but without domain-level markers pointing to p300 or generic kinase cores. URL: https://doi.org/10.1159/000535793 (Jan 2024). (truthe2024roleoflectinlike pages 7-9)

5. Recommendations
- Do not assign GO:1990840 based solely on generic serine/threonine kinase FunFams or p300 FunFams. These domains are non-diagnostic for lectin responsiveness and are widely reused across signaling. Retain the term for proteins with domain signatures or orthology to lectin receptors (e.g., CLRs with CTLD and signaling motifs/adaptors) or complement lectin pathway components (MBL, ficolins, MASPs). (colaco2024mannoseandlactobionic pages 20-22, malamud2024thedectin1and pages 1-2)
- Strengthen rule logic by requiring lectin-receptor or adaptor/kinase signatures proximal to CLR signaling, e.g., presence of CTLD consistent with mammalian CLR families, Syk-binding motifs, CARD9/BCL10/MALT1 association domains, or complement lectin pathway PRM/MASP signatures. This would markedly reduce false positives. (colaco2024mannoseandlactobionic pages 20-22, kotrba2023mastcellsecretory pages 26-30)
- Remove or relax primate/Catarrhini taxon restrictions unless supported by evidence of lineage-specific lectin pathways or ligands; mammalian lectin responses are broadly conserved and not primate-specific. (colaco2024mannoseandlactobionic pages 20-22, malamud2024thedectin1and pages 1-2)
- If retention is desired, reframe the GO assignment to a less specific downstream term (e.g., “regulation of NF-κB signaling”) when only generic kinase or p300 domains are present, and only if additional evidence links the protein to PRR signaling contexts in the same sequence space. (kotrba2023mastcellsecretory pages 26-30, ganguly2024neemleafglycoprotein pages 14-16)
- Add explicit exclusions: proteins annotated only by general kinase/p300 domains without PRR linkage should not receive “response to lectin.” Consider positive evidence filters (e.g., co-occurrence with CTLD signatures) or negative evidence (absence of CTLD/adaptor features) to gate the rule. (colaco2024mannoseandlactobionic pages 20-22)

References (URLs/dates embedded above; statements supported by the following sources):
- CLR clusters in mammals and signaling overview (EMBO Reports, Oct 2024): https://doi.org/10.1038/s44319-024-00296-2 (Dectin-1/2 clusters). (malamud2024thedectin1and pages 1-2)
- Complement lectin pathway breadth (IJMS, Jan 2024): https://doi.org/10.3390/ijms25031566. (colaco2024mannoseandlactobionic pages 20-22)
- Dectin-1→PKCδ→CARD9 signaling example (CCS, Apr 2024): https://doi.org/10.1186/s12964-024-01576-z. (ganguly2024neemleafglycoprotein pages 14-16)
- Glycan challenge activating MAPK/AP-1 in human THP-1 cells (thesis, year n/a): record shows TLR/MAPK/AP-1 activation upon glycan stimuli. (kumarUnknownyearaspectsofgene pages 68-71)
- Raf-1/MAPK engagement downstream of CLRs (PhD thesis, Jan 2023): CLR signaling routes include Syk/Card9 and Raf-1, activating NF-κB/MAPK. https://doi.org/10.25673/110894. (kotrba2023mastcellsecretory pages 26-30)
- Human dataset usage of “response to lectin/cellular response to lectin” (Frontiers Immunol 2024; J Transl Med 2023; Indian J Crit Care Med 2024): https://doi.org/10.3389/fimmu.2024.1424308; https://doi.org/10.1186/s12967-023-04573-x; https://doi.org/10.5005/jp-journals-10071-24789. (colaco2024mannoseandlactobionic pages 20-22)
- p300/CBP in immune/epigenetic regulation but not specific to lectin signaling (Exp Mol Med 2023; IJMS 2023): https://doi.org/10.1038/s12276-023-01014-z; https://doi.org/10.3390/ijms241914551. (, )

References

1. (malamud2024thedectin1and pages 1-2): Mariano Malamud and G. D. Brown. The dectin-1 and dectin-2 clusters: c-type lectin receptors with fundamental roles in immunity. EMBO Reports, 25:5239-5264, Oct 2024. URL: https://doi.org/10.1038/s44319-024-00296-2, doi:10.1038/s44319-024-00296-2. This article has 15 citations and is from a highest quality peer-reviewed journal.

2. (colaco2024mannoseandlactobionic pages 20-22): Mariana Colaço, Maria T. Cruz, Luís Pereira de Almeida, and Olga Borges. Mannose and lactobionic acid in nasal vaccination: enhancing antigen delivery via c-type lectin receptors. Pharmaceutics, 16:1308, Oct 2024. URL: https://doi.org/10.3390/pharmaceutics16101308, doi:10.3390/pharmaceutics16101308. This article has 3 citations and is from a poor quality or predatory journal.

3. (ganguly2024neemleafglycoprotein pages 14-16): Nilanjan Ganguly, Tapasi Das, Avishek Bhuniya, Ipsita Guha, Mohona Chakravarti, Sukanya Dhar, Anirban Sarkar, Saurav Bera, Jesmita Dhar, Shayani Dasgupta, Akata Saha, Tithi Ghosh, Juhina Das, Ugir Hossain Sk, Saptak Banerjee, Subrata Laskar, Anamika Bose, and Rathindranath Baral. Neem leaf glycoprotein binding to dectin-1 receptors on dendritic cell induces type-1 immunity through card9 mediated intracellular signal to nfκb. Cell Communication and Signaling : CCS, Apr 2024. URL: https://doi.org/10.1186/s12964-024-01576-z, doi:10.1186/s12964-024-01576-z. This article has 3 citations.

4. (kumarUnknownyearaspectsofgene pages 68-71): K Thirnahalli Udaya Kumar. Aspects of gene regulation after glycan challenge in human thp-1 cells. Unknown journal, Unknown year.

5. (kotrba2023mastcellsecretory pages 26-30): Johanna Kotrba. Mast cell secretory granules serve as endogenous c-type lectin receptor ligands skewing dendritic cell function towards t-h2/t-h17 response. Other, Jan 2023. URL: https://doi.org/10.25673/110894, doi:10.25673/110894. This article has 0 citations.

6. (truthe2024roleoflectinlike pages 7-9): Sarah Truthe, Tilman E. Klassert, Stefan Schmelz, Danny Jonigk, Wulf Blankenfeldt, and Hortense Slevogt. Role of lectin-like oxidized low-density lipoprotein receptor-1 in inflammation and pathogen-associated interactions. Journal of Innate Immunity, 16:105-132, Jan 2024. URL: https://doi.org/10.1159/000535793, doi:10.1159/000535793. This article has 25 citations and is from a peer-reviewed journal.

## Citations

1. colaco2024mannoseandlactobionic pages 20-22
2. truthe2024roleoflectinlike pages 7-9
3. ganguly2024neemleafglycoprotein pages 14-16
4. kotrba2023mastcellsecretory pages 26-30
5. https://doi.org/10.1186/s12964-024-01576-z
6. https://doi.org/10.25673/110894
7. https://doi.org/10.3390/ijms25031566
8. https://doi.org/10.1038/s44319-024-00296-2
9. https://doi.org/10.3389/fimmu.2024.1424308
10. https://doi.org/10.1186/s12967-023-04573-x
11. https://doi.org/10.5005/jp-journals-10071-24789
12. https://doi.org/10.1038/s12276-023-01014-z
13. https://doi.org/10.3390/ijms241914551
14. https://doi.org/10.1159/000535793
15. https://doi.org/10.3390/ijms25031566.
16. https://doi.org/10.1186/s12964-024-01576-z.
17. https://doi.org/10.25673/110894.
18. https://doi.org/10.3389/fimmu.2024.1424308;
19. https://doi.org/10.1186/s12967-023-04573-x;
20. https://doi.org/10.5005/jp-journals-10071-24789.
21. https://doi.org/10.1038/s12276-023-01014-z;
22. https://doi.org/10.3390/ijms241914551.
23. https://doi.org/10.1038/s44319-024-00296-2,
24. https://doi.org/10.3390/pharmaceutics16101308,
25. https://doi.org/10.1186/s12964-024-01576-z,
26. https://doi.org/10.25673/110894,
27. https://doi.org/10.1159/000535793,