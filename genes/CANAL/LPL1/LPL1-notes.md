# LPL1 (Candida albicans, Q5AMS2 / orf19.12043) notes

## 2026-10-01 re-review after GOA refresh

GOA was refreshed from remote. The following previously reviewed rows are no longer present in the
current GOA snapshot and were marked `retired: true` (reviews kept for provenance; retirement is not
a biological REMOVE judgment):

- GO:0047372 monoacylglycerol lipase activity | IBA | GO_REF:0000033 (was REMOVE as a ROG1-branch
  wrong-subfamily transfer via PANTHER:PTN000773837|SGD:S000003112; the current GOA no longer carries it,
  consistent with the OpenScientist report's subfamily analysis)
- GO:0016020 membrane | IEA | GO_REF:0000043
- GO:0016042 lipid catabolic process | IEA | GO_REF:0000043 (still used in core_functions as a
  process the phospholipase B activity directly carries out)
- GO:0016787 hydrolase activity | IEA | GO_REF:0000043

New GOA rows reviewed:
- GO:0120559 phosphatidylethanolamine lysophospholipase A1 activity (IBA, PTN000280739 / yeast LPL1) -> ACCEPT
- GO:0005737 cytoplasm (IBA, PTN000967933) -> KEEP_AS_NON_CORE (lipid droplet is the informative location)
- ND root rows GO:0003674 / GO:0005575 / GO:0008150 (GO_REF:0000015) -> KEEP_AS_NON_CORE (no C. albicans
  experimental data; not a functional claim)

Flag: the sister row GO:0004622 phosphatidylcholine lysophospholipase A1 activity (IBA) was previously
MODIFY'd to GO:0102545 B-type glycerophospholipase activity; left unchanged (granularity choice), though
the lysophospholipase A1 activity is a genuine component of Lpl1's PLB activity [PMID:25014274 "acting on
all glycerophospholipids primarily at sn-2 position and later at sn-1 position"].

Note: the retired GO:0047372 row (and the `file:CANAL/LPL1/LPL1-goa.tsv` reference finding) quote the GOA
line `GO:0047372 ... PANTHER:PTN000773837|SGD:S000003112` that was verbatim in the pre-refresh goa.tsv;
that line is absent from the refreshed file, which is exactly why the row was retired. The quote is kept
as historical provenance. Also re-anchored the deep-research PLB quotes to verbatim substrings.
