---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T17:03:40.590078'
end_time: '2026-06-11T17:24:11.036624'
duration_seconds: 1230.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fur
  gene_symbol: fur
  uniprot_accession: Q88DT9
  protein_description: 'RecName: Full=Ferric uptake regulation protein {ECO:0000256|ARBA:ARBA00020910,
    ECO:0000256|RuleBase:RU364037};'
  gene_info: Name=fur {ECO:0000256|RuleBase:RU364037, ECO:0000313|EMBL:AAN70302.1};
    OrderedLocusNames=PP_4730 {ECO:0000313|EMBL:AAN70302.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the Fur family. {ECO:0000256|ARBA:ARBA00007957,
  protein_domains: FUR. (IPR002481); Fur_C. (IPR043135); WH-like_DNA-bd_sf. (IPR036388);
    WH_DNA-bd_sf. (IPR036390); FUR (PF01475)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: fur-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q88DT9
- **Protein Description:** RecName: Full=Ferric uptake regulation protein {ECO:0000256|ARBA:ARBA00020910, ECO:0000256|RuleBase:RU364037};
- **Gene Information:** Name=fur {ECO:0000256|RuleBase:RU364037, ECO:0000313|EMBL:AAN70302.1}; OrderedLocusNames=PP_4730 {ECO:0000313|EMBL:AAN70302.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the Fur family. {ECO:0000256|ARBA:ARBA00007957,
- **Key Domains:** FUR. (IPR002481); Fur_C. (IPR043135); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390); FUR (PF01475)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fur" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fur' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fur** (gene ID: fur, UniProt: Q88DT9) in PSEPK.

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
- **UniProt Accession:** Q88DT9
- **Protein Description:** RecName: Full=Ferric uptake regulation protein {ECO:0000256|ARBA:ARBA00020910, ECO:0000256|RuleBase:RU364037};
- **Gene Information:** Name=fur {ECO:0000256|RuleBase:RU364037, ECO:0000313|EMBL:AAN70302.1}; OrderedLocusNames=PP_4730 {ECO:0000313|EMBL:AAN70302.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the Fur family. {ECO:0000256|ARBA:ARBA00007957,
- **Key Domains:** FUR. (IPR002481); Fur_C. (IPR043135); WH-like_DNA-bd_sf. (IPR036388); WH_DNA-bd_sf. (IPR036390); FUR (PF01475)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fur" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fur' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fur** (gene ID: fur, UniProt: Q88DT9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: **fur** (Ferric uptake regulation protein) in *Pseudomonas putida* KT2440 (UniProt: Q88DT9)

## 0. Target verification (critical identity checks)

**Target specified by user:** UniProt **Q88DT9**, protein name **Ferric uptake regulation protein (Fur)**, gene **fur**, ordered locus **PP_4730**, organism ***Pseudomonas putida* strain KT2440**.

**Verification outcome:** The literature retrieved here contains **direct experimental evidence for a Fur regulator in *P. putida* KT2440** controlling iron-responsive expression of iron-storage genes (bacterioferritins) and influencing oxidative-stress phenotypes in a **fur mutant** background, consistent with the UniProt-provided identity. However, within the accessible full texts **we did not retrieve a paper that explicitly mentions UniProt accession Q88DT9 or locus tag PP_4730**, so the **accession↔locus mapping relies on the user-provided UniProt record**. All KT2440-specific functional claims below are cited from KT2440 studies; broader mechanistic statements about Fur come from authoritative cross-bacterial reviews and Pseudomonas primary literature and are explicitly labeled as such. (chen2010molecularanalysisof pages 5-6, chen2010molecularanalysisof pages 1-2)

## 1. Key concepts and definitions (current understanding)

### 1.1 What Fur is
**Fur (ferric uptake regulator)** is the founding member of the FUR superfamily of bacterial metalloregulatory transcription factors that control metal homeostasis. Canonically, **Fe-bound Fur (holo-Fur)** binds DNA at operator sites (often called **Fur boxes**) to regulate gene expression as iron availability changes. (steingard2023meddlingwithmetal pages 1-2, steingard2023meddlingwithmetal pages 2-5)

### 1.2 Fur as an iron-dependent transcriptional regulator: repression, indirect activation, and network integration
Across bacteria, **holo-Fur most commonly acts as a repressor** of genes involved in iron acquisition and the “iron-sparing” response; conversely, **iron limitation leads to Fur demetallation and promoter release**, permitting transcription. Fur can also **indirectly activate** genes (e.g., by repressing small RNAs) and, in some organisms, apo-Fur can participate in activation. Fur also frequently integrates signals via cooperative/competitive interactions with other regulators at shared promoter regions. (steingard2023meddlingwithmetal pages 2-5, steingard2023meddlingwithmetal pages 1-2)

### 1.3 Fur boxes (operator DNA recognition)
Operator recognition is often described using:
- A **19-bp inverted repeat** Fur box model (e.g., 5′-GATAATGATAATCATTATC-3′) (crosa1997signaltransductionand pages 1-2, kang2024structuralperspectiveson pages 6-7)
- Or an overlapping **7-1-7 motif** view of the Fur box (consensus reported as **TGATAATnATTATCA**) (steingard2023meddlingwithmetal pages 2-5)

### 1.4 Why Fur matters physiologically
Iron is essential for redox chemistry and respiration but dangerous when unbuffered because it can promote reactive oxygen species (ROS) via Fenton chemistry. Therefore, **iron uptake, storage, and utilization are tightly regulated and coupled to oxidative-stress defenses**, and Fur sits at the center of this regulation in many bacteria. (steingard2023meddlingwithmetal pages 1-2, stein2023navigatingpyoverdineand pages 18-22)

## 2. Molecular function and mechanism of Fur (with structural context)

### 2.1 Domain architecture and oligomerization
Recent structural syntheses emphasize that Fur proteins are typically **two-domain** regulators:
- **N-terminal DNA-binding domain (DBD)** (helix-turn-helix architecture)
- **C-terminal dimerization domain (DD)**
Fur commonly exists as a **dimer in solution**, but **tetramers and higher-order DNA-bound assemblies** can occur and may influence which operator classes are bound. (kang2024structuralperspectiveson pages 1-2, kang2024structuralperspectiveson pages 7-9)

### 2.2 Metal-binding sites and conformational switching
A modern consensus from structural reviews is that Fur proteins often contain **three metal-binding sites (S1/S2/S3)**, with **S2 functioning as the key regulatory iron-sensing site** that drives conformational changes required for high-affinity DNA binding. In this framework:
- **Apo-Fur** adopts a more “open” conformation that is less DNA-binding competent.
- **Fe(II) (or other divalent metals at the regulatory site)** induces a “closed” DNA-binding competent state by repositioning the DBD relative to the DD.
Structural sites can also bind Zn(II) (often for stability), and some homologs can be mismetalated by noncognate ions (e.g., Mn(II)), which can misregulate iron responses. (kang2024structuralperspectiveson pages 1-2, kang2024structuralperspectiveson pages 6-7, steingard2023meddlingwithmetal pages 1-2)

Quantitative metal-binding observations summarized in the 2024 structural review include that, in some systems, **Zn(II) can bind more tightly than Fe(II)/Mn(II)** and reported Fe(II)/Mn(II) affinities can be on the order of ~µM in certain assays, emphasizing the importance of metal availability and competition in vivo. (kang2024structuralperspectiveson pages 4-6)

### 2.3 Evidence for Fur box binding and repression logic (Pseudomonas and general)
Foundational mechanistic work (across bacteria) established that Fur is an **iron-dependent repressor** and that metal (often Mn(II) in vitro as a surrogate) can dramatically enhance DNA binding to Fur boxes. (crosa1997signaltransductionand pages 1-2)

In **Pseudomonas aeruginosa**, Fur has been purified and shown to bind Fur boxes in promoters of **siderophore regulatory genes pvdS and pchR**, consistent with **Fur-Fe(II) repressing siderophore production pathways** when iron is sufficient. (Ochsner et al., 1995; publication date Dec 1995; https://doi.org/10.1128/jb.177.24.7194-7201.1995) (ochsner1995roleofthe pages 1-2)

## 3. *Pseudomonas putida* KT2440-specific functional annotation of Fur

### 3.1 Primary biological role in KT2440: coordinating iron storage and oxidative-stress tolerance
The strongest KT2440-specific experimental evidence retrieved here connects Fur to **iron storage** via bacterioferritins.

**Bacterioferritin genes bfrα and bfrβ are Fur-dependent in KT2440.** Chen et al. (Applied and Environmental Microbiology; Aug 2010; https://doi.org/10.1128/AEM.00215-10) used a **fur deletion mutant** and **luciferase reporter fusions** to quantify expression of two bacterioferritin genes (bfrα and bfrβ) under iron manipulation, finding that Fur has a **positive regulatory effect** on bfr expression, particularly under high-iron conditions. (chen2010molecularanalysisof pages 5-6, chen2010molecularanalysisof pages 6-8)

**Quantitative KT2440 data (Chen et al., 2010):**
- Under high iron, bfrα and bfrβ expression in Fur+ cells was ~**3-fold** and **6-fold** higher than in a Fur mutant. (chen2010molecularanalysisof pages 6-8)
- The fur mutant displayed **greater H2O2 sensitivity** (disk diffusion zone ~**5.6 cm**) than wild-type and bacterioferritin mutants (~**3.5 ± 0.2 cm**), consistent with Fur controlling broader ROS-relevant functions beyond bacterioferritin alone. (chen2010molecularanalysisof pages 6-8)

**Mechanistic nuance in KT2440:** Despite Fur-dependence, Chen et al. report that **canonical Fur box motifs were not detected upstream of bfrα/bfrβ**, implying regulation may be **indirect or mediated by noncanonical binding/other factors** in KT2440. (chen2010molecularanalysisof pages 4-5)

### 3.2 Pathways and processes Fur connects to in KT2440 iron homeostasis

#### (A) Iron storage: bacterioferritins (direct KT2440 evidence)
In KT2440, bacterioferritins contribute measurably to intracellular iron buffering:
- Single bfr mutants show ~**16–18%** reduction in total cellular iron (log phase), and a double mutant shows ~**38%** reduction (stationary phase). (chen2010molecularanalysisof pages 5-6, chen2010molecularanalysisof pages 6-8)
- The double mutant shows **reduced growth under low-iron conditions**, whereas growth in high iron is not significantly different. (chen2010molecularanalysisof pages 5-6)
These effects support a model in which Fur-dependent tuning of iron storage helps maintain iron availability while limiting iron-driven oxidative damage. (chen2010molecularanalysisof pages 8-8)

#### (B) Siderophore-mediated iron acquisition: pyoverdine context (KT2440 and pseudomonad context)
A Pseudomonas-focused review reports that **Fur is the major iron-responsive global regulator in pseudomonads**, and it provides KT2440-specific ecological constraints on iron acquisition:
- KT2440 appears to rely primarily on **pyoverdine** as its siderophore: **pyoverdine-negative mutants show no detectable siderophore activity**.
- KT2440 is reported to **utilize only its own ferripyoverdine** (limited xenosiderophore use). (Cornelis, Mar 2010; https://doi.org/10.1007/s00253-010-2550-2) (cornelis2010ironuptakeand pages 4-6)

Although the retrieved KT2440 papers here do not directly map Fur binding to pyoverdine promoters, primary mechanistic evidence from *P. aeruginosa* demonstrates that Fur can repress key siderophore regulators (pvdS/pchR), supporting the inference that Fur generally sits upstream of siderophore control in pseudomonads. (ochsner1995roleofthe pages 1-2)

#### (C) Iron–oxidative stress coupling in KT2440 (direct and contextual evidence)
A KT2440 study (Barrientos-Moreno et al., Journal of Bacteriology; Nov 2019; https://doi.org/10.1128/jb.00454-19) shows that **pyoverdine production/release** is functionally linked to oxidative-stress adaptation through arginine/polyamine metabolism:
- Arginine biosynthesis mutants show reduced pyoverdine production/release and increased sensitivity to iron limitation.
- Spermidine protects against hydrogen peroxide, while defects in arginine and pyoverdine synthesis increase ROS. (barrientosmoreno2019argininebiosynthesismodulates pages 1-2, barrientosmoreno2019argininebiosynthesismodulates pages 2-5)
This supports the broader principle that KT2440 must balance iron capture with oxidative-stress control; Fur is a plausible upstream regulator of that balance even when specific promoter-level evidence in KT2440 is incomplete in the retrieved set. (steingard2023meddlingwithmetal pages 1-2)

## 4. Subcellular localization
Fur is a **cytosolic DNA-binding transcription factor**: it senses intracellular metal availability and binds chromosomal operators to regulate transcription. This is consistent with the structural and mechanistic view of Fur as a metal-dependent dimeric regulator acting on promoter regions. (kang2024structuralperspectiveson pages 1-2, steingard2023meddlingwithmetal pages 1-2)

## 5. Recent developments (prioritizing 2023–2024)

### 5.1 Fur as a “signaling hub” (2023)
A 2023 Journal of Bacteriology review frames Fur-family regulators as **signal-integration hubs** with emerging allosteric regulation, multi-protein interactions, and dynamic DNA occupancy that can tune response kinetics. This is relevant for interpreting how KT2440 Fur might integrate iron with other stresses (e.g., oxygen/redox state, noncognate metals). (Steingard & Helmann; Apr 2023; https://doi.org/10.1128/jb.00022-23) (steingard2023meddlingwithmetal pages 2-5)

### 5.2 Structural modernization of Fur models (2024)
A 2024 Biomolecules review consolidates current Fur structural understanding: explicit **S1/S2/S3 site models**, metal-dependent conformational switching, and operator-binding architectures (dimer vs dimer-of-dimers vs tetramer), and discusses Fur as a potential antimicrobial target. These developments strengthen confidence in annotation of Q88DT9 as a canonical Fur-family metalloregulator. (Kang et al.; Aug 2024; https://doi.org/10.3390/biom14080981) (kang2024structuralperspectiveson pages 1-2, kang2024structuralperspectiveson pages 4-6)

### 5.3 New Fur-adjacent regulatory circuitry affecting siderophores in Pseudomonas (2024)
A 2024 Communications Biology study identifies an **osmotic-stress-responsive two-component system (BfmRS)** that directly activates siderophore gene clusters (pvd/fpv/femARI) in *P. aeruginosa*. Importantly for KT2440, the paper reports **functional evidence that BfmR homologs from *P. putida* KT2440 can bind promoters of key siderophore genes and that osmolality-mediated increases in siderophore production occur**, indicating additional non-Fur inputs to iron acquisition regulation in KT2440-like pseudomonads. (Song et al.; Mar 2024; https://doi.org/10.1038/s42003-024-05995-z) (song2024molecularmechanismof pages 1-2)

## 6. Current applications and real-world implementations (why Fur annotation matters)

### 6.1 Environmental survival and rhizosphere fitness
Iron acquisition via siderophores (primarily pyoverdine in KT2440) is central to survival in iron-limited soil/rhizosphere environments; tight regulation is required to avoid ROS costs. KT2440-specific studies show that metabolic state (arginine/polyamines) affects pyoverdine and oxidative-stress resilience, demonstrating that iron acquisition regulation is intertwined with stress physiology relevant to plant-associated niches. (barrientosmoreno2019argininebiosynthesismodulates pages 1-2)

### 6.2 Industrial biotechnology and chassis engineering
*P. putida* KT2440 is widely used as a chassis for chemical production and environmental biotechnology; iron availability affects respiration, enzyme cofactor supply, oxidative stress, and thus productivity. Evidence that Fur controls iron storage (bfr genes) and that KT2440 has limited xenosiderophore utilization suggests that **media iron management and regulatory engineering (directly or indirectly involving Fur-controlled modules)** can be important for stable performance under scale-up or stress conditions. (chen2010molecularanalysisof pages 5-6, cornelis2010ironuptakeand pages 4-6)

### 6.3 Bioremediation context (iron chemistry and metallophore promiscuity)
Siderophores can bind metals beyond iron (e.g., Ga, Al, Ni, Co, Cu), and some siderophore systems are implicated in pollutant transformation; this connects iron-regulatory networks to environmental applications. KT2440’s iron acquisition specialization (pyoverdine-centered) shapes how it competes and mobilizes metals in complex matrices. (cornelis2010ironuptakeand pages 4-6)

## 7. Key statistics and data summary (recent and foundational)

- **KT2440 Fur-dependent bfr regulation:** bfrα/bfrβ expression ~3×/~6× higher in Fur+ vs Fur− under high iron (Chen et al., 2010). (chen2010molecularanalysisof pages 6-8)
- **Iron manipulation conditions (KT2440 study):** low iron with **200 µM 2,2′-dipyridyl**; high iron with **15 µM FeCl3** (Chen et al., 2010). (chen2010molecularanalysisof pages 5-6)
- **Iron storage phenotypes:** single bfr deletions reduce cellular iron by ~16–18%; double deletion reduces total iron by ~38% and compromises growth in low iron (Chen et al., 2010). (chen2010molecularanalysisof pages 5-6)
- **Oxidative stress phenotype:** H2O2 inhibition zone ~5.6 cm for fur mutant vs ~3.5 ± 0.2 cm for WT/bfr mutants (Chen et al., 2010). (chen2010molecularanalysisof pages 6-8)
- **Fur box models:** 19-bp inverted repeat and 7-1-7 overlapping motifs (Crosa 1997; Steingard & Helmann 2023). (crosa1997signaltransductionand pages 1-2, steingard2023meddlingwithmetal pages 2-5)
- **KT2440 siderophore specialization:** pyoverdine-negative mutants have no siderophore activity; KT2440 uses mainly its own ferripyoverdine (Cornelis 2010). (cornelis2010ironuptakeand pages 4-6)

## 8. Confidence and limitations (KT2440-specific vs inferred)

- **High confidence (KT2440-specific):** Fur influences iron storage gene expression (bfrα/bfrβ) and oxidative-stress phenotype based on a KT2440 fur mutant and reporter assays. (chen2010molecularanalysisof pages 5-6, chen2010molecularanalysisof pages 6-8)
- **Moderate confidence (KT2440 context):** Fur is a central global regulator of iron acquisition in pseudomonads, and KT2440’s iron acquisition is pyoverdine-centered with limited xenosiderophore use; thus Fur is expected to sit upstream of iron uptake/storage balancing. (cornelis2010ironuptakeand pages 4-6)
- **Lower confidence / not directly supported in retrieved KT2440 full text:** exact KT2440 Fur regulon size, direct Fur binding to KT2440 pyoverdine promoters, and precise Fur-box instances in KT2440 promoters. These remain gaps in the retrieved evidence set.

## Summary
Fur (UniProt Q88DT9; gene fur; KT2440) is best annotated as a **cytosolic, metal-dependent transcriptional regulator** that senses intracellular iron and coordinates expression programs for iron homeostasis. In KT2440, the clearest direct evidence is Fur-dependent control of **bacterioferritin iron storage genes (bfrα/bfrβ)** and a measurable oxidative-stress phenotype in a fur mutant. Modern 2023–2024 reviews refine Fur’s mechanism as a multi-site metalloregulator with metal-triggered conformational switching and complex DNA-binding architectures, while 2024 primary work in Pseudomonas adds additional Fur-adjacent control of siderophore expression through osmotic-stress signaling with demonstrated promoter binding by a KT2440 homolog.

| Aspect | Key points | Best supporting sources (with year) | URLs/DOIs |
|---|---|---|---|
| Identity | UniProt Q88DT9 corresponds to **Fur, ferric uptake regulator**, in *Pseudomonas putida* KT2440 (gene **fur**, locus **PP_4730** per supplied target context). Evidence directly supporting KT2440 Fur function is organism-specific for iron-responsive regulation, though explicit PP_4730 naming was limited in retrieved papers. Fur-family assignment is strongly supported by conserved two-domain Fur architecture and iron-homeostasis role. (chen2010molecularanalysisof pages 5-6, kang2024structuralperspectiveson pages 1-2) | Chen et al., 2010; Kang et al., 2024 | https://doi.org/10.1128/AEM.00215-10; https://doi.org/10.3390/biom14080981 |
| Molecular function | Fur is a **metal-dependent transcriptional regulator** that usually represses iron-acquisition genes when metal bound; it can also positively affect some genes indirectly. In KT2440, Fur positively affects **bfrα/bfrβ** expression, even though upstream canonical Fur boxes were not detected, implying indirect or noncanonical control. (chen2010molecularanalysisof pages 5-6, chen2010molecularanalysisof pages 6-8, chen2010molecularanalysisof pages 4-5, steingard2023meddlingwithmetal pages 1-2) | Chen et al., 2010; Steingard & Helmann, 2023 | https://doi.org/10.1128/AEM.00215-10; https://doi.org/10.1128/JB.00022-23 |
| Metal sensing | Fur proteins have conserved metal-binding sites **S1/S2/S3**; **S2** is the key regulatory iron-sensing site, while S1 often contributes structural stability and S3 can modulate conformation/oligomerization. Metal loading converts Fur from a less DNA-binding-competent open state to a DNA-binding-competent closed state. Reported affinities in structural studies show Zn²⁺ can bind more tightly than Fe²⁺/Mn²⁺ in some homologs. (kang2024structuralperspectiveson pages 1-2, kang2024structuralperspectiveson pages 6-7, kang2024structuralperspectiveson pages 4-6, steingard2023meddlingwithmetal pages 1-2) | Kang et al., 2024; Steingard & Helmann, 2023 | https://doi.org/10.3390/biom14080981; https://doi.org/10.1128/JB.00022-23 |
| DNA binding / Fur box | Fur has an N-terminal DNA-binding domain and C-terminal dimerization domain; it typically binds DNA as a dimer or dimer-of-dimers. Canonical Fur boxes are described as a **19-bp inverted repeat** or overlapping **7-1-7 motifs** with consensus like **TGATAATnATTATCA** / **GATAATGATAATCATTATC**. For KT2440 **bfrα/bfrβ**, no canonical Fur box was detected, suggesting noncanonical or indirect regulation. (chen2010molecularanalysisof pages 4-5, kang2024structuralperspectiveson pages 2-4, kang2024structuralperspectiveson pages 6-7, steingard2023meddlingwithmetal pages 2-5) | Chen et al., 2010; Kang et al., 2024; Steingard & Helmann, 2023 | https://doi.org/10.1128/AEM.00215-10; https://doi.org/10.3390/biom14080981; https://doi.org/10.1128/JB.00022-23 |
| Regulon examples | Best-supported KT2440 targets from retrieved evidence are **bfrα** and **bfrβ** (bacterioferritins), positively influenced by Fur. More broadly in pseudomonads, Fur controls iron-acquisition circuits including siderophore pathways via regulators such as **pvdS/pchR** in *P. aeruginosa*; this supports cautious inference that KT2440 Fur sits upstream of iron uptake and storage homeostasis, but organism-specific direct regulon mapping remains limited here. (chen2010molecularanalysisof pages 5-6, chen2010molecularanalysisof pages 6-8, ochsner1995roleofthe pages 1-2) | Chen et al., 2010; Ochsner et al., 1995 | https://doi.org/10.1128/AEM.00215-10; https://doi.org/10.1128/JB.177.24.7194-7201.1995 |
| Localization | Fur is a **cytosolic DNA-binding regulator** acting on chromosomal promoters/operator regions. Its function depends on intracellular metal availability rather than secretion or membrane localization. (kang2024structuralperspectiveson pages 1-2, kang2024structuralperspectiveson pages 2-4, steingard2023meddlingwithmetal pages 1-2) | Kang et al., 2024; Steingard & Helmann, 2023 | https://doi.org/10.3390/biom14080981; https://doi.org/10.1128/JB.00022-23 |
| Phenotypes | In KT2440, loss of Fur is associated with **greater H₂O₂ sensitivity** than bacterioferritin mutants, consistent with a broader iron/ROS homeostasis role. Fur-dependent control of bacterioferritins supports tolerance to iron starvation and oxidative stress indirectly through proper iron storage/homeostasis. (chen2010molecularanalysisof pages 6-8, chen2010molecularanalysisof pages 8-8) | Chen et al., 2010 | https://doi.org/10.1128/AEM.00215-10 |
| Quantitative data | In KT2440, under high-iron conditions, **bfrα** and **bfrβ** expression were about **3-fold** and **6-fold** higher in Fur⁺ than Fur⁻ cells; under low iron, differences were ~**0.5-fold** and **1.2-fold**. Single **bfr** mutants had ~**16–18%** lower cellular iron, while the double mutant had ~**38%** lower iron; Fur mutant H₂O₂ inhibition zone was ~**5.6 cm** vs ~**3.5 ± 0.2 cm** for bacterioferritin mutants. (chen2010molecularanalysisof pages 5-6, chen2010molecularanalysisof pages 6-8, chen2010molecularanalysisof pages 1-2) | Chen et al., 2010 | https://doi.org/10.1128/AEM.00215-10 |
| Recent developments 2023-2024 | Recent reviews refined Fur understanding by emphasizing **metal-dependent conformational switching**, multiple metal sites, **dimer/tetramer** behavior, and nuanced operator architectures; Fur-family proteins are now viewed as broader **signaling hubs** integrating iron with other regulators and ligands. These advances strengthen functional inference for KT2440 Fur even where direct 2023-2024 KT2440 primary studies are sparse. (kang2024structuralperspectiveson pages 1-2, kang2024structuralperspectiveson pages 7-9, steingard2023meddlingwithmetal pages 1-2, steingard2023meddlingwithmetal pages 2-5) | Steingard & Helmann, 2023; Kang et al., 2024 | https://doi.org/10.1128/JB.00022-23; https://doi.org/10.3390/biom14080981 |


*Table: This table summarizes the best-supported functional annotation for *Pseudomonas putida* KT2440 Fur (UniProt Q88DT9), separating direct KT2440 evidence from broader Fur-family mechanistic inference. It is useful for quickly identifying molecular function, regulatory logic, phenotypes, and the strongest recent sources.*

References

1. (chen2010molecularanalysisof pages 5-6): Shicheng Chen, William F. Bleam, and William J. Hickey. Molecular analysis of two bacterioferritin genes, <i>bfr</i> α and <i>bfr</i> β, in the model rhizobacterium <i>pseudomonas putida</i> kt2440. Aug 2010. URL: https://doi.org/10.1128/aem.00215-10, doi:10.1128/aem.00215-10. This article has 20 citations and is from a peer-reviewed journal.

2. (chen2010molecularanalysisof pages 1-2): Shicheng Chen, William F. Bleam, and William J. Hickey. Molecular analysis of two bacterioferritin genes, <i>bfr</i> α and <i>bfr</i> β, in the model rhizobacterium <i>pseudomonas putida</i> kt2440. Aug 2010. URL: https://doi.org/10.1128/aem.00215-10, doi:10.1128/aem.00215-10. This article has 20 citations and is from a peer-reviewed journal.

3. (steingard2023meddlingwithmetal pages 1-2): Caroline H. Steingard and John D. Helmann. Meddling with metal sensors: fur-family proteins as signaling hubs. Journal of Bacteriology, Apr 2023. URL: https://doi.org/10.1128/jb.00022-23, doi:10.1128/jb.00022-23. This article has 58 citations and is from a peer-reviewed journal.

4. (steingard2023meddlingwithmetal pages 2-5): Caroline H. Steingard and John D. Helmann. Meddling with metal sensors: fur-family proteins as signaling hubs. Journal of Bacteriology, Apr 2023. URL: https://doi.org/10.1128/jb.00022-23, doi:10.1128/jb.00022-23. This article has 58 citations and is from a peer-reviewed journal.

5. (crosa1997signaltransductionand pages 1-2): J. H. Crosa. Signal transduction and transcriptional and posttranscriptional control of iron-regulated genes in bacteria. Microbiology and Molecular Biology Reviews, 61:319-336, Sep 1997. URL: https://doi.org/10.1128/mmbr.61.3.319-336.1997, doi:10.1128/mmbr.61.3.319-336.1997. This article has 349 citations and is from a domain leading peer-reviewed journal.

6. (kang2024structuralperspectiveson pages 6-7): Sung-Min Kang, Hoon-Seok Kang, Woo-Hyun Chung, Kyu-Tae Kang, and Do-Hee Kim. Structural perspectives on metal dependent roles of ferric uptake regulator (fur). Biomolecules, 14:981, Aug 2024. URL: https://doi.org/10.3390/biom14080981, doi:10.3390/biom14080981. This article has 13 citations.

7. (stein2023navigatingpyoverdineand pages 18-22): Nicola Victoria Maria Stein. Navigating pyoverdine and beyond: the role of tripartite efflux pumps in pseudomonas putida kt2440. Dissertation, Jan 2023. URL: https://doi.org/10.5282/edoc.32605, doi:10.5282/edoc.32605. This article has 1 citations.

8. (kang2024structuralperspectiveson pages 1-2): Sung-Min Kang, Hoon-Seok Kang, Woo-Hyun Chung, Kyu-Tae Kang, and Do-Hee Kim. Structural perspectives on metal dependent roles of ferric uptake regulator (fur). Biomolecules, 14:981, Aug 2024. URL: https://doi.org/10.3390/biom14080981, doi:10.3390/biom14080981. This article has 13 citations.

9. (kang2024structuralperspectiveson pages 7-9): Sung-Min Kang, Hoon-Seok Kang, Woo-Hyun Chung, Kyu-Tae Kang, and Do-Hee Kim. Structural perspectives on metal dependent roles of ferric uptake regulator (fur). Biomolecules, 14:981, Aug 2024. URL: https://doi.org/10.3390/biom14080981, doi:10.3390/biom14080981. This article has 13 citations.

10. (kang2024structuralperspectiveson pages 4-6): Sung-Min Kang, Hoon-Seok Kang, Woo-Hyun Chung, Kyu-Tae Kang, and Do-Hee Kim. Structural perspectives on metal dependent roles of ferric uptake regulator (fur). Biomolecules, 14:981, Aug 2024. URL: https://doi.org/10.3390/biom14080981, doi:10.3390/biom14080981. This article has 13 citations.

11. (ochsner1995roleofthe pages 1-2): U A Ochsner, A I Vasil, and M L Vasil. Role of the ferric uptake regulator of pseudomonas aeruginosa in the regulation of siderophores and exotoxin a expression: purification and activity on iron-regulated promoters. Journal of Bacteriology, 177:7194-7201, Dec 1995. URL: https://doi.org/10.1128/jb.177.24.7194-7201.1995, doi:10.1128/jb.177.24.7194-7201.1995. This article has 253 citations and is from a peer-reviewed journal.

12. (chen2010molecularanalysisof pages 6-8): Shicheng Chen, William F. Bleam, and William J. Hickey. Molecular analysis of two bacterioferritin genes, <i>bfr</i> α and <i>bfr</i> β, in the model rhizobacterium <i>pseudomonas putida</i> kt2440. Aug 2010. URL: https://doi.org/10.1128/aem.00215-10, doi:10.1128/aem.00215-10. This article has 20 citations and is from a peer-reviewed journal.

13. (chen2010molecularanalysisof pages 4-5): Shicheng Chen, William F. Bleam, and William J. Hickey. Molecular analysis of two bacterioferritin genes, <i>bfr</i> α and <i>bfr</i> β, in the model rhizobacterium <i>pseudomonas putida</i> kt2440. Aug 2010. URL: https://doi.org/10.1128/aem.00215-10, doi:10.1128/aem.00215-10. This article has 20 citations and is from a peer-reviewed journal.

14. (chen2010molecularanalysisof pages 8-8): Shicheng Chen, William F. Bleam, and William J. Hickey. Molecular analysis of two bacterioferritin genes, <i>bfr</i> α and <i>bfr</i> β, in the model rhizobacterium <i>pseudomonas putida</i> kt2440. Aug 2010. URL: https://doi.org/10.1128/aem.00215-10, doi:10.1128/aem.00215-10. This article has 20 citations and is from a peer-reviewed journal.

15. (cornelis2010ironuptakeand pages 4-6): Pierre Cornelis. Iron uptake and metabolism in pseudomonads. Applied Microbiology and Biotechnology, 86:1637-1645, Mar 2010. URL: https://doi.org/10.1007/s00253-010-2550-2, doi:10.1007/s00253-010-2550-2. This article has 549 citations and is from a domain leading peer-reviewed journal.

16. (barrientosmoreno2019argininebiosynthesismodulates pages 1-2): Laura Barrientos-Moreno, María Antonia Molina-Henares, Marta Pastor-García, María Isabel Ramos-González, and Manuel Espinosa-Urgel. Arginine biosynthesis modulates pyoverdine production and release in pseudomonas putida as part of the mechanism of adaptation to oxidative stress. Journal of Bacteriology, Nov 2019. URL: https://doi.org/10.1128/jb.00454-19, doi:10.1128/jb.00454-19. This article has 44 citations and is from a peer-reviewed journal.

17. (barrientosmoreno2019argininebiosynthesismodulates pages 2-5): Laura Barrientos-Moreno, María Antonia Molina-Henares, Marta Pastor-García, María Isabel Ramos-González, and Manuel Espinosa-Urgel. Arginine biosynthesis modulates pyoverdine production and release in pseudomonas putida as part of the mechanism of adaptation to oxidative stress. Journal of Bacteriology, Nov 2019. URL: https://doi.org/10.1128/jb.00454-19, doi:10.1128/jb.00454-19. This article has 44 citations and is from a peer-reviewed journal.

18. (song2024molecularmechanismof pages 1-2): Yingjie Song, Xiyu Wu, Ze Li, Qin qin Ma, and Rui Bao. Molecular mechanism of siderophore regulation by the pseudomonas aeruginosa bfmrs two-component system in response to osmotic stress. Communications Biology, Mar 2024. URL: https://doi.org/10.1038/s42003-024-05995-z, doi:10.1038/s42003-024-05995-z. This article has 36 citations and is from a peer-reviewed journal.

19. (kang2024structuralperspectiveson pages 2-4): Sung-Min Kang, Hoon-Seok Kang, Woo-Hyun Chung, Kyu-Tae Kang, and Do-Hee Kim. Structural perspectives on metal dependent roles of ferric uptake regulator (fur). Biomolecules, 14:981, Aug 2024. URL: https://doi.org/10.3390/biom14080981, doi:10.3390/biom14080981. This article has 13 citations.

## Artifacts

- [Edison artifact artifact-00](fur-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. steingard2023meddlingwithmetal pages 2-5
2. kang2024structuralperspectiveson pages 4-6
3. crosa1997signaltransductionand pages 1-2
4. ochsner1995roleofthe pages 1-2
5. chen2010molecularanalysisof pages 6-8
6. chen2010molecularanalysisof pages 4-5
7. chen2010molecularanalysisof pages 5-6
8. chen2010molecularanalysisof pages 8-8
9. cornelis2010ironuptakeand pages 4-6
10. steingard2023meddlingwithmetal pages 1-2
11. song2024molecularmechanismof pages 1-2
12. barrientosmoreno2019argininebiosynthesismodulates pages 1-2
13. chen2010molecularanalysisof pages 1-2
14. kang2024structuralperspectiveson pages 6-7
15. stein2023navigatingpyoverdineand pages 18-22
16. kang2024structuralperspectiveson pages 1-2
17. kang2024structuralperspectiveson pages 7-9
18. barrientosmoreno2019argininebiosynthesismodulates pages 2-5
19. kang2024structuralperspectiveson pages 2-4
20. https://doi.org/10.1128/jb.177.24.7194-7201.1995
21. https://doi.org/10.1128/AEM.00215-10
22. https://doi.org/10.1007/s00253-010-2550-2
23. https://doi.org/10.1128/jb.00454-19
24. https://doi.org/10.1128/jb.00022-23
25. https://doi.org/10.3390/biom14080981
26. https://doi.org/10.1038/s42003-024-05995-z
27. https://doi.org/10.1128/AEM.00215-10;
28. https://doi.org/10.1128/JB.00022-23
29. https://doi.org/10.3390/biom14080981;
30. https://doi.org/10.1128/JB.177.24.7194-7201.1995
31. https://doi.org/10.1128/JB.00022-23;
32. https://doi.org/10.1128/aem.00215-10,
33. https://doi.org/10.1128/jb.00022-23,
34. https://doi.org/10.1128/mmbr.61.3.319-336.1997,
35. https://doi.org/10.3390/biom14080981,
36. https://doi.org/10.5282/edoc.32605,
37. https://doi.org/10.1128/jb.177.24.7194-7201.1995,
38. https://doi.org/10.1007/s00253-010-2550-2,
39. https://doi.org/10.1128/jb.00454-19,
40. https://doi.org/10.1038/s42003-024-05995-z,