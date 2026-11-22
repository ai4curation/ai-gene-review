# RIM9 manual notes

## 2026-11-22

`RIM9` encodes the N. glabratus member of the PalI/Rim9 PTHR28013:SF3 subfamily. The fetched UniProt record infers by homology that it is "Required for the proteolytic cleavage of the transcription factor RIM101 in response to alkaline ambient pH", and the same record places Q6FU42 in `PTHR28013:SF3`.

PubMed searches for `CAGL0F06545g`, `Q6FU42`, exact C. glabrata/N. glabratus `RIM9` or `PalI`, and broader C. glabrata Rim101/ambient-pH terms did not find a direct experimental N. glabratus RIM9 paper. The 2015 C. glabrata pH hit on Asg1p/Hal9p and the 2008 proteomic pH-response paper do not mention RIM9 by title or abstract. This review therefore treats the two CGD ND rows as still accurate and uses S. cerevisiae Rim9, C. albicans RIM9, Aspergillus PalI, and the PTHR28013 PAINT node as cross-fungal support only.

The `PANTHER:PTN001997378` TreeGrafter node in the current GOA rows does not appear in the local PAINT snapshot, whose only PTHR28013 IBD node is `PTN001997363`; the full pinned PANTHER 19 tree places `PTN001997378` on the S. cerevisiae RIM9 leaf and lacks N. glabratus as a leaf. Plasma-membrane localization is safe at the broader fungal node because it is seeded from S. cerevisiae Rim9/Tos7, S. pombe Mac1/Mug33, and A. nidulans PalI descendants. Cell-division-site and growing-cell-tip localization are over-specific for N. glabratus: the cell-division-site IBD is seeded only from Mug33 in `PTHR28013:SF6`, and S. cerevisiae Dcv1 is the closest budding-yeast SF3 member with direct imaging that argues against fission-yeast growing-tip transfer.

The EnsemblCompara ascospore-formation row is an over-transfer of a S. cerevisiae sporulation phenotype. The conserved Rim9 role is upstream ambient-pH signaling, while meiotic ascospore formation is a downstream yeast output inapplicable to a species with only observed haploid cells and no documented sexual cycle.
