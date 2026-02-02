#!/usr/bin/env python3
"""
Script to add suggested_questions and suggested_experiments fields to gene review YAML files.
"""

from pathlib import Path

# Define gene-specific suggested questions and experiments
GENE_SUGGESTIONS = {
    # Human genes
    'CFAP300': {
        'questions': [
            'How does CFAP300 coordinate with other cilia and flagella associated proteins to ensure proper axoneme assembly and stability?',
            'What are the molecular mechanisms by which CFAP300 contributes to ciliary motility and sperm flagellar function?',
            'How do mutations in CFAP300 lead to primary ciliary dyskinesia and male infertility at the cellular and molecular level?',
            'What role does CFAP300 play in the radial spoke complex and how does it interact with dynein arms?'
        ],
        'experiments': [
            'Cryo-electron tomography of cilia and sperm flagella from CFAP300-deficient cells to visualize ultrastructural defects in the axoneme',
            'High-resolution live-cell imaging to track CFAP300 dynamics during ciliogenesis and correlate with ciliary beating patterns',
            'Proteomics analysis of the radial spoke complex to map CFAP300 protein-protein interactions and assembly hierarchy',
            'CRISPR-mediated knock-in of disease-associated CFAP300 variants to study structure-function relationships in ciliary motility'
        ]
    },
    'CFTR': {
        'questions': [
            'How do different classes of CFTR mutations affect protein folding, trafficking, and channel gating at the molecular level?',
            'What are the regulatory mechanisms that control CFTR channel activity in response to cAMP and other signaling pathways?',
            'How does CFTR dysfunction lead to the characteristic thick mucus secretions and bacterial infections in cystic fibrosis?',
            'What determines tissue-specific sensitivity to CFTR dysfunction and why are some organs more severely affected than others?'
        ],
        'experiments': [
            'Single-channel patch-clamp electrophysiology to characterize the gating kinetics and ion selectivity of CFTR variants',
            'Cryo-EM structure determination of full-length CFTR in different conformational states and with bound modulators',
            'Organoid models of cystic fibrosis using patient-derived cells to test personalized therapeutic approaches',
            'Real-time imaging of CFTR trafficking from ER to plasma membrane using fluorescently tagged proteins and live-cell microscopy'
        ]
    },
    'CAMK2A': {
        'questions': [
            'How does autophosphorylation of CAMK2A create molecular memory and contribute to synaptic plasticity and learning?',
            'What determines the subcellular localization of CAMK2A and how does this regulate its access to different substrates?',
            'How do different splice variants of CAMK2A contribute to brain region-specific functions and neuronal plasticity?',
            'What are the mechanisms by which CAMK2A integrates calcium signals with other signaling pathways during synaptic transmission?'
        ],
        'experiments': [
            'Two-photon calcium imaging combined with optogenetics to study CAMK2A activation dynamics in dendritic spines during synaptic plasticity',
            'Cryo-EM structural analysis of CAMK2A holoenzymes in different activation states to understand autophosphorylation mechanisms',
            'Single-molecule tracking of CAMK2A in live neurons to characterize its mobility and clustering at synaptic sites',
            'Proteomics identification of context-specific CAMK2A substrates using chemical crosslinking and mass spectrometry'
        ]
    },
    'CFAP418': {
        'questions': [
            'How does CFAP418 function in ciliary assembly and what specific role does it play in axoneme structure and stability?',
            'What are the molecular interactions between CFAP418 and other ciliary proteins that are essential for proper cilia function?',
            'How do mutations in CFAP418 contribute to ciliopathy phenotypes and what are the downstream cellular consequences?',
            'What determines the tissue-specific expression pattern of CFAP418 and why is it particularly important in certain cell types?'
        ],
        'experiments': [
            'Cryo-electron microscopy of cilia from CFAP418-deficient cells to identify structural abnormalities in the axoneme',
            'Proximity labeling proteomics to identify the complete CFAP418 interactome in ciliated cells',
            'Live-cell imaging of ciliary assembly and disassembly to study CFAP418 dynamics during the cell cycle',
            'Functional complementation studies using CFAP418 orthologs from different species to identify conserved functional domains'
        ]
    },
    'INTU': {
        'questions': [
            'How does INTU regulate intraflagellar transport and what specific cargo does it help transport within cilia?',
            'What are the molecular mechanisms by which INTU coordinates ciliary assembly with cell cycle progression?',
            'How do mutations in INTU lead to left-right asymmetry defects and what role does it play in nodal cilia function?',
            'What determines the specificity of INTU interactions with different intraflagellar transport complexes?'
        ],
        'experiments': [
            'Super-resolution microscopy to track INTU and IFT particle movements along the ciliary axoneme with nanometer precision',
            'Biochemical reconstitution of IFT complexes containing INTU to study cargo loading and transport mechanisms in vitro',
            'Developmental analysis of left-right patterning in INTU mutant embryos using whole-mount in situ hybridization',
            'Proteomics analysis of INTU-associated complexes during different stages of ciliogenesis'
        ]
    },
    'JAK1': {
        'questions': [
            'How does JAK1 achieve specificity in cytokine signaling despite being used by multiple different cytokine receptors?',
            'What are the molecular mechanisms of JAK1 activation and how do negative regulatory mechanisms prevent inappropriate signaling?',
            'How do JAK1 inhibitors achieve selectivity and what are the structural determinants of drug binding and specificity?',
            'What role does JAK1 play in immune cell development versus mature immune cell function and how is this regulated?'
        ],
        'experiments': [
            'Cryo-EM structures of JAK1 in complex with different cytokine receptors to understand receptor-specific activation mechanisms',
            'Single-cell RNA sequencing of immune cells with JAK1 perturbations to map cell-type-specific transcriptional responses',
            'Chemical proteomics to identify off-target effects and selectivity profiles of JAK1 inhibitors in development',
            'Real-time measurement of JAK1 kinase activity using FRET-based biosensors in response to different cytokines'
        ]
    },
    'STAT1': {
        'questions': [
            'How does STAT1 achieve gene-specific transcriptional regulation and what determines its chromatin binding specificity?',
            'What are the molecular mechanisms that distinguish STAT1 homodimer from STAT1-STAT2 heterodimer function?',
            'How do post-translational modifications of STAT1 regulate its nuclear translocation, DNA binding, and transcriptional activity?',
            'What role does STAT1 play in balancing immune activation versus immunosuppression in different disease contexts?'
        ],
        'experiments': [
            'ChIP-seq combined with RNA-seq to map genome-wide STAT1 binding sites and correlate with transcriptional outcomes in different immune contexts',
            'Single-molecule imaging of STAT1 nuclear translocation and chromatin binding dynamics in response to interferon stimulation',
            'Cryo-EM structural determination of STAT1 dimers bound to DNA and associated transcriptional co-regulators',
            'Mass spectrometry-based analysis of STAT1 post-translational modifications and their effects on protein stability and activity'
        ]
    },
    'SCN1A': {
        'questions': [
            'How do different SCN1A mutations affect sodium channel gating properties and contribute to distinct epilepsy phenotypes?',
            'What determines the brain region-specific effects of SCN1A dysfunction and why is inhibitory neuron function particularly affected?',
            'How does SCN1A haploinsufficiency lead to the temperature-sensitive seizures characteristic of Dravet syndrome?',
            'What are the developmental changes in SCN1A expression and function that contribute to age-dependent seizure patterns?'
        ],
        'experiments': [
            'Patch-clamp electrophysiology of SCN1A variants in different neuronal subtypes to correlate biophysical properties with clinical phenotypes',
            'Organoid models of human brain development using patient-derived iPSCs to study SCN1A function in cortical circuit formation',
            'Two-photon calcium imaging in brain slices to study how SCN1A mutations affect inhibitory circuit function and excitability',
            'Cryo-EM structural analysis of SCN1A in different conformational states to understand mutation effects on channel structure'
        ]
    },
    'DHCR24': {
        'questions': [
            'How does DHCR24 coordinate cholesterol biosynthesis with membrane homeostasis and cellular sterol requirements?',
            'What are the regulatory mechanisms that control DHCR24 expression and activity in response to sterol levels?',
            'How do mutations in DHCR24 lead to Smith-Lemli-Opitz syndrome and what are the developmental consequences of altered sterol metabolism?',
            'What determines the subcellular localization of DHCR24 and how does this affect its function in sterol metabolism?'
        ],
        'experiments': [
            'Lipidomics analysis to characterize the complete sterol profile in DHCR24-deficient cells and tissues',
            'Live-cell imaging using fluorescent sterol analogs to track cholesterol metabolism and membrane distribution in real-time',
            'Cryo-EM structure determination of DHCR24 to understand the molecular basis of sterol reduction and enzyme specificity',
            'Developmental analysis of DHCR24 mutant model organisms to study the role of cholesterol in embryogenesis and organogenesis'
        ]
    },
    'ENDOU': {
        'questions': [
            'How does ENDOU achieve specificity for polyuridine sequences and what determines its substrate selectivity?',
            'What role does ENDOU play in placental development and how does it regulate trophoblast function?',
            'How is ENDOU expression and activity regulated during pregnancy and in response to placental stress?',
            'What are the downstream consequences of ENDOU-mediated RNA cleavage on gene expression and protein synthesis?'
        ],
        'experiments': [
            'RNA-seq analysis of ENDOU-deficient placental tissues to identify direct and indirect targets of ENDOU regulation',
            'Biochemical characterization of ENDOU substrate specificity using synthetic RNA oligonucleotides and kinetic analyses',
            'Single-cell RNA sequencing of placental cell types to understand ENDOU function in trophoblast differentiation',
            'Structural biology approaches to determine the molecular basis of ENDOU endonuclease activity and substrate recognition'
        ]
    },
    'CKAP2': {
        'questions': [
            'How does CKAP2 coordinate with other cytoskeletal proteins to regulate microtubule dynamics during cell division?',
            'What determines the cell cycle-dependent expression and phosphorylation of CKAP2?',
            'How does CKAP2 contribute to proper chromosome segregation and what are the consequences of its dysfunction?',
            'What role does CKAP2 play in non-mitotic cells and how does it affect microtubule organization in interphase?'
        ],
        'experiments': [
            'Live-cell imaging of fluorescently tagged CKAP2 to study its dynamics during mitosis and cell division',
            'Cryo-electron tomography of mitotic spindles in CKAP2-depleted cells to visualize microtubule organization defects',
            'Proteomics analysis to identify CKAP2 interacting partners and phosphorylation sites throughout the cell cycle',
            'Single-molecule biophysics to study CKAP2 interactions with microtubules and effects on microtubule stability'
        ]
    },
    'C18orf21': {
        'questions': [
            'What is the molecular function of C18orf21 and how does it contribute to cellular processes?',
            'How is C18orf21 expression regulated and what determines its tissue-specific distribution?',
            'What are the protein domains and structural features that define C18orf21 function?',
            'How does C18orf21 interact with other cellular proteins and what pathways does it regulate?'
        ],
        'experiments': [
            'Proteomics approaches using affinity purification and mass spectrometry to identify C18orf21 interacting partners',
            'Structural characterization using X-ray crystallography or NMR to determine the three-dimensional structure of C18orf21',
            'Functional genomics screens using CRISPR knockout to identify cellular processes dependent on C18orf21',
            'Subcellular localization studies using fluorescent protein fusions to determine C18orf21 cellular distribution'
        ]
    },
    'DNMT1': {
        'questions': [
            'How does DNMT1 maintain DNA methylation patterns during DNA replication while allowing for dynamic changes in gene expression?',
            'What determines the specificity of DNMT1 for hemimethylated CpG sites and how does it avoid de novo methylation?',
            'How do DNMT1-interacting proteins like PCNA and UHRF1 coordinate replication-coupled maintenance methylation?',
            'What are the mechanisms by which DNMT1 dysfunction leads to genome instability and cancer development?'
        ],
        'experiments': [
            'Single-molecule imaging of DNMT1 dynamics at replication forks to study maintenance methylation in real-time',
            'Genome-wide bisulfite sequencing combined with DNMT1 ChIP-seq to map methylation maintenance across the genome',
            'Cryo-EM structural determination of DNMT1 in complex with DNA and regulatory proteins like UHRF1 and PCNA',
            'Chemical biology approaches using methyltransferase inhibitors to study the role of DNMT1 in epigenetic inheritance'
        ]
    },
    'UBA7': {
        'questions': [
            'How does UBA7 specifically activate ISG15 and what determines its selectivity for this ubiquitin-like modifier?',
            'What role does UBA7 play in antiviral immunity and how is its activity regulated during viral infections?',
            'How do different ISG15 conjugates formed by UBA7 contribute to interferon-mediated cellular responses?',
            'What are the structural determinants that allow UBA7 to function as an E1 enzyme for ISG15 but not ubiquitin?'
        ],
        'experiments': [
            'Structural biology approaches to determine the molecular basis of UBA7-ISG15 interaction and activation mechanisms',
            'Proteomics analysis to identify the complete landscape of ISG15 conjugation targets downstream of UBA7',
            'Live-cell imaging to study UBA7 dynamics and ISG15 conjugation during viral infection and interferon responses',
            'Biochemical reconstitution of the ISG15 conjugation pathway to study UBA7 enzyme kinetics and regulation'
        ]
    },
    'SFT2D3': {
        'questions': [
            'What is the specific function of SFT2D3 in intracellular membrane trafficking and organelle biogenesis?',
            'How does SFT2D3 interact with the SNARE machinery and other trafficking regulators?',
            'What determines the subcellular localization of SFT2D3 and how does this relate to its function?',
            'How is SFT2D3 expression and activity regulated in different cell types and conditions?'
        ],
        'experiments': [
            'Live-cell imaging using fluorescently tagged SFT2D3 to study its dynamics and localization in membrane trafficking',
            'Proteomics approaches to identify SFT2D3 interacting partners in different subcellular compartments',
            'Functional analysis using CRISPR knockout to determine the cellular processes dependent on SFT2D3',
            'Electron microscopy analysis of cells lacking SFT2D3 to identify ultrastructural defects in organelle organization'
        ]
    },

    # Mouse genes
    'Ctnnb1': {
        'questions': [
            'How does β-catenin coordinate its dual roles in cell adhesion and Wnt signaling, and what mechanisms prevent crosstalk?',
            'What determines the tissue-specific requirements for β-catenin in development versus homeostasis?',
            'How do different β-catenin mutations lead to distinct developmental disorders and cancer types?',
            'What role does β-catenin play in stem cell maintenance and differentiation across different tissue types?'
        ],
        'experiments': [
            'Single-cell RNA sequencing of tissues with conditional β-catenin knockout to map cell-type-specific transcriptional programs',
            'Super-resolution microscopy to study β-catenin dynamics between adherens junctions and the nucleus during Wnt signaling',
            'Cryo-EM structural determination of β-catenin in complex with different binding partners like cadherins and TCF/LEF',
            'Lineage tracing in mouse models to study β-catenin function in stem cell fate decisions during development and regeneration'
        ]
    },
    'Surf1': {
        'questions': [
            'How does SURF1 specifically facilitate cytochrome c oxidase assembly and what is its role in complex IV biogenesis?',
            'What are the molecular consequences of SURF1 deficiency that lead to Leigh syndrome and mitochondrial dysfunction?',
            'How does SURF1 interact with other assembly factors and chaperones during respiratory complex formation?',
            'What determines the tissue-specific sensitivity to SURF1 deficiency and why are some organs more affected?'
        ],
        'experiments': [
            'Cryo-EM analysis of mitochondrial respiratory complexes in SURF1-deficient cells to visualize assembly defects',
            'Blue native PAGE and mass spectrometry to characterize respiratory complex assembly intermediates in SURF1 mutants',
            'Metabolomics analysis of SURF1-deficient tissues to understand the consequences of respiratory chain dysfunction',
            'Live-cell imaging of mitochondrial dynamics and bioenergetics in SURF1 knockout cells using fluorescent indicators'
        ]
    },

    # Rat genes
    'Prkaa2': {
        'questions': [
            'How do the α1 and α2 subunits of AMPK differ in their tissue distribution, regulation, and substrate specificity?',
            'What determines the subcellular localization of PRKAA2-containing AMPK complexes and how does this affect their function?',
            'How does PRKAA2 contribute to metabolic sensing and energy homeostasis in different physiological conditions?',
            'What role does PRKAA2 play in cellular stress responses beyond its canonical metabolic functions?'
        ],
        'experiments': [
            'Proteomics analysis to identify PRKAA2-specific substrates and interacting partners compared to PRKAA1',
            'Live-cell imaging using FRET-based biosensors to monitor PRKAA2-containing AMPK activity in real-time',
            'Metabolomics analysis of tissues from PRKAA2 knockout mice to understand metabolic pathway alterations',
            'Single-cell analysis of AMPK activity and metabolic state in different cell types using genetically encoded indicators'
        ]
    },
    'Rgn': {
        'questions': [
            'How does regucalcin regulate intracellular calcium homeostasis and what are its tissue-specific functions?',
            'What determines the nuclear versus cytoplasmic distribution of regucalcin and how does this affect its function?',
            'How does regucalcin interact with calcium-binding proteins and calcium channels to modulate cellular calcium?',
            'What role does regucalcin play in aging and cellular senescence, and how is its expression regulated?'
        ],
        'experiments': [
            'Live-cell calcium imaging to study the effects of regucalcin on calcium dynamics in different cell types',
            'Proteomics analysis to identify regucalcin interacting partners and calcium-dependent protein interactions',
            'Subcellular fractionation and imaging to determine regucalcin localization and translocation during calcium signaling',
            'Analysis of regucalcin expression and function during aging using longitudinal studies in animal models'
        ]
    },

    # Fly genes
    'Dscam1': {
        'questions': [
            'How does alternative splicing generate the extraordinary diversity of DSCAM1 isoforms and what regulates this process?',
            'What molecular mechanisms ensure self-avoidance in neuronal dendrites through DSCAM1 homophilic repulsion?',
            'How do different DSCAM1 isoforms contribute to synaptic specificity and neural circuit formation?',
            'What role does DSCAM1 play in axon guidance beyond self-avoidance and how does it integrate with other guidance cues?'
        ],
        'experiments': [
            'Single-cell RNA sequencing of developing neurons to map DSCAM1 isoform expression and splicing patterns',
            'Live imaging of dendritic development in DSCAM1 mutants to study self-avoidance and branching patterns',
            'Structural biology approaches to understand the molecular basis of DSCAM1 isoform-specific recognition',
            'Optogenetic manipulation of DSCAM1 expression to study its role in activity-dependent circuit refinement'
        ]
    },
    'CG6051': {
        'questions': [
            'What is the molecular function of CG6051 and how does it contribute to Drosophila development?',
            'How is CG6051 expression regulated during development and what signaling pathways control its activity?',
            'What are the downstream targets and cellular processes regulated by CG6051?',
            'How does CG6051 function compare to its orthologs in other organisms?'
        ],
        'experiments': [
            'RNA-seq analysis of CG6051 mutant flies to identify transcriptional targets and affected pathways',
            'Proteomics approaches to identify CG6051 interacting partners and protein complexes',
            'Developmental analysis using immunostaining to determine CG6051 expression patterns and subcellular localization',
            'Functional complementation studies with orthologs from other species to identify conserved functions'
        ]
    },
    'sws': {
        'questions': [
            'How does swiss cheese regulate membrane composition and what specific lipids does it target?',
            'What is the molecular basis of neurodegeneration in swiss cheese mutants and how does lipid metabolism affect neuronal function?',
            'How does swiss cheese coordinate with other enzymes in phospholipid metabolism and membrane remodeling?',
            'What role does swiss cheese play in synaptic function and how do membrane composition changes affect neurotransmission?'
        ],
        'experiments': [
            'Lipidomics analysis of swiss cheese mutant flies to characterize membrane lipid composition changes',
            'Electron microscopy analysis of synaptic ultrastructure in swiss cheese mutants',
            'Electrophysiological recording from swiss cheese mutant neuromuscular junctions to assess synaptic function',
            'Biochemical characterization of swiss cheese enzymatic activity and substrate specificity'
        ]
    },

    # Worm genes
    'lrx-1': {
        'questions': [
            'How does LRX-1 regulate left-right asymmetry in C. elegans and what are its downstream targets?',
            'What determines the asymmetric expression pattern of LRX-1 and how is this established during development?',
            'How does LRX-1 interact with other transcription factors to control cell fate specification?',
            'What role does LRX-1 play in maintaining versus establishing asymmetric gene expression?'
        ],
        'experiments': [
            'Single-cell RNA sequencing of developing C. elegans embryos to map LRX-1 expression and target genes',
            'ChIP-seq analysis to identify direct LRX-1 binding sites across the genome',
            'Live imaging of LRX-1 expression during embryogenesis using fluorescent reporter constructs',
            'Functional analysis of LRX-1 binding site mutations to determine the cis-regulatory logic of asymmetric expression'
        ]
    },

    # Fungal genes
    'XYL1': {
        'questions': [
            'How does XYL1 contribute to xylose metabolism and what determines its substrate specificity?',
            'What are the regulatory mechanisms that control XYL1 expression in response to different carbon sources?',
            'How does XYL1 function in the broader context of lignocellulosic biomass degradation?',
            'What role does XYL1 play in fungal adaptation to different environmental conditions?'
        ],
        'experiments': [
            'Enzyme kinetics analysis to characterize XYL1 substrate specificity and catalytic parameters',
            'RNA-seq analysis of XYL1-deficient strains grown on different carbon sources to identify metabolic pathway alterations',
            'Structural biology approaches to determine the molecular basis of XYL1 enzymatic activity',
            'Metabolomics analysis to study xylose metabolism pathways in wild-type versus XYL1 mutant strains'
        ]
    },
    'cbh1': {
        'questions': [
            'How does CBH1 achieve processivity in cellulose degradation and what determines its substrate specificity?',
            'What are the structural features that allow CBH1 to function efficiently on crystalline cellulose?',
            'How is CBH1 expression and secretion regulated in response to cellulose availability?',
            'What role does CBH1 play in fungal ecology and lignocellulose decomposition in natural environments?'
        ],
        'experiments': [
            'Single-molecule biophysics to study CBH1 processivity and movement on cellulose surfaces',
            'Cryo-EM structural analysis of CBH1 in complex with cellulose substrates',
            'Proteomics analysis of the cellulase secretome to understand CBH1 regulation and co-expression with other enzymes',
            'Environmental metagenomics to study CBH1 function and expression in natural lignocellulose-degrading communities'
        ]
    },
    'aatA': {
        'questions': [
            'How does AatA contribute to amino acid metabolism and what determines its substrate specificity?',
            'What role does AatA play in nitrogen metabolism and how is it regulated by nitrogen availability?',
            'How does AatA function in different growth conditions and stress responses?',
            'What are the evolutionary relationships of AatA with similar enzymes in other fungi?'
        ],
        'experiments': [
            'Enzyme kinetics analysis to characterize AatA substrate range and catalytic properties',
            'Metabolomics analysis of AatA mutant strains to understand amino acid metabolism alterations',
            'RNA-seq analysis under different nitrogen conditions to study AatA regulation',
            'Structural determination of AatA to understand the molecular basis of its enzymatic activity'
        ]
    },

    # Plant genes
    'APO1': {
        'questions': [
            'How does APO1 regulate apomixis and what are the molecular mechanisms that bypass sexual reproduction?',
            'What determines the tissue-specific expression of APO1 in reproductive organs?',
            'How does APO1 interact with other genes in the apomixis pathway to control reproductive mode?',
            'What role does APO1 play in plant evolution and the maintenance of hybrid vigor?'
        ],
        'experiments': [
            'Single-cell RNA sequencing of developing ovules to map APO1 expression during reproduction',
            'CRISPR-Cas9 knockout studies to analyze APO1 function in apomictic versus sexual reproduction',
            'Comparative genomics analysis to study APO1 evolution across different plant species',
            'Live imaging of reproductive development in APO1 mutants using confocal microscopy'
        ]
    },
    'WIN6.2C': {
        'questions': [
            'How does WIN6.2C contribute to plant defense responses and pathogen resistance?',
            'What determines the specificity of WIN6.2C recognition by different pathogen effectors?',
            'How is WIN6.2C expression regulated during pathogen infection and stress responses?',
            'What role does WIN6.2C play in the broader plant immune system and resistance gene networks?'
        ],
        'experiments': [
            'Pathogen infection assays to study WIN6.2C function in disease resistance',
            'Protein-protein interaction studies to identify WIN6.2C binding partners and downstream signaling components',
            'RNA-seq analysis during pathogen infection to study WIN6.2C-dependent transcriptional responses',
            'Structural biology approaches to understand WIN6.2C protein structure and function'
        ]
    },
    'LCI5': {
        'questions': [
            'How does LCI5 contribute to CO2 concentrating mechanisms in Chlamydomonas photosynthesis?',
            'What determines the subcellular localization of LCI5 and how does this affect its function?',
            'How is LCI5 expression regulated in response to CO2 availability and light conditions?',
            'What role does LCI5 play in algal adaptation to different environmental carbon conditions?'
        ],
        'experiments': [
            'Photosynthetic measurements in LCI5 mutant strains to assess CO2 concentrating mechanism function',
            'Subcellular localization studies using fluorescent protein fusions to determine LCI5 distribution',
            'RNA-seq analysis under different CO2 conditions to study LCI5 regulation and downstream targets',
            'Proteomics analysis of carbon concentrating mechanism components to understand LCI5 protein interactions'
        ]
    },

    # Other organisms
    'aldh1a2': {
        'questions': [
            'How does ALDH1A2 control retinoic acid synthesis during Xenopus development?',
            'What determines the tissue-specific expression patterns of ALDH1A2 during embryogenesis?',
            'How do different ALDH1A2 activity levels affect anterior-posterior and dorsal-ventral patterning?',
            'What role does ALDH1A2 play in neural crest cell development and migration?'
        ],
        'experiments': [
            'In situ hybridization and immunostaining to map ALDH1A2 expression during Xenopus development',
            'Morpholino knockdown experiments to study ALDH1A2 function in embryonic patterning',
            'Retinoic acid level measurements in ALDH1A2-deficient embryos using LC-MS/MS',
            'Time-lapse imaging of neural crest cell migration in ALDH1A2 morphants'
        ]
    },
    'trpm7': {
        'questions': [
            'How does TRPM7 integrate mechanosensing with magnesium homeostasis in zebrafish development?',
            'What determines the tissue-specific requirements for TRPM7 kinase versus channel activity?',
            'How does TRPM7 regulate cell migration and morphogenesis during gastrulation and organogenesis?',
            'What role does TRPM7 play in left-right asymmetry establishment in the zebrafish embryo?'
        ],
        'experiments': [
            'Electrophysiological analysis of TRPM7 channel properties in different zebrafish cell types',
            'Live imaging of cell migration during gastrulation in TRPM7 mutant embryos',
            'Magnesium imaging using fluorescent indicators to study TRPM7 function in ion homeostasis',
            'Analysis of left-right patterning genes in TRPM7 mutant embryos using whole-mount in situ hybridization'
        ]
    },
    'Agaphelin': {
        'questions': [
            'How does Agaphelin function as an anticoagulant and what determines its specificity for different clotting factors?',
            'What role does Agaphelin play in mosquito feeding and how does it facilitate blood meal acquisition?',
            'How has Agaphelin evolved to evade host immune responses and maintain anticoagulant activity?',
            'What are the structural determinants that allow Agaphelin to inhibit blood coagulation?'
        ],
        'experiments': [
            'Coagulation assays to characterize Agaphelin anticoagulant activity and factor specificity',
            'Structural biology approaches to determine Agaphelin three-dimensional structure and binding sites',
            'Feeding behavior analysis in mosquitoes with altered Agaphelin expression',
            'Evolutionary analysis of Agaphelin sequences across different mosquito species'
        ]
    },
    'fibrolase': {
        'questions': [
            'How does fibrolase achieve substrate specificity for fibrin and other extracellular matrix proteins?',
            'What role does fibrolase play in venom composition and prey immobilization?',
            'How has fibrolase evolved to optimize its proteolytic activity in different environmental conditions?',
            'What are the structural features that determine fibrolase enzymatic activity and stability?'
        ],
        'experiments': [
            'Enzyme kinetics analysis to characterize fibrolase substrate specificity and catalytic parameters',
            'Structural determination using X-ray crystallography to understand the molecular basis of fibrolase activity',
            'Venom composition analysis to study fibrolase expression and co-expressed proteins',
            'Phylogenetic analysis of fibrolase evolution across different snake species'
        ]
    },

    # Additional yeast/pombe genes
    'Epe1': {
        'questions': [
            'How does Epe1 regulate heterochromatin formation and maintenance at centromeres and telomeres?',
            'What determines the specificity of Epe1 for different chromatin modifications and histone variants?',
            'How does Epe1 coordinate with other chromatin remodeling factors during cell cycle progression?',
            'What role does Epe1 play in epigenetic inheritance and chromatin stability across generations?'
        ],
        'experiments': [
            'ChIP-seq analysis to map Epe1 binding sites across the genome and correlate with chromatin modifications',
            'Live-cell imaging of fluorescently tagged Epe1 to study its dynamics during the cell cycle',
            'Genetic screens to identify Epe1 interacting factors and chromatin regulators',
            'Single-cell analysis of heterochromatin inheritance in Epe1 mutant cells'
        ]
    },
    'Shu1': {
        'questions': [
            'How does Shu1 contribute to homologous recombination and DNA repair pathway choice?',
            'What determines the recruitment of Shu1 to sites of DNA damage and replication stress?',
            'How does Shu1 interact with other recombination factors to promote error-free repair?',
            'What role does Shu1 play in preventing genome instability during DNA replication?'
        ],
        'experiments': [
            'Live-cell imaging of Shu1-GFP to study its dynamics at sites of DNA damage',
            'Genetic analysis of DNA repair pathway usage in Shu1 mutant cells',
            'Proteomics analysis to identify Shu1 interacting partners during DNA repair',
            'Single-molecule biophysics to study Shu1 function in homologous recombination'
        ]
    },
    'tam10': {
        'questions': [
            'How does tam10 regulate meiotic progression and what specific processes does it control?',
            'What determines the meiosis-specific expression and function of tam10?',
            'How does tam10 interact with other meiotic regulators to ensure proper chromosome segregation?',
            'What role does tam10 play in meiotic quality control and error prevention?'
        ],
        'experiments': [
            'Live-cell imaging during meiosis to study tam10 localization and dynamics',
            'RNA-seq analysis of meiotic cells to identify tam10-dependent gene expression programs',
            'Cytological analysis of chromosome behavior in tam10 mutant meioses',
            'Proteomics analysis to identify tam10 interacting partners during meiotic progression'
        ]
    },
    'ura7': {
        'questions': [
            'How does ura7 contribute to pyrimidine biosynthesis and what determines its enzymatic specificity?',
            'What are the regulatory mechanisms that control ura7 expression in response to pyrimidine availability?',
            'How does ura7 function in the broader context of nucleotide metabolism and cellular growth?',
            'What role does ura7 play in cellular responses to nucleotide stress and starvation?'
        ],
        'experiments': [
            'Enzyme kinetics analysis to characterize ura7 catalytic properties and substrate specificity',
            'Metabolomics analysis of ura7 mutant strains to study pyrimidine metabolism alterations',
            'RNA-seq analysis under different nucleotide conditions to study ura7 regulation',
            'Growth analysis of ura7 mutants in different media to assess metabolic requirements'
        ]
    }
}

def add_suggestions_to_file(filepath, gene_name):
    """Add suggested questions and experiments to a gene review file."""
    if gene_name not in GENE_SUGGESTIONS:
        print(f"No suggestions defined for {gene_name}")
        return False
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if suggestions already exist
        if 'suggested_questions:' in content or 'suggested_experiments:' in content:
            print(f"Suggestions already exist in {filepath}")
            return False
        
        # Add suggestions at the end
        suggestions = GENE_SUGGESTIONS[gene_name]
        
        suggestion_text = "\nsuggested_questions:\n"
        for q in suggestions['questions']:
            suggestion_text += f"- question: {q}\n"
        
        suggestion_text += "suggested_experiments:\n"
        for e in suggestions['experiments']:
            suggestion_text += f"- experiment: {e}\n"
        
        # Append to file
        with open(filepath, 'a') as f:
            f.write(suggestion_text)
        
        print(f"Added suggestions to {filepath}")
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all gene review files."""
    base_path = Path("/Users/cjm/repos/ai-gene-review/genes")
    
    # Find all gene review files
    for yaml_file in base_path.rglob("*-ai-review.yaml"):
        # Extract gene name from filename
        gene_name = yaml_file.stem.replace('-ai-review', '')
        print(f"Processing {gene_name}...")
        add_suggestions_to_file(yaml_file, gene_name)

if __name__ == "__main__":
    main()