# PP_4602 notes

## 2026-07-10 AraC/XylS-family regulator first pass

- Batch: `projects/P_PUTIDA/batches/module_regulation_signal_transduction_arac_xyls_transcriptional_regulators.tsv`.
- Main conclusion: PAS-domain AraC-family DNA-binding transcription regulator candidate with unsupported kinase-family side call.
- Decision: keep DNA-binding transcription factor activity as the shared core molecular function; leave direct regulon, effector, and regulatory direction unresolved unless separately curated.
- Kinase activity is treated as likely over-propagated side context and not a core function.

Primary provenance:
- [file:PSEPK/PP_4602/PP_4602-goa.tsv "UniProtKB	Q88E65	PP_4602	enables	GO:0003700	DNA-binding transcription factor activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR018060|InterPro:IPR018062	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	HTH araC/xylS-type domain-containing protein	20260706"]
- [file:PSEPK/PP_4602/PP_4602-uniprot.txt "DE   SubName: Full=Transcriptional regulator, AraC family {ECO:0000313|EMBL:AAN70175.1};"]
- [file:PSEPK/PP_4602/PP_4602-uniprot.txt "DR   InterPro; IPR018060; HTH_AraC."]
- [file:PSEPK/PP_4602/PP_4602-uniprot.txt "DR   InterPro; IPR018062; HTH_AraC-typ_CS."]
- [file:PSEPK/PP_4602/PP_4602-uniprot.txt "DR   InterPro; IPR020449; Tscrpt_reg_AraC-type_HTH."]
- [file:PSEPK/PP_4602/PP_4602-uniprot.txt "DR   InterPro; IPR009057; Homeodomain-like_sf."]
- [file:PSEPK/PP_4602/PP_4602-uniprot.txt "DR   InterPro; IPR035965; PAS-like_dom_sf."]
- [file:PSEPK/PP_4602/PP_4602-uniprot.txt "DR   InterPro; IPR013656; PAS_4."]
