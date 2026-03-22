# BioReason Chat Export
*Captured via automation on 2026-03-21 at 11:41 PM*

---

**Organism:** Pseudomonas putida

### Thinking Trace
I begin with the InterPro architecture. The sequence is dominated by PQQ-dependent dehydrogenase signatures: IPR017512 (PQQ-dependent dehydrogenase, methanol/ethanol family, residues 26–556) and IPR034119 (PQQ-dependent type I alcohol dehydrogenase, residues 34–583) define the enzyme class and firmly place it among soluble type I PQQ dehydrogenases that oxidize short-chain alcohols. This assignment is reinforced by IPR011047 (Quinoprotein alcohol dehydrogenase-like superfamily, residues 37–579), indicating the characteristic β-propeller scaffold. The core fold is elaborated by IPR002372 (Pyrrolo-quinoline quinone repeat domain, residues 52–538) and IPR018391 (Pyrrolo-quinoline quinone beta-propeller repeat, residues 90–528), which together specify a tandem β-propeller assembly that cradles the PQQ cofactor and creates a deep active-site cavity for alcohol oxidation. IPR001479 (Quinoprotein dehydrogenase, conserved site, residues 263–284) marks the catalytic locus that orients substrate and cofactor for hydride-equivalent transfer. The ordered layout—N-terminal PQQ-family signatures leading into extensive β-propeller repeats and a conserved catalytic patch—causally dictates a soluble quinoprotein enzyme that binds PQQ and catalyzes primary alcohol oxidation.

From this architecture, the molecular function resolves as oxidoreductase chemistry centered on PQQ. The β-propeller repeats and conserved site coordinate PQQ to abstract a hydride equivalent from the C–H bond of a primary alcohol and pass electrons to an external acceptor. This defines oxidoreductase activity acting on the CH-OH group of donors (consistent with GO:0016614) and necessitates cofactor engagement; PQQ binding is intrinsic to catalysis.

Biological process follows from the chemistry and substrate class. The methanol/ethanol family annotation (IPR017512/IPR034119) and β-propeller PQQ scaffold point to assimilation of small alcohols via sequential oxidation to aldehydes and then acids that feed central metabolism. In soil-dwelling Pseudomonads, this route channels carbon into the TCA and gluconeogenic networks. Therefore, the enzyme contributes to alcohol metabolic process and broader oxidation–reduction process that assimilates reduced carbon into core pathways.

Cellular location is implied by the soluble, β-propeller quinoprotein architecture and lack of transmembrane features: these enzymes are cytosolic. The absence of signal peptides or membrane anchors and the soluble type I designation together argue for a cytoplasmic enzyme.

Mechanistically, the enzyme likely binds PQQ within the β-propeller cavity, positions short-chain primary alcohols via hydrophobic and hydrogen-bonding contacts defined by the conserved site (263–284), and transfers reducing equivalents to a soluble electron acceptor. In bacteria, type I PQQ dehydrogenases commonly pass electrons to small-molecule acceptors such as NAD(P)+ via partner redox carriers or directly to disproportionating acceptors; downstream aldehyde dehydrogenases and acetyl-CoA–forming enzymes would capture the resulting aldehydes. I therefore hypothesize transient assemblies with aldehyde dehydrogenases and central carbon enzymes to channel products efficiently within the cytoplasm of Pseudomonas putida.

### Functional Summary
A soluble quinoprotein alcohol dehydrogenase that uses a pyrrolo‑quinoline quinone cofactor embedded in a β‑propeller scaffold to oxidize primary alcohols into their corresponding aldehydes in the cytoplasm of Pseudomonas. By coupling PQQ-mediated hydride transfer to downstream electron acceptors, it initiates the assimilation of environmental short-chain alcohols, feeding aldehyde and acyl‑intermediate pathways that ultimately supply central metabolism. Its architecture and chemistry indicate a cytosolic enzyme that supports reduced‑carbon assimilation by catalyzing primary‑alcohol oxidation.

### UniProt Summary
Probable alcohol dehydrogenase.

### GO Terms
Molecular Function
GO:0003674
Molecular_function
GO:0005488
Binding
GO:0003824
Catalytic Activity
GO:0036094
Small Molecule Binding
GO:1901363
Heterocyclic Compound Binding
GO:0048038
Quinone Binding
GO:0097159
Organic Cyclic Compound Binding
GO:0043167
Ion Binding
GO:0016491
Oxidoreductase Activity
GO:0009055
Electron Transfer Activity
GO:0046906
Tetrapyrrole Binding
GO:0043177
Organic Acid Binding
GO:0043168
Anion Binding
GO:0043169
Cation Binding
GO:0020037
Heme Binding
GO:0031406
Carboxylic Acid Binding
GO:0046872
Metal Ion Binding
GO:0005509
Calcium Ion Binding
Biological Process
GO:0008150
Biological_process
GO:0008152
Metabolic Process
GO:0009987
Cellular Process
GO:0044281
Small Molecule Metabolic Process
GO:0044237
Cellular Metabolic Process
GO:0071704
Organic Substance Metabolic Process
GO:1901615
Organic Hydroxy Compound Metabolic Process
GO:0006082
Organic Acid Metabolic Process
GO:0043436
Oxoacid Metabolic Process
GO:0019752
Carboxylic Acid Metabolic Process
GO:0032787
Monocarboxylic Acid Metabolic Process
Cellular Component
GO:0005575
Cellular_component
GO:0110165
Cellular Anatomical Entity
GO:0032991
Protein-Containing Complex
GO:1902494
Catalytic Complex
GO:0005622
Intracellular Anatomical Structure
GO:0043226
Organelle
GO:0043229
Intracellular Organelle
GO:1990204
Oxidoreductase Complex
GO:0043228
Non-Membrane-Bounded Organelle
GO:0043232
Intracellular Non-Membrane-Bounded Organelle
GO:0009579
Thylakoid

### InterPro Domains
1
595
IPR017512
IPR034119
IPR011047
IPR002372
IPR018391
IPR001479
Domain Details
IPR017512
PQQ-dependent dehydrogenase, methanol/ethanol family (family) [26-556]
IPR034119
PQQ-dependent type I alcohol dehydrogenase (family) [34-583]
IPR011047
Quinoprotein alcohol dehydrogenase-like superfamily (homologous_superfamily) [37-579]
IPR002372
Pyrrolo-quinoline quinone repeat domain (domain) [52-538]
IPR018391
Pyrrolo-quinoline quinone beta-propeller repeat (repeat) [90-528]
IPR001479
Quinoprotein dehydrogenase, conserved site (conserved_site) [263-284]

---
*Generated by [BioReason](https://bioreason.net)*
