# EBP source audit

Python 3.9+ and its standard library are sufficient. Run from this directory:

```sh
python3 replay.py --check
python3 replay.py --output /tmp/EBP-replayed-results.json
```

`--inputs` can point to another saved artifact directory. The script reads the tar archive in memory without extracting paths, verifies every member hash and the archive hash, then derives the selected IntAct records, source-row joins, interactor ROGIDs, historical SLC3A2 sequence, target PAINT path, literal family assertions, Reactome identities and actual GO definitions. `--check` compares the recomputed complete result to `results.json`; changed raw inputs or results fail. No network or API key is required. Live provider URLs are recorded in `source-manifest.json`; they may now serve newer data.

The input archive contains exact saved database records and a declared exact-line GAF subset, not article bodies. `source-objects.json` provides the preserved annotation identities used by the join. Record numbers are one-based physical TSV lines; annotation indices are zero-based. An aggregate source row without a partner remains a publication aggregate. The identical-protein row requires Q15125 on both sides. A matched interactor sequence does not establish a full-length experimental fusion or a native physiological interaction. Nine IntAct-only clone-side occurrences have no verified official sequence and are explicitly unresolved.

`partner-classes.md` records the separate manual functional assessment and official authority links. It is not a computational function prediction. `results.json` preserves every selected raw TSV field, including constructs, taxon, assay and record identifiers, so the positive-pair scope can be independently inspected. The algorithm does not assign paper-wide orthogonal benchmarking to a particular pair.
