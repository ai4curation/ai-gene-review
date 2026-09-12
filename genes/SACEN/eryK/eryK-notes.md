# eryK (P48635, CYP113A1) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`) and the erythromycin
pathway concept (`terms/erythromycin_biosynthesis/`). MIBiG BGC0000055; GenBank CAM00054.1
→ UniProt **P48635** (CPXK_SACEN), gene *eryK*.

## Function

EryK (**CYP113A1**) is the cytochrome P450 that catalyzes the **C-12 hydroxylation** of a late
erythromycin intermediate — one of the **final steps** of erythromycin A biosynthesis (EC
**1.14.13.154**). It converts erythromycin D → erythromycin C (and erythromycin B →
erythromycin A).

- "Identification of a Saccharopolyspora erythraea gene required for the final hydroxylation
  step in erythromycin biosynthesis"; "eryK encodes a 44-kDa protein which... belongs to the
  P450 monooxygenase family." [PMID:8416893 — Stassi et al. 1993].
- "Overproduction and characterization of the erythromycin C-12 hydroxylase, EryK";
  "Hydroxylation of C-12 is one of the final steps in the biosynthesis of erythromycin A...
  the P-450 monooxygenase responsible for erythromycin C-12 hydroxylation." EryK strongly
  prefers erythromycin D over erythromycin B as substrate [PMID:7849045 — Lambalot et al. 1995].

## Annotation review

A genuine catalytic P450; all GOA terms accurate and experimentally supported → **ACCEPT**:
monooxygenase activity (IEA + IMP), iron ion binding (IEA), heme binding (IEA + IDA),
oxidoreductase activity acting on paired donors with O2 (IEA) and the more specific
NAD(P)H-dependent class GO:0016709 (IDA), NADP binding (IDA), and macrolide biosynthetic
process (GO:0033068; IDA + IMP). No GO MF term exists for EC 1.14.13.154 → propose
"erythromycin 12-hydroxylase activity". GO:1901115 (erythromycin biosynthetic process) is a
more specific BP child of the annotated GO:0033068 and is added in core_functions.

## References
- PMID:8416893 — Stassi et al. 1993, *J Bacteriol*: eryK identification (final hydroxylation). VERIFIED.
- PMID:7849045 — Lambalot et al. 1995, *Biochemistry*: EryK C-12 hydroxylase characterization. VERIFIED.
