# ACTRT2: does the actin fold still do actin things, and does the GO record hold up?

All numbers below are computed by `analyze_actrt2.py` from live UniProt, RCSB, QuickGO and
IntAct queries plus the repository's cached PANTHER PAINT table. Nothing is hardcoded from
a previous run or from a sibling review. Re-running the script reproduces this file.

- gene: **ACTRT2** (Q8TDY3, ACTT2_HUMAN, 377 aa)
- GOA rows analysed: 7 (`genes/human/ACTRT2/ACTRT2-goa.tsv`)
- contact cutoff: 4.0 A heavy-atom to heavy-atom

## 1. Nucleotide site: is actin's ATP pocket still there?

Contacts computed from **PDB 2BTF** chain A (ligands ATP, SR), 374 observed residues, giving **19 contact positions**.

Literature-named actin residues inside the computed contact set: D157, E214, G15, G156, K18, K336, Q137, S14, V159, Y306. Outside it (probed by alignment anyway): A108, D11, D154, H161, P109, R183.

**Sequence-length audit first, because a truncated reference manufactures fake substitutions.** The structure's observed chain is 374 residues; a panel member shorter than 280.5 residues (0.75 x the structure's observed chain length; the shortest unflagged panel member is 366 aa and the longest flagged is 245 aa, so the cut lies in an observed gap) is flagged as too short to contain the fold: **ACTL10 (human actin-like 10)** at 245 aa. Tallies for a flagged member are NOT comparable: gaps and apparent substitutions may reflect absent residues rather than divergence. No conclusion in this analysis rests on a flagged member, and that is asserted rather than claimed: `panel_length_audit` raises if a flagged accession appears in any of the argument-carrying reference sets (filament_builders, nucleators_not_polymerisers, pt_complex_arps), and it currently finds 0 such overlaps. Every table row carrying a flagged member's tally is marked - `**[TRUNCATED - not comparable]**` in the wide tables, `[TRUNC]` in the per-position table, whose cells are too narrow for the long form - and the number of marked rows is counted from the rendered tables at the end of this section rather than stated by hand.

Aligned residue at each named actin position:

| protein | D11 | S14 | G15 | K18 | A108 | P109 | Q137 | D154 | G156 | D157 | V159 | H161 | R183 | E214 | Y306 | K336 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACTRT2 | D | S | G | K | P** | S** | Q | D | G | D | V | C** | R | K** | F* | W** |
| ACTB | D | S | G | K | A | P | Q | D | G | D | V | H | R | E | Y | K |
| ACTG1 | D | S | G | K | A | P | Q | D | G | D | V | H | R | E | Y | K |
| ACTA1 | D | S | G | K | A | P | Q | D | G | D | V | H | R | E | Y | K |
| ACTC1 | D | S | G | K | A | P | Q | D | G | D | V | H | R | E | Y | K |
| Arp53D | D | S | G | K | A | P | Q | D | G | D | V | H | R | E | F* | R* |
| ACTR1A | D | S | G | K | A | P | Q | D | G | D | V | H | R | E | F* | L** |
| ACTR2 | D | T* | G | K | P** | P | Q | D | G | D | V | H | R | E | Y | K |
| ACTR3 | D | T* | G | K | P** | P | Q | D | G | D | V | H | R | E | F* | R* |
| ACTR10 | D | E** | A* | K | S** | V** | S** | D | G | Y** | E** | L** | K* | A** | L** | A** |
| ACTRT1 | D | S | G | K | P** | S** | H** | D | G | D | V | C** | R | E | L** | C** |
| ACTRT3 | D | S | G | K | P** | A** | Q | N** | G | A** | V | Q** | L** | E | F* | K |
| ACTL7A | D | T* | G | K | P** | P | Q | E* | G | H** | V | Y** | S** | K** | L** | D** |
| ACTL7B | D | S | Q** | K | P** | P | Q | E* | G | H** | V | H | G** | K** | L** | K |
| ACTL9 | D | T* | G | K | P** | P | Q | D | G | H** | V | Y** | N** | H** | F* | N** |
| ACTL10 [TRUNC] | -! | -! | -! | -! | -! | -! | T** | E* | G | A** | V | H | S** | K** | F* | G** |
| ACTL8 | D | S | G | K | T** | P | Q | D | G | Y** | L* | R* | Q** | M** | Y | N** |

(`*` conservative, `**` non-conservative, `!` gap; roles: D11 = phosphate-binding loop 1; S14 = phosphate-binding loop 1, beta-phosphate contact; G15 = phosphate-binding loop 1; K18 = phosphate-binding loop 1; A108 = Pro-rich loop; governs His161 flipping; P109 = Pro-rich loop; governs His161 flipping; Q137 = hydrogen-bonded to the attacking water W1; D154 = divalent cation coordination; G156 = phosphate-binding loop 2; D157 = phosphate-binding loop 2; V159 = phosphate-binding loop 2; H161 = ATP hydrolysis trigger; R183 = sensor loop / nucleotide state; E214 = adenosine region; Y306 = adenine pocket; K336 = adenine/ribose region.)

Scheme BLOSUM62/-11/-1:

| protein | % id (full length) | identical | conservative | non-conservative | gap |
|---|---|---|---|---|---|
| ACTB (human beta-actin; IBA donor) (P60709) | 100.0 | 19 | 0 | 0 | 0 |
| ACTG1 (human gamma-actin; IBA donor) (P63261) | 98.9 | 19 | 0 | 0 | 0 |
| ACTA1 (human alpha-skeletal actin; IBA donor) (P68133) | 93.6 | 18 | 1 | 0 | 0 |
| ACTC1 (human alpha-cardiac actin; IBA donor) (P68032) | 94.1 | 18 | 1 | 0 | 0 |
| Arp53D (Drosophila actin-like 53D; polymerising divergent actin; IBA donor) (P45891) | 64.4 | 16 | 3 | 0 | 0 |
| ACTR2 (human Arp2; Arp2/3 subunit) (P61160) | 48.7 | 16 | 3 | 0 | 0 |
| ACTRT3 (human actin-related protein T3 / ARPM1; PT complex) (Q9BYD9) | 49.2 | 15 | 2 | 2 | 0 |
| ACTR1A (human alpha-centractin; builds the dynactin minifilament) (P61163) | 52.9 | 14 | 4 | 1 | 0 |
| ACTR3 (human Arp3; Arp2/3 subunit) (P61158) | 40.9 | 14 | 4 | 1 | 0 |
| ACTRT1 (human actin-related protein T1; PT complex) (Q8TDG2) | 48.7 | 14 | 2 | 3 | 0 |
| ACTRT2 (this gene) (Q8TDY3) | 48.4 | 13 | 4 | 2 | 0 |
| ACTL7B (human actin-like 7B; GO:0005200 negated by PAINT) (Q9Y614) | 44.1 | 13 | 0 | 6 | 0 |
| ACTL7A (human actin-like 7A; PT complex; GO:0005200 negated by PAINT) (Q9Y615) | 43.6 | 12 | 2 | 5 | 0 |
| ACTL9 (human actin-like 9; PT complex) (Q8TC94) | 41.2 | 11 | 4 | 4 | 0 |
| ACTL8 (human actin-like 8) (Q9H568) | 34.4 | 11 | 3 | 5 | 0 |
| ACTR10 (human Arp11; dynactin pointed-end cap) (Q9NZ32) | 27.8 | 9 | 2 | 8 | 0 |
| ACTL10 (human actin-like 10) (Q5JWF8) **[TRUNCATED - not comparable]** | 33.5 | 7 | 3 | 4 | 5 |

Robustness, scheme BLOSUM45/-14/-2:

| protein | % id (full length) | identical | conservative | non-conservative | gap |
|---|---|---|---|---|---|
| ACTB (human beta-actin; IBA donor) (P60709) | 100.0 | 19 | 0 | 0 | 0 |
| ACTG1 (human gamma-actin; IBA donor) (P63261) | 98.9 | 19 | 0 | 0 | 0 |
| ACTA1 (human alpha-skeletal actin; IBA donor) (P68133) | 93.6 | 18 | 1 | 0 | 0 |
| ACTC1 (human alpha-cardiac actin; IBA donor) (P68032) | 94.1 | 18 | 1 | 0 | 0 |
| Arp53D (Drosophila actin-like 53D; polymerising divergent actin; IBA donor) (P45891) | 64.4 | 16 | 3 | 0 | 0 |
| ACTR2 (human Arp2; Arp2/3 subunit) (P61160) | 48.4 | 16 | 3 | 0 | 0 |
| ACTRT3 (human actin-related protein T3 / ARPM1; PT complex) (Q9BYD9) | 49.2 | 15 | 2 | 2 | 0 |
| ACTR1A (human alpha-centractin; builds the dynactin minifilament) (P61163) | 52.9 | 14 | 4 | 1 | 0 |
| ACTR3 (human Arp3; Arp2/3 subunit) (P61158) | 40.4 | 14 | 4 | 1 | 0 |
| ACTRT1 (human actin-related protein T1; PT complex) (Q8TDG2) | 48.7 | 14 | 2 | 3 | 0 |
| ACTRT2 (this gene) (Q8TDY3) | 48.4 | 13 | 4 | 2 | 0 |
| ACTL7B (human actin-like 7B; GO:0005200 negated by PAINT) (Q9Y614) | 44.1 | 13 | 0 | 6 | 0 |
| ACTL7A (human actin-like 7A; PT complex; GO:0005200 negated by PAINT) (Q9Y615) | 43.3 | 12 | 2 | 5 | 0 |
| ACTL9 (human actin-like 9; PT complex) (Q8TC94) | 41.2 | 11 | 4 | 4 | 0 |
| ACTL8 (human actin-like 8) (Q9H568) | 33.9 | 11 | 3 | 5 | 0 |
| ACTR10 (human Arp11; dynactin pointed-end cap) (Q9NZ32) | 27.8 | 9 | 2 | 8 | 0 |
| ACTL10 (human actin-like 10) (Q5JWF8) **[TRUNCATED - not comparable]** | 33.5 | 7 | 3 | 4 | 5 |

ACTRT2 positions that are non-conservative or gapped: E214->K, K336->W

## 2. Filament protomer interface: could ACTRT2 polymerise like actin?

Computed from **PDB 6DJO** (chains A, B, C, D); the most-buried chain is C, giving **38 protomer-protomer contact positions**. The D-loop column covers actin residues 38-52; that this segment makes protomer contacts is not assumed but read off the computation - each of its contacts is listed with the neighbouring chain it touches in the table of contact positions in results.json.

Scheme BLOSUM62/-11/-1:

| protein | % id (full length) | identical | conservative | non-conservative | gap  D-loop identical / n |
|---|---|---|---|---|------|
| ACTA1 (human alpha-skeletal actin; IBA donor) (P68133) | 100.0 | 38 | 0 | 0 | 0  10/10 |
| ACTC1 (human alpha-cardiac actin; IBA donor) (P68032) | 99.5 | 38 | 0 | 0 | 0  10/10 |
| ACTB (human beta-actin; IBA donor) (P60709) | 93.8 | 37 | 1 | 0 | 0  10/10 |
| ACTG1 (human gamma-actin; IBA donor) (P63261) | 94.1 | 37 | 1 | 0 | 0  10/10 |
| Arp53D (Drosophila actin-like 53D; polymerising divergent actin; IBA donor) (P45891) | 63.2 | 29 | 4 | 5 | 0  4/10 |
| ACTR1A (human alpha-centractin; builds the dynactin minifilament) (P61163) | 52.7 | 20 | 8 | 10 | 0  4/10 |
| ACTR2 (human Arp2; Arp2/3 subunit) (P61160) | 48.4 | 15 | 7 | 16 | 0  2/10 |
| ACTRT2 (this gene) (Q8TDY3) | 47.8 | 14 | 6 | 18 | 0  2/10 |
| ACTL7B (human actin-like 7B; GO:0005200 negated by PAINT) (Q9Y614) | 43.0 | 14 | 2 | 22 | 0  0/10 |
| ACTRT1 (human actin-related protein T1; PT complex) (Q8TDG2) | 47.8 | 13 | 8 | 17 | 0  1/10 |
| ACTRT3 (human actin-related protein T3 / ARPM1; PT complex) (Q9BYD9) | 48.9 | 13 | 5 | 19 | 1  1/10 |
| ACTL7A (human actin-like 7A; PT complex; GO:0005200 negated by PAINT) (Q9Y615) | 43.5 | 13 | 1 | 24 | 0  1/10 |
| ACTL9 (human actin-like 9; PT complex) (Q8TC94) | 40.3 | 11 | 5 | 22 | 0  0/10 |
| ACTR10 (human Arp11; dynactin pointed-end cap) (Q9NZ32) | 28.5 | 9 | 5 | 12 | 12  0/10 |
| ACTL8 (human actin-like 8) (Q9H568) | 34.2 | 8 | 3 | 24 | 3  1/10 |
| ACTR3 (human Arp3; Arp2/3 subunit) (P61158) | 41.1 | 5 | 3 | 29 | 1  2/10 |
| ACTL10 (human actin-like 10) (Q5JWF8) **[TRUNCATED - not comparable]** | 32.7 | 3 | 2 | 13 | 20  0/10 |

Robustness, scheme BLOSUM45/-14/-2:

| protein | % id (full length) | identical | conservative | non-conservative | gap  D-loop identical / n |
|---|---|---|---|---|------|
| ACTA1 (human alpha-skeletal actin; IBA donor) (P68133) | 100.0 | 38 | 0 | 0 | 0  10/10 |
| ACTC1 (human alpha-cardiac actin; IBA donor) (P68032) | 99.5 | 38 | 0 | 0 | 0  10/10 |
| ACTB (human beta-actin; IBA donor) (P60709) | 93.8 | 37 | 1 | 0 | 0  10/10 |
| ACTG1 (human gamma-actin; IBA donor) (P63261) | 94.1 | 37 | 1 | 0 | 0  10/10 |
| Arp53D (Drosophila actin-like 53D; polymerising divergent actin; IBA donor) (P45891) | 63.2 | 29 | 4 | 5 | 0  4/10 |
| ACTR1A (human alpha-centractin; builds the dynactin minifilament) (P61163) | 52.7 | 20 | 8 | 10 | 0  4/10 |
| ACTR2 (human Arp2; Arp2/3 subunit) (P61160) | 48.4 | 15 | 7 | 16 | 0  2/10 |
| ACTRT2 (this gene) (Q8TDY3) | 47.8 | 14 | 6 | 18 | 0  2/10 |
| ACTL7B (human actin-like 7B; GO:0005200 negated by PAINT) (Q9Y614) | 43.0 | 14 | 2 | 22 | 0  0/10 |
| ACTRT1 (human actin-related protein T1; PT complex) (Q8TDG2) | 47.8 | 13 | 8 | 17 | 0  1/10 |
| ACTRT3 (human actin-related protein T3 / ARPM1; PT complex) (Q9BYD9) | 48.9 | 13 | 5 | 19 | 1  1/10 |
| ACTL7A (human actin-like 7A; PT complex; GO:0005200 negated by PAINT) (Q9Y615) | 43.3 | 13 | 1 | 24 | 0  1/10 |
| ACTL9 (human actin-like 9; PT complex) (Q8TC94) | 40.3 | 11 | 5 | 22 | 0  0/10 |
| ACTR10 (human Arp11; dynactin pointed-end cap) (Q9NZ32) | 28.5 | 9 | 5 | 12 | 12  0/10 |
| ACTL8 (human actin-like 8) (Q9H568) | 34.2 | 8 | 3 | 24 | 3  1/10 |
| ACTR3 (human Arp3; Arp2/3 subunit) (P61158) | 40.6 | 5 | 4 | 28 | 1  2/10 |
| ACTL10 (human actin-like 10) (Q5JWF8) **[TRUNCATED - not comparable]** | 32.7 | 3 | 2 | 13 | 20  0/10 |

A tally can hide which residues were lost, so the D-loop contact positions are also
printed as a motif. This is where the comparison discriminates: both
polymerisation-competent divergent controls keep the loop's anchor and its hydrophobic
core, and ACTRT2 does not.

Actin positions 38, 39, 40, 41, 42, 43, 44, 45, 47, 49 = `PRHQGVMVMQ`

| protein | D-loop contact motif | identical / n |
|---|---|---|
| ACTB (human beta-actin; IBA donor) (P60709) | `PRHQGVMVMQ` | 10/10 |
| ACTG1 (human gamma-actin; IBA donor) (P63261) | `PRHQGVMVMQ` | 10/10 |
| ACTA1 (human alpha-skeletal actin; IBA donor) (P68133) | `PRHQGVMVMQ` | 10/10 |
| ACTC1 (human alpha-cardiac actin; IBA donor) (P68032) | `PRHQGVMVMQ` | 10/10 |
| Arp53D (Drosophila actin-like 53D; polymerising divergent actin; IBA donor) (P45891) | `PRHLNVLLSI` | 4/10 |
| ACTR1A (human alpha-centractin; builds the dynactin minifilament) (P61163) | `PKHVRVMAAE` | 4/10 |
| ACTRT2 (this gene) (Q8TDY3) | `LKFQAPSAAQ` | 2/10 |
| ACTR2 (human Arp2; Arp2/3 subunit) (P61160) | `PRSTTKVGII` | 2/10 |
| ACTR3 (human Arp3; Arp2/3 subunit) (P61158) | `QAQRRVMKVD` | 2/10 |
| ACTRT1 (human actin-related protein T1; PT complex) (Q8TDG2) | `CKFNVPLALQ` | 1/10 |
| ACTRT3 (human actin-related protein T3 / ARPM1; PT complex) (Q9BYD9) | `AKGQS-RAQG` | 1/10 |
| ACTL7A (human actin-like 7A; PT complex; GO:0005200 negated by PAINT) (Q9Y615) | `PYMETAKTDR` | 1/10 |
| ACTL8 (human actin-like 8) (Q9H568) | `PCKENPGPYR` | 1/10 |
| ACTR10 (human Arp11; dynactin pointed-end cap) (Q9NZ32) | `----------` | 0/10 |
| ACTL7B (human actin-like 7B; GO:0005200 negated by PAINT) (Q9Y614) | `RCPEAADADR` | 0/10 |
| ACTL9 (human actin-like 9; PT complex) (Q8TC94) | `QPKKPATSQG` | 0/10 |
| ACTL10 (human actin-like 10) (Q5JWF8) **[TRUNCATED - not comparable]** | `----------` | 0/10 |

Marked table rows counted from the rendered tables above: **6** across 1 flagged member(s), i.e. 6 rows each. Both marker forms are counted and prose mentioning a marker is excluded, since the count looks only at lines that are table rows. Rows carrying annotation counts rather than sequence comparisons are deliberately unmarked, since a length flag cannot affect them.

## 3. IBA source audit

### GO:0015629 actin cytoskeleton (is_active_in)

- WITH/FROM tokens: **25** (1 PANTHER node(s), 24 resolved to protein entries, 0 unresolved)
- sources carrying their **own** experimental evidence for this term or a descendant: **24/24**
- unambiguous Swiss-Prot sources: 16
- organisms represented: 12 (Caenorhabditis elegans, Candida albicans (strain SC5314 / ATCC MYA-2876), Dictyostelium discoideum, Drosophila melanogaster, Gallus gallus, Homo sapiens, Mus musculus, Plasmodium falciparum (isolate 3D7), Rattus norvegicus, Saccharomyces cerevisiae (strain ATCC 204508 / S288c), Schizosaccharomyces pombe (strain 972 / ATCC 24843), Sus scrofa)

| token | resolved | reviewed | organism | own evidence for the donated term |
|---|---|---|---|---|
| `CGD:CAL0000191211` | ACT1 (A0A1D8PFR4, A0A1D8PFR4_CANAL) | TrEMBL | Candida albicans (strain SC5314 / ATCC MYA-2876) | IBAx1,IDAx1 |
| `FB:FBgn0011743` | Arp53D (P45891, ACTY_DROME) | Swiss-Prot | Drosophila melanogaster | IBAx1,IDAx1 |
| `MGI:MGI:87906` | Actg1 (P63260, ACTG_MOUSE) | Swiss-Prot | Mus musculus | IBAx2,IDAx3,IEAx1,ISOx5 |
| `MGI:MGI:87906` | Actg1 (Q4KL81, Q4KL81_MOUSE) | TrEMBL | Mus musculus | IEAx1 |
| `MGI:MGI:87906` | Actg1 (Q3TSB7, Q3TSB7_MOUSE) | TrEMBL | Mus musculus | none |
| `MGI:MGI:87906` | Actg1 (F8WGM8, F8WGM8_MOUSE) | TrEMBL | Mus musculus | none |
| `MGI:MGI:87906` | Actg1 (G3UYG0, G3UYG0_MOUSE) | TrEMBL | Mus musculus | none |
| `MGI:MGI:87909` | Acta2 (P62737, ACTA_MOUSE) | Swiss-Prot | Mus musculus | IBAx1,IDAx1,IEAx2,ISOx2,ISSx1 |
| `MGI:MGI:87909` | Acta2 (Q3U122, Q3U122_MOUSE) | TrEMBL | Mus musculus | ISSx1 |
| `MGI:MGI:87909` | Acta2 (A0A494B9T3, A0A494B9T3_MOUSE) | TrEMBL | Mus musculus | none |
| `MGI:MGI:87909` | Acta2 (Q8CF71, Q8CF71_MOUSE) | TrEMBL | Mus musculus | none |
| `PANTHER:PTN002631484` | - | - | - | PANTHER internal tree node, not a protein; cannot be resolved to an entry |
| `PomBase:SPBC32H8.12c` | act1 (P10989, ACT_SCHPO) | Swiss-Prot | Schizosaccharomyces pombe (strain 972 / ATCC 24843) | IBAx1,IDAx4,TASx1 |
| `RGD:1304556` | Actg1 (P63259, ACTG_RAT) | Swiss-Prot | Rattus norvegicus | IBAx2,IDAx4,ISOx3 |
| `RGD:1304556` | Actg1 (A0A8I6AQR0, A0A8I6AQR0_RAT) | TrEMBL | Rattus norvegicus | none |
| `RGD:621676` | Acta2 (P62738, ACTA_RAT) | Swiss-Prot | Rattus norvegicus | IBAx1,IDAx2,ISOx1,ISSx1 |
| `RGD:621676` | Acta2 (B0BMT0, B0BMT0_RAT) | TrEMBL | Rattus norvegicus | ISSx1 |
| `RGD:621676` | Acta2 (A0A0G2K4M6, A0A0G2K4M6_RAT) | TrEMBL | Rattus norvegicus | none |
| `RGD:628837` | Actb (P60711, ACTB_RAT) | Swiss-Prot | Rattus norvegicus | IBAx2,IDAx2,ISOx3 |
| `RGD:628837` | Actb (A0A0G2K3K2, A0A0G2K3K2_RAT) | TrEMBL | Rattus norvegicus | IEAx2 |
| `RGD:628837` | Actb (A0A068F1Y2, A0A068F1Y2_RAT) | TrEMBL | Rattus norvegicus | none |
| `SGD:S000001855` | ACT1 (P60010, ACT_YEAST) | Swiss-Prot | Saccharomyces cerevisiae (strain ATCC 204508 / S288c) | IBAx1,IDAx9 |
| `UniProtKB:P08023` | ACTA2 (P08023, ACTA_CHICK) | Swiss-Prot | Gallus gallus | IBAx1,IDAx1 |
| `UniProtKB:P60709` | ACTB (P60709, ACTB_HUMAN) | Swiss-Prot | Homo sapiens | IBAx2,IDAx3,IMPx1 |
| `UniProtKB:P63261` | ACTG1 (P63261, ACTG_HUMAN) | Swiss-Prot | Homo sapiens | IBAx2,IDAx1 |
| `UniProtKB:P68032` | ACTC1 (P68032, ACTC_HUMAN) | Swiss-Prot | Homo sapiens | IBAx2,IDAx2,ISSx1 |
| `UniProtKB:P68133` | ACTA1 (P68133, ACTS_HUMAN) | Swiss-Prot | Homo sapiens | IBAx4,IDAx3,IMPx1,ISSx1 |
| `UniProtKB:Q6QAQ1` | ACTB (Q6QAQ1, ACTB_PIG) | Swiss-Prot | Sus scrofa | IBAx2,IEAx2,IPIx1,ISSx1 |
| `UniProtKB:Q8I4X0` | ACT1 (Q8I4X0, ACT1_PLAF7) | Swiss-Prot | Plasmodium falciparum (isolate 3D7) | IBAx1,IDAx1,IEAx1,ISSx2 |
| `WB:WBGene00000064` | act-2 (P10984, ACT2_CAEEL) | Swiss-Prot | Caenorhabditis elegans | IBAx1,IDAx1 |
| `WB:WBGene00000065` | act-3 (P0DM42, ACT3_CAEEL) | Swiss-Prot | Caenorhabditis elegans | IBAx1,IDAx1 |
| `WB:WBGene00000066` | act-4 (P10986, ACT4_CAEEL) | Swiss-Prot | Caenorhabditis elegans | IBAx1,IDAx1 |
| `WB:WBGene00000066` | act-4 (Q95ZL1, Q95ZL1_CAEEL) | TrEMBL | Caenorhabditis elegans | IDAx1 |
| `WB:WBGene00000067` | act-5 (O45815, O45815_CAEEL) | TrEMBL | Caenorhabditis elegans | IBAx1,IDAx2 |
| `dictyBase:DDB_G0269234` | act1/act2/act4/act5/act6/act7/act8/act9/act11/act12/act13/act14/act15/act16/act19/act20/act21 (P07830, ACT1_DICDI) | Swiss-Prot | Dictyostelium discoideum | IBAx1,IDAx3,IEAx1 |
| `dictyBase:DDB_G0275023` | act22 (Q553U6, ACT22_DICDI) | Swiss-Prot | Dictyostelium discoideum | IBAx1,IDAx1,IEAx1,ISSx1 |
| `dictyBase:DDB_G0289487` | act3 (P07829, ACT3_DICDI) | Swiss-Prot | Dictyostelium discoideum | IBAx1,IDAx1,IEAx1,ISSx1 |
| `dictyBase:DDB_G0289811` | act10 (Q54GX7, ACT10_DICDI) | Swiss-Prot | Dictyostelium discoideum | IBAx1,IDAx3,IEAx1 |

### GO:0005200 structural constituent of cytoskeleton (enables)

- WITH/FROM tokens: **11** (1 PANTHER node(s), 10 resolved to protein entries, 0 unresolved)
- sources carrying their **own** experimental evidence for this term or a descendant: **10/10**
- unambiguous Swiss-Prot sources: 8
- organisms represented: 5 (Dictyostelium discoideum, Homo sapiens, Mus musculus, Rattus norvegicus, Saccharomyces cerevisiae (strain ATCC 204508 / S288c))

| token | resolved | reviewed | organism | own evidence for the donated term |
|---|---|---|---|---|
| `MGI:MGI:87906` | Actg1 (P63260, ACTG_MOUSE) | Swiss-Prot | Mus musculus | IBAx1,IDAx1,ISOx2 |
| `MGI:MGI:87906` | Actg1 (Q4KL81, Q4KL81_MOUSE) | TrEMBL | Mus musculus | none |
| `MGI:MGI:87906` | Actg1 (Q3TSB7, Q3TSB7_MOUSE) | TrEMBL | Mus musculus | none |
| `MGI:MGI:87906` | Actg1 (F8WGM8, F8WGM8_MOUSE) | TrEMBL | Mus musculus | none |
| `MGI:MGI:87906` | Actg1 (G3UYG0, G3UYG0_MOUSE) | TrEMBL | Mus musculus | none |
| `PANTHER:PTN000940351` | - | - | - | PANTHER internal tree node, not a protein; cannot be resolved to an entry |
| `RGD:1304556` | Actg1 (P63259, ACTG_RAT) | Swiss-Prot | Rattus norvegicus | IBAx1,IDAx2,ISOx1 |
| `RGD:1304556` | Actg1 (A0A8I6AQR0, A0A8I6AQR0_RAT) | TrEMBL | Rattus norvegicus | none |
| `SGD:S000001171` | ARP1 (P38696, ARP1_YEAST) | Swiss-Prot | Saccharomyces cerevisiae (strain ATCC 204508 / S288c) | IDAx1 |
| `SGD:S000001855` | ACT1 (P60010, ACT_YEAST) | Swiss-Prot | Saccharomyces cerevisiae (strain ATCC 204508 / S288c) | IBAx1,IDAx1 |
| `SGD:S000002513` | ARP10 (Q04549, ARP10_YEAST) | Swiss-Prot | Saccharomyces cerevisiae (strain ATCC 204508 / S288c) | IPIx3 |
| `UniProtKB:P60709` | ACTB (P60709, ACTB_HUMAN) | Swiss-Prot | Homo sapiens | EXPx1,IBAx1,IDAx3,IMPx1,TASx1 |
| `UniProtKB:P61158` | ACTR3 (P61158, ARP3_HUMAN) | Swiss-Prot | Homo sapiens | IDAx1 |
| `UniProtKB:P61160` | ACTR2 (P61160, ARP2_HUMAN) | Swiss-Prot | Homo sapiens | IDAx1 |
| `dictyBase:DDB_G0269234` | act1/act2/act4/act5/act6/act7/act8/act9/act11/act12/act13/act14/act15/act16/act19/act20/act21 (P07830, ACT1_DICDI) | Swiss-Prot | Dictyostelium discoideum | IBAx1,IDAx1 |
| `dictyBase:DDB_G0289811` | act10 (Q54GX7, ACT10_DICDI) | Swiss-Prot | Dictyostelium discoideum | IBAx1,IDAx1 |

### 3b. Are the sibling genes' IBA rows the same rows?

| sibling | shared IBA row | WITH/FROM byte-identical | tokens (ACTRT2 / sibling) |
|---|---|---|---|
| ACTL7A | none | - | - |
| ACTL7B | none | - | - |
| ACTL8 | GO:0015629 (IBA) | **True** | 25 / 25 |
| ACTR1A | none | - | - |
| ACTR1B | none | - | - |
| ACTR10 | GO:0005200 (IBA) | **True** | 11 / 11 |

## 4. Where PAINT has, and has not, negated `GO:0005200`

In the cached PAINT table for PTHR11937, `GO:0005200 structural constituent of cytoskeleton` is propagated at **1** node(s) and explicitly negated (IRD, negated=true) at **8** node(s).

| node | evidence | negated | date | that node's other PAINT annotations |
|---|---|---|---|---|
| PTN000940351 | IBD | false | 20250805 | - |
| PTN000233596 | IRD | true | 20260416 | GO:0005885(C,IBD), GO:0005938(C,IBD), GO:0034314(P,IBD), GO:0051015(F,IBD) |
| PTN000233752 | IRD | true | 20250805 | GO:0005737(C,IBD), GO:0006338(P,IBD), GO:0006355(P,IBD), GO:0030234(F,IBD), GO:0031011(C,IBD) |
| PTN000233796 | IRD | true | 20260416 | GO:0005885(C,IBD), GO:0034314(P,IBD), GO:0044396(P,IBD), GO:0051015(F,IBD) |
| PTN000233887 | IRD | true | 20250805 | GO:0000812(C,IBD), GO:0006338(P,IBD), GO:0007000(P,IBD), GO:0031491(F,IBD) |
| PTN000234048 | IRD | true | 20250805 | GO:0003729(F,IBD), GO:0006302(P,IBD), GO:0006355(P,IBD), GO:0031011(C,IBD) |
| PTN001732543 | IRD | true | 20250805 | GO:0003682(F,IBD), GO:0006338(P,IBD), GO:0006357(P,IBD), GO:0016514(C,IBD), GO:0035267(C,IBD) |
| PTN007551901 | IRD | true | 20260416 | GO:0106006(F,IBD) |
| PTN008986528 | IRD | true | 20250805 | GO:0005198(F,IBA) |

`GO:0005198 structural molecule activity` rows anywhere in the family: PTN008986528 (IBA, 20250805)

Human genes that end up with each term by IBA (live QuickGO), with the donating node:

| term | human genes | donating node(s) |
|---|---|---|
| GO:0005200 | ACTA1, ACTA2, ACTC1, ACTG2, ACTL10, ACTL9, ACTR10, ACTRT1, ACTRT2, ACTRT3, DES, EPB41, EPB41L2, GFAP, LMNA, LMNB1, LMNB2, NEFM, PLEC, PRPH, SYNM, TUBA1A, TUBA1B, TUBA1C, TUBA3C, TUBA3D, TUBA3E, TUBA4A, TUBA8, TUBAL3, TUBB, TUBB1, TUBB2A, TUBB2B, TUBB3, TUBB4A, TUBB4B, TUBB6, TUBB8, TUBB8B, TUBD1, TUBE1, VIM | PTN000172598, PTN000580114, PTN000940351, PTN001145669, PTN002753803, PTN002760594, PTN002932247 |
| GO:0005198 | ACTL7A, ACTL7B, ARC, DSP, DST, EPPK1, EVPL, GPS1, LYRM4, MACF1, POPDC1, POPDC2, POPDC3, PPL, PSMD11, PSMD13, PSMD6, SEC13, SEC31A, SEC31B, UPK1B, UPK2, VPS25 | PTN000056911, PTN000073599, PTN000111812, PTN000322234, PTN000323064, PTN000357875, PTN000365347, PTN000940351, PTN001383178, PTN002704844, PTN002753757, PTN008562333, PTN008714166, PTN008986528 |

## 5. Relatives census (live)

IBA rows per gene: ACTL7A=3, ACTL7B=3, ACTL8=11, ACTL9=2, ACTL10=2, ACTRT1=5, ACTRT2=2, ACTRT3=2. Median over all eight: **2.5**; excluding ACTL8: **2**; excluding ACTRT2: **3**. Modal count **2** (in 4 of 8 genes).

Genes drawing on the beta-actin-subfamily nodes PTN002631586, PTN007551913: **ACTL8**.

(These are annotation counts, not sequence comparisons, so they are unaffected by the length flag above and are deliberately unmarked.)

| gene | accession | IBA rows | IBA terms | PANTHER nodes |
|---|---|---|---|---|
| ACTL7A | Q9Y615 (ACL7A_HUMAN) | 3 | GO:0005198, GO:0005634, GO:0005737 | PTN000940351, PTN001377938, PTN008986520, PTN008986528 |
| ACTL7B | Q9Y614 (ACL7B_HUMAN) | 3 | GO:0005198, GO:0005634, GO:0005737 | PTN000940351, PTN001377938, PTN008986520, PTN008986528 |
| ACTL8 | Q9H568 (ACTL8_HUMAN) | 11 | GO:0005737, GO:0005884, GO:0007409, GO:0015629, GO:0016020, GO:0019901, GO:0030424, GO:0035267, GO:0045202, GO:0048870, GO:0098973 | PTN002631484, PTN002631586, PTN007551913 |
| ACTL9 | Q8TC94 (ACTL9_HUMAN) | 2 | GO:0005200, GO:0015629 | PTN000940351, PTN002631484 |
| ACTL10 | Q5JWF8 (ACL10_HUMAN) | 2 | GO:0005200, GO:0015629 | PTN000940351, PTN002631484 |
| ACTRT1 | Q8TDG2 (ACTT1_HUMAN) | 5 | GO:0003682, GO:0005200, GO:0005634, GO:0006355, GO:0015629 | PTN000748066, PTN000940351, PTN002631484 |
| ACTRT2 | Q8TDY3 (ACTT2_HUMAN) | 2 | GO:0005200, GO:0015629 | PTN000940351, PTN002631484 |
| ACTRT3 | Q9BYD9 (ACTT3_HUMAN) | 2 | GO:0005200, GO:0015629 | PTN000940351, PTN002631484 |

### 5b. Term relationships (computed, not assumed)

| term | label | obsolete | is GO:0005856 an ancestor | is GO:0015629 an ancestor |
|---|---|---|---|---|
| GO:0005198 | structural molecule activity | False | False | False |
| GO:0005200 | structural constituent of cytoskeleton | False | False | False |
| GO:0015629 | actin cytoskeleton | False | True | True |
| GO:0033011 | perinuclear theca | False | True | False |
| GO:0005856 | cytoskeleton | False | True | False |

- `GO:0033011_is_under_GO:0005856_cytoskeleton` = **True**
- `GO:0033011_is_under_GO:0015629_actin_cytoskeleton` = **False**
- `GO:0005200_is_under_GO:0005198` = **True**

## 6. The `GO:0005515` row

GOA's WITH/FROM partner is `Q9H2J4` = **PDCL3** (PDCL3_HUMAN, Swiss-Prot, 239 aa, Homo sapiens).

Every IntAct record for ACTRT2:

| A | B | method | type | expansion | MI score | PMID |
|---|---|---|---|---|---|---|
| ACTRT2 | PDCL3 | anti tag coip | association | spoke expansion | 0.5 | 33961781 |
| ACTRT2 | PDCL3 | anti tag coip | physical association | - | 0.5 | 33961781 |
| ACTRT2 | CCT6B | anti tag coip | association | spoke expansion | 0.35 | 33961781 |
| ACTRT2 | SLC25A19 | anti tag coip | association | spoke expansion | 0.35 | 33961781 |
| ACTRT2 | ACSL4 | anti tag coip | association | spoke expansion | 0.35 | 33961781 |
| ACTRT2 | TCP1 | anti tag coip | association | spoke expansion | 0.35 | 33961781 |
| ACTRT2 | CCT6A | anti tag coip | association | spoke expansion | 0.35 | 33961781 |
| ACTRT2 | CCT3 | anti tag coip | association | spoke expansion | 0.35 | 33961781 |
| ACTRT2 | CCT2 | anti tag coip | association | spoke expansion | 0.35 | 33961781 |
| ACTRT2 | CCT7 | anti tag coip | association | spoke expansion | 0.35 | 33961781 |

What that partner interacts with across all of IntAct: **91 partners** in 156 records.

- actin-superfamily partners (12): ACTA2, ACTB, ACTBL2, ACTG1, ACTR1A, ACTR1B, ACTR2, ACTRT1, ACTRT2, ACTRT3, POTEF, POTEI
- CCT/TRiC chaperonin partners (9): CCT2, CCT3, CCT4, CCT5, CCT6A, CCT6B, CCT7, CCT8, TCP1
- tubulin partners (3): TUBA1A, TUBD1, TUBG1

## 7. Perinuclear-theca complex: who is annotated, and to what?

| gene | species | accession | GO:0033011? | evidence | experimental BP terms | n BP rows |
|---|---|---|---|---|---|---|
| ACTRT1 | human | Q8TDG2 (ACTT1_HUMAN) | yes | IEA/GO_REF:0000107, ISS/GO_REF:0000024 | GO:0008589, GO:0045892 | 4 |
| ACTRT1 | mouse | Q9D9J3 (ACTT1_MOUSE) | yes | IDA/PMID:35793634 | none | 8 |
| ACTRT2 | human | Q8TDY3 (ACTT2_HUMAN) | yes | IEA/GO_REF:0000107, ISS/GO_REF:0000024 | none | 1 |
| ACTRT2 | mouse | Q9D9L5 (ACTT2_MOUSE) | yes | IDA/PMID:35793634 | none | 2 |
| ACTRT3 | human | Q9BYD9 (ACTT3_HUMAN) | yes | IEA/GO_REF:0000107, ISS/GO_REF:0000024 | none | 1 |
| ACTRT3 | mouse | Q8BXF8 (ACTT3_MOUSE) | yes | IDA/PMID:35793634 | none | 1 |
| ACTL7A | human | Q9Y615 (ACL7A_HUMAN) | yes | IDA/GO_REF:0000052, IEA/GO_REF:0000107 | none | 7 |
| ACTL7A | mouse | Q9QY84 (ACL7A_MOUSE) | yes | IDA/PMID:41169243, IEA/GO_REF:0000120, ISO/GO_REF:0000119 | GO:0001675, GO:0007286, GO:0009566 | 5 |
| ACTL9 | human | Q8TC94 (ACTL9_HUMAN) | yes | IDA/PMID:33626338, IEA/GO_REF:0000120 | GO:0001675, GO:0009566 | 5 |
| ACTL9 | mouse | Q8CG27 (ACTL9_MOUSE) | yes | IDA/PMID:35793634, IEA/GO_REF:0000120, ISO/GO_REF:0000119, ISS/GO_REF:0000024 | GO:0001675, GO:0009566 | 7 |
| CCIN | human | Q13939 (CALI_HUMAN) | yes | IDA/GO_REF:0000052, IEA/GO_REF:0000107 | GO:0007283 | 5 |
| CCIN | mouse | Q8CDE2 (CALI_MOUSE) | yes | IDA/PMID:35793634, IDA/PMID:41169243, IEA/GO_REF:0000120, ISO/GO_REF:0000119 | GO:0007283, GO:0007286 | 5 |

### 7b. How many entities does each supporting reference annotate?

Querying QuickGO by reference rather than by gene distinguishes an observation of this
protein from a projection onto it.

The first column is an **annotation** count, not an entity count - QuickGO's total counts
annotations, and one reference can annotate many terms per entity. Where the result set is
large enough to paginate, the walk is capped and the entity count is reported as
unavailable rather than replaced by the sample size.

| reference | annotations in GOA | entities | distinct terms | assigned by |
|---|---|---|---|---|
| PMID:12243744 | 0 | 0 | - | - |
| PMID:11750065 | 0 | 0 | - | - |
| PMID:35616329 | 0 | 0 | - | - |
| PMID:41668650 | 0 | 0 | - | - |
| PMID:40811009 | 0 | 0 | - | - |
| PMID:25293813 | 0 | 0 | - | - |
| PMID:33961781 | 9514 | not counted (330+ in a partial walk) | GO:0005515 | IntAct |
| PMID:35793634 | 35 | 19 | GO:0005515, GO:0007286, GO:0033011 | UniProt |

Subset test on PMID:35793634 / GO:0033011: **12** of 19 entities the reference touches received the term (`is_subset_not_blanket` = **True**).

- with the term: Actl9, Actrt1, Actrt2, Actrt3, Capza3, Capzb, Ccin, Cylc1, Fabp9, Gsto2, H2bl1, Wbp2nl
- touched but NOT given the term: Actl7a, Dpy19l2, Fam209, Lbr, Parp11, Spaca1, Spata46

A curator who assigned the term to a strict subset of the proteins named in the paper
was discriminating per protein, not projecting one localisation onto every partner.

## 8. What the measurements do and do not support

**Whole computed contact set first, so no sub-selection can flatter the result.** Of the 19 residues within 4.0 A of ATP or the divalent cation in PDB 2BTF, ACTRT2 matches actin at **13 identically** and 4 conservatively, with **2 non-conservative** substitutions.

**The phosphate, cation and sensor positions are fully conserved; the adenine/ribose region is not.** Split by role:

| group | positions | identical | conservative | non-conservative | substitutions |
|---|---|---|---|---|---|
| phosphate loops, cation site, sensor | D11, S14, G15, K18, Q137, D154, G156, D157, V159, R183 | 10 | 0 | 0 | none |
| adenine/ribose region | E214, Y306, K336 | 0 | 1 | 2 | E214->K, Y306->F, K336->W |

Which of those named positions are inside the computed 4 A contact set, and which are not:

- phosphate loops, cation site, sensor: inside S14, G15, K18, Q137, G156, D157, V159; outside D11, D154, R183
- adenine/ribose region: inside E214, Y306, K336; outside none

So Harata et al. 2001's sequence-inspection claim that actin's ATP-binding motif is highly conserved in this protein is confirmed where it matters most - every phosphate-binding-loop residue, the divalent-cation ligand and the sensor arginine are identical - while the adenine/ribose region has diverged. Either way a retained pocket means a nucleotide-binding claim is **untested, not refuted**: it is not itself evidence that ACTRT2 binds anything.

**The ATP-hydrolysis trigger is lost.** Actin's His161 is C in ACTRT2 (non-conservative). The Pro-rich loop that governs its rotamer has also changed (A108->P, P109->S), but that is reported as context only: PMID:37009486 reports the A108G and P109A actin mutants polymerise and hydrolyse like wild type, so these substitutions modulate the His161 rotamer rather than gating hydrolysis; they are context for the His161 loss, not independent evidence of lost hydrolysis.

- His161 is retained in every panel member that either extends a filament or nucleates one: `his161_retained_in_all_filament_builders_and_nucleators` = **True**.
- His161 is lost in **all reported members of the sperm perinuclear-theca ARP complex**: `his161_lost_in_all_reported_PT_complex_members` = **True** (Q8TC94=Y, Q8TDG2=C, Q8TDY3=C, Q9BYD9=Q, Q9Y615=Y). It is also lost outside that complex, in Q9H568=R, Q9NZ32=L - so the loss is not exclusive to the PT ARPs, only universal within them.
- Internal control: ACTL7B is testis-specific but is not a reported member of that complex, and it **retains** His161 (`H`). So the loss tracks the complex, not merely testis expression.

**The filament interface is not intact either.** ACTRT2 matches actin at 14/38 protomer-contact positions. `ACTRT2_below_every_filament_builder` = **True** (filament builders: P45891=29, P60709=37, P61163=20, P63261=37, P68032=38, P68133=38; lowest is P61163 at 20). ACTRT2 instead sits with the proteins that nucleate a filament without extending one (P61158=5, P61160=15). So the measurement argues against ACTRT2 extending an F-actin filament; it does not exclude an Arp2/3-like role, and no such role has been proposed for it.

The His161 loss and the interface degeneracy are **one coupled observation, not two independent ones**: actin's ATPase activity operates in the F-form and His161 flips as part of the G-to-F transition, so a protein that cannot make the F-form contacts has no route to the hydrolysis step regardless of His161. Counting them as separate lines of evidence would inflate the case, as would counting the Pro-rich loop substitutions as a third.

**The IBA donors are not weak.** Sources carrying their own experimental evidence for the term they donated: GO:0015629 24/24; GO:0005200 10/10. So any objection to these rows has to be about propagation, not about donor quality.

**The gap.** Reported PT-complex members with no experimental biological-process annotation in either human or mouse: **ACTRT2, ACTRT3**.

