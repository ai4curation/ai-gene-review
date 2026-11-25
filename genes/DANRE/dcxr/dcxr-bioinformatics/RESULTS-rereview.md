# dcxr (Q567K5) re-review: subfamily placement and catalytic-site conservation

Independent of any prediction files: sequences are fetched directly from UniProt REST by
`compare_sequences_rereview.py` (PEP 723; `uv run --script compare_sequences_rereview.py`).
Subfamily assignments are from the PANTHER 19.0 per-organism classification files.

## Q567K5 versus PTHR44252 members (global BLOSUM62, open -10, extend -0.5)

| Accession | Protein | Subfamily | Length | Identical / aligned | % identity |
|---|---|---|---|---|---|
| Q7Z4W1 | human DCXR | SF2 | 244 | 169 / 244 | 69.3 |
| Q91X52 | mouse Dcxr | SF2 | 244 | 168 / 244 | 68.9 |
| Q920P0 | rat Dcxr | SF2 | 244 | 171 / 244 | 70.1 |
| Q8JIS3 | chicken DER D-erythrulose reductase | SF3 | 246 | 171 / 244 | 70.1 |
| Q6P630 | Xenopus tropicalis dcxr | SF3 | 244 | 175 / 244 | 71.7 |
| Q21929 | C. elegans dhs-21 | SF3 | 251 | 123 / 241 | 51.0 |
| Q9VWP2 | Drosophila CG7322 | SF3 | 242 | 115 / 241 | 47.7 |
| P08074 | mouse Cbr2 | SF1 | 244 | 150 / 244 | 61.5 |

## Human DCXR catalytic triad mapped onto each sequence

| Accession | S136 | Y149 | K153 |
|---|---|---|---|
| Q567K5 | S136 | Y149 | K153 |
| Q91X52 | S136 | Y149 | K153 |
| Q920P0 | S136 | Y149 | K153 |
| Q8JIS3 | S138 | Y151 | K155 |
| Q6P630 | S136 | Y149 | K153 |
| Q21929 | S143 | Y156 | K160 |
| Q9VWP2 | S134 | Y147 | K151 |
| P08074 | S136 | Y149 | K153 |

## Rossmann TGxxxGxG motif (first 25 residues)

- Q567K5: MEISFRGKRALVTGAGKGIGRATAL
- Q7Z4W1: MELFLAGRRVLVTGAGKGIGRGTVQ
- Q91X52: MDLGLAGRRALVTGAGKGIGRSTVL
- Q920P0: MDLGLAGRRALVTGAGKGIGRSTVL
- Q8JIS3: MEPDLSFRGRRALVTGAGKGIGRAV
- Q6P630: MEINFCGQRALVTGAGKGIGRETVK
- Q21929: MPANYDFTDKRILVTGASQGIGKEI
- Q9VWP2: MWTDLAGKVILVTGAGAGIGQALVK
- P08074: MKLNFSGLRALVTGAGKGIGRDTVK

## Interpretation

- Q567K5 is a full-length 244-residue SDR with the TGxxxGxG Rossmann cofactor motif and the
  human DCXR catalytic triad (S136, Y149, K153) at identical positions.
- Q567K5 is about equally similar to the mammalian SF2 DCXR proteins (69-70% identity) and to the
  non-mammalian vertebrate SF3 members chicken DER and Xenopus dcxr (70-72% identity), and less
  similar to the SF1 carbonyl reductase Cbr2 (61.5%) and the invertebrate SF3 members (48-51%).
- Zebrafish and human each have a single PTHR44252 gene in PANTHER 19.0 (zebrafish Q567K5 in SF3,
  human DCXR in SF2), so the SF2/SF3 boundary here separates the mammalian DCXR lineage from the
  non-mammalian vertebrate and invertebrate members; it does not separate a DCXR clade from a
  different-function clade. Characterised SF3 members (C. elegans dhs-21, chicken DER) are
  NADPH-dependent reducers of small sugars (L-xylulose, tetruloses) like SF2 DCXR.
- This is a pairwise identity comparison, not a tree; it does not by itself place the PAINT node.
