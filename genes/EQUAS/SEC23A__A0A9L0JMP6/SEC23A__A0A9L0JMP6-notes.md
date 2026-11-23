# SEC23A (donkey, Equus asinus) - A0A9L0JMP6 (gene-centric canonical)

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. This folder holds the UniProt gene-centric canonical product
(765 aa) of donkey SEC23A (Ensembl gene ENSEASG00005007615); the ProtNLM2 benchmark entry
A0A9L0IQB9 (739 aa, in-frame exon-skipping transcript) is reviewed separately in genes/EQUAS/SEC23A.

### Setup
- `just fetch-gene EQUAS A0A9L0JMP6 --alias SEC23A__A0A9L0JMP6`: 11 IEA GOA rows (3 TreeGrafter
  GO_REF:0000118 citing PTN000124665, 3 UniProt SubCell GO_REF:0000044, 4 InterPro2GO GO_REF:0000002,
  1 combined GO_REF:0000120). Same term set as A0A9L0IQB9.
- Deep research: `just deep-research-falcon EQUAS SEC23A__A0A9L0JMP6 --fallback perplexity-lite`
  failed (exit 1; falcon and the perplexity-lite fallback both failed, as for the sibling entry).
  No deep-research file exists; the review uses cached primary literature and Swiss-Prot Q15436.

### Evolutionary grounding
- UniProt DR: PANTHER PTHR11141:SF7 (PROTEIN TRANSPORT PROTEIN SEC23A), the subfamily of human
  Q15436 and mouse Q01405 (interpro/panther/PTHR11141/PTHR11141-entries.csv). Human SEC23B is SF10;
  yeast Sec23 is SF0.
- `SEC23A__A0A9L0JMP6-bioinformatics/compare_orthologs.py` (live UniProt sequences): 99.35% identity
  to human and mouse SEC23A over 765 pairs, no gaps; 85.10% to human SEC23B; 51.00% to yeast Sec23.
  Zn ligands C61/C66/C85/C88, CLSD F382 and gelsolin PPP-binding F628/Y672/Y678/F681 conserved at the
  human positions; yeast arginine finger R722 aligns to donkey R716 [file:EQUAS/SEC23A__A0A9L0JMP6/SEC23A__A0A9L0JMP6-bioinformatics/RESULTS.md].
- Human SEC23A IBA rows (GAP activity, cargo loading, ER exit site, COPII vesicle coat) come from
  PTN000124617; the donkey TreeGrafter node PTN000124665 was not traced to PTN000124617.

### What is experimental, and where
- Donkey: nothing experimental. All functions are inferred.
- Human SEC23A (SF7): transitional-ER/vesicle localization, cytosolic complex, yeast sec23-1 complementation
  [PMID:8898360]; F382L loses budding activity [PMID:16980979]; mutant poorly recruits Sec13-Sec31
  [PMID:17981132]; SEC22B binding at the Sec23/24 interface [PMID:17499046]; gelsolin-like domain binds
  TANGO1/cTAGE5/Sec31 PPP motifs, mutagenesis of F628/Y672/Y678/F681 [PMID:27551091].
- Yeast Sec23 (SF0): Sar1 GAP activity [PMID:8451644]; arginine finger structure [PMID:12239560].
  GAP activity is therefore a family-level (SEC23 node) inference, not measured on mammalian SEC23A
  in the cached literature.

### Decisions
- ACCEPT: GTPase activator activity, ER membrane, cytosol, ER to Golgi vesicle-mediated transport,
  ER to Golgi transport vesicle membrane, COPII vesicle coat, ER exit site, COPII-coated vesicle cargo
  loading, COPII-coated vesicle budding.
- KEEP_AS_NON_CORE: intracellular protein transport (broad; not an ancestor of the specific accepted
  process terms), zinc ion binding (structural Zn site).
- No NEW terms. The zebrafish morpholino phenotype in PMID:16980979 and the GLUT4-translocation
  statement (by similarity from mouse in Swiss-Prot) were not used as process evidence.
