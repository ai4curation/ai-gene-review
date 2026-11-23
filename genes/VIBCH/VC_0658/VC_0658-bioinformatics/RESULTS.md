# VC_0658 (Q9KU65, CdgI) bioinformatics: catalytic motifs, membrane segments and identity to the dashboard sequence

## Question

The KBase gene-annotate dashboard call for `NZ_JABEED010000006.1_102` describes an "Integral inner-membrane c-di-GMP-binding protein containing GGDEF and EAL domains" and deliberately assigns no catalytic activity. Two questions follow:

1. Are the GGDEF (diguanylate cyclase) and EAL (phosphodiesterase) catalytic motifs intact, or is either domain degenerate?
2. How close is the dashboard sequence to the N16961 reference entry Q9KU65 (VC_0658)?

## Inputs

- `data/NZ_JABEED010000006.1_102.fasta`: the dashboard sequence (681 aa).
- Q9KU65 sequence (685 aa) from `../VC_0658-uniprot.txt`.

## Method

`vc0658_motifs.py` was run through BERIL provenance as
`beril run --name vc0658-motifs` (run `20261030T213403Z-vc0658-motifs`). It does three things:

- a Needleman-Wunsch global alignment of the two sequences (identity scoring), written to `alignment.txt`;
- regular-expression searches on Q9KU65 for the GGDEF A-site (`GG[DE]EF`), an RxxD I-site within 12 residues upstream of it, and conserved EAL-domain catalytic positions (`ExLxR`, the loop-6 `DDFGxG`, `KxD`, `ExxE`, `ExVE`, and the `N` of the INxS stretch);
- a Kyte-Doolittle hydropathy scan (window 19, threshold 1.6).

All numbers are in `results.json`.

## Results

- **Identity.** 679 of 681 aligned positions are identical, giving 99.71% identity over the dashboard length. The differences are N170H, C376S, and a 4-residue deletion (A531, I533, T534, G535 of Q9KU65) in the dashboard sequence. The deletion lies in the EAL domain, between the EAL motif (447-451) and the DDFGTG loop (571-576). It removes none of the catalytic positions listed below.
- **GGDEF domain.** The A-site motif `GGDEF` is intact at residues 321-325 (context `AWTKNDYLSARIGGDEFAVLIP`). No RxxD I-site is present in the 12 residues upstream. This agrees with PMID:26506097, which lists VC0658 among the GGDEF-EAL proteins "lacking the RxxD motif".
- **EAL domain.** All the conserved catalytic positions checked are present: `EALIR` (447-451, a full ExLxR), `INIS` (508-511, the conserved Asn), `ELEITE` (539-544), `DDFGTG` (571-576, loop 6), `KIDR` (592-595, the conserved Lys) and `EGVE` (628-631). On sequence grounds the EAL domain is a canonical, presumably active c-di-GMP phosphodiesterase domain.
- **Membrane segments.** The scan finds two hydrophobic segments, residues 17-36 (`SVFLVSVLLGLCFSFYHTLS`) and 162-181 (`VLLFDLLRNTLLTTILLLFF`), which flank a roughly 125-residue loop. This fits the dashboard's DeepTMHMM result ("TM · 2 helices", inner membrane). The loop is presumably periplasmic and the GGDEF-EAL module cytoplasmic.

## Interpretation

Both catalytic domains are sequence-intact, so on motif grounds the protein could be bifunctional. The only functional data on VC0658 point to net phosphodiesterase output. Deleting VC0658 (*cdgI*) in a Δ*crp* background increased biofilm formation (PMID:18708497). The protein binds c-di-GMP without an I-site, which suggests binding at the EAL domain (PMID:26506097). No purified-enzyme DGC or PDE assay has been reported. Motif integrity is necessary, but not sufficient, for activity.

## Limitations

- These are motif and hydropathy checks only. No HMM rescan or structural model was made; the domain calls come from UniProt/InterPro (PF00990, PF00563).
- The hydropathy threshold is heuristic. Topology is taken as consistent with, not independent of, the dashboard's DeepTMHMM call.
