# rab-7 review notes

## 2026-10-28 initial review

- Fetched Q23146 (unreviewed TrEMBL, W03C9.3); GOA had 27 rows. No deep-research API keys;
  literature summary written by hand in `rab-7-deep-research-manual.md`.
- Full text cached: PMID:10588660, 16801682, 18351800, 19915558, 20462958, 26783301, 23840591.
  Abstract-only: PMID:17203072, 17762880, 20921409, 38538795.
- Decisions:
  - GTPase activity (2 IDA + IEA), GTP binding, lysosome/late endosome/phagosome CC rows,
    endosome to lysosome transport, phagosome-lysosome fusion, phagolysosome assembly in
    apoptotic cell clearance: ACCEPT.
  - oocyte growth and body morphogenesis (PMID:10588660 RNAi): MARK_AS_OVER_ANNOTATED.
    The paper says rab-7 RNAi did not significantly impair yolk uptake
    [PMID:10588660 "Although Ce-rab7 (RNAi) did not appear to significantly impair the uptake of YP170::GFP into oocytes"];
    Dpy is "mild" and indirect. Table 1 not cached, so not REMOVE.
  - endosomal transport: MODIFY to GO:0045022 + GO:0008333.
  - organelle membrane (PMID:17203072): MODIFY to late endosome membrane.
  - organelle fusion (3 IGI rows, PMID:26783301): MODIFY to phagosome-lysosome fusion. The
    IGI data themselves are indirect: loss of rab-7 in sorf mutants causes excess early
    endosome fusion through persistent PtdIns3P.
  - positive regulation of early endosome to late endosome transport (IGI): MODIFY to the
    participation term GO:0045022; RAB-7 is the core Rab of the switch, not an upstream regulator.
  - protein localization to lysosome (HPO-27 recruitment): KEEP_AS_NON_CORE.
- No NEW rows. Fat storage (PMID:17762880) and embryonic lethality are necessity
  phenotypes, which do not meet the bar for a NEW process term.
