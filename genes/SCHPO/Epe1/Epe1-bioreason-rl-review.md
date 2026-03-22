# BioReason-Pro RL Review: Epe1 (S. pombe)

Source: Epe1-deep-research-bioreason-rl.md

## Verdict: MAJOR ERRORS — pseudoenzyme misclassified as active enzyme

BioReason-Pro confidently assigns Epe1 as an active Fe(II)/2-oxoglutarate-dependent histone demethylase. This is **wrong**. Epe1 is a well-characterized pseudoenzyme — it has a JmjC domain with degenerate active site residues and no detectable catalytic activity.

## What BioReason got wrong

### 1. Catalytic activity (critical error)
- **BioReason says**: "JmjC catalytic center... dictates a lysine demethylase mechanism that consumes Fe(II) and 2-oxoglutarate"
- **Reality**: The JmjC domain has degenerate active site residues (HVD instead of HXD motif, Tyr307 instead of catalytic His). Mass spectrometry assays with purified Epe1 showed **no detectable demethylase activity** on methylated H3K9 peptides, even with HP1/Swi6 present.
- **Root cause**: BioReason reasons purely from domain architecture (InterPro) and assumes JmjC = catalytic. It has no way to detect degenerate active sites or negative experimental results.

### 2. Molecular function
- **BioReason says**: demethylase-type oxidoreductase (though confusingly maps to GO:0005515)
- **Reality**: Epe1 functions through protein-protein interactions, not catalysis. It binds HP1/Swi6, recruits SAGA HAT complex and Bdf2, promotes nucleosome turnover. The existing review correctly flagged GO:0032452 (histone demethylase activity, IBA) for REMOVE.

### 3. Biological process
- **BioReason says**: chromatin regulation via demethylation
- **Partially right, wrong mechanism**: Epe1 does regulate chromatin, but through anti-silencing (HP1 binding, HAT recruitment, nucleosome turnover) — not through demethylation. It maintains heterochromatin boundaries and prevents ectopic spreading.

## What BioReason got right

### 1. Nuclear localization ✓
Correctly placed in nucleus (GO:0005634). Epe1 is indeed a nuclear protein that acts on chromatin.

### 2. Chromatin regulation (broad level) ✓
The general area — chromatin organization, gene regulation — is correct, just the mechanism is wrong.

### 3. InterPro domain identification ✓
Correctly identified the JmjC domain and JHDM1 family. The domains are real, the inference from them is wrong.

## Lessons for BioReason evaluation

1. **Pseudoenzymes are a blind spot**: BioReason reasons from domain architecture → function. It cannot detect when conserved domains have lost catalytic activity through active site degeneration. This is a known limitation of any InterPro-first approach.
2. **Negative results matter**: The reasoning has no access to experimental evidence showing absence of activity.
3. **IBA had the same problem**: The existing IBA annotation (GO:0032452, histone demethylase activity) made the same error for the same reason — phylogenetic inference from domain conservation.
4. **The functional summary is fluent but wrong**: The text reads convincingly but describes a protein that doesn't exist. This is a hallucination grounded in domain architecture rather than fabricated facts.

## Comparison with curated review

| Aspect | BioReason-Pro | Curated review |
|--------|--------------|----------------|
| Catalytic activity | Active demethylase | Pseudoenzyme, no activity |
| Mechanism | Fe(II)/2-OG oxidation | Protein-protein interactions |
| HP1/Swi6 binding | Not mentioned | Central to function |
| SAGA recruitment | Not mentioned | Key mechanism |
| Nuclear localization | ✓ Correct | ✓ Correct |
| Chromatin role | ✓ Correct (broad) | ✓ Correct (specific) |
