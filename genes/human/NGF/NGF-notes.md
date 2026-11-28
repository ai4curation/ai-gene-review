## 2026-11-28 NGF family review

Perplexity deep research was unavailable for this family, so this review used manual
triage of the fetched GOA rows, the human UniProt record, cached publications, Reactome
events, and the PTHR11589 PAINT node file.

NGF is the NGF-branch ligand in PTHR11589. The mature beta-NGF product is a secreted
homodimeric neurotrophin that binds NTRK1/TrkA and NGFR/p75NTR to drive neuronal survival,
differentiation and neurite responses. PMID:20978020 was useful as human evidence because
it assays HSAN5 NGF variants and states that wild-type NGF is processed, secreted and able
to activate TRKA-dependent PC12 differentiation.

The generic protein-binding IPI rows were retired under the project protein-binding policy:
they record receptor or interactome contacts as bare GO:0005515 rows rather than a more
informative ligand activity. The proNGF death-domain apoptosis row was kept as a real
secondary NGFR/SORT1 pathway, supported by PMID:14985763, but the mature NGF/NTRK1 growth
factor activity remains the core function. PMID:20164177 supports a real ADAM10/ADAM17
metalloendopeptidase-inhibitor activity for recombinant human NGF; it was kept as non-core.

PAINT places GO:0008021 at PTN001697725, the same deep mammalian neurotrophin node that
covers NGF, BDNF, NTF3 and NTF4. That location is too broad for the synaptic-vesicle row,
so the row is marked over-annotated and the family sidecar proposes moving the IBD to the
BDNF branch. The same node also carries the NGF-specific GO:0038180; the family sidecar
now proposes moving that term to the NGF subfamily branch because it over-propagates to the
non-NGF paralogs.
