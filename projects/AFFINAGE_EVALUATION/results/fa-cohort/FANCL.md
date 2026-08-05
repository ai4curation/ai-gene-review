# FANCL (FANCL) — AIGR vs Affinage

**Affinage record:** 2026-06-09 · 22 discoveries · self-eval pairwise win (faith 100%) · gates passed.

## Agreement (brief)

Both sources converge on FANCL's core biology: FANCL (PHF9) is the catalytic RING-type E3
ubiquitin ligase subunit of the Fanconi anemia core complex that, with its dedicated E2
UBE2T, site-specifically monoubiquitinates FANCD2 (Lys561) and FANCI (Lys523) to activate
replication-coupled interstrand-crosslink (ICL) repair. Both resolve the modular
architecture (N-terminal ELF/E2-like fold, central DRWD/RWD-like substrate-binding domain,
C-terminal RING that recruits UBE2T), the essential RING Cys307 and Trp341, FA core-complex
membership, chromatin/nuclear localization, and the requirement of FANCL RING activity for
all major FA phenotypes. Affinage's 22-citation narrative is factually consistent with the
AIGR review and overlaps on the foundational mechanistic PMIDs (12973351, 16916645, 17938197,
19111657, 19589784, 24389026, 22343915). No factual contradictions on core function.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Molecular activity GO layer | `mechanism_profile`: **GO:0016874 ligase activity**, **GO:0140096 catalytic activity acting on a protein**, **GO:0031386 protein tag activity** | **GO:0061630 ubiquitin protein ligase activity** (+ parent GO:0004842) and **GO:0031624 ubiquitin conjugating enzyme binding** for the E2-recruitment MF | **AIGR right; Affinage coarse.** Affinage collapses to high parents; GO:0016874 and GO:0140096 are non-specific ancestors and GO:0031386 "protein tag activity" is the wrong sense (that term is for ubiquitin/UBL *as the tag*, not the ligase). AIGR's specific RING-E3 term and the E2-binding MF are the correct branches. |
| E2 interaction MF | Lists UBE2T/UBE2W as partners; narrative treats the RING–E2 interface as central | **Corrected E3→E2 term**: MODIFY GO:0031625 (ubiquitin protein *ligase* binding, = binding an E3) → **GO:0031624 (ubiquitin *conjugating enzyme* binding, = binding an E2)** because UBE2T/UBE2W are E2s | **AIGR right (key fix).** GOA's IPI carried the E3-binding term for an E2 partner; AIGR fixes the branch. Affinage's coarse layer neither surfaces nor corrects this. |
| Localization | `mechanism_profile`: nucleus, **GO:0000228 nuclear chromosome**, **GO:0005739 mitochondrion** | Nucleus + **nucleoplasm** + **GO:0000785 chromatin (IDA)**; cytoplasm/cytosol **KEEP_AS_NON_CORE**; mitochondrion **not annotated** | **AIGR more precise + appropriately conservative.** Mitochondrial localization rests on a single ligase-independent-mitophagy study (PMID:35644338); AIGR keeps it out of GO core localization. Chromatin (the active-holoenzyme site) is captured experimentally. |
| ELF-domain ubiquitin binding | Narrative flags ELF domain binds free ubiquitin (Ile44 patch), required for efficient in-vivo FANCD2 monoubiquitination (PMID:26149689) | Was **absent** from the review | **Affinage surfaced a genuine gap.** Now **incorporated** as NEW GO:0043130 ubiquitin binding (regulatory/non-core). Legitimate distinct MF of the ELF domain. |
| Wnt / β-catenin K11 chains | K11-linked non-proteolytic ubiquitination of β-catenin enhancing Wnt targets in HSPCs (PMID:22653977) | Not annotated | **AIGR correctly conservative.** Single 2012 study, distinct substrate/chain type; a moonlighting claim not established as a core human FANCL function. Documentable in notes, not promoted to GO. |
| Ligase-independent mitophagy | Supports Parkin-mediated mitophagy via a ubiquitin-ligase-*independent* mitochondrial role; rescued by catalytic-dead C307A (PMID:35644338) | Not annotated | **AIGR correctly conservative.** Single study, mechanism-independent of FANCL's defining activity; over-reach to import as human GO core function. |
| Germline / reproduction | PGC proliferation, oocyte survival, sex-reversal phenotypes (mouse Pog PMID:12417526; zebrafish fancl PMID:20661450; GGN interaction PMID:12574169) | Not annotated | **AIGR correctly conservative.** Non-human organism/tissue-level consequences of FA-pathway loss, not FANCL's direct molecular function. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:26149689 | FANCL ELF (E2-like fold) domain binds free ubiquitin non-covalently via the Ile44 patch; dispensable in vitro but required for efficient DNA-damage-induced FANCD2 monoubiquitination in vivo | Added to `references` (reference_review MEDIUM/VERIFIED, PMC4543658 full text verified); added **NEW** annotation GO:0043130 ubiquitin binding (IDA, action NEW, non-core) with two verbatim `supported_by` quotes. GO:0043130 confirmed molecular_function (QuickGO, not obsolete). |

## Net assessment

The AIGR review is materially more precise and better-grounded than the Affinage record on
FANCL's molecular function: it uses the specific RING-E3 term (GO:0061630) and, crucially,
corrects a GOA branch error by remapping the UBE2T/UBE2W interaction from E3-binding
(GO:0031625) to the correct E2-binding term (GO:0031624), whereas Affinage's coarse
`mechanism_profile` sits at non-specific parents (GO:0016874/GO:0140096) and even mis-tags a
"protein tag activity." Affinage's dense narrative was nonetheless valuable as a sourcing
layer: it surfaced one genuine molecular function the review had missed — non-covalent
ubiquitin binding by the ELF domain (PMID:26149689) — now incorporated as a non-core
GO:0043130 annotation with verbatim support. Affinage's remaining extensions (β-catenin/Wnt,
ligase-independent mitophagy, and germ-cell/reproduction phenotypes) are single-study and/or
non-human organism/tissue phenotypes that AIGR correctly declines to promote to human GO core
functions. **1 paper incorporated, 1 new annotation (GO:0043130 ubiquitin binding),
validation ✓ Valid (1 benign deep-research warning).**
