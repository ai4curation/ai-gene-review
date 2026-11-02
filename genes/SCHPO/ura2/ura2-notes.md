# ura2 (SPAC16.03c, UniProt Q9UTI0) notes

Naming trap: S. pombe ura2 = monofunctional dihydroorotase, ortholog of S. cerevisiae URA4 (not URA2). Accession Q9UTI0 (PYRC_SCHPO) fetched correctly. No PMIDs in GOA.

## Evidence
- Class II DHOase, Zn-dependent [file:SCHPO/ura2/ura2-uniprot.txt "Reaction=(S)-dihydroorotate + H2O = N-carbamoyl-L-aspartate + H(+);"]. UniProt name is still "Probable dihydroorotase".
- ura2 deletion is a uracil auxotroph; described as dihydroorotase [PMID:23555823 "This was specific to the ura4 gene and was not observed in the other uracil auxotrophs, ura1, ura2, ura3, and ura5."].
- Supplies the activity missing from the defective DHOase-like domain of ura1 [file:SCHPO/ura1/ura1-uniprot.txt].

## Decisions
- 10 rows: 7 ACCEPT, 1 KEEP_AS_NON_CORE (nucleus ISO from S. cerevisiae URA4 HDA), 2 MODIFY (generic hydrolase terms -> GO:0004151).
- Core MF GO:0004151, BP 'de novo' UMP, cytoplasm (GO-CAM uses cytoplasm; others in pathway use cytosol).
- No direct enzymology on ura2 in GOA; suggested experiment added.
