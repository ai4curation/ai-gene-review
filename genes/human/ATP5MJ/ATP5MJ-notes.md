# ATP5MJ notes

## 2026-10-05 review (PAINT, affinage)

- Subunit j (MLQ, 6.8-kDa proteolipid) [PMID:24330338 "Here, we show that MLQ-knockdown HeLa cells lose population of ATP synthase in mitochondria."].
- All 14 GOA rows (complex, location, ATP synthesis) are accepted.
- NEW contributes_to GO:0046933 (IDA, PMID:37244256 structure). Comparator check: ATP5ME, ATP5MF, ATP5MG and ATP5PD carry it as contributes_to by IBA and IDA; ATP5MK does not. GO:0042776 was not added, because it is a descendant of the GO:0015986 the gene already carries.
- Knowledge gap: how subunit j maintains ATP synthase levels (assembly vs. stability).

## 2026-10-05 revision (reviewer round 1)

- Withdrew the NEW contributes_to GO:0046933 row. The cited structure abstract never mentions subunit j, UniProt made no rows for ATP5MJ from that paper (it made several for subunit c), and the knockdown shows reduced enzyme abundance, not impaired catalysis. contributes_to GO:0046933 now appears only in core_functions, alongside GO:0005198 structural molecule activity, matching the ATP5MD (subunit k) review.
- The comparator results, recorded exactly (QuickGO, 2026-10-05): contributes_to GO:0046933 by IBA and IDA on ATP5ME (e), ATP5MF (f), ATP5MG (g), ATP5PD (d) and ATP5F1E; absent on ATP5MK (k). The reviewer could not query QuickGO and doubted these rows; they do exist. Correction: ATP5PD (subunit d) is a peripheral-stalk subunit, not an F(o) accessory subunit as I wrote before.
