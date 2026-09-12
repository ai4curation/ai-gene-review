# SET6 (YPL165C / Q12529) bioinformatics

Custom analysis of whether *S. cerevisiae* SET6 is a catalytically competent
SET-domain protein-lysine methyltransferase (SMYD subfamily) or a degenerate
pseudo-methyltransferase.

**See [`RESULTS.md`](RESULTS.md) for findings and the reproducibility checklist.**

## Run

Requires `uv`, `mafft`, HMMER (`hmmsearch`, `hmmalign`), and `curl`.

```bash
just all        # fetch -> HMM -> hmmsearch -> motifs -> identity
# or individual steps:
just fetch
just hmm
just hmmsearch
just motifs
just identity
```

## What each script does
- `scripts/fetch_sequences.py` — reads SET6 from the cached UniProt record and fetches a
  reference panel (yeast Set1-5, human SMYD1/2/3, SETD6) from UniProt REST.
- `scripts/motif_from_mafft.py` — MAFFT MSA, then reads each protein's residues at the
  SET6 catalytic / SAM-binding motif columns.
- `scripts/analyze_set_motifs.py` — alternative hmmalign-based read-out (secondary;
  `--trim` collapses SMYD split-SET inserts, so the MAFFT script is primary).
- `scripts/pairwise_identity.py`, `scripts/set_domain_identity.py` — % identity vs panel
  (full-length and SET-domain-restricted).

No conclusions are hardcoded in any script; all interpretation lives in `RESULTS.md`.
