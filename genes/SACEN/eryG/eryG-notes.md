# eryG (A4F7P5) — review notes

Erythromycin pathway concept (`terms/erythromycin_biosynthesis/`), MIBiG BGC0000055; GenBank
CAM00069.1 → UniProt **A4F7P5**, gene *eryG*.

## Function

EryG is the **SAM-dependent erythromycin 3''-O-methyltransferase** (EC 2.1.1.254): it
3''-O-methylates the L-mycarose sugar to give **L-cladinose**, the final tailoring step that
converts erythromycin C → erythromycin A (and erythromycin D → erythromycin B).

- "eryG, the structural gene for erythromycin O-methyltransferase from Saccharopolyspora
  erythraea" — cloned, mutated, and expressed in *E. coli* [PMID:2185226 — Paulus et al. 1990].

## Annotation review

Cleanly annotated — including the **specific** MF term:
- GO:0102307 erythromycin 3''-O-methyltransferase activity (IEA) → ACCEPT (the exact EC 2.1.1.254 term).
- GO:0008757 SAM-dependent methyltransferase activity (IMP) → ACCEPT (accurate general parent).
- GO:0017000 antibiotic biosynthetic process (IMP) → ACCEPT; add the more specific GO:1901115
  (erythromycin biosynthetic process) in core_functions.
- GO:0032259 methylation (IMP) → ACCEPT (general process for the methyltransferase).

No proposed new term needed (the specific MF term already exists).

## References
- PMID:2185226 — Paulus et al. 1990, *J Bacteriol*: eryG = erythromycin O-methyltransferase. VERIFIED.
