---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T03:29:14.838881'
end_time: '2026-05-11T03:59:39.133263'
duration_seconds: 1824.29
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

Research the human long non-coding RNA gene XIST (X-inactive specific transcript; RNAcentral URS000075D95B_9606) for Gene Ontology functional annotation. This is a lncRNA/non-coding RNA, not a protein; do not infer protein domains or enzyme activity. Focus on its core molecular function as a chromatin/RNA scaffold or chromatin-protein adaptor in X-chromosome inactivation, XIST coating of the inactive X, recruitment of silencing and chromatin-modifying complexes, heterochromatin formation, cellular localization, and which GO terms are directly supported by primary literature. Distinguish core X-inactivation function from broad dosage-compensation outcomes, and provide citations for each major claim.

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

Research the human long non-coding RNA gene XIST (X-inactive specific transcript; RNAcentral URS000075D95B_9606) for Gene Ontology functional annotation. This is a lncRNA/non-coding RNA, not a protein; do not infer protein domains or enzyme activity. Focus on its core molecular function as a chromatin/RNA scaffold or chromatin-protein adaptor in X-chromosome inactivation, XIST coating of the inactive X, recruitment of silencing and chromatin-modifying complexes, heterochromatin formation, cellular localization, and which GO terms are directly supported by primary literature. Distinguish core X-inactivation function from broad dosage-compensation outcomes, and provide citations for each major claim.

## Research report: Gene Ontology (GO) functional annotation evidence for human XIST lncRNA (RNAcentral: URS000075D95B_9606)

### Scope and constraints
This report summarizes primary-literature evidence that supports GO-style functional annotations for **XIST**, a **long non-coding RNA (lncRNA)** that orchestrates **X-chromosome inactivation (XCI)**. XIST is **not a protein**; therefore this report does **not** infer protein domains or enzymatic activities. Instead it focuses on XIST’s core molecular role as an **RNA/chromatin scaffold or adaptor** that (i) coats the inactive X in cis, (ii) recruits transcriptional repressors and chromatin-modifying complexes, (iii) helps establish repressive chromatin and higher-order chromosome organization, and (iv) localizes to defined nuclear compartments (Xi territory; nuclear lamina/nuclear matrix). Claims about **dosage compensation outcomes** are distinguished from the **core mechanistic functions**.

### Key concepts and current understanding (definitions)

#### X-chromosome inactivation (XCI)
XCI is a mammalian epigenetic program that transcriptionally silences most genes on one X chromosome in XX cells to balance X-linked gene dosage. XIST/Xist is required and is expressed from the future inactive X and spreads in cis to create a coated X territory where silencing and repressive chromatin accumulate (dror2024xistdirectlyregulates pages 1-3, valledor2023earlychromosomecondensation pages 1-3).

#### “Coating” and Xi territory formation
“Coating” refers to the accumulation of XIST RNA across the chromosome territory (often observed as an XIST “cloud”), which is necessary to spatially concentrate silencing factors and establish a repressive nuclear compartment (dror2024xistdirectlyregulates pages 1-3, valledor2023earlychromosomecondensation pages 1-3).

#### Modular scaffold/adaptor model
XIST engages many proteins through modular repeat regions and higher-order RNA folding. Large-scale structural and interaction mapping shows that XIST forms a modular ribonucleoprotein architecture with clustered protein-binding domains (lu2020structuralmodularityof pages 1-2, lu2020structuralmodularityof pages 6-7). Systematic interactome mapping identifies multiple direct Xist-binding proteins (including chromatin and nuclear-envelope factors), supporting its scaffold/adaptor role (minajigi2015acomprehensivexist pages 1-3).

### Core XIST molecular functions directly supported by primary literature

#### 1) Recruitment of SHARP/SPEN → SMRT/NCoR → HDAC3 to initiate transcriptional silencing and RNA Pol II exclusion
**Primary evidence:** McHugh et al. used RAP-MS to identify proteins that directly associate with Xist and showed that **SHARP (SPEN)** is among the direct interactors required for silencing; SHARP is required for **RNA polymerase II exclusion** from the Xist-coated territory, and **SMRT** and **HDAC3** are also required for silencing and Pol II exclusion (mchugh2015thexistlncrna pages 1-2, mchugh2015thexistlncrna pages 6-7). The paper’s mechanistic model links SHARP (a direct Xist-binding factor) to recruitment/activation of HDAC3 through SMRT, consistent with histone deacetylation-based transcriptional repression (mchugh2015thexistlncrna pages 6-7).

**Interpretation for GO annotation:** This supports GO molecular-function-style annotations centered on **protein binding** and **corepressor complex recruitment**, and GO biological-process annotations for **transcriptional gene silencing** and **RNA polymerase II exclusion from chromatin territory** (mchugh2015thexistlncrna pages 6-7, mchugh2015thexistlncrna pages 1-2).

#### 2) Polycomb recruitment via hnRNPK binding to Xist B-repeat/XR-PID and initiation of PRC1→PRC2 cascade
**Primary evidence:** Pintacuda et al. mapped an Xist **Polycomb Interaction Domain** (XR-PID; ~600 nt encompassing B-repeat), where deletion abrogates Polycomb recruitment and Xist-dependent chromosome silencing, and identified **hnRNPK** as the principal XR-PID binding factor needed to recruit **PCGF3/5-PRC1** (pintacuda2017hnrnpkrecruitspcgf35prc1 pages 1-3). They further showed **direct biochemical interaction** between hnRNPK and a recombinant PCGF3-PRC1 complex and demonstrated that **synthetic tethering of hnRNPK** to XR-PID–deleted Xist restores H2AK119ub and H3K27me3 accumulation over the Xist domain (pintacuda2017hnrnpkrecruitspcgf35prc1 pages 10-13).

**Interpretation for GO annotation:** These data directly support annotations for **Polycomb complex recruitment**, **H2A K119 ubiquitination involved in chromatin silencing**, and establishment of repressive chromatin states downstream of PRC1/PRC2 (pintacuda2017hnrnpkrecruitspcgf35prc1 pages 1-3, pintacuda2017hnrnpkrecruitspcgf35prc1 pages 10-13).

#### 3) Nuclear lamina tethering through LBR and functional impact on spreading to active genes
**Primary evidence:** Chen et al. report that Xist **directly interacts** with **lamin B receptor (LBR)** and that this interaction is required for Xist-mediated silencing by recruiting the inactive X to the **nuclear lamina**, enabling Xist to spread to actively transcribed genes across the X (chen2016xistrecruitsthe pages 1-2). The paper includes functional tests showing LBR perturbation disrupts silencing and lamina association, and that engineered tethering strategies can rescue spreading/silencing defects, consistent with a mechanistic role for lamina recruitment in chromosome-wide silencing (chen2016xistrecruitsthe pages 1-2, chen2016xistrecruitsthe pages 3-4).

**Important limitation / nuance:** A systematic allelic dissection of Xist pathways reported that **LBR makes only minor contributions** to gene silencing in the tested ESC models, suggesting redundancy or context-dependence of LBR-mediated effects across systems (nesterova2019systematicallelicanalysis pages 1-2).

**Interpretation for GO annotation:** Supports CC/BP annotations for **nuclear lamina association** and BP annotations linking XIST to chromosome-wide silencing through nuclear positioning/spreading mechanisms, while indicating potential context specificity (chen2016xistrecruitsthe pages 1-2, nesterova2019systematicallelicanalysis pages 1-2).

#### 4) Xist/XIST interactome evidence for nuclear-envelope/nuclear-matrix factors and chromosome conformation control
**Primary evidence:** Minajigi et al. developed iDRiP to identify a broad set of **direct Xist-interacting proteins**, including nuclear-envelope components (e.g., LBR) and nuclear matrix proteins (hnRPU/SAF-A, hnRNPK), and explored functional impacts on Xi repression and chromosome conformation (minajigi2015acomprehensivexist pages 1-3).

**Interpretation for GO annotation:** Supports MF/CC terms around **protein binding**, **nuclear matrix association**, and BP terms tied to **chromosome organization** and the assembly of a repressive chromosome territory (minajigi2015acomprehensivexist pages 1-3).

#### 5) Early heterochromatinization/compaction as a distinct, measurable process driven by XIST RNA density
**Primary evidence (2023):** Valledor et al. used inducible human XIST to show that XIST modifies chromosome territory architecture before widespread gene silencing, creating distinct **“sparse” and “dense” RNA zones** with different chromatin impacts; **H2AK119ub and CIZ1** appear rapidly, while **H3K27me3** appears later in the dense zone as condensation proceeds (valledor2023earlychromosomecondensation pages 1-3, valledor2023earlychromosomecondensation media 58d592e8). Critically, they report quantitative local gene silencing by the isolated A-repeat fragment: transcription foci for nearby genes dropped **~82% (DSCR3) and ~83% (TTC3)** upon induction, indicating strong local repression (valledor2023earlychromosomecondensation pages 10-11). Their data support a model where condensation builds a high-density RNA/DNA environment that facilitates an A-repeat/HDAC-dependent silencing step (valledor2023earlychromosomecondensation pages 1-3, valledor2023earlychromosomecondensation pages 10-11, valledor2023earlychromosomecondensation media 58d592e8).

**Interpretation for GO annotation:** Supports BP terms such as **heterochromatin formation**, **chromosome condensation/organization**, and chromatin-mark deposition timing consistent with Polycomb involvement (valledor2023earlychromosomecondensation pages 1-3, valledor2023earlychromosomecondensation media 58d592e8).

### Recent developments and latest research (prioritizing 2023–2024)

#### A) XIST localization states and non-canonical (dispersed) configurations in naïve human pluripotent cells (2024)
Dror et al. (Cell, publication date 2024-01-04; URL in record) report that in **naïve human pluripotent stem cells**, XIST shows a **dispersed nuclear configuration** and is associated with **X-chromosome dampening** rather than full silencing; they further report that XIST spreads across the X chromosome and can target specific autosomal regions with associated gene-expression dampening and repressive chromatin changes (dror2024xistdirectlyregulates pages 1-3). This expands the functional landscape of XIST localization beyond the classical compact Xi cloud, while still being consistent with scaffold/adaptor logic (dror2024xistdirectlyregulates pages 1-3).

#### B) Quantitative, time-resolved architecture-first model for initiation (2023)
Valledor et al. provide an explicit time ordering: rapid appearance of H2AK119ub/CIZ1 with early sparse RNA, later H3K27me3 coincident with dense zone expansion and condensation, and gene silencing after compaction (valledor2023earlychromosomecondensation pages 1-3, valledor2023earlychromosomecondensation media 58d592e8).

#### C) Translational and experimental “chromosome therapy” platforms using XIST transgenes (2024)
A 2024 Science Advances study established a dynamic trisomy 21 iPSC model where an inducible XIST transgene on chromosome 21 yields homogenous XIST clouds with H2AK119ub/H3K27me3 and near-complete repression of the targeted allele; importantly, repression remains efficient even after terminal differentiation, enabling post-developmental dosage-correction experiments (bansal2024adynamicin pages 1-3). A 2024 Human Genetics review synthesizes translational prospects/challenges and reports Down syndrome incidence in the US as **~1/750 live births** and chromosomal abnormalities collectively as **~1/150 newborns**, framing real-world motivations for XIST-based dosage correction research (gupta2024trisomysilencingby pages 1-3).

### Applications and real-world implementations

1. **In vitro dosage correction / disease modeling (Trisomy 21):** XIST transgene insertion on one chromosome 21 enables monoallelic chromosome-wide repression, providing a platform to dissect which phenotypes depend on ongoing trisomic dosage and which can be corrected later (bansal2024adynamicin pages 1-3).
2. **Translational roadmapping for chromosome dosage disorders:** The 2024 review outlines how XIST transgenics could inform future therapeutic strategies, while emphasizing major technical and biological hurdles for in vivo application (gupta2024trisomysilencingby pages 1-3).

### Expert opinions and authoritative synthesis (used cautiously)
Where reviews are used, they are treated as secondary synthesis rather than primary GO evidence. Loda & Heard (2019) provides a consolidated view of modular repeat functions and the landscape of interactors, consistent with the primary evidence that SPEN/SHARP–HDAC3 and hnRNPK–PRC1 are central pathways, and that LBR effects may be modest in some models (loda2019xistrnain pages 7-9, loda2019xistrnain pages 13-14).

### Statistics and quantitative findings from recent studies
- **Local repression by A-repeat alone:** transcription foci decreased **82% (DSCR3)** and **83% (TTC3)** upon A-repeat induction in a human iPSC transgene context, supporting strong local gene repression capacity when RNA density is high (valledor2023earlychromosomecondensation pages 10-11).
- **Down syndrome incidence:** ~**1/750** live births in the US (reviewed statistic) (gupta2024trisomysilencingby pages 1-3).
- **Chromosomal abnormalities overall:** ~**1/150** newborns (reviewed statistic) (gupta2024trisomysilencingby pages 1-3).

### GO-term mapping (candidate annotations supported by primary literature)
The following table summarizes candidate GO terms for XIST that are directly supported by the evidence assembled here.

| GO Category | Candidate GO Term | Concise Definition for XIST | Key Primary Evidence | Mechanistic Notes & Limitations | Citations |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Biological Process (BP)** | X-chromosome inactivation | Initiates cis-limited chromosome-wide gene silencing across the inactive X (Xi). | McHugh 2015 (RAP-MS & knockdown); Dror 2024 (naïve hPSC localization) | Core mechanism; functions as a cis-acting lncRNA scaffold. Dror 2024 shows trans-acting capabilities in early development. | (dror2024xistdirectlyregulates pages 1-3, mchugh2015thexistlncrna pages 1-2) |
| **Biological Process (BP)** | Dosage compensation by X inactivation | Equalizes expression of X-linked genes between male and female somatic cells. | Dror 2024, Gupta 2024, Bansal 2024 (iPSC models & transgene targeting) | Downstream biological outcome. Can also be repurposed for autosomal dosage correction (e.g., Trisomy 21). | (dror2024xistdirectlyregulates pages 1-3, gupta2024trisomysilencingby pages 1-3, bansal2024adynamicin pages 1-3) |
| **Molecular Function (MF)** | Protein binding / RNA binding | Scaffolds multiple interacting proteins via a folded, evolutionarily conserved modular architecture. | Minajigi 2015 (iDRiP-MS); Lu 2020 (PARIS, fRIP-seq, eCLIP) | Modularity specifies unique interaction zones for specific RBPs (e.g., A-repeat, B/C-repeats). | (lu2020structuralmodularityof pages 1-2, minajigi2015acomprehensivexist pages 1-3) |
| **Cellular Component (CC) / MF** | Chromatin binding / association | Coats the future inactive X chromosome to establish a repressive nuclear territory. | Valledor 2023 (RNA FISH & inducible XIST); Dror 2024 (CUT&Tag/RAP-seq) | Occurs in dense and sparse zones. In naïve hPSCs, XIST is highly dispersed rather than tightly compacted. | (dror2024xistdirectlyregulates pages 1-3, valledor2023earlychromosomecondensation pages 1-3) |
| **Biological Process (BP)** | Chromosome organization / Heterochromatin formation | Modifies cytoarchitecture and drives large-scale condensation of active chromatin into a Barr body. | Valledor 2023 (Inducible XIST time-course); Minajigi 2015 (Allele-specific ChIP-seq) | Early condensation builds RNA density required for sustained silencing. Involves cohesin repulsion and distinct topological remodeling. | (valledor2023earlychromosomecondensation pages 1-3, minajigi2015acomprehensivexist pages 6-8, valledor2023earlychromosomecondensation media 58d592e8) |
| **Biological Process (BP) / MF** | Recruitment of histone deacetylase complex | Recruits HDAC3 via direct binding to SHARP/SPEN to mediate transcriptional silencing. | McHugh 2015 (Knockdown of SHARP, SMRT, HDAC3) | Mediated by the A-repeat. Crucial for exclusion of RNA Pol II; acts rapidly at sites of high RNA density. | (mchugh2015thexistlncrna pages 4-6, mchugh2015thexistlncrna pages 6-7, mchugh2015thexistlncrna pages 1-2) |
| **Biological Process (BP) / MF** | Polycomb repressive complex recruitment | Initiates the Polycomb cascade by recruiting PCGF3/5-PRC1 via hnRNPK. | Pintacuda 2017 (XR-PID deletion & synthetic tethering); Nesterova 2019 (Allelic silencing) | Driven by XIST B/C repeats interacting with hnRNPK. PRC2 is recruited indirectly downstream of PRC1. | (pintacuda2017hnrnpkrecruitspcgf35prc1 pages 1-3, pintacuda2017hnrnpkrecruitspcgf35prc1 pages 10-13, nesterova2019systematicallelicanalysis pages 1-2) |
| **Biological Process (BP)** | Histone H2A K119 ubiquitination | PRC1-mediated deposition of repressive ubiquitin marks on H2A across the Xi territory. | Pintacuda 2017 (ImmunoFISH & Xist tethering); Valledor 2023 (Timing assays) | Appears early in the 'sparse' XIST zone concurrent with CIZ1 recruitment and preceding widespread gene silencing. | (valledor2023earlychromosomecondensation pages 1-3, pintacuda2017hnrnpkrecruitspcgf35prc1 pages 1-3, valledor2023earlychromosomecondensation media 58d592e8) |
| **Biological Process (BP)** | Histone H3K27 methylation enrichment | PRC2-mediated trimethylation of H3K27 to maintain and stabilize facultative heterochromatin. | Pintacuda 2017 (Tethering complementation); Valledor 2023 (Time-course) | Follows H2AK119ub deposition. Accumulates later in 'dense' RNA zones during chromosome condensation. | (valledor2023earlychromosomecondensation pages 1-3, pintacuda2017hnrnpkrecruitspcgf35prc1 pages 10-13, valledor2023earlychromosomecondensation media 58d592e8) |
| **Biological Process (BP) / CC** | Nuclear lamina tethering | Recruits the Xi to the nuclear lamina to facilitate spreading to active genes. | Chen 2016 (LBR knockdown, DLBS-Xist cells); Nesterova 2019 (Allelic analysis) | Interaction with Lamin B Receptor (LBR). Nesterova 2019 indicates LBR plays only a minor or redundant role in aggregate silencing. | (nesterova2019systematicallelicanalysis pages 1-2, chen2016xistrecruitsthe pages 1-2, chen2016xistrecruitsthe pages 3-4) |
| **Cellular Component (CC)** | Nuclear matrix association | Anchors XIST RNPs and Xi chromatin to the insoluble nuclear scaffold. | Minajigi 2015 (Interactome); Valledor 2023 (CIZ1 immunofluorescence) | Involves interactions with SAF-A (hnRNP U) and CIZ1. Recruited immediately alongside sparse XIST RNA. | (valledor2023earlychromosomecondensation pages 1-3, minajigi2015acomprehensivexist pages 1-3, valledor2023earlychromosomecondensation media 58d592e8) |
| **Cellular Component (CC)** | Nuclear localization to Xi territory | Highly concentrated accumulation in a specific sub-nuclear compartment (the Xist cloud). | Valledor 2023 (RNA FISH spatial mapping); Dror 2024 (Imaging) | Forms a biphasic structure ('dense' vs 'sparse' zones) essential for bridging architectural changes and local gene repression. | (dror2024xistdirectlyregulates pages 1-3, valledor2023earlychromosomecondensation pages 1-3, valledor2023earlychromosomecondensation media 58d592e8) |


*Table: This table maps specific Gene Ontology (GO) functional annotations for the human XIST lncRNA to their primary supporting literature and key mechanistic details.*

### Distinguishing core mechanism from downstream outcomes
- **Core XIST molecular functions (mechanistic GO focus):** cis coating/association with Xi territory; direct binding to SHARP/SPEN; recruitment/activation of SMRT/HDAC3 for histone deacetylation and Pol II exclusion; recruitment of hnRNPK to bring PCGF3/5-PRC1 and initiate Polycomb marking (H2AK119ub → PRC2/H3K27me3); nuclear lamina tethering via LBR enabling spreading to active genes; and driving chromosome condensation/organization (mchugh2015thexistlncrna pages 6-7, pintacuda2017hnrnpkrecruitspcgf35prc1 pages 10-13, chen2016xistrecruitsthe pages 1-2, valledor2023earlychromosomecondensation pages 1-3).
- **Downstream outcomes (should not be over-annotated as direct functions):** organismal dosage compensation, sex-biased traits, and disease phenotypes are emergent consequences of the above molecular functions and should be annotated as higher-level BP outcomes only with careful scoping (gupta2024trisomysilencingby pages 1-3, dror2024xistdirectlyregulates pages 1-3).

### Notes on evidence gaps and caution for GO annotation
- **Context dependence:** LBR/LBR-binding-site perturbations show strong effects in some systems (chen2016xistrecruitsthe pages 1-2) but only minor contributions in others (nesterova2019systematicallelicanalysis pages 1-2); GO annotations should reflect this as “contributes to” rather than strictly “essential for” across all contexts.
- **PRC2 recruitment:** McHugh et al. report PRC2 enrichment depends on SHARP/HDAC3 and note that PRC2 components were not robustly identified as direct Xist interactors by RAP-MS, supporting an **indirect** or downstream recruitment model (mchugh2015thexistlncrna pages 6-7).

### Key primary references (with URLs and publication dates)
- McHugh CA et al. **Nature** (Apr 2015). “The Xist lncRNA interacts directly with SHARP to silence transcription through HDAC3.” https://doi.org/10.1038/nature14443 (mchugh2015thexistlncrna pages 1-2, mchugh2015thexistlncrna pages 6-7)
- Minajigi A et al. **Science** (Jun 2015). “A comprehensive Xist interactome reveals cohesin repulsion and an RNA-directed chromosome conformation.” https://doi.org/10.1126/science.aab2276 (minajigi2015acomprehensivexist pages 1-3)
- Chen C-K et al. **Science** (Oct 2016). “Xist recruits the X chromosome to the nuclear lamina to enable chromosome-wide silencing.” https://doi.org/10.1126/science.aae0047 (chen2016xistrecruitsthe pages 1-2, chen2016xistrecruitsthe pages 3-4)
- Pintacuda G et al. **Molecular Cell** (Dec 2017). “hnRNPK Recruits PCGF3/5-PRC1 to the Xist RNA B-Repeat to Establish Polycomb-Mediated Chromosomal Silencing.” https://doi.org/10.1016/j.molcel.2017.11.013 (pintacuda2017hnrnpkrecruitspcgf35prc1 pages 1-3, pintacuda2017hnrnpkrecruitspcgf35prc1 pages 10-13)
- Nesterova TB et al. **Nature Communications** (Nov 2019). “Systematic allelic analysis defines the interplay of key pathways in X chromosome inactivation.” https://doi.org/10.1038/s41467-019-11171-3 (nesterova2019systematicallelicanalysis pages 1-2)
- Valledor M et al. **Cell Reports** (Jul 2023). “Early chromosome condensation by XIST builds A-repeat RNA density that facilitates gene silencing.” https://doi.org/10.1016/j.celrep.2023.112686 (valledor2023earlychromosomecondensation pages 1-3, valledor2023earlychromosomecondensation pages 10-11, valledor2023earlychromosomecondensation media 58d592e8)
- Dror I et al. **Cell** (Jan 2024). “XIST directly regulates X-linked and autosomal genes in naive human pluripotent cells.” https://doi.org/10.1016/j.cell.2023.11.033 (dror2024xistdirectlyregulates pages 1-3)
- Bansal P et al. **Science Advances** (Jun 2024). “A dynamic in vitro model of Down syndrome neurogenesis with trisomy 21 gene dosage correction.” https://doi.org/10.1126/sciadv.adj0385 (bansal2024adynamicin pages 1-3)
- Gupta K et al. **Human Genetics** (Mar 2024). “Trisomy silencing by XIST: translational prospects and challenges.” https://doi.org/10.1007/s00439-024-02651-8 (gupta2024trisomysilencingby pages 1-3)


References

1. (dror2024xistdirectlyregulates pages 1-3): Iris Dror, Tsotne Chitiashvili, Shawn Y.X. Tan, Clara T. Cano, Anna Sahakyan, Yolanda Markaki, Constantinos Chronis, Amanda J. Collier, Weixian Deng, Guohao Liang, Yu Sun, Anna Afasizheva, Jarrett Miller, Wen Xiao, Douglas L. Black, Fangyuan Ding, and Kathrin Plath. Xist directly regulates x-linked and autosomal genes in naive human pluripotent cells. Cell, 187:110-129.e31, Jan 2024. URL: https://doi.org/10.1016/j.cell.2023.11.033, doi:10.1016/j.cell.2023.11.033. This article has 74 citations and is from a highest quality peer-reviewed journal.

2. (valledor2023earlychromosomecondensation pages 1-3): Melvys Valledor, Meg Byron, Brett Dumas, Dawn M. Carone, Lisa L. Hall, and Jeanne B. Lawrence. Early chromosome condensation by xist builds a-repeat rna density that facilitates gene silencing. Cell Reports, 42:112686, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112686, doi:10.1016/j.celrep.2023.112686. This article has 23 citations and is from a highest quality peer-reviewed journal.

3. (lu2020structuralmodularityof pages 1-2): Zhipeng Lu, Jimmy K. Guo, Yuning Wei, Diana R. Dou, Brian Zarnegar, Qing Ma, Rui Li, Yang Zhao, Fan Liu, Hani Choudhry, Paul A. Khavari, and Howard Y. Chang. Structural modularity of the xist ribonucleoprotein complex. Nature Communications, Dec 2020. URL: https://doi.org/10.1038/s41467-020-20040-3, doi:10.1038/s41467-020-20040-3. This article has 102 citations and is from a highest quality peer-reviewed journal.

4. (lu2020structuralmodularityof pages 6-7): Zhipeng Lu, Jimmy K. Guo, Yuning Wei, Diana R. Dou, Brian Zarnegar, Qing Ma, Rui Li, Yang Zhao, Fan Liu, Hani Choudhry, Paul A. Khavari, and Howard Y. Chang. Structural modularity of the xist ribonucleoprotein complex. Nature Communications, Dec 2020. URL: https://doi.org/10.1038/s41467-020-20040-3, doi:10.1038/s41467-020-20040-3. This article has 102 citations and is from a highest quality peer-reviewed journal.

5. (minajigi2015acomprehensivexist pages 1-3): Anand Minajigi, John E. Froberg, Chunyao Wei, Hongjae Sunwoo, Barry Kesner, David Colognori, Derek Lessing, Bernhard Payer, Myriam Boukhali, Wilhelm Haas, and Jeannie T. Lee. A comprehensive xist interactome reveals cohesin repulsion and an rna-directed chromosome conformation. Science, Jul 2015. URL: https://doi.org/10.1126/science.aab2276, doi:10.1126/science.aab2276. This article has 587 citations and is from a highest quality peer-reviewed journal.

6. (mchugh2015thexistlncrna pages 1-2): Colleen A. McHugh, Chun-Kan Chen, Amy Chow, Christine F. Surka, Christina Tran, Patrick McDonel, Amy Pandya-Jones, Mario Blanco, Christina Burghard, Annie Moradian, Michael J. Sweredoski, Alexander A. Shishkin, Julia Su, Eric S. Lander, Sonja Hess, Kathrin Plath, and Mitchell Guttman. The xist lncrna interacts directly with sharp to silence transcription through hdac3. Nature, 521:232-236, Apr 2015. URL: https://doi.org/10.1038/nature14443, doi:10.1038/nature14443. This article has 1319 citations and is from a highest quality peer-reviewed journal.

7. (mchugh2015thexistlncrna pages 6-7): Colleen A. McHugh, Chun-Kan Chen, Amy Chow, Christine F. Surka, Christina Tran, Patrick McDonel, Amy Pandya-Jones, Mario Blanco, Christina Burghard, Annie Moradian, Michael J. Sweredoski, Alexander A. Shishkin, Julia Su, Eric S. Lander, Sonja Hess, Kathrin Plath, and Mitchell Guttman. The xist lncrna interacts directly with sharp to silence transcription through hdac3. Nature, 521:232-236, Apr 2015. URL: https://doi.org/10.1038/nature14443, doi:10.1038/nature14443. This article has 1319 citations and is from a highest quality peer-reviewed journal.

8. (pintacuda2017hnrnpkrecruitspcgf35prc1 pages 1-3): Greta Pintacuda, Guifeng Wei, Chloë Roustan, Burcu Anil Kirmizitas, Nicolae Solcan, Andrea Cerase, Alfredo Castello, Shabaz Mohammed, Benoît Moindrot, Tatyana B. Nesterova, and Neil Brockdorff. Hnrnpk recruits pcgf3/5-prc1 to the xist rna b-repeat to establish polycomb-mediated chromosomal silencing. Molecular Cell, 68:955-969.e10, Dec 2017. URL: https://doi.org/10.1016/j.molcel.2017.11.013, doi:10.1016/j.molcel.2017.11.013. This article has 403 citations and is from a highest quality peer-reviewed journal.

9. (pintacuda2017hnrnpkrecruitspcgf35prc1 pages 10-13): Greta Pintacuda, Guifeng Wei, Chloë Roustan, Burcu Anil Kirmizitas, Nicolae Solcan, Andrea Cerase, Alfredo Castello, Shabaz Mohammed, Benoît Moindrot, Tatyana B. Nesterova, and Neil Brockdorff. Hnrnpk recruits pcgf3/5-prc1 to the xist rna b-repeat to establish polycomb-mediated chromosomal silencing. Molecular Cell, 68:955-969.e10, Dec 2017. URL: https://doi.org/10.1016/j.molcel.2017.11.013, doi:10.1016/j.molcel.2017.11.013. This article has 403 citations and is from a highest quality peer-reviewed journal.

10. (chen2016xistrecruitsthe pages 1-2): Chun-Kan Chen, Mario Blanco, Constanza Jackson, Erik Aznauryan, Noah Ollikainen, Christine Surka, Amy Chow, Andrea Cerase, Patrick McDonel, and Mitchell Guttman. Xist recruits the x chromosome to the nuclear lamina to enable chromosome-wide silencing. Science, 354:468-472, Oct 2016. URL: https://doi.org/10.1126/science.aae0047, doi:10.1126/science.aae0047. This article has 348 citations and is from a highest quality peer-reviewed journal.

11. (chen2016xistrecruitsthe pages 3-4): Chun-Kan Chen, Mario Blanco, Constanza Jackson, Erik Aznauryan, Noah Ollikainen, Christine Surka, Amy Chow, Andrea Cerase, Patrick McDonel, and Mitchell Guttman. Xist recruits the x chromosome to the nuclear lamina to enable chromosome-wide silencing. Science, 354:468-472, Oct 2016. URL: https://doi.org/10.1126/science.aae0047, doi:10.1126/science.aae0047. This article has 348 citations and is from a highest quality peer-reviewed journal.

12. (nesterova2019systematicallelicanalysis pages 1-2): Tatyana B Nesterova, Guifeng Wei, Heather Coker, Greta Pintacuda, Joseph S Bowness, Tianyi Zhang, Mafalda Almeida, Bianca Bloechl, Benoit Moindrot, Emma J Carter, Ines Alvarez Rodrigo, Qi Pan, Ying Bi, Chun-Xiao Song, and Neil Brockdorff. Systematic allelic analysis defines the interplay of key pathways in x chromosome inactivation. Nature Communications, Nov 2019. URL: https://doi.org/10.1038/s41467-019-11171-3, doi:10.1038/s41467-019-11171-3. This article has 160 citations and is from a highest quality peer-reviewed journal.

13. (valledor2023earlychromosomecondensation media 58d592e8): Melvys Valledor, Meg Byron, Brett Dumas, Dawn M. Carone, Lisa L. Hall, and Jeanne B. Lawrence. Early chromosome condensation by xist builds a-repeat rna density that facilitates gene silencing. Cell Reports, 42:112686, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112686, doi:10.1016/j.celrep.2023.112686. This article has 23 citations and is from a highest quality peer-reviewed journal.

14. (valledor2023earlychromosomecondensation pages 10-11): Melvys Valledor, Meg Byron, Brett Dumas, Dawn M. Carone, Lisa L. Hall, and Jeanne B. Lawrence. Early chromosome condensation by xist builds a-repeat rna density that facilitates gene silencing. Cell Reports, 42:112686, Jul 2023. URL: https://doi.org/10.1016/j.celrep.2023.112686, doi:10.1016/j.celrep.2023.112686. This article has 23 citations and is from a highest quality peer-reviewed journal.

15. (bansal2024adynamicin pages 1-3): Prakhar Bansal, Erin C. Banda, Heather R. Glatt-Deeley, Christopher E. Stoddard, Jeremy W. Linsley, Neha Arora, Cécile Deleschaux, Darcy T. Ahern, Yuvabharath Kondaveeti, Rachael E. Massey, Michael Nicouleau, Shijie Wang, Miguel Sabariego-Navarro, Mara Dierssen, Steven Finkbeiner, and Stefan F. Pinter. A dynamic in vitro model of down syndrome neurogenesis with trisomy 21 gene dosage correction. Science Advances, Jun 2024. URL: https://doi.org/10.1126/sciadv.adj0385, doi:10.1126/sciadv.adj0385. This article has 14 citations and is from a highest quality peer-reviewed journal.

16. (gupta2024trisomysilencingby pages 1-3): Khusali Gupta, Jan T. Czerminski, and Jeanne B. Lawrence. Trisomy silencing by xist: translational prospects and challenges. Human Genetics, 143:843-855, Mar 2024. URL: https://doi.org/10.1007/s00439-024-02651-8, doi:10.1007/s00439-024-02651-8. This article has 18 citations and is from a peer-reviewed journal.

17. (loda2019xistrnain pages 7-9): Agnese Loda and Edith Heard. Xist rna in action: past, present, and future. PLOS Genetics, 15:e1008333, Sep 2019. URL: https://doi.org/10.1371/journal.pgen.1008333, doi:10.1371/journal.pgen.1008333. This article has 313 citations and is from a domain leading peer-reviewed journal.

18. (loda2019xistrnain pages 13-14): Agnese Loda and Edith Heard. Xist rna in action: past, present, and future. PLOS Genetics, 15:e1008333, Sep 2019. URL: https://doi.org/10.1371/journal.pgen.1008333, doi:10.1371/journal.pgen.1008333. This article has 313 citations and is from a domain leading peer-reviewed journal.

19. (minajigi2015acomprehensivexist pages 6-8): Anand Minajigi, John E. Froberg, Chunyao Wei, Hongjae Sunwoo, Barry Kesner, David Colognori, Derek Lessing, Bernhard Payer, Myriam Boukhali, Wilhelm Haas, and Jeannie T. Lee. A comprehensive xist interactome reveals cohesin repulsion and an rna-directed chromosome conformation. Science, Jul 2015. URL: https://doi.org/10.1126/science.aab2276, doi:10.1126/science.aab2276. This article has 587 citations and is from a highest quality peer-reviewed journal.

20. (mchugh2015thexistlncrna pages 4-6): Colleen A. McHugh, Chun-Kan Chen, Amy Chow, Christine F. Surka, Christina Tran, Patrick McDonel, Amy Pandya-Jones, Mario Blanco, Christina Burghard, Annie Moradian, Michael J. Sweredoski, Alexander A. Shishkin, Julia Su, Eric S. Lander, Sonja Hess, Kathrin Plath, and Mitchell Guttman. The xist lncrna interacts directly with sharp to silence transcription through hdac3. Nature, 521:232-236, Apr 2015. URL: https://doi.org/10.1038/nature14443, doi:10.1038/nature14443. This article has 1319 citations and is from a highest quality peer-reviewed journal.

## Citations

1. minajigi2015acomprehensivexist pages 1-3
2. mchugh2015thexistlncrna pages 6-7
3. chen2016xistrecruitsthe pages 1-2
4. nesterova2019systematicallelicanalysis pages 1-2
5. valledor2023earlychromosomecondensation pages 10-11
6. dror2024xistdirectlyregulates pages 1-3
7. bansal2024adynamicin pages 1-3
8. gupta2024trisomysilencingby pages 1-3
9. valledor2023earlychromosomecondensation pages 1-3
10. lu2020structuralmodularityof pages 1-2
11. lu2020structuralmodularityof pages 6-7
12. mchugh2015thexistlncrna pages 1-2
13. chen2016xistrecruitsthe pages 3-4
14. loda2019xistrnain pages 7-9
15. loda2019xistrnain pages 13-14
16. minajigi2015acomprehensivexist pages 6-8
17. mchugh2015thexistlncrna pages 4-6
18. https://doi.org/10.1038/nature14443
19. https://doi.org/10.1126/science.aab2276
20. https://doi.org/10.1126/science.aae0047
21. https://doi.org/10.1016/j.molcel.2017.11.013
22. https://doi.org/10.1038/s41467-019-11171-3
23. https://doi.org/10.1016/j.celrep.2023.112686
24. https://doi.org/10.1016/j.cell.2023.11.033
25. https://doi.org/10.1126/sciadv.adj0385
26. https://doi.org/10.1007/s00439-024-02651-8
27. https://doi.org/10.1016/j.cell.2023.11.033,
28. https://doi.org/10.1016/j.celrep.2023.112686,
29. https://doi.org/10.1038/s41467-020-20040-3,
30. https://doi.org/10.1126/science.aab2276,
31. https://doi.org/10.1038/nature14443,
32. https://doi.org/10.1016/j.molcel.2017.11.013,
33. https://doi.org/10.1126/science.aae0047,
34. https://doi.org/10.1038/s41467-019-11171-3,
35. https://doi.org/10.1126/sciadv.adj0385,
36. https://doi.org/10.1007/s00439-024-02651-8,
37. https://doi.org/10.1371/journal.pgen.1008333,