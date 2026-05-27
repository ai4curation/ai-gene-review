---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T13:51:43.634085'
end_time: '2026-05-12T14:03:50.103714'
duration_seconds: 726.47
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 12
---

## Question

Concise GO annotation research for human HSPA12A / UniProt O43301. Focus on: whether HSPA12A has experimentally supported canonical HSP70 chaperone/protein-folding activity; ATP/ADP-sensitive interaction with SORL1/SorLA cytosolic tail; effects on SORL1 internalization, subcellular localization, APP/amyloid context only where relevant; cellular localization evidence; disease/tissue signaling studies only if they change GO annotation; caveats for generic protein binding and high-throughput HSPA12B transferred interactions. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human HSPA12A / UniProt O43301. Focus on: whether HSPA12A has experimentally supported canonical HSP70 chaperone/protein-folding activity; ATP/ADP-sensitive interaction with SORL1/SorLA cytosolic tail; effects on SORL1 internalization, subcellular localization, APP/amyloid context only where relevant; cellular localization evidence; disease/tissue signaling studies only if they change GO annotation; caveats for generic protein binding and high-throughput HSPA12B transferred interactions. Include PMID/DOI citations and keep under 1500 words.

## Concise GO annotation research report: Human HSPA12A (UniProt O43301)

### Scope and key questions
This report evaluates whether HSPA12A has **experimentally supported canonical HSP70 chaperone/protein-folding activity**, and summarizes **experimentally demonstrated** interactions and trafficking effects with **SORL1/SorLA**, including **ATP/ADP sensitivity**, plus **subcellular localization** evidence relevant to GO annotation. Claims are restricted to evidence in the retrieved primary literature (notably Madsen et al., 2019) and selected contextual sources. 

| Topic | Key findings | Experimental approach (assay/method) | System (cell type/organism) | Evidence strength for GO (suggested GO annotation impact) | Reference (publication year, journal) | Identifier (DOI and/or PMID; include URL) |
|---|---|---|---|---|---|---|
| Canonical HSP70 activity | HSPA12A/HSPA12B were identified as distant HSP70 family members with an **atypical Hsp70 ATPase domain**; this supports family relationship but not canonical ATPase/chaperone annotation. Later cancer work describes HSPA12A as an HSP70-family protein based on domain architecture, but provides no direct ATPase, refolding, aggregation-suppression, or co-chaperone assays. | Sequence/domain analysis; expression studies; protein interaction work without ATPase/chaperone biochemistry | Mouse/human gene characterization; human HCC cells | **Weak/negative for canonical GO MF**: do **not** infer ATPase activity, unfolded protein binding, or protein folding chaperone activity from current evidence alone. | Han et al., 2003, *PNAS*; Cheng et al., 2020, *FEBS J* (han2003twohsp70family pages 1-2, cheng2020heat‐shockproteina12a pages 1-3) | Han 2003 DOI: 10.1073/pnas.252764399; https://doi.org/10.1073/pnas.252764399. Cheng 2020 DOI: 10.1111/febs.15276; https://doi.org/10.1111/febs.15276 |
| SORL1/SorLA binding | HSPA12A was identified as a **specific SorLA cytosolic-tail interactor**; Y2H recovered C-terminal HSPA12A clones, GST-HSPA12A pulled down full-length SorLA, and binding mapped to SorLA cytosolic acidic clusters including E34-D38 and D47D48. HSPA12B was negative in Y2H, arguing against paralog transfer. | Yeast two-hybrid screen and mapping; GST pull-down; mutagenesis of SorLA cytosolic tail | Adult human brain cDNA library; HEK293 cells expressing SorLA; mouse cortical astrocytes for co-localization | **Moderate/strong for specific protein binding**: supports curated binding to SORL1/SorLA cytosolic domain; avoid generic broad “protein binding” beyond tested partner. | Madsen et al., 2019, *Sci Rep* (madsen2019hspa12atargetsthe pages 2-3, madsen2019hspa12atargetsthe pages 3-5) | DOI: 10.1038/s41598-018-37336-6; https://doi.org/10.1038/s41598-018-37336-6 |
| ATP/ADP sensitivity | SorLA precipitation by GST-HSPA12A increased with **ADP** and decreased with **ATP**, consistent with nucleotide-sensitive substrate interaction; however, this is binding modulation, not a direct ATPase assay. | Pull-downs with titrated ATP/ADP (0.5–5 mM; methods also report 0.1–5 mM) followed by immunoblot | HEK293 lysates with recombinant GST-HSPA12A | **Moderate for nucleotide-regulated binding behavior**, but **insufficient for ATPase GO MF**. Could support annotation note/caveat, not direct ATP hydrolysis activity. | Madsen et al., 2019, *Sci Rep* (madsen2019hspa12atargetsthe pages 2-3, madsen2019hspa12atargetsthe pages 5-7, madsen2019hspa12atargetsthe pages 10-11, madsen2019hspa12atargetsthe media 335a8308) | DOI: 10.1038/s41598-018-37336-6; https://doi.org/10.1038/s41598-018-37336-6 |
| Effects on SorLA internalization | HSPA12A **delays SorLA internalization/endocytosis**: surface SorLA staining persisted longer in HSPA12A-expressing cells, and labeled SorLA accumulated in HSPA12A-positive vesicles. | Antibody uptake/internalization time course; confocal microscopy; image quantification | HEK293 stable transfectants expressing SorLA ± HSPA12A | **Moderate for process-level trafficking/endocytosis regulation** involving SorLA; relevant to receptor internalization/trafficking rather than APP biology per se. | Madsen et al., 2019, *Sci Rep* (madsen2019hspa12atargetsthe pages 5-7, madsen2019hspa12atargetsthe pages 1-2, madsen2019hspa12atargetsthe media 335a8308) | DOI: 10.1038/s41598-018-37336-6; https://doi.org/10.1038/s41598-018-37336-6 |
| Effects on SorLA subcellular localization | HSPA12A expression redistributes SorLA into **dense perinuclear vesicular compartments** and denser sucrose-gradient fractions; co-localization seen in vesicles. APP/amyloid context is indirect via SorLA identity, not a direct HSPA12A-APP experiment. | Immunofluorescence/confocal microscopy; live imaging of GFP-HSPA12A; sucrose-gradient/endosomal fractionation; high-content imaging | HEK293 cells; primary cortical astrocytes | **Moderate for receptor trafficking/localization regulation**; may support biological process annotations tied to SorLA trafficking if curated conservatively. | Madsen et al., 2019, *Sci Rep* (madsen2019hspa12atargetsthe pages 5-7, madsen2019hspa12atargetsthe pages 7-9, madsen2019hspa12atargetsthe pages 3-5, madsen2019hspa12atargetsthe media 335a8308) | DOI: 10.1038/s41598-018-37336-6; https://doi.org/10.1038/s41598-018-37336-6 |
| HSPA12A localization | Experimental evidence places HSPA12A in **cytosol and nucleus**, with additional association with **perinuclear/vesicular compartments** and SorLA-positive vesicles. Evidence derives from endogenous IF, tagged HSPA12A imaging, and soluble/insoluble plus gradient fractionation. | Immunofluorescence; Western blot of soluble/insoluble fractions; confocal imaging of GFP/mCherry-HSPA12A; sucrose gradients | Primary mouse cortical astrocytes; transfected HEK293 cells | **Moderate for CC terms**: cytosol and nucleus are supported; vesicular/perinuclear compartment association is supported but specific endosome subtype should be annotated cautiously. | Madsen et al., 2019, *Sci Rep* (madsen2019hspa12atargetsthe pages 7-9, madsen2019hspa12atargetsthe pages 5-7, madsen2019hspa12atargetsthe pages 10-11, madsen2019hspa12atargetsthe pages 3-5) | DOI: 10.1038/s41598-018-37336-6; https://doi.org/10.1038/s41598-018-37336-6 |


*Table: This table summarizes GO-relevant experimental evidence for human HSPA12A, emphasizing what is directly supported versus what remains too weak for annotation. It is useful for distinguishing specific SorLA trafficking evidence from unsupported assumptions of canonical HSP70 chaperone activity.*

### 1) Key concepts and definitions (GO-relevant)
**Canonical HSP70 chaperone activity** typically implies (i) ATP binding/hydrolysis by a nucleotide-binding domain (NBD), (ii) nucleotide-regulated substrate binding/release by a substrate-binding domain (SBD), and (iii) measurable chaperone outcomes (e.g., prevention of aggregation, protein refolding) often modulated by HSP40/J-domain proteins and nucleotide exchange factors. A molecular chaperone definition emphasizing **controlled binding/release** to stabilize unstable conformers and influence folding/assembly/transport is summarized in a recent review of heat shock protein networks (Melikov & Novák, 2024; published 2024-01; https://doi.org/10.14712/fb2024070030152) (melikov2024heatshockprotein pages 1-3).

**GO implication:** For HSPA12A, assigning GO molecular function terms like *ATPase activity* or *protein folding chaperone* generally requires **direct enzymatic ATPase assays** and/or **client protein folding/refolding/aggregation assays**, not solely membership in an HSP70-like sequence family or nucleotide-sensitive binding to one partner.

### 2) Does HSPA12A have experimentally supported canonical HSP70 ATPase/chaperone/protein-folding activity?
**Current evidence in retrieved primary literature is insufficient to support canonical HSP70 chaperone/protein-folding activity for HSPA12A.**

*Foundational characterization:* HspA12A (and HspA12B) were originally described as **distant members of the Hsp70 family** with an **“atypical Hsp70 ATPase domain”** based on conserved domain searches and sequence similarity (Han et al., 2003, PNAS; published 2003-02-04; https://doi.org/10.1073/pnas.252764399) (han2003twohsp70family pages 1-2). This supports *family relationship* but does not establish ATP hydrolysis or refolding activity.

*Functional papers examined:* A study in hepatocellular carcinoma identifies HSPA12A as an HSP70-family protein and reports **direct binding to PCNA** with an effect on PCNA trimerization and tumor phenotypes, but the provided text contains **no ATPase assays and no refolding/aggregation suppression assays** (Cheng et al., 2020, FEBS J; published online 2020-03; https://doi.org/10.1111/febs.15276) (cheng2020heat‐shockproteina12a pages 1-3).

*SorLA study:* Madsen et al. interpret nucleotide-sensitive SorLA binding as “similar to other HSPs regarding ADP dependent substrate binding,” but they do **not** report direct ATPase kinetics or canonical folding/refolding assays for HSPA12A (Madsen et al., 2019) (madsen2019hspa12atargetsthe pages 7-9, madsen2019hspa12atargetsthe pages 1-2).

**Conclusion for GO MF:** Based on the retrieved evidence, HSPA12A should **not** be annotated as a canonical HSP70 chaperone (e.g., *ATP hydrolysis activity*, *unfolded protein binding*, *protein folding chaperone*) on experimental grounds alone; the strongest experimental support is instead **nucleotide-modulated binding** to a specific partner (SORL1/SorLA tail) (madsen2019hspa12atargetsthe pages 2-3, madsen2019hspa12atargetsthe pages 5-7).

### 3) ATP/ADP-sensitive interaction with SORL1/SorLA cytosolic tail
**Primary evidence:** Madsen et al. (Scientific Reports, 2019-01) identify HSPA12A as a **SorLA (SORL1) cytosolic-domain binding partner** and provide multiple orthogonal assays supporting specificity and nucleotide modulation (https://doi.org/10.1038/s41598-018-37336-6) (madsen2019hspa12atargetsthe pages 2-3).

**Interaction discovery and specificity**
- **Yeast two-hybrid (Y2H)** screen using an adult human brain cDNA library identified HSPA12A prey clones interacting with SorLA cytosolic domain; importantly, the related paralog **HSPA12B was negative** in Y2H, supporting *no automatic paralog transfer* (madsen2019hspa12atargetsthe pages 2-3).
- **GST pull-down** with full-length recombinant GST-HSPA12A pulled down full-length SorLA from HEK293 lysates; GST alone did not (madsen2019hspa12atargetsthe pages 2-3).
- Specificity within the Vps10p-domain receptor family was supported by failure to detect binding to Sortilin and other tested receptors in the reported assays (madsen2019hspa12atargetsthe pages 5-7).

**Nucleotide sensitivity (ATP/ADP modulation)**
- Pull-downs performed with nucleotide titrations showed **ADP increased** SorLA precipitation while **ATP decreased** it, consistent with an HSP70-like nucleotide-regulated binding mode (madsen2019hspa12atargetsthe pages 2-3, madsen2019hspa12atargetsthe pages 5-7).
- Figure evidence for the nucleotide-dependence is captured in the cropped figure panels (madsen2019hspa12atargetsthe media 335a8308, madsen2019hspa12atargetsthe media c051a9b6, madsen2019hspa12atargetsthe media 6d1a2daf).

**Binding site mapping on SorLA cytosolic tail**
- Y2H truncations and mutagenesis mapped binding dependence to a region (reported as G29–P50 in the excerpt) containing **acidic clusters**, with strong dependence on the pentameric acidic cluster **E34–D38** and the **D47D48** motif (madsen2019hspa12atargetsthe pages 7-9, madsen2019hspa12atargetsthe pages 2-3).
- The D47D48 motif overlaps a reported GGA2 binding site, raising a mechanistic possibility of adaptor competition (important caveat for GO process inference) (madsen2019hspa12atargetsthe pages 7-9, madsen2019hspa12atargetsthe pages 3-5).

**GO implication:** This supports a curated annotation for **specific protein binding** to SORL1/SorLA cytosolic domain, and a mechanistic note that binding is **ATP/ADP sensitive** (madsen2019hspa12atargetsthe pages 2-3).

### 4) Effects on SORL1/SorLA internalization and subcellular localization (APP/amyloid context only where relevant)
Madsen et al. experimentally link HSPA12A binding to functional trafficking changes in SorLA.

**SorLA internalization/endocytosis**
- Using an antibody uptake/internalization time course in HEK293 cells, HSPA12A expression **delayed SorLA internalization**, with surface SorLA persisting longer in the presence of HSPA12A (madsen2019hspa12atargetsthe pages 5-7).
- Figure evidence showing delayed internalization is present in the retrieved crops (madsen2019hspa12atargetsthe media 335a8308, madsen2019hspa12atargetsthe media c051a9b6, madsen2019hspa12atargetsthe media 6d1a2daf).

**SorLA subcellular distribution/localization**
- Immunofluorescence/live imaging and biochemical fractionation indicated HSPA12A constrained SorLA into **dense perinuclear compartments/vesicles** and shifted SorLA into **denser vesicle fractions** on sucrose gradients (madsen2019hspa12atargetsthe pages 3-5).
- Figure crops demonstrating SorLA redistribution to perinuclear compartments are included among retrieved images (madsen2019hspa12atargetsthe media 335a8308, madsen2019hspa12atargetsthe media c051a9b6, madsen2019hspa12atargetsthe media 6d1a2daf).

**APP/amyloid relevance:** SorLA is an APP receptor encoded by SORL1, a major Alzheimer’s disease risk gene. In this dataset, HSPA12A effects are established at the level of SorLA trafficking; **direct effects on APP processing/amyloid output were not required to support the GO-relevant trafficking statements** and were not the focus of the extracted evidence (madsen2019hspa12atargetsthe pages 1-2, madsen2019hspa12atargetsthe pages 5-7).

**GO implication:** Evidence supports cautious biological process annotations around **regulation of receptor internalization/trafficking** in the SorLA system, but the mechanism could be via adaptor competition (e.g., with GGA2/AP adaptors) rather than chaperone-mediated folding (madsen2019hspa12atargetsthe pages 7-9, madsen2019hspa12atargetsthe pages 3-5).

### 5) HSPA12A cellular localization evidence (GO cellular component)
The strongest localization evidence in the retrieved context comes from Madsen et al. (2019).

**Cytosol and nucleus**
- Western blotting of detergent **soluble/insoluble fractions** and immunofluorescence supported that HSPA12A is present in **cytosol and nucleus** (madsen2019hspa12atargetsthe pages 7-9, madsen2019hspa12atargetsthe pages 3-5).

**Vesicular/perinuclear association (SorLA-positive vesicles)**
- In primary cortical astrocytes, immunofluorescence showed partial co-localization of endogenous cytoplasmic HSPA12A with SorLA in vesicular structures (madsen2019hspa12atargetsthe pages 5-7, madsen2019hspa12atargetsthe pages 3-5).
- Live imaging of GFP-tagged HSPA12A in HEK293 cells showed prominent signal in large perinuclear vesicles and smaller mobile vesicles (madsen2019hspa12atargetsthe pages 3-5).

**GO implication:** Cellular component annotations supported by direct evidence include **cytosol** and **nucleus**, with cautious support for association with **perinuclear vesicular/endosomal compartments** (the precise endosome subtype is not firmly established by the excerpted evidence) (madsen2019hspa12atargetsthe pages 5-7, madsen2019hspa12atargetsthe pages 3-5).

### 6) Caveats relevant to GO curation
1. **Do not infer canonical HSP70 chaperone/protein-folding activity** from sequence family assignment or nucleotide-sensitive binding alone; direct ATPase and refolding assays were not identified in the retrieved evidence (han2003twohsp70family pages 1-2, cheng2020heat‐shockproteina12a pages 1-3, madsen2019hspa12atargetsthe pages 1-2).
2. **Avoid generic “protein binding” over-annotation.** The best-supported specific binding partner in the retrieved primary literature is SorLA/SORL1 cytosolic tail, mapped to defined acidic motifs, and shown to be nucleotide-sensitive (madsen2019hspa12atargetsthe pages 2-3).
3. **Avoid transferring high-throughput or paralog interactions from HSPA12B to HSPA12A.** In the SorLA study, **HSPA12B was explicitly negative** in Y2H, emphasizing paralog specificity (madsen2019hspa12atargetsthe pages 2-3).
4. **Overexpression/heterologous-system limitations:** Many trafficking/localization effects were measured in HEK293 transfectants, and localization includes tagged HSPA12A constructs; these are strong for mechanistic hypotheses but should be curated with appropriate evidence codes and caution (madsen2019hspa12atargetsthe pages 10-11).

### 7) “Recent developments” (2023–2024) in the retrieved context and GO relevance
The retrieved 2023–2024 HSPA12A studies in other disease contexts (e.g., metabolism/signaling, lactylation pathways) were not necessary to establish the SorLA trafficking mechanism and generally do not provide direct canonical HSP70 chaperone assays in the provided excerpts (e.g., Li et al., 2024; https://doi.org/10.1007/s00018-024-05427-5) (li2024hspa12apromotescmyc pages 1-3). A 2024 heat shock protein network review provides updated conceptual framing for chaperone mechanisms but is not specific evidence for HSPA12A’s molecular function (Melikov & Novák, 2024; https://doi.org/10.14712/fb2024070030152) (melikov2024heatshockprotein pages 1-3).

### Suggested GO-annotation takeaways (evidence-bounded)
- **Molecular function:** support **SORL1/SorLA cytosolic-tail binding** (nucleotide-modulated interaction) (madsen2019hspa12atargetsthe pages 2-3, madsen2019hspa12atargetsthe pages 5-7).
- **Biological process:** support conservative annotation related to **SorLA receptor internalization/trafficking regulation** based on delayed internalization and relocalization (madsen2019hspa12atargetsthe pages 5-7, madsen2019hspa12atargetsthe media 335a8308).
- **Cellular component:** support **cytosol** and **nucleus**, and cautious association with **perinuclear vesicular/endosomal structures** (madsen2019hspa12atargetsthe pages 3-5, madsen2019hspa12atargetsthe pages 5-7).
- **Not supported (from retrieved evidence):** canonical HSP70 *ATPase activity* and *protein folding chaperone activity* (han2003twohsp70family pages 1-2, cheng2020heat‐shockproteina12a pages 1-3, madsen2019hspa12atargetsthe pages 1-2).

References

1. (han2003twohsp70family pages 1-2): Zhihua Han, Quynh A. Truong, Shirley Park, and Jan L. Breslow. Two hsp70 family members expressed in atherosclerotic lesions. Proceedings of the National Academy of Sciences of the United States of America, 100:1256-1261, Jan 2003. URL: https://doi.org/10.1073/pnas.252764399, doi:10.1073/pnas.252764399. This article has 158 citations and is from a highest quality peer-reviewed journal.

2. (cheng2020heat‐shockproteina12a pages 1-3): Hao Cheng, Xiaofei Cao, Xinxu Min, Xiaojin Zhang, Qiuyue Kong, Qian Mao, Rongrong Li, Bin Xue, Lei Fang, Li Liu, and Zhengnian Ding. Heat‐shock protein a12a is a novel pcna‐binding protein and promotes hepatocellular carcinoma growth. The FEBS Journal, 287:5464-5477, Mar 2020. URL: https://doi.org/10.1111/febs.15276, doi:10.1111/febs.15276. This article has 19 citations.

3. (madsen2019hspa12atargetsthe pages 2-3): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

4. (madsen2019hspa12atargetsthe pages 3-5): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

5. (madsen2019hspa12atargetsthe pages 5-7): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

6. (madsen2019hspa12atargetsthe pages 10-11): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

7. (madsen2019hspa12atargetsthe media 335a8308): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

8. (madsen2019hspa12atargetsthe pages 1-2): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

9. (madsen2019hspa12atargetsthe pages 7-9): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

10. (melikov2024heatshockprotein pages 1-3): Aleksandr Melikov and Petr Novák. Heat shock protein network: the mode of action, the role in protein folding and human pathologies. Folia biologica, 70 3:152-165, Jan 2024. URL: https://doi.org/10.14712/fb2024070030152, doi:10.14712/fb2024070030152. This article has 11 citations and is from a peer-reviewed journal.

11. (madsen2019hspa12atargetsthe media c051a9b6): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

12. (madsen2019hspa12atargetsthe media 6d1a2daf): Peder Madsen, Toke Jost Isaksen, Piotr Siupka, Andrea E. Tóth, Mette Nyegaard, Camilla Gustafsen, and Morten S. Nielsen. Hspa12a targets the cytoplasmic domain and affects the trafficking of the amyloid precursor protein receptor sorla. Scientific Reports, Jan 2019. URL: https://doi.org/10.1038/s41598-018-37336-6, doi:10.1038/s41598-018-37336-6. This article has 16 citations and is from a peer-reviewed journal.

13. (li2024hspa12apromotescmyc pages 1-3): Yunfan Li, Xinxu Min, Xiaojin Zhang, Xiaofei Cao, Qiuyue Kong, Qian Mao, Hao Cheng, Liming Gou, Yuehua Li, Chuanfu Li, Li Liu, and Zhengnian Ding. Hspa12a promotes c-myc lactylation-mediated proliferation of tubular epithelial cells to facilitate renal functional recovery from kidney ischemia/reperfusion injury. Cellular and Molecular Life Sciences: CMLS, Sep 2024. URL: https://doi.org/10.1007/s00018-024-05427-5, doi:10.1007/s00018-024-05427-5. This article has 23 citations.

## Citations

1. melikov2024heatshockprotein pages 1-3
2. https://doi.org/10.1073/pnas.252764399.
3. https://doi.org/10.1111/febs.15276
4. https://doi.org/10.1038/s41598-018-37336-6
5. https://doi.org/10.14712/fb2024070030152
6. https://doi.org/10.1073/pnas.252764399
7. https://doi.org/10.1007/s00018-024-05427-5
8. https://doi.org/10.1073/pnas.252764399,
9. https://doi.org/10.1111/febs.15276,
10. https://doi.org/10.1038/s41598-018-37336-6,
11. https://doi.org/10.14712/fb2024070030152,
12. https://doi.org/10.1007/s00018-024-05427-5,