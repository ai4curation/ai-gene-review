# rmlC curation notes

## Annotation-reviewer pass (2026-09-01)

Reviewed all 5 selected annotation rows against `rmlC-goa.tsv`, the local
UniProt record, and the combined module report. The exact epimerase activity,
cytosol, and dTDP-rhamnose process are retained; the generic epimerase term is
replaced by GO:0008830 and downstream polysaccharide synthesis remains marked
as over-annotated. PP_0265 is a supported extra RmlC-family enzyme, but its
specific physiological partition from cluster-encoded rfbC remains open. Final
actions: 3 ACCEPT, 1 MODIFY, 1 MARK_AS_OVER_ANNOTATED; no PENDING row.

Provenance: [UniProt Q88R69, "Catalyzes the epimerization of the C3' and C5'positions"] and `projects/P_PUTIDA/deep-research/PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist.md`.

## Completion pass (2026-11-10, dTDP-L-rhamnose module)

Added vetted supported_by quotes to every row that lacked one (cytosol rows cite
the E. coli RmlA-D ortholog cytosolic proteome, PMID:18304323), removed ARBA-only
PATHWAY quotes where they were the only support, and aligned polymer-level
process rows (GO:0000271, GO:0009243) with the batch-07 TreeGrafter re-review
decision (MARK_AS_OVER_ANNOTATED: precursor-supply enzymes form no glycosidic
bond). Status set to COMPLETE. Deep research was not regenerated (no provider
keys in this session).
