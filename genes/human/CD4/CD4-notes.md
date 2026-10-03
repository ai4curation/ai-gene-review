# CD4 curation notes

Human CD4 (UniProt P01730), reviewed for the ADAPTIVE_IMMUNITY project (T cell receptor
trunk). 161 existing GOA rows plus one proposed new row.

## What CD4 does

- **MHC class II coreceptor.** The membrane-distal D1 immunoglobulin-like domain binds a
  non-polymorphic concavity formed by the alpha-2 and beta-2 domains of class II molecules,
  with CD4 Phe43 inserting into the pocket [PMID:11535811 "The CD4 Phe-43 side chain extends
  into a hydrophobic concavity formed by MHC residues from both alpha 2 and beta 2 domains."];
  the atomic description of the invariant HLA-DR, -DP and -DQ residues targeted comes from the
  affinity-matured CD4-HLA-DR1 structure [PMID:21900604 "CD4 recognizes HLA-DR1 through its
  membrane-distal D1 domain, which contacts the membrane-proximal alpha2 and beta2 domains of
  the MHC class II molecule"]. The founding functional evidence is adhesion of CD4-expressing
  cells to class II-positive B cells [PMID:2823150 "Thus, the CD4 protein, even in the absence
  of T-cell receptor-antigen interactions, can interact directly with class II antigens to
  function as a cell surface adhesion molecule."].
- **The affinity is extraordinarily low**, which is the mechanistically important point:
  [PMID:27114505 "to measure the 2D K d for the CD4/pMHC II interaction, which proves to the
  best of our knowledge to be the weakest such interaction ever studied"]. CD4 therefore works
  by being co-recruited to a pMHCII that the TCR already holds, not by independent ligation.
  Consistent with this, the ternary model from the CD4-pMHCII structure excludes a direct
  CD4-TCR contact [PMID:11535811 "This configuration excludes a direct TCR-CD4 interaction and
  suggests how TCR and CD4 signaling is coordinated around the antigenic pMHCII complex."].
- **Zinc clasp delivery of LCK.** Two cysteines in the CD4 cytoplasmic tail and two in the LCK
  unique region co-coordinate one Zn2+ ion [PMID:9668045 "Biochemical and biophysical
  experiments show that the complex dissociates in the presence of EDTA and that it contains a
  single Zn2+ ion."]; the solution structures show the two tails are unstructured alone and
  cofold around the metal [PMID:14500983 "The coreceptor tails and the Lck N-terminus are
  unstructured in isolation but assemble in the presence of zinc to form compactly folded
  heterodimeric domains."]. The same work notes that LCK binding masks the CD4 dileucine
  endocytosis motif [PMID:14500983 "A dileucine motif required for clathrin-mediated
  endocytosis of CD4 is masked by Lck."]. A large fraction of cellular LCK co-precipitates with
  CD4/CD8 [PMID:3262426 "a large fraction of the total cellular lck protein can be
  coimmunoprecipitated with these surface glycoproteins"].
- **Raft localization and synapse organisation.** Palmitoylation of Cys396/Cys399 plus LCK
  association enrich CD4 in rafts [PMID:12517957 "By mutagenesis, we demonstrated that the
  palmitoylation of the membrane-proximal Cys(396) and Cys(399)of CD4, and the association of
  CD4 with Lck contribute to the enrichment of CD4 in lipid rafts."], and raft-localized CD4 is
  what enhances receptor tyrosine phosphorylation [PMID:12517957 "The localization of CD4 in
  lipid rafts also correlates to the ability of CD4 to enhance receptor tyrosine
  phosphorylation."]. CD4 is required for TCR/PKC-theta clustering at the synapse, and the
  palmitoylation sequences are needed for it [PMID:15128768 "Specifically, we demonstrate that
  CD4 palmitoylation sequences are required for TCR/PKCtheta raft association and subsequent
  clustering, indicating a particular role for raft-associated CD4 molecules in regulating
  immune synapse organization."].
- **Dimerization.** D4-mediated homodimers are seen crystallographically and in solution
  [PMID:9168119 "a common dimeric association through D4 domains"] and mapped to K318/Q344,
  where they are required for coreceptor function [PMID:12444132 "we demonstrate that dimer
  formation is essential for the coligand and coreceptor functions of CD4 in T cell
  activation."]. The dominant-negative F43I experiment separates the two ligands neatly:
  oligomerization is needed for class II binding but not for gp120 [PMID:7604010 "Expression of
  F43I results in a dominant negative effect: no class II MHC binding is observed even though
  wtCD4 expression is preserved."].
- **Development and output.** The CD4 tail/TM region delivers the lineage-directing signal
  [PMID:1533274 "Here we show that the CD4 transmembrane region and/or cytoplasmic tail
  mediates the delivery of a specific signal that directs differentiation of T cells to a CD4
  lineage."]; CD4 surface level sets the avidity threshold for thymic selection
  [PMID:9551897 "CD4 plays a crucial role in determining this avidity"]; and the tail is what
  potentiates IL-2 secretion when CD4 and the TCR see the same MHC molecule [PMID:1901411].
- **Non-T-cell role (human-specific).** MHC class II ligation of CD4 on human blood monocytes
  triggers macrophage differentiation [PMID:24942581 "the activation of CD4 via interaction
  with major histocompatibility complex class II (MHC-II) triggers cytokine expression and the
  differentiation of human monocytes into functional mature macrophages"], MAPK- and Src-kinase
  dependent. Mouse monocytes do not express CD4, so this is a place to be careful with
  cross-species propagation.
- **Human loss of function.** A homozygous splice variant abolishing CD4 expression causes
  recalcitrant HPV warts with double-negative T cells substituting for the CD4+ compartment
  [PMID:31781092].
- **HIV-1 receptor.** CD4 binds gp120 at the same D1 surface and induces the conformational
  change that creates the coreceptor site [PMID:9641677; PMID:20080564 "Binding of the initial
  receptor, CD4, induces changes in gp120 conformation that allow high-affinity interaction
  with the coreceptor, CCR5 or CXCR4"]. Treated as a real but non-physiological function:
  GO:0001618 and GO:0046718 are kept as non-core, per the project's convention that virus
  receptor terms are legitimate but not core T cell biology, and the rows where a viral protein
  (Nef, Vpu) targets CD4 get no molecular function on the host side.

## Curation calls worth recording

- **Generic `protein binding` (21 rows).** gp120 rows -> GO:0001618; HLA-DR rows ->
  GO:0023026; LCK rows -> GO:1990782. Removed: CCR5 co-IP rows (x3), Nef/Vpu rows (x3,
  host-as-target), ACP33/SPG21, NR3C1, PLSCR4, the two Y2H interactome hits (LAMP2, SH3GLB1)
  and CD81.
- **GO:0005201 extracellular matrix structural constituent (NAS)** removed: CD4 is a type I
  membrane protein and the cited paper is about CD4 dimers in T cell activation.
- **GO:0019865 immunoglobulin binding (IEA from rat)** removed: CD4 is built from Ig-like
  domains and binds Ig-superfamily ligands, which is not binding an immunoglobulin.
- **GO:0005788 ER lumen (IEA from rat)** removed; the ER membrane rows are kept as non-core
  (biosynthesis, gp160 sequestration, Vpu-driven ERAD).
- **GO:0042101 T cell receptor complex (NAS, part_of)** marked over-annotated: CD4 is a
  separate coreceptor, not a stoichiometric subunit, and the structural model excludes a direct
  CD4-TCR contact.
- **IL-16 rows left UNDECIDED** (GO:0042011, GO:0042012). PMID:1673145 shows CD4-dependent
  calcium/IP3 signaling by IL-16 and a reported sub-nanomolar affinity; PMID:27231345 detected
  no interaction between mature IL-16 and the CD4 ectodomain by NMR, nor on CD4-expressing
  cells [PMID:27231345 "Attempts to directly or indirectly observe hIL-16 binding to cell lines
  expressing CD4 by flow cytometry also detected no interaction between CD4 and hIL-16"], and
  suggests multimeric IL-16 as the reconciliation. The two downstream NAS rows that depend on
  the IL-16 story (GO:0030595 leukocyte chemotaxis, cited to PMID:27231345 itself, and
  GO:0050729 positive regulation of inflammatory response, cited to the caspase-3 processing
  paper PMID:9422780) are removed.
- **GO:0035723 IL-15-mediated signaling (IDA + IBA)** left UNDECIDED: the cited reference is
  the monocyte CD4-ligation paper, cached abstract-only, which does not mention IL-15; CD4 is
  not part of the IL-15 receptor. GO:0097011 (GM-CSF response, same reference) likewise
  UNDECIDED.
- **Response-to-chemical rows from rat orthology** (estradiol, vitamin D, ethanol,
  methamphetamine, ionomycin) marked over-annotated: these track CD4 expression or CD4+ cell
  numbers after treatment, not a step CD4 performs.
- **GO:0045121 membrane raft** modified to GO:0044853 plasma membrane raft on all three rows
  (keeping the action consistent across evidence types), matching the CD8A review.
- **GO:0032507 maintenance of protein location in cell** modified to GO:0001771 immunological
  synapse formation, which is what PMID:15128768 actually shows.
- **One NEW row**: GO:0001772 immunological synapse (CC). CD4 is a constituent of the clustered
  structure, not merely required for it: it is co-recruited with the TCR to pMHCII on the
  opposing cell and supplies LCK there.
- **Knockout/transgenic phenotypes kept non-core** per project rule 3: T cell differentiation,
  T cell selection, macrophage/monocyte differentiation, IL-2 production, T cell proliferation,
  calcium transport.
- **Consistency with LCK**: GO:1990782 protein tyrosine kinase binding on CD4 is the mirror of
  GO:0042609 CD4 receptor binding on LCK (ACCEPTed there, with the same zinc-clasp rationale).

## Deep research integration (falcon)

Pending at the time the annotation review was written; see the section appended below.
