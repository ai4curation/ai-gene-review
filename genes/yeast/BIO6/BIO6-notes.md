# BIO6 (E9P8E0; non-S288C, SGD S000029723) notes

- Named for 52% identity to BIO3 [PMID:16269718 "This ORF was named BIO6 because it has 52% identity with BIO3"]
- bio6 rescued by KAPA, bio3 not [PMID:16269718 "The BIO6 disruptant was able to grow in biotin-deficient medium supplemented with 7-keto-8-amino-pelargonic acid (KAPA), while the bio3 disruptant was not able to grow in this medium"]
- Acts before KAPA [PMID:16269718 "These results suggest that Bio6p acts in an unknown step of biotin synthesis before KAPA synthesis"]
- Called KAPA synthase in later work [PMID:32276977 "yeast KAPA synthase (Bio6)"] - assumption, no enzyme assay.
- Class-III PLP aminotransferase family, BioA PANTHER PTHR42684:SF17 [UniProt:E9P8E0]
- ISS with/from Q89AK6 = Buchnera BioF (class II, PTHR13693) per UniProt REST lookup: not same family.

## Decisions
- BioA activity (GO:0004015) IEA removed (paralog neofunctionalization; BIO3 does that step).
- KAPA synthase ISS UNDECIDED. Core: biotin biosynthetic process, no MF.
- YeastPathways comment assigns KAPA synthase to BIO6, but 7KAPSYN-RXN has no gene in the BioPAX export.
