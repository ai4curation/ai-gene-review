# VRN5 / VIL1 curation notes

## Session 2026-10-05 (vernalization_flc_silencing module)

- Q9LHF5, At3g24440. The UniProt primary name is VIL1 (synonym VRN5); the folder is `VRN5` as assigned by the module plan, and the review `gene_symbol` is VRN5 (TAIR name; a UniProt synonym), matching the folder.
- Falcon deep research failed.
- Identification: [PMID:17174094 "VRN5 and VIN3 form a heterodimer"]; [PMID:17114575 "VIL1, along with VERNALIZATION INSENSITIVE 3 (VIN3), is necessary for the modifications to FLC and FLM chromatin"].
- FLC binding dynamics: [PMID:18854416 "The vernalization-induced silencing is triggered by the cold-dependent association of the PHD finger protein VRN5 to a specific domain in FLC intron 1, and this association is dependent on the cold-induced PHD protein VIN3."]
- Adaptor role: [PMID:40858112 "specifically in VRN5, there is a close packing of the central PHD superdomain and FNIII domain, and this mediates its interaction with a PRC2 core complex with the core subunit VRN2"] and "it is required to physically connect VIN3 with PRC2". Basis for the NEW GO:0030674 protein-macromolecule adaptor activity.
- Photoperiod (FLM) roles are kept as non-core: [PMID:17114575 "VIL1 regulates FLM independently of VIN3 in a photoperiod-dependent manner."]

## Decisions
- IBA histone H3 reader -> MARK_AS_OVER_ANNOTATED. The VRN5 PHD superdomain itself was not assayed, but the VEL PHD superdomain lacks the H3 pocket, and in VRN5 this module mediates PRC2 binding.
- IBA constitutive heterochromatin -> MODIFY to facultative heterochromatin formation.
