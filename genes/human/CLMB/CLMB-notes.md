# CLMB (calcimembrin; C16orf74; MICT1) - curation notes

## Identity
- UniProt Q96GX8, HGNC:23362, symbol CLMB; synonyms C16orf74, MICT1. 76 aa canonical
  isoform (V1); isoform 2 (V3) lacks residues 1-12 (and thus the myristoylation site).
- Canonical, annotated ORF (not an alt-ORF peptide), so the standard folder convention applies.
- Family: DUF4597 (Pfam PF15366, InterPro IPR027864), PANTHER PTHR37455. No TM segment;
  membrane association via lipidation (N-myristoyl Gly2, S-palmitoyl Cys7/Cys14).
- Mouse ortholog Q8K1L6 (1190005I06Rik / Mict1).

## Literature (PubMed search C16orf74 OR calcimembrin OR MICT1, Oct 2026: 17 hits)
Most hits are cancer prognostic / bioinformatic signature papers. Mechanistic papers:

1. PMID:28881575 (Nakamura lab, 2017, pancreatic cancer). Identified PPP3CA as partner.
   [PMID:28881575 "Endogenous PPP3CA interacted with the phosphorylated form of endogenous C16orf74 (arrow)."]
   PxIxIT (PDIIIT) dependence: [PMID:28881575 "IP assays demonstrated that a mutant in which the PDIIIT sequence within C16orf74 is deleted (∆PDIIIT) completely abolished the interaction with PPP3CA (Figure 5C)"]
   Phospho-T44 dependence: [PMID:28881575 "we confirmed that the non-phosphorylated form of C16orf74 (the T44A substitutant) did not interact with PPP3CA in the IP assay (Figure 5C)"]
2. PMID:29371937 (2017) cell-permeable DN peptide blocks C16orf74/calcineurin binding,
   suppresses PDAC proliferation. [PMID:29371937 "DN-C16orf74 inhibited the binding of C16orf74 to CN in an immunoprecipitation assay."]
3. PMID:31597713 (2020, abstract only) - homodimer under the cell membrane, binds integrin
   aVb3, Rac1/MMP2 activation in PDAC invasion. Cancer-cell phenotypes; not used for GO.
4. PMID:41224739 (Cyert lab, Nat Commun 2025; preprint PMID:38798520) - names calcimembrin.
   Lipidation: [PMID:41224739 "Together, these findings establish that CLMB is myristoylated at Gly2 and S-acylated at Cys7 and Cys14."]
   Composite LxVPxIxIT motif; CLMB is a calcineurin substrate (pThr44):
   [PMID:41224739 "Together, these data show that both the LxVP and PxIxIT components of the composite motif are functional, that CLMB is a calcineurin substrate, and that pThr44 increases CLMB binding to calcineurin."]
   Recruitment of calcineurin to membranes: [PMID:41224739 "Thus, CLMB recruits calcineurin to membranes primarily via PxIxT-mediated binding."]
   and with the IxIT mutant [PMID:41224739 "In contrast, when co-expressed with CLMBIxITMut, this colocalization was greatly reduced, and calcineurin was predominantly cytosolic."]
5. PMID:40355556 (Sul lab, EMBO J 2025) - MICT1 in brown/beige adipocytes. Mostly mouse
   (KO, BAT-specific ablation, overexpression), but human MICT1 also tested in human beige
   adipocytes (adipose MSC derived): [PMID:40355556 "Together, these data show that MICT1 promotes thermogenic gene expression and can improve insulin sensitivity in human beige adipocytes."]
   Human MICT1 in plasma membrane fraction of HEK293: [PMID:40355556 "When we overexpressed the human ortholog, which corresponds to the mouse 76 aa MICT1 in HEK293 cells, human MICT1 was also found in the plasma membrane fraction (Fig."]
   Mechanism: MICT1 binds PP2B via PxIxIT, limiting PP2B-RIIb interaction / RIIb dephosphorylation,
   prolonging PKA activity. G2A (non-myristoylated) MICT1 is inactive.

## Interpretation
- MF: best described as a calcineurin (PP2B) docking/anchoring protein: binds CNA via a
  phospho-regulated high-affinity PxIxIT, and as a lipid-anchored protein targets calcineurin to
  membranes -> protein phosphatase 2B binding (GO:0030346) plus protein-membrane adaptor activity
  (GO:0043495). It is also a calcineurin substrate (no GO MF for "being a substrate").
  Whether its net effect is inhibitory (sequestering CN from RIIb; Sul) or a membrane-targeting
  scaffold that can promote dephosphorylation of LxVP-only membrane substrates (Cyert) is
  context-dependent; I did not assert protein phosphatase inhibitor/regulator activity.
- UNC119 Y2H hits (3 high-throughput screens): UNC119 is a carrier for N-myristoylated cargo,
  so this is plausibly a genuine lipid-cargo interaction, but it says nothing about CLMB's own
  function; bare protein binding -> REMOVE per project policy.
- BP adaptive thermogenesis: supported in human beige adipocytes (OE) and mouse KO; the role is
  modulatory (PKA signalling tuning). Accepted as annotated; regulation term
  (GO:0120162 positive regulation of cold-induced thermogenesis) raised as a question.
- Cancer roles (PDAC invasion, prognostic marker) are not GO-annotatable functions.
