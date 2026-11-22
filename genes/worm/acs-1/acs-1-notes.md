# acs-1 review notes

## Session 2026-10-28

- `just fetch-gene worm acs-1` resolved UniProt Q5TKA3 (GeneID 179043, WBGene00018488), as expected.
  The GOA file keyed to Q5TKA3 has a single row: GO:0031956 medium-chain fatty acid-CoA ligase
  activity, IEA via EC:6.2.1.2 (GO_REF:0000003). The EC number itself comes from an ARBA rule
  (UniProt DE line `EC=6.2.1.2 {ECO:0000256|ARBA:ARBA00039009}`).
- No WormBase experimental rows are keyed to Q5TKA3 in this GOA download.
- `just fetch-gene-pmids` found no PMIDs (only GO_REF). Cached PMID:15340492 (key paper, full text),
  PMID:18676815 (full text), PMID:22426533 (abstract only), PMID:34623380 (full text),
  PMID:21704635 (full text), PMID:23705068 and PMID:24086720 (full text, background).
- Literature summary in `acs-1-deep-research-manual.md`.

## Decision on GO:0031956

- The activity class (fatty acid-CoA ligase) is well supported by family (ANL superfamily, ACSF2
  subfamily, AMP-binding signature) and by genetic data showing ACS-1 is needed to make and use
  C15ISO/C17ISO [PMID:18676815 "plays an essential role in mmBCFA biosynthesis and activation"].
- The medium-chain specificity is only inherited from the ARBA name/EC of the ACSF2 subfamily. The
  worm genetic data point instead to C13-C17 iso-branched (long-chain) substrates, and the
  original authors called it a very-long-chain ACS homolog [PMID:15340492]. No assay of substrate
  preference exists. So: MODIFY to GO:0120515 fatty acid-CoA ligase activity (parent of
  GO:0031956), rather than REMOVE.

## NEW terms considered

- GO:1902321 methyl-branched fatty acid biosynthetic process: ACS-1 plausibly performs a catalytic
  step (acyl-CoA formation) in mmBCFA synthesis, but the only evidence is RNAi FA profiles plus
  family membership; no biochemical demonstration of which step. Per the NEW bar, not added as an
  annotation; recorded as the core-function process with the caveat and as a suggested question.
- Embryonic development, lipid droplet growth, ER integrity, IP3 signalling: downstream phenotypes
  of mmBCFA loss; not added.
- Mitochondrion: no worm evidence; not added.

## 2026-10-28 PR review fixes

Added a NEW GO:1902321 methyl-branched fatty acid biosynthetic process row (IMP, PMID:18676815) and restored it to core_functions directly_involved_in. Participation argument: ACS-1 forms the acyl-CoA thioester, a chemical step in mmBCFA synthesis; comparator elo-6 carries the same term by IMP from PMID:15340492. The exact step and substrate are not biochemically established.

## 2026-10-28 PR review fix: GO:1902321 support

Removed the two PMID:15340492 quotes from the supported_by of the NEW GO:1902321 row. They describe elo-5/elo-6 RNAi, not acs-1, so they do not support the row; the elo-6 comparator argument stays in the row's reason. The row is supported by the two PMID:18676815 acs-1 quotes.
