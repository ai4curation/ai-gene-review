# Lst8 (Q9W328) curation notes

Deep research: falcon run queued; earlier runs in this session took ~30 min and the wrapper reported
timeouts. Notes from cached publications.

## Literature journal

- Lst8 is in both complexes but acts only in TORC2 in flies
  [PMID:22493059 "Here, we demonstrate that Drosophila LST8, the  only conserved TOR-binding protein present in both TORC1 and TORC2, functions  exclusively in TORC2 and is not required for TORC1 activity."]
- TORC1 activity without Lst8
  [PMID:22493059 "In mutants lacking  LST8, expression of TOR and RAPTOR, together with their upstream activator Rheb,  was sufficient to provide TORC1 activity and stimulate cell and organ growth."]
- TORC2 growth via Myc
  [PMID:25999153 "Expression of Myc fully rescued growth defects associated with lst8 and rictor mutations, both of which encode essential components of TORC2."]
- GOLPH3 interaction
  [PMID:36435842 "The interaction of dGOLPH3 with Lst8 posits that dGOLPH3 might also regulate mTORC2 activity."]

## Curation decisions

- Core: TORC2 subunit; MF slot protein Ser/Thr kinase activator activity for consistency with Rictor and
  Sin1 (validator notes this MF is not among Lst8's GOA rows).
- TORC1: IDA physical membership kept non-core; NOT TORC1 signaling (IMP) accepted; positive TORC1
  signaling NAS removed as contradicted; NOT TORC1 complex (IMP) UNDECIDED because a mutant phenotype
  cannot establish absence from the complex and conflicts with the IDA row.
- protein binding: TOR partner -> protein kinase binding; GOLPH3 partner removed.
