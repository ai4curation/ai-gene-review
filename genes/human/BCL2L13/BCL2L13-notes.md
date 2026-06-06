# BCL2L13 (Bcl-rambo / Mil1) curation notes

UniProt: Q9BXK5 (B2L13_HUMAN). Synonyms: Bcl-rambo, Mil1, BCL2L13, ORFNames=CD003.
485 aa (canonical isoform 2 displayed, Q9BXK5-1). Single-pass tail-anchored membrane protein
(FT TRANSMEM 460..480). Contains BH4 (14..30), BH3 (100..116), BH1 (147..157), BH2 (193..206)
motifs, plus a unique ~250 aa insertion with two tandem repeats (A, B) preceding the C-terminal
transmembrane anchor.

## Core function synthesis

BCL2L13/Bcl-rambo is a mitochondrial outer-membrane (tail-anchored) BCL-2-family protein. The two
best-established, distinct activities reported in the literature are:

1. **Mitophagy receptor** — BCL2L13 is the mammalian functional homolog of yeast Atg32. It carries a
   WXXL-type LIR (LC3-interacting region) and binds LC3/GABARAP-family proteins to recruit the
   autophagy machinery to mitochondria, inducing mitochondrial fragmentation and mitophagy. The
   foundational study (Murakawa et al., Nat Commun 2015, PMID:26471991) is NOT among the GOA-cited
   references and is NOT cached in this repo, so it cannot be used for verbatim supporting_text;
   however, the UniProt IntAct interaction table directly records BCL2L13 binding to the human Atg8
   ortholog GABARAPL2 (P60520), consistent with the LIR-dependent receptor model.
   [file:human/BCL2L13/BCL2L13-uniprot.txt "Q9BXK5; P60520: GABARAPL2; NbExp=4; IntAct=EBI-747430, EBI-720116;"]
   UniProt/Ensembl GOA also carries GO:0000423 mitophagy (IEA:Ensembl) and GO:0007005 mitochondrion
   organization (IEA:Ensembl), reflecting this role, though these specific terms are not in the
   seeded existing_annotations set.
   [file:human/BCL2L13/BCL2L13-uniprot.txt "GO:0000423; P:mitophagy; IEA:Ensembl."]

2. **Apoptosis (original characterization)** — Bcl-rambo was first described as a pro-apoptotic
   BCL-2 homolog whose cell-death activity is induced by its membrane-anchored C-terminal domain
   (the unique insertion + TM), NOT by its BH motifs, and is blocked by caspase inhibitors/IAPs but
   not by Bcl-xL. Notably it does NOT heterodimerize with other BCL-2-family members.
   [PMID:11262395 "Bcl-rambo was localized to mitochondria, and its overexpression induces apoptosis that is specifically blocked by the caspase inhibitors, IAPs, whereas inhibitors controlling upstream events of either the 'death receptor' (FLIP, FADD-DN) or the 'mitochondrial' pro-apoptotic pathway (Bcl-x(L)) had no effect."]
   [PMID:11262395 "No interaction of Bcl-rambo with either anti-apoptotic (Bcl-2, Bcl-x(L), Bcl-w, A1, MCL-1, E1B-19K, and BHRF1) or pro-apoptotic (Bax, Bak, Bik, Bid, Bim, and Bad) members of the Bcl-2 family was observed."]
   [PMID:11262395 "Bcl-rambo constitutes a novel type of pro-apoptotic Bcl-2 member that triggers cell death independently of its BH motifs."]

The apoptosis function is the basis of the GOA NAS annotations (PMID:11262395): apoptotic process
(GO:0006915), mitochondrion (GO:0005739), cysteine-type endopeptidase activator activity involved
in apoptotic process (GO:0008656, i.e. caspase-3 activation), and membrane (GO:0016020, IDA).
UniProt FUNCTION: "May promote the activation of caspase-3 and apoptosis."
[file:human/BCL2L13/BCL2L13-uniprot.txt "FUNCTION: May promote the activation of caspase-3 and apoptosis."]

The original overexpression-driven apoptosis phenotype is the historical view; the more recent and
mechanistically distinct mitophagy-receptor role (Atg32 homolog) is now regarded as a central,
conserved function. Distinguishing CORE (mitophagy receptor / mitochondrial fragmentation) from the
context-dependent apoptosis annotations is the main curation task.

## Legionella SidF (apoptosis inhibition by pathogen)

Legionella pneumophila effector SidF specifically interacts with and neutralizes BNIP3 and Bcl-rambo
to inhibit host macrophage apoptosis, confirming Bcl-rambo as a genuine pro-death host protein and a
pathogen target. UniProt IntAct records Q9BXK5-sidF (Q5ZSD5, Xeno).
[PMID:17360363 "SidF contributes to apoptosis resistance in L. pneumophila-infected cells by specifically interacting with and neutralizing the effects of BNIP3 and Bcl-rambo, two proapoptotic members of Bcl2 protein family."]
[PMID:17360363 "binding of SidF to Bcl-rambo can be detected under various conditions, including in cells in which SidF is delivered directly from the bacterium"]
The seeded GO:0005515 protein binding IPI from PMID:17360363 corresponds to this SidF interaction;
as bare protein binding it is uninformative and is marked over-annotated.

## Localization

UniProt: Isoform 2 (canonical, Q9BXK5-1): Mitochondrion membrane; Single-pass membrane protein;
Nucleus. Isoform 1 (Q9BXK5-2, a short 201-aa form): Nucleus.
[file:human/BCL2L13/BCL2L13-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]: Mitochondrion membrane"]
Mitochondrial (outer) membrane is the core functional location. The Nucleus localization is reported
(largely for the truncated isoform 1, which lacks the TM anchor) and is secondary; isoform 1
(Q9BXK5-2) ends at residue 201 (VSP_000526/VSP_000527) and is nuclear.

## Protein binding annotations

Many GO:0005515 protein binding IPI annotations derive from high-throughput interactome papers
(16189514, 25416956, 25910212, 26871637, 28514442, 32296183, 32814053, 33961781) plus the specific
SidF study (17360363). The UniProt IntAct table is dominated by membrane-protein partners (many
single-pass TM proteins, e.g. PLN, MAL, PLP1, VAMP3/4, syntaxins), consistent with a
membrane-embedded tail-anchored protein; most are not functionally informative. "protein binding"
is uninformative and marked over-annotated. The functionally meaningful interaction is with the
Atg8-family protein GABARAPL2 (mitophagy receptor activity), but that is recorded as an IntAct hit,
not among the seeded protein-binding annotations with a cached PMID.

## Key existing annotation classification summary

CORE (mitophagy receptor / mitochondrial fragmentation): mitochondrion (GO:0005739) localization,
membrane (better as mitochondrial outer membrane). NOTE: the defining mitophagy MF/BP terms are not
in the seeded set (they exist in UniProt GOA as IEA: GO:0000423 mitophagy, GO:0007005 mitochondrion
organization) — proposed as new/expanded annotation.

SECONDARY / NON-CORE: apoptotic process, regulation of apoptotic process, caspase-3 activator
activity (GO:0008656), nucleus localization.

OVER-ANNOTATED / UNINFORMATIVE: protein binding (GO:0005515) — all instances.

## Caveat

The strongest evidence for the mitophagy-receptor / Atg32-homolog function (Murakawa et al. 2015)
is not in the cached publications, so verbatim supporting_text for that function is drawn only from
the UniProt record (GABARAPL2 IntAct interaction; GO:0000423 mitophagy IEA) and is reflected in the
description, core_functions, and proposed_new_terms rather than asserted from an inaccessible PMID.
