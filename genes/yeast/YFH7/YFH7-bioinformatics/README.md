# YFH7 bioinformatics

Reproducible analysis of *S. cerevisiae* YFH7 (P43591 / YFR007W), an atypical
P-loop ATP-dependent kinase. See `RESULTS.md` for findings and `justfile` for the
pipeline (`just all`, `just test-controls`).

Scripts (all take FASTA/accession as arguments — no hardcoded gene data):
- `analyze_motifs.py` — Walker A/B & P-loop motif scan
- `analyze_domains_orthology.py` — domain architecture + orthology cross-refs
- `analyze_conservation.py` — taxonomic span via UniRef clusters
- `compare_urk_motifs.py` — PRK/URK/PANK family motif comparison
