# fabI (Escherichia coli K-12, UniProtKB:P0AEK4) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml` as the E. coli
representative of the FabI enoyl-reduction variant, and as the reference protein
for the PTHR43159 family review. FabI (formerly EnvM) reduces trans-2-enoyl-ACP
with NADH
[PMID:8119879 "It showed NADH-dependent enoyl-acyl carrier protein (ACP) reductase activity using both crotonyl-ACP and crotonyl-CoA as substrates."]
and is the only enoyl-ACP reductase E. coli has
[PMID:7592873 "FabI was verified to be the only enoyl-ACP reductase required for the synthesis of fatty acids by demonstrating that purified FabI was required for the"];
because the dehydratase equilibrium favours the hydroxyacyl intermediate, the amount
of FabI sets how much product the cycle makes
[PMID:7592873 "The amount of butyryl-ACP formed depended on the amount of FabI protein added to the assay."].

Cofactor note: both the NADH- and the NADPH-dependent enoyl-ACP reductase activities
of E. coli reside in this one protein
[PMID:9022698 "We now demonstrate that both enoyl-ACP reductase activities reside in FabI."],
with the NADPH activity about eightfold more diazaborine-resistant. No `GO:0141148`
(NADPH) row was proposed: the curated reaction, the kinetics and the structures all
describe the NADH reaction, the preference for NADH is marked, and a second
cofactor-specific annotation would assert a physiological role the data do not
establish. The open question is recorded in `suggested_questions` instead.

The membrane row (HDA, from a blue-native complexome gel) is marked over-annotated
rather than removed: FabI has no transmembrane segment, is soluble, and is assigned
to the cytosol by two independent proteomes, but the cached abstract does not say
which fraction FabI came from, so a peripheral association cannot be excluded. The
bare `GO:0005515` row is removed under the protein-binding policy; the homotetramer
is covered by the identical-protein-binding, homotetramerization and catalytic-complex
rows, and `GO:0032991` is TOO_GENERAL beside `GO:1902494`. The biotin rows are
non-core: FabI really does perform the reduction in the diverted elongation rounds
that build the pimeloyl moiety
[PMID:20693992 "Moreover, the effects of triclosan were shown to be due to inhibition of FabI because addition of purified Vibrio cholerae FabV, a naturally triclosan-resistant enoyl-ACP reductase24, largely restored DTB synthesis to triclosan-treated extracts."],
so this is participation, but with the same catalytic step serving a second pathway.

## Annotation decisions (28 GOA rows)

| GO term | Evidence | Action | Rationale in brief |
|---|---|---|---|
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | EXP | ACCEPT | The core NADH-dependent enoyl-ACP reductase activity, in the reconstitution of a complete round of E. coli fatty-acid synthesis. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | EXP | ACCEPT | Enoyl-ACP reductase activity of E. coli FabI, used as the reference enzyme in the characterization of the B. subtilis reductases. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | EXP | ACCEPT | Enoyl-ACP reductase activity, from the study showing FabI is the only reductase able to complete the elongation cycle. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | EXP | ACCEPT | Enoyl-ACP reductase activity in the reconstituted system used to study FabH regulation. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | IBA | ACCEPT | Phylogenetic assignment of NADH-dependent enoyl-ACP reductase activity across the FabI/InhA/ENR clade. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | IDA | ACCEPT | Enoyl-ACP reductase activity assayed directly while characterizing triclosan inhibition. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | IDA | ACCEPT | The activity that established EnvM as FabI: NADH-dependent reduction of crotonyl-ACP by the purified protein. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | IDA | ACCEPT | Enoyl-ACP reductase activity of purified FabI, in the study showing both NADH- and NADPH-dependent activities reside in this one protein. |
| GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity | IEA | ACCEPT | Electronic assignment of the core activity from the FabI family signature, Rhea and EC. |
| GO:0005515 protein binding | IPI | REMOVE | Bare protein binding from a large-scale affinity-tagging screen; it names no function. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from fractionation-based proteomic assignment. |
| GO:0005829 cytosol | IDA | ACCEPT | Cytosolic localization from abundance profiling of the cytosolic fraction. |
| GO:0006633 fatty acid biosynthetic process | IEA | ACCEPT | Fatty-acid biosynthesis is the pathway FabI's reduction completes. |
| GO:0008610 lipid biosynthetic process | IDA | TOO_GENERAL | Correct but uninformative process: the fatty-acid biosynthesis and elongation terms asserted in this review entail it. |
| GO:0008610 lipid biosynthetic process | IMP | TOO_GENERAL | Correct but uninformative process, from the envM mutant phenotype; the specific biosynthetic terms are asserted elsewhere. |
| GO:0009102 biotin biosynthetic process | IEA | KEEP_AS_NON_CORE | Biotin synthesis uses the same elongation chemistry, so FabI serves it; a real secondary role of the core activity. |
| GO:0009102 biotin biosynthetic process | IMP | KEEP_AS_NON_CORE | Experimental demonstration that blocking FabI blocks biotin precursor synthesis. |
| GO:0016020 membrane | HDA | MARK_AS_OVER_ANNOTATED | Membrane localization from a complexome gel survey; FabI is a soluble cytosolic enzyme. |
| GO:0030497 fatty acid elongation | IBA | ACCEPT | Phylogenetic assignment of fatty-acid elongation across the FabI clade. |
| GO:0030497 fatty acid elongation | IDA | ACCEPT | Direct demonstration that FabI is the step that completes each elongation cycle and determines how much saturated product is made. |
| GO:0030497 fatty acid elongation | IMP | ACCEPT | Elongation is a target of acyl-ACP feedback acting on the reconstituted cycle, which places FabI in the process. |
| GO:0032991 protein-containing complex | IDA | TOO_GENERAL | Correct but uninformative: the specific catalytic-complex and homotetramer claims are asserted elsewhere in this review. |
| GO:0042802 identical protein binding | IDA | KEEP_AS_NON_CORE | Self-association of FabI, which is a homotetramer. |
| GO:0042802 identical protein binding | IPI | KEEP_AS_NON_CORE | Self-association seen in the triclosan-NADH ternary complex structure. |
| GO:0042802 identical protein binding | IPI | KEEP_AS_NON_CORE | Self-association seen while characterizing triclosan inhibition kinetics. |
| GO:0051289 protein homotetramerization | IDA | KEEP_AS_NON_CORE | Assembly of the FabI homotetramer. |
| GO:0070404 NADH binding | IDA | KEEP_AS_NON_CORE | NADH binding, seen in the ternary complex with triclosan and demonstrated kinetically. |
| GO:1902494 catalytic complex | IDA | KEEP_AS_NON_CORE | The catalytically competent unit is an oligomer, resolved as an enzyme-NAD(+)-inhibitor complex. |

**Core function:** enables GO:0004318 enoyl-[acyl-carrier-protein] reductase (NADH) activity; in GO:0006633, GO:0030497; located in GO:0005829

