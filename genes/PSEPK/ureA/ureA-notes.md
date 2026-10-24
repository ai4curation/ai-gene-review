# ureA curation notes

## 2026-08-11

- Q88J06 is reviewed UniProt UreA/PP_2843, the 100-aa gamma chain of the
  cytoplasmic UreABC heterotrimer [`ureA-uniprot.txt`, "Urease subunit gamma"].
- The historical Asta-backed review at commit `86cf4fd8e9` was inspected but
  not reused wholesale. In particular, its acceptance of nickel binding and
  individual `enables urease activity` overstates this structural chain.
- The orthologous apoenzyme is an `(alpha beta gamma)3` assembly, with the
  binickel center specifically in the alpha/UreC subunit
  [PMID:8718850, "each alpha-subunit having an (alpha beta)8-barrel domain
  containing a binickel active center"]. UreA is therefore modeled as
  contributing to complex-level urease activity, not independently enabling it.
- No direct KT2440 UreA experiment was found in the cached primary literature;
  the exact locus assignment rests on current reviewed UniProt, conserved
  family architecture, and a complete adjacent `ureDABCEFG` system.
