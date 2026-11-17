# metA notes (metAS, b4013, P07623)

No deep-research file; literature from UniProt references and Europe PMC search (2026-11-13).

- Succinyl-CoA specific, ping-pong via succinyl-cysteine [PMID:10572016 "This suggests the presence of an active site cysteine which forms a succinyl-cysteine intermediate during enzymatic turnover."]; UniProt "Cannot use acetyl-CoA (PubMed:10572016)."
- Catalytic Cys142, His235, Lys47 [PMID:17302437]; Cys-His-Glu triad and substrate-binding Arg/Lys [PMID:17442255].
- Feedback inhibition by methionine [PMID:35084172 "the enzyme is noncompetitively inhibited by methionine with a Ki value of 2.44 mM"]. Transcription from P1 repressed by methionine (UniProt INDUCTION, PMID:6094503).
- Thermolabile, aggregates above 44 C, limits growth at high temperature [PMID:12453224].
- MetA fold PTHR20919 / PTHR20919:SF0; NCBIfam TIGR01001 MetA_succinyl; HAMAP MF_00295. PAINT IBD PTN000467771 (taxon Bacteria) seeded only by P07623.

## UniRule defect (important for the module)
UniRule UR000083172 (HAMAP MF_00295), fetched from rest.uniprot.org/unirule/UR000083172.json on 2026-11-13: the case rule annotating "Homoserine O-succinyltransferase" (EC 2.3.1.46, gene metAS, succinyl reaction) carries GO:0004414, and the case annotating "Homoserine O-acetyltransferase" (EC 2.3.1.31, gene metAA) carries GO:0008899. The GO xrefs are swapped. UR000083175 (MF_00296, MetX) pairs them correctly. Consequence: P07623 gets a false GO:0004414 IEA (GO_REF:0000104). Recorded as a CONFIRMED source defect. Payload not retained.

## Curation decisions (2026-11-13)
- 11 GOA rows: GO:0004414 REMOVE; 8 ACCEPT (6 x GO:0008899, cytoplasm, GO:0071266 de novo Met biosynthesis); GO:0042803 KEEP_AS_NON_CORE; GO:0071265 TOO_GENERAL (child GO:0071266 accepted).
