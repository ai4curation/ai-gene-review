# ANKRD49 notes

- First described as FGIF (fetal globin-inducing factor). It has an N-terminal acidic domain with potent transactivation activity (yeast and COS assays) and three C-terminal ANK repeats, and it raises gamma-globin [PMID:11162141, PMID:16131492; abstracts]. Affinage missed this origin.
- Positive regulation of transcription (IDA ×2 and IBA): ACCEPT. The IBA node PTN009083995 is seeded only by ANKRD49 (NO_FAILURE_CORE). Nucleus (IEA, ISS, IC): ACCEPT. Mouse germ cells show predominantly nuclear ANKRD49 [PMID:26043108].
- NEW GO:0003713 transcription coactivator activity (IDA, PMID:11162141): an acidic TAD plus the physical PKNOX1 interaction driving TGF-B1 [PMID:41821002]. Limits are stated: fusion-construct assays, and promoter occupancy not tested.
- Protein binding:
  - HIF1AN ×5 → MODIFY to GO:0019899. FIH hydroxylates ankyrin repeats [PMID:17003112]; the pair is also seen by AP-MS.
  - RAN → MODIFY to GO:0031267 small GTPase binding. GO:0008536 Ran GTPase binding is merged into GO:0031267. Source: the RaDAR RanGDP-ankyrin import study [PMID:24855949].
  - FKBPL ×5 → REMOVE: reproducible across AP-MS and Y2H, but no informative term fits; raised as a question.
  - SMARCD1, ENKD1 (HuRI) → REMOVE.
- Phenotypes with no GO drawn: NF-kB-dependent autophagy in GC-1 cells and lung-cancer invasion/EMT.

## Round 2 (reviewer, PR #4136)

- The coactivator row now quotes both decisive PKNOX1 results. In support: Flag-PKNOX1 ChIP enrichment is higher in ANKRD49-overexpressing cells ("ANKRD49 strengthens the interaction"). Against: ANKRD49 overexpression also raises PKNOX1 mRNA and protein, so the effect could be abundance rather than coactivation. The reporter did not test ANKRD49 enhancement of PKNOX1 activity. The description and core function are softened accordingly, and the experiment now separates the two models.
- The HIF1AN rows have per-row provenance: one FIH screen plus four AP-MS studies, so 5 rows, not 4.
- GO:0008536 is now described as merged into GO:0031267.
- Cited PMID:37964204 and PMID:35775112 (LOW; signaling phenotypes). Added a SMARCD1/SWI-SNF suggested question.
