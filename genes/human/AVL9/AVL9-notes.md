# AVL9 notes

## 2026-10-05 review (PAINT, affinage)

- Migration: [PMID:22595670 "Here, we find that Rab4, Rab11, and Rab14 and the candidate Rab GDP-GTP exchange factors (GEFs) FAM116A and AVL9 are required for cell migration."] The direction is opposite in MDCK cells (PMID:25621300), where knockdown promoted migration. Cell migration is accepted as the core process.
- No Rab GEF activity: [PMID:22595670 "Despite repeated attempts, it was not possible to measure Avl9 GEF activity toward any of the Rabs tested under the assay conditions used."]
- Arf GAP: [PMID:41542567 "We determined that Avl9 possesses robust Arf-GAP activity and is recruited to secretory vesicles by Rab8."] This is a bioRxiv preprint, and all the biochemistry is on yeast Avl9. For human AVL9, only the R111A migration phenotype is reported. No NEW GO:0005096 is proposed; it is recorded as a knowledge gap instead.
- Localization: recycling-endosome overlap is partial (PMID:22595670). HPA calls the protein ER, and AVL9 has no OpenCell line (AVL9-bioinformatics/RESULTS.md). The predicted TM helix (214-230) sits inside the cDENN domain, so the membrane row is kept as non-core.
- The PDAC IκBα-SKP1 scaffold report (PMID:39566663, abstract-only) is not used for any annotation.

## 2026-10-05 revision (reviewer round 1)

- The preprint was published as PMID:42714338 (J Cell Biol 2026). [PMID:42714338 "Together these results support the prediction that human AVL9 functions as a GAP and indicate that the role of AVL9 in cell migration of A549 cells is directly tied to its GAP activity."]
- Added NEW GO:0005096 (ISS). AVL9 is the catalyst, so it does the work of the activity. The comparator Arf GAPs (for example SMAP2, the Age2 homolog used as the benchmark) carry GO:0005096.
- Recycling-endosome overlap (PMID:22595670) used expressed protein, whereas HPA endogenous staining is ER.
