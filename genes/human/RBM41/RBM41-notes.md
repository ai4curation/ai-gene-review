# RBM41 (human, Q96IZ5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised relative (same PANTHER subfamily
PTHR16105:SF2, RNA-BINDING PROTEIN 41) of the donkey RBM41 entry. ProtNLM2 output was not consulted.

### Deep research
- `just deep-research-falcon human RBM41 --fallback perplexity-lite` failed: Edison API returned
  "Failed to authenticate" (403), and the perplexity-lite fallback also failed. No deep-research
  file exists; the review rests on the cached full text of PMID:38499487 and the UniProt record.

### Evolutionary placement
- PTHR16105 (RNA-BINDING REGION-CONTAINING PROTEIN 3) splits into SF0 (U11/U12-65K/RNPC3: human
  Q96LT9, mouse, rat, bovine, zebrafish, Arabidopsis SNRNP65 Q8RWV8) and SF2 (RBM41: human Q96IZ5,
  mouse Q8JZV4) (`interpro/panther/PTHR16105/PTHR16105-entries.csv`).
- All four IBA rows come from PTN000413238, a node above both subfamilies; every listed donor
  (AT1G09230, FBgn0265184, ZFIN rnpc3, human RNPC3) is an SF0/65K protein. So the IBAs reach RBM41
  across the paralog split, and each must be checked against RBM41-specific data.

### Experimental findings for human RBM41 (PMID:38499487, full text)
- RRM (267-413 construct) binds U12 and U6atac 3' stem-loop hairpins by EMSA, Kd ~2.1 and ~3.8 uM
  [PMID:38499487 "Thus, both RBM41 and U11/U12-65K C-terminal RRMs show dual snRNA binding specificity in vitro with only slight differences in RNA affinity"].
- RIP: tagged and endogenous RBM41 bring down U12, U4atac, U6atac but not U11 snRNA; RRM point
  mutants Q352A/F354A abolish this
  [PMID:38499487 "V5-RBM41 co-immunoprecipitated the U12 snRNA, U4atac and U6atac snRNAs, but not the U11 snRNA"].
- Glycerol gradient: RBM41 peaks with the U12 mono-snRNP, 65K with the di-snRNP
  [PMID:38499487 "RBM41 peak co-migrated with the U12 mono-snRNP"].
- BioID/co-IP: DHX8 association needs the RBM41 N-terminal region; ZCRB1 and coilin associations
  need RNA binding.
- Associates with excised U12-type intron lariats
  [PMID:38499487 "In contrast, RBM41 preferentially co-immunoprecipitated U12-type but not U2-type intron lariats"].
- Endogenous RBM41 in Cajal bodies
  [PMID:38499487 "Consistently, we found that endogenous RBM41 localizes to Cajal bodies, as shown by colocalization with coilin-GFP in HEK293 cells"].
- CRISPR KO HEK293: viable, weak but significant U12-type 3'ss changes.

### Decisions
- U12 snRNA binding, U12-type spliceosomal complex, mRNA splicing via spliceosome (IBA): ACCEPT,
  each corroborated by direct human data despite SF0 donors.
- pre-mRNA intronic binding (IBA): MARK_AS_OVER_ANNOTATED. No direct intron binding shown; lariat
  co-IP is explained by U12 snRNA association. Intron recognition is the 65K/di-snRNP stage.
- RNA binding / nucleic acid binding (IEA): MODIFY to U12 snRNA binding + U6atac snRNA binding.
- 39 protein binding rows (Y2H/AP-MS screens): REMOVE per protein-binding policy.
- NEW (IDA, PMID:38499487): U6atac snRNA binding, U12 snRNP, Cajal body.
- Not proposed: a process term for post-catalytic spliceosome disassembly/mRNA release. The paper
  only suggests this stage; the step itself is driven by DHX8, so RBM41's participation is not
  established.

### For transfer to SF2 orthologs
Experimentally established in human: U12/U6atac snRNA binding (in vitro and in cells), U12 snRNP
and U12-type spliceosome association, Cajal body localisation, a modest role in U12-type intron
splicing. Inferred only: the post-catalytic step and any function of the N-terminal region beyond
DHX8 association.
