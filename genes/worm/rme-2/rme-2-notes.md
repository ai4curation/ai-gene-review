# rme-2 review notes

## Session 1 (create review)

- fetch-gene resolved O44191 (WormBase WBGene00004374, GeneID 177329), as expected; 16 GOA rows.
- Literature: Grant & Hirsh 1999 (PMID:10588660, full text) is the primary paper: RME-2 is the LDLR-family
  yolk receptor of the oocyte [PMID:10588660 "We show that RME-2 is the C. elegans yolk receptor."].
  Supporting localization papers: PMID:15895077 (immuno-EM, PM/endosome cycling), PMID:19798448 (PM),
  PMID:22768351 (VHA-19 needed for RME-2 delivery to PM), PMID:23840591 (RME-2 degraded after
  fertilization). PMID:15456850 and PMID:17234175 are abstract-only and do not mention RME-2 in the abstract.
- No deep-research provider available; manual synthesis in `rme-2-deep-research-manual.md`.

### Decisions
- GO:0005041 LDL particle receptor activity (IDA): lateral MODIFY to GO:0008196 vitellogenin receptor
  activity; the ligand shown is yolk (vitellogenin), not LDL. Recorded as a WRONG_TERM source defect (WB),
  PROBABLE.
- GO:0016192 vesicle-mediated transport (IEA, inter-ontology from GO:0005041): MODIFY to GO:0061883
  clathrin-dependent endocytosis involved in vitellogenesis. RME-2 is the cargo receptor that does the work
  of this process (binds and internalizes the cargo), so it passes the "does the work" bar; clathrin
  dependence shown by Ce-chc RNAi.
- PM rows: ACCEPT (core location of the receptor activity). Endosome membrane: ACCEPT.
- Cytoplasmic vesicle rows: KEEP_AS_NON_CORE (assay cannot resolve the compartment further).
- Membrane / endomembrane system IEA: MODIFY to plasma membrane + endosome membrane.
- Calcium ion binding IEA (EGF-Ca/LDLR-A motifs): KEEP_AS_NON_CORE, structural, not shown experimentally.
- Developmental IMP rows: embryo development and oocyte development KEEP_AS_NON_CORE (downstream of yolk
  provisioning); ovulation MARK_AS_OVER_ANNOTATED (indirect; no evidence RME-2 acts in spermatheca, and
  RME-2 is not detected outside the germline/embryo).
- No NEW process terms beyond the MODIFY replacement; vitellogenesis-type terms not added as NEW.
