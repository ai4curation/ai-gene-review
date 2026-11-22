# ura1 (SPAC22G7.06c, UniProt Q09794) notes

Naming trap: S. pombe ura1 = CAD-like GLNase/CPSase-ATCase (ortholog of S. cerevisiae URA2), NOT budding-yeast URA1 (DHODH). Accession Q09794 (PYR1_SCHPO) fetched correctly.

## Evidence
- Bifunctional GLNase/CPSase-ATCase, steps 1-2 [PMID:8590465 "The URA1 gene encodes the bifunctional protein GLNase/CPSase-ATCase which catalyses the first two steps of the pyrimidine biosynthesis pathway."]; both activities on one polypeptide and UTP-inhibited (same abstract); cryptic DHOase domain [PMID:8590465 "one cryptic DHOase (dihydroorotase) domain"].
- ura1 is the ATCase structural gene [PMID:6961452 "thereby demonstrating that ural is the structural gene for aspartate transcarbamylase of S. pombe"].
- UniProt: DHOase domain defective; DHOase supplied by ura2 [file:SCHPO/ura1/ura1-uniprot.txt "The DHOase domain is defective. The third step of the de novo"]; cytoplasmic CPSase P vs mitochondrial arginine CPSase A (arg5/arg4), separate carbamoyl-phosphate pools.
- Cytosol [PMID:16823372].

## Decisions
- 27 rows: 16 ACCEPT (incl. NOT dihydroorotase), 5 KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED, 2 MODIFY, 1 REMOVE.
- GO:0003922 GMP synthase (glutamine-hydrolyzing) IGI from PMID:8590465 (WITH SGD URA2) looks like a term-selection slip for GO:0004088 CPSase (glutamine-hydrolyzing) -> MODIFY. Derived GO:0006177 GMP biosynthetic process (GO_REF:0000108) -> REMOVE. Flag to PomBase.
- Core MFs GO:0004088 and GO:0004070, BP 'de novo' UMP, cytosol; consistent with S. cerevisiae URA2 review.
