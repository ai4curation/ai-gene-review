---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T20:50:23.012624'
end_time: '2026-05-12T21:04:34.056373'
duration_seconds: 851.04
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

Concise GO annotation research for human HRAS / UniProt P01112 (GTPase HRas). Focus only on GO-relevant evidence: core molecular function as a small monomeric GTPase/GTP binding and GTP hydrolysis molecular switch; regulation by GEFs/GAPs; membrane targeting by CAAX prenylation/palmitoylation and plasma membrane/Golgi/endosome localization; Ras protein signal transduction and downstream RAF-MEK-ERK, PI3K-AKT, RalGDS and other effector pathways; evidence for positive regulation of MAPK cascade, cell proliferation/differentiation, actin cytoskeleton, apoptosis or senescence, and whether these should be core or non-core; protein binding annotations and specific effector binding terms; over-annotation risks for generic protein binding, broad cancer/development/cell cycle terms, transcriptional regulation, immune/inflammatory processes, and phenotypes from oncogenic mutants. Include caveats distinguishing normal HRAS function from oncogenic mutant/overexpression evidence. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human HRAS / UniProt P01112 (GTPase HRas). Focus only on GO-relevant evidence: core molecular function as a small monomeric GTPase/GTP binding and GTP hydrolysis molecular switch; regulation by GEFs/GAPs; membrane targeting by CAAX prenylation/palmitoylation and plasma membrane/Golgi/endosome localization; Ras protein signal transduction and downstream RAF-MEK-ERK, PI3K-AKT, RalGDS and other effector pathways; evidence for positive regulation of MAPK cascade, cell proliferation/differentiation, actin cytoskeleton, apoptosis or senescence, and whether these should be core or non-core; protein binding annotations and specific effector binding terms; over-annotation risks for generic protein binding, broad cancer/development/cell cycle terms, transcriptional regulation, immune/inflammatory processes, and phenotypes from oncogenic mutants. Include caveats distinguishing normal HRAS function from oncogenic mutant/overexpression evidence. Include PMID/DOI citations and keep under 1500 words.

## Concise GO annotation research report: Human HRAS (UniProt P01112, GTPase HRas)

### Scope and intent
This report summarizes *GO-relevant* experimental/review evidence for the core Molecular Function (MF), Cellular Component (CC), and Biological Process (BP) annotations of human **HRAS (P01112)**, focusing on its role as a small monomeric GTPase molecular switch; regulation by GEFs/GAPs; lipidation-driven membrane targeting and compartmental localization; and Ras signal transduction through canonical effectors (RAF–MEK–ERK, PI3K–AKT, RalGDS/Ral, RASSF). It also flags **over-annotation risks**, especially where evidence comes from **oncogenic mutants**, **overexpression**, or **high-throughput interactomics** without nucleotide-state validation.

### 1) Key concepts and definitions (current understanding)

#### 1.1 Core MF: small GTPase molecular switch
RAS proteins (including HRAS) are **GTP hydrolases** that function as **binary molecular switches**: GDP-bound is “OFF,” GTP-bound is “ON,” and the ON state supports binding to downstream effector proteins. Intrinsic GTPase activity is **accelerated by GAPs**, while **GEFs promote GDP→GTP exchange**. These are core, canonical features that directly support GO MF terms such as *GTP binding* and *GTPase activity* as well as BP terms such as *Ras protein signal transduction*. (smith2023definingbonefide pages 1-2, mozzarelli2024functionalandstructural pages 1-3)

A key GO-relevant principle is that **bona fide Ras effectors must bind RAS in a nucleotide-dependent manner (GTP-bound)** and that binding should change effector activity; domain presence alone is not sufficient for effector designation. (smith2023definingbonefide pages 1-2, mozzarelli2024functionalandstructural pages 1-3)

#### 1.2 Switch regions and nucleotide-dependent effector binding
RAS conformational changes occur prominently in **switch I (≈ residues 30–40) and switch II (≈ residues 60–68)**, and **GTP-bound RAS exposes these regions to enable effector association**, forming the mechanistic basis for GO “effector binding” annotations and for avoiding generic “protein binding.” (adariani2021acomprehensiveanalysis pages 1-4)

### 2) Cellular Component: membrane targeting and localization (CAAX processing, palmitoylation; PM/Golgi/endosomes)

#### 2.1 CAAX-driven prenylation and ER/Golgi processing (core)
HRAS contains a C-terminal **CAAX motif** that is post-translationally processed by a canonical sequence: **farnesylation → AAX proteolysis (RCE1) → carboxymethylation (ICMT)**. The post-prenylation processing machinery is localized to **endomembranes/ER**, and prenylation drives nascent Ras proteins to **ER and Golgi** before subsequent trafficking to the plasma membrane. (wright2006thematicreviewseries pages 2-3, choy1999endomembranetraffickingof pages 1-2)

Choy et al. (Cell, 1999-07; DOI: **10.1016/S0092-8674(00)80607-8**) provide mechanistic evidence that CAAX proteins are **targeted to ER/Golgi**, then transported onward, rather than being targeted directly from cytosol to the plasma membrane; for HRAS specifically, **palmitoylation upstream of CAAX is a secondary targeting signal required for efficient plasma membrane expression**. (choy1999endomembranetraffickingof pages 1-2)

#### 2.2 Palmitoylation-mediated membrane affinity, Golgi localization, and trafficking (core)
Palmitoylation provides the “second signal” for HRAS membrane targeting beyond prenylation and supports vesicular transport from **Golgi→plasma membrane**; palmitoylation is **reversible/dynamic**, supporting HRAS cycling between Golgi and plasma membrane. (wright2006thematicreviewseries pages 2-3, berthiaume2002insiderinformationhow pages 1-2, lynch2015thedifferentialpalmitoylation pages 1-3)

Lynch et al. (J Cell Physiol, 2015-03; DOI: **10.1002/jcp.24779**) describe H-Ras as **doubly palmitoylated** and distributed throughout Golgi stacks, with palmitoylation acting as an “affinity trap” in Golgi membranes and contributing to Golgi↔PM trafficking dynamics. (lynch2015thedifferentialpalmitoylation pages 1-3)

#### 2.3 Recycling endosome localization (supported but typically non-core)
Taguchi & Misaki (Small GTPases, 2011-03; DOI: **10.4161/sgtp.2.2.15245**) report that **palmitoylated H-Ras localizes to recycling endosomes**, proposed as a **way-station** in post-Golgi trafficking to the plasma membrane. This supports CC annotation to *recycling endosome* in contexts where HRAS endosomal trafficking is being curated. (taguchi2011palmitoylationpilotsras pages 1-3)

### 3) Biological Process: Ras signal transduction and downstream pathways; core vs non-core outcomes

#### 3.1 Core BP: Ras protein signal transduction; MAPK activation
RAS proteins sit at the apex of the **RAF–MEK–ERK (MAPK) cascade**, and Ras-effector binding directly routes signals into MAPK outputs. Dynamic features of Ras–ERK signaling can encode distinct biological outcomes (e.g., proliferation vs differentiation) depending on stimulus duration/feedback. (kolch2023dynamicregulationof pages 1-2, kolch2023dynamicregulationof pages 11-11)

Kolch et al. (Biochem J, 2023-01; DOI: **10.1042/BCJ20220234**) specifically note that **HRAS produces higher baseline ERK activity than wild-type KRAS** in comparative RAS-less MEF reconstitution experiments, supporting HRAS contribution to MAPK cascade activation (while still emphasizing that dynamics/feedback regulate phenotypic outcomes). (kolch2023dynamicregulationof pages 12-13)

**Annotation guidance:** “Ras protein signal transduction” and “positive regulation of MAPK cascade” are generally **core** for HRAS, but very specific outcome terms (e.g., “cell cycle progression” as a default) should be restricted to contexts with strong, direct, wild-type evidence.

#### 3.2 PI3K–AKT pathway as a canonical Ras output (core, with context qualifiers)
PI3K is a recognized Ras effector pathway. Kolch et al. emphasize that **effector selection depends on active RAS concentration**: high-affinity effectors dominate at low RAS-GTP levels, while **lower-affinity partners (including PI3K) become prevalent at high RAS activity levels**, often more evident in oncogenic settings. (kolch2023dynamicregulationof pages 15-16, kolch2023dynamicregulationof pages 11-11)

**Annotation guidance:** “PI3K–AKT signaling” is part of canonical Ras biology, but annotating HRAS to broad survival/proliferation outcomes via PI3K should be conditioned on evidence that is not solely mutant-locked HRAS or transformed-cell phenotypes.

#### 3.3 RalGDS/Ral pathway and RASSF pathways (core Ras outputs)
Kolch et al. summarize that in healthy tissues Ras signaling is largely funneled into three main pathways: **RAF (MAPK), RAL (via RALGDS/RGL2), and RASSF5**, and that six high-affinity effectors (ARAF, BRAF, RAF1, RALGDS, RGL2, RASSF5) can constitute **up to ~80% of Ras effector complexes** (quantitative). (kolch2023dynamicregulationof pages 11-11)

#### 3.4 Apoptosis/senescence: generally non-core default for HRAS
Kolch et al. describe that apoptotic vs proliferative outcomes can depend on **kinetics and pathway competition**, e.g., competition between **MEK and MST2 for RAF1** coordinating proliferative ERK outputs vs proapoptotic MST2 signaling; sustained vs transient Ras activation can flip these outputs. This supports *context-dependent* annotations, but argues against default, unconditional HRAS annotations to apoptosis/senescence regulation without specific, physiological evidence. (kolch2023dynamicregulationof pages 13-14)

### 4) Effector/protein-binding annotations: specificity and evidence strength

#### 4.1 Prefer specific effector binding terms over generic “protein binding”
Because Ras engages many partners, GO MF annotations should, where possible, use **specific binding terms** supported by direct interaction evidence and nucleotide dependence criteria. Recent expert reviews stress that the minimal criterion for effector classification is **binding only when RAS is GTP-bound**, and that experimental validation is required (sequence motifs alone are insufficient). (mozzarelli2024functionalandstructural pages 1-3, smith2023definingbonefide pages 1-2)

#### 4.2 Quantitative binding data (helps prevent over-annotation)
Nakhaeizadeh et al. (PLoS ONE, 2016-12; DOI: **10.1371/journal.pone.0167145**) report direct HRAS binding affinities (Kd) to isolated effector domains, supporting graded specificity rather than indiscriminate binding:
- **CRAF/RAF1 RB domain:** ~0.094 μM (high affinity)
- **RASSF5 RA:** ~0.238 μM
- **RALGDS RA:** ~2.50 μM
- **PLCε RA2:** ~3.70 μM
- **PI3Kα RB:** ~84.3 μM (much weaker)
These data support annotating specific effector binding (e.g., RAF binding, RASSF5 binding, RALGDS binding) and also suggest that PI3K binding may be **weaker and potentially more conditional**. (nakhaeizadeh2016theraseffectorinterface pages 6-7)

#### 4.3 Primary effector-binding literature identifiers (PMID/DOI)
Primary studies cited within Nakhaeizadeh et al. include:
- Ras–c-Raf-1 RBD binding/kinetics: Biochemistry 1998, DOI **10.1021/bi980764f**, PMID **9760267**; FEBS Lett 1999 PMID **10386625** (nakhaeizadeh2016theraseffectorinterface pages 19-20)
- Ras–RalGDS: FEBS Lett 1999 PMID **10371160** (nakhaeizadeh2016theraseffectorinterface pages 19-20)
- Ras–RASSF5/NORE1A interactions involving switch regions: EMBO J 2008 DOI **10.1038/emboj.2008.125**, PMID **18596699**; Structure 2006 DOI **10.1016/j.str.2006.03.008**, PMID **16698549** (nakhaeizadeh2016theraseffectorinterface pages 19-20)

### 5) Recent developments (prioritize 2023–2024)

#### 5.1 2024 expert synthesis of effector biology and annotation caveats
Mozzarelli et al. (Molecular Cell, 2024-08; DOI: **10.1016/j.molcel.2024.06.027**, URL https://doi.org/10.1016/j.molcel.2024.06.027) emphasize that many reported “effectors” require **experimental validation**, that RBD/RA presence is **not sufficient**, and that effector competition for limited RAS-GTP complicates interpretation of binding and downstream effects—important for conservative GO effector-binding and BP annotations. (mozzarelli2024functionalandstructural pages 1-3)

#### 5.2 2023 expert analysis of Ras dynamics and interactomics uncertainty
Kolch et al. (Biochem J, 2023-01; DOI: **10.1042/BCJ20220234**, URL https://doi.org/10.1042/bcj20220234) highlight that BioID can produce **false positives**, that interactome overlap between isoforms/contexts can be limited, and that chronic oncogenic signaling drives extensive **network rewiring**—all of which argues for restricting HRAS GO BP annotations to **proximal, mechanism-supported** processes rather than distal phenotypes. (kolch2023dynamicregulationof pages 13-14, kolch2023dynamicregulationof pages 14-15)

### 6) Current applications / real-world implementations (GO-relevant)

- **Spatial control of signaling:** The ER/Golgi→PM trafficking logic and dynamic palmitoylation cycles provide a mechanistic basis for “spatial Ras signaling,” supporting CC terms (Golgi, plasma membrane, recycling endosome) and cautioning that signaling outputs can vary by compartment. (choy1999endomembranetraffickingof pages 1-2, lynch2015thedifferentialpalmitoylation pages 1-3, taguchi2011palmitoylationpilotsras pages 1-3)
- **Effector-interface targeting (conceptual):** While not a GO term, 2023–2024 work framing strict effector definitions and binding competition informs how curated interactions should be captured (only GTP-dependent, mechanistically supported associations). (mozzarelli2024functionalandstructural pages 1-3, smith2023definingbonefide pages 1-2)

### 7) Statistics / quantitative data relevant for curation decisions
- Six high-affinity effectors (ARAF, BRAF, RAF1, RALGDS, RGL2, RASSF5) can constitute **up to ~80%** of Ras effector complexes (supports prioritizing these in core pathway annotation). (kolch2023dynamicregulationof pages 11-11)
- Interactomics and genetics show strong context dependence: e.g., large-scale screening reported **548 vs 447 genetic interactions** in two lines with only **59** overlaps; a **threefold** difference in RAS activity rewired **~30%** of PPIs (supports caution for downstream BP over-annotation). (kolch2023dynamicregulationof pages 14-15)
- Smith 2023 reports **KRAS mutations present in 22% of cancers** (epidemiology context; relevant mainly as a caution about mutant-based literature dominating the field rather than as a basis for normal-function GO). (smith2023definingbonefide pages 1-2)

### 8) Over-annotation risks and caveats (especially mutants/overexpression)

1) **Do not transfer oncogenic mutant phenotypes to wild-type HRAS GO BP terms by default.** Oncogenic Ras can produce constitutive effector interactions, altered feedback, and network rewiring; some mutants remain regulatable by GEFs/GAPs, and outcomes depend on activation kinetics (sustained vs transient). (kolch2023dynamicregulationof pages 15-16, kolch2023dynamicregulationof pages 13-14)

2) **Avoid overly broad BP terms** (e.g., generic “cancer,” “development,” “cell cycle,” “transcriptional regulation,” “immune/inflammatory processes”) unless there is direct mechanistic evidence placing *wild-type HRAS* as a proximal regulator rather than a downstream correlate. Large interactome datasets include false positives and many context-specific interactors. (kolch2023dynamicregulationof pages 13-14, kolch2023dynamicregulationof pages 14-15)

3) **Avoid generic MF “protein binding” where possible.** Recent expert reviews stress that effector status requires GTP-dependent binding and functional impact; many reported interactors lack mechanistic validation. Use specific effector-binding terms (RAF1/CRAF binding, RALGDS binding, RASSF5 binding, PI3K binding) when directly supported. (mozzarelli2024functionalandstructural pages 1-3, smith2023definingbonefide pages 1-2, nakhaeizadeh2016theraseffectorinterface pages 6-7)

4) **Be explicit about cellular compartment context** for localization annotations: CAAX processing localizes HRAS to ER/Golgi during maturation, palmitoylation supports Golgi trapping and PM trafficking, and recycling endosome localization is supported but may be context-specific. (choy1999endomembranetraffickingof pages 1-2, lynch2015thedifferentialpalmitoylation pages 1-3, taguchi2011palmitoylationpilotsras pages 1-3)

### 9) Recommended GO annotation elements (summary table)
The following table captures a conservative, evidence-driven set of core terms plus “avoid/flag” items.

| GO aspect | Suggested GO term label (plain English) | Evidence summary (1 sentence) | Key caveats | Supporting source |
|---|---|---|---|---|
| MF | GTP binding | HRAS is a canonical RAS small GTPase that binds GDP/GTP with high affinity and functions as a nucleotide-dependent molecular switch. | Core, well established | Smith 2023, DOI:10.1002/bies.202300088; Mozzarelli et al. 2024, DOI:10.1016/j.molcel.2024.06.027 (smith2023definingbonefide pages 1-2, mozzarelli2024functionalandstructural pages 1-3) |
| MF | Small monomeric GTPase activity / GTP hydrolysis | HRAS has intrinsic GTPase activity, with GAPs accelerating hydrolysis and GEFs promoting GDP-to-GTP exchange. | Do not infer mutant behavior to WT | Smith 2023, DOI:10.1002/bies.202300088; Kolch et al. 2023, DOI:10.1042/bcj20220234 (smith2023definingbonefide pages 1-2, kolch2023dynamicregulationof pages 15-16) |
| MF | Effector binding (GTP-dependent) | Bona fide HRAS effectors bind preferentially to the GTP-bound switch-region conformation rather than GDP-bound HRAS. | Require direct, nucleotide-dependent evidence | Smith 2023, DOI:10.1002/bies.202300088; Adariani et al. 2021, DOI:10.1016/j.jbc.2021.100626 (smith2023definingbonefide pages 1-2, adariani2021acomprehensiveanalysis pages 1-4) |
| MF | RAF1 / CRAF binding | Direct binding studies support high-affinity HRAS interaction with RAF-family RBDs, including CRAF/RAF1. | Prefer specific partner term over generic protein binding | Nakhaeizadeh et al. 2016, DOI:10.1371/journal.pone.0167145; Sydor et al. 1998, PMID:9760267 (nakhaeizadeh2016theraseffectorinterface pages 6-7, nakhaeizadeh2016theraseffectorinterface pages 19-20) |
| MF | RALGDS binding | HRAS directly binds the RALGDS RA domain in a GTP-dependent manner, supporting specific effector-binding annotation. | Affinity lower than RAF; context matters | Nakhaeizadeh et al. 2016, DOI:10.1371/journal.pone.0167145; Vetter et al. 1999, PMID:10371160 (nakhaeizadeh2016theraseffectorinterface pages 6-7, nakhaeizadeh2016theraseffectorinterface pages 19-20) |
| MF | RASSF5 binding | HRAS directly binds RASSF5/NORE1A RA-domain-containing effectors, involving switch-region contacts. | Use specific evidence; not all RASSF family equal | Nakhaeizadeh et al. 2016, DOI:10.1371/journal.pone.0167145; Stieglitz et al. 2008, DOI:10.1038/emboj.2008.125, PMID:18596699 (nakhaeizadeh2016theraseffectorinterface pages 6-7, nakhaeizadeh2016theraseffectorinterface pages 19-20) |
| MF | PI3K binding | HRAS can bind PI3K RBD-containing catalytic subunits, but measured affinity is substantially weaker than for RAF/RASSF5. | Keep as specific, possibly non-core partner binding | Nakhaeizadeh et al. 2016, DOI:10.1371/journal.pone.0167145; Smith 2023, DOI:10.1002/bies.202300088 (nakhaeizadeh2016theraseffectorinterface pages 6-7, smith2023definingbonefide pages 3-3) |
| BP | Ras protein signal transduction | HRAS is one of the canonical RAS proteins acting upstream of multiple effector pathways in Ras signal transduction. | Core BP term | Kolch et al. 2023, DOI:10.1042/bcj20220234 (kolch2023dynamicregulationof pages 1-2) |
| BP | Positive regulation of MAPK cascade | RAS signaling is funneled strongly into RAF-MEK-ERK, and HRAS contributes to ERK output and MAPK signaling dynamics. | Core but avoid over-specific phenotypes from mutants | Kolch et al. 2023, DOI:10.1042/bcj20220234 (kolch2023dynamicregulationof pages 12-13, kolch2023dynamicregulationof pages 11-11) |
| BP | PI3K-AKT pathway activation | PI3K is a recognized RAS effector pathway, especially engaged at higher RAS-GTP levels and in some oncogenic contexts. | Core Ras output, but context dependent for HRAS-specific strength | Kolch et al. 2023, DOI:10.1042/bcj20220234; Smith 2023, DOI:10.1002/bies.202300088 (kolch2023dynamicregulationof pages 11-11, smith2023definingbonefide pages 1-2) |
| BP | Ral signaling via RalGDS | High-affinity RAS effectors include RALGDS/RGL2, supporting HRAS participation in Ral GTPase signaling. | Reasonable pathway annotation if direct HRAS evidence retained | Kolch et al. 2023, DOI:10.1042/bcj20220234 (kolch2023dynamicregulationof pages 11-11) |
| BP | Regulation of proliferation or differentiation | RAS-ERK signaling dynamics can bias proliferation versus differentiation outputs, but these outcomes depend strongly on cell type and signaling kinetics. | Usually non-core/context specific | Kolch et al. 2023, DOI:10.1042/bcj20220234 (kolch2023dynamicregulationof pages 1-2, kolch2023dynamicregulationof pages 13-14) |
| BP | Apoptosis / senescence regulation | Pro- or anti-apoptotic outputs can arise through pathway competition (e.g., RAF1-MEK versus MST2) and mutant/kinetic context rather than constitutive normal HRAS function. | Flag for review, not default core | Kolch et al. 2023, DOI:10.1042/bcj20220234 (kolch2023dynamicregulationof pages 13-14, kolch2023dynamicregulationof pages 15-16) |
| CC | Plasma membrane localization | HRAS membrane association is essential for signaling, with lipid modifications enabling stable plasma membrane localization. | Core CC term | Choy et al. 1999, DOI:10.1016/S0092-8674(00)80607-8; Wright & Philips 2006, DOI:10.1194/jlr.R600004-JLR200 (choy1999endomembranetraffickingof pages 1-2, wright2006thematicreviewseries pages 2-3) |
| CC | Golgi apparatus localization / trafficking | HRAS transits ER/Golgi during post-CAAX processing and palmitoylation, and cycles between Golgi and plasma membrane. | Core trafficking/localization term | Choy et al. 1999, DOI:10.1016/S0092-8674(00)80607-8; Lynch et al. 2015, DOI:10.1002/jcp.24779 (choy1999endomembranetraffickingof pages 1-2, lynch2015thedifferentialpalmitoylation pages 1-3) |
| CC | Recycling endosome localization | Palmitoylated HRAS has been reported on recycling endosomes as a waypoint in post-Golgi trafficking to the plasma membrane. | Useful but less core than PM/Golgi | Taguchi & Misaki 2011, DOI:10.4161/sgtp.2.2.15245 (taguchi2011palmitoylationpilotsras pages 1-3) |
| CC | Membrane targeting by CAAX prenylation and palmitoylation | HRAS uses CAAX farnesylation, AAX cleavage, carboxymethylation, and reversible palmitoylation as the core membrane-targeting logic. | PTM mechanism, not a location term by itself | Wright & Philips 2006, DOI:10.1194/jlr.R600004-JLR200; Berthiaume 2002, DOI:10.1126/stke.2002.152.pe41 (wright2006thematicreviewseries pages 2-3, berthiaume2002insiderinformationhow pages 1-2) |
| Avoid/flag for review | Generic protein binding | Broad protein-binding annotation adds little value when specific effector binding terms are available with direct evidence. | Over-annotation risk | Mozzarelli et al. 2024, DOI:10.1016/j.molcel.2024.06.027; Smith 2023, DOI:10.1002/bies.202300088 (mozzarelli2024functionalandstructural pages 1-3, smith2023definingbonefide pages 1-2) |
| Avoid/flag for review | Broad cancer/development/cell cycle terms from oncogenic mutants | Many mutant RAS phenotypes reflect constitutive signaling, network rewiring, or overexpression and should not be transferred wholesale to normal HRAS GO annotations. | Mutant/overexpression confound | Kolch et al. 2023, DOI:10.1042/bcj20220234; Smith 2023, DOI:10.1002/bies.202300088 (kolch2023dynamicregulationof pages 14-15, smith2023definingbonefide pages 1-2) |
| Avoid/flag for review | Transcriptional regulation, immune/inflammatory, or other distal phenotypes | High-throughput interactomics and downstream phenotypes often show context-specific rewiring and false positives, so distal process terms need direct mechanistic evidence. | Indirect/context-specific | Kolch et al. 2023, DOI:10.1042/bcj20220234; Mozzarelli et al. 2024, DOI:10.1016/j.molcel.2024.06.027 (kolch2023dynamicregulationof pages 13-14, mozzarelli2024functionalandstructural pages 1-3) |


*Table: This table summarizes core and cautionary GO annotation elements for human HRAS, emphasizing direct, GO-relevant evidence for molecular function, signaling processes, localization, and specific effector interactions. It also flags common over-annotation risks from mutant, overexpression, and indirect phenotype-based evidence.*

### References (URLs / dates)
- Kolch W, Berta D, Rosta E. *Dynamic regulation of RAS and RAS signaling.* **Biochemical Journal** (2023-01). DOI: 10.1042/BCJ20220234. https://doi.org/10.1042/bcj20220234 (kolch2023dynamicregulationof pages 1-2)
- Mozzarelli AM, Simanshu DK, Castel P. *Functional and structural insights into RAS effector proteins.* **Molecular Cell** (2024-08). DOI: 10.1016/j.molcel.2024.06.027. https://doi.org/10.1016/j.molcel.2024.06.027 (mozzarelli2024functionalandstructural pages 1-3)
- Smith MJ. *Defining bone fide effectors of RAS GTPases.* **BioEssays** (2023-07). DOI: 10.1002/bies.202300088. https://doi.org/10.1002/bies.202300088 (smith2023definingbonefide pages 1-2)
- Choy E et al. *Endomembrane trafficking of Ras: the CAAX motif targets proteins to the ER and Golgi.* **Cell** (1999-07). DOI: 10.1016/S0092-8674(00)80607-8. https://doi.org/10.1016/S0092-8674(00)80607-8 (choy1999endomembranetraffickingof pages 1-2)
- Wright LP, Philips MR. *CAAX modification and membrane targeting of Ras.* **Journal of Lipid Research** (2006-05). DOI: 10.1194/jlr.R600004-JLR200. https://doi.org/10.1194/jlr.r600004-jlr200 (wright2006thematicreviewseries pages 2-3)
- Lynch SJ et al. *Differential palmitoylation states of N-Ras and H-Ras determine distinct Golgi localizations.* **Journal of Cellular Physiology** (2015-03). DOI: 10.1002/jcp.24779. https://doi.org/10.1002/jcp.24779 (lynch2015thedifferentialpalmitoylation pages 1-3)
- Taguchi T, Misaki R. *Palmitoylation pilots Ras to recycling endosomes.* **Small GTPases** (2011-03). DOI: 10.4161/sgtp.2.2.15245. https://doi.org/10.4161/sgtp.2.2.15245 (taguchi2011palmitoylationpilotsras pages 1-3)
- Nakhaeizadeh H et al. *The RAS-Effector Interface: Isoform-Specific Differences in the Effector Binding Regions.* **PLoS ONE** (2016-12). DOI: 10.1371/journal.pone.0167145. https://doi.org/10.1371/journal.pone.0167145 (nakhaeizadeh2016theraseffectorinterface pages 6-7)



References

1. (smith2023definingbonefide pages 1-2): Matthew J. Smith. Defining bone fide effectors of ras gtpases. BioEssays, Jul 2023. URL: https://doi.org/10.1002/bies.202300088, doi:10.1002/bies.202300088. This article has 11 citations and is from a peer-reviewed journal.

2. (mozzarelli2024functionalandstructural pages 1-3): Alessandro M. Mozzarelli, Dhirendra K. Simanshu, and Pau Castel. Functional and structural insights into ras effector proteins. Molecular Cell, 84:2807-2821, Aug 2024. URL: https://doi.org/10.1016/j.molcel.2024.06.027, doi:10.1016/j.molcel.2024.06.027. This article has 35 citations and is from a highest quality peer-reviewed journal.

3. (adariani2021acomprehensiveanalysis pages 1-4): Soheila Rezaei Adariani, Neda S. Kazemein Jasemi, Farhad Bazgir, Christoph Wittich, Ehsan Amin, Claus A.M. Seidel, Radovan Dvorsky, and Mohammad R. Ahmadian. A comprehensive analysis of ras-effector interactions reveals interaction hotspots and new binding partners. The Journal of Biological Chemistry, 296:100626, Apr 2021. URL: https://doi.org/10.1016/j.jbc.2021.100626, doi:10.1016/j.jbc.2021.100626. This article has 31 citations.

4. (wright2006thematicreviewseries pages 2-3): Latasha P. Wright and Mark R. Philips. Thematic review series: lipid posttranslational modifications caax modification and membrane targeting of ras published, jlr papers in press, march 16, 2006. Journal of Lipid Research, 47:883-891, May 2006. URL: https://doi.org/10.1194/jlr.r600004-jlr200, doi:10.1194/jlr.r600004-jlr200. This article has 482 citations and is from a peer-reviewed journal.

5. (choy1999endomembranetraffickingof pages 1-2): Edwin Choy, Vi K. Chiu, Joseph Silletti, Marianna Feoktistov, Takashi Morimoto, David Michaelson, Ivan E. Ivanov, and Mark R. Philips. Endomembrane trafficking of ras the caax motif targets proteins to the er and golgi. Cell, 98:69-80, Jul 1999. URL: https://doi.org/10.1016/s0092-8674(00)80607-8, doi:10.1016/s0092-8674(00)80607-8. This article has 1054 citations and is from a highest quality peer-reviewed journal.

6. (berthiaume2002insiderinformationhow pages 1-2): Luc G. Berthiaume. Insider information: how palmitoylation of ras makes it a signaling double agent. Science's STKE, 2002:pe41-pe41, Oct 2002. URL: https://doi.org/10.1126/stke.2002.152.pe41, doi:10.1126/stke.2002.152.pe41. This article has 47 citations.

7. (lynch2015thedifferentialpalmitoylation pages 1-3): Stephen J. Lynch, Harriet Snitkin, Iwona Gumper, Mark R. Philips, David Sabatini, and Angel Pellicer. The differential palmitoylation states of n‐ras and h‐ras determine their distinct golgi subcompartment localizations. Journal of Cellular Physiology, 230:610-619, Mar 2015. URL: https://doi.org/10.1002/jcp.24779, doi:10.1002/jcp.24779. This article has 63 citations and is from a peer-reviewed journal.

8. (taguchi2011palmitoylationpilotsras pages 1-3): Tomohiko Taguchi and Ryo Misaki. Palmitoylation pilots ras to recycling endosomes. Small GTPases, 2:29-82-84, Mar 2011. URL: https://doi.org/10.4161/sgtp.2.2.15245, doi:10.4161/sgtp.2.2.15245. This article has 21 citations and is from a peer-reviewed journal.

9. (kolch2023dynamicregulationof pages 1-2): Walter Kolch, Dénes Berta, and Edina Rosta. Dynamic regulation of ras and ras signaling. Biochemical Journal, 480:1-23, Jan 2023. URL: https://doi.org/10.1042/bcj20220234, doi:10.1042/bcj20220234. This article has 103 citations and is from a domain leading peer-reviewed journal.

10. (kolch2023dynamicregulationof pages 11-11): Walter Kolch, Dénes Berta, and Edina Rosta. Dynamic regulation of ras and ras signaling. Biochemical Journal, 480:1-23, Jan 2023. URL: https://doi.org/10.1042/bcj20220234, doi:10.1042/bcj20220234. This article has 103 citations and is from a domain leading peer-reviewed journal.

11. (kolch2023dynamicregulationof pages 12-13): Walter Kolch, Dénes Berta, and Edina Rosta. Dynamic regulation of ras and ras signaling. Biochemical Journal, 480:1-23, Jan 2023. URL: https://doi.org/10.1042/bcj20220234, doi:10.1042/bcj20220234. This article has 103 citations and is from a domain leading peer-reviewed journal.

12. (kolch2023dynamicregulationof pages 15-16): Walter Kolch, Dénes Berta, and Edina Rosta. Dynamic regulation of ras and ras signaling. Biochemical Journal, 480:1-23, Jan 2023. URL: https://doi.org/10.1042/bcj20220234, doi:10.1042/bcj20220234. This article has 103 citations and is from a domain leading peer-reviewed journal.

13. (kolch2023dynamicregulationof pages 13-14): Walter Kolch, Dénes Berta, and Edina Rosta. Dynamic regulation of ras and ras signaling. Biochemical Journal, 480:1-23, Jan 2023. URL: https://doi.org/10.1042/bcj20220234, doi:10.1042/bcj20220234. This article has 103 citations and is from a domain leading peer-reviewed journal.

14. (nakhaeizadeh2016theraseffectorinterface pages 6-7): Hossein Nakhaeizadeh, Ehsan Amin, Saeideh Nakhaei-Rad, Radovan Dvorsky, and Mohammad Reza Ahmadian. The ras-effector interface: isoform-specific differences in the effector binding regions. PLoS ONE, 11:e0167145, Dec 2016. URL: https://doi.org/10.1371/journal.pone.0167145, doi:10.1371/journal.pone.0167145. This article has 97 citations and is from a peer-reviewed journal.

15. (nakhaeizadeh2016theraseffectorinterface pages 19-20): Hossein Nakhaeizadeh, Ehsan Amin, Saeideh Nakhaei-Rad, Radovan Dvorsky, and Mohammad Reza Ahmadian. The ras-effector interface: isoform-specific differences in the effector binding regions. PLoS ONE, 11:e0167145, Dec 2016. URL: https://doi.org/10.1371/journal.pone.0167145, doi:10.1371/journal.pone.0167145. This article has 97 citations and is from a peer-reviewed journal.

16. (kolch2023dynamicregulationof pages 14-15): Walter Kolch, Dénes Berta, and Edina Rosta. Dynamic regulation of ras and ras signaling. Biochemical Journal, 480:1-23, Jan 2023. URL: https://doi.org/10.1042/bcj20220234, doi:10.1042/bcj20220234. This article has 103 citations and is from a domain leading peer-reviewed journal.

17. (smith2023definingbonefide pages 3-3): Matthew J. Smith. Defining bone fide effectors of ras gtpases. BioEssays, Jul 2023. URL: https://doi.org/10.1002/bies.202300088, doi:10.1002/bies.202300088. This article has 11 citations and is from a peer-reviewed journal.

## Citations

1. adariani2021acomprehensiveanalysis pages 1-4
2. choy1999endomembranetraffickingof pages 1-2
3. lynch2015thedifferentialpalmitoylation pages 1-3
4. taguchi2011palmitoylationpilotsras pages 1-3
5. kolch2023dynamicregulationof pages 12-13
6. kolch2023dynamicregulationof pages 11-11
7. kolch2023dynamicregulationof pages 13-14
8. nakhaeizadeh2016theraseffectorinterface pages 6-7
9. nakhaeizadeh2016theraseffectorinterface pages 19-20
10. mozzarelli2024functionalandstructural pages 1-3
11. kolch2023dynamicregulationof pages 14-15
12. smith2023definingbonefide pages 1-2
13. kolch2023dynamicregulationof pages 1-2
14. wright2006thematicreviewseries pages 2-3
15. berthiaume2002insiderinformationhow pages 1-2
16. kolch2023dynamicregulationof pages 15-16
17. smith2023definingbonefide pages 3-3
18. https://doi.org/10.1016/j.molcel.2024.06.027
19. https://doi.org/10.1042/bcj20220234
20. https://doi.org/10.1002/bies.202300088
21. https://doi.org/10.1016/S0092-8674(00
22. https://doi.org/10.1194/jlr.r600004-jlr200
23. https://doi.org/10.1002/jcp.24779
24. https://doi.org/10.4161/sgtp.2.2.15245
25. https://doi.org/10.1371/journal.pone.0167145
26. https://doi.org/10.1002/bies.202300088,
27. https://doi.org/10.1016/j.molcel.2024.06.027,
28. https://doi.org/10.1016/j.jbc.2021.100626,
29. https://doi.org/10.1194/jlr.r600004-jlr200,
30. https://doi.org/10.1016/s0092-8674(00
31. https://doi.org/10.1126/stke.2002.152.pe41,
32. https://doi.org/10.1002/jcp.24779,
33. https://doi.org/10.4161/sgtp.2.2.15245,
34. https://doi.org/10.1042/bcj20220234,
35. https://doi.org/10.1371/journal.pone.0167145,