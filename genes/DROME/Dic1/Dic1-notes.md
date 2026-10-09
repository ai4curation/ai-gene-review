# Dic1 notes

- 2026-10-09: Initial review of Dic1 (Q9Y166; FBgn0027610), mitochondrial dicarboxylate carrier.
- Iacopetta et al. 2011 [PMID:21130726] (abstract only in cache): "DmDic1p is a typical dicarboxylate
  carrier showing similar substrate specificity and inhibitor sensitivity as mammalian and yeast
  mitochondrial dicarboxylate carriers."; carrier family "catalyzes an electroneutral exchange across
  the inner mitochondrial membrane of dicarboxylates for inorganic phosphate and certain
  sulfur-containing compounds"; "All expressed proteins are localized in mitochondria."
- All IDA substrate rows accepted in deference to the curator (full text not cached). IBA donors are
  fly Dic1 (FBgn0027610) and Dic3 (FBgn0033248).
- Added NEW GO:0015364 dicarboxylate:phosphate antiporter activity to capture the exchange mechanism.
- membrane IEA and mitochondrion IDA -> mitochondrial inner membrane. Gluconeogenesis NAS non-core.
- Falcon deep research (Dic1-deep-research-falcon.md, arrived after initial commit), summarizing the
  full text of PMID:21130726: Dic1 (CG8790) is a strict exchanger (malate/phosphate uptake needs an
  internal counter-substrate), which supports the NEW dicarboxylate:phosphate antiporter annotation;
  strong exchange with malate, phosphate, malonate and maleate; weaker exchange with succinate,
  sulfate, thiosulfate and oxaloacetate; Km malate 0.81 mM, phosphate 2.35 mM. Mitochondrial
  localization was reported as "data not shown". No annotation changes (weaker substrates kept as
  accepted curator IDA rows).
