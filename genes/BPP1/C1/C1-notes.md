# C1 (P13121) — Curation Notes

## Summary
- **Gene symbol**: `C1` (`c1`)
- **UniProtKB**: `P13121` (`IMM1_BPP1`, 283 aa, 32.5 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Master transcriptional repressor of bacteriophage P1 lytic functions (`immC` locus), responsible for establishing and maintaining the prophage in the lysogenic plasmid state.

## Literature Evidence
- **Eliason & Sternberg 1987 (`PMID:3430609`)**:
  - Identified 11 C1 repressor binding sites across the P1 genome and derived the 17-bp asymmetric consensus operator sequence `5'-ATTGCTCTAATAAATTT-3'`.
  - Quote: `"The repressor of bacteriophage P1, encoded by the c1 gene, is responsible for maintaining a P1 prophage in the lysogenic state."`
  - Quote: `"From these sites we have derived the consensus binding site sequence ATTGCTCTAATAAATTT."`
- **Osborne, Yao & Lehnherr / Dreiseikelmann, Velleman & Schuster 1988 (`PMID:2678003`)**:
  - Sequenced and compared the `c1` repressor genes of phages P1 and P7 (`M22684`), demonstrating identical 283-aa C1 protein sequences despite nucleotide differences, and showed transcriptional repression from an upstream promoter (`Pc1` / `Op99a-b`).
  - Quote: `"Plasmids expressing the c1 gene from either phage cause the repression of transcription from a cloned promoter situated upstream of P1c1."`
- **Heinzel, Velleman & Schuster 1989 (`PMID:2678004`)**:
  - Demonstrated that C1 repressor binds operator DNA as a monomer in solution, that operator DNA binding is sensitive to the sulfhydryl reagent N-ethylmaleimide (via three cysteine residues in the C-terminal half), and that a 14-kDa cyanogen bromide C-terminal fragment retains sequence-specific operator DNA-binding activity.
  - Quote: `"Binding to the operator DNA of c1 repressor is sensitive to N-ethylmaleimide."`
  - Quote: `"a 14-kDa C-terminal repressor fragment obtained by cyanogen bromide cleavage retains DNA binding properties."`
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Comprehensive genome-wide review of P1 multipartite immunity (`immC`, `immI`, `immT`). Identified 20 C1-binding operators (`Op`) across the P1 genome controlling 17 genes/operons (including `coi`, `c1`, `c4-icd-ant`, `kilA-repL`, `ban`, `ssb`, `sit`, `lxc`, `ulx`, `darB`, `pdcB`, and `pacA`).
  - C1 repression is modulated by Lxc (`bof`, `immT`), which forms a ternary complex with C1 and operator DNA and promotes DNA looping at bivalent operators, and is antagonized by Coi (`immC`) and Ant1/Ant2 (`immI`).
  - Quote: `"The key repressor of P1 lytic functions is the C1 protein, encoded by c 1 within ImmC"`
  - Quote: `"C1 protein exists as a monomer in solution and binds to a score of widely dispersed operators"`

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA: `GO_REF:0000120`): **MODIFY** to `GO:0001217` (`DNA-binding transcription repressor activity`) and `GO:0000976` (`transcription cis-regulatory region binding`). C1 is experimentally characterized as a sequence-specific transcriptional repressor binding 17-bp operator sites across the P1 genome (`PMID:3430609`, `PMID:2678003`, `PMID:2678004`, `PMID:15489417`).
