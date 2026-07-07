# DLAT (P10515) — curation notes

Deep research (`DLAT-deep-research-falcon.md`) was NOT present within the 8-min poll window; this
review is grounded in the UniProt record (`DLAT-uniprot.txt`), the seeded GOA
(`DLAT-goa.tsv`), the cached `publications/PMID_*.md` files (all 16 cited PMIDs present) and
Reactome entries, plus `~/repos/dismech/kb/disorders/Pyruvate_Dehydrogenase_Deficiency.yaml`.

## Verified biology

DLAT (ODP2_HUMAN, PDC-E2, EC 2.3.1.12) is the dihydrolipoyllysine-residue acetyltransferase
(E2) component of the mitochondrial pyruvate dehydrogenase complex (PDC). It is the structural
and catalytic core of the complex.

- **Core MF**: GO:0004742 dihydrolipoyllysine-residue acetyltransferase activity. Reaction
  (UniProt/RHEA:17017): N6-[(R)-dihydrolipoyl]-L-lysyl-[protein] + acetyl-CoA =
  N6-[(R)-S(8)-acetyldihydrolipoyl]-L-lysyl-[protein] + CoA. Physiologically DLAT accepts the
  acetyl group from the E1-generated acetyl-dihydrolipoyl intermediate and transfers it to CoA
  to form acetyl-CoA [PMID:20160912 "E2 then transfers the acetyl moiety to CoA forming acetyl-CoA"].
- **Core BP**: GO:0006086 pyruvate decarboxylation to acetyl-CoA — DLAT catalyzes the E2 step of
  the overall pyruvate→acetyl-CoA conversion linking glycolysis to the TCA cycle.
- **Core CC/complex**: GO:0045254 pyruvate dehydrogenase complex; GO:0005759 mitochondrial matrix.
  The E2 (+E3BP) C-terminal catalytic domains form a 60-meric dodecahedral inner core to which E1,
  E3 and PDK/PDP attach [PMID:9045657 "inner core was assembled in the expected pentagonal
  dodecahedron shape"; PMID:19240034 "60-meric dodecahedral core comprising the C-terminal domains
  of E2p"; PMID:18184588 "Dihydrolipoyl acetyltransferase (E2) is the central component"].
- **Cofactor / lipoyl**: two covalent lipoyl cofactors at K132 and K259 (lipoyl-binding domains 1
  and 2); the lipoyl arm shuttles intermediates between active sites [PMID:25525879 K132/K259
  lipoyl; PMID:18184587 "lipoyl domains of E2 that carry catalytic intermediates shuttle between
  E1, E2, and E3 active sites"]. SIRT4 delipoylates DLAT to inhibit PDH (regulatory, non-core).
- **Disease**: biallelic loss-of-function DLAT variants cause pyruvate dehydrogenase E2 deficiency
  (PDHE2, MIM:245348) — a rare PDH-deficiency subtype with childhood lactic acidosis, episodic
  dystonia and neurologic dysfunction [UniProt DISEASE; PMID:16049940; disorders KB Orphanet
  record]. DLAT is also the 70-kDa M2 mitochondrial autoantigen of primary biliary cholangitis
  (genuine but non-core immunological fact) [UniProt; PMID:3174635].

## Annotation-review decisions (summary)

- Catalytic MF (GO:0004742): ACCEPT the experimental/IBA/IEA lines as core (IDA PMID:20160912,
  9242632, 9045657; IBA; IEA GO_REF:0000120 EC 2.3.1.12; TAS Reactome R-HSA-9861667; NAS
  PMID:3191998). GO:0016407 acetyltransferase activity (IEA) and GO:0016746 acyltransferase
  activity (IEA) are correct-but-general parents → MARK_AS_OVER_ANNOTATED (keep, non-core parent).
- BP GO:0006086 (multiple IDA/IBA/IEA/TAS/IC): ACCEPT as core process.
- GO:0042867 pyruvate catabolic process (IEA): broader/adjacent, KEEP_AS_NON_CORE.
- GO:0006099 tricarboxylic acid cycle (ISS): DLAT is not a TCA-cycle enzyme — it feeds the TCA
  cycle by producing acetyl-CoA but the PDH reaction is not part of the TCA cycle. Over-annotation
  → MARK_AS_OVER_ANNOTATED (do not REMOVE an ISS silently; keep flagged).
- CC: GO:0045254 (PDC) core; GO:0005759 mitochondrial matrix core; GO:0005739 mitochondrion
  (parent) KEEP_AS_NON_CORE.
- protein binding IPIs (GO:0005515): all bare "protein binding" → MARK_AS_OVER_ANNOTATED per policy
  (uninformative; underlying interactions are real: PDHB/E1, PDK2/PDK3, SIRT4). identical protein
  binding IPIs (GO:0042802, PMID:18184587/18184588) capture DLAT self-assembly into the homomeric
  core — informative → ACCEPT (KEEP_AS_NON_CORE structural).
