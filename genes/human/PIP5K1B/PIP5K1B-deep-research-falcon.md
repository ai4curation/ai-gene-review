---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T05:38:57.567062'
end_time: '2026-06-20T05:53:04.856394'
duration_seconds: 847.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PIP5K1B
  gene_symbol: PIP5K1B
  uniprot_accession: O14986
  protein_description: 'RecName: Full=Phosphatidylinositol 4-phosphate 5-kinase type-1
    beta {ECO:0000305|PubMed:8955136}; Short=PIP5K1-beta {ECO:0000303|PubMed:8955136};
    Short=PtdIns(4)P-5-kinase 1 beta {ECO:0000305|PubMed:8955136}; EC=2.7.1.68 {ECO:0000250|UniProtKB:P70181};
    AltName: Full=Phosphatidylinositol 4-phosphate 5-kinase type I beta {ECO:0000305|PubMed:8955136};
    Short=PIP5KIbeta {ECO:0000303|PubMed:8955136}; AltName: Full=Protein STM-7 {ECO:0000303|PubMed:8841185};
    AltName: Full=Type I phosphatidylinositol 4-phosphate 5-kinase beta {ECO:0000305|PubMed:8955136};'
  gene_info: Name=PIP5K1B {ECO:0000312|HGNC:HGNC:8995}; Synonyms=STM7 {ECO:0000303|PubMed:8841185};
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: PInositol-4-P-4/5-kinase_C_sf. (IPR027483); PInositol-4-P-4/5-kinase_core.
    (IPR002498); PInositol-4-P-5-kinase_N. (IPR027484); PInositol-4/5-P-5/4-kinase.
    (IPR023610); PIP5K (PF01504)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PIP5K1B-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** O14986
- **Protein Description:** RecName: Full=Phosphatidylinositol 4-phosphate 5-kinase type-1 beta {ECO:0000305|PubMed:8955136}; Short=PIP5K1-beta {ECO:0000303|PubMed:8955136}; Short=PtdIns(4)P-5-kinase 1 beta {ECO:0000305|PubMed:8955136}; EC=2.7.1.68 {ECO:0000250|UniProtKB:P70181}; AltName: Full=Phosphatidylinositol 4-phosphate 5-kinase type I beta {ECO:0000305|PubMed:8955136}; Short=PIP5KIbeta {ECO:0000303|PubMed:8955136}; AltName: Full=Protein STM-7 {ECO:0000303|PubMed:8841185}; AltName: Full=Type I phosphatidylinositol 4-phosphate 5-kinase beta {ECO:0000305|PubMed:8955136};
- **Gene Information:** Name=PIP5K1B {ECO:0000312|HGNC:HGNC:8995}; Synonyms=STM7 {ECO:0000303|PubMed:8841185};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PInositol-4-P-4/5-kinase_C_sf. (IPR027483); PInositol-4-P-4/5-kinase_core. (IPR002498); PInositol-4-P-5-kinase_N. (IPR027484); PInositol-4/5-P-5/4-kinase. (IPR023610); PIP5K (PF01504)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PIP5K1B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PIP5K1B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PIP5K1B** (gene ID: PIP5K1B, UniProt: O14986) in human.

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
- **UniProt Accession:** O14986
- **Protein Description:** RecName: Full=Phosphatidylinositol 4-phosphate 5-kinase type-1 beta {ECO:0000305|PubMed:8955136}; Short=PIP5K1-beta {ECO:0000303|PubMed:8955136}; Short=PtdIns(4)P-5-kinase 1 beta {ECO:0000305|PubMed:8955136}; EC=2.7.1.68 {ECO:0000250|UniProtKB:P70181}; AltName: Full=Phosphatidylinositol 4-phosphate 5-kinase type I beta {ECO:0000305|PubMed:8955136}; Short=PIP5KIbeta {ECO:0000303|PubMed:8955136}; AltName: Full=Protein STM-7 {ECO:0000303|PubMed:8841185}; AltName: Full=Type I phosphatidylinositol 4-phosphate 5-kinase beta {ECO:0000305|PubMed:8955136};
- **Gene Information:** Name=PIP5K1B {ECO:0000312|HGNC:HGNC:8995}; Synonyms=STM7 {ECO:0000303|PubMed:8841185};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** PInositol-4-P-4/5-kinase_C_sf. (IPR027483); PInositol-4-P-4/5-kinase_core. (IPR002498); PInositol-4-P-5-kinase_N. (IPR027484); PInositol-4/5-P-5/4-kinase. (IPR023610); PIP5K (PF01504)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PIP5K1B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PIP5K1B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PIP5K1B** (gene ID: PIP5K1B, UniProt: O14986) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Comprehensive Research Report: PIP5K1B Gene Function and Annotation

### Gene Identity and Classification

PIP5K1B (phosphatidylinositol 4-phosphate 5-kinase type-1 beta, UniProt O14986) encodes a Type I phosphatidylinositol phosphate kinase, also referred to as PIP5Kβ, PIP5KIβ, or by the older synonym STM-7. This gene is one of three paralogs in the human Type I PIP5K family, alongside PIP5K1A and PIP5K1C (jin2023lipidkinasespip5ks pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2). Type I PIP5Ks are lipid kinases responsible for generating the majority of phosphatidylinositol 4,5-bisphosphate [PI(4,5)P2] at the plasma membrane in eukaryotic cells, distinguishing them from Type II PIPKs (PIP4Ks), which preferentially use phosphatidylinositol 5-phosphate as substrate (muftuoglu2016mechanismofsubstrate pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, balla2013phosphoinositidestinylipids pages 1-2).

### Enzymatic Function and Catalytic Mechanism

**Primary Catalytic Reaction:** PIP5K1B catalyzes the phosphorylation of phosphatidylinositol 4-phosphate (PI4P, PtdIns4P) to generate phosphatidylinositol 4,5-bisphosphate [PI(4,5)P2, PtdIns(4,5)P2] using ATP as the phosphate donor (roy2023pip5k1cphosphoinositidekinase pages 1-2, muftuoglu2016mechanismofsubstrate pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2). Specifically, the enzyme transfers a phosphate group to the 5-position of the inositol ring of PI4P, yielding the bis-phosphorylated product PI(4,5)P2 and ADP (muftuoglu2016mechanismofsubstrate pages 1-2, balla2013phosphoinositidestinylipids pages 1-2). This reaction represents the major synthetic route for cellular PI(4,5)P2, with Type I PIP5Ks producing the dominant pool of this critical signaling lipid at the plasma membrane (hansen2022membranemediateddimerizationpotentiates pages 1-2, balla2013phosphoinositidestinylipids pages 2-3).

**Substrate Specificity:** PIP5K1B exhibits primary specificity for PI4P as its physiological substrate, phosphorylating the 5-position hydroxyl group of the inositol headgroup (muftuoglu2016mechanismofsubstrate pages 1-2, liu2016theactivationloop pages 1-1). Crystallographic and mutagenesis studies on Type I PIP5K family members have revealed that substrate specificity is determined by two key structural elements: a specialized "specificity loop" (also called the activation loop) and a conserved monophosphate-binding site that recognizes the 4-phosphate moiety of PI4P (muftuoglu2016mechanismofsubstrate pages 1-2, liu2016theactivationloop pages 1-1). While in vitro studies show that Type I PIP5Ks can also phosphorylate phosphatidylinositol 3-phosphate (PI3P) to generate PI(3,4)P2 and PI(3,5)P2, PI4P remains the predominant cellular substrate for PI(4,5)P2 synthesis (muftuoglu2016mechanismofsubstrate pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2).

**Structural and Mechanistic Insights:** PIP5K1B belongs to the PIPK family of lipid kinases, which possess a catalytic domain with a protein kinase-like fold distinct from classical serine/threonine or tyrosine kinases (muftuoglu2016mechanismofsubstrate pages 1-2, hu2015resolutionofstructure pages 1-2). Crystal structures of Type I PIP5Ks reveal that these enzymes form side-to-side dimers, and dimerization enhances catalytic efficiency through mechanisms consistent with allosteric regulation (hansen2022membranemediateddimerizationpotentiates pages 1-2, hu2015resolutionofstructure pages 1-2). The enzyme requires membrane association for activity, and this membrane docking is mediated by an activation loop that functions as a membrane sensor (liu2016theactivationloop pages 1-1). NMR studies have shown that the activation loop, which is disordered in crystal structures, folds into an amphipathic helix upon association with membrane surfaces, and the hydrophobic face of this helix is essential for both kinase activity and membrane sensing (liu2016theactivationloop pages 1-1). The membrane-bound kinase can undergo protein density-dependent dimerization, which potentiates lipid kinase activity and creates a broad dynamic range of enzymatic activities coupled to the local density of PI(4,5)P2 and membrane-bound enzyme (hansen2022membranemediateddimerizationpotentiates pages 1-2).

### Subcellular Localization and Functional Compartmentalization

PIP5K1B localizes primarily to the cytoplasmic face of the plasma membrane, where it carries out its principal function of generating PI(4,5)P2 (hansen2022membranemediateddimerizationpotentiates pages 1-2, wen2023regulationofphosphoinositide pages 1-3, balla2013phosphoinositidestinylipids pages 2-3). Studies of Type I PIP5K family members consistently demonstrate that these enzymes are targeted to the plasma membrane through multiple mechanisms: substrate recognition, electrostatic interactions with anionic lipids, and positive feedback through cooperative binding to their PI(4,5)P2 product (hansen2022membranemediateddimerizationpotentiates pages 1-2). Single-molecule studies on human PIP5KB have revealed that the enzyme exhibits cooperative membrane association with PI(4,5)P2-containing membranes, establishing a positive feedback loop during the PI4P phosphorylation reaction (hansen2022membranemediateddimerizationpotentiates pages 1-2). The amphipathic activation loop serves as a critical membrane sensor, enabling the kinase to detect and bind to membrane surfaces in an orientation conducive to lipid substrate processing (liu2016theactivationloop pages 1-1). While Type I PIP5K isoforms share plasma membrane localization, they may exhibit distinct spatiotemporal regulation and subcellular distributions that allow for isoform-specific functions (roy2023pip5k1cphosphoinositidekinase pages 1-2, kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2).

### Signaling and Biochemical Pathways

PIP5K1B functions within multiple interconnected signaling pathways through the generation and regulation of PI(4,5)P2 levels at the plasma membrane.

**PI3K/Akt Signaling Pathway:** PI(4,5)P2 produced by PIP5K1B serves as the immediate substrate for class I phosphatidylinositol 3-kinases (PI3Ks), which phosphorylate PI(4,5)P2 at the 3-position to generate phosphatidylinositol 3,4,5-trisphosphate [PI(3,4,5)P3, PIP3] (jin2023lipidkinasespip5ks pages 1-2, dieterle2014pdk1controlsupstream pages 1-2, balla2013phosphoinositidestinylipids pages 1-2). This conversion is central to the PI3K/Akt pathway, which regulates cell growth, proliferation, survival, and metabolism (dieterle2014pdk1controlsupstream pages 1-2). Studies have demonstrated that PIP5K activity influences PI3K signaling output by controlling substrate availability; for example, PDK1 (a downstream effector in this pathway) can negatively regulate PI3K class IA subunit expression through transcriptional feedback, and this regulation is modulated by PIP5K-dependent PI(4,5)P2 generation and PIP5K protein stability (dieterle2014pdk1controlsupstream pages 1-2, jin2023lipidkinasespip5ks pages 5-6). The PI3K/Akt pathway is frequently dysregulated in cancer, and recent literature identifies PIP5K family members, including PIP5K1B, as potential therapeutic targets in malignancies such as breast cancer (jin2023lipidkinasespip5ks pages 1-2, jin2023lipidkinasespip5ks pages 5-6).

**Phospholipase C Signaling:** PI(4,5)P2 at the plasma membrane is the substrate for phospholipase C (PLC) enzymes, which cleave PI(4,5)P2 to generate two critical second messengers: inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) (balla2013phosphoinositidestinylipids pages 1-2, balla2013phosphoinositidestinylipids pages 2-3). This pathway is activated downstream of G protein-coupled receptors (GPCRs) and receptor tyrosine kinases (RTKs), initiating calcium signaling and protein kinase C activation (balla2013phosphoinositidestinylipids pages 1-2). By controlling the plasma membrane pool of PI(4,5)P2, PIP5K1B indirectly regulates the magnitude and duration of PLC-mediated signaling responses.

**Actin Cytoskeleton Regulation:** PI(4,5)P2 plays a pivotal role in reorganizing the actin cytoskeleton in response to extracellular signals (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2, wen2023regulationofphosphoinositide pages 1-3, hou2025phosphoinositidesignalingat pages 1-2). The lipid directly binds to and regulates numerous actin-binding proteins, modulating actin polymerization, filament capping, and cross-linking. PI(4,5)P2 is essential for the formation and dynamics of cellular protrusions such as lamellipodia and filopodia, which are critical for cell migration (peng2021clic1recruitspip5k1ac pages 1-2, wen2023regulationofphosphoinositide pages 1-3, hou2025phosphoinositidesignalingat pages 1-2). Recent studies have shown that PIP5K recruitment to the leading edge of migrating cells generates PI(4,5)P2-rich microdomains that coordinate the extension of actin filaments and the formation of integrin-mediated cell-matrix adhesions (peng2021clic1recruitspip5k1ac pages 1-2). Specifically, membrane-targeted proteins can recruit PIP5Ks (including PIP5K1A and PIP5K1C) from the cytoplasm to the plasma membrane, where they locally produce PI(4,5)P2 to induce nascent adhesion formation and signaling for cytoskeleton extension during directional migration and tumor invasion (peng2021clic1recruitspip5k1ac pages 1-2).

**T-cell Receptor Signaling and Immunological Synapse Formation:** PIP5K1B (PIP5Kβ) has been shown to play a specific, non-redundant role in T lymphocyte activation through its function at the immunological synapse (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2). PI(4,5)P2 is critical for T-cell activation, serving both as a substrate for second messenger generation and as a regulator of actin cytoskeleton remodeling necessary for clustering lipid rafts, T-cell receptors, and costimulatory molecules at the T cell-antigen presenting cell interface (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2). Studies demonstrate that CD28 costimulation induces the recruitment of PIP5Kβ to the immunological synapse, where it regulates filamin A (FLNA) and lipid raft accumulation, as well as overall T-cell activation, in a manner that is not compensated by other PIP5K isoforms (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2). The functional specificity of PIP5Kβ in this context depends on interactions with the guanine nucleotide exchange factor Vav1 and the C-terminal region of PIP5Kβ (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2).

**Endocytosis and Vesicle Trafficking:** PI(4,5)P2 is a key regulator of endocytic processes, particularly clathrin-mediated endocytosis (wen2023regulationofphosphoinositide pages 1-3, balla2013phosphoinositidestinylipids pages 1-2, balla2013phosphoinositidestinylipids pages 2-3). The lipid recruits adaptor proteins and regulates the dynamics of endocytic vesicle formation and scission. Phosphoinositide signaling, including PIP5K-mediated PI(4,5)P2 generation, controls membrane dynamics and vesicular trafficking at multiple intracellular compartments (balla2013phosphoinositidestinylipids pages 1-2, baba2020emergingrolesof pages 1-2). Recent evidence also indicates roles for PI4P and PI(4,5)P2 in regulating multiple steps of autophagy, including autophagosome-lysosome fusion and reformation processes (baba2020emergingrolesof pages 1-2).

**Ion Channel and Receptor Regulation:** PI(4,5)P2 directly modulates the activity of numerous ion channels, pumps, and transporters at the plasma membrane (balla2013phosphoinositidestinylipids pages 1-2, balla2013phosphoinositidestinylipids pages 2-3). Many channels require PI(4,5)P2 binding for proper gating and function, and changes in local PI(4,5)P2 levels mediated by PIP5K activity can rapidly alter channel activity.

### Biological Processes and Cellular Functions

Through the generation of PI(4,5)P2, PIP5K1B participates in a wide array of biological processes central to cellular physiology:

1. **Cell Motility and Migration:** PI(4,5)P2 produced by PIP5Ks drives the formation of membrane protrusions and cell-matrix adhesions essential for directional cell migration (peng2021clic1recruitspip5k1ac pages 1-2, wen2023regulationofphosphoinositide pages 1-3, hou2025phosphoinositidesignalingat pages 1-2). The spatiotemporal coordination of PIP5K activity at the leading edge enables cells to extend lamellipodia/invadopodia and form nascent integrin-based adhesions (peng2021clic1recruitspip5k1ac pages 1-2).

2. **Cell Adhesion:** PIP5K-mediated PI(4,5)P2 synthesis regulates the formation and dynamics of cell-matrix adhesions by recruiting adhesion-complex components such as talin to the plasma membrane and activating integrin signaling (peng2021clic1recruitspip5k1ac pages 1-2, hou2025phosphoinositidesignalingat pages 1-2).

3. **Immune Cell Function:** In T lymphocytes, PIP5Kβ controls the organization of the immunological synapse, including the recruitment of lipid rafts and signaling molecules necessary for effective T-cell activation and immune responses (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2).

4. **Membrane Trafficking:** PI(4,5)P2 regulates both endocytic and exocytic processes, controlling vesicle formation, trafficking, and fusion events throughout the endomembrane system (balla2013phosphoinositidestinylipids pages 1-2, balla2013phosphoinositidestinylipids pages 2-3, baba2020emergingrolesof pages 1-2).

5. **Signal Transduction:** As the substrate for PI3K and PLC, PI(4,5)P2 is positioned at a critical node in multiple receptor-mediated signaling cascades that control cell fate decisions, proliferation, survival, and metabolism (jin2023lipidkinasespip5ks pages 1-2, dieterle2014pdk1controlsupstream pages 1-2, balla2013phosphoinositidestinylipids pages 1-2).

### Disease Relevance and Recent Developments

Recent literature highlights the involvement of PIP5K family members, including PIP5K1B, in cancer biology and other diseases. A 2023 review identifies PIP5Ks and PIP4Ks as potential drug targets for breast cancer treatment, noting that the PI(4,5)P2 signaling axis is frequently dysregulated in malignancies (jin2023lipidkinasespip5ks pages 1-2). The review emphasizes that PI(4,5)P2 serves as a key activator of the frequently altered PI3K pathway in breast cancer, and that aberrant phosphoinositide metabolism contributes to tumor progression, metastasis, and drug resistance (jin2023lipidkinasespip5ks pages 1-2, jin2023lipidkinasespip5ks pages 5-6). Studies have also demonstrated that PIP5K activity is involved in cancer cell migration and invasion through the regulation of cytoskeletal dynamics and adhesion complexes (jin2023lipidkinasespip5ks pages 5-6, peng2021clic1recruitspip5k1ac pages 1-2). More broadly, dysregulation of phosphoinositide signaling has been implicated in diverse diseases including neurological disorders, metabolic diseases, and immune dysfunction (balla2013phosphoinositidestinylipids pages 1-2). A 2025 review discusses how phosphoinositide signaling at the cytoskeleton regulates cell dynamics, and how its dysregulation is implicated in diseases including cancer, highlighting therapeutic opportunities through targeted modulation of these pathways (hou2025phosphoinositidesignalingat pages 1-2).

### Summary

PIP5K1B is a Type I phosphatidylinositol 4-phosphate 5-kinase that catalyzes the ATP-dependent phosphorylation of PI4P to generate PI(4,5)P2, the predominant signaling phosphoinositide at the plasma membrane. The enzyme localizes to the cytoplasmic face of the plasma membrane, where it uses an amphipathic activation loop as a membrane sensor to dock and process lipid substrates. Through the generation of PI(4,5)P2, PIP5K1B functions in multiple interconnected signaling pathways including PI3K/Akt signaling, phospholipase C signaling, actin cytoskeleton regulation, endocytosis, and ion channel modulation. PIP5Kβ plays specific roles in T-cell receptor signaling and immunological synapse formation, demonstrating functional specialization among the three Type I PIP5K isoforms. The enzyme's regulation of PI(4,5)P2 levels is critical for cell migration, adhesion, membrane trafficking, and signal transduction. Recent research has identified PIP5K family members as potential therapeutic targets in cancer and other diseases characterized by dysregulated phosphoinositide metabolism.

| Feature | Description/Details (with citations) |
|---|---|
| Gene nomenclature | **Official human gene:** **PIP5K1B**; **protein:** phosphatidylinositol 4-phosphate 5-kinase type-1 beta / PIP5K1B / PIP5Kβ / PIP5KIβ; older synonym **STM7** is also associated with this beta isoform in the supplied target definition. The human Type I PIP5K family comprises three paralogs: **PIP5K1A, PIP5K1B, and PIP5K1C** (jin2023lipidkinasespip5ks pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, hu2015resolutionofstructure pages 1-2). |
| Protein classification and family | PIP5K1B is a **Type I phosphatidylinositol phosphate kinase (PIP5K)**, i.e., a **lipid kinase** in the broader **PIPK family**. Type I PIPKs are the principal enzymes that synthesize most cellular and plasma-membrane **PI(4,5)P2** from **PI4P**, distinguishing them from Type II PIPKs/PIP4Ks, which mainly use **PI5P** as substrate (muftuoglu2016mechanismofsubstrate pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, balla2013phosphoinositidestinylipids pages 1-2). |
| Enzymatic reaction catalyzed | Canonical reaction: **phosphatidylinositol 4-phosphate [PI4P/PtdIns4P] + ATP → phosphatidylinositol 4,5-bisphosphate [PI(4,5)P2/PtdIns(4,5)P2] + ADP**. This is the defining reaction of Type I PIP5Ks and is the major synthetic route for PI(4,5)P2 in most cells (roy2023pip5k1cphosphoinositidekinase pages 1-2, muftuoglu2016mechanismofsubstrate pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, hu2015resolutionofstructure pages 1-2). |
| Substrate specificity | Primary physiological substrate is **PI4P**, phosphorylated at the **5-position** of the inositol ring. Structural/biochemical studies of Type I PIPKs show that substrate specificity is determined by a specialized **specificity loop/activation loop** and a **monophosphate-binding site**; in vitro, Type I PIPKs can also show activity toward **PI3P**, but PI4P is the main cellular substrate for PI(4,5)P2 production (muftuoglu2016mechanismofsubstrate pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, liu2016theactivationloop pages 1-1). |
| Primary subcellular localization | Type I PIP5Ks function mainly at the **cytoplasmic face of the plasma membrane**, where they generate the dominant pool of **PI(4,5)P2**. Family studies emphasize membrane docking through substrate recognition, electrostatic interactions with anionic lipids, and product-assisted membrane association; recent work on human PIP5KB specifically discusses cooperative membrane association on PI(4,5)P2-containing membranes (muftuoglu2016mechanismofsubstrate pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, wen2023regulationofphosphoinositide pages 1-3). |
| Key structural features | PIP5K1B is expected to share the conserved **PIPK catalytic core** of Type I PIP5Ks, including a **protein-kinase-like fold**, a **specificity/activation loop** important for lipid-substrate recognition and localization, and a **membrane-sensing amphipathic helix behavior** within that activation loop. Structural work on Type I PIPKs also shows **side-to-side dimerization** that can enhance catalytic efficiency/allosteric regulation (liu2016theactivationloop pages 1-1, hu2015resolutionofstructure pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2). |
| Major signaling pathways involved | Through generation of **PI(4,5)P2**, PIP5K1B feeds multiple pathways: **(1) PI3K-Akt signaling**, because PI(4,5)P2 is the substrate for class I PI3K to make **PI(3,4,5)P3**; **(2) PLC signaling**, because PI(4,5)P2 is cleaved to IP3 and DAG; **(3) membrane/cytoskeleton signaling**, including actin remodeling, endocytosis, and receptor signaling; and **(4) T-cell signaling**, where PIP5Kβ has a nonredundant role in immunological synapse organization (dieterle2014pdk1controlsupstream pages 1-2, kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, balla2013phosphoinositidestinylipids pages 1-2). |
| Biological processes regulated | PI(4,5)P2 produced by Type I PIP5Ks regulates **actin cytoskeleton organization**, **lipid raft dynamics**, **immunological synapse assembly**, **endocytosis/exocytosis**, **ion channel and transporter regulation**, **vesicular trafficking**, and **cell migration/adhesion**. In T cells, PIP5Kβ controls recruitment of **lipid rafts** and **filamin A** to the immunological synapse; more broadly, phosphoinositide signaling organizes membrane–cytosol interfaces controlling motility and adhesion (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2, hansen2022membranemediateddimerizationpotentiates pages 1-2, wen2023regulationofphosphoinositide pages 1-3, hou2025phosphoinositidesignalingat pages 1-2). |
| Disease associations mentioned in recent literature | Recent literature links the **PIP5K/PIP4K axis** to **cancer biology** and drug targeting, especially via altered PI(4,5)P2/PI3K signaling. A 2023 review identifies PIP5K family members as potential **drug targets in breast cancer**; broader phosphoinositide literature connects these enzymes to malignant signaling, trafficking, and cytoskeletal dysregulation. While recent papers more often emphasize **PIP5K1A** or **PIP5K1C**, PIP5K1B is part of the same disease-relevant enzymatic network and has been noted in cancer-cell phosphoinositide studies (jin2023lipidkinasespip5ks pages 1-2, jin2023lipidkinasespip5ks pages 5-6, wen2023regulationofphosphoinositide pages 1-3). |


*Table: This table compiles the key functional annotation points for human PIP5K1B, including nomenclature, enzyme activity, localization, structural features, pathways, and disease relevance. It is useful as a concise evidence-backed reference for interpreting the protein’s primary biochemical role.*

References

1. (jin2023lipidkinasespip5ks pages 1-2): Yue Jin and Jian Xue. Lipid kinases pip5ks and pip4ks: potential drug targets for breast cancer. Frontiers in Oncology, Dec 2023. URL: https://doi.org/10.3389/fonc.2023.1323897, doi:10.3389/fonc.2023.1323897. This article has 11 citations.

2. (hansen2022membranemediateddimerizationpotentiates pages 1-2): Scott D Hansen, Albert A Lee, Benjamin R Duewell, and Jay T Groves. Membrane-mediated dimerization potentiates pip5k lipid kinase activity. Aug 2022. URL: https://doi.org/10.7554/elife.73747, doi:10.7554/elife.73747. This article has 36 citations and is from a domain leading peer-reviewed journal.

3. (muftuoglu2016mechanismofsubstrate pages 1-2): Yagmur Muftuoglu, Yi Xue, Xiang Gao, Dianqing Wu, and Ya Ha. Mechanism of substrate specificity of phosphatidylinositol phosphate kinases. Proceedings of the National Academy of Sciences, 113:8711-8716, Jul 2016. URL: https://doi.org/10.1073/pnas.1522112113, doi:10.1073/pnas.1522112113. This article has 49 citations and is from a highest quality peer-reviewed journal.

4. (balla2013phosphoinositidestinylipids pages 1-2): T. Balla. Phosphoinositides: tiny lipids with giant impact on cell regulation. Physiological reviews, 93 3:1019-137, Jul 2013. URL: https://doi.org/10.1152/physrev.00028.2012, doi:10.1152/physrev.00028.2012. This article has 1987 citations and is from a highest quality peer-reviewed journal.

5. (roy2023pip5k1cphosphoinositidekinase pages 1-2): Ajit Roy, Arup R. Chakraborty, Tyzoon Nomanbhoy, and Melvin L. DePamphilis. Pip5k1c phosphoinositide kinase deficiency distinguishes pikfyve-dependent cancer cells from non-malignant cells. Mar 2023. URL: https://doi.org/10.1080/15548627.2023.2182594, doi:10.1080/15548627.2023.2182594. This article has 14 citations and is from a domain leading peer-reviewed journal.

6. (balla2013phosphoinositidestinylipids pages 2-3): T. Balla. Phosphoinositides: tiny lipids with giant impact on cell regulation. Physiological reviews, 93 3:1019-137, Jul 2013. URL: https://doi.org/10.1152/physrev.00028.2012, doi:10.1152/physrev.00028.2012. This article has 1987 citations and is from a highest quality peer-reviewed journal.

7. (liu2016theactivationloop pages 1-1): Aizhuo Liu, Dexin Sui, Dianqing Wu, and Jian Hu. The activation loop of pip5k functions as a membrane sensor essential for lipid substrate processing. Science Advances, Nov 2016. URL: https://doi.org/10.1126/sciadv.1600925, doi:10.1126/sciadv.1600925. This article has 44 citations and is from a highest quality peer-reviewed journal.

8. (hu2015resolutionofstructure pages 1-2): Jian Hu, Qianying Yuan, Xue Kang, Yuanbo Qin, Lin Li, Ya Ha, and Dianqing Wu. Resolution of structure of pip5k1a reveals molecular mechanism for its regulation by dimerization and dishevelled. Nature Communications, Sep 2015. URL: https://doi.org/10.1038/ncomms9205, doi:10.1038/ncomms9205. This article has 68 citations and is from a highest quality peer-reviewed journal.

9. (wen2023regulationofphosphoinositide pages 1-3): Tianmu Wen, Narendra Thapa, Vincent L. Cryns, and Richard A. Anderson. Regulation of phosphoinositide signaling by scaffolds at cytoplasmic membranes. Biomolecules, 13:1297, Aug 2023. URL: https://doi.org/10.3390/biom13091297, doi:10.3390/biom13091297. This article has 20 citations.

10. (kallikourdis2016phosphatidylinositol4phosphate5kinase pages 1-2): Marinos Kallikourdis, Anna Elisa Trovato, Giuliana Roselli, Michela Muscolini, Nicla Porciello, Loretta Tuosto, and Antonella Viola. Phosphatidylinositol 4-phosphate 5-kinase β controls recruitment of lipid rafts into the immunological synapse. The Journal of Immunology, 196:1955-1963, Feb 2016. URL: https://doi.org/10.4049/jimmunol.1501788, doi:10.4049/jimmunol.1501788. This article has 32 citations.

11. (dieterle2014pdk1controlsupstream pages 1-2): Alexandra M. Dieterle, P. Böhler, Hildegard Keppeler, S. Alers, N. Berleth, Stefan Driessen, N. Hieke, S. Pietkiewicz, Antje S. Löffler, C. Peter, Alex Gray, Nick R. Leslie, H. Shinohara, Tomohiro Kurosaki, M. Engelke, J. Wienands, M. Bonin, Sebastian Wesselborg, and B. Stork. Pdk1 controls upstream pi3k expression and pip3 generation. Oncogene, 33:3043-3053, Jun 2014. URL: https://doi.org/10.1038/onc.2013.266, doi:10.1038/onc.2013.266. This article has 69 citations and is from a domain leading peer-reviewed journal.

12. (jin2023lipidkinasespip5ks pages 5-6): Yue Jin and Jian Xue. Lipid kinases pip5ks and pip4ks: potential drug targets for breast cancer. Frontiers in Oncology, Dec 2023. URL: https://doi.org/10.3389/fonc.2023.1323897, doi:10.3389/fonc.2023.1323897. This article has 11 citations.

13. (hou2025phosphoinositidesignalingat pages 1-2): Xiaoting Hou, Yu Chen, Noah D. Carrillo, Vincent L. Cryns, Richard A. Anderson, Jichao Sun, Songlin Wang, and Mo Chen. Phosphoinositide signaling at the cytoskeleton in the regulation of cell dynamics. Cell Death & Disease, Apr 2025. URL: https://doi.org/10.1038/s41419-025-07616-x, doi:10.1038/s41419-025-07616-x. This article has 26 citations and is from a peer-reviewed journal.

14. (peng2021clic1recruitspip5k1ac pages 1-2): Jei-Ming Peng, Sheng-Hsuan Lin, Ming-Chin Yu, and Sen-Yung Hsieh. Clic1 recruits pip5k1a/c to induce cell-matrix adhesions for tumor metastasis. Journal of Clinical Investigation, Jan 2021. URL: https://doi.org/10.1172/jci133525, doi:10.1172/jci133525. This article has 88 citations and is from a highest quality peer-reviewed journal.

15. (baba2020emergingrolesof pages 1-2): Takashi Baba and Tamas Balla. Emerging roles of phosphatidylinositol 4-phosphate and phosphatidylinositol 4,5-bisphosphate as regulators of multiple steps in autophagy. The Journal of Biochemistry, 168(4):329-336, Aug 2020. URL: https://doi.org/10.1093/jb/mvaa089, doi:10.1093/jb/mvaa089. This article has 49 citations.

## Artifacts

- [Edison artifact artifact-00](PIP5K1B-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. liu2016theactivationloop pages 1-1
2. hansen2022membranemediateddimerizationpotentiates pages 1-2
3. balla2013phosphoinositidestinylipids pages 1-2
4. baba2020emergingrolesof pages 1-2
5. hou2025phosphoinositidesignalingat pages 1-2
6. muftuoglu2016mechanismofsubstrate pages 1-2
7. balla2013phosphoinositidestinylipids pages 2-3
8. hu2015resolutionofstructure pages 1-2
9. wen2023regulationofphosphoinositide pages 1-3
10. PI(4,5)P2
11. PI(4,5)P2, PtdIns(4,5)P2
12. PI(3,4,5)P3, PIP3
13. PI4P/PtdIns4P
14. PI(4,5)P2/PtdIns(4,5)P2
15. https://doi.org/10.3389/fonc.2023.1323897,
16. https://doi.org/10.7554/elife.73747,
17. https://doi.org/10.1073/pnas.1522112113,
18. https://doi.org/10.1152/physrev.00028.2012,
19. https://doi.org/10.1080/15548627.2023.2182594,
20. https://doi.org/10.1126/sciadv.1600925,
21. https://doi.org/10.1038/ncomms9205,
22. https://doi.org/10.3390/biom13091297,
23. https://doi.org/10.4049/jimmunol.1501788,
24. https://doi.org/10.1038/onc.2013.266,
25. https://doi.org/10.1038/s41419-025-07616-x,
26. https://doi.org/10.1172/jci133525,
27. https://doi.org/10.1093/jb/mvaa089,