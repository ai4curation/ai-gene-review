---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T13:09:24.986203'
end_time: '2026-10-09T13:28:41.531027'
duration_seconds: 1156.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Dph1
  gene_symbol: Dph1
  uniprot_accession: Q9VTM2
  protein_description: 'RecName: Full=2-(3-amino-3-carboxypropyl)histidine synthase
    subunit 1 {ECO:0000256|ARBA:ARBA00021915}; EC=2.5.1.108 {ECO:0000256|ARBA:ARBA00012221};
    AltName: Full=Diphthamide biosynthesis protein 1 {ECO:0000256|ARBA:ARBA00032574};
    AltName: Full=Diphtheria toxin resistance protein 1 {ECO:0000256|ARBA:ARBA00032789};
    AltName: Full=S-adenosyl-L-methionine:L-histidine 3-amino-3-carboxypropyltransferase
    1 {ECO:0000256|ARBA:ARBA00031690};'
  gene_info: Name=Dph1 {ECO:0000313|EMBL:AAF50025.1, ECO:0000313|FlyBase:FBgn0036194};
    Synonyms=Dmel\CG11652 {ECO:0000313|EMBL:AAF50025.1}; ORFNames=CG11652 {ECO:0000313|EMBL:AAF50025.1,
    ECO:0000313|FlyBase:FBgn0036194}, Dmel_CG11652 {ECO:0000313|EMBL:AAF50025.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the DPH1/DPH2 family. DPH1 subfamily.
  protein_domains: DPH1/DPH2. (IPR016435); DPH1/DPH2_1. (IPR042263); DPH1/DPH2_2.
    (IPR042264); DPH1/DPH2_3. (IPR042265); Diphthamide_syn (PF01866)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 59
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dph1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9VTM2
- **Protein Description:** RecName: Full=2-(3-amino-3-carboxypropyl)histidine synthase subunit 1 {ECO:0000256|ARBA:ARBA00021915}; EC=2.5.1.108 {ECO:0000256|ARBA:ARBA00012221}; AltName: Full=Diphthamide biosynthesis protein 1 {ECO:0000256|ARBA:ARBA00032574}; AltName: Full=Diphtheria toxin resistance protein 1 {ECO:0000256|ARBA:ARBA00032789}; AltName: Full=S-adenosyl-L-methionine:L-histidine 3-amino-3-carboxypropyltransferase 1 {ECO:0000256|ARBA:ARBA00031690};
- **Gene Information:** Name=Dph1 {ECO:0000313|EMBL:AAF50025.1, ECO:0000313|FlyBase:FBgn0036194}; Synonyms=Dmel\CG11652 {ECO:0000313|EMBL:AAF50025.1}; ORFNames=CG11652 {ECO:0000313|EMBL:AAF50025.1, ECO:0000313|FlyBase:FBgn0036194}, Dmel_CG11652 {ECO:0000313|EMBL:AAF50025.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the DPH1/DPH2 family. DPH1 subfamily.
- **Key Domains:** DPH1/DPH2. (IPR016435); DPH1/DPH2_1. (IPR042263); DPH1/DPH2_2. (IPR042264); DPH1/DPH2_3. (IPR042265); Diphthamide_syn (PF01866)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dph1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dph1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dph1** (gene ID: Dph1, UniProt: Q9VTM2) in DROME.

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
- **UniProt Accession:** Q9VTM2
- **Protein Description:** RecName: Full=2-(3-amino-3-carboxypropyl)histidine synthase subunit 1 {ECO:0000256|ARBA:ARBA00021915}; EC=2.5.1.108 {ECO:0000256|ARBA:ARBA00012221}; AltName: Full=Diphthamide biosynthesis protein 1 {ECO:0000256|ARBA:ARBA00032574}; AltName: Full=Diphtheria toxin resistance protein 1 {ECO:0000256|ARBA:ARBA00032789}; AltName: Full=S-adenosyl-L-methionine:L-histidine 3-amino-3-carboxypropyltransferase 1 {ECO:0000256|ARBA:ARBA00031690};
- **Gene Information:** Name=Dph1 {ECO:0000313|EMBL:AAF50025.1, ECO:0000313|FlyBase:FBgn0036194}; Synonyms=Dmel\CG11652 {ECO:0000313|EMBL:AAF50025.1}; ORFNames=CG11652 {ECO:0000313|EMBL:AAF50025.1, ECO:0000313|FlyBase:FBgn0036194}, Dmel_CG11652 {ECO:0000313|EMBL:AAF50025.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the DPH1/DPH2 family. DPH1 subfamily.
- **Key Domains:** DPH1/DPH2. (IPR016435); DPH1/DPH2_1. (IPR042263); DPH1/DPH2_2. (IPR042264); DPH1/DPH2_3. (IPR042265); Diphthamide_syn (PF01866)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Dph1" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Dph1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Dph1** (gene ID: Dph1, UniProt: Q9VTM2) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Comprehensive Research Report: Dph1 (CG11652, UniProt Q9VTM2) in *Drosophila melanogaster*

## Executive Summary

Dph1 (gene symbol: *Dph1*; gene identifier: CG11652; UniProt accession: Q9VTM2) is a highly conserved eukaryotic protein in the fruit fly *Drosophila melanogaster* that belongs to the DPH1/DPH2 family and participates in the first committed step of diphthamide biosynthesis (cina2019forwardgeneticscreen pages 37-44, utkur2024functionalintegrityof pages 2-4). The fly Dph1 protein forms a heterodimeric radical S-adenosylmethionine (SAM) enzyme complex with Dph2, catalyzing the transfer of a 3-amino-3-carboxypropyl (ACP) group from SAM to a conserved histidine residue in eukaryotic translation elongation factor 2 (eEF2), thereby initiating a multi-step post-translational modification pathway that supports translational fidelity (dong2014dph3isan pages 1-2, shin2023eef2diphthamidemodification pages 1-2). This report synthesizes current understanding of Dph1 function, experimental evidence from *Drosophila* genetics, mechanistic insights from yeast and mammalian studies, and recent 2023–2024 advances.

---

## 1. Key Concepts and Definitions

### 1.1 Diphthamide and Its Biosynthesis

Diphthamide is a unique, highly conserved post-translational modification found exclusively on a single histidine residue of eEF2 in eukaryotes and archaeal EF2 homologues (zhao2024lossofdiphthamide pages 1-2, shin2023eef2diphthamidemodification pages 1-2). The modification is named after its original identification as the molecular target of diphtheria toxin, which catalyzes ADP-ribosylation of diphthamide, thereby inactivating eEF2 and inhibiting protein translation (utkur2024functionalintegrityof pages 1-2, shin2023eef2diphthamidemodification pages 13-13). The biosynthesis of diphthamide in eukaryotes requires seven dedicated proteins (Dph1–Dph7) and proceeds in four chemically distinct steps (zhao2024lossofdiphthamide pages 1-2):

1. **First step (ACP attachment):** Dph1, Dph2, Dph3, and Dph4 catalyze the transfer of the ACP moiety of SAM to the imidazole-C2 atom of the target eEF2 histidine through a non-canonical radical-SAM reaction, forming the ACP-modified intermediate (zhang2025diphthamideformationin pages 1-4, dong2014dph3isan pages 1-2).
2. **Second step (methylation):** Dph5 methylates both the amino and carboxyl groups of the ACP intermediate (lin2016functionalstudiesof pages 43-48).
3. **Third step (demethylation):** Dph7 hydrolyzes the carboxyl methyl ester to produce diphthine (lin2016functionalstudiesof pages 43-48).
4. **Fourth step (amidation):** Dph6 uses ATP and ammonium to amidate the diphthine carboxyl group, completing diphthamide (zhao2024lossofdiphthamide pages 1-2).

In humans and yeast, the acceptor histidine is His715 (human eEF2) and His699 (yeast eEF2), respectively (zhao2024lossofdiphthamide pages 1-2, shin2023eef2diphthamidemodification pages 1-2). The equivalent histidine is conserved in *Drosophila* eEF2 (obata2018nutritionalcontrolof pages 4-5, tsuda‐sakurai2020diphthamidemodificationof pages 1-5), though fly-specific residue numbering was not established in the reviewed literature.

### 1.2 Dph1: Identity and Protein Family

The fly protein encoded by *Dph1* (official gene name, CG11652, UniProt Q9VTM2) was unambiguously verified as belonging to the DPH1/DPH2 family in cross-species alignments that included humans, mice, *Arabidopsis*, and yeast, which confirmed conservation of the noncanonical Fe-S cluster coordination motifs (utkur2024functionalintegrityof pages 2-4). No homonymous fly gene or protein was detected (cina2019forwardgeneticscreen pages 37-44). Q9VTM2 is annotated as a 2-(3-amino-3-carboxypropyl)histidine synthase subunit 1, with enzyme commission number EC 2.5.1.108 and alternative names including diphthamide biosynthesis protein 1 and diphtheria toxin resistance protein 1 (utkur2024functionalintegrityof pages 2-4). It is therefore functionally equivalent to the yeast Saccharomyces cerevisiae Dph1 and human DPH1 studied in the mechanistic literature (utkur2024functionalintegrityof pages 1-2, dong2019theasymmetricfunction pages 1-2).

### 1.3 Mechanistic Role: Radical-SAM Chemistry and the Dph1–Dph2 Heterodimer

Dph1 and Dph2 form an obligate heterodimeric radical-SAM enzyme complex (dong2019theasymmetricfunction pages 1-2, dong2014dph3isan pages 1-2). Each subunit harbors an atypical [4Fe-4S] cluster whose cysteine ligands differ from canonical radical-SAM motifs (utkur2024functionalintegrityof pages 1-2). Reconstituted yeast Dph1-Dph2 in vitro was sufficient for the first-step reaction when supplied with SAM, eEF2, and chemical reductant, and later work distinguished the functional asymmetry of the two subunits: the Dph1 cluster is essential for catalytic activity, whereas the Dph2 cluster primarily facilitates physiological reduction of Dph1 by the endogenous electron-donor system, which in yeast comprises Dph3 and NADH-dependent Cbr1 (dong2019theasymmetricfunction pages 1-2, dong2014dph3isan pages 1-2). The enzyme cleaves the SAM Cγ-S bond, generating an organometallic Fe-C intermediate; subsequent homolysis releases the ACP radical, which adds to the histidine side chain of eEF2 (su2013thebiosynthesisand pages 3-4, yugang2021investigationofunique pages 17-22). Structural modeling and 2023 site-directed mutagenesis studies predicted a conserved SAM-binding pocket localized in Dph1 rather than Dph2; four of six tested yeast Dph1 substitutions (G238A, H261A, R370A, D374A) impaired diphthamide synthesis in vivo (utkur2023dph1genemutations pages 4-6, utkur2023dph1genemutations pages 1-2).

---

## 2. Recent Developments and Latest Research (2023–2024)

### 2.1 Fe-S Cluster Stability and Tandem Cysteines (2024)

Ütkür et al. (April 2024, *Biomolecules*, https://doi.org/10.3390/biom14040470) demonstrated that conserved tandem-cysteine motifs (TCMs) in both Dph1 and Dph2 subunits are functionally critical for enzyme stability and activity (utkur2024functionalintegrityof pages 2-4, utkur2024functionalintegrityof pages 1-2). Combined replacement of yeast Dph2 Cys106 and Cys107 with serines nearly abolished the radical-SAM activity in vivo, whereas single substitutions had mild defects (utkur2024functionalintegrityof pages 4-6, utkur2024functionalintegrityof pages 8-10). Cycloheximide-chase experiments revealed that Cys substitutions in cofactor motifs accelerated degradation of both subunits (utkur2024functionalintegrityof pages 8-10). Q9VTM2 and its partner fly Dph2 (Q9VFE9) were confirmed to possess these conserved cysteine motifs (utkur2024functionalintegrityof pages 2-4), though functional assays were performed in yeast.

### 2.2 SAM-Binding Pocket Identification (2023)

Ütkür et al. (November 2023, *Biomolecules*, https://doi.org/10.3390/biom13111655) used AlphaFold/ColabFold modeling guided by archaeal *Candidatus methanoperedens nitroreducens* Dph2 structure to predict a SAM pocket near the Fe-S cluster domain in yeast Dph1 (utkur2023dph1genemutations pages 4-6, utkur2023dph1genemutations pages 1-2). Site-directed DPH1 mutagenesis at residues close to the methionine moiety of SAM (G238, H261, R370, D374) resulted in diphthamide-deficiency phenotypes, confirming that these residues are essential for SAM recognition and ACP radical formation, which distinguishes Dph1•Dph2 from canonical radical-SAM enzymes (utkur2023dph1genemutations pages 4-6, utkur2023dph1genemutations pages 1-2). The corresponding region of fly Dph1 (Q9VTM2) was modeled but not directly tested.

### 2.3 Translational Fidelity: Frameshifting and Ribosome Dynamics (2023)

Shin et al. (May 2023, *Nucleic Acids Research*, https://doi.org/10.1093/nar/gkad461) provided the first systematic demonstration that loss of diphthamide increases non-programmed −1 ribosomal frameshifting throughout translation elongation, as well as enhancing viral programmed frameshifting (shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-2). Yeast and mammalian ribosome profiling revealed that diphthamide-deficient cells accumulate ribosomal drop-off and premature termination at out-of-frame stop codons (shin2023eef2diphthamidemodification pages 1-1). In vitro reconstituted translation assays showed that approximately four-fold higher concentrations of ADP-ribosylated eEF2 (relative to unmodified) were required to maintain normal peptide synthesis rates (shin2023eef2diphthamidemodification pages 13-13), confirming that the diphthamide modification stabilizes eEF2's productive engagement with elongating ribosomes. This 2023 study resolved a long-standing controversy over diphthamide's specific role in translocation versus general translation.

### 2.4 Mammalian RRM1 Regulation and DNA Replication Stress (2024)

Zhao et al. (September 2024, *ACS Central Science*, https://doi.org/10.1021/acscentsci.4c00967) integrated computational frameshifting-motif prediction with quantitative proteomics of DPH4-knockout HEK293T cells and identified ribonucleotide reductase subunit 1 (RRM1) as a diphthamide-sensitive target whose translation is regulated by −1 frameshifting (zhao2024lossofdiphthamide pages 1-2, zhao2024lossofdiphthamide pages 2-4). Loss of diphthamide caused slower cell doubling time, elevated γ-H2AX foci, hyperphosphorylated RPA32, and replication-fork stalling, which were partially rescued by RRM1 overexpression (zhao2024lossofdiphthamide pages 2-4). This is the first example of a specific human mRNA whose translation is quantitatively altered by diphthamide deficiency and provides a mechanistic link to genome stability and carcinogenesis.

### 2.5 Arabidopsis DPH1 and Localization Evidence (2024–2025)

Zhang et al. (preprint posted September 2024, *BioRxiv*, https://doi.org/10.1101/2024.09.16.613322) demonstrated that *Arabidopsis thaliana* DPH1 is required for eEF2 diphthamide and that approximately 96% of plant eEF2 carries the modification (zhang2025diphthamideformationin pages 1-4). The study also showed that AtDPH2 localizes to the cytosol by confocal microscopy of a DPH2-GFP reporter line and physically interacts with AtDPH1 by co-immunoprecipitation and bimolecular fluorescence complementation (zhang2025diphthamideformationin pages 1-4, zhang2025diphthamideformationin pages 52-56). However, no direct fluorescence or cellular-fractionation localization data for AtDPH1 protein were provided (zhang2025diphthamideformationin pages 1-4). Because eEF2 is a cytosolic translational GTPase, Dph1 is strongly inferred to function in the cytosol; however, fly-specific subcellular-localization experiments for Q9VTM2 were not found in the literature (zhang2025diphthamideformationin pages 1-4).

---

## 3. Current Applications and Real-World Implementations

### 3.1 *Drosophila* Intestinal Stem-Cell Division and Metabolic Signaling (2018)

Obata et al. (March 2018, *Developmental Cell*, https://doi.org/10.1016/j.devcel.2018.02.017) discovered that S-adenosylmethionine (SAM), synthesized from dietary methionine, controls intestinal stem-cell (ISC) division in adult fly midgut (obata2018nutritionalcontrolof pages 1-3, obata2018nutritionalcontrolof pages 5-6). A genetic screen for SAM-dependent methyltransferases identified Dph5, and ISC-specific RNAi confirmed that both Dph1 and eEF2 are required for ISC division after induced damage or refeeding (obata2018nutritionalcontrolof pages 5-6, obata2018nutritionalcontrolof pages 4-5). Five days of methionine deprivation reduced whole-body methionine to less than 5% of control (obata2018nutritionalcontrolof pages 3-3), and supplementation with 5 mM SAM partially rescued damage-induced ISC proliferation (obata2018nutritionalcontrolof pages 3-3). Dph1/Dph5 RNAi reduced EdU incorporation without lowering ISC numbers, indicating proliferation defects rather than cell loss (obata2018nutritionalcontrolof pages 4-5). Nascent protein synthesis, monitored by HPG (methionine analogue) incorporation in progenitor cells, was diminished by either SamS or Dph5 knockdown (obata2018nutritionalcontrolof pages 5-6). These results established that diphthamide synthesis is sensitive to methionine availability and essential for SAM-dependent control of protein synthesis and ISC activity in *Drosophila* (obata2018nutritionalcontrolof pages 6-7, obata2018nutritionalcontrolof pages 7-8).

### 3.2 Nephrocyte Function in *Drosophila* (2019)

Cinà et al. (December 2019, *American Journal of Physiology-Renal Physiology*, https://doi.org/10.1152/ajprenal.00195.2019) performed a genome-scale RNAi screen in cultured human podocytes and identified the diphthamide biosynthesis genes as regulators of cell adhesion (cina2019forwardgeneticscreen pages 37-44). They further validated these findings in *Drosophila* nephrocytes, which are specialized filtration cells functionally analogous to mammalian podocytes. Nephrocyte-specific RNAi using Dot-Gal4 driver significantly reduced ANF-RFP uptake (an in-vivo readout of nephrocyte filtration capacity) for Dph1 (p=0.0036), Dph2 (p=0.0001), and Dph4 (p=0.0162), while Dph3 RNAi did not significantly alter uptake (cina2019forwardgeneticscreen pages 37-44). Public transcriptomic data indicated moderate expression of CG11652 (Dph1) in fly nephrocytes (cina2019forwardgeneticscreen pages 37-44). This work provided direct, quantitative genetic evidence that Dph1 supports nephrocyte function in vivo.

### 3.3 Oncogenic Ras-Induced Hyperplasia in Fly Gut (2020)

Tsuda-Sakurai et al. (January 2020, *Genes to Cells*, https://doi.org/10.1111/gtc.12742) examined diphthamide's role in tumor-like overgrowth in adult fly intestine by expressing oncogenic Ras-V12 in progenitor cells (tsuda‐sakurai2020diphthamidemodificationof pages 1-5). Knockdown of Dph5 ameliorated Ras-V12-induced EdU incorporation, tissue hypertrophy, epithelial disruption, and shortened lifespan (tsuda‐sakurai2020diphthamidemodificationof pages 1-5). Dph5 was required for the elevated translation observed in Ras-V12 guts, as well as for high dMyc protein levels (tsuda‐sakurai2020diphthamidemodificationof pages 1-5). Transcriptome analysis suggested that Dph5 is involved in regulating ribosome-biogenesis genes (tsuda‐sakurai2020diphthamidemodificationof pages 1-5). This study demonstrated that completed diphthamide is essential for translation activation and proliferation downstream of oncogenic Ras signaling in *Drosophila*, linking the Dph1 pathway to a model of tumorigenesis.

---

## 4. Expert Opinions and Analysis from Authoritative Sources

### 4.1 Conservation and Non-Essentiality Paradox

Diphthamide synthesis is evolutionarily conserved from archaea to humans, yet diphthamide biosynthesis genes are non-essential for viability in yeast and mammalian cell culture (shin2023eef2diphthamidemodification pages 1-2). However, complete DPH gene knockouts in mice are embryonic lethal, and humans with partial loss-of-function mutations in DPH1, DPH2, or DPH5 exhibit diphthamide deficiency syndrome characterized by intellectual disability, developmental abnormalities, and craniofacial features (utkur2023dph1anddph2 pages 1-2). Schaffrath and colleagues have emphasized that the costly multi-enzyme, multi-SAM pathway is maintained because diphthamide provides a selective advantage by maintaining translational fidelity under stress or high-demand conditions, despite its vulnerability as a toxin target (utkur2024functionalintegrityof pages 1-2, shin2023eef2diphthamidemodification pages 1-2). The 2023 ribosome profiling studies by Shin et al. support this interpretation, showing that the modification restrains spurious frameshifting and processivity defects genome-wide (shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-1).

### 4.2 Dph3 as Electron Donor and Regulatory Linkage

Dong et al. (January 2014, *Journal of the American Chemical Society*, https://doi.org/10.1021/ja4118957) established through in vitro reconstitution that yeast Dph3, a CSL-type zinc-finger protein, binds iron and, in the reduced state, serves as an electron donor to reduce the Fe-S clusters in Dph1-Dph2 (dong2014dph3isan pages 1-2). This finding opened new avenues into understanding electron transfer to eukaryotic cytosolic Fe-S proteins, because most bacterial radical-SAM enzymes use flavodoxins and flavodoxin reductases (dong2014dph3isan pages 1-2). A subsequent study identified cytochrome b5 reductase (Cbr1) as the NADH-dependent reductase for Dph3, thereby coupling diphthamide synthesis to cellular redox state and potentially linking metabolism to translation (zhang2025diphthamideformationin pages 66-69). These mechanistic insights provide a framework for understanding how Drosophila methionine/SAM availability could regulate ISC proliferation: both SAM as the substrate and cellular NADH-dependent reduction of Dph3 are required for Dph1-Dph2 activity (obata2018nutritionalcontrolof pages 6-7).

### 4.3 Substrate Specificity: Protein vs. Free Amino Acid

It is essential to emphasize that Dph1-Dph2 does not modify free histidine or any histidine-containing peptide; it requires the intact three-dimensional structure of eEF2 and specifically recognizes the conserved histidine residue within domain IV of the translation factor (su2013thebiosynthesisand pages 3-4, zhao2024lossofdiphthamide pages 1-2). This exquisite substrate specificity explains why the diphthamide modification is found on only one protein in the entire eukaryotic proteome (zhao2024lossofdiphthamide pages 1-2) and underscores that Dph1's biological function is inseparable from eEF2 function in protein translation (shin2023eef2diphthamidemodification pages 1-2).

---

## 5. Relevant Statistics and Data from Recent Studies

### 5.1 Quantitative Fly Genetic Phenotypes

- Nephrocyte RNAi (Cinà et al. 2019): Dph1 RNAi p=0.0036; Dph2 RNAi p=0.0001; Dph4 RNAi p=0.0162 for reduced uptake (cina2019forwardgeneticscreen pages 37-44).
- Methionine depletion (Obata et al. 2018): Five days without methionine reduced whole-body methionine to <5% of control (obata2018nutritionalcontrolof pages 3-3). Supplementation with 5 mM SAM rescued bleomycin-induced ISC proliferation defects (obata2018nutritionalcontrolof pages 3-3).
- Diphthamide synthesis consumes five molecules of SAM per eEF2 modification, indicating significant metabolic investment (obata2018nutritionalcontrolof pages 4-5, tsuda‐sakurai2020diphthamidemodificationof pages 1-5).

### 5.2 Yeast Protein Stability (2024)

Ütkür et al. (2024) reported that Dph1 variants with cysteine substitutions declined to 25–38% of wild-type abundance after cycloheximide treatment, while corresponding Dph2 levels were 13–27% (utkur2024functionalintegrityof pages 8-10). In Dph2 mutants, Dph2 abundance was retained at 40–71%, and Dph1 at 30–56% (utkur2024functionalintegrityof pages 8-10). This asymmetry underscores the interdependence of the two subunits for structural stability.

### 5.3 Translational Fidelity and Frameshifting (2023)

Earlier studies reported approximately 1.5- to 2-fold increases in programmed −1 frameshifting on viral L-A and HIV sites in diphthamide-deficient yeast (shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-2). The 2023 Shin study extended this to genome-wide non-programmed frameshifting and showed that ADP-ribosylation of diphthamide required roughly four-fold higher eEF2 concentration to achieve normal translation rates in vitro (shin2023eef2diphthamidemodification pages 13-13).

### 5.4 Mammalian DNA Damage (2024)

Zhao et al. (2024) observed that HEK293T DPH4-knockout cells had significantly elevated γ-H2AX foci and phosphorylated RPA32 (Thr21), indicating elevated DNA replication stress (zhao2024lossofdiphthamide pages 1-2, zhao2024lossofdiphthamide pages 2-4). This was mechanistically linked to dysregulated RRM1 translation via −1 frameshifting (zhao2024lossofdiphthamide pages 2-4).

---

## 6. Synthesis and Conclusion

The *Drosophila melanogaster* Dph1 protein (CG11652, Q9VTM2) is a central component of the conserved eukaryotic diphthamide biosynthesis pathway. It forms an obligate heterodimeric radical-SAM enzyme complex with Dph2, together catalyzing the first committed step: the transfer of a 3-amino-3-carboxypropyl group from S-adenosylmethionine to a conserved histidine residue on eEF2 through a noncanonical [4Fe-4S]-dependent radical reaction (dong2019theasymmetricfunction pages 1-2, dong2014dph3isan pages 1-2). This initial reaction requires Dph3 as an electron donor and is supported by Dph4; subsequent steps by Dph5, Dph7, and Dph6 complete the modification (zhao2024lossofdiphthamide pages 1-2, dong2014dph3isan pages 1-2, lin2016functionalstudiesof pages 43-48). The primary function of this post-translational modification is to maintain translational fidelity by restraining spurious −1 ribosomal frameshifting and premature ribosome drop-off during translation elongation (shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-2).

Direct genetic evidence in *Drosophila* demonstrates that Dph1 is essential for intestinal stem-cell proliferation in response to tissue damage and refeeding (obata2018nutritionalcontrolof pages 5-6, obata2018nutritionalcontrolof pages 4-5), for nephrocyte filtration capacity (cina2019forwardgeneticscreen pages 37-44), and for oncogenic Ras-driven tissue hyperplasia when assessed through downstream diphthamide pathway activity (tsuda‐sakurai2020diphthamidemodificationof pages 1-5). The enzyme's dependence on dietary methionine and SAM links nutrient availability to translational capacity and stem-cell homeostasis (obata2018nutritionalcontrolof pages 6-7, obata2018nutritionalcontrolof pages 3-3).

Recent 2023–2024 mechanistic advances include: (1) identification of a conserved SAM-binding pocket in Dph1 (utkur2023dph1genemutations pages 4-6, utkur2023dph1genemutations pages 1-2); (2) demonstration that tandem cysteine motifs are critical for Fe-S cluster stability and enzyme activity (utkur2024functionalintegrityof pages 2-4, utkur2024functionalintegrityof pages 8-10, utkur2024functionalintegrityof pages 1-2); (3) genome-wide ribosome profiling showing that diphthamide restrains frameshifting throughout elongation (shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-1, shin2023eef2diphthamidemodification pages 1-2); and (4) the first identification of a specific human mRNA (RRM1) whose translation is modulated by diphthamide-dependent frameshifting, with consequences for DNA replication stress (zhao2024lossofdiphthamide pages 1-2, zhao2024lossofdiphthamide pages 2-4).

Cellular localization of Dph1 is inferred to be cytosolic based on the cytosolic localization of its substrate eEF2 and direct localization data for plant DPH2 (zhang2025diphthamideformationin pages 1-4, zhang2025diphthamideformationin pages 52-56), though fly-specific imaging of Q9VTM2 has not been reported. Together, these studies establish that Dph1 is not a standalone transferase but rather a catalytic subunit within a multi-protein, multi-cofactor system whose activity integrates metabolic status (SAM, NADH), protein quality control (translational fidelity), and tissue-specific physiological demands (ISC proliferation, nephrocyte filtration).

| Topic | Principal finding | Evidence and relevance to fly Dph1 | Source |
|---|---|---|---|
| Identity verification | *Drosophila melanogaster* Dph1 is **CG11652**, encoding **UniProt Q9VTM2**, a member of the DPH1/DPH2 family. Q9VTM2 was explicitly identified as fly Dph1 in a 2024 cross-species alignment. | Direct identity evidence; no conflicting homonymous fly protein was found. | Cinà et al., December 2019, [doi:10.1152/ajprenal.00195.2019](https://doi.org/10.1152/ajprenal.00195.2019); Ütkür et al., April 11, 2024, [doi:10.3390/biom14040470](https://doi.org/10.3390/biom14040470) (cina2019forwardgeneticscreen pages 37-44, utkur2024functionalintegrityof pages 2-4, utkur2024functionalintegrityof pages 1-2) |
| Primary function | Dph1 and Dph2 form a **noncanonical radical-SAM heterodimer** that initiates diphthamide synthesis on eEF2. Dph1 is therefore a catalytic-complex component rather than a conventional independent transferase. | Demonstrated with yeast proteins and strongly inferred for Q9VTM2 from family and motif conservation; purified fly Dph1 catalysis has not been reported. | Dong et al., January 2014, [doi:10.1021/ja4118957](https://doi.org/10.1021/ja4118957); Dong et al., August 2019, [doi:10.1007/s00775-019-01702-0](https://doi.org/10.1007/s00775-019-01702-0) (dong2019theasymmetricfunction pages 1-2, dong2014dph3isan pages 1-2) |
| First-step reaction | The complex transfers the **3-amino-3-carboxypropyl (ACP)** group of S-adenosyl-L-methionine (SAM) to the C2 position of the imidazole ring of a conserved eEF2 histidine, creating an ACP-eEF2 C-C bond. Human eEF2 uses His715 and budding-yeast eEF2 His699. | SAM is the cosubstrate and intact eEF2, not free histidine, is the macromolecular acceptor. The equivalent fly eEF2 histidine is predicted to be the substrate, although its residue number was not established in the retrieved fly studies. | Dong et al., January 2014, [doi:10.1021/ja4118957](https://doi.org/10.1021/ja4118957); Zhao et al., September 6, 2024, [doi:10.1021/acscentsci.4c00967](https://doi.org/10.1021/acscentsci.4c00967) (zhao2024lossofdiphthamide pages 1-2, dong2014dph3isan pages 1-2) |
| Radical-SAM chemistry | Dph1-Dph2 uses Fe-S clusters to cleave SAM and generate an **ACP radical**, rather than the canonical 5-prime-deoxyadenosyl radical. The ACP radical adds to the eEF2 histidine ring. | Explains Q9VTM2's ACP-histidine synthase annotation and its Diphthamide_syn/DPH1-DPH2 domains. | Ütkür et al., November 16, 2023, [doi:10.3390/biom13111655](https://doi.org/10.3390/biom13111655); Dong et al., August 2019, [doi:10.1007/s00775-019-01702-0](https://doi.org/10.1007/s00775-019-01702-0) (dong2019theasymmetricfunction pages 1-2, utkur2023dph1genemutations pages 1-2) |
| Fe-S clusters and asymmetry | Yeast Dph1 and Dph2 each carry an atypically coordinated **[4Fe-4S] cluster**. Reconstitution indicates that the Dph1 cluster performs the radical chemistry, whereas the Dph2 cluster facilitates physiological reduction of Dph1 by the Dph3/Cbr1/NADH system. | Direct yeast mechanism and strong fly inference; both subunits remain necessary for normal in-vivo function. | Dong et al., August 2019, [doi:10.1007/s00775-019-01702-0](https://doi.org/10.1007/s00775-019-01702-0) (dong2019theasymmetricfunction pages 1-2) |
| Dph3 | Reduced Dph3 is an iron-binding electron carrier for the Dph1-Dph2 Fe-S machinery. Yeast Dph1-Dph2 catalyzed the reaction with artificial reductant dithionite, while Dph3 supplied physiological electron-transfer activity. | Fly Dph3 is expected to support Q9VTM2 by electron donation rather than catalyzing ACP attachment itself. | Dong et al., January 2014, [doi:10.1021/ja4118957](https://doi.org/10.1021/ja4118957) (dong2014dph3isan pages 1-2) |
| Dph4 | Dph4 is required genetically for the initiating stage and has a J-domain/co-chaperone-related role, but it is not the Dph1-Dph2 catalytic subunit. Its exact contribution may include assembly, activation, or maintenance of the first-step machinery. | Fly Dph4 RNAi phenotypes support pathway involvement but do not demonstrate ACP-transfer catalysis by Dph4. | Zhao et al., September 6, 2024, [doi:10.1021/acscentsci.4c00967](https://doi.org/10.1021/acscentsci.4c00967); Cinà et al., December 2019, [doi:10.1152/ajprenal.00195.2019](https://doi.org/10.1152/ajprenal.00195.2019) (cina2019forwardgeneticscreen pages 37-44, zhao2024lossofdiphthamide pages 1-2) |
| Dph5, Dph7, and Dph6 | After ACP attachment, **Dph5** methylates the ACP amino and carboxyl groups; **Dph7** removes the carboxyl methyl group to produce diphthine; **Dph6** uses ATP and ammonium to amidate diphthine, completing diphthamide. | Places Q9VTM2 specifically at the first committed step. Dph5 phenotypes measure loss of completed diphthamide and are indirect evidence for Dph1 function. | Zhao et al., September 6, 2024, [doi:10.1021/acscentsci.4c00967](https://doi.org/10.1021/acscentsci.4c00967) (zhao2024lossofdiphthamide pages 1-2, lin2016functionalstudiesof pages 43-48) |
| Localization | The reaction modifies cytosolic translation factor eEF2, making a **cytosolic location** likely. Arabidopsis DPH2 was directly localized to the cytosol and shown to interact with AtDPH1. | No direct subcellular-localization experiment for fly Q9VTM2 was retrieved. Cytosolic localization should therefore be labeled as a conserved-function inference, not established fly evidence. | Zhang et al., preprint posted September 16, 2024, [doi:10.1101/2024.09.16.613322](https://doi.org/10.1101/2024.09.16.613322) (zhang2025diphthamideformationin pages 1-4, zhang2025diphthamideformationin pages 52-56) |
| Fly intestinal stem cells | ISC-specific RNAi showed that **Dph1 and eEF2 are required for induced intestinal-stem-cell division**. Dph1/Dph5 RNAi reduced EdU incorporation without lowering ISC number, indicating impaired proliferation rather than stem-cell depletion. | Direct CG11652/Dph1 genetic evidence. Effects were prominent after damage or refeeding and were not general across every proliferative fly tissue. | Obata et al., March 26, 2018, [doi:10.1016/j.devcel.2018.02.017](https://doi.org/10.1016/j.devcel.2018.02.017) (obata2018nutritionalcontrolof pages 4-5, obata2018nutritionalcontrolof pages 5-6) |
| Fly methionine and SAM physiology | Five days without dietary methionine reduced whole-body methionine to **less than 5% of control** and reduced ISC proliferation; **5 mM SAM** rescued the damage-associated proliferative defect. SamS or Dph5 RNAi also reduced nascent-protein labeling. | Direct fly evidence linking methionine-derived SAM to translation and diphthamide-dependent proliferation. Because SAM supports many pathways, Dph1/Dph5/eEF2 genetics are needed for pathway specificity. | Obata et al., March 26, 2018, [doi:10.1016/j.devcel.2018.02.017](https://doi.org/10.1016/j.devcel.2018.02.017) (obata2018nutritionalcontrolof pages 6-7, obata2018nutritionalcontrolof pages 3-3) |
| Fly nephrocytes | Nephrocyte-specific RNAi significantly reduced ANF-RFP uptake for **Dph1 (p=0.0036), Dph2 (p=0.0001), and Dph4 (p=0.0162)**; Dph3 RNAi was not significant. CG11652 showed moderate nephrocyte expression in public transcriptomic data. | Direct fly evidence that Dph1 supports nephrocyte filtration/endocytic function, although the downstream molecular cause was not resolved. | Cinà et al., December 2019, [doi:10.1152/ajprenal.00195.2019](https://doi.org/10.1152/ajprenal.00195.2019) (cina2019forwardgeneticscreen pages 37-44) |
| Fly Ras hyperplasia | In adult fly gut, Dph5 RNAi reduced Ras-V12-induced epithelial overgrowth, EdU incorporation, elevated translation, high dMyc, tissue disorganization, and shortened lifespan. | Direct fly pathway evidence showing that completed diphthamide supports high-output translation in a tumor-like model; it is not a direct Dph1 perturbation. | Tsuda-Sakurai et al., January 2020, [doi:10.1111/gtc.12742](https://doi.org/10.1111/gtc.12742) (tsuda‐sakurai2020diphthamidemodificationof pages 1-5) |
| Candidate SAM pocket, 2023 | Modeling predicted a SAM pocket conserved in Dph1 but not Dph2. Four of six tested yeast Dph1 substitutions, G238A, H261A, R370A, and D374A, caused diphthamide-deficiency phenotypes; Q321A and V349A resembled wild type. | Supports a direct Dph1 contribution to SAM recognition, but it is not a direct SAM-binding measurement for fly Q9VTM2. | Ütkür et al., November 16, 2023, [doi:10.3390/biom13111655](https://doi.org/10.3390/biom13111655) (utkur2023dph1genemutations pages 4-6, utkur2023dph1genemutations pages 1-2) |
| Tandem cysteines, 2024 | Conserved noncanonical tandem-cysteine motifs contribute to Fe-S coordination and Dph1-Dph2 stability. Combined replacement of yeast Dph2 Cys106/Cys107 nearly abolished activity; essential Cys substitutions accelerated degradation of both subunits. Mutant Dph1 abundance was approximately **25-38%** of wild type, with partner Dph2 at **13-27%** in the reported variants. | Fly Q9VTM2 was included in the conservation analysis, but the activity and stability experiments were performed in yeast. | Ütkür et al., April 11, 2024, [doi:10.3390/biom14040470](https://doi.org/10.3390/biom14040470) (utkur2024functionalintegrityof pages 2-4, utkur2024functionalintegrityof pages 8-10, utkur2024functionalintegrityof pages 1-2) |
| Translational fidelity, 2023 | Loss of diphthamide increased nonprogrammed and viral programmed **minus-1 ribosomal frameshifting**, premature termination at out-of-frame stops, and ribosome drop-off. Earlier programmed-site assays showed roughly **1.5- to 2-fold** higher frameshifting without diphthamide. | Demonstrated in yeast and mammalian cells; provides the best current mechanistic explanation for fly Dph1-dependent tissue phenotypes, but is not a direct fly Dph1 measurement. | Shin et al., May 2023, [doi:10.1093/nar/gkad461](https://doi.org/10.1093/nar/gkad461) (shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-1, shin2023eef2diphthamidemodification pages 1-2) |
| Mammalian RRM1 finding, 2024 | Diphthamide-deficient HEK293T cells showed altered RRM1 translation through minus-1 frameshifting, slower growth, elevated gamma-H2AX, RPA32-Thr21 phosphorylation, and replication-fork stress. | Demonstrates a real transcript-specific consequence of diphthamide loss, but the experiment used DPH4-knockout human cells and should not be described as direct fly Dph1 evidence. | Zhao et al., September 6, 2024, [doi:10.1021/acscentsci.4c00967](https://doi.org/10.1021/acscentsci.4c00967) (zhao2024lossofdiphthamide pages 1-2, zhao2024lossofdiphthamide pages 2-4) |
| Diphtheria-toxin target | Mature diphthamide is ADP-ribosylated by diphtheria toxin and related toxins, blocking productive eEF2 action and translation. Dph-deficient cells resist this toxin action because the acceptor modification is absent. | Toxin sensitivity is a useful pathway assay; toxin resistance does not mean that Dph1's normal function is toxin response. Its normal function is eEF2 modification and translational fidelity. | Shin et al., May 2023, [doi:10.1093/nar/gkad461](https://doi.org/10.1093/nar/gkad461); Ütkür et al., April 11, 2024, [doi:10.3390/biom14040470](https://doi.org/10.3390/biom14040470) (utkur2024functionalintegrityof pages 1-2, shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-2) |
| Overall annotation | **Q9VTM2 is the fly Dph1 subunit of the cytosolic eEF2-diphthamide biosynthetic machinery. With Dph2 and Fe-S cofactors, it initiates radical transfer of ACP from SAM to conserved eEF2 histidine; Dph3 supplies reducing equivalents and Dph4 supports the first-stage system. The completed modification stabilizes reading-frame maintenance during ribosomal translocation.** | High confidence for identity and conserved biochemical role; moderate confidence for exact fly subcellular localization; direct fly evidence presently consists mainly of tissue-specific genetics rather than purified-protein enzymology. | Integrated evidence (obata2018nutritionalcontrolof pages 5-6, cina2019forwardgeneticscreen pages 37-44, zhao2024lossofdiphthamide pages 1-2, dong2019theasymmetricfunction pages 1-2, dong2014dph3isan pages 1-2, utkur2023dph1genemutations pages 1-2, shin2023eef2diphthamidemodification pages 1-2) |


*Table: This table distinguishes direct evidence for fly Dph1/CG11652 from mechanistic conclusions inferred from conserved yeast, plant, and mammalian homologues. It summarizes the radical-SAM reaction, pathway partners, localization confidence, fly phenotypes, and key 2018-2024 developments.*

---

## References and URLs (by citation order)

1. Cinà et al. (December 2019). Forward genetic screen in human podocytes identifies diphthamide biosynthesis genes as regulators of adhesion. *American Journal of Physiology-Renal Physiology*, 317(6), F1593–F1604. https://doi.org/10.1152/ajprenal.00195.2019 (cina2019forwardgeneticscreen pages 37-44)

2. Ütkür et al. (April 11, 2024). Functional Integrity of Radical SAM Enzyme Dph1•Dph2 Requires Non-Canonical Cofactor Motifs with Tandem Cysteines. *Biomolecules*, 14(4), 470. https://doi.org/10.3390/biom14040470 (utkur2024functionalintegrityof pages 2-4, utkur2024functionalintegrityof pages 4-6, utkur2024functionalintegrityof pages 8-10, utkur2024functionalintegrityof pages 1-2)

3. Zhang et al. (preprint posted September 16, 2024). Diphthamide formation in Arabidopsis requires DPH1-interacting DPH2 for light and oxidative stress resistance. *BioRxiv*. https://doi.org/10.1101/2024.09.16.613322 (zhang2025diphthamideformationin pages 1-4, zhang2025diphthamideformationin pages 52-56)

4. Dong et al. (January 2014). Dph3 Is an Electron Donor for Dph1-Dph2 in the First Step of Eukaryotic Diphthamide Biosynthesis. *Journal of the American Chemical Society*, 136(5), 1754–1757. https://doi.org/10.1021/ja4118957 (dong2014dph3isan pages 1-2)

5. Obata et al. (March 26, 2018). Nutritional Control of Stem Cell Division through S-Adenosylmethionine in Drosophila Intestine. *Developmental Cell*, 44(6), 741–751.e3. https://doi.org/10.1016/j.devcel.2018.02.017 (obata2018nutritionalcontrolof pages 4-5, obata2018nutritionalcontrolof pages 5-6, obata2018nutritionalcontrolof pages 1-3, obata2018nutritionalcontrolof pages 6-7, obata2018nutritionalcontrolof pages 3-3, obata2018nutritionalcontrolof pages 7-8)

6. Zhao et al. (September 6, 2024). Loss of Diphthamide Increases DNA Replication Stress in Mammalian Cells by Modulating the Translation of RRM1. *ACS Central Science*, 10(10), 1835–1847. https://doi.org/10.1021/acscentsci.4c00967 (zhao2024lossofdiphthamide pages 1-2, zhao2024lossofdiphthamide pages 2-4)

7. Tsuda-Sakurai et al. (January 2020). Diphthamide modification of eEF2 is required for gut tumor-like hyperplasia induced by oncogenic Ras. *Genes to Cells*, 25(2), 76–85. https://doi.org/10.1111/gtc.12742 (tsuda‐sakurai2020diphthamidemodificationof pages 1-5)

8. Dong et al. (August 2019). The asymmetric function of Dph1–Dph2 heterodimer in diphthamide biosynthesis. *JBIC Journal of Biological Inorganic Chemistry*, 24(6), 777–782. https://doi.org/10.1007/s00775-019-01702-0 (dong2019theasymmetricfunction pages 1-2)

9. Lin et al. (January 2016). Functional Studies Of Three Genes Involved In Diphthamide Biosynthesis. *Text* (Cornell). https://doi.org/10.7298/x4qj7f8x (lin2016functionalstudiesof pages 43-48)

10. Shin et al. (May 2023). eEF2 diphthamide modification restrains spurious frameshifting to maintain translational fidelity. *Nucleic Acids Research*, 51(13), 6899–6913. https://doi.org/10.1093/nar/gkad461 (shin2023eef2diphthamidemodification pages 13-13, shin2023eef2diphthamidemodification pages 1-1, shin2023eef2diphthamidemodification pages 1-2)

11. Ütkür et al. (November 16, 2023). DPH1 Gene Mutations Identify a Candidate SAM Pocket in Radical Enzyme Dph1•Dph2 for Diphthamide Synthesis on EF2. *Biomolecules*, 13(11), 1655. https://doi.org/10.3390/biom13111655 (utkur2023dph1genemutations pages 4-6, utkur2023dph1genemutations pages 1-2)

12. Ütkür et al. (September 2023). DPH1 and DPH2 variants that confer susceptibility to diphthamide deficiency syndrome in human cells and yeast models. *Disease Models & Mechanisms*, 16(9), dmm050207. https://doi.org/10.1242/dmm.050207 (utkur2023dph1anddph2 pages 1-2)

13. Su et al. (November 2013). The biosynthesis and biological function of diphthamide. *Critical Reviews in Biochemistry and Molecular Biology*, 48(6), 515–521. https://doi.org/10.3109/10409238.2013.831023 (su2013thebiosynthesisand pages 3-4)

14. Zhang (2021). INVESTIGATION OF UNIQUE POST TRANSLATIONAL MODIFICATIONS ON ELONGATION FACTORS. *Text* (Cornell). https://doi.org/10.7298/t2e8-kc49 (yugang2021investigationofunique pages 17-22)

---

**Report Date:** December 2024  
**Report Prepared by:** Literature AI (PaperQA agentic RAG system)

References

1. (cina2019forwardgeneticscreen pages 37-44): Davide P. Cinà, Troy Ketela, Kevin R. Brown, Megha Chandrashekhar, Patricia Mero, Chengjin Li, Tuncer Onay, Yulong Fu, Zhe Han, Moin Saleem, Jason Moffat, and Susan E. Quaggin. Forward genetic screen in human podocytes identifies diphthamide biosynthesis genes as regulators of adhesion. American Journal of Physiology-Renal Physiology, 317:F1593-F1604, Dec 2019. URL: https://doi.org/10.1152/ajprenal.00195.2019, doi:10.1152/ajprenal.00195.2019. This article has 10 citations and is from a peer-reviewed journal.

2. (utkur2024functionalintegrityof pages 2-4): Koray Ütkür, Klaus Mayer, Shihui Liu, Ulrich Brinkmann, and Raffael Schaffrath. Functional integrity of radical sam enzyme dph1•dph2 requires non-canonical cofactor motifs with tandem cysteines. Biomolecules, Apr 2024. URL: https://doi.org/10.3390/biom14040470, doi:10.3390/biom14040470. This article has 2 citations.

3. (dong2014dph3isan pages 1-2): Min Dong, Xiaoyang Su, Boris Dzikovski, Emily E. Dando, Xuling Zhu, Jintang Du, Jack H. Freed, and Hening Lin. Dph3 is an electron donor for dph1-dph2 in the first step of eukaryotic diphthamide biosynthesis. Journal of the American Chemical Society, 136:1754-1757, Jan 2014. URL: https://doi.org/10.1021/ja4118957, doi:10.1021/ja4118957. This article has 87 citations and is from a highest quality peer-reviewed journal.

4. (shin2023eef2diphthamidemodification pages 1-2): Byung-Sik Shin, Ivaylo P Ivanov, Joo-Ran Kim, Chune Cao, Terri G Kinzy, and Thomas E Dever. Eef2 diphthamide modification restrains spurious frameshifting to maintain translational fidelity. Nucleic acids research, 51:6899-6913, May 2023. URL: https://doi.org/10.1093/nar/gkad461, doi:10.1093/nar/gkad461. This article has 23 citations and is from a highest quality peer-reviewed journal.

5. (zhao2024lossofdiphthamide pages 1-2): Jiaqi Zhao, Byunghyun Ahn, and Hening Lin. Loss of diphthamide increases dna replication stress in mammalian cells by modulating the translation of rrm1. ACS Central Science, 10:1835-1847, Sep 2024. URL: https://doi.org/10.1021/acscentsci.4c00967, doi:10.1021/acscentsci.4c00967. This article has 5 citations and is from a highest quality peer-reviewed journal.

6. (utkur2024functionalintegrityof pages 1-2): Koray Ütkür, Klaus Mayer, Shihui Liu, Ulrich Brinkmann, and Raffael Schaffrath. Functional integrity of radical sam enzyme dph1•dph2 requires non-canonical cofactor motifs with tandem cysteines. Biomolecules, Apr 2024. URL: https://doi.org/10.3390/biom14040470, doi:10.3390/biom14040470. This article has 2 citations.

7. (shin2023eef2diphthamidemodification pages 13-13): Byung-Sik Shin, Ivaylo P Ivanov, Joo-Ran Kim, Chune Cao, Terri G Kinzy, and Thomas E Dever. Eef2 diphthamide modification restrains spurious frameshifting to maintain translational fidelity. Nucleic acids research, 51:6899-6913, May 2023. URL: https://doi.org/10.1093/nar/gkad461, doi:10.1093/nar/gkad461. This article has 23 citations and is from a highest quality peer-reviewed journal.

8. (zhang2025diphthamideformationin pages 1-4): Hongliang Zhang, Nadežda Janina, Koray Ütkür, Thirishika Manivannan, Lei Zhang, Lizhen Wang, Christopher Grefen, Raffael Schaffrath, and Ute Krämer. Diphthamide formation in arabidopsis requires dph1-interacting dph2 for light and oxidative stress resistance. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2024.09.16.613322, doi:10.1101/2024.09.16.613322. This article has 2 citations.

9. (lin2016functionalstudiesof pages 43-48): Zhewang Lin. Functional studies of three genes involved in diphthamide biosynthesis. Text, Jan 2016. URL: https://doi.org/10.7298/x4qj7f8x, doi:10.7298/x4qj7f8x. This article has 0 citations and is from a peer-reviewed journal.

10. (obata2018nutritionalcontrolof pages 4-5): Fumiaki Obata, Kayoko Tsuda-Sakurai, Takahiro Yamazaki, Ryo Nishio, Kei Nishimura, Masaki Kimura, Masabumi Funakoshi, and Masayuki Miura. Nutritional control of stem cell division through s-adenosylmethionine in drosophila intestine. Developmental cell, 44 6:741-751.e3, Mar 2018. URL: https://doi.org/10.1016/j.devcel.2018.02.017, doi:10.1016/j.devcel.2018.02.017. This article has 102 citations and is from a highest quality peer-reviewed journal.

11. (tsuda‐sakurai2020diphthamidemodificationof pages 1-5): Kayoko Tsuda‐Sakurai, Masaki Kimura, and Masayuki Miura. Diphthamide modification of eef2 is required for gut tumor‐like hyperplasia induced by oncogenic ras. Genes to Cells, 25:76-85, Jan 2020. URL: https://doi.org/10.1111/gtc.12742, doi:10.1111/gtc.12742. This article has 11 citations and is from a peer-reviewed journal.

12. (dong2019theasymmetricfunction pages 1-2): Min Dong, Emily E. Dando, Ilana Kotliar, Xiaoyang Su, Boris Dzikovski, Jack H. Freed, and Hening Lin. The asymmetric function of dph1–dph2 heterodimer in diphthamide biosynthesis. JBIC Journal of Biological Inorganic Chemistry, 24:777-782, Aug 2019. URL: https://doi.org/10.1007/s00775-019-01702-0, doi:10.1007/s00775-019-01702-0. This article has 21 citations.

13. (su2013thebiosynthesisand pages 3-4): Xiaoyang Su, Zhewang Lin, and Hening Lin. The biosynthesis and biological function of diphthamide. Critical Reviews in Biochemistry and Molecular Biology, 48:515-521, Nov 2013. URL: https://doi.org/10.3109/10409238.2013.831023, doi:10.3109/10409238.2013.831023. This article has 95 citations and is from a peer-reviewed journal.

14. (yugang2021investigationofunique pages 17-22): Yugang Zhang. Investigation of unique post translational modifications on elongation factors. Text, 2021. URL: https://doi.org/10.7298/t2e8-kc49, doi:10.7298/t2e8-kc49. This article has 0 citations and is from a peer-reviewed journal.

15. (utkur2023dph1genemutations pages 4-6): Koray Ütkür, Sarina Schmidt, Klaus Mayer, Roland Klassen, Ulrich Brinkmann, and Raffael Schaffrath. Dph1 gene mutations identify a candidate sam pocket in radical enzyme dph1•dph2 for diphthamide synthesis on ef2. Biomolecules, 13:1655, Nov 2023. URL: https://doi.org/10.3390/biom13111655, doi:10.3390/biom13111655. This article has 5 citations.

16. (utkur2023dph1genemutations pages 1-2): Koray Ütkür, Sarina Schmidt, Klaus Mayer, Roland Klassen, Ulrich Brinkmann, and Raffael Schaffrath. Dph1 gene mutations identify a candidate sam pocket in radical enzyme dph1•dph2 for diphthamide synthesis on ef2. Biomolecules, 13:1655, Nov 2023. URL: https://doi.org/10.3390/biom13111655, doi:10.3390/biom13111655. This article has 5 citations.

17. (utkur2024functionalintegrityof pages 4-6): Koray Ütkür, Klaus Mayer, Shihui Liu, Ulrich Brinkmann, and Raffael Schaffrath. Functional integrity of radical sam enzyme dph1•dph2 requires non-canonical cofactor motifs with tandem cysteines. Biomolecules, Apr 2024. URL: https://doi.org/10.3390/biom14040470, doi:10.3390/biom14040470. This article has 2 citations.

18. (utkur2024functionalintegrityof pages 8-10): Koray Ütkür, Klaus Mayer, Shihui Liu, Ulrich Brinkmann, and Raffael Schaffrath. Functional integrity of radical sam enzyme dph1•dph2 requires non-canonical cofactor motifs with tandem cysteines. Biomolecules, Apr 2024. URL: https://doi.org/10.3390/biom14040470, doi:10.3390/biom14040470. This article has 2 citations.

19. (shin2023eef2diphthamidemodification pages 1-1): Byung-Sik Shin, Ivaylo P Ivanov, Joo-Ran Kim, Chune Cao, Terri G Kinzy, and Thomas E Dever. Eef2 diphthamide modification restrains spurious frameshifting to maintain translational fidelity. Nucleic acids research, 51:6899-6913, May 2023. URL: https://doi.org/10.1093/nar/gkad461, doi:10.1093/nar/gkad461. This article has 23 citations and is from a highest quality peer-reviewed journal.

20. (zhao2024lossofdiphthamide pages 2-4): Jiaqi Zhao, Byunghyun Ahn, and Hening Lin. Loss of diphthamide increases dna replication stress in mammalian cells by modulating the translation of rrm1. ACS Central Science, 10:1835-1847, Sep 2024. URL: https://doi.org/10.1021/acscentsci.4c00967, doi:10.1021/acscentsci.4c00967. This article has 5 citations and is from a highest quality peer-reviewed journal.

21. (zhang2025diphthamideformationin pages 52-56): Hongliang Zhang, Nadežda Janina, Koray Ütkür, Thirishika Manivannan, Lei Zhang, Lizhen Wang, Christopher Grefen, Raffael Schaffrath, and Ute Krämer. Diphthamide formation in arabidopsis requires dph1-interacting dph2 for light and oxidative stress resistance. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2024.09.16.613322, doi:10.1101/2024.09.16.613322. This article has 2 citations.

22. (obata2018nutritionalcontrolof pages 1-3): Fumiaki Obata, Kayoko Tsuda-Sakurai, Takahiro Yamazaki, Ryo Nishio, Kei Nishimura, Masaki Kimura, Masabumi Funakoshi, and Masayuki Miura. Nutritional control of stem cell division through s-adenosylmethionine in drosophila intestine. Developmental cell, 44 6:741-751.e3, Mar 2018. URL: https://doi.org/10.1016/j.devcel.2018.02.017, doi:10.1016/j.devcel.2018.02.017. This article has 102 citations and is from a highest quality peer-reviewed journal.

23. (obata2018nutritionalcontrolof pages 5-6): Fumiaki Obata, Kayoko Tsuda-Sakurai, Takahiro Yamazaki, Ryo Nishio, Kei Nishimura, Masaki Kimura, Masabumi Funakoshi, and Masayuki Miura. Nutritional control of stem cell division through s-adenosylmethionine in drosophila intestine. Developmental cell, 44 6:741-751.e3, Mar 2018. URL: https://doi.org/10.1016/j.devcel.2018.02.017, doi:10.1016/j.devcel.2018.02.017. This article has 102 citations and is from a highest quality peer-reviewed journal.

24. (obata2018nutritionalcontrolof pages 3-3): Fumiaki Obata, Kayoko Tsuda-Sakurai, Takahiro Yamazaki, Ryo Nishio, Kei Nishimura, Masaki Kimura, Masabumi Funakoshi, and Masayuki Miura. Nutritional control of stem cell division through s-adenosylmethionine in drosophila intestine. Developmental cell, 44 6:741-751.e3, Mar 2018. URL: https://doi.org/10.1016/j.devcel.2018.02.017, doi:10.1016/j.devcel.2018.02.017. This article has 102 citations and is from a highest quality peer-reviewed journal.

25. (obata2018nutritionalcontrolof pages 6-7): Fumiaki Obata, Kayoko Tsuda-Sakurai, Takahiro Yamazaki, Ryo Nishio, Kei Nishimura, Masaki Kimura, Masabumi Funakoshi, and Masayuki Miura. Nutritional control of stem cell division through s-adenosylmethionine in drosophila intestine. Developmental cell, 44 6:741-751.e3, Mar 2018. URL: https://doi.org/10.1016/j.devcel.2018.02.017, doi:10.1016/j.devcel.2018.02.017. This article has 102 citations and is from a highest quality peer-reviewed journal.

26. (obata2018nutritionalcontrolof pages 7-8): Fumiaki Obata, Kayoko Tsuda-Sakurai, Takahiro Yamazaki, Ryo Nishio, Kei Nishimura, Masaki Kimura, Masabumi Funakoshi, and Masayuki Miura. Nutritional control of stem cell division through s-adenosylmethionine in drosophila intestine. Developmental cell, 44 6:741-751.e3, Mar 2018. URL: https://doi.org/10.1016/j.devcel.2018.02.017, doi:10.1016/j.devcel.2018.02.017. This article has 102 citations and is from a highest quality peer-reviewed journal.

27. (utkur2023dph1anddph2 pages 1-2): Koray Ütkür, Klaus Mayer, Maliha Khan, Thirishika Manivannan, Raffael Schaffrath, and Ulrich Brinkmann. Dph1 and dph2 variants that confer susceptibility to diphthamide deficiency syndrome in human cells and yeast models. Disease Models & Mechanisms, Sep 2023. URL: https://doi.org/10.1242/dmm.050207, doi:10.1242/dmm.050207. This article has 10 citations and is from a domain leading peer-reviewed journal.

28. (zhang2025diphthamideformationin pages 66-69): Hongliang Zhang, Nadežda Janina, Koray Ütkür, Thirishika Manivannan, Lei Zhang, Lizhen Wang, Christopher Grefen, Raffael Schaffrath, and Ute Krämer. Diphthamide formation in arabidopsis requires dph1-interacting dph2 for light and oxidative stress resistance. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2024.09.16.613322, doi:10.1101/2024.09.16.613322. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](Dph1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. zhao2024lossofdiphthamide pages 1-2
2. lin2016functionalstudiesof pages 43-48
3. utkur2024functionalintegrityof pages 2-4
4. cina2019forwardgeneticscreen pages 37-44
5. utkur2024functionalintegrityof pages 1-2
6. utkur2024functionalintegrityof pages 8-10
7. zhao2024lossofdiphthamide pages 2-4
8. zhang2025diphthamideformationin pages 1-4
9. obata2018nutritionalcontrolof pages 3-3
10. obata2018nutritionalcontrolof pages 4-5
11. obata2018nutritionalcontrolof pages 5-6
12. zhang2025diphthamideformationin pages 66-69
13. obata2018nutritionalcontrolof pages 6-7
14. dong2019theasymmetricfunction pages 1-2
15. su2013thebiosynthesisand pages 3-4
16. yugang2021investigationofunique pages 17-22
17. utkur2024functionalintegrityof pages 4-6
18. zhang2025diphthamideformationin pages 52-56
19. obata2018nutritionalcontrolof pages 1-3
20. obata2018nutritionalcontrolof pages 7-8
21. 4Fe-4S
22. doi:10.1152/ajprenal.00195.2019
23. doi:10.3390/biom14040470
24. doi:10.1021/ja4118957
25. doi:10.1007/s00775-019-01702-0
26. doi:10.1021/acscentsci.4c00967
27. doi:10.3390/biom13111655
28. doi:10.1101/2024.09.16.613322
29. doi:10.1016/j.devcel.2018.02.017
30. doi:10.1111/gtc.12742
31. doi:10.1093/nar/gkad461
32. https://doi.org/10.3390/biom14040470
33. https://doi.org/10.3390/biom13111655
34. https://doi.org/10.1093/nar/gkad461
35. https://doi.org/10.1021/acscentsci.4c00967
36. https://doi.org/10.1101/2024.09.16.613322
37. https://doi.org/10.1016/j.devcel.2018.02.017
38. https://doi.org/10.1152/ajprenal.00195.2019
39. https://doi.org/10.1111/gtc.12742
40. https://doi.org/10.1021/ja4118957
41. https://doi.org/10.1007/s00775-019-01702-0
42. https://doi.org/10.7298/x4qj7f8x
43. https://doi.org/10.1242/dmm.050207
44. https://doi.org/10.3109/10409238.2013.831023
45. https://doi.org/10.7298/t2e8-kc49
46. https://doi.org/10.1152/ajprenal.00195.2019,
47. https://doi.org/10.3390/biom14040470,
48. https://doi.org/10.1021/ja4118957,
49. https://doi.org/10.1093/nar/gkad461,
50. https://doi.org/10.1021/acscentsci.4c00967,
51. https://doi.org/10.1101/2024.09.16.613322,
52. https://doi.org/10.7298/x4qj7f8x,
53. https://doi.org/10.1016/j.devcel.2018.02.017,
54. https://doi.org/10.1111/gtc.12742,
55. https://doi.org/10.1007/s00775-019-01702-0,
56. https://doi.org/10.3109/10409238.2013.831023,
57. https://doi.org/10.7298/t2e8-kc49,
58. https://doi.org/10.3390/biom13111655,
59. https://doi.org/10.1242/dmm.050207,