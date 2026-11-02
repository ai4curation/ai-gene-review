# kap-1 (F08F8.3, WBGene00002182) notes

## Accession choice
- UniProt has two unreviewed entries for kap-1: H2KZP1 (F08F8.3a, 710 aa) and G5EEE6 (F08F8.3b, 713 aa). Q18930 is a different gene, aka-1 (D1022.7, an A-kinase anchor protein); "kap-1" is only a synonym there.
- G5EEE6 was chosen. It is the longer product, and it is the entry that carries the PANTHER IBA rows (PTN000401088) and the ComplexPortal NAS rows, which marks it as the gene-centric representative.
- Not imported, because these GOA rows are on H2KZP1 only: IMP/IGI intraciliary anterograde transport and IGI rows for GO:1902856/GO:1902857 (PMID:17420466, DYF-5 study), plus IDA non-motile cilium (PMID:17420466, PMID:22342749). They are consistent with this review.
- The module (modules/intraflagellar_transport.yaml) names KAP-1 without an accession. G5EEE6 is the recommended one.

## Provenance and process
- Deep research: falcon timed out and the perplexity-lite fallback is unavailable. No deep-research file was written.

## Key findings
- Heterotrimer [PMID:17000880 "the KLP-11, KAP-1, and KLP-20 subunits elute as a monodisperse heterotrimeric complex"].
- Structure [PMID:40707480 "The two motor tails fold together and are co-recognized by the central groove of KAP-1."]; interface mutants "disrupt the heterotrimeric kinesin-2 complex and impair kinesin-2-mediated intraflagellar transport".
- Binds only the heterodimer [PMID:20498083 "heterodimerization is necessary to bind KAP1, the in vivo link between motor and cargo"].
- Localization and IFT [PMID:10545497 "concentrate at the base of the transition zones"].
- Motor handover [PMID:26523365 "kinesin-II transports IFT trains through the ciliary base and transition zone to a 'handover zone' on the proximal axoneme"].

## Curation decisions
- 16 GOA rows: 15 ACCEPT, 1 REMOVE (nucleus, ARBA IEA).
- Core MF: GO:0019894 kinesin binding, with contributes_to GO:0003777 microtubule motor activity.
