# gon-2 review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene worm gon-2`. UniProt Q93971 (TRPG_CAEEL), with 16 GOA rows. The literature
  synthesis is in `gon-2-deep-research-manual.md`; no deep-research provider was run.
- Cached the PubMed hits for "gon-2 elegans TRPM", including PMID:20221407 (GTL-2 / Mg2+ excretion) and the
  channel papers PMID:16054081, PMID:18299395 and PMID:19923421.
- Core function: a Ca2+-selective, Mg2+-permeable TRPM cation channel in the intestinal plasma membrane, and
  presumably in the gonadal precursors. The direct evidence is the patch clamp of intestinal cells from mutants
  [PMID:18299395 "GON-2, GTL-1, and the ORCa channels exhibit a >60-fold selectivity for Ca2+ over Na+"].
- Generic transport and channel rows (IEA/IBA/ISS) were MODIFIED to calcium channel activity and to calcium / magnesium
  ion transmembrane transport. The Mg2+ claim is weaker than the Ca2+ claim. Permeability is measured
  [PMID:18299395 "clearly have measurable Mg2+ permeabilities under bi-ionic conditions"], but whether
  the channel carries much Mg2+ in vivo is debated [PMID:20221407].
- The phenotype rows (mitotic cell cycle, gonad development, defecation) come from IMP/IGI evidence on abstract-only
  or full-text papers. All are kept as non-core. The channel most likely supports gonadal divisions by supplying
  cations (GEM-1 bypass, Mg2+ suppression), not as part of the cell-cycle machinery. Per the CLAUDE.md rules I did not
  overrule the experimental rows.
- Following the strict NEW-term bar, I added no NEW process terms (no magnesium homeostasis, no pathogen avoidance), because the
  evidence for them is genetic necessity only.
- Plasma membrane rows (IBA, ISS) were accepted. The support is whole-cell currents plus topology. No direct GON-2 protein
  localization was found.
