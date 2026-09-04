# yajC research notes

## Functional assignment

The KT2440 protein is a single-pass membrane member of the YajC family
[file:PSEPK/yajC/yajC-uniprot.txt "Belongs to the YajC family."]. The same local
record assigns Q88PL6 to the YajC-specific subfamily
[file:PSEPK/yajC/yajC-uniprot.txt "PANTHER; PTHR33909:SF1; SEC TRANSLOCON
ACCESSORY COMPLEX SUBUNIT YAJC; 1."].

The strongest complex-level evidence comes from purification of the bacterial
SecYEG-SecDF-YajC-YidC holo-translocon [PMID:24550475 "The bacterial version
SecYEG interacts with the highly conserved YidC and SecDF-YajC subcomplex, which
facilitates translocation into and across the membrane."]. This supports
part_of GO:0031522 but does not isolate an individual YajC molecular function or
biological-process contribution.

Direct E. coli genetics found that yajC was neither essential nor detectably a
sec gene [PMID:7507921 "An analysis of yajC mutations constructed in vitro and
recombined onto the chromosome indicates that yajC is neither essential nor a
sec gene."]. That result does not exclude a condition-dependent accessory role
in KT2440, but it requires leaving individual MF and BP assertions unresolved.

## Annotation-reviewer pass (2026-09-01)

Reviewed the single GOA-derived location row and the proposed complex-membership
annotation against the local UniProt record, direct E. coli genetics,
holo-translocon literature, and the module-aware OpenScientist report. Outcome:
1 ACCEPT and 1 NEW; no row remains PENDING or UNDECIDED. No individual MF or BP
is asserted for YajC because the available evidence supports assembly membership
but does not isolate a conserved mechanistic activity.
