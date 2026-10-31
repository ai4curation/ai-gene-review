# C4 (P11189) — Curation Notes

## Summary
- **Gene symbol**: `C4` (`c4`)
- **UniProtKB**: `P11189` (`IMM4_BPP1`, 66 aa predicted polypeptide; `PE 4: Predicted`)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Biological Reality**: Although `P11189` was created from a hypothetical 66-codon ORF proposed in the original nucleotide sequence of the `c4` locus (Baumstark & Scott 1987, `PMID:3811234`), subsequent genetic and biochemical studies (Citron & Schuster 1990; Biere, Citron & Schuster 1992; reviewed in Łobocka et al. 2004, `PMID:15489417`) demonstrated conclusively that the functional product of the `c4` gene in the `immI` immunity region is a **77-nt processed antisense RNA (C4 RNA)**, not a protein.

## Literature Evidence
- **Baumstark & Scott 1987 (`PMID:3811234`)**:
  - Localized the `c4` immunity determinant to a 335-bp DNA fragment of P1EcoRI-9 and tentatively proposed a 66-aa open reading frame prior to the discovery that `c4` encodes an antisense RNA.
  - Quote: `"The c4 gene of phage P1 has been localized to 335 bp of the P1EcoRI-9 fragment, within 50 bp of the EcoRI-9/14 junction. DNA sequence analysis of this fragment reveals a single open reading frame of 66 amino acids."`
- **Heisig, Severin,els & Schuster 1989 (`PMID:2585500`)**:
  - Sequenced the `immI` region (`c4` and `ant/reb`) and showed that `c4` negatively regulates synthesis of the Ant1/Ant2 antirepressor proteins.
  - Quote: `"The immI region of bacteriophage P1 includes the ant/reb gene, which encodes the antirepressor protein, and the c4 gene, which encodes a repressor molecule that negatively regulates antirepressor synthesis."`
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Detailed the mechanism of C4 antisense RNA in the `c4-icd-ant1/2` operon (`immI`): C4 RNA is excised by RNase P (and other host ribonucleases) as a 77-nt cloverleaf-like RNA from the leader of the `c4-icd-ant1/2` polycistronic transcript. Two exposed single-stranded loops (`b'` and `a'`) base-pair with complementary sequences (`a2` and `b2`) in the nascent `c4-icd-ant1/2` mRNA, occluding the ribosome-binding site of `icd` (which is translationally coupled to `ant1`) and triggering premature Rho-dependent transcription termination of `ant1/2`.
  - Quote: `"A trans -acting RNA (the c 4 product) regulates Ant1/2 synthesis in a novel way, being excised from a transcript on which lies its site of action."`
  - Quote: `"A 77-bp antisense RNA encoded by c 4 regulates expression of downstream genes in its own message"`
  - Quote: `"Two short single-stranded regions, b′ and a′, exposed in its cloverleaf-like structure, block translation of icd (and of translationally coupled ant1 ) by interaction with the complementary regions, a2 and b2, in the c 4 icd ant1/2 mRNA. The interaction occludes the RBS in front of the icd gene"`

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA: `GO_REF:0000043`): **REMOVE**. This annotation is an automated keyword-mapping artifact from the historical UniProtKB entry `P11189` (`KW-0238 DNA-binding`), which assumed `c4` encoded a DNA-binding repressor protein (`PMID:3811234`). In reality, `c4` functions exclusively as a 77-nt antisense RNA that base-pairs with complementary regions of the `c4-icd-ant1/2` mRNA to repress translation of `icd` and `ant1` (`PMID:15489417`); it does not bind DNA.
