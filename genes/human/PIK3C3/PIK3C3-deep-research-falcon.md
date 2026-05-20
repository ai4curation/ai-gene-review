---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T07:20:13.222491'
end_time: '2026-05-12T07:27:33.020845'
duration_seconds: 439.8
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

Perform concise GO-focused deep research on the human PIK3C3 gene (UniProt Q8NEB9; phosphatidylinositol 3-kinase catalytic subunit type 3/Vps34). Summarize the core molecular function, major biological processes, cellular locations, key experimental evidence, and any GO annotation caveats. Include PMID or DOI citations where available, and keep the report focused for gene annotation review.

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

Perform concise GO-focused deep research on the human PIK3C3 gene (UniProt Q8NEB9; phosphatidylinositol 3-kinase catalytic subunit type 3/Vps34). Summarize the core molecular function, major biological processes, cellular locations, key experimental evidence, and any GO annotation caveats. Include PMID or DOI citations where available, and keep the report focused for gene annotation review.

## GO-focused gene annotation research report: human **PIK3C3** (VPS34) (UniProt Q8NEB9)

### 1) Key concepts and definitions (current understanding)

**Gene/protein**: Human **PIK3C3** encodes **VPS34**, the *class III phosphatidylinositol 3-kinase* catalytic subunit that produces **phosphatidylinositol 3-phosphate (PI3P)**. In the most authoritative recent pharmacology-focused synthesis, VPS34 is described as **exclusively catalyzing PI3P production from phosphatidylinositol (PI) in vitro and in vivo**—a key point for GO molecular function specificity (i.e., not generating PIP3 from PI(4,5)P2 as class I PI3Ks do). (burke2023beyondpi3kstargeting pages 22-23)

**GO-relevant biochemical reaction** (MF + BP):
- Substrate/product specificity for curation: **PI → PI3P** (phosphatidylinositol 3-phosphate biosynthesis) as the defining catalytic activity of VPS34. (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 1-2)

**Complex architecture and nomenclature** (GO CC + context for BP): VPS34 functions as a subunit of two **distinct tetrameric complexes**:
- **PI3KC3 Complex I (PI3KC3-C1)**: VPS34 (**PIK3C3**) + **VPS15 (PIK3R4)** + **BECN1** + **ATG14**. This complex is classically associated with **autophagy initiation/autophagosome nucleation**. (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 1-2, chau2024thecellularadaptor pages 1-2)
- **PI3KC3 Complex II (PI3KC3-C2)**: VPS34 (**PIK3C3**) + **VPS15 (PIK3R4)** + **BECN1** + **UVRAG**, classically associated with **endocytic sorting/endosome maturation** and related trafficking. (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 1-2)

**Key regulators frequently relevant to annotation context**:
- **NRBF2**: described as an activator of **Complex I** (and thus relevant when annotating autophagy-initiation-linked PI3P production). (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 12-12)
- **Rubicon (RUBCN)**: described as a Complex-II-associated regulator that can modulate autophagy stages and endocytic roles in a context-dependent manner; it contributes to why Complex I vs II should be separated in annotation where possible. (lee2024regulatorymechanismsgoverning pages 12-12)

### 2) Core GO Molecular Function (MF): what VPS34 does

**Core MF statement for PIK3C3**: VPS34 is the catalytic subunit of class III PI3K and **produces PI3P from PI**, with major sources emphasizing the **exclusivity** of this reaction for VPS34 in vivo/in vitro among class III PI3Ks. (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 1-2)

**Complex requirement for activity**: VPS34 activity depends on its complex context; notably **VPS15/PIK3R4 is described as required for VPS34 activity**, reinforcing that MF evidence often comes from complex-level biochemistry/structural studies rather than isolated VPS34. (lee2024regulatorymechanismsgoverning pages 1-2)

### 3) Major GO Biological Processes (BP): autophagy and endocytosis-centered roles

#### 3.1 Autophagy initiation / autophagosome nucleation (canonical macroautophagy)
- Multiple sources converge on the model that **Complex I (ATG14-containing)** is the **autophagy initiation** VPS34 complex, generating PI3P to recruit downstream PI3P-binding effectors (including WIPI proteins) to early autophagic membranes. (lee2024regulatorymechanismsgoverning pages 1-2, lee2024regulatorymechanismsgoverning pages 12-12)
- In an experimentally grounded signaling study (STING/autophagy), PI3P is described as a key product that **recruits ATG12–ATG5–ATG16L1 via WIPI2 to target LC3 to the phagophore**, consistent with a canonical pathway in which VPS34-derived PI3P supports phagophore maturation steps. (wan2023stingdirectlyrecruits pages 1-2)

#### 3.2 Endocytic trafficking, endosomal identity, and endolysosomal maturation
- VPS34 activity is strongly tied to **endosomal PI3P pools** that define **early endosome identity** and sorting, and PI3P serves as a platform for downstream trafficking and maturation processes. (thibault2023targetingclassiiiiii pages 8-10, swamynathan2024dietaryprooxidanttherapy pages 8-9)
- A recent 2024 *Science* study provides direct phenotype-level support consistent with an endosomal identity role: both a selective VPS34 inhibitor (**VPS34-IN1**) and an oxidative intervention (**MSB**) produce endosomal defects alongside a reduction in PI3P-reporter puncta (GFP-2xFYVE), and CRISPR targeting of VPS34 phenocopies these effects. This supports annotating VPS34 to **PI3P-dependent endosomal organization/trafficking** processes. (swamynathan2024dietaryprooxidanttherapy pages 8-9)

### 4) GO Cellular Component (CC): where VPS34 acts

**Complex-level CC annotations (high confidence)**:
- **PI3KC3-C1 (Complex I)** and **PI3KC3-C2 (Complex II)** as distinct cellular components/complexes are directly supported by recent authoritative reviews describing their tetrameric composition and functional distinctness. (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 1-2)

**Membrane compartments** (context-dependent localization):
- **ER-linked autophagy initiation sites / phagophore assembly sites**: Evidence that Complex I is functionally tied to ER-associated initiation emerges from work showing that factors can promote **ATG14 targeting to the ER** and enhance PI3KC3-C1 activity, supporting ER/phagophore-associated CC assignments for the autophagy-initiation complex. (chau2024thecellularadaptor pages 1-2)
- **Early endosomes**: A recent *Science* study reports that VPS34 perturbation reduces PI3P reporter puncta and yields vacuoles retaining early-endosome markers (e.g., Rab5 association) while lacking lysosomal marker LAMP1 in the tested context, consistent with a key VPS34 role at early endosomal membranes. (swamynathan2024dietaryprooxidanttherapy pages 8-9)
- **Endosomes and endosome–lysosome interface**: Complex composition is described as directing VPS34 to endosome-linked vs phagophore-linked functions, and VPS34-dependent PI3P is connected to later fusion/maturation events involving late endosomes/lysosomes in trafficking-centric models. (wible2024unexpectedinhibitionof pages 1-3, thibault2023targetingclassiiiiii pages 8-10)

### 5) Key experimental evidence (selected, GO-curation-relevant)

#### 5.1 PI3P reporter depletion and endosomal phenotypes (2024)
- **Swamynathan et al., Science (Oct 2024; DOI: 10.1126/science.adk9167; URL: https://doi.org/10.1126/science.adk9167)**: Demonstrates that an oxidative agent (MSB) functionally antagonizes VPS34 and phenocopies VPS34 inhibition, sharply reducing PI3P reporter puncta (GFP-2xFYVE) and producing endosome identity defects; NAC reverses MSB effects consistent with oxidative inactivation rather than simple competitive inhibition. This is strong support for **PI3P biosynthesis** and **endosomal organization** functions at the cellular level. (swamynathan2024dietaryprooxidanttherapy pages 8-9, swamynathan2024dietaryprooxidanttherapy pages 1-3)

#### 5.2 Genetic + inhibitor evidence tying VPS34 to endosomal trafficking during viral entry (2024; quantitative)
- **Gong et al., PLoS Pathogens (Aug 2024; DOI: 10.1371/journal.ppat.1012444; URL: https://doi.org/10.1371/journal.ppat.1012444)**: Shows VPS34/PIK3C3 is required for **Ebola virus entry** via endocytic trafficking. Quantitatively, **VPS34-IN-1** inhibits EBOV infection with **IC50 = 371 nM** (EBOVΔVP30-EGFP model) and **IC50 = 405 nM** (authentic EBOV), and a **kinase-dead PIK3C3 D761A** does not complement PIK3C3 KO. These results link **VPS34 kinase activity** to **endosomal maturation/trafficking to NPC1-positive endolysosomal compartments**. (gong2024genomewidecrisprcas9screen pages 7-10)

#### 5.3 Autophagy-independent PI3P-dependent membrane phenotypes (2024)
- **Wible et al., Cell Death & Disease (Jan 2024; DOI: 10.1038/s41419-024-06423-0; URL: https://doi.org/10.1038/s41419-024-06423-0)**: Reports that a vacuolation phenotype can **rely on the PIK3C3 complex and PI(3)P production but not on autophagy per se**, supporting VPS34 assignment to endolysosomal organization/volume control processes that are distinct from canonical macroautophagy readouts. (wible2024unexpectedinhibitionof pages 1-3)

#### 5.4 Noncanonical autophagy route bypassing PIK3C3 (2023; caveat)
- **Wan et al., EMBO Journal (Mar 2023; DOI: 10.15252/embj.2022112387; URL: https://doi.org/10.15252/embj.2022112387)**: Shows **STING-induced autophagy requires WIPI2 but not the PIK3C3 complex**, an important warning against blanket annotation of PIK3C3 as required for all forms of autophagosome formation/LC3 lipidation. (wan2023stingdirectlyrecruits pages 1-2)

### 6) GO annotation caveats and curation guidance (for review)

1. **Avoid class I PI3K conflation**: VPS34 produces **PI3P from PI**, not PIP3 from PI(4,5)P2; MF terms should reflect PI3P biosynthesis rather than PI(3,4,5)P3-linked signaling. (burke2023beyondpi3kstargeting pages 22-23)

2. **Complex-specific annotation is preferred**: When evidence indicates autophagy initiation, it is most consistent with **Complex I (ATG14; NRBF2-activated)**; when evidence indicates endocytic sorting/viral entry/early endosome identity, it is most consistent with **Complex II (UVRAG)** and shared core subunits. Consider annotating to both BP terms only when evidence supports both, or qualifying via complex context. (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 1-2, thibault2023targetingclassiiiiii pages 8-10)

3. **Noncanonical autophagy can be VPS34-independent**: STING-induced autophagy provides a clear example that autophagy-related phenotypes can occur without PIK3C3 dependency; phenotype-only studies should not automatically imply direct PIK3C3 participation in all autophagy initiation contexts. (wan2023stingdirectlyrecruits pages 1-2)

4. **Endosomal PI3P roles can masquerade as ‘autophagy’ phenotypes**: PI3P-dependent vacuolation and endolysosomal swelling can depend on PIK3C3 but be **autophagy-independent**, affecting inference of BP terms from morphology alone. (wible2024unexpectedinhibitionof pages 1-3)

5. **Phenotype interpretation (KO vs kinase-dead; compensatory PI3P)**: A synthesis focused on PI3K targeting highlights that VPS34 has roles that can be complicated by scaffolding/complex-level effects, differences between genetic knockout and catalytic inactivation, and potential compensatory PI3P sources in specific contexts; this argues for prioritizing direct biochemical/kinase-activity evidence (IDAs/IMP with catalytic mutants) for MF/BP assertions. (thibault2023targetingclassiiiiii pages 8-10)

### 7) Recent developments and real-world applications (2023–2024)

- **Therapeutic targeting/redox pharmacology**: A high-impact 2024 *Science* paper identifies an oxidative dietary compound (MSB) as functionally antagonizing VPS34 by **oxidation of key cysteines**, tying VPS34 to endosomal identity/sorting and suggesting redox-sensitive control points relevant to drug development and disease models. (Oct 2024; https://doi.org/10.1126/science.adk9167). (swamynathan2024dietaryprooxidanttherapy pages 1-3, swamynathan2024dietaryprooxidanttherapy pages 8-9)

- **Antiviral host-factor targeting**: A 2024 *PLOS Pathogens* study provides quantitative inhibitor potency (sub-micromolar IC50s) and genetic validation of kinase activity requirement for EBOV entry, supporting VPS34 as a potential host-directed antiviral target specifically through endocytic/endolysosomal trafficking mechanisms. (Aug 2024; https://doi.org/10.1371/journal.ppat.1012444). (gong2024genomewidecrisprcas9screen pages 7-10)

- **Expert synthesis of complex biology and druggability**: A widely cited 2023 *Nature Reviews Drug Discovery* review emphasizes VPS34’s catalytic specificity and clear complex partitioning (C1 vs C2), supporting precise GO MF/CC curation and motivating use of complex-aware annotations. (Nov 2023; https://doi.org/10.1038/s41573-022-00582-5). (burke2023beyondpi3kstargeting pages 22-23)

### 8) GO-focused evidence summary table

| GO aspect | Proposed GO concept / term label | Evidence summary | Key complex context | Representative experimental evidence types | Citations |
|---|---|---|---|---|---|
| MF | Phosphatidylinositol 3-kinase activity; phosphatidylinositol-3-phosphate biosynthetic process | Human VPS34/PIK3C3 is the class III PI3K catalytic subunit that converts phosphatidylinositol (PI) to PI3P, with recent reviews emphasizing this as its defining enzymatic activity and distinguishing it from class I PI3Ks. | Shared catalytic core in both Complex I and II with VPS15/PIK3R4 and BECN1; VPS15 is required for full VPS34 activity. | Biochemical/structural studies; kinase inhibition; PI3P-effector recruitment analyses. | Burke et al., *Nat Rev Drug Discov* (Nov 2023), DOI: 10.1038/s41573-022-00582-5, https://doi.org/10.1038/s41573-022-00582-5 (burke2023beyondpi3kstargeting pages 22-23, lee2024regulatorymechanismsgoverning pages 1-2) |
| BP | Macroautophagy initiation / autophagosome nucleation | VPS34-generated PI3P promotes recruitment of WIPI/ATG machinery to phagophore membranes, supporting autophagosome initiation and early biogenesis. | Complex I: PIK3C3-VPS15-BECN1-ATG14; activated by NRBF2 and regulated by ULK1-linked inputs. | Complex reconstitution/structural studies; localization of ATG14 puncta; PI3P-dependent effector recruitment. | Lee et al., *Biomol Ther* (Oct 2024), DOI: 10.4062/biomolther.2024.094, https://doi.org/10.4062/biomolther.2024.094 (lee2024regulatorymechanismsgoverning pages 12-12, lee2024regulatorymechanismsgoverning pages 6-7) |
| CC | PI3KC3-C1 autophagy initiation complex; ER/phagophore assembly site / omegasome-associated membrane | PI3KC3-C1 is targeted to ER-linked autophagy initiation sites, and ATG14-directed ER localization promotes autophagic vacuole formation. | Complex I with ATG14 as specifying subunit; GULP1 can enhance ATG14 targeting to ER and stimulate PI3KC3-C1 activity. | ER localization microscopy; autophagic vacuole analysis; modulation of ATG14 targeting. | Chau et al., *Cell Mol Life Sci* (Jul 2024), DOI: 10.1007/s00018-024-05351-8, https://doi.org/10.1007/s00018-024-05351-8 (chau2024thecellularadaptor pages 1-2) |
| BP | Endocytic trafficking / early endosome organization | VPS34 activity is required to maintain PI3P-positive early endosome identity, and oxidative or pharmacologic VPS34 inhibition depletes PI3P and disrupts endosomal sorting. | Most consistent with endosomal VPS34 complexes, especially Complex II-linked endocytic function; shared VPS34-VPS15-BECN1 core. | GFP-2xFYVE PI3P reporter loss; CRISPR targeting; VPS34-IN1; live-cell vacuolization imaging. | Swamynathan et al., *Science* (Oct 2024), DOI: 10.1126/science.adk9167, https://doi.org/10.1126/science.adk9167 (swamynathan2024dietaryprooxidanttherapy pages 8-9, swamynathan2024dietaryprooxidanttherapy pages 1-3) |
| CC | Early endosome | PI3P reporter depletion, Rab5-associated vacuoles, and loss of normal endosomal identity after VPS34 perturbation support localization/function at early endosomal membranes. | Endosomal VPS34 complexes; Rab5-dependent recruitment of hVPS34/p150 noted in review-level mechanistic summaries. | PI3P reporter imaging; Rab5 colocalization; inhibitor phenocopy; CRISPR knockout. | Swamynathan et al., *Science* (Oct 2024), DOI: 10.1126/science.adk9167, https://doi.org/10.1126/science.adk9167; Lee et al., *Biomol Ther* (Oct 2024), DOI: 10.4062/biomolther.2024.094, https://doi.org/10.4062/biomolther.2024.094 (swamynathan2024dietaryprooxidanttherapy pages 8-9, lee2024regulatorymechanismsgoverning pages 12-12) |
| BP | Endosome maturation / endolysosomal trafficking | VPS34 kinase activity is necessary for trafficking cargo/virions into NPC1-positive endolysosomal compartments, supporting a role in endosomal maturation and membrane traffic beyond canonical autophagy. | Functional emphasis on endocytic VPS34 activity; Complex II is the main endocytic sorting complex in current models. | KO/rescue with kinase-dead mutant; selective inhibitor; confocal colocalization with NPC1; viral entry assays. | Gong et al., *PLoS Pathog* (Aug 2024), DOI: 10.1371/journal.ppat.1012444, https://doi.org/10.1371/journal.ppat.1012444; VPS34-IN-1 IC50 = 371 nM for EBOVΔVP30-EGFP and 405 nM for authentic EBOV (gong2024genomewidecrisprcas9screen pages 7-10) |
| BP | Regulation of autophagy-independent endolysosomal membrane organization | Some VPS34-dependent PI3P phenotypes reflect endolysosomal control rather than autophagy itself, since vacuolation can require the PIK3C3 complex and PI3P but occur independently of autophagy per se. | Shared VPS34 complex with context-dependent adaptor usage; not uniquely attributable to Complex I. | Pharmacologic perturbation; PI3P dependence tests; endolysosomal morphology assays. | Wible et al., *Cell Death & Disease* (Jan 2024), DOI: 10.1038/s41419-024-06423-0, https://doi.org/10.1038/s41419-024-06423-0 (wible2024unexpectedinhibitionof pages 1-3) |
| CC | Endosome/lysosome fusion pathway; autophagosome-endolysosome interface | VPS34 participates in pathways linking PI3P-positive autophagic/endosomal membranes to later Rab7-dependent fusion with late endosomes and lysosomes. | Complex composition helps determine whether VPS34 acts at phagophore-associated or endosomal membranes; UVRAG/Rubicon-linked contexts are especially relevant downstream. | Membrane-trafficking studies; inhibitor phenotypes; pathway reconstruction from imaging and genetics. | Wible et al., *Cell Death & Disease* (Jan 2024), DOI: 10.1038/s41419-024-06423-0, https://doi.org/10.1038/s41419-024-06423-0; Thibault et al., *Cancers* (Jan 2023), DOI: 10.3390/cancers15030784, https://doi.org/10.3390/cancers15030784 (wible2024unexpectedinhibitionof pages 1-3, thibault2023targetingclassiiiiii pages 8-10) |
| CC/BP caveat | Context-specific: not all LC3 lipidation/autophagosome formation is VPS34-dependent | STING-induced autophagy can require WIPI2 but not the PIK3C3 complex, so annotations for autophagosome formation should avoid overgeneralizing VPS34 dependence to all noncanonical autophagy pathways. | Canonical autophagy uses Complex I; this caveat applies to noncanonical STING-driven LC3 lipidation/autophagosome formation. | Genetic pathway dissection; VPS34 inhibitor insensitivity in STING context; WIPI2 dependency tests. | Wan et al., *EMBO J* (Mar 2023), DOI: 10.15252/embj.2022112387, https://doi.org/10.15252/embj.2022112387 (wan2023stingdirectlyrecruits pages 1-2) |


*Table: This table summarizes GO-relevant molecular function, biological process, and cellular component evidence for human PIK3C3/VPS34, with emphasis on complex-specific context and annotation caveats. It also includes the key quantitative antiviral statistic from Gong 2024 for VPS34-IN-1.*


References

1. (burke2023beyondpi3kstargeting pages 22-23): John E Burke, Joanna Catherine Caprio Triscott, Brooke M Emerling, and Gerald R V Hammond. Beyond pi3ks: targeting phosphoinositide kinases in disease. Nature Reviews. Drug Discovery, 22:357-386, Nov 2023. URL: https://doi.org/10.1038/s41573-022-00582-5, doi:10.1038/s41573-022-00582-5. This article has 157 citations.

2. (lee2024regulatorymechanismsgoverning pages 1-2): Yongook Lee, Nguyen Minh Tuan, Gi Jeong Lee, Boram Kim, Jung Ho Park, and Chang Hoon Lee. Regulatory mechanisms governing the autophagy-initiating vps34 complex and its inhibitors. Biomolecules & Therapeutics, 32:723-735, Oct 2024. URL: https://doi.org/10.4062/biomolther.2024.094, doi:10.4062/biomolther.2024.094. This article has 16 citations and is from a peer-reviewed journal.

3. (chau2024thecellularadaptor pages 1-2): Dennis Dik-Long Chau, Zhicheng Yu, Wai Wa Ray Chan, Zhai Yuqi, Raymond Chuen Chung Chang, Jacky Chi Ki Ngo, Ho Yin Edwin Chan, and Kwok-Fai Lau. The cellular adaptor gulp1 interacts with atg14 to potentiate autophagy and app processing. Cellular and Molecular Life Sciences: CMLS, Jul 2024. URL: https://doi.org/10.1007/s00018-024-05351-8, doi:10.1007/s00018-024-05351-8. This article has 6 citations.

4. (lee2024regulatorymechanismsgoverning pages 12-12): Yongook Lee, Nguyen Minh Tuan, Gi Jeong Lee, Boram Kim, Jung Ho Park, and Chang Hoon Lee. Regulatory mechanisms governing the autophagy-initiating vps34 complex and its inhibitors. Biomolecules & Therapeutics, 32:723-735, Oct 2024. URL: https://doi.org/10.4062/biomolther.2024.094, doi:10.4062/biomolther.2024.094. This article has 16 citations and is from a peer-reviewed journal.

5. (wan2023stingdirectlyrecruits pages 1-2): Wei Wan, Chuying Qian, Qian Wang, Jin Li, Hongtao Zhang, Lei Wang, Maomao Pu, Yewei Huang, Zhengfu He, Tianhua Zhou, Han‐Ming Shen, and Wei Liu. Sting directly recruits wipi2 for autophagosome formation during sting‐induced autophagy. The EMBO Journal, Mar 2023. URL: https://doi.org/10.15252/embj.2022112387, doi:10.15252/embj.2022112387. This article has 71 citations.

6. (thibault2023targetingclassiiiiii pages 8-10): Benoît Thibault, Fernanda Ramos-Delgado, and Julie Guillermet-Guibert. Targeting class i-ii-iii pi3ks in cancer therapy: recent advances in tumor biology and preclinical research. Cancers, 15:784, Jan 2023. URL: https://doi.org/10.3390/cancers15030784, doi:10.3390/cancers15030784. This article has 36 citations.

7. (swamynathan2024dietaryprooxidanttherapy pages 8-9): Manojit M. Swamynathan, Shan Kuang, Kaitlin E. Watrud, Mary R. Doherty, Charlotte Gineste, Grinu Mathew, Grace Q. Gong, Hilary Cox, Eileen Cheng, David Reiss, Jude Kendall, Diya Ghosh, Colleen R. Reczek, Xiang Zhao, Tali Herzka, Saulė Špokaitė, Antoine N. Dessus, Seung Tea Kim, Olaf Klingbeil, Juan Liu, Dawid G. Nowak, Habeeb Alsudani, Tse-Luen Wee, Youngkyu Park, Francesca Minicozzi, Keith Rivera, Ana S. Almeida, Kenneth Chang, Ram P. Chakrabarty, John E. Wilkinson, Phyllis A. Gimotty, Sarah D. Diermeier, Mikala Egeblad, Christopher R. Vakoc, Jason W. Locasale, Navdeep S. Chandel, Tobias Janowitz, James B. Hicks, Michael Wigler, Darryl J. Pappin, Roger L. Williams, Paolo Cifani, David A. Tuveson, Jocelyn Laporte, and Lloyd C. Trotman. Dietary pro-oxidant therapy by a vitamin k precursor targets pi 3-kinase vps34 function. Science, Oct 2024. URL: https://doi.org/10.1126/science.adk9167, doi:10.1126/science.adk9167. This article has 41 citations and is from a highest quality peer-reviewed journal.

8. (wible2024unexpectedinhibitionof pages 1-3): Daric J. Wible, Zalak Parikh, Eun Jeong Cho, Miao-Der Chen, Collene R. Jeter, Somshuvra Mukhopadhyay, Kevin N. Dalby, Shankar Varadarajan, and Shawn B. Bratton. Unexpected inhibition of the lipid kinase pikfyve reveals an epistatic role for p38 mapks in endolysosomal fission and volume control. Cell Death &amp; Disease, Jan 2024. URL: https://doi.org/10.1038/s41419-024-06423-0, doi:10.1038/s41419-024-06423-0. This article has 19 citations and is from a peer-reviewed journal.

9. (swamynathan2024dietaryprooxidanttherapy pages 1-3): Manojit M. Swamynathan, Shan Kuang, Kaitlin E. Watrud, Mary R. Doherty, Charlotte Gineste, Grinu Mathew, Grace Q. Gong, Hilary Cox, Eileen Cheng, David Reiss, Jude Kendall, Diya Ghosh, Colleen R. Reczek, Xiang Zhao, Tali Herzka, Saulė Špokaitė, Antoine N. Dessus, Seung Tea Kim, Olaf Klingbeil, Juan Liu, Dawid G. Nowak, Habeeb Alsudani, Tse-Luen Wee, Youngkyu Park, Francesca Minicozzi, Keith Rivera, Ana S. Almeida, Kenneth Chang, Ram P. Chakrabarty, John E. Wilkinson, Phyllis A. Gimotty, Sarah D. Diermeier, Mikala Egeblad, Christopher R. Vakoc, Jason W. Locasale, Navdeep S. Chandel, Tobias Janowitz, James B. Hicks, Michael Wigler, Darryl J. Pappin, Roger L. Williams, Paolo Cifani, David A. Tuveson, Jocelyn Laporte, and Lloyd C. Trotman. Dietary pro-oxidant therapy by a vitamin k precursor targets pi 3-kinase vps34 function. Science, Oct 2024. URL: https://doi.org/10.1126/science.adk9167, doi:10.1126/science.adk9167. This article has 41 citations and is from a highest quality peer-reviewed journal.

10. (gong2024genomewidecrisprcas9screen pages 7-10): Mingli Gong, Cheng Peng, Chen Yang, Zhenhua Wang, Hongwu Qian, Xue Hu, Peng Zhou, Chao Shan, and Qiang Ding. Genome-wide crispr/cas9 screen identifies slc39a9 and pik3c3 as crucial entry factors for ebola virus infection. PLOS Pathogens, 20:e1012444, Aug 2024. URL: https://doi.org/10.1371/journal.ppat.1012444, doi:10.1371/journal.ppat.1012444. This article has 12 citations and is from a highest quality peer-reviewed journal.

11. (lee2024regulatorymechanismsgoverning pages 6-7): Yongook Lee, Nguyen Minh Tuan, Gi Jeong Lee, Boram Kim, Jung Ho Park, and Chang Hoon Lee. Regulatory mechanisms governing the autophagy-initiating vps34 complex and its inhibitors. Biomolecules & Therapeutics, 32:723-735, Oct 2024. URL: https://doi.org/10.4062/biomolther.2024.094, doi:10.4062/biomolther.2024.094. This article has 16 citations and is from a peer-reviewed journal.

## Citations

1. lee2024regulatorymechanismsgoverning pages 12-12
2. lee2024regulatorymechanismsgoverning pages 1-2
3. wan2023stingdirectlyrecruits pages 1-2
4. swamynathan2024dietaryprooxidanttherapy pages 8-9
5. chau2024thecellularadaptor pages 1-2
6. wible2024unexpectedinhibitionof pages 1-3
7. thibault2023targetingclassiiiiii pages 8-10
8. swamynathan2024dietaryprooxidanttherapy pages 1-3
9. lee2024regulatorymechanismsgoverning pages 6-7
10. https://doi.org/10.1126/science.adk9167
11. https://doi.org/10.1371/journal.ppat.1012444
12. https://doi.org/10.1038/s41419-024-06423-0
13. https://doi.org/10.15252/embj.2022112387
14. https://doi.org/10.1038/s41573-022-00582-5
15. https://doi.org/10.4062/biomolther.2024.094
16. https://doi.org/10.1007/s00018-024-05351-8
17. https://doi.org/10.1126/science.adk9167;
18. https://doi.org/10.1371/journal.ppat.1012444;
19. https://doi.org/10.1038/s41419-024-06423-0;
20. https://doi.org/10.3390/cancers15030784
21. https://doi.org/10.1038/s41573-022-00582-5,
22. https://doi.org/10.4062/biomolther.2024.094,
23. https://doi.org/10.1007/s00018-024-05351-8,
24. https://doi.org/10.15252/embj.2022112387,
25. https://doi.org/10.3390/cancers15030784,
26. https://doi.org/10.1126/science.adk9167,
27. https://doi.org/10.1038/s41419-024-06423-0,
28. https://doi.org/10.1371/journal.ppat.1012444,