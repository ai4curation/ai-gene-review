# ADK2 (AKY3/PAK3, YER170W, P26364) notes

- AK3-type GTP:AMP phosphotransferase; does NOT use ATP [PMID:8537371 "The encoded protein exhibited GTP:AMP and ITP:AMP phosphotransferase activities but did not accept ATP as phosphate donor"]; [UniProt:P26364 "Belongs to the adenylate kinase family. AK3 subfamily."].
- Mitochondrial matrix [PMID:8537371 "was located exclusively in the mitochondrial matrix"].
- Short (PAK3, lab strains) vs long (AKY3) C-terminal forms; both active at 30C [PMID:15753074 "both short and long forms of Adk2p are enzymatically active"].
- Null has no phenotype [PMID:8537371 "yeast mitochondria can completely dispense with GTP:AMP phosphotransferase activity"].
- Consequence for GO: all ATP:AMP "AMP kinase activity" rows (IBA PTN000599576, InterPro IEA, 6 YeastPathways RCA) are wrong -> REMOVE. YeastCyc attaches ADK2 to the cytosolic AMP + ATP reaction alongside ADK1 (paralog over-assignment), also generating wrong cytosol RCA rows and de novo purine BP rows.
- Inner membrane IDA (PMID:15753074, PMID:8537371) conflicts with matrix description in abstracts; kept non-core.
