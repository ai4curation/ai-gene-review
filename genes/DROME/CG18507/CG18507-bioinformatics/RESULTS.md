# CG18507 vs TMEM268: isoform and ortholog comparison

Script: `compare_tmem268.py` (run with `uv run compare_tmem268.py`; sequences fetched live from UniProt REST).
Raw output: `results-tmem268.json`.

## CG18507 UniProt products (FBgn0028527)

All five UniProt entries for CG18507 are unreviewed TrEMBL records; there is no Swiss-Prot canonical entry.

| Accession | Length | Residues identical to M9PBB3 from the N-terminus |
|---|---|---|
| M9PBB3 | 510 | 510 (benchmark accession) |
| M9PCX0 | 510 | 491 |
| M9PFU6 | 499 | 492 |
| Q9VJW7 | 513 | 492 |
| Q7KTB0 | 514 | 438 |

The five products share an identical N-terminal region, including both Phobius transmembrane helices (292-310, 316-339)
and the region that aligns to vertebrate TMEM268. They differ only in their C-terminal 20-75 residues, consistent with
alternative 3' exons. M9PBB3 is a full-length alternative product of the gene, not a fragment.

## M9PBB3 vs vertebrate TMEM268 (same PANTHER subfamily PTHR31193:SF1)

Local alignment, BLOSUM62, gap open -11 / extend -1:

| Target | Fly span | Target span | Aligned pairs | Identity | Similarity |
|---|---|---|---|---|---|
| Human TMEM268 Q5VZI3 (342 aa) | 227-399 | 39-215 | 164 | 30.5% | 52.4% |
| Mouse Tmem268 Q8R239 (342 aa) | 227-486 | 40-331 | 251 | 29.1% | 49.0% |

The aligned core spans the two predicted transmembrane helices of both proteins (fly 292-339; human UniProt TRANSMEM 105-125
and 132-152). Fly residues 1-226 (largely disordered and low-complexity per MobiDB-lite) have no counterpart in the
vertebrate proteins, so the fly protein is an N-terminally extended member of the family.

## Interpretation and limits

- Pairwise similarity is consistent with, but does not by itself establish, orthology; the ortholog assignment rests on
  shared PANTHER subfamily membership (PTHR31193:SF1, a single-subfamily family).
- This analysis says nothing about whether the integrin-stabilizing role reported for mammalian TMEM268 is conserved;
  Drosophila has no beta4 integrin or CD11b ortholog.
