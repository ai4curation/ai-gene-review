# pqsH (PA2587, Q9I0Q0) review notes

No deep-research API was available, so these notes come from manual literature
research (cached publications plus a PubMed search on "PqsH Pseudomonas aeruginosa
monooxygenase", 2026-10-28).

## Biology

- PqsH is the terminal enzyme of PQS biosynthesis. It hydroxylates HHQ at C3 to
  give PQS, using NADH and O2 [PMID:20662781 "we show that PqsH catalyses the
  terminal step in PQS production, synthesizing PQS in vitro using the substrates
  2-heptyl-4-quinolone (HHQ), NADH and oxygen"].
- Purified MBP-PqsH was characterised biochemically. Kinetics confirm HHQ, NADH
  and O2 as substrates. NADPH also works, with about 20-fold lower kcat/Km
  [PMID:20662781 "Steady state kinetic analysis confirmed HHQ, NADH, and oxygen as
  substrates of MBP-PqsH, consistent with its predicted role as an HHQ hydroxylating
  monooxygenase"]. Turnover is about 2.5 min-1.
- The enzyme is a flavin monooxygenase by family membership [PMID:20662781 "PqsH is a
  member of a family of flavin-dependent monooxygenases that utilize NAD(P)H and
  oxygen to catalyze hydroxylation of aromatic substrates"]. The paper did not
  measure FAD content directly. UniProt places it in the 3-hydroxybenzoate
  6-hydroxylase family, and it has Pfam PF01494 FAD_binding_3.
- Substrate range: C7 and C9 HHQ are processed with similar kcat/Km. C5 and C3
  analogues are poorer substrates because their Km is higher [PMID:20662781].
- Oxygen is the limiting substrate in vivo. Anaerobic P. aeruginosa makes no PQS
  and has defects in PQS-controlled behaviours such as membrane vesicle
  formation. These behaviours recover as soon as O2 returns, without new protein
  synthesis [PMID:20662781].
- Genetics: pqsH is required for PQS synthesis, and its transcription depends on
  LasR [PMID:12426334 "Since pqsH is required for PQS synthesis, this finding
  accounts for a previous observation that PQS production requires LasR
  function"]. It was originally predicted as a "putative FAD-dependent
  monooxygenase" [PMID:12426334].
- Comparative work: PqsH and the catabolic ortholog AqdB (Mycobacteroides
  abscessus) catalyse the same 3-hydroxylation [PMID:33452035 "Hydroxylation of the
  PQS precursor 2-heptylquinolin-4(1H)-one (HHQ) by the signal synthase PqsH boosts
  AQ quorum sensing. Remarkably, the same reaction, catalyzed by the ortholog
  AqdB"]. AQ 3-monooxygenases do not discriminate AQs from AQNOs, so PqsH
  may also make PQS-N-oxide (abstract only; full text not cached).
- Localization: no TM segments, but the protein associates with membrane
  fractions when overexpressed [PMID:20662781]. Not strong enough to add a
  cellular-component term.

## GO term check (OLS / go-basic.obo)

- GO:0102164 2-heptyl-3-hydroxy-4(1H)-quinolone synthase activity is_a GO:0016709
  (NAD(P)H-dependent, one O incorporated), which is_a GO:0004497 monooxygenase
  activity. GO:0102164 is therefore the exact, more specific term for the IDA in
  PMID:20662781.
- GO has no "quinolone signal biosynthetic process" term (searched OLS and
  go-basic.obo), so GO:0044550 secondary metabolite biosynthetic process is the
  most specific available BP.
- GO:0009372 quorum sensing: the definition includes "producing small, diffusible,
  signal molecules", so a signal synthase arguably does part of quorum sensing.
  Comparator check: pqsB and pqsC (same pathway, same role) carry only GO:0044550,
  not quorum sensing. I did not add a NEW row; raised as a question instead.

## PseudoCAP IBA-seed assessment

Tree analysis: `pqsH-bioinformatics/RESULTS.md`. PTN008173107 is the root of the
PTHR45934 tree. Its children are an Emericella leaf and a horizontal-transfer
node, and under that node sit PqsH, Streptomyces SCO1338 and a 294-leaf
Viridiplantae clade (Arabidopsis MO1/MO2/MO3, CTF2A/B, ...).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN008173107 | GO:0004497 monooxygenase activity | 1 (sole seed) | 297 (43 taxa) | GO:0004497 monooxygenase activity, IDA, PMID:20662781 (PseudoCAP) | SOUND | The seed is direct evidence: a purified enzyme hydroxylates HHQ with NADH and O2, which meets the monooxygenase definition. The seed is under-specific (the paper supports GO:0102164), but the IBD needs only the generic term. The IBD sits at the family root of class A FAD aromatic hydroxylases (FAD_binding_3/MOase), and generic monooxygenase activity is the right level there. The PqsH-specific GO:0102164 would be wrong on this node, since 294/297 leaves are plant proteins. Caveat: every plant IBA rests on a single bacterial seed on a horizontally transferred branch. No plant member contributed experimental support, and plant catalytic-residue conservation was not checked. |

Recommended actions: PseudoCAP could refine the IDA to GO:0102164. This would
not break the IBD, because GO:0102164 is_a GO:0004497 and a descendant term is
valid IBD evidence. I filed no GO_CENTRAL defect: the node term is generic and
plausible. The caveat is listed under suggested_questions.
