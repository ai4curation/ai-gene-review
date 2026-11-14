# ubiH (PP_5199, Q88CI2) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research available (no provider keys); OpenScientist report
read critically. Unreviewed UniProt entry: its COFACTOR, PATHWAY and SIMILARITY lines are
ARBA-only, so only DR family signatures are quoted. No KT2440 experiment.

Hydroxylase assignment in KT2440 (see `../visC/visC-bioinformatics/RESULTS.md`):
- PP_5199 (this gene): UbiH. NCBIfam TIGR01984 UbiH, InterPro IPR011295, PANTHER
  PTHR43876:SF8; TreeGrafter row inherits GO:0008681 from UbiH node PTN000350242 (seed E. coli
  P25534). Pairwise identity: 40.5% to E. coli UbiH vs 34.4% UbiI, 36.2% UbiF.
- PP_5197 (visC): UbiI-type C-5 hydroxylase. PP_0427 (coq7): di-iron Coq7, C-6.
- [PMID:27822549 "constituting two different protein sets in E. coli (UbiF, UbiH, and UbiI)
  (11) and in P. aeruginosa and A. ferrooxidans (UbiH, UbiI, and Coq7) (16)."] KT2440 has the
  P. aeruginosa-type set.
- Ring numbering: Pelosi et al. use UbiH = C-1, UbiI = C-5, UbiF/Coq7 = C-6 (UbiA-product
  numbering); Kwon et al. 2000 (PMID:10802164) used C-4 (UbiH), C-6, C-5.
- GO:0008681 is octaprenyl-specific; KT2440 makes UQ-9. No chain-neutral NAD(P)H term exists
  (GO:0120538 is the ferredoxin-dependent version). Accepted, caveat recorded, ontology
  question raised in suggested_questions.
- Deep-research errors (reference_review LOW_QUALITY): calls PP_5197 "ubiV"; lists ubiC as
  PP_5013 (actually ubiB) and PP_0548 as UbiF-type (actually ubiX).
- Decisions: GO:0008681, GO:0006744 ACCEPT; GO:0003824, GO:0016705 MODIFY to GO:0008681;
  FAD binding rows (GO:0050660, GO:0071949) KEEP_AS_NON_CORE.

Module agreement: `octaprenyl_methoxyphenol_hydroxylase_activity` (GO:0008681). Consistent.
