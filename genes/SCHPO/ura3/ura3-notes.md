# ura3 (SPAC57A10.12c, UniProt P32747) notes

Naming trap: S. pombe ura3 = mitochondrial class 2 dihydroorotate dehydrogenase (quinone), functional counterpart of S. cerevisiae URA1 but NOT its ortholog (URA1 is an unrelated class 1A cytosolic fumarate enzyme acquired by HGT [PMID:15014982]); closest annotated ortholog is human DHODH. Not related to S. cerevisiae URA3 (OMPDC). Accession P32747 (PYRD_SCHPO) fetched correctly.

## Evidence
- Mitochondrial; activity requires intact respiratory chain [PMID:1409592 "The DHOdehase from Sch. pombe was localized in the mitochondria whereas its homolog from S. cerevisiae was found to be cytosolic."; "allowed us to demonstrate that the Sch. pombe DHOdehase activity requires the integrity of the mitochondrial electron transport chain."].
- Family 2, quinone acceptor [PMID:15196933 "One is closely related to the Schizosaccharomyces pombe mitochondrial family 2 enzymes, which use quinones as direct and oxygen as the final electron acceptor."]; UniProt Km for decylubiquinone; does not use fumarate or NAD [UniProt:P32747].
- Requires CoQ in vivo [PMID:23555823 "This is likely because Ura3 requires coenzyme Q for its activity."].
- Transit peptide 1-21, TM 38-54 [UniProt:P32747].

## Decisions
- 16 rows: 9 ACCEPT, 7 MODIFY (4x generic GO:0004152 -> GO:0106430; GO:0016627 -> GO:0106430; cytoplasm and membrane IEA -> mitochondrial inner membrane).
- Core MF GO:0106430, BP 'de novo' UMP, mitochondrial inner membrane. Matches GO-CAM 69a0c46f00003691 (GO:0106430, mitochondrial inner membrane).
