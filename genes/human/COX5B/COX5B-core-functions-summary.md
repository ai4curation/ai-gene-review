# COX5B Core Functions Synthesis

## Summary

COX5B has been synthesized to have **one primary core function** based on the annotation review:

## Core Function

### Zinc-coordinating structural subunit enabling cytochrome c oxidase activity and assembly in mitochondrial respiratory chain Complex IV

**Molecular Function:** GO:0008270 (zinc ion binding)

**Directly Involved In:**
- GO:0006123 - mitochondrial electron transport, cytochrome c to oxygen
- GO:1902600 - proton transmembrane transport
- GO:0006119 - oxidative phosphorylation

**Locations:**
- GO:0005743 - mitochondrial inner membrane

**In Complex:**
- GO:0045277 - respiratory chain complex IV

## Rationale

This GO-CAM style description captures COX5B's essential molecular activity (zinc coordination) in the context of its structural role enabling Complex IV function. Key aspects:

1. **Zinc-coordinating**: COX5B's specific molecular function - coordinates Zn²⁺ via four conserved cysteines (positions 91, 93, 113, 116)

2. **Structural subunit enabling**: Acknowledges that while COX5B doesn't directly catalyze electron transfer (performed by COX1/2/3), it is absolutely required for:
   - Complex assembly
   - Complex stability
   - Optimal catalytic activity

3. **Assembly**: COX5B is incorporated early during Complex IV assembly and is required for progression to fully assembled holoenzyme. Knockdown causes accumulation of assembly intermediates.

4. **Contextual processes**: The biological processes (electron transport, proton pumping, oxidative phosphorylation) reflect the established role of Complex IV, to which COX5B is essential.

## Evidence Integration

The synthesis integrates:
- **Reviewed annotations**: All accepted annotations support this core function
- **Modified annotations**: Specific zinc ion binding (GO:0008270) was proposed to replace generic metal ion binding (GO:0046872)
- **Structural evidence**: PMID:30030519 - 3.3 Å cryo-EM structure showing COX5B as peripheral matrix-side subunit
- **UniProt annotation**: Documents Zn²⁺ binding sites and essential role in Complex IV
- **Functional studies**: Knockdown studies demonstrate loss of COX activity and impaired respiration

## Additional Functions Not Included in Core

While the gene description mentions "moonlighting" regulatory roles (PKA-R interaction regulating COX activity, MAVS interaction in antiviral signaling), these were not included as core functions because:

1. They represent context-specific regulatory activities rather than the fundamental molecular activity
2. They are secondary to COX5B's primary structural/assembly role in Complex IV
3. Insufficient evidence in the existing annotations to establish them as core (would require NEW annotations)

These regulatory interactions could be captured in future annotation expansions as they become better characterized.
