# SUR1 (CSG1/BCL21; YPL057C, P33300) notes

## Identity and activity
- GT32 (OCH1-like) glycosyltransferase; catalytic subunit of IPC mannosyltransferase, IPC + GDP-Man -> MIPC (EC 2.4.1.370) [UniProt:P33300] [PMID:9323360 "Like CSG2, SUR1/CSG1 is required for IPC mannosylation."].
- Similarity to OCH1 [PMID:9323360 "A 93-amino acid stretch of Csg1p shows 29% identity with the alpha-1, 6-mannosyltransferase encoded by OCH1."].
- Redundant paralog CSH1 (YBR161W) with different substrate specificity; csg1 csh1 double mutant has no mannosylated sphingolipids [PMID:12954640 "Deltacsg1 cells exhibited only a reduction in the synthesis of mannosylated sphingolipids compared with wild-type cells, whereas the Deltacsg1 Deltacsh1 double deletion mutant exhibited a total loss."].
- Two complexes with regulatory subunit Csg2 [PMID:12954640 "These results suggested that two distinct inositol phosphorylceramide mannosyltransferase complexes, Csg1p-Csg2p and Csh1p-Csg2p, exist."].

## Location
- UniProt: membrane, multi-pass (ECO:0000305). GOA: Golgi (NAS, PMID:12954640); vacuole/vacuolar membrane only from HTP datasets (PMID:26928762, PMID:19001347).

## Curation decisions
- Protein binding (IPI with CSG2) removed as uninformative; captured by mannosyltransferase complex (GO:0031501).
- GO:0006676 M(IP)2C metabolic process kept non-core: Sur1 makes MIPC, the precursor that Ipt1 converts to M(IP)2C. Ontology oddity: GO:0006676 is_a GPI anchor metabolic process.
- Module note: SUR1 and CSH1 are paralogous catalytic subunits, both requiring CSG2; YeastPathways reaction (IPC + GDP-Man -> MIPC) is correct.
