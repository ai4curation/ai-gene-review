# DRC4 factual source extract

This package makes the exact interaction, localization and phylogenetic records reviewable. It contains no generated annotation verdicts.

| File | Role |
|---|---|
| `selection.json` | The 112 imported IPI assertions and seven IBA assertions selected from the frozen DRC4 seed. Source indices are zero-based. |
| `source-manifest.json` | Public URLs, capture times and SHA-256 hashes for 18 genuine raw inputs. |
| `reproduce.py` | Standard-library parser and checksum verifier; no network calls or credentials. |
| `target-data.json` | Derived pair records, direction, parent ROGIDs, sufficient-binding-region features, seven IBD joins, target path and HPA samples/image URLs. |
| `partner-class-definitions.json` | Unmodified current official GO response for the four bounded class definitions. |
| `partner-class-definitions-source.json` | URL, date and hash for that ontology response. It is independent of the extractor inputs. |

Supply the raw files under the names in `source-manifest.json`, then run:

```sh
python3 reproduce.py --input-dir /path/to/raw-inputs --output /tmp/DRC4-target-data.json
```

Alternatively, use `--input-map /path/to/inputs.json`, where the JSON object maps each manifest input name to an absolute saved file path. The saved-input handoff includes that map. The script resolves `selection.json` and `source-manifest.json` alongside itself; it does not depend on the current working directory.

Compare the resulting file with `target-data.json`. The accepted reproduction reports 18 inputs, 112 binding source rows, 110 rows with matching current IntAct records, seven PAINT contexts and three HPA assay groups. All 109 HuRI pairs match; the other match is BioPlex KRT27. The two unmatched source pairs, SMO and DRC1, are supported by separately read original experiments and are not treated as absent interactions.

The full IntAct capture has 340 records. Each selected source may have multiple records. Physical IntAct line numbers are one-based in the original headerless TSV. Parent-sequence checksums authenticate the reference sequence and do not prove that a construct includes every residue when a separate binding-region feature is recorded. The extract preserves both facts.

Use the [source guide](../DRC4-source-evidence.md) for human/ortholog and assay limits. The raw file URLs are genuine acquisition routes, but mutable public endpoints may no longer return the captured version. A hash mismatch is a reproducibility limitation to resolve with the archived file, not a reason to alter a checksum or invent source content.
