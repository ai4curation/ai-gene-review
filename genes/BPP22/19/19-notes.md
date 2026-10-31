# Gene 19 (Endolysin / Lysozyme; UniProt P09963) — Curation Notes

## Overview
- **Gene symbol**: `19`
- **UniProt accession**: `P09963` (`ENLYS_BPP22`, 146 aa, 16.1 kDa, EC `3.2.1.17`)
- **Organism**: *Salmonella* phage P22 (`NCBITaxon:10754`), host *Salmonella enterica* subsp. *enterica* serovar Typhimurium (`NCBITaxon:90371`)
- **Genomic context**: Late lysis cassette (`13`–`19`–`15`/`Rz1`), located immediately downstream of holin gene `13` and upstream of i-spanin gene `15` [PMID:2998005, PMID:2763468, PMID:11053393].

## Sequence, Structure, and Catalytic Mechanism
- **Conserved domains & classification**:
  - Glycoside hydrolase family 24 (`CAZy:GH24`), T4-type lysozyme / muramidase
  - `InterPro:IPR002196` (`Glyco_hydro_24`), `InterPro:IPR034690` (`Endolysin_T4_type`), `InterPro:IPR033907` (`Endolysin_autolysin`), `InterPro:IPR051018` (`Bacteriophage_GH24`), `InterPro:IPR023346` (`Lysozyme-like_dom_sf`), `InterPro:IPR023347` (`Lysozyme_dom_sf`)
  - `Pfam:PF00959` (`Phage_lysozyme`), `HAMAP:MF_04110` (`ENDOLYSIN_T4`), `CDD:cd00737` (`lyz_endolysin_autolysin`), `PANTHER:PTHR38107` / `PANTHER:PTHR38107:SF3` (`LYSOZYME RRRD-RELATED`)
- **Crystal structure & active site**:
  - Determined *ab initio* at 1.04 Å resolution by X-ray crystallography (`PDB:2ANV`, `PDB:2ANX`) [PMID:16421448].
  - Catalytic dyad / active site proton donor/acceptor residues: `Glu16` and `Asp25` (`ACT_SITE 16`, `ACT_SITE 25` by `HAMAP-Rule:MF_04110`) [file:BPP22/19/19-uniprot.txt].
  - Hydrolyzes $\beta$-(1$\rightarrow$4) linkages between *N*-acetylmuramic acid and *N*-acetyl-D-glucosamine in bacterial peptidoglycan (EC `3.2.1.17`).
- **Subcellular localization & release mechanism**:
  - Lacks an N-terminal signal peptide or SAR (signal-anchor-release) domain; starts with a single unformylated/retained N-terminal methionine as verified by direct N-terminal protein sequencing of purified gp19 [PMID:2998005].
  - Accumulates in the host cell cytoplasm (`GO:0030430`) during late infection until holin gp13 forms micron-scale pores in the inner membrane, allowing gp19 to escape into the periplasm and degrade the peptidoglycan sacculus [file:BPP22/19/19-uniprot.txt].

## Literature Evidence
- **Rennell & Poteete (1985) [PMID:2998005]**: Cloned and sequenced P22 gene `19`, purified the 15,968-Da basic protein, confirmed its N-terminal amino acid sequence, and demonstrated that plasmids expressing P22 gene `19`, lambda `R`, or T4 `e` complement both lambda $R^-$ and P22 $19^-$ mutants.
- **Casjens et al. (1989) [PMID:2763468]**: Sequenced the region from residue 111 of gp19 through gene `3`, identifying the downstream spanin gene `15`.
- **Mooers & Matthews (2006) [PMID:16421448]**: Solved the 1.04 Å X-ray crystal structure of P22 lysozyme (gp19; `PDB:2ANV`, `PDB:2ANX`) by *ab initio* direct methods.

## GO Annotation Review
1. **`GO:0003796` (`lysozyme activity`, IEA `GO_REF:0000120`)**: `ACCEPT` — core enzymatic activity (EC 3.2.1.17).
2. **`GO:0003824` (`catalytic activity`, IEA `GO_REF:0000043`)**: `MODIFY` $\rightarrow$ `GO:0003796` (`lysozyme activity`).
3. **`GO:0009253` (`peptidoglycan catabolic process`, IEA `GO_REF:0000120`)**: `ACCEPT` — direct biological process catalyzed by gp19 in the host cell wall.
4. **`GO:0016787` (`hydrolase activity`, IEA `GO_REF:0000043`)**: `MODIFY` $\rightarrow$ `GO:0003796` (`lysozyme activity`).
5. **`GO:0016798` (`hydrolase activity, acting on glycosyl bonds`, IEA `GO_REF:0000043`)**: `MODIFY` $\rightarrow$ `GO:0003796` (`lysozyme activity`).
6. **`GO:0016998` (`cell wall macromolecule catabolic process`, IEA `GO_REF:0000002`)**: `MODIFY` $\rightarrow$ `GO:0009253` (`peptidoglycan catabolic process`).
7. **`GO:0030430` (`host cell cytoplasm`, IEA `GO_REF:0000044`)**: `ACCEPT` — canonical pre-holin-triggering compartment where canonical endolysin accumulates.
8. **`GO:0031640` (`killing of cells of another organism`, IEA `GO_REF:0000043`)**: `MODIFY` $\rightarrow$ `GO:0044659` (`viral release from host cell by cytolysis`).
9. **`GO:0042742` (`defense response to bacterium`, IEA `GO_REF:0000043` from `KW-0081` Bacteriolytic enzyme)**: `REMOVE` — false positive keyword mapping; a bacteriophage endolysin degrades host peptidoglycan for progeny virion release (`GO:0044659`), not as a host antibacterial immune defense response.
10. **`GO:0044659` (`viral release from host cell by cytolysis`, IEA `GO_REF:0000104`)**: `ACCEPT` — core biological role of the P22 lysis cassette.
