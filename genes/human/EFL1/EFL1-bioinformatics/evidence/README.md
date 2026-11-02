# EFL1 evidence replay

Run `python3 reproduce.py` (Python 3.10 or later; standard library only), or `just reproduce`. The program checks every bundled input hash, reconstructs the target family path and source-specific ancestral assertions, joins literal donor identifiers to current records, evaluates sufficient ARBA conditions, extracts the exact SBDS interaction records, and reconstructs both natural protein sequences. `--output /new/path.json` optionally saves the computed result. Missing or altered inputs raise explicit errors, including under `python3 -O`.

The approximately 2.5 MB archive contains exact computational API responses and source projections; no original papers, publisher PDFs or protein-screen supplements are bundled. Full tree, MSA and IBD inputs allow the lineage check to run without a live service. The manifest records acquisition URLs, timestamps and hashes. API content may change, so fetching a current response is not equivalent to replaying this snapshot.

The script reports observations, not annotation verdicts. Current donor records are not all experimental, and the output separates directly experimental evidence codes. The target's presence among its own IBD donors is valid. The shared yeast P32324 entry represents EFT1/EFT2; the literal source gene remains explicit.

`results.json` is generated from raw inputs and checked during every replay. [RESULTS.md](RESULTS.md) explains the biological limits; [the source guide](../../EFL1-source-evidence.yaml) gives primary-paper and stable interaction locators. The archive cannot prove experimental insert sequences, isolated-protein activity from proximity labeling, or the timing of GTP hydrolysis from static structures.
