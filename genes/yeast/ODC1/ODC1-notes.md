# ODC1 (YPL134C, Q03028) notes

Module context: `lysine_biosynthesis_aminoadipate`, order 5 (optional) oxoadipate_mitochondrial_export_step, family PANTHER:PTHR46356:SF1 (ODC1, ODC2), MF GO:0005310, BP GO:1990551, mitochondrial inner membrane. Not in the YeastPathways summary (YeastCyc LYSINE-AMINOAD-PWY does not include a transport step); no RCA annotations. No S. cerevisiae GO-CAM.

## Evidence
- [PMID:11013234 "We have localized two hitherto unidentified family members, Odc1p and Odc2p, to the inner membranes of mitochondria."]
- [PMID:11013234 "we have shown in reconstituted liposomes that they transport the oxodicarboxylates 2-oxoadipate and 2-oxoglutarate by a strict counter exchange mechanism"]
- [PMID:11013234 "Intraliposomal adipate and glutarate and to a lesser extent malate and citrate supported [14C]oxoglutarate uptake."]
- Role: [PMID:11013234 "The main physiological roles of Odc1p and Odc2p are probably to supply 2-oxoadipate and 2-oxoglutarate from the mitochondrial matrix to the cytosol where they are used in the biosynthesis of lysine and glutamate, respectively, and in lysine catabolism."]
- Paralog ODC2, 61% identity; ODC1 is the more abundant, glucose-repressed isoform [PMID:11013234].

## Issues
- IBA aspartate/glutamate transporter, aspartate/glutamate transport and malate-aspartate shuttle come from a PANTHER node (PTN000640306) seeded by AGC/GC carriers (SLC25A12/13, yeast AGC1). ODCs are a different subfamily; REMOVE (MF/transport) and MARK_AS_OVER_ANNOTATED (shuttle).
- PomBase GO-CAM 67c10cc400005826 models S. pombe odc1 (SPAC328.09) with oxoglutarate:malate antiporter and aspartate:glutamate, proton antiporter in the malate-aspartate shuttle, MF without experimental evidence (location ISS from ODC2 Q99297). This conflicts with the S. cerevisiae ODC substrate data.
- InterPro IPR002113 (ADP/ATP carrier) mappings -> ATP:ADP antiporter and ADP/ATP transport: wrong, REMOVE.
- PMID:9178508 (phylogenetic classification) used for IDA mitochondrion: content correct, evidence code questionable.
- Lysine biosynthesis BP is not annotated in GOA; the module includes ODC as an optional transport step. Not proposing NEW lysine biosynthesis BP (carrier exports an intermediate; no published lysine auxotrophy of odc mutants in the cached literature).
