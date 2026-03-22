# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:18 PM*

---

**Organism:** Mus musculus

### Thinking Trace
I begin by examining the InterPro architecture and its order along the polypeptide. The N-terminus (residues 1–123) is assigned to IPR011993 (PH-like domain superfamily), with tighter mapping of a canonical pleckstrin homology module by IPR039026 (Protein Kinase B, pleckstrin homology domain, residues 4–111) and IPR001849 (Pleckstrin homology domain, residues 5–110). This tandem PH/PH-like configuration dictates high-affinity recognition of phosphoinositide headgroups—particularly phosphatidylinositol 3,4,5-trisphosphate—driving membrane recruitment and allosteric activation. Immediately following, the core kinase region is defined by IPR034676 (Protein kinase B alpha, catalytic domain, residues 124–479), with its catalytic heart captured by IPR011009 (Protein kinase-like domain superfamily, residues 145–459) and IPR000719 (Protein kinase domain, residues 150–408). The nucleotide- and chemistry-defining features are specified by IPR017441 (Protein kinase, ATP binding site, residues 156–189) and IPR008271 (Serine/threonine-protein kinase, active site, residues 270–282), which together cause ATP-dependent transfer of phosphate to serine/threonine residues. The C-terminal regulatory tail is characteristic of AGC kinases and is annotated by IPR000961 (AGC-kinase, C-terminal, residues 409–480) and IPR017892 (Protein kinase, C-terminal, residues 429–474). This tail mediates docking and phosphorylation-dependent stabilization, completing the canonical AGC kinase architecture: N-terminal PH domain for membrane targeting, central catalytic core for phosphotransfer, and AGC C-tail for maturation and substrate selection.

From this architecture, the molecular function resolves as a phosphatidylinositol 3-kinase–dependent agc-family serine/threonine kinase. The PH module enforces lipid-gated activation; the kinase core binds ATP and catalyzes phosphate transfer; and the AGC tail enforces proper activation loop and hydrophobic motif regulation. These features specify GO:0004674 protein serine/threonine kinase activity and GO:0005524 ATP binding.

The biological process follows causally from lipid-gated kinase signaling. PH-domain–driven recruitment to PI3K-generated phosphoinositides positions the enzyme downstream of PI3K signaling cascades, where it phosphorylates effectors controlling metabolism and survival. Thus, it executes GO:0014065 phosphatidylinositol 3-kinase signaling and broadly modulates GO:0006468 protein phosphorylation–driven pathways that coordinate cell cycle progression, survival, and migration.

Cellular location emerges from the same logic. The PH domain drives transient membrane association at signaling sites, but the soluble catalytic and regulatory modules support a cytosolic pool that cycles on and off membranes. This dynamic balance supports localization to the cytoplasm, consistent with GO:0005737 cytoplasm.

Mechanistically, membrane-proximal activation via phosphoinositide binding unmasks the kinase active site and stabilizes the AGC C-terminal tail, enabling a maturation pathway that yields a fully active enzyme. Once active, it phosphorylates substrates such as metabolic and cytoskeletal regulators to propagate survival and motility cues. I hypothesize that it transiently complexes with PI3K pathway adaptors and modulators: phosphoinositide lipids dock the PH domain; scaffold proteins such as IRS-family adaptors and IRS-1 chaperone activity; and regulatory partners including PDPK1 (which primes AGC kinases), mTORC2 components (which supply hydrophobic motif phosphorylation), and endogenous inhibitors such as AKT1-S6K-binding proteins and 14-3-3 proteins that tune cytosolic signaling assemblies. Together, these interactions channel signals from lipid second messengers to phosphorylation circuits that control growth and migration programs.

### Functional Summary
A cytoplasmic, lipid-gated serine/threonine kinase that is activated downstream of phosphoinositide production and then propagates growth and survival signals by phosphorylating diverse cytosolic substrates. Its N-terminal lipid-recognition module drives transient membrane recruitment and allosteric activation, the central catalytic core transfers phosphate from ATP to serine/threonine residues, and the C-terminal regulatory tail stabilizes the active state characteristic of AGC kinases. Through this architecture, it coordinates signaling pathways that govern cell cycle progression, survival, and migration within cytoplasmic networks.

### UniProt Summary
Acts downstream of PI3 kinase in the regulation of diverse cellular functions related to cell growth, survival, proliferation, migration and differentiation.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0005488
Binding
GO:0003824
Catalytic Activity
GO:0016740
Transferase Activity
GO:0140096
Catalytic Activity, Acting On A Protein
GO:0005515
Protein Binding
GO:0016772
Transferase Activity, Transferring Phosphorus-Containing Groups
GO:0004672
Protein Kinase Activity
GO:0019899
Enzyme Binding
GO:0004674
Protein Serine/Threonine Kinase Activity
GO:0016301
Kinase Activity
GO:0016773
Phosphotransferase Activity, Alcohol Group As Acceptor
GO:0019900
Kinase Binding
GO:0019901
Protein Kinase Binding
Biological Process
GO:0008150
Biological_process
GO:0023052
Signaling
GO:0065007
Biological Regulation
GO:0050896
Response To Stimulus
GO:0044419
Biological Process Involved In Interspecies Interaction Between Organisms
GO:0022414
Reproductive Process
GO:0048519
Negative Regulation Of Biological Process
GO:0048518
Positive Regulation Of Biological Process
GO:0050789
Regulation Of Biological Process
GO:0000003
Reproduction
GO:0032501
Multicellular Organismal Process
GO:0032502
Developmental Process
GO:0009987
Cellular Process
GO:0008152
Metabolic Process
GO:0042592
Homeostatic Process
GO:0019953
Sexual Reproduction
GO:0048856
Anatomical Structure Development
GO:0023057
Negative Regulation Of Signaling
GO:0051240
Positive Regulation Of Multicellular Organismal Process
GO:0071840
Cellular Component Organization Or Biogenesis
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0007272
Ensheathment Of Neurons
GO:0003006
Developmental Process Involved In Reproduction
GO:0051050
Positive Regulation Of Transport
GO:0009892
Negative Regulation Of Metabolic Process
GO:0065008
Regulation Of Biological Quality
GO:0022412
Cellular Process Involved In Reproduction In Multicellular Organism
GO:0033555
Multicellular Organismal Response To Stress
GO:0050794
Regulation Of Cellular Process
GO:0044703
Multi-Organism Reproductive Process
GO:0048583
Regulation Of Response To Stimulus
GO:0051716
Cellular Response To Stimulus
GO:0048523
Negative Regulation Of Cellular Process
GO:0040012
Regulation Of Locomotion
GO:0009628
Response To Abiotic Stimulus
GO:0048869
Cellular Developmental Process
GO:0019222
Regulation Of Metabolic Process
GO:0009056
Catabolic Process
GO:0001503
Ossification
GO:0065009
Regulation Of Molecular Function
GO:0007154
Cell Communication
GO:0048522
Positive Regulation Of Cellular Process
GO:0009605
Response To External Stimulus
GO:0042221
Response To Chemical
GO:0097194
Execution Phase Of Apoptosis
GO:0006807
Nitrogen Compound Metabolic Process
GO:0032504
Multicellular Organism Reproduction
GO:0045927
Positive Regulation Of Growth
GO:0050793
Regulation Of Developmental Process
GO:0044706
Multi-Multicellular Organism Process
GO:0009607
Response To Biotic Stimulus
GO:0009719
Response To Endogenous Stimulus
GO:0008219
Cell Death
GO:0040017
Positive Regulation Of Locomotion
GO:0023051
Regulation Of Signaling
GO:0051707
Response To Other Organism
GO:0007165
Signal Transduction
GO:0007275
Multicellular Organism Development
GO:0032879
Regulation Of Localization
GO:0071704
Organic Substance Metabolic Process
GO:0048878
Chemical Homeostasis
GO:0044237
Cellular Metabolic Process
GO:0044281
Small Molecule Metabolic Process
GO:0009893
Positive Regulation Of Metabolic Process
GO:0006950
Response To Stress
GO:0051094
Positive Regulation Of Developmental Process
GO:0048609
Multicellular Organismal Reproductive Process
GO:0048585
Negative Regulation Of Response To Stimulus
GO:0040008
Regulation Of Growth
GO:0044238
Primary Metabolic Process
GO:0007610
Behavior
GO:0051129
Negative Regulation Of Cellular Component Organization
GO:0043207
Response To External Biotic Stimulus
GO:2000145
Regulation Of Cell Motility
GO:0048513
Animal Organ Development
GO:0009966
Regulation Of Signal Transduction
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0005975
Carbohydrate Metabolic Process
GO:0060135
Maternal Process Involved In Female Pregnancy
GO:0009725
Response To Hormone
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0009790
Embryo Development
GO:0044260
Cellular Macromolecule Metabolic Process
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0007281
Germ Cell Development
GO:0050790
Regulation Of Catalytic Activity
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:1903829
Positive Regulation Of Protein Localization
GO:0008366
Axon Ensheathment
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0001568
Blood Vessel Development
GO:0044092
Negative Regulation Of Molecular Function
GO:0060341
Regulation Of Cellular Localization
GO:0019538
Protein Metabolic Process
GO:0033500
Carbohydrate Homeostasis
GO:0005996
Monosaccharide Metabolic Process
GO:1901700
Response To Oxygen-Containing Compound
GO:0048266
Behavioral Response To Pain
GO:0043170
Macromolecule Metabolic Process
GO:0071216
Cellular Response To Biotic Stimulus
GO:2000147
Positive Regulation Of Cell Motility
GO:0009891
Positive Regulation Of Biosynthetic Process
GO:0061061
Muscle Structure Development
GO:2000026
Regulation Of Multicellular Organismal Development
GO:0010941
Regulation Of Cell Death
GO:1901698
Response To Nitrogen Compound
GO:0031325
Positive Regulation Of Cellular Metabolic Process
GO:0048265
Response To Pain
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0080090
Regulation Of Primary Metabolic Process
GO:0006091
Generation Of Precursor Metabolites And Energy
GO:0009266
Response To Temperature Stimulus
GO:0009968
Negative Regulation Of Signal Transduction
GO:0012501
Programmed Cell Death
GO:0060548
Negative Regulation Of Cell Death
GO:0048468
Cell Development
GO:0030154
Cell Differentiation
GO:0044248
Cellular Catabolic Process
GO:0048731
System Development
GO:0070482
Response To Oxygen Levels
GO:0070848
Response To Growth Factor
GO:0071495
Cellular Response To Endogenous Stimulus
GO:0046620
Regulation Of Organ Growth
GO:0050803
Regulation Of Synapse Structure Or Activity
GO:0006793
Phosphorus Metabolic Process
GO:0009408
Response To Heat
GO:0009894
Regulation Of Catabolic Process
GO:0031641
Regulation Of Myelination
GO:0043270
Positive Regulation Of Monoatomic Ion Transport
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0001893
Maternal Placenta Development
GO:0016043
Cellular Component Organization
GO:0007166
Cell Surface Receptor Signaling Pathway
GO:0051128
Regulation Of Cellular Component Organization
GO:1901575
Organic Substance Catabolic Process
GO:0048638
Regulation Of Developmental Growth
GO:0044262
Cellular Carbohydrate Metabolic Process
GO:0048639
Positive Regulation Of Developmental Growth
GO:0007276
Gamete Generation
GO:0010648
Negative Regulation Of Cell Communication
GO:0051049
Regulation Of Transport
GO:1901564
Organonitrogen Compound Metabolic Process
GO:0032094
Response To Food
GO:0035556
Intracellular Signal Transduction
GO:0001649
Osteoblast Differentiation
GO:0060706
Cell Differentiation Involved In Embryonic Placenta Development
GO:0006952
Defense Response
GO:0046622
Positive Regulation Of Organ Growth
GO:0010033
Response To Organic Substance
GO:0009991
Response To Extracellular Stimulus
GO:0007565
Female Pregnancy
GO:0009888
Tissue Development
GO:0010646
Regulation Of Cell Communication
GO:0070887
Cellular Response To Chemical Stimulus
GO:0009617
Response To Bacterium
GO:0009889
Regulation Of Biosynthetic Process
GO:0060711
Labyrinthine Layer Development
GO:0009896
Positive Regulation Of Catabolic Process
GO:0097305
Response To Alcohol
GO:1901654
Response To Ketone
GO:0050807
Regulation Of Synapse Organization
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0071453
Cellular Response To Oxygen Levels
GO:0051246
Regulation Of Protein Metabolic Process
GO:0001944
Vasculature Development
GO:0032292
Peripheral Nervous System Axon Ensheathment
GO:0031663
Lipopolysaccharide-Mediated Signaling Pathway
GO:0010001
Glial Cell Differentiation
GO:2000010
Positive Regulation Of Protein Localization To Cell Surface
GO:0010468
Regulation Of Gene Expression
GO:0043412
Macromolecule Modification
GO:0042692
Muscle Cell Differentiation
GO:0072359
Circulatory System Development
GO:0036293
Response To Decreased Oxygen Levels
GO:0005976
Polysaccharide Metabolic Process
GO:0030335
Positive Regulation Of Cell Migration
GO:0015980
Energy Derivation By Oxidation Of Organic Compounds
GO:1901701
Cellular Response To Oxygen-Containing Compound
GO:0010629
Negative Regulation Of Gene Expression
GO:0071417
Cellular Response To Organonitrogen Compound
GO:0043491
Protein Kinase B Signaling
GO:0019318
Hexose Metabolic Process
GO:0032496
Response To Lipopolysaccharide
GO:0070849
Response To Epidermal Growth Factor
GO:0007167
Enzyme-Linked Receptor Protein Signaling Pathway
GO:1901565
Organonitrogen Compound Catabolic Process
GO:0006508
Proteolysis
GO:0031344
Regulation Of Cell Projection Organization
GO:0071310
Cellular Response To Organic Substance
GO:0051248
Negative Regulation Of Protein Metabolic Process
GO:1901699
Cellular Response To Nitrogen Compound
GO:2001234
Negative Regulation Of Apoptotic Signaling Pathway
GO:0032880
Regulation Of Protein Localization
GO:0001890
Placenta Development
GO:0036211
Protein Modification Process
GO:0043434
Response To Peptide Hormone
GO:0010557
Positive Regulation Of Macromolecule Biosynthetic Process
GO:0022008
Neurogenesis
GO:0010639
Negative Regulation Of Organelle Organization
GO:0051254
Positive Regulation Of RNA Metabolic Process
GO:0032870
Cellular Response To Hormone Stimulus
GO:0006954
Inflammatory Response
GO:0044265
Cellular Macromolecule Catabolic Process
GO:0033993
Response To Lipid
GO:0042593
Glucose Homeostasis
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:0006915
Apoptotic Process
GO:0019219
Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0033043
Regulation Of Organelle Organization
GO:0045732
Positive Regulation Of Protein Catabolic Process
GO:0071363
Cellular Response To Growth Factor Stimulus
GO:0031328
Positive Regulation Of Cellular Biosynthetic Process
GO:0009792
Embryo Development Ending In Birth Or Egg Hatching
GO:1901652
Response To Peptide
GO:0010765
Positive Regulation Of Sodium Ion Transport
GO:0043069
Negative Regulation Of Programmed Cell Death
GO:0043067
Regulation Of Programmed Cell Death
GO:0030163
Protein Catabolic Process
GO:0034694
Response To Prostaglandin
GO:0002237
Response To Molecule Of Bacterial Origin
GO:0030334
Regulation Of Cell Migration
GO:0009057
Macromolecule Catabolic Process
GO:0048568
Embryonic Organ Development
GO:0007399
Nervous System Development
GO:0031667
Response To Nutrient Levels
GO:0060674
Placenta Blood Vessel Development
GO:0060716
Labyrinthine Layer Blood Vessel Development
GO:0051252
Regulation Of RNA Metabolic Process
GO:0010467
Gene Expression
GO:0061024
Membrane Organization
GO:0043086
Negative Regulation Of Catalytic Activity
GO:0034097
Response To Cytokine
GO:0071219
Cellular Response To Molecule Of Bacterial Origin
GO:0042176
Regulation Of Protein Catabolic Process
GO:0042552
Myelination
GO:0010256
Endomembrane System Organization
GO:0051336
Regulation Of Hydrolase Activity
GO:0021782
Glial Cell Development
GO:0010628
Positive Regulation Of Gene Expression
GO:0006796
Phosphate-Containing Compound Metabolic Process
GO:1902532
Negative Regulation Of Intracellular Signal Transduction
GO:0051960
Regulation Of Nervous System Development
GO:2001233
Regulation Of Apoptotic Signaling Pathway
GO:0044264
Cellular Polysaccharide Metabolic Process
GO:0045935
Positive Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0010243
Response To Organonitrogen Compound
GO:0007422
Peripheral Nervous System Development
GO:0051247
Positive Regulation Of Protein Metabolic Process
GO:0031331
Positive Regulation Of Cellular Catabolic Process
GO:0043269
Regulation Of Monoatomic Ion Transport
GO:0031329
Regulation Of Cellular Catabolic Process
GO:0006996
Organelle Organization
GO:1902531
Regulation Of Intracellular Signal Transduction
GO:0006006
Glucose Metabolic Process
GO:0007005
Mitochondrion Organization
GO:0042981
Regulation Of Apoptotic Process
GO:0001892
Embryonic Placenta Development
GO:2001141
Regulation Of RNA Biosynthetic Process
GO:0018193
Peptidyl-Amino Acid Modification
GO:0071345
Cellular Response To Cytokine Stimulus
GO:0016310
Phosphorylation
GO:1902680
Positive Regulation Of RNA Biosynthetic Process
GO:0097306
Cellular Response To Alcohol
GO:0010763
Positive Regulation Of Fibroblast Migration
GO:1901655
Cellular Response To Ketone
GO:2001242
Regulation Of Intrinsic Apoptotic Signaling Pathway
GO:0120035
Regulation Of Plasma Membrane Bounded Cell Projection Organization
GO:0034695
Response To Prostaglandin E
GO:0006112
Energy Reserve Metabolic Process
GO:0032868
Response To Insulin
GO:0070647
Protein Modification By Small Protein Conjugation Or Removal
GO:0043632
Modification-Dependent Macromolecule Catabolic Process
GO:0071379
Cellular Response To Prostaglandin Stimulus
GO:0042063
Gliogenesis
GO:1901653
Cellular Response To Peptide
GO:1901800
Positive Regulation Of Proteasomal Protein Catabolic Process
GO:0034612
Response To Tumor Necrosis Factor
GO:0010762
Regulation Of Fibroblast Migration
GO:0045861
Negative Regulation Of Proteolysis
GO:0090201
Negative Regulation Of Release Of Cytochrome C From Mitochondria
GO:0090199
Regulation Of Release Of Cytochrome C From Mitochondria
GO:0010823
Negative Regulation Of Mitochondrion Organization
GO:0071222
Cellular Response To Lipopolysaccharide
GO:0051346
Negative Regulation Of Hydrolase Activity
GO:0030162
Regulation Of Proteolysis
GO:0010821
Regulation Of Mitochondrion Organization
GO:0052547
Regulation Of Peptidase Activity
GO:0008637
Apoptotic Mitochondrial Changes
GO:2001243
Negative Regulation Of Intrinsic Apoptotic Signaling Pathway
GO:0010959
Regulation Of Metal Ion Transport
GO:0007010
Cytoskeleton Organization
GO:0007169
Transmembrane Receptor Protein Tyrosine Kinase Signaling Pathway
GO:0014037
Schwann Cell Differentiation
GO:2000058
Regulation Of Ubiquitin-Dependent Protein Catabolic Process
GO:0010498
Proteasomal Protein Catabolic Process
GO:0071364
Cellular Response To Epidermal Growth Factor Stimulus
GO:0043009
Chordate Embryonic Development
GO:0099175
Regulation Of Postsynapse Organization
GO:0044042
Glucan Metabolic Process
GO:0071375
Cellular Response To Peptide Hormone Stimulus
GO:0043066
Negative Regulation Of Apoptotic Process
GO:0022011
Myelination In Peripheral Nervous System
GO:0006468
Protein Phosphorylation
GO:0014044
Schwann Cell Development
GO:0006355
Regulation Of DNA-Templated Transcription
GO:0051603
Proteolysis Involved In Protein Catabolic Process
GO:0006073
Cellular Glucan Metabolic Process
GO:0071396
Cellular Response To Lipid
GO:0036294
Cellular Response To Decreased Oxygen Levels
GO:0045862
Positive Regulation Of Proteolysis
GO:0051146
Striated Muscle Cell Differentiation
GO:2000060
Positive Regulation Of Ubiquitin-Dependent Protein Catabolic Process
GO:0007009
Plasma Membrane Organization
GO:0061136
Regulation Of Proteasomal Protein Catabolic Process
GO:2000008
Regulation Of Protein Localization To Cell Surface
GO:0035924
Cellular Response To Vascular Endothelial Growth Factor Stimulus
GO:0001701
In Utero Embryonic Development
GO:0032869
Cellular Response To Insulin Stimulus
GO:0052548
Regulation Of Endopeptidase Activity
GO:0043154
Negative Regulation Of Cysteine-Type Endopeptidase Activity Involved In Apoptotic Process
GO:1903508
Positive Regulation Of Nucleic Acid-Templated Transcription
GO:0019941
Modification-Dependent Protein Catabolic Process
GO:0010975
Regulation Of Neuron Projection Development
GO:0006357
Regulation Of Transcription By RNA Polymerase II
GO:0045893
Positive Regulation Of DNA-Templated Transcription
GO:0071380
Cellular Response To Prostaglandin E Stimulus
GO:0032434
Regulation Of Proteasomal Ubiquitin-Dependent Protein Catabolic Process
GO:0043161
Proteasome-Mediated Ubiquitin-Dependent Protein Catabolic Process
GO:0048009
Insulin-Like Growth Factor Receptor Signaling Pathway
GO:1903050
Regulation Of Proteolysis Involved In Protein Catabolic Process
GO:0010466
Negative Regulation Of Peptidase Activity
GO:1903506
Regulation Of Nucleic Acid-Templated Transcription
GO:0018105
Peptidyl-Serine Phosphorylation
GO:0032446
Protein Modification By Small Protein Conjugation
GO:0032436
Positive Regulation Of Proteasomal Ubiquitin-Dependent Protein Catabolic Process
GO:0018209
Peptidyl-Serine Modification
GO:0008286
Insulin Receptor Signaling Pathway
GO:0005977
Glycogen Metabolic Process
GO:1903052
Positive Regulation Of Proteolysis Involved In Protein Catabolic Process
GO:0002028
Regulation Of Sodium Ion Transport
GO:0071356
Cellular Response To Tumor Necrosis Factor
GO:0006511
Ubiquitin-Dependent Protein Catabolic Process
GO:2000116
Regulation Of Cysteine-Type Endopeptidase Activity
GO:0016567
Protein Ubiquitination
GO:0010951
Negative Regulation Of Endopeptidase Activity
GO:0045944
Positive Regulation Of Transcription By RNA Polymerase II
GO:2000117
Negative Regulation Of Cysteine-Type Endopeptidase Activity
GO:0043281
Regulation Of Cysteine-Type Endopeptidase Activity Involved In Apoptotic Process
Cellular Component
GO:0005575
Cellular_component
GO:0032991
Protein-Containing Complex
GO:0110165
Cellular Anatomical Entity
GO:0005815
Microtubule Organizing Center
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0042995
Cell Projection
GO:0016020
Membrane
GO:0030054
Cell Junction
GO:0005829
Cytosol
GO:0005737
Cytoplasm
GO:0071944
Cell Periphery
GO:0036064
Ciliary Basal Body
GO:0005739
Mitochondrion
GO:0120025
Plasma Membrane Bounded Cell Projection
GO:0043229
Intracellular Organelle
GO:0070161
Anchoring Junction
GO:0045202
Synapse
GO:0043227
Membrane-Bounded Organelle
GO:0005886
Plasma Membrane
GO:0043228
Non-Membrane-Bounded Organelle
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0005929
Cilium
GO:0005911
Cell-Cell Junction
GO:0043232
Intracellular Non-Membrane-Bounded Organelle
GO:0098978
Glutamatergic Synapse
GO:0005856
Cytoskeleton
GO:0005819
Spindle
GO:0005634
Nucleus
GO:0015630
Microtubule Cytoskeleton

### InterPro Domains
1
480
IPR011993
IPR039026
IPR001849
IPR034676
IPR011009
IPR000719
IPR017441
IPR008271
IPR000961
IPR017892
Domain Details
IPR011993
PH-like domain superfamily (homologous_superfamily) [1-123]
IPR039026
Protein Kinase B, pleckstrin homology domain (domain) [4-111]
IPR001849
Pleckstrin homology domain (domain) [5-110]
IPR034676
Protein kinase B alpha, catalytic domain (domain) [124-479]
IPR011009
Protein kinase-like domain superfamily (homologous_superfamily) [145-459]
IPR000719
Protein kinase domain (domain) [150-408]
IPR017441
Protein kinase, ATP binding site (binding_site) [156-189]
IPR008271
Serine/threonine-protein kinase, active site (active_site) [270-282]
IPR000961
AGC-kinase, C-terminal (domain) [409-480]
IPR017892
Protein kinase, C-terminal (domain) [429-474]

---
*Generated by [BioReason](https://bioreason.net)*
