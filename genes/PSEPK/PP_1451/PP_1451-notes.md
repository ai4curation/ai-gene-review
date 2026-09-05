# PP_1451 curation notes

## 2026-09-01 evidence reconciliation

The gene-level OpenScientist request reached the configured 7200-second limit
without producing a report. The pathway report classified PP_1451 as an
uncertain tether-release candidate because short-range k-mer and
Smith-Waterman comparisons did not recover E. coli DpaA. That result is
superseded by exact family evidence: PP_1451/Q88MW7, PA14
LdtPae3/A0A0H2ZF55, and the
reviewed E. coli DpaA protein P0AA99 all map to PANTHER PTHR36699:SF1. PAINT
places GO:0004175 endopeptidase activity at a bacterial PTHR36699 node using
P0AA99 as descendant evidence.

Two independent studies directly establish the activity of the E. coli
exemplar. LdtF/YafK is described as a murein hydrolase that cleaves Lpp from the
peptidoglycan sacculus [PMID:33941679, "Here, using genetic and biochemical
approaches, we show that LdtF (formerly yafK), a newly identified paralog of
l,d-transpeptidases in E. coli, is a murein hydrolytic enzyme that catalyzes
cleavage of Lpp from the PG sacculus."]. The independent DpaA study reports the
same hydrolysis reaction [PMID:33947763, "We now show that LdtF hydrolyzes the
Lpp-peptidoglycan linkage, detaching Lpp from peptidoglycan, and have renamed
LdtF to peptidoglycan meso-diaminopimelic acid protein amidase A (DpaA)."].

This establishes the hydrolase family and supports GO:0004175 as PP_1451's
first-pass molecular function. The exact OprI-like substrate and activity of
PP_1451 itself remain untested in Pseudomonas putida KT2440.

The Pseudomonas paper does not directly demonstrate LdtPae3 hydrolysis. Its
full-text discussion states that the function was tentative and based on the
absence of amide-bond-forming activity plus similarity to YafK [PMID:37255442,
"The function of LdtPae3 was tentatively assigned to the release of OprI based
on both the absence of detectable amide bond-forming activity (formation of
3→3 and tripeptide→ OprI bonds) and the close similarity between LdtPae3 and
E. coli hydrolase YafK."]. This is retained as supporting orthology evidence,
not treated as a direct biochemical assay.
