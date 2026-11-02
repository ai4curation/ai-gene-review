---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-30T05:14:05.210386'
end_time: '2026-09-30T05:33:04.044074'
duration_seconds: 1138.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: N
  gene_symbol: N
  uniprot_accession: P07207
  protein_description: 'RecName: Full=Neurogenic locus Notch protein; Contains: RecName:
    Full=Processed neurogenic locus Notch protein; Flags: Precursor;'
  gene_info: Name=N {ECO:0000312|FlyBase:FBgn0004647}; ORFNames=CG3936 {ECO:0000312|FlyBase:FBgn0004647};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the NOTCH family. .
  protein_domains: Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770);
    EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_CS. (IPR013032)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 51
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: N-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: N-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: N-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P07207
- **Protein Description:** RecName: Full=Neurogenic locus Notch protein; Contains: RecName: Full=Processed neurogenic locus Notch protein; Flags: Precursor;
- **Gene Information:** Name=N {ECO:0000312|FlyBase:FBgn0004647}; ORFNames=CG3936 {ECO:0000312|FlyBase:FBgn0004647};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the NOTCH family. .
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_CS. (IPR013032)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "N" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'N' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **N** (gene ID: N, UniProt: P07207) in DROME.

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
- **UniProt Accession:** P07207
- **Protein Description:** RecName: Full=Neurogenic locus Notch protein; Contains: RecName: Full=Processed neurogenic locus Notch protein; Flags: Precursor;
- **Gene Information:** Name=N {ECO:0000312|FlyBase:FBgn0004647}; ORFNames=CG3936 {ECO:0000312|FlyBase:FBgn0004647};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the NOTCH family. .
- **Key Domains:** Ankyrin_rpt. (IPR002110); Ankyrin_rpt-contain_sf. (IPR036770); EGF. (IPR000742); EGF-like_Ca-bd_dom. (IPR001881); EGF-like_CS. (IPR013032)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "N" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'N' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **N** (gene ID: N, UniProt: P07207) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Notch Protein (Gene N, UniProt P07207) in *Drosophila melanogaster*

## Gene Identity Verification

The target gene **N** (CG3936) in *Drosophila melanogaster* encodes the Notch protein (UniProt P07207), a highly conserved transmembrane receptor that serves as the founding member of the NOTCH protein family (sachan2023notchsignallingmultifaceted pages 1-2, nurmahdi2022notchmissensemutations pages 1-2). The protein description "Neurogenic locus Notch protein" accurately reflects its discovery as a neurogenic gene, where loss-of-function mutations cause embryos to produce excessive neurons at the expense of epidermal tissue (sachan2023notchsignallingmultifaceted pages 4-4, sachan2023notchsignallingmultifaceted pages 2-2). The characteristic ankyrin repeat domains (IPR002110, IPR036770) and EGF-like domains (IPR000742, IPR001881, IPR013032) listed in the UniProt entry match the experimentally characterized structural organization of *Drosophila* Notch.

## Molecular Structure and Domain Organization

*Drosophila* Notch is organized as a large, single-pass type I transmembrane receptor with three principal regions: an extensive extracellular domain, a single transmembrane segment, and an intracellular signaling module (nurmahdi2022notchmissensemutations pages 1-2, pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4).

### Extracellular Domain

The extracellular region contains **36 tandem epidermal growth factor (EGF)-like repeats**, each approximately 40 amino acids in length and stabilized by three conserved disulfide bonds (nurmahdi2022notchmissensemutations pages 1-2, bray2025modesofnotch pages 24-27). These repeats serve multiple functions: they mediate ligand binding, with EGF repeats 11-12 constituting the core recognition region for both Delta and Serrate ligands, and additional repeats contributing to ligand selectivity and signaling strength (sachan2023notchsignallingmultifaceted pages 8-8, sachan2023notchsignallingmultifaceted pages 7-8). Specific EGF repeats, particularly those in positions 8-10 and 25, have been identified through mutational analysis as critical for proper receptor folding and trafficking through the endoplasmic reticulum (ER) (nurmahdi2022notchmissensemutations pages 1-2).

The extracellular domain also includes a **negative regulatory region (NRR)** composed of three cysteine-rich Lin-12/Notch repeats (LNR-A, LNR-B, LNR-C) and a heterodimerization domain (bray2025modesofnotch pages 24-27, lv2024evolutionandfunction pages 2-4). This region functions as an autoinhibitory module that masks the S2 protease cleavage site, preventing ligand-independent receptor activation (lv2024evolutionandfunction pages 2-4, bray2025modesofnotch pages 24-27).

### Intracellular Domain

The intracellular region contains several functional modules that mediate nuclear signaling. Immediately membrane-proximal is the **RAM domain** (RBP-Jκ association module), which provides high-affinity binding to the transcription factor Suppressor of Hairless [Su(H)], the *Drosophila* CSL protein (sachan2023notchsignallingmultifaceted pages 1-2, lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 8-8). Adjacent to this is a **nuclear localization sequence (NLS)** that directs the proteolytically released Notch intracellular domain (NICD) to the nucleus (sachan2023notchsignallingmultifaceted pages 1-2, lv2024evolutionandfunction pages 2-4).

The core signaling module consists of **seven ankyrin repeats** (also termed CDC10/ankyrin repeats) that mediate protein-protein interactions with Su(H), Mastermind, and other transcriptional regulators (sachan2023notchsignallingmultifaceted pages 1-2, bray2025modesofnotch pages 24-27, sachan2023notchsignallingmultifaceted pages 8-8). The C-terminal region includes intrinsically disordered regulatory sequences and a **PEST domain** (proline, glutamate, serine, threonine-rich) that controls NICD stability through recognition by the F-box protein Archipelago, targeting NICD for proteasomal degradation (bray2025modesofnotch pages 24-27, sachan2023notchsignallingmultifaceted pages 10-11).

| Domain or structural feature | Location | Specific features | Principal functional role | Evidence |
|---|---|---|---|---|
| Signal peptide | N terminus; secretory-pathway targeting sequence | Cleaved during receptor biogenesis | Directs nascent Notch into the endoplasmic reticulum for folding, glycosylation, and subsequent trafficking through the Golgi to the cell surface | (sachan2023notchsignallingmultifaceted pages 1-2, nurmahdi2022notchmissensemutations pages 1-2) |
| EGF-like repeat array | Extracellular | **36 tandem EGF-like repeats**; individual repeats are approximately 40 amino acids and usually contain six cysteines forming three disulfide bonds | Forms most of the extracellular domain; supports receptor folding and ligand recognition. EGF repeats 11–12 constitute the core binding region for Delta and are also critical for Serrate-dependent regulation; additional repeats tune ligand selectivity and signaling | (nurmahdi2022notchmissensemutations pages 1-2, sachan2023notchsignallingmultifaceted pages 8-8, sachan2023notchsignallingmultifaceted pages 7-8) |
| Glycosylated sites in EGF-like repeats | Extracellular | Carry O-fucose, O-glucose, O-GlcNAc, and N-linked glycans; Ofut1 installs O-fucose, Fringe extends selected O-fucose residues, and Rumi installs O-glucose | Regulate folding, secretory trafficking, cell-surface availability, and ligand responsiveness. Fringe modification generally enhances Delta-dependent signaling while reducing Serrate responsiveness | (sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6, sachan2023notchsignallingmultifaceted pages 7-7) |
| Negative regulatory region (NRR) | Extracellular, membrane-proximal | Comprises three cysteine-rich Lin-12/Notch repeats (LNR-A–C) plus a heterodimerization region; masks the S2 protease site in the resting receptor | Maintains autoinhibition and prevents ligand-independent cleavage. Mechanical force generated by ligand endocytosis opens the NRR and permits activating S2 cleavage | (bray2025modesofnotch pages 24-27, lv2024evolutionandfunction pages 2-4) |
| S2 cleavage region | Extracellular juxtamembrane segment | Normally buried by the NRR; cleaved by the ADAM-family metalloprotease Kuzbanian after ligand-dependent exposure | Removes the large extracellular region and generates the membrane-tethered Notch extracellular truncation/NEXT intermediate required for subsequent γ-secretase processing | (pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4, pinot2024spatiotemporalregulationof pages 13-15) |
| Single transmembrane helix | Plasma-membrane spanning | Anchors this type-I, single-pass receptor; contains the intramembrane S3 cleavage region | Couples extracellular ligand recognition to intracellular signal release. γ-Secretase cleaves the membrane-retained receptor fragment here to liberate NICD | (pinot2024spatiotemporalregulationof pages 2-4) |
| RAM domain | Intracellular, membrane-proximal portion of NICD | RBP-Jκ/Su(H)-association module | Provides a high-affinity interaction with the DNA-binding factor Suppressor of Hairless [Su(H)], helping recruit NICD to Notch-responsive regulatory DNA | (sachan2023notchsignallingmultifaceted pages 1-2, bray2025modesofnotch pages 24-27, lv2024evolutionandfunction pages 2-4) |
| Nuclear localization sequence (NLS) | Intracellular/NICD | Located between or near the RAM and ankyrin-repeat signaling modules | Promotes transport of proteolytically released NICD from the cytoplasm into the nucleus | (sachan2023notchsignallingmultifaceted pages 1-2, lv2024evolutionandfunction pages 2-4) |
| Ankyrin-repeat domain | Intracellular/NICD | **Seven ankyrin repeats** (also termed CDC10/ANK repeats) | Mediates protein–protein interactions with Su(H), Mastermind, and other transcriptional regulators; helps assemble and stabilize the nuclear NICD–Su(H)–Mastermind activation complex | (sachan2023notchsignallingmultifaceted pages 1-2, bray2025modesofnotch pages 24-27, sachan2023notchsignallingmultifaceted pages 8-8) |
| C-terminal regulatory region | Intracellular/NICD | Intrinsically disordered regulatory sequences downstream of the ankyrin repeats | Supports context-dependent transcriptional activation and provides sites for post-translational regulation of NICD activity and lifetime | (bray2025modesofnotch pages 24-27, bray2025modesofnotch pages 27-33) |
| PEST-rich domain | Intracellular, extreme C terminus | Enriched in proline, glutamate, serine, and threonine residues; recognized by the Drosophila F-box protein Archipelago following regulatory phosphorylation | Limits signal duration by promoting NICD polyubiquitination and proteasomal degradation after nuclear signaling | (bray2025modesofnotch pages 24-27, lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 10-11) |


*Table: Structural map of the Drosophila melanogaster Notch receptor (N; UniProt P07207), linking extracellular ligand-recognition and autoinhibitory modules to the transmembrane proteolytic switch and intracellular transcriptional-effector domains.*

## Primary Molecular Function: Transmembrane Receptor for Cell-Cell Communication

### Ligand Recognition and Substrate Specificity

Notch functions as a transmembrane receptor that mediates short-range communication between adjacent cells. In *Drosophila*, the receptor recognizes two canonical DSL (Delta-Serrate-Lag2) family ligands: **Delta (Dl)** and **Serrate (Ser)** (sachan2023notchsignallingmultifaceted pages 8-8, lv2024evolutionandfunction pages 2-4, pinot2024spatiotemporalregulationof pages 2-4). Both ligands are themselves transmembrane proteins expressed on the surface of signal-sending cells, making Notch signaling strictly juxtacrine—requiring direct cell-cell contact (pinot2024spatiotemporalregulationof pages 2-4, sachan2023notchsignallingmultifaceted pages 2-2). A third, non-DSL ligand called Weary (Wry, CG31665) has been identified in cardiac tissue, contributing to heart function through Notch activation (sachan2023notchsignallingmultifaceted pages 8-8).

The interaction between Notch and its ligands is modulated by post-translational glycosylation. EGF-like repeats are modified by **O-fucosyltransferase 1 (Ofut1)**, which adds O-fucose residues, and by **Fringe**, a glycosyltransferase that extends O-fucose with N-acetylglucosamine (sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6, sachan2023notchsignallingmultifaceted pages 7-7). Fringe modification generally enhances Delta-dependent signaling while reducing responsiveness to Serrate, thereby tuning ligand selectivity (sachan2023notchsignallingmultifaceted pages 7-8, sachan2023notchsignallingmultifaceted pages 7-7, nurmahdi2022notchmissensemutations pages 14-15). O-glucose modification by Rumi is essential for receptor folding and trafficking (sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6).

### Mechanism of Receptor Activation: Sequential Proteolytic Processing

Unlike typical receptor tyrosine kinases or G-protein-coupled receptors, Notch activation occurs through a regulated intramembrane proteolysis cascade involving three sequential cleavages (pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 2-2).

**S1 Cleavage**: During biosynthesis in the trans-Golgi network, Notch may undergo S1 cleavage by furin-like convertases, generating a heterodimeric receptor at the cell surface (sachan2023notchsignallingmultifaceted pages 2-2, sachan2023notchsignallingmultifaceted pages 4-5). However, this cleavage is dispensable for *Drosophila* Notch activity, and full-length receptor can reach the plasma membrane and signal effectively (pinot2024spatiotemporalregulationof pages 2-4, pinot2024spatiotemporalregulationof pages 13-15).

**S2 Cleavage**: Ligand binding initiates activation. When Delta or Serrate on a neighboring cell binds Notch, the ligand undergoes ubiquitination by E3 ligases Neuralized (Neur) or Mindbomb (Mib), promoting ligand endocytosis (lv2024evolutionandfunction pages 2-4, bray2025modesofnotch pages 24-27, bray2025modesofnotch pages 27-33). This endocytic event generates mechanical pulling force on the ligand-receptor complex, inducing a conformational change in the NRR that exposes the normally buried S2 cleavage site (lv2024evolutionandfunction pages 2-4, bray2025modesofnotch pages 24-27). The ADAM-family metalloprotease **Kuzbanian** then cleaves at the S2 site, removing the large extracellular domain and producing a membrane-tethered intermediate termed NEXT (Notch extracellular truncation) (pinot2024spatiotemporalregulationof pages 2-4, pinot2024spatiotemporalregulationof pages 13-15).

**S3 Cleavage**: The γ-secretase complex, composed of Presenilin, Nicastrin, APH-1, and PEN-2, performs intramembrane cleavage at the S3 site within the transmembrane segment (pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4). This liberates the **Notch intracellular domain (NICD)** from the membrane, converting a membrane-proximal signal into a soluble transcriptional regulator.

## Subcellular Localization

### Plasma Membrane Localization

The full-length Notch receptor localizes to the plasma membrane of signal-receiving cells, where it is positioned to interact with ligands on adjacent cells (pinot2024spatiotemporalregulationof pages 2-4, sachan2023notchsignallingmultifaceted pages 2-2, bray2025modesofnotch pages 24-27). In sensory organ precursor cells, Notch concentrates at the apical and lateral cell-cell interface, particularly in specialized Baz (Bazooka)-containing protein clusters that also contain Delta and the Notch regulator Sanpodo (pinot2024spatiotemporalregulationof pages 7-8, pinot2024spatiotemporalregulationof pages 4-6). Both apical and basal membrane pools contribute to signaling, with the basal pool identified as the major source of nuclear NICD production (pinot2024spatiotemporalregulationof pages 7-8, pinot2024spatiotemporalregulationof pages 4-6).

### Endosomal Trafficking

Following activation or as part of regulatory turnover, Notch traffics through the endocytic pathway. The receptor is detected in **Rab5-positive early endosomes** and **Rab7-positive late endosomes/multivesicular bodies** (katz2025autophagycontrolsdifferentiation pages 8-10, lv2024evolutionandfunction pages 2-4). Endosomal localization serves dual purposes: endosomes can be sites of productive γ-secretase cleavage and NICD release, but they also route receptors to lysosomes for degradation (katz2025autophagycontrolsdifferentiation pages 8-10, lv2024evolutionandfunction pages 2-4). The choice between activation and degradation is regulated by ubiquitination machinery and ESCRT (endosomal sorting complex required for transport) components (sachan2023notchsignallingmultifaceted pages 22-22, sachan2023notchsignallingmultifaceted pages 10-11).

### Nuclear Localization

After proteolytic release, NICD translocates to the nucleus, where it carries out its transcriptional function (pinot2024spatiotemporalregulationof pages 6-7, pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 2-2). In sensory organ lineages, nuclear NICD progressively accumulates in the Notch-active pIIa daughter cell, reaching plateau levels approximately 30 minutes after asymmetric division (pinot2024spatiotemporalregulationof pages 6-7). Nuclear localization is essential for the receptor's primary function: NICD does not possess intrinsic enzymatic activity but instead functions as a transcriptional coactivator.

## The Notch Signaling Pathway

### Transcriptional Activation Mechanism

In the nucleus, NICD executes its signaling function by forming a ternary transcriptional complex with two key partners: **Suppressor of Hairless [Su(H)]**, the *Drosophila* CSL (CBF1/RBP-Jκ/Su(H)/Lag-1) DNA-binding transcription factor, and **Mastermind (Mam)**, a transcriptional coactivator (sachan2023notchsignallingmultifaceted pages 8-8, lv2024evolutionandfunction pages 2-4, pinot2024spatiotemporalregulationof pages 2-4).

In the absence of NICD, Su(H) binds to Notch-responsive DNA elements and recruits corepressors such as Hairless, actively suppressing target genes (lv2024evolutionandfunction pages 2-4, lv2024evolutionandfunction pages 4-6). Upon NICD nuclear entry, NICD binds Su(H) through its RAM and ankyrin-repeat domains, and Mastermaid joins the complex, displacing corepressors and converting Su(H) into an activator (sachan2023notchsignallingmultifaceted pages 8-8, lv2024evolutionandfunction pages 2-4, lv2024evolutionandfunction pages 4-6). This activated complex recruits additional coactivators, including histone acetyltransferases such as CBP/EP300, PCAF, and GCN5, and chromatin-remodeling factors that open chromatin and promote transcription (lv2024evolutionandfunction pages 4-6). Recent work has shown that the histone variant H2Av and the Tip60 complex facilitate Notch signaling activity through a two-tier mechanism: they promote transcription of both Notch target genes and the Su(H) gene itself (chen2025thedrosophilahistone pages 1-2, chen2025thedrosophilahistone pages 5-7).

### Target Genes

The canonical direct targets of Notch signaling in *Drosophila* are the **Enhancer of split [E(spl)] complex genes**, which encode seven related basic helix-loop-helix (bHLH) transcriptional repressors: E(spl)m8, m7, m5, m3, mβ, mγ, and mδ (lv2024evolutionandfunction pages 25-26, pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4). These E(spl) proteins function as transcriptional repressors that suppress proneural genes, thereby executing Notch-dependent cell-fate decisions (lv2024evolutionandfunction pages 25-26, chen2023notchsignalingin pages 2-4).

Context-dependent target genes include developmental regulators such as **Cut**, **Deadpan**, and **Wingless** in wing development; **twist**, **tinman**, **Mes2**, **Mef2**, **stumps**, **NetA**, and **string** in early mesoderm patterning; and **WntD**, which provides negative feedback to Toll signaling during dorsal-ventral patterning (megaly2023notchsignallingplays pages 7-9, megaly2026notchsignallingplays pages 6-9).

### Lateral Inhibition: The Core Patterning Mechanism

A defining feature of Notch function is **lateral inhibition**, a cell-selection mechanism that generates distinct neighboring cell fates from initially equivalent cells (sachan2023notchsignallingmultifaceted pages 4-4, bray2025modesofnotch pages 24-27, bray2025modesofnotch pages 1-3). The mechanism operates through reciprocal feedback between Delta ligand and Notch signaling (yasugi2022mathematicalmodelingof pages 7-8, yasugi2022mathematicalmodelingof pages 1-2).

In proneural fields where all cells initially express both Notch and Delta, stochastic or pre-patterned differences are amplified through the following circuit (bray2025modesofnotch pages 24-27, bray2025modesofnotch pages 3-5, yasugi2022mathematicalmodelingof pages 1-2):

1. A cell with slightly higher Delta expression or proneural gene activity activates Notch more strongly in its neighbors
2. Notch activation induces E(spl) repressors, which suppress proneural genes (achaete-scute complex, atonal) and Delta expression in the receiving cells
3. Reduced Delta in receiving cells decreases Notch activation in the sending cell
4. The sending cell maintains high proneural activity and Delta, becomes specified as a neuroblast or sensory organ precursor
5. Neighboring cells, with high Notch and low Delta, are prevented from adopting the same neural fate and instead become epidermal cells

This creates a mutually exclusive, self-reinforcing pattern (sachan2023notchsignallingmultifaceted pages 4-4, yasugi2022mathematicalmodelingof pages 7-8, lv2024evolutionandfunction pages 2-4). Additionally, **cis-inhibition**—the antagonistic interaction between Notch and its ligands within the same cell—reinforces the contrast between sending and receiving states (yasugi2022mathematicalmodelingof pages 7-8, yasugi2022mathematicalmodelingof pages 1-2).

| Pathway step/component | Molecular players | Location/compartment | Mechanism/function |
|---|---|---|---|
| 1. Receptor maturation | Notch precursor; furin-like convertase | Endoplasmic reticulum and trans-Golgi network | Notch enters the secretory pathway for folding and glycosylation. S1 cleavage may generate associated extracellular and transmembrane-intracellular subunits, although furin/S1 processing is dispensable for *Drosophila* Notch activity and full-length receptor can reach the surface (pinot2024spatiotemporalregulationof pages 2-4, pinot2024spatiotemporalregulationof pages 13-15, sachan2023notchsignallingmultifaceted pages 2-2). |
| 2. Glycan-dependent tuning | Ofut1; Rumi; Fringe | ER and Golgi; extracellular EGF-like repeats | Ofut1 and Rumi add O-fucose and O-glucose, supporting receptor folding, trafficking, and activity. Fringe extends O-fucose with GlcNAc, generally increasing Delta responsiveness while reducing Serrate responsiveness (sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6, sachan2023notchsignallingmultifaceted pages 7-7). |
| 3. Juxtacrine ligand recognition | Delta (Dl); Serrate (Ser); Notch EGF repeats 11-12 | Contact between adjacent signal-sending and signal-receiving cells | Membrane-bound Delta or Serrate binds Notch in trans. EGF repeats 11-12 form the core ligand-interaction region, making canonical signaling short-range and contact dependent (sachan2023notchsignallingmultifaceted pages 8-8, lv2024evolutionandfunction pages 2-4, pinot2024spatiotemporalregulationof pages 2-4). |
| 4. Ligand activation and mechanical pulling | Neuralized (Neur); Mindbomb (Mib); Delta/Serrate | Plasma membrane and endocytic pathway of the sending cell | Neur- or Mib-dependent ligand ubiquitination promotes ligand endocytosis. Internalization exerts force on receptor-bound ligand, opening the Notch negative regulatory region and exposing the S2 site (lv2024evolutionandfunction pages 2-4, bray2025modesofnotch pages 24-27, bray2025modesofnotch pages 27-33). |
| 5. S2 extracellular cleavage | Kuzbanian; ADAM-family metalloprotease | Extracellular juxtamembrane region at the receiving-cell membrane | Kuzbanian/ADAM cleaves the exposed S2 site, removes the large extracellular portion, and produces the membrane-tethered activated intermediate NEXT (pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4, pinot2024spatiotemporalregulationof pages 13-15). |
| 6. S3 intramembrane cleavage | Gamma-secretase complex: Presenilin, Nicastrin, APH-1, PEN-2 | Plasma membrane or endosomal membrane of the receiving cell | Gamma-secretase cleaves NEXT within its transmembrane segment, releasing the Notch intracellular domain (NICD) from the membrane (pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4). |
| 7. NICD nuclear translocation | NICD; nuclear-localization sequences | Cytoplasm to nucleus | Released NICD moves into the nucleus, converting a membrane-proximal ligand encounter into a transcriptional response without a conventional kinase-based second-messenger cascade (pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4). |
| 8. Transcriptional switch | NICD; Suppressor of Hairless [Su(H)/CSL]; Mastermind (Mam); Hairless/corepressors | Nucleus; Notch-responsive enhancers and promoters | Without NICD, Su(H) supports transcriptional repression. NICD binds Su(H), and Mastermind joins the complex, displacing repression and recruiting coactivators and chromatin regulators (sachan2023notchsignallingmultifaceted pages 8-8, lv2024evolutionandfunction pages 2-4, lv2024evolutionandfunction pages 4-6). |
| 9. Canonical target-gene activation | Enhancer of split complex: *E(spl)m8, m7, m5, m3, mbeta, mgamma,* and *mdelta* | Nucleus | The NICD-Su(H)-Mastermind complex activates *E(spl)* genes encoding bHLH repressors. Their products suppress proneural programs and execute Notch-dependent fate choices (lv2024evolutionandfunction pages 25-26, pinot2024spatiotemporalregulationof pages 2-4, lv2024evolutionandfunction pages 2-4). |
| 10. Lateral-inhibition feedback | Notch; Delta; E(spl) repressors; achaete-scute proneural factors | Neighboring cells in proneural fields | A Delta-high cell activates Notch in its neighbor. Notch-induced E(spl) represses proneural genes and Delta in the receiving cell, amplifying small differences into stable sender and receiver states (sachan2023notchsignallingmultifaceted pages 4-4, bray2025modesofnotch pages 24-27, yasugi2022mathematicalmodelingof pages 1-2). |
| 11. Cis-regulation | Notch and Delta/Serrate expressed by the same cell | Plasma membrane of one cell | Ligand-receptor interaction in cis commonly inhibits productive signaling in trans, reinforcing sender-versus-receiver asymmetry during cell-fate selection (bray2025modesofnotch pages 27-33, yasugi2022mathematicalmodelingof pages 7-8). |
| 12. Receptor trafficking and termination | Deltex; Suppressor of deltex; Nedd4; ESCRT machinery; lysosomes | Endosomes, multivesicular bodies, and lysosomes | Ubiquitination and endosomal sorting determine whether Notch is recycled or activated from membranes versus incorporated into intraluminal vesicles and degraded in lysosomes (katz2025autophagycontrolsdifferentiation pages 8-10, lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 10-11). |
| 13. NICD turnover | Archipelago/Fbw7-related ubiquitin ligase; NICD PEST region; proteasome | Nucleus and cytoplasm | Phosphorylation-dependent recognition of the NICD PEST region promotes polyubiquitination and proteasomal destruction, limiting signal duration (lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 10-11). |


*Table: Stepwise summary of canonical Notch signaling in Drosophila, from receptor maturation and ligand-dependent proteolysis to nuclear transcription and signal termination. The table also highlights glycosylation, ubiquitination, trafficking, and lateral-inhibition controls.*

## Biological Processes and Developmental Functions

### Embryonic Neurogenesis

Notch was originally identified through its essential role in neurogenesis. During embryonic development, Notch regulates the selection of neuroblasts from proneural clusters in the neuroectoderm (chen2023notchsignalingin pages 2-4, sachan2023notchsignallingmultifaceted pages 4-4, sachan2023notchsignallingmultifaceted pages 2-2). Proneural genes including the achaete-scute complex, atonal, Bearded, and SoxNeuro encode bHLH transcription factors that promote neural fate, while Notch signaling antagonizes this program (sachan2023notchsignallingmultifaceted pages 4-4).

Through lateral inhibition, a single cell in each proneural cluster adopts the neuroblast fate with high Delta expression, while Notch activation in surrounding cells suppresses their proneural potential and directs them toward epidermal differentiation (chen2023notchsignalingin pages 2-4, yasugi2022mathematicalmodelingof pages 1-2, sachan2023notchsignallingmultifaceted pages 4-4). Loss of Notch function causes all cells in proneural clusters to become neuroblasts, resulting in nervous system hypertrophy and loss of epidermis—the classic neurogenic phenotype (sachan2023notchsignallingmultifaceted pages 4-4, sachan2023notchsignallingmultifaceted pages 2-2).

Notch continues to function throughout neural lineage progression, regulating neuroblast proliferation, neuronal fate specification, glial development, and aspects of axon pathfinding (chen2023notchsignalingin pages 2-4, chen2023notchsignalingin pages 16-17).

### Sensory Organ Development

In the pupal notum and wing margin, Notch mediates sensory organ precursor (SOP) selection and lineage specification (pinot2024spatiotemporalregulationof pages 1-2). Lateral inhibition first selects a single SOP from a proneural cluster. The SOP then undergoes asymmetric cell division, producing two daughter cells with distinct fates: pIIa (posterior, Notch-active) and pIIb (anterior, Notch-inactive) (pinot2024spatiotemporalregulationof pages 6-7, pinot2024spatiotemporalregulationof pages 1-2).

This fate asymmetry depends on unequal segregation of the Notch antagonist Numb and the Delta regulator Neuralized (pinot2024spatiotemporalregulationof pages 1-2). The pIIa cell, which receives less Numb, maintains active Notch signaling and generates external sensory structures (bristle shaft and socket), while the pIIb cell produces internal lineage components (neurons and support cells) (pinot2024spatiotemporalregulationof pages 6-7, pinot2024spatiotemporalregulationof pages 1-2). Spatio-temporal regulation of Notch activation at the apical and basal cell interface, coordinated by polarity proteins such as Bazooka, ensures proper fate specification during this critical division (pinot2024spatiotemporalregulationof pages 7-8, pinot2024spatiotemporalregulationof pages 4-6).

### Wing and Eye Development

In wing imaginal discs, Notch regulates multiple patterning processes: wing margin formation, vein versus intervein differentiation, cell proliferation, and sensory bristle patterning (lv2024evolutionandfunction pages 25-26). Spatially restricted Delta-Serrate-Notch interactions establish developmental boundaries, with Fringe-dependent glycosylation creating sharp transitions in ligand responsiveness (sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6). Notch loss-of-function produces the namesake "notched wing" phenotype, along with thickened veins and abnormal bristle placement (lv2024evolutionandfunction pages 25-26).

In eye development, Notch-mediated lateral inhibition restricts atonal expression and R8 photoreceptor specification, producing the regular spacing of ommatidial precursors (yasugi2022mathematicalmodelingof pages 1-2, lv2024evolutionandfunction pages 25-26). Disruption of Su(H) causes persistent atonal expression and excess R8 differentiation (lv2024evolutionandfunction pages 25-26). Notch also interacts with homeodomain transcription factors to diversify visual neuron types in the optic lobe (chen2023notchsignalingin pages 16-17).

### Mesoderm Patterning

Recent work has revealed an important role for Notch in early ventral mesoderm development (megaly2023notchsignallingplays pages 1-3). Endocytosis of Delta and Notch extracellular domain is prominently observed in the ventral mesoderm, indicating active signaling (megaly2023notchsignallingplays pages 1-3). Notch regulates expression of key mesodermal genes including twist, tinman, Mes2, Mef2, stumps, NetA, and string, and helps establish the mesoderm-mesectoderm-ectoderm boundary (megaly2023notchsignallingplays pages 7-9, megaly2023notchsignallingplays pages 1-3). Additionally, Notch induces WntD, which provides negative feedback to the Toll-mediated Dorsal/Twist/Snail patterning network, integrating Notch signaling with the primary dorsal-ventral patterning system (megaly2023notchsignallingplays pages 7-9, megaly2026notchsignallingplays pages 6-9, megaly2023notchsignallingplays pages 1-3).

### Hematopoiesis

In the larval lymph gland, Notch regulates blood cell progenitor maintenance and differentiation (katz2025autophagycontrolsdifferentiation pages 8-10, chen2023notchsignalingin pages 16-17). Notch signaling integrates nutrient availability with cell-fate decisions: under nutrient-rich conditions, TOR signaling inhibits autophagy, reducing lysosomal degradation of Notch and elevating Notch protein levels in progenitors (katz2025autophagycontrolsdifferentiation pages 8-10). High Notch activity promotes crystal cell (megakaryocyte-like) differentiation over plasmatocyte (macrophage-like) fate (katz2025autophagycontrolsdifferentiation pages 8-10). This regulation occurs through endosomal trafficking: Notch is activated at late endosomes, but autophagy-mediated delivery to lysosomes limits receptor abundance and signaling duration (katz2025autophagycontrolsdifferentiation pages 8-10).

| Process or tissue | Specific Notch function | Mechanism | Phenotype or biological outcome |
|---|---|---|---|
| Embryonic neuroectoderm and neurogenesis | Selects individual neuroblasts from proneural clusters and distinguishes neural from epidermal fates | Delta-high prospective neuroblasts activate Notch in adjacent cells. NICD–Su(H)–Mastermind induces E(spl) repressors, which suppress proneural activity and Delta expression in receiving cells through lateral inhibition. | Normal signaling produces spaced neural precursors surrounded by epidermal cells. Notch loss causes excess neuroblasts and nervous-system hypertrophy at the expense of epidermis. (chen2023notchsignalingin pages 2-4, sachan2023notchsignallingmultifaceted pages 4-4, yasugi2022mathematicalmodelingof pages 1-2) |
| Pupal notum and mechanosensory-organ lineage | Selects a single sensory-organ precursor and specifies binary pIIa versus pIIb daughter-cell identities | Lateral inhibition first selects the precursor. During asymmetric division, unequal segregation of Numb and Neuralized generates differential Notch activity: Notch-active pIIa produces external sensory cells, whereas Notch-low pIIb produces internal lineage cells. | Produces the correct number, spacing, and composition of mechanosensory bristles. Defective signaling causes abnormal precursor numbers and daughter-cell fate transformations. (pinot2024spatiotemporalregulationof pages 6-7, pinot2024spatiotemporalregulationof pages 7-8, pinot2024spatiotemporalregulationof pages 1-2) |
| Wing imaginal disc | Regulates wing-margin formation, vein versus intervein differentiation, proliferation, and sensory-bristle patterning | Spatially restricted Delta–Serrate–Notch signaling establishes developmental boundaries, while Fringe-dependent glycosylation changes ligand responsiveness and lateral inhibition patterns sensory precursors. | Normal activity produces an intact wing margin, narrow veins, and properly patterned bristles. Reduced signaling causes notched wings, thickened veins, and bristle abnormalities. (lv2024evolutionandfunction pages 25-26, sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6) |
| Eye imaginal disc and visual system | Controls photoreceptor spacing, restriction of R8 precursors, neuronal identity, and aspects of axon guidance | Notch-mediated lateral inhibition restricts persistent atonal expression and R8 differentiation. In later visual lineages, binary Notch states interact with lineage-specific transcription factors and regulate downstream guidance programs. | Produces regularly spaced ommatidial precursors and distinct visual-neuron identities. Disrupted signaling causes excess R8 cells, altered photoreceptor specification, and neural-patterning defects. (yasugi2022mathematicalmodelingof pages 1-2, lv2024evolutionandfunction pages 25-26) |
| Early ventral mesoderm and mesectoderm–ectoderm boundary | Coordinates mesodermal gene expression, gastrulation, and tissue-boundary formation | Notch-dependent transcription regulates twist, tinman, Mes2, Mef2, stumps, NetA, and string. Induction of WntD provides feedback to Toll-dependent Dorsal–Twist–Snail patterning. | Supports correct ventral-mesoderm patterning and boundary placement. Altered signaling changes mesodermal transcription and disrupts gastrulation-associated patterning. (megaly2023notchsignallingplays pages 7-9, megaly2023notchsignallingplays pages 1-3) |
| Larval lymph gland and hematopoiesis | Regulates progenitor maintenance and lineage choice, particularly crystal-cell differentiation | Cell-surface and endosomal Notch activity integrates niche and metabolic inputs. Endosomal maturation supports activation, whereas autophagic and lysosomal degradation limits receptor abundance and signaling. | Balanced signaling maintains appropriate progenitor and mature hemocyte populations. Reduced Notch degradation elevates pathway output and promotes crystal-cell differentiation. (katz2025autophagycontrolsdifferentiation pages 8-10, chen2023notchsignalingin pages 16-17) |


*Table: Key tissue-specific functions of Drosophila Notch, the mechanisms producing each developmental decision, and the principal outcomes of altered signaling.*

## Regulatory Mechanisms

### Post-Translational Modifications

**Glycosylation** is the primary extracellular regulatory mechanism. O-fucosylation by Ofut1, which is essential for both receptor folding and ligand interaction, is subsequently modified by Fringe to tune ligand responsiveness (sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6, sachan2023notchsignallingmultifaceted pages 7-7, nurmahdi2022notchmissensemutations pages 14-15). O-glucosylation by Rumi is critical for Notch folding and trafficking; loss of Rumi produces Notch-like phenotypes (sachan2023notchsignallingmultifaceted pages 7-8, lv2024evolutionandfunction pages 4-6). Under hypoxic conditions, NICD ankyrin repeats can be hydroxylated, affecting NICD interactions and activity (sachan2023notchsignallingmultifaceted pages 7-8, sachan2023notchsignallingmultifaceted pages 7-7).

**Ubiquitination** regulates both ligand and receptor. Neuralized and Mindbomb ubiquitinate Delta and Serrate, promoting ligand endocytosis and the mechanical force required for receptor activation (lv2024evolutionandfunction pages 2-4, bray2025modesofnotch pages 27-33). For the receptor itself, E3 ligases including Deltex, Suppressor of deltex (Su(dx)/Itch), and Nedd4 control Notch endocytosis, trafficking, and degradation (sachan2023notchsignallingmultifaceted pages 22-22, sachan2023notchsignallingmultifaceted pages 8-8, revici2022e3ubiquitinligase pages 10-12, sachan2023notchsignallingmultifaceted pages 10-11).

### Protein Stability and Turnover

Notch protein levels are controlled through multiple degradation pathways (sarkar2025regulationofnotch pages 18-22, sachan2023notchsignallingmultifaceted pages 22-22, lv2024evolutionandfunction pages 2-4, sachan2023notchsignallingmultifaceted pages 10-11). Full-length receptor can be ubiquitinated and routed to lysosomes for degradation via ESCRT-dependent sorting (sachan2023notchsignallingmultifaceted pages 22-22, sachan2023notchsignallingmultifaceted pages 10-11). The Mask protein has been identified as a positive regulator that stabilizes NICD by protecting it from lysosomal degradation; loss of Mask increases NICD turnover through lysosomal pathways (sarkar2025regulationofnotch pages 18-22).

In the nucleus, NICD turnover is controlled by phosphorylation-dependent recognition. The PEST domain serves as a degron: following phosphorylation, it is recognized by **Archipelago** (the *Drosophila* Fbw7 ortholog), an F-box protein that mediates NICD polyubiquitination and proteasomal degradation (sachan2023notchsignallingmultifaceted pages 10-11). This limits the duration of Notch-dependent transcription and allows for dynamic signaling responses.

## Summary

The Notch protein (gene N, UniProt P07207) in *Drosophila melanogaster* functions as a transmembrane receptor that mediates cell-cell communication through a unique proteolytic signaling mechanism. Its primary molecular function is to bind DSL-family ligands (Delta and Serrate) on adjacent cells and, through sequential proteolytic cleavages by Kuzbanian and γ-secretase, release the NICD transcriptional regulator. NICD translocates to the nucleus, where it forms a complex with Su(H) and Mastermind to activate target genes, most notably the E(spl) repressor complex.

The receptor localizes to the plasma membrane for ligand reception, traffics through endosomes during activation and turnover, and delivers NICD to the nucleus for transcriptional regulation. Notch signaling is extensively regulated by glycosylation (particularly Fringe-mediated modification), ubiquitination of ligands and receptors, endosomal trafficking, and phosphorylation-dependent NICD degradation.

Notch's key developmental role is mediating lateral inhibition, whereby small differences between initially equivalent cells are amplified through reciprocal Notch-Delta feedback, producing mutually exclusive cell fates. This mechanism underlies neuroblast selection, sensory organ precursor specification, photoreceptor patterning, and multiple other binary cell-fate decisions. Notch also regulates asymmetric cell division, tissue boundary formation, wing and eye development, mesoderm patterning, and hematopoiesis. The conservation of this pathway from flies to humans, combined with the extensive genetic tools available in *Drosophila*, has made the fly Notch protein one of the most intensively studied developmental regulators and a paradigm for understanding cell-fate determination in metazoan development.

References

1. (sachan2023notchsignallingmultifaceted pages 1-2): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

2. (nurmahdi2022notchmissensemutations pages 1-2): Hilman Nurmahdi, Mao Hasegawa, Elzava Yuslimatin Mujizah, Takeshi Sasamura, Mikiko Inaki, Shinya Yamamoto, Tomoko Yamakawa, and Kenji Matsuno. Notch missense mutations in drosophila reveal functions of specific egf-like repeats in notch folding, trafficking, and signaling. Biomolecules, 12:1752, Nov 2022. URL: https://doi.org/10.3390/biom12121752, doi:10.3390/biom12121752. This article has 15 citations.

3. (sachan2023notchsignallingmultifaceted pages 4-4): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

4. (sachan2023notchsignallingmultifaceted pages 2-2): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

5. (pinot2024spatiotemporalregulationof pages 2-4): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

6. (lv2024evolutionandfunction pages 2-4): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

7. (bray2025modesofnotch pages 24-27): Sarah J. Bray and Anna Bigas. Modes of notch signalling in development and disease. Nature reviews. Molecular cell biology, 26:522-537, Mar 2025. URL: https://doi.org/10.1038/s41580-025-00835-2, doi:10.1038/s41580-025-00835-2. This article has 63 citations.

8. (sachan2023notchsignallingmultifaceted pages 8-8): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

9. (sachan2023notchsignallingmultifaceted pages 7-8): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

10. (sachan2023notchsignallingmultifaceted pages 10-11): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

11. (lv2024evolutionandfunction pages 4-6): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

12. (sachan2023notchsignallingmultifaceted pages 7-7): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

13. (pinot2024spatiotemporalregulationof pages 13-15): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

14. (bray2025modesofnotch pages 27-33): Sarah J. Bray and Anna Bigas. Modes of notch signalling in development and disease. Nature reviews. Molecular cell biology, 26:522-537, Mar 2025. URL: https://doi.org/10.1038/s41580-025-00835-2, doi:10.1038/s41580-025-00835-2. This article has 63 citations.

15. (nurmahdi2022notchmissensemutations pages 14-15): Hilman Nurmahdi, Mao Hasegawa, Elzava Yuslimatin Mujizah, Takeshi Sasamura, Mikiko Inaki, Shinya Yamamoto, Tomoko Yamakawa, and Kenji Matsuno. Notch missense mutations in drosophila reveal functions of specific egf-like repeats in notch folding, trafficking, and signaling. Biomolecules, 12:1752, Nov 2022. URL: https://doi.org/10.3390/biom12121752, doi:10.3390/biom12121752. This article has 15 citations.

16. (sachan2023notchsignallingmultifaceted pages 4-5): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

17. (pinot2024spatiotemporalregulationof pages 7-8): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

18. (pinot2024spatiotemporalregulationof pages 4-6): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

19. (katz2025autophagycontrolsdifferentiation pages 8-10): Maximiliano J. Katz, Felipe Rodríguez, Fermín Evangelisti, Agustina G. Borrat, Sebastián Perez-Pandolfo, Tomás Peters, Natalia Sommario, Graciela L. Boccaccio, Mariana Melani, and Pablo Wappner. Autophagy controls differentiation of drosophila blood cells by regulating notch levels in response to nutrient availability. Jul 2025. URL: https://doi.org/10.1038/s41467-025-58389-y, doi:10.1038/s41467-025-58389-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

20. (sachan2023notchsignallingmultifaceted pages 22-22): Nalani Sachan, Vartika Sharma, Mousumi Mutsuddi, and Ashim Mukherjee. Notch signalling: multifaceted role in development and disease. The FEBS Journal, 291:3030-3059, May 2024. URL: https://doi.org/10.1111/febs.16815, doi:10.1111/febs.16815. This article has 124 citations.

21. (pinot2024spatiotemporalregulationof pages 6-7): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

22. (chen2025thedrosophilahistone pages 1-2): Yao Chen, Xinyue Zhang, Yu Song, Jie Shen, and Junzheng Zhang. The drosophila histone variant h2av facilitates notch signaling activity in a two-tier regulatory fashion. Cell Communication and Signaling : CCS, Jul 2025. URL: https://doi.org/10.1186/s12964-025-02333-6, doi:10.1186/s12964-025-02333-6. This article has 1 citations.

23. (chen2025thedrosophilahistone pages 5-7): Yao Chen, Xinyue Zhang, Yu Song, Jie Shen, and Junzheng Zhang. The drosophila histone variant h2av facilitates notch signaling activity in a two-tier regulatory fashion. Cell Communication and Signaling : CCS, Jul 2025. URL: https://doi.org/10.1186/s12964-025-02333-6, doi:10.1186/s12964-025-02333-6. This article has 1 citations.

24. (lv2024evolutionandfunction pages 25-26): Yan Lv, Xuan Pang, Zhonghong Cao, Changping Song, Baohua Liu, Weiwei Wu, and Qiuxiang Pang. Evolution and function of the notch signaling pathway: an invertebrate perspective. International Journal of Molecular Sciences, 25:3322, Mar 2024. URL: https://doi.org/10.3390/ijms25063322, doi:10.3390/ijms25063322. This article has 36 citations.

25. (chen2023notchsignalingin pages 2-4): Yao Chen, Haomiao Li, Tian-Ci Yi, Jie Shen, and Junzheng Zhang. Notch signaling in insect development: a simple pathway with diverse functions. International Journal of Molecular Sciences, 24:14028, Sep 2023. URL: https://doi.org/10.3390/ijms241814028, doi:10.3390/ijms241814028. This article has 35 citations.

26. (megaly2023notchsignallingplays pages 7-9): Marvel Megaly, Gregory Foran, Arsala Ali, Anel Turgambayeva, Ryan D. Hallam, and Aleksandar Necakov. Notch signalling plays a critical role in patterning the ventral mesoderm during early embryogenesis in drosophila melanogaster. bioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.27.558900, doi:10.1101/2023.09.27.558900. This article has 0 citations.

27. (megaly2026notchsignallingplays pages 6-9): Marvel Megaly, Gregory Foran, Arsala Ali, Anel Turgambayeva, Ryan D. Hallam, Ping Liang, and Aleksandar Necakov. Notch signalling plays a role in patterning the ventral mesoderm during early embryogenesis in drosophila melanogaster. Unknown journal, Apr 2026. URL: https://doi.org/10.21203/rs.3.rs-4119428/v1, doi:10.21203/rs.3.rs-4119428/v1.

28. (bray2025modesofnotch pages 1-3): Sarah J. Bray and Anna Bigas. Modes of notch signalling in development and disease. Nature reviews. Molecular cell biology, 26:522-537, Mar 2025. URL: https://doi.org/10.1038/s41580-025-00835-2, doi:10.1038/s41580-025-00835-2. This article has 63 citations.

29. (yasugi2022mathematicalmodelingof pages 7-8): Tetsuo Yasugi and Makoto Sato. Mathematical modeling of notch dynamics in drosophila neural development. Fly, 16:24-36, Oct 2022. URL: https://doi.org/10.1080/19336934.2021.1953363, doi:10.1080/19336934.2021.1953363. This article has 10 citations and is from a peer-reviewed journal.

30. (yasugi2022mathematicalmodelingof pages 1-2): Tetsuo Yasugi and Makoto Sato. Mathematical modeling of notch dynamics in drosophila neural development. Fly, 16:24-36, Oct 2022. URL: https://doi.org/10.1080/19336934.2021.1953363, doi:10.1080/19336934.2021.1953363. This article has 10 citations and is from a peer-reviewed journal.

31. (bray2025modesofnotch pages 3-5): Sarah J. Bray and Anna Bigas. Modes of notch signalling in development and disease. Nature reviews. Molecular cell biology, 26:522-537, Mar 2025. URL: https://doi.org/10.1038/s41580-025-00835-2, doi:10.1038/s41580-025-00835-2. This article has 63 citations.

32. (chen2023notchsignalingin pages 16-17): Yao Chen, Haomiao Li, Tian-Ci Yi, Jie Shen, and Junzheng Zhang. Notch signaling in insect development: a simple pathway with diverse functions. International Journal of Molecular Sciences, 24:14028, Sep 2023. URL: https://doi.org/10.3390/ijms241814028, doi:10.3390/ijms241814028. This article has 35 citations.

33. (pinot2024spatiotemporalregulationof pages 1-2): Mathieu Pinot and Roland Le Borgne. Spatio-temporal regulation of notch activation in asymmetrically dividing sensory organ precursor cells in drosophila melanogaster epithelium. Cells, 13:1133, Jun 2024. URL: https://doi.org/10.3390/cells13131133, doi:10.3390/cells13131133. This article has 3 citations.

34. (megaly2023notchsignallingplays pages 1-3): Marvel Megaly, Gregory Foran, Arsala Ali, Anel Turgambayeva, Ryan D. Hallam, and Aleksandar Necakov. Notch signalling plays a critical role in patterning the ventral mesoderm during early embryogenesis in drosophila melanogaster. bioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.27.558900, doi:10.1101/2023.09.27.558900. This article has 0 citations.

35. (revici2022e3ubiquitinligase pages 10-12): Raluca Revici, Samira Hosseini-Alghaderi, Fabienne Haslam, Rory Whiteford, and Martin Baron. E3 ubiquitin ligase regulators of notch receptor endocytosis: from flies to humans. Biomolecules, 12:224, Jan 2022. URL: https://doi.org/10.3390/biom12020224, doi:10.3390/biom12020224. This article has 25 citations.

36. (sarkar2025regulationofnotch pages 18-22): Bappi Sarkar, Jyoti Singh, Dipti Verma, Mousumi Mutsuddi, and Ashim Mukherjee. Regulation of notch signaling by multiple ankyrin repeat containing protein mask. Cell Communication and Signaling : CCS, Jul 2025. URL: https://doi.org/10.1186/s12964-025-02190-3, doi:10.1186/s12964-025-02190-3. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](N-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](N-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](N-deep-research-falcon_artifacts/artifact-02.md)

## Citations

1. nurmahdi2022notchmissensemutations pages 1-2
2. pinot2024spatiotemporalregulationof pages 2-4
3. sachan2023notchsignallingmultifaceted pages 8-8
4. pinot2024spatiotemporalregulationof pages 6-7
5. lv2024evolutionandfunction pages 4-6
6. sachan2023notchsignallingmultifaceted pages 4-4
7. pinot2024spatiotemporalregulationof pages 1-2
8. lv2024evolutionandfunction pages 25-26
9. chen2023notchsignalingin pages 16-17
10. megaly2023notchsignallingplays pages 1-3
11. katz2025autophagycontrolsdifferentiation pages 8-10
12. sarkar2025regulationofnotch pages 18-22
13. sachan2023notchsignallingmultifaceted pages 10-11
14. sachan2023notchsignallingmultifaceted pages 1-2
15. sachan2023notchsignallingmultifaceted pages 2-2
16. lv2024evolutionandfunction pages 2-4
17. bray2025modesofnotch pages 24-27
18. sachan2023notchsignallingmultifaceted pages 7-8
19. sachan2023notchsignallingmultifaceted pages 7-7
20. pinot2024spatiotemporalregulationof pages 13-15
21. bray2025modesofnotch pages 27-33
22. nurmahdi2022notchmissensemutations pages 14-15
23. sachan2023notchsignallingmultifaceted pages 4-5
24. pinot2024spatiotemporalregulationof pages 7-8
25. pinot2024spatiotemporalregulationof pages 4-6
26. sachan2023notchsignallingmultifaceted pages 22-22
27. chen2025thedrosophilahistone pages 1-2
28. chen2025thedrosophilahistone pages 5-7
29. chen2023notchsignalingin pages 2-4
30. megaly2023notchsignallingplays pages 7-9
31. megaly2026notchsignallingplays pages 6-9
32. bray2025modesofnotch pages 1-3
33. yasugi2022mathematicalmodelingof pages 7-8
34. yasugi2022mathematicalmodelingof pages 1-2
35. bray2025modesofnotch pages 3-5
36. Su(H)
37. E(spl)
38. Su(H)/CSL
39. https://doi.org/10.1111/febs.16815,
40. https://doi.org/10.3390/biom12121752,
41. https://doi.org/10.3390/cells13131133,
42. https://doi.org/10.3390/ijms25063322,
43. https://doi.org/10.1038/s41580-025-00835-2,
44. https://doi.org/10.1038/s41467-025-58389-y,
45. https://doi.org/10.1186/s12964-025-02333-6,
46. https://doi.org/10.3390/ijms241814028,
47. https://doi.org/10.1101/2023.09.27.558900,
48. https://doi.org/10.21203/rs.3.rs-4119428/v1,
49. https://doi.org/10.1080/19336934.2021.1953363,
50. https://doi.org/10.3390/biom12020224,
51. https://doi.org/10.1186/s12964-025-02190-3,