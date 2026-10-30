# sufB (A2RMK5, llmg_1969) bioinformatics results

## Query identity

The KBase Dark Protein Atlas protein NZ_LKLC01000161.1_58 (Lactococcus lactis,
470 aa) is 100% identical over its full length to UniProtKB A2RMK5 (llmg_1969,
L. lactis subsp. cremoris MG1363), which is reviewed here.

## Essential E. coli SufB residues are conserved

`map_ecoli_residues.py` aligns A2RMK5 with E. coli SufB (P77522; global, BLOSUM62).
Output (`alignment_output.txt`):

- aligned columns: 466; identity: 39.9%
- E. coli C254 -> query C236 (E.coli SYIEGCSAPVR / query QYVEGCTAPTY)
- E. coli C405 -> query C380 (E.coli RNFTQCDSMLI / query ASHIECDTILM)
- E. coli E434 -> query E409 (E.coli AQLEHEATTSR / query VALEHEAKVSK)

C254 is the E. coli SufB sulfur-acceptor cysteine, and C405/E434 form part of the
de novo cluster site at the SufB-SufD interface (PMID:28839209). All three are
conserved in the L. lactis protein, consistent with a functional SufB scaffold
subunit rather than a degenerate paralog.

## Operon context (KEGG, MG1363)

`fetch_neighborhood.sh` (`neighborhood_output.txt`), all on the minus strand:

| locus | KEGG KO | assignment |
|---|---|---|
| llmg_1974 | K09013 | Fe-S cluster assembly ATP-binding protein (SufC) |
| llmg_1973 | K09015 | Fe-S cluster assembly protein SufD |
| llmg_1972 | K11717 | cysteine desulfurase (SufS) |
| llmg_1971 | none | unknown protein |
| llmg_1970 | K04488 | NifU-related (SufU) |
| llmg_1969 | K09014 | Fe-S cluster assembly protein SufB (query) |

This is the Firmicute-type sufCDSUB operon, with SufU (not SufE) as the sulfur
transfer partner of SufS.
