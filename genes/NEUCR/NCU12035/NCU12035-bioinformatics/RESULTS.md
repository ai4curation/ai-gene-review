# NCU12035 (V5ILC0) bioinformatics checks (2026-10-21)

Script: `gnat_motif_check.py` (run with `uv run --script gnat_motif_check.py`). Output is reproduced below; nothing is hand-entered.

```
length=232
GNAT domain (PROSITE PS51186) = 3..184
motif A candidate RRMGVG at 107-112 inside_domain=True
C-terminal tail 185..232 (48 aa): IQPGMERVLWIKSLPPRLGSKRYDDSTPPSDESTPKSYGWPSLRRLLL
S+T+P fraction in tail = 0.33
max KD hydropathy (19-aa window) = 1.73 starting at 50 (values >1.6 suggest a TM helix)
```

## Interpretation

- The GNAT domain covers residues 3-184 of 232, so the protein is a full-length single-domain GNAT, not a fragment.
- One acetyl-CoA pyrophosphate-binding motif A match, R107-R-M-G-V-G112, sits inside the domain in the expected position for the beta4-alpha3 loop of GNAT folds. This supports retained acyl-CoA binding. The script does not test the catalytic base or the acceptor-binding residues, which vary across the superfamily.
- The 48-residue C-terminal tail is S/T/P-rich (33%) and has no recognised domain.
- The single window above the crude Kyte-Doolittle threshold (start 50, LLNLCLIKGMLWVAVAKLA) lies within the GNAT core, where hydrophobic beta strands are expected. UniProt records no Phobius transmembrane or SignalP feature for this entry, so the protein is not predicted to be membrane-anchored or secreted. Location remains unassigned.

## Orthology (queried 2026-10-21)

- InterPro API: no PANTHER family or subfamily is assigned to V5ILC0; member signatures are only the generic GNAT ones (PF00583, PS51186, cd04301, SSF55729, G3DSA:3.40.630.30, IPR000182, IPR016181).
- OrthoDB v12 group 1321247at2759 (the Eukaryota-level group returned for V5ILC0) contains 4 genes from 4 genomes, all in *Neurospora* (N. crassa NCU12035 and GE21DRAFT_9904; N. tetrasperma NEUTE1DRAFT_147790 and NEUTE2DRAFT_116227). No characterised ortholog exists, and the absence of a PANTHER placement leaves no phylogenetic basis for transferring a substrate-specific function from another GNAT.
