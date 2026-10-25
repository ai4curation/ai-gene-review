# rpsA (P0AG67, E. coli K-12) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: rpsA is the experimentally characterised SF7 relative used as the transfer
reference for DEIRA/Q9RSY6. No ProtNLM2 output was consulted.

### Provenance / tooling
- `just fetch-gene ECOLI rpsA` created uniprot, goa (30 rows) and the review stub.
- `just deep-research-falcon ECOLI rpsA --fallback perplexity-lite` FAILED: falcon
  "Failed to authenticate"; perplexity-lite HTTP 401 insufficient_quota. No
  deep-research file exists; the review is based on cached primary literature.
- `just fetch-fitness ECOLI rpsA` failed (no FEBA source reachable). rpsA is essential
  in any case [PMID:9677288 "This exogenous source of protein S1 was essential for growth."].
- Additionally cached: PMID 24339747, 15340139, 12068815, 7003157, 11593008, 778845,
  25122749, 23653193, 11101533, 17376482, 17392345, 35264790.

### Evolutionary grounding
- PANTHER PTHR10724:SF7 (SMALL RIBOSOMAL SUBUNIT PROTEIN BS1C), same subfamily as Q9RSY6;
  SF7 holds bacterial bS1 and plastid bS1c proteins (50 members in the entries file).
- PAINT PTN000076677 (seeds P0AG67, AT5G30510, P46837/YhgF) carries mRNA binding,
  structural constituent of ribosome and translation. The node also spans SF10 (Tex/YhgF),
  which is not ribosomal; ribosome terms should be read as bS1-specific.
- PTN000076734 (taxon Bacteria) carries cytosolic small ribosomal subunit.

### Experimentally established in E. coli (vs inferred)
- 30S subunit protein, loosely bound, anchored by N-terminal domain to uS2
  [PMID:22412910 "the N-terminal domain of S1 (amino acids 1-106; S1(106)) is necessary and sufficient for the interaction with protein S2 as well as for ribosome binding"];
  [PMID:12068815 "demonstrating that S2 is essential for binding of S1 to the 30S ribosomal subunit"].
- mRNA binding / ssRNA binding / unwinding [PMID:22908248 "each S1 binds 10 nucleotides of RNA in a multistep fashion"];
  RNA chaperone in initiation [PMID:24339747 "r-protein S1 endows the 30S with an RNA chaperone activity"].
- Required for translation of most natural mRNAs [PMID:9677288], dispensable for leaderless
  mRNAs [PMID:12068815 "S1 is indeed dispensable for translation of leaderless mRNAs"].
- Translational autorepression of rpsA [PMID:2120211].
- tmRNA binding established; role in trans-translation disputed
  [PMID:17376482 "S1 does not play a role in the trans-translation machinery"] vs
  [PMID:17392345 "S1 has a role in tmRNA-mediated tagging that is distinct from its role during canonical translation"]. No trans-translation term proposed.
- Phage functions (Qbeta replicase subunit, T4 RegB activation, ModB RNAylation) noted
  in description only; not annotated as host processes.

### Decisions
- GO:0000028 ribosomal small subunit assembly (IDA, PMID:3297162): MARK_AS_OVER_ANNOTATED;
  abstract is an NMR/proteolysis structure study and S1 binds a pre-formed 30S via uS2.
- membrane (HDA): MARK_AS_OVER_ANNOTATED (ribosome co-fractionation).
- nucleic acid binding IEA -> MODIFY to RNA binding; ribosome IEA -> MODIFY to cytosolic SSU.
- NEW: GO:0006413 translational initiation (IDA PMID:24339747). Participation: S1 itself
  captures/unfolds mRNA and positions the start codon on the 30S.
- Transfer caution for Q9RSY6: S1 domain number and N-terminal uS2-binding domains vary among
  bS1 lineages; structural-constituent and mRNA-binding functions are SF7-wide (PAINT),
  whereas autoregulation, tmRNA and phage roles are E. coli-specific findings.
