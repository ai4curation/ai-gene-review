# PALB2 (FANCN) — AIGR vs Affinage

**Affinage record:** run 2026-06-10 · 35 discoveries · self-eval pairwise = win, faith 100% · gates passed.

The Affinage record for PALB2 is a strong, PMID-dense (35 citations) mechanistic narrative of the
HR-scaffold life cycle: the N-terminal antiparallel coiled-coil leucine zipper binding BRCA1 (and the
homodimer→heterodimer switch that gates HR), the C-terminal WD40 β-propeller binding BRCA2, ubiquitin-
signaling recruitment to breaks (MDC1/RNF8/RAP80/Abraxas → BRCA1; RNF168-generated ub-H2A read by
BARD1-BRCA1; direct RNF168-PID/WD40 binding), intrinsic DNA/chromatin binding (N-DBD strand exchange;
ChAM–acidic-patch engagement antagonized by 53BP1), steady-state residence at active genes via
MRG15/SETD2/H3K36me3, stalled-fork recruitment by phospho-RPA and POLη support, ATM/ATR phospho-
regulation and a CHK1/CHK2-independent G2/M checkpoint, the KEAP1-NRF2 antioxidant branch, and a large
patient-variant/mouse-model layer (L24S/L35P/I944N/L1070P, Brca1-CC and Brca2-G25R knock-ins). The
AIGR review is curated, GOA-grounded, validated, and was already the product of a careful A→Z manual
pass with `core_functions` centered on the adaptor and DNA-binding activities.

## Agreement (brief)

The two sources agree on the core biology. Both center PALB2 as the molecular adaptor/scaffold that
physically bridges BRCA1 (N-terminal coiled-coil) and BRCA2 (C-terminal WD40 propeller) to form the
BRCA1-PALB2-BRCA2 complex that localizes/stabilizes BRCA2 and loads RAD51 for HR (AIGR:
`GO:0060090` molecular adaptor activity core, `GO:0000724` ACCEPT across IBA/IEA/IDA/IMP, `GO:1990391`
DNA repair complex; Affinage narrative + PMID:19369211/19584259/24141787). Both agree on intrinsic
N-terminal DNA binding stimulating RAD51 strand invasion (AIGR `GO:0003677`/`GO:0003697` ACCEPT, second
core function; Affinage PMID:20871616/31017574), coiled-coil homodimerization (`GO:0042803` ACCEPT;
PMID:22941656/39584160), and nucleoplasmic/nuclear-foci localization. Both explicitly demote the same
secondary roles to non-core: KEAP1-NRF2 antioxidant signaling, POLη support at blocked forks, and
MRG15/MORF4L1 chromatin targeting.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Mechanism-profile GO layer | `molecular_activity` includes `GO:0140097 catalytic activity, acting on DNA` and `GO:0098772 molecular function regulator activity` | PALB2 is not a catalytic enzyme; MF captured as `GO:0060090` adaptor + `GO:0003677/0003697` DNA/ssDNA binding | **AIGR right.** Affinage's own header flags this layer as coarse/collapsed-to-parents. `catalytic activity, acting on DNA` is wrong-branch — PALB2 has no established catalytic activity (its "strand exchange" is a DNA-binding/annealing property, not an enzyme reaction); `molecular function regulator activity` is a generic parent of the specific RAD51-stimulation captured via DNA binding. Not imported. |
| "Histone binding" for ChAM | Lists `GO:0042393 histone binding` | Now annotated `GO:0031491 nucleosome binding` (NEW, non-core) | **AIGR right (and more precise).** The ChAM paper explicitly states "direct DNA or core histone binding was not detectable" while "ChAM robustly binds to nucleosomes." Histone binding is the wrong term; nucleosome binding is the correct, evidenced one — added here as a NEW annotation. |
| RNA binding | Lists `GO:0003723 RNA binding` | Not annotated | **Both partly right; AIGR conservative.** The N-DBD does have in-vitro RNA strand-exchange/binding activity (PMID:31017574 "Novel RNA and DNA strand exchange activity"), so the claim is not baseless — but it is a specialized in-vitro property with no established in-vivo RNA-binding role, so AIGR reasonably omits it rather than over-annotate. Flagged as a minor gap, not incorporated. |
| Transcription / gene expression | `mechanism_profile` Reactome `R-HSA-74160 Gene expression`; narrative cites BRCA1-PALB2 co-occupancy at active genes and NF-κB/RA transcriptional co-activation (PMID:24591564) | Not annotated to transcription | **AIGR right to exclude as core.** Transcriptional co-activation is a single-lab, less-replicated secondary observation; the chromatin residence it depends on is better captured as nucleosome/MRG15 chromatin targeting. Correctly out of the core MF/BP set. |
| Ubiquitin-recruitment cascade, ATM/ATR phospho, G2/M checkpoint, cGAS-STING/PD-L1 | Narrated as PALB2 mechanism (RNF168/RNF8/MDC1/RAP80; S/Q phosphosites; checkpoint; HCC immune signaling) | Not annotated as PALB2 functions | **AIGR right.** These are upstream regulators of PALB2 recruitment, post-translational regulation *of* PALB2, or downstream consequences of PALB2 loss — not molecular functions/processes PALB2 itself enables. Correctly out of scope; the G2/M checkpoint role is a defensible but minor omission. |
| KEAP1-NRF2 secondary role sourcing | Anchored to the primary mechanistic paper PMID:22331464 | Present (description + over-annotated interaction rows) but cited only via high-throughput interactomes | **Affinage right that primary evidence exists.** Incorporated: PMID:22331464 added as a reference and as `supported_by` on the KEAP1 interaction row, grounding a role that previously rested only on HuRI/BioPlex hits. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:22193777 | Nucleosome binding (NEW `GO:0031491`) | Bleuyard et al. 2012 EMBO Rep (ChAM). Full text confirms ChAM is necessary and sufficient for intrinsic chromatin association and "robustly binds to nucleosomes" (distinct from the DNA-binding regions). Added a NEW, non-core `GO:0031491 nucleosome binding` annotation with two verbatim `supported_by` quotes; upgraded the reference with `reference_review` (HIGH/VERIFIED). Term verified as a molecular_function via QuickGO. |
| PMID:22331464 | KEAP1-NRF2 secondary role (`GO:0005515` KEAP1 row) | Ma et al. 2012 MCB. Added as a reference (`reference_review` MEDIUM/VERIFIED) and as verbatim `supported_by` ("PALB2 shares with NRF2 a highly conserved ETGE-type KEAP1 binding motif and can effectively compete with NRF2 for KEAP1 binding") on the previously interactome-only KEAP1 over-annotation row, giving the demoted antioxidant role a primary citation. |

Both PMIDs fetched/cached via `fetch-pmid`; every `supporting_text` is a verbatim substring of the
cached full text (whitespace-normalized, confirmed against the reference validator). One NEW annotation
was added — `GO:0031491 nucleosome binding` — a correctly-branched MF the review had captured only as
uninformative "protein binding"; it is marked non-core (a chromatin-anchoring/targeting activity, not
the central adaptor function). No existing curation decision was weakened by Affinage's coarse GO layer.

## Net assessment

The AIGR review and Affinage agree fully on PALB2's core BRCA1↔BRCA2 adaptor/scaffold and RAD51-loading
HR biology, on intrinsic N-terminal DNA binding stimulating strand invasion, and on demoting the KEAP1,
POLη, and MRG15 roles to non-core. Affinage's own GO `mechanism_profile` is coarse and in places
wrong-branch (`catalytic activity, acting on DNA` PALB2 does not possess; `histone binding` where the
evidence supports `nucleosome binding`; generic `molecular function regulator activity`) and was
correctly not imported. Affinage's real value was its dense, well-anchored narrative, which surfaced two
concrete additions incorporated conservatively: (1) a NEW, precise `GO:0031491 nucleosome binding`
annotation for the ChAM motif (replacing an uninformative "protein binding" row), and (2) the primary
KEAP1-NRF2 paper (PMID:22331464) to ground a secondary role that previously rested only on
high-throughput interactome hits. Over-reaches Affinage narrates (ubiquitin-recruitment cascade, ATM/ATR
phosphoregulation, G2/M checkpoint, transcriptional co-activation, cGAS-STING immune signaling) are
regulation-of / consequence-of / partner functions and were correctly kept out of PALB2's MF/BP set.
File remains ✓ Valid (one benign deep-research-file warning).
