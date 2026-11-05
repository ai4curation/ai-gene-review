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


## 2026-10-30 PR5740 follow-up: donor attribution

The earlier two-donor replacement rationale is superseded. PMID:9765565 reports: “Activity with NADPH was less than 10% of that with NADH.” This was a crude-extract signal, unlike a purified enzyme donor comparison. The assay does not separate direct NasDE NADPH turnover from possible transhydrogenase-mediated electron transfer or other extract activities; these are unresolved alternatives, not demonstrated mechanisms. Every affected MODIFY now proposes only GO:0106316, the established main NADH activity. The minor observation is preserved verbatim and raised as a question requiring purified-enzyme attribution. No primary quote, machine annotation field or raw record is changed.

A single IC NEW GO:0042128 proposal is added after reconsidering participation, not merely to mirror the core summary. NasE contributes to the enzyme executing nitrite reduction: native deletion with downstream-expression controls eliminates activity and assimilatory growth, and the sequence/cofactor assignment identifies an enzyme component. PMID:9765565 explicitly concludes that “the nasD and the nasE genes encode subunits of assimilatory nitrite reductase.” This is stronger than an unlocalized necessity phenotype or a substrate relationship.

The exact-term QuickGO comparator query returned zero GO:0042128 annotations for each same-role small-subunit comparator: ECOLI NirD P0A9I8, PSEPK NirD Q88M68 and MYCS2 MSMEG_0428 A0QPK3. This negative result is retained and cautions against manufacturing a proposal from absence alone. BACSU NasB P42433, a noncatalytic electron-transfer component of the same assimilatory pathway, has the term. The proposed NasE claim rests on its native functional evidence, not on claiming that all homologs carry the annotation.

The current GO definition encompasses nitrate uptake, reduction to ammonia and incorporation of nitrate-derived nitrogen into cellular substances. Its retrieved ancestors include nitrate metabolic process, nutrient assimilation and nitrogen cycle metabolic process; no restriction to independently catalytic subunits is stated. The existing NasE rows contain no biological-process ancestor or descendant, and the cached GO-CAM index has no P42436 entry. The module already represents NasE as a required enzyme component; this proposal does not introduce a separate pathway or a new molecular activity. Query responses and the zero-hit GO-CAM result are preserved in the ignored nitrate-bacsu-pr5740-followup log. The earlier no-NEW scope statement is superseded only for this evidence-backed process proposal.
