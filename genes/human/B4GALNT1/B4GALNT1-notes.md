# B4GALNT1 (Q00973) — review notes

## Identity and overview

- HGNC symbol **B4GALNT1** (synonyms GALGT, SIAT2); UniProt **Q00973** (B4GN1_HUMAN); gene on chromosome 12q13.3.
- Product: **Beta-1,4 N-acetylgalactosaminyltransferase 1**, also called **GM2/GD2 synthase** and **GalNAc-T**; **EC 2.4.1.92** [file:human/B4GALNT1/B4GALNT1-uniprot.txt "RecName: Full=Beta-1,4 N-acetylgalactosaminyltransferase 1"; "AltName: Full=GM2/GD2 synthase"; "EC=2.4.1.92"].
- Type II single-pass Golgi membrane protein (signal-anchor): TOPO_DOM 1..7 cytoplasmic, TRANSMEM 8..25, TOPO_DOM 26..533 lumenal [file:human/B4GALNT1/B4GALNT1-uniprot.txt "Single-pass type II membrane protein"].
- Belongs to the **glycosyltransferase 2 family** (CAZy GT12); GT-A fold (Gene3D 3.90.550.10) [file:human/B4GALNT1/B4GALNT1-uniprot.txt "Belongs to the glycosyltransferase 2 family."].
- Homodimer, disulfide-linked (antiparallel catalytic domains) [file:human/B4GALNT1/B4GALNT1-uniprot.txt "SUBUNIT: Homodimer; disulfide-linked."]; established biochemically in [PMID:11018043 "Disulfide bonds of GM2 synthase homodimers. Antiparallel orientation of the catalytic domains."].

## Molecular function / catalytic activity

- Committed step of **complex ganglioside biosynthesis**: transfers GalNAc (beta-1,4) from **UDP-GalNAc** onto the sialylated (or neutral) lactosylceramide-based precursors. Core reaction:
  `ganglioside GM3 + UDP-GalNAc -> ganglioside GM2 + UDP + H(+)` (EC 2.4.1.92, RHEA:12588) [file:human/B4GALNT1/B4GALNT1-uniprot.txt "a ganglioside GM3 (d18:1(4E)) + UDP-N-acetyl-alpha-D-"].
- UniProt FUNCTION: "Involved in the biosynthesis of gangliosides GM2, GD2, GT2 and GA2 from GM3, GD3, GT3 and GA3, respectively." [file:human/B4GALNT1/B4GALNT1-uniprot.txt "Involved in the biosynthesis of gangliosides GM2, GD2, GT2"].
- Also acts on **GD3 -> GD2** (RHEA:43272 / RHEA:41816) and on **LacCer -> GA2 (asialo-GM2)** (RHEA:47564 / RHEA:62516) [file:human/B4GALNT1/B4GALNT1-uniprot.txt "a ganglioside GA2 (d18:1(4E))"].
- The enzyme thus feeds the **a-series (GM2->GM1...), b-series (GD2->GD1b...) and o-series (GA2->GA1...)** complex gangliosides; it is the branch point committing GM3/GD3 to the complex pathways.
- Expression cloning established that the cDNA transfers GalNAc onto GM3 and GD3 by a beta-1,4 linkage to make GM2 and GD2 [PMID:1601877 "catalyze the transfer of GalNAc onto GM3 and GD3 by a beta 1,4 linkage, resulting in the synthesis of GM2 and GD2"]; it "suggest that these cDNAs derive from the UDP-GalNAc: GM3/GD3 beta 1,4 N-acetylgalactosaminyltransferase (EC 2.4.1.92) gene." [PMID:1601877 "UDP-GalNAc: GM3/GD3 beta 1,4"].
- In-vitro biochemistry: membrane preparations of transfectants showed "de novo synthesis of GM2 or GD2 in in vitro assays using GM3 or GD3, respectively, as ganglioside acceptors." [PMID:7487055 "de\nnovo synthesis of GM2 or GD2 in in vitro assays using GM3 or GD3, respectively"] — note this quote spans a line wrap; use the substring "novo synthesis of GM2 or GD2 in in vitro assays using GM3 or GD3, respectively".
- Substrate specificity (fusion enzyme + transfectant extracts): produces "not only GM2 and GD2, but also asialo-GM2, GalNAc-sialylparagloboside, and Gal-NAc-GD1a from appropriate acceptors" — the minor acceptors at ~1-3% efficiency of GM2/GD2 [PMID:7890749 "not only GM2 and \nGD2, but also asialo-GM2"]. Kinetics: KM 500 uM for GM3, 40 uM for lactosylceramide [file:human/B4GALNT1/B4GALNT1-uniprot.txt "KM=500 uM for GM3"; "KM=40 uM for lactosylceramide"].
- **The specific GO MF is GO:0003947** "(N-acetylneuraminyl)-galactosylglucosylceramide N-acetylgalactosaminyltransferase activity" — this is exactly the GM3->GM2 GalNAc-transferase step (verified label in go.db). This is the informative core MF; GO:0008376 (acetylgalactosaminyltransferase activity) and GO:0016758 (hexosyltransferase activity) are its correct-but-general parents.

## Biological process / pathway

- **Ganglioside biosynthetic process** (GO:0001574) is the core BP; supported by IDA/IMP in humans [PMID:7487055; PMID:7890749; PMID:1601877].
- Relative levels of B4GALNT1 vs competing sialyltransferases dictate cell ganglioside composition; over-expression redirected synthesis "away from the b pathway to the a pathway" [PMID:7487055 "away from the b pathway to the a pathway"].
- UniProt PATHWAY: "Sphingolipid metabolism." [file:human/B4GALNT1/B4GALNT1-uniprot.txt "PATHWAY: Sphingolipid metabolism."]. Reactome places it in "Glycosphingolipid biosynthesis" (R-HSA-9840309) via reaction R-HSA-8856223 "B4GALNT1 dimer transfers GalNAc to gangliosides".

## Subcellular location

- **Golgi apparatus membrane**, single-pass type II [file:human/B4GALNT1/B4GALNT1-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"]. Consistent with Golgi-resident glycosyltransferase acting in the ganglioside assembly line. GO:0000139 (Golgi membrane) is the precise CC term; GO:0005794 (Golgi apparatus) is its parent; GO:0016020 (membrane) is a very general (ProtInc/TAS) call.

## Disease

- **Autosomal recessive spastic paraplegia 26 (SPG26; MIM:609195)** — a complicated hereditary spastic paraplegia with intellectual disability, peripheral neuropathy, dysarthria, cerebellar and extrapyramidal signs, cortical atrophy [file:human/B4GALNT1/B4GALNT1-uniprot.txt "Spastic paraplegia 26, autosomal recessive (SPG26)"]. Causative variants R300C (VAR_070235) and D433A (VAR_070236) identified in [PMID:23746551 "Alteration of ganglioside biosynthesis responsible for complex hereditary spastic paraplegia."]. This ties loss of complex-ganglioside synthesis to neurodegeneration.

## Structure

- Three X-ray structures (PDB 9H6J/9H6K/9H6L, residues 47-533) [file:human/B4GALNT1/B4GALNT1-uniprot.txt "PDB; 9H6J"]. Interchain disulfides (C80-C412, C82-C529) plus intrachain C429-C476 from [PMID:11018043].

## Annotation review reasoning (summary)

- **Core MF**: GO:0003947 (GM2/GM3-type GalNAc-transferase). ACCEPT the IDA/IMP/TAS annotations to this term; the IEA to same is redundant-but-correct. Keep GO:0008376 (IBA/IEA/ARBA) as correct-but-general parent (KEEP_AS_NON_CORE / general). GO:0016758 hexosyltransferase (InterPro IEA) is an even more general parent — correct but over-general (MARK/general).
- **Core BP**: GO:0001574 ganglioside biosynthetic process — ACCEPT the human IDA/IMP; IBA/IEA/Ensembl-IEA to same term are correct. GO:0006687 glycosphingolipid metabolic process and GO:0005975 carbohydrate metabolic process (ProtInc TAS) are correct but general; GO:1901135 carbohydrate derivative metabolic process (ARBA IEA) is very general.
- **Core CC**: GO:0000139 Golgi membrane — ACCEPT (multiple ISS/IEA/TAS). GO:0005794 Golgi apparatus (ISS) is a correct parent; GO:0016020 membrane (ProtInc TAS) is uninformatively general.
- No experimental annotation is contradicted; no REMOVE of experimental annotations. IEA-only very-general terms are kept but flagged as over-general rather than removed, per policy (they are not *wrong*).
