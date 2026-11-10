# LOC541855 (A0A1D6L7U4, ZmTSAlike) bioinformatics checks

Script: `check_active_site.py` (fetches live UniProt records; raw output in `RESULTS_raw.txt`).

## 1. Identity of the UniProt entry

The ZmTSAlike forward expression primer given in PMID:18430213 (CGCATATGGCCAACGGCGGCG)
encodes the N-terminus MANGG, which is exactly the N-terminus of A0A1D6L7U4 (MANGGAAAGK...).
A0A1D6L7U4 is 274 aa, whereas IGL is described as a 339-aa protein (PMID:11106389).
A0A1D6L7U4 therefore corresponds to ZmTSAlike, not to IGL, even though NCBI Gene 541855 and
RefSeq NP_001105002.2 name it "indole-3-glycerol phosphate lyase 1" (igl1); the two genes are
adjacent on chromosome 1L (1.6 kb apart, PMID:11106389).

## 2. Catalytic residues

The PROSITE PS00167 motif matches A0A1D6L7U4 at 57-70 (IEVGVPYSDPLADG) and E. coli TrpA
(P0A877) at 48-61 (LELGIPFSDPLADG). The two catalytic residues of E. coli TrpA (E49, D60;
UniProt ACT_SITE) align to E58 and D69 of A0A1D6L7U4. Both catalytic residues are retained
in ZmTSAlike.

The A0A1D6L7U4 record places ACT_SITE features at 58 (E) and 68 (A). Position 68 is an
alanine; the catalytic aspartate is D69. The second ACT_SITE feature appears to be offset by
one residue.

## Interpretation

Retention of the catalytic Glu/Asp pair means that the absence of detectable
indole-3-glycerol-phosphate cleavage by recombinant ZmTSAlike (PMID:18430213) is not
explained by loss of the catalytic acid/base residues. Sequence conservation alone does not
show activity.
