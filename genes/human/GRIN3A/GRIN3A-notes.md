# GRIN3A notes

## Evidence synthesis

- `just fetch-gene human GRIN3A` created the review stub, GOA cache, UniProt cache, and newly cached abstracts for PMID:11880201, PMID:17320117 and PMID:17502428.
- No provider-named deep-research file was present for GRIN3A, so the review used the GOA and UniProt inputs, cached publications, and the GluN1/GluN3A GO-CAM source context directly.
- Human GluN3A has direct glycine-binding evidence: PMID:17320117 reports that "only glycine binds to human NR3A (hNR3A) with high affinity". The same abstract states that D-serine displaced radiolabeled glycine, matching the retained glycine-binding and serine-binding molecular functions.
- Human GluN1/GluN3A has direct structural and functional support from PMID:38598639: "Uniquely, NMDARs composed of GluN1 and GluN3 are activated exclusively by glycine" and "The structures show a 1-3-1-3 subunit heterotetrameric arrangement". Those observations support `GO:0160212 glycine-gated cation channel activity` and the broader neurotransmitter receptor complex row.
- The older PMID:17502428 HEK293 study directly supports excitatory glycine-gated NR1/NR3A/NR3B receptors and explicitly says they were not stimulated by glutamate or kainic acid, so the direct `GO:0004972 NMDA glutamate receptor activity` row was marked over-annotated rather than accepted as a canonical glutamate-gated NMDAR activity.
- GluN3A can also enter NR1/NR2A or NR1/NR2B assemblies in adult human CNS. PMID:17997397 found that "NR3A is associated with NR1, NR2A and NR2B in adult human CNS". That keeps the NMDA-family complex row, but does not make glutamate binding a GluN3A molecular function.
- PMID:17658481 supports the MAP1S interaction and broad neuronal locations, but the GO term `GO:0005515 protein binding` is uninformative. The review removes the bare protein-binding row and keeps neuron-projection, neuronal-cell-body and synapse locations as non-core context.
- Two direct ethanol rows cite pharmacological studies in recombinant receptors, PMID:17502428 and PMID:18445116. Both were marked over-annotated because the experiments measure channel modulation by ethanol rather than a GRIN3A activity in a cellular ethanol-response pathway.

## GO-CAM consistency

- `66c7d41500001953` correctly models GRIN3A as enabling `GO:0160212 glycine-gated cation channel activity`; that term is the first GRIN3A core function.
- The GRIN3A model's complex-level activity still uses the broader transmitter-gated channel term while the subunit activities use the better glycine-gated term. The complex activity should be checked in the final GO-CAM consistency PR, not in this gene PR.
- The GRIN3A model represents calcium as input and output of the complex-level glycine-gated receptor. This review keeps GluN1/GluN3A as a cation channel with low calcium permeability and marks calcium-channel annotations over-annotated, so the final notes PR should ask curators to check whether calcium transport belongs in the GluN1/GluN3A model.
- The GRIN3A model makes glycine a positive activator of the GRIN1 subunit activity. PMID:26777280 and the GRIN1 review both indicate that glycine at GluN3 opens the channel while glycine at GluN1 auto-inhibits GluN1/GluN3 receptors, so the causal sign on the GRIN1 branch remains questionable.
