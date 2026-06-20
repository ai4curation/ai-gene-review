Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for GO Annotation Review

## Target

- Gene symbol: FKF1
- Organism: Arabidopsis thaliana

## UniProt Context

=== UNIPROT METADATA ===
UniProt ID: Q9C9W9
Entry Name: ADO3_ARATH
Gene Name: ADO3
Protein Name: Adagio protein 3
Organism: Arabidopsis thaliana (Mouse-ear cress)
NCBI Taxonomy ID: 3702
Function: Component of an E3 ubiquitin ligase complex that plays a central role in blue light-dependent circadian cycles. Acts as a blue light photoreceptor, due to the presence of FMN, that mediates light- regulated protein degradation of critical clock components by targeting them to the proteasome complex. The SCF(ADO3) E3 ubiquitin ligase complex is involved in the regulation of circadian clock-dependent processes including transition to flowering time, hypocotyl elongation, cotyledons and leaf movement rhythms. Forms a complex with 'GIGANTEA' (GI) to regulate 'CONSTANS' (CO) expression. Promotes CO expression during the light period of long days by decreasing the stability of CDF1 and CDF2 and by interacting directly with the CO protein and stabilizing it. ADO3 function is mainly GI dependent. Does not act as a regulator of CDF1 transcription. The interactions of ADO1/ZTL and ADO2 with ADO3 prevent its interaction with CDF1.
Subcellular Location: Nucleus. Cytoplasm. Note=Moves from the nucleus into cytosolic speckles upon interaction with ADO1 and ADO2.
Subunit: Interacts with ADO1 (via Kelch repeats), ADO2 (via Kelch repeats), SKP1A/ASK1, SKP1B/ASK2, ASK3, SKP1K/ASK11, ASK12, ASK13 and SKP1N/ASK14. Interacts (via Kelch repeats) with CDF1, CDF2 and CDF3. Interacts (via N-terminus) with CO and GI (via N-terminus) in a blue- light-dependent manner.
======================

## Research Objective

Prepare a comprehensive literature-backed research report for GO annotation review of the target gene.

Focus on:

1. The core biochemical activity of the gene product and any substrate specificity.
2. The activation or maturation mechanism of the protein, including proteolytic processing if relevant.
3. The best-supported subcellular localization and complexes where the active protein functions.
4. The strongest experimentally supported biological processes in the target organism, or in very close orthologs when transfer is justified.
5. Which annotations appear to reflect core function versus context-specific, pleiotropic, or over-extended roles.
6. Any evidence bearing on apoptosis, developmental cell death, neuronal roles, inflammatory signaling, pyroptosis, synaptic remodeling, protein processing, and localization to cytoplasm, cytosol, nucleus, or signaling complexes.

## Output Requirements

Structure the report as:

1. Executive summary
2. Molecular function
3. Biological process roles
4. Cellular localization and complexes
5. Annotation-risk assessment
6. Key literature

Use citations for all substantive claims.


# Gene Research Report for GO Annotation Review: **FKF1 / ADO3** (Arabidopsis thaliana)

**Target:** FKF1 (UniProt: Q9C9W9; entry name ADO3_ARATH; protein name “Adagio protein 3/FLAVIN-BINDING, KELCH REPEAT, F-BOX 1”)  
**Scope:** GO annotation review focused on biochemical activity, activation mechanism, localization/complexes, best-supported biological processes, and annotation risks.

## 1) Executive summary

FKF1/ADO3 is best supported as a **blue-light–activated LOV-domain photoreceptor** that also functions as an **F-box substrate receptor/adaptor in an SCF-type E3 ubiquitin ligase** complex (SCF^FKF1), linking light perception to ubiquitin-mediated proteostasis. FKF1 integrates circadian timing (diurnal FKF1 abundance and photoperiod dependence) with targeted degradation and stabilization of flowering regulators, most directly via **(i) ubiquitin/proteasome-dependent removal of CYCLING DOF FACTOR (CDF) transcriptional repressors** and **(ii) blue-light-enhanced direct binding and stabilization of CONSTANS (CO)**, including regulation of COP1-dependent CO degradation. (ito2012lovdomaincontainingfbox pages 4-5, song2012fkf1conveystiming pages 1-2, song2014distinctrolesof pages 1-2, song2012fkf1conveystiming pages 2-4, lee2017thefboxprotein pages 1-2, lee2017thefboxprotein pages 7-8)

Recent work (2024) adds mechanistic granularity by showing that **FKF1 dimerization state** is an adjustable parameter: an FKF1 LOV-domain variant (I160R) that attenuates homodimerization increases evening **FT** transcript and accelerates flowering, consistent with **fine-tuning of CO stability and FKF1 partner interactions** (GI and COP1). (cho2024disruptingfkf1homodimerization pages 4-6, cho2024disruptingfkf1homodimerization pages 1-2)

No evidence in the retrieved Arabidopsis FKF1 literature supports roles in **apoptosis, neuronal/synaptic processes, inflammatory signaling, pyroptosis, or animal-like programmed cell death**; these appear to be cross-kingdom over-extensions and should be excluded unless plant-specific evidence emerges. (cho2024disruptingfkf1homodimerization pages 1-2, lee2017thefboxprotein pages 1-2, ito2012lovdomaincontainingfbox pages 4-5, l2023sheddingnewlight pages 39-42)

## 2) Molecular function

### 2.1 Core concepts/definitions (GO-relevant)

**LOV-domain photoreceptor (blue-light receptor):** FKF1 contains an N-terminal LOV domain that binds flavin chromophore (FMN) and undergoes blue-light-driven photochemistry that changes protein conformation and interaction capacity, enabling light-dependent signaling. (ito2012lovdomaincontainingfbox pages 4-5, lee2017thefboxprotein pages 1-2)

**SCF-type E3 ubiquitin ligase component (F-box protein):** FKF1 contains an F-box motif that binds SKP1-like proteins (ASKs) and enables assembly into an SCF complex together with CUL1 and Rbx; its Kelch repeats provide a substrate-binding interface typical of substrate receptors. (ito2012lovdomaincontainingfbox pages 4-5, song2014distinctrolesof pages 1-2, song2014distinctrolesof pages 2-3)

### 2.2 Biochemical activity and substrate specificity

**Substrate binding via Kelch repeats: CDF repressors.** FKF1 binds CDF1 through its Kelch repeat domain and is implicated in CDF1 degradation, thereby relieving repression of CO and FT transcription. (ito2012lovdomaincontainingfbox pages 4-5, song2012fkf1conveystiming pages 1-2)

**Direct protein binding and stabilization: CO.** FKF1 directly interacts with CO; domain mapping indicates the LOV domain is sufficient for CO binding (LOV and LOV+F constructs interact with CO), and binding is enhanced under blue light. (song2012fkf1conveystiming pages 2-4, song2012fkf1conveystiming media 04b014ef)

**Regulation of an upstream E3 ligase: COP1.** FKF1 binds COP1 (primarily its RING domain) and inhibits COP1 homodimerization, reducing COP1-dependent CO degradation and promoting flowering under long days (LD). (lee2017thefboxprotein pages 7-8)

### 2.3 Activation / maturation mechanism

**Light activation and photocycle:** FKF1 has a slow LOV dark reversion (S390→D450) with half-life reported ~62.5 hours at room temperature; a 9–amino-acid loop modulates recovery (deletion accelerates recovery to ~20.9 h). This supports a model where FKF1 can remain in a light-activated state for prolonged periods until degraded. (ito2012lovdomaincontainingfbox pages 4-5)

**Blue-light enhancement of FKF1–CO binding:** Blue light increases FKF1–CO co-immunoprecipitation relative to red light, and photochemically blind LOV mutations (C91A, R92D, Q163L) weaken the interaction, linking CO binding to LOV photochemistry. (song2012fkf1conveystiming pages 2-4, song2012fkf1conveystiming media 04b014ef)

**Dimerization as a regulatory mechanism (2024 development):** A LOV-domain substitution (I160R) attenuates FKF1 homodimerization without grossly altering photochemistry; transgenic expression of FKF1(I160R) in fkf1 background increases evening FT transcript and accelerates flowering, consistent with altered partner binding (enhanced GI and COP1 interaction) and increased CO stability. (cho2024disruptingfkf1homodimerization pages 4-6, cho2024disruptingfkf1homodimerization pages 1-2)

## 3) Biological process roles

### 3.1 Strongest experimentally supported processes in Arabidopsis

**Photoperiodic flowering regulation via GI–FKF1–CDF–CO–FT module.** FKF1 is a key positive regulator of flowering under long days by participating in the timed removal of CDF repressors and stabilization of CO in the afternoon, leading to increased FT expression. (song2012fkf1conveystiming pages 1-2, song2014distinctrolesof pages 1-2, wang2024circadianandphotoperiodic pages 3-4)

**Mechanistic evidence tying FKF1 to FT promoter regulation:** In Song et al. (2012), CDF1 overexpression reduced FT mRNA and delayed flowering; CDF1 bound FT promoter regions (amplicons 7, 8, 12, 13) at ZT4, and HA-CDF1 occupancy near the FT transcription start site persisted into the afternoon in fkf1 mutants, supporting that FKF1 activity is required to clear CDF1 from the promoter region at the appropriate time. (song2012fkf1conveystiming pages 1-2)

**CO stabilization timing information (LD afternoon):** FKF1 stabilizes CO protein in the LD afternoon (e.g., ZT12–16 window), and FKF1 and CO co-associate near the FT transcription start site, consistent with direct control of FT induction timing. (song2012fkf1conveystiming pages 2-4, song2012fkf1conveystiming media 412dd69c)

**COP1 pathway modulation:** FKF1 contributes to photoperiodic control by inhibiting COP1 homodimerization (in LD afternoon when FKF1 is light-activated), preventing COP1-dependent CO degradation; genetic epistasis supports COP1 downstream of FKF1. (lee2017thefboxprotein pages 1-2, lee2017thefboxprotein pages 7-8)

### 3.2 Circadian roles (strength and limits)

FKF1 is discussed as part of a family (ZTL/FKF1/LKP2) involved in ubiquitin-mediated degradation of clock proteins, with review-level statements indicating that in the dark ZTL (and FKF1/LKP2) interact with TOC1 and PRR5 and promote proteasome-dependent degradation. However, within the retrieved evidence, **FKF1 appears more central to flowering/photoperiodic regulation**, with circadian effects often described as **weaker/redundant** compared with ZTL/LKP2. Consequently, circadian-core annotations for FKF1 should be made conservatively unless supported by direct FKF1-specific experiments in the target organism. (ito2012lovdomaincontainingfbox pages 6-7, l2023sheddingnewlight pages 39-42, fujiwara2008novelbluelight pages 4-5)

## 4) Cellular localization and complexes

### 4.1 Subcellular localization

**Nucleus and cytosol:** Subcellular fractionation detected FKF1 in both cytosolic and nuclear fractions, supporting activity in both compartments. (song2012fkf1conveystiming pages 2-4)

This dual localization is consistent with FKF1’s functions: nuclear chromatin-associated regulation of FT/CO-related transcription (through clearing CDF repressors and CO promoter/proximal effects) and cytosolic/nuclear protein stability regulation (CO stabilization, COP1 interaction). (song2012fkf1conveystiming pages 2-4, lee2017thefboxprotein pages 7-8)

### 4.2 Complex membership

**SCF^FKF1 E3 ubiquitin ligase complex:** FKF1 purification recovered ASK1, ASK2, and CUL1 peptides, supporting in vivo association with SCF core subunits and the conclusion that FKF1 forms an SCF^FKF1 complex. (song2014distinctrolesof pages 1-2, song2014distinctrolesof pages 2-3)

**FKF1–GI complex:** Proteomics and co-IP/fractionation data indicate the FKF1–GI complex is present in both cytosolic and nuclear fractions throughout the day. (song2014distinctrolesof pages 2-2)

**FKF1–CO complex:** Co-immunoprecipitation demonstrates FKF1–CO interaction in planta; interaction is blue-light enhanced and depends on LOV photochemistry. (song2012fkf1conveystiming pages 2-4, song2012fkf1conveystiming media 04b014ef)

**FKF1–COP1 interaction:** FKF1 interacts with COP1 (RING domain) and inhibits COP1 homodimerization; fractionation suggests FKF1 alone does not drive COP1 light/dark movement, implying inhibition is more via complex formation/dimerization interference than via relocalization. (lee2017thefboxprotein pages 7-8)

## 5) Annotation-risk assessment (core vs context-specific)

### 5.1 Likely “core function” annotations (high confidence)

1. **Blue-light photoreceptor activity / LOV-domain FMN-binding photochemistry** (MF): strong mechanistic and quantitative photocycle evidence and blue-light-enhanced interaction behavior. (ito2012lovdomaincontainingfbox pages 4-5, song2012fkf1conveystiming pages 2-4)
2. **SCF ubiquitin ligase complex component / F-box protein function** (MF/CC): ASK/CUL1 association by TAP-MS and functional dependence on F-box–ASK interaction mutations. (song2014distinctrolesof pages 2-3, song2012fkf1conveystiming pages 2-4)
3. **Substrate recognition and ubiquitin-dependent degradation of CDF repressors** (MF/BP): supported by binding via Kelch repeats and promoter occupancy/genetic evidence linking FKF1 to clearing CDF1 from FT promoter region. (ito2012lovdomaincontainingfbox pages 4-5, song2012fkf1conveystiming pages 1-2)
4. **Photoperiodic flowering regulation (LD) via CO/FT induction** (BP): multiple genetic and mechanistic studies; corroborated by 2024 synthesis. (song2012fkf1conveystiming pages 1-2, wang2024circadianandphotoperiodic pages 3-4)

### 5.2 Context-specific or potentially over-extended annotations (moderate-to-high risk)

1. **“Circadian clock regulation” in a core oscillator sense** (BP): FKF1-family members can influence clock protein stability in the dark, but FKF1’s dominant experimentally characterized role in this evidence set is flowering/photoperiod; circadian-core annotations should be conservative and ideally supported by FKF1-specific clock phenotyping and/or direct degradation evidence for TOC1/PRR5 by FKF1. (ito2012lovdomaincontainingfbox pages 6-7, l2023sheddingnewlight pages 39-42)
2. **Over-broad developmental categories** (BP): phenotypes such as hypocotyl elongation rhythms and leaf movements can be downstream of altered circadian/photoperiodic signaling and ubiquitin-mediated proteostasis. Use care not to treat pleiotropic phenotypes as direct FKF1 biochemical roles without mechanistic evidence. (ito2012lovdomaincontainingfbox pages 4-5, l2023sheddingnewlight pages 39-42)

### 5.3 Excluded processes (no support in retrieved evidence)

No retrieved FKF1/ADO3 sources provide evidence linking FKF1 to **apoptosis, neuronal roles, inflammatory signaling, pyroptosis, or synaptic remodeling**; the literature frames FKF1 as a plant photoreceptor/E3-ligase adaptor acting in flowering/circadian/light signaling networks. Such annotations should not be applied for Arabidopsis FKF1 in GO unless new, direct plant evidence is identified. (cho2024disruptingfkf1homodimerization pages 1-2, lee2017thefboxprotein pages 1-2, ito2012lovdomaincontainingfbox pages 4-5, l2023sheddingnewlight pages 39-42)

## 6) Key literature (with dates, URLs)

**Recent (priority 2023–2024)**

1. Cho SW *et al.* (Apr 2024). *Plant Cell Reports.* “Disrupting FKF1 homodimerization increases FT transcript levels in the evening by enhancing CO stabilization.” DOI: https://doi.org/10.1007/s00299-024-03207-w (cho2024disruptingfkf1homodimerization pages 4-6, cho2024disruptingfkf1homodimerization pages 1-2)
2. Wang F, Han T, Chen ZJ (May 2024). *Communications Biology.* “Circadian and photoperiodic regulation of the vegetative to reproductive transition in plants.” DOI: https://doi.org/10.1038/s42003-024-06275-6 (wang2024circadianandphotoperiodic pages 3-4)
3. Lummer CL (2023). “Shedding new light on a core concept: Elucidating the roles of photoreceptors in the Arabidopsis circadian rhythm using phenomics, proteomics, and metabolomics.” DOI: https://doi.org/10.7939/r3-rz2q-z656 (l2023sheddingnewlight pages 39-42)

**Foundational primary studies**

4. Song YH *et al.* (May 2012). *Science.* “FKF1 conveys timing information for CONSTANS stabilization in photoperiodic flowering.” DOI: https://doi.org/10.1126/science.1219644 (song2012fkf1conveystiming pages 2-4, song2012fkf1conveystiming media 04b014ef, song2012fkf1conveystiming media 412dd69c)
5. Song YH *et al.* (Nov 2014). *PNAS.* “Distinct roles of FKF1, GIGANTEA, and ZEITLUPE proteins in the regulation of CONSTANS stability in Arabidopsis photoperiodic flowering.” DOI: https://doi.org/10.1073/pnas.1415375111 (song2014distinctrolesof pages 2-3)
6. Lee BD *et al.* (Dec 2017). *Nature Communications.* “The F-box protein FKF1 inhibits dimerization of COP1 in the control of photoperiodic flowering.” DOI: https://doi.org/10.1038/s41467-017-02476-2 (lee2017thefboxprotein pages 7-8)
7. Ito S, Song YH, Imaizumi T (May 2012). *Molecular Plant.* “LOV domain-containing F-box proteins: light-dependent protein degradation modules in Arabidopsis.” DOI: https://doi.org/10.1093/mp/sss013 (ito2012lovdomaincontainingfbox pages 4-5)

---

## Evidence summary table

| GO aspect | Proposed GO term/phrase | Key evidence statement | Mechanism/substrate | Experimental system & method | Conditions/time (LD/SD, ZT, blue light) | Key quantitative/statistical detail (if present) | Primary citation (authors, year, journal) | DOI URL |
|---|---|---|---|---|---|---|---|---|
| MF | blue-light photoreceptor activity; FMN binding; LOV-domain photochemistry | FKF1 is a LOV-domain blue-light receptor whose LOV domain binds flavin and undergoes light-dependent conformational change; after blue-light exposure FKF1 interacts with GI. FKF1 forms at least homodimers and has an unusually slow dark recovery. (ito2012lovdomaincontainingfbox pages 4-5) | FMN/LOV photocycle; light-triggered activation of GI binding | In vitro photochemistry and structural/biochemical analysis summarized from primary work; review synthesis | Blue light; dark reversion at room temperature | FKF1 LOV S390→D450 dark reversion half-life ~62.5 h; deletion of a 9-aa loop accelerated recovery to ~20.9 h (~3-fold faster). (ito2012lovdomaincontainingfbox pages 4-5) | Ito, Song & Imaizumi, 2012, *Molecular Plant* | https://doi.org/10.1093/mp/sss013 |
| MF/CC | SCF-type E3 ubiquitin ligase complex component; F-box protein binding ASK/SKP1 and CUL1 | FKF1 contains an F-box that interacts with ASK proteins and TAP-MS recovered ASK1, ASK2, and CUL1 with FKF1, strongly indicating FKF1 forms an SCF^FKF1 complex in vivo. (song2014distinctrolesof pages 1-2, song2014distinctrolesof pages 2-2, song2014distinctrolesof pages 2-3, ito2012lovdomaincontainingfbox pages 4-5) | SCF adaptor/substrate receptor within SCF^FKF1 | Arabidopsis transgenic FKF1-3F6H purification; TAP-MS/IP-MS; prior ASK interaction data; F-box mutant affecting ASK1 binding | Diurnal sampling including ZT13; LD/SD contexts in associated experiments | No stoichiometric values provided in excerpt; peptide recovery ranked GI second after FKF1 in pulldowns. (song2014distinctrolesof pages 2-2) | Song et al., 2014, *PNAS* | https://doi.org/10.1073/pnas.1415375111 |
| MF/BP | substrate recognition of CDF repressors; ubiquitin-dependent degradation of CDF1 | FKF1 binds CDF1 through its Kelch repeat domain and mediates CDF degradation, relieving repression of CO/FT transcription; CDF1 overexpression reduces FT mRNA and delays flowering, and CDF1 occupancy at the FT promoter persists in fkf1 mutants in the afternoon. (ito2012lovdomaincontainingfbox pages 4-5, song2012fkf1conveystiming pages 1-2) | Kelch-repeat substrate recognition of CDF1/CDF family repressors; proteasome-targeting via SCF^FKF1 | Arabidopsis genetics, overexpression, ChIP at FT promoter, interaction assays summarized in primary study/review | Long days; morning ZT4 for promoter occupancy; afternoon persistence in fkf1; blue-light-dependent GI-FKF1 module | Specific FT promoter amplicons 7, 8, 12, 13 bound by CDF1 at ZT4; afternoon HA-CDF1 retention near FT TSS in fkf1. (song2012fkf1conveystiming pages 1-2) | Song et al., 2012, *Science*; Ito et al., 2012, *Molecular Plant* | https://doi.org/10.1126/science.1219644 |
| MF/BP | blue-light-enhanced protein binding to CONSTANS (CO); positive regulation of CO stability | FKF1 directly interacts with CO, with the LOV domain sufficient for interaction; blue light enhances FKF1-CO binding, and photochemically blind LOV mutants weaken the interaction. F-box mutations abolishing ASK1 binding attenuate blue-light effects. FKF1 stabilizes CO in the long-day afternoon. (song2012fkf1conveystiming pages 1-2, song2012fkf1conveystiming pages 2-4, song2012fkf1conveystiming media 04b014ef) | Direct FKF1-CO binding via LOV (and LOV+F) plus SCF-associated contribution to CO stabilization | Co-IP in transgenic Arabidopsis and *Nicotiana benthamiana*; domain mapping; LOV photochemical mutants C91A/R92D/Q163L; F-box mutants L214A/I223A; ChIP/co-association near FT promoter | Blue vs red light; LD afternoon; ZT12–16; ZT13 for promoter co-association | Interaction significantly greater in blue than red light; fkf1 causes reduced afternoon CO abundance and lower FT mRNA in CO overexpressor backgrounds. (song2012fkf1conveystiming pages 2-4, song2012fkf1conveystiming media 04b014ef) | Song et al., 2012, *Science* | https://doi.org/10.1126/science.1219644 |
| MF/BP | COP1 binding; negative regulation of COP1 homodimerization; positive regulation of CO stability | FKF1 interacts with COP1, primarily via the COP1 RING domain, and inhibits COP1 homodimerization, thereby reducing COP1-dependent CO degradation and promoting flowering in LD. Genetic epistasis places COP1 downstream of FKF1. (lee2017thefboxprotein pages 1-2, lee2017thefboxprotein pages 7-8) | FKF1-COP1 interaction blocks COP1 E3 activity toward CO; likely competition at RING/dimer interface | Yeast two-hybrid, in vivo/transient interaction assays, mutant analysis, overexpression, genetic epistasis (cop1-4 fkf1-t) | Long days, afternoon, light-activated FKF1; weak/no action in SD after dusk | No strong effect on COP1 stability reported; cop1-4 fkf1-t flowers as early as cop1-4. (lee2017thefboxprotein pages 1-2) | Lee et al., 2017, *Nature Communications* | https://doi.org/10.1038/s41467-017-02476-2 |
| CC | nucleus and cytosol localization; active in both compartments | FKF1 is detected in both cytosolic and nuclear fractions; FKF1-GI complexes are present in both fractions throughout the day, and CO-FKF1 interaction is strong in both fractions. (song2014distinctrolesof pages 2-2, song2012fkf1conveystiming pages 2-4, song2014distinctrolesof pages 2-3) | Dual-compartment function in CO stabilization and GI-associated flowering control | Arabidopsis subcellular fractionation; co-IP/TAP-IP from cytosolic- and nuclear-enriched fractions | Across the day; ZT-series including ZT13; LD/SD in associated experiments | Qualitative fractionation evidence; no compartment percentage values reported. (song2014distinctrolesof pages 2-2, song2012fkf1conveystiming pages 2-4) | Song et al., 2012, *Science*; Song et al., 2014, *PNAS* | https://doi.org/10.1126/science.1219644 |
| BP/MF | regulation of FKF1 dimerization modulates CO stabilization, FT expression, and flowering time | A LOV-domain I160R substitution disrupting FKF1 homodimerization increased evening FT transcript, enhanced GI and COP1 interaction, elevated afternoon CO, and promoted earlier flowering when expressed in fkf1 plants, despite lower FKF1 protein abundance. (cho2024disruptingfkf1homodimerization pages 1-2, cho2024disruptingfkf1homodimerization pages 4-6) | Altered homo-/heterodimerization state fine-tunes GI/COP1/CO outputs | In vitro dimerization analysis; transgenic Arabidopsis complementation lines under FKF1 promoter; co-IP in tobacco and Arabidopsis phenotyping | Long days; afternoon/evening around dusk; blue-light photoreceptor context | I160R preserved WT-like photochemistry but lowered protein accumulation and still increased evening FT and accelerated flowering; excerpts do not provide exact p-values. (cho2024disruptingfkf1homodimerization pages 4-6, cho2024disruptingfkf1homodimerization pages 1-2) | Cho et al., 2024, *Plant Cell Reports* | https://doi.org/10.1007/s00299-024-03207-w |
| BP | circadian-clock protein degradation in the dark (TOC1/PRR5); annotation should be cautious for FKF1 specifically | Review-level evidence states that in the dark, ZTL (and FKF1/LKP2) interact with TOC1 and PRR5 and degrade them through the proteasome pathway; however, stronger direct modern evidence emphasizes ZTL/LKP2 as principal regulators, with FKF1 contributing more weakly or redundantly to clock control than to flowering. (ito2012lovdomaincontainingfbox pages 6-7, l2023sheddingnewlight pages 39-42, fujiwara2008novelbluelight pages 4-5) | Putative/redundant targeting of TOC1 and PRR5 within ZTL/FKF1/LKP2 family | Review synthesis of earlier family studies; comparative genetic interpretation | Dark conditions; circadian context rather than photoperiodic flowering output | No FKF1-specific quantitative degradation statistic in provided excerpts; 2023 review notes FKF1 role in core circadian regulation is weaker than ZTL and period effects are clearer in combined mutants. (l2023sheddingnewlight pages 39-42, fujiwara2008novelbluelight pages 4-5) | Ito et al., 2012, *Molecular Plant*; Lummer, 2023, thesis/review text | https://doi.org/10.1093/mp/sss013 |


*Table: This table summarizes the strongest GO-relevant evidence for Arabidopsis FKF1/ADO3 across molecular function, biological process, and cellular component. It highlights where support is direct and strong versus where annotations should be made cautiously because evidence is more redundant or review-level.*

## Figure evidence (blue-light enhanced FKF1–CO interaction and model)

Song et al. (2012) includes co-IP panels demonstrating FKF1–CO interaction and quantification showing increased complex formation under blue light relative to red/other conditions, and a model summarizing the feed-forward mechanism (CDF degradation plus CO stabilization) by which FKF1 regulates FT induction and flowering time. (song2012fkf1conveystiming media 04b014ef, song2012fkf1conveystiming media 412dd69c)


References

1. (ito2012lovdomaincontainingfbox pages 4-5): Shogo Ito, Young Hun Song, and Takato Imaizumi. Lov domain-containing f-box proteins: light-dependent protein degradation modules in arabidopsis. Molecular plant, 5 3:573-82, May 2012. URL: https://doi.org/10.1093/mp/sss013, doi:10.1093/mp/sss013. This article has 271 citations and is from a highest quality peer-reviewed journal.

2. (song2012fkf1conveystiming pages 1-2): Young Hun Song, Robert W. Smith, Benjamin J. To, Andrew J. Millar, and Takato Imaizumi. Fkf1 conveys timing information for constans stabilization in photoperiodic flowering. Science, 336:1045-1049, May 2012. URL: https://doi.org/10.1126/science.1219644, doi:10.1126/science.1219644. This article has 575 citations and is from a highest quality peer-reviewed journal.

3. (song2014distinctrolesof pages 1-2): Young Hun Song, Daniel A. Estrada, Richard S. Johnson, Somi K. Kim, Sang Yeol Lee, Michael J. MacCoss, and Takato Imaizumi. Distinct roles of fkf1, gigantea, and zeitlupe proteins in the regulation of constans stability in arabidopsis photoperiodic flowering. Proceedings of the National Academy of Sciences, 111:17672-17677, Nov 2014. URL: https://doi.org/10.1073/pnas.1415375111, doi:10.1073/pnas.1415375111. This article has 228 citations and is from a highest quality peer-reviewed journal.

4. (song2012fkf1conveystiming pages 2-4): Young Hun Song, Robert W. Smith, Benjamin J. To, Andrew J. Millar, and Takato Imaizumi. Fkf1 conveys timing information for constans stabilization in photoperiodic flowering. Science, 336:1045-1049, May 2012. URL: https://doi.org/10.1126/science.1219644, doi:10.1126/science.1219644. This article has 575 citations and is from a highest quality peer-reviewed journal.

5. (lee2017thefboxprotein pages 1-2): Byoung-Doo Lee, Mi Ri Kim, Min-Young Kang, Joon-Yung Cha, Su-Hyun Han, Ganesh M. Nawkar, Yasuhito Sakuraba, Sang Yeol Lee, Takato Imaizumi, C. Robertson McClung, Woe-Yeon Kim, and Nam-Chon Paek. The f-box protein fkf1 inhibits dimerization of cop1 in the control of photoperiodic flowering. Nature Communications, Dec 2017. URL: https://doi.org/10.1038/s41467-017-02476-2, doi:10.1038/s41467-017-02476-2. This article has 108 citations and is from a highest quality peer-reviewed journal.

6. (lee2017thefboxprotein pages 7-8): Byoung-Doo Lee, Mi Ri Kim, Min-Young Kang, Joon-Yung Cha, Su-Hyun Han, Ganesh M. Nawkar, Yasuhito Sakuraba, Sang Yeol Lee, Takato Imaizumi, C. Robertson McClung, Woe-Yeon Kim, and Nam-Chon Paek. The f-box protein fkf1 inhibits dimerization of cop1 in the control of photoperiodic flowering. Nature Communications, Dec 2017. URL: https://doi.org/10.1038/s41467-017-02476-2, doi:10.1038/s41467-017-02476-2. This article has 108 citations and is from a highest quality peer-reviewed journal.

7. (cho2024disruptingfkf1homodimerization pages 4-6): Sung Won Cho, Jameela Lokhandwala, Jun Sang Park, Hye Won Kang, Mingi Choi, Hong-Quan Yang, Takato Imaizumi, Brian D. Zoltowski, and Young Hun Song. Disrupting fkf1 homodimerization increases ft transcript levels in the evening by enhancing co stabilization. Plant Cell Reports, Apr 2024. URL: https://doi.org/10.1007/s00299-024-03207-w, doi:10.1007/s00299-024-03207-w. This article has 12 citations and is from a peer-reviewed journal.

8. (cho2024disruptingfkf1homodimerization pages 1-2): Sung Won Cho, Jameela Lokhandwala, Jun Sang Park, Hye Won Kang, Mingi Choi, Hong-Quan Yang, Takato Imaizumi, Brian D. Zoltowski, and Young Hun Song. Disrupting fkf1 homodimerization increases ft transcript levels in the evening by enhancing co stabilization. Plant Cell Reports, Apr 2024. URL: https://doi.org/10.1007/s00299-024-03207-w, doi:10.1007/s00299-024-03207-w. This article has 12 citations and is from a peer-reviewed journal.

9. (l2023sheddingnewlight pages 39-42): Christina L Lummer. Shedding new light on a core concept: elucidating the roles of photoreceptors in the arabidopsis circadian rhythm using phenomics, proteomics, and metabolomics. Text, 2023. URL: https://doi.org/10.7939/r3-rz2q-z656, doi:10.7939/r3-rz2q-z656. This article has 0 citations and is from a peer-reviewed journal.

10. (song2014distinctrolesof pages 2-3): Young Hun Song, Daniel A. Estrada, Richard S. Johnson, Somi K. Kim, Sang Yeol Lee, Michael J. MacCoss, and Takato Imaizumi. Distinct roles of fkf1, gigantea, and zeitlupe proteins in the regulation of constans stability in arabidopsis photoperiodic flowering. Proceedings of the National Academy of Sciences, 111:17672-17677, Nov 2014. URL: https://doi.org/10.1073/pnas.1415375111, doi:10.1073/pnas.1415375111. This article has 228 citations and is from a highest quality peer-reviewed journal.

11. (song2012fkf1conveystiming media 04b014ef): Young Hun Song, Robert W. Smith, Benjamin J. To, Andrew J. Millar, and Takato Imaizumi. Fkf1 conveys timing information for constans stabilization in photoperiodic flowering. Science, 336:1045-1049, May 2012. URL: https://doi.org/10.1126/science.1219644, doi:10.1126/science.1219644. This article has 575 citations and is from a highest quality peer-reviewed journal.

12. (wang2024circadianandphotoperiodic pages 3-4): Fang Wang, Tongwen Han, and Z. Jeffrey Chen. Circadian and photoperiodic regulation of the vegetative to reproductive transition in plants. Communications Biology, May 2024. URL: https://doi.org/10.1038/s42003-024-06275-6, doi:10.1038/s42003-024-06275-6. This article has 60 citations and is from a peer-reviewed journal.

13. (song2012fkf1conveystiming media 412dd69c): Young Hun Song, Robert W. Smith, Benjamin J. To, Andrew J. Millar, and Takato Imaizumi. Fkf1 conveys timing information for constans stabilization in photoperiodic flowering. Science, 336:1045-1049, May 2012. URL: https://doi.org/10.1126/science.1219644, doi:10.1126/science.1219644. This article has 575 citations and is from a highest quality peer-reviewed journal.

14. (ito2012lovdomaincontainingfbox pages 6-7): Shogo Ito, Young Hun Song, and Takato Imaizumi. Lov domain-containing f-box proteins: light-dependent protein degradation modules in arabidopsis. Molecular plant, 5 3:573-82, May 2012. URL: https://doi.org/10.1093/mp/sss013, doi:10.1093/mp/sss013. This article has 271 citations and is from a highest quality peer-reviewed journal.

15. (fujiwara2008novelbluelight pages 4-5): Sumire Fujiwara. Novel blue light receptors with an f-box: their direct control of the circadian clock and the flowering timing in arabidopsis. Plant Biotechnology, 25:123-129, Mar 2008. URL: https://doi.org/10.5511/plantbiotechnology.25.123, doi:10.5511/plantbiotechnology.25.123. This article has 9 citations and is from a peer-reviewed journal.

16. (song2014distinctrolesof pages 2-2): Young Hun Song, Daniel A. Estrada, Richard S. Johnson, Somi K. Kim, Sang Yeol Lee, Michael J. MacCoss, and Takato Imaizumi. Distinct roles of fkf1, gigantea, and zeitlupe proteins in the regulation of constans stability in arabidopsis photoperiodic flowering. Proceedings of the National Academy of Sciences, 111:17672-17677, Nov 2014. URL: https://doi.org/10.1073/pnas.1415375111, doi:10.1073/pnas.1415375111. This article has 228 citations and is from a highest quality peer-reviewed journal.