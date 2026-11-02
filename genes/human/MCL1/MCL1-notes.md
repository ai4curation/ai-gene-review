# MCL1 apoptosis review notes

## 2026-09-30

Seeded MCL1 for the APOPTOSIS BCL2-family MOMP-control slice with
`just fetch-gene human MCL1`, yielding 117 GOA rows.

MCL1 is in PANTHER family `PTHR11256`, subfamily `PTHR11256:SF46`
("INDUCED MYELOID LEUKEMIA CELL DIFFERENTIATION PROTEIN MCL-1"). The
human protein sits under the same broad `PTN000135648` BCL2-family PAINT
node as BAX, BAK1, BCL2, and BCL2L1. That node carries both positive and
negative apoptotic regulation, channel activity, cytochrome-c release,
outer-membrane localization, DNA-damage intrinsic apoptosis, and
ligand-withdrawal signaling, so MCL1 inherited several rows that need
role/sign review rather than simple acceptance by family membership.

Canonical MCL-1L is a pro-survival OMM BCL2-family protein. Willis et al.
show that healthy cells keep BAK associated specifically with Mcl-1 and
Bcl-xL, and that displacement of BAK from both anti-apoptotic partners is
needed for BAK-mediated cell death [PMID:15901672]. Obatoclax experiments
then provide a membrane-preserving demonstration of the endogenous
MCL1/BAK complex: isolated intact mitochondria and intact SK-Mel5 cells
both showed obatoclax-sensitive MCL1/BAK association, while obatoclax
alone did not directly release cytochrome c from isolated mitochondria
[PMID:18040043]. These sources justify tightening broad generic
`protein binding` and apoptosis-regulation rows to BH3-domain binding
and negative regulation of MOMP or cytochrome-c release.

MCL1 has conditional pro-death products that must not be conflated with
the long isoform. Bae et al. describe MCL-1S as a short splice product
that lacks BH1/BH2 and the transmembrane domain, dimerizes with MCL-1L,
and induces apoptosis when overexpressed [PMID:10837489]. UniProt also
records caspase cleavage of intact MCL1 to a pro-apoptotic C-terminal
fragment. These findings explain old positive-apoptosis assertions but
do not turn canonical MCL-1L into a BAK/BAX-like pore.

Several rows are correctly secondary rather than core. MCL1 stability
falls after IL-3 withdrawal through GSK3-dependent S159
phosphorylation, ubiquitination, and degradation, and GSK3 inhibition
maintains MCL1, cytochrome-c retention, and survival in that
ligand-withdrawal context [PMID:16543145]. The BOK/MCL1 trophoblast
paper supports a BECN1-associated autophagy role in which pro-survival
MCL1 represses autophagy and BOK or oxidative stress disrupts that
state [PMID:24113155]. Cav1 stabilizes MCL1 and decreases
detachment-induced anoikis in lung carcinoma and melanoma cells, but the
reciprocal MCL1/Cav1 protein-binding row is still a low-information
generic contact for MCL1 itself [PMID:22277751].

The GOA file has many `GO:0005515 protein binding` imports from large
IntAct or screening papers. Focused BCL2-family interaction sources can
be converted to `GO:0051434 BH3 domain binding`; large interactome rows
or enzyme/substrate contacts to USP9X, HUWE1, AKT1, and membrane traffic
proteins should not be retained as generic MCL1 molecular functions.

The annotation-reviewer audit agreed with the central BH3-groove/MOMP
framing and the sign fixes, but identified several abstract-only rows
where the initial pass was too confident. Those BIM/BID/PUMA/NOXA/BAX
rows were changed back to `UNDECIDED` pending the hidden full text, the
Reactome expression-module cytosol rows were removed, mitochondrial
fusion and cytokine-withdrawal apoptosis were kept as non-core
contexts, and the stability-control paragraph was folded out of
`core_functions` so the only core activity is canonical MCL-1L
BH3-domain binding at the OMM.
