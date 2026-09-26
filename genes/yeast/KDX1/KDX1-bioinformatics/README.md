# KDX1 catalytic-motif coordinate check

This small comparison resolves whether the lysine at KDX1 position 55 is the
canonical beta3 ATP-site lysine of its characterized comparator SLT2. It also maps
the catalytic-loop, DFG and activation-loop positions cited in the review.

Run from this directory:

```bash
just all
```

The repository's `pyproject.toml` and `uv.lock` supply Python and **Biopython 1.85**;
no separate environment is needed. Analysis used Python 3.12.9. The generic script
accepts input records, formats and reference coordinates as arguments. It uses a
global BLOSUM62 alignment with gap-open -10 and gap-extension -0.5; output includes
input and sequence hashes, parameters, coordinate mappings and complete alignment.

`data/` holds exact source snapshots and `provenance.json`; `results/` holds direct
script outputs. `just refresh-inputs` retrieves the current UniProt comparators and
copies the cached target. Refreshing can change the inputs, so inspect record
versions and new output hashes against the saved provenance before interpreting.

Q00772 is SLT2/MPK1. P41808 is **SMK1**, not SLT2; it is used solely as an independent
second input to check script reuse. The analysis verifies coordinate correspondence
and sequence changes. It does not infer PAINT node membership, prove orthology,
measure ATP binding, or directly assay kinase activity. See [RESULTS.md](RESULTS.md)
for the evidence-limited interpretation.
