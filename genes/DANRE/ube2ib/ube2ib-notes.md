# Notes for DANRE ube2ib

- Core function is SUMO E2 conjugating enzyme activity [file:DANRE/ube2ib/ube2ib-uniprot.txt "Accepts the ubiquitin-like proteins sumo1, sumo2 and sumo3"].
- Developmental annotations for heart and definitive hematopoiesis are retained as non-core outputs of SUMOylation [PMID:25757417 "sumoylation is essential for HSPC development during definitive hematopoiesis"].

## Re-review 2026-09-29

- Resolved the two PENDING IBA rows (nucleus, protein sumoylation) as ACCEPT: the PAINT node PTN000629675 is the whole Ubc9 clade and the zebrafish paralog sits inside it with an intact UBC core and catalytic Cys93 [file:DANRE/ube2ib/ube2ib-uniprot.txt "ACT_SITE 93 ... Glycyl thioester intermediate"].
- Replaced templated summaries/reasons on all rows. Deep-research quotes that paraphrased UniProt were dropped in favour of the primary zebrafish papers cited by UniProt, now cached: PMID:17035631 (Nowak & Hammerschmidt 2006) and PMID:11331779 (Vsx-1 nuclear import).
- SUMO E2 activity and protein sumoylation remain the core function: [PMID:17035631 "reduction of Ubc9 activity by expression of a dominant negative version causes widespread apoptosis, similar to the effect described in Ubc9 -deficient mice."]; zygotic knockdown reveals a requirement of [PMID:17035631 "Ubc9 for G2/M transition and/or progression through mitosis during vertebrate organogenesis."].
- Heart looping / embryonic heart tube elongation (IGI, PMID:28285006, abstract-only cache) and definitive hemopoiesis (IGI, PMID:25757417, full text) stay KEEP_AS_NON_CORE: the enzyme's work is SUMOylating Gata5 and C/ebpa; the morphogenetic and haematopoietic phenotypes are downstream [PMID:28285006 "in SUMOylation-deficient ubc9 mutants, the abnormal expression pattern displayed by the early markers of cardiac development (nkx2.5 and mef2cb) could be restored using a sumo-gata5 fusion, but not with a WT gata5."] [PMID:25757417 "Expression of the myeloid lineage marker lysozyme C and erythroid lineage marker hbae1 were drastically decreased in both SUMOs and Ubc9 morphants"]. ARBA IEAs for the same terms mirror these rows and get the same action.
- Nucleus: UniProt location is inferred (ECO:0000305); no zebrafish immunolocalisation is cached, so a localisation experiment is suggested. Paralog identity caveat: functional papers use ubc9.1/ubc9.2 naming; ZFIN's MO/genotype entities on the GOA rows tie them to ube2ib.
- Description rewritten as standalone biology; reference_review added to every PMID; validation: 0 errors.
