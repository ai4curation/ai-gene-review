# ARMCX1 (ALEX1) review notes

## Sources
- Affinage: trust gates clear. Checked against:
  - PMID:28009275 (mouse Armcx1, full text): mitochondrial; enhances RGC mitochondrial transport.
  - PMID:22569362 (abstract): Armcx family is mitochondrial and derived from Armc10; Armcx3 binds Kinesin/Miro/Trak2.
- Mouse Armcx1 (Q9CX83, MGI:1925498) donor rows (QuickGO): EXP mitochondrion (PMID:28009275, PMID:22569362).
- The IBA rows use node PTN001038987, the same ARMC10/ARMCX node as in the ARMC10 review. The axonal-transport IBA is seeded only by Armcx3.

## Decisions
- ACCEPT:
  - Mitochondrion (IBA, IEA, IDA, ISS) and mitochondrial outer membrane (IEA, ISS).
  - Axonal transport of mitochondrion (IBA).
- KEEP_AS_NON_CORE: axon cytoplasm (IEA derived from the process).
- REMOVE: 8 generic protein-binding rows (policy).
- No NEW. The FBXW7/TRIM21 substrate-recruitment claims come from single cancer cell-line studies (PMID:39285446 and a 2026 study), so they are raised as a question.
