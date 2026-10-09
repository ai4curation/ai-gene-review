# MKK5 curation notes

Session 2026-10-06, added for the stomatal_lineage_development module (where MKK4/MKK5 are representative members of the redundant MAPKK step). Fetched by accession (Q8RXG3, alias MKK5); UniProt entry verified (M2K5_ARATH, At3g21220). Falcon deep research not attempted (provider returned HTTP 402 for all other genes this session).

## Key findings
- MKK4/MKK5 act downstream of YODA and upstream of MPK3/MPK6 in stomatal development [PMID:17259259 "We further establish that the MKK4/MKK5-MPK3/MPK6 module is downstream of YODA, a MAPKKK."]; loss gives clustered stomata, activation abolishes stomatal fate [PMID:17259259 "Loss of function of MKK4/MKK5 or MPK3/MPK6 disrupts the coordinated cell fate specification of stomata versus pavement cells, resulting in the formation of clustered stomata."].
- YDA phosphorylates MKK4 [PMID:22307275 "BIN2 phosphorylates YDA to inhibit YDA phosphorylation of its substrate MKK4"]; MAPKKK5 phosphorylates MKK4/MKK5 activation loops [PMID:27679653].
- Immune MAPK cascade downstream of FLS2 [PMID:11875555 "Here we identify a complete plant MAP kinase cascade (MEKK1, MKK4/MKK5 and MPK3/MPK6)..."].
- Inflorescence architecture downstream of ERECTA [PMID:23263767]; floral organ abscission downstream of HAE/HSL2 [PMID:18809915].
- AIK1-MKK5-MPK6 ABA module [PMID:27913741 "Bimolecular fluorescence complementation analysis showed that MPK3, MPK6, and AIK1 interact with MKK5."]; MEK5(DD) induces ethylene and HR-like death [PMID:18268539].

## Curation decisions
- Core MF: MAP kinase kinase activity (GO:0004708, IEA accepted; EXP Ser/Tyr kinase rows accepted).
- NEW: negative regulation of stomatal complex development (IGI, PMID:17259259).
- Mitochondrion ISM MARK_AS_OVER_ANNOTATED; cell division IMP MARK_AS_OVER_ANNOTATED (regulatory, not participatory); stress granule kept non-core.
- Protein binding: MPK3/MPK6 rows MODIFIED to MAP kinase binding; AIK1 and MAPKKK5 to MAPKKK binding; BASL, SLOMO, ILK4 REMOVED.
