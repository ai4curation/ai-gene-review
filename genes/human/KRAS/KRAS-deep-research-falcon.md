---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T22:38:45.982323'
end_time: '2026-05-12T23:03:05.379101'
duration_seconds: 1459.4
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

Concise GO annotation research for human KRAS / UniProt P01116 (K-Ras isoforms KRAS4A and KRAS4B). Focus only on GO-relevant evidence: core molecular function as a Ras-family small GTPase with GDP/GTP binding and GTP hydrolysis; GEF/GAP-regulated nucleotide cycling; effector binding in the GTP-bound state; core biological processes Ras protein signal transduction, MAPK cascade/positive regulation of MAPK cascade, PI3K/AKT/mTOR signaling where directly supported; isoform-specific membrane targeting of KRAS4A and KRAS4B including farnesylation, palmitoylation/fatty acylation, polybasic region, PDEdelta-mediated trafficking, plasma membrane/endosomal/Golgi localization; distinguish wild-type KRAS core function from oncogenic mutant phenotypes, cancer, proliferation, senescence, apoptosis, transcription, development, and immune/metabolic downstream outcomes; evaluate generic protein binding, G protein activity vs GTPase activity, protein-membrane adaptor activity, and over-annotation risks from pathway membership or mutant studies. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human KRAS / UniProt P01116 (K-Ras isoforms KRAS4A and KRAS4B). Focus only on GO-relevant evidence: core molecular function as a Ras-family small GTPase with GDP/GTP binding and GTP hydrolysis; GEF/GAP-regulated nucleotide cycling; effector binding in the GTP-bound state; core biological processes Ras protein signal transduction, MAPK cascade/positive regulation of MAPK cascade, PI3K/AKT/mTOR signaling where directly supported; isoform-specific membrane targeting of KRAS4A and KRAS4B including farnesylation, palmitoylation/fatty acylation, polybasic region, PDEdelta-mediated trafficking, plasma membrane/endosomal/Golgi localization; distinguish wild-type KRAS core function from oncogenic mutant phenotypes, cancer, proliferation, senescence, apoptosis, transcription, development, and immune/metabolic downstream outcomes; evaluate generic protein binding, G protein activity vs GTPase activity, protein-membrane adaptor activity, and over-annotation risks from pathway membership or mutant studies. Include PMID/DOI citations and keep under 1500 words.

## Concise GO-annotation research report: Human KRAS (UniProt P01116; KRAS4A/KRAS4B)

### Scope and GO-caution framing
This report summarizes **GO-relevant evidence** for the *wild-type* (WT) KRAS molecular switch function (GDP/GTP cycling, effector engagement) and **isoform-specific membrane targeting** of KRAS4A versus KRAS4B. It explicitly avoids over-annotation from (i) pathway membership, (ii) overexpression systems, and (iii) oncogenic-mutant phenotypes unless the claim is a direct biochemical consequence of the mutation that is relevant to the core switch mechanism. Recent expert reviews emphasize that a “bona fide” RAS effector must **bind directly and nucleotide-dependently** and **alter effector activity**, and that domain presence (e.g., an RBD/RA motif) is insufficient without experimental validation. (smith2023definingbonefide pages 1-2, mozzarelli2024functionalandstructural pages 1-3)

### 1) Key concepts and definitions (GO-relevant)
**KRAS is a Ras-family small GTPase** that functions as a GDP/GTP-regulated switch. GTP binding induces conformational changes in **switch I/II** regions enabling effector recognition, while GTP hydrolysis returns KRAS to the GDP-bound state. (jesus2023targetingkrasin pages 2-4, ahearn2012regulatingtheregulator pages 2-4, pacold2000crystalstructureand pages 1-2)

**GEF/GAP-regulated nucleotide cycling** is central to KRAS function: GEFs (e.g., SOS) promote GDP release and GTP loading; GAPs accelerate hydrolysis, in part via an “arginine finger” mechanism. (nair2023regulationofrasgtpase pages 1-2, boriacksjodin1998thestructuralbasis pages 1-2, hall2001structurebasedmutagenesisreveals pages 1-2, scheffzek1998gtpaseactivatingproteinshelping pages 1-2)

### 2) Recent developments (prioritizing 2023–2024)
**Effector definition and over-annotation risk (2023–2024):** Reviews stress that many proteins labeled “effectors” lack mechanistic proof (nucleotide dependence + functional consequence), and that kinetics/competition among effectors and local concentrations shape outputs—critical for avoiding BP over-annotation from correlation. (smith2023definingbonefide pages 1-2, mozzarelli2024functionalandstructural pages 1-3)

**Mutant-specific biochemical bias (2023–2024):** Recent analyses summarize that different KRAS hotspot variants can differ in intrinsic hydrolysis and RAF affinity, producing *variant-dependent* pathway bias; therefore “KRAS activates X pathway” statements require direct evidence in the relevant context and should not be inferred from a single mutant or tumor dataset. (mondal2024krasmutationsubtypes pages 10-12, jani2024insightintostructural pages 16-17)

### 3) Core molecular function evidence (MF)
#### GDP/GTP binding and intrinsic GTPase activity
A widely cited expert synthesis reports Ras intrinsic hydrolysis is slow (**kcat ≈ 2×10−4 s−1**), but it is a real enzymatic activity central to the molecular switch. (ahearn2012regulatingtheregulator pages 2-4)

#### GAP-stimulated hydrolysis
GAPs accelerate Ras hydrolysis (reported up to ~10^5-fold in expert synthesis) and do so by complementing the active site, including an **external arginine** (“arginine finger”) concept; importantly, Gly12 oncogenic mutants are classically noted to resist such stimulation. (ahearn2012regulatingtheregulator pages 2-4, scheffzek1998gtpaseactivatingproteinshelping pages 1-2)

#### GEF-catalyzed nucleotide exchange (SOS)
Primary structural evidence for Ras activation by SOS comes from the crystal structure of Ras in complex with the SOS catalytic region, indicating SOS stabilizes Ras in a **nucleotide-free** state, a mechanistic basis for GEF-driven exchange. (Boriack-Sjodin et al., *Nature* 1998-07; DOI/URL: https://doi.org/10.1038/28548) (boriacksjodin1998thestructuralbasis pages 1-2)

Structure-guided mutagenesis further shows **distinct roles for Ras switch I vs switch II**: switch II interactions largely anchor Ras to SOS, while switch I perturbation disrupts the nucleotide-binding site to promote GDP dissociation. (Hall et al., *JBC* 2001-07; DOI/URL: https://doi.org/10.1074/jbc.M101727200) (hall2001structurebasedmutagenesisreveals pages 1-2)

#### Effector binding in the GTP-bound state
A primary structural and functional demonstration of Ras effector engagement is the Ras–PI3Kγ complex: PI3Kγ is directly activated by GTP-loaded Ras, and the structure shows Ras uses **switch I/II** to bind the PI3Kγ Ras-binding domain. (Pacold et al., *Cell* 2000-12; DOI/URL: https://doi.org/10.1016/S0092-8674(00)00196-3) (pacold2000crystalstructureand pages 1-2)

### 4) Core biological processes (BP) supported without overreach
**Ras protein signal transduction** is the safest high-level BP annotation because it directly follows from nucleotide cycling and effector engagement (WT function). (nair2023regulationofrasgtpase pages 1-2, jesus2023targetingkrasin pages 4-6)

**Positive regulation of MAPK cascade (RAS→RAF→MEK→ERK):** Reviews of KRAS mechanism and signaling connect KRAS-GTP effector binding to RAF-family activation and MAPK signaling; however, expert cautions emphasize that “pathway membership” or overexpression is insufficient, and that effector engagement is limited by a single RBD-binding site per RAS at a given time. (jesus2023targetingkrasin pages 4-6)

**PI3K signaling / PI3K–AKT–mTOR signaling:** Direct biochemical/structural evidence supports Ras→PI3K effector binding and activation (PI3Kγ is a clear case). Extending to downstream AKT/mTOR should be done only where direct KRAS–PI3K effector evidence and context-specific functional readouts exist, not solely from tumor omics or mutant phenotypes. (pacold2000crystalstructureand pages 1-2, jesus2023targetingkrasin pages 4-6)

### 5) Isoform-specific membrane targeting and localization (CC/BP)
KRAS4A and KRAS4B differ almost exclusively in their **C-terminal hypervariable region (HVR)**, which controls membrane binding, trafficking routes, and compartmental signaling. (Rossi et al., *Biochem Soc Trans* 2023-05; DOI/URL: https://doi.org/10.1042/bst20221347) (rossi2023differentialfunctionsof pages 9-10)

**Shared CAAX processing and farnesylation:** Both isoforms are farnesylated at the CAAX cysteine and further processed (RCE1 cleavage and ICMT methylation) in the ER, enabling membrane association. (Cox et al., *Clin Cancer Res* 2015-04; DOI/URL: https://doi.org/10.1158/1078-0432.CCR-14-3214) (cox2015targetingrasmembrane pages 2-4)

**KRAS4A palmitoylation / fatty-acylation:** KRAS4A contains a palmitoylation site (Cys180) enabling reversible palmitoylation-dependent Golgi trafficking. Expert synthesis notes that farnesylation + palmitoylation can increase membrane affinity by **>100-fold** and acts as a Golgi “affinity trap” promoting vesicular delivery to the plasma membrane. (Ahearn et al., *Nat Rev Mol Cell Biol* 2012-12; DOI/URL: https://doi.org/10.1038/nrm3255) (ahearn2012regulatingtheregulator pages 5-7)

**KRAS4B polybasic region:** KRAS4B lacks palmitoylatable cysteines and instead uses a lysine-rich polybasic HVR (reported net charge **+8**) to electrostatically stabilize plasma membrane association with anionic lipids. (ahearn2012regulatingtheregulator pages 5-7)

**PDE6D (PDEδ) trafficking/chaperoning:** KRAS4B (and depalmitoylated prenylated cargo) can bind PDE6D to shield its prenyl group and support trafficking between endomembranes and plasma membrane. Quantitatively summarized evidence indicates that loss of KRAS4B carboxymethylation reduces PDE6D affinity by **>35-fold**, and a Ser181 phosphomimic (S181E) reduces affinity by **>6-fold**. (kaya2023characterizationofnovel pages 23-27)

A curated schematic comparing KRAS4A vs KRAS4B trafficking and compartmental localization (including PDE6D for KRAS4B and palmitoylation cycling for KRAS4A) is available in the Rossi 2023 review. (rossi2023differentialfunctionsof media 2c8748fc)

### 6) Wild-type vs oncogenic mutant phenotypes: what to annotate and what to avoid
Oncogenic KRAS mutations (e.g., G12/G13/Q61) can reduce intrinsic and/or GAP-stimulated hydrolysis and shift conformational state populations, thereby sustaining effector engagement; however, downstream phenotypes (proliferation, senescence, apoptosis, transcriptional programs, developmental and immune/metabolic outcomes) are highly context dependent and often derived from mutant/overexpression models. These should not be propagated as WT KRAS GO BP annotations without direct WT evidence. (jesus2023targetingkrasin pages 4-6, mondal2024krasmutationsubtypes pages 10-12, jani2024insightintostructural pages 16-17, mozzarelli2024functionalandstructural pages 22-23)

### 7) Real-world implementations relevant to GO curation (evidence-use perspective)
Therapeutic strategies targeting membrane association/trafficking (e.g., CAAX processing inhibitors, PDE6D inhibitors) and effector interaction surfaces demonstrate that localization and effector engagement are mechanistically separable axes of KRAS biology; this reinforces the need for GO annotations to separate **core MF (GTPase switch)** from **contextual disease phenotypes**. (cox2015targetingrasmembrane pages 2-4, kaya2023characterizationofnovel pages 23-27)

### 8) Key statistics and data (context, not for over-annotation)
*Effector landscape:* prediction-based summaries report **56 RBD-containing Ras effectors**, and emphasize that **each RAS molecule has one RBD-binding site** such that only one effector binds at a time. (jesus2023targetingkrasin pages 4-6)

*Cancer context:* KRAS mutations are reported as present in ~**22% of cancers** (contextual prevalence, not a functional annotation). (smith2023definingbonefide pages 1-2)

*PDAC context:* in a compiled dataset (n=1552), **>90%** of PDAC tumors harbor KRAS mutations; the majority are at **G12 (90%)** and **Q61 (7%)**, with reported G12D 36–45%, G12V 28–39%, G12R 12–21%, and G12C 0–4%. (jesus2023targetingkrasin pages 4-6)

---

### GO evidence map (artifact)
| GO aspect | Recommended GO term label | Evidence summary (1 line) | Key refs (DOI/URL + year; PMID if explicit) | Annotation cautions |
|---|---|---|---|---|
| MF | GTP binding | KRAS is a Ras-family small GTPase whose active state is GTP-bound, with switch I/II conformational changes underlying signaling competence (jesus2023targetingkrasin pages 2-4, ahearn2012regulatingtheregulator pages 2-4, kewagamang2024therelationshipbetween pages 25-28) | Boriack-Sjodin et al. 1998, https://doi.org/10.1038/28548; Jesus et al. 2023, https://doi.org/10.3390/cancers15205015 | Prefer specific nucleotide binding over generic “G protein activity”; do not infer altered affinity from oncogenic mutants alone. |
| MF | GDP binding | KRAS also binds GDP as the inactive nucleotide-bound state; GDP/GTP cycling is the core switch mechanism (jesus2023targetingkrasin pages 2-4, nair2023regulationofrasgtpase pages 1-2, kewagamang2024therelationshipbetween pages 25-28) | Nair & Saha 2023, https://doi.org/10.3390/kinasesphosphatases1020007; Jesus et al. 2023, https://doi.org/10.3390/cancers15205015 | Annotate GDP binding separately from GTPase activity; avoid conflating inactive GDP-bound state with loss of function. |
| MF | GTPase activity | Ras has intrinsic GTP hydrolysis activity; catalytic turnover is low but real, central to KRAS molecular function (mozzarelli2024functionalandstructural pages 1-3, ahearn2012regulatingtheregulator pages 5-7, ahearn2012regulatingtheregulator pages 2-4) | Mozzarelli et al. 2024, https://doi.org/10.1016/j.molcel.2024.06.027; Ahearn et al. 2012, https://doi.org/10.1038/nrm3255 | Use “GTPase activity,” not broad “G protein activity”; mutant-impaired hydrolysis should not redefine WT function. |
| MF | Ras guanine nucleotide exchange factor binding / GEF-regulated nucleotide exchange | SOS binds nucleotide-free Ras and distorts switch regions to promote GDP release and GTP loading, establishing GEF-regulated cycling (boriacksjodin1998thestructuralbasis pages 1-2, hall2001structurebasedmutagenesisreveals pages 1-2) | Boriack-Sjodin et al. 1998, https://doi.org/10.1038/28548; Hall et al. 2001, https://doi.org/10.1074/jbc.M101727200 | Evidence supports regulation by GEFs; avoid annotating KRAS itself as a GEF. Use direct biochemical/structural evidence, not pathway membership. |
| MF | Ras GTPase-activating protein binding / GAP-stimulated GTP hydrolysis | GAPs accelerate KRAS hydrolysis by complementing the active site with an arginine finger; oncogenic codon-12 mutants resist this stimulation (ahearn2012regulatingtheregulator pages 2-4, scheffzek1998gtpaseactivatingproteinshelping pages 1-2) | Scheffzek et al. 1998, https://doi.org/10.1016/S0968-0004(98)01224-9; Ahearn et al. 2012, https://doi.org/10.1038/nrm3255 | Good support for GAP-regulated hydrolysis, but avoid mutant-centric annotations as WT properties; do not annotate generic “protein binding.” |
| MF | Effector binding (RAF/PI3K) in GTP-bound state | Bona fide effectors must bind GTP-bound Ras directly and change effector activity; structural work shows Ras·GTP engages PI3Kγ through switch I/II (smith2023definingbonefide pages 1-2, mozzarelli2024functionalandstructural pages 1-3, pacold2000crystalstructureand pages 1-2) | Smith 2023, https://doi.org/10.1002/bies.202300088; Mozzarelli et al. 2024, https://doi.org/10.1016/j.molcel.2024.06.027; Pacold et al. 2000, https://doi.org/10.1016/S0092-8674(00)00196-3 | Avoid annotating generic “protein binding”; require nucleotide dependence and functional consequence. Presence of an RBD/RA domain alone is insufficient. |
| BP | Ras protein signal transduction | Core WT role is Ras signal transduction via nucleotide cycling and effector engagement downstream of receptor inputs (jesus2023targetingkrasin pages 2-4, nair2023regulationofrasgtpase pages 1-2, jesus2023targetingkrasin pages 4-6) | Nair & Saha 2023, https://doi.org/10.3390/kinasesphosphatases1020007; Jesus et al. 2023, https://doi.org/10.3390/cancers15205015 | This is the safest high-level BP term; avoid importing cancer, proliferation, apoptosis, immune, or metabolic outcomes from mutant studies. |
| BP | Positive regulation of MAPK cascade | KRAS-GTP directly engages RAF-family effectors, supporting upstream positive regulation of the RAF-MEK-ERK/MAPK cascade (jesus2023targetingkrasin pages 4-6, ahearn2012regulatingtheregulator pages 2-4) | Jesus et al. 2023, https://doi.org/10.3390/cancers15205015; Ahearn et al. 2012, https://doi.org/10.1038/nrm3255 | Use when direct KRAS→RAF/MAPK evidence is available; avoid assigning all downstream transcriptional/developmental outputs to KRAS WT core function. |
| BP | PI3K signaling / positive regulation of PI3K-AKT-mTOR signaling | Ras directly binds and activates PI3Kγ structurally and biochemically, supporting PI3K pathway annotation where direct effector evidence exists (jesus2023targetingkrasin pages 4-6, pacold2000crystalstructureand pages 1-2) | Pacold et al. 2000, https://doi.org/10.1016/S0092-8674(00)00196-3; Jesus et al. 2023, https://doi.org/10.3390/cancers15205015 | Prefer direct Ras–PI3K evidence; be cautious with broad AKT/mTOR annotations inferred only from mutant tumors or indirect pathway studies. |
| BP | Protein prenylation / farnesylation-dependent membrane targeting | All KRAS isoforms undergo CAAX processing with farnesylation, followed by RCE1/ICMT processing, enabling membrane association (cox2015targetingrasmembrane pages 2-4, ahearn2012regulatingtheregulator pages 5-7) | Cox et al. 2015, https://doi.org/10.1158/1078-0432.CCR-14-3214; Ahearn et al. 2012, https://doi.org/10.1038/nrm3255 | This is primarily PTM/localization biology, not a unique signaling output; avoid overextending to disease phenotypes. |
| BP | Protein palmitoylation / fatty-acylation (KRAS4A-specific) | KRAS4A, unlike KRAS4B, carries a palmitoylatable cysteine and can undergo reversible acylation that promotes Golgi-dependent trafficking (rossi2023differentialfunctionsof pages 9-10, cox2015targetingrasmembrane pages 2-4, ahearn2012regulatingtheregulator pages 5-7) | Rossi et al. 2023, https://doi.org/10.1042/BST20221347; Cox et al. 2015, https://doi.org/10.1158/1078-0432.CCR-14-3214; Ahearn et al. 2012, https://doi.org/10.1038/nrm3255 | Isoform-specific: do not propagate palmitoylation to KRAS4B. Some fatty-acylation studies use oncogenic constructs; keep WT/isoform boundaries clear. |
| CC | Plasma membrane | KRAS signaling-competent pools localize predominantly to the inner leaflet of the plasma membrane; KRAS4B uses its polybasic HVR, KRAS4A uses lipidation plus HVR features (rossi2023differentialfunctionsof pages 9-10, cox2015targetingrasmembrane pages 2-4, ahearn2012regulatingtheregulator pages 5-7) | Rossi et al. 2023, https://doi.org/10.1042/BST20221347; Cox et al. 2015, https://doi.org/10.1158/1078-0432.CCR-14-3214 | Strong CC annotation is justified, but avoid assuming exclusive PM residence because KRAS also traffics through endomembranes. |
| CC | Golgi / endosome / ER membranes | KRAS cycles through endomembranes: KRAS4A via palmitoylation-dependent Golgi trafficking; KRAS4B can shuttle among ER/Golgi/endosomal membranes during solubilization and recycling (rossi2023differentialfunctionsof pages 9-10, cox2015targetingrasmembrane pages 2-4, rossi2023differentialfunctionsof media 2c8748fc) | Rossi et al. 2023, https://doi.org/10.1042/BST20221347; Cox et al. 2015, https://doi.org/10.1158/1078-0432.CCR-14-3214 | Use broader endomembrane/Golgi annotations cautiously and preferably with isoform-resolved evidence; localization may be transient and context dependent. |
| BP/CC | PDE6D-mediated trafficking / prenyl-dependent solubilization | PDE6D binds the KRAS prenyl group and supports solubilization/trafficking of especially KRAS4B between endomembranes and the plasma membrane; affinity is reduced >35-fold without carboxymethylation and >6-fold by S181E phosphomimic (rossi2023differentialfunctionsof pages 9-10, kaya2023characterizationofnovel pages 23-27) | Rossi et al. 2023, https://doi.org/10.1042/BST20221347; quantitative summary citing Dharmaiah et al. 2016 in pqac-00000025 | Useful for trafficking/localization curation, but avoid annotating KRAS as having “protein-membrane adaptor activity.” This is transport/chaperone-assisted localization, not an intrinsic adaptor MF. |


*Table: This table maps GO-relevant functions, processes, and localizations for human KRAS (P01116) to concise evidence summaries and key sources. It is designed to support careful annotation while flagging common over-annotation risks, especially from mutant or generic pathway data.*

### Practical annotation guidance (summary)
1) Prefer specific MF terms (**GTP binding**, **GDP binding**, **GTPase activity**) over generic “G protein activity/protein binding.” (ahearn2012regulatingtheregulator pages 2-4, smith2023definingbonefide pages 1-2)
2) Add regulatory interaction terms (GEF/GAP-related) only with direct mechanistic evidence (e.g., SOS structural/functional evidence). (boriacksjodin1998thestructuralbasis pages 1-2, hall2001structurebasedmutagenesisreveals pages 1-2, scheffzek1998gtpaseactivatingproteinshelping pages 1-2)
3) Annotate MAPK/PI3K processes when supported by direct effector interaction/activation evidence; avoid inferring broad downstream phenotypes from mutant tumor biology. (pacold2000crystalstructureand pages 1-2, jesus2023targetingkrasin pages 4-6, mozzarelli2024functionalandstructural pages 22-23)
4) Use isoform-specific CC/BP annotations for KRAS4A palmitoylation trafficking vs KRAS4B polybasic/PDE6D-mediated trafficking; do not propagate palmitoylation to KRAS4B. (ahearn2012regulatingtheregulator pages 5-7, kaya2023characterizationofnovel pages 23-27, rossi2023differentialfunctionsof media 2c8748fc)


References

1. (smith2023definingbonefide pages 1-2): Matthew J. Smith. Defining bone fide effectors of ras gtpases. BioEssays, Jul 2023. URL: https://doi.org/10.1002/bies.202300088, doi:10.1002/bies.202300088. This article has 11 citations and is from a peer-reviewed journal.

2. (mozzarelli2024functionalandstructural pages 1-3): Alessandro M. Mozzarelli, Dhirendra K. Simanshu, and Pau Castel. Functional and structural insights into ras effector proteins. Molecular Cell, 84:2807-2821, Aug 2024. URL: https://doi.org/10.1016/j.molcel.2024.06.027, doi:10.1016/j.molcel.2024.06.027. This article has 35 citations and is from a highest quality peer-reviewed journal.

3. (jesus2023targetingkrasin pages 2-4): Victor Hugo Fonseca de Jesus, Maria Cecília Mathias-Machado, João Paulo Fogacci de Farias, Marcelo Porfirio Sunagua Aruquipa, Alexandre A. Jácome, and Renata D’Alpino Peixoto. Targeting kras in pancreatic ductal adenocarcinoma: the long road to cure. Cancers, 15:5015, Oct 2023. URL: https://doi.org/10.3390/cancers15205015, doi:10.3390/cancers15205015. This article has 42 citations.

4. (ahearn2012regulatingtheregulator pages 2-4): Ian M. Ahearn, Kevin Haigis, Dafna Bar-Sagi, and Mark R. Philips. Regulating the regulator: post-translational modification of ras. Nature Reviews Molecular Cell Biology, 13:39-51, Dec 2012. URL: https://doi.org/10.1038/nrm3255, doi:10.1038/nrm3255. This article has 749 citations and is from a domain leading peer-reviewed journal.

5. (pacold2000crystalstructureand pages 1-2): Michael E. Pacold, Sabine Suire, Olga Perisic, Samuel Lara-Gonzalez, Colin T. Davis, Edward H. Walker, Phillip T. Hawkins, Len Stephens, John F. Eccleston, and Roger L. Williams. Crystal structure and functional analysis of ras binding to its effector phosphoinositide 3-kinase γ. Cell, 103:931-944, Dec 2000. URL: https://doi.org/10.1016/s0092-8674(00)00196-3, doi:10.1016/s0092-8674(00)00196-3. This article has 843 citations and is from a highest quality peer-reviewed journal.

6. (nair2023regulationofrasgtpase pages 1-2): Arathi Nair and Bhaskar Saha. Regulation of ras-gtpase signaling and localization by post-translational modifications. Kinases and Phosphatases, 1:97-116, Apr 2023. URL: https://doi.org/10.3390/kinasesphosphatases1020007, doi:10.3390/kinasesphosphatases1020007. This article has 7 citations.

7. (boriacksjodin1998thestructuralbasis pages 1-2): P. Ann Boriack-Sjodin, S. Mariana Margarit, Dafna Bar-Sagi, and John Kuriyan. The structural basis of the activation of ras by sos. Nature, 394:337-343, Jul 1998. URL: https://doi.org/10.1038/28548, doi:10.1038/28548. This article has 1134 citations and is from a highest quality peer-reviewed journal.

8. (hall2001structurebasedmutagenesisreveals pages 1-2): Brian E. Hall, Shao Song Yang, P. Ann Boriack-Sjodin, John Kuriyan, and Dafna Bar-Sagi. Structure-based mutagenesis reveals distinct functions for ras switch 1 and switch 2 in sos-catalyzed guanine nucleotide exchange*. The Journal of Biological Chemistry, 276:27629-27637, Jul 2001. URL: https://doi.org/10.1074/jbc.m101727200, doi:10.1074/jbc.m101727200. This article has 181 citations.

9. (scheffzek1998gtpaseactivatingproteinshelping pages 1-2): Klaus Scheffzek, Mohammad Reza Ahmadian, and Alfred Wittinghofer. Gtpase-activating proteins: helping hands to complement an active site. Trends in biochemical sciences, 23 7:257-62, Jul 1998. URL: https://doi.org/10.1016/s0968-0004(98)01224-9, doi:10.1016/s0968-0004(98)01224-9. This article has 590 citations and is from a domain leading peer-reviewed journal.

10. (mondal2024krasmutationsubtypes pages 10-12): Koushik Mondal, Mahesh Kumar Posa, Revathi P. Shenoy, and Susanta Roychoudhury. Kras mutation subtypes and their association with other driver mutations in oncogenic pathways. Cells, 13:1221, Jul 2024. URL: https://doi.org/10.3390/cells13141221, doi:10.3390/cells13141221. This article has 45 citations.

11. (jani2024insightintostructural pages 16-17): Vinod Jani, Uddhavesh Sonavane, and Rajendra Joshi. Insight into structural dynamics involved in activation mechanism of full length kras wild type and p-loop mutants. Heliyon, 10:e36161, Aug 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e36161, doi:10.1016/j.heliyon.2024.e36161. This article has 7 citations.

12. (jesus2023targetingkrasin pages 4-6): Victor Hugo Fonseca de Jesus, Maria Cecília Mathias-Machado, João Paulo Fogacci de Farias, Marcelo Porfirio Sunagua Aruquipa, Alexandre A. Jácome, and Renata D’Alpino Peixoto. Targeting kras in pancreatic ductal adenocarcinoma: the long road to cure. Cancers, 15:5015, Oct 2023. URL: https://doi.org/10.3390/cancers15205015, doi:10.3390/cancers15205015. This article has 42 citations.

13. (rossi2023differentialfunctionsof pages 9-10): Juan Kochen Rossi, Cristina Nuevo-Tapioles, and Mark R. Philips. Differential functions of the kras splice variants. Biochemical Society transactions, 51:1191-1199, May 2023. URL: https://doi.org/10.1042/bst20221347, doi:10.1042/bst20221347. This article has 9 citations and is from a peer-reviewed journal.

14. (cox2015targetingrasmembrane pages 2-4): Adrienne D. Cox, Channing J. Der, and Mark R. Philips. Targeting ras membrane association: back to the future for anti-ras drug discovery? Clinical Cancer Research, 21:1819-1827, Apr 2015. URL: https://doi.org/10.1158/1078-0432.ccr-14-3214, doi:10.1158/1078-0432.ccr-14-3214. This article has 448 citations and is from a highest quality peer-reviewed journal.

15. (ahearn2012regulatingtheregulator pages 5-7): Ian M. Ahearn, Kevin Haigis, Dafna Bar-Sagi, and Mark R. Philips. Regulating the regulator: post-translational modification of ras. Nature Reviews Molecular Cell Biology, 13:39-51, Dec 2012. URL: https://doi.org/10.1038/nrm3255, doi:10.1038/nrm3255. This article has 749 citations and is from a domain leading peer-reviewed journal.

16. (kaya2023characterizationofnovel pages 23-27): P KAYA. Characterization of novel inhibitors of the trafficking chaperone pde6d. Unknown journal, 2023.

17. (rossi2023differentialfunctionsof media 2c8748fc): Juan Kochen Rossi, Cristina Nuevo-Tapioles, and Mark R. Philips. Differential functions of the kras splice variants. Biochemical Society transactions, 51:1191-1199, May 2023. URL: https://doi.org/10.1042/bst20221347, doi:10.1042/bst20221347. This article has 9 citations and is from a peer-reviewed journal.

18. (mozzarelli2024functionalandstructural pages 22-23): Alessandro M. Mozzarelli, Dhirendra K. Simanshu, and Pau Castel. Functional and structural insights into ras effector proteins. Molecular Cell, 84:2807-2821, Aug 2024. URL: https://doi.org/10.1016/j.molcel.2024.06.027, doi:10.1016/j.molcel.2024.06.027. This article has 35 citations and is from a highest quality peer-reviewed journal.

19. (kewagamang2024therelationshipbetween pages 25-28): K Kewagamang. The relationship between oncogenic kras and wild-type ras activity and signaling. Unknown journal, 2024.

## Citations

1. ahearn2012regulatingtheregulator pages 2-4
2. boriacksjodin1998thestructuralbasis pages 1-2
3. hall2001structurebasedmutagenesisreveals pages 1-2
4. pacold2000crystalstructureand pages 1-2
5. jesus2023targetingkrasin pages 4-6
6. rossi2023differentialfunctionsof pages 9-10
7. cox2015targetingrasmembrane pages 2-4
8. ahearn2012regulatingtheregulator pages 5-7
9. kaya2023characterizationofnovel pages 23-27
10. smith2023definingbonefide pages 1-2
11. mozzarelli2024functionalandstructural pages 1-3
12. jesus2023targetingkrasin pages 2-4
13. nair2023regulationofrasgtpase pages 1-2
14. scheffzek1998gtpaseactivatingproteinshelping pages 1-2
15. mondal2024krasmutationsubtypes pages 10-12
16. jani2024insightintostructural pages 16-17
17. mozzarelli2024functionalandstructural pages 22-23
18. kewagamang2024therelationshipbetween pages 25-28
19. https://doi.org/10.1038/28548
20. https://doi.org/10.1074/jbc.M101727200
21. https://doi.org/10.1016/S0092-8674(00
22. https://doi.org/10.1042/bst20221347
23. https://doi.org/10.1158/1078-0432.CCR-14-3214
24. https://doi.org/10.1038/nrm3255
25. https://doi.org/10.1038/28548;
26. https://doi.org/10.3390/cancers15205015
27. https://doi.org/10.3390/kinasesphosphatases1020007;
28. https://doi.org/10.1016/j.molcel.2024.06.027;
29. https://doi.org/10.1016/S0968-0004(98
30. https://doi.org/10.1002/bies.202300088;
31. https://doi.org/10.3390/cancers15205015;
32. https://doi.org/10.1158/1078-0432.CCR-14-3214;
33. https://doi.org/10.1042/BST20221347;
34. https://doi.org/10.1002/bies.202300088,
35. https://doi.org/10.1016/j.molcel.2024.06.027,
36. https://doi.org/10.3390/cancers15205015,
37. https://doi.org/10.1038/nrm3255,
38. https://doi.org/10.1016/s0092-8674(00
39. https://doi.org/10.3390/kinasesphosphatases1020007,
40. https://doi.org/10.1038/28548,
41. https://doi.org/10.1074/jbc.m101727200,
42. https://doi.org/10.1016/s0968-0004(98
43. https://doi.org/10.3390/cells13141221,
44. https://doi.org/10.1016/j.heliyon.2024.e36161,
45. https://doi.org/10.1042/bst20221347,
46. https://doi.org/10.1158/1078-0432.ccr-14-3214,