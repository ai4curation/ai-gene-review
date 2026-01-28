---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-22T17:51:23.489842'
end_time: '2026-01-22T18:08:54.040773'
duration_seconds: 1050.55
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: HSCB
  gene_symbol: HSCB
  uniprot_accession: Q8IWL3
  protein_description: 'RecName: Full=Iron-sulfur cluster co-chaperone protein HscB
    {ECO:0000305}; AltName: Full=DnaJ homolog subfamily C member 20; Contains: RecName:
    Full=Iron-sulfur cluster co-chaperone protein HscB, cytoplasmic; Short=C-HSC20
    {ECO:0000303|PubMed:29309586}; Contains: RecName: Full=Iron-sulfur cluster co-chaperone
    protein HscB, mitochondrial;'
  gene_info: Name=HSCB {ECO:0000312|HGNC:HGNC:28913}; Synonyms=DNAJC20, HSC20;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the HscB family. .
  protein_domains: HscB. (IPR004640); HscB_4_cys. (IPR040682); HscB_C_sf. (IPR036386);
    HscB_oligo_C. (IPR009073); J_dom_sf. (IPR036869)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 12
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8IWL3
- **Protein Description:** RecName: Full=Iron-sulfur cluster co-chaperone protein HscB {ECO:0000305}; AltName: Full=DnaJ homolog subfamily C member 20; Contains: RecName: Full=Iron-sulfur cluster co-chaperone protein HscB, cytoplasmic; Short=C-HSC20 {ECO:0000303|PubMed:29309586}; Contains: RecName: Full=Iron-sulfur cluster co-chaperone protein HscB, mitochondrial;
- **Gene Information:** Name=HSCB {ECO:0000312|HGNC:HGNC:28913}; Synonyms=DNAJC20, HSC20;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the HscB family. .
- **Key Domains:** HscB. (IPR004640); HscB_4_cys. (IPR040682); HscB_C_sf. (IPR036386); HscB_oligo_C. (IPR009073); J_dom_sf. (IPR036869)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HSCB" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HSCB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HSCB** (gene ID: HSCB, UniProt: Q8IWL3) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# HSCB (HSC20): Iron-Sulfur Cluster Co-chaperone Protein

## Introduction

HSCB, also known as HSC20 (Heat Shock Cognate protein 20) or DNAJC20, encodes a specialized J-type co-chaperone protein that plays an essential role in the biogenesis and transfer of iron-sulfur (Fe-S) clusters in human cells. Iron-sulfur clusters are among the most ancient and versatile cofactors in biology, essential for numerous cellular processes including mitochondrial respiration, DNA replication and repair, ribosome biogenesis, and the regulation of iron homeostasis [maio-2022-mammalian-fes-review-abstract]. The human HSCB protein is the ortholog of the bacterial HscB and yeast Jac1p proteins, which have long been recognized as crucial components of the conserved Fe-S cluster assembly machinery inherited from the proteobacterial ancestor of mitochondria [uhrigshardt-2010-hsc20-characterization-abstract].

The 235-amino acid HSCB protein functions primarily as a co-chaperone partner to HSPA9 (also known as mortalin or mtHSP70), the mitochondrial member of the Hsp70 chaperone family. Together, this chaperone/co-chaperone pair facilitates the transfer of nascent [2Fe-2S] clusters from the scaffold protein ISCU to a wide variety of recipient Fe-S proteins [uhrigshardt-2010-hsc20-characterization-abstract]. Remarkably, HSCB exists in both mitochondrial and cytosolic isoforms, enabling it to participate in Fe-S cluster biogenesis in multiple cellular compartments [kim-2018-cytosolic-hsc20-abstract]. The recent discovery that mutations in HSCB cause congenital sideroblastic anemia has underscored its critical importance in human physiology, particularly in erythropoiesis where Fe-S cluster-dependent enzymes are essential for heme biosynthesis [crispin-2020-hscb-sideroblastic-anemia-abstract]. Most recently, a 2024 study has revealed a novel Fe-S cluster-independent function of HSCB in regulating transcription factor localization during hematopoietic differentiation [liu-2024-pi3k-hscb-fog1-abstract].

## Molecular Function and Co-chaperone Activity

HSCB belongs to the DnaJ family of J-domain proteins, specifically classified as a type III J-protein due to its atypical structure compared to canonical DnaJ proteins [kampinga-2010-hsp70-jproteins-review-abstract]. The HSP70 chaperone machinery operates through a cycle driven by ATP binding and hydrolysis, with J-domain proteins serving as the primary determinants of functional specificity [kampinga-2010-hsp70-jproteins-review-abstract]. While humans possess only 11 HSP70 genes, they have 41 genes encoding J-domain proteins, illustrating how J-proteins enable the HSP70 machinery to perform diverse cellular functions. HSCB is distinguished from most other J-proteins by its specialized client protein binding domain, which has neither sequence nor structural similarity to the canonical DnaJ-type substrate binding domain [kampinga-2010-hsp70-jproteins-review-abstract].

The primary molecular function of HSCB is to stimulate the ATPase activity of HSPA9 in the context of Fe-S cluster transfer. The co-chaperone HSC20 initiates the functional cycle by associating with the scaffold protein ISCU when it is loaded with an Fe-S cluster, and simultaneously engages a recipient Fe-S apo-protein [maio-2022-mammalian-fes-review-abstract]. The J-domain of HSC20 contacts the nucleotide-binding domain (NBD) of ATP-bound HSPA9, while ISCU transiently interacts with the substrate-binding domain (SBD) of the chaperone. The simultaneous association of ISCU and the J-domain interaction with HSPA9 synergistically stimulates ATP hydrolysis nearly 1000-fold [maio-2022-mammalian-fes-review-abstract]. This dramatic enhancement of ATPase activity, coupled with conformational changes in the chaperone, is proposed to facilitate cluster release from ISCU and transfer to the recipient protein.

Importantly, NMR spectroscopy studies have revealed that HSC20 exhibits a distinct binding preference for the structured conformation of ISCU. The ISCU scaffold protein exists in equilibrium between two interconvertible states: a more structured state (S-state) and a partially disordered state (D-state), with approximately 28% of ISCU populating the S-state under physiological conditions [cai-2013-iscu-conformations-abstract]. While HSPA9 and the cysteine desulfurase NFS1 bind preferentially to the D-state (shifting the equilibrium away from the S-state), HSC20 uniquely binds to and stabilizes the S-state [cai-2013-iscu-conformations-abstract]. This finding suggests that the D-state serves as the substrate for cluster assembly by the cysteine desulfurase complex, while the S-state is the form recognized by the chaperone/co-chaperone system for cluster transfer, providing a potential mechanism for coordination between assembly and transfer steps.

## Protein Structure

The three-dimensional structure of human HscB has been determined by X-ray crystallography at 3.0 Å resolution [bitto-2008-hscb-structure-abstract]. The crystal structure (PDB ID: 3BVO) revealed an L-shaped protein architecture that is conserved with its bacterial homolog from E. coli. The protein consists of an N-terminal J-domain containing the characteristic His-Pro-Asp (HPD) signature motif essential for HSP70 interaction, connected by a short loop to a C-terminal domain folded into a compact three-helix bundle [uhrigshardt-2010-hsc20-characterization-abstract].

The most striking structural feature distinguishing human HscB from bacterial and fungal orthologs is an auxiliary metal-binding domain at the N-terminus [bitto-2008-hscb-structure-abstract]. This domain coordinates a metal ion (likely zinc) via a tetracysteine consensus motif with the sequence CWXCX(9-13)FCXXCXXXQ. Specifically, two CxxC modules (Cys41-Cys44 and Cys58-Cys61) form the metal-binding site, which is structurally similar to rubredoxin and several zinc finger proteins containing rubredoxin-like knuckles [bitto-2008-hscb-structure-abstract]. Normal mode analysis revealed that the L-shaped protein preferentially undergoes a scissors-like motion, which may be functionally important for its co-chaperone activity [bitto-2008-hscb-structure-abstract].

Comparative sequence analysis showed that this metal-coordinating CxxC motif is highly conserved in HSC20 proteins of higher eukaryotes and in corresponding proteins from anaerobic amitochondriates such as Giardia intestinalis and Trichomonas vaginalis, but is notably absent from fungal proteins [uhrigshardt-2010-hsc20-characterization-abstract]. Mutagenesis studies confirmed the functional importance of this domain: substitution of the four conserved cysteines with serines abolished HSC20 dimerization and disrupted its interactions with HSPA9, the CIA complex components, and Fe-S recipient proteins [kim-2018-cytosolic-hsc20-abstract]. The zinc-binding domain therefore stabilizes a dimeric form of HSC20 that is required for productive protein-protein interactions and also contributes to overall protein stability [uhrigshardt-2010-hsc20-characterization-abstract].

## Role in Iron-Sulfur Cluster Biogenesis

The general pathway of Fe-S cluster biogenesis in mammalian mitochondria begins with the mobilization of sulfane sulfur from cysteine by the cysteine desulfurase NFS1, which operates in a complex with ISD11/LYRM4 and NDUFAB1/ACP [maio-2022-mammalian-fes-review-abstract]. Frataxin (FXN) functions as an allosteric activator of this cysteine desulfurase complex. The sulfur and ferrous iron are combined on the ISCU scaffold protein to generate a nascent [2Fe-2S] cluster, which must then be transferred to recipient apoproteins. HSCB serves as the essential recognition and targeting component of the transfer machinery, guiding the chaperone system to specific Fe-S protein recipients.

A landmark discovery in understanding how HSCB recognizes its target proteins was the identification of the LYR motif as a molecular signature of Fe-S recipient proteins [maio-2014-lyr-motifs-abstract]. The tripeptide sequence L(I)YR is found in numerous Fe-S proteins and enables their recognition by HSC20, facilitating cluster acquisition from the ISCU scaffold. Succinate dehydrogenase B (SDHB), the iron-sulfur protein subunit of mitochondrial complex II, contains two conserved L(I)YR motifs that directly interact with HSC20 and are essential for the incorporation of its three Fe-S clusters [maio-2014-lyr-motifs-abstract]. The identification of a novel Complex II assembly intermediate (designated CIIb) containing the chaperone-cochaperone-ISCU transfer complex provided direct evidence for this mechanism in living cells [maio-2014-lyr-motifs-abstract].

The LYR motif recognition extends beyond direct Fe-S cluster recipients to include assembly factors that facilitate cluster insertion. SDHAF1, a Complex II assembly factor, uses its N-terminal LYR motif (L14Y15R16) to recruit the HSC20-HSPA9-ISCU transfer complex to SDHB [maio-2016-sdhaf1-fes-transfer-abstract]. SDHAF1 first binds to SDHB through an arginine-rich region in its C-terminus, creating a binding platform that then engages the Fe-S donor complex through its LYR motif interaction with HSC20. This sequential binding mechanism ensures proper Fe-S cluster incorporation during Complex II assembly. Pathogenic mutations in SDHAF1 that disrupt either SDHB binding or HSC20 interaction cause infantile leukoencephalopathy, demonstrating the critical importance of this assembly pathway [maio-2016-sdhaf1-fes-transfer-abstract].

## Role in Respiratory Chain Assembly

A pivotal 2017 study established that HSC20 serves as the central hub for Fe-S cluster delivery to the entire mitochondrial respiratory chain, encompassing Complexes I, II, and III [maio-2017-respiratory-complexes-abstract]. For Complex III assembly, the iron-sulfur cluster of the Rieske protein UQCRFS1 is essential for enzymatic activity. The co-chaperone HSC20 directly binds LYRM7, an assembly factor that stabilizes UQCRFS1 prior to its insertion into Complex III. A transient subcomplex composed of LYRM7 bound to UQCRFS1 interacts with the Fe-S transfer complex consisting of HSC20, HSPA9, and holo-ISCU [maio-2017-respiratory-complexes-abstract]. Binding of HSC20 to the LYR motif of LYRM7 in this pre-assembled intermediate facilitates Fe-S cluster transfer to UQCRFS1 in the mitochondrial matrix.

Importantly, all five Fe-S cluster subunits of Complex I were also shown to interact with HSC20 to acquire their clusters [maio-2017-respiratory-complexes-abstract]. This finding established HSC20 as the crucial organizing center for the assembly of multiple respiratory chain complexes, explaining the profound impact of HSC20 deficiency on mitochondrial respiration. The adaptability of the HSC20-HSPA9-ISCU transfer complex to serve multiple LYR motif-containing targets—whether direct Fe-S recipients or assembly factors—represents an elegant mechanism for coordinating the biogenesis of the mitochondrial electron transport chain.

The relationship between the HSPA9/HSC20 chaperone pair and the intermediate carrier protein glutaredoxin 5 (GLRX5) has revealed unexpected differences between human and bacterial Fe-S biogenesis systems. While in prokaryotes, the HscA/HscB chaperone pair facilitates cluster transfer from IscU to monothiol glutaredoxin, studies of the human system demonstrated that HSPA9/HSC20 actually inhibit cluster transfer from ISCU to GLRX5 while promoting the reverse transfer from GLRX5 to ISCU [olive-2018-hspa9-hsc20-glrx5-abstract]. This finding suggests that NFU1, rather than ISCU, may serve as the primary physiological donor of Fe-S clusters to GLRX5 in human cells, highlighting important mechanistic differences that have evolved in the mammalian Fe-S biogenesis pathway.

## Subcellular Localization

The mature HSCB protein contains an N-terminal mitochondrial targeting signal that directs the majority of the protein to the mitochondrial matrix, where the core Fe-S cluster assembly machinery resides [uhrigshardt-2010-hsc20-characterization-abstract]. Early studies using EGFP-hHSC20 fusion proteins in HeLa cells demonstrated predominantly mitochondrial localization, though small amounts were also detected outside mitochondria [uhrigshardt-2010-hsc20-characterization-abstract]. This observation proved prescient, as subsequent research established that a distinct cytosolic isoform of HSC20 (designated C-HSC20) plays important roles in cytosolic and nuclear Fe-S protein biogenesis.

The cytosolic HSC20 isoform integrates de novo Fe-S cluster biogenesis with the cytoplasmic iron-sulfur cluster assembly (CIA) machinery [kim-2018-cytosolic-hsc20-abstract]. In the cytoplasm, C-HSC20 mediates complex formation between components of the de novo Fe-S cluster biosynthesis pathway (ISCU1 and the cytosolic HSP70 chaperone HSPA8) and the CIA targeting complex (CIAO1, MMS19, and FAM96B). This targeting complex is responsible for delivering Fe-S clusters to a subset of cytosolic and nuclear proteins involved in DNA metabolism, including POLD1 (DNA polymerase delta), ELP3 (a component of the elongator complex), PPAT, and DPYD [kim-2018-cytosolic-hsc20-abstract]. The conserved LYR motif in CIAO1 mediates its binding to the C-terminal three-helix bundle of C-HSC20, establishing a direct physical connection between the early biosynthesis machinery and the late delivery complex.

## Clinical Relevance and Disease Associations

The essential role of HSCB in Fe-S cluster biogenesis makes it a candidate gene for mitochondrial diseases affecting iron metabolism. In 2020, biallelic mutations in HSCB were identified as the cause of congenital sideroblastic anemia type 5 (SIDBA5), establishing HSCB as a human disease gene [crispin-2020-hscb-sideroblastic-anemia-abstract]. The index patient, a 26-year-old woman, presented with hypochromic microcytic anemia detected at age 10 years. Genetic analysis revealed compound heterozygous mutations: a 1-bp duplication causing a frameshift (c.259dup; Thr87Asnfs*27) and a rare promoter variant (c.-134G>A) that reduced transcription [crispin-2020-hscb-sideroblastic-anemia-abstract]. Western blot analysis showed approximately 75% reduction in HSCB protein levels in patient fibroblasts.

The pathophysiology of HSCB deficiency reflects the broad importance of Fe-S clusters in cellular metabolism. HSCB knockdown in K562 erythroleukemia cells reduced expression of mitochondrial Fe-S cluster-containing enzymes including ferrochelatase (FECH), the terminal enzyme in heme biosynthesis, and mitochondrial aconitase (ACO2) [crispin-2020-hscb-sideroblastic-anemia-abstract]. Multiple respiratory complex proteins were also affected. Notably, HSCB knockdown impaired the lipoylation of E2 subunits of the pyruvate and α-ketoglutarate dehydrogenase complexes, because lipoic acid biosynthesis requires the Fe-S enzyme LIAS [crispin-2020-hscb-sideroblastic-anemia-abstract]. These defects resulted in reduced oxidative phosphorylation capacity and an attenuated cellular response to iron deficiency.

Animal model studies have confirmed the essential nature of HSCB in vivo. Homozygous loss of Hscb in mice is embryonic lethal, and erythroid-specific deletion of Hscb causes prenatal lethality due to severe anemia [crispin-2020-hscb-sideroblastic-anemia-abstract]. Circulating nucleated erythrocytes in these mice contained coarse iron granules resembling the ring sideroblasts characteristic of sideroblastic anemia. Pan-hematopoietic deletion of Hscb caused severe pancytopenia and bone marrow failure [crispin-2020-hscb-sideroblastic-anemia-abstract]. Morpholino knockdown of hscb in zebrafish similarly resulted in reduced erythrocyte numbers and decreased hemoglobinization, recapitulating key features of the human disease phenotype.

HSCB mutations join a growing list of Fe-S cluster biogenesis genes implicated in congenital sideroblastic anemia, including GLRX5 and HSPA9 [crispin-2020-hscb-sideroblastic-anemia-abstract]. The sideroblastic phenotype arises because ring sideroblasts form when iron accumulates in mitochondria due to impaired Fe-S cluster and heme synthesis. The ALAS2 mRNA, which encodes the erythroid-specific first enzyme of heme biosynthesis, contains an iron-responsive element (IRE) in its 5'-UTR that is regulated by Fe-S cluster-dependent iron regulatory proteins, creating an additional layer of dysregulation when Fe-S biogenesis is impaired.

Beyond sideroblastic anemia, the LYR motif recognition system connecting HSC20 to Fe-S cluster delivery has implications for cancer. Mutations in the L(I)YR motifs of SDHB, including I44, R46, L240, and R242, have been identified as cancer-associated mutations [maio-2014-lyr-motifs-abstract]. These residues are critical for HSC20 binding and Fe-S cluster acquisition, and their mutation leads to Complex II deficiency, succinate accumulation, and activation of hypoxia-inducible factor (HIF) signaling even under normoxic conditions—a phenomenon known as pseudohypoxia that drives tumorigenesis in SDH-deficient tumors.

## Novel Non-Canonical Function in Hematopoiesis

A significant 2024 study revealed an unexpected Fe-S cluster-independent function of HSCB in regulating transcription factor localization during hematopoietic differentiation [liu-2024-pi3k-hscb-fog1-abstract]. This research identified HSCB as an indispensable protein for the nuclear translocation of Friend of GATA 1 (FOG1) during erythropoiesis in K562 cells and cord-blood-derived human CD34+CD90+ hematopoietic stem cells, as well as during megakaryopoiesis.

Mechanistically, upon activation of EPO/EPOR or TPO/MPL signaling, HSCB is phosphorylated by phosphoinositol-3-kinase (PI3K) [liu-2024-pi3k-hscb-fog1-abstract]. This phosphorylation enables HSCB to bind to transforming acidic coiled-coil containing protein 3 (TACC3), which otherwise sequesters FOG1 in the cytoplasm. HSCB then mediates the proteasomal degradation of TACC3, thereby liberating FOG1 for nuclear entry where it can fulfill its role as a transcriptional co-regulator essential for erythroid and megakaryocyte development [liu-2024-pi3k-hscb-fog1-abstract].

This discovery has important therapeutic implications. Treatment with the TACC3 inhibitor KHS101 partially rescued erythropoiesis in HSCB-deficient cells, suggesting that targeting this pathway could provide therapeutic benefit in HSCB-related anemias [liu-2024-pi3k-hscb-fog1-abstract]. Importantly, this signaling function operates independently of HSCB's canonical role in Fe-S cluster delivery, revealing that HSCB has acquired additional cellular functions beyond its ancestral chaperone activity.

## Oxidative Stress and Protective Functions

A particularly noteworthy aspect of HSC20 function is its role in protecting cells from oxidative stress. Fe-S clusters are inherently susceptible to oxidative damage, and the recovery of inactivated Fe-S enzymes following oxidative insult was markedly delayed in HSC20-deficient cells [uhrigshardt-2010-hsc20-characterization-abstract]. Conversely, overexpression of hHSC20 substantially protected cells from oxidative damage. These observations suggest that HSC20 may act as a "pacemaker" regulating the efficiency of Fe-S cluster biogenesis, with its levels becoming rate-limiting particularly under conditions of oxidative stress when Fe-S cluster repair demand is elevated [uhrigshardt-2010-hsc20-characterization-abstract].

The oxidative stress sensitivity associated with HSC20 deficiency likely explains the particular vulnerability of erythroid cells, which experience high levels of reactive oxygen species generated during hemoglobin synthesis. This may contribute to the preferential manifestation of HSCB mutations as sideroblastic anemia rather than a more generalized mitochondrial disease.

## Open Questions

Several important questions remain regarding HSCB function and its role in human disease:

1. **Structural basis of LYR motif recognition**: While the importance of LYR motifs for HSC20 binding is established, higher-resolution structural information on the HSC20-LYR peptide complex would illuminate the molecular details of this recognition system and potentially enable prediction of novel HSC20 targets.

2. **Regulation of non-canonical functions**: How the PI3K-mediated phosphorylation of HSCB discovered in 2024 is coordinated with its canonical Fe-S cluster delivery function, and whether other signaling pathways similarly regulate HSCB activity, remain to be determined.

3. **Cytosolic versus mitochondrial isoform regulation**: How the relative expression and activity of mitochondrial and cytosolic HSC20 isoforms are regulated, and whether their dysfunction contributes differentially to disease, is unclear.

4. **Therapeutic strategies**: Whether upregulation of HSC20 expression could provide therapeutic benefit in Fe-S cluster deficiency disorders, or whether targeting TACC3 as suggested by Liu et al. [liu-2024-pi3k-hscb-fog1-abstract] offers a viable therapeutic approach for HSCB-related sideroblastic anemia.

5. **Complete spectrum of HSCB-dependent Fe-S proteins**: The full complement of proteins dependent on HSC20 for Fe-S cluster acquisition remains to be catalogued, particularly in the cytosolic and nuclear compartments.

6. **Role in cancer and aging**: Given the connections between Fe-S biogenesis, DNA repair, and genomic stability, whether HSC20 dysfunction contributes to cancer predisposition or aging phenotypes beyond the established SDH tumor suppressor pathway deserves exploration.

7. **Dynamics of the scissors-like motion**: How the conformational dynamics revealed by normal mode analysis of the crystal structure relate to the functional cycle of cluster transfer warrants further investigation using molecular dynamics simulations or time-resolved structural methods.

## References

1. **uhrigshardt-2010-hsc20-characterization**: Uhrigshardt H, Singh A, Kovtunovych G, Ghosh M, Rouault TA. Characterization of the human HSC20, an unusual DnaJ type III protein, involved in iron-sulfur cluster biogenesis. *Human Molecular Genetics*. 2010;19(19):3816-3834. PMID: 20668094; PMCID: PMC2935859; DOI: 10.1093/hmg/ddq301

2. **crispin-2020-hscb-sideroblastic-anemia**: Crispin A, Guo C, Chen C, et al. Mutations in the iron-sulfur cluster biogenesis protein HSCB cause congenital sideroblastic anemia. *The Journal of Clinical Investigation*. 2020;130(10):5245-5256. PMID: 32634119; PMCID: PMC7524500; DOI: 10.1172/JCI135479

3. **kim-2018-cytosolic-hsc20**: Kim KS, Maio N, Singh A, Rouault TA. Cytosolic HSC20 integrates de novo iron-sulfur cluster biogenesis with the CIAO1-mediated transfer to recipients. *Human Molecular Genetics*. 2018;27(5):837-852. PMID: 29309586; PMCID: PMC6075588; DOI: 10.1093/hmg/ddy004

4. **maio-2014-lyr-motifs**: Maio N, Singh A, Uhrigshardt H, Saxena N, Tong WH, Rouault TA. Cochaperone binding to LYR motifs confers specificity of iron sulfur cluster delivery. *Cell Metabolism*. 2014;19(3):445-457. PMID: 24606901; PMCID: PMC6550293; DOI: 10.1016/j.cmet.2014.01.015

5. **maio-2016-sdhaf1-fes-transfer**: Maio N, Ghezzi D, Verrigni D, et al. Disease-causing SDHAF1 mutations impair transfer of Fe-S clusters to SDHB. *Cell Metabolism*. 2016;23(2):292-302. PMID: 26749241; PMCID: PMC4749439; DOI: 10.1016/j.cmet.2015.12.005

6. **maio-2017-respiratory-complexes**: Maio N, Kim KS, Singh A, Rouault TA. A Single Adaptable Cochaperone-Scaffold Complex Delivers Nascent Iron-Sulfur Clusters to Mammalian Respiratory Chain Complexes I–III. *Cell Metabolism*. 2017;25(4):945-953.e6. PMID: 28380382; PMCID: PMC12285277; DOI: 10.1016/j.cmet.2017.03.010

7. **olive-2018-hspa9-hsc20-glrx5**: Olive JA, Cowan JA. Role of the HSPA9/HSC20 chaperone pair in promoting directional human iron-sulfur cluster exchange involving monothiol glutaredoxin 5. *Journal of Inorganic Biochemistry*. 2018;184:100-107. PMID: 29689452; PMCID: PMC5964037; DOI: 10.1016/j.jinorgbio.2018.04.007

8. **maio-2022-mammalian-fes-review**: Maio N, Rouault TA. Mammalian iron sulfur cluster biogenesis: From assembly to delivery to recipient proteins with a focus on novel targets of the chaperone and co-chaperone proteins. *IUBMB Life*. 2022;74(7):684-704. PMID: 35080107; PMCID: PMC10118776; DOI: 10.1002/iub.2593

9. **cai-2013-iscu-conformations**: Cai K, Frederick RO, Kim JH, Reinen NM, Tonelli M, Markley JL. Human mitochondrial chaperone (mtHSP70) and cysteine desulfurase (NFS1) bind preferentially to the disordered conformation, whereas co-chaperone (HSC20) binds to the structured conformation of the iron-sulfur cluster scaffold protein (ISCU). *Journal of Biological Chemistry*. 2013;288(40):28755-28770. PMID: 23940031; PMCID: PMC3789972; DOI: 10.1074/jbc.M113.482042

10. **kampinga-2010-hsp70-jproteins-review**: Kampinga HH, Craig EA. The HSP70 chaperone machinery: J proteins as drivers of functional specificity. *Nature Reviews Molecular Cell Biology*. 2010;11(8):579-592. PMID: 20651708; PMCID: PMC3003299; DOI: 10.1038/nrm2941

11. **bitto-2008-hscb-structure**: Bitto E, Bingman CA, Bitto E, Wesenberg GE, McCoy JG, Phillips GN Jr. Structure of human J-type co-chaperone HscB reveals a tetracysteine metal-binding domain. *Journal of Biological Chemistry*. 2008;283(44):30184-30192. PMID: 18713742; DOI: 10.1074/jbc.M804746200; PDB: 3BVO

12. **liu-2024-pi3k-hscb-fog1**: Liu G, Hou Y, Jin X, Zhang Y, Sun C, Huang C, Ren Y, Gao J, Wang X, Jiang X. PI3K/HSCB axis facilitates FOG1 nuclear translocation to promote erythropoiesis and megakaryopoiesis. *eLife*. 2024;13:e95815. PMID: 38757931; PMCID: PMC11101173; DOI: 10.7554/eLife.95815.3


## Citations

1. bitto-2008-hscb-structure-abstract.md
2. cai-2013-iscu-conformations-abstract.md
3. crispin-2020-hscb-sideroblastic-anemia-abstract.md
4. kampinga-2010-hsp70-jproteins-review-abstract.md
5. kim-2018-cytosolic-hsc20-abstract.md
6. liu-2024-pi3k-hscb-fog1-abstract.md
7. maio-2014-lyr-motifs-abstract.md
8. maio-2016-sdhaf1-fes-transfer-abstract.md
9. maio-2017-respiratory-complexes-abstract.md
10. maio-2022-mammalian-fes-review-abstract.md
11. olive-2018-hspa9-hsc20-glrx5-abstract.md
12. uhrigshardt-2010-hsc20-characterization-abstract.md