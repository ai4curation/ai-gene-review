# DAK1 (YML070W, P54838) notes

Module context: `glycerol_metabolism`, dihydroxyacetone_kinase_step (family PANTHER:PTHR28629, members DAK1/DAK2/S. pombe dak1/dak2), MF GO:0004371, BP GO:0019563, cytosol. DAK1 is not in the YeastPathways summary file (no YeastCyc rows, no RCA annotations). No S. cerevisiae GO-CAM; the S. pombe glycerol GO-CAM (6796b94c00004743) types the dak1/dak2 orthologs GO:0004371 in cytosol, consistent with this review.

## Evidence
- DAK family (fused DhaK/DhaL), EC 2.7.1.29; EC 2.7.1.28 by similarity only [UniProt]; "Catalyzes both the phosphorylation of dihydroxyacetone and of glyceraldehyde" is ECO:0000250.
- [PMID:12401799 "were characterized by a combined genetic and biochemical approach that firmly functionally classified their encoded proteins as dihydroxyacetone kinases (DAKs)"]; kinetics [PMID:12401799 "The kinetic properties of the two isoforms were similar, exhibiting K(m)((DHA)) of 22 and 5 microm and K(m)((ATP)) of 0.5 and 0.1 mm for Dak1p and Dak2p, respectively."].
- Redundancy with DAK2: [PMID:12401799 "The importance of DAK was clearly apparent for cells where both isogenes were deleted (dak1 Delta dak2 Delta), since this strain was highly sensitive to DHA."].
- Pathway placement: [PMID:22979944 "DHA was not detected in the gcy1 gene-disrupted strain but accumulated 225.91 μmol g DCW(-1) in a DHA kinase gene-deficient strain under micro-aerobic conditions."].

## Decisions
- Glycerone kinase rows ACCEPT (core). Triokinase IEA UNDECIDED (by similarity only). UniPathway "anaerobic glycerol catabolic process" -> MODIFY to GO:0019563 (S. cerevisiae does not ferment glycerol). ATP binding non-core.
- DAK1 cytoplasm HDA (Huh et al. 2003) accepted.
