# rheb-1 review notes

## Session 1 (create review)

- `just fetch-gene worm rheb-1` timed out repeatedly on the UniProt gene-symbol
  search (UniProt returned "Too Many Requests"); fetched with
  `--uniprot-id P34443` instead. Accession confirmed P34443 (RHEB1_CAEEL, F54C8.5).
- GOA: 12 rows, all IBA/IEA/ISS; no experimental worm rows. No PMIDs in GOA.
- Literature compiled by hand in `rheb-1-deep-research-manual.md` (no deep-research
  API keys).

### Key evidence
- Endogenous CRISPR-tagged RHEB-1 colocalizes with CTNS-1 (lysosomal membrane) and
  DAF-15/Raptor [PMID:32041790 "mK2::RHEB-1 also colocalized with CTNS-1::GFP"].
- GTP-locked rheb-1(Q71L Q72D) activates TORC1 in vivo [PMID:23705068 "a third TORC1-activating transgene, rheb-1Q71LQ72D"].
- Null = L3 arrest like TORC1 [PMID:32041790 "deletion of RHEB-1 similarly conferred L3 arrest"].

### Decisions
- GTPase activity / GTP binding: ACCEPT (family + nucleotide-state allele).
- Plasma membrane (IBA from broad Ras-family node; IEA from UniProt SubCell ECO:0000305):
  MARK_AS_OVER_ANNOTATED. Rheb proteins are endomembrane/lysosomal; worm endogenous
  RHEB-1 is lysosomal. Not REMOVE because farnesylated Rheb can visit other membranes.
- membrane (IEA): MODIFY -> lysosomal membrane.
- signal transduction: MODIFY -> positive regulation of TORC1 signaling.
- positive regulation of TOR signaling (ISS): MODIFY -> positive regulation of TORC1 signaling.
- NEW: lysosomal membrane (IDA, PMID:32041790). Two lines: farnesyl CAAX anchor and
  colocalization with a lysosomal-membrane marker.
- No NEW developmental / lifespan process terms: these are TORC1 downstream outcomes
  (necessity evidence, not participation).
