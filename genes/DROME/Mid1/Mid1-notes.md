# Mid1 (CG33988, Nlf-1) review notes

UniProt Q9I7V0; NALF/FAM155 family (PTHR15819), homolog of yeast Mid1 and mammalian NALF1/2.

## Literature journal

- Predicted and validated as an NA-associated protein by homology to yeast Mid1
  [PMID:24639627 "the Mid1 homolog in Drosophila, encoded by the CG33988 gene, is coordinately expressed with NALCN, and that knockdown of either protein creates identical phenotypes in several behaviors associated with NALCN function"].
- Circadian locomotion: [PMID:24639627 "RNAi knockdown of CG33988 using the same pan-neural driver results in an identical circadian aberration (Figure 3)."]
- Social clustering: [PMID:24639627 "neurally induced RNAi knockdown of na and CG33988 similarly and significantly suppressed the social clustering"].
- CG33988 = Nlf-1 (NCA localization factor 1); clock-controlled regulator of NA current in DN1p neurons
  [PMID:26276633 "This current is driven by the rhythmic expression of NCA localization factor-1, linking the molecular clock to ion channel function."]
  [PMID:26276633 "Moreover, RNAi knockdown of Nlf-1 results in suppression of behavioral rhythms, NA expression and related current."]
  [PMID:26276633 "Conversely, NLF-1 overexpression increases NA current, firing frequency and membrane potential in the evening"].
- Worm NLF-1 is ER-resident [PMID:26276633 "NLF-1 protein is expressed in the endoplasmic reticulum and is required for the proper axonal localization of NCA-1 and −2"]; fly localization unknown.
- Developmental expression suffices for adult rhythms [PMID:28634443 "developmental expression of endogenous channel subunits and Nlf-1 is sufficient to promote robust rhythmic behavior in adults"].

## Curation decisions

- IBA channel regulator activity ACCEPTED as core MF (fly gain/loss of NA current).
- Complex term -> sodium channel complex (consistent with na, unc79, unc80).
- IBA cation import -> sodium ion transmembrane transport (consistent with na).

## Deep research

`Mid1-deep-research-falcon.md` (falcon) arrived after the review was first committed. It agrees with the review: fly Mid1/CG33988 is a NALF/FAM155-like NALCN auxiliary factor rather than a pore or enzyme. It stresses that fly localization is unresolved: nematode NLF-1 is ER-localized, while mammalian FAM155A has also been detected at the cell surface and sits on the extracellular side of NALCN in channelosome structures. This supports the plasma-membrane IBA caveat and the localization question in the review. It also notes that CG33988 RNAi did not measurably reduce CG33988 mRNA in Ghezzi et al. 2014. No annotation decision changed.
