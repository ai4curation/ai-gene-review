# dnaA curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 10 current GOA rows, the reviewed UniProt record P0A116, and the row provenance in `dnaA-goa.tsv`. Accepted origin binding, ATP binding/hydrolysis, sequence-specific DNA binding, cytoplasmic localization, replication, initiation, and regulation. Retained generic DNA binding and plasma-membrane localization as non-core because neither replaces the oriC-centered role. No GOA row remains pending.


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target P0A116 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: MODIFY. DnaA recognizes origin DnaA boxes, so refine general DNA binding to the origin-binding term already present. P. putida DnaA binding and open-complex formation are directly demonstrated on plasmid RK2 oriV in PMID10749858; this is not a direct KT2440 chromosomal-oriC assay.
- GO:0003688 DNA replication origin binding: ACCEPT. Conserved DnaA origin recognition is supported by HAMAP MF_00377 and P. putida DnaA biochemical binding to RK2 oriV. The experimental paper assays plasmid origin opening, while the chromosomal role is inferred from the conserved initiator family.
- GO:0005524 ATP binding: ACCEPT. The conserved DnaA AAA+ domain binds ATP and its nucleotide state controls origin-firing competence; this is a core mechanistic property rather than an unrelated binding activity.
- GO:0005737 cytoplasm: ACCEPT. The conserved chromosomal initiator acts on the bacterial chromosome in the cytoplasm, consistent with the target HAMAP location statement; this is a conserved-location inference.
- GO:0005886 plasma membrane: UNDECIDED. The target HAMAP statement mentions acidic-phospholipid binding, but the frozen record assigns cytoplasm and the accessible P. putida primary paper does not establish plasma-membrane residence. Lipid binding alone cannot resolve this location claim; retain uncertainty rather than treating localization as demonstrated.
- GO:0006260 DNA replication: MODIFY. Origin recognition and opening specifically execute replication initiation, the part_of descendant already present; refine the broad replication term to GO0006270.
- GO:0006270 DNA replication initiation: ACCEPT. DnaA directly executes the origin-recognition/opening step rather than merely being required for cell division; the conserved DnaA mechanism and P. putida origin-opening experiments support initiation.
- GO:0006275 regulation of DNA replication: ACCEPT. ATP/ADP-dependent DnaA competence controls the onset of replication, a regulatory role in addition to the physical origin-opening step; this is conserved-family inference, not a measured KT2440 firing-frequency experiment.
- GO:0016887 ATP hydrolysis activity: ACCEPT. DnaA nucleotide hydrolysis switches the initiator from ATP-bound to ADP-bound states. Its AAA+ architecture and conserved DnaA regulation support ATP hydrolysis; no target-specific kinetic rate is asserted.
- GO:0043565 sequence-specific DNA binding: ACCEPT. DnaA-box sequence recognition is demonstrated for P. putida DnaA on oriV. Sequence specificity and origin localization are complementary binding properties; no automatic parent-child relationship between those two specific classes is assumed.

Primary sources used: PMID:10749858. Independent frozen support: file:PSEPK/dnaA/dnaA-uniprot.txt.
