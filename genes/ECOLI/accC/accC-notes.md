# accC (Escherichia coli K-12, UniProtKB:P24182) — curation notes

Reviewed with accA, accB and accD for the ACC part of
`modules/type_ii_fatty_acid_synthesis.yaml`. AccC is the biotin carboxylase: it
uses ATP and bicarbonate to carboxylate the biotin of AccB (EC 6.3.4.14), which is
its own measured activity and the gene's core function. Because that half-reaction
really is an ATP-dependent carbon-nitrogen ligation, the broad ligase terms are
kept as TOO_GENERAL here, whereas on the carboxyltransferase subunits they are
removed as mislocating the chemistry. `GO:0003989`, the complete four-subunit
reaction, is over-annotated on this subunit as on the others.

## Annotation decisions (32 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0003989 acetyl-CoA carboxylase activity | IBA | MARK_AS_OVER_ANNOTATED | The holoenzyme reaction is correctly assigned to the biotin carboxylase clade, but AccC alone catalyses only the first half-reaction; it cannot car... |
| GO:0004075 biotin carboxylase activity | EXP | ACCEPT | Biotin carboxylase activity of purified E. coli AccC and of dimer-interface mutants was measured directly; this is the protein's own catalytic func... |
| GO:0004075 biotin carboxylase activity | EXP | ACCEPT | The structure of E. coli BC with biotin, bicarbonate and Mg-ADP bound, plus mutagenesis and kinetics, defines the biotin carboxylase mechanism. |
| GO:0004075 biotin carboxylase activity | IDA | ACCEPT | Biotin carboxylase activity attributable to accC was assayed in the ACC overproduction study. |
| GO:0004075 biotin carboxylase activity | IEA | ACCEPT | Electronic mapping from the Rhea reaction and EC number that UniProt records with experimental evidence for this entry. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccC/AccD interaction it records is real and is captured informatively by the complex t... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccC/AccB interaction it records is the functionally central BC-BCCP pair, kept elsewhe... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding with a cysteine synthase (CysM) partner from a large-scale affinity screen; uninformative. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding with the riboflavin biosynthesis bifunctional enzyme RibD from a large-scale affinity screen; uninformative. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccC/AccB interaction is retained informatively elsewhere. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccC/AccD interaction is retained informatively as complex membership. |
| GO:0005515 protein binding | IPI | REMOVE | Generic form of the BC-BCCP crystal structure interaction; the structural content is used elsewhere in this review. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from a genome-scale two-hybrid screen; uninformative. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from a genome-scale two-hybrid screen; uninformative. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding with CysM from a genome-scale two-hybrid screen; uninformative. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding with RibD from a genome-scale two-hybrid screen; uninformative. |
| GO:0005524 ATP binding | IEA | ACCEPT | AccC has an ATP-grasp fold and ATP is bound in its crystal structures; ATP binding is an integral part of its catalytic mechanism. |
| GO:0005737 cytoplasm | IC | MODIFY -> GO:0005829 | Cytoplasmic localization is right but less precise than the cytosol localization directly demonstrated for AccC by proteomics. |
| GO:0005829 cytosol | IDA | ACCEPT | AccC was assigned to the cytosol by fractionation, 2D gel electrophoresis and tandem mass spectrometry. |
| GO:0005829 cytosol | IDA | ACCEPT | Independent detection of AccC in the E. coli cytosolic proteome. |
| GO:0006633 fatty acid biosynthetic process | IBA | ACCEPT | Phylogenetic propagation of the fatty acid biosynthesis role to the biotin carboxylase clade; correct and core for E. coli AccC. |
| GO:0006633 fatty acid biosynthetic process | IDA | ACCEPT | Classical mechanistic study of the purified E. coli ACC system, including the biotin carboxylase half-reaction. |
| GO:0006633 fatty acid biosynthetic process | IGI | ACCEPT | Coordinate overexpression of accC with the other three acc genes raises ACC activity, malonyl-CoA and the rate of fatty acid synthesis. |
| GO:0006633 fatty acid biosynthetic process | IMP | ACCEPT | Changing accC expression changes flux into fatty acid synthesis, placing the gene within the pathway. |
| GO:0009317 acetyl-CoA carboxylase complex | IDA | ACCEPT | Direct evidence that accC encodes one of the four subunits of the E. coli acetyl-CoA carboxylase holoenzyme; core for the gene. |
| GO:0016874 ligase activity | IEA | TOO_GENERAL | True but uninformative: the specific ligase activity of AccC, biotin carboxylase activity, is accepted in this review and entails this term. |
| GO:0016879 ligase activity, forming carbon-nitrogen bonds | IEA | TOO_GENERAL | True but uninformative: this is the immediate parent of the accepted biotin carboxylase activity. |
| GO:0042803 protein homodimerization activity | IDA | KEEP_AS_NON_CORE | AccC is a homodimer and dimerization is required for its function in vivo, but dimerization supports the catalytic activity rather than being the c... |
| GO:0045717 negative regulation of fatty acid biosynthetic process | IMP | MARK_AS_OVER_ANNOTATED | What the cited experiment shows is that unbalanced AccC overproduction sequesters AccB and leaves it underbiotinylated, which down-regulates biotin... |
| GO:0046872 metal ion binding | IEA | MODIFY -> GO:0000287, GO:0030145 | Correct but general: the ions AccC binds are identified, magnesium in the substrate complex and manganese as an alternative. |
| GO:2001295 malonyl-CoA biosynthetic process | IDA | ACCEPT | AccC catalyses the first of the two half-reactions by which the ACC holoenzyme makes malonyl-CoA. |
| GO:2001295 malonyl-CoA biosynthetic process | IEA | ACCEPT | UniPathway mapping of the malonyl-CoA biosynthesis step; agrees with the curated pathway statement and the direct evidence. |

**Core function:** contributes to GO:0004075 biotin carboxylase activity; in GO:2001295, GO:0006633; located in GO:0005829; complex GO:0009317

