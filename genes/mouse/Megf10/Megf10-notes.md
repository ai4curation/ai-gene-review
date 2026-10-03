# Megf10 (mouse) notes

Reviewed alongside human MEGF10 (`genes/human/MEGF10/`). The literature synthesis is in `genes/human/MEGF10/MEGF10-notes.md`. No provider deep research was run: Falcon returned 402 and the OpenAI key was invalid in this environment.

## Mouse-specific evidence

- Glial engulfment of apoptotic DRG neurons: [PMID:19915564 "Expression of Jedi-1 or MEGF10 in fibroblasts facilitated binding to dead neurons"]. Also [PMID:19915564 "knocking down either protein in glial cells or overexpressing truncated forms lacking the intracellular domain inhibited engulfment of apoptotic neurons"].
- Astrocyte clearance in the cerebellum: [PMID:27170117 "Megf10-deficient mice have increased apoptotic cells in the developing cerebellum and have impaired phagocytosis of apoptotic cells by astrocytes"].
- Satellite cells: [PMID:18056409 "Megf10 represents a novel transmembrane protein that impinges on Notch signaling to regulate the satellite cell population balance between proliferation and differentiation"].
- Synapse elimination by astrocytes: [PMID:24270812 "requires the MEGF10 and MERTK phagocytic pathways"].

## GO:1902742 apoptotic process involved in development (IMP, MGI, PMID:27170117): REMOVE

The phenotype is more TUNEL- and cleaved-caspase-3-positive cells in the P7 cerebellum. The full text was read at PMC4863057; the local cache has only the abstract. Its Figure 1 title is "Megf10 is necessary for apoptotic cell uptake by astrocytes, and its deficiency results in accumulation of apoptotic cells in the developing CB". The authors therefore read the excess apoptotic cells as uncleared corpses, not extra death. The annotation turns a clearance defect into participation in apoptosis. The human ISS row inherits this error. Both reviews mark it REMOVE, and the case is logged in `projects/SPKW/SPKW-APOPTOSIS.md`.
