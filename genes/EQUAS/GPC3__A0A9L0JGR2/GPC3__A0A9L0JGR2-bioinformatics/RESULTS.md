# GPC3 (donkey A0A9L0JGR2): ortholog comparison with human and mouse GPC3

## Question

Is the canonical donkey GPC3 product (A0A9L0JGR2, 580 aa) colinear with the experimentally
characterised human GPC3 (P51654) and mouse Gpc3 (Q8CFZ4), and does it keep the signal peptide and
the residues that the characterised functions depend on?

## Evolutionary placement (from the UniProt records, not computed here)

The donkey, human and mouse records all carry the PANTHER cross-reference PTHR10822:SF4 (GLYPICAN-3),
so the three proteins are in the same PANTHER subfamily. Donkey GPC3 is also Ensembl gene
ENSEASG00005018489 (UniProt DR line), the gene that encodes the alternative-first-exon model
A0A9L0J2B1 reviewed in `genes/EQUAS/GPC3/`.

## Method

`compare_orthologs.py` (PEP 723 script; Biopython) performs global alignments (BLOSUM62, gap open
-10, extend -0.5) of the donkey sequence against each ortholog. It maps the human P51654 feature
positions (SIGNAL 1..24, SITE 358..359, CARBOHYD 495 and 509, LIPID 554) onto the donkey sequence.
Run from this folder:

```
uv run --script compare_orthologs.py ../GPC3__A0A9L0JGR2-uniprot.txt human-GPC3-P51654.fasta mouse-Gpc3-Q8CFZ4.fasta
```

Sequence files were downloaded from the UniProt REST API on 2026-10-21 (the human files are copies
of those in `genes/EQUAS/GPC3/GPC3-bioinformatics/`).

## Output (compare_orthologs_output.txt)

```
Donkey A0A9L0JGR2 length 580

== vs P51654 (length 580) ==
Identical paired residues: 558/580 (96.21%)
Donkey residues 1..24: MAGTVHTACLVVAMLLSLDCPGQA
P51654 residues 1..24:    MAGTVRTACLVVAMLLSLDFPGQA
Signal-peptide positions 1..24 identical: 22/24
Human R358 (convertase cleavage site, P1 (SITE 358..359)) -> donkey R358
Human S359 (convertase cleavage site, P1' (SITE 358..359)) -> donkey S359
Human S495 (heparan sulfate attachment (CARBOHYD 495)) -> donkey S495
Human S509 (heparan sulfate attachment (CARBOHYD 509)) -> donkey S509
Human N554 (GPI-anchor amidated asparagine (LIPID 554)) -> donkey N554

== vs Q8CFZ4 (length 579) ==
Identical paired residues: 551/579 (95.16%)
Donkey residues 1..24: MAGTVHTACLVVAMLLSLDCPGQA
Q8CFZ4 residues 1..24:    MAGTVRTACLLVAMLLGLGCLGQA
Signal-peptide positions 1..24 identical: 19/24
```

## Interpretation

Donkey GPC3 A0A9L0JGR2 is the same length as human GPC3 and is 96.21% identical to it over its full length, with no internal indels.
The signal peptide differs at only 2 of 24 positions, and the convertase cleavage site, both heparan sulfate
attachment serines and the GPI-anchor asparagine are conserved at the same positions as in human GPC3.
The donkey UniProt record independently predicts a signal peptide at 1..24 (SignalP). The donkey
protein therefore has every sequence feature that the experimentally characterised human and mouse
GPC3 functions depend on. Whether those functions are carried out in donkey has not been tested
experimentally: no donkey GPC3 study was found, and all functional statements for this entry are
inferences from the PTHR10822:SF4 orthologs.
