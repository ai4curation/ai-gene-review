# BCO2 notes

Perplexity deep research could not run in this checkout because the provider is unavailable in
the retained runtime. This review therefore uses the local UniProt, QuickGO, PAINT, Reactome and
cached publication evidence directly.

## Core biology

BCO2 is the asymmetric, mitochondrial member of the animal carotenoid oxygenases. The first BCO2
paper cloned a mouse enzyme that cleaves beta-carotene at the 9',10' double bond and also cloned
human and zebrafish cDNAs [PMID:11278918]. The cached abstract is not enough to verify a human
protein assay in that paper, so direct human beta-carotene cleavage is instead pinned to
PMID:21302131, which cloned human beta-carotene-9',10'-oxygenase, expressed it in *E. coli*, and
measured beta-apo-10'-carotenal production from beta-carotene.

PMID:21106934 supplies the mitochondrial and protective physiology evidence: BCDO2 is described
as a mitochondrial carotenoid oxygenase with broad substrate specificity, BCDO2-deficient mouse
tissues accumulated carotenoids, hepatic mitochondria had reduced ADP-dependent respiration, and
carotenoid treatment depolarized mitochondria and induced ROS in HepG2 cells.

## Annotation decisions

BCO2 keeps the eccentric 9,10-carotenoid-cleaving activity and carotene/xanthophyll catabolic
process rows. The generic carotenoid dioxygenase row is also true for BCO2, but the inherited
`GO:0003834` 15,15'-dioxygenase IBA is wrong for the BCO2 paralog and should be pruned at the
vertebrate BCO2 node. The `retinal metabolic process` IBA from the BCO1/RPE65/BCO2 ancestor is
left `UNDECIDED` because mouse Bco2 seeds the PAINT assertion and PMID:24106281 supports a minor,
BCO1-dependent route from BCO2-produced apocarotenoids into retinoids. The early NAS
retinoic-acid/retinal rows still overstate the speculative route in PMID:11278918 and are marked
`MARK_AS_OVER_ANNOTATED` rather than `REMOVE`.

The mitochondrial root term is accepted under the root-organelle policy. The Reactome
mitochondrial-matrix TAS row is left `UNDECIDED`: the cached event text supports BCO2 in the
mitochondrion and models the beta-carotene eccentric-cleavage reaction, but it does not state why
the reaction is in the matrix rather than another mitochondrial subcompartment.
