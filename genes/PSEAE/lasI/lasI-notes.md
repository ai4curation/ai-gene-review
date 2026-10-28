# lasI (PA1432, P33883) notes

No deep-research provider was available; this is a manual literature review
(PubMed MCP / E-utilities, cached abstracts). All cached papers below are
abstract-only.

## Identity

- UniProt P33883 (Swiss-Prot), LASI_PSEAE, 201 aa, acyl-homoserine-lactone
  synthase, EC 2.3.1.184. Pfam PF00765 Autoind_synth; InterPro IPR001690;
  PANTHER PTHR39322. Crystal structure 1RO5.
- Reaction (UniProt CC CATALYTIC ACTIVITY, Rhea:10096): a fatty acyl-[ACP] +
  S-adenosyl-L-methionine = an N-acyl-L-homoserine lactone +
  S-methyl-5'-thioadenosine + holo-[ACP] + H+.

## Literature

- Passador et al. 1993 (PMID:8493556, PseudoCAP seed paper): lasI is needed for
  high-level elastase (lasB) expression in gene-fusion experiments and is
  "involved in the synthesis of a diffusible molecule termed Pseudomonas
  autoinducer (PAI)" [PMID:8493556 "Experiments with gene fusions show that gene
  lasl is essential for high expression of elastase. The lasl gene is involved in
  the synthesis of a diffusible molecule termed Pseudomonas autoinducer (PAI)."].
  The evidence is genetic (mutant/fusion phenotype), not a direct assay; the
  abstract foregrounds production of a signal, not transduction of one.
- Pearson et al. 1994 (PMID:8278364): PAI purified from P. aeruginosa or from
  E. coli carrying lasI is 3-oxo-C12-HSL [PMID:8278364 "Chemical analyses
  indicated the purified material was
  3-oxo-N-(tetrahydro-2-oxo-3-furanyl)dodecanamide."].
- Hoang et al. 2002 (PMID:12480888): an in vitro fatty acid / 3-oxo-AHL
  synthesis system with purified Fab proteins, ACP and LasI produced almost
  exclusively 3-oxo-C12-HSL; "the LasI 3-oxo-AHL synthase is sufficient for
  their synthesis" [PMID:12480888 "An in vitro fatty acid-3-oxo-AHL synthesis
  system was established utilizing purified P. aeruginosa Fab proteins, ACP and
  the LasI 3-oxo-AHL synthase."]. This is direct biochemical evidence for
  GO:0061579 on the purified protein.
- Gould et al. 2004 (PMID:15306017): crystal structure; LasI "produces
  3-oxo-C12-AHL from the substrates 3-oxo-C12-acyl-carrier protein (acyl-ACP)
  and S-adenosyl-L-methionine"; an acyl-chain tunnel and an acyl-ACP binding
  surface (Arg154, Lys150) supported by in vivo reporter assays.

## GO term reasoning

- GO:0007165 signal transduction is defined to begin "with reception of a
  signal" and, "For signaling between cells, signal transduction is restricted
  to events at and within the receiving cell." LasI makes the ligand; LasR is
  the receptor/transducer. LasI does no step of signal transduction, so the term
  is wrong for LasI under CLAUDE.md's participation test (the entity that
  performs the transduction steps is LasR, not LasI).
- GO:0009372 quorum sensing: "The cell-cell signaling process in which
  single-celled organisms ... [produce] small, diffusible, signal molecules,
  detecting the concentration of these molecules, and triggering a signal
  transduction pathway". Producing the signal is an explicit part of this
  process, and LasI catalyses that step. Parents: cell-cell signaling
  (GO:0007267, which covers "release of a ligand").
- Comparator check (QuickGO, 2026-10-28): other autoinducer synthases do carry
  quorum sensing with experimental evidence: the AinS-family AHL synthase G3FB25 (ainS, IDA,
  PMID:10482519, CACAO) and LuxS (P45578 EcoCyc IMP; A1AEN2 CACAO IMP). RhlI
  (P54291) and LuxI (P12747) carry only the IBA/TreeGrafter signal
  transduction propagated from the same family, i.e. the same error, not an
  independent convention. So quorum sensing is the term GO uses for signal
  synthases.
- No "N-acyl homoserine lactone biosynthetic process" term exists in GO (OAK
  search of go.db). Not proposing a new term; the MF term GO:0061579 captures
  the biosynthesis.
- MF: GO:0061579 N-acyl homoserine lactone synthase activity is the right,
  specific term. Currently only IEA (EC/Rhea); an IDA to
  PMID:12480888 should be added upstream (recommended in the IEA row reason).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002217335 | GO:0007165 signal transduction | 1 (sole seed) | 5 (3 taxa; QuickGO lists lasI, rhlI, Yersinia yspI and ypeI, Bradyrhizobium bjaI) | GO:0007165 signal transduction, IDA, PMID:8493556 (PseudoCAP) | WRONG | LasI synthesises the diffusible autoinducer 3-oxo-C12-HSL; GO restricts signal transduction to events at and within the receiving cell, beginning with signal reception (LasR). The paper is a gene-fusion/mutant study (lasI needed for lasB expression and PAI synthesis), so IDA is also the wrong code. The correct process for a signal synthase is GO:0009372 quorum sensing (comparators AinS IDA, LuxS IMP). The IBD should be re-termed to quorum sensing; that term suits every LuxI-family AHL synthase leaf of the node. The node's MF, GO:0061579, is already on all leaves by EC/Rhea IEA. |

## Decisions summary

- signal transduction IBA and IDA: MODIFY to GO:0009372 quorum sensing
  (lateral correction; the gene makes the signal, it does not transduce it).
  PSEUDOCAP WRONG_TERM (PROBABLE) on the IDA row and GO_CENTRAL WRONG_TERM
  (PROBABLE) on the IBD at PTN002217335.
- transferase activity IEA: MODIFY to GO:0061579.
- N-acyl homoserine lactone synthase activity IEA: ACCEPT.
- GO:0061579 has only IEA in GOA; an IDA to PMID:12480888 (purified LasI in a
  reconstituted system) is recommended in the IEA row reason (a NEW row is not
  allowed for a term already in GOA).
