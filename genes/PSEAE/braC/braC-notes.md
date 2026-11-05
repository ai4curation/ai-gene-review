# braC (PA1074, P21175) review notes

Periplasmic LIVAT-binding protein of the LIV-I ABC transporter BraCDEFG
(leucine-binding protein family; Pfam Peripla_BP_6; PANTHER PTHR47151).
Reviewed UniProt entry. First gene of the braC-braD-braE-braF-braG operon.

## Literature (no deep-research provider available; own reading)

- Hoshino and Kose 1989 (abstract only). braC cloned; signal peptide of 26
  residues cleaved; protein purified from shock fluid; the braC plasmid restores
  LIV-I transport in the braC310 mutant [PMID:2509433 "The plasmid carrying the
  LIVAT-BP gene restored the activity of the high-affinity branched-chain amino
  acid transport system"]. 51% identical to E. coli LivJ/LivK.
- Johnson et al. 2008 (full text read). Biolog/plate phenotypes of the PA1074
  Tn5 mutant: D-Ala C+/-, L-Ala C-, L-Ile C+/-, L-Val N- [PMID:18833300 "In this
  work, mutants for each of these genes were found to be defective in Alanine
  metabolism, while utilization of L-Valine and L-Isoleucine was also altered in
  some cases"]. braC is the first gene of the operon, so the insertion may be
  polar on braDEFG.
- Fernandez et al. 2019 (full text). ITC of purified BraC: nanomolar binding of
  the five LIVAT ligands, none of D-Ala or L-Met [PMID:31627455 "ITC experiments
  revealed binding with nanomolar affinities for the five ligands identified in
  the study by Hoshino et al. [58] (Figure 6A), whereas no binding was detected
  for l-Met and d-Ala."]; also binds L-homoserine.

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002524712 | GO:0015829 valine transport | 2 | 17 (9 taxa) | GO:1903805 L-valine import across plasma membrane, IMP, PMID:18833300 (PseudoCAP) | SOUND | Full text: mutant cannot use L-valine as N source; agrees with direct nanomolar valine binding (PMID:31627455) and LIV-I complementation (PMID:2509433). Node term suits the LivJ/LivK/BraC clade. | E. coli LivJ P0AD96 (EcoCyc IMP, acts_upstream_of_or_within, PMID:323236) | Yes, on LivJ (weakly; IMP upstream-qualified), and BraC's own binding data make the term sound for the clade |
| PTN002524712 | GO:0015818 isoleucine transport | 2 | 17 (9 taxa) | GO:1903806 L-isoleucine import across plasma membrane, IMP, PMID:18833300 (PseudoCAP) | SOUND | Partial growth defect on L-Ile; agrees with direct binding. | E. coli LivJ P0AD96 (EcoCyc IMP PMID:323236) | Yes |

No PSEUDOCAP defect on the seed rows and no GO_CENTRAL defect. braG
(reviewed in parallel) sits on a different node (PTN000657089), so braC
shares no node with it.

### Other PseudoCAP rows (not seeds)

| term | verdict | defect |
|---|---|---|
| GO:0042941 D-alanine transmembrane transport (IMP, PMID:18833300) | WRONG | PSEUDOCAP WRONG_TERM, PROBABLE: purified BraC does not bind D-alanine (ITC, PMID:31627455); the weak growth phenotype of a possibly polar insertion does not show BraC-mediated D-Ala transport. This differs from the braG review, which left its D-alanine row UNDECIDED without the ITC paper; the BraC binding data bear on the whole LIV-I system. |
| GO:0015808 L-alanine transport (IMP) | SOUND | none; MODIFY to GO:1904273 (as on braG) |
| GO:0015803 branched-chain amino acid transport (IDA, PMID:2509433) | SOUND | none; TOO_GENERAL (entailed by GO:1903805/GO:1903806). The abstract describes genetic complementation, so IMP would fit better than IDA, but not recorded as a defect. |
