# ligA curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 6 current GOA rows and reviewed UniProt Q88F25. Accepted NAD-dependent DNA ligase activity, cytosolic localization, and DNA replication; retained generic DNA binding as non-core. Kept DNA repair as a genuine non-core role outside the focused replication boundary and marked generic DNA metabolism as over-annotated. No GOA row remains pending.


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88F25 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: ACCEPT. LigA binds nicked double-stranded DNA as its substrate; this is part of its core ligation chemistry rather than a peripheral binding property.
- GO:0003911 DNA ligase (NAD+) activity: ACCEPT. HAMAP MF_01588 identifies NAD-dependent nick sealing, distinguishing LigA from ATP-dependent ligases. This is curated-family inference, not a measured KT2440 rate.
- GO:0005829 cytosol: ACCEPT. LigA seals chromosome DNA nicks in the cytosol; the cellular location is inferred from its conserved genome-maintenance function.
- GO:0006259 DNA metabolic process: MODIFY. LigA directly seals nicks in both replication and repair. Refine the broad DNA-metabolism term to both supported descendants already present rather than treating repair as peripheral.
- GO:0006260 DNA replication: ACCEPT. LigA directly joins adjacent DNA fragments during replication, providing the nick-sealing step rather than merely affecting growth.
- GO:0006281 DNA repair: ACCEPT. The same nick-sealing chemistry completes DNA repair intermediates. Repair is a core LigA genome-maintenance role alongside replication, as supported by the target HAMAP function.

Primary sources used: . Independent frozen support: file:PSEPK/ligA/ligA-uniprot.txt.
