# ced-1 notes

Provider deep research was not run: Falcon returned 402 and the OpenAI key was invalid in this environment (see `genes/human/MEGF10/MEGF10-notes.md`). This synthesis was made by hand from cached publications.

## Core
- Receptor: [PMID:11163239 "CED-1 is a cell surface phagocytic receptor that recognizes cell corpses"]. It acts in engulfing cells: [PMID:11163239 "ced-1 is expressed in and functions in engulfing cells"].
- Ligand bridge: [PMID:20526330 "binds to both PtdSer and the extracellular domain of CED-1 in vitro"]. The binding site is the EMI domain: [PMID:22713871 "CED-1 binds TTR-52 through its N-terminal EMI domain"].
- Adaptor: [PMID:11729193 "we present evidence for a physical interaction between GULP/CED-6 and one of the two motifs (NPXY motif) in the cytoplasmic tail of CED-1"].
- Phagosome maturation: [PMID:18351800 "One of the pathways, composed of CED-1, the adaptor protein CED-6, and DYN-1, controls the rate of enrichment of PI(3)P and RAB-7 on phagosomal surfaces and the formation of phagolysosomes"].
- Recycling: [PMID:35929733 "CED-1 is recycled from phagosome membranes to plasma membranes via the retromer complex"].

## Killing role (worm-specific, regulatory)
- [PMID:11449278 "the expression in engulfing cells of ced-1, which encodes a receptor that recognizes cell corpses, rescues the cell-killing defects of ced-1 mutants"]
- [PMID:11449279 "genes that mediate corpse removal can also function to actively kill cells"]
- CED-1 therefore promotes death, which fits *positive regulation* of apoptotic process. It does not take part in the dying cell's own program.

## Background-genotype annotations (see projects/APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.md)
- PMID:24225442 (CED-8) and PMID:23505386 (CSP-1) use ced-1(e1735) only as a background that makes corpses persist so they can be counted: [PMID:24225442 "ced-1(e1735) blocks cell corpse engulfment and sensitizes"]. Also [PMID:23505386 "the extra cell corpses in ced-1 mutant larvae likely reflected an engulfment defect"]. The ced-1 apoptosis annotations taken from these papers attribute the background genotype's role to the gene being studied.

## Wnt paper (PMID:20126385)
- DTC migration: [PMID:20126385 "we found that the CED-1/6/7 pathway appears to play at most a minor role, if any, in this process"].
- Spindle: [PMID:20126385 "we did observe spindle defects in a small fraction of ced-1; ced-5 double mutants"].
