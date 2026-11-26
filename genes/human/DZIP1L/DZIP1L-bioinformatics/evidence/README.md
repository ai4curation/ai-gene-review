# DZIP1L source-identity reconstruction

This Python 3.12 standard-library analysis joins the frozen annotation queries to authentic IntAct records, checks participant reference-sequence ROGIDs, reconstructs the target PAINT path and literal IBDs, distinguishes direct donor records from propagated records, checks ARBA conditions, extracts HPA's individual-location reliability, and compares current natural products with archived clone translations. It does not compute GO review actions or protein activities.

Run from this directory, writing outputs outside the published source files:

```sh
python3 reproduce.py --inputs . --cache /tmp/dzip1l-inputs --output /tmp/dzip1l-results.json
cmp results.json /tmp/dzip1l-results.json
python3 reproduce.py --inputs . --cache /tmp/dzip1l-inputs --control-target Q8TAP6 --output /tmp/dzip1l-cep76.json
cmp control-CEP76.json /tmp/dzip1l-cep76.json
```

`raw-inputs.tar.gz` contains the exact 59 retrieved structured-data/sequence files, including both genuine ENA records. Every member is checked against `input-manifest.json` before parsing. It contains no publication bodies. The manifest records public source URLs, retrieval times and hashes. `queries.json` holds the unchanged 28 source assertions and the explicit accession/feature queries; these are input questions, not expected answers. `results.json` and `control-CEP76.json` are actual outputs. The same participant-identity code is tested with CEP76 as the target and DZIP1L as its partner.

`fetch_inputs.py` can acquire the declared URLs, but current services can change or block access. It stops on a changed checksum and never silently substitutes current data for the frozen snapshot. Offline replay uses the bundled bytes and needs no network or third-party library. The archive is checked for plain filenames before extraction.

The ROGID check authenticates the database's participant reference sequence, not the sequence of the experimental insert. Literal feature sides and ranges remain separate. The ENA comparison uses the archived record's translation qualifier; it is not a fresh translation of experimental DNA. Natural-product domain retention does not prove equivalent activity. PAINT reconstruction establishes present tree descent and source records; it does not claim to recreate a curator's historical reading. HPA metadata is not image-pixel interpretation. Database class evidence supports a binding-partner class without assigning that partner's activity to DZIP1L.
