# ARHGAP11B: a GAP-dead RhoGAP that still has its arginine finger

All numbers below are produced by `analyze_arhgap11b.py` in this directory.
Re-run it to regenerate this file; do not hand-edit.

```
uv run python analyze_arhgap11b.py
uv run python analyze_arhgap11b.py --self-test
```

## Subjects

| role | accession | entry | length | Rho-GAP DOMAIN (UniProt) |
|---|---|---|---|---|
| query | Q3KRB8 | RHGBB_HUMAN | 267 | 49..250 |
| paralog / ancestor | Q6P4F7 | RHGBA_HUMAN | 1023 | 49..239 |
| structural control | Q07960 | RHG01_HUMAN | 439 | 244..431 |

The GTPase in the control structure is RHOA_HUMAN (P61586).

## 1. Where ARHGAP11B stops being ARHGAP11A

Colinearity proved (global alignment of the N-terminal regions opens no gaps): `True`.
No identity cutoff is chosen anywhere. The boundary is the single changepoint that maximises the between-segment sum of squares of the per-residue identity vector, and its significance is established by permuting that vector 2000 times: observed statistic 34.1653, best statistic over permutations 3.2891, empirical p = 5.00e-04. The script raises rather than reporting the argmax of noise if any permutation matches the observed statistic.

**Derived divergence point: residue 220.**

| region | identical / compared | identity |
|---|---|---|
| 1-220 | 216 / 220 | 98.2% |
| 221-267 | 2 / 47 | 4.3% |

## 2. The arginine finger is retained

A control's own annotated arginine finger is aligned onto ARHGAP11B and scored as retained only if the aligned residue is an arginine **and** the aligned position lands on one of ARHGAP11B's own annotated Site features.

| control | control site | control residue | aligned ARHGAP11B position | residue | on an annotated ARHGAP11B site | retained |
|---|---|---|---|---|---|---|
| RHGBA_HUMAN (Q6P4F7) | 87 | R | 87 | R | True | **True** |
| RHG01_HUMAN (Q07960) | 282 | R | 87 | R | True | **True** |

So the residue test that normally exposes a pseudo-enzyme returns *retained* here, for a protein that two independent experimental annotations record as GAP-dead. The hypothesis that ARHGAP11B lost catalysis by losing its arginine finger is **not confirmed**.

## 3. How much does the arginine-finger test discriminate?

All **66 reviewed (Swiss-Prot) human proteins** carrying the PROSITE RhoGAP profile PS50238 were fetched. This is the Swiss-Prot subset of the family, not the whole family.

| | count |
|---|---|
| entries | 66 |
| with an annotated arginine finger | 66 |
| without an annotated arginine finger | 0 |
| annotated finger position holds R | 60 |
| annotated finger position does not hold R | 6 |

The screen flags 6 of 66. **ARHGAP11B is not among them.** But a count of flagged proteins is not a count of confirmed pseudo-enzymes, so each flagged entry is asked what UniProt itself concluded, and on what evidence:

| entry | residue | UniProt verdict | evidence |
|---|---|---|---|
| `OCRL_HUMAN` | Q | UNIPROT_SAYS_INACTIVE | ECO:0000269 |
| `I5P2_HUMAN` | Q | UNIPROT_SAYS_INACTIVE | ECO:0000250 |
| `ARAP2_HUMAN` | Q | UNIPROT_SILENT | - |
| `FA13B_HUMAN` | Q | UNIPROT_SILENT | - |
| `RHG36_HUMAN` | T | UNIPROT_ASSERTS_ACTIVITY | ECO:0000250 |
| `DEP1B_HUMAN` | I | UNIPROT_SILENT | - |

Only **1** of the flagged entries carries an *experimentally* supported (`ECO:0000269`) UniProt statement that the domain is catalytically inactive for want of the arginine.

The sharper result is that **residue identity and curated activity are decoupled in both directions within this family**. ARHGAP11B keeps the arginine and is experimentally GAP-dead. `RHG36_HUMAN` (ARHGAP36) has a threonine at its own annotated arginine-finger position and UniProt nonetheless asserts GTPase activator activity for it — by similarity, `ECO:0000250`, which is the weakest thing UniProt says. That is the same class of defect as the one this review corrects, pointing the other way.

So the catalytic-residue screen could not have predicted ARHGAP11B's inactivity, and would not have been decisive even where it fires. A curation pipeline that gates a GAP-activity term on arginine-finger presence keeps the term on this protein.

## 4. What the truncation actually removes

The GAP:GTPase interface is computed from PDB 1TX4 (chain A = RHG01_HUMAN, chain B = RHOA_HUMAN), a transition-state mimic containing ALF, GDP, MG. Chain roles are proved, not assumed: chain A is 99.5% identical to Q07960 and chain B is 99.4% identical to P61586. Contacts are every GAP residue with an atom within 4.5 A of RhoA or of the nucleotide/metal/fluoride.

Sanity check on the geometry: the calculation recovers the control's own annotated arginine finger [282] among its contacts, as it must.

Those 25 contact positions are projected onto ARHGAP11A (global, control Rho-GAP domain vs paralog Rho-GAP domain) and split at the divergence point derived in section 1. The projection is accepted only because it is in register: the control's arginine finger (282) maps onto ARHGAP11A's own annotated arginine finger (87). Without that reciprocal anchor a global alignment of these two proteins lands the whole interface in the wrong half of ARHGAP11A, because ARHGAP1 carries its Rho-GAP domain at the C-terminus and ARHGAP11A at the N-terminus.

| | count |
|---|---|
| control GAP contacts | 25 |
| mapped onto ARHGAP11A | 24 |
| unmapped | 1 |
| **retained** by ARHGAP11B (ARHGAP11A pos <= 220) | 22 |
| **lost** by ARHGAP11B (ARHGAP11A pos > 220) | 2 |
| of those, inside ARHGAP11A's own Rho-GAP domain | 2 |

Interface positions ARHGAP11B does **not** have (ARHGAP11A numbering):

| control pos | control res | ARHGAP11A pos | ARHGAP11A res | inside ARHGAP11A's Rho-GAP domain |
|---|---|---|---|---|
| 413 | I | 221 | L | True |
| 417 | N | 225 | A | True |

The truncation therefore removes 2 of 24 mapped GAP:GTPase interface positions (8%) while leaving the arginine finger in place. The catalytic residue survives; part of the surface that has to present it to the GTPase does not.

## 5. The UniProt Rho-GAP domain boundary

| | value |
|---|---|
| ARHGAP11B Rho-GAP DOMAIN | 49..250 (202 aa) |
| ARHGAP11A Rho-GAP DOMAIN | 49..239 (191 aa) |
| derived divergence point | 220 |
| ARHGAP11B domain residues past the divergence point | 30 |
| ARHGAP11B domain longer than ARHGAP11A's by | 11 aa |

UniProt's Rho-GAP DOMAIN feature on ARHGAP11B runs 30 residues past the last residue that is homologous to ARHGAP11A, i.e. into the human-specific frameshift C-terminus. The annotated domain on the truncated paralog is therefore 11 residues **longer** than the annotated domain on the catalytically active parent. Any pipeline reading domain extent as evidence of a working RhoGAP will read this protein as more intact than the active one, not less.

