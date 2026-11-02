# AVPI1 notes

## 2026-10-05 review (PAINT, affinage)

- The only functional paper is PMID:12356727 (full text fetched from PMC129031 in revision 1). Its functional and MAPK assays all use mouse VIT32 cRNA in Xenopus oocytes [PMID:12356727 "As shown in Figure 6 A, progesterone induces a time-dependent increase in the phosphorylation of ERK2 (lanes 4–6). mVIT32 had a similar effect at 12 h (lane 9), but not at 6 h (lane 8)."]. The only mammalian-cell data are vasopressin induction of the transcript in mpkCCD cells.
- The MAPK IBA traces to MGI's IDA on mouse Avpi1 (GO API, 2026-10-05: GO:0043410 IDA plus IBA). Both sources are marked SOURCE_WEAK_OR_INFERRED, and the row is kept as non-core.
- All 33 GO:0005515 rows come from Y2H screens (mostly KRTAPs and MDFI) and are removed under policy.
- AVPI1 has no OpenCell line. HPA calls it nucleoplasm and plasma membrane, but no GOA rows exist for either, and no NEW is added.
- core_functions is left empty, because no endogenous function is known. This is recorded as a WHOLLY_DARK knowledge gap.

## 2026-10-05 revision (reviewer round 1)

- Fetched the PMC full text of PMID:12356727. The MAPK data are mouse VIT32 cRNA in Xenopus oocytes [PMID:12356727 "As shown in Figure 6 A, progesterone induces a time-dependent increase in the phosphorylation of ERK2 (lanes 4–6). mVIT32 had a similar effect at 12 h (lane 9), but not at 6 h (lane 8)."], and kidney cells remain untested [PMID:12356727 "It is now important to test this novel regulatory cascade in kidney cells experimentally, either in vitro or in vivo ."]. The SOURCE_WEAK_OR_INFERRED comments now cite this.

## 2026-10-05 revision (reviewer round 2)

- The description now attributes the oocyte experiments to mouse VIT32, and says the human protein is untested.
- ENaC: no NEW term (for example negative regulation of sodium ion transmembrane transport) is proposed. The only evidence is co-injection into oocytes, the channel itself does the transporting, and no human or endogenous data exist.
