# ARL15 notes

## Biology
- GTP/GDP binding and GTPase kinetics [PMID:37939768]; GTP and CNNM binding; CNNM2 crystal structure; inhibits CNNM2 efflux and TRPM7 uptake [PMID:37449820].
- Negative regulator of Mg2+ transport via CNNM complex N-glycosylation [PMID:34089346].
- Active ARL15 binds the Smad4 MH2 domain and relieves its autoinhibition; positively regulates TGFbeta-family signalling. Smad4 acts as its GAP [PMID:35834310].
- Golgi localization:
  - Endogenous protein with golgin-245 in HeLa [PMID:35834310].
  - Palmitoylation-dependent movement between Golgi compartments in adipocytes [PMID:34779483].
  - Golgi cargo transport [PMID:40241309].
- Knockout mice have cleft palate [PMID:37773757]. Adipocyte role [PMID:29242557].

## GOA calls
- **ACCEPT:** GTP binding, GTPase activity.
- **REMOVE:** ND root-term rows (data now exist); Y2H protein binding (PDE6D, UNC119, MEOX2).
- **Non-core:** exosome (HDA).
- **NEW:** Golgi apparatus (IDA); positive regulation of SMAD protein signal transduction (IDA).
- Round 1 (PR #4177): the CNNM/Mg2+ role is now encoded as NEW transporter inhibitor activity (GO:0141110) plus negative regulation of cation transmembrane transport (GO:1904063), both IDA from PMID:37449820. GO has no magnesium-specific regulation term, so one is proposed in proposed_new_terms. No glycosylation term is proposed: ARL15 promotes CNNM N-glycosylation but does not perform it.
- Round 1 also adds: NEW endolysosome (IDA, PMID:35834310); S-acylation paper PMID:41999893 imported; PMID:36711628 recorded as the bioRxiv preprint of PMID:37449820; a PDE6D/UNC119 chaperone question added.
- Round 2 (PR #4177):
  - PMID:37449820 disputes ARL15's intrinsic GTPase activity and the Smad4-as-GAP claim (weak GTP binding, Ala at the catalytic Gln position). Recorded as finding_review DISPUTED on the PMID:37939768 kinetics finding.
  - GTPase ACCEPT kept, with both sides quoted. The description and core_functions[1] now say the activity is contested.
  - The GO:1904063 support now uses the data sentences (CNNM2 efflux, TRPM7 Zn2+), not the model statement.
  - The NTR justification explains why GO:0010960 is not a substitute.
  - The glycosylation quote was dropped from core_functions[0].
  - The GO:1904063 label was confirmed current in QuickGO (2026-10-04).
