---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-01T19:49:16.349642'
end_time: '2025-12-01T19:56:47.307710'
duration_seconds: 450.96
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00089175
  rule_type: arba
  go_terms: GO:1990849 (vacuolar localization)
  conditions_summary: '**Condition Set 1:** FunFam id: pleckstrin homology domain-containing
    family M member 1 isoform X1 (CATH.FunFam:1.20.58.900:FF:000013) AND FunFam id:
    pleckstrin homology domain-containing family M member 1 isoform X1 (CATH.FunFam:2.30.29.30:FF:000315)
    AND taxon: Eukaryota (NCBITaxon:2759)'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00089175
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990849 (vacuolar localization)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: pleckstrin homology domain-containing family M member 1 isoform X1 (CATH.FunFam:1.20.58.900:FF:000013) AND FunFam id: pleckstrin homology domain-containing family M member 1 isoform X1 (CATH.FunFam:2.30.29.30:FF:000315) AND taxon: Eukaryota (NCBITaxon:2759)

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

For the predicted GO term(s) **GO:1990849 (vacuolar localization)**:
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

- **Rule ID:** ARBA00089175
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990849 (vacuolar localization)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: pleckstrin homology domain-containing family M member 1 isoform X1 (CATH.FunFam:1.20.58.900:FF:000013) AND FunFam id: pleckstrin homology domain-containing family M member 1 isoform X1 (CATH.FunFam:2.30.29.30:FF:000315) AND taxon: Eukaryota (NCBITaxon:2759)

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

For the predicted GO term(s) **GO:1990849 (vacuolar localization)**:
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
ARBA00089175 links proteins in two CATH FunFams labeled for “pleckstrin homology domain-containing family M member 1 isoform X1” (i.e., PLEKHM1-like) in Eukaryota to GO:1990849 (vacuolar localization). Current evidence supports that PLEKHM1 is a Rab7/Arl8 effector and multivalent adaptor that promotes autophagosome–lysosome and late endosome–lysosome tethering/fusion via HOPS and LC3/GABARAP, with steady-state localization on late endosome/lysosome compartments in animals. However, “vacuolar localization” is a process term most applicable to organisms with a vacuole (fungi/plants), whereas in animals the equivalent organelle is the lysosome. The prediction should be taxonomically nuanced: support for lysosomal localization/process in Metazoa is strong, but mapping to vacuolar localization across all eukaryotes on the basis of PH and RUN family membership alone risks false positives because PH and RUN domains are multifunctional and widespread. We recommend replacing/augmenting the rule with taxa-specific CC and BP terms and additional domain/motif constraints to reduce false positives (see Recommendations). (schleinitz2023consecutivefunctionsof pages 1-3, ke2024molecularmechanismof pages 7-8, schleinitz2023consecutivefunctionsof pages 10-12, das2024molecularandfunctional pages 5-6, walia2024sarscov2virulencefactor pages 1-2, walia2024sarscov2virulencefactor pages 2-4, diao2024molecularstructuresand pages 7-9, diao2024molecularstructuresand pages 12-13)

2. Domain Analysis
- PLEKHM1 architecture and core biology: Reviews and recent primary work describe PLEKHM1 (pleckstrin homology and RUN domain-containing M1) as a multivalent adaptor: an N‑terminal PH domain, central RUN domain(s), a C‑terminal Rubicon-homology (RH) region that binds Rab7, and a canonical LC3‑interacting region (LIR). PLEKHM1 bridges Rab7-positive late endosomes to Arl8b/HOPS-positive lysosomes and binds LC3/GABARAP, promoting autophagosome–lysosome fusion. Structural data show the LIR binds the LC3B LDS in a canonical manner; the RUN region has been implicated in Arl8b binding and the RH domain in Rab7 binding, though the detailed structural basis for HOPS binding via RUN needs further definition. (Autophagy Reports, Feb 2024; https://doi.org/10.1080/27694127.2024.2305594) (diao2024molecularstructuresand pages 7-9, diao2024molecularstructuresand pages 12-13)
- Interactions and functional positioning: PLEKHM1 is considered a dual Rab7/Arl8 effector that operates with HOPS during late endosome–lysosome and autophagosome–lysosome tethering. Cell Reports (Jan 2023) positions PLEKHM1 among the Rab7/Arl8 effectors in the HOPS network; it suggests PLEKHM1 does not recruit HOPS in the absence of Arl8, highlighting Arl8 dependence for HOPS engagement. (Cell Reports, Jan 31, 2023; https://doi.org/10.1016/j.celrep.2022.111969) (schleinitz2023consecutivefunctionsof pages 1-3, schleinitz2023consecutivefunctionsof pages 10-12)
- PH and RUN domain diagnosticity: PH domains are common lipid-binding modules across many cellular pathways; presence is not diagnostic for vacuolar/lysosomal localization. RUN domains broadly interact with small GTPases (Rap, Rab, Ral/Arl families), with PLEKHM1’s RUN involved in ARL8B engagement, but RUN domains exist in many proteins with diverse roles. Thus, neither PH nor RUN domains alone diagnose vacuolar/lysosomal localization. The PLEKHM family’s RH domain and LIR motif provide more specific linkage to endolysosomal/autophagy fusion machinery. (Autophagy Reports, Feb 2024; https://doi.org/10.1080/27694127.2024.2305594) (diao2024molecularstructuresand pages 7-9, diao2024molecularstructuresand pages 12-13)
- Subfamilies and multifunctionality: PLEKHM1 is one of several PLEKHM proteins; evidence shows tissue- and pathway-specific roles (e.g., osteoclast bone resorption and lysosome trafficking depend on PLEKHM1–Rab7 via the RH domain), and PLEKHM1 is subject to regulation (e.g., by lipids and ubiquitination) with context-dependent effects on fusion. This indicates multifunctionality across cell types and contexts; subfamily members may have distinct partners or regulatory inputs. (JBMR Plus, Mar 2024; https://doi.org/10.1093/jbmrpl/ziae034; Cells, Mar 2024; https://doi.org/10.3390/cells13060500; Nat Commun, Jan 2024; https://doi.org/10.1038/s41467-023-44316-6) (das2024molecularandfunctional pages 5-6, ke2024molecularmechanismof pages 7-8, jeong2024tmem55blinksautophagy pages 1-2, jeong2024tmem55blinksautophagy pages 2-3)

3. GO Term Evaluation
- Predicted term: GO:1990849 (vacuolar localization) refers to the process by which any material or protein is localized to the vacuole. In fungi/plants, “vacuole” is the lytic organelle. In animals, the analogous organelle is the lysosome, and the appropriate localization process term would be lysosome-directed, while the CC location is “lysosome.” Literature for PLEKHM1 overwhelmingly comes from animals, showing localization to late endosome/lysosome and roles in autophagosome–lysosome fusion. Thus, a blanket Eukaryota vacuolar localization prediction is taxonomically imprecise. (Cell Reports, 2023; Nat Commun, 2024; Autophagy Reports, 2024) (schleinitz2023consecutivefunctionsof pages 1-3, walia2024sarscov2virulencefactor pages 1-2, walia2024sarscov2virulencefactor pages 2-4, diao2024molecularstructuresand pages 7-9, diao2024molecularstructuresand pages 12-13)
- Too broad or too narrow? As a process term, “vacuolar localization” is broad and agnostic to mechanism. For PLEKHM1-like proteins in animals, stronger and more specific evidence supports “autophagosome–lysosome fusion” and “late endosome–lysosome fusion” processes and CC localization to lysosome, rather than a vacuolar localization process term. (Cells, 2024; Cell Reports, 2023; Nat Commun, 2023/2024) (ke2024molecularmechanismof pages 7-8, schleinitz2023consecutivefunctionsof pages 1-3, zhang2023c9orf72catalyzedgtploading pages 6-8, zhang2023c9orf72catalyzedgtploading pages 8-9, walia2024sarscov2virulencefactor pages 1-2)
- Better alternatives:
  • Animals (Metazoa): CC “lysosome” (GO:0005764) and “lysosomal membrane” (GO:0005765) as appropriate; BP “autophagosome–lysosome fusion” (GO:0097352) and “late endosome–lysosome fusion” or “endolysosomal transport” where supported. Evidence: PLEKHM1 on Rab7-positive LEs, connects to Arl8b/HOPS-positive lysosomes, regulates fusion. (Cell Reports, 2023; Autophagy Reports, 2024; Nat Commun, 2023) (schleinitz2023consecutivefunctionsof pages 1-3, diao2024molecularstructuresand pages 7-9, zhang2023c9orf72catalyzedgtploading pages 6-8, zhang2023c9orf72catalyzedgtploading pages 8-9)
  • Fungi/plants: If PLEKHM1 orthologs existed and were shown to function at the vacuole, “vacuole” (GO:0005773) CC and vacuole localization process could be considered. Current evidence cited here focuses on animals; cross-kingdom orthology/function is not demonstrated in these sources. (Autophagy Reports, 2024) (diao2024molecularstructuresand pages 7-9)

4. Evidence Review
- Autophagosome–lysosome fusion and multivalent binding:
  • Diao et al. (2024) review: PLEKHM1 acts as a multivalent adaptor that binds Rab7, Arl8, LC3/GABARAPs, and HOPS; contains a canonical LIR that docks into LC3B; RUN–HOPS contacts are proposed but need more structural work. Autophagosome–lysosome fusion is a central role. (Autophagy Reports, Feb 2024; https://doi.org/10.1080/27694127.2024.2305594) (diao2024molecularstructuresand pages 7-9, diao2024molecularstructuresand pages 12-13)
  • Ke (2024) review: Summarizes PLEKHM1 as a Rab7-interacting pro‑fusion factor that engages HOPS and ATG8s; highlights regulation by PI(4,5)P2 cycling and TRIM22-mediated enhancement of the PLEKHM1–GABARAP association. (Cells, Mar 2024; https://doi.org/10.3390/cells13060500) (ke2024molecularmechanismof pages 7-8)
  • Liu et al. (2025 review of 2023–2024 progress): Emphasizes PLEKHM1 as endolysosomal adaptor interfacing Rab7/HOPS/Arl8 and ATG8s, and cites recent mechanistic updates including RUN–ARL8B contacts. (Medical Review, Jun 2025; https://doi.org/10.1515/mr-2024-0095) (liu2025spatiotemporalprocessesin pages 17-18)
- Position in HOPS network and GTPase dependency:
  • Schleinitz et al. (2023): Arl8 directly and Rab7 indirectly anchor HOPS; PLEKHM1 and SKIP are dual Rab7/Arl8 effectors but likely do not recruit HOPS without Arl8, underscoring Arl8 dependence in mammals. (Cell Reports, Jan 2023; https://doi.org/10.1016/j.celrep.2022.111969) (schleinitz2023consecutivefunctionsof pages 1-3, schleinitz2023consecutivefunctionsof pages 10-12)
  • Zhang et al. (2023): Defines a Rab2–HOPS–Rab39A “hook-up” model for autophagy fusion; contextualizes prior reports where PLEKHM1 on lysosomes contributed to HOPS-mediated fusion. Although focused on Rab39A, these data reinforce the centrality of HOPS adaptors in autophagosome–lysosome fusion. (Nature Communications, Oct 2023; https://doi.org/10.1038/s41467-023-42003-0) (zhang2023c9orf72catalyzedgtploading pages 6-8, zhang2023c9orf72catalyzedgtploading pages 8-9)
- Regulation and stress/pathogen modulation:
  • Walia et al. (2024): SARS‑CoV‑2 ORF3a disrupts the HOPS–PLEKHM1 interaction, enhances PLEKHM1–Rab7 on late endosomes, and reduces tethering of Rab7 and Arl8b compartments, impairing endolysosome formation; directly links PLEKHM1’s complex to lysosomal dysfunction during infection. (Nature Communications, Mar 2024; https://doi.org/10.1038/s41467-024-46417-2) (walia2024sarscov2virulencefactor pages 1-2, walia2024sarscov2virulencefactor pages 2-4)
  • Jeong et al. (2024): TMEM55B recruits NEDD4-like ligases to lysosomes, promoting PLEKHM1 ubiquitination and proteasomal degradation under oxidative stress, halting autophagosome–lysosome fusion; confirms co-localization of TMEM55B and PLEKHM1 in Rab7-positive compartments. (Nature Communications, Jan 2024; https://doi.org/10.1038/s41467-023-44316-6) (jeong2024tmem55blinksautophagy pages 1-2, jeong2024tmem55blinksautophagy pages 2-3)
- Cell type–specific functional evidence:
  • Das et al. (2024): Structure-function mapping of PLEKHM1–Rab7 via the RH domain in osteoclasts; compound mutations reduce Rab7 binding, impair lysosome trafficking and bone resorption, highlighting physiologic relevance of PLEKHM1 at lysosomes. (JBMR Plus, Mar 2024; https://doi.org/10.1093/jbmrpl/ziae034) (das2024molecularandfunctional pages 5-6)
- Limitations/contradictions:
  • HOPS recruitment: Some studies suggest PLEKHM1 does not by itself recruit HOPS to late endosomes without Arl8, indicating context-dependent interactions and a need to avoid over-stating direct HOPS recruitment by PLEKHM1. (Cell Reports, 2023) (schleinitz2023consecutivefunctionsof pages 10-12)
  • Structural gaps: Detailed biophysical definition of RUN–HOPS contacts is incomplete; some conclusions rely on interaction mapping and functional assays rather than complete structural models. (Autophagy Reports, 2024) (diao2024molecularstructuresand pages 7-9)
  • Taxonomic scope: The cited literature largely concerns animal systems; evidence for PLEKHM1 orthologs establishing vacuole localization in fungi/plants is not provided in these sources. (Autophagy Reports, 2024) (diao2024molecularstructuresand pages 7-9)

5. Recommendations
- Taxonomic refinement: Restrict Metazoan predictions to lysosome-related CC/BP terms (e.g., CC lysosome; BP autophagosome–lysosome fusion). Only use “vacuolar localization” in taxa with vacuoles and with explicit evidence; avoid applying the vacuolar localization process term broadly to Eukaryota. (Cell Reports, 2023; Nature Communications, 2024; Autophagy Reports, 2024) (schleinitz2023consecutivefunctionsof pages 1-3, walia2024sarscov2virulencefactor pages 1-2, diao2024molecularstructuresand pages 7-9)
- Rule condition logic: PH and RUN domains are not diagnostic. To reduce false positives, add requirements for: (i) presence of a C‑terminal RH (Rubicon-homology) domain/region with Rab7-binding determinants; (ii) a canonical LIR motif; and/or (iii) coiled-coil segments involved in tethering, where available. Consider requiring co-occurrence of RUN and RH/LIR features rather than just PH/RUN domain membership. (Autophagy Reports, 2024; JBMR Plus, 2024) (diao2024molecularstructuresand pages 7-9, das2024molecularandfunctional pages 5-6)
- Alternative/supplemental GO terms: For Metazoa, CC lysosome (GO:0005764) or lysosomal membrane (GO:0005765), and BP autophagosome–lysosome fusion (GO:0097352) are better supported by the literature than the generic “vacuolar localization” process term. For fungi/plants, prefer CC vacuole (GO:0005773) and BP vacuolar localization where experimental support exists. (Cell Reports, 2023; Nature Communications, 2023/2024; Autophagy Reports, 2024) (schleinitz2023consecutivefunctionsof pages 1-3, zhang2023c9orf72catalyzedgtploading pages 6-8, walia2024sarscov2virulencefactor pages 1-2, diao2024molecularstructuresand pages 7-9)
- False positive risk and subfamily diversity: Because many PH/RUN proteins have roles unrelated to endolysosomal fusion, maintain conservative propagation. Incorporate sequence motifs/domains specific to PLEKHM1-like proteins (RH domain, LIR) and, if possible, orthology constraints to PLEKHM1/PLEKHM family rather than FunFam-level PH/RUN definitions alone. (Autophagy Reports, 2024) (diao2024molecularstructuresand pages 7-9)
- Evidence track: Where possible, prefer annotations supported by experimental interaction/localization data (Rab7/Arl8/HOPS/LC3 co-localization or co-IP) or by curated orthology to PLEKHM1, given the strong links to lysosomal fusion machinery in animals. (Nature Communications, 2024; JBMR Plus, 2024) (walia2024sarscov2virulencefactor pages 1-2, das2024molecularandfunctional pages 5-6)

URLs and publication dates
- Diao J, Yip CK, Zhong Q. Molecular structures and function of the autophagosome-lysosome fusion machinery. Autophagy Reports. Feb 2024. https://doi.org/10.1080/27694127.2024.2305594 (diao2024molecularstructuresand pages 7-9, diao2024molecularstructuresand pages 12-13)
- Schleinitz A et al. Consecutive functions of small GTPases guide HOPS-mediated tethering of late endosomes and lysosomes. Cell Reports. Jan 31, 2023. https://doi.org/10.1016/j.celrep.2022.111969 (schleinitz2023consecutivefunctionsof pages 1-3, schleinitz2023consecutivefunctionsof pages 10-12)
- Ke P‑Y. Molecular mechanism of autophagosome–lysosome fusion in mammalian cells. Cells. Mar 2024. https://doi.org/10.3390/cells13060500 (ke2024molecularmechanismof pages 7-8)
- Zhang S et al. C9orf72-catalyzed GTP loading of Rab39A enables HOPS-mediated membrane tethering and fusion in mammalian autophagy. Nature Communications. Oct 2023. https://doi.org/10.1038/s41467-023-42003-0 (zhang2023c9orf72catalyzedgtploading pages 6-8, zhang2023c9orf72catalyzedgtploading pages 8-9)
- Das BK et al. Molecular and functional mapping of Plekhm1–Rab7 interaction in osteoclasts. JBMR Plus. Mar 2024. https://doi.org/10.1093/jbmrpl/ziae034 (das2024molecularandfunctional pages 5-6)
- Walia K et al. SARS-CoV-2 ORF3a blocks lysosome function by modulating TBC1D5-dependent Rab7 cycle. Nature Communications. Mar 2024. https://doi.org/10.1038/s41467-024-46417-2 (walia2024sarscov2virulencefactor pages 1-2, walia2024sarscov2virulencefactor pages 2-4)
- Jeong E et al. TMEM55B links autophagy flux, lysosomal repair, and TFE3 activation in response to oxidative stress. Nature Communications. Jan 2024. https://doi.org/10.1038/s41467-023-44316-6 (jeong2024tmem55blinksautophagy pages 1-2, jeong2024tmem55blinksautophagy pages 2-3)

References

1. (schleinitz2023consecutivefunctionsof pages 1-3): Ariane Schleinitz, Lara-Alina Pöttgen, Tal Keren-Kaplan, Jing Pu, Paul Saftig, Juan S. Bonifacino, Albert Haas, and Andreas Jeschke. Consecutive functions of small gtpases guide hops-mediated tethering of late endosomes and lysosomes. Cell reports, 42:111969-111969, Jan 2023. URL: https://doi.org/10.1016/j.celrep.2022.111969, doi:10.1016/j.celrep.2022.111969. This article has 49 citations and is from a highest quality peer-reviewed journal.

2. (ke2024molecularmechanismof pages 7-8): Po-Yuan Ke. Molecular mechanism of autophagosome–lysosome fusion in mammalian cells. Cells, 13:500, Mar 2024. URL: https://doi.org/10.3390/cells13060500, doi:10.3390/cells13060500. This article has 48 citations and is from a poor quality or predatory journal.

3. (schleinitz2023consecutivefunctionsof pages 10-12): Ariane Schleinitz, Lara-Alina Pöttgen, Tal Keren-Kaplan, Jing Pu, Paul Saftig, Juan S. Bonifacino, Albert Haas, and Andreas Jeschke. Consecutive functions of small gtpases guide hops-mediated tethering of late endosomes and lysosomes. Cell reports, 42:111969-111969, Jan 2023. URL: https://doi.org/10.1016/j.celrep.2022.111969, doi:10.1016/j.celrep.2022.111969. This article has 49 citations and is from a highest quality peer-reviewed journal.

4. (das2024molecularandfunctional pages 5-6): Bhaba K Das, Tarun Minocha, Mikaela D Kunika, Aarthi Kannan, Ling Gao, Subburaman Mohan, Weirong Xing, Kottayil I Varughese, and Haibo Zhao. Molecular and functional mapping of plekhm1-rab7 interaction in osteoclasts. JBMR plus, 8 5:ziae034, Mar 2024. URL: https://doi.org/10.1093/jbmrpl/ziae034, doi:10.1093/jbmrpl/ziae034. This article has 5 citations and is from a peer-reviewed journal.

5. (walia2024sarscov2virulencefactor pages 1-2): Kshitiz Walia, Abhishek Sharma, Sankalita Paul, Priya Chouhan, Gaurav Kumar, Rajesh Ringe, Mahak Sharma, and Amit Tuli. Sars-cov-2 virulence factor orf3a blocks lysosome function by modulating tbc1d5-dependent rab7 gtpase cycle. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46417-2, doi:10.1038/s41467-024-46417-2. This article has 44 citations and is from a highest quality peer-reviewed journal.

6. (walia2024sarscov2virulencefactor pages 2-4): Kshitiz Walia, Abhishek Sharma, Sankalita Paul, Priya Chouhan, Gaurav Kumar, Rajesh Ringe, Mahak Sharma, and Amit Tuli. Sars-cov-2 virulence factor orf3a blocks lysosome function by modulating tbc1d5-dependent rab7 gtpase cycle. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46417-2, doi:10.1038/s41467-024-46417-2. This article has 44 citations and is from a highest quality peer-reviewed journal.

7. (diao2024molecularstructuresand pages 7-9): Jiajie Diao, Calvin K. Yip, and Qing Zhong. Molecular structures and function of the autophagosome-lysosome fusion machinery. Autophagy Reports, Feb 2024. URL: https://doi.org/10.1080/27694127.2024.2305594, doi:10.1080/27694127.2024.2305594. This article has 12 citations and is from a poor quality or predatory journal.

8. (diao2024molecularstructuresand pages 12-13): Jiajie Diao, Calvin K. Yip, and Qing Zhong. Molecular structures and function of the autophagosome-lysosome fusion machinery. Autophagy Reports, Feb 2024. URL: https://doi.org/10.1080/27694127.2024.2305594, doi:10.1080/27694127.2024.2305594. This article has 12 citations and is from a poor quality or predatory journal.

9. (jeong2024tmem55blinksautophagy pages 1-2): Eutteum Jeong, Rose Willett, Alberto Rissone, Martina La Spina, and Rosa Puertollano. Tmem55b links autophagy flux, lysosomal repair, and tfe3 activation in response to oxidative stress. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44316-6, doi:10.1038/s41467-023-44316-6. This article has 18 citations and is from a highest quality peer-reviewed journal.

10. (jeong2024tmem55blinksautophagy pages 2-3): Eutteum Jeong, Rose Willett, Alberto Rissone, Martina La Spina, and Rosa Puertollano. Tmem55b links autophagy flux, lysosomal repair, and tfe3 activation in response to oxidative stress. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44316-6, doi:10.1038/s41467-023-44316-6. This article has 18 citations and is from a highest quality peer-reviewed journal.

11. (zhang2023c9orf72catalyzedgtploading pages 6-8): Shen Zhang, Mindan Tong, Denghao Zheng, Huiying Huang, Linsen Li, Christian Ungermann, Yi Pan, Hanyan Luo, Ming Lei, Zaiming Tang, Wan Fu, She Chen, Xiaoxia Liu, and Qing Zhong. C9orf72-catalyzed gtp loading of rab39a enables hops-mediated membrane tethering and fusion in mammalian autophagy. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42003-0, doi:10.1038/s41467-023-42003-0. This article has 27 citations and is from a highest quality peer-reviewed journal.

12. (zhang2023c9orf72catalyzedgtploading pages 8-9): Shen Zhang, Mindan Tong, Denghao Zheng, Huiying Huang, Linsen Li, Christian Ungermann, Yi Pan, Hanyan Luo, Ming Lei, Zaiming Tang, Wan Fu, She Chen, Xiaoxia Liu, and Qing Zhong. C9orf72-catalyzed gtp loading of rab39a enables hops-mediated membrane tethering and fusion in mammalian autophagy. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42003-0, doi:10.1038/s41467-023-42003-0. This article has 27 citations and is from a highest quality peer-reviewed journal.

13. (liu2025spatiotemporalprocessesin pages 17-18): Shizuo Liu, Huan Yan, Jiajie Diao, Shen Zhang, and Qing Zhong. Spatio-temporal processes in autophagosome-lysosome fusion. Medical Review, 5:297-317, Jun 2025. URL: https://doi.org/10.1515/mr-2024-0095, doi:10.1515/mr-2024-0095. This article has 0 citations.

## Citations

1. diao2024molecularstructuresand pages 7-9
2. ke2024molecularmechanismof pages 7-8
3. liu2025spatiotemporalprocessesin pages 17-18
4. das2024molecularandfunctional pages 5-6
5. schleinitz2023consecutivefunctionsof pages 10-12
6. schleinitz2023consecutivefunctionsof pages 1-3
7. diao2024molecularstructuresand pages 12-13
8. https://doi.org/10.1080/27694127.2024.2305594
9. https://doi.org/10.1016/j.celrep.2022.111969
10. https://doi.org/10.1093/jbmrpl/ziae034;
11. https://doi.org/10.3390/cells13060500;
12. https://doi.org/10.1038/s41467-023-44316-6
13. https://doi.org/10.3390/cells13060500
14. https://doi.org/10.1515/mr-2024-0095
15. https://doi.org/10.1038/s41467-023-42003-0
16. https://doi.org/10.1038/s41467-024-46417-2
17. https://doi.org/10.1093/jbmrpl/ziae034
18. https://doi.org/10.1016/j.celrep.2022.111969,
19. https://doi.org/10.3390/cells13060500,
20. https://doi.org/10.1093/jbmrpl/ziae034,
21. https://doi.org/10.1038/s41467-024-46417-2,
22. https://doi.org/10.1080/27694127.2024.2305594,
23. https://doi.org/10.1038/s41467-023-44316-6,
24. https://doi.org/10.1038/s41467-023-42003-0,
25. https://doi.org/10.1515/mr-2024-0095,