# Shared FdeB panel analysis

This directory hosts one reusable analysis of **PP_3195 (PSEPK), Hsero_1004 (HERSS), and bll6428 (BRADU)**, compared with experimentally characterized Q93NG6. PP_3195 is the historical host directory, not the species scope or an experimentally characterized donor. Cross-species citations intentionally point to this shared workflow; a path under PSEPK must not be read as Pseudomonas-specific experimental evidence.

The generic `map_residues.py` takes query, positions, targets and output as arguments. The repository's `uv` environment supplies pinned dependencies (Biopython 1.85 in the recorded runs). `justfile` is the explicit input manifest. Derived tables are published at the species-neutral module-audit path `analysis/module_audits/bacterial_flavonoid_degradation/`. The README makes this ownership explicit without moving stable, previously cited analysis files or rewriting historical outputs.

From the repository root:

```sh
just --justfile genes/PSEPK/PP_3195/PP_3195-bioinformatics/fdeb-round2/justfile --working-directory . analyze
just --justfile genes/PSEPK/PP_3195/PP_3195-bioinformatics/fdeb-round2/justfile --working-directory . analyze-round3
```

The first command reproduces the historical round-2 maps. The second creates separate round-3 maps including Q93NG6 E148 and its PP_3195 counterpart D195. `RESULTS.md` separates the two rounds, source evidence from predictions, and candidate correspondence from demonstrated catalytic residues. No sequence alignment establishes substrate identity, native pathway participation or target active-site geometry.
