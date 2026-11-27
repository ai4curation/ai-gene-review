# Cyb5 topology from sequence (Candida albicans, A0A1D8PQP7)

Run `python3 tail_anchor_topology.py` from this directory. Stdlib only, no network;
it reads `../CYB5-uniprot.txt` and prints every number it derives.

This was written because the OpenScientist run that would have addressed this gap
(`kgap-cyb5-topology`) could not be obtained: the service returned nothing for every
submission after 2026-11-26 19:52 (see `genes/BACSU/plsY/plsY-notes.md`). It
therefore covers only the part of the gap that local sequence analysis can reach,
and it is a prediction, not a measurement.

## What the script computes

| Quantity | Value |
|---|---|
| Length | 126 aa |
| Most hydrophobic 19-residue window | 100–118, mean Kyte–Doolittle **+1.87** |
| Whole-protein mean hydropathy | −0.26 |
| Sequence of that window | `SGINFPLIAVGVFLLAFGA` |
| Residues beyond the window | 8 (`YYYKTNFA`), net charge **+1** |
| 15-residue N-flank (85–99) | `KPVEAKHAQSYATED`, net charge −1 |
| Curated heme ligands | His41, His65 — both N-terminal to the segment |
| Curated cytochrome-b5 domain | 6–82, ending 18 residues before the segment |

## What follows, and what does not

**Tail anchor rather than a conventional transmembrane helix.** The single
hydrophobic segment sits at the extreme C-terminus with only 8 residues beyond it.
There is not enough C-terminal sequence for a translocated domain, which is the
defining feature of a tail anchor. The computed peak (100–118) independently
reproduces the record's curated `TRANSMEM 102..121` without being given it, so the
segment assignment does not depend on either source alone.

**The heme domain faces the cytosol.** Both curated heme-ligating histidines, His41
and His65, lie inside the cytochrome-b5 domain (6–82), entirely N-terminal to the
anchor. For a C-terminally anchored protein the N-terminal domain is necessarily on
the cytosolic face, so this part of the predicted topology is firm and does not rest
on charge rules.

**What the charge analysis cannot settle.** The flanking charges are weak and nearly
balanced (N-flank −1, C-flank +1). With only 8 residues and a single lysine beyond
the segment, the positive-inside rule has almost no purchase, so whether that short
tail is translocated or stays cytosolic — equivalently, whether the segment fully
crosses the bilayer or forms a hairpin — is **not** resolved here. That distinction
is genuinely contested for cytochrome b5 proteins generally and should not be
asserted from this analysis.

**What is out of scope entirely.** This constrains the orientation of the functional
domain relative to a bilayer, not *which* bilayer. It is no evidence at all for the
ER or microsomal assignment specifically; that remains transferred from the
*S. cerevisiae* orthologue and from family membership, which is exactly what the
knowledge gap says. No localisation dataset was consulted.

## Transfer to the Nakaseomyces glabratus orthologue

`genes/CANGA/CAGL0L03828g` carries this gap verbatim. The script is not specific to
this protein beyond its hardcoded record path, so the same analysis can be run there
by changing that path; it has **not** been run, and no claim is made about that
protein here.
