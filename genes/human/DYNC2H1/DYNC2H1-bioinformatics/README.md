# Saved DYNC2H1 evidence replay

Requirements: Python 3.9 or later, standard library only. No network, credentials or external executables are needed.

From any working directory:

```bash
python3 /path/to/DYNC2H1-bioinformatics/replay.py --check
```

To recompute the four JSON outputs in another directory:

```bash
python3 /path/to/DYNC2H1-bioinformatics/replay.py --output /tmp/dync2h1-replay
```

The script verifies the compressed archive and every member against `source-manifest.json`, then independently computes PAINT lineage/IBD joins, Reactome paths, interaction/sequence matches and the urinary-exosome target row. It reads archive members in memory without extracting files. `--check` compares the computed objects with `outputs/` and writes nothing.

`inputs.tar.gz` contains 26 exact saved inputs. Most are unmodified official/source payloads: PANTHER tree and MSA, PAINT IBD GAF, UniProt JSON, IntAct MITAB, Reactome JSON and the original-linked NHLBI identification table. Two inputs are explicitly derived: source dictionaries exported from the preserved review supply query selectors, and the product inventory supplies independently reconstructed official sequences for ROGID checks. The manifest records source URLs, byte counts, SHA256 hashes and available retrieval dates. Live service responses may change; the bundled bytes make this execution reproducible.

The output is a record reconstruction, not an automatic biological classifier. In particular, a real ancestral IBD does not settle the biological appropriateness of every propagated term; an association record does not establish every physiological role; and an exosome protein identification does not establish secretion or isoform specificity. See [RESULTS.md](RESULTS.md) and the [source guide](../DYNC2H1-source-guide.md).

The supplementary publication workbooks are not included: their literal target-name survey supplements the manually inspected antibody Methods and Figure 4 caption and is not needed to replay these four database analyses. No publication body or provider-generated narrative is bundled.
