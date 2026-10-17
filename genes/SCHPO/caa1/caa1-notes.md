# caa1 (SPAC10F6.13c, UniProt O42652) notes

Cytosolic aspartate aminotransferase (AspAT, EC 2.6.1.1).

- Reaction: [UniProt:O42652 "Reaction=L-aspartate + 2-oxoglutarate = oxaloacetate + L-glutamate;"] (by similarity to S. cerevisiae Aat2, P23542). PLP cofactor, homodimer (by similarity).
- Location: [UniProt:O42652 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16823372}."]; HDA cytosol from the ORFeome GFP screen [PMID:16823372 "we determined the localization of 4,431 proteins"].
- S. pombe genetics (Kitamura 2024, micropublication on maa1/glu1): [PMID:39502420 "The cytoplasmic Caa1 has a major role for this reaction in"] (i.e. aspartate synthesis in S. pombe). Multicopy caa1+ does NOT rescue the maa1/glu1 glutamate requirement on ammonium.
- PANTHER PTHR11879:SF55 (fungal cytosolic AspAT subfamily), same as S. cerevisiae AAT2.
- Budding-yeast ortholog AAT2: [PMID:9288922 "We demonstrate that the gene AAT2 codes for the cytosolic and peroxisomal AAT activities."]; [PMID:33397945 "suggesting that Aat2p is the major enzyme for aspartate synthesis under nitrogen starvation"]. Consistent with caa1 being the major aspartate-forming isozyme.

## GO-CAM
- gomodel:67c10cc400005826 has two caa1 activities (…/67c10cc400005832 and …/684b6c8100000690), both GO:0004069 in cytosol and **part_of GO:0043490 malate-aspartate shuttle**, not GO:0006532. The aspartate_asparagine_metabolism module describes …/684b6c8100000690 as "aspartate biosynthetic process (GO:0006532)" with inputs/outputs; in the model it is part_of the shuttle (has_input/has_output molecule associations present). The GOA IC row is malate-aspartate shuttle.

## Decisions
- Core: GO:0004069 / GO:0006532 / cytosol, same as S. cerevisiae AAT2 review.
- Malate-aspartate shuttle (IC, ARBA) kept as non-core: canonical by analogy, no S. pombe test.
- ISS donor P00508 is chicken *mitochondrial* AspAT; MF transfer fine, BP rows (2-oxoglutarate/glutamate/aspartate metabolic process) are generic -> non-core.
