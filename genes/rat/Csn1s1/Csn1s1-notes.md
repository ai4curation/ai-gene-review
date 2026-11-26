# Csn1s1 (rat alpha-casein, P02661) - review notes

## Identity
- Rat "alpha-casein" is the ortholog of ruminant alpha-s1-casein; 284 aa precursor, 15-aa signal peptide [PMID:6298707 "The 1402-nucleotide alpha- and 864-nucleotide gamma-casein mRNAs both encode 15 amino acid signal peptides and mature proteins of 269 and 164 residues, respectively."]
- Rat-specific insertion of 10 x 18-nt repeats [PMID:6298707 "A unique feature of the rat alpha-casein sequence is an insertion in the coding region containing 10 repeated elements of 18 nucleotides each."]
- Homology to bovine alpha-s1 casein [PMID:6298707 "Significant homology was also detected between rat alpha- and bovine alpha s1-casein."]
- Gene structure: separate exons encode 5' UTR, signal peptide and casein-kinase phosphorylation sequence [PMID:3952000 "the 5' noncoding, signal peptide and casein kinase phosphorylation sequences are each encoded by separate exons"]
- UniProt: phosphoserine cluster 93-99 (by similarity) = phosphate centre; Secreted; mammary specific.

## Function (family picture)
- Calcium-sensitive casein; phosphate centres sequester amorphous calcium phosphate nanoclusters, allowing milk to be supersaturated in Ca-phosphate without calcification [PMID:23958008 "most of which form thermodynamically stable complexes with nanoclusters of amorphous calcium phosphate"]; [PMID:25632319 "Phosphopeptides that contain three or more phosphorylated residues (usually seryl) in a short sequence are said to have a phosphate centre (PC)."]
- Mouse Csn1s1 knockout (Kolb 2011): [PMID:21789179 "Absence of α-casein protein significantly curtails secretion of other milk proteins and calcium-phosphate, suggesting a role for α-casein in the establishment of casein micelles."]; [PMID:21789179 "In mouse milk, 3 of the phosphate centres are in present α-casein and only one in β-casein."]; pup growth delayed.
- No rat-specific functional experiments found; rat annotations are all propagated (IBA/ISO/IEA) plus one TAS.

## Annotation judgements
- Hormone-response IBAs (estradiol, progesterone, DHEA, deoxycorticosterone) trace to a bovine explant study where supraphysiological steroids inhibited casein synthesis [PMID:3585228 "A similar inhibitory effect was also found using high levels of other steroids without 11 beta-hydroxyl, such as deoxycorticosterone and dehydroepiandrosterone, and to some extent with oestradiol-17 beta"]: casein is a transcriptional readout, not a participant -> REMOVE.
- molecular sequestering activity -> MODIFY to calcium ion sequestering activity (GO:0140314, OLS-verified, is_a GO:0140313).

## Deep research integration (OpenScientist, 2026-10-24)

All PMIDs cited by the report were fetched into publications/ and the points used were
checked against the abstracts (full text where cached).

- No contradictions with the review. The report's primary (calcium phosphate
  sequestration) and secondary (ER export organizer, chaperone) functions match the core
  functions and the ISO lactation row.
- Added to GO:0007595 lactation (ISO): PMID:25549363, a rat mammary-cell study showing the
  membrane-associated form of alpha-s1-casein in ER cholesterol-rich microdomains and its
  central place in micelle building and transport, and PMID:10504344 (goat null: ER export
  of the other caseins depends on alpha-s1-casein). This gives rat-specific grounding to
  the participation claim.
- Added to GO:0140313 (MODIFY -> GO:0140314): PMID:8126102 (casein phosphorylation is needed
  for Ca2+ binding and micelle formation; mouse acini, not rat as the report's context
  could suggest) and a quote from the report.
- Not used: JAK/STAT/SOCS and hypothyroidism expression studies (PMID:26472537), casein
  kinase activity changes (PMID:6273140, 2833669), FAM20C, Golgi calcium for late
  phosphorylation (PMID:8713076). An ER/Golgi location for rat alpha-s1-casein was not
  proposed; PMID:25549363 could support one but casein transit locations are not
  annotated elsewhere in the rat reviews.
- No action changes.
- Note: the earlier bullet above saying the hormone-response IBAs go to REMOVE is out of date; the review marks them MARK_AS_OVER_ANNOTATED, the family convention.
