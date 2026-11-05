# bifA (PA4367, Q9HW35) review notes

## Summary of the literature

BifA is a 687-aa inner-membrane protein with one TM segment (159-179 in UniProt),
a degenerate GGDEF domain (GGDQF) and an EAL domain.

- Kuchma et al. 2007 (PMID:17586641; full text cached) named the gene for its
  hyperbiofilm phenotype: "Deletion of the PA4367 gene results in a severe defect
  in swarming motility and a hyperbiofilm phenotype". BifA is enriched in the
  inner-membrane fraction ("BifA localizes to the inner membrane."). Purified
  His-BifA hydrolysed bis-pNPP and extracts degraded c-di-GMP; the paper concludes
  that "purified BifA protein exhibits phosphodiesterase activity in vitro but no
  detectable diguanylate cyclase activity". EAL-to-AAL and GGDQF-to-AAAAA mutants
  were stable but did not complement: "In contrast, expression of either
  His-BifA-AAAAA or His-BifA-AAL fails to suppress the hyperbiofilm phenotype of
  the Δ bifA mutant." The hyperbiofilm needs Pel polysaccharide.
- The inactive GGDEF domain binds GTP, which regulates the EAL domain and
  Pel-dependent biofilm through an interaction with PelD [PMID:38197635 "Here we
  demonstrate that the inactive GGDEF domain of BifA binds GTP and regulates the
  adjacent phosphodiesterase EAL domain"].
- HecE inhibits BifA to raise c-di-GMP in a subpopulation [PMID:37291227 "HecE
  inhibits the phosphodiesterase BifA and stimulates the diguanylate cyclase WspR"].
- Inducing native BifA disperses biofilms [PMID:33495218].
- Kulesekara et al. 2006 (PMID:16477007; full text read on PMC, see
  rocR-notes.md): lysates of a BifA-overexpressing strain showed no detectable
  PDE activity in that assay ("PA4367 GGDQF EAL — —"); the authors note that
  activity was not detected for any DGC-PDE hybrid in this assay. This does not
  contradict the later purified-protein work.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002105365 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 18 | 162 (24 taxa) | GO:0071111, IMP, PMID:17586641 (PseudoCAP) | SOUND | Purified BifA has PDE activity, and EAL-motif mutation abolishes it and complementation (full text read). The evidence is really IDA plus IMP; the claim is right. | E. coli PdeA/B/C/F/H/I/K/L/N, DosP; Mtb P9WM13; P. aeruginosa rocR, PA2133, PA2200, nbdA, PA2567, PA3825 | Yes. Node-level defects (degenerate EAL leaves; PM term) are recorded once in rocR-ai-review.yaml. |
| PTN009140332 | GO:1900190 regulation of single-species biofilm formation | 4 | 84 (9 taxa) | GO:1900191 negative regulation of single-species biofilm formation, IMP, PMID:17586641 (PseudoCAP) | SOUND | Clean deletion gives a complementable hyperbiofilm; catalytic mutants fail to complement, so the effect runs through BifA's own PDE activity. Regulation of biofilm via c-di-GMP is the accepted role of such PDEs. | PA2133 (Q9I1Y2; overexpression only, INDIRECT-PHENOTYPE, see PA2133 notes), E. coli PdeF (P77172), arr (Q9I025) | Yes. bifA is the strongest seed. Without PA2133 the IBD still rests on bifA plus PdeF and arr. No GO_CENTRAL defect. |

## Annotation decisions

- GO:0071111 (IBA, IEA, IMP): ACCEPT; core function.
- GO:0005886 IBA: ACCEPT; one TM segment and inner-membrane fractionation.
- GO:1900191 IMP: ACCEPT.
- GO:1900190 IBA: MODIFY to GO:1900191, which the gene carries by IMP.
- GO:0044010 single-species biofilm formation IMP: MODIFY to GO:1900191. BifA
  restrains biofilm formation; it is a regulator, not a participant.
