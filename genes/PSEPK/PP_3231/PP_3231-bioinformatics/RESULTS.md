# PP_3231 (Q88HX2) bioinformatics results

Two analyses, each run through `beril run` in the BERIL hackathon project
(`/home/cmungall/.beril/projects/hackathon/runs/`). Outputs are copied here unchanged.

## 1. Ere-family catalytic residues (`catalytic_site.py`, `catalytic_site/`)

Run `20261030T213637Z-pp3231-catalytic-site`. Semi-global pairwise alignments (Biopython
PairwiseAligner, BLOSUM62, gap -10/-0.5, free end gaps) of the dashboard query (identical to
Q88HX2, 455 aa) against EreA (P07684), EreB (P05789), EreC (C7C425), EreD (A0A0H4JQQ7) and
*B. cereus* Bcr136 (PDB 2QGM chain A). EreC catalytic residues are taken from Zielinski et al.
2021 (PMID:33741980): E47 (positions H50), H50 (general base), E78, R261 (K in EreB/EreD), H289.
The script checks that C7C425 carries E/H/E/R/H at those positions (it does).

- Identity of PP_3231 over aligned positions: EreA 28.5% (330 pairs), EreB 25.9% (351), EreC 27.8% (352), EreD 24.0% (367), Bcr136 27.7% (390). PP_3231 is equidistant from the macrolide-inactivating Eres and from the non-macrolide esterase Bcr136.
- PP_3231 residues at the EreC catalytic positions: **E60, H63, E91, R268, H297**. All five are conserved. Local windows: `LLGEASHGSSE` (E60/H63; EreC `LGEGAHFVAE`), `VAVEADW` (E91), `WNLRDRHM` (R268, followed by Asp as in EreC R261-D262), `VWAHNSHIG` (H297; EreC `LAHNNHL`).
- Bcr136 has His (H282) at the EreC R261 position, whereas PP_3231 has Arg, like EreA/EreC. A single residue does not decide substrate class.

Interpretation: the Ere metal-independent water-activating catalytic set is intact, so PP_3231 is
most likely an active Ere-family hydrolase (not a pseudoenzyme). These are pairwise sequence
alignments, not a structure superposition, and ~25-28% identity cannot discriminate macrolide
esterases from other Ere-family esterases. Bcr136 keeps the same catalytic residues yet does not
inactivate macrolides (PMID:22303981).

## 2. Fitness Browser data for PP_3231 and its neighbours (`fb_fitness.py`, `fitness/`)

Run `20261030T213340Z-pp3231-fitness`. `just fetch-fitness` failed (no FEBA source reachable; the
Fitness Browser web site returns HTTP 403), so KT2440 (orgId Putida) RB-TnSeq data were read from
the BERDL lakehouse copy (`kescience.fitnessbrowser`).

- PP_3231 was measured in 300 experiments (128 carbon source, 104 nitrogen source, 21 stress, 15 reactor, others R2A controls/supernatants). Fitness range -0.83 to +0.59; **no experiment** passes |fit| >= 1 and |t| >= 4. No entry in `specificphenotype`.
- No experiment uses a macrolide or any other ribosome-targeting antibiotic; the only antibiotic-like stresses are polymyxin B and fusaric acid (PP_3231 fit +0.44/+0.50 and +0.43, not significant).
- Top cofitness partners are weak (maximum cofit 0.29, PP_0199 stomatin-family protease), i.e. uninformative.
- Neighbours (Fitness Browser coordinates): PP_3228 and PP_3229 (+, putative aliphatic sulfonate-binding proteins), PP_3230 (+, phosphoribosyl transferase domain protein, 3666365-3667057), **PP_3231 (-, 3667319-3668686)**, PP_3232 (-, GNAT acetyltransferase), PP_3233 (+, Crp/Fnr regulator). None has a strong phenotype either.
- STRING (in the dashboard evidence) links PP_3231 to PP_3230 (score 973, including fusion) and to pcm (protein-L-isoaspartate O-methyltransferase, score 900, fusion/neighbourhood). The eggNOG/KEGG "protein-L-isoaspartate O-methyltransferase (EC 2.1.1.77)" label shown on the dashboard is consistent with propagation from such fusion proteins; PP_3231 has no methyltransferase domain.

Interpretation: RB-TnSeq gives no condition in which PP_3231 matters, and macrolides were never
tested, so fitness neither supports nor refutes an antibiotic-resistance role.
