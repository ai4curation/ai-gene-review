# KIAA1614 curation notes

## 2026-09-21 full-gene re-review

Read all six annotations and the existing focused OpenScientist report. No duplicate requested. Live InterPro identifies IPR051741 as a family, not a physical PAR6 domain, and retains a PTHR14102:SF12 hit with score 4.6e-32. DUF4685 is the only specific domain annotation; no annotated PB1/PDZ/CRIB supports conventional Par6 architecture. This warrants a node/region audit, not a claim of random homology from four-mer Jaccard scores. IBA is not circular merely because the target lacks experimental GO assertions. The report's unproven AlphaFold numerical claims and absolute cannot-bind deductions were not adopted.

Verified source Q9NPB6 as PARD6A, not PARD6B. Current IBD and target PAINT rows retain the main ancestral assignments and add newer terms; original six rows are preserved without importing redundant NEW annotations. No full tree/MSA reconstruction was claimed.

Nucleus restored to ACCEPT: PMID:30021884 describes intact-nucleus crosslinking, and live IntAct IM-26653-2713 maps Q5VZ46 to histone H2B Q93079. The cache is labelled full text but contains abstract/discussion only; raw peptides were not reanalyzed. This is high-throughput corroboration of the existing location, not proof of a nuclear molecular function. IntAct also verifies PTPRR association in PMID:31980649; this was not converted into a generic binding or pathway annotation. Snapshot in projects/IBA_REVIEW/rereview-2026-09-20/kiaa1614-evidence-check.json.

Other five functions remain UNDECIDED due unresolved node/architecture relationship. Absence of a target study, alternative compartment or interaction-database edge is not evidence of functional loss.
