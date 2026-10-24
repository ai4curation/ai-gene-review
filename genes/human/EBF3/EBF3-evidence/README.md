# EBF3 evidence replay

This small artifact reconstructs the family-tree path, literal PAINT assertions on that path, and sequence identity of the two deposited templates cited in the human transcription study. It computes these observations from source data; it does not compute annotation decisions or infer equivalent activity of natural products.

The seven input URLs, exact hashes and sizes are in [sources.json](sources.json). The captured IBD source was reused byte-for-byte from the genuine PANTHER source (header: PANTHER 19, 2026-08-28). Other inputs were retrieved from the official PANTHER, UniProt and ENA endpoints. Large inputs and full article bodies are not bundled. [observations.json](observations.json) is the raw-derived result for the recorded versions.

Use Python 3.9 or later; no third-party package or API key is required. With saved raw files, make a JSON object mapping the seven keys in `sources.json` to their local paths, then run:

```sh
python3 reproduce.py --inputs saved-paths.json --output replay.json
```

Alternatively, retrieve the public sources and enforce the recorded hashes:

```sh
python3 reproduce.py --download-dir raw-inputs --output replay.json
```

The saved-input route was executed during preparation. Live downloading is implemented but was not rerun as part of that check; endpoints may change or become unavailable. Any changed source bytes fail the hash check and require a new, explicitly documented evidence snapshot.

The result identifies a 14-node path to human EBF3, four ancestral IBD assertions, and a 596-residue target sequence matching Long. Both deposited human template translations are 551 residues and match Short. Template agreement does not authenticate each physical experimental preparation. The IBD's target-including nuclear evidence is preserved, as are all literal supporting identifiers; its presence is not a circularity claim.

Primary assay context, access limitations and the distinction between human EBF3 and EBF1 structural constructs are described in the [source guide](../EBF3-source-guide.md).
