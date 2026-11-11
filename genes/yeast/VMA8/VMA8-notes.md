# VMA8 manual notes

## Functional synthesis

- VMA8 encodes subunit D of the yeast V-type ATPase V1 sector. The original
  biochemical identification matched tryptic peptides from the isolated
  vacuolar proton-translocating ATPase to ORF11/VMA8, and vma8 deletion
  abolished vacuolar membrane V-ATPase activity while leaving Vo subunits stable
  in the membrane [PMID:7797485, "Vacuolar membranes isolated from vma8 delta
  yeast cells exhibited no V-ATPase activity"].
- Vma8/D is part of the central rotor that couples ATP hydrolysis in V1 to
  proton translocation through Vo, not an independently catalytic ATPase.
  VMA8 point mutants that retained near-normal subunit levels and assembly
  reduced both proton transport and concanamycin-sensitive ATPase activity, with
  M221V and V71D/E220V specifically uncoupling transport from ATP hydrolysis
  [PMID:10801866, "significant uncoupling of proton transport and ATPase
  activity"].
- Structural work directly places the D subunit in the V1 rotor. The 2015
  cryo-EM V1Vo structures captured three rotational states of yeast V-ATPase
  [PMID:25971514, "three rotational states of the V-ATPase from the yeast
  Saccharomyces cerevisiae"], and the 2016 autoinhibited V1 crystal structure
  describes D as the central rotor shaft [PMID:27295975, "The central rotor
  subunit D is an elongated coiled-coil folded as a hairpin"].
- Vma8 is shared by Vph1- and Stv1-containing V-ATPases. Vph1 marks the
  vacuolar enzyme, while Stv1 targets a lower-activity but still fully coupled
  isoform to the Golgi apparatus and endosomes [PMID:30910982, "Stv1p, which is
  targeted to the Golgi apparatus and endosomes"].
- The 2024 RAVE:V1 partial-complex structure is useful context for assembly and
  reassembly of the Vma8-containing V1 sector: RAVE binds V1 after dissociation
  and its structure appears to capture a snapshot before subunit H inhibition is
  released and subunit C/Vo reassembly is completed [PMID:39625975, "Therefore,
  the structure likely presents just one snapshot in the process of RAVE-mediated
  V-ATPase reassembly"].

## Annotation decisions

- Accepted the PTHR11671 IBA rows as curated PAINT node calls. In particular,
  PTN000912657 is the fungal IBD node for fungal-type vacuole membrane and
  vacuolar V-type ATPase complex; it is seeded by S. cerevisiae VMA8 rather
  than being a weak pairwise transfer.
- Kept the starvation-induced vacuolar membrane raft localization as
  non-core. The Toulmay and Prinz paper supports partitioning of tested
  vacuolar membrane proteins into vacuolar lipid domains in stationary phase,
  but this is a context-specific sublocalization of Vma8's vacuolar pool rather
  than its central function.
- Removed all GO:0005515 protein binding rows. The RAV1/RAVE row and the
  Vma6/Vma7/Vph1 co-complex rows may reflect real physical proximity or
  co-purification, but generic protein binding does not describe Vma8's
  molecular role; the specific assertions are V-ATPase complex membership,
  contribution to rotary proton ATPase activity, and participation in proton
  transmembrane transport.
- Marked the two GO:0046961 rows whose qualifier is `enables` as
  `MARK_AS_OVER_ANNOTATED`. Vma8 contributes to the V-ATPase holoenzyme
  activity as a rotor subunit, but isolated Vma8 does not catalyze
  proton-transporting ATP hydrolysis; the IBA and IMP `contributes_to` rows
  retain the correct complex-level MF.
- Did not add NEW rows. The existing GOA set already covers V1 membership,
  vacuolar/Golgi V-type ATPase complex membership at the available GO
  granularity, rotary proton ATPase contribution, proton transport, and
  vacuolar/Golgi/endosomal acidification.
