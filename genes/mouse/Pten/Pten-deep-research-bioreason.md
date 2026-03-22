# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:21 PM*

---

**Organism:** Mus musculus

### Thinking Trace
I begin with the InterPro architecture. The N-terminal half is densely annotated with phosphatase core signatures: IPR029021 (Protein-tyrosine phosphatase-like homologous superfamily, residues 1–187) frames the catalytic scaffold; within it lie IPR003595 (Protein-tyrosine phosphatase, catalytic domain, residues 23–183) and IPR045101 (PTEN, phosphatase domain, residues 24–181), together defining the cysteine-dependent PTP fold. IPR000387 (Tyrosine-specific protein phosphatases domain, residues 102–173) and the embedded IPR016130 active site (Protein-tyrosine phosphatase, active site, residues 122–132) specify the canonical HCX5R nucleophile/arginine pair that executes phosphate ester hydrolysis. This catalytic block is further contextualized by IPR029023 (Tensin-type phosphatase domain, residues 14–185), which indicates a PTP-like catalytic unit often adapted for both lipid and protein substrates, and by two family-level envelopes—IPR017361 (Bifunctional phosphatidylinositol trisphosphate phosphatase/dual specificity phosphatase PTEN family, residues 1–403) and IPR051281 (Dual-specificity lipid and protein phosphatase family, residues 1–377)—which together assert dual-specificity chemistry. Downstream, the C-terminal half is dominated by membrane-targeting modules: IPR035892 (C2 domain superfamily, residues 188–349) and IPR014020 (Tensin phosphatase, C2 domain, residues 188–350). This C2 architecture confers Ca2+-modulated phospholipid binding and membrane association. The overall linear arrangement—N-terminal PTP catalytic core followed by a C2 membrane-targeting module—matches the archetypal PTEN-like arrangement that positions catalysis at membrane-proximal phosphoinositide pools.

From this architecture, the molecular function resolves as a cysteine-dependent phosphatase with dual specificity. The PTP catalytic core (IPR003595, IPR045101) and active-site motif (IPR016130) cause phosphate-ester hydrolysis on both phosphotyrosine and phosphoserine/threonine residues in proteins, and—by virtue of the PTEN family envelopes (IPR017361, IPR051281)—extend to soluble and membrane-anchored phosphoinositides. The C2 domain (IPR035892, IPR014020) targets acidic phospholipid surfaces and orients the catalytic domain toward membrane-associated substrates such as phosphatidylinositol-3,4,5-trisphosphate. Together, these features mechanistically support the molecular function formalized as GO:0005515 (the essential enzymatic capability being phosphate hydrolysis inherent to phosphatases).

The biological process follows from the chemistry and targeting. Hydrolysis of phosphatidylinositol-3,4,5-trisphosphate and tuning of downstream signaling nodes directly modulate cell-cycle checkpoints and survival pathways. The dual-specificity PTP core can dephosphorylate protein regulators that gate checkpoint transitions, while membrane-directed lipid hydrolysis dampens PI3K-driven pathways that feed into cyclin/CDK circuits. This causal chain—membrane-localized phosphoinositide turnover leading to altered kinase cascades and effector networks—places the protein in broader regulatory programs encompassed by GO:0005515 as the central enzymatic driver of signaling homeostasis.

Cellular localization emerges from the soluble catalytic core and membrane-targeting C2 domain. The absence of transmembrane segments and the soluble PTP fold support a cytosolic pool, while the C2 module recruits the enzyme to membrane surfaces. This duality explains a predominant cytoplasmic residency with dynamic membrane association, aligning with a cellular component assignment to the cytoplasm.

Mechanistically, I hypothesize that the N-terminal PTP fold performs catalysis while the C2 domain docks the enzyme at membrane-proximal phosphoinositide assemblies. There, the enzyme hydrolyzes phosphatidylinositol-3,4,5-trisphosphate to restrain AKT pathway flux, while its dual-specificity activity fine-tunes protein nodes that feed into cell-cycle control. Likely interaction partners therefore include membrane-tethered phosphoinositide complexes and checkpoint regulators; candidates include PI3K pathway components and cyclin-dependent kinase modules that operate near membrane-associated signaling hubs.

### Functional Summary
A cytoplasmic dual-specificity phosphatase that uses an N-terminal cysteine-dependent catalytic core and a C-terminal C2 membrane-targeting module to hydrolyze phosphate esters on both proteins and membrane phosphoinositides. By docking to acidic membrane surfaces and depleting signaling lipids, it dampens PI3K-driven pathways and fine-tunes checkpoint regulators, thereby coordinating cell-cycle control and survival decisions from a primarily cytoplasmic locale with dynamic membrane association.

### UniProt Summary
May be involved in cell cycle control.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0005488
Binding
GO:0003824
Catalytic Activity
GO:0016787
Hydrolase Activity
GO:0005515
Protein Binding
GO:0019899
Enzyme Binding
GO:0016788
Hydrolase Activity, Acting On Ester Bonds
GO:0019900
Kinase Binding
GO:0042578
Phosphoric Ester Hydrolase Activity
GO:0016791
Phosphatase Activity
GO:0019901
Protein Kinase Binding
GO:0052866
Phosphatidylinositol Phosphate Phosphatase Activity
GO:0034594
Phosphatidylinositol Trisphosphate Phosphatase Activity
Biological Process
GO:0008150
Biological_process
GO:0023052
Signaling
GO:0065007
Biological Regulation
GO:0050896
Response To Stimulus
GO:0022414
Reproductive Process
GO:0040007
Growth
GO:0048519
Negative Regulation Of Biological Process
GO:0048518
Positive Regulation Of Biological Process
GO:0050789
Regulation Of Biological Process
GO:0051703
Biological Process Involved In Intraspecies Interaction Between Organisms
GO:0000003
Reproduction
GO:0032501
Multicellular Organismal Process
GO:0048511
Rhythmic Process
GO:0032502
Developmental Process
GO:0009987
Cellular Process
GO:0002376
Immune System Process
GO:0048856
Anatomical Structure Development
GO:0023057
Negative Regulation Of Signaling
GO:0090130
Tissue Migration
GO:0071840
Cellular Component Organization Or Biogenesis
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0007272
Ensheathment Of Neurons
GO:0003006
Developmental Process Involved In Reproduction
GO:0048646
Anatomical Structure Formation Involved In Morphogenesis
GO:0009892
Negative Regulation Of Metabolic Process
GO:0065008
Regulation Of Biological Quality
GO:0090394
Negative Regulation Of Excitatory Postsynaptic Potential
GO:0033555
Multicellular Organismal Response To Stress
GO:0050794
Regulation Of Cellular Process
GO:0048583
Regulation Of Response To Stimulus
GO:0051716
Cellular Response To Stimulus
GO:0021700
Developmental Maturation
GO:0048523
Negative Regulation Of Cellular Process
GO:0009628
Response To Abiotic Stimulus
GO:0048869
Cellular Developmental Process
GO:0035265
Organ Growth
GO:0048584
Positive Regulation Of Response To Stimulus
GO:0019222
Regulation Of Metabolic Process
GO:0065009
Regulation Of Molecular Function
GO:0007154
Cell Communication
GO:0048522
Positive Regulation Of Cellular Process
GO:0009605
Response To External Stimulus
GO:0048589
Developmental Growth
GO:0009653
Anatomical Structure Morphogenesis
GO:0048870
Cell Motility
GO:0042221
Response To Chemical
GO:0045321
Leukocyte Activation
GO:0008283
Cell Population Proliferation
GO:0035176
Social Behavior
GO:0051241
Negative Regulation Of Multicellular Organismal Process
GO:0032504
Multicellular Organism Reproduction
GO:0007267
Cell-Cell Signaling
GO:0050793
Regulation Of Developmental Process
GO:0019098
Reproductive Behavior
GO:0002683
Negative Regulation Of Immune System Process
GO:0023051
Regulation Of Signaling
GO:0051093
Negative Regulation Of Developmental Process
GO:0007165
Signal Transduction
GO:0023056
Positive Regulation Of Signaling
GO:0007275
Multicellular Organism Development
GO:0001775
Cell Activation
GO:0051051
Negative Regulation Of Transport
GO:0032879
Regulation Of Localization
GO:0007623
Circadian Rhythm
GO:0002682
Regulation Of Immune System Process
GO:0003008
System Process
GO:0009893
Positive Regulation Of Metabolic Process
GO:0006950
Response To Stress
GO:0045926
Negative Regulation Of Growth
GO:0048585
Negative Regulation Of Response To Stimulus
GO:0040008
Regulation Of Growth
GO:0007610
Behavior
GO:0032989
Cellular Component Morphogenesis
GO:0061000
Negative Regulation Of Dendritic Spine Development
GO:0002695
Negative Regulation Of Leukocyte Activation
GO:0070570
Regulation Of Neuron Projection Regeneration
GO:0044085
Cellular Component Biogenesis
GO:0051129
Negative Regulation Of Cellular Component Organization
GO:0080134
Regulation Of Response To Stress
GO:0021542
Dentate Gyrus Development
GO:0046621
Negative Regulation Of Organ Growth
GO:0044057
Regulation Of System Process
GO:0048513
Animal Organ Development
GO:0009966
Regulation Of Signal Transduction
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0032101
Regulation Of Response To External Stimulus
GO:0048608
Reproductive Structure Development
GO:0044087
Regulation Of Cellular Component Biogenesis
GO:0007626
Locomotory Behavior
GO:0099536
Synaptic Signaling
GO:0050866
Negative Regulation Of Cell Activation
GO:0007611
Learning Or Memory
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0042391
Regulation Of Membrane Potential
GO:0022603
Regulation Of Anatomical Structure Morphogenesis
GO:0050865
Regulation Of Cell Activation
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0060998
Regulation Of Dendritic Spine Development
GO:0021766
Hippocampus Development
GO:0050790
Regulation Of Catalytic Activity
GO:0048167
Regulation Of Synaptic Plasticity
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:0044093
Positive Regulation Of Molecular Function
GO:0008366
Axon Ensheathment
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0001568
Blood Vessel Development
GO:0021537
Telencephalon Development
GO:0060341
Regulation Of Cellular Localization
GO:0008285
Negative Regulation Of Cell Population Proliferation
GO:0080135
Regulation Of Cellular Response To Stress
GO:0030534
Adult Behavior
GO:0001525
Angiogenesis
GO:2000026
Regulation Of Multicellular Organismal Development
GO:0042127
Regulation Of Cell Population Proliferation
GO:0010941
Regulation Of Cell Death
GO:0060074
Synapse Maturation
GO:0033554
Cellular Response To Stress
GO:0045596
Negative Regulation Of Cell Differentiation
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0010647
Positive Regulation Of Cell Communication
GO:0050877
Nervous System Process
GO:0099177
Regulation Of Trans-Synaptic Signaling
GO:0080090
Regulation Of Primary Metabolic Process
GO:0007622
Rhythmic Behavior
GO:0032102
Negative Regulation Of Response To External Stimulus
GO:0001666
Response To Hypoxia
GO:0009968
Negative Regulation Of Signal Transduction
GO:0010942
Positive Regulation Of Cell Death
GO:0060548
Negative Regulation Of Cell Death
GO:0048468
Cell Development
GO:0051961
Negative Regulation Of Nervous System Development
GO:0030154
Cell Differentiation
GO:0048731
System Development
GO:0070482
Response To Oxygen Levels
GO:0030155
Regulation Of Cell Adhesion
GO:0046620
Regulation Of Organ Growth
GO:0002694
Regulation Of Leukocyte Activation
GO:0050803
Regulation Of Synapse Structure Or Activity
GO:0046649
Lymphocyte Activation
GO:0035295
Tube Development
GO:0051726
Regulation Of Cell Cycle
GO:0000902
Cell Morphogenesis
GO:0009887
Animal Organ Morphogenesis
GO:0070661
Leukocyte Proliferation
GO:0007162
Negative Regulation Of Cell Adhesion
GO:0050806
Positive Regulation Of Synaptic Transmission
GO:0031641
Regulation Of Myelination
GO:0030900
Forebrain Development
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0021543
Pallium Development
GO:0045595
Regulation Of Cell Differentiation
GO:0016043
Cellular Component Organization
GO:0051128
Regulation Of Cellular Component Organization
GO:0090066
Regulation Of Anatomical Structure Size
GO:0070571
Negative Regulation Of Neuron Projection Regeneration
GO:0048638
Regulation Of Developmental Growth
GO:0008284
Positive Regulation Of Cell Population Proliferation
GO:0016477
Cell Migration
GO:0001964
Startle Response
GO:0035239
Tube Morphogenesis
GO:0009967
Positive Regulation Of Signal Transduction
GO:0010648
Negative Regulation Of Cell Communication
GO:0051049
Regulation Of Transport
GO:0060746
Parental Behavior
GO:0035556
Intracellular Signal Transduction
GO:0007617
Mating Behavior
GO:0090132
Epithelium Migration
GO:0048512
Circadian Behavior
GO:0060996
Dendritic Spine Development
GO:0031324
Negative Regulation Of Cellular Metabolic Process
GO:0048853
Forebrain Morphogenesis
GO:0009888
Tissue Development
GO:0060322
Head Development
GO:0010646
Regulation Of Cell Communication
GO:0016358
Dendrite Development
GO:0070887
Cellular Response To Chemical Stimulus
GO:0048640
Negative Regulation Of Developmental Growth
GO:0031645
Negative Regulation Of Nervous System Process
GO:1903035
Negative Regulation Of Response To Wounding
GO:0030030
Cell Projection Organization
GO:0050807
Regulation Of Synapse Organization
GO:0071453
Cellular Response To Oxygen Levels
GO:0060179
Male Mating Behavior
GO:0045475
Locomotor Rhythm
GO:0051246
Regulation Of Protein Metabolic Process
GO:0001944
Vasculature Development
GO:0010001
Glial Cell Differentiation
GO:0050678
Regulation Of Epithelial Cell Proliferation
GO:0051250
Negative Regulation Of Lymphocyte Activation
GO:0060291
Long-Term Synaptic Potentiation
GO:0055021
Regulation Of Cardiac Muscle Tissue Growth
GO:0072359
Circulatory System Development
GO:0036293
Response To Decreased Oxygen Levels
GO:0010563
Negative Regulation Of Phosphorus Metabolic Process
GO:1902533
Positive Regulation Of Intracellular Signal Transduction
GO:0022408
Negative Regulation Of Cell-Cell Adhesion
GO:0043085
Positive Regulation Of Catalytic Activity
GO:2000463
Positive Regulation Of Excitatory Postsynaptic Potential
GO:0048858
Cell Projection Morphogenesis
GO:0042113
B Cell Activation
GO:0007507
Heart Development
GO:0071456
Cellular Response To Hypoxia
GO:0043491
Protein Kinase B Signaling
GO:0046651
Lymphocyte Proliferation
GO:0031344
Regulation Of Cell Projection Organization
GO:0060284
Regulation Of Cell Development
GO:0051248
Negative Regulation Of Protein Metabolic Process
GO:0050804
Modulation Of Chemical Synaptic Transmission
GO:0048854
Brain Morphogenesis
GO:2000773
Negative Regulation Of Cellular Senescence
GO:0001667
Ameboidal-Type Cell Migration
GO:0055022
Negative Regulation Of Cardiac Muscle Tissue Growth
GO:0022008
Neurogenesis
GO:0061001
Regulation Of Dendritic Spine Morphogenesis
GO:0050770
Regulation Of Axonogenesis
GO:0050680
Negative Regulation Of Epithelial Cell Proliferation
GO:0060537
Muscle Tissue Development
GO:0070664
Negative Regulation Of Leukocyte Proliferation
GO:0044091
Membrane Biogenesis
GO:0099173
Postsynapse Organization
GO:0051338
Regulation Of Transferase Activity
GO:0031345
Negative Regulation Of Cell Projection Organization
GO:0010721
Negative Regulation Of Cell Development
GO:0034330
Cell Junction Organization
GO:0048681
Negative Regulation Of Axon Regeneration
GO:0032535
Regulation Of Cellular Component Size
GO:0010631
Epithelial Cell Migration
GO:2000772
Regulation Of Cellular Senescence
GO:0061117
Negative Regulation Of Heart Growth
GO:0043069
Negative Regulation Of Programmed Cell Death
GO:0043067
Regulation Of Programmed Cell Death
GO:0022407
Regulation Of Cell-Cell Adhesion
GO:0032990
Cell Part Morphogenesis
GO:0098815
Modulation Of Excitatory Postsynaptic Potential
GO:0048732
Gland Development
GO:0070663
Regulation Of Leukocyte Proliferation
GO:0048666
Neuron Development
GO:0022607
Cellular Component Assembly
GO:0007420
Brain Development
GO:0050768
Negative Regulation Of Neurogenesis
GO:0060420
Regulation Of Heart Growth
GO:0000904
Cell Morphogenesis Involved In Differentiation
GO:0007399
Nervous System Development
GO:0021761
Limbic System Development
GO:0031644
Regulation Of Nervous System Process
GO:0007417
Central Nervous System Development
GO:0048813
Dendrite Morphogenesis
GO:0060043
Regulation Of Cardiac Muscle Cell Proliferation
GO:0051249
Regulation Of Lymphocyte Activation
GO:0061024
Membrane Organization
GO:0050890
Cognition
GO:0061458
Reproductive System Development
GO:1903034
Regulation Of Response To Wounding
GO:0042552
Myelination
GO:0010256
Endomembrane System Organization
GO:0043068
Positive Regulation Of Programmed Cell Death
GO:2001235
Positive Regulation Of Apoptotic Signaling Pathway
GO:0021782
Glial Cell Development
GO:0001655
Urogenital System Development
GO:1902532
Negative Regulation Of Intracellular Signal Transduction
GO:0051960
Regulation Of Nervous System Development
GO:0060997
Dendritic Spine Morphogenesis
GO:2001233
Regulation Of Apoptotic Signaling Pathway
GO:0032943
Mononuclear Cell Proliferation
GO:0032291
Axon Ensheathment In Central Nervous System
GO:0050905
Neuromuscular Process
GO:0048679
Regulation Of Axon Regeneration
GO:0048514
Blood Vessel Morphogenesis
GO:0090069
Regulation Of Ribosome Biogenesis
GO:0030850
Prostate Gland Development
GO:0099537
Trans-Synaptic Signaling
GO:0051247
Positive Regulation Of Protein Metabolic Process
GO:0099172
Presynapse Organization
GO:0042110
T Cell Activation
GO:0006996
Organelle Organization
GO:0030182
Neuron Differentiation
GO:1902531
Regulation Of Intracellular Signal Transduction
GO:0051174
Regulation Of Phosphorus Metabolic Process
GO:0007416
Synapse Assembly
GO:0042981
Regulation Of Apoptotic Process
GO:0050670
Regulation Of Lymphocyte Proliferation
GO:0032944
Regulation Of Mononuclear Cell Proliferation
GO:0014706
Striated Muscle Tissue Development
GO:0120039
Plasma Membrane Bounded Cell Projection Morphogenesis
GO:0034329
Cell Junction Assembly
GO:0042100
B Cell Proliferation
GO:0032228
Regulation Of Synaptic Transmission, GABAergic
GO:0051896
Regulation Of Protein Kinase B Signaling
GO:0050672
Negative Regulation Of Lymphocyte Proliferation
GO:0050864
Regulation Of B Cell Activation
GO:0031401
Positive Regulation Of Protein Modification Process
GO:0070925
Organelle Assembly
GO:0043408
Regulation Of MAPK Cascade
GO:0043065
Positive Regulation Of Apoptotic Process
GO:0051347
Positive Regulation Of Transferase Activity
GO:0120035
Regulation Of Plasma Membrane Bounded Cell Projection Organization
GO:0048738
Cardiac Muscle Tissue Development
GO:0014003
Oligodendrocyte Development
GO:0120036
Plasma Membrane Bounded Cell Projection Organization
GO:0099084
Postsynaptic Specialization Organization
GO:0008361
Regulation Of Cell Size
GO:0042063
Gliogenesis
GO:0031175
Neuron Projection Development
GO:1903037
Regulation Of Leukocyte Cell-Cell Adhesion
GO:0050808
Synapse Organization
GO:0050868
Negative Regulation Of T Cell Activation
GO:0045936
Negative Regulation Of Phosphate Metabolic Process
GO:0021954
Central Nervous System Neuron Development
GO:0022010
Central Nervous System Myelination
GO:0099068
Postsynapse Assembly
GO:0050863
Regulation Of T Cell Activation
GO:0048709
Oligodendrocyte Differentiation
GO:0031400
Negative Regulation Of Protein Modification Process
GO:0051438
Regulation Of Ubiquitin-Protein Transferase Activity
GO:0032945
Negative Regulation Of Mononuclear Cell Proliferation
GO:0042098
T Cell Proliferation
GO:0098916
Anterograde Trans-Synaptic Signaling
GO:0050869
Negative Regulation Of B Cell Activation
GO:0071709
Membrane Assembly
GO:0010977
Negative Regulation Of Neuron Projection Development
GO:0050767
Regulation Of Neurogenesis
GO:0043410
Positive Regulation Of MAPK Cascade
GO:0048699
Generation Of Neurons
GO:1903038
Negative Regulation Of Leukocyte Cell-Cell Adhesion
GO:0048667
Cell Morphogenesis Involved In Neuron Differentiation
GO:0099175
Regulation Of Postsynapse Organization
GO:0031399
Regulation Of Protein Modification Process
GO:0021953
Central Nervous System Neuron Differentiation
GO:0043066
Negative Regulation Of Apoptotic Process
GO:0043542
Endothelial Cell Migration
GO:0019220
Regulation Of Phosphate Metabolic Process
GO:0051898
Negative Regulation Of Protein Kinase B Signaling
GO:0036294
Cellular Response To Decreased Oxygen Levels
GO:0050771
Negative Regulation Of Axonogenesis
GO:0097061
Dendritic Spine Organization
GO:0007009
Plasma Membrane Organization
GO:0099054
Presynapse Assembly
GO:0070374
Positive Regulation Of ERK1 And ERK2 Cascade
GO:2000106
Regulation Of Leukocyte Apoptotic Process
GO:0048812
Neuron Projection Morphogenesis
GO:0098698
Postsynaptic Specialization Assembly
GO:0061564
Axon Development
GO:0030888
Regulation Of B Cell Proliferation
GO:0010975
Regulation Of Neuron Projection Development
GO:0021955
Central Nervous System Neuron Axonogenesis
GO:1903320
Regulation Of Protein Modification By Small Protein Conjugation Or Removal
GO:0106027
Neuron Projection Organization
GO:0001932
Regulation Of Protein Phosphorylation
GO:0042326
Negative Regulation Of Phosphorylation
GO:1904861
Excitatory Synapse Assembly
GO:1903322
Positive Regulation Of Protein Modification By Small Protein Conjugation Or Removal
GO:0097106
Postsynaptic Density Organization
GO:0051443
Positive Regulation Of Ubiquitin-Protein Transferase Activity
GO:0007409
Axonogenesis
GO:0070372
Regulation Of ERK1 And ERK2 Cascade
GO:0042325
Regulation Of Phosphorylation
GO:0042130
Negative Regulation Of T Cell Proliferation
GO:0001933
Negative Regulation Of Protein Phosphorylation
GO:0007268
Chemical Synaptic Transmission
GO:0030889
Negative Regulation Of B Cell Proliferation
GO:0033032
Regulation Of Myeloid Cell Apoptotic Process
GO:0045792
Negative Regulation Of Cell Size
GO:0042129
Regulation Of T Cell Proliferation
GO:1904666
Regulation Of Ubiquitin Protein Ligase Activity
GO:0070228
Regulation Of Lymphocyte Apoptotic Process
GO:0031398
Positive Regulation Of Protein Ubiquitination
GO:0031396
Regulation Of Protein Ubiquitination
GO:0002902
Regulation Of B Cell Apoptotic Process
Cellular Component
GO:0005575
Cellular_component
GO:0110165
Cellular Anatomical Entity
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0043218
Compact Myelin
GO:0042995
Cell Projection
GO:0005737
Cytoplasm
GO:0043209
Myelin Sheath
GO:0120025
Plasma Membrane Bounded Cell Projection
GO:0043229
Intracellular Organelle
GO:0043227
Membrane-Bounded Organelle
GO:0043005
Neuron Projection
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0005634
Nucleus

### InterPro Domains
1
403
IPR029021
IPR017361
IPR051281
IPR029023
IPR003595
IPR045101
IPR000387
IPR016130
IPR035892
IPR014020
Domain Details
IPR029021
Protein-tyrosine phosphatase-like (homologous_superfamily) [1-187]
IPR017361
Bifunctional phosphatidylinositol trisphosphate phosphatase/dual specificity phosphatase PTEN (family) [1-403]
IPR051281
Dual-specificity lipid and protein phosphatase (family) [1-377]
IPR029023
Tensin-type phosphatase domain (domain) [14-185]
IPR003595
Protein-tyrosine phosphatase, catalytic (domain) [23-183]
IPR045101
PTEN, phosphatase domain (domain) [24-181]
IPR000387
Tyrosine-specific protein phosphatases domain (domain) [102-173]
IPR016130
Protein-tyrosine phosphatase, active site (active_site) [122-132]
IPR035892
C2 domain superfamily (homologous_superfamily) [188-349]
IPR014020
Tensin phosphatase, C2 domain (domain) [188-350]

---
*Generated by [BioReason](https://bioreason.net)*
