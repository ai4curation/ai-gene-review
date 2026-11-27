# Synpcc7942_0873 (Q31PW6): NTPase motifs, DUF4062 domain context and the conserved Glu

Query: dashboard sequence CP088958.1_900, 362 aa, identical to Q31PW6 (UniParc
UPI000049B91D). The dashboard labels it only "Synechococcus elongatus". NCBI titles contig
CP088958.1 "Synechococcus elongatus PCC 6311 chromosome" (strain PCC 6311, BioSample
SAMN22215176; NCBI esummary frozen in
`../Synpcc7942_0873-dashboard-prediction-evidence/CP088958.1_nuccore_summary.json`). The
protein is therefore from PCC 6311 and identical to the PCC 7942 protein (UniProt
`DR EMBL; CP000100`), and the review is filed under PCC 7942.

Each analysis was run as a BERIL run in the LBNL hackathon BERIL workspace project
`hackathon` (see `projects/LBNL_HACKATHON.md`). That workspace is not part of this
repository, so the run IDs below are provenance labels only. The scripts here and the
committed `data/*.json` copies of each run's `results.json` are the record.

| Script | BERIL run | Output copy |
|---|---|---|
| `duf4062_ntpase_check.py` | `20261030T221227Z-duf4062-ntpase-check` | `data/ntpase_check_results.json`, `data/duf4062_cooccurrence.tsv` |
| `duf4062_conserved_glu.py` | `20261030T221430Z-duf4062-conserved-glu` | `data/conserved_glu_results.json`, `data/position_conservation.tsv` |
| `duf4062_hmm_glu.py` | `20261030T221521Z-duf4062-hmm-glu` | `data/hmm_glu_results.json` |
| `tep1_glu_correspondence.py` | `20261031T012834Z-tep1-glu-correspondence` | `data/tep1_glu_results.json` |

Exact invocations (the scripts write to `$BERIL_RUN_DIR`; set it to any output
directory). `data/CP088958.1_900.fasta` is the dashboard query sequence:

```
python3 -I duf4062_ntpase_check.py --fasta data/CP088958.1_900.fasta
python3 -I duf4062_conserved_glu.py --fasta data/CP088958.1_900.fasta   # needs biopython
uv run --no-project --with pyhmmer python -I duf4062_hmm_glu.py --fasta data/CP088958.1_900.fasta
uv run --no-project --with pyhmmer --with biopython python -I tep1_glu_correspondence.py --hmm data/PF13271.hmm
```

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
NTPase domain. The four reviewed (Swiss-Prot) DUF4062 entries are all large P-loop
proteins: TEP1 from human, mouse and rat (2627-2629 aa, with NACHT) and *Dictyostelium*
DDB_G0287407 (Q54KD0, 1663 aa, P-loop domain IPR027417 without a NACHT match). COG5635 groups the short stand-alone DUF4062 proteins with
these multidomain NACHT proteins, so its NTPase label describes the long members, not
this one.

## 3. The conserved DUF4062 Glu is present (Glu83)

Osinski et al. 2026 (PMID:42146377) report that DUF4062 is a TIR-like NADase whose
activity needs a conserved Glu (E97 in *K. pneumoniae* Swarozyc; E1008 in human TEP1).
Two independent estimates locate that Glu in the query:

- **Pairwise conservation.** 375 bacterial DUF4062 proteins of 200-450 aa (identity
  >= 20% over the query's DUF4062 region) were aligned globally to the query. They are
  the first 400 hits of one UniProt search, not a random sample, and conservation is
  scored against the query residue, so this estimate is query-centred; the HMM below is
  not. Glu83 is
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

### 3b. Glu83 corresponds to the tested TEP1 Glu1008

The other Glu tested by mutation, human TEP1 E1008 (Q99973; DUF4062 at 886-1113), was
mapped onto the same PF13271 HMM with `tep1_glu_correspondence.py`. The HMM is the saved
copy from the HMM run above (committed as `data/PF13271.hmm`), because InterPro and UniProt REST returned HTTP 500 on
2026-10-31; sequences were fetched through NCBI. TEP1 hits PF13271 at 901-1015 (HMM
2-85, i-Evalue 5.6e-19). TEP1 E1008 also maps to match state 78, the
state of the query's Glu83. The flanking residues agree position by position: query
`S78-Y-T80-E81-K-E83` against TEP1 `S1003-V-T1005-E1006-M-E1008`.

A plain pairwise local alignment of the two DUF4062 regions (BLOSUM62, gap open 10,
extend 1; 116 aligned pairs, 29% identity) does not recover this. It inserts a 7-residue
gap just upstream and puts Glu83 opposite TEP1 Tyr998. At this divergence the profile
mapping, which agrees with the shared motif, is the more reliable of the two, but the
correspondence is still an alignment inference, not a structural one.

## 4. Independent structural checks (not run here)

Two dashboard reviewers independently assessed the same protein by structure, and their
results are consistent with sections 1-3. Summarised, not re-run: MorganP reports no
CDD or InterPro link to NTPase domains and reads the predicted structure as a TIR domain
plus a winged helix. JMC-Claude-SCOP reports a SCOPe 2.08 comparison of AF-Q31PW6-F1 in
which residues ~1-168 give TIR (c.23.2) as the strongest superfamily over-representation
of 524 tested, residues ~206-348 return ten hits that are all winged-helix DNA-binding
domains (a.4.5), the P-loop signal looks like generic alpha/beta similarity, and a
TIR-like domain plus a winged helix leaves no room for NACHT in 362 residues. Both sets
of hits are individually weak, so these are fold-level candidates.

This adds a domain to the architecture in section 3: the C-terminal region called
unassigned there is a predicted winged helix, which matches the helix-turn-helix/winged
fold of the Swarozyc auxiliary domain.

## Conclusions

- The dashboard's basis for GO:0017111 is refuted: the call is a NACHT (P-loop) NTPase,
  and the protein has no NACHT or P-loop domain and no Walker A or Walker B motif.
  GO:0017111 itself is fold-agnostic, but no other NTPase fold or activity is indicated.
  The NTPase label comes from multidomain COG5635 relatives through the shared DUF4062
  domain, which does not hydrolyse NTPs.
- The protein has the architecture of the short bacterial DUF4062 proteins: an
  N-terminal TIR-like DUF4062 domain with the conserved putative catalytic Glu (Glu83,
  at the HMM position of TEP1 E1008),
  a coiled-coil stalk and a C-terminal region that structural review predicts to be a
  winged helix (section 4). This matches the Swarozyc layout of TIR-like domain, helical
  stalk and auxiliary domain, down to that domain's winged fold. Its likely activity is
  NAD+ hydrolysis (NAD+ nucleosidase). This has not been tested for this protein, and
  some DUF4062 proteins are inactive (human NWD1, NWD2 and NPHP3 did not hydrolyse NAD+).
