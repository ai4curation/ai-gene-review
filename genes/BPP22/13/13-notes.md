# Gene 13 (Holin / Antiholin; UniProt P09962) — Curation Notes

## Overview
- **Gene symbol**: `13`
- **UniProt accession**: `P09962` (`HOLIN_BPP22`, 108 aa, 11.7 kDa)
- **Organism**: *Salmonella* phage P22 (`NCBITaxon:10754`), host *Salmonella enterica* subsp. *enterica* serovar Typhimurium (`NCBITaxon:90371`)
- **Genomic context**: Late lysis cassette (`13`–`19`–`15`/`Rz1`), expressed during the late phase of the lytic cycle under gp23 antitermination control [PMID:2998005, PMID:11053393].

## Sequence, Domain Architecture, and Isoforms
- **Conserved domains**:
  - `InterPro:IPR006481` (`Phage_lambda_GpS_holin`)
  - `Pfam:PF05106` (`Phage_holin_3_1`)
  - `NCBIfam:TIGR01594` (`holin_lambda`)
  - `TCDB:1.E.2.1.2` (Lambda holin S family)
- **Dual translational start (`M1-K2-K3-M4`)**:
  - Gene `13` shares 89% amino acid identity with bacteriophage lambda gene *S* [PMID:2998005] and utilizes a conserved dual translational start motif (`Met1-Lys2-Lys3-Met4`) to produce two polypeptides of opposing function [PMID:7831803]:
    1. **Antiholin / Lysis inhibitor 13-108 (`P09962-1`)**: Full-length 108-aa polypeptide initiated at Met1. Contains two positive lysine residues (`Lys2`, `Lys3`) at the N-terminus that prevent insertion of the first transmembrane segment across the energized inner membrane, resulting in a 2-TM topology (cytoplasmic 1–38, TM 39–59, periplasmic 60–71, TM 72–92, cytoplasmic C-terminus 93–108). Heterodimerizes with the holin isoform to inhibit premature oligomerization and pore formation [PMID:7831803, file:BPP22/13/13-uniprot.txt].
    2. **Holin / Lysis protein 13-105 (`P09962-2`, `VSP_058251`)**: 105-aa polypeptide initiated at Met4 (lacking residues 1–3). Adopts a class I holin 3-TM topology (N-out, C-in) in the host inner membrane. Accumulates harmlessly until a critical allele-specific concentration is reached, triggering oligomerization into micron-scale inner membrane pores ("holes") that collapse the proton-motive force and release the cytoplasmic endolysin gp19 into the periplasm [PMID:7831803, file:BPP22/13/13-uniprot.txt].

## Literature Evidence
- **Rennell & Poteete (1985) [PMID:2998005]**: Cloned and sequenced wild-type and amber mutant alleles of P22 lysis genes `13` and `19`, demonstrating that `"Gene 13 encodes an 11,520-Da basic hydrophobic protein that has 89% amino acid homology to lambda S protein."`
- **Tedin et al. (1995) [PMID:7831803]**: Established that `"The Lambda S, phage 21 S, and P22 13 holin genes contain a dual translational start motif, beginning with Met1-Lys2-X-Met3. In all cases both start codons at the 5' end of the respective holin gene are utilized. The resulting polypeptides have opposing functions, with the longer product acting as an inhibitor of the shorter one."`
- **Vander Byl & Kropinski (2000) [PMID:11053393]** and **Pedulla et al. (2003) [PMID:12562822]**: Confirmed the genomic sequence and late-operon organization of gene `13`.

## GO Annotation Review
1. **`GO:0020002` (`host cell plasma membrane`, IEA `GO_REF:0000044` & ISS `GO_REF:0000024` from `UniProtKB:P03705`)**:
   - **Action**: `ACCEPT` for both rows. Both gp13 isoforms are integral multi-pass proteins of the *Salmonella* inner (cytoplasmic) membrane, directly orthologous (89% identity) to lambda S (`UniProtKB:P03705`).
2. **`GO:0031640` (`killing of cells of another organism`, IEA `GO_REF:0000043` from `UniProtKB-KW:KW-0204` Cytolysis)**:
   - **Action**: `MODIFY` to `GO:0044659` (`viral release from host cell by cytolysis`) and `GO:0140911` (`pore-forming activity`). `GO:0031640` is an overly broad UniProt keyword mapping that conflates inter-organismal toxin/predation killing with programmed bacteriophage progeny release via holin-mediated inner membrane permeabilization.
