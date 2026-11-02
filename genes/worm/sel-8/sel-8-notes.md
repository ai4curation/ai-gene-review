# sel-8 / lag-3 (C. elegans) review notes

- UniProt: Q09260 (LAG3_CAEEL), "Protein lag-3"; gene name sel-8, synonym lag-3; ORF C32A3.1; 490 aa, glutamine-rich.
- PANTHER: none listed in the UniProt record (no DR PANTHER line). InterPro IPR021587 / Pfam PF11498 (Activator_LAG-3). Mastermind-family relationship is functional/structural (N-terminal helix binding the CSL-ANK groove) rather than detectable by a shared PANTHER family.
- No IBA annotations in GOA.

## Key findings
- Two groups found it independently: SEL-8 (Greenwald; lin-12(gf) suppressor) and LAG-3 (Kimble; two-hybrid with LAG-1/GLP-1 ICD).
- [PMID:10830967 "Here we identify LAG-3, a glutamine-rich protein that forms a ternary complex together with the LAG-1 DNA-binding protein and the receptor's intracellular domain."]
- [PMID:10830967 "LAG-3 is a potent transcriptional activator in yeast, and a Myc-tagged LAG-3 is predominantly nuclear in C. elegans."]
- [PMID:10884418 "In all cells where fluorescence is visible, SEL-8∷GFP is nuclear."]
- Worm ternary complex crystal structure includes LAG-3 [PMID:16530045]; RAM-induced allostery creates Mastermind docking site [PMID:18381292].
- ChIP with LAG-3 antibodies / SEL-8::GFP shows occupancy of LAG-1 binding site regions in lag-1 gene [PMID:23615264 "the regions containing LAG-1 binding sites (regions 1, 3, and 4), but not the region lacking the LAG-1 binding sites (region 2), are enriched in the LAG-3- and GFP-specific precipitates"]. Not currently annotated (chromatin) for sel-8.
- Required in M lineage patterning [PMID:18036582].
- Contributes to CEP-1/p53-dependent germ cell apoptosis after DNA damage [PMID:17317671 "RNA interference-mediated knockdown of the single Caenorhabditis elegans MAML homolog, Lag-3, led to substantial abrogation of p53-mediated germ-cell apoptotic response to DNA damage"].

## Review decisions (summary)
- Core MF: GO:0003713 transcription coactivator activity; BP GO:0007221; complex GO:1990433; nucleus.
- MODIFY: positive regulation of DNA-templated transcription (NAS) -> GO:0007221.
- Developmental IMP terms (mesodermal fate, stem cell proliferation) kept as non-core. No REMOVE.

## Deep research
- Falcon deep research completed (sel-8-deep-research-falcon.md; the first wrapper run reported a 600 s timeout but the Falcon job finished and wrote the report). Consistent with the review. Additional points:
  - Mastermind assignment "rests primarily on its conserved role in the Notch transcription complex rather than strong primary-sequence similarity to non-nematode Mastermind proteins" - relevant variant note: no PANTHER family on the UniProt record.
  - Recent work (Zhou et al. 2023-2025, not cached) implicates SEL-8 in neuronal LIN-12/OSM-11 Notch signaling linking hypodermal insulin signaling to associative memory.
