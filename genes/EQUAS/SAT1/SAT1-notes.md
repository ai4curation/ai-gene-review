# SAT1 (donkey, A0A9L0KCT9) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry, 171 aa; names, function text and catalytic activities come from ARBA. A human SAT1 review exists in this repository (genes/human/SAT1/SAT1-ai-review.yaml) and was used for consistency.

## Identity and sequence
- PANTHER PTHR10545:SF36 (DIAMINE ACETYLTRANSFERASE 1); GNAT domain 4-170 [file:EQUAS/SAT1/SAT1-uniprot.txt "DR   PANTHER; PTHR10545:SF36; DIAMINE ACETYLTRANSFERASE 1; 1."].
- 97.08% identity to human P21673 over the full length without gaps; catalytic Tyr140 conserved [file:EQUAS/SAT1/SAT1-bioinformatics/RESULTS.md "The human catalytic Tyr140 is conserved (donkey Tyr140)"].

## Function (human ortholog)
- Spermidine/spermine N1-acetyltransferase, rate-limiting enzyme of polyamine catabolism [PMID:1985966 "rate-limiting enzyme in the catabolism of polyamines"]; [PMID:17516632 "The N1-acetylation of spermidine and spermine by spermidine/spermine"].
- Substrate preference norspermidine = spermidine >> spermine; also 1,3-diaminopropane and 1,5-diaminopentane; putrescine is not among the listed substrates [file:human/SAT1/SAT1-uniprot.txt "Substrate"; "specificity: norspermidine = spermidine >> spermine > N(1)-"].
- Cytosolic [file:human/SAT1/SAT1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"].
- The UniProt PATHWAY line "putrescine degradation; N-acetylputrescine from putrescine" (UniPathway) is the basis of electronic putrescine catabolic process annotations; the cached abstracts (PMID:17516632, 16455797, 15283699, 1985966) do not mention putrescine acetylation by SAT1.

## Annotation decisions
- diamine N-acetyltransferase activity: ACCEPT (core).
- N-acetyltransferase, acetyltransferase, transferase, acyltransferase activities: TOO_GENERAL (all entailed by diamine N-acetyltransferase activity).
- cytoplasm: MODIFY to cytosol. polyamine metabolic process: MODIFY to polyamine catabolic process.
- spermidine binding (TreeGrafter): KEEP_AS_NON_CORE (substrate binding inherent to the activity; consistent with human review).

## ProtNLM2
- GO:0009447 putrescine catabolic process: not in donkey GOA; plausible only via the UniPathway assignment; SAT1's established substrates are spermidine/spermine, whose catabolism produces rather than consumes putrescine -> UNC.
- Non-GO output (not scored): subcellular location "Nucleus" (the human enzyme is cytosolic).
