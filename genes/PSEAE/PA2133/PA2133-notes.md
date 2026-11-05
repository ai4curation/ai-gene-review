# PA2133 (Q9I1Y2) review notes

## Summary of the literature

PA2133 is a 285-aa protein consisting essentially of one EAL domain (UniProt
domain 23-273) with no predicted TM segment. Its catalytic motif reads ETL rather
than EAL.

- Kulesekara et al. 2006 (PMID:16477007; full text read on PMC, PMC1413825; cached
  copy abstract-only; verbatim excerpts in rocR-notes.md). Lysates of a
  PA2133-overexpressing strain degraded 71% of added c-di-GMP ("PA2133 ETL — +(71)");
  Fig. 3B shows the HPLC traces for PA2133. Overexpression also reduced TTSS
  cytotoxicity.
- Hickman et al. 2005 (PMID:16186483; full text cached). PA2133 was chosen as a
  predicted EAL PDE and expressed from a plasmid to test whether c-di-GMP drives the
  wspF phenotype: "wspF mutant cells carrying the PA2133 expression vector had
  undetectable levels of c-diGMP". Expression in wild-type PAO1 blocked attachment
  and biofilm. The loss-of-function mutant had no phenotype: "A PA2133 mutant
  resembled the wild type in attachment assays."
- Andersen et al. 2021 (PMID:33495218; full text cached). Induction of chromosomal
  PBAD-PA2133 disperses biofilms; the authors call PA2133 a characterised bona fide
  c-di-GMP PDE and find it more active than BifA.

So the PDE activity is well supported (lysate assay plus near-complete in vivo
c-di-GMP depletion), but every biofilm result uses PA2133 as an overexpressed tool
to drain c-di-GMP. Nothing shows a physiological role for native PA2133 in biofilm
regulation.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002105365 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 18 | 162 (24 taxa) | GO:0071111, IDA, PMID:16477007 (PseudoCAP) | SOUND | Lysates of the overexpressing strain degraded 71% of added c-di-GMP (full text read). In vivo expression makes c-di-GMP undetectable (PMID:16186483). | E. coli PdeA/B/C/F/H/I/K/L/N, DosP; Mtb P9WM13; P. aeruginosa bifA, rocR, PA2200, nbdA, PA2567, PA3825 | Yes. Node-level defects are recorded once in rocR-ai-review.yaml. |
| PTN009140332 | GO:1900190 regulation of single-species biofilm formation | 4 | 84 (9 taxa) | GO:1900191 negative regulation of single-species biofilm formation, IMP, PMID:16186483 (PseudoCAP) | INDIRECT-PHENOTYPE | The paper expresses PA2133 from a plasmid as a tool to deplete c-di-GMP; the PA2133 mutant resembles wild type. The biofilm loss reflects artificial c-di-GMP depletion, not a demonstrated role of native PA2133 (full text read). | bifA (Q9HW35; SOUND, deletion + complementation), E. coli PdeF (P77172), arr (Q9I025) | Yes. It stands on bifA (see bifA notes), so no GO_CENTRAL defect. Only a PSEUDOCAP defect on this row. |

## Annotation decisions

- GO:0071111 IBA and IDA: ACCEPT.
- GO:0005886 IBA: MARK_AS_OVER_ANNOTATED. No TM segment; the node-level PM defect
  is recorded in the rocR review.
- GO:1900190 IBA: KEEP_AS_NON_CORE. Inherited from a sound node; plausible for a
  c-di-GMP PDE, but PA2133 has no loss-of-function biofilm phenotype.
- GO:1900191 IMP (PMID:16186483): MARK_AS_OVER_ANNOTATED, with a PSEUDOCAP source
  defect (overexpression-as-tool phenotype).
