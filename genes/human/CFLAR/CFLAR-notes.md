# CFLAR notes

## Manual apoptosis review, 2026-09-30

CFLAR encodes cellular FLICE-like inhibitory protein, a tandem-DED regulator of
FADD/CASP8 death-effector assemblies. It is not an active caspase: the original
Casper abstract explicitly states that "Casper is not a caspase" because it
lacks several conserved caspase residues [PMID:9208847, "Casper is a FADD- and
caspase-related inducer of apoptosis"], and the UniProt record likewise notes
that the caspase domain lacks catalytic active-site residues. I therefore
removed IBA and InterPro2GO cysteine endopeptidase / proteolysis rows that were
propagated from active caspases to catalytically inactive c-FLIP.

The core physical function is recruitment into death-effector-domain complexes.
The Irmler c-FLIP paper reports that "FLIPs and FLIP(L) interact with the
adaptor protein FADD and the protease FLICE" and inhibit death-receptor
apoptosis [PMID:9217161, "Inhibition of death receptor signals by cellular
FLIP"]. The 2024 structural paper directly solved human
FADD-procaspase-8-cFLIP DED complexes and shows how FADD and c-FLIP assemble
CASP8-containing complexes [PMID:38710704, "Deciphering DED assembly mechanisms
in FADD-procaspase-8-cFLIP complexes regulating apoptosis"]. Existing FADD,
CASP8, and CASP10 rows were therefore narrowed where possible from generic
`protein binding` to `GO:0035877 death effector domain binding`.

c-FLIP has isoform- and stoichiometry-specific outputs that should not be
flattened into a catalytic assertion. FLIP(L) contains a pseudo-caspase domain
that forms limited-activity CASP8 or CASP10 heterodimers, while DED-only
FLIP(S) blocks DISC-dependent CASP8 processing. The ripoptosome paper identified
a RIP1/FADD/CASP8/CASP10/cFLIP platform and reported that "cFLIP(L) prevents
Ripoptosome formation, whereas, intriguingly, cFLIP(S) promotes Ripoptosome
assembly" [PMID:21737330, "cIAPs block Ripoptosome formation, a RIP1/caspase-8
containing intracellular cell death complex differentially regulated by cFLIP
isoforms"]. I kept the bidirectional `GO:0060544 regulation of necroptotic
process` row, proposed the more specific FLIP(L)-leaning
`GO:0060546 negative regulation of necroptotic process`, and described FLIP(L)
versus FLIP(S) in `functional_isoforms`.

The broad `GO:0006915 apoptotic process`, `GO:0008625 extrinsic apoptotic
signaling pathway via death domain receptors`, and `GO:0030225 macrophage
differentiation` IBA rows are active-caspase family transfers rather than good
descriptions of CFLAR. CFLAR belongs to PANTHER:PTHR48169:SF3, distinct from
CASP8/CASP10 in PTHR48169:SF7, and the family contains catalytically active
caspases plus DED pseudoenzymes. I added structured propagation reviews marking
the catalytic and sign-leaking PAINT rows as pseudoenzyme loss, role conflation,
or term-scoping problems.

Most Ensembl Compara rows from rat and mouse describe tissue or stimulus
phenotypes rather than work done by human c-FLIP: hypoxia, insulin, hormone,
EGF, nitric oxide, hepatocyte/epithelial apoptosis, glomerular mesangial
proliferation, extracellular matrix, TGF-beta and ROS response, and skeletal
muscle regeneration / atrophy / myofibril / myoblast terms. These were marked
as over-annotations, preserving the direct DISC, CD95 DISC, cytosol, and
ripoptosome rows.

Several IntAct rows remain undecided because the cached abstracts do not expose
the individual partner edge even though the full-text curation may be valid:
CASP10 in the TNFR1 complex-II paper, CASP8 in the TRAIL/HUVEC proangiogenic
paper, CASP10 in the in situ PPI survey, and the HO-1 / Lifeguard
death-receptor-inhibition process rows. The old Casper
`GO:0008047 enzyme activator activity` and `GO:2001237 negative regulation of
extrinsic apoptotic signaling pathway` IDA rows are also left undecided because
the abstract mixes wild-type overexpression with C-terminal deletion mutant
effects.
