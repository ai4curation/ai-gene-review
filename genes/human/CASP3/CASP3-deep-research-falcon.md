---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-06-21T07:05:41.623075'
end_time: '2026-06-21T07:05:41.625430'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: CASP3
  gene_symbol: CASP3
  uniprot_accession: P42574
  protein_description: 'RecName: Full=Caspase-3 {ECO:0000303|PubMed:15003516, ECO:0000303|PubMed:18723680};
    Short=CASP-3; EC=3.4.22.56 {ECO:0000269|PubMed:23152800, ECO:0000269|PubMed:23845944,
    ECO:0000269|PubMed:30878284, ECO:0000269|PubMed:33725486, ECO:0000269|PubMed:7596430};
    AltName: Full=Apopain {ECO:0000303|PubMed:8696339}; AltName: Full=Cysteine protease
    CPP32 {ECO:0000303|PubMed:7774019}; Short=CPP-32 {ECO:0000303|PubMed:7774019,
    ECO:0000303|PubMed:9334240}; AltName: Full=Protein Yama {ECO:0000303|PubMed:7774019};
    AltName: Full=SREBP cleavage activity 1; Short=SCA-1; Contains: RecName: Full=Caspase-3
    subunit p17; Contains: RecName: Full=Caspase-3 subunit p12; Flags: Precursor;'
  gene_info: Name=CASP3; Synonyms=CPP32 {ECO:0000303|PubMed:7983002};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the peptidase C14A family. .
  protein_domains: Caspase-like_dom_sf. (IPR029030); Caspase_cys_AS. (IPR033139);
    Caspase_his_AS. (IPR016129); Pept_C14. (IPR002398); Pept_C14_caspase. (IPR011600)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: CASP3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: CASP3-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P42574
- **Protein Description:** RecName: Full=Caspase-3 {ECO:0000303|PubMed:15003516, ECO:0000303|PubMed:18723680}; Short=CASP-3; EC=3.4.22.56 {ECO:0000269|PubMed:23152800, ECO:0000269|PubMed:23845944, ECO:0000269|PubMed:30878284, ECO:0000269|PubMed:33725486, ECO:0000269|PubMed:7596430}; AltName: Full=Apopain {ECO:0000303|PubMed:8696339}; AltName: Full=Cysteine protease CPP32 {ECO:0000303|PubMed:7774019}; Short=CPP-32 {ECO:0000303|PubMed:7774019, ECO:0000303|PubMed:9334240}; AltName: Full=Protein Yama {ECO:0000303|PubMed:7774019}; AltName: Full=SREBP cleavage activity 1; Short=SCA-1; Contains: RecName: Full=Caspase-3 subunit p17; Contains: RecName: Full=Caspase-3 subunit p12; Flags: Precursor;
- **Gene Information:** Name=CASP3; Synonyms=CPP32 {ECO:0000303|PubMed:7983002};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the peptidase C14A family. .
- **Key Domains:** Caspase-like_dom_sf. (IPR029030); Caspase_cys_AS. (IPR033139); Caspase_his_AS. (IPR016129); Pept_C14. (IPR002398); Pept_C14_caspase. (IPR011600)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CASP3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CASP3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CASP3** (gene ID: CASP3, UniProt: P42574) in human.

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
- **UniProt Accession:** P42574
- **Protein Description:** RecName: Full=Caspase-3 {ECO:0000303|PubMed:15003516, ECO:0000303|PubMed:18723680}; Short=CASP-3; EC=3.4.22.56 {ECO:0000269|PubMed:23152800, ECO:0000269|PubMed:23845944, ECO:0000269|PubMed:30878284, ECO:0000269|PubMed:33725486, ECO:0000269|PubMed:7596430}; AltName: Full=Apopain {ECO:0000303|PubMed:8696339}; AltName: Full=Cysteine protease CPP32 {ECO:0000303|PubMed:7774019}; Short=CPP-32 {ECO:0000303|PubMed:7774019, ECO:0000303|PubMed:9334240}; AltName: Full=Protein Yama {ECO:0000303|PubMed:7774019}; AltName: Full=SREBP cleavage activity 1; Short=SCA-1; Contains: RecName: Full=Caspase-3 subunit p17; Contains: RecName: Full=Caspase-3 subunit p12; Flags: Precursor;
- **Gene Information:** Name=CASP3; Synonyms=CPP32 {ECO:0000303|PubMed:7983002};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the peptidase C14A family. .
- **Key Domains:** Caspase-like_dom_sf. (IPR029030); Caspase_cys_AS. (IPR033139); Caspase_his_AS. (IPR016129); Pept_C14. (IPR002398); Pept_C14_caspase. (IPR011600)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CASP3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CASP3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CASP3** (gene ID: CASP3, UniProt: P42574) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Human CASP3 (Caspase-3)

## Gene and Protein Identity

The CASP3 gene encodes human caspase-3 (UniProt P42574), a pivotal executioner caspase in the caspase family of cysteine-dependent, aspartate-specific proteases (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3). Caspase-3 is classified as EC 3.4.22.56 and functions as the most proteolytically proficient executioner of programmed cell death, though it also plays important roles in non-apoptotic cellular processes (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3, blais2026usingabioluminescence pages 2-3). The protein is synthesized as an inactive zymogen (procaspase-3) and belongs to the peptidase C14A family (malireddi2025threedecadesof pages 1-3).

## Primary Enzymatic Function and Substrate Specificity

Caspase-3 is a cysteine protease that cleaves peptide bonds almost exclusively C-terminal to aspartate residues at the P1 position (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3). The enzyme catalyzes the hydrolysis of protein substrates during apoptosis and cellular stress responses, functioning as the primary executioner protease that mediates downstream substrate cleavage following activation by initiator caspases (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 7-9).

### Catalytic Mechanism and Activation

Procaspase-3 exists as an inactive homodimer that requires proteolytic cleavage at the intersubunit linker to form an active tetramer (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3). Initiator caspases, particularly caspase-9 (via the intrinsic pathway) and caspase-8 (via the extrinsic pathway), cleave procaspase-3 at the intersubunit linker sequence 172-IETD↓S to generate the active enzyme (araya2021deorphanizingcaspase3and pages 1-3, soni2021caspase9activationof pages 1-3). This cleavage produces two subunits (p17 and p12) that assemble into the catalytically active tetrameric form (malireddi2025threedecadesof pages 1-3).

### Substrate Recognition and Cleavage Specificity

Deep substrate profiling using subtiligase N-terminomics in native human cell lysates has revealed that caspase-3 recognizes a clear consensus motif of **DEVD↓(G/S/A)** for positions P4-P3-P2-P1↓P1′ (araya2021deorphanizingcaspase3and pages 4-6, blais2026usingabioluminescence pages 2-3). This motif can be more broadly summarized as DXXD↓X, though the P4 aspartate contributes importantly to substrate discrimination (araya2021deorphanizingcaspase3and pages 4-6, blais2026usingabioluminescence pages 2-3). However, substrate cleavage depends not only on sequence but also on local structural context and accessibility, as many proteins containing potential recognition motifs are not efficiently cleaved (araya2021deorphanizingcaspase3and pages 4-6, soni2021caspase9activationof pages 1-3).

### Substrate Repertoire

The most comprehensive substrate profiling to date identified **906 putative protein substrates** and **1,126 cleavage sites** for caspase-3 in native lysates (araya2021deorphanizingcaspase3and pages 1-3, araya2021deorphanizingcaspase3and pages 4-6). Of these, 577 cleavage sites and 257 substrates had not previously been reported in the apoptosis DegraBase, revealing a pool of novel substrates that likely function in non-apoptotic contexts (araya2021deorphanizingcaspase3and pages 4-6). Caspase-3 substrates are enriched in cytoplasmic (~49%) and nuclear (~48%) proteins, with smaller fractions in mitochondria, endoplasmic reticulum, cell membrane, and secreted compartments (araya2021deorphanizingcaspase3and pages 4-6).

Key validated substrates include:
- **PARP1 (poly(ADP-ribose) polymerase 1)**: A canonical substrate whose cleavage is widely used as a hallmark readout of caspase-3 activation during apoptosis (blais2026usingabioluminescence pages 2-3, samarasekera2025caspase3and pages 1-2, killarney2023executionercaspasesrestrict pages 1-2)
- **ICAD/DFF45 (inhibitor of caspase-activated DNase)**: Cleavage releases CAD nuclease activity, enabling genomic DNA fragmentation (blais2026usingabioluminescence pages 2-3, zhou2024diversefunctionsof pages 1-2)
- **Gasdermin E (GSDME)**: Cleaved by caspase-3 but not efficiently by caspase-7, demonstrating non-redundant substrate discrimination between executioner caspases (blais2026usingabioluminescence pages 2-3)
- **CAD (carbamoyl-phosphate synthetase/aspartate transcarbamylase/dihydroorotase)**: Cleaved at Asp1371 prior to degradation, linking caspase-3 to pyrimidine synthesis control and chemosensitivity (tannous2025supersensitivechemiluminescentprobe pages 1-3)

| Feature | Human CASP3 summary | Evidence |
|---|---|---|
| Verified identity | CASP3 encodes human caspase-3, an executioner/effector caspase in the caspase family; UniProt P42574 aligns with literature describing a cysteine-dependent, aspartate-specific protease central to apoptosis. | (mustafa2024apoptosisacomprehensive pages 2-4, malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3) |
| Enzyme classification | EC 3.4.22.56; proteolytic enzyme that hydrolyzes peptide bonds in protein substrates during apoptosis and other stress responses. | (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3) |
| Protease type | Cysteine-dependent, aspartate-specific protease (cysteine aspartyl protease). Caspases cleave almost exclusively C-terminal to Asp at the P1 position. | (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3, soni2021caspase9activationof pages 1-3) |
| Primary biochemical function | CASP3 is the major executioner protease that performs downstream substrate cleavage after activation by initiator caspases, thereby driving apoptotic dismantling of the cell; it also contributes to selected non-apoptotic stress-adaptation pathways. | (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 7-9, samarasekera2025caspase3and pages 1-2) |
| Catalytic mechanism | Activated initiator caspases cleave procaspase-3 at the intersubunit linker to generate the active executioner enzyme; executioner caspases are inactive homodimers that require cleavage to form active tetramers that mediate downstream substrate cleavage. Proteolysis occurs at the scissile bond between P1 and P1′, with strict requirement for Asp at P1. | (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3, soni2021caspase9activationof pages 1-3) |
| Preferred cleavage motif | Deep substrate profiling in native human cell lysates identified a clear caspase-3 consensus of **DEVD↓(G/S/A)** for P4-P1↓P1′; broader tolerated motifs exist, indicating cleavage depends on both sequence and local structural context. | (araya2021deorphanizingcaspase3and pages 4-6, blais2026usingabioluminescence pages 2-3) |
| Minimal sequence rule | Preference is often summarized as DXXD↓X, but the strongest observed motif for human caspase-3 is DEVD↓(G/A/S); P4 contributes importantly to specificity. | (araya2021deorphanizingcaspase3and pages 4-6, soni2021caspase9activationof pages 1-3, blais2026usingabioluminescence pages 2-3) |
| Importance of substrate context | Sequence alone is insufficient to explain cleavage; local accessibility and structural context strongly affect whether a potential motif is actually cleaved in proteins. | (araya2021deorphanizingcaspase3and pages 4-6, soni2021caspase9activationof pages 1-3) |
| Scale of substrate repertoire | Reverse N-terminomics identified **906 putative protein substrates** and **1126 cleavage sites** for caspase-3 in native lysates, representing one of the most comprehensive substrate maps reported. | (araya2021deorphanizingcaspase3and pages 1-3, araya2021deorphanizingcaspase3and pages 4-6) |
| Novelty of substrate map | Of the observed caspase-3 cleavage events, **577 cleavage sites** had not previously been found in the apoptosis DegraBase, and **257 substrates** were newly reported. | (araya2021deorphanizingcaspase3and pages 4-6) |
| Major substrate classes | CASP3 cleaves structural, regulatory, DNA-repair, cytoskeletal, chromatin, and signaling proteins, consistent with its role in morphological remodeling, DNA fragmentation, and apoptotic execution. | (tannous2025supersensitivechemiluminescentprobe pages 1-3, blais2026usingabioluminescence pages 2-3, mustafa2024apoptosisacomprehensive pages 7-9) |
| Key substrate example: PARP1 | PARP1 is a canonical bona fide caspase-3 substrate and a standard readout of caspase-3 activity during apoptosis; cleavage of PARP1 is repeatedly cited as a hallmark of executioner caspase activation. | (blais2026usingabioluminescence pages 2-3, samarasekera2025caspase3and pages 1-2, killarney2023executionercaspasesrestrict pages 1-2) |
| Key substrate example: ICAD/DFF45 | CASP3 cleaves the inhibitor of caspase-activated DNase (ICAD), enabling CAD-mediated genomic DNA fragmentation during apoptosis. | (zhou2024diversefunctionsof pages 1-2, blais2026usingabioluminescence pages 2-3) |
| Key substrate example: GSDME | Human GSDME contains a DxxD motif recognized by CASP3; recent work emphasizes that human GSDME is cleaved by CASP3 but not efficiently by human CASP7, illustrating non-redundant substrate discrimination between the two executioner caspases. | (blais2026usingabioluminescence pages 2-3) |
| Key substrate example: CAD (carbamoyl-phosphate synthetase/aspartate transcarbamylase/dihydroorotase) | Recent work shows CAD must be cleaved by caspase-3 at Asp1371 prior to degradation, linking CASP3 activity to chemosensitivity and pyrimidine synthesis control in cancer cells. | (tannous2025supersensitivechemiluminescentprobe pages 1-3) |
| Other validated/representative substrate themes | Caspase-3 substrates include proteins involved in apoptosis, stress adaptation, autophagy modulation, DNA-damage signaling, and inflammatory restraint; cleavage landscapes differ under lethal vs non-lethal stress. | (samarasekera2025caspase3and pages 1-2, killarney2023executionercaspasesrestrict pages 1-2) |
| Subcellular distribution of substrates | In the N-terminomics dataset, caspase-3 substrates were enriched in cytoplasmic and nuclear proteins: ~49% cytoplasmic and ~48% nuclear, with smaller fractions in mitochondria, ER, membrane, and secreted compartments. | (araya2021deorphanizingcaspase3and pages 4-6) |
| Comparison with caspase-7: shared features | CASP3 and CASP7 are closely related executioner caspases with overlapping preferences and a shared preference for DEVD-like motifs; both are activated downstream of initiator caspases in apoptosis. | (mustafa2024apoptosisacomprehensive pages 2-4, blais2026usingabioluminescence pages 2-3) |
| Comparison with caspase-7: key difference | Despite shared DxxD recognition, CASP3 and CASP7 are not fully redundant. Human GSDME is cleaved by CASP3 but not by human CASP7, and structural work attributes this to differences in the CASP7 p10 subunit/prime-side substrate recognition. | (blais2026usingabioluminescence pages 2-3) |
| Comparison with caspase-7: proteolytic breadth | Caspase-3 is described as the most proteolytically proficient executioner caspase and has a very broad substrate repertoire; some recent assay work and reviews continue to treat CASP3 as the dominant executioner enzyme. | (blais2026usingabioluminescence pages 2-3, tannous2025supersensitivechemiluminescentprobe pages 1-3) |


*Table: This table summarizes the primary enzymatic activity, cleavage preferences, substrate scope, and mechanism of human caspase-3, with a focused comparison to caspase-7. It is useful for quickly identifying what CASP3 cleaves, how it recognizes substrates, and why it is considered the dominant executioner caspase.*

## Subcellular Localization

Procaspase-3 is synthesized in the cytosol where it exists as an inactive enzyme under normal conditions (araya2021deorphanizingcaspase3and pages 4-6). Upon apoptotic stimulation, the activated caspase-3 functions primarily in the cytoplasm and nucleus, where it cleaves its broad substrate repertoire (araya2021deorphanizingcaspase3and pages 4-6). The distribution of caspase-3 substrates reflects this dual cytoplasmic-nuclear localization, with approximately equal representation in both compartments (araya2021deorphanizingcaspase3and pages 4-6). During apoptosis, active caspase-3 can also translocate to mitochondria and the nucleus to execute specific functions (mustafa2024apoptosisacomprehensive pages 7-9).

## Role in Apoptotic Signaling Pathways

Caspase-3 serves as the central convergence point for both intrinsic (mitochondrial) and extrinsic (death receptor) apoptotic pathways, making it a critical integration node for diverse death stimuli (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 5-7).

### Intrinsic (Mitochondrial) Pathway

The intrinsic pathway is initiated by intracellular stress signals including DNA damage, reactive oxygen species (ROS), endoplasmic reticulum stress, growth factor withdrawal, and hypoxia (mustafa2024apoptosisacomprehensive pages 5-7, mustafa2024apoptosisacomprehensive pages 7-9). These stressors activate BH3-only proteins and p53, which either directly activate the pore-forming effectors BAX and BAK or neutralize anti-apoptotic BCL-2 family members (BCL-2, BCL-xL, MCL-1) (mustafa2024apoptosisacomprehensive pages 2-4, mustafa2024apoptosisacomprehensive pages 5-7, mustafa2024apoptosisacomprehensive pages 7-9).

BAX and BAK oligomerize to form pores in the outer mitochondrial membrane, causing mitochondrial outer membrane permeabilization (MOMP), often described as the apoptotic "point of no return" (mustafa2024apoptosisacomprehensive pages 7-9). MOMP releases cytochrome c from the mitochondrial intermembrane space into the cytosol (araya2021deorphanizingcaspase3and pages 1-3, zhou2024diversefunctionsof pages 1-2). Cytosolic cytochrome c binds to apoptotic protease activating factor-1 (APAF-1) in the presence of ATP, forming the apoptosome complex (araya2021deorphanizingcaspase3and pages 1-3, zhou2024diversefunctionsof pages 1-2, killarney2023executionercaspasesrestrict pages 1-2). Procaspase-9 associates with the apoptosome and undergoes proximity-induced auto-activation (araya2021deorphanizingcaspase3and pages 1-3, zhou2024diversefunctionsof pages 1-2). Active caspase-9 then cleaves and activates procaspase-3 and procaspase-7, initiating the downstream proteolytic cascade (araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 7-9).

### Extrinsic (Death Receptor) Pathway

The extrinsic pathway is initiated by extracellular death ligands (such as FasL, TNF-α, and TRAIL) binding to their cognate death receptors (Fas/CD95, TNFR1, and death receptors 4/5) on the cell surface (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 5-7). Ligand binding induces receptor oligomerization and assembly of the death-inducing signaling complex (DISC), which recruits and activates initiator caspases-8 and -10 through proximity-induced dimerization and autoproteolysis (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 5-7).

Active caspase-8 can directly cleave and activate procaspase-3, providing a rapid route to apoptotic execution (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 5-7). Alternatively, caspase-8 can cleave the BH3-only protein BID, generating truncated BID (tBID) that translocates to mitochondria and engages the intrinsic pathway, thereby amplifying the death signal through mitochondrial amplification and caspase-9 activation (araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 7-9). This cross-talk mechanism integrates extrinsic and intrinsic signaling.

### Regulatory Mechanisms

Multiple regulatory mechanisms fine-tune caspase-3 activation:
- **Inhibitor of apoptosis proteins (IAPs)** such as XIAP suppress caspase activity by direct binding (mustafa2024apoptosisacomprehensive pages 7-9)
- **Smac/DIABLO and Omi/HtrA2**, released from mitochondria during MOMP, antagonize IAPs and relieve caspase inhibition (mustafa2024apoptosisacomprehensive pages 7-9)
- **BCL-2 family proteins** determine the apoptotic threshold upstream of caspase-3 by regulating MOMP (mustafa2024apoptosisacomprehensive pages 2-4, mustafa2024apoptosisacomprehensive pages 5-7, mustafa2024apoptosisacomprehensive pages 7-9)

### Downstream Effects of Caspase-3 Activation

Once activated, caspase-3 cleaves a vast array of structural, regulatory, DNA repair, cytoskeletal, and chromatin-associated proteins, producing the hallmark biochemical and morphological features of apoptosis (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3, araya2021deorphanizingcaspase3and pages 4-6, blais2026usingabioluminescence pages 2-3):

- **PARP1 cleavage**: Marks shutdown of DNA repair and progression toward irreversible apoptotic execution (blais2026usingabioluminescence pages 2-3, samarasekera2025caspase3and pages 1-2)
- **DNA fragmentation**: Cleavage of ICAD releases CAD nuclease activity, causing characteristic apoptotic DNA ladder formation (blais2026usingabioluminescence pages 2-3, zhou2024diversefunctionsof pages 1-2)
- **Cellular demolition**: Proteolysis of cytoskeletal and structural proteins produces membrane blebbing, chromatin condensation, cell shrinkage, phosphatidylserine externalization, and detachment from the extracellular matrix (mustafa2024apoptosisacomprehensive pages 2-4, blais2026usingabioluminescence pages 2-3, mustafa2024apoptosisacomprehensive pages 7-9)

| Pathway/component | Sequence of events involving CASP3 | Key regulators / molecular details | Functional outcome | Evidence |
|---|---|---|---|---|
| Intrinsic (mitochondrial) apoptosis | Intracellular stress signals trigger mitochondrial outer membrane permeabilization (MOMP), releasing cytochrome c into the cytosol; cytochrome c binds APAF1 to assemble the apoptosome, which activates caspase-9, and caspase-9 then cleaves and activates procaspase-3. | Stressors include DNA damage, ROS, ER stress, loss of adhesion, growth-factor withdrawal, and hypoxia. BAX/BAK are the key pore-forming effectors that drive MOMP. | Activation of executioner caspase-3 initiates the downstream proteolytic cascade that dismantles the cell. | (mustafa2024apoptosisacomprehensive pages 5-7, mustafa2024apoptosisacomprehensive pages 7-9, zhou2024diversefunctionsof pages 1-2, killarney2023executionercaspasesrestrict pages 1-2) |
| MOMP as the commitment step | MOMP is described as the apoptotic “point of no return”; after membrane permeabilization, mitochondrial proteins enter the cytosol and enable caspase activation. | BH3-only proteins and p53 promote BAX/BAK activation directly or by neutralizing anti-apoptotic BCL-2 family members. | Commits the cell to apoptosis and licenses caspase-9 to activate caspase-3. | (mustafa2024apoptosisacomprehensive pages 7-9) |
| Cytochrome c–apoptosome axis | Released cytochrome c binds apoptotic protease activating factor-1 (APAF1), forming the apoptosome complex with procaspase-9; auto-activation of caspase-9 within this complex leads to downstream cleavage of executioner caspases-3/7. | Cytochrome c is normally in the mitochondrial intermembrane space and becomes apoptogenic upon cytosolic release. | Central biochemical route linking mitochondrial injury to CASP3 activation. | (araya2021deorphanizingcaspase3and pages 1-3, zhou2024diversefunctionsof pages 1-2, killarney2023executionercaspasesrestrict pages 1-2) |
| Extrinsic (death receptor) apoptosis | Extracellular death ligands bind cell-surface death receptors, leading to assembly of the death-inducing signaling complex (DISC), activation of initiator caspase-8 (and sometimes caspase-10), and direct cleavage/activation of procaspase-3. | Fas/CD95 and TNFR-family death receptors are highlighted; DISC-mediated proximity promotes initiator caspase activation. | Rapid activation of CASP3 from receptor-proximal signaling. | (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 5-7) |
| Extrinsic–intrinsic cross-talk via BID | Activated caspase-8 can also cleave BID, thereby engaging mitochondrial apoptosis and caspase-9 in addition to directly activating caspase-3. | BID is a BH3-interacting death agonist linking death receptor signaling to MOMP. | Amplifies apoptotic signaling and integrates extrinsic and intrinsic pathways. | (araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 7-9) |
| Key upstream regulators: BCL-2 family | The balance between pro-apoptotic and anti-apoptotic BCL-2 family proteins determines whether MOMP occurs and therefore whether CASP3 can be activated through the intrinsic pathway. | Pro-apoptotic: BAX, BAK, BID, BIM, PUMA, NOXA, BIK. Anti-apoptotic: BCL-2, BCL-xL, MCL-1. | Governs apoptotic threshold upstream of CASP3. | (mustafa2024apoptosisacomprehensive pages 2-4, mustafa2024apoptosisacomprehensive pages 5-7, mustafa2024apoptosisacomprehensive pages 7-9) |
| Key upstream regulators: death receptors | Fas/CD95 and TNFR1-family receptors transduce extracellular apoptotic cues to initiator caspases that activate CASP3. | Ligand binding induces receptor complex assembly and initiator caspase activation at the DISC. | Couples immune/extracellular death signals to executioner caspase activation. | (mustafa2024apoptosisacomprehensive pages 2-4, mustafa2024apoptosisacomprehensive pages 5-7) |
| Key upstream regulators: IAPs and Smac/DIABLO | IAP proteins suppress caspase activity, while mitochondrial Smac/DIABLO released during MOMP antagonizes IAPs, thereby facilitating caspase-3 activation and function. | XIAP and related IAPs inhibit caspases; Smac/DIABLO relieves this inhibition after mitochondrial permeabilization. | Strengthens and sustains CASP3-mediated execution. | (mustafa2024apoptosisacomprehensive pages 7-9) |
| CASP3 as executioner protease | Initiator caspases activate CASP3, which then cleaves broad sets of structural, regulatory, DNA-repair, cytoskeletal, and chromatin-associated proteins. | CASP3 is an executioner cysteine-aspartate protease with strong DEVD-like substrate preference and a large substrate repertoire. | Produces the canonical biochemical and morphological features of apoptosis. | (malireddi2025threedecadesof pages 1-3, araya2021deorphanizingcaspase3and pages 1-3, araya2021deorphanizingcaspase3and pages 4-6, blais2026usingabioluminescence pages 2-3) |
| Downstream effect: PARP1 cleavage | CASP3 cleaves PARP1, a canonical hallmark substrate commonly used as a readout of executioner caspase activation. | PARP1 cleavage marks shutdown of DNA repair and progression of apoptosis. | Promotes irreversible apoptotic execution. | (blais2026usingabioluminescence pages 2-3, samarasekera2025caspase3and pages 1-2, killarney2023executionercaspasesrestrict pages 1-2) |
| Downstream effect: DNA fragmentation | CASP3 cleaves ICAD, releasing CAD activity and driving genomic DNA fragmentation. | Cleavage of the inhibitor of caspase-activated DNase is a core mechanism for apoptotic DNA breakdown. | Produces a defining nuclear feature of apoptosis. | (blais2026usingabioluminescence pages 2-3, zhou2024diversefunctionsof pages 1-2) |
| Downstream effect: cellular demolition | CASP3 activation causes membrane blebbing, chromatin condensation, cell shrinkage, phosphatidylserine exposure, and detachment from the extracellular matrix through cleavage of multiple substrates. | Executioner caspases-3/6/7 mediate the terminal demolition phase downstream of initiators. | Morphological and biochemical completion of apoptosis. | (mustafa2024apoptosisacomprehensive pages 2-4, blais2026usingabioluminescence pages 2-3, mustafa2024apoptosisacomprehensive pages 7-9) |
| Pathway convergence | Both intrinsic and extrinsic pathways converge on CASP3 activation, making it a central integration point for diverse death stimuli. | Caspase-8 and caspase-9 represent the main upstream initiators for extrinsic and intrinsic apoptosis, respectively. | Explains why CASP3 is widely used as a core apoptosis effector/readout. | (mustafa2024apoptosisacomprehensive pages 2-4, araya2021deorphanizingcaspase3and pages 1-3, mustafa2024apoptosisacomprehensive pages 5-7) |
| Additional route: granzyme B-mediated apoptosis | Cytotoxic lymphocyte granzyme B can promote caspase-dependent apoptosis by cleaving caspase-3, caspase-7, and BID. | Provides an immune-mediated apoptotic route that intersects with both direct CASP3 activation and mitochondrial amplification. | Supports target-cell killing by immune effectors. | (mustafa2024apoptosisacomprehensive pages 7-9) |
| Inflammatory restraint during apoptosis | During MOMP-associated apoptosis, executioner caspases-3/7 suppress mtRNA-driven type I interferon signaling, limiting inflammatory responses while cell death proceeds. | In CASP3/7-deficient settings, mtRNA activates the MDA5/MAVS/IRF3 pathway and type I IFN signaling. | Helps maintain the typically immunologically silent character of apoptosis. | (killarney2023executionercaspasesrestrict pages 1-2) |


*Table: This table summarizes how human caspase-3 is activated through intrinsic and extrinsic apoptosis pathways, the main upstream regulators controlling those routes, and the principal downstream consequences of caspase-3 activation. It is useful for linking CASP3's biochemical function to its pathway context and cellular effects.*

## Non-Apoptotic Functions of Caspase-3

Accumulating evidence from 2022-2025 demonstrates that caspase-3 plays critical roles beyond apoptosis, supporting the hypothesis that the primordial function of caspases was to regulate cellular stress adaptations rather than solely execute cell death (samarasekera2025caspase3and pages 1-2, rosa2024nonapoptoticcaspaseevents pages 1-2).

### Cytoprotective Autophagy and Stress Adaptation

Recent work has established a functionally conserved role for caspase-3 and caspase-7 in promoting starvation- or proteasome inhibition-induced cytoprotective autophagy in human breast cancer cells (samarasekera2025caspase3and pages 1-2). Loss of CASP3 and CASP7 results in increased PARP1 cleavage, reduced LC3B and ATG7 transcript levels, and decreased H2AX phosphorylation, consistent with a block in autophagy and DNA damage response pathways (samarasekera2025caspase3and pages 1-2). Under non-lethal stress conditions, caspase-7 undergoes non-canonical processing at calpain cleavage sites flanking a PARP1 exosite, producing stable fragments that can rescue H2AX phosphorylation (samarasekera2025caspase3and pages 1-2). The synthetic lethality observed between CASP3/CASP7 loss and BRCA1 deficiency underscores the importance of caspases in stress adaptation (samarasekera2025caspase3and pages 1-2).

### Suppression of Inflammatory Signaling During Apoptosis

During apoptosis, mitochondrial outer membrane permeabilization (MOMP) releases mitochondrial RNA (mtRNA) into the cytosol (killarney2023executionercaspasesrestrict pages 1-2). Executioner caspases-3 and -7 prevent cytoplasmic mtRNA from triggering inflammatory signaling pathways (killarney2023executionercaspasesrestrict pages 1-2). In settings where caspase-3/7 are inhibited, apoptotic insults result in mtRNA activation of the MDA5/MAVS/IRF3 pathway, driving Type I interferon (IFN) signaling (killarney2023executionercaspasesrestrict pages 1-2). This key function of caspase-3/7 helps maintain the typically immunologically silent character of apoptosis by inhibiting inflammation caused by cytoplasmic release of mtRNA (killarney2023executionercaspasesrestrict pages 1-2).

### Neuronal Plasticity and Synaptic Remodeling

Non-apoptotic caspase-3 activation mediates synaptic pruning, dendritic spine loss, and long-term depression (LTD) in neurons without causing cell death (fieblinger2022nonapoptoticcaspase3activation pages 1-2). In a mouse model of Parkinson's disease, caspase-3 is transiently activated in the striatum following dopaminergic denervation, coinciding with rapid loss of dendritic spines and deficits in synaptic LTD in indirect pathway neurons (fieblinger2022nonapoptoticcaspase3activation pages 1-2). Systemic caspase inhibitor treatment prevents both spine pruning and LTD deficits without interfering with ongoing dopaminergic degeneration, identifying non-apoptotic caspase activation as a critical event in early neuroplastic changes (fieblinger2022nonapoptoticcaspase3activation pages 1-2). Similar non-apoptotic caspase-3 functions have been documented in synaptic dysfunction in Alzheimer's disease models.

### Neural Stem Cell Differentiation

Non-apoptotic caspase-3/7 events occur in adult neural stem cells (NSCs) and are biased toward direct neuronal conversion under physiological conditions (rosa2024nonapoptoticcaspaseevents pages 1-2). Using an NSC-specific genetic tracer of caspase-3/7 activation in zebrafish, researchers demonstrated that non-apoptotic caspase events facilitate direct neuronal differentiation without cell division (rosa2024nonapoptoticcaspaseevents pages 1-2). The transcription factor Atf3 is necessary for this fate choice, and caspase-3/7 activation is part of the processes engaged when NSCs are recruited for neuronal regeneration (rosa2024nonapoptoticcaspaseevents pages 1-2).

### Oncogenic Transformation

In certain contexts, caspase-3 can promote rather than suppress oncogene-induced malignant transformation (fieblinger2022nonapoptoticcaspase3activation pages 1-2). Active caspase-3 triggers translocation of endonuclease G (EndoG) from mitochondria to the nucleus, inducing phosphorylation of the Src-STAT3 signaling pathway to facilitate oncogenic transformation (fieblinger2022nonapoptoticcaspase3activation pages 1-2). Genetic ablation of caspase-3 significantly attenuates oncogene-induced transformation in vitro and delays breast cancer progression in mouse models, revealing a context-dependent pro-oncogenic role (fieblinger2022nonapoptoticcaspase3activation pages 1-2).

## Comparison with Caspase-7

While caspase-3 and caspase-7 are closely related executioner caspases with overlapping substrate preferences and shared recognition of DEVD-like motifs, they are not fully redundant (mustafa2024apoptosisacomprehensive pages 2-4, blais2026usingabioluminescence pages 2-3). Caspase-3 is described as the most proteolytically proficient executioner caspase, and recent structural studies reveal that substrate discrimination differs between the two enzymes (blais2026usingabioluminescence pages 2-3). For example, human GSDME is efficiently cleaved by caspase-3 but not by caspase-7, a difference attributed to variations in the p10 subunit and prime-side substrate recognition architecture (blais2026usingabioluminescence pages 2-3). Caspase-7 can serve as a "backup" to caspase-3 in certain developmental contexts, though caspase-3 is considered the dominant executioner in most apoptotic settings (mustafa2024apoptosisacomprehensive pages 2-4).

## Summary

Human caspase-3 (CASP3, UniProt P42574) is the central executioner caspase in programmed cell death, functioning as a cysteine-dependent, aspartate-specific protease (EC 3.4.22.56) with a preferred cleavage motif of DEVD↓(G/S/A). The enzyme is activated downstream of initiator caspases-9 and -8 in the intrinsic (mitochondrial) and extrinsic (death receptor) apoptotic pathways, respectively, and cleaves over 900 protein substrates to produce the biochemical and morphological hallmarks of apoptosis. Beyond its canonical role in cell death, recent research (2022-2025) has established important non-apoptotic functions for caspase-3, including promotion of cytoprotective autophagy, suppression of inflammatory signaling during stress, regulation of neuronal plasticity and synaptic remodeling, facilitation of neural stem cell differentiation, and context-dependent roles in oncogenic transformation. The protein functions primarily in the cytoplasm and nucleus, where the majority of its substrates are localized. Understanding caspase-3's multifaceted roles in both apoptotic and non-apoptotic contexts is essential for developing targeted therapeutic strategies in cancer, neurodegenerative diseases, and other conditions where cell fate decisions are dysregulated.

References

1. (malireddi2025threedecadesof pages 1-3): RKS Malireddi and TD Kanneganti. Three decades of caspases and ripks in life and death. Human molecular genetics, Jul 2025. URL: https://doi.org/10.1093/hmg/ddaf106, doi:10.1093/hmg/ddaf106. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (araya2021deorphanizingcaspase3and pages 1-3): Luam E. Araya, Ishankumar V. Soni, Jeanne A. Hardy, and Olivier Julien. Deorphanizing caspase-3 and caspase-9 substrates in and out of apoptosis with deep substrate profiling. ACS chemical biology, 16:2280-2296, Sep 2021. URL: https://doi.org/10.1021/acschembio.1c00456, doi:10.1021/acschembio.1c00456. This article has 157 citations and is from a domain leading peer-reviewed journal.

3. (blais2026usingabioluminescence pages 2-3): Véronique Blais and Jean-Bernard Denault. Using a bioluminescence resonance energy transfer caspase biosensor to study caspase-3 cleavage site specificity. Bioscience Reports, Mar 2026. URL: https://doi.org/10.1042/bsr20254030, doi:10.1042/bsr20254030. This article has 0 citations and is from a peer-reviewed journal.

4. (mustafa2024apoptosisacomprehensive pages 2-4): Mohd Mustafa, Rizwan Ahmad, Irfan Qadir Tantry, Waleem Ahmad, Sana Siddiqui, Mudassir Alam, Kashif Abbas, Moinuddin, Md. Imtaiyaz Hassan, Safia Habib, and Sidra Islam. Apoptosis: a comprehensive overview of signaling pathways, morphological changes, and physiological significance and therapeutic implications. Cells, 13:1838, Nov 2024. URL: https://doi.org/10.3390/cells13221838, doi:10.3390/cells13221838. This article has 545 citations.

5. (mustafa2024apoptosisacomprehensive pages 7-9): Mohd Mustafa, Rizwan Ahmad, Irfan Qadir Tantry, Waleem Ahmad, Sana Siddiqui, Mudassir Alam, Kashif Abbas, Moinuddin, Md. Imtaiyaz Hassan, Safia Habib, and Sidra Islam. Apoptosis: a comprehensive overview of signaling pathways, morphological changes, and physiological significance and therapeutic implications. Cells, 13:1838, Nov 2024. URL: https://doi.org/10.3390/cells13221838, doi:10.3390/cells13221838. This article has 545 citations.

6. (soni2021caspase9activationof pages 1-3): Ishankumar V. Soni and Jeanne A. Hardy. Caspase-9 activation of procaspase-3 but not procaspase-6 is based on the local context of cleavage site motifs and on sequence. Biochemistry, 60:2824-2835, Sep 2021. URL: https://doi.org/10.1021/acs.biochem.1c00459, doi:10.1021/acs.biochem.1c00459. This article has 20 citations and is from a peer-reviewed journal.

7. (araya2021deorphanizingcaspase3and pages 4-6): Luam E. Araya, Ishankumar V. Soni, Jeanne A. Hardy, and Olivier Julien. Deorphanizing caspase-3 and caspase-9 substrates in and out of apoptosis with deep substrate profiling. ACS chemical biology, 16:2280-2296, Sep 2021. URL: https://doi.org/10.1021/acschembio.1c00456, doi:10.1021/acschembio.1c00456. This article has 157 citations and is from a domain leading peer-reviewed journal.

8. (samarasekera2025caspase3and pages 1-2): Gayathri Samarasekera, Nancy E. Go, Courtney Choutka, Jing Xu, Yuka Takemon, Jennifer Chan, Michelle Chan, Shivani Perera, Samuel Aparicio, Gregg B. Morin, Marco A. Marra, Suganthi Chittaranjan, and Sharon M. Gorski. Caspase 3 and caspase 7 promote cytoprotective autophagy and the dna damage response during non-lethal stress conditions in human breast cancer cells. Feb 2025. URL: https://doi.org/10.1371/journal.pbio.3003034, doi:10.1371/journal.pbio.3003034. This article has 11 citations and is from a highest quality peer-reviewed journal.

9. (killarney2023executionercaspasesrestrict pages 1-2): Shane T. Killarney, Rachel Washart, Ryan S. Soderquist, Jacob P. Hoj, Jamie Lebhar, Kevin H. Lin, and Kris C. Wood. Executioner caspases restrict mitochondrial rna-driven type i ifn induction during chemotherapy-induced apoptosis. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-37146-z, doi:10.1038/s41467-023-37146-z. This article has 42 citations and is from a highest quality peer-reviewed journal.

10. (zhou2024diversefunctionsof pages 1-2): Zhuan Zhou, Tasnim Arroum, Xu Luo, Rui Kang, Yong J. Lee, Daolin Tang, Maik Hüttemann, and Xinxin Song. Diverse functions of cytochrome c in cell death and disease. Cell death and differentiation, 31:387-404, Mar 2024. URL: https://doi.org/10.1038/s41418-024-01284-8, doi:10.1038/s41418-024-01284-8. This article has 182 citations and is from a domain leading peer-reviewed journal.

11. (tannous2025supersensitivechemiluminescentprobe pages 1-3): Rozan Tannous, Chi Zhang, and Doron Shabat. Super-sensitive chemiluminescent probe for the detection of caspase‑3 activity. Bioconjugate Chemistry, 36:1113-1120, May 2025. URL: https://doi.org/10.1021/acs.bioconjchem.5c00151, doi:10.1021/acs.bioconjchem.5c00151. This article has 3 citations and is from a peer-reviewed journal.

12. (mustafa2024apoptosisacomprehensive pages 5-7): Mohd Mustafa, Rizwan Ahmad, Irfan Qadir Tantry, Waleem Ahmad, Sana Siddiqui, Mudassir Alam, Kashif Abbas, Moinuddin, Md. Imtaiyaz Hassan, Safia Habib, and Sidra Islam. Apoptosis: a comprehensive overview of signaling pathways, morphological changes, and physiological significance and therapeutic implications. Cells, 13:1838, Nov 2024. URL: https://doi.org/10.3390/cells13221838, doi:10.3390/cells13221838. This article has 545 citations.

13. (rosa2024nonapoptoticcaspaseevents pages 1-2): Frédéric Rosa, Nicolas Dray, and Laure Bally-Cuif. Non-apoptotic caspase events and atf3 expression underlie direct neuronal differentiation of adult neural stem cells. Development (Cambridge, England), Mar 2024. URL: https://doi.org/10.1242/dev.204381, doi:10.1242/dev.204381. This article has 6 citations.

14. (fieblinger2022nonapoptoticcaspase3activation pages 1-2): Tim Fieblinger, Chang Li, Elena Espa, and M. Angela Cenci. Non-apoptotic caspase-3 activation mediates early synaptic dysfunction of indirect pathway neurons in the parkinsonian striatum. International Journal of Molecular Sciences, 23:5470, May 2022. URL: https://doi.org/10.3390/ijms23105470, doi:10.3390/ijms23105470. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](CASP3-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](CASP3-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. malireddi2025threedecadesof pages 1-3
2. blais2026usingabioluminescence pages 2-3
3. tannous2025supersensitivechemiluminescentprobe pages 1-3
4. mustafa2024apoptosisacomprehensive pages 7-9
5. killarney2023executionercaspasesrestrict pages 1-2
6. rosa2024nonapoptoticcaspaseevents pages 1-2
7. mustafa2024apoptosisacomprehensive pages 2-4
8. zhou2024diversefunctionsof pages 1-2
9. mustafa2024apoptosisacomprehensive pages 5-7
10. https://doi.org/10.1093/hmg/ddaf106,
11. https://doi.org/10.1021/acschembio.1c00456,
12. https://doi.org/10.1042/bsr20254030,
13. https://doi.org/10.3390/cells13221838,
14. https://doi.org/10.1021/acs.biochem.1c00459,
15. https://doi.org/10.1371/journal.pbio.3003034,
16. https://doi.org/10.1038/s41467-023-37146-z,
17. https://doi.org/10.1038/s41418-024-01284-8,
18. https://doi.org/10.1021/acs.bioconjchem.5c00151,
19. https://doi.org/10.1242/dev.204381,
20. https://doi.org/10.3390/ijms23105470,