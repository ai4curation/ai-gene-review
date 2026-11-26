# ubiD (PP_5213, Q88CG8) - Pseudomonas putida KT2440 - curation notes

## 2026-11-11 audit (ubiquinone_biosynthesis module)

No Perplexity/Falcon/OpenAI deep research available (no provider keys); OpenScientist report
read critically. Evidence: reviewed UniProt entry (HAMAP MF_01636) and E. coli/yeast UbiD-UbiX
literature. No KT2440 experiment.

- Two-component system: [PMID:25647642 "Our results suggest that UbiX and UbiD constitute a
  similar two-component decarboxylase system and that the same flavin-based cofactor is
  necessary for the biosynthesis of ubiquinone."]
- E. coli genetics: [PMID:17889824 "both UbiX and UbiD are required for the decarboxylation of
  4-hydroxy-3-octaprenyl-benzoate"]
- Not in the Ubi metabolon: [PMID:30686758 "seven Ubi proteins form the Ubi complex"] - the
  seven are UbiE/F/G/H/I/J/K. The OpenScientist report's statement that UbiD works within the
  soluble metabolon is unsupported (reference_review LOW_QUALITY).
- PAINT PTHR30108: root PTN000764648 GO:0005737, GO:0016831; bacterial UbiD node PTN000764659
  GO:0005829, GO:0008694, GO:0006744 (seed E. coli P0AAB4).
- Decisions: GO:0008694, GO:0006744, GO:0005886 ACCEPT; GO:0016831 MODIFY to GO:0008694;
  cytoplasm MODIFY to cytosol; cytosol KEEP_AS_NON_CORE (peripheral-membrane enzyme with a
  plausible soluble pool).

Module agreement: `polyprenyl_hydroxybenzoate_decarboxylase_activity` (GO:0008694); module
gives no location, review uses plasma membrane (HAMAP).
