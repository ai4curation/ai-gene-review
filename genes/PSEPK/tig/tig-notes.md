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
- MF: peptidyl-prolyl cis-trans isomerase activity (GO:0003755); ribosome binding (GO:0043022); protein folding chaperone (GO:0044183).
- BP: protein folding (GO:0006457), specifically 'de novo' cotranslational protein folding (GO:0051083) at the ribosomal exit tunnel.
- CC: cytoplasm (GO:0005737), ribosome-associated.

## Annotation review notes
- GO:0015031 protein transport / "Involved in protein export": The UniRule/HAMAP function line states "Involved in protein export," reflecting trigger factor's historical/general chaperone role and possible role in delivering/holding substrates. In bacteria TF is primarily a cytosolic co-translational folding chaperone; the dedicated export holdase role is SecB's. This is a broad/peripheral, homology-only annotation, not the core function — best kept as non-core.
- GO:0043335 protein unfolding (TreeGrafter): TF maintains nascent chains in an open, folding-competent conformation but is not an ATP-dependent unfoldase or disaggregase. "Protein unfolding" therefore mischaracterizes the activity and is removed; the existing GO:0044183 protein-folding-chaperone MF captures the supported activity. [UniProt "Acts as a chaperone by maintaining the newly synthesized protein in an open conformation."]
- GO:0006457 protein folding is correct but broad; the specific child 'de novo' cotranslational protein folding (GO:0051083) is also annotated and is more informative for TF.

## 2026-08-29 qualifier-aware re-review

- Reconciled all 8 current physical GOA signatures exactly once: 3 `enables`, 4 `involved_in`, and 1 `located_in`. All are IEA; there are no IBA annotations.
- The four TreeGrafter rows cite `PANTHER:PTN002412671`. Current cached PAINT for family PTHR30560 instead places the corresponding IBD assertions at `PANTHER:PTN001254607`, seeded by E. coli trigger factor UniProtKB:P0A850 (plus two additional experimental sources for PPIase). This is recorded as provenance/node-version drift, not treated as an IBA review, because the physical Q88KJ1 rows are TreeGrafter IEA rather than GO_Central IBA. [file:interpro/panther/PTHR30560/PTHR30560-paint.tsv]
- Removed the author-supplied synthetic GO:0051082 row. Live/project ontology guidance records GO:0051082 as obsolete. Trigger factor binds emerging chains in situ and no defined escort destination or acceptor is asserted, so carrier-specific GO:0140309 does not fit. Unlike a pure holdase, however, trigger factor supports productive protein folding, and the current physical GO:0044183 protein folding chaperone annotation already captures that function; retaining an obsolete interim binding claim is unnecessary. [file:projects/UNFOLDED_PROTEIN_BINDING.md]
- GO:0003755 PPIase is retained as a distinct catalytic core activity, while GO:0043022 ribosome binding and GO:0044183 protein folding chaperone describe the positioning and chaperone activities underlying GO:0051083 cotranslational folding. The organism-specific record remains homology-based (PE 3); no cached P. putida Tig functional paper was available, so the review does not claim direct P. putida experimental confirmation. [file:PSEPK/tig/tig-uniprot.txt]
