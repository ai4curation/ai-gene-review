# UBE2T (FANCT) — AIGR vs Affinage

**Affinage record:** 2026-06-10 · 35 discoveries · self-eval pairwise win (faith 100%) · gates passed.

## Agreement (brief)

Both sources converge on UBE2T's core biology: it is the dedicated E2 ubiquitin-conjugating
enzyme of the Fanconi anemia (FA) interstrand-crosslink repair pathway that, paired with the
cognate RING E3 ligase FANCL, catalyzes DNA-damage-induced, site-specific monoubiquitination
of FANCD2 (Lys561) and FANCI (Lys523) on chromatin. Both resolve active-site Cys86, the
minimal UBE2T+FANCL reconstitution stimulated by FANCL's RWD-like domain, FANCI's role in
restricting the modification to the physiological substrate lysine, regulation by
chromatin localization rather than core-complex assembly, FANCL-stimulated inactivating
automonoubiquitination, and the FA-T (FANCT) disease link. The two records overlap on the
foundational mechanistic PMIDs (16916645, 17938197, 19111657, 19589784, 24389026). No
factual contradiction on core function.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Molecular activity GO layer | `mechanism_profile`: **GO:0140096 catalytic activity, acting on a protein**, **GO:0016740 transferase activity** | **GO:0061631 ubiquitin conjugating enzyme activity** (the E2-specific term), and MODIFY of GOA's broad GO:0004842 (ubiquitin-protein transferase activity, IDA ×4) → GO:0061631 | **AIGR right; Affinage coarse.** GO:0140096 and GO:0016740 are non-specific high ancestors; GO:0016740 (transferase) is far above even the ubiquitin layer. AIGR's E2-specific GO:0061631 is the correct branch and AIGR additionally sharpens GOA's own generic GO:0004842 (which also covers E3 ligase activity) to the E2 term. |
| Linkage-specific polyubiquitination | Narrative foregrounds UBE2T building **K48- and K63-linked chains** on cancer substrates; David 2010 lysine preferences (K6/K11/K27/K29/K48/K63) | GOA's six David-2010 linkage-specific process IDAs (K6/K11/K27/K29/K48/K63) all **MARK_AS_OVER_ANNOTATED**; polyubiquitination kept only as **KEEP_AS_NON_CORE** | **AIGR right.** David 2010 (PMID:20061386) was run in the **absence of any E3**, measuring intrinsic in-vitro lysine preference, not physiological output. AIGR correctly demotes these; the physiological UBE2T reaction is site-specific *mono*ubiquitination. |
| Oncogenic substrate ubiquitination | ~15 cancer papers: UBE2T ubiquitinates p53, RACK1, Akt, RPL6, CDC42, FOXO1, CBX6, GSK3β, PBX1, SORBS3, HP1α, BIRC5… activating Wnt/β-catenin, PI3K/AKT, JAK-STAT3 | Not annotated (canonical FA-pathway function only; BRCA1 downregulation kept as context-specific/non-core) | **AIGR correctly conservative.** Each is a single-study, cancer-cell claim, several asserting E3-independent degradation; a heterogeneous set of moonlighting/context activities not established as UBE2T's core molecular function. Documentable, not promoted to GO core. |
| Second E2–E3 pairing (RNF8) | UBE2T pairs with **RNF8** to monoubiquitinate H2AX/γH2AX, driving CHK1 activation (PMID:33087136) | Frames FANCL as the exclusive cognate E3 partner; RNF8 pairing not annotated | **AIGR conservative; no contradiction.** "Exclusive" is from FANCL's side (structural: FANCL selects UBE2T among E2s, PMID:24389026), not a claim UBE2T cannot engage another E3. The RNF8 pairing is a single medium-confidence cancer study; appropriately left out of core GO. |
| Extended genome-maintenance roles | UBE2T required for **NER** (PMID:22615860) and **R-loop/transcription-replication-conflict resolution** in PGCs (PMID:36928776) | Captured at the general level: DNA damage response (GO:0006974), interstrand cross-link repair (GO:0036297), DNA repair | **AIGR appropriately conservative.** Single-study (DT40 / mouse PGC) extensions; the review's general DDR + ICL-repair terms cover the core, and promoting narrow specific processes on one paper each is not warranted. |
| Regulation of UBE2T abundance | CaMKII-δ9 phospho-degradation (PMID:31481791), NEDD4L-directed turnover (PMID:34838005), SENP1 deSUMOylation (PMID:31969492) | Not annotated | **AIGR correct.** These describe UBE2T *being regulated* by other enzymes — the molecular functions of CaMKII/NEDD4L/SENP1, not activities of UBE2T. They do not belong in UBE2T's function annotations. |
| Localization granularity | `mechanism_profile`: GO:0005634 nucleus, **GO:0000228 nuclear chromosome** | Nucleus + **nucleoplasm** (core location) + **chromatin binding GO:0003682 (IDA)** as MF | **AIGR more precise.** AIGR captures the functionally relevant chromatin association experimentally (holoenzyme forms on chromatin) and uses nucleoplasm as the specific core location; Affinage's GO:0000228 is a coarser CC that AIGR's chromatin-binding IDA already covers more informatively. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:19887602 | UBE2T polyubiquitinates BRCA1 in a Cys86-dependent manner in breast cancer cells | Already in `references` (reference_review MEDIUM/VERIFIED). Added a verbatim `supported_by` anchor ("BRCA1 to be polyubiquitinated by incubation with") to the previously unanchored GO:0000209 protein polyubiquitination (IBA) annotation, which the `reason` already cited. |

No new references were fetched and **no new annotations were added.** The one existing annotation lacking a
verbatim quote for its cited-in-`reason` paper — GO:0051865 autoubiquitination (IDA, PMID:19111657) — could not
be anchored because that record is abstract-only in cache and the abstract does not state the autoubiquitination
sites (its sibling GO:0051865 annotation on PMID:16916645 already carries the verbatim evidence).

## Net assessment

The AIGR review is materially more precise and better-grounded than the Affinage record on
UBE2T's molecular function. AIGR uses the E2-specific GO:0061631 and sharpens GOA's own broad
GO:0004842 to it, whereas Affinage's coarse `mechanism_profile` sits at non-specific parents
(GO:0140096 / GO:0016740). Crucially, AIGR correctly demotes GOA's six in-vitro, E3-free
linkage-specific polyubiquitination IDAs (David 2010) as over-annotations and declines
Affinage's large, heterogeneous set of single-study cancer substrate/signaling claims
(p53, RACK1, Akt, CDC42, CBX6, Wnt/β-catenin, PI3K/AKT…), the RNF8/H2AX second-E3 pairing,
the NER and R-loop extensions, and the UBE2T-abundance-regulation papers — none of which are
established as UBE2T's core human molecular function. Affinage's 35-citation narrative was a
useful sourcing layer but surfaced no missed core function meriting a new GO annotation; its
value here was one verbatim experimental anchor for an existing polyubiquitination annotation.
**1 paper anchored (existing reference), 0 new annotations, validation ✓ Valid (1 benign
deep-research warning).**
