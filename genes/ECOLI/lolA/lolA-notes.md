# lolA (Escherichia coli K-12) review notes

## 2026-10-23

- Review created as an experimental exemplar for the reusable module
  `modules/bacterial_lol_lipoprotein_trafficking.yaml`; E. coli K-12 is the
  organism in which the LolCDE-LolA-LolB pathway was defined biochemically and
  genetically (Tokuda laboratory).
- Provider deep research was not generated: no deep-research provider API key
  is configured in this session. The review is based on the UniProt record,
  the GOA rows and the cached publications in `publications/`, most of which
  are abstract-only (`full_text_available: false`).
- GO has specific molecular-function terms for two Lol stages:
  GO:0140306 lipoprotein releasing activity (LolCDE; already annotated to
  E. coli LolC, LolD and LolE by IDA/IMP) and GO:0140598 lipoprotein carrier
  activity (LolA). No MF term exists for the LolB acceptance/insertion step.


## 2026-11-07: Lol comparative consultation

All existing annotations and core functions were reassessed against their cited cached literature, curated UniProt text, and relevant full primary texts. Ordered annotation payloads and immutable sources are preserved. The evidence/action ledger and access limits are in `analysis/module_audits/bacterial_lol_lipoprotein_trafficking/ecoli-consultation/evidence.md`.

An actual configured Falcon attempt for this gene failed with HTTP 403 authentication; no provider report was fabricated. The log is retained under `.cache/module-audit-logs/lol-20261107/ecoli-consultation/falcon-lolA.log`. Manual primary-source review supplies the evidence.

LolA is the soluble periplasmic carrier that transfers mature outer-membrane lipoproteins between LolCDE in the inner membrane and LolB at the outer membrane of Escherichia coli. Recruitment by the periplasmic domain of LolC enables cargo loading into LolA's hydrophobic cavity, which shields the lipid anchor during passage through the aqueous periplasm. LolA then delivers cargo to LolB for membrane insertion. LolCDE normally excludes inner-membrane retention substrates at the extraction step. LolA is essential in ordinary E. coli backgrounds, although conditional bypass of LolA and LolB is possible when lipoprotein toxicity and envelope stress responses are altered.

The publication-linked UniProt suggestion that LolA may regulate Rcs was checked against PMID:11758943: the accessible abstract reports multicopy-induced activation. This does not establish direct native regulatory activity, so no new regulatory annotation or core function is manufactured. The same UniProt citation does not independently establish its preceding transport statement; founding transport studies supply that evidence.
