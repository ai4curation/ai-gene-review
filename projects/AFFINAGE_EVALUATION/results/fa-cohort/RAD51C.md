# RAD51C (FANCO) — AIGR vs Affinage

**Affinage record:** run 2026-06-10 · 42 discoveries · self-eval pairwise = win, faith 100% · gates passed.

The Affinage record for RAD51C is a dense (42 citations), well-anchored mechanistic narrative
covering the full RAD51-paralog biology: the two shared complexes (BCDX2 and CX3), the
recombination-mediator / RPA-relief activity, RAD51-filament nucleation, Holliday-junction branch
migration/resolution, ATM/NBS1/RPA-dependent recruitment with CHK2 checkpoint activation, fork
protection/restart, and the non-canonical roles (mitochondrial nucleoid, PALB2-BRCA2 complex,
ALKBH3 stimulation), plus the FANCO / breast-ovarian-cancer / PARPi-resistance clinical axis. The
AIGR review is curated, GOA-grounded and validated.

## Agreement (brief)

The two sources agree closely on the core biology. Both place RAD51C as the only paralog shared by
BCDX2 (RAD51B-RAD51C-RAD51D-XRCC2) and CX3 (RAD51C-XRCC3); both frame it as an ATP-dependent
recombination mediator that promotes RAD51-filament nucleation/extension on RPA-coated ssDNA (AIGR
GO:0097435 supramolecular fiber organization ACCEPT, GO:0140664 ATP-dependent damage sensor ACCEPT,
core_functions; Affinage PMID:37344587/11751636/23149936). Both agree on branched/junction DNA
binding (AIGR GO:0000400 ×2 ACCEPT), replication-fork protection/restart (AIGR GO:0031297 ACCEPT,
GO:0043596 ACCEPT), the ATM/NBS1/RPA→CHK2 checkpoint role (AIGR GO:0006281 IDA ACCEPT,
core_functions), complex membership (GO:0033063/GO:0033065 ACCEPT ×multiple), the mitochondrial
mtDNA-maintenance pool (GO:0005739 ACCEPT), and the PALB2-BRCA2 association. Both recognize the
RecA-fold ATPase nature of RAD51C and that HJ resolvase catalysis is not intrinsic to it.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Mechanism-profile GO layer | `molecular_activity` list flattens to `GO:0140097 catalytic activity, acting on DNA`, `GO:0140657 ATP-dependent activity`, `GO:0060090 molecular adaptor activity`; localization collapsed to `nucleus`/`nuclear chromosome`/`mitochondrion`/`cytosol`/`microtubule organizing center` | Uses specific, evidence-matched terms: four-way junction binding, ATP-dependent DNA damage sensor, supramolecular fiber organization; no generic "catalytic activity acting on DNA" | **AIGR right.** Affinage's own note flags this layer as coarse and self-contradictory. `catalytic activity, acting on DNA` wrongly implies RAD51C is an enzyme acting on DNA (nuclease/resolvase); RAD51C is a RecA-fold ATPase mediator. Do not import. |
| HJ resolvase / endonuclease catalysis | Narrative: RAD51C "required for Holliday-junction branch migration and resolution" (PMID:14716019); does **not** claim RAD51C is itself the endonuclease | GO:0008821 crossover-junction endonuclease MARK_AS_OVER_ANNOTATED ×2 (catalysis reassigned to GEN1) | **Agreement, not conflict.** Affinage frames RAD51C as *required for* HJ processing (correct) and never asserts intrinsic endonuclease catalysis; its coarse `catalytic activity acting on DNA` GO tag is the only place that over-reaches, and AIGR correctly excludes that. |
| MTOC / centrosome localization | mechanism_profile lists `GO:0005815 microtubule organizing center`; narrative cites centrosome-number defects in RAD51C-deficient cells (PMID:17268176, 19403737) | Not annotated as a localization | **AIGR right to exclude.** The centrosome-amplification phenotype is a downstream (ATR-CHK1-dependent) consequence of RAD51C loss, not evidence that RAD51C localizes to / functions at the MTOC. No localization annotation warranted. |
| `protein binding` (GO:0005515) | Narrative leans on many PPIs (XRCC3, RAD51B/D, XRCC2, RAD51, PALB2, BRCA2, ALKBH3) | 15 IPI `protein binding` rows MARK_AS_OVER_ANNOTATED as uninformative; interactions retained via complex/process terms | **AIGR right** per curation policy; Affinage does not assert the generic term, so no true conflict. |
| Interstrand cross-link repair | Strongly emphasized: FANCO, MMC/cisplatin hypersensitivity, FA-like disorder (PMID:20400963, 12000837, 22167183) | Captured only broadly under GO:0006281 DNA repair / GO:0000724 HR; **no specific ICL-repair annotation** | **Affinage surfaced a real gap.** Added NEW GO:0036297 interstrand cross-link repair (see below) — the defining FANCO function. |
| Sister chromatid cohesion | Narrative: RAD51C-deficient CL-V4B cells show reduced cohesion (PMID:12000837) | GO:0007062 KEEP_AS_NON_CORE but ISS with **no supporting_text** | **Affinage supplied the primary evidence.** Attached verbatim `supported_by` from PMID:12000837. |
| Meiotic recombination | Narrative: RAD51C on meiotic chromosomes, CX3 resolvase at crossovers, sexually dimorphic meiotic arrest (PMID:17114795, 17312021) | GO:0000707 / GO:0007131 KEEP_AS_NON_CORE, both IBA with **no supporting_text** | **Affinage supplied mammalian support** for the phylo-inferred meiotic terms; attached verbatim `supported_by` (mouse ortholog). |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:11751636 | BCDX2 HR-mediator core function | Added verbatim `supported_by` to core_functions[0] (RPA competition "partially alleviated by Rad51B-Rad51C"); primary mediator/RPA-relief biochemistry that previously had only the later cryo-EM/epistasis papers. Reference + reference_review (HIGH/VERIFIED). |
| PMID:12000837 | Sister chromatid cohesion (GO:0007062) | Attached verbatim `supported_by` ("reduced level of sister chromatid cohesion was found in CL-V4B cells") to the previously unsupported ISS annotation. Reference + reference_review (MEDIUM/VERIFIED). Also cited on new GO:0036297. |
| PMID:17312021 | Meiotic recombinase assembly (GO:0000707) | Attached verbatim `supported_by` (spermatocyte early-prophase-I arrest → early RAD51-mediated recombination) to the previously unsupported IBA meiotic annotation. Reference + reference_review (MEDIUM/VERIFIED). |
| PMID:17114795 | Reciprocal meiotic recombination (GO:0007131) | Attached verbatim `supported_by` (CX3 resolvase "associates with crossovers … resolution of recombination intermediates prior to chromosome segregation") to the previously unsupported IBA meiotic annotation. Reference + reference_review (MEDIUM/VERIFIED). |
| PMID:20400963 | Interstrand cross-link repair (GO:0036297) | `original_reference_id` for NEW GO:0036297; two verbatim `supported_by` quotes (MMC/camptothecin hypersensitivity; biallelic FA-like syndrome). Reference + reference_review (HIGH/VERIFIED). |

All five PMIDs fetched/cached via `fetch-pmid`; every `supporting_text` is a verbatim substring of
the cached publication. GO:0036297 (interstrand cross-link repair) verified via QuickGO as an active
biological_process term, correctly branched under DNA repair and more specific than the existing
GO:0006281 parent.

## Net assessment

AIGR and Affinage agree on RAD51C's core biology (dual-complex HR mediator, RAD51-filament
nucleation, junction binding, fork protection, checkpoint role) and — importantly — both decline to
credit RAD51C with intrinsic HJ endonuclease catalysis; Affinage frames it as *required for* HJ
processing while its own coarse `mechanism_profile` GO layer (`catalytic activity, acting on DNA`,
`microtubule organizing center`) over-reaches and was correctly not imported. Affinage's value here
was (1) surfacing one genuine annotation gap — specific interstrand-cross-link repair, the defining
FANCO function, added as a validated NEW GO:0036297 — and (2) supplying the primary experimental
evidence for three thinly-supported non-core annotations (sister chromatid cohesion; the two
phylo-inferred meiotic terms), plus the foundational RPA-relief mediator paper for the BCDX2 core
function. Edits were conservative; no existing AIGR decision (including the crossover-junction
endonuclease over-annotation call) was weakened. File remains ✓ Valid (single benign
deep-research-file warning).
