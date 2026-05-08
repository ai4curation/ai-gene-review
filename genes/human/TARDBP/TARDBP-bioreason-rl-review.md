# BioReason-Pro RL Review: TARDBP (human)

Source: TARDBP-deep-research-bioreason-rl.md

- **Correctness**: 4/5
- **Completeness**: 3/5

## Functional Summary Review

The BioReason functional summary states:

> A soluble nucleic-acid-binding protein that assembles into higher-order ribonucleoprotein complexes to regulate RNA fate. Its N-terminal oligomerization module and a central RNA-recognition core cooperate with a stabilizing C-terminus to bind and chaperone structured RNAs, thereby coordinating post-transcriptional events such as processing, transport, stability, and translation. The assemblies it forms operate in both nucleus and cytoplasm and likely couple RNA recognition to ribosome-associated functions.

This captures the core features of TDP-43 (TARDBP) reasonably well. The curated review describes it as "a highly conserved, dosage-sensitive RNA-binding protein essential for RNA metabolism" with RRM domains that bind UG-rich RNA and TG-rich DNA. BioReason correctly identifies:

1. RNA binding (GO:0003723) via RRM domains
2. N-terminal oligomerization domain
3. Nuclear and cytoplasmic distribution
4. Roles in RNA processing, transport, stability
5. Higher-order RNP complex formation

However, there are notable gaps and inaccuracies:

1. **DNA binding omitted**: TDP-43 was originally identified as a TAR DNA-binding protein. The curated review includes DNA binding (GO:0003677) as a function. While RNA binding is the dominant function, the DNA-binding capacity is part of the gene's identity.

2. **Splicing function underemphasized**: TDP-43's role as a splicing regulator is its best-characterized nuclear function, including regulation of cryptic exon inclusion (particularly the STMN2 cryptic exon in neurodegeneration). BioReason mentions "processing" generically but does not highlight splicing.

3. **The C-terminal low-complexity domain** (prion-like domain) and its role in liquid-liquid phase separation and pathological aggregation are not mentioned. This is a defining feature of TDP-43 biology.

4. **Translation role**: BioReason claims involvement in "translation" and "ribosome-associated functions," which is speculative. TDP-43's role in translation is less well-established compared to its splicing and mRNA stability functions.

Comparison with interpro2go:

The interpro2go annotations from IPR000504 (RRM domain) would map to RNA binding and nucleic acid binding. BioReason recapitulates this and adds the N-terminal and C-terminal TDP-43-specific domain context. The predicted GO terms include mRNA binding (GO:0003729) and mRNA 3'-UTR binding (GO:0003730), which are accurate and present in the curated review. BioReason modestly extends beyond interpro2go by incorporating TDP-43-specific domain architecture.

## Notes on thinking trace

The trace correctly identifies the N-terminal domain (IPR041105), RRM domain, and C-terminal domain (IPR049124). The description of the C-terminus as a "stabilizing" module underrepresents its role as a disordered, aggregation-prone region. The mechanistic hypothesis about ribosomal interactions is speculative.
