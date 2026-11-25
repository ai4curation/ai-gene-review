# BPP2 G (P26699 / TFA_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `G`
- **UniProt ID**: `P26699` (`TFA_BPP2`)
- **Protein**: Probable tail fiber assembly protein gpG (175 aa, 20.0 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:1531648** (Haggård-Ljungquist et al., 1992, *J. Bacteriol.*):
   - Sequenced P2 genes `H` and `G` and demonstrated that `gpG` is homologous over its entire length to the tail fiber assembly proteins gpU and gpU' of phage Mu and shares a conserved domain with the tail fiber assembly chaperones of phages TuIa, TuIb, T4 (gp38), and lambda (Tfa).
   - Mapped `Gam1` and showed that gene `G` is essential for assembly of the P2 tail fibers on the virion.
   - Quote: `"Gene G of P2 probably codes for a protein required for assembly of the tail fibers of the virion. The entire G gene product is very similar to the products of genes U and U' of phage Mu; a region of these proteins is also found in the tail fiber assembly proteins of phages TuIa, TuIb, T4, and lambda."`

## Annotation Review Decisions
- `GO:0098003` (`viral tail assembly`, IEA): **MODIFY** to `GO:0098004` (`virus tail fiber assembly`).
- `GO:0098004` (`virus tail fiber assembly`, IEA): **ACCEPT**.
- **NEW** `GO:0044183` (`protein folding chaperone`, IMP, `PMID:1531648`): gpG functions as a dedicated tail fiber assembly chaperone required for the folding/oligomerization and attachment of the gpH tail fiber.
- **NEW** `GO:0030430` (`host cell cytoplasm`, ISS, `PMID:1531648`): gpG acts in the host cell cytoplasm during tail fiber maturation and is not incorporated into the mature virion.
