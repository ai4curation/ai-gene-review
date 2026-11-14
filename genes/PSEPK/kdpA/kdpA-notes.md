# kdpA curation notes

## Evidence assessment

PSEPK Q88FD7 is assigned to the KdpA family by UniProt and retains the role of
the potassium-selective, channel-like subunit. The E. coli KdpFABC crystal
structure directly places potassium in the KdpA selectivity filter and separates
the KdpA ion pathway from the KdpB ATPase machinery [PMID:28636601, "one
channel-like subunit (KdpA) belonging to the superfamily of potassium
transporters"]. The completed OpenScientist report independently identifies the
same architecture and explicitly notes that direct P. putida biochemical data
were not found [file:PSEPK/kdpA/kdpA-deep-research-openscientist.md].

## Curation decision

GO:0030955 is KdpA's own molecular function. GO:0008556 describes the complete
heteromeric pump and is accepted in substance, with the preferred
`contributes_to` relationship represented in `core_functions` rather than as a
no-op term replacement.

## 2026-11-01 completion pass

Rows upgraded with reasons and supported_by; GO:0006813 changed to MODIFY ->
GO:0071805 (correct-but-general rule). Added NEW part_of GO:0031004 (ISO, from E.
coli KdpFABC) to match the core_functions in_complex. E. coli evidence is cited as
orthology-based support throughout.


## Scoped Kdp module consultation — 2026-11-07

The target sequence independently confirms TNGGG at234–238. The current ion path is periplasm→KdpA filter/tunnel→KdpB→cytoplasm, not a wholly KdpA transmembrane pore. PMID41259220 supports this with E. coli wild-type nanodisc structure and tunnel-mutant transport tests; the KT2440 mechanism is inferred. The original source/provider report and historical ISO complex row remain intact.

Every original annotation row and its source payload/order was reviewed and preserved. No additional annotation rows were proposed. Full provenance and assay boundaries: `analysis/module_audits/bacterial_kdp_potassium_homeostasis/psepk-consultation/primary-scope.md`; sequence checks are adjacent. No IBA rows occur in these six reviews, so no IBA loss judgment is being made. Family membership and original historical ISO donors are retained independently of donor counts.

Existing OpenScientist research was inspected, not rewritten; target sequence checks corroborate its filter motif.

Native KT2440 context is supplied by PMID38927284 full text: salt stress increases kdpA/B/D transcripts, but individual overexpression does not improve growth in the tested high-salt medium. This is not a purified activity assay or proof that the complete pump is unimportant. PMID26913973 publisher text corrects the historical kdpB pseudogene annotation; its local abstract cache remains unchanged. No salt-tolerance process assertion is added.
