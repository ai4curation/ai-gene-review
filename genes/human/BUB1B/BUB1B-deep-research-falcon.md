---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T01:16:49.909500'
end_time: '2026-09-25T01:26:21.233856'
duration_seconds: 571.32
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: BUB1B
  gene_symbol: BUB1B
  uniprot_accession: O60566
  protein_description: 'RecName: Full=Mitotic checkpoint serine/threonine-protein
    kinase BUB1 beta; EC=2.7.11.1 {ECO:0000269|PubMed:10477750, ECO:0000269|PubMed:31201382};
    AltName: Full=MAD3/BUB1-related protein kinase; Short=hBUBR1; AltName: Full=Mitotic
    checkpoint kinase MAD3L; AltName: Full=Protein SSK1;'
  gene_info: Name=BUB1B {ECO:0000312|HGNC:HGNC:1149}; Synonyms=BUBR1 {ECO:0000303|PubMed:14706340,
    ECO:0000303|PubMed:16760428, ECO:0000303|PubMed:17376779, ECO:0000303|PubMed:17785528,
    ECO:0000303|PubMed:9763420}, MAD3L, SSK1 {ECO:0000303|PubMed:9618306};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: Bub1/Mad3. (IPR015661); Kinase-like_dom_sf. (IPR011009); Mad3/Bub1_I.
    (IPR013212); Mad3_BUB1_I (PF08311)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: BUB1B-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** O60566
- **Protein Description:** RecName: Full=Mitotic checkpoint serine/threonine-protein kinase BUB1 beta; EC=2.7.11.1 {ECO:0000269|PubMed:10477750, ECO:0000269|PubMed:31201382}; AltName: Full=MAD3/BUB1-related protein kinase; Short=hBUBR1; AltName: Full=Mitotic checkpoint kinase MAD3L; AltName: Full=Protein SSK1;
- **Gene Information:** Name=BUB1B {ECO:0000312|HGNC:HGNC:1149}; Synonyms=BUBR1 {ECO:0000303|PubMed:14706340, ECO:0000303|PubMed:16760428, ECO:0000303|PubMed:17376779, ECO:0000303|PubMed:17785528, ECO:0000303|PubMed:9763420}, MAD3L, SSK1 {ECO:0000303|PubMed:9618306};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Bub1/Mad3. (IPR015661); Kinase-like_dom_sf. (IPR011009); Mad3/Bub1_I. (IPR013212); Mad3_BUB1_I (PF08311)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "BUB1B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'BUB1B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **BUB1B** (gene ID: BUB1B, UniProt: O60566) in human.

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
- **UniProt Accession:** O60566
- **Protein Description:** RecName: Full=Mitotic checkpoint serine/threonine-protein kinase BUB1 beta; EC=2.7.11.1 {ECO:0000269|PubMed:10477750, ECO:0000269|PubMed:31201382}; AltName: Full=MAD3/BUB1-related protein kinase; Short=hBUBR1; AltName: Full=Mitotic checkpoint kinase MAD3L; AltName: Full=Protein SSK1;
- **Gene Information:** Name=BUB1B {ECO:0000312|HGNC:HGNC:1149}; Synonyms=BUBR1 {ECO:0000303|PubMed:14706340, ECO:0000303|PubMed:16760428, ECO:0000303|PubMed:17376779, ECO:0000303|PubMed:17785528, ECO:0000303|PubMed:9763420}, MAD3L, SSK1 {ECO:0000303|PubMed:9618306};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Bub1/Mad3. (IPR015661); Kinase-like_dom_sf. (IPR011009); Mad3/Bub1_I. (IPR013212); Mad3_BUB1_I (PF08311)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "BUB1B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'BUB1B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **BUB1B** (gene ID: BUB1B, UniProt: O60566) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: human **BUB1B / BUBR1** (UniProt O60566)

## Executive summary

The requested target is correctly identified. Human **BUB1B** encodes **BUBR1** (also hBUBR1, MAD3L or SSK1), a MAD3-related spindle-assembly-checkpoint protein; it is distinct from its paralogue **BUB1**. The supplied organism, *Homo sapiens*, accession O60566, Bub1/Mad3 domains and C-terminal kinase-like fold all agree with the literature. No evidence encountered indicated a symbol collision or a different organism-specific protein. (braga2020thefunctionofa pages 73-78, braga2020thefunctionof pages 78-82, malumbres2024mosaicvariegatedaneuploidy pages 1-2)

BUBR1 has two principal, mechanistically separable functions during mitosis:

1. **Checkpoint effector/scaffold:** BUBR1 is an essential component of the mitotic checkpoint complex (MCC; BUBR1–BUB3–MAD2–CDC20), which inhibits APC/C–CDC20 and prevents destruction of securin and cyclin B until chromosome attachment is satisfactory.
2. **Kinetochore attachment regulator:** its KARD recruits PP2A-B56 to outer kinetochores, counterbalancing Aurora B/MPS1-dependent phosphorylation, stabilizing correct kinetochore–microtubule attachments and facilitating checkpoint silencing. (braga2019thebubr1pseudokinase pages 1-5, braga2020thefunctionof pages 86-91)

Despite the historical name “mitotic checkpoint serine/threonine-protein kinase BUB1 beta” and EC annotation, the strongest current mechanistic evidence classifies the human C-terminal kinase-like region as a **pseudokinase** with structural/allosteric rather than established phosphotransferase activity. Consequently, no securely established intrinsic substrate specificity or catalytic reaction can presently be assigned to human BUBR1. A 2019 report that BUBR1 directly phosphorylates CENP-E Ser2639 remains important but conflicts with direct phosphotransfer and evolutionary evidence supporting catalytic inactivity. (braga2020thefunctionofa pages 151-155, huang2019bubr1phosphorylatescenpe pages 10-11, braga2020thefunctionof pages 82-86)

| Feature/function | Molecular mechanism/partners | Cellular location/timing | Evidence and confidence |
|---|---|---|---|
| **Target identity** | Human **BUB1B** encodes **BUBR1/hBUBR1**, the MAD3-related spindle-assembly-checkpoint protein corresponding to supplied UniProt **O60566**; distinct from paralogue **BUB1**. | Predominantly mitotic checkpoint machinery at outer kinetochores and in soluble MCC–APC/C complexes. | Gene–protein relationship and MAD3 homology are directly supported; **high confidence**. (braga2020thefunctionofa pages 73-78, braga2020thefunctionof pages 78-82, malumbres2024mosaicvariegatedaneuploidy pages 1-2) |
| **N-terminal checkpoint/scaffold function** | TPR region and **KEN boxes** engage checkpoint components; the **BUB3-binding/GLEBS domain** supports kinetochore recruitment, while KEN and **ABBA/IC20BD** motifs bind CDC20. BUBR1–BUB3–MAD2–CDC20 forms the **mitotic checkpoint complex (MCC)**, blocking CDC20-dependent substrate recognition and thereby inhibiting APC/C-mediated securin and cyclin-B destruction. | MCC is assembled/amplified during prometaphase in response to unattached kinetochores and acts as a diffusible inhibitor of mitotic APC/C. | Biochemical, structural and cellular evidence supports an essential scaffold/inhibitor role; **high confidence**. (braga2020thefunctionof pages 78-82, braga2020thefunctionofa pages 82-86, braga2020thefunctionof pages 86-91) |
| **KARD–PP2A-B56 attachment control** | The KARD contains a **LxxIxE** B56-binding motif. **CDK1 phosphorylation of S670** and **PLK1 phosphorylation of S676** enhance PP2A-B56 recruitment; the resulting phosphatase relay, with PP1, opposes Aurora-B/MPS1 signalling, stabilizes correct kinetochore–microtubule attachments and promotes checkpoint silencing. | Outer kinetochore during prometaphase–metaphase; activity becomes especially important as chromosomes congress and establish end-on attachments. | Residue-specific biochemical and functional evidence; **high confidence**. (braga2019thebubr1pseudokinase pages 1-5, braga2020thefunctionof pages 82-86) |
| **C-terminal kinase-like domain** | Although annotated historically as a serine/threonine kinase, human BUBR1 contains non-canonical catalytic-loop and glycine-loop substitutions. The best-supported interpretation is a **pseudokinase** with structural/allosteric functions: maintaining BUBR1 stability and promoting KARD phosphorylation/PP2A-B56 recruitment, possibly through coupling to BUB1. | C-terminal regulatory module acting at mitotic kinetochores; not required as a conventional kinase for the core MCC scaffold function. | Phylogenomic, structural and direct phosphotransfer assays support catalytic inactivity; earlier mutant phenotypes were confounded by protein destabilization or possible kinase contamination. **Moderate–high confidence**, acknowledging unresolved contrary findings. (braga2020thefunctionofa pages 151-155, braga2020thefunctionof pages 82-86, braga2019thebubr1pseudokinase pages 1-5) |
| **Proposed CENP-E substrate—disputed** | One 2019 study reported BUBR1-dependent phosphorylation of kinetochore motor **CENP-E at Ser2639**, proposed to switch microtubule binding from lateral association to end-on capture and enable plus-end tracking. This conflicts with direct evidence that purified human BUBR1 lacks phosphotransfer activity. | Proposed at kinetochores during chromosome congression and conversion to end-on microtubule attachment. | Ser2639 phosphorylation and its phenotype have experimental support, but attribution to intrinsic BUBR1 catalysis remains disputed; **low–moderate confidence for BUBR1 as the direct kinase**. (huang2019bubr1phosphorylatescenpe pages 10-11, braga2019thebubr1pseudokinase pages 1-5, braga2020thefunctionof pages 82-86) |
| **Mosaic variegated aneuploidy type 1 (MVA1)** | **Biallelic pathogenic BUB1B variants** weaken the checkpoint and attachment machinery, producing premature chromatid separation and mosaic aneuploidy. Reported manifestations include growth retardation, microcephaly, developmental delay, congenital anomalies and susceptibility to childhood cancers. | Constitutional disorder affecting proliferating tissues; peripheral lymphocytes show approximately **10–32% aneuploidy**, usually **>25%**, in a summarized cohort of **22 patients**. | Established autosomal-recessive disease association, although the condition and cohorts are rare; **high confidence for causality**, less precise phenotype-frequency estimates. (malumbres2024mosaicvariegatedaneuploidy pages 5-6, malumbres2024mosaicvariegatedaneuploidy pages 1-2) |
| **2024 monoallelic-variant/prostate-cancer study** | Rare heterozygous variants reduced BUBR1 expression or stability and produced premature chromatid separation, lagging chromosomes, premature mitotic exit and reduced Taxol response in edited prostate-cell models; carrier lymphocytes also showed PCS. | Germline variation assessed in blood and tumors; mitotic defects examined in CRISPR-edited RWPE-1 cells and carrier lymphocytes. | Among **462** early-onset/familial prostate-cancer cases, rare variants occurred in **~1.9%** overall (**2.5%** diagnosed before 56); frequency was **~0.6%** among **1,416** other hereditary-cancer referrals. PCS ranged **19–70%** in recurrent-variant carriers. Promising but requires replication and penetrance estimates before clinical use; **moderate confidence**. (silva2024bub1bmonoallelicgermline pages 1-2, silva2024bub1bmonoallelicgermline pages 11-12, silva2024bub1bmonoallelicgermline pages 12-15, silva2024bub1bmonoallelicgermline pages 15-16) |


*Table: Compact evidence map for human BUB1B/BUBR1 (UniProt O60566), separating established checkpoint and kinetochore functions from the disputed kinase claim. It also summarizes major disease evidence and quantitative findings reported in 2024.*

## 1. Identity, nomenclature and domain architecture

### 1.1 Identity verification

The literature directly states that **BUB1B encodes BUBR1**, a vital human spindle-assembly-checkpoint protein related more closely in functional organization to budding-yeast MAD3 than to a second conventional BUB1 kinase. Human BUBR1 therefore matches UniProt O60566 and the aliases hBUBR1/MAD3L supplied in the query. It should not be conflated with human BUB1, which retains conventional kinase activity and has different kinetochore functions. (braga2020thefunctionofa pages 73-78, braga2020thefunctionof pages 78-82)

### 1.2 Functional modules

BUBR1 is a multidomain, motif-rich protein rather than simply an enzyme:

- The **N-terminal TPR region** participates in checkpoint-protein interactions.
- Two **KEN boxes** bind CDC20 and are central to MCC-mediated APC/C inhibition.
- A **BUB3-binding/GLEBS or B3BD region** supports association with BUB3 and kinetochore recruitment.
- **ABBA/Phe-box/IC20BD motifs** provide additional CDC20-binding determinants.
- The central **kinetochore attachment regulatory domain (KARD)** contains an **LxxIxE** PP2A-B56-binding motif.
- The C terminus adopts a **protein-kinase-like fold**, but is best regarded as a pseudokinase domain in humans. (braga2020thefunctionof pages 78-82, braga2020thefunctionof pages 82-86, braga2020thefunctionofa pages 82-86)

This architecture aligns with the supplied InterPro/Pfam annotations—Bub1/Mad3 and Mad3/Bub1-I modules plus a kinase-like superfamily domain—while clarifying that membership in a kinase-fold family does not itself establish catalytic activity.

## 2. Primary molecular function

### 2.1 MCC assembly and APC/C inhibition

At unattached kinetochores, upstream MPS1-dependent phosphorylation of KNL1 MELT repeats recruits BUB3–BUB1 and subsequently BUB3–BUBR1-containing machinery. BUBR1 then functions principally as a checkpoint scaffold and inhibitor in the **MCC**, together with BUB3, MAD2 and CDC20. Its KEN and ABBA-related motifs bind CDC20, stabilizing an inhibitory complex that acts beyond the kinetochore as a diffusible “wait-anaphase” signal. (braga2020thefunctionof pages 78-82, braga2019thebubr1pseudokinase pages 1-5, braga2020thefunctionof pages 86-91)

Structural work on APC/C–MCC showed that BUBR1 degron-like elements occupy CDC20 substrate-recognition sites and that BUBR1 also obstructs productive engagement of an initiating E2 enzyme. Thus, BUBR1 does not merely recruit another inhibitor: it directly helps prevent APC/C from recognizing and ubiquitinating securin and cyclin B. Maintaining these proteins preserves sister-chromatid cohesion and high mitotic CDK activity, delaying anaphase and mitotic exit. This is fundamentally a **stoichiometric scaffold/inhibitor function**, not an enzymatic reaction. The key structural study was published in *Nature* in August 2016: https://doi.org/10.1038/nature19083.

Classic biochemical purification identified BUBR1, BUB3, MAD2 and CDC20 in near-equal stoichiometry in the human MCC and reported approximately **3,000-fold greater APC/C-inhibitory activity** than recombinant MAD2 alone. This foundational study was published in September 2001: https://doi.org/10.1083/jcb.200102093.

### 2.2 Recruitment of PP2A-B56 and attachment stabilization

BUBR1’s second major role occurs locally at the outer kinetochore. Its KARD contains an **LxxIxE** short linear motif recognized by PP2A regulatory B56 subunits. **CDK1 phosphorylation of BUBR1 Ser670** and **PLK1 phosphorylation of Ser676** strengthen B56 recruitment. BUBR1 therefore acts as a targeting platform that positions PP2A-B56 where kinetochore phosphosignalling must be reversed. (braga2019thebubr1pseudokinase pages 1-5, braga2020thefunctionof pages 82-86)

The BUBR1–PP2A-B56 complex opposes Aurora B-driven destabilization of kinetochore–microtubule attachments. Together with PP1, it contributes to a phosphatase relay that dephosphorylates KNL1-associated checkpoint machinery, weakens BUB1–MAD1 signalling, stabilizes appropriate end-on attachments and ultimately silences the SAC. Mutation of BUBR1 residues required for B56 binding disrupts chromosome congression; Aurora B inhibition can partially reverse this phenotype, supporting the proposed kinase–phosphatase balance. (braga2019thebubr1pseudokinase pages 1-5, braga2020thefunctionof pages 86-91)

Relevant primary studies include:

- Suijkerbuijk et al., *Developmental Cell*, October 2012: https://doi.org/10.1016/j.devcel.2012.09.005.
- Xu et al., *Biology Open*, March 2013: https://doi.org/10.1242/bio.20134051.
- Wang et al., PP2A-B56–BUBR1 crystal structure, June 2016: https://doi.org/10.1007/s13238-016-0283-4.
- Braga et al., *Cell Reports*, November 2020: https://doi.org/10.1016/j.celrep.2020.108397.

## 3. Catalytic activity and substrate specificity: an important annotation conflict

### 3.1 Evidence supporting pseudokinase classification

Human BUBR1 retains a kinase-like fold but contains noncanonical substitutions in the glycine-rich and catalytic loops. Phylogenomic, structural and direct biochemical analyses found no convincing intrinsic phosphotransfer activity. Some earlier “kinase-dead” substitutions also destabilized BUBR1, meaning that mitotic defects caused by these mutations cannot safely be attributed to loss of catalysis. Contaminating kinases are another concern in biochemical preparations. (braga2020thefunctionofa pages 151-155, braga2020thefunctionof pages 82-86)

The 2020 work concluded that the C-terminal region instead promotes KARD phosphorylation and PP2A-B56 recruitment **allosterically**. Deleting or mutating the region reduced kinetochore PP2A-B56, delayed checkpoint silencing and caused chromosome-alignment defects. Coupling between BUB1 and BUBR1 kinase-like domains may stabilize a BUBR1 conformation favorable for KARD regulation. Thus, the domain is functionally important even if catalytically inactive. (braga2020thefunctionofa pages 151-155, braga2019thebubr1pseudokinase pages 1-5)

### 3.2 Contrary CENP-E evidence

Huang et al. reported that human BUBR1 phosphorylates the kinesin CENP-E at **Ser2639**, enabling a transition from lateral microtubule association to end-on capture and promoting plus-end tracking. A phosphomimetic CENP-E mutant caused abnormal condensates and targeting defects, suggesting that this modification must be temporally controlled. The study appeared in *Cell Research* in June 2019: https://doi.org/10.1038/s41422-019-0178-z. (huang2019bubr1phosphorylatescenpe pages 10-11)

### 3.3 Recommended functional annotation

The most defensible annotation is:

> **Human BUBR1 is a spindle-checkpoint scaffold, APC/C inhibitor and PP2A-B56-targeting pseudokinase. Intrinsic serine/threonine phosphotransferase activity is disputed and is not sufficiently secure to define a canonical catalytic reaction or broad substrate specificity. CENP-E Ser2639 is a proposed direct substrate, but this assignment requires independent reconciliation with direct evidence of catalytic inactivity.**

Accordingly, database EC 2.7.11.1 should be interpreted cautiously rather than as proof that phosphotransfer is the protein’s primary physiological function.

## 4. Cellular localization and timing

BUBR1 is produced throughout the cell cycle but functions most prominently during mitosis. During prometaphase it accumulates at **unattached or improperly attached outer kinetochores**, through BUB3/BUB1-dependent interactions with the KNL1 checkpoint platform. Its kinetochore pool supports MCC generation and locally recruits PP2A-B56. As stable end-on attachments form and checkpoint signalling declines, kinetochore BUBR1 is reduced. (braga2020thefunctionofa pages 151-155, braga2019thebubr1pseudokinase pages 1-5)

A substantial functional pool is also **soluble in the mitotic cytoplasm** as part of the MCC. This spatial arrangement explains how a signal generated at one unattached kinetochore can inhibit APC/C molecules throughout the cell. APC/C–MCC complexes act in the nucleoplasm/cytosol of the open mitotic cell, whereas BUBR1’s attachment-regulatory role is specifically concentrated at the outer kinetochore. There is no evidence that BUBR1 is secreted, membrane-spanning or extracellular.

## 5. Biological pathways

### 5.1 Spindle assembly checkpoint

A simplified pathway is:

1. Unattached kinetochores permit **MPS1** to phosphorylate KNL1 MELT motifs.
2. BUB3–BUB1 and associated BUBR1 machinery accumulate at the outer kinetochore.
3. MAD2 conversion and CDC20 capture promote **MCC assembly**.
4. MCC-bound BUBR1 uses KEN/ABBA-related interfaces to inhibit APC/C–CDC20.
5. Securin and cyclin B remain stable; separase is restrained and anaphase is delayed.
6. Correct microtubule attachment reduces checkpoint production; MCC disassembly and APC/C reactivation permit anaphase.

BUBR1 loss or insufficiency shortens mitosis, permits premature chromatid separation and elevates chromosome missegregation. (braga2020thefunctionof pages 73-78, braga2020thefunctionof pages 86-91)

### 5.2 Attachment-error correction and checkpoint silencing

Aurora B destabilizes low-tension or incorrect attachments through phosphorylation of outer-kinetochore substrates. BUBR1-bound PP2A-B56 supplies the opposing phosphatase activity needed to stabilize productive attachments. PP2A-B56 and PP1 also remove checkpoint-supporting phosphorylations, coupling chromosome alignment to SAC silencing. BUBR1 therefore operates at the interface between **error correction** and **cell-cycle timing**, preventing both premature anaphase and unnecessarily prolonged arrest. (braga2019thebubr1pseudokinase pages 1-5, braga2020thefunctionof pages 86-91)

## 6. Human disease and experimental evidence

### 6.1 Mosaic variegated aneuploidy type 1

Biallelic pathogenic BUB1B variants cause autosomal-recessive **mosaic variegated aneuploidy type 1 (MVA1)**. The mechanistic chain is coherent: reduced or dysfunctional BUBR1 weakens checkpoint control and kinetochore attachment, causing premature chromatid separation and mosaic gains or losses of different chromosomes. Reported manifestations include prenatal/postnatal growth restriction, microcephaly, developmental delay or intellectual disability, dysmorphism, eye and cardiac abnormalities, seizures, hypotonia and congenital malformations. Childhood embryonal rhabdomyosarcoma and Wilms tumour are prominent cancer associations, with additional reported hematologic and solid malignancies. (malumbres2024mosaicvariegatedaneuploidy pages 5-6, malumbres2024mosaicvariegatedaneuploidy pages 1-2)

A 2024 *Nature Reviews Genetics* synthesis summarized **22 BUB1B-associated patients** and reported approximately **10–32% aneuploid peripheral lymphocytes**, usually more than 25%. Because MVA is rare and ascertainment is heterogeneous, these ranges should not be treated as population incidence estimates. Published August 2024: https://doi.org/10.1038/s41576-024-00762-6. (malumbres2024mosaicvariegatedaneuploidy pages 5-6)

Mouse dosage studies further demonstrate a threshold effect. Heterozygous-null animals had 14–19% aneuploid embryonic fibroblasts, whereas a hypomorphic allele producing approximately 10% of normal protein yielded 36% aneuploid fibroblasts and 15% aneuploid splenocytes. Reduction to approximately 4% produced 72% and 21%, respectively, and perinatal death. These data strongly support dosage-sensitive genome protection, although mouse percentages should not be extrapolated directly to patients. (malumbres2024mosaicvariegatedaneuploidy pages 9-10)

### 6.2 2024 monoallelic-variant study in prostate cancer

Silva et al. sequenced germline DNA from **462 early-onset/familial prostate-cancer cases** and **1,416 patients referred for other hereditary-cancer syndromes**. Rare BUB1B variants were detected in approximately **1.9%** and **0.6%**, respectively; among prostate cancers diagnosed before age 56, the reported frequency was **2.5%**. Nine rare-variant carriers were identified in the prostate cohort. (silva2024bub1bmonoallelicgermline pages 1-2, silva2024bub1bmonoallelicgermline pages 11-12)

The recurrent c.1171_1173del, p.Glu391del allele accounted for 38.9% of all carriers and 55.5% of hereditary-prostate-cancer index patients carrying a BUB1B variant. It was absent from 459 male controls in one comparison, but the estimated odds ratio of 10.98 had a wide uncertainty and **p=0.074**, so the association did not provide definitive population-level risk estimation. (silva2024bub1bmonoallelicgermline pages 11-12, silva2024bub1bmonoallelicgermline pages 5-6)

CRISPR-edited prostate epithelial cells and carrier lymphocytes supplied functional support: reduced BUBR1 abundance or stability was associated with premature chromatid separation, lagging chromosomes and premature mitotic exit. Premature chromatid separation ranged from **19% to 70%** among recurrent-variant carriers. Edited cells also showed reduced Taxol-induced growth inhibition and apoptosis. Published July 2024 in the *Journal of Biomedical Science*: https://doi.org/10.1186/s12929-024-01056-z. (silva2024bub1bmonoallelicgermline pages 12-15, silva2024bub1bmonoallelicgermline pages 15-16)

These findings are biologically compelling but should be considered **emerging evidence**, not yet proof that BUB1B is a clinically validated moderate-penetrance prostate-cancer gene or that taxanes should routinely be withheld. Replication, segregation analysis, penetrance estimates and prospective treatment-response studies are needed.

## 7. Current applications and real-world implementation

### Established uses

- **Rare-disease diagnosis:** BUB1B sequencing is relevant when MVA/PCS is suspected from mosaic aneuploidy, microcephaly, growth restriction and premature chromatid separation.
- **Functional cytogenetics:** lymphocyte aneuploidy and PCS assays can support interpretation of candidate variants, although normal ranges and laboratory methods must be controlled.
- **Research models:** BUB1B depletion, hypomorphic alleles and domain-specific mutants are extensively used to manipulate SAC strength, chromosome instability and kinetochore phosphoregulation.

### Emerging applications

- **Hereditary-cancer assessment:** the 2024 prostate-cancer data suggest that selected monoallelic variants may influence cancer susceptibility, but routine broad clinical actionability has not been established. (silva2024bub1bmonoallelicgermline pages 1-2, silva2024bub1bmonoallelicgermline pages 12-15)
- **Treatment stratification:** variant-associated Taxol resistance in edited cells raises the possibility of using BUB1B status or a PCS/CIN phenotype as a taxane-response biomarker. This remains preclinical and should not yet determine standard therapy. (silva2024bub1bmonoallelicgermline pages 11-12, silva2024bub1bmonoallelicgermline pages 15-16)
- **Drug discovery:** because human BUBR1 is probably a pseudokinase, conventional ATP-site kinase inhibition may not reproduce BUBR1 loss. More rational approaches would target protein–protein interfaces, stability, MCC assembly or KARD–PP2A-B56 recruitment, but systemic interference risks toxicity in normal proliferative tissues.

No direct BUBR1-targeted therapy is currently established as standard clinical practice. Its strongest present clinical relevance is diagnostic and mechanistic rather than as a validated drug target.

## 8. Conclusions

Human BUB1B/O60566 is unambiguously BUBR1, a MAD3-related mitotic checkpoint protein. Its primary physiological function is best understood not as conventional kinase catalysis but as coordinated **molecular scaffolding**: it forms the MCC to inhibit APC/C–CDC20 throughout the mitotic cell and recruits PP2A-B56 at outer kinetochores to stabilize correct microtubule attachments and terminate checkpoint signalling at the appropriate time. These functions explain why reduced BUBR1 causes premature chromatid separation, chromosome instability and MVA1.

The central annotation caveat is the kinase question. The preponderance of structural, evolutionary and biochemical evidence supports a human **pseudokinase**, whereas direct CENP-E Ser2639 phosphorylation has been reported by one major study. Until that contradiction is experimentally resolved, catalytic reaction and substrate-specificity annotations should be qualified, while BUBR1’s MCC/APC/C and KARD–PP2A-B56 functions can be assigned with high confidence. Recent 2024 work expands interest in monoallelic BUB1B variants as possible cancer-predisposition and taxane-response biomarkers, but these applications require independent clinical validation.

References

1. (braga2020thefunctionofa pages 73-78): LG Braga. The function of the pseudokinase domain of bubr1 in mitosis. Unknown journal, 2020.

2. (braga2020thefunctionof pages 78-82): LG Braga. The function of the pseudokinase domain of bubr1 in mitosis. Unknown journal, 2020.

3. (malumbres2024mosaicvariegatedaneuploidy pages 1-2): Marcos Malumbres and Carolina Villarroya-Beltri. Mosaic variegated aneuploidy in development, ageing and cancer. Nature reviews. Genetics, 25:864-878, Aug 2024. URL: https://doi.org/10.1038/s41576-024-00762-6, doi:10.1038/s41576-024-00762-6. This article has 20 citations.

4. (braga2019thebubr1pseudokinase pages 1-5): Luciano Gama Braga, Angel F. Cisneros, Michelle Mathieu, Maxime Clerc, Pauline Garcia, Baptiste Lottin, Chantal Garand, Philippe Thebault, Christian R Landry, and Sabine Elowe. The bubr1 pseudokinase domain promotes efficient kinetochore pp2a-b56 recruitment to regulate spindle checkpoint silencing and chromosome alignment. bioRxiv, Aug 2019. URL: https://doi.org/10.1101/733378, doi:10.1101/733378. This article has 1 citations.

5. (braga2020thefunctionof pages 86-91): LG Braga. The function of the pseudokinase domain of bubr1 in mitosis. Unknown journal, 2020.

6. (braga2020thefunctionofa pages 151-155): LG Braga. The function of the pseudokinase domain of bubr1 in mitosis. Unknown journal, 2020.

7. (huang2019bubr1phosphorylatescenpe pages 10-11): Yuejia Huang, Lin Lin, Xing Liu, Sheng Ye, Phil Y. Yao, Wenwen Wang, Fengrui Yang, Xinjiao Gao, Junying Li, Yin Zhang, Jiancun Zhang, Zhihong Yang, Xu Liu, Zhenye Yang, Jianye Zang, Maikun Teng, Zhiyong Wang, Ke Ruan, Xia Ding, Lin Li, Don W. Cleveland, Rongguang Zhang, and Xuebiao Yao. Bubr1 phosphorylates cenp-e as a switch enabling the transition from lateral association to end-on capture of spindle microtubules. Cell Research, 29:562-578, Jun 2019. URL: https://doi.org/10.1038/s41422-019-0178-z, doi:10.1038/s41422-019-0178-z. This article has 79 citations and is from a domain leading peer-reviewed journal.

8. (braga2020thefunctionof pages 82-86): LG Braga. The function of the pseudokinase domain of bubr1 in mitosis. Unknown journal, 2020.

9. (braga2020thefunctionofa pages 82-86): LG Braga. The function of the pseudokinase domain of bubr1 in mitosis. Unknown journal, 2020.

10. (malumbres2024mosaicvariegatedaneuploidy pages 5-6): Marcos Malumbres and Carolina Villarroya-Beltri. Mosaic variegated aneuploidy in development, ageing and cancer. Nature reviews. Genetics, 25:864-878, Aug 2024. URL: https://doi.org/10.1038/s41576-024-00762-6, doi:10.1038/s41576-024-00762-6. This article has 20 citations.

11. (silva2024bub1bmonoallelicgermline pages 1-2): Maria P. Silva, Luísa T. Ferreira, Natércia F. Brás, Lurdes Torres, Andreia Brandão, Manuela Pinheiro, Marta Cardoso, Adriana Resende, Joana Vieira, Carlos Palmeira, Gabriela Martins, Miguel Silva, Carla Pinto, Ana Peixoto, João Silva, Rui Henrique, Sofia Maia, Helder Maiato, Manuel R. Teixeira, and Paula Paulo. Bub1b monoallelic germline variants contribute to prostate cancer predisposition by triggering chromosomal instability. Journal of Biomedical Science, Jul 2024. URL: https://doi.org/10.1186/s12929-024-01056-z, doi:10.1186/s12929-024-01056-z. This article has 13 citations and is from a domain leading peer-reviewed journal.

12. (silva2024bub1bmonoallelicgermline pages 11-12): Maria P. Silva, Luísa T. Ferreira, Natércia F. Brás, Lurdes Torres, Andreia Brandão, Manuela Pinheiro, Marta Cardoso, Adriana Resende, Joana Vieira, Carlos Palmeira, Gabriela Martins, Miguel Silva, Carla Pinto, Ana Peixoto, João Silva, Rui Henrique, Sofia Maia, Helder Maiato, Manuel R. Teixeira, and Paula Paulo. Bub1b monoallelic germline variants contribute to prostate cancer predisposition by triggering chromosomal instability. Journal of Biomedical Science, Jul 2024. URL: https://doi.org/10.1186/s12929-024-01056-z, doi:10.1186/s12929-024-01056-z. This article has 13 citations and is from a domain leading peer-reviewed journal.

13. (silva2024bub1bmonoallelicgermline pages 12-15): Maria P. Silva, Luísa T. Ferreira, Natércia F. Brás, Lurdes Torres, Andreia Brandão, Manuela Pinheiro, Marta Cardoso, Adriana Resende, Joana Vieira, Carlos Palmeira, Gabriela Martins, Miguel Silva, Carla Pinto, Ana Peixoto, João Silva, Rui Henrique, Sofia Maia, Helder Maiato, Manuel R. Teixeira, and Paula Paulo. Bub1b monoallelic germline variants contribute to prostate cancer predisposition by triggering chromosomal instability. Journal of Biomedical Science, Jul 2024. URL: https://doi.org/10.1186/s12929-024-01056-z, doi:10.1186/s12929-024-01056-z. This article has 13 citations and is from a domain leading peer-reviewed journal.

14. (silva2024bub1bmonoallelicgermline pages 15-16): Maria P. Silva, Luísa T. Ferreira, Natércia F. Brás, Lurdes Torres, Andreia Brandão, Manuela Pinheiro, Marta Cardoso, Adriana Resende, Joana Vieira, Carlos Palmeira, Gabriela Martins, Miguel Silva, Carla Pinto, Ana Peixoto, João Silva, Rui Henrique, Sofia Maia, Helder Maiato, Manuel R. Teixeira, and Paula Paulo. Bub1b monoallelic germline variants contribute to prostate cancer predisposition by triggering chromosomal instability. Journal of Biomedical Science, Jul 2024. URL: https://doi.org/10.1186/s12929-024-01056-z, doi:10.1186/s12929-024-01056-z. This article has 13 citations and is from a domain leading peer-reviewed journal.

15. (braga2020thefunctionof pages 73-78): LG Braga. The function of the pseudokinase domain of bubr1 in mitosis. Unknown journal, 2020.

16. (malumbres2024mosaicvariegatedaneuploidy pages 9-10): Marcos Malumbres and Carolina Villarroya-Beltri. Mosaic variegated aneuploidy in development, ageing and cancer. Nature reviews. Genetics, 25:864-878, Aug 2024. URL: https://doi.org/10.1038/s41576-024-00762-6, doi:10.1038/s41576-024-00762-6. This article has 20 citations.

17. (silva2024bub1bmonoallelicgermline pages 5-6): Maria P. Silva, Luísa T. Ferreira, Natércia F. Brás, Lurdes Torres, Andreia Brandão, Manuela Pinheiro, Marta Cardoso, Adriana Resende, Joana Vieira, Carlos Palmeira, Gabriela Martins, Miguel Silva, Carla Pinto, Ana Peixoto, João Silva, Rui Henrique, Sofia Maia, Helder Maiato, Manuel R. Teixeira, and Paula Paulo. Bub1b monoallelic germline variants contribute to prostate cancer predisposition by triggering chromosomal instability. Journal of Biomedical Science, Jul 2024. URL: https://doi.org/10.1186/s12929-024-01056-z, doi:10.1186/s12929-024-01056-z. This article has 13 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](BUB1B-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. malumbres2024mosaicvariegatedaneuploidy pages 5-6
2. malumbres2024mosaicvariegatedaneuploidy pages 9-10
3. braga2020thefunctionofa pages 73-78
4. braga2020thefunctionof pages 78-82
5. malumbres2024mosaicvariegatedaneuploidy pages 1-2
6. braga2020thefunctionof pages 86-91
7. braga2020thefunctionofa pages 151-155
8. braga2020thefunctionof pages 82-86
9. braga2020thefunctionofa pages 82-86
10. braga2020thefunctionof pages 73-78
11. https://doi.org/10.1038/nature19083.
12. https://doi.org/10.1083/jcb.200102093.
13. https://doi.org/10.1016/j.devcel.2012.09.005.
14. https://doi.org/10.1242/bio.20134051.
15. https://doi.org/10.1007/s13238-016-0283-4.
16. https://doi.org/10.1016/j.celrep.2020.108397.
17. https://doi.org/10.1038/s41422-019-0178-z.
18. https://doi.org/10.1038/s41576-024-00762-6.
19. https://doi.org/10.1186/s12929-024-01056-z.
20. https://doi.org/10.1038/s41576-024-00762-6,
21. https://doi.org/10.1101/733378,
22. https://doi.org/10.1038/s41422-019-0178-z,
23. https://doi.org/10.1186/s12929-024-01056-z,