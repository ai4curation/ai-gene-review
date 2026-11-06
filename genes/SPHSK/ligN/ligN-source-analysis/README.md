# Retired SYK-6 beta-etherase pathway records

`fetch_archived_records.py` recovers LigN C0SUK1 (UniSave74), LigP E1CJ68 (UniSave63), and LigQ G2IKM4 (UniSave56). It requests original version-pinned UniSave flat files, checks their accession and taxon627192, checks the current deleted record's UniParc identity, and passes the original flat-file block to the normal `fetch_gene_data` pipeline. The normal pipeline supplies live QuickGO data and deterministic review seeding. It does not generate functional decisions or artificial annotations.

Run from the repository root:

```sh
uv run python genes/SPHSK/ligN/ligN-source-analysis/fetch_archived_records.py
```

Each gene's `*-record-evidence.yaml` records the retrieval URL, entry and sequence versions, current deletion response and flat-file SHA256. Existing nonempty raw source text must match exactly or the script stops. The source records retain historical gene names and taxonomic classifications; review prose explains their current interpretation. All three live GOA queries returned zero rows at initial seeding. An empty annotation set is not an ND assertion.

## Current exact-sequence cross-references

`uniparc-2026-11-03/` retains unmodified official UniParc entry and complete database-cross-reference JSON responses, direct current UniProtKB accession responses, and URL/time/SHA256 provenance. All three archived sequences match their UniParc sequences exactly. None has an active UniProtKB cross-reference; active RefSeq and EMBL records remain. All organism-bearing cross-references identify taxon 627192. The original archival sources are retained.

Reproduce in a **new** output directory; this read-only lookup does not alter reviews, raw gene sources or existing snapshots:

```sh
uv run python genes/SPHSK/ligN/ligN-source-analysis/query_uniparc_cross_references.py /tmp/beta-aryl-uniparc-new
```

The script follows cross-reference pagination, checks the reported total, compares each archived sequence to UniParc, and fetches the current UniProtKB record for any active candidate a future lookup returns.
