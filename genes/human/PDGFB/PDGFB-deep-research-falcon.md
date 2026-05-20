---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-13T00:28:05.354305'
end_time: '2026-05-13T00:42:21.188140'
duration_seconds: 855.83
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

Concise GO annotation research for human PDGFB / UniProt P01127. Focus only on GO-relevant evidence for platelet-derived growth factor subunit B: core molecular function as a secreted/disulfide-linked PDGF receptor ligand and growth factor; PDGFB homodimer and PDGFA-PDGFB heterodimer formation; direct binding/activation of PDGFRA and PDGFRB receptor dimers; platelet-derived growth factor receptor signaling pathway; receptor ligand activity and growth factor activity; extracellular region/space, secreted protein, extracellular matrix retention, ER/Golgi secretory processing, platelet alpha granule if directly supported. Evaluate biological processes including chemotaxis, cell migration, mesenchymal/pericyte/vascular smooth muscle proliferation and recruitment, angiogenesis/blood vessel development, wound healing, placenta/heart/kidney glomerulus development, and mesangial cell proliferation/migration only where directly supported. Distinguish PDGFB ligand functions from receptor intracellular kinase activity, peptidyl-tyrosine phosphorylation, PI3K-AKT/ERK/MAPK downstream signaling, ROS/NADPH oxidase, transcription/gene-expression/miRNA effects, generic protein binding, and broad proliferation/migration terms. Include PMID/DOI citations and keep under 1700 words.

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

Concise GO annotation research for human PDGFB / UniProt P01127. Focus only on GO-relevant evidence for platelet-derived growth factor subunit B: core molecular function as a secreted/disulfide-linked PDGF receptor ligand and growth factor; PDGFB homodimer and PDGFA-PDGFB heterodimer formation; direct binding/activation of PDGFRA and PDGFRB receptor dimers; platelet-derived growth factor receptor signaling pathway; receptor ligand activity and growth factor activity; extracellular region/space, secreted protein, extracellular matrix retention, ER/Golgi secretory processing, platelet alpha granule if directly supported. Evaluate biological processes including chemotaxis, cell migration, mesenchymal/pericyte/vascular smooth muscle proliferation and recruitment, angiogenesis/blood vessel development, wound healing, placenta/heart/kidney glomerulus development, and mesangial cell proliferation/migration only where directly supported. Distinguish PDGFB ligand functions from receptor intracellular kinase activity, peptidyl-tyrosine phosphorylation, PI3K-AKT/ERK/MAPK downstream signaling, ROS/NADPH oxidase, transcription/gene-expression/miRNA effects, generic protein binding, and broad proliferation/migration terms. Include PMID/DOI citations and keep under 1700 words.

## Concise GO annotation research report: Human **PDGFB** (UniProt **P01127**)—GO-relevant ligand evidence (≤1700 words)

### 0) Scope and curation rules (GO-focused)
This report summarizes **GO-relevant evidence for PDGFB as a secreted PDGF ligand**: disulfide-linked dimer formation (PDGF‑BB; PDGF‑AB), **direct binding/activation of PDGF receptor dimers (PDGFRA/PDGFRB)**, secretion/localization (extracellular space; ER/Golgi processing; ECM/HS retention), platelet α‑granule localization (only where explicitly stated), and **ligand-attributable biological processes** (pericyte recruitment/coverage; angiogenesis/blood vessel morphogenesis; limited wound-healing evidence). It **excludes** receptor **intrinsic kinase activity** (peptidyl-tyrosine phosphorylation), downstream pathway terms (PI3K–AKT, ERK/MAPK, ROS/NADPH oxidase), and broad transcriptional/miRNA effects unless strictly necessary to interpret ligand localization or binding (ostman1992pdgfaaandpdgfbb pages 1-2, fredriksson2004thepdgffamily pages 5-7).

### 1) Key GO concepts/definitions (current understanding relevant to PDGFB)
**PDGFB encodes the PDGF B-chain**, which participates in **secreted, disulfide-linked dimeric ligands** (notably **PDGF‑BB homodimer** and **PDGF‑AB heterodimer with PDGFA**) that activate PDGF receptors by promoting receptor dimerization (ostman1992pdgfaaandpdgfbb pages 1-2, fredriksson2004thepdgffamily pages 5-7, duran2018molecularregulationof pages 9-11). PDGF ligands act extracellularly as growth factors for mesenchymal lineage target cells and vascular mural cells (pericytes/smooth muscle) in paracrine signaling contexts (duran2018molecularregulationof pages 9-11, strell2024functionalandclinical pages 3-5).

### 2) Molecular function (MF): ligand/dimerization and receptor binding specificity
#### 2.1 Disulfide-linked PDGF dimers; PDGF‑BB and PDGF‑AB
A foundational biosynthesis study explicitly describes PDGF as assembled into **disulfide-linked AA, AB, and BB dimers** and analyzes PDGF‑BB biogenesis (ostman1992pdgfaaandpdgfbb pages 1-2). Review-level summaries also state PDGF ligands (including **PDGF‑BB**) are **disulfide-linked dimers** (strell2024functionalandclinical pages 1-3), consistent with the canonical PDGF family description (fredriksson2004thepdgffamily pages 5-7).

#### 2.2 Direct binding/activation of PDGF receptor dimers (PDGFRA/PDGFRB)
A well-cited PDGF family review summarizes receptor specificity at the ligand level: **PDGF‑BB** can bind/activate **PDGFRβ** and can also stimulate **PDGFRα/β heterodimers**; **PDGF‑AB** and **PDGF‑BB** can stimulate **PDGFRα/β heterodimers**; and **PDGF‑AA/AB/BB** are among ligands engaging PDGFRα-containing complexes (fredriksson2004thepdgffamily pages 5-7). A classic experimental study provides a direct chain-specific rule: the **α receptor binds A- or B-chain**, whereas the **β receptor binds only B-chain**, supporting annotation of **PDGFB as necessary for PDGFRβ-binding ligands** (ostman1992pdgfaaandpdgfbb pages 1-2).

**GO MF recommendations (plain-English):** “PDGF receptor binding” and “growth factor activity,” with the binding scope emphasizing **receptor dimer activation via extracellular ligand**, not receptor catalytic activity (fredriksson2004thepdgffamily pages 5-7, ostman1992pdgfaaandpdgfbb pages 1-2).

### 3) Cellular component (CC): secretion, secretory pathway processing, ECM retention, platelet α-granule
#### 3.1 ER/Golgi secretory processing (direct evidence)
Östman et al. (J Cell Biol; Aug 1992; DOI **10.1083/jcb.118.3.509**; https://doi.org/10.1083/jcb.118.3.509) provide direct experimental evidence that PDGF chains **dimerize in the ER** and that **proteolytic processing occurs distal to the ER (Golgi)**. PDGF‑BB formed a **minor secreted ~30 kDa form** and a **major cell-associated ~24 kDa form**; brefeldin A and chloroquine experiments supported ER→Golgi trafficking, Golgi processing, and lysosomal degradation of retained PDGF‑BB (ostman1992pdgfaaandpdgfbb pages 1-2, ostman1992pdgfaaandpdgfbb pages 2-3).

**GO CC recommendation:** annotate secretory pathway involvement as **ER dimerization** and **Golgi processing/trafficking** evidence for a secreted ligand, without over-asserting stable ER/Golgi residence as the mature localization (ostman1992pdgfaaandpdgfbb pages 1-2, ostman1992pdgfaaandpdgfbb pages 2-3).

#### 3.2 Extracellular localization and secretion
PDGF‑AA/AB/BB are described as **secreted in active form**, supporting extracellular localization of mature PDGF‑B-containing ligands (duran2018molecularregulationof pages 9-11).

**GO CC recommendation:** “extracellular region/space” consistent with secreted ligand function (duran2018molecularregulationof pages 9-11).

#### 3.3 Extracellular matrix (ECM)/cell-surface retention via heparan sulfate (HS) (direct in vivo evidence)
Abramsson et al. (Genes & Development; Feb 2007; DOI **10.1101/gad.398207**; https://doi.org/10.1101/gad.398207) provide strong direct evidence that PDGF‑B contains a **conserved C-terminal basic/heparin-binding ‘retention motif’** whose deletion **impairs PDGF‑BB retention** and produces defective vascular mural cell coverage in vivo, consistent with **HS-dependent retention near endothelium** (abramsson2007defectivensulfationof pages 1-2). These findings support a GO-relevant CC concept of **ECM/cell-surface association mediated by HS** rather than purely freely diffusible extracellular localization.

**Figure evidence (visual):** Abramsson et al. figures include (i) images showing reduced pericyte coverage in retention/HS mutants and (ii) a schematic of HS–PDGF‑BB retention motif interaction (abramsson2007defectivensulfationof media b90fa2f5, abramsson2007defectivensulfationof media cfcc7e5d).

#### 3.4 Platelet α-granule localization (explicitly stated; review-level)
Karampini et al. (Arterioscler Thromb Vasc Biol; Jun 2020; DOI **10.1161/ATVBAHA.120.314245**; https://doi.org/10.1161/ATVBAHA.120.314245) explicitly lists **PDGFB** among platelet **α-granule** contents (karampini2020orchestrationofprimary pages 2-3). This supports annotating platelet α-granule localization, with the caveat that this is a **review statement** in the retrieved excerpt (not a primary imaging/proteomics experiment shown here).

### 4) Biological process (BP): ligand-attributable processes with direct support
#### 4.1 Pericyte recruitment/coverage in vascular development (strong direct support)
Abramsson et al. directly connect PDGF‑BB **HS-dependent retention** to **pericyte recruitment/coverage** during vascular development: altering HS sulfation or deleting the PDGF‑B retention motif reduces PDGF‑BB binding/retention and leads to deficient pericyte investment (abramsson2007defectivensulfationof pages 1-2, abramsson2007defectivensulfationof media b90fa2f5). A 2024 authoritative review further summarizes genetic evidence that **Pdgfb/Pdgfrb deficiency causes lethal vascular defects including microvascular bleeding and reduced pericyte coverage**, and specifically cites impaired endothelial PDGF‑B retention phenotypes (published online 9 Jul 2024; DOI **10.1007/s10555-024-10194-7**; https://doi.org/10.1007/s10555-024-10194-7) (strell2024functionalandclinical pages 3-5, strell2024functionalandclinical pages 12-13).

**GO BP recommendation:** “pericyte recruitment,” “pericyte coverage,” or “mural cell recruitment” in vascular development contexts (abramsson2007defectivensulfationof pages 1-2, strell2024functionalandclinical pages 3-5).

#### 4.2 Angiogenesis/blood vessel morphogenesis (supported via mural cell axis)
PDGF‑B/PDGFRβ signaling is summarized as required for vessel function and morphogenesis, with phenotypes including abnormal capillary morphogenesis and endothelial hyperplasia when disrupted; in tumor models, truncation/retention defects in PDGF‑B associate with reduced pericyte coverage and impaired angiogenesis (strell2024functionalandclinical pages 3-5, strell2024functionalandclinical pages 12-13). A comprehensive physiology review also discusses PDGF‑B in new vessel growth contexts and links PDGF‑B/PDGFRβ to mural cell migration/proliferation (DOI **10.1002/cphy.c160048**; https://doi.org/10.1002/cphy.c160048) (duran2018molecularregulationof pages 9-11).

**GO BP recommendation:** “angiogenesis”/“blood vessel morphogenesis,” preferably framed through the **endothelial–mural cell axis** rather than generic proliferation statements (strell2024functionalandclinical pages 3-5, duran2018molecularregulationof pages 9-11).

#### 4.3 Chemotaxis/cell migration and proliferation (limited specificity)
Some retrieved sources describe PDGF ligands broadly as **chemoattractants/mitogens** and discuss PDGF-driven migration/proliferation, but these statements are largely review-level and not always cell-type specific in the provided excerpts (chan2019aninvestigationon pages 24-27, duran2018molecularregulationof pages 9-11). For GO annotation, the strongest support in this evidence set is to annotate **pericyte/mural cell recruitment and related vascular processes**, rather than broad “cell migration” or “cell proliferation” (abramsson2007defectivensulfationof pages 1-2, strell2024functionalandclinical pages 3-5).

#### 4.4 Requested developmental/kidney/mesangial/placenta terms—status
Within the retrieved and excerpted evidence, there is **no direct support** sufficient to annotate PDGFB specifically to: **placenta development, heart development, kidney glomerulus development, or mesangial cell proliferation/migration** (as distinct BP terms) without importing additional primary sources beyond those gathered here (duran2018molecularregulationof pages 9-11, strell2024functionalandclinical pages 3-5).

### 5) Recent developments (prioritizing 2023–2024) and real-world implementations (GO-relevant)
#### 5.1 2023: Engineering PDGF‑BB for ECM retention (localization-focused application)
Alshoubaki et al. (NPJ Regenerative Medicine; May 2023; DOI **10.1038/s41536-023-00297-0**; https://doi.org/10.1038/s41536-023-00297-0) report a translational approach that **increases ECM binding/retention** of therapeutic proteins by fusing an amphiregulin-derived ECM-binding motif; fusion to **PDGF‑BB increased ECM binding affinity (reported 5–50×)** and enhanced local retention in ECM-mimetic matrices compared with wild-type PDGF‑BB (alshoubaki2023asuperiorextracellular pages 3-4). While the excerpt does not reproduce all numeric time-course values, it provides GO-relevant, quantitative assay context including hydrogel composition (e.g., inclusion of **heparan sulfate**), PDGF‑BB loading (**500 ng/ml**), plasmin-triggered release, and typical sample sizes (**n≈4** per time point in the described assays) (alshoubaki2023asuperiorextracellular pages 9-10).

**GO relevance:** supports the general principle that **ECM-binding/retention of PDGF‑BB modulates localization**, but engineered constructs are not direct evidence of native PDGFB CC terms; use primarily as **application context** (alshoubaki2023asuperiorextracellular pages 3-4).

#### 5.2 2024: Authoritative synthesis of PDGF‑BB/PDGFRβ vascular mural cell axis
Strell et al. (Cancer Metastasis Reviews; published online 9 Jul 2024; DOI **10.1007/s10555-024-10194-7**) synthesize genetic and disease evidence highlighting the **PDGF‑BB/PDGFRβ endothelial–mural cell axis** and vascular phenotypes tied to PDGF‑B ligand function (strell2024functionalandclinical pages 3-5, strell2024functionalandclinical pages 1-3).

### 6) Summary table of recommended GO-relevant statements
| GO aspect | Recommended GO concept | Evidence summary | Key supporting citation(s) with DOI/URL | Notes/exclusions |
|---|---|---|---|---|
| MF | PDGF receptor binding | PDGF-B-containing ligands directly bind/activate PDGF receptors; the B-chain binds the α receptor and is required for β receptor binding, with PDGF-BB engaging PDGFRβ-containing dimers and PDGF-AB/BB engaging PDGFRαβ. | Östman et al., 1992, J Cell Biol, DOI: https://doi.org/10.1083/jcb.118.3.509; Fredriksson et al., 2004, DOI: https://doi.org/10.1016/j.cytogfr.2004.03.007; Strell et al., 2024, DOI: https://doi.org/10.1007/s10555-024-10194-7 (ostman1992pdgfaaandpdgfbb pages 1-2, fredriksson2004thepdgffamily pages 5-7, strell2024functionalandclinical pages 1-3) | Annotate ligand binding/activation only; exclude receptor intrinsic kinase activity, transphosphorylation, PI3K-AKT/ERK/MAPK downstream terms. |
| MF | Growth factor activity | PDGF-B is described as a potent mitogen/growth factor for mesenchymal-derived target cells, consistent with canonical growth factor activity. | Östman et al., 1992, DOI: https://doi.org/10.1083/jcb.118.3.509; Duran et al., 2018, DOI: https://doi.org/10.1002/cphy.c160048 (ostman1992pdgfaaandpdgfbb pages 1-2, duran2018molecularregulationof pages 9-11) | Keep broad growth factor activity only where tied to extracellular ligand action, not downstream gene-expression outputs. |
| MF | Secreted disulfide-linked dimer | PDGF family ligands are secreted disulfide-linked dimers, and PDGF-B participates in these active extracellular dimers. | Duran et al., 2018, DOI: https://doi.org/10.1002/cphy.c160048; Strell et al., 2024, DOI: https://doi.org/10.1007/s10555-024-10194-7 (duran2018molecularregulationof pages 9-11, strell2024functionalandclinical pages 1-3) | Structural/biochemical property; do not confuse with receptor dimerization or intracellular receptor complexes. |
| MF | PDGF-BB homodimer and PDGF-AB heterodimer formation | PDGF is assembled as AA, AB, and BB dimers; PDGF-B therefore forms both PDGF-BB homodimer and PDGF-AB heterodimer. | Östman et al., 1992, DOI: https://doi.org/10.1083/jcb.118.3.509; Fredriksson et al., 2004, DOI: https://doi.org/10.1016/j.cytogfr.2004.03.007 (ostman1992pdgfaaandpdgfbb pages 1-2, fredriksson2004thepdgffamily pages 5-7) | Appropriate for complex/dimer formation language; avoid unsupported claims about other isoforms not containing PDGFB. |
| CC | Endoplasmic reticulum dimerization during secretion | Pulse-chase and brefeldin A studies showed newly synthesized PDGF chains dimerize in the ER before later proteolytic processing. | Östman et al., 1992, DOI: https://doi.org/10.1083/jcb.118.3.509 (ostman1992pdgfaaandpdgfbb pages 1-2, ostman1992pdgfaaandpdgfbb pages 2-3) | Best used as secretory-pathway processing support; not evidence for stable ER residency as final localization. |
| CC | Golgi processing / secretory pathway | PDGF-B precursors undergo proteolytic processing distal to the ER in the Golgi, yielding a minor secreted 30-kD form and a major intracellular retained 24-kD form. | Östman et al., 1992, DOI: https://doi.org/10.1083/jcb.118.3.509 (ostman1992pdgfaaandpdgfbb pages 1-2, ostman1992pdgfaaandpdgfbb pages 2-3) | Supports biosynthetic processing, not a final functional localization term at the plasma membrane or cytosol. |
| CC | Extracellular region / extracellular space / secreted protein | PDGF-AA, -AB, and -BB are secreted in active form, supporting extracellular localization of the mature ligand. | Duran et al., 2018, DOI: https://doi.org/10.1002/cphy.c160048; Corsinovi, 2018 (duran2018molecularregulationof pages 9-11, corsinovi2018daniorerioand pages 15-19) | Strong CC support for extracellular/secreted protein; more specific extracellular matrix annotation needs separate retention evidence. |
| CC | Extracellular matrix or cell-surface heparan sulfate-dependent retention via C-terminal basic motif | A conserved C-terminal basic/heparin-binding retention motif in PDGF-B mediates HS-dependent cell-surface/ECM retention, and loss of this motif reduces retention. | Abramsson et al., 2007, Genes Dev, DOI: https://doi.org/10.1101/gad.398207; Fredriksson et al., 2004, DOI: https://doi.org/10.1016/j.cytogfr.2004.03.007 (abramsson2007defectivensulfationof pages 1-2, fredriksson2004thepdgffamily pages 5-7) | Good support for matrix/cell-surface retention of the ligand; distinguish from generic protein binding and from engineered ECM-binding studies. |
| CC | Platelet alpha granule | Review evidence explicitly states PDGFB/PDGF-B is present in platelet α-granules and released with α-granule contents upon activation. | Karampini et al., 2020, DOI: https://doi.org/10.1161/ATVBAHA.120.314245 (karampini2020orchestrationofprimary pages 2-3) | Direct support is review-level rather than a primary localization experiment here; use cautiously if stricter experimental evidence is required. |
| BP | Pericyte recruitment / pericyte coverage during vascular development | Endothelial PDGF-BB is a key ligand for mural cell recruitment, and impaired HS-dependent retention or Pdgfb loss causes defective pericyte investment/coverage. | Abramsson et al., 2007, DOI: https://doi.org/10.1101/gad.398207; Strell et al., 2024, DOI: https://doi.org/10.1007/s10555-024-10194-7 (abramsson2007defectivensulfationof pages 1-2, strell2024functionalandclinical pages 3-5, strell2024functionalandclinical pages 12-13) | Strongly supported BP; preferable to generic “cell migration” because it is directly linked to PDGF-B ligand function in vivo. |
| BP | Angiogenesis / blood vessel morphogenesis | Loss of PDGF-B signaling causes microvascular defects, abnormal capillary morphogenesis, reduced pericyte coverage, and impaired angiogenesis, supporting vascular development roles. | Duran et al., 2018, DOI: https://doi.org/10.1002/cphy.c160048; Strell et al., 2024, DOI: https://doi.org/10.1007/s10555-024-10194-7 (duran2018molecularregulationof pages 9-11, strell2024functionalandclinical pages 3-5, strell2024functionalandclinical pages 12-13) | Attribute to ligand-driven mural cell recruitment and vessel stabilization; exclude receptor downstream signaling terms. |
| BP | Wound healing / granulation tissue formation | PDGF-B/PDGF-BB is described as promoting new vessel growth in wound-healing contexts, and PDGF-BB-stimulated granulation tissue formation is reported in vivo. | Duran et al., 2018, DOI: https://doi.org/10.1002/cphy.c160048; Prasad et al., 2019, DOI: https://doi.org/10.1111/wrr.12744 (via cited evidence summary) (duran2018molecularregulationof pages 9-11) | Support exists, but some cited wound-healing data are from PDGF-BB reagent studies rather than direct human PDGFB gene perturbation; annotate conservatively. |
| BP | Positive regulation of mesenchymal/pericyte/VSMC proliferation and migration/chemotaxis | PDGF-BB directly supports pericyte migration/proliferation and mesenchymal/VSMC recruitment in vascular development, with older literature and reviews also describing PDGF as a chemoattractant/mitogen. | Duran et al., 2018, DOI: https://doi.org/10.1002/cphy.c160048; Abramsson et al., 2007, DOI: https://doi.org/10.1101/gad.398207; Chan, 2019 (duran2018molecularregulationof pages 9-11, abramsson2007defectivensulfationof pages 1-2, chan2019aninvestigationon pages 24-27) | Use only qualified, cell-type-specific terms; avoid broad generic proliferation/migration annotations unless directly tied to PDGF-B ligand action. |


*Table: This table summarizes recommended GO-relevant annotations for human PDGFB based on direct evidence for ligand function, secretion/localization, and supported biological processes. It is useful for separating bona fide PDGFB ligand annotations from excluded receptor-kinase and downstream signaling claims.*

### 7) Key exclusions (to avoid mis-annotation)
Do **not** annotate PDGFB with receptor enzymatic activities (e.g., **protein tyrosine kinase activity**, **peptidyl-tyrosine phosphorylation**) or generic downstream pathways (PI3K/AKT, ERK/MAPK, ROS) based solely on PDGFR signaling descriptions; these belong to PDGF receptors or downstream effectors, not the PDGFB ligand itself (fredriksson2004thepdgffamily pages 5-7, strell2024functionalandclinical pages 3-5).

### 8) Core references (URLs/DOIs; publication dates)
- Östman A. et al. **Aug 1992**. *PDGF-AA and PDGF-BB biosynthesis…* J Cell Biol. DOI: **10.1083/jcb.118.3.509**. https://doi.org/10.1083/jcb.118.3.509 (ostman1992pdgfaaandpdgfbb pages 1-2)
- Abramsson A. et al. **Feb 2007**. *Defective N-sulfation… limits PDGF-BB binding and pericyte recruitment…* Genes Dev. DOI: **10.1101/gad.398207**. https://doi.org/10.1101/gad.398207 (abramsson2007defectivensulfationof pages 1-2)
- Fredriksson L. et al. **Aug 2004**. *The PDGF family: four gene products form five dimeric isoforms.* Cytokine Growth Factor Rev. DOI: **10.1016/j.cytogfr.2004.03.007**. https://doi.org/10.1016/j.cytogfr.2004.03.007 (fredriksson2004thepdgffamily pages 5-7)
- Karampini E. et al. **Jun 2020**. *Orchestration of primary hemostasis…* ATVB. DOI: **10.1161/ATVBAHA.120.314245**. https://doi.org/10.1161/ATVBAHA.120.314245 (karampini2020orchestrationofprimary pages 2-3)
- Alshoubaki YK. et al. **May 2023**. *A superior extracellular matrix binding motif…* NPJ Regen Med. DOI: **10.1038/s41536-023-00297-0**. https://doi.org/10.1038/s41536-023-00297-0 (alshoubaki2023asuperiorextracellular pages 3-4)
- Strell C. et al. **Jul 2024** (online 9 Jul 2024). *Functional and clinical roles of stromal PDGF receptors in tumor biology.* Cancer Metastasis Rev. DOI: **10.1007/s10555-024-10194-7**. https://doi.org/10.1007/s10555-024-10194-7 (strell2024functionalandclinical pages 1-3)



References

1. (ostman1992pdgfaaandpdgfbb pages 1-2): A. Östman, J. Thyberg, B. Westermark, and C. Heldin. Pdgf-aa and pdgf-bb biosynthesis: proprotein processing in the golgi complex and lysosomal degradation of pdgf-bb retained intracellularly. The Journal of Cell Biology, 118:509-519, Aug 1992. URL: https://doi.org/10.1083/jcb.118.3.509, doi:10.1083/jcb.118.3.509. This article has 120 citations.

2. (fredriksson2004thepdgffamily pages 5-7): Linda Fredriksson, Hong Li, and Ulf Eriksson. The pdgf family: four gene products form five dimeric isoforms. Cytokine & growth factor reviews, 15 4:197-204, Aug 2004. URL: https://doi.org/10.1016/j.cytogfr.2004.03.007, doi:10.1016/j.cytogfr.2004.03.007. This article has 1215 citations and is from a peer-reviewed journal.

3. (duran2018molecularregulationof pages 9-11): Camille L. Duran, David W. Howell, J. Dave, Rebecca Smith, M. Torrie, J. Essner, and K. Bayless. Molecular regulation of sprouting angiogenesis. Comprehensive Physiology, 8 1:153-235, Dec 2018. URL: https://doi.org/10.1002/cphy.c160048, doi:10.1002/cphy.c160048. This article has 107 citations and is from a peer-reviewed journal.

4. (strell2024functionalandclinical pages 3-5): Carina Strell, Elisabet Rodríguez-Tomàs, and Arne Östman. Functional and clinical roles of stromal pdgf receptors in tumor biology. Cancer Metastasis Reviews, 43:1593-1609, Jul 2024. URL: https://doi.org/10.1007/s10555-024-10194-7, doi:10.1007/s10555-024-10194-7. This article has 26 citations.

5. (strell2024functionalandclinical pages 1-3): Carina Strell, Elisabet Rodríguez-Tomàs, and Arne Östman. Functional and clinical roles of stromal pdgf receptors in tumor biology. Cancer Metastasis Reviews, 43:1593-1609, Jul 2024. URL: https://doi.org/10.1007/s10555-024-10194-7, doi:10.1007/s10555-024-10194-7. This article has 26 citations.

6. (ostman1992pdgfaaandpdgfbb pages 2-3): A. Östman, J. Thyberg, B. Westermark, and C. Heldin. Pdgf-aa and pdgf-bb biosynthesis: proprotein processing in the golgi complex and lysosomal degradation of pdgf-bb retained intracellularly. The Journal of Cell Biology, 118:509-519, Aug 1992. URL: https://doi.org/10.1083/jcb.118.3.509, doi:10.1083/jcb.118.3.509. This article has 120 citations.

7. (abramsson2007defectivensulfationof pages 1-2): Alexandra Abramsson, Sindhulakshmi Kurup, Marta Busse, Shuhei Yamada, Per Lindblom, Edith Schallmeiner, Denise Stenzel, Dominique Sauvaget, Johan Ledin, Maria Ringvall, Ulf Landegren, Lena Kjellén, Göran Bondjers, Jin-ping Li, Ulf Lindahl, Dorothe Spillmann, Christer Betsholtz, and Holger Gerhardt. Defective n-sulfation of heparan sulfate proteoglycans limits pdgf-bb binding and pericyte recruitment in vascular development. Genes & development, 21 3:316-31, Feb 2007. URL: https://doi.org/10.1101/gad.398207, doi:10.1101/gad.398207. This article has 239 citations and is from a highest quality peer-reviewed journal.

8. (abramsson2007defectivensulfationof media b90fa2f5): Alexandra Abramsson, Sindhulakshmi Kurup, Marta Busse, Shuhei Yamada, Per Lindblom, Edith Schallmeiner, Denise Stenzel, Dominique Sauvaget, Johan Ledin, Maria Ringvall, Ulf Landegren, Lena Kjellén, Göran Bondjers, Jin-ping Li, Ulf Lindahl, Dorothe Spillmann, Christer Betsholtz, and Holger Gerhardt. Defective n-sulfation of heparan sulfate proteoglycans limits pdgf-bb binding and pericyte recruitment in vascular development. Genes & development, 21 3:316-31, Feb 2007. URL: https://doi.org/10.1101/gad.398207, doi:10.1101/gad.398207. This article has 239 citations and is from a highest quality peer-reviewed journal.

9. (abramsson2007defectivensulfationof media cfcc7e5d): Alexandra Abramsson, Sindhulakshmi Kurup, Marta Busse, Shuhei Yamada, Per Lindblom, Edith Schallmeiner, Denise Stenzel, Dominique Sauvaget, Johan Ledin, Maria Ringvall, Ulf Landegren, Lena Kjellén, Göran Bondjers, Jin-ping Li, Ulf Lindahl, Dorothe Spillmann, Christer Betsholtz, and Holger Gerhardt. Defective n-sulfation of heparan sulfate proteoglycans limits pdgf-bb binding and pericyte recruitment in vascular development. Genes & development, 21 3:316-31, Feb 2007. URL: https://doi.org/10.1101/gad.398207, doi:10.1101/gad.398207. This article has 239 citations and is from a highest quality peer-reviewed journal.

10. (karampini2020orchestrationofprimary pages 2-3): Ellie Karampini, Ruben Bierings, and Jan Voorberg. Orchestration of primary hemostasis by platelet and endothelial lysosome-related organelles. Arteriosclerosis, Thrombosis, and Vascular Biology, 40:1441-1453, Jun 2020. URL: https://doi.org/10.1161/atvbaha.120.314245, doi:10.1161/atvbaha.120.314245. This article has 63 citations and is from a domain leading peer-reviewed journal.

11. (strell2024functionalandclinical pages 12-13): Carina Strell, Elisabet Rodríguez-Tomàs, and Arne Östman. Functional and clinical roles of stromal pdgf receptors in tumor biology. Cancer Metastasis Reviews, 43:1593-1609, Jul 2024. URL: https://doi.org/10.1007/s10555-024-10194-7, doi:10.1007/s10555-024-10194-7. This article has 26 citations.

12. (chan2019aninvestigationon pages 24-27): CPSL Chan. An investigation on the role of non-canonical hedgehog signalling in cell migration. Unknown journal, 2019.

13. (alshoubaki2023asuperiorextracellular pages 3-4): Yasmin K. Alshoubaki, Yen-Zhen Lu, Julien M. D. Legrand, Rezvan Karami, Mathilde Fossat, Ekaterina Salimova, Ziad Julier, and Mikaël M. Martino. A superior extracellular matrix binding motif to enhance the regenerative activity and safety of therapeutic proteins. NPJ Regenerative Medicine, May 2023. URL: https://doi.org/10.1038/s41536-023-00297-0, doi:10.1038/s41536-023-00297-0. This article has 14 citations and is from a peer-reviewed journal.

14. (alshoubaki2023asuperiorextracellular pages 9-10): Yasmin K. Alshoubaki, Yen-Zhen Lu, Julien M. D. Legrand, Rezvan Karami, Mathilde Fossat, Ekaterina Salimova, Ziad Julier, and Mikaël M. Martino. A superior extracellular matrix binding motif to enhance the regenerative activity and safety of therapeutic proteins. NPJ Regenerative Medicine, May 2023. URL: https://doi.org/10.1038/s41536-023-00297-0, doi:10.1038/s41536-023-00297-0. This article has 14 citations and is from a peer-reviewed journal.

15. (corsinovi2018daniorerioand pages 15-19): D Corsinovi. Danio rerio and xenopus laevis embryos: alternative and valuable models to unveil new molecular mechanisms involved in glioma progression. Unknown journal, 2018.

## Citations

1. ostman1992pdgfaaandpdgfbb pages 1-2
2. strell2024functionalandclinical pages 1-3
3. fredriksson2004thepdgffamily pages 5-7
4. duran2018molecularregulationof pages 9-11
5. abramsson2007defectivensulfationof pages 1-2
6. karampini2020orchestrationofprimary pages 2-3
7. alshoubaki2023asuperiorextracellular pages 3-4
8. alshoubaki2023asuperiorextracellular pages 9-10
9. strell2024functionalandclinical pages 3-5
10. ostman1992pdgfaaandpdgfbb pages 2-3
11. strell2024functionalandclinical pages 12-13
12. chan2019aninvestigationon pages 24-27
13. corsinovi2018daniorerioand pages 15-19
14. https://doi.org/10.1083/jcb.118.3.509
15. https://doi.org/10.1101/gad.398207
16. https://doi.org/10.1161/ATVBAHA.120.314245
17. https://doi.org/10.1007/s10555-024-10194-7
18. https://doi.org/10.1002/cphy.c160048
19. https://doi.org/10.1038/s41536-023-00297-0
20. https://doi.org/10.1083/jcb.118.3.509;
21. https://doi.org/10.1016/j.cytogfr.2004.03.007;
22. https://doi.org/10.1002/cphy.c160048;
23. https://doi.org/10.1016/j.cytogfr.2004.03.007
24. https://doi.org/10.1101/gad.398207;
25. https://doi.org/10.1111/wrr.12744
26. https://doi.org/10.1083/jcb.118.3.509,
27. https://doi.org/10.1016/j.cytogfr.2004.03.007,
28. https://doi.org/10.1002/cphy.c160048,
29. https://doi.org/10.1007/s10555-024-10194-7,
30. https://doi.org/10.1101/gad.398207,
31. https://doi.org/10.1161/atvbaha.120.314245,
32. https://doi.org/10.1038/s41536-023-00297-0,