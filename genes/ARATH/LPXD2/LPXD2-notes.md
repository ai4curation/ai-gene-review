# LPXD2 (At4g21220, F4JIP6) notes

Deep research could not be run (provider authentication fails in this
environment), so this summary was compiled manually from the cached full text of
Li et al. 2011 (PMID:21709257, PMC3136250), the UniProt record and PubMed
searches. No `-deep-research-*.md` file was produced.

## Identity

- Swiss-Prot F4JIP6, "Probable UDP-3-O-acylglucosamine N-acyltransferase 2,
  mitochondrial" (AtLpxD2), 304 aa, predicted mitochondrial transit peptide 1-47.
  LpxD subfamily of the transferase hexapeptide repeat family; InterPro IPR007691;
  NCBIfam TIGR01853 lipid_A_lpxD; PANTHER PTHR43378:SF2.
- Paralog of LPXD1 (about 75% identical in our alignment; the paper says "more than
  60%") [PMID:21709257 "these proteins share 41 and 34% identity with E. coli LpxD ( Table 1 ), with conservation of key catalytic residues"].
- Keeps the acyl-ACP-binding arginine:
  [PMID:21709257 "R293 is conserved between E. coli LpxD and AtLpxD2, but is replaced by lysine in AtLpxD1."]
  Our alignment (`../LPXD1/LPXD1-bioinformatics/RESULTS.md`) maps E. coli H239 to
  LPXD2 H216 and R293 to LPXD2 R270.

## Mutant chemistry: LPXD2 is the main LpxD

- atlpxd2-1 (ET116191, CSHL gene trap, Landsberg erecta) is a homozygous null,
  compared with its Ler parent.
- [PMID:21709257 "lipid X was undetectable in the atlpxd2-1 mutant compared with its parental plant"]
  [PMID:21709257 "indicating that AtLpxD2 is the predominant UDP-3- O -acyl-GlcN N -acyltransferase"]
- [PMID:21709257 "Introducing the atlpxd2-1 mutation into the atlpxb-1 mutant background significantly lowered lipid X levels"]
- [PMID:21709257 "the genes encoding AtLpxA, AtLpxC, and AtLpxD2 are required for the efficient production of lipid X"]
- [PMID:21709257 "These results suggest that AtLpxD2 is the primary UDP-3- O -acyl-GlcN N -acyltransferase in Arabidopsis"]
- No visible phenotype:
  [PMID:21709257 "Null mutants of AtLpxA , AtLpxD2 , AtLpxB , AtLpxK , and AtKdtA , as well as AtLpxC-RNAi knock-down plants, show no obvious phenotypic differences compared to wild type under laboratory conditions"]
- Caveat: a single allele in a different accession from the other mutants; no
  complementation reported.

## Localisation

- [PMID:21709257 "However, 5′-terminal fusions of AtLpxD1, AtLpxD2, AtLpxB, and AtLpxK to GFP showed the same mitochondrial pattern as full-length AtLpxA and AtLpxC"]
- Lipid X enriched in mitochondria:
  [PMID:21709257 "Lipid X levels in mitochondria were 3- and 48-fold higher than in chloroplasts or whole cell homogenates, respectively."]
- Not chloroplast:
  [PMID:21709257 "In mesophyll cells, GFP signals were shown as 1 μm dots, but were not colocalized with chloroplasts"].

## Other literature

- PubMed search "(LpxD OR lipid A OR lipid X) AND Arabidopsis" (2026-10-26):
  no further LpxD work. No in vitro assay or E. coli complementation of LPXD2
  has been published.
- Wei et al. 2020 (PMID:32470107) flagged the lipid A annotation; refuted for
  LPXD2 by the mutant chemistry above.

## Paralog comparison

LPXD2 carries essentially all lipid X synthesis in seedlings; LPXD1 has no
detectable contribution, carries substitutions at substrate-binding residues and
may have a different acceptor. The two are therefore not redundant in the assay
conditions tested, and the reviews treat them differently: LpxD activity and lipid
A biosynthesis are accepted for LPXD2 and left undecided for LPXD1.

## Review decisions (summary)

- LpxD activity GO:0103118 (IBA, IEA, IMP): ACCEPT, core. GO:0016747 MODIFY to
  GO:0103118.
- Lipid A biosynthetic process (IEA): ACCEPT, core, with the experimental
  evidence recorded on the row (a NEW row is not possible because the term is
  already in GOA). Obsolete lipid X metabolic process (IBA, IMP): MODIFY to
  lipid A biosynthetic process.
- Mitochondrion ACCEPT; cytoplasm MODIFY to mitochondrion; chloroplast REMOVE.
