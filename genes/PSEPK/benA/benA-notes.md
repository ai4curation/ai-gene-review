# BenA (PP_3161) - Benzoate 1,2-dioxygenase alpha subunit

## Gene Identity
- **UniProt**: Q88I40 (unreviewed TrEMBL entry)
- **Gene**: benA (PP_3161)
- **Organism**: Pseudomonas putida KT2440
- **EC**: 1.14.12.10 (benzoate 1,2-dioxygenase)
- **PANTHER**: PTHR43756:SF1 (3-phenylpropionate/cinnamic acid dioxygenase alpha subunit)

## Summary

BenA is the alpha (large) subunit of benzoate 1,2-dioxygenase, the first enzyme in the chromosomal
benzoate degradation pathway of P. putida KT2440. The complete dioxygenase system consists of:
- **BenA** (alpha subunit) - contains Rieske [2Fe-2S] cluster and mononuclear iron active site
- **BenB** (beta subunit) - structural role
- **BenC** (reductase) - electron transfer from NADH via FAD and [2Fe-2S] to the terminal oxygenase

The enzyme catalyzes: benzoate + NADH + O2 → cis-1,2-dihydroxycyclohexa-3,5-diene-1-carboxylate (benzoate cis-diol) + NAD+

This is the first committed step in the beta-ketoadipate (ortho-cleavage) pathway for benzoate degradation.

## Operon Structure

The ben operon in P. putida KT2440 consists of benABCD plus a second copy of catA (catA2/PP_3166)
located downstream [PMID:12534466 "the genes encoding the peripheral pathways for the catabolism of
benzoate (ben) were mapped in the chromosome of P. putida KT2440"; PMID:24341396 "P. putida mt-2
has a second chromosomal copy of the catA gene (named catA2) located downstream of the ben operon"].

The operon is regulated by BenR, an AraC/XylS family transcriptional activator that requires
benzoate as an allosteric effector (see BenR review in this project).

## Pathway Context

BenA functions in the beta-ketoadipate pathway:
1. **Benzoate → benzoate cis-diol** (BenABC - benzoate 1,2-dioxygenase) ← BenA is here
2. Benzoate cis-diol → catechol (BenD - cis-diol dehydrogenase)
3. Catechol → cis,cis-muconate (CatA/CatA2 - catechol 1,2-dioxygenase)
4. cis,cis-muconate → muconolactone → beta-ketoadipate → TCA cycle intermediates

[PMID:12534466 "four main pathways for the catabolism of central aromatic intermediates, that is,
the protocatechuate (pca genes) and catechol (cat genes) branches of the beta-ketoadipate pathway,
the homogentisate pathway (hmg/fah/mai genes) and the phenylacetate pathway (pha genes)"]

## Protein Structure

BenA is a Rieske-type aromatic ring-hydroxylating dioxygenase alpha subunit:
- **Rieske [2Fe-2S] domain** (residues 47-129, PROSITE PS51296) - electron transfer
- **Catalytic domain** with Ring_hydroxyl_A fold - contains mononuclear non-heme iron active site
- The Rieske domain transfers electrons to the mononuclear iron center where O2 activation occurs
- 452 amino acids, 51.5 kDa

Homologs include XylX from the TOL plasmid pWW0 (58.3% identity to Acinetobacter BenA)
[PMID:1938949 "comparison of aligned XylX-BenA amino acid sequences revealed respective identities of 58.3%"]

## Biotechnological Relevance

The ben operon has been extensively studied for production of cis,cis-muconate from benzoate
[PMID:21906639 "The specific production rate achieved is at least eight times higher than those
reported for other cis, cis-muconate-producing strains"; PMID:21954182 "18.5 g/L cis,cis-muconate
accumulated in the culture medium with a molar product yield of close to 100%"]

## Key References

- PMID:12534463 - Nelson et al. 2002 - Complete genome sequence of P. putida KT2440
- PMID:12534466 - Jimenez et al. 2002 - Genomic analysis of aromatic catabolic pathways in KT2440
- PMID:24341396 - Jimenez et al. 2014 - CatA2 as metabolic safety valve in ben operon context
- PMID:1938949 - Harayama et al. 1991 - Evolutionary divergence of benABC and xylXYZ
- PMID:21906639 - van Duuren et al. 2011 - catR mutant and ben operon expression
- PMID:21954182 - van Duuren et al. 2012 - pH-stat fed-batch for muconate production
