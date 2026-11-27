# glnL (NtrB / NRII), E. coli K-12, P0AFB5 — curation notes

Provider deep research was NOT run for this gene (not available in this session); these notes are based on the cached
publications in `publications/` and the UniProt record `glnL-uniprot.txt`.

## Function
- Sensor histidine kinase of the NtrB/NtrC two-component system: [PMID:2848245 "the reaction of ATP with NRII results in the reversible transfer of the gamma-phosphate of ATP to a histidine residue of NRII. In turn, NRII-phosphate transfers its phosphate reversibly to an aspartic residue of NRI"]. His139 is the phosphohistidine (UniProt MOD_RES 139).
- Phosphatase toward NtrC-P, stimulated by PII (GlnB): [PMID:2874557 "In the presence of PII, the product of glnB, NRII catalyzes the removal of the phosphate from NRI-phosphate."]
- Reciprocal regulation of kinase and phosphatase by PII and 2-ketoglutarate: [PMID:10074086 "At low 2-ketoglutarate concentrations, PII trimers complexed with a single molecule of 2-ketoglutarate interact with NRII to inhibit its kinase activity and activate its phosphatase activity."]
- Mechanistic caveat: [PMID:10074086 "It is not known whether these transmitters are actually phosphatases or act as activators of the autophosphatase activity of the phosphorylated receiver."]
- Required for glnAp2 transcription in vitro: [PMID:3536843 "In vitro transcription of the nitrogen-regulated promoter glnAp2 by purified components of Escherichia coli required NRII or NRII2302 when the template DNA was linear."]
- Y2H partners GlnB, GlnK, AspA: [PMID:12838411 "Three different genes, encoding GlnB, GlnK and AspA, respectively, were found among 64 positive clones identified from E. coli Sau3AI Y2H libraries using the nitrogen regulator NtrB as bait."]

## Curation decisions
- GO:0004673 (EXP/IDA/IEA), GO:0016772 and GO:0016774 -> MODIFY to GO:0000155 phosphorelay sensor kinase activity.
- GO:0007165 (IBA/IEA) -> MODIFY to GO:0000160.
- GO:0005515 rows -> REMOVE per protein-binding policy (interactions with PII are real; captured by kinase/phosphatase terms).
- GO:0042802 Y2H self-interaction -> MODIFY to GO:0042803; GO:0042803 IDA (abstract-only paper) kept as non-core, deferring to curator.
- GO:0006355 (PAS IEA) kept as non-core: NtrB regulates transcription only indirectly via NtrC.
- GO:0006796 (ARBA) marked over-annotated.
