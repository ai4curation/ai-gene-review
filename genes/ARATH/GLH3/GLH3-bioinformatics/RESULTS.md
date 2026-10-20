# GLH3 (Q9FM66) active-site conservation

## Question

Does GLH3 keep the catalytic arginine and the Ca2+-binding aspartates of PL1
pectate lyases whose activity has been measured? The answer bears on the
pectate lyase activity annotations (IBA, IEA), because no enzyme assay on GLH3
is reported in the cached literature.

## Method

`active_site_conservation.py` downloads the UniProt entries for GLH3 (Q9FM66)
and the two Aspergillus nidulans pectate lyases that seed the PAINT node behind
GLH3's IBA (PTN001271105): plyB (Q00645) and plyA (Q5AVN4). Both references have
kinetics and pH optima in UniProt, with ECO:0000269 evidence from PubMed:16844780.
Each reference is globally aligned to GLH3 (Biopython PairwiseAligner, BLOSUM62,
gap open -10, extend -0.5). For every ACT_SITE and BINDING feature in the
reference entry, the script reports the aligned GLH3 residue. Feature positions
are read from UniProt at run time, not hardcoded.

Run: `uv run python active_site_conservation.py` (output in `output.txt`).

## Results

| Reference | Identity | Active-site Arg | Ca2+ ligands |
|---|---|---|---|
| Q00645 plyB | 35.0% over 306 aligned residues | R219 -> GLH3 R269 | D133/D162/D166 -> GLH3 D191/D213/D217 |
| Q5AVN4 plyA | 35.5% over 296 aligned residues | R226 -> GLH3 R269 | D140/D169/D173 -> GLH3 D191/D213/D217 |

All four functional residues are conserved, and they align to the same GLH3
positions against both references.

UniProt lists the first Ca2+ ligand of GLH3 as D189, not D191. GLH3 has the motif
`S-D188/189-G-D191-G` (residues 188-192 read `SDGDG`), so 189 and 191 are both Asp.
The two-residue difference is just where the aligner places the gap within this
motif; it does not affect the conclusion.

## Interpretation and limits

- GLH3 keeps the catalytic arginine and all three Ca2+-binding aspartates of
  characterized PL1 enzymes. This is consistent with a catalytically competent
  pectate lyase and gives no sign of a pseudoenzyme.
- Residue conservation is necessary but not sufficient for activity. Substrate
  preference, pH optimum and real in-vivo activity of GLH3 are untested here.
- Only two references are used: the PAINT seeds. A plant PL1 enzyme with measured
  activity would be a closer comparator.
