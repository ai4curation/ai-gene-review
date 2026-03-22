# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:17 PM*

---

**Organism:** Homo sapiens

### Thinking Trace
I begin by dissecting the InterPro architecture. The sequence is anchored by two family-level envelopes that define enzyme identity and lineage: IPR020831 (Glyceraldehyde/Erythrose phosphate dehydrogenase family, residues 3–334) and IPR006424 (Glyceraldehyde-3-phosphate dehydrogenase, type I family, residues 5–326). These broad signatures establish a classical type I GAPDH scaffold that typically forms soluble tetramers and catalyzes oxidation–phosphorylation chemistry on triose phosphate substrates. The N-terminus contains IPR020828 (Glyceraldehyde 3-phosphate dehydrogenase, NAD(P) binding domain, residues 4–152), embedded within IPR036291 (NAD(P)-binding domain superfamily, residues 4–173). This Rossmann-like module dictates tight binding of pyridine nucleotides and positions NAD+ for hydride transfer. The C-terminal half transitions into IPR020829 (Glyceraldehyde 3-phosphate dehydrogenase, catalytic domain, residues 157–314), which houses the chemistry-bearing core. Critically, IPR020830 (Glyceraldehyde 3-phosphate dehydrogenase, active site, residues 150–157) pinpoints the catalytic locus that in type I enzymes coordinates a nucleophilic cysteine and neighboring residues that enable Schiff-base and acyl-intermediate transitions. The ordered layout—N-terminal NAD(P)-binding domain feeding into a C-terminal catalytic barrel—causally produces oxidoreductase chemistry that channels electrons from substrate to NAD+, defining molecular function.

This domain architecture compels the molecular function formalized as GO:0005515 (molecular_function). The Rossmann fold (IPR020828/IPR036291) necessitates NAD(P) engagement, while the catalytic core (IPR020829) and active-site signature (IPR020830) enforce the dehydrogenase mechanism. In a type I framework (IPR006424), the enzyme’s chemistry class is that of an NAD-dependent oxidoreductase acting on an aldehyde/oxo group, with GAPDH lineage biasing toward NAD+.

From function to process, this chemistry feeds directly into carbohydrate breakdown and energy harvesting. The presence of a GAPDH-type I scaffold and triose-phosphate chemistry positions the protein in the breakdown of sugars through glycolysis—an early-to-mid pathway node that manages glyceraldehyde-3-phosphate flux. Thus, the architecture drives participation in GO:0006096 (glycolytic process), coupling substrate oxidation to NADH production and downstream ATP generation.

Cellular localization follows from solubility and pathway context. Type I GAPDHs are soluble cytosolic tetramers in many systems, and glycolysis predominantly proceeds in the cytoplasm. The soluble, non-membranous architecture implied by the Rossmann/catalytic tandem and absence of transmembrane features supports a cytoplasmic residence, aligning with GO:0005737 (cytoplospherm). This cytosolic setting provides immediate access to glycolytic intermediates and nucleotide pools.

Mechanistically, I hypothesize a soluble tetramer that binds NAD+ at the N-terminal Rossmann domain and executes thiohemiacetal chemistry via the Cys-centered active site (150–157). Substrate binding induces domain closure that aligns catalytic residues in the C-terminal domain (157–314) to form and resolve acyl- and imine-like intermediates, funneling reducing equivalents to NAD+. In the broader cellular milieu, this enzyme likely assembles transient complexes with other glycolytic enzymes—such as enolases and aldolases—to channel triose phosphates efficiently. Additional moonlighting interactions with cytoskeletal or RNA-binding partners may tune localization and regulation, but the primary operational hub remains a cytoplasmic glycolytic node that converts triose phosphate flux into reduced cofactors for energy metabolism.

### Functional Summary
A soluble cytoplasmic oxidoreductase that assembles a NAD-binding module with a catalytic core to drive early glycolytic chemistry on triose phosphate substrates. By binding NAD+ through an N-terminal Rossmann-like fold and executing cysteine-centered dehydrogenase chemistry in its C-terminal domain, it channels electron flow to generate reducing equivalents that feed energy-yielding pathways in central carbon metabolism. Its tetrameric architecture and lack of membrane features position it as a cytosolic hub coordinating glycolytic flux.

### UniProt Summary
Involved in glycolysis.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0005488
Binding
GO:0098772
Molecular Function Regulator Activity
GO:0030234
Enzyme Regulator Activity
GO:0005515
GO:0005515 GO:0005515 GO:0005515
GO:0140678
Molecular Function Inhibitor Activity
GO:0042802
Identical Protein Binding
GO:0019904
Protein Domain Specific Binding
GO:0061134
Peptidase Regulator Activity
GO:0004857
Enzyme Inhibitor Activity
GO:0061135
Endopeptidase Regulator Activity
GO:0030414
Peptidase Inhibitor Activity
GO:0097718
Disordered Domain Specific Binding
GO:0004866
Endopeptidase Inhibitor Activity
Biological Process
GO:0008150
Biological_process
GO:0048518
Positive Regulation Of Biological Process
GO:0050789
Regulation Of Biological Process
GO:0044419
Biological Process Involved In Interspecies Interaction Between Organisms
GO:0002376
Immune System Process
GO:0065007
Biological Regulation
GO:0050896
Response To Stimulus
GO:0009987
Cellular Process
GO:0048519
Negative Regulation Of Biological Process
GO:0009605
Response To External Stimulus
GO:0023056
Positive Regulation Of Signaling
GO:0042221
Response To Chemical
GO:0048584
Positive Regulation Of Response To Stimulus
GO:0019222
Regulation Of Metabolic Process
GO:0006955
Immune Response
GO:0051240
Positive Regulation Of Multicellular Organismal Process
GO:0051239
Regulation Of Multicellular Organismal Process
GO:0009892
Negative Regulation Of Metabolic Process
GO:0009607
Response To Biotic Stimulus
GO:0050794
Regulation Of Cellular Process
GO:0048583
Regulation Of Response To Stimulus
GO:0009893
Positive Regulation Of Metabolic Process
GO:0051716
Cellular Response To Stimulus
GO:0023051
Regulation Of Signaling
GO:0065009
Regulation Of Molecular Function
GO:0006950
Response To Stress
GO:0048523
Negative Regulation Of Cellular Process
GO:0051707
Response To Other Organism
GO:0048522
Positive Regulation Of Cellular Process
GO:0009967
Positive Regulation Of Signal Transduction
GO:0050790
Regulation Of Catalytic Activity
GO:0051172
Negative Regulation Of Nitrogen Compound Metabolic Process
GO:0043207
Response To External Biotic Stimulus
GO:0010604
Positive Regulation Of Macromolecule Metabolic Process
GO:0044092
Negative Regulation Of Molecular Function
GO:0009966
Regulation Of Signal Transduction
GO:0006952
Defense Response
GO:0060255
Regulation Of Macromolecule Metabolic Process
GO:0001817
Regulation Of Cytokine Production
GO:0031324
Negative Regulation Of Cellular Metabolic Process
GO:0010033
Response To Organic Substance
GO:0045087
Innate Immune Response
GO:0098542
Defense Response To Other Organism
GO:0009894
Regulation Of Catabolic Process
GO:0010646
Regulation Of Cell Communication
GO:0070887
Cellular Response To Chemical Stimulus
GO:0010605
Negative Regulation Of Macromolecule Metabolic Process
GO:0006959
Humoral Immune Response
GO:0009889
Regulation Of Biosynthetic Process
GO:0051171
Regulation Of Nitrogen Compound Metabolic Process
GO:0010647
Positive Regulation Of Cell Communication
GO:0031323
Regulation Of Cellular Metabolic Process
GO:0009890
Negative Regulation Of Biosynthetic Process
GO:0001819
Positive Regulation Of Cytokine Production
GO:0080090
Regulation Of Primary Metabolic Process
GO:0019730
Antimicrobial Humoral Response
GO:0043086
Negative Regulation Of Catalytic Activity
GO:0034097
Response To Cytokine
GO:0010556
Regulation Of Macromolecule Biosynthetic Process
GO:0051246
Regulation Of Protein Metabolic Process
GO:0071310
Cellular Response To Organic Substance
GO:0051336
Regulation Of Hydrolase Activity
GO:0051248
Negative Regulation Of Protein Metabolic Process
GO:0010506
Regulation Of Autophagy
GO:0010628
Positive Regulation Of Gene Expression
GO:0010468
Regulation Of Gene Expression
GO:0032479
Regulation Of Type I Interferon Production
GO:0034248
Regulation Of Amide Metabolic Process
GO:0032481
Positive Regulation Of Type I Interferon Production
GO:0031326
Regulation Of Cellular Biosynthetic Process
GO:1902533
Positive Regulation Of Intracellular Signal Transduction
GO:0010558
Negative Regulation Of Macromolecule Biosynthetic Process
GO:0031327
Negative Regulation Of Cellular Biosynthetic Process
GO:0034341
Response To Type II Interferon
GO:0031329
Regulation Of Cellular Catabolic Process
GO:0010629
Negative Regulation Of Gene Expression
GO:1902531
Regulation Of Intracellular Signal Transduction
GO:0034249
Negative Regulation Of Amide Metabolic Process
GO:0017148
Negative Regulation Of Translation
GO:0051346
Negative Regulation Of Hydrolase Activity
GO:0030162
Regulation Of Proteolysis
GO:0016241
Regulation Of Macroautophagy
GO:0061844
Antimicrobial Humoral Immune Response Mediated By Antimicrobial Peptide
GO:0052547
Regulation Of Peptidase Activity
GO:0071345
Cellular Response To Cytokine Stimulus
GO:0043122
Regulation Of I-KappaB Kinase/NF-KappaB Signaling
GO:2000112
Regulation Of Cellular Macromolecule Biosynthetic Process
GO:0043123
Positive Regulation Of I-KappaB Kinase/NF-KappaB Signaling
GO:0006417
Regulation Of Translation
GO:0045861
Negative Regulation Of Proteolysis
GO:0071346
Cellular Response To Type II Interferon
GO:2000113
Negative Regulation Of Cellular Macromolecule Biosynthetic Process
GO:0010608
Post-Transcriptional Regulation Of Gene Expression
GO:0052548
Regulation Of Endopeptidase Activity
GO:0010466
Negative Regulation Of Peptidase Activity
GO:0010951
Negative Regulation Of Endopeptidase Activity
Cellular Component
GO:0005575
Cellular_component
GO:0110165
Cellular Anatomical Entity
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0031975
Envelope
GO:0016020
Membrane
GO:0005829
Cytosol
GO:0071944
Cell Periphery
GO:0005737
GO:0005737 GO:0005737 GO:0005737
GO:0012505
Endomembrane System
GO:0031090
Organelle Membrane
GO:0031967
Organelle Envelope
GO:0005635
Nuclear Envelope
GO:0043229
Intracellular Organelle
GO:0043227
Membrane-Bounded Organelle
GO:0005886
Plasma Membrane
GO:0031965
Nuclear Membrane
GO:0043231
Intracellular Membrane-Bounded Organelle
GO:0005634
Nucleus

### InterPro Domains
1
335
IPR020831
IPR020828
IPR036291
IPR006424
IPR020830
IPR020829
Domain Details
IPR020831
Glyceraldehyde/Erythrose phosphate dehydrogenase family (family) [3-334]
IPR020828
Glyceraldehyde 3-phosphate dehydrogenase, NAD(P) binding domain (domain) [4-152]
IPR036291
NAD(P)-binding domain superfamily (homologous_superfamily) [4-173]
IPR006424
Glyceraldehyde-3-phosphate dehydrogenase, type I (family) [5-326]
IPR020830
Glyceraldehyde 3-phosphate dehydrogenase, active site (active_site) [150-157]
IPR020829
Glyceraldehyde 3-phosphate dehydrogenase, catalytic domain (domain) [157-314]

---
*Generated by [BioReason](https://bioreason.net)*
