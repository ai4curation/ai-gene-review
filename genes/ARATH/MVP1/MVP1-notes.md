# MVP1 review notes

- Fetched with `just fetch-gene ARATH MVP1`; UniProt Q7XA74 (GeneID 841841, TAIR AT1G54030) confirmed; 18 GOA rows.
- Literature summary in MVP1-deep-research-manual.md (manual; no deep-research API).
- Full text read: PMID:23155454 (Nakano 2012), PMID:19880612 (Agee 2010). Abstract only: PMID:20626647, PMID:24330158, PMID:35147444.

## Decisions
- Lipase/esterase: experimentally absent [PMID:19880612 "MVP1 does not act as a lipase or esterase"]; NOT lipase IBA accepted; InterPro2GO hydrolase-on-ester-bonds IEA removed (pseudoenzyme over-propagation) with source defect.
- UniProt MUTAGEN G59S says "Restored lipase activity", but PMID:23155454 only introduced the catalytic residue and tested complementation ("regardless of whether it has enzymatic activity"); no activity assay is reported. Recorded as a CHECK source defect against UniProt.
- Chloroplast ISM (AtSubP): contradicted by signal peptide and experimental ER/vacuole localization; removed.
- Tonoplast IDA (Agee, transvacuolar strand GFP): Nakano shows lumen; no TM segment. Marked over-annotated.
- Added NEW plant-type vacuole lumen (IDA, PMID:23155454) beside the vacuole rows.
- Transport BP rows (ER-to-Golgi, intracellular protein transport) kept non-core: Nakano argues they are secondary to ER disorganization.
- No MF in core functions: activity unknown; PYK10-complex/TGG2 binding is physical association only.
- Did not add a NEW defense-response term from the alp4 powdery mildew phenotype (mutant phenotype only, likely indirect via PEN3 mistargeting).
