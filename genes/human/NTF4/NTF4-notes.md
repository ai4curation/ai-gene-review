## 2026-11-28 NGF family review

Perplexity deep research was unavailable for this family, so this review used manual
triage of the fetched GOA rows, the human UniProt record, cached publications, Reactome
events, and the PTHR11589 PAINT node file.

NTF4 encodes neurotrophin-4/5, a secreted human neurotrophin that activates Trk-family
receptors and is biased toward NTRK2/TrkB signaling. PMID:1742028 provides the main
direct experimental support, reporting that recombinant NT-5 promotes peripheral sensory
and sympathetic neuron survival, induces PC12 differentiation and activates Trk-related
receptor tyrosine kinases.

The mouse ISS and IEA rows describe a mixture of plausible secondary tissue phenotypes and
over-specific organism-level outcomes. Long-term memory is retained as non-core from
PMID:10869436, and ameloblast differentiation is retained as non-core because the human
UniProt record records the mouse-derived role by similarity. Adult locomotory behavior,
ganglion mother cell fate determination and sensory organ boundary specification are
marked over-annotated rather than treated as direct processes executed by the secreted
NTF4 ligand.

The family PAINT node for GO:0008021 synaptic vesicle is too specific for neurotrophin
secretory cargo, and the GO:0038180 nerve growth factor signaling pathway IBA is specific
to NGF. Both are handled consistently with BDNF and NTF3 through the PTHR11589 sidecar.
