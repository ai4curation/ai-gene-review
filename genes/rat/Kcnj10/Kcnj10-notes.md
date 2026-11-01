# Kcnj10 (rat) review notes

## Session 1 (2026-10-28)

- Fetched with `just fetch-gene rat Kcnj10`; UniProt P49655 (KCJ10_RAT, Swiss-Prot,
  RGD:61822, GeneID 29718) matches the requested accession. 49 GOA rows.
- No deep-research provider available; literature synthesis written by hand in
  `Kcnj10-deep-research-manual.md`.
- Most GOA experimental references are abstract-only in the cache (16206160, 17091490, 18303016,
  18395087, 18450590, 19931615, 20466875, 20833221); full text read for 15198689, 21084311,
  19665991, 17942730, 26546361, 31736353.
- PMID:19665991 (Shang et al. 2009) is about Xenopus tropicalis Kir5.1 but uses rat Kir4.1
  as a reference throughout: rat Kir4.1 homomers give inward rectifier currents, rat
  Kir4.1/Kir5.1 tandems give heteromeric channels with sublevels [PMID:19665991 "Fig. 2C shows
  that ratKir4.1/XtKir5.1 heteromeric channels also exhibited markedly long S1 sublevels"].
  It supports the core MF; not in GOA.

### Decisions

- GO:0005242 rows (IBA contributes_to, IEA, ISO): ACCEPT. Rat Kir4.1 makes homomeric channels
  [PMID:7608203], and contributes to Kir4.1/Kir5.1 heteromers, so both enables and
  contributes_to hold.
- GO:0005267, GO:0006813, GO:0016020, GO:0042391 general rows: MODIFY to the specific terms the
  gene already carries (GO:0005242, GO:0071805, GO:0005886/GO:0016323, GO:0060075).
- GO:0005515 MLC1 pull-down: REMOVE per protein-binding policy.
- GO:0098793 presynapse IEA: REMOVE. Derived by inter-ontology logic from glutamate reuptake,
  itself an indirect annotation; Kir4.1 is glial (astrocytes, oligodendrocytes, Mueller cells)
  [PMID:15310750 "Kir4.1/5.1 and Kir4.1 expression appeared to occur only in astrocytes"].
- Glutamate uptake rows (IMP rat, ISO mouse): MARK_AS_OVER_ANNOTATED. Kir4.1 does not move
  glutamate; the effect is through membrane hyperpolarisation driving EAATs, which the
  authors themselves say.
- Myelination, oligodendrocyte development, walking behaviour, visual perception, synaptic
  plasticity, non-motile cilium assembly: MARK_AS_OVER_ANNOTATED (knockout/knockdown
  phenotypes; necessity, not participation).
- IEP rows (blue light, mineralocorticoid, optic nerve development): MARK_AS_OVER_ANNOTATED;
  response to glucocorticoid UNDECIDED: the abstract reports only aldosterone as stimulus, acting
  through MR and GR; whether a glucocorticoid was tested needs the full text.
- NEW: GO:0097450 astrocyte end-foot (IDA PMID:15198689, rat optic nerve full text) and
  GO:0005546 PIP2 binding (rat cryo-EM, PMID:38355723 via UniProt FT BINDING).
- No NEW process terms.
