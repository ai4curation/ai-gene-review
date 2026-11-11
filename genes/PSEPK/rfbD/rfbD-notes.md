# rfbD curation notes

## Annotation-reviewer pass (2026-09-01)

Reviewed all 4 selected annotation rows against `rfbD-goa.tsv`, the local
UniProt record, and the combined module report. Exact reductase activity,
cytosol, and dTDP-rhamnose biosynthesis are retained; O-antigen biosynthesis is
kept as non-core downstream product-use context. Cluster context supports rfbD
as the committed final reductase. Final actions: 3 ACCEPT,
1 KEEP_AS_NON_CORE; no PENDING or unresolved row.

Provenance: [UniProt Q88LZ2, "Catalyzes the reduction of dTDP-6-deoxy-L-lyxo-4-hexulose to yield dTDP-L-rhamnose"] and `projects/P_PUTIDA/deep-research/PSEPK__dtdp_l_rhamnose_biosynthesis__ppu00523-deep-research-openscientist.md`.

## Completion pass (2026-11-10, dTDP-L-rhamnose module)

Added vetted supported_by quotes to every row that lacked one (cytosol rows cite
the E. coli RmlA-D ortholog cytosolic proteome, PMID:18304323), removed ARBA-only
PATHWAY quotes where they were the only support, and aligned polymer-level
process rows (GO:0000271, GO:0009243) with the batch-07 TreeGrafter re-review
decision (MARK_AS_OVER_ANNOTATED: precursor-supply enzymes form no glycosidic
bond). Status set to COMPLETE. Deep research was not regenerated (no provider
keys in this session).
