# ASSAY_TO_FUNCTION — working notes

Journal of decisions and findings. Append, don't rewrite.

## 2026-06-06 — project kickoff, first mining pass

- Named the project ASSAY_TO_FUNCTION (branch: gene-readout-reliability).
- Core thesis: `R → P` reliability = f(proximity, convergence); phenotypic +
  high-convergence "hub" readouts (ROS, caspase, UPR, Ca²⁺, pH, ΔΨm) are the
  over-annotation traps. GO evidence codes don't capture this axis.
- Decision: start by mining the corpus (per user) rather than writing the rubric
  first.

### What I built
- `readout_catalog.yaml` — editable, regex-based catalog of readout classes,
  each tagged proximity/convergence + GO terms it's commonly over-mapped to.
- `mine_readouts.py` — scans all `*-ai-review.yaml`, joins readout class to
  reviewer action, writes matches + crosstab + QC string-count table.

### Findings
- 1,971 files / 75,931 annotations; 1,736 matches.
- Phenotypic hubs with usable N: caspase/apoptosis 49% any-downgrade, ΔΨm 42%
  vs molecular controls (in-vitro 24%, binding 18%). Directional but weak; most
  hub classes are N<10.
- **Key negative result**: probe brand names (CellROX, DCFDA, MitoSOX, pHrodo,
  FeRhoNox) are essentially absent from curator *prose*. The review summaries
  are synthesis, not methods. So review-text mining under-captures the very
  readouts we care about.

### Bugs caught in QC (don't repeat)
- `HyPer` → matched "hyper-activation" (case + hyphen). Fix: `(?-i:HyPer)`.
- `ERSE` → matched "diverse/reverse/adverse". Fix: `\bERSE\b`. (Had inflated
  UPR 29→609.)
- `MTS` → matched "MTs" (microtubules) + mito-targeting-sequence. Fix: require
  "MTS assay/reagent/reduction".
- Lesson: always read `matched_string_counts.tsv` before believing a total.

### Next
1. Pivot to publications corpus: PMID → cached `publications/PMID_*.md` →
   detect assay in the *paper* → join to annotation action. Richer signal.
2. Add GO aspect (from `*-goa.tsv`) to test "hubs shouldn't drive MF" directly.
3. Expand catalog; build the per-readout licensing rubric with worked examples.

## 2026-06-06 (cont.) — publications-corpus pass (mine_papers.py)

Coverage: 36,449 of 36,660 PMID-backed annotations resolved to cached papers.
16,682 paper-level matches; 722 thematically aligned (high-precision subset).

### Perf war story (don't repeat)
- v1: 80 regex/annotation over full text → killed at 280s.
- v2 memoize per pmid + 1 alternation/class → still ~10min (IGNORECASE scan of
  ~MB papers is ~0.15s each, ×12 classes ×many large papers).
- v3 combined single regex w/ named groups → SLOWER (0.2s/MB ×, alternation
  tries every branch per char). Reverted.
- v4 WINNER: two-stage filter. Cheap literal substring screen (necessary
  superset per class, `SCREEN` dict) gates the precise regex. Validated 0 lost
  matches vs regex-only on 350 papers (incl 50 largest). Full run ~4 min.
- Keep text original-case so case-sensitive `(?-i:HyPer)` works; screen on a
  lowercased copy.

### Findings (the good stuff)
- **Aspect constraint CONFIRMED**: aligned hub readouts license BP (or CC for
  ΔΨm = mito localization), essentially never MF. Caspase BP68/MF0, ROS BP10/MF0,
  viability BP87, autophagy BP109. Only exception: transcriptional reporters
  MF71 — but those are real TF-activity terms on real TFs, mostly ACCEPT. Not
  over-annotation.
- **Real failure mode = non-core demotion, not error.** Hard removal (rm/OA) of
  hub-readout annotations is ~comparable to molecular evidence (~27%). The
  difference: viability (58/90) and apoptosis (34/63) aligned annotations get
  KEEP_AS_NON_CORE. So hubs inflate the annotation set with correct-but-
  peripheral BP terms rather than producing wrong calls.
- ΔΨm is the one hub with elevated *hard* downgrade (21%), often via MODIFY —
  refined to more proximal terms.
- Caveat: any-downgrade is 40-60% for ALL classes incl molecular (dominated by
  NON_CORE/MODIFY refinements). Don't headline that number; headline aspect +
  non-core breakdown.

### Next
- Build the licensing rubric (per readout: aspect allowed, default core/non-core).
- Tighten paper→annotation link (title/abstract or methods-section only).

## 2026-06-06 (cont.) — rubric built

- RUBRIC.md (narrative + decision procedure + quick-ref table + worked
  contrasts) and rubric.yaml (machine-readable) written.
- Core rule: phenotypic hub readout -> BP/CC "response to/regulation of P",
  never MF, default non-core; promote to core only if gene is in P's recognized
  machinery/sensor set. MF exception: transcriptional reporter for a real TF.
- Every per-class rule anchored to ACCEPT-vs-downgrade corpus contrasts (BCL2 vs
  Akt1; CDK1 vs ACTB; TP53 vs PEX10/13; ATF4 vs HSPA1A + IRE1 MF over-call;
  AMBRA1 vs ABI2; ATF2/ASCL1 vs AIP). All examples verified against
  paper_readout_matches.tsv.
- Next: operationalize as a flagger (hub-readout + MF aspect, or core-call on a
  non-machinery gene = re-review candidate).

## 2026-06-06 (cont.) — flagger built

- flag_candidates.py consumes paper_readout_matches.tsv, applies rubric, writes
  reports/flagged_candidates.tsv. Flags only standing + hub-aligned annotations.
- Tier 1 (MF from hub): 7. Exactly the predicted pattern — reporter-driven
  coactivator/corepressor MF for non-TF coregulators (CTNNB1, NOTCH1, SIRT1,
  HMGB1) + Ca2+-binding MF (Calm2, HRC) that needs EF-hand evidence not imaging.
  TF DNA-binding-activity MF excluded via TF_LEGIT_MF regex.
- Tier 2 (core hub-aligned BP/CC): 291. Triage queue: MITO 85 (mostly generic
  mitochondrion), TRANSCRIPTIONAL 72, AUTOPHAGY 70, APOPTOSIS 24, VIABILITY 18.
- Dedup per (organism, gene, go_id). Framed as re-review candidates, not errors.

## 2026-06-06 (cont.) — Tier-1 re-review (loop closed)

- Re-reviewed all 7 Tier-1 candidates vs actual file evidence (REREVIEW_TIER1.md).
- Outcome: NONE a clean over-annotation. 6 KEEP, SIRT1 soft non-core. Flag
  over-fired.
- Calibration: (1) binding MF (Ca-binding: Calm2, HRC) is a direct activity, not
  readout-licensed -> flagger now excludes *binding MF from Tier 1 (7->5).
  (2) coregulator MF legit for real coregulators (β-catenin, NICD); discriminator
  is machinery membership not aspect. (3) standing-only filter already excluded
  the true over-annotation (AIP, already OVER_ANNOTATED) -> flagger best used on
  UNREVIEWED annotations, not accepted ones.
- No gene YAMLs edited (verdicts were KEEP / soft). Honest null-ish result; the
  value was calibrating the rubric + confirming existing curation handled the
  real MF over-calls.
- Next: re-target flagger at unreviewed hub-aligned MF; work Tier-2 queue.

## 2026-06-06 (cont.) — Tier-2 queue + machinery discriminator

- Re-aiming at *unreviewed* only yields 18 candidates (all BP/CC, no MF) — volume
  is in the Tier-2 ACCEPT queue (291). So prioritized that instead.
- flag_candidates.py now: --target {accepted,unreviewed,all}; Tier-2 ranked by
  class any-downgrade rate (read from aligned crosstab); clean \n TSVs (miners too).
- VIABILITY re-review (18): queue MIXES machinery (CDK1/MYC/RB1/TP53/Mtor =
  correctly core) with indirect (IL21/PDGFB/VEGFA/Sirt2). Flag alone can't tell
  them apart.
- KEY: the gene's own MF is the discriminator. Added `indirect_ligand` tag =
  gene has signaling-ligand MF (cytokine/growth factor/hormone/chemokine) ->
  process is downstream of receptor signaling -> non-core. Surfaces 6 clean
  candidates (IL21, PDGFB, VEGFA x2, HMGB1 x2) at top of queue. See REREVIEW_TIER2.md.
- No YAML edits (defensible cases, respecting curation). Handed off as worklist.
- Honest limit: discriminator only catches signaling-ligand indirects; other
  indirect classes (transporters etc.) still need human judgement.

## 2026-06-06 (cont.) — actual YAML edits (EDITS.md)

- Carried analysis through to curation edits. Downgraded ACCEPT->KEEP_AS_NON_CORE:
  PDGFB GO:0072126 (x2), HMGB1 GO:0007204, Sirt2 GO:0051781, VEGFA GO:0043066 (x2).
  = 4 genes, 6 records. All re-validate clean.
- Kept (false positives): VEGFA GO:0001938 EC prolif (defining fn), SIRT1 GO:0003714
  corepressor (well-supported MF), Calm2/HRC binding MF, CTNNB1/NOTCH1 coactivator.
- IMPORTANT: tried to downgrade IL21 GO:0042102 T-cell-prolif but the core_functions
  pretool validation hook BLOCKED it — GO:0042102 is in IL21 core_functions
  directly_involved_in (cytokine -> immune outputs, incl B cell prolif). Singling
  out T cell prolif = inconsistent. Reverted; kept core. Good catch by the hook.
- Lesson: a flag is a candidate; decline the edit when the "downstream" process is
  the gene's defining role (VEGFA EC prolif, IL21 immune outputs). Tracked in EDITS.md.

## 2026-06-06 (cont.) — IL21 deferred, PDGFB confirmed, rubric refined

- Discussion w/ cmungall on IL21. Outcome:
  - IL21 GO:0042102 (T cell prolif) x2: ACCEPT -> UNDECIDED (paper-backed:
    PMID:17673207 abstract shows proliferative effect on anti-CD3 T cells).
    Removed GO:0042102 from core_functions (else validation fails / inconsistent).
    Created detailed GitHub issue #1418 for expert curator; NK cytotoxicity
    (GO:0045954, IBA/IEA) raised there too. IL21 validates clean.
  - PDGFB: considered reverting (mesangial = signature, KO-null lacks mesangial
    cells) but user rightly noted that's necessity not mechanism -> ligand doesn't
    directly regulate proliferation, receptor does. STAYS KEEP_AS_NON_CORE.
  - Rubric refined: "signaling-ligand -> indirect" over-fires on DEDICATED
    cytokines/growth factors. Better axis = signature vs incidental. Added caveat
    to RUBRIC.md. (Flagger discriminator left as-is for now; the caveat documents
    that signature outputs must not be auto-demoted.)
- No new papers fetched; reasoning used background knowledge + already-cached
  PMID:17673207 / PMID:15207081 to back the UNDECIDED. publications/ is write-
  protected by hook anyway.

## 2026-06-07 — catalog extension to 12 new readout classes

- Added readout classes: CELL_MIGRATION_INVASION, CELL_ADHESION_SPREADING,
  MEMBRANE_TRAFFICKING_ENDOCYTOSIS, SECRETION_DEGRANULATION, METABOLIC_FLUX,
  DNA_DAMAGE_FOCI, SENESCENCE, and pathway reporters WNT/NFKB/HYPOXIA_HIF/
  NOTCH/HIPPO_TEAD. Each: aligned_label_regex + commonly_overmapped_to GO IDs +
  patterns + a necessary-superset SCREEN entry in mine_papers.py.
- Built a corpus-level QC: mine_papers.py now writes
  reports/paper_matched_string_counts.tsv (matched substrings counted once per
  paper) — the publications analogue of the prose miner's QC. This is where
  substring bugs actually surface in the corpus that matters.

### Substring bug caught in QC (don't repeat)
- `\bOCR\b` (oxygen consumption rate) matched the C. elegans **ocr-2** TRPV gene
  (19 false hits in prose). Dropped bare OCR; rely on "oxygen consumption rate",
  Seahorse, ECAR. After the fix, paper_matched_string_counts.tsv is clean across
  all 12 new classes (transwell, γh2ax, topflash, sa-β-gal, fm4-64, cd107a, …).
  Lesson reconfirmed: short all-caps abbreviations collide with gene symbols.

### Findings (the aspect constraint generalizes)
- Every new aligned class is BP/CC-dominant, ~zero MF. Sole MF: LRRK2
  *β-catenin destruction complex binding* (a binding MF, already non-core).
- Non-core demotion elevated as predicted: migration 16/35, membrane-traffic
  7/14, Wnt 8/17, senescence 6/9.
- Well-powered new hubs: migration 35, DNA-damage 36, Wnt 17, endocytosis 14.
  Under-powered (flagged honestly): secretion 1, metabolic 3, adhesion 4,
  NF-κB 6, hypoxia 2, Notch/Hippo ~0.

### Re-review (flagger precision on accepted calls is again low)
- New `CELL_MIGRATION_INVASION` indirect_ligand cluster = CCL11/PDGFA/PDGFB/
  VEGFA/HMGB1 — all SIGNATURE outputs (chemotaxis IS a chemokine's job; PDGF
  migration already in core_functions). Declined; documented in EDITS.md.
- Non-ligand Tier-2 in new classes = the MACHINERY (BRCA1/2, CHD1, CLTC, TFRC,
  CTNNB1, AXIN1, FZD7, TRAF6, ARNT, TP53). Correctly core → KEEP.
- The one genuine non-core/borderline: STAT3 GO:0030335 (TF; migration is
  downstream). High-profile + contested → ACCEPT→UNDECIDED, issue #1422, and a
  staged+submitted OpenScientist job (worked example of the user's workflow).

### Tooling for the OpenScientist workflow (user request)
- `stage_hypotheses.py` (+ `just assay-stage-hypotheses`): human-gated generator
  that turns selected flagged_candidates.tsv rows into committed, frontmatter-free
  prompt.md files under genes/<sp>/<gene>/<gene>-hypotheses/<slug>/ and prints the
  submit command — but NEVER submits. Reuses scripts/gene_hypothesis_deep_research.py
  record/template machinery; specializes the seed to the "core vs downstream?"
  question. Added `just assay-mine` / `just assay-flag` too.
- Submitted ONE job (STAT3) as the worked example since it's a contested case a
  cited adjudication can settle. Result committed as provenance; verdict posted to
  #1422; annotation kept UNDECIDED (output is hypothesis-generating, not ground
  truth — verify cited PMIDs).

## 2026-06-07 (cont.) — rubidium (86Rb) flux as a molecular positive control

- Per cmungall: added RUBIDIUM_FLUX (86Rb+/Rb+ K+-channel/transporter assay) as a
  MOLECULAR / low-convergence class (user picked this classification) — the MF-
  licensing end of the proximity axis, the mirror image of the Ca2+ imaging hub.
  Gave it aligned_label_regex + commonly_overmapped_to (K+ channel/transport) so
  we could test whether it shows MF (unlike the hubs' ~zero MF).
- QC clean: gated on unambiguous notations ("rubidium", "86rb", "rb-86", ...);
  bare "rb" deliberately NOT a screen token (collides with RB1 gene + substring
  "rb" everywhere). 86Rb matched 33 papers, no false positives.
- HONEST NULL: only 1 (annotation, RUBIDIUM_FLUX) match in the whole corpus, and
  it's Mtor "transmembrane transporter binding" (not a K+ channel, aligned=False).
  Of 33 86Rb papers, ~none is an annotation's original_reference_id. So the MF-
  licensing positive control can't be demonstrated in this corpus yet. Kept the
  class (correct, future-proof); the null re-confirms the first-pass lesson that
  MF annotations cite structural/biochemical refs, not functional-flux assays.
  Also a known miner limitation: joins on original_reference_id only, not
  supported_by.
- Caveat documented: Rb+ flux is direct only for the pore-forming channel; flux
  moved via an upstream regulator/subunit is as indirect as the hubs.

## 2026-06-07 (cont.) — broader join on supported_by refs (--include-supporting)

- Per cmungall (option a): added annotation_pmids() + --include-supporting to
  mine_papers.py so an annotation joins to readout usage across ALL its cited
  papers (supported_by / additional_reference_ids), not just original_reference_id.
  Rows gain ref_role (primary/supporting). Default unchanged; broader run written
  to reports/with_supporting/ to keep canonical strong-link reports intact.
- Coverage jump: PMID-backed 37.6k->47.2k, matches 18.9k->28.1k, aligned
  863->1200 (+39%; 337 from supporting). Headline STRENGTHENS: hubs stay
  BP/CC-dominant, ~zero MF on the bigger sample. QC clean (only pre-existing
  IN_VITRO_ENZYME 'km' token, not mine).
- RUBIDIUM_FLUX STILL null (same 1 non-aligned Mtor hit) even with supporting
  refs -> robust null: the 33 86Rb papers are disconnected from curated annotation
  refs. Confirms MF annotations cite structural/biochemical, not flux assays.
- Known remaining limitation: join is on PMIDs only (file:/reactome refs ignored);
  supported_by weak-link is weaker than primary (use ref_role to separate).

## 2026-06-07 (cont.) — 10 more classes: proximity axis demonstrated BOTH ways

- Added 5 molecular/MF-licensing classes (ELECTROPHYSIOLOGY, KINASE_ACTIVITY_ASSAY,
  GTPASE_ACTIVITY, UBIQUITINATION_ASSAY, CHROMATIN_CHIP) + 5 phenotypic hubs
  (CELL_DIFFERENTIATION, ANGIOGENESIS_TUBE, PHAGOCYTOSIS, CELL_CYCLE_FLOW,
  BARRIER_PERMEABILITY). Chose common, well-cited molecular assays specifically to
  deliver the MF positive control Rb flux couldn't.
- HEADLINE: aspect of aligned splits cleanly on the axis. Molecular: ChIP MF136,
  kinase MF106, GTPase MF55, ubiquitination MF39/CC24, electrophysiology MF18.
  Phenotypic: differentiation BP19, angiogenesis BP22, cell-cycle BP16,
  phagocytosis BP6, barrier CC5. Electrophysiology finally captured channel-MF
  (MF18) that Rb flux missed. Even sharper with --include-supporting (ChIP MF212).
- QC clean: required ChIP+suffix (no potato/microarray "chip"); broad "kinase"/
  "ubiquitin"/"teer" screens gate precise regexes. matched_string_counts verified.
- Curation: new-hub flags (26) all machinery or signature (VEGFA angiogenesis;
  GATA3/SOX9 master diff TFs; RB1/BRCA1 cell cycle) -> correctly core, NO edits.
- Perf note: broad screens (kinase, ubiquitin) make detection scan more papers;
  canonical run ~slower. Still fine. Two-stage filter holds.

## 2026-06-07 (cont.) — 8 more classes (proteostasis/lipid/redox/nucleic acid) -> 43 total

- Molecular: PROTEASE_ACTIVITY, NUCLEASE_ACTIVITY, LIPID_TRANSFER_FLIPPASE,
  PROTEASOME_ACTIVITY. Phenotypic: PROTEIN_TURNOVER (CHX chase/half-life),
  REDOX_BALANCE (GSH/GSSG, NAD(P)+/NAD(P)H), LIPID_PEROXIDATION (MDA/TBARS/4-HNE/
  BODIPY-C11), TRANSLATION_ASSAY (SUnSET/polysome/35S-Met).
- Axis holds: NUCLEASE MF20, PROTEASE MF15, LIPID_TRANSFER MF5 (MF) vs
  PROTEIN_TURNOVER BP29, TRANSLATION BP13, LIPID_PEROXIDATION BP12 (BP).
  PROTEASOME -> BP30/CC12 (catabolic process + complex, not bare endopeptidase MF).
  REDOX_BALANCE under-powered (BP1).
- Substring traps dodged (lesson #1): bare MDA (MDA-MB cell lines) -> malondialdehyde;
  bare puromycin (selection antibiotic) -> puromycin incorporation/SUnSET; cyclic
  nucleotide DROPPED this round to avoid cAMP->"hippocampus"/"campaign". QC clean.
- Flags (27) all machinery again (PSMA1/PSMB5 proteasome subunits, CUL3 cullin,
  CDC37/PEX19 chaperones) -> correctly core, NO edits.

## 2026-06-07 (cont.) — 9 more classes (epigenetic/immune/2nd messenger) -> 52 total

- Molecular: METHYLTRANSFERASE_ACTIVITY, ACETYLTRANSFERASE_DEACETYLASE,
  PHOSPHATASE_ACTIVITY, POLYMERASE_ACTIVITY, HELICASE_ACTIVITY. Phenotypic:
  CYCLIC_NUCLEOTIDE_SIGNALING, CYTOTOXICITY_KILLING (51Cr/killing),
  CYTOKINE_PRODUCTION (ELISpot/ICS), HISTONE_MARK (H3K4me3 etc.).
- Axis holds (5th time): acetyltransferase MF59, polymerase MF15, phosphatase MF8,
  methyltransferase MF7, helicase MF7 (MF) vs histone-mark BP13, cyclic-nucleotide
  BP10, cytokine BP7, cytotoxicity BP3 (BP). Nice epigenetic pair: enzyme assay
  (HAT/HMT) = MF, mark state (H3K4me3) = BP.
- Cyclic nucleotide added SAFELY: bare cAMP avoided (IGNORECASE \bcAMP\b hits
  "camp"; substring collides w/ hippocampus/campaign); required assay/level/sensor
  context. HAT requires "HAT assay/activity" not bare "hat". QC clean.
- Flags (11) machinery/signature again: chromatin enzymes (RTT109 HAT, SET1 HMT,
  CHD1 remodeler, ASF1 chaperone) + GPCRs whose cyclase signaling is signature
  (ADRB2, Drd1) -> correctly core, NO edits.
