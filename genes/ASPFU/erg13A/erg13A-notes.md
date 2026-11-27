# erg13A review notes

- Falcon deep-research failed because agentapi was unavailable, so no
  provider-generated deep-research file was available for this compact review.
- Q4WBQ3 is the A. fumigatus Af293 erg13A member of PTHR43323:SF2. The same
  Af293 genome also has erg13B/Q4WXT8 in PTHR43323:SF2, so the A. fumigatus
  mevalonate-pathway HMG-CoA synthase step is duplicated. The local PTHR43323
  review treats PTN000222418 as the inherited HMG-CoA synthase / mevalonate node
  and PTN000933803 as the fungal ergosterol node.
- UniProt describes the direct Erg13A reaction as condensation of acetyl-CoA and
  acetoacetyl-CoA to form HMG-CoA, and also curates the Rhea/EC reaction for
  `RHEA:10188` / `EC:2.3.3.10`.
- The UniProt ISS row uses `UniProtKB:P41338` as the similarity donor, but that
  accession is yeast ERG10 acetyl-CoA acetyltransferase in PTHR18919 rather than
  the HMG-CoA synthase ERG13/P54839 in PTHR43323:SF2. The ISS row's GO term is
  still correct for erg13A, but the `WITH/FROM` needs to be re-pointed.
- Yasmin et al. 2012 place mevalonate at the branch point between A. fumigatus
  ergosterol and nonsterol isoprenoid metabolism:
  [PMID:22106303, "Mevalonate is a key metabolite in the biosynthesis of
  sterols such as fungal ergosterol and a variety of nonsterol isoprenoid
  derivatives"].
- Q4WBQ3 retains the HMG-CoA synthase PROSITE and PANTHER signatures, the
  expected predicted catalytic Glu/Cys/His residues, and HMG-CoA binding
  residues, arguing against loss of catalytic activity.
- All three `GO:0004421` rows were accepted, while recording the wrong
  `UniProtKB:P41338` donor on the ISS row as a UniProt source defect. Both
  `GO:0006084` rows were kept as peripheral acetyl-CoA metabolism annotations.
  The `GO:0008299` row was modified to `GO:0019287` to capture the direct
  mevalonate-pathway isopentenyl-diphosphate synthesis branch. The generic
  `GO:0016746` acyltransferase row was marked `TOO_GENERAL` because the specific
  HMG-CoA synthase activity is already accepted.
- The available cached evidence does not establish the relative flux carried by
  erg13A and erg13B in vivo, or whether the two same-subfamily paralogs are
  redundant or condition-biased during TAFC-inducing iron starvation.
