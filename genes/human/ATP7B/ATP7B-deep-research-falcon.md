---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T13:09:03.086296'
end_time: '2026-05-12T13:22:47.760977'
duration_seconds: 824.67
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

Concise GO annotation research for human ATP7B / UniProt P35670. Focus only on: P-type Cu(I)-transporting ATPase molecular function; ATP hydrolysis/copper binding/ATOX1 copper transfer mechanism; trans-Golgi network membrane localization; copper-induced trafficking to vesicles/pericanalicular vesicles; roles in copper ion transport, copper homeostasis, cellular copper detoxification, ceruloplasmin copper loading and biliary copper excretion; caveats for plasma membrane, copper import, xenobiotic export, mitochondrion, late endosome, and generic protein binding GO annotations. Include PMID/DOI citations. Keep under 1500 words.

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

Concise GO annotation research for human ATP7B / UniProt P35670. Focus only on: P-type Cu(I)-transporting ATPase molecular function; ATP hydrolysis/copper binding/ATOX1 copper transfer mechanism; trans-Golgi network membrane localization; copper-induced trafficking to vesicles/pericanalicular vesicles; roles in copper ion transport, copper homeostasis, cellular copper detoxification, ceruloplasmin copper loading and biliary copper excretion; caveats for plasma membrane, copper import, xenobiotic export, mitochondrion, late endosome, and generic protein binding GO annotations. Include PMID/DOI citations. Keep under 1500 words.

## Concise GO-annotation research report: Human **ATP7B** (UniProt **P35670**)

### Scope and GO framing
ATP7B encodes the Wilson disease copper transporter, a **P1B-type (P-type) Cu(I)-transporting ATPase** whose well-supported GO-relevant biology centers on: (i) **ATP-driven Cu(I) export from the cytosol into the trans-Golgi network (TGN) lumen** for metallation of secretory cuproproteins, and (ii) **copper-induced trafficking** to post-Golgi vesicles/pericanalicular compartments to enable **cellular copper detoxification and biliary copper excretion** in hepatocytes. The evidence base also supports a specific **ATOX1→ATP7B copper transfer mechanism** via transient Cu-bridged complexes with ATP7B N-terminal metal-binding domains (MBDs). (polishchuk2013golgiincopper pages 1-2, yu2017themetalchaperone pages 1-2, roelofsen2000copperinducedapicaltrafficking pages 1-2)

| GO aspect | Concise claim | Key supporting experimental/review evidence | Quantitative/statistical details | Best citation IDs |
|---|---|---|---|---|
| MF | ATP7B is a P-type Cu(I)-transporting ATPase | Reviews and mechanistic studies describe ATP7B as a P1B-type ATPase that uses ATP hydrolysis to move Cu(I) across membranes; Cu binding is required for formation of the phosphorylated catalytic intermediate | ATP7B has 8 TM segments and 6 N-terminal metal-binding domains | (yu2017themetalchaperone pages 1-2, polishchuk2013golgiincopper pages 1-2, polishchuk2019cellularfunctionof pages 1-3) |
| MF | ATP hydrolysis/Cu-binding mechanism involves canonical P-type motifs and TM Cu site | ATP binds the N-domain; the conserved DKTG/T motif in the P-domain is phosphorylated; Cu(I) binds a high-affinity CPC motif in TM6 and is released during E1/E2 transitions | DKTGT and TGE motifs highlighted in 2024 structural work; CPC site central to uptake/release | (yu2017dynamicsandinteractions pages 18-22, guo2024diverserolesof pages 1-2, valverde2024proteinkinasesin pages 6-7) |
| MF/BP | ATOX1 transfers Cu(I) to ATP7B regulatory metal-binding domains and activates transport | ATOX1 forms transient Cu-bridged complexes with ATP7B MBDs; transfer alters MBD dynamics and stimulates catalytic phosphorylation/ATPase activity; delivery likely favors regulatory MBD2/3 region, while recent structural work suggests an MBD near the core has a delivery role | ATOX1 binds ~0.85±0.1 Cu; ATP7B N-terminus binds ~6.5–7.3 Cu; apo-ATOX1 can remove 3–4 Cu, leaving ~1.11±0.11 Cu and ~50% activity | (yu2017themetalchaperone pages 1-2, gloria2006functionalassessmentof pages 45-48, guo2024diverserolesof pages 1-2) |
| CC | ATP7B localizes to the trans-Golgi network membrane at basal copper | Multiple hepatocyte/hepatoma studies place ATP7B in the TGN under low Cu, where it transfers Cu into the secretory pathway | Basal localization observed below ~1 µM extracellular Cu in polarized hepatoma cells | (roelofsen2000copperinducedapicaltrafficking pages 1-2, cater2006atp7bmediatesvesicular pages 1-2, lalioti2016basolateralsortingand pages 1-2) |
| CC/BP | Elevated copper drives trafficking from TGN to cytosolic/pericanalicular vesicles | Copper induces reversible redistribution from perinuclear TGN to peripheral vesicles clustered near the canalicular region; trafficking is vesicle- and microtubule-dependent | Redistribution seen from ~5 µM Cu, stronger at 20–40 µM after 4 h; reversed by 100 µM BCS; no stable canalicular localization even at 100 µM or 16 h in one study | (cater2006atp7bmediatesvesicular pages 4-6, roelofsen2000copperinducedapicaltrafficking pages 1-2, cater2006atp7bmediatesvesicular pages 1-2) |
| BP | ATP7B mediates copper ion transport, copper homeostasis, and cellular copper detoxification | ATP7B exports cytosolic Cu into the Golgi lumen and Cu-sequestering vesicles, supporting homeostasis and protection from Cu excess; Wilson disease results from loss of these functions | 2024 review reports 24 ATP7B phospho-Ser/Thr sites, with several Cu-induced sites linked to regulation/trafficking | (polishchuk2019cellularfunctionof pages 1-3, polishchuk2013golgiincopper pages 1-2, valverde2024proteinkinasesin pages 9-10) |
| BP | ATP7B is required for ceruloplasmin copper loading in the secretory pathway | At low Cu, ATP7B in the TGN loads Cu onto newly synthesized secretory cuproproteins, especially ceruloplasmin; ATP7B deficiency reduces serum ceruloplasmin metallation/activity | Functional rescue studies in rodent Wilson disease models restored ceruloplasmin copper incorporation | (roelofsen2000copperinducedapicaltrafficking pages 1-2, polishchuk2019cellularfunctionof pages 3-5, gloria2006functionalassessmentof pages 42-45) |
| BP | ATP7B supports biliary copper excretion | Cu-induced ATP7B trafficking to apical/pericanalicular compartments enables hepatocyte Cu disposal into bile; proposed routes include vesicular sequestration/exocytosis and transcytosis to bile canaliculus | In perfused liver, biliary 64Cu showed an early wave detected at 9 min and peak 9 min later plus a later ATP7B-dependent wave reduced by BCS | (cater2006atp7bmediatesvesicular pages 1-2, lalioti2016basolateralsortingand pages 1-2, hernandez2008atp7bcopperregulatedtraffic pages 5-8) |
| Caveat | Plasma membrane annotation should be narrow, not generic | Evidence is mixed: some studies detect canalicular/apical membrane-associated ATP7B or tight-junction pools during Cu response, whereas others fail to detect stable canalicular membrane residence and support vesicular intermediates instead | Best interpreted as copper-induced, hepatocyte apical/canalicular-associated trafficking rather than constitutive plasma membrane localization | (hernandez2008atp7bcopperregulatedtraffic pages 5-8, cater2006atp7bmediatesvesicular pages 4-6, polishchuk2013golgiincopper pages 7-8) |
| Caveat | Copper import is not supported | ATP7B moves Cu out of the cytosol into Golgi/vesicle lumen and ultimately bile; import into cytosol is performed by other systems, not ATP7B | No primary evidence in retrieved sources for ATP7B-mediated Cu uptake | (yu2017dynamicsandinteractions pages 18-22, polishchuk2013golgiincopper pages 1-2, polishchuk2019cellularfunctionof pages 1-3) |
| Caveat | Xenobiotic export should not be used as core GO annotation here | ATP7B can bind/traffic platinum drugs in cancer contexts, but this is distinct from its physiological copper-transport function and not the focus of requested GO annotation | Evidence for platinum handling is contextual and secondary to Cu homeostasis | (polishchuk2019cellularfunctionof pages 1-3) |
| Caveat | Mitochondrion localization is unsupported for ATP7B | Reviews note mitochondrial Cu delivery is mediated by COX17 and related factors; ATP7B’s established sites are TGN and Cu-responsive vesicular/apical compartments | No direct support here for mitochondrial ATP7B localization | (polishchuk2019cellularfunctionof pages 1-3) |
| Caveat | Late endosome annotation is context-dependent and should be cautious | Some studies/reviews report overlap with late endosome/lysosome markers in certain cell systems, but vesicle identity and route remain debated across models | Not a robust default CC annotation compared with TGN/pericanalicular vesicles | (polishchuk2019cellularfunctionof pages 3-5, polishchuk2013golgiincopper pages 7-8, lalioti2016basolateralsortingand pages 1-2) |
| Caveat | Generic protein binding is too broad to be useful | The informative interaction is specific Cu-dependent ATOX1-to-ATP7B docking/transfer and intramolecular MBD-core regulation, not nonspecific protein binding | Prefer specific mechanistic annotations over generic binding | (yu2017themetalchaperone pages 1-2, gloria2006functionalassessmentof pages 45-48) |


*Table: This table summarizes GO-relevant evidence for human ATP7B, focusing on its core copper-transporting molecular function, trafficking/localization, physiological roles, and annotation caveats. It is designed to support concise, evidence-based GO annotation decisions.*

### 1) Key concepts and definitions (current understanding)

#### 1.1 Molecular function: P-type Cu(I)-transporting ATPase activity
ATP7B is described as a **P-type ATPase** that uses **ATP hydrolysis** to drive Cu(I) translocation across a membrane (from cytosol into lumenal/extracellular-facing compartments), consistent with the general Post–Albers P-type cycle. Copper binding is required to form the **phosphorylated catalytic intermediate**, making ATPase activity **copper-dependent**. (yu2017themetalchaperone pages 1-2, polishchuk2019cellularfunctionof pages 1-3)

Mechanistically, ATP7B follows canonical P-type ATPase logic: ATP binding at the **N-domain** and phosphorylation of a conserved **P-domain Asp in a DKTG/T motif** generate a transient phosphorylated intermediate that is linked to conformational transitions for substrate release and enzyme reset. (yu2017dynamicsandinteractions pages 18-22, valverde2024proteinkinasesin pages 6-7)

A key annotation-relevant Cu(I) binding site is the **high-affinity transmembrane CPC motif** (TM6) used in Cu(I) handling during the transport cycle. (yu2017dynamicsandinteractions pages 18-22)

#### 1.2 Copper binding/ATOX1 copper transfer mechanism
The cytosolic copper chaperone **ATOX1** delivers Cu(I) to ATP7B by forming **transient Cu-bridged protein–protein complexes**, stabilized largely by the copper-coordinating cysteines, transferring Cu(I) to ATP7B’s N-terminal MBDs and (directly or indirectly) onward to the transmembrane transport site. (yu2017themetalchaperone pages 1-2, arioz2018foldingofcopper pages 17-19)

Quantitative/biophysical details useful for evidence-based annotation include: ATOX1 binds ~**0.85 ± 0.1 Cu/ATOX1**; the ATP7B N-terminal region can bind ~**6.5–7.3 Cu/protein** (consistent with multiple MBD sites); apo-ATOX1 can remove **3–4 Cu** from ATP7B relatively easily but ~**1.11 ± 0.11 Cu** can remain, with ATP7B retaining ~**50% activity**, supporting a regulatory (not purely catalytic) role for full MBD occupancy. (gloria2006functionalassessmentof pages 45-48)

#### 1.3 Cellular component: TGN membrane localization and copper-induced trafficking
At **basal/low copper**, ATP7B localizes predominantly to the **trans-Golgi network** (TGN), consistent with its biosynthetic role in delivering Cu into the secretory pathway. (roelofsen2000copperinducedapicaltrafficking pages 1-2, cater2006atp7bmediatesvesicular pages 1-2)

Upon **copper elevation**, ATP7B exits the TGN and redistributes to **cytosolic vesicles/pericanalicular vesicles** and subapical compartments in hepatocyte-derived polarized models; this trafficking is reversible upon copper chelation. (roelofsen2000copperinducedapicaltrafficking pages 1-2, cater2006atp7bmediatesvesicular pages 4-6)

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 2024 structural/transport-mechanism synthesis for Cu+ P-type ATPases
A 2024 cryo-EM/MD study of a Cu+-transporting P1B-1 ATPase clarifies how **MBDs near the core** can serve distinct roles, with one proximal MBD acting structurally to remodel uptake regions and another likely assisting copper delivery to the core, and emphasizes conserved P-type motifs (DKTGT; A-domain TGE) and transmembrane residues that position sulfur ligands for Cu uptake/binding/release. While not ATP7B-specific structures, these data are directly relevant to ATP7B GO MF mechanism annotation because ATP7B is a homologous P1B-1 Cu+ pump and shares these conserved mechanistic motifs/principles. (guo2024diverserolesof pages 1-2, guo2024diverserolesof pages 4-5)

#### 2.2 2024 phosphorylation/trafficking regulation: quantitative site mapping
A 2024 review summarizes a proteomics-derived ATP7B phosphorylation landscape and links Cu-dependent phosphorylation to trafficking and stability. Reported quantitative points include **24 phosphorylatable Ser/Thr sites**, conserved C-terminal diphosphopeptides (e.g., **Ser1429/1432** and **Ser1442/1453**), and Cu-induced phosphorylation at **Ser246, Ser1121, Ser1431, Ser1442**; PKD inhibition can abolish phosphorylation at several sites (e.g., Ser478/Ser481/Ser1121/Ser1453) and correlates phosphorylation with trafficking from TGN to vesicles in some contexts. These data support a “regulation of localization/trafficking” layer relevant to CC annotations (though not requested as a primary focus, it informs mechanism). (valverde2024proteinkinasesin pages 9-10)

#### 2.3 2023 synthesis of P-type ATPase mechanistic advances
A 2023 review highlights cryo-EM-driven advances across P-type ATPases and notes Cu+-ATPases exhibit distinctive uptake/release features and regulation via terminal tails/PTMs and chaperone interactions, supporting the current expert consensus that ATP7B function cannot be annotated purely as a static membrane transporter but must include regulated trafficking. (stock2023fastforwardonptype pages 13-16)

### 3) Current applications and real-world implementations
ATP7B biology is implemented clinically in **Wilson disease**: ATP7B dysfunction causes impaired copper export, leading to hepatic copper accumulation, defective **ceruloplasmin metallation**, and reduced **biliary copper excretion**. These mechanistic links (TGN biosynthetic role + Cu-stimulated excretory trafficking) underpin diagnostic interpretation (e.g., low ceruloplasmin activity) and therapeutic rationale for copper chelation and strategies aimed at restoring ATP7B function/trafficking. (roelofsen2000copperinducedapicaltrafficking pages 1-2, gloria2006functionalassessmentof pages 42-45)

### 4) Expert opinions/analysis (authoritative sources)
Authoritative trafficking-focused reviews emphasize a dual functional model: ATP7B at the **TGN** supplies copper to secretory enzymes (including ceruloplasmin), while copper overload triggers ATP7B redistribution to **peripheral/endolysosomal or pericanalicular compartments** that sequester copper and promote efflux/excretion; the exact identity of the vesicular carriers and whether ATP7B transiently resides at the canalicular membrane remain debated. (polishchuk2019cellularfunctionof pages 3-5, polishchuk2013golgiincopper pages 7-8)

### 5) Relevant statistics and data from studies
Key quantitative details directly supporting GO-relevant trafficking/mechanism include:

* **Copper thresholds for trafficking:** ATP7B redistribution from TGN to vesicles observed at ~**5 µM Cu**, more pronounced at **20–40 µM** after **4 h**, and reversible with chelation (e.g., BCS). Prolonged exposure (up to **16 h**) or higher copper (e.g., **100 µM**) did **not** necessarily yield stable canalicular membrane localization in one widely cited model system, supporting a vesicle-centric interpretation. (cater2006atp7bmediatesvesicular pages 4-6)
* **Biliary copper excretion kinetics:** In perfused liver, biliary 64Cu showed an **early wave detected at 9 min** and peaking **9 min later**, plus a later, longer transcytotic component reduced by copper chelation and associated with ATP7B Golgi sequestration—data linking ATP7B trafficking to copper excretion dynamics. (hernandez2008atp7bcopperregulatedtraffic pages 5-8)
* **ATOX1/ATP7B copper stoichiometry:** ATOX1 binds ~**0.85 ± 0.1 Cu**; ATP7B N-terminus binds ~**6.5–7.3 Cu**; apo-ATOX1 can remove **3–4 Cu** leaving ~**1.11 ± 0.11 Cu**, with ~**50%** residual ATP7B activity. (gloria2006functionalassessmentof pages 45-48)

### Annotation caveats requested (avoid over-broad GO claims)

1. **Plasma membrane (generic) localization:** Evidence supports copper-stimulated redistribution toward apical/canalicular regions, but stable canalicular plasma membrane residence is **variable across systems**; some studies support vesicular sequestration/exocytosis without clear canalicular membrane labeling, while others report canalicular fractions and/or tight junction pools. A cautious annotation should emphasize **copper-induced apical/canalicular-associated trafficking** and/or “TGN → pericanalicular vesicles” rather than constitutive “plasma membrane.” (hernandez2008atp7bcopperregulatedtraffic pages 5-8, cater2006atp7bmediatesvesicular pages 4-6, cater2006atp7bmediatesvesicular pages 1-2)

2. **Copper import:** The supported directionality is **export from cytosol into TGN/vesicle lumen and ultimately bile**, not import into cytosol. Copper uptake into cells is mediated by other proteins (e.g., CTR1), not ATP7B. (polishchuk2013golgiincopper pages 1-2, yu2017dynamicsandinteractions pages 18-22)

3. **Xenobiotic export:** ATP7B has context-dependent roles in platinum drug resistance, but this is mechanistically distinct from the core GO focus requested here (copper transport/homeostasis) and should not be substituted for copper-transport annotations. (polishchuk2019cellularfunctionof pages 1-3)

4. **Mitochondrion:** No strong support in the provided evidence set for ATP7B being a mitochondrial protein; reviews instead highlight other mitochondrial copper delivery factors (e.g., COX17). Avoid “mitochondrion” CC annotation unless direct experimental evidence exists in the specific curated dataset. (polishchuk2019cellularfunctionof pages 1-3)

5. **Late endosome:** Some models report overlap with endosomal/lysosomal markers and describe endolysosomal participation in copper sequestration/efflux; however, vesicle identity and routes (lysosomal exocytosis vs basolateral sorting/transcytosis vs other post-Golgi vesicles) remain debated. Thus “late endosome” should be used cautiously (context-/cell-type-specific) relative to the robust TGN assignment. (lalioti2016basolateralsortingand pages 1-2, polishchuk2019cellularfunctionof pages 3-5)

6. **Generic protein binding:** A generic “protein binding” GO MF term is not informative compared to specific, mechanistically supported interactions such as **ATOX1 docking/copper transfer** and MBD-mediated intramolecular regulation. Prefer specific interaction/process annotations over generic binding. (yu2017themetalchaperone pages 1-2, gloria2006functionalassessmentof pages 45-48)

### Key sources (with publication dates and URLs)
* Guo Z. et al. **Nature Communications** (2024-03). “Diverse roles of the metal binding domains and transport mechanism of copper transporting P-type ATPases.” https://doi.org/10.1038/s41467-024-47001-4 (guo2024diverserolesof pages 1-2)
* Valverde R.H.F., Lowe J. **Kinases and Phosphatases** (2024-07). “Protein Kinases in Copper Homeostasis: A Review on Cu+-ATPase Modulation.” https://doi.org/10.3390/kinasesphosphatases2030015 (valverde2024proteinkinasesin pages 9-10)
* Stock C. et al. **Biochemical Society Transactions** (2023-06). “Fast-forward on P-type ATPases: recent advances on structure and function.” https://doi.org/10.1042/BST20221543 (stock2023fastforwardonptype pages 13-16)
* Roelofsen H. et al. **Gastroenterology** (2000-09). “Copper-induced apical trafficking of ATP7B…” https://doi.org/10.1053/gast.2000.17834 (roelofsen2000copperinducedapicaltrafficking pages 1-2)
* Cater M.A. et al. **Gastroenterology** (2006-02). “ATP7B mediates vesicular sequestration of copper…” https://doi.org/10.1053/j.gastro.2005.10.054 (cater2006atp7bmediatesvesicular pages 4-6)
* Hernandez S. et al. **Gastroenterology** (2008-04). “ATP7B copper-regulated traffic…” https://doi.org/10.1053/j.gastro.2008.01.043 (hernandez2008atp7bcopperregulatedtraffic pages 5-8)
* Lalioti V. et al. **Journal of Cell Science** (2016-06). “Basolateral sorting and transcytosis define the Cu+-regulated translocation of ATP7B…” https://doi.org/10.1242/jcs.184663 (lalioti2016basolateralsortingand pages 1-2)
* Yu C.H. et al. **Journal of Biological Chemistry** (2017-11). “Atox1 regulates the activity of ATP7B…” https://doi.org/10.1074/jbc.M117.811752 (yu2017themetalchaperone pages 1-2)

Note on PMIDs: The evidence retrieved here provides DOIs/URLs; PMIDs were not included in the extracted text snippets. Where needed for GO curation workflows, PMIDs can be obtained by DOI-to-PMID mapping via PubMed.


References

1. (polishchuk2013golgiincopper pages 1-2): Roman Polishchuk and Svetlana Lutsenko. Golgi in copper homeostasis: a view from the membrane trafficking field. Histochemistry and Cell Biology, 140:285-295, Jul 2013. URL: https://doi.org/10.1007/s00418-013-1123-8, doi:10.1007/s00418-013-1123-8. This article has 149 citations and is from a peer-reviewed journal.

2. (yu2017themetalchaperone pages 1-2): Corey H. Yu, Nan Yang, Jameson Bothe, Marco Tonelli, Sergiy Nokhrin, Natalia V. Dolgova, Lelita Braiterman, Svetlana Lutsenko, and Oleg Y. Dmitriev. The metal chaperone atox1 regulates the activity of the human copper transporter atp7b by modulating domain dynamics. Journal of Biological Chemistry, 292:18169-18177, Nov 2017. URL: https://doi.org/10.1074/jbc.m117.811752, doi:10.1074/jbc.m117.811752. This article has 76 citations and is from a domain leading peer-reviewed journal.

3. (roelofsen2000copperinducedapicaltrafficking pages 1-2): Han Roelofsen, Henk Wolters, Marja J.A. Van Luyn, Naoyuki Miura, Folkert Kuipers, and Roel J. Vonk. Copper-induced apical trafficking of atp7b in polarized hepatoma cells provides a mechanism for biliary copper excretion. Gastroenterology, 119 3:782-93, Sep 2000. URL: https://doi.org/10.1053/gast.2000.17834, doi:10.1053/gast.2000.17834. This article has 334 citations and is from a highest quality peer-reviewed journal.

4. (polishchuk2019cellularfunctionof pages 1-3): Roman S. Polishchuk. Cellular function of atp7b (wilson atpase). Clinical and Translational Perspectives on WILSON DISEASE, pages 45-56, Jan 2019. URL: https://doi.org/10.1016/b978-0-12-810532-0.00006-9, doi:10.1016/b978-0-12-810532-0.00006-9. This article has 9 citations.

5. (yu2017dynamicsandinteractions pages 18-22): CH Yu. Dynamics and interactions of metal-binding domains in the function of wilson disease protein. Unknown journal, 2017.

6. (guo2024diverserolesof pages 1-2): Zongxin Guo, Fredrik Orädd, Viktoria Bågenholm, Christina Grønberg, Jian Feng Ma, Peter Ott, Yong Wang, Magnus Andersson, Per Amstrup Pedersen, Kaituo Wang, and Pontus Gourdon. Diverse roles of the metal binding domains and transport mechanism of copper transporting p-type atpases. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-47001-4, doi:10.1038/s41467-024-47001-4. This article has 20 citations and is from a highest quality peer-reviewed journal.

7. (valverde2024proteinkinasesin pages 6-7): Rafael Hospodar Felippe Valverde and Jennifer Lowe. Protein kinases in copper homeostasis: a review on cu+-atpase modulation. Kinases and Phosphatases, 2:240-254, Jul 2024. URL: https://doi.org/10.3390/kinasesphosphatases2030015, doi:10.3390/kinasesphosphatases2030015. This article has 2 citations.

8. (gloria2006functionalassessmentof pages 45-48): Gloria Hsi. Functional assessment of the human copper transporter, atp7b. Text, 2006. URL: https://doi.org/10.7939/r3-hwv9-3r15, doi:10.7939/r3-hwv9-3r15. This article has 0 citations and is from a peer-reviewed journal.

9. (cater2006atp7bmediatesvesicular pages 1-2): Michael A. Cater, Sharon La Fontaine, Kristy Shield, Yolanda Deal, and Julian F.B. Mercer. Atp7b mediates vesicular sequestration of copper: insight into biliary copper excretion. Gastroenterology, 130 2:493-506, Feb 2006. URL: https://doi.org/10.1053/j.gastro.2005.10.054, doi:10.1053/j.gastro.2005.10.054. This article has 174 citations and is from a highest quality peer-reviewed journal.

10. (lalioti2016basolateralsortingand pages 1-2): Vasiliki Lalioti, Ramón Peiró, Manuela Pérez-Berlanga, Yo Tsuchiya, Angeles Muñoz, Teresa Villalba, Carlos Sanchez, and Ignacio V. Sandoval. Basolateral sorting and transcytosis define the cu+-regulated translocation of atp7b to the bile canaliculus. Journal of Cell Science, 129:2190-2201, Jun 2016. URL: https://doi.org/10.1242/jcs.184663, doi:10.1242/jcs.184663. This article has 32 citations and is from a domain leading peer-reviewed journal.

11. (cater2006atp7bmediatesvesicular pages 4-6): Michael A. Cater, Sharon La Fontaine, Kristy Shield, Yolanda Deal, and Julian F.B. Mercer. Atp7b mediates vesicular sequestration of copper: insight into biliary copper excretion. Gastroenterology, 130 2:493-506, Feb 2006. URL: https://doi.org/10.1053/j.gastro.2005.10.054, doi:10.1053/j.gastro.2005.10.054. This article has 174 citations and is from a highest quality peer-reviewed journal.

12. (valverde2024proteinkinasesin pages 9-10): Rafael Hospodar Felippe Valverde and Jennifer Lowe. Protein kinases in copper homeostasis: a review on cu+-atpase modulation. Kinases and Phosphatases, 2:240-254, Jul 2024. URL: https://doi.org/10.3390/kinasesphosphatases2030015, doi:10.3390/kinasesphosphatases2030015. This article has 2 citations.

13. (polishchuk2019cellularfunctionof pages 3-5): Roman S. Polishchuk. Cellular function of atp7b (wilson atpase). Clinical and Translational Perspectives on WILSON DISEASE, pages 45-56, Jan 2019. URL: https://doi.org/10.1016/b978-0-12-810532-0.00006-9, doi:10.1016/b978-0-12-810532-0.00006-9. This article has 9 citations.

14. (gloria2006functionalassessmentof pages 42-45): Gloria Hsi. Functional assessment of the human copper transporter, atp7b. Text, 2006. URL: https://doi.org/10.7939/r3-hwv9-3r15, doi:10.7939/r3-hwv9-3r15. This article has 0 citations and is from a peer-reviewed journal.

15. (hernandez2008atp7bcopperregulatedtraffic pages 5-8): Sonia Hernandez, Yo Tsuchiya, Josefa P. García–Ruiz, Vassiliki Lalioti, Søren Nielsen, Doris Cassio, and Ignacio V. Sandoval. Atp7b copper-regulated traffic and association with the tight junctions: copper excretion into the bile. Gastroenterology, 134 4:1215-23, Apr 2008. URL: https://doi.org/10.1053/j.gastro.2008.01.043, doi:10.1053/j.gastro.2008.01.043. This article has 76 citations and is from a highest quality peer-reviewed journal.

16. (polishchuk2013golgiincopper pages 7-8): Roman Polishchuk and Svetlana Lutsenko. Golgi in copper homeostasis: a view from the membrane trafficking field. Histochemistry and Cell Biology, 140:285-295, Jul 2013. URL: https://doi.org/10.1007/s00418-013-1123-8, doi:10.1007/s00418-013-1123-8. This article has 149 citations and is from a peer-reviewed journal.

17. (arioz2018foldingofcopper pages 17-19): Candan Ariöz and Pernilla Wittung-Stafshede. Folding of copper proteins: role of the metal? Quarterly Reviews of Biophysics, Mar 2018. URL: https://doi.org/10.1017/s0033583518000021, doi:10.1017/s0033583518000021. This article has 51 citations and is from a peer-reviewed journal.

18. (guo2024diverserolesof pages 4-5): Zongxin Guo, Fredrik Orädd, Viktoria Bågenholm, Christina Grønberg, Jian Feng Ma, Peter Ott, Yong Wang, Magnus Andersson, Per Amstrup Pedersen, Kaituo Wang, and Pontus Gourdon. Diverse roles of the metal binding domains and transport mechanism of copper transporting p-type atpases. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-47001-4, doi:10.1038/s41467-024-47001-4. This article has 20 citations and is from a highest quality peer-reviewed journal.

19. (stock2023fastforwardonptype pages 13-16): Charlott Stock, Tomáš Heger, Sara Basse Hansen, Sigrid Thirup Larsen, Michael Habeck, Thibaud Dieudonné, Ronja Driller, and Poul Nissen. Fast-forward on p-type atpases: recent advances on structure and function. Biochemical Society transactions, 51:1347-1360, Jun 2023. URL: https://doi.org/10.1042/bst20221543, doi:10.1042/bst20221543. This article has 30 citations and is from a peer-reviewed journal.

## Citations

1. polishchuk2019cellularfunctionof pages 1-3
2. yu2017dynamicsandinteractions pages 18-22
3. gloria2006functionalassessmentof pages 45-48
4. valverde2024proteinkinasesin pages 9-10
5. stock2023fastforwardonptype pages 13-16
6. guo2024diverserolesof pages 1-2
7. roelofsen2000copperinducedapicaltrafficking pages 1-2
8. lalioti2016basolateralsortingand pages 1-2
9. yu2017themetalchaperone pages 1-2
10. polishchuk2013golgiincopper pages 1-2
11. valverde2024proteinkinasesin pages 6-7
12. polishchuk2019cellularfunctionof pages 3-5
13. gloria2006functionalassessmentof pages 42-45
14. polishchuk2013golgiincopper pages 7-8
15. arioz2018foldingofcopper pages 17-19
16. guo2024diverserolesof pages 4-5
17. https://doi.org/10.1038/s41467-024-47001-4
18. https://doi.org/10.3390/kinasesphosphatases2030015
19. https://doi.org/10.1042/BST20221543
20. https://doi.org/10.1053/gast.2000.17834
21. https://doi.org/10.1053/j.gastro.2005.10.054
22. https://doi.org/10.1053/j.gastro.2008.01.043
23. https://doi.org/10.1242/jcs.184663
24. https://doi.org/10.1074/jbc.M117.811752
25. https://doi.org/10.1007/s00418-013-1123-8,
26. https://doi.org/10.1074/jbc.m117.811752,
27. https://doi.org/10.1053/gast.2000.17834,
28. https://doi.org/10.1016/b978-0-12-810532-0.00006-9,
29. https://doi.org/10.1038/s41467-024-47001-4,
30. https://doi.org/10.3390/kinasesphosphatases2030015,
31. https://doi.org/10.7939/r3-hwv9-3r15,
32. https://doi.org/10.1053/j.gastro.2005.10.054,
33. https://doi.org/10.1242/jcs.184663,
34. https://doi.org/10.1053/j.gastro.2008.01.043,
35. https://doi.org/10.1017/s0033583518000021,
36. https://doi.org/10.1042/bst20221543,