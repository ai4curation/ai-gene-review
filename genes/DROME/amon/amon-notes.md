# amon (Q9VBC7) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files were consulted.

### Identity
- Q9VBC7 is the canonical, Swiss-Prot reviewed product of amon/CG6438 (FBgn0023179), 654 aa, PE 1. Not a fragment, isoform or alternative gene model.
- Architecture (UniProt): signal 1-21, propeptide 22-121, mature chain 122-654, peptidase S8 domain 158-483 with charge-relay triad D196/H237/S412, P-domain 491-627; no transmembrane segment. Soluble PC2 architecture.

### Evolutionary placement
- PANTHER PTHR42884:SF13 "NEUROENDOCRINE CONVERTASE 2", together with human PCSK2 (P16519), mouse/rat Pcsk2 and C. elegans egl-3 (interpro/panther/PTHR42884/PTHR42884-entries.csv).
- PAINT: PC2 bilaterian node PTN000082858 carries IBDs for extracellular region, neuron projection and peptide hormone processing (donors include amon itself, P16519, MGI:97512, RGD:3273, egl-3); IRD NOTs for Golgi membrane and TGN were placed on this node, i.e. curators deliberately kept TGN/Golgi only for constitutive convertases. Serine endopeptidase activity and generic membrane come from the deep node PTN002451026.
- The PANTHER family review (PTHR42884-review.yaml) places amon in SF13; no disagreement.

### Literature-grounded function
- Active dPC2 secreted from S2 cells only when coexpressed with 7B2 [PMID:10749852 "when dPC2 and either d7B2 or r7B2 were coexpressed in Drosophila S2 cells, abundant immunoreactive dPC2 was secreted into the medium, coincident with the appearance of PC2 activity."]
- Catalytic-His mutant fails to rescue hatching [PMID:10436051 "expression of amontillado with an alanine substitution for the catalytic histidine cannot."]
- AKH maturation [PMID:20523747 "mass spectrometric profiling shows that the production of mature AKH is inhibited in amon mutants."]; neurohemal peptides [PMID:21138435]; enteroendocrine peptides [PMID:21214272].
- Retina: RNAi-only, ligand processing proposed not shown [PMID:28853393 "We propose a model where pale R7-specific ligand processing by Amon and possibly additional factors instructs non-redundant signaling by two arms of the TGFβ family to specify pale R8 subtypes"].

### Changes in this re-review
- proteolysis (IDA, IEA): ACCEPT -> MODIFY to GO:0016486 peptide hormone processing (is_a descendant, already on gene).
- serine hydrolase activity (HDA): KEEP_AS_NON_CORE -> MODIFY to GO:0004252 (general-term rule).
- larval behavior (IEA ARBA): KEEP_AS_NON_CORE -> MODIFY to GO:0035180 larval wandering behavior.
- R8 cell fate specification (IMP): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED (indirect, non-autonomous, RNAi-only).
- neuron projection (IBA): ACCEPT -> KEEP_AS_NON_CORE.
- membrane (IBA): stays UNDECIDED, now with propagation_review (deep node, PC2 lacks TM; human PCSK2 is a donor).
- Description rewritten; core function expanded; reference_review added for all PMIDs; suggested questions/experiments added; status COMPLETE.

### Relative
- Closest characterised relative by phylogeny: human PCSK2 (P16519), same PANTHER subfamily SF13 and a donor at PAINT node PTN000082858. No genes/human/PCSK2 review exists in the repo.
- Modules mentioning PCSK2: modules/leptin_melanocortin_signaling.yaml, modules/beta_cell_glucose_stimulated_insulin_secretion.yaml (mammalian; amon not a member).
