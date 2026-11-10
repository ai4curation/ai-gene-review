# elo-6 review notes

- UniProt Q20303 (ELO6_CAEEL, Swiss-Prot), WormBase WBGene00001244, GeneID 177321. Fetched
  accession matches the requested one.
- Only experimental paper: PMID:15340492 (Kniazeva et al. 2004, full text cached). RNAi of elo-6
  reduces only C17ISO ["The RNAi of elo-6 significantly reduced the amount of only C17ISO"];
  authors infer ELO-6 elongates C15ISO to C17ISO. No biochemical assay.
- UniProt CATALYTIC ACTIVITY (RHEA:35335) is attributed ECO:0000269 to PMID:15340492, but that
  paper has no enzyme assay; the reaction is an inference. Not a GOA row here (no EXP MF row), so
  recorded only as a suggested question; cf. the parallel bckd-1A review where the EXP row exists.
- IBA rows all come from PTN000125390, the PTHR11157 family root. The family review
  (interpro/panther/PTHR11157/PTHR11157-review.yaml) notes substrate-class process terms are
  paralog-specific. For ELO-6: saturated FA elongation is consistent (iso-FAs are saturated);
  MUFA/PUFA/VLCFA/sphingolipid terms lack ELO-6-specific support -> MARK_AS_OVER_ANNOTATED.
- Sphingoid base in worms is made from C15ISO (ELO-5 product), not C17ISO [PMID:38704027].
- ER membrane: family-wide; 7 TM; no ELO-6 localisation data. Accepted from IBA.
- Broad IEA BP rows (lipid metabolic process, fatty acid biosynthetic process) and membrane CC
  MODIFIED to the specific terms already carried.
- No NEW terms proposed.
