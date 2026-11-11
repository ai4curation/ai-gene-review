# DYNLT2B (horse, A0A9L0S9P8) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Target: A0A9L0S9P8, the UniProt reference-proteome (UP000002281) gene-centric entry for equine DYNLT2B
(Ensembl ENSECAG00000015913, chr 19). Folder follows the `HOST__ACC` convention because the benchmark
model A0A9L0SWY1 of the same gene already occupies `genes/HORSE/DYNLT2B/`. ProtNLM2 files were not opened.

### Inputs
- `just fetch-gene HORSE A0A9L0S9P8 --alias DYNLT2B__A0A9L0S9P8`: GOA has no rows for this accession
  (header-only goa.tsv), so there were no existing annotations to adjudicate.
- Deep research: `just deep-research-falcon HORSE DYNLT2B__A0A9L0S9P8 --fallback perplexity-lite` failed
  (falcon failed; perplexity-lite HTTP 401 "You exceeded your current quota"). No deep-research file was
  written. The review relies on cached full-text papers PMID:29742051, PMID:25830415, PMID:38454149,
  PMID:39827215, the human Swiss-Prot record Q8WW35 and the human review `genes/human/DYNLT2B`.
- No equine-specific functional literature exists; everything functional is human/mouse.

### Sequence analysis (new)
`DYNLT2B__A0A9L0S9P8-bioinformatics/compare_s9p8.py` -> `RESULTS.md`, `results.json`.
- 145 aa, starts with G (no initiator Met). 78.83% identity over 137 aligned pairs with human Q8WW35;
  continuous identity begins at human residue 38.
- Last 105 residues identical to A0A9L0TLH8 (the human-like full-length equine model) and A0A9L0S150
  (Ensembl canonical). Only the 40-residue prefix GESSHSWLLTLIDLKVKKIKNGSLEVKLTAPSPSLKCSST differs; it
  replaces TLH8's MAAPRDASFSAGVSFSVADSLPETEKNAGESENTYILRPIFQQ, which carries human strand 1 (SIGVSFSV).
- Mapping PDB 8RGI elements: strand 1 (h4-11) 1/8 identical; helices h41-56 and h66-81 16/16 and 14/16;
  strands h89-99, 104-113, 119-126, 128-140 11/11, 9/10, 8/8, 13/13. So unlike the benchmark SWY1 (which
  lacks the C-terminal strand), S9P8 keeps the C-terminus but lacks the first strand. Most likely an
  incomplete/mis-joined 5' gene model; not demonstrated either way.
- Caveat on the sibling `RESULTS-rereview.md`: its "all human strands" column counts aligned positions,
  not identity, so it reports True for S9P8.

### Evolutionary grounding
- PANTHER PTHR21255:SF7 (DYNLT2B-specific subfamily) for S9P8 (UniProt DR line) and for human Q8WW35;
  family review `interpro/panther/PTHR21255` agrees for SF7 membership.
- PAINT node PTN000478852 (seen in human IBA rows): GO:0045505 dynein intermediate chain binding,
  GO:0005868 cytoplasmic dynein complex, GO:0007018 microtubule-based movement, GO:0005737 cytoplasm.
- Human GO:0035721 intraciliary retrograde transport, cilium assembly, ciliary base: IMP/IDA only on human,
  not propagated by PAINT; treated as a deliberate omission and not added. Mouse sperm-flagellum phenotypes
  (PMID:39827215) are organismal and not annotated. GO:0045503 dynein light chain binding (human X-ray
  DYNLT1-DYNLT2B) is also not propagated by PAINT; not added.

### Review decisions
- NEW ISO GO:0045505 and GO:0005868 (same as for the benchmark sibling), with core_function MF GO:0045505
  in_complex GO:0005868 and deliberately no directly_involved_in process.
- Experimental status in horse: none. All function is orthology-inferred.
- No gocams/index.tsv entry for DYNLT2B.
