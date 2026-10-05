# HSPD1: ProtNLM function-text review

**PLI (score 0): Hsp60 type I chaperonin is assigned the cytosolic TRiC/CCT type II complex and its clients.**

## Original prediction

[ProtNLM F6Z587](https://www.uniprot.org/uniprotkb/F6Z587/entry#prot-nlm), frozen API snapshot 2026-09-08.

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance. As part of the TRiC complex may play a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia. The TRiC complex plays a role in the folding of actin and tubulin

## Atomic claims

| Claim | Assessment | Evidence |
|---|---|---|
| Subunit of TRiC/CCT | PLI | Hsp60 belongs to the mitochondrial Cpn60/GroEL branch and cooperates with Hsp10. |
| ATP-assisted protein folding | Supported family mechanism; uncertain exact-model competence | Conserved Hsp60 ATP sites remain, but the selected protein has a 32 aa internal deletion. |
| TRiC-mediated WRAP53/TCAB1 folding and telomere maintenance | PLI | Specific client/pathway is imported with the wrong chaperonin complex identity. |
| BBSome assembly and ciliary vesicle transport | PLI | No target-specific evidence establishes this TRiC-associated role for Hsp60. |
| TRiC folding of actin/tubulin | PLI | Hsp60 type I identity does not transfer the type II complex's client functions. |

Human [PMID:25918392](https://pubmed.ncbi.nlm.nih.gov/25918392/), DOI [10.1073/pnas.1411718112](https://doi.org/10.1073/pnas.1411718112), states “Human mitochondria harbor a single type I chaperonin system” and resolves its structure. The [horse sequence comparison](HSPD1-bioinformatics/RESULTS.md) preserves the precursor region and 97.4% identity across 541 paired residues. It identifies an internal 32 aa deletion, so active Hsp60 folding is not simply presumed for this exact model.

The existing horse GOA TRiC annotation comes from ARBA and repeats the same wrong complex identity. Its agreement with ProtNLM is an error-agreement observation, not validation. **PARALOG_OVERANNOTATION** captures over-transfer between related chaperonin branches. The model's exact training donor is unknown. The review distinguishes shared general chaperone chemistry from specific complex/client claims and from unresolved effects of the selected protein model.
