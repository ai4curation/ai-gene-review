# rimO (P0AEI4) notes

Deep research was unavailable for this gene (falcon returned 403; asta returned nothing useful in
Phase 1 of the RADICAL_SAM project). The review was built from cached primary papers, the UniProt
record and QuickGO term lookups.

## Function

- yliG/rimO is required for beta-methylthiolation of uS12 Asp88: [PMID:18252828 "Using mass
  spectrometry, we have identified the enzyme responsible for this modification in E. coli, the yliG
  gene product."]. Predicted unique among MTTase subgroups in modifying protein [PMID:18252828 "we
  predict that RimO is unique among these subgroups in its modification of protein as opposed to
  tRNA"].
- In vitro: [PMID:19736993 "RimO(rcn) catalyzes the attachment of a methylthio group to a peptide
  substrate analogue that mimics the loop structure bearing aspartyl 88 of the S12 ribosomal protein
  from E. coli."]; two [4Fe-4S] clusters after reconstitution; SAM cleaved to 5'-dA
  [PMID:19736993 "Results from the HPLC-based kinetic assays imply that the reductive cleavage of SAM
  by RimOrcn to generate 5′-dA takes place in the presence of the substrate analog P1."]. SAH formed
  only substoichiometrically, so the methyl source was not proven in that paper; the RHEA reaction
  (RHEA:37087) uses 2 SAM by analogy with MiaB.
- In vivo context: [PMID:21169565 "the proteomic data from this study provides direct evidence that
  the E. coli specific β-methylthiolation likely occurs when S12 is assembled as part of a ribosomal
  subunit."]; YcaO needed for efficient modification.
- Family mechanism and T. maritima RimO structure with SAM: PMID:23542644.

## Term decisions

- Protein methylthiolation MF: GO:0103039 protein methylthiotransferase activity (QuickGO: defined as
  the RHEA:37087 uS12 Asp89 reaction; is_a GO:0140096 catalytic activity, acting on a protein, and
  GO:0035596). GO:0035599 aspartic acid methylthiotransferase activity (peptidyl-Asp beta-carbon) is a
  sibling under GO:0035596, not a parent. Both ACCEPTed; core MF = GO:0103039 (RHEA-defined, parallel
  to GO:0035597 for MiaB). Ontology question raised in suggested_questions.
- BP: GO:0018339 (peptidyl-L-beta-methylthioaspartic acid biosynthesis) and GO:0018197
  (peptidyl-aspartic acid modification) are OBSOLETE in QuickGO ("specific pathway variant, out of
  scope"). No BP asserted for RimO.
- GO:0006400 tRNA modification (IEA, InterPro IPR005839 family-wide mapping) REMOVED: RimO modifies
  protein, not tRNA [PMID:19736993 "To date, it is the only enzyme known to catalyze methylthiolation
  of a protein substrate"].
- GO:0003824 -> GO:0103039; GO:0016740 and GO:0035596 -> GO:0103039 + GO:0035599; GO:0051536 ->
  GO:0051539; GO:0005737 -> GO:0005829. NEW GO:1904047 (IDA PMID:19736993).
