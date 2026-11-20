# cysE (P. aeruginosa PAO1, Q9HXI6, PA3816) curation notes

## 2026-11-03 review

- Deep research could not be generated: no provider API keys are available in
  this session. No `-deep-research-*.md` file was created.
- Key literature: PMID:42278617 (full text). It validates PA3816 as the major
  SAT ["In this work, we have identified and validated PA3816 as the major
  serine acetyltransferase"], shows deletion gives cysteine auxotrophy
  ["Deletion of cysE resulted in a marked cysteine auxotrophy under the
  conditions tested"], and shows no CysK regulation ["The results of the enzyme
  characterization in vitro suggest that PaCysE activity is not regulated by
  CysK"].
- PA2105 (Q9I210) is a second PTHR42811:SF5 paralog in PAO1; the paper notes
  ["PA2105 encodes a probable acetyltransferase and interestingly co-occurs
  with a probable cysteine synthase (PA2104)."] but it does not compensate for
  PA3816 loss.
- The UniProt record is unreviewed; its reaction and location lines are ARBA
  and were not cited.
- No GO:0009333 cysteine synthase complex is proposed: PaCysE lacks the
  C-terminal isoleucine anchor and shows no functional CysK interaction.
- Decisions follow the module sibling-consistency policy (cytoplasm MODIFY to
  cytosol; generic O-acetyltransferase parent TOO_GENERAL).

## 2026-11-03 PR #5929 review round

- Cytoplasm -> cytosol MODIFY reason now states that the refinement is an inference from solubility plus the PTHR42811 PAINT cytosol node, not a localization measurement.


## Comparative cysteine-route audit (2026-11-06)

All six original payloads/actions preserved. PMID42278617 distinguishes native PAO1 PA3816 deletion/complementation from Q9HXI6 codon-optimized N-terminal Strep-tagged protein expressed in E.coli BL21 Tuner. Reciprocal purified-enzyme kinetic assays show negligible effects of PaCysK and PaCysE on one another; the description and core now say precisely that, rather than proving no interaction in every native condition. The separate synthetic-tail result in PMID41676964 reinforces the noncanonical architecture. Missing terminal isoleucine and N-terminal helices are sequence/structural observations; the proposed assembly is not an experimentally solved native oligomer. PA2105 fails to compensate only under tested conditions.

Default Falcon research was attempted normally with --provider falcon and failed with HTTP403. No provider report was fabricated; this section records manual review.

Original GOA payloads, raw UniProt/GOA files and inherited authored proposals are preserved. Current GO checks distinguish the active cysteine synthase MF from obsolete route-specific BP terms GO:0006535 and GO:0019345. Focused gene and helper-history validations are recorded in the audit manifest.
