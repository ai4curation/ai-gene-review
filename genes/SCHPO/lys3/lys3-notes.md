# lys3 notes

## 2026-10-24

Reviewed S. pombe `lys3` in the `PTHR11133` saccharopine dehydrogenase family.
The PAINT split is clean: `PANTHER:PTN000875292` carries `GO:0009085
L-lysine biosynthetic process` on the NAD(+), L-lysine-forming `LYS1`/`lys3`
branch, while `PANTHER:PTN000875327` separately carries the same process on the
reciprocal NADP(+), L-glutamate-forming `LYS9`/`lys9` branch. `Q09694` is in
`PTHR11133:SF23`, so the `PTN000875292` IBA is an exact transfer.

The broad `GO:0004753 saccharopine dehydrogenase activity` IBA comes from the
eukaryotic `PANTHER:PTN000123605` node. That ancestor supports the parent
activity for the whole saccharopine dehydrogenase family, but it is too generic
for S. pombe `lys3`, which already carries the exact NAD(+), L-lysine-forming
`GO:0004754` term from InterPro/Rhea/EC and from S. cerevisiae LYS1.

The cytoplasm/cytosol rows should be kept. Unlike S. cerevisiae Lys1, there is
no evidence that S. pombe Lys3 is peroxisomal. The ORFeome row directly
supports broad cytoplasm, while PomBase infers `GO:0005829 cytosol` from the
accepted `GO:0004754` activity and exports the same placement in its
L-lysine-biosynthesis GO-CAM.

Cached PMIDs for `lys3` are abstract-only. `PMID:3142867` directly places the
classical `lys3-37` auxotroph at the saccharopine dehydrogenase step, while
`PMID:17622533` only reports a later lys3 auxotroph marker. The 2006 ORFeome
localization paper supports the source of the PomBase `GO:0005737 cytoplasm`
HDA row, but the precise cytosol placement comes from PomBase curation and the
GO-CAM carries that same curator inference rather than an independent
localization assay.

Newer-paper search: searched for S. pombe `lys3`, `SPAC227.18`, and
saccharopine dehydrogenase. Newer hits were PomBase/BioGRID/clone or reagent
pages plus pathway and metabolomics background; no paper changed the core lys3
activity, biological-process, or cytosol decisions.
