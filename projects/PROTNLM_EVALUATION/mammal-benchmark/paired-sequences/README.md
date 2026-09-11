# Human–horse sequence comparisons

These global alignments compare the exact selected horse protein with the downloaded human Swiss-Prot canonical sequence. Run `uv run compare.py HUMAN-uniprot.txt HORSE-uniprot.txt OUTPUT.json` from the repository root with the appropriate paths. The script pins Biopython 1.85 and uses BLOSUM62 with gap opening −10 and extension −0.5. JSON records include the full alignment, input paths and sequence hashes, identities, and residue coverage.

Identity is calculated among residue–residue columns; coverage is the fraction of each input paired with a residue. Terminal and internal gaps therefore reduce coverage rather than identity. Similarity corroborates family assignment but does not establish reciprocal orthology, prove every isoform is functional, or exclude a gene-model error. Current sequences need not be the sequences originally submitted to ProtNLM.

- [x] Results computed from downloaded records, with no hardcoded results.
- [x] Script exercised on ten distinct gene pairs.
- [x] Full alignments and input hashes retained in JSON.
- [x] Alignment calculations completed for all ten supplied pairs.
- [ ] Reciprocal orthology and transcript-model correctness independently established: these require additional evidence beyond this analysis.

In particular, the selected horse DYNLT2B protein is 245 residues whereas the human canonical protein is 142 residues. Only 52.2% of the horse sequence pairs with human residues, despite 91.4% identity among paired positions. This warrants examination of the extra sequence before transferring detailed localization or interaction claims. WEE1 is 646 residues in both species with 95.4% identity and complete paired coverage. The different outcomes demonstrate why identity alone is insufficient.
