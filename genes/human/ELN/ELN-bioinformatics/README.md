# ELN database evidence replay

Run from this directory, or pass the script's path from another directory:

```sh
python3 reproduce.py
```

Python 3.9 or later and its standard library are sufficient. No network access,
repository checkout, package installation or pre-existing extraction directory is
needed. The replay reads adjacent files using the script's location and writes
only into an automatically removed temporary directory.

- `reproduce.py` contains all executable reconstruction and verification logic.
- `results.json` is the unchanged expected database projection previously stored
  as `expected-projection.json` inside the archive. It is compared with values
  freshly derived from the saved inputs, not printed as a substitute for them.
- `input-manifest.json` lists the exact 99 input paths, SHA-256 hashes, sizes and
  modes. These are 95 official database/sequence/receipt files and four frozen
  source/context/product records.
- `database-evidence.tar.gz` contains only those 99 inputs. Every input's bytes
  and mode are unchanged from the original published archive.
- `archive-manifest.json` binds the archive and the two visible JSON files.
- `RESULTS.md` records the scope and limits of the reconstruction.

Before writing any input, the replay verifies the archive hash and its entire
member set, hashes, sizes and modes. It rejects unexpected, duplicate, traversal,
absolute, non-regular and sparse members. It never executes code from the archive.
The hash records detect inconsistency; they are not a digital signature or a
substitute for reviewing the code and the underlying evidence.

The replay reconstructs 48 source objects against 50 raw contexts, eight Reactome
source-event paths to human P15502, literal mouse-donor joins, 13 official product
sequence checks and the saved typed ontology edges. Unexpanded branches remain
explicit. This is positive database/source/product evidence, not a proof of absent
paths, experimental equivalence of every product, or primary-paper assay results.
No article bodies, figures, supplements or provider output are bundled. Genuine
normal publication caches and the gene review are not changed by this packaging.
