# Nepl15 catalytic-site and topology check (2026-10-21)

Script: `active_site_topology.py` (run with `uv run python active_site_topology.py`).
Outputs: `input.fasta`, `aln.fasta`, `results.json`. Sequences come from UniProt REST; alignment is MAFFT
L-INS-i. Positions of human neprilysin (MME, P08473) functional residues are taken from UniProt features.

## Sequences

Nepl15 Q9VCU1 (686 aa, FlyBase FBgn0039024 reference-proteome entry) was aligned with its 94C4 tandem
neighbours Nepl14 Q9VCU2 and Nepl13 Q9VCU3 (both PANTHER PTHR11733:SF240), the SF238 members Nepl19
Q9VAS1 and Nep4 Q8T062, fly Nep2 A0A0B4K692 (SF224) and human MME P08473. The cDNA-derived entry Q95U74
for the same gene differs from Q9VCU1 at a single position (673, R vs M).

## Catalytic and zinc-binding residues

| MME residue (role) | Nepl15 | Nepl19 | Nep4 | Nep2 |
|---|---|---|---|---|
| H584 (Zn ligand) | R521 | Q511 | H872 | H609 |
| E585 (catalytic Glu) | Q522 | Q512 | E873 | E610 |
| H588 (Zn ligand) | H525 | H515 | H876 | H613 |
| E647 (Zn ligand, ENIAD) | R582 | E560 | E934 | E671 |
| D651 (UniProt active site) | D586 | D564 | D938 | D675 |
| R103 (peptide binding) | R80 | R99 | G300 | S130 |

The HExxH window aligned to MME HEITH 584-588 reads RQMLH in Nepl15. Two of the three zinc ligands
(H584 and E647) are replaced by arginine, and the catalytic glutamate is replaced by glutamine. This
reproduces the description in PMID:33483521. Nep4 and Nep2 keep all of these residues.

The 94C4 tandem neighbours Nepl14 (QQLVM) and Nepl13 (SALVQ) have also lost the motif, but they are in a
different PANTHER subfamily (SF240).

## Topology

The Kyte-Doolittle scan (window 19, threshold 1.6) finds hydrophobic windows only at the N terminus
(window starts 1-8), which matches the SignalP signal peptide at 1-22. After residue 40 the highest window
mean is 0.97, so the sequence has no second hydrophobic segment that could act as a transmembrane anchor.
The C terminus ends in the M13 domain (…NAYGCSREEKLNARFKCTLY). The sequence therefore predicts a secreted
protein, not a type II membrane protein.

## Identity

Nepl15 percent identity over aligned columns: Nepl19 27.9, Nep4 26.5, human MME 24.9, Nepl14 24.0,
Nepl13 22.8, Nep2 22.0.

## Interpretation

Nepl15 keeps the M13 fold but has lost the zinc-coordinating and catalytic residues. It is predicted to
be a secreted, non-catalytic M13 protein. These findings are sequence-based predictions. No peptidase
assay, localisation experiment or ligand-binding experiment exists for the protein.
