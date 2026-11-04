# nuoI (P0AFD6) notes

## 2026-10-23 review session

Deep-research providers are not available here (no API keys), so I reviewed
the literature by hand from cached publications/PMID_*.md and the UniProt
record.

- NuoI (TYKY/NDUFS8/Nqo9 homologue) binds two [4Fe-4S] clusters, N6a and N6b,
  which bridge N5 and N2 [PMID:22474289 "Subunit NuoI in the peripheral domain
  contains two [4Fe-4S] clusters (N6a and N6b) and plays a role in bridging the
  electron transfer from cluster N5 to the terminal cluster N2"]. The clusters
  are essential for electron transfer [PMID:22474289 "unequivocally affirmed
  that clusters N6a and N6b are essential for electron transfer of NDH-1"].
- NEW GO:0009055 electron transfer activity, as the core MF; this matches the
  module leaf function.
- The GO:0050136 IDA row (PMID:10587449) was MODIFIED to GO:0008137 rather
  than removed. The paper is about the proton-pumping enzyme, so its finding
  is sound but the term (now restricted to the non-electrogenic activity) is
  wrong. The IEA GO:0050136 row is removed.
- Iron ion binding is MODIFIED to 4Fe-4S cluster binding. Membrane is
  MODIFIED to plasma membrane, and NADH dehydrogenase complex to complex I.
  The GO:0003954/GO:0016651 rows are MODIFIED to contributes_to GO:0008137.
- Aerobic respiration (IBA, IMP PMID:9495756) is kept as non-core context.
  The nuoI::Km allele is polar.
- Validation: 0 warnings and 0 errors (with UV_NATIVE_TLS unset).
