# FADS1 notes

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- Two GO:0005739 rows, both synthesis: IEA (GO_REF:0000044, SL-0173) and ISS (GO_REF:0000024, from baboon A4UVI1).
  Both trace back to one study, Park et al. 2012 [PMID:22619218 "FADS1, but not FADS1AT1, localizes to endoplasmic reticulum and mitochondria."].
  UniProt records this for isoform 1 with ECO:0000269 on both the human and baboon entries; the human ER membrane location is by similarity to A4UVI1.
- The earlier review summary had the isoforms backwards (it said isoform 2); corrected: the canonical isoform 1 (FADS1CS) is the one seen in mitochondria.
- Both rows changed ACCEPT -> KEEP_AS_NON_CORE: the organelle claim is recorded, but the desaturase works in the ER membrane and the mitochondrial pool rests on a single imaging study (full text not available via PMC tools).
- No sub-compartment: FADS1 has four predicted TM segments (UniProt TRANSMEM 122-142, 146-170, 268-288, 306-326) but they say nothing about which mitochondrial membrane, and ER-mitochondria contact sites cannot be ruled out. Only one line, so stay at the root (PYCR2 model).
