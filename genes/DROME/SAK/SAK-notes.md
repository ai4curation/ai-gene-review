# SAK (DROME) review notes

## Session 2026-10-26
- Fetched with `just fetch-gene DROME SAK`; UniProt O97143 (PLK4_DROME) confirmed. 31 GOA rows.
- No deep-research providers available; literature synthesis is in SAK-deep-research-manual.md.
- Additional PMIDs cached: 21987638 (key, full text), 25264260, 29263250, 17463247, 18555779, 19084407, 25517369.
- Interactor accessions resolved via UniProt REST: Q9VNE4 = asl, Q9VDE3 = slmb, FBgn0025388 = Alms1a (Q5BI31).

### Key decisions
- Core MF: protein serine/threonine kinase activity (IDA, PMID:21987638 in vitro kinase assays) [PMID:21987638 "Plk4 phosphorylates itself and purified bovine myelin basic protein (MBP)"].
  Physiological substrate Ana2 STAN motif [PMID:25264260 "Drosophila Plk4 phosphorylates four conserved serines in the STAN motif"].
- Core BP: centriole replication (multiple IMP). centrosome cycle rows -> MODIFY to centriole replication.
- regulation of centriole replication -> MODIFY to positive regulation (overexpression drives amplification; PMID:17463247).
- Autophosphorylation-driven self-destruction: regulation of protein stability / positive regulation of protein catabolic process kept as non-core; NEW protein autophosphorylation (IDA PMID:21987638). Here Sak itself does the work (phosphorylates its own degron), so it meets the participation bar.
- nucleus IBA (Polo family node) marked over-annotated: no Drosophila evidence of nuclear activity; Plk4 acts at centrioles.
- Male meiosis, syncytial division, sperm axoneme assembly are downstream consequences of centriole loss; meiosis marked over-annotated, the other two kept as non-core.
- protein binding (Asl, Slimb, Alms1a) kept as non-core; identical protein binding -> MODIFY to protein homodimerization activity (CPB/PB3 homodimers, PMID:23000383).
