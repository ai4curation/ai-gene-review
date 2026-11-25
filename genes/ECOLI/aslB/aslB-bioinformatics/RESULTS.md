# AslB and YdeM vs characterised anaerobic sulfatase-maturating enzymes

Script: `map_anSME_residues.py` (run from this folder with
`uv run --with biopython python map_anSME_residues.py > map_anSME_residues.out`).
Raw output: `map_anSME_residues.out`.

Inputs, all fetched at run time from the UniProt REST API: the Cys-type anSME of
Clostridium perfringens (anSMEcpe, Q0TTH1, the structurally characterised reference),
E. coli K-12 AslB (P25550) and YdeM (P76134), and the Ser-type anSME AtsB of
Klebsiella pneumoniae (Q9X758). The 17 BINDING/ACT_SITE features of Q0TTH1 (three
[4Fe-4S] clusters, SAM-binding residues, the catalytic base) are parsed from its UniProt
flat file and mapped through global pairwise alignments (BLOSUM62, gap open -10, extend
-0.5; Biopython PairwiseAligner).

## Results

- Identity to anSMEcpe over aligned pairs: AslB 34.9%, YdeM 35.0%, AtsB 33.2%.
  AslB vs YdeM 43.2%; AslB vs AtsB 44.7%; YdeM vs AtsB 36.4%.
- Radical SAM motif: AslB CNLNCDYC at 21, YdeM CNLKCDYC at 12 (anSMEcpe CNLKCTYC at 15).
- AslB keeps 16 of 17 reference features: all 11 cysteine ligands of the three [4Fe-4S]
  clusters (radical SAM cluster, auxiliary clusters I and II of the SPASM domain), the
  catalytic proton acceptor (anSMEcpe D277 = AslB D298) and 4 of 5 SAM-binding residues
  (L195 is V202, a conservative change).
- YdeM keeps all 17 reference features: 11 cluster cysteines, 5 SAM-binding residues and the catalytic base (anSMEcpe D277 = YdeM D279).
- For comparison the characterised Ser-type maturase AtsB keeps 15 of 17 (two SAM-contact
  residues differ), so the small differences seen in AslB are within the range of a
  functional anSME.

## Interpretation (inference, not experiment)

Neither E. coli paralog shows any sign of degeneration of the catalytic machinery that
the anSMEcpe structures define: all three [4Fe-4S] cluster sites and the catalytic
aspartate are intact. On sequence alone both are expected to be competent radical SAM
enzymes that perform a two-electron oxidation of a substrate bound to the SPASM domain.
This does not identify the substrate: conservation of the catalytic core is shared with
every SPASM-domain enzyme of the anSME-like group, including those that make peptide
cross-links rather than formylglycine, and E. coli K-12 deletion mutants show that these
paralogs are not required for Cys-type sulfatase maturation (PMID:17303125). AslB is
closer to the Ser-type AtsB (44.7%) than YdeM is (36.4%), which is consistent with AslB
being the candidate maturase of the adjacent, Ser-type putative sulfatase AslA, but no
experiment has tested that. YdeM is likewise encoded next to a predicted Ser-type
sulfatase, YdeN (UniProt P77318; gene adjacency taken from UniProt locus tags b1497/b1498,
not computed by this script).
