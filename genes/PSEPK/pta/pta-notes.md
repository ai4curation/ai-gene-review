# PSEPK pta follow-up,2026-11-06

Baseline frozen before mutation in `.cache/module-audit-logs/ethanolamine-20261106/pta-followup/baseline.json`: five original annotation rows, two raw sources and the genuine Falcon report plus its three artifacts. No seeded payload or raw/provider bytes changed.

GO0016407 and GO0016746 were incorrectly marked over-annotated solely because broad/redundant. QuickGO ancestry confirms GO0008959 descends from both. Both now MODIFY to the existing precise phosphate acetyltransferase activity; no family-wide catalytic claim is rejected. Frozen UniProt catalytic text and directly checked KT2440 assays support the correction.

The primary study underlying Falcon is PMID23149123 (Nikel and de Lorenzo,2013), normally fetched without refreshing any existing cache. An author-deposited CONICET PDF was acquired to ignored cache and read. Pages103–104 identify PP0774, demonstrate WT-versus-pta::mini-Tn5 phosphotransacetylase activity, report absence of acetate kinase in KT2440, and state that Pta physiological relevance remains uncertain. Page104 Figure3 explicitly uses introduced E. coli MG1655 AckA for acetate/ATP production. Small exact excerpts and acquisition hash are preserved under pta-source-analysis; the full PDF/text are not committed.

Consequently GO0006085 is UNDECIDED, not rejected: biochemical reversibility and a pathway map cannot alone establish native acetyl-CoA biosynthetic flux, but other sources of acetyl phosphate/reverse flux are not excluded. The duplicated core was consolidated to intrinsic GO0008959 with the native-versus-engineered boundary. Description and other row prose now distinguish direct assays from inference. No NEW rows, processes, or source-defect accusations were added.

Status remains DRAFT: this was a bounded correction and primary verification, not a comprehensive audit of every additional source in the existing Falcon report. In particular native reverse-flux physiology remains unresolved.
