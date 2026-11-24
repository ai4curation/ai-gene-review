# smoC (Atu3279, A9CEY7) notes

## Deep research
- 2026-11-10: `just deep-research AGRFC <gene> --provider perplexity` fails in this environment
  (no provider credentials; unsatisfiable deep-research-client dependency, "All providers failed",
  tried on smoA). Review built from UniProt and cached literature.

## Literature (PMID:35074914, full text)
- SmoC annotated as alkanesulfonate monooxygenase but only 30% identical to E. coli SsuD
  [PMID:35074914 "SmoC is annotated as an alkanesulfonate monooxygenase, though it possesses only 30% sequence identity with the well-characterized alkanesulfonate monooxygenase SsuD, from E. coli."]
- Coupled sulfite-release assay with SmoA/FMN/NADH; SQ-specific, inactive on SQGro and HEPES
  [PMID:35074914 "No activity was observed when SQ was replaced with other sulfonates, including SQGro (the precursor to SQ) or HEPES (an unrelated sulfonate) demonstrating that, unlike the promiscuous SsuD, SmoC has high specificity for SQ"]
- ITC: SQ binds without flavin (Kd 3 uM), SQGro does not.
- Homodimer (SEC-MALS); 3.4 A structure 7OLF; RoSmoC 1.9 A structure; conserved sulfonate site
  Trp206/Arg236/His238/Tyr341/His343 (RoSmoC numbering).
- A. tumefaciens does not grow on DHPS, SL, pentanesulfonate, MES, HEPES, etc.

## Decisions
- GO:0008726 (TreeGrafter, PTN000768559): ACCEPT; SQ C6 is an alkyl sulfonate and the reaction
  fits the GO definition literally. Proposed NTR "sulfoquinovose monooxygenase activity"
  (RHEA:70775, EC 1.14.14.181) as child.
- GO:0016705 -> MODIFY to GO:0008726.
- GO:0046306 alkanesulfonate catabolic process -> MODIFY to GO:1902777 (lateral).
- PANTHER PTHR42847:SF4 (same subfamily as SsuD and RutA).
