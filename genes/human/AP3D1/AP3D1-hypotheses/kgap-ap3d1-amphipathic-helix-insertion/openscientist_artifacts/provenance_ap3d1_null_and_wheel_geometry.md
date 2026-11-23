# Calibration of the AP3D1 N-terminal helix against a proteome null, and helical-wheel geometry

All numbers below were computed in this job. Sequences were streamed live from the
UniProt REST API; the AlphaFold model was downloaded from the AlphaFold DB API.

## Table 1. Human proteome null for N-terminal hydrophobic moment

Null set: all reviewed human UniProt entries with length >= 24 aa (n = 20,396).
Metric: Eisenberg consensus hydrophobic moment per residue, 100 deg/residue.

| Window | median | p75 | p90 | p95 | p99 | AP3D1 value | AP3D1 percentile | empirical P(muH >= obs) |
|---|---|---|---|---|---|---|---|---|
| first 14 aa | 0.210 | 0.306 | 0.407 | 0.471 | 0.600 | 0.464 | 94.6 | 0.054 |
| first 24 aa | 0.165 | 0.238 | 0.314 | 0.364 | 0.460 | 0.421 | 98.0 | 0.020 |

Benchmarks placed on the same "first 24 aa" null:

| Helix | muH | percentile |
|---|---|---|
| ApoA-I class A 220-241 (surface-binding control) | 0.418 | 97.9 |
| epsin-1 H0 1-18 (inserting) | 0.395 | 96.9 |
| ArfGAP1 ALPS1 (curvature sensor) | 0.384 | 96.3 |
| Sar1A 1-23 (deep insertion) | 0.328 | 91.6 |
| GMAP210 ALPS | 0.321 | 90.8 |
| amphiphysin-1 H0 (inserting) | 0.310 | 89.5 |
| AP1G1 1-24 (paralog control) | 0.273 | 83.2 |
| AP2A1 1-24 (paralog control) | 0.197 | 62.2 |

The surface-binding control and AP3D1 are indistinguishable on this metric, and the
deep inserter Sar1A scores lower than both. Hydrophobic moment alone does not
discriminate insertion depth.

## Table 2. Helical-wheel geometry (100 deg/residue)

apolar_arc = angular width spanned by apolar residues (A,V,L,I,M,F,W,C,Y).
Angles for Lys/Arg and Asp/Glu are measured from the hydrophobic-moment direction
(0 deg = centre of the hydrophobic face, 180 deg = centre of the polar face).

| Helix | sequence | apolar arc (deg) | mean abs angle Lys/Arg | mean abs angle Asp/Glu |
|---|---|---|---|---|
| AP3D1 1-14 | MALKMVKGSIDRMF | 220 | 123.9 | 131.8 |
| AP3D1 1-18 | MALKMVKGSIDRMFDKNL | 260 | 115.0 | 132.2 |
| AP3D1 1-24 | MALKMVKGSIDRMFDKNLQDLVRG | 320 | 122.4 | 102.6 |
| epsin-1 H0 1-18 | MSTSSLRRQMKNIVHNYS | 220 | 132.5 | none |
| amphiphysin-1 H0 1-27 | MADIKTGIFAKNVQKRLNRAQEKVLQK | 340 | 129.2 | 75.3 |
| ArfGAP1 ALPS1 | MSSLYSGWSSFTTGASRFASAAK | 200 | 120.0 | none |
| Sar1A 1-23 | MSFIFEWIYNGFSSVLQFLGLYK | 240 | 79.9 | 179.9 |
| ApoA-I class A 220-241 | ATEHLSTLSEKAKPALEDLRQG | 100 | 101.1 | 148.3 |
| Apl5 yeast 1-24 | MTSLYAPGAEDIRQRLRPFGFFFE | 300 | 105.3 | 132.0 |

Reading: AP3D1 1-14 has the wide apolar arc of a membrane-binding helix and is not the
narrow-arc, charge-polarised class-A architecture of the ApoA-I control. Its arc and
basic-residue placement are closest to epsin-1 H0. It lacks the Sar1A signature of a
single snorkelling Lys at 80 deg with the acidic residue at the polar-face centre.

## Table 3. AlphaFold DB model AF-O14617-F1 (v6)

| Region | mean pLDDT |
|---|---|
| residues 1-14 | 48.3 |
| residues 15-17 | 76.3 |
| residues 18-60 | 91.3 |
| residues 18-600 | 90.5 |
| whole chain 1-1153 | 76.7 |

Per-residue pLDDT 1-25: M1 45, A2 45, L3 47, K4 49, M5 46, V6 49, K7 49, G8 50, S9 46,
I10 50, D11 50, R12 50, M13 46, F14 55, D15 64, K16 78, N17 87, L18 89, Q19 91, D20 90,
L21 91, V22 91, R23 91, G24 89, I25 90.

CA(i) to CA(i+4) distances in the AlphaFold model: 6.00-6.90 A over residues 1-11
(helical), 8.84 / 10.12 / 12.64 / 11.35 A at residues 12-15 (break), 5.52-6.50 A from
residue 16 (trunk helix). This reproduces the two-helix architecture seen in cryo-EM
structure 9C59. There are 81 heavy-atom contacts closer than 5 A between residues 1-17
and residues 40 onward, but at pLDDT 48 that placement is not interpretable.
