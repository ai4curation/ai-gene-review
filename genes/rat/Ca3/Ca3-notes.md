# Ca3 (rat, P14141) review notes

## 2026-10-28 initial review

- Fetched with `just fetch-gene rat Ca3`; UniProt P14141 (CAH3_RAT), RGD:2241, GeneID 54232 - matches.
- No deep-research provider available; literature synthesis in `Ca3-deep-research-manual.md`.
- Additional papers cached: PMID:10845711 (phosphatase is extrinsic), PMID:15509796 (Car3 KO mouse),
  PMID:11024467 (crystal structure, glutathiolated Cys), PMID:8476041 (adipocyte CA III), PMID:9020864
  (mouse Ni-binding, source of the ISO nickel row).

### Key decisions

- Core function: carbonate dehydratase activity in the cytosol (low turnover but genuine;
  [PMID:10845711 "The purified recombinant had the same specific activity as the carbonic anhydrase purified from rat liver"]).
- GO:0016791 phosphatase activity (IDA, PMID:8633035) is refuted by the same laboratory
  [PMID:10845711 "We conclude that the phosphatase activity previously considered to be intrinsic to carbonic anhydrase III is actually extrinsic."].
  REMOVE with a source_defects entry and a finding_review on PMID:8633035. Flag for expert because it
  is an experimental row whose full text was not read.
- Sarcomere IDA (PMID:3133407): the abstract concludes CA III is randomly distributed in the cytoplasm
  and not associated with myofibrils; MODIFY to cytosol, source defect WRONG_TERM.
- Cytoplasm rows MODIFY to cytosol (more specific, gene already carries IDA cytosol rows).
- Oxidative-stress protection: supported by rat overexpression (PMID:10064618) and knockdown
  (PMID:29559661), but Car3-null mice have normal hyperoxia response (PMID:15509796). Kept as non-core.
- IEP expression rows (insulin, leptin, hypoxia, lipid, ethanol): KEEP_AS_NON_CORE; response to alcohol
  MODIFY to response to ethanol. Skeletal muscle contraction IEP (leakage during contraction) and liver
  regeneration IDA (arginine methylation substrate) marked over-annotated.
- No NEW terms proposed. Antioxidant activity was considered and rejected as a NEW MF: mechanism
  (scavenging via reactive Cys / glutathionylation) is not established and the KO mouse is normal.
