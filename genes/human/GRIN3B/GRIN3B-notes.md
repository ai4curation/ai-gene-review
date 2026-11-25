# GRIN3B notes

## Evidence synthesis

- `just fetch-gene human GRIN3B` created the review stub, GOA cache, UniProt cache, and a newly cached abstract for PMID:11735224.
- `just paint-losses human GRIN3B` initially raced with the GRIN3A run on a shared `.cache/paint/.../IBD.gaf.part` path and was rerun serially; the serial rerun reported no IRD or IKR losses on the human GRIN3B lineage.
- No provider-named deep-research file was present for GRIN3B, so the review used the GOA and UniProt inputs, cached publications, and the GluN1/GluN3B GO-CAM source context directly.
- Human GRIN3B itself is much less directly characterized than GRIN3A. PMID:11735224 identified the human gene and its mouse ortholog, reporting that "GRIN3B localizes to chromosome 19p13.3 and contains, as does the mouse NR3B gene".
- The glycine-gated channel function is kept by orthology. PMID:11823786 established that "NR3A or NR3B co-assembles with NR1 to form excitatory glycine receptors that are unaffected by glutamate or NMDA", and UniProt now summarizes GluN3B as forming excitatory glycinergic receptor complexes with GluN1.
- The only direct paper in GOA for the SynGO `GO:0099507 ligand-gated monoatomic ion channel activity involved in regulation of presynaptic membrane potential` rows is PMID:22564863. Its full text records recombinant GluN1/GluN2A/GluN3A or GluN1/GluN2A/GluN3B currents in Xenopus oocytes, not a presynaptic preparation. Those rows were marked over-annotated and structured source defects were recorded against SynGO asking that the presynaptic context be checked.
- Calcium-specific GRIN3B rows were marked over-annotated. GluN3B-containing receptors are cation channels and PMID:22564863 supports altered blocker sensitivity, but GluN3 subunits reduce calcium permeability; the retained process row is therefore `GO:0051924 regulation of calcium ion transport`, not calcium-channel activity or calcium ion transmembrane transport.

## GO-CAM consistency

- `66c7d41500003371` correctly models GRIN3B as enabling `GO:0160212 glycine-gated cation channel activity`; this review keeps the same function as core, based on rodent NR3B/GluN3B evidence.
- The GRIN3B model places the GRIN3B activity and complex activity in the presynaptic membrane while the GRIN1 activity in the same tetramer is in the postsynaptic membrane. This review keeps presynaptic membrane only as a non-core transferred location, so the final GO-CAM consistency PR should flag the internally inconsistent location.
- The GRIN3B model has the same complex-level transmitter-gated term, calcium input/output and GRIN1 glycine-activation concerns as the GRIN3A model. All of those are GO-CAM-level issues for the final notes PR.
