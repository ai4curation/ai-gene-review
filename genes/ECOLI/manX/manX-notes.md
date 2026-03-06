# ManX (EIIAB-Man) - Research Notes

## Summary

ManX (P69797) is the cytoplasmic EIIAB phosphorylating subunit of the mannose-specific PTS in E. coli K12. It is encoded by the manXYZ operon (b1817).

## Key findings

### Domain structure and phosphorylation
- ManX is a bifunctional protein with N-terminal EIIA domain (residues 2-124) and C-terminal EIIB domain (residues 157-320), connected by a flexible hinge [PMID:2681202 "Domain structure and function of the phosphorylating subunit"]
- EIIA domain is phosphorylated by HPr at His-10 (tele-phosphohistidine) [PMID:2681202, PMID:8262947]
- EIIB domain is phosphorylated at His-175 (pros-phosphohistidine) by EIIA [PMID:2681202, PMID:8262947]
- His-86 is involved in phosphoryl transfer between domains [PMID:8262947 "H86N mutation abolishes activity"]

### Dimerization
- ManX forms stable homodimers [PMID:2999119 "IIIMan, a 35-kDa protein, exists as a dimer"]
- H10C mutation abolishes dimerization [PMID:8262947]
- NMR structure of IIAMan-HPr complex (PDB: 1VRC) shows 48 kDa complex [PMID:15788390]

### Localization
- Dual localization: found both membrane-associated and free in cytoplasm [PMID:2999119]
- Peripheral membrane protein associated with inner membrane [PMID:16079137]

### Substrate specificity
- Primary substrates: mannose, glucose (2-deoxyglucose)
- Secondary substrates: fructose [PMID:4153999, PMID:4154035], N-acetylglucosamine [PMID:6252281]

### Regulation
- manXYZ operon positively regulated by cAMP-CRP complex [PMID:9484892]
- Negatively regulated by Mlc transcriptional repressor [PMID:9484892]
- Weakly repressed by NagC [PMID:11361067]

### Additional functions
- ManXYZ complex serves as chemoreceptor for sugar chemotaxis [PMID:4604906]
- ManXYZ required for phage lambda DNA injection, but ManY/ManZ alone sufficient [PMID:353494, PMID:2951378]

## Review decisions
- Removed GO:0005515 (protein binding) - uninformative per curation guidelines
- Marked GO:0016301 (kinase activity) as over-annotated - too broad for PTS phosphotransferase
- Core MF: GO:0022870 (mannose PTS transporter activity)
- Secondary substrates (fructose, GlcNAc, glucose) kept as non-core
