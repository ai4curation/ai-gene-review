# CG43124 catalytic-residue mapping

Run `just` in this directory with Python 3.12+ and HMMER 3.4 (`hmmalign`, `hmmsearch`). Python uses only its standard library. Inputs are cached for reproducibility; `python fetch_inputs.py` refreshes public comparator/profile data and re-extracts the target from the frozen benchmark. Refreshing changes the input versions and requires re-evaluation.

The script maps annotated active sites from UniProt records through a common Pfam Trypsin profile. It makes no biological decisions. The positive control changes the target to experimentally characterized bovine trypsin; the other comparator is the actual ProtNLM phmmer donor, toad ovochymase-2. Full donor sequence has two trypsin domains; `hmmalign` aligns its first domain, containing the source-record catalytic triad. Inspect `hmmsearch.txt` for domain boundaries and coverage; do not interpret a gap in a poorly aligned region as a proven residue deletion.

Sources: https://www.ebi.ac.uk/interpro/entry/pfam/PF00089/ ; https://rest.uniprot.org/uniprotkb/P00760.json ; https://rest.uniprot.org/uniprotkb/Q90WD8.json . Retrieved 2026-09-08. HMM PF00089.33; exact hashes are in `results/results.json`.
