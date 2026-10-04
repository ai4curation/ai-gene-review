# ARPIN review notes

## Sources
- Affinage: trust gates clear. Checked against:
  - PMID:24132237 (Nature 2013, abstract): Arpin inhibits Arp2/3 and steers migration.
  - PMID:35110533 (cryo-EM, full text): Arpin binds only the Arp3 site.
  - PMID:27939292 (EM, full text): open, inactive conformation.
  - PMID:33923443 (full text): tankyrase binding through the acidic tail.
- The IBA node PTN001260652 is seeded by human ARPIN itself. The lamellipodium IEA/ISS rows come from mouse Arpin (Q9D0A3).
- Partners: TRIM27, NIF3L1 and DDIT4L (proteome-scale Y2H).

## Decisions
- ACCEPT:
  - Negative regulation of actin nucleation (IBA, IEA, IDA) and lamellipodium (IEA, ISS).
  - Negative regulation of cell migration and of lamellipodium morphogenesis (IMP).
- KEEP_AS_NON_CORE: directional locomotion. Arpin steers persistence; the negative regulation of migration row covers the core.
- REMOVE: 3 generic protein-binding rows.
- NEW: Arp2/3 complex binding (IDA, cryo-EM, PMID:35110533), the core MF.

## 2026-10-04 review round (PR #4205)

- GO:0051126 rows changed to GO:0034316. The comparators GMFG, GMFB and PICK1 carry GO:0034316.
- In endothelium, Arpin acts independently of Arp2/3 [PMID:39298260 "Arpin depletion in Human Umbilical Vein Endothelial Cells causes the formation of actomyosin stress fibers leading to increased permeability in an Arp2/3-independent manner."].
