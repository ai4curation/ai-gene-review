# pvdL notes

2026-07-10: First-pass curation for the translation/RNA-processing NRPS spillover batch.

Asta was run for this gene and returned fast retrieval, but the useful gene-specific content was mainly the UniProt-derived target context; most retrieved papers were generic database/annotation resources rather than pyoverdine NRPS papers. The curation therefore uses Asta for provenance plus UniProt/domain evidence and the previously generated pyoverdine NRPS pathway report for mechanistic context.

Key evidence:
- [file:PSEPK/pvdL/pvdL-goa.tsv "UniProtKB	Q88F56	pvdL	enables	GO:0003824	catalytic activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR001242	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	Carrier domain-containing protein	20260706"]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DE   SubName: Full=Non-ribosomal peptide synthase (Subunit of ferribactin synthase) {ECO:0000313|EMBL:AAN69823.1};"]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   InterPro; IPR010071; AA_adenyl_dom."]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   InterPro; IPR001242; Condensation_dom."]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   InterPro; IPR010060; NRPS_synth."]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   InterPro; IPR020806; PKS_PP-bd."]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   InterPro; IPR006162; Ppantetheine_attach_site."]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   InterPro; IPR040097; FAAL/FAAC."]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   Pfam; PF00501; AMP-binding; 4."]
- [file:PSEPK/pvdL/pvdL-uniprot.txt "DR   Pfam; PF00668; Condensation; 4."]

Curation implications:
- Treat the gene as a pyoverdine/ferribactin NRPS subunit, not as translation/RNA-processing despite the word `non-ribosomal`.
- Replace generic catalytic activity with NRPS activity where possible.
- Replace phosphopantetheine binding with phosphopantetheine-dependent carrier activity.
- Route broad secondary-metabolite or wrong-family siderophore terms to pyoverdine/siderophore biosynthesis.
