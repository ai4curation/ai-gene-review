# Hsp83 notes

## 2026-09-28 IBA re-review

Re-reviewed all Hsp83 rows for the DROME IBA campaign, with emphasis on the ten PAINT/IBA rows.

### Cached literature read

- Read the complete cached full text for PMID:23509070. The Sicily paper directly supports the cytosolic client-stabilization framing: Sicily binds cytosolic Hsp90 and chaperones ND42 before mitochondrial import, and Sicily loss reduces ND42/NDUFS3 abundance.
- Read the complete cached full text for PMID:22902557. Hsp83 localizes to nurse-cell cytoplasm with a perinuclear rim in the piRNA biogenesis context; AGO3-positive foci after piRNA-factor knockdown support a contextual perinuclear/nuage-associated Hsp83 pool rather than a general constitutive compartment switch.
- Re-read the cached abstracts for the main Hsp83 GOA papers that currently lack cached full text, including PMID:29775584, PMID:30193096, PMID:30245208, PMID:33176138, PMID:22579285, PMID:22099462, PMID:31907206, PMID:10716925, PMID:19101615, PMID:18344983, and PMID:16595740.

### IBA decisions

- PANTHER PTHR11528 currently places Hsp83 below PTN000163527 for the ATP binding, ATP hydrolysis, and protein folding IBDs, and below PTN000163629 for the cytosol, plasma membrane, perinuclear cytoplasm, heat-response, protein-stabilization, and protein-complex IBDs.
- The conserved core IBA rows were retained for protein folding, ATP hydrolysis, ATP binding, cytosol, protein stabilization, and cellular response to heat.
- The plasma-membrane and perinuclear-cytoplasm IBA rows were kept as non-core. Drosophila has independent evidence for both, but they describe specific pools of a predominantly cytosolic Hsp90 chaperone.
- The matching HDA plasma-membrane and IDA perinuclear-cytoplasm rows were also harmonized to `KEEP_AS_NON_CORE`, accepting the observations while keeping Hsp83's primary location cytosolic.
- The generic `GO:0032991 protein-containing complex` IBA was marked over-annotated: Hsp83 genuinely forms dimers and client/co-chaperone assemblies, but `GO:0101031 protein folding chaperone complex` is the informative cellular-component term already present in the review.
- The stale `GO:0051082 unfolded protein binding` IBA remains a `MODIFY` to `GO:0140662 ATP-dependent protein folding chaperone`. The current PAINT extract no longer carries `GO:0051082`, but that is an ontology/staleness issue, not evidence of Hsp83-specific loss.

### Protein-binding cleanup

Migrated two legacy generic `GO:0005515 protein binding` rows from `MARK_AS_OVER_ANNOTATED` to `MODIFY -> GO:0140662`, and removed the Morgana row:

- PMID:22579285: Hsp90/Nelf-E interaction is part of NELF stabilization.
- PMID:31907206: Morgana/CHORD co-purifies with the Hsp90-R2TP-TTT supercomplex, supporting complex association but not Hsp83 foldase activity on Morgana as a client.
- PMID:23509070: Hsp90 binds Sicily and, Sicily-dependently, the CI subunit ND42.

### New-publication search

Searched PubMed/web for direct Hsp83/Hsp90 Drosophila literature from 2024-2026. Two new direct papers were cached:

- PMID:41701796 (2026, full cached): Hsp83 buffers behavioral variability by regulating `Pdf` transcription in clock neurons. This adds a direct modern neural/circadian client context but does not change the conserved IBA calls.
- PMID:42773879 (2026, abstract-only cached): HSF supports developmental growth by maintaining basal HSP83/HSP90. This reinforces constitutive developmental Hsp83 expression rather than replacing any existing GOA term.
