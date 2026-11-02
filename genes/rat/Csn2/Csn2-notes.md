# Csn2 (rat beta-casein, P02665) - review notes

- cDNA: 216-aa mature sequence; conserved N-terminal phosphorylation cluster [PMID:6283475 "One such cluster containing the majority of the potential casein phosphorylation sites was located near the amino terminus."]; signal peptide nearly identical to ovine [PMID:6283475 "14 of 15 amino acids in the signal peptide sequence of the precasein were identical between the rat and ovine caseins."]
- Gene: 9 exons; separate exons for signal peptide and hydrophobic C-terminal region [PMID:3997858 "The conserved 5' noncoding region, the highly conserved signal peptide, and the hydrophobic carboxyl-terminal region of the protein are each encoded by a separate exon."]
- Phosphate centre in rat: S29/S31/S32 (SISSEE), by similarity (UniProt).
- Mouse Csn2 KO (Kumar 1994) [PMID:8016126 "Homozygous beta-casein mutant mice are viable and fertile; females can lactate and successfully rear young."]; [PMID:8016126 "Despite the deficiency of beta-casein, casein micelles were assembled in heterozygous and homozygous mutants, albeit with reduced diameters."]; [PMID:8016126 "The growth of pups feeding on the milk of homozygous mutants was reduced relative to those feeding on the milk of wild-type mice."]
- Cysteine protease inhibition: single reverse-zymography study on milk beta-casein [PMID:12788072 "beta-Casein and the active domain, synthesized L(133)-Q(151), peptide inhibited cysteine proteases."] -> MARK_AS_OVER_ANNOTATED for propagated rows (not tested in rat, no in vivo role).
- NEW: calcium ion sequestering activity (GO:0140314, OLS-verified) by sequence similarity, consistent with Csn1s1 review.

## Deep research integration (OpenScientist, 2026-10-24)

All PMIDs cited by the report were fetched into publications/ and the points used were
checked against the abstracts (full text where cached).

- No contradictions with the review. The report's primary function (phosphoserine-cluster
  calcium chelation, micelle building, nutrient delivery, extracellular) matches the core
  functions; peptide activities (beta-casomorphins, CPPs, ACE-inhibitory peptides) are
  treated as digestion products, consistent with the over-annotation of the propagated
  cysteine-protease-inhibitor rows.
- Added to GO:0140314 (NEW): PMID:34717964 (beta-casein monomer flexibility prevents calcium
  phosphate precipitation), PMID:38318529 (beta- and alpha-s-caseins are the mineral
  chaperones) and a quote from the report. Both papers are on bovine/recombinant
  beta-casein; rat-specific data in the report are expression and promoter studies.
- Not used: rat promoter/STAT5 reporter work (PMID:27452799, 1446822, 33930363, 41275902),
  parity marker expression (PMID:16525678), CPP calcium absorption in rats
  (PMID:37874279, 20355020; a property of peptides), ACE-inhibitory peptides (PMID:32448573).
- No action changes.
