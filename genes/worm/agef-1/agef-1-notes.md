# agef-1 review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene worm agef-1`; UniProt G5EFH7 (TrEMBL), 8 GOA rows, all IBA/IEA.
  No experimental GOA rows, and WormBase has not annotated the published mutant/RNAi work.
- Literature was read from cache: PMID:23840591 (GBF-1 paper, full text; compares agef-1 RNAi),
  PMID:25329472 (vh4 allele, full text), PMID:42312793 (epidermal AGEF-1/RAB-35, full text),
  PMID:42388253 (vh4 activating, microPub), PMID:22446376 and PMID:16672374 (abstract-only).
  See `agef-1-deep-research-manual.md` for quotes.
- Residue numbering checked against G5EFH7: E608 (Sec7 glutamic finger, used for the dominant
  negative in PMID:42312793), S784 (vd92, HDS1) and E1028 (vh4, PMID:42388253) all match the
  displayed sequence.
- GO:0005086 (ARF GEF activity) has been merged into GO:0005085, so GO:0005085 is the most specific
  available MF term.

### Decisions
- GEF activity (IBA, IEA): ACCEPT. Sec7 domain, catalytically dead E608K acts as dominant negative,
  human BIG2 rescues [PMID:42312793].
- trans-Golgi network (IBA): ACCEPT; Golgi apparatus (IEA, ARBA): ACCEPT (root organelle, claim holds
  by orthology plus trans-Golgi phenotypes [PMID:23840591]; no direct worm localization).
- membrane (IEA): MODIFY to trans-Golgi network membrane (GO:0032588): BIG-family GEFs are peripheral
  membrane proteins working on the TGN membrane.
- vesicle-mediated transport (IBA): MODIFY to Golgi to plasma membrane transport (GO:0006893):
  secretion defects and CAV-1 Golgi exit, with the Arf GEF doing the coat-recruitment step.
- regulation of ARF protein signal transduction (IEA): ACCEPT.
- perinuclear region of cytoplasm (IEA, SubCell): MARK_AS_OVER_ANNOTATED. The worm Golgi is
  dispersed mini-stacks and tagged AGEF-1 is in puncta throughout the cytoplasm.
- No NEW rows. Secretion, LET-23 EGFR negative regulation, lysosome size and axon integrity are
  mutant phenotypes downstream of trafficking (strict NEW bar). Raised as questions instead.
