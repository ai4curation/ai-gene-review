---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-31T23:44:49.172109'
end_time: '2026-05-31T23:52:00.666158'
duration_seconds: 431.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: rat
  gene_id: Gss
  gene_symbol: Gss
  uniprot_accession: P46413
  protein_description: 'RecName: Full=Glutathione synthetase {ECO:0000303|PubMed:7862666};
    Short=GSH synthetase; Short=GSH-S; EC=6.3.2.3 {ECO:0000269|PubMed:7862666}; AltName:
    Full=Glutathione synthase;'
  gene_info: Name=Gss {ECO:0000312|RGD:2752};
  organism_full: Rattus norvegicus (Rat).
  protein_family: Belongs to the eukaryotic GSH synthase family.
  protein_domains: Glutathione_synthase. (IPR005615); Glutathione_synthase_a-hlx.
    (IPR014042); Glutathione_synthase_C_euk. (IPR014709); Glutathione_synthase_N_euk.
    (IPR014049); GSH-S_sub-bd_sf. (IPR037013)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Gss-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P46413
- **Protein Description:** RecName: Full=Glutathione synthetase {ECO:0000303|PubMed:7862666}; Short=GSH synthetase; Short=GSH-S; EC=6.3.2.3 {ECO:0000269|PubMed:7862666}; AltName: Full=Glutathione synthase;
- **Gene Information:** Name=Gss {ECO:0000312|RGD:2752};
- **Organism (full):** Rattus norvegicus (Rat).
- **Protein Family:** Belongs to the eukaryotic GSH synthase family.
- **Key Domains:** Glutathione_synthase. (IPR005615); Glutathione_synthase_a-hlx. (IPR014042); Glutathione_synthase_C_euk. (IPR014709); Glutathione_synthase_N_euk. (IPR014049); GSH-S_sub-bd_sf. (IPR037013)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Gss" matches the protein description above**
2. **Verify the organism is correct:** Rattus norvegicus (Rat).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Gss' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Gss** (gene ID: Gss, UniProt: P46413) in rat.

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
- **UniProt Accession:** P46413
- **Protein Description:** RecName: Full=Glutathione synthetase {ECO:0000303|PubMed:7862666}; Short=GSH synthetase; Short=GSH-S; EC=6.3.2.3 {ECO:0000269|PubMed:7862666}; AltName: Full=Glutathione synthase;
- **Gene Information:** Name=Gss {ECO:0000312|RGD:2752};
- **Organism (full):** Rattus norvegicus (Rat).
- **Protein Family:** Belongs to the eukaryotic GSH synthase family.
- **Key Domains:** Glutathione_synthase. (IPR005615); Glutathione_synthase_a-hlx. (IPR014042); Glutathione_synthase_C_euk. (IPR014709); Glutathione_synthase_N_euk. (IPR014049); GSH-S_sub-bd_sf. (IPR037013)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Gss" matches the protein description above**
2. **Verify the organism is correct:** Rattus norvegicus (Rat).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Gss' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Gss** (gene ID: Gss, UniProt: P46413) in rat.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research Report: Rat **Gss** (Glutathione Synthetase) — UniProt **P46413**

### 0. Target verification (critical identity checks)
**User-specified target:** UniProt **P46413**, **Rattus norvegicus** (rat), protein described as **glutathione synthetase (GSH synthetase; GSH-S)**, **EC 6.3.2.3**, gene **Gss**.

**Disambiguation status:** The literature retrieved here consistently uses **Gss/GSS** to denote **glutathione synthetase**, the enzyme catalyzing the final step of glutathione (GSH) biosynthesis, and no alternative mammalian gene with the same symbol/function emerged in the evidence set (chen2007relationshipofglutathione pages 16-20, zhu2023gssdeficiencycauses pages 1-2). However, **within the citable full-text snippets retrieved in this run, an explicit statement mapping the UniProt accession “P46413” to rat glutathione synthetase was not captured**; therefore, the **P46413↔rat GSS** link in this report is grounded in the user-provided UniProt record and is **biologically consistent** with mammalian Gss/GSS function, but not directly re-demonstrated by the citable snippets (limitation documented throughout).

### 1. Key concepts and current understanding

#### 1.1. What GSS/Gss is
**Glutathione synthetase (GSS; gene symbol Gss)** is the **second (final) enzyme** in the canonical two-step de novo biosynthesis of glutathione (GSH), a major low-molecular-weight cellular thiol antioxidant (chen2007relationshipofglutathione pages 16-20, tandon2024unravelingthemultifaceted pages 1-2).

#### 1.2. Enzymatic reaction, EC number, and substrates/products
Glutathione biosynthesis proceeds via **two ATP-dependent ligation reactions**:
1) **Glutamate-cysteine ligase (GCL; EC 6.3.2.2)** forms **γ-glutamylcysteine** from glutamate and cysteine.
2) **Glutathione synthetase (GSS; EC 6.3.2.3)** catalyzes the **ATP-dependent ligation of glycine** to **γ-glutamylcysteine (γ-GC)** to form **glutathione (GSH)** (chen2007relationshipofglutathione pages 16-20).

This EC assignment (6.3.2.3) and the reaction definition are explicitly stated in review-style sources discussing glutathione metabolism and deficiency states (galant2011homoglutathionesynthetaseand pages 18-22, chen2007relationshipofglutathione pages 16-20).

#### 1.3. Pathway context (γ-glutamyl cycle) and why GSS matters
Although the **first step (GCL)** is commonly described as **rate-limiting**, GSS is essential to complete GSH synthesis and prevent diversion of γ-glutamylcysteine intermediates into alternative pathways (chen2007relationshipofglutathione pages 16-20, levonen2000glutathione pages 17-21).

A clinically important metabolic consequence of inadequate GSS activity is that **γ-glutamylcysteine may be diverted to oxoproline (5-oxoproline/pyroglutamate)**, contributing to **oxoproline accumulation and metabolic acidosis**, worsening glutathione deficiency (chen2007relationshipofglutathione pages 16-20).

#### 1.4. Substrate specificity and kinetic considerations (what is known)
Across organisms, glutathione synthetase enzymes catalyze glycine ligation to γ-glutamylcysteine and can show measurable kinetic specificity for these substrates. For example, a well-characterized bacterial glutathione synthetase shows reported **Km** values for **γ-EC (~0.24 mM)**, **glycine (~0.91 mM)**, and **ATP (~240 μM)** and inhibition by **GSSG** (oxidized glutathione) (wu2019identificationandcharacterisation pages 79-84). While these are **not mammalian/rat** constants, they illustrate the conserved biochemical logic of substrate usage and regulation.

#### 1.5. Cellular and subcellular localization
At the cell-biological level in animals, glutathione synthesis is generally described as occurring in the **cytosol**, with **GSH subsequently distributed to organelles**, including mitochondria (levonen2000glutathione pages 17-21, tandon2024unravelingthemultifaceted pages 1-2). This implies that rat Gss (P46413) most directly exerts its catalytic function in the **cytosolic compartment**, while influencing mitochondrial and other organelle redox capacity **indirectly via GSH availability** (tandon2024unravelingthemultifaceted pages 1-2).

### 2. Recent developments and latest research (prioritizing 2023–2024)

#### 2.1. 2023: Gss loss drives age-dependent ferroptosis-linked male fertility impairment (mouse; mechanistic in vivo)
A 2023 primary study investigated **Gss function in germ cells** using a **postnatal germ-cell-specific deletion model** (Stra8-Cre; S8/Gss−/−). The authors report that **Gss deficiency causes age-dependent fertility impairment** mediated by **ROS-triggered ferroptosis** in testes (publication date: **Dec 2023**; URL: https://doi.org/10.1038/s41419-023-06359-x) (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8).

Key mechanistic findings with quantitative/statistical support include:
- **Testicular GSH levels decreased** at both 2 and 8 months, but oxidative damage and ferroptosis-associated signatures were most prominent with aging (zhu2023gssdeficiencycauses pages 7-8).
- At **8 months**, knockout testes showed increased **ROS and lipid peroxidation markers** (e.g., **3-NT, 4-HNE; P < 0.01, n = 4**) and elevated **8-OHdG and Fe2+ (P < 0.01; n = 3–4)** (zhu2023gssdeficiencycauses pages 7-8).
- Molecularly, ferroptosis-associated changes included **reduced GPX4** and increased **ALOX15** at 8 months, consistent with lipid peroxide accumulation and ferroptotic vulnerability (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8).
- Importantly, the phenotype was **functionally rescued** by inhibiting ferroptosis through **intraperitoneal GSH supplementation** or **ferroptosis inhibitor Fer-1**, which reduced oxidative/iron readouts and improved sperm morphology (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8).

**Interpretation for rat functional annotation:** While this is a mouse model, it provides high-quality in vivo evidence that **GSS activity can be a proximal determinant of ferroptosis sensitivity** in specific tissues through maintaining GSH pools that support lipid hydroperoxide detoxification systems (e.g., GPX4 axis) (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8).

#### 2.2. 2024: Compartmentation and mitochondrial glutathione framing (review perspective)
A 2024 review on **mitochondrial glutathione (mGSH)** emphasizes that GSH is **synthesized primarily in the cytoplasm and delivered to mitochondria**, where it contributes to detoxification of mitochondrial hydrogen peroxide and helps constrain multiple programmed cell death modes, including ferroptosis (publication date: **Jan 2024**; URL: https://doi.org/10.3390/ijms25021314) (tandon2024unravelingthemultifaceted pages 1-2). This framing reinforces the concept that cytosolic biosynthetic enzymes such as GSS indirectly shape mitochondrial redox homeostasis through GSH supply (tandon2024unravelingthemultifaceted pages 1-2).

### 3. Current applications and real-world implementations

#### 3.1. Disease mechanism interpretation: GSS deficiency and pyroglutamate/5-oxoproline accumulation
A recurring clinical/biochemical application of GSS knowledge is interpretation of **inborn errors of glutathione metabolism**, where insufficient GSS function contributes to **5-oxoproline (pyroglutamate) accumulation** and metabolic acidosis via diversion of γ-glutamylcysteine (chen2007relationshipofglutathione pages 16-20, chen2007relationshipofglutathione pages 20-24). This is directly relevant to functional annotation because it ties the **enzymatic bottleneck** (γ-GC→GSH) to measurable metabolic outcomes (oxoproline/pyroglutamate) (chen2007relationshipofglutathione pages 16-20).

#### 3.2. Ferroptosis-directed interventions (preclinical)
The 2023 mouse study provides a concrete example of how manipulating the GSS product pool can have therapeutic-like effects: **GSH administration** and **Fer-1** functionally rescued age-dependent subfertility and reduced ferroptosis-associated biochemical signatures (Dec 2023; https://doi.org/10.1038/s41419-023-06359-x) (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8). This supports the real-world experimental practice of using GSH supplementation and ferroptosis inhibitors to probe the causal role of glutathione synthesis capacity.

#### 3.3. Sepsis/critical illness framing (systems-level antioxidant context)
A 2024 review on glutathione in sepsis reiterates the canonical two-step ATP-dependent GSH synthesis and highlights glutathione as a major non-protein thiol antioxidant in animal cells, present across cytosolic and organellar compartments (publication date: **Mar 2024**; URL: https://doi.org/10.7759/cureus.56896) (tandon2024unravelingthemultifaceted pages 1-2). While not rat- or Gss-specific experimentally, it reflects current clinical-medicine framing in which glutathione availability is central to systemic oxidative stress responses (tandon2024unravelingthemultifaceted pages 1-2).

### 4. Expert opinions and analysis (authoritative synthesis)

1) **Biochemical consensus:** Multiple sources converge on GSS as **EC 6.3.2.3**, catalyzing glycine ligation to γ-glutamylcysteine to form GSH (galant2011homoglutathionesynthetaseand pages 18-22, chen2007relationshipofglutathione pages 16-20). This is the core catalytic annotation for rat Gss/P46413.

2) **Localization consensus (functional compartment):** Animal-cell glutathione synthesis is generally described as cytosolic, with downstream distribution of GSH to organelles including mitochondria; thus, GSS is best annotated as **cytosolic enzyme supporting cellular/mitochondrial redox buffering via GSH supply** (levonen2000glutathione pages 17-21, tandon2024unravelingthemultifaceted pages 1-2).

3) **Systems biology insight (2023–2024 trend):** Recent mechanistic work increasingly places **GSH synthesis capacity** upstream of **ferroptosis sensitivity** in vivo, consistent with a shift from “GSH as a generic antioxidant” toward “GSH synthesis as a regulated node controlling lipid-peroxide detoxification and tissue-specific degenerative phenotypes” (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8).

### 5. Relevant statistics and data points (recent studies)

- In germ-cell-specific **Gss knockout** testes (mouse), oxidative and ferroptosis-associated markers increased at older age with reported significance for several readouts (e.g., **3-NT and 4-HNE: P < 0.01, n = 4; 8-OHdG and Fe2+: P < 0.01, n = 3–4**) (zhu2023gssdeficiencycauses pages 7-8).

- Example enzyme kinetics from a well-characterized glutathione synthetase (non-mammalian) include **Km** values: **γ-EC 0.24 mM**, **glycine 0.91 mM**, **ATP 240 μM**, and inhibition by **GSSG** (wu2019identificationandcharacterisation pages 79-84). These values are included as indicative of substrate use/specificity, not as rat parameters.

### 6. Structured functional annotation summary
The following table consolidates key functional-annotation points (including noted evidence gaps for rat-specific mapping):

| Aspect | Key points | Best supporting citations | Notes/limitations |
|---|---|---|---|
| Identity | • UniProt P46413 is the rat protein entry used in proteomics studies and identified as glutathione synthetase. • Gss/GSS is the eukaryotic enzyme for the second and final step of glutathione biosynthesis. | (zhu2023gssdeficiencycauses pages 1-2) | Direct P46413→rat GSS mapping was not explicitly recovered in the available context IDs; identity is strongly consistent with the user-supplied UniProt record and GSS literature, but rat-specific confirmation from the available contexts is limited. |
| Reaction / EC | • Glutathione synthetase is EC 6.3.2.3. • It catalyzes the ATP-dependent final step of GSH synthesis by adding glycine to γ-glutamylcysteine. • This is the non-rate-limiting second step after GCL activity. | (galant2011homoglutathionesynthetaseand pages 18-22, chen2007relationshipofglutathione pages 16-20, levonen2000glutathione pages 17-21) | Reaction chemistry is well established across eukaryotes; rat-specific enzymology was not directly captured in the available contexts. |
| Substrates / products | • Core substrates are γ-glutamylcysteine, glycine, and ATP. • Product is glutathione (GSH), the major low-molecular-weight cellular thiol antioxidant. • Literature supports strong substrate specificity for glycine ligation to γ-glutamylcysteine. | (wu2019identificationandcharacterisation pages 79-84, chen2007relationshipofglutathione pages 16-20, tandon2024unravelingthemultifaceted pages 1-2) | Detailed mammalian kinetic constants were not available in the retrieved context; one substrate-specificity example comes from non-rat GS literature. |
| Cellular localization | • Glutathione biosynthesis enzymes are generally described as cytosolic in animal cells. • GSH is synthesized mainly in the cytoplasm and then distributed to organelles, including mitochondria. • Therefore, rat Gss function is most plausibly cytosolic, supporting cellular and mitochondrial redox buffering indirectly via GSH supply. | (levonen2000glutathione pages 17-21, tandon2024unravelingthemultifaceted pages 1-2) | Available context supports animal-cell cytosolic synthesis but lacks a rat GSS subcellular localization experiment tied specifically to P46413. |
| Pathways / biological roles | • Gss acts in the γ-glutamyl cycle / glutathione biosynthesis pathway. • Its product GSH supports ROS detoxification, redox homeostasis, xenobiotic defense, and ferroptosis resistance. • When GSS activity is insufficient, γ-glutamylcysteine can be diverted toward oxoproline/pyroglutamate accumulation. | (chen2007relationshipofglutathione pages 16-20, tandon2024unravelingthemultifaceted pages 1-2, chen2007relationshipofglutathione pages 20-24) | Most pathway statements are conserved mammalian biology; direct rat pathway experiments in the retrieved set are sparse. |
| Phenotypes / disease links | • Human GSS deficiency is classically linked to hemolytic anemia, metabolic acidosis, 5-oxoprolinuria/pyroglutamate accumulation, and neurologic manifestations in generalized forms. • These phenotypes mechanistically fit loss of GSH synthesis and diversion of γ-glutamylcysteine metabolism. | (chen2007relationshipofglutathione pages 16-20, chen2007relationshipofglutathione pages 20-24) | Disease evidence is mainly human/inherited-metabolic-disease literature rather than rat-specific pathology. |
| Recent 2023–2024 developments | • A 2023 mouse study showed germ-cell Gss deficiency causes age-dependent male subfertility via ROS-driven ferroptosis in testis. • At 8 months, knockout testes showed higher ROS/lipid peroxidation and Fe2+ with reduced GPX4 and increased ALOX15; some readouts were significant at P < 0.01 with n = 3–4. • Rescue by GSH or ferroptosis inhibitor Fer-1 supports a specific Gss→GSH→GPX4/ALOX15→ferroptosis axis. | (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8) | Strong recent mechanistic evidence exists in mouse, not rat; still highly informative for mammalian functional annotation. |
| Applications / implementations | • GSS/GSH biology is used in redox, toxicology, and ferroptosis research to interpret oxidative-stress phenotypes. • Recent work suggests practical use of GSH replenishment or ferroptosis inhibition to rescue Gss-linked phenotypes in vivo. • GSS status is also relevant for interpreting pyroglutamate acidosis and broader glutathione-pathway dysfunction. | (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8, tandon2024unravelingthemultifaceted pages 1-2) | These are pathway-level or translational implementations; no rat-specific therapeutic manipulation of P46413 was recovered from the available contexts. |


*Table: This table summarizes the main functional annotation points for rat Gss/UniProt P46413, integrating core biochemical function with recent mammalian evidence. It also flags where evidence is indirect or not yet rat-specific, which is important for careful annotation.*

### 7. Evidence gaps and recommendations (for rat-specific annotation fidelity)
- **Rat-specific enzymology and localization:** The evidence retrieved here supports the conserved reaction and broad cytosolic localization in animals, but does not provide rat-specific kinetic constants, direct subcellular localization experiments, or direct P46413 mapping within the citable snippets (chen2007relationshipofglutathione pages 16-20, levonen2000glutathione pages 17-21, tandon2024unravelingthemultifaceted pages 1-2).
- **Accession-to-gene linkage:** While the user-supplied UniProt record defines P46413 as rat GSS, the retrieved citable texts in this run did not explicitly restate “P46413 = glutathione synthetase (rat)”. A targeted follow-up retrieval focused on proteomics papers that explicitly list accession mappings (e.g., supplementary tables) would strengthen accession-level verification.

### References (URLs and publication dates as available in evidence)
- Chen Y. *Relationship of glutathione deficiency to oxidative stress-related disease and aging.* 2007. (chen2007relationshipofglutathione pages 16-20, chen2007relationshipofglutathione pages 20-24)
- Zhu H, et al. *Gss deficiency causes age-related fertility impairment via ROS-triggered ferroptosis in the testes of mice.* **Cell Death & Disease**. **Dec 2023**. https://doi.org/10.1038/s41419-023-06359-x (zhu2023gssdeficiencycauses pages 1-2, zhu2023gssdeficiencycauses pages 7-8)
- Chen T-H, et al. *Mitochondrial Glutathione in Cellular Redox Homeostasis and Disease Manifestation.* **Int J Mol Sci**. **Jan 2024**. https://doi.org/10.3390/ijms25021314 (tandon2024unravelingthemultifaceted pages 1-2)
- Tandon R, Tandon A. *Unraveling the Multifaceted Role of Glutathione in Sepsis: A Comprehensive Review.* **Cureus**. **Mar 2024**. https://doi.org/10.7759/cureus.56896 (tandon2024unravelingthemultifaceted pages 1-2)


References

1. (chen2007relationshipofglutathione pages 16-20): Y Chen. Relationship of glutathione deficiency to oxidative stress-related disease and aging. Unknown journal, 2007.

2. (zhu2023gssdeficiencycauses pages 1-2): Haixia Zhu, Yin Cheng, Xianmei Wang, Xing Yang, Min Liu, Jun Liu, Shuqiao Liu, Hongxiang Wang, Aizhen Zhang, Runze Li, Chao Ye, Jian Zhang, Jiangang Gao, Xiaolong Fu, and Bin Wu. Gss deficiency causes age-related fertility impairment via ros-triggered ferroptosis in the testes of mice. Cell Death &amp; Disease, Dec 2023. URL: https://doi.org/10.1038/s41419-023-06359-x, doi:10.1038/s41419-023-06359-x. This article has 49 citations and is from a peer-reviewed journal.

3. (tandon2024unravelingthemultifaceted pages 1-2): Ratan Tandon and Ashish Tandon. Unraveling the multifaceted role of glutathione in sepsis: a comprehensive review. Cureus, Mar 2024. URL: https://doi.org/10.7759/cureus.56896, doi:10.7759/cureus.56896. This article has 14 citations.

4. (galant2011homoglutathionesynthetaseand pages 18-22): Ashley Galant. Homoglutathione synthetase and the plant thiol-redox proteome. ArXiv, Jan 2011. URL: https://doi.org/10.7936/k76m34v9, doi:10.7936/k76m34v9. This article has 0 citations.

5. (levonen2000glutathione pages 17-21): AL Levonen. Glutathione. Unknown journal, 2000.

6. (wu2019identificationandcharacterisation pages 79-84): D Wu. Identification and characterisation of a novel glutathione synthetase gene family in the plant parasitic nematode rotylenchulus reniformis. Unknown journal, 2019.

7. (zhu2023gssdeficiencycauses pages 7-8): Haixia Zhu, Yin Cheng, Xianmei Wang, Xing Yang, Min Liu, Jun Liu, Shuqiao Liu, Hongxiang Wang, Aizhen Zhang, Runze Li, Chao Ye, Jian Zhang, Jiangang Gao, Xiaolong Fu, and Bin Wu. Gss deficiency causes age-related fertility impairment via ros-triggered ferroptosis in the testes of mice. Cell Death &amp; Disease, Dec 2023. URL: https://doi.org/10.1038/s41419-023-06359-x, doi:10.1038/s41419-023-06359-x. This article has 49 citations and is from a peer-reviewed journal.

8. (chen2007relationshipofglutathione pages 20-24): Y Chen. Relationship of glutathione deficiency to oxidative stress-related disease and aging. Unknown journal, 2007.

## Artifacts

- [Edison artifact artifact-00](Gss-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. chen2007relationshipofglutathione pages 16-20
2. wu2019identificationandcharacterisation pages 79-84
3. tandon2024unravelingthemultifaceted pages 1-2
4. zhu2023gssdeficiencycauses pages 7-8
5. zhu2023gssdeficiencycauses pages 1-2
6. galant2011homoglutathionesynthetaseand pages 18-22
7. levonen2000glutathione pages 17-21
8. chen2007relationshipofglutathione pages 20-24
9. https://doi.org/10.1038/s41419-023-06359-x
10. https://doi.org/10.3390/ijms25021314
11. https://doi.org/10.7759/cureus.56896
12. https://doi.org/10.1038/s41419-023-06359-x,
13. https://doi.org/10.7759/cureus.56896,
14. https://doi.org/10.7936/k76m34v9,