---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-21T13:53:39.162366'
end_time: '2026-03-21T13:59:23.501810'
duration_seconds: 344.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: zwf
  gene_symbol: zwf
  uniprot_accession: Q88C32
  protein_description: 'RecName: Full=Glucose-6-phosphate 1-dehydrogenase {ECO:0000256|HAMAP-Rule:MF_00966};
    Short=G6PD {ECO:0000256|HAMAP-Rule:MF_00966}; EC=1.1.1.49 {ECO:0000256|HAMAP-Rule:MF_00966};'
  gene_info: Name=zwf {ECO:0000256|HAMAP-Rule:MF_00966, ECO:0000313|EMBL:AAN70916.1};
    OrderedLocusNames=PP_5351 {ECO:0000313|EMBL:AAN70916.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glucose-6-phosphate dehydrogenase family.
  protein_domains: G6P_DH. (IPR001282); G6P_DH_AS. (IPR019796); G6P_DH_C. (IPR022675);
    G6P_DH_NAD-bd. (IPR022674); NAD(P)-bd_dom_sf. (IPR036291)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88C32
- **Protein Description:** RecName: Full=Glucose-6-phosphate 1-dehydrogenase {ECO:0000256|HAMAP-Rule:MF_00966}; Short=G6PD {ECO:0000256|HAMAP-Rule:MF_00966}; EC=1.1.1.49 {ECO:0000256|HAMAP-Rule:MF_00966};
- **Gene Information:** Name=zwf {ECO:0000256|HAMAP-Rule:MF_00966, ECO:0000313|EMBL:AAN70916.1}; OrderedLocusNames=PP_5351 {ECO:0000313|EMBL:AAN70916.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glucose-6-phosphate dehydrogenase family.
- **Key Domains:** G6P_DH. (IPR001282); G6P_DH_AS. (IPR019796); G6P_DH_C. (IPR022675); G6P_DH_NAD-bd. (IPR022674); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "zwf" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'zwf' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **zwf** (gene ID: zwf, UniProt: Q88C32) in PSEPK.

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
- **UniProt Accession:** Q88C32
- **Protein Description:** RecName: Full=Glucose-6-phosphate 1-dehydrogenase {ECO:0000256|HAMAP-Rule:MF_00966}; Short=G6PD {ECO:0000256|HAMAP-Rule:MF_00966}; EC=1.1.1.49 {ECO:0000256|HAMAP-Rule:MF_00966};
- **Gene Information:** Name=zwf {ECO:0000256|HAMAP-Rule:MF_00966, ECO:0000313|EMBL:AAN70916.1}; OrderedLocusNames=PP_5351 {ECO:0000313|EMBL:AAN70916.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glucose-6-phosphate dehydrogenase family.
- **Key Domains:** G6P_DH. (IPR001282); G6P_DH_AS. (IPR019796); G6P_DH_C. (IPR022675); G6P_DH_NAD-bd. (IPR022674); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "zwf" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'zwf' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **zwf** (gene ID: zwf, UniProt: Q88C32) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research report: functional annotation of **zwf (PP_5351; UniProt Q88C32)** in *Pseudomonas putida* KT2440

### 0) Target verification (mandatory disambiguation)
The UniProt accession **Q88C32** corresponds to the *P. putida* KT2440 locus **PP_5351**, which is one of three glucose-6-phosphate dehydrogenase (G6PDH) paralogs in this strain (often referred to as **zwfC / zwf-3** in the literature). In KT2440, the three G6PDH genes are **zwfA (PP_1022)**, **zwfB (PP_4042)**, and **zwfC (PP_5351)**, and the connecting point between ED and (partial) EMP metabolism is the G6PDH reaction catalyzed by these isozymes. (volke2021cofactorspecificityof pages 2-4, nikel2015pseudomonasputidakt2440 pages 21-25)

Accordingly, this report is specifically about **zwfC = PP_5351 = UniProt Q88C32**, while also summarizing how this paralog relates to the better-studied **zwfA/zwfB** system that dominates glycolytic physiology in KT2440. (volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 7-9)

### 1) Key concepts and definitions (current understanding)

#### 1.1 Enzymatic function and reaction chemistry
**Glucose-6-phosphate dehydrogenase (G6PDH; EC 1.1.1.49)** catalyzes the first committed step of the **oxidative pentose phosphate (PP) pathway** and also supplies carbon into the **Entner–Doudoroff (ED) pathway** via 6-phosphogluconate. In *P. putida* KT2440, the zwf-1 product is described as required to convert **glucose-6-phosphate (G6P) to 6-phosphogluconolactone** with reduction of NAD(P)+ to NAD(P)H (reported in the context of zwf-1 as the major isozyme). (kim2008dualregulationof pages 4-6)

A standard biochemical description of the reaction is:
- **D-glucose-6-phosphate + NAD(P)+ → 6-phospho-D-glucono-δ-lactone + NAD(P)H + H+**

Because NAD(P)H (often predominantly **NADPH**) supports biosynthesis and oxidative-stress defense (e.g., via glutathione reduction), Zwf enzymes are central determinants of **redox balance** in KT2440. (volke2021cofactorspecificityof pages 1-2, i.2021reconfigurationofmetabolic pages 8-10)

#### 1.2 Pathway context in *P. putida*: ED–EMP–PP “EDEMP cycle”
A key concept for KT2440 is that glucose catabolism is organized as an interconnected network (often called the **EDEMP cycle**) that merges the ED pathway with a gluconeogenic operation of (incomplete) EMP and PP pathway reactions to tune precursor supply and **NADPH formation**. (nikel2015pseudomonasputidakt2440 pages 1-2, volke2021cofactorspecificityof pages 2-4)

This network architecture is directly relevant to zwf paralogs because G6PDH activity sits at the connection between ED and EMP/PP routing, and can be rate- and redox-controlling. (volke2021cofactorspecificityof pages 2-4)

#### 1.3 Isozyme multiplicity and cofactor specificity
Unlike the “default” assumption (from *E. coli*) that bacterial G6PDH is strictly NADP+-specific, KT2440 encodes **three** G6PDH isozymes with **distinct cofactor preferences and kinetic behaviors**, interpreted as an evolutionary/physiological strategy to balance **NADPH vs NADH** production depending on carbon source and redox state. (volke2021cofactorspecificityof pages 1-2, volke2021cofactorspecificityof pages 7-9)

### 2) Gene product-specific functional annotation: **ZwfC (PP_5351; UniProt Q88C32)**

#### 2.1 Molecular function
ZwfC is a **G6PDH-family enzyme** (glucose-6-phosphate dehydrogenase isozyme C) that conserves canonical G6PDH sequence motifs for cofactor and substrate binding. (volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 7-9)

**Cofactor specificity and kinetics (isozyme-level):** ZwfC/G6PDH-C is described as **highly NADP+-specific**, with a specificity coefficient ω reported to be ~5× higher than the canonical *E. coli* enzyme’s ω (~410), but with **very low turnover** (reported **kcat < 1 s−1**), consistent with low physiological contribution under tested conditions. (volke2021cofactorspecificityof pages 7-9)

#### 2.2 Biological process and pathway role
Although ZwfC is a bona fide G6PDH, multiple lines of evidence indicate that in KT2440 it contributes **little** to bulk glucose catabolism in standard laboratory conditions:
- **Transcription is very low**: reporter constructs for the zwfC promoter/5′UTR showed **almost no detectable expression** across tested carbon sources. (volke2021cofactorspecificityof pages 9-11)
- **Phenotype is minimal**: deletion of zwfC alone produced **no significant growth phenotype** in the tested substrate panel (whereas zwfA loss severely affects growth on glucose). (volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 2-4)

Thus, the most defensible functional statement from current evidence is that **ZwfC encodes an NADP+-specific G6PDH isozyme with low expression and low catalytic turnover, likely acting as a condition-dependent or auxiliary redox enzyme rather than the primary entry point for glycolytic carbon** in KT2440. (volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 7-9)

#### 2.3 Cellular localization
Direct subcellular localization measurements for ZwfC were not identified in the retrieved evidence. However, the pathway context and enzyme assays described for KT2440 focus on cytoplasmic sugar phosphorylation and intracellular flux through the ED/PP network connected by G6PDHs, consistent with Zwf isozymes functioning as **intracellular (cytosolic) dehydrogenases** acting on G6P. This should be treated as pathway-based inference rather than a direct localization experiment. (volke2021cofactorspecificityof pages 2-4, kim2008dualregulationof pages 4-6)

### 3) Regulation and control (KT2440-specific)

#### 3.1 HexR as a major transcriptional regulator of zwf in KT2440
For the major zwf gene (historically “zwf-1”), the transcription factor **HexR** acts as a **repressor**: zwf promoter activity in glucose or gluconate is reported to be **25–50-fold higher** than in pyruvate/succinate, and HexR knockout yields constitutively high reporter signal across conditions. (kim2008dualregulationof pages 4-6)

Mechanistically, **KDPG (2-keto-3-deoxy-6-phosphogluconate)**—a key ED intermediate—acts as an inducer by **blocking HexR binding** to the zwf promoter region; this is supported by EMSA and by edd/eda mutants that modulate intracellular KDPG (edd cannot make KDPG; eda accumulates KDPG). (kim2008dualregulationof pages 6-7)

For **zwfC (PP_5351)** specifically, upstream sequence analysis reported a HexR binding motif, but **functional reporter assays still detected almost no zwfC expression** under the conditions tested, implying that (i) zwfC is under tighter/alternative regulation, (ii) it may require specific inducing conditions not present in the tested set, or (iii) it is effectively silent in many standard regimes. (volke2021cofactorspecificityof pages 9-11)

#### 3.2 Oxidative-stress induction and physiological relevance
Oxidative stress strongly increases the cellular need for NADPH. In KT2440, network-level 13C flux analysis under sublethal H2O2 showed that periplasmic glucose processing is rerouted toward **cytoplasmic oxidation** and a cyclic PP operation, generating NADPH fluxes that **exceed biosynthetic demands by ~50%**. (i.2021reconfigurationofmetabolic pages 1-2)

Quantitatively, net NADPH generation under oxidative stress is reported to increase to **14.4 ± 0.3 mmol gCDW−1 h−1**, producing ~50% NADPH surplus relative to biosynthetic requirements. (i.2021reconfigurationofmetabolic pages 8-10)

In vitro enzyme assays support this metabolic reconfiguration: under H2O2, specific activities of the two major NADPH-generating dehydrogenases in the PP-related network increased strongly, with **Zwf activity increasing 4.7-fold** (and GntZ 9.2-fold). (i.2021reconfigurationofmetabolic pages 8-10)

These results establish Zwf-linked metabolism as a key, rapidly tunable NADPH supply route under redox stress, even if the evidence does not isolate ZwfC’s specific contribution (given its low expression/activity). (i.2021reconfigurationofmetabolic pages 8-10, volke2021cofactorspecificityof pages 7-9)

**Visual evidence:** Figure panels summarizing the NADPH balance shift and enzyme activity changes under oxidative stress are available in the extracted images. (i.2021reconfigurationofmetabolic media b8b02296, i.2021reconfigurationofmetabolic media a2c989ad)

### 4) Quantitative cofactor specificity and redox outputs (KT2440)

#### 4.1 Whole-cell-extract cofactor preference (combined Zwf activity)
Because KT2440 has multiple Zwf isozymes, measured cofactor preference can depend on assay conditions and reflects the **combined** activity of all contributing isozymes.

In KT2440 glucose-grown extracts:
- Under **saturating** assay conditions, total Zwf activity showed ~**67.1% NADP+** and ~**32.9% NAD+** usage.
- Under **non-saturating (quasi in vivo)** conditions, the same activity becomes strongly NADP+-biased: ~**93.8% NADP+** vs ~**6.2% NAD+**.

This supports a model where in vivo Zwf function is tuned toward NADPH production. (nikel2015pseudomonasputidakt2440 pages 21-25)

#### 4.2 Isozyme-level specialization (notably zwfC)
Isozyme-resolved biochemical modeling/kinetic comparisons indicate:
- **G6PDH-A (zwfA)** produces NADH and NADPH in roughly equal amounts under physiological settings (NADH/NADPH near 1).
- **G6PDH-B (zwfB)** tends to produce mostly NADH and has ~**5-fold lower Km for G6P** than G6PDH-A, implying stronger activity at low G6P.
- **G6PDH-C (zwfC = PP_5351 = Q88C32)** is highly NADP+-specific but has **kcat < 1 s−1** and is poorly expressed.

Together, this supports an “isozyme portfolio” hypothesis: KT2440 maintains multiple Zwf enzymes to flexibly balance NADH/NADPH output across carbon sources and environmental stresses. (volke2021cofactorspecificityof pages 7-9)

### 5) Recent developments (prioritizing 2023–2024)

#### 5.1 2024 systems-level engineering: derepressing glycolysis/PPP via **hexR** deletion
A 2024 *Nature Communications* study on engineering KT2440 derivatives for xylose utilization used **deletion of hexR** to derepress native glycolysis-associated functions, and explicitly pursued enhancing the **pentose phosphate pathway** by implanting additional transketolase/transaldolase activities. This positions the HexR–PPP/ED control structure (which includes zwf regulation in KT2440) as a practical engineering lever for expanding substrate scope and improving growth on non-native feedstocks. (Published 2024-03; https://doi.org/10.1038/s41467-024-46812-9) (dvorak2024syntheticallyprimedadaptationof pages 1-2)

Within their multilevel comparisons of evolved/engineered states, they report differential expression for **ZwfA** in pathway schematics (log2 fold changes shown), emphasizing the continued centrality of Zwf-mediated redox generation in rewired central metabolism—even when the target phenotype is new substrate assimilation (xylose → X5P → EDEMP cycle). (dvorak2024syntheticallyprimedadaptationof pages 9-10)

While this work does not single out **zwfC**, it is an authoritative recent example of real-world strain development where PPP/ED routing (and by implication Zwf gatekeeping) is explicitly engineered for lignocellulosic bioprocess goals. (dvorak2024syntheticallyprimedadaptationof pages 1-2)

#### 5.2 2023 preprint to 2024 paper trajectory (xylose adaptation)
A 2023 bioRxiv preprint on adapting *P. putida* to xylose (later published in 2024) emphasizes the importance of redox/PPP capacity and highlights Zwf as a key NADPH-supplying enzyme in this host’s physiology and engineering. (2023-05; https://doi.org/10.1101/2023.05.19.541448) (volke2021cofactorspecificityof pages 4-6)

### 6) Current applications and real-world implementations

#### 6.1 Bioprocess robustness and oxidative-stress tolerance
Mechanistic fluxomics under oxidative stress demonstrates that KT2440 increases NADPH-forming fluxes (including via Zwf and GntZ) to generate a substantial NADPH surplus that fuels glutathione-based detoxification, linking Zwf-network function to **stress robustness**—a core reason KT2440 is widely used for harsh industrial biotransformations and bioremediation contexts. (i.2021reconfigurationofmetabolic pages 1-2, i.2021reconfigurationofmetabolic pages 8-10)

#### 6.2 Metabolic engineering logic: using Zwf/PPP control for redox-intensive production
The broader metabolic-engineering literature treats zwf as an archetypal NADPH-supply lever (PPP entry) and highlights that cofactor supply limitations (especially NADPH regeneration) are frequent bottlenecks in redox-intensive whole-cell catalysis. While not KT2440-specific, this provides a conceptual rationale for why *P. putida*’s high-NADPH EDEMP architecture (with Zwf gatekeeping) is attractive as a chassis. (volke2021cofactorspecificityof pages 1-2)

### 7) Expert synthesis and interpretation (authoritative-source-backed)

1. **ZwfC (PP_5351/Q88C32) is a confirmed G6PDH-family enzyme but is not the dominant glycolytic Zwf in KT2440.** Evidence strongly supports very low zwfC transcription and minimal phenotype upon zwfC deletion, while showing that zwfA (and to a lesser extent zwfB) carries most G6PDH function in typical glycolytic regimes. (volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 2-4)

2. **KT2440’s multi-zwf design is best understood as a redox-balancing strategy rather than redundancy.** Isozyme differences in cofactor preference and substrate affinity (e.g., zwfB low Km for G6P; zwfC extreme NADP+ specificity but low kcat) support a division of labor that can reshape NADH vs NADPH production as carbon entry points and redox conditions vary. (volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 1-2)

3. **Zwf-linked NADPH generation is a cornerstone of oxidative-stress tolerance and thus industrial robustness, but attributing this system-level phenotype specifically to zwfC is not currently justified by available evidence.** Under oxidative stress, overall metabolic flux is rerouted to increase Zwf- and GntZ-linked NADPH formation, with net NADPH generation rising to 14.4 ± 0.3 mmol gCDW−1 h−1 and producing ~50% excess over biosynthetic demands; however, these analyses and enzyme activity measurements do not resolve zwfC’s individual contribution and likely reflect predominantly zwfA/zwfB activity. (i.2021reconfigurationofmetabolic pages 8-10, volke2021cofactorspecificityof pages 7-9)

### 8) High-value quantitative statistics for annotation (selected)
- **zwf-1 promoter induction by carbon source:** glucose/gluconate induce ~**25–50×** higher reporter activity than pyruvate/succinate; HexR deletion leads to constitutively high activity. (Kim et al., 2008-12; https://doi.org/10.1099/mic.0.2008/020362-0) (kim2008dualregulationof pages 4-6)
- **Oxidative stress NADPH surplus:** cyclic PPP operation yields NADPH formation exceeding biosynthetic demand by **~50%**; net NADPH generation reported **14.4 ± 0.3 mmol gCDW−1 h−1** in H2O2-stressed cultures. (Nikel et al., 2021-01-11; https://doi.org/10.1038/s41396-020-00884-9) (i.2021reconfigurationofmetabolic pages 8-10)
- **Enzyme activity shifts under oxidative stress:** Zwf activity **+4.7×**, GntZ activity **+9.2×** in vitro (cell-free extracts) under H2O2 vs control. (i.2021reconfigurationofmetabolic pages 8-10)
- **Total Zwf cofactor usage in extracts (glucose-grown):** saturating assays ~**67.1% NADP+ / 32.9% NAD+**; quasi in vivo assays ~**93.8% NADP+ / 6.2% NAD+**. (Nikel et al., 2015-10; https://doi.org/10.1074/jbc.M115.687749) (nikel2015pseudomonasputidakt2440 pages 21-25)
- **zwfC-specific biochemistry:** strongly **NADP+-specific**, with **kcat < 1 s−1** and very low transcription, consistent with minor contribution in standard conditions. (Volke et al., 2021-03-16; https://doi.org/10.1128/mSystems.00014-21) (volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 9-11)

### 9) Summary table (isoform map; includes target mapping)
The following table maps UniProt Q88C32 to the correct KT2440 zwf paralog and contrasts all zwf isozymes for practical annotation.

| Isoform / target mapping | Locus tag / identifier | Role in metabolism and growth phenotype | Expression / regulation notes | Cofactor specificity / kinetic highlights |
|---|---|---|---|---|
| **zwfA (G6PDH-A)** | **PP_1022** | Major G6PDH for glycolytic conditions; provides the bulk of total G6PDH activity. Deletion causes a major glucose-growth defect (reported as ~84% lower specific growth rate than WT on glucose), and activity is almost lost in mutants lacking zwfA; also important for fructose/ribose entry into the EDEMP/PP network (volke2021cofactorspecificityof pages 4-6, volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 2-4) | Part of the **zwfA-pgl-eda** operon. Strongly expressed on glucose/glycolytic substrates. Negatively regulated by **HexR**; deleting hexR caused a ~2.5-fold increase in a **PzwfA** reporter on fructose (volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 2-4) | Produces roughly balanced NADH and NADPH under simulated physiological conditions (NADH/NADPH output near 1). In total-cell Zwf activity assays, G6PDH activity in KT2440 is strongly NADP+-biased under quasi in vivo conditions (~93.8% NADP+ versus ~6.2% NAD+), though this reflects combined isozyme activity rather than zwfA alone (volke2021cofactorspecificityof pages 7-9, nikel2015pseudomonasputidakt2440 pages 21-25) |
| **zwfB (G6PDH-B)** | **PP_4042** | Contributes substantially alongside zwfA, especially as a metabolic gatekeeper for carbon sources entering different network nodes; double/triple zwf mutants show strong defects, including no growth of ΔzwfAB on ribose and ~70% lower growth rate of ΔzwfABC on fructose (volke2021cofactorspecificityof pages 4-6, volke2021cofactorspecificityof pages 2-4) | Cotranscribed with **gntZ**; less emphasized than zwfA in HexR-controlled glycolytic induction, but retained as an active isozyme in central carbon metabolism (volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 2-4) | Reported as **dual-cofactor** in P. putida KT2440 comparative analysis. Simulations indicate zwfB tends to generate mostly **NADH**; it has an approximately **5-fold lower Km for G6P** than G6PDH-A, suggesting effectiveness at lower substrate concentrations (volke2021cofactorspecificityof pages 7-9, shah2022glucose6phosphatedehydrogenasezwfa pages 5-8) |
| **zwfC (G6PDH-C)** | **PP_5351**; **UniProt Q88C32 target** | This is the user’s target protein. Present in KT2440 but appears to make little contribution to growth under tested conditions; deletion of **zwfC** alone had no significant effect on growth patterns, and the enzyme likely has a minor physiological role under standard conditions (volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 2-4) | **Poorly transcribed** across tested conditions; upstream region contains a duplicated/consensus **HexR**-binding motif and adjacent **RpiR-family regulator** gene (**PP_5350**), but reporter assays detected almost no **PzwfC** expression (volke2021cofactorspecificityof pages 9-11) | Highly **NADP+-specific**. Sequence conserves the canonical cofactor-binding motif and substrate-contact residues. The specificity coefficient (**ω**) is reported as about **5-fold higher** than the canonical E. coli G6PDH value (~410), but turnover is very low (**kcat < 1 s⁻¹**), consistent with near-zero activity in vivo (volke2021cofactorspecificityof pages 7-9, volke2021cofactorspecificityof pages 9-11) |
| **Total Zwf activity in KT2440 extracts** | Combined activity of **zwfA/zwfB/zwfC** | Supports the oxidative PP / ED-linked **EDEMP** cycle that underpins glucose catabolism and redox balancing in P. putida KT2440 (nikel2015pseudomonasputidakt2440 pages 1-2, volke2021cofactorspecificityof pages 2-4) | Under oxidative stress, carbon flux is rerouted toward cytosolic oxidation and Zwf-linked NADPH formation; Zwf activity increased **4.7-fold** in vitro, contributing to increased NADPH supply (i.2021reconfigurationofmetabolic pages 8-10) | Combined cofactor use in extracts grown on glucose: under saturating conditions ~**67.1% NADP+ / 32.9% NAD+**; under quasi in vivo conditions ~**93.8% NADP+ / 6.2% NAD+** (nikel2015pseudomonasputidakt2440 pages 21-25) |


*Table: This table maps the user’s UniProt target Q88C32 to zwfC/PP_5351 and contrasts all three Pseudomonas putida KT2440 zwf-encoded G6PDH isoforms by locus, physiological importance, regulation, and cofactor/kinetic properties. It is useful for distinguishing the specific target from the better-studied zwfA and zwfB paralogs.*

### 10) Practical functional annotation statements (recommended)

**Gene:** zwfC (PP_5351; UniProt Q88C32)

**Recommended molecular function:** Glucose-6-phosphate dehydrogenase isozyme (G6PDH-C); oxidizes G6P to 6-phosphogluconolactone with reduction of NADP+ (high specificity) and supports NADPH generation capacity in the ED/PP-linked central carbon metabolism network. (kim2008dualregulationof pages 4-6, volke2021cofactorspecificityof pages 7-9)

**Recommended pathway assignment:** Oxidative PP / ED interface (EDEMP cycle connection point), but likely auxiliary under many laboratory conditions due to low expression and low turnover. (volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 9-11, volke2021cofactorspecificityof pages 7-9)

**Regulatory notes:** Promoter region contains HexR motifs, yet zwfC reporter expression is near-zero under tested conditions; core HexR/KDPG regulation is clearly demonstrated for the major zwf promoter system in KT2440. (kim2008dualregulationof pages 6-7, volke2021cofactorspecificityof pages 9-11)

**Phenotype notes:** zwfC deletion alone: no significant growth effect across tested substrates; contrast with zwfA deletion showing strong growth impairment on glucose. (volke2021cofactorspecificityof pages 2-4, volke2021cofactorspecificityof pages 7-9)

### Figures (evidence)
- NADPH balance shift under oxidative stress and enzyme activity ratios including Zwf/GntZ: (i.2021reconfigurationofmetabolic media b8b02296, i.2021reconfigurationofmetabolic media a2c989ad)


References

1. (volke2021cofactorspecificityof pages 2-4): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 40 citations and is from a peer-reviewed journal.

2. (nikel2015pseudomonasputidakt2440 pages 21-25): Pablo I. Nikel, Max Chavarría, Tobias Fuhrer, Uwe Sauer, and Víctor de Lorenzo. Pseudomonas putida kt2440 strain metabolizes glucose through a cycle formed by enzymes of the entner-doudoroff, embden-meyerhof-parnas, and pentose phosphate pathways. Journal of Biological Chemistry, 290:25920-25932, Oct 2015. URL: https://doi.org/10.1074/jbc.m115.687749, doi:10.1074/jbc.m115.687749. This article has 427 citations and is from a domain leading peer-reviewed journal.

3. (volke2021cofactorspecificityof pages 9-11): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 40 citations and is from a peer-reviewed journal.

4. (volke2021cofactorspecificityof pages 7-9): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 40 citations and is from a peer-reviewed journal.

5. (kim2008dualregulationof pages 4-6): Juhyun Kim, Che Ok Jeon, and Woojun Park. Dual regulation of zwf-1 by both 2-keto-3-deoxy-6-phosphogluconate and oxidative stress in pseudomonas putida. Microbiology, 154 Pt 12:3905-16, Dec 2008. URL: https://doi.org/10.1099/mic.0.2008/020362-0, doi:10.1099/mic.0.2008/020362-0. This article has 75 citations and is from a peer-reviewed journal.

6. (volke2021cofactorspecificityof pages 1-2): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 40 citations and is from a peer-reviewed journal.

7. (i.2021reconfigurationofmetabolic pages 8-10): Pablo I. Nikel, Tobias Fuhrer, Max Chavarria, Alberto Sanchez-Pascuala, Uwe Sauer, and Victor de Lorenzo. Reconfiguration of metabolic fluxes in pseudomonas putida as a response to sub-lethal oxidative stress. The ISME Journal, 15:1751-1766, Jan 2021. URL: https://doi.org/10.1038/s41396-020-00884-9, doi:10.1038/s41396-020-00884-9. This article has 152 citations.

8. (nikel2015pseudomonasputidakt2440 pages 1-2): Pablo I. Nikel, Max Chavarría, Tobias Fuhrer, Uwe Sauer, and Víctor de Lorenzo. Pseudomonas putida kt2440 strain metabolizes glucose through a cycle formed by enzymes of the entner-doudoroff, embden-meyerhof-parnas, and pentose phosphate pathways. Journal of Biological Chemistry, 290:25920-25932, Oct 2015. URL: https://doi.org/10.1074/jbc.m115.687749, doi:10.1074/jbc.m115.687749. This article has 427 citations and is from a domain leading peer-reviewed journal.

9. (kim2008dualregulationof pages 6-7): Juhyun Kim, Che Ok Jeon, and Woojun Park. Dual regulation of zwf-1 by both 2-keto-3-deoxy-6-phosphogluconate and oxidative stress in pseudomonas putida. Microbiology, 154 Pt 12:3905-16, Dec 2008. URL: https://doi.org/10.1099/mic.0.2008/020362-0, doi:10.1099/mic.0.2008/020362-0. This article has 75 citations and is from a peer-reviewed journal.

10. (i.2021reconfigurationofmetabolic pages 1-2): Pablo I. Nikel, Tobias Fuhrer, Max Chavarria, Alberto Sanchez-Pascuala, Uwe Sauer, and Victor de Lorenzo. Reconfiguration of metabolic fluxes in pseudomonas putida as a response to sub-lethal oxidative stress. The ISME Journal, 15:1751-1766, Jan 2021. URL: https://doi.org/10.1038/s41396-020-00884-9, doi:10.1038/s41396-020-00884-9. This article has 152 citations.

11. (i.2021reconfigurationofmetabolic media b8b02296): Pablo I. Nikel, Tobias Fuhrer, Max Chavarria, Alberto Sanchez-Pascuala, Uwe Sauer, and Victor de Lorenzo. Reconfiguration of metabolic fluxes in pseudomonas putida as a response to sub-lethal oxidative stress. The ISME Journal, 15:1751-1766, Jan 2021. URL: https://doi.org/10.1038/s41396-020-00884-9, doi:10.1038/s41396-020-00884-9. This article has 152 citations.

12. (i.2021reconfigurationofmetabolic media a2c989ad): Pablo I. Nikel, Tobias Fuhrer, Max Chavarria, Alberto Sanchez-Pascuala, Uwe Sauer, and Victor de Lorenzo. Reconfiguration of metabolic fluxes in pseudomonas putida as a response to sub-lethal oxidative stress. The ISME Journal, 15:1751-1766, Jan 2021. URL: https://doi.org/10.1038/s41396-020-00884-9, doi:10.1038/s41396-020-00884-9. This article has 152 citations.

13. (dvorak2024syntheticallyprimedadaptationof pages 1-2): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 33 citations and is from a highest quality peer-reviewed journal.

14. (dvorak2024syntheticallyprimedadaptationof pages 9-10): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 33 citations and is from a highest quality peer-reviewed journal.

15. (volke2021cofactorspecificityof pages 4-6): Daniel Christoph Volke, Karel Olavarría, and Pablo Iván Nikel. Cofactor specificity of glucose-6-phosphate dehydrogenase isozymes in pseudomonas putida reveals a general principle underlying glycolytic strategies in bacteria. Apr 2021. URL: https://doi.org/10.1128/msystems.00014-21, doi:10.1128/msystems.00014-21. This article has 40 citations and is from a peer-reviewed journal.

16. (shah2022glucose6phosphatedehydrogenasezwfa pages 5-8): Bhavik A. Shah, Sravanti T. Kasarlawar, and Prashant S. Phale. Glucose-6-phosphate dehydrogenase, zwfa, a dual cofactor-specific isozyme is predominantly involved in the glucose metabolism of pseudomonas bharatica csv86 <sup>t</sup>. Dec 2022. URL: https://doi.org/10.1128/spectrum.03818-22, doi:10.1128/spectrum.03818-22. This article has 7 citations and is from a domain leading peer-reviewed journal.

## Citations

1. kim2008dualregulationof pages 4-6
2. volke2021cofactorspecificityof pages 2-4
3. volke2021cofactorspecificityof pages 7-9
4. volke2021cofactorspecificityof pages 9-11
5. kim2008dualregulationof pages 6-7
6. dvorak2024syntheticallyprimedadaptationof pages 1-2
7. dvorak2024syntheticallyprimedadaptationof pages 9-10
8. volke2021cofactorspecificityof pages 4-6
9. volke2021cofactorspecificityof pages 1-2
10. https://doi.org/10.1038/s41467-024-46812-9
11. https://doi.org/10.1101/2023.05.19.541448
12. https://doi.org/10.1099/mic.0.2008/020362-0
13. https://doi.org/10.1038/s41396-020-00884-9
14. https://doi.org/10.1074/jbc.M115.687749
15. https://doi.org/10.1128/mSystems.00014-21
16. https://doi.org/10.1128/msystems.00014-21,
17. https://doi.org/10.1074/jbc.m115.687749,
18. https://doi.org/10.1099/mic.0.2008/020362-0,
19. https://doi.org/10.1038/s41396-020-00884-9,
20. https://doi.org/10.1038/s41467-024-46812-9,
21. https://doi.org/10.1128/spectrum.03818-22,