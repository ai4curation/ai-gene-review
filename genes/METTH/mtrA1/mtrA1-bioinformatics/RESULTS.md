# mtrA1 (O27227) pairwise identity

Command (run from the repository root):

    uv run python genes/METTH/mtrA1/mtrA1-bioinformatics/pairwise_identity.py O27227 P80184 O27134 Q58261

Global alignment, BLOSUM62, gap open -10, extend -0.5; sequences fetched live from UniProt.

| Pair | Identity (aligned columns) |
|---|---|
| O27227 mtrA1 Delta H vs P80184 MtrA M. marburgensis (strain Marburg) | 236/238 = 99.2% |
| O27227 mtrA1 vs O27134 mtrA2 (MTH_1062, 183 aa) | 109/180 = 60.6% |
| O27227 mtrA1 vs Q58261 MtrA M. jannaschii | 132/236 = 55.9% |
| P80184 vs O27134 | 110/180 = 61.1% |

Interpretation: the Delta H mtrA1 product is essentially identical to the
strain-Marburg MtrA used in all the biochemical work (PMIDs 8898900, 9461302,
9801157, 8001564, 7737157, 38530900), so those results transfer to O27227 with
high confidence. mtrA2 (183 aa) aligns only over the soluble cobamide domain
(~180 columns) at ~60% identity and lacks the C-terminal juxtamembrane and
transmembrane segment, matching the "cytoplasmic MtrA homologue" class of
PMID:27324530. Residue 84 of O27227 is His (sequence ...EVQGH84...), the
experimentally identified cobalt ligand.
