# dsbA curation notes

## Evidence boundary

The KT2440 entry is unreviewed and has protein-existence level 3. Its DsbA
identity, periplasmic localization, and active-site disulfide are computational
or homology-based, so the proposed protein-folding annotation uses ISS rather
than NAS [file:genes/PSEPK/dsbA/dsbA-uniprot.txt, "Belongs to the thioredoxin
family. DsbA subfamily."].

The catalytic mechanism is grounded separately in canonical *Escherichia coli*
experiments. Oxidized DsbA donates its active-site disulfide to cysteine pairs
in target proteins [PMID:9342327, "The Cys-30-Cys-33 disulfide is donated to a
pair of cysteines on the target proteins."]. This supports family-level
transfer of the oxidative-folding role without presenting the KT2440 protein as
directly assayed.


## 2026-11-06 independent annotation audit

The original annotation payloads, including inherited NEW proposals, and frozen UniProt/GOA bytes were preserved. Every row and the core synthesis were reassessed. An initial provider-unspecified invocation was rejected by the CLI; the subsequent explicit Falcon request genuinely reached the provider and failed HTTP403 authentication. No provider report was written. The PAINT command completed, but this KT2440 accession is not a leaf of the available tree; its losses could not be checked. No absence of evolutionary loss is inferred from that result.

Official QuickGO defines GO:0015035 as “Catalysis of the reaction: a protein with reduced sulfide groups = a protein with oxidized disulfide bonds.” Its reversible equation includes physiological protein oxidation despite the reductase label. GO:0015035 is a descendant of GO:0015036 and GO:0016491. GO:0016672 instead specifies a sulfur-containing donor and quinone acceptor; it is not a descendant of GO:0015035 or GO:0009055. These are distinct specificity axes, not interchangeable granularity levels. Definitions and is_a/part_of ancestor responses were saved in the ignored original-five audit cache from https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015035 and corresponding term/ancestors endpoints.

The exact target is Q88RK2, Pseudomonas putida KT2440, with locus PP_0127. PMID:24327342 uses P. aeruginosa PA14 and is comparative evidence, not a KT2440 experiment. No equivalence of numbered paralogs, substrate list, physiological redundancy, or quantitative catalytic rates is inferred from matching symbols.

The sequence has DsbA-specific CDD cd03019 and Pfam PF01323, an export signal, and the active-site cysteine pair. The UniProt similarity sentence is ARBA-only; it was replaced as support by independent domain classification, without editing the raw record. The oxidative-folding mechanism is inferred from characterized E. coli DsbA; native KT2440 substrate and membrane-partner preferences remain unknown. The historical protein-folding NEW assertion is retained unchanged in its machine fields and supported as direct catalytic participation, not necessity.

Current action counts: {"KEEP_AS_NON_CORE": 1, "MODIFY": 3, "NEW": 1}.
