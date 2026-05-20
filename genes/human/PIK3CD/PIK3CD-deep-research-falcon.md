---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T09:51:43.581323'
end_time: '2026-05-12T10:05:46.915578'
duration_seconds: 843.33
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

Perform concise GO-focused deep research on the human PIK3CD gene (UniProt O00329; phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit delta isoform / PI3K p110-delta). Summarize the core molecular function, major biological processes, cellular locations, key experimental evidence, immune-cell signaling context, disease context only where relevant to function, and GO annotation caveats. Include PMID or DOI citations where available, and keep the report focused for gene annotation review.

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

Perform concise GO-focused deep research on the human PIK3CD gene (UniProt O00329; phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit delta isoform / PI3K p110-delta). Summarize the core molecular function, major biological processes, cellular locations, key experimental evidence, immune-cell signaling context, disease context only where relevant to function, and GO annotation caveats. Include PMID or DOI citations where available, and keep the report focused for gene annotation review.

# GO-focused deep research report: human **PIK3CD** (UniProt O00329; PI3K p110δ)

## 0) Gene/product synopsis (annotation scope)
**PIK3CD** encodes the catalytic subunit **p110δ** of **class IA phosphoinositide 3-kinase (PI3Kδ)**, a lipid kinase that produces **PI(3,4,5)P3 (PIP3)** at membranes downstream of receptor signaling in immune cells, particularly in lymphocytes. p110δ acts as a heterodimer with **p85-family regulatory subunits**, and receptor-triggered recruitment/relief of p85 inhibition is central to its regulated activity. (ijspeert2024hyperactivationofthe pages 2-4, ijspeert2024hyperactivationofthe pages 1-2)

**Canonical record for protein identity**: UniProt O00329 (https://www.uniprot.org/uniprotkb/O00329/). (No UniProt text was retrieved via tools; URL provided for curator convenience.)

## 1) Key GO concepts and definitions (current understanding)
### 1.1 Molecular function (MF): what p110δ *does biochemically*
**Core enzymatic activity (lipid phosphorylation at D3 position):** Class I PI3Ks phosphorylate membrane inositol phospholipids at the **3′ position**; class IA enzymes (including p110δ) act on PI(4,5)P2 to generate **PIP3**, which serves as a membrane docking lipid for downstream signaling proteins. (ijspeert2024hyperactivationofthe pages 1-2, stokoe2005thephosphoinositide3kinase pages 1-3)

**ATP dependence / catalytic-site context:** PI3Kδ catalysis requires ATP; this is strongly supported indirectly by inhibitor mechanism studies contrasting **ATP-competitive** inhibitors (idelalisib) with **non–ATP-competitive** allosteric PI3Kδ inhibition (IOA-244), which alters enzyme kinetics consistent with catalytic-site ATP usage in the reaction. (johnson2023ioa244isa pages 6-7)

### 1.2 Cellular component (CC): where p110δ is and what complex it is part of
**Class IA PI3K complex membership:** Class IA PI3Ks function as **heterodimers of p110 catalytic subunits and p85-family regulatory subunits**; p85 stabilizes and inhibits p110 in resting state. (ijspeert2024hyperactivationofthe pages 2-4, stokoe2005thephosphoinositide3kinase pages 1-3)

**Membrane recruitment as a key localization event:** Upon receptor activation, p85 SH2 domains bind **phosphotyrosine motifs** (e.g., YxxM-containing motifs) on receptors/adaptors, recruiting the p85–p110δ complex to the **plasma membrane**, where phosphoinositide substrates reside and catalytic activity increases. (ijspeert2024hyperactivationofthe pages 2-4, stokoe2005thephosphoinositide3kinase pages 1-3)

### 1.3 Biological process (BP): what p110δ *does in cells/tissues*
**PI3K→AKT→mTOR/FOXO axis:** PIP3 recruits **AKT** to the plasma membrane for phosphorylation (PDK1/mTORC2 context) and downstream regulation of **mTORC1/S6** and **FOXO** transcription factor localization/function. (ijspeert2024hyperactivationofthe pages 2-4, ijspeert2024hyperactivationofthe pages 1-2)

**Immune receptor signaling context:** In immune cells, class IA PI3K (including p110δ) propagates signaling downstream of **BCR, TCR, CD28, ICOS, CD19, BAFF-R, CD40** (and related receptor/adaptor systems), framing the major immune-cell BP terms relevant for PIK3CD. (ijspeert2024hyperactivationofthe pages 2-4)

## 2) Major immune-cell signaling roles with key experimental evidence (curation-relevant)
### 2.1 B cell receptor (BCR) signaling and Ca2+ mobilization (high-confidence genetic evidence)
A foundational genetic study using **p110δ-deficient mice** demonstrates that p110δ is **essential and nonredundant** for effective BCR signaling.

*Key experimental findings (Mol Cell Biol, 2002-12; DOI:10.1128/MCB.22.24.8580-8591.2002; URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002)*:
- **Anti-IgM–induced intracellular Ca2+ mobilization** in p110δ−/− B cells was reduced to **~25% of wild type**, while ionomycin response was preserved, indicating a BCR-proximal signaling defect requiring p110δ. (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole media 9f8002cf)
- Proximal BCR signaling events (e.g., Btk and PLCγ2 tyrosine phosphorylation) occurred comparably, consistent with p110δ acting in the pathway needed for full Ca2+ signaling output. (jou2002essentialnonredundantrole pages 4-8)

**GO interpretation:** supports BP annotations for **B cell receptor signaling pathway** and **intracellular calcium ion mobilization** in B cells, with p110δ as a positive regulator/essential component in this context. (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole media 9f8002cf)

### 2.2 B cell development, activation, proliferation; germinal centers; humoral immunity
In the same p110δ knockout model:
- B cell developmental and compartment defects include reduced mature peripheral B cells and loss of B1 cells. (jou2002essentialnonredundantrole pages 1-2, jou2002essentialnonredundantrole pages 2-4)
- **In vitro proliferation**: p110δ−/− B cells showed decreased proliferation to **anti-CD40** and **LPS**, and impaired responses to BCR crosslinking; bypass stimulation (PMA+ionomycin) was relatively preserved. (jou2002essentialnonredundantrole pages 4-8)
- **Humoral immunity in vivo**: reduced baseline serum immunoglobulins and impaired antigen-specific antibody responses—T-independent responses reduced and **T-dependent antibody responses absent**; **germinal center formation impaired/absent** by splenic staining after immunization. (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole media 9f8002cf)

**Visual evidence from the primary paper** (used here as supporting data displays): ELISA immunoglobulin panels, antigen-response panels, absent germinal center staining, and Ca2+ flux traces in wild-type vs p110δ−/− are captured in the retrieved figure crops. (jou2002essentialnonredundantrole media 9f8002cf, jou2002essentialnonredundantrole media 37876baa, jou2002essentialnonredundantrole media 7d2b61ed, jou2002essentialnonredundantrole media 3b78ec57)

**GO interpretation:** supports BP annotations such as **B cell development**, **B cell activation**, **B cell proliferation**, **germinal center formation**, and **T-dependent humoral immune response**. (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole pages 1-2, jou2002essentialnonredundantrole media 9f8002cf)

### 2.3 Regulatory T cell (Treg) homeostasis and immune tolerance (2024 mechanistic/phenotypic update)
A 2024 conditional mouse model interrogated **activated PI3Kδ signaling specifically within Foxp3+ Tregs**, clarifying how PI3Kδ activity thresholds control tolerance.

*Key recent study (J Immunol, 2024-06; DOI:10.4049/jimmunol.2400032; URL: https://doi.org/10.4049/jimmunol.2400032)*:
- Treg-restricted activated PI3Kδ (**aPIK3CD**) **increased thymic Treg precursors and peripheral Treg numbers**, yet Tregs displayed altered phenotype (e.g., increased PD-1) and reduced competitive fitness. (singh2024activatedpi3kδspecifically pages 1-3)
- Despite increased Treg counts, mice developed **chronic inflammation**, increased memory/effector CD4+/CD8+ T cells and enhanced **IFN-γ secretion**, plus **spontaneous germinal center responses** and **broad autoantibody production**. (singh2024activatedpi3kδspecifically pages 3-4, singh2024activatedpi3kδspecifically pages 1-3)
- Mechanistic linkage is consistent with PI3K→AKT→FOXO regulation (AKT phosphorylation, FOXO1 nuclear exclusion) affecting Treg stability/function. (singh2024activatedpi3kδspecifically pages 11-13)

**GO interpretation:** supports BP terms around **regulatory T cell homeostasis**, **immune tolerance/negative regulation of immune response**, and **regulation of germinal center response/humoral immunity**, with an explicit caveat that both **loss** and **gain** of PI3Kδ signaling can disrupt tolerance (directionality depends on activity threshold/context). (singh2024activatedpi3kδspecifically pages 1-3, singh2024activatedpi3kδspecifically pages 10-11)

## 3) Recent developments (prioritize 2023–2024)
### 3.1 Refined pathway framing for GO: receptor repertoire and downstream readouts
A 2024 review synthesizes receptor contexts and regulatory mechanisms relevant to GO process selection:
- Class IA PI3K (p85–p110δ) is recruited downstream of immune receptors including **BCR/TCR/CD28/ICOS/CD19/BAFF-R/CD40**, producing PIP3 that drives AKT/mTOR/FOXO-linked programs. (ijspeert2024hyperactivationofthe pages 2-4, ijspeert2024hyperactivationofthe pages 1-2)
- It highlights pathway antagonism by PTEN/SHIP and connects FOXO-regulated transcription (e.g., immune differentiation programs) to PI3K signaling outputs (useful for downstream BP annotations, but requires careful evidence attribution if annotating those distal effects). (ijspeert2024hyperactivationofthe pages 2-4)

*Source (Immunotherapy Advances, 2024-11; DOI:10.1093/immadv/ltae009; URL: https://doi.org/10.1093/immadv/ltae009)* (ijspeert2024hyperactivationofthe pages 2-4, ijspeert2024hyperactivationofthe pages 1-2)

### 3.2 Quantitative inhibitor/probe landscape (mechanism, selectivity, and caveats)
Because PI3Kδ is frequently perturbed pharmacologically (both experimentally and clinically), inhibitor properties are directly relevant to interpreting evidence used for GO assertions.

**Allosteric vs ATP-competitive PI3Kδ inhibition (2023):**
- **IOA-244 (roginolisib)** behaves as a **non–ATP-competitive** PI3Kδ inhibitor; kinetic data show minimal ATP Km shift but a strong Vmax reduction in a PIP3 production assay; biochemical IC50 ~**19 nM** and whole blood IC50 **0.28 μM** were reported (plus extensive selectivity profiling). (johnson2023ioa244isa pages 6-7, johnson2023ioa244isa pages 13-14)
- **Idelalisib** shows **ATP-competitive** behavior (Km shift) and strong PI3Kδ potency (KiNativ PI3Kδ IC50 **1.3 nM**), but with additional off-target activity and an active metabolite (GS-563117) with its own target spectrum, supporting strong GO curation caveats for pharmacology-derived functional claims. (johnson2023ioa244isa pages 6-7, johnson2023ioa244isa pages 13-14)

*Source (Cancer Research Communications, 2023-04; DOI:10.1158/2767-9764.CRC-22-0477; URL: https://doi.org/10.1158/2767-9764.crc-22-0477)* (johnson2023ioa244isa pages 6-7, johnson2023ioa244isa pages 13-14)

**Leniolisib potency and isoform selectivity (2024):**
- Leniolisib is reported as PI3Kδ-selective with **IC50 11 nM** (PI3Kδ) vs **244 nM (α)**, **424 nM (β)**, **2230 nM (γ)**. (de2024leniolisibanovel pages 1-2, cant2024pi3kδpathwaydysregulation pages 19-20)

*Sources:* Frontiers in Pharmacology (2024-02; DOI:10.3389/fphar.2024.1337436; URL: https://doi.org/10.3389/fphar.2024.1337436) (de2024leniolisibanovel pages 1-2) and JACI-In Practice (2024-01; DOI:10.1016/j.jaip.2023.09.016; URL: https://doi.org/10.1016/j.jaip.2023.09.016) (cant2024pi3kδpathwaydysregulation pages 19-20)

**GO curation implication:** inhibitor-based inference is useful for pathway placement (PI3Kδ dependence), but should be down-weighted unless selectivity, concentrations, and metabolites are controlled and accompanied by genetic corroboration. (johnson2023ioa244isa pages 6-7, cant2024pi3kδpathwaydysregulation pages 13-14)

## 4) Cellular locations and trafficking (GO CC-focused synthesis)
- **Resting state:** cytosolic complex of p110δ with p85-family regulatory subunits, with p85 inhibiting catalytic activity until activation signals occur. (ijspeert2024hyperactivationofthe pages 2-4)
- **Activated state:** recruitment/translocation of the p85–p110δ complex to **plasma membrane** via SH2 binding to receptor/adaptor phosphotyrosines, enabling access to PI(4,5)P2 substrate and local PIP3 generation. (ijspeert2024hyperactivationofthe pages 2-4, stokoe2005thephosphoinositide3kinase pages 1-3)

**Caveat for CC annotation:** Much localization evidence in the retrieved sources is mechanistic/consensus (review synthesis). For strict experimental CC evidence codes, curators may prefer direct imaging/biochemical fractionation papers (not retrieved here in full). (ijspeert2024hyperactivationofthe pages 2-4, stokoe2005thephosphoinositide3kinase pages 1-3)

## 5) Disease context (only where functionally informative)
Disease genetics mainly reinforce **dosage/threshold sensitivity** of PI3Kδ signaling in immune function. For example, the Treg-conditional activation study demonstrates that hyperactive PI3Kδ signaling can paradoxically increase Treg numbers while impairing tolerance, emphasizing that GO BP annotations should avoid implying monotonic positive regulation for all downstream immune outcomes. (singh2024activatedpi3kδspecifically pages 1-3)

APDS-focused reviews (2024) frame PI3Kδ hyperactivation as driving excessive AKT/mTOR pathway activity in immune cells and motivating use of selective inhibitors; this is functionally relevant as it highlights pathway readouts (pAKT/pS6) used experimentally. (cant2024pi3kδpathwaydysregulation pages 1-3)

## 6) GO annotation caveats and curator notes
1. **Isoform redundancy / shared PI3K outputs:** Many downstream readouts (e.g., pAKT, pS6) are not isoform-specific, and class I PI3Ks share overlapping functions; p110δ is leukocyte-enriched but not exclusively expressed, so immune-context evidence is strongest for PIK3CD-specific BP claims. (ijspeert2024hyperactivationofthe pages 1-2, cant2024pi3kδpathwaydysregulation pages 1-3)
2. **Pharmacology confounding:** PI3Kδ inhibitors differ in mechanism (ATP-competitive vs allosteric), cellular potency vs biochemical potency, off-target profiles, and metabolites; GO assertions based solely on inhibitor phenotypes can be misleading without genetic confirmation. (johnson2023ioa244isa pages 6-7, johnson2023ioa244isa pages 13-14, cant2024pi3kδpathwaydysregulation pages 13-14)
3. **Pathological hyperactivation ≠ physiological role directionality:** Hyperactive PI3Kδ in Tregs produces immune dysregulation and autoantibodies despite increased Treg numbers, so annotations should favor neutral process placement (e.g., “involved in”) or carefully qualified regulation terms when direction is context-dependent. (singh2024activatedpi3kδspecifically pages 1-3, singh2024activatedpi3kδspecifically pages 11-13)
4. **Species-to-human transfer:** Foundational functional genetics are largely from mouse models (e.g., p110δ knockout). These are highly informative for GO, but annotation should note organism context and confirmability in human systems when possible. (jou2002essentialnonredundantrole pages 4-8)

## 7) Curator-facing GO mapping table (artifact)
The following table compiles recommended MF/BP/CC terms with evidence summaries and traceable citations.

| GO aspect | Recommended GO term name | Evidence summary (1 line) | Key experimental system | Best supporting citation IDs |
|---|---|---|---|---|
| MF | phosphatidylinositol-4,5-bisphosphate 3-kinase activity | Class I/IA PI3Ks, including p110δ, phosphorylate PI(4,5)P2 to PI(3,4,5)P3; this is the core enzymatic activity of PIK3CD. | Cell-free / review synthesis | (ijspeert2024hyperactivationofthe pages 1-2, stokoe2005thephosphoinositide3kinase pages 1-3) |
| MF | ATP binding | PI3Kδ catalytic activity is ATP-dependent; inhibitor kinetic studies distinguish ATP-competitive idelalisib from non-ATP-competitive IOA-244, reinforcing ATP use at the catalytic site. | Cell-free biochemical assays | (johnson2023ioa244isa pages 6-7, cant2024pi3kδpathwaydysregulation pages 19-20) |
| CC | class IA phosphatidylinositol 3-kinase complex | p110δ forms a class IA heterodimer with p85-family regulatory subunits, with p85 both stabilizing and inhibiting the catalytic subunit in resting cells. | Human / review synthesis | (ijspeert2024hyperactivationofthe pages 2-4, stokoe2005thephosphoinositide3kinase pages 1-3, berglund2024modulatingthepi3k pages 8-8) |
| CC | plasma membrane recruitment | Upon receptor phosphotyrosine signaling, SH2-containing p85 recruits the p85-p110δ complex to the plasma membrane where phosphoinositide substrates reside. | Human / review synthesis | (ijspeert2024hyperactivationofthe pages 2-4, ijspeert2024hyperactivationofthe pages 1-2, stokoe2005thephosphoinositide3kinase pages 1-3) |
| BP | phosphatidylinositol 3-kinase signaling | PI3Kδ-generated PIP3 recruits and activates AKT-linked signaling modules controlling downstream immune-cell responses. | Human / mouse / review synthesis | (ijspeert2024hyperactivationofthe pages 2-4, ijspeert2024hyperactivationofthe pages 1-2) |
| BP | B cell receptor signaling pathway | Genetic loss of p110δ causes a specific BCR signaling defect, indicating a nonredundant positive role downstream of the BCR/CD19 axis. | Mouse knockout | (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole pages 8-10, jou2002essentialnonredundantrole pages 1-2) |
| BP | intracellular calcium ion mobilization | Anti-IgM-induced Ca2+ mobilization in p110δ-deficient B cells is reduced to about 25% of wild type, supporting a role in BCR-triggered Ca2+ signaling. | Mouse knockout | (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole media 9f8002cf) |
| BP | B cell development | p110δ deficiency reduces mature peripheral B cells, causes a developmental block and loss of B1 cells, supporting annotation to B-cell developmental processes. | Mouse knockout | (jou2002essentialnonredundantrole pages 1-2, jou2002essentialnonredundantrole pages 2-4) |
| BP | B cell activation | p110δ-deficient B cells show impaired responses to BCR ligation and reduced activation-associated functional outputs. | Mouse knockout | (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole pages 2-4) |
| BP | B cell proliferation | Splenic p110δ-deficient B cells proliferate poorly in response to anti-IgM, anti-CD40 and LPS, while bypass stimulation is relatively preserved. | Mouse knockout | (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole pages 2-4) |
| BP | germinal center formation | Immunized p110δ-deficient mice fail to form splenic germinal centers, demonstrating a requirement for PI3Kδ in this humoral immune process. | Mouse knockout | (jou2002essentialnonredundantrole pages 1-2, jou2002essentialnonredundantrole media 9f8002cf) |
| BP | T-dependent humoral immune response | T-dependent antibody responses are absent in p110δ-deficient mice, with severe defects also seen for TI responses, supporting a role in antibody production pathways. | Mouse knockout | (jou2002essentialnonredundantrole pages 4-8, jou2002essentialnonredundantrole media 9f8002cf) |
| BP | AKT signaling / positive regulation of TOR signaling | Recent reviews and APDS-related studies place PI3Kδ upstream of AKT, mTORC1/S6 and FOXO regulation; pS6 elevation is used as a downstream readout of pathway activation. | Human patients / mouse models | (ijspeert2024hyperactivationofthe pages 2-4, nguyen2023humanpik3r1mutations pages 24-25, singh2024activatedpi3kδspecifically pages 11-13) |
| BP | regulatory T cell homeostasis | Balanced PI3Kδ activity is required in Tregs: hyperactive PI3Kδ increases Treg numbers but reduces fitness and functional stability, whereas insufficient signaling also impairs tolerance. | Mouse conditional GOF / review synthesis | (singh2024activatedpi3kδspecifically pages 3-4, singh2024activatedpi3kδspecifically pages 11-13, singh2024activatedpi3kδspecifically pages 1-3) |
| BP | immune tolerance / negative regulation of immune response | Treg-restricted activated PI3Kδ drives chronic inflammation, elevated IFN-γ, increased Tfh/GC responses and broad autoantibody production, indicating loss of tolerance when PI3Kδ is dysregulated. | Mouse conditional GOF | (singh2024activatedpi3kδspecifically pages 3-4, singh2024activatedpi3kδspecifically pages 10-11, singh2024activatedpi3kδspecifically pages 1-3) |
| BP | caveat: isoform redundancy and context dependence | Some PI3K outputs can be shared with other class I isoforms; p110δ is leukocyte-enriched but not absolutely exclusive, so annotations should favor immune-context evidence over broad generic signaling claims. | Curation note | (ijspeert2024hyperactivationofthe pages 1-2, wright2024theimportanceof pages 4-6, cant2024pi3kδpathwaydysregulation pages 1-3) |
| BP | caveat: inhibitor-based evidence can be confounded | PI3Kδ inhibitors differ in selectivity, mechanism and metabolites (e.g., ATP-competitive vs noncompetitive; off-target active metabolites), so pharmacology alone should not be over-weighted for direct GO assignment. | Curation note / cell-free and cellular pharmacology | (johnson2023ioa244isa pages 6-7, de2024leniolisibanovel pages 2-4, cant2024pi3kδpathwaydysregulation pages 13-14, johnson2023ioa244isa pages 15-16) |


*Table: This table summarizes high-confidence, curator-facing GO annotation suggestions for human PIK3CD/p110δ, mapped to the strongest experimental evidence retrieved in this session. It highlights core molecular function, complex/localization, immune signaling processes, and key curation caveats.*

## 8) Key references with publication dates and URLs (subset)
- Jou ST et al. *Molecular and Cellular Biology* (2002-12). “Essential, Nonredundant Role for the Phosphoinositide 3-Kinase p110δ in Signaling by the B-Cell Receptor Complex.” DOI:10.1128/MCB.22.24.8580-8591.2002. https://doi.org/10.1128/mcb.22.24.8580-8591.2002 (jou2002essentialnonredundantrole pages 4-8)
- IJspeert H et al. *Immunotherapy Advances* (2024-11). DOI:10.1093/immadv/ltae009. https://doi.org/10.1093/immadv/ltae009 (ijspeert2024hyperactivationofthe pages 2-4)
- Singh AK et al. *Journal of Immunology* (2024-06). DOI:10.4049/jimmunol.2400032. https://doi.org/10.4049/jimmunol.2400032 (singh2024activatedpi3kδspecifically pages 1-3)
- Cant AJ et al. *J Allergy Clin Immunol: In Practice* (2024-01). DOI:10.1016/j.jaip.2023.09.016. https://doi.org/10.1016/j.jaip.2023.09.016 (cant2024pi3kδpathwaydysregulation pages 19-20)
- Johnson Z et al. *Cancer Research Communications* (2023-04). DOI:10.1158/2767-9764.CRC-22-0477. https://doi.org/10.1158/2767-9764.crc-22-0477 (johnson2023ioa244isa pages 6-7)
- De SK. *Frontiers in Pharmacology* (2024-02). DOI:10.3389/fphar.2024.1337436. https://doi.org/10.3389/fphar.2024.1337436 (de2024leniolisibanovel pages 1-2)



References

1. (ijspeert2024hyperactivationofthe pages 2-4): Hanna IJspeert, Virgil A S H Dalm, Menno C van Zelm, and Emily S J Edwards. Hyperactivation of the pi3k pathway in inborn errors of immunity: current understanding and therapeutic perspectives. Immunotherapy Advances, Nov 2024. URL: https://doi.org/10.1093/immadv/ltae009, doi:10.1093/immadv/ltae009. This article has 11 citations.

2. (ijspeert2024hyperactivationofthe pages 1-2): Hanna IJspeert, Virgil A S H Dalm, Menno C van Zelm, and Emily S J Edwards. Hyperactivation of the pi3k pathway in inborn errors of immunity: current understanding and therapeutic perspectives. Immunotherapy Advances, Nov 2024. URL: https://doi.org/10.1093/immadv/ltae009, doi:10.1093/immadv/ltae009. This article has 11 citations.

3. (stokoe2005thephosphoinositide3kinase pages 1-3): David Stokoe. The phosphoinositide 3-kinase pathway and cancer. Expert Reviews in Molecular Medicine, 7:1-22, Jun 2005. URL: https://doi.org/10.1017/s1462399405009361, doi:10.1017/s1462399405009361. This article has 73 citations and is from a peer-reviewed journal.

4. (johnson2023ioa244isa pages 6-7): Zoë Johnson, Chiara Tarantelli, Elisa Civanelli, Luciano Cascione, Filippo Spriano, Amy Fraser, Pritom Shah, Tyzoon Nomanbhoy, Sara Napoli, Andrea Rinaldi, Karolina Niewola-Staszkowska, Michael Lahn, Dominique Perrin, Mathias Wenes, Denis Migliorini, Francesco Bertoni, Lars van der Veen, and Giusy Di Conza. Ioa-244 is a non–atp-competitive, highly selective, tolerable pi3k delta inhibitor that targets solid tumors and breaks immune tolerance. Cancer Research Communications, 3:576-591, Apr 2023. URL: https://doi.org/10.1158/2767-9764.crc-22-0477, doi:10.1158/2767-9764.crc-22-0477. This article has 33 citations and is from a peer-reviewed journal.

5. (jou2002essentialnonredundantrole pages 4-8): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

6. (jou2002essentialnonredundantrole media 9f8002cf): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

7. (jou2002essentialnonredundantrole pages 1-2): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

8. (jou2002essentialnonredundantrole pages 2-4): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

9. (jou2002essentialnonredundantrole media 37876baa): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

10. (jou2002essentialnonredundantrole media 7d2b61ed): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

11. (jou2002essentialnonredundantrole media 3b78ec57): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

12. (singh2024activatedpi3kδspecifically pages 1-3): Akhilesh K. Singh, Fahd Al Qureshah, Travis Drow, Baidong Hou, and David J. Rawlings. Activated pi3kδ specifically perturbs mouse regulatory t cell homeostasis and function leading to immune dysregulation. Journal of immunology, 213:135-147, Jun 2024. URL: https://doi.org/10.4049/jimmunol.2400032, doi:10.4049/jimmunol.2400032. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (singh2024activatedpi3kδspecifically pages 3-4): Akhilesh K. Singh, Fahd Al Qureshah, Travis Drow, Baidong Hou, and David J. Rawlings. Activated pi3kδ specifically perturbs mouse regulatory t cell homeostasis and function leading to immune dysregulation. Journal of immunology, 213:135-147, Jun 2024. URL: https://doi.org/10.4049/jimmunol.2400032, doi:10.4049/jimmunol.2400032. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (singh2024activatedpi3kδspecifically pages 11-13): Akhilesh K. Singh, Fahd Al Qureshah, Travis Drow, Baidong Hou, and David J. Rawlings. Activated pi3kδ specifically perturbs mouse regulatory t cell homeostasis and function leading to immune dysregulation. Journal of immunology, 213:135-147, Jun 2024. URL: https://doi.org/10.4049/jimmunol.2400032, doi:10.4049/jimmunol.2400032. This article has 8 citations and is from a domain leading peer-reviewed journal.

15. (singh2024activatedpi3kδspecifically pages 10-11): Akhilesh K. Singh, Fahd Al Qureshah, Travis Drow, Baidong Hou, and David J. Rawlings. Activated pi3kδ specifically perturbs mouse regulatory t cell homeostasis and function leading to immune dysregulation. Journal of immunology, 213:135-147, Jun 2024. URL: https://doi.org/10.4049/jimmunol.2400032, doi:10.4049/jimmunol.2400032. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (johnson2023ioa244isa pages 13-14): Zoë Johnson, Chiara Tarantelli, Elisa Civanelli, Luciano Cascione, Filippo Spriano, Amy Fraser, Pritom Shah, Tyzoon Nomanbhoy, Sara Napoli, Andrea Rinaldi, Karolina Niewola-Staszkowska, Michael Lahn, Dominique Perrin, Mathias Wenes, Denis Migliorini, Francesco Bertoni, Lars van der Veen, and Giusy Di Conza. Ioa-244 is a non–atp-competitive, highly selective, tolerable pi3k delta inhibitor that targets solid tumors and breaks immune tolerance. Cancer Research Communications, 3:576-591, Apr 2023. URL: https://doi.org/10.1158/2767-9764.crc-22-0477, doi:10.1158/2767-9764.crc-22-0477. This article has 33 citations and is from a peer-reviewed journal.

17. (de2024leniolisibanovel pages 1-2): Surya K. De. Leniolisib: a novel treatment for activated phosphoinositide-3 kinase delta syndrome. Frontiers in Pharmacology, Feb 2024. URL: https://doi.org/10.3389/fphar.2024.1337436, doi:10.3389/fphar.2024.1337436. This article has 12 citations.

18. (cant2024pi3kδpathwaydysregulation pages 19-20): Andrew J. Cant, Anita Chandra, Ewen Munro, V. Koneti Rao, and Carrie L. Lucas. Pi3kδ pathway dysregulation and unique features of its inhibition by leniolisib in activated pi3kδ syndrome and beyond. The Journal of Allergy and Clinical Immunology: In Practice, 12:69-78, Jan 2024. URL: https://doi.org/10.1016/j.jaip.2023.09.016, doi:10.1016/j.jaip.2023.09.016. This article has 34 citations.

19. (cant2024pi3kδpathwaydysregulation pages 13-14): Andrew J. Cant, Anita Chandra, Ewen Munro, V. Koneti Rao, and Carrie L. Lucas. Pi3kδ pathway dysregulation and unique features of its inhibition by leniolisib in activated pi3kδ syndrome and beyond. The Journal of Allergy and Clinical Immunology: In Practice, 12:69-78, Jan 2024. URL: https://doi.org/10.1016/j.jaip.2023.09.016, doi:10.1016/j.jaip.2023.09.016. This article has 34 citations.

20. (cant2024pi3kδpathwaydysregulation pages 1-3): Andrew J. Cant, Anita Chandra, Ewen Munro, V. Koneti Rao, and Carrie L. Lucas. Pi3kδ pathway dysregulation and unique features of its inhibition by leniolisib in activated pi3kδ syndrome and beyond. The Journal of Allergy and Clinical Immunology: In Practice, 12:69-78, Jan 2024. URL: https://doi.org/10.1016/j.jaip.2023.09.016, doi:10.1016/j.jaip.2023.09.016. This article has 34 citations.

21. (berglund2024modulatingthepi3k pages 8-8): Lucinda J. Berglund. Modulating the pi3k signalling pathway in activated pi3k delta syndrome: a clinical perspective. Journal of Clinical Immunology, Dec 2024. URL: https://doi.org/10.1007/s10875-023-01626-0, doi:10.1007/s10875-023-01626-0. This article has 20 citations and is from a domain leading peer-reviewed journal.

22. (jou2002essentialnonredundantrole pages 8-10): Shiann-Tarng Jou, Nick Carpino, Yutaka Takahashi, Roland Piekorz, Jyh-Rong Chao, Neena Carpino, Demin Wang, and James N. Ihle. Essential, nonredundant role for the phosphoinositide 3-kinase p110δ in signaling by the b-cell receptor complex. Molecular and Cellular Biology, 22:8580-8591, Dec 2002. URL: https://doi.org/10.1128/mcb.22.24.8580-8591.2002, doi:10.1128/mcb.22.24.8580-8591.2002. This article has 480 citations and is from a domain leading peer-reviewed journal.

23. (nguyen2023humanpik3r1mutations pages 24-25): Tina Nguyen, Anthony Lau, Julia Bier, Kristen C. Cooke, Helen Lenthall, Stephanie Ruiz-Diaz, Danielle T. Avery, Henry Brigden, David Zahra, William A Sewell, Luke Droney, Satoshi Okada, Takaki Asano, Hassan Abolhassani, Zahra Chavoshzadeh, Roshini S. Abraham, Nipunie Rajapakse, Eric W. Klee, Joseph A. Church, Andrew Williams, Melanie Wong, Christoph Burkhart, Gulbu Uzel, David R. Croucher, David E. James, Cindy S. Ma, Robert Brink, Stuart G. Tangye, and Elissa K. Deenick. Human pik3r1 mutations disrupt lymphocyte differentiation to cause activated pi3kδ syndrome 2. The Journal of Experimental Medicine, Mar 2023. URL: https://doi.org/10.1084/jem.20221020, doi:10.1084/jem.20221020. This article has 32 citations.

24. (wright2024theimportanceof pages 4-6): Brock Wright, Samuel King, and Cenk Suphioglu. The importance of phosphoinositide 3-kinase in neuroinflammation. International Journal of Molecular Sciences, 25:11638, Oct 2024. URL: https://doi.org/10.3390/ijms252111638, doi:10.3390/ijms252111638. This article has 43 citations.

25. (de2024leniolisibanovel pages 2-4): Surya K. De. Leniolisib: a novel treatment for activated phosphoinositide-3 kinase delta syndrome. Frontiers in Pharmacology, Feb 2024. URL: https://doi.org/10.3389/fphar.2024.1337436, doi:10.3389/fphar.2024.1337436. This article has 12 citations.

26. (johnson2023ioa244isa pages 15-16): Zoë Johnson, Chiara Tarantelli, Elisa Civanelli, Luciano Cascione, Filippo Spriano, Amy Fraser, Pritom Shah, Tyzoon Nomanbhoy, Sara Napoli, Andrea Rinaldi, Karolina Niewola-Staszkowska, Michael Lahn, Dominique Perrin, Mathias Wenes, Denis Migliorini, Francesco Bertoni, Lars van der Veen, and Giusy Di Conza. Ioa-244 is a non–atp-competitive, highly selective, tolerable pi3k delta inhibitor that targets solid tumors and breaks immune tolerance. Cancer Research Communications, 3:576-591, Apr 2023. URL: https://doi.org/10.1158/2767-9764.crc-22-0477, doi:10.1158/2767-9764.crc-22-0477. This article has 33 citations and is from a peer-reviewed journal.

## Citations

1. ijspeert2024hyperactivationofthe pages 2-4
2. jou2002essentialnonredundantrole pages 4-8
3. de2024leniolisibanovel pages 1-2
4. ijspeert2024hyperactivationofthe pages 1-2
5. jou2002essentialnonredundantrole pages 1-2
6. jou2002essentialnonredundantrole pages 2-4
7. jou2002essentialnonredundantrole pages 8-10
8. wright2024theimportanceof pages 4-6
9. de2024leniolisibanovel pages 2-4
10. https://www.uniprot.org/uniprotkb/O00329/
11. https://doi.org/10.1128/mcb.22.24.8580-8591.2002
12. https://doi.org/10.4049/jimmunol.2400032
13. https://doi.org/10.1093/immadv/ltae009
14. https://doi.org/10.1158/2767-9764.crc-22-0477
15. https://doi.org/10.3389/fphar.2024.1337436
16. https://doi.org/10.1016/j.jaip.2023.09.016
17. https://doi.org/10.1093/immadv/ltae009,
18. https://doi.org/10.1017/s1462399405009361,
19. https://doi.org/10.1158/2767-9764.crc-22-0477,
20. https://doi.org/10.1128/mcb.22.24.8580-8591.2002,
21. https://doi.org/10.4049/jimmunol.2400032,
22. https://doi.org/10.3389/fphar.2024.1337436,
23. https://doi.org/10.1016/j.jaip.2023.09.016,
24. https://doi.org/10.1007/s10875-023-01626-0,
25. https://doi.org/10.1084/jem.20221020,
26. https://doi.org/10.3390/ijms252111638,