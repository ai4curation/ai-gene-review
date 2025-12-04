# MxaC Research Notes

## Gene Context
MxaC is part of the mxa operon in Methylorubrum extorquens AM1 (formerly Methylobacterium extorquens AM1), which encodes the calcium-dependent methanol dehydrogenase system.

## Protein Structure
- 355 amino acids, 37.5 kDa
- Contains von Willebrand factor A (vWFA) domain (residues 86-259) [UniProt:C5AQA2]
- Two predicted transmembrane helices (residues 51-72 and 307-325) [UniProt:C5AQA2]
- Member of COG2304 family
- vWFA domains typically mediate protein-protein interactions and metal coordination

## Genetic Organization
The mxa operon contains genes involved in methanol oxidation: mxaFIRSACKLDGJ
- mxaF and mxaI encode the large and small subunits of methanol dehydrogenase
- mxaC is located between mxaA and mxaK
- Identified by Morris et al. (1995) through sequencing of a 4.4-kb region [PMID:7592474 "DNA sequence for a 4.4-kb HindIII-XhoI Methylobacterium extorquens AM1 DNA fragment that is known to contain three genes (mxaAKL) involved in incorporation of calcium into methanol dehydrogenase"]

## Function

### Essential for Methanol Oxidation
[PMID:7592474 "mutant complementation studies showed that mxaC is required for methanol oxidation"]

### Role in Ca²⁺ Incorporation
The auxiliary proteins MxaS, MxaC, and MxaL contain VWA domains and, along with MxaR (a MoxR-class AAA+ ATPase), likely assemble into a MoxR/VWA complex. This is an evolutionarily conserved prokaryotic machinery that specializes in metal cofactor insertion and presumably facilitates Ca²⁺ transport and incorporation into the methanol dehydrogenase complex [Nature Communications 2025, recent work on PQQ-dependent methanol dehydrogenase assembly].

### Membrane Localization
With two transmembrane helices, MxaC is predicted to be membrane-associated, which could facilitate:
- Anchoring the assembly machinery to the membrane
- Coordinating with the periplasmic methanol dehydrogenase complex
- Facilitating Ca²⁺ transport across the membrane

## Molecular Function

The vWFA domain in MxaC suggests several possible functions:

1. **Metal coordination**: vWFA domains often contain a metal ion-dependent adhesion site (MIDAS) motif that coordinates divalent cations. MxaC's vWFA domain may directly bind Ca²⁺ during the incorporation process.

2. **Protein-protein interactions**: vWFA domains mediate interactions with other proteins. MxaC likely interacts with:
   - Other assembly factors (MxaS, MxaL, MxaR)
   - The methanol dehydrogenase complex (MxaFI)
   - Potentially calcium transport proteins

3. **Assembly scaffold**: As a membrane protein with a protein interaction domain, MxaC may serve as a scaffold that organizes the assembly machinery at the membrane-periplasm interface.

## Related Systems

The calcium-dependent MxaFI system is regulated by a complex hierarchy and competes with the lanthanide-dependent XoxF system for methanol oxidation [see mxaF-deep-research.md]. MxaC is specific to the Ca-dependent system and not involved in XoxF maturation.

## Outstanding Questions

1. Does MxaC directly bind Ca²⁺ through its vWFA domain?
2. What is the precise role of the transmembrane helices - membrane anchoring or Ca²⁺ transport?
3. How does MxaC interact with other MoxR/VWA complex members (MxaS, MxaL, MxaR)?
4. Is MxaC required for initial assembly, ongoing function, or both?
5. What is the stoichiometry of the MoxR/VWA complex?

## GO Term Considerations

Based on this analysis, appropriate GO terms for MxaC would be:

**Molecular Function:**
- Metal ion binding (GO:0046872) - specifically calcium ion binding (GO:0005509) if experimental evidence confirms
- Protein binding (GO:0005515) - via vWFA domain
- More specifically: metalloenzyme regulator activity or similar term for assembly factors

**Biological Process:**
- Protein complex assembly (GO:0006461)
- Metal ion transport (GO:0030001) - possibly, if transport role confirmed
- Methanol metabolic process (GO:0006118)
- More specifically: would benefit from a term like "methanol dehydrogenase complex assembly" or "metal incorporation into metalloenzyme"

**Cellular Component:**
- Membrane (GO:0016020) - confirmed by transmembrane helices
- Integral component of membrane (GO:0016021)
- Potentially: methanol dehydrogenase complex (if close association is confirmed)

## References

- PMID:7592474 - Morris et al. (1995) - Initial identification and characterization
- Nature Communications 2025 - Recent structural work on MDH assembly
- UniProt:C5AQA2 - Protein sequence and domain annotations
