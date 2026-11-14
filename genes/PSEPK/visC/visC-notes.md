# visC (PP_5197, Q88CI4) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research available (no provider keys); OpenScientist gene
and pathway reports read. Unreviewed UniProt entry: COFACTOR, PATHWAY, SUBUNIT and SIMILARITY
lines are ARBA-only and not used as support.

Which hydroxylase is it? (analysis in `visC-bioinformatics/RESULTS.md`)
- Closest E. coli homolog UbiI (46.7%), then UbiF (42.1%), UbiH (35.3%). UbiI/UbiF are sister
  clades, so identity alone is a narrow margin; the PANTHER placement is decisive: the
  TreeGrafter GO:0019168 row comes from PTN002466904, below the UbiI IBD node PTN000350245
  (seed E. coli UbiI), not the UbiF node PTN001789718 (GO:0008682).
- KT2440 has no UbiF; it has UbiH (PP_5199) and Coq7 (PP_0427), the P. aeruginosa set:
  [PMID:27822549 "in P. aeruginosa and A. ferrooxidans (UbiH, UbiI, and Coq7) (16)."]
- E. coli: [PMID:23709220 "Based on genetic and biochemical experiments, we establish that the
  UbiI protein functions in the C5-hydroxylation reaction."] and [PMID:23709220 "We also
  demonstrate that UbiI is only implicated in aerobic Q biosynthesis"].
- Source defect recorded: the DE SubName "Oxidoreductase involved in anerobic synthesis of
  ubiquinone" (EMBL import) is wrong; KT2440 lacks UbiT/U/V (project pathway report).
- Ubi complex (GO:0110142, ARBA): kept non-core; E. coli complex has UbiF, KT2440 uses Coq7,
  so composition of a P. putida complex is unknown.
- Decisions: GO:0019168, GO:0006744 ACCEPT; GO:0004497, GO:0016705 MODIFY to GO:0019168; FAD
  binding rows KEEP_AS_NON_CORE (same as ubiH); GO:0110142 KEEP_AS_NON_CORE.

Module agreement: `polyprenylphenol_hydroxylase_activity` (GO:0019168), labelled "UbiH/VisC-
family"; the module could relabel it "UbiI/VisC" since this is the UbiI clade, not UbiH.
