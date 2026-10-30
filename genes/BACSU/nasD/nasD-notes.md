# nasD: native Bacillus subtilis nitrogen metabolism

## Review completed 2026-10-29

NasD is the large catalytic subunit of the cytosolic Bacillus subtilis 168 NasDE nitrite reductase. Its flavin, iron-sulfur and siroheme cofactors support six-electron reduction of nitrite to ammonium. Native activity strongly favors NADH, with lower NADPH-dependent activity. Together with the required small subunit NasE, it supports nitrogen assimilation and anaerobic nitrite reduction downstream of respiratory nitrate metabolism.

The target is UniProt P42435, B. subtilis 168. Native experiments use JH642 and derivatives; these are distinguished from purified enzymes of Klebsiella or cyanobacteria. The mechanistic evidence and access record are collected in [native-nas-system.md](../nasB/nasB-source-analysis/native-nas-system.md).

PMID:7868621 was read in the publisher PDF, although its canonical cache remains abstract-only. PMID:9765565 was normally fetched as full text and supplies direct NasDE activity, controlled subunit-deletion and fractionation experiments. PMID:10542156 is the same article as the full PMC URL cache used for exact mechanistic quotes; it is counted as one paper. PMID:24467397 was read only for the relevant Nas section and is background, not native donor evidence.

- GO:0008942 nitrite reductase [NAD(P)H] activity: **MODIFY**. Native NasDE strongly favors NADH but also exhibits NADPH-dependent activity below 10% of the NADH activity. Resolve the combined term to both supported donor-specific activities; the minor NADPH reaction does not imply equal physiological importance. NasD supplies the flavin/siroheme catalytic machinery.

- GO:0016491 oxidoreductase activity: **MODIFY**. The generic redox term can be resolved to both donor-specific reactions measured for native NasDE, with NADH dominant and NADPH minor.

- GO:0020037 heme binding: **ACCEPT**. The conserved siroheme-associated ligand and curated cofactor assignment support the heme-family binding claim for the nitrite-reducing large subunit. This is the catalytic tetrapyrrole, not an inference of a respiratory cytochrome.

- GO:0042128 nitrate assimilation: **ACCEPT**. The native NasDE enzyme reduces nitrite to ammonium for biosynthesis. Its additional anaerobic role does not negate this directly demonstrated assimilatory function.

- GO:0050660 flavin adenine dinucleotide binding: **ACCEPT**. Native NADH-dependent chemistry and the target FAD cofactor/ligand assignments agree with the flavoprotein architecture.

- GO:0050661 NADP binding: **ACCEPT**. Native NasDE shows a minor NADPH-dependent reaction and NasD has a predicted NADP ligand-binding region. These support binding without implying NADPH is the dominant physiological donor.

- GO:0051536 iron-sulfur cluster binding: **MODIFY**. Curated target cofactor and ligand annotations distinguish two cluster types. The 4Fe-4S/siroheme region participates in nitrite reduction; the 2Fe-2S assignment is comparative. Both supported types refine generic cluster binding.

- GO:0098809 nitrite reductase activity: **MODIFY**. The unspecified nitrite-reductase term can be refined to the native NADH and minor NADPH activities. This system reduces nitrite to ammonium, rather than performing nitric-oxide-forming denitrification.

- GO:0106316 nitrite reductase (NADH) activity: **ACCEPT**. Native cell-extract assays and controlled subunit deletions demonstrate NasD involvement in the NADH-driven enzyme. The same enzyme serves assimilatory and anaerobic nitrite reduction.

No isolated-subunit catalytic claim is inferred from the ordinary machine relationship value. The native complex contribution is assessed on biology. All seeded rows and machine payloads remain intact; no redundant NEW row was introduced. Nitrogen-regulator induction is regulation of these enzymes, not a transcription-factor function of the enzymes. Provider authentication failures are recorded in the foundation; no provider report was invented.
