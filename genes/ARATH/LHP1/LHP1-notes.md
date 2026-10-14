# LHP1 (Q946J8, At5g17690; TFL2) curation notes

## 2026-10-06 initial review

- Deep research: `just deep-research-falcon ARATH LHP1` failed (HTTP 402 from provider); review built from cached publications and UniProt.
- Domain architecture: N-terminal chromodomain (108-167) and C-terminal chromo shadow domain (378-442) [file:ARATH/LHP1/LHP1-uniprot.txt "Chromo 1"]. Single plant HP1 homolog.
- Core MF: H3K27me3 reader. [PMID:17542647 "in vivo TFL2/LHP1 associates almost exclusively and nearly co-extensively with H3K27me3"]; [PMID:17676062 "The LHP1 chromodomain also binds H3K27me3 with high affinity, suggesting that LHP1 has functions similar to those of Polycomb."]
- Complex: plant PRC1-like with RING1A/B [PMID:19097900 "We propose a model in which AtRING1a, AtRING1b, and LHP1 form a PRC1-like complex, which binds trimethyl-H3K27 marked by the CLF-containing PRC2"]; bridged to PRC2 via MSI1 [PMID:23778966 "We found that MSI1 serves to link PRC2 to LIKE HETEROCHROMATIN PROTEIN 1 (LHP1)"]. Added NEW part_of PRC1 complex (GO:0035102).
- Vernalization: required for maintenance (not establishment) of FLC silencing after cold [PMID:16682972 "is necessary to maintain the epigenetically repressed state of FLC upon return to warm conditions typical of spring"]; [PMID:16549797 "lhp1 mutants revealed a role for LHP1 in maintaining epigenetic silencing of FLC"].
- Localization: mostly euchromatic foci, not chromocenters, for a complementing fusion [PMID:16244868 "In A. thaliana interphase nuclei, LHP1 was predominantly located outside the heterochromatic chromocenters."]. Heterochromatin rows kept as non-core.

## Mis-attributed GOA rows (PMID:23203051)

The RIBA paper (full text cached) studies RIBA1 (At5g64300), RIBA2 (At2g22450), RIBA3 (At5g59750); it never mentions LHP1/TFL2 (At5g17690). GTP cyclohydrolase II activity (IDA), NOT DHBPS activity (IDA) and chloroplast (IDA) on LHP1 are gene-attribution errors -> REMOVE. These should be reported to TAIR.

## Other decisions

- Bare protein-binding rows: REMOVE per repo policy (no informative replacement), noting the interactions are not doubted. Self-interaction -> MODIFY to protein homodimerization activity [PMID:21304947 "We firstly confirmed that the LHP1 dimerization occurred in vivo in the plant nucleus"].
- Sequence-specific DNA binding (IDA PMID:27495811 and the derived IBA): motif enrichment in ChIP regions is not direct sequence-specific binding; LHP1 lacks a DNA-binding domain -> MARK_AS_OVER_ANNOTATED.
- DamID "DNA binding" -> MODIFY to chromatin binding.
- Module `vernalization_flc_silencing` lists LHP1 without MF; GO:0061628 (histone H3K27me3 reader activity) is now the core MF in this review.
