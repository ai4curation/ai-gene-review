# nasB: native Bacillus subtilis nitrogen metabolism

## Review completed 2026-10-29

NasB is the flavin-containing electron-transfer component of the Bacillus subtilis 168 assimilatory nitrate reductase NasBC. Its dinucleotide-binding and iron-sulfur regions deliver reducing equivalents to the molybdenum-containing catalytic subunit NasC, enabling nitrate reduction to nitrite. The system is described as NADH dependent. NasB is related to nitrite-reductase large subunits but lacks the characteristic siroheme-associated motif and functions in nitrate assimilation.

The target is UniProt P42433, B. subtilis 168. Native experiments use JH642 and derivatives; these are distinguished from purified enzymes of Klebsiella or cyanobacteria. The mechanistic evidence and access record are collected in [native-nas-system.md](../nasB/nasB-source-analysis/native-nas-system.md).

PMID:7868621 was read in the publisher PDF, although its canonical cache remains abstract-only. PMID:9765565 was normally fetched as full text and supplies direct NasDE activity, controlled subunit-deletion and fractionation experiments. PMID:10542156 is the same article as the full PMC URL cache used for exact mechanistic quotes; it is counted as one paper. PMID:24467397 was read only for the relevant Nas section and is background, not native donor evidence.

- GO:0016491 oxidoreductase activity: **MODIFY**. The generic oxidoreductase claim can be resolved to its contribution to nitrate reductase activity. NasC supplies the molybdenum catalytic site; NasB is a required electron-transfer component, not an independently demonstrated nitrate catalyst.

- GO:0020037 heme binding: **REMOVE**. The native primary sequence analysis distinguishes NasB from NasD by the absence of the conserved siroheme-associated motif. Together with its nitrate-reductase electron-transfer role, this argues against transferring heme binding from the broad nitrite/sulfite-reductase domain IPR006067. This is a target-specific motif and function conflict, not rejection based on a name.

- GO:0042128 nitrate assimilation: **ACCEPT**. NasB supplies reducing equivalents to NasC in the assimilatory nitrate-reduction step. Native genetics distinguish this system from respiratory NarGHJI.

- GO:0050660 flavin adenine dinucleotide binding: **ACCEPT**. The native sequence-derived diaphorase assignment and curated FAD cofactor annotation support flavin binding. An exact native cofactor stoichiometry is not claimed.

- GO:0050661 NADP binding: **UNDECIDED**. The domain mapping identifies a dinucleotide-binding family, whereas the mechanistic review describes NADH use. Native nitrate assays used methyl viologen and do not settle NADPH utilization or NADP binding; unlike NasD, NasB lacks a target-specific NADP ligand annotation. NADH use alone does not exclude NADP binding.

- GO:0051536 iron-sulfur cluster binding: **MODIFY**. The target cofactor annotation and BFD-like domain provide a more specific iron-sulfur assignment than the generic cluster term. This is a comparative ligand assignment, not a measurement of native cluster number.

- GO:0098809 nitrite reductase activity: **REMOVE**. Native experiments assign nitrite reduction to NasDE and nitrate assimilation to NasBC. NasB lacks the siroheme-associated motif characteristic of the catalytic nitrite-reductase region. The IPR012744 family-level substrate mapping is therefore inappropriate for this specialized member; this decision does not depend on independent-subunit catalysis.

No isolated-subunit catalytic claim is inferred from the ordinary machine relationship value. The native complex contribution is assessed on biology. All seeded rows and machine payloads remain intact; no redundant NEW row was introduced. Nitrogen-regulator induction is regulation of these enzymes, not a transcription-factor function of the enzymes. Provider authentication failures are recorded in the foundation; no provider report was invented.
