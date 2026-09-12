---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-06-03T08:00:51.533835'
end_time: '2026-06-03T08:00:51.535134'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: METEA
  gene_id: icd
  gene_symbol: icd
  uniprot_accession: C5AXM3
  protein_description: 'RecName: Full=Isocitrate dehydrogenase [NADP] {ECO:0000256|PIRNR:PIRNR000108};
    EC=1.1.1.42 {ECO:0000256|PIRNR:PIRNR000108};'
  gene_info: Name=icd {ECO:0000313|EMBL:ACS41091.1}; OrderedLocusNames=MexAM1_META1p3354
    {ECO:0000313|EMBL:ACS41091.1};
  organism_full: Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805
    / NCIMB 9133 / AM1) (Methylobacterium extorquens).
  protein_family: Belongs to the isocitrate and isopropylmalate
  protein_domains: IsoCit/isopropylmalate_DH_CS. (IPR019818); Isocitrate_DH_NADP.
    (IPR004790); IsoPropMal-DH-like_dom. (IPR024084); Iso_dh (PF00180)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: icd-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** C5AXM3
- **Protein Description:** RecName: Full=Isocitrate dehydrogenase [NADP] {ECO:0000256|PIRNR:PIRNR000108}; EC=1.1.1.42 {ECO:0000256|PIRNR:PIRNR000108};
- **Gene Information:** Name=icd {ECO:0000313|EMBL:ACS41091.1}; OrderedLocusNames=MexAM1_META1p3354 {ECO:0000313|EMBL:ACS41091.1};
- **Organism (full):** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
- **Protein Family:** Belongs to the isocitrate and isopropylmalate
- **Key Domains:** IsoCit/isopropylmalate_DH_CS. (IPR019818); Isocitrate_DH_NADP. (IPR004790); IsoPropMal-DH-like_dom. (IPR024084); Iso_dh (PF00180)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "icd" matches the protein description above**
2. **Verify the organism is correct:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'icd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **icd** (gene ID: icd, UniProt: C5AXM3) in METEA.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

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

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** C5AXM3
- **Protein Description:** RecName: Full=Isocitrate dehydrogenase [NADP] {ECO:0000256|PIRNR:PIRNR000108}; EC=1.1.1.42 {ECO:0000256|PIRNR:PIRNR000108};
- **Gene Information:** Name=icd {ECO:0000313|EMBL:ACS41091.1}; OrderedLocusNames=MexAM1_META1p3354 {ECO:0000313|EMBL:ACS41091.1};
- **Organism (full):** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
- **Protein Family:** Belongs to the isocitrate and isopropylmalate
- **Key Domains:** IsoCit/isopropylmalate_DH_CS. (IPR019818); Isocitrate_DH_NADP. (IPR004790); IsoPropMal-DH-like_dom. (IPR024084); Iso_dh (PF00180)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "icd" matches the protein description above**
2. **Verify the organism is correct:** Methylorubrum extorquens (strain ATCC 14718 / DSM 1338 / JCM 2805 / NCIMB 9133 / AM1) (Methylobacterium extorquens).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'icd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **icd** (gene ID: icd, UniProt: C5AXM3) in METEA.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: **icd** (NADP-dependent isocitrate dehydrogenase) in *Methylorubrum extorquens* AM1 (formerly *Methylobacterium extorquens* AM1)

### 1) Target verification and gene/protein identity (critical disambiguation)
The gene symbol **icd/icdA** in *Methylorubrum (Methylobacterium) extorquens* AM1 corresponds to **NADP-dependent isocitrate dehydrogenase**, a tricarboxylic acid (TCA) cycle enzyme annotated as **“NADP-dependent isocitrate dehydrogenase (icd)”** in a central-metabolism proteomics table; in that dataset it is listed as **gene number 3354** (schneider2012theethylmalonylcoapathway pages 4-4). This matches the UniProt-provided identity for the target (EC **1.1.1.42**, NADP-dependent isocitrate dehydrogenase). 

**Important limitation:** in the currently retrieved full texts, I did **not** find an explicit cross-reference that states “gene 3354 / icd = UniProt C5AXM3” or the ordered locus tag **MexAM1_META1p3354**. Therefore, the mapping to UniProt accession **C5AXM3** is consistent with enzyme name/EC number and the internal gene number 3354 reported for AM1, but is not explicitly evidenced in the retrieved papers.

### 2) Key concepts and definitions (current understanding)

#### 2.1 Enzyme class and reaction (biochemical definition)
**Isocitrate dehydrogenase (NADP-dependent; EC 1.1.1.42)** is a central-carbon enzyme that catalyzes an **oxidative decarboxylation** step in the TCA cycle, converting **isocitrate** to **2-oxoglutarate (α-ketoglutarate)** while reducing **NADP+ to NADPH** (standard enzyme definition consistent with its EC class). In *M. extorquens* AM1, experimental assays of Icd activity specifically monitor **NADPH formation**, confirming NADP(H) coupling for the measured enzyme activity in this organism (skovran2010asystemsbiology pages 13-14).

#### 2.2 Functional role in metabolism (conceptual)
In bacteria, NADP-dependent Icd often serves a dual role:
1) **Carbon flow control** through the TCA branch point from isocitrate toward **2-oxoglutarate** (biosynthetic precursor supply), and 
2) **NADPH generation** (reducing power) coupled to central carbon oxidation.

For AM1, systems-level and flux work emphasizes its role in **redox-equivalent generation** during certain growth conditions (acetate) and shows condition-dependent downregulation during shifts to C1 metabolism (methanol) (skovran2010asystemsbiology pages 8-10, schneider2012theethylmalonylcoapathway pages 5-7).

### 3) Experimental evidence for icd/Icd function in *M. extorquens* AM1

#### 3.1 Enzyme activity measurement directly tracks NADPH production
Skovran et al. (PLoS ONE; publication date **2010-11-10**; https://doi.org/10.1371/journal.pone.0014091) measured **isocitrate dehydrogenase (Icd)** activity in AM1 cell extracts by **following NADPH production at 340 nm** using an extinction coefficient of **6.2 mM−1 cm−1** (skovran2010asystemsbiology pages 13-14). Extract preparation and assay conditions were described, including washing/resuspension in **100 mM potassium phosphate buffer (pH 7.5)** and performing assays in a **200 µL** plate-reader format at room temperature (skovran2010asystemsbiology pages 13-14). These details provide direct experimental confirmation that the measured “Icd” activity corresponds to an NADP-dependent (NADPH-forming) isocitrate dehydrogenase in AM1 (skovran2010asystemsbiology pages 13-14).

#### 3.2 Expression/activity remodeling during succinate → methanol transition
During transition from succinate growth to methanol growth, **expression of TCA cycle genes including icdA decreased severely**, and Icd enzymatic activity decreased to **~79% of starting activity** shortly after methanol addition (skovran2010asystemsbiology pages 8-10). This supports a model in which the oxidative TCA branch is transcriptionally and enzymatically downshifted during entry into methylotrophic growth mode (skovran2010asystemsbiology pages 8-10).

#### 3.3 Upregulation of Icd protein abundance during acetate growth
Schneider et al. (JBC; publication date **2012-01-02**; https://doi.org/10.1074/jbc.M111.305219) performed proteomics comparing acetate vs methanol growth and found that NADP-dependent isocitrate dehydrogenase **icd (gene number 3354)** had increased abundance on acetate with **fold change 2.4** (p = 0.01) (schneider2012theethylmalonylcoapathway pages 4-4). This indicates that AM1 increases TCA-cycle capacity, including Icd, during growth on acetate (schneider2012theethylmalonylcoapathway pages 4-4).

### 4) Pathway context and physiological role in AM1 (TCA/EMC, NADPH, redox balancing)

#### 4.1 Acetate growth: TCA cycle is heavily catabolic and central for reducing equivalents
Schneider et al. used 13C steady-state labeling and metabolic flux analysis to quantify acetate metabolism. They report that **68% of acetyl-CoA enters the TCA cycle**, and **98%** of the acetyl-CoA entering the TCA cycle is **completely oxidized to CO2**, supporting that the TCA operates in an “almost purely catabolic mode” and is the main pathway for generating reducing equivalents (schneider2012theethylmalonylcoapathway pages 5-7). In that same analysis, only **2%** of acetyl-CoA entering the TCA is diverted to 2-oxoglutarate as a precursor for biomass synthesis, highlighting that under acetate growth the oxidative TCA branch (including Icd) functions largely for energy/redox rather than anabolic precursor export (schneider2012theethylmalonylcoapathway pages 5-7).

#### 4.2 NADH/NADPH balancing: strong induction of membrane transhydrogenase pntAB
Schneider et al. note that the **TCA cycle produces a fixed NADH:NADPH ratio of 1:1** in their framework, and they observed that membrane-bound **NAD(P) transhydrogenase** is more abundant in acetate-grown cells (fold change ~**10** stated in text; and **pntA/pntB** fold changes **12.5** and **12.3** in the proteomics table) (schneider2012theethylmalonylcoapathway pages 5-7, schneider2012theethylmalonylcoapathway pages 4-4). This supports the interpretation that acetate growth requires active **redox cofactor balancing** and that AM1 upregulates transhydrogenase capacity to interconvert NADH and NADPH pools (schneider2012theethylmalonylcoapathway pages 5-7, schneider2012theethylmalonylcoapathway pages 4-4).

A recent authoritative perspective (Partipilo et al., ACS Synthetic Biology; publication date **2023-04**; https://doi.org/10.1021/acssynbio.3c00070) provides general expert framing: **membrane-bound transhydrogenases** (including **PntAB**) couple hydride transfer to **proton translocation** and in vivo can favor **NADPH formation**, making them strong candidates to convert NADH into NADPH when NADPH supply is limiting (partipilo2023ahitchhiker’sguide pages 11-12). While this perspective is not AM1-specific, it supports the mechanistic plausibility of Schneider et al.’s inference that transhydrogenase induction in acetate-grown AM1 relates to NADPH/NADH balancing (partipilo2023ahitchhiker’sguide pages 11-12).

#### 4.3 Connection to the EMC pathway and absence of glyoxylate cycle
Schneider et al. show that AM1 lacks isocitrate lyase (glyoxylate-cycle key enzyme) and instead uses the **ethylmalonyl-CoA (EMC) pathway** during acetate growth, which functionally replaces the glyoxylate cycle and refills the TCA cycle while also supplying glyoxylate for biosynthesis (schneider2012theethylmalonylcoapathway pages 5-7). In this overall architecture, Icd remains a core TCA enzyme whose increased abundance is consistent with increased reliance on a catabolic TCA cycle during acetate oxidation (schneider2012theethylmalonylcoapathway pages 5-7, schneider2012theethylmalonylcoapathway pages 4-4).

### 5) Cellular localization
No retrieved AM1 paper explicitly states subcellular localization for Icd (e.g., cytosolic vs membrane-associated). However, the enzyme activity assays were performed on **soluble cell extracts** after French press lysis and clarification by centrifugation, consistent with assaying a **soluble (cytosolic) enzyme fraction** rather than a membrane enzyme (skovran2010asystemsbiology pages 13-14). In bacteria, NADP-dependent Icd is typically a soluble cytosolic enzyme; here, that localization should be regarded as **inferred** rather than directly localized by microscopy/fractionation in the retrieved AM1 sources.

### 6) Recent developments (2023–2024 emphasis) and expert analysis
Direct 2023–2024 primary studies specifically characterizing **AM1 icd (gene 3354 / MexAM1_META1p3354)** were not retrieved with the current tool searches. However, relevant *recent* developments and expert views that contextualize icd function include:

* **Redox module engineering and transhydrogenases:** Partipilo et al. (2023) synthesize expert knowledge on managing NAD(P)H in engineered/synthetic systems, emphasizing transhydrogenases as a modular solution to convert NADH↔NADPH and highlighting membrane-bound systems (including PntAB) that couple hydride transfer to proton translocation (partipilo2023ahitchhiker’sguide pages 11-12, partipilo2023ahitchhiker’sguide pages 12-12). This supports the interpretation that, in redox-challenging conditions (such as growth modes with different NADPH demand), organisms can use transhydrogenases in conjunction with central metabolism enzymes like Icd to meet NADPH demands.

* **Systems biology of methylotrophic transitions:** Although not 2023–2024, Skovran et al. remains a foundational systems-level dataset integrating transcriptomics, enzyme activities, metabolites, and fluxes for AM1 during carbon-source switching; it identifies coordinated suppression of TCA genes (including icdA) during methanol transition and provides direct enzyme assay approaches for Icd (skovran2010asystemsbiology pages 13-14, skovran2010asystemsbiology pages 8-10).

### 7) Current applications and real-world implementations

#### 7.1 Metabolic engineering relevance in methylotroph chassis
*M. extorquens* AM1 is widely used as a **model methylotroph** and engineering chassis; the studies retrieved here inform engineering in two concrete ways:

1) **Identifying metabolic control points during substrate switching:** Skovran et al. integrate multiple omics layers and enzyme assays to identify potential regulatory/flux control points during transitions to methanol utilization (skovran2010asystemsbiology pages 8-10). Because icdA and Icd activity decrease during the shift, strategies that alter TCA flux or NADPH supply during methylotrophic transitions can be informed by these dynamics (skovran2010asystemsbiology pages 8-10).

2) **Engineering acetate/C2 assimilation and redox balance:** Schneider et al. provide quantitative flux partitioning (68% acetyl-CoA to TCA; 98% fully oxidized) and identify strong induction of pntAB (~12-fold), revealing that acetate growth in AM1 relies on a catabolic TCA plus explicit redox balancing machinery, which are actionable design constraints/targets for engineering strains for C2 substrates or mixed feeds (schneider2012theethylmalonylcoapathway pages 5-7, schneider2012theethylmalonylcoapathway pages 4-4).

#### 7.2 Design principle transferable to synthetic biology
The 2023 perspective on NAD(P)H supply frames transhydrogenases (membrane and soluble) as practical tools to manage NADPH limitations in engineered systems (partipilo2023ahitchhiker’sguide pages 11-12, partipilo2023ahitchhiker’sguide pages 12-12). This is directly relevant to any application requiring robust NADPH supply and suggests how NADPH-generating steps (including Icd) can be complemented by transhydrogenases when the metabolic network’s NADH/NADPH production ratio does not match biosynthetic demand.

### 8) Key quantitative statistics (from the retrieved AM1 studies)
* During acetate growth, **icd (gene 3354)** protein abundance increases (**fold change 2.4**, p = 0.01) relative to methanol growth (schneider2012theethylmalonylcoapathway pages 4-4).
* During acetate growth, **pntA/pntB** (membrane NAD(P) transhydrogenase) abundance increases strongly (**fold changes 12.5 and 12.3**, respectively) (schneider2012theethylmalonylcoapathway pages 4-4).
* Flux analysis on acetate: **68%** of acetyl-CoA enters the TCA cycle; **98%** of the acetyl-CoA entering the TCA is fully oxidized to CO2; only **2%** is oxidized to 2-oxoglutarate as a biomass precursor (schneider2012theethylmalonylcoapathway pages 5-7).
* During succinate→methanol transition, Icd enzymatic activity declines to about **79%** of initial activity (skovran2010asystemsbiology pages 8-10).
* Icd assay method: activity tracked as **NADPH production at 340 nm** (ε = **6.2 mM−1 cm−1**) in cell extracts prepared in **100 mM potassium phosphate buffer pH 7.5**; assays run in **200 µL** volume plate reader format (skovran2010asystemsbiology pages 13-14).

### 9) Summary: functional annotation statement (evidence-weighted)
**icd/icdA (gene 3354)** in *Methylorubrum extorquens* AM1 encodes a **NADP-dependent isocitrate dehydrogenase (Icd)** that produces **NADPH** (experimentally assayed via NADPH formation at 340 nm) and functions as a **TCA cycle enzyme** whose abundance and activity change with growth substrate. On acetate, AM1 uses a strongly catabolic TCA cycle (high acetyl-CoA flux into TCA and near-complete oxidation), with increased Icd abundance and strongly increased transhydrogenase abundance, consistent with a coordinated strategy for **reducing-equivalent generation and NADH/NADPH balancing**. During transition to methanol growth, icdA transcription and Icd activity decrease, consistent with broad reconfiguration of central metabolism during onset of methylotrophy (skovran2010asystemsbiology pages 13-14, skovran2010asystemsbiology pages 8-10, schneider2012theethylmalonylcoapathway pages 5-7, schneider2012theethylmalonylcoapathway pages 4-4).

### 10) Evidence gaps and recommended next steps
* **Direct UniProt crosswalk:** Obtain the UniProt entry (C5AXM3) or AM1 genome annotation file showing **MexAM1_META1p3354 ↔ gene 3354 ↔ icd** mapping.
* **Localization:** Seek subcellular fractionation or proteomics localization studies (cytosolic vs membrane) for AM1 Icd.
* **2023–2024 AM1-specific icd work:** Additional targeted searches (e.g., PubMed/UniProt crossrefs; AM1 genome-scale model updates; recent AM1 omics papers) may uncover newer AM1-specific evidence not retrieved in the present tool run.


References

1. (schneider2012theethylmalonylcoapathway pages 4-4): Kathrin Schneider, Rémi Peyraud, Patrick Kiefer, Philipp Christen, Nathanaël Delmotte, Stéphane Massou, Jean-Charles Portais, and Julia A. Vorholt. The ethylmalonyl-coa pathway is used in place of the glyoxylate cycle by methylobacterium extorquens am1 during growth on acetate. Journal of Biological Chemistry, 287:757-766, Jan 2012. URL: https://doi.org/10.1074/jbc.m111.305219, doi:10.1074/jbc.m111.305219. This article has 106 citations and is from a domain leading peer-reviewed journal.

2. (skovran2010asystemsbiology pages 13-14): Elizabeth Skovran, Gregory J. Crowther, Xiaofeng Guo, Song Yang, and Mary E. Lidstrom. A systems biology approach uncovers cellular strategies used by methylobacterium extorquens am1 during the switch from multi- to single-carbon growth. PLoS ONE, 5:e14091, Nov 2010. URL: https://doi.org/10.1371/journal.pone.0014091, doi:10.1371/journal.pone.0014091. This article has 77 citations and is from a peer-reviewed journal.

3. (skovran2010asystemsbiology pages 8-10): Elizabeth Skovran, Gregory J. Crowther, Xiaofeng Guo, Song Yang, and Mary E. Lidstrom. A systems biology approach uncovers cellular strategies used by methylobacterium extorquens am1 during the switch from multi- to single-carbon growth. PLoS ONE, 5:e14091, Nov 2010. URL: https://doi.org/10.1371/journal.pone.0014091, doi:10.1371/journal.pone.0014091. This article has 77 citations and is from a peer-reviewed journal.

4. (schneider2012theethylmalonylcoapathway pages 5-7): Kathrin Schneider, Rémi Peyraud, Patrick Kiefer, Philipp Christen, Nathanaël Delmotte, Stéphane Massou, Jean-Charles Portais, and Julia A. Vorholt. The ethylmalonyl-coa pathway is used in place of the glyoxylate cycle by methylobacterium extorquens am1 during growth on acetate. Journal of Biological Chemistry, 287:757-766, Jan 2012. URL: https://doi.org/10.1074/jbc.m111.305219, doi:10.1074/jbc.m111.305219. This article has 106 citations and is from a domain leading peer-reviewed journal.

5. (partipilo2023ahitchhiker’sguide pages 11-12): Michele Partipilo, Nico J. Claassens, and Dirk Jan Slotboom. A hitchhiker’s guide to supplying enzymatic reducing power into synthetic cells. ACS Synthetic Biology, 12:947-962, Apr 2023. URL: https://doi.org/10.1021/acssynbio.3c00070, doi:10.1021/acssynbio.3c00070. This article has 13 citations and is from a domain leading peer-reviewed journal.

6. (partipilo2023ahitchhiker’sguide pages 12-12): Michele Partipilo, Nico J. Claassens, and Dirk Jan Slotboom. A hitchhiker’s guide to supplying enzymatic reducing power into synthetic cells. ACS Synthetic Biology, 12:947-962, Apr 2023. URL: https://doi.org/10.1021/acssynbio.3c00070, doi:10.1021/acssynbio.3c00070. This article has 13 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](icd-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. schneider2012theethylmalonylcoapathway pages 4-4
2. skovran2010asystemsbiology pages 13-14
3. skovran2010asystemsbiology pages 8-10
4. schneider2012theethylmalonylcoapathway pages 5-7
5. NADP
6. https://doi.org/10.1371/journal.pone.0014091
7. https://doi.org/10.1074/jbc.M111.305219
8. https://doi.org/10.1021/acssynbio.3c00070
9. https://doi.org/10.1074/jbc.m111.305219,
10. https://doi.org/10.1371/journal.pone.0014091,
11. https://doi.org/10.1021/acssynbio.3c00070,