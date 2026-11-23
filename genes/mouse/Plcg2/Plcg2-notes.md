

## 2026-10-26 full annotation audit: evidence review in progress

The preserved acquisition baseline and raw-file hashes are in `.cache/module-audit-logs/b-cell-panel-baseline.json`. This review covers all annotations, including functions outside B-cell signaling. Normal acquisition and actual provider attempts are recorded in `b-cell-acquisition-report.md` and `b-cell-fetch/provider-publication-results.json`; provider failures are not research reports. Existing genuine exact-target reports, where available, are discovery aids. Original machine annotation payloads and raw source records will be preserved.


## 2026-10-26 completed full annotation audit

Native mouse studies establish PLCγ2 in B-cell activation/survival and additional innate pathways: PMID:10925250 and PMID:12928432 for B cells; full PMID:19136564 for Dectin-1 and TLR2-stimulated calcium/immune responses; PMID:22041900 for Dectin-2/Candida signaling; PMID:22078883 for CD14/TLR4 endocytosis. Unsigned canonical NF-κB regulation rows are consistently refined to the positive contribution demonstrated in the relevant Dectin contexts. This does not imply a universal positive sign in every pathway.

Full PMID:23478294 directly fractionates lipid rafts after RANKL stimulation and detects PLCγ2 recruitment (Figure 6J); this supports native mouse raft localization independently of human EGF trafficking experiments. Rat RGD:3348 resolves to P24135. PMID:8958450 shows ATP/orthovanadate/Mg2+-supported kinase activation and PLCγ2 redistribution in RBL lysates, supporting qualified response terms rather than ATP binding or a magnesium cofactor assignment. PMID:31549850 shows rat BRL-3A proliferation/cell-cycle effects, but the accessible phase result is G2+M; the specific G1/S transfer remains unresolved.

T-cell receptor involvement remains unresolved for native mouse PLCγ2. PMID:15728238 uses pan-PLCγ inhibition, and full PMID:15509800 demonstrates PLCγ2 phosphorylation in engineered PLCγ1-deficient human Jurkat cells. Neither establishes an exclusive native mouse role or proves absence. The phosphatidylcholine-specific PLC Reactome claim also remains unresolved: the recovered source chain mixes phosphatidylcholine turnover/bacterial PLC experiments with PLCγ2 activation without resolving direct substrate specificity. Human and avian reconstitution evidence is explicitly distinguished from native mouse experiments.

All 141 original annotation payloads, including qualifiers and any negation flags, were preserved; no NEW assertions were added. Normal source acquisition and actual provider outcomes are retained in the acquisition logs. Failed provider calls were not replaced with fabricated reports. Source-access limits are recorded above and in the individual row reasons; partial publisher pages and captcha responses were not treated as full articles. The six-member focused strict/schema, GO-term and source-quotation check passed with zero errors and warnings before final packaging; the final package reruns those checks after finding additions. Record-section backfill, HTML rendering, helper-generated Codex provenance and exact payload/raw-hash checks accompany the package.


## PR 5584 source and scope follow-up

PMID8441394 was normally fetched and assessed as an explicit reference, closing the prose-only citation gap. Its abstract identifies added Bacillus cereus PC-PLC in murine BAC1.2F5 cells; it does not resolve purified native PLCgamma2 phosphatidylcholine specificity. Existing UNDECIDED action is retained.
