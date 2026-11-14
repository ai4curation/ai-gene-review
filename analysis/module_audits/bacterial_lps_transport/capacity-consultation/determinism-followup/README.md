# Deterministic quote ordering follow-up

The original handoff remains unchanged as historical provenance. Its quote-file hash cannot be reproduced because the original quote bytes were not retained and the former checker iterated an unordered set. This receipt does not claim original semantic equality.

The checker now sorts the quote tuples. Fresh runs with PYTHONHASHSEED=1 and 2 produced identical quotes.json and closure.json bytes, checked all 302 quotations against their sources and all 435 frozen inputs, and preserved the multiset of the observed regenerated quote file archived here. Capacity cases and Ruff pass. Only check_closure.py and quotes.json differ among the original nine manifest entries.

Use handoff-superseding.json in this directory as the current release, retaining the original parent handoff.json and this full before/after receipt.
