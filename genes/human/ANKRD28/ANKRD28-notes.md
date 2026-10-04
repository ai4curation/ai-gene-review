# ANKRD28 notes

- PP6 ankyrin-repeat scaffolding subunit (ARS-A). PP6 is a heterotrimer: PPP6C plus a SAPS subunit (PPP6R1/2/3) plus ARS (ANKRD28/44/52). PPP6R1 bridges the two other subunits [PMID:18186651 "PP6R1 acts as a scaffold with separate regions for binding to PP6 and to Ankrd28"].
- Functions: knockdown enhances TNF-induced IkBe degradation [PMID:18186651]; needed for PP6 in mitosis, with ANKRD44 [PMID:21187329]; knockdown raises pMOB1-T35 and shrinks focal adhesions [PMID:35512830, full text]. RAB40C-CUL5 ubiquitylates ANKRD28 for lysosomal degradation [PMID:35512830].
- PP1 targeting (as "PITK") [PMID:16564677, PMID:17023142; abstracts]. Nuclear foci, versus "exclusively in the cytoplasm" in PMID:17988990. Nucleoplasm kept as non-core.
- GO:0051894 positive regulation of FA assembly (IMP): the knockdown data support the positive sign, but the paper also states "ANKRD28-containing PP6 complex inhibits FA formation". Kept as non-core, with the conflict raised as a suggested question.
- 27 GO:0005515 rows:
  - DOCK1 → MODIFY to GO:0017124 SH3 domain binding.
  - PP6 subunits (PPP6C, PPP6R1/2/3; 16 rows) → REMOVE. They are co-members of one complex, already captured by GO:0008287/GO:0019888, and ANKRD28 reaches PPP6C through the PPP6R1 scaffold.
  - TNKS2 and nine HuRI screen partners → REMOVE.
- No IBA rows. The PANTHER xref places ANKRD28 in PTHR24173:SF74, whose name is "ANKYRIN REPEAT DOMAIN-CONTAINING PROTEIN 16"; I have not checked that placement.
- Affinage: trust gate tripped (pairwise tie); the narrative checks out against the abstracts.
