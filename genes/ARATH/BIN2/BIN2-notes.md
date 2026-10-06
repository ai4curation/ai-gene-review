# BIN2 (ASK7/SK21; At4g18710, UniProtKB:Q39011) curation notes

Session 2026-10-05/06 (brassinosteroid_signaling module curation).

- Symbol lookup `BIN2` first returned an unreviewed TrEMBL entry (F4JRM5, 274 aa fragment); refetched by accession Q39011 (KSG7_ARATH, Shaggy-related protein kinase eta = ASK7 = AtSK21 = BIN2 = DWF12 = UCU1). gene_symbol set to BIN2.
- Falcon deep research attempted; HTTP 402, no report.
- GSK3/SHAGGY kinase, negative regulator [PMID:11847343 "BIN2 acts as a negative regulator to control steroid signaling in plants."]
- Substrates BZR1 [PMID:12114546], BES1 [PMID:12007405], YDA [PMID:22307275], SPCH [PMID:22466366], ARF2 [PMID:18599455], EGL3/TTG1 [PMID:24771765], RAPTOR1B [PMID:36151786].
- Inactivation: BSU1 dephosphorylation of pTyr200 [PMID:19734888]; KIB1-mediated degradation [PMID:28575660 "KIB1 as an F-box E3 ubiquitin ligase that promotes the degradation of BIN2 while blocking its substrate access"]; proteasome [PMID:18726001].
- GO:0009729 detection of BR stimulus (IMP) -> MODIFY to GO:1900458 (detection is the receptor step).
- Many protein-binding IPIs: kinase partners -> GO:0019901; substrates/scaffolds -> REMOVE (uninformative).
