# CYP71B15 (PAD3, At3g26830; UniProt Q9LW27) - curation notes

## 2026-10-02 initial review

Sources: UniProt Q9LW27, GOA tsv (32 rows), deep research (falcon), cached publications.
PMID:33831160 (cited by GOA for two IPI rows plus ER and ER-lumen IDA rows) could not be
fetched: NCBI esummary returns "cannot get document summary" and Europe PMC has no record
for it. Its content could not be checked. The interactors it names (AT2G29460 = GSTU4,
Q9ZW27; AT2G30750 = CYP71A12, O49340) match the 2019 metabolon paper.

### Identity and enzymology
- Cytochrome P450 CYP71B15, encoded by the PAD3 locus. Single N-terminal helical anchor
  (UniProt TRANSMEM 1..21), no other membrane spans. pad3-2 = G176E.
- Map-based cloning: [PMID:10590168 "The predicted PAD3 protein appears to be a cytochrome P450 monooxygenase, similar to those from maize"].
- Final step: [PMID:16766671 "Recombinant CYP71B15 heterologously expressed in yeast catalyzed the conversion of dihydrocamalexic acid to camalexin with preference of the (S)-enantiomer."];
  in planta microsomes: [PMID:16766671 "Arabidopsis microsomes isolated from leaves of CYP71B15-overexpressing and induced wild-type plants were capable of the same reaction but not microsomes from induced leaves of pad3 mutants"].
  The reaction is an oxidative decarboxylation [PMID:16766671 "CYP71B15 catalyzes an oxidative decarboxylation of both enantiomers of dihydrocamalexic acid"].
- Earlier step: [PMID:19567706 "Surprisingly, yeast-expressed CYP71B15 also catalyzed thiazoline ring closure, DHCA formation, and cyanide release with Cys(IAN) as substrate."]
  So PAD3 is bifunctional: Cys(IAN) -> (R)-DHCA + HCN (RHEA:10452), then DHCA -> camalexin + CO2 (RHEA:34807); EC 1.14.19.52.
- GO has a term only for the second reaction: GO:0010298 dihydrocamalexic acid decarboxylase activity.
  It sits under carboxy-lyase activity (GO:0016831), and its definition leaves out O2 and the
  reductase, even though Rhea and UniProt describe an O2/NADPH-P450-reductase-dependent oxidative
  decarboxylation. That is a question about where GO places the term, so it is raised as a question
  rather than changed here. There is no GO term for the Cys(IAN) -> DHCA thiazoline-forming reaction,
  so a new term is proposed ("dihydrocamalexate synthase activity").
- EC 1.14.19.x covers reactions where the pair of donors is oxidized and O2 is reduced to water.
  The net reactions incorporate no oxygen atom, so "monooxygenase activity" (GO:0004497) is a
  family-level label that is not strictly accurate. GO:0016705 (paired donors, incorporation OR
  reduction of O2) fits better.

### Localization and metabolon
- [PMID:31511315 "we used two independent untargeted coimmunoprecipitation (co-IP) approaches with the biosynthetic enzymes CYP71B15 and CYP71A13 as baits and determined that the camalexin biosynthetic P450 enzymes copurified with these enzymes."]
- [PMID:31511315 "FRET-FLIM and co-IP demonstrated that the glutathione transferase GSTU4, which is coexpressed with Trp- and camalexin-specific enzymes, is physically recruited to the complex."]
- Deep research (from the Mucha 2019 full text): a native-promoter CYP71B15-GFP that complements pad3 sits in the ER of
  cells adjoining infection sites. No PAD3 homodimer was detected.
- An ER-lumen localization does not fit the topology of a type-I microsomal P450 (N-terminal anchor, catalytic domain on
  the cytosolic face). I could not read the source (PMID:33831160), so that row is UNDECIDED rather than REMOVE.

### Biological role
- pad3 mutants lack camalexin [PMID:8090752 "A biochemical screen was used to isolate three mutants of A. thaliana ecotype Columbia that were phytoalexin deficient (pad mutants)."].
- Fungal susceptibility: [PMID:10476063 "We now show that this mutant is markedly more susceptible than its wild-type parental line to infection by the necrotrophic fungus Alternaria brassicicola, but not to Botrytis cinerea."];
  Botrytis lesion development depends partly on PAD3 [PMID:12848825 "camalexin limits lesion development"]. Whether pad3 is susceptible to Botrytis depends on the isolate.
- Not required for resistance to P. syringae [PMID:10590168 "has no effect on resistance to P. syringae but compromises resistance to the fungal pathogen Alternaria brassicicola"].
- Since PAD3 is the last enzyme, pad3 phenotypes come specifically from the lack of camalexin [PMID:16766671 "it is now clear that the enhanced susceptibilities of pad3 are the specific results of camalexin deficiency"].

### Necessity vs participation (project curation question 3)
PAD3 is unusual among infection-phenotype genes: its mechanism is known. It catalyses the last two
steps that make the antifungal compound. The core annotations are therefore the MF (DHCA decarboxylase,
plus the proposed DHCA synthase) and camalexin biosynthetic process. "Defense response to fungus" is
accepted as the physiological role, because the gene product makes the defensive effector molecule.
"Defense response" and "response to bacterium" are kept as non-core. IEP rows (drought, ABA, SAR
regulation) are marked over-annotated: a transcript change does not show the gene takes part in the
process, and IEP cannot support a "regulation of" term.

## 2026-10-03: PMID:33831160 resolved

PubMed's redirection notice (supplied by the reviewer) says PMID:33831160 was
deleted as a duplicate of PMID:31511315 (Mucha et al. 2019, "The Formation of a
Camalexin Biosynthetic Metabolon", Plant Cell). E-utilities only returns
"cannot get document summary" for the old PMID, so the mapping was not visible
before. Recorded as `reference_review.replacement` (DUPLICATE_RECORD) on the
old reference; the GOA `original_reference_id` is unchanged.

Effect on the four rows citing it:
- protein binding with GSTU4 (IPI): UNDECIDED to REMOVE. Supported by the paper
  [PMID:31511315 "FRET-FLIM and co-IP demonstrated that the glutathione
  transferase GSTU4 ... is physically recruited to the complex"], but protein
  binding is uninformative and GSTU4 is not a camalexin enzyme.
- protein binding with CYP71A12 (IPI): UNDECIDED to REMOVE, same as the direct
  PMID:31511315 row.
- endoplasmic reticulum (IDA): still ACCEPT.
- endoplasmic reticulum lumen (IDA): still UNDECIDED. Full text is not
  retrievable (PMC6881122 returns abstract only), and the luminal location
  conflicts with the cytosol-facing P450 topology.
