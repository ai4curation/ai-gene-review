---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T04:07:03.578423'
end_time: '2026-09-25T04:19:20.242025'
duration_seconds: 736.66
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
citation_count: 37
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

# PIK3CA (human PI3Kα/p110α): Functional-annotation research report

## Executive conclusion

The requested target is unambiguous. **Human PIK3CA encodes the 1,068-amino-acid p110α catalytic subunit of class IA phosphoinositide 3-kinase (PI3Kα), corresponding to UniProt P42336.** The names, size, class, and architecture reported in the literature match the supplied UniProt description; no conflicting gene or nonhuman protein was encountered. Its principal physiological function is membrane-localized lipid phosphorylation:

**ATP + phosphatidylinositol-4,5-bisphosphate [PI(4,5)P₂] → ADP + phosphatidylinositol-3,4,5-trisphosphate [PI(3,4,5)P₃].**

PIK3CA therefore acts as a spatially controlled signal-generating enzyme at the cytosolic surface of cellular membranes, principally the plasma membrane. It couples activated receptor tyrosine kinases (RTKs) and RAS to PIP₃-dependent recruitment of PDK1, AKT, and other PH-domain proteins. PTEN terminates this signal by dephosphorylating PIP₃ back to PIP₂. Oncogenic and developmental-disease variants commonly activate p110α by relieving p85-dependent autoinhibition, increasing membrane recruitment, or both. (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 1-2, sheng2024molecularbasisof pages 2-4)

| Topic | Current functional annotation/evidence | Key quantitative or translational implication |
|---|---|---|
| Verified identity | Human **PIK3CA**, UniProt **P42336**, encodes the **1,068-aa p110α catalytic subunit (PI3Kα)**; the literature identity matches the supplied UniProt record, with no gene or organism ambiguity. (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 2-4) | Establishes that the annotation concerns human p110α—not another PI3K isoform or organismal orthologue. |
| Family and architecture | A **class IA PI3K** catalytic subunit that forms an obligate signaling heterodimer with a p85-family regulatory subunit. Domains are the adaptor-binding domain (**ABD**), RAS-binding domain (**RBD**), membrane-binding **C2**, helical, and bilobal kinase domains. (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 2-4) | Domain interfaces explain p85-dependent inhibition, receptor/RAS activation, membrane binding, oncogenic hotspots, and drug sensitivity. |
| Primary reaction and substrate | At the cytosolic membrane surface, p110α transfers ATP’s γ-phosphate to the **D3 hydroxyl of phosphatidylinositol-4,5-bisphosphate**: **ATP + PI(4,5)P₂ → ADP + PI(3,4,5)P₃**. PI(4,5)P₂ is the principal physiological class-I lipid substrate. (sheng2024molecularbasisof pages 1-2, sheng2024molecularbasisof pages 2-4) | Defines p110α primarily as a lipid kinase. Reported Ser/Thr protein-kinase activity exists, but its physiological substrate scope is less certain. (rangwala2022kinasesondouble pages 5-7, sulaiman2023detectionofphosphorylation pages 26-30) |
| Regulation and localization | The p110α–p85 complex is largely cytosolic and autoinhibited. Activated RTK/adaptor **pYXXM** motifs bind p85 SH2 domains, releasing inhibitory contacts; **RAS-GTP** supplies an additional activating/recruitment input. Membrane engagement separates ABD from the catalytic core and C2 from p85 iSH2 and reorients the C terminus, exposing membrane-binding surfaces. (jenkins2023oncogenicmutationsof pages 1-2, jenkins2023oncogenicmutationsof pages 2-3, jenkins2023oncogenicmutationsof pages 7-8) | Catalysis is spatially restricted chiefly to the **cytosolic leaflet of the plasma membrane** near activated receptors and PI(4,5)P₂. |
| Pathway output and termination | PI(3,4,5)P₃ recruits PH-domain proteins, including PDK1 and AKT, initiating AKT–mTOR signaling that coordinates growth, survival, metabolism, and cell-cycle progression. **PTEN** terminates the signal by converting PI(3,4,5)P₃ back to PI(4,5)P₂. (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 1-2) | Places PIK3CA immediately between RTK/RAS inputs and the PIP₃–AKT–mTOR signaling module; p110α is particularly important downstream of insulin and growth-factor receptors. (sheng2024molecularbasisof pages 19-20) |
| Oncogenic mechanisms | Helical-domain **E542K/E545K** variants disrupt p85 nSH2-mediated inhibition; kinase-domain **H1047R** remodels the membrane-facing C terminus/WIF region and enhances membrane association. Mutations acting through different steps can occur **in cis** and synergistically increase activity. (jenkins2023oncogenicmutationsof pages 8-9, jenkins2023oncogenicmutationsof pages 2-3, sheng2024molecularbasisof pages 20-23) | Mechanistically distinct conformations support development of mutant-selective inhibitors; H1047R-selective binding has been demonstrated for investigational STX-478. (sheng2024molecularbasisof pages 19-20, sheng2024molecularbasisof pages 20-23) |
| Cancer prevalence | A 2024 review of approximately **80,000 tumors from 224 studies** reported PIK3CA mutations in **10.2%** of samples, of which **88%** were classified as drivers. Another 2024 synthesis reported **38.35%** in invasive breast carcinoma; rates vary substantially by tumor type and cohort. (sheng2024molecularbasisof pages 19-20, shan2024moleculartargetingof pages 4-6) | PIK3CA is a common actionable oncogene. In a 2023 breast-cancer cohort, mutations occurred in **278/728 patients (38%)**; H1047R, E545K, and E542K comprised 41.6%, 18.9%, and 10.3% of detected mutations, respectively. |
| Alpelisib in PROS | FDA accelerated approval was granted **5 April 2022** for patients aged ≥2 years with severe PIK3CA-related overgrowth spectrum requiring systemic therapy. In EPIK-P1, the safety and efficacy populations were **57** and **37** patients; confirmed Week-24 volumetric response was **27%** (95% CI 14–44), and **60%** of responders maintained response ≥12 months. Common reactions were diarrhea, stomatitis, and hyperglycemia. (singh2024fdaapprovalsummary pages 1-3, singh2024fdaapprovalsummary pages 4-6, singh2024fdaapprovalsummary pages 3-4) | Demonstrates genotype/pathway-directed treatment beyond cancer. In 2024, alpelisib improved all **25** patients with refractory PIK3CA- or TEK-related capillary-venous malformations; median six-month MRI volume reduction was **33.4%** for PIK3CA lesions. (zerbib2024targetedtherapyfor pages 1-3) |
| Inavolisib evidence, 2024 | Inavolisib selectively inhibits p110α and promotes degradation of mutant while relatively sparing wild-type p110α. In a phase I/Ib trial of PIK3CA-mutant HR-positive/HER2-negative advanced breast cancer, **53** patients received inavolisib, palbociclib, and letrozole (**n=33**) or fulvestrant (**n=20**). Confirmed response rates were **52%** and **40%**, and median progression-free survival was **23.3** and **35.0 months**, respectively. (jhaveri2024phaseiibtrial pages 1-2, jhaveri2024phaseiibtrial pages 2-4) | All patients experienced treatment-related adverse events; grade ≥3 rates were **87.9%** and **85.0%**. Frequent events included stomatitis, hyperglycemia, diarrhea, and neutropenia; treatment discontinuation due to toxicity occurred in **6.1%** and **10.0%**. (jhaveri2024phaseiibtrial pages 1-2, jhaveri2024phaseiibtrial pages 5-6) |


*Table: Compact evidence-based annotation of human PIK3CA/PI3Kα, spanning molecular identity, membrane-localized catalysis and regulation, oncogenic mechanisms, prevalence, and 2023–2024 translational evidence.*

## 1. Mandatory identity verification

### 1.1 Gene, protein, and organism

The symbol **PIK3CA** matches the supplied protein description: phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha, commonly called **p110α**, **PI3Kα**, or PI3K-alpha. It is a human class IA PI3K catalytic subunit rather than PIK3CB/p110β, PIK3CD/p110δ, or a nonhuman orthologue. The reviewed literature describes p110α as 1,068 amino acids and explicitly assigns it to PIK3CA. (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 2-4)

The domain architecture also aligns with the supplied InterPro annotations. From N to C terminus, p110α contains an **adaptor-binding domain (ABD)**, **RAS-binding domain (RBD)**, membrane-interacting **C2 domain**, **helical domain**, and bilobal **PI3/4-kinase catalytic domain**. The supplied ARM-type-fold annotation is compatible with helical/adaptor-interaction architecture, while the C2 and PI3/4-kinase annotations correspond directly to experimentally characterized structural regions. (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 2-4)

**Verification decision:** research can proceed on PIK3CA/P42336 with high confidence; there is no symbol ambiguity in this context.

## 2. Primary molecular function and substrate specificity

### 2.1 Physiological lipid-kinase reaction

Class I PI3Ks phosphorylate the D3 hydroxyl of the inositol headgroup. For p110α, the principal physiological membrane substrate is **PI(4,5)P₂**, and the phosphate donor is ATP. The products are **PI(3,4,5)P₃ and ADP**. This distinguishes class I PI3Ks from other PI3K classes with different phosphoinositide preferences. Recombinant p110 catalytic subunits can execute the reaction, but stable, properly regulated physiological signaling requires a regulatory adaptor and upstream inputs. (sheng2024molecularbasisof pages 1-2, sheng2024molecularbasisof pages 2-4)

Substrate recognition is inseparable from membrane association: PI(4,5)P₂ is embedded in the bilayer, so productive catalysis requires the catalytic core and membrane-facing motifs to assume an orientation that permits access to the lipid headgroup. HDX-MS and membrane-binding experiments show protection or rearrangement in the C2 domain, ABD–RBD linker, kinase N-lobe, activation loop, and C-terminal kinase region upon binding PIP₂-containing membranes. (jenkins2023oncogenicmutationsof pages 1-2, jenkins2023oncogenicmutationsof pages 4-6)

### 2.2 Reported protein-kinase activity

PI3Kα has also been assigned serine/threonine protein-kinase activity, including p110α-dependent phosphorylation of p85α Ser608. However, the physiological substrate spectrum and biological importance of this activity remain substantially less established than the lipid-kinase reaction. Functional annotation should therefore designate p110α primarily as a **phosphoinositide lipid kinase**, with protein-kinase activity treated as secondary and incompletely resolved. (rangwala2022kinasesondouble pages 5-7, sulaiman2023detectionofphosphorylation pages 26-30)

## 3. Complex assembly, regulation, and activation mechanism

### 3.1 The p110α–p85 class IA heterodimer

In cells, p110α forms a class IA PI3K heterodimer with a p85-family regulatory adaptor, commonly p85α. The ABD anchors p110α to the p85 inter-SH2 region. Multiple contacts involving p85 nSH2/iSH2 and the p110α C2, helical, kinase, and activation-loop regions hold the complex in a stable, inhibited cytosolic configuration. The regulatory subunit consequently performs two linked functions: it stabilizes p110α and prevents inappropriate catalysis while providing receptor-responsive recruitment machinery. (sheng2024molecularbasisof pages 19-20, sheng2024molecularbasisof pages 2-4, jenkins2023oncogenicmutationsof pages 2-3)

### 3.2 RTK and RAS inputs

Upon growth-factor or insulin-receptor signaling, p85 SH2 domains bind phosphorylated **pYXXM** motifs on activated receptors or receptor-associated adaptors. This competitively releases inhibitory SH2 contacts with p110α and changes the complex from a closed to a membrane-competent state. GTP-loaded RAS binds the p110α RBD and provides an additional membrane-recruitment and activation input. The relative contribution of RTK phosphopeptide and RAS inputs depends on cellular context. (jenkins2023oncogenicmutationsof pages 1-2, jenkins2023oncogenicmutationsof pages 7-8)

A mechanistic sequence supported by structural and biochemical studies is: pYXXM binding disengages p85 nSH2; this destabilizes ABD/p85 and C2/iSH2 inhibitory contacts; membrane-binding surfaces on the catalytic core become exposed; RAS can reinforce recruitment; and the p110α C terminus reorients into a catalytically competent membrane-facing configuration. (jenkins2023oncogenicmutationsof pages 1-2, jenkins2023oncogenicmutationsof pages 2-3, jenkins2023oncogenicmutationsof pages 7-8)

## 4. Cellular localization

PIK3CA is not a secreted, transmembrane, or constitutively membrane-embedded protein. The inhibited p110α–p85 complex is largely **cytosolic**, whereas catalysis occurs transiently at the **cytosolic leaflet of membranes**, predominantly the plasma membrane near activated receptors and PI(4,5)P₂. Thus, “cytosol-to-membrane recruitment” is a more accurate annotation than assigning p110α exclusively to either compartment. (sheng2024molecularbasisof pages 1-2, sheng2024molecularbasisof pages 2-4, jenkins2023oncogenicmutationsof pages 1-2)

Membrane localization is mechanistically causal rather than merely correlative. Engagement of lipid bilayers disengages the ABD from the catalytic core and the C2 domain from p85 iSH2, while repositioning the C-terminal WIF-containing membrane-interaction region. Oncogenic variants that increase membrane residence can therefore raise lipid phosphorylation even without proportionate changes in solution ATPase activity. (jenkins2023oncogenicmutationsof pages 1-2, jenkins2023oncogenicmutationsof pages 6-7, jenkins2023oncogenicmutationsof pages 4-6)

## 5. Signaling pathway and proximal biological processes

PI3Kα is positioned immediately downstream of RTKs, insulin-family receptors, and RAS. Its PIP₃ product creates a short-lived membrane docking signal for PH-domain proteins. PDK1 and AKT are recruited to this membrane environment, facilitating AKT activation and subsequent signaling to mTOR complexes, GSK3/cyclin machinery, metabolic regulators, and apoptosis-control proteins. The proximal functional outputs are therefore control of nutrient and growth-factor responses, glucose and anabolic metabolism, survival, proliferation, and growth. (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 19-20, sheng2024molecularbasisof pages 1-2)

**PTEN** is the direct biochemical antagonist: it removes the D3 phosphate from PIP₃ to regenerate PI(4,5)P₂. Signal amplitude and duration consequently reflect the local balance between PI3Kα and PTEN activities, not PIK3CA activity alone. Feedback through mTORC1/S6K and receptor pathways can further reshape the response, explaining why pathway inhibition often produces compensatory signaling. (rangwala2022kinasesondouble pages 5-7, sulaiman2023detectionofphosphorylation pages 26-30, sheng2024molecularbasisof pages 1-2)

Among class I isoforms, p110α is especially important downstream of insulin and many growth-factor RTKs and is broadly expressed. This helps explain both its essential normal metabolic functions and why systemic inhibition commonly causes hyperglycemia. (sheng2024molecularbasisof pages 19-20)

## 6. Pathogenic activation and structural evidence

### 6.1 Canonical hotspots

The best-characterized activating hotspots are helical-domain **E542K/E545K** and kinase-domain **H1047R**. E542K/E545K disrupt inhibitory contacts between the helical domain and p85 nSH2, partially reproducing receptor-phosphopeptide-mediated release of autoinhibition. H1047R instead changes the kinase-domain membrane-facing surface, disrupts inhibitory C-terminal packing, reorients the WIF region toward the bilayer, and increases membrane association. (jenkins2023oncogenicmutationsof pages 8-9, jenkins2023oncogenicmutationsof pages 2-3, jenkins2023oncogenicmutationsof pages 7-8)

These mechanisms are not interchangeable. Helical-domain mutants retain greater dependence on RAS for transformation, whereas H1047R can increase direct interactions with charged membrane lipids and support more RAS-independent transformation. C2/interface mutations such as N345K or E453Q disrupt p110α–p85 contacts, while E726K changes charge at a membrane-facing surface. (jenkins2023oncogenicmutationsof pages 7-8, sheng2024molecularbasisof pages 20-23)

### 6.2 2023 membrane-centric model

Jenkins and colleagues combined biochemical assays with HDX-MS in a January 2023 *Nature Communications* study. They found that H1047R, G1049R, and N1068 frameshift variants significantly increased membrane binding; H1047R and G1049R also increased basal ATPase activity, whereas N1068fs increased membrane recruitment without changing basal ATPase. M1043L primarily elevated basal ATPase with a smaller membrane effect. These results demonstrate that pathogenic variants can increase activity through distinct combinations of conformational opening, catalytic priming, and membrane residence. URL: https://doi.org/10.1038/s41467-023-35789-6. (jenkins2023oncogenicmutationsof pages 8-9, jenkins2023oncogenicmutationsof pages 6-7)

### 6.3 Double mutations

Multiple PIK3CA variants frequently occur in cis. Mechanistically distinct pairs can synergize because one mutation relieves p85 autoinhibition while another increases membrane binding or catalytic competence. Reported synergistic combinations include E726K/H1047R, E545K/E726K, E545K/M1043L, and E453Q/H1047R. This provides a structural explanation for increased signaling and, in some settings, enhanced sensitivity to PI3Kα inhibitors in multi-mutant tumors. (sheng2024molecularbasisof pages 20-23, zhang2021pi3kdrivermutations pages 3-4)

## 7. Disease associations and recent statistics

PIK3CA gain-of-function alterations occur in two major biological settings:

1. **Somatic tumor mutations**, often clonally selected and affecting helical- or kinase-domain hotspots.
2. **Post-zygotic mosaic mutations**, producing segmental overgrowth and vascular-malformation phenotypes collectively termed PIK3CA-related overgrowth spectrum (PROS).

Open Targets independently associates human PIK3CA with breast cancer, PROS, CLOVES syndrome, and megalencephaly-capillary malformation-polymicrogyria syndrome, consistent with the mechanistic and clinical literature. (OpenTargets Search: -PIK3CA)

A 2024 structural review analyzing approximately 80,000 tumors from 224 studies reported PIK3CA mutations in **10.2%** of samples, with **88%** classified as drivers. A separate 2024 synthesis reported frequencies of 38.35% in invasive breast carcinoma, 37.03% in cervical cancer, and 30.56% in colorectal cancer, although cross-study values depend strongly on cohort composition and assay. (sheng2024molecularbasisof pages 19-20, shan2024moleculartargetingof pages 4-6)

Recent breast-cancer data illustrate this variability. A 2023 Taiwanese NGS study found mutations in **278 of 728 patients (38%)**; among detected variants, H1047R accounted for 41.6%, E545K for 18.9%, and E542K for 10.3%. More broadly, PIK3CA mutations can occur in up to approximately half of ER-positive breast cancers, making mutation testing clinically actionable rather than merely prognostic. (shan2024moleculartargetingof pages 4-6)

## 8. Current applications and real-world implementation

### 8.1 Biomarker-directed breast-cancer therapy

PIK3CA mutation testing in tumor tissue or circulating tumor DNA is used to identify HR-positive/HER2-negative advanced breast cancers for PI3K-pathway-directed therapy. Alpelisib is a PI3Kα-selective inhibitor used with endocrine therapy in this setting. The need for combination treatment reflects pathway crosstalk: estrogen-receptor signaling, RTK feedback, and parallel survival pathways can blunt PI3Kα-inhibitor monotherapy. Hyperglycemia, rash, diarrhea, and stomatitis reflect both on-target metabolic effects and systemic pathway inhibition. (burke2023beyondpi3kstargeting pages 29-30, shan2024moleculartargetingof pages 4-6)

### 8.2 PROS: FDA-approved non-oncology application

The FDA granted accelerated approval to **alpelisib (VIJOICE) on 5 April 2022** for adults and children aged at least two years with severe PROS requiring systemic therapy. The 2024 FDA approval summary reported a 57-patient safety population and 37-patient efficacy population in EPIK-P1. Confirmed response at Week 24 required at least a 20% reduction in the summed volume of one to three measurable lesions, with no new or progressing lesions. The response rate was **27% (95% CI 14–44)**, and **60% of responders maintained response for at least 12 months**. Common adverse reactions were diarrhea, stomatitis, and hyperglycemia; serious adverse reactions occurred in 12%, but no patient permanently discontinued because of an adverse reaction. Published August 2024; URL: https://doi.org/10.1158/1078-0432.CCR-23-1270. (singh2024fdaapprovalsummary pages 1-3, singh2024fdaapprovalsummary pages 4-6, singh2024fdaapprovalsummary pages 3-4)

FDA reviewers considered the volumetric responses clinically meaningful because untreated PROS lesions generally do not regress and because narratives documented improvements in pain, swelling, bleeding, inflammatory flares, mobility, fatigue, and ocular function, including in some patients below the formal imaging threshold. They nevertheless required postmarketing work on long-term response, mutation/subtype differences, and pediatric growth and development. (singh2024fdaapprovalsummary pages 6-8)

### 8.3 Vascular malformations

A June 2024 translational study treated 25 patients with refractory capillary-venous malformations—16 PIK3CA-related and 9 TEK-related, including seven children. All improved clinically. At six months, median MRI lesion-volume reductions were **33.4% for PIK3CA-related** and **27.8% for TEK-related** malformations. A matched PIK3CA mouse model showed prevention of lesion formation, improvement of established lesions, and prolonged survival, strengthening the causal interpretation. URL: https://doi.org/10.1038/s41392-024-01862-9. (zerbib2024targetedtherapyfor pages 1-3)

## 9. Recent therapeutic development: inavolisib and mutant selectivity

Inavolisib is a potent selective PI3Kα inhibitor that also promotes degradation of mutant p110α while relatively sparing wild-type protein. This dual inhibition/degradation behavior is conceptually important because mutant-selective suppression could widen the therapeutic window over inhibitors that equally suppress essential wild-type PI3Kα. (jhaveri2024phaseiibtrial pages 1-2, jhaveri2024phaseiibtrial pages 2-4)

A November 2024 phase I/Ib study evaluated inavolisib with palbociclib and endocrine therapy in 53 women with PIK3CA-mutant, HR-positive/HER2-negative locally advanced or metastatic breast cancer. Thirty-three received letrozole and 20 received fulvestrant. Confirmed objective-response rates among patients with measurable disease were **52.0% and 40.0%**, while median progression-free survival was **23.3 and 35.0 months**, respectively. Clinical-benefit rates were 78.8% and 90.0%. Published in *Journal of Clinical Oncology*; URL: https://doi.org/10.1200/JCO.24.00110. (jhaveri2024phaseiibtrial pages 1-2, jhaveri2024phaseiibtrial pages 5-6)

Toxicity remained important: all patients had treatment-related adverse events; grade ≥3 rates were **87.9% and 85.0%**. Frequent events included stomatitis, hyperglycemia, diarrhea, and neutropenia. Discontinuation of any treatment because of treatment-related toxicity occurred in 6.1% and 10.0%. Because this was a small, nonrandomized phase I/Ib study, its efficacy estimates should be viewed as promising rather than definitive. (jhaveri2024phaseiibtrial pages 1-2, jhaveri2024phaseiibtrial pages 5-6)

The structural field is simultaneously moving toward mutation-selective allosteric inhibitors. The investigational compound STX-478 preferentially binds H1047R relative to wild-type or E545K p110α, supporting the expert view that mutation-specific conformations and membrane-engagement states may be exploitable. (sheng2024molecularbasisof pages 19-20, sheng2024molecularbasisof pages 20-23)

## 10. Expert interpretation and unresolved questions

The current consensus is that **PI3Kα activation is a membrane- and conformation-dependent process**, not simply an increase in intrinsic catalytic turnover. This explains why different PIK3CA variants with similar cellular signaling output can act through different molecular mechanisms and respond differently to mutant-selective compounds. The 2023 HDX-MS work and 2024 structural reviews argue for studying intact p110α–p85 complexes on realistic membranes rather than isolated catalytic domains alone. (sheng2024molecularbasisof pages 31-33, jenkins2023oncogenicmutationsof pages 8-9, jenkins2023oncogenicmutationsof pages 6-7)

Three limitations remain important:

- The physiological significance and substrate range of p110α’s reported protein-serine/threonine kinase activity remain unresolved; lipid phosphorylation is the confidently established primary function. (rangwala2022kinasesondouble pages 5-7, sulaiman2023detectionofphosphorylation pages 26-30)
- Wild-type p110α has essential insulin/metabolic functions, so nonselective or sustained inhibition predictably causes hyperglycemia and constrains dosing. (sheng2024molecularbasisof pages 19-20, singh2024fdaapprovalsummary pages 1-3)
- Mutation identity alone does not completely predict drug response because allelic configuration, co-mutations, PTEN status, endocrine signaling, RTK feedback, and tissue context modify pathway dependence. Multi-hit mutations may mark stronger PI3Kα dependence, but prospective validation remains necessary. (sheng2024molecularbasisof pages 20-23, zhang2021pi3kdrivermutations pages 3-4)

## Final functional annotation

**PIK3CA/P42336 encodes the human p110α catalytic subunit of class IA PI3K. In a p85-regulated heterodimer, it is recruited from the cytosol to the cytoplasmic face of receptor-activated membranes, where it uses ATP to phosphorylate PI(4,5)P₂ at the inositol D3 position, generating PI(3,4,5)P₃. PIP₃ recruits and activates the PDK1–AKT–mTOR signaling network, while PTEN reverses the lipid signal. The ABD, RBD, C2, helical, and kinase domains integrate p85, RTK, RAS, and membrane inputs. Pathogenic gain-of-function variants activate the enzyme chiefly by releasing p85 autoinhibition and/or increasing membrane engagement, causing cancer or mosaic overgrowth/vascular-malformation disease.** (rangwala2022kinasesondouble pages 5-7, sheng2024molecularbasisof pages 1-2, sheng2024molecularbasisof pages 2-4, jenkins2023oncogenicmutationsof pages 1-2)

References

1. (rangwala2022kinasesondouble pages 5-7): Aziz M. Rangwala, Victoria R. Mingione, George Georghiou, and Markus A. Seeliger. Kinases on double duty: a review of uniprotkb annotated bifunctionality within the kinome. Biomolecules, 12:685, May 2022. URL: https://doi.org/10.3390/biom12050685, doi:10.3390/biom12050685. This article has 3 citations.

2. (sheng2024molecularbasisof pages 1-2): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

3. (sheng2024molecularbasisof pages 2-4): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

4. (sulaiman2023detectionofphosphorylation pages 26-30): M Sulaiman. Detection of phosphorylation signatures specific to cancer-related pi3-kinase isoforms p110α and p110β. Unknown journal, 2023.

5. (jenkins2023oncogenicmutationsof pages 1-2): Meredith L. Jenkins, Harish Ranga-Prasad, Matthew A. H. Parson, Noah J. Harris, Manoj K. Rathinaswamy, and John E. Burke. Oncogenic mutations of pik3ca lead to increased membrane recruitment driven by reorientation of the abd, p85 and c-terminus. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35789-6, doi:10.1038/s41467-023-35789-6. This article has 68 citations and is from a highest quality peer-reviewed journal.

6. (jenkins2023oncogenicmutationsof pages 2-3): Meredith L. Jenkins, Harish Ranga-Prasad, Matthew A. H. Parson, Noah J. Harris, Manoj K. Rathinaswamy, and John E. Burke. Oncogenic mutations of pik3ca lead to increased membrane recruitment driven by reorientation of the abd, p85 and c-terminus. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35789-6, doi:10.1038/s41467-023-35789-6. This article has 68 citations and is from a highest quality peer-reviewed journal.

7. (jenkins2023oncogenicmutationsof pages 7-8): Meredith L. Jenkins, Harish Ranga-Prasad, Matthew A. H. Parson, Noah J. Harris, Manoj K. Rathinaswamy, and John E. Burke. Oncogenic mutations of pik3ca lead to increased membrane recruitment driven by reorientation of the abd, p85 and c-terminus. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35789-6, doi:10.1038/s41467-023-35789-6. This article has 68 citations and is from a highest quality peer-reviewed journal.

8. (sheng2024molecularbasisof pages 19-20): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

9. (jenkins2023oncogenicmutationsof pages 8-9): Meredith L. Jenkins, Harish Ranga-Prasad, Matthew A. H. Parson, Noah J. Harris, Manoj K. Rathinaswamy, and John E. Burke. Oncogenic mutations of pik3ca lead to increased membrane recruitment driven by reorientation of the abd, p85 and c-terminus. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35789-6, doi:10.1038/s41467-023-35789-6. This article has 68 citations and is from a highest quality peer-reviewed journal.

10. (sheng2024molecularbasisof pages 20-23): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

11. (shan2024moleculartargetingof pages 4-6): Khine S. Shan, Amalia Bonano-Rios, Nyein Wint Yee Theik, Atif Hussein, and Marcelo Blaya. Molecular targeting of the phosphoinositide-3-protein kinase (pi3k) pathway across various cancers. International Journal of Molecular Sciences, 25:1973, Feb 2024. URL: https://doi.org/10.3390/ijms25041973, doi:10.3390/ijms25041973. This article has 35 citations.

12. (singh2024fdaapprovalsummary pages 1-3): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

13. (singh2024fdaapprovalsummary pages 4-6): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

14. (singh2024fdaapprovalsummary pages 3-4): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

15. (zerbib2024targetedtherapyfor pages 1-3): Lola Zerbib, Sophia Ladraa, Antoine Fraissenon, Charles Bayard, Marina Firpion, Quitterie Venot, Sanela Protic, Clément Hoguin, Amandine Thomas, Sylvie Fraitag, Jean-Paul Duong, Sophie Kaltenbach, Estelle Balducci, Coline Lefevre, Patrick Villarese, Vahid Asnafi, Christine Broissand, Nicolas Goudin, Ivan Nemazanyy, Gwennhael Autret, Bertrand Tavitian, Christophe Legendre, Nadia Arzouk, Veronique Minard-Colin, Caroline Chopinet, Michael Dussiot, Denise M. Adams, Tristan Mirault, Laurent Guibaud, Paul Isenring, and Guillaume Canaud. Targeted therapy for capillary-venous malformations. Signal Transduction and Targeted Therapy, Jun 2024. URL: https://doi.org/10.1038/s41392-024-01862-9, doi:10.1038/s41392-024-01862-9. This article has 46 citations and is from a peer-reviewed journal.

16. (jhaveri2024phaseiibtrial pages 1-2): Komal L. Jhaveri, Melissa K. Accordino, Philippe L. Bedard, Andrés Cervantes, Valentina Gambardella, Erika Hamilton, Antoine Italiano, Kevin Kalinsky, Ian E. Krop, Mafalda Oliveira, Peter Schmid, Cristina Saura, Nicholas C. Turner, Andrea Varga, Sravanthi Cheeti, Stephanie Hilz, Katherine E. Hutchinson, Yanling Jin, Stephanie Royer-Joo, Ubong Peters, Noopur Shankar, Jennifer L. Schutzman, and Dejan Juric. Phase i/ib trial of inavolisib plus palbociclib and endocrine therapy for <i>pik3ca</i> -mutated, hormone receptor–positive, human epidermal growth factor receptor 2–negative advanced or metastatic breast cancer. Journal of Clinical Oncology, 42:3947-3956, Nov 2024. URL: https://doi.org/10.1200/jco.24.00110, doi:10.1200/jco.24.00110. This article has 46 citations and is from a highest quality peer-reviewed journal.

17. (jhaveri2024phaseiibtrial pages 2-4): Komal L. Jhaveri, Melissa K. Accordino, Philippe L. Bedard, Andrés Cervantes, Valentina Gambardella, Erika Hamilton, Antoine Italiano, Kevin Kalinsky, Ian E. Krop, Mafalda Oliveira, Peter Schmid, Cristina Saura, Nicholas C. Turner, Andrea Varga, Sravanthi Cheeti, Stephanie Hilz, Katherine E. Hutchinson, Yanling Jin, Stephanie Royer-Joo, Ubong Peters, Noopur Shankar, Jennifer L. Schutzman, and Dejan Juric. Phase i/ib trial of inavolisib plus palbociclib and endocrine therapy for <i>pik3ca</i> -mutated, hormone receptor–positive, human epidermal growth factor receptor 2–negative advanced or metastatic breast cancer. Journal of Clinical Oncology, 42:3947-3956, Nov 2024. URL: https://doi.org/10.1200/jco.24.00110, doi:10.1200/jco.24.00110. This article has 46 citations and is from a highest quality peer-reviewed journal.

18. (jhaveri2024phaseiibtrial pages 5-6): Komal L. Jhaveri, Melissa K. Accordino, Philippe L. Bedard, Andrés Cervantes, Valentina Gambardella, Erika Hamilton, Antoine Italiano, Kevin Kalinsky, Ian E. Krop, Mafalda Oliveira, Peter Schmid, Cristina Saura, Nicholas C. Turner, Andrea Varga, Sravanthi Cheeti, Stephanie Hilz, Katherine E. Hutchinson, Yanling Jin, Stephanie Royer-Joo, Ubong Peters, Noopur Shankar, Jennifer L. Schutzman, and Dejan Juric. Phase i/ib trial of inavolisib plus palbociclib and endocrine therapy for <i>pik3ca</i> -mutated, hormone receptor–positive, human epidermal growth factor receptor 2–negative advanced or metastatic breast cancer. Journal of Clinical Oncology, 42:3947-3956, Nov 2024. URL: https://doi.org/10.1200/jco.24.00110, doi:10.1200/jco.24.00110. This article has 46 citations and is from a highest quality peer-reviewed journal.

19. (jenkins2023oncogenicmutationsof pages 4-6): Meredith L. Jenkins, Harish Ranga-Prasad, Matthew A. H. Parson, Noah J. Harris, Manoj K. Rathinaswamy, and John E. Burke. Oncogenic mutations of pik3ca lead to increased membrane recruitment driven by reorientation of the abd, p85 and c-terminus. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35789-6, doi:10.1038/s41467-023-35789-6. This article has 68 citations and is from a highest quality peer-reviewed journal.

20. (jenkins2023oncogenicmutationsof pages 6-7): Meredith L. Jenkins, Harish Ranga-Prasad, Matthew A. H. Parson, Noah J. Harris, Manoj K. Rathinaswamy, and John E. Burke. Oncogenic mutations of pik3ca lead to increased membrane recruitment driven by reorientation of the abd, p85 and c-terminus. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35789-6, doi:10.1038/s41467-023-35789-6. This article has 68 citations and is from a highest quality peer-reviewed journal.

21. (zhang2021pi3kdrivermutations pages 3-4): Mingzhen Zhang, Hyunbum Jang, and Ruth Nussinov. Pi3k driver mutations: a biophysical membrane-centric perspective. Cancer Research, 81:237-247, Jan 2021. URL: https://doi.org/10.1158/0008-5472.can-20-0911, doi:10.1158/0008-5472.can-20-0911. This article has 49 citations and is from a highest quality peer-reviewed journal.

22. (OpenTargets Search: -PIK3CA): Open Targets Query (-PIK3CA, 21 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

23. (burke2023beyondpi3kstargeting pages 29-30): John E Burke, Joanna Catherine Caprio Triscott, Brooke M Emerling, and Gerald R V Hammond. Beyond pi3ks: targeting phosphoinositide kinases in disease. Nature Reviews. Drug Discovery, 22:357-386, Nov 2023. URL: https://doi.org/10.1038/s41573-022-00582-5, doi:10.1038/s41573-022-00582-5. This article has 189 citations.

24. (singh2024fdaapprovalsummary pages 6-8): Sonia Singh, Diana Bradford, Xiaoxue Li, Pallavi S. Mishra-Kalyani, Yuan-Li Shen, Lingshan Wang, Hong Zhao, Ye Xiong, Jiang Liu, Rosane Charlab, Jeffrey Kraft, Sachia Khasar, Claudia P. Miller, Donna R. Rivera, Paul G. Kluetz, Richard Pazdur, Julia A. Beaver, Harpreet Singh, and Martha Donoghue. Fda approval summary: alpelisib for pik3ca-related overgrowth spectrum (pros). Clinical cancer research : an official journal of the American Association for Cancer Research, 30:23-28, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1270, doi:10.1158/1078-0432.ccr-23-1270. This article has 72 citations.

25. (sheng2024molecularbasisof pages 31-33): Zhi Sheng, Patrick Beck, Maegan Gabby, Semhar Habte-Mariam, and Katherine Mitkos. Molecular basis of oncogenic pi3k proteins. Cancers, 17:77, Dec 2024. URL: https://doi.org/10.3390/cancers17010077, doi:10.3390/cancers17010077. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](PIK3CA-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. sheng2024molecularbasisof pages 19-20
2. zerbib2024targetedtherapyfor pages 1-3
3. shan2024moleculartargetingof pages 4-6
4. singh2024fdaapprovalsummary pages 6-8
5. rangwala2022kinasesondouble pages 5-7
6. sheng2024molecularbasisof pages 1-2
7. sheng2024molecularbasisof pages 2-4
8. sulaiman2023detectionofphosphorylation pages 26-30
9. jenkins2023oncogenicmutationsof pages 1-2
10. jenkins2023oncogenicmutationsof pages 2-3
11. jenkins2023oncogenicmutationsof pages 7-8
12. jenkins2023oncogenicmutationsof pages 8-9
13. sheng2024molecularbasisof pages 20-23
14. singh2024fdaapprovalsummary pages 1-3
15. singh2024fdaapprovalsummary pages 4-6
16. singh2024fdaapprovalsummary pages 3-4
17. jhaveri2024phaseiibtrial pages 1-2
18. jhaveri2024phaseiibtrial pages 2-4
19. jhaveri2024phaseiibtrial pages 5-6
20. jenkins2023oncogenicmutationsof pages 4-6
21. jenkins2023oncogenicmutationsof pages 6-7
22. sheng2024molecularbasisof pages 31-33
23. PI(4,5)P₂
24. PI(3,4,5)P₃
25. https://doi.org/10.1038/s41467-023-35789-6.
26. https://doi.org/10.1158/1078-0432.CCR-23-1270.
27. https://doi.org/10.1038/s41392-024-01862-9.
28. https://doi.org/10.1200/JCO.24.00110.
29. https://doi.org/10.3390/biom12050685,
30. https://doi.org/10.3390/cancers17010077,
31. https://doi.org/10.1038/s41467-023-35789-6,
32. https://doi.org/10.3390/ijms25041973,
33. https://doi.org/10.1158/1078-0432.ccr-23-1270,
34. https://doi.org/10.1038/s41392-024-01862-9,
35. https://doi.org/10.1200/jco.24.00110,
36. https://doi.org/10.1158/0008-5472.can-20-0911,
37. https://doi.org/10.1038/s41573-022-00582-5,