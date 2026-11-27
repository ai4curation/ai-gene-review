# SCHPO zim17 manual deep research

Automated deep research was attempted with Perplexity, but the provider was not
available in this environment. The available literature is almost entirely from
_Saccharomyces cerevisiae_ ZIM17/HEP1/TIM15 and human DNLZ/HEP1; the _S. pombe_
SPAC24H6.02c product is a Swiss-Prot reviewed but uncharacterized 175 aa protein
with the DNL-type zinc-finger signature, PomBase identifier SPAC24H6.02c, and
InterPro/PANTHER/Pfam cross-references to the mtHsp70 escort family
(`IPR024158`, `IPR007853`, `PTHR20922`, `PF05180`).

## Direct _S. pombe_ evidence

- The sole direct _S. pombe_ GOA literature row is the Matsuyama et al. ORFeome
  localization screen [PMID:16823372], a proteome-scale YFP-tagging experiment
  that "determined the localization of 4,431 proteins". This supports a
  mitochondrion row, but the abstract and cached record do not identify zim17
  specifically or resolve the matrix versus membrane face.
- UniProt carries no named gene symbol for Q09759; `zim17` is supplied by the
  GO-CAM/PomBase label, while the UniProt flat file lists only
  `ORFNames=SPAC24H6.02c`.

## Conserved Zim17/Hep1/Tim15 function

- Burri et al. identified budding-yeast Zim17 as an essential mitochondrial
  DNL zinc-finger protein involved in protein import [PMID:15383543]. Their
  abstract reports that "Loss of Zim17 selectively diminishes import of
  proteins into the matrix of mitochondria" and proposed a specialized
  Pam18-adjacent role for Zim17 in substrate loading onto Hsp70.
- Yamamoto et al. independently named the same budding-yeast protein Tim15/Zim17,
  described it as a 15 kDa peripheral inner-membrane protein with a zinc-finger
  motif, and concluded that "Tim15/Zim17 therefore cooperates with mtHsp70 to
  facilitate import of presequence-containing proteins into the matrix"
  [PMID:15642367].
- Sanjuan Szklarz et al. separated the immediate and downstream effects of Zim17
  loss in budding yeast: short temperature shift of a zim17 mutant caused
  aggregation of matrix Hsp70s before strong import, Fe/S, or morphology
  phenotypes, leading them to conclude that Zim17 "plays a specific role in
  preventing protein aggregation in the mitochondrial matrix" [PMID:15992824].
- Momose et al. solved the NMR structure of the Tim15 core domain and found that
  residues required for growth and matrix import also suppress mtHsp70
  aggregation, linking the DNL zinc-finger structure to this mtHsp70 escort
  activity [PMID:17571076].
- Blamowska et al. showed that Hep1 is required and sufficient with ATP/ADP for
  de novo folding of yeast mtHsp70 after mitochondrial import; their abstract
  states that "Thus, Hep1 acts as a specialized chaperone mediating the de novo
  folding of an Hsp70 chaperone" [PMID:23007651].
- Lewrenz et al. used conditional zim17 mutants to show that Zim17 is needed for
  Ssc1/Ssq1 functional substrate interaction, not merely for preventing bulk
  aggregation; their abstract concludes that Zim17 "directly assists the
  functional interaction of mtHsp70 with substrate proteins" in a J-type
  co-chaperone-dependent process [PMID:24030826].

## Annotation implications

- The mitochondrial root and matrix locations are conserved and consistent with
  the S. cerevisiae literature. Keep the root mitochondrion rows and the matrix
  ISO row; do not add a matrix-side inner-membrane row unless _S. pombe_ or
  ortholog evidence resolves SPAC24H6.02c as membrane-associated rather than
  matrix soluble.
- `GO:0044183` protein folding chaperone is a reasonable molecular function for
  the specialized Hep1/Zim17 chaperone role toward mtHsp70 itself.
- `GO:0030150` protein import into mitochondrial matrix is justified for the
  Zim17/Hep1 protein family because budding-yeast loss-of-function and
  conditional-mutant work connect Zim17 to presequence import through the Ssc1
  Hsp70 motor.
- `GO:0006457` protein folding is true for de novo folding of mtHsp70, but it is
  broader than the mechanistic MF and BP; keep it as non-core or over-annotated
  only if the rest of the review captures the specific mtHsp70-escort role.
- `GO:0051131` chaperone-mediated protein complex assembly is the shakiest IBA
  row. The yeast papers show Hsp70 folding, maintenance, anti-aggregation, and
  substrate interaction. They do not show that Zim17 assembles a protein complex
  in the usual GO:0051131 sense.
- `GO:0008270` zinc ion binding is a structural DNL zinc-finger call from
  InterPro/PROSITE and is real but not, by itself, the central chaperone
  activity.

## GO-CAM context

- GO-CAM 69729a3800007453 uses SPAC24H6.02c/Zim17 as a matrix-localized unknown
  molecular function in the protein-import-into-matrix pathway upstream of Ssc1.
  That is consistent with the current gene-level evidence: no more specific
  GO molecular function exists for the mtHsp70 escort/chaperone-of-chaperone
  activity.
