---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T01:52:53.255765'
end_time: '2026-06-12T02:11:39.740539'
duration_seconds: 1126.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: EMC10
  gene_symbol: EMC10
  uniprot_accession: Q5UCC4
  protein_description: 'RecName: Full=ER membrane protein complex subunit 10; AltName:
    Full=Hematopoietic signal peptide-containing membrane domain-containing protein
    1; Flags: Precursor;'
  gene_info: Name=EMC10; Synonyms=C19orf63, INM02; ORFNames=UNQ764/PRO1556;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the EMC10 family. .
  protein_domains: ECM10 (PF21203)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: EMC10-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: EMC10-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000029 The architecture and subunit localization
    of the human EMC (ER membrane protein complex) are detailed in Figure 5. Panel
    B shows th'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q5UCC4
- **Protein Description:** RecName: Full=ER membrane protein complex subunit 10; AltName: Full=Hematopoietic signal peptide-containing membrane domain-containing protein 1; Flags: Precursor;
- **Gene Information:** Name=EMC10; Synonyms=C19orf63, INM02; ORFNames=UNQ764/PRO1556;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the EMC10 family. .
- **Key Domains:** ECM10 (PF21203)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EMC10" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EMC10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EMC10** (gene ID: EMC10, UniProt: Q5UCC4) in human.

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
- **UniProt Accession:** Q5UCC4
- **Protein Description:** RecName: Full=ER membrane protein complex subunit 10; AltName: Full=Hematopoietic signal peptide-containing membrane domain-containing protein 1; Flags: Precursor;
- **Gene Information:** Name=EMC10; Synonyms=C19orf63, INM02; ORFNames=UNQ764/PRO1556;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the EMC10 family. .
- **Key Domains:** ECM10 (PF21203)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EMC10" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EMC10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EMC10** (gene ID: EMC10, UniProt: Q5UCC4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive research report: human **EMC10** (UniProt Q5UCC4; gene **EMC10**, synonyms include **C19orf63/HSM1**)

### Executive summary
Human **EMC10** is best-supported as (i) an **auxiliary, primarily lumen-facing subunit** of the **endoplasmic reticulum (ER) membrane protein complex (EMC)** that assists **membrane protein biogenesis** (insertion/topogenesis and later chaperoning), and (ii) a source of a **distinct alternatively spliced secreted isoform (scEMC10)** that functions as a **circulating endocrine/paracrine regulator of thermogenesis and metabolic homeostasis** (not an insertase subunit). The strongest recent translational evidence centers on scEMC10 as a **biomarker and drug target** for obesity/insulin resistance, whereas human genetic aggregation links EMC10 most strongly to **recessive neurodevelopmental disorders**. (hegde2022thefunctionstructure pages 11-13, millervedam2020structuralandmechanistic pages 18-21, wang2022secretedemc10is pages 1-2, wat2024novelsecretedregulators pages 2-4, OpenTargets Search: -EMC10)

### 1) Key concepts & definitions (current understanding)

#### 1.1 ER membrane protein complex (EMC)
The **EMC** is an **abundant ER-resident multiprotein complex** implicated in **membrane protein biogenesis**, including (a) **energy-independent insertion** of certain transmembrane domains (TMDs) and (b) broader **chaperone/holdase** functions for difficult multipass clients. A structural/functional synthesis supports a model where EMC contains a **cytosolic vestibule** leading into a **lipid-exposed intramembrane groove** that can accommodate a TMD and facilitate its insertion into the bilayer. (odonnell2020thearchitectureof pages 1-2, odonnell2020thearchitectureof pages 14-15, hegde2022thefunctionstructure pages 11-13)

A 2023 mechanistic study further proposed a **selectivity filter** within EMC that limits inappropriate insertion events (e.g., mitochondrial tail-anchored proteins into the ER), using **charge-based discrimination** at the vestibule entrance. (pleiner2023aselectivityfilter pages 1-2)

#### 1.2 What EMC10 is (and is not)
**EMC10 (ER membrane protein complex subunit 10)** is one of the mammalian EMC subunits; mammalian EMC is described as a **10-protein assembly** with multiple membrane subunits and cytosolic components (EMC2/8/9). (odonnell2020thearchitectureof pages 1-2)

However, multiple authoritative sources describe EMC10 as **peripheral/auxiliary** relative to the core insertase architecture (e.g., EMC3-centered machinery). EMC10 is placed mainly in the **lumenal module** together with EMC1 and EMC7 and is not currently assigned a catalytic “insertase” activity of its own. (hegde2022thefunctionstructure pages 11-13, millervedam2020structuralandmechanistic pages 18-21, odonnell2020thearchitectureof pages 10-11)

Separately, **scEMC10** refers to an **alternatively spliced secreted isoform** of EMC10 that **lacks a transmembrane domain** and circulates as a soluble factor with metabolic effects; this is mechanistically distinct from EMC10’s EMC-subunit role. (wang2022secretedemc10is pages 1-2, wat2024novelsecretedregulators pages 1-2)

### 2) Verified identity, localization, topology, and complex membership

#### 2.1 Complex membership and ER localization
Biochemical and structural studies of human EMC consistently include **EMC10** among EMC subunits and place EMC function at the **ER**. Mammalian EMC is described as ten subunits (EMC1–EMC10), with seven integral membrane subunits (including EMC10) associating with cytosolic EMC2/8/9. (odonnell2020thearchitectureof pages 1-2)

#### 2.2 Placement of EMC10 within EMC structure (lumenal module)
Cryo-EM/modeling indicates the **lumenal domain** of human EMC is largely accounted for by **EMC1, EMC7, and EMC10**, with EMC10 modeled as a **small beta-barrel/beta-sandwich-like lumenal domain** docked into lumenal density (the EMC10 TMD was not resolved in that dataset). (odonnell2020thearchitectureof pages 11-12)

Independent structural work supports that EMC10 forms a **beta-sandwich fold**, is **scaffolded on EMC1**, and **contacts EMC7** across a membrane-proximal EMC1 region; this lumenal module is implicated in polytopic client biogenesis and lumenal chaperone interactions. (millervedam2020structuralandmechanistic pages 18-21)

A cropped figure from O’Donnell et al. provides a visual map of EMC10 within the lumenal architecture (Figure 5; panel highlighting EMC10 and EMC7). (odonnell2020thearchitectureof media 65b3bb2d, odonnell2020thearchitectureof media 6e794663)

#### 2.3 Peripheral/auxiliary nature of EMC10
Several lines of evidence support EMC10 being **auxiliary/peripheral**:
* EMC10 is described as one of the EMC subunits with **weaker depletion phenotypes** and less disruption of complex integrity compared with core subunits, consistent with peripheral status. (chitwood2019theroleof pages 2-4)
* In a cryo-EM assignment context, EMC10 is described as one of three **single-spanning** subunits (with EMC1 and EMC7) and as the **least likely** to be visualized, with the authors noting it could be depleted without clear functional consequences in prior work. (odonnell2020thearchitectureof pages 10-11)
* Loss of EMC7 can lead to **loss of EMC10** while leaving other EMC components intact, supporting that EMC10 is not required for core complex stability. (millervedam2020structuralandmechanistic pages 18-21)

### 3) Functional annotation: biological roles, processes, and pathways

#### 3.1 EMC10 as part of the EMC lumenal domain (inferred primary function)
The most defensible “primary function” assignment for the **membrane/complex-associated EMC10 isoform** is as a **structural/interaction module** on the ER-lumenal face of the EMC that supports EMC’s broader role in **membrane protein biogenesis**, especially for **polytopic/multipass** clients.

Mechanistically, EMC as a complex is implicated in:
* **Insertion/topogenesis** of certain TMDs via a vestibule–groove pathway (energy-independent insertion). (odonnell2020thearchitectureof pages 14-15, odonnell2020thearchitectureof pages 1-2)
* **Quality control/selectivity** that prevents misinsertion using charge barriers/selectivity filters at key entry points. (pleiner2023aselectivityfilter pages 1-2)

EMC10 itself has not been shown to catalyze insertion; rather it is positioned at the **periphery of EMC1’s beta-propeller**, suggesting roles in **lumenal interactions** or stabilization. A major expert synthesis explicitly frames EMC10/EMC7 beta-sandwiches as canonical protein-interaction modules whose lumenal partners remain to be identified, implying EMC10 may mediate **client- or chaperone-facing interactions**. (hegde2022thefunctionstructure pages 11-13)

A 2023 mechanistic study of EMC selectivity describes EMC10 (with EMC4 and EMC7) as providing **dynamic transmembrane elements** that create a protected, membrane-facing environment for nascent TMD sampling—suggesting EMC10 may indirectly influence insertion fidelity/specificity even if it is not “core catalytic.” (pleiner2023aselectivityfilter pages 10-11)

#### 3.2 EMC10-derived secreted isoform (scEMC10): metabolic signaling pathway
A distinct and well-supported functional axis concerns the **secreted isoform scEMC10**:

**Core mechanism.** scEMC10 can be transported into cells, bind the **PKA catalytic subunit**, inhibit PKA’s stimulatory action on **CREB**, and thereby suppress thermogenesis-associated gene programs (e.g., reducing CREB phosphorylation/activity). (wang2022secretedemc10is pages 1-2, wang2022secretedemc10is pages 6-8)

**Physiological consequence.** Genetic deletion of Emc10 in mice increases energy expenditure and thermogenic capacity; conversely scEMC10 overexpression decreases energy expenditure and promotes obesity. (wang2022secretedemc10is pages 1-2)

**Expert framing (2023–2024).** Reviews describing thermogenesis regulators and emerging secreted metabolic factors highlight scEMC10 as a newly appreciated secreted inhibitor of thermogenesis and a candidate therapeutic target, while also noting translational uncertainties (e.g., isoform specificity and receptor/uptake mechanisms). (nie2023latestadvancesin pages 1-2, wat2024novelsecretedregulators pages 2-4)

### 4) Recent developments and latest research (prioritizing 2023–2024)

#### 4.1 EMC selectivity and EMC10-linked membrane environment (2023)
In 2023, mechanistic work on EMC proposed a **selectivity filter** that limits protein misinsertion and described how flexible loops and vestibule charge features enforce correct targeting/topology; EMC10 is implicated as part of the dynamic TMD environment supporting substrate sampling (though EMC10 topology details were not fully specified in the excerpted text). (pleiner2023aselectivityfilter pages 1-2, pleiner2023aselectivityfilter pages 10-11)

#### 4.2 scEMC10 as a metabolic endocrine factor (2023–2024 consolidation)
A 2023 review of adipocyte thermogenesis genes summarizes scEMC10 as a secreted protein produced by differential splicing and ties it to human obesity/insulin resistance correlations and mouse causal evidence, including antibody neutralization. (nie2023latestadvancesin pages 1-2)

A 2024 Diabetologia review on secreted metabolic regulators synthesizes evidence that scEMC10 neutralization improves glucose and lipid metabolic phenotypes in mice and highlights that global knockout studies cannot cleanly separate membrane EMC10 from scEMC10, emphasizing the need for isoform-specific causal experiments. (wat2024novelsecretedregulators pages 2-4)

### 5) Current applications and real-world implementations

#### 5.1 Biomarker applications (human)
In multiple cohorts, **circulating EMC10/scEMC10** is reported as elevated with obesity and associated with insulin resistance measures.

Notable quantitative intervention results (12-month follow-up):
* **Bariatric surgery**: BMI decreased **30.1%**, serum EMC10 decreased **57.9%**, and HOMA-IR decreased **77.4%** (all P < 0.001). (wang2022secretedemc10is pages 1-2)
* **Diet + exercise program**: serum EMC10 decreased **32%** (P < 0.01) and HOMA-IR decreased **46%** (P < 0.001) despite only modest BMI change. (wang2022secretedemc10is pages 1-2)

Cohort sizes reported include (examples) a white cohort with lean/overweight/obese groupings such as **n=27/20/160** and a Chinese Han cohort such as **n=32/115/39** (with alternative group-count reporting in other sections). (wang2022secretedemc10is pages 2-3, wang2022secretedemc10is pages 11-12)

#### 5.2 Therapeutic targeting (preclinical)
A neutralizing monoclonal antibody against circulating scEMC10 reduces weight and improves insulin sensitivity in obese mice; cross-over experiments with antibody withdrawal and reintroduction show reversibility consistent with causality. (wang2022secretedemc10is pages 11-12, wang2022secretedemc10is pages 6-8)

#### 5.3 Physiological phenotyping implementation (human BAT imaging)
A 2025 human study provides an example of real-world implementation of scEMC10 measurement alongside **18F-FDG PET–CT** to define BAT positivity and thermoneutrality response. In BAT-positive participants (subset n=7), **2 h thermoneutrality (28°C)** increased median serum scEMC10 from **2.34 → 4.25 ng/mL** (P = 0.0017) coincident with disappearance of active BAT, supporting an inhibitory role of scEMC10 on facultative thermogenesis in humans. (miao2025serumsecretedemc10 pages 7-9)

### 6) Disease associations and genetics (authoritative aggregation)

Open Targets aggregation indicates the strongest genetic association signal for EMC10 is with **neurodevelopmental disorders** (including “neurodevelopmental disorder with dysmorphic facies and variable seizures”), driven largely by evidence consistent with **biallelic/autosomal recessive loss-of-function** variant classes (frameshift, stop-gained, splice-acceptor; “absent gene product” annotations). (OpenTargets Search: -EMC10)

Open Targets also reports a weaker association with **hypertension** (lower overall association score, mainly GWAS credible-set evidence). (OpenTargets Search: -EMC10)

The scEMC10 metabolic axis provides an additional disease-relevant dimension, with strong evidence for involvement in **obesity and insulin resistance** and potential relevance to associated cardiometabolic complications. (wang2022secretedemc10is pages 1-2, wat2024novelsecretedregulators pages 2-4)

### 7) Expert opinions, analysis, and open questions

#### 7.1 EMC10 (complex-associated) remains incompletely characterized
A key expert synthesis emphasizes that while EMC’s core insertase architecture is increasingly clear, the lumenal beta-sandwich/beta-propeller modules (including EMC10) likely mediate interactions whose partners and precise mechanistic contributions remain to be identified; this supports prioritizing EMC10 experiments that test effects on polytopic client maturation, lumenal chaperone recruitment, and EMC conformational coupling. (hegde2022thefunctionstructure pages 11-13, millervedam2020structuralandmechanistic pages 18-21)

#### 7.2 scEMC10: isoform-specific causality and mechanism
The 2024 review literature highlights an important limitation: **whole-body EMC10 knockout** cannot definitively attribute phenotypes to scEMC10 versus membrane-associated EMC10, motivating isoform-specific perturbations and mechanistic identification of uptake mediators/receptors. (wat2024novelsecretedregulators pages 2-4)

### 8) Summary of evidence-based functional annotation for UniProt Q5UCC4

1. **Cellular location:** ER, predominantly lumen-facing as part of the EMC lumenal module; forms structural interactions with EMC1 and EMC7. (millervedam2020structuralandmechanistic pages 18-21, odonnell2020thearchitectureof pages 11-12, hegde2022thefunctionstructure pages 11-13, odonnell2020thearchitectureof media 65b3bb2d)
2. **Molecular role (most supported):** Auxiliary/peripheral EMC subunit contributing to lumenal architecture and likely client/chaperone interaction surfaces in membrane protein biogenesis (especially polytopic clients), rather than being the catalytic insertase core. (hegde2022thefunctionstructure pages 11-13, millervedam2020structuralandmechanistic pages 18-21, chitwood2019theroleof pages 2-4)
3. **Pathway context:** EMC-mediated membrane protein insertion/topogenesis and selectivity mechanisms (EMC vestibule/groove; selectivity filter); EMC10 may contribute to the dynamic membrane-facing environment for substrate sampling. (odonnell2020thearchitectureof pages 1-2, odonnell2020thearchitectureof pages 14-15, pleiner2023aselectivityfilter pages 10-11)
4. **Distinct secreted function (isoform):** scEMC10 is a circulating inhibitor of thermogenesis acting via intracellular uptake and inhibition of **PKA–CREB** signaling; robust evidence supports biomarker and antibody-based targeting potential in metabolic disease. (wang2022secretedemc10is pages 1-2, wang2022secretedemc10is pages 6-8, wat2024novelsecretedregulators pages 2-4)

### Key sources (URLs and publication dates)
* Pleiner et al. “A selectivity filter in the ER membrane protein complex limits protein misinsertion at the ER.” *J Cell Biol* (May 2023). https://doi.org/10.1083/jcb.202212007 (pleiner2023aselectivityfilter pages 10-11, pleiner2023aselectivityfilter pages 1-2)
* Wat & Svensson. “Novel secreted regulators of glucose and lipid metabolism in the development of metabolic diseases.” *Diabetologia* (Aug 2024). https://doi.org/10.1007/s00125-024-06253-x (wat2024novelsecretedregulators pages 2-4, wat2024novelsecretedregulators pages 1-2)
* Wang et al. “Secreted EMC10 is upregulated in human obesity and its neutralizing antibody prevents diet-induced obesity in mice.” *Nature Communications* (Nov 2022). https://doi.org/10.1038/s41467-022-34259-9 (wang2022secretedemc10is pages 1-2, wang2022secretedemc10is pages 2-3, wang2022secretedemc10is pages 11-12, wang2022secretedemc10is pages 6-8)
* Hegde. “The Function, Structure, and Origins of the ER Membrane Protein Complex.” *Annual Review of Biochemistry* (Jun 2022). https://doi.org/10.1146/annurev-biochem-032620-104553 (hegde2022thefunctionstructure pages 11-13, hegde2022thefunctionstructure pages 10-11)
* O’Donnell et al. “The architecture of EMC reveals a path for membrane protein insertion.” *eLife* (May 2020). https://doi.org/10.7554/elife.57887 (odonnell2020thearchitectureof pages 1-2, odonnell2020thearchitectureof pages 11-12, odonnell2020thearchitectureof media 65b3bb2d)
* Open Targets Platform (EMC10 / ENSG00000161671). Accessed via tool output. https://platform.opentargets.org/target/ENSG00000161671 (OpenTargets Search: -EMC10)

| Aspect | Key claim | Evidence summary | Key quantitative data | Primary sources (with year, journal) | URL |
|---|---|---|---|---|---|
| identity/localization | Human EMC10 is a bona fide ER membrane protein complex (EMC) subunit localized mainly on the ER lumenal face. | Structural and review evidence place EMC10 with EMC1 and EMC7 in the EMC lumenal domain; EMC10 has a lumenal beta-sandwich/beta-barrel-like domain and is part of the mammalian 10-subunit EMC. It is ER-resident and contributes to the lumenal architecture rather than acting as a free soluble protein. (odonnell2020thearchitectureof pages 1-2, millervedam2020structuralandmechanistic pages 18-21, odonnell2020thearchitectureof pages 11-12, hegde2022thefunctionstructure pages 11-13) | EMC is described as 10 subunits in mammals; EMC10 is one of only three subunits with appreciable lumenal domains. (odonnell2020thearchitectureof pages 1-2, chitwood2019theroleof pages 2-4) | O'Donnell et al. 2020, *eLife*; Miller-Vedam et al. 2020, *eLife*; Hegde 2022, *Annual Review of Biochemistry* | https://doi.org/10.7554/elife.57887; https://doi.org/10.1101/2020.09.02.280008; https://doi.org/10.1146/annurev-biochem-032620-104553 |
| EMC complex role | EMC10 appears to be an auxiliary/peripheral EMC subunit that supports lumenal architecture and polytopic client biogenesis rather than forming the catalytic insertase core. | EMC10 is scaffolded on EMC1 and contacts EMC7 in the lumenal domain. Loss of EMC7 can cause loss of EMC10 while leaving other core components intact, and EMC10 depletion can have minimal functional consequences in some assays, supporting a peripheral classification. Recent EMC work also implicates EMC10-containing dynamic TMD elements in creating a protected environment for substrate TMD sampling. (millervedam2020structuralandmechanistic pages 18-21, hegde2022thefunctionstructure pages 11-13, odonnell2020thearchitectureof pages 10-11, pleiner2023aselectivityfilter pages 10-11) | Prior studies cited in structural work note EMC10 depletion without overt functional consequence in some settings; no direct catalytic activity assigned. (odonnell2020thearchitectureof pages 10-11, hegde2022thefunctionstructure pages 11-13) | O'Donnell et al. 2020, *eLife*; Miller-Vedam et al. 2020, *eLife*; Pleiner et al. 2023, *Journal of Cell Biology*; Hegde 2022, *Annual Review of Biochemistry* | https://doi.org/10.7554/elife.57887; https://doi.org/10.1101/2020.09.02.280008; https://doi.org/10.1083/jcb.202212007; https://doi.org/10.1146/annurev-biochem-032620-104553 |
| secreted isoform scEMC10 | EMC10 also has an alternatively spliced secreted isoform, scEMC10, which acts as a circulating inhibitor of adipocyte thermogenesis via PKA-CREB suppression. | Primary and review sources report that scEMC10 lacks the transmembrane domain, is secreted, can be taken up by cells, binds the PKA catalytic subunit, inhibits CREB phosphorylation/activity, and suppresses thermogenic gene programs. This function is mechanistically distinct from EMC10’s role as an EMC subunit. (wang2022secretedemc10is pages 1-2, wat2024novelsecretedregulators pages 2-4, wang2022secretedemc10is pages 11-12, wat2024novelsecretedregulators pages 1-2, wang2022secretedemc10is pages 6-8) | 25 mmol/L glucose caused a ~3-fold increase in scEMC10 mRNA in cultured beta cells/islets; thermoneutrality in BAT-positive humans increased median serum scEMC10 from 2.34 to 4.25 ng/mL. (wat2024novelsecretedregulators pages 1-2, miao2025serumsecretedemc10 pages 7-9) | Wang et al. 2022, *Nature Communications*; Wat & Svensson 2024, *Diabetologia*; Miao et al. 2025, *International Journal of Obesity* | https://doi.org/10.1038/s41467-022-34259-9; https://doi.org/10.1007/s00125-024-06253-x; https://doi.org/10.1038/s41366-025-01744-2 |
| human cohort statistics | Circulating scEMC10 is elevated with obesity and insulin resistance in multiple human cohorts and decreases after weight-loss interventions. | In white and Chinese Han cohorts, serum EMC10 positively correlated with BMI and with metabolic risk markers; in clamp studies it inversely correlated with glucose infusion rate and positively with fasting insulin. Bariatric surgery and lifestyle intervention lowered circulating EMC10 alongside improved insulin resistance. (wang2022secretedemc10is pages 1-2, wang2022secretedemc10is pages 2-3, wang2022secretedemc10is pages 11-12) | Cohorts included white lean/overweight/obese groups of n=27/20/160 and Chinese Han groups of n=32/115/39; alternate grouping reported as 30/22/188 and 32/115/39. Bariatric surgery: BMI -30.1%, serum EMC10 -57.9%, HOMA-IR -77.4% at 12 months. Diet+exercise: serum EMC10 -32%, HOMA-IR -46% at 12 months. BAT study: 38 BAT+ and 38 BAT- participants; thermoneutrality subset n=7. (wang2022secretedemc10is pages 1-2, miao2025serumsecretedemc10 pages 7-9, wang2022secretedemc10is pages 2-3, wang2022secretedemc10is pages 11-12) | Wang et al. 2022, *Nature Communications*; Miao et al. 2025, *International Journal of Obesity* | https://doi.org/10.1038/s41467-022-34259-9; https://doi.org/10.1038/s41366-025-01744-2 |
| mouse intervention/therapeutic | Genetic deletion or antibody neutralization of scEMC10 improves metabolic phenotypes in mice, supporting therapeutic targeting. | Whole-body Emc10 knockout mice resist diet-induced obesity through higher energy expenditure and thermogenesis. A neutralizing monoclonal antibody to circulating scEMC10 lowers body weight, improves insulin sensitivity/glucose tolerance, and cross-over experiments support reversibility/causality. AAV-mediated scEMC10 overexpression worsens adiposity and glucose metabolism. (wang2022secretedemc10is pages 1-2, wat2024novelsecretedregulators pages 2-4, wang2022secretedemc10is pages 11-12, wang2022secretedemc10is pages 6-8) | On chow, WT vs KO body weight was similar: 33.68 ± 1.64 vs 33.77 ± 1.78 g, p=0.97. Antibody neutralization improved fasting glucose, glucose tolerance, insulin tolerance, and reduced weight gain in HFD models; mouse groups were often n=6–9 per arm in cited experiments. (wat2024novelsecretedregulators pages 2-4, wang2022secretedemc10is pages 6-8, wang2022secretedemc10is pages 2-3, wang2022secretedemc10is pages 11-12) | Wang et al. 2022, *Nature Communications*; Wat & Svensson 2024, *Diabetologia* | https://doi.org/10.1038/s41467-022-34259-9; https://doi.org/10.1007/s00125-024-06253-x |
| disease genetics | Human EMC10 is genetically linked most strongly to recessive neurodevelopmental disease; weaker association signals exist for hypertension. | Open Targets aggregates genetic evidence linking EMC10 to neurodevelopmental disorder, complex genetic disorder, and the specific syndrome “neurodevelopmental disorder with dysmorphic facies and variable seizures.” Evidence includes likely loss-of-function variant classes under autosomal recessive/biallelic models. Wang et al. also note prior reports of intellectual disability/global developmental delay and male fertility roles. (OpenTargets Search: -EMC10, wang2022secretedemc10is pages 1-2, wang2022secretedemc10is pages 2-3) | Open Targets association scores: neurodevelopmental disorder 0.7349; genetic disorder 0.7108; specific neurodevelopmental syndrome 0.6956; hypertension 0.3457. Variant consequences include frameshift, stop-gained, splice-acceptor, and absent_gene_product annotations. (OpenTargets Search: -EMC10) | Open Targets Platform (query output citing PMIDs incl. 32869858, 33531666, 35124540, 35684946); Wang et al. 2022, *Nature Communications* | https://platform.opentargets.org/target/ENSG00000161671; https://doi.org/10.1038/s41467-022-34259-9 |


*Table: This table summarizes the main evidence-based findings for human EMC10, separating its ER membrane complex role from the distinct biology of the secreted scEMC10 isoform. It also highlights recent quantitative human and mouse data that are useful for functional annotation and translational interpretation.*

References

1. (hegde2022thefunctionstructure pages 11-13): Ramanujan S. Hegde. The function, structure, and origins of the er membrane protein complex. Annual Review of Biochemistry, 91:651-678, Jun 2022. URL: https://doi.org/10.1146/annurev-biochem-032620-104553, doi:10.1146/annurev-biochem-032620-104553. This article has 65 citations and is from a domain leading peer-reviewed journal.

2. (millervedam2020structuralandmechanistic pages 18-21): Lakshmi E. Miller-Vedam, Bastian Bräuning, Katerina D. Popova, Nicole T. Schirle Oakdale, Jessica L. Bonnar, Jesuraj Rajan Prabu, Elizabeth A. Boydston, Natalia Sevillano, Matthew J. Shurtleff, Robert M. Stroud, Charles S. Craik, Brenda A. Schulman, Adam Frost, and Jonathan S. Weissman. Structural and mechanistic basis of the emc-dependent biogenesis of distinct transmembrane clients. eLife, Sep 2020. URL: https://doi.org/10.1101/2020.09.02.280008, doi:10.1101/2020.09.02.280008. This article has 102 citations and is from a domain leading peer-reviewed journal.

3. (wang2022secretedemc10is pages 1-2): Xuanchun Wang, Yanliang Li, Guifen Qiang, Kaihua Wang, Jiarong Dai, Maximilian McCann, Marcos D. Munoz, Victoria Gil, Yifei Yu, Shengxian Li, Zhihong Yang, Shanshan Xu, Jose Cordoba-Chacon, Dario F. De Jesus, Bei Sun, Kuangyang Chen, Yahao Wang, Xiaoxia Liu, Qing Miao, Linuo Zhou, Renming Hu, Qiang Ding, Rohit N. Kulkarni, Daming Gao, Matthias Blüher, and Chong Wee Liew. Secreted emc10 is upregulated in human obesity and its neutralizing antibody prevents diet-induced obesity in mice. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34259-9, doi:10.1038/s41467-022-34259-9. This article has 20 citations and is from a highest quality peer-reviewed journal.

4. (wat2024novelsecretedregulators pages 2-4): Lianna W. Wat and Katrin J. Svensson. Novel secreted regulators of glucose and lipid metabolism in the development of metabolic diseases. Diabetologia, 67:2626-2636, Aug 2024. URL: https://doi.org/10.1007/s00125-024-06253-x, doi:10.1007/s00125-024-06253-x. This article has 8 citations and is from a highest quality peer-reviewed journal.

5. (OpenTargets Search: -EMC10): Open Targets Query (-EMC10, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (odonnell2020thearchitectureof pages 1-2): John P O'Donnell, Ben P Phillips, Yuichi Yagita, Szymon Juszkiewicz, Armin Wagner, Duccio Malinverni, Robert J Keenan, Elizabeth A Miller, and Ramanujan S Hegde. The architecture of emc reveals a path for membrane protein insertion. eLife, May 2020. URL: https://doi.org/10.7554/elife.57887, doi:10.7554/elife.57887. This article has 121 citations and is from a domain leading peer-reviewed journal.

7. (odonnell2020thearchitectureof pages 14-15): John P O'Donnell, Ben P Phillips, Yuichi Yagita, Szymon Juszkiewicz, Armin Wagner, Duccio Malinverni, Robert J Keenan, Elizabeth A Miller, and Ramanujan S Hegde. The architecture of emc reveals a path for membrane protein insertion. eLife, May 2020. URL: https://doi.org/10.7554/elife.57887, doi:10.7554/elife.57887. This article has 121 citations and is from a domain leading peer-reviewed journal.

8. (pleiner2023aselectivityfilter pages 1-2): Tino Pleiner, Masami Hazu, Giovani Pinton Tomaleri, Vy N. Nguyen, Kurt Januszyk, and Rebecca M. Voorhees. A selectivity filter in the er membrane protein complex limits protein misinsertion at the er. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202212007, doi:10.1083/jcb.202212007. This article has 28 citations.

9. (odonnell2020thearchitectureof pages 10-11): John P O'Donnell, Ben P Phillips, Yuichi Yagita, Szymon Juszkiewicz, Armin Wagner, Duccio Malinverni, Robert J Keenan, Elizabeth A Miller, and Ramanujan S Hegde. The architecture of emc reveals a path for membrane protein insertion. eLife, May 2020. URL: https://doi.org/10.7554/elife.57887, doi:10.7554/elife.57887. This article has 121 citations and is from a domain leading peer-reviewed journal.

10. (wat2024novelsecretedregulators pages 1-2): Lianna W. Wat and Katrin J. Svensson. Novel secreted regulators of glucose and lipid metabolism in the development of metabolic diseases. Diabetologia, 67:2626-2636, Aug 2024. URL: https://doi.org/10.1007/s00125-024-06253-x, doi:10.1007/s00125-024-06253-x. This article has 8 citations and is from a highest quality peer-reviewed journal.

11. (odonnell2020thearchitectureof pages 11-12): John P O'Donnell, Ben P Phillips, Yuichi Yagita, Szymon Juszkiewicz, Armin Wagner, Duccio Malinverni, Robert J Keenan, Elizabeth A Miller, and Ramanujan S Hegde. The architecture of emc reveals a path for membrane protein insertion. eLife, May 2020. URL: https://doi.org/10.7554/elife.57887, doi:10.7554/elife.57887. This article has 121 citations and is from a domain leading peer-reviewed journal.

12. (odonnell2020thearchitectureof media 65b3bb2d): John P O'Donnell, Ben P Phillips, Yuichi Yagita, Szymon Juszkiewicz, Armin Wagner, Duccio Malinverni, Robert J Keenan, Elizabeth A Miller, and Ramanujan S Hegde. The architecture of emc reveals a path for membrane protein insertion. eLife, May 2020. URL: https://doi.org/10.7554/elife.57887, doi:10.7554/elife.57887. This article has 121 citations and is from a domain leading peer-reviewed journal.

13. (odonnell2020thearchitectureof media 6e794663): John P O'Donnell, Ben P Phillips, Yuichi Yagita, Szymon Juszkiewicz, Armin Wagner, Duccio Malinverni, Robert J Keenan, Elizabeth A Miller, and Ramanujan S Hegde. The architecture of emc reveals a path for membrane protein insertion. eLife, May 2020. URL: https://doi.org/10.7554/elife.57887, doi:10.7554/elife.57887. This article has 121 citations and is from a domain leading peer-reviewed journal.

14. (chitwood2019theroleof pages 2-4): Patrick J. Chitwood and Ramanujan S. Hegde. The role of emc during membrane protein biogenesis. Trends in cell biology, 29 5:371-384, May 2019. URL: https://doi.org/10.1016/j.tcb.2019.01.007, doi:10.1016/j.tcb.2019.01.007. This article has 97 citations and is from a domain leading peer-reviewed journal.

15. (pleiner2023aselectivityfilter pages 10-11): Tino Pleiner, Masami Hazu, Giovani Pinton Tomaleri, Vy N. Nguyen, Kurt Januszyk, and Rebecca M. Voorhees. A selectivity filter in the er membrane protein complex limits protein misinsertion at the er. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202212007, doi:10.1083/jcb.202212007. This article has 28 citations.

16. (wang2022secretedemc10is pages 6-8): Xuanchun Wang, Yanliang Li, Guifen Qiang, Kaihua Wang, Jiarong Dai, Maximilian McCann, Marcos D. Munoz, Victoria Gil, Yifei Yu, Shengxian Li, Zhihong Yang, Shanshan Xu, Jose Cordoba-Chacon, Dario F. De Jesus, Bei Sun, Kuangyang Chen, Yahao Wang, Xiaoxia Liu, Qing Miao, Linuo Zhou, Renming Hu, Qiang Ding, Rohit N. Kulkarni, Daming Gao, Matthias Blüher, and Chong Wee Liew. Secreted emc10 is upregulated in human obesity and its neutralizing antibody prevents diet-induced obesity in mice. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34259-9, doi:10.1038/s41467-022-34259-9. This article has 20 citations and is from a highest quality peer-reviewed journal.

17. (nie2023latestadvancesin pages 1-2): Tao Nie, Jinli Lu, Hua Zhang, and Liufeng Mao. Latest advances in the regulatory genes of adipocyte thermogenesis. Frontiers in Endocrinology, Aug 2023. URL: https://doi.org/10.3389/fendo.2023.1250487, doi:10.3389/fendo.2023.1250487. This article has 3 citations.

18. (wang2022secretedemc10is pages 2-3): Xuanchun Wang, Yanliang Li, Guifen Qiang, Kaihua Wang, Jiarong Dai, Maximilian McCann, Marcos D. Munoz, Victoria Gil, Yifei Yu, Shengxian Li, Zhihong Yang, Shanshan Xu, Jose Cordoba-Chacon, Dario F. De Jesus, Bei Sun, Kuangyang Chen, Yahao Wang, Xiaoxia Liu, Qing Miao, Linuo Zhou, Renming Hu, Qiang Ding, Rohit N. Kulkarni, Daming Gao, Matthias Blüher, and Chong Wee Liew. Secreted emc10 is upregulated in human obesity and its neutralizing antibody prevents diet-induced obesity in mice. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34259-9, doi:10.1038/s41467-022-34259-9. This article has 20 citations and is from a highest quality peer-reviewed journal.

19. (wang2022secretedemc10is pages 11-12): Xuanchun Wang, Yanliang Li, Guifen Qiang, Kaihua Wang, Jiarong Dai, Maximilian McCann, Marcos D. Munoz, Victoria Gil, Yifei Yu, Shengxian Li, Zhihong Yang, Shanshan Xu, Jose Cordoba-Chacon, Dario F. De Jesus, Bei Sun, Kuangyang Chen, Yahao Wang, Xiaoxia Liu, Qing Miao, Linuo Zhou, Renming Hu, Qiang Ding, Rohit N. Kulkarni, Daming Gao, Matthias Blüher, and Chong Wee Liew. Secreted emc10 is upregulated in human obesity and its neutralizing antibody prevents diet-induced obesity in mice. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34259-9, doi:10.1038/s41467-022-34259-9. This article has 20 citations and is from a highest quality peer-reviewed journal.

20. (miao2025serumsecretedemc10 pages 7-9): Qing Miao, Yahao Wang, Qiongyue Zhang, Wei Wu, Yifei Yu, Fangfang Zeng, Yehong Yang, Chuantao Zuo, Yihui Guan, Chong Wee Liew, Matthias Blüher, Yiming Li, and Xuanchun Wang. Serum secreted emc10 (scemc10) levels are inversely associated with metabolically active brown adipose tissue in humans. International Journal of Obesity, 49:1264-1271, Mar 2025. URL: https://doi.org/10.1038/s41366-025-01744-2, doi:10.1038/s41366-025-01744-2. This article has 1 citations and is from a highest quality peer-reviewed journal.

21. (hegde2022thefunctionstructure pages 10-11): Ramanujan S. Hegde. The function, structure, and origins of the er membrane protein complex. Annual Review of Biochemistry, 91:651-678, Jun 2022. URL: https://doi.org/10.1146/annurev-biochem-032620-104553, doi:10.1146/annurev-biochem-032620-104553. This article has 65 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](EMC10-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000029 The architecture and subunit localization of the human EMC (ER membrane protein complex) are detailed in Figure 5. Panel B shows th](EMC10-deep-research-falcon_artifacts/image-1.png)

## Citations

1. pleiner2023aselectivityfilter pages 1-2
2. odonnell2020thearchitectureof pages 1-2
3. odonnell2020thearchitectureof pages 11-12
4. millervedam2020structuralandmechanistic pages 18-21
5. chitwood2019theroleof pages 2-4
6. odonnell2020thearchitectureof pages 10-11
7. hegde2022thefunctionstructure pages 11-13
8. pleiner2023aselectivityfilter pages 10-11
9. nie2023latestadvancesin pages 1-2
10. wat2024novelsecretedregulators pages 2-4
11. odonnell2020thearchitectureof pages 14-15
12. wat2024novelsecretedregulators pages 1-2
13. hegde2022thefunctionstructure pages 10-11
14. https://doi.org/10.1083/jcb.202212007
15. https://doi.org/10.1007/s00125-024-06253-x
16. https://doi.org/10.1038/s41467-022-34259-9
17. https://doi.org/10.1146/annurev-biochem-032620-104553
18. https://doi.org/10.7554/elife.57887
19. https://platform.opentargets.org/target/ENSG00000161671
20. https://doi.org/10.7554/elife.57887;
21. https://doi.org/10.1101/2020.09.02.280008;
22. https://doi.org/10.1083/jcb.202212007;
23. https://doi.org/10.1038/s41467-022-34259-9;
24. https://doi.org/10.1007/s00125-024-06253-x;
25. https://doi.org/10.1038/s41366-025-01744-2
26. https://platform.opentargets.org/target/ENSG00000161671;
27. https://doi.org/10.1146/annurev-biochem-032620-104553,
28. https://doi.org/10.1101/2020.09.02.280008,
29. https://doi.org/10.1038/s41467-022-34259-9,
30. https://doi.org/10.1007/s00125-024-06253-x,
31. https://doi.org/10.7554/elife.57887,
32. https://doi.org/10.1083/jcb.202212007,
33. https://doi.org/10.1016/j.tcb.2019.01.007,
34. https://doi.org/10.3389/fendo.2023.1250487,
35. https://doi.org/10.1038/s41366-025-01744-2,