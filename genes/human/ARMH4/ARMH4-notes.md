# ARMH4 (UT2) review notes

## Sources
- The affinage narrative (trust gates clear) misses the UT2-named literature:
  - PMID:25418727 (mouse UT2 binds and inhibits RICTOR/mTORC2; full text). This is the IDA donor for both mouse ISS rows (QuickGO Q8BT18).
  - PMID:26927669 (UT2 binds GP130 and inhibits pSTAT3; abstract only; UniProt curates it for human).
- Other sources:
  - PMID:36649229 (full text): kidney cells; membrane fraction; reduced IL-1B/IL-8.
  - PMID:41390521 (full text): IGF1R/FGFR1, aging.
- Partner: ELAPOR2 (A8MWY0, BioPlex).

## Decisions
- ACCEPT: membrane (IEA, IDA); TORC2 complex binding (ISS); the core MF.
- MODIFY:
  - Regulation of inflammatory response → negative regulation (GO:0050728).
  - Regulation of TORC2 signaling → negative regulation (GO:1903940).
- REMOVE: ELAPOR2 binding (policy).
- No NEW STAT3 process term: the species of the PMID:26927669 experiments is not stated in the cached abstract. It is raised as a suggested experiment.
