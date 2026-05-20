---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T14:44:04.742386'
end_time: '2026-05-12T14:59:10.727578'
duration_seconds: 905.99
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

Concise GO annotation research for human IL15 / UniProt P40933. Focus only on GO-relevant evidence: IL15 cytokine activity; high-affinity binding to IL15RA and signaling through IL2RB/IL2RG; IL15 trans-presentation by IL15RA versus soluble/secreted cytokine activity; NK cell, CD8 T cell, T cell, B cell and neutrophil proliferation/activation/survival; positive regulation of cytokine production and immune response; JAK1/JAK3, STAT3/STAT5 signaling; isoform-specific localization of secreted IL15-S48AA versus intracellular IL15-S21AA cytoplasm/nucleus; caveats for generic protein binding, broad cell population proliferation, and over-broad immune/developmental process annotations. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human IL15 / UniProt P40933. Focus only on GO-relevant evidence: IL15 cytokine activity; high-affinity binding to IL15RA and signaling through IL2RB/IL2RG; IL15 trans-presentation by IL15RA versus soluble/secreted cytokine activity; NK cell, CD8 T cell, T cell, B cell and neutrophil proliferation/activation/survival; positive regulation of cytokine production and immune response; JAK1/JAK3, STAT3/STAT5 signaling; isoform-specific localization of secreted IL15-S48AA versus intracellular IL15-S21AA cytoplasm/nucleus; caveats for generic protein binding, broad cell population proliferation, and over-broad immune/developmental process annotations. Include PMID/DOI citations and keep under 1500 words.

## Concise GO annotation research report: Human IL15 (UniProt P40933)

### Scope and approach
This report summarizes **GO-relevant** mechanistic evidence for human IL-15 (IL15; UniProt **P40933**) focusing on (i) cytokine activity, (ii) **high-affinity IL15RA binding** and signaling via **IL2RB/IL2RG**, (iii) **IL-15 trans-presentation** versus soluble IL-15/IL-15Rα activity, (iv) downstream **JAK1/JAK3 → STAT3/STAT5** signaling, (v) leukocyte functional outcomes (NK, CD8 T, T, B, neutrophils), and (vi) **isoform-specific localization** determined by alternative signal peptides (48-aa vs 21-aa). Evidence is prioritized for 2023–2024 where possible; however, key GO assertions rely on foundational mechanistic studies.

### 1) Key concepts and definitions (current understanding)

#### IL-15 as a cytokine and receptor system
IL-15 is a common γ-chain (γc) cytokine that signals through a **heterotrimeric receptor system**: a private **IL-15Rα (IL15RA/CD215)** chain and shared signaling chains **IL-2Rβ (IL2RB/CD122)** and **γc (IL2RG/CD132)**. (skariah2024signallingmechanismsdriving pages 2-3)

A central concept for GO curation is that IL-15 is not best modeled as a freely diffusing cytokine under physiologic conditions. Instead, IL-15 is commonly delivered by **trans-presentation**: an “IL-15-presenting” cell displays a **membrane IL-15/IL-15Rα complex** that stimulates neighboring lymphocytes through **IL2RB/IL2RG**. (skariah2024signallingmechanismsdriving pages 2-3, skariah2024signallingmechanismsdriving pages 3-3)

#### Trans-presentation vs soluble cytokine activity
Recent synthesis emphasizes that **soluble IL-15 is rarely detected as ‘free’ IL-15** in serum; rather, it is found **complexed with soluble IL-15Rα** (heterodimeric IL-15/IL-15Rα), which can also stimulate IL2RB/IL2RG on lymphocytes. (skariah2024signallingmechanismsdriving pages 2-3, skariah2024signallingmechanismsdriving pages 10-11)

### 2) Recent developments and latest research (prioritize 2023–2024)

A 2024 mechanistic review integrates current understanding that IL-15 is controlled at multiple levels (mRNA translation, trafficking, receptor chaperoning), and that **IL-15Rα serves as both a high-affinity binding partner and a chaperone** that stabilizes IL-15 and supports surface display and trans-presentation. (Skariah et al., 2024-01, *Discovery Immunology*, DOI: **10.1093/discim/kyae002**, URL: https://doi.org/10.1093/discim/kyae002) (skariah2024signallingmechanismsdriving pages 4-5, skariah2024signallingmechanismsdriving pages 2-3)

This review also highlights downstream signaling branches relevant to GO BP terms (JAK/STAT; PI3K/AKT/mTOR; MAPK) and connects IL-15 to tissue lymphocyte homeostasis and inflammation. (skariah2024signallingmechanismsdriving pages 7-8, skariah2024signallingmechanismsdriving pages 8-8)

### 3) Molecular function evidence (GO: Molecular Function)

#### High-affinity binding to IL15RA and recruitment of IL2RB/IL2RG
A definitive biochemical mapping study identified IL-15 residues required for **IL-15Rα binding** and implicated additional residues in **IL-2Rβ recruitment** (thus supporting specific receptor-binding MF annotations rather than generic “protein binding”). (Bernard et al., 2004-06, *J Biol Chem*, DOI: **10.1074/jbc.M312458200**, URL: https://doi.org/10.1074/jbc.M312458200) (bernard2004identificationofan pages 1-2, bernard2004identificationofan pages 8-9)

Quantitatively, this study reports tight IL-15:IL-15Rα binding (Kd ≈ **0.05 nM**) and provides mutational effects on affinity and bioactivity (e.g., V49D ~13-fold affinity drop with near WT bioactivity; certain mutations preserve IL-15Rα binding but abrogate activity, consistent with disrupted signaling-chain recruitment). (bernard2004identificationofan pages 1-2, bernard2004identificationofan pages 8-9)

Independent receptor framework evidence (including transfection responsiveness requiring IL-2Rβ and γc) is summarized in a highly cited receptor review. (Waldmann et al., 1998-01, *Int Rev Immunol*, DOI: **10.3109/08830189809042995**, URL: https://doi.org/10.3109/08830189809042995) (waldmann1998interleukin2interleukin15and pages 8-11)

### 4) Signaling evidence (GO: Biological Process—cytokine-mediated signaling; JAK-STAT)

#### JAK1/JAK3 and STAT3/STAT5 activation
Quantitative phosphoproteomics in T-cell lines showed **IL-15 induces tyrosine-phosphorylation/activation of JAK1 and JAK3** and downstream **STAT5** phosphorylation. JAK1 and JAK3 were highly enriched in phosphotyrosine immunocomplexes (reported ratios ~**13** and **20**, respectively), and JAK3 phosphopeptides including **Y980/Y981** were strongly enriched (up to ratio **75**). STAT5 phosphorylation (e.g., STAT5 Y694/Y699 depending on isoform/assay) was validated. (Osinalde et al., 2015-01, *PROTEOMICS*, DOI: **10.1002/pmic.201400194**, URL: https://doi.org/10.1002/pmic.201400194) (osinalde2015simultaneousdissectionand pages 6-7, osinalde2015simultaneousdissectionand pages 7-8)

In immune contexts, IL-15-driven expansion and effector programs are frequently described as JAK/STAT-dependent, and JAK1→STAT3 and JAK3/STAT5 dependencies are emphasized in disease-relevant models (e.g., IL-15-induced STAT3 phosphorylation increased with activating JAK1 mutations and abolished by JAK1 inhibition; JAK3/STAT5 inhibition abolishes NK proliferation). (skariah2024signallingmechanismsdriving pages 7-8)

### 5) Presentation mode and IL-15Rα chaperoning (GO-relevant for trans-presentation and soluble complex activity)

#### IL-15Rα as chaperone and soluble heterodimer
In vivo evidence demonstrates that IL-15Rα can **chaperone IL-15** to yield secreted bioactive **IL-15/IL-15Rα heterodimers**, particularly enabling secretion/activity of the SSP isoform when co-expressed with IL-15Rα. (Bergamaschi et al., 2009-09, *J Immunol*, DOI: **10.4049/jimmunol.0900693**, URL: https://doi.org/10.4049/jimmunol.0900693) (bergamaschi2009secretionandbiological pages 1-2, bergamaschi2009secretionandbiological pages 8-9)

A conceptual and mechanistic review additionally supports that soluble IL-15Rα can extend IL-15 half-life and modulate activity, and provides approximate sizes for soluble receptor species (human ~42 kDa). (Bulfone-Paus et al., 2006-04, *BioEssays*, DOI: **10.1002/bies.20380**, URL: https://doi.org/10.1002/bies.20380) (bulfone‐paus2006theinterleukin‐15interleukin‐15receptor pages 6-8)

### 6) Isoform-specific localization (GO: Cellular Component)

Two human IL-15 precursor isoforms are generated by alternate signal peptides, with identical mature cytokine sequences.

* **48-aa long signal peptide (LSP) isoform**: ER localization and secretion competence. In COS cells, LSP-GFP showed ER staining in the majority of fluorescent cells (~**85%**) and LSP-IL-15 was described as largely secreted (though translation/trafficking can be limiting). (Tagaya et al., 1997-12, *PNAS*, DOI: **10.1073/pnas.94.26.14444**, URL: https://doi.org/10.1073/pnas.94.26.14444) (tagaya1997generationofsecretable pages 4-5)

* **21-aa short signal peptide (SSP) isoform**: not secreted in COS-cell experiments and instead localizes to **cytoplasm and nucleus**, supporting isoform-specific intracellular/nuclear CC annotations. (Tagaya et al., 1997) (tagaya1997generationofsecretable pages 1-2)

Follow-up trafficking work showed LSP-IL-15 has multiple fates (ER entry with glycosylation and secretion vs cytosolic unglycosylated proteasome-targeted species), while SSP-IL-15 does not enter ER and can enter the nucleus. (Kurys et al., 2000-09, *J Biol Chem*, DOI: **10.1074/jbc.M002373200**, URL: https://doi.org/10.1074/jbc.M002373200) (kurys2000thelongsignal pages 4-5, kurys2000thelongsignal pages 1-1)

### 7) Functional outcomes relevant to GO Biological Process annotations

#### NK cells and CD8 T cells (proliferation/activation/survival)
IL-15 supports homeostatic and inflammatory programs in tissue lymphocytes, promoting proliferation and effector differentiation (e.g., NK metabolic activation via mTORC1 to support cytotoxic effector functions). (skariah2024signallingmechanismsdriving pages 8-8, skariah2024signallingmechanismsdriving pages 7-8)

The 2024 synthesis emphasizes IL-15-dependent maintenance of specific lymphocyte populations and effector molecules, supporting BP annotations such as **positive regulation of NK cell proliferation/activation** and **positive regulation of CD8 T cell homeostasis/trafficking**. (skariah2024signallingmechanismsdriving pages 8-8, skariah2024signallingmechanismsdriving pages 10-11)

#### B cells (proliferation, differentiation, immunoglobulin production)
Primary data show IL-15 **costimulates activated human B cell proliferation** (but not resting B cells) and, in combination with **CD40L**, induces **polyclonal Ig secretion** (IgM, IgG1, IgA). Blocking studies demonstrate IL-15 signaling in B cells requires **IL-2Rβ (IL2RB)** but not IL-2Rα, supporting a receptor-signaling GO link that is specific and experimentally tested. (Armitage et al., 1995-01, *J Immunol*, DOI: **10.4049/jimmunol.154.2.483**, URL: https://doi.org/10.4049/jimmunol.154.2.483) (armitage1995il15hasstimulatory pages 1-2, armitage1995il15hasstimulatory pages 4-5)

FDC-derived IL-15 presented in **membrane-bound form** enhances **germinal center B cell proliferation**, consistent with a trans-presentation-like delivery mode in B cell zones. (Park et al., 2004-12, *J Immunol*, DOI: **10.4049/jimmunol.173.11.6676**, URL: https://doi.org/10.4049/jimmunol.173.11.6676) (park2004folliculardendriticcells pages 1-2)

#### Neutrophils (activation, phagocytosis, adhesion, chemotaxis, survival)
A focused neutrophil review summarizes direct IL-15 effects including cytoskeletal rearrangements, enhanced phagocytosis, IL-8 production (via NF-κB/AP-1 activation), and delayed apoptosis, supporting specific neutrophil-focused BP terms. (Cassatella & McDonald, 2000-05, *Curr Opin Hematol*, DOI: **10.1097/00062752-200005000-00008**, URL: https://doi.org/10.1097/00062752-200005000-00008) (cassatella2000interleukin15andits pages 1-2, cassatella2000interleukin15andits pages 3-4)

IL-15 increases neutrophil adhesion onto respiratory epithelial cells and attracts neutrophils in vivo, and is associated with increased CXCL2/MIP-2 and IL-6 production, supporting neutrophil chemotaxis/recruitment and adhesion processes. (Pelletier & Girard, 2005-08, *Clin Exp Immunol*, DOI: **10.1111/j.1365-2249.2005.02861.x**, URL: https://doi.org/10.1111/j.1365-2249.2005.02861.x) (pelletier2005interleukin‐15increasesneutrophil pages 9-11)

### 8) Curation caveats (avoid over-broad GO annotations)

* Avoid generic **“protein binding”** when IL15RA binding is experimentally supported with affinity/mutational mapping (use specific receptor-binding terms). (bernard2004identificationofan pages 1-2)
* Avoid over-broad **“cell population proliferation”** unless the cell type is explicitly assayed; IL-15 effects are lineage- and context-dependent (e.g., strong evidence in NK/CD8 T, activated B cells, neutrophils), and often depend on **trans-presentation**. (skariah2024signallingmechanismsdriving pages 2-3, armitage1995il15hasstimulatory pages 1-2)
* Avoid overly broad immune/developmental process terms not directly supported in the experimental system (e.g., do not infer organism-wide developmental roles from in vitro proliferation or from tumor cell contexts). (bulfone‐paus2006theinterleukin‐15interleukin‐15receptor pages 6-8)
* For cellular component, consider **isoform-specific** annotations: SSP (21 aa) cytoplasm/nucleus vs LSP (48 aa) ER/Golgi/secreted—do not collapse into a single “secreted cytokine” localization if annotating isoforms. (tagaya1997generationofsecretable pages 1-2, kurys2000thelongsignal pages 4-5)

### Evidence-to-GO mapping table
| GO aspect | Suggested GO term name | Evidence summary (1 sentence) | Key experimental system | Key citation details |
|---|---|---|---|---|
| MF | cytokine activity | IL-15 is a γc-family cytokine that exerts pleiotropic immune-enhancing activity on lymphocytes and other leukocytes, supporting a specific cytokine-function annotation rather than generic binding alone. | Human cells; review integrating primary studies | Skariah et al. 2024, *Discovery Immunology*, doi:10.1093/discim/kyae002; Fehniger & Caligiuri 2001, *Blood*, doi:10.1182/blood.v97.1.14 (skariah2024signallingmechanismsdriving pages 2-3, skariah2024signallingmechanismsdriving pages 4-5) |
| MF | interleukin-15 receptor alpha chain binding | Human IL-15 binds IL15RA with very high affinity and mutational mapping identified key IL-15 residues in helices B/C required for IL15RA engagement. | In vitro biochem; peptide scanning; mutagenesis | Bernard et al. 2004, *J Biol Chem*, doi:10.1074/jbc.M312458200; IL-15:IL15RA Kd ≈ 0.05 nM; alternative affinity notation Ka ~10^11 M^-1 in reviews (bernard2004identificationofan pages 1-2, djaafar2008effectsofil15 pages 21-25) |
| MF | cytokine receptor binding involved in IL2RB/IL2RG signaling | After IL15RA engagement, IL-15 recruits the signaling receptor chains IL2RB/IL2RG, with peptide-2 residues contributing to IL-2Rβ/γ recruitment and signaling-competent complex assembly. | In vitro biochem; receptor mapping; transfection | Bernard et al. 2004, *J Biol Chem*, doi:10.1074/jbc.M312458200; Waldmann et al. 1998, *Int Rev Immunol*, doi:10.3109/08830189809042995 (bernard2004identificationofan pages 1-2, waldmann1998interleukin2interleukin15and pages 8-11) |
| BP | cytokine-mediated signaling pathway via trans-presentation | Physiologic IL-15 delivery is dominated by IL15RA-dependent trans-presentation, where membrane IL-15/IL15RA on one cell stimulates IL2RB/IL2RG on adjacent lymphocytes. | Human/mouse immune cells; review with primary support | Skariah et al. 2024, *Discovery Immunology*, doi:10.1093/discim/kyae002; Cloutier et al. 2024, *Front Immunol*, doi:10.3389/fimmu.2024.1404891 (skariah2024signallingmechanismsdriving pages 2-3, skariah2024signallingmechanismsdriving pages 3-3) |
| MF/BP | soluble IL-15/IL-15Rα complex activity | Circulating soluble IL-15 is typically found as IL-15/IL15RA heterodimer, and soluble IL15RA can chaperone/stabilize IL-15 and enhance or modulate activity through IL2RB/IL2RG-bearing cells. | Human/mouse serum; in vivo plasmid expression; review | Bergamaschi et al. 2009, *J Immunol*, doi:10.4049/jimmunol.0900693; Bulfone-Paus et al. 2006, *BioEssays*, doi:10.1002/bies.20380; soluble IL15RA species ~30 kDa mouse/~42 kDa human (bergamaschi2009secretionandbiological pages 1-2, bulfone‐paus2006theinterleukin‐15interleukin‐15receptor pages 6-8) |
| BP | JAK-STAT cascade downstream of IL-15 receptor | IL-15 receptor signaling activates JAK1/JAK3 and predominantly STAT5, with STAT3 also activated in some T-cell/IEL contexts downstream of IL2RB/IL2RG. | Human T cells; T-cell lines; phosphoproteomics; NK review | Osinalde et al. 2015, *PROTEOMICS*, doi:10.1002/pmic.201400194; JAK1/JAK3 phospho-enrichment ratios ~13/~20 and JAK3 Y980/Y981 ratios up to 75; Marzec et al. 2008, *Cancer Res*, doi:10.1158/0008-5472.CAN-07-2403; Nielsen et al. 1998, *Cytokine*, doi:10.1006/cyto.1998.0356 (osinalde2015simultaneousdissectionand pages 6-7, marzec2008differentialeffectsof pages 4-5) |
| BP | positive regulation of natural killer cell proliferation / activation / cytotoxicity | IL-15 is essential for NK-cell development and potently promotes NK proliferation, activation, granzyme/perforin expression, degranulation, and inflammatory cytotoxicity. | Mouse genetics; human/mouse NK cells; recent review | Skariah et al. 2024, *Discovery Immunology*, doi:10.1093/discim/kyae002; Wang & Zhao 2021, *Front Immunol*, doi:10.3389/fimmu.2021.610789; JAK3/STAT5 inhibition abolishes NK proliferation (skariah2024signallingmechanismsdriving pages 7-8, wang2021transcriptionfactorsassociated pages 7-8) |
| BP | positive regulation of CD8-positive alpha-beta T cell homeostasis / survival / trafficking | IL-15 supports memory and tissue CD8 T-cell homeostasis, survival, and tissue trafficking/residency, including induction of CD69 and maintenance of intestinal/tissue-resident CD8 populations. | Mouse genetics; tissue lymphocyte studies; review | Skariah et al. 2024, *Discovery Immunology*, doi:10.1093/discim/kyae002; Berard et al. 2003, *J Immunol*, doi:10.4049/jimmunol.170.10.5018 (skariah2024signallingmechanismsdriving pages 8-8, skariah2024signallingmechanismsdriving pages 10-11) |
| BP | positive regulation of T cell proliferation / activation | IL-15 drives proliferation and activation-marker expression in T cells and can sustain TH1/CD8 programs without the IL-2-associated death phenotype. | Human T cells; cell lines; primary studies/reviews | Djaafar 2008 review summarizing primary data; Campbell et al. 2001, *J Immunol*, doi:10.4049/jimmunol.167.1.553; Lowe et al. 2014, *Genes Immun*, doi:10.1038/gene.2014.3 (djaafar2008effectsofil15 pages 25-29, skariah2024signallingmechanismsdriving pages 4-5) |
| BP | positive regulation of B cell proliferation / differentiation / immunoglobulin production | IL-15 costimulates activated human B-cell proliferation and, with CD40L, induces IgM, IgG1, and IgA secretion via IL2RB-dependent signaling. | Purified human B cells; in vitro culture | Armitage et al. 1995, *J Immunol*, doi:10.4049/jimmunol.154.2.483; anti-IL-2Rβ blocks IL-15-driven B-cell proliferation; Park et al. 2004, *J Immunol*, doi:10.4049/jimmunol.173.11.6676 (armitage1995il15hasstimulatory pages 4-5, park2004folliculardendriticcells pages 1-2) |
| BP | positive regulation of neutrophil survival / phagocytosis / adhesion / chemotaxis | IL-15 directly delays neutrophil apoptosis and enhances phagocytosis, adhesion, IL-8 production, and in vivo recruitment, supporting specific neutrophil-focused process annotations rather than broad leukocyte proliferation terms. | Human neutrophils; in vivo recruitment models | Bouchard et al. 2004, *J Leukoc Biol*, doi:10.1189/jlb.1103585; Ratthé & Girard 2004, *J Leukoc Biol*, doi:10.1189/jlb.0605298; Pelletier & Girard 2005, *Clin Exp Immunol*, doi:10.1111/j.1365-2249.2005.02861.x (cassatella2000interleukin15andits pages 3-4, pelletier2005interleukin‐15increasesneutrophil pages 9-11) |
| CC | extracellular region / secretory pathway localization (48-aa isoform) | The 48-aa long signal peptide isoform enters ER/Golgi trafficking and is the major secretable form, although some molecules are inefficiently translocated and degraded. | COS cells; GFP chimeras; biochemical trafficking assays | Tagaya et al. 1997, *PNAS*, doi:10.1073/pnas.94.26.14444; ~85% of LSP-GFP fluorescent cells showed ER staining; Kurys et al. 2000, *J Biol Chem*, doi:10.1074/jbc.M002373200 (tagaya1997generationofsecretable pages 4-5, kurys2000thelongsignal pages 4-5) |
| CC | cytoplasm / nucleus localization (21-aa isoform) | The 21-aa short signal peptide isoform is largely nonsecreted and localizes to cytoplasmic and nuclear compartments, supporting isoform-specific intracellular annotations. | COS cells; confocal microscopy; fusion constructs | Tagaya et al. 1997, *PNAS*, doi:10.1073/pnas.94.26.14444; Kurys et al. 2000, *J Biol Chem*, doi:10.1074/jbc.M002373200; Bergamaschi et al. 2009, *J Immunol*, doi:10.4049/jimmunol.0900693 (tagaya1997generationofsecretable pages 1-2, kurys2000thelongsignal pages 1-1) |
| Curation note | caveats for GO curation | Prefer specific terms supported by direct assays (cytokine activity, IL15RA binding, trans-presentation, NK/CD8/B/neutrophil processes, JAK/STAT signaling, isoform-localization) and avoid generic “protein binding,” broad “cell population proliferation,” or over-broad immune/developmental annotations unless directly tested in the relevant lineage/context. | GO curation synthesis from evidence above | Specific receptor/functional evidence comes from Bernard 2004, Tagaya 1997, Kurys 2000, Armitage 1995, Skariah 2024, and neutrophil/NK studies above; broad claims should not be inferred beyond assayed cell types or delivery modes (bernard2004identificationofan pages 1-2, tagaya1997generationofsecretable pages 4-5) |


*Table: This table summarizes GO-relevant evidence for human IL15 (UniProt P40933), linking molecular function, biological process, and cellular component annotations to primary mechanistic studies and a recent 2024 review. It is designed to support concise, evidence-based curation and highlight important annotation caveats.*



References

1. (skariah2024signallingmechanismsdriving pages 2-3): Neema Skariah, Olivia J James, and Mahima Swamy. Signalling mechanisms driving homeostatic and inflammatory effects of interleukin-15 on tissue lymphocytes. Discovery Immunology, Jan 2024. URL: https://doi.org/10.1093/discim/kyae002, doi:10.1093/discim/kyae002. This article has 29 citations.

2. (skariah2024signallingmechanismsdriving pages 3-3): Neema Skariah, Olivia J James, and Mahima Swamy. Signalling mechanisms driving homeostatic and inflammatory effects of interleukin-15 on tissue lymphocytes. Discovery Immunology, Jan 2024. URL: https://doi.org/10.1093/discim/kyae002, doi:10.1093/discim/kyae002. This article has 29 citations.

3. (skariah2024signallingmechanismsdriving pages 10-11): Neema Skariah, Olivia J James, and Mahima Swamy. Signalling mechanisms driving homeostatic and inflammatory effects of interleukin-15 on tissue lymphocytes. Discovery Immunology, Jan 2024. URL: https://doi.org/10.1093/discim/kyae002, doi:10.1093/discim/kyae002. This article has 29 citations.

4. (skariah2024signallingmechanismsdriving pages 4-5): Neema Skariah, Olivia J James, and Mahima Swamy. Signalling mechanisms driving homeostatic and inflammatory effects of interleukin-15 on tissue lymphocytes. Discovery Immunology, Jan 2024. URL: https://doi.org/10.1093/discim/kyae002, doi:10.1093/discim/kyae002. This article has 29 citations.

5. (skariah2024signallingmechanismsdriving pages 7-8): Neema Skariah, Olivia J James, and Mahima Swamy. Signalling mechanisms driving homeostatic and inflammatory effects of interleukin-15 on tissue lymphocytes. Discovery Immunology, Jan 2024. URL: https://doi.org/10.1093/discim/kyae002, doi:10.1093/discim/kyae002. This article has 29 citations.

6. (skariah2024signallingmechanismsdriving pages 8-8): Neema Skariah, Olivia J James, and Mahima Swamy. Signalling mechanisms driving homeostatic and inflammatory effects of interleukin-15 on tissue lymphocytes. Discovery Immunology, Jan 2024. URL: https://doi.org/10.1093/discim/kyae002, doi:10.1093/discim/kyae002. This article has 29 citations.

7. (bernard2004identificationofan pages 1-2): Jérôme Bernard, Catherine Harb, Erwan Mortier, Agnès Quéméner, Rob H. Meloen, Claudine Vermot-Desroches, John Wijdeness, Peter van Dijken, Joachim Grötzinger, Jerry W. Slootstra, Ariane Plet, and Yannick Jacques. Identification of an interleukin-15α receptor-binding site on human interleukin-15*. Journal of Biological Chemistry, 279:24313-24322, Jun 2004. URL: https://doi.org/10.1074/jbc.m312458200, doi:10.1074/jbc.m312458200. This article has 104 citations and is from a domain leading peer-reviewed journal.

8. (bernard2004identificationofan pages 8-9): Jérôme Bernard, Catherine Harb, Erwan Mortier, Agnès Quéméner, Rob H. Meloen, Claudine Vermot-Desroches, John Wijdeness, Peter van Dijken, Joachim Grötzinger, Jerry W. Slootstra, Ariane Plet, and Yannick Jacques. Identification of an interleukin-15α receptor-binding site on human interleukin-15*. Journal of Biological Chemistry, 279:24313-24322, Jun 2004. URL: https://doi.org/10.1074/jbc.m312458200, doi:10.1074/jbc.m312458200. This article has 104 citations and is from a domain leading peer-reviewed journal.

9. (waldmann1998interleukin2interleukin15and pages 8-11): Thomas Waldmann, Yutaka Tagaya, and Richard Bamford. Interleukin-2, interleukin-15, and their receptors. International reviews of immunology, 16 3-4:205-26, Jan 1998. URL: https://doi.org/10.3109/08830189809042995, doi:10.3109/08830189809042995. This article has 254 citations and is from a peer-reviewed journal.

10. (osinalde2015simultaneousdissectionand pages 6-7): Nerea Osinalde, Virginia Sanchez‐Quiles, Vyacheslav Akimov, Barbara Guerra, Blagoy Blagoev, and Irina Kratchmarova. Simultaneous dissection and comparison of il‐2 and il‐15 signaling pathways by global quantitative phosphoproteomics. PROTEOMICS, 15:520-531, Jan 2015. URL: https://doi.org/10.1002/pmic.201400194, doi:10.1002/pmic.201400194. This article has 34 citations and is from a peer-reviewed journal.

11. (osinalde2015simultaneousdissectionand pages 7-8): Nerea Osinalde, Virginia Sanchez‐Quiles, Vyacheslav Akimov, Barbara Guerra, Blagoy Blagoev, and Irina Kratchmarova. Simultaneous dissection and comparison of il‐2 and il‐15 signaling pathways by global quantitative phosphoproteomics. PROTEOMICS, 15:520-531, Jan 2015. URL: https://doi.org/10.1002/pmic.201400194, doi:10.1002/pmic.201400194. This article has 34 citations and is from a peer-reviewed journal.

12. (bergamaschi2009secretionandbiological pages 1-2): Cristina Bergamaschi, Rashmi Jalah, Viraj Kulkarni, Margherita Rosati, Gen-Mu Zhang, Candido Alicea, Andrei S. Zolotukhin, Barbara K. Felber, and George N. Pavlakis. Secretion and biological activity of short signal peptide il-15 is chaperoned by il-15 receptor alpha in vivo1. The Journal of Immunology, 183:3064-3072, Sep 2009. URL: https://doi.org/10.4049/jimmunol.0900693, doi:10.4049/jimmunol.0900693. This article has 81 citations.

13. (bergamaschi2009secretionandbiological pages 8-9): Cristina Bergamaschi, Rashmi Jalah, Viraj Kulkarni, Margherita Rosati, Gen-Mu Zhang, Candido Alicea, Andrei S. Zolotukhin, Barbara K. Felber, and George N. Pavlakis. Secretion and biological activity of short signal peptide il-15 is chaperoned by il-15 receptor alpha in vivo1. The Journal of Immunology, 183:3064-3072, Sep 2009. URL: https://doi.org/10.4049/jimmunol.0900693, doi:10.4049/jimmunol.0900693. This article has 81 citations.

14. (bulfone‐paus2006theinterleukin‐15interleukin‐15receptor pages 6-8): Silvia Bulfone‐Paus, Elena Bulanova, Vadim Budagian, and Ralf Paus. The interleukin‐15/interleukin‐15 receptor system as a model for juxtacrine and reverse signaling. BioEssays, 28:362-377, Apr 2006. URL: https://doi.org/10.1002/bies.20380, doi:10.1002/bies.20380. This article has 91 citations and is from a peer-reviewed journal.

15. (tagaya1997generationofsecretable pages 4-5): Yutaka Tagaya, Gloria Kurys, Tiffany A. Thies, Jacqueline M. Losi, Nazli Azimi, John A. Hanover, Richard N. Bamford, and Thomas A. Waldmann. Generation of secretable and nonsecretable interleukin 15 isoforms through alternate usage of signal peptides. Proceedings of the National Academy of Sciences of the United States of America, 94 26:14444-9, Dec 1997. URL: https://doi.org/10.1073/pnas.94.26.14444, doi:10.1073/pnas.94.26.14444. This article has 277 citations and is from a highest quality peer-reviewed journal.

16. (tagaya1997generationofsecretable pages 1-2): Yutaka Tagaya, Gloria Kurys, Tiffany A. Thies, Jacqueline M. Losi, Nazli Azimi, John A. Hanover, Richard N. Bamford, and Thomas A. Waldmann. Generation of secretable and nonsecretable interleukin 15 isoforms through alternate usage of signal peptides. Proceedings of the National Academy of Sciences of the United States of America, 94 26:14444-9, Dec 1997. URL: https://doi.org/10.1073/pnas.94.26.14444, doi:10.1073/pnas.94.26.14444. This article has 277 citations and is from a highest quality peer-reviewed journal.

17. (kurys2000thelongsignal pages 4-5): Gloria Kurys, Yutaka Tagaya, Richard Bamford, John A. Hanover, and Thomas A. Waldmann. The long signal peptide isoform and its alternative processing direct the intracellular trafficking of interleukin-15*. The Journal of Biological Chemistry, 275:30653-30659, Sep 2000. URL: https://doi.org/10.1074/jbc.m002373200, doi:10.1074/jbc.m002373200. This article has 143 citations.

18. (kurys2000thelongsignal pages 1-1): Gloria Kurys, Yutaka Tagaya, Richard Bamford, John A. Hanover, and Thomas A. Waldmann. The long signal peptide isoform and its alternative processing direct the intracellular trafficking of interleukin-15*. The Journal of Biological Chemistry, 275:30653-30659, Sep 2000. URL: https://doi.org/10.1074/jbc.m002373200, doi:10.1074/jbc.m002373200. This article has 143 citations.

19. (armitage1995il15hasstimulatory pages 1-2): R J Armitage, B M Macduff, J Eisenman, R Paxton, and K H Grabstein. Il-15 has stimulatory activity for the induction of b cell proliferation and differentiation. Journal of immunology, 154 2:483-90, Jan 1995. URL: https://doi.org/10.4049/jimmunol.154.2.483, doi:10.4049/jimmunol.154.2.483. This article has 598 citations and is from a domain leading peer-reviewed journal.

20. (armitage1995il15hasstimulatory pages 4-5): R J Armitage, B M Macduff, J Eisenman, R Paxton, and K H Grabstein. Il-15 has stimulatory activity for the induction of b cell proliferation and differentiation. Journal of immunology, 154 2:483-90, Jan 1995. URL: https://doi.org/10.4049/jimmunol.154.2.483, doi:10.4049/jimmunol.154.2.483. This article has 598 citations and is from a domain leading peer-reviewed journal.

21. (park2004folliculardendriticcells pages 1-2): Chan-Sik Park, Sun-Ok Yoon, Richard J. Armitage, and Yong Sung Choi. Follicular dendritic cells produce il-15 that enhances germinal center b cell proliferation in membrane-bound form1. The Journal of Immunology, 173:6676-6683, Dec 2004. URL: https://doi.org/10.4049/jimmunol.173.11.6676, doi:10.4049/jimmunol.173.11.6676. This article has 162 citations.

22. (cassatella2000interleukin15andits pages 1-2): Marco A. Cassatella and Patrick P. McDonald. Interleukin-15 and its impact on neutrophil function. Current Opinion in Hematology, 7:174-177, May 2000. URL: https://doi.org/10.1097/00062752-200005000-00008, doi:10.1097/00062752-200005000-00008. This article has 72 citations and is from a peer-reviewed journal.

23. (cassatella2000interleukin15andits pages 3-4): Marco A. Cassatella and Patrick P. McDonald. Interleukin-15 and its impact on neutrophil function. Current Opinion in Hematology, 7:174-177, May 2000. URL: https://doi.org/10.1097/00062752-200005000-00008, doi:10.1097/00062752-200005000-00008. This article has 72 citations and is from a peer-reviewed journal.

24. (pelletier2005interleukin‐15increasesneutrophil pages 9-11): Martin Pelletier and Denis Girard. Interleukin‐15 increases neutrophil adhesion onto human respiratory epithelial a549 cells and attracts neutrophils in vivo. Clinical & Experimental Immunology, Aug 2005. URL: https://doi.org/10.1111/j.1365-2249.2005.02861.x, doi:10.1111/j.1365-2249.2005.02861.x. This article has 42 citations and is from a peer-reviewed journal.

25. (djaafar2008effectsofil15 pages 21-25): S Djaafar. Effects of il-15 and its specific inhibitor, the mutant il-15/fcγ2a protein, on bone turnover: new players in osteoimmunology. Unknown journal, 2008.

26. (marzec2008differentialeffectsof pages 4-5): Michal Marzec, Krzysztof Halasa, Monika Kasprzycka, Maria Wysocka, Xiaobin Liu, John W. Tobias, Donald Baldwin, Qian Zhang, Niels Odum, Alain H. Rook, and Mariusz A. Wasik. Differential effects of interleukin-2 and interleukin-15 versus interleukin-21 on cd4+ cutaneous t-cell lymphoma cells. Cancer research, 68 4:1083-91, Feb 2008. URL: https://doi.org/10.1158/0008-5472.can-07-2403, doi:10.1158/0008-5472.can-07-2403. This article has 104 citations and is from a highest quality peer-reviewed journal.

27. (wang2021transcriptionfactorsassociated pages 7-8): Xiang Wang and Xiang-Yu Zhao. Transcription factors associated with il-15 cytokine signaling during nk cell development. Frontiers in Immunology, Mar 2021. URL: https://doi.org/10.3389/fimmu.2021.610789, doi:10.3389/fimmu.2021.610789. This article has 144 citations and is from a peer-reviewed journal.

28. (djaafar2008effectsofil15 pages 25-29): S Djaafar. Effects of il-15 and its specific inhibitor, the mutant il-15/fcγ2a protein, on bone turnover: new players in osteoimmunology. Unknown journal, 2008.

## Citations

1. skariah2024signallingmechanismsdriving pages 2-3
2. skariah2024signallingmechanismsdriving pages 7-8
3. tagaya1997generationofsecretable pages 4-5
4. tagaya1997generationofsecretable pages 1-2
5. park2004folliculardendriticcells pages 1-2
6. bernard2004identificationofan pages 1-2
7. skariah2024signallingmechanismsdriving pages 3-3
8. skariah2024signallingmechanismsdriving pages 10-11
9. skariah2024signallingmechanismsdriving pages 4-5
10. skariah2024signallingmechanismsdriving pages 8-8
11. bernard2004identificationofan pages 8-9
12. osinalde2015simultaneousdissectionand pages 6-7
13. osinalde2015simultaneousdissectionand pages 7-8
14. bergamaschi2009secretionandbiological pages 1-2
15. bergamaschi2009secretionandbiological pages 8-9
16. kurys2000thelongsignal pages 4-5
17. kurys2000thelongsignal pages 1-1
18. marzec2008differentialeffectsof pages 4-5
19. wang2021transcriptionfactorsassociated pages 7-8
20. https://doi.org/10.1093/discim/kyae002
21. https://doi.org/10.1074/jbc.M312458200
22. https://doi.org/10.3109/08830189809042995
23. https://doi.org/10.1002/pmic.201400194
24. https://doi.org/10.4049/jimmunol.0900693
25. https://doi.org/10.1002/bies.20380
26. https://doi.org/10.1073/pnas.94.26.14444
27. https://doi.org/10.1074/jbc.M002373200
28. https://doi.org/10.4049/jimmunol.154.2.483
29. https://doi.org/10.4049/jimmunol.173.11.6676
30. https://doi.org/10.1097/00062752-200005000-00008
31. https://doi.org/10.1111/j.1365-2249.2005.02861.x
32. https://doi.org/10.1093/discim/kyae002,
33. https://doi.org/10.1074/jbc.m312458200,
34. https://doi.org/10.3109/08830189809042995,
35. https://doi.org/10.1002/pmic.201400194,
36. https://doi.org/10.4049/jimmunol.0900693,
37. https://doi.org/10.1002/bies.20380,
38. https://doi.org/10.1073/pnas.94.26.14444,
39. https://doi.org/10.1074/jbc.m002373200,
40. https://doi.org/10.4049/jimmunol.154.2.483,
41. https://doi.org/10.4049/jimmunol.173.11.6676,
42. https://doi.org/10.1097/00062752-200005000-00008,
43. https://doi.org/10.1111/j.1365-2249.2005.02861.x,
44. https://doi.org/10.1158/0008-5472.can-07-2403,
45. https://doi.org/10.3389/fimmu.2021.610789,