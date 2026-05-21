---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-21T13:53:29.756706'
end_time: '2026-05-21T14:12:14.787593'
duration_seconds: 1125.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: POPTR
  gene_id: A9P822
  gene_symbol: METK1
  uniprot_accession: A9P822
  protein_description: 'RecName: Full=S-adenosylmethionine synthase 1; Short=AdoMet
    synthase 1; EC=2.5.1.6 {ECO:0000250|UniProtKB:Q96551}; AltName: Full=Methionine
    adenosyltransferase 1; Short=MAT 1;'
  gene_info: Name=METK1; ORFNames=POPTR_0014s11000g;
  organism_full: Populus trichocarpa (Western balsam poplar) (Populus balsamifera
    subsp. trichocarpa).
  protein_family: Belongs to the AdoMet synthase family. .
  protein_domains: ADOMET_SYNTHASE_CS. (IPR022631); S-AdoMet_synt_C. (IPR022630);
    S-AdoMet_synt_central. (IPR022629); S-AdoMet_synt_N. (IPR022628); S-AdoMet_synthetase.
    (IPR002133)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: METK1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: METK1-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000013 The requested Table 3 and Figure 8 are
    both located on page 9 of the document. Table 3 presents the chemical composition
    of cell wa'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A9P822
- **Protein Description:** RecName: Full=S-adenosylmethionine synthase 1; Short=AdoMet synthase 1; EC=2.5.1.6 {ECO:0000250|UniProtKB:Q96551}; AltName: Full=Methionine adenosyltransferase 1; Short=MAT 1;
- **Gene Information:** Name=METK1; ORFNames=POPTR_0014s11000g;
- **Organism (full):** Populus trichocarpa (Western balsam poplar) (Populus balsamifera subsp. trichocarpa).
- **Protein Family:** Belongs to the AdoMet synthase family. .
- **Key Domains:** ADOMET_SYNTHASE_CS. (IPR022631); S-AdoMet_synt_C. (IPR022630); S-AdoMet_synt_central. (IPR022629); S-AdoMet_synt_N. (IPR022628); S-AdoMet_synthetase. (IPR002133)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "METK1" matches the protein description above**
2. **Verify the organism is correct:** Populus trichocarpa (Western balsam poplar) (Populus balsamifera subsp. trichocarpa).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'METK1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **METK1** (gene ID: A9P822, UniProt: A9P822) in POPTR.

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
- **UniProt Accession:** A9P822
- **Protein Description:** RecName: Full=S-adenosylmethionine synthase 1; Short=AdoMet synthase 1; EC=2.5.1.6 {ECO:0000250|UniProtKB:Q96551}; AltName: Full=Methionine adenosyltransferase 1; Short=MAT 1;
- **Gene Information:** Name=METK1; ORFNames=POPTR_0014s11000g;
- **Organism (full):** Populus trichocarpa (Western balsam poplar) (Populus balsamifera subsp. trichocarpa).
- **Protein Family:** Belongs to the AdoMet synthase family. .
- **Key Domains:** ADOMET_SYNTHASE_CS. (IPR022631); S-AdoMet_synt_C. (IPR022630); S-AdoMet_synt_central. (IPR022629); S-AdoMet_synt_N. (IPR022628); S-AdoMet_synthetase. (IPR002133)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "METK1" matches the protein description above**
2. **Verify the organism is correct:** Populus trichocarpa (Western balsam poplar) (Populus balsamifera subsp. trichocarpa).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'METK1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **METK1** (gene ID: A9P822, UniProt: A9P822) in POPTR.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: Functional annotation of **METK1** (UniProt **A9P822**) from *Populus trichocarpa*

### Executive summary (identity verification and evidence limits)
The target protein is **S-adenosylmethionine synthase 1** (AdoMet/SAM synthase; **methionine adenosyltransferase**, **EC 2.5.1.6**), gene **METK1**, ORF **POPTR_0014s11000g**, from *Populus trichocarpa* (western balsam poplar). In the retrieved literature set, I did **not** find a primary paper that explicitly assays or localizes this specific *Populus trichocarpa* protein (UniProt A9P822) by accession/ORF name. Therefore, the functional annotation below is a **high-confidence orthology/family-based inference** grounded in plant SAMS/MAT literature, supplemented with **direct poplar evidence** that *metK* (SAMS) is transcriptionally responsive under stress and sits in the expected methionine→SAM→ethylene/methylation pathway. (chen2025theyangcycle pages 4-5, feng2022differencesindetoxification pages 6-9)


---

## 1) Key concepts and definitions (current understanding)

### 1.1 What METK1 encodes
**METK1/SAMS/MAT** enzymes catalyze formation of **S-adenosyl-L-methionine (SAM; AdoMet)** from **L-methionine** and **ATP**; SAM is the central activated methyl donor and a precursor for several plant pathways. (chen2025theyangcycle pages 2-3, jockmann2025chemoselectivityofoand pages 26-30)

### 1.2 Primary biochemical function: catalyzed reaction and substrate specificity
**Reaction** (canonical MAT/SAMS):
- **L-methionine + ATP → S-adenosyl-L-methionine (SAM) + pyrophosphate (PPi) + orthophosphate (Pi)**. (jockmann2025chemoselectivityofoand pages 26-30)

**Mechanistic understanding** (general MAT chemistry, applicable to plant homologs):
- MAT binds ATP and L-methionine (requires **Mg2+** and **K+**) and proceeds via an **SN2-type** reaction where methionine sulfur attacks the **5′ carbon** of the ATP ribose; the ATP β–γ bond is hydrolyzed producing **PPi and Pi**. (jockmann2025chemoselectivityofoand pages 26-30)

**Substrate specificity**:
- The defining substrates are **L-methionine** and **ATP**; the principal product is **SAM**. (jockmann2025chemoselectivityofoand pages 26-30)

### 1.3 Why SAM matters in plants (pathway context)
SAM is described in plant-focused reviews as:
- The **universal methyl donor** for methyltransferases, including those involved in **DNA/histone methylation** and **secondary metabolism**. (watanabe2021metabolismandregulatory pages 3-5, chen2025theyangcycle pages 2-3)
- A key precursor feeding biosynthesis of **ethylene** and **polyamines**, and also **nicotianamine/phytosiderophores**. (watanabe2021metabolismandregulatory pages 3-5, chen2025theyangcycle pages 2-3)
- A metabolite whose compartmentalization and recycling (Yang cycle / MTA cycle) influences growth and development. (chen2025theyangcycle pages 4-5, watanabe2021metabolismandregulatory pages 3-5)

### 1.4 Subcellular localization and compartmentation
Plant SAMS is reported to localize primarily to the **cytoplasm and nucleus**. This supports annotating *Populus* METK1 as a **cytosolic/nuclear enzyme** generating SAM for cellular methylation capacity and for distribution to other compartments. (chen2025theyangcycle pages 4-5)

SAM is synthesized in the **cytoplasm**, while methylation reactions in organelles require **SAM transport**. In cotton/Arabidopsis-focused discussion, SAM transporters include plastid- and mitochondria-associated transporters (e.g., AtSAMC1 plastid; AtSAMC2 plastid+mitochondrial membranes). (yang2023rolesofsadenosylmethionine pages 9-11)


---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 2024: Field-scale engineering of SAM pools to modify lignin and biomass processing
A major 2024 development relevant to METK1 functional context is field testing of **SAM depletion** (via heterologous SAM hydrolase “AdoMetase”) in sorghum. This work provides real-world evidence that SAM availability constrains methylation-dependent wall chemistry:
- **Acid-insoluble lignin** decreased **18%** (Davis site) and **13%** (KARE site) in the best engineered line. (tian2024engineeredreductionof pages 8-9, tian2024engineeredreductionof media dafe8723)
- Cell-wall **glucuronic acid methylation** was reduced (reported via changes in GlcA vs 4-O-MeGlcA), consistent with reduced SAM-dependent methylation capacity. (tian2024engineeredreductionof pages 8-9, tian2024engineeredreductionof media dafe8723)
- Biomass saccharification sugar release improved by roughly **~12–24%** depending on site and pretreatment conditions (as shown in the saccharification figure). (tian2024engineeredreductionof pages 8-9, tian2024engineeredreductionof media 23ba5d32)
- However, there were large **yield penalties** (e.g., up to **69% biomass reduction** in one line at one site), indicating that globally reducing SAM can have strong pleiotropic impacts. (tian2024engineeredreductionof pages 8-9)

Although this is not a poplar study and manipulates SAM downstream of SAMS rather than altering METK1 directly, it is among the clearest 2024 demonstrations that SAM supply is rate-limiting for lignin-related methylation and biomass-processing traits in crops—supporting METK1’s inferred importance upstream of these processes. (tian2024engineeredreductionof pages 8-9, tian2024engineeredreductionof media 23ba5d32)

### 2.2 2023: SAM in stress responses and precursor partitioning (ethylene vs polyamines)
A 2023 review focusing on salt tolerance emphasizes that ethylene and polyamines share SAM as a common precursor and discusses SAM synthesis in the cytoplasm with organellar dependence on import. (yang2023rolesofsadenosylmethionine pages 9-11)

### 2.3 2023–2025: Regulatory control of plant SAMS abundance and downstream outcomes
Recent plant synthesis highlights multiple layers of SAMS regulation (phosphorylation and proteasome-mediated turnover) and links SAMS perturbations to developmental outcomes and lignin deposition via regulation of methionine adenosyltransferases. (chen2025theyangcycle pages 5-5, chen2025theyangcycle pages 10-11)


---

## 3) Current applications and real-world implementations

### 3.1 Biomass/cell-wall engineering (bioenergy, pulp, and digestibility)
The 2024 sorghum field trial demonstrates that altering SAM pools can measurably reduce lignin and improve saccharification, a direct route to improved biomass processing; it also highlights the main risk: growth/yield penalties if SAM depletion is not spatially/temporally controlled. (tian2024engineeredreductionof pages 8-9, tian2024engineeredreductionof media 23ba5d32)

### 3.2 Stress physiology and environmental resilience in trees
In poplar varieties exposed to SO2, methionine→SAM metabolism is explicitly placed in the sulfur/methionine response network, and **metK (SAMS)** is reported as **up-regulated** (with ACS) under SO2 fumigation in a resistant cultivar (“Purui”). This supports a real-world role for SAM production capacity in stress-associated metabolic remodeling in poplar. (feng2022differencesindetoxification pages 6-9)

### 3.3 Epigenetic regulation during wood formation
A Populus trichocarpa methylome/transcriptome resource quantified global methylation patterns during the transition from primary to secondary growth, providing context for SAM-demanding methylation processes in developing stems and wood formation. (zhang2020dnamethylationand pages 1-2)


---

## 4) Expert opinions and analysis from authoritative sources (interpretation grounded in reviews)

### 4.1 METK1 is best annotated as a “central metabolic capacity” enzyme
Plant-focused reviews frame SAMS as a “well-studied” Yang-cycle enzyme whose perturbation leads to broad developmental phenotypes and impacts methylation and hormone-related pathways. This implies METK1 is less likely to be a pathway-specific regulator and more likely a **central capacity enzyme** affecting multiple downstream processes via SAM availability. (chen2025theyangcycle pages 4-5, chen2025theyangcycle pages 10-11)

### 4.2 Expected downstream pathways influenced by METK1-derived SAM
Based on synthesis across reviews, the most defensible downstream processes to connect to Populus METK1 are:
- **Transmethylation reactions** (DNA/histone and small-molecule methylation). (watanabe2021metabolismandregulatory pages 3-5, chen2025theyangcycle pages 2-3)
- **Ethylene biosynthesis** (SAM used to produce ACC; methionine salvage/Yang cycle coupled to ethylene-associated turnover). (chen2025theyangcycle pages 11-11, feng2022differencesindetoxification pages 6-9)
- **Polyamine metabolism** (SAM is a precursor in polyamine biosynthesis; shared precursor logic affects stress responses). (watanabe2021metabolismandregulatory pages 3-5, yang2023rolesofsadenosylmethionine pages 9-11)
- **Lignin and cell-wall methylation chemistry**, because lignin monomer methylation depends on SAM and SAM-dependent O-methyltransferases; perturbations in SAM metabolism can reduce lignin and alter wall methylation. (chen2025theyangcycle pages 2-3, tian2024engineeredreductionof pages 8-9)

### 4.3 Cellular localization: cytosolic production with nuclear adjacency
Because plant SAMS is reported in the cytoplasm and nucleus, METK1 can be functionally interpreted as supporting (i) cytosolic methylation-dependent metabolism and (ii) nuclear methylation capacity (chromatin-associated methylation) while indirectly supplying SAM to organelles via transporters. (chen2025theyangcycle pages 4-5, yang2023rolesofsadenosylmethionine pages 9-11)


---

## 5) Relevant statistics and data from recent studies

### 5.1 Populus trichocarpa stem methylation levels during development
During primary-to-secondary growth in *P. trichocarpa* stems, whole-genome bisulfite sequencing found average methylation levels of approximately:
- **CG ~53.6%**, **CHG ~37.7%**, and **CHH ~8.5%** (genome-wide averages), with statistically significant differences among developmental stages. (zhang2020dnamethylationand pages 1-2)

These data are relevant to METK1 because methylation marks (5mC) depend on SAM supply as methyl donor, linking methylome maintenance and remodeling to cellular methylation capacity. (watanabe2021metabolismandregulatory pages 3-5, zhang2020dnamethylationand pages 1-2)

### 5.2 Poplar stress physiology: SO2 responses connected to metK/SAMS
In *Populus × euramericana* varieties exposed to SO2, the resistant cultivar showed substantial increases in sulfur-assimilation enzyme activities (e.g., increases reported on the order of ~27–54% depending on enzyme) and increased Cys/GSH under fumigation, and the pathway schematic and results state that **Met is partly converted into SAM by metK** and that **metK** is **up-regulated** under SO2 fumigation (with ACS, linking SAM to ethylene precursor ACC). (feng2022differencesindetoxification pages 6-9)

### 5.3 2024 field trial manipulating SAM pools (quantitative wall chemistry and performance)
From the 2024 sorghum AdoMetase field trial:
- **Acid-insoluble lignin** reduced by **18%** and **13%** (best line, different sites). (tian2024engineeredreductionof pages 8-9, tian2024engineeredreductionof media dafe8723)
- **Sugar release** after pretreatment + enzymatic digestion increased by roughly **~12–24%** depending on conditions (figure). (tian2024engineeredreductionof media 23ba5d32)
- **Biomass yield** penalties up to **69%** (site/line dependent). (tian2024engineeredreductionof pages 8-9)


---

## Functional annotation statement for Populus METK1 (UniProt A9P822)

**Recommended primary function annotation:** METK1 (UniProt A9P822) is a **S-adenosyl-L-methionine synthase (methionine adenosyltransferase; EC 2.5.1.6)** catalyzing **L-methionine + ATP → SAM + PPi + Pi** in the **cytoplasm and nucleus**, thereby supplying SAM for cellular **transmethylation reactions** and as a precursor feeding **ethylene** and **polyamine** biosynthesis; through SAM availability it can indirectly influence **lignin/cell-wall methylation chemistry** and methylation-associated regulation during wood formation and stress responses in poplar. (jockmann2025chemoselectivityofoand pages 26-30, chen2025theyangcycle pages 4-5, feng2022differencesindetoxification pages 6-9, tian2024engineeredreductionof pages 8-9)


---

## Summary table
| Topic | Key points (concise) | Evidence/source (include paper title + year + URL) | Notes/limits |
|---|---|---|---|
| Target identity / ambiguity check | UniProt A9P822 is annotated as **S-adenosylmethionine synthase 1 / methionine adenosyltransferase 1 (EC 2.5.1.6)** from **Populus trichocarpa**, gene **METK1 / POPTR_0014s11000g**. Literature directly naming this exact poplar gene is sparse; functional annotation therefore relies mainly on conserved plant **SAMS/MAT** biology. | *The Yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes* (2025), https://doi.org/10.48130/ph-0025-0007; *Metabolism and Regulatory Functions of O-Acetylserine, S-Adenosylmethionine, Homocysteine, and Serine in Plant Development and Environmental Responses* (2021), https://doi.org/10.3389/fpls.2021.643403 (chen2025theyangcycle pages 2-3, chen2025theyangcycle pages 4-5, watanabe2021metabolismandregulatory pages 3-5) | No Populus-specific biochemical paper for A9P822 was retrieved in the available evidence set; conclusions are inference-based but strongly supported by family conservation. |
| Enzyme reaction / substrates / products / mechanism | Plant MAT/SAMS catalyzes **L-methionine + ATP → S-adenosyl-L-methionine (SAM/AdoMet) + PPi + Pi**. Mechanistically, methionine sulfur attacks the 5′ carbon of ATP ribose in an **SN2-type** reaction; enzyme activity requires **Mg2+ and K+**, with active oligomers described as homo-dimer/tetramer and loop closure during catalysis. | *Chemoselectivity of O- and N-Methyltransferases* (2025), URL not clearly available in retrieved record; plant context in *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007 (jockmann2025chemoselectivityofoand pages 26-30, chen2025theyangcycle pages 2-3) | Mechanistic detail comes from general MAT literature, not a Populus enzyme assay. Still appropriate for A9P822 because UniProt places it in the canonical AdoMet synthase family. |
| Primary biochemical function of METK1 | The primary function inferred for Populus METK1 is to make **SAM**, the central activated methyl donor and branch-point metabolite feeding methylation chemistry plus ethylene/polyamine-related metabolism. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007; *Metabolism and Regulatory Functions of O-Acetylserine...* (2021), https://doi.org/10.3389/fpls.2021.643403 (chen2025theyangcycle pages 2-3, watanabe2021metabolismandregulatory pages 3-5) | This is the most defensible direct annotation for A9P822. |
| SAM as methyl donor | SAM is the **universal methyl donor** for many plant methyltransferases, including reactions affecting **DNA/histone methylation**, RNA/protein methylation, and secondary metabolism. Thus METK1 likely supports epigenetic regulation and broad methylation capacity. | *Metabolism and Regulatory Functions of O-Acetylserine...* (2021), https://doi.org/10.3389/fpls.2021.643403; *Roles of S-Adenosylmethionine and Its Derivatives in Salt Tolerance of Cotton* (2023), https://doi.org/10.3390/ijms24119517; *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007 (watanabe2021metabolismandregulatory pages 3-5, yang2023rolesofsadenosylmethionine pages 9-11, chen2025theyangcycle pages 2-3) | For Populus, this implies a likely role in chromatin methylation and methyl-dependent metabolism, but gene-specific methylome data were not retrieved. |
| Lignin-related role | SAM is required by **O-methyltransferases** in lignin biosynthesis; perturbing SAM/SAMS can reduce lignin. A cited Arabidopsis **sams3** mutation decreased lignin, and proteolytic regulation of methionine adenosyltransferases can affect lignin deposition. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007 (chen2025theyangcycle pages 10-11, chen2025theyangcycle pages 2-3) | This supports annotating Populus METK1 as an upstream contributor to wood-cell-wall methylation and lignification, but not as a lignin-pathway enzyme per se. |
| Ethylene pathway connection | SAM is the immediate precursor used to make **ACC**, the precursor of **ethylene**; therefore METK1 likely influences ethylene biosynthetic capacity indirectly by supplying SAM. MTA/Methionine salvage cycle coupling links SAM turnover to ethylene production. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007; *Roles of S-Adenosylmethionine and Its Derivatives in Salt Tolerance of Cotton* (2023), https://doi.org/10.3390/ijms24119517 (chen2025theyangcycle pages 11-11, chen2025theyangcycle pages 5-5, yang2023rolesofsadenosylmethionine pages 9-11) | No direct Populus METK1–ethylene experiment was retrieved. |
| Polyamine pathway connection | SAM is also a precursor for **polyamine biosynthesis** (via decarboxylated SAM in downstream steps). Reviews note ethylene and polyamines share SAM as a common precursor, placing METK1 at a key metabolic branch point. | *Metabolism and Regulatory Functions of O-Acetylserine...* (2021), https://doi.org/10.3389/fpls.2021.643403; *Roles of S-Adenosylmethionine and Its Derivatives in Salt Tolerance of Cotton* (2023), https://doi.org/10.3390/ijms24119517 (watanabe2021metabolismandregulatory pages 3-5, yang2023rolesofsadenosylmethionine pages 9-11) | Annotation is pathway-level; substrate specificity of METK1 itself is methionine + ATP, not polyamines. |
| Other SAM-dependent pathways | SAM also feeds biosynthesis of **nicotianamine/phytosiderophores** and methylation of compounds such as **flavonoids** and cell-wall-associated metabolites. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007; *Metabolism and Regulatory Functions of O-Acetylserine...* (2021), https://doi.org/10.3389/fpls.2021.643403 (chen2025theyangcycle pages 2-3, watanabe2021metabolismandregulatory pages 3-5) | Broad systems role; not evidence of unique specialization of METK1 over other SAMS paralogs. |
| Subcellular localization of SAMS/METK protein | Plant SAMS is reported to localize in the **cytoplasm and nucleus**. This is the best-supported localization inference for Populus METK1. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007 (chen2025theyangcycle pages 4-5) | No Populus A9P822 localization experiment was retrieved; localization inferred from plant ortholog studies. |
| SAM transport / compartmentation | Although SAM is synthesized in the **cytoplasm**, organelles need imported SAM for methylation reactions. Arabidopsis **AtSAMC1** localizes to plastids and **AtSAMC2** to plastid + mitochondrial membranes; Golgi-localized SAM transporters also affect cell-wall architecture and morphology. | *Roles of S-Adenosylmethionine and Its Derivatives in Salt Tolerance of Cotton* (2023), https://doi.org/10.3390/ijms24119517; *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007 (yang2023rolesofsadenosylmethionine pages 9-11, chen2025theyangcycle pages 2-3) | This does **not** mean METK1 itself is membrane-localized; rather, it supports the annotation that METK1-generated SAM is distributed to other compartments. |
| Biological process inference for Populus | By family function, Populus METK1 most plausibly participates in **methionine/SAM metabolism**, **methylation-dependent regulation**, and indirect control of **ethylene, polyamine, and lignin-related processes**, all central to growth, development, and stress responses in plants. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007; *Metabolism and Regulatory Functions of O-Acetylserine...* (2021), https://doi.org/10.3389/fpls.2021.643403 (chen2025theyangcycle pages 4-5, chen2025theyangcycle pages 10-11, watanabe2021metabolismandregulatory pages 3-5) | Appropriate for functional annotation; should be labeled as inference unless Populus-specific validation becomes available. |
| Regulation (post-translational) | Plant SAMS proteins are post-translationally regulated, including **phosphorylation** and **26S proteasome-mediated degradation**. Examples include regulation by **CDPK/CPK kinases** and proteins such as **OsWAK112**, **OsLCD3**, and **OsFBK12**, with consequences for ethylene/polyamine balance and development. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007 (chen2025theyangcycle pages 5-5, chen2025theyangcycle pages 10-11) | Specific regulators are from rice/cucumber/tomato studies, not Populus. |
| Developmental / stress evidence from plants | Altering SAMS affects flowering, grain size, pollen tube growth, fruit ripening, and tolerance to cold/drought/salt in multiple plants. These phenotypes support the view that METK1 is a central metabolic control point rather than a pathway-specific enzyme. | *The Yang cycle in plants* (2025), https://doi.org/10.48130/ph-0025-0007 (chen2025theyangcycle pages 4-5, chen2025theyangcycle pages 10-11, chen2025theyangcycle pages 5-5) | Indirect evidence for poplar; useful for hypothesis generation in woody tissues and stress biology. |
| Quantitative engineering evidence when SAM is reduced (2024 sorghum AdoMetase study) | Lowering SAM in sorghum by expressing **AdoMetase** reduced **acid-insoluble lignin by 18% and 13%** in line #1 at two field sites; biomass saccharification improved by about **~12–24%** depending on site/pretreatment; biomass yield penalties were substantial: **69% reduction** for line #1 and **49%** for line #3 at one site, and about **23% less biomass** for both lines at the other site. | *Engineered reduction of S-adenosylmethionine alters lignin in sorghum* (2024), https://doi.org/10.1186/s13068-024-02572-8 (tian2024engineeredreductionof pages 8-9, tian2024engineeredreductionof pages 11-12, tian2024engineeredreductionof media dafe8723, tian2024engineeredreductionof media 23ba5d32) | Not a Populus study and it manipulates SAM levels downstream of SAMS rather than METK1 directly, but it gives strong real-world evidence that SAM supply strongly constrains lignin methylation and biomass processing traits. |
| Practical annotation statement for A9P822 | **Recommended functional annotation:** cytosolic/nuclear **S-adenosylmethionine synthase** that converts methionine and ATP to SAM, thereby supplying methyl donor capacity and precursors for ethylene/polyamine-associated metabolism; likely important for methylation status, cell-wall/lignin methylation, and stress/developmental responses in Populus. | Synthesized from plant SAMS/MAT literature above (chen2025theyangcycle pages 2-3, chen2025theyangcycle pages 4-5, chen2025theyangcycle pages 10-11, jockmann2025chemoselectivityofoand pages 26-30, watanabe2021metabolismandregulatory pages 3-5, yang2023rolesofsadenosylmethionine pages 9-11) | Best current evidence supports a high-confidence enzyme-function annotation but only moderate confidence for Populus-specific biological specialization. |


*Table: This table summarizes the most defensible functional annotation for Populus trichocarpa METK1 (UniProt A9P822) based on conserved plant SAMS/MAT literature. It highlights catalytic function, localization, pathway context, regulation, and quantitative evidence showing how SAM perturbation affects lignin and biomass traits.*


---

## Key references (publication date, URL)
- Feng J. et al. **Sep 2022**. *Differences in detoxification mechanism and gene expression changes of sulfur metabolism in coping with the air pollutant SO2 between the resistant and ordinary poplar variety.* Acta Physiologiae Plantarum. https://doi.org/10.1007/s11738-022-03442-2 (feng2022differencesindetoxification pages 6-9)
- Zhang Y. et al. **Jul 2020**. *DNA methylation and its effects on gene expression during primary to secondary growth in poplar stems.* BMC Genomics. https://doi.org/10.1186/s12864-020-06902-6 (zhang2020dnamethylationand pages 1-2)
- Watanabe M. et al. **May 2021**. *Metabolism and Regulatory Functions of O-Acetylserine, S-Adenosylmethionine, Homocysteine, and Serine in Plant Development and Environmental Responses.* Frontiers in Plant Science. https://doi.org/10.3389/fpls.2021.643403 (watanabe2021metabolismandregulatory pages 3-5)
- Yang L. et al. **May 2023**. *Roles of S-Adenosylmethionine and Its Derivatives in Salt Tolerance of Cotton.* Int. J. Mol. Sci. https://doi.org/10.3390/ijms24119517 (yang2023rolesofsadenosylmethionine pages 9-11)
- Tian Y. et al. **Oct 2024**. *Engineered reduction of S-adenosylmethionine alters lignin in sorghum.* Biotechnology for Biofuels and Bioproducts. https://doi.org/10.1186/s13068-024-02572-8 (tian2024engineeredreductionof pages 8-9)
- Chen H. et al. **Jan 2025**. *The Yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes.* Plant Hormones. https://doi.org/10.48130/ph-0025-0007 (chen2025theyangcycle pages 4-5)



References

1. (chen2025theyangcycle pages 4-5): Huixin Chen, Ziyi Zhao, Jiawen Chen, Jana Mertens, Bram Van de Poel, Dongdong Li, and Kunsong Chen. The yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes. Plant Hormones, 1:0-0, Jan 2025. URL: https://doi.org/10.48130/ph-0025-0007, doi:10.48130/ph-0025-0007. This article has 8 citations.

2. (feng2022differencesindetoxification pages 6-9): Jinxia Feng, Luyi Wang, Wenxin Liu, Xianchong Wan, Zhicheng Chen, and Jiaping Zhao. Differences in detoxification mechanism and gene expression changes of sulfur metabolism in coping with the air pollutant so2 between the resistant and ordinary poplar variety. Acta Physiologiae Plantarum, Sep 2022. URL: https://doi.org/10.1007/s11738-022-03442-2, doi:10.1007/s11738-022-03442-2. This article has 2 citations and is from a peer-reviewed journal.

3. (chen2025theyangcycle pages 2-3): Huixin Chen, Ziyi Zhao, Jiawen Chen, Jana Mertens, Bram Van de Poel, Dongdong Li, and Kunsong Chen. The yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes. Plant Hormones, 1:0-0, Jan 2025. URL: https://doi.org/10.48130/ph-0025-0007, doi:10.48130/ph-0025-0007. This article has 8 citations.

4. (jockmann2025chemoselectivityofoand pages 26-30): E Jockmann. Chemoselectivity of o-and n-methyltransferases. Unknown journal, 2025.

5. (watanabe2021metabolismandregulatory pages 3-5): Mutsumi Watanabe, Yukako Chiba, and Masami Yokota Hirai. Metabolism and regulatory functions of o-acetylserine, s-adenosylmethionine, homocysteine, and serine in plant development and environmental responses. Frontiers in Plant Science, May 2021. URL: https://doi.org/10.3389/fpls.2021.643403, doi:10.3389/fpls.2021.643403. This article has 96 citations.

6. (yang2023rolesofsadenosylmethionine pages 9-11): Li Yang, Xingxing Wang, Fuyong Zhao, Xianliang Zhang, Wei Li, Junsen Huang, Xiaoyu Pei, Xiang Ren, Yangai Liu, Kunlun He, Fei Zhang, Xiongfeng Ma, and Daigang Yang. Roles of s-adenosylmethionine and its derivatives in salt tolerance of cotton. International Journal of Molecular Sciences, 24:9517, May 2023. URL: https://doi.org/10.3390/ijms24119517, doi:10.3390/ijms24119517. This article has 21 citations.

7. (tian2024engineeredreductionof pages 8-9): Yang Tian, Yu Gao, Halbay Turumtay, Emine Akyuz Turumtay, Yen Ning Chai, Hemant Choudhary, Joon-Hyun Park, Chuan-Yin Wu, Christopher M. De Ben, Jutta Dalton, Katherine B. Louie, Thomas Harwood, Dylan Chin, Khanh M. Vuu, Benjamin P. Bowen, Patrick M. Shih, Edward E. K. Baidoo, Trent R. Northen, Blake A. Simmons, Robert Hutmacher, Jackie Atim, Daniel H. Putnam, Corinne D. Scown, Jenny C. Mortimer, Henrik V. Scheller, and Aymerick Eudes. Engineered reduction of s-adenosylmethionine alters lignin in sorghum. Biotechnology for Biofuels and Bioproducts, Oct 2024. URL: https://doi.org/10.1186/s13068-024-02572-8, doi:10.1186/s13068-024-02572-8. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (tian2024engineeredreductionof media dafe8723): Yang Tian, Yu Gao, Halbay Turumtay, Emine Akyuz Turumtay, Yen Ning Chai, Hemant Choudhary, Joon-Hyun Park, Chuan-Yin Wu, Christopher M. De Ben, Jutta Dalton, Katherine B. Louie, Thomas Harwood, Dylan Chin, Khanh M. Vuu, Benjamin P. Bowen, Patrick M. Shih, Edward E. K. Baidoo, Trent R. Northen, Blake A. Simmons, Robert Hutmacher, Jackie Atim, Daniel H. Putnam, Corinne D. Scown, Jenny C. Mortimer, Henrik V. Scheller, and Aymerick Eudes. Engineered reduction of s-adenosylmethionine alters lignin in sorghum. Biotechnology for Biofuels and Bioproducts, Oct 2024. URL: https://doi.org/10.1186/s13068-024-02572-8, doi:10.1186/s13068-024-02572-8. This article has 7 citations and is from a domain leading peer-reviewed journal.

9. (tian2024engineeredreductionof media 23ba5d32): Yang Tian, Yu Gao, Halbay Turumtay, Emine Akyuz Turumtay, Yen Ning Chai, Hemant Choudhary, Joon-Hyun Park, Chuan-Yin Wu, Christopher M. De Ben, Jutta Dalton, Katherine B. Louie, Thomas Harwood, Dylan Chin, Khanh M. Vuu, Benjamin P. Bowen, Patrick M. Shih, Edward E. K. Baidoo, Trent R. Northen, Blake A. Simmons, Robert Hutmacher, Jackie Atim, Daniel H. Putnam, Corinne D. Scown, Jenny C. Mortimer, Henrik V. Scheller, and Aymerick Eudes. Engineered reduction of s-adenosylmethionine alters lignin in sorghum. Biotechnology for Biofuels and Bioproducts, Oct 2024. URL: https://doi.org/10.1186/s13068-024-02572-8, doi:10.1186/s13068-024-02572-8. This article has 7 citations and is from a domain leading peer-reviewed journal.

10. (chen2025theyangcycle pages 5-5): Huixin Chen, Ziyi Zhao, Jiawen Chen, Jana Mertens, Bram Van de Poel, Dongdong Li, and Kunsong Chen. The yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes. Plant Hormones, 1:0-0, Jan 2025. URL: https://doi.org/10.48130/ph-0025-0007, doi:10.48130/ph-0025-0007. This article has 8 citations.

11. (chen2025theyangcycle pages 10-11): Huixin Chen, Ziyi Zhao, Jiawen Chen, Jana Mertens, Bram Van de Poel, Dongdong Li, and Kunsong Chen. The yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes. Plant Hormones, 1:0-0, Jan 2025. URL: https://doi.org/10.48130/ph-0025-0007, doi:10.48130/ph-0025-0007. This article has 8 citations.

12. (zhang2020dnamethylationand pages 1-2): Yang Zhang, Cong Liu, He Cheng, Shuanghui Tian, Yingying Liu, Shuang Wang, Huaxin Zhang, Muhammad Saqib, Hairong Wei, and Zhigang Wei. Dna methylation and its effects on gene expression during primary to secondary growth in poplar stems. BMC Genomics, Jul 2020. URL: https://doi.org/10.1186/s12864-020-06902-6, doi:10.1186/s12864-020-06902-6. This article has 52 citations and is from a peer-reviewed journal.

13. (chen2025theyangcycle pages 11-11): Huixin Chen, Ziyi Zhao, Jiawen Chen, Jana Mertens, Bram Van de Poel, Dongdong Li, and Kunsong Chen. The yang cycle in plants: a journey of methionine recycling with fascinating metabolites and enzymes. Plant Hormones, 1:0-0, Jan 2025. URL: https://doi.org/10.48130/ph-0025-0007, doi:10.48130/ph-0025-0007. This article has 8 citations.

14. (tian2024engineeredreductionof pages 11-12): Yang Tian, Yu Gao, Halbay Turumtay, Emine Akyuz Turumtay, Yen Ning Chai, Hemant Choudhary, Joon-Hyun Park, Chuan-Yin Wu, Christopher M. De Ben, Jutta Dalton, Katherine B. Louie, Thomas Harwood, Dylan Chin, Khanh M. Vuu, Benjamin P. Bowen, Patrick M. Shih, Edward E. K. Baidoo, Trent R. Northen, Blake A. Simmons, Robert Hutmacher, Jackie Atim, Daniel H. Putnam, Corinne D. Scown, Jenny C. Mortimer, Henrik V. Scheller, and Aymerick Eudes. Engineered reduction of s-adenosylmethionine alters lignin in sorghum. Biotechnology for Biofuels and Bioproducts, Oct 2024. URL: https://doi.org/10.1186/s13068-024-02572-8, doi:10.1186/s13068-024-02572-8. This article has 7 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](METK1-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000013 The requested Table 3 and Figure 8 are both located on page 9 of the document. Table 3 presents the chemical composition of cell wa](METK1-deep-research-falcon_artifacts/image-1.png)

## Citations

1. jockmann2025chemoselectivityofoand pages 26-30
2. chen2025theyangcycle pages 4-5
3. yang2023rolesofsadenosylmethionine pages 9-11
4. tian2024engineeredreductionof pages 8-9
5. feng2022differencesindetoxification pages 6-9
6. zhang2020dnamethylationand pages 1-2
7. watanabe2021metabolismandregulatory pages 3-5
8. chen2025theyangcycle pages 2-3
9. chen2025theyangcycle pages 5-5
10. chen2025theyangcycle pages 10-11
11. chen2025theyangcycle pages 11-11
12. tian2024engineeredreductionof pages 11-12
13. https://doi.org/10.48130/ph-0025-0007;
14. https://doi.org/10.3389/fpls.2021.643403
15. https://doi.org/10.48130/ph-0025-0007
16. https://doi.org/10.3389/fpls.2021.643403;
17. https://doi.org/10.3390/ijms24119517;
18. https://doi.org/10.3390/ijms24119517
19. https://doi.org/10.1186/s13068-024-02572-8
20. https://doi.org/10.1007/s11738-022-03442-2
21. https://doi.org/10.1186/s12864-020-06902-6
22. https://doi.org/10.48130/ph-0025-0007,
23. https://doi.org/10.1007/s11738-022-03442-2,
24. https://doi.org/10.3389/fpls.2021.643403,
25. https://doi.org/10.3390/ijms24119517,
26. https://doi.org/10.1186/s13068-024-02572-8,
27. https://doi.org/10.1186/s12864-020-06902-6,