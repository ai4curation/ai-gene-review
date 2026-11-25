# ELANE reproducible database evidence

Run from this directory with Python 3.9 or later:

```bash
python reproduce.py
```

No packages, network connection, credentials or environment installation are needed. The program authenticates the archive and each member, extracts it into a temporary directory, reconstructs database identities and joins, and removes the temporary files. It prints the resulting counts and rule matches; it does not generate annotation decisions.

The archive contains official database responses and retrieval receipts, the complete saved IBD file, the literal target family tree and alignment, source contexts, and reconstruction code. It includes 102 source objects and all 104 raw QuickGO contexts. It excludes original article bodies, figure images, supplements, provider logs and private working environments.

`archive.json` records the exact compressed-file and member-manifest hashes. `RESULTS.md` describes the biological meaning and limits. The reconstructed paths retain catalyst, input/output, cargo and candidate membership distinctions. They are evidence of what the captured resource asserted, not an automatic endorsement of every downstream biological claim.

The database reconstruction and PAINT code are preserved from the source analysis except for one portability adaptation: the absolute external-origin check is replaced by authentication of the bundled frozen inputs through the archive manifest. All scientific parsing and path reconstruction remain unchanged. Every raw database and frozen-input byte is unchanged.
