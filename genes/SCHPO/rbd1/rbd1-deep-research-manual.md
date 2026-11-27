# rbd1 deep research

## Retrieval

- `just fetch-gene SCHPO rbd1` could not resolve the current PomBase symbol, so
  the review was seeded with `just fetch-gene SCHPO O14364 --alias rbd1`.
- `just fetch-gene-pmids SCHPO rbd1` cached the two PMIDs cited by the current
  PomBase GO annotations.
- `just mod-description-deep-research SCHPO rbd1` skipped because this
  repository has no configured MOD-description provider for `SCHPO`.
- `just paint-losses SCHPO rbd1` reported no IRD or IKR loss on the rbd1
  lineage.
- Automated Falcon deep research and the Perplexity fallback were unavailable,
  so this manual synthesis uses the cached S. pombe GO literature, the UniProt
  record, the GO-CAM activity, and the cached budding-yeast PCP1/RBD1 papers
  that ground the orthologous mitochondrial rhomboid function.

## Synthesis

`rbd1` is PomBase `SPBC13E7.11` and UniProt `O14364`, a 298 aa protein with
eight predicted transmembrane helices and the Peptidase S54 rhomboid domain
`IPR022764`. UniProt also places the entry in PANTHER `PTHR43731:SF35`,
Rhomboid protease.

The direct S. pombe publication is Leroy et al. 2010 (`PMID:20621843`). The
cached abstract reports that mitochondrial OPA1/Mgm1/Msp1 dynamin processing
was tested in S. pombe, that Msp1 is processed by a rhomboid and an
m-AAA-family protease, and that the rhomboid is involved in generation of short
Msp1. PomBase's EXP annotation to `GO:0004252` names rbd1 as that rhomboid
protease.

The S. cerevisiae ortholog PCP1/RBD1 provides the main orthology support for the
inner-membrane localization and additional conserved substrate-processing
evidence. McQuibban et al. 2003 (`PMID:12774122`) localized budding-yeast Rbd1p
to the inner mitochondrial membrane, identified Ccp1p and Mgm1p as Rbd1p
substrates, and reported that human PARL can rescue the yeast mutant. Sesaki et
al. 2003 (`PMID:12901865`) and Herlan et al. 2003 (`PMID:12707284`)
independently tied Pcp1 to Mgm1 processing, while Esser et al. 2002
(`PMID:12417197`) tied Pcp1 to the second processing step of Ccp1 maturation.

## GO-CAM consistency

GO-CAM `69729a3800007453` represents `SPBC13E7.11/rbd1` as `GO:0004252`
serine-type endopeptidase activity occurring in `GO:0005743` mitochondrial
inner membrane and contributing to `GO:0034982` mitochondrial protein
processing with `msp1` as the input. The gene review agrees with that
representation; no final GO-CAM consistency note is needed for this rbd1
activity.

## Annotation review decisions

- Accept `GO:0004252` from PomBase EXP, PAINT IBA, and the InterPro/ARBA IEA
  row as the core molecular function.
- Accept root `GO:0005739` mitochondrion from Matsuyama et al. 2006 under the
  root-organelle policy and accept `GO:0005743` mitochondrial inner membrane
  from PAINT and PomBase ISO.
- Mark `GO:0016020` membrane as `TOO_GENERAL` because rbd1 is reviewed more
  precisely at the mitochondrial inner membrane.
- Modify `GO:0016485` protein processing to `GO:0034982` mitochondrial protein
  processing, preserving the PAINT proteolytic-processing claim while
  identifying the mitochondrial context, and mark `GO:0051604` protein
  maturation as `TOO_GENERAL` because the more precise PomBase process row
  already captures rbd1's Msp1-processing role.
