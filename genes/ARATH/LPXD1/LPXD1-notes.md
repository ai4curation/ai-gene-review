# LPXD1 (At4g05210, F4JGP6) notes

Deep research could not be run (provider authentication fails in this
environment), so this summary was compiled manually from the cached full text of
Li et al. 2011 (PMID:21709257, PMC3136250), the UniProt record and PubMed
searches. No `-deep-research-*.md` file was produced.

## Identity

- Swiss-Prot F4JGP6, "Probable UDP-3-O-acylglucosamine N-acyltransferase 1,
  mitochondrial" (AtLpxD1), 330 aa, predicted mitochondrial transit peptide 1-52
  (ECO:0000255). LpxD subfamily of the transferase hexapeptide repeat family;
  InterPro IPR007691 (LpxD); PANTHER PTHR43378:SF2.
- One of two Arabidopsis LpxD paralogs on chromosome 4
  [PMID:21709257 "Two AtLpxD orthologs (designated AtLxpD1 and AtLpxD2) were encoded on chromosome 4"],
  [PMID:21709257 "these proteins share 41 and 34% identity with E. coli LpxD ( Table 1 ), with conservation of key catalytic residues"].

## Sequence divergence from LpxD

- [PMID:21709257 "R293 is conserved between E. coli LpxD and AtLpxD2, but is replaced by lysine in AtLpxD1."]
- [PMID:21709257 "AtLpxD1 also lacks two aromatic residues in its N-terminal domain that are required for acceptor substrate binding"]
- Own check (`LPXD1-bioinformatics/RESULTS.md`, global alignment against E. coli
  P21645): catalytic H239 is conserved in both paralogs (LPXD1 H217, LPXD2 H216);
  R293 maps to LPXD1 K271 and LPXD2 R270, confirming the R293K substitution on the
  current gene model. LPXD1 and LPXD2 are about 75% identical. Both current gene
  models align comparably over the E. coli N-terminal region, so the paper's
  statement that only AtLpxD2 has the N-terminal nucleotide-binding domain may
  reflect the 2011 gene models.

## Mutant chemistry: no lipid X phenotype

- atlpxd1-1 (CS855902, Wisconsin DsLox, Col-0) is a homozygous null.
- [PMID:21709257 "The lipid X level in the atlpxd1-1 mutant was not reduced from that of wild type"]
- [PMID:21709257 "Introducing the atlpxd1-1 mutation into the atlpxb-1 mutant background did not lower its elevated lipid X levels"]
- In contrast, LPXD2 loss abolishes lipid X; residual lipid X in atlpxd2 atlpxb:
  [PMID:21709257 "The presence of some residual lipid X in this setting leaves open the possibility that AtLpxD1 generates a small portion of the lipid X pool."]
- Alternative role suggested by the authors:
  [PMID:21709257 "At present, we cannot exclude the intriguing possibility that AtLpxD1 has LpxA activity"]
  (atlpxa mutants keep about 21% of lipid X).
- The UniProt disruption-phenotype line ("plants lacking LPXD1 accumulate very low
  levels of 2,3-diacylglucosamine-1-phosphate") does not match the paper text,
  which says lipid X is not reduced.
- No visible phenotype:
  [PMID:21709257 "All null mutants and RNAi knock-down lines were viable and showed no obvious phenotypic differences compared to wild-type plants."]

## Localisation

- [PMID:21709257 "However, 5′-terminal fusions of AtLpxD1, AtLpxD2, AtLpxB, and AtLpxK to GFP showed the same mitochondrial pattern as full-length AtLpxA and AtLpxC"]
  (full-length fusions too dim to image). Not chloroplast:
  [PMID:21709257 "In mesophyll cells, GFP signals were shown as 1 μm dots, but were not colocalized with chloroplasts"].

## Other literature

- PubMed search "(LpxD OR lipid A OR lipid X) AND Arabidopsis" (2026-10-26)
  returned no further work on either LpxD paralog; other hits concern LPS
  perception by plants (LORE) and are not about the plant pathway enzymes.
- Wei et al. 2020 (PMID:32470107) flagged plant lipid A biosynthetic process
  annotations including LPXD1 as misannotations (see projects/RAR_MISANNOTATION.md).
  The pathway exists in Arabidopsis, but for LPXD1 specifically the involvement is
  unresolved.

## Review decisions (summary)

- Mitochondrion: ACCEPT (IDA, IBA, IEA); cytoplasm MODIFY to mitochondrion;
  chloroplast (ISM) REMOVE.
- LpxD activity GO:0103118 (IBA, IEA, IMP): UNDECIDED. The IMP is not supported by
  the paper's data for LPXD1 (no lipid X change), and residue divergence plus the
  LpxA hypothesis leave the specific activity open.
- Acyltransferase activity GO:0016747: ACCEPT as the most specific supported MF;
  transferase activity TOO_GENERAL.
- Lipid A biosynthetic process (IEA): UNDECIDED. Obsolete lipid X metabolic
  process: IBA UNDECIDED, IMP REMOVE (no phenotype).
- No NEW annotations: no experimental evidence supports a term absent from GOA.
