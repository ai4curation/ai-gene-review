# Synpcc7942_0873 (Q31PW6): NTPase motifs, DUF4062 domain context and the conserved Glu

Query: dashboard sequence CP088958.1_900 (*S. elongatus* PCC 6311), 362 aa, identical
to Q31PW6 (UniParc UPI000049B91D). Three analyses, each recorded as a BERIL run in
`projects/hackathon/`. Numbers below are from the `data/*.json` copies of each run's
`results.json`.

| Script | BERIL run | Output copy |
|---|---|---|
| `duf4062_ntpase_check.py` | `20261030T221227Z-duf4062-ntpase-check` | `data/ntpase_check_results.json`, `data/duf4062_cooccurrence.tsv` |
| `duf4062_conserved_glu.py` | `20261030T221430Z-duf4062-conserved-glu` | `data/conserved_glu_results.json`, `data/position_conservation.tsv` |
| `duf4062_hmm_glu.py` | `20261030T221521Z-duf4062-hmm-glu` | `data/hmm_glu_results.json` |

## Question

The dashboard called this protein a "putative NACHT-family NTPase" (GO:0017111) because
its STRING orthogroup is COG5635 ("Predicted NTPase, NACHT family domain"). Does the
protein itself have an NTPase domain?

## 1. No P-loop NTPase motifs

The query has no Walker A motif (GxxxxGK[ST]: 0 hits; relaxed [GA]xxxxGK[ST]: 0 hits;
any GK[ST]: 0 hits) and no Walker B motif (hhhhD[DE]: 0 hits). InterProScan, as shown
to the dashboard model, finds only DUF4062 (PF13271, residues 6-87). UniProt lists
DUF4062 at 6-146 and a coiled coil at 170-197. The C-terminal ~165 residues match no
domain.

## 2. NACHT/P-loop domains go with long DUF4062 proteins, not short ones

UniProtKB counts of DUF4062 (IPR025139) proteins that also carry NACHT (IPR007111) or a
P-loop NTPase domain (IPR027417):

| Set | Proteins | With P-loop | With NACHT |
|---|---|---|---|
| all DUF4062 | 4645 | 2537 (54.6%) | 1243 (26.8%) |
| length > 450 aa | 2925 | 2514 (85.9%) | - |
| length <= 450 aa | 1720 | 23 (1.3%) | 1 (0.06%) |

DUF4062 proteins of 450 aa or less, like this 362-aa protein, almost never carry an
NTPase domain. The four reviewed (Swiss-Prot) DUF4062 entries are all large NACHT
proteins: TEP1 from human, mouse and rat (2627-2629 aa) and *Dictyostelium*
DDB_G0287407 (1663 aa). COG5635 groups the short stand-alone DUF4062 proteins with
these multidomain NACHT proteins, so its NTPase label describes the long members, not
this one.

## 3. The conserved DUF4062 Glu is present (Glu83)

Osinski et al. 2026 (PMID:42146377) report that DUF4062 is a TIR-like NADase whose
activity needs a conserved Glu (E97 in *K. pneumoniae* Swarozyc; E1008 in human TEP1).
Two independent estimates locate that Glu in the query:

- **Pairwise conservation.** 375 bacterial DUF4062 proteins of 200-450 aa (identity
  >= 20% over the query's DUF4062 region) were aligned globally to the query. Glu83 is
  identical in 93% of them, the third most conserved position overall after Met1 and
  Gly70 (99%). The next best Glu is Glu38 (73%); Glu81 is at 29%.
- **Pfam HMM.** The query aligns to PF13271 (HMM length 146) over residues 6-146
  (HMM 1-141; i-Evalue 1.4e-53, score 167.1). Glu83 sits at match state 78, whose
  consensus is an uppercase (highly conserved) E with emission probability P(E) = 0.602,
  the highest of any query Glu. Glu81 maps to state 76 (P(E) = 0.197).

Glu83 lies in the motif `GLSYTEKEY` (76-84), next to the conserved Ser78 (82% identical)
and Thr80 (77%). The deep-research report quotes an "acidic-SYT region containing a
putative catalytic glutamate" for the related Evangelion protein Eva01 (E87; bioRxiv
10.64898/2026.06.25.731849); that preprint was not read for this analysis. That Glu83 corresponds to KpSwz E97 is an inference from
family conservation. The KpSwz sequence was not available here (it is in the
preprint's supplement), so it was not aligned directly.

## Conclusions

- The protein lacks the P-loop NTPase machinery that GO:0017111 requires. The NTPase
  label comes from multidomain COG5635 relatives through the shared, non-catalytic
  (for NTP hydrolysis) DUF4062 domain.
- The protein has the architecture of the short bacterial DUF4062 proteins: an
  N-terminal TIR-like DUF4062 domain with the conserved putative catalytic Glu (Glu83),
  a coiled-coil stalk and an unassigned C-terminal region. This matches the Swarozyc
  layout of TIR-like domain, helical stalk and auxiliary domain. Its likely activity is
  NAD+ hydrolysis (NAD+ nucleosidase). This has not been tested for this protein, and
  some DUF4062 proteins are inactive (human NWD1, NWD2 and NPHP3 did not hydrolyse NAD+).
