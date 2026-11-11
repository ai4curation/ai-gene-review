# Executed DNM1 extraction

The fixed AP-MS snapshot contains 7,543 nodes and 36,842 edges. Five edges involve the exact DNM1 node 560878; three match the requested partner subset. The fixed OpenCell CSV contains 29,922 data rows, five involving DNM1; two match its reciprocal DNM2 subset. The outputs preserve all original fields and make no scientific verdict.

| Dataset | Selected original record | Direction |
| --- | --- | --- |
| U2OS AP-MS | edge 605226 | SNX9 → DNM1 |
| U2OS AP-MS | edge 609892 | DNM2 → DNM1 |
| U2OS AP-MS | edge 568720 | GRB2 → DNM1 |
| OpenCell | data index 7578; physical line 7580 | DNM1 bait → DNM2 prey |
| OpenCell | data index 7582; physical line 7584 | DNM2 bait → DNM1 prey |

The AP-MS node attributes independently mark the selected source partners as baits and DNM1 as prey. The other two incident graph edges concern AMPH and MRPL49. OpenCell's other DNM1-involving rows concern DNM3, PARP1 and SNX9. These exclusions are selection boundaries, not negative biological findings.

The DNM1-bait/DNM2-prey accession field remains `K7EMQ3;P50570-3;P50570-2;P50570-5;P50570-4;P50570`; the reciprocal DNM1-prey group remains `A0A0D9SFE4;A0A1B0GU67;A0A1B0GUX5`. No member was substituted, removed or promoted to an assayed natural isoform.

The script output exactly matches the owner's independently saved three-edge and two-row projections after order-insensitive comparison of node attributes. All numeric CSV values remain their original strings. The alternate-target DNM2 test on the same raw inputs produces 12 incident graph edges and 11 incident CSV rows, with 3 and 2 selected by that test's explicit partner lists. It is a computational control, not a DNM2 scientific review.

- [x] Raw source hashes verified before extraction.
- [x] Target/partner inputs are explicit configuration; no result IDs, measurements or counts are hardcoded in the script.
- [x] Executed on DNM1 and a distinct DNM2 target selection.
- [x] Complete raw-derived output saved in `RESULTS.json`.
- [x] Exact output replay with `--check` passed.
- [x] Independent saved projections matched.
- [x] Source direction, complete accession groups and indexing conventions retained.
- [x] No source retrieval, scientific verdict, canonical write or owner-file mutation performed by this task.
