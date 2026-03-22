# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:27 PM*

---

**Organism:** Caenorhabditis elegans

### Thinking Trace
I begin with the InterPro architecture and its order along the polypeptide. The N-terminal ectodomain is dominated by IPR036941 (Receptor L-domain superfamily, residues 169–655) that houses IPR000494 (Receptor L-domain, residues 180–625). This tandem L-domain scaffold is characteristic of ligand-binding modules in receptor tyrosine kinases, creating a curved beta-sandwich surface that captures extracellular growth-factor-like ligands. Embedded within this ectodomain lies a cysteine-rich segment: IPR009030 (Growth factor receptor cysteine-rich domain superfamily, residues 342–494) and its core IPR006211 (Furin-like cysteine-rich domain, residues 347–495). This cysteine-rich module stabilizes the ectodomain and often participates in ligand-induced dimerization. Following the L-domain, the ectodomain transitions into an Ig-like/FnIII-rich stalk: IPR036116 (Fibronectin type III superfamily, residues 651–1174), IPR013783 (Immunoglobulin-like fold superfamily, residues 656–1178), and a concrete IPR003961 (Fibronectin type III, residues 775–1179). This elongated scaffold positions the extracellular sensor above the membrane and supports avid ligand engagement and receptor clustering.

The intracellular region is built around a canonical tyrosine kinase engine. Multiple overlapping signatures define a bilobal kinase core: IPR011009 (Protein kinase-like domain superfamily, residues 1228–1519), IPR020635 (Tyrosine-protein kinase, catalytic domain, residues 1246–1520), IPR000719 (Protein kinase domain, residues 1246–1528), and IPR001245 (Serine-threonine/tyrosine-protein kinase, catalytic domain, residues 1248–1519). The presence of IPR008266 (Tyrosine-protein kinase, active site, residues 1384–1396) marks the catalytic machinery that binds ATP and transfers phosphate to tyrosine residues. The global family assignment IPR050122 (Receptor Tyrosine Kinase, residues 712–1521) ties the extracellular sensing apparatus to the intracellular tyrosine kinase, defining a single-pass type I receptor tyrosine kinase whose activation proceeds via ligand-induced dimerization and trans-autophosphorylation.

This architecture causally specifies molecular function. The extracellular L-domain and cysteine-rich module capture growth-factor-like ligands and promote receptor dimerization; the intracellular TK catalytic core then executes ATP-dependent phosphotransfer onto tyrosines. These features necessitate GO:0004714 receptor tyrosine kinase activity and GO:0005524 ATP binding, with the kinase signatures explaining ATP engagement and tyrosine specificity. The FnIII/Ig-like stalk further supports high-avidity clustering that enhances autophosphorylation.

From this molecular function, the biological process follows. Ligand-triggered dimerization and kinase activation propagate signals through phosphorylated docking sites to downstream pathways, defining a transmembrane receptor protein tyrosine kinase signaling pathway. Thus, the most precise process inference is a transmembrane receptor protein tyrosine kinase signaling pathway, with broader placement in cell surface receptor signaling and growth control circuits. In metazoans, such pathways regulate proliferation, differentiation, and migration; in C. elegans, this logic predicts developmental and stress-responsive signaling hubs.

The cellular component is dictated by the single-pass type I topology and receptor function. The presence of a large extracellular ectodomain, a single transmembrane segment (implied between the stalk and kinase), and a cytosolic kinase domain constrains localization to the plasma membrane as an integral membrane component. This aligns with a membrane-resident signaling platform that surveys the extracellular milieu and transduces intracellular signals.

Mechanistically, I hypothesize that extracellular ligand binding to the L-domain/cysteine-rich module induces receptor dimerization and rearrangement of the FnIII stalk, which positions intracellular kinase domains for trans-autophosphorylation. Newly formed phosphotyrosine motifs recruit SH2/PTB-containing adaptors that assemble signaling complexes. Likely partners include extracellular growth-factor-like ligands and heparan sulfate proteoglycans that stabilize receptor clustering; intracellularly, SH2-domain adaptors and scaffolds would couple to MAPK and PI3K cascades. In C. elegans, this suggests associations with SH2/SH3 adaptors and Ras/MAPK pathway components at the plasma membrane to coordinate organismal growth and patterning.

### Functional Summary
A single-pass membrane receptor that presents a large extracellular ligand-binding scaffold and an intracellular tyrosine kinase engine. Ligand engagement at the ectodomain drives receptor clustering and trans-autophosphorylation, which in turn initiates intracellular signaling cascades that regulate growth and developmental programs at the cell surface. The protein resides at the plasma membrane as an integral membrane component and signals through ATP-dependent phosphotransfer to orchestrate downstream pathways characteristic of receptor tyrosine kinase systems.

### UniProt Summary
Tyrosine-protein kinase receptor whose ligand is unknown.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0005488
Binding
GO:0005515
Protein Binding
GO:0019904
Protein Domain Specific Binding
GO:0019899
Enzyme Binding
GO:0019900
Kinase Binding
GO:0042169
SH2 Domain Binding
GO:0019901
Protein Kinase Binding
Biological Process
GO:0008150
Biological_process
GO:0051179
Localization
GO:0048518
Positive Regulation Of Biological Process
GO:0050789
Regulation Of Biological Process
GO:0000003
Reproduction
GO:0032501
Multicellular Organismal Process
GO:0065007
Biological Regulation
GO:0050896
Response To Stimulus
GO:0032502
Developmental Process
GO:0009987
Cellular Process
GO:0048519
Negative Regulation Of Biological Process
GO:1905953
Negative Regulation Of Lipid Localization
GO:0051641
Cellular Localization
GO:0048856
Anatomical Structure Development
GO:0022611
Dormancy Process
GO:0042221
Response To Chemical
GO:0051240
Positive Regulation Of Multicellular Organismal Process
GO:0051241
Negative Regulation Of Multicellular Organismal Process
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0045927
Positive Regulation Of Growth
GO:0009791
Post-Embryonic Development
GO:0009892
Negative Regulation Of Metabolic Process
GO:0050793
Regulation Of Developmental Process
GO:0065008
Regulation Of Biological Quality
GO:0050794
Regulation Of Cellular Process
GO:0048583
Regulation Of Response To Stimulus
GO:0051716
Cellular Response To Stimulus
GO:0023051
Regulation Of Signaling
GO:0051093
Negative Regulation Of Developmental Process
GO:0048523
Negative Regulation Of Cellular Process
GO:0009628
Response To Abiotic Stimulus
GO:0023056
Positive Regulation Of Signaling
GO:0007275
Multicellular Organism Development
GO:0008340
Determination Of Adult Lifespan
GO:0019222
Regulation Of Metabolic Process
GO:0032879
Regulation Of Localization
GO:0051234
Establishment Of Localization
GO:0033036
Macromolecule Localization
GO:0009893
Positive Regulation Of Metabolic Process
GO:0006950
Response To Stress
GO:0051094
Positive Regulation Of Developmental Process
GO:0040008
Regulation Of Growth
GO:0007610
Behavior
GO:0048522
Positive Regulation Of Cellular Process
GO:0009266
Response To Temperature Stimulus
GO:0009314
Response To Radiation
GO:1903828
Negative Regulation Of Protein Localization
GO:0080134
Regulation Of Response To Stress
GO:0007631
Feeding Behavior
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0010883
Regulation Of Lipid Storage
GO:0050803
Regulation Of Synapse Structure Or Activity
GO:0030537
Larval Behavior
GO:0044089
Positive Regulation Of Cellular Component Biogenesis
GO:0045184
Establishment Of Protein Localization
GO:0044087
Regulation Of Cellular Component Biogenesis
GO:0009408
Response To Heat
GO:0009894
Regulation Of Catabolic Process
GO:0048580
Regulation Of Post-Embryonic Development
GO:0040034
Regulation Of Development, Heterochronic
GO:0046907
Intracellular Transport
GO:0050806
Positive Regulation Of Synaptic Transmission
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0002164
Larval Development
GO:0051128
Regulation Of Cellular Component Organization
GO:0051962
Positive Regulation Of Nervous System Development
GO:0048638
Regulation Of Developmental Growth
GO:1902074
Response To Salt
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0010888
Negative Regulation Of Lipid Storage
GO:0048639
Positive Regulation Of Developmental Growth
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0006979
Response To Oxidative Stress
GO:1905952
Regulation Of Lipid Localization
GO:0060341
Regulation Of Cellular Localization
GO:0051649
Establishment Of Localization In Cell
GO:0051130
Positive Regulation Of Cellular Component Organization
GO:0031324
Negative Regulation Of Cellular Metabolic Process
GO:0009891
Positive Regulation Of Biosynthetic Process
GO:2000026
Regulation Of Multicellular Organismal Development
GO:0040018
Positive Regulation Of Multicellular Organism Growth
GO:0040014
Regulation Of Multicellular Organism Growth
GO:0031325
Positive Regulation Of Cellular Metabolic Process
GO:0010646
Regulation Of Cell Communication
GO:0070887
Cellular Response To Chemical Stimulus
GO:0006810
Transport
GO:0009889
Regulation Of Biosynthetic Process
GO:0070727
Cellular Macromolecule Localization
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0010647
Positive Regulation Of Cell Communication
GO:0009895
Negative Regulation Of Catabolic Process
GO:0099177
Regulation Of Trans-Synaptic Signaling
GO:0080090
Regulation Of Primary Metabolic Process
GO:0050795
Regulation Of Behavior
GO:0048581
Negative Regulation Of Post-Embryonic Development
GO:0061062
Regulation Of Nematode Larval Development
GO:0071705
Nitrogen Compound Transport
GO:0050807
Regulation Of Synapse Organization
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0051246
Regulation Of Protein Metabolic Process
GO:0031330
Negative Regulation Of Cellular Catabolic Process
GO:1902075
Cellular Response To Salt
GO:0071702
Organic Substance Transport
GO:0051169
Nuclear Transport
GO:0010468
Regulation Of Gene Expression
GO:0006886
Intracellular Protein Transport
GO:1900181
Negative Regulation Of Protein Localization To Nucleus
GO:0015031
Protein Transport
GO:1902882
Regulation Of Response To Oxidative Stress
GO:0060259
Regulation Of Feeding Behavior
GO:0008582
Regulation Of Synaptic Assembly At Neuromuscular Junction
GO:0051252
Regulation Of RNA Metabolic Process
GO:0010629
Negative Regulation Of Gene Expression
GO:1901890
Positive Regulation Of Cell Junction Assembly
GO:0009416
Response To Light Stimulus
GO:0042177
Negative Regulation Of Protein Catabolic Process
GO:0042176
Regulation Of Protein Catabolic Process
GO:1901888
Regulation Of Cell Junction Assembly
GO:0072594
Establishment Of Protein Localization To Organelle
GO:0051248
Negative Regulation Of Protein Metabolic Process
GO:0050804
Modulation Of Chemical Synaptic Transmission
GO:0010628
Positive Regulation Of Gene Expression
GO:0032880
Regulation Of Protein Localization
GO:0051960
Regulation Of Nervous System Development
GO:1902115
Regulation Of Organelle Assembly
GO:1904398
Positive Regulation Of Neuromuscular Junction Development
GO:0010557
Positive Regulation Of Macromolecule Biosynthetic Process
GO:0045935
Positive Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0051254
Positive Regulation Of RNA Metabolic Process
GO:0061064
Negative Regulation Of Nematode Larval Development
GO:0051965
Positive Regulation Of Synapse Assembly
GO:0010286
Heat Acclimation
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:0030536
Larval Feeding Behavior
GO:0019219
Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0033043
Regulation Of Organelle Organization
GO:0045887
Positive Regulation Of Synaptic Assembly At Neuromuscular Junction
GO:0008104
Protein Localization
GO:0031329
Regulation Of Cellular Catabolic Process
GO:0002119
Nematode Larval Development
GO:0031328
Positive Regulation Of Cellular Biosynthetic Process
GO:0006606
Protein Import Into Nucleus
GO:0030162
Regulation Of Proteolysis
GO:0044088
Regulation Of Vacuole Organization
GO:2000785
Regulation Of Autophagosome Assembly
GO:1901799
Negative Regulation Of Proteasomal Protein Catabolic Process
GO:2001141
Regulation Of RNA Biosynthetic Process
GO:1901031
Regulation Of Response To Reactive Oxygen Species
GO:1904396
Regulation Of Neuromuscular Junction Development
GO:0051963
Regulation Of Synapse Assembly
GO:0061065
Regulation Of Dauer Larval Development
GO:0009411
Response To UV
GO:1902680
Positive Regulation Of RNA Biosynthetic Process
GO:0040024
Dauer Larval Development
GO:2000059
Negative Regulation Of Ubiquitin-Dependent Protein Catabolic Process
GO:1900180
Regulation Of Protein Localization To Nucleus
GO:2000058
Regulation Of Ubiquitin-Dependent Protein Catabolic Process
GO:0006913
Nucleocytoplasmic Transport
GO:0033365
Protein Localization To Organelle
GO:0006355
Regulation Of DNA-Templated Transcription
GO:1900073
Regulation Of Neuromuscular Synaptic Transmission
GO:1903998
Regulation Of Eating Behavior
GO:0061136
Regulation Of Proteasomal Protein Catabolic Process
GO:0045861
Negative Regulation Of Proteolysis
GO:0061067
Negative Regulation Of Dauer Larval Development
GO:0034504
Protein Localization To Nucleus
GO:0051170
Import Into Nucleus
GO:0032435
Negative Regulation Of Proteasomal Ubiquitin-Dependent Protein Catabolic Process
GO:1903051
Negative Regulation Of Proteolysis Involved In Protein Catabolic Process
GO:1903508
Positive Regulation Of Nucleic Acid-Templated Transcription
GO:1903506
Regulation Of Nucleic Acid-Templated Transcription
GO:0006357
Regulation Of Transcription By RNA Polymerase II
GO:0045893
Positive Regulation Of DNA-Templated Transcription
GO:0032434
Regulation Of Proteasomal Ubiquitin-Dependent Protein Catabolic Process
GO:1903050
Regulation Of Proteolysis Involved In Protein Catabolic Process
GO:0045944
Positive Regulation Of Transcription By RNA Polymerase II
Cellular Component
GO:0005575
Cellular_component
GO:0110165
Cellular Anatomical Entity
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0042995
Cell Projection
GO:0016020
Membrane
GO:0044297
Cell Body
GO:0036477
Somatodendritic Compartment
GO:0005737
Cytoplasm
GO:0071944
Cell Periphery
GO:0043025
Neuronal Cell Body
GO:0120025
Plasma Membrane Bounded Cell Projection
GO:0031410
Cytoplasmic Vesicle
GO:0043229
Intracellular Organelle
GO:0043227
Membrane-Bounded Organelle
GO:0005886
Plasma Membrane
GO:0043005
Neuron Projection
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0005929
Cilium
GO:0031982
Vesicle
GO:0030424
Axon
GO:0097708
Intracellular Vesicle
GO:0097730
Non-Motile Cilium

### InterPro Domains
1
1846
IPR036941
IPR000494
IPR009030
IPR006211
IPR036116
IPR013783
IPR050122
IPR003961
IPR011009
IPR020635
IPR000719
IPR001245
IPR008266
Domain Details
IPR036941
Receptor L-domain superfamily (homologous_superfamily) [169-655]
IPR000494
Receptor L-domain (domain) [180-625]
IPR009030
Growth factor receptor cysteine-rich domain superfamily (homologous_superfamily) [342-494]
IPR006211
Furin-like cysteine-rich domain (domain) [347-495]
IPR036116
Fibronectin type III superfamily (homologous_superfamily) [651-1174]
IPR013783
Immunoglobulin-like fold (homologous_superfamily) [656-1178]
IPR050122
Receptor Tyrosine Kinase (family) [712-1521]
IPR003961
Fibronectin type III (domain) [775-1179]
IPR011009
Protein kinase-like domain superfamily (homologous_superfamily) [1228-1519]
IPR020635
Tyrosine-protein kinase, catalytic domain (domain) [1246-1520]
IPR000719
Protein kinase domain (domain) [1246-1528]
IPR001245
Serine-threonine/tyrosine-protein kinase, catalytic domain (domain) [1248-1519]
IPR008266
Tyrosine-protein kinase, active site (active_site) [1384-1396]

---
*Generated by [BioReason](https://bioreason.net)*
