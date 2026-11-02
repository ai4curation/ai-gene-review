# Bacteriophage T4 Gene 18 (gp18) — Curation Notes

## Summary of Gene Function
Bacteriophage T4 gene `18` encodes the contractile tail sheath protein gp18 (UniProt `P13332`, 659 amino acids, ~71.3 kDa). It is the sole structural subunit of the outer contractile sheath that surrounds the rigid inner tail tube (composed of gp19) in the T4 virion tail.

## Structural Organization and Assembly
- **Stoichiometry and Architecture**: A total of 138 copies of gp18 assemble into 23 stacked hexameric rings arranged in a six-start right-handed helix around the 24-ring gp19 tail tube (PubMed 19229296).
- **Domain Architecture**: X-ray crystallography and cryo-EM reconstructions show that gp18 comprises four domains (Domains I–IV) formed through an insertion hierarchy: Domain I is inserted into Domain II, which is inserted into Domain III, while the C-terminal Domain IV binds directly to the inner gp19 tail tube in the extended state and mediates inter-ring contacts (PubMed 19229296).
- **Morphogenesis**: During late infection, gp18 polymerizes exclusively onto the completed baseplate–tail tube complex (nucleated at the baseplate wedge/junction proteins including gp48, gp53, and gp54) and is capped at the distal neck/collar interface by the tail completion protein gp15. Monomeric gp18 does not self-assemble into functional sheaths in the absence of the baseplate-tube template, though extended-time incubation can yield aberrant polysheaths.

## Mechanism of Contraction and Infection
- **Rigid-Body Rearrangement**: Upon host receptor recognition by the tail fibers and conformational switching of the baseplate from a hexagonal dome to a six-pointed star, contraction propagates through the gp18 sheath. During contraction, the sheath shortens from ~925 Å to ~420 Å and widens from ~240 Å to ~330 Å as gp18 subunits slide and rotate as rigid bodies without refolding their individual domain structures (PubMed 19229296).
- **Host Envelope Penetration**: Because the distal end of the sheath is anchored to the neck/capsid via gp15 and the distal gp19 ring while the proximal end is linked to the expanding baseplate, sheath contraction drives the non-contractile gp19 tail tube and its tip spike complex (gp5–gp27–gp5.4) mechanically through the *Escherichia coli* outer membrane into the periplasm, creating the conduit for viral genomic DNA ejection into the host cytoplasm.

## Annotation Review Notes
- `GO:0098027` (`virus tail, sheath`, IDA from PubMed 19229296 and IEA from `GO_REF:0000043`): Directly supported by crystallographic and cryo-EM determination of the T4 sheath composed of 138 gp18 subunits (`ACCEPT`).
- `GO:0098015` (`virus tail`, IEA from `GO_REF:0000043`): True but overly general relative to `GO:0098027` (`virus tail, sheath`), which is already present on this gene (`MODIFY` -> `GO:0098027`).
- `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA from `GO_REF:0000043`): Accurately captures the core biological process driven by gp18 sheath contraction (`ACCEPT`).
- `GO:0046718` (`symbiont entry into host cell`, IEA from `GO_REF:0000043`): Broad parent term superseded by the specific contractile tail genome ejection term `GO:0099000` (`MODIFY` -> `GO:0099000`).
