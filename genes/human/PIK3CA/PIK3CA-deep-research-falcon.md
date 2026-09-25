---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T03:56:34.578816'
end_time: '2026-09-25T04:16:28.025442'
duration_seconds: 1193.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PIK3CA
  gene_symbol: PIK3CA
  uniprot_accession: P42336
  protein_description: 'RecName: Full=Phosphatidylinositol 4,5-bisphosphate 3-kinase
    catalytic subunit alpha isoform; Short=PI3-kinase subunit alpha; Short=PI3K-alpha;
    Short=PI3Kalpha {ECO:0000303|PubMed:28676499}; Short=PtdIns-3-kinase subunit alpha;
    EC=2.7.1.137 {ECO:0000269|PubMed:23936502}; EC=2.7.1.153 {ECO:0000269|PubMed:15135396,
    ECO:0000269|PubMed:28676499}; AltName: Full=Phosphatidylinositol 4,5-bisphosphate
    3-kinase 110 kDa catalytic subunit alpha; Short=PtdIns-3-kinase subunit p110-alpha;
    Short=p110alpha {ECO:0000303|PubMed:15135396}; AltName: Full=Phosphoinositide
    3-kinase alpha {ECO:0000303|PubMed:28676499}; AltName: Full=Phosphoinositide-3-kinase
    catalytic alpha polypeptide; AltName: Full=Serine/threonine protein kinase PIK3CA;
    EC=2.7.11.1 {ECO:0000269|PubMed:23936502, ECO:0000269|PubMed:28676499};'
  gene_info: Name=PIK3CA;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the PI3/PI4-kinase family. {ECO:0000255|PROSITE-
  protein_domains: ARM-type_fold. (IPR016024); C2_domain_sf. (IPR035892); Kinase-like_dom_sf.
    (IPR011009); PI3-kinase_alpha_cat. (IPR037704); PI3/4_kinase. (IPR015433)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 72
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PIK3CA-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P42336
- **Protein Description:** RecName: Full=Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform; Short=PI3-kinase subunit alpha; Short=PI3K-alpha; Short=PI3Kalpha {ECO:0000303|PubMed:28676499}; Short=PtdIns-3-kinase subunit alpha; EC=2.7.1.137 {ECO:0000269|PubMed:23936502}; EC=2.7.1.153 {ECO:0000269|PubMed:15135396, ECO:0000269|PubMed:28676499}; AltName: Full=Phosphatidylinositol 4,5-bisphosphate 3-kinase 110 kDa catalytic subunit alpha; Short=PtdIns-3-kinase subunit p110-alpha; Short=p110alpha {ECO:0000303|PubMed:15135396}; AltName: Full=Phosphoinositide 3-kinase alpha {ECO:0000303|PubMed:28676499}; AltName: Full=Phosphoinositide-3-kinase catalytic alpha polypeptide; AltName: Full=Serine/threonine protein kinase PIK3CA; EC=2.7.11.1 {ECO:0000269|PubMed:23936502, ECO:0000269|PubMed:28676499};
- **Gene Information:** Name=PIK3CA;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PI3/PI4-kinase family. {ECO:0000255|PROSITE-
- **Key Domains:** ARM-type_fold. (IPR016024); C2_domain_sf. (IPR035892); Kinase-like_dom_sf. (IPR011009); PI3-kinase_alpha_cat. (IPR037704); PI3/4_kinase. (IPR015433)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PIK3CA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PIK3CA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PIK3CA** (gene ID: PIK3CA, UniProt: P42336) in human.

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
- **UniProt Accession:** P42336
- **Protein Description:** RecName: Full=Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform; Short=PI3-kinase subunit alpha; Short=PI3K-alpha; Short=PI3Kalpha {ECO:0000303|PubMed:28676499}; Short=PtdIns-3-kinase subunit alpha; EC=2.7.1.137 {ECO:0000269|PubMed:23936502}; EC=2.7.1.153 {ECO:0000269|PubMed:15135396, ECO:0000269|PubMed:28676499}; AltName: Full=Phosphatidylinositol 4,5-bisphosphate 3-kinase 110 kDa catalytic subunit alpha; Short=PtdIns-3-kinase subunit p110-alpha; Short=p110alpha {ECO:0000303|PubMed:15135396}; AltName: Full=Phosphoinositide 3-kinase alpha {ECO:0000303|PubMed:28676499}; AltName: Full=Phosphoinositide-3-kinase catalytic alpha polypeptide; AltName: Full=Serine/threonine protein kinase PIK3CA; EC=2.7.11.1 {ECO:0000269|PubMed:23936502, ECO:0000269|PubMed:28676499};
- **Gene Information:** Name=PIK3CA;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PI3/PI4-kinase family. {ECO:0000255|PROSITE-
- **Key Domains:** ARM-type_fold. (IPR016024); C2_domain_sf. (IPR035892); Kinase-like_dom_sf. (IPR011009); PI3-kinase_alpha_cat. (IPR037704); PI3/4_kinase. (IPR015433)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PIK3CA" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PIK3CA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PIK3CA** (gene ID: PIK3CA, UniProt: P42336) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# PIK3CA (human; UniProt P42336): functional-annotation research report

## Executive summary

**Identity is verified.** The requested target is unambiguously human **PIK3CA** (*Homo sapiens*), encoding the approximately 110-kDa **p110α catalytic subunit of class IA phosphoinositide 3-kinase (PI3Kα)**; recent structural literature explicitly associates human p110α with **UniProt P42336**. Its conserved adaptor-binding, RAS-binding, C2, helical and kinase domains agree with the supplied PI3/PI4-kinase-family and InterPro annotations. No evidence of symbol confusion with another gene or organism was encountered. (sheng2024molecularbasisof pages 9-11, sheng2024molecularbasisof pages 4-9)

The primary physiological function is **membrane lipid phosphorylation**:

**ATP + phosphatidylinositol-4,5-bisphosphate [PI(4,5)P₂; PIP₂] → ADP + phosphatidylinositol-3,4,5-trisphosphate [PI(3,4,5)P₃; PIP₃].**

PI3Kα transfers phosphate to the 3-hydroxyl of the inositol ring. PIP₃ is a transient membrane second messenger rather than a soluble product; PTEN reverses the reaction by removing the 3-phosphate. Reported protein-kinase activity is secondary and of uncertain in-vivo importance. (sulaiman2023detectionofphosphorylationa pages 16-21, sulaiman2023detectionofphosphorylationa pages 26-30, nicholas2022characterizationofras pages 20-25)

| Aspect | Evidence-based annotation | Key quantitative/detail |
|---|---|---|
| Identity | Human **PIK3CA** encodes p110α, the catalytic subunit of class IA phosphoinositide 3-kinase α (**PI3Kα**); this matches **UniProt P42336** and is not a different, similarly named protein. (sheng2024molecularbasisof pages 9-11, sheng2024molecularbasisof pages 4-9) | Organism: *Homo sapiens*; protein: p110α/PI3Kα catalytic subunit. |
| Domain architecture | The N-to-C-terminal organization is adaptor-binding (ABD), RAS-binding (RBD), C2, helical, and kinase domains, consistent with the supplied PI3/PI4-kinase-family and InterPro annotations. (sheng2024molecularbasisof pages 9-11) | ABD **16–105**; RBD **187–289**; C2 **330–487**; helical **517–694**; kinase **765–1051**. |
| Holoenzyme and regulation | p110α forms an obligate class IA heterodimer with a p85-family regulatory adaptor. The adaptor stabilizes p110α but also imposes basal inhibition through SH2/iSH2 contacts. Partners include p85α, p85β, p55γ, p55α, and p50α. (sheng2024molecularbasisof pages 2-4, sheng2024molecularbasisof pages 4-9) | Regulatory genes include **PIK3R1**, **PIK3R2**, and **PIK3R3**; p55α and p50α are PIK3R1-derived isoforms. |
| Primary reaction and specificity | PI3Kα transfers the γ-phosphate of ATP to the **3-hydroxyl of the inositol ring** of membrane PI(4,5)P₂, producing the second messenger PI(3,4,5)P₃. PTEN terminates the signal by removing that 3-phosphate. (sulaiman2023detectionofphosphorylationa pages 16-21, nicholas2022characterizationofras pages 71-76, nicholas2022characterizationofras pages 20-25) | **ATP + PI(4,5)P₂ → ADP + PI(3,4,5)P₃**; PTEN: **PIP₃ → PI(4,5)P₂**. Protein-kinase activity has been reported, but its in-vivo significance is much less established. (sulaiman2023detectionofphosphorylationa pages 26-30) |
| Localization and activation | The inhibited holoenzyme is predominantly cytosolic. Growth-factor-activated RTKs or adaptors present pYXXM phosphotyrosine motifs to p85 SH2 domains, relieving inhibition and recruiting PI3Kα to the cytosolic face of membranes; RAS-GTP and C2/kinase-domain membrane contacts further orient the enzyme toward PIP₂. (sulaiman2023detectionofphosphorylation pages 16-21, nicholas2022characterizationofras pages 29-33, sheng2024molecularbasisof pages 2-4) | Functional catalysis occurs principally at the **inner plasma-membrane leaflet**; activation involves transition from a closed to an open, membrane-engaged conformation. |
| Major downstream pathway | PIP₃ recruits PH-domain proteins including PDK1 and AKT. PDK1 phosphorylates AKT Thr308 and mTORC2 phosphorylates Ser473; AKT then regulates TSC2, PRAS40, FOXO, GSK3 and mTORC1. (nicholas2022characterizationofras pages 25-29, sulaiman2023detectionofphosphorylationa pages 21-26) | Core axis: **RTK/RAS → PI3Kα → PIP₃ → PDK1/AKT → mTORC1**, controlling growth, metabolism, survival and proliferation. |
| Hotspot mechanisms | **E542K/E545K** in the helical domain disrupt p110α–p85 nSH2 autoinhibitory contacts and generally retain RAS dependence. **H1047R** in the kinase domain reorganizes the C-terminal region, increases binding to anionic membranes and can signal independently of RAS. (sheng2024molecularbasisof pages 20-23, jenkins2023oncogenicmutationsof pages 1-2) | Double mutations can combine release of autoinhibition with enhanced membrane engagement and produce synergistically greater activity. (jenkins2023oncogenicmutationsof pages 1-2, zhang2021pi3kdrivermutations pages 3-4) |
| Physiological roles | Genetic and pharmacological evidence assigns p110α major roles in RTK and insulin signaling, glucose/metabolic control, cell growth and survival, endothelial migration, angiogenesis, vascular remodeling and embryonic development. (sulaiman2023detectionofphosphorylationa pages 26-30, sulaiman2023detectionofphosphorylation pages 26-30, daloglu2023phosphoproteomicanalysisof pages 20-24) | Complete deletion or homozygous kinase-dead mutation is embryonically lethal in mice; heterozygous kinase impairment reduces insulin sensitivity. (sulaiman2023detectionofphosphorylationa pages 26-30) |
| Mutation prevalence | In a pooled analysis of **6,338 breast cancers**, 35.7% carried PIK3CA mutations; prevalence was 42% in HR+/HER2−, 31% in HER2-positive and 16% in triple-negative disease. H1047R, E545K and E542K represented 35%, 17% and 11% of detected variants; 12% of mutant tumors had double mutations. (martinezsaez2020frequencyandspectrum pages 1-2) | A 2023 Taiwanese NGS cohort found mutations in **278/728 (38%)**, with H1047R 41.6%, E545K 18.9% and E542K 10.3% among mutations. (chao2023prevalenceofpik3ca pages 1-2) |
| Alpelisib—breast cancer | Alpelisib is a direct, α-selective PI3K inhibitor approved with fulvestrant for eligible patients with PIK3CA-mutated HR+/HER2− advanced or metastatic breast cancer after endocrine therapy. (shan2024moleculartargetingof pages 11-12, li2024targetingpi3kfamily pages 10-11) | FDA approval: **24 May 2019**. SOLAR-1 median PFS: **11.0 vs 5.7 months**; HR **0.65** (95% CI 0.50–0.85). Treatment discontinuation due to adverse effects: **25% vs 4.2%**. (shan2024moleculartargetingof pages 11-12) |
| Alpelisib—PROS | Alpelisib is the first FDA-approved systemic therapy for adults and children aged ≥2 years with severe PIK3CA-related overgrowth spectrum requiring systemic treatment. (singh2024fdaapprovalsummary pages 1-3) | Accelerated approval: **5 April 2022**. EPIK-P1 efficacy population: **37**; confirmed Week-24 volumetric response **27%** (95% CI 14–44), with **60%** of responders maintaining response ≥12 months. (singh2024fdaapprovalsummary pages 1-3) |
| Inavolisib—breast cancer | Inavolisib is a direct, selective p110α inhibitor that also promotes degradation of mutant p110α; by the end of 2024 it was approved with palbociclib and fulvestrant for PIK3CA-mutated HR+/HER2− advanced breast cancer. (jhaveri2024phaseiibtrial pages 1-2, tomas2025pik3camutationsare pages 10-12) | FDA approval year: **2024**. Early-phase triplets produced confirmed response rates of **52%** with letrozole and **40%** with fulvestrant; these figures are phase I/Ib results, not the phase III approval estimate. (jhaveri2024phaseiibtrial pages 1-2, jhaveri2024phaseiibtrial pages 6-7) |


*Table: Compact evidence-based annotation of human PIK3CA/PI3Kα, covering molecular identity, catalytic function, regulation, disease mutations, prevalence, and direct clinical applications through 2024.*

## 1. Molecular identity, family and structure

PIK3CA/p110α is one of the class IA catalytic isoforms, alongside p110β and p110δ. Its N-to-C-terminal organization is: adaptor-binding domain (**ABD**, residues 16–105), RAS-binding domain (**RBD**, 187–289), C2 domain (330–487), helical domain (517–694) and bilobal kinase domain (765–1051). This architecture explains the supplied annotations: the C2/ARM-like regions organize membrane and protein interactions, whereas the conserved PI3/4-kinase domain supplies the ATP- and lipid-binding catalytic machinery. (sheng2024molecularbasisof pages 9-11, sheng2024molecularbasisof pages 15-16)

p110α normally exists as an obligate heterodimer with a class IA regulatory adaptor—p85α, p85β or p55γ, with p55α and p50α also arising from *PIK3R1*. The ABD binds the adaptor’s inter-SH2 segment, while contacts among p85 nSH2/iSH2 and the p110α C2, helical and kinase regions stabilize the protein but restrain basal activity. Thus, p85 is both a molecular chaperone and an autoinhibitory regulator. (sheng2024molecularbasisof pages 2-4, sheng2024molecularbasisof pages 9-11, sheng2024molecularbasisof pages 12-15)

## 2. Primary biochemical function and substrate specificity

### 2.1 Catalytic reaction

PI3Kα is primarily a **class I phosphoinositide 3-kinase**. It uses ATP to phosphorylate membrane PI(4,5)P₂ at the D3 position, generating PI(3,4,5)P₃. This substrate specificity distinguishes class I enzymes from class II/III PI3Ks, which chiefly generate other 3-phosphorylated phosphoinositides involved in membrane trafficking. In reconstituted assays, p110α–p85α consumes ATP and phosphorylates PIP₂ embedded in vesicles that mimic the inner plasma-membrane leaflet, illustrating that substrate presentation in a lipid bilayer is integral to physiological catalysis. (sulaiman2023detectionofphosphorylationa pages 16-21, nicholas2022characterizationofras pages 71-76, nicholas2022characterizationofras pages 76-80)

PTEN terminates the signal by converting PIP₃ back to PI(4,5)P₂; SHIP phosphatases instead remove the 5-phosphate to form PI(3,4)P₂. The balance between PI3Kα and these lipid phosphatases controls the magnitude, location and duration of the signal. (gavgani2018classiphosphoinositide pages 3-5, nicholas2022characterizationofras pages 20-25)

PI3Kα can also phosphorylate proteins—for example, p85α Ser608 has been reported as a substrate—but the physiological significance of class I PI3K protein-kinase activity remains unresolved. Functional annotation should therefore designate **PIP₂ 3-kinase activity as the primary function**, not serine/threonine protein phosphorylation. (sulaiman2023detectionofphosphorylationa pages 16-21, sulaiman2023detectionofphosphorylationa pages 26-30)

### 2.2 Activation and localization

In unstimulated cells, the inhibited p110α–p85 complex is predominantly cytosolic. Growth-factor or insulin stimulation causes receptor tyrosine kinases—or adaptors such as IRS proteins—to present phosphorylated YXXM motifs. The p85 SH2 domains bind these motifs, recruit the heterodimer to the cytosolic face of the plasma membrane and weaken inhibitory p85–p110α contacts. The complex changes from a closed to an open, membrane-engaged state, bringing the kinase domain into contact with PIP₂. (sulaiman2023detectionofphosphorylation pages 16-21, nicholas2022characterizationofras pages 29-33, sheng2024molecularbasisof pages 2-4)

Membrane-anchored RAS-GTP supplies a cooperating input through the p110α RBD. RAS contributes recruitment, productive orientation and allosteric changes across the RBD, C2, helical and kinase domains. The C2 domain and C-terminal kinase surface also contact anionic lipids. Accordingly, the biologically meaningful site of catalysis is principally the **inner leaflet of stimulated cellular membranes**, especially the plasma membrane, rather than the bulk cytosol or extracellular space. (nicholas2022characterizationofras pages 25-29, nicholas2022characterizationofras pages 29-33)

## 3. Pathway position and biological processes

PIP₃ recruits pleckstrin-homology-domain proteins, particularly PDK1 and AKT, to the membrane. PDK1 phosphorylates AKT Thr308; mTORC2 phosphorylates Ser473. Activated AKT regulates TSC2 and PRAS40 to activate mTORC1, and also acts on FOXO transcription factors, GSK3 and other substrates controlling biosynthesis, proliferation, metabolism and survival. The core pathway is therefore:

**RTK/IRS and RAS → p85–p110α → PIP₃ → PDK1/AKT → TSC–mTORC1 and other AKT effectors.** (nicholas2022characterizationofras pages 25-29, sulaiman2023detectionofphosphorylationa pages 21-26, nicholas2022characterizationofras pages 20-25)

Isoform-specific genetic evidence is strongest for:

* **Insulin and metabolic signaling:** tissue-selective p110α loss impairs insulin-stimulated PIP₃ and AKT signaling in liver and muscle; heterozygous kinase impairment reduces insulin sensitivity. (sulaiman2023detectionofphosphorylationa pages 26-30, daloglu2023phosphoproteomicanalysisof pages 20-24)
* **Development and growth:** complete deletion or homozygous kinase-dead *Pik3ca* is embryonically lethal in mice, demonstrating that catalytic activity is required for normal development. (sulaiman2023detectionofphosphorylationa pages 26-30, sulaiman2023detectionofphosphorylation pages 26-30)
* **Angiogenesis:** p110α selectively supports endothelial migration and vascular remodeling, including VEGF-linked signaling. (gavgani2018classiphosphoinositide pages 13-14, daloglu2023phosphoproteomicanalysisof pages 20-24)
* **Cell growth, survival and differentiation:** loss-of-function experiments impair growth-factor signaling, proliferation, transformation and adipocyte differentiation, while the downstream AKT–mTOR network coordinates anabolic growth and survival. (gavgani2018classiphosphoinositide pages 13-14, daloglu2023phosphoproteomicanalysisof pages 20-24, sulaiman2023detectionofphosphorylationa pages 21-26)

These processes are not separate enzymatic functions; they are consequences of localized PIP₃ production.

## 4. Oncogenic activation and recent structural understanding

PIK3CA is among the most frequently mutated oncogenes in solid tumors. Mutations activate the same lipid-kinase reaction but remove its normal dependence on upstream signals. Importantly, different domains use different mechanisms.

* **E542K and E545K**, in the helical domain, reverse charge and disrupt inhibitory contacts with p85 nSH2. They mimic phosphotyrosine-mediated release of autoinhibition and generally retain greater dependence on RAS for transformation.
* **H1047R**, in the kinase domain, remodels the C-terminal membrane-interacting surface, adds favorable electrostatics toward anionic membranes and improves PIP₂ engagement. It can transform with less RAS dependence.
* C2 mutations such as N345K can weaken C2–iSH2 restraint; ABD mutations perturb ABD–kinase coupling. (sheng2024molecularbasisof pages 20-23, zhang2021pi3kdrivermutations pages 3-4)

A 2023 biochemical/HDX-MS study showed that membrane activation entails disengagement of the ABD from the catalytic core, separation of C2 from p85 iSH2 and reorientation of the p110α C terminus. H1047R, M1043I/L, G1049R and other C-terminal mutants enhance membrane recruitment through non-identical mechanisms. This argues against treating every PIK3CA mutation as one structural class. [Jenkins et al., *Nature Communications*, January 2023, DOI URL](https://doi.org/10.1038/s41467-023-35789-6). (jenkins2023oncogenicmutationsof pages 1-2)

Double mutations can combine complementary mechanisms—release of p85 inhibition plus stronger membrane/substrate engagement—and yield synergistically higher activity. Recent expert analysis consequently favors mutation-aware inhibitors rather than assuming that a single ATP-site drug will have an optimal therapeutic window for every variant. The allosteric agent STX-478, for example, has been reported to prefer H1047R over wild-type p110α and E545K, illustrating the feasibility of conformation-selective targeting. [Sheng et al., published December 2024, *Cancers* 17:77, DOI URL](https://doi.org/10.3390/cancers17010077). (sheng2024molecularbasisof pages 20-23, sheng2024molecularbasisof pages 19-20)

## 5. Mutation prevalence and diagnostic implementation

In a pooled analysis of 6,338 breast cancers, 2,261 (**35.7%**) were PIK3CA-mutated. Rates were **42% in HR+/HER2−**, **31% in HER2-positive** and **16% in triple-negative** disease. Five variants comprised 73% of detected mutations: H1047R 35%, E545K 17%, E542K 11%, N345K 6% and H1047L 4%; 12% of mutant tumors carried double mutations. [Martínez-Sáez et al., May 2020, DOI URL](https://doi.org/10.1186/s13058-020-01284-9). (martinezsaez2020frequencyandspectrum pages 1-2)

A 2023 Taiwanese NGS cohort found PIK3CA mutations in **278/728 patients (38%)**; among mutations, H1047R represented 41.6%, E545K 18.9% and E542K 10.3%. This broadly confirms hotspot dominance while showing population and subtype variation. [Chao et al., August 2023, DOI URL](https://doi.org/10.3389/fonc.2023.1192946). (chao2023prevalenceofpik3ca pages 1-2)

Testing is clinically actionable but method-dependent. A hotspot companion panel was estimated to capture only 72% of all variants and 80% of patients known to be mutation-positive; 28% of variants found by ctDNA in one advanced-disease cohort lay outside the panel. Tissue and plasma assays also differ in sensitivity, tumor fraction and timing. Broad validated NGS can therefore be preferable where available; a negative plasma result may warrant tissue testing when clinical suspicion remains. (martinezsaez2020frequencyandspectrum pages 1-2, anderson2020asystematicreview pages 3-4, anderson2020asystematicreview pages 2-3)

## 6. Current clinical applications through 2024

### 6.1 PIK3CA-mutant breast cancer

**Alpelisib** is an ATP-pocket, PI3Kα-selective inhibitor. The FDA approved it on **24 May 2019**, with fulvestrant, for eligible postmenopausal women and men with PIK3CA-mutated HR-positive/HER2-negative advanced or metastatic breast cancer after endocrine therapy. In SOLAR-1, median progression-free survival in the mutant cohort was **11.0 versus 5.7 months** (hazard ratio 0.65, 95% CI 0.50–0.85). However, adverse-event discontinuation was **25% versus 4.2%**, demonstrating a clinically important therapeutic-index limitation. (shan2024moleculartargetingof pages 11-12, browne2024resistancetotargeted pages 4-6)

Biochemically, alpelisib is much more potent against PI3Kα than PI3Kβ (reported IC₅₀ values 4.6 versus 1,156 nM), but it inhibits wild-type as well as mutant PI3Kα. This explains both efficacy and metabolic toxicity. (li2024targetingpi3kfamily pages 10-11)

**Inavolisib** is a selective p110α inhibitor that also promotes degradation of mutant p110α. By the end of 2024 it had been approved in combination with palbociclib and fulvestrant for an eligible PIK3CA-mutated HR+/HER2− advanced breast-cancer population. Supporting phase I/Ib work reported confirmed objective responses of **52%** with a letrozole triplet and **40%** with a fulvestrant triplet, with median PFS of 23.3 and 35.0 months, respectively; these uncontrolled early-phase values should not be interpreted as the randomized phase III treatment effect. Stomatitis, hyperglycemia and diarrhea were common. [Jhaveri et al., November 2024, DOI URL](https://doi.org/10.1200/JCO.24.00110). (jhaveri2024phaseiibtrial pages 1-2, jhaveri2024phaseiibtrial pages 6-7, tomas2025pik3camutationsare pages 10-12)

Capivasertib should be distinguished mechanistically: it is a **downstream pan-AKT inhibitor**, not a direct PIK3CA/p110α inhibitor, although its approved biomarker-defined population can include PIK3CA alterations. (liu2024newemergingtherapies pages 2-4, tomas2025pik3camutationsare pages 10-12)

### 6.2 PIK3CA-related overgrowth spectrum

Postzygotic activating PIK3CA variants cause mosaic PIK3CA-related overgrowth spectrum (PROS), including CLOVES and related vascular/segmental-overgrowth phenotypes. This is the clearest non-oncology demonstration that excess p110α signaling is sufficient to drive human tissue overgrowth. Open Targets independently links PIK3CA strongly to PROS, CLOVES and megalencephaly-capillary malformation syndromes. (OpenTargets Search: -PIK3CA)

On **5 April 2022**, FDA granted accelerated approval to alpelisib (VIJOICE) for adults and children aged at least two years with severe PROS requiring systemic therapy. EPIK-P1 used expanded-access real-world data: 57 patients contributed safety data and 37 formed the efficacy population. Response required at least a 20% reduction in the summed volume of up to three target lesions without progression elsewhere. At week 24, **27%** responded (95% CI 14–44), and **60% of responders** maintained response for at least 12 months. [FDA approval summary, published August 2024, DOI URL](https://doi.org/10.1158/1078-0432.CCR-23-1270). (singh2024fdaapprovalsummary pages 1-3, singh2024fdaapprovalsummary pages 3-4)

In EPIK-P1, diarrhea and stomatitis each occurred in 16%, hyperglycemia in 12%, and no grade-5 event occurred; the small, retrospectively monitored cohort limits precision, especially for long-term pediatric growth and metabolic safety. (singh2024fdaapprovalsummary pages 6-8, singh2024fdaapprovalsummary pages 12-13)

A 2024 translational study extended implementation to difficult capillary-venous malformations: all 25 treated patients improved clinically, and median MRI lesion volume at six months declined by **33.4% in PIK3CA-mutant** and **27.8% in TEK-mutant** malformations. This is promising real-world evidence but not a randomized estimate. [Zerbib et al., June 2024, DOI URL](https://doi.org/10.1038/s41392-024-01862-9).

## 7. Toxicity, resistance and expert interpretation

Authoritative reviews describe the central problem as a **narrow on-target therapeutic window**. p110α is indispensable for normal insulin action; its inhibition reduces peripheral glucose uptake and promotes hepatic glucose output, causing hyperglycemia and compensatory hyperinsulinemia. In SOLAR-1, hyperglycemia occurred in 63.7% overall and at grade 3/4 in 36.6%. Rash, diarrhea and stomatitis reflect additional normal-tissue pathway dependence. (castel2021thepresentand pages 6-7, shan2024moleculartargetingof pages 19-21)

Compensatory insulin can reactivate tumor PI3K signaling. Within cancer cells, release of FOXO and mTORC1/S6K feedback induces RTKs such as HER3, IGF-1R and insulin receptor. Crosstalk with RAS–MAPK, NF-κB and Wnt pathways can maintain proliferation. PTEN loss is a clinically important escape route because it shifts PIP₃ production toward PI3Kβ; other mechanisms include mutant-PIK3CA amplification, PIK3CB activation, AKT3 upregulation and PDK1–SGK or PIM signaling. [Li et al., August 2024, DOI URL](https://doi.org/10.1186/s12943-024-02072-1). (li2024targetingpi3kfamily pages 22-24, browne2024resistancetotargeted pages 8-9, castel2021thepresentand pages 10-12)

Expert priorities are therefore:

1. **Mutant-selective or allosteric inhibitors** that spare wild-type p110α and reduce metabolic toxicity.
2. **Drug-induced mutant degradation**, exemplified by inavolisib’s mutant-p110α degradation behavior.
3. **Rational combinations** with endocrine/CDK4/6, RTK or context-specific parallel-pathway therapy, rather than indiscriminate multi-pathway blockade.
4. **Metabolic management**—for example metformin or investigation of SGLT2 inhibition—to limit insulin feedback, while recognizing that several proposed strategies remain preclinical.
5. **Better biomarker resolution**, including mutation class, clonality, PTEN status and co-drivers. (castel2021thepresentand pages 7-9, castel2021thepresentand pages 9-10, castel2021thepresentand pages 6-7)

## 8. Functional-annotation conclusion

The most defensible primary annotation is: **PIK3CA encodes the human p110α catalytic component of class IA PI3Kα, a regulated cytosolic-to-membrane lipid kinase that uses ATP to convert membrane PI(4,5)P₂ into PI(3,4,5)P₃ downstream of receptor phosphotyrosines and RAS.** The resulting localized PIP₃ recruits and activates the PDK1–AKT–mTOR signaling system. Its major physiological specialization is growth-factor/insulin signaling, metabolic control, developmental growth and angiogenesis. Oncogenic variants do not create a new reaction; they uncouple the normal reaction from autoinhibition and upstream control, chiefly by disrupting p85 interfaces or increasing membrane/substrate engagement. (sheng2024molecularbasisof pages 2-4, sheng2024molecularbasisof pages 20-23, sulaiman2023detectionofphosphorylationa pages 26-30)

Clinically, the annotation is validated by genotype-directed use of direct PI3Kα inhibitors in PIK3CA-mutant breast cancer and mosaic PROS. The remaining challenge is to suppress mutant signaling without disabling wild-type PI3Kα’s essential metabolic functions or permitting compensatory pathway reactivation. (singh2024fdaapprovalsummary pages 1-3, li2024targetingpi3kfamily pages 22-24, tomas2025pik3camutationsare pages 10-12)

References

1. (sheng2024molecularbasisof pages 9-11): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

2. (sheng2024molecularbasisof pages 4-9): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

3. (sulaiman2023detectionofphosphorylationa pages 16-21): M Sulaiman. Detection of phosphorylation signatures specific to cancer-related pi3-kinase isoforms p110α and p110β. Unknown journal, 2023.

4. (sulaiman2023detectionofphosphorylationa pages 26-30): M Sulaiman. Detection of phosphorylation signatures specific to cancer-related pi3-kinase isoforms p110α and p110β. Unknown journal, 2023.

5. (nicholas2022characterizationofras pages 20-25): Characterization of RAS Interactions with PI3K This article has 0 citations and is from a peer-reviewed journal.

6. (sheng2024molecularbasisof pages 2-4): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

7. (nicholas2022characterizationofras pages 71-76): Characterization of RAS Interactions with PI3K This article has 0 citations and is from a peer-reviewed journal.

8. (sulaiman2023detectionofphosphorylation pages 16-21): M Sulaiman. Detection of phosphorylation signatures specific to cancer-related pi3-kinase isoforms p110α and p110β. Unknown journal, 2023.

9. (nicholas2022characterizationofras pages 29-33): Characterization of RAS Interactions with PI3K This article has 0 citations and is from a peer-reviewed journal.

10. (nicholas2022characterizationofras pages 25-29): Characterization of RAS Interactions with PI3K This article has 0 citations and is from a peer-reviewed journal.

11. (sulaiman2023detectionofphosphorylationa pages 21-26): M Sulaiman. Detection of phosphorylation signatures specific to cancer-related pi3-kinase isoforms p110α and p110β. Unknown journal, 2023.

12. (sheng2024molecularbasisof pages 20-23): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

13. (jenkins2023oncogenicmutationsof pages 1-2): Meredith L. Jenkins, Harish Ranga-Prasad, Matthew A. H. Parson, Noah J. Harris, Manoj K. Rathinaswamy, and John E. Burke. Oncogenic mutations of pik3ca lead to increased membrane recruitment driven by reorientation of the abd, p85 and c-terminus. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35789-6, doi:10.1038/s41467-023-35789-6. This article has 68 citations and is from a highest quality peer-reviewed journal.

14. (zhang2021pi3kdrivermutations pages 3-4): Mingzhen Zhang, Hyunbum Jang, and Ruth Nussinov. Pi3k driver mutations: a biophysical membrane-centric perspective. Cancer Research, 81:237-247, Jan 2021. URL: https://doi.org/10.1158/0008-5472.can-20-0911, doi:10.1158/0008-5472.can-20-0911. This article has 49 citations and is from a highest quality peer-reviewed journal.

15. (sulaiman2023detectionofphosphorylation pages 26-30): M Sulaiman. Detection of phosphorylation signatures specific to cancer-related pi3-kinase isoforms p110α and p110β. Unknown journal, 2023.

16. (daloglu2023phosphoproteomicanalysisof pages 20-24): B Daloğlu. Phosphoproteomic analysis of class ia p110β isoform-specific signal transducers upon pi3k pathway activation. Unknown journal, 2023.

17. (martinezsaez2020frequencyandspectrum pages 1-2): Olga Martínez-Sáez, Nuria Chic, Tomás Pascual, Barbara Adamo, Maria Vidal, Blanca González-Farré, Esther Sanfeliu, Francesco Schettini, Benedetta Conte, Fara Brasó-Maristany, Adela Rodríguez, Débora Martínez, Patricia Galván, Ana Belén Rodríguez, Antonio Martinez, Montserrat Muñoz, and Aleix Prat. Frequency and spectrum of pik3ca somatic mutations in breast cancer. Breast Cancer Research : BCR, May 2020. URL: https://doi.org/10.1186/s13058-020-01284-9, doi:10.1186/s13058-020-01284-9. This article has 498 citations.

18. (chao2023prevalenceofpik3ca pages 1-2): Ta-Chung Chao, Yi-Fang Tsai, Chun-Yu Liu, Pei-Ju Lien, Yen-Shu Lin, Chin-Jung Feng, Yen-Jen Chen, Jiun-I. Lai, Chih-Yi Hsu, Jiun Jen Lynn, Chi-Cheng Huang, and Ling-Ming Tseng. Prevalence of pik3ca mutations in taiwanese patients with breast cancer: a retrospective next-generation sequencing database analysis. Frontiers in Oncology, Aug 2023. URL: https://doi.org/10.3389/fonc.2023.1192946, doi:10.3389/fonc.2023.1192946. This article has 10 citations.

19. (shan2024moleculartargetingof pages 11-12): Khine S. Shan, Amalia Bonano-Rios, Nyein Wint Yee Theik, Atif Hussein, and Marcelo Blaya. Molecular targeting of the phosphoinositide-3-protein kinase (pi3k) pathway across various cancers. International Journal of Molecular Sciences, 25:1973, Feb 2024. URL: https://doi.org/10.3390/ijms25041973, doi:10.3390/ijms25041973. This article has 35 citations.

20. (li2024targetingpi3kfamily pages 10-11): Hongyao Li, Xiang Wen, Yueting Ren, Zhichao Fan, Jin Zhang, Gu He, and Leilei Fu. Targeting pi3k family with small-molecule inhibitors in cancer therapy: current clinical status and future directions. Molecular Cancer, Aug 2024. URL: https://doi.org/10.1186/s12943-024-02072-1, doi:10.1186/s12943-024-02072-1. This article has 130 citations and is from a highest quality peer-reviewed journal.

21. (singh2024fdaapprovalsummary pages 1-3): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

22. (jhaveri2024phaseiibtrial pages 1-2): Komal L. Jhaveri, Melissa K. Accordino, Philippe L. Bedard, Andrés Cervantes, Valentina Gambardella, Erika Hamilton, Antoine Italiano, Kevin Kalinsky, Ian E. Krop, Mafalda Oliveira, Peter Schmid, Cristina Saura, Nicholas C. Turner, Andrea Varga, Sravanthi Cheeti, Stephanie Hilz, Katherine E. Hutchinson, Yanling Jin, Stephanie Royer-Joo, Ubong Peters, Noopur Shankar, Jennifer L. Schutzman, and Dejan Juric. Phase i/ib trial of inavolisib plus palbociclib and endocrine therapy for <i>pik3ca</i> -mutated, hormone receptor–positive, human epidermal growth factor receptor 2–negative advanced or metastatic breast cancer. Nov 2024. URL: https://doi.org/10.1200/jco.24.00110, doi:10.1200/jco.24.00110. This article has 46 citations and is from a highest quality peer-reviewed journal.

23. (tomas2025pik3camutationsare pages 10-12): Ana Tomás and Marta Pojo. Pik3ca mutations: are they a relevant target in adult diffuse gliomas? International Journal of Molecular Sciences, 26:5276, May 2025. URL: https://doi.org/10.3390/ijms26115276, doi:10.3390/ijms26115276. This article has 7 citations.

24. (jhaveri2024phaseiibtrial pages 6-7): Komal L. Jhaveri, Melissa K. Accordino, Philippe L. Bedard, Andrés Cervantes, Valentina Gambardella, Erika Hamilton, Antoine Italiano, Kevin Kalinsky, Ian E. Krop, Mafalda Oliveira, Peter Schmid, Cristina Saura, Nicholas C. Turner, Andrea Varga, Sravanthi Cheeti, Stephanie Hilz, Katherine E. Hutchinson, Yanling Jin, Stephanie Royer-Joo, Ubong Peters, Noopur Shankar, Jennifer L. Schutzman, and Dejan Juric. Phase i/ib trial of inavolisib plus palbociclib and endocrine therapy for <i>pik3ca</i> -mutated, hormone receptor–positive, human epidermal growth factor receptor 2–negative advanced or metastatic breast cancer. Nov 2024. URL: https://doi.org/10.1200/jco.24.00110, doi:10.1200/jco.24.00110. This article has 46 citations and is from a highest quality peer-reviewed journal.

25. (sheng2024molecularbasisof pages 15-16): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

26. (sheng2024molecularbasisof pages 12-15): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

27. (nicholas2022characterizationofras pages 76-80): Characterization of RAS Interactions with PI3K This article has 0 citations and is from a peer-reviewed journal.

28. (gavgani2018classiphosphoinositide pages 3-5): Fatemeh Mazloumi Gavgani, Victoria Smith Arnesen, Rhîan G. Jacobsen, Camilla Krakstad, Erling A. Hoivik, and Aurélia E. Lewis. Class i phosphoinositide 3-kinase pik3ca/p110α and pik3cb/p110β isoforms in endometrial cancer. International Journal of Molecular Sciences, 19:3931, Dec 2018. URL: https://doi.org/10.3390/ijms19123931, doi:10.3390/ijms19123931. This article has 61 citations.

29. (gavgani2018classiphosphoinositide pages 13-14): Fatemeh Mazloumi Gavgani, Victoria Smith Arnesen, Rhîan G. Jacobsen, Camilla Krakstad, Erling A. Hoivik, and Aurélia E. Lewis. Class i phosphoinositide 3-kinase pik3ca/p110α and pik3cb/p110β isoforms in endometrial cancer. International Journal of Molecular Sciences, 19:3931, Dec 2018. URL: https://doi.org/10.3390/ijms19123931, doi:10.3390/ijms19123931. This article has 61 citations.

30. (sheng2024molecularbasisof pages 19-20): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

31. (anderson2020asystematicreview pages 3-4): Elizabeth J. Anderson, Lea E. Mollon, Joni L. Dean, Terri L. Warholak, Ayal Aizer, Emma A. Platt, Derek H. Tang, and Lisa E. Davis. A systematic review of the prevalence and diagnostic workup of pik3ca mutations in hr+/her2– metastatic breast cancer. International Journal of Breast Cancer, 2020:1-16, Jun 2020. URL: https://doi.org/10.1155/2020/3759179, doi:10.1155/2020/3759179. This article has 123 citations.

32. (anderson2020asystematicreview pages 2-3): Elizabeth J. Anderson, Lea E. Mollon, Joni L. Dean, Terri L. Warholak, Ayal Aizer, Emma A. Platt, Derek H. Tang, and Lisa E. Davis. A systematic review of the prevalence and diagnostic workup of pik3ca mutations in hr+/her2– metastatic breast cancer. International Journal of Breast Cancer, 2020:1-16, Jun 2020. URL: https://doi.org/10.1155/2020/3759179, doi:10.1155/2020/3759179. This article has 123 citations.

33. (browne2024resistancetotargeted pages 4-6): Iseult M. Browne and Alicia F. C. Okines. Resistance to targeted inhibitors of the pi3k/akt/mtor pathway in advanced oestrogen-receptor-positive breast cancer. Jun 2024. URL: https://doi.org/10.3390/cancers16122259, doi:10.3390/cancers16122259. This article has 58 citations.

34. (liu2024newemergingtherapies pages 2-4): Liu Liu, Stephanie L. Graff, and Yihong Wang. New emerging therapies targeting pi3k/akt/mtor/pten pathway in hormonal receptor-positive and her2-negative breast cancer—current state and molecular pathology perspective. Cancers, 17:16, Dec 2024. URL: https://doi.org/10.3390/cancers17010016, doi:10.3390/cancers17010016. This article has 33 citations.

35. (OpenTargets Search: -PIK3CA): Open Targets Query (-PIK3CA, 21 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

36. (singh2024fdaapprovalsummary pages 3-4): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

37. (singh2024fdaapprovalsummary pages 6-8): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

38. (singh2024fdaapprovalsummary pages 12-13): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

39. (castel2021thepresentand pages 6-7): Pau Castel, Eneda Toska, Jeffrey A. Engelman, and Maurizio Scaltriti. The present and future of pi3k inhibitors for cancer therapy. Jun 2021. URL: https://doi.org/10.1038/s43018-021-00218-4, doi:10.1038/s43018-021-00218-4. This article has 232 citations and is from a highest quality peer-reviewed journal.

40. (shan2024moleculartargetingof pages 19-21): Khine S. Shan, Amalia Bonano-Rios, Nyein Wint Yee Theik, Atif Hussein, and Marcelo Blaya. Molecular targeting of the phosphoinositide-3-protein kinase (pi3k) pathway across various cancers. International Journal of Molecular Sciences, 25:1973, Feb 2024. URL: https://doi.org/10.3390/ijms25041973, doi:10.3390/ijms25041973. This article has 35 citations.

41. (li2024targetingpi3kfamily pages 22-24): Hongyao Li, Xiang Wen, Yueting Ren, Zhichao Fan, Jin Zhang, Gu He, and Leilei Fu. Targeting pi3k family with small-molecule inhibitors in cancer therapy: current clinical status and future directions. Molecular Cancer, Aug 2024. URL: https://doi.org/10.1186/s12943-024-02072-1, doi:10.1186/s12943-024-02072-1. This article has 130 citations and is from a highest quality peer-reviewed journal.

42. (browne2024resistancetotargeted pages 8-9): Iseult M. Browne and Alicia F. C. Okines. Resistance to targeted inhibitors of the pi3k/akt/mtor pathway in advanced oestrogen-receptor-positive breast cancer. Jun 2024. URL: https://doi.org/10.3390/cancers16122259, doi:10.3390/cancers16122259. This article has 58 citations.

43. (castel2021thepresentand pages 10-12): Pau Castel, Eneda Toska, Jeffrey A. Engelman, and Maurizio Scaltriti. The present and future of pi3k inhibitors for cancer therapy. Jun 2021. URL: https://doi.org/10.1038/s43018-021-00218-4, doi:10.1038/s43018-021-00218-4. This article has 232 citations and is from a highest quality peer-reviewed journal.

44. (castel2021thepresentand pages 7-9): Pau Castel, Eneda Toska, Jeffrey A. Engelman, and Maurizio Scaltriti. The present and future of pi3k inhibitors for cancer therapy. Jun 2021. URL: https://doi.org/10.1038/s43018-021-00218-4, doi:10.1038/s43018-021-00218-4. This article has 232 citations and is from a highest quality peer-reviewed journal.

45. (castel2021thepresentand pages 9-10): Pau Castel, Eneda Toska, Jeffrey A. Engelman, and Maurizio Scaltriti. The present and future of pi3k inhibitors for cancer therapy. Jun 2021. URL: https://doi.org/10.1038/s43018-021-00218-4, doi:10.1038/s43018-021-00218-4. This article has 232 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PIK3CA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. sheng2024molecularbasisof pages 9-11
2. sulaiman2023detectionofphosphorylationa pages 26-30
3. martinezsaez2020frequencyandspectrum pages 1-2
4. shan2024moleculartargetingof pages 11-12
5. singh2024fdaapprovalsummary pages 1-3
6. jenkins2023oncogenicmutationsof pages 1-2
7. sheng2024molecularbasisof pages 4-9
8. sulaiman2023detectionofphosphorylationa pages 16-21
9. nicholas2022characterizationofras pages 20-25
10. sheng2024molecularbasisof pages 2-4
11. nicholas2022characterizationofras pages 71-76
12. sulaiman2023detectionofphosphorylation pages 16-21
13. nicholas2022characterizationofras pages 29-33
14. nicholas2022characterizationofras pages 25-29
15. sulaiman2023detectionofphosphorylationa pages 21-26
16. sheng2024molecularbasisof pages 20-23
17. sulaiman2023detectionofphosphorylation pages 26-30
18. daloglu2023phosphoproteomicanalysisof pages 20-24
19. jhaveri2024phaseiibtrial pages 1-2
20. jhaveri2024phaseiibtrial pages 6-7
21. sheng2024molecularbasisof pages 15-16
22. sheng2024molecularbasisof pages 12-15
23. nicholas2022characterizationofras pages 76-80
24. gavgani2018classiphosphoinositide pages 3-5
25. gavgani2018classiphosphoinositide pages 13-14
26. sheng2024molecularbasisof pages 19-20
27. anderson2020asystematicreview pages 3-4
28. anderson2020asystematicreview pages 2-3
29. browne2024resistancetotargeted pages 4-6
30. liu2024newemergingtherapies pages 2-4
31. singh2024fdaapprovalsummary pages 3-4
32. singh2024fdaapprovalsummary pages 6-8
33. singh2024fdaapprovalsummary pages 12-13
34. castel2021thepresentand pages 6-7
35. shan2024moleculartargetingof pages 19-21
36. browne2024resistancetotargeted pages 8-9
37. castel2021thepresentand pages 10-12
38. castel2021thepresentand pages 7-9
39. castel2021thepresentand pages 9-10
40. PI(4,5)P₂; PIP₂
41. PI(3,4,5)P₃; PIP₃
42. Jenkins et al., *Nature Communications*, January 2023, DOI URL
43. Sheng et al., published December 2024, *Cancers* 17:77, DOI URL
44. Martínez-Sáez et al., May 2020, DOI URL
45. Chao et al., August 2023, DOI URL
46. Jhaveri et al., November 2024, DOI URL
47. FDA approval summary, published August 2024, DOI URL
48. Zerbib et al., June 2024, DOI URL
49. Li et al., August 2024, DOI URL
50. https://doi.org/10.1038/s41467-023-35789-6
51. https://doi.org/10.3390/cancers17010077
52. https://doi.org/10.1186/s13058-020-01284-9
53. https://doi.org/10.3389/fonc.2023.1192946
54. https://doi.org/10.1200/JCO.24.00110
55. https://doi.org/10.1158/1078-0432.CCR-23-1270
56. https://doi.org/10.1038/s41392-024-01862-9
57. https://doi.org/10.1186/s12943-024-02072-1
58. https://doi.org/10.3390/cancers17010077,
59. https://doi.org/10.1038/s41467-023-35789-6,
60. https://doi.org/10.1158/0008-5472.can-20-0911,
61. https://doi.org/10.1186/s13058-020-01284-9,
62. https://doi.org/10.3389/fonc.2023.1192946,
63. https://doi.org/10.3390/ijms25041973,
64. https://doi.org/10.1186/s12943-024-02072-1,
65. https://doi.org/10.1158/1078-0432.ccr-23-1270,
66. https://doi.org/10.1200/jco.24.00110,
67. https://doi.org/10.3390/ijms26115276,
68. https://doi.org/10.3390/ijms19123931,
69. https://doi.org/10.1155/2020/3759179,
70. https://doi.org/10.3390/cancers16122259,
71. https://doi.org/10.3390/cancers17010016,
72. https://doi.org/10.1038/s43018-021-00218-4,