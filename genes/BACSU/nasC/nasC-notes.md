# nasC: native Bacillus subtilis nitrogen metabolism

## Review completed 2026-10-29

NasC is the molybdenum-containing catalytic component of the Bacillus subtilis 168 assimilatory nitrate reductase NasBC. It uses a bis-molybdopterin guanine dinucleotide cofactor and an iron-sulfur center to reduce nitrate to nitrite, receiving reducing equivalents through NasB. The nitrite can then be reduced to ammonium by NasDE for nitrogen assimilation.

The target is UniProt P42434, B. subtilis 168. Native experiments use JH642 and derivatives; these are distinguished from purified enzymes of Klebsiella or cyanobacteria. The mechanistic evidence and access record are collected in [native-nas-system.md](../nasB/nasB-source-analysis/native-nas-system.md).

PMID:7868621 was read in the publisher PDF, although its canonical cache remains abstract-only. PMID:9765565 was normally fetched as full text and supplies direct NasDE activity, controlled subunit-deletion and fractionation experiments. PMID:10542156 is the same article as the full PMC URL cache used for exact mechanistic quotes; it is counted as one paper. PMID:24467397 was read only for the relevant Nas section and is background, not native donor evidence.

- GO:0016491 oxidoreductase activity: **MODIFY**. The molybdenum-containing catalytic component performs the nitrate-to-nitrite step, with NasB supplying electron transfer. Nitrate reductase activity is the supported specific replacement for generic oxidoreductase activity; donor-specific kinetics were not established by the native methyl-viologen assay.

- GO:0019333 denitrification pathway: **MODIFY**. GO:0019333 requires the denitrification pathway ending in dinitrogen. Native NasBC supplies nitrite for assimilatory reduction to ammonium. The UniPathway denitrification mapping confuses a shared nitrate-reduction reaction with its physiological pathway; nitrate assimilation is the supported process.

- GO:0043546 molybdopterin cofactor binding: **ACCEPT**. The target molybdopterin-containing oxidoreductase family, cofactor annotation and native catalytic-subunit assignment agree. The binding term accommodates the bis-MGD form.

- GO:0051539 4 iron, 4 sulfur cluster binding: **ACCEPT**. A target PROSITE-supported 4Fe-4S domain with conserved ligand features and curated cofactor annotation supports this center adjacent to the molybdenum catalytic region.

No isolated-subunit catalytic claim is inferred from the ordinary machine relationship value. The native complex contribution is assessed on biology. All seeded rows and machine payloads remain intact; no redundant NEW row was introduced. Nitrogen-regulator induction is regulation of these enzymes, not a transcription-factor function of the enzymes. Provider authentication failures are recorded in the foundation; no provider report was invented.
