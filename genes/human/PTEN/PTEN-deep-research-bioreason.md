# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:15 PM*

---

**Organism:** Homo sapiens

### Thinking Trace
I begin by dissecting the InterPro architecture and its order along the polypeptide. The N-terminal two-thirds (residues 1–403) are densely annotated with phosphatase signatures that define a cysteine-dependent phosphatase core. IPR029021 (Protein-tyrosine phosphatase-like homologous superfamily, residues 1–187) frames the fold, while multiple overlapping catalytic annotations converge on the same core: IPR003595 (Protein-tyrosine phosphatase, catalytic domain, residues 23–183), IPR045101 (PTEN, phosphatase domain, residues 24–181), IPR029023 (Tensin-type phosphatase domain, residues 14–185), and IPR000387 (Tyrosine-specific protein phosphatases domain, residues 102–173). The catalytic center is pinpointed by IPR016130 (Protein-tyrosine phosphatase, active site, residues 122–132), which denotes the canonical HCX5R motif that drives nucleophilic attack and phosphate ester hydrolysis. Family-level assignments IPR017361 (Bifunctional phosphatidylinositol trisphosphate phosphatase/dual specificity phosphatase PTEN family, residues 1–403) and IPR051281 (Dual-specificity lipid and protein phosphatase family, residues 1–377) establish that this enzyme acts both as a lipid phosphatase and as a dual-specificity protein phosphatase. Downstream, residues 188–350 form a membrane-targeting module: IPR035892 (C2 domain superfamily, residues 188–349) and IPR014020 (Tensin phosphatase, C2 domain, residues 188–350). This C2 architecture mediates Ca2+-modulated lipid binding and positions the catalytic head relative to membrane-associated substrates. The combined architecture—PTEN-like PTP catalytic domain followed by a tensin-type C2 membrane-targeting domain—creates a bifunctional catalyst that can hydrolyze phosphate groups on both phosphoinositides and phosphotyrosine/protein substrates.

This domain layout dictates molecular function. The N-terminal PTEN-like catalytic core with the HCX5R active site causes phosphomonoester hydrolysis on lipid and protein substrates, consistent with GO:0003674 (molecular function label to explain). The dual-specificity designation and tyrosine-phosphatase fold support broad phosphate-removal chemistry rather than a single-pathway specificity. The C2 domain does not confer a separate catalytic activity; instead, it localizes and orients the enzyme at membrane-proximal sites where phosphatidylinositol trisphosphate accumulates. Together, these features explain why the protein executes both lipid and protein dephosphorylation in vivo.

From function to process, a PTEN-like lipid phosphatase that erases the D3 phosphate of phosphatidylinositol 3,4,5-trisphosphate necessarily reduces local PIP3 levels and thereby dampens phosphoinositide-dependent signaling cascades. This causal link places the enzyme squarely in phosphoinositide-mediated signaling and, by extension, in pathways that govern cell survival, proliferation, and polarity. The dual-specificity protein phosphatase activity further tunes kinase-driven signaling circuits. Thus, the most parsimonious biological processes are regulation of phosphatidylinositol 3-kinase/AKT signaling and general signal transduction control, achieved through coordinated lipid and protein dephosphorylation.

Cellular location follows directly from the targeting modules and observed compartmental distribution. The tensin-type C2 domain and membrane-binding propensity argue for a predominantly soluble enzyme that transiently associates with membranes and cytoskeletal hubs. This explains accumulation in the cytoplasm and at the cytoskeleton, with additional residence in the nucleus where phosphorylation-dependent transcriptional programs are adjusted. The reported presence in melanosomes and at the spindle apparatus aligns with a membrane-anchored yet soluble catalyst that concentrates where PIP3 gradients and cytoskeletal assemblies form. Therefore, the cellular components encompass cytoplasm, cytoskeleton, nucleus, and specialized organelles such as melanosomes.

Mechanistically, I propose that the N-terminal PTEN-like catalytic center removes the D3 phosphate from PIP3 at membrane-proximal sites defined by the C2 domain, locally lowering PIP3 and antagonizing PI3K-driven signaling. In parallel, the same catalytic chemistry enables reversible dephosphorylation of protein substrates within kinase pathways. This dual action predicts interactions with membrane-proximal signaling assemblies and cytoskeletal scaffolds. Likely partners include phosphoinositide-binding adaptors and spindle-associated complexes that recruit the enzyme to sites where lipid gradients and microtubule structures coordinate cell-cycle and trafficking events.

### Functional Summary
A human soluble phosphatase that couples a PTEN-like catalytic core with a membrane-targeting C2 module to remove phosphate groups from both membrane phosphoinositides and protein substrates. By erasing the D3 phosphate of phosphatidylinositol trisphosphate at membrane-proximal sites and tuning kinase-driven signaling, it dampens PI3K/AKT outputs and shapes cytoskeleton- and organelle-associated pathways. The enzyme operates primarily in the cytoplasm and at cytoskeletal assemblies, with additional residence in the nucleus and melanosomes, where it modulates signaling and trafficking through localized lipid and protein dephosphorylation.

### UniProt Summary
Acts as a bifunctional lipid- and protein-phosphatase by removing phosphate groups from different phospholipids and phosphoproteins.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0003824
Catalytic Activity
GO:0098772
Molecular Function Regulator Activity
GO:0005488
Binding
GO:0140678
Molecular Function Inhibitor Activity
GO:0016787
Hydrolase Activity
GO:0044877
Protein-Containing Complex Binding
GO:0140096
Catalytic Activity, Acting On A Protein
GO:0005515
Protein Binding
GO:0004721
Phosphoprotein Phosphatase Activity
GO:0042802
Identical Protein Binding
GO:0016788
Hydrolase Activity, Acting On Ester Bonds
GO:0019904
Protein Domain Specific Binding
GO:0019899
Enzyme Binding
GO:0042578
Phosphoric Ester Hydrolase Activity
GO:0030165
PDZ Domain Binding
GO:0002020
Protease Binding
GO:0004722
Protein Serine/Threonine Phosphatase Activity
GO:0004725
Protein Tyrosine Phosphatase Activity
GO:1990381
Ubiquitin-Specific Protease Binding
GO:0016791
Phosphatase Activity
GO:0052866
Phosphatidylinositol Phosphate Phosphatase Activity
GO:0052745
Inositol Phosphate Phosphatase Activity
GO:0052744
Phosphatidylinositol Monophosphate Phosphatase Activity
GO:0034593
Phosphatidylinositol Bisphosphate Phosphatase Activity
GO:0034594
Phosphatidylinositol Trisphosphate Phosphatase Activity
GO:0004438
Phosphatidylinositol-3-Phosphate Phosphatase Activity
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
GO:0023057
Negative Regulation Of Signaling
GO:0006807
Nitrogen Compound Metabolic Process
GO:0051241
Negative Regulation Of Multicellular Organismal Process
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0009892
Negative Regulation Of Metabolic Process
GO:0007267
Cell-Cell Signaling
GO:0050793
Regulation Of Developmental Process
GO:0065008
Regulation Of Biological Quality
GO:0050794
Regulation Of Cellular Process
GO:0048583
Regulation Of Response To Stimulus
GO:0040013
Negative Regulation Of Locomotion
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
GO:0009058
Biosynthetic Process
GO:0048584
Positive Regulation Of Response To Stimulus
GO:0019222
Regulation Of Metabolic Process
GO:0071704
Organic Substance Metabolic Process
GO:0009056
Catabolic Process
GO:0044237
Cellular Metabolic Process
GO:0044281
Small Molecule Metabolic Process
GO:0009893
Positive Regulation Of Metabolic Process
GO:0065009
Regulation Of Molecular Function
GO:0048585
Negative Regulation Of Response To Stimulus
GO:0007154
Cell Communication
GO:0044238
Primary Metabolic Process
GO:0048522
Positive Regulation Of Cellular Process
GO:0051602
Response To Electrical Stimulus
GO:0009968
Negative Regulation Of Signal Transduction
GO:0010942
Positive Regulation Of Cell Death
GO:0051129
Negative Regulation Of Cellular Component Organization
GO:2000145
Regulation Of Cell Motility
GO:0080134
Regulation Of Response To Stress
GO:0009966
Regulation Of Signal Transduction
GO:0030155
Regulation Of Cell Adhesion
GO:0044255
Cellular Lipid Metabolic Process
GO:0010719
Negative Regulation Of Epithelial To Mesenchymal Transition
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0032101
Regulation Of Response To External Stimulus
GO:0005975
Carbohydrate Metabolic Process
GO:0010948
Negative Regulation Of Cell Cycle Process
GO:0044087
Regulation Of Cellular Component Biogenesis
GO:0006793
Phosphorus Metabolic Process
GO:0009894
Regulation Of Catabolic Process
GO:0010632
Regulation Of Epithelial Cell Migration
GO:0051726
Regulation Of Cell Cycle
GO:0007162
Negative Regulation Of Cell Adhesion
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0071214
Cellular Response To Abiotic Stimulus
GO:0010633
Negative Regulation Of Epithelial Cell Migration
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0045595
Regulation Of Cell Differentiation
GO:0007166
Cell Surface Receptor Signaling Pathway
GO:0045786
Negative Regulation Of Cell Cycle
GO:0051128
Regulation Of Cellular Component Organization
GO:1901575
Organic Substance Catabolic Process
GO:0010564
Regulation Of Cell Cycle Process
GO:2000146
Negative Regulation Of Cell Motility
GO:0051173
Positive Regulation Of Nitrogen Compound Metabolic Process
GO:0044262
Cellular Carbohydrate Metabolic Process
GO:0009967
Positive Regulation Of Signal Transduction
GO:1901615
Organic Hydroxy Compound Metabolic Process
GO:0010648
Negative Regulation Of Cell Communication
GO:0050790
Regulation Of Catalytic Activity
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:0044093
Positive Regulation Of Molecular Function
GO:1901576
Organic Substance Biosynthetic Process
GO:1901564
Organonitrogen Compound Metabolic Process
GO:0044282
Small Molecule Catabolic Process
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0198738
Cell-Cell Signaling By Wnt
GO:0008285
Negative Regulation Of Cell Population Proliferation
GO:0019637
Organophosphate Metabolic Process
GO:0019538
Protein Metabolic Process
GO:0044092
Negative Regulation Of Molecular Function
GO:1905114
Cell Surface Receptor Signaling Pathway Involved In Cell-Cell Signaling
GO:0044249
Cellular Biosynthetic Process
GO:0006066
Alcohol Metabolic Process
GO:0031647
Regulation Of Protein Stability
GO:0031324
Negative Regulation Of Cellular Metabolic Process
GO:0043170
Macromolecule Metabolic Process
GO:0104004
Cellular Response To Environmental Stimulus
GO:0042127
Regulation Of Cell Population Proliferation
GO:0006629
Lipid Metabolic Process
GO:0010941
Regulation Of Cell Death
GO:0010646
Regulation Of Cell Communication
GO:0031325
Positive Regulation Of Cellular Metabolic Process
GO:0045596
Negative Regulation Of Cell Differentiation
GO:0051090
Regulation Of DNA-Binding Transcription Factor Activity
GO:0009889
Regulation Of Biosynthetic Process
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0010647
Positive Regulation Of Cell Communication
GO:0080090
Regulation Of Primary Metabolic Process
GO:1903035
Negative Regulation Of Response To Wounding
GO:0009896
Positive Regulation Of Catabolic Process
GO:0032102
Negative Regulation Of Response To External Stimulus
GO:0007346
Regulation Of Mitotic Cell Cycle
GO:0061045
Negative Regulation Of Wound Healing
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0051246
Regulation Of Protein Metabolic Process
GO:0010810
Regulation Of Cell-Substrate Adhesion
GO:0043067
Regulation Of Programmed Cell Death
GO:0016055
Wnt Signaling Pathway
GO:0006644
Phospholipid Metabolic Process
GO:0030334
Regulation Of Cell Migration
GO:0071257
Cellular Response To Electrical Stimulus
GO:0048662
Negative Regulation Of Smooth Muscle Cell Proliferation
GO:0150116
Regulation Of Cell-Substrate Junction Organization
GO:0045017
Glycerolipid Biosynthetic Process
GO:0010468
Regulation Of Gene Expression
GO:0046838
Phosphorylated Carbohydrate Dephosphorylation
GO:0043647
Inositol Phosphate Metabolic Process
GO:0048660
Regulation Of Smooth Muscle Cell Proliferation
GO:0043412
Macromolecule Modification
GO:0046486
Glycerolipid Metabolic Process
GO:0046164
Alcohol Catabolic Process
GO:0045930
Negative Regulation Of Mitotic Cell Cycle
GO:0090407
Organophosphate Biosynthetic Process
GO:0010563
Negative Regulation Of Phosphorus Metabolic Process
GO:0030258
Lipid Modification
GO:0051252
Regulation Of RNA Metabolic Process
GO:0043085
Positive Regulation Of Catalytic Activity
GO:0008610
Lipid Biosynthetic Process
GO:0051091
Positive Regulation Of DNA-Binding Transcription Factor Activity
GO:0010812
Negative Regulation Of Cell-Substrate Adhesion
GO:0043086
Negative Regulation Of Catalytic Activity
GO:1903034
Regulation Of Response To Wounding
GO:0043068
Positive Regulation Of Programmed Cell Death
GO:1901888
Regulation Of Cell Junction Assembly
GO:0051248
Negative Regulation Of Protein Metabolic Process
GO:2001235
Positive Regulation Of Apoptotic Signaling Pathway
GO:0006796
Phosphate-Containing Compound Metabolic Process
GO:1902532
Negative Regulation Of Intracellular Signal Transduction
GO:2001233
Regulation Of Apoptotic Signaling Pathway
GO:1901889
Negative Regulation Of Cell Junction Assembly
GO:0030336
Negative Regulation Of Cell Migration
GO:0036211
Protein Modification Process
GO:1901616
Organic Hydroxy Compound Catabolic Process
GO:1904029
Regulation Of Cyclin-Dependent Protein Kinase Activity
GO:0019751
Polyol Metabolic Process
GO:1901987
Regulation Of Cell Cycle Phase Transition
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:0051247
Positive Regulation Of Protein Metabolic Process
GO:0019219
Regulation Of Nucleobase-Containing Compound Metabolic Process
GO:0031331
Positive Regulation Of Cellular Catabolic Process
GO:0050821
Protein Stabilization
GO:0051338
Regulation Of Transferase Activity
GO:0031329
Regulation Of Cellular Catabolic Process
GO:0046434
Organophosphate Catabolic Process
GO:0010717
Regulation Of Epithelial To Mesenchymal Transition
GO:1902531
Regulation Of Intracellular Signal Transduction
GO:0051174
Regulation Of Phosphorus Metabolic Process
GO:0045736
Negative Regulation Of Cyclin-Dependent Protein Serine/Threonine Kinase Activity
GO:1901988
Negative Regulation Of Cell Cycle Phase Transition
GO:0001953
Negative Regulation Of Cell-Matrix Adhesion
GO:0014066
Regulation Of Phosphatidylinositol 3-Kinase Signaling
GO:0042981
Regulation Of Apoptotic Process
GO:1904705
Regulation Of Vascular Associated Smooth Muscle Cell Proliferation
GO:0030162
Regulation Of Proteolysis
GO:1904030
Negative Regulation Of Cyclin-Dependent Protein Kinase Activity
GO:0031400
Negative Regulation Of Protein Modification Process
GO:2001141
Regulation Of RNA Biosynthetic Process
GO:0001952
Regulation Of Cell-Matrix Adhesion
GO:0006470
Protein Dephosphorylation
GO:0051438
Regulation Of Ubiquitin-Protein Transferase Activity
GO:0071545
Inositol Phosphate Catabolic Process
GO:0060070
Canonical Wnt Signaling Pathway
GO:0008654
Phospholipid Biosynthetic Process
GO:0043549
Regulation Of Kinase Activity
GO:0051896
Regulation Of Protein Kinase B Signaling
GO:0051348
Negative Regulation Of Transferase Activity
GO:2000058
Regulation Of Ubiquitin-Dependent Protein Catabolic Process
GO:0031401
Positive Regulation Of Protein Modification Process
GO:0046839
Phospholipid Dephosphorylation
GO:0061041
Regulation Of Wound Healing
GO:0046855
Inositol Phosphate Dephosphorylation
GO:0043409
Negative Regulation Of MAPK Cascade
GO:0016311
Dephosphorylation
GO:0000079
Regulation Of Cyclin-Dependent Protein Serine/Threonine Kinase Activity
GO:0043408
Regulation Of MAPK Cascade
GO:0043065
Positive Regulation Of Apoptotic Process
GO:0051347
Positive Regulation Of Transferase Activity
GO:0031399
Regulation Of Protein Modification Process
GO:1901991
Negative Regulation Of Mitotic Cell Cycle Phase Transition
GO:2001238
Positive Regulation Of Extrinsic Apoptotic Signaling Pathway
GO:1904706
Negative Regulation Of Vascular Associated Smooth Muscle Cell Proliferation
GO:0046474
Glycerophospholipid Biosynthetic Process
GO:0006355
Regulation Of DNA-Templated Transcription
GO:0019220
Regulation Of Phosphate Metabolic Process
GO:0006650
Glycerophospholipid Metabolic Process
GO:0051898
Negative Regulation Of Protein Kinase B Signaling
GO:0014067
Negative Regulation Of Phosphatidylinositol 3-Kinase Signaling
GO:0045862
Positive Regulation Of Proteolysis
GO:1901990
Regulation Of Mitotic Cell Cycle Phase Transition
GO:0090109
Regulation Of Cell-Substrate Junction Assembly
GO:2000060
Positive Regulation Of Ubiquitin-Dependent Protein Catabolic Process
GO:2001236
Regulation Of Extrinsic Apoptotic Signaling Pathway
GO:0046174
Polyol Catabolic Process
GO:1902806
Regulation Of Cell Cycle G1/S Phase Transition
GO:1902807
Negative Regulation Of Cell Cycle G1/S Phase Transition
GO:0045936
Negative Regulation Of Phosphate Metabolic Process
GO:0001932
Regulation Of Protein Phosphorylation
GO:2000134
Negative Regulation Of G1/S Transition Of Mitotic Cell Cycle
GO:0042326
Negative Regulation Of Phosphorylation
GO:0045859
Regulation Of Protein Kinase Activity
GO:1902041
Regulation Of Extrinsic Apoptotic Signaling Pathway Via Death Domain Receptors
GO:1903322
Positive Regulation Of Protein Modification By Small Protein Conjugation Or Removal
GO:0051443
Positive Regulation Of Ubiquitin-Protein Transferase Activity
GO:0051893
Regulation Of Focal Adhesion Assembly
GO:1903506
Regulation Of Nucleic Acid-Templated Transcription
GO:0070372
Regulation Of ERK1 And ERK2 Cascade
GO:0042325
Regulation Of Phosphorylation
GO:0001933
Negative Regulation Of Protein Phosphorylation
GO:1903320
Regulation Of Protein Modification By Small Protein Conjugation Or Removal
GO:1903052
Positive Regulation Of Proteolysis Involved In Protein Catabolic Process
GO:0033673
Negative Regulation Of Kinase Activity
GO:0046856
Phosphatidylinositol Dephosphorylation
GO:0046488
Phosphatidylinositol Metabolic Process
GO:1903050
Regulation Of Proteolysis Involved In Protein Catabolic Process
GO:0070373
Negative Regulation Of ERK1 And ERK2 Cascade
GO:2000045
Regulation Of G1/S Transition Of Mitotic Cell Cycle
GO:1904666
Regulation Of Ubiquitin Protein Ligase Activity
GO:0006661
Phosphatidylinositol Biosynthetic Process
GO:0071900
Regulation Of Protein Serine/Threonine Kinase Activity
GO:0031396
Regulation Of Protein Ubiquitination
GO:0033137
Negative Regulation Of Peptidyl-Serine Phosphorylation
GO:0033135
Regulation Of Peptidyl-Serine Phosphorylation
GO:0006469
Negative Regulation Of Protein Kinase Activity
GO:0031398
Positive Regulation Of Protein Ubiquitination
GO:0071901
Negative Regulation Of Protein Serine/Threonine Kinase Activity
Cellular Component
GO:0005575
Cellular_component
GO:0110165
Cellular Anatomical Entity
GO:0098552
Side Of Membrane
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0045177
Apical Part Of Cell
GO:0042995
Cell Projection
GO:0016020
Membrane
GO:0005829
Cytosol
GO:0005737
Cytoplasm
GO:0071944
Cell Periphery
GO:0031974
Membrane-Enclosed Lumen
GO:0005654
Nucleoplasm
GO:0098590
Plasma Membrane Region
GO:0043233
Organelle Lumen
GO:0043229
Intracellular Organelle
GO:0098562
Cytoplasmic Side Of Membrane
GO:0043227
Membrane-Bounded Organelle
GO:0005886
Plasma Membrane
GO:0016324
Apical Plasma Membrane
GO:0009898
Cytoplasmic Side Of Plasma Membrane
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
