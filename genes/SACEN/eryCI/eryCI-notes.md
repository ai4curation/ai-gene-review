# eryCI (P14290) — review notes

Erythromycin pathway concept (`terms/erythromycin_biosynthesis/`), MIBiG BGC0000055; GenBank
CAM00075.1 → UniProt **P14290** (gene *eryCI* / eryC1).

## Function — desosamine aminotransferase (NOT a "sensory transduction protein")

EryC1 is the **PLP-dependent sugar aminotransferase** of TDP-D-desosamine biosynthesis; it
installs the C-3 amino group on the deoxysugar precursor. It is the **eponymous member of the
DegT/DnrJ/EryC1 family** of sugar aminotransferases (alongside DnrJ for daunosamine).

## Annotation discrepancy (resolved here)

UniProt **P14290 carries a legacy misannotation**: RecName "Erythromycin biosynthesis sensory
transduction protein EryC1", FUNCTION "Sensor protein that transfers the signal of
environmental...", keywords *DNA-binding / Transcription / Two-component regulatory system*, and
subcellular location *Cell membrane (peripheral)*. These date from the 1990 deposition, before
the function was understood. However:
- UniProt's own `SIMILARITY` places it in the **DegT/DnrJ/EryC1 family** (PLP sugar
  aminotransferases), and the **Pyridoxal phosphate** keyword is retained.
- GOA (independently) annotates **transaminase activity** (GO:0008483) + **PLP binding**
  (GO:0030170).

So the catalytic identity (PLP sugar aminotransferase) is correct; the "sensory/transcription/
membrane" layer is the error. This corroborates the discrepancy flagged in the concept doc §6.

## Annotation review

- GO:0008483 transaminase activity (IEA) → ACCEPT (correct; DegT/DnrJ/EryC1 sugar aminotransferase).
- GO:0030170 pyridoxal phosphate binding (IEA) → ACCEPT (PLP cofactor).
- GO:0000271 polysaccharide biosynthetic process (IEA) → MODIFY → GO:1901115 erythromycin
  biosynthetic process (desosamine is a monosaccharide moiety of erythromycin, not a polysaccharide).
- GO:0005886 plasma membrane (IEA, from UniProt "Cell membrane") → REMOVE (knock-on of the legacy
  sensory/two-component misannotation; DegT/DnrJ/EryC1 aminotransferases are soluble cytoplasmic).

## References
- UniProt P14290 — family (DegT/DnrJ/EryC1) and PLP keyword correct; FUNCTION/name outdated.
