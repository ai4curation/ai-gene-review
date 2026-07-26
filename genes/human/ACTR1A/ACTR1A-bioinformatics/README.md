# ACTR1A bioinformatics

One analysis, answering one curation question: does human ACTR1A (Arp1) retain
actin's nucleotide site and actin's polymerisation interface, and does its
non-polymerising paralog ACTR10 (Arp11)?

```bash
uv run python analyze_arp1_actin_fold.py
```

Writes `RESULTS.md` and `results.json` (both overwritten on each run — do not
hand-edit). Inputs are fetched into `cache/`, which is gitignored: UniProt FASTA
for ACTB/ACTR1A/ACTR1B/ACTR10, PDB 2BTF (beta-actin with ATP) and PDB 9B85 (the
human dynactin cryo-EM structure). Every residue position in the output is
derived from coordinates or from an alignment computed at run time; no residue
list is hard-coded, and a missing input is a hard error rather than a silently
degraded report.
