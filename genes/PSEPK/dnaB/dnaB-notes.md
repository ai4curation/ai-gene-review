# dnaB curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 11 current GOA rows, UniProt Q88DF2, EC 5.6.2.3, and the DnaB domain assignments. Accepted DNA helicase activity, ATP binding/hydrolysis, cytosolic localization, DNA replication, and the specific 5'-3' helicase activity; retained generic DNA binding as non-core. Marked generic nucleotide binding, helicase activity, and hydrolase activity as over-annotated. Primer synthesis is retained as non-core because the target record assigns that process and primosome-complex membership, without using those automated assignments to infer a target-specific interaction mechanism. No GOA row remains pending.


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88DF2 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0000166 nucleotide binding: MODIFY. ATP is the supported nucleotide for the DnaB ATPase motor; refine nucleotide binding to the ATP-binding descendant already present.
- GO:0003677 DNA binding: ACCEPT. DnaB directly contacts the DNA tracking strand and separates duplex DNA. DNA interaction is integral to its motor mechanism; this binding claim is not peripheral simply because helicase catalysis is more informative.
- GO:0003678 DNA helicase activity: MODIFY. The target DnaB RuleBase-supported function specifies 5-prime to 3-prime translocation, warranting the directional helicase descendant already present.
- GO:0004386 helicase activity: MODIFY. The DNA substrate and 5-prime to 3-prime polarity are established for the conserved DnaB motor, so refine this broad helicase term.
- GO:0005524 ATP binding: ACCEPT. ATP binding fuels the conserved DnaB helicase motor; the target RuleBase function explicitly identifies an ATP-dependent helicase.
- GO:0005829 cytosol: ACCEPT. The chromosome-associated DnaB motor acts in the bacterial cytosol. This location is inferred from conserved replisome function rather than an independent KT2440 microscopy assay.
- GO:0006260 DNA replication: ACCEPT. DnaB performs parental-duplex unwinding during initiation and elongation, directly participating in replication rather than merely causing an indirect growth phenotype.
- GO:0006269 DNA replication, synthesis of primer: ACCEPT. DnaB contributes primosome organization and template presentation to DnaG-mediated priming; DnaG performs RNA polymerization. The conserved helicase–primase coupling supports participation without assigning primase catalysis to DnaB. The previous GO cross-reference quote was circular and has been replaced by independent functional/domain evidence.
- GO:0016787 hydrolase activity: MODIFY. The hydrolysis is ATP hydrolysis coupled to the directional helicase mechanism. Refine to both supported descendants already present rather than marking a true parent as false.
- GO:0016887 ATP hydrolysis activity: ACCEPT. The target RuleBase statement explicitly describes DNA-dependent ATPase activity, which drives the helicase motor.
- GO:0043139 5'-3' DNA helicase activity: ACCEPT. The target RuleBase function and DnaB family assignment support an ATP-driven 5-prime to 3-prime replicative helicase; this is conserved-function inference, not a KT2440 unwinding-rate measurement.

Primary sources used: . Independent frozen support: file:PSEPK/dnaB/dnaB-uniprot.txt.

Primary helicase–primase coupling support added: [PMID:17947583], explicitly a homologous structural system rather than KT2440 biochemistry.
