# PA1242 (SprP, Q9I496) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I496 --alias PA1242`; accession matches the worklist. No
deep-research provider was used. Both SprP papers are cached with full text (PMC4618607, PMC3937732).

### Literature

- [PMID:24376018 "SprP variant S499A which had the catalytic serine replaced by alanine also did not show protease activity"]
  Catalytic triad E262, H299, S499 (Glu in place of the usual Asp, which explains the UniProt CAUTION
  on missing conserved residues).
- [PMID:26175208 "Our results confirm the classification of SprP as a serine protease"]; purified
  SprP hydrolyses resorufin-casein, inhibited by AEBSF and TPCK, not by E-64, pepstatin A or EDTA;
  [PMID:26175208 "SprP is autocatalytically activated by proteolysis"].
- Deletion mutant: [PMID:24376018 "Examination of P. aeruginosa ΔsprP for its swimming, swarming, and twitching motility revealed that all three types of motility were virtually abolished"];
  biofilm sixfold up, pyoverdine fivefold up, both complemented; 218 genes changed in the transcriptome.

### Annotation decisions

- GO:0004252 (IBA, IDA seed, IEA), GO:0006508 (IBA, IEA): ACCEPT.
- GO:0008233 (IDA), GO:0008236 (IEA): TOO_GENERAL (entailed by GO:0004252).
- Motility IMP rows (GO:0043107, GO:0071977, GO:0071978): MARK_AS_OVER_ANNOTATED; pleiotropic
  deletion phenotype, SprP is not motility machinery.
- GO:1900232 (IMP): KEEP_AS_NON_CORE. GO:1900377 (IMP): MODIFY to GO:1900705 negative regulation of
  siderophore biosynthetic process (pyoverdine was measured).
- Action counts: ACCEPT 5, TOO_GENERAL 2, MARK_AS_OVER_ANNOTATED 3, KEEP_AS_NON_CORE 1, MODIFY 1.
- No source defects.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002459139 | GO:0004252 serine-type endopeptidase activity | 3 | 90 (31 taxa) | GO:0004252, IDA, PMID:26175208 (PseudoCAP) | SOUND | Full text read; purified enzyme, casein substrate, serine-protease inhibitor profile, S499A inactive. Node term suits a subtilase clade. | B. subtilis AprE P04189, Plasmodium SUB1 Q8I430 | Yes |

The node's GO:0006508 proteolysis IBD (seeds P04189, P16396, Q8I430) is not seeded by PA1242.
