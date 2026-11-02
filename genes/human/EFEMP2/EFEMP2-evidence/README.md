# EFEMP2 source extracts

These files expose the underlying records used to review EFEMP2. They contain measurements and database assertions, not independent experimental conclusions or automated annotation decisions. The scientific interpretation is in the [source guide](../EFEMP2-source-guide.md) and review YAML.

## Contents

- `interactions.json`: source-row joins to the original MITAB records, including literal partner accessions, methods, taxa, checksums, recorded fragments and negative flags. Source-row numbers are zero-based positions in the 162 imported annotations.
- `official-partners.json` and `alternative-sequences.json`: official identities, functional/class annotations, relevant sequence features and reconstruction of 16 alternative sequences. A reference-sequence checksum does not authenticate an experimental insert; recorded fragment boundaries remain separate.
- `phylogeny.json`: the target sequence, lineage, two literal IBD assertions and their descendant donor paths. The current family is PTHR24034; the normal UniProt-derived PTHR24050 lookup is a distinct preserved source snapshot.
- `workbooks.json`: exact EFEMP2 cells and short headings from the parotid exosome and stem-cell-derived matrix workbooks. Physical row numbers include all original header and blank rows. The parotid extract retains the first ten columns, including accession, peptide/spectrum counts and coverage. The matrix extract distinguishes Table I protein measurements from Table VII expression clusters.
- `reactome.json`: saved reaction/entity fields showing the modeled EFEMP2 membership paths.
- `ontology.json`: current official definitions used for the partner-class and basement-membrane judgments.
- `source-manifest.json`: public URLs, byte counts, acquisition times and SHA-256 hashes for every raw input. `selection.json` specifies the biological target and source joins, not expected results.

Large original workbooks, the family MSA/tree and full articles are not bundled. The extracts can be reproduced from the exact saved raw files or downloaded from the recorded public URLs. Current APIs may have changed since capture; a changed hash is reported as a different source version and is never silently accepted.

## Reproduction

Python 3.9 or later is required, with `openpyxl==3.0.8` and `xlrd==2.0.1`. From this directory, either supply a JSON mapping of input IDs from `source-manifest.json` to saved raw filenames:

```sh
python3 reproduce.py --inputs /path/to/saved-inputs.json --output /path/to/new-output
```

or use the public source URLs:

```sh
python3 reproduce.py --download-cache /path/to/raw-cache --output /path/to/new-output
```

The output directory must not already exist. Each source hash is checked before parsing. The download route requires no API key, but availability and unchanged current-API responses are not guaranteed. It fails clearly on unavailable or changed input; it does not substitute summary text or a new dataset version. An existing saved-input mapping can be combined with `--download-cache` to retrieve only missing inputs.

The parser opens both workbooks read-only. Openpyxl may warn about an unsupported worksheet extension; no workbook is saved, and the original bytes remain unchanged. The selected cell values were independently compared with earlier source projections. A changed-input control fails hash validation, and an unrelated target filter returns no workbook target hits.

## Interpretation limits

Missing matches in this IntAct snapshot do not refute a low-throughput paper. Binary assays do not establish native extracellular complexes. A partner-class binding term does not transfer the partner's own activity. Matrix or vesicle detection does not establish a specialized physiological role. The PAINT record is a curator's ancestral-node judgment, not a donor-count score; target self-inclusion is not circularity.
