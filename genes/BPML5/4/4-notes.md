# Mycobacteriophage L5 Gene 4 (gp4, Q05251) Notes

## Overview
- **Gene symbol**: `4`
- **UniProt ID**: `Q05251` (`VG04_BPML5`)
- **Length**: 98 AA (11.1 kDa)
- **Organism**: Mycobacterium phage L5 (`NCBITaxon:31757`)

## Genomic Context and Domain Architecture
- Gene `4` is located in the left arm of the mycobacteriophage L5 genome just upstream of the putative small terminase subunit gene `5` [PMID:8459766, "We describe here the complete DNA sequence of the L5 genome and initial characterization of L5 virion structure and gene expression."].
- L5 gp4 is a 98-residue protein containing a canonical HNH homing endonuclease domain (residues 38-73; `PF01844`, `IPR002711`, `IPR003615`, `cd00085`, `SM00507`) [file:BPML5/4/4-uniprot.txt, "DR   InterPro; IPR002711; HNH."].
- The HNH fold (`beta-beta-alpha-Me` finger) in gp4 includes two conserved CxxC zinc-binding motifs (`CQINGPGCV` at residues 31-39 and `CHVCH` at residues 64-68) that coordinate a structural zinc ion, alongside the catalytic His/Asn residues (`DVDHIKRGNDHSRSN`) and a basic C-terminal tail (residues 75-98).
- Therefore, `GO:0004519` (`endonuclease activity`) and `GO:0008270` (`zinc ion binding`) are both supported by the HNH domain architecture, while `GO:0003676` (`nucleic acid binding`) is refined (`MODIFY`) to `GO:0003677` (`DNA binding`).
