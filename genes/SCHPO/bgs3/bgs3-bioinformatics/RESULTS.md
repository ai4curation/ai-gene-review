# Re-analysis of the deposited AlphaFold3 Ghs2-Bgs3 model (PMID:42786154)

## Question

Willet, Jacob et al. 2026 (PMID:42786154) use an AlphaFold3 (AF3) model of Ghs2
(O13789) with Bgs3 (Q9P377) for two things. They propose three binding interfaces,
and they place the Ghs2 GH16 domain next to the Bgs3 glucan-extrusion pore. The main
text reports no confidence metrics. This analysis asks which parts of the model AF3
itself is confident about.

## Data and method

- Input: the authors' AF3 server output, deposited in Mendeley Data
  doi:10.17632/8j46dhsyxr.1 ("Figure 3/AF3_Ghs2_Bgs3" and "Figure S3/AF3_Sbg1_Bgs1").
  It contains the job request, models 0-4, summary confidences and full_data JSON with
  PAE matrices.
- Script: `af3_interface_analysis.py` (run `uv run python af3_interface_analysis.py`).
  It downloads the files to `data/`, which is git-ignored. Raw output is in
  `af3_interface_analysis.out`.
- Contacts: inter-chain residue pairs with any heavy atoms closer than 5 A. For each
  pair, the PAE is the mean of the two directions. Regions come from UniProt features:
  Ghs2 cytosolic 1-170, TM 171-191, linker 192-217, GH16 218-587, C-term 588-636.
  Bgs3 is split into N-term 1-426, TM1-7 427-680, central cytosolic GT48 681-1271,
  TM8-18 1272-1790 and C-term 1791-1826.

## Results

1. Global confidence is in the grey zone. Ghs2-Bgs3 has ipTM 0.67-0.68 and pTM
   0.72-0.73 across all 5 models (ranking score 0.75-0.76). Sbg1-Bgs1 has ipTM 0.58-0.59,
   and Sbg1's own chain pTM is only 0.24-0.25.
2. The deposited Ghs2-Bgs3 job used seed 1940401513. The paper's Methods give seed
   361330275 for this model. The Sbg1-Bgs1 seed matches (815971004). The deposited run
   reproduces the interface residues the paper names, so it is equivalent for that
   purpose, but it is not the run described in Methods.
3. Confidence differs sharply between the three interfaces the paper proposes:

   | Interface (paper) | Region pair | Contact pairs, model_0 | Mean inter-chain PAE | Present across models |
   |---|---|---|---|---|
   | TM-TM | Ghs2 TM x Bgs3 TM8-18 | 14 | 3.5 A | 4.6/5 |
   | TM-TM | Ghs2 TM x Bgs3 TM1-7 | 8 | 4.5 A | 4.5/5 |
   | N-term x catalytic domain | Ghs2 1-170 x Bgs3 681-1271 | 222 | 7.4 A (min 2.9) | 3.4/5 |
   | GH16 x extracellular loops | Ghs2 GH16 x Bgs3 TM1-7 / TM8-18 | 8 / 15 | 22.9 / 21.9 A | 2.3/5 |

   - The TM-TM interface is confident and reproducible.
   - The cytosolic interface is large but only moderately confident. The Ghs2 residues
     involved have mean pLDDT 62, and the whole Ghs2 N-terminal region has pLDDT 43.
   - AF3 does not know where the GH16 domain sits relative to Bgs3: inter-chain PAE is
     about 20-23 A for every GH16 contact. The GH16 domain itself is well folded
     (pLDDT 82). The linker tethering it to the TM is disordered (pLDDT 43).
   - The GH16 contacts change from model to model. In models 0 and 2 many of them are
     with Bgs3 residues 1-7, a disordered terminus (pLDDT 22-26), at PAE about 20 A.
     These are not meaningful contacts. The topology of the Bgs3 N-terminus is itself
     uncertain: UniProt's predicted TM6 and TM7 are only 2 residues apart, so the TM
     count before the cytosolic GT48 region is not settled.
4. The specific residues fit the TM interface. In model_0, Ghs2 L177, L184 and F185
   contact Bgs3 W670, L673, I1334, I1338 and L1341 with PAE 3.2-5.0 A.
   - Bgs3 T1224 (the paper's "I1224") contacts nothing; the nearest Ghs2 residue is
     21.8 A away. This supports reading "I1224" as a typo for I1334.
   - The GH16 catalytic residues E414 and E419, and F449, make no confident contact
     with Bgs3. Y478 touches only Bgs3 Lys4, with PAE 22.9 A.

## Interpretation

- The AF3 model gives real support for one claim: a TM-TM interface between the Ghs2
  signal-anchor helix and two Bgs3 TM clusters. That interface is also what the paper
  tested with ghs2-3A/bgs3-5A, and what the Sbg1 TM-swap rescue supports.
- The headline mechanistic claim, that the GH16 domain sits next to the glucan-extrusion
  pore, is not a confident prediction. AF3 tethers a well-folded GH16 domain by a
  flexible linker at a position it cannot fix relative to Bgs3. The proximity follows
  from the domain being anchored to a TM helix packed against Bgs3, not from a
  predicted GH16-Bgs3 interface.
- Limitations: PAE measures how uncertain the relative placement is, not that it is
  wrong. This analysis uses no membrane-orientation model and cannot locate the pore
  itself. It covers one seed (the deposited one).

## Multi-seed re-run (prepared; needs AlphaFold Server)

AF3 cannot run in this repository's environment: there is no GPU, and the AF3
weights are licensed per user. The re-run is therefore set up for the public
AlphaFold Server, using the same job format the authors deposited.

1. `uv run python make_af_server_jobs.py` writes `af_server_jobs/`. It checks that the
   UniProt sequences of Ghs2 and Bgs3 are identical to the deposited job request (they
   are: 636 and 1826 aa). It contains:
   - `ghs2_bgs3_multiseed.json`: 10 Ghs2+Bgs3 jobs. One uses the paper's Methods seed
     (361330275); 9 use further fixed seeds.
   - `ghs2_controls.json`: 3 Ghs2+Bgs4 jobs (Bgs4 does not co-IP with Ghs2 in the paper)
     and 3 Ghs2+Bgs1 jobs. These test whether AF3 also "finds" a Ghs2 interface with
     synthases Ghs2 is not known to bind.
2. Upload the JSON files at alphafoldserver.com (Upload JSON), download each result zip,
   and unzip them all under `af_server_runs/`, which is git-ignored.
3. `uv run python af3_multiseed_analysis.py data af_server_runs` reports, for each model
   and each job:
   - ipTM;
   - contacts and inter-chain PAE for each Ghs2 region;
   - the GH16 block PAE (median PAE between confident GH16 residues and confident
     partner residues);
   - for Bgs3 runs, the GH16 and TM placement relative to the deposited model_0 after
     superposing on Bgs3.

### Baseline: the 5 deposited models, all from a single seed (`af3_multiseed_deposited.out`)

These 5 diffusion samples share one trunk, so they understate the variability a
multi-seed run would show.
- The Ghs2 TM helix is fixed against Bgs3: CA RMSD 0.4-0.6 A versus model_0, TM contact
  PAE about 4 A.
- The GH16 domain moves: CA RMSD 7.4-13.7 A after superposing on Bgs3 (centroid shift
  5.5-10.8 A).
- The GH16 block PAE is 28.4-28.7 A in every model, near the top of AF3's PAE scale.

So even within the authors' own run, the GH16 position near the Bgs3 pore varies
between samples. Only the TM anchoring is stable.

### What the multi-seed run would decide

If the GH16 position and block PAE stay variable across seeds, while the TM interface
recurs and the Bgs4/Bgs1 controls do not show it, the model supports a specific TM-TM
interface but no defined GH16 placement. If the controls show an equally confident TM
interface, AF3 is packing a lone TM helix against any synthase, and even the TM result
is not specific evidence.
