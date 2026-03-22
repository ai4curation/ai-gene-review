# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:12 PM*

---

**Organism:** Homo sapiens

### Thinking Trace
I begin with the InterPro architecture and its order along the polypeptide. The N-terminus carries IPR013872 (p53, transactivation domain, residues 6–30) followed by IPR040926 (transactivation domain 2, residues 35–59). These tandem activation modules precede a central DNA-recognition core: IPR011615 (p53, DNA-binding domain, residues 100–288) sits within two overlapping superfamily signatures, IPR012346 (p53/RUNT-type transcription factor, DNA-binding domain superfamily, residues 95–294) and IPR008967 (p53-like transcription factor, DNA-binding domain superfamily, residues 97–287). Immediately downstream lies IPR057064 (p53, central conserved site, residues 237–249), a hallmark motif that stabilizes the DNA-binding core and couples it to regulatory allostery. The C-terminus is devoted to oligomer formation: IPR010991 (p53, tetramerisation domain, residues 319–357) and its higher-order envelope IPR036674 (p53-like tetramerisation domain superfamily, residues 319–360). The entire sequence is encompassed by IPR002117 (p53 tumour suppressor family, residues 3–369), which frames the canonical tumor-suppressor transcription-factor architecture: N-terminal transactivation modules, central site-specific DNA-binding fold, and a C-terminal tetramerization hub.

This ordered layout dictates molecular function. The paired N-terminal activation domains (IPR013872 and IPR040926) cause transcriptional activation by recruiting co-regulators and the general transcription machinery; this supports DNA-binding transcription factor activity and specifically transcriptional activation. The central p53 DNA-binding core (IPR011615 within IPR012346/IPR008967) confers high-affinity, sequence-specific recognition of target promoters and enhancers, fulfilling sequence-specific DNA binding. The C-terminal tetramerization region (IPR010991/IPR036674) enforces cooperative assembly into a homotetramer, which increases DNA-binding avidity and regulatory versatility—hallmarks of transcriptional activators that operate via cooperative occupancy and enhancer looping. Together, these features define the molecular functions formalized as GO:0003700 DNA-binding transcription factor activity and GO:0001228 DNA-binding transcription activator activity, with the tetrameric assembly ensuring robust transcriptional output.

From this molecular function, the biological processes follow. A transcriptional activator with this architecture drives cell-cycle arrest and apoptosis by turning on genes that halt proliferation and tip the balance toward programmed cell death. The central conserved site (IPR057064) and tetramerization domain causally link DNA binding to stress-responsive transcription, enabling checkpoint signaling and caspase pathway induction. Thus, the protein participates in GO:0007050 cell cycle arrest and GO:0006915 apoptotic process, and—through its stress-responsive transcriptional control—acts as a tumor suppressor by preventing propagation of oncogenic states.

Cellular localization emerges from the same architecture. Transcriptional activation by the N-terminal domains and the central DNA-binding core requires nuclear residence for promoter/enhancer engagement, aligning with a nuclear role. Dynamic regulation through the tetramerization- and activation-modules often involves nucleocytoplasmic shuttling and cytoplasmic sequestration; therefore, a cytoplasmic pool is expected as part of regulated turnover and stress responses. This yields a composite localization to the nucleus and cytoplasm.

Mechanistically, I hypothesize that the protein functions as a stress-inducible, tetrameric transcriptional activator that binds specific DNA elements via its central core, recruits co-activators through its N-terminal activation domains, and enforces cooperative assembly through its C-terminal oligomerization hub. Likely interaction partners include upstream checkpoint kinases and ubiquitin ligases that modulate its abundance and activity, as well as chromatin-modifying co-activators that potentiate transcription at target loci. These interactions situate the protein at the nexus of genome surveillance, where tetramerization-driven cooperativity and rapid cytoplasm–nucleus cycling enable decisive transcriptional programs that arrest the cell cycle and trigger apoptosis.

### Functional Summary
A stress-responsive transcriptional activator that assembles into a cooperative tetramer to control gene expression programs that halt proliferation and promote apoptosis. Its N-terminal activation modules recruit transcriptional machinery and co-regulators, the central core confers high-affinity, sequence-specific DNA recognition, and the C-terminal oligomerization hub enforces tetramer formation that stabilizes promoter occupancy. Operating primarily in the nucleus with a regulated cytoplasmic pool, it integrates checkpoint cues to enforce tumor-suppressive pathways by activating genes that drive cell-cycle arrest and programmed cell death.

### UniProt Summary
Acts as a tumor suppressor in many tumor types; induces transcriptional and transcriptional-independent apoptosis by stimulating BAX and FAS pathways.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0098772
Molecular Function Regulator Activity
GO:0005488
Binding
GO:0140657
ATP-Dependent Activity
GO:0140110
Transcription Regulator Activity
GO:0097159
Organic Cyclic Compound Binding
GO:0043167
Ion Binding
GO:0003700
DNA-Binding Transcription Factor Activity
GO:0140677
Molecular Function Activator Activity
GO:1901363
Heterocyclic Compound Binding
GO:0044877
Protein-Containing Complex Binding
GO:0003682
Chromatin Binding
GO:0005515
Protein Binding
GO:1990841
Promoter-Specific Chromatin Binding
GO:0043169
Cation Binding
GO:0001216
DNA-Binding Transcription Activator Activity
GO:0005102
Signaling Receptor Binding
GO:0046983
Protein Dimerization Activity
GO:0001098
Basal Transcription Machinery Binding
GO:0019899
Enzyme Binding
GO:0000981
DNA-Binding Transcription Factor Activity, RNA Polymerase II-Specific
GO:0008134
Transcription Factor Binding
GO:0051087
Chaperone Binding
GO:0001217
DNA-Binding Transcription Repressor Activity
GO:0002039
P53 Binding
GO:0042802
Identical Protein Binding
GO:0043621
Protein Self-Association
GO:0003676
Nucleic Acid Binding
GO:0071889
14-3-3 Protein Binding
GO:0019904
Protein Domain Specific Binding
GO:0140666
Annealing Activity
GO:0140296
General Transcription Initiation Factor Binding
GO:0097718
Disordered Domain Specific Binding
GO:0042826
Histone Deacetylase Binding
GO:0001227
DNA-Binding Transcription Repressor Activity, RNA Polymerase II-Specific
GO:0140297
DNA-Binding Transcription Factor Binding
GO:0003677
DNA Binding
GO:0046872
Metal Ion Binding
GO:0001228
DNA-Binding Transcription Activator Activity
GO:0044389
Ubiquitin-Like Protein Ligase Binding
GO:0001067
Transcription Regulatory Region Nucleic Acid Binding
GO:0019900
Kinase Binding
GO:0019902
Phosphatase Binding
GO:0046982
Protein Heterodimerization Activity
GO:0002020
Protease Binding
GO:0001099
Basal RNA Polymerase II Transcription Machinery Binding
GO:0003723
RNA Binding
GO:0030971
Receptor Tyrosine Kinase Binding
GO:0035035
Histone Acetyltransferase Binding
GO:0031625
Ubiquitin Protein Ligase Binding
GO:0043565
Sequence-Specific DNA Binding
GO:0001091
RNA Polymerase II General Transcription Initiation Factor Binding
GO:0046914
Transition Metal Ion Binding
GO:1990814
DNA/DNA Annealing Activity
GO:0000976
Transcription Cis-Regulatory Region Binding
GO:0061629
RNA Polymerase II-Specific DNA-Binding Transcription Factor Binding
GO:0003690
Double-Stranded DNA Binding
GO:0019903
Protein Phosphatase Binding
GO:0003729
MRNA Binding
GO:0003697
Single-Stranded DNA Binding
GO:0019901
Protein Kinase Binding
GO:1990837
Sequence-Specific Double-Stranded DNA Binding
GO:0000987
Cis-Regulatory Region Sequence-Specific DNA Binding
GO:0001046
Core Promoter Sequence-Specific DNA Binding
GO:0008270
Zinc Ion Binding
GO:0005507
Copper Ion Binding
GO:0051721
Protein Phosphatase 2A Binding
GO:1990782
Protein Tyrosine Kinase Binding
GO:0000977
RNA Polymerase II Transcription Regulatory Region Sequence-Specific DNA Binding
GO:0003730
MRNA 3'-UTR Binding
GO:0000978
RNA Polymerase II Cis-Regulatory Region Sequence-Specific DNA Binding
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
GO:0048519
Negative Regulation Of Biological Process
GO:0048518
Positive Regulation Of Biological Process
GO:0050789
Regulation Of Biological Process
GO:0032501
Multicellular Organismal Process
GO:0032502
Developmental Process
GO:0009987
Cellular Process
GO:0008152
Metabolic Process
GO:0002376
Immune System Process
GO:0016032
Viral Process
GO:0051641
Cellular Localization
GO:0048856
Anatomical Structure Development
GO:0022402
Cell Cycle Process
GO:0071840
Cellular Component Organization Or Biogenesis
GO:0009892
Negative Regulation Of Metabolic Process
GO:0050794
Regulation Of Cellular Process
GO:0048583
Regulation Of Response To Stimulus
GO:0051716
Cellular Response To Stimulus
GO:0061919
Process Utilizing Autophagic Mechanism
GO:0048523
Negative Regulation Of Cellular Process
GO:0048869
Cellular Developmental Process
GO:0009628
Response To Abiotic Stimulus
GO:0009058
Biosynthetic Process
GO:0048584
Positive Regulation Of Response To Stimulus
GO:0019222
Regulation Of Metabolic Process
GO:0009056
Catabolic Process
GO:0033036
Macromolecule Localization
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
GO:0006807
Nitrogen Compound Metabolic Process
GO:0009607
Response To Biotic Stimulus
GO:0009719
Response To Endogenous Stimulus
GO:0008219
Cell Death
GO:0023051
Regulation Of Signaling
GO:0007165
Signal Transduction
GO:0023056
Positive Regulation Of Signaling
GO:0007275
Multicellular Organism Development
GO:0007049
Cell Cycle
GO:0071704
Organic Substance Metabolic Process
GO:0044237
Cellular Metabolic Process
GO:0002520
Immune System Development
GO:0009893
Positive Regulation Of Metabolic Process
GO:0006950
Response To Stress
GO:0045926
Negative Regulation Of Growth
GO:0040008
Regulation Of Growth
GO:0044238
Primary Metabolic Process
GO:0044085
Cellular Component Biogenesis
GO:0009314
Response To Radiation
GO:0048513
Animal Organ Development
GO:0009966
Regulation Of Signal Transduction
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0006725
Cellular Aromatic Compound Metabolic Process
GO:0010948
Negative Regulation Of Cell Cycle Process
GO:0006984
ER-Nucleus Signaling Pathway
GO:0006914
Autophagy
GO:0044087
Regulation Of Cellular Component Biogenesis
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0090398
Cellular Senescence
GO:0045786
Negative Regulation Of Cell Cycle
GO:0031668
Cellular Response To Extracellular Stimulus
GO:0044260
Cellular Macromolecule Metabolic Process
GO:0010564
Regulation Of Cell Cycle Process
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0050790
Regulation Of Catalytic Activity
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:1901576
Organic Substance Biosynthetic Process
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0046483
Heterocycle Metabolic Process
GO:0044092
Negative Regulation Of Molecular Function
GO:0008285
Negative Regulation Of Cell Population Proliferation
GO:0001558
Regulation Of Cell Growth
GO:0044249
Cellular Biosynthetic Process
GO:1901700
Response To Oxygen-Containing Compound
GO:0034641
Cellular Nitrogen Compound Metabolic Process
GO:0043170
Macromolecule Metabolic Process
GO:0071216
Cellular Response To Biotic Stimulus
GO:0009891
Positive Regulation Of Biosynthetic Process
GO:0043462
Regulation Of ATP-Dependent Activity
GO:0104004
Cellular Response To Environmental Stimulus
GO:0042127
Regulation Of Cell Population Proliferation
GO:0010941
Regulation Of Cell Death
GO:0042594
Response To Starvation
GO:1901698
Response To Nitrogen Compound
GO:0031325
Positive Regulation Of Cellular Metabolic Process
GO:0033554
Cellular Response To Stress
GO:0070727
Cellular Macromolecule Localization
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0010647
Positive Regulation Of Cell Communication
GO:0009890
Negative Regulation Of Biosynthetic Process
GO:0080090
Regulation Of Primary Metabolic Process
GO:0001666
Response To Hypoxia
GO:0010942
Positive Regulation Of Cell Death
GO:0012501
Programmed Cell Death
GO:0060548
Negative Regulation Of Cell Death
GO:0048468
Cell Development
GO:0009410
Response To Xenobiotic Stimulus
GO:0030154
Cell Differentiation
GO:0044248
Cellular Catabolic Process
GO:0048731
System Development
GO:0070482
Response To Oxygen Levels
GO:0071495
Cellular Response To Endogenous Stimulus
GO:1900117
Regulation Of Execution Phase Of Apoptosis
GO:0044089
Positive Regulation Of Cellular Component Biogenesis
GO:0051726
Regulation Of Cell Cycle
GO:0009894
Regulation Of Catabolic Process
GO:1901360
Organic Cyclic Compound Metabolic Process
GO:0071214
Cellular Response To Abiotic Stimulus
GO:0097190
Apoptotic Signaling Pathway
GO:0030308
Negative Regulation Of Cell Growth
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0062014
Negative Regulation Of Small Molecule Metabolic Process
GO:0016043
Cellular Component Organization
GO:0007166
Cell Surface Receptor Signaling Pathway
GO:0051128
Regulation Of Cellular Component Organization
GO:0071496
Cellular Response To External Stimulus
GO:0009967
Positive Regulation Of Signal Transduction
GO:1903047
Mitotic Cell Cycle Process
GO:0035556
Intracellular Signal Transduction
GO:0006979
Response To Oxidative Stress
GO:0051130
Positive Regulation Of Cellular Component Organization
GO:0031324
Negative Regulation Of Cellular Metabolic Process
GO:0010033
Response To Organic Substance
GO:0009991
Response To Extracellular Stimulus
GO:0006139
Nucleobase-Containing Compound Metabolic Process
GO:0009888
Tissue Development
GO:0010646
Regulation Of Cell Communication
GO:0070887
Cellular Response To Chemical Stimulus
GO:0046677
Response To Antibiotic
GO:0009889
Regulation Of Biosynthetic Process
GO:0062012
Regulation Of Small Molecule Metabolic Process
GO:0048534
Hematopoietic Or Lymphoid Organ Development
GO:0000278
Mitotic Cell Cycle
GO:0071236
Cellular Response To Antibiotic
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0071453
Cellular Response To Oxygen Levels
GO:0045980
Negative Regulation Of Nucleotide Metabolic Process
GO:0010675
Regulation Of Cellular Carbohydrate Metabolic Process
GO:0007093
Mitotic Cell Cycle Checkpoint Signaling
GO:0051095
Regulation Of Helicase Activity
GO:0010468
Regulation Of Gene Expression
GO:0006140
Regulation Of Nucleotide Metabolic Process
GO:0001501
Skeletal System Development
GO:0036293
Response To Decreased Oxygen Levels
GO:0043620
Regulation Of DNA-Templated Transcription In Response To Stress
GO:0045930
Negative Regulation Of Mitotic Cell Cycle
GO:0010563
Negative Regulation Of Phosphorus Metabolic Process
GO:0097193
Intrinsic Apoptotic Signaling Pathway
GO:0048147
Negative Regulation Of Fibroblast Proliferation
GO:1902533
Positive Regulation Of Intracellular Signal Transduction
GO:0007264
Small GTPase Mediated Signal Transduction
GO:0002244
Hematopoietic Progenitor Cell Differentiation
GO:2000379
Positive Regulation Of Reactive Oxygen Species Metabolic Process
GO:1901701
Cellular Response To Oxygen-Containing Compound
GO:0019221
Cytokine-Mediated Signaling Pathway
GO:0071478
Cellular Response To Radiation
GO:0071456
Cellular Response To Hypoxia
GO:0071417
Cellular Response To Organonitrogen Compound
GO:0009416
Response To Light Stimulus
GO:2000377
Regulation Of Reactive Oxygen Species Metabolic Process
GO:0051052
Regulation Of DNA Metabolic Process
GO:0006974
Cellular Response To DNA Damage Stimulus
GO:0071310
Cellular Response To Organic Substance
GO:0042770
Signal Transduction In Response To DNA Damage
GO:0019438
Aromatic Compound Biosynthetic Process
GO:0062197
Cellular Response To Chemical Stress
GO:1901699
Cellular Response To Nitrogen Compound
GO:0006325
Chromatin Organization
GO:0034976
Response To Endoplasmic Reticulum Stress
GO:0010557
Positive Regulation Of Macromolecule Biosynthetic Process
GO:0043467
Regulation Of Generation Of Precursor Metabolites And Energy
GO:0051254
Positive Regulation Of RNA Metabolic Process
GO:0060348
Bone Development
GO:0043471
Regulation Of Cellular Carbohydrate Catabolic Process
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:0006915
Apoptotic Process
GO:0019219
Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0033043
Regulation Of Organelle Organization
GO:0044271
Cellular Nitrogen Compound Biosynthetic Process
GO:0008104
Protein Localization
GO:0051338
Regulation Of Transferase Activity
GO:0010638
Positive Regulation Of Organelle Organization
GO:0031669
Cellular Response To Nutrient Levels
GO:0032780
Negative Regulation Of ATP-Dependent Activity
GO:0031328
Positive Regulation Of Cellular Biosynthetic Process
GO:0031334
Positive Regulation Of Protein-Containing Complex Assembly
GO:1901988
Negative Regulation Of Cell Cycle Phase Transition
GO:0034599
Cellular Response To Oxidative Stress
GO:1901652
Response To Peptide
GO:0009059
Macromolecule Biosynthetic Process
GO:1901362
Organic Cyclic Compound Biosynthetic Process
GO:0043254
Regulation Of Protein-Containing Complex Assembly
GO:0007346
Regulation Of Mitotic Cell Cycle
GO:0048145
Regulation Of Fibroblast Proliferation
GO:0043069
Negative Regulation Of Programmed Cell Death
GO:0043067
Regulation Of Programmed Cell Death
GO:0072331
Signal Transduction By P53 Class Mediator
GO:0022607
Cellular Component Assembly
GO:0051053
Negative Regulation Of DNA Metabolic Process
GO:0090304
Nucleic Acid Metabolic Process
GO:0031667
Response To Nutrient Levels
GO:0018130
Heterocycle Biosynthetic Process
GO:0006259
DNA Metabolic Process
GO:0031327
Negative Regulation Of Cellular Biosynthetic Process
GO:0051252
Regulation Of RNA Metabolic Process
GO:0043933
Protein-Containing Complex Organization
GO:0010212
Response To Ionizing Radiation
GO:0045934
Negative Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0010467
Gene Expression
GO:0030097
Hemopoiesis
GO:0043086
Negative Regulation Of Catalytic Activity
GO:0034097
Response To Cytokine
GO:0071466
Cellular Response To Xenobiotic Stimulus
GO:0043470
Regulation Of Carbohydrate Catabolic Process
GO:0000075
Cell Cycle Checkpoint Signaling
GO:0009267
Cellular Response To Starvation
GO:0043068
Positive Regulation Of Programmed Cell Death
GO:2001235
Positive Regulation Of Apoptotic Signaling Pathway
GO:0010628
Positive Regulation Of Gene Expression
GO:0006109
Regulation Of Carbohydrate Metabolic Process
GO:2001233
Regulation Of Apoptotic Signaling Pathway
GO:0034654
Nucleobase-Containing Compound Biosynthetic Process
GO:0045935
Positive Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0048863
Stem Cell Differentiation
GO:0034248
Regulation Of Amide Metabolic Process
GO:0010243
Response To Organonitrogen Compound
GO:1901987
Regulation Of Cell Cycle Phase Transition
GO:0010558
Negative Regulation Of Macromolecule Biosynthetic Process
GO:0031329
Regulation Of Cellular Catabolic Process
GO:0051253
Negative Regulation Of RNA Metabolic Process
GO:0051174
Regulation Of Phosphorus Metabolic Process
GO:1902531
Regulation Of Intracellular Signal Transduction
GO:1900542
Regulation Of Purine Nucleotide Metabolic Process
GO:0042981
Regulation Of Apoptotic Process
GO:0016070
RNA Metabolic Process
GO:2001141
Regulation Of RNA Biosynthetic Process
GO:1900543
Negative Regulation Of Purine Nucleotide Metabolic Process
GO:0006281
DNA Repair
GO:0045815
Transcription Initiation-Coupled Chromatin Remodeling
GO:0071345
Cellular Response To Cytokine Stimulus
GO:0007265
Ras Protein Signal Transduction
GO:0008630
Intrinsic Apoptotic Signaling Pathway In Response To DNA Damage
GO:0006338
Chromatin Remodeling
GO:0044774
Mitotic DNA Integrity Checkpoint Signaling
GO:1902749
Regulation Of Cell Cycle G2/M Phase Transition
GO:0090200
Positive Regulation Of Release Of Cytochrome C From Mitochondria
GO:2000630
Positive Regulation Of MiRNA Metabolic Process
GO:1902680
Positive Regulation Of RNA Biosynthetic Process
GO:0043618
Regulation Of Transcription From RNA Polymerase II Promoter In Response To Stress
GO:0042149
Cellular Response To Glucose Starvation
GO:0045898
Regulation Of RNA Polymerase II Transcription Preinitiation Complex Assembly
GO:0043065
Positive Regulation Of Apoptotic Process
GO:2001242
Regulation Of Intrinsic Apoptotic Signaling Pathway
GO:0071479
Cellular Response To Ionizing Radiation
GO:0033209
Tumor Necrosis Factor-Mediated Signaling Pathway
GO:0010332
Response To Gamma Radiation
GO:2001244
Positive Regulation Of Intrinsic Apoptotic Signaling Pathway
GO:0071482
Cellular Response To Light Stimulus
GO:1901653
Cellular Response To Peptide
GO:0034612
Response To Tumor Necrosis Factor
GO:1902807
Negative Regulation Of Cell Cycle G1/S Phase Transition
GO:2000279
Negative Regulation Of DNA Biosynthetic Process
GO:0032774
RNA Biosynthetic Process
GO:0097659
Nucleic Acid-Templated Transcription
GO:0090199
Regulation Of Release Of Cytochrome C From Mitochondria
GO:0045936
Negative Regulation Of Phosphate Metabolic Process
GO:0051972
Regulation Of Telomerase Activity
GO:0010821
Regulation Of Mitochondrion Organization
GO:0065003
Protein-Containing Complex Assembly
GO:0010822
Positive Regulation Of Mitochondrion Organization
GO:0051348
Negative Regulation Of Transferase Activity
GO:0009411
Response To UV
GO:1902679
Negative Regulation Of RNA Biosynthetic Process
GO:0000077
DNA Damage Checkpoint Signaling
GO:0031570
DNA Integrity Checkpoint Signaling
GO:0030330
DNA Damage Response, Signal Transduction By P53 Class Mediator
GO:1901991
Negative Regulation Of Mitotic Cell Cycle Phase Transition
GO:0060218
Hematopoietic Stem Cell Differentiation
GO:0043066
Negative Regulation Of Apoptotic Process
GO:0006355
Regulation Of DNA-Templated Transcription
GO:0072332
Intrinsic Apoptotic Signaling Pathway By P53 Class Mediator
GO:0019220
Regulation Of Phosphate Metabolic Process
GO:0040029
Epigenetic Regulation Of Gene Expression
GO:0036294
Cellular Response To Decreased Oxygen Levels
GO:1901990
Regulation Of Mitotic Cell Cycle Phase Transition
GO:0044819
Mitotic G1/S Transition Checkpoint Signaling
GO:2000278
Regulation Of DNA Biosynthetic Process
GO:2000628
Regulation Of MiRNA Metabolic Process
GO:1902806
Regulation Of Cell Cycle G1/S Phase Transition
GO:0036003
Positive Regulation Of Transcription From RNA Polymerase II Promoter In Response To Stress
GO:2000134
Negative Regulation Of G1/S Transition Of Mitotic Cell Cycle
GO:0031571
Mitotic G1 DNA Damage Checkpoint Signaling
GO:0016071
MRNA Metabolic Process
GO:1903508
Positive Regulation Of Nucleic Acid-Templated Transcription
GO:0042771
Intrinsic Apoptotic Signaling Pathway In Response To DNA Damage By P53 Class Mediator
GO:0006357
Regulation Of Transcription By RNA Polymerase II
GO:0044773
Mitotic DNA Damage Checkpoint Signaling
GO:0045893
Positive Regulation Of DNA-Templated Transcription
GO:0034644
Cellular Response To UV
GO:0006289
Nucleotide-Excision Repair
GO:0045892
Negative Regulation Of DNA-Templated Transcription
GO:1903506
Regulation Of Nucleic Acid-Templated Transcription
GO:1902893
Regulation Of MiRNA Transcription
GO:0006351
DNA-Templated Transcription
GO:2000142
Regulation Of DNA-Templated Transcription Initiation
GO:0006977
DNA Damage Response, Signal Transduction By P53 Class Mediator Resulting In Cell Cycle Arrest
GO:1902895
Positive Regulation Of MiRNA Transcription
GO:1903507
Negative Regulation Of Nucleic Acid-Templated Transcription
GO:2000045
Regulation Of G1/S Transition Of Mitotic Cell Cycle
GO:0071356
Cellular Response To Tumor Necrosis Factor
GO:0071480
Cellular Response To Gamma Radiation
GO:0000122
Negative Regulation Of Transcription By RNA Polymerase II
GO:0060260
Regulation Of Transcription Initiation By RNA Polymerase II
GO:2000144
Positive Regulation Of DNA-Templated Transcription Initiation
GO:0045944
Positive Regulation Of Transcription By RNA Polymerase II
GO:0009299
MRNA Transcription
GO:0060261
Positive Regulation Of Transcription Initiation By RNA Polymerase II
Cellular Component
GO:0005575
Cellular_component
GO:0110165
Cellular Anatomical Entity
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0005829
Cytosol
GO:0005737
Cytoplasm
GO:0031974
Membrane-Enclosed Lumen
GO:0005654
Nucleoplasm
GO:0043233
Organelle Lumen
GO:0043229
Intracellular Organelle
GO:0043227
Membrane-Bounded Organelle
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0070013
Intracellular Organelle Lumen
GO:0031981
Nuclear Lumen
GO:0005634
Nucleus

### InterPro Domains
1
393
IPR002117
IPR013872
IPR040926
IPR012346
IPR008967
IPR011615
IPR057064
IPR010991
IPR036674
Domain Details
IPR002117
p53 tumour suppressor family (family) [3-369]
IPR013872
p53, transactivation domain (domain) [6-30]
IPR040926
Cellular tumor antigen p53, transactivation domain 2 (domain) [35-59]
IPR012346
p53/RUNT-type transcription factor, DNA-binding domain superfamily (homologous_superfamily) [95-294]
IPR008967
p53-like transcription factor, DNA-binding domain superfamily (homologous_superfamily) [97-287]
IPR011615
p53, DNA-binding domain (domain) [100-288]
IPR057064
p53, central conserved site (conserved_site) [237-249]
IPR010991
p53, tetramerisation domain (domain) [319-357]
IPR036674
p53-like tetramerisation domain superfamily (homologous_superfamily) [319-360]

---
*Generated by [BioReason](https://bioreason.net)*
