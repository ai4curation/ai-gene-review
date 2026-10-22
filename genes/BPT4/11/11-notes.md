# Gene 11 (Baseplate wedge protein gp11) - Research Notes

## Overview
- **Gene symbol**: `11` (gp11)
- **UniProt ID**: `P10929`
- **Organism**: Bacteriophage T4 (`NCBITaxon:10665`, Tequatrovirus T4)
- **Length**: 219 amino acids (~23.7 kDa monomer)

## Biological Function & Architecture
- **Peripheral Baseplate Clamp / Adaptor**: gp11 is a structural protein of the outer baseplate periphery, present in 18 copies per virion (six homotrimers located at the six peripheral vertices of the baseplate). Each monomer comprises three domains: an N-terminal alpha-helical domain that forms a central coiled-coil trimerization core, a middle "finger" domain (with a seven-stranded antiparallel beta-roll and an alpha-helix) that varies slightly in orientation among protomers, and a C-terminal trimerization domain stabilized by swapped beta-strands (PubMed 10984513; PubMed 27193680).
- **Bridge Between gp10 and gp12 Short Tail Fibers**: Unlike the core wedge proteins (`gp10`, `gp7`, `gp8`, `gp6`, `gp53`, `gp25`), gp11 can attach either to the gp10 pin during wedge assembly or onto nearly complete `11-` tail/baseplate particles in vitro to restore infectivity. In the virion, the gp11 homotrimer binds specifically to domain III of the gp10 homotrimer and clamps onto the central shaft/hinge region of the gp12 short tail fiber (STF) trimer, stabilizing the stowed garland of STFs beneath the dome-shaped baseplate (PubMed 15315755; PubMed 27193680).
- **Role in Conformational Switching and Irreversible Attachment**: During infection, rotation of the gp10-gp11 unit (~100° rotation of gp10 and coupled reorientation of gp11) releases the C-terminal receptor-binding heads of the neighboring gp12 short tail fibers and points them downward toward the Escherichia coli lipopolysaccharide (LPS) core, coupling long tail fiber host sensing to irreversible adsorption and sheath contraction.

## Annotation Assessment Notes
- `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680 and IEA from `GO_REF:0000043`): Core cellular component (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): True but overly general relative to `GO:0098025` (`virus tail, baseplate`) (`MODIFY`).
- `GO:0098003` (`viral tail assembly`, IEA from `GO_REF:0000043`): Core biological process (`ACCEPT`), as gp11 is required to assemble the functionalgp10-gp11-gp12 peripheral baseplate/short tail fiber complex.
