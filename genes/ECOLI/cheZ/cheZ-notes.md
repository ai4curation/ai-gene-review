# cheZ (E. coli K-12, P0A9H9) review notes

## 2026-11-03 session

- Deep research: `just deep-research ECOLI cheZ --provider perplexity` failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist, claude_code").
  `just mod-description-deep-research ECOLI cheZ` skipped (no MOD provider for ECOLI).
  Review built from cached publications (mostly abstract-only; PMID:21496648 and
  PMID:30890609 are full text) and the UniProt record.
- Added PMID:10852888 and PMID:12644507 (UniProt-cited) to references and cached them with
  `just fetch-gene-pmids ECOLI cheZ`.

## Key evidence

- Activity: [PMID:17998207 "CheZ catalyzes the dephosphorylation of the response regulator CheY in the two-component regulatory system that mediates chemotaxis in Escherichia coli."]
  [PMID:17998207 "CheZ is a homodimer with two active sites for dephosphorylation."]
- Mechanism: [PMID:12080332 "The side chain of Gln 147 of CheZ inserts into the CheY active site and is essential to the dephosphorylation activity of CheZ."]
- Substrate selectivity: [PMID:8305438 "the binding to phosphorylated CheY is higher by over 2 orders of magnitude than the binding to nonphosphorylated CheY"]
- Localization: [PMID:12644507 "We conclude that CheZ localization requires the truncated C-terminal portion of the P1 domain present in CheA(S)."]
  [PMID:19502407 "CheA-short interacts with CheZ to localize CheZ to cell poles."]
- CheA-S stimulation: [PMID:8820640 "Finally, the CheAS/CheZ complex formed in vitro shows a greater dephosphorylating activity on CheY-P than does free CheZ."]
- Phenotype: [PMID:353036 "whereas cheB or cheZ mutants exhibited very high tumbling rates"]
- Swarming: [PMID:30890609 "The tumble bias response is very sensitive to CheZ expression, especially in liquid cultures."]

## Decisions

- Module MF GO:0004721 phosphoprotein phosphatase activity: SUPPORTED (IDA kinetics,
  structure/mutagenesis); used as core MF. No more specific GO child exists for
  response-regulator aspartyl-phosphate phosphatases (raised as suggested question).
- catalytic activity (IEA) -> MODIFY to GO:0004721 (as in PSEPK ortholog review).
- 10 protein binding IPI rows -> REMOVE (CheY-P binding is the enzyme-substrate interaction,
  captured by GO:0004721 / GO:0051219; CheA-S binding captured as location).
- cytoplasm IEA -> MODIFY to cytosol (IDA row present). plasma membrane IDA x2 -> MODIFY to
  GO:0009898 cytoplasmic side of plasma membrane (peripheral via CheA-S/receptor arrays; no TM).
- bacterial-type flagellum IEA (InterPro2GO IPR007439) -> REMOVE with source defect
  (CheZ localizes to receptor patches, not flagellum). NOTE: the PSEPK ortholog review
  currently uses MARK_AS_OVER_ANNOTATED for this row; harmonise if needed.
- NEW: GO:0060187 cell pole, IDA PMID:12644507 (CheZ-GFP polar localization).
- GO:0000160 phosphorelay signal transduction system: not added. CheZ acts on the response
  regulator's phosphoaspartate to terminate the relay output; whether that counts as
  participation is left as a suggested question rather than a NEW row.
