# Falcon Research Report: AimP (BPPHT)

Generated using FutureHouse Falcon API

---

Question: You are a molecular biologist and gene annotation expert conducting comprehensive research to support GO annotation curation.

Provide detailed, well-cited information focusing on:
1. Gene function and molecular mechanisms
2. Cellular localization and subcellular components
3. Biological processes involvement
4. Disease associations and phenotypes
5. Protein domains and structural features
6. Expression patterns and regulation
7. Evolutionary conservation
8. Key experimental evidence and literature

Format as a comprehensive research report with citations suitable for Gene Ontology annotation curation.

Research the Bacillus phage phi3T gene AimP.

=== UNIPROT METADATA ===
UniProt ID: P0DOE2
Entry Name: AIMP_BPPHT
Gene Name: aimP
Protein Name: Protein AimP
Organism: Bacillus phage phi3T (Bacteriophage phi-3T)
NCBI Taxonomy ID: 10736
Function: [Arbitrium peptide]: Peptide which is released by the infected host bacteria and acts as a communication agent that affects the latency versus replication (lysogeny-lysis) decision for any new infecting virus from the same specie. High concentration of arbitrium peptide results in increased lysogeny in the upcoming viruses. The arbitrium peptide is secreted by infected bacteria and, after several cycles of infection, accumulates in the extracellular medium. When a virus from the same specie subsequently infects an uninfected bacterium which has internalized the peptide via its OPP transporter, the peptide will binds to the viral AimR transcriptional regulator and prevents AimR transcriptional activation of the aimX locus. Inhibition of aimX transcription promotes lysogeny.
Subcellular Location: [Arbitrium peptide]: Secreted
Subunit: [Arbitrium peptide]: Interacts with the viral AimR transcriptional regulator; this interaction changes the oligomeric state of AimR from an active dimer to an inactive monomer leading to lysogeny.
======================

Provide a comprehensive report covering function, localization, processes, domains, disease associations, expression, conservation, and relevant GO terms.

IMPORTANT: Focus specifically on the gene identified by the metadata above, particularly the UniProt ID, locus tag, and protein description if provided.

Sometimes different genes in the same organism have the same name. In this case, the gene being reviewed is the one identified by the metadata above.


# Comprehensive Research Report: The aimP Gene (UniProt: P0DOE2) of Bacillus phage phi3T

## 1. Gene Function and Molecular Mechanisms

**Function in Arbitrium System:**  
AimP encodes the arbitrium peptide—the founding component of a phage-encoded small peptide communication system that modulates the lysis-lysogeny decision in Bacillus phage phi3T and related SPβ-like phages (also called arbitrium systems) (erez2017communicationbetweenviruses pages 1-3, erez2017communicationbetweenviruses pages 4-6, erez2017communicationbetweenviruses pages 28-32, erez2017communicationbetweenviruses pages 8-14, brady2021molecularbasisof pages 14-17, leonfelix2021theimpactof pages 7-9, shang2025theroleof pages 9-11, sol2019decipheringthemolecular pages 1-3). The gene is part of a conserved locus with two other key components: aimR, encoding the transcriptional regulator/receptor, and aimX, encoding a regulatory RNA that acts as a negative regulator of lysogeny (brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 1-3, erez2017communicationbetweenviruses pages 8-14, stokaravihail2019widespreadutilizationof pages 1-3).

**Peptide Maturation and Secretion:**  
AimP is transcribed early upon infection as a 43-amino acid precursor (pro-peptide) with a predicted N-terminal signal peptide for secretion via the Sec pathway. Following secretion into the extracellular medium, the pro-peptide is processed by host (Bacillus) proteases to generate the mature, active 6-amino acid arbitrium peptide. In phi3T, the mature peptide sequence is **SAIRGA** (Ser-Ala-Ile-Arg-Gly-Ala), though the mature sequence is highly variable across phage families and forms the basis of high specificity in function (erez2017communicationbetweenviruses pages 4-6, erez2017communicationbetweenviruses pages 28-32, stokaravihail2019widespreadutilizationof pages 21-26, brady2021molecularbasisof pages 14-17, stokaravihail2019widespreadutilizationof pages 4-6, stokaravihail2019widespreadutilizationof pages 1-3, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 9-11).

**Signal Transduction Mechanism:**  
The mature AimP peptide accumulates in the environment during lytic replication. When its concentration surpasses a certain threshold—indicative of previous or ongoing phage infections—it is imported back into Bacillus cells by the OPP (oligopeptide permease) transporter system (brady2021molecularbasisof pages 14-17, leonfelix2021theimpactof pages 7-9, erez2017communicationbetweenviruses pages 6-8, stokaravihail2019widespreadutilizationof pages 6-7). Intracellular AimP binds to its cognate receptor AimR with high specificity and affinity (phi3T: EC50 ~138 nM) (erez2017communicationbetweenviruses pages 4-6, brady2021thearbitriumsystem pages 1-3, sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 11-13). This binding event triggers a conformational change in AimR that prevents its binding to the operator sequence upstream of aimX (erez2017communicationbetweenviruses pages 4-6, sol2019decipheringthemolecular pages 3-4, erez2017communicationbetweenviruses pages 8-14, sol2019decipheringthemolecular pages 11-13, brady2021molecularbasisof pages 14-17, sol2019decipheringthemolecular pages 10-11). The precise molecular mechanism is phage-specific: in phi3T, peptide binding to AimR causes dimer dissociation into inactive monomers, whereas in SPβ, AimR remains dimeric but is locked in a closed, DNA-incompetent conformation (sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 7-8, brady2021molecularbasisof pages 14-17, sol2022insightsintothe pages 1-2, guan2019structuralinsightsinto pages 5-7, zhen2019structuralbasisof pages 3-5, sol2019decipheringthemolecular pages 10-11, guan2019structuralinsightsinto pages 7-8). This inhibition prevents activation of aimX transcription, promoting lysogeny; in the absence of peptide, aimX is expressed, which represses the cI repressor gene (indirectly via a cis-antisense mechanism) and thus drives the phage toward the lytic pathway (stokaravihail2019widespreadutilizationof pages 21-26, rajaure2019molecularbasisof pages 1-2, brady2021molecularbasisof pages 14-17, stokaravihail2019widespreadutilizationof pages 7-9, stokaravihail2019widespreadutilizationof pages 1-3).

**Functional Specificity:**  
AimP peptides confer strict species-specific signaling: different Bacillus phages encode distinct arbitrium peptides that exhibit high specificity due to sequence differences, especially in the N-terminal three residues, while the C-terminal RGA is typically conserved (brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 4-6, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 1-3, stokaravihail2019widespreadutilizationof pages 4-6, stokaravihail2019widespreadutilizationof pages 21-26). The specificity is encoded both at the AimP peptide and AimR receptor binding interface (sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 7-8, sol2022insightsintothe pages 11-12, brady2021molecularbasisof pages 14-17).

**Integration with Host Systems:**  
Recent work has demonstrated that arbitrium signaling via AimP can cross-regulate the bacterial MazEF toxin-antitoxin system, further embedding the lysis-lysogeny decision within the broader host defense regulatory network (loyo2025conflictbetweenbacteriophagesa pages 29-33, guler2024arbitriumcommunicationcontrols pages 1-2, guler2023arbitriumcommunicationcontrols pages 13-15). This multi-tier integration allows the phage to sense both phage population density and host physiological state.

## 2. Cellular Localization and Subcellular Components

**Precursor Localization and Secretion:**  
The AimP precursor is synthesized in the cytoplasm and directed for secretion via a canonical N-terminal signal peptide (Sec pathway targeting) (erez2017communicationbetweenviruses pages 4-6, erez2017communicationbetweenviruses pages 3-4, stokaravihail2019widespreadutilizationof pages 6-7, rajaure2019molecularbasisof pages 1-2, stokaravihail2019widespreadutilizationof pages 7-9, brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 1-3). Bioinformatic analysis and experimental cleavage mapping support extracellular secretion and subsequent proteolytic maturation (brady2021molecularbasisof pages 14-17, stokaravihail2019widespreadutilizationof pages 4-6, stokaravihail2019widespreadutilizationof pages 21-26, stokaravihail2019widespreadutilizationof pages 9-11).

**Mature Peptide Distribution:**  
The mature 6-mer peptide accumulates in the extracellular environment and is re-imported into cells via the OPP transporter, a system ubiquitous in Bacillales for importing exogenous oligopeptides (brady2021molecularbasisof pages 14-17, leonfelix2021theimpactof pages 7-9, erez2017communicationbetweenviruses pages 6-8, stokaravihail2019widespreadutilizationof pages 7-9, stokaravihail2019widespreadutilizationof pages 6-7, erez2017communicationbetweenviruses pages 3-4). Upon re-entry, AimP exerts its function in the bacterial cytoplasm by physically binding to the AimR protein, which is also localized in the cytoplasm (brady2021molecularbasisof pages 14-17, sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 11-13). Thus, AimP is localized briefly in the cytoplasm, secreted to the extracellular milieu, and then re-imported to act intracellularly.

## 3. Biological Processes Involvement

**Lysis-Lysogeny Decision Control:**  
AimP is essential for the phage's decision between lytic replication (host cell destruction and virion release) and lysogeny (integration as a prophage and dormant state) (erez2017communicationbetweenviruses pages 3-4, erez2017communicationbetweenviruses pages 4-6, erez2017communicationbetweenviruses pages 6-8, erez2017communicationbetweenviruses pages 1-3, erez2017communicationbetweenviruses pages 8-14, brady2021thearbitriumsystem pages 3-4, zamoracaballero2024antagonisticinteractionsbetween pages 1-2, rajaure2019molecularbasisof pages 1-2, brady2021thearbitriumsystem pages 7-8, zamoracaballero2024antagonisticinteractionsbetween pages 2-3). When AimP is absent or at low concentration (early stage, few phages), lysis is favored; when present at high extracellular levels after multiple infection cycles, lysogeny is promoted (erez2017communicationbetweenviruses pages 1-3, brady2021molecularbasisof pages 14-17, stokaravihail2019widespreadutilizationof pages 21-26, erez2017communicationbetweenviruses pages 3-4, erez2017communicationbetweenviruses pages 28-32, leonfelix2021theimpactof pages 7-9).

**Population Sensing/Phage Communication:**  
AimP constitutes a bona fide quorum sensing system in bacteriophages and is the founding member of viral communication peptides that regulate collective behavioral strategies at the population level (brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 1-3, erez2017communicationbetweenviruses pages 8-14, stokaravihail2019widespreadutilizationof pages 16-21, stokaravihail2019widespreadutilizationof pages 3-4).

**Regulation of Prophage Induction and Persistence:**  
AimP-mediated signaling in established lysogens modulates prophage induction, acting as a 'bet-hedging' mechanism to balance the production of new phage particles against host cell viability under stress or exposure to inducers like mitomycin C. AimP suppresses excessive prophage induction, protecting host populations and ensuring long-term prophage maintenance (brady2021thearbitriumsystem pages 3-4, brady2021thearbitriumsystem pages 7-8, brady2021thearbitriumsystem pages 6-7, brady2021thearbitriumsystem pages 1-3).

**Interaction with Host Defense Elements:**  
AimP integrates with Bacillus toxin-antitoxin operons (notably, the MazEF system) via the regulatory circuit involving aimX, linking phage population sensing to cellular stress response and abortive infection resistance mechanisms (loyo2025conflictbetweenbacteriophagesa pages 29-33, loyo2025conflictbetweenbacteriophages pages 29-33, loyo2025conflictbetweenbacteriophagesb pages 29-33, guler2024arbitriumcommunicationcontrols pages 1-2, guler2023arbitriumcommunicationcontrols pages 13-15, zamoracaballero2024antagonisticinteractionsbetween pages 7-8).

**Horizontal Gene Transfer Regulation:**  
AimP (and associated arbitrium elements) are present on conjugative plasmids as well as temperate phages, suggesting a broader role in regulating transfer and maintenance of mobile genetic elements (stokaravihail2019widespreadutilizationof pages 6-7, stokaravihail2019widespreadutilizationof pages 16-21, stokaravihail2019widespreadutilizationof pages 3-4).

## 4. Disease Associations and Phenotypes

**Pathogen Association:**  
AimP systems are encoded not only by environmental Bacillus phages but also by phages/prophages and conjugative elements found in bacterial pathogens such as *Bacillus anthracis* and *Bacillus thuringiensis*, including virulence and insecticidal plasmids (stokaravihail2019widespreadutilizationof pages 6-7, stokaravihail2019widespreadutilizationof pages 16-21, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 4-6). This underpins potential roles in modulating emergence, virulence, or maintenance of pathogenic *Bacillus* strains via phage-induced genetic changes and mobile element transfer (stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 4-6).

**Phenotypic Evidence from Mutants:**  
ΔaimP (aimP deletion) mutant phages display aberrant infection phenotypes: increased lytic activity, higher phage titers, sharper plaques, and decreased ability to promote lysogeny after induction with DNA damaging agents (e.g., mitomycin C), confirming that AimP normally restricts lytic development and promotes lysogenization (brady2021thearbitriumsystem pages 3-4, brady2021thearbitriumsystem pages 6-7, brady2021thearbitriumsystem pages 7-8, erez2017communicationbetweenviruses pages 8-14). The absence of AimP peptide in the environment leads to lytic dominance and partial collapse of host populations (erez2017communicationbetweenviruses pages 1-3, erez2017communicationbetweenviruses pages 8-14).

## 5. Protein Domains and Structural Features

**Domain Organization:**  
- **Precursor:** The full-length AimP is a 43–44 amino acid protein composed of:
  - An **N-terminal Sec-dependent signal peptide** (by SignalP and TMHMM, facilitating export/secretion) (erez2017communicationbetweenviruses pages 4-6, erez2017communicationbetweenviruses pages 3-4, stokaravihail2019widespreadutilizationof pages 21-26, stokaravihail2019widespreadutilizationof pages 9-11, stokaravihail2019widespreadutilizationof pages 4-6).
  - A **pro-peptide domain** that enables proteolytic processing, similar to canonical Bacillus quorum sensing peptides of the Phr family (brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 4-6, stokaravihail2019widespreadutilizationof pages 3-4).
  - A **mature C-terminal hexapeptide**, the active communication signal, typically with sequence “SAIRGA” in phi3T (erez2017communicationbetweenviruses pages 4-6, brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 8-14, stokaravihail2019widespreadutilizationof pages 4-6).

- **Mature Peptide:** Sequence signatures are highly variable at the N-terminus and conserved at the C-terminus (RGA motif) across SPβ-like phages. Key residues underpin binding specificity and activity (brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 4-6, sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 7-8, sol2022insightsintothe pages 11-12).

**Receptor (AimR) Binding Interface:**  
High-resolution crystal structures reveal that AimP binds within a peptide binding groove in AimR’s tetratricopeptide repeat (TPR) domain, with N202, N239 and salt-bridges at the peptide N- and C-termini critical for recognition and specificity (sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 11-13, sol2019decipheringthemolecular pages 7-8). Conserved arginine in peptide position four is essential for anchoring the peptide and for the “locked” AimR conformation that blocks DNA binding (sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 11-13).

**Functional Parallels:**  
Although conceptually similar to the RRNPP family, structural, biochemical, and phylogenetic analyses indicate that AimP and the arbitrium system likely represent a distinct class of prokaryotic peptide-based signaling systems, with AimR showing similarities but belonging to a separate lineage (brady2021molecularbasisof pages 14-17, sol2019decipheringthemolecular pages 3-4, sol2019decipheringthemolecular pages 13-14).

## 6. Expression Patterns and Regulation

**Temporal Expression:**  
AimP (with aimR) is expressed immediately upon infection as part of the early gene program (erez2017communicationbetweenviruses pages 28-32, erez2017communicationbetweenviruses pages 6-8). RNA-seq reveals high expression in both initial lytic and established lysogenic states, consistent with a dual role in acute infection and prophage maintenance (erez2017communicationbetweenviruses pages 1-3, brady2021thearbitriumsystem pages 3-4, brady2021thearbitriumsystem pages 1-3, erez2017communicationbetweenviruses pages 21-23).

**Accumulation and Threshold Concentrations:**  
The peptide is not detectable during initial infection but accumulates with iterative infection cycles; effective concentrations (≥500 nM) are reached after 3–4 cycles, especially when phage:bacteria ratios approach 1:1 (erez2017communicationbetweenviruses pages 4-6, erez2017communicationbetweenviruses pages 3-4, erez2017communicationbetweenviruses pages 6-8, brady2021molecularbasisof pages 14-17). Lysogenization rate is highly sensitive to extracellular AimP levels, reaching ~48% with peptide vs ~18% without in experimental systems (erez2017communicationbetweenviruses pages 3-4).

**Regulatory Circuit:**  
AimP levels act as a critical input into a transcriptional switch:
- **Low extracellular AimP:** AimR is active, binds DNA, facilitates aimX transcription, blocking cI repressor and enforcing lysis.
- **High extracellular AimP:** AimR is inactivated by peptide binding, cannot activate aimX, cI repressor is expressed, and lysogeny occurs (erez2017communicationbetweenviruses pages 6-8, stokaravihail2019widespreadutilizationof pages 21-26, erez2017communicationbetweenviruses pages 1-3, stokaravihail2019widespreadutilizationof pages 1-3, stokaravihail2019widespreadutilizationof pages 6-7).

**Operon Organization:**  
The aimP gene is typically part of a conserved gene cluster organized as aimR-aimP-aimX, sometimes in a bicistronic operon with regulated antitermination by AimR (zamoracaballero2024antagonisticinteractionsbetween pages 2-3, erez2017communicationbetweenviruses pages 21-23, brady2021molecularbasisof pages 14-17).

## 7. Evolutionary Conservation

**Distribution Across Phages and Mobile Elements:**  
- **Phage Conservation:** Homology searches have identified at least 112 functional AimP/AimR systems in Bacillus phages/prophages and over 1,000 related systems in bacterial, archaeal, and conjugative element genomes (brady2021molecularbasisof pages 14-17, stokaravihail2019widespreadutilizationof pages 16-21, stokaravihail2019widespreadutilizationof pages 1-3, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 4-6, brady2021molecularbasisof pages 17-20).
- **Diversification:** AimP undergoes strong diversifying selection at the N-terminal three residues, generating a diverse code of peptide variants, while the C-terminal RGA motif is highly conserved in SPβ-related systems (brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 4-6, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 1-3).
- **Peptide Code Clades:** Phylogenetic analysis defines up to 10 major clades with distinct AimP and AimR combinations, indicating a large spectrum of communication codes across the Firmicutes and associated mobile elements (brady2021molecularbasisof pages 14-17, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 9-11).
- **Horizontal Transfer:** The organization near prophage integrase and cI repressor genes and identification on conjugative plasmids suggest horizontal gene transfer and adaptation to various mobile DNA backgrounds (stokaravihail2019widespreadutilizationof pages 16-21, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 4-6, stokaravihail2019widespreadutilizationof pages 6-7).

**Molecular Evolution with Host:**  
AimP likely evolved through co-option of bacterial quorum sensing machinery, as its maturation and import depend on general host pathways—secretory (Sec), extracellular proteases, and OPP transporters. This inter-kingdom exchange points to frequent horizontal gene acquisition and adaptation (stokaravihail2019widespreadutilizationof pages 6-7, stokaravihail2019widespreadutilizationof pages 1-3, stokaravihail2019widespreadutilizationof pages 3-4, brady2021molecularbasisof pages 14-17).

## 8. Key Experimental Evidence and Literature

**Peptide Identification and Processing:**  
- Mature AimP peptide (SAIRGA) identified in conditioned medium from phi3T-infected Bacillus cultures by mass spectrometry, confirming in vivo processing and secretion (erez2017communicationbetweenviruses pages 8-14, stokaravihail2019widespreadutilizationof pages 21-26, erez2017communicationbetweenviruses pages 6-8).
- Pulse-chase and conditioned media experiments demonstrate activity is proteinaceous, abolished by protease treatment (erez2017communicationbetweenviruses pages 1-3, erez2017communicationbetweenviruses pages 8-14).

**Functional Specificity and Synthetic Peptide Activity:**  
- Synthetic SAIRGA addition to infections promotes lysogeny in phi3T but not in other phage systems, demonstrating high specificity (erez2017communicationbetweenviruses pages 4-6, erez2017communicationbetweenviruses pages 8-14, stokaravihail2019widespreadutilizationof pages 21-26).
- Truncated or mutated peptides (e.g., AIRGA, SAIRG) are non-functional, defining the minimal active sequence (erez2017communicationbetweenviruses pages 8-14).

**Mutant Phenotype Studies:**  
- ΔaimP phages lack the communication signal, resulting in increased lytic activity, altered lysogenization rates, and more severe host lysis upon induction (brady2021thearbitriumsystem pages 3-4, brady2021thearbitriumsystem pages 6-7, brady2021thearbitriumsystem pages 7-8, brady2021thearbitriumsystem pages 1-3, erez2017communicationbetweenviruses pages 8-14).
- Complementation of aimP deletion or addition of synthetic peptide restores normal phenotype (erez2017communicationbetweenviruses pages 8-14, brady2021thearbitriumsystem pages 3-4).

**Structural Biology:**  
- Crystal structures of AimR with and without AimP (PDB: 6HP3, 6HP5, 6HP7) define the peptide binding pocket, interactions with conserved receptor residues, and allosteric changes underpinning functional inactivation (sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 7-8, sol2019decipheringthemolecular pages 3-4, sol2019decipheringthemolecular pages 11-13, sol2019decipheringthemolecular pages 10-11, guan2019structuralinsightsinto pages 5-7, zhen2019structuralbasisof pages 3-5, sol2019decipheringthemolecular pages 17-18, guan2019structuralinsightsinto pages 7-8).
- Thermal shift, EMSA, ITC, and SEC-MALS biochemical data corroborate structural findings and allow calculation of receptor/peptide affinities, conformational changes, and oligomeric states (sol2019decipheringthemolecular pages 17-18, sol2022insightsintothe pages 11-12, sol2019decipheringthemolecular pages 7-8, sol2019decipheringthemolecular pages 13-14).

**Population and Evolutionary Surveys:**  
- Bioinformatic identification of >1,000 arbitrium-like systems, with variable peptide sequence clades and organization across phage, plasmid, and bacterial genomes (stokaravihail2019widespreadutilizationof pages 16-21, stokaravihail2019widespreadutilizationof pages 6-7, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 4-6, stokaravihail2019widespreadutilizationof pages 9-11).

**Integration with Host Defense:**  
- AimP-driven modulation of the MazEF toxin-antitoxin system shown by functional assays, providing the first mechanistic link between phage communication and host abortive infection defenses (loyo2025conflictbetweenbacteriophagesa pages 29-33, guler2023arbitriumcommunicationcontrols pages 13-15, guler2024arbitriumcommunicationcontrols pages 1-2, zamoracaballero2024antagonisticinteractionsbetween pages 7-8).

**Comprehensive Reviews:**  
- Reviews summarizing molecular mechanism, evolutionary conservation, and physiological impact (brady2021molecularbasisof pages 14-17, brady2021thearbitriumsystem pages 1-3, leonfelix2021theimpactof pages 7-9).

---

## GO Annotation Recommendations

**Molecular Function:**
- *peptide pheromone activity* (GO:0019236)
- *receptor binding* (GO:0005102) [receptor: AimR]

**Biological Process:**
- *regulation of viral lysogenic process* (GO:0045825)
- *regulation of viral lytic cycle* (GO:1903909)
- *quorum sensing* (GO:0009372) [viral/quasi-quorum]
- *viral population density sensing* (proposed term)
- *modulation of host toxin-antitoxin system* (GO:0140737, host integration)
- *horizontal gene transfer via conjugation* (possible, in context of conjugative elements)

**Cellular Component:**
- *extracellular region* (GO:0005576)
- *cytoplasm* (GO:0005737)
- *secreted* (GO:0005576, supported by UniProt metadata)

---

## Conclusion

AimP (UniProt: P0DOE2) from Bacillus phage phi3T is a small secreted signaling peptide that represents the paradigm of viral quorum sensing and communication. Functioning as the arbitrium peptide, it coordinates population-level decisions between lytic and lysogenic cycles in response to extracellular peptide concentration—an indirect proxy for population density of infecting phages. The molecular mechanism involves sophisticated processing, secretion, and reuptake of the mature peptide and high-specificity interaction with the AimR receptor to control downstream regulatory modules. AimP acts at the nexus of mobile genetic element regulation, intertwining phage communication, horizontal gene transfer, host stress responses, and survival strategies. Its evolutionary conservation and dynamic diversification underpin its broad importance in phage biology, bacterial pathogenesis, and inter-microbial regulatory networks. This gene and its system are supported by robust experimental and structural studies and merit focused attention for annotation of peptide-mediated signaling, viral communication, and lysogeny/lysis decision-making in microbial genomics (brady2021molecularbasisof pages 14-17, erez2017communicationbetweenviruses pages 8-14, erez2017communicationbetweenviruses pages 4-6, stokaravihail2019widespreadutilizationof pages 21-26, erez2017communicationbetweenviruses pages 1-3, erez2017communicationbetweenviruses pages 6-8, leonfelix2021theimpactof pages 7-9, stokaravihail2019widespreadutilizationof pages 16-21, stokaravihail2019widespreadutilizationof pages 3-4, stokaravihail2019widespreadutilizationof pages 4-6, stokaravihail2019widespreadutilizationof pages 6-7, rajaure2019molecularbasisof pages 1-2, guler2023arbitriumcommunicationcontrols pages 13-15, brady2021thearbitriumsystem pages 7-8, sol2019decipheringthemolecular pages 17-18, sol2019decipheringthemolecular pages 11-13, sol2019decipheringthemolecular pages 13-14, sol2019decipheringthemolecular pages 3-4, sol2019decipheringthemolecular pages 7-8, zhen2019structuralbasisof pages 3-5, erez2017communicationbetweenviruses pages 3-4, zamoracaballero2024antagonisticinteractionsbetween pages 2-3, zamoracaballero2024antagonisticinteractionsbetween pages 7-8, brady2021thearbitriumsystem pages 3-4, brady2021thearbitriumsystem pages 6-7, brady2021thearbitriumsystem pages 1-3, zamoracaballero2024antagonisticinteractionsbetween pages 1-2, zhen2019structuralbasisof pages 1-3, guan2019structuralinsightsinto pages 7-8, stokaravihail2019widespreadutilizationof pages 7-9, wang2018structuralbasisof pages 1-15, erez2017communicationbetweenviruses pages 21-23, stokaravihail2019widespreadutilizationof pages 1-3, stokaravihail2019widespreadutilizationof pages 9-11, guan2019structuralinsightsinto pages 1-2, loyo2025conflictbetweenbacteriophages pages 29-33, loyo2025conflictbetweenbacteriophagesa pages 29-33, loyo2025conflictbetweenbacteriophagesb pages 29-33, vela2023emerginginvestigatorseries pages 4-5, shang2025theroleof pages 9-11).

References

1. (erez2017communicationbetweenviruses pages 1-3): Zohar Erez, Ida Steinberger-Levy, Maya Shamir, Shany Doron, Avigail Stokar-Avihail, Yoav Peleg, Sarah Melamed, Azita Leavitt, Alon Savidor, Shira Albeck, Gil Amitai, and Rotem Sorek. Communication between viruses guides lysis–lysogeny decisions. Nature, 541:488-493, Jan 2017. URL: https://doi.org/10.1038/nature21049, doi:10.1038/nature21049. This article has 827 citations and is from a highest quality peer-reviewed journal.

2. (erez2017communicationbetweenviruses pages 4-6): Zohar Erez, Ida Steinberger-Levy, Maya Shamir, Shany Doron, Avigail Stokar-Avihail, Yoav Peleg, Sarah Melamed, Azita Leavitt, Alon Savidor, Shira Albeck, Gil Amitai, and Rotem Sorek. Communication between viruses guides lysis–lysogeny decisions. Nature, 541:488-493, Jan 2017. URL: https://doi.org/10.1038/nature21049, doi:10.1038/nature21049. This article has 827 citations and is from a highest quality peer-reviewed journal.

3. (erez2017communicationbetweenviruses pages 28-32): Zohar Erez, Ida Steinberger-Levy, Maya Shamir, Shany Doron, Avigail Stokar-Avihail, Yoav Peleg, Sarah Melamed, Azita Leavitt, Alon Savidor, Shira Albeck, Gil Amitai, and Rotem Sorek. Communication between viruses guides lysis–lysogeny decisions. Nature, 541:488-493, Jan 2017. URL: https://doi.org/10.1038/nature21049, doi:10.1038/nature21049. This article has 827 citations and is from a highest quality peer-reviewed journal.

4. (erez2017communicationbetweenviruses pages 8-14): Zohar Erez, Ida Steinberger-Levy, Maya Shamir, Shany Doron, Avigail Stokar-Avihail, Yoav Peleg, Sarah Melamed, Azita Leavitt, Alon Savidor, Shira Albeck, Gil Amitai, and Rotem Sorek. Communication between viruses guides lysis–lysogeny decisions. Nature, 541:488-493, Jan 2017. URL: https://doi.org/10.1038/nature21049, doi:10.1038/nature21049. This article has 827 citations and is from a highest quality peer-reviewed journal.

5. (brady2021molecularbasisof pages 14-17): Aisling Brady, Alonso Felipe-Ruiz, Francisca Gallego del Sol, Alberto Marina, Nuria Quiles-Puchalt, and José R. Penadés. Molecular basis of lysis–lysogeny decisions in gram-positive phages. Annual Review of Microbiology, 75:563-581, Oct 2021. URL: https://doi.org/10.1146/annurev-micro-033121-020757, doi:10.1146/annurev-micro-033121-020757. This article has 72 citations and is from a peer-reviewed journal.

6. (leonfelix2021theimpactof pages 7-9): Josefina León-Félix and Claudia Villicaña. The impact of quorum sensing on the modulation of phage-host interactions. Journal of Bacteriology, May 2021. URL: https://doi.org/10.1128/jb.00687-20, doi:10.1128/jb.00687-20. This article has 54 citations and is from a peer-reviewed journal.

7. (shang2025theroleof pages 9-11): Junjie Shang, Kehan Wang, Qian Zhou, and Yunlin Wei. The role of quorum sensing in phage lifecycle decision: a switch between lytic and lysogenic pathways. Viruses, 17:317, Feb 2025. URL: https://doi.org/10.3390/v17030317, doi:10.3390/v17030317. This article has 4 citations and is from a poor quality or predatory journal.

8. (sol2019decipheringthemolecular pages 1-3): Francisca Gallego del Sol, José R. Penadés, and Alberto Marina. Deciphering the molecular mechanism underpinning phage arbitrium communication systems. Molecular Cell, 74:59-72.e3, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.01.025, doi:10.1016/j.molcel.2019.01.025. This article has 60 citations and is from a highest quality peer-reviewed journal.

9. (stokaravihail2019widespreadutilizationof pages 1-3): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

10. (stokaravihail2019widespreadutilizationof pages 21-26): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

11. (stokaravihail2019widespreadutilizationof pages 4-6): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

12. (stokaravihail2019widespreadutilizationof pages 3-4): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

13. (stokaravihail2019widespreadutilizationof pages 9-11): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

14. (erez2017communicationbetweenviruses pages 6-8): Zohar Erez, Ida Steinberger-Levy, Maya Shamir, Shany Doron, Avigail Stokar-Avihail, Yoav Peleg, Sarah Melamed, Azita Leavitt, Alon Savidor, Shira Albeck, Gil Amitai, and Rotem Sorek. Communication between viruses guides lysis–lysogeny decisions. Nature, 541:488-493, Jan 2017. URL: https://doi.org/10.1038/nature21049, doi:10.1038/nature21049. This article has 827 citations and is from a highest quality peer-reviewed journal.

15. (stokaravihail2019widespreadutilizationof pages 6-7): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

16. (brady2021thearbitriumsystem pages 1-3): Aisling Brady, Nuria Quiles-Puchalt, Francisca Gallego del Sol, Sara Zamora-Caballero, Alonso Felipe-Ruíz, Jorge Val-Calvo, Wilfried J.J. Meijer, Alberto Marina, and José R. Penadés. The arbitrium system controls prophage induction. Current Biology, 31:5037-5045.e3, Nov 2021. URL: https://doi.org/10.1016/j.cub.2021.08.072, doi:10.1016/j.cub.2021.08.072. This article has 43 citations and is from a highest quality peer-reviewed journal.

17. (sol2019decipheringthemolecular pages 13-14): Francisca Gallego del Sol, José R. Penadés, and Alberto Marina. Deciphering the molecular mechanism underpinning phage arbitrium communication systems. Molecular Cell, 74:59-72.e3, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.01.025, doi:10.1016/j.molcel.2019.01.025. This article has 60 citations and is from a highest quality peer-reviewed journal.

18. (sol2019decipheringthemolecular pages 11-13): Francisca Gallego del Sol, José R. Penadés, and Alberto Marina. Deciphering the molecular mechanism underpinning phage arbitrium communication systems. Molecular Cell, 74:59-72.e3, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.01.025, doi:10.1016/j.molcel.2019.01.025. This article has 60 citations and is from a highest quality peer-reviewed journal.

19. (sol2019decipheringthemolecular pages 3-4): Francisca Gallego del Sol, José R. Penadés, and Alberto Marina. Deciphering the molecular mechanism underpinning phage arbitrium communication systems. Molecular Cell, 74:59-72.e3, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.01.025, doi:10.1016/j.molcel.2019.01.025. This article has 60 citations and is from a highest quality peer-reviewed journal.

20. (sol2019decipheringthemolecular pages 10-11): Francisca Gallego del Sol, José R. Penadés, and Alberto Marina. Deciphering the molecular mechanism underpinning phage arbitrium communication systems. Molecular Cell, 74:59-72.e3, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.01.025, doi:10.1016/j.molcel.2019.01.025. This article has 60 citations and is from a highest quality peer-reviewed journal.

21. (sol2019decipheringthemolecular pages 7-8): Francisca Gallego del Sol, José R. Penadés, and Alberto Marina. Deciphering the molecular mechanism underpinning phage arbitrium communication systems. Molecular Cell, 74:59-72.e3, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.01.025, doi:10.1016/j.molcel.2019.01.025. This article has 60 citations and is from a highest quality peer-reviewed journal.

22. (sol2022insightsintothe pages 1-2): Francisca Gallego del Sol, Nuria Quiles-Puchalt, Aisling Brady, José R. Penadés, and Alberto Marina. Insights into the mechanism of action of the arbitrium communication system in spbeta phages. Nature Communications, Jun 2022. URL: https://doi.org/10.1038/s41467-022-31144-3, doi:10.1038/s41467-022-31144-3. This article has 20 citations and is from a highest quality peer-reviewed journal.

23. (guan2019structuralinsightsinto pages 5-7): Zeyuan Guan, Kai Pei, Jing Wang, Yongqing Cui, Xiang Zhu, Xiang Su, Yuanbao Zhou, Delin Zhang, Chun Tang, Ping Yin, Zhu Liu, and Tingting Zou. Structural insights into dna recognition by aimr of the arbitrium communication system in the spbeta phage. Cell Discovery, May 2019. URL: https://doi.org/10.1038/s41421-019-0101-2, doi:10.1038/s41421-019-0101-2. This article has 23 citations and is from a peer-reviewed journal.

24. (zhen2019structuralbasisof pages 3-5): Xiangkai Zhen, Huan Zhou, Wei Ding, Biao Zhou, Xiaolong Xu, Vanja Perčulija, Chun-Jung Chen, Ming-Xian Chang, Muhammad Iqbal Choudhary, and Songying Ouyang. Structural basis of aimp signaling molecule recognition by aimr in spbeta group of bacteriophages. Protein & Cell, 10:131-136, Nov 2019. URL: https://doi.org/10.1007/s13238-018-0588-6, doi:10.1007/s13238-018-0588-6. This article has 22 citations and is from a peer-reviewed journal.

25. (guan2019structuralinsightsinto pages 7-8): Zeyuan Guan, Kai Pei, Jing Wang, Yongqing Cui, Xiang Zhu, Xiang Su, Yuanbao Zhou, Delin Zhang, Chun Tang, Ping Yin, Zhu Liu, and Tingting Zou. Structural insights into dna recognition by aimr of the arbitrium communication system in the spbeta phage. Cell Discovery, May 2019. URL: https://doi.org/10.1038/s41421-019-0101-2, doi:10.1038/s41421-019-0101-2. This article has 23 citations and is from a peer-reviewed journal.

26. (rajaure2019molecularbasisof pages 1-2): Manoj Rajaure and Sankar Adhya. Molecular basis of phage communication. Molecular cell, 74 1:1-2, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.03.015, doi:10.1016/j.molcel.2019.03.015. This article has 6 citations and is from a highest quality peer-reviewed journal.

27. (stokaravihail2019widespreadutilizationof pages 7-9): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

28. (sol2022insightsintothe pages 11-12): Francisca Gallego del Sol, Nuria Quiles-Puchalt, Aisling Brady, José R. Penadés, and Alberto Marina. Insights into the mechanism of action of the arbitrium communication system in spbeta phages. Nature Communications, Jun 2022. URL: https://doi.org/10.1038/s41467-022-31144-3, doi:10.1038/s41467-022-31144-3. This article has 20 citations and is from a highest quality peer-reviewed journal.

29. (loyo2025conflictbetweenbacteriophagesa pages 29-33): CL Loyo. Conflict between bacteriophages and a mobile genetic element in bacterial immunity. Unknown journal, 2025.

30. (guler2024arbitriumcommunicationcontrols pages 1-2): Polina Guler, Shira Omer Bendori, Tom Borenstein, Nitzan Aframian, Amit Kessel, and Avigdor Eldar. Arbitrium communication controls phage lysogeny through non-lethal modulation of a host toxin–antitoxin defence system. Nature Microbiology, 9:150-160, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01551-3, doi:10.1038/s41564-023-01551-3. This article has 17 citations and is from a highest quality peer-reviewed journal.

31. (guler2023arbitriumcommunicationcontrols pages 13-15): Polina Guler, Shira Omer Bendori, Nitzan Aframian, Amit Kessel, and Avigdor Eldar. Arbitrium communication controls phage life-cycle through modulation of a bacterial anti-phage defense system. bioRxiv, Apr 2023. URL: https://doi.org/10.1101/2023.04.27.537455, doi:10.1101/2023.04.27.537455. This article has 2 citations and is from a poor quality or predatory journal.

32. (erez2017communicationbetweenviruses pages 3-4): Zohar Erez, Ida Steinberger-Levy, Maya Shamir, Shany Doron, Avigail Stokar-Avihail, Yoav Peleg, Sarah Melamed, Azita Leavitt, Alon Savidor, Shira Albeck, Gil Amitai, and Rotem Sorek. Communication between viruses guides lysis–lysogeny decisions. Nature, 541:488-493, Jan 2017. URL: https://doi.org/10.1038/nature21049, doi:10.1038/nature21049. This article has 827 citations and is from a highest quality peer-reviewed journal.

33. (brady2021thearbitriumsystem pages 3-4): Aisling Brady, Nuria Quiles-Puchalt, Francisca Gallego del Sol, Sara Zamora-Caballero, Alonso Felipe-Ruíz, Jorge Val-Calvo, Wilfried J.J. Meijer, Alberto Marina, and José R. Penadés. The arbitrium system controls prophage induction. Current Biology, 31:5037-5045.e3, Nov 2021. URL: https://doi.org/10.1016/j.cub.2021.08.072, doi:10.1016/j.cub.2021.08.072. This article has 43 citations and is from a highest quality peer-reviewed journal.

34. (zamoracaballero2024antagonisticinteractionsbetween pages 1-2): Sara Zamora-Caballero, Cora Chmielowska, Nuria Quiles-Puchalt, Aisling Brady, Francisca Gallego del Sol, Javier Mancheño-Bonillo, Alonso Felipe-Ruíz, Wilfried J. J. Meijer, José R. Penadés, and Alberto Marina. Antagonistic interactions between phage and host factors control arbitrium lysis–lysogeny decision. Nature Microbiology, 9:161-172, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01550-4, doi:10.1038/s41564-023-01550-4. This article has 13 citations and is from a highest quality peer-reviewed journal.

35. (brady2021thearbitriumsystem pages 7-8): Aisling Brady, Nuria Quiles-Puchalt, Francisca Gallego del Sol, Sara Zamora-Caballero, Alonso Felipe-Ruíz, Jorge Val-Calvo, Wilfried J.J. Meijer, Alberto Marina, and José R. Penadés. The arbitrium system controls prophage induction. Current Biology, 31:5037-5045.e3, Nov 2021. URL: https://doi.org/10.1016/j.cub.2021.08.072, doi:10.1016/j.cub.2021.08.072. This article has 43 citations and is from a highest quality peer-reviewed journal.

36. (zamoracaballero2024antagonisticinteractionsbetween pages 2-3): Sara Zamora-Caballero, Cora Chmielowska, Nuria Quiles-Puchalt, Aisling Brady, Francisca Gallego del Sol, Javier Mancheño-Bonillo, Alonso Felipe-Ruíz, Wilfried J. J. Meijer, José R. Penadés, and Alberto Marina. Antagonistic interactions between phage and host factors control arbitrium lysis–lysogeny decision. Nature Microbiology, 9:161-172, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01550-4, doi:10.1038/s41564-023-01550-4. This article has 13 citations and is from a highest quality peer-reviewed journal.

37. (stokaravihail2019widespreadutilizationof pages 16-21): Avigail Stokar-Avihail, Nitzan Tal, Zohar Erez, Anna Lopatina, and Rotem Sorek. Widespread utilization of peptide communication in phages infecting soil and pathogenic bacteria. Cell Host &amp; Microbe, 25:746-755.e5, May 2019. URL: https://doi.org/10.1016/j.chom.2019.03.017, doi:10.1016/j.chom.2019.03.017. This article has 112 citations and is from a highest quality peer-reviewed journal.

38. (brady2021thearbitriumsystem pages 6-7): Aisling Brady, Nuria Quiles-Puchalt, Francisca Gallego del Sol, Sara Zamora-Caballero, Alonso Felipe-Ruíz, Jorge Val-Calvo, Wilfried J.J. Meijer, Alberto Marina, and José R. Penadés. The arbitrium system controls prophage induction. Current Biology, 31:5037-5045.e3, Nov 2021. URL: https://doi.org/10.1016/j.cub.2021.08.072, doi:10.1016/j.cub.2021.08.072. This article has 43 citations and is from a highest quality peer-reviewed journal.

39. (loyo2025conflictbetweenbacteriophages pages 29-33): CL Loyo. Conflict between bacteriophages and a mobile genetic element in bacterial immunity. Unknown journal, 2025.

40. (loyo2025conflictbetweenbacteriophagesb pages 29-33): CL Loyo. Conflict between bacteriophages and a mobile genetic element in bacterial immunity. Unknown journal, 2025.

41. (zamoracaballero2024antagonisticinteractionsbetween pages 7-8): Sara Zamora-Caballero, Cora Chmielowska, Nuria Quiles-Puchalt, Aisling Brady, Francisca Gallego del Sol, Javier Mancheño-Bonillo, Alonso Felipe-Ruíz, Wilfried J. J. Meijer, José R. Penadés, and Alberto Marina. Antagonistic interactions between phage and host factors control arbitrium lysis–lysogeny decision. Nature Microbiology, 9:161-172, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01550-4, doi:10.1038/s41564-023-01550-4. This article has 13 citations and is from a highest quality peer-reviewed journal.

42. (erez2017communicationbetweenviruses pages 21-23): Zohar Erez, Ida Steinberger-Levy, Maya Shamir, Shany Doron, Avigail Stokar-Avihail, Yoav Peleg, Sarah Melamed, Azita Leavitt, Alon Savidor, Shira Albeck, Gil Amitai, and Rotem Sorek. Communication between viruses guides lysis–lysogeny decisions. Nature, 541:488-493, Jan 2017. URL: https://doi.org/10.1038/nature21049, doi:10.1038/nature21049. This article has 827 citations and is from a highest quality peer-reviewed journal.

43. (brady2021molecularbasisof pages 17-20): Aisling Brady, Alonso Felipe-Ruiz, Francisca Gallego del Sol, Alberto Marina, Nuria Quiles-Puchalt, and José R. Penadés. Molecular basis of lysis–lysogeny decisions in gram-positive phages. Annual Review of Microbiology, 75:563-581, Oct 2021. URL: https://doi.org/10.1146/annurev-micro-033121-020757, doi:10.1146/annurev-micro-033121-020757. This article has 72 citations and is from a peer-reviewed journal.

44. (sol2019decipheringthemolecular pages 17-18): Francisca Gallego del Sol, José R. Penadés, and Alberto Marina. Deciphering the molecular mechanism underpinning phage arbitrium communication systems. Molecular Cell, 74:59-72.e3, Apr 2019. URL: https://doi.org/10.1016/j.molcel.2019.01.025, doi:10.1016/j.molcel.2019.01.025. This article has 60 citations and is from a highest quality peer-reviewed journal.

45. (zhen2019structuralbasisof pages 1-3): Xiangkai Zhen, Huan Zhou, Wei Ding, Biao Zhou, Xiaolong Xu, Vanja Perčulija, Chun-Jung Chen, Ming-Xian Chang, Muhammad Iqbal Choudhary, and Songying Ouyang. Structural basis of aimp signaling molecule recognition by aimr in spbeta group of bacteriophages. Protein & Cell, 10:131-136, Nov 2019. URL: https://doi.org/10.1007/s13238-018-0588-6, doi:10.1007/s13238-018-0588-6. This article has 22 citations and is from a peer-reviewed journal.

46. (wang2018structuralbasisof pages 1-15): Qiang Wang, Zeyuan Guan, Kai Pei, Jing Wang, Zhu Liu, Ping Yin, Donghai Peng, and Tingting Zou. Structural basis of the arbitrium peptide–aimr communication system in the phage lysis–lysogeny decision. Nature Microbiology, 3:1266-1273, Sep 2018. URL: https://doi.org/10.1038/s41564-018-0239-y, doi:10.1038/s41564-018-0239-y. This article has 47 citations and is from a highest quality peer-reviewed journal.

47. (guan2019structuralinsightsinto pages 1-2): Zeyuan Guan, Kai Pei, Jing Wang, Yongqing Cui, Xiang Zhu, Xiang Su, Yuanbao Zhou, Delin Zhang, Chun Tang, Ping Yin, Zhu Liu, and Tingting Zou. Structural insights into dna recognition by aimr of the arbitrium communication system in the spbeta phage. Cell Discovery, May 2019. URL: https://doi.org/10.1038/s41421-019-0101-2, doi:10.1038/s41421-019-0101-2. This article has 23 citations and is from a peer-reviewed journal.

48. (vela2023emerginginvestigatorseries pages 4-5): Jeseth Delgado Vela and Mitham Al-Faliti. Emerging investigator series: the role of phage lifestyle in wastewater microbial community structures and functions: insights into diverse microbial environments. Environmental Science: Water Research &amp; Technology, 9:1982-1991, Jan 2023. URL: https://doi.org/10.1039/d2ew00755j, doi:10.1039/d2ew00755j. This article has 6 citations.
