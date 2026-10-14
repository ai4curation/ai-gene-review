# ATAD3C notes

## 2026-10-05 review (PAINT, affinage)

- Expressed protein, not a pseudogene [PMID:38092275 "We detected unique ATAD3C peptides in HEK 293T cells, with expression similar to that in human tissues, and showed that it is an integral membrane protein that exposes its carboxy-terminus to the intermembrane space."]. This source is abstract-only.
- Dominant negative on ATAD3A [PMID:38092275 "This was due to the incorporation of ATAD3C monomers in ATAD3A complex in the mitochondrial membrane reducing its size."].
- Residue check (`ATAD3C-bioinformatics/`): Walker A K183 and Walker B D236/E237 are intact, but the ATAD3A arginine finger R466 aligns to ATAD3C C291 (window checked; ATAD3B control keeps R). This matches the fusion paper [PMID:32004445 "(C) The ATAD3A arginine finger, Arg466 (yellow) which is changed to a cysteine in the ATAD3A-C fusion gene, is overlaid with the SPAST arginine finger (Arg499; orange)."].
- Row calls: ATP hydrolysis (IEA) is marked over-annotated; ATP binding is accepted; mitochondrion organization (IBA) is non-core. I added NEW mitochondrial inner membrane (IDA); ATAD3A carries it by IDA/EXP.
- Not used: the uncached locus-rearrangement papers PMID:33575671 and PMID:28549128.

## 2026-10-05 revision (reviewer round 1)

- ATP hydrolysis over-annotation restated to separate cis from trans. ATAD3C keeps its own Walker residues, so an adjacent ATAD3A could complete ATAD3C's site, but ATAD3C (C291) cannot complete its neighbour's. Added the SPAST quote [PMID:32004445 "These variants have been shown to result in the complete loss of SPAST ATPase activity,19 leading to disease through a dominant-negative mechanism."].
- ATP binding stays accepted (intact Walker motifs). The knowledge gap now asks about turnover at ATAD3C's own site, not binding.
- NEW location changed from inner membrane to the parent GO:0031966 mitochondrial membrane: the abstract says "in the mitochondrial membrane" and does not name the inner membrane.
- No MF is asserted. Candidates such as ATPase inhibitor activity (GO:0042030) would need a measurement of ATAD3A ATPase activity in the presence of ATAD3C; the abstract reports effects on complex size, respiration and supercomplexes only.
- Cross-check of the residue mapping against the fusion junction: ATAD3A 1-405 + ATAD3C 231-411 gives an offset of 175, so ATAD3A R466 corresponds to ATAD3C 291. This matches the C291 found by alignment.
