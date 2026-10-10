# put1 (SPCC70.03c, UniProt O74524) notes

## Identity and naming
- PomBase symbol put1; UniProt has NO gene name for O74524 (only ORF SPCC70.03c; DR PomBase line shows "-"), so `just fetch-gene SCHPO put1` failed and the entry had to be fetched by accession.
- Probable proline dehydrogenase, mitochondrial (EC 1.5.5.2), ortholog of S. cerevisiae PUT1 (P09368). PANTHER PTHR13914:SF0. [UniProt:O74524 "RecName: Full=Probable proline dehydrogenase, mitochondrial;"]

## Evidence
- Only sequence-based: [UniProt:O74524 "Reaction=L-proline + a quinone = (S)-1-pyrroline-5-carboxylate + a"], FAD cofactor, predicted mitochondrial transit peptide (ECO:0000255).
- No S. pombe experimental data in GOA; no cached publications.
- PomBase GO-CAM 678073a900003902: put1 GO:0004657 in mitochondrial matrix, part of GO:0006562.

## Curation points
- Mitochondrial matrix ISS from PUT1: PRODHs are inner-membrane-associated (ubiquinone acceptor); keep as non-core, same as yeast PUT1 review. Core location: mitochondrion.
