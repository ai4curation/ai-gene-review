# Ssu module checks and evidence limits

Run `uv run python modules/bacterial_alkanesulfonate_uptake_desulfonation-source-analysis/check_module.py` and `check_routes.py` from the repository root.

`check_module.py` invokes the production module validator with membership read independently from the 15 normally fetched UniProt records. It does not derive membership from the assertions being checked and does not download a release-wide PANTHER index. Official names remain checked against the local PANTHER ontology. Exact product selectors prevent broader family membership from conferring substrate specificity.

`check_routes.py` uses the production compiler with an oracle that requires every exact active unit for a complex atom. All three canonical routes, each missing component, singleton proteins, missing transport and 27 mixed-species transporter selections are checked. This is named-capability coverage, not a prediction of essentiality, expression, flux or whole-cell growth from gene presence.

The independently observed S-313 aliphatic-sulfonate activity without SsuE is reconciled through the production `module_logic.abduce` API (the name at the pinned repository version). The result must be `ABDUCTION_TARGET` at the missing reductase step. This records an unidentified reduced-FMN supplier or alternative route; it does not negate the native growth observation. The SsuF and alternate-uptake limitations remain explicit in module biology gaps.

Native identities are normally fetched records. S-313 identity is specifically AF075709: SsuE AAC31903.2, SsuA AAC31904.1, SsuD AAC31905.1, SsuC AAC31906.1 and SsuB AAC31907.1. Several UniProt entries merge other strains, which are not additional native S-313 experiments. The KT2440 thesis maps PP_0236–PP_0240 and is treated as unpublished primary genetic evidence, not as a peer-reviewed purified-enzyme study.

The cached full primary Table 1 in `publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC6295896_.md` supports similar E. coli SsuE NADH/NADPH rates. The S-313 heterologous extract experiment in PMID:10781557 instead reports no NADH activity under its conditions. Neither result is silently transferred to KT2440. PMID:26634408 supports interaction-assisted optimal flavin transfer with diffusion possible under specified conditions; no universally exclusive transfer mechanism is encoded.
