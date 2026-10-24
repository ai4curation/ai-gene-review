# Curation Notes: Pseudomonas phage phiKZ `PHIKZ144` (`KZ144` / `gp144`, UniProt `Q8SD18`)

## Identity & Taxonomic Context
- **Gene / Symbol**: `PHIKZ144` (`gp144`, `KZ144`)
- **Organism**: *Pseudomonas phage phiKZ* (`NCBITaxon:2905945`), giant myovirus infecting *Pseudomonas aeruginosa*.
- **UniProt Accession**: `Q8SD18` (260 AA, ~28.8 kDa, EC `4.2.2.n1`).
- **Structural Data**: X-ray crystal structures of unbound (`PDB:3BKH`, 2.6 A) and chitotetraose-bound (`PDB:3BKV`, 2.0 A) `gp144` [PMID:18160394], plus `PDB:9XPS`.

## Molecular Function & Modular Architecture
- **Modular Endolysin with Lytic Transglycosylase Activity**: `PHIKZ144` (`KZ144` / `gp144`) is a 260-residue, predominantly alpha-helical modular endolysin composed of an N-terminal peptidoglycan-binding domain (`PBD`, `residues 9–69`, `Pfam:PF01471`) and a C-terminal glycoside hydrolase family 23 (`GH23`) catalytic transglycosylase domain (`residues 70–260`, core `106–210`, `Pfam:PF01464`) connected by a charged linker [PMID:17697255, PMID:18160394, PMID:19348786].
- **Non-Hydrolytic Cleavage Mechanism**: Mass spectrometry of peptidoglycan degradation products proves that `gp144` is a lytic transglycosylase (not a hydrolytic lysozyme) that cleaves the beta-1,4-glycosidic bond between *N*-acetylmuramic acid (`MurNAc`) and *N*-acetylglucosamine (`GlcNAc`) with concomitant intramolecular transglycosylation to form a `1,6-anhydro-N-acetylmuramic acid` (`1,6-anhydro-MurNAc`) ring (`GO:0008933` `peptidoglycan lytic transglycosylase activity`, `GO:0140100` `lytic exotransglycosylase activity`) [PMID:17233731, PMID:18160394].
- **Dual Active Site**: While `Glu115` (paired with `Tyr197`) serves as the canonical primary catalytic proton donor in the substrate-binding groove [PMID:17697255, PMID:18160394], `E115A` retains ~30% residual muralytic activity; site-directed mutagenesis revealed a secondary catalytic center involving `Glu178` and `Tyr147`, and only simultaneous mutation (`E115A/E178A` or `E115A/Y197F`) completely abolishes peptidoglycan degradation [PMID:28461978].
- **High-Affinity Peptidoglycan-Binding Domain**: The N-terminal `PBD` (`residues 9–69`) binds broadly across Gram-negative (A1gamma chemotype) peptidoglycans with an equilibrium affinity constant `Ka = 2.95 x 10^7 M^-1` (`~1.2 x 10^5` binding sites per *P. aeruginosa* cell) [PMID:17697255, PMID:19348786].
- **Role in Host Cell Lysis / Viral Release**: Expression of `gp144` in *E. coli* causes rapid host cell lysis, and purified `gp144` (`210,000 units/mg`) degrades outer-membrane-permeabilized *P. aeruginosa* and other Gram-negative bacteria to mediate progeny virion release at the end of the lytic cycle (`GO:0044659` `viral release from host cell by cytolysis`) [PMID:17233731, PMID:17697255].

## Curation Decisions
- **ACCEPT**: `GO:0008933` (`peptidoglycan lytic transglycosylase activity`, IDA from `PMID:17233731`), `GO:0140100` (`lytic exotransglycosylase activity`, EXP from `PMID:17233731` and `PMID:28461978`), and `GO:0044659` (`viral release from host cell by cytolysis`, IDA from `PMID:17233731`).
- **TOO_GENERAL**: `GO:0003824` (`catalytic activity`), `GO:0016829` (`lyase activity`, entailed by `GO:0008933` / `GO:0140100`), and `GO:0031640` (`killing of cells of another organism`, entailed by `GO:0044659`).
- **REMOVE**: `GO:0042742` (`defense response to bacterium`, IEA from `KW-0081` Antimicrobial) — automated keyword mapping error; a phage endolysin mediates viral egress by host cell lysis, not an immune defense response against bacteria.
