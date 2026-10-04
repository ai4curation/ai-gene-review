# ALKBH3 (Q96Q83) review notes

## 2026-10-04: PAINT/affinage review

ALKBH3 is a well-characterized AlkB-family dioxygenase that reverses m1A and m3C in single-stranded DNA and RNA.
- **Activity:** [PMID:12486230 "Both enzymes remove 1-methyladenine and 3-methylcytosine from methylated polynucleotides in an alpha-ketoglutarate-dependent reaction, and act by direct damage reversal with the regeneration of the unsubstituted bases."]
- **Partner complex:** it works with the ASCC complex [PMID:22055184 "ASCC3, the largest subunit of ASCC, encodes a 3'-5' DNA helicase, whose activity is crucial for the generation of single-stranded DNA upon which ALKBH3 preferentially functions for dealkylation."]
- **mRNA m1A eraser:** [PMID:26863410 "Moreover, m(1)A in mRNA is reversible by ALKBH3, a known DNA/RNA demethylase."]

Decisions:
- **Accepted:** all MF, DNA-repair, nucleus and cytoplasm rows.
- **Kept as non-core:** proliferation (IMP, cell-type specific) and negative regulation of cytoplasmic translation (inferred from an m1A-translation correlation).
- **ASCC3 interaction row:** MODIFY to GO:0044877 protein-containing complex binding, since ALKBH3 co-purifies with the whole ASCC complex.
- **Nine yeast two-hybrid protein-binding rows** (GLRX3, GOLGA2, IKZF1, LNX1, AK8): REMOVE.
