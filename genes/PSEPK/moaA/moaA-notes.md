# moaA curation notes

## 2026-07-20 OpenScientist report assessment

The completed OpenScientist report is retained unchanged as provider output and
assessed as `LOW_QUALITY`. Its canonical GTP 3',8'-cyclase assignment and the
division of labor with MoaC agree with reviewed Q88E69 UniProt. It also
acknowledges that the mechanistic and structural evidence comes from orthologs.

The report nevertheless presents unsaved target residue/motif analysis, target
homodimer and structural transfer, heterologous xanthine-oxidase production, and
rate-defining or nonredundant physiological claims as Q88E69 evidence. Those
claims are not propagated, especially because the physiological roles of the
divergent PP_2482 and PP_1969 MoaA-family proteins remain unresolved. Q88E69 is
retained as the canonical KT2440 MoaA because its reviewed target record and
MoaA-specific domain set support the exact reaction.

## 2026-11-10 completion for the MoCo biosynthesis module

- Replaced quotes of UniProt DE name/EC lines (labels, not evidence) with the HAMAP CC
  FUNCTION and SIMILARITY lines and with ortholog publications (PMID:23627491,
  PMID:16632608, PMID:14761975).
- Added supported_by to the GTP binding (FT BINDING ligand GTP) and GO:0006777 (CC PATHWAY)
  rows; removed the reference entry that quoted the GOA table itself.
- Verdicts unchanged and aligned with ECOLI/moaA: GO:0061799 cPMP synthase stays REMOVE (MoaC
  activity; TreeGrafter batch-05 verdict retained), GO:0061798/GO:0051539/GO:1904047 ACCEPT,
  generic rows MODIFY. Status set to COMPLETE.
