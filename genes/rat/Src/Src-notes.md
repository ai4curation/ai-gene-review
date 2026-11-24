# Src (rat) review notes

## Session 1 (initial review)

- Fetched with `just fetch-gene rat Src`; UniProt Q9WUD9 (SRC_RAT, RGD:620795, GeneID 83805)
  confirmed. 272 GOA rows. Literature synthesis in `Src-deep-research-manual.md` (no
  deep-research API available).
- Most cached papers are abstract-only; full text available for PMID:10884433, 19230846,
  19736311, 19948503, 20167931, 20356829, 20380727, 26026271, 28220894 and 19193640.
- Core picture: myristoylated SH3-SH2-kinase non-receptor tyrosine kinase
  [UniProtKB:Q9WUD9 "Non-receptor protein tyrosine kinase which is activated following
  engagement of many different classes of cellular receptors"]; at the plasma membrane and
  focal adhesions it relays integrin, RTK and GPCR (angiotensin II) signals; in neurons it is
  anchored to the NMDA receptor complex and up-regulates NMDA channel activity
  [PMID:9005855 "the endogenous tyrosine kinase Src was shown to regulate the activity of
  NMDA channels"].
- Decisions:
  - Kinase MF rows (protein kinase / kinase / protein tyrosine kinase activity) MODIFY to
    GO:0004715 non-membrane spanning protein tyrosine kinase activity, the core MF.
  - Bare protein binding rows REMOVE, except PMID:8849729 (SH2 binds Pyk2 pTyr402) ->
    phosphotyrosine residue binding and PMID:16352297 (SH3 binds Cav1.2 alpha1c) ->
    transmembrane transporter binding.
  - Generic CC (membrane, cell junction, anchoring junction, actin-based cell projection)
    MODIFY to plasma membrane / focal adhesion / cell-cell junction / podosome.
  - IEP rows on CC terms (glutamatergic synapse, postsynaptic specialization from
    PMID:14529711) get WRONG_EVIDENCE_CODE source defects (CHECK); the location itself is
    supported by the IDA rows from the same paper.
  - Several IEP "response to X" / proliferation rows rest on expression or activation
    correlation only: MARK_AS_OVER_ANNOTATED.
  - PMID:2462872 (PC12 growth cones) curated to dendritic growth cone / dendritic filopodium;
    PC12 neurites are not dendrites -> MODIFY to growth cone with source defect, filopodium
    row UNDECIDED.
  - PMID:10698670 (testicular Src) curated to mitochondrion-derived vesicle: not supported
    by abstract -> UNDECIDED with CHECK defect.
  - PMID:9227431 DNA biosynthetic process -> MODIFY to positive regulation of DNA
    biosynthetic process (Src is a signalling kinase, not a DNA synthesis enzyme).
  - GO:0030331 carries an "obsolete" prefix in the GOA label, but OLS and the local GO build
    still list "nuclear estrogen receptor binding" as live; kept as non-core.
- NEW: GO:2000310 regulation of NMDA receptor activity (IDA, PMID:9005855). Src catalyses the
  regulatory phosphorylation itself, so it passes the participation test. Comparator check
  (QuickGO, GO:2000310 exact, 42 rows): the regulator kinase DAPK1 (IMP, mouse) and the
  scaffold Dlg4 (IMP, rat) carry the term, so regulatory kinases of the receptor are within
  GO convention; Fyn does not carry it, which is an absence rather than a contrary convention.
- PMID:19193640 (annexin 2 and v-Src) read in full; concerns viral Src in Rat-1 cells; used
  only as context.
