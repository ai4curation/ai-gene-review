# PANTHER, PTHR22988 / PTHR24356: Warts/LATS kinases split across two families

**Destination:** PANTHER team (pantherdb.org feedback).

**Summary.** Warts/LATS kinases fall in two families depending on the
sequence. Human LATS1 (O95835) and LATS2 (Q9NRM7) are in PTHR24356 (SF138,
SF149), as are *S. rosetta* Warts (F2U943, SF418) and *M. brevicollis* LATS
(A9UVF9). But UniProt's PANTHER cross-references put the following in
**PTHR22988**, "MYOTONIC DYSTROPHY S/T KINASE-RELATED" (ROCK, MRCK, citron):
- Drosophila wts (Q9VA38, SF76);
- *Capsaspora* coWts (A0A0D2VGR4, SF71 "CITRON RHO-INTERACTING KINASE").

Fly wts is a reference-tree leaf and takes its IBAs from the LATS node
PTN002390470 in PTHR24356, so its annotations are right. *Capsaspora* is not a
reference genome, so coWts is annotated by TreeGrafter from node PTN001122925.
It therefore inherits cytoskeleton and actomyosin structure organization, and
misses hippo signaling.

**Evidence.**
- Gene targeting identifies coWts as CAOG_00619 (PMID:38517944); NCBI names
  it "serine/threonine protein kinase lats".
- Loss of coWts makes the Yorkie homolog coYki nuclear (PMID:38517944).
- coWts carries a LATS-type MOB-binding region.

**Requested change.** Rescore coWts, fly wts and F2U943 against the PTHR22988
SF71/SF76 and PTHR24356 LATS subfamily HMMs. If PTHR22988 wins for some LATS
sequences, adjust the LATS HMM or the family boundary.

**Repo references.** `genes/CAPO3/coWts/coWts-ai-review.yaml` (actomyosin
structure organization removed; cytoskeleton over-annotated; hippo signaling
added by IMP).
