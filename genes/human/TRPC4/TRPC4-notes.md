# TRPC4 review notes

Automated Falcon and Perplexity deep-research providers were unavailable in this
environment, so no provider-named deep-research file was created. These notes
were compiled manually from GOA, cached publications, the UniProt record, and
the 68d5ebd600001111 GO-CAM review.

## Channel function and complexes

- The core activity is receptor-operated, calcium-permeant nonselective cation
  channel activity at the plasma membrane. The earliest human TRPC4 paper found
  basal divalent cation permeability and a nonselective cation current in
  heterologous cells [PMID:11042129 "Whole-cell patch-clamp studies of hTRP4
  expressed in Chinese hamster ovary cells revealed a constitutively active
  non-selective cation current"], and the recent human TRPC1/TRPC4 cryo-EM paper
  showed a heteromer with one TRPC1 and three TRPC4 subunits [PMID:39478185
  "human TRPC1/TRPC4 heteromer in the apo and antagonist-bound states, both
  consisting of one TRPC1 subunit and three TRPC4 subunits"].
- TRPC1, TRPC4 and TRPC5 form related cation channel complexes. Older FRET and
  co-IP experiments showed TRPC1/TRPC4/TRPC5 assembly [PMID:12032305 "TRPC1 has
  the ability to form channel complexes together with TRPC4 and TRPC5"], and
  TRPC1-containing heteromers are functional receptor-operated channels
  [PMID:22157757 "TRPC1 was shown to form functional heteromeric,
  receptor-operated channel complexes with TRPC3, -4, -5, -6, and -7"].

## KISS1R/GnRH GO-CAM context

- GO-CAM 68d5ebd600001111 uses TRPC4 as the downstream cation channel whose
  activity drives membrane depolarization in GnRH neurons. That is plausible and
  consistent with accepted GO:0005261, GO:0051899 and GO:0005886 rows in this
  review, but the subunit identity remains inferred from mouse evidence. The
  2008 study detected several TRPC messages in single GnRH neurons, including
  TRPC4 [PMID:18434521 "TRPC4, TRPC5, TRPC6, and TRPC7 subunits were expressed
  in GnRH neurons"], and the 2013 study found TRPC4alpha mRNA and receptor-
  operated, cSrc-dependent kisspeptin activation in mouse GnRH neurons.
- The 2013 GnRH current is not a store-operated calcium entry context
  [PMID:23744639 "TRPC channels in GnRH neurons are receptor-operated, and
  kisspeptin activates TRPC channels through PIP(2) depletion and cSrc tyrosine
  kinase activation"]. Store-operated calcium channel rows were kept as
  non-core because the endothelial ISOC evidence supports that mode in another
  cell type.

## Regulatory partners

- The beta-catenin and VE-cadherin rows were kept as non-core regulatory
  interactions at endothelial junctions [PMID:19996314 "TRPC4 co-precipitated
  with the junctional proteins beta-catenin and VE-cadherin"].
- The SESTD1, MxA and protein 4.1 bare GO:0005515 rows were removed under the
  repository protein-binding policy. Their papers are still useful for complex
  regulation, but the bare parent term is not an informative MF assertion.
- The inositol 1,4,5-trisphosphate binding rows appear to conflate IP3 ligand
  binding with TRPC4's CIRB region, a calmodulin- and IP3-receptor-binding
  domain [PMID:20164195 "calmodulin- and inositol
  1,4,5-trisphosphate receptor-binding domain"].
