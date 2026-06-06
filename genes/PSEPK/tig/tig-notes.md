# tig (Trigger factor) — Pseudomonas putida KT2440 (PSEPK)

UniProt: Q88KJ1 (TIG_PSEPK); gene `tig`; OrderedLocusName PP_2299; 437 AA.
Evidence level: PE 3 (Inferred from homology). Annotations are HAMAP-Rule (MF_00303) / UniRule / TreeGrafter-based; no organism-specific functional publication exists for this protein (only the genome paper PMID:12534463).

## FUNCTION
Trigger factor (TF) is the ribosome-associated molecular chaperone that is the first chaperone to contact nascent polypeptides emerging from the ribosomal exit tunnel, promoting co-translational folding. It also has peptidyl-prolyl cis-trans isomerase (PPIase, FKBP-type) activity.

- [UniProt "Involved in protein export. Acts as a chaperone by maintaining the newly synthesized protein in an open conformation. Functions as a peptidyl-prolyl cis-trans isomerase."]
- EC 5.2.1.8; catalyzes interconversion of peptidylproline (omega=180) and peptidylproline (omega=0):
  [UniProt "Reaction=[protein]-peptidylproline (omega=180) = [protein]-peptidylproline (omega=0)"]
- Belongs to the FKBP-type PPIase family, Tig subfamily:
  [UniProt "Belongs to the FKBP-type PPIase family. Tig subfamily."]

## DOMAIN architecture
Three-domain organization, each with a distinct activity:
- [UniProt "Consists of 3 domains; the N-terminus binds the ribosome, the middle domain has PPIase activity, while the C-terminus has intrinsic chaperone activity on its own."]
- PPIase FKBP-type domain mapped to residues 161..246:
  [UniProt "DOMAIN          161..246" / "PPIase FKBP-type"]

## SUBUNIT / ribosome association
About half of TF is bound to the ribosome near the polypeptide exit tunnel; the rest is free in the cytoplasm. The N-terminal domain mediates ribosome binding.
- [UniProt "About half TF is bound to the ribosome near the polypeptide exit tunnel while the other half is free in the cytoplasm."]

## SUBCELLULAR LOCATION
Cytoplasm.
- [UniProt "SUBCELLULAR LOCATION: Cytoplasm."]

## Core function synthesis
- MF: peptidyl-prolyl cis-trans isomerase activity (GO:0003755); ribosome binding (GO:0043022); protein folding chaperone / holdase / unfolded protein binding (GO:0044183).
- BP: protein folding (GO:0006457), specifically 'de novo' cotranslational protein folding (GO:0051083) at the ribosomal exit tunnel.
- CC: cytoplasm (GO:0005737), ribosome-associated.

## Annotation review notes
- GO:0015031 protein transport / "Involved in protein export": The UniRule/HAMAP function line states "Involved in protein export," reflecting trigger factor's historical/general chaperone role and possible role in delivering/holding substrates. In bacteria TF is primarily a cytosolic co-translational folding chaperone; the dedicated export holdase role is SecB's. This is a broad/peripheral, homology-only annotation, not the core function — best kept as non-core.
- GO:0043335 protein unfolding (TreeGrafter): TF is a holdase/foldase chaperone, not a disaggregase/unfoldase like ClpB. "Protein unfolding" mischaracterizes the activity; the holdase activity is better captured by "protein folding chaperone" (GO:0044183) / unfolded protein binding. Marked as over-annotation / better modeled by the chaperone MF term.
- GO:0006457 protein folding is correct but broad; the specific child 'de novo' cotranslational protein folding (GO:0051083) is also annotated and is more informative for TF.
