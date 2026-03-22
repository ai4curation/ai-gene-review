# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:14 PM*

---

**Organism:** Homo sapiens

### Thinking Trace
I begin with the InterPro architecture and its order along the polypeptide. The N-terminal ectodomain is defined by IPR036941 (Receptor L-domain superfamily, residues 25–530) and the embedded IPR000494 (Receptor L-domain, residues 57–480). These paired L-domains form a rigid scaffold that supports ligand capture and receptor dimerization. Interleaved with the L-domains lies IPR006211 (Furin-like cysteine-rich domain, residues 185–338) and its tandem IPR006212 (Furin-like repeat, residues 228–601), together with IPR009030 (Growth factor receptor cysteine-rich domain superfamily, residues 186–636) and IPR032778 (Growth factor receptor domain 4, residues 505–637). This extracellular module suite is characteristic of receptor tyrosine kinases that use cysteine-rich repeats to stabilize ectodomain folding and to regulate activation via ligand-induced dimerization. The membrane-proximal region is anchored by IPR049328 (Epidermal growth factor receptor-like, transmembrane-juxtamembrane segment, residues 646–681), which positions the receptor in the membrane and couples ectodomain status to intracellular signaling through the juxtamembrane switch.

The intracellular catalytic core is unambiguously specified by IPR011009 (Protein kinase-like domain superfamily, residues 708–1003), IPR000719 (Protein kinase domain, residues 712–979), IPR020635 (Tyrosine-protein kinase, catalytic domain, residues 712–968), and IPR001245 (Serine-threonine/tyrosine-protein kinase, catalytic domain, residues 714–966). The active chemistry is constrained by IPR017441 (Protein kinase, ATP binding site, residues 718–745) and IPR008266 (Tyrosine-protein kinase, active site, residues 833–845), which together create the ATP-binding pocket and the catalytic base required for phosphotransfer to tyrosine residues. Two broad family assignments, IPR016245 (Tyrosine protein kinase, EGF/ERB/XmrK receptor family, residues 6–1204) and IPR050122 (Receptor Tyrosine Kinase family, residues 58–974), integrate these extracellular and intracellular modules into a single receptor tyrosine kinase lineage.

This domain architecture causes a precise molecular function: the intracellular kinase module binds ATP via the glycine-rich loop and catalytic lysine (IPR017441) and executes phosphotransfer via the tyrosine-kinase active site (IPR008266), establishing GO:0004713 protein tyrosine kinase activity. The extracellular L-domains and cysteine-rich repeats dictate regulated dimerization and activation, ensuring that catalytic output is stimulus-gated.

From this activity, the biological process follows: receptor tyrosine kinases initiate intracellular signaling cascades that regulate cell proliferation and differentiation. The modular receptor layout—extracellular ligand/dimerization platform feeding into a cytosolic kinase—drives phosphorylation cascades that remodel transcriptional and cytoskeletal pathways, supporting GO:0007169 transmembrane receptor protein tyrosine kinase signaling pathway as the core process.

Cellular placement is encoded by the architecture. The presence of a single-pass transmembrane segment with an EGFR-like juxtamembrane region (IPR049328) and a large N-terminal ectodomain indicates a type I membrane receptor that primarily resides at the cell surface. Thus, the protein is an integral component of membrane and is positioned at the plasma membrane, consistent with the experimentally inferred membrane localization.

Mechanistically, I infer that extracellular binding and ectodomain rigidity promote receptor dimerization; the transmembrane-juxtamembrane segment then stabilizes an active intracellular kinase dimer. Autophosphorylation creates docking sites that recruit cytosolic adaptors and enzymes. Likely interaction partners include SH2- and PTB-domain-containing adaptors (e.g., SHC1, GRB2) that couple to SOS and PI3K pathways, as well as phosphatases such as PTPN11 (SHP2) and regulatory phosphatases that tune signal amplitude. This assembly produces a switchable kinase hub that propagates signals controlling proliferation and differentiation from the plasma membrane.

### Functional Summary
A single-pass cell-surface receptor that uses an extracellular ligand-binding scaffold and a juxtamembrane switch to control an intracellular tyrosine kinase core. Upon dimerization at the membrane, it binds ATP and autophosphorylates tyrosine residues, creating docking sites that recruit adaptor and effector proteins. This signaling hub propagates pathways that govern cell proliferation and differentiation from the plasma membrane.

### UniProt Summary
Tyrosine-protein kinase that is believed to play a role in the regulation of cell proliferation and differentiation.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0003824
Catalytic Activity
GO:0060089
Molecular Transducer Activity
GO:0098772
Molecular Function Regulator Activity
GO:0005488
Binding
GO:0030234
Enzyme Regulator Activity
GO:0140677
Molecular Function Activator Activity
GO:0016740
Transferase Activity
GO:0044877
Protein-Containing Complex Binding
GO:0003682
Chromatin Binding
GO:0038023
Signaling Receptor Activity
GO:0140096
Catalytic Activity, Acting On A Protein
GO:0005515
Protein Binding
GO:0051015
Actin Filament Binding
GO:0004672
Protein Kinase Activity
GO:0042802
Identical Protein Binding
GO:0050839
Cell Adhesion Molecule Binding
GO:0008047
Enzyme Activator Activity
GO:0008092
Cytoskeletal Protein Binding
GO:0004888
Transmembrane Signaling Receptor Activity
GO:0016772
Transferase Activity, Transferring Phosphorus-Containing Groups
GO:0019899
Enzyme Binding
GO:0019207
Kinase Regulator Activity
GO:0044389
Ubiquitin-Like Protein Ligase Binding
GO:0016301
Kinase Activity
GO:0019209
Kinase Activator Activity
GO:0019900
Kinase Binding
GO:0016773
Phosphotransferase Activity, Alcohol Group As Acceptor
GO:0019902
Phosphatase Binding
GO:0003779
Actin Binding
GO:0019887
Protein Kinase Regulator Activity
GO:0045296
Cadherin Binding
GO:0019199
Transmembrane Receptor Protein Kinase Activity
GO:0004713
Protein Tyrosine Kinase Activity
GO:0031625
Ubiquitin Protein Ligase Binding
GO:0004714
Transmembrane Receptor Protein Tyrosine Kinase Activity
GO:0030295
Protein Kinase Activator Activity
GO:0019903
Protein Phosphatase Binding
GO:0030296
Protein Tyrosine Kinase Activator Activity
Biological Process
GO:0008150
Biological_process
GO:0051179
Localization
GO:0048518
Positive Regulation Of Biological Process
GO:0050789
Regulation Of Biological Process
GO:0023052
Signaling
GO:0065007
Biological Regulation
GO:0050896
Response To Stimulus
GO:0009987
Cellular Process
GO:0008152
Metabolic Process
GO:0048519
Negative Regulation Of Biological Process
GO:0051641
Cellular Localization
GO:0023057
Negative Regulation Of Signaling
GO:0042221
Response To Chemical
GO:0006807
Nitrogen Compound Metabolic Process
GO:0071840
Cellular Component Organization Or Biogenesis
GO:0051241
Negative Regulation Of Multicellular Organismal Process
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0045927
Positive Regulation Of Growth
GO:0009892
Negative Regulation Of Metabolic Process
GO:0050793
Regulation Of Developmental Process
GO:0040017
Positive Regulation Of Locomotion
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
GO:0007165
Signal Transduction
GO:0040012
Regulation Of Locomotion
GO:0009628
Response To Abiotic Stimulus
GO:0023056
Positive Regulation Of Signaling
GO:0048584
Positive Regulation Of Response To Stimulus
GO:0019222
Regulation Of Metabolic Process
GO:0007155
Cell Adhesion
GO:0032879
Regulation Of Localization
GO:0051234
Establishment Of Localization
GO:0071704
Organic Substance Metabolic Process
GO:0033036
Macromolecule Localization
GO:0044237
Cellular Metabolic Process
GO:0009893
Positive Regulation Of Metabolic Process
GO:0065009
Regulation Of Molecular Function
GO:0044238
Primary Metabolic Process
GO:0006950
Response To Stress
GO:0048585
Negative Regulation Of Response To Stimulus
GO:0007154
Cell Communication
GO:0040008
Regulation Of Growth
GO:0048522
Positive Regulation Of Cellular Process
GO:0009968
Negative Regulation Of Signal Transduction
GO:0090068
Positive Regulation Of Cell Cycle Process
GO:2000145
Regulation Of Cell Motility
GO:0060548
Negative Regulation Of Cell Death
GO:0009314
Response To Radiation
GO:0080134
Regulation Of Response To Stress
GO:0009966
Regulation Of Signal Transduction
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0051668
Localization Within Membrane
GO:1905208
Negative Regulation Of Cardiocyte Differentiation
GO:0045184
Establishment Of Protein Localization
GO:0045787
Positive Regulation Of Cell Cycle
GO:0006793
Phosphorus Metabolic Process
GO:0009894
Regulation Of Catabolic Process
GO:0051726
Regulation Of Cell Cycle
GO:0010035
Response To Inorganic Substance
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0045595
Regulation Of Cell Differentiation
GO:0007166
Cell Surface Receptor Signaling Pathway
GO:0016043
Cellular Component Organization
GO:0051128
Regulation Of Cellular Component Organization
GO:0010564
Regulation Of Cell Cycle Process
GO:0008284
Positive Regulation Of Cell Population Proliferation
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0009967
Positive Regulation Of Signal Transduction
GO:0050790
Regulation Of Catalytic Activity
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:0010648
Negative Regulation Of Cell Communication
GO:0044093
Positive Regulation Of Molecular Function
GO:1903829
Positive Regulation Of Protein Localization
GO:1901564
Organonitrogen Compound Metabolic Process
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0098609
Cell-Cell Adhesion
GO:0006979
Response To Oxidative Stress
GO:0060341
Regulation Of Cellular Localization
GO:0019538
Protein Metabolic Process
GO:0001558
Regulation Of Cell Growth
GO:0080135
Regulation Of Cellular Response To Stress
GO:1901700
Response To Oxygen-Containing Compound
GO:0030307
Positive Regulation Of Cell Growth
GO:0043170
Macromolecule Metabolic Process
GO:0010033
Response To Organic Substance
GO:2000147
Positive Regulation Of Cell Motility
GO:0009891
Positive Regulation Of Biosynthetic Process
GO:2001022
Positive Regulation Of Response To DNA Damage Stimulus
GO:0042127
Regulation Of Cell Population Proliferation
GO:0010941
Regulation Of Cell Death
GO:0031325
Positive Regulation Of Cellular Metabolic Process
GO:0010646
Regulation Of Cell Communication
GO:0070887
Cellular Response To Chemical Stimulus
GO:0033554
Cellular Response To Stress
GO:0045596
Negative Regulation Of Cell Differentiation
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
GO:0080090
Regulation Of Primary Metabolic Process
GO:0034599
Cellular Response To Oxidative Stress
GO:0051341
Regulation Of Oxidoreductase Activity
GO:0007346
Regulation Of Mitotic Cell Cycle
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0032355
Response To Estradiol
GO:0051246
Regulation Of Protein Metabolic Process
GO:0043069
Negative Regulation Of Programmed Cell Death
GO:0043067
Regulation Of Programmed Cell Death
GO:0070302
Regulation Of Stress-Activated Protein Kinase Signaling Cascade
GO:0030334
Regulation Of Cell Migration
GO:0050678
Regulation Of Epithelial Cell Proliferation
GO:0010468
Regulation Of Gene Expression
GO:0043412
Macromolecule Modification
GO:1901184
Regulation Of ERBB Signaling Pathway
GO:0030335
Positive Regulation Of Cell Migration
GO:1902533
Positive Regulation Of Intracellular Signal Transduction
GO:0051252
Regulation Of RNA Metabolic Process
GO:0043085
Positive Regulation Of Catalytic Activity
GO:1901701
Cellular Response To Oxygen-Containing Compound
GO:0061024
Membrane Organization
GO:0010038
Response To Metal Ion
GO:1901185
Negative Regulation Of ERBB Signaling Pathway
GO:0009416
Response To Light Stimulus
GO:0042177
Negative Regulation Of Protein Catabolic Process
GO:0010562
Positive Regulation Of Phosphorus Metabolic Process
GO:1904377
Positive Regulation Of Protein Localization To Cell Periphery
GO:0007167
Enzyme-Linked Receptor Protein Signaling Pathway
GO:1901989
Positive Regulation Of Cell Cycle Phase Transition
GO:0042176
Regulation Of Protein Catabolic Process
GO:0051052
Regulation Of DNA Metabolic Process
GO:0071310
Cellular Response To Organic Substance
GO:0051054
Positive Regulation Of DNA Metabolic Process
GO:0051336
Regulation Of Hydrolase Activity
GO:0062197
Cellular Response To Chemical Stress
GO:0051248
Negative Regulation Of Protein Metabolic Process
GO:0006796
Phosphate-Containing Compound Metabolic Process
GO:0030111
Regulation Of Wnt Signaling Pathway
GO:0032880
Regulation Of Protein Localization
GO:0045931
Positive Regulation Of Mitotic Cell Cycle
GO:0030177
Positive Regulation Of Wnt Signaling Pathway
GO:1905477
Positive Regulation Of Protein Localization To Membrane
GO:0045739
Positive Regulation Of DNA Repair
GO:0090150
Establishment Of Protein Localization To Membrane
GO:2001020
Regulation Of Response To DNA Damage Stimulus
GO:0050679
Positive Regulation Of Epithelial Cell Proliferation
GO:0036211
Protein Modification Process
GO:0010557
Positive Regulation Of Macromolecule Biosynthetic Process
GO:0045935
Positive Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0051254
Positive Regulation Of RNA Metabolic Process
GO:0072657
Protein Localization To Membrane
GO:0071241
Cellular Response To Inorganic Substance
GO:1904029
Regulation Of Cyclin-Dependent Protein Kinase Activity
GO:0033993
Response To Lipid
GO:0045737
Positive Regulation Of Cyclin-Dependent Protein Serine/Threonine Kinase Activity
GO:1901987
Regulation Of Cell Cycle Phase Transition
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:0051247
Positive Regulation Of Protein Metabolic Process
GO:0019219
Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0008104
Protein Localization
GO:0014070
Response To Organic Cyclic Compound
GO:0051338
Regulation Of Transferase Activity
GO:1905207
Regulation Of Cardiocyte Differentiation
GO:0000302
Response To Reactive Oxygen Species
GO:0031328
Positive Regulation Of Cellular Biosynthetic Process
GO:0051174
Regulation Of Phosphorus Metabolic Process
GO:1902531
Regulation Of Intracellular Signal Transduction
GO:0014066
Regulation Of Phosphatidylinositol 3-Kinase Signaling
GO:0042981
Regulation Of Apoptotic Process
GO:1905475
Regulation Of Protein Localization To Membrane
GO:0045937
Positive Regulation Of Phosphate Metabolic Process
GO:2001141
Regulation Of RNA Biosynthetic Process
GO:0051897
Positive Regulation Of Protein Kinase B Signaling
GO:1902808
Positive Regulation Of Cell Cycle G1/S Phase Transition
GO:0018193
Peptidyl-Amino Acid Modification
GO:1904031
Positive Regulation Of Cyclin-Dependent Protein Kinase Activity
GO:0016310
Phosphorylation
GO:0043549
Regulation Of Kinase Activity
GO:1901992
Positive Regulation Of Mitotic Cell Cycle Phase Transition
GO:2000630
Positive Regulation Of MiRNA Metabolic Process
GO:0060191
Regulation Of Lipase Activity
GO:0051896
Regulation Of Protein Kinase B Signaling
GO:0006275
Regulation Of DNA Replication
GO:0009411
Response To UV
GO:0007169
Transmembrane Receptor Protein Tyrosine Kinase Signaling Pathway
GO:0046686
Response To Cadmium Ion
GO:1902680
Positive Regulation Of RNA Biosynthetic Process
GO:0043410
Positive Regulation Of MAPK Cascade
GO:0051205
Protein Insertion Into Membrane
GO:0051345
Positive Regulation Of Hydrolase Activity
GO:0034614
Cellular Response To Reactive Oxygen Species
GO:0060828
Regulation Of Canonical Wnt Signaling Pathway
GO:0031401
Positive Regulation Of Protein Modification Process
GO:0032872
Regulation Of Stress-Activated MAPK Cascade
GO:0042058
Regulation Of Epidermal Growth Factor Receptor Signaling Pathway
GO:0043408
Regulation Of MAPK Cascade
GO:0000079
Regulation Of Cyclin-Dependent Protein Serine/Threonine Kinase Activity
GO:0010749
Regulation Of Nitric Oxide Mediated Signal Transduction
GO:0051347
Positive Regulation Of Transferase Activity
GO:0031399
Regulation Of Protein Modification Process
GO:0006282
Regulation Of DNA Repair
GO:1901222
Regulation Of NIK/NF-KappaB Signaling
GO:0071392
Cellular Response To Estradiol Stimulus
GO:0043066
Negative Regulation Of Apoptotic Process
GO:0045740
Positive Regulation Of DNA Replication
GO:0006468
Protein Phosphorylation
GO:0006355
Regulation Of DNA-Templated Transcription
GO:0071407
Cellular Response To Organic Cyclic Compound
GO:0019220
Regulation Of Phosphate Metabolic Process
GO:0071396
Cellular Response To Lipid
GO:1901224
Positive Regulation Of NIK/NF-KappaB Signaling
GO:0071248
Cellular Response To Metal Ion
GO:1901990
Regulation Of Mitotic Cell Cycle Phase Transition
GO:2000628
Regulation Of MiRNA Metabolic Process
GO:0032768
Regulation Of Monooxygenase Activity
GO:1902806
Regulation Of Cell Cycle G1/S Phase Transition
GO:1904375
Regulation Of Protein Localization To Cell Periphery
GO:1903078
Positive Regulation Of Protein Localization To Plasma Membrane
GO:0042059
Negative Regulation Of Epidermal Growth Factor Receptor Signaling Pathway
GO:0090263
Positive Regulation Of Canonical Wnt Signaling Pathway
GO:0001932
Regulation Of Protein Phosphorylation
GO:0070141
Response To UV-A
GO:0070374
Positive Regulation Of ERK1 And ERK2 Cascade
GO:1903076
Regulation Of Protein Localization To Plasma Membrane
GO:0010517
Regulation Of Phospholipase Activity
GO:0038127
ERBB Signaling Pathway
GO:0045859
Regulation Of Protein Kinase Activity
GO:1903508
Positive Regulation Of Nucleic Acid-Templated Transcription
GO:0042327
Positive Regulation Of Phosphorylation
GO:1903506
Regulation Of Nucleic Acid-Templated Transcription
GO:0043406
Positive Regulation Of MAP Kinase Activity
GO:1900087
Positive Regulation Of G1/S Transition Of Mitotic Cell Cycle
GO:0001934
Positive Regulation Of Protein Phosphorylation
GO:1902893
Regulation Of MiRNA Transcription
GO:0060193
Positive Regulation Of Lipase Activity
GO:0070372
Regulation Of ERK1 And ERK2 Cascade
GO:0018212
Peptidyl-Tyrosine Modification
GO:0042325
Regulation Of Phosphorylation
GO:0006357
Regulation Of Transcription By RNA Polymerase II
GO:0046328
Regulation Of JNK Cascade
GO:0018108
Peptidyl-Tyrosine Phosphorylation
GO:0045893
Positive Regulation Of DNA-Templated Transcription
GO:0033674
Positive Regulation Of Kinase Activity
GO:0071276
Cellular Response To Cadmium Ion
GO:1902895
Positive Regulation Of MiRNA Transcription
GO:0050999
Regulation Of Nitric-Oxide Synthase Activity
GO:2000045
Regulation Of G1/S Transition Of Mitotic Cell Cycle
GO:0046777
Protein Autophosphorylation
GO:0045944
Positive Regulation Of Transcription By RNA Polymerase II
GO:0071900
Regulation Of Protein Serine/Threonine Kinase Activity
GO:0033138
Positive Regulation Of Peptidyl-Serine Phosphorylation
GO:0050730
Regulation Of Peptidyl-Tyrosine Phosphorylation
GO:0038083
Peptidyl-Tyrosine Autophosphorylation
GO:0007173
Epidermal Growth Factor Receptor Signaling Pathway
GO:0010518
Positive Regulation Of Phospholipase Activity
GO:1900274
Regulation Of Phospholipase C Activity
GO:0033135
Regulation Of Peptidyl-Serine Phosphorylation
GO:0038128
ERBB2 Signaling Pathway
GO:0045860
Positive Regulation Of Protein Kinase Activity
GO:0043405
Regulation Of MAP Kinase Activity
GO:0071902
Positive Regulation Of Protein Serine/Threonine Kinase Activity
GO:0010863
Positive Regulation Of Phospholipase C Activity
GO:0007202
Activation Of Phospholipase C Activity
Cellular Component
GO:0005575
Cellular_component
GO:0032991
Protein-Containing Complex
GO:0110165
Cellular Anatomical Entity
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0045178
Basal Part Of Cell
GO:0042995
Cell Projection
GO:0016020
Membrane
GO:0031974
Membrane-Enclosed Lumen
GO:0009986
Cell Surface
GO:0048471
Perinuclear Region Of Cytoplasm
GO:0071944
Cell Periphery
GO:0030054
Cell Junction
GO:0031252
Cell Leading Edge
GO:0031256
Leading Edge Membrane
GO:0043235
Receptor Complex
GO:0005737
Cytoplasm
GO:0012505
Endomembrane System
GO:0031090
Organelle Membrane
GO:0120025
Plasma Membrane Bounded Cell Projection
GO:0031410
Cytoplasmic Vesicle
GO:0043229
Intracellular Organelle
GO:0005768
Endosome
GO:0001726
Ruffle
GO:0009925
Basal Plasma Membrane
GO:0098590
Plasma Membrane Region
GO:0043233
Organelle Lumen
GO:0098857
Membrane Microdomain
GO:0032587
Ruffle Membrane
GO:0070161
Anchoring Junction
GO:0043227
Membrane-Bounded Organelle
GO:0005886
Plasma Membrane
GO:0030055
Cell-Substrate Junction
GO:0045121
Membrane Raft
GO:0030139
Endocytic Vesicle
GO:0031253
Cell Projection Membrane
GO:0031983
Vesicle Lumen
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0098588
Bounding Membrane Of Organelle
GO:0012506
Vesicle Membrane
GO:0005770
Late Endosome
GO:0005769
Early Endosome
GO:0030135
Coated Vesicle
GO:0010008
Endosome Membrane
GO:0016323
Basolateral Plasma Membrane
GO:0031982
Vesicle
GO:0070013
Intracellular Organelle Lumen
GO:0030659
Cytoplasmic Vesicle Membrane
GO:0005771
Multivesicular Body
GO:0005925
Focal Adhesion
GO:0030666
Endocytic Vesicle Membrane
GO:0097708
Intracellular Vesicle
GO:0005634
Nucleus
GO:0031901
Early Endosome Membrane
GO:0030136
Clathrin-Coated Vesicle
GO:0030662
Coated Vesicle Membrane
GO:0045334
Clathrin-Coated Endocytic Vesicle
GO:0030669
Clathrin-Coated Endocytic Vesicle Membrane
GO:0030665
Clathrin-Coated Vesicle Membrane

### InterPro Domains
1
1210
IPR016245
IPR036941
IPR000494
IPR050122
IPR006211
IPR009030
IPR006212
IPR032778
IPR049328
IPR011009
IPR000719
IPR020635
IPR001245
IPR017441
IPR008266
Domain Details
IPR016245
Tyrosine protein kinase, EGF/ERB/XmrK receptor (family) [6-1204]
IPR036941
Receptor L-domain superfamily (homologous_superfamily) [25-530]
IPR000494
Receptor L-domain (domain) [57-480]
IPR050122
Receptor Tyrosine Kinase (family) [58-974]
IPR006211
Furin-like cysteine-rich domain (domain) [185-338]
IPR009030
Growth factor receptor cysteine-rich domain superfamily (homologous_superfamily) [186-636]
IPR006212
Furin-like repeat (repeat) [228-601]
IPR032778
Growth factor receptor domain 4 (domain) [505-637]
IPR049328
Epidermal growth factor receptor-like, transmembrane-juxtamembrane segment (domain) [646-681]
IPR011009
Protein kinase-like domain superfamily (homologous_superfamily) [708-1003]
IPR000719
Protein kinase domain (domain) [712-979]
IPR020635
Tyrosine-protein kinase, catalytic domain (domain) [712-968]
IPR001245
Serine-threonine/tyrosine-protein kinase, catalytic domain (domain) [714-966]
IPR017441
Protein kinase, ATP binding site (binding_site) [718-745]
IPR008266
Tyrosine-protein kinase, active site (active_site) [833-845]

---
*Generated by [BioReason](https://bioreason.net)*
