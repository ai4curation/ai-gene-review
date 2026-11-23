# BPP2 E (O64313 / TAP_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `E`
- **UniProt ID**: `O64313` (`TAP_BPP2`)
- **Protein**: Tail assembly protein E / gpE (91 aa, 10.3 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:12426340** (Christie et al., 2002, *J. Bacteriol.*):
   - Sequenced the `E` and `E'` coding region in the `FII-E-T-U-D` tail operon and demonstrated that ribosomes translating gene `E` undergo a programmed -1 frameshift near the 3' end of `E` (~10% efficiency) at a slippery heptanucleotide (`TTTAAAA`) to produce the extended protein `gpE+E'` (`O64312`).
   - Showed that both `gpE` and `gpE+E'` are essential for P2 tail assembly (comparable to lambda `gpG` and `gpGT`), that `Eam30` results in a complete lack of tails, and noted prior evidence (Lengyel et al., 1974) that the tape measure protein `gpT` is unstable in the absence of `gpE`, supporting a chaperone/scaffold role in stabilizing `gpT` during tail tube polymerization.
   - Quotes:
     - `"Work described here demonstrates that this reading frame encodes an essential P2 function and that ribosomes translating gene E undergo a programmed frameshift near the 3′ end of the gene about 10% of the time and enter the −1 reading frame. The resulting 15.4-kDa protein shares 85 N-terminal amino acids (aa) with gpE and contains a C-terminal extension encoded by the overlapping reading frame. This extended protein has been designated gpE+E′."`
     - `"Gene E was originally defined by the ts mutation 55 ( 26 ); nonsense mutation am30 lies in the same complementation group and was shown by Lengyel et al. ( 24 ) to result in a lack of tails."`
     - `"The role of gpE is unknown; Lengyel et al. ( 24 ) reported that the product of gene T appears to be unstable in the absence of gpE and suggested that gpE plays a role in stabilizing gpT."`

## Annotation Review Decisions
- `GO:0075523` (`viral translational frameshifting`, IEA): **REMOVE** — gpE is the conventional 0-frame translation product of gene `E`; the `E` mRNA contains a slippery sequence where host ribosomes undergo programmed -1 frameshifting to synthesize `gpE+E'`, and gpE protein itself does not perform or regulate translational frameshifting.
- `GO:0098003` (`viral tail assembly`, IEA): **ACCEPT** — gpE is essential for P2 tail morphogenesis (`Eam30` and `Ets55` mutants fail to assemble tails).
- **NEW** `GO:0044183` (`protein folding chaperone`, IMP, `PMID:12426340`): gpE acts with gpE+E' as a cytosolic tail assembly chaperone that coats and stabilizes the tape measure protein gpT prior to tail tube (gpFII) polymerization.
- **NEW** `GO:0030430` (`host cell cytoplasm`, IDA, `PMID:12426340`): gpE functions in the host cell cytoplasm during tail assembly and is not incorporated into mature virions.
