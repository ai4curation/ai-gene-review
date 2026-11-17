# rffG curation notes

## Annotation-reviewer pass (2026-09-01)

Reviewed all 2 selected annotation rows against `rffG-goa.tsv`, the local
UniProt record, existing OpenScientist gene research, and the combined module
report. GO:0008460 is the exact EC 4.2.1.46 activity. Replacing broad
GO:0009225 with GO:0019305 records the specific pathway once without a duplicate
NEW assertion. Final actions: 1 ACCEPT, 1 MODIFY; no PENDING or unresolved row.

Provenance: [UniProt Q88LZ1, "Reaction=dTDP-alpha-D-glucose = dTDP-4-dehydro-6-deoxy-alpha-D-glucose"] and `projects/P_PUTIDA/deep-research/PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist.md`.

## Completion pass (2026-11-10, dTDP-L-rhamnose module)

Added vetted supported_by quotes to every row that lacked one (cytosol rows cite
the E. coli RmlA-D ortholog cytosolic proteome, PMID:18304323), removed ARBA-only
PATHWAY quotes where they were the only support, and aligned polymer-level
process rows (GO:0000271, GO:0009243) with the batch-07 TreeGrafter re-review
decision (MARK_AS_OVER_ANNOTATED: precursor-supply enzymes form no glycosidic
bond). Status set to COMPLETE. Deep research was not regenerated (no provider
keys in this session).
