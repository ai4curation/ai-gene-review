# Recheck of the provider's hydropathy artifact

Run `just` in this directory. Python 3.12 standard library only; no third-party dependencies. Inputs are the untouched repository UniProt snapshots, with exact file and sequence hashes emitted in each output. The second input verifies reuse on an unrelated protein rather than embedding an A1BG result.

The Kyte–Doolittle amino-acid scale, 19-residue window and threshold 1.6 reproduce the method in `../A1BG-hypotheses/membrane-receptor-and-growth-hormone-capacities/openscientist_artifacts/provenance_a1bg_hydropathy.json`. The threshold is a heuristic chosen by the provider, not a universal membrane-localization classifier. The region-start parameter restricts only the reported regional maximum; the complete profile and all threshold crossings are retained. See RESULTS.md for biological limits.
