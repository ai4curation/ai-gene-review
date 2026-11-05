# nasA: native Bacillus subtilis nitrogen metabolism

## Review completed 2026-10-29

NasA is a multipass plasma-membrane nitrate transporter of Bacillus subtilis 168. It supplies nitrate to the assimilatory NasBC nitrate-reductase system. Native mutant physiology supports nitrate uptake, while an additional nitrite-transport activity and the coupling mechanism remain unresolved.

The target is UniProt P42432, B. subtilis 168. Native experiments use JH642 and derivatives; these are distinguished from purified enzymes of Klebsiella or cyanobacteria. The mechanistic evidence and access record are collected in [native-nas-system.md](../nasB/nasB-source-analysis/native-nas-system.md).

PMID:7868621 was read in the publisher PDF, although its canonical cache remains abstract-only. PMID:9765565 was normally fetched as full text and supplies direct NasDE activity, controlled subunit-deletion and fractionation experiments. PMID:10542156 is the same article as the full PMC URL cache used for exact mechanistic quotes; it is counted as one paper. PMID:24467397 was read only for the relevant Nas section and is background, not native donor evidence.

- GO:0005886 plasma membrane: **ACCEPT**. Native nitrate-use genetics, the hydrophobic multipass sequence and curated membrane localization support this inherited location. No target-specific loss of the membrane function is indicated.

- GO:0005886 plasma membrane: **ACCEPT**. The curated cell-membrane location agrees with the multipass transporter architecture and native uptake phenotype.

- GO:0015112 nitrate transmembrane transporter activity: **ACCEPT**. The nitrate-selective growth defect despite retained nitrate-reducing capacity supports a transport step. Native evidence corroborates the phylogenetic nitrate-porter assignment; transport kinetics and coupling stoichiometry were not measured.

- GO:0015112 nitrate transmembrane transporter activity: **ACCEPT**. NasA is an MFS nitrate/nitrite-porter family member whose nitrate uptake role is supported by the native mutant phenotype.

- GO:0015113 nitrite transmembrane transporter activity: **UNDECIDED**. Family membership can encompass nitrate and nitrite substrates, but the native growth experiments establish nitrate uptake. Retained nitrite growth does not exclude redundant nitrite transport, so neither a definite nitrite assignment nor its absence is justified.

- GO:0015706 nitrate transmembrane transport: **ACCEPT**. Transport is the step supported by the membrane architecture and nitrate-use phenotype; NasA is not the nitrate-reducing enzyme.

- GO:0015706 nitrate transmembrane transport: **ACCEPT**. The automated transport assignment agrees with native genetics and the independently curated transporter-family placement.

- GO:0015707 nitrite transport: **UNDECIDED**. This is the same substrate-specific claim as the nitrite transporter row. A shared nitrate/nitrite-porter domain does not establish which additional substrate the native NasA protein transports.

- GO:0016020 membrane: **MODIFY**. NasA is a multipass bacterial cell-membrane transporter; the already represented plasma-membrane term captures this location more precisely.

- GO:0022857 transmembrane transporter activity: **MODIFY**. Native physiology resolves the generic transporter activity to nitrate transmembrane transporter activity, already present in this review. Nitrite specificity remains unresolved.

- GO:0055085 transmembrane transport: **MODIFY**. The nitrate uptake step is more informative than substrate-unspecified transmembrane transport and is already represented.

No isolated-subunit catalytic claim is inferred from the ordinary machine relationship value. The native complex contribution is assessed on biology. All seeded rows and machine payloads remain intact; no redundant NEW row was introduced. Nitrogen-regulator induction is regulation of these enzymes, not a transcription-factor function of the enzymes. Provider authentication failures are recorded in the foundation; no provider report was invented.
