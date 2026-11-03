# Retired SYK-6 beta-etherase pathway records

`fetch_archived_records.py` recovers LigN C0SUK1 (UniSave74), LigP E1CJ68 (UniSave63), and LigQ G2IKM4 (UniSave56). It requests original version-pinned UniSave flat files, checks their accession and taxon627192, checks the current deleted record's UniParc identity, and passes the original flat-file block to the normal `fetch_gene_data` pipeline. The normal pipeline supplies live QuickGO data and deterministic review seeding. It does not generate functional decisions or artificial annotations.

Run from the repository root:

```sh
uv run python genes/SPHSK/ligN/ligN-source-analysis/fetch_archived_records.py
```

Each gene's `*-record-evidence.yaml` records the retrieval URL, entry and sequence versions, current deletion response and flat-file SHA256. Existing nonempty raw source text must match exactly or the script stops. The source records retain historical gene names and taxonomic classifications; review prose explains their current interpretation. All three live GOA queries returned zero rows at initial seeding. An empty annotation set is not an ND assertion.
