# Mtmr9 (mouse, Q9Z2D0) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This is the first review of mouse Mtmr9. It was written as the reference for transfer to human MTMR9 (Q96QG7). No ProtNLM2 file or prediction-evidence folder was opened.

### Deep research
`just deep-research-falcon mouse Mtmr9 --fallback perplexity-lite` failed. Falcon/Edison returned "Failed to authenticate" (HTTP 403), and the perplexity-lite fallback also failed, so no deep-research file exists. The review is based on the cached primary literature (abstracts only; a forced re-fetch of PMC187840 and PMC3964036 did not return full text), the mouse Swiss-Prot entry, PAINT data for PTHR10807, and the cached mouse Reactome reactions. Web searches for further mouse Mtmr9 primary studies (knockout or physiology) found nothing usable.

### Identity and evolutionary grounding
- Q9Z2D0 is the reviewed 545-aa mouse entry. PANTHER places it in subfamily PTHR10807:SF56 (MYOTUBULARIN-RELATED PROTEIN 9) with human MTMR9 Q96QG7 and bovine A7MB43 [file:mouse/Mtmr9/Mtmr9-uniprot.txt "PTHR10807:SF56; MYOTUBULARIN-RELATED PROTEIN 9"]. Human-to-mouse transfers in this review are therefore ortholog transfers within one subfamily.
- The catalytic loop at 332-340 reads HGTEGTDST, as in human. Both the Cys and the Arg of CX5R are lost [file:human/MTMR9/MTMR9-bioinformatics/RESULTS-rereview.md "MTMR9 lacks both the catalytic cysteine and the catalytic arginine"]. I checked this against the mouse sequence in the UniProt file ("...ASVL IHGTEGTDST LQ...", residues 327-342).
- PAINT: PTN000086907 (MTMR9 lineage, Bilateria) has IRD NOT for GO:0004438 and GO:0106018, but GO:0046856, inherited from PTN008506586, was not negated. PTN002246859 (Eumetazoa) carries GO:0019903 and GO:0010507 and is seeded by human MTMR9. Mouse Mtmr9 descends from all of these nodes.

### What is experimental in mouse, and what is inferred
Experimental for mouse Mtmr9:
- Mtmr7 binding. Mtmr9 is the Mtmr7-binding protein found by IP-MS from N1E-115 cells, and its coiled coil is sufficient for the binding [PMID:12890864 "The coiled-coil domain of MTMR9 was sufficient for binding to MTMR7."].
- Activation of Mtmr7 [PMID:12890864 "The binding of MTMR9 increased the Ins(1,3)P2 phosphatase activity of MTMR7."]. Reactome R-MMU-6809627 gives a 2- to 5-fold increase.
- Homodimer formation and the Mtmr6 heterodimer. These rest on the full text via UniProt (ECO:0000269 PubMed:12890864) and are not stated in the abstract.
- Cytoplasm and ruffle membrane localization during EGF-induced macropinocytosis. Deleting residues 2-108 (GRAM region) abolishes cell membrane recruitment. All of this is ECO:0000269 PubMed:24591580 in UniProt.

Inferred from human MTMR9 (by similarity / ISO):
- Activation of MTMR6 and MTMR8, with substrate preference set by the partner (PMID:19038970, PMID:22647598).
- Stabilization of MTMR6 [PMID:19038970 "the formation of this heteromer in cells resulted in increased protein levels of both MTMR6 and MTMR9"].
- Inhibition of autophagy through MTMR8 [PMID:22647598 "the MTMR8/R9 complex inhibits autophagy"].
- Apoptosis protection, ER and perinuclear localization.
- The macropinocytosis requirement (siRNA). UniProt marks the function as by similarity.

### Decisions (30 rows: ACCEPT 16, KEEP_AS_NON_CORE 8, MODIFY 6)
- GO:0005515 IPI (partner mouse Mtmr7, PMID:12890864) → MODIFY to GO:0019902 phosphatase binding.
- GO:0019903 protein phosphatase binding (IBA/IEA/ISO) → MODIFY to GO:0019902. The partners are lipid phosphatases. This matches the human review and is raised as a question.
- GO:0030234 enzyme regulator activity (IDA and ARBA IEA) → MODIFY to GO:0019211 phosphatase activator activity. The IDA row is the mouse Mtmr7 activation result.
- ACCEPT: GO:0019211, GO:0010922, GO:0060304, GO:0046856 (IBA; Mtmr9 contributes activation to the step, and PAINT deliberately kept it), GO:0050821, GO:0032991, cytoplasm (all rows), cytosol (all rows).
- KEEP_AS_NON_CORE:
  - ER (ISS/ISO/IEA; by similarity only).
  - Perinuclear region (by similarity only).
  - Ruffle membrane. This is experimental in mouse, but recruitment is stimulus-dependent.
  - Negative regulation of autophagy (IBA/IEA/ISO). The human data are sound but describe a downstream cellular effect, and it has not been tested in mouse.
- No NEW terms. Macropinocytosis was deliberately not added: the evidence is knockdown necessity, the MTMR6 phosphatase does the PI3P step, and Mtmr9 is already covered by the regulation terms.
