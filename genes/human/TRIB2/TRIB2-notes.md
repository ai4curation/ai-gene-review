# TRIB2 (human, Q92519) review notes

## 2026-11-26: review started from literature-scan issue 7137

The trigger paper is PMID:43019314 (TRIB2 supports a high glycolytic phenotype in melanoma cells).

### Deep research

Deep research did not run. `just deep-research-falcon human TRIB2 --fallback perplexity-lite`
failed: the falcon API returned 403 "Failed to authenticate", and perplexity-lite returned 401 because
its quota is used up. No provider file was written. I searched the literature by hand instead, with
PubMed E-utilities (esearch, sorted by relevance), using these queries:

- `TRIB2[ti] AND (pseudokinase OR ATP OR COP1 OR AKT OR "C/EBP" OR ubiquitin OR structure)`
- `(Tribbles 2 OR TRIB2 OR TRB2) AND (autophosphorylates OR "binds to ATP" OR "covalent inhibitors" OR "C/EBPalpha" OR Keeshan OR COP1)`

From the results I cached and read these papers:

- PMID:25583260: human TRB2 binds ATP weakly and autophosphorylates in a metal-independent way
  (full text). It contradicts the ISS NOT nucleotide binding row.
- PMID:27563873: human TRIB2 drives K48-linked ubiquitination and nuclear proteasomal degradation of
  CDC25C (full text).
- PMID:20805362: mouse Trib2 needs both its COP1-binding motif and its kinase domain to degrade
  C/EBPalpha and to cause AML (abstract).
- PMID:20208562: TRIB2 represses FOXO in melanoma (abstract).
- PMID:28276427: a TRIB2-activates-AKT paper (Nat Commun 2017) that was RETRACTED (retraction note
  PMID:37468494). I did not use it.

### What the trigger paper adds

PMID:43019314 (full text) used two CRISPR TRIB2-KO clones of UACC-62 melanoma cells. Compared with
the parental cells, the knockouts showed:

- lower glucose consumption, lactate secretion and ECAR (glycolysis and glycolytic capacity);
- unchanged OCR;
- lower PDK4 mRNA and protein, and lower citrate synthase activity.

There is no re-expression rescue and no mechanism, and the authors state "the molecular mechanisms
linking TRIB2 to PDK4 remain to be elucidated". The paper therefore shows an indirect, cell-line
phenotype, a TRIB2-dependent glycolytic state, and not a molecular function.

I did not add a NEW `positive regulation of glycolysis` (GO:0045821) row. The evidence comes from
one cell line, has no rescue, and the effect is most likely downstream of TRIB2's AKT/FOXO and
transcriptional effects. The paper did not close a molecular-function gap for TRIB2.

### Annotation decisions

- REMOVE: ISS NOT nucleotide binding, which PMID:25583260 contradicts directly; and two bare
  GO:0005515 rows from interactome screens.
- UNDECIDED: NOT protein kinase activity and NOT protein phosphorylation. Weak autophosphorylation
  exists, but no substrate kinase activity has been shown.
- MARK_AS_OVER_ANNOTATED: cytoskeleton, which rests only on a UniProt "may associate" note.
- Core: GO:0055106 ubiquitin-protein transferase regulator activity, the COP1 adaptor role, with
  positive regulation of proteasomal ubiquitin-dependent protein catabolism. GO uses GO:0055106 for
  all three human Tribbles (QuickGO, 2026-11-26), so I kept it rather than moving to GO:1990756.

## 2026-11-27: changes after the PR #7144 review

- Added NEW GO:0005524 ATP binding (IDA, PMID:25583260), so the positive finding is recorded rather than lost with the removed NOT row.
- Recorded the UniProt ISS negation as a source defect.
- Changed GO:0055106 to MODIFY, replaced by GO:1990756 ubiquitin-like ligase-substrate adaptor activity. QuickGO (2026-11-27) shows GO:1990756 sits under molecular adaptor activity, as a sibling of GO:0055106, not a descendant. This row's evidence (PMID:20805362: binds both COP1 and C/EBPalpha; kinase-domain mutants bind but do not degrade) supports the adaptor reading. This supersedes the earlier entry above that kept GO:0055106.
