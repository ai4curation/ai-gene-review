# ADO1 (YJR105W, UniProt P47143) notes

## Function
- Adenosine kinase EC 2.7.1.20 "Reaction=adenosine + ATP = AMP + ADP + H(+)" [UniProt:P47143]; PfkB family.
- "Adenosine (Km 3 microM) is its primary substrate." (recombinant) [PMID:14558146]
- ado1 deletion "affected utilization of S-adenosyl methionine (AdoMet) as a purine source and resulted in a severe reduction of adenosine kinase activity in crude extracts" [PMID:11223943]
- "We also show that ADO1 does not play a major role in adenine utilization in yeast and we propose that the physiological role of adenosine kinase in S. cerevisiae could primarily be to recycle adenosine produced by the methyl cycle." [PMID:11223943]
- Cytoplasm and nucleus (HDA) [PMID:14562095].

## Pathway
- ADENOSINE-KINASE-RXN in PWY3O-1/2220/285; correct. Default cytosol fine.
- Physiologically linked to the methyl (AdoMet) cycle (adenosine from SAH hydrolase Sah1).

## Decisions
- Core MF GO:0004001; BP GO:0044209 AMP salvage, GO:0006166 purine ribonucleoside salvage; cytosol.
- KEEP_AS_NON_CORE purine nucleobase metabolic process (IBA/IMP; substrate is a nucleoside), nucleus, ARBA general terms; MARK_AS_OVER_ANNOTATED carbohydrate derivative biosynthetic process; MODIFY kinase activity -> GO:0004001.
