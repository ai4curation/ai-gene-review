# ManZ (EIID-Man) - Research Notes

## Summary

ManZ (P69805) is the EIID component of the mannose-specific PTS in E. coli K12. It is encoded by the manXYZ operon (b1819).

## Key findings

### Membrane topology and structure
- Integral inner membrane protein with multiple transmembrane helices [PMID:8774730, PMID:15919996]
- Forms the translocation channel together with ManY (EIIC) [PMID:2951378 "Both are integral membrane proteins and most likely form the transmembrane channel"]
- ManY/ManZ heterodimer assembles as homotrimer of protomers [PMID:31209249 "Structure of the mannose transporter"]
- Cryo-EM structures available: 3.52 A (PDB: 6K1H) and 2.28 A (PDB: 7DYR)
- ManZ is moderately hydrophobic (31 kDa) [PMID:2951378]

### Function
- EIID domain contains part of the substrate-binding site [UniProt, PROSITE PRU00431]
- Together with ManY, forms the PTS translocation channel
- All three subunits (ManX, ManY, ManZ) required for sugar transport and phosphorylation [PMID:2951378]
- ManY and ManZ alone sufficient for phage lambda DNA penetration [PMID:2951378]

### Substrate specificity
- Primary: mannose
- Secondary: glucose (2-deoxyglucose), fructose, N-acetylglucosamine [PMID:2999119, PMID:6252281]

### Regulation
- Same operon regulation as ManX and ManY (cAMP-CRP positive, Mlc negative, NagC weak negative)

## Review decisions
- All plasma membrane annotations ACCEPTED (multiple IDA evidence)
- PTS and mannose transport annotations ACCEPTED as core
- Secondary substrates (glucose, fructose, GlcNAc) kept as non-core
- Added NEW annotation: GO:1902495 (transmembrane transporter complex) from ComplexPortal
- Core MF: GO:0022870 (mannose PTS transporter activity)
