# wbpL (PA3145, G3XD50) review notes

No deep-research provider was available. Literature checked by hand on 2026-11-05: cached
PMID:9680202 (abstract only; no PMC copy), Europe PMC search "wbpL AND aeruginosa" (recent
hits are phenotype or phage-receptor papers, with no biochemical assay of WbpL). The 1998 paper
remains the primary functional study.

## Function

- WbpL is a 9-TM polyprenyl-phosphate HexNAc-1-phosphate transferase of the Pfam PF00953
  "Glycos_transf_4" (WecA/MraY) family; PANTHER PTHR22926:SF3 (undecaprenyl-phosphate
  alpha-N-acetylglucosaminyl 1-phosphate transferase subfamily), CDD cd06854 GT_WbpL_WbcO_like.
- It initiates both O antigens of PAO1 [PMID:9680202 "In this study, chromosomal wbpL mutants
  were generated that did not express A band or B band, indicating that WbpL initiates the
  synthesis of both LPS molecules."].
- Cross-complementation with E. coli WecA [PMID:9680202 "Cross-complementation experiments
  using WbpL and its homologue, Escherichia coli WecA, demonstrates that WbpL is bifunctional,
  initiating B-band synthesis with a Fuc2NAc residue and A-band synthesis with either a GlcNAc
  (N-acetylglucosamine) or GalNAc (N-acetylgalactosamine) residue."].
- The acceptor is undecaprenyl phosphate [PMID:9680202 "WbpL, a transferase encoded within
  the B-band biosynthetic cluster, was previously proposed to initiate B-band biosynthesis
  through the addition of Fuc2NAc (2-acetamido-2,6-dideoxy-D-galactose) to undecaprenol
  phosphate (Und-P)."]. Like WecA (EC 2.7.8.33), it transfers a sugar-1-phosphate from a
  UDP-sugar to Und-P. In GO and EC terms that is a phosphotransferase for substituted phosphate
  groups (GO:0016780), not a glycosyltransferase (GO:0016757), whatever the Pfam family name.
  GO has no term for the Fuc2NAc-1-P or GalNAc-1-P transfer, so GO:0016780 is as specific as
  the evidence allows.

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; other seeds' rows from QuickGO, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000532005 | GO:0009103 lipopolysaccharide biosynthetic process | 3 | 35 (27 taxa) | GO:0009103, IMP, PMID:9680202 (PseudoCAP); GO:0009243 O antigen biosynthetic process, IDA, PMID:9680202 (PseudoCAP) | SOUND | The wbpL mutant makes neither A-band nor B-band O antigen, and WbpL performs the initiating step. The abstract shows mutant and cross-complementation data, so IMP or IGI would fit the GO:0009243 row better than IDA; the full text was not read, so the code is not challenged. | E. coli WecA P0AC78 (IDA PMID:11700352, UniProt); Thermotoga Q9X1N5 (IDA PMID:18723618, UniProt) | Yes |

The node term LPS biosynthetic process suits the clade: WecA-like initiating transferases
start O antigen and, in enterobacteria, enterobacterial common antigen (ECA). At gene level
WbpL's more specific process is O antigen biosynthesis, so the GO:0009103 rows are
TOO_GENERAL here. That is not a defect. No PSEUDOCAP or GO_CENTRAL defect on the seeding
rows.

Other PseudoCAP row (not a seed): GO:0016757 glycosyltransferase activity, IMP, PMID:9680202.
The term class is wrong for a sugar-1-phosphate transferase. MODIFY to GO:0016780, with a
PSEUDOCAP WRONG_TERM defect (PROBABLE: abstract only).

Non-seeded IBAs from PTN000531998 (GO:0044038 cell wall macromolecule biosynthetic process,
GO:0071555 cell wall organization; seeds WecA P0AC78 and Q9X1N5): WbpL makes O antigen, an
outer-membrane LPS component, not peptidoglycan or another cell-wall polymer. Marked
over-annotated for WbpL. These rows rest on the seeds' own IDA rows, and the node also covers
MraY-like and other members that do build cell-wall precursors, so no GO_CENTRAL defect is
filed from this gene.

Consistency: for GO:0009103 versus GO:0009243 the earlier wbp reviews differ (wbpX
TOO_GENERAL, wbpY MODIFY). This review follows the tier-2 convention: GO:0009243 is part_of
GO:0009103, so TOO_GENERAL.
