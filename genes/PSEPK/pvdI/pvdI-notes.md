# pvdI notes

2026-07-10: First-pass curation for the translation/RNA-processing NRPS spillover batch.

Asta was run for this gene and returned fast retrieval, but the useful gene-specific content was mainly the UniProt-derived target context; most retrieved papers were generic database/annotation resources rather than pyoverdine NRPS papers. The curation therefore uses Asta for provenance plus UniProt/domain evidence and the previously generated pyoverdine NRPS pathway report for mechanistic context.

Key evidence:
- [file:PSEPK/pvdI/pvdI-goa.tsv "UniProtKB	Q88F77	pvdI	enables	GO:0003824	catalytic activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR001242	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	Carrier domain-containing protein	20260706"]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DE   SubName: Full=Non-ribosomal peptide synthetase (Subunit of ferribactin synthase) {ECO:0000313|EMBL:AAN69802.1};"]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DR   InterPro; IPR010071; AA_adenyl_dom."]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DR   InterPro; IPR001242; Condensation_dom."]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DR   InterPro; IPR020806; PKS_PP-bd."]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DR   InterPro; IPR006162; Ppantetheine_attach_site."]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DR   Pfam; PF00501; AMP-binding; 2."]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DR   Pfam; PF00668; Condensation; 2."]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "DR   Pfam; PF00550; PP-binding; 2."]
- [file:PSEPK/pvdI/pvdI-uniprot.txt "KW   Phosphopantetheine {ECO:0000256|ARBA:ARBA00022450};"]

Curation implications:
- Treat the gene as a pyoverdine/ferribactin NRPS subunit, not as translation/RNA-processing despite the word `non-ribosomal`.
- Replace generic catalytic activity with NRPS activity where possible.
- Replace phosphopantetheine binding with phosphopantetheine-dependent carrier activity.
- Route broad secondary-metabolite or wrong-family siderophore terms to pyoverdine/siderophore biosynthesis.
