# SGMS1 primary evidence checks, 2026-09-21

All 41 source annotation objects and both alternative products are preserved.
Nine actions change; no GO annotation is added. The companion YAML records the
full review and the shared SGMS1/SGMS2 ER question. The JSON preserves the actual
PANTHER path and IBD evidence, action comparison and hashes of temporary retrievals.

The live PTHR21290 target leaf PTN002501710 is below positive IBD PTN000480004
(ER, Golgi, plasma membrane, reverse ceramide formation and choline transfer),
PTN000480005 (CPE activity), and PTN000480007 (SM biosynthesis). There is no
recovered negative assertion on that path. Target inclusion in descendant
experimental support is legitimate. Reaction-definition mismatches affect the
source term, not the demonstrated lineage membership.

## Reaction chemistry

[GO:0002950](https://www.ebi.ac.uk/QuickGO/term/GO:0002950) currently specifies
CDP-ethanolamine and CMP; the SGMS1 reaction uses PE and releases DAG. Likewise,
[GO:0047493](https://www.ebi.ac.uk/QuickGO/term/GO:0047493) specifies CDP-choline,
whereas [GO:0033188](https://www.ebi.ac.uk/QuickGO/term/GO:0033188) describes the
observed PC-dependent SM synthesis. The shared SGMS2 evidence artifact contains
the retrieved term records and OLS searches for a PE-dependent CPE term. Use the
valid broad GO:0016780 until a donor-correct term exists; do not invent an ID.

[PMID:37715942](https://pubmed.ncbi.nlm.nih.gov/37715942/): the published abstract
and the authors' later [Jxiv manuscript](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/4192)
were inspected separately. Methods/Results describe purified human SGMS1,
direct CPE formation from PE and ceramide, and hydrolysis without ceramide.
The manuscript's numerical ratios differ from the final abstract, so no draft
percentage is generalized to cellular activity. The local publication cache
remains the fetched abstract.

[PMID:25605874](https://pmc.ncbi.nlm.nih.gov/articles/PMC4340302/): indexed Results
include Sf9 expression, HeLa isoform assays and Sms1 knockout animals. Results
calls the Sf9 constructs human, while the figure caption/abstract use mouse.
This internal inconsistency is recorded rather than resolved by guessing. The
paper does assay SMS1 despite prominently discussing SMSr. Its Discussion
reports reduced plasma ceramide in Sms1-deficient mice; the source annotation's
upstream-or-within qualifier is retained. The 2023 human purification independently
supports CPE chemistry.

[PMID:14685263](https://pmc.ncbi.nlm.nih.gov/articles/PMC1271672/): previously checked
primary Results/Fig. 5 demonstrate SM-dependent reverse transfer to NBD-DAG in
SMS1-expressing yeast extracts. This regenerates ceramide through work performed
by SGMS1 itself. The forward reaction's usual predominance does not make the
reverse chemistry indirect. The local cache's full-text flag overstates its
actual coverage; the Results were inspected separately.

## Localization and contextual functions

[PMID:14976195](https://doi.org/10.1074/jbc.M401205200): full author-deposited
text was read through ResearchGate. Microscopy uses lysenin to visualize SM,
not the SGMS1 protein. Discussion mentions ER/nuclear enzyme-class activity
and calls for molecular analysis. Complementation and donor tests establish
human SGMS1 activity in mouse lymphoid cells, but do not isolate a human
intrinsic-apoptosis mechanism.

[PMID:38026182](https://pubmed.ncbi.nlm.nih.gov/38026182/): Fig. 3A and its Results
describe a C-terminally tagged SGMS1 protein at the cell surface in human cells.
This is positive protein-location evidence, qualified by the tag and expression
context. Whole-cell functionality does not measure catalysis specifically by
the surface pool. The source IBA is retained as an inherited contextual function.

[Human Protein Atlas SGMS1](https://www.proteinatlas.org/ENSG00000198964-SGMS1/subcellular):
nuclear staining appears in A-431, U-251MG and U2OS with HPA045191. Its
[antibody validation page](https://www.proteinatlas.org/ENSG00000198964-SGMS1/summary/antibody)
reports Approved immunocytochemistry and a predicted-size Western-blot band
with additional bands; enhanced genetic or independent-antibody validation
is not shown. Retain nuclear association as non-core with those caveats, without
claiming nuclear catalysis or identifying a specific isoform. Golgi predominance
and membrane topology do not prove nuclear exclusion.

[PMID:30242129](https://pubmed.ncbi.nlm.nih.gov/30242129/): cached Introduction
and Discussion were read; the cache does not contain complete Methods/Results.
The described cellular complex/proximity manipulations support a contextual
effect on GlcCer synthesis. Construct geometry matters, and the short-chain
in vitro assays do not establish a general allosteric mechanism. Core Golgi
location and SM synthesis remain accepted.

[PMID:16879426](https://pubmed.ncbi.nlm.nih.gov/16879426/): mouse SMS1 suppresses
Bax-associated death in a heterologous yeast setting. This corroborates a
contextual survival function but is not a direct human intrinsic-apoptosis assay.
Existing apoptosis TAS is retained non-core with that distinction.

[PMID:19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/): the original membrane
proteomics annotation is broad but appropriate for an integral membrane enzyme.
Its generality does not justify marking it over-annotated or replacing the
observed compartment with a more specific organelle unsupported by that assay.

Normal SGMS1 ER location/activity remains unresolved. It is covered by the
already requested SGMS2 export-signal adjudication; no duplicate request was
submitted. The separate SGMS2 variant evidence is not silently treated as
SGMS1 evidence. No new BP terms were proposed.
