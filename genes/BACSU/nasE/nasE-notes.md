# nasE: native Bacillus subtilis nitrogen metabolism

## Review completed 2026-10-29

NasE is the small Rieske-like subunit of the cytosolic Bacillus subtilis 168 NasDE nitrite reductase. It is required with NasD for NADH-preferring reduction of nitrite to ammonium and is predicted to bind a 2Fe-2S cluster. The assembled enzyme supports both nitrogen assimilation and anaerobic nitrite reduction; NasE is not independently established as a nitrite-reducing catalyst.

The target is UniProt P42436, B. subtilis 168. Native experiments use JH642 and derivatives; these are distinguished from purified enzymes of Klebsiella or cyanobacteria. The mechanistic evidence and access record are collected in [native-nas-system.md](../nasB/nasB-source-analysis/native-nas-system.md).

PMID:7868621 was read in the publisher PDF, although its canonical cache remains abstract-only. PMID:9765565 was normally fetched as full text and supplies direct NasDE activity, controlled subunit-deletion and fractionation experiments. PMID:10542156 is the same article as the full PMC URL cache used for exact mechanistic quotes; it is counted as one paper. PMID:24467397 was read only for the relevant Nas section and is background, not native donor evidence.

- GO:0005737 cytoplasm: **MODIFY**. The primary fractionation experiment resolves the broad cytoplasm annotation to cytosol: nearly all native NasDE activity partitioned there, with none in the membrane fraction.

- GO:0008942 nitrite reductase [NAD(P)H] activity: **MODIFY**. Native NasDE strongly favors NADH but also exhibits NADPH-dependent activity below 10% of the NADH activity. Resolve the combined term to both supported donor-specific activities; the minor NADPH reaction does not imply equal physiological importance. NasE is a required complex subunit; this does not assert an isolated NasE active site.

- GO:0051537 2 iron, 2 sulfur cluster binding: **ACCEPT**. The phylogenetic cofactor assignment agrees with the target Rieske domain, predicted ligand positions and curated 2Fe-2S cofactor. No target-specific loss is indicated. Cluster occupancy and a particular electron-transfer sequence were not directly measured in the native activity study.

- GO:0051537 2 iron, 2 sulfur cluster binding: **ACCEPT**. The target conserved domain and ligand features support the same cofactor assignment as the phylogenetic row. It remains a comparative structural inference rather than a native spectroscopic measurement.

- GO:0106316 nitrite reductase (NADH) activity: **ACCEPT**. Native cell-extract assays and controlled subunit deletions demonstrate the requirement for NasE in the NADH-driven enzyme. The full reaction is assigned to the assembled NasDE system, not isolated NasE. The same enzyme serves assimilatory and anaerobic nitrite reduction.

No isolated-subunit catalytic claim is inferred from the ordinary machine relationship value. The native complex contribution is assessed on biology. All seeded rows and machine payloads remain intact; no redundant NEW row was introduced. Nitrogen-regulator induction is regulation of these enzymes, not a transcription-factor function of the enzymes. Provider authentication failures are recorded in the foundation; no provider report was invented.
