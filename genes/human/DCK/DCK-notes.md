# DCK / PTHR10513 review notes

Reviewed human `DCK` (`UniProtKB:P27707`, `PANTHER:PTHR10513:SF19`) as the last
unreviewed human reviewed member of the compact PTHR10513 deoxyribonucleoside kinase
family.

## Scope

| human gene | UniProt | PANTHER SF | status |
| --- | --- | --- | --- |
| `DCK` | `P27707` | `PTHR10513:SF19` | new review |
| `TK2` | `O00142` | `PTHR10513:SF24` | existing review cross-checked |
| `DGUOK` | `Q16854` | `PTHR10513:SF8` | existing review cross-checked |
| `NDUFA10` | `O95299` | `PTHR10513:SF15` | existing review cross-checked |

`just fetch-gene human DCK` produced a real GOA file, not a header-only failed fetch:
42 lines including the header and 41 seeded annotation rows.

## Deep research

`just deep-research human DCK --provider perplexity-lite` was attempted after the
standard fetch. The wrapper reported that only `claude_code` was available for that
recipe in this runtime, so no provider-authored `DCK-deep-research-*.md` file was
created or fabricated. The review therefore used cached GOA, UniProt, PANTHER/PAINT,
Reactome and primary PMID records directly.

## PAINT and family calls

`interpro/panther/PTHR10513/PTHR10513-tree-check.txt`, generated from the cached
PANTHER 19.0 tree, places human `DCK` on leaf `PTN002471218`, below the vertebrate
DCK node `PTN002575111` and the broader DCK/DGUOK/DCK2 node `PTN002236991`. Human
`DGUOK` is in SF8 under the same `PTN002236991` branch, human `TK2` is in SF24 under
`PTN000828170`, and human `NDUFA10` is on the separate SF15 Complex-I branch under
`PTN000828201`.

The root `GO:0019136` deoxynucleoside kinase IBD is a sound broad family assertion for
the DCK/TK2/DGUOK kinase branches, and PAINT already blocks it from the NDUFA10 branch
with an IRD at `PTN000828201`. The DCK/DGUOK node `PTN002236991` correctly carries the
three DCK natural-substrate MFs that descend to human DCK. The `PTN000828170`
`GO:0004136` deoxyadenosine kinase IBD is correct for broad Drosophila dNK but should
be pruned from vertebrate TK2 at `PTN002575123`. The `GO:0005739` mitochondrion IBD at
`PTN002236975` should continue to cover TK2/DGUOK but should be blocked from the
vertebrate DCK SF19 branch at `PTN002575111`.

The existing `modules/mitochondrial_dntp_supply.yaml` module covers TK2 and DGUOK and
mentions DCK only as the cytosolic paralog that does not supply mitochondrial dNTPs.
DCK has no local production GO-CAM entry in `gocams/index.tsv`.

## Row decisions

The deoxyadenosine, deoxycytidine and deoxyguanosine kinase rows were accepted as the
core biochemical function of cytosolic/nuclear DCK. `GO:0043771` cytidine kinase
activity and its logical `GO:0009224` CMP biosynthetic-process row were kept as
non-core because purified DCK can phosphorylate cytidine and Reactome models CMP
formation, but the natural deoxyribonucleosides are the physiological emphasis.

`GO:0005737` cytoplasm, `GO:0006220` pyrimidine nucleotide metabolic process,
`GO:1901135` carbohydrate derivative metabolic process and `GO:1901293` nucleoside
phosphate biosynthetic process were marked `TOO_GENERAL` beside accepted, more
specific DCK terms. The PAINT `GO:0005739` mitochondrion row was marked
`MARK_AS_OVER_ANNOTATED` because it propagates the TK2/DGUOK mitochondrial branch to
cytosolic/nuclear DCK.

The two `GO:0005515` protein-binding rows from AP-MS interactome screens were removed
under the generic protein-binding policy. Both use DGUOK as the interactor, but DGUOK
is a mitochondrial-matrix kinase while DCK is cytosolic/nuclear; neither paper turns
the AP-MS edge into a specific DCK function.
