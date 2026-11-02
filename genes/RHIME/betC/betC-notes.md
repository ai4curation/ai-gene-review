# betC (O69787) notes: Sinorhizobium meliloti 1021 choline sulfatase

Reviewed for the `bacterial_choline_o_sulfate_uptake_and_desulfation` module, where
O69787 is the experimentally characterized BetC exemplar.

## Evidence

- betC is in the betICBA operon and encodes a choline sulfatase acting on
  choline-O-sulfate and, more slowly, phosphorylcholine [PMID:9736747 "a new gene
  (betC) was identified as encoding a choline sulfatase catalyzing the conversion of
  choline-O-sulfate and, at a lower rate, phosphorylcholine, into choline."].
- Genetic requirement: [PMID:9736747 "Choline sulfatase activity was absent from betC
  but not from betB mutants"].
- Physiology: choline-O-sulfate is converted to glycine betaine and can serve as a
  sole C, N and S source [PMID:9736747 "S. meliloti also can use this compound as the
  sole carbon, nitrogen, and sulfur source for growth and that depends on a functional
  bet locus."].
- Purified enzyme kinetics and structure [PMID:29458126 "Sinorhizobium meliloti choline
  sulfatase (SmCS) efficiently catalyzes the hydrolysis of alkyl sulfate
  choline-O-sulfate"]; the active-site numbering (Cys54/fGly54, His104) matches the
  O69787 ACT_SITE features [PMID:29458126 "The nucleophile (Cys54/fGly54) is
  coordinated to His104 and the metal ion."].
- The paper's abstract-level kinetics give kcat/KM 4.8e3 s-1 M-1 for
  choline-O-sulfate vs 12 s-1 M-1 for 4-nitrophenyl sulfate (about 400-fold).

## Decisions

- GO:0047753 choline-sulfatase activity: ACCEPT (core).
- GO:0008484 sulfuric ester hydrolase activity: MODIFY to GO:0047753 (correct but
  general; same treatment as the KT2440 BetC sibling Q88RQ2).
- GO:0042425 choline biosynthetic process (UniPathway): KEEP_AS_NON_CORE. The GO
  definition ("formation of choline") is satisfied, there is no more specific
  choline-O-sulfate catabolism term, but the step is desulfation of an exogenous ester.
- GO:0005737 cytoplasm (TreeGrafter): KEEP_AS_NON_CORE.

## Deep research

`just deep-research RHIME betC --provider openscientist` was run on 2026-11-02 and
produced `betC-deep-research-openscientist.md`. Its identity checks, CXPXR motif
location (C54) and no-TM hydropathy scan agree with the UniProt record. It incorrectly
states "Although BetC itself has not been crystallized"; PMID:29458126 reports the
2.8-Angstrom SmCS structure. Recorded as LOW_QUALITY in the review's reference_review.
