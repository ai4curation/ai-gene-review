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

The Falcon report (`file:human/CD4/CD4-deep-research-falcon.md`, Edison Scientific, 40
citations) arrived after the annotation review was written and was then sorted claim by claim.

**Adopted (traced to primary papers, now cached and quoted):**

- *Compact TCR-CD3-pMHCII-CD4 macrocomplex.* FRET between the CD4 and CD3-delta cytosolic
  juxtamembrane regions increases on concurrent engagement of the same agonist pMHC
  [PMID:27183595 "indicating that concurrent TCR and CD4 engagement of agonist pMHC positions
  CD3delta and CD4 in a cl"], and notably the clasp domain was replaced by the FRET probe, so
  the proximity is not an artefact of LCK-ITAM binding [PMID:27183595]. This strengthens the
  reasoning behind marking the `part_of` T cell receptor complex row over-annotated: ligand-
  induced proximity is not subunit membership.
- *Microvillar-tip localization.* [PMID:31001252 "CD4 accumulates at the tips of T-cell
  microvilli."] and the LCK dependence of that accumulation; added to the core coreceptor
  function and raised as a suggested question, since no GO term covers this sub-compartment.
- *Short isoform 2.* It retains D4, the TM segment and the LCK-binding tail but lacks the
  distal domains, so it binds LCK and enhances ZAP70 phosphorylation in vitro while being
  unable to bind HLA class II [PMID:38557723 "From a structural perspective, the lack of D1 and
  D2 domains prevents isoform 2 from directly binding HLA class II"]. Recorded in the
  description and as a suggested question about isoform-specific annotation.
- *Human inherited CD4 deficiency, 2024 cohort.* Seven patients from five families, no
  detectable CD4+ T cells, expanded helper-like double-negative TCR alpha-beta cells with
  reduced but real HLA-II-restricted responses [PMID:38557723]. This is a better primary source
  than the single-case report PMID:31781092 and both are now cited.
- *Macrophage recycling.* CD4 recycles constitutively in primary macrophages with roughly
  40-50% intracellular at steady state; added as support for keeping the early endosome rows
  non-core, with the proteomic source cached (PMID:21533244).
- *Framing checks the report gets right and that the review follows:* LCK is the kinase and CD4
  has no catalytic activity; CD4 is the primary HIV receptor while CCR5/CXCR4 are the entry
  coreceptors.

**Noted but not adopted as asserted:**

- The report cautions that stable CD4 oligomers and discrete lipid-raft localization "should
  not be treated as established universal requirements" in living cells. The review keeps both,
  because the raft claim rests on direct human-cell mutagenesis [PMID:12517957] and the
  dimerization claim on mapped point mutants plus structures [PMID:12444132, PMID:9168119,
  PMID:7604010]; the caveat is recorded here rather than weakening the annotations. It is a
  fair caution about mechanism, not a contradiction of the data.
- A mouse result quoted second-hand inside PMID:38557723 (that the CD4-LCK interaction was not
  required for commitment of class II-restricted thymocytes to the CD4 lineage) was not used:
  it is a secondary citation and would need the primary paper before it could bear on the
  lineage-commitment rows, which are non-core in any case.
- Clinical material (ibalizumab, UB-421, CD4 counts in advanced HIV disease, trial
  NCT02475629) is accurate but irrelevant to GO annotation and was left out.

**Report errors / weaknesses:** none that affect the review. The report gives no PMIDs, only
author-year keys and DOIs, so every adopted claim had to be resolved to a PMID by hand
(Guérin 2024 = PMID:38557723, Glassman 2016 = PMID:27183595, Glatzová 2019 = PMID:31001252,
Raposo 2011 = PMID:21533244, Jönsson 2016 = PMID:27114505, already cited by GOA). It leans
heavily on two sources (the Guérin cohort and the Glatzová review) and does not mention the
zinc clasp, the Phe43 contact, the D4 dimerization site, the IL-16 controversy or the human
monocyte/macrophage differentiation role -- all of which the GOA rows required and which were
sourced independently. Its statement that CD4 is "458 amino acids" is correct for the
precursor (UniProt P01730: 458 AA, signal peptide 1-25, mature chain 26-458). It also prints a sentence fragment
in one table cell (a truncated "in a cl..."), which is why the quote used here ends mid-word.
