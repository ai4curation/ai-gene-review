# PRDX4 notes

## 2026-11-05 ORGANELLES ER batch 3 (endoplasmic reticulum rows)

Rows: GO:0005783 IBA (GO_REF:0000033; GOA qualifier is_active_in, not recorded in the review
row), IEA (GO_REF:0000120, SL-0095 + mouse O08807), IDA (GO_REF:0000052, HPA). No ER
sub-compartment rows before this pass.

Checks:
- PAINT: PTHR10681 node PTN000841180, GO:0005783 IBD seeded by FB:FBgn0040308 (Jafrac2),
  MGI:1859815, RGD:620043 and UniProtKB:Q13162 (PRDX4 itself; expected seed).
- UniProt Q13162: SIGNAL 1..37 (ECO:0000269|PubMed:19892738, N-terminal proteomics), no TM,
  no KDEL-type C-terminus (ends ...KYFDKLN). ER line ECO:0000269|PubMed:18052930.
- PMID:18052930 (Tavender et al. 2008, full text, fetched this pass):
  [PMID:18052930 "In contrast, the predominant form of Prx IV co-localised mainly with calnexin in the organellar fraction (lane 2, representing the membranes of the secretory pathway) and like the calnexin lumenal domain was again protected from proteinase K digestion (lane 3)."]
  [PMID:18052930 "The data indicate that native Prx IV is ER-retained in human cells even when over-produced, despite lacking a recognised retention/retrieval motif."]
  [PMID:18052930 "Interestingly Prx IV remained co-localised with ER markers for a full five hours after cycloheximide addition"]
  (anti-KDEL co-staining; no secretion detected from four cell lines).
- PMID:20627953 (Tavender & Bulleid 2010, abstract only, found by PubMed search
  "peroxiredoxin IV disulphide formation endoplasmic reticulum Tavender"):
  [PMID:20627953 "Here, we show that mammalian peroxiredoxin IV (PrxIV) metabolises hydrogen peroxide produced by Ero1."]

Outcome: the three root rows stay ACCEPT (core); reasons rewritten to record the check and the
non-verbatim falcon/UniProt quotes on these rows were replaced by verbatim ones. NEW
GO:0005788 ER lumen (IC, PMID:18052930): three lines agree (cleaved signal peptide with no
anchor; proteinase K protection inside calnexin-containing membranes; lumenal Ero1-coupled
peroxide removal). is_active_in is defensible: the peroxidase is shown acting in the ER.
core_functions locations gained GO:0005788 beside the root, because the activity itself is
shown there. Added PMID:18052930 and PMID:20627953 to references.
