# GSTU20 (Q8L7C9, At1g78370; FIP1) review notes

## Session 2026-09-30

### Identity and biochemistry
- Tau-class GST, 217 aa, PANTHER PTHR11260:SF601 (UniProt DR line). Also called FIP1 (FIN219-interacting protein 1).
- Recombinant FIP1 conjugates GSH to CDNB: [PMID:17220357 "The result showed that FIP1 can use GSH and 1-chloro-2,4-dinitrobenzene (CDNB) as substrates"] (Km 0.467 mM GSH, 1.794 mM CDNB per UniProt).
- Crystal structure: canonical homodimeric GST fold, GSH in the G-site: [PMID:28223489 "FIP1 possesses a canonical, homodimerized GST protein fold."]; [PMID:28223489 "interacts with conserved K40, E66, and S67"]; GST activity lower than SjGST [PMID:28223489 "FIP1 showed lower GST activity than Schistosoma japonicum GST (SjGST)"].
- Included in the family-wide recombinant assays of Dixon et al. 2009 (CDNB, BITC, cumene-OOH); tau GSTs generally conjugate BITC [PMID:19174456 "BITC was a more discriminating GST substrate, being acted on by most tau class enzymes but rarely by the GSTFs."].

### Localisation
- GUS-FIP1 in onion cells: cytoplasm and nucleus [PMID:17220357 "bombarded cells showed the GUS-FIP1 fusion protein localized in the cytoplasm and the nucleus"].
- Proteomic detections in chloroplast (Zybailov 2008, noted in [PMID:19174456 "GSTs F2, F8, F9, F10, U19, U20, L2, and DHAR3 in the chloroplast"]), mitochondria/membranes (PMID:28887381) and apoplast (PMID:18538804) treated as contamination/over-annotation; no targeting signal.

### FIN219/JAR1 and light signalling
- Interacts with FIN219 (JAR1/GH3.11, Q9SKE2) [PMID:17220357 "we demonstrate that FIN219-interacting protein 1 (FIP1) interacts with FIN219 in vitro and in vivo"].
- Doubles FIN219 adenylation activity [PMID:28223489 "the adenylation activity per mole of FIN219–FIP1 was approximately double the adenylation activity per mole of FIN219 alone"] -> MODIFY enzyme binding (IPI, PMID:28223489) to GO:0008047 enzyme activator activity.
- Both gain and partial loss of function give far-red hyposensitivity and late flowering [PMID:17220357 "The gain of function and partial loss of function of FIP1 resulted in a hyposensitive hypocotyl phenotype under continuous FR (cFR) light"].

### Aliphatic glucosinolates
- MYB28-regulated with the aliphatic GSL pathway [PMID:17420480 "Transcriptome analyses of myb28 and Myb28 -overexpressing cell cultures indicated that both of them are regulated by Myb28"].
- CRISPR knockouts: aliphatic but not indolic GSLs drop [PMID:35145536 "both gstf11 and gstu20 mutants exhibited substantial reduction in almost all categories of aliphatic GSLs with different side chain lengths"]; gstu20 stronger than gstf11; double mutant additive but not null [PMID:35145536 "the double mutation of GSTF11 and GSTU20 caused a dramatic decrease but did not completely abolish the formation of aliphatic GSLs"].
- No activity assay on the native intermediate [PMID:35145536 "the levels of protein and its derived enzymatic activity should be validated in future studies"]; broad transcriptome change in gstu20 [PMID:35145536 "In gstu20, 1,232 genes were identified as DEGs"].

### Decision: no NEW GO:0019761 (glucosinolate biosynthetic process)
- Participation test: if GSTU20 catalyses GSH conjugation of the CYP83A1 product, it would do a step of the pathway (catalyst case), so the term could in principle apply. But the only in planta evidence is necessity (knockout loss of end products). There is no enzyme assay on the native aci-nitro/nitrile oxide intermediate, no accumulation of upstream intermediates reported, the conjugation can occur non-enzymatically, the double mutant is not null, and gstu20 has >1,200 DEGs (indirect effects not excluded; core pathway transcripts were not reported). The module itself carries this caveat.
- Comparator check (QuickGO, 2026-09-30): GO:0019761 in Arabidopsis is carried by pathway enzymes with biochemical support (CYP83A1/B1 IDA; SUR1, UGT74B1, CYP79F1 IMP) and by GSH1 (IMP). GGP1 was accepted in this repo because it has in vitro activity on a glucosinolate GSH conjugate and mutants accumulate intermediates. Among GSTs, GSTF9/GSTF10 carry no glucosinolate term; GSTU13 carries IMP "indole glucosinolate catabolic process" (acts_upstream_of_or_within, PMID:29122987). So a mutant-based acts_upstream_of_or_within annotation has GST precedent, but an involved_in (participation) assertion is not established.
- Outcome: glucosinolate role described in the description and core_functions free text only; a GO curator question about an acts_upstream_of_or_within IMP annotation is recorded in suggested_questions.

### Action tally
- ACCEPT 13, KEEP_AS_NON_CORE 7, MARK_AS_OVER_ANNOTATED 4, MODIFY 1, UNDECIDED 0, NEW 0 (25 rows). (Response to gravity IEP moved from non-core to over-annotated on 2026-10-01, PR review.)

### Falcon deep research (GSTU20-deep-research-falcon.md, appeared mid-session)
- Consulted after the review was drafted. It frames GSTU20 as catalysing "or facilitating" the GSH-conjugation step, citing Zhang et al. 2022 and Choi et al. 2024 (Plant Physiol 196:1340, HY5-HDA9 repression of glucosinolate genes including GSTU20). Neither provides enzyme assays on the native intermediate (Choi 2024 is transcriptional regulation), so the no-NEW decision stands. Choi 2024 not cached/cited in the YAML.


## Module-member evidence audit — 2026-10-25

Reviewed every original row (25) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

PMID17220357 and28223489 directly assay general GST activity and FIN219 interaction/adenylation stimulation. Both enzyme-binding rows now refine consistently to enzyme activation. PMID35145536 measures pathway mutants and profiles, not purified native activated-aldoxime conjugation: maintain that limitation. Generic GSH metabolism describes real conjugation; toxin catabolism is unresolved rather than assumed from family reputation. Unchecked organellar/apoplastic fractionation assignments remain undecided.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.

### Final consistency QA, 2026-10-26

The FIN219-activation core location now matches the supported cytosol refinement already applied to its general cytoplasm annotations.


## 2026-10-26 — PR #5550 source-level correction

Revisited review findings 1–3 against the actual publication cache and the primary sources. Removed generic source-unresolved boilerplate where the assay design is adjudicable. Restored relevant verbatim biochemical and localization evidence; did not restore label-only CHAIN features, unrelated introductory statements, or quotations that no longer support the revised claim. Existing source annotation fields were preserved.

Primary supplemental check for PMID:18431481: [annotated-protein workbook s005](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0001994.s005&type=supplementary), worksheet `supplTable5`, and [abundance workbook s003](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0001994.s003&type=supplementary), worksheet `supplTable1`, explicitly classify AT1G78370 as **"not plastid"**. Internal workbook titles and article table numbering differ, so file identifier plus locus are the stable join. These are direct reads of publisher supplements, not an inference from absent targeting signals. Working downloads are under `.cache/module-audit-logs/18431481-s003` and `18431481-s005`; source caches were not manually modified.

Read PMID:28887381 full text, especially "Identification of True Membrane-associated Proteins" and Fig. 7: washed microsomes and sucrose gradients distinguish membrane association but do not separate organelles; named compartments are imported from SUBAcon/GFP knowledge. The paper states "no organelle fell in a single cluster". Mark the specific compartment claim as over-annotated while preserving proteomic detection. This applies projects/ORGANELLES.md at the actual resolution of the assay.

Both GO:0019899 refinements now quote the FIN219–FIP1 adenylation-doubling result from PMID:28223489. PMID:18538804 remains abstract-only after force-fetch: GSTU20 apoplastic peptide identification/purity controls remain unresolved; unlike SUBAcon labels, this is a genuine access limitation.
