---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-05T01:11:09.374596'
end_time: '2026-10-05T01:41:56.775210'
duration_seconds: 1847.4
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: IGFBP5
  gene_symbol: IGFBP5
  uniprot_accession: P24593
  protein_description: 'RecName: Full=Insulin-like growth factor-binding protein 5;
    Short=IBP-5; Short=IGF-binding protein 5; Short=IGFBP-5; Flags: Precursor;'
  gene_info: Name=IGFBP5; Synonyms=IBP5;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: Growth_fac_rcpt_cys_sf. (IPR009030); IGFBP-5. (IPR012213); IGFBP-like.
    (IPR000867); IGFBP_1-6_chordata. (IPR022321); Insulin_GF-bd_Cys-rich_CS. (IPR017891)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 65
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: IGFBP5-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: IGFBP5-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000020 I have extracted Figure 2 from page 4,
    which illustrates the proposed modes of IGFBP-5 actions across four panels: (A)
    the IGF:IGFB'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P24593
- **Protein Description:** RecName: Full=Insulin-like growth factor-binding protein 5; Short=IBP-5; Short=IGF-binding protein 5; Short=IGFBP-5; Flags: Precursor;
- **Gene Information:** Name=IGFBP5; Synonyms=IBP5;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Growth_fac_rcpt_cys_sf. (IPR009030); IGFBP-5. (IPR012213); IGFBP-like. (IPR000867); IGFBP_1-6_chordata. (IPR022321); Insulin_GF-bd_Cys-rich_CS. (IPR017891)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IGFBP5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IGFBP5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IGFBP5** (gene ID: IGFBP5, UniProt: P24593) in human.

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
- **UniProt Accession:** P24593
- **Protein Description:** RecName: Full=Insulin-like growth factor-binding protein 5; Short=IBP-5; Short=IGF-binding protein 5; Short=IGFBP-5; Flags: Precursor;
- **Gene Information:** Name=IGFBP5; Synonyms=IBP5;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Growth_fac_rcpt_cys_sf. (IPR009030); IGFBP-5. (IPR012213); IGFBP-like. (IPR000867); IGFBP_1-6_chordata. (IPR022321); Insulin_GF-bd_Cys-rich_CS. (IPR017891)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IGFBP5" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IGFBP5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IGFBP5** (gene ID: IGFBP5, UniProt: P24593) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human IGFBP5 (UniProt P24593): functional annotation research report

**Identity verified.** The supplied UniProt accession **P24593** identifies *Homo sapiens* IGFBP5, encoding insulin-like growth factor-binding protein 5 (IGFBP-5; synonym IBP5). Human-protein studies describe a 272-amino-acid precursor and a 252-amino-acid mature protein after removal of its secretion signal. IGFBP-5 is one of the six **high-affinity IGF-binding proteins**, not the distinct proteins IGFBP-3 or IGFBP-7. Its conserved, disulfide-stabilized, cysteine-rich N- and C-terminal regions—12 and six cysteines, respectively—flank a more flexible linker. These features agree with the IGFBP-like and cysteine-rich domain annotations supplied for P24593. IGFBP-5 is a **ligand-binding regulator, not an enzyme or transporter**. (beattie2006insulinlikegrowthfactorbinding pages 2-4, baxter2023signalingpathwaysof pages 2-3, duan2020insulinlikegrowthfactor pages 2-3)

## Primary function, pathway and site of action

IGFBP-5’s best-established function is to control **where and when IGF-1 and IGF-2 can activate IGF1R**. One IGFBP molecule binds one IGF molecule through contributions from both terminal domains. When soluble intact IGFBP-5 sequesters an IGF, it can prevent ligand access to IGF1R and diminish downstream growth and survival signaling; when IGFBP-5 concentrates IGF near a cell or releases it, the same protein can instead enhance signaling. IGF1R-linked PI3K–AKT and MAPK responses are therefore *downstream consequences of altered ligand availability*, not reactions catalyzed by IGFBP-5. This conditional behavior is more informative than labeling the protein simply an IGF inhibitor or activator. (baxter2023signalingpathwaysof pages 2-3, duan2020insulinlikegrowthfactor pages 3-5, sechrist2025pathologicsignalingand pages 2-4)

**Blood.** IGF-bound IGFBP-5 can associate with acid-labile subunit (ALS) to form a roughly 150-kDa ternary complex retained in the circulation. More than half of circulating human IGFBP-5 is reported in these complexes. Separately, approximately **75–80% of circulating IGF** is in ALS complexes containing **either IGFBP-3 or IGFBP-5**—that percentage must not be interpreted as the fraction carried by IGFBP-5 alone. Complex formation extends IGF residence and provides a circulating reservoir; reported free IGF is approximately 1% or less of circulating IGF. (duan2020insulinlikegrowthfactor pages 2-3, baxter2023signalingpathwaysof pages 2-3)

**Extracellular matrix and cell surface.** Secreted IGFBP-5 associates with matrix constituents including collagen, laminin, fibronectin and vitronectin, and with heparin-like glycosaminoglycans; bone-matrix association includes hydroxyapatite. Its basic C-terminal region contributes to these interactions. Matrix binding can protect IGFBP-5 from degradation, retain local IGF, or facilitate IGF delivery near IGF1R. The direction is not invariant: fibronectin suppressed IGFBP-5-mediated potentiation of IGF-1-dependent migration in one cell system. The linker is susceptible to **PAPP-A and PAPP-A2 proteolysis**, which weakens sequestration and can increase receptor access; unlike PAPP-A cleavage of IGFBP-4, cleavage of IGFBP-5 need not require IGF occupancy. These observations locate much of IGFBP-5’s primary action **outside the cell**, in blood and tissue microenvironments. (duan2020insulinlikegrowthfactor pages 2-3, duan2020insulinlikegrowthfactor pages 3-5, baxter2023signalingpathwaysof pages 2-3, baxter2023signalingpathwaysof pages 5-6)

The following evidence matrix separates established compartment-level functions from human observational and preclinical results. (duan2020insulinlikegrowthfactor pages 2-3, sureshbabu2012igfbp5inducescell pages 2-4, nimptsch2024pregnancyassociatedplasma pages 6-7, zhu2024igfbp5affectscardiomyocyte pages 2-6)

| Compartment/context | Direct molecular role or observation | Evidentiary tier | Precise source (year) |
|---|---|---|---|
| Plasma: IGF–IGFBP5–ALS transport | IGFBP5 binds one IGF-1 or IGF-2 molecule and, when IGF-occupied, can bind acid-labile subunit (ALS) to form a ~150-kDa circulating reservoir. **75–80% of circulating IGF** is in ALS ternary complexes containing either IGFBP3 or IGFBP5; viewed from the protein side, **more than half of circulating IGFBP5** is in such complexes. These statistics are related but not interchangeable. (duan2020insulinlikegrowthfactor pages 2-3, baxter2023signalingpathwaysof pages 2-3) | Established biochemical/endocrine function; human circulation plus supporting model evidence | [Baxter, *Endocrine Reviews*](https://doi.org/10.1210/endrev/bnad008) (2023); [Duan & Allard, *Frontiers in Endocrinology*](https://doi.org/10.3389/fendo.2020.00100) (2020) |
| Extracellular matrix and proteolytic release | IGFBP5 binds collagen, laminin, fibronectin, vitronectin, proteoglycans and hydroxyapatite, concentrating or storing IGF near cells. Matrix association can lower effective IGF affinity or alter proteolysis, permitting IGF delivery to IGF1R, although fibronectin can inhibit potentiation in some systems. PAPP-A and PAPP-A2 cleave the linker region; PAPP-A2 cleavage is IGF-independent and relatively selective for IGFBP5, reducing IGF sequestration and increasing receptor access. (duan2020insulinlikegrowthfactor pages 3-5, duan2020insulinlikegrowthfactor pages 2-3, baxter2023signalingpathwaysof pages 2-3, baxter2023signalingpathwaysof pages 5-6) | Strong biochemical and cell-model evidence; physiological direction is matrix- and cell-context dependent | [Baxter, *Endocrine Reviews*](https://doi.org/10.1210/endrev/bnad008) (2023); [Duan & Allard](https://doi.org/10.3389/fendo.2020.00100) (2020) |
| Cell surface: α2β1 integrin | In human MCF-7 cells, an IGF-binding-deficient IGFBP5 mutant retained adhesion activity, whereas α2- or β1-integrin-blocking antibodies inhibited it. Biosensor analysis showed direct, slowly dissociating IGFBP5–α2β1 binding with an equilibrium constant of approximately **0.5 nM**; IGFBP5 increased ILK and Akt-S473 signaling. This supports IGF-independent adhesion/survival signaling. (sureshbabu2012igfbp5inducescell pages 2-4, sureshbabu2012igfbp5inducescell pages 4-5) | Direct mechanistic human-cell evidence with mutant, blocking-antibody and biophysical-binding controls | [Sureshbabu et al., *Journal of Cell Science*](https://doi.org/10.1242/jcs.092882) (2012) |
| Nucleus | IGFBP5 has a C-terminal nuclear-localization sequence and can undergo importin-β-dependent nuclear import. Cell studies report transactivation and interactions with FHL2 or vitamin-D receptor, but target genes and physiological nuclear functions remain incompletely established; nuclear localization is not required for every reported phenotype, including fibrosis. IGFBP3-specific RXR and NLS-mutant findings must not be assigned to IGFBP5. (bach201840yearsof pages 9-10, duan2020insulinlikegrowthfactor pages 7-8, firth2002cellularactionsof pages 15-16, baxter2023signalingpathwaysof pages 10-11) | Demonstrated transport and in-vitro interactions; limited causal in-vivo validation | [Baxter, *Endocrine Reviews*](https://doi.org/10.1210/endrev/bnad008) (2023); [Bach, *Journal of Molecular Endocrinology*](https://doi.org/10.1530/JME-17-0254) (2018) |
| Adult human plasma | Cross-sectional German cohort: **394 adults**, but usable IGFBP5 analyses involved **125** because **68% of measurements were below the detection limit**. Among available values, median IGFBP5 was **22.6 ng/mL** (IQR 6.2–73.7). PAPP-A was positively associated with IGFBP5, whereas PAPP-A2 was not (0.97-fold per 0.05-ng/mL increment; 95% CI 0.85–1.11). Assay censoring and cross-sectional design preclude causal inference. (nimptsch2024pregnancyassociatedplasma pages 6-7, nimptsch2024pregnancyassociatedplasma pages 5-6, nimptsch2024pregnancyassociatedplasma pages 3-4, nimptsch2024pregnancyassociatedplasma pages 4-5, nimptsch2024pregnancyassociatedplasma pages 2-3) | Human quantitative observational evidence; substantial detection-limit limitation | [Nimptsch et al., *Scientific Reports*](https://doi.org/10.1038/s41598-024-52074-8) (2024) |
| Primary human fibrotic-lung fibroblasts and lung organ culture | Recombinant or adenovirally expressed IGFBP5 increased collagen-I/fibronectin deposition, CTGF, LOX and IGFBP5 itself in primary human lung fibroblasts. Human lung-tissue cores from 7–9 donors treated with 500 ng/mL IGFBP5 reproduced ECM/profibrotic responses. IGFBP5 siRNA achieved ~57%, 72% and 69% knockdown in normal, IPF and systemic-sclerosis fibroblasts, respectively, but downstream effects varied by disease and donor. (nguyen2018igfbp5promotesfibrosis pages 7-9, nguyen2018igfbp5promotesfibrosis pages 4-7, nguyen2018igfbp5promotesfibrosis pages 3-4, nguyen2018igfbp5promotesfibrosis pages 2-3) | Direct human-cell and ex-vivo-organ evidence; donor heterogeneity and short exposure limit translation | [Nguyen et al., *Frontiers in Endocrinology*](https://doi.org/10.3389/fendo.2018.00601) (2018) |
| Myocardial infarction model | Cardiomyocyte-targeted Igfbp5 knockdown increased IGF1R/AKT signaling, reduced apoptosis and increased proliferation after ischemic injury. At 21 days after mouse MI, fibrosis was approximately **10% with knockdown versus 18% in controls**; echocardiographic function also improved. Human evidence was limited to IGFBP5-expression measurements in blood from five AMI patients and five controls, so therapeutic efficacy remains preclinical. (zhu2024igfbp5affectscardiomyocyte pages 2-6, zhu2024igfbp5affectscardiomyocyte pages 1-2, zhu2024igfbp5affectscardiomyocyte pages 6-6, zhu2024igfbp5affectscardiomyocyte pages 10-11) | Causal rodent and rat-cell evidence; minimal human observational evidence; **no demonstrated clinical approval** | [Zhu et al., *Communications Biology*](https://doi.org/10.1038/s42003-024-07304-0) (2024) |


*Table: Compartment-resolved evidence for human IGFBP5/P24593, separating established molecular functions, human observational findings and preclinical disease models. No row represents an approved IGFBP5-directed clinical intervention.*

Figure 2 of Duan and Allard’s [March 2020 IGFBP-5 review](https://doi.org/10.3389/fendo.2020.00100) illustrates the proposed progression from circulating IGF–IGFBP-5–ALS transport to IGF sequestration, matrix- or protease-enabled delivery, and possible IGF-independent actions. Its membrane-receptor and nuclear panels are **models**, not proof that every depicted route is physiologically required. (duan2020insulinlikegrowthfactor media 295916b3, duan2020insulinlikegrowthfactor pages 3-5)

## Additional experimentally supported actions

**IGF-independent cell-surface signaling.** In human MCF-7 cells, an IGFBP-5 mutant unable to bind IGFs still promoted adhesion, whereas disruption of its C-terminal heparin-binding region removed that adhesion response. Blocking α2 or β1 integrin inhibited adhesion; direct binding of purified α2β1 integrin to IGFBP-5 was measured with an estimated equilibrium dissociation constant of approximately **0.5 nM**. Increased integrin-linked kinase expression and Akt Ser473 phosphorylation accompanied the response. These are relatively strong controls for an IGF-independent **IGFBP-5–α2β1-integrin-associated** mechanism in this cell model, not evidence that integrin signaling replaces IGF binding as the protein’s general function. ([Sureshbabu et al., *Journal of Cell Science*, April 2012](https://doi.org/10.1242/jcs.092882).) (sureshbabu2012igfbp5inducescell pages 2-4, sureshbabu2012igfbp5inducescell pages 4-5)

**Nuclear localization: demonstrated entry, less certain physiological role.** IGFBP-5 has a basic C-terminal nuclear-localization region and has been observed entering nuclei through an importin-dependent route. In human osteosarcoma cells, knockdown increased apoptosis; an IGF-binding-competent rescue construct with reduced nuclear localization restored survival, whereas an IGF-binding-deficient construct retaining nuclear localization did not. That experiment supports **IGF binding rather than nuclear entry** as necessary for that particular survival phenotype. Interactions with candidate nuclear partners, including FHL2 or the vitamin-D-receptor pathway, have been reported in experimental systems, but in-vivo target genes and the general importance of nuclear IGFBP-5 remain unresolved. RXR-dependent nuclear mechanisms established for **IGFBP-3** should not be assigned to IGFBP-5. ([Duan and Allard, March 2020](https://doi.org/10.3389/fendo.2020.00100); [Baxter, *Endocrine Reviews*, March 2023](https://doi.org/10.1210/endrev/bnad008).) (duan2020insulinlikegrowthfactor pages 5-7, duan2020insulinlikegrowthfactor pages 7-8, firth2002cellularactionsof pages 15-16, baxter2023signalingpathwaysof pages 10-11)

**Tissue remodeling and senescence.** Recombinant or adenovirally expressed IGFBP-5 increased extracellular-matrix proteins and profibrotic mediators, including CTGF and lysyl oxidase, in primary human lung fibroblasts; human lung tissue maintained in organ culture also responded. In fibroblasts from idiopathic pulmonary fibrosis, IGFBP5 silencing reduced COL1A1 and CTGF, but effects in normal and systemic-sclerosis donor cells differed, and some gene responses were nonsignificant. This supports a context-dependent contribution to a fibrotic program, not a universal fibrosis pathway. In older human endothelial-cell cultures, reducing IGFBP-5 partially reversed senescence markers, whereas adding or expressing it induced senescence in young cultures; the reported mechanism involves p53. These secondary actions matter biologically but should not obscure the established IGF-regulatory function. ([Nguyen et al., *Frontiers in Endocrinology*, October 2018](https://doi.org/10.3389/fendo.2018.00601); [Kim et al., *Molecular Biology of the Cell*, November 2007](https://doi.org/10.1091/mbc.e07-03-0280).) (nguyen2018igfbp5promotesfibrosis pages 4-7, nguyen2018igfbp5promotesfibrosis pages 3-4, kim2007inductionofcellular pages 2-3, kim2007inductionofcellular pages 3-4)

## Developments and quantitative evidence, emphasizing 2023–2024

* **Mechanistic reassessment (2023).** Baxter’s authoritative [March 2023 review](https://doi.org/10.1210/endrev/bnad008) places IGFBP-5 within a framework of ligand sequestration, regulated proteolysis, matrix-dependent potentiation and selected IGF-independent signaling. It cautions against transferring mechanisms demonstrated for other IGFBPs to IGFBP-5. (baxter2023signalingpathwaysof pages 2-3, baxter2023signalingpathwaysof pages 5-6)
* **Human circulating measurements (2024).** A [January 2024 cross-sectional study](https://doi.org/10.1038/s41598-024-52074-8) included **394 adults**, but IGFBP-5 analyses used **125** because **68% of measurements were below the assay detection limit**. In the analyzable subset, median IGFBP-5 was **22.6 ng/mL** (interquartile range 6.2–73.7). PAPP-A was positively associated with IGFBP-5, whereas the estimated IGFBP-5 association with PAPP-A2 was **0.97-fold per 0.05 ng/mL** higher PAPP-A2 (95% CI 0.85–1.11). The censoring and cross-sectional design preclude an inference that the measured protease caused an individual’s circulating IGFBP-5 level. (nimptsch2024pregnancyassociatedplasma pages 5-6, nimptsch2024pregnancyassociatedplasma pages 6-7, nimptsch2024pregnancyassociatedplasma pages 3-4, nimptsch2024pregnancyassociatedplasma pages 4-5)
* **Human tissue association (2024).** In [August 2024 pelvic-organ-prolapse tissue work](https://doi.org/10.1038/s41598-024-69098-9), IGFBP-5 protein and transcript abundance were lower in affected vaginal-wall samples; reported relative Western-blot expression was **0.45 ± 0.2333 versus 1.00 ± 0.8160** in controls (*P* < 0.01). Lower expression also tracked older age and greater prolapse severity. The authors could not establish whether reduced IGFBP-5 was a cause or consequence of prolapse. (duan2024expressionofinsulinlike pages 9-10, duan2024expressionofinsulinlike pages 4-6)
* **Ischemic injury model (2024).** In [November 2024 mouse myocardial-infarction experiments](https://doi.org/10.1038/s42003-024-07304-0), cardiomyocyte-directed *Igfbp5* knockdown increased IGF1R/AKT signaling and reduced apoptosis; measured fibrosis at 21 days was approximately **10% versus 18%** in infarcted controls. An IGF1R inhibitor countered protective knockdown effects in cultured rat cardiomyocytes. Human observations in that study were limited to blood-expression measurements from **five infarction patients and five controls**: the efficacy result is **preclinical**, not a human treatment outcome. (zhu2024igfbp5affectscardiomyocyte pages 2-6, zhu2024igfbp5affectscardiomyocyte pages 6-6, zhu2024igfbp5affectscardiomyocyte pages 10-11)

## Applications and assessment

**Current implementation is chiefly research use:** measuring IGFBP-5 in human blood or tissues, studying IGF availability and protease activity, and perturbing IGFBP5 in cell, organ-culture and animal disease models. The retrieved evidence does **not** establish a validated stand-alone IGFBP-5 clinical diagnostic, an approved IGFBP-5-directed treatment, or a demonstrated human therapeutic benefit from increasing or decreasing the protein. Because IGFBP-5 can either restrict or support IGF1R signaling and has context-specific matrix and integrin actions, any therapeutic strategy requires tissue-specific mechanism and safety assessment; ordinary systemic expression measurements alone cannot determine the direction of local signaling. ([Baxter, March 2023](https://doi.org/10.1210/endrev/bnad008); [Mancarella et al., May 2024](https://doi.org/10.3390/ijms25115915).) (duan2020insulinlikegrowthfactor pages 3-5, mancarella2024extracellularinteractorsof pages 3-5, duan2024expressionofinsulinlike pages 1-2, nimptsch2024pregnancyassociatedplasma pages 1-2)

**Bottom line:** Annotate human IGFBP5/P24593 principally as a **secreted, extracellular high-affinity IGF-1/IGF-2-binding regulator** that transports and stores IGFs, restricts receptor access when intact and soluble, and can promote local IGF signaling following matrix-dependent presentation or proteolysis. Annotate α2β1-integrin-associated signaling, nuclear localization, senescence and fibrotic remodeling as **experimentally observed but context-dependent additional functions**, with the nuclear pathway’s physiological contribution less securely established. (baxter2023signalingpathwaysof pages 2-3, duan2020insulinlikegrowthfactor pages 2-3, sureshbabu2012igfbp5inducescell pages 2-4, duan2020insulinlikegrowthfactor pages 5-7, nguyen2018igfbp5promotesfibrosis pages 7-9)

References

1. (beattie2006insulinlikegrowthfactorbinding pages 2-4): James Beattie, Gordon J. Allan, Jennifer D. Lochrie, and David J. Flint. Insulin-like growth factor-binding protein-5 (igfbp-5): a critical member of the igf axis. The Biochemical journal, 395 1:1-19, Apr 2006. URL: https://doi.org/10.1042/bj20060086, doi:10.1042/bj20060086. This article has 296 citations.

2. (baxter2023signalingpathwaysof pages 2-3): Robert C Baxter. Signaling pathways of the insulin-like growth factor binding proteins. Endocrine Reviews, 44:753-778, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad008, doi:10.1210/endrev/bnad008. This article has 193 citations and is from a domain leading peer-reviewed journal.

3. (duan2020insulinlikegrowthfactor pages 2-3): Cunming Duan and John B. Allard. Insulin-like growth factor binding protein-5 in physiology and disease. Frontiers in Endocrinology, Mar 2020. URL: https://doi.org/10.3389/fendo.2020.00100, doi:10.3389/fendo.2020.00100. This article has 122 citations.

4. (duan2020insulinlikegrowthfactor pages 3-5): Cunming Duan and John B. Allard. Insulin-like growth factor binding protein-5 in physiology and disease. Frontiers in Endocrinology, Mar 2020. URL: https://doi.org/10.3389/fendo.2020.00100, doi:10.3389/fendo.2020.00100. This article has 122 citations.

5. (sechrist2025pathologicsignalingand pages 2-4): Zachary R. Sechrist, Jaeden S. Cortés, Nidhi R. Patel, Zoe J. Pittman, Gayathri Guru Murthy, Guangzhen Zhu, Calvin L. Cole, and Benjamin D. Korman. Pathologic signaling and disease implications of insulin-like growth factor binding proteins in cancer, cardiovascular disease, and fibrosis. International Journal of Molecular Sciences, 26:10248, Oct 2025. URL: https://doi.org/10.3390/ijms262110248, doi:10.3390/ijms262110248. This article has 10 citations.

6. (baxter2023signalingpathwaysof pages 5-6): Robert C Baxter. Signaling pathways of the insulin-like growth factor binding proteins. Endocrine Reviews, 44:753-778, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad008, doi:10.1210/endrev/bnad008. This article has 193 citations and is from a domain leading peer-reviewed journal.

7. (sureshbabu2012igfbp5inducescell pages 2-4): A. Sureshbabu, H. Okajima, D. Yamanaka, E. Tonner, Surya Shastri, Joanna Maycock, M. Szymanowska, J. Shand, Shin-ichiro Takahashi, J. Beattie, G. Allan, and D. Flint. Igfbp5 induces cell adhesion, increases cell survival and inhibits cell migration in mcf-7 human breast cancer cells. Journal of Cell Science, 125:1693-1705, Apr 2012. URL: https://doi.org/10.1242/jcs.092882, doi:10.1242/jcs.092882. This article has 123 citations and is from a domain leading peer-reviewed journal.

8. (nimptsch2024pregnancyassociatedplasma pages 6-7): Katharina Nimptsch, Elif Ece Aydin, Rafael Francisco Rios Chavarria, Jürgen Janke, Matthew N. Poy, Claus Oxvig, Astrid Steinbrecher, and Tobias Pischon. Pregnancy associated plasma protein-a2 (papp-a2) and stanniocalcin-2 (stc2) but not papp-a are associated with circulating total igf-1 in a human adult population. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52074-8, doi:10.1038/s41598-024-52074-8. This article has 4 citations and is from a peer-reviewed journal.

9. (zhu2024igfbp5affectscardiomyocyte pages 2-6): Qingqing Zhu, Xinyi Lu, Mengli Chen, Ting Zhang, Mengsha Shi, Wenming Yao, Haifeng Zhang, Rongrong Gao, Xinli Li, Yanli Zhou, and Shengen Liao. Igfbp5 affects cardiomyocyte survival and functional recovery in mice following myocardial ischemia. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07304-0, doi:10.1038/s42003-024-07304-0. This article has 7 citations and is from a peer-reviewed journal.

10. (sureshbabu2012igfbp5inducescell pages 4-5): A. Sureshbabu, H. Okajima, D. Yamanaka, E. Tonner, Surya Shastri, Joanna Maycock, M. Szymanowska, J. Shand, Shin-ichiro Takahashi, J. Beattie, G. Allan, and D. Flint. Igfbp5 induces cell adhesion, increases cell survival and inhibits cell migration in mcf-7 human breast cancer cells. Journal of Cell Science, 125:1693-1705, Apr 2012. URL: https://doi.org/10.1242/jcs.092882, doi:10.1242/jcs.092882. This article has 123 citations and is from a domain leading peer-reviewed journal.

11. (bach201840yearsof pages 9-10): Leon A. Bach. 40 years of igf1: igf-binding proteins. Journal of Molecular Endocrinology, 61:T11-T28, Jul 2018. URL: https://doi.org/10.1530/jme-17-0254, doi:10.1530/jme-17-0254. This article has 329 citations and is from a peer-reviewed journal.

12. (duan2020insulinlikegrowthfactor pages 7-8): Cunming Duan and John B. Allard. Insulin-like growth factor binding protein-5 in physiology and disease. Frontiers in Endocrinology, Mar 2020. URL: https://doi.org/10.3389/fendo.2020.00100, doi:10.3389/fendo.2020.00100. This article has 122 citations.

13. (firth2002cellularactionsof pages 15-16): SM Firth and RC Baxter. Cellular actions of the insulin-like growth factor binding proteins. Endocrine reviews, 23 6:824-54, Dec 2002. URL: https://doi.org/10.1210/er.2001-0033, doi:10.1210/er.2001-0033. This article has 2359 citations and is from a domain leading peer-reviewed journal.

14. (baxter2023signalingpathwaysof pages 10-11): Robert C Baxter. Signaling pathways of the insulin-like growth factor binding proteins. Endocrine Reviews, 44:753-778, Mar 2023. URL: https://doi.org/10.1210/endrev/bnad008, doi:10.1210/endrev/bnad008. This article has 193 citations and is from a domain leading peer-reviewed journal.

15. (nimptsch2024pregnancyassociatedplasma pages 5-6): Katharina Nimptsch, Elif Ece Aydin, Rafael Francisco Rios Chavarria, Jürgen Janke, Matthew N. Poy, Claus Oxvig, Astrid Steinbrecher, and Tobias Pischon. Pregnancy associated plasma protein-a2 (papp-a2) and stanniocalcin-2 (stc2) but not papp-a are associated with circulating total igf-1 in a human adult population. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52074-8, doi:10.1038/s41598-024-52074-8. This article has 4 citations and is from a peer-reviewed journal.

16. (nimptsch2024pregnancyassociatedplasma pages 3-4): Katharina Nimptsch, Elif Ece Aydin, Rafael Francisco Rios Chavarria, Jürgen Janke, Matthew N. Poy, Claus Oxvig, Astrid Steinbrecher, and Tobias Pischon. Pregnancy associated plasma protein-a2 (papp-a2) and stanniocalcin-2 (stc2) but not papp-a are associated with circulating total igf-1 in a human adult population. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52074-8, doi:10.1038/s41598-024-52074-8. This article has 4 citations and is from a peer-reviewed journal.

17. (nimptsch2024pregnancyassociatedplasma pages 4-5): Katharina Nimptsch, Elif Ece Aydin, Rafael Francisco Rios Chavarria, Jürgen Janke, Matthew N. Poy, Claus Oxvig, Astrid Steinbrecher, and Tobias Pischon. Pregnancy associated plasma protein-a2 (papp-a2) and stanniocalcin-2 (stc2) but not papp-a are associated with circulating total igf-1 in a human adult population. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52074-8, doi:10.1038/s41598-024-52074-8. This article has 4 citations and is from a peer-reviewed journal.

18. (nimptsch2024pregnancyassociatedplasma pages 2-3): Katharina Nimptsch, Elif Ece Aydin, Rafael Francisco Rios Chavarria, Jürgen Janke, Matthew N. Poy, Claus Oxvig, Astrid Steinbrecher, and Tobias Pischon. Pregnancy associated plasma protein-a2 (papp-a2) and stanniocalcin-2 (stc2) but not papp-a are associated with circulating total igf-1 in a human adult population. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52074-8, doi:10.1038/s41598-024-52074-8. This article has 4 citations and is from a peer-reviewed journal.

19. (nguyen2018igfbp5promotesfibrosis pages 7-9): Xinh-Xinh Nguyen, Lutfiyya Muhammad, Paul J. Nietert, and Carol Feghali-Bostwick. Igfbp-5 promotes fibrosis via increasing its own expression and that of other pro-fibrotic mediators. Frontiers in Endocrinology, Oct 2018. URL: https://doi.org/10.3389/fendo.2018.00601, doi:10.3389/fendo.2018.00601. This article has 88 citations.

20. (nguyen2018igfbp5promotesfibrosis pages 4-7): Xinh-Xinh Nguyen, Lutfiyya Muhammad, Paul J. Nietert, and Carol Feghali-Bostwick. Igfbp-5 promotes fibrosis via increasing its own expression and that of other pro-fibrotic mediators. Frontiers in Endocrinology, Oct 2018. URL: https://doi.org/10.3389/fendo.2018.00601, doi:10.3389/fendo.2018.00601. This article has 88 citations.

21. (nguyen2018igfbp5promotesfibrosis pages 3-4): Xinh-Xinh Nguyen, Lutfiyya Muhammad, Paul J. Nietert, and Carol Feghali-Bostwick. Igfbp-5 promotes fibrosis via increasing its own expression and that of other pro-fibrotic mediators. Frontiers in Endocrinology, Oct 2018. URL: https://doi.org/10.3389/fendo.2018.00601, doi:10.3389/fendo.2018.00601. This article has 88 citations.

22. (nguyen2018igfbp5promotesfibrosis pages 2-3): Xinh-Xinh Nguyen, Lutfiyya Muhammad, Paul J. Nietert, and Carol Feghali-Bostwick. Igfbp-5 promotes fibrosis via increasing its own expression and that of other pro-fibrotic mediators. Frontiers in Endocrinology, Oct 2018. URL: https://doi.org/10.3389/fendo.2018.00601, doi:10.3389/fendo.2018.00601. This article has 88 citations.

23. (zhu2024igfbp5affectscardiomyocyte pages 1-2): Qingqing Zhu, Xinyi Lu, Mengli Chen, Ting Zhang, Mengsha Shi, Wenming Yao, Haifeng Zhang, Rongrong Gao, Xinli Li, Yanli Zhou, and Shengen Liao. Igfbp5 affects cardiomyocyte survival and functional recovery in mice following myocardial ischemia. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07304-0, doi:10.1038/s42003-024-07304-0. This article has 7 citations and is from a peer-reviewed journal.

24. (zhu2024igfbp5affectscardiomyocyte pages 6-6): Qingqing Zhu, Xinyi Lu, Mengli Chen, Ting Zhang, Mengsha Shi, Wenming Yao, Haifeng Zhang, Rongrong Gao, Xinli Li, Yanli Zhou, and Shengen Liao. Igfbp5 affects cardiomyocyte survival and functional recovery in mice following myocardial ischemia. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07304-0, doi:10.1038/s42003-024-07304-0. This article has 7 citations and is from a peer-reviewed journal.

25. (zhu2024igfbp5affectscardiomyocyte pages 10-11): Qingqing Zhu, Xinyi Lu, Mengli Chen, Ting Zhang, Mengsha Shi, Wenming Yao, Haifeng Zhang, Rongrong Gao, Xinli Li, Yanli Zhou, and Shengen Liao. Igfbp5 affects cardiomyocyte survival and functional recovery in mice following myocardial ischemia. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07304-0, doi:10.1038/s42003-024-07304-0. This article has 7 citations and is from a peer-reviewed journal.

26. (duan2020insulinlikegrowthfactor media 295916b3): Cunming Duan and John B. Allard. Insulin-like growth factor binding protein-5 in physiology and disease. Frontiers in Endocrinology, Mar 2020. URL: https://doi.org/10.3389/fendo.2020.00100, doi:10.3389/fendo.2020.00100. This article has 122 citations.

27. (duan2020insulinlikegrowthfactor pages 5-7): Cunming Duan and John B. Allard. Insulin-like growth factor binding protein-5 in physiology and disease. Frontiers in Endocrinology, Mar 2020. URL: https://doi.org/10.3389/fendo.2020.00100, doi:10.3389/fendo.2020.00100. This article has 122 citations.

28. (kim2007inductionofcellular pages 2-3): Kwang Seok Kim, Young Bae Seu, Suk-Hwan Baek, Mi Jin Kim, Keuk Jun Kim, Jung Hye Kim, and Jae-Ryong Kim. Induction of cellular senescence by insulin-like growth factor binding protein-5 through a p53-dependent mechanism. Molecular biology of the cell, 18 11:4543-52, Nov 2007. URL: https://doi.org/10.1091/mbc.e07-03-0280, doi:10.1091/mbc.e07-03-0280. This article has 255 citations and is from a domain leading peer-reviewed journal.

29. (kim2007inductionofcellular pages 3-4): Kwang Seok Kim, Young Bae Seu, Suk-Hwan Baek, Mi Jin Kim, Keuk Jun Kim, Jung Hye Kim, and Jae-Ryong Kim. Induction of cellular senescence by insulin-like growth factor binding protein-5 through a p53-dependent mechanism. Molecular biology of the cell, 18 11:4543-52, Nov 2007. URL: https://doi.org/10.1091/mbc.e07-03-0280, doi:10.1091/mbc.e07-03-0280. This article has 255 citations and is from a domain leading peer-reviewed journal.

30. (duan2024expressionofinsulinlike pages 9-10): Yinan Duan, Yifei Chen, Yan He, Runqi Gong, and Zhijun Xia. Expression of insulin-like growth factor binding protein 5 in the vaginal wall tissues of older women with pelvic organ prolapse. Aug 2024. URL: https://doi.org/10.1038/s41598-024-69098-9, doi:10.1038/s41598-024-69098-9. This article has 7 citations and is from a peer-reviewed journal.

31. (duan2024expressionofinsulinlike pages 4-6): Yinan Duan, Yifei Chen, Yan He, Runqi Gong, and Zhijun Xia. Expression of insulin-like growth factor binding protein 5 in the vaginal wall tissues of older women with pelvic organ prolapse. Aug 2024. URL: https://doi.org/10.1038/s41598-024-69098-9, doi:10.1038/s41598-024-69098-9. This article has 7 citations and is from a peer-reviewed journal.

32. (mancarella2024extracellularinteractorsof pages 3-5): Caterina Mancarella, Andrea Morrione, and Katia Scotlandi. Extracellular interactors of the igf system: impact on cancer hallmarks and therapeutic approaches. International Journal of Molecular Sciences, 25:5915, May 2024. URL: https://doi.org/10.3390/ijms25115915, doi:10.3390/ijms25115915. This article has 7 citations.

33. (duan2024expressionofinsulinlike pages 1-2): Yinan Duan, Yifei Chen, Yan He, Runqi Gong, and Zhijun Xia. Expression of insulin-like growth factor binding protein 5 in the vaginal wall tissues of older women with pelvic organ prolapse. Aug 2024. URL: https://doi.org/10.1038/s41598-024-69098-9, doi:10.1038/s41598-024-69098-9. This article has 7 citations and is from a peer-reviewed journal.

34. (nimptsch2024pregnancyassociatedplasma pages 1-2): Katharina Nimptsch, Elif Ece Aydin, Rafael Francisco Rios Chavarria, Jürgen Janke, Matthew N. Poy, Claus Oxvig, Astrid Steinbrecher, and Tobias Pischon. Pregnancy associated plasma protein-a2 (papp-a2) and stanniocalcin-2 (stc2) but not papp-a are associated with circulating total igf-1 in a human adult population. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52074-8, doi:10.1038/s41598-024-52074-8. This article has 4 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](IGFBP5-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000020 I have extracted Figure 2 from page 4, which illustrates the proposed modes of IGFBP-5 actions across four panels: (A) the IGF:IGFB](IGFBP5-deep-research-falcon_artifacts/image-1.png)

## Citations

1. beattie2006insulinlikegrowthfactorbinding pages 2-4
2. baxter2023signalingpathwaysof pages 2-3
3. duan2020insulinlikegrowthfactor pages 2-3
4. duan2020insulinlikegrowthfactor pages 3-5
5. sechrist2025pathologicsignalingand pages 2-4
6. baxter2023signalingpathwaysof pages 5-6
7. nimptsch2024pregnancyassociatedplasma pages 6-7
8. duan2020insulinlikegrowthfactor pages 7-8
9. firth2002cellularactionsof pages 15-16
10. baxter2023signalingpathwaysof pages 10-11
11. nimptsch2024pregnancyassociatedplasma pages 5-6
12. nimptsch2024pregnancyassociatedplasma pages 3-4
13. nimptsch2024pregnancyassociatedplasma pages 4-5
14. nimptsch2024pregnancyassociatedplasma pages 2-3
15. duan2020insulinlikegrowthfactor pages 5-7
16. kim2007inductionofcellular pages 2-3
17. kim2007inductionofcellular pages 3-4
18. duan2024expressionofinsulinlike pages 9-10
19. duan2024expressionofinsulinlike pages 4-6
20. mancarella2024extracellularinteractorsof pages 3-5
21. duan2024expressionofinsulinlike pages 1-2
22. nimptsch2024pregnancyassociatedplasma pages 1-2
23. Baxter, *Endocrine Reviews*
24. Duan & Allard, *Frontiers in Endocrinology*
25. Duan & Allard
26. Sureshbabu et al., *Journal of Cell Science*
27. Bach, *Journal of Molecular Endocrinology*
28. Nimptsch et al., *Scientific Reports*
29. Nguyen et al., *Frontiers in Endocrinology*
30. Zhu et al., *Communications Biology*
31. March 2020 IGFBP-5 review
32. Sureshbabu et al., *Journal of Cell Science*, April 2012
33. Duan and Allard, March 2020
34. Baxter, *Endocrine Reviews*, March 2023
35. Nguyen et al., *Frontiers in Endocrinology*, October 2018
36. Kim et al., *Molecular Biology of the Cell*, November 2007
37. March 2023 review
38. January 2024 cross-sectional study
39. August 2024 pelvic-organ-prolapse tissue work
40. November 2024 mouse myocardial-infarction experiments
41. Baxter, March 2023
42. Mancarella et al., May 2024
43. https://doi.org/10.1210/endrev/bnad008
44. https://doi.org/10.3389/fendo.2020.00100
45. https://doi.org/10.1242/jcs.092882
46. https://doi.org/10.1530/JME-17-0254
47. https://doi.org/10.1038/s41598-024-52074-8
48. https://doi.org/10.3389/fendo.2018.00601
49. https://doi.org/10.1038/s42003-024-07304-0
50. https://doi.org/10.1091/mbc.e07-03-0280
51. https://doi.org/10.1038/s41598-024-69098-9
52. https://doi.org/10.3390/ijms25115915
53. https://doi.org/10.1042/bj20060086,
54. https://doi.org/10.1210/endrev/bnad008,
55. https://doi.org/10.3389/fendo.2020.00100,
56. https://doi.org/10.3390/ijms262110248,
57. https://doi.org/10.1242/jcs.092882,
58. https://doi.org/10.1038/s41598-024-52074-8,
59. https://doi.org/10.1038/s42003-024-07304-0,
60. https://doi.org/10.1530/jme-17-0254,
61. https://doi.org/10.1210/er.2001-0033,
62. https://doi.org/10.3389/fendo.2018.00601,
63. https://doi.org/10.1091/mbc.e07-03-0280,
64. https://doi.org/10.1038/s41598-024-69098-9,
65. https://doi.org/10.3390/ijms25115915,