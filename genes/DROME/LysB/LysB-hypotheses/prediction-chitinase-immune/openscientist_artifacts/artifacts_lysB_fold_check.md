# LysB (Q08694) fold/catalytic-residue provenance

Sequence-based test of chitinase-vs-lysozyme identity. Executed in-run (numpy Needleman–Wunsch, no external DB call).

## Inputs
- **LysB** Q08694 precursor (140 aa), signal peptide 1–18 removed → mature 122 aa.
- **HEWL** hen egg-white lysozyme (P00698), the archetypal GH22 C-type lysozyme, catalytic dyad Glu35/Asp52.

## Computed results
| Metric | Result | Interpretation |
|---|---|---|
| LysB(mature) vs HEWL global identity | **50/121 = 41.3%** | High homology to a C-type lysozyme (GH22). |
| Cysteine count (LysB / HEWL) | **8 / 8** | Conserved 4-disulfide C-type lysozyme scaffold. |
| HEWL Glu35 → LysB aligned residue | **E (Glu)** | Catalytic acid conserved. |
| HEWL Asp52 → LysB aligned residue | **D (Asp)** | Catalytic base/nucleophile-assisting residue conserved. |
| GH18 chitinase catalytic motif `DxxDxDxE` in LysB | **Absent** | No chitinase (GH18) active-site signature. |

## Conclusion
LysB has the C-type lysozyme (GH22) architecture — 41% identity to HEWL, both catalytic residues conserved, 8 cysteines / 4 disulfides — and completely lacks the GH18 chitinase catalytic motif. This is independent, computed support that the predicted **chitinase activity (GO:0004568) is a fold misassignment**; the correct MF is **lysozyme activity (GO:0003796)**.

## Code
See `lysB_fold_check.py` (custom NW alignment; sequences hard-coded from UniProt Q08694 and P00698).

Note: a simplified PROSITE PS00128 regex did not match and is uninformative (pattern approximation only); the identity/dyad/cysteine/GH18-motif results above are the robust evidence.
