---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-02T08:22:17.544214'
end_time: '2026-10-02T08:32:44.511405'
duration_seconds: 626.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: MYCMD
  gene_id: CMU1
  gene_symbol: CMU1
  uniprot_accession: A0A0D1DWQ2
  protein_description: 'RecName: Full=Secreted chorismate mutase {ECO:0000303|PubMed:21976020};
    EC=5.4.99.5 {ECO:0000269|PubMed:21976020}; Flags: Precursor;'
  gene_info: Name=CMU1; ORFNames=UMAG_05731;
  organism_full: Mycosarcoma maydis (Corn smut fungus) (Ustilago maydis).
  protein_family: Not specified in UniProt
  protein_domains: Chorismate_II_sf. (IPR036263); CM_AroQ_sf_eucaryotic. (IPR037039)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: CMU1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: CMU1-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000012 The requested information for the effector
    Cmu1 from Table 1 on page 4 is shown in the image. It indicates that Cmu1 functions
    to s'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A0D1DWQ2
- **Protein Description:** RecName: Full=Secreted chorismate mutase {ECO:0000303|PubMed:21976020}; EC=5.4.99.5 {ECO:0000269|PubMed:21976020}; Flags: Precursor;
- **Gene Information:** Name=CMU1; ORFNames=UMAG_05731;
- **Organism (full):** Mycosarcoma maydis (Corn smut fungus) (Ustilago maydis).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Chorismate_II_sf. (IPR036263); CM_AroQ_sf_eucaryotic. (IPR037039)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CMU1" matches the protein description above**
2. **Verify the organism is correct:** Mycosarcoma maydis (Corn smut fungus) (Ustilago maydis).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CMU1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CMU1** (gene ID: CMU1, UniProt: A0A0D1DWQ2) in MYCMD.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

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

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A0D1DWQ2
- **Protein Description:** RecName: Full=Secreted chorismate mutase {ECO:0000303|PubMed:21976020}; EC=5.4.99.5 {ECO:0000269|PubMed:21976020}; Flags: Precursor;
- **Gene Information:** Name=CMU1; ORFNames=UMAG_05731;
- **Organism (full):** Mycosarcoma maydis (Corn smut fungus) (Ustilago maydis).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Chorismate_II_sf. (IPR036263); CM_AroQ_sf_eucaryotic. (IPR037039)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CMU1" matches the protein description above**
2. **Verify the organism is correct:** Mycosarcoma maydis (Corn smut fungus) (Ustilago maydis).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CMU1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CMU1** (gene ID: CMU1, UniProt: A0A0D1DWQ2) in MYCMD.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: fungal CMU1

## Identity and principal function

**CMU1** here denotes the *Ustilago maydis* (also named *Mycosarcoma maydis*) corn-smut effector **Cmu1**, specified in the question as ORF **UMAG_05731**, UniProt **A0A0D1DWQ2**. The organism, symbol, and description agree with the Cmu1 studied in the *U. maydis*–maize literature. The supplied chorismate-mutase domain annotations are consistent with its experimentally established AroQ-class enzyme structure; the accession-to-ORF mapping and exact domain identifiers were supplied with the question rather than independently established from the retrieved papers. This report does not attribute findings from similarly named proteins in other fungi to this gene. (han2019akiwellindisarms pages 1-2, han2019akiwellindisarms pages 6-11, yu2023progressinpathogenesis pages 4-5)

**Primary molecular function:** Cmu1 catalyses the chorismate-mutase reaction **chorismate → prephenate** (EC 5.4.99.5), a branch point connecting chorismate metabolism to phenylalanine and tyrosine biosynthesis. Purified Cmu1 activity has been measured by following chorismate disappearance; crystallography identifies a homodimeric AroQ-type enzyme with two active sites. **Chorismate is the experimentally supported substrate**; the available studies do not establish a broader substrate range. Unlike the comparator yeast and maize chorismate mutases tested, Cmu1 was not regulated by tryptophan or tyrosine in the reported assays. (han2019akiwellindisarms pages 1-2, han2019akiwellindisarms pages 2-3, han2019akiwellindisarms pages 5-6)

The following evidence summary separates direct observations from the metabolic model they support.

| Claim | Experimental support | Caveat |
|---|---|---|
| Fungal *Ustilago maydis* Cmu1 catalyzes chorismate → prephenate. | Purified Cmu1 displayed chorismate-mutase activity in a spectrophotometric assay monitoring chorismate disappearance; structural analysis classified it as a homodimeric AroQ-class chorismate mutase with conserved catalytic residues (Han et al., 2019). (han2019akiwellindisarms pages 1-2, han2019akiwellindisarms pages 5-6) | Direct evidence establishes activity toward chorismate; comparative assays against a broad substrate panel were not reported, so broader substrate specificity is unresolved. |
| Cmu1 acts in host cells with maize chorismate mutases and suppresses salicylic-acid accumulation. | Cmu1 is translocated into maize cells and interacts with ZmCM1/ZmCM2; reviews of Djamei et al. (2011) report that Δ*cmu1* infection produced an approximately tenfold increase in salicylic acid and reduced virulence/tumour formation (Bauters et al., 2021; Yu et al., 2023). (bauters2021pathogenspullingthe pages 2-4, yu2023progressinpathogenesis pages 4-5) | The quantitative mutant result is reported here through later reviews of the 2011 primary study. Interaction and host-cytoplasmic localization are supported, but direct metabolic-flux measurements are lacking. |
| Maize ZmKWL1 specifically binds and inhibits fungal Cmu1. | Co-immunoprecipitation and purified-protein pull-down supported binding. ZmKWL1 reduced Cmu1 activity from **40.8 ± 2.4** to **21.2 ± 1.7 µmol min⁻¹ mg⁻¹**, while *K*<sub>m</sub> remained essentially unchanged (**0.80 ± 0.10** versus **0.83 ± 0.15 mM**), consistent with inhibition of catalytic output rather than reduced chorismate affinity (Han et al., 2019). (han2019akiwellindisarms pages 2-3, han2019akiwellindisarms pages 3-3) | The unchanged *K*<sub>m</sub> supports noncompetitive/catalytic inhibition, while structural data additionally indicate obstruction near the active site; these descriptions are complementary rather than proof of a single classical kinetic mechanism. |
| Apoplastic interception by ZmKWL1 and diversion of host chorismate away from salicylic-acid biosynthesis are mechanistic models. | ZmKWL1 has a secretion signal and can inhibit Cmu1, supporting a model in which it captures Cmu1 in the apoplast before host-cell entry. Enzyme, mutant-SA, and virulence data support the broader chorismate-diversion model (Han et al., 2019; Bauters et al., 2021). (han2019akiwellindisarms pages 3-4, han2019manipulationofphytohormone pages 1-2, bauters2021pathogenspullingthe pages 2-4) | Apoplastic restriction of Cmu1 entry was proposed rather than directly demonstrated. Flux from chorismate through prephenate versus isochorismate/SA was not directly traced, so the exact in-planta redistribution remains inferential. |


*Table: Evidence supporting the catalytic activity, host-cell action, and ZmKWL1-mediated inhibition of fungal Cmu1. The table distinguishes direct experimental results from proposed localization and metabolic-flux mechanisms.*

## Biological pathway and site of action

Cmu1 is made by the **fungus as a secreted precursor**, reaches the maize–fungus interface, and has been reported to enter **host cells**, where the plant cytoplasm is an important site of action. The 2023 review lists the live nutrition interface/plant cytoplasm and identifies maize chorismate mutases **ZmCM1 and ZmCM2** as interaction partners. These are host enzymes, **not** alternate names for fungal Cmu1. One review additionally reports Cmu1 in the host nucleus; the strongest mechanistic localization for the chorismate-mutase interaction remains the host cytoplasm. (yu2023progressinpathogenesis pages 4-5, yu2023progressinpathogenesis media 2ace0c33, bauters2021pathogenspullingthe pages 2-4)

The accepted **working model** is that fungal Cmu1, acting alongside host chorismate mutase, increases conversion of chorismate to prephenate and thereby reduces chorismate available to the competing isochorismate-dependent **salicylic-acid (SA) defence pathway**. This is a biochemical explanation for its effect on immunity, **not a directly measured in-planta flux map**: the cited reviews explicitly present diversion and any depletion of particular cellular chorismate pools as proposed mechanisms. Likewise, Cmu1 is an enzyme that affects SA accumulation, not an SA receptor or a demonstrated direct modifier of SA-signalling proteins. (han2019manipulationofphytohormone pages 1-2, bauters2021pathogenspullingthe pages 2-4, wildermuth2019plantsfightfungi pages 2-2)

Genetic and metabolite findings support the biological consequence. Reviews describing the original deletion experiments report that maize infected with **Δcmu1** fungus accumulates approximately **tenfold more SA** than maize infected with the corresponding Cmu1-producing fungus; deletion also reduces virulence and tumour formation. The approximate fold change is reported through a later review because the full text of the original study was not available for independent inspection here. The founding primary report is Djamei *et al.*, **“Metabolic priming by a secreted fungal effector,”** *Nature* **478**, 395–398 (October 2011), https://doi.org/10.1038/nature10454. (han2019manipulationofphytohormone pages 1-2, bauters2021pathogenspullingthe pages 2-4, yu2023progressinpathogenesis pages 4-5)

## Host countermeasure and biochemical specificity

Maize **ZmKWL1**, a kiwellin defence protein, binds fungal Cmu1: Han *et al.* detected association with Cmu1 recovered from infected leaves and confirmed direct association with purified proteins. Structural work places kiwellin against the Cmu1 homodimer near its active sites, with a kiwellin loop contacting the active-site region. In purified-enzyme measurements, ZmKWL1 lowered reported Cmu1 activity from **40.8 ± 2.4 to 21.2 ± 1.7 µmol min⁻¹ mg⁻¹**, while measured chorismate *K*m was essentially unchanged (**0.80 ± 0.10 versus 0.83 ± 0.15 mM**). This supports impaired catalytic output rather than a measurable decrease in apparent substrate affinity under those assay conditions. The interaction exploits structural features of fungal Cmu1; ZmKWL1 did not comparably inhibit the tested endogenous maize chorismate mutases or yeast Aro7p. (han2019akiwellindisarms pages 3-4, han2019akiwellindisarms pages 2-3, wildermuth2019plantsfightfungi pages 2-2, han2019akiwellindisarms pages 3-3)

ZmKWL1 has a secretion signal, making **interception of Cmu1 in the apoplast** a plausible additional spatial aspect of defence. However, the suggestion that kiwellin binding *prevents Cmu1 entering the host cytoplasm* should not be stated as a demonstrated transport mechanism. Reducing ZmKWL1 expression by virus-induced gene silencing increased maize susceptibility in the reported infection assay; this was **silencing, not a maize knockout**. These results establish a specific host antagonist and support Cmu1 as an experimentally tractable virulence mechanism, but do not themselves constitute a field-validated crop-protection implementation. Han *et al.*, **“A kiwellin disarms the metabolic activity of a secreted fungal virulence factor,”** *Nature* **565**, 650–653 (January 2019), https://doi.org/10.1038/s41586-018-0857-9. (han2019akiwellindisarms pages 1-2, han2019akiwellindisarms pages 3-4, wildermuth2019plantsfightfungi pages 2-2)

Efficient secretion also depends on fungal secretory machinery: the ER co-chaperone **Dnj1** has been reported as required for Cmu1 secretion under ER stress. This identifies a production/secretion dependency, **not** an alternative site of Cmu1’s catalytic action. Hampel *et al.*, *PLOS ONE* **11**, e0153861 (April 2016), https://doi.org/10.1371/journal.pone.0153861. (hampel2016unfoldedproteinresponse pages 11-12)

## Recent literature and limits of the annotation

The relevant **2023** synthesis by Yu *et al.* continues to identify Cmu1 as a secreted effector targeting maize ZmCM1/ZmCM2, associated with SA suppression and reduced disease when deleted; its tabulated localization is the live nutrition interface/plant cytoplasm. It summarizes earlier functional studies rather than providing a new Cmu1 catalytic assay. Yu *et al.*, *Molecular Plant Pathology* **24**, 495–509 (February 2023), https://doi.org/10.1111/mpp.13307. A separate **2023** primary study used the *cmu1* promoter and signal peptide in an experimental control, but investigated the **different fungal protein Cpl1**; its chitin-binding or cell-wall functions must not be assigned to Cmu1. Weiland *et al.*, *Molecular Plant Pathology* **24**, 768–787 (May 2023), https://doi.org/10.1111/mpp.13349. (weiland2023structuralandfunctional pages 10-12, yu2023progressinpathogenesis pages 4-5, yu2023progressinpathogenesis media 2ace0c33)

**Annotation conclusion:** CMU1 encodes a **secreted, host-translocated chorismate-to-prephenate mutase** whose best-supported functional role during maize infection is alteration of host chorismate metabolism and suppression of SA-associated defence. Purified-enzyme catalysis, host protein interactions, and infection-associated SA/virulence phenotypes are experimentally supported; the exact intracellular metabolic flux and the extent of apoplastic interception remain unresolved. The retrieved 2023–2024 material did not establish a newer, target-specific mechanism that supersedes the foundational 2011 and 2019 findings. (han2019akiwellindisarms pages 1-2, bauters2021pathogenspullingthe pages 2-4, yu2023progressinpathogenesis pages 4-5, han2019akiwellindisarms pages 3-3)

References

1. (han2019akiwellindisarms pages 1-2): Xiaowei Han, Florian Altegoer, Wieland Steinchen, Lynn Binnebesel, Jan Schuhmacher, Timo Glatter, Pietro I. Giammarinaro, Armin Djamei, Stefan A. Rensing, Stefanie Reissmann, Regine Kahmann, and Gert Bange. A kiwellin disarms the metabolic activity of a secreted fungal virulence factor. Jan 2019. URL: https://doi.org/10.1038/s41586-018-0857-9, doi:10.1038/s41586-018-0857-9. This article has 84 citations and is from a highest quality peer-reviewed journal.

2. (han2019akiwellindisarms pages 6-11): Xiaowei Han, Florian Altegoer, Wieland Steinchen, Lynn Binnebesel, Jan Schuhmacher, Timo Glatter, Pietro I. Giammarinaro, Armin Djamei, Stefan A. Rensing, Stefanie Reissmann, Regine Kahmann, and Gert Bange. A kiwellin disarms the metabolic activity of a secreted fungal virulence factor. Jan 2019. URL: https://doi.org/10.1038/s41586-018-0857-9, doi:10.1038/s41586-018-0857-9. This article has 84 citations and is from a highest quality peer-reviewed journal.

3. (yu2023progressinpathogenesis pages 4-5): Chun-Man Yu, Jianzhao Qi, Haiyan Han, Pengchao Wang, and Chengwei Liu. Progress in pathogenesis research of ustilago maydis, and the metabolites involved along with their biosynthesis. Molecular Plant Pathology, 24:495-509, Feb 2023. URL: https://doi.org/10.1111/mpp.13307, doi:10.1111/mpp.13307. This article has 42 citations and is from a peer-reviewed journal.

4. (han2019akiwellindisarms pages 2-3): Xiaowei Han, Florian Altegoer, Wieland Steinchen, Lynn Binnebesel, Jan Schuhmacher, Timo Glatter, Pietro I. Giammarinaro, Armin Djamei, Stefan A. Rensing, Stefanie Reissmann, Regine Kahmann, and Gert Bange. A kiwellin disarms the metabolic activity of a secreted fungal virulence factor. Jan 2019. URL: https://doi.org/10.1038/s41586-018-0857-9, doi:10.1038/s41586-018-0857-9. This article has 84 citations and is from a highest quality peer-reviewed journal.

5. (han2019akiwellindisarms pages 5-6): Xiaowei Han, Florian Altegoer, Wieland Steinchen, Lynn Binnebesel, Jan Schuhmacher, Timo Glatter, Pietro I. Giammarinaro, Armin Djamei, Stefan A. Rensing, Stefanie Reissmann, Regine Kahmann, and Gert Bange. A kiwellin disarms the metabolic activity of a secreted fungal virulence factor. Jan 2019. URL: https://doi.org/10.1038/s41586-018-0857-9, doi:10.1038/s41586-018-0857-9. This article has 84 citations and is from a highest quality peer-reviewed journal.

6. (bauters2021pathogenspullingthe pages 2-4): Lander Bauters, Boris Stojilković, and Godelieve Gheysen. Pathogens pulling the strings: effectors manipulating salicylic acid and phenylpropanoid biosynthesis in plants. Molecular Plant Pathology, 22:1436-1448, Aug 2021. URL: https://doi.org/10.1111/mpp.13123, doi:10.1111/mpp.13123. This article has 87 citations and is from a peer-reviewed journal.

7. (han2019akiwellindisarms pages 3-3): Xiaowei Han, Florian Altegoer, Wieland Steinchen, Lynn Binnebesel, Jan Schuhmacher, Timo Glatter, Pietro I. Giammarinaro, Armin Djamei, Stefan A. Rensing, Stefanie Reissmann, Regine Kahmann, and Gert Bange. A kiwellin disarms the metabolic activity of a secreted fungal virulence factor. Jan 2019. URL: https://doi.org/10.1038/s41586-018-0857-9, doi:10.1038/s41586-018-0857-9. This article has 84 citations and is from a highest quality peer-reviewed journal.

8. (han2019akiwellindisarms pages 3-4): Xiaowei Han, Florian Altegoer, Wieland Steinchen, Lynn Binnebesel, Jan Schuhmacher, Timo Glatter, Pietro I. Giammarinaro, Armin Djamei, Stefan A. Rensing, Stefanie Reissmann, Regine Kahmann, and Gert Bange. A kiwellin disarms the metabolic activity of a secreted fungal virulence factor. Jan 2019. URL: https://doi.org/10.1038/s41586-018-0857-9, doi:10.1038/s41586-018-0857-9. This article has 84 citations and is from a highest quality peer-reviewed journal.

9. (han2019manipulationofphytohormone pages 1-2): Xiaowei Han and Regine Kahmann. Manipulation of phytohormone pathways by effectors of filamentous plant pathogens. Frontiers in Plant Science, Jun 2019. URL: https://doi.org/10.3389/fpls.2019.00822, doi:10.3389/fpls.2019.00822. This article has 214 citations.

10. (yu2023progressinpathogenesis media 2ace0c33): Chun-Man Yu, Jianzhao Qi, Haiyan Han, Pengchao Wang, and Chengwei Liu. Progress in pathogenesis research of ustilago maydis, and the metabolites involved along with their biosynthesis. Molecular Plant Pathology, 24:495-509, Feb 2023. URL: https://doi.org/10.1111/mpp.13307, doi:10.1111/mpp.13307. This article has 42 citations and is from a peer-reviewed journal.

11. (wildermuth2019plantsfightfungi pages 2-2): Mary C. Wildermuth. Plants fight fungi using kiwellin proteins. Nature, 565:575-577, Jan 2019. URL: https://doi.org/10.1038/d41586-019-00092-2, doi:10.1038/d41586-019-00092-2. This article has 12 citations and is from a highest quality peer-reviewed journal.

12. (hampel2016unfoldedproteinresponse pages 11-12): Martin Hampel, Mareike Jakobi, Lara Schmitz, Ute Meyer, Florian Finkernagel, Gunther Doehlemann, and Kai Heimel. Unfolded protein response (upr) regulator cib1 controls expression of genes encoding secreted virulence factors in ustilago maydis. PLoS ONE, 11:e0153861, Apr 2016. URL: https://doi.org/10.1371/journal.pone.0153861, doi:10.1371/journal.pone.0153861. This article has 32 citations and is from a peer-reviewed journal.

13. (weiland2023structuralandfunctional pages 10-12): Paul Weiland, Felix Dempwolff, Wieland Steinchen, Sven‐Andreas Freibert, Hui Tian, Timo Glatter, Roman Martin, Bart P. H. J. Thomma, Gert Bange, and Florian Altegoer. Structural and functional analysis of the cerato‐platanin‐like protein cpl1 suggests diverging functions in smut fungi. Molecular Plant Pathology, 24:768-787, May 2023. URL: https://doi.org/10.1111/mpp.13349, doi:10.1111/mpp.13349. This article has 22 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CMU1-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000012 The requested information for the effector Cmu1 from Table 1 on page 4 is shown in the image. It indicates that Cmu1 functions to s](CMU1-deep-research-falcon_artifacts/image-1.png)

## Citations

1. hampel2016unfoldedproteinresponse pages 11-12
2. han2019akiwellindisarms pages 1-2
3. han2019akiwellindisarms pages 6-11
4. yu2023progressinpathogenesis pages 4-5
5. han2019akiwellindisarms pages 2-3
6. han2019akiwellindisarms pages 5-6
7. bauters2021pathogenspullingthe pages 2-4
8. han2019akiwellindisarms pages 3-3
9. han2019akiwellindisarms pages 3-4
10. han2019manipulationofphytohormone pages 1-2
11. wildermuth2019plantsfightfungi pages 2-2
12. weiland2023structuralandfunctional pages 10-12
13. https://doi.org/10.1038/nature10454.
14. https://doi.org/10.1038/s41586-018-0857-9.
15. https://doi.org/10.1371/journal.pone.0153861.
16. https://doi.org/10.1111/mpp.13307.
17. https://doi.org/10.1111/mpp.13349.
18. https://doi.org/10.1038/s41586-018-0857-9,
19. https://doi.org/10.1111/mpp.13307,
20. https://doi.org/10.1111/mpp.13123,
21. https://doi.org/10.3389/fpls.2019.00822,
22. https://doi.org/10.1038/d41586-019-00092-2,
23. https://doi.org/10.1371/journal.pone.0153861,
24. https://doi.org/10.1111/mpp.13349,