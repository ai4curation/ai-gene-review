# lipM notes

Reviewed for the endogenous protein lipoylation module (modules/endogenous_protein_lipoylation.yaml).

## Literature sources

No deep-research provider is configured in this session (no provider API key), so no
`-deep-research-*.md` file was generated. Sources: UniProt record and cached full texts
PMID:20882995 (LipM discovery), PMID:21338420 and PMID:21338421 (companion papers defining
the LipM-GcvH-LipL relay).

## Summary

- LipM octanoylates GcvH from octanoyl-ACP (Cys150 thioester) and has no lipoate ligase activity
  [PMID:20882995 "YqhM lacks lipoate ligase activity and instead has octanoyltransferase activity"].
- LipL transfers octanoyl from octanoyl-GcvH to E2 domains (EC 2.3.1.204, RHEA:20213)
  [PMID:21338421 "LipL represents a new enzyme activity."].
- LipM and LipL are both in PANTHER PTHR43679:SF2 and share PAINT node PTN008684097, which
  assigns GO:0033819 (octanoyl-ACP donor) to both; correct for LipM, not for LipL.
- GO has no term for the LipL reaction; a proposed new term is recorded in the lipL review.
