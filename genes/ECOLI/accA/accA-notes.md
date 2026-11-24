# accA (Escherichia coli K-12, UniProtKB:P0ABD5) — curation notes

Reviewed as part of the acetyl-CoA carboxylase (ACC) part of
`modules/type_ii_fatty_acid_synthesis.yaml`, together with accB, accC and accD.
AccA is the alpha subunit of the alpha2beta2 carboxyltransferase: it supplies half
of each active site that transfers the carboxyl group from carboxybiotinyl-AccB to
acetyl-CoA, giving malonyl-CoA. No isolated subunit performs the complete ACC
reaction, which is why `GO:0003989` is marked over-annotated on every subunit of
the complex and the subunit's share is recorded as
`contributes_to_molecular_function` with `in_complex: GO:0009317`. Ligase terms
are removed here (a carboxyltransferase performs a group transfer and no
ATP-coupled ligation) while the same terms are kept as TOO_GENERAL on accC, which
does the ATP chemistry — the difference is deliberate.

## Annotation decisions (28 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0003989 acetyl-CoA carboxylase activity | IEA | MARK_AS_OVER_ANNOTATED | The overall ATP-dependent carboxylation of acetyl-CoA is a holoenzyme reaction; AccA supplies only the alpha half of the carboxyltransferase active... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccA/AccD interaction it records is real but is captured informatively by the complex t... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccA/AccD interaction it records is real but is captured informatively by the complex t... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccA/AccD interaction it records is real but is captured informatively by the complex t... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccA/AccD interaction it records is real but is captured informatively by the complex t... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccA/AccD interaction it records is real but is captured informatively by the complex t... |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding carries no functional information; the AccA/AccD interaction it records is real but is captured informatively by the complex t... |
| GO:0005737 cytoplasm | IC | MODIFY -> GO:0005829 | Cytoplasmic localization is right but less precise than the cytosol localization directly demonstrated for AccA by proteomics. |
| GO:0005737 cytoplasm | IEA | MODIFY -> GO:0005829 | Electronic cytoplasm mapping from the UniProt subcellular-location keyword; correct but coarser than the demonstrated cytosolic localization. |
| GO:0005829 cytosol | IDA | ACCEPT | AccA was assigned to the cytosol by biochemical fractionation followed by 2D gel electrophoresis and tandem mass spectrometry. |
| GO:0005829 cytosol | IDA | ACCEPT | Independent confirmation of cytosolic localization from quantitative profiling of the E. coli cytosolic proteome. |
| GO:0006633 fatty acid biosynthetic process | IBA | ACCEPT | Phylogenetic propagation of the fatty acid biosynthesis role to the ACC carboxyltransferase alpha subunit clade; correct for E. coli AccA. |
| GO:0006633 fatty acid biosynthetic process | IDA | ACCEPT | Classical mechanistic study of the purified E. coli ACC system, including the carboxyltransferase half-reaction that AccA contributes to. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | InterPro2GO mapping of the AccA family signature to fatty acid biosynthesis; the right process for this protein. |
| GO:0006633 fatty acid biosynthetic process | IGI | ACCEPT | Coordinate overexpression of accA with accB, accC and accD raises ACC activity, malonyl-CoA levels and the rate of fatty acid synthesis. |
| GO:0006633 fatty acid biosynthetic process | IMP | ACCEPT | Manipulating accA expression changes flux into fatty acid synthesis, placing the gene within the pathway. |
| GO:0009317 acetyl-CoA carboxylase complex | IBA | ACCEPT | Propagated membership of the heteromeric acetyl-CoA carboxylase; correct and core for AccA. |
| GO:0009317 acetyl-CoA carboxylase complex | IDA | ACCEPT | Direct evidence that accA encodes one of the four subunits of the E. coli acetyl-CoA carboxylase holoenzyme. |
| GO:0009317 acetyl-CoA carboxylase complex | IEA | ACCEPT | InterPro2GO mapping of the AccA signature to the acetyl-CoA carboxylase complex; agrees with the direct evidence. |
| GO:0009329 acetate CoA-transferase complex | IDA | ACCEPT | AccA is the 35-kDa alpha subunit of the purified two-subunit carboxyltransferase component of E. coli ACC, which is what this GO term denotes. |
| GO:0016743 carboxyl- or carbamoyltransferase activity | IEA | MARK_AS_OVER_ANNOTATED | The right reaction class for the half-reaction AccA takes part in, but the activity belongs to the AccA/AccD heterotetramer, not to AccA alone. |
| GO:0016874 ligase activity | IEA | REMOVE | AccA catalyses no ligation; the ATP-dependent carbon-nitrogen ligase step of ACC is the biotin carboxylase (AccC) half-reaction. |
| GO:0042759 long-chain fatty acid biosynthetic process | NAS | MARK_AS_OVER_ANNOTATED | True of the end products of E. coli fatty acid synthesis, but a narrowing of the pathway role that the malonyl-CoA supply does not justify. |
| GO:0042802 identical protein binding | IPI | KEEP_AS_NON_CORE | Two copies of AccA are present in the alpha2beta2 carboxyltransferase, so self-association is structurally real, but it is a property of complex as... |
| GO:0042802 identical protein binding | IPI | KEEP_AS_NON_CORE | Yeast two-hybrid self-interaction of AccA, consistent with the two alpha subunits of the carboxyltransferase. |
| GO:2001295 malonyl-CoA biosynthetic process | IBA | ACCEPT | Propagated assignment of the single-step malonyl-CoA biosynthetic process to the ACC alpha carboxyltransferase clade; correct and core. |
| GO:2001295 malonyl-CoA biosynthetic process | IDA | ACCEPT | Assays of the isolated E. coli carboxyltransferase measure malonyl-CoA turnover and map inhibitor resistance to accA, directly placing AccA in malo... |
| GO:2001295 malonyl-CoA biosynthetic process | IEA | ACCEPT | Electronic assignment of the malonyl-CoA biosynthesis pathway from the curated HAMAP/UniRule system; agrees with the direct evidence. |

**Core function:** contributes to GO:0003989 acetyl-CoA carboxylase activity; in GO:2001295, GO:0006633; located in GO:0005829; complex GO:0009317

