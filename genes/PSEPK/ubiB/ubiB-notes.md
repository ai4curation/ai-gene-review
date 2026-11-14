# ubiB (PP_5013, A0A140FWS4) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research (no provider keys); OpenScientist report read.
Unreviewed UniProt entry (HAMAP MF_00414, with a CAUTION that some residues needed for feature
propagation are not conserved). No KT2440 experiment.

- Not a protein kinase: [PMID:27499294 "Although COQ8 was predicted to be a protein kinase, we
  demonstrate that it lacks canonical protein kinase activity in trans."]; [PMID:25498144
  "UbiB proteins adopt an atypical PKL fold with multiple UbiB-specific features positioned to
  inhibit protein kinase activity."]
- ATPase in E. coli UbiB: [PMID:29198567 "We found that ATPase activity is an evolutionarily
  conserved feature of COQ8 orthologs from E. coli to humans that is enhanced by phenolic
  compounds resembling CoQ biosynthetic precursors."] The assay used purified MBP-tagged E. coli
  UbiB lacking its TM region. This is direct evidence on the bacterial ortholog, so ATP
  hydrolysis (GO:0016887) as core MF of PP_5013 is a defensible orthology inference; the
  OpenScientist motif table shows the KxGQ and catalytic-loop Asp shared with E. coli UbiB.
- Protein kinase activity row MODIFY (lateral) to GO:0016887; regulation of ubiquinone
  biosynthesis MARK_AS_OVER_ANNOTATED (speculative HAMAP "UbiI regulator").
- E. coli necessity: [PMID:10960098 "lack CoQ and accumulate octaprenylphenol."]
- Deep research error: says P. putida depends on ubiquinone-8 (it is UQ-9).

Module: `ubib_pathway_accessory_factor` asserts no MF. This review asserts ATP hydrolysis
activity as core MF; reported to the coordinator as a deliberate difference.
