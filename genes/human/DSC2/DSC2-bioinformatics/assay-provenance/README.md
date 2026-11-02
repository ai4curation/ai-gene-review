# DSC2 assay-source and sequence checks

This executable analysis joins the literal 2011 DSC2–DSG2 IntAct record to official reference sequences, and extracts the DSC2 construct and DSC2–DSG2 affinity provenance from the 2022 publication’s original workbooks. It does not calculate biochemical affinity or infer native binding from sequence similarity.

The saved run found one exact IntAct pair, whose reference ROGIDs match human Q02487 and Q14126. The record retains its COS-1 host, GFP tag and DSC2 sufficient-region/mutant context. In the workbook, the 693-residue DSC2 ectodomain exactly matches canonical residues 1–693. The 29,000 nM affinity is attributed to the earlier PMID:27298358 study; the source-data network calls it Published. The ectodomain is shared by both natural DSC2 products and cannot resolve their tail-dependent functions.

Install `requests` and `openpyxl`, then run:

```sh
python fetch_inputs.py --output-dir inputs
python check_assays.py --inputs inputs --output rerun.json
```

Alternatively provide previously downloaded genuine inputs with the names listed in `input-manifest.json`. Fetches use real public endpoints and preserve HTTP response bytes/receipts. If an endpoint fails or returns a challenge instead of a workbook, the script fails rather than inventing a result. Remote database versions may change; compare the new input hashes and reference sequences with the saved run before interpreting a changed result. `results.json` was generated from the archived genuine inputs identified by the manifest, without a second network retrieval.

Public sources:

- [PMID:35922511 article and supplements](https://pmc.ncbi.nlm.nih.gov/articles/PMC9365698/): Table 1 row 183, Table 3 row 151, Figure 1/2 network source data.
- [IntAct EBI-6901957](https://www.ebi.ac.uk/intact/interaction/EBI-6901957), IM-20978-13, anti-tag co-IP MI:0007.
- [Q02487](https://www.uniprot.org/uniprotkb/Q02487/entry) and [Q14126](https://www.uniprot.org/uniprotkb/Q14126/entry) reference sequences.

The full source scope, independent original-paper readings and limitations are recorded in the adjacent DSC2 source-evidence guide. No new annotation or all-product equivalence follows from this analysis.
