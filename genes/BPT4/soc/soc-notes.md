# Curation Notes: Bacteriophage T4 gene soc (UniProt P03715)

## Identity and Nomenclature
- **Gene symbol**: `soc`
- **Protein**: Small outer capsid protein Soc (80 aa processed / 81 aa precursor, ~9.1 kDa)
- **UniProt**: `P03715` (`SOC_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Outer capsid decoration protein ("molecular clamp")**:
   - Soc is a small, nonessential outer capsid decoration protein (~9.1 kDa, tadpole-like beta-sandwich fold with three-stranded and four-stranded beta-sheets plus a short alpha-helix) that binds to the outer surface of the T4 capsid only after gp21-mediated proteolytic maturation and expansion of the gp23* hexameric lattice (Ishii & Yanagida 1977, PubMed 327084; Qin et al. 2010, PubMed 20060836; Chen et al. 2017, PubMed 28893988).
   - In the mature wild-type prolate T4 capsid, ~810-870 copies of Soc bind at stoichiometric 1:1 ratio with gp23* monomers at hexamer-hexamer interfaces (excluding hexamer-gp24* pentamer and hexamer-portal interfaces); in the `T=13` isometric mutant capsid, 660 copies of Soc form an external cage of 200 trimers (Chen et al. 2017, PubMed 28893988).
   - Each Soc monomer bridges twogp23* subunits from adjacent hexameric capsomers, and three Soc monomers trimerize via C-terminal interactions at quasi-threefold axes to clamp three neighboring gp23* hexamers together. Occupancy is highest around the fivefold vertices where curvature and lattice strain between adjacent hexamer planes are greatest (Chen et al. 2017, PubMed 28893988).
2. **Capsid stabilization against environmental stress**:
   - Although `soc` deletion mutants are viable and package full-length DNA with normal infectivity under standard laboratory conditions, Soc reinforcement substantially increases capsid stability against alkaline pH (preventing disruption at pH 10.6), elevated temperatures, and osmotic shock (Ishii & Yanagida 1977, PubMed 327084; Qin et al. 2010, PubMed 20060836).
   - Because both its N- and C-termini are surface-exposed on the capsid exterior without perturbing virion assembly, Soc is widely used as a high-copy-number platform for T4 phage display of vaccine antigens and large proteins.

## Review of Existing GOA Annotations
- `GO:0098021` (`viral capsid, decoration`, IEA `GO_REF:0000120` and IMP `PMID:28893988`): **ACCEPT** (both rows). Directly supported by X-ray and 3.3 Å cryo-EM structures showing Soc forming the outer decoration cage clamping adjacent gp23* hexamers.
- `GO:0019028` (`viral capsid`, IEA `GO_REF:0000120`): **MODIFY** -> `GO:0098021` (`viral capsid, decoration`). `GO:0019028` is a broader parent term of `GO:0098021`, which is already present on the record.
- **New annotations (`NEW`)**:
  - `GO:0039660` (`structural constituent of virion`): Soc is a structural component of the mature T4 virion capsid (~810-870 copies per prolate head), acting as an inter-capsomer clamp that stabilizes the capsid lattice.
