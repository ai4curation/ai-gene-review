# SERK1 review notes (ARATH, Q94AG2)

- fetch-gene resolved Q94AG2 (SERK1_ARATH, At1g71830, GeneID 843513) as requested; 66 GOA rows.
- No deep-research provider available; literature synthesis in SERK1-deep-research-manual.md.
- Key full texts read: PMID:22253607 (BR genetics), PMID:20230490 (nev suppression, Golgi),
  PMID:27058169 (HAESA-IDA-SERK1), PMID:27920157 (EMS1), PMID:26320950 (stomata), PMID:16284306,
  PMID:21693696, PMID:28887381 (no SERK1 discussed in main text).
- Abstract-only: 11397085, 11509554, 11706164, 15592873, 16231101, 16284305, 16473966, 16621602,
  17644812, 17693538, 18667726, 19616764, 23929946, 26308901, 27229311. PMC129253 (11706164) has no
  full text via PubMed MCP either.
- Decisions:
  - Core MF GO:0004675; generic kinase IEA rows MODIFY to it.
  - Golgi organization IGI (20230490): suppressor genetics only; serk1 alone has normal Golgi
    ["As in wild-type, only flat stacks of Golgi cisternae were present in serk1 cells"]; marked
    over-annotated, flagged upstream.
  - embryo development (11706164 IMP): abstract reports overexpression in culture only; UNDECIDED.
  - Chloroplast ISM removed (signal peptide, type I PM receptor); mitochondrion HDA marked
    over-annotated (as for SERK4), flagged upstream.
  - protein-containing complex MODIFY to GO:0043235 signaling receptor complex (BN-PAGE BRI1
    complexes).
  - No NEW terms: HAESA/EMS1/BRI1 co-receptor roles already captured by existing rows.
