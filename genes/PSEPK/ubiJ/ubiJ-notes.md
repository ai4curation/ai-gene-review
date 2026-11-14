# ubiJ (PP_5012, Q88D16) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research (no provider keys); OpenScientist report read.
Unreviewed UniProt entry with HAMAP MF_02215 curated text. No KT2440 experiment.

- HAMAP: "Binds hydrophobic ubiquinone biosynthetic intermediates via its SCP2 domain and is
  essential for the stability of the Ubi complex." SCP2 domain 14-111 (Pfam PF02036), coiled
  coil 173-207.
- E. coli: [PMID:30686758 "The SCP2 domain of UbiJ forms an extended hydrophobic cavity that
  binds UQ intermediates inside the 1-MDa Ubi complex."]; [PMID:24142253 "Under aerobic
  conditions, an ubiJ mutant was found to be impaired for Q8 biosynthesis"].
- Added NEW MF GO:0019840 isoprenoid binding (two lines: SCP2 domain + HAMAP text, E. coli
  structure/biochemistry). Chosen over the parent GO:0008289 lipid binding because the ligands
  are polyprenylated intermediates; matches the E. coli UbiJ review. The module plans
  GO:0008289; GO:0019840 is_a GO:0008289, so they agree, at different depth.
- Added NEW GO:0110142 ubiquinone biosynthesis complex (part_of).
- Cytoplasm MODIFY to cytosol (soluble complex from cytoplasmic extracts), aligned with
  E. coli UbiJ, PSEPK ubiC and ubiK.

Module agreement: `ubij_metabolon_scaffold` (GO:0006744). Consistent.
