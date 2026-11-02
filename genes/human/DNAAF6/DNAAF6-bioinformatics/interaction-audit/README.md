# DNAAF6 interaction-record audit

This saved-input audit reproduces the **16 screen-derived source rows, 49 matching interaction records and 98 participant reference-sequence checks** discussed in the [evidence guide](../../DNAAF6-evidence-guide.md). It requires Python 3.9 or newer and no third-party packages or network calls:

```sh
python3 replay.py --check
```

Run without `--check` to regenerate `RESULTS.json`. The script selects records by the literal DNAAF6 accession, partner accession and source PMID. It independently computes the ROGID sequence component from each reference protein sequence and compares both participant checksums and taxa with the MITAB record. It retains method, host, fusion features, participant-identification method, positive/negative flag and original interaction identifiers in its output.

## Inputs and selection

- `intact-all.tsv` is the unchanged 52-record IntAct PSI-MITAB 2.7 response retrieved on 2026-10-17. The exact query, date and digest appear in `input-provenance.json`.
- `source-rows.json` contains the 16 unchanged source annotation dictionaries for PMID:25416956 and PMID:32296183, with their zero-based indices in the 40-row review at the recorded source head. Review actions are not input to record selection.
- `reference-sequences.fasta` contains 16 distinct official reference sequences extracted from the cited UniProt JSON responses and three product-specific FASTAs. The extraction method, original URL, retrieval date, original-response digest and sequence digest are recorded individually in `input-provenance.json`. These are protein reference sequences, not reconstructed experimental fusion constructs.
- `RESULTS.json` is derived output. It reports three unselected raw records (indices 41–43), which belong to PMID:26871637 and therefore are not counted as support for the selected source assertions. Their exclusion is by publication/source boundary, not a negative biological verdict.

The 2014 and HuRI records include pooled, array and validated two-hybrid stages. Multiple records for a pair are not multiple independently established physiological interactions. Each selected group has a validated two-hybrid record, and all selected records have a negative-interaction flag of false. GAS2L2 additionally has a recorded MAPPIT assay in human HEK293T cells; this is not generalized to all pairs.

## Interpretation limits

A matching ROGID authenticates a reference sequence and taxon. It does not establish that the experimental protein lacked tags, that every unrecorded modification is known, that full-length native topology was reproduced, or that a native complex exists in the same cell. In particular, binary P2RX4 association does not demonstrate binding to an active channel in a native membrane. ARID4B-3, PID1-3 and Q8IY57-5 are literal partner products; the last is named YAF2 isoform 2 in UniProt, despite its accession suffix.

The script does not infer molecular function, regulation, endogenous coexistence or false-positive rates. The biological review separately evaluates each partner's class and the source-specific assay limits. The original 2014 map reports a three-of-four retesting criterion; that threshold is not imported into the separate HuRI study.

Original study links: [2014 human interactome](https://pmc.ncbi.nlm.nih.gov/articles/PMC4266588/), [HuRI](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/). The published raw interaction identifiers and source accession pairs remain available in the tabular input and derived result.
