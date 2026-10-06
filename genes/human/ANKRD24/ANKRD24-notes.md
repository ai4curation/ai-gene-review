# ANKRD24 notes

- The defining study is Krey et al. 2022 JCB [PMID:35175278, full text, mouse]. ANKRD24 "concentrates at the stereocilia insertion point, forming a ring at the junction between the lower and upper rootlets", "surrounds and binds TRIOBP-5", and the knockout shows "progressive hearing loss". It has a membrane-binding N-terminus, and its coiled coils mediate self-association and TRIOBP binding. Rootlet localization is reciprocal: TRIOBP-5 recruits ANKRD24, and ANKRD24 sets the distribution of TRIOBP-5.
- TPRN (taperin) is upstream: without it, TRIOBP-5 and ANKRD24 are gradually lost from rootlets [PMID:40471101, full text].
- Human: a homozygous frameshift p.Thr645Lysfs*52 segregates with recessive NSHL in one Iranian family [PMID:39434538, abstract].
- HMGCS2/Tau autophagy [PMID:36442191, abstract only]: knockdown lowers LAMP1/LC3-II. Single study, model system not stated in the abstract; no GO drawn.
- Actin binding (IEA, InterPro IPR042420): there is no direct binding assay, and superresolution places ANKRD24 outside the TRIOBP layer ("ANKRD24 fills the actin-free region"). MARK_AS_OVER_ANNOTATED.
- Stereocilium (IEA, ISS) → MODIFY to GO:0120044 stereocilium base (rootlet). Adding it as NEW would have been a descendant of an existing term.
- NEW GO:0106006 cytoskeletal protein-membrane anchor activity (ISS from Q80VM7). The definition fits: ANKRD24 binds the membrane and TRIOBP-5 and holds TRIOBP-5 at the insertion point. ANKRD24 does the work itself (participation).
- PAINT: PTHR24129 node PTN002793001 carries only GO:0007605, seeded by mouse Ankrd24. Files committed.
- Affinage: trust gate tripped (pairwise tie); the narrative checks out against the papers.

## Round 2 (reviewer, PR #4105)

- Description: removed the repository-cache clause ("available here as an abstract only").
- Actin-binding reason now names the likely source of the IEA. IPR042420 is the InterPro integration of PTHR24129, and ANKRD24 shares subfamily SF0 with RAI14/ankycorbin, an actin-associated protein.
- Set full_text_unavailable on PMID:39434538 and PMID:36442191.
- Added an experiment: test N-terminal membrane binding directly.
- Kept actin binding as MARK_AS_OVER_ANNOTATED, with a separate NEW GO:0106006, instead of folding them into one MODIFY. The two rows rest on different evidence (InterPro family mapping vs mouse ISS).
- Checked whether human RAI14 (Q9P0K7) also receives GO:0007605 by IBA: QuickGO returns none, so PTN002793001 is not an SF0-wide node.
