# accD (Escherichia coli K-12, UniProtKB:P0A9Q5) — curation notes

Reviewed with accA, accB and accC for the ACC part of
`modules/type_ii_fatty_acid_synthesis.yaml`. AccD is the carboxyltransferase beta
subunit, and its treatment mirrors accA's: `GO:0003989` and the
carboxyl/carbamoyltransferase term are over-annotations on a single subunit of an
alpha2beta2 enzyme whose active sites sit at the alpha-beta interfaces, so the
contribution is recorded in `core_functions` with `in_complex: GO:0009317`.

The gene has a genuine second function. Its bacterial-specific zinc domain binds
the coding regions of the accA and accD mRNAs and represses their translation,
with acetyl-CoA relieving the repression and mRNA binding reciprocally inhibiting
catalysis
[PMID:19965770 "Carboxyltransferase binds the coding regions of both subunit mRNAs and inhibits translation, an inhibition that is relieved by the substrate acetyl-CoA."],
through the zinc finger whose four cysteines are needed for both activities
[PMID:19965770 "This interaction is mediated by a zinc finger on the beta-subunit; mutation of the four cysteines to alanine diminished nucleic acid binding and catalytic activity."].
That is modelled as a second core function (mRNA binding, negative regulation of
translation). The separate DNA-binding row is marked over-annotated: the same
surface binds DNA in vitro, but cooperatively and nonspecifically, and DNA acts as
a competitive inhibitor of catalysis
[PMID:18156466 "Half-maximal saturation of different single-stranded or double-stranded DNA constructs is seen at 0.5-1.0 muM, and binding is cooperative and nonspecific."],
which is a polyanion effect rather than a function. `GO:0009329` keeps its
misleading label but is defined as the alpha2beta2 carboxyltransferase that is part
of ACC, so it is accepted.

## Annotation decisions (35 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0003677 DNA binding | IMP | MARK_AS_OVER_ANNOTATED | Nonspecific DNA binding measured in vitro; the physiological nucleic-acid ligand of the carboxyltransferase is its own mRNA. |
| GO:0003729 mRNA binding | IDA | ACCEPT | mRNA binding by the carboxyltransferase, mediated by the AccD zinc finger; the basis of its translational autoregulation. |
| GO:0003989 acetyl-CoA carboxylase activity | IDA | MARK_AS_OVER_ANNOTATED | The complete acetyl-CoA carboxylase reaction, which needs all four subunits; AccD contributes one half-site of the carboxyltransferase. |
| GO:0003989 acetyl-CoA carboxylase activity | IEA | MARK_AS_OVER_ANNOTATED | Electronic assignment of the whole-holoenzyme activity to a single subunit. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from a genome-scale affinity-tagging survey; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from a genome-scale affinity-tagging survey; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from an interaction study; it names no function. |
| GO:0005737 cytoplasm | IEA | MODIFY -> GO:0005829 | Correct but less specific than the direct evidence: the subunit is assigned to the cytosol by proteomics. |
| GO:0005829 cytosol | HDA | ACCEPT | Cytosolic localization from a complexome survey that separated cytosolic complexes. |
| GO:0006633 fatty acid biosynthetic process | IBA | ACCEPT | Phylogenetic assignment of fatty-acid biosynthesis across the bacterial carboxyltransferase beta-subunit family. |
| GO:0006633 fatty acid biosynthetic process | IDA | ACCEPT | Participation in fatty-acid synthesis, from the mechanistic study of the biotin carboxylase and carboxyltransferase reactions. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | Electronic pathway assignment, consistent with the experimental rows. |
| GO:0006633 fatty acid biosynthetic process | IGI | ACCEPT | Genetic interaction evidence: raising all four ACC subunits together raises carboxylase activity and perturbs fatty-acid synthesis. |
| GO:0006633 fatty acid biosynthetic process | IMP | ACCEPT | Perturbation evidence from the same study, testing whether ACC controls the rate of fatty-acid synthesis. |
| GO:0008270 zinc ion binding | IDA | KEEP_AS_NON_CORE | Zinc binding by the bacterial-specific zinc domain of the carboxyltransferase beta subunit, seen in the crystal structure. |
| GO:0008270 zinc ion binding | IDA | KEEP_AS_NON_CORE | Zinc binding by the AccD zinc finger, whose cysteines are required for nucleic-acid binding and catalysis. |
| GO:0008270 zinc ion binding | IEA | KEEP_AS_NON_CORE | Electronic zinc-binding assignment from the curated rule for this family. |
| GO:0009317 acetyl-CoA carboxylase complex | IDA | ACCEPT | Membership of the four-subunit acetyl-CoA carboxylase complex. |
| GO:0009317 acetyl-CoA carboxylase complex | IEA | ACCEPT | Electronic assignment of acetyl-CoA carboxylase complex membership. |
| GO:0009329 acetate CoA-transferase complex | IBA | ACCEPT | Membership of the alpha2beta2 carboxyltransferase component, which is what this oddly-named term denotes. |
| GO:0009329 acetate CoA-transferase complex | IDA | ACCEPT | Direct evidence for the alpha2beta2 carboxyltransferase: peptide mapping of the purified component. |
| GO:0016743 carboxyl- or carbamoyltransferase activity | IEA | MARK_AS_OVER_ANNOTATED | The carboxyl-transfer activity belongs to the alpha-beta pair, not to the beta subunit alone. |
| GO:0017148 negative regulation of translation | IBA | ACCEPT | Phylogenetic assignment of translational repression, the autoregulatory role of the carboxyltransferase. |
| GO:0017148 negative regulation of translation | IDA | ACCEPT | Direct evidence that the carboxyltransferase represses translation of its own subunit mRNAs, with acetyl-CoA relieving the repression. |
| GO:0042759 long-chain fatty acid biosynthetic process | NAS | MARK_AS_OVER_ANNOTATED | A pathway-outcome phrase rather than an annotation: ACC supplies malonyl-CoA for every chain length, not specifically long-chain products. |
| GO:2001295 malonyl-CoA biosynthetic process | IBA | ACCEPT | Phylogenetic assignment of malonyl-CoA biosynthesis, the product of the reaction AccD completes. |
| GO:2001295 malonyl-CoA biosynthetic process | IDA | ACCEPT | Malonyl-CoA formation by the carboxylase, measured in the antibacterial-inhibitor study of the multisubunit enzyme. |
| GO:2001295 malonyl-CoA biosynthetic process | IEA | ACCEPT | Electronic assignment of malonyl-CoA biosynthesis. |

**Core function:** contributes to GO:0003989 acetyl-CoA carboxylase activity; in GO:2001295, GO:0006633; located in GO:0005829; complex GO:0009317

**Core function:** enables GO:0003729 mRNA binding; in GO:0017148; located in GO:0005829

