# dsbB2 curation notes

## Evidence boundary and GO direction

The KT2440 DsbB2 function and localization statements are explicitly marked
"By similarity" and the entry has protein-existence level 3. The review
therefore describes this paralog as predicted rather than directly assayed
[file:genes/PSEPK/dsbB2/dsbB2-uniprot.txt, "Acts by oxidizing the DsbA protein
(By similarity)."].

The official GO definition for GO:0015035 is "Catalysis of the reaction: a
protein with reduced sulfide groups = a protein with oxidized disulfide bonds."
The equality is direction-neutral, but the GO:0015035 mapping is widened to
GO:0016672 because the quinone-coupled sulfur-donor oxidoreductase term captures
DsbB's membrane reaction more precisely. GO:0009055 electron transfer activity
is retained as a valid non-core description of the DsbA-to-quinone relay.

Canonical *E. coli* experiments show respiratory-chain-dependent DsbA oxidation
through DsbB [PMID:9342327] and direct DsbB-catalyzed oxidation of DsbA by
ubiquinone [PMID:12853466]. These studies ground the family mechanism; they do
not directly establish when or how the second KT2440 paralog is used.


## 2026-11-06 independent annotation audit

The original annotation payloads, including inherited NEW proposals, and frozen UniProt/GOA bytes were preserved. Every row and the core synthesis were reassessed. An initial provider-unspecified invocation was rejected by the CLI; the subsequent explicit Falcon request genuinely reached the provider and failed HTTP403 authentication. No provider report was written. The PAINT command completed, but this KT2440 accession is not a leaf of the available tree; its losses could not be checked. No absence of evolutionary loss is inferred from that result.

Official QuickGO defines GO:0015035 as “Catalysis of the reaction: a protein with reduced sulfide groups = a protein with oxidized disulfide bonds.” Its reversible equation includes physiological protein oxidation despite the reductase label. GO:0015035 is a descendant of GO:0015036 and GO:0016491. GO:0016672 instead specifies a sulfur-containing donor and quinone acceptor; it is not a descendant of GO:0015035 or GO:0009055. These are distinct specificity axes, not interchangeable granularity levels. Definitions and is_a/part_of ancestor responses were saved in the ignored original-five audit cache from https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015035 and corresponding term/ancestors endpoints.

The exact target is P59344, Pseudomonas putida KT2440, with locus PP_0190. PMID:24327342 uses P. aeruginosa PA14 and is comparative evidence, not a KT2440 experiment. No equivalence of numbered paralogs, substrate list, physiological redundancy, or quantitative catalytic rates is inferred from matching symbols.

The reviewed sequence belongs to the DsbB family, carries the HAMAP MF_00286 signature, and has four membrane helices plus two conserved redox cysteine pairs. These independent features support transfer of the sulfur-donor/quinone-acceptor catalytic mechanism [PMID:12853466; PMID:24327342: “both PaDsbB1 and PaDsbB2 shuttle electrons from PaDsbA1 to membrane-bound quinones.”]. A NEW IC GO:0016672 records this inferred MF because the five historical rows contain no GO:0016491/GO:0016667 ancestor to refine, and GO:0015035 and GO:0009055 are not its ancestors or descendants. This is not a new process assertion or a target-specific enzyme assay. The proposed native roles of the two KT2440 paralogs remain unresolved.

Current action counts: {"ACCEPT": 4, "MODIFY": 1, "NEW": 1}.
