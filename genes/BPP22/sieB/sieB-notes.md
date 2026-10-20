# Curation Notes for Salmonella phage P22 `sieB` (P38396)

## Summary of Gene Product
`sieB` (synonym `git`) encodes the superinfection exclusion protein B (SieB; UniProt `P38396`, 192 amino acids, 22.4 kDa) of *Salmonella* phage P22 [PMID:8335629]. Expressed by the P22 prophage in lysogenic *Salmonella* cells, SieB is a multi-pass integral membrane protein with two predicted alpha-helical transmembrane segments (residues 22-42 and 51-71) that mediates abortive-infection-type superinfection exclusion against heteroimmune or non-P22-escaped phages [PMID:4610993, PMID:8335629, PMID:38236051].

## Molecular Function, Biological Process, and Mechanism
- **Superinfection exclusion (`GO:0098669`)**: Unlike SieA (which blocks DNA entry across the inner membrane), the SieB system allows DNA injection and early gene expression of susceptible superinfecting phages to proceed normally until midway through the lytic cycle, when host and phage macromolecular synthesis (DNA, RNA, and protein synthesis) abruptly ceases, aborting phage progeny production and killing the superinfected cell [PMID:4610993, PMID:8335629, PMID:38236051].
- **Escape via overlapping/in-frame `esc` determinant**: P22 itself escapes SieB exclusion because it expresses an inhibitor peptide (`Esc`, escape from SieB exclusion) from an internal start site / overlapping sequence at the `sieB` locus that antagonizes SieB toxicity during P22 lytic infection [PMID:8335629].

## Subcellular Localization
- **Host cell plasma membrane (`GO:0020002`)**: SieB contains two N-terminal alpha-helical transmembrane domains (residues 22-42 and 51-71; `file:genes/BPP22/sieB/sieB-uniprot.txt`) and integrates into the host bacterial inner membrane (plasma membrane), where abortive superinfection exclusion proteins of the SieB/RexB family act to disrupt membrane integrity or macromolecular synthesis upon activation.

## Domain Architecture
- InterPro: `IPR025982` (`SieB`)
- Pfam: `PF14163` (`SieB`)
