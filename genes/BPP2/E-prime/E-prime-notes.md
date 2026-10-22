# BPP2 E-prime (O64312 / TAPFS_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `E-prime`
- **UniProt ID**: `O64312` (`TAPFS_BPP2`)
- **Protein**: Tail assembly protein E' / gpE+E' (142 aa, 15.4 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:12426340** (Christie et al., 2002, *J. Bacteriol.*):
   - Demonstrated that an overlapping -1 reading frame (`E'`) immediately downstream of `E` encodes the C-terminal extension of a 15.4-kDa fusion polypeptide (`gpE+E'`, 142 aa) produced when ribosomes translating `E` undergo a programmed -1 frameshift (~10% efficiency) at a slippery `TTTAAAA` site near the 3' end of `E`.
   - Site-directed mutagenesis and complementation assays proved that the `E'` extension is essential for P2 phage viability and tail assembly, and that `gpE` and `gpE+E'` are functionally analogous to the bacteriophage lambda `gpG` and `gpGT` tail assembly chaperones.
   - Quotes:
     - `"Work described here demonstrates that this reading frame encodes an essential P2 function and that ribosomes translating gene E undergo a programmed frameshift near the 3′ end of the gene about 10% of the time and enter the −1 reading frame. The resulting 15.4-kDa protein shares 85 N-terminal amino acids (aa) with gpE and contains a C-terminal extension encoded by the overlapping reading frame. This extended protein has been designated gpE+E′."`
     - `"The organizational parallel at the genetic level of λ genes G and T and P2 genes E and E′ as well as what is currently known about the functions of these genes suggests a true evolutionary relationship between the head and tail assembly genes of these phages, as observed previously by Casjens et al. ( 8 ) for the morphogenetic genes of phages λ and P22."`

## Annotation Review Decisions
- `GO:0075523` (`viral translational frameshifting`, IEA): **REMOVE** — `gpE+E'` is the polypeptide *product* of a programmed -1 ribosomal frameshift on the `E-E'` mRNA; the protein itself does not perform or regulate translational frameshifting.
- `GO:0098003` (`viral tail assembly`, IEA): **ACCEPT** — `gpE+E'` is essential for P2 tail morphogenesis.
- **NEW** `GO:0044183` (`protein folding chaperone`, IMP, `PMID:12426340`): `gpE+E'` acts with `gpE` as a cytosolic tail assembly chaperone that coats the tape measure protein (`gpT`) and recruits the tail tube protein (`gpFII`) during tail assembly.
- **NEW** `GO:0030430` (`host cell cytoplasm`, IDA, `PMID:12426340`): `gpE+E'` is synthesized and acts in the infected host cell cytoplasm and is not incorporated into the mature virion.
