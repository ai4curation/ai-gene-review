# Horse IRAK3 (F6QZW8): conservation of experimentally characterised human IRAK3 features

Script: `map_human_features.py` (run with `uv run --no-project --with biopython --with requests python map_human_features.py`). Output: `features.json`.
Horse F6QZW8 (614 aa, Ensembl canonical ENSECAT00000029063) and human Q9Y616 (596 aa) were read from the cached UniProt flat files. Mouse Irak3 Q8K4B2, the knockout donor for the negative-regulation annotations (PMID:12150927), was fetched from UniProt REST. Global alignment, BLOSUM62, gap open -10, extend -0.5, free end gaps.

## Pairwise identity

- Human Q9Y616 vs horse F6QZW8: 485/596 identical (81.4%), covering 100% of human.
- Human Q9Y616 vs mouse Q8K4B2: 454/596 identical (76.2%).

## Feature mapping (human position -> horse F6QZW8 -> mouse Q8K4B2)

| Feature (source) | Human | Horse F6QZW8 | Mouse Q8K4B2 |
|---|---|---|---|
| Death domain (UniProt PROSITE) | 41-106 | 46-111 (62/66 identical) | 41-106 (60/66) |
| Trp74, DD surface 1, MyD88/IRAK4 binding (PMID:38268724) | W74 | W79 | W74 |
| Arg97, DD surface, IRAK1/TRAF6 interaction (PMID:38268724) | R97 | R102 | R97 |
| Ser110, IRAK1 phosphosite / PIN1 (PMID:29686383) | S110 | **N115** | **T110** |
| Pro111 (PMID:29686383) | P111 | P116 | P111 |
| Pseudokinase domain (UniProt PROSITE) | 165-452 | 170-457 (248/288) | 178-465 (240/288) |
| Glycine-rich loop | 171-179 IGEGEIFEV | 176-184 IGEGEIFEV | 184-192 IGEGEIFEV |
| ATP-binding Lys | K192 | K197 | K205 |
| Interchain disulfide Cys (PMID:33238146) | C202 | C207 | **L215** |
| Interchain disulfide Cys (PMID:33238146) | C287 | C292 | C300 |
| Catalytic loop (HRD in active kinases) (PMID:33238146) | CGS291-293 | CGS296-298 | CGN304-306 |
| Mg-binding loop (DFG in active kinases) (PMID:33238146) | DFA311-313 | DFA316-318 | DFA324-326 |
| TRAF6-binding motif region around P478 (PMID:25481771) | 476-482 SIPVEDD | 481-487 SIPVEND | 489-495 SIPVEDD |

## Interpretation

Horse F6QZW8 is a full-length IRAK3. Every residue tested in the human and mouse functional and structural studies is conserved: the death-domain surface residues W74 and R97, the noncanonical CGS catalytic loop and DFA Mg-loop that make IRAK3 a pseudokinase, both cysteines of the human head-to-head disulfide-linked dimer interface, and the C-terminal TRAF6-binding region. Mouse lacks the C202 cysteine. Horse therefore matches human more closely than the mouse knockout donor at the dimer interface.

The one exception is human Ser110, the IRAK1 phosphorylation site that PIN1 recognises (PMID:29686383). It is Asn in horse and Thr in mouse, so the IL-33/PIN1-driven nuclear translocation and pro-inflammatory gene induction described for human dendritic cells cannot be assumed in horse.

Sequence conservation is not an assay. None of these features has been tested experimentally in horse.
