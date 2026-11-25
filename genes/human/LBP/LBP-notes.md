# LBP (human, P18428) review notes

## GO-CAM 5fb9cc0600000727

The triacyl lipopeptide TLR1-TLR2 GO-CAM models human LBP as an
extracellular `GO:0140104` molecular carrier activity with the triacylated
lipopeptide as input.

- This agrees with the biochemical reconstitution in PMID:23430250: "either
  LBP or sCD14 can drive ternary complex formation and TLR activation by
  acting as mobile carriers of triacylated lipopeptides or lipoproteins".
- PMID:23430250 also shows that LBP is a ligand carrier rather than a receptor
  subunit: "neither LBP nor sCD14 was physically associated with the final
  ternary complex".
- No conflict with the gene review. The model omits a `part_of` process for
  the LBP carrier step, which is a GO-CAM completeness issue already recorded
  on the model review rather than a disagreement.

## Molecular Function

- LBP is a secreted serum BPI/LBP-family acute-phase protein. UniProt records
  the human protein as secreted, and the original cloning paper described LBP
  as a "trace plasma protein" that binds bacterial LPS.
- LPS binding and delivery are core. PMID:11739189 summarizes the low-dose
  role directly: "an acute-phase protein recognizing lipopolysaccharide
  (LPS), catalyzes in low concentrations its transfer to the cellular LPS
  receptor consisting of CD14 and Toll-like receptor-4".
- The cytokine-effect papers from the early 1990s support the same biochemical
  story. PMID:8409400 shows LBP competing with BPI for LPS and enhancing
  LPS-induced TNF-alpha, IL-6 and IL-8 release; PMID:7517398 shows purified
  recombinant human LBP can replace the serum requirement for LPS binding to
  human monocytes and LPS-induced TNF-alpha secretion.
- LBP also binds Gram-positive ligands. PMID:12594207 verified "formation of
  complexes of LTA with LBP and soluble CD14 as well as catalytic transfer of
  LTA to CD14 by LBP"; PMID:15294986 shows that lipopeptides bind LBP and that
  LBP transfers them to CD14 on human monocytes.
- The `GO:0015026` coreceptor activity row has the right biological direction
  but the wrong molecular-function term. LBP is a soluble mobile carrier for
  lipidated cargo, not a stable signaling coreceptor; the row is therefore
  modified to molecular carrier activity.
- `GO:0005102` signaling receptor binding is generic but supported by
  opsonic receptor contact on macrophages and transient cargo handoff to
  CD14/TLR1-TLR2, so it was kept as non-core.

## Process And Location Rows

- LBP clearly acts in LPS-mediated signaling, in TLR1-TLR2 lipopeptide
  signaling, and in TLR2-dependent LTA signaling. Process rows describing
  macrophage activation, cytokine production, and defense against whole
  bacterial classes were kept as non-core because they are outputs of the
  extracellular binding and transfer reactions.
- The positive and negative TNF-production rows are both biologically
  coherent. Low concentrations of LBP sensitize monocytes to LPS; high
  acute-phase concentrations inhibit LPS transfer and TNF secretion in sepsis
  serum in PMID:11739189.
- `GO:0009986` cell surface was marked over-annotated. PMID:11528597 assayed
  LBP bound to the surface of nontypeable Haemophilus influenzae, not a stable
  human host-cell surface pool.
- `GO:0060265` positive regulation of respiratory burst involved in
  inflammatory response was marked over-annotated. PMID:2477488 explicitly
  showed that LBP-LPS particle binding alone caused neither phagocytosis nor
  initiation of an oxidative burst.
- `GO:0070062` extracellular exosome rows from urinary and EPS-urine
  proteomics were kept as non-core: they are plausible for a secreted abundant
  protein but are not where the LBP carrier reaction is known to occur.

## Deep Research

Falcon deep research was attempted for this review but could not run in the
current environment (`agentapi` was unavailable, and the configured fallback
provider was also unavailable). The review therefore uses the cached GOA-cited
publications, Reactome records, UniProt record, GO-CAM review, and manual notes
rather than a provider-authored `LBP-deep-research-*.md` artifact.

## PR review follow-up

- Oxidized phospholipid binding is modeled in Reactome:R-HSA-8869683; because
  LBP also handles other negatively charged amphiphiles in PMID:8985160, the
  generic `GO:0008289` lipid binding row was kept as non-core rather than
  marked too general.
- The same carrier-participation logic supports NEW `GO:0034142` TLR4
  signaling and NEW `GO:0038123` TLR1:TLR2 signaling rows; LBP catalytically
  delivers the ligand cargo that the receptor complex detects in each model.
