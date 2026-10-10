# NSUN3 review notes

## Deep research

Automated deep research could not be generated: `just deep-research-falcon` failed
(Edison API 402 Payment Required; perplexity-lite fallback unavailable) and
`just deep-research-openai` failed with 401. The review uses the cached literature and
UniProt record directly.

## Literature used

- Nakano et al. 2016 [PMID:27214402 "We demonstrate that biogenesis of f(5)C34 is initiated by S-adenosylmethionine (AdoMet)-dependent methylation catalyzed by NSUN3"] (abstract only).
- Van Haute et al. 2016 [PMID:27356879 "We show that NSun3 is required for deposition of m(5)C at the anticodon loop in the mitochondrially encoded transfer RNA methionine (mt-tRNA(Met))"]; matrix localization by protease protection [PMID:27356879 "Both NSun3 and mtSSB1 were resistant to proteinase K treatment of the mitochondrial fraction"].
- Haag et al. 2016 [PMID:27497299 "NSUN3 specifically recognises the anticodon stem loop (ASL) of the tRNA"]; ALKBH1 oxidises m5C34 to f5C34.

## Curation decisions

- `regulation of mitochondrial translation` (IMP x2) modified to `mitochondrial tRNA
  methylation` (GO:0070901): NSUN3 installs a constitutive modification required for
  translation; it is not a regulator.
- HSPD1 `protein binding` rows (two proteome-scale AP-MS maps) removed as uninformative.

## Disease context (dismech)

dismech `Combined_Oxidative_Phosphorylation_Deficiency_48` used only as a literature lead.
