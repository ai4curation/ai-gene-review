# FCY1 (Q12178, YPR062W) notes

Module: `pyrimidine_salvage` (optional cytosine deamination step), role = cytosine deaminase (EC 3.5.4.1). YeastCyc: CYTDEAM-RXN in YEAST-RNT-SALV.

## Evidence journal
- Activity and phenotype [PMID:9000374 "Disruption of FCY1 resulted in high resistance to 5-fluorocytosine (10(-2) M) and in total loss of cytosine deaminase activity"]
- Growth on cytosine [PMID:9000374 "restored sensitivity to 5-fluorocytosine and allowed growth on cytosine, as a source of pyrimidine, or ammonium"]
- Limiting for cytidine use [PMID:10501935 "a block in cytosine deaminase (Fcy1p), but not in cytidine deaminase (Cdd1p), constitutes a limiting step in cytidine utilisation as a UMP precursor"]
- Mechanism (computational) [PMID:15535715 "a zinc metalloenzyme of significant biomedical interest"]; Zn, homodimer, many PDB structures [UniProt:Q12178]
- Yeast DRAP deaminase is Rib2 [UniProt RIB2: "Diaminohydroxyphosphoribosylaminopyrimidine deaminase"].

## Decisions
- IBA GO:0008835 DRAP deaminase (RibD-only donor, deep CDA-superfamily node) REMOVE.
- IDA from PMID:15535715 (ONIOM computational study) ACCEPT on content but evidence code questionable.
- Cytidine metabolic process rows KEEP_AS_NON_CORE (acts on cytosine released from cytidine).
- GO-CAM YEAST-RNT-SALV types FCY1 with obsolete GO:0102480 (5-fluorocytosine deaminase), so no RCA cytosine deaminase row reaches GOA.
