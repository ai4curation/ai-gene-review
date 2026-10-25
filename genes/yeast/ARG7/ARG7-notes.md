# ARG7 (YMR062C, Q04728; ECM40) notes

- Mitochondrial ornithine acetyltransferase (ArgJ family, EC 2.3.1.35): "ARG7 gene encoding mitochondrial ornithine acetyltransferase, the enzyme catalyzing the fifth step in arginine biosynthesis"; "While forming ornithine, this enzyme regenerates acetylglutamate" [PMID:9428669].
- Modest bifunctionality (acetyl-CoA NAGS, EC 2.3.1.1): "overexpressed ARG7 can complement yeast arg2 and Escherichia coli argA mutations"; "The yeast enzyme is thus clearly, albeit modestly, bifunctional." [PMID:9428669]
- Inhibited by ornithine, insensitive to arginine [PMID:9428669]; deletion is arginine-leaky, implying an alternative route [PMID:9428669 "total deletion of the genomic ARG7 ORF resulted in an arginine-leaky phenotype"].
- Autoproteolytic processing into alpha/beta chains in the matrix [UniProt:Q04728, citing PMID:10753950].
- Mitochondrial matrix [PMID:205532; UniProt:Q04728].

## Curation decisions
- Core MF GO:0004358 (only IEA/RCA in GOA - no experimental row although PMID:9428669 characterises it); BP GO:0006592, GO:0006526; CC GO:0005759.
- GO:0004042 (acetyl-CoA NAGS) rows KEEP_AS_NON_CORE (genuine but minor; Arg2 is the physiological NAGS).
- RCA cytosol and RCA GO:0103045 L-methionine N-acyltransferase: REMOVE.
