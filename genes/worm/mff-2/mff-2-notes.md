# mff-2 (F55F8.6; UniProt P91344, unreviewed) review notes

## Deep research status
`just deep-research-falcon worm mff-2 --fallback perplexity-lite` failed on 2026-10-08 (falcon timeout; perplexity unavailable). No deep-research file was created. All GOA annotations are IEA. The review is based on cached publications PMID:24196833 and PMID:21248201 (both full text).

## Accession
P91344 is the F55F8.6 product. PMID:21248201 names "mff-1(F11C1.2) and mff-2(F55F8.6)", but its Methods also call the antibody "MFF-1 (F55F8.6)", so the paper is internally inconsistent. The F55F8.6 = mff-2 assignment follows UniProt/WormBase.

## Key findings
- Redundancy with mff-1 [PMID:24196833 "mff-1 and mff-2 single mutants have weak effects, and that the Mff double mutant has a mitochondrial fission defect similar to but not as strong as the drp-1 defect"]
- Peroxisome fission [PMID:24196833 "tubular peroxisomes in drp-1 mutant and Mff double mutants"]
- Not essential for DRP-1 recruitment in worms [PMID:24196833 "Mff and Fis1 are not essential for fission or for Drp1 recruitment to mitochondria in C. elegans."]
- Outer membrane, facing the cytosol [PMID:21248201 "We used antibodies against a C. elegans Mff homologue, encoded by the F55F8.6 gene, as a control for proteins exposed to the cytosol"]

## Curation decisions
- The IEA for positive regulation of protein targeting to membrane (Drp1 recruitment) is marked over-annotated, given the worm data.
- NEW: peroxisome fission (GO:0016559). In the comparator check, human MFF and DNM1L carry GO:0016559 (QuickGO).
- Core MF: GO:0060090 molecular adaptor activity, by family homology, matching the module. No direct worm MF evidence exists, which is why validation warns that the MF is not among the existing annotations.
