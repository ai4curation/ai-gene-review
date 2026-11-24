# MET2 notes (YNL277W, P08465)

- Homoserine O-acetyltransferase, EC 2.3.1.31, MetX family [UniProt:P08465 "SIMILARITY: Belongs to the AB hydrolase superfamily. MetX family."].
- Biochemistry: [PMID:3301801 "The reaction product was ascertained to be O-acetyl-L-homoserine by confirming that it produced L-homocysteine in an O-acetyl-L-homoserine sulfhydrylase reaction."]; [PMID:3301801 "Of the hydroxy amino acids examined, the enzyme showed reactivity only to L-homoserine."]
- First step of methionine branch [PMID:6035500 "Regulation of homoserine O-transacetylase, first step in methionine biosyntheis in Saccharomyces cerevisiae."] (no abstract cached).
- Cytoplasmic [UniProt:P08465 "SUBCELLULAR LOCATION: Cytoplasm"].

## Curation observations
- Threonine metabolic process RCA (P4-PWY-1 superpathway) REMOVED: Met2 diverts homoserine away from threonine.

## 2026-11-13 audit (acyl-donor check for methionine module)
- Acyl donor is acetyl-CoA, not succinyl-CoA [PMID:3301801 "Succinyl coenzyme A was not an acyl donor."]. GO:0004414 (not GO:0008899) is correct.
- Methionine represses enzyme synthesis but does not inhibit activity; SAM/SAH inhibit slightly [PMID:3301801 "S-Adenosylmethionine and S-adenosylhomocysteine slightly inhibited the enzyme, but methionine had no effect."].
- UniProt FUNCTION/CATALYTIC ACTIVITY for P08465 are by similarity to S. pombe Met6 (ECO:0000250|UniProtKB:O60062), not experimental on Met2.
- PANTHER PTHR32268:SF11 (UniProt DR line); IBA node PTN000791315 (seeded by SGD:S000005221 itself, PomBase met6, CGD, bacterial MetX).
- SGD hand-written description checked against PMID:3301801/PMID:6035500: no errors.
