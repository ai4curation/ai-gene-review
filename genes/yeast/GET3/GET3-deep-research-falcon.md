---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-13T03:01:39.869307'
end_time: '2026-05-13T03:18:20.507928'
duration_seconds: 1000.64
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

GO annotation research for Saccharomyces cerevisiae GET3/ARR4 (UniProt Q12154). Focus on GO evidence for core functions: ATPase/ATP hydrolysis and ATP binding, homodimeric GET3 as cytosolic targeting factor for tail-anchored membrane proteins, binding/shielding TA protein transmembrane domains, delivery to the ER membrane GET1/GET2 insertase/receptor, tail-anchored membrane protein insertion into ER membrane, GET complex, cytosol/cytoplasm and ER membrane localization. Evaluate non-core or context-specific roles: oxidative-stress ATP-independent holdase/chaperone, protein folding/unfolded protein binding, heat/metal/arsenite response, Golgi-to-ER retrograde transport with Erd2/HDEL receptor, guanyl-nucleotide exchange factor activity for Gpa1/pheromone signaling, generic protein binding and identical protein binding. Include PMID/DOI citations and keep under 1200 words.

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

GO annotation research for Saccharomyces cerevisiae GET3/ARR4 (UniProt Q12154). Focus on GO evidence for core functions: ATPase/ATP hydrolysis and ATP binding, homodimeric GET3 as cytosolic targeting factor for tail-anchored membrane proteins, binding/shielding TA protein transmembrane domains, delivery to the ER membrane GET1/GET2 insertase/receptor, tail-anchored membrane protein insertion into ER membrane, GET complex, cytosol/cytoplasm and ER membrane localization. Evaluate non-core or context-specific roles: oxidative-stress ATP-independent holdase/chaperone, protein folding/unfolded protein binding, heat/metal/arsenite response, Golgi-to-ER retrograde transport with Erd2/HDEL receptor, guanyl-nucleotide exchange factor activity for Gpa1/pheromone signaling, generic protein binding and identical protein binding. Include PMID/DOI citations and keep under 1200 words.

## Research report: GO-annotation evidence for *S. cerevisiae* Get3/Arr4 (UniProt Q12154)

### Scope and sources
This report summarizes Gene Ontology (GO)-relevant experimental evidence for Get3/Arr4, emphasizing core Guided Entry of Tail-anchored proteins (GET) pathway roles and evaluating proposed non-core/context-specific roles. Priority is given to recent 2023–2024 work when available, complemented by high-confidence mechanistic primary studies.

A compact evidence map is provided in the table artifact below.

| GO aspect | Proposed GO term/concept | Evidence summary | Key quantitative data | Strongest supporting citations with year/DOI/URL |
|---|---|---|---|---|
| MF | ATPase activity / ATP hydrolysis | Get3 is a SIMIBI-class ATPase whose nucleotide cycle drives conformational switching needed for TA-client release at the ER; hydrolysis-defective mutants remain substrate-bound and insertion-defective. | Get2 binds ATP-bound Get3 with Kd ~190 nM; Get1 binds post-release apo-Get3 with Kd ~50 nM. | Mariappan et al., 2011, doi:10.1038/nature10362, https://doi.org/10.1038/nature10362; Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334 (mariappan2011themechanismof pages 22-25, denic2013endoplasmicreticulumtargeting pages 5-7) |
| MF | ATP binding | Structural states with AMPPNP, ADP, and ADP·AlF4− show ATP-dependent open/closed Get3 dimer conformations required for substrate capture and receptor engagement. | ATP-bound state preferentially engages Get4/Get5; Get4/Get5 has ~10-fold lower affinity for ADP-bound Get3. | Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334; Jennrich, 2024, doi:10.53846/goediss-10715, https://doi.org/10.53846/goediss-10715 (denic2013endoplasmicreticulumtargeting pages 5-7, jennrich2024characterizationofstressinduced pages 20-23) |
| MF | Tail-anchored membrane protein binding / TMD shielding | Zn2+-stabilized homodimeric Get3 forms a composite hydrophobic groove that binds and shields α-helical TA transmembrane domains in the cytosol. | Hydrophilizing groove mutations reduce TA binding; hydrolysis-deficient D57N/D57E mutants trap substrate-bound states. | Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334; Mariappan et al., 2011, doi:10.1038/nature10362, https://doi.org/10.1038/nature10362 (denic2013endoplasmicreticulumtargeting pages 5-7, mariappan2011themechanismof pages 22-25) |
| MF | Identical protein binding / homodimerization | Get3 functions as an obligate homodimer, and dimer closure generates the TA-binding site central to GET-pathway activity. | Obligatory Zn2+-coordinated homodimer; tetramers also observed under oxidizing/stress conditions. | Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334; Jennrich, 2024, doi:10.53846/goediss-10715, https://doi.org/10.53846/goediss-10715 (denic2013endoplasmicreticulumtargeting pages 5-7, jennrich2024characterizationofstressinduced pages 20-23) |
| BP | Cytosolic targeting factor for TA proteins | Get3 receives TA clients from the Sgt2/Get4/Get5 pretargeting machinery and escorts them post-translationally from the cytosol to the ER receptor. | Reconstituted Get3–Sec22 complexes are insertion-competent. | Wang et al., 2011, doi:10.1016/j.molcel.2011.07.020, https://doi.org/10.1016/j.molcel.2011.07.020; Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334 (wang2011themechanismof pages 1-2, denic2013endoplasmicreticulumtargeting pages 4-5) |
| BP | Delivery to ER membrane Get1/Get2 receptor/insertase | Get2 first tethers the Get3-TA complex to the ER, then Get1 binds and wedges open Get3 to trigger cargo release for membrane insertion. | Minimal functional membrane machinery is Get1/Get2; ATP disrupts Get1–Get3 complex for recycling. | Mariappan et al., 2011, doi:10.1038/nature10362, https://doi.org/10.1038/nature10362; Wang et al., 2011, doi:10.1016/j.molcel.2011.07.020, https://doi.org/10.1016/j.molcel.2011.07.020 (mariappan2011themechanismof pages 22-25, wang2011themechanismof pages 1-2) |
| BP | Tail-anchored protein insertion into ER membrane | Get1/Get2 constitute the ER insertase/receptor complex, and Get3 ATPase cycling is essential for productive TA insertion rather than mere docking. | A single Get1/2 heterodimer can function as minimal insertase; recent work supports a Get1/2 channel mechanism. | Wang et al., 2011, doi:10.1016/j.molcel.2011.07.020, https://doi.org/10.1016/j.molcel.2011.07.020; Heo et al., 2023, doi:10.1016/j.celrep.2022.111921, https://doi.org/10.1016/j.celrep.2022.111921 (wang2011themechanismof pages 1-2, zalisko2017tailanchoredprotein pages 6-11) |
| CC | Cytosol / cytoplasm | Core GET-pathway function places Get3 in the cytosol as the soluble TA-targeting ATPase that shuttles between pretargeting factors and the ER. | In stress/starvation, soluble Get3 relocalizes to cytosolic foci/GET bodies within ~1 h. | Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334; Jennrich, 2024, doi:10.53846/goediss-10715, https://doi.org/10.53846/goediss-10715 (denic2013endoplasmicreticulumtargeting pages 5-7, jennrich2024characterizationofstressinduced pages 113-115) |
| CC | Endoplasmic reticulum membrane | A substantial fraction of Get3 is membrane-associated through interaction with the ER Get1/Get2 receptor complex during cargo delivery and recycling. | Membrane association is ATP-sensitive and reversible. | Wang et al., 2011, doi:10.1016/j.molcel.2011.07.020, https://doi.org/10.1016/j.molcel.2011.07.020; Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334 (wang2011themechanismof pages 1-2, denic2013endoplasmicreticulumtargeting pages 5-7) |
| CC | GET complex | Get3 physically and functionally associates with the pretargeting complex (Sgt2/Get4/Get5) and the ER receptor/insertase (Get1/Get2), defining it as a core GET-pathway component. | Loss of GET components causes strong aggregation/proteostasis phenotypes; in 2023 screening, GET1/2/3 were top hits. | Denic et al., 2013, doi:10.1101/cshperspect.a013334, https://doi.org/10.1101/cshperspect.a013334; Josefson et al., 2023, doi:10.1038/s41598-023-35666-8, https://doi.org/10.1038/s41598-023-35666-8 (denic2013endoplasmicreticulumtargeting pages 3-4, josefson2023thegetpathway pages 1-2) |
| MF/BP | Unfolded protein binding / ATP-independent holdase chaperone | Under oxidative or ATP-depleting stress, Get3 undergoes redox remodeling and switches from TA-targeting ATPase to ATP-independent holdase that binds unfolding proteins and suppresses aggregation. | Chaperone activation T1/2 <1 min with H2O2/Cu2+ and ~5 min with H2O2 alone; oxidized Get3 retains <20% ATPase activity; near-complete citrate synthase aggregation suppression at 8:1 Get3:substrate. | Voth et al., 2014, doi:10.1016/j.molcel.2014.08.017, https://doi.org/10.1016/j.molcel.2014.08.017; Powis et al., 2013, doi:10.1242/jcs.112151, https://doi.org/10.1242/jcs.112151 (voth2014theproteintargeting pages 2-3, powis2013get3isa pages 6-7) |
| BP | Response to oxidative stress / metal stress | get3Δ cells show copper and oxidative-stress sensitivity, and oxidized Get3 accumulates in stress foci with Hsp70/Hsp104, supporting a condition-specific stress-protective role. | Example condition: 1 mM CuSO4 at 37°C for 4 h induces relocalization; Get3 abundance ~17,300 molecules/cell vs Get1 ~2,250. | Voth et al., 2014, doi:10.1016/j.molcel.2014.08.017, https://doi.org/10.1016/j.molcel.2014.08.017; Reichmann et al., 2018, doi:10.1016/j.molcel.2017.12.021, https://doi.org/10.1016/j.molcel.2017.12.021 (voth2014theproteintargeting pages 9-10, voth2014theproteintargeting pages 8-9, reichmann2018maintainingahealthy pages 3-4) |
| MF/BP | Guanine nucleotide exchange factor activity for Gpa1 / pheromone signaling | Arr4 and Get3 are aliases, and a 2008 study reported direct Gpa1 binding, accelerated nucleotide exchange, and reduced pheromone signaling in arr4Δ cells, but this role is less integrated into the later core Get3 literature and should be treated as context-specific/cautious. | GTPγS binding increased from 0.085 to 0.36 pmol/pmol/min; Pi release from 0.009 to 0.021 pmol/pmol/min; arr4Δ reduced pheromone-induced FUS1-lacZ by ~50% and mating by ~40%. | Lee, 2008, doi:10.17615/tt4v-sn52, https://doi.org/10.17615/tt4v-sn52; Garcia-Marcos, 2024, doi:10.1016/j.jbc.2024.105756, https://doi.org/10.1016/j.jbc.2024.105756 (michael2008activationofg pages 128-134, michael2008activationofg pages 121-128, michael2008activationofg pages 167-173) |
| BP/CC | Golgi-to-ER retrograde transport with Erd2/HDEL receptor | Retrieved sources do not provide direct mechanistic evidence for Get3 in Erd2/HDEL-mediated retrograde transport; available data suggest any trafficking effects are indirect consequences of TA-client mislocalization/proteostasis defects. | Negative evidence: Get3 foci under starvation were explicitly not Golgi-localized. | Powis et al., 2013, doi:10.1242/jcs.112151, https://doi.org/10.1242/jcs.112151 (powis2013get3isa pages 3-5, powis2013get3isa pages 7-8, powis2013get3isa pages 6-7) |
| BP | Proteostasis bottleneck / recent 2023 development | A 2023 genome-wide screen found GET pathway loss to be a major non-stress proteostasis bottleneck, indicating broad cellular consequences beyond TA-client targeting. | Nearly 100% of get1Δ/get2Δ/get3Δ cells displayed Hsp104-GFP foci; 24% of get2Δ foci-forming hits were intrinsically disordered vs ~7.7% expected genome-wide; get3Δ median replicative lifespan 14 vs WT 20 generations. | Josefson et al., 2023, doi:10.1038/s41598-023-35666-8, https://doi.org/10.1038/s41598-023-35666-8 (josefson2023thegetpathway pages 1-2, josefson2023thegetpathway pages 3-5, josefson2023thegetpathway pages 6-8) |


*Table: This table summarizes GO-relevant evidence for Saccharomyces cerevisiae Get3/Arr4 (Q12154) across molecular function, biological process, and cellular component. It highlights strongly supported core GET-pathway annotations and distinguishes stress-induced or less-established context-specific roles.*

### 1) Key concepts and definitions (current understanding)
**Tail-anchored (TA) membrane proteins** are defined by a single C-terminal transmembrane domain (TMD) that emerges only after translation termination; thus they require **post-translational targeting and insertion** into the ER membrane. The yeast GET pathway comprises a **cytosolic pre-targeting complex** (Sgt2/Get4/Get5), the central targeting ATPase **Get3**, and the ER membrane receptor/insertase **Get1/Get2**. Get3/Arr4 is therefore naturally annotated across GO aspects: **Molecular Function (MF)** (ATP binding/hydrolysis; TA-client binding), **Biological Process (BP)** (TA targeting/insertion), and **Cellular Component (CC)** (cytosol and ER membrane/GET complex) (denic2013endoplasmicreticulumtargeting pages 4-5, denic2013endoplasmicreticulumtargeting pages 5-7).

Mechanistically, Get3 is a **SIMIBI-class ATPase** whose nucleotide state controls an **open/closed homodimer** cycle that binds, shields, and releases hydrophobic TMDs, enabling safe cytosolic transit and delivery to the ER receptor (denic2013endoplasmicreticulumtargeting pages 5-7, mariappan2011themechanismof pages 22-25).

### 2) Core GO evidence for canonical GET-pathway functions
#### 2.1 ATP binding and ATPase/ATP hydrolysis (MF)
Structural and biochemical evidence supports that Get3 is an ATPase with multiple nucleotide-linked conformations (open/closed/transition-state analog), consistent with GO:ATP binding and ATP hydrolysis-coupled function (denic2013endoplasmicreticulumtargeting pages 5-7, denic2013endoplasmicreticulumtargeting pages 4-5). Functionally, ATP hydrolysis is required for productive insertion because a hydrolysis-deficient Get3 mutant remains substrate-bound and is inactive in insertion assays (mariappan2011themechanismof pages 22-25). 

Quantitative receptor-binding parameters link the nucleotide cycle to ER docking: Get2 binds ATP-bound Get3 with **Kd ~190 nM**, and the post-release Get1–Get3 nucleotide-free complex is very stable (**Kd ~50 nM**) (mariappan2011themechanismof pages 22-25).

#### 2.2 Homodimeric cytosolic targeting factor; TA-TMD binding/shielding (MF/BP)
Get3 is described as a **Zn2+-stabilized homodimer** whose dimer interface forms a **composite hydrophobic groove** that binds an α-helical TA TMD; mutations that increase groove hydrophilicity reduce TA binding, and conformational closure is nucleotide dependent (denic2013endoplasmicreticulumtargeting pages 5-7). Get2 can bind the ATP-closed Get3 conformation without disrupting the hydrophobic groove, supporting a model where Get3 **shields the TA TMD during delivery** (mariappan2011themechanismof pages 22-25).

#### 2.3 Delivery to ER Get1/Get2 receptor/insertase and TA insertion (BP)
Biochemical reconstitution demonstrates Get1/Get2 are the minimal ER membrane machinery for insertion, with **Get2 tethering** membrane-proximal Get3–TA complexes and **Get1 driving ATPase-dependent substrate release** for insertion (wang2011themechanismof pages 1-2). Mechanistically, Get1 can “wedge open” Get3 after nucleotide hydrolysis to trigger TMD release, and ATP promotes disruption/dissociation of the Get1–Get3 complex to recycle Get3 (mariappan2011themechanismof pages 22-25). 

**Recent development (2023):** a mechanistic update supports the concept that the **Get1/2 insertase forms a channel** mediating TA insertion, refining how GO “TA insertion into ER membrane” may be interpreted structurally/mechanistically in modern annotations (Heo et al., 2023-01; doi:10.1016/j.celrep.2022.111921; https://doi.org/10.1016/j.celrep.2022.111921) (zalisko2017tailanchoredprotein pages 6-11).

#### 2.4 Localization: cytosol/cytoplasm and ER membrane; GET complex (CC)
Core pathway evidence places Get3 as a **cytosolic shuttle** that also becomes **ER membrane-associated** via Get1/Get2 during docking/release; membrane association is ATP-sensitive and reversible (wang2011themechanismof pages 1-2, denic2013endoplasmicreticulumtargeting pages 5-7). Accordingly, CC annotations should include cytosol/cytoplasm and association with the ER membrane GET receptor complex.

### 3) Non-core/context-specific roles: evidence strength and GO implications
#### 3.1 ATP-independent holdase/chaperone; unfolded protein binding; oxidative stress response (MF/BP)
**Strong evidence supports a regulated “moonlighting” role**: under oxidative stress or ATP depletion, Get3 is converted from ATPase targeting factor into an **ATP-independent holdase chaperone**.

Mechanism: oxidation triggers disulfide bond formation and zinc release with partial unfolding/oligomerization; oxidized Get3 becomes ATPase-inactive yet binds unfolding proteins and prevents aggregation (voth2014theproteintargeting pages 1-2, ulrich2021thiolbasedswitchingmechanisms pages 5-6). Quantitatively, oxidative activation is rapid (**T1/2 < 1 min** with H2O2/Cu2+; **~5 min** with H2O2 alone), and oxidized Get3 can almost completely suppress citrate synthase aggregation at an **8:1 Get3:substrate** ratio; oxidized Get3 retains **<20%** ATPase activity (voth2014theproteintargeting pages 2-3). Stress phenotypes and in vivo relocalization are consistent with a protective role during copper/oxidative stress (example: **1 mM CuSO4 at 37°C for 4 h**) (voth2014theproteintargeting pages 9-10).

**GO guidance implication:** MF terms like “unfolded protein binding” and BP terms like “response to oxidative stress” are well supported but **condition-specific** and should not replace the core TA-targeting annotations.

#### 3.2 Heat/metal/arsenite response
Metal/oxidative stress support is direct (copper sensitivity; copper-triggered relocalization) (voth2014theproteintargeting pages 9-10, voth2014theproteintargeting pages 8-9). Heat stress is referenced as a sensitivity phenotype associated with get3 deletion in the oxidative-stress chaperone study, but the mechanistic evidence in the retrieved excerpts is strongest for oxidative/metal stress rather than a dedicated heat-response pathway (voth2014theproteintargeting pages 1-2).

#### 3.3 Golgi-to-ER retrograde transport (Erd2/HDEL receptor) and Golgi localization
No direct evidence for Erd2/HDEL-mediated retrograde transport involvement was found in the retrieved primary mechanistic GET literature. Moreover, during glucose starvation Get3 foci were explicitly **not Golgi-localized** (Golgi marker Anp1 used to exclude Golgi) (powis2013get3isa pages 3-5). Available data instead suggest that any trafficking phenotypes (e.g., involving Sed5 stability) likely reflect **indirect consequences** of TA mis-targeting or proteostasis disruption rather than a primary Erd2-dependent role (powis2013get3isa pages 6-7).

#### 3.4 Guanine nucleotide exchange factor (GEF) activity for Gpa1; pheromone signaling
A 2008 study reported that Arr4 is a **non-receptor GEF for Gpa1** and indicates that **Arr4 is an alias of Get3** (“Get3, an alias for Arr4”) (Lee, 2008; doi:10.17615/tt4v-sn52; https://doi.org/10.17615/tt4v-sn52) (michael2008activationofg pages 167-173). The same source describes direct biochemical activity: Arr4 increased GTPγS binding from **0.085 → 0.36 pmol GTPγS·pmol Gpa1−1·min−1** and Pi release from **0.009 → 0.021 pmol Pi·pmol Gpa1−1·min−1**, and arr4Δ reduced pheromone-induced transcription (~50% in FUS1-lacZ) and mating (~40%) (michael2008activationofg pages 121-128, michael2008activationofg pages 128-134). 

**Caution for GO annotation:** while this evidence is quantitative and directly biochemical, it is (i) less represented in later, GET-pathway-centric mechanistic syntheses and (ii) potentially context-dependent (copper/dimerization dependence noted in that work). Thus, annotating “GEF activity” may be appropriate but should be **qualified with evidence code and context**, and not conflated with Get3’s core TA-targeting role.

#### 3.5 Generic protein binding and identical protein binding
“Identical protein binding” is consistent with obligate Get3 homodimerization required for TA binding and function (denic2013endoplasmicreticulumtargeting pages 5-7, jennrich2024characterizationofstressinduced pages 20-23). “Protein binding” is trivially true (clients and partners), but is low-specificity relative to mechanistically informative terms such as “tail-anchored protein binding” or “unfolded protein binding.”

### 4) Recent developments (2023–2024)
**Insertase mechanism refinement (2023):** Get1/2 is proposed to form a channel enabling insertion, strengthening mechanistic grounding for BP annotations related to TA insertion into ER membrane (Heo et al., 2023-01; doi:10.1016/j.celrep.2022.111921) (zalisko2017tailanchoredprotein pages 6-11).

**GET pathway as a proteostasis bottleneck (2023):** A genome-wide screen found GET1/2/3 among top aggregation hits; manual verification showed **~100%** of get1Δ/get2Δ/get3Δ cells had Hsp104-GFP foci at 30°C, and get3Δ median replicative lifespan was **14 generations vs 20 in WT**. Disorder was enriched among proteins forming foci in GET mutants (**24% vs ~7.7%** expected) (Josefson et al., 2023-06; doi:10.1038/s41598-023-35666-8; https://doi.org/10.1038/s41598-023-35666-8) (josefson2023thegetpathway pages 1-2, josefson2023thegetpathway pages 6-8, josefson2023thegetpathway pages 3-5).

**Stress-induced cytosolic assemblies / “GET bodies” (2024):** During glucose starvation, GET components assemble into cytosolic foci within **~1 h**; Hsp70 chaperones robustly co-localize later (**~4 h**), and after prolonged starvation Hsp70s appear in **≥70%** of foci (Jennrich, 2024; doi:10.53846/goediss-10715; https://doi.org/10.53846/goediss-10715) (jennrich2024characterizationofstressinduced pages 113-115).

### 5) Applications and real-world implementations
1. **In vitro reconstitution** of TA targeting/insertion (Get3 with Get1/2 and upstream factors) provides a rigorous platform for mapping GO evidence to direct biochemical activity and defining minimal machinery (wang2011themechanismof pages 1-2, mariappan2011themechanismof pages 22-25).
2. **Fluorescent reporters** (e.g., Hsp104-GFP aggregation, TA SNARE Sed5 reporters) and genome-wide genetics quantify system-level consequences of GET dysfunction, bridging molecular GO terms with cellular phenotypes (josefson2023thegetpathway pages 1-2, powis2013get3isa pages 6-7).
3. **Stress/foci imaging paradigms** support CC/BP annotations for cytosolic assemblies under starvation and for stress-associated relocalization consistent with holdase function (powis2013get3isa pages 3-5, jennrich2024characterizationofstressinduced pages 113-115).

### Visual evidence
A schematic summarizing the canonical GET pathway and Get3 relocalization to deposition sites under starvation/blocked ATP hydrolysis is available (Powis et al., 2013; doi:10.1242/jcs.112151; https://doi.org/10.1242/jcs.112151) (powis2013get3isa media e2d53b1f).

### Bottom line for GO annotation focus
**Core, high-confidence GO annotations** for Get3/Arr4 should prioritize ATP binding/ATPase activity coupled to TA TMD binding/shielding, ER targeting, and Get1/Get2-dependent TA insertion, with CC terms spanning cytosol and ER membrane/GET complex (mariappan2011themechanismof pages 22-25, wang2011themechanismof pages 1-2, denic2013endoplasmicreticulumtargeting pages 5-7). **Secondary but well-supported condition-specific annotations** include ATP-independent unfolded-protein binding/holdase and oxidative/metal stress response. **Trafficking claims involving Erd2/HDEL** lack direct support in the retrieved evidence. **GEF activity for Gpa1** has direct quantitative biochemical evidence in one source and is cited in later reviews, but appears more context-limited and should be annotated cautiously with appropriate evidence coding and notes (michael2008activationofg pages 128-134, michael2008activationofg pages 167-173).

References

1. (mariappan2011themechanismof pages 22-25): Malaiyalam Mariappan, Agnieszka Mateja, Malgorzata Dobosz, Elia Bove, Ramanujan S. Hegde, and Robert J. Keenan. The mechanism of membrane-associated steps in tail-anchored protein insertion. Nature, 477:61-66, Sep 2011. URL: https://doi.org/10.1038/nature10362, doi:10.1038/nature10362. This article has 201 citations and is from a highest quality peer-reviewed journal.

2. (denic2013endoplasmicreticulumtargeting pages 5-7): Vladimir Denic, V. Dötsch, and I. Sinning. Endoplasmic reticulum targeting and insertion of tail-anchored membrane proteins by the get pathway. Cold Spring Harbor perspectives in biology, 5 8:a013334, Aug 2013. URL: https://doi.org/10.1101/cshperspect.a013334, doi:10.1101/cshperspect.a013334. This article has 92 citations and is from a peer-reviewed journal.

3. (jennrich2024characterizationofstressinduced pages 20-23): Jonas Jennrich. Characterization of stress-induced cytosolic assemblies containing components of the guided-entry of tail-anchored proteins targeting pathway. ArXiv, 2024. URL: https://doi.org/10.53846/goediss-10715, doi:10.53846/goediss-10715. This article has 0 citations.

4. (wang2011themechanismof pages 1-2): Fei Wang, Andrew Whynot, Matthew Tung, and Vladimir Denic. The mechanism of tail-anchored protein insertion into the er membrane. Molecular cell, 43 5:738-50, Sep 2011. URL: https://doi.org/10.1016/j.molcel.2011.07.020, doi:10.1016/j.molcel.2011.07.020. This article has 121 citations and is from a highest quality peer-reviewed journal.

5. (denic2013endoplasmicreticulumtargeting pages 4-5): Vladimir Denic, V. Dötsch, and I. Sinning. Endoplasmic reticulum targeting and insertion of tail-anchored membrane proteins by the get pathway. Cold Spring Harbor perspectives in biology, 5 8:a013334, Aug 2013. URL: https://doi.org/10.1101/cshperspect.a013334, doi:10.1101/cshperspect.a013334. This article has 92 citations and is from a peer-reviewed journal.

6. (zalisko2017tailanchoredprotein pages 6-11): Benjamin Edward Zalisko. Tail anchored protein insertion by a get1/2 heterodimer. Jan 2017. URL: https://doi.org/10.6082/m1pg1pvq, doi:10.6082/m1pg1pvq. This article has 0 citations.

7. (jennrich2024characterizationofstressinduced pages 113-115): Jonas Jennrich. Characterization of stress-induced cytosolic assemblies containing components of the guided-entry of tail-anchored proteins targeting pathway. ArXiv, 2024. URL: https://doi.org/10.53846/goediss-10715, doi:10.53846/goediss-10715. This article has 0 citations.

8. (denic2013endoplasmicreticulumtargeting pages 3-4): Vladimir Denic, V. Dötsch, and I. Sinning. Endoplasmic reticulum targeting and insertion of tail-anchored membrane proteins by the get pathway. Cold Spring Harbor perspectives in biology, 5 8:a013334, Aug 2013. URL: https://doi.org/10.1101/cshperspect.a013334, doi:10.1101/cshperspect.a013334. This article has 92 citations and is from a peer-reviewed journal.

9. (josefson2023thegetpathway pages 1-2): Rebecca Josefson, Navinder Kumar, Xinxin Hao, Beidong Liu, and Thomas Nyström. The get pathway is a major bottleneck for maintaining proteostasis in saccharomyces cerevisiae. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-35666-8, doi:10.1038/s41598-023-35666-8. This article has 4 citations and is from a peer-reviewed journal.

10. (voth2014theproteintargeting pages 2-3): Wilhelm Voth, Markus Schick, Stephanie Gates, Sheng Li, Fabio Vilardi, Irina Gostimskaya, Daniel R. Southworth, Blanche Schwappach, and Ursula Jakob. The protein targeting factor get3 functions as atp-independent chaperone under oxidative stress conditions. Molecular cell, 56 1:116-27, Oct 2014. URL: https://doi.org/10.1016/j.molcel.2014.08.017, doi:10.1016/j.molcel.2014.08.017. This article has 95 citations and is from a highest quality peer-reviewed journal.

11. (powis2013get3isa pages 6-7): Katie Powis, Bianca Schrul, Heather Tienson, Irina Gostimskaya, Michal Breker, Stephen High, Maya Schuldiner, Ursula Jakob, and Blanche Schwappach. Get3 is a holdase chaperone and moves to deposition sites for aggregated proteins when membrane targeting is blocked. Journal of Cell Science, 126:473-483, Jan 2013. URL: https://doi.org/10.1242/jcs.112151, doi:10.1242/jcs.112151. This article has 84 citations and is from a domain leading peer-reviewed journal.

12. (voth2014theproteintargeting pages 9-10): Wilhelm Voth, Markus Schick, Stephanie Gates, Sheng Li, Fabio Vilardi, Irina Gostimskaya, Daniel R. Southworth, Blanche Schwappach, and Ursula Jakob. The protein targeting factor get3 functions as atp-independent chaperone under oxidative stress conditions. Molecular cell, 56 1:116-27, Oct 2014. URL: https://doi.org/10.1016/j.molcel.2014.08.017, doi:10.1016/j.molcel.2014.08.017. This article has 95 citations and is from a highest quality peer-reviewed journal.

13. (voth2014theproteintargeting pages 8-9): Wilhelm Voth, Markus Schick, Stephanie Gates, Sheng Li, Fabio Vilardi, Irina Gostimskaya, Daniel R. Southworth, Blanche Schwappach, and Ursula Jakob. The protein targeting factor get3 functions as atp-independent chaperone under oxidative stress conditions. Molecular cell, 56 1:116-27, Oct 2014. URL: https://doi.org/10.1016/j.molcel.2014.08.017, doi:10.1016/j.molcel.2014.08.017. This article has 95 citations and is from a highest quality peer-reviewed journal.

14. (reichmann2018maintainingahealthy pages 3-4): Dana Reichmann, Wilhelm Voth, and Ursula Jakob. Maintaining a healthy proteome during oxidative stress. Molecular cell, 69 2:203-213, Jan 2018. URL: https://doi.org/10.1016/j.molcel.2017.12.021, doi:10.1016/j.molcel.2017.12.021. This article has 224 citations and is from a highest quality peer-reviewed journal.

15. (michael2008activationofg pages 128-134): Michael Lee. Activation of g protein signaling by a non-receptor exchange factor. Text, 2008. URL: https://doi.org/10.17615/tt4v-sn52, doi:10.17615/tt4v-sn52. This article has 1 citations and is from a peer-reviewed journal.

16. (michael2008activationofg pages 121-128): Michael Lee. Activation of g protein signaling by a non-receptor exchange factor. Text, 2008. URL: https://doi.org/10.17615/tt4v-sn52, doi:10.17615/tt4v-sn52. This article has 1 citations and is from a peer-reviewed journal.

17. (michael2008activationofg pages 167-173): Michael Lee. Activation of g protein signaling by a non-receptor exchange factor. Text, 2008. URL: https://doi.org/10.17615/tt4v-sn52, doi:10.17615/tt4v-sn52. This article has 1 citations and is from a peer-reviewed journal.

18. (powis2013get3isa pages 3-5): Katie Powis, Bianca Schrul, Heather Tienson, Irina Gostimskaya, Michal Breker, Stephen High, Maya Schuldiner, Ursula Jakob, and Blanche Schwappach. Get3 is a holdase chaperone and moves to deposition sites for aggregated proteins when membrane targeting is blocked. Journal of Cell Science, 126:473-483, Jan 2013. URL: https://doi.org/10.1242/jcs.112151, doi:10.1242/jcs.112151. This article has 84 citations and is from a domain leading peer-reviewed journal.

19. (powis2013get3isa pages 7-8): Katie Powis, Bianca Schrul, Heather Tienson, Irina Gostimskaya, Michal Breker, Stephen High, Maya Schuldiner, Ursula Jakob, and Blanche Schwappach. Get3 is a holdase chaperone and moves to deposition sites for aggregated proteins when membrane targeting is blocked. Journal of Cell Science, 126:473-483, Jan 2013. URL: https://doi.org/10.1242/jcs.112151, doi:10.1242/jcs.112151. This article has 84 citations and is from a domain leading peer-reviewed journal.

20. (josefson2023thegetpathway pages 3-5): Rebecca Josefson, Navinder Kumar, Xinxin Hao, Beidong Liu, and Thomas Nyström. The get pathway is a major bottleneck for maintaining proteostasis in saccharomyces cerevisiae. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-35666-8, doi:10.1038/s41598-023-35666-8. This article has 4 citations and is from a peer-reviewed journal.

21. (josefson2023thegetpathway pages 6-8): Rebecca Josefson, Navinder Kumar, Xinxin Hao, Beidong Liu, and Thomas Nyström. The get pathway is a major bottleneck for maintaining proteostasis in saccharomyces cerevisiae. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-35666-8, doi:10.1038/s41598-023-35666-8. This article has 4 citations and is from a peer-reviewed journal.

22. (voth2014theproteintargeting pages 1-2): Wilhelm Voth, Markus Schick, Stephanie Gates, Sheng Li, Fabio Vilardi, Irina Gostimskaya, Daniel R. Southworth, Blanche Schwappach, and Ursula Jakob. The protein targeting factor get3 functions as atp-independent chaperone under oxidative stress conditions. Molecular cell, 56 1:116-27, Oct 2014. URL: https://doi.org/10.1016/j.molcel.2014.08.017, doi:10.1016/j.molcel.2014.08.017. This article has 95 citations and is from a highest quality peer-reviewed journal.

23. (ulrich2021thiolbasedswitchingmechanisms pages 5-6): Kathrin Ulrich, Blanche Schwappach, and Ursula Jakob. Thiol-based switching mechanisms of stress-sensing chaperones. Biological Chemistry, 402:239-252, Oct 2021. URL: https://doi.org/10.1515/hsz-2020-0262, doi:10.1515/hsz-2020-0262. This article has 24 citations and is from a peer-reviewed journal.

24. (powis2013get3isa media e2d53b1f): Katie Powis, Bianca Schrul, Heather Tienson, Irina Gostimskaya, Michal Breker, Stephen High, Maya Schuldiner, Ursula Jakob, and Blanche Schwappach. Get3 is a holdase chaperone and moves to deposition sites for aggregated proteins when membrane targeting is blocked. Journal of Cell Science, 126:473-483, Jan 2013. URL: https://doi.org/10.1242/jcs.112151, doi:10.1242/jcs.112151. This article has 84 citations and is from a domain leading peer-reviewed journal.

## Citations

1. mariappan2011themechanismof pages 22-25
2. denic2013endoplasmicreticulumtargeting pages 5-7
3. wang2011themechanismof pages 1-2
4. zalisko2017tailanchoredprotein pages 6-11
5. voth2014theproteintargeting pages 2-3
6. voth2014theproteintargeting pages 9-10
7. voth2014theproteintargeting pages 1-2
8. michael2008activationofg pages 167-173
9. jennrich2024characterizationofstressinduced pages 113-115
10. jennrich2024characterizationofstressinduced pages 20-23
11. denic2013endoplasmicreticulumtargeting pages 4-5
12. denic2013endoplasmicreticulumtargeting pages 3-4
13. josefson2023thegetpathway pages 1-2
14. voth2014theproteintargeting pages 8-9
15. reichmann2018maintainingahealthy pages 3-4
16. michael2008activationofg pages 128-134
17. michael2008activationofg pages 121-128
18. josefson2023thegetpathway pages 3-5
19. josefson2023thegetpathway pages 6-8
20. ulrich2021thiolbasedswitchingmechanisms pages 5-6
21. https://doi.org/10.1038/nature10362;
22. https://doi.org/10.1101/cshperspect.a013334
23. https://doi.org/10.1101/cshperspect.a013334;
24. https://doi.org/10.53846/goediss-10715
25. https://doi.org/10.1038/nature10362
26. https://doi.org/10.1016/j.molcel.2011.07.020;
27. https://doi.org/10.1016/j.molcel.2011.07.020
28. https://doi.org/10.1016/j.celrep.2022.111921
29. https://doi.org/10.1038/s41598-023-35666-8
30. https://doi.org/10.1016/j.molcel.2014.08.017;
31. https://doi.org/10.1242/jcs.112151
32. https://doi.org/10.1016/j.molcel.2017.12.021
33. https://doi.org/10.17615/tt4v-sn52;
34. https://doi.org/10.1016/j.jbc.2024.105756
35. https://doi.org/10.17615/tt4v-sn52
36. https://doi.org/10.1038/nature10362,
37. https://doi.org/10.1101/cshperspect.a013334,
38. https://doi.org/10.53846/goediss-10715,
39. https://doi.org/10.1016/j.molcel.2011.07.020,
40. https://doi.org/10.6082/m1pg1pvq,
41. https://doi.org/10.1038/s41598-023-35666-8,
42. https://doi.org/10.1016/j.molcel.2014.08.017,
43. https://doi.org/10.1242/jcs.112151,
44. https://doi.org/10.1016/j.molcel.2017.12.021,
45. https://doi.org/10.17615/tt4v-sn52,
46. https://doi.org/10.1515/hsz-2020-0262,