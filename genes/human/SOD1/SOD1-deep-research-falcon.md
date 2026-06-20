---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T05:15:40.795510'
end_time: '2026-06-20T05:25:27.176338'
duration_seconds: 586.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: SOD1
  gene_symbol: SOD1
  uniprot_accession: P00441
  protein_description: 'RecName: Full=Superoxide dismutase [Cu-Zn] {ECO:0000305};
    EC=1.15.1.1 {ECO:0000269|PubMed:24140062}; EC=1.8.-.- {ECO:0000305}; AltName:
    Full=Hydrogen sulfide oxidase {ECO:0000303|PubMed:36630448}; AltName: Full=Superoxide
    dismutase 1; Short=hSod1;'
  gene_info: Name=SOD1 {ECO:0000312|HGNC:HGNC:11179};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the Cu-Zn superoxide dismutase family.
  protein_domains: SOD-like_Cu/Zn_dom_sf. (IPR036423); SOD_Cu/Zn_/chaperone. (IPR024134);
    SOD_Cu/Zn_BS. (IPR018152); SOD_Cu_Zn_dom. (IPR001424); Sod_Cu (PF00080)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: SOD1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P00441
- **Protein Description:** RecName: Full=Superoxide dismutase [Cu-Zn] {ECO:0000305}; EC=1.15.1.1 {ECO:0000269|PubMed:24140062}; EC=1.8.-.- {ECO:0000305}; AltName: Full=Hydrogen sulfide oxidase {ECO:0000303|PubMed:36630448}; AltName: Full=Superoxide dismutase 1; Short=hSod1;
- **Gene Information:** Name=SOD1 {ECO:0000312|HGNC:HGNC:11179};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the Cu-Zn superoxide dismutase family.
- **Key Domains:** SOD-like_Cu/Zn_dom_sf. (IPR036423); SOD_Cu/Zn_/chaperone. (IPR024134); SOD_Cu/Zn_BS. (IPR018152); SOD_Cu_Zn_dom. (IPR001424); Sod_Cu (PF00080)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SOD1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SOD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SOD1** (gene ID: SOD1, UniProt: P00441) in human.

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
- **UniProt Accession:** P00441
- **Protein Description:** RecName: Full=Superoxide dismutase [Cu-Zn] {ECO:0000305}; EC=1.15.1.1 {ECO:0000269|PubMed:24140062}; EC=1.8.-.- {ECO:0000305}; AltName: Full=Hydrogen sulfide oxidase {ECO:0000303|PubMed:36630448}; AltName: Full=Superoxide dismutase 1; Short=hSod1;
- **Gene Information:** Name=SOD1 {ECO:0000312|HGNC:HGNC:11179};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the Cu-Zn superoxide dismutase family.
- **Key Domains:** SOD-like_Cu/Zn_dom_sf. (IPR036423); SOD_Cu/Zn_/chaperone. (IPR024134); SOD_Cu/Zn_BS. (IPR018152); SOD_Cu_Zn_dom. (IPR001424); Sod_Cu (PF00080)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SOD1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SOD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SOD1** (gene ID: SOD1, UniProt: P00441) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: SOD1 (Superoxide Dismutase [Cu-Zn]) - Human Gene P00441

## Gene Identity Verification

The gene SOD1 (UniProt P00441) encodes human copper-zinc superoxide dismutase 1, confirmed as the correct target gene. This protein belongs to the Cu-Zn superoxide dismutase family and contains the conserved SOD_Cu_Zn_dom domain, matching the UniProt annotation for Homo sapiens (trist2021superoxidedismutase1 pages 1-3, trist2021superoxidedismutase1 pages 5-6).

## Primary Enzymatic Function and Catalytic Mechanism

### Core Enzymatic Activity

Human SOD1 catalyzes the dismutation of superoxide anion radicals (O2•−) to hydrogen peroxide (H2O2) and molecular oxygen (O2) via the reaction: **2O2•− + 2H+ → H2O2 + O2** (rosa2021superoxidedismutaseadministration pages 1-2, xu2022nuclearsod1in pages 1-2). The substrate specificity is highly selective for the superoxide anion radical, with the enzyme exhibiting exceptional catalytic efficiency at or near the diffusion limit (zheng2023theapplicationsand pages 1-2, boyd2020coppersourcesfor pages 1-3).

### Catalytic Mechanism

The catalytic mechanism depends on copper redox cycling between Cu(I) and Cu(II) oxidation states at the active site (boyd2020coppersourcesfor pages 1-3). In the first half-reaction, Cu(II) is reduced to Cu(I) while oxidizing one superoxide molecule to molecular oxygen. In the second half-reaction, Cu(I) is reoxidized to Cu(II) while reducing a second superoxide molecule to hydrogen peroxide. This reaction is facilitated by an "electrostatic guidance system" comprising positively charged residues in the electrostatic loop, particularly Arg143, which attracts the anionic substrate and excludes non-substrate molecules (zheng2023theapplicationsand pages 1-2, boyd2020coppersourcesfor pages 1-3).

### Substrate Recognition and Active Site Structure

Structural studies reveal that SOD1 is a homodimeric metalloprotein (~32 kDa) composed of two 153-amino acid monomers, each forming an eight-stranded β-barrel architecture (trist2021superoxidedismutase1 pages 5-6). The active site contains copper coordinated by four histidine residues (His46, His48, His63, His120) in a square-pyramidal geometry with a water ligand, while zinc is coordinated by His63, His71, His80, and Asp83 in a distorted tetrahedral arrangement (trist2021superoxidedismutase1 pages 5-6, boyd2020coppersourcesfor pages 1-3). Zinc binding stabilizes the active site architecture and is essential for proper protein folding and catalytic function, while copper performs the actual redox chemistry (boyd2020coppersourcesfor pages 1-3).

## Subcellular Localization

SOD1 exhibits a multi-compartmental distribution pattern. The protein is predominantly cytosolic, where it carries out its primary antioxidant function (xu2022nuclearsod1in pages 1-2). However, SOD1 is also localized to the mitochondrial intermembrane space, providing antioxidant protection in this organelle (trist2021superoxidedismutase1 pages 1-3, xu2022nuclearsod1in pages 1-2). Recent studies have identified substantial nuclear localization of SOD1 under both normal and pathological conditions, where it participates in oxidative stress response and may have regulatory roles in transcription and ribosome biogenesis (xu2022nuclearsod1in pages 1-2). Additionally, SOD1 can be secreted via unconventional secretory pathways and circulates in blood bound to lipoproteins, suggesting paracrine functions (damiano2020metabolismregulationand pages 1-3).

## Biochemical Pathways and Metabolic Regulation

### SOD1-Mediated Metabolic Reprogramming

Beyond its classical antioxidant role, SOD1 functions as a key regulator integrating oxygen availability with cellular metabolism (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4). A pivotal 2022 study demonstrated that SOD1 directly interacts with glyceraldehyde-3-phosphate dehydrogenase (GAPDH) and oxidizes its catalytic cysteine residue using SOD1-derived H2O2 (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4). This oxidative inactivation of GAPDH reduces glycolytic flux and reroutes glucose metabolism toward the oxidative pentose phosphate pathway (oxPPP), thereby increasing NADPH production (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4, chandel2021nadphtheforgottenreducing pages 1-3).

### Mechanism of GAPDH Regulation

Experimental evidence from co-immunoprecipitation and thiol alkylation assays confirms physical interaction between SOD1 and GAPDH (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4). The aerobic oxidation of GAPDH is both dependent on and rate-limited by SOD1, as demonstrated by dose-dependent increases in GAPDH oxidation with titrated SOD1 expression (montlloralbalate2022sod1integratesoxygen pages 3-4). Importantly, this regulatory mechanism requires the bulk of cellular SOD1 (~99%), distinguishing it from the direct superoxide scavenging function which requires less than 1% of total SOD1 (montlloralbalate2022sod1integratesoxygen pages 1-2).

### NADPH Production and Antioxidant Defense

The SOD1-mediated redirection of metabolism to the pentose phosphate pathway maintains cellular NADPH pools, which are essential for regenerating reduced glutathione (GSH) and thioredoxin (TRX), the major cellular antioxidant systems (chandel2021nadphtheforgottenreducing pages 1-3, damiano2020metabolismregulationand pages 1-3). This mechanism positions SOD1 as a master regulator of both oxidative stress defense and metabolic adaptation to aerobic conditions (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4). The pentose phosphate pathway generates NADPH through the oxidative phase catalyzed by glucose-6-phosphate dehydrogenase (G6PDH), providing reducing equivalents for biosynthetic reactions and antioxidant systems (chandel2021nadphtheforgottenreducing pages 1-3).

## Post-Translational Maturation

SOD1 requires multiple post-translational modifications to achieve full catalytic activity and structural stability (trist2021superoxidedismutase1 pages 5-6, boyd2020coppersourcesfor pages 1-3). Immature apo-SOD1 monomers undergo three critical modifications: (1) zinc binding at the metal-binding loop, (2) copper insertion at the active site mediated by the copper chaperone for SOD1 (CCS), and (3) formation of an intramolecular disulfide bond between Cys57 and Cys146 (trist2021superoxidedismutase1 pages 5-6, boyd2020coppersourcesfor pages 1-3). These modifications promote homodimerization, burying approximately 640 Å² of hydrophobic surface area and creating an exceptionally stable enzyme with a melting temperature of 85-95°C (trist2021superoxidedismutase1 pages 5-6). In contrast, apo-SOD1 has a melting temperature of only ~43°C, near physiological temperature, making it susceptible to degradation by the proteasome and autophagy systems (trist2021superoxidedismutase1 pages 5-6).

## Recent Discoveries: Hydrogen Sulfide Oxidase Activity

A novel non-canonical function of SOD1 has been identified in 2023, revealing that the enzyme can act as a hydrogen sulfide (H2S) oxidase (anwar2025therapeuticapplicationsand pages 1-3). The UniProt annotation for P00441 now includes the alternative name "Hydrogen sulfide oxidase" based on recent evidence showing that H2S binds at the copper active site of SOD1, where it functions as a micro-modulator regulating the enzyme's catalytic activity (anwar2025therapeuticapplicationsand pages 1-3). This finding expands our understanding of SOD1 beyond its traditional role in superoxide dismutation to include regulation by gaseous signaling molecules.

## Structural Features and Protein Domains

The mature SOD1 homodimer exhibits several structurally and functionally important features (trist2021superoxidedismutase1 pages 5-6). Each monomer contains a metal-binding loop (residues 49-83) that coordinates both copper and zinc ions. The disulfide loop (residues 49-62) contains Cys57, which forms the rare cytosolic disulfide bond with Cys146. The electrostatic loop contains positively charged residues that create an electrostatic field to guide negatively charged superoxide substrates into the active site channel. The Greek key loop (residues 102-115) contributes to dimer interface stability (trist2021superoxidedismutase1 pages 5-6). These structural elements work in concert to achieve the enzyme's remarkable catalytic efficiency and stability.

## Experimental Evidence and Methodological Approaches

The functional characterization of SOD1 has employed diverse experimental methodologies. Structural studies using X-ray crystallography and NMR spectroscopy have defined the atomic-level architecture and dynamics of SOD1 metalloforms (trist2021superoxidedismutase1 pages 5-6). Biochemical experiments using methoxypolyethylene glycol maleimide (mPEG-mal) thiol alkylation assays quantitatively measured GAPDH oxidation states in cells with varying SOD1 expression (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4). Co-immunoprecipitation experiments confirmed direct protein-protein interactions between SOD1 and GAPDH (montlloralbalate2022sod1integratesoxygen pages 1-2). Metabolic flux studies using pH-sensitive fluorescent reporters (pHluorin) demonstrated SOD1's regulation of glycolytic activity and the pentose phosphate pathway (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4). These precise, hypothesis-driven studies provide robust evidence for SOD1's multifaceted cellular roles.

## Signaling and Redox Regulation

SOD1-derived hydrogen peroxide functions as a redox signaling molecule beyond its role as a metabolic byproduct (montlloralbalate2022sod1integratesoxygen pages 1-2, damiano2020metabolismregulationand pages 1-3). H2O2 generated by SOD1 can diffuse across cellular membranes and oxidize specific protein thiols, thereby regulating enzyme activities, transcription factors, and signaling pathways (damiano2020metabolismregulationand pages 1-3). This positions SOD1 at the intersection of oxygen sensing, metabolic regulation, and redox signaling. The enzyme participates in the NRF2-mediated oxidative stress response pathway, which coordinates the expression of antioxidant genes (anwar2025therapeuticapplicationsand pages 1-3, damiano2020metabolismregulationand pages 1-3).

## Summary Table of Key Features

| Feature | Description | Evidence/Citation |
|---|---|---|
| Protein structure | Human SOD1 is a mature **~32 kDa homodimer** composed of two **153-aa monomers (~16 kDa each)**. Each monomer forms an **eight-stranded β-barrel** with prominent **metal-binding**, **disulfide**, **electrostatic**, and **Greek key** loop elements. The electrostatic loop helps steer anionic substrate into the active site, and the dimer interface buries substantial hydrophobic surface, contributing to exceptional stability of holo-SOD1. | (trist2021superoxidedismutase1 pages 5-6, boyd2020coppersourcesfor pages 1-3) |
| Metal cofactors | SOD1 is a **Cu/Zn metalloenzyme**. **Cu** at the catalytic site is coordinated by **His46, His48, His63, and His120**, with a water ligand completing a square-pyramidal geometry; these residues support Cu(I)/Cu(II) redox cycling. **Zn** is coordinated in a distorted tetrahedral site by **His63, His71, His80, and Asp83**, stabilizing the active-site architecture and loop conformations required for function. | (trist2021superoxidedismutase1 pages 5-6, boyd2020coppersourcesfor pages 1-3) |
| Primary enzymatic reaction | The canonical reaction is **superoxide dismutation**: **2 O2•− + 2 H+ → H2O2 + O2**. Thus, the **substrate specificity** is for the **superoxide anion radical (O2•−)**, and the products are **hydrogen peroxide** and **molecular oxygen**. This reaction is a first-line antioxidant defense against intracellular superoxide. | (rosa2021superoxidedismutaseadministration pages 1-2, xu2022nuclearsod1in pages 1-2, boyd2020coppersourcesfor pages 1-3) |
| Catalytic mechanism | Catalysis depends on **copper redox cycling** between **Cu(I)** and **Cu(II)** at the active site. One superoxide is oxidized to O2 while reducing Cu(II) to Cu(I); a second superoxide is then reduced to H2O2 as Cu(I) is reoxidized to Cu(II). Catalysis occurs at or near the **diffusion limit**, aided by an **electrostatic guidance system** in the electrostatic loop; **Arg143** is specifically important for substrate attraction and nonsubstrate exclusion. | (zheng2023theapplicationsand pages 1-2, boyd2020coppersourcesfor pages 1-3) |
| Subcellular localization | SOD1 is found primarily in the **cytosol**, but also in the **mitochondrial intermembrane space** and **nucleus** under normal and pathological conditions. Reviews also note **extracellular/secreted SOD1** via unconventional secretion and circulation in blood-associated compartments, extending function beyond the strictly intracellular space. | (rosa2021superoxidedismutaseadministration pages 1-2, xu2022nuclearsod1in pages 1-2, damiano2020metabolismregulationand pages 1-3) |
| Post-translational maturation requirements | Functional maturation requires **(1) Zn binding, (2) Cu insertion, (3) oxidation of the intramonomeric disulfide bond Cys57–Cys146, and (4) homodimerization**. The mature enzyme is highly stable, whereas **apo-SOD1** is markedly less stable. Copper incorporation is mediated by the **copper chaperone for SOD1 (CCS)**, and proper metallation/disulfide formation are essential for catalytic activity and structural integrity. | (trist2021superoxidedismutase1 pages 5-6, boyd2020coppersourcesfor pages 1-3) |
| Novel regulatory functions | Beyond detoxifying superoxide, SOD1-derived **H2O2** can function in **redox signaling**. Experimental work showed SOD1 **interacts with GAPDH**, promotes **GAPDH thiol oxidation**, lowers GAPDH activity, and thereby helps reroute carbon flux from **glycolysis** to the **oxidative pentose phosphate pathway**, increasing **NADPH** production and oxidative-stress resistance. This places SOD1 as a regulator of metabolic adaptation, not just a scavenger enzyme. | (montlloralbalate2022sod1integratesoxygen pages 1-2, montlloralbalate2022sod1integratesoxygen pages 3-4, damiano2020metabolismregulationand pages 1-3) |
| Hydrogen sulfide oxidase activity | Recent literature and UniProt-linked annotation indicate a **non-canonical H2S-related activity** for Cu/Zn-SOD1, including description as **“hydrogen sulfide oxidase”** and evidence that **H2S binds at the copper active site** to modulate catalytic behavior. Available accessible review sources describe this as a newly emerging role of SOD1 beyond classical superoxide dismutation; however, mechanistic depth is more limited in the presently available contexts than for canonical activity. | (anwar2025therapeuticapplicationsand pages 1-3, boyd2020coppersourcesfor pages 1-3) |


*Table: This table compiles the main structural, catalytic, localization, maturation, and emerging regulatory properties of human SOD1. It is useful as a compact evidence-based reference for functional annotation of UniProt P00441.*

## Conclusion

Human SOD1 (UniProt P00441) is a highly conserved Cu-Zn metalloenzyme that serves as a critical first-line antioxidant defense by catalyzing superoxide dismutation to hydrogen peroxide and molecular oxygen. Beyond this canonical function, SOD1 acts as a metabolic regulator by oxidizing GAPDH to redirect glucose metabolism toward NADPH production via the pentose phosphate pathway. The enzyme exhibits multi-compartmental localization including cytosol, mitochondria, and nucleus, with emerging evidence for extracellular functions. Recent discoveries of H2S oxidase activity further expand SOD1's functional repertoire. The enzyme's structure, comprising an eight-stranded β-barrel homodimer with precisely coordinated copper and zinc ions, enables its exceptional catalytic efficiency and stability. These findings establish SOD1 as a multifunctional protein integrating antioxidant defense, metabolic regulation, and cellular signaling in response to oxygen availability and oxidative stress.

References

1. (trist2021superoxidedismutase1 pages 1-3): Benjamin G. Trist, James B. Hilton, Dominic J. Hare, Peter J. Crouch, and Kay L. Double. Superoxide dismutase 1 in health and disease: how a frontline antioxidant becomes neurotoxic. Nov 2021. URL: https://doi.org/10.1002/anie.202000451, doi:10.1002/anie.202000451. This article has 260 citations.

2. (trist2021superoxidedismutase1 pages 5-6): Benjamin G. Trist, James B. Hilton, Dominic J. Hare, Peter J. Crouch, and Kay L. Double. Superoxide dismutase 1 in health and disease: how a frontline antioxidant becomes neurotoxic. Nov 2021. URL: https://doi.org/10.1002/anie.202000451, doi:10.1002/anie.202000451. This article has 260 citations.

3. (rosa2021superoxidedismutaseadministration pages 1-2): Arianna Carolina Rosa, Daniele Corsi, Niccolò Cavi, Natascia Bruni, and Franco Dosio. Superoxide dismutase administration: a review of proposed human uses. Molecules, 26:1844, Mar 2021. URL: https://doi.org/10.3390/molecules26071844, doi:10.3390/molecules26071844. This article has 338 citations.

4. (xu2022nuclearsod1in pages 1-2): Joyce Xu, Xiaoyang Su, Stephen K. Burley, and X. F. Steven Zheng. Nuclear sod1 in growth control, oxidative stress response, amyotrophic lateral sclerosis, and cancer. Antioxidants, 11:427, Feb 2022. URL: https://doi.org/10.3390/antiox11020427, doi:10.3390/antiox11020427. This article has 95 citations.

5. (zheng2023theapplicationsand pages 1-2): Mengli Zheng, Yating Liu, Guanfeng Zhang, Zhikang Yang, Weiwei Xu, and Qinghua Chen. The applications and mechanisms of superoxide dismutase in medicine, food, and cosmetics. Antioxidants, 12:1675, Aug 2023. URL: https://doi.org/10.3390/antiox12091675, doi:10.3390/antiox12091675. This article has 386 citations.

6. (boyd2020coppersourcesfor pages 1-3): Stefanie D. Boyd, Morgan S. Ullrich, Amelie Skopp, and Duane D. Winkler. Copper sources for sod1 activation. Antioxidants, 9:500, Jun 2020. URL: https://doi.org/10.3390/antiox9060500, doi:10.3390/antiox9060500. This article has 87 citations.

7. (damiano2020metabolismregulationand pages 1-3): Simona Damiano, Concetta Sozio, Giuliana La Rosa, Bruna Guida, Raffaella Faraonio, Mariarosaria Santillo, and Paolo Mondola. Metabolism regulation and redox state: insight into the role of superoxide dismutase 1. International Journal of Molecular Sciences, 21:6606, Sep 2020. URL: https://doi.org/10.3390/ijms21186606, doi:10.3390/ijms21186606. This article has 68 citations.

8. (montlloralbalate2022sod1integratesoxygen pages 1-2): Claudia Montllor-Albalate, Hyojung Kim, Anna E. Thompson, Alex P. Jonke, Matthew P. Torres, and Amit R. Reddi. Sod1 integrates oxygen availability to redox regulate nadph production and the thiol redoxome. Dec 2022. URL: https://doi.org/10.1073/pnas.2023328119, doi:10.1073/pnas.2023328119. This article has 92 citations and is from a highest quality peer-reviewed journal.

9. (montlloralbalate2022sod1integratesoxygen pages 3-4): Claudia Montllor-Albalate, Hyojung Kim, Anna E. Thompson, Alex P. Jonke, Matthew P. Torres, and Amit R. Reddi. Sod1 integrates oxygen availability to redox regulate nadph production and the thiol redoxome. Dec 2022. URL: https://doi.org/10.1073/pnas.2023328119, doi:10.1073/pnas.2023328119. This article has 92 citations and is from a highest quality peer-reviewed journal.

10. (chandel2021nadphtheforgottenreducing pages 1-3): Navdeep S. Chandel. Nadph-the forgotten reducing equivalent. Cold Spring Harbor perspectives in biology, 13 6:a040550, Jun 2021. URL: https://doi.org/10.1101/cshperspect.a040550, doi:10.1101/cshperspect.a040550. This article has 160 citations and is from a peer-reviewed journal.

11. (anwar2025therapeuticapplicationsand pages 1-3): S. Anwar, Tarique Sarwar, Amjad Ali Khan, and A. Rahmani. Therapeutic applications and mechanisms of superoxide dismutase (sod) in different pathogenesis. Biomolecules, Aug 2025. URL: https://doi.org/10.3390/biom15081130, doi:10.3390/biom15081130. This article has 60 citations.

## Artifacts

- [Edison artifact artifact-00](SOD1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. boyd2020coppersourcesfor pages 1-3
2. damiano2020metabolismregulationand pages 1-3
3. chandel2021nadphtheforgottenreducing pages 1-3
4. anwar2025therapeuticapplicationsand pages 1-3
5. rosa2021superoxidedismutaseadministration pages 1-2
6. zheng2023theapplicationsand pages 1-2
7. Cu-Zn
8. https://doi.org/10.1002/anie.202000451,
9. https://doi.org/10.3390/molecules26071844,
10. https://doi.org/10.3390/antiox11020427,
11. https://doi.org/10.3390/antiox12091675,
12. https://doi.org/10.3390/antiox9060500,
13. https://doi.org/10.3390/ijms21186606,
14. https://doi.org/10.1073/pnas.2023328119,
15. https://doi.org/10.1101/cshperspect.a040550,
16. https://doi.org/10.3390/biom15081130,