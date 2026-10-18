# ARMCX2 (ALEX2) review notes

## Sources
- Affinage: trust gates clear. Its trafficking statement rests on a family review (PMID:33267763), not on ARMCX2 data.
- PubMed "ARMCX2" (2026-10-04) returns 10 records: expression, prognosis-signature and methylation papers, and one mouse testis expression study (PMID:15759267). None tests ARMCX2 mitochondrial function. "ALEX2" also matches an unrelated allergy array.
- ISS donors (QuickGO):
  - Mouse Armcx2 (Q6A058), the ortholog: EXP mitochondrion (PMID:22569362).
  - Mouse Armcx3 (Q8BHS6), a paralog: IDA/EXP outer membrane (PMID:19304657, PMID:22569362).
- The IBA rows use node PTN001038987 (the ARMC10/ARMCX node). The axonal-transport IBA is seeded only by Armcx3.

## Decisions
- ACCEPT:
  - Mitochondrion (IBA, IEA, HTP, ISS) and mitochondrial outer membrane (IEA, ISS from the Armcx3 paralog, justified by the shared TM anchor).
  - Axonal transport of mitochondrion (IBA): an inherited family role with no evidence of loss.
- KEEP_AS_NON_CORE: axon cytoplasm.
