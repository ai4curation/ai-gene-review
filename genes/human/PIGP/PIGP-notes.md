# PIGP (human) — review notes

UniProtKB:P57054, HGNC:3046. Aliases: DSCR5, DCRC, DSCRC, DSCR6-neighbor; "Down syndrome
critical region protein 5 / C". Gene on chr 21q22.2. 158 aa, small multi-pass membrane
protein with two predicted TM helices (UniProt TRANSMEM 40-60, 80-100).

## Core biology (grounded in UniProt + cached abstracts)

PIGP (PIG-P) is a small, **non-catalytic accessory subunit** of the
GPI-N-acetylglucosaminyltransferase (**GPI-GnT**) complex. GPI-GnT catalyses the first,
committed step of GPI-anchor biosynthesis: transfer of GlcNAc from UDP-GlcNAc onto
phosphatidylinositol (PI) to give GlcNAc-PI. The catalytic subunit is **PIGA**; PIGP is
required for activity but is not itself the catalytic enzyme.

- [PMID:10944123 abstract, "Biosynthesis of GPI is initiated by GPI-N-acetylglucosaminyltransferase (GPI-GnT), which transfers N-acetylglucosamine from UDP- N-acetylglucosamine to phosphatidylinositol."] — defines the reaction.
- [PMID:10944123 abstract, "PIG-P, a 134-amino acid protein having two hydrophobic domains, associates with PIG-A and GPI1."] — PIGP binds PIGA (P37287) and GPI1/PIGQ.
- [PMID:10944123 abstract, "PIG-P is essential for GPI-GnT since a cell lacking PIG-P is GPI-anchor negative."] — required subunit (IMP-like functional evidence: PIGP-null cells are GPI-anchor negative).
- [PMID:16162815 abstract, "consisting of at least six proteins" ... "A complex of six components was formed without PIG-Y."] — GPI-GnT is multi-subunit; PIGP is one of the components. UniProt SUBUNIT: "composed at least by PIGA, PIGC, PIGH, PIGP, PIGQ, PIGY and DPM2".
- [PMID:28334793 abstract, "PIGP encodes a subunit of the enzyme that catalyzes the first step of GPI anchor biosynthesis."] — subunit, first step.

## Localisation
ER membrane. UniProt subcellular location is generic "Membrane; Multi-pass membrane
protein" but the GPI-GnT complex is an ER membrane complex; ComplexPortal IDA
(PMID:16162815) places PIGP at the ER membrane (GO:0005789). IBA is to ER (GO:0005783).
Reactome TAS also ER membrane.

## Disease
Biallelic (compound het) PIGP variants cause **Developmental and epileptic encephalopathy 55
(DEE55 / MIM:617599)**, an autosomal-recessive inherited GPI-deficiency (IGD). Patient cells
show reduced PIGP mRNA and reduced GPI-anchored surface proteins, rescued by WT PIGP.
- [PMID:28334793 abstract, "cells showed reduced PIGP mRNA levels, and an associated reduction of GPI-anchored cell surface proteins, which was rescued by exogenous expression of wild-type PIGP."]

## Annotation decisions summary
- GPI anchor biosynthetic process (GO:0006506) — core BP. IBA/IEA/IDA/IMP all ACCEPT.
- GPI-GnT complex (GO:0000506, part_of) — core CC. IPI/IDA ACCEPT.
- ER (GO:0005783 IBA) / ER membrane (GO:0005789 IDA, TAS) — ACCEPT; ER membrane is the more precise, correct location.
- membrane (GO:0016020 IEA) — correct but generic; KEEP_AS_NON_CORE (subsumed by ER membrane).
- phosphatidylinositol N-acetylglucosaminyltransferase activity (GO:0017176):
  - IEA (InterPro GO_REF:0000002, enables) — PIGP is a NON-catalytic subunit; assigning the
    catalytic MF via "enables" to the accessory subunit is an over-annotation of the whole-complex
    activity onto a single non-catalytic subunit. MARK_AS_OVER_ANNOTATED (do not REMOVE per policy on IEA vs. the correct complex-level activity residing in PIGA).
  - IDA (PMID:10944123, contributes_to) — the `contributes_to` qualifier is exactly the correct
    way to record a non-catalytic subunit's participation in the complex's catalytic activity. ACCEPT.
- protein binding (GO:0005515 IPI) x several:
  - PMID:10944123 (with PIGA P37287) and PMID:16162815 (with PIGA P37287) — these are the
    functionally meaningful GPI-GnT complex interactions. Bare `protein binding` is
    uninformative; MARK_AS_OVER_ANNOTATED (functional content captured by GPI-GnT complex part_of + GO:0017176 contributes_to). Not REMOVE (experimental IPI).
  - PMID:32296183 (binary interactome / HuRI), PMID:32814053 (ND interactome), PMID:33961781
    (BioPlex) — high-throughput proteome-scale screens; bare `protein binding`, uninformative,
    many partners are unrelated membrane proteins (ITGAM, KLF11, PLP1, etc.). MARK_AS_OVER_ANNOTATED.

No catalytic activity should be invented for PIGP itself; GOA carries GO:0017176 only via
IEA(enables, over-annotated) and IDA(contributes_to, correct). core_functions therefore
records BP + complex + location, and the MF only as contributes_to (GO:0017176) — not as an
`enables`/`molecular_function` claim for PIGP alone.
