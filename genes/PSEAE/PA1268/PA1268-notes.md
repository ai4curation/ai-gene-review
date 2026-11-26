# PA1268 (LhpA) curation notes

- Deep research: `just deep-research-falcon PSEAE PA1268` failed on 2026-11-11
  (Edison API returned 403 "Failed to authenticate"). No provider file was
  written; this review rests on the cached publications and the UniProt record.
- Q9I476 is the P. aeruginosa 4-hydroxyproline 2-epimerase (PaHyPRE/LhpA).
  Purified recombinant protein epimerizes 4-hydroxyproline and has no proline
  racemase activity [PMID:17849014, "B. pseudomallei and P. aeruginosa
  recombinant proteins presented no measurable PRAC activity but demonstrated
  strong epimerization of OH-L/D-Pro behaving as genuine OH-Pro epimerases."].
- Both catalytic cysteines are required [PMID:17849014, "C88SHyPRE and
  C236SHyPRE single mutations induce radical loss of OH-L/D-Pro epimerization"].
- The paper cloned the gene from strain PAK; UniProt maps it to PAO1 PA1268.
- lhpA lies in an LhpR-controlled, Hyp-inducible locus with the three-subunit
  D-Hyp dehydrogenase LhpBEF [PMID:27145750, "The first locus includes lhpABFE
  encoding a Hyp epimerase (LhpA) and d-Hyp dehydrogenase (LhpBEF)"]. This is
  the convergent alternative to the single-chain P. putida PP_1255 oxidase
  [PMID:22833679, "the L-hydroxyproline pathway clearly evolved convergently in
  P. putida and P. aeruginosa"].
- Naming caution: Li & Lu 2016 call a second epimerase LhpK, while Watanabe
  et al. 2016 (PMID:27929065) name PA1255 LhpL, the bifunctional
  t3LHyp dehydratase/2-epimerase. Locus tags are safer than lhp letters.
- All five GOA rows (GO:0047580) are accepted. GO:0019470 is added as NEW
  (IMP, PMID:27145750) to match the KT2440 ProR review.
- PANTHER PTHR33442:SF1. No IBA rows: the only GO:0047580 IBD node
  (PTN002433936) is seeded by the SF5 protein Q9I489 and does not reach this
  protein in the current GOA.
