# Traf2 (mouse, P39429) curation notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: new full review of all 172 GOA rows for mouse Traf2 (UniProtKB:P39429, MGI:101835). No ProtNLM2 file or prediction-evidence folder was opened or used. This review is meant to serve as the experimental reference for transfer to human TRAF2 (Q12933) and other orthologs, so the notes below separate mouse-experimental claims from projected ones.

**Deep research.** `just deep-research-falcon mouse Traf2 --fallback perplexity-lite` was run on 2026-10-20. Falcon failed with "Failed to authenticate". Perplexity-lite returned HTTP 401 (quota exceeded). No provider file exists. The review is built from cached primary literature: the 28 GOA-cited papers, plus seven mouse genetics papers fetched for this review (PMID:9390694, PMID:10514016, PMID:15539150, PMID:18313334, PMID:18997794, PMID:18997792, PMID:26701909).

**Identity and evolutionary grounding.** P39429 is the reviewed canonical mouse TRAF2 (501 aa). It has a RING (34-73), TRAF-type zinc fingers (124-180, 177-233) and a C-terminal MATH domain. Isoform 2 (TRAF2A, VSP_007402) exists; no row is isoform-specific. PANTHER places it in PTHR10131:SF21 (TRAF2 orthologs), the same subfamily as human Q12933. Mouse Traf2 is an IBD donor at:
- PTN002562154 (Euteleostomi TRAF2 node): GO:0004842, GO:0043123, GO:1990604
- PTN000805720 (TRAF1/TRAF2 clade): GO:0033209. The GO:0005164 IBD at this node is seeded by human TRAF1/TRAF2.
- PTN008301857 (deep TRAF node): GO:0035591, with mouse Traf2 as the only seed

The ISO/IEA rows come from human Q12933 (GO_REF:0000119/0000107) and rat B5DFH7/RGD:1310457 (GO_REF:0000096). All three proteins are in the same subfamily, so adaptor-level transfer is grounded.

**Mouse-experimental functions (established in this species):**
- TNF signaling. Traf2-/- cells show severe loss of TNF-induced JNK and only a mild NF-kappaB defect. They are hypersensitive to TNF-induced death, and serum TNF is elevated [PMID:9390694 "Examination of traf2-/- cells revealed a severe reduction in TNF-mediated JNK/SAPK activation but a mild effect on NF-kappaB activation."]. TRAF2 has to recruit cIAP1/2 for TNFR1 to drive NF-kappaB efficiently. The RING is not needed for NF-kappaB, but it is needed for protection against apoptosis [PMID:19815541]. Deleting Traf2 in keratinocytes disrupts TNF signaling, and Sphk1 is not needed for this [PMID:26701909].
- CD40 signaling. Traf2-deficient B cells cannot activate canonical NF-kappaB or proliferate after CD40 ligation [PMID:15539150]. Defective T-dependent antibody responses are seen in Traf2/Tnf double knockouts [PMID:10514016]. TRAF2 recruits HOIP, cIAP1 and IKKs to CD40 [PMID:20614026].
- Non-canonical NF-kappaB. When TRAF2 is lost, p100 processing becomes constitutive [PMID:15539150]. TRAF2 recruits cIAP1/2 into the NIK-degrading complex, while TRAF3 brings in NIK [PMID:18997794]. Receptor-induced degradation of TRAF3 requires TRAF2 [PMID:18997792; PMID:18313334; PMID:12958312].
- Other experimental contexts, all treated as non-core:
  - ER-stress complexes containing IRE1, AIP1 and TRAF2 [PMID:18281285]
  - IL-17 stabilization of CXCL1 mRNA, which needs both TRAF2 and TRAF5 [PMID:21822258]
  - K63 ubiquitination of GbetaL, which shifts the balance between mTORC1 and mTORC2 [PMID:28489822]
  - RNS-induced JNK activation and non-apoptotic death in MEFs [PMID:18007661]
  - CD27 signaling to JNK [PMID:9692890]
  - CD40-induced IRAK1 sumoylation in macrophages [PMID:24706909]

**Inferred only (projection, no mouse experiment found):** T cell cytokine and IL-2 production, PTPN2 binding, GSTP1 complex, pyroptosis, glial apoptosis, cell cortex, and sphingolipid (S1P) binding. Sphk1 deficiency does not phenocopy Traf2 loss in mouse [PMID:26701909], which argues against S1P being important in vivo.

**E3 activity.** Kept as non-core (GO:0004842, GO:0061630, GO:0051865), the same decision as in the human review.
- For: mouse data show TRAF2-dependent K63 ubiquitination of GbetaL that needs the RING [PMID:28489822], and PAINT places GO:0004842 at PTN002562154.
- Against: in mouse cells the RING is dispensable for TNF-induced NF-kappaB and RIPK1 ubiquitylation [PMID:19815541], and the cIAPs are the principal E3s in TNFR1 signaling [PMID:26701909].

**Main decisions.**
- Generic protein binding (23 rows). Rows whose partner tells us something were changed to MODIFY:
  - TNFRSF receptors (RANK, LTbetaR, OX40, CD27) to GO:0005164
  - CD40 to GO:0005174
  - cIAP2 to GO:0031625
  - TAK1 to GO:0031435
  - IRAK1 and the IRE1/AIP1 complex to GO:0019901

  All other generic rows (TNFR1 via TRADD, HCV NS5A, caspase-8/10, TANK, A20, Mnk2, Fcrla, FLN29, TRAF3) were changed to REMOVE as uninformative. The REMOVE does not mean the interactions are false.
- GO:0043120 TNF binding was changed to REMOVE. TRAF2 is intracellular and does not bind the cytokine. This matches the human review.
- Terms that are true but general were changed to MODIFY, pointing to the specific term the gene already carries:
  - cytoplasm to cytosol and cytoplasmic side of PM
  - signal transduction to TNF-mediated signaling and CD40 signaling
  - protein-macromolecule adaptor activity to signaling adaptor activity
  - protein ubiquitination to K63-linked ubiquitination
  - MAPK cascade to JNK cascade
  - TNFRSF binding to TNFR binding
  - generic complex terms to TNFRSF complex
  - metal ion binding to zinc ion binding
  - programmed cell death to regulation of apoptotic process
  - regulation of molecular mediator production to regulation of immunoglobulin production
  - enzyme binding to ubiquitin protein ligase binding and protein kinase binding
  - positive regulation of TNF signaling (the HCV core paper) to TNF-mediated signaling pathway
- Six rows are UNDECIDED: cell cortex (2), glial apoptosis (2) and positive regulation of extrinsic apoptotic signaling (2). Mouse genetics points the opposite way on the last of these.
- No NEW annotations. I considered GO:1901223 (negative regulation of non-canonical NF-kappaB signal transduction). A comparator check on QuickGO found that neither mouse TRAF3 (Q60803) nor human TRAF3 carries it, and cIAP1/2 carry only GO:1901222 or GO:0038061. Because that absence looks like a convention I have not yet identified, I raised it as a suggested question instead of asserting it.

**Core functions:**
- signaling adaptor activity in TNF/CD40 signaling
- TNF receptor binding
- cIAP (ubiquitin protein ligase) binding, for non-canonical NF-kappaB control and K63 ubiquitination
- MAP3K binding in the IRE1-TRAF2-ASK1 complex
