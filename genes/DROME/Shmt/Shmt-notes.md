# Shmt (CG3011, Q9W457) notes

## 2026-10-09 review session

- Deep research (falcon, with perplexity-lite fallback) timed out / failed; no deep-research file.
- Winkler et al. 2017 (full text cached):
  - catalytic requirement: [PMID:28515048 "A transgene with this allele did not complement SHMT[X238], indicating that the enzymatic function is required."]
  - isoforms: [PMID:28515048 "a longer one of 470 amino acid residues with a putative N-terminal mitochondrial presequence, and a shorter one of 400 amino acid residues"]
  - localization: [PMID:28515048 "SHMT is present in mitochondria and the cytoplasm."];
    nuclear pool [PMID:28515048 "Staining of such extracted cells revealed a nucleoplasmic staining for SHMT together with the lamina protein LaminDm0 (Figure 3D)."]
  - tetramer: [PMID:28515048 "These data indicate that SHMT largely constitutes a tetramer in Drosophila."]
- Frenkel et al. 2017 (abstract only): glycine synthesis in LNv clock neurons needed for normal period
  [PMID:28380364 "impairment of glycine synthesis in LNv neurons increased period length"].

## Decisions
- Core: GO:0004372 in cytoplasm, mitochondrion, nucleus; glycine biosynthesis, serine catabolism, folate cycle.
- regulation of circadian rhythm (IMP): KEEP_AS_NON_CORE (glycine-supply consequence).
- hydroxytrimethyllysine aldolase (ISS from SHMT1) and carnitine biosynthesis (IC): KEEP_AS_NON_CORE;
  in vitro side activity of mammalian SHMT, untested in insects.

## Update: deep research arrived
- `Shmt-deep-research-falcon.md` (written after the wrapper timed out) agrees with the review.
- Caveat: mitochondrial localization in flies is inferred from the presequence, not shown directly
  [Shmt-deep-research-falcon.md "Mitochondrial localization is inferred from transcript structure and the predicted import sequence, not directly demonstrated by organelle colocalization."].
  The IBA/ISS mitochondrial rows are still accepted as sound inferences.
- Later work (per deep research; not cached): dTTP depletion by cycle 13 in Shmt embryos, and SHMT loss
  promoting genome instability in a Ras tumor model.
