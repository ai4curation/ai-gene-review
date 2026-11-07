# kdpC: Caulobacter vibrioides NA1000

## 2026-11-07 primary-source review

- Identity: B8GVG0, taxon565050 (NA1000/CB15N), not the distinct CB15 reference. Pristine ordered annotations and raw source hashes were frozen before review.
- All 6 seeded rows were reviewed. No annotation payload, order or evidence code was changed; no NEW row was added.
- A genuine default Falcon attempt failed with HTTP403 authentication; no provider report was created or invented. Manual reading used the frozen sources cited in the review.
- PAINT-loss tooling completed but the exact accession is absent from the cached family tree. Loss placement is therefore unassessed, not proven absent. These seeds contain IEA, not IBA, rows.
- PMID:39133005 full text establishes the exact NA1000 locus and native experiments. KdpC (CCNA_01665) is a single-pass membrane accessory subunit of the KdpABC potassium uptake complex in Caulobacter vibrioides NA1000. KdpC-family conservation and the native requirement for the KdpABC locus under potassium limitation support a structural contribution to the assembled transport machinery. Homolog structures place the large soluble domain on the periplasmic side, although this orientation has not been measured for NA1000 KdpC. The ATP-hydrolyzing catalytic center resides in KdpB. An older model assigning KdpC an ATP-dependent catalytic-chaperone role remains uncertain for this protein.
- Core synthesis separates intrinsic catalytic/recognition activity from assembled-complex contributions. No arbitrary cross-species subunit compatibility is assumed.
- KdpC ATP-binding remains UNDECIDED: comparative topology does not prove a negative binding assay, and target activity is unmeasured. PMID:21711450 remains an abstract-only cache; PMID:28636601 full text is an E. coli KdpA-Q116R complex.


## 2026-11-07 PR6179 round-one adjudication

Reviewed the source relation, core role and source-specific limits relevant to this gene. See `analysis/module_audits/bacterial_kdp_potassium_homeostasis/round1/evidence.md` for the full evidence and disagreement record. Original ordered annotation payloads, qualifiers and historical NEW/retired flags are preserved. GO0008556 now has a relation-specific overannotation judgment and probable source correction from enables to contributes_to; structural contribution remains core. KdpF requirement is conditional on the tested detergent-solubilized preparation, not universal native essentiality. [PMID:10608856; PMID:34272288].
