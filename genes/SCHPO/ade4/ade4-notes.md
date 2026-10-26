# ade4 (SPAC4D7.08c, UniProt P41390) notes

Fetch: `just fetch-gene SCHPO ade4` fetched the correct accession (PUR1_SCHPO, P41390, 533 aa).

## Evidence
- [PMID:8082193 "which encodes the glutamine phosphoribosylpyrophosphate amidotransferase, the first enzyme of the purine nucleotide de-novo biosynthetic pathway"].
- Regulation differs from budding yeast: [PMID:8082193 "In contrast to the situation in S. cerevisiae, adenine does not repress ade4 expression at the mRNA level"].
- Enzyme activity / kinetics in S. pombe extracts: PMID:4371850 (title-only cache: "Variations in the stability and kinetic parameters of amidophosphoribosyltransferase depending on growth phase and growth conditions").
- Cytoplasm (ORFeome, PMID:16823372).

## Decisions
- Core MF GO:0004044, BP GO:0006189, location cytoplasm (S. pombe evidence and PomBase GO-CAM use cytoplasm; S. cerevisiae ADE4 review uses cytosol - equivalent intent).
- Nucleobase (GO:0009113) and adenine metabolic process (GO:0046083) rows MODIFIED to GO:0006189, consistent with genes/yeast/ADE4 and ADE8 handling.
