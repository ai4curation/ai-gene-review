# rbd1 notes

## 2026-11-25

Reviewed rbd1 for GO-CAM `69729a3800007453` after seeding the review with
`just fetch-gene SCHPO O14364 --alias rbd1`; the direct `rbd1` symbol lookup did
not resolve in the local UniProt lookup, but the model's `SPBC13E7.11`
enabled_by entity maps to UniProt `O14364`.

The direct S. pombe evidence is the PomBase-curated Msp1-processing paper
(`PMID:20621843`). Its cached abstract reports rhomboid-dependent Msp1
processing in S. pombe and PomBase's EXP annotation records rbd1 as that
rhomboid. The same protein is a multi-pass Peptidase S54 rhomboid by UniProt,
so the direct, IBA, and InterPro/ARBA serine endopeptidase rows all describe
the same core activity.

The two inner-membrane rows are orthology/PAINT transfers, not direct S. pombe
localization, but they are well supported. Budding-yeast Pcp1/Rbd1 was
localized to the inner mitochondrial membrane in the abstract cached for
McQuibban et al. 2003, and the fission-yeast protein is a multi-pass Rhomboid
protease in the same mitochondrial processing context. The root mitochondrion
HDA row from the fission-yeast ORFeome localization screen is broad but kept
under the root-organelle policy.

GO-CAM `69729a3800007453` uses rbd1 as the inner-membrane serine-type
endopeptidase in mitochondrial Msp1 processing. That agrees with the finished
gene review, so there is no rbd1-specific disagreement to carry into the final
GO-CAM notes PR.
