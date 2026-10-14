# MKK4 curation notes

Session 2026-10-06, added for the stomatal_lineage_development module (where MKK4/MKK5 are representative members of the redundant MAPKK step). Fetched by accession (O80397, alias MKK4); UniProt entry verified (M2K4_ARATH, At1g51660). Falcon deep research not attempted (provider returned HTTP 402 for all other genes this session).

## Key findings
- MKK4/MKK5 act downstream of YODA and upstream of MPK3/MPK6 in stomatal development [PMID:17259259 "We further establish that the MKK4/MKK5-MPK3/MPK6 module is downstream of YODA, a MAPKKK."]; loss gives clustered stomata, activation abolishes stomatal fate [PMID:17259259 "Loss of function of MKK4/MKK5 or MPK3/MPK6 disrupts the coordinated cell fate specification of stomata versus pavement cells, resulting in the formation of clustered stomata."].
- YDA phosphorylates MKK4 [PMID:22307275 "BIN2 phosphorylates YDA to inhibit YDA phosphorylation of its substrate MKK4"]; MAPKKK5 phosphorylates MKK4/MKK5 activation loops [PMID:27679653].
- Immune MAPK cascade downstream of FLS2 [PMID:11875555 "Here we identify a complete plant MAP kinase cascade (MEKK1, MKK4/MKK5 and MPK3/MPK6)..."].
- Inflorescence architecture downstream of ERECTA [PMID:23263767]; floral organ abscission downstream of HAE/HSL2 [PMID:18809915].
- Non-canonical chloroplast stromal import of MKK4 [PMID:19516975] - kept non-core.

## Curation decisions
- Core MF: MAP kinase kinase activity (GO:0004708). IDA from PMID:9878570 accepted deferring to curator (abstract only, centred on MKK2/MEK1).
- NEW: negative regulation of stomatal complex development (IGI, PMID:17259259) - MKK4 performs the phosphorylation relay step, so it does part of the work.
- Protein binding: MPK3/MPK6 rows MODIFIED to MAP kinase binding; MAPKKK5 row to MAPKKK binding; BRX, MYB73, KNAT1, TIFY8, ILK4 rows REMOVED.
