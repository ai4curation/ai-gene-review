# FPS1 (ARATH) review notes

## 2026-10-28 session
- fetch-gene resolved Q09152 (FPPS1_ARATH, TAIR AT5G47770, GeneID 834828); 19 GOA rows.
- No deep-research providers; manual literature in FPS1-deep-research-manual.md.
- Key experimental paper PMID:23145086 (full text): FPS1S purified and kinetically
  characterised ["Purified FPS1S and FPS2 were also subjected to kinetic analyses and the resulting steady-state kinetic constants are shown in Table 1."];
  GFP fusions cytosolic ["Under our experimental conditions all the four fusion proteins localized exclusively in the cytosol (Figure 5)."].
- Mitochondrial FPS1L: PMID:9182568 (abstract only) import experiments.
- Decisions:
  - MF: GO:0004337 and GO:0004161 accepted (both half-reactions of FPS). Generic
    prenyltransferase / alkyl transferase IEA rows MODIFY to GO:0004337.
  - CC: cytosol accepted (GFP, HDA, IBA); cytoplasm MODIFY -> cytosol; mitochondrion
    accepted for FPS1L (root organelle; only the transit peptide/import line supports a
    sub-compartment, so no NEW matrix term). Plastid HDA (membrane proteomics) marked
    over-annotated: no plastid targeting, GFP excludes it.
  - BP: FPP biosynthetic process accepted; isoprenoid biosynthetic process MODIFY ->
    GO:0045337; GPP biosynthetic process kept as non-core (GPP is the reaction
    intermediate, not the physiological product; plastid GPPS makes monoterpene GPP).
  - No NEW process terms: embryo lethality of fps1 fps2 is necessity evidence only.
