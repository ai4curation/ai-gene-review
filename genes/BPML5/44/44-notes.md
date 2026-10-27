# Curation Notes: Mycobacteriophage L5 gene 44 (DNA polymerase Gp44, Q05254)

## Summary
- **Gene symbol**: `44`
- **UniProt ID**: `Q05254` (`DPOL_BPML5`)
- **Organism**: Mycobacterium phage L5 (`NCBITaxon:31757`)
- **Protein length**: 595 amino acids (66,221 Da)
- **EC numbers**: EC 2.7.7.7 (DNA-directed DNA polymerase); EC 3.1.11.- (3'-5' exonuclease)

## Literature & Bioinformatic Findings
- Identified in the genome sequence of mycobacteriophage L5 as the phage-encoded DNA polymerase I (Pol A) homolog [PMID:8459766, "We describe here the complete DNA sequence of the L5 genome and initial characterization of L5 virion structure and gene expression."].
- Comparative genomics with mycobacteriophage D29 confirmed conservation of the right-arm replication module across L5-like phages [PMID:9636706, "The overall organization of the D29 genome is similar to that of L5, although a 3.6 kb deletion removing the repressor gene accounts for the inability of D29 to form lysogens."].
- Domain architecture (`file:genes/BPML5/44/44-uniprot.txt`):
  - **N-terminal 3'-5' proofreading exonuclease domain** (residues 1-212; `InterPro:IPR002562` / `Pfam:PF01612` `DNA_pol_A_exo1` / `SMART:SM00474` `35EXOc`, RNase H-like superfamily `InterPro:IPR012337`), catalyzing 3'-5' single-stranded DNA exonucleolytic proofreading.
  - **C-terminal DNA polymerase type-A domain** (residues 213-595; `InterPro:IPR002298` `DNA_polymerase_A` / `Pfam:PF00476` `DNA_pol_A` / `InterPro:IPR001098` `DNA-dir_DNA_pol_A_palm_dom` / `PROSITE:PS00447` `DNA_POLYMERASE_A`), catalyzing DNA-templated DNA synthesis (`RHEA:22508`).
  - Like the Klenow fragment of bacterial DNA polymerase I and bacteriophage T7 gp5, L5 Gp44 lacks an N-terminal 5'-3' exonuclease domain.

## Review of Existing GOA Annotations
- `GO:0003887` (`DNA-directed DNA polymerase activity`), `GO:0008408` (`3'-5' exonuclease activity`), `GO:0003677` (`DNA binding`), and `GO:0039693` (`viral DNA genome replication`) are accepted (`ACCEPT`) as core functions of Gp44.
- Broader ancestor terms (`GO:0003676` `nucleic acid binding`, `GO:0004518` `nuclease activity`, `GO:0004527` `exonuclease activity`, `GO:0006260` `DNA replication`, `GO:0006261` `DNA-templated DNA replication`, `GO:0016740` `transferase activity`, `GO:0016779` `nucleotidyltransferase activity`, `GO:0016787` `hydrolase activity`, and `GO:0034061` `DNA polymerase activity`) are marked `TOO_GENERAL` because they are directly entailed by the more specific accepted terms.
