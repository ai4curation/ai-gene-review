# EHMT1 evidence replay

Run `python3 replay.py --check` with Python 3.9 or later. It uses only the standard library and bundled `inputs.zip`; no network, installation or environment changes are required. To write independently recomputed output, use `python3 replay.py --output /tmp/EHMT1-results.json`.

The archive preserves 60 exact saved inputs: official protein and FASTA records, the normal GOA export and source dictionaries, PAINT tree/MSA/IBDs, donor annotations, ARBA rules (including the genuine unavailable-rule response), Reactome records, HPA metadata and the IntAct export. The manifest records checksums, retrieval provenance and derivations. Article bodies are excluded. The program reads archive members directly without extracting paths, checks exact names/sizes/hashes and rejects unexpected or missing input.

The calculations verify source identity and literal evidence joins. They do not turn a pathway model into an experiment, prove physiological activity from a sequence, or adjudicate a paper from its title. Current donor annotations retain their original evidence labels; missing current interaction records are not negative evidence. Mixed-case PANTHER alignment residues are normalized to uppercase only for sequence comparison.
