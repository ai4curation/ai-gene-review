# accB (Escherichia coli K-12, UniProtKB:P0ABD8) — curation notes

Reviewed with accA, accC and accD for the ACC part of
`modules/type_ii_fatty_acid_synthesis.yaml`. AccB is the biotin carboxyl carrier
protein (BCCP): its biotinylated lysine is carboxylated by AccC and then swings to
the carboxyltransferase, so the subunit carries the activated carboxyl group
rather than catalysing anything itself. The molecular-adaptor row was therefore
refined to molecular carrier activity, and `GO:0003989` is marked over-annotated
on this subunit as on the other three.

## Annotation decisions (18 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0003989 acetyl-CoA carboxylase activity | IBA | MARK_AS_OVER_ANNOTATED | The holoenzyme reaction is correctly assigned to the BCCP clade, but AccB has no catalytic activity of its own: it carries the carboxyl group rathe... |
| GO:0003989 acetyl-CoA carboxylase activity | IEA | MARK_AS_OVER_ANNOTATED | InterPro2GO mapping of the BCCP signature to the holoenzyme activity; the right complex, the wrong entity for an enables-style claim. |
| GO:0003989 acetyl-CoA carboxylase activity | IMP | MARK_AS_OVER_ANNOTATED | Raising accB levels together with the other three subunits raises measured ACC activity, which demonstrates a requirement for AccB rather than an a... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccB/AccC interaction it records is real and is captured informatively elsewhere in thi... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccB/AccC interaction it records is real and is captured informatively elsewhere in thi... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; here it is the generic form of the BC-BCCP crystal structure, whose content is kept as carr... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccB/AccC two-hybrid interaction adds no functional detail. |
| GO:0005737 cytoplasm | IC | MODIFY -> GO:0005829 | Cytoplasmic localization is right but less precise than the cytosol localization directly demonstrated for AccB by proteomics. |
| GO:0005829 cytosol | IDA | ACCEPT | AccB was assigned to the cytosol by fractionation, 2D gel electrophoresis and tandem mass spectrometry. |
| GO:0006633 fatty acid biosynthetic process | IBA | ACCEPT | Phylogenetic propagation of the fatty acid biosynthesis role to the BCCP clade; correct and core for E. coli AccB. |
| GO:0006633 fatty acid biosynthetic process | IDA | ACCEPT | Classical mechanistic study of the purified E. coli ACC system, in which the biotinylated carrier protein is one of the components assayed. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | Electronic assignment of the fatty acid biosynthesis pathway from the BCCP signature and UniPathway; agrees with the experimental rows. |
| GO:0006633 fatty acid biosynthetic process | IGI | ACCEPT | Coordinate overexpression of accB with accA, accC and accD raises ACC activity, malonyl-CoA and the rate of fatty acid synthesis. |
| GO:0006633 fatty acid biosynthetic process | IMP | ACCEPT | Changing accB expression changes flux into fatty acid synthesis, placing the gene within the pathway. |
| GO:0009317 acetyl-CoA carboxylase complex | IDA | ACCEPT | Direct evidence that accB encodes one of the four subunits of the E. coli acetyl-CoA carboxylase holoenzyme; this is core for the gene. |
| GO:0009317 acetyl-CoA carboxylase complex | IEA | ACCEPT | InterPro2GO mapping of the BCCP signature to the acetyl-CoA carboxylase complex; agrees with the direct evidence. |
| GO:0060090 molecular adaptor activity | EXP | MODIFY -> GO:0140104 | The experiment shows BCCP docking on the biotin carboxylase dimer, but AccB's function is to carry the activated carboxyl group between two active ... |
| GO:2001295 malonyl-CoA biosynthetic process | IDA | ACCEPT | AccB takes part in the single-step conversion of acetyl-CoA to malonyl-CoA assayed for the E. coli holoenzyme. |

**Core function:** contributes to GO:0140104 molecular carrier activity; in GO:2001295, GO:0006633; located in GO:0005829; complex GO:0009317

