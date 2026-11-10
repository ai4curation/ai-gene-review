# Manual deep research: NEUCR mak-2

`mak-2` / `NCU02393` encodes a 352 aa PTHR24055 MAP kinase with the canonical
MAPK TEY activation motif and the conserved protein kinase ATP-binding,
Ser/Thr kinase active-site, protein kinase domain, and MAPK signatures in
UniProt. It is the terminal MAPK in the Neurospora crassa NRC-1/MEK-2/MAK-2
module.

The foundational Neurospora study is PMID:15075265. The paper disrupted
`mak-2`, observed pleiotropic defects including loss of vegetative hyphal
fusion, female sterility, and autonomous ascospore lethality, and showed that
MAK-2 phosphorylation peaks during germ-tube elongation, branching, and
germling fusion. The upstream MAPKKK `nrc-1` was required for MAK-2
phosphorylation, placing the two proteins in a shared MAPK cascade.

The strongest live-cell evidence is PMID:19884508. Functional MAK-2-GFP was
cytoplasmic/nuclear when germlings were isolated, then alternated with SO at
cortical complexes in interacting fusion partners. An analog-sensitive MAK-2
variant established that the kinase activity is required for chemotropic
interactions and for coordinated MAK-2/SO oscillation.

PMID:23028357 and PMID:25412208 clarify that MAK-2 acts as a scaffolded module
with NRC-1 and MEK-2. HYM1 is critical for organizing the MAK-2 pathway, and
HAM-5 functions as a MAPK scaffold required for MEK-2/MAK-2 puncta and
oscillation during germling and hyphal fusion.

Recent papers did not change the GOA decisions. PMID:34899653 and
PMID:39283084 connect MAK-2/PR-MAPK signaling to protoperithecium and sexual
development, and PMID:41915693 places MAK-2 upstream of the 2026 EOP-1/SO
pre-fusion oscillator. None supplies evidence that Neurospora MAK-2 executes a
literal pheromone-response GPCR cascade, so the PANTHER Fus3/Spk1-clade IBA
to `GO:0071507 pheromone response MAPK cascade` is better modified to the
ancestor `GO:0000165 MAPK cascade`.
