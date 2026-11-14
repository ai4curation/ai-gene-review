# nbdA (PA3311, Q9HYT3) review notes

## Summary of the literature

NbdA ("NO-induced biofilm dispersion locus A") is a 783-aa inner-membrane protein
with an N-terminal MHYT domain (seven predicted TM helices), a degenerate GGDEF
domain (AGDEF) and an EAL domain.

- Li et al. 2013 (PMID:23729646; cached abstract only, full text not read; the PMC
  page could not be retrieved). nbdA inactivation impairs NO-induced but not
  glutamate-induced dispersion [PMID:23729646 "inactivation of nbdA only impaired
  biofilm dispersion upon exposure to NO"]. NO raises PDE activity and lowers
  c-di-GMP in nbdA-expressing biofilms, but not in the deletion strain
  [PMID:23729646 "increased PDE activity, resulting in decreased c-di-GMP levels in
  biofilms expressing nbdA upon exposure to NO, a response that was absent in the
  ΔnbdA strain"]. This is mainly through transcriptional induction by NO. A
  recombinant protein lacking the MHYT domain is an active PDE [PMID:23729646
  "Biochemical analyses of recombinant protein variants lacking the
  membrane-anchored MHYT domain support NbdA being an active PDE"]. UniProt adds
  that the protein has no DGC activity and is stimulated by GTP.
- NbdA, together with DipA and RbdA, inhibits flagellar motor switching through
  MapZ [PMID:31350333 "three of them (DipA, NbdA, and RbdA) can significantly
  inhibit flagellar motor switching and swimming directional reversal in a
  MapZ-dependent manner"].
- Kulesekara et al. 2006 (PMID:16477007; full text read on PMC, see rocR-notes.md):
  a PA3311 insertion formed a pellicle (hyperbiofilm), and the lysate PDE assay gave
  no detectable activity for PA3311 ("PA3311 AGDEF EAL — —"). The authors note that
  activity was not detected for any GGDEF-EAL hybrid in that assay. This does not
  contradict the later purified-protein result.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002105365 | GO:0071111 cyclic-guanylate-specific phosphodiesterase activity | 18 | 162 (24 taxa) | GO:0071111, IDA, PMID:23729646 (PseudoCAP) | SOUND | The abstract states outright that recombinant NbdA lacking the MHYT domain is an active PDE, and UniProt curators cite the same paper for EC 3.1.4.52. Full text not read; the decisive fact is stated in the abstract. | E. coli PdeA/B/C/F/H/I/K/L/N, DosP; Mtb P9WM13; P. aeruginosa bifA, rocR, PA2133, PA2200, PA2567, PA3825 | Yes. Node-level defects are recorded once in rocR-ai-review.yaml. |

nbdA is not a seed of PTN009140332 but inherits GO:1900190; NbdA's own data (NO-induced
dispersion) fit that regulation term.

## Annotation decisions

- GO:0071111 (IBA, IEA, IDA): ACCEPT; core function.
- GO:0005886 (IBA, IEA): ACCEPT; MHYT domain with seven TM helices.
- GO:1900190 IBA: ACCEPT; regulates biofilm dispersal in response to NO. GO has no
  biofilm-dispersal term.
- GO:0071732 cellular response to nitric oxide (IMP, IEA): ACCEPT. nbdA is induced
  by NO and required for the NO dispersal response.
