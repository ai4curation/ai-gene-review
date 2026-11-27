# A0A674PKV4 (Takifugu gas7a) gene-model and domain comparison (re-review, 2026-10-21)

Script: `compare_isoforms_rereview.py` (run with `uv run python compare_isoforms_rereview.py`);
raw output in `compare_isoforms_rereview.out`.

Inputs (fetched from rest.uniprot.org on 2026-10-21):
- `fugu_gas7.fasta`: all Takifugu rubripes UniProt entries with gene name gas7/gas7a/gas7b
  (A0A674NLH4, A0A674NVV7, A0A674PKV4). All three are unreviewed TrEMBL entries and all
  three map to the same Ensembl gene ENSTRUG00000029588 (transcripts ENSTRUT00000080391,
  ENSTRUT00000068268 and ENSTRUT00000065002 respectively). All three are classified in
  PANTHER PTHR23065:SF57 (GROWTH ARREST-SPECIFIC PROTEIN 7).
- `human.fasta`: human GAS7 O60861 (476 aa, isoform 3 displayed; SH3 1-62, WW 77-110,
  F-BAR 196-456 per UniProt).
- `mouse.fasta`: mouse Gas7 Q60780 (421 aa).

## Results

| Fugu entry | Length | Aligned to human O60861 | Identity (of aligned) | Human span covered |
|---|---|---|---|---|
| A0A674PKV4 | 401 | 385 | 72.5% | 43-476 |
| A0A674NVV7 | 392 | 365 | 71.2% | 109-476 |
| A0A674NLH4 | 357 | 356 | 73.6% | 105-476 |

Versus mouse Q60780, A0A674PKV4 aligns over 372 residues with 73.9% identity, spanning
mouse residues 1-421.

A regular-expression scan for the WW-domain tryptophan spacing (W, 20-22 residues, W, two
residues, P) finds the WW motif in human GAS7 (start 83) and mouse Gas7 (start 28), but
finds no such motif in any of the three fugu gene models.

## Interpretation

- A0A674PKV4 is the longest of three alternative Ensembl transcript models of a single
  fugu gas7a gene; none of the three is a reviewed or canonical UniProt entry. It covers the
  WW-FCH linker and the complete F-BAR domain to the C-terminus of human GAS7, and has an
  extra N-terminal segment (residues ~1-90) that aligns only poorly with the human
  SH3/WW region. It does not contain an SH3 domain and has no canonical WW motif by this
  scan, so the GAS7 WW-dependent N-WASP interaction described for mouse Gas7 cannot be
  assumed for this model.
- No residues follow the F-BAR domain beyond ~20 aa, so like all GAS7 proteins it lacks
  any mu-homology domain (muHD) or AP-2-activating linker of the FCHO1/FCHO2 muniscins.
- The motif scan is a simple heuristic; a degenerate WW domain could exist below its
  sensitivity. Pfam reports only the WW_FCH_linker (PF16623), not PF00397 WW.
