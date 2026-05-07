# fusB (EF-G 2) - Streptomyces coelicolor - Review Notes

## Gene Identity
- UniProt: O87844 (EFG2_STRCO)
- Gene: fusB / SCO6589
- Product: Elongation factor G 2 (EF-G 2)
- 686 AA, GTPase superfamily member
- PANTHER family: PTHR43261 (Elongation Factors and Tetracycline Resistance)
- PANTHER subfamily: PTHR43261:SF1 (Ribosome-releasing factor 2, mitochondrial)

## Key Biological Context

fusB is one of two EF-G paralogs in S. coelicolor. In bacteria that have undergone EF-G gene duplication, the two paralogs typically partition the two canonical functions of EF-G:
- **EF-G1** (fusA): canonical translational elongation (mRNA-tRNA translocation)
- **EF-G2** (fusB): ribosome recycling / disassembly

### Evidence from EF-G2 paralogs in other organisms

1. **Borrelia burgdorferi** [PMID:20132446 "EF-G1 is a translocase, while EF-G2 is an exclusive recycling factor"]: Two EF-G paralogs divide labor - EF-G1 for translocation, EF-G2 exclusively for ribosome recycling. EF-G2 does not require GTP hydrolysis for ribosome disassembly when IF-3 is present.

2. **Bacteroides thetaiotaomicron** [PMID:36472247 "EF-G2's singular ability to sustain protein synthesis, albeit at slow rates, is crucial for bacterial gut colonization"]: EF-G2 supports translocation WITHOUT GTP hydrolysis. Accumulates during carbon starvation. Contains a unique 26-residue region responsible for absence of GTPase activity.

3. **Mycobacterium smegmatis** [PMID:40569974 "mycobacterial EF-G2 acts as a translation repressor during nutrient starvation"]: EF-G2 lacks ribosome-dependent GTPase activity. Two copies of EF-G2 can bind the 50S subunit, preventing 70S formation. Acts as anti-associator during starvation.

4. **Human mitochondria** (GFM2/EF-G2, Q969S9): Mitochondrial ribosome-releasing factor that mediates ribosome disassembly during translation termination. Works with MRRF.

### IBA annotation basis
The IBA for GO:0032790 (ribosome disassembly) is based on PANTHER:PTN000754007 and human GFM2 (Q969S9). This is phylogenetically well-supported - the PANTHER subfamily SF1 specifically corresponds to ribosome-releasing factors.

## Annotation Assessment Summary

The key insight is that EF-G2 paralogs have functionally diverged from canonical EF-G1. The IEA annotations for "translation elongation factor activity" and "translational elongation" are based on domain-level matches to the broader EF-G family but may not accurately reflect EF-G2's specialized function. The IBA annotation for ribosome disassembly is likely the most accurate functional annotation.

Similarly, GTPase activity is questionable for EF-G2 - multiple studies show EF-G2 paralogs lack ribosome-dependent GTPase activity, though they retain GTP binding capability.

## UniProt Function Note
UniProt describes fusB with "By similarity" annotation: "Catalyzes the GTP-dependent ribosomal translocation step during translation elongation." This similarity-based annotation likely derives from the broader EF-G family rather than EF-G2-specific characterization.
