# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:23 PM*

---

**Organism:** Mus musculus

### Thinking Trace
I begin with the InterPro architecture. The sequence is saturated with Bcl-2 family signatures: IPR013278 (Apoptosis regulator, Bcl-2 family, residues 1–218), IPR004725 (Apoptosis regulator, Bcl-2/Bcl-X family, residues 4–236), IPR026298 (Bcl-2 family, residues 5–202), and IPR036834 (Bcl-2-like superfamily, residues 6–220). These overlapping family/superfamily assignments establish a canonical Bcl-2 fold—a multi-helix bundle that binds and neutralizes pro-apoptotic partners. The N-terminus carries IPR003093 (BH4 domain, residues 7–33) and its conserved site IPR020731 (BH4 motif, residues 10–30), followed by a central BH3/BH1/BH2/BHx module array: IPR020728 (BH3 motif conserved site, residues 90–104) defines the primary ligand-binding groove; IPR020717 (BH1 motif conserved site, residues 134–152) and IPR020726 (BH2 motif conserved site, residues 185–196) complete the core binding scaffold; IPR046371 (Bcl-2 homology regions 1–3 domain, residues 94–192) demarcates the structured BH1–BH3 core. The C-terminal region is reinforced by IPR002475 (Bcl2-like family, residues 94–194), consolidating the fold from the central bundle outward. The ordered BH4–BH3–BH1–BH2 architecture is diagnostic of anti-apoptotic Bcl-2 proteins that assemble and regulate protein complexes through BH3-groove recognition.

This BH-domain architecture dictates molecular function. The BH3-binding groove and conserved BH1–BH2 surfaces cause tight, selective protein–protein interactions with Bcl-2 family partners and other apoptosis regulators. Thus, the primary molecular activity is protein binding (GO:0005515), executed by a multi-surface helical scaffold that sequesters BH3-only activators and effector proteins.

From this binding mechanism, the biological process follows. By capturing BH3-only initiators and stabilizing anti-apoptotic assemblies, the protein suppresses mitochondrial outer membrane permeabilization and downstream caspase activation. This places it squarely in the regulation of apoptosis, most parsimoniously the negative regulation of apoptotic pathways that preserve cell viability under stress.

Cellular localization is inferred from function and fold. Anti-apoptotic Bcl-2 scaffolds operate where mitochondrial outer membrane permeabilization is controlled and where cytoplasmic signaling complexes assemble. The absence of transmembrane domains and the reliance on dynamic protein assemblies support a soluble distribution with peripheral association to membranes. This aligns with a cytoplasmic residence (GO:0005737), consistent with the need to intercept pro-apoptotic factors before they engage mitochondria.

Mechanistically, the BH4 domain at residues 7–33 stabilizes the anti-apoptotic conformation and tunes partner affinity, while the BH1–BH3 core (residues ~94–192) forms the canonical hydrophobic groove that captures BH3 helices. This causes the protein to titrate and neutralize BH3-only activators and to stabilize effector assemblies. I therefore hypothesize interactions with pro-apoptotic Bcl-2 family members and their regulators—particularly BH3-only proteins and effector assemblies—forming a cytoplasmic checkpoint that restrains mitochondrial apoptosis pathways.

### Functional Summary
A cytoplasmic apoptosis regulator that uses a conserved Bcl-2 fold and multiple homology regions to bind and neutralize pro-apoptotic partners, thereby preserving cell viability. Its N-terminal regulatory module and central helical core assemble high-affinity protein complexes that sequester BH3-only activators and stabilize anti-apoptotic assemblies upstream of mitochondrial permeabilization. Operating as a soluble scaffold that dynamically associates with cytoplasmic signaling hubs, it restrains apoptotic execution by controlling partner availability and complex formation.

### UniProt Summary
May be involved in apoptosis.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0005488
Binding
GO:0005515
Protein Binding
GO:0019899
Enzyme Binding
GO:0019902
Phosphatase Binding
GO:0019903
Protein Phosphatase Binding
GO:0051721
Protein Phosphatase 2A Binding
Biological Process
GO:0008150
Biological_process
GO:0051179
Localization
GO:0023052
Signaling
GO:0065007
Biological Regulation
GO:0050896
Response To Stimulus
GO:0043473
Pigmentation
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
GO:0002376
Immune System Process
GO:0019953
Sexual Reproduction
GO:0051641
Cellular Localization
GO:0048856
Anatomical Structure Development
GO:0023057
Negative Regulation Of Signaling
GO:0042303
Molting Cycle
GO:0022402
Cell Cycle Process
GO:0051240
Positive Regulation Of Multicellular Organismal Process
GO:0071840
Cellular Component Organization Or Biogenesis
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0019748
Secondary Metabolic Process
GO:0003006
Developmental Process Involved In Reproduction
GO:0048871
Multicellular Organismal-Level Homeostasis
GO:0009892
Negative Regulation Of Metabolic Process
GO:0065008
Regulation Of Biological Quality
GO:0019725
Cellular Homeostasis
GO:0022412
Cellular Process Involved In Reproduction In Multicellular Organism
GO:0033555
Multicellular Organismal Response To Stress
GO:0033059
Cellular Pigmentation
GO:0050794
Regulation Of Cellular Process
GO:0048583
Regulation Of Response To Stimulus
GO:0051716
Cellular Response To Stimulus
GO:0021700
Developmental Maturation
GO:0001776
Leukocyte Homeostasis
GO:0048523
Negative Regulation Of Cellular Process
GO:0040012
Regulation Of Locomotion
GO:0048869
Cellular Developmental Process
GO:0009628
Response To Abiotic Stimulus
GO:0035265
Organ Growth
GO:0019222
Regulation Of Metabolic Process
GO:0051234
Establishment Of Localization
GO:0022404
Molting Cycle Process
GO:0001503
Ossification
GO:0065009
Regulation Of Molecular Function
GO:0030029
Actin Filament-Based Process
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
GO:0042221
Response To Chemical
GO:0048870
Cell Motility
GO:0055085
Transmembrane Transport
GO:0045321
Leukocyte Activation
GO:0008283
Cell Population Proliferation
GO:0042440
Pigment Metabolic Process
GO:0006807
Nitrogen Compound Metabolic Process
GO:0051241
Negative Regulation Of Multicellular Organismal Process
GO:0032504
Multicellular Organism Reproduction
GO:0045927
Positive Regulation Of Growth
GO:0009791
Post-Embryonic Development
GO:0050793
Regulation Of Developmental Process
GO:0009719
Response To Endogenous Stimulus
GO:0008219
Cell Death
GO:0040017
Positive Regulation Of Locomotion
GO:0040013
Negative Regulation Of Locomotion
GO:0048087
Positive Regulation Of Developmental Pigmentation
GO:0023051
Regulation Of Signaling
GO:0051093
Negative Regulation Of Developmental Process
GO:0048066
Developmental Pigmentation
GO:0007165
Signal Transduction
GO:0001775
Cell Activation
GO:0007275
Multicellular Organism Development
GO:0051051
Negative Regulation Of Transport
GO:0007610
Behavior
GO:0007155
Cell Adhesion
GO:0032879
Regulation Of Localization
GO:0007049
Cell Cycle
GO:0071704
Organic Substance Metabolic Process
GO:0045058
T Cell Selection
GO:0003008
System Process
GO:0048878
Chemical Homeostasis
GO:0044237
Cellular Metabolic Process
GO:0002520
Immune System Development
GO:0009893
Positive Regulation Of Metabolic Process
GO:0120305
Regulation Of Pigmentation
GO:0050792
Regulation Of Viral Process
GO:0006950
Response To Stress
GO:0045926
Negative Regulation Of Growth
GO:0001763
Morphogenesis Of A Branching Structure
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
GO:0032989
Cellular Component Morphogenesis
GO:0001101
Response To Acid Chemical
GO:0042633
Hair Cycle
GO:0044085
Cellular Component Biogenesis
GO:2000145
Regulation Of Cell Motility
GO:0072593
Reactive Oxygen Species Metabolic Process
GO:0009314
Response To Radiation
GO:0048513
Animal Organ Development
GO:0021548
Pons Development
GO:0009966
Regulation Of Signal Transduction
GO:0002209
Behavioral Defense Response
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0032101
Regulation Of Response To External Stimulus
GO:0006725
Cellular Aromatic Compound Metabolic Process
GO:0034220
Monoatomic Ion Transmembrane Transport
GO:0010948
Negative Regulation Of Cell Cycle Process
GO:0009725
Response To Hormone
GO:0055082
Intracellular Chemical Homeostasis
GO:0010035
Response To Inorganic Substance
GO:0046907
Intracellular Transport
GO:0043368
Positive T Cell Selection
GO:0042391
Regulation Of Membrane Potential
GO:0045786
Negative Regulation Of Cell Cycle
GO:0031668
Cellular Response To Extracellular Stimulus
GO:0072006
Nephron Development
GO:0010564
Regulation Of Cell Cycle Process
GO:0006582
Melanin Metabolic Process
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0090559
Regulation Of Membrane Permeability
GO:0045597
Positive Regulation Of Cell Differentiation
GO:0050790
Regulation Of Catalytic Activity
GO:0007281
Germ Cell Development
GO:0044093
Positive Regulation Of Molecular Function
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:1901863
Positive Regulation Of Muscle Tissue Development
GO:0060341
Regulation Of Cellular Localization
GO:0008285
Negative Regulation Of Cell Population Proliferation
GO:0019538
Protein Metabolic Process
GO:0001558
Regulation Of Cell Growth
GO:0030902
Hindbrain Development
GO:0051649
Establishment Of Localization In Cell
GO:1901700
Response To Oxygen-Containing Compound
GO:0031647
Regulation Of Protein Stability
GO:0048070
Regulation Of Developmental Pigmentation
GO:0048639
Positive Regulation Of Developmental Growth
GO:0043170
Macromolecule Metabolic Process
GO:2000147
Positive Regulation Of Cell Motility
GO:0048872
Homeostasis Of Number Of Cells
GO:0061061
Muscle Structure Development
GO:0042127
Regulation Of Cell Population Proliferation
GO:0010941
Regulation Of Cell Death
GO:0042594
Response To Starvation
GO:1901698
Response To Nitrogen Compound
GO:0040014
Regulation Of Multicellular Organism Growth
GO:0031325
Positive Regulation Of Cellular Metabolic Process
GO:0033554
Cellular Response To Stress
GO:0006810
Transport
GO:0043271
Negative Regulation Of Monoatomic Ion Transport
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0009895
Negative Regulation Of Catabolic Process
GO:0001541
Ovarian Follicle Development
GO:0022405
Hair Cycle Process
GO:0080090
Regulation Of Primary Metabolic Process
GO:0046661
Male Sex Differentiation
GO:1901861
Regulation Of Muscle Tissue Development
GO:0040018
Positive Regulation Of Multicellular Organism Growth
GO:0002260
Lymphocyte Homeostasis
GO:0001666
Response To Hypoxia
GO:0009968
Negative Regulation Of Signal Transduction
GO:0045069
Regulation Of Viral Genome Replication
GO:0012501
Programmed Cell Death
GO:0048729
Tissue Morphogenesis
GO:0060548
Negative Regulation Of Cell Death
GO:0048468
Cell Development
GO:0009410
Response To Xenobiotic Stimulus
GO:0030154
Cell Differentiation
GO:0098660
Inorganic Ion Transmembrane Transport
GO:0048731
System Development
GO:0070482
Response To Oxygen Levels
GO:0030155
Regulation Of Cell Adhesion
GO:0003014
Renal System Process
GO:0045137
Development Of Primary Sexual Characteristics
GO:0030279
Negative Regulation Of Ossification
GO:0046649
Lymphocyte Activation
GO:0070997
Neuron Death
GO:0006793
Phosphorus Metabolic Process
GO:0071695
Anatomical Structure Maturation
GO:0034763
Negative Regulation Of Transmembrane Transport
GO:0035295
Tube Development
GO:0051726
Regulation Of Cell Cycle
GO:0000902
Cell Morphogenesis
GO:0009894
Regulation Of Catabolic Process
GO:0046668
Regulation Of Retinal Cell Programmed Cell Death
GO:0009887
Animal Organ Morphogenesis
GO:1901360
Organic Cyclic Compound Metabolic Process
GO:0007204
Positive Regulation Of Cytosolic Calcium Ion Concentration
GO:0048469
Cell Maturation
GO:0097190
Apoptotic Signaling Pathway
GO:0030308
Negative Regulation Of Cell Growth
GO:0051481
Negative Regulation Of Cytosolic Calcium Ion Concentration
GO:0072028
Nephron Morphogenesis
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0010623
Programmed Cell Death Involved In Cell Development
GO:0001942
Hair Follicle Development
GO:0045595
Regulation Of Cell Differentiation
GO:0016043
Cellular Component Organization
GO:0007166
Cell Surface Receptor Signaling Pathway
GO:0009994
Oocyte Differentiation
GO:0007548
Sex Differentiation
GO:0048753
Pigment Granule Organization
GO:0051128
Regulation Of Cellular Component Organization
GO:0048608
Reproductive Structure Development
GO:0071496
Cellular Response To External Stimulus
GO:0030278
Regulation Of Ossification
GO:0031589
Cell-Substrate Adhesion
GO:0048638
Regulation Of Developmental Growth
GO:0008284
Positive Regulation Of Cell Population Proliferation
GO:0016477
Cell Migration
GO:2000146
Negative Regulation Of Cell Motility
GO:0035239
Tube Morphogenesis
GO:0046660
Female Sex Differentiation
GO:0050801
Monoatomic Ion Homeostasis
GO:0007276
Gamete Generation
GO:1901615
Organic Hydroxy Compound Metabolic Process
GO:0010648
Negative Regulation Of Cell Communication
GO:0051049
Regulation Of Transport
GO:1901564
Organonitrogen Compound Metabolic Process
GO:1903047
Mitotic Cell Cycle Process
GO:0035556
Intracellular Signal Transduction
GO:0009611
Response To Wounding
GO:0098609
Cell-Cell Adhesion
GO:0006979
Response To Oxidative Stress
GO:0031069
Hair Follicle Morphogenesis
GO:0009636
Response To Toxic Substance
GO:0034762
Regulation Of Transmembrane Transport
GO:0006952
Defense Response
GO:0061138
Morphogenesis Of A Branching Epithelium
GO:0098771
Inorganic Ion Homeostasis
GO:0042596
Fear Response
GO:0036473
Cell Death In Response To Oxidative Stress
GO:0048857
Neural Nucleus Development
GO:0031324
Negative Regulation Of Cellular Metabolic Process
GO:0022037
Metencephalon Development
GO:0030036
Actin Cytoskeleton Organization
GO:0038034
Signal Transduction In Absence Of Ligand
GO:0010033
Response To Organic Substance
GO:0060249
Anatomical Structure Homeostasis
GO:0009991
Response To Extracellular Stimulus
GO:0045165
Cell Fate Commitment
GO:1903900
Regulation Of Viral Life Cycle
GO:0009888
Tissue Development
GO:0060322
Head Development
GO:0010646
Regulation Of Cell Communication
GO:0070887
Cellular Response To Chemical Stimulus
GO:0010522
Regulation Of Calcium Ion Transport Into Cytosol
GO:0009889
Regulation Of Biosynthetic Process
GO:0044770
Cell Cycle Phase Transition
GO:0050931
Pigment Cell Differentiation
GO:0032835
Glomerulus Development
GO:0001894
Tissue Homeostasis
GO:0048534
Hematopoietic Or Lymphoid Organ Development
GO:0031099
Regeneration
GO:0000278
Mitotic Cell Cycle
GO:0002931
Response To Ischemia
GO:0060562
Epithelial Tube Morphogenesis
GO:0072009
Nephron Epithelium Development
GO:0030030
Cell Projection Organization
GO:0002360
T Cell Lineage Commitment
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0071453
Cellular Response To Oxygen Levels
GO:0051246
Regulation Of Protein Metabolic Process
GO:0044843
Cell Cycle G1/S Phase Transition
GO:0048880
Sensory System Development
GO:2000378
Negative Regulation Of Reactive Oxygen Species Metabolic Process
GO:0048545
Response To Steroid Hormone
GO:0008406
Gonad Development
GO:0030318
Melanocyte Differentiation
GO:0001782
B Cell Homeostasis
GO:0046546
Development Of Primary Male Sexual Characteristics
GO:0031102
Neuron Projection Regeneration
GO:0051881
Regulation Of Mitochondrial Membrane Potential
GO:0060993
Kidney Morphogenesis
GO:0048538
Thymus Development
GO:0010468
Regulation Of Gene Expression
GO:0018958
Phenol-Containing Compound Metabolic Process
GO:0007160
Cell-Matrix Adhesion
GO:1903429
Regulation Of Cell Maturation
GO:0043412
Macromolecule Modification
GO:0010507
Negative Regulation Of Autophagy
GO:0042692
Muscle Cell Differentiation
GO:0048599
Oocyte Development
GO:0036293
Response To Decreased Oxygen Levels
GO:0045930
Negative Regulation Of Mitotic Cell Cycle
GO:0030335
Positive Regulation Of Cell Migration
GO:0097193
Intrinsic Apoptotic Signaling Pathway
GO:0072164
Mesonephric Tubule Development
GO:0002244
Hematopoietic Progenitor Cell Differentiation
GO:0043085
Positive Regulation Of Catalytic Activity
GO:0048858
Cell Projection Morphogenesis
GO:0042113
B Cell Activation
GO:0007015
Actin Filament Organization
GO:0006839
Mitochondrial Transport
GO:0071456
Cellular Response To Hypoxia
GO:0009416
Response To Light Stimulus
GO:0097192
Extrinsic Apoptotic Signaling Pathway In Absence Of Ligand
GO:0002521
Leukocyte Differentiation
GO:2000377
Regulation Of Reactive Oxygen Species Metabolic Process
GO:0006974
Cellular Response To DNA Damage Stimulus
GO:0071310
Cellular Response To Organic Substance
GO:0055001
Muscle Cell Development
GO:0062197
Cellular Response To Chemical Stress
GO:0034765
Regulation Of Monoatomic Ion Transmembrane Transport
GO:0060284
Regulation Of Cell Development
GO:0007423
Sensory Organ Development
GO:0048477
Oogenesis
GO:0010506
Regulation Of Autophagy
GO:1901214
Regulation Of Neuron Death
GO:2001234
Negative Regulation Of Apoptotic Signaling Pathway
GO:0032880
Regulation Of Protein Localization
GO:0006873
Intracellular Monoatomic Ion Homeostasis
GO:0051147
Regulation Of Muscle Cell Differentiation
GO:0043369
CD4-Positive Or CD8-Positive, Alpha-Beta T Cell Lineage Commitment
GO:0036211
Protein Modification Process
GO:0022008
Neurogenesis
GO:0098662
Inorganic Cation Transmembrane Transport
GO:0051402
Neuron Apoptotic Process
GO:0001662
Behavioral Fear Response
GO:0033993
Response To Lipid
GO:0071702
Organic Substance Transport
GO:0060537
Muscle Tissue Development
GO:0006915
Apoptotic Process
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:0043029
T Cell Homeostasis
GO:0033688
Regulation Of Osteoblast Proliferation
GO:0097191
Extrinsic Apoptotic Signaling Pathway
GO:0042542
Response To Hydrogen Peroxide
GO:0007517
Muscle Organ Development
GO:0060429
Epithelium Development
GO:0034330
Cell Junction Organization
GO:0022612
Gland Morphogenesis
GO:0031669
Cellular Response To Nutrient Levels
GO:0097435
Supramolecular Fiber Organization
GO:0000302
Response To Reactive Oxygen Species
GO:1901988
Negative Regulation Of Cell Cycle Phase Transition
GO:0034599
Cellular Response To Oxidative Stress
GO:0098655
Monoatomic Cation Transmembrane Transport
GO:0045664
Regulation Of Neuron Differentiation
GO:0048864
Stem Cell Development
GO:0007346
Regulation Of Mitotic Cell Cycle
GO:0055123
Digestive System Development
GO:0043069
Negative Regulation Of Programmed Cell Death
GO:0043067
Regulation Of Programmed Cell Death
GO:0010810
Regulation Of Cell-Substrate Adhesion
GO:0031330
Negative Regulation Of Cellular Catabolic Process
GO:0032990
Cell Part Morphogenesis
GO:0072088
Nephron Epithelium Morphogenesis
GO:0048732
Gland Development
GO:0090596
Sensory Organ Morphogenesis
GO:0002009
Morphogenesis Of An Epithelium
GO:0043588
Skin Development
GO:0030334
Regulation Of Cell Migration
GO:0048536
Spleen Development
GO:0030098
Lymphocyte Differentiation
GO:0048666
Neuron Development
GO:0048754
Branching Morphogenesis Of An Epithelial Tube
GO:0022607
Cellular Component Assembly
GO:0007420
Brain Development
GO:0048643
Positive Regulation Of Skeletal Muscle Tissue Development
GO:0000904
Cell Morphogenesis Involved In Differentiation
GO:0061326
Renal Tubule Development
GO:0048641
Regulation Of Skeletal Muscle Tissue Development
GO:0007399
Nervous System Development
GO:0034766
Negative Regulation Of Monoatomic Ion Transmembrane Transport
GO:0007292
Female Gamete Generation
GO:0008544
Epidermis Development
GO:0031667
Response To Nutrient Levels
GO:0007417
Central Nervous System Development
GO:1903431
Positive Regulation Of Cell Maturation
GO:0048762
Mesenchymal Cell Differentiation
GO:0010212
Response To Ionizing Radiation
GO:0001836
Release Of Cytochrome C From Mitochondria
GO:0014812
Muscle Cell Migration
GO:0061024
Membrane Organization
GO:0072001
Renal System Development
GO:0030097
Hemopoiesis
GO:0061458
Reproductive System Development
GO:0034097
Response To Cytokine
GO:1901215
Negative Regulation Of Neuron Death
GO:0042551
Neuron Maturation
GO:0043200
Response To Amino Acid
GO:0010562
Positive Regulation Of Phosphorus Metabolic Process
GO:0009267
Cellular Response To Starvation
GO:0010720
Positive Regulation Of Cell Development
GO:0006796
Phosphate-Containing Compound Metabolic Process
GO:0060485
Mesenchyme Development
GO:1903018
Regulation Of Glycoprotein Metabolic Process
GO:2001233
Regulation Of Apoptotic Signaling Pathway
GO:0048546
Digestive Tract Morphogenesis
GO:0006811
Monoatomic Ion Transport
GO:0032104
Regulation Of Response To Extracellular Stimulus
GO:0055074
Calcium Ion Homeostasis
GO:0030336
Negative Regulation Of Cell Migration
GO:0048678
Response To Axon Injury
GO:0051149
Positive Regulation Of Muscle Cell Differentiation
GO:0044772
Mitotic Cell Cycle Phase Transition
GO:0046902
Regulation Of Mitochondrial Membrane Permeability
GO:0048863
Stem Cell Differentiation
GO:0008631
Intrinsic Apoptotic Signaling Pathway In Response To Oxidative Stress
GO:0055080
Monoatomic Cation Homeostasis
GO:0010243
Response To Organonitrogen Compound
GO:0046545
Development Of Primary Female Sexual Characteristics
GO:1901987
Regulation Of Cell Cycle Phase Transition
GO:0060402
Calcium Ion Transport Into Cytosol
GO:0051247
Positive Regulation Of Protein Metabolic Process
GO:0042110
T Cell Activation
GO:0051926
Negative Regulation Of Calcium Ion Transport
GO:0014070
Response To Organic Cyclic Compound
GO:0048873
Homeostasis Of Number Of Cells Within A Tissue
GO:0043269
Regulation Of Monoatomic Ion Transport
GO:0031329
Regulation Of Cellular Catabolic Process
GO:0006996
Organelle Organization
GO:0001822
Kidney Development
GO:0048565
Digestive Tract Development
GO:0030182
Neuron Differentiation
GO:0051174
Regulation Of Phosphorus Metabolic Process
GO:0072080
Nephron Tubule Development
GO:0007005
Mitochondrion Organization
GO:0042981
Regulation Of Apoptotic Process
GO:0008585
Female Gonad Development
GO:0001823
Mesonephros Development
GO:0031960
Response To Corticosteroid
GO:0016050
Vesicle Organization
GO:0045937
Positive Regulation Of Phosphate Metabolic Process
GO:0043583
Ear Development
GO:0001952
Regulation Of Cell-Matrix Adhesion
GO:0120039
Plasma Membrane Bounded Cell Projection Morphogenesis
GO:0098773
Skin Epidermis Development
GO:0043523
Regulation Of Neuron Apoptotic Process
GO:0018193
Peptidyl-Amino Acid Modification
GO:0034329
Cell Junction Assembly
GO:0016310
Phosphorylation
GO:0030003
Intracellular Monoatomic Cation Homeostasis
GO:0007519
Skeletal Muscle Tissue Development
GO:0061333
Renal Tubule Morphogenesis
GO:0014041
Regulation Of Neuron Maturation
GO:0001658
Branching Involved In Ureteric Bud Morphogenesis
GO:0008630
Intrinsic Apoptotic Signaling Pathway In Response To DNA Damage
GO:0043524
Negative Regulation Of Neuron Apoptotic Process
GO:2000112
Regulation Of Cellular Macromolecule Biosynthetic Process
GO:1903170
Negative Regulation Of Calcium Ion Transmembrane Transport
GO:1904062
Regulation Of Monoatomic Cation Transmembrane Transport
GO:0042149
Cellular Response To Glucose Starvation
GO:0006874
Intracellular Calcium Ion Homeostasis
GO:1904019
Epithelial Cell Apoptotic Process
GO:0031401
Positive Regulation Of Protein Modification Process
GO:0014911
Positive Regulation Of Smooth Muscle Cell Migration
GO:0016311
Dephosphorylation
GO:0014042
Positive Regulation Of Neuron Maturation
GO:0072073
Kidney Epithelium Development
GO:0120036
Plasma Membrane Bounded Cell Projection Organization
GO:1904063
Negative Regulation Of Cation Transmembrane Transport
GO:0014910
Regulation Of Smooth Muscle Cell Migration
GO:0010332
Response To Gamma Radiation
GO:0070588
Calcium Ion Transmembrane Transport
GO:0008584
Male Gonad Development
GO:0032107
Regulation Of Response To Nutrient Levels
GO:0031175
Neuron Projection Development
GO:0002363
Alpha-Beta T Cell Lineage Commitment
GO:0048041
Focal Adhesion Assembly
GO:1902807
Negative Regulation Of Cell Cycle G1/S Phase Transition
GO:0033028
Myeloid Cell Apoptotic Process
GO:0072078
Nephron Tubule Morphogenesis
GO:0046631
Alpha-Beta T Cell Activation
GO:0048592
Eye Morphogenesis
GO:0006812
Monoatomic Cation Transport
GO:0008637
Apoptotic Mitochondrial Changes
GO:0001656
Metanephros Development
GO:0006470
Protein Dephosphorylation
GO:0010959
Regulation Of Metal Ion Transport
GO:0150063
Visual System Development
GO:0010559
Regulation Of Glycoprotein Biosynthetic Process
GO:0007010
Cytoskeleton Organization
GO:0048730
Epidermis Morphogenesis
GO:0000082
G1/S Transition Of Mitotic Cell Cycle
GO:1903131
Mononuclear Cell Differentiation
GO:0009411
Response To UV
GO:0001657
Ureteric Bud Development
GO:0048699
Generation Of Neurons
GO:0007006
Mitochondrial Membrane Organization
GO:0072171
Mesonephric Tubule Morphogenesis
GO:0048667
Cell Morphogenesis Involved In Neuron Differentiation
GO:0001654
Eye Development
GO:0031399
Regulation Of Protein Modification Process
GO:0030217
T Cell Differentiation
GO:0014909
Smooth Muscle Cell Migration
GO:1901991
Negative Regulation Of Mitotic Cell Cycle Phase Transition
GO:0060218
Hematopoietic Stem Cell Differentiation
GO:0060538
Skeletal Muscle Organ Development
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
GO:0005829
Cytosol
GO:0031984
Organelle Subcompartment
GO:0043209
Myelin Sheath
GO:0031975
Envelope
GO:0005737
Cytoplasm
GO:0012505
Endomembrane System
GO:0031090
Organelle Membrane
GO:0031967
Organelle Envelope
GO:0043229
Intracellular Organelle
GO:0098827
Endoplasmic Reticulum Subcompartment
GO:0042175
Nuclear Outer Membrane-Endoplasmic Reticulum Membrane Network
GO:0005739
Mitochondrion
GO:0005783
Endoplasmic Reticulum
GO:0005635
Nuclear Envelope
GO:0043227
Membrane-Bounded Organelle
GO:0031965
Nuclear Membrane
GO:0005740
Mitochondrial Envelope
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0005789
Endoplasmic Reticulum Membrane
GO:0031966
Mitochondrial Membrane
GO:0005634
Nucleus

### InterPro Domains
1
236
IPR013278
IPR004725
IPR026298
IPR036834
IPR003093
IPR020731
IPR020728
IPR002475
IPR046371
IPR020717
IPR020726
Domain Details
IPR013278
Apoptosis regulator, Bcl-2 (family) [1-218]
IPR004725
Apoptosis regulator, Bcl-2/ BclX (family) [4-236]
IPR026298
Bcl-2 family (family) [5-202]
IPR036834
Bcl-2-like superfamily (homologous_superfamily) [6-220]
IPR003093
Apoptosis regulator, Bcl-2 protein, BH4 (domain) [7-33]
IPR020731
Apoptosis regulator, Bcl-2, BH4 motif, conserved site (conserved_site) [10-30]
IPR020728
Apoptosis regulator, Bcl-2, BH3 motif, conserved site (conserved_site) [90-104]
IPR002475
Bcl2-like (family) [94-194]
IPR046371
Bcl-2, Bcl-2 homology region 1-3 (domain) [94-192]
IPR020717
Apoptosis regulator, Bcl-2, BH1 motif, conserved site (conserved_site) [134-152]
IPR020726
Apoptosis regulator, Bcl-2, BH2 motif, conserved site (conserved_site) [185-196]

---
*Generated by [BioReason](https://bioreason.net)*
