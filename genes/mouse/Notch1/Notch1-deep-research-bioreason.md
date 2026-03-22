# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:20 PM*

---

**Organism:** Mus musculus

### Thinking Trace
I begin by examining the InterPro architecture and its order along the polypeptide. A broad family signature IPR008297 (Notch family, residues 5–2000) blankets essentially the entire sequence, immediately placing the protein within the canonical Notch receptor class. The N-terminal ectodomain is dominated by tandem epidermal growth factor modules: IPR000742 (EGF-like domain, residues 20–1426) forms a long series of disulfide-rich repeats that mediate high-affinity extracellular interactions. Many of these repeats are calcium-coordinated, as indicated by IPR001881 (EGF-like calcium-binding domain, residues 59–1384), IPR018097 (EGF-like calcium-binding, conserved site, residues 178–1253), and IPR049883 (NOTCH1, EGF-like calcium-binding domain, residues 178–900). These Ca2+-binding EGF modules rigidify the ectodomain and create precise binding surfaces necessary for ligand recognition and mechanical signaling. Post-translational fine-tuning of these repeats is signaled by IPR000152 (EGF-type aspartate/asparagine hydroxylation site, residues 195–1255) and IPR013032 (EGF-like, conserved site, residues 344–1374), which together specify hydroxylation and glycosylation chemistries that stabilize the fold and modulate receptor–ligand dynamics. The ectodomain belongs to IPR009030 (Growth factor receptor cysteine-rich domain superfamily, residues 288–1311), further emphasizing a modular, disulfide-bonded extracellular platform.

A transition occurs after the large ectodomain into the intracellular signaling core. IPR022362 (Neurogenic locus notch homolog protein 1 family, residues 1426–1714) spans the juxtamembrane-to-ankyrin region and leads into the hallmark negative regulatory apparatus: IPR000800 (Notch domain, residues 1442–1571) and IPR235993 superfamily IPR035993 (Notch-like domain superfamily, residues 1448–1561) define the autoinhibited negative regulatory region that holds the receptor in a latent state. Immediately downstream, IPR010660 (Notch, NOD domain, residues 1566–1622) and IPR011656 (Notch, NODP domain, residues 1660–1722) form the paired negative regulatory elements that physically mask the intracellular tail until proteolytic activation. This architecture causes a tethered “switch”: force or conformational input from extracellular ligand binding unlocks the NOD/NODP clamp and exposes the intracellular signaling platform.

The C-terminal cytoplasmic portion contains IPR036770 (Ankyrin repeat-containing domain superfamily, residues 1858–2000) and discrete repeats IPR002110 (Ankyrin repeat, residues 1870–1980). Ankyrin repeats form a solenoid that scaffolds transcriptional complexes. In the intracellular domain, this ankyrin core recruits the CSL/RBPJ DNA-binding factor and coactivators, translating receptor activation into transcriptional responses. Together, this ordered arrangement—extracellular EGF arrays for ligand sensing, an intracellular negative regulatory cassette (NOD/NODP), and a C-terminal ankyrin scaffold—establishes a single-pass type I receptor that signals by proteolysis-dependent release of a transcriptional effector module.

From this domain logic, the molecular function emerges as a signaling receptor that operates through intracellular protein–protein interaction surfaces rather than intrinsic catalysis. The EGF-rich ectodomain confers ligand recognition and force transduction, while the ankyrin repeats enforce transcriptional complex assembly. This architecture dictates GO:0030234 molecular_function as a coreceptor/scaffolding receptor that binds partners to transmit signals rather than enzymatic chemistry.

The biological process follows directly from the receptor’s canonical role in metazoan developmental signaling. The combination of Notch family signatures (IPR008297; IPR022362), the NOD/NODP regulatory apparatus, and the ankyrin repeat tail causally links extracellular ligand perception to CSL/RBPJ-centered transcriptional control. Such signaling governs lineage choices and tissue patterning; therefore, I infer participation in the Notch signaling pathway and its downstream developmental programs.

Cellular localization is dictated by topology and domains. The long extracellular region and single-pass architecture place the receptor at the plasma membrane as a type I membrane protein. The intracellular ankyrin-rich tail and proteolytic activation further imply cycling between the cell surface and endomembrane compartments for signal propagation. Thus, the most parsimonious cellular component assignments are the plasma membrane and, more generally, the membrane system.

Mechanistically, I hypothesize that extracellular DSL-family ligands (Delta/Serrate/Jagged) bind the Ca2+-stabilized EGF array, applying mechanical or allosteric input that unlocks the NOD/NODP clamp. This permits metalloprotease cleavage and intramembrane proteolysis, liberating the intracellular domain to dock onto CSL/RBPJ and assemble coactivators via the ankyrin repeats. Likely interaction partners therefore include CSL/RBPJ and its co-regulators, as well as ligand and trafficking machinery that coordinate receptor activation and transcriptional output.

### Functional Summary
A single-pass membrane signaling receptor in mouse that presents a long, calcium-stabilized extracellular array of cysteine-rich repeats to perceive secreted ligands and convert this binding into intracellular signals. Autoinhibitory elements near the membrane restrain the receptor until ligand engagement triggers proteolytic activation, after which the intracellular tail uses ankyrin repeats to assemble transcriptional complexes that modulate developmental gene expression. The receptor operates at the cell surface and within the membrane system to regulate lineage and patterning decisions through ligand-gated assembly of transcriptional machinery.

### UniProt Summary
Not a secreted protein but a membrane-bound precursor of a transcription factor.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0098772
Molecular Function Regulator Activity
GO:0005488
Binding
GO:0140110
Transcription Regulator Activity
GO:0030234
Enzyme Regulator Activity
GO:0140677
Molecular Function Activator Activity
GO:1901363
Heterocyclic Compound Binding
GO:0003682
Chromatin Binding
GO:0097159
Organic Cyclic Compound Binding
GO:0003712
Transcription Coregulator Activity
GO:0005515
Protein Binding
GO:0140678
Molecular Function Inhibitor Activity
GO:0003676
Nucleic Acid Binding
GO:0005102
Signaling Receptor Binding
GO:0031490
Chromatin DNA Binding
GO:0019899
Enzyme Binding
GO:0004857
Enzyme Inhibitor Activity
GO:0003713
Transcription Coactivator Activity
GO:0005112
Notch Binding
GO:0003677
DNA Binding
Biological Process
GO:0008150
Biological_process
GO:0065007
Biological Regulation
GO:0050896
Response To Stimulus
GO:0022414
Reproductive Process
GO:0050789
Regulation Of Biological Process
GO:0000003
Reproduction
GO:0032501
Multicellular Organismal Process
GO:0008152
Metabolic Process
GO:0042592
Homeostatic Process
GO:0002376
Immune System Process
GO:0051179
Localization
GO:0023052
Signaling
GO:0040007
Growth
GO:0048519
Negative Regulation Of Biological Process
GO:0048518
Positive Regulation Of Biological Process
GO:0032502
Developmental Process
GO:0009987
Cellular Process
GO:0048856
Anatomical Structure Development
GO:0023057
Negative Regulation Of Signaling
GO:0051301
Cell Division
GO:0003006
Developmental Process Involved In Reproduction
GO:0048646
Anatomical Structure Formation Involved In Morphogenesis
GO:0048871
Multicellular Organismal-Level Homeostasis
GO:0048583
Regulation Of Response To Stimulus
GO:0048523
Negative Regulation Of Cellular Process
GO:0009058
Biosynthetic Process
GO:0048524
Positive Regulation Of Viral Process
GO:0051234
Establishment Of Localization
GO:0009056
Catabolic Process
GO:0033036
Macromolecule Localization
GO:0048589
Developmental Growth
GO:0008283
Cell Population Proliferation
GO:0006807
Nitrogen Compound Metabolic Process
GO:0051241
Negative Regulation Of Multicellular Organismal Process
GO:0008219
Cell Death
GO:0040017
Positive Regulation Of Locomotion
GO:0023051
Regulation Of Signaling
GO:0051093
Negative Regulation Of Developmental Process
GO:0007165
Signal Transduction
GO:0051051
Negative Regulation Of Transport
GO:0050792
Regulation Of Viral Process
GO:0044238
Primary Metabolic Process
GO:0001763
Morphogenesis Of A Branching Structure
GO:0051094
Positive Regulation Of Developmental Process
GO:0048585
Negative Regulation Of Response To Stimulus
GO:0040008
Regulation Of Growth
GO:0051641
Cellular Localization
GO:0006955
Immune Response
GO:0051240
Positive Regulation Of Multicellular Organismal Process
GO:0042303
Molting Cycle
GO:0007389
Pattern Specification Process
GO:0071840
Cellular Component Organization Or Biogenesis
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0009892
Negative Regulation Of Metabolic Process
GO:0050794
Regulation Of Cellular Process
GO:0051716
Cellular Response To Stimulus
GO:0040012
Regulation Of Locomotion
GO:0048869
Cellular Developmental Process
GO:0009628
Response To Abiotic Stimulus
GO:0035265
Organ Growth
GO:0048584
Positive Regulation Of Response To Stimulus
GO:0019222
Regulation Of Metabolic Process
GO:0022404
Molting Cycle Process
GO:0065009
Regulation Of Molecular Function
GO:0140352
Export From Cell
GO:0007154
Cell Communication
GO:0048522
Positive Regulation Of Cellular Process
GO:0009653
Anatomical Structure Morphogenesis
GO:0048870
Cell Motility
GO:0042221
Response To Chemical
GO:2000241
Regulation Of Reproductive Process
GO:0045927
Positive Regulation Of Growth
GO:0050793
Regulation Of Developmental Process
GO:0023056
Positive Regulation Of Signaling
GO:0007275
Multicellular Organism Development
GO:0032879
Regulation Of Localization
GO:0071704
Organic Substance Metabolic Process
GO:0044237
Cellular Metabolic Process
GO:0009893
Positive Regulation Of Metabolic Process
GO:0006950
Response To Stress
GO:0032989
Cellular Component Morphogenesis
GO:0051129
Negative Regulation Of Cellular Component Organization
GO:2000145
Regulation Of Cell Motility
GO:0044057
Regulation Of System Process
GO:0048513
Animal Organ Development
GO:0003407
Neural Retina Development
GO:0060627
Regulation Of Vesicle-Mediated Transport
GO:1904747
Positive Regulation Of Apoptotic Process Involved In Development
GO:0090288
Negative Regulation Of Cellular Response To Growth Factor Stimulus
GO:0060041
Retina Development In Camera-Type Eye
GO:0051048
Negative Regulation Of Secretion
GO:0040034
Regulation Of Development, Heterochronic
GO:0060411
Cardiac Septum Morphogenesis
GO:0022603
Regulation Of Anatomical Structure Morphogenesis
GO:0032940
Secretion By Cell
GO:0072006
Nephron Development
GO:0061383
Trabecula Morphogenesis
GO:0014741
Negative Regulation Of Muscle Hypertrophy
GO:0045684
Positive Regulation Of Epidermis Development
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0045597
Positive Regulation Of Cell Differentiation
GO:0048736
Appendage Development
GO:1901576
Organic Substance Biosynthetic Process
GO:0008285
Negative Regulation Of Cell Population Proliferation
GO:0019538
Protein Metabolic Process
GO:0009799
Specification Of Symmetry
GO:0044249
Cellular Biosynthetic Process
GO:1901700
Response To Oxygen-Containing Compound
GO:0060740
Prostate Gland Epithelium Morphogenesis
GO:0043170
Macromolecule Metabolic Process
GO:2000147
Positive Regulation Of Cell Motility
GO:0009891
Positive Regulation Of Biosynthetic Process
GO:0048872
Homeostasis Of Number Of Cells
GO:0003272
Endocardial Cushion Formation
GO:0061061
Muscle Structure Development
GO:0042127
Regulation Of Cell Population Proliferation
GO:0010941
Regulation Of Cell Death
GO:0003002
Regionalization
GO:1901698
Response To Nitrogen Compound
GO:0045596
Negative Regulation Of Cell Differentiation
GO:0006810
Transport
GO:0006959
Humoral Immune Response
GO:0010647
Positive Regulation Of Cell Communication
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0022405
Hair Cycle Process
GO:0080090
Regulation Of Primary Metabolic Process
GO:0009968
Negative Regulation Of Signal Transduction
GO:0001666
Response To Hypoxia
GO:0045069
Regulation Of Viral Genome Replication
GO:0060548
Negative Regulation Of Cell Death
GO:0030154
Cell Differentiation
GO:0051961
Negative Regulation Of Nervous System Development
GO:0048731
System Development
GO:0070482
Response To Oxygen Levels
GO:0003279
Cardiac Septum Development
GO:0030155
Regulation Of Cell Adhesion
GO:0046620
Regulation Of Organ Growth
GO:0060419
Heart Growth
GO:0035295
Tube Development
GO:0000902
Cell Morphogenesis
GO:0009887
Animal Organ Morphogenesis
GO:0007166
Cell Surface Receptor Signaling Pathway
GO:0051128
Regulation Of Cellular Component Organization
GO:0070168
Negative Regulation Of Biomineral Tissue Development
GO:0030278
Regulation Of Ossification
GO:0008284
Positive Regulation Of Cell Population Proliferation
GO:0035239
Tube Morphogenesis
GO:0048639
Positive Regulation Of Developmental Growth
GO:0010648
Negative Regulation Of Cell Communication
GO:1902742
Apoptotic Process Involved In Development
GO:0009798
Axis Specification
GO:0060042
Retina Morphogenesis In Camera-Type Eye
GO:0031069
Hair Follicle Morphogenesis
GO:0061138
Morphogenesis Of A Branching Epithelium
GO:0046622
Positive Regulation Of Organ Growth
GO:0003205
Cardiac Chamber Development
GO:0031324
Negative Regulation Of Cellular Metabolic Process
GO:0045165
Cell Fate Commitment
GO:0048598
Embryonic Morphogenesis
GO:0070887
Cellular Response To Chemical Stimulus
GO:0032835
Glomerulus Development
GO:0001894
Tissue Homeostasis
GO:0017145
Stem Cell Division
GO:0042633
Hair Cycle
GO:0120161
Regulation Of Cold-Induced Thermogenesis
GO:0060560
Developmental Growth Involved In Morphogenesis
GO:0046533
Negative Regulation Of Photoreceptor Cell Differentiation
GO:0009966
Regulation Of Signal Transduction
GO:0007440
Foregut Morphogenesis
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0048608
Reproductive Structure Development
GO:0006725
Cellular Aromatic Compound Metabolic Process
GO:0043502
Regulation Of Muscle Adaptation
GO:0010718
Positive Regulation Of Epithelial To Mesenchymal Transition
GO:0045184
Establishment Of Protein Localization
GO:0044087
Regulation Of Cellular Component Biogenesis
GO:1904748
Regulation Of Apoptotic Process Involved In Development
GO:0046907
Intracellular Transport
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0033002
Muscle Cell Proliferation
GO:0009790
Embryo Development
GO:0050790
Regulation Of Catalytic Activity
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:0045682
Regulation Of Epidermis Development
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0001568
Blood Vessel Development
GO:0046483
Heterocycle Metabolic Process
GO:0044092
Negative Regulation Of Molecular Function
GO:0051649
Establishment Of Localization In Cell
GO:0035107
Appendage Morphogenesis
GO:0034641
Cellular Nitrogen Compound Metabolic Process
GO:0060561
Apoptotic Process Involved In Morphogenesis
GO:0001525
Angiogenesis
GO:2000026
Regulation Of Multicellular Organismal Development
GO:0046782
Regulation Of Viral Transcription
GO:0031325
Positive Regulation Of Cellular Metabolic Process
GO:0033554
Cellular Response To Stress
GO:0050673
Epithelial Cell Proliferation
GO:0070727
Cellular Macromolecule Localization
GO:0009890
Negative Regulation Of Biosynthetic Process
GO:0090287
Regulation Of Cellular Response To Growth Factor Stimulus
GO:0010942
Positive Regulation Of Cell Death
GO:0048729
Tissue Morphogenesis
GO:0012501
Programmed Cell Death
GO:0002250
Adaptive Immune Response
GO:0048468
Cell Development
GO:0060512
Prostate Gland Morphogenesis
GO:0055017
Cardiac Muscle Tissue Growth
GO:0001708
Cell Fate Specification
GO:0003170
Heart Valve Development
GO:0030279
Negative Regulation Of Ossification
GO:0002437
Inflammatory Response To Antigenic Stimulus
GO:1901360
Organic Cyclic Compound Metabolic Process
GO:0030900
Forebrain Development
GO:0001942
Hair Follicle Development
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0045595
Regulation Of Cell Differentiation
GO:0016043
Cellular Component Organization
GO:0048839
Inner Ear Development
GO:1901575
Organic Substance Catabolic Process
GO:0051962
Positive Regulation Of Nervous System Development
GO:1903531
Negative Regulation Of Secretion By Cell
GO:0048638
Regulation Of Developmental Growth
GO:0003157
Endocardium Development
GO:0016477
Cell Migration
GO:0009967
Positive Regulation Of Signal Transduction
GO:1903530
Regulation Of Secretion By Cell
GO:0045070
Positive Regulation Of Viral Genome Replication
GO:0051049
Regulation Of Transport
GO:1901564
Organonitrogen Compound Metabolic Process
GO:0006952
Defense Response
GO:0010033
Response To Organic Substance
GO:0060249
Anatomical Structure Homeostasis
GO:1903900
Regulation Of Viral Life Cycle
GO:0009888
Tissue Development
GO:0006139
Nucleobase-Containing Compound Metabolic Process
GO:0060322
Head Development
GO:0010646
Regulation Of Cell Communication
GO:0009889
Regulation Of Biosynthetic Process
GO:0003206
Cardiac Chamber Morphogenesis
GO:0003179
Heart Valve Morphogenesis
GO:0120163
Negative Regulation Of Cold-Induced Thermogenesis
GO:0007492
Endoderm Development
GO:1901532
Regulation Of Hematopoietic Progenitor Cell Differentiation
GO:0072009
Nephron Epithelium Development
GO:0030030
Cell Projection Organization
GO:0008593
Regulation Of Notch Signaling Pathway
GO:0048103
Somatic Stem Cell Division
GO:0090092
Regulation Of Transmembrane Receptor Protein Serine/Threonine Kinase Signaling Pathway
GO:0060045
Positive Regulation Of Cardiac Muscle Cell Proliferation
GO:1904892
Regulation Of Receptor Signaling Pathway Via STAT
GO:0050678
Regulation Of Epithelial Cell Proliferation
GO:1905314
Semi-Lunar Valve Development
GO:0042692
Muscle Cell Differentiation
GO:0035050
Embryonic Heart Tube Development
GO:0061311
Cell Surface Receptor Signaling Pathway Involved In Heart Development
GO:0072359
Circulatory System Development
GO:0036293
Response To Decreased Oxygen Levels
GO:0030335
Positive Regulation Of Cell Migration
GO:0045667
Regulation Of Osteoblast Differentiation
GO:0048858
Cell Projection Morphogenesis
GO:0003184
Pulmonary Valve Morphogenesis
GO:0019221
Cytokine-Mediated Signaling Pathway
GO:0045920
Negative Regulation Of Exocytosis
GO:0003281
Ventricular Septum Development
GO:0045747
Positive Regulation Of Notch Signaling Pathway
GO:2000136
Regulation Of Cell Proliferation Involved In Heart Morphogenesis
GO:0071310
Cellular Response To Organic Substance
GO:0072594
Establishment Of Protein Localization To Organelle
GO:0060973
Cell Migration Involved In Heart Development
GO:0030858
Positive Regulation Of Epithelial Cell Differentiation
GO:0035108
Limb Morphogenesis
GO:0051147
Regulation Of Muscle Cell Differentiation
GO:0061008
Hepaticobiliary System Development
GO:0035914
Skeletal Muscle Cell Differentiation
GO:0007219
Notch Signaling Pathway
GO:0003209
Cardiac Atrium Morphogenesis
GO:0010557
Positive Regulation Of Macromolecule Biosynthetic Process
GO:0006915
Apoptotic Process
GO:0002460
Adaptive Immune Response Based On Somatic Recombination Of Immune Receptors Built From Immunoglobulin Superfamily Domains
GO:0019219
Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0060429
Epithelium Development
GO:0022612
Gland Morphogenesis
GO:0031328
Positive Regulation Of Cellular Biosynthetic Process
GO:0003181
Atrioventricular Valve Morphogenesis
GO:0030856
Regulation Of Epithelial Cell Differentiation
GO:0060541
Respiratory System Development
GO:1901652
Response To Peptide
GO:0043067
Regulation Of Programmed Cell Death
GO:0030163
Protein Catabolic Process
GO:0048732
Gland Development
GO:0061005
Cell Differentiation Involved In Kidney Development
GO:0003231
Cardiac Ventricle Development
GO:0002009
Morphogenesis Of An Epithelium
GO:0050769
Positive Regulation Of Neurogenesis
GO:0043588
Skin Development
GO:0030334
Regulation Of Cell Migration
GO:0048666
Neuron Development
GO:0060976
Coronary Vasculature Development
GO:0048754
Branching Morphogenesis Of An Epithelial Tube
GO:0003208
Cardiac Ventricle Morphogenesis
GO:0009057
Macromolecule Catabolic Process
GO:0048568
Embryonic Organ Development
GO:0000904
Cell Morphogenesis Involved In Differentiation
GO:0006887
Exocytosis
GO:0061326
Renal Tubule Development
GO:0090304
Nucleic Acid Metabolic Process
GO:0060219
Camera-Type Eye Photoreceptor Cell Differentiation
GO:1903053
Regulation Of Extracellular Matrix Organization
GO:0031327
Negative Regulation Of Cellular Biosynthetic Process
GO:0030178
Negative Regulation Of Wnt Signaling Pathway
GO:0048762
Mesenchymal Cell Differentiation
GO:0010614
Negative Regulation Of Cardiac Muscle Hypertrophy
GO:0010467
Gene Expression
GO:0045934
Negative Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0060043
Regulation Of Cardiac Muscle Cell Proliferation
GO:0072001
Renal System Development
GO:0060038
Cardiac Muscle Cell Proliferation
GO:0061458
Reproductive System Development
GO:0090101
Negative Regulation Of Transmembrane Receptor Protein Serine/Threonine Kinase Signaling Pathway
GO:0048562
Embryonic Organ Morphogenesis
GO:1901533
Negative Regulation Of Hematopoietic Progenitor Cell Differentiation
GO:0010720
Positive Regulation Of Cell Development
GO:0001655
Urogenital System Development
GO:0010628
Positive Regulation Of Gene Expression
GO:0048644
Muscle Organ Morphogenesis
GO:1904894
Positive Regulation Of Receptor Signaling Pathway Via STAT
GO:0045935
Positive Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:1901201
Regulation Of Extracellular Matrix Assembly
GO:0030323
Respiratory Tube Development
GO:0010243
Response To Organonitrogen Compound
GO:0090100
Positive Regulation Of Transmembrane Receptor Protein Serine/Threonine Kinase Signaling Pathway
GO:0030850
Prostate Gland Development
GO:0060841
Venous Blood Vessel Development
GO:0010558
Negative Regulation Of Macromolecule Biosynthetic Process
GO:0003230
Cardiac Atrium Development
GO:0035051
Cardiocyte Differentiation
GO:0060837
Blood Vessel Endothelial Cell Differentiation
GO:0010717
Regulation Of Epithelial To Mesenchymal Transition
GO:0072012
Glomerulus Vasculature Development
GO:0048565
Digestive Tract Development
GO:0030182
Neuron Differentiation
GO:0055006
Cardiac Cell Development
GO:0060562
Epithelial Tube Morphogenesis
GO:0071705
Nitrogen Compound Transport
GO:0042733
Embryonic Digit Morphogenesis
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0071453
Cellular Response To Oxygen Levels
GO:0048880
Sensory System Development
GO:0001944
Vasculature Development
GO:0061448
Connective Tissue Development
GO:0060251
Regulation Of Glial Cell Proliferation
GO:0010001
Glial Cell Differentiation
GO:0071702
Organic Substance Transport
GO:0003143
Embryonic Heart Tube Morphogenesis
GO:0051148
Negative Regulation Of Muscle Cell Differentiation
GO:0010468
Regulation Of Gene Expression
GO:0055021
Regulation Of Cardiac Muscle Tissue Growth
GO:0014855
Striated Muscle Cell Proliferation
GO:0006886
Intracellular Protein Transport
GO:0045668
Negative Regulation Of Osteoblast Differentiation
GO:0002064
Epithelial Cell Development
GO:0045995
Regulation Of Embryonic Development
GO:0061384
Heart Trabecula Morphogenesis
GO:0009957
Epidermal Cell Fate Specification
GO:0002040
Sprouting Angiogenesis
GO:0007507
Heart Development
GO:0060840
Artery Development
GO:0071456
Cellular Response To Hypoxia
GO:0060421
Positive Regulation Of Heart Growth
GO:0003171
Atrioventricular Valve Development
GO:1901565
Organonitrogen Compound Catabolic Process
GO:0072148
Epithelial Cell Fate Commitment
GO:0048663
Neuron Fate Commitment
GO:0055001
Muscle Cell Development
GO:0019438
Aromatic Compound Biosynthetic Process
GO:0060284
Regulation Of Cell Development
GO:0007423
Sensory Organ Development
GO:0017157
Regulation Of Exocytosis
GO:0046903
Secretion
GO:0030111
Regulation Of Wnt Signaling Pathway
GO:0045685
Regulation Of Glial Cell Differentiation
GO:0050679
Positive Regulation Of Epithelial Cell Proliferation
GO:0022008
Neurogenesis
GO:0051254
Positive Regulation Of RNA Metabolic Process
GO:0060412
Ventricular Septum Morphogenesis
GO:0006954
Inflammatory Response
GO:0050680
Negative Regulation Of Epithelial Cell Proliferation
GO:0060972
Left/Right Pattern Formation
GO:0060537
Muscle Tissue Development
GO:0072091
Regulation Of Stem Cell Proliferation
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:0010611
Regulation Of Cardiac Muscle Hypertrophy
GO:0044271
Cellular Nitrogen Compound Biosynthetic Process
GO:0035113
Embryonic Appendage Morphogenesis
GO:0008104
Protein Localization
GO:0007517
Muscle Organ Development
GO:0010721
Negative Regulation Of Cell Development
GO:0009792
Embryo Development Ending In Birth Or Egg Hatching
GO:0045664
Regulation Of Neuron Differentiation
GO:0009059
Macromolecule Biosynthetic Process
GO:1901362
Organic Cyclic Compound Biosynthetic Process
GO:0030514
Negative Regulation Of BMP Signaling Pathway
GO:0055123
Digestive System Development
GO:0032990
Cell Part Morphogenesis
GO:0090596
Sensory Organ Morphogenesis
GO:0051169
Nuclear Transport
GO:0003180
Aortic Valve Morphogenesis
GO:0030510
Regulation Of BMP Signaling Pathway
GO:0090257
Regulation Of Muscle System Process
GO:0045604
Regulation Of Epidermal Cell Differentiation
GO:0007420
Brain Development
GO:0050768
Negative Regulation Of Neurogenesis
GO:0060420
Regulation Of Heart Growth
GO:0003007
Heart Morphogenesis
GO:0007399
Nervous System Development
GO:0008544
Epidermis Development
GO:0015031
Protein Transport
GO:0055023
Positive Regulation Of Cardiac Muscle Tissue Growth
GO:0018130
Heterocycle Biosynthetic Process
GO:0001570
Vasculogenesis
GO:0007417
Central Nervous System Development
GO:0060253
Negative Regulation Of Glial Cell Proliferation
GO:0060113
Inner Ear Receptor Cell Differentiation
GO:0051252
Regulation Of RNA Metabolic Process
GO:0034097
Response To Cytokine
GO:0043086
Negative Regulation Of Catalytic Activity
GO:0060415
Muscle Tissue Morphogenesis
GO:0021915
Neural Tube Development
GO:0043068
Positive Regulation Of Programmed Cell Death
GO:0045606
Positive Regulation Of Epidermal Cell Differentiation
GO:0051960
Regulation Of Nervous System Development
GO:0060485
Mesenchyme Development
GO:0045665
Negative Regulation Of Neuron Differentiation
GO:0070986
Left/Right Axis Specification
GO:0048546
Digestive Tract Morphogenesis
GO:0030855
Epithelial Cell Differentiation
GO:0034654
Nucleobase-Containing Compound Biosynthetic Process
GO:0070167
Regulation Of Biomineral Tissue Development
GO:0009855
Determination Of Bilateral Symmetry
GO:0030324
Lung Development
GO:0048863
Stem Cell Differentiation
GO:0072132
Mesenchyme Morphogenesis
GO:0045445
Myoblast Differentiation
GO:0048514
Blood Vessel Morphogenesis
GO:0030857
Negative Regulation Of Epithelial Cell Differentiation
GO:0060173
Limb Development
GO:0051046
Regulation Of Secretion
GO:0016192
Vesicle-Mediated Transport
GO:0048873
Homeostasis Of Number Of Cells Within A Tissue
GO:0051253
Negative Regulation Of RNA Metabolic Process
GO:0001822
Kidney Development
GO:0009952
Anterior/Posterior Pattern Specification
GO:0042981
Regulation Of Apoptotic Process
GO:0014014
Negative Regulation Of Gliogenesis
GO:0014706
Striated Muscle Tissue Development
GO:0043583
Ear Development
GO:0003214
Cardiac Left Ventricle Morphogenesis
GO:0007519
Skeletal Muscle Tissue Development
GO:0003222
Ventricular Trabecula Myocardium Morphogenesis
GO:0048713
Regulation Of Oligodendrocyte Differentiation
GO:0001889
Liver Development
GO:1902680
Positive Regulation Of RNA Biosynthetic Process
GO:0048844
Artery Morphogenesis
GO:0060317
Cardiac Epithelial To Mesenchymal Transition
GO:0006913
Nucleocytoplasmic Transport
GO:0048710
Regulation Of Astrocyte Differentiation
GO:0097396
Response To Interleukin-17
GO:0030513
Positive Regulation Of BMP Signaling Pathway
GO:0048738
Cardiac Muscle Tissue Development
GO:0046530
Photoreceptor Cell Differentiation
GO:0072073
Kidney Epithelium Development
GO:0003203
Endocardial Cushion Morphogenesis
GO:0002065
Columnar/Cuboidal Epithelial Cell Differentiation
GO:0042063
Gliogenesis
GO:0031175
Neuron Projection Development
GO:0003158
Endothelium Development
GO:0009913
Epidermal Cell Differentiation
GO:0045616
Regulation Of Keratinocyte Differentiation
GO:0097659
Nucleic Acid-Templated Transcription
GO:0060039
Pericardium Development
GO:0042490
Mechanoreceptor Differentiation
GO:0007368
Determination Of Left/Right Symmetry
GO:0003177
Pulmonary Valve Development
GO:0048592
Eye Morphogenesis
GO:0035137
Hindlimb Morphogenesis
GO:0051145
Smooth Muscle Cell Differentiation
GO:0048709
Oligodendrocyte Differentiation
GO:0003197
Endocardial Cushion Development
GO:0048730
Epidermis Morphogenesis
GO:1903306
Negative Regulation Of Regulated Secretory Pathway
GO:0050767
Regulation Of Neurogenesis
GO:0090090
Negative Regulation Of Canonical Wnt Signaling Pathway
GO:0060828
Regulation Of Canonical Wnt Signaling Pathway
GO:0042491
Inner Ear Auditory Receptor Cell Differentiation
GO:0048667
Cell Morphogenesis Involved In Neuron Differentiation
GO:0060538
Skeletal Muscle Organ Development
GO:0051153
Regulation Of Striated Muscle Cell Differentiation
GO:0014015
Positive Regulation Of Gliogenesis
GO:0045687
Positive Regulation Of Glial Cell Differentiation
Cellular Component
GO:0005575
Cellular_component
GO:0110165
Cellular Anatomical Entity
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0016020
Membrane
GO:0031974
Membrane-Enclosed Lumen
GO:0005829
Cytosol
GO:0009986
Cell Surface
GO:0071944
Cell Periphery
GO:0030054
Cell Junction
GO:0031984
Organelle Subcompartment
GO:0045177
Apical Part Of Cell
GO:0005737
Cytoplasm
GO:0012505
Endomembrane System
GO:0005654
Nucleoplasm
GO:0005576
Extracellular Region
GO:0031090
Organelle Membrane
GO:0031410
Cytoplasmic Vesicle
GO:0043229
Intracellular Organelle
GO:0016324
Apical Plasma Membrane
GO:0098827
Endoplasmic Reticulum Subcompartment
GO:0042175
Nuclear Outer Membrane-Endoplasmic Reticulum Membrane Network
GO:0005794
Golgi Apparatus
GO:0098590
Plasma Membrane Region
GO:0043233
Organelle Lumen
GO:0005783
Endoplasmic Reticulum
GO:0070161
Anchoring Junction
GO:0043227
Membrane-Bounded Organelle
GO:0005886
Plasma Membrane
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0098588
Bounding Membrane Of Organelle
GO:0005789
Endoplasmic Reticulum Membrane
GO:0031982
Vesicle
GO:0070013
Intracellular Organelle Lumen
GO:0005911
Cell-Cell Junction
GO:0000139
Golgi Membrane
GO:0097708
Intracellular Vesicle
GO:0005634
Nucleus
GO:0031981
Nuclear Lumen
GO:0005912
Adherens Junction

### InterPro Domains
1
2000
IPR008297
IPR000742
IPR001881
IPR018097
IPR049883
IPR000152
IPR009030
IPR013032
IPR022362
IPR000800
IPR035993
IPR010660
IPR011656
IPR036770
IPR002110
Domain Details
IPR008297
Notch (family) [5-2000]
IPR000742
EGF-like domain (domain) [20-1426]
IPR001881
EGF-like calcium-binding domain (domain) [59-1384]
IPR018097
EGF-like calcium-binding, conserved site (conserved_site) [178-1253]
IPR049883
NOTCH1, EGF-like calcium-binding domain (domain) [178-900]
IPR000152
EGF-type aspartate/asparagine hydroxylation site (ptm) [195-1255]
IPR009030
Growth factor receptor cysteine-rich domain superfamily (homologous_superfamily) [288-1311]
IPR013032
EGF-like, conserved site (conserved_site) [344-1374]
IPR022362
Neurogenic locus notch homolog protein 1 (family) [1426-1714]
IPR000800
Notch domain (domain) [1442-1571]
IPR035993
Notch-like domain superfamily (homologous_superfamily) [1448-1561]
IPR010660
Notch, NOD domain (domain) [1566-1622]
IPR011656
Notch, NODP domain (domain) [1660-1722]
IPR036770
Ankyrin repeat-containing domain superfamily (homologous_superfamily) [1858-2000]
IPR002110
Ankyrin repeat (repeat) [1870-1980]

---
*Generated by [BioReason](https://bioreason.net)*
