# rfbA curation notes

## Annotation-reviewer pass (2026-09-01)

Reviewed all 2 selected annotation rows against `rfbA-goa.tsv`, the local
UniProt record, the four-step module, and the OpenScientist module/pathway/taxon
report. The accepted GO:0008879 activity and proposed GO:0019305 pathway term
match the recorded EC 2.7.7.24 reaction and UniProt pathway statement. Final
actions: 1 ACCEPT, 1 NEW; no PENDING or unresolved existing annotation.

Provenance: [UniProt Q88LZ3, "Catalyzes the formation of dTDP-glucose, from dTTP and glucose 1-phosphate"] and `projects/P_PUTIDA/deep-research/PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist.md`.

## Completion pass (2026-11-10, dTDP-L-rhamnose module)

Added vetted supported_by quotes to every row that lacked one (cytosol rows cite
the E. coli RmlA-D ortholog cytosolic proteome, PMID:18304323), removed ARBA-only
PATHWAY quotes where they were the only support, and aligned polymer-level
process rows (GO:0000271, GO:0009243) with the batch-07 TreeGrafter re-review
decision (MARK_AS_OVER_ANNOTATED: precursor-supply enzymes form no glycosidic
bond). Status set to COMPLETE. Deep research was not regenerated (no provider
keys in this session).
