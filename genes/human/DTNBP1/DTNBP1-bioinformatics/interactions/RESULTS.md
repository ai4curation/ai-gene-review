# Interaction reference-identity results

The frozen DTNBP1 input contains 95 selected IntAct records. All 190 side-specific sequence/taxon ROGIDs match the 26 supplied official reference sequences. The independent SNAPIN-target run selects nine records and verifies 18 reference identities. These counts were read from the actual script outputs; they are not encoded as expected results in the algorithm.

The result verifies database reference identity only. It cannot establish experimental insert sequence, native physiology, directness of co-complex association, affinity or product-specific function. The original methods, spoke-expansion markers, negative flags and side-specific features remain decisive. In particular, the SYBU pair's 1–189 feature is attached to DTNBP1, while the separate source table does not confirm that boundary.

`source-manifest.json` records the live-source URL, original snapshot hash, unchanged source-line selection and sequence provenance. The finite inputs permit reproduction without a network request. The control uses SNAPIN, a different protein, without adding any functional conclusion about it.

- [x] The algorithm accepts arbitrary supplied MITAB, FASTA and target; no gene-specific result or biological conclusion is encoded.
- [x] It was executed on DTNBP1 and on the independent SNAPIN input.
- [x] Both runs completed and their direct JSON outputs are included.
- [x] All source lines and reference sequences are derived from authenticated database captures.
- [x] The conclusions remain limited to reference identity and preserve assay/insert uncertainty.
