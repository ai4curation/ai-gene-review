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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this pass.

### Deep research
- `just deep-research-falcon EQUAS SAT1 --fallback perplexity-lite` failed (falcon and the perplexity-lite fallback both exited with errors; no deep-research file written). Continued with the cached literature (PMID:17516632, PMID:1985966, PMID:15283699; all abstract-only) and the human SAT1 review.

### Identity
- A0A9L0KCT9 is the full-length canonical SAT1 product in donkey (171 aa, same length as human P21673, no gaps; Ensembl ENSEASP00005059060.1, chromosome X). Not a fragment, isoform or alternative gene model.
- Catalytic residues per the human structure [PMID:17516632 "suggested that Tyr140 acts as general acid and Glu92, through one or more water"] are conserved: donkey Glu92 and Tyr140 [file:EQUAS/SAT1/SAT1-bioinformatics/RESULTS-rereview.md].

### Evolutionary grounding
- UniProt PANTHER: PTHR10545:SF36 (DIAMINE ACETYLTRANSFERASE 1), the same subfamily as human SAT1 and mouse Sat1 (interpro/panther/PTHR10545/PTHR10545-entries.csv). The orchestrator listed no PANTHER id, but the UniProt record does carry SF36.
- 97.1% identical to human SAT1 vs 45.3% to human SAT2 (Q96F10, SF51) [file:EQUAS/SAT1/SAT1-bioinformatics/RESULTS-rereview.md]. SAT2 is not a polyamine catabolic enzyme [PMID:15283699 "These results indicate that SSAT2 is not a polyamine catabolic enzyme"], so polyamine N1-acetylation is transferred only within SF36.
- PAINT: GO:0004145 and GO:0019809 sit at PTN002576187 (Euteleostomi SAT1 node); GO:0008080 at the family root PTN000057452. The donkey TreeGrafter rows cite PTN008947708 (a TreeGrafter node id, not in the PAINT tsv). Family review PTHR10545-review.yaml agrees (SF36 = SAT1, SUBFAMILY_ONLY scope for GO:0004145); no disagreement on subfamily placement.

### Changes vs previous review
- polyamine metabolic process MODIFY now lists polyamine catabolic, spermidine catabolic and spermine catabolic process (matching human core functions); core function directly_involved_in extended likewise.
- Description rewritten to include catalytic mechanism and subfamily placement; ACCEPT reason for GO:0004145 now grounded in SF36 / PAINT node placement rather than identity alone.
- Added PMID:15283699 and RESULTS-rereview.md; reference_review on the PMIDs. All other actions (cytoplasm -> cytosol MODIFY; general MF terms TOO_GENERAL; spermidine binding KEEP_AS_NON_CORE) re-examined and retained.
- Putrescine catabolic process (UniPathway in human) not proposed: SAT1's characterised substrates are spermidine/spermine.

### Relative
- Human SAT1 (P21673), same subfamily SF36 and PAINT seed of PTN002576187; review at genes/human/SAT1/SAT1-ai-review.yaml has all annotations actioned and core_functions, though its status field still reads INITIALIZED.
- Modules: modules/polyamine_metabolism.yaml (animal_sat1_variant, PTHR10545:SF36).
