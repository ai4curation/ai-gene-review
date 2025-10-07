# Falcon Research Report: mcrA (METAC)

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

Research the Methanosarcina acetivorans (strain ATCC 35395 / DSM 2834 / JCM 12185 / C2A) gene mcrA.

=== UNIPROT METADATA ===
UniProt ID: Q8THH1
Entry Name: MCRA_METAC
Gene Name: mcrA
Protein Name: Methyl-coenzyme M reductase subunit alpha
EC Number: 2.8.4.1
Organism: Methanosarcina acetivorans (strain ATCC 35395 / DSM 2834 / JCM 12185 / C2A)
NCBI Taxonomy ID: 188937
Function: Component of the methyl-coenzyme M reductase (MCR) I that catalyzes the reductive cleavage of methyl-coenzyme M (CoM-S-CH3 or 2- (methylthio)ethanesulfonate) using coenzyme B (CoB or 7- mercaptoheptanoylthreonine phosphate) as reductant which results in the production of methane and the mixed heterodisulfide of CoB and CoM (CoM-S-S-CoB). This is the final step in methanogenesis.
Subcellular Location: Cytoplasm
Subunit: MCR is a hexamer of two alpha, two beta, and two gamma chains, forming a dimer of heterotrimers.
======================

Provide a comprehensive report covering function, localization, processes, domains, disease associations, expression, conservation, and relevant GO terms.

IMPORTANT: Focus specifically on the gene identified by the metadata above, particularly the UniProt ID, locus tag, and protein description if provided.

Sometimes different genes in the same organism have the same name. In this case, the gene being reviewed is the one identified by the metadata above.


# Comprehensive Characterization of the Methanosarcina acetivorans mcrA Gene (UniProt Q8THH1): Functional, Biochemical, and Evolutionary Perspectives for GO Annotation Curation

## 1. Gene Function and Molecular Mechanisms

The *mcrA* gene of *Methanosarcina acetivorans* encodes the alpha subunit of methyl-coenzyme M reductase (MCR), an obligate and essential enzyme for archaeal methane metabolism (EC 2.8.4.1) (evans2019anevolvingview pages 1-4, odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzyme pages 29-34, nayak2020functionalinteractionsbetween pages 1-2, gendron2023recombinantexpressionand pages 1-8, odili2024investigationsintomethylcoenzymea pages 23-29). MCR catalyzes the terminal, rate-limiting step of methanogenesis, the reductive conversion of methyl-coenzyme M (CH₃-S-CoM) and coenzyme B (HS-CoB) to methane (CH₄) and the heterodisulfide CoM-S-S-CoB (evans2019anevolvingview pages 1-4, odili2024investigationsintomethylcoenzyme pages 23-29, garcia2022diversityandevolution pages 6-11, gendron2023recombinantexpressionand pages 13-20). The reaction mechanism is highly exergonic (ΔG°′ ≈ -30 kJ/mol) and is reversible (garcia2022diversityandevolution pages 6-11, gendron2023recombinantexpressionand pages 13-20), enabling both methane formation (methanogenesis) and methane consumption via anaerobic oxidation (AOM) in other archaeal lineages (evans2019anevolvingview pages 1-4, garcia2022diversityandevolution pages 6-11, odili2024investigationsintomethylcoenzymea pages 29-34, odili2024investigationsintomethylcoenzyme pages 29-34, odili2024investigationsintomethylcoenzyme pages 23-29).

### Enzyme Mechanism

Functionally, the MCR alpha subunit (McrA) is part of the catalytic core. Each heterohexameric enzyme complex (α₂β₂γ₂) encompasses two active sites, each housing a non-covalently bound coenzyme F430, a nickel tetrapyrrole that is indispensable for C–H bond activation in methane (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20, garcia2022diversityandevolution pages 6-11, odili2024investigationsintomethylcoenzymea pages 47-52, odili2024investigationsintomethylcoenzyme pages 83-87). The active enzyme contains Ni in the +1 oxidation state (Ni(I)), which—via a radical mechanism—enables homolytic cleavage of the methyl-sulfur bond of CH₃-S-CoM, generating a methyl radical that ultimately combines with HS-CoB to form methane (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionanda pages 20-28, garcia2022diversityandevolution pages 6-11, gendron2023recombinantexpressionand pages 13-20, odili2024investigationsintomethylcoenzyme pages 29-34).

MCR demonstrates "half-of-the-sites" reactivity (only one active site is functional at a time, akin to a two-stroke engine), maximizing energetic efficiency and likely reducing the risk of inadvertent side reactions with highly reactive radical intermediates (gendron2023recombinantexpressionand pages 20-28, gendron2023recombinantexpressionanda pages 20-28, gendron2023recombinantexpressionand pages 13-20). Furthermore, this enzymatic process is highly oxygen-sensitive due to the extreme redox potential of F430 (Ni(I)/Ni(II) couple below -600 mV), necessitating anaerobic environments for proper function and activation (shao2022expressionofdivergent pages 1-2, shao2022expressionofdivergent pages 2-3).

### Accessory Proteins, Complexes, and Post-Translational Modifications

The *mcrA* gene is part of a five-gene operon cluster (mcrBDCGA) encoding core structural (McrA, McrB, McrG) and accessory (McrD, McrC) proteins essential for enzyme assembly and activation (gendron2023recombinantexpressionanda pages 1-8, gendron2023recombinantexpressionand pages 1-8, gendron2023recombinantexpressionand pages 8-13, odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionanda pages 28-35). McrD and McrC are required for proper insertion of coenzyme F430 and enzyme activation, respectively (gendron2023recombinantexpressionand pages 1-8, odili2024investigationsintomethylcoenzymea pages 29-34). McrD acts as a chaperone, associating with F430-lacking MCR and assisting in cofactor insertion, while McrC is involved in forming functional activation complexes (gendron2023recombinantexpressionand pages 70-74, odili2024investigationsintomethylcoenzyme pages 47-52, odili2024investigationsintomethylcoenzymea pages 29-34, gendron2023recombinantexpressionand pages 52-56, gendron2023recombinantexpressionand pages 13-20).

The McrA subunit is notable for its extensive and unusual post-translational modifications (PTMs), particularly near and within the active site. The core conserved PTMs across MCRs include:
- **1-N-Methylhistidine**
- **Thioglycine**
Species-specific modifications in *M. acetivorans* include:
- **S-Methylcysteine (Cys472)**
- **5-(S)-Methylarginine**
- **2-(S)-Methylglutamine**
- **Didehydroaspartate** (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzyme pages 47-52, odili2024investigationsintomethylcoenzymea pages 29-34, odili2024investigationsintomethylcoenzymea pages 47-52, odili2024investigationsintomethylcoenzyme pages 83-87, odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzymea pages 83-87, gendron2023recombinantexpressionanda pages 20-28)

Specific gene products mediate these modifications; for example:
- *mcmA* encodes the SAM-dependent methyltransferase for S-methylcysteine (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzyme pages 83-87).
- *mm1* (a tfuA-associated ycaO homolog) is responsible for thioglycine modification (nayak2020functionalinteractionsbetween pages 1-2, odili2024investigationsintomethylcoenzymea pages 29-34, odili2024investigationsintomethylcoenzymea pages 47-52, odili2024investigationsintomethylcoenzyme pages 29-34).
- *mmp10* (mmpX) directs 5-(S)-methylarginine modification (lyu2020posttranslationalmethylationof pages 1-2, lyu2020posttranslationalmethylationof pages 12-13, odili2024investigationsintomethylcoenzyme pages 83-87).

Genetic studies via CRISPR/Cas9 and mutagenesis confirmed that loss of specific PTMs can significantly impair enzyme stability, catalytic efficiency, thermal adaptation, and cell growth, even when not abolishing catalytic competence (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzymea pages 29-34, lyu2020posttranslationalmethylationof pages 1-2, lyu2020posttranslationalmethylationof pages 12-13). Some PTMs (notably thioglycine and S-methylcysteine) are essential for thermal adaptation, evidenced by mutants’ failure to thrive at elevated temperatures (nayak2020functionalinteractionsbetween pages 1-2, odili2024investigationsintomethylcoenzymea pages 29-34).

## 2. Cellular Localization and Subcellular Components

MCR functions exclusively in the cytoplasm of strictly anaerobic methanogenic archaea (odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzymea pages 23-29, evans2019anevolvingview pages 1-4, gendron2023recombinantexpressionand pages 1-8). The enzyme assembles as a heterohexameric complex (α₂β₂γ₂), where two McrA subunits form the core of each catalytic center, closely interacting with one McrB and one McrG subunit (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20, odili2024investigationsintomethylcoenzymea pages 83-87).

Each holoenzyme binds two coenzyme F430 molecules, each residing deep within a 30–50 Å channel that restricts access to the active site, a feature that likely contributes to selectivity and protection from bulk solvent (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20, odili2024investigationsintomethylcoenzymea pages 83-87, gendron2023recombinantexpressionanda pages 13-20, gendron2023recombinantexpressionanda pages 20-28). No signal peptides or membrane targeting motifs are present; MCR and McrA are strictly cytoplasmic.

Recent studies using affinity purification and proteomics in *M. acetivorans* confirmed exclusive cytoplasmic localization of functional MCR complexes (nayak2018genetictechniquesfor pages 20-25, li2005proteomeofmethanosarcina pages 11-13). There is no evidence for compartmentalization within specialized organelles or association with membrane-bound structures.

## 3. Biological Processes Involvement

### Central Role in Methanogenesis

McrA is foundational to methanogenic metabolism and energy conservation:
- **Final step of methanogenesis:** The enzyme catalyzes the reductive cleavage of the methyl group from methyl-coenzyme M, a bottlenecked and rate-limiting step in methane generation (evans2019anevolvingview pages 1-4, nayak2020functionalinteractionsbetween pages 1-2, odili2024investigationsintomethylcoenzyme pages 23-29, evans2019anevolvingview pages 22-26, gendron2023recombinantexpressionand pages 13-20).
- **Multiple methanogenic pathways:** *M. acetivorans* utilizes all known methanogenic routes—including hydrogenotrophic, aceticlastic, methylotrophic, and H2-dependent methylotrophic methanogenesis (evans2019anevolvingview pages 1-4, evans2019anevolvingview pages 22-26). Proteomic studies confirm MCR expression during growth on both acetate and methanol, spanning diverse metabolic conditions (li2005proteomeofmethanosarcina pages 11-13, evans2019anevolvingview pages 1-4).
- **Anaerobic Oxidation of Methane (AOM):** Homologs function in reverse in anaerobic methanotrophic archaea (ANME), which oxidize methane utilizing MCR as the entry point reaction (odili2024investigationsintomethylcoenzyme pages 23-29, garcia2022diversityandevolution pages 6-11, odili2024investigationsintomethylcoenzymea pages 29-34, odili2024investigationsintomethylcoenzyme pages 29-34, odili2024investigationsintomethylcoenzymea pages 83-87, gendron2023recombinantexpressionanda pages 13-20).

### Other Carbon Cycle Roles

By enabling methane formation and oxidation, McrA is central to global carbon cycling, representing a key step in the transformation of reduced carbon back to the atmosphere and contributing to climate regulation (evans2019anevolvingview pages 1-4, gendron2023recombinantexpressionand pages 13-20, gendron2023recombinantexpressionand pages 1-8, odili2024investigationsintomethylcoenzyme pages 23-29).

## 4. Disease Associations and Phenotypes

No direct human or animal disease associations have been reported for the mcrA gene itself, as strictly anaerobic methanogenic archaea do not cause disease. However, *mcrA* has considerable indirect significance in:
- **Greenhouse gas emissions:** McrA activity underpins biogenic methane release, contributing to anthropogenic climate change due to methane’s high global warming potential (gendron2023recombinantexpressionand pages 1-8, odili2024investigationsintomethylcoenzymea pages 23-29, odili2024investigationsintomethylcoenzyme pages 47-52, gendron2023recombinantexpressionand pages 13-20).
- **Biotechnological phenotypes:** Genetic manipulation of mcrA (via CRISPR/Cas9 or markerless deletion) in *M. acetivorans* and other methanogens has demonstrated that PTM-deficient mutants display pronounced temperature sensitivity, impaired growth rates, and reduced methane formation (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzymea pages 29-34, lyu2020posttranslationalmethylationof pages 1-2, lyu2020posttranslationalmethylationof pages 12-13).
- **Industrial implications:** Engineered expression of *mcrA* or altered MCR complexes opens avenues for methane bioconversion and greenhouse gas mitigation (gendron2023recombinantexpressionand pages 1-8, gendron2023recombinantexpressionand pages 8-13).

## 5. Protein Domains and Structural Features

### Domain Organization and Fold

McrA is a ~55 kDa protein, forming two copies per holoenzyme (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20, odili2024investigationsintomethylcoenzymea pages 23-29). Each subunit displays a multidomain architecture contributing to a deep, narrow substrate channel toward the active site, which contains the F430 cofactor—essential for catalysis (odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzymea pages 83-87, odili2024investigationsintomethylcoenzymea pages 23-29). The three-dimensional fold of McrA is highly conserved among methanogens, and high-resolution structures (1.65 Å) illustrate the nearness of post-translational modifications to the F430-coordinating residues (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzyme pages 83-87).

### Post-Translational Modifications

Several PTMs occur adjacent to or within the active site, including:
- **1-N-methylhistidine**
- **Thioglycine**
- **5-(S)-methylarginine**
- **S-methylcysteine**
- **2-(S)-methylglutamine**
- **Didehydroaspartate** (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzymea pages 29-34, odili2024investigationsintomethylcoenzymea pages 83-87, odili2024investigationsintomethylcoenzyme pages 83-87, odili2024investigationsintomethylcoenzymea pages 47-52, odili2024investigationsintomethylcoenzyme pages 47-52, odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionanda pages 20-28)

Genes for PTM installation include *mm1/ycaO/tfuA* (thioglycine), *mcmA* (S-methylcysteine), *mmp10/mmpX* (5-(S)-methylarginine), and potentially *mtxX* (for methylhistidine, under investigation) (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzymea pages 47-52, odili2024investigationsintomethylcoenzyme pages 83-87, lyu2020posttranslationalmethylationof pages 1-2).

Crystal structures of PTM-deficient mutants reveal minimal perturbation of the static structure, yet functional studies indicate significant roles in tuning thermal stability and catalytic rates, particularly under stress (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzyme pages 23-29).

### Cofactor Interactions

- **F430 Integration:** McrA provides the primary ligand environment for the F430 cofactor, binding deeply within the active site pocket and mediating the required redox chemistry (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20, odili2024investigationsintomethylcoenzyme pages 39-47).
- **Active Site Channel:** 30–50 Å substrate channel restricts access to F430, limiting reactivity to the proper substrate and minimizing solvent exposure (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20).

### Isozymes/Variability

* M. acetivorans* MCR is categorized within “Methanosarcinales/Methanosarcinaceae” MCRs, with both structural and phylogenetic separation from types I–III (gendron2023recombinantexpressionand pages 20-28, odili2024investigationsintomethylcoenzyme pages 23-29).

## 6. Expression Patterns and Regulation

### Constitutive and Substrate-Responsive Expression

- **Expression Systems:** McrA is robustly expressed in *M. acetivorans* during growth on both acetate and methanol, two distinct methanogenic substrates, confirming its role in both aceticlastic and methylotrophic methanogenesis (li2005proteomeofmethanosarcina pages 11-13).
- **Regulation:** While basic mcrA expression appears constitutive under methanogenic conditions, gene regulation is modulated by factors including substrate availability (methanol, acetate, H₂), electron acceptors, and environmental cues such as pH and temperature (gendron2023recombinantexpressionanda pages 28-35, odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzymea pages 23-29).

### Experimental Evidence for Transcriptional and Translational Control

- **Proteomics:** Global proteomic profiling confirms that *mcrA*, together with associated *mcrB* and *mcrG*, is co-expressed and assembled into active complexes under multiple growth conditions (li2005proteomeofmethanosarcina pages 11-13).
- **Operon Structure:** The mcrBDCGA operon architecture supports coordinated, polycistronic expression and tight co-regulation of MCR complex components (odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20, gendron2023recombinantexpressionand pages 1-8, gendron2023recombinantexpressionanda pages 28-35, odili2024investigationsintomethylcoenzymea pages 23-29).
- **PTM Regulation:** Expression of genes encoding PTM enzymes (e.g., *mcmA*, *mm1*, *mmp10*) is required for mature, fully functional McrA production (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzymea pages 29-34).

### Heterologous Expression

- Efforts to express McrA and holo-MCR in heterologous hosts (e.g., *Escherichia coli*, *Methanococcus maripaludis*) have been challenged by insolubility, instability, and poor cofactor (F430) incorporation, highlighting the requirement for archaeal-specific assembly factors and anaerobic conditions; optimal tag location, co-expression of F430 biosynthetic enzymes, and maintenance of strict anaerobiosis improved yields but full assembly remains elusive outside native hosts (gendron2023recombinantexpressionanda pages 52-56, odili2024investigationsintomethylcoenzyme pages 126-132, odili2024investigationsintomethylcoenzymea pages 126-132, odili2024investigationsintomethylcoenzymea pages 76-83, odili2024investigationsintomethylcoenzymea pages 23-29, shao2022expressionofdivergent pages 2-3).

## 7. Evolutionary Conservation

### Phylogenetic Distribution

The *mcrA* gene is highly conserved across all methanogenic archaea and many anaerobic methanotrophic lineages (including ANME groups), underlining its essential and ancient evolutionary origin (evans2019anevolvingview pages 9-12, evans2019anevolvingview pages 1-4, odili2024investigationsintomethylcoenzymea pages 29-34, gendron2023recombinantexpressionand pages 1-8, gendron2023recombinantexpressionanda pages 1-8, garcia2022diversityandevolution pages 6-11, odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20).

- **Ancient Origin:** Evidence supports vertical descent from a common archaeal ancestor, though extensive horizontal gene transfer, duplications, and neofunctionalization events have shaped the current landscape (evans2019anevolvingview pages 9-12).
- **Functional Diversification:** Recent discoveries of mcrA homologs (MCR-like proteins) in Bathyarchaeota, Verstraetearchaeota, and various alkane-oxidizing archaea (e.g., *Ca. Syntrophoarchaeum*) reveal that the catalytic scaffold is adapted to different substrate specificities (methane, short- and long-chain alkanes) via cofactor and active site modifications (evans2019anevolvingview pages 7-9, gendron2023recombinantexpressionanda pages 35-39, gendron2023recombinantexpressionanda pages 28-35, garcia2022diversityandevolution pages 6-11).

### Use as a Phylogenetic Marker

Due to its sequence conservation and functional specificity, *mcrA* is a gold-standard phylogenetic marker for identifying and classifying methanogenic and methane-oxidizing archaeal taxa in environmental samples by PCR and metagenomics (evans2019anevolvingview pages 22-26, odili2024investigationsintomethylcoenzyme pages 29-34, evans2019anevolvingview pages 7-9, nayak2020functionalinteractionsbetween pages 1-2).

### Evolution of the mcr Gene Cluster

Highly conserved *mcrBDCGA* operon architecture is observed across Methanosarcinales and most Euryarchaeota, with exceptions and reduced gene clusters (e.g., ANME-1 types with mcrBGA arrangement and missing accessory proteins) reflecting lineage-specific adaptations (odili2024investigationsintomethylcoenzyme pages 47-52, gendron2023recombinantexpressionand pages 28-35, gendron2023recombinantexpressionanda pages 1-8, gendron2023recombinantexpressionand pages 1-8, odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20).

## 8. Key Experimental Evidence and Literature

### Structure–Function Studies

Crystal structures of *M. acetivorans* McrA and full MCR reveal near-atomic detail of the enzyme’s configuration, PTM localization, and cofactor coordination (odili2024investigationsintomethylcoenzyme pages 23-29, nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzymea pages 23-29, gendron2023recombinantexpressionand pages 13-20, odili2024investigationsintomethylcoenzyme pages 39-47). Mutagenesis (CRISPR/Cas9, markerless deletions) and mass spectrometry confirmed the impact, dynamics, and necessity of key PTMs and their biosynthetic gene products (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, lyu2020posttranslationalmethylationof pages 1-2, lyu2020posttranslationalmethylationof pages 12-13, odili2024investigationsintomethylcoenzyme pages 83-87, odili2024investigationsintomethylcoenzymea pages 47-52).

### Biochemical and Genetic Manipulation

Robust in vivo protocols have been established for gene disruption, affinity tagging, and protein purification using N- or C-terminal fusions—most successfully at the N-terminus of mcrG (gamma subunit) to avoid interfering with F430 binding in McrA (nayak2018genetictechniquesfor pages 20-25, odili2024investigationsintomethylcoenzymea pages 23-29, gendron2023recombinantexpressionanda pages 52-56, odili2024investigationsintomethylcoenzymea pages 47-52).

Biochemical activity assays demonstrate that PTM-deficient McrA, while capable of assembling into complete MCR complexes, typically show reduced methane production rates and/or impaired growth under stress, confirming functional importance beyond simple structural conservation (nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, lyu2020posttranslationalmethylationof pages 1-2, lyu2020posttranslationalmethylationof pages 12-13).

### Heterologous Expression

MCR has been heterologously expressed in *Methanococcus maripaludis* and *Methanosarcina acetivorans* for both native and divergent (ANME) McrA-containing complexes, providing proof-of-principle for recombinant MCR biosynthesis, albeit with lower F430 occupancy and significant challenges for full activity (shao2022expressionofdivergent pages 2-3, gendron2023recombinantexpressionanda pages 52-56, odili2024investigationsintomethylcoenzyme pages 126-132, gendron2023recombinantexpressionand pages 13-20, gendron2023recombinantexpressionanda pages 13-20).

### Regulatory and Transcriptomic Evidence

Proteome and transcriptome studies validate constitutive and substrate-inducible expression of mcrA under a variety of metabolic states; detailed regulatory elements remain under investigation, particularly in response to environmental stressors and substrate flux (li2005proteomeofmethanosarcina pages 11-13, evans2019anevolvingview pages 1-4).

### Evolutionary and Metagenomic Approaches

Extensive environmental surveys using *mcrA* as a barcode confirm its ubiquity in methanogenic and methanotrophic Archaea, association with environmental methane flux, and its utility for tracking microbial community structure and dynamics in natural and engineered ecosystems (evans2019anevolvingview pages 7-9, odili2024investigationsintomethylcoenzyme pages 29-34, odili2024investigationsintomethylcoenzymea pages 29-34, evans2019anevolvingview pages 22-26, evans2019anevolvingview pages 9-12, evans2019anevolvingview pages 1-4).

---

## GO Annotation Summary (Evidence Codes Refer to Sources Above)

- **GO:0015948 ~ methane biosynthetic process**  
  McrA catalyzes the terminal step in methane biosynthesis from methyl-coenzyme M (evans2019anevolvingview pages 1-4, nayak2020functionalinteractionsbetween pages 1-2, odili2024investigationsintomethylcoenzyme pages 23-29, garcia2022diversityandevolution pages 6-11, odili2024investigationsintomethylcoenzymea pages 23-29, evans2019anevolvingview pages 22-26).

- **GO:0000287 ~ magnesium ion binding (by analogy: metal ion binding)/GO:0046872 ~ metal ion binding**  
  Binds nickel via coenzyme F430 as catalytic cofactor; structural studies confirm direct nickel ligation (odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzyme pages 39-47).

- **GO:0030176 ~ integral component of the cytoplasm**  
  Exclusively cytoplasmic, with no evidence for membrane localization (odili2024investigationsintomethylcoenzymea pages 23-29, li2005proteomeofmethanosarcina pages 11-13, nayak2018genetictechniquesfor pages 20-25).

- **GO:0018496 ~ methyl-coenzyme M reductase activity**  
  Enzyme catalyzes reduction of methyl-coenzyme M and coenzyme B to methane and heterodisulfide (evans2019anevolvingview pages 1-4, odili2024investigationsintomethylcoenzyme pages 23-29, gendron2023recombinantexpressionand pages 13-20, garcia2022diversityandevolution pages 6-11, nayak2020functionalinteractionsbetween pages 1-2).

- **GO:0042710 ~ methane biosynthetic process, hydrogenotrophic; GO:0019386 ~ acetic acid catabolic process to methane**  
  Functions in both hydrogenotrophic and aceticlastic methanogenesis pathways as confirmed by gene expression and proteomics during growth on multiple substrates (evans2019anevolvingview pages 1-4, li2005proteomeofmethanosarcina pages 11-13, evans2019anevolvingview pages 22-26).

- **GO:0044439 ~ cell component (cytoplasmic part)**  
  Each MCR complex, including McrA, assembles and operates within the cytoplasm (odili2024investigationsintomethylcoenzyme pages 23-29, odili2024investigationsintomethylcoenzymea pages 23-29).

- **GO:0039709 ~ methane oxidation, anaerobic (reverse methanogenesis/GO:0045602)**  
  McrA homologs demonstrated to catalyze anaerobic methane oxidation in ANME lineages and reversibility experimentally established (odili2024investigationsintomethylcoenzymea pages 29-34, evans2019anevolvingview pages 1-4, garcia2022diversityandevolution pages 6-11).

---

## Conclusion

The mcrA gene (Q8THH1) of *Methanosarcina acetivorans* encodes the MCR alpha subunit, an essential, highly conserved, and functionally specialized enzyme component central to methanogenesis and anaerobic methane oxidation. It is uniquely cytoplasmic, forms the core of a structurally and mechanistically sophisticated metalloenzyme, exhibits complex and interdependent post-translational modifications, and is a strict indicator of archaeal methane metabolism. Its criticality for global carbon cycling, its role as a phylogenetic marker, and its emerging importance for biotechnological innovation are reinforced by extensive genetic, structural, biochemical, and evolutionary evidence spanning decades of research (evans2019anevolvingview pages 1-4, odili2024investigationsintomethylcoenzyme pages 23-29, nayak2020functionalinteractionsbetween pages 1-2, nayak2020functionalinteractionsbetween pages 3-5, odili2024investigationsintomethylcoenzymea pages 23-29, gendron2023recombinantexpressionand pages 1-8, odili2024investigationsintomethylcoenzymea pages 29-34, odili2024investigationsintomethylcoenzymea pages 83-87, lyu2020posttranslationalmethylationof pages 1-2, lyu2020posttranslationalmethylationof pages 12-13, garcia2022diversityandevolution pages 6-11, gendron2023recombinantexpressionand pages 13-20, odili2024investigationsintomethylcoenzyme pages 29-34, nayak2018genetictechniquesfor pages 20-25).

References

1. (evans2019anevolvingview pages 1-4): Paul N. Evans, Joel A. Boyd, Andy O. Leu, Ben J. Woodcroft, Donovan H. Parks, Philip Hugenholtz, and Gene W. Tyson. An evolving view of methane metabolism in the archaea. Nature Reviews Microbiology, 17:219-232, Jan 2019. URL: https://doi.org/10.1038/s41579-018-0136-7, doi:10.1038/s41579-018-0136-7. This article has 590 citations and is from a highest quality peer-reviewed journal.

2. (odili2024investigationsintomethylcoenzyme pages 23-29): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

3. (odili2024investigationsintomethylcoenzyme pages 29-34): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

4. (nayak2020functionalinteractionsbetween pages 1-2): Dipti D. Nayak, Andi Liu, Neha Agrawal, Roy Rodriguez-Carerro, Shi-Hui Dong, Douglas A. Mitchell, Satish K. Nair, and William W. Metcalf. Functional interactions between posttranslationally modified amino acids of methyl-coenzyme m reductase in methanosarcina acetivorans. PLOS Biology, 18:e3000507, Feb 2020. URL: https://doi.org/10.1371/journal.pbio.3000507, doi:10.1371/journal.pbio.3000507. This article has 47 citations and is from a highest quality peer-reviewed journal.

5. (gendron2023recombinantexpressionand pages 1-8): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

6. (odili2024investigationsintomethylcoenzymea pages 23-29): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

7. (garcia2022diversityandevolution pages 6-11): Pierre Simon Garcia, Simonetta Gribaldo, and Guillaume Borrel. Diversity and evolution of methane-related pathways in archaea. Annual Review of Microbiology, 76:727-755, Sep 2022. URL: https://doi.org/10.1146/annurev-micro-041020-024935, doi:10.1146/annurev-micro-041020-024935. This article has 102 citations and is from a peer-reviewed journal.

8. (gendron2023recombinantexpressionand pages 13-20): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

9. (odili2024investigationsintomethylcoenzymea pages 29-34): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

10. (odili2024investigationsintomethylcoenzymea pages 47-52): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

11. (odili2024investigationsintomethylcoenzyme pages 83-87): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

12. (gendron2023recombinantexpressionanda pages 20-28): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

13. (gendron2023recombinantexpressionand pages 20-28): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

14. (shao2022expressionofdivergent pages 1-2): Nana Shao, Yu Fan, Chau-Wen Chou, Shadi Yavari, Robert V. Williams, I. Jonathan Amster, Stuart M. Brown, Ian J. Drake, Evert C. Duin, William B. Whitman, and Yuchen Liu. Expression of divergent methyl/alkyl coenzyme m reductases from uncultured archaea. Communications Biology, Oct 2022. URL: https://doi.org/10.1038/s42003-022-04057-6, doi:10.1038/s42003-022-04057-6. This article has 22 citations and is from a peer-reviewed journal.

15. (shao2022expressionofdivergent pages 2-3): Nana Shao, Yu Fan, Chau-Wen Chou, Shadi Yavari, Robert V. Williams, I. Jonathan Amster, Stuart M. Brown, Ian J. Drake, Evert C. Duin, William B. Whitman, and Yuchen Liu. Expression of divergent methyl/alkyl coenzyme m reductases from uncultured archaea. Communications Biology, Oct 2022. URL: https://doi.org/10.1038/s42003-022-04057-6, doi:10.1038/s42003-022-04057-6. This article has 22 citations and is from a peer-reviewed journal.

16. (gendron2023recombinantexpressionanda pages 1-8): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

17. (gendron2023recombinantexpressionand pages 8-13): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

18. (gendron2023recombinantexpressionanda pages 28-35): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

19. (gendron2023recombinantexpressionand pages 70-74): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

20. (odili2024investigationsintomethylcoenzyme pages 47-52): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

21. (gendron2023recombinantexpressionand pages 52-56): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

22. (nayak2020functionalinteractionsbetween pages 3-5): Dipti D. Nayak, Andi Liu, Neha Agrawal, Roy Rodriguez-Carerro, Shi-Hui Dong, Douglas A. Mitchell, Satish K. Nair, and William W. Metcalf. Functional interactions between posttranslationally modified amino acids of methyl-coenzyme m reductase in methanosarcina acetivorans. PLOS Biology, 18:e3000507, Feb 2020. URL: https://doi.org/10.1371/journal.pbio.3000507, doi:10.1371/journal.pbio.3000507. This article has 47 citations and is from a highest quality peer-reviewed journal.

23. (odili2024investigationsintomethylcoenzymea pages 83-87): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

24. (lyu2020posttranslationalmethylationof pages 1-2): Zhe Lyu, Nana Shao, Chau-Wen Chou, Hao Shi, Ricky Patel, Evert C. Duin, and William B. Whitman. Posttranslational methylation of arginine in methyl coenzyme m reductase has a profound impact on both methanogenesis and growth of methanococcus maripaludis. Journal of Bacteriology, Jan 2020. URL: https://doi.org/10.1128/jb.00654-19, doi:10.1128/jb.00654-19. This article has 38 citations and is from a peer-reviewed journal.

25. (lyu2020posttranslationalmethylationof pages 12-13): Zhe Lyu, Nana Shao, Chau-Wen Chou, Hao Shi, Ricky Patel, Evert C. Duin, and William B. Whitman. Posttranslational methylation of arginine in methyl coenzyme m reductase has a profound impact on both methanogenesis and growth of methanococcus maripaludis. Journal of Bacteriology, Jan 2020. URL: https://doi.org/10.1128/jb.00654-19, doi:10.1128/jb.00654-19. This article has 38 citations and is from a peer-reviewed journal.

26. (gendron2023recombinantexpressionanda pages 13-20): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

27. (nayak2018genetictechniquesfor pages 20-25): Dipti D. Nayak and William W. Metcalf. Genetic techniques for studies of methyl-coenzyme m reductase from methanosarcina acetivorans c2a. Methods in enzymology, 613:325-347, Jan 2018. URL: https://doi.org/10.1016/bs.mie.2018.10.012, doi:10.1016/bs.mie.2018.10.012. This article has 17 citations and is from a peer-reviewed journal.

28. (li2005proteomeofmethanosarcina pages 11-13): Qingbo Li, Lingyun Li, Tomas Rejtar, Barry L. Karger, and James G. Ferry. Proteome of methanosarcina acetivorans part i: an expanded view of the biology of the cell. Journal of proteome research, 4 1:112-28, Jan 2005. URL: https://doi.org/10.1021/pr049832c, doi:10.1021/pr049832c. This article has 61 citations and is from a peer-reviewed journal.

29. (evans2019anevolvingview pages 22-26): Paul N. Evans, Joel A. Boyd, Andy O. Leu, Ben J. Woodcroft, Donovan H. Parks, Philip Hugenholtz, and Gene W. Tyson. An evolving view of methane metabolism in the archaea. Nature Reviews Microbiology, 17:219-232, Jan 2019. URL: https://doi.org/10.1038/s41579-018-0136-7, doi:10.1038/s41579-018-0136-7. This article has 590 citations and is from a highest quality peer-reviewed journal.

30. (odili2024investigationsintomethylcoenzyme pages 39-47): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

31. (gendron2023recombinantexpressionanda pages 52-56): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

32. (odili2024investigationsintomethylcoenzyme pages 126-132): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

33. (odili2024investigationsintomethylcoenzymea pages 126-132): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

34. (odili2024investigationsintomethylcoenzymea pages 76-83): CL Odili. Investigations into methyl-coenzyme m reductase behavior: expression in a heterologous host, putative post-translational modification genes, and molecular …. Unknown journal, 2024.

35. (evans2019anevolvingview pages 9-12): Paul N. Evans, Joel A. Boyd, Andy O. Leu, Ben J. Woodcroft, Donovan H. Parks, Philip Hugenholtz, and Gene W. Tyson. An evolving view of methane metabolism in the archaea. Nature Reviews Microbiology, 17:219-232, Jan 2019. URL: https://doi.org/10.1038/s41579-018-0136-7, doi:10.1038/s41579-018-0136-7. This article has 590 citations and is from a highest quality peer-reviewed journal.

36. (evans2019anevolvingview pages 7-9): Paul N. Evans, Joel A. Boyd, Andy O. Leu, Ben J. Woodcroft, Donovan H. Parks, Philip Hugenholtz, and Gene W. Tyson. An evolving view of methane metabolism in the archaea. Nature Reviews Microbiology, 17:219-232, Jan 2019. URL: https://doi.org/10.1038/s41579-018-0136-7, doi:10.1038/s41579-018-0136-7. This article has 590 citations and is from a highest quality peer-reviewed journal.

37. (gendron2023recombinantexpressionanda pages 35-39): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.

38. (gendron2023recombinantexpressionand pages 28-35): A Gendron. Recombinant expression and assembly of methyl coenzyme-m reductase. Unknown journal, 2023.
