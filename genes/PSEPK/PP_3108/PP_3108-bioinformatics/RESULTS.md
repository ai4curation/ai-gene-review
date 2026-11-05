# PP_3108 (Tke2) vs dashboard protein NZ_SPUT01000035.1_2: windowed identity, toxin domains and locus partners

Run: `just all` (BERIL run `projects/hackathon/runs/20261030T211644Z-pp3108-tke2-windowed-identity`).
All numbers below are in `results.json`.

## Inputs

- Query: dashboard protein NZ_SPUT01000035.1_2 (1409 aa). It is WP_135192713.1 (locus E4L40_RS19050, complement 1194..5423) on contig NODE_35 of *P. putida* strain KB3, from the NCBI CDS translation of NZ_SPUT01000035.1.
- Reference: KT2440 PP_3108 / Tke2 (UniProt Q88I91, 1385 aa).
- Locus partners from the KB3 contig: WP_223271142.1 (149 aa, directly downstream of the Rhs gene, its start overlapping the Rhs stop), WP_003248404.1 (DcrB/DUF1795), WP_103444332.1 (VgrG). KT2440 partners: PP_3109 (Q88I90, Tki2), PP_3107 (Q88I92, DUF1795), PP_3106 (Q88I93, VgrG1) and PP_4084 (Q88FK7, DUF1795).
- Pfam HMMs from InterPro: PF05488 PAAR_motif, PF25799 prePAAR_I, PF14411 LHH, PF14412 AHH, PF12639 Colicin-DNase, PF01844 HNH, PF14414 WHH, PF13930 Endonuclea_NS_2.

## Results

**The full-length identity hides a swapped C-terminal toxin.** Over the whole length the
global alignment gives 1242 identical residues in 1381 aligned pairs (89.9%). Identity is
not uniform along the length:

| Query region | Identity (over region length) |
|---|---|
| 1-58 prePAAR (class I) | 58/58 (100%) |
| 59-148 PAAR | 89/90 (98.9%) |
| 149-1253 Rhs/YD-repeat shell up to the DPIGL motif | 1056/1105 (95.6%) |
| 1254-1409 C-terminal toxin region (after DPxGL) | 39/156 (25.0%) |
| 1313-1409 LHH domain | 21/97 (21.6%) |

In 100-residue windows the identity is 0.96-1.00 from residue 1 to 1100 (with one dip to 0.89 at 801-900). It falls to 0.80 at 1151-1250, then 0.53, 0.32 and 0.21 in the last three windows (1201-1300, 1251-1350, 1301-1400).

The C-terminal boundary motif of the Rhs core reads VTQDPIGL at residue 1249 in both proteins. Bernal et al. 2017 write it PxxxxDPxGL. After it, the proteins share only a ~60-residue proximal segment: a local alignment of the two toxin regions covers query toxin residues 2-71 at 45.5% identity (shuffle z = 13.0). The query has a second DPYGL at 1271, which PP_3108 lacks (it reads DPWGW). The LHH segment, residues 1313-1409, has no significant similarity to the PP_3108 C-terminus (best local alignment 27 pairs, shuffle z = 3.3).

**Toxin domain HMMs.**
- Query: LHH (PF14411) hits the C-terminus at 1313-1397 (i-Evalue 2.7e-13 on the full sequence; 6.2e-15 on the excised toxin region).
- PP_3108: the C-terminus gives only weak LHH fragments (i-Evalue 0.005 and 0.02) and no significant hit to the other nuclease HMMs tested. UniProt/InterPro place it in the colicin/pyocin DNase superfamily (IPR037146, Gene3D 3.90.540.10) and the His-Me finger superfamily. Bernal et al. 2017 describe it as an HNH-superfamily nuclease domain similar to colicin E7 and pyocin S1.
- Both C-termini are therefore HNH/ENDO VII-superfamily (His-Me finger) predicted nucleases, but they are different toxin modules.

**The immunity genes differ as well.** WP_223271142.1, the gene directly downstream of the query and in the position of tki2, is only 18.0% identical to Tki2 (PP_3109) over 111 aligned pairs in a global alignment. The best local alignment has 19 pairs with shuffle z = 2.4, so the two proteins are not detectably related. By contrast, the N-terminal partners are conserved. The DUF1795 (Eag-family) chaperone WP_003248404.1 is 100% identical over 155 residues to PP_3107; PP_3107 has an 18-residue N-terminal extension, aligned at 19-173. The VgrG WP_103444332.1 is 76.2% identical over 617 pairs to VgrG1 PP_3106.

**The PAAR and prePAAR motifs are present.**
- PAAR_motif (PF05488) hits residues 69-140 in both proteins (i-Evalue 6e-21 in the query, 1.8e-21 in PP_3108).
- Class I prePAAR (PF25799) hits residues 1-58 in both (1e-23).
- The prePAAR region carries a strongly hydrophobic stretch: Kyte-Doolittle 19-residue windows of ≥1.6 cover residues 13-64. This matches the two Phobius TM segments in UniProt (16-36 and 43-64), though DeepTMHMM called the protein globular.
- An N-terminal hydrophobic prePAAR region, together with an adjacent DUF1795/Eag chaperone gene, is the organization of class I prePAAR Rhs effectors.

## Interpretation

The query is the KB3 allele of the KT2440 K1-T6SS Tke2 locus. Its delivery module is
conserved: the prePAAR, PAAR and Rhs shell, the Eag chaperone and VgrG. Its C-terminal
toxin and the cognate immunity gene are a different cassette: an LHH-family predicted
nuclease with an unrelated immunity protein. Such a swap is typical of Rhs polymorphic
toxins. Two kinds of property follow:

- Properties of the N-terminal part transfer from PP_3108 with high confidence: K1-T6SS-dependent secretion, PAAR/VgrG spike association and the Eag chaperone requirement.
- The toxin-specific properties of Tke2 do not transfer: the toxic domain itself, its neutralisation by Tki2 and the colicin-like DNase fold. For the query, toxin activity rests only on the LHH domain prediction. No LHH-family toxin from this locus has been assayed.
