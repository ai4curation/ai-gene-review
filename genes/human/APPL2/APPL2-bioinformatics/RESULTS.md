# APPL2 (Q8NEU8) sequence checks

All numbers below are produced by `appl_orthology.py`, which fetches the four
sequences live from the UniProt REST API and asserts their lengths before scoring.
Re-run with `uv run python appl_orthology.py`; the raw table is `appl_orthology.tsv`.

## 1. The mouse-to-human orthology transfers are sound

Twenty-four ISS rows (GO_REF:0000024) and nineteen IEA rows (GO_REF:0000107) on
human APPL2 are transfers from one mouse donor, Appl2/Q8K3G9. Their safety rests
on the orthology being unambiguous, so the identity was measured directly:

| pair | identity | aligned columns | note |
|---|---|---|---|
| Q8NEU8 vs Q8K3G9 | 92.7% | 614/662 | human APPL2 vs mouse Appl2 (the ISS/IEA donor) |
| Q9UKG1 vs Q8K3H0 | 98.3% | 695/707 | human APPL1 vs mouse Appl1 |
| Q8NEU8 vs Q9UKG1 | 53.9% | 356/661 | human APPL2 vs human APPL1 (paralogs) |
| Q8K3G9 vs Q8K3H0 | 53.9% | 352/653 | mouse Appl2 vs mouse Appl1 (paralogs) |

Human and mouse APPL2 are 92.7% identical over a full-length global alignment,
with no length difference beyond two residues (664 vs 662 aa). The orthology is
1:1 and unambiguous, so the ISS/IEA rows do not carry an ortholog-assignment risk;
where they are questionable it is because of what the mouse experiment showed, not
because of the transfer.

The paralog identity, 53.9%, reproduces the 52% that King et al. report by ClustalW
(PMID:23055524). It is high enough that APPL1 and APPL2 share the same BAR-PH-PTB
architecture and heterodimerise, and low enough that they are not interchangeable:
the two proteins have different Rab partners, opposite effects on adiponectin
signalling, and a documented difference in Akt2 binding. An experiment that
perturbs both therefore does not establish what either one does.

## 2. UniProt domain spans in Q8NEU8

| domain | span | length | first residues |
|---|---|---|---|
| BAR | 3-268 | 266 aa | AVDKLLLEEALQ... |
| PH | 277-375 | 99 aa | LIQKAGYLNLRN... |
| PID (PTB) | 488-637 | 150 aa | SLLQQMFIVRFL... |

## 3. Residue-level checks (all positions from PMID:23055524)

King et al. name three human APPL2 PH-domain residues as the candidate
non-canonical inositol-phosphate contact surface, by structural superposition on
the ARHGAP9 PH domain bound to Ins(1,4,5)P3. All three are present at the stated
positions:

| position | residue claimed | residue found | in PH domain | mouse Appl2 | human APPL1 |
|---|---|---|---|---|---|
| 287 | R | R | yes | R | R |
| 289 | K | K | yes | K | K |
| 297 | W | W | yes | W | W |

The patch is intact in human APPL2 and conserved in mouse Appl2, which is
consistent with the IDA phosphoinositide-binding rows (PMID:18034774) and with
their transfer between the two species. It is equally conserved in APPL1, so it
does **not** discriminate the two paralogs and should not be used to argue that
lipid binding is an APPL2-specific property.

The putative nuclear localisation signal quoted for APPL2, 151-PKKKENE-157, is
also present verbatim, sits inside the BAR domain (loop 2), and is conserved in
mouse Appl2 — but the aligned span in human APPL1 is SKKREND, which loses the
basic-cluster character at two of the three lysine positions. This is one of the
few positions examined where the paralogs genuinely differ, and it is on the face
that the APPL2 crystal structure shows is masked by the PH domain.

## Caveats

Pairwise global alignment with BLOSUM62 and affine gaps (-11/-1) is used
throughout; percentages are computed over aligned columns only, so they exclude
terminal gaps. The residue roles are structural inferences made by King et al.
from a superposition, not from a liganded APPL2 structure, and no APPL2-Ins(1,4,5)P3
complex has been solved. Nothing here tests binding; it tests only that the
residues the literature names are the residues the sequence has.
