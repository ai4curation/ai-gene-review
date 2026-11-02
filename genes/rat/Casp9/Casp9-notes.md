# Casp9 (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Casp9` resolved Q9JHK1 (RGD:61867, GeneID 58918), as expected;
  76 GOA rows seeded. `just fetch-gene-pmids` cached 14 PMIDs; PMID:16987298 cached
  separately (full text). Only PMID:16987298 and PMID:24089674 have full text; all
  other rat papers are abstract-only.
- No deep-research provider; literature synthesis written to
  `Casp9-deep-research-manual.md`.
- Bioinformatics (`Casp9-bioinformatics/RESULTS.md`): catalytic His275/Cys325
  conserved; ABL1 site conserved (rat Tyr191 = human Tyr153); AKT1 site Ser196 not
  conserved (rat Trp234). The Reactome rat projection "AKT phosphorylates targets in
  the cytosol" (R-RNO-198323) may therefore not apply to caspase-9 in rat.

### Decisions

- Core: GO:0004197 cysteine-type endopeptidase activity; part of apoptosome
  (GO:0043293) in cytosol; intrinsic apoptotic signaling pathway (GO:0097193);
  protein processing of executioner procaspases (GO:0016485); positive regulation of
  execution phase of apoptosis (GO:1900119). Basis: "Activated caspase-9 in turn
  cleaves and activates caspase-3" [PMID:9390557]; "directly cleaves/activates
  procaspase-7" [PMID:16352606].
- General terms refined: peptidase / cysteine-type peptidase activity -> GO:0004197;
  apoptotic process -> GO:0097193; DNA damage response -> GO:0008630; proteolysis and
  protein maturation -> GO:0016485; protein-containing complex -> GO:0043293;
  regulation / positive regulation of apoptotic process -> GO:1900119. Cytoplasm rows
  (IBA family-level, IDA immunohistochemistry) are accepted as precise as their evidence
  allows; cytosol is accepted on its own rows.
- IEP "response to X" rows (hypoxia, ischemia, cobalt, estradiol, LPS, ethanol,
  anesthetic, kidney development, leukocyte/glial apoptosis) are caspase activation
  used as a death marker: MARK_AS_OVER_ANNOTATED, not REMOVE.
- PMID:17869439 IMP positive regulation of apoptotic process: the abstract says
  caspase-9 inhibitors did NOT reduce hair cell loss ("but caspase-8 and -9 inhibitors
  did not"). Full text not available. The claim is true of the gene, so the row gets the
  same MODIFY (-> GO:1900119) as the term's other rows, and the doubt about the
  reference is recorded as a WRONG_REFERENCE CHECK source defect for RGD.
- PMID:17297389 response to indole-3-methanol carries IDA, but the abstract reports
  an activity increase after I3C treatment, an expression-pattern observation
  (IEP-like): MARK_AS_OVER_ANNOTATED plus WRONG_EVIDENCE_CODE CHECK.
- No NEW rows proposed: every process I considered (e.g. brain development, neuron
  apoptosis) is either already present or rests on necessity evidence only.
