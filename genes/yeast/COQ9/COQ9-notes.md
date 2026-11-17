# COQ9 (YLR201C, UniProt Q05779) – review notes

- Identified as a new COQ gene; mutant is Q-deficient [PMID:16027161 "Here, we report a new gene designated COQ9 that is also required for the biosynthesis of this lipoid quinone"]; function was then unclear [PMID:16027161 "Coq9p may either catalyze a reaction in the coenzyme Q biosynthetic pathway or have a regulatory role similar to that proposed for Coq8p"].
- Peripheral matrix-side inner-membrane protein in the ~1 MDa Q complex; co-IPs with Coq4/5/6/7 [PMID:17391640 "Submitochondrial localization studies indicate Coq9p is a peripheral membrane protein on the matrix side of the mitochondrial inner membrane"]; [PMID:17391640 "A direct physical interaction was shown by the immunoprecipitation of HA-tagged Coq9 polypeptide with Coq4p, Coq5p, Coq6p and Coq7p"].
- Required for synthome integrity and for Coq6/Coq7 function and deamination of pABA-derived intermediates [PMID:26008578 "Deletion of COQ9 results in dissociation of the CoQ-synthome"]; [PMID:26008578 "required for the function of Coq6 and Coq7 hydroxylases"].
- Human COQ9 structure: TetR (TFR) fold with lipid-binding site; binds CoQ and intermediates; interacts with COQ7 [PMID:25339443 "Our structure also reveals a lipid-binding site"]; [PMID:30661980 "COQ9 repurposes the bacterial TetR fold to bind aromatic isoprenes with high specificity"]. Yeast lipid binding is inferred (IBA/InterPro), not directly measured.
- GO: lipid binding (GO:0008289) is the core MF; isoprenoid binding (GO:0019840) would be more specific but rests on human data. Complex = GO:0110142 ubiquinone biosynthesis complex (definition lists COQ9). "protein-containing complex" (IDA PMID:25152161) should be refined to GO:0110142.
- COQ9 is absent from the YeastCyc pathways (no reactions in summary file). PomBase GO-CAM types S. pombe coq9 as GO:0098772 molecular function regulator activity regulating coq7.

## Audit to COMPLETE (2026-11-11)

- Deep research: no provider deep-research file is available (no API keys in this session); review rests
  on UniProt Q05779, the SGD description and the cached literature.
- ND literature search for molecular function. Papers checked: PMID:16027161 (cloning; abstract),
  PMID:17391640 (fractionation, BN-PAGE, co-IP; full text), PMID:24406904 (synthome; full text),
  PMID:26008578 (deamination; full text), PMID:25339443 (Lohman 2014; abstract cached, full text
  PMC4226113 read online: yeast work is complementation of coq9 null by 18 Coq9p point mutants and
  DMQ6/CoQ6 ratios, while lipid binding was measured on recombinant human COQ9) and PMID:30661980
  (human COQ9 isoprene binding). No paper in this set reports a molecular activity measured on the S. cerevisiae Coq9 protein, so the MF ND is accepted (nd_case INFERABLE).
- Added NEW GO:0031314 (IDA, PMID:17391640) so the core-function location has an annotation row.
- SGD says human COQ9 complements yeast coq9; PMID:24406904 says this had not been shown as of 2014
  [PMID:24406904 "Human COQ9 has not yet demonstrated interspecific complementation of the yeast coq9 mutants"].
  The SGD claim may reflect later work (not cached); left unverified.
