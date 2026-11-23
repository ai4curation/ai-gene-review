# Provenance: contact positions measured from DNA-bound homeodomain structures, and superposition of the ADNP2 model onto 9ANT

Run 2026-11-23 in the job's `execute_code` Python executor. Structures downloaded from
`https://files.rcsb.org/download/<ID>.pdb`, the ADNP2 model from the AlphaFold DB API. PDB parsing,
Needleman-Wunsch alignment and Kabsch superposition are written out below because Biopython is not
installed in this executor.

This answers the part of the seed hypothesis that asked to "align the ADNP2 homeodomain to DNA-bound
homeodomain structures and score the residues that contact DNA bases and backbone". In iteration 1
the contact positions came from the homeodomain literature. Here they are measured.

## Cell A: which canonical positions actually touch DNA

Method. For each entry, every chain was parsed, amino-acid chains were aligned to the Antennapedia
1-60 reference by affine-gap Needleman-Wunsch with BLOSUM62, and chains below 22 % identity or with
fewer than 45 mapped positions were dropped. Nucleotide atoms were split into base atoms and
sugar-phosphate atoms (`P OP1 OP2 OP3 O1P O2P O3P O5' C5' C4' O4' C3' O3' C2' C1' O2'`). For each
mapped residue the minimum heavy-atom distance to each atom class was computed and scored as a
contact at 4.0 Angstrom. Duplicate identical chains within one entry were counted once.

### Output

```
1HDD  399 DNA-base atoms, 456 backbone atoms, homeodomain chains used: [('C', 0.48)]
9ANT  570 DNA-base atoms, 648 backbone atoms, homeodomain chains used: [('A', 0.92)]
1FJL  398 DNA-base atoms, 453 backbone atoms, homeodomain chains used: [('A', 0.38), ('B', 0.38), ('C', 0.38)]
1B72  380 DNA-base atoms, 434 backbone atoms, homeodomain chains used: [('A', 0.62), ('B', 0.3)]
1PUF  380 DNA-base atoms, 434 backbone atoms, homeodomain chains used: [('A', 0.68), ('B', 0.28)]
1NK2  6080 DNA-base atoms, 6920 backbone atoms, homeodomain chains used: [('P', 0.42)]
1IG7  274 DNA-base atoms, 316 backbone atoms, homeodomain chains used: [('A', 0.47)]
1VND  no DNA in file
1OCT  285 DNA-base atoms, 324 backbone atoms, homeodomain chains used: [('C', 0.37)]
5EDN  1444 DNA-base atoms, 1672 backbone atoms, homeodomain chains used: [('A', 0.48), ('B', 0.48), ('G', 0.47)]
1AKH  399 DNA-base atoms, 456 backbone atoms, homeodomain chains used: [('B', 0.33)]
3A01  646 DNA-base atoms, 736 backbone atoms, homeodomain chains used: [('A', 0.48), ('B', 0.47), ('E', 0.47), ('F', 0.47)]
1LFB  no DNA in file
2HDD  399 DNA-base atoms, 456 backbone atoms, homeodomain chains used: [('A', 0.45), ('B', 0.47)]
1ZQ3  4940 DNA-base atoms, 5600 backbone atoms, homeodomain chains used: [('P', 0.42)]
6A5V  2876 DNA-base atoms, 3330 backbone atoms, homeodomain chains used: [('A', 0.53), ('B', 0.38), ('F', 0.25), ('G', 0.23), ('H', 0.25), ('d', 0.25), ('h', 0.23)]
1YZ8  4940 DNA-base atoms, 5600 backbone atoms, homeodomain chains used: [('P', 0.42)]
1K61  390 DNA-base atoms, 448 backbone atoms, homeodomain chains used: [('A', 0.3), ('B', 0.3), ('C', 0.27), ('D', 0.28)]

homeodomain chains analysed: 35

pos  base_n  base_frac  bb_n  bb_frac  literature_class
  5     23      0.66    25     0.71  BASE
  6      4      0.11    26     0.74  -
  8      0      0.00    26     0.74  -
 25      1      0.03    28     0.80  backbone
 31      0      0.00    19     0.54  backbone
 44      0      0.00    27     0.77  -
 46      7      0.20    18     0.51  -
 47     26      0.74    12     0.34  BASE
 48      0      0.00    25     0.71  -
 50     20      0.57    14     0.40  BASE
 51     27      0.77     4     0.11  BASE
 53      1      0.03    26     0.74  backbone
 54      9      0.26     9     0.26  BASE
 55      3      0.09    22     0.63  backbone
 57      0      0.00    23     0.66  backbone

empirical base-contact set (>=40% of chains): [5, 47, 50, 51]
literature base set used in iteration 1:        [3, 5, 47, 50, 51, 54]
empirical backbone-only set (>=60%):           [6, 8, 25, 44, 48, 53, 55, 57]
literature backbone set used in iteration 1:    [25, 28, 31, 53, 55, 57]
```

Four of the six literature base positions are confirmed at high frequency. Position 54 reaches only
0.26 and position 3 passes neither threshold, so neither is used in the structure-derived scoring
below. Position 3 is not resolved in several of these entries (9ANT chain A, for example, covers
canonical 5-60 only), so its measurement here is not reliable either way. Position 48, the invariant
Trp, is a phosphate-backbone contact in 71 % of chains, which is more than a purely core role.

## Cell B: rescoring with the structure-derived positions

The 240 register-corrected human homeodomains from
`provenance/adnp2_contact_analysis_run.md` were rescored, holding ADNP2 and ADNP out of the
background as before.

```
empirical base set [5, 47, 50, 51]  (n positions = 4)
  consensus matches:  ADNP2 0/4 | ADNP 1/4 | background 2.94 +/- 1.11
  log-odds: background 12.2 +/- 5.8 | ADNP2 -13.0 (z -4.31, pct 0.0) | ADNP -4.1 (z -2.78, pct 5.4)

empirical base+backbone set [5, 6, 8, 25, 44, 47, 48, 50, 51, 53, 55, 57]  (n positions = 12)
  consensus matches:  ADNP2 2/12 | ADNP 4/12 | background 8.39 +/- 2.49
  log-odds: background 36.6 +/- 13.0 | ADNP2 -21.5 (z -4.45, pct 0.0) | ADNP -13.3 (z -3.82, pct 0.4)

residues at the structure-derived base positions:
   pos  5  consensus R (0.875)  Antp R  ADNP E  ADNP2 E
   pos 47  consensus I (0.421)  Antp I  ADNP S  ADNP2 S
   pos 50  consensus Q (0.725)  Antp Q  ADNP S  ADNP2 G
   pos 51  consensus N (0.921)  Antp N  ADNP N  ADNP2 K
```

ADNP2 holds the lowest score in the set on both position sets. ADNP falls to the 0.4 percentile on
the 12-position set, mainly because of His at position 48 where 97.5 % of human homeodomains have
Trp. The difference between the paralogs reduces to Asn51 and to the Pfam and PROSITE matches.

## Cell C: superposition onto the Antennapedia-DNA complex

A first attempt mapped 9ANT chain A to canonical numbering with
`seqA.find(ANTP[:12])`, which returned -1 because that chain starts at canonical position 5. The
resulting distance table was shifted by three positions and is discarded. The corrected version
locates the chain by scanning the 1-60 reference for an ungapped window with at most two mismatches,
and prints an explicit check.

```python
ant = requests.get("https://files.rcsb.org/download/9ANT.pdb", timeout=120, headers=H).text
prot, dbase, dback = parse(ant)
chA = prot["A"]; nums = sorted(chA)
seqA = "".join(chA[k][0] for k in nums)
start = None
for s0 in range(0, 61 - len(seqA) + 1):
    win = ANTP[s0:s0+len(seqA)]
    if len(win) == len(seqA) and sum(a != b for a, b in zip(win, seqA)) <= 2:
        start = s0 + 1; break
ant_map = {start + i: nums[i] for i in range(len(seqA))}

af = requests.get("https://alphafold.ebi.ac.uk/api/prediction/Q6IQ32", timeout=120, headers=H).json()
afprot, _, _ = parse(requests.get(af[0]["pdbUrl"], timeout=180, headers=H).text)
afch = list(afprot.values())[0]
a2_map = {p: 1042 + p for p in range(1, 61)}        # residues 1043-1102 are canonical 1-60

CORE = [p for p in range(max(7, start), 58) if p in ant_map]     # the three helices
P  = np.array([ca(afch, a2_map[p]) for p in CORE])
Qm = np.array([ca(chA,  ant_map[p]) for p in CORE])
pmu, qmu = P.mean(0), Qm.mean(0)
U, Sv, Vt = np.linalg.svd((P - pmu).T @ (Qm - qmu))
R = U @ np.diag([1, 1, np.sign(np.linalg.det(U @ Vt))]) @ Vt
rmsd = np.sqrt((((P - pmu) @ R + qmu - Qm)**2).sum(1).mean())
def xf(x): return (np.array(x) - pmu) @ R + qmu
```

### Output

```
9ANT chain A, 56 residues: RQTYTRYQTLELEKEFHFNRYLTRRRRIEIAHALSLTERQIKIWFQNRRMKWKKEN
canonical start position: 5  -> covers canonical 5-60
check: canonical 48/49/50/51 in 9ANT = WFQN (expect WFQN)
DNA atoms in 9ANT: 570 base, 648 sugar-phosphate
AlphaFold model AF-Q6IQ32-F1-model_v6.pdb, residues 1043-1102 match UniProt: True

Kabsch superposition, CA of canonical 7-57: n=51, RMSD = 2.36 A

minimum heavy-atom distance to DNA in the 9ANT frame (Angstrom)
pos class     Antp  d_base d_bb  |  ADNP2  d_base d_bb
  5 base      R       2.2   3.3  |  E      21.4  16.9
  6 backbone  Q       6.4   2.9  |  G      20.7  15.3
  8 backbone  Y       6.7   2.9  |  S      15.0  10.1
 25 backbone  Y       7.6   2.5  |  Y      10.1   5.0
 31 other     R       7.9   3.2  |  I       9.4   4.8
 44 backbone  Q       7.7   3.0  |  D       6.0   2.9
 47 base      I       3.6   4.3  |  S       3.9   5.6
 48 backbone  W       6.7   3.5  |  F       6.9   3.7
 49 other     F       8.4   5.5  |  F       8.7   5.3
 50 base      Q       3.6   4.3  |  G       6.1   4.0
 51 base      N       3.1   4.7  |  K       3.5   3.5
 53 backbone  R       5.9   2.4  |  R       6.5   3.0
 54 other     M       4.3   3.3  |  Y       3.9   1.5
 55 backbone  K       7.9   4.0  |  I       7.5   6.6
 57 backbone  K       6.2   3.5  |  M       9.2   3.7

residues within 4 A of DNA, whole 60-mer
  Antennapedia in 9ANT         : 5 base-contacting, 14 backbone-contacting
  ADNP2 model, rigid-superposed: 3 base-contacting, 11 backbone-contacting

residues within 8 A of DNA: basic vs acidic
  Antennapedia : 12 K/R, 3 D/E
  ADNP2 model  : 10 K/R, 3 D/E
```

Reading of the numbers. The helical core superposes at 2.36 Angstrom and the recognition helix lands
where Antennapedia's lands, so the domain can be placed on B-DNA without steric conflict, and the
basic face is of comparable size (10 versus 12 Lys or Arg within 8 Angstrom). The chemistry at the
reading positions is gone: Gln50 becomes glycine, which removes the side chain at the specificity
position, and Asn51 becomes lysine, which reaches 3.5 Angstrom but cannot make the bidentate amide
hydrogen bond to the adenine of the TAAT core.

The N-terminal arm numbers (positions 5, 6, 8 at 15 to 21 Angstrom) are not evidence. They come from
a rigid placement of an apo prediction, and the arm is the part of a homeodomain that is disordered
without DNA. Only the helix-3 placement is informative here, because that is what drives the
superposition.

Figures: `provenance/plot_5.png` is from the shifted first attempt and is superseded.
`provenance/plot_6.png` is the corrected per-position distance comparison.
