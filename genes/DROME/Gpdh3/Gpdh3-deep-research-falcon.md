---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:41:07.307417'
end_time: '2026-09-10T14:48:37.729703'
duration_seconds: 450.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Gpdh3
  gene_symbol: Gpdh3
  uniprot_accession: E1JIT1
  protein_description: 'RecName: Full=Glycerol-3-phosphate dehydrogenase [NAD(+)]
    {ECO:0000256|RuleBase:RU361243}; EC=1.1.1.8 {ECO:0000256|RuleBase:RU361243};'
  gene_info: Name=Gpdh3 {ECO:0000313|EMBL:ACZ94981.1, ECO:0000313|FlyBase:FBgn0263048};
    Synonyms=CG18427 {ECO:0000313|EMBL:ACZ94981.1}, CG31169 {ECO:0000313|EMBL:ACZ94981.1},
    Dmel\CG43343 {ECO:0000313|EMBL:ACZ94981.1}, GPDH-3 {ECO:0000313|EMBL:ACZ94981.1},
    gpdh-3 {ECO:0000313|EMBL:ACZ94981.1}, NEST:bs15d11 {ECO:0000313|EMBL:ACZ94981.1},
    NEST:bs16c09 {ECO:0000313|EMBL:ACZ94981.1}; ORFNames=CG43343 {ECO:0000313|EMBL:ACZ94981.1,
    ECO:0000313|FlyBase:FBgn0263048}, Dmel_CG43343 {ECO:0000313|EMBL:ACZ94981.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the NAD-dependent glycerol-3-phosphate
  protein_domains: 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328);
    G3P_DH_NAD-dep. (IPR006168); G3P_DH_NAD-dep_C. (IPR006109); G3P_DH_NAD-dep_euk.
    (IPR017751)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Gpdh3-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** E1JIT1
- **Protein Description:** RecName: Full=Glycerol-3-phosphate dehydrogenase [NAD(+)] {ECO:0000256|RuleBase:RU361243}; EC=1.1.1.8 {ECO:0000256|RuleBase:RU361243};
- **Gene Information:** Name=Gpdh3 {ECO:0000313|EMBL:ACZ94981.1, ECO:0000313|FlyBase:FBgn0263048}; Synonyms=CG18427 {ECO:0000313|EMBL:ACZ94981.1}, CG31169 {ECO:0000313|EMBL:ACZ94981.1}, Dmel\CG43343 {ECO:0000313|EMBL:ACZ94981.1}, GPDH-3 {ECO:0000313|EMBL:ACZ94981.1}, gpdh-3 {ECO:0000313|EMBL:ACZ94981.1}, NEST:bs15d11 {ECO:0000313|EMBL:ACZ94981.1}, NEST:bs16c09 {ECO:0000313|EMBL:ACZ94981.1}; ORFNames=CG43343 {ECO:0000313|EMBL:ACZ94981.1, ECO:0000313|FlyBase:FBgn0263048}, Dmel_CG43343 {ECO:0000313|EMBL:ACZ94981.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the NAD-dependent glycerol-3-phosphate
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); G3P_DH_NAD-dep. (IPR006168); G3P_DH_NAD-dep_C. (IPR006109); G3P_DH_NAD-dep_euk. (IPR017751)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Gpdh3" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Gpdh3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Gpdh3** (gene ID: Gpdh3, UniProt: E1JIT1) in DROME.

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
- **UniProt Accession:** E1JIT1
- **Protein Description:** RecName: Full=Glycerol-3-phosphate dehydrogenase [NAD(+)] {ECO:0000256|RuleBase:RU361243}; EC=1.1.1.8 {ECO:0000256|RuleBase:RU361243};
- **Gene Information:** Name=Gpdh3 {ECO:0000313|EMBL:ACZ94981.1, ECO:0000313|FlyBase:FBgn0263048}; Synonyms=CG18427 {ECO:0000313|EMBL:ACZ94981.1}, CG31169 {ECO:0000313|EMBL:ACZ94981.1}, Dmel\CG43343 {ECO:0000313|EMBL:ACZ94981.1}, GPDH-3 {ECO:0000313|EMBL:ACZ94981.1}, gpdh-3 {ECO:0000313|EMBL:ACZ94981.1}, NEST:bs15d11 {ECO:0000313|EMBL:ACZ94981.1}, NEST:bs16c09 {ECO:0000313|EMBL:ACZ94981.1}; ORFNames=CG43343 {ECO:0000313|EMBL:ACZ94981.1, ECO:0000313|FlyBase:FBgn0263048}, Dmel_CG43343 {ECO:0000313|EMBL:ACZ94981.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the NAD-dependent glycerol-3-phosphate
- **Key Domains:** 6-PGluconate_DH-like_C_sf. (IPR008927); 6PGD_dom2. (IPR013328); G3P_DH_NAD-dep. (IPR006168); G3P_DH_NAD-dep_C. (IPR006109); G3P_DH_NAD-dep_euk. (IPR017751)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Gpdh3" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Gpdh3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Gpdh3** (gene ID: Gpdh3, UniProt: E1JIT1) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* **Gpdh3** (UniProt E1JIT1)

## Executive conclusion

The gene symbol **Gpdh3 is ambiguous in the literature, and literature is limited for this specific protein**. The requested target is the *D. melanogaster* locus **Gpdh3/CG43343/FBgn0263048**, represented by UniProt **E1JIT1** and annotated computationally as an NAD-dependent glycerol-3-phosphate dehydrogenase (EC 1.1.1.8). However, the historical term **“GPDH-3” usually refers to an alternatively processed isozyme of the classical *Gpdh* locus**, not to CG43343. Those historical results must therefore not be attributed to E1JIT1.

No primary publication directly characterizing CG43343/E1JIT1 was identified, including in targeted searches for **Gpdh3, gpdh-3, GPDH-3, CG43343, CG31169, CG18427, Dmel_CG43343,** and **FBgn0263048**. Accordingly, the most defensible annotation is a **family- and domain-based prediction**, not an experimentally demonstrated gene-specific function.

## 1. Identity verification and nomenclature

### Verified target

The supplied UniProt record identifies:

- **Organism:** *Drosophila melanogaster* (fruit fly)
- **Gene:** *Gpdh3*
- **Stable gene identifier:** FBgn0263048
- **Current/associated CG identifier:** CG43343
- **UniProt accession:** [E1JIT1](https://www.uniprot.org/uniprotkb/E1JIT1/entry)
- **Predicted product:** glycerol-3-phosphate dehydrogenase [NAD(+)]
- **EC number:** [EC 1.1.1.8](https://enzyme.expasy.org/EC/1.1.1.8)

The record’s ECO codes indicate that the enzyme name is **RuleBase-derived**, while gene-name links are imported from EMBL/FlyBase. Thus, identity and organism are database-supported, whereas catalytic function has not necessarily been demonstrated experimentally for E1JIT1.

### Critical collision with historical “GPDH-3”

A 1989 molecular analysis described the classical *Drosophila Gpdh* locus as one approximately 5-kb, eight-protein-coding-exon gene whose alternative 3′ processing generates GPDH-1, GPDH-2, and **GPDH-3** proteins with different C termini. Consequently, “GPDH-3” in that literature is an isozyme from the classical locus, not evidence about standalone *Gpdh3*/CG43343 (published November 1989; DOI: [10.1093/nar/17.21.8553](https://doi.org/10.1093/nar/17.21.8553)). (bewley1989sequencestructureand pages 1-2, bewley1989sequencestructureand pages 2-4)

A later transgenic study retained the same nomenclature: the exons 1–6 transcript encoded classical GPDH-3, whereas another terminal-exon arrangement encoded GPDH-4. That study provides no link to CG43343 or E1JIT1 (published October 1998; DOI: [10.1038/sj.hdy.6883890](https://doi.org/10.1038/sj.hdy.6883890)). (wilanowski1998expressionofthe pages 2-4, wilanowski1998expressionofthe pages 1-2)

Therefore, historical reports that classical GPDH-3 occurs in larval fat body, Malpighian tubules, or adult abdomen **cannot be used as localization or expression evidence for E1JIT1**. (bewley1989sequencestructureand pages 1-2, wilanowski1998expressionofthe pages 1-2)

## 2. Primary molecular-function prediction

### Predicted catalytic reaction

On the basis of the supplied EC assignment, E1JIT1 is predicted to catalyze the reversible reaction:

**sn-glycerol-3-phosphate + NAD⁺ ⇌ dihydroxyacetone phosphate + NADH + H⁺**

Under many biosynthetic or redox-balancing conditions, the physiologically relevant direction is expected to be:

**dihydroxyacetone phosphate + NADH + H⁺ → sn-glycerol-3-phosphate + NAD⁺**

Classical *Drosophila* GPDH literature experimentally associates this enzyme family with conversion of dihydroxyacetone phosphate to sn-glycerol-3-phosphate, glycolytic/redox metabolism, and diversion of carbohydrate carbon into lipid synthesis. This establishes the family’s biochemical context, but not E1JIT1-specific activity. (lissemore1990effectofdietary pages 1-4)

### Predicted substrate and cofactor specificity

The strongest defensible specificity assignment is:

- **Carbon substrates:** sn-glycerol-3-phosphate and dihydroxyacetone phosphate (DHAP)
- **Redox cofactor:** NAD⁺/NADH
- **Not established:** use of NADP(H), alternative polyols or phosphorylated carbonyl compounds

The supplied NAD-dependent family assignments distinguish this protein from membrane-associated, FAD-dependent mitochondrial glycerol-3-phosphate dehydrogenases. Nevertheless, no CG43343-specific substrate panel, cofactor-discrimination assay, inhibitor profile, **Km**, **Vmax**, or **kcat** has been reported in the literature retrieved.

### Domain and structural consistency

The supplied InterPro matches—**G3P_DH_NAD-dep** (IPR006168), **G3P_DH_NAD-dep_C** (IPR006109), **G3P_DH_NAD-dep_euk** (IPR017751), **6PGD_dom2** (IPR013328), and **6-PGluconate_DH-like_C_sf** (IPR008927)—are mutually consistent with a eukaryotic, soluble NAD-dependent glycerol-3-phosphate-dehydrogenase-fold protein. Classical GPDH sequence analysis independently distinguishes a relatively conserved NAD-binding region from a catalytic region, supporting the general architectural interpretation. (bewley1989sequencestructureand pages 13-15, bewley1989sequencestructureand pages 11-12)

These matches make the catalytic annotation biologically plausible, but domain recognition alone does not prove that E1JIT1 is active, determine its preferred reaction direction, or identify its physiological tissue.

The evidence levels are summarized below.

| Annotation topic | Best-supported conclusion | Evidence type/grade | Important limitation |
|---|---|---|---|
| Identity and organism | Target is **Gpdh3** (**FBgn0263048/CG43343; UniProt E1JIT1**) from *Drosophila melanogaster*, based on the UniProt record supplied by the user. | **Database annotation supplied by user; moderate confidence** | No target-specific primary paper was retrieved that independently links all identifiers. |
| Nomenclature collision | Historical **GPDH-3** denotes an alternatively processed isozyme of the classical *Gpdh* locus, not necessarily the modern standalone **Gpdh3/CG43343** gene. The classical locus is one approximately 5-kb, eight-exon gene producing multiple C-terminal isoforms (bewley1989sequencestructureand pages 1-2, bewley1989sequencestructureand pages 2-4). | **Direct literature evidence; high confidence** | Classical GPDH-3 findings, including fat-body expression, must not be assigned to E1JIT1/CG43343. |
| Predicted enzyme class | E1JIT1 is annotated as an NAD-dependent glycerol-3-phosphate dehydrogenase, **EC 1.1.1.8**. | **Rule-based UniProt annotation supplied by user; moderate confidence** | No CG43343-specific biochemical validation was found. |
| Predicted reaction | **sn-Glycerol-3-phosphate + NAD⁺ ⇌ dihydroxyacetone phosphate (DHAP) + NADH + H⁺**. Classical Drosophila GPDH literature supports the physiologically important reverse direction, DHAP reduction coupled to NADH oxidation (lissemore1990effectofdietary pages 1-4). | **Enzyme-class assignment plus family-level experimental context; moderate confidence** | Reaction direction and catalytic efficiency have not been measured specifically for E1JIT1. |
| Substrate and cofactor specificity | Predicted carbon substrates are **sn-glycerol-3-phosphate and DHAP**; the predicted pyridine-nucleotide pair is **NAD⁺/NADH**, rather than FAD or NADP(H). | **EC/family inference; moderate confidence** | No target-specific substrate panel, NAD-versus-NADP discrimination assay, Km, kcat, or inhibition data were found. |
| Domain architecture | Supplied InterPro assignments—**G3P_DH_NAD-dep**, **G3P_DH_NAD-dep_C**, **G3P_DH_NAD-dep_euk**, **6PGD_dom2**, and **6-PGluconate_DH-like_C_sf**—are consistent with a eukaryotic NAD-dependent G3P-dehydrogenase-family protein. Classical GPDH literature independently distinguishes conserved NAD-binding and catalytic regions (bewley1989sequencestructureand pages 13-15, bewley1989sequencestructureand pages 11-12). | **Sequence/domain inference; moderate-to-high confidence for family membership** | InterPro matches do not by themselves prove catalytic activity or physiological substrate use. |
| Subcellular localization | The most defensible working hypothesis is a **soluble intracellular, probably cytosolic enzyme**, consistent with the NAD-dependent G3P-dehydrogenase family. | **Family-level inference; low-to-moderate confidence** | No CG43343-specific imaging, fractionation, targeting-signal validation, or localization study was retrieved. |
| Likely biochemical pathways | If active as annotated, Gpdh3 would connect **DHAP metabolism, cytosolic NADH/NAD⁺ balance, and glycerol-3-phosphate supply for glycerolipid synthesis**. These roles are experimentally discussed for classical Drosophila GPDH (wilanowski1998expressionofthe pages 1-2, lissemore1990effectofdietary pages 1-4). | **Family-level pathway inference; moderate confidence** | Participation in the mitochondrial glycerol-phosphate shuttle or a particular tissue pathway is not established for CG43343. |
| Expression and phenotype | **Unknown for the specific target** in the literature retrieved. Historical larval fat-body, Malpighian-tubule, and adult-abdominal observations concern the classical GPDH-3 splice isozyme (bewley1989sequencestructureand pages 1-2, wilanowski1998expressionofthe pages 1-2). | **Evidence gap; high confidence that cited evidence is not target-specific** | Classical-locus expression and mutant phenotypes cannot be transferred to FBgn0263048. |
| Kinetics and quantitative data | No E1JIT1-specific activity, affinity, turnover, oligomeric-state, abundance, loss-of-function, or effect-size measurements were found. | **Evidence gap** | The reported evolutionary rate of **2.0 accepted substitutions per 100 residues per 100 million years** pertains to classical GPDH and is not a CG43343 measurement (bewley1989sequencestructureand pages 12-13). |
| Recent research, 2023–2024 | No directly relevant 2023–2024 primary study on **Gpdh3/CG43343/E1JIT1** was identified in the searches performed. | **Search result/evidence gap** | There are consequently no defensible recent gene-specific applications, implementations, expert conclusions, or quantitative developments to report. |


*Table: Evidence-graded annotation of Drosophila Gpdh3 that separates the supplied database prediction and family-level inference from direct target-specific evidence. It also highlights the critical collision between modern Gpdh3/CG43343 and the classical GPDH-3 splice-isozyme name.*

## 3. Biological processes and biochemical pathways

If E1JIT1 is catalytically active as predicted, it would potentially connect three processes:

1. **Glycerolipid-backbone production.** Reduction of DHAP produces sn-glycerol-3-phosphate, the glycerol backbone precursor used in phospholipid and triacylglycerol biosynthesis.
2. **Cytosolic redox balancing.** DHAP reduction consumes NADH and regenerates NAD⁺, potentially supporting continued glycolytic flux.
3. **Carbohydrate–lipid carbon partitioning.** The reaction diverts a glycolytic intermediate toward glycerolipid synthesis.

These roles are directly discussed for classical *Drosophila* GPDH: GPDH activity has been associated with cytoplasmic NAD⁺/NADH regulation and provision of sn-glycerol-3-phosphate for lipid biosynthesis. (wilanowski1998expressionofthe pages 1-2, lissemore1990effectofdietary pages 1-4)

Participation by CG43343 in the **glycerol-phosphate shuttle** is possible in principle but is not established. That shuttle requires coordinated oxidation of cytosolic NADH through soluble NAD-dependent GPDH and transfer of reducing equivalents to a mitochondrial FAD-dependent enzyme. Neither physical interaction nor pathway flux has been measured for E1JIT1.

## 4. Cellular and tissue localization

The best current working hypothesis is that E1JIT1 is a **soluble intracellular protein, probably cytosolic**, because its sequence is assigned to the soluble NAD-dependent GPDH family rather than the membrane-associated FAD-dependent enzyme class. This remains an inference.

No target-specific evidence was found from:

- fluorescent-protein imaging;
- immunohistochemistry;
- cell fractionation or organellar proteomics;
- targeting-sequence validation;
- tissue-specific protein detection.

Historical localization of “GPDH-3” to fat body and Malpighian tubules concerns the splice-derived product of the classical *Gpdh* locus and is explicitly excluded from the annotation of CG43343. (bewley1989sequencestructureand pages 1-2)

## 5. Expression, genetics, and phenotype

No direct CG43343/E1JIT1 study was retrieved that establishes developmental timing, sex bias, tissue enrichment, metabolic regulation, essentiality, or mutant phenotype. Likewise, there is no defensible gene-specific evidence for effects on flight, lipid storage, starvation resistance, fertility, development, or lifespan.

A 1990 dietary study found that ethanol and several carbohydrates increased activity and transcript abundance from the **classical *Gpdh* locus**, with transcript-specific regulation. This is useful evidence that the broader enzyme system can be nutritionally regulated, but it is not evidence that *Gpdh3*/CG43343 responds similarly (published December 1990; DOI: [10.1007/BF00553954](https://doi.org/10.1007/BF00553954)). (lissemore1990effectofdietary pages 1-4)

## 6. Recent developments, applications, and quantitative evidence

### 2023–2024 literature

No directly relevant 2023–2024 primary publication on **Gpdh3/CG43343/FBgn0263048/E1JIT1** was identified. The absence of a retrieved paper is not proof that no dataset contains the gene, but it means there is no defensible recent mechanistic development to summarize as target-specific research.

### Applications and real-world implementation

There are currently no validated applications specifically involving E1JIT1—such as a metabolic engineering target, biomarker, pesticide target, disease model, diagnostic reagent, or therapeutic target—in the evidence retrieved. Its immediate value is instead as an **uncharacterized candidate metabolic enzyme** suitable for functional-genomics and comparative-biochemistry studies.

### Relevant statistics

No E1JIT1-specific kinetic constants, expression fold changes, protein abundance measurements, structural-resolution statistics, or loss-of-function effect sizes were found. One historical analysis estimated an evolutionary rate of **2.0 accepted amino-acid substitutions per 100 residues per 100 million years** for classical Drosophila GPDH, but this is explicitly not a measurement of CG43343 and should not be transferred to it. (bewley1989sequencestructureand pages 12-13)

## 7. Expert assessment and confidence-ranked annotation

**High confidence:** The requested target is a *D. melanogaster* protein represented by E1JIT1 and associated with *Gpdh3*/CG43343/FBgn0263048 in the supplied record. It must be distinguished from the historical GPDH-3 splice isozyme.

**Moderate confidence:** Sequence/domain evidence supports membership in the eukaryotic NAD-dependent glycerol-3-phosphate dehydrogenase family and predicts EC 1.1.1.8 activity with DHAP/sn-glycerol-3-phosphate and NADH/NAD⁺.

**Low-to-moderate confidence:** The protein is probably soluble and cytosolic and may support glycerolipid precursor synthesis and cytosolic redox balance.

**Unknown:** Physiological reaction direction, tissue and developmental expression, subcellular localization, oligomeric state, kinetic constants, pathway importance, mutant phenotype, and in-vivo substrate specificity.

## 8. Experiments needed for definitive annotation

The highest-value validation sequence would be:

1. Express and purify E1JIT1 and test both reaction directions using DHAP/NADH and sn-glycerol-3-phosphate/NAD⁺.
2. Measure NADH absorbance or fluorescence to obtain **Km**, **kcat**, cofactor discrimination, pH optimum, and substrate breadth.
3. Verify endogenous expression using CG43343-specific RT-qPCR, targeted proteomics, or a genomic epitope-tagged allele.
4. Determine localization using an endogenous knock-in tag rather than overexpression alone.
5. Generate a precise knockout or catalytic-site mutant and quantify glycerol-3-phosphate, DHAP, NADH/NAD⁺, triacylglycerol, and phospholipid profiles.
6. Perform tissue-restricted rescue to identify the physiological site of action.

## Final annotation

**Gpdh3/CG43343 (UniProt E1JIT1) should presently be annotated as a predicted, likely soluble NAD-dependent glycerol-3-phosphate dehydrogenase-family protein whose probable reaction is DHAP + NADH + H⁺ ⇌ sn-glycerol-3-phosphate + NAD⁺. Its proposed roles in glycerolipid synthesis and cytosolic redox balance are family-level inferences. There is currently insufficient target-specific literature to assign a demonstrated localization, tissue, pathway dependence, kinetic profile, or organismal phenotype.**

References

1. (bewley1989sequencestructureand pages 1-2): Glenn C. Bewley, Julia L. Cook, Shinichi Kusakabe, Terumi Mukai, Donna L. Rigby, and Geoff K. Chambers. Sequence, structure and evolution of the gene coding for sn-glycerol-3-phosphate dehydrogenase in drosophila melanogaster. Nucleic acids research, 17 21:8553-67, Nov 1989. URL: https://doi.org/10.1093/nar/17.21.8553, doi:10.1093/nar/17.21.8553. This article has 60 citations and is from a highest quality peer-reviewed journal.

2. (bewley1989sequencestructureand pages 2-4): Glenn C. Bewley, Julia L. Cook, Shinichi Kusakabe, Terumi Mukai, Donna L. Rigby, and Geoff K. Chambers. Sequence, structure and evolution of the gene coding for sn-glycerol-3-phosphate dehydrogenase in drosophila melanogaster. Nucleic acids research, 17 21:8553-67, Nov 1989. URL: https://doi.org/10.1093/nar/17.21.8553, doi:10.1093/nar/17.21.8553. This article has 60 citations and is from a highest quality peer-reviewed journal.

3. (wilanowski1998expressionofthe pages 2-4): Tomasz M Wilanowski, Simon H S Yoong, Slawomir Bartoszewski, and John B Gibson. Expression of the gpdh-4 isozyme of sn-glycerol-3-phosphate dehydrogenase in three drosophila species. Heredity, 81:390-395, Oct 1998. URL: https://doi.org/10.1038/sj.hdy.6883890, doi:10.1038/sj.hdy.6883890. This article has 4 citations and is from a domain leading peer-reviewed journal.

4. (wilanowski1998expressionofthe pages 1-2): Tomasz M Wilanowski, Simon H S Yoong, Slawomir Bartoszewski, and John B Gibson. Expression of the gpdh-4 isozyme of sn-glycerol-3-phosphate dehydrogenase in three drosophila species. Heredity, 81:390-395, Oct 1998. URL: https://doi.org/10.1038/sj.hdy.6883890, doi:10.1038/sj.hdy.6883890. This article has 4 citations and is from a domain leading peer-reviewed journal.

5. (lissemore1990effectofdietary pages 1-4): James L. Lissemore, Christine A. Baumgardner, Billy W. Geer, and David T. Sullivan. Effect of dietary carbohydrates and ethanol on expression of genes encodingsn-glycerol-3-phosphate dehydrogenase, aldolase, and phosphoglycerate kinase indrosophila larvae. Biochemical Genetics, 28:615-630, Dec 1990. URL: https://doi.org/10.1007/bf00553954, doi:10.1007/bf00553954. This article has 19 citations and is from a peer-reviewed journal.

6. (bewley1989sequencestructureand pages 13-15): Glenn C. Bewley, Julia L. Cook, Shinichi Kusakabe, Terumi Mukai, Donna L. Rigby, and Geoff K. Chambers. Sequence, structure and evolution of the gene coding for sn-glycerol-3-phosphate dehydrogenase in drosophila melanogaster. Nucleic acids research, 17 21:8553-67, Nov 1989. URL: https://doi.org/10.1093/nar/17.21.8553, doi:10.1093/nar/17.21.8553. This article has 60 citations and is from a highest quality peer-reviewed journal.

7. (bewley1989sequencestructureand pages 11-12): Glenn C. Bewley, Julia L. Cook, Shinichi Kusakabe, Terumi Mukai, Donna L. Rigby, and Geoff K. Chambers. Sequence, structure and evolution of the gene coding for sn-glycerol-3-phosphate dehydrogenase in drosophila melanogaster. Nucleic acids research, 17 21:8553-67, Nov 1989. URL: https://doi.org/10.1093/nar/17.21.8553, doi:10.1093/nar/17.21.8553. This article has 60 citations and is from a highest quality peer-reviewed journal.

8. (bewley1989sequencestructureand pages 12-13): Glenn C. Bewley, Julia L. Cook, Shinichi Kusakabe, Terumi Mukai, Donna L. Rigby, and Geoff K. Chambers. Sequence, structure and evolution of the gene coding for sn-glycerol-3-phosphate dehydrogenase in drosophila melanogaster. Nucleic acids research, 17 21:8553-67, Nov 1989. URL: https://doi.org/10.1093/nar/17.21.8553, doi:10.1093/nar/17.21.8553. This article has 60 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Gpdh3-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. lissemore1990effectofdietary pages 1-4
2. bewley1989sequencestructureand pages 12-13
3. bewley1989sequencestructureand pages 1-2
4. bewley1989sequencestructureand pages 2-4
5. wilanowski1998expressionofthe pages 2-4
6. wilanowski1998expressionofthe pages 1-2
7. bewley1989sequencestructureand pages 13-15
8. bewley1989sequencestructureand pages 11-12
9. NAD(+)
10. E1JIT1
11. EC 1.1.1.8
12. 10.1093/nar/17.21.8553
13. 10.1038/sj.hdy.6883890
14. 10.1007/BF00553954
15. https://www.uniprot.org/uniprotkb/E1JIT1/entry
16. https://enzyme.expasy.org/EC/1.1.1.8
17. https://doi.org/10.1093/nar/17.21.8553
18. https://doi.org/10.1038/sj.hdy.6883890
19. https://doi.org/10.1007/BF00553954
20. https://doi.org/10.1093/nar/17.21.8553,
21. https://doi.org/10.1038/sj.hdy.6883890,
22. https://doi.org/10.1007/bf00553954,