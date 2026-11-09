# GJB3 source and assay boundaries

<a id="human-channel-assays"></a>

## Human channel assays — PMID:16549784

Human Cx31 in HeLa/Neuro2a cells supported coupling, dye passage and gating. Heterotypic pairing is not mixed-connexon assembly; Cx45 species labeling is inconsistent. Reporters are engineered. Main text/captions, not images/supplement, were read. ([PMID:16549784](https://pubmed.ncbi.nlm.nih.gov/16549784/)).

## Interaction evidence

[HuRI](https://pubmed.ncbi.nlm.nih.gov/32296183/) provides 36 retained records for 12 pairs. These are three method-labelled representations per pair, not 36 independent physiological results. The target is O75712 / ORF2665 / ENST00000373362.3 / ENSP00000362460.3; complete historical clone sequence identity is unverified. The original PSI-MI file SHA256 is `d6e8185519d18ce18cfa66f5eab66ecb1e711113f0b62810e0a145dd33a9ee12`.

| Raw index | Incoming partner | Original source product | Disposition |
|---|---|---|---|
| 2 | TUSC5 (A5PKU2) | Q8IXB3 / ORF72045 | REMOVE; source CHECK |
| 3 | LAT (O43561-2) | O43561-2 | REMOVE |
| 4 | MFSD11 (O43934) | O43934-1 | REMOVE |
| 5 | COMT (P21964) | P21964-1 | REMOVE |
| 6 | IGFBP5 (P24593) | P24593 | REMOVE |
| 7 | TMEM97 (Q5BJF2) | Q5BJF2 | REMOVE |
| 8 | TMUB2 (Q71RG4) | Q71RG4-2 | REMOVE |
| 9 | LHFPL5 (Q8TAF8) | Q8TAF8 | REMOVE |
| 10 | BTN2A2 (Q8WVV5) | Q8WVV5-1 | REMOVE |
| 11 | GIMAP5 (Q96F15) | Q96F15-1 | REMOVE |
| 12 | RPRM (Q9NS64) | Q9NS64 | REMOVE |
| 13 | SERP1 (Q9Y6X1) | Q9Y6X1 | REMOVE |
| 14 | PCYOX1 (Q9UHG3) | Q9UHG3 | REMOVE |

A5PKU2 and Q8IXB3 are both 177 residues but differ at positions 15, 20, 57 and 170. The source clone record does not establish complete equivalence. Other partner functions were read from official UniProt records separately from the pair evidence; generic removals concern functional informativeness and preserve the positive observations.

[BioPlex](https://pubmed.ncbi.nlm.nih.gov/33961781/) line 34725 links GJB3/O75712 and PCYOX1/Q9UHG3 with pInt 0.954099960347321. The 293T AP-MS table supports association, not necessarily binary contact; no target-specific HCT116 replication is asserted. Original TSV SHA256: `5a98def087fc77c7bf07aac79e2553fd64ea1a27a7d0c4617870476f3f120833`.

## Ancestry and donor localization

The actual [PTHR11984 family](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR11984) contains the exact 270-residue human AN801/PTN002485542 sequence. The three incoming IBA terms descend from AN0/PTN008334405; literal IBD donor sets match and no target IRD/IKR loss was found. The 948-node tree, 497 leaves and 2873-column alignment were inspected.

[PMID:7889986](https://pubmed.ncbi.nlm.nih.gov/7889986/) describes mouse Cx31 DNA in HeLa hosts and mouse-cell/tissue immunolocalization. [PMID:14595769](https://pubmed.ncbi.nlm.nih.gov/14595769/) describes mouse cochlear Cx31; its separate Cx26/Cx30 association does not establish a Cx31 heteromer. Only authentic abstracts were read; full donor articles remain uninspected. Current mouse P28231 IDA rows and the human transfer contexts are preserved.

## Localization and pathway context

[Human Protein Atlas GJB3](https://www.proteinatlas.org/ENSG00000188910-GJB3/subcellular) metadata lists A431 cell junctions and HaCaT vesicles/cell junctions for HPA074472. The vesicle dictionary denotes cytoplasmic dots without a specific organelle identity. No image pixels, ultrastructure or plasma-membrane-to-cytoplasm ontology ancestry is claimed.

[Reactome R-HSA-190861](https://reactome.org/content/detail/R-HSA-190861) reaches O75712 residues 1–270 through the translated ER product chain 190682→190703→190625→53214. GJB3 is the synthesis product. [R-HSA-9725554](https://reactome.org/content/detail/R-HSA-9725554) reaches the target through 9727355→9727357→9839597→9839595→53214, a cell-marker chain, not a demonstrated differentiation-regulatory role.

## Access limits

For [PMID:9704026](https://pubmed.ncbi.nlm.nih.gov/9704026/), authentic metadata and abstract were read but full original access was unsuccessful. HEK denotes E6/E7 human keratinocytes in that paper; transcript lengths do not establish alternative protein products. Existing NAS assertions are evaluated with independent support without alleging absent experiments.
## Source excerpts and target records

These are excerpts of the named original sources, not independent experiments performed for this review. Source locations and hashes are in the evidence manifest.

### Human Protein Atlas

The retained [GJB3 subcellular table](https://www.proteinatlas.org/ENSG00000188910-GJB3/subcellular) gives antibody, cell line, RNA nTPM and localization in that order:

```text
HPA074472
HaCaT
94.1
Vesicles
Cell Junctions

HPA074472
A-431
87.9
Cell Junctions
```

The numbers are RNA expression values, not localization confidence or channel activity. The [vesicle dictionary](https://www.proteinatlas.org/humanproteome/subcellular/vesicles) describes punctate cytoplasmic staining without a demonstrated organelle identity. No image pixels were inspected.

### UniProt subunit account

[O75712, SUBUNIT](https://www.uniprot.org/uniprotkb/O75712/entry), with the original ECO:0000250 attribution:

> A connexon is composed of a hexamer of connexins.

This is a curated inference by similarity, not a new human stoichiometry measurement.

### BioPlex target row

The [original 293T network](https://bioplex.hms.harvard.edu/data/BioPlex_293T_Network_10K_Dec_2019.tsv), line 34725 including the header as line 1, contains:

```tsv
"GeneA"	"GeneB"	"UniprotA"	"UniprotB"	"SymbolA"	"SymbolB"	"pW"	"pNI"	"pInt"
"2707"	"51449"	"O75712"	"Q9UHG3"	"GJB3"	"PCYOX1"	5.39910554694665e-6	0.0458946405471317	0.954099960347321
```

This is the measured association used for the PCYOX1 row; it does not establish a direct interface or physiological cargo relationship.
