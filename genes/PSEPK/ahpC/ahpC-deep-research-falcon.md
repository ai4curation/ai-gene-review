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
- **UniProt Accession:** Q88K52
- **Protein Description:** RecName: Full=Alkyl hydroperoxide reductase C {ECO:0000256|ARBA:ARBA00017462, ECO:0000256|RuleBase:RU366004}; EC=1.11.1.26 {ECO:0000256|ARBA:ARBA00013021, ECO:0000256|RuleBase:RU366004}; AltName: Full=Peroxiredoxin {ECO:0000256|ARBA:ARBA00032077, ECO:0000256|RuleBase:RU366004}; AltName: Full=Thioredoxin peroxidase {ECO:0000256|ARBA:ARBA00032824, ECO:0000256|RuleBase:RU366004};
- **Gene Information:** Name=ahpC {ECO:0000313|EMBL:AAN68051.1}; OrderedLocusNames=PP_2439 {ECO:0000313|EMBL:AAN68051.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peroxiredoxin family. AhpC/Prx1 subfamily.
- **Key Domains:** AhpC. (IPR017559); AhpC/TSA. (IPR000866); Peroxiredoxin. (IPR050217); Peroxiredoxin_AhpC-typ. (IPR024706); Peroxiredoxin_C. (IPR019479)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ahpC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ahpC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ahpC** (gene ID: ahpC, UniProt: Q88K52) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: *ahpC* (UniProt Q88K52; locus PP_2439) in *Pseudomonas putida* KT2440

### 1) Target verification (gene/protein identity)
The research target is **alkyl hydroperoxide reductase C (AhpC)**, a **peroxiredoxin-family** thiol peroxidase, encoded by **ahpC** with ordered locus name **PP_2439** in *Pseudomonas putida* KT2440, matching the user-provided UniProt context for Q88K52. This locus assignment is explicitly used in oxidative-stress transcriptomics for KT2440 (Table 2 lists **ahpC = PP_2439** and **ahpF = PP_2440**). (bojanovic2017globaltranscriptionalresponses pages 10-11, bojanovic2017globaltranscriptionalresponses media 03a7ec25)

### 2) Key concepts and definitions (current understanding)

#### 2.1 AhpC as a bacterial peroxiredoxin (AhpC/Prx1 subfamily)
AhpC is the **peroxidatic** component (“C” subunit) of the bacterial **alkyl hydroperoxide reductase (Ahp) system**, belonging to the **peroxiredoxin** family. In *P. putida*, AhpC is observed as an abundant **soluble ~24 kDa** protein and is predicted/confirmed to be a **2-Cys peroxiredoxin** with conserved cysteines (e.g., **Cys47 and Cys166** in KT2442 AhpC), consistent with the canonical Prx catalytic cycle. (fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 3-4)

#### 2.2 Enzymatic reaction and substrate specificity
**Reaction (functional definition):** AhpC catalyzes the **reduction of hydroperoxides** (ROOH, including organic hydroperoxides and H2O2) to the corresponding products (ROH + H2O, for alkyl hydroperoxides). In *P. putida* KT2442, AhpC is described as reducing **alkyl hydroperoxides to the corresponding alcohol**, with oxidized AhpC then being recycled by AhpF. (fukumori2001molecularcloningand pages 6-8)

**Substrate preference in *P. putida* evidence:** Experimental phenotypes and expression studies in KT2442 indicate AhpC is especially important for **organic hydroperoxide** detoxification; hydrogen peroxide was reported as potentially **not the preferred substrate** for the *P. putida* AHPR system in the KT2442 context (e.g., AhpC overexpression increased resistance to t‑butyl hydroperoxide but did not similarly improve H2O2 resistance). (fukumori2001molecularcloningand pages 6-8, fukumori2001molecularcloningand pages 3-4)

**General peroxiredoxin perspective:** A dedicated review and *P. putida*-focused oxidative-stress review describe AhpC as a high-affinity peroxide detoxification tool (qualitatively “very low Km” for hydroperoxides is noted), but those sources do not provide numeric kinetic constants for *P. putida* AhpC in the retrieved text. (hishinuma2006oxyrregulatedthe pages 1-2, kim2014oxidativestressresponse pages 5-6)

#### 2.3 Electron donor system and catalytic cycling (AhpF/NADH)
In *P. putida*, the AhpC catalytic cycle is coupled to a dedicated reductase **AhpF**, characterized as a **flavoprotein/disulfide reductase** that uses **NADH** as the reducing equivalent to restore AhpC from its oxidized form. This NADH dependence is repeatedly emphasized and is a key mechanistic constraint: the AhpCF system may be less suited for detoxifying very large peroxide loads because the peroxidase must be continually re-reduced at the expense of reducing equivalents. (hishinuma2006oxyrregulatedthe pages 1-2, kim2014oxidativestressresponse pages 5-6)

Consistent with this electron-transfer role, *P. putida* KT2442 AhpF is predicted to have conserved **FAD-binding** and **NAD(P)H-binding** motifs/domains typical of electron-transfer flavoenzymes, supporting an electron flow **NAD(P)H → AhpF → AhpC → peroxide**. (fukumori2001molecularcloningand pages 4-6)

### 3) Pathway context: operon organization and regulation

#### 3.1 Operon organization and transcriptional architecture (ahpCF)
In *P. putida* KT2442 (closely related to KT2440), **ahpC and ahpF are adjacent and co-transcribed** as an **ahpCF operon**, but with **strong differential accumulation** of transcripts/proteins.

Key evidence includes:
- a predominant **~0.7 kb** transcript corresponding largely to **ahpC**, and a less abundant **~2.7 kb** transcript consistent with **ahpCF** co-transcription. (fukumori2001molecularcloningand pages 4-6, dubbs2007peroxiredoxinsinbacterial pages 9-12)
- evidence for **transcriptional attenuation** between ahpC and ahpF: a stem-loop structure in the intergenic region can reduce readthrough to ahpF, explaining lower AhpF accumulation; deletion of this stem-loop increases ahpF expression. (fukumori2001molecularcloningand pages 6-8, fukumori2001molecularcloningand pages 4-6)
- mapped transcription start sites: in KT2442, ahpC transcription initiates from **two closely spaced starts** (**P1 at −37; P2 at −28** relative to the start site), and expression is reported as **RpoS-independent** (transcripts present even in an rpoS mutant). (hishinuma2006oxyrregulatedthe pages 6-7)

#### 3.2 OxyR-controlled oxidative stress regulon
A central regulatory concept is that **OxyR** serves as a peroxide-sensing transcriptional regulator that controls antioxidant genes including **ahpC**.

Direct regulatory evidence in *P. putida* includes:
- **OxyR binds the ahpC promoter region** (gel shift/binding evidence). (hishinuma2006oxyrregulatedthe pages 1-2)
- mechanistic model: reduced OxyR can bind the promoter, while oxidized OxyR is linked to transcriptional activation (e.g., via interaction with RNA polymerase). (hishinuma2006oxyrregulatedthe pages 6-7)
- **oxyR1 point mutation**: in KT2442TOL, a point mutation in oxyR (Phe106→Ile is described for oxyR1) is associated with **constitutively increased AhpC expression**, consistent with an altered redox-sensing/activation state. (fukumori2001molecularcloningand pages 6-8, fukumori2001molecularcloningand pages 1-3)

### 4) Cellular localization and site of action
Experimental fractionation in *P. putida* KT2442 recovered AhpC as a **soluble protein** in the **soluble fraction**, supporting a **cytosolic** site of action where intracellular hydroperoxides are detoxified. No evidence in the retrieved sources supports secretion or a membrane-anchored localization for AhpC. (fukumori2001molecularcloningand pages 3-4)

### 5) Physiological roles, phenotypes, and quantitative data

#### 5.1 Organic peroxide resistance and solvent-associated stress tolerance (KT2442 studies)
In KT2442/KT2442TOL, AhpC is induced by oxidants and contributes to resistance to **organic hydroperoxides**:
- The 24-kDa AhpC-like protein is inducibly produced by **H2O2** or **t‑butyl hydroperoxide (BHP)** supplementation (but not by toluene alone in the parental strain). (fukumori2001molecularcloningand pages 3-4)
- Disk diffusion phenotypes show markedly increased resistance to BHP in the toluene-adapted strain (smaller zone = more resistant): **BHP zone** KT2442 **30 ± 2 mm**, KT2442TOL **14 ± 1 mm**, and oxyR revertant KT2442TOL-oxyR **30 ± 2 mm**. In contrast, **H2O2 zones** were similar across strains (**23 ± 1**, **24 ± 1**, **25 ± 1 mm**, respectively), supporting a more prominent AhpC role in organic peroxide defense than in bulk H2O2 detoxification under those conditions. (fukumori2001molecularcloningand pages 3-4)
- A toluene colony-formation phenotype links oxyR/AhpC regulation to solvent stress adaptation: colony-forming ability under toluene decreased from **~92 ± 10%** (KT2442TOL) to **~51 ± 8%** (KT2442TOL-oxyR), consistent with a partial contribution of OxyR-controlled oxidative-stress defenses (including AhpC) to solvent-associated fitness. (fukumori2001molecularcloningand pages 6-8)

#### 5.2 Rapid induction by hydrogen peroxide in KT2440 (transcriptomics)
A genome-wide expression dataset for KT2440 exposed to hydrogen peroxide shows AhpC and AhpF are among the most strongly induced oxidative-stress genes early after exposure:
- **ahpC (PP_2439): 74.7-fold** induction at **7 min** (T1) and **2.3-fold** at **60 min** (T2).
- **ahpF (PP_2440): 203.4-fold** induction at **7 min** (T1) and **3.5-fold** at **60 min** (T2).
This time-resolved pattern indicates a rapid transcriptional spike followed by partial relaxation/adaptation. (bojanovic2017globaltranscriptionalresponses pages 10-11, bojanovic2017globaltranscriptionalresponses media 03a7ec25)

#### 5.3 qPCR evidence for strong OxyR1-dependent ahpC upregulation
In *P. putida* (OxyR study), qPCR Ct values indicate that an **oxyR1** background causes very strong elevation of ahpC transcript abundance across growth states. Reported Ct values include (LOG phase) **20.10 ± 0.34** (oxyR) vs **12.49 ± 0.75** (oxyR1), and (stationary) **15.16 ± 1.43** (oxyR) vs **10.67 ± 0.15** (oxyR1). The large Ct decreases imply very large fold-changes in transcript abundance (since each Ct approximates a doubling under ideal PCR efficiency). (hishinuma2006oxyrregulatedthe pages 6-7)

### 6) Recent developments (2023–2024) and emerging applications
Direct 2023–2024 primary studies centered specifically on **KT2440 AhpC biochemistry** were limited in the retrieved corpus. However, recent work in related environmental bacteria and applied contexts reinforces AhpC’s importance as part of oxidative-stress defense relevant to biotechnology.

#### 6.1 Bioremediation context: oxidative stress during aromatic compound degradation (2024)
A 2024 study in *Paraburkholderia xenovorans* (an environmental aromatic degrader) shows that aromatic degradation can trigger oxidative stress and upregulation of multiple detoxification enzymes, including **alkyl hydroperoxide reductase/peroxiredoxin components** among a broader antioxidant network. Importantly, the authors demonstrate a **real-world implementation**: overexpression of a redox protein (FldX1) improves degradation performance in **soil microcosms** (bioaugmentation) by mitigating oxidative stress, which in turn alters the need to induce antioxidant genes (including those in peroxide detoxification pathways). This supports the general translational principle that peroxide-defense modules like AhpC/AhpF are operationally important in field-relevant biodegradation scenarios, even when the specific organism differs from *P. putida*. (rodriguezcastro2024thelongchainflavodoxin pages 10-11)

### 7) Expert opinion and synthesis (authoritative analyses)
Two overarching expert interpretations emerge from reviews and *P. putida* regulatory work:
1. **AhpC is a high-affinity thiol peroxidase central to peroxide defense**, especially at low-to-moderate peroxide levels where peroxiredoxins can be highly effective scavengers. (hishinuma2006oxyrregulatedthe pages 1-2, kim2014oxidativestressresponse pages 5-6)
2. **Dependence on reductant supply (NADH via AhpF)** implies a potential limitation for coping with massive peroxide influx; thus, AhpC typically operates alongside catalases and other systems in a coordinated OxyR-controlled oxidative stress response. (hishinuma2006oxyrregulatedthe pages 1-2, kim2014oxidativestressresponse pages 5-6, bojanovic2017globaltranscriptionalresponses pages 10-11)

### 8) Evidence summary table
| Aspect | Key findings | Evidence type | Citations |
|---|---|---|---|
| Identity/domains | Target identity is consistent across sources: **ahpC = PP_2439** in *Pseudomonas putida* KT2440/KT2442, encoding a **small, soluble ~24 kDa alkyl hydroperoxide reductase subunit C/peroxiredoxin**. The protein is a **2-Cys peroxiredoxin** with conserved cysteines at positions **Cys47** and **Cys166**, matching the AhpC/Prx1 family assignment. | Primary study; review | (fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 1-3, bojanovic2017globaltranscriptionalresponses pages 10-11) |
| Reaction/substrates | AhpC is the **peroxidatic subunit** of alkyl hydroperoxide reductase and reduces **organic hydroperoxides to the corresponding alcohols**; it can also detoxify **H2O2**, but evidence in *P. putida* suggests **organic hydroperoxides are preferred substrates** and H2O2 may be less preferred. Reviews note very low Km values for hydroperoxides qualitatively, but no numeric kinetics were recovered here for *P. putida* AhpC. | Primary study; review | (hishinuma2006oxyrregulatedthe pages 1-2, fukumori2001molecularcloningand pages 6-8, kim2014oxidativestressresponse pages 5-6) |
| Electron donor/regeneration | Oxidized AhpC is regenerated by **AhpF**, the dedicated **NADH-dependent flavo-disulfide reductase/peroxiredoxin reductase**. AhpF contains conserved **FAD-binding** and **NAD(P)H-binding** motifs, supporting electron flow from **NADH → AhpF → AhpC → peroxide substrate**. | Primary study; review | (hishinuma2006oxyrregulatedthe pages 1-2, fukumori2001molecularcloningand pages 4-6, fukumori2001molecularcloningand pages 1-3, kim2014oxidativestressresponse pages 5-6) |
| Regulation | **OxyR directly regulates ahpC**. Purified OxyR binds upstream of ahpC; reduced OxyR can bind promoter DNA, whereas oxidized OxyR is linked to transcriptional activation. An **oxyR1** mutation causes constitutively elevated ahpC expression. | Primary study; review | (hishinuma2006oxyrregulatedthe pages 1-2, fukumori2001molecularcloningand pages 1-3, dubbs2007peroxiredoxinsinbacterial pages 9-12, hishinuma2006oxyrregulatedthe pages 6-7) |
| Operon/transcription | **ahpC and ahpF are co-transcribed** in an **ahpCF operon**. A major **~0.7 kb ahpC transcript** and a less abundant **~2.7 kb ahpCF transcript** were detected; an additional **~1.4 kb ahpF RNA** may arise from processing or a second promoter. A stem-loop between ahpC and ahpF likely attenuates downstream ahpF expression, explaining lower AhpF abundance. Transcription starts were mapped to two ahpC starts (**P1 = -37, P2 = -28**). | Primary study; review | (fukumori2001molecularcloningand pages 6-8, fukumori2001molecularcloningand pages 4-6, dubbs2007peroxiredoxinsinbacterial pages 9-12, hishinuma2006oxyrregulatedthe pages 6-7) |
| Localization | Experimental descriptions identify AhpC as a **soluble protein** recovered in the **soluble/cytosolic fraction**; no evidence here supports secretion or membrane localization. Function is therefore most parsimoniously assigned to the **cytosol**, where it detoxifies intracellular peroxides generated by metabolism or chemical stress. | Primary study; inference from fractionation/review | (fukumori2001molecularcloningand pages 1-3, fukumori2001molecularcloningand pages 3-4) |
| Physiological roles/phenotypes | AhpC contributes to **oxidative stress defense**, especially against **organic hydroperoxides**. In KT2442, induction occurred with **H2O2** or **t-butyl hydroperoxide (BHP)**, but not toluene alone. Overproduction of AhpC in the toluene-adapted strain correlated with improved BHP resistance: inhibition zones were **30 ± 2 mm** in KT2442, **14 ± 1 mm** in KT2442TOL, and **30 ± 2 mm** in the oxyR-revertant; H2O2 zones remained similar (**23 ± 1**, **24 ± 1**, **25 ± 1 mm**, respectively). Heterologous expression of *P. putida* ahpC partially protected *E. coli* against BHP but not H2O2. Reversion of oxyR reduced colony formation in toluene from **~92 ± 10%** in KT2442TOL to **~51 ± 8%** in KT2442TOL-oxyR, linking OxyR/AhpC overexpression with solvent-associated stress tolerance. | Primary study; review | (fukumori2001molecularcloningand pages 6-8, fukumori2001molecularcloningand pages 1-3, fukumori2001molecularcloningand pages 3-4, kim2014oxidativestressresponse pages 5-6) |
| Quantitative expression stats | Under H2O2 stress in KT2440, **ahpC (PP_2439)** increased **74.7-fold at 7 min** and **2.3-fold at 60 min**; **ahpF (PP_2440)** increased **203.4-fold at 7 min** and **3.5-fold at 60 min**. In an oxyR1 background, ahpC qPCR Ct values were **20.10 ± 0.34** (LOG oxyR) vs **12.49 ± 0.75** (LOG oxyR1), and **15.16 ± 1.43** (ST oxyR) vs **10.67 ± 0.15** (ST oxyR1), indicating very large transcript increases in oxyR1. | Primary study | (hishinuma2006oxyrregulatedthe pages 6-7, bojanovic2017globaltranscriptionalresponses pages 10-11, bojanovic2017globaltranscriptionalresponses media 03a7ec25) |


*Table: This table summarizes the core functional annotation for *Pseudomonas putida* AhpC (PP_2439; UniProt Q88K52), including enzymatic role, regulation, operon structure, localization, phenotypes, and quantitative expression evidence. It is useful as a compact evidence map linking the curated protein identity to experimental studies in *P. putida*.*

### 9) Key evidence figure/table
A cropped image of Table 2 reporting **H2O2-induced fold changes** for **ahpC (PP_2439)** and **ahpF (PP_2440)** at 7 min and 60 min is available for direct visual verification. (bojanovic2017globaltranscriptionalresponses media 03a7ec25)

### 10) Practical functional annotation (concise)
- **Primary molecular function:** thiol-dependent **peroxidase** reducing **organic hydroperoxides** (and H2O2 under some conditions) using the **AhpF/NADH** reducing system. (fukumori2001molecularcloningand pages 6-8, kim2014oxidativestressresponse pages 5-6)
- **Likely cellular compartment:** **cytosol/soluble fraction**. (fukumori2001molecularcloningand pages 3-4)
- **Pathway/regulon:** **OxyR-controlled oxidative stress regulon**; **ahpCF operon** with transcriptional attenuation influencing AhpF abundance. (fukumori2001molecularcloningand pages 4-6, dubbs2007peroxiredoxinsinbacterial pages 9-12, hishinuma2006oxyrregulatedthe pages 6-7)

### Limitations of the current evidence set
While core function and regulation of *P. putida* AhpC are strongly supported by classic primary literature and authoritative reviews, the retrieved corpus contained **few 2023–2024 studies directly focused on AhpC in *P. putida* KT2440** with detailed enzymology (e.g., Km/kcat for specific hydroperoxide substrates). Consequently, quantitative enzymatic kinetics for the specific Q88K52 protein are not reported here, and the “recent developments” section relies partly on 2024 work in a closely related environmental biodegradation context rather than *P. putida* KT2440 itself. (hishinuma2006oxyrregulatedthe pages 1-2, fukumori2001molecularcloningand pages 6-8, rodriguezcastro2024thelongchainflavodoxin pages 10-11)

References

1. (bojanovic2017globaltranscriptionalresponses pages 10-11): Klara Bojanovič, Isotta D'Arrigo, and Katherine S. Long. Global transcriptional responses to osmotic, oxidative, and imipenem stress conditions in pseudomonas putida. Applied and Environmental Microbiology, Apr 2017. URL: https://doi.org/10.1128/aem.03236-16, doi:10.1128/aem.03236-16. This article has 82 citations and is from a peer-reviewed journal.

2. (bojanovic2017globaltranscriptionalresponses media 03a7ec25): Klara Bojanovič, Isotta D'Arrigo, and Katherine S. Long. Global transcriptional responses to osmotic, oxidative, and imipenem stress conditions in pseudomonas putida. Applied and Environmental Microbiology, Apr 2017. URL: https://doi.org/10.1128/aem.03236-16, doi:10.1128/aem.03236-16. This article has 82 citations and is from a peer-reviewed journal.

3. (fukumori2001molecularcloningand pages 4-6): Fumiyasu Fukumori and Mitsuru Kishii. Molecular cloning and transcriptional analysis of the alkyl hydroperoxide reductase genes from pseudomonas putida kt2442. The Journal of general and applied microbiology, 47 5:269-277, Oct 2001. URL: https://doi.org/10.2323/jgam.47.269, doi:10.2323/jgam.47.269. This article has 21 citations.

4. (fukumori2001molecularcloningand pages 3-4): Fumiyasu Fukumori and Mitsuru Kishii. Molecular cloning and transcriptional analysis of the alkyl hydroperoxide reductase genes from pseudomonas putida kt2442. The Journal of general and applied microbiology, 47 5:269-277, Oct 2001. URL: https://doi.org/10.2323/jgam.47.269, doi:10.2323/jgam.47.269. This article has 21 citations.

5. (fukumori2001molecularcloningand pages 6-8): Fumiyasu Fukumori and Mitsuru Kishii. Molecular cloning and transcriptional analysis of the alkyl hydroperoxide reductase genes from pseudomonas putida kt2442. The Journal of general and applied microbiology, 47 5:269-277, Oct 2001. URL: https://doi.org/10.2323/jgam.47.269, doi:10.2323/jgam.47.269. This article has 21 citations.

6. (hishinuma2006oxyrregulatedthe pages 1-2): Sota Hishinuma, Masahiro Yuki, Makoto Fujimura, and Fumiyasu Fukumori. Oxyr regulated the expression of two major catalases, kata and katb, along with peroxiredoxin, ahpc in pseudomonas putida. Environmental microbiology, 8 12:2115-24, Dec 2006. URL: https://doi.org/10.1111/j.1462-2920.2006.01088.x, doi:10.1111/j.1462-2920.2006.01088.x. This article has 86 citations and is from a domain leading peer-reviewed journal.

7. (kim2014oxidativestressresponse pages 5-6): Jisun Kim and Woojun Park. Oxidative stress response in pseudomonas putida. Applied Microbiology and Biotechnology, 98:6933-6946, Jun 2014. URL: https://doi.org/10.1007/s00253-014-5883-4, doi:10.1007/s00253-014-5883-4. This article has 142 citations and is from a domain leading peer-reviewed journal.

8. (dubbs2007peroxiredoxinsinbacterial pages 9-12): James M. Dubbs and Skorn Mongkolsuk. Peroxiredoxins in bacterial antioxidant defense. Sub-cellular biochemistry, 44:143-93, Jan 2007. URL: https://doi.org/10.1007/978-1-4020-6051-9\_7, doi:10.1007/978-1-4020-6051-9\_7. This article has 133 citations.

9. (hishinuma2006oxyrregulatedthe pages 6-7): Sota Hishinuma, Masahiro Yuki, Makoto Fujimura, and Fumiyasu Fukumori. Oxyr regulated the expression of two major catalases, kata and katb, along with peroxiredoxin, ahpc in pseudomonas putida. Environmental microbiology, 8 12:2115-24, Dec 2006. URL: https://doi.org/10.1111/j.1462-2920.2006.01088.x, doi:10.1111/j.1462-2920.2006.01088.x. This article has 86 citations and is from a domain leading peer-reviewed journal.

10. (fukumori2001molecularcloningand pages 1-3): Fumiyasu Fukumori and Mitsuru Kishii. Molecular cloning and transcriptional analysis of the alkyl hydroperoxide reductase genes from pseudomonas putida kt2442. The Journal of general and applied microbiology, 47 5:269-277, Oct 2001. URL: https://doi.org/10.2323/jgam.47.269, doi:10.2323/jgam.47.269. This article has 21 citations.

11. (rodriguezcastro2024thelongchainflavodoxin pages 10-11): Laura Rodríguez-Castro, Roberto E. Durán, Valentina Méndez, Flavia Dorochesi, Daniela Zühlke, Katharina Riedel, and Michael Seeger. The long-chain flavodoxin fldx1 improves the biodegradation of 4-hydroxyphenylacetate and 3-hydroxyphenylacetate and counteracts the oxidative stress associated to aromatic catabolism in paraburkholderia xenovorans. Biological Research, Apr 2024. URL: https://doi.org/10.1186/s40659-024-00491-4, doi:10.1186/s40659-024-00491-4. This article has 6 citations and is from a peer-reviewed journal.