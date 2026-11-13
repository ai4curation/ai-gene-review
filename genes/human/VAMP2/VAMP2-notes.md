# VAMP2 (synaptobrevin-2, P63027) — curation notes

## What the protein is

A 116-residue tail-anchored R-SNARE of the synaptic vesicle membrane: proline-rich
N-terminus, ~60-residue SNARE motif with the zero-layer arginine, a tryptophan-containing
juxtamembrane linker, and a C-terminal transmembrane anchor. UniProt states the function
plainly: "VAMP2 is a v-SNARE assembling into a SNARE complex with the t-SNAREs SNAP25 and
STX1A to mediate the fusion of synaptic vesicles with the presynaptic plasma membrane in
neurotransmitter release" (`file:human/VAMP2/VAMP2-uniprot.txt`).

The only *human*-specific functional evidence in this entry is the disease study:
[PMID:30929742 "VAMP2 is essential for vesicular exocytosis and activity-dependent
neurotransmitter release."] and [PMID:30929742 "Reconstituted fusion involving a
lipid-mixing assay indicated impairment in vesicle fusion as one of the possible associated
disease mechanisms."]. Almost everything else in the GOA table is ISS from the rat and mouse
orthologues (P63045/P63044, identical over the SNARE motif), IBA from the synaptobrevin
PAINT node, or Reactome TAS. That is acceptable here — the orthologues are the proteins the
mechanistic work was done on — but it is why so few rows carry a direct human quote.

## Core

Two core functions: `GO:0005484` (the term is now *helical-bundle zippering fusogenic
activity*, checked against QuickGO, not *SNAP receptor activity* as in older reviews) and
`GO:0017075` syntaxin-1 binding, the binary interaction that nucleates the bundle
[PMID:10481273 "The entire SNARE motif of synaptobrevin is capable of interacting with the
isolated C-terminal SNARE motif of syntaxin"]. Directly involved in vesicle fusion, synaptic
vesicle exocytosis, calcium-ion regulated exocytosis and SNARE complex assembly; located on
the synaptic vesicle membrane and (post-fusion) the plasma membrane; in the SNARE complex.

This matches the worm comparator `snb-1` on the shape of the claim. Two differences worth
recording. First, `snb-1` uses the old label for `GO:0005484`; the term has been renamed and
redefined as a mechanism-based fusogen class. Second, `snb-1` lists only exocytosis and
vesicle fusion under `directly_involved_in`; I added `GO:0017156` calcium-ion regulated
exocytosis and `GO:0035493` SNARE complex assembly, because VAMP2 contributes one of the
four helices and so does part of the work of assembly (QuickGO confirms `GO:0035493` is a
descendant of `GO:0006906`, so the two are not in tension).

## Decisions that took thought

**Protein binding (42 rows).** Removed as uninformative, which is not a claim that any of
these interactions is false — PRKD3, WDFY2/PKCζ, α-synuclein, CALM, VAP-B, the clostridial
proteases, and the two large interactome maps. Two rows were modified instead, because the
partner is a syntaxin and an informative term exists: PMID:10481273 (NMR of the
synaptobrevin–syntaxin motifs) and PMID:38225382 [".. we further experimentally corroborated
for FBXO23-STX1B, STX1B-VAMP2, .."]. No GO term exists for α-synuclein binding or for
clathrin-adaptor binding (searched OLS), so those could not be rescued.

**Execution versus regulation.** `regulation of exocytosis`, `regulation of
vesicle-mediated transport` and `positive regulation of intracellular protein transport` are
marked over-annotated. VAMP2 *is* the fusion machine; the regulators of that step are
synaptotagmin, complexin, Munc13 and Munc18. The same reasoning retires `response to
glucose`: VAMP2 is machinery used downstream of glucose sensing, not a protein whose state
changes in response to the sugar.

**The negative annotations are the useful part of the non-neuronal tail**, and all four are
supported by their cited paper: neutrophil degranulation [PMID:16677249 "Our observations
indicate for the first time a critical role for VAMP-7 in both eosinophil and neutrophil
mediator release."], NK degranulation [PMID:18042464 "Our data showed that YT-Indy cells
express VAMP-7 and SNAP-23, but not VAMP-2."], mucus secretion [PMID:22144578 "Unlike VAMP8
silencing, knockdown of VAMP2 or VAMP3 did not affect mucin secretion."] and mast cell
histamine release [PMID:18253931 "Inhibition of SNAP-23, STX-4, VAMP-7 or VAMP-8, but not
VAMP-2 or VAMP-3, resulted in a markedly reduced high-affinity IgE receptor-mediated
histamine release."]. The *positive* eosinophil row from the same granulocyte paper survives
as non-core, because the abstract records a real if minor effect [PMID:16677249 "In
contrast, anti-VAMP-2 modestly and selectively impaired secretion from small granules and
vesicles."].

The NOT on `secretory granule membrane` (granulocyte granules) collides with a Reactome TAS
row for the same term (neuroendocrine granules). Both claims hold in different cell types,
so the NOT row carries a `consistency_exception` rather than either row being dropped. The
schema check accepts this; a separate generic warning about same-term actions remains and is
expected.

**Reactome's clathrin-sculpted transport vesicle membranes** (glutamate, GABA, monoamine —
14 rows). QuickGO shows `GO:0060203` sits under *clathrin-coated vesicle membrane*, not
under *synaptic vesicle membrane*, so these describe the retrieved and reloading compartment
rather than the fusion-competent vesicle. Kept as non-core, consistent with the
clathrin-coated endocytic vesicle membrane rows. The route is real: [PMID:22118466 ".. the
N-terminal halves of their SNARE motifs bind the CALM(ANTH) domain as helices"] means only
disassembled VAMP2 is sorted.

**Cytosol (7 Reactome rows)** marked over-annotated: the SNARE motif faces the cytoplasm but
the protein is membrane-anchored throughout its life.

**Voltage-gated potassium channel complex** marked over-annotated while `regulation of
delayed rectifier potassium channel activity` is kept as non-core. These are different
claims: UniProt supports a modulatory contact with the KCNB1 N-terminus, not subunit
membership.

## Open

Nothing is left `UNDECIDED`. The two questions I could not settle from the cached material —
whether VAMP2 performs any of the work of synaptic vesicle endocytosis or is only its cargo,
and which R-SNARE carries insulin-stimulated GLUT4 exocytosis in human tissue — are recorded
as `suggested_questions` with matching experiments. `synaptic vesicle endocytosis` is kept as
non-core for exactly that reason.
