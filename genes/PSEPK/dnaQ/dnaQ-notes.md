# dnaQ curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 10 current GOA rows, UniProt Q88FF6, and the DnaQ/RNase-H-like domain assignments. Accepted cytosolic localization, DNA replication, 3'-5' exonuclease activity, and replication proofreading; retained generic DNA binding as non-core. Removed DNA-directed DNA polymerase and DNA polymerase activity because DnaQ edits nascent DNA but does not polymerize it. Marked broader nucleic-acid binding, exonuclease activity, and DNA biosynthesis terms as over-annotated. No GOA row remains pending.


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88FF6 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003676 nucleic acid binding: MODIFY. The proofreading nuclease acts on DNA, so refine general nucleic-acid binding to the DNA-binding descendant already present.
- GO:0003677 DNA binding: ACCEPT. The editing subunit directly engages the nascent DNA end. DNA binding is integral to proofreading rather than a peripheral accessory property.
- GO:0003887 DNA-directed DNA polymerase activity: REMOVE. DnaQ is the editing exonuclease, whereas DnaE performs nucleotide addition. Target DnaQ family classification and Pseudomonas alpha/epsilon biochemical separation contradict assignment of the complex polymerase reaction to this individual subunit.
- GO:0004527 exonuclease activity: MODIFY. The DnaQ proofreading nuclease removes nucleotides in the 3-prime to 5-prime direction, supporting the directional descendant already present.
- GO:0005829 cytosol: ACCEPT. DnaQ acts with the chromosome-associated polymerase in the cytosol; localization is inferred from the conserved proofreading role.
- GO:0006260 DNA replication: MODIFY. Its direct replication contribution is proofreading, represented by the part_of descendant GO0045004 already present.
- GO:0008408 3'-5' exonuclease activity: ACCEPT. The target DnaQ-specific domain and RuleBase editing function agree with the separate epsilon exonuclease in the Pseudomonas replicase. This supports proofreading nuclease chemistry without assigning polymerase chemistry.
- GO:0034061 DNA polymerase activity: REMOVE. The polymerase reaction belongs to DnaE, not the DnaQ exonuclease. This is a complex-to-subunit catalytic misassignment, not a rejection of DnaQ participation in replication.
- GO:0045004 DNA replication proofreading: ACCEPT. DnaQ removes mismatched nascent nucleotides through its editing exonuclease activity; it performs the corrective step directly.
- GO:0071897 DNA biosynthetic process: MARK_AS_OVER_ANNOTATED. The inferred DNA-biosynthesis row appears to follow the erroneous complex-wide polymerase assignment. DnaQ removes nucleotides rather than synthesizing DNA; its established direct process is replication proofreading. A coupling to synthesis is real but does not by itself establish that this nuclease performs DNA biosynthesis.

Primary sources used: PMID:15611049. Independent frozen support: file:PSEPK/dnaQ/dnaQ-uniprot.txt.

### Follow-up: DNA biosynthesis participation

The initial over-annotation judgment on GO:0071897 was reconsidered after comparative primary evidence was checked. PMID:8702818 compares purified alpha with alpha-epsilon cores and reports faster DNA synthesis with epsilon; PMID:15611049 reconstructs the Pseudomonas alpha-epsilon replicase. This supports a conserved functional contribution to biosynthesis, beyond necessity alone. The existing BP is ACCEPT, while intrinsic polymerase MFs remain REMOVE. E. coli kinetic values are not transferred to KT2440.
