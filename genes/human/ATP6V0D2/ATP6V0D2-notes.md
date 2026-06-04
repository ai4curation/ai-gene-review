# ATP6V0D2 review notes

## Core function

ATP6V0D2 encodes the d2 isoform of the V-ATPase V0 d subunit. The core function
is as a structural V0-sector component that contributes to the assembled
V-ATPase rotary proton pump, not as an independently catalytic ATPase. Smith et
al. show that the mammalian V0 d subunit has d1 and d2 forms and that d2 is
predominantly expressed in kidney and osteoclast [PMID:18752060 "d2 is predominantly expressed at the cell surface in kidney and osteoclast"].
The same paper supports a central-stalk/rotary mechanism role because the human
d subunits pull down V1 D and F subunits and the authors conclude that the d
subunit is centrally located in the pump [PMID:18752060 "the d subunit in man forms part of the pump's central stalk"].

The direct tissue-localization evidence supports specialized plasma membrane
V-ATPases in kidney intercalated cells and osteoclasts. Smith et al. report
human collecting-duct intercalated-cell staining that co-localized with the a4
subunit [PMID:15800125 "high-intensity d2 staining was observed only in intercalated cells of the collecting duct in fresh-frozen human kidney"] and bone
osteoclast co-localization with a3 [PMID:15800125 "In human bone, d2 co-localized with the a3 subunit in osteoclasts"].

## PN projection

Falcon deep research already existed as
`genes/human/ATP6V0D2/ATP6V0D2-deep-research-falcon.md`, so this was handled as
a PN-context re-review rather than a new deep-research run.

The PN projection has two ATP6V0D2 candidate additions from
`projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv`:
`GO:0007042 lysosomal lumen acidification` and `GO:0046610 lysosomal proton-transporting V-type ATPase, V0 domain`.
I treated both as conservative `action: NEW` recommendations. `GO:0007042` is
a specific child/refinement of the existing GOA `GO:0007035 vacuolar
acidification` and is supported by the ATP6V0D2-specific Autophagy abstract,
which states that ATP6V0D2 promoted autolysosome degradation by increasing
lysosomal acidification/activity [PMID:39477683 "ATP6V0D2 promoted autolysosome degradation by increasing the acidification and activity of lysosomes"].

`GO:0046610` is a compositional PN refinement, not a single direct experiment:
ATP6V0D2 is already in GOA as V0 domain, V-ATPase complex, and lysosomal
membrane, and the PN mapping
`Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component`
targets `GO:0046610` [file:projects/PROTEOSTASIS/mappings/autophagy_lysosome_pathway.yaml].
Because this depends on combining existing GOA/Reactome context with V0-subunit
identity, I recorded it as a conservative proposed annotation and added an expert
question about whether direct d2-specific lysosomal V0-domain evidence should be
required.

## Conservative annotation decisions

- Kept `GO:0007035 vacuolar acidification`, V-ATPase complex, V0 domain, and
  plasma membrane V-ATPase complex as core.
- Added PN-projected `GO:0007042` and `GO:0046610` as `NEW` recommendations.
- Moved broad `GO:0007034 vacuolar transport` to non-core because acidification
  is the cleaner core process.
- Kept macroautophagy regulation as non-core. PMID:39477683 supports a real
  late-autophagy/fusion role, but the original GOA citation PMID:22982048 is not
  ATP6V0D2-specific and instead addresses lipofuscin/autophagy generally
  [PMID:22982048 "macroautophagy is responsible for the uptake of lipofuscin into the lysosomes"].
- Kept phagocytic vesicle membrane and endosome membrane localizations as
  non-core Reactome/automated contexts rather than ATP6V0D2-defining locations.
- Removed generic `GO:0005515 protein binding` annotations because they are less
  informative than V-ATPase complex membership and specific mechanistic process
  annotations.

## Description cleanup note

The YAML description was kept project-independent. PN-specific rationale and
curation commentary are recorded here and in individual annotation review
reasons, not in the top-level biological summary.
