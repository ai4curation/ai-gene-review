---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-21T13:53:29.756708'
end_time: '2026-05-21T14:18:08.672039'
duration_seconds: 1478.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: CHLRE
  gene_id: Q00914
  gene_symbol: psaC
  uniprot_accession: Q00914
  protein_description: 'RecName: Full=Photosystem I iron-sulfur center {ECO:0000255|HAMAP-Rule:MF_01303};
    EC=1.97.1.12 {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=9 kDa polypeptide
    {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=PSI-C {ECO:0000255|HAMAP-Rule:MF_01303};
    AltName: Full=Photosystem I subunit VII {ECO:0000255|HAMAP-Rule:MF_01303}; AltName:
    Full=PsaC {ECO:0000255|HAMAP-Rule:MF_01303};'
  gene_info: Name=psaC {ECO:0000255|HAMAP-Rule:MF_01303};
  organism_full: Chlamydomonas reinhardtii (Chlamydomonas smithii).
  protein_family: Not specified in UniProt
  protein_domains: 4Fe4S_Fe-S-bd. (IPR017896); 4Fe4S_Fe_S_CS. (IPR017900); PSI_iron-sulfur_center.
    (IPR050157); PSI_PsaC. (IPR017491); Fer4_7 (PF12838)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 47
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: psaC-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: psaC-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000040 Figure 2B on page 5 provides a schematic
    representation of the Photosystem I (PSI) electron transfer chain. The ''Right
    side view'' e'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q00914
- **Protein Description:** RecName: Full=Photosystem I iron-sulfur center {ECO:0000255|HAMAP-Rule:MF_01303}; EC=1.97.1.12 {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=9 kDa polypeptide {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=PSI-C {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=Photosystem I subunit VII {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=PsaC {ECO:0000255|HAMAP-Rule:MF_01303};
- **Gene Information:** Name=psaC {ECO:0000255|HAMAP-Rule:MF_01303};
- **Organism (full):** Chlamydomonas reinhardtii (Chlamydomonas smithii).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 4Fe4S_Fe-S-bd. (IPR017896); 4Fe4S_Fe_S_CS. (IPR017900); PSI_iron-sulfur_center. (IPR050157); PSI_PsaC. (IPR017491); Fer4_7 (PF12838)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "psaC" matches the protein description above**
2. **Verify the organism is correct:** Chlamydomonas reinhardtii (Chlamydomonas smithii).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'psaC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **psaC** (gene ID: Q00914, UniProt: Q00914) in CHLRE.

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
- **UniProt Accession:** Q00914
- **Protein Description:** RecName: Full=Photosystem I iron-sulfur center {ECO:0000255|HAMAP-Rule:MF_01303}; EC=1.97.1.12 {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=9 kDa polypeptide {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=PSI-C {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=Photosystem I subunit VII {ECO:0000255|HAMAP-Rule:MF_01303}; AltName: Full=PsaC {ECO:0000255|HAMAP-Rule:MF_01303};
- **Gene Information:** Name=psaC {ECO:0000255|HAMAP-Rule:MF_01303};
- **Organism (full):** Chlamydomonas reinhardtii (Chlamydomonas smithii).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 4Fe4S_Fe-S-bd. (IPR017896); 4Fe4S_Fe_S_CS. (IPR017900); PSI_iron-sulfur_center. (IPR050157); PSI_PsaC. (IPR017491); Fer4_7 (PF12838)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "psaC" matches the protein description above**
2. **Verify the organism is correct:** Chlamydomonas reinhardtii (Chlamydomonas smithii).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'psaC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **psaC** (gene ID: Q00914, UniProt: Q00914) in CHLRE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research Report: *Chlamydomonas reinhardtii* **psaC** (UniProt **Q00914**) — Photosystem I iron–sulfur center subunit (PSI-C)

## Executive summary
The *Chlamydomonas reinhardtii* chloroplast gene **psaC** (UniProt **Q00914**) encodes the stromal, membrane-extrinsic Photosystem I (PSI) subunit **PsaC/PSI‑C**, a small ferredoxin-like protein that binds the terminal/secondary **[4Fe–4S] iron–sulfur clusters FA and FB** that relay light-generated electrons from PSI to soluble acceptors such as **ferredoxin (Fd)** (and in some conditions **flavodoxin**) to support NADPH production and broader reductive metabolism. This identity is directly supported by a Chlamydomonas proteomics study that explicitly labels **PsaC (Q00914)** as a PSI iron–sulfur center protein. (ford2019inhibitionoftor pages 16-18, ford2019inhibitionoftor pages 14-16)

Functionally, PsaC is essential for PSI integrity and oxygenic photosynthesis in *Chlamydomonas*: **deletion of psaC eliminates detectable functional PSI, photoautotrophic growth, and strongly impairs CO2 fixation and H2 photoproduction**, with residual electron transport signatures reflecting non-PSI processes. (redding1999photosystemiis pages 7-8, redding1999photosystemiis pages 5-7, redding1999photosystemiis pages 2-3)

## 1) Key concepts and definitions (current understanding)

### 1.1 Photosystem I as a plastocyanin–ferredoxin oxidoreductase
PSI is widely described as a **light-driven plastocyanin–ferredoxin oxidoreductase**, transferring electrons from lumenal donors (plastocyanin; in algae often also cytochrome c6) to stromal acceptors (ferredoxin) to generate reducing power for metabolism. (rolo2024structurefunctionand pages 3-4, rochaix2000chloroplastsitedirectedmutagenesis pages 2-3)

### 1.2 What is PsaC?
**PsaC** is the stromal-side PSI subunit that carries the terminal iron–sulfur electron acceptors **FA and FB** (both **[Fe4–S4]** clusters) and participates in forming the stromal “ridge” (with PsaD and PsaE) that supports **ferredoxin docking** for productive electron transfer. (rolo2024structurefunctionand pages 4-5, ozawa2018configurationoften pages 1-2)

A 2024 review summarizes that PsaC together with the PsaA–PsaB reaction-center heterodimer carries the cofactors for plastocyanin→ferredoxin oxidoreduction, explicitly including the **three [Fe4–S4] clusters FX, FA, and FB**. (rolo2024structurefunctionand pages 3-4)

### 1.3 Biochemical reaction context / EC number interpretation
The UniProt record associates PsaC with EC **1.97.1.12**, reflecting PSI’s overall oxidoreductase activity of transferring electrons from reduced plastocyanin/cytochrome c6 to ferredoxin through the PSI cofactor chain, with PsaC specifically functioning as the protein scaffold that binds FA/FB and enables terminal electron transfer to soluble acceptors. Consistent with this, PSI electron flow is described as plastocyanin → P700 → internal cofactors → **PsaC FA/FB** → ferredoxin. (rolo2024structurefunctionand pages 4-5)

## 2) Molecular function: electron-transfer role of PsaC and its partners

### 2.1 Cofactors bound by PsaC
PsaC contains the terminal/secondary **FA and FB [4Fe–4S] clusters** and sits adjacent to the FX site of the PsaA–PsaB core, accepting electrons from upstream cofactors and passing them onward to ferredoxin. (rolo2024structurefunctionand pages 4-5)

Figure evidence: a Plant Cell 2024 schematic shows the PSI electron-transfer chain with **PsaC housing FA/FB on the stromal side**. (rolo2024structurefunctionand media e293fb55)

### 2.2 Electron donor(s) to PSI vs acceptor(s) from PSI
Structural evidence indicates that the **binding site of the reduced electron carriers** (plastocyanin and cytochrome c6) is on the **luminal face** of PSI. (caspy2020thestructureof pages 3-4)

On the stromal side, ferredoxin binds near PsaC. In a PSI–ferredoxin complex structure, multiple close contacts between PsaC and ferredoxin are reported, including specific residue–residue proximity constraints (Å-level distances) and an experimental record that mutagenesis of several PsaC residues impacts ferredoxin binding. (caspy2020thestructureof pages 3-4)

### 2.3 Quantitative kinetics: PsaC residues tune ferredoxin/flavodoxin electron transfer
**Targeted psaC mutations in *Chlamydomonas*** provide strong, quantitative evidence that PsaC residues tune electron-transfer kinetics and docking affinity for soluble acceptors:

* **K52/R53 region (near FA):** A psaC double mutant **K52S/R53A** accumulates only **~20–30%** PSI and shows altered low-temperature FA/FB behavior (preferential FB photoreduction at 15 K) but maintains near-normal PSI→ferredoxin electron transfer at room temperature. Quantitatively, ferredoxin binding/dynamics were similar (Kd **6.1 µM** WT vs **7.3 µM** mutant) and second-order rate constants were **3.5 × 10^8 M⁻¹ s⁻¹** (WT) vs **5.6 × 10^8 M⁻¹ s⁻¹** (mutant), with a fast reduction phase measurable in the microsecond regime. (fischer1997targetedmutationsin pages 7-8, fischer1997targetedmutationsin pages 8-9, fischer1997targetedmutationsin pages 1-2)

* **Lys35 (key electrostatic contact):** Mutations at **PsaC Lys35** strongly impact photoreduction of external acceptors. For flavodoxin reduction, half-times and second-order constants show that charge inversion (Lys→Glu/Asp) severely slows electron transfer, while Lys→Arg largely preserves WT kinetics. Example quantitative outcomes include oxidized-flavodoxin t1/2 **2.4 ms** (WT) vs **<9.9 ms** (Lys35Glu), semiquinone t1/2 **0.35 ms** (WT) vs **<9.9 ms** (Lys35Glu), and second-order constants dropping from **0.96 × 10^8 M⁻¹ s⁻¹** (WT) to **0.05 × 10^8 M⁻¹ s⁻¹** (Lys35Glu). Cross-linking experiments also indicate Lys35 is necessary for forming a flavodoxin–PsaC adduct. (meimberg1999lys35ofpsac pages 3-4, meimberg1999lys35ofpsac pages 4-6, meimberg1999lys35ofpsac pages 6-7)

These data support a mechanistic model where PsaC is not merely a passive Fe–S carrier but **actively shapes encounter complex formation, orientation, and ET efficiency** for stromal acceptors.

### 2.4 Stress/redox regulation signals involving PsaC
In a TOR-inhibition proteomics study in *Chlamydomonas*, **PsaC (Q00914)** is explicitly described as a PSI subunit containing an iron–sulfur center and showed a substantial increase in reversible cysteine oxidation (reported fold-changes include **2.46** for a significant oxidation identifier and **3.36** in discussion). These redox changes were discussed in the context of altered electron-flow partitioning (e.g., shifts toward cyclic electron flow or downstream bottlenecks). (ford2019inhibitionoftor pages 16-18, ford2019inhibitionoftor pages 14-16)

## 3) Cellular and subcellular localization

### 3.1 Subcellular location
PsaC functions in the **chloroplast thylakoid membrane system** as part of PSI. It is **membrane-extrinsic on the stromal side** (i.e., chloroplast stroma-facing surface of PSI), where it presents FA/FB and forms part of the ferredoxin-docking ridge. (caspy2020thestructureof pages 3-4, rolo2024structurefunctionand pages 4-5, ozawa2018configurationoften pages 1-2)

### 3.2 Topological context (two-sided electron-transfer)
PSI is topologically polarized: electron donation occurs on the **luminal** face (plastocyanin/cytochrome c6), while electron acceptance occurs on the **stromal** face (ferredoxin binding near PsaC). (caspy2020thestructureof pages 3-4, rolo2024structurefunctionand pages 3-4)

## 4) Pathways and biological processes involving psaC/PsaC

### 4.1 Linear electron flow (LEF) and NADPH generation
Reduced ferredoxin produced by PSI is primarily reoxidized by ferredoxin–NADP+ reductase (FNR) to generate NADPH in LEF. (rolo2024structurefunctionand pages 3-4)

### 4.2 Alternative acceptors and iron-stress substitution
A 2024 review notes that under iron deprivation, **flavodoxin can substitute for ferredoxin** and accept electrons from a **PsaC-coordinated [4Fe–4S] cluster**, emphasizing functional flexibility at the PSI acceptor side. (tian2024photosystemiaa pages 2-4)

### 4.3 Cyclic electron flow (CEF) and photoprotection/ATP balancing
Ferredoxin can also route electrons into **cyclic electron flow** from the PSI acceptor side back to cytochrome b6f, increasing proton motive force without NADPH production and thereby increasing ATP/NADPH ratio and protecting PSI against over-reduction. (rolo2024structurefunctionand pages 3-4)

## 5) Mutant and phenotype evidence in *Chlamydomonas reinhardtii*

### 5.1 psaC is essential for PSI function and photoautotrophy
Chloroplast deletion of **psaC** causes loss of photoautotrophic growth and PSI detectability by immunological and spectroscopic assays, with **CO2 uptake reduced from ~1500 to ~210 nmol·min⁻¹·mg Chl⁻¹** and **H2 evolution reduced from ~1200 to ~3 nmol·min⁻¹·mg Chl⁻¹** (WT vs psaC-deletion strain values as reported). (redding1999photosystemiis pages 5-7, redding1999photosystemiis pages 2-3)

These data support that PsaC is indispensable for establishing the PSI acceptor side capable of reducing ferredoxin sufficiently to drive CO2 fixation and hydrogenase-linked H2 photoevolution. (redding1999photosystemiis pages 7-8, redding1999photosystemiis pages 2-3)

### 5.2 psaC mutations impact PSI stability, light sensitivity, and acceptor-side ET
Site-directed mutant analysis shows multiple mechanistic phenotypes:
* K52/R53 mutations destabilize PSI to varying degrees, alter low-temperature FA/FB behavior, and can produce aerobic photosensitivity while preserving near-normal PSI→ferredoxin ET at room temperature in some alleles. (fischer1997targetedmutationsin pages 1-2)
* Lys35 mutations strongly reduce rates of electron transfer to flavodoxin and (by parallel mechanistic rationale) ferredoxin. (meimberg1999lys35ofpsac pages 3-4, meimberg1999lys35ofpsac pages 4-6)
* A Chlamydomonas PSI mutagenesis review describes that psaC mutations can decrease acceptor-side ET, increase ferredoxin affinity, and lead to **high light sensitivity**; it also notes an estimated FA–FB redox potential difference on the order of **~50 mV** and frames PsaC/FA placement as protective against electron escape to oxygen. (rochaix2000chloroplastsitedirectedmutagenesis pages 8-9)

## 6) Recent developments (prioritizing 2023–2024) and latest research directions

### 6.1 2024 structural and assembly perspectives: PsaC’s role in biogenesis
A major 2024 Plant Cell review synthesizes current knowledge of PSI assembly, including the idea that intermediates exposing or lacking Fe–S clusters (FX/FA/FB) can be oxidation sensitive and that correct incorporation/stabilization of PsaC and its clusters is integrated with formation of the stromal ridge and ferredoxin docking features. (rolo2024structurefunctionand pages 13-14)

A 2024 high-resolution cryo-EM study of a cyanobacterial **PsaC-less assembly intermediate** reports that removing PsaC eliminates FA/FB and is associated with **incomplete FX formation** and missing stromal subunits PsaD and PsaE, supporting a model in which **PsaC binding promotes conformational states needed for proper FX maturation and subsequent stromal-subunit incorporation** (note: cyanobacterial system, but informative mechanistically). (naschberger20241.8åresolution pages 1-5, naschberger20241.8åresolution pages 5-8)

### 6.2 2024 expert analysis: conservation vs flexibility
A 2024 expert review emphasizes that PSI has a remarkably conserved core but flexible peripheral architecture, and describes PsaC as a conserved Fe–S protein (FA/FB) that helps stabilize extremely low-potential electrons and protect PSI from radical damage; it also advances an interpretation that PSI maintains two electron-transfer branches, potentially balancing efficiency with protective “slippage.” (nelson2024investigatingthebalance pages 3-5, nelson2024investigatingthebalance pages 1-3)

### 6.3 2024 algal PSI supercomplex diversity (context for psaC functional environment)
A 2024 IJMS review on PSI adaptations highlights that *Chlamydomonas* PSI can exist in multiple supramolecular forms (e.g., PSI–LHCI–LHCII supercomplex in state transitions; PSI–LHCI dimers under low light/anoxia) with hundreds of cofactors, underscoring that while PsaC’s Fe–S function is conserved, the **antenna and supercomplex context that modulates excitation/electron flow is highly plastic**. (tian2024photosystemiaa pages 7-9)

## 7) Current applications and real-world implementations

### 7.1 Photosynthetic hydrogen production and bioenergy engineering
Because PsaC-mediated terminal electron transfer is required to reduce ferredoxin, and reduced ferredoxin is a key electron donor for algal hydrogenases, psaC integrity is a prerequisite for **photobiological H2 production**. This is supported by direct experiments showing **H2 photoevolution is essentially absent in psaC deletion mutants** (vs robust WT H2 evolution). (redding1999photosystemiis pages 7-8, redding1999photosystemiis pages 2-3)

### 7.2 Engineering/biotechnology: tuning stromal acceptor interactions
Quantitative mutagenesis at PsaC residues (e.g., Lys35; K52/R53 region) demonstrates that **electron-transfer rates and binding affinities to soluble acceptors are tunable** by targeted changes. This principle is broadly relevant to synthetic biology strategies aiming to rewire electron flow to desired metabolic sinks (e.g., hydrogenases, reductive biosynthesis, or redox enzymes), even if direct industrial deployment remains developmental. (fischer1997targetedmutationsin pages 8-9, meimberg1999lys35ofpsac pages 3-4)

### 7.3 Structural biology and modeling platforms
High-resolution structural studies of PSI with bound partners (ferredoxin, plastocyanin) provide atomistic interaction maps—PsaC contributes multiple close-contact residues to ferredoxin binding—supporting rational design of PSI–acceptor interfaces. (caspy2020thestructureof pages 3-4)

## 8) Key statistics and data points (from the cited studies)

* **PSI-LHCI stoichiometry in *Chlamydomonas*:** ~10 LHCI subunits per PSI-LHCI, including **LHCA1 at 1.81 ± 0.07 copies** and ~1 copy each of LHCA2–LHCA9; PSAD ~1.17 ± 0.19 and PSAF ~1.00 ± 0.19; apparent complex size ~700 kDa. (ozawa2018configurationoften pages 2-3, ozawa2018configurationoften pages 8-9)
* **psaC deletion phenotype (gas exchange/H2):** WT CO2 uptake **1500** vs psaC deletion **210** nmol·min⁻¹·mg Chl⁻¹; WT H2 evolution **1200** vs psaC deletion **~3** nmol·min⁻¹·mg Chl⁻¹; phototrophic growth absent. (redding1999photosystemiis pages 2-3)
* **PsaC K52S/R53A mutant:** PSI accumulation **~20–30%**; Fd Kd **6.1 µM** (WT) vs **7.3 µM**; second-order constants **3.5 × 10^8** (WT) vs **5.6 × 10^8 M⁻¹ s⁻¹**; ~25% complexes with damaged redox cofactors. (fischer1997targetedmutationsin pages 7-8, fischer1997targetedmutationsin pages 8-9)
* **PsaC Lys35 mutants (flavodoxin ET):** oxidized flavodoxin t1/2 **2.4 ms** (WT) vs **<9.9 ms** (Lys35Glu); semiquinone t1/2 **0.35 ms** (WT) vs **<9.9 ms** (Lys35Glu); second-order constant **0.96 × 10^8** (WT) vs **0.05 × 10^8 M⁻¹ s⁻¹** (Lys35Glu). (meimberg1999lys35ofpsac pages 3-4, meimberg1999lys35ofpsac pages 4-6)
* **Redox proteomics under TOR inhibition:** PsaC (Q00914) oxidation fold-changes reported as **2.46** (significant oxidation identifier) and **3.36** (discussion). (ford2019inhibitionoftor pages 16-18, ford2019inhibitionoftor pages 14-16)

## Evidence map (tabular)
The following table consolidates the most directly relevant experimental findings and quantitative data for functional annotation of *Chlamydomonas* PsaC (Q00914).

| Study (author year) | System/approach | Key PsaC-related finding | Quantitative data (rates, Kd, stoichiometry, fold changes) | URL/DOI |
|---|---|---|---|---|
| Ford et al. 2019 | *Chlamydomonas reinhardtii*; redox proteomics after TOR inhibition | PsaC was explicitly identified as the PSI iron-sulfur center protein corresponding to UniProt Q00914; cysteine oxidation changes were linked to altered photosynthetic electron flow/cyclic electron transport hypotheses. (ford2019inhibitionoftor pages 16-18, ford2019inhibitionoftor pages 14-16) | PsaC oxidation fold change 3.36 in discussion; significant oxidation identifier fold change 2.46 in results. (ford2019inhibitionoftor pages 16-18, ford2019inhibitionoftor pages 14-16) | https://doi.org/10.3390/cells8101171 |
| Fischer et al. 1997 | Chloroplast site-directed mutagenesis of *psaC* in *C. reinhardtii*; low-temperature EPR, flash absorption, ferredoxin reduction assays | PsaC residues K52/R53 affect PSI stability and low-temperature FA/FB behavior; K52S/R53A caused preferential FB photoreduction at low temperature but did not measurably impair PSI→ferredoxin electron transfer at room temperature. (fischer1997targetedmutationsin pages 7-8, fischer1997targetedmutationsin pages 3-4, fischer1997targetedmutationsin pages 8-9, fischer1997targetedmutationsin pages 1-2) | K52S/R53A accumulated ~20–30% PSI; WT ferredoxin Kd 6.1 µM vs mutant 7.3 µM; second-order rate constants 3.5 × 10^8 M^-1 s^-1 (WT) vs 5.6 × 10^8 M^-1 s^-1 (mutant); WT P700 kinetics half-times 10 µs, 22 ms, 1.2 s; mutant 20 µs, 1.6 ms, 27 ms, 1.2 s; ~25% mutant complexes had damaged redox cofactors. (fischer1997targetedmutationsin pages 7-8, fischer1997targetedmutationsin pages 3-4, fischer1997targetedmutationsin pages 8-9, fischer1997targetedmutationsin pages 1-2) | https://doi.org/10.1021/bi962244v |
| Meimberg et al. 1999 | Site-directed mutagenesis of PsaC Lys35; flavodoxin photoreduction kinetics, flash absorption, EDC cross-linking | Lys35 is an important electrostatic contact for docking/reduction of soluble acceptors; charge inversion at Lys35 strongly impairs PSI-mediated flavodoxin reduction, while Lys35Arg largely preserves WT behavior. (meimberg1999lys35ofpsac pages 7-7, meimberg1999lys35ofpsac pages 3-4, meimberg1999lys35ofpsac pages 1-2, meimberg1999lys35ofpsac pages 4-6, meimberg1999lys35ofpsac pages 6-7) | Oxidized flavodoxin t1/2: WT 2.4 ms; Lys35Arg <2.2 ms; Lys35Asp <7.5 ms; Lys35Glu <9.9 ms. Semiquinone t1/2: WT 0.35 ms; Lys35Arg ~0.32 ms; Lys35Asp <5.8 ms; Lys35Glu <9.9 ms. Second-order constants: WT 0.96 × 10^8 M^-1 s^-1; Lys35Arg 1.1 × 10^8; Lys35Asp 0.115 × 10^8; Lys35Glu 0.05 × 10^8; semiquinone reduction for Lys35Asp/Lys35Glu reported as 1 × 10^7 and 5 × 10^6 M^-1 s^-1, respectively; steady-state rates ~49.7–63.4 mmol flavodoxin·mg chl^-1·h^-1; ~0.6–0.9 flavodoxin molecules reduced per PSI center. (meimberg1999lys35ofpsac pages 3-4, meimberg1999lys35ofpsac pages 1-2, meimberg1999lys35ofpsac pages 4-6, meimberg1999lys35ofpsac pages 6-7) | https://doi.org/10.1046/j.1432-1327.1999.00474.x |
| Redding et al. 1999 | Chloroplast deletion of *psaC* or *psaA*; immunoblotting, spectroscopy, mass spectrometry, growth and gas-exchange assays | PsaC is essential for functional PSI in *C. reinhardtii*; deleting *psaC* abolished photoautotrophic growth, CO2 fixation, detectable PSI, and essentially all H2 photoproduction. (redding1999photosystemiis pages 7-8, redding1999photosystemiis pages 1-2, redding1999photosystemiis pages 5-7, redding1999photosystemiis pages 2-3, redding1999photosystemiis pages 3-5) | In psaC-deletion strain: residual PsaA ~5–10% of WT, no detectable PsaD, no photooxidizable P700, CO2 uptake ~210 nmol·min^-1·mg Chl^-1, H2 evolution ~3 nmol·min^-1·mg Chl^-1, phototrophic growth absent; WT values listed as CO2 uptake 1500, O2 evolution 1530, H2 evolution 1200 nmol·min^-1·mg Chl^-1. Reverted psaA strain restored P700 to ~40% of WT. (redding1999photosystemiis pages 5-7, redding1999photosystemiis pages 2-3, redding1999photosystemiis pages 3-5) | https://doi.org/10.1074/jbc.274.15.10466 |
| Ozawa et al. 2018 | Quantitative [14C]-labeling, SDS-PAGE, cross-linking analysis of *C. reinhardtii* PSI-LHCI | PsaC was described as a peripheral PSI subunit on the stromal side that binds FA and FB and, with PsaD/PsaE, forms the stromal ridge for ferredoxin docking. (ozawa2018configurationoften pages 1-2) | PSI-LHCI contained 10 LHCI subunits total: LHCA1 at 1.81 ± 0.07 copies and ~1 copy each of LHCA2–LHCA9; apparent complex size ~700 kD; PSAD 1.17 ± 0.19 and PSAF 1.00 ± 0.19 copies. (ozawa2018configurationoften pages 1-2, ozawa2018configurationoften pages 2-3, ozawa2018configurationoften pages 8-9) | https://doi.org/10.1104/pp.18.00749 |
| Caspy et al. 2020 | Structural analysis of PSI with ferredoxin and plastocyanin | PsaC lies on the stromal side of PSI, houses the terminal Fe-S centers, and makes multiple close contacts with ferredoxin; plastocyanin/cytochrome c6 bind on the luminal face. (caspy2020thestructureof pages 3-4, caspy2020thestructureof pages 4-5) | PsaC residues Ile12, Gly13, Cys14, Thr15, Gln16, Ala36, Pro59 were within ≤6 Å of ferredoxin; specific contacts included Arg19(PsaC)-Glu92(Fd) 5.0 Å and Lys35(PsaC)-Asp34(Fd) 3.5 Å; Cu+ center of plastocyanin located 14.7 Å from P700. In *C. reinhardtii*, PsaB substitutions D612H/E613H reduced plastocyanin Kd by >5-fold. (caspy2020thestructureof pages 3-4, caspy2020thestructureof pages 4-5) | https://doi.org/10.1038/s41477-020-00779-9 |
| Rolo et al. 2024 | Expert review of PSI structure/function/assembly | PsaC is the stromal PSI subunit that contains FA and FB [Fe4-S4] clusters; PSAD/PSAE stabilize PsaC attachment and support ferredoxin docking. Loss of PsaC abolishes PSI accumulation and photoautotrophy. (rolo2024structurefunctionand pages 3-4, rolo2024structurefunctionand pages 4-5) | PSI core mass 422 kDa; PsaA-PsaB heterodimer 257 kDa; PSI-LHCI ~584 kDa; LHCI belt ~162 kDa. Electron flow proceeds plastocyanin → P700 → FX → FA/FB → ferredoxin. (rolo2024structurefunctionand pages 4-5, rolo2024structurefunctionand pages 3-4) | https://doi.org/10.1093/plcell/koae169 |


*Table: This table summarizes core experimental and review evidence for Chlamydomonas reinhardtii PsaC/PSI-C (UniProt Q00914), focusing on function, localization, docking interactions, mutant phenotypes, and quantitative kinetic or stoichiometric data. It is useful as a compact evidence map for functional annotation.*

## Conclusion (functional annotation statement)
**psaC (UniProt Q00914) encodes the PSI stromal iron–sulfur center subunit PsaC (PSI‑C) in *Chlamydomonas reinhardtii*.** PsaC binds the terminal **[4Fe–4S] clusters FA and FB**, forms part of the stromal ferredoxin docking ridge with PsaD/PsaE, and is indispensable for productive PSI electron transfer to soluble acceptors (ferredoxin/flavodoxin), enabling CO2 fixation and hydrogen photoproduction in vivo. This function is supported by structural interaction mapping, quantitative acceptor-side kinetics from site-directed mutants, and strong loss-of-function phenotypes in psaC deletion strains. (caspy2020thestructureof pages 3-4, rolo2024structurefunctionand pages 4-5, fischer1997targetedmutationsin pages 8-9, meimberg1999lys35ofpsac pages 3-4, redding1999photosystemiis pages 2-3)


References

1. (ford2019inhibitionoftor pages 16-18): Megan M. Ford, Amanda L. Smythers, Evan W. McConnell, Sarah C. Lowery, Derrick R. J. Kolling, and Leslie M. Hicks. Inhibition of tor in chlamydomonas reinhardtii leads to rapid cysteine oxidation reflecting sustained physiological changes. Cells, 8:1171, Sep 2019. URL: https://doi.org/10.3390/cells8101171, doi:10.3390/cells8101171. This article has 28 citations.

2. (ford2019inhibitionoftor pages 14-16): Megan M. Ford, Amanda L. Smythers, Evan W. McConnell, Sarah C. Lowery, Derrick R. J. Kolling, and Leslie M. Hicks. Inhibition of tor in chlamydomonas reinhardtii leads to rapid cysteine oxidation reflecting sustained physiological changes. Cells, 8:1171, Sep 2019. URL: https://doi.org/10.3390/cells8101171, doi:10.3390/cells8101171. This article has 28 citations.

3. (redding1999photosystemiis pages 7-8): Kevin Redding, Laurent Cournac, Ilya R. Vassiliev, John H. Golbeck, Gilles Peltier, and Jean-David Rochaix. Photosystem i is indispensable for photoautotrophic growth, co2 fixation, and h2 photoproduction inchlamydomonas reinhardtii *. The Journal of Biological Chemistry, 274:10466-10473, Apr 1999. URL: https://doi.org/10.1074/jbc.274.15.10466, doi:10.1074/jbc.274.15.10466. This article has 92 citations.

4. (redding1999photosystemiis pages 5-7): Kevin Redding, Laurent Cournac, Ilya R. Vassiliev, John H. Golbeck, Gilles Peltier, and Jean-David Rochaix. Photosystem i is indispensable for photoautotrophic growth, co2 fixation, and h2 photoproduction inchlamydomonas reinhardtii *. The Journal of Biological Chemistry, 274:10466-10473, Apr 1999. URL: https://doi.org/10.1074/jbc.274.15.10466, doi:10.1074/jbc.274.15.10466. This article has 92 citations.

5. (redding1999photosystemiis pages 2-3): Kevin Redding, Laurent Cournac, Ilya R. Vassiliev, John H. Golbeck, Gilles Peltier, and Jean-David Rochaix. Photosystem i is indispensable for photoautotrophic growth, co2 fixation, and h2 photoproduction inchlamydomonas reinhardtii *. The Journal of Biological Chemistry, 274:10466-10473, Apr 1999. URL: https://doi.org/10.1074/jbc.274.15.10466, doi:10.1074/jbc.274.15.10466. This article has 92 citations.

6. (rolo2024structurefunctionand pages 3-4): David Rolo, Mark A Schöttler, Omar Sandoval-Ibáñez, and Ralph Bock. Structure, function, and assembly of psi in thylakoid membranes of vascular plants. The Plant Cell, 36:4080-4108, Jun 2024. URL: https://doi.org/10.1093/plcell/koae169, doi:10.1093/plcell/koae169. This article has 28 citations.

7. (rochaix2000chloroplastsitedirectedmutagenesis pages 2-3): J. Rochaix, N. Fischer, and M. Hippler. Chloroplast site-directed mutagenesis of photosystem i in chlamydomonas: electron transfer reactions and light sensitivity. Biochimie, 82 6-7:635-45, Jun 2000. URL: https://doi.org/10.1016/s0300-9084(00)00604-0, doi:10.1016/s0300-9084(00)00604-0. This article has 41 citations and is from a peer-reviewed journal.

8. (rolo2024structurefunctionand pages 4-5): David Rolo, Mark A Schöttler, Omar Sandoval-Ibáñez, and Ralph Bock. Structure, function, and assembly of psi in thylakoid membranes of vascular plants. The Plant Cell, 36:4080-4108, Jun 2024. URL: https://doi.org/10.1093/plcell/koae169, doi:10.1093/plcell/koae169. This article has 28 citations.

9. (ozawa2018configurationoften pages 1-2): Shin-Ichiro Ozawa, Till Bald, Takahito Onishi, Huidan Xue, Takunori Matsumura, Ryota Kubo, Hiroko Takahashi, Michael Hippler, and Yuichiro Takahashi. Configuration of ten light-harvesting chlorophyll a/b complex i subunits in chlamydomonas reinhardtii photosystem i. Plant Physiology, 178:583-595, Aug 2018. URL: https://doi.org/10.1104/pp.18.00749, doi:10.1104/pp.18.00749. This article has 89 citations and is from a highest quality peer-reviewed journal.

10. (rolo2024structurefunctionand media e293fb55): David Rolo, Mark A Schöttler, Omar Sandoval-Ibáñez, and Ralph Bock. Structure, function, and assembly of psi in thylakoid membranes of vascular plants. The Plant Cell, 36:4080-4108, Jun 2024. URL: https://doi.org/10.1093/plcell/koae169, doi:10.1093/plcell/koae169. This article has 28 citations.

11. (caspy2020thestructureof pages 3-4): Ido Caspy, Anna Borovikova-Sheinker, Daniel Klaiman, Yoel Shkolnisky, and Nathan Nelson. The structure of a triple complex of plant photosystem i with ferredoxin and plastocyanin. Nature Plants, 6:1300-1305, Oct 2020. URL: https://doi.org/10.1038/s41477-020-00779-9, doi:10.1038/s41477-020-00779-9. This article has 79 citations and is from a highest quality peer-reviewed journal.

12. (fischer1997targetedmutationsin pages 7-8): Nicolas Fischer, Pierre Sétif, and Jean-David Rochaix. Targeted mutations in the psac gene of chlamydomonas reinhardtii: preferential reduction of fb at low temperature is not accompanied by altered electron flow from photosystem i to ferredoxin. Biochemistry, 36 1:93-102, Jan 1997. URL: https://doi.org/10.1021/bi962244v, doi:10.1021/bi962244v. This article has 108 citations and is from a peer-reviewed journal.

13. (fischer1997targetedmutationsin pages 8-9): Nicolas Fischer, Pierre Sétif, and Jean-David Rochaix. Targeted mutations in the psac gene of chlamydomonas reinhardtii: preferential reduction of fb at low temperature is not accompanied by altered electron flow from photosystem i to ferredoxin. Biochemistry, 36 1:93-102, Jan 1997. URL: https://doi.org/10.1021/bi962244v, doi:10.1021/bi962244v. This article has 108 citations and is from a peer-reviewed journal.

14. (fischer1997targetedmutationsin pages 1-2): Nicolas Fischer, Pierre Sétif, and Jean-David Rochaix. Targeted mutations in the psac gene of chlamydomonas reinhardtii: preferential reduction of fb at low temperature is not accompanied by altered electron flow from photosystem i to ferredoxin. Biochemistry, 36 1:93-102, Jan 1997. URL: https://doi.org/10.1021/bi962244v, doi:10.1021/bi962244v. This article has 108 citations and is from a peer-reviewed journal.

15. (meimberg1999lys35ofpsac pages 3-4): Karen Meimberg, Nicolas Fischer, Jean‐David Rochaix, and Ulrich Mühlenhoff. Lys35 of psac is required for the efficient photoreduction of flavodoxin by photosystem i from chlamydomonas reinhardtii. European journal of biochemistry, 263 1:137-44, Jul 1999. URL: https://doi.org/10.1046/j.1432-1327.1999.00474.x, doi:10.1046/j.1432-1327.1999.00474.x. This article has 21 citations.

16. (meimberg1999lys35ofpsac pages 4-6): Karen Meimberg, Nicolas Fischer, Jean‐David Rochaix, and Ulrich Mühlenhoff. Lys35 of psac is required for the efficient photoreduction of flavodoxin by photosystem i from chlamydomonas reinhardtii. European journal of biochemistry, 263 1:137-44, Jul 1999. URL: https://doi.org/10.1046/j.1432-1327.1999.00474.x, doi:10.1046/j.1432-1327.1999.00474.x. This article has 21 citations.

17. (meimberg1999lys35ofpsac pages 6-7): Karen Meimberg, Nicolas Fischer, Jean‐David Rochaix, and Ulrich Mühlenhoff. Lys35 of psac is required for the efficient photoreduction of flavodoxin by photosystem i from chlamydomonas reinhardtii. European journal of biochemistry, 263 1:137-44, Jul 1999. URL: https://doi.org/10.1046/j.1432-1327.1999.00474.x, doi:10.1046/j.1432-1327.1999.00474.x. This article has 21 citations.

18. (tian2024photosystemiaa pages 2-4): Li-Rong Tian and Jing-Hua Chen. Photosystem i: a paradigm for understanding biological environmental adaptation mechanisms in cyanobacteria and algae. International Journal of Molecular Sciences, 25:8767, Aug 2024. URL: https://doi.org/10.3390/ijms25168767, doi:10.3390/ijms25168767. This article has 7 citations.

19. (rochaix2000chloroplastsitedirectedmutagenesis pages 8-9): J. Rochaix, N. Fischer, and M. Hippler. Chloroplast site-directed mutagenesis of photosystem i in chlamydomonas: electron transfer reactions and light sensitivity. Biochimie, 82 6-7:635-45, Jun 2000. URL: https://doi.org/10.1016/s0300-9084(00)00604-0, doi:10.1016/s0300-9084(00)00604-0. This article has 41 citations and is from a peer-reviewed journal.

20. (rolo2024structurefunctionand pages 13-14): David Rolo, Mark A Schöttler, Omar Sandoval-Ibáñez, and Ralph Bock. Structure, function, and assembly of psi in thylakoid membranes of vascular plants. The Plant Cell, 36:4080-4108, Jun 2024. URL: https://doi.org/10.1093/plcell/koae169, doi:10.1093/plcell/koae169. This article has 28 citations.

21. (naschberger20241.8åresolution pages 1-5): Andreas Naschberger, Quentin Charras, Josef Komenda, Sadanand Gupta, Martin Tichý, Ashraf Al‐Amoudi, Martin Lukeš, Peter Koník, Roman Sobotka, Petr Novák, and Marek Zákopčaník. 1.8 å resolution structure of the cyanobacterial photosystem i assembly intermediate lacking cytoplasmic subunits. Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4640615/v1, doi:10.21203/rs.3.rs-4640615/v1.

22. (naschberger20241.8åresolution pages 5-8): Andreas Naschberger, Quentin Charras, Josef Komenda, Sadanand Gupta, Martin Tichý, Ashraf Al‐Amoudi, Martin Lukeš, Peter Koník, Roman Sobotka, Petr Novák, and Marek Zákopčaník. 1.8 å resolution structure of the cyanobacterial photosystem i assembly intermediate lacking cytoplasmic subunits. Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4640615/v1, doi:10.21203/rs.3.rs-4640615/v1.

23. (nelson2024investigatingthebalance pages 3-5): Nathan Nelson. Investigating the balance between structural conservation and functional flexibility in photosystem i. International Journal of Molecular Sciences, 25:5073, May 2024. URL: https://doi.org/10.3390/ijms25105073, doi:10.3390/ijms25105073. This article has 12 citations.

24. (nelson2024investigatingthebalance pages 1-3): Nathan Nelson. Investigating the balance between structural conservation and functional flexibility in photosystem i. International Journal of Molecular Sciences, 25:5073, May 2024. URL: https://doi.org/10.3390/ijms25105073, doi:10.3390/ijms25105073. This article has 12 citations.

25. (tian2024photosystemiaa pages 7-9): Li-Rong Tian and Jing-Hua Chen. Photosystem i: a paradigm for understanding biological environmental adaptation mechanisms in cyanobacteria and algae. International Journal of Molecular Sciences, 25:8767, Aug 2024. URL: https://doi.org/10.3390/ijms25168767, doi:10.3390/ijms25168767. This article has 7 citations.

26. (ozawa2018configurationoften pages 2-3): Shin-Ichiro Ozawa, Till Bald, Takahito Onishi, Huidan Xue, Takunori Matsumura, Ryota Kubo, Hiroko Takahashi, Michael Hippler, and Yuichiro Takahashi. Configuration of ten light-harvesting chlorophyll a/b complex i subunits in chlamydomonas reinhardtii photosystem i. Plant Physiology, 178:583-595, Aug 2018. URL: https://doi.org/10.1104/pp.18.00749, doi:10.1104/pp.18.00749. This article has 89 citations and is from a highest quality peer-reviewed journal.

27. (ozawa2018configurationoften pages 8-9): Shin-Ichiro Ozawa, Till Bald, Takahito Onishi, Huidan Xue, Takunori Matsumura, Ryota Kubo, Hiroko Takahashi, Michael Hippler, and Yuichiro Takahashi. Configuration of ten light-harvesting chlorophyll a/b complex i subunits in chlamydomonas reinhardtii photosystem i. Plant Physiology, 178:583-595, Aug 2018. URL: https://doi.org/10.1104/pp.18.00749, doi:10.1104/pp.18.00749. This article has 89 citations and is from a highest quality peer-reviewed journal.

28. (fischer1997targetedmutationsin pages 3-4): Nicolas Fischer, Pierre Sétif, and Jean-David Rochaix. Targeted mutations in the psac gene of chlamydomonas reinhardtii: preferential reduction of fb at low temperature is not accompanied by altered electron flow from photosystem i to ferredoxin. Biochemistry, 36 1:93-102, Jan 1997. URL: https://doi.org/10.1021/bi962244v, doi:10.1021/bi962244v. This article has 108 citations and is from a peer-reviewed journal.

29. (meimberg1999lys35ofpsac pages 7-7): Karen Meimberg, Nicolas Fischer, Jean‐David Rochaix, and Ulrich Mühlenhoff. Lys35 of psac is required for the efficient photoreduction of flavodoxin by photosystem i from chlamydomonas reinhardtii. European journal of biochemistry, 263 1:137-44, Jul 1999. URL: https://doi.org/10.1046/j.1432-1327.1999.00474.x, doi:10.1046/j.1432-1327.1999.00474.x. This article has 21 citations.

30. (meimberg1999lys35ofpsac pages 1-2): Karen Meimberg, Nicolas Fischer, Jean‐David Rochaix, and Ulrich Mühlenhoff. Lys35 of psac is required for the efficient photoreduction of flavodoxin by photosystem i from chlamydomonas reinhardtii. European journal of biochemistry, 263 1:137-44, Jul 1999. URL: https://doi.org/10.1046/j.1432-1327.1999.00474.x, doi:10.1046/j.1432-1327.1999.00474.x. This article has 21 citations.

31. (redding1999photosystemiis pages 1-2): Kevin Redding, Laurent Cournac, Ilya R. Vassiliev, John H. Golbeck, Gilles Peltier, and Jean-David Rochaix. Photosystem i is indispensable for photoautotrophic growth, co2 fixation, and h2 photoproduction inchlamydomonas reinhardtii *. The Journal of Biological Chemistry, 274:10466-10473, Apr 1999. URL: https://doi.org/10.1074/jbc.274.15.10466, doi:10.1074/jbc.274.15.10466. This article has 92 citations.

32. (redding1999photosystemiis pages 3-5): Kevin Redding, Laurent Cournac, Ilya R. Vassiliev, John H. Golbeck, Gilles Peltier, and Jean-David Rochaix. Photosystem i is indispensable for photoautotrophic growth, co2 fixation, and h2 photoproduction inchlamydomonas reinhardtii *. The Journal of Biological Chemistry, 274:10466-10473, Apr 1999. URL: https://doi.org/10.1074/jbc.274.15.10466, doi:10.1074/jbc.274.15.10466. This article has 92 citations.

33. (caspy2020thestructureof pages 4-5): Ido Caspy, Anna Borovikova-Sheinker, Daniel Klaiman, Yoel Shkolnisky, and Nathan Nelson. The structure of a triple complex of plant photosystem i with ferredoxin and plastocyanin. Nature Plants, 6:1300-1305, Oct 2020. URL: https://doi.org/10.1038/s41477-020-00779-9, doi:10.1038/s41477-020-00779-9. This article has 79 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](psaC-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000040 Figure 2B on page 5 provides a schematic representation of the Photosystem I (PSI) electron transfer chain. The 'Right side view' e](psaC-deep-research-falcon_artifacts/image-1.png)

## Citations

1. rolo2024structurefunctionand pages 3-4
2. rolo2024structurefunctionand pages 4-5
3. caspy2020thestructureof pages 3-4
4. tian2024photosystemiaa pages 2-4
5. fischer1997targetedmutationsin pages 1-2
6. rochaix2000chloroplastsitedirectedmutagenesis pages 8-9
7. rolo2024structurefunctionand pages 13-14
8. tian2024photosystemiaa pages 7-9
9. redding1999photosystemiis pages 2-3
10. ozawa2018configurationoften pages 1-2
11. ford2019inhibitionoftor pages 16-18
12. ford2019inhibitionoftor pages 14-16
13. redding1999photosystemiis pages 7-8
14. redding1999photosystemiis pages 5-7
15. rochaix2000chloroplastsitedirectedmutagenesis pages 2-3
16. fischer1997targetedmutationsin pages 7-8
17. fischer1997targetedmutationsin pages 8-9
18. nelson2024investigatingthebalance pages 3-5
19. nelson2024investigatingthebalance pages 1-3
20. ozawa2018configurationoften pages 2-3
21. ozawa2018configurationoften pages 8-9
22. fischer1997targetedmutationsin pages 3-4
23. redding1999photosystemiis pages 1-2
24. redding1999photosystemiis pages 3-5
25. caspy2020thestructureof pages 4-5
26. 4Fe–4S
27. Fe4–S4
28. 14C
29. Fe4-S4
30. https://doi.org/10.3390/cells8101171
31. https://doi.org/10.1021/bi962244v
32. https://doi.org/10.1046/j.1432-1327.1999.00474.x
33. https://doi.org/10.1074/jbc.274.15.10466
34. https://doi.org/10.1104/pp.18.00749
35. https://doi.org/10.1038/s41477-020-00779-9
36. https://doi.org/10.1093/plcell/koae169
37. https://doi.org/10.3390/cells8101171,
38. https://doi.org/10.1074/jbc.274.15.10466,
39. https://doi.org/10.1093/plcell/koae169,
40. https://doi.org/10.1016/s0300-9084(00
41. https://doi.org/10.1104/pp.18.00749,
42. https://doi.org/10.1038/s41477-020-00779-9,
43. https://doi.org/10.1021/bi962244v,
44. https://doi.org/10.1046/j.1432-1327.1999.00474.x,
45. https://doi.org/10.3390/ijms25168767,
46. https://doi.org/10.21203/rs.3.rs-4640615/v1,
47. https://doi.org/10.3390/ijms25105073,